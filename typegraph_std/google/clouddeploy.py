from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_clouddeploy():
    clouddeploy = HTTPRuntime("https://clouddeploy.googleapis.com/")

    renames = {
        "ErrorResponse": "_clouddeploy_1_ErrorResponse",
        "GkeClusterIn": "_clouddeploy_2_GkeClusterIn",
        "GkeClusterOut": "_clouddeploy_3_GkeClusterOut",
        "DeploymentJobsIn": "_clouddeploy_4_DeploymentJobsIn",
        "DeploymentJobsOut": "_clouddeploy_5_DeploymentJobsOut",
        "CancelOperationRequestIn": "_clouddeploy_6_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_clouddeploy_7_CancelOperationRequestOut",
        "RuntimeConfigIn": "_clouddeploy_8_RuntimeConfigIn",
        "RuntimeConfigOut": "_clouddeploy_9_RuntimeConfigOut",
        "DeployArtifactIn": "_clouddeploy_10_DeployArtifactIn",
        "DeployArtifactOut": "_clouddeploy_11_DeployArtifactOut",
        "BuildArtifactIn": "_clouddeploy_12_BuildArtifactIn",
        "BuildArtifactOut": "_clouddeploy_13_BuildArtifactOut",
        "TargetRenderIn": "_clouddeploy_14_TargetRenderIn",
        "TargetRenderOut": "_clouddeploy_15_TargetRenderOut",
        "VerifyJobRunIn": "_clouddeploy_16_VerifyJobRunIn",
        "VerifyJobRunOut": "_clouddeploy_17_VerifyJobRunOut",
        "ReleaseRenderEventIn": "_clouddeploy_18_ReleaseRenderEventIn",
        "ReleaseRenderEventOut": "_clouddeploy_19_ReleaseRenderEventOut",
        "StrategyIn": "_clouddeploy_20_StrategyIn",
        "StrategyOut": "_clouddeploy_21_StrategyOut",
        "SerialPipelineIn": "_clouddeploy_22_SerialPipelineIn",
        "SerialPipelineOut": "_clouddeploy_23_SerialPipelineOut",
        "MultiTargetIn": "_clouddeploy_24_MultiTargetIn",
        "MultiTargetOut": "_clouddeploy_25_MultiTargetOut",
        "BindingIn": "_clouddeploy_26_BindingIn",
        "BindingOut": "_clouddeploy_27_BindingOut",
        "ExecutionConfigIn": "_clouddeploy_28_ExecutionConfigIn",
        "ExecutionConfigOut": "_clouddeploy_29_ExecutionConfigOut",
        "CreateChildRolloutJobIn": "_clouddeploy_30_CreateChildRolloutJobIn",
        "CreateChildRolloutJobOut": "_clouddeploy_31_CreateChildRolloutJobOut",
        "TargetNotificationEventIn": "_clouddeploy_32_TargetNotificationEventIn",
        "TargetNotificationEventOut": "_clouddeploy_33_TargetNotificationEventOut",
        "CustomCanaryDeploymentIn": "_clouddeploy_34_CustomCanaryDeploymentIn",
        "CustomCanaryDeploymentOut": "_clouddeploy_35_CustomCanaryDeploymentOut",
        "RetryJobResponseIn": "_clouddeploy_36_RetryJobResponseIn",
        "RetryJobResponseOut": "_clouddeploy_37_RetryJobResponseOut",
        "PipelineReadyConditionIn": "_clouddeploy_38_PipelineReadyConditionIn",
        "PipelineReadyConditionOut": "_clouddeploy_39_PipelineReadyConditionOut",
        "CloudRunLocationIn": "_clouddeploy_40_CloudRunLocationIn",
        "CloudRunLocationOut": "_clouddeploy_41_CloudRunLocationOut",
        "DeployJobRunMetadataIn": "_clouddeploy_42_DeployJobRunMetadataIn",
        "DeployJobRunMetadataOut": "_clouddeploy_43_DeployJobRunMetadataOut",
        "RenderMetadataIn": "_clouddeploy_44_RenderMetadataIn",
        "RenderMetadataOut": "_clouddeploy_45_RenderMetadataOut",
        "ListJobRunsResponseIn": "_clouddeploy_46_ListJobRunsResponseIn",
        "ListJobRunsResponseOut": "_clouddeploy_47_ListJobRunsResponseOut",
        "RetryJobRequestIn": "_clouddeploy_48_RetryJobRequestIn",
        "RetryJobRequestOut": "_clouddeploy_49_RetryJobRequestOut",
        "AdvanceChildRolloutJobIn": "_clouddeploy_50_AdvanceChildRolloutJobIn",
        "AdvanceChildRolloutJobOut": "_clouddeploy_51_AdvanceChildRolloutJobOut",
        "DeliveryPipelineIn": "_clouddeploy_52_DeliveryPipelineIn",
        "DeliveryPipelineOut": "_clouddeploy_53_DeliveryPipelineOut",
        "ReleaseIn": "_clouddeploy_54_ReleaseIn",
        "ReleaseOut": "_clouddeploy_55_ReleaseOut",
        "PhaseIn": "_clouddeploy_56_PhaseIn",
        "PhaseOut": "_clouddeploy_57_PhaseOut",
        "TestIamPermissionsResponseIn": "_clouddeploy_58_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_clouddeploy_59_TestIamPermissionsResponseOut",
        "ListOperationsResponseIn": "_clouddeploy_60_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_clouddeploy_61_ListOperationsResponseOut",
        "AdvanceChildRolloutJobRunIn": "_clouddeploy_62_AdvanceChildRolloutJobRunIn",
        "AdvanceChildRolloutJobRunOut": "_clouddeploy_63_AdvanceChildRolloutJobRunOut",
        "ListRolloutsResponseIn": "_clouddeploy_64_ListRolloutsResponseIn",
        "ListRolloutsResponseOut": "_clouddeploy_65_ListRolloutsResponseOut",
        "GatewayServiceMeshIn": "_clouddeploy_66_GatewayServiceMeshIn",
        "GatewayServiceMeshOut": "_clouddeploy_67_GatewayServiceMeshOut",
        "AbandonReleaseResponseIn": "_clouddeploy_68_AbandonReleaseResponseIn",
        "AbandonReleaseResponseOut": "_clouddeploy_69_AbandonReleaseResponseOut",
        "OperationIn": "_clouddeploy_70_OperationIn",
        "OperationOut": "_clouddeploy_71_OperationOut",
        "ListTargetsResponseIn": "_clouddeploy_72_ListTargetsResponseIn",
        "ListTargetsResponseOut": "_clouddeploy_73_ListTargetsResponseOut",
        "PipelineConditionIn": "_clouddeploy_74_PipelineConditionIn",
        "PipelineConditionOut": "_clouddeploy_75_PipelineConditionOut",
        "AuditLogConfigIn": "_clouddeploy_76_AuditLogConfigIn",
        "AuditLogConfigOut": "_clouddeploy_77_AuditLogConfigOut",
        "ListDeliveryPipelinesResponseIn": "_clouddeploy_78_ListDeliveryPipelinesResponseIn",
        "ListDeliveryPipelinesResponseOut": "_clouddeploy_79_ListDeliveryPipelinesResponseOut",
        "JobRunNotificationEventIn": "_clouddeploy_80_JobRunNotificationEventIn",
        "JobRunNotificationEventOut": "_clouddeploy_81_JobRunNotificationEventOut",
        "TestIamPermissionsRequestIn": "_clouddeploy_82_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_clouddeploy_83_TestIamPermissionsRequestOut",
        "TargetIn": "_clouddeploy_84_TargetIn",
        "TargetOut": "_clouddeploy_85_TargetOut",
        "CloudRunConfigIn": "_clouddeploy_86_CloudRunConfigIn",
        "CloudRunConfigOut": "_clouddeploy_87_CloudRunConfigOut",
        "DeployJobRunIn": "_clouddeploy_88_DeployJobRunIn",
        "DeployJobRunOut": "_clouddeploy_89_DeployJobRunOut",
        "AbandonReleaseRequestIn": "_clouddeploy_90_AbandonReleaseRequestIn",
        "AbandonReleaseRequestOut": "_clouddeploy_91_AbandonReleaseRequestOut",
        "ListLocationsResponseIn": "_clouddeploy_92_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_clouddeploy_93_ListLocationsResponseOut",
        "ReleaseConditionIn": "_clouddeploy_94_ReleaseConditionIn",
        "ReleaseConditionOut": "_clouddeploy_95_ReleaseConditionOut",
        "ServiceNetworkingIn": "_clouddeploy_96_ServiceNetworkingIn",
        "ServiceNetworkingOut": "_clouddeploy_97_ServiceNetworkingOut",
        "CancelRolloutRequestIn": "_clouddeploy_98_CancelRolloutRequestIn",
        "CancelRolloutRequestOut": "_clouddeploy_99_CancelRolloutRequestOut",
        "ListReleasesResponseIn": "_clouddeploy_100_ListReleasesResponseIn",
        "ListReleasesResponseOut": "_clouddeploy_101_ListReleasesResponseOut",
        "StageIn": "_clouddeploy_102_StageIn",
        "StageOut": "_clouddeploy_103_StageOut",
        "LocationIn": "_clouddeploy_104_LocationIn",
        "LocationOut": "_clouddeploy_105_LocationOut",
        "DeployJobIn": "_clouddeploy_106_DeployJobIn",
        "DeployJobOut": "_clouddeploy_107_DeployJobOut",
        "ChildRolloutJobsIn": "_clouddeploy_108_ChildRolloutJobsIn",
        "ChildRolloutJobsOut": "_clouddeploy_109_ChildRolloutJobsOut",
        "IgnoreJobResponseIn": "_clouddeploy_110_IgnoreJobResponseIn",
        "IgnoreJobResponseOut": "_clouddeploy_111_IgnoreJobResponseOut",
        "SetIamPolicyRequestIn": "_clouddeploy_112_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_clouddeploy_113_SetIamPolicyRequestOut",
        "PhaseConfigIn": "_clouddeploy_114_PhaseConfigIn",
        "PhaseConfigOut": "_clouddeploy_115_PhaseConfigOut",
        "SkaffoldVersionIn": "_clouddeploy_116_SkaffoldVersionIn",
        "SkaffoldVersionOut": "_clouddeploy_117_SkaffoldVersionOut",
        "ExprIn": "_clouddeploy_118_ExprIn",
        "ExprOut": "_clouddeploy_119_ExprOut",
        "RolloutNotificationEventIn": "_clouddeploy_120_RolloutNotificationEventIn",
        "RolloutNotificationEventOut": "_clouddeploy_121_RolloutNotificationEventOut",
        "AnthosClusterIn": "_clouddeploy_122_AnthosClusterIn",
        "AnthosClusterOut": "_clouddeploy_123_AnthosClusterOut",
        "CloudRunMetadataIn": "_clouddeploy_124_CloudRunMetadataIn",
        "CloudRunMetadataOut": "_clouddeploy_125_CloudRunMetadataOut",
        "PolicyIn": "_clouddeploy_126_PolicyIn",
        "PolicyOut": "_clouddeploy_127_PolicyOut",
        "StatusIn": "_clouddeploy_128_StatusIn",
        "StatusOut": "_clouddeploy_129_StatusOut",
        "TargetArtifactIn": "_clouddeploy_130_TargetArtifactIn",
        "TargetArtifactOut": "_clouddeploy_131_TargetArtifactOut",
        "CloudRunRenderMetadataIn": "_clouddeploy_132_CloudRunRenderMetadataIn",
        "CloudRunRenderMetadataOut": "_clouddeploy_133_CloudRunRenderMetadataOut",
        "DeployParametersIn": "_clouddeploy_134_DeployParametersIn",
        "DeployParametersOut": "_clouddeploy_135_DeployParametersOut",
        "CancelRolloutResponseIn": "_clouddeploy_136_CancelRolloutResponseIn",
        "CancelRolloutResponseOut": "_clouddeploy_137_CancelRolloutResponseOut",
        "CreateChildRolloutJobRunIn": "_clouddeploy_138_CreateChildRolloutJobRunIn",
        "CreateChildRolloutJobRunOut": "_clouddeploy_139_CreateChildRolloutJobRunOut",
        "ApproveRolloutResponseIn": "_clouddeploy_140_ApproveRolloutResponseIn",
        "ApproveRolloutResponseOut": "_clouddeploy_141_ApproveRolloutResponseOut",
        "VerifyJobIn": "_clouddeploy_142_VerifyJobIn",
        "VerifyJobOut": "_clouddeploy_143_VerifyJobOut",
        "StandardIn": "_clouddeploy_144_StandardIn",
        "StandardOut": "_clouddeploy_145_StandardOut",
        "ApproveRolloutRequestIn": "_clouddeploy_146_ApproveRolloutRequestIn",
        "ApproveRolloutRequestOut": "_clouddeploy_147_ApproveRolloutRequestOut",
        "ConfigIn": "_clouddeploy_148_ConfigIn",
        "ConfigOut": "_clouddeploy_149_ConfigOut",
        "TargetsPresentConditionIn": "_clouddeploy_150_TargetsPresentConditionIn",
        "TargetsPresentConditionOut": "_clouddeploy_151_TargetsPresentConditionOut",
        "TerminateJobRunResponseIn": "_clouddeploy_152_TerminateJobRunResponseIn",
        "TerminateJobRunResponseOut": "_clouddeploy_153_TerminateJobRunResponseOut",
        "MetadataIn": "_clouddeploy_154_MetadataIn",
        "MetadataOut": "_clouddeploy_155_MetadataOut",
        "DateIn": "_clouddeploy_156_DateIn",
        "DateOut": "_clouddeploy_157_DateOut",
        "JobIn": "_clouddeploy_158_JobIn",
        "JobOut": "_clouddeploy_159_JobOut",
        "TerminateJobRunRequestIn": "_clouddeploy_160_TerminateJobRunRequestIn",
        "TerminateJobRunRequestOut": "_clouddeploy_161_TerminateJobRunRequestOut",
        "KubernetesConfigIn": "_clouddeploy_162_KubernetesConfigIn",
        "KubernetesConfigOut": "_clouddeploy_163_KubernetesConfigOut",
        "AuditConfigIn": "_clouddeploy_164_AuditConfigIn",
        "AuditConfigOut": "_clouddeploy_165_AuditConfigOut",
        "CanaryDeploymentIn": "_clouddeploy_166_CanaryDeploymentIn",
        "CanaryDeploymentOut": "_clouddeploy_167_CanaryDeploymentOut",
        "PhaseArtifactIn": "_clouddeploy_168_PhaseArtifactIn",
        "PhaseArtifactOut": "_clouddeploy_169_PhaseArtifactOut",
        "AdvanceRolloutResponseIn": "_clouddeploy_170_AdvanceRolloutResponseIn",
        "AdvanceRolloutResponseOut": "_clouddeploy_171_AdvanceRolloutResponseOut",
        "TargetsTypeConditionIn": "_clouddeploy_172_TargetsTypeConditionIn",
        "TargetsTypeConditionOut": "_clouddeploy_173_TargetsTypeConditionOut",
        "ReleaseReadyConditionIn": "_clouddeploy_174_ReleaseReadyConditionIn",
        "ReleaseReadyConditionOut": "_clouddeploy_175_ReleaseReadyConditionOut",
        "PrivatePoolIn": "_clouddeploy_176_PrivatePoolIn",
        "PrivatePoolOut": "_clouddeploy_177_PrivatePoolOut",
        "JobRunIn": "_clouddeploy_178_JobRunIn",
        "JobRunOut": "_clouddeploy_179_JobRunOut",
        "SkaffoldSupportedConditionIn": "_clouddeploy_180_SkaffoldSupportedConditionIn",
        "SkaffoldSupportedConditionOut": "_clouddeploy_181_SkaffoldSupportedConditionOut",
        "AdvanceRolloutRequestIn": "_clouddeploy_182_AdvanceRolloutRequestIn",
        "AdvanceRolloutRequestOut": "_clouddeploy_183_AdvanceRolloutRequestOut",
        "DeliveryPipelineNotificationEventIn": "_clouddeploy_184_DeliveryPipelineNotificationEventIn",
        "DeliveryPipelineNotificationEventOut": "_clouddeploy_185_DeliveryPipelineNotificationEventOut",
        "ReleaseNotificationEventIn": "_clouddeploy_186_ReleaseNotificationEventIn",
        "ReleaseNotificationEventOut": "_clouddeploy_187_ReleaseNotificationEventOut",
        "CanaryIn": "_clouddeploy_188_CanaryIn",
        "CanaryOut": "_clouddeploy_189_CanaryOut",
        "EmptyIn": "_clouddeploy_190_EmptyIn",
        "EmptyOut": "_clouddeploy_191_EmptyOut",
        "DefaultPoolIn": "_clouddeploy_192_DefaultPoolIn",
        "DefaultPoolOut": "_clouddeploy_193_DefaultPoolOut",
        "RolloutIn": "_clouddeploy_194_RolloutIn",
        "RolloutOut": "_clouddeploy_195_RolloutOut",
        "OperationMetadataIn": "_clouddeploy_196_OperationMetadataIn",
        "OperationMetadataOut": "_clouddeploy_197_OperationMetadataOut",
        "IgnoreJobRequestIn": "_clouddeploy_198_IgnoreJobRequestIn",
        "IgnoreJobRequestOut": "_clouddeploy_199_IgnoreJobRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GkeClusterIn"] = t.struct(
        {"cluster": t.string().optional(), "internalIp": t.boolean().optional()}
    ).named(renames["GkeClusterIn"])
    types["GkeClusterOut"] = t.struct(
        {
            "cluster": t.string().optional(),
            "internalIp": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GkeClusterOut"])
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
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
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
    types["TargetRenderIn"] = t.struct({"_": t.string().optional()}).named(
        renames["TargetRenderIn"]
    )
    types["TargetRenderOut"] = t.struct(
        {
            "metadata": t.proxy(renames["RenderMetadataOut"]).optional(),
            "failureCause": t.string().optional(),
            "renderingBuild": t.string().optional(),
            "failureMessage": t.string().optional(),
            "renderingState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetRenderOut"])
    types["VerifyJobRunIn"] = t.struct({"_": t.string().optional()}).named(
        renames["VerifyJobRunIn"]
    )
    types["VerifyJobRunOut"] = t.struct(
        {
            "build": t.string().optional(),
            "failureCause": t.string().optional(),
            "eventLogPath": t.string().optional(),
            "artifactUri": t.string().optional(),
            "failureMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VerifyJobRunOut"])
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
    types["StrategyIn"] = t.struct(
        {
            "standard": t.proxy(renames["StandardIn"]).optional(),
            "canary": t.proxy(renames["CanaryIn"]).optional(),
        }
    ).named(renames["StrategyIn"])
    types["StrategyOut"] = t.struct(
        {
            "standard": t.proxy(renames["StandardOut"]).optional(),
            "canary": t.proxy(renames["CanaryOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StrategyOut"])
    types["SerialPipelineIn"] = t.struct(
        {"stages": t.array(t.proxy(renames["StageIn"])).optional()}
    ).named(renames["SerialPipelineIn"])
    types["SerialPipelineOut"] = t.struct(
        {
            "stages": t.array(t.proxy(renames["StageOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SerialPipelineOut"])
    types["MultiTargetIn"] = t.struct({"targetIds": t.array(t.string())}).named(
        renames["MultiTargetIn"]
    )
    types["MultiTargetOut"] = t.struct(
        {
            "targetIds": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MultiTargetOut"])
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
    types["ExecutionConfigIn"] = t.struct(
        {
            "executionTimeout": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "defaultPool": t.proxy(renames["DefaultPoolIn"]).optional(),
            "artifactStorage": t.string().optional(),
            "workerPool": t.string().optional(),
            "usages": t.array(t.string()),
            "privatePool": t.proxy(renames["PrivatePoolIn"]).optional(),
        }
    ).named(renames["ExecutionConfigIn"])
    types["ExecutionConfigOut"] = t.struct(
        {
            "executionTimeout": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "defaultPool": t.proxy(renames["DefaultPoolOut"]).optional(),
            "artifactStorage": t.string().optional(),
            "workerPool": t.string().optional(),
            "usages": t.array(t.string()),
            "privatePool": t.proxy(renames["PrivatePoolOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecutionConfigOut"])
    types["CreateChildRolloutJobIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CreateChildRolloutJobIn"]
    )
    types["CreateChildRolloutJobOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CreateChildRolloutJobOut"])
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
    types["CustomCanaryDeploymentIn"] = t.struct(
        {"phaseConfigs": t.array(t.proxy(renames["PhaseConfigIn"]))}
    ).named(renames["CustomCanaryDeploymentIn"])
    types["CustomCanaryDeploymentOut"] = t.struct(
        {
            "phaseConfigs": t.array(t.proxy(renames["PhaseConfigOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomCanaryDeploymentOut"])
    types["RetryJobResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RetryJobResponseIn"]
    )
    types["RetryJobResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RetryJobResponseOut"])
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
    types["CloudRunLocationIn"] = t.struct({"location": t.string()}).named(
        renames["CloudRunLocationIn"]
    )
    types["CloudRunLocationOut"] = t.struct(
        {"location": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CloudRunLocationOut"])
    types["DeployJobRunMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeployJobRunMetadataIn"]
    )
    types["DeployJobRunMetadataOut"] = t.struct(
        {
            "cloudRun": t.proxy(renames["CloudRunMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeployJobRunMetadataOut"])
    types["RenderMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RenderMetadataIn"]
    )
    types["RenderMetadataOut"] = t.struct(
        {
            "cloudRun": t.proxy(renames["CloudRunRenderMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RenderMetadataOut"])
    types["ListJobRunsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "jobRuns": t.array(t.proxy(renames["JobRunIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListJobRunsResponseIn"])
    types["ListJobRunsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "jobRuns": t.array(t.proxy(renames["JobRunOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListJobRunsResponseOut"])
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
    types["AdvanceChildRolloutJobIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AdvanceChildRolloutJobIn"]
    )
    types["AdvanceChildRolloutJobOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AdvanceChildRolloutJobOut"])
    types["DeliveryPipelineIn"] = t.struct(
        {
            "suspended": t.boolean().optional(),
            "serialPipeline": t.proxy(renames["SerialPipelineIn"]).optional(),
            "etag": t.string().optional(),
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["DeliveryPipelineIn"])
    types["DeliveryPipelineOut"] = t.struct(
        {
            "uid": t.string().optional(),
            "condition": t.proxy(renames["PipelineConditionOut"]).optional(),
            "suspended": t.boolean().optional(),
            "serialPipeline": t.proxy(renames["SerialPipelineOut"]).optional(),
            "etag": t.string().optional(),
            "description": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeliveryPipelineOut"])
    types["ReleaseIn"] = t.struct(
        {
            "deployParameters": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "skaffoldVersion": t.string().optional(),
            "skaffoldConfigPath": t.string().optional(),
            "buildArtifacts": t.array(t.proxy(renames["BuildArtifactIn"])).optional(),
            "name": t.string().optional(),
            "etag": t.string().optional(),
            "skaffoldConfigUri": t.string().optional(),
        }
    ).named(renames["ReleaseIn"])
    types["ReleaseOut"] = t.struct(
        {
            "targetRenders": t.struct({"_": t.string().optional()}).optional(),
            "renderStartTime": t.string().optional(),
            "renderState": t.string().optional(),
            "targetSnapshots": t.array(t.proxy(renames["TargetOut"])).optional(),
            "deployParameters": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "abandoned": t.boolean().optional(),
            "condition": t.proxy(renames["ReleaseConditionOut"]).optional(),
            "skaffoldVersion": t.string().optional(),
            "skaffoldConfigPath": t.string().optional(),
            "deliveryPipelineSnapshot": t.proxy(
                renames["DeliveryPipelineOut"]
            ).optional(),
            "buildArtifacts": t.array(t.proxy(renames["BuildArtifactOut"])).optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "etag": t.string().optional(),
            "skaffoldConfigUri": t.string().optional(),
            "uid": t.string().optional(),
            "renderEndTime": t.string().optional(),
            "targetArtifacts": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReleaseOut"])
    types["PhaseIn"] = t.struct({"_": t.string().optional()}).named(renames["PhaseIn"])
    types["PhaseOut"] = t.struct(
        {
            "deploymentJobs": t.proxy(renames["DeploymentJobsOut"]).optional(),
            "childRolloutJobs": t.proxy(renames["ChildRolloutJobsOut"]).optional(),
            "id": t.string().optional(),
            "state": t.string().optional(),
            "skipMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhaseOut"])
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
    types["GatewayServiceMeshIn"] = t.struct(
        {"httpRoute": t.string(), "service": t.string(), "deployment": t.string()}
    ).named(renames["GatewayServiceMeshIn"])
    types["GatewayServiceMeshOut"] = t.struct(
        {
            "httpRoute": t.string(),
            "service": t.string(),
            "deployment": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GatewayServiceMeshOut"])
    types["AbandonReleaseResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AbandonReleaseResponseIn"]
    )
    types["AbandonReleaseResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AbandonReleaseResponseOut"])
    types["OperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationOut"])
    types["ListTargetsResponseIn"] = t.struct(
        {
            "targets": t.array(t.proxy(renames["TargetIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListTargetsResponseIn"])
    types["ListTargetsResponseOut"] = t.struct(
        {
            "targets": t.array(t.proxy(renames["TargetOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTargetsResponseOut"])
    types["PipelineConditionIn"] = t.struct(
        {
            "pipelineReadyCondition": t.proxy(
                renames["PipelineReadyConditionIn"]
            ).optional(),
            "targetsTypeCondition": t.proxy(
                renames["TargetsTypeConditionIn"]
            ).optional(),
            "targetsPresentCondition": t.proxy(
                renames["TargetsPresentConditionIn"]
            ).optional(),
        }
    ).named(renames["PipelineConditionIn"])
    types["PipelineConditionOut"] = t.struct(
        {
            "pipelineReadyCondition": t.proxy(
                renames["PipelineReadyConditionOut"]
            ).optional(),
            "targetsTypeCondition": t.proxy(
                renames["TargetsTypeConditionOut"]
            ).optional(),
            "targetsPresentCondition": t.proxy(
                renames["TargetsPresentConditionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PipelineConditionOut"])
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
    types["JobRunNotificationEventIn"] = t.struct(
        {
            "type": t.string().optional(),
            "rolloutUid": t.string().optional(),
            "releaseUid": t.string().optional(),
            "targetId": t.string().optional(),
            "jobRun": t.string().optional(),
            "message": t.string().optional(),
            "pipelineUid": t.string().optional(),
        }
    ).named(renames["JobRunNotificationEventIn"])
    types["JobRunNotificationEventOut"] = t.struct(
        {
            "type": t.string().optional(),
            "rolloutUid": t.string().optional(),
            "releaseUid": t.string().optional(),
            "targetId": t.string().optional(),
            "jobRun": t.string().optional(),
            "message": t.string().optional(),
            "pipelineUid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobRunNotificationEventOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["TargetIn"] = t.struct(
        {
            "requireApproval": t.boolean().optional(),
            "multiTarget": t.proxy(renames["MultiTargetIn"]).optional(),
            "gke": t.proxy(renames["GkeClusterIn"]).optional(),
            "executionConfigs": t.array(
                t.proxy(renames["ExecutionConfigIn"])
            ).optional(),
            "name": t.string().optional(),
            "etag": t.string().optional(),
            "deployParameters": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "anthosCluster": t.proxy(renames["AnthosClusterIn"]).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "run": t.proxy(renames["CloudRunLocationIn"]).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["TargetIn"])
    types["TargetOut"] = t.struct(
        {
            "requireApproval": t.boolean().optional(),
            "multiTarget": t.proxy(renames["MultiTargetOut"]).optional(),
            "gke": t.proxy(renames["GkeClusterOut"]).optional(),
            "executionConfigs": t.array(
                t.proxy(renames["ExecutionConfigOut"])
            ).optional(),
            "name": t.string().optional(),
            "etag": t.string().optional(),
            "deployParameters": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "uid": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "anthosCluster": t.proxy(renames["AnthosClusterOut"]).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "run": t.proxy(renames["CloudRunLocationOut"]).optional(),
            "description": t.string().optional(),
            "targetId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetOut"])
    types["CloudRunConfigIn"] = t.struct(
        {"automaticTrafficControl": t.boolean().optional()}
    ).named(renames["CloudRunConfigIn"])
    types["CloudRunConfigOut"] = t.struct(
        {
            "automaticTrafficControl": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudRunConfigOut"])
    types["DeployJobRunIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeployJobRunIn"]
    )
    types["DeployJobRunOut"] = t.struct(
        {
            "failureCause": t.string().optional(),
            "metadata": t.proxy(renames["DeployJobRunMetadataOut"]).optional(),
            "failureMessage": t.string().optional(),
            "build": t.string().optional(),
            "artifact": t.proxy(renames["DeployArtifactOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeployJobRunOut"])
    types["AbandonReleaseRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AbandonReleaseRequestIn"]
    )
    types["AbandonReleaseRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AbandonReleaseRequestOut"])
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
    types["ServiceNetworkingIn"] = t.struct(
        {
            "service": t.string(),
            "disablePodOverprovisioning": t.boolean().optional(),
            "deployment": t.string(),
        }
    ).named(renames["ServiceNetworkingIn"])
    types["ServiceNetworkingOut"] = t.struct(
        {
            "service": t.string(),
            "disablePodOverprovisioning": t.boolean().optional(),
            "deployment": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceNetworkingOut"])
    types["CancelRolloutRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelRolloutRequestIn"]
    )
    types["CancelRolloutRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelRolloutRequestOut"])
    types["ListReleasesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "releases": t.array(t.proxy(renames["ReleaseIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListReleasesResponseIn"])
    types["ListReleasesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "releases": t.array(t.proxy(renames["ReleaseOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListReleasesResponseOut"])
    types["StageIn"] = t.struct(
        {
            "strategy": t.proxy(renames["StrategyIn"]).optional(),
            "deployParameters": t.array(
                t.proxy(renames["DeployParametersIn"])
            ).optional(),
            "profiles": t.array(t.string()).optional(),
            "targetId": t.string().optional(),
        }
    ).named(renames["StageIn"])
    types["StageOut"] = t.struct(
        {
            "strategy": t.proxy(renames["StrategyOut"]).optional(),
            "deployParameters": t.array(
                t.proxy(renames["DeployParametersOut"])
            ).optional(),
            "profiles": t.array(t.string()).optional(),
            "targetId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StageOut"])
    types["LocationIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["DeployJobIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeployJobIn"]
    )
    types["DeployJobOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeployJobOut"])
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
    types["IgnoreJobResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["IgnoreJobResponseIn"]
    )
    types["IgnoreJobResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["IgnoreJobResponseOut"])
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
    types["PhaseConfigIn"] = t.struct(
        {
            "phaseId": t.string(),
            "verify": t.boolean().optional(),
            "percentage": t.integer(),
            "profiles": t.array(t.string()).optional(),
        }
    ).named(renames["PhaseConfigIn"])
    types["PhaseConfigOut"] = t.struct(
        {
            "phaseId": t.string(),
            "verify": t.boolean().optional(),
            "percentage": t.integer(),
            "profiles": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhaseConfigOut"])
    types["SkaffoldVersionIn"] = t.struct(
        {
            "supportEndDate": t.proxy(renames["DateIn"]).optional(),
            "supportExpirationTime": t.string().optional(),
            "version": t.string().optional(),
            "maintenanceModeTime": t.string().optional(),
        }
    ).named(renames["SkaffoldVersionIn"])
    types["SkaffoldVersionOut"] = t.struct(
        {
            "supportEndDate": t.proxy(renames["DateOut"]).optional(),
            "supportExpirationTime": t.string().optional(),
            "version": t.string().optional(),
            "maintenanceModeTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SkaffoldVersionOut"])
    types["ExprIn"] = t.struct(
        {
            "description": t.string().optional(),
            "title": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "description": t.string().optional(),
            "title": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["RolloutNotificationEventIn"] = t.struct(
        {
            "message": t.string().optional(),
            "pipelineUid": t.string().optional(),
            "rollout": t.string().optional(),
            "releaseUid": t.string().optional(),
            "targetId": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["RolloutNotificationEventIn"])
    types["RolloutNotificationEventOut"] = t.struct(
        {
            "message": t.string().optional(),
            "pipelineUid": t.string().optional(),
            "rollout": t.string().optional(),
            "releaseUid": t.string().optional(),
            "targetId": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RolloutNotificationEventOut"])
    types["AnthosClusterIn"] = t.struct({"membership": t.string().optional()}).named(
        renames["AnthosClusterIn"]
    )
    types["AnthosClusterOut"] = t.struct(
        {
            "membership": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnthosClusterOut"])
    types["CloudRunMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CloudRunMetadataIn"]
    )
    types["CloudRunMetadataOut"] = t.struct(
        {
            "serviceUrls": t.array(t.string()).optional(),
            "service": t.string().optional(),
            "revision": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudRunMetadataOut"])
    types["PolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["StatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["TargetArtifactIn"] = t.struct({"_": t.string().optional()}).named(
        renames["TargetArtifactIn"]
    )
    types["TargetArtifactOut"] = t.struct(
        {
            "manifestPath": t.string().optional(),
            "skaffoldConfigPath": t.string().optional(),
            "artifactUri": t.string().optional(),
            "phaseArtifacts": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetArtifactOut"])
    types["CloudRunRenderMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CloudRunRenderMetadataIn"]
    )
    types["CloudRunRenderMetadataOut"] = t.struct(
        {
            "service": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudRunRenderMetadataOut"])
    types["DeployParametersIn"] = t.struct(
        {
            "values": t.struct({"_": t.string().optional()}),
            "matchTargetLabels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["DeployParametersIn"])
    types["DeployParametersOut"] = t.struct(
        {
            "values": t.struct({"_": t.string().optional()}),
            "matchTargetLabels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeployParametersOut"])
    types["CancelRolloutResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelRolloutResponseIn"]
    )
    types["CancelRolloutResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelRolloutResponseOut"])
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
    types["ApproveRolloutResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ApproveRolloutResponseIn"]
    )
    types["ApproveRolloutResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ApproveRolloutResponseOut"])
    types["VerifyJobIn"] = t.struct({"_": t.string().optional()}).named(
        renames["VerifyJobIn"]
    )
    types["VerifyJobOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["VerifyJobOut"])
    types["StandardIn"] = t.struct({"verify": t.boolean().optional()}).named(
        renames["StandardIn"]
    )
    types["StandardOut"] = t.struct(
        {
            "verify": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StandardOut"])
    types["ApproveRolloutRequestIn"] = t.struct({"approved": t.boolean()}).named(
        renames["ApproveRolloutRequestIn"]
    )
    types["ApproveRolloutRequestOut"] = t.struct(
        {"approved": t.boolean(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ApproveRolloutRequestOut"])
    types["ConfigIn"] = t.struct(
        {
            "name": t.string().optional(),
            "defaultSkaffoldVersion": t.string().optional(),
            "supportedVersions": t.array(
                t.proxy(renames["SkaffoldVersionIn"])
            ).optional(),
        }
    ).named(renames["ConfigIn"])
    types["ConfigOut"] = t.struct(
        {
            "name": t.string().optional(),
            "defaultSkaffoldVersion": t.string().optional(),
            "supportedVersions": t.array(
                t.proxy(renames["SkaffoldVersionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigOut"])
    types["TargetsPresentConditionIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "status": t.boolean().optional(),
            "missingTargets": t.array(t.string()).optional(),
        }
    ).named(renames["TargetsPresentConditionIn"])
    types["TargetsPresentConditionOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "status": t.boolean().optional(),
            "missingTargets": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetsPresentConditionOut"])
    types["TerminateJobRunResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["TerminateJobRunResponseIn"]
    )
    types["TerminateJobRunResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["TerminateJobRunResponseOut"])
    types["MetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MetadataIn"]
    )
    types["MetadataOut"] = t.struct(
        {
            "cloudRun": t.proxy(renames["CloudRunMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetadataOut"])
    types["DateIn"] = t.struct(
        {
            "year": t.integer().optional(),
            "day": t.integer().optional(),
            "month": t.integer().optional(),
        }
    ).named(renames["DateIn"])
    types["DateOut"] = t.struct(
        {
            "year": t.integer().optional(),
            "day": t.integer().optional(),
            "month": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
    types["JobIn"] = t.struct({"_": t.string().optional()}).named(renames["JobIn"])
    types["JobOut"] = t.struct(
        {
            "advanceChildRolloutJob": t.proxy(
                renames["AdvanceChildRolloutJobOut"]
            ).optional(),
            "createChildRolloutJob": t.proxy(
                renames["CreateChildRolloutJobOut"]
            ).optional(),
            "id": t.string().optional(),
            "skipMessage": t.string().optional(),
            "deployJob": t.proxy(renames["DeployJobOut"]).optional(),
            "jobRun": t.string().optional(),
            "state": t.string().optional(),
            "verifyJob": t.proxy(renames["VerifyJobOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobOut"])
    types["TerminateJobRunRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["TerminateJobRunRequestIn"]
    )
    types["TerminateJobRunRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["TerminateJobRunRequestOut"])
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
    types["PhaseArtifactIn"] = t.struct({"_": t.string().optional()}).named(
        renames["PhaseArtifactIn"]
    )
    types["PhaseArtifactOut"] = t.struct(
        {
            "jobManifestsPath": t.string().optional(),
            "manifestPath": t.string().optional(),
            "skaffoldConfigPath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhaseArtifactOut"])
    types["AdvanceRolloutResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AdvanceRolloutResponseIn"]
    )
    types["AdvanceRolloutResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AdvanceRolloutResponseOut"])
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
    types["ReleaseReadyConditionIn"] = t.struct(
        {"status": t.boolean().optional()}
    ).named(renames["ReleaseReadyConditionIn"])
    types["ReleaseReadyConditionOut"] = t.struct(
        {
            "status": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReleaseReadyConditionOut"])
    types["PrivatePoolIn"] = t.struct(
        {
            "artifactStorage": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "workerPool": t.string(),
        }
    ).named(renames["PrivatePoolIn"])
    types["PrivatePoolOut"] = t.struct(
        {
            "artifactStorage": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "workerPool": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrivatePoolOut"])
    types["JobRunIn"] = t.struct({"name": t.string().optional()}).named(
        renames["JobRunIn"]
    )
    types["JobRunOut"] = t.struct(
        {
            "verifyJobRun": t.proxy(renames["VerifyJobRunOut"]).optional(),
            "phaseId": t.string().optional(),
            "etag": t.string().optional(),
            "name": t.string().optional(),
            "jobId": t.string().optional(),
            "endTime": t.string().optional(),
            "uid": t.string().optional(),
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "startTime": t.string().optional(),
            "deployJobRun": t.proxy(renames["DeployJobRunOut"]).optional(),
            "advanceChildRolloutJobRun": t.proxy(
                renames["AdvanceChildRolloutJobRunOut"]
            ).optional(),
            "createChildRolloutJobRun": t.proxy(
                renames["CreateChildRolloutJobRunOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobRunOut"])
    types["SkaffoldSupportedConditionIn"] = t.struct(
        {
            "supportExpirationTime": t.string().optional(),
            "maintenanceModeTime": t.string().optional(),
            "skaffoldSupportState": t.string().optional(),
            "status": t.boolean().optional(),
        }
    ).named(renames["SkaffoldSupportedConditionIn"])
    types["SkaffoldSupportedConditionOut"] = t.struct(
        {
            "supportExpirationTime": t.string().optional(),
            "maintenanceModeTime": t.string().optional(),
            "skaffoldSupportState": t.string().optional(),
            "status": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SkaffoldSupportedConditionOut"])
    types["AdvanceRolloutRequestIn"] = t.struct({"phaseId": t.string()}).named(
        renames["AdvanceRolloutRequestIn"]
    )
    types["AdvanceRolloutRequestOut"] = t.struct(
        {"phaseId": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AdvanceRolloutRequestOut"])
    types["DeliveryPipelineNotificationEventIn"] = t.struct(
        {
            "message": t.string().optional(),
            "deliveryPipeline": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["DeliveryPipelineNotificationEventIn"])
    types["DeliveryPipelineNotificationEventOut"] = t.struct(
        {
            "message": t.string().optional(),
            "deliveryPipeline": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeliveryPipelineNotificationEventOut"])
    types["ReleaseNotificationEventIn"] = t.struct(
        {
            "message": t.string().optional(),
            "release": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["ReleaseNotificationEventIn"])
    types["ReleaseNotificationEventOut"] = t.struct(
        {
            "message": t.string().optional(),
            "release": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReleaseNotificationEventOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["RolloutIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "etag": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "targetId": t.string(),
        }
    ).named(renames["RolloutIn"])
    types["RolloutOut"] = t.struct(
        {
            "controllerRollout": t.string().optional(),
            "createTime": t.string().optional(),
            "deployEndTime": t.string().optional(),
            "metadata": t.proxy(renames["MetadataOut"]).optional(),
            "deployingBuild": t.string().optional(),
            "approvalState": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "phases": t.array(t.proxy(renames["PhaseOut"])).optional(),
            "etag": t.string().optional(),
            "approveTime": t.string().optional(),
            "deployFailureCause": t.string().optional(),
            "name": t.string().optional(),
            "deployStartTime": t.string().optional(),
            "failureReason": t.string().optional(),
            "description": t.string().optional(),
            "state": t.string().optional(),
            "targetId": t.string(),
            "enqueueTime": t.string().optional(),
            "uid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RolloutOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "target": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "verb": t.string().optional(),
            "endTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "createTime": t.string().optional(),
            "statusMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["IgnoreJobRequestIn"] = t.struct(
        {"phaseId": t.string(), "jobId": t.string()}
    ).named(renames["IgnoreJobRequestIn"])
    types["IgnoreJobRequestOut"] = t.struct(
        {
            "phaseId": t.string(),
            "jobId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IgnoreJobRequestOut"])

    functions = {}
    functions["projectsLocationsGetConfig"] = clouddeploy.get(
        "v1/{name}/locations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = clouddeploy.get(
        "v1/{name}/locations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTargetsList"] = clouddeploy.patch(
        "v1/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "updateMask": t.string(),
                "allowMissing": t.boolean().optional(),
                "requireApproval": t.boolean().optional(),
                "multiTarget": t.proxy(renames["MultiTargetIn"]).optional(),
                "gke": t.proxy(renames["GkeClusterIn"]).optional(),
                "executionConfigs": t.array(
                    t.proxy(renames["ExecutionConfigIn"])
                ).optional(),
                "etag": t.string().optional(),
                "deployParameters": t.struct({"_": t.string().optional()}).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "anthosCluster": t.proxy(renames["AnthosClusterIn"]).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "run": t.proxy(renames["CloudRunLocationIn"]).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTargetsSetIamPolicy"] = clouddeploy.patch(
        "v1/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "updateMask": t.string(),
                "allowMissing": t.boolean().optional(),
                "requireApproval": t.boolean().optional(),
                "multiTarget": t.proxy(renames["MultiTargetIn"]).optional(),
                "gke": t.proxy(renames["GkeClusterIn"]).optional(),
                "executionConfigs": t.array(
                    t.proxy(renames["ExecutionConfigIn"])
                ).optional(),
                "etag": t.string().optional(),
                "deployParameters": t.struct({"_": t.string().optional()}).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "anthosCluster": t.proxy(renames["AnthosClusterIn"]).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "run": t.proxy(renames["CloudRunLocationIn"]).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTargetsTestIamPermissions"] = clouddeploy.patch(
        "v1/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "updateMask": t.string(),
                "allowMissing": t.boolean().optional(),
                "requireApproval": t.boolean().optional(),
                "multiTarget": t.proxy(renames["MultiTargetIn"]).optional(),
                "gke": t.proxy(renames["GkeClusterIn"]).optional(),
                "executionConfigs": t.array(
                    t.proxy(renames["ExecutionConfigIn"])
                ).optional(),
                "etag": t.string().optional(),
                "deployParameters": t.struct({"_": t.string().optional()}).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "anthosCluster": t.proxy(renames["AnthosClusterIn"]).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "run": t.proxy(renames["CloudRunLocationIn"]).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTargetsDelete"] = clouddeploy.patch(
        "v1/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "updateMask": t.string(),
                "allowMissing": t.boolean().optional(),
                "requireApproval": t.boolean().optional(),
                "multiTarget": t.proxy(renames["MultiTargetIn"]).optional(),
                "gke": t.proxy(renames["GkeClusterIn"]).optional(),
                "executionConfigs": t.array(
                    t.proxy(renames["ExecutionConfigIn"])
                ).optional(),
                "etag": t.string().optional(),
                "deployParameters": t.struct({"_": t.string().optional()}).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "anthosCluster": t.proxy(renames["AnthosClusterIn"]).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "run": t.proxy(renames["CloudRunLocationIn"]).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTargetsCreate"] = clouddeploy.patch(
        "v1/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "updateMask": t.string(),
                "allowMissing": t.boolean().optional(),
                "requireApproval": t.boolean().optional(),
                "multiTarget": t.proxy(renames["MultiTargetIn"]).optional(),
                "gke": t.proxy(renames["GkeClusterIn"]).optional(),
                "executionConfigs": t.array(
                    t.proxy(renames["ExecutionConfigIn"])
                ).optional(),
                "etag": t.string().optional(),
                "deployParameters": t.struct({"_": t.string().optional()}).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "anthosCluster": t.proxy(renames["AnthosClusterIn"]).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "run": t.proxy(renames["CloudRunLocationIn"]).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTargetsGetIamPolicy"] = clouddeploy.patch(
        "v1/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "updateMask": t.string(),
                "allowMissing": t.boolean().optional(),
                "requireApproval": t.boolean().optional(),
                "multiTarget": t.proxy(renames["MultiTargetIn"]).optional(),
                "gke": t.proxy(renames["GkeClusterIn"]).optional(),
                "executionConfigs": t.array(
                    t.proxy(renames["ExecutionConfigIn"])
                ).optional(),
                "etag": t.string().optional(),
                "deployParameters": t.struct({"_": t.string().optional()}).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "anthosCluster": t.proxy(renames["AnthosClusterIn"]).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "run": t.proxy(renames["CloudRunLocationIn"]).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTargetsGet"] = clouddeploy.patch(
        "v1/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "updateMask": t.string(),
                "allowMissing": t.boolean().optional(),
                "requireApproval": t.boolean().optional(),
                "multiTarget": t.proxy(renames["MultiTargetIn"]).optional(),
                "gke": t.proxy(renames["GkeClusterIn"]).optional(),
                "executionConfigs": t.array(
                    t.proxy(renames["ExecutionConfigIn"])
                ).optional(),
                "etag": t.string().optional(),
                "deployParameters": t.struct({"_": t.string().optional()}).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "anthosCluster": t.proxy(renames["AnthosClusterIn"]).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "run": t.proxy(renames["CloudRunLocationIn"]).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTargetsPatch"] = clouddeploy.patch(
        "v1/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "updateMask": t.string(),
                "allowMissing": t.boolean().optional(),
                "requireApproval": t.boolean().optional(),
                "multiTarget": t.proxy(renames["MultiTargetIn"]).optional(),
                "gke": t.proxy(renames["GkeClusterIn"]).optional(),
                "executionConfigs": t.array(
                    t.proxy(renames["ExecutionConfigIn"])
                ).optional(),
                "etag": t.string().optional(),
                "deployParameters": t.struct({"_": t.string().optional()}).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "anthosCluster": t.proxy(renames["AnthosClusterIn"]).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "run": t.proxy(renames["CloudRunLocationIn"]).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = clouddeploy.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = clouddeploy.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = clouddeploy.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = clouddeploy.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDeliveryPipelinesPatch"] = clouddeploy.post(
        "v1/{parent}/deliveryPipelines",
        t.struct(
            {
                "requestId": t.string().optional(),
                "deliveryPipelineId": t.string(),
                "parent": t.string(),
                "validateOnly": t.boolean().optional(),
                "suspended": t.boolean().optional(),
                "serialPipeline": t.proxy(renames["SerialPipelineIn"]).optional(),
                "etag": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDeliveryPipelinesSetIamPolicy"] = clouddeploy.post(
        "v1/{parent}/deliveryPipelines",
        t.struct(
            {
                "requestId": t.string().optional(),
                "deliveryPipelineId": t.string(),
                "parent": t.string(),
                "validateOnly": t.boolean().optional(),
                "suspended": t.boolean().optional(),
                "serialPipeline": t.proxy(renames["SerialPipelineIn"]).optional(),
                "etag": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDeliveryPipelinesList"] = clouddeploy.post(
        "v1/{parent}/deliveryPipelines",
        t.struct(
            {
                "requestId": t.string().optional(),
                "deliveryPipelineId": t.string(),
                "parent": t.string(),
                "validateOnly": t.boolean().optional(),
                "suspended": t.boolean().optional(),
                "serialPipeline": t.proxy(renames["SerialPipelineIn"]).optional(),
                "etag": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDeliveryPipelinesTestIamPermissions"
    ] = clouddeploy.post(
        "v1/{parent}/deliveryPipelines",
        t.struct(
            {
                "requestId": t.string().optional(),
                "deliveryPipelineId": t.string(),
                "parent": t.string(),
                "validateOnly": t.boolean().optional(),
                "suspended": t.boolean().optional(),
                "serialPipeline": t.proxy(renames["SerialPipelineIn"]).optional(),
                "etag": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDeliveryPipelinesDelete"] = clouddeploy.post(
        "v1/{parent}/deliveryPipelines",
        t.struct(
            {
                "requestId": t.string().optional(),
                "deliveryPipelineId": t.string(),
                "parent": t.string(),
                "validateOnly": t.boolean().optional(),
                "suspended": t.boolean().optional(),
                "serialPipeline": t.proxy(renames["SerialPipelineIn"]).optional(),
                "etag": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDeliveryPipelinesGet"] = clouddeploy.post(
        "v1/{parent}/deliveryPipelines",
        t.struct(
            {
                "requestId": t.string().optional(),
                "deliveryPipelineId": t.string(),
                "parent": t.string(),
                "validateOnly": t.boolean().optional(),
                "suspended": t.boolean().optional(),
                "serialPipeline": t.proxy(renames["SerialPipelineIn"]).optional(),
                "etag": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDeliveryPipelinesGetIamPolicy"] = clouddeploy.post(
        "v1/{parent}/deliveryPipelines",
        t.struct(
            {
                "requestId": t.string().optional(),
                "deliveryPipelineId": t.string(),
                "parent": t.string(),
                "validateOnly": t.boolean().optional(),
                "suspended": t.boolean().optional(),
                "serialPipeline": t.proxy(renames["SerialPipelineIn"]).optional(),
                "etag": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDeliveryPipelinesCreate"] = clouddeploy.post(
        "v1/{parent}/deliveryPipelines",
        t.struct(
            {
                "requestId": t.string().optional(),
                "deliveryPipelineId": t.string(),
                "parent": t.string(),
                "validateOnly": t.boolean().optional(),
                "suspended": t.boolean().optional(),
                "serialPipeline": t.proxy(renames["SerialPipelineIn"]).optional(),
                "etag": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDeliveryPipelinesReleasesAbandon"] = clouddeploy.post(
        "v1/{parent}/releases",
        t.struct(
            {
                "parent": t.string(),
                "validateOnly": t.boolean().optional(),
                "requestId": t.string().optional(),
                "releaseId": t.string(),
                "deployParameters": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "skaffoldVersion": t.string().optional(),
                "skaffoldConfigPath": t.string().optional(),
                "buildArtifacts": t.array(
                    t.proxy(renames["BuildArtifactIn"])
                ).optional(),
                "name": t.string().optional(),
                "etag": t.string().optional(),
                "skaffoldConfigUri": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDeliveryPipelinesReleasesGet"] = clouddeploy.post(
        "v1/{parent}/releases",
        t.struct(
            {
                "parent": t.string(),
                "validateOnly": t.boolean().optional(),
                "requestId": t.string().optional(),
                "releaseId": t.string(),
                "deployParameters": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "skaffoldVersion": t.string().optional(),
                "skaffoldConfigPath": t.string().optional(),
                "buildArtifacts": t.array(
                    t.proxy(renames["BuildArtifactIn"])
                ).optional(),
                "name": t.string().optional(),
                "etag": t.string().optional(),
                "skaffoldConfigUri": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDeliveryPipelinesReleasesList"] = clouddeploy.post(
        "v1/{parent}/releases",
        t.struct(
            {
                "parent": t.string(),
                "validateOnly": t.boolean().optional(),
                "requestId": t.string().optional(),
                "releaseId": t.string(),
                "deployParameters": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "skaffoldVersion": t.string().optional(),
                "skaffoldConfigPath": t.string().optional(),
                "buildArtifacts": t.array(
                    t.proxy(renames["BuildArtifactIn"])
                ).optional(),
                "name": t.string().optional(),
                "etag": t.string().optional(),
                "skaffoldConfigUri": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDeliveryPipelinesReleasesCreate"] = clouddeploy.post(
        "v1/{parent}/releases",
        t.struct(
            {
                "parent": t.string(),
                "validateOnly": t.boolean().optional(),
                "requestId": t.string().optional(),
                "releaseId": t.string(),
                "deployParameters": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "skaffoldVersion": t.string().optional(),
                "skaffoldConfigPath": t.string().optional(),
                "buildArtifacts": t.array(
                    t.proxy(renames["BuildArtifactIn"])
                ).optional(),
                "name": t.string().optional(),
                "etag": t.string().optional(),
                "skaffoldConfigUri": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDeliveryPipelinesReleasesRolloutsRetryJob"
    ] = clouddeploy.get(
        "v1/{parent}/rollouts",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListRolloutsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDeliveryPipelinesReleasesRolloutsApprove"
    ] = clouddeploy.get(
        "v1/{parent}/rollouts",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListRolloutsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDeliveryPipelinesReleasesRolloutsAdvance"
    ] = clouddeploy.get(
        "v1/{parent}/rollouts",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListRolloutsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDeliveryPipelinesReleasesRolloutsCreate"
    ] = clouddeploy.get(
        "v1/{parent}/rollouts",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListRolloutsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDeliveryPipelinesReleasesRolloutsGet"
    ] = clouddeploy.get(
        "v1/{parent}/rollouts",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListRolloutsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDeliveryPipelinesReleasesRolloutsCancel"
    ] = clouddeploy.get(
        "v1/{parent}/rollouts",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListRolloutsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDeliveryPipelinesReleasesRolloutsIgnoreJob"
    ] = clouddeploy.get(
        "v1/{parent}/rollouts",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListRolloutsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDeliveryPipelinesReleasesRolloutsList"
    ] = clouddeploy.get(
        "v1/{parent}/rollouts",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListRolloutsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDeliveryPipelinesReleasesRolloutsJobRunsTerminate"
    ] = clouddeploy.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["JobRunOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDeliveryPipelinesReleasesRolloutsJobRunsList"
    ] = clouddeploy.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["JobRunOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDeliveryPipelinesReleasesRolloutsJobRunsGet"
    ] = clouddeploy.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["JobRunOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="clouddeploy",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
