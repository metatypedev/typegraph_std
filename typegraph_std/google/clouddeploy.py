from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_clouddeploy() -> Import:
    clouddeploy = HTTPRuntime("https://clouddeploy.googleapis.com/")

    renames = {
        "ErrorResponse": "_clouddeploy_1_ErrorResponse",
        "ReleaseConditionIn": "_clouddeploy_2_ReleaseConditionIn",
        "ReleaseConditionOut": "_clouddeploy_3_ReleaseConditionOut",
        "AuditConfigIn": "_clouddeploy_4_AuditConfigIn",
        "AuditConfigOut": "_clouddeploy_5_AuditConfigOut",
        "KubernetesConfigIn": "_clouddeploy_6_KubernetesConfigIn",
        "KubernetesConfigOut": "_clouddeploy_7_KubernetesConfigOut",
        "AbandonReleaseResponseIn": "_clouddeploy_8_AbandonReleaseResponseIn",
        "AbandonReleaseResponseOut": "_clouddeploy_9_AbandonReleaseResponseOut",
        "ListRolloutsResponseIn": "_clouddeploy_10_ListRolloutsResponseIn",
        "ListRolloutsResponseOut": "_clouddeploy_11_ListRolloutsResponseOut",
        "CancelRolloutRequestIn": "_clouddeploy_12_CancelRolloutRequestIn",
        "CancelRolloutRequestOut": "_clouddeploy_13_CancelRolloutRequestOut",
        "TargetIn": "_clouddeploy_14_TargetIn",
        "TargetOut": "_clouddeploy_15_TargetOut",
        "PhaseConfigIn": "_clouddeploy_16_PhaseConfigIn",
        "PhaseConfigOut": "_clouddeploy_17_PhaseConfigOut",
        "TargetNotificationEventIn": "_clouddeploy_18_TargetNotificationEventIn",
        "TargetNotificationEventOut": "_clouddeploy_19_TargetNotificationEventOut",
        "ListTargetsResponseIn": "_clouddeploy_20_ListTargetsResponseIn",
        "ListTargetsResponseOut": "_clouddeploy_21_ListTargetsResponseOut",
        "StageIn": "_clouddeploy_22_StageIn",
        "StageOut": "_clouddeploy_23_StageOut",
        "TargetArtifactIn": "_clouddeploy_24_TargetArtifactIn",
        "TargetArtifactOut": "_clouddeploy_25_TargetArtifactOut",
        "CloudRunLocationIn": "_clouddeploy_26_CloudRunLocationIn",
        "CloudRunLocationOut": "_clouddeploy_27_CloudRunLocationOut",
        "DeliveryPipelineNotificationEventIn": "_clouddeploy_28_DeliveryPipelineNotificationEventIn",
        "DeliveryPipelineNotificationEventOut": "_clouddeploy_29_DeliveryPipelineNotificationEventOut",
        "CancelRolloutResponseIn": "_clouddeploy_30_CancelRolloutResponseIn",
        "CancelRolloutResponseOut": "_clouddeploy_31_CancelRolloutResponseOut",
        "BindingIn": "_clouddeploy_32_BindingIn",
        "BindingOut": "_clouddeploy_33_BindingOut",
        "AdvanceRolloutResponseIn": "_clouddeploy_34_AdvanceRolloutResponseIn",
        "AdvanceRolloutResponseOut": "_clouddeploy_35_AdvanceRolloutResponseOut",
        "ListOperationsResponseIn": "_clouddeploy_36_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_clouddeploy_37_ListOperationsResponseOut",
        "JobIn": "_clouddeploy_38_JobIn",
        "JobOut": "_clouddeploy_39_JobOut",
        "CreateChildRolloutJobRunIn": "_clouddeploy_40_CreateChildRolloutJobRunIn",
        "CreateChildRolloutJobRunOut": "_clouddeploy_41_CreateChildRolloutJobRunOut",
        "CustomCanaryDeploymentIn": "_clouddeploy_42_CustomCanaryDeploymentIn",
        "CustomCanaryDeploymentOut": "_clouddeploy_43_CustomCanaryDeploymentOut",
        "ExecutionConfigIn": "_clouddeploy_44_ExecutionConfigIn",
        "ExecutionConfigOut": "_clouddeploy_45_ExecutionConfigOut",
        "EmptyIn": "_clouddeploy_46_EmptyIn",
        "EmptyOut": "_clouddeploy_47_EmptyOut",
        "DeployJobRunMetadataIn": "_clouddeploy_48_DeployJobRunMetadataIn",
        "DeployJobRunMetadataOut": "_clouddeploy_49_DeployJobRunMetadataOut",
        "RetryJobRequestIn": "_clouddeploy_50_RetryJobRequestIn",
        "RetryJobRequestOut": "_clouddeploy_51_RetryJobRequestOut",
        "DefaultPoolIn": "_clouddeploy_52_DefaultPoolIn",
        "DefaultPoolOut": "_clouddeploy_53_DefaultPoolOut",
        "DeliveryPipelineIn": "_clouddeploy_54_DeliveryPipelineIn",
        "DeliveryPipelineOut": "_clouddeploy_55_DeliveryPipelineOut",
        "AdvanceRolloutRequestIn": "_clouddeploy_56_AdvanceRolloutRequestIn",
        "AdvanceRolloutRequestOut": "_clouddeploy_57_AdvanceRolloutRequestOut",
        "GatewayServiceMeshIn": "_clouddeploy_58_GatewayServiceMeshIn",
        "GatewayServiceMeshOut": "_clouddeploy_59_GatewayServiceMeshOut",
        "AbandonReleaseRequestIn": "_clouddeploy_60_AbandonReleaseRequestIn",
        "AbandonReleaseRequestOut": "_clouddeploy_61_AbandonReleaseRequestOut",
        "ChildRolloutJobsIn": "_clouddeploy_62_ChildRolloutJobsIn",
        "ChildRolloutJobsOut": "_clouddeploy_63_ChildRolloutJobsOut",
        "PrivatePoolIn": "_clouddeploy_64_PrivatePoolIn",
        "PrivatePoolOut": "_clouddeploy_65_PrivatePoolOut",
        "VerifyJobRunIn": "_clouddeploy_66_VerifyJobRunIn",
        "VerifyJobRunOut": "_clouddeploy_67_VerifyJobRunOut",
        "AdvanceChildRolloutJobRunIn": "_clouddeploy_68_AdvanceChildRolloutJobRunIn",
        "AdvanceChildRolloutJobRunOut": "_clouddeploy_69_AdvanceChildRolloutJobRunOut",
        "ListDeliveryPipelinesResponseIn": "_clouddeploy_70_ListDeliveryPipelinesResponseIn",
        "ListDeliveryPipelinesResponseOut": "_clouddeploy_71_ListDeliveryPipelinesResponseOut",
        "RenderMetadataIn": "_clouddeploy_72_RenderMetadataIn",
        "RenderMetadataOut": "_clouddeploy_73_RenderMetadataOut",
        "ReleaseReadyConditionIn": "_clouddeploy_74_ReleaseReadyConditionIn",
        "ReleaseReadyConditionOut": "_clouddeploy_75_ReleaseReadyConditionOut",
        "OperationMetadataIn": "_clouddeploy_76_OperationMetadataIn",
        "OperationMetadataOut": "_clouddeploy_77_OperationMetadataOut",
        "DeploymentJobsIn": "_clouddeploy_78_DeploymentJobsIn",
        "DeploymentJobsOut": "_clouddeploy_79_DeploymentJobsOut",
        "StandardIn": "_clouddeploy_80_StandardIn",
        "StandardOut": "_clouddeploy_81_StandardOut",
        "CreateChildRolloutJobIn": "_clouddeploy_82_CreateChildRolloutJobIn",
        "CreateChildRolloutJobOut": "_clouddeploy_83_CreateChildRolloutJobOut",
        "TargetRenderIn": "_clouddeploy_84_TargetRenderIn",
        "TargetRenderOut": "_clouddeploy_85_TargetRenderOut",
        "BuildArtifactIn": "_clouddeploy_86_BuildArtifactIn",
        "BuildArtifactOut": "_clouddeploy_87_BuildArtifactOut",
        "ConfigIn": "_clouddeploy_88_ConfigIn",
        "ConfigOut": "_clouddeploy_89_ConfigOut",
        "JobRunNotificationEventIn": "_clouddeploy_90_JobRunNotificationEventIn",
        "JobRunNotificationEventOut": "_clouddeploy_91_JobRunNotificationEventOut",
        "MetadataIn": "_clouddeploy_92_MetadataIn",
        "MetadataOut": "_clouddeploy_93_MetadataOut",
        "TerminateJobRunRequestIn": "_clouddeploy_94_TerminateJobRunRequestIn",
        "TerminateJobRunRequestOut": "_clouddeploy_95_TerminateJobRunRequestOut",
        "IgnoreJobResponseIn": "_clouddeploy_96_IgnoreJobResponseIn",
        "IgnoreJobResponseOut": "_clouddeploy_97_IgnoreJobResponseOut",
        "CanaryDeploymentIn": "_clouddeploy_98_CanaryDeploymentIn",
        "CanaryDeploymentOut": "_clouddeploy_99_CanaryDeploymentOut",
        "PhaseArtifactIn": "_clouddeploy_100_PhaseArtifactIn",
        "PhaseArtifactOut": "_clouddeploy_101_PhaseArtifactOut",
        "AnthosClusterIn": "_clouddeploy_102_AnthosClusterIn",
        "AnthosClusterOut": "_clouddeploy_103_AnthosClusterOut",
        "AuditLogConfigIn": "_clouddeploy_104_AuditLogConfigIn",
        "AuditLogConfigOut": "_clouddeploy_105_AuditLogConfigOut",
        "GkeClusterIn": "_clouddeploy_106_GkeClusterIn",
        "GkeClusterOut": "_clouddeploy_107_GkeClusterOut",
        "TerminateJobRunResponseIn": "_clouddeploy_108_TerminateJobRunResponseIn",
        "TerminateJobRunResponseOut": "_clouddeploy_109_TerminateJobRunResponseOut",
        "SkaffoldSupportedConditionIn": "_clouddeploy_110_SkaffoldSupportedConditionIn",
        "SkaffoldSupportedConditionOut": "_clouddeploy_111_SkaffoldSupportedConditionOut",
        "PhaseIn": "_clouddeploy_112_PhaseIn",
        "PhaseOut": "_clouddeploy_113_PhaseOut",
        "PolicyIn": "_clouddeploy_114_PolicyIn",
        "PolicyOut": "_clouddeploy_115_PolicyOut",
        "CancelOperationRequestIn": "_clouddeploy_116_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_clouddeploy_117_CancelOperationRequestOut",
        "MultiTargetIn": "_clouddeploy_118_MultiTargetIn",
        "MultiTargetOut": "_clouddeploy_119_MultiTargetOut",
        "ListJobRunsResponseIn": "_clouddeploy_120_ListJobRunsResponseIn",
        "ListJobRunsResponseOut": "_clouddeploy_121_ListJobRunsResponseOut",
        "ListReleasesResponseIn": "_clouddeploy_122_ListReleasesResponseIn",
        "ListReleasesResponseOut": "_clouddeploy_123_ListReleasesResponseOut",
        "ReleaseRenderEventIn": "_clouddeploy_124_ReleaseRenderEventIn",
        "ReleaseRenderEventOut": "_clouddeploy_125_ReleaseRenderEventOut",
        "RuntimeConfigIn": "_clouddeploy_126_RuntimeConfigIn",
        "RuntimeConfigOut": "_clouddeploy_127_RuntimeConfigOut",
        "CloudRunConfigIn": "_clouddeploy_128_CloudRunConfigIn",
        "CloudRunConfigOut": "_clouddeploy_129_CloudRunConfigOut",
        "SerialPipelineIn": "_clouddeploy_130_SerialPipelineIn",
        "SerialPipelineOut": "_clouddeploy_131_SerialPipelineOut",
        "OperationIn": "_clouddeploy_132_OperationIn",
        "OperationOut": "_clouddeploy_133_OperationOut",
        "RolloutNotificationEventIn": "_clouddeploy_134_RolloutNotificationEventIn",
        "RolloutNotificationEventOut": "_clouddeploy_135_RolloutNotificationEventOut",
        "CanaryIn": "_clouddeploy_136_CanaryIn",
        "CanaryOut": "_clouddeploy_137_CanaryOut",
        "StrategyIn": "_clouddeploy_138_StrategyIn",
        "StrategyOut": "_clouddeploy_139_StrategyOut",
        "ReleaseNotificationEventIn": "_clouddeploy_140_ReleaseNotificationEventIn",
        "ReleaseNotificationEventOut": "_clouddeploy_141_ReleaseNotificationEventOut",
        "ListLocationsResponseIn": "_clouddeploy_142_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_clouddeploy_143_ListLocationsResponseOut",
        "DeployJobIn": "_clouddeploy_144_DeployJobIn",
        "DeployJobOut": "_clouddeploy_145_DeployJobOut",
        "ServiceNetworkingIn": "_clouddeploy_146_ServiceNetworkingIn",
        "ServiceNetworkingOut": "_clouddeploy_147_ServiceNetworkingOut",
        "TestIamPermissionsRequestIn": "_clouddeploy_148_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_clouddeploy_149_TestIamPermissionsRequestOut",
        "ExprIn": "_clouddeploy_150_ExprIn",
        "ExprOut": "_clouddeploy_151_ExprOut",
        "StatusIn": "_clouddeploy_152_StatusIn",
        "StatusOut": "_clouddeploy_153_StatusOut",
        "PipelineReadyConditionIn": "_clouddeploy_154_PipelineReadyConditionIn",
        "PipelineReadyConditionOut": "_clouddeploy_155_PipelineReadyConditionOut",
        "SkaffoldVersionIn": "_clouddeploy_156_SkaffoldVersionIn",
        "SkaffoldVersionOut": "_clouddeploy_157_SkaffoldVersionOut",
        "CloudRunMetadataIn": "_clouddeploy_158_CloudRunMetadataIn",
        "CloudRunMetadataOut": "_clouddeploy_159_CloudRunMetadataOut",
        "IgnoreJobRequestIn": "_clouddeploy_160_IgnoreJobRequestIn",
        "IgnoreJobRequestOut": "_clouddeploy_161_IgnoreJobRequestOut",
        "CloudRunRenderMetadataIn": "_clouddeploy_162_CloudRunRenderMetadataIn",
        "CloudRunRenderMetadataOut": "_clouddeploy_163_CloudRunRenderMetadataOut",
        "TargetsPresentConditionIn": "_clouddeploy_164_TargetsPresentConditionIn",
        "TargetsPresentConditionOut": "_clouddeploy_165_TargetsPresentConditionOut",
        "DateIn": "_clouddeploy_166_DateIn",
        "DateOut": "_clouddeploy_167_DateOut",
        "AdvanceChildRolloutJobIn": "_clouddeploy_168_AdvanceChildRolloutJobIn",
        "AdvanceChildRolloutJobOut": "_clouddeploy_169_AdvanceChildRolloutJobOut",
        "LocationIn": "_clouddeploy_170_LocationIn",
        "LocationOut": "_clouddeploy_171_LocationOut",
        "ReleaseIn": "_clouddeploy_172_ReleaseIn",
        "ReleaseOut": "_clouddeploy_173_ReleaseOut",
        "ApproveRolloutResponseIn": "_clouddeploy_174_ApproveRolloutResponseIn",
        "ApproveRolloutResponseOut": "_clouddeploy_175_ApproveRolloutResponseOut",
        "RolloutIn": "_clouddeploy_176_RolloutIn",
        "RolloutOut": "_clouddeploy_177_RolloutOut",
        "JobRunIn": "_clouddeploy_178_JobRunIn",
        "JobRunOut": "_clouddeploy_179_JobRunOut",
        "DeployJobRunIn": "_clouddeploy_180_DeployJobRunIn",
        "DeployJobRunOut": "_clouddeploy_181_DeployJobRunOut",
        "DeployArtifactIn": "_clouddeploy_182_DeployArtifactIn",
        "DeployArtifactOut": "_clouddeploy_183_DeployArtifactOut",
        "TestIamPermissionsResponseIn": "_clouddeploy_184_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_clouddeploy_185_TestIamPermissionsResponseOut",
        "ApproveRolloutRequestIn": "_clouddeploy_186_ApproveRolloutRequestIn",
        "ApproveRolloutRequestOut": "_clouddeploy_187_ApproveRolloutRequestOut",
        "TargetsTypeConditionIn": "_clouddeploy_188_TargetsTypeConditionIn",
        "TargetsTypeConditionOut": "_clouddeploy_189_TargetsTypeConditionOut",
        "VerifyJobIn": "_clouddeploy_190_VerifyJobIn",
        "VerifyJobOut": "_clouddeploy_191_VerifyJobOut",
        "RetryJobResponseIn": "_clouddeploy_192_RetryJobResponseIn",
        "RetryJobResponseOut": "_clouddeploy_193_RetryJobResponseOut",
        "SetIamPolicyRequestIn": "_clouddeploy_194_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_clouddeploy_195_SetIamPolicyRequestOut",
        "PipelineConditionIn": "_clouddeploy_196_PipelineConditionIn",
        "PipelineConditionOut": "_clouddeploy_197_PipelineConditionOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ReleaseConditionIn"] = t.struct(
        {
            "skaffoldSupportedCondition": t.proxy(
                renames["SkaffoldSupportedConditionIn"]
            ).optional(),
            "releaseReadyCondition": t.proxy(
                renames["ReleaseReadyConditionIn"]
            ).optional(),
        }
    ).named(renames["ReleaseConditionIn"])
    types["ReleaseConditionOut"] = t.struct(
        {
            "skaffoldSupportedCondition": t.proxy(
                renames["SkaffoldSupportedConditionOut"]
            ).optional(),
            "releaseReadyCondition": t.proxy(
                renames["ReleaseReadyConditionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReleaseConditionOut"])
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
    types["KubernetesConfigIn"] = t.struct(
        {
            "serviceNetworking": t.proxy(renames["ServiceNetworkingIn"]).optional(),
            "gatewayServiceMesh": t.proxy(renames["GatewayServiceMeshIn"]).optional(),
        }
    ).named(renames["KubernetesConfigIn"])
    types["KubernetesConfigOut"] = t.struct(
        {
            "serviceNetworking": t.proxy(renames["ServiceNetworkingOut"]).optional(),
            "gatewayServiceMesh": t.proxy(renames["GatewayServiceMeshOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KubernetesConfigOut"])
    types["AbandonReleaseResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AbandonReleaseResponseIn"]
    )
    types["AbandonReleaseResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AbandonReleaseResponseOut"])
    types["ListRolloutsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "rollouts": t.array(t.proxy(renames["RolloutIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListRolloutsResponseIn"])
    types["ListRolloutsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "rollouts": t.array(t.proxy(renames["RolloutOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListRolloutsResponseOut"])
    types["CancelRolloutRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelRolloutRequestIn"]
    )
    types["CancelRolloutRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelRolloutRequestOut"])
    types["TargetIn"] = t.struct(
        {
            "requireApproval": t.boolean().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "executionConfigs": t.array(
                t.proxy(renames["ExecutionConfigIn"])
            ).optional(),
            "run": t.proxy(renames["CloudRunLocationIn"]).optional(),
            "etag": t.string().optional(),
            "name": t.string().optional(),
            "multiTarget": t.proxy(renames["MultiTargetIn"]).optional(),
            "anthosCluster": t.proxy(renames["AnthosClusterIn"]).optional(),
            "description": t.string().optional(),
            "gke": t.proxy(renames["GkeClusterIn"]).optional(),
        }
    ).named(renames["TargetIn"])
    types["TargetOut"] = t.struct(
        {
            "targetId": t.string().optional(),
            "requireApproval": t.boolean().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "executionConfigs": t.array(
                t.proxy(renames["ExecutionConfigOut"])
            ).optional(),
            "run": t.proxy(renames["CloudRunLocationOut"]).optional(),
            "etag": t.string().optional(),
            "uid": t.string().optional(),
            "name": t.string().optional(),
            "multiTarget": t.proxy(renames["MultiTargetOut"]).optional(),
            "createTime": t.string().optional(),
            "anthosCluster": t.proxy(renames["AnthosClusterOut"]).optional(),
            "description": t.string().optional(),
            "gke": t.proxy(renames["GkeClusterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetOut"])
    types["PhaseConfigIn"] = t.struct(
        {
            "percentage": t.integer(),
            "verify": t.boolean().optional(),
            "phaseId": t.string(),
            "profiles": t.array(t.string()).optional(),
        }
    ).named(renames["PhaseConfigIn"])
    types["PhaseConfigOut"] = t.struct(
        {
            "percentage": t.integer(),
            "verify": t.boolean().optional(),
            "phaseId": t.string(),
            "profiles": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhaseConfigOut"])
    types["TargetNotificationEventIn"] = t.struct(
        {
            "target": t.string().optional(),
            "message": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["TargetNotificationEventIn"])
    types["TargetNotificationEventOut"] = t.struct(
        {
            "target": t.string().optional(),
            "message": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetNotificationEventOut"])
    types["ListTargetsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "targets": t.array(t.proxy(renames["TargetIn"])).optional(),
        }
    ).named(renames["ListTargetsResponseIn"])
    types["ListTargetsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "targets": t.array(t.proxy(renames["TargetOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTargetsResponseOut"])
    types["StageIn"] = t.struct(
        {
            "targetId": t.string().optional(),
            "strategy": t.proxy(renames["StrategyIn"]).optional(),
            "profiles": t.array(t.string()).optional(),
        }
    ).named(renames["StageIn"])
    types["StageOut"] = t.struct(
        {
            "targetId": t.string().optional(),
            "strategy": t.proxy(renames["StrategyOut"]).optional(),
            "profiles": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StageOut"])
    types["TargetArtifactIn"] = t.struct({"_": t.string().optional()}).named(
        renames["TargetArtifactIn"]
    )
    types["TargetArtifactOut"] = t.struct(
        {
            "manifestPath": t.string().optional(),
            "phaseArtifacts": t.struct({"_": t.string().optional()}).optional(),
            "artifactUri": t.string().optional(),
            "skaffoldConfigPath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetArtifactOut"])
    types["CloudRunLocationIn"] = t.struct({"location": t.string()}).named(
        renames["CloudRunLocationIn"]
    )
    types["CloudRunLocationOut"] = t.struct(
        {"location": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CloudRunLocationOut"])
    types["DeliveryPipelineNotificationEventIn"] = t.struct(
        {
            "deliveryPipeline": t.string().optional(),
            "message": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["DeliveryPipelineNotificationEventIn"])
    types["DeliveryPipelineNotificationEventOut"] = t.struct(
        {
            "deliveryPipeline": t.string().optional(),
            "message": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeliveryPipelineNotificationEventOut"])
    types["CancelRolloutResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelRolloutResponseIn"]
    )
    types["CancelRolloutResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelRolloutResponseOut"])
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
    types["AdvanceRolloutResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AdvanceRolloutResponseIn"]
    )
    types["AdvanceRolloutResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AdvanceRolloutResponseOut"])
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
    types["JobIn"] = t.struct({"_": t.string().optional()}).named(renames["JobIn"])
    types["JobOut"] = t.struct(
        {
            "verifyJob": t.proxy(renames["VerifyJobOut"]).optional(),
            "jobRun": t.string().optional(),
            "advanceChildRolloutJob": t.proxy(
                renames["AdvanceChildRolloutJobOut"]
            ).optional(),
            "createChildRolloutJob": t.proxy(
                renames["CreateChildRolloutJobOut"]
            ).optional(),
            "id": t.string().optional(),
            "state": t.string().optional(),
            "skipMessage": t.string().optional(),
            "deployJob": t.proxy(renames["DeployJobOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobOut"])
    types["CreateChildRolloutJobRunIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CreateChildRolloutJobRunIn"]
    )
    types["CreateChildRolloutJobRunOut"] = t.struct(
        {
            "rolloutPhaseId": t.string().optional(),
            "rollout": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateChildRolloutJobRunOut"])
    types["CustomCanaryDeploymentIn"] = t.struct(
        {"phaseConfigs": t.array(t.proxy(renames["PhaseConfigIn"]))}
    ).named(renames["CustomCanaryDeploymentIn"])
    types["CustomCanaryDeploymentOut"] = t.struct(
        {
            "phaseConfigs": t.array(t.proxy(renames["PhaseConfigOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomCanaryDeploymentOut"])
    types["ExecutionConfigIn"] = t.struct(
        {
            "executionTimeout": t.string().optional(),
            "privatePool": t.proxy(renames["PrivatePoolIn"]).optional(),
            "usages": t.array(t.string()),
            "defaultPool": t.proxy(renames["DefaultPoolIn"]).optional(),
            "workerPool": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "artifactStorage": t.string().optional(),
        }
    ).named(renames["ExecutionConfigIn"])
    types["ExecutionConfigOut"] = t.struct(
        {
            "executionTimeout": t.string().optional(),
            "privatePool": t.proxy(renames["PrivatePoolOut"]).optional(),
            "usages": t.array(t.string()),
            "defaultPool": t.proxy(renames["DefaultPoolOut"]).optional(),
            "workerPool": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "artifactStorage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecutionConfigOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["DeployJobRunMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeployJobRunMetadataIn"]
    )
    types["DeployJobRunMetadataOut"] = t.struct(
        {
            "cloudRun": t.proxy(renames["CloudRunMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeployJobRunMetadataOut"])
    types["RetryJobRequestIn"] = t.struct(
        {"jobId": t.string(), "phaseId": t.string()}
    ).named(renames["RetryJobRequestIn"])
    types["RetryJobRequestOut"] = t.struct(
        {
            "jobId": t.string(),
            "phaseId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RetryJobRequestOut"])
    types["DefaultPoolIn"] = t.struct(
        {
            "artifactStorage": t.string().optional(),
            "serviceAccount": t.string().optional(),
        }
    ).named(renames["DefaultPoolIn"])
    types["DefaultPoolOut"] = t.struct(
        {
            "artifactStorage": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DefaultPoolOut"])
    types["DeliveryPipelineIn"] = t.struct(
        {
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "etag": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "serialPipeline": t.proxy(renames["SerialPipelineIn"]).optional(),
            "suspended": t.boolean().optional(),
        }
    ).named(renames["DeliveryPipelineIn"])
    types["DeliveryPipelineOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "etag": t.string().optional(),
            "condition": t.proxy(renames["PipelineConditionOut"]).optional(),
            "updateTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "serialPipeline": t.proxy(renames["SerialPipelineOut"]).optional(),
            "uid": t.string().optional(),
            "suspended": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeliveryPipelineOut"])
    types["AdvanceRolloutRequestIn"] = t.struct({"phaseId": t.string()}).named(
        renames["AdvanceRolloutRequestIn"]
    )
    types["AdvanceRolloutRequestOut"] = t.struct(
        {"phaseId": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AdvanceRolloutRequestOut"])
    types["GatewayServiceMeshIn"] = t.struct(
        {"deployment": t.string(), "service": t.string(), "httpRoute": t.string()}
    ).named(renames["GatewayServiceMeshIn"])
    types["GatewayServiceMeshOut"] = t.struct(
        {
            "deployment": t.string(),
            "service": t.string(),
            "httpRoute": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GatewayServiceMeshOut"])
    types["AbandonReleaseRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AbandonReleaseRequestIn"]
    )
    types["AbandonReleaseRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AbandonReleaseRequestOut"])
    types["ChildRolloutJobsIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ChildRolloutJobsIn"]
    )
    types["ChildRolloutJobsOut"] = t.struct(
        {
            "createRolloutJobs": t.array(t.proxy(renames["JobOut"])).optional(),
            "advanceRolloutJobs": t.array(t.proxy(renames["JobOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChildRolloutJobsOut"])
    types["PrivatePoolIn"] = t.struct(
        {
            "serviceAccount": t.string().optional(),
            "workerPool": t.string(),
            "artifactStorage": t.string().optional(),
        }
    ).named(renames["PrivatePoolIn"])
    types["PrivatePoolOut"] = t.struct(
        {
            "serviceAccount": t.string().optional(),
            "workerPool": t.string(),
            "artifactStorage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrivatePoolOut"])
    types["VerifyJobRunIn"] = t.struct({"_": t.string().optional()}).named(
        renames["VerifyJobRunIn"]
    )
    types["VerifyJobRunOut"] = t.struct(
        {
            "eventLogPath": t.string().optional(),
            "artifactUri": t.string().optional(),
            "failureMessage": t.string().optional(),
            "build": t.string().optional(),
            "failureCause": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VerifyJobRunOut"])
    types["AdvanceChildRolloutJobRunIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AdvanceChildRolloutJobRunIn"]
    )
    types["AdvanceChildRolloutJobRunOut"] = t.struct(
        {
            "rollout": t.string().optional(),
            "rolloutPhaseId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdvanceChildRolloutJobRunOut"])
    types["ListDeliveryPipelinesResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "deliveryPipelines": t.array(
                t.proxy(renames["DeliveryPipelineIn"])
            ).optional(),
        }
    ).named(renames["ListDeliveryPipelinesResponseIn"])
    types["ListDeliveryPipelinesResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "deliveryPipelines": t.array(
                t.proxy(renames["DeliveryPipelineOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDeliveryPipelinesResponseOut"])
    types["RenderMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RenderMetadataIn"]
    )
    types["RenderMetadataOut"] = t.struct(
        {
            "cloudRun": t.proxy(renames["CloudRunRenderMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RenderMetadataOut"])
    types["ReleaseReadyConditionIn"] = t.struct(
        {"status": t.boolean().optional()}
    ).named(renames["ReleaseReadyConditionIn"])
    types["ReleaseReadyConditionOut"] = t.struct(
        {
            "status": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReleaseReadyConditionOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "verb": t.string().optional(),
            "createTime": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "apiVersion": t.string().optional(),
            "target": t.string().optional(),
            "statusMessage": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["DeploymentJobsIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeploymentJobsIn"]
    )
    types["DeploymentJobsOut"] = t.struct(
        {
            "deployJob": t.proxy(renames["JobOut"]).optional(),
            "verifyJob": t.proxy(renames["JobOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeploymentJobsOut"])
    types["StandardIn"] = t.struct({"verify": t.boolean().optional()}).named(
        renames["StandardIn"]
    )
    types["StandardOut"] = t.struct(
        {
            "verify": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StandardOut"])
    types["CreateChildRolloutJobIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CreateChildRolloutJobIn"]
    )
    types["CreateChildRolloutJobOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CreateChildRolloutJobOut"])
    types["TargetRenderIn"] = t.struct({"_": t.string().optional()}).named(
        renames["TargetRenderIn"]
    )
    types["TargetRenderOut"] = t.struct(
        {
            "metadata": t.proxy(renames["RenderMetadataOut"]).optional(),
            "renderingBuild": t.string().optional(),
            "renderingState": t.string().optional(),
            "failureCause": t.string().optional(),
            "failureMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetRenderOut"])
    types["BuildArtifactIn"] = t.struct(
        {"tag": t.string().optional(), "image": t.string().optional()}
    ).named(renames["BuildArtifactIn"])
    types["BuildArtifactOut"] = t.struct(
        {
            "tag": t.string().optional(),
            "image": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuildArtifactOut"])
    types["ConfigIn"] = t.struct(
        {
            "defaultSkaffoldVersion": t.string().optional(),
            "supportedVersions": t.array(
                t.proxy(renames["SkaffoldVersionIn"])
            ).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ConfigIn"])
    types["ConfigOut"] = t.struct(
        {
            "defaultSkaffoldVersion": t.string().optional(),
            "supportedVersions": t.array(
                t.proxy(renames["SkaffoldVersionOut"])
            ).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigOut"])
    types["JobRunNotificationEventIn"] = t.struct(
        {
            "jobRun": t.string().optional(),
            "type": t.string().optional(),
            "releaseUid": t.string().optional(),
            "pipelineUid": t.string().optional(),
            "rolloutUid": t.string().optional(),
            "message": t.string().optional(),
            "targetId": t.string().optional(),
        }
    ).named(renames["JobRunNotificationEventIn"])
    types["JobRunNotificationEventOut"] = t.struct(
        {
            "jobRun": t.string().optional(),
            "type": t.string().optional(),
            "releaseUid": t.string().optional(),
            "pipelineUid": t.string().optional(),
            "rolloutUid": t.string().optional(),
            "message": t.string().optional(),
            "targetId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobRunNotificationEventOut"])
    types["MetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MetadataIn"]
    )
    types["MetadataOut"] = t.struct(
        {
            "cloudRun": t.proxy(renames["CloudRunMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetadataOut"])
    types["TerminateJobRunRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["TerminateJobRunRequestIn"]
    )
    types["TerminateJobRunRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["TerminateJobRunRequestOut"])
    types["IgnoreJobResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["IgnoreJobResponseIn"]
    )
    types["IgnoreJobResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["IgnoreJobResponseOut"])
    types["CanaryDeploymentIn"] = t.struct(
        {"verify": t.boolean().optional(), "percentages": t.array(t.integer())}
    ).named(renames["CanaryDeploymentIn"])
    types["CanaryDeploymentOut"] = t.struct(
        {
            "verify": t.boolean().optional(),
            "percentages": t.array(t.integer()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CanaryDeploymentOut"])
    types["PhaseArtifactIn"] = t.struct({"_": t.string().optional()}).named(
        renames["PhaseArtifactIn"]
    )
    types["PhaseArtifactOut"] = t.struct(
        {
            "manifestPath": t.string().optional(),
            "jobManifestsPath": t.string().optional(),
            "skaffoldConfigPath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhaseArtifactOut"])
    types["AnthosClusterIn"] = t.struct({"membership": t.string().optional()}).named(
        renames["AnthosClusterIn"]
    )
    types["AnthosClusterOut"] = t.struct(
        {
            "membership": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnthosClusterOut"])
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
    types["GkeClusterIn"] = t.struct(
        {"internalIp": t.boolean().optional(), "cluster": t.string().optional()}
    ).named(renames["GkeClusterIn"])
    types["GkeClusterOut"] = t.struct(
        {
            "internalIp": t.boolean().optional(),
            "cluster": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GkeClusterOut"])
    types["TerminateJobRunResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["TerminateJobRunResponseIn"]
    )
    types["TerminateJobRunResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["TerminateJobRunResponseOut"])
    types["SkaffoldSupportedConditionIn"] = t.struct(
        {
            "supportExpirationTime": t.string().optional(),
            "skaffoldSupportState": t.string().optional(),
            "maintenanceModeTime": t.string().optional(),
            "status": t.boolean().optional(),
        }
    ).named(renames["SkaffoldSupportedConditionIn"])
    types["SkaffoldSupportedConditionOut"] = t.struct(
        {
            "supportExpirationTime": t.string().optional(),
            "skaffoldSupportState": t.string().optional(),
            "maintenanceModeTime": t.string().optional(),
            "status": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SkaffoldSupportedConditionOut"])
    types["PhaseIn"] = t.struct({"_": t.string().optional()}).named(renames["PhaseIn"])
    types["PhaseOut"] = t.struct(
        {
            "id": t.string().optional(),
            "deploymentJobs": t.proxy(renames["DeploymentJobsOut"]).optional(),
            "skipMessage": t.string().optional(),
            "state": t.string().optional(),
            "childRolloutJobs": t.proxy(renames["ChildRolloutJobsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhaseOut"])
    types["PolicyIn"] = t.struct(
        {
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["MultiTargetIn"] = t.struct({"targetIds": t.array(t.string())}).named(
        renames["MultiTargetIn"]
    )
    types["MultiTargetOut"] = t.struct(
        {
            "targetIds": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MultiTargetOut"])
    types["ListJobRunsResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "jobRuns": t.array(t.proxy(renames["JobRunIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListJobRunsResponseIn"])
    types["ListJobRunsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "jobRuns": t.array(t.proxy(renames["JobRunOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListJobRunsResponseOut"])
    types["ListReleasesResponseIn"] = t.struct(
        {
            "releases": t.array(t.proxy(renames["ReleaseIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListReleasesResponseIn"])
    types["ListReleasesResponseOut"] = t.struct(
        {
            "releases": t.array(t.proxy(renames["ReleaseOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListReleasesResponseOut"])
    types["ReleaseRenderEventIn"] = t.struct(
        {"message": t.string().optional(), "release": t.string().optional()}
    ).named(renames["ReleaseRenderEventIn"])
    types["ReleaseRenderEventOut"] = t.struct(
        {
            "message": t.string().optional(),
            "release": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReleaseRenderEventOut"])
    types["RuntimeConfigIn"] = t.struct(
        {
            "cloudRun": t.proxy(renames["CloudRunConfigIn"]).optional(),
            "kubernetes": t.proxy(renames["KubernetesConfigIn"]).optional(),
        }
    ).named(renames["RuntimeConfigIn"])
    types["RuntimeConfigOut"] = t.struct(
        {
            "cloudRun": t.proxy(renames["CloudRunConfigOut"]).optional(),
            "kubernetes": t.proxy(renames["KubernetesConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RuntimeConfigOut"])
    types["CloudRunConfigIn"] = t.struct(
        {"automaticTrafficControl": t.boolean().optional()}
    ).named(renames["CloudRunConfigIn"])
    types["CloudRunConfigOut"] = t.struct(
        {
            "automaticTrafficControl": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudRunConfigOut"])
    types["SerialPipelineIn"] = t.struct(
        {"stages": t.array(t.proxy(renames["StageIn"])).optional()}
    ).named(renames["SerialPipelineIn"])
    types["SerialPipelineOut"] = t.struct(
        {
            "stages": t.array(t.proxy(renames["StageOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SerialPipelineOut"])
    types["OperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationOut"])
    types["RolloutNotificationEventIn"] = t.struct(
        {
            "message": t.string().optional(),
            "pipelineUid": t.string().optional(),
            "targetId": t.string().optional(),
            "rollout": t.string().optional(),
            "type": t.string().optional(),
            "releaseUid": t.string().optional(),
        }
    ).named(renames["RolloutNotificationEventIn"])
    types["RolloutNotificationEventOut"] = t.struct(
        {
            "message": t.string().optional(),
            "pipelineUid": t.string().optional(),
            "targetId": t.string().optional(),
            "rollout": t.string().optional(),
            "type": t.string().optional(),
            "releaseUid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RolloutNotificationEventOut"])
    types["CanaryIn"] = t.struct(
        {
            "customCanaryDeployment": t.proxy(
                renames["CustomCanaryDeploymentIn"]
            ).optional(),
            "runtimeConfig": t.proxy(renames["RuntimeConfigIn"]).optional(),
            "canaryDeployment": t.proxy(renames["CanaryDeploymentIn"]).optional(),
        }
    ).named(renames["CanaryIn"])
    types["CanaryOut"] = t.struct(
        {
            "customCanaryDeployment": t.proxy(
                renames["CustomCanaryDeploymentOut"]
            ).optional(),
            "runtimeConfig": t.proxy(renames["RuntimeConfigOut"]).optional(),
            "canaryDeployment": t.proxy(renames["CanaryDeploymentOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CanaryOut"])
    types["StrategyIn"] = t.struct(
        {
            "canary": t.proxy(renames["CanaryIn"]).optional(),
            "standard": t.proxy(renames["StandardIn"]).optional(),
        }
    ).named(renames["StrategyIn"])
    types["StrategyOut"] = t.struct(
        {
            "canary": t.proxy(renames["CanaryOut"]).optional(),
            "standard": t.proxy(renames["StandardOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StrategyOut"])
    types["ReleaseNotificationEventIn"] = t.struct(
        {
            "release": t.string().optional(),
            "message": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["ReleaseNotificationEventIn"])
    types["ReleaseNotificationEventOut"] = t.struct(
        {
            "release": t.string().optional(),
            "message": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReleaseNotificationEventOut"])
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
    types["DeployJobIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeployJobIn"]
    )
    types["DeployJobOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeployJobOut"])
    types["ServiceNetworkingIn"] = t.struct(
        {"service": t.string(), "deployment": t.string()}
    ).named(renames["ServiceNetworkingIn"])
    types["ServiceNetworkingOut"] = t.struct(
        {
            "service": t.string(),
            "deployment": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceNetworkingOut"])
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
            "location": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
            "expression": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "location": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
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
    types["PipelineReadyConditionIn"] = t.struct(
        {"status": t.boolean().optional(), "updateTime": t.string().optional()}
    ).named(renames["PipelineReadyConditionIn"])
    types["PipelineReadyConditionOut"] = t.struct(
        {
            "status": t.boolean().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PipelineReadyConditionOut"])
    types["SkaffoldVersionIn"] = t.struct(
        {
            "supportExpirationTime": t.string().optional(),
            "supportEndDate": t.proxy(renames["DateIn"]).optional(),
            "version": t.string().optional(),
            "maintenanceModeTime": t.string().optional(),
        }
    ).named(renames["SkaffoldVersionIn"])
    types["SkaffoldVersionOut"] = t.struct(
        {
            "supportExpirationTime": t.string().optional(),
            "supportEndDate": t.proxy(renames["DateOut"]).optional(),
            "version": t.string().optional(),
            "maintenanceModeTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SkaffoldVersionOut"])
    types["CloudRunMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CloudRunMetadataIn"]
    )
    types["CloudRunMetadataOut"] = t.struct(
        {
            "revision": t.string().optional(),
            "service": t.string().optional(),
            "serviceUrls": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudRunMetadataOut"])
    types["IgnoreJobRequestIn"] = t.struct(
        {"jobId": t.string(), "phaseId": t.string()}
    ).named(renames["IgnoreJobRequestIn"])
    types["IgnoreJobRequestOut"] = t.struct(
        {
            "jobId": t.string(),
            "phaseId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IgnoreJobRequestOut"])
    types["CloudRunRenderMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CloudRunRenderMetadataIn"]
    )
    types["CloudRunRenderMetadataOut"] = t.struct(
        {
            "service": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudRunRenderMetadataOut"])
    types["TargetsPresentConditionIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "missingTargets": t.array(t.string()).optional(),
            "status": t.boolean().optional(),
        }
    ).named(renames["TargetsPresentConditionIn"])
    types["TargetsPresentConditionOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "missingTargets": t.array(t.string()).optional(),
            "status": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetsPresentConditionOut"])
    types["DateIn"] = t.struct(
        {
            "day": t.integer().optional(),
            "month": t.integer().optional(),
            "year": t.integer().optional(),
        }
    ).named(renames["DateIn"])
    types["DateOut"] = t.struct(
        {
            "day": t.integer().optional(),
            "month": t.integer().optional(),
            "year": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
    types["AdvanceChildRolloutJobIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AdvanceChildRolloutJobIn"]
    )
    types["AdvanceChildRolloutJobOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AdvanceChildRolloutJobOut"])
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
    types["ReleaseIn"] = t.struct(
        {
            "skaffoldConfigPath": t.string().optional(),
            "buildArtifacts": t.array(t.proxy(renames["BuildArtifactIn"])).optional(),
            "skaffoldVersion": t.string().optional(),
            "etag": t.string().optional(),
            "name": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "skaffoldConfigUri": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ReleaseIn"])
    types["ReleaseOut"] = t.struct(
        {
            "uid": t.string().optional(),
            "skaffoldConfigPath": t.string().optional(),
            "targetArtifacts": t.struct({"_": t.string().optional()}).optional(),
            "buildArtifacts": t.array(t.proxy(renames["BuildArtifactOut"])).optional(),
            "abandoned": t.boolean().optional(),
            "skaffoldVersion": t.string().optional(),
            "condition": t.proxy(renames["ReleaseConditionOut"]).optional(),
            "deliveryPipelineSnapshot": t.proxy(
                renames["DeliveryPipelineOut"]
            ).optional(),
            "etag": t.string().optional(),
            "targetRenders": t.struct({"_": t.string().optional()}).optional(),
            "renderState": t.string().optional(),
            "targetSnapshots": t.array(t.proxy(renames["TargetOut"])).optional(),
            "createTime": t.string().optional(),
            "renderStartTime": t.string().optional(),
            "name": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "skaffoldConfigUri": t.string().optional(),
            "renderEndTime": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReleaseOut"])
    types["ApproveRolloutResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ApproveRolloutResponseIn"]
    )
    types["ApproveRolloutResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ApproveRolloutResponseOut"])
    types["RolloutIn"] = t.struct(
        {
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "etag": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "targetId": t.string(),
        }
    ).named(renames["RolloutIn"])
    types["RolloutOut"] = t.struct(
        {
            "approveTime": t.string().optional(),
            "description": t.string().optional(),
            "approvalState": t.string().optional(),
            "failureReason": t.string().optional(),
            "metadata": t.proxy(renames["MetadataOut"]).optional(),
            "phases": t.array(t.proxy(renames["PhaseOut"])).optional(),
            "deployStartTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "deployEndTime": t.string().optional(),
            "enqueueTime": t.string().optional(),
            "uid": t.string().optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "deployingBuild": t.string().optional(),
            "etag": t.string().optional(),
            "deployFailureCause": t.string().optional(),
            "createTime": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "targetId": t.string(),
            "controllerRollout": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RolloutOut"])
    types["JobRunIn"] = t.struct({"name": t.string().optional()}).named(
        renames["JobRunIn"]
    )
    types["JobRunOut"] = t.struct(
        {
            "verifyJobRun": t.proxy(renames["VerifyJobRunOut"]).optional(),
            "etag": t.string().optional(),
            "state": t.string().optional(),
            "advanceChildRolloutJobRun": t.proxy(
                renames["AdvanceChildRolloutJobRunOut"]
            ).optional(),
            "createChildRolloutJobRun": t.proxy(
                renames["CreateChildRolloutJobRunOut"]
            ).optional(),
            "uid": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "deployJobRun": t.proxy(renames["DeployJobRunOut"]).optional(),
            "jobId": t.string().optional(),
            "endTime": t.string().optional(),
            "phaseId": t.string().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobRunOut"])
    types["DeployJobRunIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeployJobRunIn"]
    )
    types["DeployJobRunOut"] = t.struct(
        {
            "failureMessage": t.string().optional(),
            "failureCause": t.string().optional(),
            "artifact": t.proxy(renames["DeployArtifactOut"]).optional(),
            "build": t.string().optional(),
            "metadata": t.proxy(renames["DeployJobRunMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeployJobRunOut"])
    types["DeployArtifactIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeployArtifactIn"]
    )
    types["DeployArtifactOut"] = t.struct(
        {
            "manifestPaths": t.array(t.string()).optional(),
            "artifactUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeployArtifactOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["ApproveRolloutRequestIn"] = t.struct({"approved": t.boolean()}).named(
        renames["ApproveRolloutRequestIn"]
    )
    types["ApproveRolloutRequestOut"] = t.struct(
        {"approved": t.boolean(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ApproveRolloutRequestOut"])
    types["TargetsTypeConditionIn"] = t.struct(
        {"status": t.boolean().optional(), "errorDetails": t.string().optional()}
    ).named(renames["TargetsTypeConditionIn"])
    types["TargetsTypeConditionOut"] = t.struct(
        {
            "status": t.boolean().optional(),
            "errorDetails": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetsTypeConditionOut"])
    types["VerifyJobIn"] = t.struct({"_": t.string().optional()}).named(
        renames["VerifyJobIn"]
    )
    types["VerifyJobOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["VerifyJobOut"])
    types["RetryJobResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RetryJobResponseIn"]
    )
    types["RetryJobResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RetryJobResponseOut"])
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
    types["PipelineConditionIn"] = t.struct(
        {
            "pipelineReadyCondition": t.proxy(
                renames["PipelineReadyConditionIn"]
            ).optional(),
            "targetsPresentCondition": t.proxy(
                renames["TargetsPresentConditionIn"]
            ).optional(),
            "targetsTypeCondition": t.proxy(
                renames["TargetsTypeConditionIn"]
            ).optional(),
        }
    ).named(renames["PipelineConditionIn"])
    types["PipelineConditionOut"] = t.struct(
        {
            "pipelineReadyCondition": t.proxy(
                renames["PipelineReadyConditionOut"]
            ).optional(),
            "targetsPresentCondition": t.proxy(
                renames["TargetsPresentConditionOut"]
            ).optional(),
            "targetsTypeCondition": t.proxy(
                renames["TargetsTypeConditionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PipelineConditionOut"])

    functions = {}
    functions["projectsLocationsGet"] = clouddeploy.get(
        "v1/{name}/locations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGetConfig"] = clouddeploy.get(
        "v1/{name}/locations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsList"] = clouddeploy.get(
        "v1/{name}/locations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDeliveryPipelinesList"] = clouddeploy.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["DeliveryPipelineOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDeliveryPipelinesGetIamPolicy"] = clouddeploy.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["DeliveryPipelineOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDeliveryPipelinesTestIamPermissions"] = clouddeploy.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["DeliveryPipelineOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDeliveryPipelinesPatch"] = clouddeploy.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["DeliveryPipelineOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDeliveryPipelinesDelete"] = clouddeploy.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["DeliveryPipelineOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDeliveryPipelinesCreate"] = clouddeploy.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["DeliveryPipelineOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDeliveryPipelinesSetIamPolicy"] = clouddeploy.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["DeliveryPipelineOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDeliveryPipelinesGet"] = clouddeploy.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["DeliveryPipelineOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDeliveryPipelinesReleasesAbandon"] = clouddeploy.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ReleaseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDeliveryPipelinesReleasesList"] = clouddeploy.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ReleaseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDeliveryPipelinesReleasesCreate"] = clouddeploy.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ReleaseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDeliveryPipelinesReleasesGet"] = clouddeploy.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ReleaseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDeliveryPipelinesReleasesRolloutsCancel"
    ] = clouddeploy.post(
        "v1/{name}:approve",
        t.struct(
            {"name": t.string(), "approved": t.boolean(), "auth": t.string().optional()}
        ),
        t.proxy(renames["ApproveRolloutResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDeliveryPipelinesReleasesRolloutsIgnoreJob"
    ] = clouddeploy.post(
        "v1/{name}:approve",
        t.struct(
            {"name": t.string(), "approved": t.boolean(), "auth": t.string().optional()}
        ),
        t.proxy(renames["ApproveRolloutResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDeliveryPipelinesReleasesRolloutsAdvance"
    ] = clouddeploy.post(
        "v1/{name}:approve",
        t.struct(
            {"name": t.string(), "approved": t.boolean(), "auth": t.string().optional()}
        ),
        t.proxy(renames["ApproveRolloutResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDeliveryPipelinesReleasesRolloutsList"
    ] = clouddeploy.post(
        "v1/{name}:approve",
        t.struct(
            {"name": t.string(), "approved": t.boolean(), "auth": t.string().optional()}
        ),
        t.proxy(renames["ApproveRolloutResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDeliveryPipelinesReleasesRolloutsGet"
    ] = clouddeploy.post(
        "v1/{name}:approve",
        t.struct(
            {"name": t.string(), "approved": t.boolean(), "auth": t.string().optional()}
        ),
        t.proxy(renames["ApproveRolloutResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDeliveryPipelinesReleasesRolloutsRetryJob"
    ] = clouddeploy.post(
        "v1/{name}:approve",
        t.struct(
            {"name": t.string(), "approved": t.boolean(), "auth": t.string().optional()}
        ),
        t.proxy(renames["ApproveRolloutResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDeliveryPipelinesReleasesRolloutsCreate"
    ] = clouddeploy.post(
        "v1/{name}:approve",
        t.struct(
            {"name": t.string(), "approved": t.boolean(), "auth": t.string().optional()}
        ),
        t.proxy(renames["ApproveRolloutResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDeliveryPipelinesReleasesRolloutsApprove"
    ] = clouddeploy.post(
        "v1/{name}:approve",
        t.struct(
            {"name": t.string(), "approved": t.boolean(), "auth": t.string().optional()}
        ),
        t.proxy(renames["ApproveRolloutResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDeliveryPipelinesReleasesRolloutsJobRunsTerminate"
    ] = clouddeploy.get(
        "v1/{parent}/jobRuns",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListJobRunsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDeliveryPipelinesReleasesRolloutsJobRunsGet"
    ] = clouddeploy.get(
        "v1/{parent}/jobRuns",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListJobRunsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDeliveryPipelinesReleasesRolloutsJobRunsList"
    ] = clouddeploy.get(
        "v1/{parent}/jobRuns",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListJobRunsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = clouddeploy.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = clouddeploy.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = clouddeploy.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = clouddeploy.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTargetsPatch"] = clouddeploy.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TargetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTargetsTestIamPermissions"] = clouddeploy.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TargetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTargetsList"] = clouddeploy.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TargetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTargetsGetIamPolicy"] = clouddeploy.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TargetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTargetsSetIamPolicy"] = clouddeploy.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TargetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTargetsDelete"] = clouddeploy.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TargetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTargetsCreate"] = clouddeploy.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TargetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTargetsGet"] = clouddeploy.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TargetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="clouddeploy", renames=renames, types=types, functions=functions
    )
