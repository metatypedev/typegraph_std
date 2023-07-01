from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_gkehub():
    gkehub = HTTPRuntime("https://gkehub.googleapis.com/")

    renames = {
        "ErrorResponse": "_gkehub_1_ErrorResponse",
        "LocationIn": "_gkehub_2_LocationIn",
        "LocationOut": "_gkehub_3_LocationOut",
        "MembershipFeatureStateIn": "_gkehub_4_MembershipFeatureStateIn",
        "MembershipFeatureStateOut": "_gkehub_5_MembershipFeatureStateOut",
        "AuthorityIn": "_gkehub_6_AuthorityIn",
        "AuthorityOut": "_gkehub_7_AuthorityOut",
        "ConfigManagementPolicyControllerVersionIn": "_gkehub_8_ConfigManagementPolicyControllerVersionIn",
        "ConfigManagementPolicyControllerVersionOut": "_gkehub_9_ConfigManagementPolicyControllerVersionOut",
        "MembershipFeatureSpecIn": "_gkehub_10_MembershipFeatureSpecIn",
        "MembershipFeatureSpecOut": "_gkehub_11_MembershipFeatureSpecOut",
        "ConfigManagementOperatorStateIn": "_gkehub_12_ConfigManagementOperatorStateIn",
        "ConfigManagementOperatorStateOut": "_gkehub_13_ConfigManagementOperatorStateOut",
        "MembershipEndpointIn": "_gkehub_14_MembershipEndpointIn",
        "MembershipEndpointOut": "_gkehub_15_MembershipEndpointOut",
        "ConfigManagementConfigSyncErrorIn": "_gkehub_16_ConfigManagementConfigSyncErrorIn",
        "ConfigManagementConfigSyncErrorOut": "_gkehub_17_ConfigManagementConfigSyncErrorOut",
        "IdentityServiceOidcConfigIn": "_gkehub_18_IdentityServiceOidcConfigIn",
        "IdentityServiceOidcConfigOut": "_gkehub_19_IdentityServiceOidcConfigOut",
        "ConfigManagementConfigSyncIn": "_gkehub_20_ConfigManagementConfigSyncIn",
        "ConfigManagementConfigSyncOut": "_gkehub_21_ConfigManagementConfigSyncOut",
        "ListFleetsResponseIn": "_gkehub_22_ListFleetsResponseIn",
        "ListFleetsResponseOut": "_gkehub_23_ListFleetsResponseOut",
        "StatusIn": "_gkehub_24_StatusIn",
        "StatusOut": "_gkehub_25_StatusOut",
        "ConfigManagementPolicyControllerMonitoringIn": "_gkehub_26_ConfigManagementPolicyControllerMonitoringIn",
        "ConfigManagementPolicyControllerMonitoringOut": "_gkehub_27_ConfigManagementPolicyControllerMonitoringOut",
        "ConfigManagementGitConfigIn": "_gkehub_28_ConfigManagementGitConfigIn",
        "ConfigManagementGitConfigOut": "_gkehub_29_ConfigManagementGitConfigOut",
        "IdentityServiceAuthMethodIn": "_gkehub_30_IdentityServiceAuthMethodIn",
        "IdentityServiceAuthMethodOut": "_gkehub_31_IdentityServiceAuthMethodOut",
        "ResourceManifestIn": "_gkehub_32_ResourceManifestIn",
        "ResourceManifestOut": "_gkehub_33_ResourceManifestOut",
        "FeatureResourceStateIn": "_gkehub_34_FeatureResourceStateIn",
        "FeatureResourceStateOut": "_gkehub_35_FeatureResourceStateOut",
        "ScopeFeatureStateIn": "_gkehub_36_ScopeFeatureStateIn",
        "ScopeFeatureStateOut": "_gkehub_37_ScopeFeatureStateOut",
        "ConfigManagementPolicyControllerMigrationIn": "_gkehub_38_ConfigManagementPolicyControllerMigrationIn",
        "ConfigManagementPolicyControllerMigrationOut": "_gkehub_39_ConfigManagementPolicyControllerMigrationOut",
        "ConfigManagementPolicyControllerIn": "_gkehub_40_ConfigManagementPolicyControllerIn",
        "ConfigManagementPolicyControllerOut": "_gkehub_41_ConfigManagementPolicyControllerOut",
        "AppDevExperienceFeatureSpecIn": "_gkehub_42_AppDevExperienceFeatureSpecIn",
        "AppDevExperienceFeatureSpecOut": "_gkehub_43_AppDevExperienceFeatureSpecOut",
        "ExprIn": "_gkehub_44_ExprIn",
        "ExprOut": "_gkehub_45_ExprOut",
        "IdentityServiceGoogleConfigIn": "_gkehub_46_IdentityServiceGoogleConfigIn",
        "IdentityServiceGoogleConfigOut": "_gkehub_47_IdentityServiceGoogleConfigOut",
        "ConfigManagementOciConfigIn": "_gkehub_48_ConfigManagementOciConfigIn",
        "ConfigManagementOciConfigOut": "_gkehub_49_ConfigManagementOciConfigOut",
        "MembershipStateIn": "_gkehub_50_MembershipStateIn",
        "MembershipStateOut": "_gkehub_51_MembershipStateOut",
        "FleetObservabilityFeatureStateIn": "_gkehub_52_FleetObservabilityFeatureStateIn",
        "FleetObservabilityFeatureStateOut": "_gkehub_53_FleetObservabilityFeatureStateOut",
        "GenerateConnectManifestResponseIn": "_gkehub_54_GenerateConnectManifestResponseIn",
        "GenerateConnectManifestResponseOut": "_gkehub_55_GenerateConnectManifestResponseOut",
        "SetIamPolicyRequestIn": "_gkehub_56_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_gkehub_57_SetIamPolicyRequestOut",
        "ConfigManagementHierarchyControllerStateIn": "_gkehub_58_ConfigManagementHierarchyControllerStateIn",
        "ConfigManagementHierarchyControllerStateOut": "_gkehub_59_ConfigManagementHierarchyControllerStateOut",
        "ListOperationsResponseIn": "_gkehub_60_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_gkehub_61_ListOperationsResponseOut",
        "OperationMetadataIn": "_gkehub_62_OperationMetadataIn",
        "OperationMetadataOut": "_gkehub_63_OperationMetadataOut",
        "OperationIn": "_gkehub_64_OperationIn",
        "OperationOut": "_gkehub_65_OperationOut",
        "PolicyIn": "_gkehub_66_PolicyIn",
        "PolicyOut": "_gkehub_67_PolicyOut",
        "IdentityServiceAzureADConfigIn": "_gkehub_68_IdentityServiceAzureADConfigIn",
        "IdentityServiceAzureADConfigOut": "_gkehub_69_IdentityServiceAzureADConfigOut",
        "ConfigManagementSyncStateIn": "_gkehub_70_ConfigManagementSyncStateIn",
        "ConfigManagementSyncStateOut": "_gkehub_71_ConfigManagementSyncStateOut",
        "ConfigManagementMembershipStateIn": "_gkehub_72_ConfigManagementMembershipStateIn",
        "ConfigManagementMembershipStateOut": "_gkehub_73_ConfigManagementMembershipStateOut",
        "AppDevExperienceFeatureStateIn": "_gkehub_74_AppDevExperienceFeatureStateIn",
        "AppDevExperienceFeatureStateOut": "_gkehub_75_AppDevExperienceFeatureStateOut",
        "ServiceMeshControlPlaneManagementIn": "_gkehub_76_ServiceMeshControlPlaneManagementIn",
        "ServiceMeshControlPlaneManagementOut": "_gkehub_77_ServiceMeshControlPlaneManagementOut",
        "OriginIn": "_gkehub_78_OriginIn",
        "OriginOut": "_gkehub_79_OriginOut",
        "ConfigManagementHierarchyControllerVersionIn": "_gkehub_80_ConfigManagementHierarchyControllerVersionIn",
        "ConfigManagementHierarchyControllerVersionOut": "_gkehub_81_ConfigManagementHierarchyControllerVersionOut",
        "MultiCloudClusterIn": "_gkehub_82_MultiCloudClusterIn",
        "MultiCloudClusterOut": "_gkehub_83_MultiCloudClusterOut",
        "ListLocationsResponseIn": "_gkehub_84_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_gkehub_85_ListLocationsResponseOut",
        "ConfigManagementConfigSyncVersionIn": "_gkehub_86_ConfigManagementConfigSyncVersionIn",
        "ConfigManagementConfigSyncVersionOut": "_gkehub_87_ConfigManagementConfigSyncVersionOut",
        "CommonFeatureStateIn": "_gkehub_88_CommonFeatureStateIn",
        "CommonFeatureStateOut": "_gkehub_89_CommonFeatureStateOut",
        "FeatureStateIn": "_gkehub_90_FeatureStateIn",
        "FeatureStateOut": "_gkehub_91_FeatureStateOut",
        "ConfigManagementGroupVersionKindIn": "_gkehub_92_ConfigManagementGroupVersionKindIn",
        "ConfigManagementGroupVersionKindOut": "_gkehub_93_ConfigManagementGroupVersionKindOut",
        "ConfigManagementConfigSyncDeploymentStateIn": "_gkehub_94_ConfigManagementConfigSyncDeploymentStateIn",
        "ConfigManagementConfigSyncDeploymentStateOut": "_gkehub_95_ConfigManagementConfigSyncDeploymentStateOut",
        "ListFeaturesResponseIn": "_gkehub_96_ListFeaturesResponseIn",
        "ListFeaturesResponseOut": "_gkehub_97_ListFeaturesResponseOut",
        "ServiceMeshMembershipStateIn": "_gkehub_98_ServiceMeshMembershipStateIn",
        "ServiceMeshMembershipStateOut": "_gkehub_99_ServiceMeshMembershipStateOut",
        "ResourceOptionsIn": "_gkehub_100_ResourceOptionsIn",
        "ResourceOptionsOut": "_gkehub_101_ResourceOptionsOut",
        "CancelOperationRequestIn": "_gkehub_102_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_gkehub_103_CancelOperationRequestOut",
        "MultiClusterIngressFeatureSpecIn": "_gkehub_104_MultiClusterIngressFeatureSpecIn",
        "MultiClusterIngressFeatureSpecOut": "_gkehub_105_MultiClusterIngressFeatureSpecOut",
        "ServiceMeshStatusDetailsIn": "_gkehub_106_ServiceMeshStatusDetailsIn",
        "ServiceMeshStatusDetailsOut": "_gkehub_107_ServiceMeshStatusDetailsOut",
        "ApplianceClusterIn": "_gkehub_108_ApplianceClusterIn",
        "ApplianceClusterOut": "_gkehub_109_ApplianceClusterOut",
        "KubernetesMetadataIn": "_gkehub_110_KubernetesMetadataIn",
        "KubernetesMetadataOut": "_gkehub_111_KubernetesMetadataOut",
        "FeatureIn": "_gkehub_112_FeatureIn",
        "FeatureOut": "_gkehub_113_FeatureOut",
        "FleetLifecycleStateIn": "_gkehub_114_FleetLifecycleStateIn",
        "FleetLifecycleStateOut": "_gkehub_115_FleetLifecycleStateOut",
        "ServiceMeshMembershipSpecIn": "_gkehub_116_ServiceMeshMembershipSpecIn",
        "ServiceMeshMembershipSpecOut": "_gkehub_117_ServiceMeshMembershipSpecOut",
        "TestIamPermissionsResponseIn": "_gkehub_118_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_gkehub_119_TestIamPermissionsResponseOut",
        "ServiceMeshDataPlaneManagementIn": "_gkehub_120_ServiceMeshDataPlaneManagementIn",
        "ServiceMeshDataPlaneManagementOut": "_gkehub_121_ServiceMeshDataPlaneManagementOut",
        "GkeClusterIn": "_gkehub_122_GkeClusterIn",
        "GkeClusterOut": "_gkehub_123_GkeClusterOut",
        "FleetObservabilityFeatureSpecIn": "_gkehub_124_FleetObservabilityFeatureSpecIn",
        "FleetObservabilityFeatureSpecOut": "_gkehub_125_FleetObservabilityFeatureSpecOut",
        "ConfigManagementHierarchyControllerConfigIn": "_gkehub_126_ConfigManagementHierarchyControllerConfigIn",
        "ConfigManagementHierarchyControllerConfigOut": "_gkehub_127_ConfigManagementHierarchyControllerConfigOut",
        "BindingIn": "_gkehub_128_BindingIn",
        "BindingOut": "_gkehub_129_BindingOut",
        "KubernetesResourceIn": "_gkehub_130_KubernetesResourceIn",
        "KubernetesResourceOut": "_gkehub_131_KubernetesResourceOut",
        "TypeMetaIn": "_gkehub_132_TypeMetaIn",
        "TypeMetaOut": "_gkehub_133_TypeMetaOut",
        "ScopeFeatureSpecIn": "_gkehub_134_ScopeFeatureSpecIn",
        "ScopeFeatureSpecOut": "_gkehub_135_ScopeFeatureSpecOut",
        "OnPremClusterIn": "_gkehub_136_OnPremClusterIn",
        "OnPremClusterOut": "_gkehub_137_OnPremClusterOut",
        "ListMembershipBindingsResponseIn": "_gkehub_138_ListMembershipBindingsResponseIn",
        "ListMembershipBindingsResponseOut": "_gkehub_139_ListMembershipBindingsResponseOut",
        "GoogleRpcStatusIn": "_gkehub_140_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_gkehub_141_GoogleRpcStatusOut",
        "TestIamPermissionsRequestIn": "_gkehub_142_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_gkehub_143_TestIamPermissionsRequestOut",
        "FleetIn": "_gkehub_144_FleetIn",
        "FleetOut": "_gkehub_145_FleetOut",
        "ListMembershipsResponseIn": "_gkehub_146_ListMembershipsResponseIn",
        "ListMembershipsResponseOut": "_gkehub_147_ListMembershipsResponseOut",
        "ConfigManagementHierarchyControllerDeploymentStateIn": "_gkehub_148_ConfigManagementHierarchyControllerDeploymentStateIn",
        "ConfigManagementHierarchyControllerDeploymentStateOut": "_gkehub_149_ConfigManagementHierarchyControllerDeploymentStateOut",
        "EdgeClusterIn": "_gkehub_150_EdgeClusterIn",
        "EdgeClusterOut": "_gkehub_151_EdgeClusterOut",
        "ScopeLifecycleStateIn": "_gkehub_152_ScopeLifecycleStateIn",
        "ScopeLifecycleStateOut": "_gkehub_153_ScopeLifecycleStateOut",
        "ConfigManagementPolicyControllerStateIn": "_gkehub_154_ConfigManagementPolicyControllerStateIn",
        "ConfigManagementPolicyControllerStateOut": "_gkehub_155_ConfigManagementPolicyControllerStateOut",
        "ConfigManagementInstallErrorIn": "_gkehub_156_ConfigManagementInstallErrorIn",
        "ConfigManagementInstallErrorOut": "_gkehub_157_ConfigManagementInstallErrorOut",
        "ScopeIn": "_gkehub_158_ScopeIn",
        "ScopeOut": "_gkehub_159_ScopeOut",
        "MonitoringConfigIn": "_gkehub_160_MonitoringConfigIn",
        "MonitoringConfigOut": "_gkehub_161_MonitoringConfigOut",
        "ConfigManagementGatekeeperDeploymentStateIn": "_gkehub_162_ConfigManagementGatekeeperDeploymentStateIn",
        "ConfigManagementGatekeeperDeploymentStateOut": "_gkehub_163_ConfigManagementGatekeeperDeploymentStateOut",
        "AuditLogConfigIn": "_gkehub_164_AuditLogConfigIn",
        "AuditLogConfigOut": "_gkehub_165_AuditLogConfigOut",
        "MembershipBindingIn": "_gkehub_166_MembershipBindingIn",
        "MembershipBindingOut": "_gkehub_167_MembershipBindingOut",
        "ConfigManagementMembershipSpecIn": "_gkehub_168_ConfigManagementMembershipSpecIn",
        "ConfigManagementMembershipSpecOut": "_gkehub_169_ConfigManagementMembershipSpecOut",
        "ConfigManagementErrorResourceIn": "_gkehub_170_ConfigManagementErrorResourceIn",
        "ConfigManagementErrorResourceOut": "_gkehub_171_ConfigManagementErrorResourceOut",
        "EmptyIn": "_gkehub_172_EmptyIn",
        "EmptyOut": "_gkehub_173_EmptyOut",
        "AuditConfigIn": "_gkehub_174_AuditConfigIn",
        "AuditConfigOut": "_gkehub_175_AuditConfigOut",
        "MembershipBindingLifecycleStateIn": "_gkehub_176_MembershipBindingLifecycleStateIn",
        "MembershipBindingLifecycleStateOut": "_gkehub_177_MembershipBindingLifecycleStateOut",
        "MembershipIn": "_gkehub_178_MembershipIn",
        "MembershipOut": "_gkehub_179_MembershipOut",
        "ConfigManagementSyncErrorIn": "_gkehub_180_ConfigManagementSyncErrorIn",
        "ConfigManagementSyncErrorOut": "_gkehub_181_ConfigManagementSyncErrorOut",
        "CommonFeatureSpecIn": "_gkehub_182_CommonFeatureSpecIn",
        "CommonFeatureSpecOut": "_gkehub_183_CommonFeatureSpecOut",
        "ListScopesResponseIn": "_gkehub_184_ListScopesResponseIn",
        "ListScopesResponseOut": "_gkehub_185_ListScopesResponseOut",
        "FleetObservabilityMembershipSpecIn": "_gkehub_186_FleetObservabilityMembershipSpecIn",
        "FleetObservabilityMembershipSpecOut": "_gkehub_187_FleetObservabilityMembershipSpecOut",
        "FleetObservabilityMembershipStateIn": "_gkehub_188_FleetObservabilityMembershipStateIn",
        "FleetObservabilityMembershipStateOut": "_gkehub_189_FleetObservabilityMembershipStateOut",
        "CommonFleetDefaultMemberConfigSpecIn": "_gkehub_190_CommonFleetDefaultMemberConfigSpecIn",
        "CommonFleetDefaultMemberConfigSpecOut": "_gkehub_191_CommonFleetDefaultMemberConfigSpecOut",
        "IdentityServiceMembershipSpecIn": "_gkehub_192_IdentityServiceMembershipSpecIn",
        "IdentityServiceMembershipSpecOut": "_gkehub_193_IdentityServiceMembershipSpecOut",
        "ConnectAgentResourceIn": "_gkehub_194_ConnectAgentResourceIn",
        "ConnectAgentResourceOut": "_gkehub_195_ConnectAgentResourceOut",
        "ConfigManagementConfigSyncStateIn": "_gkehub_196_ConfigManagementConfigSyncStateIn",
        "ConfigManagementConfigSyncStateOut": "_gkehub_197_ConfigManagementConfigSyncStateOut",
        "IdentityServiceMembershipStateIn": "_gkehub_198_IdentityServiceMembershipStateIn",
        "IdentityServiceMembershipStateOut": "_gkehub_199_IdentityServiceMembershipStateOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["LocationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["MembershipFeatureStateIn"] = t.struct(
        {
            "configmanagement": t.proxy(
                renames["ConfigManagementMembershipStateIn"]
            ).optional(),
            "servicemesh": t.proxy(renames["ServiceMeshMembershipStateIn"]).optional(),
            "fleetobservability": t.proxy(
                renames["FleetObservabilityMembershipStateIn"]
            ).optional(),
            "identityservice": t.proxy(
                renames["IdentityServiceMembershipStateIn"]
            ).optional(),
            "appdevexperience": t.proxy(
                renames["AppDevExperienceFeatureStateIn"]
            ).optional(),
            "state": t.proxy(renames["FeatureStateIn"]).optional(),
        }
    ).named(renames["MembershipFeatureStateIn"])
    types["MembershipFeatureStateOut"] = t.struct(
        {
            "configmanagement": t.proxy(
                renames["ConfigManagementMembershipStateOut"]
            ).optional(),
            "servicemesh": t.proxy(renames["ServiceMeshMembershipStateOut"]).optional(),
            "fleetobservability": t.proxy(
                renames["FleetObservabilityMembershipStateOut"]
            ).optional(),
            "identityservice": t.proxy(
                renames["IdentityServiceMembershipStateOut"]
            ).optional(),
            "appdevexperience": t.proxy(
                renames["AppDevExperienceFeatureStateOut"]
            ).optional(),
            "state": t.proxy(renames["FeatureStateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipFeatureStateOut"])
    types["AuthorityIn"] = t.struct(
        {"oidcJwks": t.string().optional(), "issuer": t.string().optional()}
    ).named(renames["AuthorityIn"])
    types["AuthorityOut"] = t.struct(
        {
            "oidcJwks": t.string().optional(),
            "workloadIdentityPool": t.string().optional(),
            "identityProvider": t.string().optional(),
            "issuer": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthorityOut"])
    types["ConfigManagementPolicyControllerVersionIn"] = t.struct(
        {"version": t.string().optional()}
    ).named(renames["ConfigManagementPolicyControllerVersionIn"])
    types["ConfigManagementPolicyControllerVersionOut"] = t.struct(
        {
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementPolicyControllerVersionOut"])
    types["MembershipFeatureSpecIn"] = t.struct(
        {
            "fleetobservability": t.proxy(
                renames["FleetObservabilityMembershipSpecIn"]
            ).optional(),
            "mesh": t.proxy(renames["ServiceMeshMembershipSpecIn"]).optional(),
            "configmanagement": t.proxy(
                renames["ConfigManagementMembershipSpecIn"]
            ).optional(),
            "identityservice": t.proxy(
                renames["IdentityServiceMembershipSpecIn"]
            ).optional(),
            "origin": t.proxy(renames["OriginIn"]).optional(),
        }
    ).named(renames["MembershipFeatureSpecIn"])
    types["MembershipFeatureSpecOut"] = t.struct(
        {
            "fleetobservability": t.proxy(
                renames["FleetObservabilityMembershipSpecOut"]
            ).optional(),
            "mesh": t.proxy(renames["ServiceMeshMembershipSpecOut"]).optional(),
            "configmanagement": t.proxy(
                renames["ConfigManagementMembershipSpecOut"]
            ).optional(),
            "identityservice": t.proxy(
                renames["IdentityServiceMembershipSpecOut"]
            ).optional(),
            "origin": t.proxy(renames["OriginOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipFeatureSpecOut"])
    types["ConfigManagementOperatorStateIn"] = t.struct(
        {
            "errors": t.array(
                t.proxy(renames["ConfigManagementInstallErrorIn"])
            ).optional(),
            "deploymentState": t.string().optional(),
            "version": t.string().optional(),
        }
    ).named(renames["ConfigManagementOperatorStateIn"])
    types["ConfigManagementOperatorStateOut"] = t.struct(
        {
            "errors": t.array(
                t.proxy(renames["ConfigManagementInstallErrorOut"])
            ).optional(),
            "deploymentState": t.string().optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementOperatorStateOut"])
    types["MembershipEndpointIn"] = t.struct(
        {
            "multiCloudCluster": t.proxy(renames["MultiCloudClusterIn"]).optional(),
            "edgeCluster": t.proxy(renames["EdgeClusterIn"]).optional(),
            "applianceCluster": t.proxy(renames["ApplianceClusterIn"]).optional(),
            "onPremCluster": t.proxy(renames["OnPremClusterIn"]).optional(),
            "kubernetesResource": t.proxy(renames["KubernetesResourceIn"]).optional(),
            "gkeCluster": t.proxy(renames["GkeClusterIn"]).optional(),
        }
    ).named(renames["MembershipEndpointIn"])
    types["MembershipEndpointOut"] = t.struct(
        {
            "multiCloudCluster": t.proxy(renames["MultiCloudClusterOut"]).optional(),
            "edgeCluster": t.proxy(renames["EdgeClusterOut"]).optional(),
            "applianceCluster": t.proxy(renames["ApplianceClusterOut"]).optional(),
            "kubernetesMetadata": t.proxy(renames["KubernetesMetadataOut"]).optional(),
            "onPremCluster": t.proxy(renames["OnPremClusterOut"]).optional(),
            "kubernetesResource": t.proxy(renames["KubernetesResourceOut"]).optional(),
            "googleManaged": t.boolean().optional(),
            "gkeCluster": t.proxy(renames["GkeClusterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipEndpointOut"])
    types["ConfigManagementConfigSyncErrorIn"] = t.struct(
        {"errorMessage": t.string().optional()}
    ).named(renames["ConfigManagementConfigSyncErrorIn"])
    types["ConfigManagementConfigSyncErrorOut"] = t.struct(
        {
            "errorMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementConfigSyncErrorOut"])
    types["IdentityServiceOidcConfigIn"] = t.struct(
        {
            "extraParams": t.string().optional(),
            "clientId": t.string().optional(),
            "clientSecret": t.string().optional(),
            "scopes": t.string().optional(),
            "enableAccessToken": t.boolean().optional(),
            "certificateAuthorityData": t.string().optional(),
            "userPrefix": t.string().optional(),
            "issuerUri": t.string().optional(),
            "groupsClaim": t.string().optional(),
            "kubectlRedirectUri": t.string().optional(),
            "groupPrefix": t.string().optional(),
            "userClaim": t.string().optional(),
            "deployCloudConsoleProxy": t.boolean().optional(),
        }
    ).named(renames["IdentityServiceOidcConfigIn"])
    types["IdentityServiceOidcConfigOut"] = t.struct(
        {
            "extraParams": t.string().optional(),
            "clientId": t.string().optional(),
            "clientSecret": t.string().optional(),
            "scopes": t.string().optional(),
            "enableAccessToken": t.boolean().optional(),
            "certificateAuthorityData": t.string().optional(),
            "userPrefix": t.string().optional(),
            "issuerUri": t.string().optional(),
            "groupsClaim": t.string().optional(),
            "kubectlRedirectUri": t.string().optional(),
            "groupPrefix": t.string().optional(),
            "userClaim": t.string().optional(),
            "encryptedClientSecret": t.string().optional(),
            "deployCloudConsoleProxy": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentityServiceOidcConfigOut"])
    types["ConfigManagementConfigSyncIn"] = t.struct(
        {
            "git": t.proxy(renames["ConfigManagementGitConfigIn"]).optional(),
            "allowVerticalScale": t.boolean().optional(),
            "sourceFormat": t.string().optional(),
            "enabled": t.boolean().optional(),
            "oci": t.proxy(renames["ConfigManagementOciConfigIn"]).optional(),
            "metricsGcpServiceAccountEmail": t.string().optional(),
            "stopSyncing": t.boolean().optional(),
            "preventDrift": t.boolean().optional(),
        }
    ).named(renames["ConfigManagementConfigSyncIn"])
    types["ConfigManagementConfigSyncOut"] = t.struct(
        {
            "git": t.proxy(renames["ConfigManagementGitConfigOut"]).optional(),
            "allowVerticalScale": t.boolean().optional(),
            "sourceFormat": t.string().optional(),
            "enabled": t.boolean().optional(),
            "oci": t.proxy(renames["ConfigManagementOciConfigOut"]).optional(),
            "metricsGcpServiceAccountEmail": t.string().optional(),
            "stopSyncing": t.boolean().optional(),
            "preventDrift": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementConfigSyncOut"])
    types["ListFleetsResponseIn"] = t.struct(
        {
            "fleets": t.array(t.proxy(renames["FleetIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListFleetsResponseIn"])
    types["ListFleetsResponseOut"] = t.struct(
        {
            "fleets": t.array(t.proxy(renames["FleetOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListFleetsResponseOut"])
    types["StatusIn"] = t.struct(
        {"code": t.string().optional(), "description": t.string().optional()}
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "code": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["ConfigManagementPolicyControllerMonitoringIn"] = t.struct(
        {"backends": t.array(t.string()).optional()}
    ).named(renames["ConfigManagementPolicyControllerMonitoringIn"])
    types["ConfigManagementPolicyControllerMonitoringOut"] = t.struct(
        {
            "backends": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementPolicyControllerMonitoringOut"])
    types["ConfigManagementGitConfigIn"] = t.struct(
        {
            "syncWaitSecs": t.string().optional(),
            "policyDir": t.string().optional(),
            "syncBranch": t.string().optional(),
            "secretType": t.string().optional(),
            "httpsProxy": t.string().optional(),
            "syncRepo": t.string().optional(),
            "gcpServiceAccountEmail": t.string().optional(),
            "syncRev": t.string().optional(),
        }
    ).named(renames["ConfigManagementGitConfigIn"])
    types["ConfigManagementGitConfigOut"] = t.struct(
        {
            "syncWaitSecs": t.string().optional(),
            "policyDir": t.string().optional(),
            "syncBranch": t.string().optional(),
            "secretType": t.string().optional(),
            "httpsProxy": t.string().optional(),
            "syncRepo": t.string().optional(),
            "gcpServiceAccountEmail": t.string().optional(),
            "syncRev": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementGitConfigOut"])
    types["IdentityServiceAuthMethodIn"] = t.struct(
        {
            "oidcConfig": t.proxy(renames["IdentityServiceOidcConfigIn"]).optional(),
            "googleConfig": t.proxy(
                renames["IdentityServiceGoogleConfigIn"]
            ).optional(),
            "proxy": t.string().optional(),
            "name": t.string().optional(),
            "azureadConfig": t.proxy(
                renames["IdentityServiceAzureADConfigIn"]
            ).optional(),
        }
    ).named(renames["IdentityServiceAuthMethodIn"])
    types["IdentityServiceAuthMethodOut"] = t.struct(
        {
            "oidcConfig": t.proxy(renames["IdentityServiceOidcConfigOut"]).optional(),
            "googleConfig": t.proxy(
                renames["IdentityServiceGoogleConfigOut"]
            ).optional(),
            "proxy": t.string().optional(),
            "name": t.string().optional(),
            "azureadConfig": t.proxy(
                renames["IdentityServiceAzureADConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentityServiceAuthMethodOut"])
    types["ResourceManifestIn"] = t.struct(
        {"clusterScoped": t.boolean().optional(), "manifest": t.string().optional()}
    ).named(renames["ResourceManifestIn"])
    types["ResourceManifestOut"] = t.struct(
        {
            "clusterScoped": t.boolean().optional(),
            "manifest": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceManifestOut"])
    types["FeatureResourceStateIn"] = t.struct({"state": t.string().optional()}).named(
        renames["FeatureResourceStateIn"]
    )
    types["FeatureResourceStateOut"] = t.struct(
        {
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FeatureResourceStateOut"])
    types["ScopeFeatureStateIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ScopeFeatureStateIn"]
    )
    types["ScopeFeatureStateOut"] = t.struct(
        {
            "state": t.proxy(renames["FeatureStateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScopeFeatureStateOut"])
    types["ConfigManagementPolicyControllerMigrationIn"] = t.struct(
        {"stage": t.string().optional(), "copyTime": t.string().optional()}
    ).named(renames["ConfigManagementPolicyControllerMigrationIn"])
    types["ConfigManagementPolicyControllerMigrationOut"] = t.struct(
        {
            "stage": t.string().optional(),
            "copyTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementPolicyControllerMigrationOut"])
    types["ConfigManagementPolicyControllerIn"] = t.struct(
        {
            "auditIntervalSeconds": t.string().optional(),
            "enabled": t.boolean().optional(),
            "mutationEnabled": t.boolean().optional(),
            "templateLibraryInstalled": t.boolean().optional(),
            "logDeniesEnabled": t.boolean().optional(),
            "monitoring": t.proxy(
                renames["ConfigManagementPolicyControllerMonitoringIn"]
            ).optional(),
            "exemptableNamespaces": t.array(t.string()).optional(),
            "referentialRulesEnabled": t.boolean().optional(),
        }
    ).named(renames["ConfigManagementPolicyControllerIn"])
    types["ConfigManagementPolicyControllerOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "auditIntervalSeconds": t.string().optional(),
            "enabled": t.boolean().optional(),
            "mutationEnabled": t.boolean().optional(),
            "templateLibraryInstalled": t.boolean().optional(),
            "logDeniesEnabled": t.boolean().optional(),
            "monitoring": t.proxy(
                renames["ConfigManagementPolicyControllerMonitoringOut"]
            ).optional(),
            "exemptableNamespaces": t.array(t.string()).optional(),
            "referentialRulesEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementPolicyControllerOut"])
    types["AppDevExperienceFeatureSpecIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AppDevExperienceFeatureSpecIn"])
    types["AppDevExperienceFeatureSpecOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AppDevExperienceFeatureSpecOut"])
    types["ExprIn"] = t.struct(
        {
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["IdentityServiceGoogleConfigIn"] = t.struct(
        {"disable": t.boolean().optional()}
    ).named(renames["IdentityServiceGoogleConfigIn"])
    types["IdentityServiceGoogleConfigOut"] = t.struct(
        {
            "disable": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentityServiceGoogleConfigOut"])
    types["ConfigManagementOciConfigIn"] = t.struct(
        {
            "policyDir": t.string().optional(),
            "syncWaitSecs": t.string().optional(),
            "secretType": t.string().optional(),
            "gcpServiceAccountEmail": t.string().optional(),
            "syncRepo": t.string().optional(),
        }
    ).named(renames["ConfigManagementOciConfigIn"])
    types["ConfigManagementOciConfigOut"] = t.struct(
        {
            "policyDir": t.string().optional(),
            "syncWaitSecs": t.string().optional(),
            "secretType": t.string().optional(),
            "gcpServiceAccountEmail": t.string().optional(),
            "syncRepo": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementOciConfigOut"])
    types["MembershipStateIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MembershipStateIn"]
    )
    types["MembershipStateOut"] = t.struct(
        {
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipStateOut"])
    types["FleetObservabilityFeatureStateIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["FleetObservabilityFeatureStateIn"])
    types["FleetObservabilityFeatureStateOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["FleetObservabilityFeatureStateOut"])
    types["GenerateConnectManifestResponseIn"] = t.struct(
        {"manifest": t.array(t.proxy(renames["ConnectAgentResourceIn"])).optional()}
    ).named(renames["GenerateConnectManifestResponseIn"])
    types["GenerateConnectManifestResponseOut"] = t.struct(
        {
            "manifest": t.array(t.proxy(renames["ConnectAgentResourceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateConnectManifestResponseOut"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyIn"]).optional(),
            "updateMask": t.string().optional(),
        }
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "updateMask": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
    types["ConfigManagementHierarchyControllerStateIn"] = t.struct(
        {
            "version": t.proxy(
                renames["ConfigManagementHierarchyControllerVersionIn"]
            ).optional(),
            "state": t.proxy(
                renames["ConfigManagementHierarchyControllerDeploymentStateIn"]
            ).optional(),
        }
    ).named(renames["ConfigManagementHierarchyControllerStateIn"])
    types["ConfigManagementHierarchyControllerStateOut"] = t.struct(
        {
            "version": t.proxy(
                renames["ConfigManagementHierarchyControllerVersionOut"]
            ).optional(),
            "state": t.proxy(
                renames["ConfigManagementHierarchyControllerDeploymentStateOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementHierarchyControllerStateOut"])
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
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "endTime": t.string().optional(),
            "verb": t.string().optional(),
            "target": t.string().optional(),
            "apiVersion": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "statusDetail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["OperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationOut"])
    types["PolicyIn"] = t.struct(
        {
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["IdentityServiceAzureADConfigIn"] = t.struct(
        {
            "tenant": t.string().optional(),
            "clientSecret": t.string().optional(),
            "clientId": t.string().optional(),
            "kubectlRedirectUri": t.string().optional(),
        }
    ).named(renames["IdentityServiceAzureADConfigIn"])
    types["IdentityServiceAzureADConfigOut"] = t.struct(
        {
            "tenant": t.string().optional(),
            "clientSecret": t.string().optional(),
            "encryptedClientSecret": t.string().optional(),
            "clientId": t.string().optional(),
            "kubectlRedirectUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentityServiceAzureADConfigOut"])
    types["ConfigManagementSyncStateIn"] = t.struct(
        {
            "code": t.string().optional(),
            "sourceToken": t.string().optional(),
            "errors": t.array(
                t.proxy(renames["ConfigManagementSyncErrorIn"])
            ).optional(),
            "lastSync": t.string().optional(),
            "syncToken": t.string().optional(),
            "lastSyncTime": t.string().optional(),
            "importToken": t.string().optional(),
        }
    ).named(renames["ConfigManagementSyncStateIn"])
    types["ConfigManagementSyncStateOut"] = t.struct(
        {
            "code": t.string().optional(),
            "sourceToken": t.string().optional(),
            "errors": t.array(
                t.proxy(renames["ConfigManagementSyncErrorOut"])
            ).optional(),
            "lastSync": t.string().optional(),
            "syncToken": t.string().optional(),
            "lastSyncTime": t.string().optional(),
            "importToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementSyncStateOut"])
    types["ConfigManagementMembershipStateIn"] = t.struct(
        {
            "hierarchyControllerState": t.proxy(
                renames["ConfigManagementHierarchyControllerStateIn"]
            ).optional(),
            "policyControllerState": t.proxy(
                renames["ConfigManagementPolicyControllerStateIn"]
            ).optional(),
            "clusterName": t.string().optional(),
            "configSyncState": t.proxy(
                renames["ConfigManagementConfigSyncStateIn"]
            ).optional(),
            "operatorState": t.proxy(
                renames["ConfigManagementOperatorStateIn"]
            ).optional(),
            "membershipSpec": t.proxy(
                renames["ConfigManagementMembershipSpecIn"]
            ).optional(),
        }
    ).named(renames["ConfigManagementMembershipStateIn"])
    types["ConfigManagementMembershipStateOut"] = t.struct(
        {
            "hierarchyControllerState": t.proxy(
                renames["ConfigManagementHierarchyControllerStateOut"]
            ).optional(),
            "policyControllerState": t.proxy(
                renames["ConfigManagementPolicyControllerStateOut"]
            ).optional(),
            "clusterName": t.string().optional(),
            "configSyncState": t.proxy(
                renames["ConfigManagementConfigSyncStateOut"]
            ).optional(),
            "operatorState": t.proxy(
                renames["ConfigManagementOperatorStateOut"]
            ).optional(),
            "membershipSpec": t.proxy(
                renames["ConfigManagementMembershipSpecOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementMembershipStateOut"])
    types["AppDevExperienceFeatureStateIn"] = t.struct(
        {"networkingInstallSucceeded": t.proxy(renames["StatusIn"]).optional()}
    ).named(renames["AppDevExperienceFeatureStateIn"])
    types["AppDevExperienceFeatureStateOut"] = t.struct(
        {
            "networkingInstallSucceeded": t.proxy(renames["StatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppDevExperienceFeatureStateOut"])
    types["ServiceMeshControlPlaneManagementIn"] = t.struct(
        {
            "state": t.string().optional(),
            "details": t.array(
                t.proxy(renames["ServiceMeshStatusDetailsIn"])
            ).optional(),
        }
    ).named(renames["ServiceMeshControlPlaneManagementIn"])
    types["ServiceMeshControlPlaneManagementOut"] = t.struct(
        {
            "state": t.string().optional(),
            "details": t.array(
                t.proxy(renames["ServiceMeshStatusDetailsOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceMeshControlPlaneManagementOut"])
    types["OriginIn"] = t.struct({"type": t.string().optional()}).named(
        renames["OriginIn"]
    )
    types["OriginOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OriginOut"])
    types["ConfigManagementHierarchyControllerVersionIn"] = t.struct(
        {"extension": t.string().optional(), "hnc": t.string().optional()}
    ).named(renames["ConfigManagementHierarchyControllerVersionIn"])
    types["ConfigManagementHierarchyControllerVersionOut"] = t.struct(
        {
            "extension": t.string().optional(),
            "hnc": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementHierarchyControllerVersionOut"])
    types["MultiCloudClusterIn"] = t.struct(
        {"resourceLink": t.string().optional()}
    ).named(renames["MultiCloudClusterIn"])
    types["MultiCloudClusterOut"] = t.struct(
        {
            "clusterMissing": t.boolean().optional(),
            "resourceLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MultiCloudClusterOut"])
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
    types["ConfigManagementConfigSyncVersionIn"] = t.struct(
        {
            "syncer": t.string().optional(),
            "admissionWebhook": t.string().optional(),
            "reconcilerManager": t.string().optional(),
            "gitSync": t.string().optional(),
            "rootReconciler": t.string().optional(),
            "importer": t.string().optional(),
            "monitor": t.string().optional(),
        }
    ).named(renames["ConfigManagementConfigSyncVersionIn"])
    types["ConfigManagementConfigSyncVersionOut"] = t.struct(
        {
            "syncer": t.string().optional(),
            "admissionWebhook": t.string().optional(),
            "reconcilerManager": t.string().optional(),
            "gitSync": t.string().optional(),
            "rootReconciler": t.string().optional(),
            "importer": t.string().optional(),
            "monitor": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementConfigSyncVersionOut"])
    types["CommonFeatureStateIn"] = t.struct(
        {
            "appdevexperience": t.proxy(
                renames["AppDevExperienceFeatureStateIn"]
            ).optional(),
            "fleetobservability": t.proxy(
                renames["FleetObservabilityFeatureStateIn"]
            ).optional(),
        }
    ).named(renames["CommonFeatureStateIn"])
    types["CommonFeatureStateOut"] = t.struct(
        {
            "appdevexperience": t.proxy(
                renames["AppDevExperienceFeatureStateOut"]
            ).optional(),
            "fleetobservability": t.proxy(
                renames["FleetObservabilityFeatureStateOut"]
            ).optional(),
            "state": t.proxy(renames["FeatureStateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommonFeatureStateOut"])
    types["FeatureStateIn"] = t.struct(
        {
            "description": t.string().optional(),
            "updateTime": t.string().optional(),
            "code": t.string().optional(),
        }
    ).named(renames["FeatureStateIn"])
    types["FeatureStateOut"] = t.struct(
        {
            "description": t.string().optional(),
            "updateTime": t.string().optional(),
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FeatureStateOut"])
    types["ConfigManagementGroupVersionKindIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "version": t.string().optional(),
            "group": t.string().optional(),
        }
    ).named(renames["ConfigManagementGroupVersionKindIn"])
    types["ConfigManagementGroupVersionKindOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "version": t.string().optional(),
            "group": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementGroupVersionKindOut"])
    types["ConfigManagementConfigSyncDeploymentStateIn"] = t.struct(
        {
            "admissionWebhook": t.string().optional(),
            "reconcilerManager": t.string().optional(),
            "syncer": t.string().optional(),
            "monitor": t.string().optional(),
            "importer": t.string().optional(),
            "gitSync": t.string().optional(),
            "rootReconciler": t.string().optional(),
        }
    ).named(renames["ConfigManagementConfigSyncDeploymentStateIn"])
    types["ConfigManagementConfigSyncDeploymentStateOut"] = t.struct(
        {
            "admissionWebhook": t.string().optional(),
            "reconcilerManager": t.string().optional(),
            "syncer": t.string().optional(),
            "monitor": t.string().optional(),
            "importer": t.string().optional(),
            "gitSync": t.string().optional(),
            "rootReconciler": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementConfigSyncDeploymentStateOut"])
    types["ListFeaturesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "resources": t.array(t.proxy(renames["FeatureIn"])).optional(),
        }
    ).named(renames["ListFeaturesResponseIn"])
    types["ListFeaturesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "resources": t.array(t.proxy(renames["FeatureOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListFeaturesResponseOut"])
    types["ServiceMeshMembershipStateIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ServiceMeshMembershipStateIn"])
    types["ServiceMeshMembershipStateOut"] = t.struct(
        {
            "dataPlaneManagement": t.proxy(
                renames["ServiceMeshDataPlaneManagementOut"]
            ).optional(),
            "controlPlaneManagement": t.proxy(
                renames["ServiceMeshControlPlaneManagementOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceMeshMembershipStateOut"])
    types["ResourceOptionsIn"] = t.struct(
        {
            "v1beta1Crd": t.boolean().optional(),
            "k8sVersion": t.string().optional(),
            "connectVersion": t.string().optional(),
        }
    ).named(renames["ResourceOptionsIn"])
    types["ResourceOptionsOut"] = t.struct(
        {
            "v1beta1Crd": t.boolean().optional(),
            "k8sVersion": t.string().optional(),
            "connectVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceOptionsOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["MultiClusterIngressFeatureSpecIn"] = t.struct(
        {"configMembership": t.string().optional()}
    ).named(renames["MultiClusterIngressFeatureSpecIn"])
    types["MultiClusterIngressFeatureSpecOut"] = t.struct(
        {
            "configMembership": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MultiClusterIngressFeatureSpecOut"])
    types["ServiceMeshStatusDetailsIn"] = t.struct(
        {"code": t.string().optional(), "details": t.string().optional()}
    ).named(renames["ServiceMeshStatusDetailsIn"])
    types["ServiceMeshStatusDetailsOut"] = t.struct(
        {
            "code": t.string().optional(),
            "details": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceMeshStatusDetailsOut"])
    types["ApplianceClusterIn"] = t.struct(
        {"resourceLink": t.string().optional()}
    ).named(renames["ApplianceClusterIn"])
    types["ApplianceClusterOut"] = t.struct(
        {
            "resourceLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplianceClusterOut"])
    types["KubernetesMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["KubernetesMetadataIn"]
    )
    types["KubernetesMetadataOut"] = t.struct(
        {
            "nodeProviderId": t.string().optional(),
            "nodeCount": t.integer().optional(),
            "updateTime": t.string().optional(),
            "vcpuCount": t.integer().optional(),
            "kubernetesApiServerVersion": t.string().optional(),
            "memoryMb": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KubernetesMetadataOut"])
    types["FeatureIn"] = t.struct(
        {
            "spec": t.proxy(renames["CommonFeatureSpecIn"]).optional(),
            "fleetDefaultMemberConfig": t.proxy(
                renames["CommonFleetDefaultMemberConfigSpecIn"]
            ).optional(),
            "scopeSpecs": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "membershipSpecs": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["FeatureIn"])
    types["FeatureOut"] = t.struct(
        {
            "name": t.string().optional(),
            "spec": t.proxy(renames["CommonFeatureSpecOut"]).optional(),
            "fleetDefaultMemberConfig": t.proxy(
                renames["CommonFleetDefaultMemberConfigSpecOut"]
            ).optional(),
            "deleteTime": t.string().optional(),
            "resourceState": t.proxy(renames["FeatureResourceStateOut"]).optional(),
            "scopeSpecs": t.struct({"_": t.string().optional()}).optional(),
            "membershipStates": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "scopeStates": t.struct({"_": t.string().optional()}).optional(),
            "state": t.proxy(renames["CommonFeatureStateOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "membershipSpecs": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FeatureOut"])
    types["FleetLifecycleStateIn"] = t.struct({"_": t.string().optional()}).named(
        renames["FleetLifecycleStateIn"]
    )
    types["FleetLifecycleStateOut"] = t.struct(
        {
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FleetLifecycleStateOut"])
    types["ServiceMeshMembershipSpecIn"] = t.struct(
        {"management": t.string().optional(), "controlPlane": t.string().optional()}
    ).named(renames["ServiceMeshMembershipSpecIn"])
    types["ServiceMeshMembershipSpecOut"] = t.struct(
        {
            "management": t.string().optional(),
            "controlPlane": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceMeshMembershipSpecOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["ServiceMeshDataPlaneManagementIn"] = t.struct(
        {
            "details": t.array(
                t.proxy(renames["ServiceMeshStatusDetailsIn"])
            ).optional(),
            "state": t.string().optional(),
        }
    ).named(renames["ServiceMeshDataPlaneManagementIn"])
    types["ServiceMeshDataPlaneManagementOut"] = t.struct(
        {
            "details": t.array(
                t.proxy(renames["ServiceMeshStatusDetailsOut"])
            ).optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceMeshDataPlaneManagementOut"])
    types["GkeClusterIn"] = t.struct({"resourceLink": t.string().optional()}).named(
        renames["GkeClusterIn"]
    )
    types["GkeClusterOut"] = t.struct(
        {
            "clusterMissing": t.boolean().optional(),
            "resourceLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GkeClusterOut"])
    types["FleetObservabilityFeatureSpecIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["FleetObservabilityFeatureSpecIn"])
    types["FleetObservabilityFeatureSpecOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["FleetObservabilityFeatureSpecOut"])
    types["ConfigManagementHierarchyControllerConfigIn"] = t.struct(
        {
            "enablePodTreeLabels": t.boolean().optional(),
            "enableHierarchicalResourceQuota": t.boolean().optional(),
            "enabled": t.boolean().optional(),
        }
    ).named(renames["ConfigManagementHierarchyControllerConfigIn"])
    types["ConfigManagementHierarchyControllerConfigOut"] = t.struct(
        {
            "enablePodTreeLabels": t.boolean().optional(),
            "enableHierarchicalResourceQuota": t.boolean().optional(),
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementHierarchyControllerConfigOut"])
    types["BindingIn"] = t.struct(
        {
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["KubernetesResourceIn"] = t.struct(
        {
            "resourceOptions": t.proxy(renames["ResourceOptionsIn"]).optional(),
            "membershipCrManifest": t.string().optional(),
        }
    ).named(renames["KubernetesResourceIn"])
    types["KubernetesResourceOut"] = t.struct(
        {
            "resourceOptions": t.proxy(renames["ResourceOptionsOut"]).optional(),
            "membershipResources": t.array(
                t.proxy(renames["ResourceManifestOut"])
            ).optional(),
            "connectResources": t.array(
                t.proxy(renames["ResourceManifestOut"])
            ).optional(),
            "membershipCrManifest": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KubernetesResourceOut"])
    types["TypeMetaIn"] = t.struct(
        {"kind": t.string().optional(), "apiVersion": t.string().optional()}
    ).named(renames["TypeMetaIn"])
    types["TypeMetaOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "apiVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TypeMetaOut"])
    types["ScopeFeatureSpecIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ScopeFeatureSpecIn"]
    )
    types["ScopeFeatureSpecOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ScopeFeatureSpecOut"])
    types["OnPremClusterIn"] = t.struct(
        {
            "clusterType": t.string().optional(),
            "resourceLink": t.string().optional(),
            "adminCluster": t.boolean().optional(),
        }
    ).named(renames["OnPremClusterIn"])
    types["OnPremClusterOut"] = t.struct(
        {
            "clusterType": t.string().optional(),
            "resourceLink": t.string().optional(),
            "adminCluster": t.boolean().optional(),
            "clusterMissing": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OnPremClusterOut"])
    types["ListMembershipBindingsResponseIn"] = t.struct(
        {
            "membershipBindings": t.array(
                t.proxy(renames["MembershipBindingIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListMembershipBindingsResponseIn"])
    types["ListMembershipBindingsResponseOut"] = t.struct(
        {
            "membershipBindings": t.array(
                t.proxy(renames["MembershipBindingOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListMembershipBindingsResponseOut"])
    types["GoogleRpcStatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["GoogleRpcStatusIn"])
    types["GoogleRpcStatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleRpcStatusOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["FleetIn"] = t.struct({"displayName": t.string().optional()}).named(
        renames["FleetIn"]
    )
    types["FleetOut"] = t.struct(
        {
            "deleteTime": t.string().optional(),
            "createTime": t.string().optional(),
            "uid": t.string().optional(),
            "displayName": t.string().optional(),
            "state": t.proxy(renames["FleetLifecycleStateOut"]).optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FleetOut"])
    types["ListMembershipsResponseIn"] = t.struct(
        {
            "resources": t.array(t.proxy(renames["MembershipIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListMembershipsResponseIn"])
    types["ListMembershipsResponseOut"] = t.struct(
        {
            "resources": t.array(t.proxy(renames["MembershipOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListMembershipsResponseOut"])
    types["ConfigManagementHierarchyControllerDeploymentStateIn"] = t.struct(
        {"hnc": t.string().optional(), "extension": t.string().optional()}
    ).named(renames["ConfigManagementHierarchyControllerDeploymentStateIn"])
    types["ConfigManagementHierarchyControllerDeploymentStateOut"] = t.struct(
        {
            "hnc": t.string().optional(),
            "extension": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementHierarchyControllerDeploymentStateOut"])
    types["EdgeClusterIn"] = t.struct({"resourceLink": t.string().optional()}).named(
        renames["EdgeClusterIn"]
    )
    types["EdgeClusterOut"] = t.struct(
        {
            "resourceLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EdgeClusterOut"])
    types["ScopeLifecycleStateIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ScopeLifecycleStateIn"]
    )
    types["ScopeLifecycleStateOut"] = t.struct(
        {
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScopeLifecycleStateOut"])
    types["ConfigManagementPolicyControllerStateIn"] = t.struct(
        {
            "version": t.proxy(
                renames["ConfigManagementPolicyControllerVersionIn"]
            ).optional(),
            "migration": t.proxy(
                renames["ConfigManagementPolicyControllerMigrationIn"]
            ).optional(),
            "deploymentState": t.proxy(
                renames["ConfigManagementGatekeeperDeploymentStateIn"]
            ).optional(),
        }
    ).named(renames["ConfigManagementPolicyControllerStateIn"])
    types["ConfigManagementPolicyControllerStateOut"] = t.struct(
        {
            "version": t.proxy(
                renames["ConfigManagementPolicyControllerVersionOut"]
            ).optional(),
            "migration": t.proxy(
                renames["ConfigManagementPolicyControllerMigrationOut"]
            ).optional(),
            "deploymentState": t.proxy(
                renames["ConfigManagementGatekeeperDeploymentStateOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementPolicyControllerStateOut"])
    types["ConfigManagementInstallErrorIn"] = t.struct(
        {"errorMessage": t.string().optional()}
    ).named(renames["ConfigManagementInstallErrorIn"])
    types["ConfigManagementInstallErrorOut"] = t.struct(
        {
            "errorMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementInstallErrorOut"])
    types["ScopeIn"] = t.struct(
        {"allMemberships": t.boolean().optional(), "name": t.string().optional()}
    ).named(renames["ScopeIn"])
    types["ScopeOut"] = t.struct(
        {
            "state": t.proxy(renames["ScopeLifecycleStateOut"]).optional(),
            "uid": t.string().optional(),
            "allMemberships": t.boolean().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "deleteTime": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScopeOut"])
    types["MonitoringConfigIn"] = t.struct(
        {
            "location": t.string().optional(),
            "cluster": t.string().optional(),
            "clusterHash": t.string().optional(),
            "projectId": t.string().optional(),
            "kubernetesMetricsPrefix": t.string().optional(),
        }
    ).named(renames["MonitoringConfigIn"])
    types["MonitoringConfigOut"] = t.struct(
        {
            "location": t.string().optional(),
            "cluster": t.string().optional(),
            "clusterHash": t.string().optional(),
            "projectId": t.string().optional(),
            "kubernetesMetricsPrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MonitoringConfigOut"])
    types["ConfigManagementGatekeeperDeploymentStateIn"] = t.struct(
        {
            "gatekeeperAudit": t.string().optional(),
            "gatekeeperControllerManagerState": t.string().optional(),
            "gatekeeperMutation": t.string().optional(),
        }
    ).named(renames["ConfigManagementGatekeeperDeploymentStateIn"])
    types["ConfigManagementGatekeeperDeploymentStateOut"] = t.struct(
        {
            "gatekeeperAudit": t.string().optional(),
            "gatekeeperControllerManagerState": t.string().optional(),
            "gatekeeperMutation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementGatekeeperDeploymentStateOut"])
    types["AuditLogConfigIn"] = t.struct(
        {
            "logType": t.string().optional(),
            "exemptedMembers": t.array(t.string()).optional(),
        }
    ).named(renames["AuditLogConfigIn"])
    types["AuditLogConfigOut"] = t.struct(
        {
            "logType": t.string().optional(),
            "exemptedMembers": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditLogConfigOut"])
    types["MembershipBindingIn"] = t.struct(
        {
            "fleet": t.boolean().optional(),
            "name": t.string().optional(),
            "scope": t.string().optional(),
        }
    ).named(renames["MembershipBindingIn"])
    types["MembershipBindingOut"] = t.struct(
        {
            "fleet": t.boolean().optional(),
            "createTime": t.string().optional(),
            "state": t.proxy(renames["MembershipBindingLifecycleStateOut"]).optional(),
            "uid": t.string().optional(),
            "deleteTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "scope": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipBindingOut"])
    types["ConfigManagementMembershipSpecIn"] = t.struct(
        {
            "configSync": t.proxy(renames["ConfigManagementConfigSyncIn"]).optional(),
            "hierarchyController": t.proxy(
                renames["ConfigManagementHierarchyControllerConfigIn"]
            ).optional(),
            "management": t.string().optional(),
            "policyController": t.proxy(
                renames["ConfigManagementPolicyControllerIn"]
            ).optional(),
            "cluster": t.string().optional(),
            "version": t.string().optional(),
        }
    ).named(renames["ConfigManagementMembershipSpecIn"])
    types["ConfigManagementMembershipSpecOut"] = t.struct(
        {
            "configSync": t.proxy(renames["ConfigManagementConfigSyncOut"]).optional(),
            "hierarchyController": t.proxy(
                renames["ConfigManagementHierarchyControllerConfigOut"]
            ).optional(),
            "management": t.string().optional(),
            "policyController": t.proxy(
                renames["ConfigManagementPolicyControllerOut"]
            ).optional(),
            "cluster": t.string().optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementMembershipSpecOut"])
    types["ConfigManagementErrorResourceIn"] = t.struct(
        {
            "resourceNamespace": t.string().optional(),
            "resourceGvk": t.proxy(
                renames["ConfigManagementGroupVersionKindIn"]
            ).optional(),
            "sourcePath": t.string().optional(),
            "resourceName": t.string().optional(),
        }
    ).named(renames["ConfigManagementErrorResourceIn"])
    types["ConfigManagementErrorResourceOut"] = t.struct(
        {
            "resourceNamespace": t.string().optional(),
            "resourceGvk": t.proxy(
                renames["ConfigManagementGroupVersionKindOut"]
            ).optional(),
            "sourcePath": t.string().optional(),
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementErrorResourceOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["AuditConfigIn"] = t.struct(
        {
            "service": t.string().optional(),
            "auditLogConfigs": t.array(t.proxy(renames["AuditLogConfigIn"])).optional(),
        }
    ).named(renames["AuditConfigIn"])
    types["AuditConfigOut"] = t.struct(
        {
            "service": t.string().optional(),
            "auditLogConfigs": t.array(
                t.proxy(renames["AuditLogConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditConfigOut"])
    types["MembershipBindingLifecycleStateIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["MembershipBindingLifecycleStateIn"])
    types["MembershipBindingLifecycleStateOut"] = t.struct(
        {
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipBindingLifecycleStateOut"])
    types["MembershipIn"] = t.struct(
        {
            "externalId": t.string().optional(),
            "authority": t.proxy(renames["AuthorityIn"]).optional(),
            "monitoringConfig": t.proxy(renames["MonitoringConfigIn"]).optional(),
            "endpoint": t.proxy(renames["MembershipEndpointIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["MembershipIn"])
    types["MembershipOut"] = t.struct(
        {
            "externalId": t.string().optional(),
            "name": t.string().optional(),
            "uniqueId": t.string().optional(),
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "authority": t.proxy(renames["AuthorityOut"]).optional(),
            "updateTime": t.string().optional(),
            "monitoringConfig": t.proxy(renames["MonitoringConfigOut"]).optional(),
            "state": t.proxy(renames["MembershipStateOut"]).optional(),
            "endpoint": t.proxy(renames["MembershipEndpointOut"]).optional(),
            "deleteTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "lastConnectionTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipOut"])
    types["ConfigManagementSyncErrorIn"] = t.struct(
        {
            "errorMessage": t.string().optional(),
            "code": t.string().optional(),
            "errorResources": t.array(
                t.proxy(renames["ConfigManagementErrorResourceIn"])
            ).optional(),
        }
    ).named(renames["ConfigManagementSyncErrorIn"])
    types["ConfigManagementSyncErrorOut"] = t.struct(
        {
            "errorMessage": t.string().optional(),
            "code": t.string().optional(),
            "errorResources": t.array(
                t.proxy(renames["ConfigManagementErrorResourceOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementSyncErrorOut"])
    types["CommonFeatureSpecIn"] = t.struct(
        {
            "multiclusteringress": t.proxy(
                renames["MultiClusterIngressFeatureSpecIn"]
            ).optional(),
            "appdevexperience": t.proxy(
                renames["AppDevExperienceFeatureSpecIn"]
            ).optional(),
            "fleetobservability": t.proxy(
                renames["FleetObservabilityFeatureSpecIn"]
            ).optional(),
        }
    ).named(renames["CommonFeatureSpecIn"])
    types["CommonFeatureSpecOut"] = t.struct(
        {
            "multiclusteringress": t.proxy(
                renames["MultiClusterIngressFeatureSpecOut"]
            ).optional(),
            "appdevexperience": t.proxy(
                renames["AppDevExperienceFeatureSpecOut"]
            ).optional(),
            "fleetobservability": t.proxy(
                renames["FleetObservabilityFeatureSpecOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommonFeatureSpecOut"])
    types["ListScopesResponseIn"] = t.struct(
        {
            "scopes": t.array(t.proxy(renames["ScopeIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListScopesResponseIn"])
    types["ListScopesResponseOut"] = t.struct(
        {
            "scopes": t.array(t.proxy(renames["ScopeOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListScopesResponseOut"])
    types["FleetObservabilityMembershipSpecIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["FleetObservabilityMembershipSpecIn"])
    types["FleetObservabilityMembershipSpecOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["FleetObservabilityMembershipSpecOut"])
    types["FleetObservabilityMembershipStateIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["FleetObservabilityMembershipStateIn"])
    types["FleetObservabilityMembershipStateOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["FleetObservabilityMembershipStateOut"])
    types["CommonFleetDefaultMemberConfigSpecIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["CommonFleetDefaultMemberConfigSpecIn"])
    types["CommonFleetDefaultMemberConfigSpecOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CommonFleetDefaultMemberConfigSpecOut"])
    types["IdentityServiceMembershipSpecIn"] = t.struct(
        {
            "authMethods": t.array(
                t.proxy(renames["IdentityServiceAuthMethodIn"])
            ).optional()
        }
    ).named(renames["IdentityServiceMembershipSpecIn"])
    types["IdentityServiceMembershipSpecOut"] = t.struct(
        {
            "authMethods": t.array(
                t.proxy(renames["IdentityServiceAuthMethodOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentityServiceMembershipSpecOut"])
    types["ConnectAgentResourceIn"] = t.struct(
        {
            "type": t.proxy(renames["TypeMetaIn"]).optional(),
            "manifest": t.string().optional(),
        }
    ).named(renames["ConnectAgentResourceIn"])
    types["ConnectAgentResourceOut"] = t.struct(
        {
            "type": t.proxy(renames["TypeMetaOut"]).optional(),
            "manifest": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConnectAgentResourceOut"])
    types["ConfigManagementConfigSyncStateIn"] = t.struct(
        {
            "version": t.proxy(
                renames["ConfigManagementConfigSyncVersionIn"]
            ).optional(),
            "errors": t.array(
                t.proxy(renames["ConfigManagementConfigSyncErrorIn"])
            ).optional(),
            "deploymentState": t.proxy(
                renames["ConfigManagementConfigSyncDeploymentStateIn"]
            ).optional(),
            "syncState": t.proxy(renames["ConfigManagementSyncStateIn"]).optional(),
        }
    ).named(renames["ConfigManagementConfigSyncStateIn"])
    types["ConfigManagementConfigSyncStateOut"] = t.struct(
        {
            "version": t.proxy(
                renames["ConfigManagementConfigSyncVersionOut"]
            ).optional(),
            "errors": t.array(
                t.proxy(renames["ConfigManagementConfigSyncErrorOut"])
            ).optional(),
            "deploymentState": t.proxy(
                renames["ConfigManagementConfigSyncDeploymentStateOut"]
            ).optional(),
            "syncState": t.proxy(renames["ConfigManagementSyncStateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementConfigSyncStateOut"])
    types["IdentityServiceMembershipStateIn"] = t.struct(
        {
            "memberConfig": t.proxy(
                renames["IdentityServiceMembershipSpecIn"]
            ).optional(),
            "failureReason": t.string().optional(),
            "state": t.string().optional(),
            "installedVersion": t.string().optional(),
        }
    ).named(renames["IdentityServiceMembershipStateIn"])
    types["IdentityServiceMembershipStateOut"] = t.struct(
        {
            "memberConfig": t.proxy(
                renames["IdentityServiceMembershipSpecOut"]
            ).optional(),
            "failureReason": t.string().optional(),
            "state": t.string().optional(),
            "installedVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentityServiceMembershipStateOut"])

    functions = {}
    functions["organizationsLocationsFleetsList"] = gkehub.get(
        "v1/{parent}/fleets",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFleetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = gkehub.get(
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
    functions["projectsLocationsList"] = gkehub.get(
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
    functions["projectsLocationsFeaturesTestIamPermissions"] = gkehub.post(
        "v1/{parent}/features",
        t.struct(
            {
                "requestId": t.string().optional(),
                "featureId": t.string().optional(),
                "parent": t.string(),
                "spec": t.proxy(renames["CommonFeatureSpecIn"]).optional(),
                "fleetDefaultMemberConfig": t.proxy(
                    renames["CommonFleetDefaultMemberConfigSpecIn"]
                ).optional(),
                "scopeSpecs": t.struct({"_": t.string().optional()}).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "membershipSpecs": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFeaturesGetIamPolicy"] = gkehub.post(
        "v1/{parent}/features",
        t.struct(
            {
                "requestId": t.string().optional(),
                "featureId": t.string().optional(),
                "parent": t.string(),
                "spec": t.proxy(renames["CommonFeatureSpecIn"]).optional(),
                "fleetDefaultMemberConfig": t.proxy(
                    renames["CommonFleetDefaultMemberConfigSpecIn"]
                ).optional(),
                "scopeSpecs": t.struct({"_": t.string().optional()}).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "membershipSpecs": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFeaturesList"] = gkehub.post(
        "v1/{parent}/features",
        t.struct(
            {
                "requestId": t.string().optional(),
                "featureId": t.string().optional(),
                "parent": t.string(),
                "spec": t.proxy(renames["CommonFeatureSpecIn"]).optional(),
                "fleetDefaultMemberConfig": t.proxy(
                    renames["CommonFleetDefaultMemberConfigSpecIn"]
                ).optional(),
                "scopeSpecs": t.struct({"_": t.string().optional()}).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "membershipSpecs": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFeaturesPatch"] = gkehub.post(
        "v1/{parent}/features",
        t.struct(
            {
                "requestId": t.string().optional(),
                "featureId": t.string().optional(),
                "parent": t.string(),
                "spec": t.proxy(renames["CommonFeatureSpecIn"]).optional(),
                "fleetDefaultMemberConfig": t.proxy(
                    renames["CommonFleetDefaultMemberConfigSpecIn"]
                ).optional(),
                "scopeSpecs": t.struct({"_": t.string().optional()}).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "membershipSpecs": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFeaturesSetIamPolicy"] = gkehub.post(
        "v1/{parent}/features",
        t.struct(
            {
                "requestId": t.string().optional(),
                "featureId": t.string().optional(),
                "parent": t.string(),
                "spec": t.proxy(renames["CommonFeatureSpecIn"]).optional(),
                "fleetDefaultMemberConfig": t.proxy(
                    renames["CommonFleetDefaultMemberConfigSpecIn"]
                ).optional(),
                "scopeSpecs": t.struct({"_": t.string().optional()}).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "membershipSpecs": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFeaturesDelete"] = gkehub.post(
        "v1/{parent}/features",
        t.struct(
            {
                "requestId": t.string().optional(),
                "featureId": t.string().optional(),
                "parent": t.string(),
                "spec": t.proxy(renames["CommonFeatureSpecIn"]).optional(),
                "fleetDefaultMemberConfig": t.proxy(
                    renames["CommonFleetDefaultMemberConfigSpecIn"]
                ).optional(),
                "scopeSpecs": t.struct({"_": t.string().optional()}).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "membershipSpecs": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFeaturesGet"] = gkehub.post(
        "v1/{parent}/features",
        t.struct(
            {
                "requestId": t.string().optional(),
                "featureId": t.string().optional(),
                "parent": t.string(),
                "spec": t.proxy(renames["CommonFeatureSpecIn"]).optional(),
                "fleetDefaultMemberConfig": t.proxy(
                    renames["CommonFleetDefaultMemberConfigSpecIn"]
                ).optional(),
                "scopeSpecs": t.struct({"_": t.string().optional()}).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "membershipSpecs": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFeaturesCreate"] = gkehub.post(
        "v1/{parent}/features",
        t.struct(
            {
                "requestId": t.string().optional(),
                "featureId": t.string().optional(),
                "parent": t.string(),
                "spec": t.proxy(renames["CommonFeatureSpecIn"]).optional(),
                "fleetDefaultMemberConfig": t.proxy(
                    renames["CommonFleetDefaultMemberConfigSpecIn"]
                ).optional(),
                "scopeSpecs": t.struct({"_": t.string().optional()}).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "membershipSpecs": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = gkehub.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = gkehub.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = gkehub.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = gkehub.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsScopesGet"] = gkehub.post(
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
    functions["projectsLocationsScopesList"] = gkehub.post(
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
    functions["projectsLocationsScopesSetIamPolicy"] = gkehub.post(
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
    functions["projectsLocationsScopesDelete"] = gkehub.post(
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
    functions["projectsLocationsScopesCreate"] = gkehub.post(
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
    functions["projectsLocationsScopesPatch"] = gkehub.post(
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
    functions["projectsLocationsScopesGetIamPolicy"] = gkehub.post(
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
    functions["projectsLocationsScopesTestIamPermissions"] = gkehub.post(
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
    functions["projectsLocationsMembershipsDelete"] = gkehub.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMembershipsPatch"] = gkehub.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMembershipsTestIamPermissions"] = gkehub.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMembershipsGet"] = gkehub.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMembershipsSetIamPolicy"] = gkehub.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMembershipsGenerateConnectManifest"] = gkehub.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMembershipsList"] = gkehub.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMembershipsCreate"] = gkehub.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMembershipsGetIamPolicy"] = gkehub.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMembershipsBindingsPatch"] = gkehub.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["MembershipBindingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMembershipsBindingsList"] = gkehub.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["MembershipBindingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMembershipsBindingsDelete"] = gkehub.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["MembershipBindingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMembershipsBindingsCreate"] = gkehub.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["MembershipBindingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMembershipsBindingsGet"] = gkehub.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["MembershipBindingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFleetsCreate"] = gkehub.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFleetsList"] = gkehub.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFleetsGet"] = gkehub.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFleetsPatch"] = gkehub.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFleetsDelete"] = gkehub.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="gkehub", renames=renames, types=Box(types), functions=Box(functions)
    )
