from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_gkehub() -> Import:
    gkehub = HTTPRuntime("https://gkehub.googleapis.com/")

    renames = {
        "ErrorResponse": "_gkehub_1_ErrorResponse",
        "ConfigManagementOciConfigIn": "_gkehub_2_ConfigManagementOciConfigIn",
        "ConfigManagementOciConfigOut": "_gkehub_3_ConfigManagementOciConfigOut",
        "GenerateConnectManifestResponseIn": "_gkehub_4_GenerateConnectManifestResponseIn",
        "GenerateConnectManifestResponseOut": "_gkehub_5_GenerateConnectManifestResponseOut",
        "GkeClusterIn": "_gkehub_6_GkeClusterIn",
        "GkeClusterOut": "_gkehub_7_GkeClusterOut",
        "ConfigManagementErrorResourceIn": "_gkehub_8_ConfigManagementErrorResourceIn",
        "ConfigManagementErrorResourceOut": "_gkehub_9_ConfigManagementErrorResourceOut",
        "AuthorityIn": "_gkehub_10_AuthorityIn",
        "AuthorityOut": "_gkehub_11_AuthorityOut",
        "ConfigManagementOperatorStateIn": "_gkehub_12_ConfigManagementOperatorStateIn",
        "ConfigManagementOperatorStateOut": "_gkehub_13_ConfigManagementOperatorStateOut",
        "MembershipIn": "_gkehub_14_MembershipIn",
        "MembershipOut": "_gkehub_15_MembershipOut",
        "ConfigManagementHierarchyControllerConfigIn": "_gkehub_16_ConfigManagementHierarchyControllerConfigIn",
        "ConfigManagementHierarchyControllerConfigOut": "_gkehub_17_ConfigManagementHierarchyControllerConfigOut",
        "LocationIn": "_gkehub_18_LocationIn",
        "LocationOut": "_gkehub_19_LocationOut",
        "OnPremClusterIn": "_gkehub_20_OnPremClusterIn",
        "OnPremClusterOut": "_gkehub_21_OnPremClusterOut",
        "MonitoringConfigIn": "_gkehub_22_MonitoringConfigIn",
        "MonitoringConfigOut": "_gkehub_23_MonitoringConfigOut",
        "ConfigManagementManagedIn": "_gkehub_24_ConfigManagementManagedIn",
        "ConfigManagementManagedOut": "_gkehub_25_ConfigManagementManagedOut",
        "MembershipEndpointIn": "_gkehub_26_MembershipEndpointIn",
        "MembershipEndpointOut": "_gkehub_27_MembershipEndpointOut",
        "ConfigManagementGroupVersionKindIn": "_gkehub_28_ConfigManagementGroupVersionKindIn",
        "ConfigManagementGroupVersionKindOut": "_gkehub_29_ConfigManagementGroupVersionKindOut",
        "OperationMetadataIn": "_gkehub_30_OperationMetadataIn",
        "OperationMetadataOut": "_gkehub_31_OperationMetadataOut",
        "TestIamPermissionsResponseIn": "_gkehub_32_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_gkehub_33_TestIamPermissionsResponseOut",
        "ServiceMeshMembershipStateIn": "_gkehub_34_ServiceMeshMembershipStateIn",
        "ServiceMeshMembershipStateOut": "_gkehub_35_ServiceMeshMembershipStateOut",
        "KubernetesResourceIn": "_gkehub_36_KubernetesResourceIn",
        "KubernetesResourceOut": "_gkehub_37_KubernetesResourceOut",
        "EdgeClusterIn": "_gkehub_38_EdgeClusterIn",
        "EdgeClusterOut": "_gkehub_39_EdgeClusterOut",
        "ConfigManagementConfigSyncVersionIn": "_gkehub_40_ConfigManagementConfigSyncVersionIn",
        "ConfigManagementConfigSyncVersionOut": "_gkehub_41_ConfigManagementConfigSyncVersionOut",
        "ConfigManagementConfigSyncIn": "_gkehub_42_ConfigManagementConfigSyncIn",
        "ConfigManagementConfigSyncOut": "_gkehub_43_ConfigManagementConfigSyncOut",
        "AuditLogConfigIn": "_gkehub_44_AuditLogConfigIn",
        "AuditLogConfigOut": "_gkehub_45_AuditLogConfigOut",
        "BindingIn": "_gkehub_46_BindingIn",
        "BindingOut": "_gkehub_47_BindingOut",
        "FleetObservabilityMembershipSpecIn": "_gkehub_48_FleetObservabilityMembershipSpecIn",
        "FleetObservabilityMembershipSpecOut": "_gkehub_49_FleetObservabilityMembershipSpecOut",
        "ConfigManagementMembershipStateIn": "_gkehub_50_ConfigManagementMembershipStateIn",
        "ConfigManagementMembershipStateOut": "_gkehub_51_ConfigManagementMembershipStateOut",
        "FeatureIn": "_gkehub_52_FeatureIn",
        "FeatureOut": "_gkehub_53_FeatureOut",
        "OperationIn": "_gkehub_54_OperationIn",
        "OperationOut": "_gkehub_55_OperationOut",
        "EmptyIn": "_gkehub_56_EmptyIn",
        "EmptyOut": "_gkehub_57_EmptyOut",
        "ConfigManagementHierarchyControllerDeploymentStateIn": "_gkehub_58_ConfigManagementHierarchyControllerDeploymentStateIn",
        "ConfigManagementHierarchyControllerDeploymentStateOut": "_gkehub_59_ConfigManagementHierarchyControllerDeploymentStateOut",
        "KubernetesMetadataIn": "_gkehub_60_KubernetesMetadataIn",
        "KubernetesMetadataOut": "_gkehub_61_KubernetesMetadataOut",
        "IdentityServiceGoogleConfigIn": "_gkehub_62_IdentityServiceGoogleConfigIn",
        "IdentityServiceGoogleConfigOut": "_gkehub_63_IdentityServiceGoogleConfigOut",
        "ResourceManifestIn": "_gkehub_64_ResourceManifestIn",
        "ResourceManifestOut": "_gkehub_65_ResourceManifestOut",
        "ListMembershipsResponseIn": "_gkehub_66_ListMembershipsResponseIn",
        "ListMembershipsResponseOut": "_gkehub_67_ListMembershipsResponseOut",
        "ConfigManagementHierarchyControllerVersionIn": "_gkehub_68_ConfigManagementHierarchyControllerVersionIn",
        "ConfigManagementHierarchyControllerVersionOut": "_gkehub_69_ConfigManagementHierarchyControllerVersionOut",
        "ServiceMeshControlPlaneManagementIn": "_gkehub_70_ServiceMeshControlPlaneManagementIn",
        "ServiceMeshControlPlaneManagementOut": "_gkehub_71_ServiceMeshControlPlaneManagementOut",
        "IdentityServiceOidcConfigIn": "_gkehub_72_IdentityServiceOidcConfigIn",
        "IdentityServiceOidcConfigOut": "_gkehub_73_IdentityServiceOidcConfigOut",
        "ConfigManagementHierarchyControllerStateIn": "_gkehub_74_ConfigManagementHierarchyControllerStateIn",
        "ConfigManagementHierarchyControllerStateOut": "_gkehub_75_ConfigManagementHierarchyControllerStateOut",
        "ListLocationsResponseIn": "_gkehub_76_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_gkehub_77_ListLocationsResponseOut",
        "ResourceOptionsIn": "_gkehub_78_ResourceOptionsIn",
        "ResourceOptionsOut": "_gkehub_79_ResourceOptionsOut",
        "ConfigManagementGatekeeperDeploymentStateIn": "_gkehub_80_ConfigManagementGatekeeperDeploymentStateIn",
        "ConfigManagementGatekeeperDeploymentStateOut": "_gkehub_81_ConfigManagementGatekeeperDeploymentStateOut",
        "ConfigManagementPolicyControllerIn": "_gkehub_82_ConfigManagementPolicyControllerIn",
        "ConfigManagementPolicyControllerOut": "_gkehub_83_ConfigManagementPolicyControllerOut",
        "ConfigManagementMembershipSpecIn": "_gkehub_84_ConfigManagementMembershipSpecIn",
        "ConfigManagementMembershipSpecOut": "_gkehub_85_ConfigManagementMembershipSpecOut",
        "ScopeLifecycleStateIn": "_gkehub_86_ScopeLifecycleStateIn",
        "ScopeLifecycleStateOut": "_gkehub_87_ScopeLifecycleStateOut",
        "ConfigManagementPolicyControllerStateIn": "_gkehub_88_ConfigManagementPolicyControllerStateIn",
        "ConfigManagementPolicyControllerStateOut": "_gkehub_89_ConfigManagementPolicyControllerStateOut",
        "CommonFeatureSpecIn": "_gkehub_90_CommonFeatureSpecIn",
        "CommonFeatureSpecOut": "_gkehub_91_CommonFeatureSpecOut",
        "ConnectAgentResourceIn": "_gkehub_92_ConnectAgentResourceIn",
        "ConnectAgentResourceOut": "_gkehub_93_ConnectAgentResourceOut",
        "ConfigManagementSyncErrorIn": "_gkehub_94_ConfigManagementSyncErrorIn",
        "ConfigManagementSyncErrorOut": "_gkehub_95_ConfigManagementSyncErrorOut",
        "ScopeIn": "_gkehub_96_ScopeIn",
        "ScopeOut": "_gkehub_97_ScopeOut",
        "MultiCloudClusterIn": "_gkehub_98_MultiCloudClusterIn",
        "MultiCloudClusterOut": "_gkehub_99_MultiCloudClusterOut",
        "ServiceMeshDataPlaneManagementIn": "_gkehub_100_ServiceMeshDataPlaneManagementIn",
        "ServiceMeshDataPlaneManagementOut": "_gkehub_101_ServiceMeshDataPlaneManagementOut",
        "ScopeFeatureSpecIn": "_gkehub_102_ScopeFeatureSpecIn",
        "ScopeFeatureSpecOut": "_gkehub_103_ScopeFeatureSpecOut",
        "ConfigManagementConfigSyncStateIn": "_gkehub_104_ConfigManagementConfigSyncStateIn",
        "ConfigManagementConfigSyncStateOut": "_gkehub_105_ConfigManagementConfigSyncStateOut",
        "ApplianceClusterIn": "_gkehub_106_ApplianceClusterIn",
        "ApplianceClusterOut": "_gkehub_107_ApplianceClusterOut",
        "CommonFeatureStateIn": "_gkehub_108_CommonFeatureStateIn",
        "CommonFeatureStateOut": "_gkehub_109_CommonFeatureStateOut",
        "GoogleRpcStatusIn": "_gkehub_110_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_gkehub_111_GoogleRpcStatusOut",
        "IdentityServiceMembershipStateIn": "_gkehub_112_IdentityServiceMembershipStateIn",
        "IdentityServiceMembershipStateOut": "_gkehub_113_IdentityServiceMembershipStateOut",
        "ScopeFeatureStateIn": "_gkehub_114_ScopeFeatureStateIn",
        "ScopeFeatureStateOut": "_gkehub_115_ScopeFeatureStateOut",
        "ConfigManagementPolicyControllerMonitoringIn": "_gkehub_116_ConfigManagementPolicyControllerMonitoringIn",
        "ConfigManagementPolicyControllerMonitoringOut": "_gkehub_117_ConfigManagementPolicyControllerMonitoringOut",
        "MultiClusterIngressFeatureSpecIn": "_gkehub_118_MultiClusterIngressFeatureSpecIn",
        "MultiClusterIngressFeatureSpecOut": "_gkehub_119_MultiClusterIngressFeatureSpecOut",
        "ExprIn": "_gkehub_120_ExprIn",
        "ExprOut": "_gkehub_121_ExprOut",
        "MembershipFeatureSpecIn": "_gkehub_122_MembershipFeatureSpecIn",
        "MembershipFeatureSpecOut": "_gkehub_123_MembershipFeatureSpecOut",
        "FleetObservabilityMembershipStateIn": "_gkehub_124_FleetObservabilityMembershipStateIn",
        "FleetObservabilityMembershipStateOut": "_gkehub_125_FleetObservabilityMembershipStateOut",
        "FleetObservabilityFeatureStateIn": "_gkehub_126_FleetObservabilityFeatureStateIn",
        "FleetObservabilityFeatureStateOut": "_gkehub_127_FleetObservabilityFeatureStateOut",
        "ListMembershipBindingsResponseIn": "_gkehub_128_ListMembershipBindingsResponseIn",
        "ListMembershipBindingsResponseOut": "_gkehub_129_ListMembershipBindingsResponseOut",
        "FeatureResourceStateIn": "_gkehub_130_FeatureResourceStateIn",
        "FeatureResourceStateOut": "_gkehub_131_FeatureResourceStateOut",
        "ConfigManagementGitConfigIn": "_gkehub_132_ConfigManagementGitConfigIn",
        "ConfigManagementGitConfigOut": "_gkehub_133_ConfigManagementGitConfigOut",
        "AppDevExperienceFeatureSpecIn": "_gkehub_134_AppDevExperienceFeatureSpecIn",
        "AppDevExperienceFeatureSpecOut": "_gkehub_135_AppDevExperienceFeatureSpecOut",
        "MembershipBindingLifecycleStateIn": "_gkehub_136_MembershipBindingLifecycleStateIn",
        "MembershipBindingLifecycleStateOut": "_gkehub_137_MembershipBindingLifecycleStateOut",
        "SetIamPolicyRequestIn": "_gkehub_138_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_gkehub_139_SetIamPolicyRequestOut",
        "ListOperationsResponseIn": "_gkehub_140_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_gkehub_141_ListOperationsResponseOut",
        "ServiceMeshMembershipSpecIn": "_gkehub_142_ServiceMeshMembershipSpecIn",
        "ServiceMeshMembershipSpecOut": "_gkehub_143_ServiceMeshMembershipSpecOut",
        "ListFeaturesResponseIn": "_gkehub_144_ListFeaturesResponseIn",
        "ListFeaturesResponseOut": "_gkehub_145_ListFeaturesResponseOut",
        "MembershipStateIn": "_gkehub_146_MembershipStateIn",
        "MembershipStateOut": "_gkehub_147_MembershipStateOut",
        "StatusIn": "_gkehub_148_StatusIn",
        "StatusOut": "_gkehub_149_StatusOut",
        "CommonFleetDefaultMemberConfigSpecIn": "_gkehub_150_CommonFleetDefaultMemberConfigSpecIn",
        "CommonFleetDefaultMemberConfigSpecOut": "_gkehub_151_CommonFleetDefaultMemberConfigSpecOut",
        "PolicyIn": "_gkehub_152_PolicyIn",
        "PolicyOut": "_gkehub_153_PolicyOut",
        "IdentityServiceAzureADConfigIn": "_gkehub_154_IdentityServiceAzureADConfigIn",
        "IdentityServiceAzureADConfigOut": "_gkehub_155_IdentityServiceAzureADConfigOut",
        "CancelOperationRequestIn": "_gkehub_156_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_gkehub_157_CancelOperationRequestOut",
        "FleetObservabilityFeatureSpecIn": "_gkehub_158_FleetObservabilityFeatureSpecIn",
        "FleetObservabilityFeatureSpecOut": "_gkehub_159_FleetObservabilityFeatureSpecOut",
        "ConfigManagementInstallErrorIn": "_gkehub_160_ConfigManagementInstallErrorIn",
        "ConfigManagementInstallErrorOut": "_gkehub_161_ConfigManagementInstallErrorOut",
        "AuditConfigIn": "_gkehub_162_AuditConfigIn",
        "AuditConfigOut": "_gkehub_163_AuditConfigOut",
        "ServiceMeshStatusDetailsIn": "_gkehub_164_ServiceMeshStatusDetailsIn",
        "ServiceMeshStatusDetailsOut": "_gkehub_165_ServiceMeshStatusDetailsOut",
        "MembershipFeatureStateIn": "_gkehub_166_MembershipFeatureStateIn",
        "MembershipFeatureStateOut": "_gkehub_167_MembershipFeatureStateOut",
        "ConfigManagementSyncStateIn": "_gkehub_168_ConfigManagementSyncStateIn",
        "ConfigManagementSyncStateOut": "_gkehub_169_ConfigManagementSyncStateOut",
        "IdentityServiceMembershipSpecIn": "_gkehub_170_IdentityServiceMembershipSpecIn",
        "IdentityServiceMembershipSpecOut": "_gkehub_171_IdentityServiceMembershipSpecOut",
        "TestIamPermissionsRequestIn": "_gkehub_172_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_gkehub_173_TestIamPermissionsRequestOut",
        "ListScopesResponseIn": "_gkehub_174_ListScopesResponseIn",
        "ListScopesResponseOut": "_gkehub_175_ListScopesResponseOut",
        "ConfigManagementPolicyControllerMigrationIn": "_gkehub_176_ConfigManagementPolicyControllerMigrationIn",
        "ConfigManagementPolicyControllerMigrationOut": "_gkehub_177_ConfigManagementPolicyControllerMigrationOut",
        "AppDevExperienceFeatureStateIn": "_gkehub_178_AppDevExperienceFeatureStateIn",
        "AppDevExperienceFeatureStateOut": "_gkehub_179_AppDevExperienceFeatureStateOut",
        "MembershipBindingIn": "_gkehub_180_MembershipBindingIn",
        "MembershipBindingOut": "_gkehub_181_MembershipBindingOut",
        "TypeMetaIn": "_gkehub_182_TypeMetaIn",
        "TypeMetaOut": "_gkehub_183_TypeMetaOut",
        "FeatureStateIn": "_gkehub_184_FeatureStateIn",
        "FeatureStateOut": "_gkehub_185_FeatureStateOut",
        "IdentityServiceAuthMethodIn": "_gkehub_186_IdentityServiceAuthMethodIn",
        "IdentityServiceAuthMethodOut": "_gkehub_187_IdentityServiceAuthMethodOut",
        "ConfigManagementConfigSyncDeploymentStateIn": "_gkehub_188_ConfigManagementConfigSyncDeploymentStateIn",
        "ConfigManagementConfigSyncDeploymentStateOut": "_gkehub_189_ConfigManagementConfigSyncDeploymentStateOut",
        "ConfigManagementPolicyControllerVersionIn": "_gkehub_190_ConfigManagementPolicyControllerVersionIn",
        "ConfigManagementPolicyControllerVersionOut": "_gkehub_191_ConfigManagementPolicyControllerVersionOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ConfigManagementOciConfigIn"] = t.struct(
        {
            "policyDir": t.string().optional(),
            "syncRepo": t.string().optional(),
            "gcpServiceAccountEmail": t.string().optional(),
            "syncWaitSecs": t.string().optional(),
            "secretType": t.string().optional(),
        }
    ).named(renames["ConfigManagementOciConfigIn"])
    types["ConfigManagementOciConfigOut"] = t.struct(
        {
            "policyDir": t.string().optional(),
            "syncRepo": t.string().optional(),
            "gcpServiceAccountEmail": t.string().optional(),
            "syncWaitSecs": t.string().optional(),
            "secretType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementOciConfigOut"])
    types["GenerateConnectManifestResponseIn"] = t.struct(
        {"manifest": t.array(t.proxy(renames["ConnectAgentResourceIn"])).optional()}
    ).named(renames["GenerateConnectManifestResponseIn"])
    types["GenerateConnectManifestResponseOut"] = t.struct(
        {
            "manifest": t.array(t.proxy(renames["ConnectAgentResourceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateConnectManifestResponseOut"])
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
    types["ConfigManagementErrorResourceIn"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "resourceGvk": t.proxy(
                renames["ConfigManagementGroupVersionKindIn"]
            ).optional(),
            "resourceNamespace": t.string().optional(),
            "sourcePath": t.string().optional(),
        }
    ).named(renames["ConfigManagementErrorResourceIn"])
    types["ConfigManagementErrorResourceOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "resourceGvk": t.proxy(
                renames["ConfigManagementGroupVersionKindOut"]
            ).optional(),
            "resourceNamespace": t.string().optional(),
            "sourcePath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementErrorResourceOut"])
    types["AuthorityIn"] = t.struct(
        {"oidcJwks": t.string().optional(), "issuer": t.string().optional()}
    ).named(renames["AuthorityIn"])
    types["AuthorityOut"] = t.struct(
        {
            "oidcJwks": t.string().optional(),
            "issuer": t.string().optional(),
            "identityProvider": t.string().optional(),
            "workloadIdentityPool": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthorityOut"])
    types["ConfigManagementOperatorStateIn"] = t.struct(
        {
            "version": t.string().optional(),
            "errors": t.array(
                t.proxy(renames["ConfigManagementInstallErrorIn"])
            ).optional(),
            "deploymentState": t.string().optional(),
        }
    ).named(renames["ConfigManagementOperatorStateIn"])
    types["ConfigManagementOperatorStateOut"] = t.struct(
        {
            "version": t.string().optional(),
            "errors": t.array(
                t.proxy(renames["ConfigManagementInstallErrorOut"])
            ).optional(),
            "deploymentState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementOperatorStateOut"])
    types["MembershipIn"] = t.struct(
        {
            "endpoint": t.proxy(renames["MembershipEndpointIn"]).optional(),
            "monitoringConfig": t.proxy(renames["MonitoringConfigIn"]).optional(),
            "authority": t.proxy(renames["AuthorityIn"]).optional(),
            "externalId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["MembershipIn"])
    types["MembershipOut"] = t.struct(
        {
            "uniqueId": t.string().optional(),
            "lastConnectionTime": t.string().optional(),
            "endpoint": t.proxy(renames["MembershipEndpointOut"]).optional(),
            "monitoringConfig": t.proxy(renames["MonitoringConfigOut"]).optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "deleteTime": t.string().optional(),
            "description": t.string().optional(),
            "state": t.proxy(renames["MembershipStateOut"]).optional(),
            "authority": t.proxy(renames["AuthorityOut"]).optional(),
            "externalId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipOut"])
    types["ConfigManagementHierarchyControllerConfigIn"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "enableHierarchicalResourceQuota": t.boolean().optional(),
            "enablePodTreeLabels": t.boolean().optional(),
        }
    ).named(renames["ConfigManagementHierarchyControllerConfigIn"])
    types["ConfigManagementHierarchyControllerConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "enableHierarchicalResourceQuota": t.boolean().optional(),
            "enablePodTreeLabels": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementHierarchyControllerConfigOut"])
    types["LocationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["OnPremClusterIn"] = t.struct(
        {
            "resourceLink": t.string().optional(),
            "adminCluster": t.boolean().optional(),
            "clusterType": t.string().optional(),
        }
    ).named(renames["OnPremClusterIn"])
    types["OnPremClusterOut"] = t.struct(
        {
            "resourceLink": t.string().optional(),
            "adminCluster": t.boolean().optional(),
            "clusterMissing": t.boolean().optional(),
            "clusterType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OnPremClusterOut"])
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
    types["ConfigManagementManagedIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["ConfigManagementManagedIn"])
    types["ConfigManagementManagedOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementManagedOut"])
    types["MembershipEndpointIn"] = t.struct(
        {
            "gkeCluster": t.proxy(renames["GkeClusterIn"]).optional(),
            "kubernetesResource": t.proxy(renames["KubernetesResourceIn"]).optional(),
            "onPremCluster": t.proxy(renames["OnPremClusterIn"]).optional(),
            "edgeCluster": t.proxy(renames["EdgeClusterIn"]).optional(),
            "multiCloudCluster": t.proxy(renames["MultiCloudClusterIn"]).optional(),
            "applianceCluster": t.proxy(renames["ApplianceClusterIn"]).optional(),
        }
    ).named(renames["MembershipEndpointIn"])
    types["MembershipEndpointOut"] = t.struct(
        {
            "gkeCluster": t.proxy(renames["GkeClusterOut"]).optional(),
            "kubernetesResource": t.proxy(renames["KubernetesResourceOut"]).optional(),
            "googleManaged": t.boolean().optional(),
            "onPremCluster": t.proxy(renames["OnPremClusterOut"]).optional(),
            "edgeCluster": t.proxy(renames["EdgeClusterOut"]).optional(),
            "multiCloudCluster": t.proxy(renames["MultiCloudClusterOut"]).optional(),
            "kubernetesMetadata": t.proxy(renames["KubernetesMetadataOut"]).optional(),
            "applianceCluster": t.proxy(renames["ApplianceClusterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipEndpointOut"])
    types["ConfigManagementGroupVersionKindIn"] = t.struct(
        {
            "version": t.string().optional(),
            "group": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ConfigManagementGroupVersionKindIn"])
    types["ConfigManagementGroupVersionKindOut"] = t.struct(
        {
            "version": t.string().optional(),
            "group": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementGroupVersionKindOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "apiVersion": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "target": t.string().optional(),
            "endTime": t.string().optional(),
            "verb": t.string().optional(),
            "createTime": t.string().optional(),
            "statusDetail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["ServiceMeshMembershipStateIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ServiceMeshMembershipStateIn"])
    types["ServiceMeshMembershipStateOut"] = t.struct(
        {
            "controlPlaneManagement": t.proxy(
                renames["ServiceMeshControlPlaneManagementOut"]
            ).optional(),
            "dataPlaneManagement": t.proxy(
                renames["ServiceMeshDataPlaneManagementOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceMeshMembershipStateOut"])
    types["KubernetesResourceIn"] = t.struct(
        {
            "membershipCrManifest": t.string().optional(),
            "resourceOptions": t.proxy(renames["ResourceOptionsIn"]).optional(),
        }
    ).named(renames["KubernetesResourceIn"])
    types["KubernetesResourceOut"] = t.struct(
        {
            "membershipResources": t.array(
                t.proxy(renames["ResourceManifestOut"])
            ).optional(),
            "membershipCrManifest": t.string().optional(),
            "connectResources": t.array(
                t.proxy(renames["ResourceManifestOut"])
            ).optional(),
            "resourceOptions": t.proxy(renames["ResourceOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KubernetesResourceOut"])
    types["EdgeClusterIn"] = t.struct({"resourceLink": t.string().optional()}).named(
        renames["EdgeClusterIn"]
    )
    types["EdgeClusterOut"] = t.struct(
        {
            "resourceLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EdgeClusterOut"])
    types["ConfigManagementConfigSyncVersionIn"] = t.struct(
        {
            "reconcilerManager": t.string().optional(),
            "monitor": t.string().optional(),
            "importer": t.string().optional(),
            "rootReconciler": t.string().optional(),
            "admissionWebhook": t.string().optional(),
            "gitSync": t.string().optional(),
            "syncer": t.string().optional(),
        }
    ).named(renames["ConfigManagementConfigSyncVersionIn"])
    types["ConfigManagementConfigSyncVersionOut"] = t.struct(
        {
            "reconcilerManager": t.string().optional(),
            "monitor": t.string().optional(),
            "importer": t.string().optional(),
            "rootReconciler": t.string().optional(),
            "admissionWebhook": t.string().optional(),
            "gitSync": t.string().optional(),
            "syncer": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementConfigSyncVersionOut"])
    types["ConfigManagementConfigSyncIn"] = t.struct(
        {
            "preventDrift": t.boolean().optional(),
            "git": t.proxy(renames["ConfigManagementGitConfigIn"]).optional(),
            "managed": t.proxy(renames["ConfigManagementManagedIn"]).optional(),
            "enabled": t.boolean().optional(),
            "allowVerticalScale": t.boolean().optional(),
            "sourceFormat": t.string().optional(),
            "oci": t.proxy(renames["ConfigManagementOciConfigIn"]).optional(),
        }
    ).named(renames["ConfigManagementConfigSyncIn"])
    types["ConfigManagementConfigSyncOut"] = t.struct(
        {
            "preventDrift": t.boolean().optional(),
            "git": t.proxy(renames["ConfigManagementGitConfigOut"]).optional(),
            "managed": t.proxy(renames["ConfigManagementManagedOut"]).optional(),
            "enabled": t.boolean().optional(),
            "allowVerticalScale": t.boolean().optional(),
            "sourceFormat": t.string().optional(),
            "oci": t.proxy(renames["ConfigManagementOciConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementConfigSyncOut"])
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
    types["BindingIn"] = t.struct(
        {
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["FleetObservabilityMembershipSpecIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["FleetObservabilityMembershipSpecIn"])
    types["FleetObservabilityMembershipSpecOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["FleetObservabilityMembershipSpecOut"])
    types["ConfigManagementMembershipStateIn"] = t.struct(
        {
            "clusterName": t.string().optional(),
            "policyControllerState": t.proxy(
                renames["ConfigManagementPolicyControllerStateIn"]
            ).optional(),
            "configSyncState": t.proxy(
                renames["ConfigManagementConfigSyncStateIn"]
            ).optional(),
            "operatorState": t.proxy(
                renames["ConfigManagementOperatorStateIn"]
            ).optional(),
            "hierarchyControllerState": t.proxy(
                renames["ConfigManagementHierarchyControllerStateIn"]
            ).optional(),
            "membershipSpec": t.proxy(
                renames["ConfigManagementMembershipSpecIn"]
            ).optional(),
        }
    ).named(renames["ConfigManagementMembershipStateIn"])
    types["ConfigManagementMembershipStateOut"] = t.struct(
        {
            "clusterName": t.string().optional(),
            "policyControllerState": t.proxy(
                renames["ConfigManagementPolicyControllerStateOut"]
            ).optional(),
            "configSyncState": t.proxy(
                renames["ConfigManagementConfigSyncStateOut"]
            ).optional(),
            "operatorState": t.proxy(
                renames["ConfigManagementOperatorStateOut"]
            ).optional(),
            "hierarchyControllerState": t.proxy(
                renames["ConfigManagementHierarchyControllerStateOut"]
            ).optional(),
            "membershipSpec": t.proxy(
                renames["ConfigManagementMembershipSpecOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementMembershipStateOut"])
    types["FeatureIn"] = t.struct(
        {
            "fleetDefaultMemberConfig": t.proxy(
                renames["CommonFleetDefaultMemberConfigSpecIn"]
            ).optional(),
            "spec": t.proxy(renames["CommonFeatureSpecIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "membershipSpecs": t.struct({"_": t.string().optional()}).optional(),
            "scopeSpecs": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["FeatureIn"])
    types["FeatureOut"] = t.struct(
        {
            "deleteTime": t.string().optional(),
            "fleetDefaultMemberConfig": t.proxy(
                renames["CommonFleetDefaultMemberConfigSpecOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "spec": t.proxy(renames["CommonFeatureSpecOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "membershipSpecs": t.struct({"_": t.string().optional()}).optional(),
            "state": t.proxy(renames["CommonFeatureStateOut"]).optional(),
            "updateTime": t.string().optional(),
            "membershipStates": t.struct({"_": t.string().optional()}).optional(),
            "resourceState": t.proxy(renames["FeatureResourceStateOut"]).optional(),
            "scopeStates": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "scopeSpecs": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FeatureOut"])
    types["OperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["KubernetesMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["KubernetesMetadataIn"]
    )
    types["KubernetesMetadataOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "vcpuCount": t.integer().optional(),
            "nodeCount": t.integer().optional(),
            "memoryMb": t.integer().optional(),
            "kubernetesApiServerVersion": t.string().optional(),
            "nodeProviderId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KubernetesMetadataOut"])
    types["IdentityServiceGoogleConfigIn"] = t.struct(
        {"disable": t.boolean().optional()}
    ).named(renames["IdentityServiceGoogleConfigIn"])
    types["IdentityServiceGoogleConfigOut"] = t.struct(
        {
            "disable": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentityServiceGoogleConfigOut"])
    types["ResourceManifestIn"] = t.struct(
        {"manifest": t.string().optional(), "clusterScoped": t.boolean().optional()}
    ).named(renames["ResourceManifestIn"])
    types["ResourceManifestOut"] = t.struct(
        {
            "manifest": t.string().optional(),
            "clusterScoped": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceManifestOut"])
    types["ListMembershipsResponseIn"] = t.struct(
        {
            "resources": t.array(t.proxy(renames["MembershipIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListMembershipsResponseIn"])
    types["ListMembershipsResponseOut"] = t.struct(
        {
            "resources": t.array(t.proxy(renames["MembershipOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListMembershipsResponseOut"])
    types["ConfigManagementHierarchyControllerVersionIn"] = t.struct(
        {"hnc": t.string().optional(), "extension": t.string().optional()}
    ).named(renames["ConfigManagementHierarchyControllerVersionIn"])
    types["ConfigManagementHierarchyControllerVersionOut"] = t.struct(
        {
            "hnc": t.string().optional(),
            "extension": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementHierarchyControllerVersionOut"])
    types["ServiceMeshControlPlaneManagementIn"] = t.struct(
        {
            "details": t.array(
                t.proxy(renames["ServiceMeshStatusDetailsIn"])
            ).optional(),
            "state": t.string().optional(),
        }
    ).named(renames["ServiceMeshControlPlaneManagementIn"])
    types["ServiceMeshControlPlaneManagementOut"] = t.struct(
        {
            "details": t.array(
                t.proxy(renames["ServiceMeshStatusDetailsOut"])
            ).optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceMeshControlPlaneManagementOut"])
    types["IdentityServiceOidcConfigIn"] = t.struct(
        {
            "certificateAuthorityData": t.string().optional(),
            "extraParams": t.string().optional(),
            "enableAccessToken": t.boolean().optional(),
            "groupsClaim": t.string().optional(),
            "userClaim": t.string().optional(),
            "deployCloudConsoleProxy": t.boolean().optional(),
            "issuerUri": t.string().optional(),
            "clientSecret": t.string().optional(),
            "userPrefix": t.string().optional(),
            "kubectlRedirectUri": t.string().optional(),
            "clientId": t.string().optional(),
            "groupPrefix": t.string().optional(),
            "scopes": t.string().optional(),
        }
    ).named(renames["IdentityServiceOidcConfigIn"])
    types["IdentityServiceOidcConfigOut"] = t.struct(
        {
            "certificateAuthorityData": t.string().optional(),
            "extraParams": t.string().optional(),
            "enableAccessToken": t.boolean().optional(),
            "groupsClaim": t.string().optional(),
            "userClaim": t.string().optional(),
            "encryptedClientSecret": t.string().optional(),
            "deployCloudConsoleProxy": t.boolean().optional(),
            "issuerUri": t.string().optional(),
            "clientSecret": t.string().optional(),
            "userPrefix": t.string().optional(),
            "kubectlRedirectUri": t.string().optional(),
            "clientId": t.string().optional(),
            "groupPrefix": t.string().optional(),
            "scopes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentityServiceOidcConfigOut"])
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
    types["ResourceOptionsIn"] = t.struct(
        {
            "k8sVersion": t.string().optional(),
            "v1beta1Crd": t.boolean().optional(),
            "connectVersion": t.string().optional(),
        }
    ).named(renames["ResourceOptionsIn"])
    types["ResourceOptionsOut"] = t.struct(
        {
            "k8sVersion": t.string().optional(),
            "v1beta1Crd": t.boolean().optional(),
            "connectVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceOptionsOut"])
    types["ConfigManagementGatekeeperDeploymentStateIn"] = t.struct(
        {
            "gatekeeperControllerManagerState": t.string().optional(),
            "gatekeeperAudit": t.string().optional(),
            "gatekeeperMutation": t.string().optional(),
        }
    ).named(renames["ConfigManagementGatekeeperDeploymentStateIn"])
    types["ConfigManagementGatekeeperDeploymentStateOut"] = t.struct(
        {
            "gatekeeperControllerManagerState": t.string().optional(),
            "gatekeeperAudit": t.string().optional(),
            "gatekeeperMutation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementGatekeeperDeploymentStateOut"])
    types["ConfigManagementPolicyControllerIn"] = t.struct(
        {
            "templateLibraryInstalled": t.boolean().optional(),
            "enabled": t.boolean().optional(),
            "monitoring": t.proxy(
                renames["ConfigManagementPolicyControllerMonitoringIn"]
            ).optional(),
            "logDeniesEnabled": t.boolean().optional(),
            "mutationEnabled": t.boolean().optional(),
            "auditIntervalSeconds": t.string().optional(),
            "referentialRulesEnabled": t.boolean().optional(),
            "exemptableNamespaces": t.array(t.string()).optional(),
        }
    ).named(renames["ConfigManagementPolicyControllerIn"])
    types["ConfigManagementPolicyControllerOut"] = t.struct(
        {
            "templateLibraryInstalled": t.boolean().optional(),
            "enabled": t.boolean().optional(),
            "monitoring": t.proxy(
                renames["ConfigManagementPolicyControllerMonitoringOut"]
            ).optional(),
            "logDeniesEnabled": t.boolean().optional(),
            "mutationEnabled": t.boolean().optional(),
            "auditIntervalSeconds": t.string().optional(),
            "referentialRulesEnabled": t.boolean().optional(),
            "exemptableNamespaces": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementPolicyControllerOut"])
    types["ConfigManagementMembershipSpecIn"] = t.struct(
        {
            "configSync": t.proxy(renames["ConfigManagementConfigSyncIn"]).optional(),
            "policyController": t.proxy(
                renames["ConfigManagementPolicyControllerIn"]
            ).optional(),
            "version": t.string().optional(),
            "hierarchyController": t.proxy(
                renames["ConfigManagementHierarchyControllerConfigIn"]
            ).optional(),
        }
    ).named(renames["ConfigManagementMembershipSpecIn"])
    types["ConfigManagementMembershipSpecOut"] = t.struct(
        {
            "configSync": t.proxy(renames["ConfigManagementConfigSyncOut"]).optional(),
            "policyController": t.proxy(
                renames["ConfigManagementPolicyControllerOut"]
            ).optional(),
            "version": t.string().optional(),
            "hierarchyController": t.proxy(
                renames["ConfigManagementHierarchyControllerConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementMembershipSpecOut"])
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
            "deploymentState": t.proxy(
                renames["ConfigManagementGatekeeperDeploymentStateIn"]
            ).optional(),
            "migration": t.proxy(
                renames["ConfigManagementPolicyControllerMigrationIn"]
            ).optional(),
        }
    ).named(renames["ConfigManagementPolicyControllerStateIn"])
    types["ConfigManagementPolicyControllerStateOut"] = t.struct(
        {
            "version": t.proxy(
                renames["ConfigManagementPolicyControllerVersionOut"]
            ).optional(),
            "deploymentState": t.proxy(
                renames["ConfigManagementGatekeeperDeploymentStateOut"]
            ).optional(),
            "migration": t.proxy(
                renames["ConfigManagementPolicyControllerMigrationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementPolicyControllerStateOut"])
    types["CommonFeatureSpecIn"] = t.struct(
        {
            "fleetobservability": t.proxy(
                renames["FleetObservabilityFeatureSpecIn"]
            ).optional(),
            "appdevexperience": t.proxy(
                renames["AppDevExperienceFeatureSpecIn"]
            ).optional(),
            "multiclusteringress": t.proxy(
                renames["MultiClusterIngressFeatureSpecIn"]
            ).optional(),
        }
    ).named(renames["CommonFeatureSpecIn"])
    types["CommonFeatureSpecOut"] = t.struct(
        {
            "fleetobservability": t.proxy(
                renames["FleetObservabilityFeatureSpecOut"]
            ).optional(),
            "appdevexperience": t.proxy(
                renames["AppDevExperienceFeatureSpecOut"]
            ).optional(),
            "multiclusteringress": t.proxy(
                renames["MultiClusterIngressFeatureSpecOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommonFeatureSpecOut"])
    types["ConnectAgentResourceIn"] = t.struct(
        {
            "manifest": t.string().optional(),
            "type": t.proxy(renames["TypeMetaIn"]).optional(),
        }
    ).named(renames["ConnectAgentResourceIn"])
    types["ConnectAgentResourceOut"] = t.struct(
        {
            "manifest": t.string().optional(),
            "type": t.proxy(renames["TypeMetaOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConnectAgentResourceOut"])
    types["ConfigManagementSyncErrorIn"] = t.struct(
        {
            "errorResources": t.array(
                t.proxy(renames["ConfigManagementErrorResourceIn"])
            ).optional(),
            "code": t.string().optional(),
            "errorMessage": t.string().optional(),
        }
    ).named(renames["ConfigManagementSyncErrorIn"])
    types["ConfigManagementSyncErrorOut"] = t.struct(
        {
            "errorResources": t.array(
                t.proxy(renames["ConfigManagementErrorResourceOut"])
            ).optional(),
            "code": t.string().optional(),
            "errorMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementSyncErrorOut"])
    types["ScopeIn"] = t.struct(
        {"allMemberships": t.boolean().optional(), "name": t.string().optional()}
    ).named(renames["ScopeIn"])
    types["ScopeOut"] = t.struct(
        {
            "allMemberships": t.boolean().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "deleteTime": t.string().optional(),
            "uid": t.string().optional(),
            "state": t.proxy(renames["ScopeLifecycleStateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScopeOut"])
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
    types["ScopeFeatureSpecIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ScopeFeatureSpecIn"]
    )
    types["ScopeFeatureSpecOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ScopeFeatureSpecOut"])
    types["ConfigManagementConfigSyncStateIn"] = t.struct(
        {
            "version": t.proxy(
                renames["ConfigManagementConfigSyncVersionIn"]
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
            "deploymentState": t.proxy(
                renames["ConfigManagementConfigSyncDeploymentStateOut"]
            ).optional(),
            "syncState": t.proxy(renames["ConfigManagementSyncStateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementConfigSyncStateOut"])
    types["ApplianceClusterIn"] = t.struct(
        {"resourceLink": t.string().optional()}
    ).named(renames["ApplianceClusterIn"])
    types["ApplianceClusterOut"] = t.struct(
        {
            "resourceLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplianceClusterOut"])
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
            "state": t.proxy(renames["FeatureStateOut"]).optional(),
            "fleetobservability": t.proxy(
                renames["FleetObservabilityFeatureStateOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommonFeatureStateOut"])
    types["GoogleRpcStatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["GoogleRpcStatusIn"])
    types["GoogleRpcStatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleRpcStatusOut"])
    types["IdentityServiceMembershipStateIn"] = t.struct(
        {
            "memberConfig": t.proxy(
                renames["IdentityServiceMembershipSpecIn"]
            ).optional(),
            "state": t.string().optional(),
            "installedVersion": t.string().optional(),
            "failureReason": t.string().optional(),
        }
    ).named(renames["IdentityServiceMembershipStateIn"])
    types["IdentityServiceMembershipStateOut"] = t.struct(
        {
            "memberConfig": t.proxy(
                renames["IdentityServiceMembershipSpecOut"]
            ).optional(),
            "state": t.string().optional(),
            "installedVersion": t.string().optional(),
            "failureReason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentityServiceMembershipStateOut"])
    types["ScopeFeatureStateIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ScopeFeatureStateIn"]
    )
    types["ScopeFeatureStateOut"] = t.struct(
        {
            "state": t.proxy(renames["FeatureStateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScopeFeatureStateOut"])
    types["ConfigManagementPolicyControllerMonitoringIn"] = t.struct(
        {"backends": t.array(t.string()).optional()}
    ).named(renames["ConfigManagementPolicyControllerMonitoringIn"])
    types["ConfigManagementPolicyControllerMonitoringOut"] = t.struct(
        {
            "backends": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementPolicyControllerMonitoringOut"])
    types["MultiClusterIngressFeatureSpecIn"] = t.struct(
        {"configMembership": t.string().optional()}
    ).named(renames["MultiClusterIngressFeatureSpecIn"])
    types["MultiClusterIngressFeatureSpecOut"] = t.struct(
        {
            "configMembership": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MultiClusterIngressFeatureSpecOut"])
    types["ExprIn"] = t.struct(
        {
            "title": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "title": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["MembershipFeatureSpecIn"] = t.struct(
        {
            "identityservice": t.proxy(
                renames["IdentityServiceMembershipSpecIn"]
            ).optional(),
            "configmanagement": t.proxy(
                renames["ConfigManagementMembershipSpecIn"]
            ).optional(),
            "mesh": t.proxy(renames["ServiceMeshMembershipSpecIn"]).optional(),
            "fleetInherited": t.boolean().optional(),
            "fleetobservability": t.proxy(
                renames["FleetObservabilityMembershipSpecIn"]
            ).optional(),
        }
    ).named(renames["MembershipFeatureSpecIn"])
    types["MembershipFeatureSpecOut"] = t.struct(
        {
            "identityservice": t.proxy(
                renames["IdentityServiceMembershipSpecOut"]
            ).optional(),
            "configmanagement": t.proxy(
                renames["ConfigManagementMembershipSpecOut"]
            ).optional(),
            "mesh": t.proxy(renames["ServiceMeshMembershipSpecOut"]).optional(),
            "fleetInherited": t.boolean().optional(),
            "fleetobservability": t.proxy(
                renames["FleetObservabilityMembershipSpecOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipFeatureSpecOut"])
    types["FleetObservabilityMembershipStateIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["FleetObservabilityMembershipStateIn"])
    types["FleetObservabilityMembershipStateOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["FleetObservabilityMembershipStateOut"])
    types["FleetObservabilityFeatureStateIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["FleetObservabilityFeatureStateIn"])
    types["FleetObservabilityFeatureStateOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["FleetObservabilityFeatureStateOut"])
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
    types["FeatureResourceStateIn"] = t.struct({"state": t.string().optional()}).named(
        renames["FeatureResourceStateIn"]
    )
    types["FeatureResourceStateOut"] = t.struct(
        {
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FeatureResourceStateOut"])
    types["ConfigManagementGitConfigIn"] = t.struct(
        {
            "gcpServiceAccountEmail": t.string().optional(),
            "httpsProxy": t.string().optional(),
            "policyDir": t.string().optional(),
            "syncWaitSecs": t.string().optional(),
            "syncRev": t.string().optional(),
            "syncBranch": t.string().optional(),
            "secretType": t.string().optional(),
            "syncRepo": t.string().optional(),
        }
    ).named(renames["ConfigManagementGitConfigIn"])
    types["ConfigManagementGitConfigOut"] = t.struct(
        {
            "gcpServiceAccountEmail": t.string().optional(),
            "httpsProxy": t.string().optional(),
            "policyDir": t.string().optional(),
            "syncWaitSecs": t.string().optional(),
            "syncRev": t.string().optional(),
            "syncBranch": t.string().optional(),
            "secretType": t.string().optional(),
            "syncRepo": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementGitConfigOut"])
    types["AppDevExperienceFeatureSpecIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AppDevExperienceFeatureSpecIn"])
    types["AppDevExperienceFeatureSpecOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AppDevExperienceFeatureSpecOut"])
    types["MembershipBindingLifecycleStateIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["MembershipBindingLifecycleStateIn"])
    types["MembershipBindingLifecycleStateOut"] = t.struct(
        {
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipBindingLifecycleStateOut"])
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
    types["ListFeaturesResponseIn"] = t.struct(
        {
            "resources": t.array(t.proxy(renames["FeatureIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListFeaturesResponseIn"])
    types["ListFeaturesResponseOut"] = t.struct(
        {
            "resources": t.array(t.proxy(renames["FeatureOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListFeaturesResponseOut"])
    types["MembershipStateIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MembershipStateIn"]
    )
    types["MembershipStateOut"] = t.struct(
        {
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipStateOut"])
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
    types["CommonFleetDefaultMemberConfigSpecIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["CommonFleetDefaultMemberConfigSpecIn"])
    types["CommonFleetDefaultMemberConfigSpecOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CommonFleetDefaultMemberConfigSpecOut"])
    types["PolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["IdentityServiceAzureADConfigIn"] = t.struct(
        {
            "clientId": t.string().optional(),
            "clientSecret": t.string().optional(),
            "kubectlRedirectUri": t.string().optional(),
            "tenant": t.string().optional(),
        }
    ).named(renames["IdentityServiceAzureADConfigIn"])
    types["IdentityServiceAzureADConfigOut"] = t.struct(
        {
            "clientId": t.string().optional(),
            "clientSecret": t.string().optional(),
            "encryptedClientSecret": t.string().optional(),
            "kubectlRedirectUri": t.string().optional(),
            "tenant": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentityServiceAzureADConfigOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["FleetObservabilityFeatureSpecIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["FleetObservabilityFeatureSpecIn"])
    types["FleetObservabilityFeatureSpecOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["FleetObservabilityFeatureSpecOut"])
    types["ConfigManagementInstallErrorIn"] = t.struct(
        {"errorMessage": t.string().optional()}
    ).named(renames["ConfigManagementInstallErrorIn"])
    types["ConfigManagementInstallErrorOut"] = t.struct(
        {
            "errorMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementInstallErrorOut"])
    types["AuditConfigIn"] = t.struct(
        {
            "auditLogConfigs": t.array(t.proxy(renames["AuditLogConfigIn"])).optional(),
            "service": t.string().optional(),
        }
    ).named(renames["AuditConfigIn"])
    types["AuditConfigOut"] = t.struct(
        {
            "auditLogConfigs": t.array(
                t.proxy(renames["AuditLogConfigOut"])
            ).optional(),
            "service": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditConfigOut"])
    types["ServiceMeshStatusDetailsIn"] = t.struct(
        {"details": t.string().optional(), "code": t.string().optional()}
    ).named(renames["ServiceMeshStatusDetailsIn"])
    types["ServiceMeshStatusDetailsOut"] = t.struct(
        {
            "details": t.string().optional(),
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceMeshStatusDetailsOut"])
    types["MembershipFeatureStateIn"] = t.struct(
        {
            "fleetobservability": t.proxy(
                renames["FleetObservabilityMembershipStateIn"]
            ).optional(),
            "identityservice": t.proxy(
                renames["IdentityServiceMembershipStateIn"]
            ).optional(),
            "state": t.proxy(renames["FeatureStateIn"]).optional(),
            "servicemesh": t.proxy(renames["ServiceMeshMembershipStateIn"]).optional(),
            "appdevexperience": t.proxy(
                renames["AppDevExperienceFeatureStateIn"]
            ).optional(),
            "configmanagement": t.proxy(
                renames["ConfigManagementMembershipStateIn"]
            ).optional(),
        }
    ).named(renames["MembershipFeatureStateIn"])
    types["MembershipFeatureStateOut"] = t.struct(
        {
            "fleetobservability": t.proxy(
                renames["FleetObservabilityMembershipStateOut"]
            ).optional(),
            "identityservice": t.proxy(
                renames["IdentityServiceMembershipStateOut"]
            ).optional(),
            "state": t.proxy(renames["FeatureStateOut"]).optional(),
            "servicemesh": t.proxy(renames["ServiceMeshMembershipStateOut"]).optional(),
            "appdevexperience": t.proxy(
                renames["AppDevExperienceFeatureStateOut"]
            ).optional(),
            "configmanagement": t.proxy(
                renames["ConfigManagementMembershipStateOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipFeatureStateOut"])
    types["ConfigManagementSyncStateIn"] = t.struct(
        {
            "code": t.string().optional(),
            "sourceToken": t.string().optional(),
            "lastSync": t.string().optional(),
            "lastSyncTime": t.string().optional(),
            "errors": t.array(
                t.proxy(renames["ConfigManagementSyncErrorIn"])
            ).optional(),
            "syncToken": t.string().optional(),
            "importToken": t.string().optional(),
        }
    ).named(renames["ConfigManagementSyncStateIn"])
    types["ConfigManagementSyncStateOut"] = t.struct(
        {
            "code": t.string().optional(),
            "sourceToken": t.string().optional(),
            "lastSync": t.string().optional(),
            "lastSyncTime": t.string().optional(),
            "errors": t.array(
                t.proxy(renames["ConfigManagementSyncErrorOut"])
            ).optional(),
            "syncToken": t.string().optional(),
            "importToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementSyncStateOut"])
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
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
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
    types["ConfigManagementPolicyControllerMigrationIn"] = t.struct(
        {"stage": t.string().optional()}
    ).named(renames["ConfigManagementPolicyControllerMigrationIn"])
    types["ConfigManagementPolicyControllerMigrationOut"] = t.struct(
        {
            "stage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementPolicyControllerMigrationOut"])
    types["AppDevExperienceFeatureStateIn"] = t.struct(
        {"networkingInstallSucceeded": t.proxy(renames["StatusIn"]).optional()}
    ).named(renames["AppDevExperienceFeatureStateIn"])
    types["AppDevExperienceFeatureStateOut"] = t.struct(
        {
            "networkingInstallSucceeded": t.proxy(renames["StatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppDevExperienceFeatureStateOut"])
    types["MembershipBindingIn"] = t.struct(
        {
            "scope": t.string().optional(),
            "name": t.string().optional(),
            "fleet": t.boolean().optional(),
        }
    ).named(renames["MembershipBindingIn"])
    types["MembershipBindingOut"] = t.struct(
        {
            "scope": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "fleet": t.boolean().optional(),
            "createTime": t.string().optional(),
            "deleteTime": t.string().optional(),
            "state": t.proxy(renames["MembershipBindingLifecycleStateOut"]).optional(),
            "uid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipBindingOut"])
    types["TypeMetaIn"] = t.struct(
        {"apiVersion": t.string().optional(), "kind": t.string().optional()}
    ).named(renames["TypeMetaIn"])
    types["TypeMetaOut"] = t.struct(
        {
            "apiVersion": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TypeMetaOut"])
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
    types["IdentityServiceAuthMethodIn"] = t.struct(
        {
            "proxy": t.string().optional(),
            "oidcConfig": t.proxy(renames["IdentityServiceOidcConfigIn"]).optional(),
            "googleConfig": t.proxy(
                renames["IdentityServiceGoogleConfigIn"]
            ).optional(),
            "name": t.string().optional(),
            "azureadConfig": t.proxy(
                renames["IdentityServiceAzureADConfigIn"]
            ).optional(),
        }
    ).named(renames["IdentityServiceAuthMethodIn"])
    types["IdentityServiceAuthMethodOut"] = t.struct(
        {
            "proxy": t.string().optional(),
            "oidcConfig": t.proxy(renames["IdentityServiceOidcConfigOut"]).optional(),
            "googleConfig": t.proxy(
                renames["IdentityServiceGoogleConfigOut"]
            ).optional(),
            "name": t.string().optional(),
            "azureadConfig": t.proxy(
                renames["IdentityServiceAzureADConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentityServiceAuthMethodOut"])
    types["ConfigManagementConfigSyncDeploymentStateIn"] = t.struct(
        {
            "importer": t.string().optional(),
            "monitor": t.string().optional(),
            "gitSync": t.string().optional(),
            "rootReconciler": t.string().optional(),
            "admissionWebhook": t.string().optional(),
            "reconcilerManager": t.string().optional(),
            "syncer": t.string().optional(),
        }
    ).named(renames["ConfigManagementConfigSyncDeploymentStateIn"])
    types["ConfigManagementConfigSyncDeploymentStateOut"] = t.struct(
        {
            "importer": t.string().optional(),
            "monitor": t.string().optional(),
            "gitSync": t.string().optional(),
            "rootReconciler": t.string().optional(),
            "admissionWebhook": t.string().optional(),
            "reconcilerManager": t.string().optional(),
            "syncer": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementConfigSyncDeploymentStateOut"])
    types["ConfigManagementPolicyControllerVersionIn"] = t.struct(
        {"version": t.string().optional()}
    ).named(renames["ConfigManagementPolicyControllerVersionIn"])
    types["ConfigManagementPolicyControllerVersionOut"] = t.struct(
        {
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementPolicyControllerVersionOut"])

    functions = {}
    functions["projectsLocationsGet"] = gkehub.get(
        "v1/{name}/locations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
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
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMembershipsSetIamPolicy"] = gkehub.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "requestId": t.string().optional(),
                "endpoint": t.proxy(renames["MembershipEndpointIn"]).optional(),
                "monitoringConfig": t.proxy(renames["MonitoringConfigIn"]).optional(),
                "authority": t.proxy(renames["AuthorityIn"]).optional(),
                "externalId": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMembershipsGetIamPolicy"] = gkehub.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "requestId": t.string().optional(),
                "endpoint": t.proxy(renames["MembershipEndpointIn"]).optional(),
                "monitoringConfig": t.proxy(renames["MonitoringConfigIn"]).optional(),
                "authority": t.proxy(renames["AuthorityIn"]).optional(),
                "externalId": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMembershipsGet"] = gkehub.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "requestId": t.string().optional(),
                "endpoint": t.proxy(renames["MembershipEndpointIn"]).optional(),
                "monitoringConfig": t.proxy(renames["MonitoringConfigIn"]).optional(),
                "authority": t.proxy(renames["AuthorityIn"]).optional(),
                "externalId": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMembershipsTestIamPermissions"] = gkehub.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "requestId": t.string().optional(),
                "endpoint": t.proxy(renames["MembershipEndpointIn"]).optional(),
                "monitoringConfig": t.proxy(renames["MonitoringConfigIn"]).optional(),
                "authority": t.proxy(renames["AuthorityIn"]).optional(),
                "externalId": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMembershipsCreate"] = gkehub.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "requestId": t.string().optional(),
                "endpoint": t.proxy(renames["MembershipEndpointIn"]).optional(),
                "monitoringConfig": t.proxy(renames["MonitoringConfigIn"]).optional(),
                "authority": t.proxy(renames["AuthorityIn"]).optional(),
                "externalId": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMembershipsGenerateConnectManifest"] = gkehub.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "requestId": t.string().optional(),
                "endpoint": t.proxy(renames["MembershipEndpointIn"]).optional(),
                "monitoringConfig": t.proxy(renames["MonitoringConfigIn"]).optional(),
                "authority": t.proxy(renames["AuthorityIn"]).optional(),
                "externalId": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMembershipsList"] = gkehub.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "requestId": t.string().optional(),
                "endpoint": t.proxy(renames["MembershipEndpointIn"]).optional(),
                "monitoringConfig": t.proxy(renames["MonitoringConfigIn"]).optional(),
                "authority": t.proxy(renames["AuthorityIn"]).optional(),
                "externalId": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMembershipsDelete"] = gkehub.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "requestId": t.string().optional(),
                "endpoint": t.proxy(renames["MembershipEndpointIn"]).optional(),
                "monitoringConfig": t.proxy(renames["MonitoringConfigIn"]).optional(),
                "authority": t.proxy(renames["AuthorityIn"]).optional(),
                "externalId": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMembershipsPatch"] = gkehub.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "requestId": t.string().optional(),
                "endpoint": t.proxy(renames["MembershipEndpointIn"]).optional(),
                "monitoringConfig": t.proxy(renames["MonitoringConfigIn"]).optional(),
                "authority": t.proxy(renames["AuthorityIn"]).optional(),
                "externalId": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
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
    functions["projectsLocationsMembershipsBindingsList"] = gkehub.get(
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
    functions["projectsLocationsOperationsCancel"] = gkehub.delete(
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
    functions["projectsLocationsOperationsGet"] = gkehub.delete(
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
    functions["projectsLocationsScopesGet"] = gkehub.get(
        "v1/{parent}/scopes",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListScopesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsScopesDelete"] = gkehub.get(
        "v1/{parent}/scopes",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListScopesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsScopesCreate"] = gkehub.get(
        "v1/{parent}/scopes",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListScopesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsScopesList"] = gkehub.get(
        "v1/{parent}/scopes",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListScopesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFeaturesSetIamPolicy"] = gkehub.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "requestId": t.string().optional(),
                "name": t.string(),
                "fleetDefaultMemberConfig": t.proxy(
                    renames["CommonFleetDefaultMemberConfigSpecIn"]
                ).optional(),
                "spec": t.proxy(renames["CommonFeatureSpecIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "membershipSpecs": t.struct({"_": t.string().optional()}).optional(),
                "scopeSpecs": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFeaturesCreate"] = gkehub.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "requestId": t.string().optional(),
                "name": t.string(),
                "fleetDefaultMemberConfig": t.proxy(
                    renames["CommonFleetDefaultMemberConfigSpecIn"]
                ).optional(),
                "spec": t.proxy(renames["CommonFeatureSpecIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "membershipSpecs": t.struct({"_": t.string().optional()}).optional(),
                "scopeSpecs": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFeaturesTestIamPermissions"] = gkehub.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "requestId": t.string().optional(),
                "name": t.string(),
                "fleetDefaultMemberConfig": t.proxy(
                    renames["CommonFleetDefaultMemberConfigSpecIn"]
                ).optional(),
                "spec": t.proxy(renames["CommonFeatureSpecIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "membershipSpecs": t.struct({"_": t.string().optional()}).optional(),
                "scopeSpecs": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFeaturesGet"] = gkehub.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "requestId": t.string().optional(),
                "name": t.string(),
                "fleetDefaultMemberConfig": t.proxy(
                    renames["CommonFleetDefaultMemberConfigSpecIn"]
                ).optional(),
                "spec": t.proxy(renames["CommonFeatureSpecIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "membershipSpecs": t.struct({"_": t.string().optional()}).optional(),
                "scopeSpecs": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFeaturesList"] = gkehub.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "requestId": t.string().optional(),
                "name": t.string(),
                "fleetDefaultMemberConfig": t.proxy(
                    renames["CommonFleetDefaultMemberConfigSpecIn"]
                ).optional(),
                "spec": t.proxy(renames["CommonFeatureSpecIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "membershipSpecs": t.struct({"_": t.string().optional()}).optional(),
                "scopeSpecs": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFeaturesGetIamPolicy"] = gkehub.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "requestId": t.string().optional(),
                "name": t.string(),
                "fleetDefaultMemberConfig": t.proxy(
                    renames["CommonFleetDefaultMemberConfigSpecIn"]
                ).optional(),
                "spec": t.proxy(renames["CommonFeatureSpecIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "membershipSpecs": t.struct({"_": t.string().optional()}).optional(),
                "scopeSpecs": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFeaturesDelete"] = gkehub.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "requestId": t.string().optional(),
                "name": t.string(),
                "fleetDefaultMemberConfig": t.proxy(
                    renames["CommonFleetDefaultMemberConfigSpecIn"]
                ).optional(),
                "spec": t.proxy(renames["CommonFeatureSpecIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "membershipSpecs": t.struct({"_": t.string().optional()}).optional(),
                "scopeSpecs": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFeaturesPatch"] = gkehub.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "requestId": t.string().optional(),
                "name": t.string(),
                "fleetDefaultMemberConfig": t.proxy(
                    renames["CommonFleetDefaultMemberConfigSpecIn"]
                ).optional(),
                "spec": t.proxy(renames["CommonFeatureSpecIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "membershipSpecs": t.struct({"_": t.string().optional()}).optional(),
                "scopeSpecs": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="gkehub", renames=renames, types=Box(types), functions=Box(functions)
    )
