from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_clouddeploy() -> Import:
    clouddeploy = HTTPRuntime("https://clouddeploy.googleapis.com/")

    renames = {
        "ErrorResponse": "_clouddeploy_1_ErrorResponse",
        "ListLocationsResponseIn": "_clouddeploy_2_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_clouddeploy_3_ListLocationsResponseOut",
        "DefaultPoolIn": "_clouddeploy_4_DefaultPoolIn",
        "DefaultPoolOut": "_clouddeploy_5_DefaultPoolOut",
        "BuildArtifactIn": "_clouddeploy_6_BuildArtifactIn",
        "BuildArtifactOut": "_clouddeploy_7_BuildArtifactOut",
        "DeployJobIn": "_clouddeploy_8_DeployJobIn",
        "DeployJobOut": "_clouddeploy_9_DeployJobOut",
        "PrivatePoolIn": "_clouddeploy_10_PrivatePoolIn",
        "PrivatePoolOut": "_clouddeploy_11_PrivatePoolOut",
        "ExprIn": "_clouddeploy_12_ExprIn",
        "ExprOut": "_clouddeploy_13_ExprOut",
        "ReleaseReadyConditionIn": "_clouddeploy_14_ReleaseReadyConditionIn",
        "ReleaseReadyConditionOut": "_clouddeploy_15_ReleaseReadyConditionOut",
        "DateIn": "_clouddeploy_16_DateIn",
        "DateOut": "_clouddeploy_17_DateOut",
        "TestIamPermissionsRequestIn": "_clouddeploy_18_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_clouddeploy_19_TestIamPermissionsRequestOut",
        "TargetsTypeConditionIn": "_clouddeploy_20_TargetsTypeConditionIn",
        "TargetsTypeConditionOut": "_clouddeploy_21_TargetsTypeConditionOut",
        "PhaseConfigIn": "_clouddeploy_22_PhaseConfigIn",
        "PhaseConfigOut": "_clouddeploy_23_PhaseConfigOut",
        "ListRolloutsResponseIn": "_clouddeploy_24_ListRolloutsResponseIn",
        "ListRolloutsResponseOut": "_clouddeploy_25_ListRolloutsResponseOut",
        "CloudRunRenderMetadataIn": "_clouddeploy_26_CloudRunRenderMetadataIn",
        "CloudRunRenderMetadataOut": "_clouddeploy_27_CloudRunRenderMetadataOut",
        "CancelOperationRequestIn": "_clouddeploy_28_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_clouddeploy_29_CancelOperationRequestOut",
        "DeploymentJobsIn": "_clouddeploy_30_DeploymentJobsIn",
        "DeploymentJobsOut": "_clouddeploy_31_DeploymentJobsOut",
        "VerifyJobRunIn": "_clouddeploy_32_VerifyJobRunIn",
        "VerifyJobRunOut": "_clouddeploy_33_VerifyJobRunOut",
        "DeliveryPipelineNotificationEventIn": "_clouddeploy_34_DeliveryPipelineNotificationEventIn",
        "DeliveryPipelineNotificationEventOut": "_clouddeploy_35_DeliveryPipelineNotificationEventOut",
        "RenderMetadataIn": "_clouddeploy_36_RenderMetadataIn",
        "RenderMetadataOut": "_clouddeploy_37_RenderMetadataOut",
        "ListDeliveryPipelinesResponseIn": "_clouddeploy_38_ListDeliveryPipelinesResponseIn",
        "ListDeliveryPipelinesResponseOut": "_clouddeploy_39_ListDeliveryPipelinesResponseOut",
        "PipelineConditionIn": "_clouddeploy_40_PipelineConditionIn",
        "PipelineConditionOut": "_clouddeploy_41_PipelineConditionOut",
        "SkaffoldVersionIn": "_clouddeploy_42_SkaffoldVersionIn",
        "SkaffoldVersionOut": "_clouddeploy_43_SkaffoldVersionOut",
        "ExecutionConfigIn": "_clouddeploy_44_ExecutionConfigIn",
        "ExecutionConfigOut": "_clouddeploy_45_ExecutionConfigOut",
        "AuditLogConfigIn": "_clouddeploy_46_AuditLogConfigIn",
        "AuditLogConfigOut": "_clouddeploy_47_AuditLogConfigOut",
        "ReleaseRenderEventIn": "_clouddeploy_48_ReleaseRenderEventIn",
        "ReleaseRenderEventOut": "_clouddeploy_49_ReleaseRenderEventOut",
        "TerminateJobRunResponseIn": "_clouddeploy_50_TerminateJobRunResponseIn",
        "TerminateJobRunResponseOut": "_clouddeploy_51_TerminateJobRunResponseOut",
        "GatewayServiceMeshIn": "_clouddeploy_52_GatewayServiceMeshIn",
        "GatewayServiceMeshOut": "_clouddeploy_53_GatewayServiceMeshOut",
        "IgnoreJobResponseIn": "_clouddeploy_54_IgnoreJobResponseIn",
        "IgnoreJobResponseOut": "_clouddeploy_55_IgnoreJobResponseOut",
        "ListOperationsResponseIn": "_clouddeploy_56_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_clouddeploy_57_ListOperationsResponseOut",
        "CreateChildRolloutJobRunIn": "_clouddeploy_58_CreateChildRolloutJobRunIn",
        "CreateChildRolloutJobRunOut": "_clouddeploy_59_CreateChildRolloutJobRunOut",
        "RuntimeConfigIn": "_clouddeploy_60_RuntimeConfigIn",
        "RuntimeConfigOut": "_clouddeploy_61_RuntimeConfigOut",
        "AdvanceChildRolloutJobRunIn": "_clouddeploy_62_AdvanceChildRolloutJobRunIn",
        "AdvanceChildRolloutJobRunOut": "_clouddeploy_63_AdvanceChildRolloutJobRunOut",
        "TargetNotificationEventIn": "_clouddeploy_64_TargetNotificationEventIn",
        "TargetNotificationEventOut": "_clouddeploy_65_TargetNotificationEventOut",
        "ListReleasesResponseIn": "_clouddeploy_66_ListReleasesResponseIn",
        "ListReleasesResponseOut": "_clouddeploy_67_ListReleasesResponseOut",
        "AnthosClusterIn": "_clouddeploy_68_AnthosClusterIn",
        "AnthosClusterOut": "_clouddeploy_69_AnthosClusterOut",
        "AdvanceRolloutResponseIn": "_clouddeploy_70_AdvanceRolloutResponseIn",
        "AdvanceRolloutResponseOut": "_clouddeploy_71_AdvanceRolloutResponseOut",
        "AbandonReleaseRequestIn": "_clouddeploy_72_AbandonReleaseRequestIn",
        "AbandonReleaseRequestOut": "_clouddeploy_73_AbandonReleaseRequestOut",
        "SkaffoldSupportedConditionIn": "_clouddeploy_74_SkaffoldSupportedConditionIn",
        "SkaffoldSupportedConditionOut": "_clouddeploy_75_SkaffoldSupportedConditionOut",
        "DeployJobRunMetadataIn": "_clouddeploy_76_DeployJobRunMetadataIn",
        "DeployJobRunMetadataOut": "_clouddeploy_77_DeployJobRunMetadataOut",
        "SerialPipelineIn": "_clouddeploy_78_SerialPipelineIn",
        "SerialPipelineOut": "_clouddeploy_79_SerialPipelineOut",
        "DeployArtifactIn": "_clouddeploy_80_DeployArtifactIn",
        "DeployArtifactOut": "_clouddeploy_81_DeployArtifactOut",
        "ListTargetsResponseIn": "_clouddeploy_82_ListTargetsResponseIn",
        "ListTargetsResponseOut": "_clouddeploy_83_ListTargetsResponseOut",
        "ApproveRolloutRequestIn": "_clouddeploy_84_ApproveRolloutRequestIn",
        "ApproveRolloutRequestOut": "_clouddeploy_85_ApproveRolloutRequestOut",
        "ReleaseIn": "_clouddeploy_86_ReleaseIn",
        "ReleaseOut": "_clouddeploy_87_ReleaseOut",
        "CanaryIn": "_clouddeploy_88_CanaryIn",
        "CanaryOut": "_clouddeploy_89_CanaryOut",
        "DeployJobRunIn": "_clouddeploy_90_DeployJobRunIn",
        "DeployJobRunOut": "_clouddeploy_91_DeployJobRunOut",
        "KubernetesConfigIn": "_clouddeploy_92_KubernetesConfigIn",
        "KubernetesConfigOut": "_clouddeploy_93_KubernetesConfigOut",
        "StrategyIn": "_clouddeploy_94_StrategyIn",
        "StrategyOut": "_clouddeploy_95_StrategyOut",
        "CloudRunConfigIn": "_clouddeploy_96_CloudRunConfigIn",
        "CloudRunConfigOut": "_clouddeploy_97_CloudRunConfigOut",
        "RetryJobRequestIn": "_clouddeploy_98_RetryJobRequestIn",
        "RetryJobRequestOut": "_clouddeploy_99_RetryJobRequestOut",
        "StatusIn": "_clouddeploy_100_StatusIn",
        "StatusOut": "_clouddeploy_101_StatusOut",
        "StandardIn": "_clouddeploy_102_StandardIn",
        "StandardOut": "_clouddeploy_103_StandardOut",
        "AdvanceRolloutRequestIn": "_clouddeploy_104_AdvanceRolloutRequestIn",
        "AdvanceRolloutRequestOut": "_clouddeploy_105_AdvanceRolloutRequestOut",
        "JobRunIn": "_clouddeploy_106_JobRunIn",
        "JobRunOut": "_clouddeploy_107_JobRunOut",
        "TargetsPresentConditionIn": "_clouddeploy_108_TargetsPresentConditionIn",
        "TargetsPresentConditionOut": "_clouddeploy_109_TargetsPresentConditionOut",
        "ConfigIn": "_clouddeploy_110_ConfigIn",
        "ConfigOut": "_clouddeploy_111_ConfigOut",
        "TestIamPermissionsResponseIn": "_clouddeploy_112_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_clouddeploy_113_TestIamPermissionsResponseOut",
        "AbandonReleaseResponseIn": "_clouddeploy_114_AbandonReleaseResponseIn",
        "AbandonReleaseResponseOut": "_clouddeploy_115_AbandonReleaseResponseOut",
        "AuditConfigIn": "_clouddeploy_116_AuditConfigIn",
        "AuditConfigOut": "_clouddeploy_117_AuditConfigOut",
        "SetIamPolicyRequestIn": "_clouddeploy_118_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_clouddeploy_119_SetIamPolicyRequestOut",
        "PolicyIn": "_clouddeploy_120_PolicyIn",
        "PolicyOut": "_clouddeploy_121_PolicyOut",
        "LocationIn": "_clouddeploy_122_LocationIn",
        "LocationOut": "_clouddeploy_123_LocationOut",
        "ListJobRunsResponseIn": "_clouddeploy_124_ListJobRunsResponseIn",
        "ListJobRunsResponseOut": "_clouddeploy_125_ListJobRunsResponseOut",
        "AdvanceChildRolloutJobIn": "_clouddeploy_126_AdvanceChildRolloutJobIn",
        "AdvanceChildRolloutJobOut": "_clouddeploy_127_AdvanceChildRolloutJobOut",
        "GkeClusterIn": "_clouddeploy_128_GkeClusterIn",
        "GkeClusterOut": "_clouddeploy_129_GkeClusterOut",
        "CloudRunMetadataIn": "_clouddeploy_130_CloudRunMetadataIn",
        "CloudRunMetadataOut": "_clouddeploy_131_CloudRunMetadataOut",
        "JobIn": "_clouddeploy_132_JobIn",
        "JobOut": "_clouddeploy_133_JobOut",
        "PhaseIn": "_clouddeploy_134_PhaseIn",
        "PhaseOut": "_clouddeploy_135_PhaseOut",
        "VerifyJobIn": "_clouddeploy_136_VerifyJobIn",
        "VerifyJobOut": "_clouddeploy_137_VerifyJobOut",
        "EmptyIn": "_clouddeploy_138_EmptyIn",
        "EmptyOut": "_clouddeploy_139_EmptyOut",
        "RolloutNotificationEventIn": "_clouddeploy_140_RolloutNotificationEventIn",
        "RolloutNotificationEventOut": "_clouddeploy_141_RolloutNotificationEventOut",
        "IgnoreJobRequestIn": "_clouddeploy_142_IgnoreJobRequestIn",
        "IgnoreJobRequestOut": "_clouddeploy_143_IgnoreJobRequestOut",
        "ChildRolloutJobsIn": "_clouddeploy_144_ChildRolloutJobsIn",
        "ChildRolloutJobsOut": "_clouddeploy_145_ChildRolloutJobsOut",
        "JobRunNotificationEventIn": "_clouddeploy_146_JobRunNotificationEventIn",
        "JobRunNotificationEventOut": "_clouddeploy_147_JobRunNotificationEventOut",
        "OperationIn": "_clouddeploy_148_OperationIn",
        "OperationOut": "_clouddeploy_149_OperationOut",
        "TerminateJobRunRequestIn": "_clouddeploy_150_TerminateJobRunRequestIn",
        "TerminateJobRunRequestOut": "_clouddeploy_151_TerminateJobRunRequestOut",
        "TargetArtifactIn": "_clouddeploy_152_TargetArtifactIn",
        "TargetArtifactOut": "_clouddeploy_153_TargetArtifactOut",
        "CustomCanaryDeploymentIn": "_clouddeploy_154_CustomCanaryDeploymentIn",
        "CustomCanaryDeploymentOut": "_clouddeploy_155_CustomCanaryDeploymentOut",
        "RolloutIn": "_clouddeploy_156_RolloutIn",
        "RolloutOut": "_clouddeploy_157_RolloutOut",
        "ReleaseConditionIn": "_clouddeploy_158_ReleaseConditionIn",
        "ReleaseConditionOut": "_clouddeploy_159_ReleaseConditionOut",
        "CancelRolloutRequestIn": "_clouddeploy_160_CancelRolloutRequestIn",
        "CancelRolloutRequestOut": "_clouddeploy_161_CancelRolloutRequestOut",
        "TargetIn": "_clouddeploy_162_TargetIn",
        "TargetOut": "_clouddeploy_163_TargetOut",
        "CloudRunLocationIn": "_clouddeploy_164_CloudRunLocationIn",
        "CloudRunLocationOut": "_clouddeploy_165_CloudRunLocationOut",
        "CanaryDeploymentIn": "_clouddeploy_166_CanaryDeploymentIn",
        "CanaryDeploymentOut": "_clouddeploy_167_CanaryDeploymentOut",
        "RetryJobResponseIn": "_clouddeploy_168_RetryJobResponseIn",
        "RetryJobResponseOut": "_clouddeploy_169_RetryJobResponseOut",
        "MultiTargetIn": "_clouddeploy_170_MultiTargetIn",
        "MultiTargetOut": "_clouddeploy_171_MultiTargetOut",
        "ReleaseNotificationEventIn": "_clouddeploy_172_ReleaseNotificationEventIn",
        "ReleaseNotificationEventOut": "_clouddeploy_173_ReleaseNotificationEventOut",
        "OperationMetadataIn": "_clouddeploy_174_OperationMetadataIn",
        "OperationMetadataOut": "_clouddeploy_175_OperationMetadataOut",
        "CreateChildRolloutJobIn": "_clouddeploy_176_CreateChildRolloutJobIn",
        "CreateChildRolloutJobOut": "_clouddeploy_177_CreateChildRolloutJobOut",
        "CancelRolloutResponseIn": "_clouddeploy_178_CancelRolloutResponseIn",
        "CancelRolloutResponseOut": "_clouddeploy_179_CancelRolloutResponseOut",
        "MetadataIn": "_clouddeploy_180_MetadataIn",
        "MetadataOut": "_clouddeploy_181_MetadataOut",
        "BindingIn": "_clouddeploy_182_BindingIn",
        "BindingOut": "_clouddeploy_183_BindingOut",
        "DeliveryPipelineIn": "_clouddeploy_184_DeliveryPipelineIn",
        "DeliveryPipelineOut": "_clouddeploy_185_DeliveryPipelineOut",
        "TargetRenderIn": "_clouddeploy_186_TargetRenderIn",
        "TargetRenderOut": "_clouddeploy_187_TargetRenderOut",
        "PhaseArtifactIn": "_clouddeploy_188_PhaseArtifactIn",
        "PhaseArtifactOut": "_clouddeploy_189_PhaseArtifactOut",
        "ServiceNetworkingIn": "_clouddeploy_190_ServiceNetworkingIn",
        "ServiceNetworkingOut": "_clouddeploy_191_ServiceNetworkingOut",
        "PipelineReadyConditionIn": "_clouddeploy_192_PipelineReadyConditionIn",
        "PipelineReadyConditionOut": "_clouddeploy_193_PipelineReadyConditionOut",
        "ApproveRolloutResponseIn": "_clouddeploy_194_ApproveRolloutResponseIn",
        "ApproveRolloutResponseOut": "_clouddeploy_195_ApproveRolloutResponseOut",
        "StageIn": "_clouddeploy_196_StageIn",
        "StageOut": "_clouddeploy_197_StageOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["DeployJobIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeployJobIn"]
    )
    types["DeployJobOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeployJobOut"])
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
    types["ExprIn"] = t.struct(
        {
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "location": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "location": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["ReleaseReadyConditionIn"] = t.struct(
        {"status": t.boolean().optional()}
    ).named(renames["ReleaseReadyConditionIn"])
    types["ReleaseReadyConditionOut"] = t.struct(
        {
            "status": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReleaseReadyConditionOut"])
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
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["TargetsTypeConditionIn"] = t.struct(
        {"errorDetails": t.string().optional(), "status": t.boolean().optional()}
    ).named(renames["TargetsTypeConditionIn"])
    types["TargetsTypeConditionOut"] = t.struct(
        {
            "errorDetails": t.string().optional(),
            "status": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetsTypeConditionOut"])
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
    types["ListRolloutsResponseIn"] = t.struct(
        {
            "rollouts": t.array(t.proxy(renames["RolloutIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListRolloutsResponseIn"])
    types["ListRolloutsResponseOut"] = t.struct(
        {
            "rollouts": t.array(t.proxy(renames["RolloutOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListRolloutsResponseOut"])
    types["CloudRunRenderMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CloudRunRenderMetadataIn"]
    )
    types["CloudRunRenderMetadataOut"] = t.struct(
        {
            "service": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudRunRenderMetadataOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["DeploymentJobsIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeploymentJobsIn"]
    )
    types["DeploymentJobsOut"] = t.struct(
        {
            "verifyJob": t.proxy(renames["JobOut"]).optional(),
            "deployJob": t.proxy(renames["JobOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeploymentJobsOut"])
    types["VerifyJobRunIn"] = t.struct({"_": t.string().optional()}).named(
        renames["VerifyJobRunIn"]
    )
    types["VerifyJobRunOut"] = t.struct(
        {
            "failureMessage": t.string().optional(),
            "failureCause": t.string().optional(),
            "artifactUri": t.string().optional(),
            "eventLogPath": t.string().optional(),
            "build": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VerifyJobRunOut"])
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
    types["RenderMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RenderMetadataIn"]
    )
    types["RenderMetadataOut"] = t.struct(
        {
            "cloudRun": t.proxy(renames["CloudRunRenderMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RenderMetadataOut"])
    types["ListDeliveryPipelinesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "deliveryPipelines": t.array(
                t.proxy(renames["DeliveryPipelineIn"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListDeliveryPipelinesResponseIn"])
    types["ListDeliveryPipelinesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "deliveryPipelines": t.array(
                t.proxy(renames["DeliveryPipelineOut"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDeliveryPipelinesResponseOut"])
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
    types["SkaffoldVersionIn"] = t.struct(
        {
            "supportEndDate": t.proxy(renames["DateIn"]).optional(),
            "maintenanceModeTime": t.string().optional(),
            "version": t.string().optional(),
            "supportExpirationTime": t.string().optional(),
        }
    ).named(renames["SkaffoldVersionIn"])
    types["SkaffoldVersionOut"] = t.struct(
        {
            "supportEndDate": t.proxy(renames["DateOut"]).optional(),
            "maintenanceModeTime": t.string().optional(),
            "version": t.string().optional(),
            "supportExpirationTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SkaffoldVersionOut"])
    types["ExecutionConfigIn"] = t.struct(
        {
            "defaultPool": t.proxy(renames["DefaultPoolIn"]).optional(),
            "executionTimeout": t.string().optional(),
            "usages": t.array(t.string()),
            "serviceAccount": t.string().optional(),
            "workerPool": t.string().optional(),
            "artifactStorage": t.string().optional(),
            "privatePool": t.proxy(renames["PrivatePoolIn"]).optional(),
        }
    ).named(renames["ExecutionConfigIn"])
    types["ExecutionConfigOut"] = t.struct(
        {
            "defaultPool": t.proxy(renames["DefaultPoolOut"]).optional(),
            "executionTimeout": t.string().optional(),
            "usages": t.array(t.string()),
            "serviceAccount": t.string().optional(),
            "workerPool": t.string().optional(),
            "artifactStorage": t.string().optional(),
            "privatePool": t.proxy(renames["PrivatePoolOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecutionConfigOut"])
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
    types["TerminateJobRunResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["TerminateJobRunResponseIn"]
    )
    types["TerminateJobRunResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["TerminateJobRunResponseOut"])
    types["GatewayServiceMeshIn"] = t.struct(
        {"service": t.string(), "httpRoute": t.string(), "deployment": t.string()}
    ).named(renames["GatewayServiceMeshIn"])
    types["GatewayServiceMeshOut"] = t.struct(
        {
            "service": t.string(),
            "httpRoute": t.string(),
            "deployment": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GatewayServiceMeshOut"])
    types["IgnoreJobResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["IgnoreJobResponseIn"]
    )
    types["IgnoreJobResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["IgnoreJobResponseOut"])
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
    types["RuntimeConfigIn"] = t.struct(
        {
            "kubernetes": t.proxy(renames["KubernetesConfigIn"]).optional(),
            "cloudRun": t.proxy(renames["CloudRunConfigIn"]).optional(),
        }
    ).named(renames["RuntimeConfigIn"])
    types["RuntimeConfigOut"] = t.struct(
        {
            "kubernetes": t.proxy(renames["KubernetesConfigOut"]).optional(),
            "cloudRun": t.proxy(renames["CloudRunConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RuntimeConfigOut"])
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
    types["AnthosClusterIn"] = t.struct({"membership": t.string().optional()}).named(
        renames["AnthosClusterIn"]
    )
    types["AnthosClusterOut"] = t.struct(
        {
            "membership": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnthosClusterOut"])
    types["AdvanceRolloutResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AdvanceRolloutResponseIn"]
    )
    types["AdvanceRolloutResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AdvanceRolloutResponseOut"])
    types["AbandonReleaseRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AbandonReleaseRequestIn"]
    )
    types["AbandonReleaseRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AbandonReleaseRequestOut"])
    types["SkaffoldSupportedConditionIn"] = t.struct(
        {
            "status": t.boolean().optional(),
            "maintenanceModeTime": t.string().optional(),
            "skaffoldSupportState": t.string().optional(),
            "supportExpirationTime": t.string().optional(),
        }
    ).named(renames["SkaffoldSupportedConditionIn"])
    types["SkaffoldSupportedConditionOut"] = t.struct(
        {
            "status": t.boolean().optional(),
            "maintenanceModeTime": t.string().optional(),
            "skaffoldSupportState": t.string().optional(),
            "supportExpirationTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SkaffoldSupportedConditionOut"])
    types["DeployJobRunMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeployJobRunMetadataIn"]
    )
    types["DeployJobRunMetadataOut"] = t.struct(
        {
            "cloudRun": t.proxy(renames["CloudRunMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeployJobRunMetadataOut"])
    types["SerialPipelineIn"] = t.struct(
        {"stages": t.array(t.proxy(renames["StageIn"])).optional()}
    ).named(renames["SerialPipelineIn"])
    types["SerialPipelineOut"] = t.struct(
        {
            "stages": t.array(t.proxy(renames["StageOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SerialPipelineOut"])
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
    types["ApproveRolloutRequestIn"] = t.struct({"approved": t.boolean()}).named(
        renames["ApproveRolloutRequestIn"]
    )
    types["ApproveRolloutRequestOut"] = t.struct(
        {"approved": t.boolean(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ApproveRolloutRequestOut"])
    types["ReleaseIn"] = t.struct(
        {
            "skaffoldConfigPath": t.string().optional(),
            "name": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "skaffoldConfigUri": t.string().optional(),
            "skaffoldVersion": t.string().optional(),
            "buildArtifacts": t.array(t.proxy(renames["BuildArtifactIn"])).optional(),
            "description": t.string().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["ReleaseIn"])
    types["ReleaseOut"] = t.struct(
        {
            "skaffoldConfigPath": t.string().optional(),
            "uid": t.string().optional(),
            "renderState": t.string().optional(),
            "renderStartTime": t.string().optional(),
            "name": t.string().optional(),
            "condition": t.proxy(renames["ReleaseConditionOut"]).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "targetSnapshots": t.array(t.proxy(renames["TargetOut"])).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "skaffoldConfigUri": t.string().optional(),
            "skaffoldVersion": t.string().optional(),
            "buildArtifacts": t.array(t.proxy(renames["BuildArtifactOut"])).optional(),
            "deliveryPipelineSnapshot": t.proxy(
                renames["DeliveryPipelineOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "targetArtifacts": t.struct({"_": t.string().optional()}).optional(),
            "renderEndTime": t.string().optional(),
            "targetRenders": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "abandoned": t.boolean().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReleaseOut"])
    types["CanaryIn"] = t.struct(
        {
            "canaryDeployment": t.proxy(renames["CanaryDeploymentIn"]).optional(),
            "customCanaryDeployment": t.proxy(
                renames["CustomCanaryDeploymentIn"]
            ).optional(),
            "runtimeConfig": t.proxy(renames["RuntimeConfigIn"]).optional(),
        }
    ).named(renames["CanaryIn"])
    types["CanaryOut"] = t.struct(
        {
            "canaryDeployment": t.proxy(renames["CanaryDeploymentOut"]).optional(),
            "customCanaryDeployment": t.proxy(
                renames["CustomCanaryDeploymentOut"]
            ).optional(),
            "runtimeConfig": t.proxy(renames["RuntimeConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CanaryOut"])
    types["DeployJobRunIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeployJobRunIn"]
    )
    types["DeployJobRunOut"] = t.struct(
        {
            "failureCause": t.string().optional(),
            "artifact": t.proxy(renames["DeployArtifactOut"]).optional(),
            "failureMessage": t.string().optional(),
            "metadata": t.proxy(renames["DeployJobRunMetadataOut"]).optional(),
            "build": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeployJobRunOut"])
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
    types["CloudRunConfigIn"] = t.struct(
        {"automaticTrafficControl": t.boolean().optional()}
    ).named(renames["CloudRunConfigIn"])
    types["CloudRunConfigOut"] = t.struct(
        {
            "automaticTrafficControl": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudRunConfigOut"])
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
    types["StatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["StandardIn"] = t.struct({"verify": t.boolean().optional()}).named(
        renames["StandardIn"]
    )
    types["StandardOut"] = t.struct(
        {
            "verify": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StandardOut"])
    types["AdvanceRolloutRequestIn"] = t.struct({"phaseId": t.string()}).named(
        renames["AdvanceRolloutRequestIn"]
    )
    types["AdvanceRolloutRequestOut"] = t.struct(
        {"phaseId": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AdvanceRolloutRequestOut"])
    types["JobRunIn"] = t.struct({"name": t.string().optional()}).named(
        renames["JobRunIn"]
    )
    types["JobRunOut"] = t.struct(
        {
            "phaseId": t.string().optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "createChildRolloutJobRun": t.proxy(
                renames["CreateChildRolloutJobRunOut"]
            ).optional(),
            "etag": t.string().optional(),
            "startTime": t.string().optional(),
            "uid": t.string().optional(),
            "deployJobRun": t.proxy(renames["DeployJobRunOut"]).optional(),
            "createTime": t.string().optional(),
            "endTime": t.string().optional(),
            "verifyJobRun": t.proxy(renames["VerifyJobRunOut"]).optional(),
            "advanceChildRolloutJobRun": t.proxy(
                renames["AdvanceChildRolloutJobRunOut"]
            ).optional(),
            "jobId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobRunOut"])
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
    types["ConfigIn"] = t.struct(
        {
            "supportedVersions": t.array(
                t.proxy(renames["SkaffoldVersionIn"])
            ).optional(),
            "name": t.string().optional(),
            "defaultSkaffoldVersion": t.string().optional(),
        }
    ).named(renames["ConfigIn"])
    types["ConfigOut"] = t.struct(
        {
            "supportedVersions": t.array(
                t.proxy(renames["SkaffoldVersionOut"])
            ).optional(),
            "name": t.string().optional(),
            "defaultSkaffoldVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["AbandonReleaseResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AbandonReleaseResponseIn"]
    )
    types["AbandonReleaseResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AbandonReleaseResponseOut"])
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
    types["PolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "version": t.integer().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "version": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["LocationIn"] = t.struct(
        {
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
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
    types["AdvanceChildRolloutJobIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AdvanceChildRolloutJobIn"]
    )
    types["AdvanceChildRolloutJobOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AdvanceChildRolloutJobOut"])
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
    types["JobIn"] = t.struct({"_": t.string().optional()}).named(renames["JobIn"])
    types["JobOut"] = t.struct(
        {
            "advanceChildRolloutJob": t.proxy(
                renames["AdvanceChildRolloutJobOut"]
            ).optional(),
            "id": t.string().optional(),
            "jobRun": t.string().optional(),
            "deployJob": t.proxy(renames["DeployJobOut"]).optional(),
            "state": t.string().optional(),
            "verifyJob": t.proxy(renames["VerifyJobOut"]).optional(),
            "skipMessage": t.string().optional(),
            "createChildRolloutJob": t.proxy(
                renames["CreateChildRolloutJobOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobOut"])
    types["PhaseIn"] = t.struct({"_": t.string().optional()}).named(renames["PhaseIn"])
    types["PhaseOut"] = t.struct(
        {
            "childRolloutJobs": t.proxy(renames["ChildRolloutJobsOut"]).optional(),
            "id": t.string().optional(),
            "state": t.string().optional(),
            "deploymentJobs": t.proxy(renames["DeploymentJobsOut"]).optional(),
            "skipMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhaseOut"])
    types["VerifyJobIn"] = t.struct({"_": t.string().optional()}).named(
        renames["VerifyJobIn"]
    )
    types["VerifyJobOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["VerifyJobOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["RolloutNotificationEventIn"] = t.struct(
        {
            "targetId": t.string().optional(),
            "message": t.string().optional(),
            "rollout": t.string().optional(),
            "pipelineUid": t.string().optional(),
            "releaseUid": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["RolloutNotificationEventIn"])
    types["RolloutNotificationEventOut"] = t.struct(
        {
            "targetId": t.string().optional(),
            "message": t.string().optional(),
            "rollout": t.string().optional(),
            "pipelineUid": t.string().optional(),
            "releaseUid": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RolloutNotificationEventOut"])
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
    types["JobRunNotificationEventIn"] = t.struct(
        {
            "message": t.string().optional(),
            "releaseUid": t.string().optional(),
            "type": t.string().optional(),
            "targetId": t.string().optional(),
            "pipelineUid": t.string().optional(),
            "rolloutUid": t.string().optional(),
            "jobRun": t.string().optional(),
        }
    ).named(renames["JobRunNotificationEventIn"])
    types["JobRunNotificationEventOut"] = t.struct(
        {
            "message": t.string().optional(),
            "releaseUid": t.string().optional(),
            "type": t.string().optional(),
            "targetId": t.string().optional(),
            "pipelineUid": t.string().optional(),
            "rolloutUid": t.string().optional(),
            "jobRun": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobRunNotificationEventOut"])
    types["OperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["TerminateJobRunRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["TerminateJobRunRequestIn"]
    )
    types["TerminateJobRunRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["TerminateJobRunRequestOut"])
    types["TargetArtifactIn"] = t.struct({"_": t.string().optional()}).named(
        renames["TargetArtifactIn"]
    )
    types["TargetArtifactOut"] = t.struct(
        {
            "artifactUri": t.string().optional(),
            "manifestPath": t.string().optional(),
            "skaffoldConfigPath": t.string().optional(),
            "phaseArtifacts": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetArtifactOut"])
    types["CustomCanaryDeploymentIn"] = t.struct(
        {"phaseConfigs": t.array(t.proxy(renames["PhaseConfigIn"]))}
    ).named(renames["CustomCanaryDeploymentIn"])
    types["CustomCanaryDeploymentOut"] = t.struct(
        {
            "phaseConfigs": t.array(t.proxy(renames["PhaseConfigOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomCanaryDeploymentOut"])
    types["RolloutIn"] = t.struct(
        {
            "targetId": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "etag": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["RolloutIn"])
    types["RolloutOut"] = t.struct(
        {
            "targetId": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.proxy(renames["MetadataOut"]).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "etag": t.string().optional(),
            "enqueueTime": t.string().optional(),
            "deployEndTime": t.string().optional(),
            "name": t.string().optional(),
            "phases": t.array(t.proxy(renames["PhaseOut"])).optional(),
            "deployFailureCause": t.string().optional(),
            "approvalState": t.string().optional(),
            "description": t.string().optional(),
            "approveTime": t.string().optional(),
            "deployStartTime": t.string().optional(),
            "createTime": t.string().optional(),
            "deployingBuild": t.string().optional(),
            "state": t.string().optional(),
            "controllerRollout": t.string().optional(),
            "uid": t.string().optional(),
            "failureReason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RolloutOut"])
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
    types["CancelRolloutRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelRolloutRequestIn"]
    )
    types["CancelRolloutRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelRolloutRequestOut"])
    types["TargetIn"] = t.struct(
        {
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "anthosCluster": t.proxy(renames["AnthosClusterIn"]).optional(),
            "gke": t.proxy(renames["GkeClusterIn"]).optional(),
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "executionConfigs": t.array(
                t.proxy(renames["ExecutionConfigIn"])
            ).optional(),
            "run": t.proxy(renames["CloudRunLocationIn"]).optional(),
            "requireApproval": t.boolean().optional(),
            "name": t.string().optional(),
            "multiTarget": t.proxy(renames["MultiTargetIn"]).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["TargetIn"])
    types["TargetOut"] = t.struct(
        {
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "anthosCluster": t.proxy(renames["AnthosClusterOut"]).optional(),
            "gke": t.proxy(renames["GkeClusterOut"]).optional(),
            "uid": t.string().optional(),
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "executionConfigs": t.array(
                t.proxy(renames["ExecutionConfigOut"])
            ).optional(),
            "targetId": t.string().optional(),
            "run": t.proxy(renames["CloudRunLocationOut"]).optional(),
            "requireApproval": t.boolean().optional(),
            "name": t.string().optional(),
            "multiTarget": t.proxy(renames["MultiTargetOut"]).optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetOut"])
    types["CloudRunLocationIn"] = t.struct({"location": t.string()}).named(
        renames["CloudRunLocationIn"]
    )
    types["CloudRunLocationOut"] = t.struct(
        {"location": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CloudRunLocationOut"])
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
    types["RetryJobResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RetryJobResponseIn"]
    )
    types["RetryJobResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RetryJobResponseOut"])
    types["MultiTargetIn"] = t.struct({"targetIds": t.array(t.string())}).named(
        renames["MultiTargetIn"]
    )
    types["MultiTargetOut"] = t.struct(
        {
            "targetIds": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MultiTargetOut"])
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
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "apiVersion": t.string().optional(),
            "createTime": t.string().optional(),
            "statusMessage": t.string().optional(),
            "target": t.string().optional(),
            "verb": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["CreateChildRolloutJobIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CreateChildRolloutJobIn"]
    )
    types["CreateChildRolloutJobOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CreateChildRolloutJobOut"])
    types["CancelRolloutResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelRolloutResponseIn"]
    )
    types["CancelRolloutResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelRolloutResponseOut"])
    types["MetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MetadataIn"]
    )
    types["MetadataOut"] = t.struct(
        {
            "cloudRun": t.proxy(renames["CloudRunMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetadataOut"])
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
    types["DeliveryPipelineIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "suspended": t.boolean().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "etag": t.string().optional(),
            "serialPipeline": t.proxy(renames["SerialPipelineIn"]).optional(),
        }
    ).named(renames["DeliveryPipelineIn"])
    types["DeliveryPipelineOut"] = t.struct(
        {
            "uid": t.string().optional(),
            "createTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "suspended": t.boolean().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "condition": t.proxy(renames["PipelineConditionOut"]).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "etag": t.string().optional(),
            "serialPipeline": t.proxy(renames["SerialPipelineOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeliveryPipelineOut"])
    types["TargetRenderIn"] = t.struct({"_": t.string().optional()}).named(
        renames["TargetRenderIn"]
    )
    types["TargetRenderOut"] = t.struct(
        {
            "metadata": t.proxy(renames["RenderMetadataOut"]).optional(),
            "renderingBuild": t.string().optional(),
            "failureCause": t.string().optional(),
            "failureMessage": t.string().optional(),
            "renderingState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetRenderOut"])
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
    types["ServiceNetworkingIn"] = t.struct(
        {"deployment": t.string(), "service": t.string()}
    ).named(renames["ServiceNetworkingIn"])
    types["ServiceNetworkingOut"] = t.struct(
        {
            "deployment": t.string(),
            "service": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceNetworkingOut"])
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
    types["ApproveRolloutResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ApproveRolloutResponseIn"]
    )
    types["ApproveRolloutResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ApproveRolloutResponseOut"])
    types["StageIn"] = t.struct(
        {
            "strategy": t.proxy(renames["StrategyIn"]).optional(),
            "targetId": t.string().optional(),
            "profiles": t.array(t.string()).optional(),
        }
    ).named(renames["StageIn"])
    types["StageOut"] = t.struct(
        {
            "strategy": t.proxy(renames["StrategyOut"]).optional(),
            "targetId": t.string().optional(),
            "profiles": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StageOut"])

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
    functions["projectsLocationsDeliveryPipelinesGetIamPolicy"] = clouddeploy.get(
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
    functions["projectsLocationsDeliveryPipelinesList"] = clouddeploy.get(
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
    functions["projectsLocationsDeliveryPipelinesTestIamPermissions"] = clouddeploy.get(
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
    functions["projectsLocationsDeliveryPipelinesReleasesAbandon"] = clouddeploy.get(
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
        "projectsLocationsDeliveryPipelinesReleasesRolloutsCreate"
    ] = clouddeploy.get(
        "v1/{parent}/rollouts",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListRolloutsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDeliveryPipelinesReleasesRolloutsRetryJob"
    ] = clouddeploy.get(
        "v1/{parent}/rollouts",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
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
    functions["projectsLocationsOperationsCancel"] = clouddeploy.get(
        "v1/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = clouddeploy.get(
        "v1/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = clouddeploy.get(
        "v1/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = clouddeploy.get(
        "v1/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTargetsCreate"] = clouddeploy.get(
        "v1/{parent}/targets",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTargetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTargetsSetIamPolicy"] = clouddeploy.get(
        "v1/{parent}/targets",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTargetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="clouddeploy",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
