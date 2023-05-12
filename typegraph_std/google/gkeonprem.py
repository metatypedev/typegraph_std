from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_gkeonprem() -> Import:
    gkeonprem = HTTPRuntime("https://gkeonprem.googleapis.com/")

    renames = {
        "ErrorResponse": "_gkeonprem_1_ErrorResponse",
        "BareMetalAdminSecurityConfigIn": "_gkeonprem_2_BareMetalAdminSecurityConfigIn",
        "BareMetalAdminSecurityConfigOut": "_gkeonprem_3_BareMetalAdminSecurityConfigOut",
        "BareMetalAdminApiServerArgumentIn": "_gkeonprem_4_BareMetalAdminApiServerArgumentIn",
        "BareMetalAdminApiServerArgumentOut": "_gkeonprem_5_BareMetalAdminApiServerArgumentOut",
        "QueryBareMetalVersionConfigResponseIn": "_gkeonprem_6_QueryBareMetalVersionConfigResponseIn",
        "QueryBareMetalVersionConfigResponseOut": "_gkeonprem_7_QueryBareMetalVersionConfigResponseOut",
        "ListBareMetalAdminClustersResponseIn": "_gkeonprem_8_ListBareMetalAdminClustersResponseIn",
        "ListBareMetalAdminClustersResponseOut": "_gkeonprem_9_ListBareMetalAdminClustersResponseOut",
        "ValidationCheckIn": "_gkeonprem_10_ValidationCheckIn",
        "ValidationCheckOut": "_gkeonprem_11_ValidationCheckOut",
        "EnrollVmwareAdminClusterRequestIn": "_gkeonprem_12_EnrollVmwareAdminClusterRequestIn",
        "EnrollVmwareAdminClusterRequestOut": "_gkeonprem_13_EnrollVmwareAdminClusterRequestOut",
        "BareMetalPortConfigIn": "_gkeonprem_14_BareMetalPortConfigIn",
        "BareMetalPortConfigOut": "_gkeonprem_15_BareMetalPortConfigOut",
        "OperationMetadataIn": "_gkeonprem_16_OperationMetadataIn",
        "OperationMetadataOut": "_gkeonprem_17_OperationMetadataOut",
        "BareMetalWorkloadNodeConfigIn": "_gkeonprem_18_BareMetalWorkloadNodeConfigIn",
        "BareMetalWorkloadNodeConfigOut": "_gkeonprem_19_BareMetalWorkloadNodeConfigOut",
        "BareMetalAdminManualLbConfigIn": "_gkeonprem_20_BareMetalAdminManualLbConfigIn",
        "BareMetalAdminManualLbConfigOut": "_gkeonprem_21_BareMetalAdminManualLbConfigOut",
        "FleetIn": "_gkeonprem_22_FleetIn",
        "FleetOut": "_gkeonprem_23_FleetOut",
        "BareMetalAdminNetworkConfigIn": "_gkeonprem_24_BareMetalAdminNetworkConfigIn",
        "BareMetalAdminNetworkConfigOut": "_gkeonprem_25_BareMetalAdminNetworkConfigOut",
        "ResourceConditionIn": "_gkeonprem_26_ResourceConditionIn",
        "ResourceConditionOut": "_gkeonprem_27_ResourceConditionOut",
        "VmwareIpBlockIn": "_gkeonprem_28_VmwareIpBlockIn",
        "VmwareIpBlockOut": "_gkeonprem_29_VmwareIpBlockOut",
        "OperationIn": "_gkeonprem_30_OperationIn",
        "OperationOut": "_gkeonprem_31_OperationOut",
        "VmwareBundleConfigIn": "_gkeonprem_32_VmwareBundleConfigIn",
        "VmwareBundleConfigOut": "_gkeonprem_33_VmwareBundleConfigOut",
        "VmwareControlPlaneV2ConfigIn": "_gkeonprem_34_VmwareControlPlaneV2ConfigIn",
        "VmwareControlPlaneV2ConfigOut": "_gkeonprem_35_VmwareControlPlaneV2ConfigOut",
        "ListBareMetalClustersResponseIn": "_gkeonprem_36_ListBareMetalClustersResponseIn",
        "ListBareMetalClustersResponseOut": "_gkeonprem_37_ListBareMetalClustersResponseOut",
        "SetIamPolicyRequestIn": "_gkeonprem_38_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_gkeonprem_39_SetIamPolicyRequestOut",
        "BareMetalAdminDrainingMachineIn": "_gkeonprem_40_BareMetalAdminDrainingMachineIn",
        "BareMetalAdminDrainingMachineOut": "_gkeonprem_41_BareMetalAdminDrainingMachineOut",
        "VmwareVsphereConfigIn": "_gkeonprem_42_VmwareVsphereConfigIn",
        "VmwareVsphereConfigOut": "_gkeonprem_43_VmwareVsphereConfigOut",
        "BareMetalAdminOsEnvironmentConfigIn": "_gkeonprem_44_BareMetalAdminOsEnvironmentConfigIn",
        "BareMetalAdminOsEnvironmentConfigOut": "_gkeonprem_45_BareMetalAdminOsEnvironmentConfigOut",
        "ExprIn": "_gkeonprem_46_ExprIn",
        "ExprOut": "_gkeonprem_47_ExprOut",
        "BareMetalAdminVipConfigIn": "_gkeonprem_48_BareMetalAdminVipConfigIn",
        "BareMetalAdminVipConfigOut": "_gkeonprem_49_BareMetalAdminVipConfigOut",
        "VmwareNodePoolAutoscalingConfigIn": "_gkeonprem_50_VmwareNodePoolAutoscalingConfigIn",
        "VmwareNodePoolAutoscalingConfigOut": "_gkeonprem_51_VmwareNodePoolAutoscalingConfigOut",
        "VmwareNetworkConfigIn": "_gkeonprem_52_VmwareNetworkConfigIn",
        "VmwareNetworkConfigOut": "_gkeonprem_53_VmwareNetworkConfigOut",
        "VmwareDataplaneV2ConfigIn": "_gkeonprem_54_VmwareDataplaneV2ConfigIn",
        "VmwareDataplaneV2ConfigOut": "_gkeonprem_55_VmwareDataplaneV2ConfigOut",
        "PolicyIn": "_gkeonprem_56_PolicyIn",
        "PolicyOut": "_gkeonprem_57_PolicyOut",
        "BareMetalAdminControlPlaneNodePoolConfigIn": "_gkeonprem_58_BareMetalAdminControlPlaneNodePoolConfigIn",
        "BareMetalAdminControlPlaneNodePoolConfigOut": "_gkeonprem_59_BareMetalAdminControlPlaneNodePoolConfigOut",
        "LocationIn": "_gkeonprem_60_LocationIn",
        "LocationOut": "_gkeonprem_61_LocationOut",
        "BareMetalKubeletConfigIn": "_gkeonprem_62_BareMetalKubeletConfigIn",
        "BareMetalKubeletConfigOut": "_gkeonprem_63_BareMetalKubeletConfigOut",
        "BareMetalVersionInfoIn": "_gkeonprem_64_BareMetalVersionInfoIn",
        "BareMetalVersionInfoOut": "_gkeonprem_65_BareMetalVersionInfoOut",
        "BareMetalAdminProxyConfigIn": "_gkeonprem_66_BareMetalAdminProxyConfigIn",
        "BareMetalAdminProxyConfigOut": "_gkeonprem_67_BareMetalAdminProxyConfigOut",
        "BareMetalAdminIslandModeCidrConfigIn": "_gkeonprem_68_BareMetalAdminIslandModeCidrConfigIn",
        "BareMetalAdminIslandModeCidrConfigOut": "_gkeonprem_69_BareMetalAdminIslandModeCidrConfigOut",
        "BareMetalLvpShareConfigIn": "_gkeonprem_70_BareMetalLvpShareConfigIn",
        "BareMetalLvpShareConfigOut": "_gkeonprem_71_BareMetalLvpShareConfigOut",
        "ResourceStatusIn": "_gkeonprem_72_ResourceStatusIn",
        "ResourceStatusOut": "_gkeonprem_73_ResourceStatusOut",
        "TestIamPermissionsResponseIn": "_gkeonprem_74_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_gkeonprem_75_TestIamPermissionsResponseOut",
        "VmwareControlPlaneVsphereConfigIn": "_gkeonprem_76_VmwareControlPlaneVsphereConfigIn",
        "VmwareControlPlaneVsphereConfigOut": "_gkeonprem_77_VmwareControlPlaneVsphereConfigOut",
        "BareMetalMaintenanceStatusIn": "_gkeonprem_78_BareMetalMaintenanceStatusIn",
        "BareMetalMaintenanceStatusOut": "_gkeonprem_79_BareMetalMaintenanceStatusOut",
        "EnrollBareMetalClusterRequestIn": "_gkeonprem_80_EnrollBareMetalClusterRequestIn",
        "EnrollBareMetalClusterRequestOut": "_gkeonprem_81_EnrollBareMetalClusterRequestOut",
        "BareMetalAdminMaintenanceConfigIn": "_gkeonprem_82_BareMetalAdminMaintenanceConfigIn",
        "BareMetalAdminMaintenanceConfigOut": "_gkeonprem_83_BareMetalAdminMaintenanceConfigOut",
        "BareMetalControlPlaneNodePoolConfigIn": "_gkeonprem_84_BareMetalControlPlaneNodePoolConfigIn",
        "BareMetalControlPlaneNodePoolConfigOut": "_gkeonprem_85_BareMetalControlPlaneNodePoolConfigOut",
        "BareMetalAdminWorkloadNodeConfigIn": "_gkeonprem_86_BareMetalAdminWorkloadNodeConfigIn",
        "BareMetalAdminWorkloadNodeConfigOut": "_gkeonprem_87_BareMetalAdminWorkloadNodeConfigOut",
        "VmwareVersionInfoIn": "_gkeonprem_88_VmwareVersionInfoIn",
        "VmwareVersionInfoOut": "_gkeonprem_89_VmwareVersionInfoOut",
        "VmwarePlatformConfigIn": "_gkeonprem_90_VmwarePlatformConfigIn",
        "VmwarePlatformConfigOut": "_gkeonprem_91_VmwarePlatformConfigOut",
        "VmwareNodeConfigIn": "_gkeonprem_92_VmwareNodeConfigIn",
        "VmwareNodeConfigOut": "_gkeonprem_93_VmwareNodeConfigOut",
        "BareMetalAdminStorageConfigIn": "_gkeonprem_94_BareMetalAdminStorageConfigIn",
        "BareMetalAdminStorageConfigOut": "_gkeonprem_95_BareMetalAdminStorageConfigOut",
        "EnrollBareMetalNodePoolRequestIn": "_gkeonprem_96_EnrollBareMetalNodePoolRequestIn",
        "EnrollBareMetalNodePoolRequestOut": "_gkeonprem_97_EnrollBareMetalNodePoolRequestOut",
        "BareMetalAdminMachineDrainStatusIn": "_gkeonprem_98_BareMetalAdminMachineDrainStatusIn",
        "BareMetalAdminMachineDrainStatusOut": "_gkeonprem_99_BareMetalAdminMachineDrainStatusOut",
        "VmwareClusterIn": "_gkeonprem_100_VmwareClusterIn",
        "VmwareClusterOut": "_gkeonprem_101_VmwareClusterOut",
        "BareMetalClusterOperationsConfigIn": "_gkeonprem_102_BareMetalClusterOperationsConfigIn",
        "BareMetalClusterOperationsConfigOut": "_gkeonprem_103_BareMetalClusterOperationsConfigOut",
        "VmwareAAGConfigIn": "_gkeonprem_104_VmwareAAGConfigIn",
        "VmwareAAGConfigOut": "_gkeonprem_105_VmwareAAGConfigOut",
        "ListBareMetalNodePoolsResponseIn": "_gkeonprem_106_ListBareMetalNodePoolsResponseIn",
        "ListBareMetalNodePoolsResponseOut": "_gkeonprem_107_ListBareMetalNodePoolsResponseOut",
        "VmwareAdminManualLbConfigIn": "_gkeonprem_108_VmwareAdminManualLbConfigIn",
        "VmwareAdminManualLbConfigOut": "_gkeonprem_109_VmwareAdminManualLbConfigOut",
        "BareMetalNodeAccessConfigIn": "_gkeonprem_110_BareMetalNodeAccessConfigIn",
        "BareMetalNodeAccessConfigOut": "_gkeonprem_111_BareMetalNodeAccessConfigOut",
        "ListOperationsResponseIn": "_gkeonprem_112_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_gkeonprem_113_ListOperationsResponseOut",
        "StatusIn": "_gkeonprem_114_StatusIn",
        "StatusOut": "_gkeonprem_115_StatusOut",
        "BareMetalNodePoolIn": "_gkeonprem_116_BareMetalNodePoolIn",
        "BareMetalNodePoolOut": "_gkeonprem_117_BareMetalNodePoolOut",
        "BareMetalMetalLbConfigIn": "_gkeonprem_118_BareMetalMetalLbConfigIn",
        "BareMetalMetalLbConfigOut": "_gkeonprem_119_BareMetalMetalLbConfigOut",
        "ListVmwareClustersResponseIn": "_gkeonprem_120_ListVmwareClustersResponseIn",
        "ListVmwareClustersResponseOut": "_gkeonprem_121_ListVmwareClustersResponseOut",
        "BareMetalMaintenanceConfigIn": "_gkeonprem_122_BareMetalMaintenanceConfigIn",
        "BareMetalMaintenanceConfigOut": "_gkeonprem_123_BareMetalMaintenanceConfigOut",
        "BareMetalMultipleNetworkInterfacesConfigIn": "_gkeonprem_124_BareMetalMultipleNetworkInterfacesConfigIn",
        "BareMetalMultipleNetworkInterfacesConfigOut": "_gkeonprem_125_BareMetalMultipleNetworkInterfacesConfigOut",
        "QueryVmwareVersionConfigResponseIn": "_gkeonprem_126_QueryVmwareVersionConfigResponseIn",
        "QueryVmwareVersionConfigResponseOut": "_gkeonprem_127_QueryVmwareVersionConfigResponseOut",
        "BareMetalAdminControlPlaneConfigIn": "_gkeonprem_128_BareMetalAdminControlPlaneConfigIn",
        "BareMetalAdminControlPlaneConfigOut": "_gkeonprem_129_BareMetalAdminControlPlaneConfigOut",
        "BareMetalAdminNodeAccessConfigIn": "_gkeonprem_130_BareMetalAdminNodeAccessConfigIn",
        "BareMetalAdminNodeAccessConfigOut": "_gkeonprem_131_BareMetalAdminNodeAccessConfigOut",
        "BareMetalProxyConfigIn": "_gkeonprem_132_BareMetalProxyConfigIn",
        "BareMetalProxyConfigOut": "_gkeonprem_133_BareMetalProxyConfigOut",
        "BareMetalAdminPortConfigIn": "_gkeonprem_134_BareMetalAdminPortConfigIn",
        "BareMetalAdminPortConfigOut": "_gkeonprem_135_BareMetalAdminPortConfigOut",
        "BareMetalAdminClusterIn": "_gkeonprem_136_BareMetalAdminClusterIn",
        "BareMetalAdminClusterOut": "_gkeonprem_137_BareMetalAdminClusterOut",
        "BareMetalOsEnvironmentConfigIn": "_gkeonprem_138_BareMetalOsEnvironmentConfigIn",
        "BareMetalOsEnvironmentConfigOut": "_gkeonprem_139_BareMetalOsEnvironmentConfigOut",
        "VmwareAdminNetworkConfigIn": "_gkeonprem_140_VmwareAdminNetworkConfigIn",
        "VmwareAdminNetworkConfigOut": "_gkeonprem_141_VmwareAdminNetworkConfigOut",
        "VmwareManualLbConfigIn": "_gkeonprem_142_VmwareManualLbConfigIn",
        "VmwareManualLbConfigOut": "_gkeonprem_143_VmwareManualLbConfigOut",
        "BareMetalNodePoolConfigIn": "_gkeonprem_144_BareMetalNodePoolConfigIn",
        "BareMetalNodePoolConfigOut": "_gkeonprem_145_BareMetalNodePoolConfigOut",
        "EmptyIn": "_gkeonprem_146_EmptyIn",
        "EmptyOut": "_gkeonprem_147_EmptyOut",
        "ClusterUserIn": "_gkeonprem_148_ClusterUserIn",
        "ClusterUserOut": "_gkeonprem_149_ClusterUserOut",
        "ListLocationsResponseIn": "_gkeonprem_150_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_gkeonprem_151_ListLocationsResponseOut",
        "BareMetalManualLbConfigIn": "_gkeonprem_152_BareMetalManualLbConfigIn",
        "BareMetalManualLbConfigOut": "_gkeonprem_153_BareMetalManualLbConfigOut",
        "EnrollVmwareClusterRequestIn": "_gkeonprem_154_EnrollVmwareClusterRequestIn",
        "EnrollVmwareClusterRequestOut": "_gkeonprem_155_EnrollVmwareClusterRequestOut",
        "ValidationCheckResultIn": "_gkeonprem_156_ValidationCheckResultIn",
        "ValidationCheckResultOut": "_gkeonprem_157_ValidationCheckResultOut",
        "VmwareAdminMetalLbConfigIn": "_gkeonprem_158_VmwareAdminMetalLbConfigIn",
        "VmwareAdminMetalLbConfigOut": "_gkeonprem_159_VmwareAdminMetalLbConfigOut",
        "EnrollVmwareNodePoolRequestIn": "_gkeonprem_160_EnrollVmwareNodePoolRequestIn",
        "EnrollVmwareNodePoolRequestOut": "_gkeonprem_161_EnrollVmwareNodePoolRequestOut",
        "BareMetalMachineDrainStatusIn": "_gkeonprem_162_BareMetalMachineDrainStatusIn",
        "BareMetalMachineDrainStatusOut": "_gkeonprem_163_BareMetalMachineDrainStatusOut",
        "ValidationCheckStatusIn": "_gkeonprem_164_ValidationCheckStatusIn",
        "ValidationCheckStatusOut": "_gkeonprem_165_ValidationCheckStatusOut",
        "BareMetalApiServerArgumentIn": "_gkeonprem_166_BareMetalApiServerArgumentIn",
        "BareMetalApiServerArgumentOut": "_gkeonprem_167_BareMetalApiServerArgumentOut",
        "BareMetalIslandModeCidrConfigIn": "_gkeonprem_168_BareMetalIslandModeCidrConfigIn",
        "BareMetalIslandModeCidrConfigOut": "_gkeonprem_169_BareMetalIslandModeCidrConfigOut",
        "VmwareAdminVipConfigIn": "_gkeonprem_170_VmwareAdminVipConfigIn",
        "VmwareAdminVipConfigOut": "_gkeonprem_171_VmwareAdminVipConfigOut",
        "TestIamPermissionsRequestIn": "_gkeonprem_172_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_gkeonprem_173_TestIamPermissionsRequestOut",
        "BareMetalNetworkConfigIn": "_gkeonprem_174_BareMetalNetworkConfigIn",
        "BareMetalNetworkConfigOut": "_gkeonprem_175_BareMetalNetworkConfigOut",
        "BareMetalStorageConfigIn": "_gkeonprem_176_BareMetalStorageConfigIn",
        "BareMetalStorageConfigOut": "_gkeonprem_177_BareMetalStorageConfigOut",
        "ListVmwareNodePoolsResponseIn": "_gkeonprem_178_ListVmwareNodePoolsResponseIn",
        "ListVmwareNodePoolsResponseOut": "_gkeonprem_179_ListVmwareNodePoolsResponseOut",
        "ListVmwareAdminClustersResponseIn": "_gkeonprem_180_ListVmwareAdminClustersResponseIn",
        "ListVmwareAdminClustersResponseOut": "_gkeonprem_181_ListVmwareAdminClustersResponseOut",
        "BareMetalSecurityConfigIn": "_gkeonprem_182_BareMetalSecurityConfigIn",
        "BareMetalSecurityConfigOut": "_gkeonprem_183_BareMetalSecurityConfigOut",
        "BareMetalClusterIn": "_gkeonprem_184_BareMetalClusterIn",
        "BareMetalClusterOut": "_gkeonprem_185_BareMetalClusterOut",
        "AuthorizationIn": "_gkeonprem_186_AuthorizationIn",
        "AuthorizationOut": "_gkeonprem_187_AuthorizationOut",
        "VmwareF5BigIpConfigIn": "_gkeonprem_188_VmwareF5BigIpConfigIn",
        "VmwareF5BigIpConfigOut": "_gkeonprem_189_VmwareF5BigIpConfigOut",
        "VmwareHostConfigIn": "_gkeonprem_190_VmwareHostConfigIn",
        "VmwareHostConfigOut": "_gkeonprem_191_VmwareHostConfigOut",
        "VmwareHostIpIn": "_gkeonprem_192_VmwareHostIpIn",
        "VmwareHostIpOut": "_gkeonprem_193_VmwareHostIpOut",
        "VmwareAdminLoadBalancerConfigIn": "_gkeonprem_194_VmwareAdminLoadBalancerConfigIn",
        "VmwareAdminLoadBalancerConfigOut": "_gkeonprem_195_VmwareAdminLoadBalancerConfigOut",
        "BareMetalAdminClusterOperationsConfigIn": "_gkeonprem_196_BareMetalAdminClusterOperationsConfigIn",
        "BareMetalAdminClusterOperationsConfigOut": "_gkeonprem_197_BareMetalAdminClusterOperationsConfigOut",
        "BareMetalControlPlaneConfigIn": "_gkeonprem_198_BareMetalControlPlaneConfigIn",
        "BareMetalControlPlaneConfigOut": "_gkeonprem_199_BareMetalControlPlaneConfigOut",
        "VmwareAutoRepairConfigIn": "_gkeonprem_200_VmwareAutoRepairConfigIn",
        "VmwareAutoRepairConfigOut": "_gkeonprem_201_VmwareAutoRepairConfigOut",
        "BareMetalDrainingMachineIn": "_gkeonprem_202_BareMetalDrainingMachineIn",
        "BareMetalDrainingMachineOut": "_gkeonprem_203_BareMetalDrainingMachineOut",
        "VmwareLoadBalancerConfigIn": "_gkeonprem_204_VmwareLoadBalancerConfigIn",
        "VmwareLoadBalancerConfigOut": "_gkeonprem_205_VmwareLoadBalancerConfigOut",
        "BareMetalNodeConfigIn": "_gkeonprem_206_BareMetalNodeConfigIn",
        "BareMetalNodeConfigOut": "_gkeonprem_207_BareMetalNodeConfigOut",
        "VmwareAdminF5BigIpConfigIn": "_gkeonprem_208_VmwareAdminF5BigIpConfigIn",
        "VmwareAdminF5BigIpConfigOut": "_gkeonprem_209_VmwareAdminF5BigIpConfigOut",
        "VmwareAdminControlPlaneNodeConfigIn": "_gkeonprem_210_VmwareAdminControlPlaneNodeConfigIn",
        "VmwareAdminControlPlaneNodeConfigOut": "_gkeonprem_211_VmwareAdminControlPlaneNodeConfigOut",
        "BareMetalLoadBalancerNodePoolConfigIn": "_gkeonprem_212_BareMetalLoadBalancerNodePoolConfigIn",
        "BareMetalLoadBalancerNodePoolConfigOut": "_gkeonprem_213_BareMetalLoadBalancerNodePoolConfigOut",
        "VmwareMetalLbConfigIn": "_gkeonprem_214_VmwareMetalLbConfigIn",
        "VmwareMetalLbConfigOut": "_gkeonprem_215_VmwareMetalLbConfigOut",
        "CancelOperationRequestIn": "_gkeonprem_216_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_gkeonprem_217_CancelOperationRequestOut",
        "BareMetalBgpPeerConfigIn": "_gkeonprem_218_BareMetalBgpPeerConfigIn",
        "BareMetalBgpPeerConfigOut": "_gkeonprem_219_BareMetalBgpPeerConfigOut",
        "BareMetalLoadBalancerConfigIn": "_gkeonprem_220_BareMetalLoadBalancerConfigIn",
        "BareMetalLoadBalancerConfigOut": "_gkeonprem_221_BareMetalLoadBalancerConfigOut",
        "BareMetalBgpLbConfigIn": "_gkeonprem_222_BareMetalBgpLbConfigIn",
        "BareMetalBgpLbConfigOut": "_gkeonprem_223_BareMetalBgpLbConfigOut",
        "VmwareControlPlaneNodeConfigIn": "_gkeonprem_224_VmwareControlPlaneNodeConfigIn",
        "VmwareControlPlaneNodeConfigOut": "_gkeonprem_225_VmwareControlPlaneNodeConfigOut",
        "BareMetalSrIovConfigIn": "_gkeonprem_226_BareMetalSrIovConfigIn",
        "BareMetalSrIovConfigOut": "_gkeonprem_227_BareMetalSrIovConfigOut",
        "BareMetalLoadBalancerAddressPoolIn": "_gkeonprem_228_BareMetalLoadBalancerAddressPoolIn",
        "BareMetalLoadBalancerAddressPoolOut": "_gkeonprem_229_BareMetalLoadBalancerAddressPoolOut",
        "VmwareVCenterConfigIn": "_gkeonprem_230_VmwareVCenterConfigIn",
        "VmwareVCenterConfigOut": "_gkeonprem_231_VmwareVCenterConfigOut",
        "EnrollBareMetalAdminClusterRequestIn": "_gkeonprem_232_EnrollBareMetalAdminClusterRequestIn",
        "EnrollBareMetalAdminClusterRequestOut": "_gkeonprem_233_EnrollBareMetalAdminClusterRequestOut",
        "VmwareNodePoolIn": "_gkeonprem_234_VmwareNodePoolIn",
        "VmwareNodePoolOut": "_gkeonprem_235_VmwareNodePoolOut",
        "VmwareAdminVCenterConfigIn": "_gkeonprem_236_VmwareAdminVCenterConfigIn",
        "VmwareAdminVCenterConfigOut": "_gkeonprem_237_VmwareAdminVCenterConfigOut",
        "QueryBareMetalAdminVersionConfigResponseIn": "_gkeonprem_238_QueryBareMetalAdminVersionConfigResponseIn",
        "QueryBareMetalAdminVersionConfigResponseOut": "_gkeonprem_239_QueryBareMetalAdminVersionConfigResponseOut",
        "VmwareVsphereTagIn": "_gkeonprem_240_VmwareVsphereTagIn",
        "VmwareVsphereTagOut": "_gkeonprem_241_VmwareVsphereTagOut",
        "BareMetalDrainedMachineIn": "_gkeonprem_242_BareMetalDrainedMachineIn",
        "BareMetalDrainedMachineOut": "_gkeonprem_243_BareMetalDrainedMachineOut",
        "VmwareAddressPoolIn": "_gkeonprem_244_VmwareAddressPoolIn",
        "VmwareAddressPoolOut": "_gkeonprem_245_VmwareAddressPoolOut",
        "BareMetalAdminDrainedMachineIn": "_gkeonprem_246_BareMetalAdminDrainedMachineIn",
        "BareMetalAdminDrainedMachineOut": "_gkeonprem_247_BareMetalAdminDrainedMachineOut",
        "BareMetalLvpConfigIn": "_gkeonprem_248_BareMetalLvpConfigIn",
        "BareMetalLvpConfigOut": "_gkeonprem_249_BareMetalLvpConfigOut",
        "VmwareAutoResizeConfigIn": "_gkeonprem_250_VmwareAutoResizeConfigIn",
        "VmwareAutoResizeConfigOut": "_gkeonprem_251_VmwareAutoResizeConfigOut",
        "VmwareAdminAddonNodeConfigIn": "_gkeonprem_252_VmwareAdminAddonNodeConfigIn",
        "VmwareAdminAddonNodeConfigOut": "_gkeonprem_253_VmwareAdminAddonNodeConfigOut",
        "BareMetalAdminMaintenanceStatusIn": "_gkeonprem_254_BareMetalAdminMaintenanceStatusIn",
        "BareMetalAdminMaintenanceStatusOut": "_gkeonprem_255_BareMetalAdminMaintenanceStatusOut",
        "VmwareDhcpIpConfigIn": "_gkeonprem_256_VmwareDhcpIpConfigIn",
        "VmwareDhcpIpConfigOut": "_gkeonprem_257_VmwareDhcpIpConfigOut",
        "BindingIn": "_gkeonprem_258_BindingIn",
        "BindingOut": "_gkeonprem_259_BindingOut",
        "VmwareStaticIpConfigIn": "_gkeonprem_260_VmwareStaticIpConfigIn",
        "VmwareStaticIpConfigOut": "_gkeonprem_261_VmwareStaticIpConfigOut",
        "BareMetalAdminLoadBalancerConfigIn": "_gkeonprem_262_BareMetalAdminLoadBalancerConfigIn",
        "BareMetalAdminLoadBalancerConfigOut": "_gkeonprem_263_BareMetalAdminLoadBalancerConfigOut",
        "BareMetalVipConfigIn": "_gkeonprem_264_BareMetalVipConfigIn",
        "BareMetalVipConfigOut": "_gkeonprem_265_BareMetalVipConfigOut",
        "NodeTaintIn": "_gkeonprem_266_NodeTaintIn",
        "NodeTaintOut": "_gkeonprem_267_NodeTaintOut",
        "VmwareStorageConfigIn": "_gkeonprem_268_VmwareStorageConfigIn",
        "VmwareStorageConfigOut": "_gkeonprem_269_VmwareStorageConfigOut",
        "VmwareAdminClusterIn": "_gkeonprem_270_VmwareAdminClusterIn",
        "VmwareAdminClusterOut": "_gkeonprem_271_VmwareAdminClusterOut",
        "VmwareVipConfigIn": "_gkeonprem_272_VmwareVipConfigIn",
        "VmwareVipConfigOut": "_gkeonprem_273_VmwareVipConfigOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["BareMetalAdminSecurityConfigIn"] = t.struct(
        {"authorization": t.proxy(renames["AuthorizationIn"]).optional()}
    ).named(renames["BareMetalAdminSecurityConfigIn"])
    types["BareMetalAdminSecurityConfigOut"] = t.struct(
        {
            "authorization": t.proxy(renames["AuthorizationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminSecurityConfigOut"])
    types["BareMetalAdminApiServerArgumentIn"] = t.struct(
        {"value": t.string(), "argument": t.string()}
    ).named(renames["BareMetalAdminApiServerArgumentIn"])
    types["BareMetalAdminApiServerArgumentOut"] = t.struct(
        {
            "value": t.string(),
            "argument": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminApiServerArgumentOut"])
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
            "unreachable": t.array(t.string()).optional(),
            "bareMetalAdminClusters": t.array(
                t.proxy(renames["BareMetalAdminClusterIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListBareMetalAdminClustersResponseIn"])
    types["ListBareMetalAdminClustersResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "bareMetalAdminClusters": t.array(
                t.proxy(renames["BareMetalAdminClusterOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBareMetalAdminClustersResponseOut"])
    types["ValidationCheckIn"] = t.struct({"option": t.string().optional()}).named(
        renames["ValidationCheckIn"]
    )
    types["ValidationCheckOut"] = t.struct(
        {
            "option": t.string().optional(),
            "status": t.proxy(renames["ValidationCheckStatusOut"]).optional(),
            "scenario": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidationCheckOut"])
    types["EnrollVmwareAdminClusterRequestIn"] = t.struct(
        {
            "vmwareAdminClusterId": t.string().optional(),
            "localName": t.string().optional(),
            "membership": t.string(),
        }
    ).named(renames["EnrollVmwareAdminClusterRequestIn"])
    types["EnrollVmwareAdminClusterRequestOut"] = t.struct(
        {
            "vmwareAdminClusterId": t.string().optional(),
            "localName": t.string().optional(),
            "membership": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnrollVmwareAdminClusterRequestOut"])
    types["BareMetalPortConfigIn"] = t.struct(
        {"controlPlaneLoadBalancerPort": t.integer().optional()}
    ).named(renames["BareMetalPortConfigIn"])
    types["BareMetalPortConfigOut"] = t.struct(
        {
            "controlPlaneLoadBalancerPort": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalPortConfigOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "type": t.string().optional(),
            "verb": t.string().optional(),
            "endTime": t.string().optional(),
            "statusMessage": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "target": t.string().optional(),
            "apiVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
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
    types["BareMetalAdminManualLbConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["BareMetalAdminManualLbConfigIn"])
    types["BareMetalAdminManualLbConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminManualLbConfigOut"])
    types["FleetIn"] = t.struct({"_": t.string().optional()}).named(renames["FleetIn"])
    types["FleetOut"] = t.struct(
        {
            "membership": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FleetOut"])
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
    types["ResourceConditionIn"] = t.struct(
        {
            "message": t.string().optional(),
            "type": t.string().optional(),
            "lastTransitionTime": t.string().optional(),
            "state": t.string().optional(),
            "reason": t.string().optional(),
        }
    ).named(renames["ResourceConditionIn"])
    types["ResourceConditionOut"] = t.struct(
        {
            "message": t.string().optional(),
            "type": t.string().optional(),
            "lastTransitionTime": t.string().optional(),
            "state": t.string().optional(),
            "reason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceConditionOut"])
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
    types["OperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
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
    types["VmwareControlPlaneV2ConfigIn"] = t.struct(
        {"controlPlaneIpBlock": t.proxy(renames["VmwareIpBlockIn"]).optional()}
    ).named(renames["VmwareControlPlaneV2ConfigIn"])
    types["VmwareControlPlaneV2ConfigOut"] = t.struct(
        {
            "controlPlaneIpBlock": t.proxy(renames["VmwareIpBlockOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareControlPlaneV2ConfigOut"])
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
    types["SetIamPolicyRequestIn"] = t.struct(
        {"policy": t.proxy(renames["PolicyIn"]).optional()}
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
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
    types["BareMetalAdminOsEnvironmentConfigIn"] = t.struct(
        {"packageRepoExcluded": t.boolean().optional()}
    ).named(renames["BareMetalAdminOsEnvironmentConfigIn"])
    types["BareMetalAdminOsEnvironmentConfigOut"] = t.struct(
        {
            "packageRepoExcluded": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminOsEnvironmentConfigOut"])
    types["ExprIn"] = t.struct(
        {
            "location": t.string().optional(),
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "location": t.string().optional(),
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["BareMetalAdminVipConfigIn"] = t.struct(
        {"controlPlaneVip": t.string().optional()}
    ).named(renames["BareMetalAdminVipConfigIn"])
    types["BareMetalAdminVipConfigOut"] = t.struct(
        {
            "controlPlaneVip": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminVipConfigOut"])
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
    types["VmwareNetworkConfigIn"] = t.struct(
        {
            "hostConfig": t.proxy(renames["VmwareHostConfigIn"]).optional(),
            "controlPlaneV2Config": t.proxy(
                renames["VmwareControlPlaneV2ConfigIn"]
            ).optional(),
            "podAddressCidrBlocks": t.array(t.string()),
            "serviceAddressCidrBlocks": t.array(t.string()),
            "staticIpConfig": t.proxy(renames["VmwareStaticIpConfigIn"]).optional(),
            "dhcpIpConfig": t.proxy(renames["VmwareDhcpIpConfigIn"]).optional(),
        }
    ).named(renames["VmwareNetworkConfigIn"])
    types["VmwareNetworkConfigOut"] = t.struct(
        {
            "hostConfig": t.proxy(renames["VmwareHostConfigOut"]).optional(),
            "vcenterNetwork": t.string().optional(),
            "controlPlaneV2Config": t.proxy(
                renames["VmwareControlPlaneV2ConfigOut"]
            ).optional(),
            "podAddressCidrBlocks": t.array(t.string()),
            "serviceAddressCidrBlocks": t.array(t.string()),
            "staticIpConfig": t.proxy(renames["VmwareStaticIpConfigOut"]).optional(),
            "dhcpIpConfig": t.proxy(renames["VmwareDhcpIpConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareNetworkConfigOut"])
    types["VmwareDataplaneV2ConfigIn"] = t.struct(
        {
            "dataplaneV2Enabled": t.boolean().optional(),
            "advancedNetworking": t.boolean().optional(),
            "windowsDataplaneV2Enabled": t.boolean().optional(),
        }
    ).named(renames["VmwareDataplaneV2ConfigIn"])
    types["VmwareDataplaneV2ConfigOut"] = t.struct(
        {
            "dataplaneV2Enabled": t.boolean().optional(),
            "advancedNetworking": t.boolean().optional(),
            "windowsDataplaneV2Enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareDataplaneV2ConfigOut"])
    types["PolicyIn"] = t.struct(
        {
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["BareMetalAdminControlPlaneNodePoolConfigIn"] = t.struct(
        {"nodePoolConfig": t.proxy(renames["BareMetalNodePoolConfigIn"]).optional()}
    ).named(renames["BareMetalAdminControlPlaneNodePoolConfigIn"])
    types["BareMetalAdminControlPlaneNodePoolConfigOut"] = t.struct(
        {
            "nodePoolConfig": t.proxy(renames["BareMetalNodePoolConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminControlPlaneNodePoolConfigOut"])
    types["LocationIn"] = t.struct(
        {
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["BareMetalKubeletConfigIn"] = t.struct(
        {
            "registryBurst": t.integer().optional(),
            "serializeImagePullsDisabled": t.boolean().optional(),
            "registryPullQps": t.integer().optional(),
        }
    ).named(renames["BareMetalKubeletConfigIn"])
    types["BareMetalKubeletConfigOut"] = t.struct(
        {
            "registryBurst": t.integer().optional(),
            "serializeImagePullsDisabled": t.boolean().optional(),
            "registryPullQps": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalKubeletConfigOut"])
    types["BareMetalVersionInfoIn"] = t.struct(
        {"hasDependencies": t.boolean().optional(), "version": t.string().optional()}
    ).named(renames["BareMetalVersionInfoIn"])
    types["BareMetalVersionInfoOut"] = t.struct(
        {
            "hasDependencies": t.boolean().optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalVersionInfoOut"])
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
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["VmwareControlPlaneVsphereConfigIn"] = t.struct(
        {"datastore": t.string().optional()}
    ).named(renames["VmwareControlPlaneVsphereConfigIn"])
    types["VmwareControlPlaneVsphereConfigOut"] = t.struct(
        {
            "datastore": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareControlPlaneVsphereConfigOut"])
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
    types["BareMetalAdminMaintenanceConfigIn"] = t.struct(
        {"maintenanceAddressCidrBlocks": t.array(t.string())}
    ).named(renames["BareMetalAdminMaintenanceConfigIn"])
    types["BareMetalAdminMaintenanceConfigOut"] = t.struct(
        {
            "maintenanceAddressCidrBlocks": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminMaintenanceConfigOut"])
    types["BareMetalControlPlaneNodePoolConfigIn"] = t.struct(
        {"nodePoolConfig": t.proxy(renames["BareMetalNodePoolConfigIn"])}
    ).named(renames["BareMetalControlPlaneNodePoolConfigIn"])
    types["BareMetalControlPlaneNodePoolConfigOut"] = t.struct(
        {
            "nodePoolConfig": t.proxy(renames["BareMetalNodePoolConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalControlPlaneNodePoolConfigOut"])
    types["BareMetalAdminWorkloadNodeConfigIn"] = t.struct(
        {"maxPodsPerNode": t.string().optional()}
    ).named(renames["BareMetalAdminWorkloadNodeConfigIn"])
    types["BareMetalAdminWorkloadNodeConfigOut"] = t.struct(
        {
            "maxPodsPerNode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminWorkloadNodeConfigOut"])
    types["VmwareVersionInfoIn"] = t.struct(
        {
            "isInstalled": t.boolean().optional(),
            "hasDependencies": t.boolean().optional(),
            "version": t.string().optional(),
        }
    ).named(renames["VmwareVersionInfoIn"])
    types["VmwareVersionInfoOut"] = t.struct(
        {
            "isInstalled": t.boolean().optional(),
            "hasDependencies": t.boolean().optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareVersionInfoOut"])
    types["VmwarePlatformConfigIn"] = t.struct(
        {"requiredPlatformVersion": t.string().optional()}
    ).named(renames["VmwarePlatformConfigIn"])
    types["VmwarePlatformConfigOut"] = t.struct(
        {
            "platformVersion": t.string().optional(),
            "bundles": t.array(t.proxy(renames["VmwareBundleConfigOut"])).optional(),
            "requiredPlatformVersion": t.string().optional(),
            "status": t.proxy(renames["ResourceStatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwarePlatformConfigOut"])
    types["VmwareNodeConfigIn"] = t.struct(
        {
            "replicas": t.string().optional(),
            "image": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "bootDiskSizeGb": t.string().optional(),
            "memoryMb": t.string().optional(),
            "cpus": t.string().optional(),
            "enableLoadBalancer": t.boolean().optional(),
            "imageType": t.string(),
            "taints": t.array(t.proxy(renames["NodeTaintIn"])).optional(),
        }
    ).named(renames["VmwareNodeConfigIn"])
    types["VmwareNodeConfigOut"] = t.struct(
        {
            "replicas": t.string().optional(),
            "image": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "bootDiskSizeGb": t.string().optional(),
            "memoryMb": t.string().optional(),
            "cpus": t.string().optional(),
            "vsphereConfig": t.proxy(renames["VmwareVsphereConfigOut"]).optional(),
            "enableLoadBalancer": t.boolean().optional(),
            "imageType": t.string(),
            "taints": t.array(t.proxy(renames["NodeTaintOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareNodeConfigOut"])
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
    types["VmwareClusterIn"] = t.struct(
        {
            "antiAffinityGroups": t.proxy(renames["VmwareAAGConfigIn"]).optional(),
            "loadBalancer": t.proxy(renames["VmwareLoadBalancerConfigIn"]).optional(),
            "vmTrackingEnabled": t.boolean().optional(),
            "storage": t.proxy(renames["VmwareStorageConfigIn"]).optional(),
            "name": t.string().optional(),
            "dataplaneV2": t.proxy(renames["VmwareDataplaneV2ConfigIn"]).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "autoRepairConfig": t.proxy(renames["VmwareAutoRepairConfigIn"]).optional(),
            "onPremVersion": t.string().optional(),
            "controlPlaneNode": t.proxy(
                renames["VmwareControlPlaneNodeConfigIn"]
            ).optional(),
            "description": t.string().optional(),
            "etag": t.string().optional(),
            "authorization": t.proxy(renames["AuthorizationIn"]).optional(),
            "adminClusterMembership": t.string(),
            "networkConfig": t.proxy(renames["VmwareNetworkConfigIn"]).optional(),
            "enableControlPlaneV2": t.boolean().optional(),
        }
    ).named(renames["VmwareClusterIn"])
    types["VmwareClusterOut"] = t.struct(
        {
            "antiAffinityGroups": t.proxy(renames["VmwareAAGConfigOut"]).optional(),
            "loadBalancer": t.proxy(renames["VmwareLoadBalancerConfigOut"]).optional(),
            "createTime": t.string().optional(),
            "vmTrackingEnabled": t.boolean().optional(),
            "deleteTime": t.string().optional(),
            "storage": t.proxy(renames["VmwareStorageConfigOut"]).optional(),
            "validationCheck": t.proxy(renames["ValidationCheckOut"]).optional(),
            "fleet": t.proxy(renames["FleetOut"]).optional(),
            "name": t.string().optional(),
            "dataplaneV2": t.proxy(renames["VmwareDataplaneV2ConfigOut"]).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "autoRepairConfig": t.proxy(
                renames["VmwareAutoRepairConfigOut"]
            ).optional(),
            "endpoint": t.string().optional(),
            "adminClusterName": t.string().optional(),
            "onPremVersion": t.string().optional(),
            "controlPlaneNode": t.proxy(
                renames["VmwareControlPlaneNodeConfigOut"]
            ).optional(),
            "description": t.string().optional(),
            "reconciling": t.boolean().optional(),
            "etag": t.string().optional(),
            "status": t.proxy(renames["ResourceStatusOut"]).optional(),
            "authorization": t.proxy(renames["AuthorizationOut"]).optional(),
            "adminClusterMembership": t.string(),
            "uid": t.string().optional(),
            "vcenter": t.proxy(renames["VmwareVCenterConfigOut"]).optional(),
            "state": t.string().optional(),
            "networkConfig": t.proxy(renames["VmwareNetworkConfigOut"]).optional(),
            "updateTime": t.string().optional(),
            "localName": t.string().optional(),
            "enableControlPlaneV2": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareClusterOut"])
    types["BareMetalClusterOperationsConfigIn"] = t.struct(
        {"enableApplicationLogs": t.boolean().optional()}
    ).named(renames["BareMetalClusterOperationsConfigIn"])
    types["BareMetalClusterOperationsConfigOut"] = t.struct(
        {
            "enableApplicationLogs": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalClusterOperationsConfigOut"])
    types["VmwareAAGConfigIn"] = t.struct(
        {"aagConfigDisabled": t.boolean().optional()}
    ).named(renames["VmwareAAGConfigIn"])
    types["VmwareAAGConfigOut"] = t.struct(
        {
            "aagConfigDisabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareAAGConfigOut"])
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
    types["VmwareAdminManualLbConfigIn"] = t.struct(
        {
            "konnectivityServerNodePort": t.integer().optional(),
            "addonsNodePort": t.integer().optional(),
            "ingressHttpNodePort": t.integer().optional(),
            "ingressHttpsNodePort": t.integer().optional(),
            "controlPlaneNodePort": t.integer().optional(),
        }
    ).named(renames["VmwareAdminManualLbConfigIn"])
    types["VmwareAdminManualLbConfigOut"] = t.struct(
        {
            "konnectivityServerNodePort": t.integer().optional(),
            "addonsNodePort": t.integer().optional(),
            "ingressHttpNodePort": t.integer().optional(),
            "ingressHttpsNodePort": t.integer().optional(),
            "controlPlaneNodePort": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareAdminManualLbConfigOut"])
    types["BareMetalNodeAccessConfigIn"] = t.struct(
        {"loginUser": t.string().optional()}
    ).named(renames["BareMetalNodeAccessConfigIn"])
    types["BareMetalNodeAccessConfigOut"] = t.struct(
        {
            "loginUser": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalNodeAccessConfigOut"])
    types["ListOperationsResponseIn"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["OperationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListOperationsResponseIn"])
    types["ListOperationsResponseOut"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["OperationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListOperationsResponseOut"])
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
    types["BareMetalNodePoolIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "nodePoolConfig": t.proxy(renames["BareMetalNodePoolConfigIn"]),
            "name": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["BareMetalNodePoolIn"])
    types["BareMetalNodePoolOut"] = t.struct(
        {
            "state": t.string().optional(),
            "updateTime": t.string().optional(),
            "displayName": t.string().optional(),
            "nodePoolConfig": t.proxy(renames["BareMetalNodePoolConfigOut"]),
            "name": t.string().optional(),
            "status": t.proxy(renames["ResourceStatusOut"]).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "etag": t.string().optional(),
            "reconciling": t.boolean().optional(),
            "uid": t.string().optional(),
            "deleteTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalNodePoolOut"])
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
    types["BareMetalMaintenanceConfigIn"] = t.struct(
        {"maintenanceAddressCidrBlocks": t.array(t.string())}
    ).named(renames["BareMetalMaintenanceConfigIn"])
    types["BareMetalMaintenanceConfigOut"] = t.struct(
        {
            "maintenanceAddressCidrBlocks": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalMaintenanceConfigOut"])
    types["BareMetalMultipleNetworkInterfacesConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["BareMetalMultipleNetworkInterfacesConfigIn"])
    types["BareMetalMultipleNetworkInterfacesConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalMultipleNetworkInterfacesConfigOut"])
    types["QueryVmwareVersionConfigResponseIn"] = t.struct(
        {"versions": t.array(t.proxy(renames["VmwareVersionInfoIn"])).optional()}
    ).named(renames["QueryVmwareVersionConfigResponseIn"])
    types["QueryVmwareVersionConfigResponseOut"] = t.struct(
        {
            "versions": t.array(t.proxy(renames["VmwareVersionInfoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryVmwareVersionConfigResponseOut"])
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
    types["BareMetalAdminNodeAccessConfigIn"] = t.struct(
        {"loginUser": t.string()}
    ).named(renames["BareMetalAdminNodeAccessConfigIn"])
    types["BareMetalAdminNodeAccessConfigOut"] = t.struct(
        {"loginUser": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["BareMetalAdminNodeAccessConfigOut"])
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
    types["BareMetalAdminPortConfigIn"] = t.struct(
        {"controlPlaneLoadBalancerPort": t.integer().optional()}
    ).named(renames["BareMetalAdminPortConfigIn"])
    types["BareMetalAdminPortConfigOut"] = t.struct(
        {
            "controlPlaneLoadBalancerPort": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminPortConfigOut"])
    types["BareMetalAdminClusterIn"] = t.struct(
        {
            "controlPlane": t.proxy(
                renames["BareMetalAdminControlPlaneConfigIn"]
            ).optional(),
            "securityConfig": t.proxy(
                renames["BareMetalAdminSecurityConfigIn"]
            ).optional(),
            "bareMetalVersion": t.string().optional(),
            "etag": t.string().optional(),
            "osEnvironmentConfig": t.proxy(
                renames["BareMetalAdminOsEnvironmentConfigIn"]
            ).optional(),
            "maintenanceConfig": t.proxy(
                renames["BareMetalAdminMaintenanceConfigIn"]
            ).optional(),
            "networkConfig": t.proxy(
                renames["BareMetalAdminNetworkConfigIn"]
            ).optional(),
            "proxy": t.proxy(renames["BareMetalAdminProxyConfigIn"]).optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "loadBalancer": t.proxy(
                renames["BareMetalAdminLoadBalancerConfigIn"]
            ).optional(),
            "nodeConfig": t.proxy(
                renames["BareMetalAdminWorkloadNodeConfigIn"]
            ).optional(),
            "nodeAccessConfig": t.proxy(
                renames["BareMetalAdminNodeAccessConfigIn"]
            ).optional(),
            "storage": t.proxy(renames["BareMetalAdminStorageConfigIn"]).optional(),
            "clusterOperations": t.proxy(
                renames["BareMetalAdminClusterOperationsConfigIn"]
            ).optional(),
        }
    ).named(renames["BareMetalAdminClusterIn"])
    types["BareMetalAdminClusterOut"] = t.struct(
        {
            "controlPlane": t.proxy(
                renames["BareMetalAdminControlPlaneConfigOut"]
            ).optional(),
            "securityConfig": t.proxy(
                renames["BareMetalAdminSecurityConfigOut"]
            ).optional(),
            "endpoint": t.string().optional(),
            "bareMetalVersion": t.string().optional(),
            "etag": t.string().optional(),
            "osEnvironmentConfig": t.proxy(
                renames["BareMetalAdminOsEnvironmentConfigOut"]
            ).optional(),
            "maintenanceConfig": t.proxy(
                renames["BareMetalAdminMaintenanceConfigOut"]
            ).optional(),
            "networkConfig": t.proxy(
                renames["BareMetalAdminNetworkConfigOut"]
            ).optional(),
            "state": t.string().optional(),
            "proxy": t.proxy(renames["BareMetalAdminProxyConfigOut"]).optional(),
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "status": t.proxy(renames["ResourceStatusOut"]).optional(),
            "maintenanceStatus": t.proxy(
                renames["BareMetalAdminMaintenanceStatusOut"]
            ).optional(),
            "name": t.string().optional(),
            "fleet": t.proxy(renames["FleetOut"]).optional(),
            "reconciling": t.boolean().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "loadBalancer": t.proxy(
                renames["BareMetalAdminLoadBalancerConfigOut"]
            ).optional(),
            "updateTime": t.string().optional(),
            "nodeConfig": t.proxy(
                renames["BareMetalAdminWorkloadNodeConfigOut"]
            ).optional(),
            "deleteTime": t.string().optional(),
            "nodeAccessConfig": t.proxy(
                renames["BareMetalAdminNodeAccessConfigOut"]
            ).optional(),
            "localName": t.string().optional(),
            "validationCheck": t.proxy(renames["ValidationCheckOut"]).optional(),
            "storage": t.proxy(renames["BareMetalAdminStorageConfigOut"]).optional(),
            "clusterOperations": t.proxy(
                renames["BareMetalAdminClusterOperationsConfigOut"]
            ).optional(),
            "uid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminClusterOut"])
    types["BareMetalOsEnvironmentConfigIn"] = t.struct(
        {"packageRepoExcluded": t.boolean().optional()}
    ).named(renames["BareMetalOsEnvironmentConfigIn"])
    types["BareMetalOsEnvironmentConfigOut"] = t.struct(
        {
            "packageRepoExcluded": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalOsEnvironmentConfigOut"])
    types["VmwareAdminNetworkConfigIn"] = t.struct(
        {
            "vcenterNetwork": t.string().optional(),
            "hostConfig": t.proxy(renames["VmwareHostConfigIn"]).optional(),
            "podAddressCidrBlocks": t.array(t.string()),
            "serviceAddressCidrBlocks": t.array(t.string()),
            "staticIpConfig": t.proxy(renames["VmwareStaticIpConfigIn"]).optional(),
            "dhcpIpConfig": t.proxy(renames["VmwareDhcpIpConfigIn"]).optional(),
        }
    ).named(renames["VmwareAdminNetworkConfigIn"])
    types["VmwareAdminNetworkConfigOut"] = t.struct(
        {
            "vcenterNetwork": t.string().optional(),
            "hostConfig": t.proxy(renames["VmwareHostConfigOut"]).optional(),
            "podAddressCidrBlocks": t.array(t.string()),
            "serviceAddressCidrBlocks": t.array(t.string()),
            "staticIpConfig": t.proxy(renames["VmwareStaticIpConfigOut"]).optional(),
            "dhcpIpConfig": t.proxy(renames["VmwareDhcpIpConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareAdminNetworkConfigOut"])
    types["VmwareManualLbConfigIn"] = t.struct(
        {
            "ingressHttpNodePort": t.integer().optional(),
            "controlPlaneNodePort": t.integer().optional(),
            "konnectivityServerNodePort": t.integer().optional(),
            "ingressHttpsNodePort": t.integer().optional(),
        }
    ).named(renames["VmwareManualLbConfigIn"])
    types["VmwareManualLbConfigOut"] = t.struct(
        {
            "ingressHttpNodePort": t.integer().optional(),
            "controlPlaneNodePort": t.integer().optional(),
            "konnectivityServerNodePort": t.integer().optional(),
            "ingressHttpsNodePort": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareManualLbConfigOut"])
    types["BareMetalNodePoolConfigIn"] = t.struct(
        {
            "taints": t.array(t.proxy(renames["NodeTaintIn"])).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "nodeConfigs": t.array(t.proxy(renames["BareMetalNodeConfigIn"])),
            "operatingSystem": t.string().optional(),
            "kubeletConfig": t.proxy(renames["BareMetalKubeletConfigIn"]).optional(),
        }
    ).named(renames["BareMetalNodePoolConfigIn"])
    types["BareMetalNodePoolConfigOut"] = t.struct(
        {
            "taints": t.array(t.proxy(renames["NodeTaintOut"])).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "nodeConfigs": t.array(t.proxy(renames["BareMetalNodeConfigOut"])),
            "operatingSystem": t.string().optional(),
            "kubeletConfig": t.proxy(renames["BareMetalKubeletConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalNodePoolConfigOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ClusterUserIn"] = t.struct({"username": t.string()}).named(
        renames["ClusterUserIn"]
    )
    types["ClusterUserOut"] = t.struct(
        {"username": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ClusterUserOut"])
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
    types["BareMetalManualLbConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["BareMetalManualLbConfigIn"])
    types["BareMetalManualLbConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalManualLbConfigOut"])
    types["EnrollVmwareClusterRequestIn"] = t.struct(
        {
            "localName": t.string().optional(),
            "validateOnly": t.boolean().optional(),
            "adminClusterMembership": t.string(),
            "vmwareClusterId": t.string().optional(),
        }
    ).named(renames["EnrollVmwareClusterRequestIn"])
    types["EnrollVmwareClusterRequestOut"] = t.struct(
        {
            "localName": t.string().optional(),
            "validateOnly": t.boolean().optional(),
            "adminClusterMembership": t.string(),
            "vmwareClusterId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnrollVmwareClusterRequestOut"])
    types["ValidationCheckResultIn"] = t.struct(
        {
            "description": t.string().optional(),
            "reason": t.string().optional(),
            "details": t.string().optional(),
            "state": t.string().optional(),
            "category": t.string().optional(),
        }
    ).named(renames["ValidationCheckResultIn"])
    types["ValidationCheckResultOut"] = t.struct(
        {
            "description": t.string().optional(),
            "reason": t.string().optional(),
            "details": t.string().optional(),
            "state": t.string().optional(),
            "category": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidationCheckResultOut"])
    types["VmwareAdminMetalLbConfigIn"] = t.struct({"_": t.string().optional()}).named(
        renames["VmwareAdminMetalLbConfigIn"]
    )
    types["VmwareAdminMetalLbConfigOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["VmwareAdminMetalLbConfigOut"])
    types["EnrollVmwareNodePoolRequestIn"] = t.struct(
        {"vmwareNodePoolId": t.string().optional()}
    ).named(renames["EnrollVmwareNodePoolRequestIn"])
    types["EnrollVmwareNodePoolRequestOut"] = t.struct(
        {
            "vmwareNodePoolId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnrollVmwareNodePoolRequestOut"])
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
    types["ValidationCheckStatusIn"] = t.struct(
        {"result": t.array(t.proxy(renames["ValidationCheckResultIn"])).optional()}
    ).named(renames["ValidationCheckStatusIn"])
    types["ValidationCheckStatusOut"] = t.struct(
        {
            "result": t.array(t.proxy(renames["ValidationCheckResultOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidationCheckStatusOut"])
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
    types["VmwareAdminVipConfigIn"] = t.struct(
        {"addonsVip": t.string().optional(), "controlPlaneVip": t.string().optional()}
    ).named(renames["VmwareAdminVipConfigIn"])
    types["VmwareAdminVipConfigOut"] = t.struct(
        {
            "addonsVip": t.string().optional(),
            "controlPlaneVip": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareAdminVipConfigOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["BareMetalNetworkConfigIn"] = t.struct(
        {
            "advancedNetworking": t.boolean().optional(),
            "islandModeCidr": t.proxy(
                renames["BareMetalIslandModeCidrConfigIn"]
            ).optional(),
            "multipleNetworkInterfacesConfig": t.proxy(
                renames["BareMetalMultipleNetworkInterfacesConfigIn"]
            ).optional(),
            "srIovConfig": t.proxy(renames["BareMetalSrIovConfigIn"]).optional(),
        }
    ).named(renames["BareMetalNetworkConfigIn"])
    types["BareMetalNetworkConfigOut"] = t.struct(
        {
            "advancedNetworking": t.boolean().optional(),
            "islandModeCidr": t.proxy(
                renames["BareMetalIslandModeCidrConfigOut"]
            ).optional(),
            "multipleNetworkInterfacesConfig": t.proxy(
                renames["BareMetalMultipleNetworkInterfacesConfigOut"]
            ).optional(),
            "srIovConfig": t.proxy(renames["BareMetalSrIovConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalNetworkConfigOut"])
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
    types["BareMetalSecurityConfigIn"] = t.struct(
        {"authorization": t.proxy(renames["AuthorizationIn"]).optional()}
    ).named(renames["BareMetalSecurityConfigIn"])
    types["BareMetalSecurityConfigOut"] = t.struct(
        {
            "authorization": t.proxy(renames["AuthorizationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalSecurityConfigOut"])
    types["BareMetalClusterIn"] = t.struct(
        {
            "loadBalancer": t.proxy(renames["BareMetalLoadBalancerConfigIn"]),
            "maintenanceConfig": t.proxy(
                renames["BareMetalMaintenanceConfigIn"]
            ).optional(),
            "nodeAccessConfig": t.proxy(
                renames["BareMetalNodeAccessConfigIn"]
            ).optional(),
            "adminClusterMembership": t.string(),
            "description": t.string().optional(),
            "bareMetalVersion": t.string(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "securityConfig": t.proxy(renames["BareMetalSecurityConfigIn"]).optional(),
            "clusterOperations": t.proxy(
                renames["BareMetalClusterOperationsConfigIn"]
            ).optional(),
            "storage": t.proxy(renames["BareMetalStorageConfigIn"]),
            "nodeConfig": t.proxy(renames["BareMetalWorkloadNodeConfigIn"]).optional(),
            "osEnvironmentConfig": t.proxy(
                renames["BareMetalOsEnvironmentConfigIn"]
            ).optional(),
            "proxy": t.proxy(renames["BareMetalProxyConfigIn"]).optional(),
            "controlPlane": t.proxy(renames["BareMetalControlPlaneConfigIn"]),
            "name": t.string().optional(),
            "networkConfig": t.proxy(renames["BareMetalNetworkConfigIn"]),
        }
    ).named(renames["BareMetalClusterIn"])
    types["BareMetalClusterOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "loadBalancer": t.proxy(renames["BareMetalLoadBalancerConfigOut"]),
            "maintenanceConfig": t.proxy(
                renames["BareMetalMaintenanceConfigOut"]
            ).optional(),
            "nodeAccessConfig": t.proxy(
                renames["BareMetalNodeAccessConfigOut"]
            ).optional(),
            "reconciling": t.boolean().optional(),
            "adminClusterMembership": t.string(),
            "description": t.string().optional(),
            "bareMetalVersion": t.string(),
            "localName": t.string().optional(),
            "deleteTime": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "etag": t.string().optional(),
            "securityConfig": t.proxy(renames["BareMetalSecurityConfigOut"]).optional(),
            "uid": t.string().optional(),
            "clusterOperations": t.proxy(
                renames["BareMetalClusterOperationsConfigOut"]
            ).optional(),
            "adminClusterName": t.string().optional(),
            "storage": t.proxy(renames["BareMetalStorageConfigOut"]),
            "nodeConfig": t.proxy(renames["BareMetalWorkloadNodeConfigOut"]).optional(),
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "osEnvironmentConfig": t.proxy(
                renames["BareMetalOsEnvironmentConfigOut"]
            ).optional(),
            "validationCheck": t.proxy(renames["ValidationCheckOut"]).optional(),
            "proxy": t.proxy(renames["BareMetalProxyConfigOut"]).optional(),
            "endpoint": t.string().optional(),
            "fleet": t.proxy(renames["FleetOut"]).optional(),
            "controlPlane": t.proxy(renames["BareMetalControlPlaneConfigOut"]),
            "maintenanceStatus": t.proxy(
                renames["BareMetalMaintenanceStatusOut"]
            ).optional(),
            "name": t.string().optional(),
            "networkConfig": t.proxy(renames["BareMetalNetworkConfigOut"]),
            "status": t.proxy(renames["ResourceStatusOut"]).optional(),
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
    types["VmwareF5BigIpConfigIn"] = t.struct(
        {
            "address": t.string().optional(),
            "partition": t.string().optional(),
            "snatPool": t.string().optional(),
        }
    ).named(renames["VmwareF5BigIpConfigIn"])
    types["VmwareF5BigIpConfigOut"] = t.struct(
        {
            "address": t.string().optional(),
            "partition": t.string().optional(),
            "snatPool": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareF5BigIpConfigOut"])
    types["VmwareHostConfigIn"] = t.struct(
        {
            "dnsServers": t.array(t.string()).optional(),
            "ntpServers": t.array(t.string()).optional(),
            "dnsSearchDomains": t.array(t.string()).optional(),
        }
    ).named(renames["VmwareHostConfigIn"])
    types["VmwareHostConfigOut"] = t.struct(
        {
            "dnsServers": t.array(t.string()).optional(),
            "ntpServers": t.array(t.string()).optional(),
            "dnsSearchDomains": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareHostConfigOut"])
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
    types["VmwareAdminLoadBalancerConfigIn"] = t.struct(
        {
            "vipConfig": t.proxy(renames["VmwareAdminVipConfigIn"]).optional(),
            "metalLbConfig": t.proxy(renames["VmwareAdminMetalLbConfigIn"]).optional(),
            "manualLbConfig": t.proxy(
                renames["VmwareAdminManualLbConfigIn"]
            ).optional(),
            "f5Config": t.proxy(renames["VmwareAdminF5BigIpConfigIn"]).optional(),
        }
    ).named(renames["VmwareAdminLoadBalancerConfigIn"])
    types["VmwareAdminLoadBalancerConfigOut"] = t.struct(
        {
            "vipConfig": t.proxy(renames["VmwareAdminVipConfigOut"]).optional(),
            "metalLbConfig": t.proxy(renames["VmwareAdminMetalLbConfigOut"]).optional(),
            "manualLbConfig": t.proxy(
                renames["VmwareAdminManualLbConfigOut"]
            ).optional(),
            "f5Config": t.proxy(renames["VmwareAdminF5BigIpConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareAdminLoadBalancerConfigOut"])
    types["BareMetalAdminClusterOperationsConfigIn"] = t.struct(
        {"enableApplicationLogs": t.boolean().optional()}
    ).named(renames["BareMetalAdminClusterOperationsConfigIn"])
    types["BareMetalAdminClusterOperationsConfigOut"] = t.struct(
        {
            "enableApplicationLogs": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminClusterOperationsConfigOut"])
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
    types["VmwareAutoRepairConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["VmwareAutoRepairConfigIn"])
    types["VmwareAutoRepairConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareAutoRepairConfigOut"])
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
    types["VmwareLoadBalancerConfigIn"] = t.struct(
        {
            "vipConfig": t.proxy(renames["VmwareVipConfigIn"]).optional(),
            "metalLbConfig": t.proxy(renames["VmwareMetalLbConfigIn"]).optional(),
            "manualLbConfig": t.proxy(renames["VmwareManualLbConfigIn"]).optional(),
            "f5Config": t.proxy(renames["VmwareF5BigIpConfigIn"]).optional(),
        }
    ).named(renames["VmwareLoadBalancerConfigIn"])
    types["VmwareLoadBalancerConfigOut"] = t.struct(
        {
            "vipConfig": t.proxy(renames["VmwareVipConfigOut"]).optional(),
            "metalLbConfig": t.proxy(renames["VmwareMetalLbConfigOut"]).optional(),
            "manualLbConfig": t.proxy(renames["VmwareManualLbConfigOut"]).optional(),
            "f5Config": t.proxy(renames["VmwareF5BigIpConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareLoadBalancerConfigOut"])
    types["BareMetalNodeConfigIn"] = t.struct(
        {
            "nodeIp": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["BareMetalNodeConfigIn"])
    types["BareMetalNodeConfigOut"] = t.struct(
        {
            "nodeIp": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalNodeConfigOut"])
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
    types["BareMetalLoadBalancerNodePoolConfigIn"] = t.struct(
        {"nodePoolConfig": t.proxy(renames["BareMetalNodePoolConfigIn"]).optional()}
    ).named(renames["BareMetalLoadBalancerNodePoolConfigIn"])
    types["BareMetalLoadBalancerNodePoolConfigOut"] = t.struct(
        {
            "nodePoolConfig": t.proxy(renames["BareMetalNodePoolConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalLoadBalancerNodePoolConfigOut"])
    types["VmwareMetalLbConfigIn"] = t.struct(
        {"addressPools": t.array(t.proxy(renames["VmwareAddressPoolIn"]))}
    ).named(renames["VmwareMetalLbConfigIn"])
    types["VmwareMetalLbConfigOut"] = t.struct(
        {
            "addressPools": t.array(t.proxy(renames["VmwareAddressPoolOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareMetalLbConfigOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["BareMetalBgpPeerConfigIn"] = t.struct(
        {
            "asn": t.string(),
            "ipAddress": t.string(),
            "controlPlaneNodes": t.array(t.string()).optional(),
        }
    ).named(renames["BareMetalBgpPeerConfigIn"])
    types["BareMetalBgpPeerConfigOut"] = t.struct(
        {
            "asn": t.string(),
            "ipAddress": t.string(),
            "controlPlaneNodes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalBgpPeerConfigOut"])
    types["BareMetalLoadBalancerConfigIn"] = t.struct(
        {
            "manualLbConfig": t.proxy(renames["BareMetalManualLbConfigIn"]).optional(),
            "portConfig": t.proxy(renames["BareMetalPortConfigIn"]).optional(),
            "bgpLbConfig": t.proxy(renames["BareMetalBgpLbConfigIn"]).optional(),
            "vipConfig": t.proxy(renames["BareMetalVipConfigIn"]).optional(),
            "metalLbConfig": t.proxy(renames["BareMetalMetalLbConfigIn"]).optional(),
        }
    ).named(renames["BareMetalLoadBalancerConfigIn"])
    types["BareMetalLoadBalancerConfigOut"] = t.struct(
        {
            "manualLbConfig": t.proxy(renames["BareMetalManualLbConfigOut"]).optional(),
            "portConfig": t.proxy(renames["BareMetalPortConfigOut"]).optional(),
            "bgpLbConfig": t.proxy(renames["BareMetalBgpLbConfigOut"]).optional(),
            "vipConfig": t.proxy(renames["BareMetalVipConfigOut"]).optional(),
            "metalLbConfig": t.proxy(renames["BareMetalMetalLbConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalLoadBalancerConfigOut"])
    types["BareMetalBgpLbConfigIn"] = t.struct(
        {
            "loadBalancerNodePoolConfig": t.proxy(
                renames["BareMetalLoadBalancerNodePoolConfigIn"]
            ).optional(),
            "asn": t.string(),
            "addressPools": t.array(
                t.proxy(renames["BareMetalLoadBalancerAddressPoolIn"])
            ),
            "bgpPeerConfigs": t.array(t.proxy(renames["BareMetalBgpPeerConfigIn"])),
        }
    ).named(renames["BareMetalBgpLbConfigIn"])
    types["BareMetalBgpLbConfigOut"] = t.struct(
        {
            "loadBalancerNodePoolConfig": t.proxy(
                renames["BareMetalLoadBalancerNodePoolConfigOut"]
            ).optional(),
            "asn": t.string(),
            "addressPools": t.array(
                t.proxy(renames["BareMetalLoadBalancerAddressPoolOut"])
            ),
            "bgpPeerConfigs": t.array(t.proxy(renames["BareMetalBgpPeerConfigOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalBgpLbConfigOut"])
    types["VmwareControlPlaneNodeConfigIn"] = t.struct(
        {
            "replicas": t.string().optional(),
            "cpus": t.string().optional(),
            "autoResizeConfig": t.proxy(renames["VmwareAutoResizeConfigIn"]).optional(),
            "memory": t.string().optional(),
        }
    ).named(renames["VmwareControlPlaneNodeConfigIn"])
    types["VmwareControlPlaneNodeConfigOut"] = t.struct(
        {
            "replicas": t.string().optional(),
            "cpus": t.string().optional(),
            "autoResizeConfig": t.proxy(
                renames["VmwareAutoResizeConfigOut"]
            ).optional(),
            "vsphereConfig": t.proxy(
                renames["VmwareControlPlaneVsphereConfigOut"]
            ).optional(),
            "memory": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareControlPlaneNodeConfigOut"])
    types["BareMetalSrIovConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["BareMetalSrIovConfigIn"])
    types["BareMetalSrIovConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalSrIovConfigOut"])
    types["BareMetalLoadBalancerAddressPoolIn"] = t.struct(
        {
            "addresses": t.array(t.string()),
            "avoidBuggyIps": t.boolean().optional(),
            "manualAssign": t.boolean().optional(),
            "pool": t.string(),
        }
    ).named(renames["BareMetalLoadBalancerAddressPoolIn"])
    types["BareMetalLoadBalancerAddressPoolOut"] = t.struct(
        {
            "addresses": t.array(t.string()),
            "avoidBuggyIps": t.boolean().optional(),
            "manualAssign": t.boolean().optional(),
            "pool": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalLoadBalancerAddressPoolOut"])
    types["VmwareVCenterConfigIn"] = t.struct(
        {
            "datastore": t.string().optional(),
            "cluster": t.string().optional(),
            "address": t.string().optional(),
            "caCertData": t.string().optional(),
            "datacenter": t.string().optional(),
            "resourcePool": t.string().optional(),
            "folder": t.string().optional(),
        }
    ).named(renames["VmwareVCenterConfigIn"])
    types["VmwareVCenterConfigOut"] = t.struct(
        {
            "datastore": t.string().optional(),
            "cluster": t.string().optional(),
            "address": t.string().optional(),
            "caCertData": t.string().optional(),
            "datacenter": t.string().optional(),
            "resourcePool": t.string().optional(),
            "folder": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareVCenterConfigOut"])
    types["EnrollBareMetalAdminClusterRequestIn"] = t.struct(
        {
            "bareMetalAdminClusterId": t.string().optional(),
            "membership": t.string(),
            "localName": t.string().optional(),
        }
    ).named(renames["EnrollBareMetalAdminClusterRequestIn"])
    types["EnrollBareMetalAdminClusterRequestOut"] = t.struct(
        {
            "bareMetalAdminClusterId": t.string().optional(),
            "membership": t.string(),
            "localName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnrollBareMetalAdminClusterRequestOut"])
    types["VmwareNodePoolIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "nodePoolAutoscaling": t.proxy(
                renames["VmwareNodePoolAutoscalingConfigIn"]
            ).optional(),
            "config": t.proxy(renames["VmwareNodeConfigIn"]),
            "onPremVersion": t.string().optional(),
        }
    ).named(renames["VmwareNodePoolIn"])
    types["VmwareNodePoolOut"] = t.struct(
        {
            "uid": t.string().optional(),
            "etag": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "displayName": t.string().optional(),
            "reconciling": t.boolean().optional(),
            "deleteTime": t.string().optional(),
            "nodePoolAutoscaling": t.proxy(
                renames["VmwareNodePoolAutoscalingConfigOut"]
            ).optional(),
            "config": t.proxy(renames["VmwareNodeConfigOut"]),
            "onPremVersion": t.string().optional(),
            "status": t.proxy(renames["ResourceStatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareNodePoolOut"])
    types["VmwareAdminVCenterConfigIn"] = t.struct(
        {
            "caCertData": t.string().optional(),
            "resourcePool": t.string().optional(),
            "datastore": t.string().optional(),
            "dataDisk": t.string().optional(),
            "datacenter": t.string().optional(),
            "cluster": t.string().optional(),
            "address": t.string().optional(),
            "folder": t.string().optional(),
        }
    ).named(renames["VmwareAdminVCenterConfigIn"])
    types["VmwareAdminVCenterConfigOut"] = t.struct(
        {
            "caCertData": t.string().optional(),
            "resourcePool": t.string().optional(),
            "datastore": t.string().optional(),
            "dataDisk": t.string().optional(),
            "datacenter": t.string().optional(),
            "cluster": t.string().optional(),
            "address": t.string().optional(),
            "folder": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareAdminVCenterConfigOut"])
    types["QueryBareMetalAdminVersionConfigResponseIn"] = t.struct(
        {"versions": t.array(t.proxy(renames["BareMetalVersionInfoIn"])).optional()}
    ).named(renames["QueryBareMetalAdminVersionConfigResponseIn"])
    types["QueryBareMetalAdminVersionConfigResponseOut"] = t.struct(
        {
            "versions": t.array(t.proxy(renames["BareMetalVersionInfoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryBareMetalAdminVersionConfigResponseOut"])
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
    types["BareMetalDrainedMachineIn"] = t.struct(
        {"nodeIp": t.string().optional()}
    ).named(renames["BareMetalDrainedMachineIn"])
    types["BareMetalDrainedMachineOut"] = t.struct(
        {
            "nodeIp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalDrainedMachineOut"])
    types["VmwareAddressPoolIn"] = t.struct(
        {
            "avoidBuggyIps": t.boolean().optional(),
            "manualAssign": t.boolean().optional(),
            "pool": t.string(),
            "addresses": t.array(t.string()),
        }
    ).named(renames["VmwareAddressPoolIn"])
    types["VmwareAddressPoolOut"] = t.struct(
        {
            "avoidBuggyIps": t.boolean().optional(),
            "manualAssign": t.boolean().optional(),
            "pool": t.string(),
            "addresses": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareAddressPoolOut"])
    types["BareMetalAdminDrainedMachineIn"] = t.struct(
        {"nodeIp": t.string().optional()}
    ).named(renames["BareMetalAdminDrainedMachineIn"])
    types["BareMetalAdminDrainedMachineOut"] = t.struct(
        {
            "nodeIp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminDrainedMachineOut"])
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
    types["VmwareAutoResizeConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["VmwareAutoResizeConfigIn"])
    types["VmwareAutoResizeConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareAutoResizeConfigOut"])
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
    types["VmwareDhcpIpConfigIn"] = t.struct({"enabled": t.boolean().optional()}).named(
        renames["VmwareDhcpIpConfigIn"]
    )
    types["VmwareDhcpIpConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareDhcpIpConfigOut"])
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
    types["VmwareStaticIpConfigIn"] = t.struct(
        {"ipBlocks": t.array(t.proxy(renames["VmwareIpBlockIn"])).optional()}
    ).named(renames["VmwareStaticIpConfigIn"])
    types["VmwareStaticIpConfigOut"] = t.struct(
        {
            "ipBlocks": t.array(t.proxy(renames["VmwareIpBlockOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareStaticIpConfigOut"])
    types["BareMetalAdminLoadBalancerConfigIn"] = t.struct(
        {
            "vipConfig": t.proxy(renames["BareMetalAdminVipConfigIn"]).optional(),
            "portConfig": t.proxy(renames["BareMetalAdminPortConfigIn"]).optional(),
            "manualLbConfig": t.proxy(
                renames["BareMetalAdminManualLbConfigIn"]
            ).optional(),
        }
    ).named(renames["BareMetalAdminLoadBalancerConfigIn"])
    types["BareMetalAdminLoadBalancerConfigOut"] = t.struct(
        {
            "vipConfig": t.proxy(renames["BareMetalAdminVipConfigOut"]).optional(),
            "portConfig": t.proxy(renames["BareMetalAdminPortConfigOut"]).optional(),
            "manualLbConfig": t.proxy(
                renames["BareMetalAdminManualLbConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminLoadBalancerConfigOut"])
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
    types["NodeTaintIn"] = t.struct(
        {
            "key": t.string().optional(),
            "value": t.string().optional(),
            "effect": t.string().optional(),
        }
    ).named(renames["NodeTaintIn"])
    types["NodeTaintOut"] = t.struct(
        {
            "key": t.string().optional(),
            "value": t.string().optional(),
            "effect": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeTaintOut"])
    types["VmwareStorageConfigIn"] = t.struct(
        {"vsphereCsiDisabled": t.boolean().optional()}
    ).named(renames["VmwareStorageConfigIn"])
    types["VmwareStorageConfigOut"] = t.struct(
        {
            "vsphereCsiDisabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareStorageConfigOut"])
    types["VmwareAdminClusterIn"] = t.struct(
        {
            "bootstrapClusterMembership": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "autoRepairConfig": t.proxy(renames["VmwareAutoRepairConfigIn"]).optional(),
            "imageType": t.string().optional(),
            "vcenter": t.proxy(renames["VmwareAdminVCenterConfigIn"]).optional(),
            "loadBalancer": t.proxy(
                renames["VmwareAdminLoadBalancerConfigIn"]
            ).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "etag": t.string().optional(),
            "onPremVersion": t.string().optional(),
            "addonNode": t.proxy(renames["VmwareAdminAddonNodeConfigIn"]).optional(),
            "platformConfig": t.proxy(renames["VmwarePlatformConfigIn"]).optional(),
            "controlPlaneNode": t.proxy(
                renames["VmwareAdminControlPlaneNodeConfigIn"]
            ).optional(),
            "antiAffinityGroups": t.proxy(renames["VmwareAAGConfigIn"]).optional(),
            "networkConfig": t.proxy(renames["VmwareAdminNetworkConfigIn"]).optional(),
        }
    ).named(renames["VmwareAdminClusterIn"])
    types["VmwareAdminClusterOut"] = t.struct(
        {
            "status": t.proxy(renames["ResourceStatusOut"]).optional(),
            "bootstrapClusterMembership": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "state": t.string().optional(),
            "autoRepairConfig": t.proxy(
                renames["VmwareAutoRepairConfigOut"]
            ).optional(),
            "imageType": t.string().optional(),
            "vcenter": t.proxy(renames["VmwareAdminVCenterConfigOut"]).optional(),
            "fleet": t.proxy(renames["FleetOut"]).optional(),
            "loadBalancer": t.proxy(
                renames["VmwareAdminLoadBalancerConfigOut"]
            ).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "uid": t.string().optional(),
            "createTime": t.string().optional(),
            "etag": t.string().optional(),
            "updateTime": t.string().optional(),
            "onPremVersion": t.string().optional(),
            "endpoint": t.string().optional(),
            "reconciling": t.boolean().optional(),
            "addonNode": t.proxy(renames["VmwareAdminAddonNodeConfigOut"]).optional(),
            "platformConfig": t.proxy(renames["VmwarePlatformConfigOut"]).optional(),
            "controlPlaneNode": t.proxy(
                renames["VmwareAdminControlPlaneNodeConfigOut"]
            ).optional(),
            "localName": t.string().optional(),
            "antiAffinityGroups": t.proxy(renames["VmwareAAGConfigOut"]).optional(),
            "networkConfig": t.proxy(renames["VmwareAdminNetworkConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareAdminClusterOut"])
    types["VmwareVipConfigIn"] = t.struct(
        {"ingressVip": t.string().optional(), "controlPlaneVip": t.string().optional()}
    ).named(renames["VmwareVipConfigIn"])
    types["VmwareVipConfigOut"] = t.struct(
        {
            "ingressVip": t.string().optional(),
            "controlPlaneVip": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareVipConfigOut"])

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
    functions["projectsLocationsVmwareAdminClustersUnenroll"] = gkeonprem.post(
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
    functions["projectsLocationsVmwareAdminClustersGetIamPolicy"] = gkeonprem.post(
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
    functions["projectsLocationsVmwareAdminClustersEnroll"] = gkeonprem.post(
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
    functions["projectsLocationsVmwareAdminClustersPatch"] = gkeonprem.post(
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
    functions["projectsLocationsVmwareAdminClustersGet"] = gkeonprem.post(
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
    functions["projectsLocationsVmwareAdminClustersList"] = gkeonprem.post(
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
    functions[
        "projectsLocationsVmwareAdminClustersTestIamPermissions"
    ] = gkeonprem.post(
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
    functions["projectsLocationsVmwareAdminClustersSetIamPolicy"] = gkeonprem.post(
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
    functions["projectsLocationsBareMetalClustersSetIamPolicy"] = gkeonprem.post(
        "v1/{parent}/bareMetalClusters:queryVersionConfig",
        t.struct(
            {
                "createConfig.adminClusterName": t.string().optional(),
                "upgradeConfig.clusterName": t.string().optional(),
                "parent": t.string(),
                "createConfig.adminClusterMembership": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryBareMetalVersionConfigResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalClustersPatch"] = gkeonprem.post(
        "v1/{parent}/bareMetalClusters:queryVersionConfig",
        t.struct(
            {
                "createConfig.adminClusterName": t.string().optional(),
                "upgradeConfig.clusterName": t.string().optional(),
                "parent": t.string(),
                "createConfig.adminClusterMembership": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryBareMetalVersionConfigResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalClustersDelete"] = gkeonprem.post(
        "v1/{parent}/bareMetalClusters:queryVersionConfig",
        t.struct(
            {
                "createConfig.adminClusterName": t.string().optional(),
                "upgradeConfig.clusterName": t.string().optional(),
                "parent": t.string(),
                "createConfig.adminClusterMembership": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryBareMetalVersionConfigResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalClustersList"] = gkeonprem.post(
        "v1/{parent}/bareMetalClusters:queryVersionConfig",
        t.struct(
            {
                "createConfig.adminClusterName": t.string().optional(),
                "upgradeConfig.clusterName": t.string().optional(),
                "parent": t.string(),
                "createConfig.adminClusterMembership": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryBareMetalVersionConfigResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalClustersGet"] = gkeonprem.post(
        "v1/{parent}/bareMetalClusters:queryVersionConfig",
        t.struct(
            {
                "createConfig.adminClusterName": t.string().optional(),
                "upgradeConfig.clusterName": t.string().optional(),
                "parent": t.string(),
                "createConfig.adminClusterMembership": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryBareMetalVersionConfigResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalClustersEnroll"] = gkeonprem.post(
        "v1/{parent}/bareMetalClusters:queryVersionConfig",
        t.struct(
            {
                "createConfig.adminClusterName": t.string().optional(),
                "upgradeConfig.clusterName": t.string().optional(),
                "parent": t.string(),
                "createConfig.adminClusterMembership": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryBareMetalVersionConfigResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalClustersGetIamPolicy"] = gkeonprem.post(
        "v1/{parent}/bareMetalClusters:queryVersionConfig",
        t.struct(
            {
                "createConfig.adminClusterName": t.string().optional(),
                "upgradeConfig.clusterName": t.string().optional(),
                "parent": t.string(),
                "createConfig.adminClusterMembership": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryBareMetalVersionConfigResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalClustersTestIamPermissions"] = gkeonprem.post(
        "v1/{parent}/bareMetalClusters:queryVersionConfig",
        t.struct(
            {
                "createConfig.adminClusterName": t.string().optional(),
                "upgradeConfig.clusterName": t.string().optional(),
                "parent": t.string(),
                "createConfig.adminClusterMembership": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryBareMetalVersionConfigResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalClustersCreate"] = gkeonprem.post(
        "v1/{parent}/bareMetalClusters:queryVersionConfig",
        t.struct(
            {
                "createConfig.adminClusterName": t.string().optional(),
                "upgradeConfig.clusterName": t.string().optional(),
                "parent": t.string(),
                "createConfig.adminClusterMembership": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryBareMetalVersionConfigResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalClustersUnenroll"] = gkeonprem.post(
        "v1/{parent}/bareMetalClusters:queryVersionConfig",
        t.struct(
            {
                "createConfig.adminClusterName": t.string().optional(),
                "upgradeConfig.clusterName": t.string().optional(),
                "parent": t.string(),
                "createConfig.adminClusterMembership": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryBareMetalVersionConfigResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalClustersQueryVersionConfig"] = gkeonprem.post(
        "v1/{parent}/bareMetalClusters:queryVersionConfig",
        t.struct(
            {
                "createConfig.adminClusterName": t.string().optional(),
                "upgradeConfig.clusterName": t.string().optional(),
                "parent": t.string(),
                "createConfig.adminClusterMembership": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryBareMetalVersionConfigResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsBareMetalClustersBareMetalNodePoolsDelete"
    ] = gkeonprem.post(
        "v1/{parent}/bareMetalNodePools:enroll",
        t.struct(
            {
                "parent": t.string(),
                "validateOnly": t.boolean().optional(),
                "bareMetalNodePoolId": t.string().optional(),
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
        "v1/{parent}/bareMetalNodePools:enroll",
        t.struct(
            {
                "parent": t.string(),
                "validateOnly": t.boolean().optional(),
                "bareMetalNodePoolId": t.string().optional(),
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
        "v1/{parent}/bareMetalNodePools:enroll",
        t.struct(
            {
                "parent": t.string(),
                "validateOnly": t.boolean().optional(),
                "bareMetalNodePoolId": t.string().optional(),
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
        "v1/{parent}/bareMetalNodePools:enroll",
        t.struct(
            {
                "parent": t.string(),
                "validateOnly": t.boolean().optional(),
                "bareMetalNodePoolId": t.string().optional(),
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
        "v1/{parent}/bareMetalNodePools:enroll",
        t.struct(
            {
                "parent": t.string(),
                "validateOnly": t.boolean().optional(),
                "bareMetalNodePoolId": t.string().optional(),
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
        "v1/{parent}/bareMetalNodePools:enroll",
        t.struct(
            {
                "parent": t.string(),
                "validateOnly": t.boolean().optional(),
                "bareMetalNodePoolId": t.string().optional(),
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
        "v1/{parent}/bareMetalNodePools:enroll",
        t.struct(
            {
                "parent": t.string(),
                "validateOnly": t.boolean().optional(),
                "bareMetalNodePoolId": t.string().optional(),
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
        "v1/{parent}/bareMetalNodePools:enroll",
        t.struct(
            {
                "parent": t.string(),
                "validateOnly": t.boolean().optional(),
                "bareMetalNodePoolId": t.string().optional(),
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
        "v1/{parent}/bareMetalNodePools:enroll",
        t.struct(
            {
                "parent": t.string(),
                "validateOnly": t.boolean().optional(),
                "bareMetalNodePoolId": t.string().optional(),
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
        "v1/{parent}/bareMetalNodePools:enroll",
        t.struct(
            {
                "parent": t.string(),
                "validateOnly": t.boolean().optional(),
                "bareMetalNodePoolId": t.string().optional(),
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
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
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
    functions["projectsLocationsOperationsDelete"] = gkeonprem.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
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
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
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
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalAdminClustersGet"] = gkeonprem.post(
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
    functions["projectsLocationsBareMetalAdminClustersCreate"] = gkeonprem.post(
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
    functions[
        "projectsLocationsBareMetalAdminClustersTestIamPermissions"
    ] = gkeonprem.post(
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
    functions["projectsLocationsBareMetalAdminClustersGetIamPolicy"] = gkeonprem.post(
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
    functions[
        "projectsLocationsBareMetalAdminClustersQueryVersionConfig"
    ] = gkeonprem.post(
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
    functions["projectsLocationsBareMetalAdminClustersPatch"] = gkeonprem.post(
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
    functions["projectsLocationsBareMetalAdminClustersEnroll"] = gkeonprem.post(
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
    functions["projectsLocationsBareMetalAdminClustersList"] = gkeonprem.post(
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
    functions["projectsLocationsBareMetalAdminClustersUnenroll"] = gkeonprem.post(
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
    functions["projectsLocationsBareMetalAdminClustersSetIamPolicy"] = gkeonprem.post(
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
    functions["projectsLocationsVmwareClustersGetIamPolicy"] = gkeonprem.post(
        "v1/{parent}/vmwareClusters",
        t.struct(
            {
                "vmwareClusterId": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "parent": t.string(),
                "antiAffinityGroups": t.proxy(renames["VmwareAAGConfigIn"]).optional(),
                "loadBalancer": t.proxy(
                    renames["VmwareLoadBalancerConfigIn"]
                ).optional(),
                "vmTrackingEnabled": t.boolean().optional(),
                "storage": t.proxy(renames["VmwareStorageConfigIn"]).optional(),
                "name": t.string().optional(),
                "dataplaneV2": t.proxy(renames["VmwareDataplaneV2ConfigIn"]).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "autoRepairConfig": t.proxy(
                    renames["VmwareAutoRepairConfigIn"]
                ).optional(),
                "onPremVersion": t.string().optional(),
                "controlPlaneNode": t.proxy(
                    renames["VmwareControlPlaneNodeConfigIn"]
                ).optional(),
                "description": t.string().optional(),
                "etag": t.string().optional(),
                "authorization": t.proxy(renames["AuthorizationIn"]).optional(),
                "adminClusterMembership": t.string(),
                "networkConfig": t.proxy(renames["VmwareNetworkConfigIn"]).optional(),
                "enableControlPlaneV2": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersQueryVersionConfig"] = gkeonprem.post(
        "v1/{parent}/vmwareClusters",
        t.struct(
            {
                "vmwareClusterId": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "parent": t.string(),
                "antiAffinityGroups": t.proxy(renames["VmwareAAGConfigIn"]).optional(),
                "loadBalancer": t.proxy(
                    renames["VmwareLoadBalancerConfigIn"]
                ).optional(),
                "vmTrackingEnabled": t.boolean().optional(),
                "storage": t.proxy(renames["VmwareStorageConfigIn"]).optional(),
                "name": t.string().optional(),
                "dataplaneV2": t.proxy(renames["VmwareDataplaneV2ConfigIn"]).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "autoRepairConfig": t.proxy(
                    renames["VmwareAutoRepairConfigIn"]
                ).optional(),
                "onPremVersion": t.string().optional(),
                "controlPlaneNode": t.proxy(
                    renames["VmwareControlPlaneNodeConfigIn"]
                ).optional(),
                "description": t.string().optional(),
                "etag": t.string().optional(),
                "authorization": t.proxy(renames["AuthorizationIn"]).optional(),
                "adminClusterMembership": t.string(),
                "networkConfig": t.proxy(renames["VmwareNetworkConfigIn"]).optional(),
                "enableControlPlaneV2": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersDelete"] = gkeonprem.post(
        "v1/{parent}/vmwareClusters",
        t.struct(
            {
                "vmwareClusterId": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "parent": t.string(),
                "antiAffinityGroups": t.proxy(renames["VmwareAAGConfigIn"]).optional(),
                "loadBalancer": t.proxy(
                    renames["VmwareLoadBalancerConfigIn"]
                ).optional(),
                "vmTrackingEnabled": t.boolean().optional(),
                "storage": t.proxy(renames["VmwareStorageConfigIn"]).optional(),
                "name": t.string().optional(),
                "dataplaneV2": t.proxy(renames["VmwareDataplaneV2ConfigIn"]).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "autoRepairConfig": t.proxy(
                    renames["VmwareAutoRepairConfigIn"]
                ).optional(),
                "onPremVersion": t.string().optional(),
                "controlPlaneNode": t.proxy(
                    renames["VmwareControlPlaneNodeConfigIn"]
                ).optional(),
                "description": t.string().optional(),
                "etag": t.string().optional(),
                "authorization": t.proxy(renames["AuthorizationIn"]).optional(),
                "adminClusterMembership": t.string(),
                "networkConfig": t.proxy(renames["VmwareNetworkConfigIn"]).optional(),
                "enableControlPlaneV2": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersPatch"] = gkeonprem.post(
        "v1/{parent}/vmwareClusters",
        t.struct(
            {
                "vmwareClusterId": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "parent": t.string(),
                "antiAffinityGroups": t.proxy(renames["VmwareAAGConfigIn"]).optional(),
                "loadBalancer": t.proxy(
                    renames["VmwareLoadBalancerConfigIn"]
                ).optional(),
                "vmTrackingEnabled": t.boolean().optional(),
                "storage": t.proxy(renames["VmwareStorageConfigIn"]).optional(),
                "name": t.string().optional(),
                "dataplaneV2": t.proxy(renames["VmwareDataplaneV2ConfigIn"]).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "autoRepairConfig": t.proxy(
                    renames["VmwareAutoRepairConfigIn"]
                ).optional(),
                "onPremVersion": t.string().optional(),
                "controlPlaneNode": t.proxy(
                    renames["VmwareControlPlaneNodeConfigIn"]
                ).optional(),
                "description": t.string().optional(),
                "etag": t.string().optional(),
                "authorization": t.proxy(renames["AuthorizationIn"]).optional(),
                "adminClusterMembership": t.string(),
                "networkConfig": t.proxy(renames["VmwareNetworkConfigIn"]).optional(),
                "enableControlPlaneV2": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersGet"] = gkeonprem.post(
        "v1/{parent}/vmwareClusters",
        t.struct(
            {
                "vmwareClusterId": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "parent": t.string(),
                "antiAffinityGroups": t.proxy(renames["VmwareAAGConfigIn"]).optional(),
                "loadBalancer": t.proxy(
                    renames["VmwareLoadBalancerConfigIn"]
                ).optional(),
                "vmTrackingEnabled": t.boolean().optional(),
                "storage": t.proxy(renames["VmwareStorageConfigIn"]).optional(),
                "name": t.string().optional(),
                "dataplaneV2": t.proxy(renames["VmwareDataplaneV2ConfigIn"]).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "autoRepairConfig": t.proxy(
                    renames["VmwareAutoRepairConfigIn"]
                ).optional(),
                "onPremVersion": t.string().optional(),
                "controlPlaneNode": t.proxy(
                    renames["VmwareControlPlaneNodeConfigIn"]
                ).optional(),
                "description": t.string().optional(),
                "etag": t.string().optional(),
                "authorization": t.proxy(renames["AuthorizationIn"]).optional(),
                "adminClusterMembership": t.string(),
                "networkConfig": t.proxy(renames["VmwareNetworkConfigIn"]).optional(),
                "enableControlPlaneV2": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersList"] = gkeonprem.post(
        "v1/{parent}/vmwareClusters",
        t.struct(
            {
                "vmwareClusterId": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "parent": t.string(),
                "antiAffinityGroups": t.proxy(renames["VmwareAAGConfigIn"]).optional(),
                "loadBalancer": t.proxy(
                    renames["VmwareLoadBalancerConfigIn"]
                ).optional(),
                "vmTrackingEnabled": t.boolean().optional(),
                "storage": t.proxy(renames["VmwareStorageConfigIn"]).optional(),
                "name": t.string().optional(),
                "dataplaneV2": t.proxy(renames["VmwareDataplaneV2ConfigIn"]).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "autoRepairConfig": t.proxy(
                    renames["VmwareAutoRepairConfigIn"]
                ).optional(),
                "onPremVersion": t.string().optional(),
                "controlPlaneNode": t.proxy(
                    renames["VmwareControlPlaneNodeConfigIn"]
                ).optional(),
                "description": t.string().optional(),
                "etag": t.string().optional(),
                "authorization": t.proxy(renames["AuthorizationIn"]).optional(),
                "adminClusterMembership": t.string(),
                "networkConfig": t.proxy(renames["VmwareNetworkConfigIn"]).optional(),
                "enableControlPlaneV2": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersTestIamPermissions"] = gkeonprem.post(
        "v1/{parent}/vmwareClusters",
        t.struct(
            {
                "vmwareClusterId": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "parent": t.string(),
                "antiAffinityGroups": t.proxy(renames["VmwareAAGConfigIn"]).optional(),
                "loadBalancer": t.proxy(
                    renames["VmwareLoadBalancerConfigIn"]
                ).optional(),
                "vmTrackingEnabled": t.boolean().optional(),
                "storage": t.proxy(renames["VmwareStorageConfigIn"]).optional(),
                "name": t.string().optional(),
                "dataplaneV2": t.proxy(renames["VmwareDataplaneV2ConfigIn"]).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "autoRepairConfig": t.proxy(
                    renames["VmwareAutoRepairConfigIn"]
                ).optional(),
                "onPremVersion": t.string().optional(),
                "controlPlaneNode": t.proxy(
                    renames["VmwareControlPlaneNodeConfigIn"]
                ).optional(),
                "description": t.string().optional(),
                "etag": t.string().optional(),
                "authorization": t.proxy(renames["AuthorizationIn"]).optional(),
                "adminClusterMembership": t.string(),
                "networkConfig": t.proxy(renames["VmwareNetworkConfigIn"]).optional(),
                "enableControlPlaneV2": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersEnroll"] = gkeonprem.post(
        "v1/{parent}/vmwareClusters",
        t.struct(
            {
                "vmwareClusterId": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "parent": t.string(),
                "antiAffinityGroups": t.proxy(renames["VmwareAAGConfigIn"]).optional(),
                "loadBalancer": t.proxy(
                    renames["VmwareLoadBalancerConfigIn"]
                ).optional(),
                "vmTrackingEnabled": t.boolean().optional(),
                "storage": t.proxy(renames["VmwareStorageConfigIn"]).optional(),
                "name": t.string().optional(),
                "dataplaneV2": t.proxy(renames["VmwareDataplaneV2ConfigIn"]).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "autoRepairConfig": t.proxy(
                    renames["VmwareAutoRepairConfigIn"]
                ).optional(),
                "onPremVersion": t.string().optional(),
                "controlPlaneNode": t.proxy(
                    renames["VmwareControlPlaneNodeConfigIn"]
                ).optional(),
                "description": t.string().optional(),
                "etag": t.string().optional(),
                "authorization": t.proxy(renames["AuthorizationIn"]).optional(),
                "adminClusterMembership": t.string(),
                "networkConfig": t.proxy(renames["VmwareNetworkConfigIn"]).optional(),
                "enableControlPlaneV2": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersUnenroll"] = gkeonprem.post(
        "v1/{parent}/vmwareClusters",
        t.struct(
            {
                "vmwareClusterId": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "parent": t.string(),
                "antiAffinityGroups": t.proxy(renames["VmwareAAGConfigIn"]).optional(),
                "loadBalancer": t.proxy(
                    renames["VmwareLoadBalancerConfigIn"]
                ).optional(),
                "vmTrackingEnabled": t.boolean().optional(),
                "storage": t.proxy(renames["VmwareStorageConfigIn"]).optional(),
                "name": t.string().optional(),
                "dataplaneV2": t.proxy(renames["VmwareDataplaneV2ConfigIn"]).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "autoRepairConfig": t.proxy(
                    renames["VmwareAutoRepairConfigIn"]
                ).optional(),
                "onPremVersion": t.string().optional(),
                "controlPlaneNode": t.proxy(
                    renames["VmwareControlPlaneNodeConfigIn"]
                ).optional(),
                "description": t.string().optional(),
                "etag": t.string().optional(),
                "authorization": t.proxy(renames["AuthorizationIn"]).optional(),
                "adminClusterMembership": t.string(),
                "networkConfig": t.proxy(renames["VmwareNetworkConfigIn"]).optional(),
                "enableControlPlaneV2": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersSetIamPolicy"] = gkeonprem.post(
        "v1/{parent}/vmwareClusters",
        t.struct(
            {
                "vmwareClusterId": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "parent": t.string(),
                "antiAffinityGroups": t.proxy(renames["VmwareAAGConfigIn"]).optional(),
                "loadBalancer": t.proxy(
                    renames["VmwareLoadBalancerConfigIn"]
                ).optional(),
                "vmTrackingEnabled": t.boolean().optional(),
                "storage": t.proxy(renames["VmwareStorageConfigIn"]).optional(),
                "name": t.string().optional(),
                "dataplaneV2": t.proxy(renames["VmwareDataplaneV2ConfigIn"]).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "autoRepairConfig": t.proxy(
                    renames["VmwareAutoRepairConfigIn"]
                ).optional(),
                "onPremVersion": t.string().optional(),
                "controlPlaneNode": t.proxy(
                    renames["VmwareControlPlaneNodeConfigIn"]
                ).optional(),
                "description": t.string().optional(),
                "etag": t.string().optional(),
                "authorization": t.proxy(renames["AuthorizationIn"]).optional(),
                "adminClusterMembership": t.string(),
                "networkConfig": t.proxy(renames["VmwareNetworkConfigIn"]).optional(),
                "enableControlPlaneV2": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersCreate"] = gkeonprem.post(
        "v1/{parent}/vmwareClusters",
        t.struct(
            {
                "vmwareClusterId": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "parent": t.string(),
                "antiAffinityGroups": t.proxy(renames["VmwareAAGConfigIn"]).optional(),
                "loadBalancer": t.proxy(
                    renames["VmwareLoadBalancerConfigIn"]
                ).optional(),
                "vmTrackingEnabled": t.boolean().optional(),
                "storage": t.proxy(renames["VmwareStorageConfigIn"]).optional(),
                "name": t.string().optional(),
                "dataplaneV2": t.proxy(renames["VmwareDataplaneV2ConfigIn"]).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "autoRepairConfig": t.proxy(
                    renames["VmwareAutoRepairConfigIn"]
                ).optional(),
                "onPremVersion": t.string().optional(),
                "controlPlaneNode": t.proxy(
                    renames["VmwareControlPlaneNodeConfigIn"]
                ).optional(),
                "description": t.string().optional(),
                "etag": t.string().optional(),
                "authorization": t.proxy(renames["AuthorizationIn"]).optional(),
                "adminClusterMembership": t.string(),
                "networkConfig": t.proxy(renames["VmwareNetworkConfigIn"]).optional(),
                "enableControlPlaneV2": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersOperationsGet"] = gkeonprem.get(
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
    functions["projectsLocationsVmwareClustersOperationsList"] = gkeonprem.get(
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
    functions["projectsLocationsVmwareClustersVmwareNodePoolsGet"] = gkeonprem.post(
        "v1/{parent}/vmwareNodePools:enroll",
        t.struct(
            {
                "parent": t.string(),
                "vmwareNodePoolId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersVmwareNodePoolsCreate"] = gkeonprem.post(
        "v1/{parent}/vmwareNodePools:enroll",
        t.struct(
            {
                "parent": t.string(),
                "vmwareNodePoolId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersVmwareNodePoolsList"] = gkeonprem.post(
        "v1/{parent}/vmwareNodePools:enroll",
        t.struct(
            {
                "parent": t.string(),
                "vmwareNodePoolId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersVmwareNodePoolsPatch"] = gkeonprem.post(
        "v1/{parent}/vmwareNodePools:enroll",
        t.struct(
            {
                "parent": t.string(),
                "vmwareNodePoolId": t.string().optional(),
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
        "v1/{parent}/vmwareNodePools:enroll",
        t.struct(
            {
                "parent": t.string(),
                "vmwareNodePoolId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersVmwareNodePoolsDelete"] = gkeonprem.post(
        "v1/{parent}/vmwareNodePools:enroll",
        t.struct(
            {
                "parent": t.string(),
                "vmwareNodePoolId": t.string().optional(),
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
        "v1/{parent}/vmwareNodePools:enroll",
        t.struct(
            {
                "parent": t.string(),
                "vmwareNodePoolId": t.string().optional(),
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
        "v1/{parent}/vmwareNodePools:enroll",
        t.struct(
            {
                "parent": t.string(),
                "vmwareNodePoolId": t.string().optional(),
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
        "v1/{parent}/vmwareNodePools:enroll",
        t.struct(
            {
                "parent": t.string(),
                "vmwareNodePoolId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersVmwareNodePoolsEnroll"] = gkeonprem.post(
        "v1/{parent}/vmwareNodePools:enroll",
        t.struct(
            {
                "parent": t.string(),
                "vmwareNodePoolId": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
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
