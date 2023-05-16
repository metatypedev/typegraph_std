from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_gkehub() -> Import:
    gkehub = HTTPRuntime("https://gkehub.googleapis.com/")

    renames = {
        "ErrorResponse": "_gkehub_1_ErrorResponse",
        "ApplianceClusterIn": "_gkehub_2_ApplianceClusterIn",
        "ApplianceClusterOut": "_gkehub_3_ApplianceClusterOut",
        "MembershipFeatureSpecIn": "_gkehub_4_MembershipFeatureSpecIn",
        "MembershipFeatureSpecOut": "_gkehub_5_MembershipFeatureSpecOut",
        "IdentityServiceGoogleConfigIn": "_gkehub_6_IdentityServiceGoogleConfigIn",
        "IdentityServiceGoogleConfigOut": "_gkehub_7_IdentityServiceGoogleConfigOut",
        "ExprIn": "_gkehub_8_ExprIn",
        "ExprOut": "_gkehub_9_ExprOut",
        "ServiceMeshStatusDetailsIn": "_gkehub_10_ServiceMeshStatusDetailsIn",
        "ServiceMeshStatusDetailsOut": "_gkehub_11_ServiceMeshStatusDetailsOut",
        "ConfigManagementMembershipStateIn": "_gkehub_12_ConfigManagementMembershipStateIn",
        "ConfigManagementMembershipStateOut": "_gkehub_13_ConfigManagementMembershipStateOut",
        "ConfigManagementGatekeeperDeploymentStateIn": "_gkehub_14_ConfigManagementGatekeeperDeploymentStateIn",
        "ConfigManagementGatekeeperDeploymentStateOut": "_gkehub_15_ConfigManagementGatekeeperDeploymentStateOut",
        "AppDevExperienceFeatureSpecIn": "_gkehub_16_AppDevExperienceFeatureSpecIn",
        "AppDevExperienceFeatureSpecOut": "_gkehub_17_AppDevExperienceFeatureSpecOut",
        "GkeClusterIn": "_gkehub_18_GkeClusterIn",
        "GkeClusterOut": "_gkehub_19_GkeClusterOut",
        "ConfigManagementGroupVersionKindIn": "_gkehub_20_ConfigManagementGroupVersionKindIn",
        "ConfigManagementGroupVersionKindOut": "_gkehub_21_ConfigManagementGroupVersionKindOut",
        "ConfigManagementConfigSyncDeploymentStateIn": "_gkehub_22_ConfigManagementConfigSyncDeploymentStateIn",
        "ConfigManagementConfigSyncDeploymentStateOut": "_gkehub_23_ConfigManagementConfigSyncDeploymentStateOut",
        "ConfigManagementGitConfigIn": "_gkehub_24_ConfigManagementGitConfigIn",
        "ConfigManagementGitConfigOut": "_gkehub_25_ConfigManagementGitConfigOut",
        "MultiClusterIngressFeatureSpecIn": "_gkehub_26_MultiClusterIngressFeatureSpecIn",
        "MultiClusterIngressFeatureSpecOut": "_gkehub_27_MultiClusterIngressFeatureSpecOut",
        "TestIamPermissionsRequestIn": "_gkehub_28_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_gkehub_29_TestIamPermissionsRequestOut",
        "ConfigManagementHierarchyControllerConfigIn": "_gkehub_30_ConfigManagementHierarchyControllerConfigIn",
        "ConfigManagementHierarchyControllerConfigOut": "_gkehub_31_ConfigManagementHierarchyControllerConfigOut",
        "FeatureStateIn": "_gkehub_32_FeatureStateIn",
        "FeatureStateOut": "_gkehub_33_FeatureStateOut",
        "FleetObservabilityMembershipStateIn": "_gkehub_34_FleetObservabilityMembershipStateIn",
        "FleetObservabilityMembershipStateOut": "_gkehub_35_FleetObservabilityMembershipStateOut",
        "ServiceMeshDataPlaneManagementIn": "_gkehub_36_ServiceMeshDataPlaneManagementIn",
        "ServiceMeshDataPlaneManagementOut": "_gkehub_37_ServiceMeshDataPlaneManagementOut",
        "AuditLogConfigIn": "_gkehub_38_AuditLogConfigIn",
        "AuditLogConfigOut": "_gkehub_39_AuditLogConfigOut",
        "MembershipBindingIn": "_gkehub_40_MembershipBindingIn",
        "MembershipBindingOut": "_gkehub_41_MembershipBindingOut",
        "IdentityServiceAuthMethodIn": "_gkehub_42_IdentityServiceAuthMethodIn",
        "IdentityServiceAuthMethodOut": "_gkehub_43_IdentityServiceAuthMethodOut",
        "CommonFeatureSpecIn": "_gkehub_44_CommonFeatureSpecIn",
        "CommonFeatureSpecOut": "_gkehub_45_CommonFeatureSpecOut",
        "LocationIn": "_gkehub_46_LocationIn",
        "LocationOut": "_gkehub_47_LocationOut",
        "TypeMetaIn": "_gkehub_48_TypeMetaIn",
        "TypeMetaOut": "_gkehub_49_TypeMetaOut",
        "ServiceMeshMembershipStateIn": "_gkehub_50_ServiceMeshMembershipStateIn",
        "ServiceMeshMembershipStateOut": "_gkehub_51_ServiceMeshMembershipStateOut",
        "ConfigManagementPolicyControllerMonitoringIn": "_gkehub_52_ConfigManagementPolicyControllerMonitoringIn",
        "ConfigManagementPolicyControllerMonitoringOut": "_gkehub_53_ConfigManagementPolicyControllerMonitoringOut",
        "MembershipIn": "_gkehub_54_MembershipIn",
        "MembershipOut": "_gkehub_55_MembershipOut",
        "EmptyIn": "_gkehub_56_EmptyIn",
        "EmptyOut": "_gkehub_57_EmptyOut",
        "ConnectAgentResourceIn": "_gkehub_58_ConnectAgentResourceIn",
        "ConnectAgentResourceOut": "_gkehub_59_ConnectAgentResourceOut",
        "SetIamPolicyRequestIn": "_gkehub_60_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_gkehub_61_SetIamPolicyRequestOut",
        "FleetObservabilityFeatureSpecIn": "_gkehub_62_FleetObservabilityFeatureSpecIn",
        "FleetObservabilityFeatureSpecOut": "_gkehub_63_FleetObservabilityFeatureSpecOut",
        "AuditConfigIn": "_gkehub_64_AuditConfigIn",
        "AuditConfigOut": "_gkehub_65_AuditConfigOut",
        "MembershipBindingLifecycleStateIn": "_gkehub_66_MembershipBindingLifecycleStateIn",
        "MembershipBindingLifecycleStateOut": "_gkehub_67_MembershipBindingLifecycleStateOut",
        "CommonFeatureStateIn": "_gkehub_68_CommonFeatureStateIn",
        "CommonFeatureStateOut": "_gkehub_69_CommonFeatureStateOut",
        "MembershipStateIn": "_gkehub_70_MembershipStateIn",
        "MembershipStateOut": "_gkehub_71_MembershipStateOut",
        "MembershipEndpointIn": "_gkehub_72_MembershipEndpointIn",
        "MembershipEndpointOut": "_gkehub_73_MembershipEndpointOut",
        "ConfigManagementPolicyControllerStateIn": "_gkehub_74_ConfigManagementPolicyControllerStateIn",
        "ConfigManagementPolicyControllerStateOut": "_gkehub_75_ConfigManagementPolicyControllerStateOut",
        "IdentityServiceMembershipStateIn": "_gkehub_76_IdentityServiceMembershipStateIn",
        "IdentityServiceMembershipStateOut": "_gkehub_77_IdentityServiceMembershipStateOut",
        "GenerateConnectManifestResponseIn": "_gkehub_78_GenerateConnectManifestResponseIn",
        "GenerateConnectManifestResponseOut": "_gkehub_79_GenerateConnectManifestResponseOut",
        "AppDevExperienceFeatureStateIn": "_gkehub_80_AppDevExperienceFeatureStateIn",
        "AppDevExperienceFeatureStateOut": "_gkehub_81_AppDevExperienceFeatureStateOut",
        "KubernetesResourceIn": "_gkehub_82_KubernetesResourceIn",
        "KubernetesResourceOut": "_gkehub_83_KubernetesResourceOut",
        "ScopeIn": "_gkehub_84_ScopeIn",
        "ScopeOut": "_gkehub_85_ScopeOut",
        "AuthorityIn": "_gkehub_86_AuthorityIn",
        "AuthorityOut": "_gkehub_87_AuthorityOut",
        "ScopeFeatureStateIn": "_gkehub_88_ScopeFeatureStateIn",
        "ScopeFeatureStateOut": "_gkehub_89_ScopeFeatureStateOut",
        "ServiceMeshControlPlaneManagementIn": "_gkehub_90_ServiceMeshControlPlaneManagementIn",
        "ServiceMeshControlPlaneManagementOut": "_gkehub_91_ServiceMeshControlPlaneManagementOut",
        "ConfigManagementHierarchyControllerDeploymentStateIn": "_gkehub_92_ConfigManagementHierarchyControllerDeploymentStateIn",
        "ConfigManagementHierarchyControllerDeploymentStateOut": "_gkehub_93_ConfigManagementHierarchyControllerDeploymentStateOut",
        "OperationIn": "_gkehub_94_OperationIn",
        "OperationOut": "_gkehub_95_OperationOut",
        "FeatureIn": "_gkehub_96_FeatureIn",
        "FeatureOut": "_gkehub_97_FeatureOut",
        "TestIamPermissionsResponseIn": "_gkehub_98_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_gkehub_99_TestIamPermissionsResponseOut",
        "ListOperationsResponseIn": "_gkehub_100_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_gkehub_101_ListOperationsResponseOut",
        "PolicyIn": "_gkehub_102_PolicyIn",
        "PolicyOut": "_gkehub_103_PolicyOut",
        "ConfigManagementConfigSyncVersionIn": "_gkehub_104_ConfigManagementConfigSyncVersionIn",
        "ConfigManagementConfigSyncVersionOut": "_gkehub_105_ConfigManagementConfigSyncVersionOut",
        "ScopeFeatureSpecIn": "_gkehub_106_ScopeFeatureSpecIn",
        "ScopeFeatureSpecOut": "_gkehub_107_ScopeFeatureSpecOut",
        "ConfigManagementSyncErrorIn": "_gkehub_108_ConfigManagementSyncErrorIn",
        "ConfigManagementSyncErrorOut": "_gkehub_109_ConfigManagementSyncErrorOut",
        "ConfigManagementPolicyControllerVersionIn": "_gkehub_110_ConfigManagementPolicyControllerVersionIn",
        "ConfigManagementPolicyControllerVersionOut": "_gkehub_111_ConfigManagementPolicyControllerVersionOut",
        "ConfigManagementConfigSyncIn": "_gkehub_112_ConfigManagementConfigSyncIn",
        "ConfigManagementConfigSyncOut": "_gkehub_113_ConfigManagementConfigSyncOut",
        "ScopeLifecycleStateIn": "_gkehub_114_ScopeLifecycleStateIn",
        "ScopeLifecycleStateOut": "_gkehub_115_ScopeLifecycleStateOut",
        "GoogleRpcStatusIn": "_gkehub_116_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_gkehub_117_GoogleRpcStatusOut",
        "ConfigManagementManagedIn": "_gkehub_118_ConfigManagementManagedIn",
        "ConfigManagementManagedOut": "_gkehub_119_ConfigManagementManagedOut",
        "FeatureResourceStateIn": "_gkehub_120_FeatureResourceStateIn",
        "FeatureResourceStateOut": "_gkehub_121_FeatureResourceStateOut",
        "CancelOperationRequestIn": "_gkehub_122_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_gkehub_123_CancelOperationRequestOut",
        "ConfigManagementMembershipSpecIn": "_gkehub_124_ConfigManagementMembershipSpecIn",
        "ConfigManagementMembershipSpecOut": "_gkehub_125_ConfigManagementMembershipSpecOut",
        "ConfigManagementConfigSyncStateIn": "_gkehub_126_ConfigManagementConfigSyncStateIn",
        "ConfigManagementConfigSyncStateOut": "_gkehub_127_ConfigManagementConfigSyncStateOut",
        "BindingIn": "_gkehub_128_BindingIn",
        "BindingOut": "_gkehub_129_BindingOut",
        "OnPremClusterIn": "_gkehub_130_OnPremClusterIn",
        "OnPremClusterOut": "_gkehub_131_OnPremClusterOut",
        "IdentityServiceMembershipSpecIn": "_gkehub_132_IdentityServiceMembershipSpecIn",
        "IdentityServiceMembershipSpecOut": "_gkehub_133_IdentityServiceMembershipSpecOut",
        "ResourceOptionsIn": "_gkehub_134_ResourceOptionsIn",
        "ResourceOptionsOut": "_gkehub_135_ResourceOptionsOut",
        "ConfigManagementPolicyControllerIn": "_gkehub_136_ConfigManagementPolicyControllerIn",
        "ConfigManagementPolicyControllerOut": "_gkehub_137_ConfigManagementPolicyControllerOut",
        "ListMembershipsResponseIn": "_gkehub_138_ListMembershipsResponseIn",
        "ListMembershipsResponseOut": "_gkehub_139_ListMembershipsResponseOut",
        "ListMembershipBindingsResponseIn": "_gkehub_140_ListMembershipBindingsResponseIn",
        "ListMembershipBindingsResponseOut": "_gkehub_141_ListMembershipBindingsResponseOut",
        "ConfigManagementInstallErrorIn": "_gkehub_142_ConfigManagementInstallErrorIn",
        "ConfigManagementInstallErrorOut": "_gkehub_143_ConfigManagementInstallErrorOut",
        "ConfigManagementSyncStateIn": "_gkehub_144_ConfigManagementSyncStateIn",
        "ConfigManagementSyncStateOut": "_gkehub_145_ConfigManagementSyncStateOut",
        "ConfigManagementHierarchyControllerVersionIn": "_gkehub_146_ConfigManagementHierarchyControllerVersionIn",
        "ConfigManagementHierarchyControllerVersionOut": "_gkehub_147_ConfigManagementHierarchyControllerVersionOut",
        "ConfigManagementOperatorStateIn": "_gkehub_148_ConfigManagementOperatorStateIn",
        "ConfigManagementOperatorStateOut": "_gkehub_149_ConfigManagementOperatorStateOut",
        "ListLocationsResponseIn": "_gkehub_150_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_gkehub_151_ListLocationsResponseOut",
        "StatusIn": "_gkehub_152_StatusIn",
        "StatusOut": "_gkehub_153_StatusOut",
        "CommonFleetDefaultMemberConfigSpecIn": "_gkehub_154_CommonFleetDefaultMemberConfigSpecIn",
        "CommonFleetDefaultMemberConfigSpecOut": "_gkehub_155_CommonFleetDefaultMemberConfigSpecOut",
        "ConfigManagementErrorResourceIn": "_gkehub_156_ConfigManagementErrorResourceIn",
        "ConfigManagementErrorResourceOut": "_gkehub_157_ConfigManagementErrorResourceOut",
        "ServiceMeshMembershipSpecIn": "_gkehub_158_ServiceMeshMembershipSpecIn",
        "ServiceMeshMembershipSpecOut": "_gkehub_159_ServiceMeshMembershipSpecOut",
        "IdentityServiceAzureADConfigIn": "_gkehub_160_IdentityServiceAzureADConfigIn",
        "IdentityServiceAzureADConfigOut": "_gkehub_161_IdentityServiceAzureADConfigOut",
        "ListFeaturesResponseIn": "_gkehub_162_ListFeaturesResponseIn",
        "ListFeaturesResponseOut": "_gkehub_163_ListFeaturesResponseOut",
        "ListScopesResponseIn": "_gkehub_164_ListScopesResponseIn",
        "ListScopesResponseOut": "_gkehub_165_ListScopesResponseOut",
        "MonitoringConfigIn": "_gkehub_166_MonitoringConfigIn",
        "MonitoringConfigOut": "_gkehub_167_MonitoringConfigOut",
        "EdgeClusterIn": "_gkehub_168_EdgeClusterIn",
        "EdgeClusterOut": "_gkehub_169_EdgeClusterOut",
        "KubernetesMetadataIn": "_gkehub_170_KubernetesMetadataIn",
        "KubernetesMetadataOut": "_gkehub_171_KubernetesMetadataOut",
        "FleetObservabilityMembershipSpecIn": "_gkehub_172_FleetObservabilityMembershipSpecIn",
        "FleetObservabilityMembershipSpecOut": "_gkehub_173_FleetObservabilityMembershipSpecOut",
        "MultiCloudClusterIn": "_gkehub_174_MultiCloudClusterIn",
        "MultiCloudClusterOut": "_gkehub_175_MultiCloudClusterOut",
        "ConfigManagementHierarchyControllerStateIn": "_gkehub_176_ConfigManagementHierarchyControllerStateIn",
        "ConfigManagementHierarchyControllerStateOut": "_gkehub_177_ConfigManagementHierarchyControllerStateOut",
        "FleetObservabilityFeatureStateIn": "_gkehub_178_FleetObservabilityFeatureStateIn",
        "FleetObservabilityFeatureStateOut": "_gkehub_179_FleetObservabilityFeatureStateOut",
        "ResourceManifestIn": "_gkehub_180_ResourceManifestIn",
        "ResourceManifestOut": "_gkehub_181_ResourceManifestOut",
        "ConfigManagementPolicyControllerMigrationIn": "_gkehub_182_ConfigManagementPolicyControllerMigrationIn",
        "ConfigManagementPolicyControllerMigrationOut": "_gkehub_183_ConfigManagementPolicyControllerMigrationOut",
        "ConfigManagementOciConfigIn": "_gkehub_184_ConfigManagementOciConfigIn",
        "ConfigManagementOciConfigOut": "_gkehub_185_ConfigManagementOciConfigOut",
        "MembershipFeatureStateIn": "_gkehub_186_MembershipFeatureStateIn",
        "MembershipFeatureStateOut": "_gkehub_187_MembershipFeatureStateOut",
        "OperationMetadataIn": "_gkehub_188_OperationMetadataIn",
        "OperationMetadataOut": "_gkehub_189_OperationMetadataOut",
        "IdentityServiceOidcConfigIn": "_gkehub_190_IdentityServiceOidcConfigIn",
        "IdentityServiceOidcConfigOut": "_gkehub_191_IdentityServiceOidcConfigOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ApplianceClusterIn"] = t.struct(
        {"resourceLink": t.string().optional()}
    ).named(renames["ApplianceClusterIn"])
    types["ApplianceClusterOut"] = t.struct(
        {
            "resourceLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplianceClusterOut"])
    types["MembershipFeatureSpecIn"] = t.struct(
        {
            "identityservice": t.proxy(
                renames["IdentityServiceMembershipSpecIn"]
            ).optional(),
            "fleetobservability": t.proxy(
                renames["FleetObservabilityMembershipSpecIn"]
            ).optional(),
            "fleetInherited": t.boolean().optional(),
            "configmanagement": t.proxy(
                renames["ConfigManagementMembershipSpecIn"]
            ).optional(),
            "mesh": t.proxy(renames["ServiceMeshMembershipSpecIn"]).optional(),
        }
    ).named(renames["MembershipFeatureSpecIn"])
    types["MembershipFeatureSpecOut"] = t.struct(
        {
            "identityservice": t.proxy(
                renames["IdentityServiceMembershipSpecOut"]
            ).optional(),
            "fleetobservability": t.proxy(
                renames["FleetObservabilityMembershipSpecOut"]
            ).optional(),
            "fleetInherited": t.boolean().optional(),
            "configmanagement": t.proxy(
                renames["ConfigManagementMembershipSpecOut"]
            ).optional(),
            "mesh": t.proxy(renames["ServiceMeshMembershipSpecOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipFeatureSpecOut"])
    types["IdentityServiceGoogleConfigIn"] = t.struct(
        {"disable": t.boolean().optional()}
    ).named(renames["IdentityServiceGoogleConfigIn"])
    types["IdentityServiceGoogleConfigOut"] = t.struct(
        {
            "disable": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentityServiceGoogleConfigOut"])
    types["ExprIn"] = t.struct(
        {
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
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
    types["ConfigManagementMembershipStateIn"] = t.struct(
        {
            "hierarchyControllerState": t.proxy(
                renames["ConfigManagementHierarchyControllerStateIn"]
            ).optional(),
            "configSyncState": t.proxy(
                renames["ConfigManagementConfigSyncStateIn"]
            ).optional(),
            "policyControllerState": t.proxy(
                renames["ConfigManagementPolicyControllerStateIn"]
            ).optional(),
            "membershipSpec": t.proxy(
                renames["ConfigManagementMembershipSpecIn"]
            ).optional(),
            "clusterName": t.string().optional(),
            "operatorState": t.proxy(
                renames["ConfigManagementOperatorStateIn"]
            ).optional(),
        }
    ).named(renames["ConfigManagementMembershipStateIn"])
    types["ConfigManagementMembershipStateOut"] = t.struct(
        {
            "hierarchyControllerState": t.proxy(
                renames["ConfigManagementHierarchyControllerStateOut"]
            ).optional(),
            "configSyncState": t.proxy(
                renames["ConfigManagementConfigSyncStateOut"]
            ).optional(),
            "policyControllerState": t.proxy(
                renames["ConfigManagementPolicyControllerStateOut"]
            ).optional(),
            "membershipSpec": t.proxy(
                renames["ConfigManagementMembershipSpecOut"]
            ).optional(),
            "clusterName": t.string().optional(),
            "operatorState": t.proxy(
                renames["ConfigManagementOperatorStateOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementMembershipStateOut"])
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
    types["AppDevExperienceFeatureSpecIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AppDevExperienceFeatureSpecIn"])
    types["AppDevExperienceFeatureSpecOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AppDevExperienceFeatureSpecOut"])
    types["GkeClusterIn"] = t.struct({"resourceLink": t.string().optional()}).named(
        renames["GkeClusterIn"]
    )
    types["GkeClusterOut"] = t.struct(
        {
            "resourceLink": t.string().optional(),
            "clusterMissing": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GkeClusterOut"])
    types["ConfigManagementGroupVersionKindIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "group": t.string().optional(),
            "version": t.string().optional(),
        }
    ).named(renames["ConfigManagementGroupVersionKindIn"])
    types["ConfigManagementGroupVersionKindOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "group": t.string().optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementGroupVersionKindOut"])
    types["ConfigManagementConfigSyncDeploymentStateIn"] = t.struct(
        {
            "syncer": t.string().optional(),
            "importer": t.string().optional(),
            "rootReconciler": t.string().optional(),
            "reconcilerManager": t.string().optional(),
            "admissionWebhook": t.string().optional(),
            "monitor": t.string().optional(),
            "gitSync": t.string().optional(),
        }
    ).named(renames["ConfigManagementConfigSyncDeploymentStateIn"])
    types["ConfigManagementConfigSyncDeploymentStateOut"] = t.struct(
        {
            "syncer": t.string().optional(),
            "importer": t.string().optional(),
            "rootReconciler": t.string().optional(),
            "reconcilerManager": t.string().optional(),
            "admissionWebhook": t.string().optional(),
            "monitor": t.string().optional(),
            "gitSync": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementConfigSyncDeploymentStateOut"])
    types["ConfigManagementGitConfigIn"] = t.struct(
        {
            "syncRev": t.string().optional(),
            "secretType": t.string().optional(),
            "syncWaitSecs": t.string().optional(),
            "httpsProxy": t.string().optional(),
            "gcpServiceAccountEmail": t.string().optional(),
            "syncRepo": t.string().optional(),
            "policyDir": t.string().optional(),
            "syncBranch": t.string().optional(),
        }
    ).named(renames["ConfigManagementGitConfigIn"])
    types["ConfigManagementGitConfigOut"] = t.struct(
        {
            "syncRev": t.string().optional(),
            "secretType": t.string().optional(),
            "syncWaitSecs": t.string().optional(),
            "httpsProxy": t.string().optional(),
            "gcpServiceAccountEmail": t.string().optional(),
            "syncRepo": t.string().optional(),
            "policyDir": t.string().optional(),
            "syncBranch": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementGitConfigOut"])
    types["MultiClusterIngressFeatureSpecIn"] = t.struct(
        {"configMembership": t.string().optional()}
    ).named(renames["MultiClusterIngressFeatureSpecIn"])
    types["MultiClusterIngressFeatureSpecOut"] = t.struct(
        {
            "configMembership": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MultiClusterIngressFeatureSpecOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["ConfigManagementHierarchyControllerConfigIn"] = t.struct(
        {
            "enablePodTreeLabels": t.boolean().optional(),
            "enabled": t.boolean().optional(),
            "enableHierarchicalResourceQuota": t.boolean().optional(),
        }
    ).named(renames["ConfigManagementHierarchyControllerConfigIn"])
    types["ConfigManagementHierarchyControllerConfigOut"] = t.struct(
        {
            "enablePodTreeLabels": t.boolean().optional(),
            "enabled": t.boolean().optional(),
            "enableHierarchicalResourceQuota": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementHierarchyControllerConfigOut"])
    types["FeatureStateIn"] = t.struct(
        {
            "code": t.string().optional(),
            "updateTime": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["FeatureStateIn"])
    types["FeatureStateOut"] = t.struct(
        {
            "code": t.string().optional(),
            "updateTime": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FeatureStateOut"])
    types["FleetObservabilityMembershipStateIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["FleetObservabilityMembershipStateIn"])
    types["FleetObservabilityMembershipStateOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["FleetObservabilityMembershipStateOut"])
    types["ServiceMeshDataPlaneManagementIn"] = t.struct(
        {
            "state": t.string().optional(),
            "details": t.array(
                t.proxy(renames["ServiceMeshStatusDetailsIn"])
            ).optional(),
        }
    ).named(renames["ServiceMeshDataPlaneManagementIn"])
    types["ServiceMeshDataPlaneManagementOut"] = t.struct(
        {
            "state": t.string().optional(),
            "details": t.array(
                t.proxy(renames["ServiceMeshStatusDetailsOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceMeshDataPlaneManagementOut"])
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
    types["MembershipBindingIn"] = t.struct(
        {
            "name": t.string().optional(),
            "scope": t.string().optional(),
            "fleet": t.boolean().optional(),
        }
    ).named(renames["MembershipBindingIn"])
    types["MembershipBindingOut"] = t.struct(
        {
            "state": t.proxy(renames["MembershipBindingLifecycleStateOut"]).optional(),
            "deleteTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "uid": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "scope": t.string().optional(),
            "fleet": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipBindingOut"])
    types["IdentityServiceAuthMethodIn"] = t.struct(
        {
            "oidcConfig": t.proxy(renames["IdentityServiceOidcConfigIn"]).optional(),
            "googleConfig": t.proxy(
                renames["IdentityServiceGoogleConfigIn"]
            ).optional(),
            "azureadConfig": t.proxy(
                renames["IdentityServiceAzureADConfigIn"]
            ).optional(),
            "proxy": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["IdentityServiceAuthMethodIn"])
    types["IdentityServiceAuthMethodOut"] = t.struct(
        {
            "oidcConfig": t.proxy(renames["IdentityServiceOidcConfigOut"]).optional(),
            "googleConfig": t.proxy(
                renames["IdentityServiceGoogleConfigOut"]
            ).optional(),
            "azureadConfig": t.proxy(
                renames["IdentityServiceAzureADConfigOut"]
            ).optional(),
            "proxy": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentityServiceAuthMethodOut"])
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
    types["LocationIn"] = t.struct(
        {
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
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
    types["ConfigManagementPolicyControllerMonitoringIn"] = t.struct(
        {"backends": t.array(t.string()).optional()}
    ).named(renames["ConfigManagementPolicyControllerMonitoringIn"])
    types["ConfigManagementPolicyControllerMonitoringOut"] = t.struct(
        {
            "backends": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementPolicyControllerMonitoringOut"])
    types["MembershipIn"] = t.struct(
        {
            "endpoint": t.proxy(renames["MembershipEndpointIn"]).optional(),
            "externalId": t.string().optional(),
            "authority": t.proxy(renames["AuthorityIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "monitoringConfig": t.proxy(renames["MonitoringConfigIn"]).optional(),
        }
    ).named(renames["MembershipIn"])
    types["MembershipOut"] = t.struct(
        {
            "name": t.string().optional(),
            "endpoint": t.proxy(renames["MembershipEndpointOut"]).optional(),
            "lastConnectionTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "externalId": t.string().optional(),
            "deleteTime": t.string().optional(),
            "state": t.proxy(renames["MembershipStateOut"]).optional(),
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "uniqueId": t.string().optional(),
            "authority": t.proxy(renames["AuthorityOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "monitoringConfig": t.proxy(renames["MonitoringConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["FleetObservabilityFeatureSpecIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["FleetObservabilityFeatureSpecIn"])
    types["FleetObservabilityFeatureSpecOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["FleetObservabilityFeatureSpecOut"])
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
    types["MembershipBindingLifecycleStateIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["MembershipBindingLifecycleStateIn"])
    types["MembershipBindingLifecycleStateOut"] = t.struct(
        {
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipBindingLifecycleStateOut"])
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
    types["MembershipStateIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MembershipStateIn"]
    )
    types["MembershipStateOut"] = t.struct(
        {
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipStateOut"])
    types["MembershipEndpointIn"] = t.struct(
        {
            "gkeCluster": t.proxy(renames["GkeClusterIn"]).optional(),
            "applianceCluster": t.proxy(renames["ApplianceClusterIn"]).optional(),
            "edgeCluster": t.proxy(renames["EdgeClusterIn"]).optional(),
            "onPremCluster": t.proxy(renames["OnPremClusterIn"]).optional(),
            "multiCloudCluster": t.proxy(renames["MultiCloudClusterIn"]).optional(),
            "kubernetesResource": t.proxy(renames["KubernetesResourceIn"]).optional(),
        }
    ).named(renames["MembershipEndpointIn"])
    types["MembershipEndpointOut"] = t.struct(
        {
            "kubernetesMetadata": t.proxy(renames["KubernetesMetadataOut"]).optional(),
            "gkeCluster": t.proxy(renames["GkeClusterOut"]).optional(),
            "applianceCluster": t.proxy(renames["ApplianceClusterOut"]).optional(),
            "edgeCluster": t.proxy(renames["EdgeClusterOut"]).optional(),
            "googleManaged": t.boolean().optional(),
            "onPremCluster": t.proxy(renames["OnPremClusterOut"]).optional(),
            "multiCloudCluster": t.proxy(renames["MultiCloudClusterOut"]).optional(),
            "kubernetesResource": t.proxy(renames["KubernetesResourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipEndpointOut"])
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
    types["IdentityServiceMembershipStateIn"] = t.struct(
        {
            "failureReason": t.string().optional(),
            "memberConfig": t.proxy(
                renames["IdentityServiceMembershipSpecIn"]
            ).optional(),
            "installedVersion": t.string().optional(),
            "state": t.string().optional(),
        }
    ).named(renames["IdentityServiceMembershipStateIn"])
    types["IdentityServiceMembershipStateOut"] = t.struct(
        {
            "failureReason": t.string().optional(),
            "memberConfig": t.proxy(
                renames["IdentityServiceMembershipSpecOut"]
            ).optional(),
            "installedVersion": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentityServiceMembershipStateOut"])
    types["GenerateConnectManifestResponseIn"] = t.struct(
        {"manifest": t.array(t.proxy(renames["ConnectAgentResourceIn"])).optional()}
    ).named(renames["GenerateConnectManifestResponseIn"])
    types["GenerateConnectManifestResponseOut"] = t.struct(
        {
            "manifest": t.array(t.proxy(renames["ConnectAgentResourceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateConnectManifestResponseOut"])
    types["AppDevExperienceFeatureStateIn"] = t.struct(
        {"networkingInstallSucceeded": t.proxy(renames["StatusIn"]).optional()}
    ).named(renames["AppDevExperienceFeatureStateIn"])
    types["AppDevExperienceFeatureStateOut"] = t.struct(
        {
            "networkingInstallSucceeded": t.proxy(renames["StatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppDevExperienceFeatureStateOut"])
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
            "resourceOptions": t.proxy(renames["ResourceOptionsOut"]).optional(),
            "membershipCrManifest": t.string().optional(),
            "membershipResources": t.array(
                t.proxy(renames["ResourceManifestOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KubernetesResourceOut"])
    types["ScopeIn"] = t.struct(
        {"allMemberships": t.boolean().optional(), "name": t.string().optional()}
    ).named(renames["ScopeIn"])
    types["ScopeOut"] = t.struct(
        {
            "allMemberships": t.boolean().optional(),
            "state": t.proxy(renames["ScopeLifecycleStateOut"]).optional(),
            "deleteTime": t.string().optional(),
            "name": t.string().optional(),
            "uid": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScopeOut"])
    types["AuthorityIn"] = t.struct(
        {"issuer": t.string().optional(), "oidcJwks": t.string().optional()}
    ).named(renames["AuthorityIn"])
    types["AuthorityOut"] = t.struct(
        {
            "issuer": t.string().optional(),
            "oidcJwks": t.string().optional(),
            "workloadIdentityPool": t.string().optional(),
            "identityProvider": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthorityOut"])
    types["ScopeFeatureStateIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ScopeFeatureStateIn"]
    )
    types["ScopeFeatureStateOut"] = t.struct(
        {
            "state": t.proxy(renames["FeatureStateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScopeFeatureStateOut"])
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
    types["OperationIn"] = t.struct(
        {
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["FeatureIn"] = t.struct(
        {
            "membershipSpecs": t.struct({"_": t.string().optional()}).optional(),
            "spec": t.proxy(renames["CommonFeatureSpecIn"]).optional(),
            "fleetDefaultMemberConfig": t.proxy(
                renames["CommonFleetDefaultMemberConfigSpecIn"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "scopeSpecs": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["FeatureIn"])
    types["FeatureOut"] = t.struct(
        {
            "name": t.string().optional(),
            "state": t.proxy(renames["CommonFeatureStateOut"]).optional(),
            "createTime": t.string().optional(),
            "membershipSpecs": t.struct({"_": t.string().optional()}).optional(),
            "deleteTime": t.string().optional(),
            "membershipStates": t.struct({"_": t.string().optional()}).optional(),
            "spec": t.proxy(renames["CommonFeatureSpecOut"]).optional(),
            "fleetDefaultMemberConfig": t.proxy(
                renames["CommonFleetDefaultMemberConfigSpecOut"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "scopeSpecs": t.struct({"_": t.string().optional()}).optional(),
            "scopeStates": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "resourceState": t.proxy(renames["FeatureResourceStateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FeatureOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
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
    types["PolicyIn"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "etag": t.string().optional(),
            "version": t.integer().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["ConfigManagementConfigSyncVersionIn"] = t.struct(
        {
            "gitSync": t.string().optional(),
            "reconcilerManager": t.string().optional(),
            "syncer": t.string().optional(),
            "importer": t.string().optional(),
            "monitor": t.string().optional(),
            "admissionWebhook": t.string().optional(),
            "rootReconciler": t.string().optional(),
        }
    ).named(renames["ConfigManagementConfigSyncVersionIn"])
    types["ConfigManagementConfigSyncVersionOut"] = t.struct(
        {
            "gitSync": t.string().optional(),
            "reconcilerManager": t.string().optional(),
            "syncer": t.string().optional(),
            "importer": t.string().optional(),
            "monitor": t.string().optional(),
            "admissionWebhook": t.string().optional(),
            "rootReconciler": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementConfigSyncVersionOut"])
    types["ScopeFeatureSpecIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ScopeFeatureSpecIn"]
    )
    types["ScopeFeatureSpecOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ScopeFeatureSpecOut"])
    types["ConfigManagementSyncErrorIn"] = t.struct(
        {
            "errorMessage": t.string().optional(),
            "errorResources": t.array(
                t.proxy(renames["ConfigManagementErrorResourceIn"])
            ).optional(),
            "code": t.string().optional(),
        }
    ).named(renames["ConfigManagementSyncErrorIn"])
    types["ConfigManagementSyncErrorOut"] = t.struct(
        {
            "errorMessage": t.string().optional(),
            "errorResources": t.array(
                t.proxy(renames["ConfigManagementErrorResourceOut"])
            ).optional(),
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementSyncErrorOut"])
    types["ConfigManagementPolicyControllerVersionIn"] = t.struct(
        {"version": t.string().optional()}
    ).named(renames["ConfigManagementPolicyControllerVersionIn"])
    types["ConfigManagementPolicyControllerVersionOut"] = t.struct(
        {
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementPolicyControllerVersionOut"])
    types["ConfigManagementConfigSyncIn"] = t.struct(
        {
            "allowVerticalScale": t.boolean().optional(),
            "oci": t.proxy(renames["ConfigManagementOciConfigIn"]).optional(),
            "preventDrift": t.boolean().optional(),
            "managed": t.proxy(renames["ConfigManagementManagedIn"]).optional(),
            "git": t.proxy(renames["ConfigManagementGitConfigIn"]).optional(),
            "enabled": t.boolean().optional(),
            "sourceFormat": t.string().optional(),
        }
    ).named(renames["ConfigManagementConfigSyncIn"])
    types["ConfigManagementConfigSyncOut"] = t.struct(
        {
            "allowVerticalScale": t.boolean().optional(),
            "oci": t.proxy(renames["ConfigManagementOciConfigOut"]).optional(),
            "preventDrift": t.boolean().optional(),
            "managed": t.proxy(renames["ConfigManagementManagedOut"]).optional(),
            "git": t.proxy(renames["ConfigManagementGitConfigOut"]).optional(),
            "enabled": t.boolean().optional(),
            "sourceFormat": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementConfigSyncOut"])
    types["ScopeLifecycleStateIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ScopeLifecycleStateIn"]
    )
    types["ScopeLifecycleStateOut"] = t.struct(
        {
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScopeLifecycleStateOut"])
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
    types["ConfigManagementManagedIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["ConfigManagementManagedIn"])
    types["ConfigManagementManagedOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementManagedOut"])
    types["FeatureResourceStateIn"] = t.struct({"state": t.string().optional()}).named(
        renames["FeatureResourceStateIn"]
    )
    types["FeatureResourceStateOut"] = t.struct(
        {
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FeatureResourceStateOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["ConfigManagementMembershipSpecIn"] = t.struct(
        {
            "policyController": t.proxy(
                renames["ConfigManagementPolicyControllerIn"]
            ).optional(),
            "configSync": t.proxy(renames["ConfigManagementConfigSyncIn"]).optional(),
            "version": t.string().optional(),
            "hierarchyController": t.proxy(
                renames["ConfigManagementHierarchyControllerConfigIn"]
            ).optional(),
        }
    ).named(renames["ConfigManagementMembershipSpecIn"])
    types["ConfigManagementMembershipSpecOut"] = t.struct(
        {
            "policyController": t.proxy(
                renames["ConfigManagementPolicyControllerOut"]
            ).optional(),
            "configSync": t.proxy(renames["ConfigManagementConfigSyncOut"]).optional(),
            "version": t.string().optional(),
            "hierarchyController": t.proxy(
                renames["ConfigManagementHierarchyControllerConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementMembershipSpecOut"])
    types["ConfigManagementConfigSyncStateIn"] = t.struct(
        {
            "deploymentState": t.proxy(
                renames["ConfigManagementConfigSyncDeploymentStateIn"]
            ).optional(),
            "syncState": t.proxy(renames["ConfigManagementSyncStateIn"]).optional(),
            "version": t.proxy(
                renames["ConfigManagementConfigSyncVersionIn"]
            ).optional(),
        }
    ).named(renames["ConfigManagementConfigSyncStateIn"])
    types["ConfigManagementConfigSyncStateOut"] = t.struct(
        {
            "deploymentState": t.proxy(
                renames["ConfigManagementConfigSyncDeploymentStateOut"]
            ).optional(),
            "syncState": t.proxy(renames["ConfigManagementSyncStateOut"]).optional(),
            "version": t.proxy(
                renames["ConfigManagementConfigSyncVersionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementConfigSyncStateOut"])
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
    types["OnPremClusterIn"] = t.struct(
        {
            "adminCluster": t.boolean().optional(),
            "clusterType": t.string().optional(),
            "resourceLink": t.string().optional(),
        }
    ).named(renames["OnPremClusterIn"])
    types["OnPremClusterOut"] = t.struct(
        {
            "adminCluster": t.boolean().optional(),
            "clusterMissing": t.boolean().optional(),
            "clusterType": t.string().optional(),
            "resourceLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OnPremClusterOut"])
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
    types["ResourceOptionsIn"] = t.struct(
        {
            "connectVersion": t.string().optional(),
            "v1beta1Crd": t.boolean().optional(),
            "k8sVersion": t.string().optional(),
        }
    ).named(renames["ResourceOptionsIn"])
    types["ResourceOptionsOut"] = t.struct(
        {
            "connectVersion": t.string().optional(),
            "v1beta1Crd": t.boolean().optional(),
            "k8sVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceOptionsOut"])
    types["ConfigManagementPolicyControllerIn"] = t.struct(
        {
            "referentialRulesEnabled": t.boolean().optional(),
            "exemptableNamespaces": t.array(t.string()).optional(),
            "logDeniesEnabled": t.boolean().optional(),
            "monitoring": t.proxy(
                renames["ConfigManagementPolicyControllerMonitoringIn"]
            ).optional(),
            "templateLibraryInstalled": t.boolean().optional(),
            "enabled": t.boolean().optional(),
            "auditIntervalSeconds": t.string().optional(),
            "mutationEnabled": t.boolean().optional(),
        }
    ).named(renames["ConfigManagementPolicyControllerIn"])
    types["ConfigManagementPolicyControllerOut"] = t.struct(
        {
            "referentialRulesEnabled": t.boolean().optional(),
            "exemptableNamespaces": t.array(t.string()).optional(),
            "logDeniesEnabled": t.boolean().optional(),
            "monitoring": t.proxy(
                renames["ConfigManagementPolicyControllerMonitoringOut"]
            ).optional(),
            "templateLibraryInstalled": t.boolean().optional(),
            "enabled": t.boolean().optional(),
            "auditIntervalSeconds": t.string().optional(),
            "mutationEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementPolicyControllerOut"])
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
    types["ConfigManagementInstallErrorIn"] = t.struct(
        {"errorMessage": t.string().optional()}
    ).named(renames["ConfigManagementInstallErrorIn"])
    types["ConfigManagementInstallErrorOut"] = t.struct(
        {
            "errorMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementInstallErrorOut"])
    types["ConfigManagementSyncStateIn"] = t.struct(
        {
            "sourceToken": t.string().optional(),
            "lastSync": t.string().optional(),
            "code": t.string().optional(),
            "errors": t.array(
                t.proxy(renames["ConfigManagementSyncErrorIn"])
            ).optional(),
            "importToken": t.string().optional(),
            "syncToken": t.string().optional(),
            "lastSyncTime": t.string().optional(),
        }
    ).named(renames["ConfigManagementSyncStateIn"])
    types["ConfigManagementSyncStateOut"] = t.struct(
        {
            "sourceToken": t.string().optional(),
            "lastSync": t.string().optional(),
            "code": t.string().optional(),
            "errors": t.array(
                t.proxy(renames["ConfigManagementSyncErrorOut"])
            ).optional(),
            "importToken": t.string().optional(),
            "syncToken": t.string().optional(),
            "lastSyncTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementSyncStateOut"])
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
    types["ConfigManagementErrorResourceIn"] = t.struct(
        {
            "sourcePath": t.string().optional(),
            "resourceName": t.string().optional(),
            "resourceGvk": t.proxy(
                renames["ConfigManagementGroupVersionKindIn"]
            ).optional(),
            "resourceNamespace": t.string().optional(),
        }
    ).named(renames["ConfigManagementErrorResourceIn"])
    types["ConfigManagementErrorResourceOut"] = t.struct(
        {
            "sourcePath": t.string().optional(),
            "resourceName": t.string().optional(),
            "resourceGvk": t.proxy(
                renames["ConfigManagementGroupVersionKindOut"]
            ).optional(),
            "resourceNamespace": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementErrorResourceOut"])
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
            "encryptedClientSecret": t.string().optional(),
            "clientSecret": t.string().optional(),
            "kubectlRedirectUri": t.string().optional(),
            "tenant": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentityServiceAzureADConfigOut"])
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
    types["MonitoringConfigIn"] = t.struct(
        {
            "cluster": t.string().optional(),
            "kubernetesMetricsPrefix": t.string().optional(),
            "projectId": t.string().optional(),
            "clusterHash": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["MonitoringConfigIn"])
    types["MonitoringConfigOut"] = t.struct(
        {
            "cluster": t.string().optional(),
            "kubernetesMetricsPrefix": t.string().optional(),
            "projectId": t.string().optional(),
            "clusterHash": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MonitoringConfigOut"])
    types["EdgeClusterIn"] = t.struct({"resourceLink": t.string().optional()}).named(
        renames["EdgeClusterIn"]
    )
    types["EdgeClusterOut"] = t.struct(
        {
            "resourceLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EdgeClusterOut"])
    types["KubernetesMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["KubernetesMetadataIn"]
    )
    types["KubernetesMetadataOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "vcpuCount": t.integer().optional(),
            "nodeCount": t.integer().optional(),
            "nodeProviderId": t.string().optional(),
            "kubernetesApiServerVersion": t.string().optional(),
            "memoryMb": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KubernetesMetadataOut"])
    types["FleetObservabilityMembershipSpecIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["FleetObservabilityMembershipSpecIn"])
    types["FleetObservabilityMembershipSpecOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["FleetObservabilityMembershipSpecOut"])
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
    types["FleetObservabilityFeatureStateIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["FleetObservabilityFeatureStateIn"])
    types["FleetObservabilityFeatureStateOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["FleetObservabilityFeatureStateOut"])
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
    types["ConfigManagementPolicyControllerMigrationIn"] = t.struct(
        {"stage": t.string().optional()}
    ).named(renames["ConfigManagementPolicyControllerMigrationIn"])
    types["ConfigManagementPolicyControllerMigrationOut"] = t.struct(
        {
            "stage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementPolicyControllerMigrationOut"])
    types["ConfigManagementOciConfigIn"] = t.struct(
        {
            "gcpServiceAccountEmail": t.string().optional(),
            "syncWaitSecs": t.string().optional(),
            "syncRepo": t.string().optional(),
            "secretType": t.string().optional(),
            "policyDir": t.string().optional(),
        }
    ).named(renames["ConfigManagementOciConfigIn"])
    types["ConfigManagementOciConfigOut"] = t.struct(
        {
            "gcpServiceAccountEmail": t.string().optional(),
            "syncWaitSecs": t.string().optional(),
            "syncRepo": t.string().optional(),
            "secretType": t.string().optional(),
            "policyDir": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigManagementOciConfigOut"])
    types["MembershipFeatureStateIn"] = t.struct(
        {
            "servicemesh": t.proxy(renames["ServiceMeshMembershipStateIn"]).optional(),
            "state": t.proxy(renames["FeatureStateIn"]).optional(),
            "appdevexperience": t.proxy(
                renames["AppDevExperienceFeatureStateIn"]
            ).optional(),
            "fleetobservability": t.proxy(
                renames["FleetObservabilityMembershipStateIn"]
            ).optional(),
            "identityservice": t.proxy(
                renames["IdentityServiceMembershipStateIn"]
            ).optional(),
            "configmanagement": t.proxy(
                renames["ConfigManagementMembershipStateIn"]
            ).optional(),
        }
    ).named(renames["MembershipFeatureStateIn"])
    types["MembershipFeatureStateOut"] = t.struct(
        {
            "servicemesh": t.proxy(renames["ServiceMeshMembershipStateOut"]).optional(),
            "state": t.proxy(renames["FeatureStateOut"]).optional(),
            "appdevexperience": t.proxy(
                renames["AppDevExperienceFeatureStateOut"]
            ).optional(),
            "fleetobservability": t.proxy(
                renames["FleetObservabilityMembershipStateOut"]
            ).optional(),
            "identityservice": t.proxy(
                renames["IdentityServiceMembershipStateOut"]
            ).optional(),
            "configmanagement": t.proxy(
                renames["ConfigManagementMembershipStateOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipFeatureStateOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "target": t.string().optional(),
            "apiVersion": t.string().optional(),
            "statusDetail": t.string().optional(),
            "endTime": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "verb": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["IdentityServiceOidcConfigIn"] = t.struct(
        {
            "scopes": t.string().optional(),
            "clientId": t.string().optional(),
            "enableAccessToken": t.boolean().optional(),
            "extraParams": t.string().optional(),
            "kubectlRedirectUri": t.string().optional(),
            "groupPrefix": t.string().optional(),
            "deployCloudConsoleProxy": t.boolean().optional(),
            "issuerUri": t.string().optional(),
            "certificateAuthorityData": t.string().optional(),
            "userPrefix": t.string().optional(),
            "userClaim": t.string().optional(),
            "groupsClaim": t.string().optional(),
            "clientSecret": t.string().optional(),
        }
    ).named(renames["IdentityServiceOidcConfigIn"])
    types["IdentityServiceOidcConfigOut"] = t.struct(
        {
            "scopes": t.string().optional(),
            "clientId": t.string().optional(),
            "enableAccessToken": t.boolean().optional(),
            "extraParams": t.string().optional(),
            "kubectlRedirectUri": t.string().optional(),
            "groupPrefix": t.string().optional(),
            "deployCloudConsoleProxy": t.boolean().optional(),
            "issuerUri": t.string().optional(),
            "certificateAuthorityData": t.string().optional(),
            "userPrefix": t.string().optional(),
            "encryptedClientSecret": t.string().optional(),
            "userClaim": t.string().optional(),
            "groupsClaim": t.string().optional(),
            "clientSecret": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentityServiceOidcConfigOut"])

    functions = {}
    functions["projectsLocationsGet"] = gkehub.get(
        "v1/{name}/locations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
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
    functions["projectsLocationsMembershipsSetIamPolicy"] = gkehub.get(
        "v1/{name}:generateConnectManifest",
        t.struct(
            {
                "imagePullSecretContent": t.string().optional(),
                "namespace": t.string().optional(),
                "registry": t.string().optional(),
                "version": t.string().optional(),
                "proxy": t.string().optional(),
                "isUpgrade": t.boolean().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GenerateConnectManifestResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMembershipsPatch"] = gkehub.get(
        "v1/{name}:generateConnectManifest",
        t.struct(
            {
                "imagePullSecretContent": t.string().optional(),
                "namespace": t.string().optional(),
                "registry": t.string().optional(),
                "version": t.string().optional(),
                "proxy": t.string().optional(),
                "isUpgrade": t.boolean().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GenerateConnectManifestResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMembershipsCreate"] = gkehub.get(
        "v1/{name}:generateConnectManifest",
        t.struct(
            {
                "imagePullSecretContent": t.string().optional(),
                "namespace": t.string().optional(),
                "registry": t.string().optional(),
                "version": t.string().optional(),
                "proxy": t.string().optional(),
                "isUpgrade": t.boolean().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GenerateConnectManifestResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMembershipsDelete"] = gkehub.get(
        "v1/{name}:generateConnectManifest",
        t.struct(
            {
                "imagePullSecretContent": t.string().optional(),
                "namespace": t.string().optional(),
                "registry": t.string().optional(),
                "version": t.string().optional(),
                "proxy": t.string().optional(),
                "isUpgrade": t.boolean().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GenerateConnectManifestResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMembershipsGet"] = gkehub.get(
        "v1/{name}:generateConnectManifest",
        t.struct(
            {
                "imagePullSecretContent": t.string().optional(),
                "namespace": t.string().optional(),
                "registry": t.string().optional(),
                "version": t.string().optional(),
                "proxy": t.string().optional(),
                "isUpgrade": t.boolean().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GenerateConnectManifestResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMembershipsGetIamPolicy"] = gkehub.get(
        "v1/{name}:generateConnectManifest",
        t.struct(
            {
                "imagePullSecretContent": t.string().optional(),
                "namespace": t.string().optional(),
                "registry": t.string().optional(),
                "version": t.string().optional(),
                "proxy": t.string().optional(),
                "isUpgrade": t.boolean().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GenerateConnectManifestResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMembershipsTestIamPermissions"] = gkehub.get(
        "v1/{name}:generateConnectManifest",
        t.struct(
            {
                "imagePullSecretContent": t.string().optional(),
                "namespace": t.string().optional(),
                "registry": t.string().optional(),
                "version": t.string().optional(),
                "proxy": t.string().optional(),
                "isUpgrade": t.boolean().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GenerateConnectManifestResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMembershipsList"] = gkehub.get(
        "v1/{name}:generateConnectManifest",
        t.struct(
            {
                "imagePullSecretContent": t.string().optional(),
                "namespace": t.string().optional(),
                "registry": t.string().optional(),
                "version": t.string().optional(),
                "proxy": t.string().optional(),
                "isUpgrade": t.boolean().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GenerateConnectManifestResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMembershipsGenerateConnectManifest"] = gkehub.get(
        "v1/{name}:generateConnectManifest",
        t.struct(
            {
                "imagePullSecretContent": t.string().optional(),
                "namespace": t.string().optional(),
                "registry": t.string().optional(),
                "version": t.string().optional(),
                "proxy": t.string().optional(),
                "isUpgrade": t.boolean().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GenerateConnectManifestResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMembershipsBindingsDelete"] = gkehub.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "scope": t.string().optional(),
                "fleet": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMembershipsBindingsList"] = gkehub.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "scope": t.string().optional(),
                "fleet": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMembershipsBindingsGet"] = gkehub.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "scope": t.string().optional(),
                "fleet": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMembershipsBindingsCreate"] = gkehub.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "scope": t.string().optional(),
                "fleet": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMembershipsBindingsPatch"] = gkehub.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "scope": t.string().optional(),
                "fleet": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = gkehub.get(
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
    functions["projectsLocationsOperationsGet"] = gkehub.get(
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
    functions["projectsLocationsOperationsCancel"] = gkehub.get(
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
    functions["projectsLocationsOperationsList"] = gkehub.get(
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
    functions["projectsLocationsScopesDelete"] = gkehub.get(
        "v1/{parent}/scopes",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListScopesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsScopesGet"] = gkehub.get(
        "v1/{parent}/scopes",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListScopesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="gkehub", renames=renames, types=Box(types), functions=Box(functions)
    )
