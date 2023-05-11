from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_gkehub() -> Import:
    gkehub = HTTPRuntime("https://gkehub.googleapis.com/")

    renames = {
        "ErrorResponse": "_gkehub_1_ErrorResponse",
        "ConfigManagementGroupVersionKindIn": "_gkehub_2_ConfigManagementGroupVersionKindIn",
        "ConfigManagementGroupVersionKindOut": "_gkehub_3_ConfigManagementGroupVersionKindOut",
        "MembershipBindingIn": "_gkehub_4_MembershipBindingIn",
        "MembershipBindingOut": "_gkehub_5_MembershipBindingOut",
        "OnPremClusterIn": "_gkehub_6_OnPremClusterIn",
        "OnPremClusterOut": "_gkehub_7_OnPremClusterOut",
        "ListMembershipsResponseIn": "_gkehub_8_ListMembershipsResponseIn",
        "ListMembershipsResponseOut": "_gkehub_9_ListMembershipsResponseOut",
        "TestIamPermissionsResponseIn": "_gkehub_10_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_gkehub_11_TestIamPermissionsResponseOut",
        "BindingIn": "_gkehub_12_BindingIn",
        "BindingOut": "_gkehub_13_BindingOut",
        "ConfigManagementPolicyControllerStateIn": "_gkehub_14_ConfigManagementPolicyControllerStateIn",
        "ConfigManagementPolicyControllerStateOut": "_gkehub_15_ConfigManagementPolicyControllerStateOut",
        "FeatureStateIn": "_gkehub_16_FeatureStateIn",
        "FeatureStateOut": "_gkehub_17_FeatureStateOut",
        "ListLocationsResponseIn": "_gkehub_18_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_gkehub_19_ListLocationsResponseOut",
        "ServiceMeshControlPlaneManagementIn": "_gkehub_20_ServiceMeshControlPlaneManagementIn",
        "ServiceMeshControlPlaneManagementOut": "_gkehub_21_ServiceMeshControlPlaneManagementOut",
        "ResourceManifestIn": "_gkehub_22_ResourceManifestIn",
        "ResourceManifestOut": "_gkehub_23_ResourceManifestOut",
        "StatusIn": "_gkehub_24_StatusIn",
        "StatusOut": "_gkehub_25_StatusOut",
        "ConfigManagementConfigSyncVersionIn": "_gkehub_26_ConfigManagementConfigSyncVersionIn",
        "ConfigManagementConfigSyncVersionOut": "_gkehub_27_ConfigManagementConfigSyncVersionOut",
        "GoogleRpcStatusIn": "_gkehub_28_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_gkehub_29_GoogleRpcStatusOut",
        "ConfigManagementSyncStateIn": "_gkehub_30_ConfigManagementSyncStateIn",
        "ConfigManagementSyncStateOut": "_gkehub_31_ConfigManagementSyncStateOut",
        "MonitoringConfigIn": "_gkehub_32_MonitoringConfigIn",
        "MonitoringConfigOut": "_gkehub_33_MonitoringConfigOut",
        "ServiceMeshStatusDetailsIn": "_gkehub_34_ServiceMeshStatusDetailsIn",
        "ServiceMeshStatusDetailsOut": "_gkehub_35_ServiceMeshStatusDetailsOut",
        "FeatureResourceStateIn": "_gkehub_36_FeatureResourceStateIn",
        "FeatureResourceStateOut": "_gkehub_37_FeatureResourceStateOut",
        "ConfigManagementHierarchyControllerConfigIn": "_gkehub_38_ConfigManagementHierarchyControllerConfigIn",
        "ConfigManagementHierarchyControllerConfigOut": "_gkehub_39_ConfigManagementHierarchyControllerConfigOut",
        "FleetObservabilityFeatureSpecIn": "_gkehub_40_FleetObservabilityFeatureSpecIn",
        "FleetObservabilityFeatureSpecOut": "_gkehub_41_FleetObservabilityFeatureSpecOut",
        "ServiceMeshMembershipSpecIn": "_gkehub_42_ServiceMeshMembershipSpecIn",
        "ServiceMeshMembershipSpecOut": "_gkehub_43_ServiceMeshMembershipSpecOut",
        "CommonFleetDefaultMemberConfigSpecIn": "_gkehub_44_CommonFleetDefaultMemberConfigSpecIn",
        "CommonFleetDefaultMemberConfigSpecOut": "_gkehub_45_CommonFleetDefaultMemberConfigSpecOut",
        "ConfigManagementPolicyControllerMigrationIn": "_gkehub_46_ConfigManagementPolicyControllerMigrationIn",
        "ConfigManagementPolicyControllerMigrationOut": "_gkehub_47_ConfigManagementPolicyControllerMigrationOut",
        "MembershipFeatureSpecIn": "_gkehub_48_MembershipFeatureSpecIn",
        "MembershipFeatureSpecOut": "_gkehub_49_MembershipFeatureSpecOut",
        "IdentityServiceMembershipSpecIn": "_gkehub_50_IdentityServiceMembershipSpecIn",
        "IdentityServiceMembershipSpecOut": "_gkehub_51_IdentityServiceMembershipSpecOut",
        "ConfigManagementConfigSyncIn": "_gkehub_52_ConfigManagementConfigSyncIn",
        "ConfigManagementConfigSyncOut": "_gkehub_53_ConfigManagementConfigSyncOut",
        "TestIamPermissionsRequestIn": "_gkehub_54_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_gkehub_55_TestIamPermissionsRequestOut",
        "ExprIn": "_gkehub_56_ExprIn",
        "ExprOut": "_gkehub_57_ExprOut",
        "GenerateConnectManifestResponseIn": "_gkehub_58_GenerateConnectManifestResponseIn",
        "GenerateConnectManifestResponseOut": "_gkehub_59_GenerateConnectManifestResponseOut",
        "ConfigManagementHierarchyControllerDeploymentStateIn": "_gkehub_60_ConfigManagementHierarchyControllerDeploymentStateIn",
        "ConfigManagementHierarchyControllerDeploymentStateOut": "_gkehub_61_ConfigManagementHierarchyControllerDeploymentStateOut",
        "ServiceMeshDataPlaneManagementIn": "_gkehub_62_ServiceMeshDataPlaneManagementIn",
        "ServiceMeshDataPlaneManagementOut": "_gkehub_63_ServiceMeshDataPlaneManagementOut",
        "ConfigManagementPolicyControllerMonitoringIn": "_gkehub_64_ConfigManagementPolicyControllerMonitoringIn",
        "ConfigManagementPolicyControllerMonitoringOut": "_gkehub_65_ConfigManagementPolicyControllerMonitoringOut",
        "ConfigManagementMembershipStateIn": "_gkehub_66_ConfigManagementMembershipStateIn",
        "ConfigManagementMembershipStateOut": "_gkehub_67_ConfigManagementMembershipStateOut",
        "ConfigManagementGitConfigIn": "_gkehub_68_ConfigManagementGitConfigIn",
        "ConfigManagementGitConfigOut": "_gkehub_69_ConfigManagementGitConfigOut",
        "ConfigManagementErrorResourceIn": "_gkehub_70_ConfigManagementErrorResourceIn",
        "ConfigManagementErrorResourceOut": "_gkehub_71_ConfigManagementErrorResourceOut",
        "KubernetesResourceIn": "_gkehub_72_KubernetesResourceIn",
        "KubernetesResourceOut": "_gkehub_73_KubernetesResourceOut",
        "AppDevExperienceFeatureStateIn": "_gkehub_74_AppDevExperienceFeatureStateIn",
        "AppDevExperienceFeatureStateOut": "_gkehub_75_AppDevExperienceFeatureStateOut",
        "AuditConfigIn": "_gkehub_76_AuditConfigIn",
        "AuditConfigOut": "_gkehub_77_AuditConfigOut",
        "MembershipBindingLifecycleStateIn": "_gkehub_78_MembershipBindingLifecycleStateIn",
        "MembershipBindingLifecycleStateOut": "_gkehub_79_MembershipBindingLifecycleStateOut",
        "EdgeClusterIn": "_gkehub_80_EdgeClusterIn",
        "EdgeClusterOut": "_gkehub_81_EdgeClusterOut",
        "GkeClusterIn": "_gkehub_82_GkeClusterIn",
        "GkeClusterOut": "_gkehub_83_GkeClusterOut",
        "ScopeFeatureStateIn": "_gkehub_84_ScopeFeatureStateIn",
        "ScopeFeatureStateOut": "_gkehub_85_ScopeFeatureStateOut",
        "SetIamPolicyRequestIn": "_gkehub_86_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_gkehub_87_SetIamPolicyRequestOut",
        "MembershipFeatureStateIn": "_gkehub_88_MembershipFeatureStateIn",
        "MembershipFeatureStateOut": "_gkehub_89_MembershipFeatureStateOut",
        "AppDevExperienceFeatureSpecIn": "_gkehub_90_AppDevExperienceFeatureSpecIn",
        "AppDevExperienceFeatureSpecOut": "_gkehub_91_AppDevExperienceFeatureSpecOut",
        "IdentityServiceAzureADConfigIn": "_gkehub_92_IdentityServiceAzureADConfigIn",
        "IdentityServiceAzureADConfigOut": "_gkehub_93_IdentityServiceAzureADConfigOut",
        "MembershipEndpointIn": "_gkehub_94_MembershipEndpointIn",
        "MembershipEndpointOut": "_gkehub_95_MembershipEndpointOut",
        "AuditLogConfigIn": "_gkehub_96_AuditLogConfigIn",
        "AuditLogConfigOut": "_gkehub_97_AuditLogConfigOut",
        "FleetObservabilityMembershipSpecIn": "_gkehub_98_FleetObservabilityMembershipSpecIn",
        "FleetObservabilityMembershipSpecOut": "_gkehub_99_FleetObservabilityMembershipSpecOut",
        "ConfigManagementOperatorStateIn": "_gkehub_100_ConfigManagementOperatorStateIn",
        "ConfigManagementOperatorStateOut": "_gkehub_101_ConfigManagementOperatorStateOut",
        "MultiCloudClusterIn": "_gkehub_102_MultiCloudClusterIn",
        "MultiCloudClusterOut": "_gkehub_103_MultiCloudClusterOut",
        "ConfigManagementConfigSyncStateIn": "_gkehub_104_ConfigManagementConfigSyncStateIn",
        "ConfigManagementConfigSyncStateOut": "_gkehub_105_ConfigManagementConfigSyncStateOut",
        "ScopeFeatureSpecIn": "_gkehub_106_ScopeFeatureSpecIn",
        "ScopeFeatureSpecOut": "_gkehub_107_ScopeFeatureSpecOut",
        "ConfigManagementHierarchyControllerVersionIn": "_gkehub_108_ConfigManagementHierarchyControllerVersionIn",
        "ConfigManagementHierarchyControllerVersionOut": "_gkehub_109_ConfigManagementHierarchyControllerVersionOut",
        "IdentityServiceAuthMethodIn": "_gkehub_110_IdentityServiceAuthMethodIn",
        "IdentityServiceAuthMethodOut": "_gkehub_111_IdentityServiceAuthMethodOut",
        "ConfigManagementOciConfigIn": "_gkehub_112_ConfigManagementOciConfigIn",
        "ConfigManagementOciConfigOut": "_gkehub_113_ConfigManagementOciConfigOut",
        "MembershipStateIn": "_gkehub_114_MembershipStateIn",
        "MembershipStateOut": "_gkehub_115_MembershipStateOut",
        "PolicyIn": "_gkehub_116_PolicyIn",
        "PolicyOut": "_gkehub_117_PolicyOut",
        "OperationIn": "_gkehub_118_OperationIn",
        "OperationOut": "_gkehub_119_OperationOut",
        "IdentityServiceMembershipStateIn": "_gkehub_120_IdentityServiceMembershipStateIn",
        "IdentityServiceMembershipStateOut": "_gkehub_121_IdentityServiceMembershipStateOut",
        "ServiceMeshMembershipStateIn": "_gkehub_122_ServiceMeshMembershipStateIn",
        "ServiceMeshMembershipStateOut": "_gkehub_123_ServiceMeshMembershipStateOut",
        "ApplianceClusterIn": "_gkehub_124_ApplianceClusterIn",
        "ApplianceClusterOut": "_gkehub_125_ApplianceClusterOut",
        "CommonFeatureStateIn": "_gkehub_126_CommonFeatureStateIn",
        "CommonFeatureStateOut": "_gkehub_127_CommonFeatureStateOut",
        "CancelOperationRequestIn": "_gkehub_128_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_gkehub_129_CancelOperationRequestOut",
        "ListOperationsResponseIn": "_gkehub_130_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_gkehub_131_ListOperationsResponseOut",
        "ListFeaturesResponseIn": "_gkehub_132_ListFeaturesResponseIn",
        "ListFeaturesResponseOut": "_gkehub_133_ListFeaturesResponseOut",
        "ListScopesResponseIn": "_gkehub_134_ListScopesResponseIn",
        "ListScopesResponseOut": "_gkehub_135_ListScopesResponseOut",
        "FeatureIn": "_gkehub_136_FeatureIn",
        "FeatureOut": "_gkehub_137_FeatureOut",
        "ConfigManagementPolicyControllerVersionIn": "_gkehub_138_ConfigManagementPolicyControllerVersionIn",
        "ConfigManagementPolicyControllerVersionOut": "_gkehub_139_ConfigManagementPolicyControllerVersionOut",
        "ConfigManagementInstallErrorIn": "_gkehub_140_ConfigManagementInstallErrorIn",
        "ConfigManagementInstallErrorOut": "_gkehub_141_ConfigManagementInstallErrorOut",
        "ConfigManagementMembershipSpecIn": "_gkehub_142_ConfigManagementMembershipSpecIn",
        "ConfigManagementMembershipSpecOut": "_gkehub_143_ConfigManagementMembershipSpecOut",
        "OperationMetadataIn": "_gkehub_144_OperationMetadataIn",
        "OperationMetadataOut": "_gkehub_145_OperationMetadataOut",
        "ConfigManagementHierarchyControllerStateIn": "_gkehub_146_ConfigManagementHierarchyControllerStateIn",
        "ConfigManagementHierarchyControllerStateOut": "_gkehub_147_ConfigManagementHierarchyControllerStateOut",
        "ScopeIn": "_gkehub_148_ScopeIn",
        "ScopeOut": "_gkehub_149_ScopeOut",
        "TypeMetaIn": "_gkehub_150_TypeMetaIn",
        "TypeMetaOut": "_gkehub_151_TypeMetaOut",
        "ConnectAgentResourceIn": "_gkehub_152_ConnectAgentResourceIn",
        "ConnectAgentResourceOut": "_gkehub_153_ConnectAgentResourceOut",
        "AuthorityIn": "_gkehub_154_AuthorityIn",
        "AuthorityOut": "_gkehub_155_AuthorityOut",
        "ConfigManagementManagedIn": "_gkehub_156_ConfigManagementManagedIn",
        "ConfigManagementManagedOut": "_gkehub_157_ConfigManagementManagedOut",
        "IdentityServiceOidcConfigIn": "_gkehub_158_IdentityServiceOidcConfigIn",
        "IdentityServiceOidcConfigOut": "_gkehub_159_IdentityServiceOidcConfigOut",
        "IdentityServiceGoogleConfigIn": "_gkehub_160_IdentityServiceGoogleConfigIn",
        "IdentityServiceGoogleConfigOut": "_gkehub_161_IdentityServiceGoogleConfigOut",
        "MembershipIn": "_gkehub_162_MembershipIn",
        "MembershipOut": "_gkehub_163_MembershipOut",
        "ListMembershipBindingsResponseIn": "_gkehub_164_ListMembershipBindingsResponseIn",
        "ListMembershipBindingsResponseOut": "_gkehub_165_ListMembershipBindingsResponseOut",
        "KubernetesMetadataIn": "_gkehub_166_KubernetesMetadataIn",
        "KubernetesMetadataOut": "_gkehub_167_KubernetesMetadataOut",
        "FleetObservabilityMembershipStateIn": "_gkehub_168_FleetObservabilityMembershipStateIn",
        "FleetObservabilityMembershipStateOut": "_gkehub_169_FleetObservabilityMembershipStateOut",
        "ScopeLifecycleStateIn": "_gkehub_170_ScopeLifecycleStateIn",
        "ScopeLifecycleStateOut": "_gkehub_171_ScopeLifecycleStateOut",
        "ConfigManagementSyncErrorIn": "_gkehub_172_ConfigManagementSyncErrorIn",
        "ConfigManagementSyncErrorOut": "_gkehub_173_ConfigManagementSyncErrorOut",
        "EmptyIn": "_gkehub_174_EmptyIn",
        "EmptyOut": "_gkehub_175_EmptyOut",
        "ConfigManagementPolicyControllerIn": "_gkehub_176_ConfigManagementPolicyControllerIn",
        "ConfigManagementPolicyControllerOut": "_gkehub_177_ConfigManagementPolicyControllerOut",
        "LocationIn": "_gkehub_178_LocationIn",
        "LocationOut": "_gkehub_179_LocationOut",
        "ConfigManagementGatekeeperDeploymentStateIn": "_gkehub_180_ConfigManagementGatekeeperDeploymentStateIn",
        "ConfigManagementGatekeeperDeploymentStateOut": "_gkehub_181_ConfigManagementGatekeeperDeploymentStateOut",
        "FleetObservabilityFeatureStateIn": "_gkehub_182_FleetObservabilityFeatureStateIn",
        "FleetObservabilityFeatureStateOut": "_gkehub_183_FleetObservabilityFeatureStateOut",
        "CommonFeatureSpecIn": "_gkehub_184_CommonFeatureSpecIn",
        "CommonFeatureSpecOut": "_gkehub_185_CommonFeatureSpecOut",
        "ConfigManagementConfigSyncDeploymentStateIn": "_gkehub_186_ConfigManagementConfigSyncDeploymentStateIn",
        "ConfigManagementConfigSyncDeploymentStateOut": "_gkehub_187_ConfigManagementConfigSyncDeploymentStateOut",
        "MultiClusterIngressFeatureSpecIn": "_gkehub_188_MultiClusterIngressFeatureSpecIn",
        "MultiClusterIngressFeatureSpecOut": "_gkehub_189_MultiClusterIngressFeatureSpecOut",
        "ResourceOptionsIn": "_gkehub_190_ResourceOptionsIn",
        "ResourceOptionsOut": "_gkehub_191_ResourceOptionsOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ConfigManagementGroupVersionKindIn"] = t.struct(
        {
            "group": t.string().optional(),
            "version": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ConfigManagementGroupVersionKindIn"])
    types["ConfigManagementGroupVersionKindOut"] = t.struct(
        {
            "group": t.string().optional(),
            "version": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementGroupVersionKindOut"])
    types["MembershipBindingIn"] = t.struct(
        {
            "name": t.string().optional(),
            "scope": t.string().optional(),
            "fleet": t.boolean().optional(),
        }
    ).named(renames["MembershipBindingIn"])
    types["MembershipBindingOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "uid": t.string().optional(),
            "state": t.proxy(renames["MembershipBindingLifecycleStateOut"]).optional(),
            "scope": t.string().optional(),
            "deleteTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "fleet": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipBindingOut"])
    types["OnPremClusterIn"] = t.struct(
        {
            "clusterType": t.string().optional(),
            "adminCluster": t.boolean().optional(),
            "resourceLink": t.string().optional(),
        }
    ).named(renames["OnPremClusterIn"])
    types["OnPremClusterOut"] = t.struct(
        {
            "clusterType": t.string().optional(),
            "adminCluster": t.boolean().optional(),
            "clusterMissing": t.boolean().optional(),
            "resourceLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OnPremClusterOut"])
    types["ListMembershipsResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "resources": t.array(t.proxy(renames["MembershipIn"])).optional(),
        }
    ).named(renames["ListMembershipsResponseIn"])
    types["ListMembershipsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "resources": t.array(t.proxy(renames["MembershipOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListMembershipsResponseOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
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
    types["ConfigManagementPolicyControllerStateIn"] = t.struct(
        {
            "migration": t.proxy(
                renames["ConfigManagementPolicyControllerMigrationIn"]
            ).optional(),
            "version": t.proxy(
                renames["ConfigManagementPolicyControllerVersionIn"]
            ).optional(),
            "deploymentState": t.proxy(
                renames["ConfigManagementGatekeeperDeploymentStateIn"]
            ).optional(),
        }
    ).named(renames["ConfigManagementPolicyControllerStateIn"])
    types["ConfigManagementPolicyControllerStateOut"] = t.struct(
        {
            "migration": t.proxy(
                renames["ConfigManagementPolicyControllerMigrationOut"]
            ).optional(),
            "version": t.proxy(
                renames["ConfigManagementPolicyControllerVersionOut"]
            ).optional(),
            "deploymentState": t.proxy(
                renames["ConfigManagementGatekeeperDeploymentStateOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementPolicyControllerStateOut"])
    types["FeatureStateIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "description": t.string().optional(),
            "code": t.string().optional(),
        }
    ).named(renames["FeatureStateIn"])
    types["FeatureStateOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "description": t.string().optional(),
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FeatureStateOut"])
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
    types["StatusIn"] = t.struct(
        {"description": t.string().optional(), "code": t.string().optional()}
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "description": t.string().optional(),
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["ConfigManagementConfigSyncVersionIn"] = t.struct(
        {
            "gitSync": t.string().optional(),
            "reconcilerManager": t.string().optional(),
            "importer": t.string().optional(),
            "monitor": t.string().optional(),
            "syncer": t.string().optional(),
            "rootReconciler": t.string().optional(),
            "admissionWebhook": t.string().optional(),
        }
    ).named(renames["ConfigManagementConfigSyncVersionIn"])
    types["ConfigManagementConfigSyncVersionOut"] = t.struct(
        {
            "gitSync": t.string().optional(),
            "reconcilerManager": t.string().optional(),
            "importer": t.string().optional(),
            "monitor": t.string().optional(),
            "syncer": t.string().optional(),
            "rootReconciler": t.string().optional(),
            "admissionWebhook": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementConfigSyncVersionOut"])
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
    types["ConfigManagementSyncStateIn"] = t.struct(
        {
            "code": t.string().optional(),
            "sourceToken": t.string().optional(),
            "importToken": t.string().optional(),
            "errors": t.array(
                t.proxy(renames["ConfigManagementSyncErrorIn"])
            ).optional(),
            "syncToken": t.string().optional(),
            "lastSync": t.string().optional(),
            "lastSyncTime": t.string().optional(),
        }
    ).named(renames["ConfigManagementSyncStateIn"])
    types["ConfigManagementSyncStateOut"] = t.struct(
        {
            "code": t.string().optional(),
            "sourceToken": t.string().optional(),
            "importToken": t.string().optional(),
            "errors": t.array(
                t.proxy(renames["ConfigManagementSyncErrorOut"])
            ).optional(),
            "syncToken": t.string().optional(),
            "lastSync": t.string().optional(),
            "lastSyncTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementSyncStateOut"])
    types["MonitoringConfigIn"] = t.struct(
        {
            "projectId": t.string().optional(),
            "cluster": t.string().optional(),
            "kubernetesMetricsPrefix": t.string().optional(),
            "clusterHash": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["MonitoringConfigIn"])
    types["MonitoringConfigOut"] = t.struct(
        {
            "projectId": t.string().optional(),
            "cluster": t.string().optional(),
            "kubernetesMetricsPrefix": t.string().optional(),
            "clusterHash": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MonitoringConfigOut"])
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
    types["FeatureResourceStateIn"] = t.struct({"state": t.string().optional()}).named(
        renames["FeatureResourceStateIn"]
    )
    types["FeatureResourceStateOut"] = t.struct(
        {
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FeatureResourceStateOut"])
    types["ConfigManagementHierarchyControllerConfigIn"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "enablePodTreeLabels": t.boolean().optional(),
            "enableHierarchicalResourceQuota": t.boolean().optional(),
        }
    ).named(renames["ConfigManagementHierarchyControllerConfigIn"])
    types["ConfigManagementHierarchyControllerConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "enablePodTreeLabels": t.boolean().optional(),
            "enableHierarchicalResourceQuota": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementHierarchyControllerConfigOut"])
    types["FleetObservabilityFeatureSpecIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["FleetObservabilityFeatureSpecIn"])
    types["FleetObservabilityFeatureSpecOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["FleetObservabilityFeatureSpecOut"])
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
    types["CommonFleetDefaultMemberConfigSpecIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["CommonFleetDefaultMemberConfigSpecIn"])
    types["CommonFleetDefaultMemberConfigSpecOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CommonFleetDefaultMemberConfigSpecOut"])
    types["ConfigManagementPolicyControllerMigrationIn"] = t.struct(
        {"stage": t.string().optional()}
    ).named(renames["ConfigManagementPolicyControllerMigrationIn"])
    types["ConfigManagementPolicyControllerMigrationOut"] = t.struct(
        {
            "stage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementPolicyControllerMigrationOut"])
    types["MembershipFeatureSpecIn"] = t.struct(
        {
            "fleetobservability": t.proxy(
                renames["FleetObservabilityMembershipSpecIn"]
            ).optional(),
            "fleetInherited": t.boolean().optional(),
            "identityservice": t.proxy(
                renames["IdentityServiceMembershipSpecIn"]
            ).optional(),
            "configmanagement": t.proxy(
                renames["ConfigManagementMembershipSpecIn"]
            ).optional(),
            "mesh": t.proxy(renames["ServiceMeshMembershipSpecIn"]).optional(),
        }
    ).named(renames["MembershipFeatureSpecIn"])
    types["MembershipFeatureSpecOut"] = t.struct(
        {
            "fleetobservability": t.proxy(
                renames["FleetObservabilityMembershipSpecOut"]
            ).optional(),
            "fleetInherited": t.boolean().optional(),
            "identityservice": t.proxy(
                renames["IdentityServiceMembershipSpecOut"]
            ).optional(),
            "configmanagement": t.proxy(
                renames["ConfigManagementMembershipSpecOut"]
            ).optional(),
            "mesh": t.proxy(renames["ServiceMeshMembershipSpecOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipFeatureSpecOut"])
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
    types["ConfigManagementConfigSyncIn"] = t.struct(
        {
            "allowVerticalScale": t.boolean().optional(),
            "sourceFormat": t.string().optional(),
            "enabled": t.boolean().optional(),
            "oci": t.proxy(renames["ConfigManagementOciConfigIn"]).optional(),
            "managed": t.proxy(renames["ConfigManagementManagedIn"]).optional(),
            "preventDrift": t.boolean().optional(),
            "git": t.proxy(renames["ConfigManagementGitConfigIn"]).optional(),
        }
    ).named(renames["ConfigManagementConfigSyncIn"])
    types["ConfigManagementConfigSyncOut"] = t.struct(
        {
            "allowVerticalScale": t.boolean().optional(),
            "sourceFormat": t.string().optional(),
            "enabled": t.boolean().optional(),
            "oci": t.proxy(renames["ConfigManagementOciConfigOut"]).optional(),
            "managed": t.proxy(renames["ConfigManagementManagedOut"]).optional(),
            "preventDrift": t.boolean().optional(),
            "git": t.proxy(renames["ConfigManagementGitConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementConfigSyncOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["ExprIn"] = t.struct(
        {
            "title": t.string().optional(),
            "description": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "title": t.string().optional(),
            "description": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["GenerateConnectManifestResponseIn"] = t.struct(
        {"manifest": t.array(t.proxy(renames["ConnectAgentResourceIn"])).optional()}
    ).named(renames["GenerateConnectManifestResponseIn"])
    types["GenerateConnectManifestResponseOut"] = t.struct(
        {
            "manifest": t.array(t.proxy(renames["ConnectAgentResourceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateConnectManifestResponseOut"])
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
    types["ConfigManagementPolicyControllerMonitoringIn"] = t.struct(
        {"backends": t.array(t.string()).optional()}
    ).named(renames["ConfigManagementPolicyControllerMonitoringIn"])
    types["ConfigManagementPolicyControllerMonitoringOut"] = t.struct(
        {
            "backends": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementPolicyControllerMonitoringOut"])
    types["ConfigManagementMembershipStateIn"] = t.struct(
        {
            "membershipSpec": t.proxy(
                renames["ConfigManagementMembershipSpecIn"]
            ).optional(),
            "hierarchyControllerState": t.proxy(
                renames["ConfigManagementHierarchyControllerStateIn"]
            ).optional(),
            "operatorState": t.proxy(
                renames["ConfigManagementOperatorStateIn"]
            ).optional(),
            "policyControllerState": t.proxy(
                renames["ConfigManagementPolicyControllerStateIn"]
            ).optional(),
            "configSyncState": t.proxy(
                renames["ConfigManagementConfigSyncStateIn"]
            ).optional(),
            "clusterName": t.string().optional(),
        }
    ).named(renames["ConfigManagementMembershipStateIn"])
    types["ConfigManagementMembershipStateOut"] = t.struct(
        {
            "membershipSpec": t.proxy(
                renames["ConfigManagementMembershipSpecOut"]
            ).optional(),
            "hierarchyControllerState": t.proxy(
                renames["ConfigManagementHierarchyControllerStateOut"]
            ).optional(),
            "operatorState": t.proxy(
                renames["ConfigManagementOperatorStateOut"]
            ).optional(),
            "policyControllerState": t.proxy(
                renames["ConfigManagementPolicyControllerStateOut"]
            ).optional(),
            "configSyncState": t.proxy(
                renames["ConfigManagementConfigSyncStateOut"]
            ).optional(),
            "clusterName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementMembershipStateOut"])
    types["ConfigManagementGitConfigIn"] = t.struct(
        {
            "gcpServiceAccountEmail": t.string().optional(),
            "secretType": t.string().optional(),
            "policyDir": t.string().optional(),
            "syncRepo": t.string().optional(),
            "syncWaitSecs": t.string().optional(),
            "syncBranch": t.string().optional(),
            "httpsProxy": t.string().optional(),
            "syncRev": t.string().optional(),
        }
    ).named(renames["ConfigManagementGitConfigIn"])
    types["ConfigManagementGitConfigOut"] = t.struct(
        {
            "gcpServiceAccountEmail": t.string().optional(),
            "secretType": t.string().optional(),
            "policyDir": t.string().optional(),
            "syncRepo": t.string().optional(),
            "syncWaitSecs": t.string().optional(),
            "syncBranch": t.string().optional(),
            "httpsProxy": t.string().optional(),
            "syncRev": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementGitConfigOut"])
    types["ConfigManagementErrorResourceIn"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "resourceNamespace": t.string().optional(),
            "sourcePath": t.string().optional(),
            "resourceGvk": t.proxy(
                renames["ConfigManagementGroupVersionKindIn"]
            ).optional(),
        }
    ).named(renames["ConfigManagementErrorResourceIn"])
    types["ConfigManagementErrorResourceOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "resourceNamespace": t.string().optional(),
            "sourcePath": t.string().optional(),
            "resourceGvk": t.proxy(
                renames["ConfigManagementGroupVersionKindOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementErrorResourceOut"])
    types["KubernetesResourceIn"] = t.struct(
        {
            "resourceOptions": t.proxy(renames["ResourceOptionsIn"]).optional(),
            "membershipCrManifest": t.string().optional(),
        }
    ).named(renames["KubernetesResourceIn"])
    types["KubernetesResourceOut"] = t.struct(
        {
            "connectResources": t.array(
                t.proxy(renames["ResourceManifestOut"])
            ).optional(),
            "membershipResources": t.array(
                t.proxy(renames["ResourceManifestOut"])
            ).optional(),
            "resourceOptions": t.proxy(renames["ResourceOptionsOut"]).optional(),
            "membershipCrManifest": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KubernetesResourceOut"])
    types["AppDevExperienceFeatureStateIn"] = t.struct(
        {"networkingInstallSucceeded": t.proxy(renames["StatusIn"]).optional()}
    ).named(renames["AppDevExperienceFeatureStateIn"])
    types["AppDevExperienceFeatureStateOut"] = t.struct(
        {
            "networkingInstallSucceeded": t.proxy(renames["StatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppDevExperienceFeatureStateOut"])
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
    types["EdgeClusterIn"] = t.struct({"resourceLink": t.string().optional()}).named(
        renames["EdgeClusterIn"]
    )
    types["EdgeClusterOut"] = t.struct(
        {
            "resourceLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EdgeClusterOut"])
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
    types["ScopeFeatureStateIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ScopeFeatureStateIn"]
    )
    types["ScopeFeatureStateOut"] = t.struct(
        {
            "state": t.proxy(renames["FeatureStateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScopeFeatureStateOut"])
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
    types["MembershipFeatureStateIn"] = t.struct(
        {
            "servicemesh": t.proxy(renames["ServiceMeshMembershipStateIn"]).optional(),
            "identityservice": t.proxy(
                renames["IdentityServiceMembershipStateIn"]
            ).optional(),
            "configmanagement": t.proxy(
                renames["ConfigManagementMembershipStateIn"]
            ).optional(),
            "fleetobservability": t.proxy(
                renames["FleetObservabilityMembershipStateIn"]
            ).optional(),
            "state": t.proxy(renames["FeatureStateIn"]).optional(),
            "appdevexperience": t.proxy(
                renames["AppDevExperienceFeatureStateIn"]
            ).optional(),
        }
    ).named(renames["MembershipFeatureStateIn"])
    types["MembershipFeatureStateOut"] = t.struct(
        {
            "servicemesh": t.proxy(renames["ServiceMeshMembershipStateOut"]).optional(),
            "identityservice": t.proxy(
                renames["IdentityServiceMembershipStateOut"]
            ).optional(),
            "configmanagement": t.proxy(
                renames["ConfigManagementMembershipStateOut"]
            ).optional(),
            "fleetobservability": t.proxy(
                renames["FleetObservabilityMembershipStateOut"]
            ).optional(),
            "state": t.proxy(renames["FeatureStateOut"]).optional(),
            "appdevexperience": t.proxy(
                renames["AppDevExperienceFeatureStateOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipFeatureStateOut"])
    types["AppDevExperienceFeatureSpecIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AppDevExperienceFeatureSpecIn"])
    types["AppDevExperienceFeatureSpecOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AppDevExperienceFeatureSpecOut"])
    types["IdentityServiceAzureADConfigIn"] = t.struct(
        {
            "tenant": t.string().optional(),
            "clientId": t.string().optional(),
            "clientSecret": t.string().optional(),
            "kubectlRedirectUri": t.string().optional(),
        }
    ).named(renames["IdentityServiceAzureADConfigIn"])
    types["IdentityServiceAzureADConfigOut"] = t.struct(
        {
            "tenant": t.string().optional(),
            "clientId": t.string().optional(),
            "clientSecret": t.string().optional(),
            "encryptedClientSecret": t.string().optional(),
            "kubectlRedirectUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentityServiceAzureADConfigOut"])
    types["MembershipEndpointIn"] = t.struct(
        {
            "onPremCluster": t.proxy(renames["OnPremClusterIn"]).optional(),
            "edgeCluster": t.proxy(renames["EdgeClusterIn"]).optional(),
            "multiCloudCluster": t.proxy(renames["MultiCloudClusterIn"]).optional(),
            "applianceCluster": t.proxy(renames["ApplianceClusterIn"]).optional(),
            "kubernetesResource": t.proxy(renames["KubernetesResourceIn"]).optional(),
            "gkeCluster": t.proxy(renames["GkeClusterIn"]).optional(),
        }
    ).named(renames["MembershipEndpointIn"])
    types["MembershipEndpointOut"] = t.struct(
        {
            "onPremCluster": t.proxy(renames["OnPremClusterOut"]).optional(),
            "googleManaged": t.boolean().optional(),
            "edgeCluster": t.proxy(renames["EdgeClusterOut"]).optional(),
            "kubernetesMetadata": t.proxy(renames["KubernetesMetadataOut"]).optional(),
            "multiCloudCluster": t.proxy(renames["MultiCloudClusterOut"]).optional(),
            "applianceCluster": t.proxy(renames["ApplianceClusterOut"]).optional(),
            "kubernetesResource": t.proxy(renames["KubernetesResourceOut"]).optional(),
            "gkeCluster": t.proxy(renames["GkeClusterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipEndpointOut"])
    types["AuditLogConfigIn"] = t.struct(
        {
            "exemptedMembers": t.array(t.string()).optional(),
            "logType": t.string().optional(),
        }
    ).named(renames["AuditLogConfigIn"])
    types["AuditLogConfigOut"] = t.struct(
        {
            "exemptedMembers": t.array(t.string()).optional(),
            "logType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditLogConfigOut"])
    types["FleetObservabilityMembershipSpecIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["FleetObservabilityMembershipSpecIn"])
    types["FleetObservabilityMembershipSpecOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["FleetObservabilityMembershipSpecOut"])
    types["ConfigManagementOperatorStateIn"] = t.struct(
        {
            "deploymentState": t.string().optional(),
            "errors": t.array(
                t.proxy(renames["ConfigManagementInstallErrorIn"])
            ).optional(),
            "version": t.string().optional(),
        }
    ).named(renames["ConfigManagementOperatorStateIn"])
    types["ConfigManagementOperatorStateOut"] = t.struct(
        {
            "deploymentState": t.string().optional(),
            "errors": t.array(
                t.proxy(renames["ConfigManagementInstallErrorOut"])
            ).optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementOperatorStateOut"])
    types["MultiCloudClusterIn"] = t.struct(
        {"resourceLink": t.string().optional()}
    ).named(renames["MultiCloudClusterIn"])
    types["MultiCloudClusterOut"] = t.struct(
        {
            "resourceLink": t.string().optional(),
            "clusterMissing": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MultiCloudClusterOut"])
    types["ConfigManagementConfigSyncStateIn"] = t.struct(
        {
            "syncState": t.proxy(renames["ConfigManagementSyncStateIn"]).optional(),
            "version": t.proxy(
                renames["ConfigManagementConfigSyncVersionIn"]
            ).optional(),
            "deploymentState": t.proxy(
                renames["ConfigManagementConfigSyncDeploymentStateIn"]
            ).optional(),
        }
    ).named(renames["ConfigManagementConfigSyncStateIn"])
    types["ConfigManagementConfigSyncStateOut"] = t.struct(
        {
            "syncState": t.proxy(renames["ConfigManagementSyncStateOut"]).optional(),
            "version": t.proxy(
                renames["ConfigManagementConfigSyncVersionOut"]
            ).optional(),
            "deploymentState": t.proxy(
                renames["ConfigManagementConfigSyncDeploymentStateOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementConfigSyncStateOut"])
    types["ScopeFeatureSpecIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ScopeFeatureSpecIn"]
    )
    types["ScopeFeatureSpecOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ScopeFeatureSpecOut"])
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
    types["IdentityServiceAuthMethodIn"] = t.struct(
        {
            "name": t.string().optional(),
            "oidcConfig": t.proxy(renames["IdentityServiceOidcConfigIn"]).optional(),
            "azureadConfig": t.proxy(
                renames["IdentityServiceAzureADConfigIn"]
            ).optional(),
            "googleConfig": t.proxy(
                renames["IdentityServiceGoogleConfigIn"]
            ).optional(),
            "proxy": t.string().optional(),
        }
    ).named(renames["IdentityServiceAuthMethodIn"])
    types["IdentityServiceAuthMethodOut"] = t.struct(
        {
            "name": t.string().optional(),
            "oidcConfig": t.proxy(renames["IdentityServiceOidcConfigOut"]).optional(),
            "azureadConfig": t.proxy(
                renames["IdentityServiceAzureADConfigOut"]
            ).optional(),
            "googleConfig": t.proxy(
                renames["IdentityServiceGoogleConfigOut"]
            ).optional(),
            "proxy": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentityServiceAuthMethodOut"])
    types["ConfigManagementOciConfigIn"] = t.struct(
        {
            "gcpServiceAccountEmail": t.string().optional(),
            "syncWaitSecs": t.string().optional(),
            "secretType": t.string().optional(),
            "syncRepo": t.string().optional(),
            "policyDir": t.string().optional(),
        }
    ).named(renames["ConfigManagementOciConfigIn"])
    types["ConfigManagementOciConfigOut"] = t.struct(
        {
            "gcpServiceAccountEmail": t.string().optional(),
            "syncWaitSecs": t.string().optional(),
            "secretType": t.string().optional(),
            "syncRepo": t.string().optional(),
            "policyDir": t.string().optional(),
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
    types["OperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
    types["IdentityServiceMembershipStateIn"] = t.struct(
        {
            "installedVersion": t.string().optional(),
            "failureReason": t.string().optional(),
            "memberConfig": t.proxy(
                renames["IdentityServiceMembershipSpecIn"]
            ).optional(),
            "state": t.string().optional(),
        }
    ).named(renames["IdentityServiceMembershipStateIn"])
    types["IdentityServiceMembershipStateOut"] = t.struct(
        {
            "installedVersion": t.string().optional(),
            "failureReason": t.string().optional(),
            "memberConfig": t.proxy(
                renames["IdentityServiceMembershipSpecOut"]
            ).optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentityServiceMembershipStateOut"])
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
            "fleetobservability": t.proxy(
                renames["FleetObservabilityFeatureStateOut"]
            ).optional(),
            "state": t.proxy(renames["FeatureStateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommonFeatureStateOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
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
    types["ListScopesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "scopes": t.array(t.proxy(renames["ScopeIn"])).optional(),
        }
    ).named(renames["ListScopesResponseIn"])
    types["ListScopesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "scopes": t.array(t.proxy(renames["ScopeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListScopesResponseOut"])
    types["FeatureIn"] = t.struct(
        {
            "scopeSpecs": t.struct({"_": t.string().optional()}).optional(),
            "fleetDefaultMemberConfig": t.proxy(
                renames["CommonFleetDefaultMemberConfigSpecIn"]
            ).optional(),
            "membershipSpecs": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "spec": t.proxy(renames["CommonFeatureSpecIn"]).optional(),
        }
    ).named(renames["FeatureIn"])
    types["FeatureOut"] = t.struct(
        {
            "deleteTime": t.string().optional(),
            "scopeSpecs": t.struct({"_": t.string().optional()}).optional(),
            "resourceState": t.proxy(renames["FeatureResourceStateOut"]).optional(),
            "fleetDefaultMemberConfig": t.proxy(
                renames["CommonFleetDefaultMemberConfigSpecOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "membershipSpecs": t.struct({"_": t.string().optional()}).optional(),
            "scopeStates": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "spec": t.proxy(renames["CommonFeatureSpecOut"]).optional(),
            "membershipStates": t.struct({"_": t.string().optional()}).optional(),
            "state": t.proxy(renames["CommonFeatureStateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FeatureOut"])
    types["ConfigManagementPolicyControllerVersionIn"] = t.struct(
        {"version": t.string().optional()}
    ).named(renames["ConfigManagementPolicyControllerVersionIn"])
    types["ConfigManagementPolicyControllerVersionOut"] = t.struct(
        {
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementPolicyControllerVersionOut"])
    types["ConfigManagementInstallErrorIn"] = t.struct(
        {"errorMessage": t.string().optional()}
    ).named(renames["ConfigManagementInstallErrorIn"])
    types["ConfigManagementInstallErrorOut"] = t.struct(
        {
            "errorMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementInstallErrorOut"])
    types["ConfigManagementMembershipSpecIn"] = t.struct(
        {
            "hierarchyController": t.proxy(
                renames["ConfigManagementHierarchyControllerConfigIn"]
            ).optional(),
            "configSync": t.proxy(renames["ConfigManagementConfigSyncIn"]).optional(),
            "version": t.string().optional(),
            "policyController": t.proxy(
                renames["ConfigManagementPolicyControllerIn"]
            ).optional(),
        }
    ).named(renames["ConfigManagementMembershipSpecIn"])
    types["ConfigManagementMembershipSpecOut"] = t.struct(
        {
            "hierarchyController": t.proxy(
                renames["ConfigManagementHierarchyControllerConfigOut"]
            ).optional(),
            "configSync": t.proxy(renames["ConfigManagementConfigSyncOut"]).optional(),
            "version": t.string().optional(),
            "policyController": t.proxy(
                renames["ConfigManagementPolicyControllerOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementMembershipSpecOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "verb": t.string().optional(),
            "apiVersion": t.string().optional(),
            "target": t.string().optional(),
            "endTime": t.string().optional(),
            "statusDetail": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["ConfigManagementHierarchyControllerStateIn"] = t.struct(
        {
            "state": t.proxy(
                renames["ConfigManagementHierarchyControllerDeploymentStateIn"]
            ).optional(),
            "version": t.proxy(
                renames["ConfigManagementHierarchyControllerVersionIn"]
            ).optional(),
        }
    ).named(renames["ConfigManagementHierarchyControllerStateIn"])
    types["ConfigManagementHierarchyControllerStateOut"] = t.struct(
        {
            "state": t.proxy(
                renames["ConfigManagementHierarchyControllerDeploymentStateOut"]
            ).optional(),
            "version": t.proxy(
                renames["ConfigManagementHierarchyControllerVersionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementHierarchyControllerStateOut"])
    types["ScopeIn"] = t.struct(
        {"name": t.string().optional(), "allMemberships": t.boolean().optional()}
    ).named(renames["ScopeIn"])
    types["ScopeOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "allMemberships": t.boolean().optional(),
            "updateTime": t.string().optional(),
            "uid": t.string().optional(),
            "deleteTime": t.string().optional(),
            "state": t.proxy(renames["ScopeLifecycleStateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScopeOut"])
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
    types["AuthorityIn"] = t.struct(
        {"oidcJwks": t.string().optional(), "issuer": t.string().optional()}
    ).named(renames["AuthorityIn"])
    types["AuthorityOut"] = t.struct(
        {
            "identityProvider": t.string().optional(),
            "oidcJwks": t.string().optional(),
            "issuer": t.string().optional(),
            "workloadIdentityPool": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthorityOut"])
    types["ConfigManagementManagedIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["ConfigManagementManagedIn"])
    types["ConfigManagementManagedOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementManagedOut"])
    types["IdentityServiceOidcConfigIn"] = t.struct(
        {
            "clientSecret": t.string().optional(),
            "groupsClaim": t.string().optional(),
            "userClaim": t.string().optional(),
            "certificateAuthorityData": t.string().optional(),
            "scopes": t.string().optional(),
            "kubectlRedirectUri": t.string().optional(),
            "deployCloudConsoleProxy": t.boolean().optional(),
            "groupPrefix": t.string().optional(),
            "extraParams": t.string().optional(),
            "issuerUri": t.string().optional(),
            "enableAccessToken": t.boolean().optional(),
            "userPrefix": t.string().optional(),
            "clientId": t.string().optional(),
        }
    ).named(renames["IdentityServiceOidcConfigIn"])
    types["IdentityServiceOidcConfigOut"] = t.struct(
        {
            "clientSecret": t.string().optional(),
            "groupsClaim": t.string().optional(),
            "userClaim": t.string().optional(),
            "certificateAuthorityData": t.string().optional(),
            "scopes": t.string().optional(),
            "kubectlRedirectUri": t.string().optional(),
            "deployCloudConsoleProxy": t.boolean().optional(),
            "groupPrefix": t.string().optional(),
            "encryptedClientSecret": t.string().optional(),
            "extraParams": t.string().optional(),
            "issuerUri": t.string().optional(),
            "enableAccessToken": t.boolean().optional(),
            "userPrefix": t.string().optional(),
            "clientId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentityServiceOidcConfigOut"])
    types["IdentityServiceGoogleConfigIn"] = t.struct(
        {"disable": t.boolean().optional()}
    ).named(renames["IdentityServiceGoogleConfigIn"])
    types["IdentityServiceGoogleConfigOut"] = t.struct(
        {
            "disable": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentityServiceGoogleConfigOut"])
    types["MembershipIn"] = t.struct(
        {
            "externalId": t.string().optional(),
            "authority": t.proxy(renames["AuthorityIn"]).optional(),
            "monitoringConfig": t.proxy(renames["MonitoringConfigIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "endpoint": t.proxy(renames["MembershipEndpointIn"]).optional(),
        }
    ).named(renames["MembershipIn"])
    types["MembershipOut"] = t.struct(
        {
            "lastConnectionTime": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "uniqueId": t.string().optional(),
            "deleteTime": t.string().optional(),
            "externalId": t.string().optional(),
            "description": t.string().optional(),
            "authority": t.proxy(renames["AuthorityOut"]).optional(),
            "state": t.proxy(renames["MembershipStateOut"]).optional(),
            "monitoringConfig": t.proxy(renames["MonitoringConfigOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "endpoint": t.proxy(renames["MembershipEndpointOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipOut"])
    types["ListMembershipBindingsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "membershipBindings": t.array(
                t.proxy(renames["MembershipBindingIn"])
            ).optional(),
        }
    ).named(renames["ListMembershipBindingsResponseIn"])
    types["ListMembershipBindingsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "membershipBindings": t.array(
                t.proxy(renames["MembershipBindingOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListMembershipBindingsResponseOut"])
    types["KubernetesMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["KubernetesMetadataIn"]
    )
    types["KubernetesMetadataOut"] = t.struct(
        {
            "vcpuCount": t.integer().optional(),
            "nodeProviderId": t.string().optional(),
            "kubernetesApiServerVersion": t.string().optional(),
            "nodeCount": t.integer().optional(),
            "updateTime": t.string().optional(),
            "memoryMb": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KubernetesMetadataOut"])
    types["FleetObservabilityMembershipStateIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["FleetObservabilityMembershipStateIn"])
    types["FleetObservabilityMembershipStateOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["FleetObservabilityMembershipStateOut"])
    types["ScopeLifecycleStateIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ScopeLifecycleStateIn"]
    )
    types["ScopeLifecycleStateOut"] = t.struct(
        {
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScopeLifecycleStateOut"])
    types["ConfigManagementSyncErrorIn"] = t.struct(
        {
            "errorResources": t.array(
                t.proxy(renames["ConfigManagementErrorResourceIn"])
            ).optional(),
            "errorMessage": t.string().optional(),
            "code": t.string().optional(),
        }
    ).named(renames["ConfigManagementSyncErrorIn"])
    types["ConfigManagementSyncErrorOut"] = t.struct(
        {
            "errorResources": t.array(
                t.proxy(renames["ConfigManagementErrorResourceOut"])
            ).optional(),
            "errorMessage": t.string().optional(),
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementSyncErrorOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ConfigManagementPolicyControllerIn"] = t.struct(
        {
            "monitoring": t.proxy(
                renames["ConfigManagementPolicyControllerMonitoringIn"]
            ).optional(),
            "enabled": t.boolean().optional(),
            "mutationEnabled": t.boolean().optional(),
            "auditIntervalSeconds": t.string().optional(),
            "referentialRulesEnabled": t.boolean().optional(),
            "templateLibraryInstalled": t.boolean().optional(),
            "exemptableNamespaces": t.array(t.string()).optional(),
            "logDeniesEnabled": t.boolean().optional(),
        }
    ).named(renames["ConfigManagementPolicyControllerIn"])
    types["ConfigManagementPolicyControllerOut"] = t.struct(
        {
            "monitoring": t.proxy(
                renames["ConfigManagementPolicyControllerMonitoringOut"]
            ).optional(),
            "enabled": t.boolean().optional(),
            "mutationEnabled": t.boolean().optional(),
            "auditIntervalSeconds": t.string().optional(),
            "referentialRulesEnabled": t.boolean().optional(),
            "templateLibraryInstalled": t.boolean().optional(),
            "exemptableNamespaces": t.array(t.string()).optional(),
            "logDeniesEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementPolicyControllerOut"])
    types["LocationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["ConfigManagementGatekeeperDeploymentStateIn"] = t.struct(
        {
            "gatekeeperMutation": t.string().optional(),
            "gatekeeperControllerManagerState": t.string().optional(),
            "gatekeeperAudit": t.string().optional(),
        }
    ).named(renames["ConfigManagementGatekeeperDeploymentStateIn"])
    types["ConfigManagementGatekeeperDeploymentStateOut"] = t.struct(
        {
            "gatekeeperMutation": t.string().optional(),
            "gatekeeperControllerManagerState": t.string().optional(),
            "gatekeeperAudit": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementGatekeeperDeploymentStateOut"])
    types["FleetObservabilityFeatureStateIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["FleetObservabilityFeatureStateIn"])
    types["FleetObservabilityFeatureStateOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["FleetObservabilityFeatureStateOut"])
    types["CommonFeatureSpecIn"] = t.struct(
        {
            "fleetobservability": t.proxy(
                renames["FleetObservabilityFeatureSpecIn"]
            ).optional(),
            "multiclusteringress": t.proxy(
                renames["MultiClusterIngressFeatureSpecIn"]
            ).optional(),
            "appdevexperience": t.proxy(
                renames["AppDevExperienceFeatureSpecIn"]
            ).optional(),
        }
    ).named(renames["CommonFeatureSpecIn"])
    types["CommonFeatureSpecOut"] = t.struct(
        {
            "fleetobservability": t.proxy(
                renames["FleetObservabilityFeatureSpecOut"]
            ).optional(),
            "multiclusteringress": t.proxy(
                renames["MultiClusterIngressFeatureSpecOut"]
            ).optional(),
            "appdevexperience": t.proxy(
                renames["AppDevExperienceFeatureSpecOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommonFeatureSpecOut"])
    types["ConfigManagementConfigSyncDeploymentStateIn"] = t.struct(
        {
            "syncer": t.string().optional(),
            "admissionWebhook": t.string().optional(),
            "rootReconciler": t.string().optional(),
            "gitSync": t.string().optional(),
            "reconcilerManager": t.string().optional(),
            "monitor": t.string().optional(),
            "importer": t.string().optional(),
        }
    ).named(renames["ConfigManagementConfigSyncDeploymentStateIn"])
    types["ConfigManagementConfigSyncDeploymentStateOut"] = t.struct(
        {
            "syncer": t.string().optional(),
            "admissionWebhook": t.string().optional(),
            "rootReconciler": t.string().optional(),
            "gitSync": t.string().optional(),
            "reconcilerManager": t.string().optional(),
            "monitor": t.string().optional(),
            "importer": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementConfigSyncDeploymentStateOut"])
    types["MultiClusterIngressFeatureSpecIn"] = t.struct(
        {"configMembership": t.string().optional()}
    ).named(renames["MultiClusterIngressFeatureSpecIn"])
    types["MultiClusterIngressFeatureSpecOut"] = t.struct(
        {
            "configMembership": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MultiClusterIngressFeatureSpecOut"])
    types["ResourceOptionsIn"] = t.struct(
        {
            "connectVersion": t.string().optional(),
            "k8sVersion": t.string().optional(),
            "v1beta1Crd": t.boolean().optional(),
        }
    ).named(renames["ResourceOptionsIn"])
    types["ResourceOptionsOut"] = t.struct(
        {
            "connectVersion": t.string().optional(),
            "k8sVersion": t.string().optional(),
            "v1beta1Crd": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceOptionsOut"])

    functions = {}
    functions["projectsLocationsList"] = gkehub.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = gkehub.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsScopesList"] = gkehub.post(
        "v1/{parent}/scopes",
        t.struct(
            {
                "scopeId": t.string(),
                "parent": t.string(),
                "name": t.string().optional(),
                "allMemberships": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsScopesGet"] = gkehub.post(
        "v1/{parent}/scopes",
        t.struct(
            {
                "scopeId": t.string(),
                "parent": t.string(),
                "name": t.string().optional(),
                "allMemberships": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsScopesDelete"] = gkehub.post(
        "v1/{parent}/scopes",
        t.struct(
            {
                "scopeId": t.string(),
                "parent": t.string(),
                "name": t.string().optional(),
                "allMemberships": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsScopesCreate"] = gkehub.post(
        "v1/{parent}/scopes",
        t.struct(
            {
                "scopeId": t.string(),
                "parent": t.string(),
                "name": t.string().optional(),
                "allMemberships": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFeaturesPatch"] = gkehub.post(
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
    functions["projectsLocationsFeaturesSetIamPolicy"] = gkehub.post(
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
    functions["projectsLocationsFeaturesCreate"] = gkehub.post(
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
    functions["projectsLocationsFeaturesList"] = gkehub.post(
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
    functions["projectsLocationsFeaturesGetIamPolicy"] = gkehub.post(
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
    functions["projectsLocationsFeaturesDelete"] = gkehub.post(
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
    functions["projectsLocationsFeaturesGet"] = gkehub.post(
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
    functions["projectsLocationsFeaturesTestIamPermissions"] = gkehub.post(
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
    functions["projectsLocationsMembershipsTestIamPermissions"] = gkehub.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMembershipsList"] = gkehub.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMembershipsGenerateConnectManifest"] = gkehub.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMembershipsGetIamPolicy"] = gkehub.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMembershipsGet"] = gkehub.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMembershipsPatch"] = gkehub.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMembershipsCreate"] = gkehub.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMembershipsDelete"] = gkehub.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMembershipsSetIamPolicy"] = gkehub.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMembershipsBindingsPatch"] = gkehub.get(
        "v1/{parent}/bindings",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMembershipBindingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMembershipsBindingsDelete"] = gkehub.get(
        "v1/{parent}/bindings",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMembershipBindingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMembershipsBindingsGet"] = gkehub.get(
        "v1/{parent}/bindings",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMembershipBindingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMembershipsBindingsCreate"] = gkehub.get(
        "v1/{parent}/bindings",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMembershipBindingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMembershipsBindingsList"] = gkehub.get(
        "v1/{parent}/bindings",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMembershipBindingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = gkehub.post(
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
    functions["projectsLocationsOperationsDelete"] = gkehub.post(
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
    functions["projectsLocationsOperationsGet"] = gkehub.post(
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
    functions["projectsLocationsOperationsCancel"] = gkehub.post(
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

    return Import(importer="gkehub", renames=renames, types=types, functions=functions)
