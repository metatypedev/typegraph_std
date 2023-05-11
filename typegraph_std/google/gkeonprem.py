from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_gkeonprem() -> Import:
    gkeonprem = HTTPRuntime("https://gkeonprem.googleapis.com/")

    renames = {
        "ErrorResponse": "_gkeonprem_1_ErrorResponse",
        "VmwareAdminControlPlaneNodeConfigIn": "_gkeonprem_2_VmwareAdminControlPlaneNodeConfigIn",
        "VmwareAdminControlPlaneNodeConfigOut": "_gkeonprem_3_VmwareAdminControlPlaneNodeConfigOut",
        "ListBareMetalClustersResponseIn": "_gkeonprem_4_ListBareMetalClustersResponseIn",
        "ListBareMetalClustersResponseOut": "_gkeonprem_5_ListBareMetalClustersResponseOut",
        "ListBareMetalAdminClustersResponseIn": "_gkeonprem_6_ListBareMetalAdminClustersResponseIn",
        "ListBareMetalAdminClustersResponseOut": "_gkeonprem_7_ListBareMetalAdminClustersResponseOut",
        "BareMetalAdminStorageConfigIn": "_gkeonprem_8_BareMetalAdminStorageConfigIn",
        "BareMetalAdminStorageConfigOut": "_gkeonprem_9_BareMetalAdminStorageConfigOut",
        "BareMetalNodePoolIn": "_gkeonprem_10_BareMetalNodePoolIn",
        "BareMetalNodePoolOut": "_gkeonprem_11_BareMetalNodePoolOut",
        "BareMetalControlPlaneNodePoolConfigIn": "_gkeonprem_12_BareMetalControlPlaneNodePoolConfigIn",
        "BareMetalControlPlaneNodePoolConfigOut": "_gkeonprem_13_BareMetalControlPlaneNodePoolConfigOut",
        "PolicyIn": "_gkeonprem_14_PolicyIn",
        "PolicyOut": "_gkeonprem_15_PolicyOut",
        "AuthorizationIn": "_gkeonprem_16_AuthorizationIn",
        "AuthorizationOut": "_gkeonprem_17_AuthorizationOut",
        "BareMetalBgpPeerConfigIn": "_gkeonprem_18_BareMetalBgpPeerConfigIn",
        "BareMetalBgpPeerConfigOut": "_gkeonprem_19_BareMetalBgpPeerConfigOut",
        "EnrollBareMetalAdminClusterRequestIn": "_gkeonprem_20_EnrollBareMetalAdminClusterRequestIn",
        "EnrollBareMetalAdminClusterRequestOut": "_gkeonprem_21_EnrollBareMetalAdminClusterRequestOut",
        "OperationIn": "_gkeonprem_22_OperationIn",
        "OperationOut": "_gkeonprem_23_OperationOut",
        "ResourceConditionIn": "_gkeonprem_24_ResourceConditionIn",
        "ResourceConditionOut": "_gkeonprem_25_ResourceConditionOut",
        "VmwareAdminF5BigIpConfigIn": "_gkeonprem_26_VmwareAdminF5BigIpConfigIn",
        "VmwareAdminF5BigIpConfigOut": "_gkeonprem_27_VmwareAdminF5BigIpConfigOut",
        "ExprIn": "_gkeonprem_28_ExprIn",
        "ExprOut": "_gkeonprem_29_ExprOut",
        "EnrollVmwareClusterRequestIn": "_gkeonprem_30_EnrollVmwareClusterRequestIn",
        "EnrollVmwareClusterRequestOut": "_gkeonprem_31_EnrollVmwareClusterRequestOut",
        "BareMetalAdminNetworkConfigIn": "_gkeonprem_32_BareMetalAdminNetworkConfigIn",
        "BareMetalAdminNetworkConfigOut": "_gkeonprem_33_BareMetalAdminNetworkConfigOut",
        "BareMetalAdminDrainingMachineIn": "_gkeonprem_34_BareMetalAdminDrainingMachineIn",
        "BareMetalAdminDrainingMachineOut": "_gkeonprem_35_BareMetalAdminDrainingMachineOut",
        "BareMetalAdminControlPlaneNodePoolConfigIn": "_gkeonprem_36_BareMetalAdminControlPlaneNodePoolConfigIn",
        "BareMetalAdminControlPlaneNodePoolConfigOut": "_gkeonprem_37_BareMetalAdminControlPlaneNodePoolConfigOut",
        "EmptyIn": "_gkeonprem_38_EmptyIn",
        "EmptyOut": "_gkeonprem_39_EmptyOut",
        "BareMetalMaintenanceStatusIn": "_gkeonprem_40_BareMetalMaintenanceStatusIn",
        "BareMetalMaintenanceStatusOut": "_gkeonprem_41_BareMetalMaintenanceStatusOut",
        "VmwareControlPlaneVsphereConfigIn": "_gkeonprem_42_VmwareControlPlaneVsphereConfigIn",
        "VmwareControlPlaneVsphereConfigOut": "_gkeonprem_43_VmwareControlPlaneVsphereConfigOut",
        "BareMetalAdminWorkloadNodeConfigIn": "_gkeonprem_44_BareMetalAdminWorkloadNodeConfigIn",
        "BareMetalAdminWorkloadNodeConfigOut": "_gkeonprem_45_BareMetalAdminWorkloadNodeConfigOut",
        "BareMetalWorkloadNodeConfigIn": "_gkeonprem_46_BareMetalWorkloadNodeConfigIn",
        "BareMetalWorkloadNodeConfigOut": "_gkeonprem_47_BareMetalWorkloadNodeConfigOut",
        "VmwareBundleConfigIn": "_gkeonprem_48_VmwareBundleConfigIn",
        "VmwareBundleConfigOut": "_gkeonprem_49_VmwareBundleConfigOut",
        "BareMetalAdminManualLbConfigIn": "_gkeonprem_50_BareMetalAdminManualLbConfigIn",
        "BareMetalAdminManualLbConfigOut": "_gkeonprem_51_BareMetalAdminManualLbConfigOut",
        "VmwareVsphereTagIn": "_gkeonprem_52_VmwareVsphereTagIn",
        "VmwareVsphereTagOut": "_gkeonprem_53_VmwareVsphereTagOut",
        "ListOperationsResponseIn": "_gkeonprem_54_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_gkeonprem_55_ListOperationsResponseOut",
        "BareMetalLoadBalancerNodePoolConfigIn": "_gkeonprem_56_BareMetalLoadBalancerNodePoolConfigIn",
        "BareMetalLoadBalancerNodePoolConfigOut": "_gkeonprem_57_BareMetalLoadBalancerNodePoolConfigOut",
        "EnrollVmwareAdminClusterRequestIn": "_gkeonprem_58_EnrollVmwareAdminClusterRequestIn",
        "EnrollVmwareAdminClusterRequestOut": "_gkeonprem_59_EnrollVmwareAdminClusterRequestOut",
        "BareMetalApiServerArgumentIn": "_gkeonprem_60_BareMetalApiServerArgumentIn",
        "BareMetalApiServerArgumentOut": "_gkeonprem_61_BareMetalApiServerArgumentOut",
        "BareMetalManualLbConfigIn": "_gkeonprem_62_BareMetalManualLbConfigIn",
        "BareMetalManualLbConfigOut": "_gkeonprem_63_BareMetalManualLbConfigOut",
        "VmwareMetalLbConfigIn": "_gkeonprem_64_VmwareMetalLbConfigIn",
        "VmwareMetalLbConfigOut": "_gkeonprem_65_VmwareMetalLbConfigOut",
        "VmwareAdminManualLbConfigIn": "_gkeonprem_66_VmwareAdminManualLbConfigIn",
        "VmwareAdminManualLbConfigOut": "_gkeonprem_67_VmwareAdminManualLbConfigOut",
        "VmwareHostConfigIn": "_gkeonprem_68_VmwareHostConfigIn",
        "VmwareHostConfigOut": "_gkeonprem_69_VmwareHostConfigOut",
        "BareMetalDrainingMachineIn": "_gkeonprem_70_BareMetalDrainingMachineIn",
        "BareMetalDrainingMachineOut": "_gkeonprem_71_BareMetalDrainingMachineOut",
        "BareMetalMaintenanceConfigIn": "_gkeonprem_72_BareMetalMaintenanceConfigIn",
        "BareMetalMaintenanceConfigOut": "_gkeonprem_73_BareMetalMaintenanceConfigOut",
        "TestIamPermissionsResponseIn": "_gkeonprem_74_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_gkeonprem_75_TestIamPermissionsResponseOut",
        "TestIamPermissionsRequestIn": "_gkeonprem_76_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_gkeonprem_77_TestIamPermissionsRequestOut",
        "VmwareAutoRepairConfigIn": "_gkeonprem_78_VmwareAutoRepairConfigIn",
        "VmwareAutoRepairConfigOut": "_gkeonprem_79_VmwareAutoRepairConfigOut",
        "VmwareNodePoolAutoscalingConfigIn": "_gkeonprem_80_VmwareNodePoolAutoscalingConfigIn",
        "VmwareNodePoolAutoscalingConfigOut": "_gkeonprem_81_VmwareNodePoolAutoscalingConfigOut",
        "BareMetalMachineDrainStatusIn": "_gkeonprem_82_BareMetalMachineDrainStatusIn",
        "BareMetalMachineDrainStatusOut": "_gkeonprem_83_BareMetalMachineDrainStatusOut",
        "BareMetalLoadBalancerAddressPoolIn": "_gkeonprem_84_BareMetalLoadBalancerAddressPoolIn",
        "BareMetalLoadBalancerAddressPoolOut": "_gkeonprem_85_BareMetalLoadBalancerAddressPoolOut",
        "ClusterUserIn": "_gkeonprem_86_ClusterUserIn",
        "ClusterUserOut": "_gkeonprem_87_ClusterUserOut",
        "VmwareAAGConfigIn": "_gkeonprem_88_VmwareAAGConfigIn",
        "VmwareAAGConfigOut": "_gkeonprem_89_VmwareAAGConfigOut",
        "VmwareAddressPoolIn": "_gkeonprem_90_VmwareAddressPoolIn",
        "VmwareAddressPoolOut": "_gkeonprem_91_VmwareAddressPoolOut",
        "QueryBareMetalVersionConfigResponseIn": "_gkeonprem_92_QueryBareMetalVersionConfigResponseIn",
        "QueryBareMetalVersionConfigResponseOut": "_gkeonprem_93_QueryBareMetalVersionConfigResponseOut",
        "BareMetalDrainedMachineIn": "_gkeonprem_94_BareMetalDrainedMachineIn",
        "BareMetalDrainedMachineOut": "_gkeonprem_95_BareMetalDrainedMachineOut",
        "ListVmwareNodePoolsResponseIn": "_gkeonprem_96_ListVmwareNodePoolsResponseIn",
        "ListVmwareNodePoolsResponseOut": "_gkeonprem_97_ListVmwareNodePoolsResponseOut",
        "BareMetalLvpConfigIn": "_gkeonprem_98_BareMetalLvpConfigIn",
        "BareMetalLvpConfigOut": "_gkeonprem_99_BareMetalLvpConfigOut",
        "BareMetalAdminMaintenanceConfigIn": "_gkeonprem_100_BareMetalAdminMaintenanceConfigIn",
        "BareMetalAdminMaintenanceConfigOut": "_gkeonprem_101_BareMetalAdminMaintenanceConfigOut",
        "VmwareVCenterConfigIn": "_gkeonprem_102_VmwareVCenterConfigIn",
        "VmwareVCenterConfigOut": "_gkeonprem_103_VmwareVCenterConfigOut",
        "BareMetalAdminOsEnvironmentConfigIn": "_gkeonprem_104_BareMetalAdminOsEnvironmentConfigIn",
        "BareMetalAdminOsEnvironmentConfigOut": "_gkeonprem_105_BareMetalAdminOsEnvironmentConfigOut",
        "VmwareManualLbConfigIn": "_gkeonprem_106_VmwareManualLbConfigIn",
        "VmwareManualLbConfigOut": "_gkeonprem_107_VmwareManualLbConfigOut",
        "QueryBareMetalAdminVersionConfigResponseIn": "_gkeonprem_108_QueryBareMetalAdminVersionConfigResponseIn",
        "QueryBareMetalAdminVersionConfigResponseOut": "_gkeonprem_109_QueryBareMetalAdminVersionConfigResponseOut",
        "VmwarePlatformConfigIn": "_gkeonprem_110_VmwarePlatformConfigIn",
        "VmwarePlatformConfigOut": "_gkeonprem_111_VmwarePlatformConfigOut",
        "VmwareVsphereConfigIn": "_gkeonprem_112_VmwareVsphereConfigIn",
        "VmwareVsphereConfigOut": "_gkeonprem_113_VmwareVsphereConfigOut",
        "VmwareAutoResizeConfigIn": "_gkeonprem_114_VmwareAutoResizeConfigIn",
        "VmwareAutoResizeConfigOut": "_gkeonprem_115_VmwareAutoResizeConfigOut",
        "BareMetalAdminMachineDrainStatusIn": "_gkeonprem_116_BareMetalAdminMachineDrainStatusIn",
        "BareMetalAdminMachineDrainStatusOut": "_gkeonprem_117_BareMetalAdminMachineDrainStatusOut",
        "BareMetalAdminControlPlaneConfigIn": "_gkeonprem_118_BareMetalAdminControlPlaneConfigIn",
        "BareMetalAdminControlPlaneConfigOut": "_gkeonprem_119_BareMetalAdminControlPlaneConfigOut",
        "ValidationCheckIn": "_gkeonprem_120_ValidationCheckIn",
        "ValidationCheckOut": "_gkeonprem_121_ValidationCheckOut",
        "BareMetalAdminClusterIn": "_gkeonprem_122_BareMetalAdminClusterIn",
        "BareMetalAdminClusterOut": "_gkeonprem_123_BareMetalAdminClusterOut",
        "BareMetalLoadBalancerConfigIn": "_gkeonprem_124_BareMetalLoadBalancerConfigIn",
        "BareMetalLoadBalancerConfigOut": "_gkeonprem_125_BareMetalLoadBalancerConfigOut",
        "VmwareDhcpIpConfigIn": "_gkeonprem_126_VmwareDhcpIpConfigIn",
        "VmwareDhcpIpConfigOut": "_gkeonprem_127_VmwareDhcpIpConfigOut",
        "VmwareLoadBalancerConfigIn": "_gkeonprem_128_VmwareLoadBalancerConfigIn",
        "VmwareLoadBalancerConfigOut": "_gkeonprem_129_VmwareLoadBalancerConfigOut",
        "BareMetalAdminNodeAccessConfigIn": "_gkeonprem_130_BareMetalAdminNodeAccessConfigIn",
        "BareMetalAdminNodeAccessConfigOut": "_gkeonprem_131_BareMetalAdminNodeAccessConfigOut",
        "VmwareControlPlaneNodeConfigIn": "_gkeonprem_132_VmwareControlPlaneNodeConfigIn",
        "VmwareControlPlaneNodeConfigOut": "_gkeonprem_133_VmwareControlPlaneNodeConfigOut",
        "BareMetalAdminPortConfigIn": "_gkeonprem_134_BareMetalAdminPortConfigIn",
        "BareMetalAdminPortConfigOut": "_gkeonprem_135_BareMetalAdminPortConfigOut",
        "BareMetalClusterIn": "_gkeonprem_136_BareMetalClusterIn",
        "BareMetalClusterOut": "_gkeonprem_137_BareMetalClusterOut",
        "VmwareStorageConfigIn": "_gkeonprem_138_VmwareStorageConfigIn",
        "VmwareStorageConfigOut": "_gkeonprem_139_VmwareStorageConfigOut",
        "CancelOperationRequestIn": "_gkeonprem_140_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_gkeonprem_141_CancelOperationRequestOut",
        "BareMetalKubeletConfigIn": "_gkeonprem_142_BareMetalKubeletConfigIn",
        "BareMetalKubeletConfigOut": "_gkeonprem_143_BareMetalKubeletConfigOut",
        "VmwareAdminVipConfigIn": "_gkeonprem_144_VmwareAdminVipConfigIn",
        "VmwareAdminVipConfigOut": "_gkeonprem_145_VmwareAdminVipConfigOut",
        "VmwareVersionInfoIn": "_gkeonprem_146_VmwareVersionInfoIn",
        "VmwareVersionInfoOut": "_gkeonprem_147_VmwareVersionInfoOut",
        "VmwareNodePoolIn": "_gkeonprem_148_VmwareNodePoolIn",
        "VmwareNodePoolOut": "_gkeonprem_149_VmwareNodePoolOut",
        "VmwareAdminVCenterConfigIn": "_gkeonprem_150_VmwareAdminVCenterConfigIn",
        "VmwareAdminVCenterConfigOut": "_gkeonprem_151_VmwareAdminVCenterConfigOut",
        "FleetIn": "_gkeonprem_152_FleetIn",
        "FleetOut": "_gkeonprem_153_FleetOut",
        "ListVmwareClustersResponseIn": "_gkeonprem_154_ListVmwareClustersResponseIn",
        "ListVmwareClustersResponseOut": "_gkeonprem_155_ListVmwareClustersResponseOut",
        "BareMetalPortConfigIn": "_gkeonprem_156_BareMetalPortConfigIn",
        "BareMetalPortConfigOut": "_gkeonprem_157_BareMetalPortConfigOut",
        "BareMetalProxyConfigIn": "_gkeonprem_158_BareMetalProxyConfigIn",
        "BareMetalProxyConfigOut": "_gkeonprem_159_BareMetalProxyConfigOut",
        "BareMetalIslandModeCidrConfigIn": "_gkeonprem_160_BareMetalIslandModeCidrConfigIn",
        "BareMetalIslandModeCidrConfigOut": "_gkeonprem_161_BareMetalIslandModeCidrConfigOut",
        "QueryVmwareVersionConfigResponseIn": "_gkeonprem_162_QueryVmwareVersionConfigResponseIn",
        "QueryVmwareVersionConfigResponseOut": "_gkeonprem_163_QueryVmwareVersionConfigResponseOut",
        "ValidationCheckResultIn": "_gkeonprem_164_ValidationCheckResultIn",
        "ValidationCheckResultOut": "_gkeonprem_165_ValidationCheckResultOut",
        "VmwareDataplaneV2ConfigIn": "_gkeonprem_166_VmwareDataplaneV2ConfigIn",
        "VmwareDataplaneV2ConfigOut": "_gkeonprem_167_VmwareDataplaneV2ConfigOut",
        "OperationMetadataIn": "_gkeonprem_168_OperationMetadataIn",
        "OperationMetadataOut": "_gkeonprem_169_OperationMetadataOut",
        "VmwareControlPlaneV2ConfigIn": "_gkeonprem_170_VmwareControlPlaneV2ConfigIn",
        "VmwareControlPlaneV2ConfigOut": "_gkeonprem_171_VmwareControlPlaneV2ConfigOut",
        "BareMetalNodeAccessConfigIn": "_gkeonprem_172_BareMetalNodeAccessConfigIn",
        "BareMetalNodeAccessConfigOut": "_gkeonprem_173_BareMetalNodeAccessConfigOut",
        "BareMetalMultipleNetworkInterfacesConfigIn": "_gkeonprem_174_BareMetalMultipleNetworkInterfacesConfigIn",
        "BareMetalMultipleNetworkInterfacesConfigOut": "_gkeonprem_175_BareMetalMultipleNetworkInterfacesConfigOut",
        "NodeTaintIn": "_gkeonprem_176_NodeTaintIn",
        "NodeTaintOut": "_gkeonprem_177_NodeTaintOut",
        "VmwareNodeConfigIn": "_gkeonprem_178_VmwareNodeConfigIn",
        "VmwareNodeConfigOut": "_gkeonprem_179_VmwareNodeConfigOut",
        "BareMetalLvpShareConfigIn": "_gkeonprem_180_BareMetalLvpShareConfigIn",
        "BareMetalLvpShareConfigOut": "_gkeonprem_181_BareMetalLvpShareConfigOut",
        "BareMetalOsEnvironmentConfigIn": "_gkeonprem_182_BareMetalOsEnvironmentConfigIn",
        "BareMetalOsEnvironmentConfigOut": "_gkeonprem_183_BareMetalOsEnvironmentConfigOut",
        "EnrollBareMetalNodePoolRequestIn": "_gkeonprem_184_EnrollBareMetalNodePoolRequestIn",
        "EnrollBareMetalNodePoolRequestOut": "_gkeonprem_185_EnrollBareMetalNodePoolRequestOut",
        "VmwareNetworkConfigIn": "_gkeonprem_186_VmwareNetworkConfigIn",
        "VmwareNetworkConfigOut": "_gkeonprem_187_VmwareNetworkConfigOut",
        "VmwareAdminAddonNodeConfigIn": "_gkeonprem_188_VmwareAdminAddonNodeConfigIn",
        "VmwareAdminAddonNodeConfigOut": "_gkeonprem_189_VmwareAdminAddonNodeConfigOut",
        "VmwareHostIpIn": "_gkeonprem_190_VmwareHostIpIn",
        "VmwareHostIpOut": "_gkeonprem_191_VmwareHostIpOut",
        "BareMetalStorageConfigIn": "_gkeonprem_192_BareMetalStorageConfigIn",
        "BareMetalStorageConfigOut": "_gkeonprem_193_BareMetalStorageConfigOut",
        "VmwareAdminNetworkConfigIn": "_gkeonprem_194_VmwareAdminNetworkConfigIn",
        "VmwareAdminNetworkConfigOut": "_gkeonprem_195_VmwareAdminNetworkConfigOut",
        "BareMetalAdminSecurityConfigIn": "_gkeonprem_196_BareMetalAdminSecurityConfigIn",
        "BareMetalAdminSecurityConfigOut": "_gkeonprem_197_BareMetalAdminSecurityConfigOut",
        "SetIamPolicyRequestIn": "_gkeonprem_198_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_gkeonprem_199_SetIamPolicyRequestOut",
        "VmwareVipConfigIn": "_gkeonprem_200_VmwareVipConfigIn",
        "VmwareVipConfigOut": "_gkeonprem_201_VmwareVipConfigOut",
        "StatusIn": "_gkeonprem_202_StatusIn",
        "StatusOut": "_gkeonprem_203_StatusOut",
        "ListLocationsResponseIn": "_gkeonprem_204_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_gkeonprem_205_ListLocationsResponseOut",
        "BareMetalVipConfigIn": "_gkeonprem_206_BareMetalVipConfigIn",
        "BareMetalVipConfigOut": "_gkeonprem_207_BareMetalVipConfigOut",
        "BareMetalAdminClusterOperationsConfigIn": "_gkeonprem_208_BareMetalAdminClusterOperationsConfigIn",
        "BareMetalAdminClusterOperationsConfigOut": "_gkeonprem_209_BareMetalAdminClusterOperationsConfigOut",
        "VmwareAdminLoadBalancerConfigIn": "_gkeonprem_210_VmwareAdminLoadBalancerConfigIn",
        "VmwareAdminLoadBalancerConfigOut": "_gkeonprem_211_VmwareAdminLoadBalancerConfigOut",
        "EnrollBareMetalClusterRequestIn": "_gkeonprem_212_EnrollBareMetalClusterRequestIn",
        "EnrollBareMetalClusterRequestOut": "_gkeonprem_213_EnrollBareMetalClusterRequestOut",
        "ListBareMetalNodePoolsResponseIn": "_gkeonprem_214_ListBareMetalNodePoolsResponseIn",
        "ListBareMetalNodePoolsResponseOut": "_gkeonprem_215_ListBareMetalNodePoolsResponseOut",
        "BareMetalSecurityConfigIn": "_gkeonprem_216_BareMetalSecurityConfigIn",
        "BareMetalSecurityConfigOut": "_gkeonprem_217_BareMetalSecurityConfigOut",
        "BareMetalMetalLbConfigIn": "_gkeonprem_218_BareMetalMetalLbConfigIn",
        "BareMetalMetalLbConfigOut": "_gkeonprem_219_BareMetalMetalLbConfigOut",
        "BareMetalBgpLbConfigIn": "_gkeonprem_220_BareMetalBgpLbConfigIn",
        "BareMetalBgpLbConfigOut": "_gkeonprem_221_BareMetalBgpLbConfigOut",
        "BareMetalAdminMaintenanceStatusIn": "_gkeonprem_222_BareMetalAdminMaintenanceStatusIn",
        "BareMetalAdminMaintenanceStatusOut": "_gkeonprem_223_BareMetalAdminMaintenanceStatusOut",
        "BareMetalNetworkConfigIn": "_gkeonprem_224_BareMetalNetworkConfigIn",
        "BareMetalNetworkConfigOut": "_gkeonprem_225_BareMetalNetworkConfigOut",
        "EnrollVmwareNodePoolRequestIn": "_gkeonprem_226_EnrollVmwareNodePoolRequestIn",
        "EnrollVmwareNodePoolRequestOut": "_gkeonprem_227_EnrollVmwareNodePoolRequestOut",
        "VmwareClusterIn": "_gkeonprem_228_VmwareClusterIn",
        "VmwareClusterOut": "_gkeonprem_229_VmwareClusterOut",
        "BareMetalSrIovConfigIn": "_gkeonprem_230_BareMetalSrIovConfigIn",
        "BareMetalSrIovConfigOut": "_gkeonprem_231_BareMetalSrIovConfigOut",
        "BareMetalAdminDrainedMachineIn": "_gkeonprem_232_BareMetalAdminDrainedMachineIn",
        "BareMetalAdminDrainedMachineOut": "_gkeonprem_233_BareMetalAdminDrainedMachineOut",
        "BareMetalAdminProxyConfigIn": "_gkeonprem_234_BareMetalAdminProxyConfigIn",
        "BareMetalAdminProxyConfigOut": "_gkeonprem_235_BareMetalAdminProxyConfigOut",
        "ResourceStatusIn": "_gkeonprem_236_ResourceStatusIn",
        "ResourceStatusOut": "_gkeonprem_237_ResourceStatusOut",
        "BareMetalAdminApiServerArgumentIn": "_gkeonprem_238_BareMetalAdminApiServerArgumentIn",
        "BareMetalAdminApiServerArgumentOut": "_gkeonprem_239_BareMetalAdminApiServerArgumentOut",
        "BareMetalAdminIslandModeCidrConfigIn": "_gkeonprem_240_BareMetalAdminIslandModeCidrConfigIn",
        "BareMetalAdminIslandModeCidrConfigOut": "_gkeonprem_241_BareMetalAdminIslandModeCidrConfigOut",
        "VmwareIpBlockIn": "_gkeonprem_242_VmwareIpBlockIn",
        "VmwareIpBlockOut": "_gkeonprem_243_VmwareIpBlockOut",
        "VmwareAdminClusterIn": "_gkeonprem_244_VmwareAdminClusterIn",
        "VmwareAdminClusterOut": "_gkeonprem_245_VmwareAdminClusterOut",
        "BareMetalAdminVipConfigIn": "_gkeonprem_246_BareMetalAdminVipConfigIn",
        "BareMetalAdminVipConfigOut": "_gkeonprem_247_BareMetalAdminVipConfigOut",
        "ListVmwareAdminClustersResponseIn": "_gkeonprem_248_ListVmwareAdminClustersResponseIn",
        "ListVmwareAdminClustersResponseOut": "_gkeonprem_249_ListVmwareAdminClustersResponseOut",
        "VmwareF5BigIpConfigIn": "_gkeonprem_250_VmwareF5BigIpConfigIn",
        "VmwareF5BigIpConfigOut": "_gkeonprem_251_VmwareF5BigIpConfigOut",
        "BareMetalVersionInfoIn": "_gkeonprem_252_BareMetalVersionInfoIn",
        "BareMetalVersionInfoOut": "_gkeonprem_253_BareMetalVersionInfoOut",
        "BareMetalControlPlaneConfigIn": "_gkeonprem_254_BareMetalControlPlaneConfigIn",
        "BareMetalControlPlaneConfigOut": "_gkeonprem_255_BareMetalControlPlaneConfigOut",
        "BindingIn": "_gkeonprem_256_BindingIn",
        "BindingOut": "_gkeonprem_257_BindingOut",
        "ValidationCheckStatusIn": "_gkeonprem_258_ValidationCheckStatusIn",
        "ValidationCheckStatusOut": "_gkeonprem_259_ValidationCheckStatusOut",
        "VmwareStaticIpConfigIn": "_gkeonprem_260_VmwareStaticIpConfigIn",
        "VmwareStaticIpConfigOut": "_gkeonprem_261_VmwareStaticIpConfigOut",
        "BareMetalNodeConfigIn": "_gkeonprem_262_BareMetalNodeConfigIn",
        "BareMetalNodeConfigOut": "_gkeonprem_263_BareMetalNodeConfigOut",
        "VmwareAdminMetalLbConfigIn": "_gkeonprem_264_VmwareAdminMetalLbConfigIn",
        "VmwareAdminMetalLbConfigOut": "_gkeonprem_265_VmwareAdminMetalLbConfigOut",
        "LocationIn": "_gkeonprem_266_LocationIn",
        "LocationOut": "_gkeonprem_267_LocationOut",
        "BareMetalAdminLoadBalancerConfigIn": "_gkeonprem_268_BareMetalAdminLoadBalancerConfigIn",
        "BareMetalAdminLoadBalancerConfigOut": "_gkeonprem_269_BareMetalAdminLoadBalancerConfigOut",
        "BareMetalClusterOperationsConfigIn": "_gkeonprem_270_BareMetalClusterOperationsConfigIn",
        "BareMetalClusterOperationsConfigOut": "_gkeonprem_271_BareMetalClusterOperationsConfigOut",
        "BareMetalNodePoolConfigIn": "_gkeonprem_272_BareMetalNodePoolConfigIn",
        "BareMetalNodePoolConfigOut": "_gkeonprem_273_BareMetalNodePoolConfigOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["ListBareMetalClustersResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "bareMetalClusters": t.array(
                t.proxy(renames["BareMetalClusterIn"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListBareMetalClustersResponseIn"])
    types["ListBareMetalClustersResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "bareMetalClusters": t.array(
                t.proxy(renames["BareMetalClusterOut"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBareMetalClustersResponseOut"])
    types["ListBareMetalAdminClustersResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "bareMetalAdminClusters": t.array(
                t.proxy(renames["BareMetalAdminClusterIn"])
            ).optional(),
        }
    ).named(renames["ListBareMetalAdminClustersResponseIn"])
    types["ListBareMetalAdminClustersResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "bareMetalAdminClusters": t.array(
                t.proxy(renames["BareMetalAdminClusterOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBareMetalAdminClustersResponseOut"])
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
    types["BareMetalNodePoolIn"] = t.struct(
        {
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "etag": t.string().optional(),
            "name": t.string().optional(),
            "nodePoolConfig": t.proxy(renames["BareMetalNodePoolConfigIn"]),
            "displayName": t.string().optional(),
        }
    ).named(renames["BareMetalNodePoolIn"])
    types["BareMetalNodePoolOut"] = t.struct(
        {
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "reconciling": t.boolean().optional(),
            "createTime": t.string().optional(),
            "deleteTime": t.string().optional(),
            "etag": t.string().optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "nodePoolConfig": t.proxy(renames["BareMetalNodePoolConfigOut"]),
            "displayName": t.string().optional(),
            "status": t.proxy(renames["ResourceStatusOut"]).optional(),
            "updateTime": t.string().optional(),
            "uid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalNodePoolOut"])
    types["BareMetalControlPlaneNodePoolConfigIn"] = t.struct(
        {"nodePoolConfig": t.proxy(renames["BareMetalNodePoolConfigIn"])}
    ).named(renames["BareMetalControlPlaneNodePoolConfigIn"])
    types["BareMetalControlPlaneNodePoolConfigOut"] = t.struct(
        {
            "nodePoolConfig": t.proxy(renames["BareMetalNodePoolConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalControlPlaneNodePoolConfigOut"])
    types["PolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["AuthorizationIn"] = t.struct(
        {"adminUsers": t.array(t.proxy(renames["ClusterUserIn"]))}
    ).named(renames["AuthorizationIn"])
    types["AuthorizationOut"] = t.struct(
        {
            "adminUsers": t.array(t.proxy(renames["ClusterUserOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthorizationOut"])
    types["BareMetalBgpPeerConfigIn"] = t.struct(
        {
            "ipAddress": t.string(),
            "asn": t.string(),
            "controlPlaneNodes": t.array(t.string()).optional(),
        }
    ).named(renames["BareMetalBgpPeerConfigIn"])
    types["BareMetalBgpPeerConfigOut"] = t.struct(
        {
            "ipAddress": t.string(),
            "asn": t.string(),
            "controlPlaneNodes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalBgpPeerConfigOut"])
    types["EnrollBareMetalAdminClusterRequestIn"] = t.struct(
        {
            "localName": t.string().optional(),
            "bareMetalAdminClusterId": t.string().optional(),
            "membership": t.string(),
        }
    ).named(renames["EnrollBareMetalAdminClusterRequestIn"])
    types["EnrollBareMetalAdminClusterRequestOut"] = t.struct(
        {
            "localName": t.string().optional(),
            "bareMetalAdminClusterId": t.string().optional(),
            "membership": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnrollBareMetalAdminClusterRequestOut"])
    types["OperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["ResourceConditionIn"] = t.struct(
        {
            "lastTransitionTime": t.string().optional(),
            "message": t.string().optional(),
            "type": t.string().optional(),
            "state": t.string().optional(),
            "reason": t.string().optional(),
        }
    ).named(renames["ResourceConditionIn"])
    types["ResourceConditionOut"] = t.struct(
        {
            "lastTransitionTime": t.string().optional(),
            "message": t.string().optional(),
            "type": t.string().optional(),
            "state": t.string().optional(),
            "reason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceConditionOut"])
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
    types["ExprIn"] = t.struct(
        {
            "description": t.string().optional(),
            "location": t.string().optional(),
            "title": t.string().optional(),
            "expression": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "description": t.string().optional(),
            "location": t.string().optional(),
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["EnrollVmwareClusterRequestIn"] = t.struct(
        {
            "vmwareClusterId": t.string().optional(),
            "localName": t.string().optional(),
            "adminClusterMembership": t.string(),
            "validateOnly": t.boolean().optional(),
        }
    ).named(renames["EnrollVmwareClusterRequestIn"])
    types["EnrollVmwareClusterRequestOut"] = t.struct(
        {
            "vmwareClusterId": t.string().optional(),
            "localName": t.string().optional(),
            "adminClusterMembership": t.string(),
            "validateOnly": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnrollVmwareClusterRequestOut"])
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
    types["BareMetalAdminDrainingMachineIn"] = t.struct(
        {"podCount": t.integer().optional(), "nodeIp": t.string().optional()}
    ).named(renames["BareMetalAdminDrainingMachineIn"])
    types["BareMetalAdminDrainingMachineOut"] = t.struct(
        {
            "podCount": t.integer().optional(),
            "nodeIp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminDrainingMachineOut"])
    types["BareMetalAdminControlPlaneNodePoolConfigIn"] = t.struct(
        {"nodePoolConfig": t.proxy(renames["BareMetalNodePoolConfigIn"]).optional()}
    ).named(renames["BareMetalAdminControlPlaneNodePoolConfigIn"])
    types["BareMetalAdminControlPlaneNodePoolConfigOut"] = t.struct(
        {
            "nodePoolConfig": t.proxy(renames["BareMetalNodePoolConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminControlPlaneNodePoolConfigOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["VmwareControlPlaneVsphereConfigIn"] = t.struct(
        {"datastore": t.string().optional()}
    ).named(renames["VmwareControlPlaneVsphereConfigIn"])
    types["VmwareControlPlaneVsphereConfigOut"] = t.struct(
        {
            "datastore": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareControlPlaneVsphereConfigOut"])
    types["BareMetalAdminWorkloadNodeConfigIn"] = t.struct(
        {"maxPodsPerNode": t.string().optional()}
    ).named(renames["BareMetalAdminWorkloadNodeConfigIn"])
    types["BareMetalAdminWorkloadNodeConfigOut"] = t.struct(
        {
            "maxPodsPerNode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminWorkloadNodeConfigOut"])
    types["BareMetalWorkloadNodeConfigIn"] = t.struct(
        {
            "maxPodsPerNode": t.string().optional(),
            "containerRuntime": t.string().optional(),
        }
    ).named(renames["BareMetalWorkloadNodeConfigIn"])
    types["BareMetalWorkloadNodeConfigOut"] = t.struct(
        {
            "maxPodsPerNode": t.string().optional(),
            "containerRuntime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalWorkloadNodeConfigOut"])
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
    types["BareMetalAdminManualLbConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["BareMetalAdminManualLbConfigIn"])
    types["BareMetalAdminManualLbConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminManualLbConfigOut"])
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
    types["BareMetalLoadBalancerNodePoolConfigIn"] = t.struct(
        {"nodePoolConfig": t.proxy(renames["BareMetalNodePoolConfigIn"]).optional()}
    ).named(renames["BareMetalLoadBalancerNodePoolConfigIn"])
    types["BareMetalLoadBalancerNodePoolConfigOut"] = t.struct(
        {
            "nodePoolConfig": t.proxy(renames["BareMetalNodePoolConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalLoadBalancerNodePoolConfigOut"])
    types["EnrollVmwareAdminClusterRequestIn"] = t.struct(
        {
            "localName": t.string().optional(),
            "membership": t.string(),
            "vmwareAdminClusterId": t.string().optional(),
        }
    ).named(renames["EnrollVmwareAdminClusterRequestIn"])
    types["EnrollVmwareAdminClusterRequestOut"] = t.struct(
        {
            "localName": t.string().optional(),
            "membership": t.string(),
            "vmwareAdminClusterId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnrollVmwareAdminClusterRequestOut"])
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
    types["BareMetalManualLbConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["BareMetalManualLbConfigIn"])
    types["BareMetalManualLbConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalManualLbConfigOut"])
    types["VmwareMetalLbConfigIn"] = t.struct(
        {"addressPools": t.array(t.proxy(renames["VmwareAddressPoolIn"]))}
    ).named(renames["VmwareMetalLbConfigIn"])
    types["VmwareMetalLbConfigOut"] = t.struct(
        {
            "addressPools": t.array(t.proxy(renames["VmwareAddressPoolOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareMetalLbConfigOut"])
    types["VmwareAdminManualLbConfigIn"] = t.struct(
        {
            "addonsNodePort": t.integer().optional(),
            "ingressHttpsNodePort": t.integer().optional(),
            "controlPlaneNodePort": t.integer().optional(),
            "ingressHttpNodePort": t.integer().optional(),
            "konnectivityServerNodePort": t.integer().optional(),
        }
    ).named(renames["VmwareAdminManualLbConfigIn"])
    types["VmwareAdminManualLbConfigOut"] = t.struct(
        {
            "addonsNodePort": t.integer().optional(),
            "ingressHttpsNodePort": t.integer().optional(),
            "controlPlaneNodePort": t.integer().optional(),
            "ingressHttpNodePort": t.integer().optional(),
            "konnectivityServerNodePort": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareAdminManualLbConfigOut"])
    types["VmwareHostConfigIn"] = t.struct(
        {
            "ntpServers": t.array(t.string()).optional(),
            "dnsServers": t.array(t.string()).optional(),
            "dnsSearchDomains": t.array(t.string()).optional(),
        }
    ).named(renames["VmwareHostConfigIn"])
    types["VmwareHostConfigOut"] = t.struct(
        {
            "ntpServers": t.array(t.string()).optional(),
            "dnsServers": t.array(t.string()).optional(),
            "dnsSearchDomains": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareHostConfigOut"])
    types["BareMetalDrainingMachineIn"] = t.struct(
        {"nodeIp": t.string().optional(), "podCount": t.integer().optional()}
    ).named(renames["BareMetalDrainingMachineIn"])
    types["BareMetalDrainingMachineOut"] = t.struct(
        {
            "nodeIp": t.string().optional(),
            "podCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalDrainingMachineOut"])
    types["BareMetalMaintenanceConfigIn"] = t.struct(
        {"maintenanceAddressCidrBlocks": t.array(t.string())}
    ).named(renames["BareMetalMaintenanceConfigIn"])
    types["BareMetalMaintenanceConfigOut"] = t.struct(
        {
            "maintenanceAddressCidrBlocks": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalMaintenanceConfigOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["VmwareAutoRepairConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["VmwareAutoRepairConfigIn"])
    types["VmwareAutoRepairConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareAutoRepairConfigOut"])
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
    types["BareMetalMachineDrainStatusIn"] = t.struct(
        {
            "drainingMachines": t.array(
                t.proxy(renames["BareMetalDrainingMachineIn"])
            ).optional(),
            "drainedMachines": t.array(
                t.proxy(renames["BareMetalDrainedMachineIn"])
            ).optional(),
        }
    ).named(renames["BareMetalMachineDrainStatusIn"])
    types["BareMetalMachineDrainStatusOut"] = t.struct(
        {
            "drainingMachines": t.array(
                t.proxy(renames["BareMetalDrainingMachineOut"])
            ).optional(),
            "drainedMachines": t.array(
                t.proxy(renames["BareMetalDrainedMachineOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalMachineDrainStatusOut"])
    types["BareMetalLoadBalancerAddressPoolIn"] = t.struct(
        {
            "addresses": t.array(t.string()),
            "avoidBuggyIps": t.boolean().optional(),
            "pool": t.string(),
            "manualAssign": t.boolean().optional(),
        }
    ).named(renames["BareMetalLoadBalancerAddressPoolIn"])
    types["BareMetalLoadBalancerAddressPoolOut"] = t.struct(
        {
            "addresses": t.array(t.string()),
            "avoidBuggyIps": t.boolean().optional(),
            "pool": t.string(),
            "manualAssign": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalLoadBalancerAddressPoolOut"])
    types["ClusterUserIn"] = t.struct({"username": t.string()}).named(
        renames["ClusterUserIn"]
    )
    types["ClusterUserOut"] = t.struct(
        {"username": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ClusterUserOut"])
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
            "pool": t.string(),
            "manualAssign": t.boolean().optional(),
            "avoidBuggyIps": t.boolean().optional(),
            "addresses": t.array(t.string()),
        }
    ).named(renames["VmwareAddressPoolIn"])
    types["VmwareAddressPoolOut"] = t.struct(
        {
            "pool": t.string(),
            "manualAssign": t.boolean().optional(),
            "avoidBuggyIps": t.boolean().optional(),
            "addresses": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareAddressPoolOut"])
    types["QueryBareMetalVersionConfigResponseIn"] = t.struct(
        {"versions": t.array(t.proxy(renames["BareMetalVersionInfoIn"])).optional()}
    ).named(renames["QueryBareMetalVersionConfigResponseIn"])
    types["QueryBareMetalVersionConfigResponseOut"] = t.struct(
        {
            "versions": t.array(t.proxy(renames["BareMetalVersionInfoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryBareMetalVersionConfigResponseOut"])
    types["BareMetalDrainedMachineIn"] = t.struct(
        {"nodeIp": t.string().optional()}
    ).named(renames["BareMetalDrainedMachineIn"])
    types["BareMetalDrainedMachineOut"] = t.struct(
        {
            "nodeIp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalDrainedMachineOut"])
    types["ListVmwareNodePoolsResponseIn"] = t.struct(
        {
            "vmwareNodePools": t.array(t.proxy(renames["VmwareNodePoolIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListVmwareNodePoolsResponseIn"])
    types["ListVmwareNodePoolsResponseOut"] = t.struct(
        {
            "vmwareNodePools": t.array(
                t.proxy(renames["VmwareNodePoolOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListVmwareNodePoolsResponseOut"])
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
    types["BareMetalAdminMaintenanceConfigIn"] = t.struct(
        {"maintenanceAddressCidrBlocks": t.array(t.string())}
    ).named(renames["BareMetalAdminMaintenanceConfigIn"])
    types["BareMetalAdminMaintenanceConfigOut"] = t.struct(
        {
            "maintenanceAddressCidrBlocks": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminMaintenanceConfigOut"])
    types["VmwareVCenterConfigIn"] = t.struct(
        {
            "cluster": t.string().optional(),
            "folder": t.string().optional(),
            "resourcePool": t.string().optional(),
            "datacenter": t.string().optional(),
            "datastore": t.string().optional(),
            "address": t.string().optional(),
            "caCertData": t.string().optional(),
        }
    ).named(renames["VmwareVCenterConfigIn"])
    types["VmwareVCenterConfigOut"] = t.struct(
        {
            "cluster": t.string().optional(),
            "folder": t.string().optional(),
            "resourcePool": t.string().optional(),
            "datacenter": t.string().optional(),
            "datastore": t.string().optional(),
            "address": t.string().optional(),
            "caCertData": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareVCenterConfigOut"])
    types["BareMetalAdminOsEnvironmentConfigIn"] = t.struct(
        {"packageRepoExcluded": t.boolean().optional()}
    ).named(renames["BareMetalAdminOsEnvironmentConfigIn"])
    types["BareMetalAdminOsEnvironmentConfigOut"] = t.struct(
        {
            "packageRepoExcluded": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminOsEnvironmentConfigOut"])
    types["VmwareManualLbConfigIn"] = t.struct(
        {
            "konnectivityServerNodePort": t.integer().optional(),
            "ingressHttpsNodePort": t.integer().optional(),
            "ingressHttpNodePort": t.integer().optional(),
            "controlPlaneNodePort": t.integer().optional(),
        }
    ).named(renames["VmwareManualLbConfigIn"])
    types["VmwareManualLbConfigOut"] = t.struct(
        {
            "konnectivityServerNodePort": t.integer().optional(),
            "ingressHttpsNodePort": t.integer().optional(),
            "ingressHttpNodePort": t.integer().optional(),
            "controlPlaneNodePort": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareManualLbConfigOut"])
    types["QueryBareMetalAdminVersionConfigResponseIn"] = t.struct(
        {"versions": t.array(t.proxy(renames["BareMetalVersionInfoIn"])).optional()}
    ).named(renames["QueryBareMetalAdminVersionConfigResponseIn"])
    types["QueryBareMetalAdminVersionConfigResponseOut"] = t.struct(
        {
            "versions": t.array(t.proxy(renames["BareMetalVersionInfoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryBareMetalAdminVersionConfigResponseOut"])
    types["VmwarePlatformConfigIn"] = t.struct(
        {"requiredPlatformVersion": t.string().optional()}
    ).named(renames["VmwarePlatformConfigIn"])
    types["VmwarePlatformConfigOut"] = t.struct(
        {
            "status": t.proxy(renames["ResourceStatusOut"]).optional(),
            "requiredPlatformVersion": t.string().optional(),
            "bundles": t.array(t.proxy(renames["VmwareBundleConfigOut"])).optional(),
            "platformVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwarePlatformConfigOut"])
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
    types["VmwareAutoResizeConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["VmwareAutoResizeConfigIn"])
    types["VmwareAutoResizeConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareAutoResizeConfigOut"])
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
    types["ValidationCheckIn"] = t.struct({"option": t.string().optional()}).named(
        renames["ValidationCheckIn"]
    )
    types["ValidationCheckOut"] = t.struct(
        {
            "status": t.proxy(renames["ValidationCheckStatusOut"]).optional(),
            "option": t.string().optional(),
            "scenario": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidationCheckOut"])
    types["BareMetalAdminClusterIn"] = t.struct(
        {
            "maintenanceConfig": t.proxy(
                renames["BareMetalAdminMaintenanceConfigIn"]
            ).optional(),
            "bareMetalVersion": t.string().optional(),
            "loadBalancer": t.proxy(
                renames["BareMetalAdminLoadBalancerConfigIn"]
            ).optional(),
            "nodeConfig": t.proxy(
                renames["BareMetalAdminWorkloadNodeConfigIn"]
            ).optional(),
            "storage": t.proxy(renames["BareMetalAdminStorageConfigIn"]).optional(),
            "name": t.string().optional(),
            "networkConfig": t.proxy(
                renames["BareMetalAdminNetworkConfigIn"]
            ).optional(),
            "clusterOperations": t.proxy(
                renames["BareMetalAdminClusterOperationsConfigIn"]
            ).optional(),
            "osEnvironmentConfig": t.proxy(
                renames["BareMetalAdminOsEnvironmentConfigIn"]
            ).optional(),
            "description": t.string().optional(),
            "securityConfig": t.proxy(
                renames["BareMetalAdminSecurityConfigIn"]
            ).optional(),
            "etag": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "nodeAccessConfig": t.proxy(
                renames["BareMetalAdminNodeAccessConfigIn"]
            ).optional(),
            "proxy": t.proxy(renames["BareMetalAdminProxyConfigIn"]).optional(),
            "controlPlane": t.proxy(
                renames["BareMetalAdminControlPlaneConfigIn"]
            ).optional(),
        }
    ).named(renames["BareMetalAdminClusterIn"])
    types["BareMetalAdminClusterOut"] = t.struct(
        {
            "validationCheck": t.proxy(renames["ValidationCheckOut"]).optional(),
            "maintenanceStatus": t.proxy(
                renames["BareMetalAdminMaintenanceStatusOut"]
            ).optional(),
            "status": t.proxy(renames["ResourceStatusOut"]).optional(),
            "maintenanceConfig": t.proxy(
                renames["BareMetalAdminMaintenanceConfigOut"]
            ).optional(),
            "bareMetalVersion": t.string().optional(),
            "loadBalancer": t.proxy(
                renames["BareMetalAdminLoadBalancerConfigOut"]
            ).optional(),
            "nodeConfig": t.proxy(
                renames["BareMetalAdminWorkloadNodeConfigOut"]
            ).optional(),
            "storage": t.proxy(renames["BareMetalAdminStorageConfigOut"]).optional(),
            "name": t.string().optional(),
            "reconciling": t.boolean().optional(),
            "localName": t.string().optional(),
            "networkConfig": t.proxy(
                renames["BareMetalAdminNetworkConfigOut"]
            ).optional(),
            "uid": t.string().optional(),
            "clusterOperations": t.proxy(
                renames["BareMetalAdminClusterOperationsConfigOut"]
            ).optional(),
            "deleteTime": t.string().optional(),
            "osEnvironmentConfig": t.proxy(
                renames["BareMetalAdminOsEnvironmentConfigOut"]
            ).optional(),
            "state": t.string().optional(),
            "fleet": t.proxy(renames["FleetOut"]).optional(),
            "description": t.string().optional(),
            "endpoint": t.string().optional(),
            "securityConfig": t.proxy(
                renames["BareMetalAdminSecurityConfigOut"]
            ).optional(),
            "etag": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "nodeAccessConfig": t.proxy(
                renames["BareMetalAdminNodeAccessConfigOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "proxy": t.proxy(renames["BareMetalAdminProxyConfigOut"]).optional(),
            "controlPlane": t.proxy(
                renames["BareMetalAdminControlPlaneConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminClusterOut"])
    types["BareMetalLoadBalancerConfigIn"] = t.struct(
        {
            "portConfig": t.proxy(renames["BareMetalPortConfigIn"]).optional(),
            "vipConfig": t.proxy(renames["BareMetalVipConfigIn"]).optional(),
            "bgpLbConfig": t.proxy(renames["BareMetalBgpLbConfigIn"]).optional(),
            "metalLbConfig": t.proxy(renames["BareMetalMetalLbConfigIn"]).optional(),
            "manualLbConfig": t.proxy(renames["BareMetalManualLbConfigIn"]).optional(),
        }
    ).named(renames["BareMetalLoadBalancerConfigIn"])
    types["BareMetalLoadBalancerConfigOut"] = t.struct(
        {
            "portConfig": t.proxy(renames["BareMetalPortConfigOut"]).optional(),
            "vipConfig": t.proxy(renames["BareMetalVipConfigOut"]).optional(),
            "bgpLbConfig": t.proxy(renames["BareMetalBgpLbConfigOut"]).optional(),
            "metalLbConfig": t.proxy(renames["BareMetalMetalLbConfigOut"]).optional(),
            "manualLbConfig": t.proxy(renames["BareMetalManualLbConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalLoadBalancerConfigOut"])
    types["VmwareDhcpIpConfigIn"] = t.struct({"enabled": t.boolean().optional()}).named(
        renames["VmwareDhcpIpConfigIn"]
    )
    types["VmwareDhcpIpConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareDhcpIpConfigOut"])
    types["VmwareLoadBalancerConfigIn"] = t.struct(
        {
            "f5Config": t.proxy(renames["VmwareF5BigIpConfigIn"]).optional(),
            "vipConfig": t.proxy(renames["VmwareVipConfigIn"]).optional(),
            "manualLbConfig": t.proxy(renames["VmwareManualLbConfigIn"]).optional(),
            "metalLbConfig": t.proxy(renames["VmwareMetalLbConfigIn"]).optional(),
        }
    ).named(renames["VmwareLoadBalancerConfigIn"])
    types["VmwareLoadBalancerConfigOut"] = t.struct(
        {
            "f5Config": t.proxy(renames["VmwareF5BigIpConfigOut"]).optional(),
            "vipConfig": t.proxy(renames["VmwareVipConfigOut"]).optional(),
            "manualLbConfig": t.proxy(renames["VmwareManualLbConfigOut"]).optional(),
            "metalLbConfig": t.proxy(renames["VmwareMetalLbConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareLoadBalancerConfigOut"])
    types["BareMetalAdminNodeAccessConfigIn"] = t.struct(
        {"loginUser": t.string()}
    ).named(renames["BareMetalAdminNodeAccessConfigIn"])
    types["BareMetalAdminNodeAccessConfigOut"] = t.struct(
        {"loginUser": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["BareMetalAdminNodeAccessConfigOut"])
    types["VmwareControlPlaneNodeConfigIn"] = t.struct(
        {
            "memory": t.string().optional(),
            "cpus": t.string().optional(),
            "autoResizeConfig": t.proxy(renames["VmwareAutoResizeConfigIn"]).optional(),
            "replicas": t.string().optional(),
        }
    ).named(renames["VmwareControlPlaneNodeConfigIn"])
    types["VmwareControlPlaneNodeConfigOut"] = t.struct(
        {
            "memory": t.string().optional(),
            "cpus": t.string().optional(),
            "autoResizeConfig": t.proxy(
                renames["VmwareAutoResizeConfigOut"]
            ).optional(),
            "replicas": t.string().optional(),
            "vsphereConfig": t.proxy(
                renames["VmwareControlPlaneVsphereConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareControlPlaneNodeConfigOut"])
    types["BareMetalAdminPortConfigIn"] = t.struct(
        {"controlPlaneLoadBalancerPort": t.integer().optional()}
    ).named(renames["BareMetalAdminPortConfigIn"])
    types["BareMetalAdminPortConfigOut"] = t.struct(
        {
            "controlPlaneLoadBalancerPort": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminPortConfigOut"])
    types["BareMetalClusterIn"] = t.struct(
        {
            "networkConfig": t.proxy(renames["BareMetalNetworkConfigIn"]),
            "loadBalancer": t.proxy(renames["BareMetalLoadBalancerConfigIn"]),
            "description": t.string().optional(),
            "nodeAccessConfig": t.proxy(
                renames["BareMetalNodeAccessConfigIn"]
            ).optional(),
            "osEnvironmentConfig": t.proxy(
                renames["BareMetalOsEnvironmentConfigIn"]
            ).optional(),
            "nodeConfig": t.proxy(renames["BareMetalWorkloadNodeConfigIn"]).optional(),
            "maintenanceConfig": t.proxy(
                renames["BareMetalMaintenanceConfigIn"]
            ).optional(),
            "proxy": t.proxy(renames["BareMetalProxyConfigIn"]).optional(),
            "securityConfig": t.proxy(renames["BareMetalSecurityConfigIn"]).optional(),
            "clusterOperations": t.proxy(
                renames["BareMetalClusterOperationsConfigIn"]
            ).optional(),
            "name": t.string().optional(),
            "bareMetalVersion": t.string(),
            "adminClusterMembership": t.string(),
            "controlPlane": t.proxy(renames["BareMetalControlPlaneConfigIn"]),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "storage": t.proxy(renames["BareMetalStorageConfigIn"]),
        }
    ).named(renames["BareMetalClusterIn"])
    types["BareMetalClusterOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "networkConfig": t.proxy(renames["BareMetalNetworkConfigOut"]),
            "loadBalancer": t.proxy(renames["BareMetalLoadBalancerConfigOut"]),
            "description": t.string().optional(),
            "status": t.proxy(renames["ResourceStatusOut"]).optional(),
            "nodeAccessConfig": t.proxy(
                renames["BareMetalNodeAccessConfigOut"]
            ).optional(),
            "osEnvironmentConfig": t.proxy(
                renames["BareMetalOsEnvironmentConfigOut"]
            ).optional(),
            "nodeConfig": t.proxy(renames["BareMetalWorkloadNodeConfigOut"]).optional(),
            "reconciling": t.boolean().optional(),
            "maintenanceConfig": t.proxy(
                renames["BareMetalMaintenanceConfigOut"]
            ).optional(),
            "validationCheck": t.proxy(renames["ValidationCheckOut"]).optional(),
            "proxy": t.proxy(renames["BareMetalProxyConfigOut"]).optional(),
            "adminClusterName": t.string().optional(),
            "state": t.string().optional(),
            "securityConfig": t.proxy(renames["BareMetalSecurityConfigOut"]).optional(),
            "uid": t.string().optional(),
            "clusterOperations": t.proxy(
                renames["BareMetalClusterOperationsConfigOut"]
            ).optional(),
            "name": t.string().optional(),
            "bareMetalVersion": t.string(),
            "adminClusterMembership": t.string(),
            "fleet": t.proxy(renames["FleetOut"]).optional(),
            "localName": t.string().optional(),
            "controlPlane": t.proxy(renames["BareMetalControlPlaneConfigOut"]),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "maintenanceStatus": t.proxy(
                renames["BareMetalMaintenanceStatusOut"]
            ).optional(),
            "etag": t.string().optional(),
            "storage": t.proxy(renames["BareMetalStorageConfigOut"]),
            "endpoint": t.string().optional(),
            "deleteTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalClusterOut"])
    types["VmwareStorageConfigIn"] = t.struct(
        {"vsphereCsiDisabled": t.boolean().optional()}
    ).named(renames["VmwareStorageConfigIn"])
    types["VmwareStorageConfigOut"] = t.struct(
        {
            "vsphereCsiDisabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareStorageConfigOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["BareMetalKubeletConfigIn"] = t.struct(
        {
            "registryPullQps": t.integer().optional(),
            "serializeImagePullsDisabled": t.boolean().optional(),
            "registryBurst": t.integer().optional(),
        }
    ).named(renames["BareMetalKubeletConfigIn"])
    types["BareMetalKubeletConfigOut"] = t.struct(
        {
            "registryPullQps": t.integer().optional(),
            "serializeImagePullsDisabled": t.boolean().optional(),
            "registryBurst": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalKubeletConfigOut"])
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
    types["VmwareNodePoolIn"] = t.struct(
        {
            "config": t.proxy(renames["VmwareNodeConfigIn"]),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "etag": t.string().optional(),
            "onPremVersion": t.string().optional(),
            "displayName": t.string().optional(),
            "nodePoolAutoscaling": t.proxy(
                renames["VmwareNodePoolAutoscalingConfigIn"]
            ).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["VmwareNodePoolIn"])
    types["VmwareNodePoolOut"] = t.struct(
        {
            "state": t.string().optional(),
            "config": t.proxy(renames["VmwareNodeConfigOut"]),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "etag": t.string().optional(),
            "onPremVersion": t.string().optional(),
            "status": t.proxy(renames["ResourceStatusOut"]).optional(),
            "uid": t.string().optional(),
            "createTime": t.string().optional(),
            "displayName": t.string().optional(),
            "updateTime": t.string().optional(),
            "nodePoolAutoscaling": t.proxy(
                renames["VmwareNodePoolAutoscalingConfigOut"]
            ).optional(),
            "deleteTime": t.string().optional(),
            "reconciling": t.boolean().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareNodePoolOut"])
    types["VmwareAdminVCenterConfigIn"] = t.struct(
        {
            "datacenter": t.string().optional(),
            "resourcePool": t.string().optional(),
            "address": t.string().optional(),
            "dataDisk": t.string().optional(),
            "cluster": t.string().optional(),
            "folder": t.string().optional(),
            "datastore": t.string().optional(),
            "caCertData": t.string().optional(),
        }
    ).named(renames["VmwareAdminVCenterConfigIn"])
    types["VmwareAdminVCenterConfigOut"] = t.struct(
        {
            "datacenter": t.string().optional(),
            "resourcePool": t.string().optional(),
            "address": t.string().optional(),
            "dataDisk": t.string().optional(),
            "cluster": t.string().optional(),
            "folder": t.string().optional(),
            "datastore": t.string().optional(),
            "caCertData": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareAdminVCenterConfigOut"])
    types["FleetIn"] = t.struct({"_": t.string().optional()}).named(renames["FleetIn"])
    types["FleetOut"] = t.struct(
        {
            "membership": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FleetOut"])
    types["ListVmwareClustersResponseIn"] = t.struct(
        {
            "vmwareClusters": t.array(t.proxy(renames["VmwareClusterIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListVmwareClustersResponseIn"])
    types["ListVmwareClustersResponseOut"] = t.struct(
        {
            "vmwareClusters": t.array(t.proxy(renames["VmwareClusterOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListVmwareClustersResponseOut"])
    types["BareMetalPortConfigIn"] = t.struct(
        {"controlPlaneLoadBalancerPort": t.integer().optional()}
    ).named(renames["BareMetalPortConfigIn"])
    types["BareMetalPortConfigOut"] = t.struct(
        {
            "controlPlaneLoadBalancerPort": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalPortConfigOut"])
    types["BareMetalProxyConfigIn"] = t.struct(
        {"uri": t.string(), "noProxy": t.array(t.string()).optional()}
    ).named(renames["BareMetalProxyConfigIn"])
    types["BareMetalProxyConfigOut"] = t.struct(
        {
            "uri": t.string(),
            "noProxy": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalProxyConfigOut"])
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
    types["QueryVmwareVersionConfigResponseIn"] = t.struct(
        {"versions": t.array(t.proxy(renames["VmwareVersionInfoIn"])).optional()}
    ).named(renames["QueryVmwareVersionConfigResponseIn"])
    types["QueryVmwareVersionConfigResponseOut"] = t.struct(
        {
            "versions": t.array(t.proxy(renames["VmwareVersionInfoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryVmwareVersionConfigResponseOut"])
    types["ValidationCheckResultIn"] = t.struct(
        {
            "details": t.string().optional(),
            "reason": t.string().optional(),
            "description": t.string().optional(),
            "category": t.string().optional(),
            "state": t.string().optional(),
        }
    ).named(renames["ValidationCheckResultIn"])
    types["ValidationCheckResultOut"] = t.struct(
        {
            "details": t.string().optional(),
            "reason": t.string().optional(),
            "description": t.string().optional(),
            "category": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidationCheckResultOut"])
    types["VmwareDataplaneV2ConfigIn"] = t.struct(
        {
            "advancedNetworking": t.boolean().optional(),
            "windowsDataplaneV2Enabled": t.boolean().optional(),
            "dataplaneV2Enabled": t.boolean().optional(),
        }
    ).named(renames["VmwareDataplaneV2ConfigIn"])
    types["VmwareDataplaneV2ConfigOut"] = t.struct(
        {
            "advancedNetworking": t.boolean().optional(),
            "windowsDataplaneV2Enabled": t.boolean().optional(),
            "dataplaneV2Enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareDataplaneV2ConfigOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "target": t.string().optional(),
            "apiVersion": t.string().optional(),
            "endTime": t.string().optional(),
            "statusMessage": t.string().optional(),
            "createTime": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "verb": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["VmwareControlPlaneV2ConfigIn"] = t.struct(
        {"controlPlaneIpBlock": t.proxy(renames["VmwareIpBlockIn"]).optional()}
    ).named(renames["VmwareControlPlaneV2ConfigIn"])
    types["VmwareControlPlaneV2ConfigOut"] = t.struct(
        {
            "controlPlaneIpBlock": t.proxy(renames["VmwareIpBlockOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareControlPlaneV2ConfigOut"])
    types["BareMetalNodeAccessConfigIn"] = t.struct(
        {"loginUser": t.string().optional()}
    ).named(renames["BareMetalNodeAccessConfigIn"])
    types["BareMetalNodeAccessConfigOut"] = t.struct(
        {
            "loginUser": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalNodeAccessConfigOut"])
    types["BareMetalMultipleNetworkInterfacesConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["BareMetalMultipleNetworkInterfacesConfigIn"])
    types["BareMetalMultipleNetworkInterfacesConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalMultipleNetworkInterfacesConfigOut"])
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
    types["VmwareNodeConfigIn"] = t.struct(
        {
            "taints": t.array(t.proxy(renames["NodeTaintIn"])).optional(),
            "image": t.string().optional(),
            "bootDiskSizeGb": t.string().optional(),
            "cpus": t.string().optional(),
            "memoryMb": t.string().optional(),
            "replicas": t.string().optional(),
            "imageType": t.string(),
            "enableLoadBalancer": t.boolean().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["VmwareNodeConfigIn"])
    types["VmwareNodeConfigOut"] = t.struct(
        {
            "vsphereConfig": t.proxy(renames["VmwareVsphereConfigOut"]).optional(),
            "taints": t.array(t.proxy(renames["NodeTaintOut"])).optional(),
            "image": t.string().optional(),
            "bootDiskSizeGb": t.string().optional(),
            "cpus": t.string().optional(),
            "memoryMb": t.string().optional(),
            "replicas": t.string().optional(),
            "imageType": t.string(),
            "enableLoadBalancer": t.boolean().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareNodeConfigOut"])
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
    types["BareMetalOsEnvironmentConfigIn"] = t.struct(
        {"packageRepoExcluded": t.boolean().optional()}
    ).named(renames["BareMetalOsEnvironmentConfigIn"])
    types["BareMetalOsEnvironmentConfigOut"] = t.struct(
        {
            "packageRepoExcluded": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalOsEnvironmentConfigOut"])
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
    types["VmwareNetworkConfigIn"] = t.struct(
        {
            "serviceAddressCidrBlocks": t.array(t.string()),
            "staticIpConfig": t.proxy(renames["VmwareStaticIpConfigIn"]).optional(),
            "podAddressCidrBlocks": t.array(t.string()),
            "dhcpIpConfig": t.proxy(renames["VmwareDhcpIpConfigIn"]).optional(),
            "controlPlaneV2Config": t.proxy(
                renames["VmwareControlPlaneV2ConfigIn"]
            ).optional(),
            "hostConfig": t.proxy(renames["VmwareHostConfigIn"]).optional(),
        }
    ).named(renames["VmwareNetworkConfigIn"])
    types["VmwareNetworkConfigOut"] = t.struct(
        {
            "serviceAddressCidrBlocks": t.array(t.string()),
            "staticIpConfig": t.proxy(renames["VmwareStaticIpConfigOut"]).optional(),
            "podAddressCidrBlocks": t.array(t.string()),
            "dhcpIpConfig": t.proxy(renames["VmwareDhcpIpConfigOut"]).optional(),
            "controlPlaneV2Config": t.proxy(
                renames["VmwareControlPlaneV2ConfigOut"]
            ).optional(),
            "hostConfig": t.proxy(renames["VmwareHostConfigOut"]).optional(),
            "vcenterNetwork": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareNetworkConfigOut"])
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
    types["VmwareAdminNetworkConfigIn"] = t.struct(
        {
            "staticIpConfig": t.proxy(renames["VmwareStaticIpConfigIn"]).optional(),
            "dhcpIpConfig": t.proxy(renames["VmwareDhcpIpConfigIn"]).optional(),
            "hostConfig": t.proxy(renames["VmwareHostConfigIn"]).optional(),
            "serviceAddressCidrBlocks": t.array(t.string()),
            "podAddressCidrBlocks": t.array(t.string()),
            "vcenterNetwork": t.string().optional(),
        }
    ).named(renames["VmwareAdminNetworkConfigIn"])
    types["VmwareAdminNetworkConfigOut"] = t.struct(
        {
            "staticIpConfig": t.proxy(renames["VmwareStaticIpConfigOut"]).optional(),
            "dhcpIpConfig": t.proxy(renames["VmwareDhcpIpConfigOut"]).optional(),
            "hostConfig": t.proxy(renames["VmwareHostConfigOut"]).optional(),
            "serviceAddressCidrBlocks": t.array(t.string()),
            "podAddressCidrBlocks": t.array(t.string()),
            "vcenterNetwork": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareAdminNetworkConfigOut"])
    types["BareMetalAdminSecurityConfigIn"] = t.struct(
        {"authorization": t.proxy(renames["AuthorizationIn"]).optional()}
    ).named(renames["BareMetalAdminSecurityConfigIn"])
    types["BareMetalAdminSecurityConfigOut"] = t.struct(
        {
            "authorization": t.proxy(renames["AuthorizationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminSecurityConfigOut"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {"policy": t.proxy(renames["PolicyIn"]).optional()}
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
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
    types["BareMetalVipConfigIn"] = t.struct(
        {"controlPlaneVip": t.string().optional(), "ingressVip": t.string().optional()}
    ).named(renames["BareMetalVipConfigIn"])
    types["BareMetalVipConfigOut"] = t.struct(
        {
            "controlPlaneVip": t.string().optional(),
            "ingressVip": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalVipConfigOut"])
    types["BareMetalAdminClusterOperationsConfigIn"] = t.struct(
        {"enableApplicationLogs": t.boolean().optional()}
    ).named(renames["BareMetalAdminClusterOperationsConfigIn"])
    types["BareMetalAdminClusterOperationsConfigOut"] = t.struct(
        {
            "enableApplicationLogs": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminClusterOperationsConfigOut"])
    types["VmwareAdminLoadBalancerConfigIn"] = t.struct(
        {
            "vipConfig": t.proxy(renames["VmwareAdminVipConfigIn"]).optional(),
            "manualLbConfig": t.proxy(
                renames["VmwareAdminManualLbConfigIn"]
            ).optional(),
            "f5Config": t.proxy(renames["VmwareAdminF5BigIpConfigIn"]).optional(),
            "metalLbConfig": t.proxy(renames["VmwareAdminMetalLbConfigIn"]).optional(),
        }
    ).named(renames["VmwareAdminLoadBalancerConfigIn"])
    types["VmwareAdminLoadBalancerConfigOut"] = t.struct(
        {
            "vipConfig": t.proxy(renames["VmwareAdminVipConfigOut"]).optional(),
            "manualLbConfig": t.proxy(
                renames["VmwareAdminManualLbConfigOut"]
            ).optional(),
            "f5Config": t.proxy(renames["VmwareAdminF5BigIpConfigOut"]).optional(),
            "metalLbConfig": t.proxy(renames["VmwareAdminMetalLbConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareAdminLoadBalancerConfigOut"])
    types["EnrollBareMetalClusterRequestIn"] = t.struct(
        {
            "localName": t.string().optional(),
            "bareMetalClusterId": t.string().optional(),
            "adminClusterMembership": t.string(),
        }
    ).named(renames["EnrollBareMetalClusterRequestIn"])
    types["EnrollBareMetalClusterRequestOut"] = t.struct(
        {
            "localName": t.string().optional(),
            "bareMetalClusterId": t.string().optional(),
            "adminClusterMembership": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnrollBareMetalClusterRequestOut"])
    types["ListBareMetalNodePoolsResponseIn"] = t.struct(
        {
            "bareMetalNodePools": t.array(
                t.proxy(renames["BareMetalNodePoolIn"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListBareMetalNodePoolsResponseIn"])
    types["ListBareMetalNodePoolsResponseOut"] = t.struct(
        {
            "bareMetalNodePools": t.array(
                t.proxy(renames["BareMetalNodePoolOut"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBareMetalNodePoolsResponseOut"])
    types["BareMetalSecurityConfigIn"] = t.struct(
        {"authorization": t.proxy(renames["AuthorizationIn"]).optional()}
    ).named(renames["BareMetalSecurityConfigIn"])
    types["BareMetalSecurityConfigOut"] = t.struct(
        {
            "authorization": t.proxy(renames["AuthorizationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalSecurityConfigOut"])
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
    types["BareMetalBgpLbConfigIn"] = t.struct(
        {
            "loadBalancerNodePoolConfig": t.proxy(
                renames["BareMetalLoadBalancerNodePoolConfigIn"]
            ).optional(),
            "addressPools": t.array(
                t.proxy(renames["BareMetalLoadBalancerAddressPoolIn"])
            ),
            "asn": t.string(),
            "bgpPeerConfigs": t.array(t.proxy(renames["BareMetalBgpPeerConfigIn"])),
        }
    ).named(renames["BareMetalBgpLbConfigIn"])
    types["BareMetalBgpLbConfigOut"] = t.struct(
        {
            "loadBalancerNodePoolConfig": t.proxy(
                renames["BareMetalLoadBalancerNodePoolConfigOut"]
            ).optional(),
            "addressPools": t.array(
                t.proxy(renames["BareMetalLoadBalancerAddressPoolOut"])
            ),
            "asn": t.string(),
            "bgpPeerConfigs": t.array(t.proxy(renames["BareMetalBgpPeerConfigOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalBgpLbConfigOut"])
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
    types["BareMetalNetworkConfigIn"] = t.struct(
        {
            "multipleNetworkInterfacesConfig": t.proxy(
                renames["BareMetalMultipleNetworkInterfacesConfigIn"]
            ).optional(),
            "srIovConfig": t.proxy(renames["BareMetalSrIovConfigIn"]).optional(),
            "advancedNetworking": t.boolean().optional(),
            "islandModeCidr": t.proxy(
                renames["BareMetalIslandModeCidrConfigIn"]
            ).optional(),
        }
    ).named(renames["BareMetalNetworkConfigIn"])
    types["BareMetalNetworkConfigOut"] = t.struct(
        {
            "multipleNetworkInterfacesConfig": t.proxy(
                renames["BareMetalMultipleNetworkInterfacesConfigOut"]
            ).optional(),
            "srIovConfig": t.proxy(renames["BareMetalSrIovConfigOut"]).optional(),
            "advancedNetworking": t.boolean().optional(),
            "islandModeCidr": t.proxy(
                renames["BareMetalIslandModeCidrConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalNetworkConfigOut"])
    types["EnrollVmwareNodePoolRequestIn"] = t.struct(
        {"vmwareNodePoolId": t.string().optional()}
    ).named(renames["EnrollVmwareNodePoolRequestIn"])
    types["EnrollVmwareNodePoolRequestOut"] = t.struct(
        {
            "vmwareNodePoolId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnrollVmwareNodePoolRequestOut"])
    types["VmwareClusterIn"] = t.struct(
        {
            "autoRepairConfig": t.proxy(renames["VmwareAutoRepairConfigIn"]).optional(),
            "authorization": t.proxy(renames["AuthorizationIn"]).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "vmTrackingEnabled": t.boolean().optional(),
            "antiAffinityGroups": t.proxy(renames["VmwareAAGConfigIn"]).optional(),
            "name": t.string().optional(),
            "enableControlPlaneV2": t.boolean().optional(),
            "etag": t.string().optional(),
            "networkConfig": t.proxy(renames["VmwareNetworkConfigIn"]).optional(),
            "dataplaneV2": t.proxy(renames["VmwareDataplaneV2ConfigIn"]).optional(),
            "storage": t.proxy(renames["VmwareStorageConfigIn"]).optional(),
            "loadBalancer": t.proxy(renames["VmwareLoadBalancerConfigIn"]).optional(),
            "adminClusterMembership": t.string(),
            "controlPlaneNode": t.proxy(
                renames["VmwareControlPlaneNodeConfigIn"]
            ).optional(),
            "onPremVersion": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["VmwareClusterIn"])
    types["VmwareClusterOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "autoRepairConfig": t.proxy(
                renames["VmwareAutoRepairConfigOut"]
            ).optional(),
            "authorization": t.proxy(renames["AuthorizationOut"]).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "vmTrackingEnabled": t.boolean().optional(),
            "antiAffinityGroups": t.proxy(renames["VmwareAAGConfigOut"]).optional(),
            "name": t.string().optional(),
            "enableControlPlaneV2": t.boolean().optional(),
            "etag": t.string().optional(),
            "updateTime": t.string().optional(),
            "networkConfig": t.proxy(renames["VmwareNetworkConfigOut"]).optional(),
            "adminClusterName": t.string().optional(),
            "fleet": t.proxy(renames["FleetOut"]).optional(),
            "dataplaneV2": t.proxy(renames["VmwareDataplaneV2ConfigOut"]).optional(),
            "storage": t.proxy(renames["VmwareStorageConfigOut"]).optional(),
            "localName": t.string().optional(),
            "reconciling": t.boolean().optional(),
            "loadBalancer": t.proxy(renames["VmwareLoadBalancerConfigOut"]).optional(),
            "state": t.string().optional(),
            "vcenter": t.proxy(renames["VmwareVCenterConfigOut"]).optional(),
            "status": t.proxy(renames["ResourceStatusOut"]).optional(),
            "adminClusterMembership": t.string(),
            "controlPlaneNode": t.proxy(
                renames["VmwareControlPlaneNodeConfigOut"]
            ).optional(),
            "deleteTime": t.string().optional(),
            "onPremVersion": t.string().optional(),
            "endpoint": t.string().optional(),
            "uid": t.string().optional(),
            "description": t.string().optional(),
            "validationCheck": t.proxy(renames["ValidationCheckOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareClusterOut"])
    types["BareMetalSrIovConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["BareMetalSrIovConfigIn"])
    types["BareMetalSrIovConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalSrIovConfigOut"])
    types["BareMetalAdminDrainedMachineIn"] = t.struct(
        {"nodeIp": t.string().optional()}
    ).named(renames["BareMetalAdminDrainedMachineIn"])
    types["BareMetalAdminDrainedMachineOut"] = t.struct(
        {
            "nodeIp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminDrainedMachineOut"])
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
    types["BareMetalAdminIslandModeCidrConfigIn"] = t.struct(
        {
            "serviceAddressCidrBlocks": t.array(t.string()),
            "podAddressCidrBlocks": t.array(t.string()),
        }
    ).named(renames["BareMetalAdminIslandModeCidrConfigIn"])
    types["BareMetalAdminIslandModeCidrConfigOut"] = t.struct(
        {
            "serviceAddressCidrBlocks": t.array(t.string()),
            "podAddressCidrBlocks": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminIslandModeCidrConfigOut"])
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
    types["VmwareAdminClusterIn"] = t.struct(
        {
            "imageType": t.string().optional(),
            "autoRepairConfig": t.proxy(renames["VmwareAutoRepairConfigIn"]).optional(),
            "networkConfig": t.proxy(renames["VmwareAdminNetworkConfigIn"]).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "bootstrapClusterMembership": t.string().optional(),
            "platformConfig": t.proxy(renames["VmwarePlatformConfigIn"]).optional(),
            "etag": t.string().optional(),
            "loadBalancer": t.proxy(
                renames["VmwareAdminLoadBalancerConfigIn"]
            ).optional(),
            "controlPlaneNode": t.proxy(
                renames["VmwareAdminControlPlaneNodeConfigIn"]
            ).optional(),
            "name": t.string().optional(),
            "onPremVersion": t.string().optional(),
            "description": t.string().optional(),
            "vcenter": t.proxy(renames["VmwareAdminVCenterConfigIn"]).optional(),
            "antiAffinityGroups": t.proxy(renames["VmwareAAGConfigIn"]).optional(),
            "addonNode": t.proxy(renames["VmwareAdminAddonNodeConfigIn"]).optional(),
        }
    ).named(renames["VmwareAdminClusterIn"])
    types["VmwareAdminClusterOut"] = t.struct(
        {
            "imageType": t.string().optional(),
            "autoRepairConfig": t.proxy(
                renames["VmwareAutoRepairConfigOut"]
            ).optional(),
            "networkConfig": t.proxy(renames["VmwareAdminNetworkConfigOut"]).optional(),
            "reconciling": t.boolean().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "localName": t.string().optional(),
            "bootstrapClusterMembership": t.string().optional(),
            "platformConfig": t.proxy(renames["VmwarePlatformConfigOut"]).optional(),
            "endpoint": t.string().optional(),
            "updateTime": t.string().optional(),
            "status": t.proxy(renames["ResourceStatusOut"]).optional(),
            "state": t.string().optional(),
            "etag": t.string().optional(),
            "loadBalancer": t.proxy(
                renames["VmwareAdminLoadBalancerConfigOut"]
            ).optional(),
            "uid": t.string().optional(),
            "fleet": t.proxy(renames["FleetOut"]).optional(),
            "controlPlaneNode": t.proxy(
                renames["VmwareAdminControlPlaneNodeConfigOut"]
            ).optional(),
            "name": t.string().optional(),
            "onPremVersion": t.string().optional(),
            "description": t.string().optional(),
            "vcenter": t.proxy(renames["VmwareAdminVCenterConfigOut"]).optional(),
            "antiAffinityGroups": t.proxy(renames["VmwareAAGConfigOut"]).optional(),
            "addonNode": t.proxy(renames["VmwareAdminAddonNodeConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareAdminClusterOut"])
    types["BareMetalAdminVipConfigIn"] = t.struct(
        {"controlPlaneVip": t.string().optional()}
    ).named(renames["BareMetalAdminVipConfigIn"])
    types["BareMetalAdminVipConfigOut"] = t.struct(
        {
            "controlPlaneVip": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminVipConfigOut"])
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
    types["BindingIn"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["ValidationCheckStatusIn"] = t.struct(
        {"result": t.array(t.proxy(renames["ValidationCheckResultIn"])).optional()}
    ).named(renames["ValidationCheckStatusIn"])
    types["ValidationCheckStatusOut"] = t.struct(
        {
            "result": t.array(t.proxy(renames["ValidationCheckResultOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidationCheckStatusOut"])
    types["VmwareStaticIpConfigIn"] = t.struct(
        {"ipBlocks": t.array(t.proxy(renames["VmwareIpBlockIn"])).optional()}
    ).named(renames["VmwareStaticIpConfigIn"])
    types["VmwareStaticIpConfigOut"] = t.struct(
        {
            "ipBlocks": t.array(t.proxy(renames["VmwareIpBlockOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareStaticIpConfigOut"])
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
    types["VmwareAdminMetalLbConfigIn"] = t.struct({"_": t.string().optional()}).named(
        renames["VmwareAdminMetalLbConfigIn"]
    )
    types["VmwareAdminMetalLbConfigOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["VmwareAdminMetalLbConfigOut"])
    types["LocationIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["BareMetalAdminLoadBalancerConfigIn"] = t.struct(
        {
            "portConfig": t.proxy(renames["BareMetalAdminPortConfigIn"]).optional(),
            "vipConfig": t.proxy(renames["BareMetalAdminVipConfigIn"]).optional(),
            "manualLbConfig": t.proxy(
                renames["BareMetalAdminManualLbConfigIn"]
            ).optional(),
        }
    ).named(renames["BareMetalAdminLoadBalancerConfigIn"])
    types["BareMetalAdminLoadBalancerConfigOut"] = t.struct(
        {
            "portConfig": t.proxy(renames["BareMetalAdminPortConfigOut"]).optional(),
            "vipConfig": t.proxy(renames["BareMetalAdminVipConfigOut"]).optional(),
            "manualLbConfig": t.proxy(
                renames["BareMetalAdminManualLbConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminLoadBalancerConfigOut"])
    types["BareMetalClusterOperationsConfigIn"] = t.struct(
        {"enableApplicationLogs": t.boolean().optional()}
    ).named(renames["BareMetalClusterOperationsConfigIn"])
    types["BareMetalClusterOperationsConfigOut"] = t.struct(
        {
            "enableApplicationLogs": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalClusterOperationsConfigOut"])
    types["BareMetalNodePoolConfigIn"] = t.struct(
        {
            "nodeConfigs": t.array(t.proxy(renames["BareMetalNodeConfigIn"])),
            "operatingSystem": t.string().optional(),
            "kubeletConfig": t.proxy(renames["BareMetalKubeletConfigIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "taints": t.array(t.proxy(renames["NodeTaintIn"])).optional(),
        }
    ).named(renames["BareMetalNodePoolConfigIn"])
    types["BareMetalNodePoolConfigOut"] = t.struct(
        {
            "nodeConfigs": t.array(t.proxy(renames["BareMetalNodeConfigOut"])),
            "operatingSystem": t.string().optional(),
            "kubeletConfig": t.proxy(renames["BareMetalKubeletConfigOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "taints": t.array(t.proxy(renames["NodeTaintOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalNodePoolConfigOut"])

    functions = {}
    functions["projectsLocationsList"] = gkeonprem.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = gkeonprem.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalAdminClustersEnroll"] = gkeonprem.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BareMetalAdminClusterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalAdminClustersSetIamPolicy"] = gkeonprem.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BareMetalAdminClusterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalAdminClustersUnenroll"] = gkeonprem.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BareMetalAdminClusterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalAdminClustersGetIamPolicy"] = gkeonprem.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BareMetalAdminClusterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalAdminClustersPatch"] = gkeonprem.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BareMetalAdminClusterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsBareMetalAdminClustersQueryVersionConfig"
    ] = gkeonprem.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BareMetalAdminClusterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalAdminClustersList"] = gkeonprem.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BareMetalAdminClusterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalAdminClustersCreate"] = gkeonprem.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BareMetalAdminClusterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsBareMetalAdminClustersTestIamPermissions"
    ] = gkeonprem.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BareMetalAdminClusterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalAdminClustersGet"] = gkeonprem.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BareMetalAdminClusterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalAdminClustersOperationsGet"] = gkeonprem.get(
        "v1/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = gkeonprem.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = gkeonprem.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = gkeonprem.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = gkeonprem.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareAdminClustersUnenroll"] = gkeonprem.get(
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
    functions["projectsLocationsVmwareAdminClustersEnroll"] = gkeonprem.get(
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
    functions["projectsLocationsVmwareAdminClustersPatch"] = gkeonprem.get(
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
    functions["projectsLocationsVmwareAdminClustersSetIamPolicy"] = gkeonprem.get(
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
    functions["projectsLocationsVmwareAdminClustersTestIamPermissions"] = gkeonprem.get(
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
    functions["projectsLocationsVmwareAdminClustersList"] = gkeonprem.get(
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
    functions["projectsLocationsVmwareAdminClustersGet"] = gkeonprem.get(
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
    functions["projectsLocationsVmwareAdminClustersGetIamPolicy"] = gkeonprem.get(
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
    functions["projectsLocationsVmwareClustersGet"] = gkeonprem.delete(
        "v1/{name}:unenroll",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "force": t.boolean().optional(),
                "etag": t.string().optional(),
                "name": t.string(),
                "allowMissing": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersSetIamPolicy"] = gkeonprem.delete(
        "v1/{name}:unenroll",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "force": t.boolean().optional(),
                "etag": t.string().optional(),
                "name": t.string(),
                "allowMissing": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersList"] = gkeonprem.delete(
        "v1/{name}:unenroll",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "force": t.boolean().optional(),
                "etag": t.string().optional(),
                "name": t.string(),
                "allowMissing": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersDelete"] = gkeonprem.delete(
        "v1/{name}:unenroll",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "force": t.boolean().optional(),
                "etag": t.string().optional(),
                "name": t.string(),
                "allowMissing": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersCreate"] = gkeonprem.delete(
        "v1/{name}:unenroll",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "force": t.boolean().optional(),
                "etag": t.string().optional(),
                "name": t.string(),
                "allowMissing": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersGetIamPolicy"] = gkeonprem.delete(
        "v1/{name}:unenroll",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "force": t.boolean().optional(),
                "etag": t.string().optional(),
                "name": t.string(),
                "allowMissing": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersTestIamPermissions"] = gkeonprem.delete(
        "v1/{name}:unenroll",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "force": t.boolean().optional(),
                "etag": t.string().optional(),
                "name": t.string(),
                "allowMissing": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersPatch"] = gkeonprem.delete(
        "v1/{name}:unenroll",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "force": t.boolean().optional(),
                "etag": t.string().optional(),
                "name": t.string(),
                "allowMissing": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersEnroll"] = gkeonprem.delete(
        "v1/{name}:unenroll",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "force": t.boolean().optional(),
                "etag": t.string().optional(),
                "name": t.string(),
                "allowMissing": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersQueryVersionConfig"] = gkeonprem.delete(
        "v1/{name}:unenroll",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "force": t.boolean().optional(),
                "etag": t.string().optional(),
                "name": t.string(),
                "allowMissing": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersUnenroll"] = gkeonprem.delete(
        "v1/{name}:unenroll",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "force": t.boolean().optional(),
                "etag": t.string().optional(),
                "name": t.string(),
                "allowMissing": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersVmwareNodePoolsEnroll"] = gkeonprem.get(
        "v1/{parent}/vmwareNodePools",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListVmwareNodePoolsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsVmwareClustersVmwareNodePoolsGetIamPolicy"
    ] = gkeonprem.get(
        "v1/{parent}/vmwareNodePools",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListVmwareNodePoolsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersVmwareNodePoolsUnenroll"] = gkeonprem.get(
        "v1/{parent}/vmwareNodePools",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListVmwareNodePoolsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersVmwareNodePoolsPatch"] = gkeonprem.get(
        "v1/{parent}/vmwareNodePools",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListVmwareNodePoolsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersVmwareNodePoolsCreate"] = gkeonprem.get(
        "v1/{parent}/vmwareNodePools",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListVmwareNodePoolsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsVmwareClustersVmwareNodePoolsSetIamPolicy"
    ] = gkeonprem.get(
        "v1/{parent}/vmwareNodePools",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListVmwareNodePoolsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsVmwareClustersVmwareNodePoolsTestIamPermissions"
    ] = gkeonprem.get(
        "v1/{parent}/vmwareNodePools",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListVmwareNodePoolsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersVmwareNodePoolsGet"] = gkeonprem.get(
        "v1/{parent}/vmwareNodePools",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListVmwareNodePoolsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersVmwareNodePoolsDelete"] = gkeonprem.get(
        "v1/{parent}/vmwareNodePools",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListVmwareNodePoolsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersVmwareNodePoolsList"] = gkeonprem.get(
        "v1/{parent}/vmwareNodePools",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListVmwareNodePoolsResponseOut"]),
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
    functions["projectsLocationsBareMetalClustersTestIamPermissions"] = gkeonprem.post(
        "v1/{parent}/bareMetalClusters:enroll",
        t.struct(
            {
                "parent": t.string(),
                "localName": t.string().optional(),
                "bareMetalClusterId": t.string().optional(),
                "adminClusterMembership": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalClustersUnenroll"] = gkeonprem.post(
        "v1/{parent}/bareMetalClusters:enroll",
        t.struct(
            {
                "parent": t.string(),
                "localName": t.string().optional(),
                "bareMetalClusterId": t.string().optional(),
                "adminClusterMembership": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalClustersQueryVersionConfig"] = gkeonprem.post(
        "v1/{parent}/bareMetalClusters:enroll",
        t.struct(
            {
                "parent": t.string(),
                "localName": t.string().optional(),
                "bareMetalClusterId": t.string().optional(),
                "adminClusterMembership": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalClustersPatch"] = gkeonprem.post(
        "v1/{parent}/bareMetalClusters:enroll",
        t.struct(
            {
                "parent": t.string(),
                "localName": t.string().optional(),
                "bareMetalClusterId": t.string().optional(),
                "adminClusterMembership": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalClustersDelete"] = gkeonprem.post(
        "v1/{parent}/bareMetalClusters:enroll",
        t.struct(
            {
                "parent": t.string(),
                "localName": t.string().optional(),
                "bareMetalClusterId": t.string().optional(),
                "adminClusterMembership": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalClustersCreate"] = gkeonprem.post(
        "v1/{parent}/bareMetalClusters:enroll",
        t.struct(
            {
                "parent": t.string(),
                "localName": t.string().optional(),
                "bareMetalClusterId": t.string().optional(),
                "adminClusterMembership": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalClustersGet"] = gkeonprem.post(
        "v1/{parent}/bareMetalClusters:enroll",
        t.struct(
            {
                "parent": t.string(),
                "localName": t.string().optional(),
                "bareMetalClusterId": t.string().optional(),
                "adminClusterMembership": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalClustersSetIamPolicy"] = gkeonprem.post(
        "v1/{parent}/bareMetalClusters:enroll",
        t.struct(
            {
                "parent": t.string(),
                "localName": t.string().optional(),
                "bareMetalClusterId": t.string().optional(),
                "adminClusterMembership": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalClustersGetIamPolicy"] = gkeonprem.post(
        "v1/{parent}/bareMetalClusters:enroll",
        t.struct(
            {
                "parent": t.string(),
                "localName": t.string().optional(),
                "bareMetalClusterId": t.string().optional(),
                "adminClusterMembership": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalClustersList"] = gkeonprem.post(
        "v1/{parent}/bareMetalClusters:enroll",
        t.struct(
            {
                "parent": t.string(),
                "localName": t.string().optional(),
                "bareMetalClusterId": t.string().optional(),
                "adminClusterMembership": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalClustersEnroll"] = gkeonprem.post(
        "v1/{parent}/bareMetalClusters:enroll",
        t.struct(
            {
                "parent": t.string(),
                "localName": t.string().optional(),
                "bareMetalClusterId": t.string().optional(),
                "adminClusterMembership": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsBareMetalClustersBareMetalNodePoolsEnroll"
    ] = gkeonprem.post(
        "v1/{parent}/bareMetalNodePools",
        t.struct(
            {
                "parent": t.string(),
                "validateOnly": t.boolean().optional(),
                "bareMetalNodePoolId": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string().optional(),
                "name": t.string().optional(),
                "nodePoolConfig": t.proxy(renames["BareMetalNodePoolConfigIn"]),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsBareMetalClustersBareMetalNodePoolsTestIamPermissions"
    ] = gkeonprem.post(
        "v1/{parent}/bareMetalNodePools",
        t.struct(
            {
                "parent": t.string(),
                "validateOnly": t.boolean().optional(),
                "bareMetalNodePoolId": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string().optional(),
                "name": t.string().optional(),
                "nodePoolConfig": t.proxy(renames["BareMetalNodePoolConfigIn"]),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsBareMetalClustersBareMetalNodePoolsGet"
    ] = gkeonprem.post(
        "v1/{parent}/bareMetalNodePools",
        t.struct(
            {
                "parent": t.string(),
                "validateOnly": t.boolean().optional(),
                "bareMetalNodePoolId": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string().optional(),
                "name": t.string().optional(),
                "nodePoolConfig": t.proxy(renames["BareMetalNodePoolConfigIn"]),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsBareMetalClustersBareMetalNodePoolsGetIamPolicy"
    ] = gkeonprem.post(
        "v1/{parent}/bareMetalNodePools",
        t.struct(
            {
                "parent": t.string(),
                "validateOnly": t.boolean().optional(),
                "bareMetalNodePoolId": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string().optional(),
                "name": t.string().optional(),
                "nodePoolConfig": t.proxy(renames["BareMetalNodePoolConfigIn"]),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsBareMetalClustersBareMetalNodePoolsList"
    ] = gkeonprem.post(
        "v1/{parent}/bareMetalNodePools",
        t.struct(
            {
                "parent": t.string(),
                "validateOnly": t.boolean().optional(),
                "bareMetalNodePoolId": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string().optional(),
                "name": t.string().optional(),
                "nodePoolConfig": t.proxy(renames["BareMetalNodePoolConfigIn"]),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsBareMetalClustersBareMetalNodePoolsSetIamPolicy"
    ] = gkeonprem.post(
        "v1/{parent}/bareMetalNodePools",
        t.struct(
            {
                "parent": t.string(),
                "validateOnly": t.boolean().optional(),
                "bareMetalNodePoolId": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string().optional(),
                "name": t.string().optional(),
                "nodePoolConfig": t.proxy(renames["BareMetalNodePoolConfigIn"]),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsBareMetalClustersBareMetalNodePoolsDelete"
    ] = gkeonprem.post(
        "v1/{parent}/bareMetalNodePools",
        t.struct(
            {
                "parent": t.string(),
                "validateOnly": t.boolean().optional(),
                "bareMetalNodePoolId": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string().optional(),
                "name": t.string().optional(),
                "nodePoolConfig": t.proxy(renames["BareMetalNodePoolConfigIn"]),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsBareMetalClustersBareMetalNodePoolsPatch"
    ] = gkeonprem.post(
        "v1/{parent}/bareMetalNodePools",
        t.struct(
            {
                "parent": t.string(),
                "validateOnly": t.boolean().optional(),
                "bareMetalNodePoolId": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string().optional(),
                "name": t.string().optional(),
                "nodePoolConfig": t.proxy(renames["BareMetalNodePoolConfigIn"]),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsBareMetalClustersBareMetalNodePoolsUnenroll"
    ] = gkeonprem.post(
        "v1/{parent}/bareMetalNodePools",
        t.struct(
            {
                "parent": t.string(),
                "validateOnly": t.boolean().optional(),
                "bareMetalNodePoolId": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string().optional(),
                "name": t.string().optional(),
                "nodePoolConfig": t.proxy(renames["BareMetalNodePoolConfigIn"]),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsBareMetalClustersBareMetalNodePoolsCreate"
    ] = gkeonprem.post(
        "v1/{parent}/bareMetalNodePools",
        t.struct(
            {
                "parent": t.string(),
                "validateOnly": t.boolean().optional(),
                "bareMetalNodePoolId": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string().optional(),
                "name": t.string().optional(),
                "nodePoolConfig": t.proxy(renames["BareMetalNodePoolConfigIn"]),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsBareMetalClustersBareMetalNodePoolsOperationsGet"
    ] = gkeonprem.get(
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
    functions[
        "projectsLocationsBareMetalClustersBareMetalNodePoolsOperationsList"
    ] = gkeonprem.get(
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
    functions["projectsLocationsBareMetalClustersOperationsGet"] = gkeonprem.get(
        "v1/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
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
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="gkeonprem", renames=renames, types=types, functions=functions
    )
