from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_run() -> Import:
    run = HTTPRuntime("https://run.googleapis.com/")

    renames = {
        "ErrorResponse": "_run_1_ErrorResponse",
        "GoogleCloudRunV2ListServicesResponseIn": "_run_2_GoogleCloudRunV2ListServicesResponseIn",
        "GoogleCloudRunV2ListServicesResponseOut": "_run_3_GoogleCloudRunV2ListServicesResponseOut",
        "GoogleIamV1BindingIn": "_run_4_GoogleIamV1BindingIn",
        "GoogleIamV1BindingOut": "_run_5_GoogleIamV1BindingOut",
        "GoogleCloudRunV2VolumeIn": "_run_6_GoogleCloudRunV2VolumeIn",
        "GoogleCloudRunV2VolumeOut": "_run_7_GoogleCloudRunV2VolumeOut",
        "GoogleCloudRunV2ConditionIn": "_run_8_GoogleCloudRunV2ConditionIn",
        "GoogleCloudRunV2ConditionOut": "_run_9_GoogleCloudRunV2ConditionOut",
        "GoogleCloudRunV2VersionToPathIn": "_run_10_GoogleCloudRunV2VersionToPathIn",
        "GoogleCloudRunV2VersionToPathOut": "_run_11_GoogleCloudRunV2VersionToPathOut",
        "GoogleCloudRunV2ResourceRequirementsIn": "_run_12_GoogleCloudRunV2ResourceRequirementsIn",
        "GoogleCloudRunV2ResourceRequirementsOut": "_run_13_GoogleCloudRunV2ResourceRequirementsOut",
        "GoogleCloudRunV2GRPCActionIn": "_run_14_GoogleCloudRunV2GRPCActionIn",
        "GoogleCloudRunV2GRPCActionOut": "_run_15_GoogleCloudRunV2GRPCActionOut",
        "GoogleCloudRunV2EnvVarSourceIn": "_run_16_GoogleCloudRunV2EnvVarSourceIn",
        "GoogleCloudRunV2EnvVarSourceOut": "_run_17_GoogleCloudRunV2EnvVarSourceOut",
        "GoogleCloudRunV2SecretKeySelectorIn": "_run_18_GoogleCloudRunV2SecretKeySelectorIn",
        "GoogleCloudRunV2SecretKeySelectorOut": "_run_19_GoogleCloudRunV2SecretKeySelectorOut",
        "GoogleCloudRunV2EnvVarIn": "_run_20_GoogleCloudRunV2EnvVarIn",
        "GoogleCloudRunV2EnvVarOut": "_run_21_GoogleCloudRunV2EnvVarOut",
        "GoogleCloudRunV2CloudSqlInstanceIn": "_run_22_GoogleCloudRunV2CloudSqlInstanceIn",
        "GoogleCloudRunV2CloudSqlInstanceOut": "_run_23_GoogleCloudRunV2CloudSqlInstanceOut",
        "GoogleCloudRunV2VolumeMountIn": "_run_24_GoogleCloudRunV2VolumeMountIn",
        "GoogleCloudRunV2VolumeMountOut": "_run_25_GoogleCloudRunV2VolumeMountOut",
        "GoogleCloudRunV2ServiceIn": "_run_26_GoogleCloudRunV2ServiceIn",
        "GoogleCloudRunV2ServiceOut": "_run_27_GoogleCloudRunV2ServiceOut",
        "GoogleIamV1SetIamPolicyRequestIn": "_run_28_GoogleIamV1SetIamPolicyRequestIn",
        "GoogleIamV1SetIamPolicyRequestOut": "_run_29_GoogleIamV1SetIamPolicyRequestOut",
        "GoogleProtobufEmptyIn": "_run_30_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_run_31_GoogleProtobufEmptyOut",
        "GoogleCloudRunV2ListTasksResponseIn": "_run_32_GoogleCloudRunV2ListTasksResponseIn",
        "GoogleCloudRunV2ListTasksResponseOut": "_run_33_GoogleCloudRunV2ListTasksResponseOut",
        "GoogleCloudRunV2TrafficTargetIn": "_run_34_GoogleCloudRunV2TrafficTargetIn",
        "GoogleCloudRunV2TrafficTargetOut": "_run_35_GoogleCloudRunV2TrafficTargetOut",
        "GoogleCloudRunV2TrafficTargetStatusIn": "_run_36_GoogleCloudRunV2TrafficTargetStatusIn",
        "GoogleCloudRunV2TrafficTargetStatusOut": "_run_37_GoogleCloudRunV2TrafficTargetStatusOut",
        "GoogleLongrunningWaitOperationRequestIn": "_run_38_GoogleLongrunningWaitOperationRequestIn",
        "GoogleLongrunningWaitOperationRequestOut": "_run_39_GoogleLongrunningWaitOperationRequestOut",
        "GoogleCloudRunV2ListExecutionsResponseIn": "_run_40_GoogleCloudRunV2ListExecutionsResponseIn",
        "GoogleCloudRunV2ListExecutionsResponseOut": "_run_41_GoogleCloudRunV2ListExecutionsResponseOut",
        "GoogleCloudRunV2VpcAccessIn": "_run_42_GoogleCloudRunV2VpcAccessIn",
        "GoogleCloudRunV2VpcAccessOut": "_run_43_GoogleCloudRunV2VpcAccessOut",
        "GoogleCloudRunV2ExecutionTemplateIn": "_run_44_GoogleCloudRunV2ExecutionTemplateIn",
        "GoogleCloudRunV2ExecutionTemplateOut": "_run_45_GoogleCloudRunV2ExecutionTemplateOut",
        "GoogleIamV1AuditLogConfigIn": "_run_46_GoogleIamV1AuditLogConfigIn",
        "GoogleIamV1AuditLogConfigOut": "_run_47_GoogleIamV1AuditLogConfigOut",
        "GoogleCloudRunV2HTTPGetActionIn": "_run_48_GoogleCloudRunV2HTTPGetActionIn",
        "GoogleCloudRunV2HTTPGetActionOut": "_run_49_GoogleCloudRunV2HTTPGetActionOut",
        "GoogleCloudRunV2JobIn": "_run_50_GoogleCloudRunV2JobIn",
        "GoogleCloudRunV2JobOut": "_run_51_GoogleCloudRunV2JobOut",
        "GoogleIamV1AuditConfigIn": "_run_52_GoogleIamV1AuditConfigIn",
        "GoogleIamV1AuditConfigOut": "_run_53_GoogleIamV1AuditConfigOut",
        "GoogleRpcStatusIn": "_run_54_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_run_55_GoogleRpcStatusOut",
        "GoogleIamV1PolicyIn": "_run_56_GoogleIamV1PolicyIn",
        "GoogleIamV1PolicyOut": "_run_57_GoogleIamV1PolicyOut",
        "GoogleCloudRunV2TCPSocketActionIn": "_run_58_GoogleCloudRunV2TCPSocketActionIn",
        "GoogleCloudRunV2TCPSocketActionOut": "_run_59_GoogleCloudRunV2TCPSocketActionOut",
        "GoogleCloudRunV2HTTPHeaderIn": "_run_60_GoogleCloudRunV2HTTPHeaderIn",
        "GoogleCloudRunV2HTTPHeaderOut": "_run_61_GoogleCloudRunV2HTTPHeaderOut",
        "GoogleLongrunningOperationIn": "_run_62_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_run_63_GoogleLongrunningOperationOut",
        "GoogleCloudRunV2ListRevisionsResponseIn": "_run_64_GoogleCloudRunV2ListRevisionsResponseIn",
        "GoogleCloudRunV2ListRevisionsResponseOut": "_run_65_GoogleCloudRunV2ListRevisionsResponseOut",
        "GoogleCloudRunV2RevisionScalingIn": "_run_66_GoogleCloudRunV2RevisionScalingIn",
        "GoogleCloudRunV2RevisionScalingOut": "_run_67_GoogleCloudRunV2RevisionScalingOut",
        "GoogleCloudRunV2TaskIn": "_run_68_GoogleCloudRunV2TaskIn",
        "GoogleCloudRunV2TaskOut": "_run_69_GoogleCloudRunV2TaskOut",
        "GoogleCloudRunV2ListJobsResponseIn": "_run_70_GoogleCloudRunV2ListJobsResponseIn",
        "GoogleCloudRunV2ListJobsResponseOut": "_run_71_GoogleCloudRunV2ListJobsResponseOut",
        "GoogleCloudRunV2ProbeIn": "_run_72_GoogleCloudRunV2ProbeIn",
        "GoogleCloudRunV2ProbeOut": "_run_73_GoogleCloudRunV2ProbeOut",
        "GoogleCloudRunV2RevisionTemplateIn": "_run_74_GoogleCloudRunV2RevisionTemplateIn",
        "GoogleCloudRunV2RevisionTemplateOut": "_run_75_GoogleCloudRunV2RevisionTemplateOut",
        "GoogleCloudRunV2RevisionIn": "_run_76_GoogleCloudRunV2RevisionIn",
        "GoogleCloudRunV2RevisionOut": "_run_77_GoogleCloudRunV2RevisionOut",
        "GoogleCloudRunV2TaskAttemptResultIn": "_run_78_GoogleCloudRunV2TaskAttemptResultIn",
        "GoogleCloudRunV2TaskAttemptResultOut": "_run_79_GoogleCloudRunV2TaskAttemptResultOut",
        "GoogleIamV1TestIamPermissionsRequestIn": "_run_80_GoogleIamV1TestIamPermissionsRequestIn",
        "GoogleIamV1TestIamPermissionsRequestOut": "_run_81_GoogleIamV1TestIamPermissionsRequestOut",
        "GoogleCloudRunV2TaskTemplateIn": "_run_82_GoogleCloudRunV2TaskTemplateIn",
        "GoogleCloudRunV2TaskTemplateOut": "_run_83_GoogleCloudRunV2TaskTemplateOut",
        "GoogleLongrunningListOperationsResponseIn": "_run_84_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_run_85_GoogleLongrunningListOperationsResponseOut",
        "GoogleCloudRunV2RunJobRequestIn": "_run_86_GoogleCloudRunV2RunJobRequestIn",
        "GoogleCloudRunV2RunJobRequestOut": "_run_87_GoogleCloudRunV2RunJobRequestOut",
        "GoogleCloudRunV2ExecutionIn": "_run_88_GoogleCloudRunV2ExecutionIn",
        "GoogleCloudRunV2ExecutionOut": "_run_89_GoogleCloudRunV2ExecutionOut",
        "GoogleCloudRunV2SecretVolumeSourceIn": "_run_90_GoogleCloudRunV2SecretVolumeSourceIn",
        "GoogleCloudRunV2SecretVolumeSourceOut": "_run_91_GoogleCloudRunV2SecretVolumeSourceOut",
        "GoogleIamV1TestIamPermissionsResponseIn": "_run_92_GoogleIamV1TestIamPermissionsResponseIn",
        "GoogleIamV1TestIamPermissionsResponseOut": "_run_93_GoogleIamV1TestIamPermissionsResponseOut",
        "GoogleCloudRunV2ContainerIn": "_run_94_GoogleCloudRunV2ContainerIn",
        "GoogleCloudRunV2ContainerOut": "_run_95_GoogleCloudRunV2ContainerOut",
        "GoogleCloudRunV2ExecutionReferenceIn": "_run_96_GoogleCloudRunV2ExecutionReferenceIn",
        "GoogleCloudRunV2ExecutionReferenceOut": "_run_97_GoogleCloudRunV2ExecutionReferenceOut",
        "GoogleTypeExprIn": "_run_98_GoogleTypeExprIn",
        "GoogleTypeExprOut": "_run_99_GoogleTypeExprOut",
        "GoogleCloudRunV2ContainerPortIn": "_run_100_GoogleCloudRunV2ContainerPortIn",
        "GoogleCloudRunV2ContainerPortOut": "_run_101_GoogleCloudRunV2ContainerPortOut",
        "GoogleCloudRunV2BinaryAuthorizationIn": "_run_102_GoogleCloudRunV2BinaryAuthorizationIn",
        "GoogleCloudRunV2BinaryAuthorizationOut": "_run_103_GoogleCloudRunV2BinaryAuthorizationOut",
        "GoogleCloudRunV2EmptyDirVolumeSourceIn": "_run_104_GoogleCloudRunV2EmptyDirVolumeSourceIn",
        "GoogleCloudRunV2EmptyDirVolumeSourceOut": "_run_105_GoogleCloudRunV2EmptyDirVolumeSourceOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudRunV2ListServicesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "services": t.array(
                t.proxy(renames["GoogleCloudRunV2ServiceIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudRunV2ListServicesResponseIn"])
    types["GoogleCloudRunV2ListServicesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "services": t.array(
                t.proxy(renames["GoogleCloudRunV2ServiceOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2ListServicesResponseOut"])
    types["GoogleIamV1BindingIn"] = t.struct(
        {
            "condition": t.proxy(renames["GoogleTypeExprIn"]).optional(),
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
        }
    ).named(renames["GoogleIamV1BindingIn"])
    types["GoogleIamV1BindingOut"] = t.struct(
        {
            "condition": t.proxy(renames["GoogleTypeExprOut"]).optional(),
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1BindingOut"])
    types["GoogleCloudRunV2VolumeIn"] = t.struct(
        {
            "name": t.string(),
            "emptyDir": t.proxy(
                renames["GoogleCloudRunV2EmptyDirVolumeSourceIn"]
            ).optional(),
            "secret": t.proxy(
                renames["GoogleCloudRunV2SecretVolumeSourceIn"]
            ).optional(),
            "cloudSqlInstance": t.proxy(
                renames["GoogleCloudRunV2CloudSqlInstanceIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudRunV2VolumeIn"])
    types["GoogleCloudRunV2VolumeOut"] = t.struct(
        {
            "name": t.string(),
            "emptyDir": t.proxy(
                renames["GoogleCloudRunV2EmptyDirVolumeSourceOut"]
            ).optional(),
            "secret": t.proxy(
                renames["GoogleCloudRunV2SecretVolumeSourceOut"]
            ).optional(),
            "cloudSqlInstance": t.proxy(
                renames["GoogleCloudRunV2CloudSqlInstanceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2VolumeOut"])
    types["GoogleCloudRunV2ConditionIn"] = t.struct(
        {
            "state": t.string().optional(),
            "severity": t.string().optional(),
            "type": t.string().optional(),
            "revisionReason": t.string().optional(),
            "reason": t.string().optional(),
            "executionReason": t.string().optional(),
            "lastTransitionTime": t.string().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["GoogleCloudRunV2ConditionIn"])
    types["GoogleCloudRunV2ConditionOut"] = t.struct(
        {
            "state": t.string().optional(),
            "severity": t.string().optional(),
            "type": t.string().optional(),
            "revisionReason": t.string().optional(),
            "reason": t.string().optional(),
            "executionReason": t.string().optional(),
            "lastTransitionTime": t.string().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2ConditionOut"])
    types["GoogleCloudRunV2VersionToPathIn"] = t.struct(
        {
            "mode": t.integer().optional(),
            "path": t.string(),
            "version": t.string().optional(),
        }
    ).named(renames["GoogleCloudRunV2VersionToPathIn"])
    types["GoogleCloudRunV2VersionToPathOut"] = t.struct(
        {
            "mode": t.integer().optional(),
            "path": t.string(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2VersionToPathOut"])
    types["GoogleCloudRunV2ResourceRequirementsIn"] = t.struct(
        {
            "cpuIdle": t.boolean().optional(),
            "limits": t.struct({"_": t.string().optional()}).optional(),
            "startupCpuBoost": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudRunV2ResourceRequirementsIn"])
    types["GoogleCloudRunV2ResourceRequirementsOut"] = t.struct(
        {
            "cpuIdle": t.boolean().optional(),
            "limits": t.struct({"_": t.string().optional()}).optional(),
            "startupCpuBoost": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2ResourceRequirementsOut"])
    types["GoogleCloudRunV2GRPCActionIn"] = t.struct(
        {"service": t.string().optional(), "port": t.integer().optional()}
    ).named(renames["GoogleCloudRunV2GRPCActionIn"])
    types["GoogleCloudRunV2GRPCActionOut"] = t.struct(
        {
            "service": t.string().optional(),
            "port": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2GRPCActionOut"])
    types["GoogleCloudRunV2EnvVarSourceIn"] = t.struct(
        {
            "secretKeyRef": t.proxy(
                renames["GoogleCloudRunV2SecretKeySelectorIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudRunV2EnvVarSourceIn"])
    types["GoogleCloudRunV2EnvVarSourceOut"] = t.struct(
        {
            "secretKeyRef": t.proxy(
                renames["GoogleCloudRunV2SecretKeySelectorOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2EnvVarSourceOut"])
    types["GoogleCloudRunV2SecretKeySelectorIn"] = t.struct(
        {"secret": t.string(), "version": t.string().optional()}
    ).named(renames["GoogleCloudRunV2SecretKeySelectorIn"])
    types["GoogleCloudRunV2SecretKeySelectorOut"] = t.struct(
        {
            "secret": t.string(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2SecretKeySelectorOut"])
    types["GoogleCloudRunV2EnvVarIn"] = t.struct(
        {
            "name": t.string(),
            "valueSource": t.proxy(
                renames["GoogleCloudRunV2EnvVarSourceIn"]
            ).optional(),
            "value": t.string().optional(),
        }
    ).named(renames["GoogleCloudRunV2EnvVarIn"])
    types["GoogleCloudRunV2EnvVarOut"] = t.struct(
        {
            "name": t.string(),
            "valueSource": t.proxy(
                renames["GoogleCloudRunV2EnvVarSourceOut"]
            ).optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2EnvVarOut"])
    types["GoogleCloudRunV2CloudSqlInstanceIn"] = t.struct(
        {"instances": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudRunV2CloudSqlInstanceIn"])
    types["GoogleCloudRunV2CloudSqlInstanceOut"] = t.struct(
        {
            "instances": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2CloudSqlInstanceOut"])
    types["GoogleCloudRunV2VolumeMountIn"] = t.struct(
        {"mountPath": t.string(), "name": t.string()}
    ).named(renames["GoogleCloudRunV2VolumeMountIn"])
    types["GoogleCloudRunV2VolumeMountOut"] = t.struct(
        {
            "mountPath": t.string(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2VolumeMountOut"])
    types["GoogleCloudRunV2ServiceIn"] = t.struct(
        {
            "name": t.string().optional(),
            "binaryAuthorization": t.proxy(
                renames["GoogleCloudRunV2BinaryAuthorizationIn"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "client": t.string().optional(),
            "launchStage": t.string().optional(),
            "ingress": t.string().optional(),
            "template": t.proxy(renames["GoogleCloudRunV2RevisionTemplateIn"]),
            "description": t.string().optional(),
            "clientVersion": t.string().optional(),
            "traffic": t.array(
                t.proxy(renames["GoogleCloudRunV2TrafficTargetIn"])
            ).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudRunV2ServiceIn"])
    types["GoogleCloudRunV2ServiceOut"] = t.struct(
        {
            "terminalCondition": t.proxy(
                renames["GoogleCloudRunV2ConditionOut"]
            ).optional(),
            "observedGeneration": t.string().optional(),
            "latestCreatedRevision": t.string().optional(),
            "latestReadyRevision": t.string().optional(),
            "name": t.string().optional(),
            "binaryAuthorization": t.proxy(
                renames["GoogleCloudRunV2BinaryAuthorizationOut"]
            ).optional(),
            "reconciling": t.boolean().optional(),
            "uid": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "trafficStatuses": t.array(
                t.proxy(renames["GoogleCloudRunV2TrafficTargetStatusOut"])
            ).optional(),
            "client": t.string().optional(),
            "updateTime": t.string().optional(),
            "conditions": t.array(
                t.proxy(renames["GoogleCloudRunV2ConditionOut"])
            ).optional(),
            "launchStage": t.string().optional(),
            "ingress": t.string().optional(),
            "creator": t.string().optional(),
            "template": t.proxy(renames["GoogleCloudRunV2RevisionTemplateOut"]),
            "generation": t.string().optional(),
            "expireTime": t.string().optional(),
            "description": t.string().optional(),
            "lastModifier": t.string().optional(),
            "clientVersion": t.string().optional(),
            "uri": t.string().optional(),
            "etag": t.string().optional(),
            "traffic": t.array(
                t.proxy(renames["GoogleCloudRunV2TrafficTargetOut"])
            ).optional(),
            "deleteTime": t.string().optional(),
            "createTime": t.string().optional(),
            "satisfiesPzs": t.boolean().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2ServiceOut"])
    types["GoogleIamV1SetIamPolicyRequestIn"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "policy": t.proxy(renames["GoogleIamV1PolicyIn"]).optional(),
        }
    ).named(renames["GoogleIamV1SetIamPolicyRequestIn"])
    types["GoogleIamV1SetIamPolicyRequestOut"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "policy": t.proxy(renames["GoogleIamV1PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1SetIamPolicyRequestOut"])
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
    types["GoogleCloudRunV2ListTasksResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "tasks": t.array(t.proxy(renames["GoogleCloudRunV2TaskIn"])).optional(),
        }
    ).named(renames["GoogleCloudRunV2ListTasksResponseIn"])
    types["GoogleCloudRunV2ListTasksResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "tasks": t.array(t.proxy(renames["GoogleCloudRunV2TaskOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2ListTasksResponseOut"])
    types["GoogleCloudRunV2TrafficTargetIn"] = t.struct(
        {
            "percent": t.integer().optional(),
            "tag": t.string().optional(),
            "revision": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["GoogleCloudRunV2TrafficTargetIn"])
    types["GoogleCloudRunV2TrafficTargetOut"] = t.struct(
        {
            "percent": t.integer().optional(),
            "tag": t.string().optional(),
            "revision": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2TrafficTargetOut"])
    types["GoogleCloudRunV2TrafficTargetStatusIn"] = t.struct(
        {
            "revision": t.string().optional(),
            "type": t.string().optional(),
            "tag": t.string().optional(),
            "percent": t.integer().optional(),
            "uri": t.string().optional(),
        }
    ).named(renames["GoogleCloudRunV2TrafficTargetStatusIn"])
    types["GoogleCloudRunV2TrafficTargetStatusOut"] = t.struct(
        {
            "revision": t.string().optional(),
            "type": t.string().optional(),
            "tag": t.string().optional(),
            "percent": t.integer().optional(),
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2TrafficTargetStatusOut"])
    types["GoogleLongrunningWaitOperationRequestIn"] = t.struct(
        {"timeout": t.string().optional()}
    ).named(renames["GoogleLongrunningWaitOperationRequestIn"])
    types["GoogleLongrunningWaitOperationRequestOut"] = t.struct(
        {
            "timeout": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleLongrunningWaitOperationRequestOut"])
    types["GoogleCloudRunV2ListExecutionsResponseIn"] = t.struct(
        {
            "executions": t.array(
                t.proxy(renames["GoogleCloudRunV2ExecutionIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudRunV2ListExecutionsResponseIn"])
    types["GoogleCloudRunV2ListExecutionsResponseOut"] = t.struct(
        {
            "executions": t.array(
                t.proxy(renames["GoogleCloudRunV2ExecutionOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2ListExecutionsResponseOut"])
    types["GoogleCloudRunV2VpcAccessIn"] = t.struct(
        {"connector": t.string().optional(), "egress": t.string().optional()}
    ).named(renames["GoogleCloudRunV2VpcAccessIn"])
    types["GoogleCloudRunV2VpcAccessOut"] = t.struct(
        {
            "connector": t.string().optional(),
            "egress": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2VpcAccessOut"])
    types["GoogleCloudRunV2ExecutionTemplateIn"] = t.struct(
        {
            "taskCount": t.integer().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "template": t.proxy(renames["GoogleCloudRunV2TaskTemplateIn"]),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "parallelism": t.integer().optional(),
        }
    ).named(renames["GoogleCloudRunV2ExecutionTemplateIn"])
    types["GoogleCloudRunV2ExecutionTemplateOut"] = t.struct(
        {
            "taskCount": t.integer().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "template": t.proxy(renames["GoogleCloudRunV2TaskTemplateOut"]),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "parallelism": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2ExecutionTemplateOut"])
    types["GoogleIamV1AuditLogConfigIn"] = t.struct(
        {
            "exemptedMembers": t.array(t.string()).optional(),
            "logType": t.string().optional(),
        }
    ).named(renames["GoogleIamV1AuditLogConfigIn"])
    types["GoogleIamV1AuditLogConfigOut"] = t.struct(
        {
            "exemptedMembers": t.array(t.string()).optional(),
            "logType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1AuditLogConfigOut"])
    types["GoogleCloudRunV2HTTPGetActionIn"] = t.struct(
        {
            "httpHeaders": t.array(
                t.proxy(renames["GoogleCloudRunV2HTTPHeaderIn"])
            ).optional(),
            "port": t.integer().optional(),
            "path": t.string().optional(),
        }
    ).named(renames["GoogleCloudRunV2HTTPGetActionIn"])
    types["GoogleCloudRunV2HTTPGetActionOut"] = t.struct(
        {
            "httpHeaders": t.array(
                t.proxy(renames["GoogleCloudRunV2HTTPHeaderOut"])
            ).optional(),
            "port": t.integer().optional(),
            "path": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2HTTPGetActionOut"])
    types["GoogleCloudRunV2JobIn"] = t.struct(
        {
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "binaryAuthorization": t.proxy(
                renames["GoogleCloudRunV2BinaryAuthorizationIn"]
            ).optional(),
            "template": t.proxy(renames["GoogleCloudRunV2ExecutionTemplateIn"]),
            "clientVersion": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "launchStage": t.string().optional(),
            "name": t.string().optional(),
            "client": t.string().optional(),
        }
    ).named(renames["GoogleCloudRunV2JobIn"])
    types["GoogleCloudRunV2JobOut"] = t.struct(
        {
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "expireTime": t.string().optional(),
            "binaryAuthorization": t.proxy(
                renames["GoogleCloudRunV2BinaryAuthorizationOut"]
            ).optional(),
            "lastModifier": t.string().optional(),
            "uid": t.string().optional(),
            "creator": t.string().optional(),
            "executionCount": t.integer().optional(),
            "observedGeneration": t.string().optional(),
            "template": t.proxy(renames["GoogleCloudRunV2ExecutionTemplateOut"]),
            "clientVersion": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "reconciling": t.boolean().optional(),
            "createTime": t.string().optional(),
            "satisfiesPzs": t.boolean().optional(),
            "terminalCondition": t.proxy(
                renames["GoogleCloudRunV2ConditionOut"]
            ).optional(),
            "launchStage": t.string().optional(),
            "deleteTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "etag": t.string().optional(),
            "client": t.string().optional(),
            "latestCreatedExecution": t.proxy(
                renames["GoogleCloudRunV2ExecutionReferenceOut"]
            ).optional(),
            "conditions": t.array(
                t.proxy(renames["GoogleCloudRunV2ConditionOut"])
            ).optional(),
            "generation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2JobOut"])
    types["GoogleIamV1AuditConfigIn"] = t.struct(
        {
            "auditLogConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditLogConfigIn"])
            ).optional(),
            "service": t.string().optional(),
        }
    ).named(renames["GoogleIamV1AuditConfigIn"])
    types["GoogleIamV1AuditConfigOut"] = t.struct(
        {
            "auditLogConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditLogConfigOut"])
            ).optional(),
            "service": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1AuditConfigOut"])
    types["GoogleRpcStatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["GoogleRpcStatusIn"])
    types["GoogleRpcStatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleRpcStatusOut"])
    types["GoogleIamV1PolicyIn"] = t.struct(
        {
            "version": t.integer().optional(),
            "auditConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditConfigIn"])
            ).optional(),
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["GoogleIamV1BindingIn"])).optional(),
        }
    ).named(renames["GoogleIamV1PolicyIn"])
    types["GoogleIamV1PolicyOut"] = t.struct(
        {
            "version": t.integer().optional(),
            "auditConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditConfigOut"])
            ).optional(),
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["GoogleIamV1BindingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1PolicyOut"])
    types["GoogleCloudRunV2TCPSocketActionIn"] = t.struct(
        {"port": t.integer().optional()}
    ).named(renames["GoogleCloudRunV2TCPSocketActionIn"])
    types["GoogleCloudRunV2TCPSocketActionOut"] = t.struct(
        {
            "port": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2TCPSocketActionOut"])
    types["GoogleCloudRunV2HTTPHeaderIn"] = t.struct(
        {"value": t.string().optional(), "name": t.string()}
    ).named(renames["GoogleCloudRunV2HTTPHeaderIn"])
    types["GoogleCloudRunV2HTTPHeaderOut"] = t.struct(
        {
            "value": t.string().optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2HTTPHeaderOut"])
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
    types["GoogleCloudRunV2ListRevisionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "revisions": t.array(
                t.proxy(renames["GoogleCloudRunV2RevisionIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudRunV2ListRevisionsResponseIn"])
    types["GoogleCloudRunV2ListRevisionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "revisions": t.array(
                t.proxy(renames["GoogleCloudRunV2RevisionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2ListRevisionsResponseOut"])
    types["GoogleCloudRunV2RevisionScalingIn"] = t.struct(
        {
            "maxInstanceCount": t.integer().optional(),
            "minInstanceCount": t.integer().optional(),
        }
    ).named(renames["GoogleCloudRunV2RevisionScalingIn"])
    types["GoogleCloudRunV2RevisionScalingOut"] = t.struct(
        {
            "maxInstanceCount": t.integer().optional(),
            "minInstanceCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2RevisionScalingOut"])
    types["GoogleCloudRunV2TaskIn"] = t.struct(
        {
            "maxRetries": t.integer().optional(),
            "timeout": t.string().optional(),
            "executionEnvironment": t.string().optional(),
            "volumes": t.array(t.proxy(renames["GoogleCloudRunV2VolumeIn"])).optional(),
            "serviceAccount": t.string().optional(),
            "containers": t.array(
                t.proxy(renames["GoogleCloudRunV2ContainerIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudRunV2TaskIn"])
    types["GoogleCloudRunV2TaskOut"] = t.struct(
        {
            "maxRetries": t.integer().optional(),
            "retried": t.integer().optional(),
            "etag": t.string().optional(),
            "job": t.string().optional(),
            "timeout": t.string().optional(),
            "conditions": t.array(
                t.proxy(renames["GoogleCloudRunV2ConditionOut"])
            ).optional(),
            "satisfiesPzs": t.boolean().optional(),
            "encryptionKey": t.string().optional(),
            "executionEnvironment": t.string().optional(),
            "generation": t.string().optional(),
            "execution": t.string().optional(),
            "expireTime": t.string().optional(),
            "vpcAccess": t.proxy(renames["GoogleCloudRunV2VpcAccessOut"]).optional(),
            "volumes": t.array(
                t.proxy(renames["GoogleCloudRunV2VolumeOut"])
            ).optional(),
            "lastAttemptResult": t.proxy(
                renames["GoogleCloudRunV2TaskAttemptResultOut"]
            ).optional(),
            "name": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "observedGeneration": t.string().optional(),
            "index": t.integer().optional(),
            "updateTime": t.string().optional(),
            "reconciling": t.boolean().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "uid": t.string().optional(),
            "containers": t.array(
                t.proxy(renames["GoogleCloudRunV2ContainerOut"])
            ).optional(),
            "deleteTime": t.string().optional(),
            "createTime": t.string().optional(),
            "startTime": t.string().optional(),
            "completionTime": t.string().optional(),
            "logUri": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2TaskOut"])
    types["GoogleCloudRunV2ListJobsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "jobs": t.array(t.proxy(renames["GoogleCloudRunV2JobIn"])).optional(),
        }
    ).named(renames["GoogleCloudRunV2ListJobsResponseIn"])
    types["GoogleCloudRunV2ListJobsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "jobs": t.array(t.proxy(renames["GoogleCloudRunV2JobOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2ListJobsResponseOut"])
    types["GoogleCloudRunV2ProbeIn"] = t.struct(
        {
            "tcpSocket": t.proxy(
                renames["GoogleCloudRunV2TCPSocketActionIn"]
            ).optional(),
            "timeoutSeconds": t.integer().optional(),
            "periodSeconds": t.integer().optional(),
            "failureThreshold": t.integer().optional(),
            "httpGet": t.proxy(renames["GoogleCloudRunV2HTTPGetActionIn"]).optional(),
            "initialDelaySeconds": t.integer().optional(),
            "grpc": t.proxy(renames["GoogleCloudRunV2GRPCActionIn"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2ProbeIn"])
    types["GoogleCloudRunV2ProbeOut"] = t.struct(
        {
            "tcpSocket": t.proxy(
                renames["GoogleCloudRunV2TCPSocketActionOut"]
            ).optional(),
            "timeoutSeconds": t.integer().optional(),
            "periodSeconds": t.integer().optional(),
            "failureThreshold": t.integer().optional(),
            "httpGet": t.proxy(renames["GoogleCloudRunV2HTTPGetActionOut"]).optional(),
            "initialDelaySeconds": t.integer().optional(),
            "grpc": t.proxy(renames["GoogleCloudRunV2GRPCActionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2ProbeOut"])
    types["GoogleCloudRunV2RevisionTemplateIn"] = t.struct(
        {
            "timeout": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "scaling": t.proxy(renames["GoogleCloudRunV2RevisionScalingIn"]).optional(),
            "sessionAffinity": t.boolean().optional(),
            "executionEnvironment": t.string().optional(),
            "vpcAccess": t.proxy(renames["GoogleCloudRunV2VpcAccessIn"]).optional(),
            "volumes": t.array(t.proxy(renames["GoogleCloudRunV2VolumeIn"])).optional(),
            "containers": t.array(
                t.proxy(renames["GoogleCloudRunV2ContainerIn"])
            ).optional(),
            "revision": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "encryptionKey": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "maxInstanceRequestConcurrency": t.integer().optional(),
        }
    ).named(renames["GoogleCloudRunV2RevisionTemplateIn"])
    types["GoogleCloudRunV2RevisionTemplateOut"] = t.struct(
        {
            "timeout": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "scaling": t.proxy(
                renames["GoogleCloudRunV2RevisionScalingOut"]
            ).optional(),
            "sessionAffinity": t.boolean().optional(),
            "executionEnvironment": t.string().optional(),
            "vpcAccess": t.proxy(renames["GoogleCloudRunV2VpcAccessOut"]).optional(),
            "volumes": t.array(
                t.proxy(renames["GoogleCloudRunV2VolumeOut"])
            ).optional(),
            "containers": t.array(
                t.proxy(renames["GoogleCloudRunV2ContainerOut"])
            ).optional(),
            "revision": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "encryptionKey": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "maxInstanceRequestConcurrency": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2RevisionTemplateOut"])
    types["GoogleCloudRunV2RevisionIn"] = t.struct(
        {
            "maxInstanceRequestConcurrency": t.integer().optional(),
            "encryptionKeyRevocationAction": t.string().optional(),
            "scaling": t.proxy(renames["GoogleCloudRunV2RevisionScalingIn"]).optional(),
            "serviceAccount": t.string().optional(),
            "volumes": t.array(t.proxy(renames["GoogleCloudRunV2VolumeIn"])).optional(),
            "encryptionKey": t.string().optional(),
            "encryptionKeyShutdownDuration": t.string().optional(),
            "launchStage": t.string().optional(),
            "sessionAffinity": t.boolean().optional(),
            "timeout": t.string().optional(),
            "executionEnvironment": t.string().optional(),
            "vpcAccess": t.proxy(renames["GoogleCloudRunV2VpcAccessIn"]).optional(),
            "containers": t.array(
                t.proxy(renames["GoogleCloudRunV2ContainerIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudRunV2RevisionIn"])
    types["GoogleCloudRunV2RevisionOut"] = t.struct(
        {
            "maxInstanceRequestConcurrency": t.integer().optional(),
            "name": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "encryptionKeyRevocationAction": t.string().optional(),
            "scaling": t.proxy(
                renames["GoogleCloudRunV2RevisionScalingOut"]
            ).optional(),
            "expireTime": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "volumes": t.array(
                t.proxy(renames["GoogleCloudRunV2VolumeOut"])
            ).optional(),
            "createTime": t.string().optional(),
            "reconciling": t.boolean().optional(),
            "encryptionKey": t.string().optional(),
            "observedGeneration": t.string().optional(),
            "generation": t.string().optional(),
            "encryptionKeyShutdownDuration": t.string().optional(),
            "launchStage": t.string().optional(),
            "sessionAffinity": t.boolean().optional(),
            "deleteTime": t.string().optional(),
            "logUri": t.string().optional(),
            "satisfiesPzs": t.boolean().optional(),
            "conditions": t.array(
                t.proxy(renames["GoogleCloudRunV2ConditionOut"])
            ).optional(),
            "timeout": t.string().optional(),
            "service": t.string().optional(),
            "updateTime": t.string().optional(),
            "etag": t.string().optional(),
            "uid": t.string().optional(),
            "executionEnvironment": t.string().optional(),
            "vpcAccess": t.proxy(renames["GoogleCloudRunV2VpcAccessOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "containers": t.array(
                t.proxy(renames["GoogleCloudRunV2ContainerOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2RevisionOut"])
    types["GoogleCloudRunV2TaskAttemptResultIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRunV2TaskAttemptResultIn"])
    types["GoogleCloudRunV2TaskAttemptResultOut"] = t.struct(
        {
            "exitCode": t.integer().optional(),
            "status": t.proxy(renames["GoogleRpcStatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2TaskAttemptResultOut"])
    types["GoogleIamV1TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["GoogleIamV1TestIamPermissionsRequestIn"])
    types["GoogleIamV1TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1TestIamPermissionsRequestOut"])
    types["GoogleCloudRunV2TaskTemplateIn"] = t.struct(
        {
            "serviceAccount": t.string().optional(),
            "timeout": t.string().optional(),
            "executionEnvironment": t.string().optional(),
            "encryptionKey": t.string().optional(),
            "vpcAccess": t.proxy(renames["GoogleCloudRunV2VpcAccessIn"]).optional(),
            "maxRetries": t.integer().optional(),
            "volumes": t.array(t.proxy(renames["GoogleCloudRunV2VolumeIn"])).optional(),
            "containers": t.array(
                t.proxy(renames["GoogleCloudRunV2ContainerIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudRunV2TaskTemplateIn"])
    types["GoogleCloudRunV2TaskTemplateOut"] = t.struct(
        {
            "serviceAccount": t.string().optional(),
            "timeout": t.string().optional(),
            "executionEnvironment": t.string().optional(),
            "encryptionKey": t.string().optional(),
            "vpcAccess": t.proxy(renames["GoogleCloudRunV2VpcAccessOut"]).optional(),
            "maxRetries": t.integer().optional(),
            "volumes": t.array(
                t.proxy(renames["GoogleCloudRunV2VolumeOut"])
            ).optional(),
            "containers": t.array(
                t.proxy(renames["GoogleCloudRunV2ContainerOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2TaskTemplateOut"])
    types["GoogleLongrunningListOperationsResponseIn"] = t.struct(
        {
            "operations": t.array(
                t.proxy(renames["GoogleLongrunningOperationIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleLongrunningListOperationsResponseIn"])
    types["GoogleLongrunningListOperationsResponseOut"] = t.struct(
        {
            "operations": t.array(
                t.proxy(renames["GoogleLongrunningOperationOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleLongrunningListOperationsResponseOut"])
    types["GoogleCloudRunV2RunJobRequestIn"] = t.struct(
        {"etag": t.string().optional(), "validateOnly": t.boolean().optional()}
    ).named(renames["GoogleCloudRunV2RunJobRequestIn"])
    types["GoogleCloudRunV2RunJobRequestOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "validateOnly": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2RunJobRequestOut"])
    types["GoogleCloudRunV2ExecutionIn"] = t.struct(
        {"launchStage": t.string().optional()}
    ).named(renames["GoogleCloudRunV2ExecutionIn"])
    types["GoogleCloudRunV2ExecutionOut"] = t.struct(
        {
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "observedGeneration": t.string().optional(),
            "launchStage": t.string().optional(),
            "runningCount": t.integer().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "conditions": t.array(
                t.proxy(renames["GoogleCloudRunV2ConditionOut"])
            ).optional(),
            "satisfiesPzs": t.boolean().optional(),
            "parallelism": t.integer().optional(),
            "job": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "deleteTime": t.string().optional(),
            "startTime": t.string().optional(),
            "completionTime": t.string().optional(),
            "retriedCount": t.integer().optional(),
            "reconciling": t.boolean().optional(),
            "succeededCount": t.integer().optional(),
            "expireTime": t.string().optional(),
            "uid": t.string().optional(),
            "failedCount": t.integer().optional(),
            "template": t.proxy(renames["GoogleCloudRunV2TaskTemplateOut"]).optional(),
            "updateTime": t.string().optional(),
            "generation": t.string().optional(),
            "cancelledCount": t.integer().optional(),
            "logUri": t.string().optional(),
            "taskCount": t.integer().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2ExecutionOut"])
    types["GoogleCloudRunV2SecretVolumeSourceIn"] = t.struct(
        {
            "items": t.array(
                t.proxy(renames["GoogleCloudRunV2VersionToPathIn"])
            ).optional(),
            "secret": t.string(),
            "defaultMode": t.integer().optional(),
        }
    ).named(renames["GoogleCloudRunV2SecretVolumeSourceIn"])
    types["GoogleCloudRunV2SecretVolumeSourceOut"] = t.struct(
        {
            "items": t.array(
                t.proxy(renames["GoogleCloudRunV2VersionToPathOut"])
            ).optional(),
            "secret": t.string(),
            "defaultMode": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2SecretVolumeSourceOut"])
    types["GoogleIamV1TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["GoogleIamV1TestIamPermissionsResponseIn"])
    types["GoogleIamV1TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1TestIamPermissionsResponseOut"])
    types["GoogleCloudRunV2ContainerIn"] = t.struct(
        {
            "args": t.array(t.string()).optional(),
            "command": t.array(t.string()).optional(),
            "startupProbe": t.proxy(renames["GoogleCloudRunV2ProbeIn"]).optional(),
            "workingDir": t.string().optional(),
            "dependsOn": t.array(t.string()).optional(),
            "volumeMounts": t.array(
                t.proxy(renames["GoogleCloudRunV2VolumeMountIn"])
            ).optional(),
            "livenessProbe": t.proxy(renames["GoogleCloudRunV2ProbeIn"]).optional(),
            "name": t.string().optional(),
            "ports": t.array(
                t.proxy(renames["GoogleCloudRunV2ContainerPortIn"])
            ).optional(),
            "resources": t.proxy(
                renames["GoogleCloudRunV2ResourceRequirementsIn"]
            ).optional(),
            "image": t.string(),
            "env": t.array(t.proxy(renames["GoogleCloudRunV2EnvVarIn"])).optional(),
        }
    ).named(renames["GoogleCloudRunV2ContainerIn"])
    types["GoogleCloudRunV2ContainerOut"] = t.struct(
        {
            "args": t.array(t.string()).optional(),
            "command": t.array(t.string()).optional(),
            "startupProbe": t.proxy(renames["GoogleCloudRunV2ProbeOut"]).optional(),
            "workingDir": t.string().optional(),
            "dependsOn": t.array(t.string()).optional(),
            "volumeMounts": t.array(
                t.proxy(renames["GoogleCloudRunV2VolumeMountOut"])
            ).optional(),
            "livenessProbe": t.proxy(renames["GoogleCloudRunV2ProbeOut"]).optional(),
            "name": t.string().optional(),
            "ports": t.array(
                t.proxy(renames["GoogleCloudRunV2ContainerPortOut"])
            ).optional(),
            "resources": t.proxy(
                renames["GoogleCloudRunV2ResourceRequirementsOut"]
            ).optional(),
            "image": t.string(),
            "env": t.array(t.proxy(renames["GoogleCloudRunV2EnvVarOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2ContainerOut"])
    types["GoogleCloudRunV2ExecutionReferenceIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "completionTime": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudRunV2ExecutionReferenceIn"])
    types["GoogleCloudRunV2ExecutionReferenceOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "completionTime": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2ExecutionReferenceOut"])
    types["GoogleTypeExprIn"] = t.struct(
        {
            "description": t.string().optional(),
            "title": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
        }
    ).named(renames["GoogleTypeExprIn"])
    types["GoogleTypeExprOut"] = t.struct(
        {
            "description": t.string().optional(),
            "title": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeExprOut"])
    types["GoogleCloudRunV2ContainerPortIn"] = t.struct(
        {"name": t.string().optional(), "containerPort": t.integer().optional()}
    ).named(renames["GoogleCloudRunV2ContainerPortIn"])
    types["GoogleCloudRunV2ContainerPortOut"] = t.struct(
        {
            "name": t.string().optional(),
            "containerPort": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2ContainerPortOut"])
    types["GoogleCloudRunV2BinaryAuthorizationIn"] = t.struct(
        {
            "breakglassJustification": t.string().optional(),
            "useDefault": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudRunV2BinaryAuthorizationIn"])
    types["GoogleCloudRunV2BinaryAuthorizationOut"] = t.struct(
        {
            "breakglassJustification": t.string().optional(),
            "useDefault": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2BinaryAuthorizationOut"])
    types["GoogleCloudRunV2EmptyDirVolumeSourceIn"] = t.struct(
        {"medium": t.string().optional(), "sizeLimit": t.string().optional()}
    ).named(renames["GoogleCloudRunV2EmptyDirVolumeSourceIn"])
    types["GoogleCloudRunV2EmptyDirVolumeSourceOut"] = t.struct(
        {
            "medium": t.string().optional(),
            "sizeLimit": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2EmptyDirVolumeSourceOut"])

    functions = {}
    functions["projectsLocationsOperationsWait"] = run.get(
        "v2/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = run.get(
        "v2/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = run.get(
        "v2/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = run.get(
        "v2/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsPatch"] = run.get(
        "v2/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsDelete"] = run.get(
        "v2/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsRun"] = run.get(
        "v2/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsTestIamPermissions"] = run.get(
        "v2/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsGet"] = run.get(
        "v2/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsList"] = run.get(
        "v2/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsSetIamPolicy"] = run.get(
        "v2/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsCreate"] = run.get(
        "v2/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsGetIamPolicy"] = run.get(
        "v2/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsExecutionsList"] = run.delete(
        "v2/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsExecutionsGet"] = run.delete(
        "v2/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsExecutionsDelete"] = run.delete(
        "v2/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsExecutionsTasksList"] = run.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRunV2TaskOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsExecutionsTasksGet"] = run.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRunV2TaskOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesGetIamPolicy"] = run.post(
        "v2/{parent}/services",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "serviceId": t.string(),
                "parent": t.string(),
                "name": t.string().optional(),
                "binaryAuthorization": t.proxy(
                    renames["GoogleCloudRunV2BinaryAuthorizationIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "client": t.string().optional(),
                "launchStage": t.string().optional(),
                "ingress": t.string().optional(),
                "template": t.proxy(renames["GoogleCloudRunV2RevisionTemplateIn"]),
                "description": t.string().optional(),
                "clientVersion": t.string().optional(),
                "traffic": t.array(
                    t.proxy(renames["GoogleCloudRunV2TrafficTargetIn"])
                ).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesDelete"] = run.post(
        "v2/{parent}/services",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "serviceId": t.string(),
                "parent": t.string(),
                "name": t.string().optional(),
                "binaryAuthorization": t.proxy(
                    renames["GoogleCloudRunV2BinaryAuthorizationIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "client": t.string().optional(),
                "launchStage": t.string().optional(),
                "ingress": t.string().optional(),
                "template": t.proxy(renames["GoogleCloudRunV2RevisionTemplateIn"]),
                "description": t.string().optional(),
                "clientVersion": t.string().optional(),
                "traffic": t.array(
                    t.proxy(renames["GoogleCloudRunV2TrafficTargetIn"])
                ).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesTestIamPermissions"] = run.post(
        "v2/{parent}/services",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "serviceId": t.string(),
                "parent": t.string(),
                "name": t.string().optional(),
                "binaryAuthorization": t.proxy(
                    renames["GoogleCloudRunV2BinaryAuthorizationIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "client": t.string().optional(),
                "launchStage": t.string().optional(),
                "ingress": t.string().optional(),
                "template": t.proxy(renames["GoogleCloudRunV2RevisionTemplateIn"]),
                "description": t.string().optional(),
                "clientVersion": t.string().optional(),
                "traffic": t.array(
                    t.proxy(renames["GoogleCloudRunV2TrafficTargetIn"])
                ).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesGet"] = run.post(
        "v2/{parent}/services",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "serviceId": t.string(),
                "parent": t.string(),
                "name": t.string().optional(),
                "binaryAuthorization": t.proxy(
                    renames["GoogleCloudRunV2BinaryAuthorizationIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "client": t.string().optional(),
                "launchStage": t.string().optional(),
                "ingress": t.string().optional(),
                "template": t.proxy(renames["GoogleCloudRunV2RevisionTemplateIn"]),
                "description": t.string().optional(),
                "clientVersion": t.string().optional(),
                "traffic": t.array(
                    t.proxy(renames["GoogleCloudRunV2TrafficTargetIn"])
                ).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesPatch"] = run.post(
        "v2/{parent}/services",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "serviceId": t.string(),
                "parent": t.string(),
                "name": t.string().optional(),
                "binaryAuthorization": t.proxy(
                    renames["GoogleCloudRunV2BinaryAuthorizationIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "client": t.string().optional(),
                "launchStage": t.string().optional(),
                "ingress": t.string().optional(),
                "template": t.proxy(renames["GoogleCloudRunV2RevisionTemplateIn"]),
                "description": t.string().optional(),
                "clientVersion": t.string().optional(),
                "traffic": t.array(
                    t.proxy(renames["GoogleCloudRunV2TrafficTargetIn"])
                ).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesSetIamPolicy"] = run.post(
        "v2/{parent}/services",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "serviceId": t.string(),
                "parent": t.string(),
                "name": t.string().optional(),
                "binaryAuthorization": t.proxy(
                    renames["GoogleCloudRunV2BinaryAuthorizationIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "client": t.string().optional(),
                "launchStage": t.string().optional(),
                "ingress": t.string().optional(),
                "template": t.proxy(renames["GoogleCloudRunV2RevisionTemplateIn"]),
                "description": t.string().optional(),
                "clientVersion": t.string().optional(),
                "traffic": t.array(
                    t.proxy(renames["GoogleCloudRunV2TrafficTargetIn"])
                ).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesList"] = run.post(
        "v2/{parent}/services",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "serviceId": t.string(),
                "parent": t.string(),
                "name": t.string().optional(),
                "binaryAuthorization": t.proxy(
                    renames["GoogleCloudRunV2BinaryAuthorizationIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "client": t.string().optional(),
                "launchStage": t.string().optional(),
                "ingress": t.string().optional(),
                "template": t.proxy(renames["GoogleCloudRunV2RevisionTemplateIn"]),
                "description": t.string().optional(),
                "clientVersion": t.string().optional(),
                "traffic": t.array(
                    t.proxy(renames["GoogleCloudRunV2TrafficTargetIn"])
                ).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesCreate"] = run.post(
        "v2/{parent}/services",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "serviceId": t.string(),
                "parent": t.string(),
                "name": t.string().optional(),
                "binaryAuthorization": t.proxy(
                    renames["GoogleCloudRunV2BinaryAuthorizationIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "client": t.string().optional(),
                "launchStage": t.string().optional(),
                "ingress": t.string().optional(),
                "template": t.proxy(renames["GoogleCloudRunV2RevisionTemplateIn"]),
                "description": t.string().optional(),
                "clientVersion": t.string().optional(),
                "traffic": t.array(
                    t.proxy(renames["GoogleCloudRunV2TrafficTargetIn"])
                ).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesRevisionsGet"] = run.get(
        "v2/{parent}/revisions",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "showDeleted": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRunV2ListRevisionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesRevisionsDelete"] = run.get(
        "v2/{parent}/revisions",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "showDeleted": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRunV2ListRevisionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesRevisionsList"] = run.get(
        "v2/{parent}/revisions",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "showDeleted": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRunV2ListRevisionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="run", renames=renames, types=Box(types), functions=Box(functions)
    )
