from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_run() -> Import:
    run = HTTPRuntime("https://run.googleapis.com/")

    renames = {
        "ErrorResponse": "_run_1_ErrorResponse",
        "GoogleCloudRunV2RunJobRequestIn": "_run_2_GoogleCloudRunV2RunJobRequestIn",
        "GoogleCloudRunV2RunJobRequestOut": "_run_3_GoogleCloudRunV2RunJobRequestOut",
        "GoogleCloudRunV2ListServicesResponseIn": "_run_4_GoogleCloudRunV2ListServicesResponseIn",
        "GoogleCloudRunV2ListServicesResponseOut": "_run_5_GoogleCloudRunV2ListServicesResponseOut",
        "GoogleCloudRunV2SecretVolumeSourceIn": "_run_6_GoogleCloudRunV2SecretVolumeSourceIn",
        "GoogleCloudRunV2SecretVolumeSourceOut": "_run_7_GoogleCloudRunV2SecretVolumeSourceOut",
        "GoogleIamV1TestIamPermissionsRequestIn": "_run_8_GoogleIamV1TestIamPermissionsRequestIn",
        "GoogleIamV1TestIamPermissionsRequestOut": "_run_9_GoogleIamV1TestIamPermissionsRequestOut",
        "GoogleCloudRunV2ExecutionIn": "_run_10_GoogleCloudRunV2ExecutionIn",
        "GoogleCloudRunV2ExecutionOut": "_run_11_GoogleCloudRunV2ExecutionOut",
        "GoogleCloudRunV2ServiceIn": "_run_12_GoogleCloudRunV2ServiceIn",
        "GoogleCloudRunV2ServiceOut": "_run_13_GoogleCloudRunV2ServiceOut",
        "GoogleCloudRunV2CloudSqlInstanceIn": "_run_14_GoogleCloudRunV2CloudSqlInstanceIn",
        "GoogleCloudRunV2CloudSqlInstanceOut": "_run_15_GoogleCloudRunV2CloudSqlInstanceOut",
        "GoogleCloudRunV2EmptyDirVolumeSourceIn": "_run_16_GoogleCloudRunV2EmptyDirVolumeSourceIn",
        "GoogleCloudRunV2EmptyDirVolumeSourceOut": "_run_17_GoogleCloudRunV2EmptyDirVolumeSourceOut",
        "GoogleCloudRunV2ListJobsResponseIn": "_run_18_GoogleCloudRunV2ListJobsResponseIn",
        "GoogleCloudRunV2ListJobsResponseOut": "_run_19_GoogleCloudRunV2ListJobsResponseOut",
        "GoogleCloudRunV2ContainerPortIn": "_run_20_GoogleCloudRunV2ContainerPortIn",
        "GoogleCloudRunV2ContainerPortOut": "_run_21_GoogleCloudRunV2ContainerPortOut",
        "GoogleCloudRunV2ListExecutionsResponseIn": "_run_22_GoogleCloudRunV2ListExecutionsResponseIn",
        "GoogleCloudRunV2ListExecutionsResponseOut": "_run_23_GoogleCloudRunV2ListExecutionsResponseOut",
        "GoogleCloudRunV2RevisionScalingIn": "_run_24_GoogleCloudRunV2RevisionScalingIn",
        "GoogleCloudRunV2RevisionScalingOut": "_run_25_GoogleCloudRunV2RevisionScalingOut",
        "GoogleIamV1BindingIn": "_run_26_GoogleIamV1BindingIn",
        "GoogleIamV1BindingOut": "_run_27_GoogleIamV1BindingOut",
        "GoogleCloudRunV2TaskIn": "_run_28_GoogleCloudRunV2TaskIn",
        "GoogleCloudRunV2TaskOut": "_run_29_GoogleCloudRunV2TaskOut",
        "GoogleCloudRunV2VpcAccessIn": "_run_30_GoogleCloudRunV2VpcAccessIn",
        "GoogleCloudRunV2VpcAccessOut": "_run_31_GoogleCloudRunV2VpcAccessOut",
        "GoogleCloudRunV2TCPSocketActionIn": "_run_32_GoogleCloudRunV2TCPSocketActionIn",
        "GoogleCloudRunV2TCPSocketActionOut": "_run_33_GoogleCloudRunV2TCPSocketActionOut",
        "GoogleCloudRunV2TrafficTargetStatusIn": "_run_34_GoogleCloudRunV2TrafficTargetStatusIn",
        "GoogleCloudRunV2TrafficTargetStatusOut": "_run_35_GoogleCloudRunV2TrafficTargetStatusOut",
        "GoogleCloudRunV2BinaryAuthorizationIn": "_run_36_GoogleCloudRunV2BinaryAuthorizationIn",
        "GoogleCloudRunV2BinaryAuthorizationOut": "_run_37_GoogleCloudRunV2BinaryAuthorizationOut",
        "GoogleCloudRunV2RevisionTemplateIn": "_run_38_GoogleCloudRunV2RevisionTemplateIn",
        "GoogleCloudRunV2RevisionTemplateOut": "_run_39_GoogleCloudRunV2RevisionTemplateOut",
        "GoogleCloudRunV2JobIn": "_run_40_GoogleCloudRunV2JobIn",
        "GoogleCloudRunV2JobOut": "_run_41_GoogleCloudRunV2JobOut",
        "GoogleCloudRunV2ConditionIn": "_run_42_GoogleCloudRunV2ConditionIn",
        "GoogleCloudRunV2ConditionOut": "_run_43_GoogleCloudRunV2ConditionOut",
        "GoogleCloudRunV2HTTPGetActionIn": "_run_44_GoogleCloudRunV2HTTPGetActionIn",
        "GoogleCloudRunV2HTTPGetActionOut": "_run_45_GoogleCloudRunV2HTTPGetActionOut",
        "GoogleCloudRunV2ResourceRequirementsIn": "_run_46_GoogleCloudRunV2ResourceRequirementsIn",
        "GoogleCloudRunV2ResourceRequirementsOut": "_run_47_GoogleCloudRunV2ResourceRequirementsOut",
        "GoogleCloudRunV2EnvVarSourceIn": "_run_48_GoogleCloudRunV2EnvVarSourceIn",
        "GoogleCloudRunV2EnvVarSourceOut": "_run_49_GoogleCloudRunV2EnvVarSourceOut",
        "GoogleIamV1TestIamPermissionsResponseIn": "_run_50_GoogleIamV1TestIamPermissionsResponseIn",
        "GoogleIamV1TestIamPermissionsResponseOut": "_run_51_GoogleIamV1TestIamPermissionsResponseOut",
        "GoogleCloudRunV2ListRevisionsResponseIn": "_run_52_GoogleCloudRunV2ListRevisionsResponseIn",
        "GoogleCloudRunV2ListRevisionsResponseOut": "_run_53_GoogleCloudRunV2ListRevisionsResponseOut",
        "GoogleTypeExprIn": "_run_54_GoogleTypeExprIn",
        "GoogleTypeExprOut": "_run_55_GoogleTypeExprOut",
        "GoogleCloudRunV2EnvVarIn": "_run_56_GoogleCloudRunV2EnvVarIn",
        "GoogleCloudRunV2EnvVarOut": "_run_57_GoogleCloudRunV2EnvVarOut",
        "GoogleCloudRunV2ListTasksResponseIn": "_run_58_GoogleCloudRunV2ListTasksResponseIn",
        "GoogleCloudRunV2ListTasksResponseOut": "_run_59_GoogleCloudRunV2ListTasksResponseOut",
        "GoogleProtobufEmptyIn": "_run_60_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_run_61_GoogleProtobufEmptyOut",
        "GoogleCloudRunV2ExecutionTemplateIn": "_run_62_GoogleCloudRunV2ExecutionTemplateIn",
        "GoogleCloudRunV2ExecutionTemplateOut": "_run_63_GoogleCloudRunV2ExecutionTemplateOut",
        "GoogleIamV1SetIamPolicyRequestIn": "_run_64_GoogleIamV1SetIamPolicyRequestIn",
        "GoogleIamV1SetIamPolicyRequestOut": "_run_65_GoogleIamV1SetIamPolicyRequestOut",
        "GoogleRpcStatusIn": "_run_66_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_run_67_GoogleRpcStatusOut",
        "GoogleCloudRunV2SecretKeySelectorIn": "_run_68_GoogleCloudRunV2SecretKeySelectorIn",
        "GoogleCloudRunV2SecretKeySelectorOut": "_run_69_GoogleCloudRunV2SecretKeySelectorOut",
        "GoogleCloudRunV2TaskTemplateIn": "_run_70_GoogleCloudRunV2TaskTemplateIn",
        "GoogleCloudRunV2TaskTemplateOut": "_run_71_GoogleCloudRunV2TaskTemplateOut",
        "GoogleCloudRunV2VersionToPathIn": "_run_72_GoogleCloudRunV2VersionToPathIn",
        "GoogleCloudRunV2VersionToPathOut": "_run_73_GoogleCloudRunV2VersionToPathOut",
        "GoogleLongrunningListOperationsResponseIn": "_run_74_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_run_75_GoogleLongrunningListOperationsResponseOut",
        "GoogleCloudRunV2RevisionIn": "_run_76_GoogleCloudRunV2RevisionIn",
        "GoogleCloudRunV2RevisionOut": "_run_77_GoogleCloudRunV2RevisionOut",
        "GoogleCloudRunV2VolumeMountIn": "_run_78_GoogleCloudRunV2VolumeMountIn",
        "GoogleCloudRunV2VolumeMountOut": "_run_79_GoogleCloudRunV2VolumeMountOut",
        "GoogleLongrunningOperationIn": "_run_80_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_run_81_GoogleLongrunningOperationOut",
        "GoogleIamV1PolicyIn": "_run_82_GoogleIamV1PolicyIn",
        "GoogleIamV1PolicyOut": "_run_83_GoogleIamV1PolicyOut",
        "GoogleCloudRunV2TrafficTargetIn": "_run_84_GoogleCloudRunV2TrafficTargetIn",
        "GoogleCloudRunV2TrafficTargetOut": "_run_85_GoogleCloudRunV2TrafficTargetOut",
        "GoogleCloudRunV2GRPCActionIn": "_run_86_GoogleCloudRunV2GRPCActionIn",
        "GoogleCloudRunV2GRPCActionOut": "_run_87_GoogleCloudRunV2GRPCActionOut",
        "GoogleCloudRunV2ExecutionReferenceIn": "_run_88_GoogleCloudRunV2ExecutionReferenceIn",
        "GoogleCloudRunV2ExecutionReferenceOut": "_run_89_GoogleCloudRunV2ExecutionReferenceOut",
        "GoogleCloudRunV2ContainerIn": "_run_90_GoogleCloudRunV2ContainerIn",
        "GoogleCloudRunV2ContainerOut": "_run_91_GoogleCloudRunV2ContainerOut",
        "GoogleIamV1AuditConfigIn": "_run_92_GoogleIamV1AuditConfigIn",
        "GoogleIamV1AuditConfigOut": "_run_93_GoogleIamV1AuditConfigOut",
        "GoogleLongrunningWaitOperationRequestIn": "_run_94_GoogleLongrunningWaitOperationRequestIn",
        "GoogleLongrunningWaitOperationRequestOut": "_run_95_GoogleLongrunningWaitOperationRequestOut",
        "GoogleCloudRunV2HTTPHeaderIn": "_run_96_GoogleCloudRunV2HTTPHeaderIn",
        "GoogleCloudRunV2HTTPHeaderOut": "_run_97_GoogleCloudRunV2HTTPHeaderOut",
        "GoogleCloudRunV2TaskAttemptResultIn": "_run_98_GoogleCloudRunV2TaskAttemptResultIn",
        "GoogleCloudRunV2TaskAttemptResultOut": "_run_99_GoogleCloudRunV2TaskAttemptResultOut",
        "GoogleCloudRunV2ProbeIn": "_run_100_GoogleCloudRunV2ProbeIn",
        "GoogleCloudRunV2ProbeOut": "_run_101_GoogleCloudRunV2ProbeOut",
        "GoogleIamV1AuditLogConfigIn": "_run_102_GoogleIamV1AuditLogConfigIn",
        "GoogleIamV1AuditLogConfigOut": "_run_103_GoogleIamV1AuditLogConfigOut",
        "GoogleCloudRunV2VolumeIn": "_run_104_GoogleCloudRunV2VolumeIn",
        "GoogleCloudRunV2VolumeOut": "_run_105_GoogleCloudRunV2VolumeOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudRunV2RunJobRequestIn"] = t.struct(
        {"validateOnly": t.boolean().optional(), "etag": t.string().optional()}
    ).named(renames["GoogleCloudRunV2RunJobRequestIn"])
    types["GoogleCloudRunV2RunJobRequestOut"] = t.struct(
        {
            "validateOnly": t.boolean().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2RunJobRequestOut"])
    types["GoogleCloudRunV2ListServicesResponseIn"] = t.struct(
        {
            "services": t.array(
                t.proxy(renames["GoogleCloudRunV2ServiceIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudRunV2ListServicesResponseIn"])
    types["GoogleCloudRunV2ListServicesResponseOut"] = t.struct(
        {
            "services": t.array(
                t.proxy(renames["GoogleCloudRunV2ServiceOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2ListServicesResponseOut"])
    types["GoogleCloudRunV2SecretVolumeSourceIn"] = t.struct(
        {
            "secret": t.string(),
            "defaultMode": t.integer().optional(),
            "items": t.array(
                t.proxy(renames["GoogleCloudRunV2VersionToPathIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudRunV2SecretVolumeSourceIn"])
    types["GoogleCloudRunV2SecretVolumeSourceOut"] = t.struct(
        {
            "secret": t.string(),
            "defaultMode": t.integer().optional(),
            "items": t.array(
                t.proxy(renames["GoogleCloudRunV2VersionToPathOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2SecretVolumeSourceOut"])
    types["GoogleIamV1TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["GoogleIamV1TestIamPermissionsRequestIn"])
    types["GoogleIamV1TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1TestIamPermissionsRequestOut"])
    types["GoogleCloudRunV2ExecutionIn"] = t.struct(
        {"launchStage": t.string().optional()}
    ).named(renames["GoogleCloudRunV2ExecutionIn"])
    types["GoogleCloudRunV2ExecutionOut"] = t.struct(
        {
            "logUri": t.string().optional(),
            "runningCount": t.integer().optional(),
            "generation": t.string().optional(),
            "deleteTime": t.string().optional(),
            "parallelism": t.integer().optional(),
            "taskCount": t.integer().optional(),
            "completionTime": t.string().optional(),
            "failedCount": t.integer().optional(),
            "cancelledCount": t.integer().optional(),
            "createTime": t.string().optional(),
            "template": t.proxy(renames["GoogleCloudRunV2TaskTemplateOut"]).optional(),
            "job": t.string().optional(),
            "succeededCount": t.integer().optional(),
            "observedGeneration": t.string().optional(),
            "startTime": t.string().optional(),
            "expireTime": t.string().optional(),
            "uid": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "satisfiesPzs": t.boolean().optional(),
            "etag": t.string().optional(),
            "conditions": t.array(
                t.proxy(renames["GoogleCloudRunV2ConditionOut"])
            ).optional(),
            "retriedCount": t.integer().optional(),
            "launchStage": t.string().optional(),
            "reconciling": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2ExecutionOut"])
    types["GoogleCloudRunV2ServiceIn"] = t.struct(
        {
            "launchStage": t.string().optional(),
            "ingress": t.string().optional(),
            "binaryAuthorization": t.proxy(
                renames["GoogleCloudRunV2BinaryAuthorizationIn"]
            ).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "traffic": t.array(
                t.proxy(renames["GoogleCloudRunV2TrafficTargetIn"])
            ).optional(),
            "clientVersion": t.string().optional(),
            "client": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "template": t.proxy(renames["GoogleCloudRunV2RevisionTemplateIn"]),
        }
    ).named(renames["GoogleCloudRunV2ServiceIn"])
    types["GoogleCloudRunV2ServiceOut"] = t.struct(
        {
            "launchStage": t.string().optional(),
            "ingress": t.string().optional(),
            "expireTime": t.string().optional(),
            "binaryAuthorization": t.proxy(
                renames["GoogleCloudRunV2BinaryAuthorizationOut"]
            ).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "traffic": t.array(
                t.proxy(renames["GoogleCloudRunV2TrafficTargetOut"])
            ).optional(),
            "updateTime": t.string().optional(),
            "generation": t.string().optional(),
            "clientVersion": t.string().optional(),
            "uri": t.string().optional(),
            "latestCreatedRevision": t.string().optional(),
            "client": t.string().optional(),
            "observedGeneration": t.string().optional(),
            "latestReadyRevision": t.string().optional(),
            "etag": t.string().optional(),
            "reconciling": t.boolean().optional(),
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "deleteTime": t.string().optional(),
            "creator": t.string().optional(),
            "lastModifier": t.string().optional(),
            "terminalCondition": t.proxy(
                renames["GoogleCloudRunV2ConditionOut"]
            ).optional(),
            "uid": t.string().optional(),
            "name": t.string().optional(),
            "trafficStatuses": t.array(
                t.proxy(renames["GoogleCloudRunV2TrafficTargetStatusOut"])
            ).optional(),
            "conditions": t.array(
                t.proxy(renames["GoogleCloudRunV2ConditionOut"])
            ).optional(),
            "satisfiesPzs": t.boolean().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "template": t.proxy(renames["GoogleCloudRunV2RevisionTemplateOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2ServiceOut"])
    types["GoogleCloudRunV2CloudSqlInstanceIn"] = t.struct(
        {"instances": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudRunV2CloudSqlInstanceIn"])
    types["GoogleCloudRunV2CloudSqlInstanceOut"] = t.struct(
        {
            "instances": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2CloudSqlInstanceOut"])
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
    types["GoogleCloudRunV2RevisionScalingIn"] = t.struct(
        {
            "minInstanceCount": t.integer().optional(),
            "maxInstanceCount": t.integer().optional(),
        }
    ).named(renames["GoogleCloudRunV2RevisionScalingIn"])
    types["GoogleCloudRunV2RevisionScalingOut"] = t.struct(
        {
            "minInstanceCount": t.integer().optional(),
            "maxInstanceCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2RevisionScalingOut"])
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
    types["GoogleCloudRunV2TaskIn"] = t.struct(
        {
            "timeout": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "volumes": t.array(t.proxy(renames["GoogleCloudRunV2VolumeIn"])).optional(),
            "maxRetries": t.integer().optional(),
            "executionEnvironment": t.string().optional(),
            "containers": t.array(
                t.proxy(renames["GoogleCloudRunV2ContainerIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudRunV2TaskIn"])
    types["GoogleCloudRunV2TaskOut"] = t.struct(
        {
            "expireTime": t.string().optional(),
            "startTime": t.string().optional(),
            "index": t.integer().optional(),
            "retried": t.integer().optional(),
            "timeout": t.string().optional(),
            "encryptionKey": t.string().optional(),
            "conditions": t.array(
                t.proxy(renames["GoogleCloudRunV2ConditionOut"])
            ).optional(),
            "serviceAccount": t.string().optional(),
            "generation": t.string().optional(),
            "deleteTime": t.string().optional(),
            "vpcAccess": t.proxy(renames["GoogleCloudRunV2VpcAccessOut"]).optional(),
            "execution": t.string().optional(),
            "completionTime": t.string().optional(),
            "etag": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "volumes": t.array(
                t.proxy(renames["GoogleCloudRunV2VolumeOut"])
            ).optional(),
            "job": t.string().optional(),
            "logUri": t.string().optional(),
            "satisfiesPzs": t.boolean().optional(),
            "updateTime": t.string().optional(),
            "observedGeneration": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "maxRetries": t.integer().optional(),
            "lastAttemptResult": t.proxy(
                renames["GoogleCloudRunV2TaskAttemptResultOut"]
            ).optional(),
            "reconciling": t.boolean().optional(),
            "executionEnvironment": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "uid": t.string().optional(),
            "containers": t.array(
                t.proxy(renames["GoogleCloudRunV2ContainerOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2TaskOut"])
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
    types["GoogleCloudRunV2TCPSocketActionIn"] = t.struct(
        {"port": t.integer().optional()}
    ).named(renames["GoogleCloudRunV2TCPSocketActionIn"])
    types["GoogleCloudRunV2TCPSocketActionOut"] = t.struct(
        {
            "port": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2TCPSocketActionOut"])
    types["GoogleCloudRunV2TrafficTargetStatusIn"] = t.struct(
        {
            "uri": t.string().optional(),
            "percent": t.integer().optional(),
            "type": t.string().optional(),
            "tag": t.string().optional(),
            "revision": t.string().optional(),
        }
    ).named(renames["GoogleCloudRunV2TrafficTargetStatusIn"])
    types["GoogleCloudRunV2TrafficTargetStatusOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "percent": t.integer().optional(),
            "type": t.string().optional(),
            "tag": t.string().optional(),
            "revision": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2TrafficTargetStatusOut"])
    types["GoogleCloudRunV2BinaryAuthorizationIn"] = t.struct(
        {
            "useDefault": t.boolean().optional(),
            "breakglassJustification": t.string().optional(),
        }
    ).named(renames["GoogleCloudRunV2BinaryAuthorizationIn"])
    types["GoogleCloudRunV2BinaryAuthorizationOut"] = t.struct(
        {
            "useDefault": t.boolean().optional(),
            "breakglassJustification": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2BinaryAuthorizationOut"])
    types["GoogleCloudRunV2RevisionTemplateIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "sessionAffinity": t.boolean().optional(),
            "maxInstanceRequestConcurrency": t.integer().optional(),
            "serviceAccount": t.string().optional(),
            "containers": t.array(
                t.proxy(renames["GoogleCloudRunV2ContainerIn"])
            ).optional(),
            "revision": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "encryptionKey": t.string().optional(),
            "vpcAccess": t.proxy(renames["GoogleCloudRunV2VpcAccessIn"]).optional(),
            "timeout": t.string().optional(),
            "executionEnvironment": t.string().optional(),
            "volumes": t.array(t.proxy(renames["GoogleCloudRunV2VolumeIn"])).optional(),
            "scaling": t.proxy(renames["GoogleCloudRunV2RevisionScalingIn"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2RevisionTemplateIn"])
    types["GoogleCloudRunV2RevisionTemplateOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "sessionAffinity": t.boolean().optional(),
            "maxInstanceRequestConcurrency": t.integer().optional(),
            "serviceAccount": t.string().optional(),
            "containers": t.array(
                t.proxy(renames["GoogleCloudRunV2ContainerOut"])
            ).optional(),
            "revision": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "encryptionKey": t.string().optional(),
            "vpcAccess": t.proxy(renames["GoogleCloudRunV2VpcAccessOut"]).optional(),
            "timeout": t.string().optional(),
            "executionEnvironment": t.string().optional(),
            "volumes": t.array(
                t.proxy(renames["GoogleCloudRunV2VolumeOut"])
            ).optional(),
            "scaling": t.proxy(
                renames["GoogleCloudRunV2RevisionScalingOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2RevisionTemplateOut"])
    types["GoogleCloudRunV2JobIn"] = t.struct(
        {
            "binaryAuthorization": t.proxy(
                renames["GoogleCloudRunV2BinaryAuthorizationIn"]
            ).optional(),
            "clientVersion": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "client": t.string().optional(),
            "template": t.proxy(renames["GoogleCloudRunV2ExecutionTemplateIn"]),
            "launchStage": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudRunV2JobIn"])
    types["GoogleCloudRunV2JobOut"] = t.struct(
        {
            "binaryAuthorization": t.proxy(
                renames["GoogleCloudRunV2BinaryAuthorizationOut"]
            ).optional(),
            "conditions": t.array(
                t.proxy(renames["GoogleCloudRunV2ConditionOut"])
            ).optional(),
            "terminalCondition": t.proxy(
                renames["GoogleCloudRunV2ConditionOut"]
            ).optional(),
            "expireTime": t.string().optional(),
            "clientVersion": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "client": t.string().optional(),
            "template": t.proxy(renames["GoogleCloudRunV2ExecutionTemplateOut"]),
            "launchStage": t.string().optional(),
            "lastModifier": t.string().optional(),
            "creator": t.string().optional(),
            "satisfiesPzs": t.boolean().optional(),
            "latestCreatedExecution": t.proxy(
                renames["GoogleCloudRunV2ExecutionReferenceOut"]
            ).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "deleteTime": t.string().optional(),
            "observedGeneration": t.string().optional(),
            "reconciling": t.boolean().optional(),
            "etag": t.string().optional(),
            "uid": t.string().optional(),
            "executionCount": t.integer().optional(),
            "generation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2JobOut"])
    types["GoogleCloudRunV2ConditionIn"] = t.struct(
        {
            "executionReason": t.string().optional(),
            "reason": t.string().optional(),
            "revisionReason": t.string().optional(),
            "lastTransitionTime": t.string().optional(),
            "state": t.string().optional(),
            "severity": t.string().optional(),
            "type": t.string().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["GoogleCloudRunV2ConditionIn"])
    types["GoogleCloudRunV2ConditionOut"] = t.struct(
        {
            "executionReason": t.string().optional(),
            "reason": t.string().optional(),
            "revisionReason": t.string().optional(),
            "lastTransitionTime": t.string().optional(),
            "state": t.string().optional(),
            "severity": t.string().optional(),
            "type": t.string().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2ConditionOut"])
    types["GoogleCloudRunV2HTTPGetActionIn"] = t.struct(
        {
            "path": t.string().optional(),
            "port": t.integer().optional(),
            "httpHeaders": t.array(
                t.proxy(renames["GoogleCloudRunV2HTTPHeaderIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudRunV2HTTPGetActionIn"])
    types["GoogleCloudRunV2HTTPGetActionOut"] = t.struct(
        {
            "path": t.string().optional(),
            "port": t.integer().optional(),
            "httpHeaders": t.array(
                t.proxy(renames["GoogleCloudRunV2HTTPHeaderOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2HTTPGetActionOut"])
    types["GoogleCloudRunV2ResourceRequirementsIn"] = t.struct(
        {
            "cpuIdle": t.boolean().optional(),
            "startupCpuBoost": t.boolean().optional(),
            "limits": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudRunV2ResourceRequirementsIn"])
    types["GoogleCloudRunV2ResourceRequirementsOut"] = t.struct(
        {
            "cpuIdle": t.boolean().optional(),
            "startupCpuBoost": t.boolean().optional(),
            "limits": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2ResourceRequirementsOut"])
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
    types["GoogleIamV1TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["GoogleIamV1TestIamPermissionsResponseIn"])
    types["GoogleIamV1TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1TestIamPermissionsResponseOut"])
    types["GoogleCloudRunV2ListRevisionsResponseIn"] = t.struct(
        {
            "revisions": t.array(
                t.proxy(renames["GoogleCloudRunV2RevisionIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudRunV2ListRevisionsResponseIn"])
    types["GoogleCloudRunV2ListRevisionsResponseOut"] = t.struct(
        {
            "revisions": t.array(
                t.proxy(renames["GoogleCloudRunV2RevisionOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2ListRevisionsResponseOut"])
    types["GoogleTypeExprIn"] = t.struct(
        {
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleTypeExprIn"])
    types["GoogleTypeExprOut"] = t.struct(
        {
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeExprOut"])
    types["GoogleCloudRunV2EnvVarIn"] = t.struct(
        {
            "valueSource": t.proxy(
                renames["GoogleCloudRunV2EnvVarSourceIn"]
            ).optional(),
            "value": t.string().optional(),
            "name": t.string(),
        }
    ).named(renames["GoogleCloudRunV2EnvVarIn"])
    types["GoogleCloudRunV2EnvVarOut"] = t.struct(
        {
            "valueSource": t.proxy(
                renames["GoogleCloudRunV2EnvVarSourceOut"]
            ).optional(),
            "value": t.string().optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2EnvVarOut"])
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
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
    types["GoogleCloudRunV2ExecutionTemplateIn"] = t.struct(
        {
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "template": t.proxy(renames["GoogleCloudRunV2TaskTemplateIn"]),
            "taskCount": t.integer().optional(),
            "parallelism": t.integer().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudRunV2ExecutionTemplateIn"])
    types["GoogleCloudRunV2ExecutionTemplateOut"] = t.struct(
        {
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "template": t.proxy(renames["GoogleCloudRunV2TaskTemplateOut"]),
            "taskCount": t.integer().optional(),
            "parallelism": t.integer().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2ExecutionTemplateOut"])
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
    types["GoogleRpcStatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
        }
    ).named(renames["GoogleRpcStatusIn"])
    types["GoogleRpcStatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleRpcStatusOut"])
    types["GoogleCloudRunV2SecretKeySelectorIn"] = t.struct(
        {"version": t.string().optional(), "secret": t.string()}
    ).named(renames["GoogleCloudRunV2SecretKeySelectorIn"])
    types["GoogleCloudRunV2SecretKeySelectorOut"] = t.struct(
        {
            "version": t.string().optional(),
            "secret": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2SecretKeySelectorOut"])
    types["GoogleCloudRunV2TaskTemplateIn"] = t.struct(
        {
            "encryptionKey": t.string().optional(),
            "vpcAccess": t.proxy(renames["GoogleCloudRunV2VpcAccessIn"]).optional(),
            "maxRetries": t.integer().optional(),
            "serviceAccount": t.string().optional(),
            "volumes": t.array(t.proxy(renames["GoogleCloudRunV2VolumeIn"])).optional(),
            "timeout": t.string().optional(),
            "containers": t.array(
                t.proxy(renames["GoogleCloudRunV2ContainerIn"])
            ).optional(),
            "executionEnvironment": t.string().optional(),
        }
    ).named(renames["GoogleCloudRunV2TaskTemplateIn"])
    types["GoogleCloudRunV2TaskTemplateOut"] = t.struct(
        {
            "encryptionKey": t.string().optional(),
            "vpcAccess": t.proxy(renames["GoogleCloudRunV2VpcAccessOut"]).optional(),
            "maxRetries": t.integer().optional(),
            "serviceAccount": t.string().optional(),
            "volumes": t.array(
                t.proxy(renames["GoogleCloudRunV2VolumeOut"])
            ).optional(),
            "timeout": t.string().optional(),
            "containers": t.array(
                t.proxy(renames["GoogleCloudRunV2ContainerOut"])
            ).optional(),
            "executionEnvironment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2TaskTemplateOut"])
    types["GoogleCloudRunV2VersionToPathIn"] = t.struct(
        {
            "version": t.string().optional(),
            "path": t.string(),
            "mode": t.integer().optional(),
        }
    ).named(renames["GoogleCloudRunV2VersionToPathIn"])
    types["GoogleCloudRunV2VersionToPathOut"] = t.struct(
        {
            "version": t.string().optional(),
            "path": t.string(),
            "mode": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2VersionToPathOut"])
    types["GoogleLongrunningListOperationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(
                t.proxy(renames["GoogleLongrunningOperationIn"])
            ).optional(),
        }
    ).named(renames["GoogleLongrunningListOperationsResponseIn"])
    types["GoogleLongrunningListOperationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(
                t.proxy(renames["GoogleLongrunningOperationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleLongrunningListOperationsResponseOut"])
    types["GoogleCloudRunV2RevisionIn"] = t.struct(
        {
            "volumes": t.array(t.proxy(renames["GoogleCloudRunV2VolumeIn"])).optional(),
            "sessionAffinity": t.boolean().optional(),
            "encryptionKeyRevocationAction": t.string().optional(),
            "launchStage": t.string().optional(),
            "encryptionKeyShutdownDuration": t.string().optional(),
            "executionEnvironment": t.string().optional(),
            "containers": t.array(
                t.proxy(renames["GoogleCloudRunV2ContainerIn"])
            ).optional(),
            "serviceAccount": t.string().optional(),
            "vpcAccess": t.proxy(renames["GoogleCloudRunV2VpcAccessIn"]).optional(),
            "scaling": t.proxy(renames["GoogleCloudRunV2RevisionScalingIn"]).optional(),
            "maxInstanceRequestConcurrency": t.integer().optional(),
            "encryptionKey": t.string().optional(),
            "timeout": t.string().optional(),
        }
    ).named(renames["GoogleCloudRunV2RevisionIn"])
    types["GoogleCloudRunV2RevisionOut"] = t.struct(
        {
            "volumes": t.array(
                t.proxy(renames["GoogleCloudRunV2VolumeOut"])
            ).optional(),
            "sessionAffinity": t.boolean().optional(),
            "encryptionKeyRevocationAction": t.string().optional(),
            "etag": t.string().optional(),
            "launchStage": t.string().optional(),
            "reconciling": t.boolean().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "encryptionKeyShutdownDuration": t.string().optional(),
            "satisfiesPzs": t.boolean().optional(),
            "deleteTime": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "uid": t.string().optional(),
            "generation": t.string().optional(),
            "executionEnvironment": t.string().optional(),
            "containers": t.array(
                t.proxy(renames["GoogleCloudRunV2ContainerOut"])
            ).optional(),
            "serviceAccount": t.string().optional(),
            "vpcAccess": t.proxy(renames["GoogleCloudRunV2VpcAccessOut"]).optional(),
            "scaling": t.proxy(
                renames["GoogleCloudRunV2RevisionScalingOut"]
            ).optional(),
            "maxInstanceRequestConcurrency": t.integer().optional(),
            "encryptionKey": t.string().optional(),
            "expireTime": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "conditions": t.array(
                t.proxy(renames["GoogleCloudRunV2ConditionOut"])
            ).optional(),
            "timeout": t.string().optional(),
            "observedGeneration": t.string().optional(),
            "logUri": t.string().optional(),
            "service": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2RevisionOut"])
    types["GoogleCloudRunV2VolumeMountIn"] = t.struct(
        {"name": t.string(), "mountPath": t.string()}
    ).named(renames["GoogleCloudRunV2VolumeMountIn"])
    types["GoogleCloudRunV2VolumeMountOut"] = t.struct(
        {
            "name": t.string(),
            "mountPath": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2VolumeMountOut"])
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
    types["GoogleIamV1PolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["GoogleIamV1BindingIn"])).optional(),
            "auditConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditConfigIn"])
            ).optional(),
            "version": t.integer().optional(),
        }
    ).named(renames["GoogleIamV1PolicyIn"])
    types["GoogleIamV1PolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["GoogleIamV1BindingOut"])).optional(),
            "auditConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditConfigOut"])
            ).optional(),
            "version": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1PolicyOut"])
    types["GoogleCloudRunV2TrafficTargetIn"] = t.struct(
        {
            "percent": t.integer().optional(),
            "tag": t.string().optional(),
            "type": t.string().optional(),
            "revision": t.string().optional(),
        }
    ).named(renames["GoogleCloudRunV2TrafficTargetIn"])
    types["GoogleCloudRunV2TrafficTargetOut"] = t.struct(
        {
            "percent": t.integer().optional(),
            "tag": t.string().optional(),
            "type": t.string().optional(),
            "revision": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2TrafficTargetOut"])
    types["GoogleCloudRunV2GRPCActionIn"] = t.struct(
        {"port": t.integer().optional(), "service": t.string().optional()}
    ).named(renames["GoogleCloudRunV2GRPCActionIn"])
    types["GoogleCloudRunV2GRPCActionOut"] = t.struct(
        {
            "port": t.integer().optional(),
            "service": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2GRPCActionOut"])
    types["GoogleCloudRunV2ExecutionReferenceIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "completionTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudRunV2ExecutionReferenceIn"])
    types["GoogleCloudRunV2ExecutionReferenceOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "completionTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2ExecutionReferenceOut"])
    types["GoogleCloudRunV2ContainerIn"] = t.struct(
        {
            "env": t.array(t.proxy(renames["GoogleCloudRunV2EnvVarIn"])).optional(),
            "livenessProbe": t.proxy(renames["GoogleCloudRunV2ProbeIn"]).optional(),
            "volumeMounts": t.array(
                t.proxy(renames["GoogleCloudRunV2VolumeMountIn"])
            ).optional(),
            "name": t.string().optional(),
            "ports": t.array(
                t.proxy(renames["GoogleCloudRunV2ContainerPortIn"])
            ).optional(),
            "image": t.string(),
            "command": t.array(t.string()).optional(),
            "dependsOn": t.array(t.string()).optional(),
            "startupProbe": t.proxy(renames["GoogleCloudRunV2ProbeIn"]).optional(),
            "args": t.array(t.string()).optional(),
            "resources": t.proxy(
                renames["GoogleCloudRunV2ResourceRequirementsIn"]
            ).optional(),
            "workingDir": t.string().optional(),
        }
    ).named(renames["GoogleCloudRunV2ContainerIn"])
    types["GoogleCloudRunV2ContainerOut"] = t.struct(
        {
            "env": t.array(t.proxy(renames["GoogleCloudRunV2EnvVarOut"])).optional(),
            "livenessProbe": t.proxy(renames["GoogleCloudRunV2ProbeOut"]).optional(),
            "volumeMounts": t.array(
                t.proxy(renames["GoogleCloudRunV2VolumeMountOut"])
            ).optional(),
            "name": t.string().optional(),
            "ports": t.array(
                t.proxy(renames["GoogleCloudRunV2ContainerPortOut"])
            ).optional(),
            "image": t.string(),
            "command": t.array(t.string()).optional(),
            "dependsOn": t.array(t.string()).optional(),
            "startupProbe": t.proxy(renames["GoogleCloudRunV2ProbeOut"]).optional(),
            "args": t.array(t.string()).optional(),
            "resources": t.proxy(
                renames["GoogleCloudRunV2ResourceRequirementsOut"]
            ).optional(),
            "workingDir": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2ContainerOut"])
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
    types["GoogleLongrunningWaitOperationRequestIn"] = t.struct(
        {"timeout": t.string().optional()}
    ).named(renames["GoogleLongrunningWaitOperationRequestIn"])
    types["GoogleLongrunningWaitOperationRequestOut"] = t.struct(
        {
            "timeout": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleLongrunningWaitOperationRequestOut"])
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
    types["GoogleCloudRunV2TaskAttemptResultIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRunV2TaskAttemptResultIn"])
    types["GoogleCloudRunV2TaskAttemptResultOut"] = t.struct(
        {
            "status": t.proxy(renames["GoogleRpcStatusOut"]).optional(),
            "exitCode": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2TaskAttemptResultOut"])
    types["GoogleCloudRunV2ProbeIn"] = t.struct(
        {
            "initialDelaySeconds": t.integer().optional(),
            "httpGet": t.proxy(renames["GoogleCloudRunV2HTTPGetActionIn"]).optional(),
            "periodSeconds": t.integer().optional(),
            "grpc": t.proxy(renames["GoogleCloudRunV2GRPCActionIn"]).optional(),
            "failureThreshold": t.integer().optional(),
            "tcpSocket": t.proxy(
                renames["GoogleCloudRunV2TCPSocketActionIn"]
            ).optional(),
            "timeoutSeconds": t.integer().optional(),
        }
    ).named(renames["GoogleCloudRunV2ProbeIn"])
    types["GoogleCloudRunV2ProbeOut"] = t.struct(
        {
            "initialDelaySeconds": t.integer().optional(),
            "httpGet": t.proxy(renames["GoogleCloudRunV2HTTPGetActionOut"]).optional(),
            "periodSeconds": t.integer().optional(),
            "grpc": t.proxy(renames["GoogleCloudRunV2GRPCActionOut"]).optional(),
            "failureThreshold": t.integer().optional(),
            "tcpSocket": t.proxy(
                renames["GoogleCloudRunV2TCPSocketActionOut"]
            ).optional(),
            "timeoutSeconds": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2ProbeOut"])
    types["GoogleIamV1AuditLogConfigIn"] = t.struct(
        {
            "logType": t.string().optional(),
            "exemptedMembers": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleIamV1AuditLogConfigIn"])
    types["GoogleIamV1AuditLogConfigOut"] = t.struct(
        {
            "logType": t.string().optional(),
            "exemptedMembers": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1AuditLogConfigOut"])
    types["GoogleCloudRunV2VolumeIn"] = t.struct(
        {
            "emptyDir": t.proxy(
                renames["GoogleCloudRunV2EmptyDirVolumeSourceIn"]
            ).optional(),
            "secret": t.proxy(
                renames["GoogleCloudRunV2SecretVolumeSourceIn"]
            ).optional(),
            "cloudSqlInstance": t.proxy(
                renames["GoogleCloudRunV2CloudSqlInstanceIn"]
            ).optional(),
            "name": t.string(),
        }
    ).named(renames["GoogleCloudRunV2VolumeIn"])
    types["GoogleCloudRunV2VolumeOut"] = t.struct(
        {
            "emptyDir": t.proxy(
                renames["GoogleCloudRunV2EmptyDirVolumeSourceOut"]
            ).optional(),
            "secret": t.proxy(
                renames["GoogleCloudRunV2SecretVolumeSourceOut"]
            ).optional(),
            "cloudSqlInstance": t.proxy(
                renames["GoogleCloudRunV2CloudSqlInstanceOut"]
            ).optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2VolumeOut"])

    functions = {}
    functions["projectsLocationsJobsCreate"] = run.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRunV2JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsDelete"] = run.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRunV2JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsTestIamPermissions"] = run.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRunV2JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsRun"] = run.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRunV2JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsGetIamPolicy"] = run.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRunV2JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsPatch"] = run.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRunV2JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsList"] = run.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRunV2JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsSetIamPolicy"] = run.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRunV2JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsGet"] = run.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRunV2JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsExecutionsList"] = run.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRunV2ExecutionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsExecutionsDelete"] = run.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRunV2ExecutionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsExecutionsGet"] = run.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRunV2ExecutionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsExecutionsTasksGet"] = run.get(
        "v2/{parent}/tasks",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "showDeleted": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRunV2ListTasksResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsExecutionsTasksList"] = run.get(
        "v2/{parent}/tasks",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "showDeleted": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRunV2ListTasksResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsWait"] = run.get(
        "v2/{name}/operations",
        t.struct(
            {
                "name": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = run.get(
        "v2/{name}/operations",
        t.struct(
            {
                "name": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = run.get(
        "v2/{name}/operations",
        t.struct(
            {
                "name": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = run.get(
        "v2/{name}/operations",
        t.struct(
            {
                "name": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesTestIamPermissions"] = run.post(
        "v2/{parent}/services",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "parent": t.string(),
                "serviceId": t.string(),
                "launchStage": t.string().optional(),
                "ingress": t.string().optional(),
                "binaryAuthorization": t.proxy(
                    renames["GoogleCloudRunV2BinaryAuthorizationIn"]
                ).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "traffic": t.array(
                    t.proxy(renames["GoogleCloudRunV2TrafficTargetIn"])
                ).optional(),
                "clientVersion": t.string().optional(),
                "client": t.string().optional(),
                "description": t.string().optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "template": t.proxy(renames["GoogleCloudRunV2RevisionTemplateIn"]),
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
                "parent": t.string(),
                "serviceId": t.string(),
                "launchStage": t.string().optional(),
                "ingress": t.string().optional(),
                "binaryAuthorization": t.proxy(
                    renames["GoogleCloudRunV2BinaryAuthorizationIn"]
                ).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "traffic": t.array(
                    t.proxy(renames["GoogleCloudRunV2TrafficTargetIn"])
                ).optional(),
                "clientVersion": t.string().optional(),
                "client": t.string().optional(),
                "description": t.string().optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "template": t.proxy(renames["GoogleCloudRunV2RevisionTemplateIn"]),
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
                "parent": t.string(),
                "serviceId": t.string(),
                "launchStage": t.string().optional(),
                "ingress": t.string().optional(),
                "binaryAuthorization": t.proxy(
                    renames["GoogleCloudRunV2BinaryAuthorizationIn"]
                ).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "traffic": t.array(
                    t.proxy(renames["GoogleCloudRunV2TrafficTargetIn"])
                ).optional(),
                "clientVersion": t.string().optional(),
                "client": t.string().optional(),
                "description": t.string().optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "template": t.proxy(renames["GoogleCloudRunV2RevisionTemplateIn"]),
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
                "parent": t.string(),
                "serviceId": t.string(),
                "launchStage": t.string().optional(),
                "ingress": t.string().optional(),
                "binaryAuthorization": t.proxy(
                    renames["GoogleCloudRunV2BinaryAuthorizationIn"]
                ).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "traffic": t.array(
                    t.proxy(renames["GoogleCloudRunV2TrafficTargetIn"])
                ).optional(),
                "clientVersion": t.string().optional(),
                "client": t.string().optional(),
                "description": t.string().optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "template": t.proxy(renames["GoogleCloudRunV2RevisionTemplateIn"]),
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
                "parent": t.string(),
                "serviceId": t.string(),
                "launchStage": t.string().optional(),
                "ingress": t.string().optional(),
                "binaryAuthorization": t.proxy(
                    renames["GoogleCloudRunV2BinaryAuthorizationIn"]
                ).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "traffic": t.array(
                    t.proxy(renames["GoogleCloudRunV2TrafficTargetIn"])
                ).optional(),
                "clientVersion": t.string().optional(),
                "client": t.string().optional(),
                "description": t.string().optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "template": t.proxy(renames["GoogleCloudRunV2RevisionTemplateIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesGetIamPolicy"] = run.post(
        "v2/{parent}/services",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "parent": t.string(),
                "serviceId": t.string(),
                "launchStage": t.string().optional(),
                "ingress": t.string().optional(),
                "binaryAuthorization": t.proxy(
                    renames["GoogleCloudRunV2BinaryAuthorizationIn"]
                ).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "traffic": t.array(
                    t.proxy(renames["GoogleCloudRunV2TrafficTargetIn"])
                ).optional(),
                "clientVersion": t.string().optional(),
                "client": t.string().optional(),
                "description": t.string().optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "template": t.proxy(renames["GoogleCloudRunV2RevisionTemplateIn"]),
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
                "parent": t.string(),
                "serviceId": t.string(),
                "launchStage": t.string().optional(),
                "ingress": t.string().optional(),
                "binaryAuthorization": t.proxy(
                    renames["GoogleCloudRunV2BinaryAuthorizationIn"]
                ).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "traffic": t.array(
                    t.proxy(renames["GoogleCloudRunV2TrafficTargetIn"])
                ).optional(),
                "clientVersion": t.string().optional(),
                "client": t.string().optional(),
                "description": t.string().optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "template": t.proxy(renames["GoogleCloudRunV2RevisionTemplateIn"]),
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
                "parent": t.string(),
                "serviceId": t.string(),
                "launchStage": t.string().optional(),
                "ingress": t.string().optional(),
                "binaryAuthorization": t.proxy(
                    renames["GoogleCloudRunV2BinaryAuthorizationIn"]
                ).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "traffic": t.array(
                    t.proxy(renames["GoogleCloudRunV2TrafficTargetIn"])
                ).optional(),
                "clientVersion": t.string().optional(),
                "client": t.string().optional(),
                "description": t.string().optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "template": t.proxy(renames["GoogleCloudRunV2RevisionTemplateIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesRevisionsGet"] = run.delete(
        "v2/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "name": t.string(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesRevisionsList"] = run.delete(
        "v2/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "name": t.string(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesRevisionsDelete"] = run.delete(
        "v2/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "name": t.string(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="run", renames=renames, types=Box(types), functions=Box(functions)
    )
