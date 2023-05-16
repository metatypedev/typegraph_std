from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_clouddeploy() -> Import:
    clouddeploy = HTTPRuntime("https://clouddeploy.googleapis.com/")

    renames = {
        "ErrorResponse": "_clouddeploy_1_ErrorResponse",
        "OperationIn": "_clouddeploy_2_OperationIn",
        "OperationOut": "_clouddeploy_3_OperationOut",
        "PolicyIn": "_clouddeploy_4_PolicyIn",
        "PolicyOut": "_clouddeploy_5_PolicyOut",
        "VerifyJobIn": "_clouddeploy_6_VerifyJobIn",
        "VerifyJobOut": "_clouddeploy_7_VerifyJobOut",
        "ExecutionConfigIn": "_clouddeploy_8_ExecutionConfigIn",
        "ExecutionConfigOut": "_clouddeploy_9_ExecutionConfigOut",
        "ReleaseNotificationEventIn": "_clouddeploy_10_ReleaseNotificationEventIn",
        "ReleaseNotificationEventOut": "_clouddeploy_11_ReleaseNotificationEventOut",
        "AnthosClusterIn": "_clouddeploy_12_AnthosClusterIn",
        "AnthosClusterOut": "_clouddeploy_13_AnthosClusterOut",
        "RetryJobResponseIn": "_clouddeploy_14_RetryJobResponseIn",
        "RetryJobResponseOut": "_clouddeploy_15_RetryJobResponseOut",
        "TestIamPermissionsRequestIn": "_clouddeploy_16_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_clouddeploy_17_TestIamPermissionsRequestOut",
        "DeployJobRunMetadataIn": "_clouddeploy_18_DeployJobRunMetadataIn",
        "DeployJobRunMetadataOut": "_clouddeploy_19_DeployJobRunMetadataOut",
        "KubernetesConfigIn": "_clouddeploy_20_KubernetesConfigIn",
        "KubernetesConfigOut": "_clouddeploy_21_KubernetesConfigOut",
        "ServiceNetworkingIn": "_clouddeploy_22_ServiceNetworkingIn",
        "ServiceNetworkingOut": "_clouddeploy_23_ServiceNetworkingOut",
        "RuntimeConfigIn": "_clouddeploy_24_RuntimeConfigIn",
        "RuntimeConfigOut": "_clouddeploy_25_RuntimeConfigOut",
        "ListLocationsResponseIn": "_clouddeploy_26_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_clouddeploy_27_ListLocationsResponseOut",
        "CloudRunLocationIn": "_clouddeploy_28_CloudRunLocationIn",
        "CloudRunLocationOut": "_clouddeploy_29_CloudRunLocationOut",
        "IgnoreJobRequestIn": "_clouddeploy_30_IgnoreJobRequestIn",
        "IgnoreJobRequestOut": "_clouddeploy_31_IgnoreJobRequestOut",
        "CreateChildRolloutJobRunIn": "_clouddeploy_32_CreateChildRolloutJobRunIn",
        "CreateChildRolloutJobRunOut": "_clouddeploy_33_CreateChildRolloutJobRunOut",
        "PrivatePoolIn": "_clouddeploy_34_PrivatePoolIn",
        "PrivatePoolOut": "_clouddeploy_35_PrivatePoolOut",
        "AbandonReleaseRequestIn": "_clouddeploy_36_AbandonReleaseRequestIn",
        "AbandonReleaseRequestOut": "_clouddeploy_37_AbandonReleaseRequestOut",
        "ReleaseReadyConditionIn": "_clouddeploy_38_ReleaseReadyConditionIn",
        "ReleaseReadyConditionOut": "_clouddeploy_39_ReleaseReadyConditionOut",
        "TestIamPermissionsResponseIn": "_clouddeploy_40_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_clouddeploy_41_TestIamPermissionsResponseOut",
        "MultiTargetIn": "_clouddeploy_42_MultiTargetIn",
        "MultiTargetOut": "_clouddeploy_43_MultiTargetOut",
        "CloudRunConfigIn": "_clouddeploy_44_CloudRunConfigIn",
        "CloudRunConfigOut": "_clouddeploy_45_CloudRunConfigOut",
        "SerialPipelineIn": "_clouddeploy_46_SerialPipelineIn",
        "SerialPipelineOut": "_clouddeploy_47_SerialPipelineOut",
        "AuditLogConfigIn": "_clouddeploy_48_AuditLogConfigIn",
        "AuditLogConfigOut": "_clouddeploy_49_AuditLogConfigOut",
        "StrategyIn": "_clouddeploy_50_StrategyIn",
        "StrategyOut": "_clouddeploy_51_StrategyOut",
        "PhaseIn": "_clouddeploy_52_PhaseIn",
        "PhaseOut": "_clouddeploy_53_PhaseOut",
        "GatewayServiceMeshIn": "_clouddeploy_54_GatewayServiceMeshIn",
        "GatewayServiceMeshOut": "_clouddeploy_55_GatewayServiceMeshOut",
        "LocationIn": "_clouddeploy_56_LocationIn",
        "LocationOut": "_clouddeploy_57_LocationOut",
        "DeployJobRunIn": "_clouddeploy_58_DeployJobRunIn",
        "DeployJobRunOut": "_clouddeploy_59_DeployJobRunOut",
        "MetadataIn": "_clouddeploy_60_MetadataIn",
        "MetadataOut": "_clouddeploy_61_MetadataOut",
        "CancelRolloutRequestIn": "_clouddeploy_62_CancelRolloutRequestIn",
        "CancelRolloutRequestOut": "_clouddeploy_63_CancelRolloutRequestOut",
        "TargetsTypeConditionIn": "_clouddeploy_64_TargetsTypeConditionIn",
        "TargetsTypeConditionOut": "_clouddeploy_65_TargetsTypeConditionOut",
        "AuditConfigIn": "_clouddeploy_66_AuditConfigIn",
        "AuditConfigOut": "_clouddeploy_67_AuditConfigOut",
        "AdvanceRolloutResponseIn": "_clouddeploy_68_AdvanceRolloutResponseIn",
        "AdvanceRolloutResponseOut": "_clouddeploy_69_AdvanceRolloutResponseOut",
        "SetIamPolicyRequestIn": "_clouddeploy_70_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_clouddeploy_71_SetIamPolicyRequestOut",
        "ListRolloutsResponseIn": "_clouddeploy_72_ListRolloutsResponseIn",
        "ListRolloutsResponseOut": "_clouddeploy_73_ListRolloutsResponseOut",
        "OperationMetadataIn": "_clouddeploy_74_OperationMetadataIn",
        "OperationMetadataOut": "_clouddeploy_75_OperationMetadataOut",
        "DeploymentJobsIn": "_clouddeploy_76_DeploymentJobsIn",
        "DeploymentJobsOut": "_clouddeploy_77_DeploymentJobsOut",
        "BindingIn": "_clouddeploy_78_BindingIn",
        "BindingOut": "_clouddeploy_79_BindingOut",
        "TerminateJobRunResponseIn": "_clouddeploy_80_TerminateJobRunResponseIn",
        "TerminateJobRunResponseOut": "_clouddeploy_81_TerminateJobRunResponseOut",
        "TargetArtifactIn": "_clouddeploy_82_TargetArtifactIn",
        "TargetArtifactOut": "_clouddeploy_83_TargetArtifactOut",
        "CanaryDeploymentIn": "_clouddeploy_84_CanaryDeploymentIn",
        "CanaryDeploymentOut": "_clouddeploy_85_CanaryDeploymentOut",
        "RolloutIn": "_clouddeploy_86_RolloutIn",
        "RolloutOut": "_clouddeploy_87_RolloutOut",
        "ApproveRolloutResponseIn": "_clouddeploy_88_ApproveRolloutResponseIn",
        "ApproveRolloutResponseOut": "_clouddeploy_89_ApproveRolloutResponseOut",
        "AbandonReleaseResponseIn": "_clouddeploy_90_AbandonReleaseResponseIn",
        "AbandonReleaseResponseOut": "_clouddeploy_91_AbandonReleaseResponseOut",
        "CloudRunRenderMetadataIn": "_clouddeploy_92_CloudRunRenderMetadataIn",
        "CloudRunRenderMetadataOut": "_clouddeploy_93_CloudRunRenderMetadataOut",
        "EmptyIn": "_clouddeploy_94_EmptyIn",
        "EmptyOut": "_clouddeploy_95_EmptyOut",
        "SkaffoldVersionIn": "_clouddeploy_96_SkaffoldVersionIn",
        "SkaffoldVersionOut": "_clouddeploy_97_SkaffoldVersionOut",
        "ListTargetsResponseIn": "_clouddeploy_98_ListTargetsResponseIn",
        "ListTargetsResponseOut": "_clouddeploy_99_ListTargetsResponseOut",
        "PipelineReadyConditionIn": "_clouddeploy_100_PipelineReadyConditionIn",
        "PipelineReadyConditionOut": "_clouddeploy_101_PipelineReadyConditionOut",
        "CustomCanaryDeploymentIn": "_clouddeploy_102_CustomCanaryDeploymentIn",
        "CustomCanaryDeploymentOut": "_clouddeploy_103_CustomCanaryDeploymentOut",
        "SkaffoldSupportedConditionIn": "_clouddeploy_104_SkaffoldSupportedConditionIn",
        "SkaffoldSupportedConditionOut": "_clouddeploy_105_SkaffoldSupportedConditionOut",
        "VerifyJobRunIn": "_clouddeploy_106_VerifyJobRunIn",
        "VerifyJobRunOut": "_clouddeploy_107_VerifyJobRunOut",
        "DeployJobIn": "_clouddeploy_108_DeployJobIn",
        "DeployJobOut": "_clouddeploy_109_DeployJobOut",
        "ListReleasesResponseIn": "_clouddeploy_110_ListReleasesResponseIn",
        "ListReleasesResponseOut": "_clouddeploy_111_ListReleasesResponseOut",
        "DeliveryPipelineNotificationEventIn": "_clouddeploy_112_DeliveryPipelineNotificationEventIn",
        "DeliveryPipelineNotificationEventOut": "_clouddeploy_113_DeliveryPipelineNotificationEventOut",
        "PhaseArtifactIn": "_clouddeploy_114_PhaseArtifactIn",
        "PhaseArtifactOut": "_clouddeploy_115_PhaseArtifactOut",
        "JobRunIn": "_clouddeploy_116_JobRunIn",
        "JobRunOut": "_clouddeploy_117_JobRunOut",
        "ReleaseIn": "_clouddeploy_118_ReleaseIn",
        "ReleaseOut": "_clouddeploy_119_ReleaseOut",
        "DeployArtifactIn": "_clouddeploy_120_DeployArtifactIn",
        "DeployArtifactOut": "_clouddeploy_121_DeployArtifactOut",
        "IgnoreJobResponseIn": "_clouddeploy_122_IgnoreJobResponseIn",
        "IgnoreJobResponseOut": "_clouddeploy_123_IgnoreJobResponseOut",
        "TerminateJobRunRequestIn": "_clouddeploy_124_TerminateJobRunRequestIn",
        "TerminateJobRunRequestOut": "_clouddeploy_125_TerminateJobRunRequestOut",
        "ListJobRunsResponseIn": "_clouddeploy_126_ListJobRunsResponseIn",
        "ListJobRunsResponseOut": "_clouddeploy_127_ListJobRunsResponseOut",
        "AdvanceChildRolloutJobRunIn": "_clouddeploy_128_AdvanceChildRolloutJobRunIn",
        "AdvanceChildRolloutJobRunOut": "_clouddeploy_129_AdvanceChildRolloutJobRunOut",
        "TargetNotificationEventIn": "_clouddeploy_130_TargetNotificationEventIn",
        "TargetNotificationEventOut": "_clouddeploy_131_TargetNotificationEventOut",
        "TargetRenderIn": "_clouddeploy_132_TargetRenderIn",
        "TargetRenderOut": "_clouddeploy_133_TargetRenderOut",
        "ConfigIn": "_clouddeploy_134_ConfigIn",
        "ConfigOut": "_clouddeploy_135_ConfigOut",
        "DeliveryPipelineIn": "_clouddeploy_136_DeliveryPipelineIn",
        "DeliveryPipelineOut": "_clouddeploy_137_DeliveryPipelineOut",
        "RetryJobRequestIn": "_clouddeploy_138_RetryJobRequestIn",
        "RetryJobRequestOut": "_clouddeploy_139_RetryJobRequestOut",
        "DefaultPoolIn": "_clouddeploy_140_DefaultPoolIn",
        "DefaultPoolOut": "_clouddeploy_141_DefaultPoolOut",
        "ReleaseConditionIn": "_clouddeploy_142_ReleaseConditionIn",
        "ReleaseConditionOut": "_clouddeploy_143_ReleaseConditionOut",
        "PipelineConditionIn": "_clouddeploy_144_PipelineConditionIn",
        "PipelineConditionOut": "_clouddeploy_145_PipelineConditionOut",
        "CancelRolloutResponseIn": "_clouddeploy_146_CancelRolloutResponseIn",
        "CancelRolloutResponseOut": "_clouddeploy_147_CancelRolloutResponseOut",
        "CreateChildRolloutJobIn": "_clouddeploy_148_CreateChildRolloutJobIn",
        "CreateChildRolloutJobOut": "_clouddeploy_149_CreateChildRolloutJobOut",
        "ApproveRolloutRequestIn": "_clouddeploy_150_ApproveRolloutRequestIn",
        "ApproveRolloutRequestOut": "_clouddeploy_151_ApproveRolloutRequestOut",
        "StatusIn": "_clouddeploy_152_StatusIn",
        "StatusOut": "_clouddeploy_153_StatusOut",
        "PhaseConfigIn": "_clouddeploy_154_PhaseConfigIn",
        "PhaseConfigOut": "_clouddeploy_155_PhaseConfigOut",
        "ListDeliveryPipelinesResponseIn": "_clouddeploy_156_ListDeliveryPipelinesResponseIn",
        "ListDeliveryPipelinesResponseOut": "_clouddeploy_157_ListDeliveryPipelinesResponseOut",
        "StandardIn": "_clouddeploy_158_StandardIn",
        "StandardOut": "_clouddeploy_159_StandardOut",
        "CloudRunMetadataIn": "_clouddeploy_160_CloudRunMetadataIn",
        "CloudRunMetadataOut": "_clouddeploy_161_CloudRunMetadataOut",
        "TargetIn": "_clouddeploy_162_TargetIn",
        "TargetOut": "_clouddeploy_163_TargetOut",
        "JobRunNotificationEventIn": "_clouddeploy_164_JobRunNotificationEventIn",
        "JobRunNotificationEventOut": "_clouddeploy_165_JobRunNotificationEventOut",
        "CancelOperationRequestIn": "_clouddeploy_166_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_clouddeploy_167_CancelOperationRequestOut",
        "BuildArtifactIn": "_clouddeploy_168_BuildArtifactIn",
        "BuildArtifactOut": "_clouddeploy_169_BuildArtifactOut",
        "RenderMetadataIn": "_clouddeploy_170_RenderMetadataIn",
        "RenderMetadataOut": "_clouddeploy_171_RenderMetadataOut",
        "TargetsPresentConditionIn": "_clouddeploy_172_TargetsPresentConditionIn",
        "TargetsPresentConditionOut": "_clouddeploy_173_TargetsPresentConditionOut",
        "ReleaseRenderEventIn": "_clouddeploy_174_ReleaseRenderEventIn",
        "ReleaseRenderEventOut": "_clouddeploy_175_ReleaseRenderEventOut",
        "ChildRolloutJobsIn": "_clouddeploy_176_ChildRolloutJobsIn",
        "ChildRolloutJobsOut": "_clouddeploy_177_ChildRolloutJobsOut",
        "DateIn": "_clouddeploy_178_DateIn",
        "DateOut": "_clouddeploy_179_DateOut",
        "ListOperationsResponseIn": "_clouddeploy_180_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_clouddeploy_181_ListOperationsResponseOut",
        "RolloutNotificationEventIn": "_clouddeploy_182_RolloutNotificationEventIn",
        "RolloutNotificationEventOut": "_clouddeploy_183_RolloutNotificationEventOut",
        "ExprIn": "_clouddeploy_184_ExprIn",
        "ExprOut": "_clouddeploy_185_ExprOut",
        "AdvanceChildRolloutJobIn": "_clouddeploy_186_AdvanceChildRolloutJobIn",
        "AdvanceChildRolloutJobOut": "_clouddeploy_187_AdvanceChildRolloutJobOut",
        "CanaryIn": "_clouddeploy_188_CanaryIn",
        "CanaryOut": "_clouddeploy_189_CanaryOut",
        "JobIn": "_clouddeploy_190_JobIn",
        "JobOut": "_clouddeploy_191_JobOut",
        "AdvanceRolloutRequestIn": "_clouddeploy_192_AdvanceRolloutRequestIn",
        "AdvanceRolloutRequestOut": "_clouddeploy_193_AdvanceRolloutRequestOut",
        "StageIn": "_clouddeploy_194_StageIn",
        "StageOut": "_clouddeploy_195_StageOut",
        "GkeClusterIn": "_clouddeploy_196_GkeClusterIn",
        "GkeClusterOut": "_clouddeploy_197_GkeClusterOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["OperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
    types["PolicyIn"] = t.struct(
        {
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["VerifyJobIn"] = t.struct({"_": t.string().optional()}).named(
        renames["VerifyJobIn"]
    )
    types["VerifyJobOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["VerifyJobOut"])
    types["ExecutionConfigIn"] = t.struct(
        {
            "executionTimeout": t.string().optional(),
            "artifactStorage": t.string().optional(),
            "privatePool": t.proxy(renames["PrivatePoolIn"]).optional(),
            "defaultPool": t.proxy(renames["DefaultPoolIn"]).optional(),
            "serviceAccount": t.string().optional(),
            "usages": t.array(t.string()),
            "workerPool": t.string().optional(),
        }
    ).named(renames["ExecutionConfigIn"])
    types["ExecutionConfigOut"] = t.struct(
        {
            "executionTimeout": t.string().optional(),
            "artifactStorage": t.string().optional(),
            "privatePool": t.proxy(renames["PrivatePoolOut"]).optional(),
            "defaultPool": t.proxy(renames["DefaultPoolOut"]).optional(),
            "serviceAccount": t.string().optional(),
            "usages": t.array(t.string()),
            "workerPool": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecutionConfigOut"])
    types["ReleaseNotificationEventIn"] = t.struct(
        {
            "message": t.string().optional(),
            "type": t.string().optional(),
            "release": t.string().optional(),
        }
    ).named(renames["ReleaseNotificationEventIn"])
    types["ReleaseNotificationEventOut"] = t.struct(
        {
            "message": t.string().optional(),
            "type": t.string().optional(),
            "release": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReleaseNotificationEventOut"])
    types["AnthosClusterIn"] = t.struct({"membership": t.string().optional()}).named(
        renames["AnthosClusterIn"]
    )
    types["AnthosClusterOut"] = t.struct(
        {
            "membership": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnthosClusterOut"])
    types["RetryJobResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RetryJobResponseIn"]
    )
    types["RetryJobResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RetryJobResponseOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["DeployJobRunMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeployJobRunMetadataIn"]
    )
    types["DeployJobRunMetadataOut"] = t.struct(
        {
            "cloudRun": t.proxy(renames["CloudRunMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeployJobRunMetadataOut"])
    types["KubernetesConfigIn"] = t.struct(
        {
            "gatewayServiceMesh": t.proxy(renames["GatewayServiceMeshIn"]).optional(),
            "serviceNetworking": t.proxy(renames["ServiceNetworkingIn"]).optional(),
        }
    ).named(renames["KubernetesConfigIn"])
    types["KubernetesConfigOut"] = t.struct(
        {
            "gatewayServiceMesh": t.proxy(renames["GatewayServiceMeshOut"]).optional(),
            "serviceNetworking": t.proxy(renames["ServiceNetworkingOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KubernetesConfigOut"])
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
    types["CloudRunLocationIn"] = t.struct({"location": t.string()}).named(
        renames["CloudRunLocationIn"]
    )
    types["CloudRunLocationOut"] = t.struct(
        {"location": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CloudRunLocationOut"])
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
    types["PrivatePoolIn"] = t.struct(
        {
            "artifactStorage": t.string().optional(),
            "workerPool": t.string(),
            "serviceAccount": t.string().optional(),
        }
    ).named(renames["PrivatePoolIn"])
    types["PrivatePoolOut"] = t.struct(
        {
            "artifactStorage": t.string().optional(),
            "workerPool": t.string(),
            "serviceAccount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrivatePoolOut"])
    types["AbandonReleaseRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AbandonReleaseRequestIn"]
    )
    types["AbandonReleaseRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AbandonReleaseRequestOut"])
    types["ReleaseReadyConditionIn"] = t.struct(
        {"status": t.boolean().optional()}
    ).named(renames["ReleaseReadyConditionIn"])
    types["ReleaseReadyConditionOut"] = t.struct(
        {
            "status": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReleaseReadyConditionOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["MultiTargetIn"] = t.struct({"targetIds": t.array(t.string())}).named(
        renames["MultiTargetIn"]
    )
    types["MultiTargetOut"] = t.struct(
        {
            "targetIds": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MultiTargetOut"])
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
    types["PhaseIn"] = t.struct({"_": t.string().optional()}).named(renames["PhaseIn"])
    types["PhaseOut"] = t.struct(
        {
            "state": t.string().optional(),
            "id": t.string().optional(),
            "skipMessage": t.string().optional(),
            "childRolloutJobs": t.proxy(renames["ChildRolloutJobsOut"]).optional(),
            "deploymentJobs": t.proxy(renames["DeploymentJobsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhaseOut"])
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
    types["LocationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["DeployJobRunIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeployJobRunIn"]
    )
    types["DeployJobRunOut"] = t.struct(
        {
            "metadata": t.proxy(renames["DeployJobRunMetadataOut"]).optional(),
            "failureMessage": t.string().optional(),
            "build": t.string().optional(),
            "failureCause": t.string().optional(),
            "artifact": t.proxy(renames["DeployArtifactOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeployJobRunOut"])
    types["MetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MetadataIn"]
    )
    types["MetadataOut"] = t.struct(
        {
            "cloudRun": t.proxy(renames["CloudRunMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetadataOut"])
    types["CancelRolloutRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelRolloutRequestIn"]
    )
    types["CancelRolloutRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelRolloutRequestOut"])
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
    types["AdvanceRolloutResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AdvanceRolloutResponseIn"]
    )
    types["AdvanceRolloutResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AdvanceRolloutResponseOut"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "policy": t.proxy(renames["PolicyIn"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
    types["ListRolloutsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "rollouts": t.array(t.proxy(renames["RolloutIn"])).optional(),
        }
    ).named(renames["ListRolloutsResponseIn"])
    types["ListRolloutsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "rollouts": t.array(t.proxy(renames["RolloutOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListRolloutsResponseOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "target": t.string().optional(),
            "createTime": t.string().optional(),
            "endTime": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "verb": t.string().optional(),
            "statusMessage": t.string().optional(),
            "apiVersion": t.string().optional(),
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
    types["TerminateJobRunResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["TerminateJobRunResponseIn"]
    )
    types["TerminateJobRunResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["TerminateJobRunResponseOut"])
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
    types["CanaryDeploymentIn"] = t.struct(
        {"percentages": t.array(t.integer()), "verify": t.boolean().optional()}
    ).named(renames["CanaryDeploymentIn"])
    types["CanaryDeploymentOut"] = t.struct(
        {
            "percentages": t.array(t.integer()),
            "verify": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CanaryDeploymentOut"])
    types["RolloutIn"] = t.struct(
        {
            "name": t.string().optional(),
            "targetId": t.string(),
            "description": t.string().optional(),
            "etag": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["RolloutIn"])
    types["RolloutOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "deployStartTime": t.string().optional(),
            "name": t.string().optional(),
            "approvalState": t.string().optional(),
            "deployEndTime": t.string().optional(),
            "targetId": t.string(),
            "controllerRollout": t.string().optional(),
            "failureReason": t.string().optional(),
            "phases": t.array(t.proxy(renames["PhaseOut"])).optional(),
            "description": t.string().optional(),
            "deployingBuild": t.string().optional(),
            "etag": t.string().optional(),
            "enqueueTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "deployFailureCause": t.string().optional(),
            "approveTime": t.string().optional(),
            "uid": t.string().optional(),
            "state": t.string().optional(),
            "metadata": t.proxy(renames["MetadataOut"]).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RolloutOut"])
    types["ApproveRolloutResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ApproveRolloutResponseIn"]
    )
    types["ApproveRolloutResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ApproveRolloutResponseOut"])
    types["AbandonReleaseResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AbandonReleaseResponseIn"]
    )
    types["AbandonReleaseResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AbandonReleaseResponseOut"])
    types["CloudRunRenderMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CloudRunRenderMetadataIn"]
    )
    types["CloudRunRenderMetadataOut"] = t.struct(
        {
            "service": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudRunRenderMetadataOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["SkaffoldVersionIn"] = t.struct(
        {
            "version": t.string().optional(),
            "supportEndDate": t.proxy(renames["DateIn"]).optional(),
            "maintenanceModeTime": t.string().optional(),
            "supportExpirationTime": t.string().optional(),
        }
    ).named(renames["SkaffoldVersionIn"])
    types["SkaffoldVersionOut"] = t.struct(
        {
            "version": t.string().optional(),
            "supportEndDate": t.proxy(renames["DateOut"]).optional(),
            "maintenanceModeTime": t.string().optional(),
            "supportExpirationTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SkaffoldVersionOut"])
    types["ListTargetsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "targets": t.array(t.proxy(renames["TargetIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListTargetsResponseIn"])
    types["ListTargetsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "targets": t.array(t.proxy(renames["TargetOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTargetsResponseOut"])
    types["PipelineReadyConditionIn"] = t.struct(
        {"updateTime": t.string().optional(), "status": t.boolean().optional()}
    ).named(renames["PipelineReadyConditionIn"])
    types["PipelineReadyConditionOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "status": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PipelineReadyConditionOut"])
    types["CustomCanaryDeploymentIn"] = t.struct(
        {"phaseConfigs": t.array(t.proxy(renames["PhaseConfigIn"]))}
    ).named(renames["CustomCanaryDeploymentIn"])
    types["CustomCanaryDeploymentOut"] = t.struct(
        {
            "phaseConfigs": t.array(t.proxy(renames["PhaseConfigOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomCanaryDeploymentOut"])
    types["SkaffoldSupportedConditionIn"] = t.struct(
        {
            "maintenanceModeTime": t.string().optional(),
            "status": t.boolean().optional(),
            "supportExpirationTime": t.string().optional(),
            "skaffoldSupportState": t.string().optional(),
        }
    ).named(renames["SkaffoldSupportedConditionIn"])
    types["SkaffoldSupportedConditionOut"] = t.struct(
        {
            "maintenanceModeTime": t.string().optional(),
            "status": t.boolean().optional(),
            "supportExpirationTime": t.string().optional(),
            "skaffoldSupportState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SkaffoldSupportedConditionOut"])
    types["VerifyJobRunIn"] = t.struct({"_": t.string().optional()}).named(
        renames["VerifyJobRunIn"]
    )
    types["VerifyJobRunOut"] = t.struct(
        {
            "eventLogPath": t.string().optional(),
            "artifactUri": t.string().optional(),
            "build": t.string().optional(),
            "failureMessage": t.string().optional(),
            "failureCause": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VerifyJobRunOut"])
    types["DeployJobIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeployJobIn"]
    )
    types["DeployJobOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeployJobOut"])
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
    types["DeliveryPipelineNotificationEventIn"] = t.struct(
        {
            "type": t.string().optional(),
            "message": t.string().optional(),
            "deliveryPipeline": t.string().optional(),
        }
    ).named(renames["DeliveryPipelineNotificationEventIn"])
    types["DeliveryPipelineNotificationEventOut"] = t.struct(
        {
            "type": t.string().optional(),
            "message": t.string().optional(),
            "deliveryPipeline": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeliveryPipelineNotificationEventOut"])
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
    types["JobRunIn"] = t.struct({"name": t.string().optional()}).named(
        renames["JobRunIn"]
    )
    types["JobRunOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "state": t.string().optional(),
            "advanceChildRolloutJobRun": t.proxy(
                renames["AdvanceChildRolloutJobRunOut"]
            ).optional(),
            "verifyJobRun": t.proxy(renames["VerifyJobRunOut"]).optional(),
            "startTime": t.string().optional(),
            "jobId": t.string().optional(),
            "createTime": t.string().optional(),
            "endTime": t.string().optional(),
            "phaseId": t.string().optional(),
            "name": t.string().optional(),
            "createChildRolloutJobRun": t.proxy(
                renames["CreateChildRolloutJobRunOut"]
            ).optional(),
            "deployJobRun": t.proxy(renames["DeployJobRunOut"]).optional(),
            "uid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobRunOut"])
    types["ReleaseIn"] = t.struct(
        {
            "skaffoldConfigPath": t.string().optional(),
            "skaffoldVersion": t.string().optional(),
            "etag": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "skaffoldConfigUri": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "buildArtifacts": t.array(t.proxy(renames["BuildArtifactIn"])).optional(),
        }
    ).named(renames["ReleaseIn"])
    types["ReleaseOut"] = t.struct(
        {
            "abandoned": t.boolean().optional(),
            "skaffoldConfigPath": t.string().optional(),
            "renderEndTime": t.string().optional(),
            "skaffoldVersion": t.string().optional(),
            "targetArtifacts": t.struct({"_": t.string().optional()}).optional(),
            "targetSnapshots": t.array(t.proxy(renames["TargetOut"])).optional(),
            "etag": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "uid": t.string().optional(),
            "createTime": t.string().optional(),
            "renderState": t.string().optional(),
            "condition": t.proxy(renames["ReleaseConditionOut"]).optional(),
            "skaffoldConfigUri": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "deliveryPipelineSnapshot": t.proxy(
                renames["DeliveryPipelineOut"]
            ).optional(),
            "renderStartTime": t.string().optional(),
            "targetRenders": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "buildArtifacts": t.array(t.proxy(renames["BuildArtifactOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReleaseOut"])
    types["DeployArtifactIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeployArtifactIn"]
    )
    types["DeployArtifactOut"] = t.struct(
        {
            "artifactUri": t.string().optional(),
            "manifestPaths": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeployArtifactOut"])
    types["IgnoreJobResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["IgnoreJobResponseIn"]
    )
    types["IgnoreJobResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["IgnoreJobResponseOut"])
    types["TerminateJobRunRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["TerminateJobRunRequestIn"]
    )
    types["TerminateJobRunRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["TerminateJobRunRequestOut"])
    types["ListJobRunsResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "jobRuns": t.array(t.proxy(renames["JobRunIn"])).optional(),
        }
    ).named(renames["ListJobRunsResponseIn"])
    types["ListJobRunsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "jobRuns": t.array(t.proxy(renames["JobRunOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListJobRunsResponseOut"])
    types["AdvanceChildRolloutJobRunIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AdvanceChildRolloutJobRunIn"]
    )
    types["AdvanceChildRolloutJobRunOut"] = t.struct(
        {
            "rolloutPhaseId": t.string().optional(),
            "rollout": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdvanceChildRolloutJobRunOut"])
    types["TargetNotificationEventIn"] = t.struct(
        {
            "target": t.string().optional(),
            "type": t.string().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["TargetNotificationEventIn"])
    types["TargetNotificationEventOut"] = t.struct(
        {
            "target": t.string().optional(),
            "type": t.string().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetNotificationEventOut"])
    types["TargetRenderIn"] = t.struct({"_": t.string().optional()}).named(
        renames["TargetRenderIn"]
    )
    types["TargetRenderOut"] = t.struct(
        {
            "renderingState": t.string().optional(),
            "metadata": t.proxy(renames["RenderMetadataOut"]).optional(),
            "failureMessage": t.string().optional(),
            "failureCause": t.string().optional(),
            "renderingBuild": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetRenderOut"])
    types["ConfigIn"] = t.struct(
        {
            "defaultSkaffoldVersion": t.string().optional(),
            "name": t.string().optional(),
            "supportedVersions": t.array(
                t.proxy(renames["SkaffoldVersionIn"])
            ).optional(),
        }
    ).named(renames["ConfigIn"])
    types["ConfigOut"] = t.struct(
        {
            "defaultSkaffoldVersion": t.string().optional(),
            "name": t.string().optional(),
            "supportedVersions": t.array(
                t.proxy(renames["SkaffoldVersionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigOut"])
    types["DeliveryPipelineIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "serialPipeline": t.proxy(renames["SerialPipelineIn"]).optional(),
            "suspended": t.boolean().optional(),
            "name": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["DeliveryPipelineIn"])
    types["DeliveryPipelineOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "etag": t.string().optional(),
            "updateTime": t.string().optional(),
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "condition": t.proxy(renames["PipelineConditionOut"]).optional(),
            "serialPipeline": t.proxy(renames["SerialPipelineOut"]).optional(),
            "suspended": t.boolean().optional(),
            "name": t.string().optional(),
            "uid": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeliveryPipelineOut"])
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
            "serviceAccount": t.string().optional(),
            "artifactStorage": t.string().optional(),
        }
    ).named(renames["DefaultPoolIn"])
    types["DefaultPoolOut"] = t.struct(
        {
            "serviceAccount": t.string().optional(),
            "artifactStorage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DefaultPoolOut"])
    types["ReleaseConditionIn"] = t.struct(
        {
            "releaseReadyCondition": t.proxy(
                renames["ReleaseReadyConditionIn"]
            ).optional(),
            "skaffoldSupportedCondition": t.proxy(
                renames["SkaffoldSupportedConditionIn"]
            ).optional(),
        }
    ).named(renames["ReleaseConditionIn"])
    types["ReleaseConditionOut"] = t.struct(
        {
            "releaseReadyCondition": t.proxy(
                renames["ReleaseReadyConditionOut"]
            ).optional(),
            "skaffoldSupportedCondition": t.proxy(
                renames["SkaffoldSupportedConditionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReleaseConditionOut"])
    types["PipelineConditionIn"] = t.struct(
        {
            "targetsPresentCondition": t.proxy(
                renames["TargetsPresentConditionIn"]
            ).optional(),
            "targetsTypeCondition": t.proxy(
                renames["TargetsTypeConditionIn"]
            ).optional(),
            "pipelineReadyCondition": t.proxy(
                renames["PipelineReadyConditionIn"]
            ).optional(),
        }
    ).named(renames["PipelineConditionIn"])
    types["PipelineConditionOut"] = t.struct(
        {
            "targetsPresentCondition": t.proxy(
                renames["TargetsPresentConditionOut"]
            ).optional(),
            "targetsTypeCondition": t.proxy(
                renames["TargetsTypeConditionOut"]
            ).optional(),
            "pipelineReadyCondition": t.proxy(
                renames["PipelineReadyConditionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PipelineConditionOut"])
    types["CancelRolloutResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelRolloutResponseIn"]
    )
    types["CancelRolloutResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelRolloutResponseOut"])
    types["CreateChildRolloutJobIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CreateChildRolloutJobIn"]
    )
    types["CreateChildRolloutJobOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CreateChildRolloutJobOut"])
    types["ApproveRolloutRequestIn"] = t.struct({"approved": t.boolean()}).named(
        renames["ApproveRolloutRequestIn"]
    )
    types["ApproveRolloutRequestOut"] = t.struct(
        {"approved": t.boolean(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ApproveRolloutRequestOut"])
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
    types["PhaseConfigIn"] = t.struct(
        {
            "phaseId": t.string(),
            "percentage": t.integer(),
            "verify": t.boolean().optional(),
            "profiles": t.array(t.string()).optional(),
        }
    ).named(renames["PhaseConfigIn"])
    types["PhaseConfigOut"] = t.struct(
        {
            "phaseId": t.string(),
            "percentage": t.integer(),
            "verify": t.boolean().optional(),
            "profiles": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhaseConfigOut"])
    types["ListDeliveryPipelinesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "deliveryPipelines": t.array(
                t.proxy(renames["DeliveryPipelineIn"])
            ).optional(),
        }
    ).named(renames["ListDeliveryPipelinesResponseIn"])
    types["ListDeliveryPipelinesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "deliveryPipelines": t.array(
                t.proxy(renames["DeliveryPipelineOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDeliveryPipelinesResponseOut"])
    types["StandardIn"] = t.struct({"verify": t.boolean().optional()}).named(
        renames["StandardIn"]
    )
    types["StandardOut"] = t.struct(
        {
            "verify": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StandardOut"])
    types["CloudRunMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CloudRunMetadataIn"]
    )
    types["CloudRunMetadataOut"] = t.struct(
        {
            "service": t.string().optional(),
            "serviceUrls": t.array(t.string()).optional(),
            "revision": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudRunMetadataOut"])
    types["TargetIn"] = t.struct(
        {
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "etag": t.string().optional(),
            "requireApproval": t.boolean().optional(),
            "run": t.proxy(renames["CloudRunLocationIn"]).optional(),
            "gke": t.proxy(renames["GkeClusterIn"]).optional(),
            "executionConfigs": t.array(
                t.proxy(renames["ExecutionConfigIn"])
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "multiTarget": t.proxy(renames["MultiTargetIn"]).optional(),
            "anthosCluster": t.proxy(renames["AnthosClusterIn"]).optional(),
        }
    ).named(renames["TargetIn"])
    types["TargetOut"] = t.struct(
        {
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "etag": t.string().optional(),
            "requireApproval": t.boolean().optional(),
            "run": t.proxy(renames["CloudRunLocationOut"]).optional(),
            "uid": t.string().optional(),
            "targetId": t.string().optional(),
            "updateTime": t.string().optional(),
            "gke": t.proxy(renames["GkeClusterOut"]).optional(),
            "executionConfigs": t.array(
                t.proxy(renames["ExecutionConfigOut"])
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "multiTarget": t.proxy(renames["MultiTargetOut"]).optional(),
            "anthosCluster": t.proxy(renames["AnthosClusterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetOut"])
    types["JobRunNotificationEventIn"] = t.struct(
        {
            "jobRun": t.string().optional(),
            "targetId": t.string().optional(),
            "releaseUid": t.string().optional(),
            "rolloutUid": t.string().optional(),
            "type": t.string().optional(),
            "pipelineUid": t.string().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["JobRunNotificationEventIn"])
    types["JobRunNotificationEventOut"] = t.struct(
        {
            "jobRun": t.string().optional(),
            "targetId": t.string().optional(),
            "releaseUid": t.string().optional(),
            "rolloutUid": t.string().optional(),
            "type": t.string().optional(),
            "pipelineUid": t.string().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobRunNotificationEventOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["BuildArtifactIn"] = t.struct(
        {"image": t.string().optional(), "tag": t.string().optional()}
    ).named(renames["BuildArtifactIn"])
    types["BuildArtifactOut"] = t.struct(
        {
            "image": t.string().optional(),
            "tag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuildArtifactOut"])
    types["RenderMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RenderMetadataIn"]
    )
    types["RenderMetadataOut"] = t.struct(
        {
            "cloudRun": t.proxy(renames["CloudRunRenderMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RenderMetadataOut"])
    types["TargetsPresentConditionIn"] = t.struct(
        {
            "missingTargets": t.array(t.string()).optional(),
            "status": t.boolean().optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["TargetsPresentConditionIn"])
    types["TargetsPresentConditionOut"] = t.struct(
        {
            "missingTargets": t.array(t.string()).optional(),
            "status": t.boolean().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetsPresentConditionOut"])
    types["ReleaseRenderEventIn"] = t.struct(
        {"release": t.string().optional(), "message": t.string().optional()}
    ).named(renames["ReleaseRenderEventIn"])
    types["ReleaseRenderEventOut"] = t.struct(
        {
            "release": t.string().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReleaseRenderEventOut"])
    types["ChildRolloutJobsIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ChildRolloutJobsIn"]
    )
    types["ChildRolloutJobsOut"] = t.struct(
        {
            "advanceRolloutJobs": t.array(t.proxy(renames["JobOut"])).optional(),
            "createRolloutJobs": t.array(t.proxy(renames["JobOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChildRolloutJobsOut"])
    types["DateIn"] = t.struct(
        {
            "month": t.integer().optional(),
            "year": t.integer().optional(),
            "day": t.integer().optional(),
        }
    ).named(renames["DateIn"])
    types["DateOut"] = t.struct(
        {
            "month": t.integer().optional(),
            "year": t.integer().optional(),
            "day": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
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
    types["RolloutNotificationEventIn"] = t.struct(
        {
            "message": t.string().optional(),
            "type": t.string().optional(),
            "targetId": t.string().optional(),
            "pipelineUid": t.string().optional(),
            "rollout": t.string().optional(),
            "releaseUid": t.string().optional(),
        }
    ).named(renames["RolloutNotificationEventIn"])
    types["RolloutNotificationEventOut"] = t.struct(
        {
            "message": t.string().optional(),
            "type": t.string().optional(),
            "targetId": t.string().optional(),
            "pipelineUid": t.string().optional(),
            "rollout": t.string().optional(),
            "releaseUid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RolloutNotificationEventOut"])
    types["ExprIn"] = t.struct(
        {
            "description": t.string().optional(),
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "description": t.string().optional(),
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["AdvanceChildRolloutJobIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AdvanceChildRolloutJobIn"]
    )
    types["AdvanceChildRolloutJobOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AdvanceChildRolloutJobOut"])
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
    types["JobIn"] = t.struct({"_": t.string().optional()}).named(renames["JobIn"])
    types["JobOut"] = t.struct(
        {
            "state": t.string().optional(),
            "deployJob": t.proxy(renames["DeployJobOut"]).optional(),
            "id": t.string().optional(),
            "jobRun": t.string().optional(),
            "skipMessage": t.string().optional(),
            "verifyJob": t.proxy(renames["VerifyJobOut"]).optional(),
            "advanceChildRolloutJob": t.proxy(
                renames["AdvanceChildRolloutJobOut"]
            ).optional(),
            "createChildRolloutJob": t.proxy(
                renames["CreateChildRolloutJobOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobOut"])
    types["AdvanceRolloutRequestIn"] = t.struct({"phaseId": t.string()}).named(
        renames["AdvanceRolloutRequestIn"]
    )
    types["AdvanceRolloutRequestOut"] = t.struct(
        {"phaseId": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AdvanceRolloutRequestOut"])
    types["StageIn"] = t.struct(
        {
            "targetId": t.string().optional(),
            "profiles": t.array(t.string()).optional(),
            "strategy": t.proxy(renames["StrategyIn"]).optional(),
        }
    ).named(renames["StageIn"])
    types["StageOut"] = t.struct(
        {
            "targetId": t.string().optional(),
            "profiles": t.array(t.string()).optional(),
            "strategy": t.proxy(renames["StrategyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StageOut"])
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

    functions = {}
    functions["projectsLocationsGet"] = clouddeploy.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsList"] = clouddeploy.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGetConfig"] = clouddeploy.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTargetsSetIamPolicy"] = clouddeploy.get(
        "v1/{parent}/targets",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTargetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTargetsTestIamPermissions"] = clouddeploy.get(
        "v1/{parent}/targets",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTargetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTargetsCreate"] = clouddeploy.get(
        "v1/{parent}/targets",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTargetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTargetsGetIamPolicy"] = clouddeploy.get(
        "v1/{parent}/targets",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTargetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTargetsDelete"] = clouddeploy.get(
        "v1/{parent}/targets",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTargetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTargetsPatch"] = clouddeploy.get(
        "v1/{parent}/targets",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTargetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTargetsGet"] = clouddeploy.get(
        "v1/{parent}/targets",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTargetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTargetsList"] = clouddeploy.get(
        "v1/{parent}/targets",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTargetsResponseOut"]),
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
    functions["projectsLocationsOperationsGet"] = clouddeploy.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDeliveryPipelinesPatch"] = clouddeploy.post(
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
    functions["projectsLocationsDeliveryPipelinesGet"] = clouddeploy.post(
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
    functions["projectsLocationsDeliveryPipelinesDelete"] = clouddeploy.post(
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
    functions["projectsLocationsDeliveryPipelinesGetIamPolicy"] = clouddeploy.post(
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
    functions["projectsLocationsDeliveryPipelinesList"] = clouddeploy.post(
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
    functions["projectsLocationsDeliveryPipelinesSetIamPolicy"] = clouddeploy.post(
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
    functions["projectsLocationsDeliveryPipelinesCreate"] = clouddeploy.post(
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
        "projectsLocationsDeliveryPipelinesTestIamPermissions"
    ] = clouddeploy.post(
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
    functions["projectsLocationsDeliveryPipelinesReleasesAbandon"] = clouddeploy.get(
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
    functions["projectsLocationsDeliveryPipelinesReleasesList"] = clouddeploy.get(
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
        "projectsLocationsDeliveryPipelinesReleasesRolloutsJobRunsGet"
    ] = clouddeploy.post(
        "v1/{name}:terminate",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TerminateJobRunResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDeliveryPipelinesReleasesRolloutsJobRunsList"
    ] = clouddeploy.post(
        "v1/{name}:terminate",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TerminateJobRunResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDeliveryPipelinesReleasesRolloutsJobRunsTerminate"
    ] = clouddeploy.post(
        "v1/{name}:terminate",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TerminateJobRunResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="clouddeploy",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
