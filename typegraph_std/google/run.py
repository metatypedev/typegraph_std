from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_run():
    run = HTTPRuntime("https://run.googleapis.com/")

    renames = {
        "ErrorResponse": "_run_1_ErrorResponse",
        "GoogleLongrunningOperationIn": "_run_2_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_run_3_GoogleLongrunningOperationOut",
        "GoogleCloudRunV2ExecutionIn": "_run_4_GoogleCloudRunV2ExecutionIn",
        "GoogleCloudRunV2ExecutionOut": "_run_5_GoogleCloudRunV2ExecutionOut",
        "GoogleLongrunningWaitOperationRequestIn": "_run_6_GoogleLongrunningWaitOperationRequestIn",
        "GoogleLongrunningWaitOperationRequestOut": "_run_7_GoogleLongrunningWaitOperationRequestOut",
        "GoogleCloudRunV2ListRevisionsResponseIn": "_run_8_GoogleCloudRunV2ListRevisionsResponseIn",
        "GoogleCloudRunV2ListRevisionsResponseOut": "_run_9_GoogleCloudRunV2ListRevisionsResponseOut",
        "GoogleCloudRunV2TaskTemplateIn": "_run_10_GoogleCloudRunV2TaskTemplateIn",
        "GoogleCloudRunV2TaskTemplateOut": "_run_11_GoogleCloudRunV2TaskTemplateOut",
        "GoogleCloudRunV2EmptyDirVolumeSourceIn": "_run_12_GoogleCloudRunV2EmptyDirVolumeSourceIn",
        "GoogleCloudRunV2EmptyDirVolumeSourceOut": "_run_13_GoogleCloudRunV2EmptyDirVolumeSourceOut",
        "GoogleCloudRunV2BinaryAuthorizationIn": "_run_14_GoogleCloudRunV2BinaryAuthorizationIn",
        "GoogleCloudRunV2BinaryAuthorizationOut": "_run_15_GoogleCloudRunV2BinaryAuthorizationOut",
        "GoogleCloudRunV2ResourceRequirementsIn": "_run_16_GoogleCloudRunV2ResourceRequirementsIn",
        "GoogleCloudRunV2ResourceRequirementsOut": "_run_17_GoogleCloudRunV2ResourceRequirementsOut",
        "GoogleIamV1TestIamPermissionsRequestIn": "_run_18_GoogleIamV1TestIamPermissionsRequestIn",
        "GoogleIamV1TestIamPermissionsRequestOut": "_run_19_GoogleIamV1TestIamPermissionsRequestOut",
        "GoogleCloudRunV2CloudSqlInstanceIn": "_run_20_GoogleCloudRunV2CloudSqlInstanceIn",
        "GoogleCloudRunV2CloudSqlInstanceOut": "_run_21_GoogleCloudRunV2CloudSqlInstanceOut",
        "GoogleCloudRunV2GRPCActionIn": "_run_22_GoogleCloudRunV2GRPCActionIn",
        "GoogleCloudRunV2GRPCActionOut": "_run_23_GoogleCloudRunV2GRPCActionOut",
        "GoogleCloudRunV2SecretKeySelectorIn": "_run_24_GoogleCloudRunV2SecretKeySelectorIn",
        "GoogleCloudRunV2SecretKeySelectorOut": "_run_25_GoogleCloudRunV2SecretKeySelectorOut",
        "GoogleCloudRunV2ListJobsResponseIn": "_run_26_GoogleCloudRunV2ListJobsResponseIn",
        "GoogleCloudRunV2ListJobsResponseOut": "_run_27_GoogleCloudRunV2ListJobsResponseOut",
        "GoogleIamV1PolicyIn": "_run_28_GoogleIamV1PolicyIn",
        "GoogleIamV1PolicyOut": "_run_29_GoogleIamV1PolicyOut",
        "GoogleCloudRunV2VersionToPathIn": "_run_30_GoogleCloudRunV2VersionToPathIn",
        "GoogleCloudRunV2VersionToPathOut": "_run_31_GoogleCloudRunV2VersionToPathOut",
        "GoogleCloudRunV2VolumeIn": "_run_32_GoogleCloudRunV2VolumeIn",
        "GoogleCloudRunV2VolumeOut": "_run_33_GoogleCloudRunV2VolumeOut",
        "GoogleIamV1AuditConfigIn": "_run_34_GoogleIamV1AuditConfigIn",
        "GoogleIamV1AuditConfigOut": "_run_35_GoogleIamV1AuditConfigOut",
        "GoogleCloudRunV2TrafficTargetStatusIn": "_run_36_GoogleCloudRunV2TrafficTargetStatusIn",
        "GoogleCloudRunV2TrafficTargetStatusOut": "_run_37_GoogleCloudRunV2TrafficTargetStatusOut",
        "GoogleCloudRunV2ExecutionTemplateIn": "_run_38_GoogleCloudRunV2ExecutionTemplateIn",
        "GoogleCloudRunV2ExecutionTemplateOut": "_run_39_GoogleCloudRunV2ExecutionTemplateOut",
        "GoogleCloudRunV2EnvVarIn": "_run_40_GoogleCloudRunV2EnvVarIn",
        "GoogleCloudRunV2EnvVarOut": "_run_41_GoogleCloudRunV2EnvVarOut",
        "GoogleCloudRunV2ListTasksResponseIn": "_run_42_GoogleCloudRunV2ListTasksResponseIn",
        "GoogleCloudRunV2ListTasksResponseOut": "_run_43_GoogleCloudRunV2ListTasksResponseOut",
        "GoogleCloudRunV2RevisionIn": "_run_44_GoogleCloudRunV2RevisionIn",
        "GoogleCloudRunV2RevisionOut": "_run_45_GoogleCloudRunV2RevisionOut",
        "GoogleCloudRunV2ConditionIn": "_run_46_GoogleCloudRunV2ConditionIn",
        "GoogleCloudRunV2ConditionOut": "_run_47_GoogleCloudRunV2ConditionOut",
        "GoogleCloudRunV2VolumeMountIn": "_run_48_GoogleCloudRunV2VolumeMountIn",
        "GoogleCloudRunV2VolumeMountOut": "_run_49_GoogleCloudRunV2VolumeMountOut",
        "GoogleCloudRunV2HTTPHeaderIn": "_run_50_GoogleCloudRunV2HTTPHeaderIn",
        "GoogleCloudRunV2HTTPHeaderOut": "_run_51_GoogleCloudRunV2HTTPHeaderOut",
        "GoogleCloudRunV2TaskIn": "_run_52_GoogleCloudRunV2TaskIn",
        "GoogleCloudRunV2TaskOut": "_run_53_GoogleCloudRunV2TaskOut",
        "GoogleCloudRunV2RevisionTemplateIn": "_run_54_GoogleCloudRunV2RevisionTemplateIn",
        "GoogleCloudRunV2RevisionTemplateOut": "_run_55_GoogleCloudRunV2RevisionTemplateOut",
        "GoogleCloudRunV2RevisionScalingIn": "_run_56_GoogleCloudRunV2RevisionScalingIn",
        "GoogleCloudRunV2RevisionScalingOut": "_run_57_GoogleCloudRunV2RevisionScalingOut",
        "GoogleCloudRunV2ContainerIn": "_run_58_GoogleCloudRunV2ContainerIn",
        "GoogleCloudRunV2ContainerOut": "_run_59_GoogleCloudRunV2ContainerOut",
        "GoogleIamV1BindingIn": "_run_60_GoogleIamV1BindingIn",
        "GoogleIamV1BindingOut": "_run_61_GoogleIamV1BindingOut",
        "GoogleCloudRunV2TCPSocketActionIn": "_run_62_GoogleCloudRunV2TCPSocketActionIn",
        "GoogleCloudRunV2TCPSocketActionOut": "_run_63_GoogleCloudRunV2TCPSocketActionOut",
        "GoogleCloudRunV2TrafficTargetIn": "_run_64_GoogleCloudRunV2TrafficTargetIn",
        "GoogleCloudRunV2TrafficTargetOut": "_run_65_GoogleCloudRunV2TrafficTargetOut",
        "GoogleCloudRunV2RunJobRequestIn": "_run_66_GoogleCloudRunV2RunJobRequestIn",
        "GoogleCloudRunV2RunJobRequestOut": "_run_67_GoogleCloudRunV2RunJobRequestOut",
        "GoogleTypeExprIn": "_run_68_GoogleTypeExprIn",
        "GoogleTypeExprOut": "_run_69_GoogleTypeExprOut",
        "GoogleProtobufEmptyIn": "_run_70_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_run_71_GoogleProtobufEmptyOut",
        "GoogleCloudRunV2ExecutionReferenceIn": "_run_72_GoogleCloudRunV2ExecutionReferenceIn",
        "GoogleCloudRunV2ExecutionReferenceOut": "_run_73_GoogleCloudRunV2ExecutionReferenceOut",
        "GoogleCloudRunV2VpcAccessIn": "_run_74_GoogleCloudRunV2VpcAccessIn",
        "GoogleCloudRunV2VpcAccessOut": "_run_75_GoogleCloudRunV2VpcAccessOut",
        "GoogleCloudRunV2EnvVarSourceIn": "_run_76_GoogleCloudRunV2EnvVarSourceIn",
        "GoogleCloudRunV2EnvVarSourceOut": "_run_77_GoogleCloudRunV2EnvVarSourceOut",
        "GoogleCloudRunV2SecretVolumeSourceIn": "_run_78_GoogleCloudRunV2SecretVolumeSourceIn",
        "GoogleCloudRunV2SecretVolumeSourceOut": "_run_79_GoogleCloudRunV2SecretVolumeSourceOut",
        "GoogleCloudRunV2ListExecutionsResponseIn": "_run_80_GoogleCloudRunV2ListExecutionsResponseIn",
        "GoogleCloudRunV2ListExecutionsResponseOut": "_run_81_GoogleCloudRunV2ListExecutionsResponseOut",
        "GoogleRpcStatusIn": "_run_82_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_run_83_GoogleRpcStatusOut",
        "GoogleIamV1TestIamPermissionsResponseIn": "_run_84_GoogleIamV1TestIamPermissionsResponseIn",
        "GoogleIamV1TestIamPermissionsResponseOut": "_run_85_GoogleIamV1TestIamPermissionsResponseOut",
        "GoogleCloudRunV2TaskAttemptResultIn": "_run_86_GoogleCloudRunV2TaskAttemptResultIn",
        "GoogleCloudRunV2TaskAttemptResultOut": "_run_87_GoogleCloudRunV2TaskAttemptResultOut",
        "GoogleIamV1AuditLogConfigIn": "_run_88_GoogleIamV1AuditLogConfigIn",
        "GoogleIamV1AuditLogConfigOut": "_run_89_GoogleIamV1AuditLogConfigOut",
        "GoogleCloudRunV2ContainerPortIn": "_run_90_GoogleCloudRunV2ContainerPortIn",
        "GoogleCloudRunV2ContainerPortOut": "_run_91_GoogleCloudRunV2ContainerPortOut",
        "GoogleCloudRunV2ProbeIn": "_run_92_GoogleCloudRunV2ProbeIn",
        "GoogleCloudRunV2ProbeOut": "_run_93_GoogleCloudRunV2ProbeOut",
        "GoogleIamV1SetIamPolicyRequestIn": "_run_94_GoogleIamV1SetIamPolicyRequestIn",
        "GoogleIamV1SetIamPolicyRequestOut": "_run_95_GoogleIamV1SetIamPolicyRequestOut",
        "GoogleLongrunningListOperationsResponseIn": "_run_96_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_run_97_GoogleLongrunningListOperationsResponseOut",
        "GoogleCloudRunV2JobIn": "_run_98_GoogleCloudRunV2JobIn",
        "GoogleCloudRunV2JobOut": "_run_99_GoogleCloudRunV2JobOut",
        "GoogleCloudRunV2HTTPGetActionIn": "_run_100_GoogleCloudRunV2HTTPGetActionIn",
        "GoogleCloudRunV2HTTPGetActionOut": "_run_101_GoogleCloudRunV2HTTPGetActionOut",
        "GoogleCloudRunV2ServiceIn": "_run_102_GoogleCloudRunV2ServiceIn",
        "GoogleCloudRunV2ServiceOut": "_run_103_GoogleCloudRunV2ServiceOut",
        "GoogleCloudRunV2ListServicesResponseIn": "_run_104_GoogleCloudRunV2ListServicesResponseIn",
        "GoogleCloudRunV2ListServicesResponseOut": "_run_105_GoogleCloudRunV2ListServicesResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
    types["GoogleCloudRunV2ExecutionIn"] = t.struct(
        {"launchStage": t.string().optional()}
    ).named(renames["GoogleCloudRunV2ExecutionIn"])
    types["GoogleCloudRunV2ExecutionOut"] = t.struct(
        {
            "succeededCount": t.integer().optional(),
            "deleteTime": t.string().optional(),
            "runningCount": t.integer().optional(),
            "observedGeneration": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "taskCount": t.integer().optional(),
            "failedCount": t.integer().optional(),
            "retriedCount": t.integer().optional(),
            "job": t.string().optional(),
            "logUri": t.string().optional(),
            "uid": t.string().optional(),
            "etag": t.string().optional(),
            "cancelledCount": t.integer().optional(),
            "parallelism": t.integer().optional(),
            "startTime": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "satisfiesPzs": t.boolean().optional(),
            "conditions": t.array(
                t.proxy(renames["GoogleCloudRunV2ConditionOut"])
            ).optional(),
            "createTime": t.string().optional(),
            "template": t.proxy(renames["GoogleCloudRunV2TaskTemplateOut"]).optional(),
            "reconciling": t.boolean().optional(),
            "launchStage": t.string().optional(),
            "completionTime": t.string().optional(),
            "expireTime": t.string().optional(),
            "generation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2ExecutionOut"])
    types["GoogleLongrunningWaitOperationRequestIn"] = t.struct(
        {"timeout": t.string().optional()}
    ).named(renames["GoogleLongrunningWaitOperationRequestIn"])
    types["GoogleLongrunningWaitOperationRequestOut"] = t.struct(
        {
            "timeout": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleLongrunningWaitOperationRequestOut"])
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
    types["GoogleCloudRunV2TaskTemplateIn"] = t.struct(
        {
            "serviceAccount": t.string().optional(),
            "maxRetries": t.integer().optional(),
            "containers": t.array(
                t.proxy(renames["GoogleCloudRunV2ContainerIn"])
            ).optional(),
            "encryptionKey": t.string().optional(),
            "volumes": t.array(t.proxy(renames["GoogleCloudRunV2VolumeIn"])).optional(),
            "timeout": t.string().optional(),
            "executionEnvironment": t.string().optional(),
            "vpcAccess": t.proxy(renames["GoogleCloudRunV2VpcAccessIn"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2TaskTemplateIn"])
    types["GoogleCloudRunV2TaskTemplateOut"] = t.struct(
        {
            "serviceAccount": t.string().optional(),
            "maxRetries": t.integer().optional(),
            "containers": t.array(
                t.proxy(renames["GoogleCloudRunV2ContainerOut"])
            ).optional(),
            "encryptionKey": t.string().optional(),
            "volumes": t.array(
                t.proxy(renames["GoogleCloudRunV2VolumeOut"])
            ).optional(),
            "timeout": t.string().optional(),
            "executionEnvironment": t.string().optional(),
            "vpcAccess": t.proxy(renames["GoogleCloudRunV2VpcAccessOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2TaskTemplateOut"])
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
    types["GoogleIamV1TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["GoogleIamV1TestIamPermissionsRequestIn"])
    types["GoogleIamV1TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1TestIamPermissionsRequestOut"])
    types["GoogleCloudRunV2CloudSqlInstanceIn"] = t.struct(
        {"instances": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudRunV2CloudSqlInstanceIn"])
    types["GoogleCloudRunV2CloudSqlInstanceOut"] = t.struct(
        {
            "instances": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2CloudSqlInstanceOut"])
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
    types["GoogleIamV1PolicyIn"] = t.struct(
        {
            "auditConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditConfigIn"])
            ).optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["GoogleIamV1BindingIn"])).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["GoogleIamV1PolicyIn"])
    types["GoogleIamV1PolicyOut"] = t.struct(
        {
            "auditConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditConfigOut"])
            ).optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["GoogleIamV1BindingOut"])).optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1PolicyOut"])
    types["GoogleCloudRunV2VersionToPathIn"] = t.struct(
        {
            "path": t.string(),
            "version": t.string().optional(),
            "mode": t.integer().optional(),
        }
    ).named(renames["GoogleCloudRunV2VersionToPathIn"])
    types["GoogleCloudRunV2VersionToPathOut"] = t.struct(
        {
            "path": t.string(),
            "version": t.string().optional(),
            "mode": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2VersionToPathOut"])
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
    types["GoogleCloudRunV2TrafficTargetStatusIn"] = t.struct(
        {
            "type": t.string().optional(),
            "revision": t.string().optional(),
            "uri": t.string().optional(),
            "tag": t.string().optional(),
            "percent": t.integer().optional(),
        }
    ).named(renames["GoogleCloudRunV2TrafficTargetStatusIn"])
    types["GoogleCloudRunV2TrafficTargetStatusOut"] = t.struct(
        {
            "type": t.string().optional(),
            "revision": t.string().optional(),
            "uri": t.string().optional(),
            "tag": t.string().optional(),
            "percent": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2TrafficTargetStatusOut"])
    types["GoogleCloudRunV2ExecutionTemplateIn"] = t.struct(
        {
            "taskCount": t.integer().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "parallelism": t.integer().optional(),
            "template": t.proxy(renames["GoogleCloudRunV2TaskTemplateIn"]),
        }
    ).named(renames["GoogleCloudRunV2ExecutionTemplateIn"])
    types["GoogleCloudRunV2ExecutionTemplateOut"] = t.struct(
        {
            "taskCount": t.integer().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "parallelism": t.integer().optional(),
            "template": t.proxy(renames["GoogleCloudRunV2TaskTemplateOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2ExecutionTemplateOut"])
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
    types["GoogleCloudRunV2RevisionIn"] = t.struct(
        {
            "encryptionKey": t.string().optional(),
            "sessionAffinity": t.boolean().optional(),
            "scaling": t.proxy(renames["GoogleCloudRunV2RevisionScalingIn"]).optional(),
            "containers": t.array(
                t.proxy(renames["GoogleCloudRunV2ContainerIn"])
            ).optional(),
            "vpcAccess": t.proxy(renames["GoogleCloudRunV2VpcAccessIn"]).optional(),
            "volumes": t.array(t.proxy(renames["GoogleCloudRunV2VolumeIn"])).optional(),
            "encryptionKeyRevocationAction": t.string().optional(),
            "maxInstanceRequestConcurrency": t.integer().optional(),
            "executionEnvironment": t.string().optional(),
            "encryptionKeyShutdownDuration": t.string().optional(),
            "launchStage": t.string().optional(),
            "timeout": t.string().optional(),
            "serviceAccount": t.string().optional(),
        }
    ).named(renames["GoogleCloudRunV2RevisionIn"])
    types["GoogleCloudRunV2RevisionOut"] = t.struct(
        {
            "logUri": t.string().optional(),
            "encryptionKey": t.string().optional(),
            "sessionAffinity": t.boolean().optional(),
            "scaling": t.proxy(
                renames["GoogleCloudRunV2RevisionScalingOut"]
            ).optional(),
            "etag": t.string().optional(),
            "containers": t.array(
                t.proxy(renames["GoogleCloudRunV2ContainerOut"])
            ).optional(),
            "vpcAccess": t.proxy(renames["GoogleCloudRunV2VpcAccessOut"]).optional(),
            "volumes": t.array(
                t.proxy(renames["GoogleCloudRunV2VolumeOut"])
            ).optional(),
            "createTime": t.string().optional(),
            "satisfiesPzs": t.boolean().optional(),
            "encryptionKeyRevocationAction": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "expireTime": t.string().optional(),
            "deleteTime": t.string().optional(),
            "observedGeneration": t.string().optional(),
            "generation": t.string().optional(),
            "name": t.string().optional(),
            "reconciling": t.boolean().optional(),
            "maxInstanceRequestConcurrency": t.integer().optional(),
            "executionEnvironment": t.string().optional(),
            "uid": t.string().optional(),
            "encryptionKeyShutdownDuration": t.string().optional(),
            "launchStage": t.string().optional(),
            "updateTime": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "timeout": t.string().optional(),
            "service": t.string().optional(),
            "conditions": t.array(
                t.proxy(renames["GoogleCloudRunV2ConditionOut"])
            ).optional(),
            "serviceAccount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2RevisionOut"])
    types["GoogleCloudRunV2ConditionIn"] = t.struct(
        {
            "reason": t.string().optional(),
            "message": t.string().optional(),
            "lastTransitionTime": t.string().optional(),
            "revisionReason": t.string().optional(),
            "executionReason": t.string().optional(),
            "severity": t.string().optional(),
            "type": t.string().optional(),
            "state": t.string().optional(),
        }
    ).named(renames["GoogleCloudRunV2ConditionIn"])
    types["GoogleCloudRunV2ConditionOut"] = t.struct(
        {
            "reason": t.string().optional(),
            "message": t.string().optional(),
            "lastTransitionTime": t.string().optional(),
            "revisionReason": t.string().optional(),
            "executionReason": t.string().optional(),
            "severity": t.string().optional(),
            "type": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2ConditionOut"])
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
    types["GoogleCloudRunV2HTTPHeaderIn"] = t.struct(
        {"name": t.string(), "value": t.string().optional()}
    ).named(renames["GoogleCloudRunV2HTTPHeaderIn"])
    types["GoogleCloudRunV2HTTPHeaderOut"] = t.struct(
        {
            "name": t.string(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2HTTPHeaderOut"])
    types["GoogleCloudRunV2TaskIn"] = t.struct(
        {
            "maxRetries": t.integer().optional(),
            "containers": t.array(
                t.proxy(renames["GoogleCloudRunV2ContainerIn"])
            ).optional(),
            "timeout": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "executionEnvironment": t.string().optional(),
            "volumes": t.array(t.proxy(renames["GoogleCloudRunV2VolumeIn"])).optional(),
        }
    ).named(renames["GoogleCloudRunV2TaskIn"])
    types["GoogleCloudRunV2TaskOut"] = t.struct(
        {
            "maxRetries": t.integer().optional(),
            "index": t.integer().optional(),
            "updateTime": t.string().optional(),
            "etag": t.string().optional(),
            "containers": t.array(
                t.proxy(renames["GoogleCloudRunV2ContainerOut"])
            ).optional(),
            "timeout": t.string().optional(),
            "generation": t.string().optional(),
            "satisfiesPzs": t.boolean().optional(),
            "startTime": t.string().optional(),
            "encryptionKey": t.string().optional(),
            "name": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "executionEnvironment": t.string().optional(),
            "volumes": t.array(
                t.proxy(renames["GoogleCloudRunV2VolumeOut"])
            ).optional(),
            "vpcAccess": t.proxy(renames["GoogleCloudRunV2VpcAccessOut"]).optional(),
            "completionTime": t.string().optional(),
            "reconciling": t.boolean().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "lastAttemptResult": t.proxy(
                renames["GoogleCloudRunV2TaskAttemptResultOut"]
            ).optional(),
            "uid": t.string().optional(),
            "execution": t.string().optional(),
            "logUri": t.string().optional(),
            "deleteTime": t.string().optional(),
            "job": t.string().optional(),
            "retried": t.integer().optional(),
            "createTime": t.string().optional(),
            "conditions": t.array(
                t.proxy(renames["GoogleCloudRunV2ConditionOut"])
            ).optional(),
            "expireTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "observedGeneration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2TaskOut"])
    types["GoogleCloudRunV2RevisionTemplateIn"] = t.struct(
        {
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "serviceAccount": t.string().optional(),
            "executionEnvironment": t.string().optional(),
            "containers": t.array(
                t.proxy(renames["GoogleCloudRunV2ContainerIn"])
            ).optional(),
            "revision": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "encryptionKey": t.string().optional(),
            "vpcAccess": t.proxy(renames["GoogleCloudRunV2VpcAccessIn"]).optional(),
            "scaling": t.proxy(renames["GoogleCloudRunV2RevisionScalingIn"]).optional(),
            "timeout": t.string().optional(),
            "volumes": t.array(t.proxy(renames["GoogleCloudRunV2VolumeIn"])).optional(),
            "sessionAffinity": t.boolean().optional(),
            "maxInstanceRequestConcurrency": t.integer().optional(),
        }
    ).named(renames["GoogleCloudRunV2RevisionTemplateIn"])
    types["GoogleCloudRunV2RevisionTemplateOut"] = t.struct(
        {
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "serviceAccount": t.string().optional(),
            "executionEnvironment": t.string().optional(),
            "containers": t.array(
                t.proxy(renames["GoogleCloudRunV2ContainerOut"])
            ).optional(),
            "revision": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "encryptionKey": t.string().optional(),
            "vpcAccess": t.proxy(renames["GoogleCloudRunV2VpcAccessOut"]).optional(),
            "scaling": t.proxy(
                renames["GoogleCloudRunV2RevisionScalingOut"]
            ).optional(),
            "timeout": t.string().optional(),
            "volumes": t.array(
                t.proxy(renames["GoogleCloudRunV2VolumeOut"])
            ).optional(),
            "sessionAffinity": t.boolean().optional(),
            "maxInstanceRequestConcurrency": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2RevisionTemplateOut"])
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
    types["GoogleCloudRunV2ContainerIn"] = t.struct(
        {
            "name": t.string().optional(),
            "args": t.array(t.string()).optional(),
            "image": t.string(),
            "dependsOn": t.array(t.string()).optional(),
            "livenessProbe": t.proxy(renames["GoogleCloudRunV2ProbeIn"]).optional(),
            "startupProbe": t.proxy(renames["GoogleCloudRunV2ProbeIn"]).optional(),
            "ports": t.array(
                t.proxy(renames["GoogleCloudRunV2ContainerPortIn"])
            ).optional(),
            "env": t.array(t.proxy(renames["GoogleCloudRunV2EnvVarIn"])).optional(),
            "workingDir": t.string().optional(),
            "resources": t.proxy(
                renames["GoogleCloudRunV2ResourceRequirementsIn"]
            ).optional(),
            "volumeMounts": t.array(
                t.proxy(renames["GoogleCloudRunV2VolumeMountIn"])
            ).optional(),
            "command": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudRunV2ContainerIn"])
    types["GoogleCloudRunV2ContainerOut"] = t.struct(
        {
            "name": t.string().optional(),
            "args": t.array(t.string()).optional(),
            "image": t.string(),
            "dependsOn": t.array(t.string()).optional(),
            "livenessProbe": t.proxy(renames["GoogleCloudRunV2ProbeOut"]).optional(),
            "startupProbe": t.proxy(renames["GoogleCloudRunV2ProbeOut"]).optional(),
            "ports": t.array(
                t.proxy(renames["GoogleCloudRunV2ContainerPortOut"])
            ).optional(),
            "env": t.array(t.proxy(renames["GoogleCloudRunV2EnvVarOut"])).optional(),
            "workingDir": t.string().optional(),
            "resources": t.proxy(
                renames["GoogleCloudRunV2ResourceRequirementsOut"]
            ).optional(),
            "volumeMounts": t.array(
                t.proxy(renames["GoogleCloudRunV2VolumeMountOut"])
            ).optional(),
            "command": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2ContainerOut"])
    types["GoogleIamV1BindingIn"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["GoogleTypeExprIn"]).optional(),
            "role": t.string().optional(),
        }
    ).named(renames["GoogleIamV1BindingIn"])
    types["GoogleIamV1BindingOut"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["GoogleTypeExprOut"]).optional(),
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1BindingOut"])
    types["GoogleCloudRunV2TCPSocketActionIn"] = t.struct(
        {"port": t.integer().optional()}
    ).named(renames["GoogleCloudRunV2TCPSocketActionIn"])
    types["GoogleCloudRunV2TCPSocketActionOut"] = t.struct(
        {
            "port": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2TCPSocketActionOut"])
    types["GoogleCloudRunV2TrafficTargetIn"] = t.struct(
        {
            "tag": t.string().optional(),
            "revision": t.string().optional(),
            "percent": t.integer().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["GoogleCloudRunV2TrafficTargetIn"])
    types["GoogleCloudRunV2TrafficTargetOut"] = t.struct(
        {
            "tag": t.string().optional(),
            "revision": t.string().optional(),
            "percent": t.integer().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2TrafficTargetOut"])
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
    types["GoogleTypeExprIn"] = t.struct(
        {
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["GoogleTypeExprIn"])
    types["GoogleTypeExprOut"] = t.struct(
        {
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeExprOut"])
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
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
    types["GoogleCloudRunV2VpcAccessIn"] = t.struct(
        {"egress": t.string().optional(), "connector": t.string().optional()}
    ).named(renames["GoogleCloudRunV2VpcAccessIn"])
    types["GoogleCloudRunV2VpcAccessOut"] = t.struct(
        {
            "egress": t.string().optional(),
            "connector": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2VpcAccessOut"])
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
    types["GoogleCloudRunV2SecretVolumeSourceIn"] = t.struct(
        {
            "secret": t.string(),
            "items": t.array(
                t.proxy(renames["GoogleCloudRunV2VersionToPathIn"])
            ).optional(),
            "defaultMode": t.integer().optional(),
        }
    ).named(renames["GoogleCloudRunV2SecretVolumeSourceIn"])
    types["GoogleCloudRunV2SecretVolumeSourceOut"] = t.struct(
        {
            "secret": t.string(),
            "items": t.array(
                t.proxy(renames["GoogleCloudRunV2VersionToPathOut"])
            ).optional(),
            "defaultMode": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2SecretVolumeSourceOut"])
    types["GoogleCloudRunV2ListExecutionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "executions": t.array(
                t.proxy(renames["GoogleCloudRunV2ExecutionIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudRunV2ListExecutionsResponseIn"])
    types["GoogleCloudRunV2ListExecutionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "executions": t.array(
                t.proxy(renames["GoogleCloudRunV2ExecutionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2ListExecutionsResponseOut"])
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
    types["GoogleIamV1TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["GoogleIamV1TestIamPermissionsResponseIn"])
    types["GoogleIamV1TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1TestIamPermissionsResponseOut"])
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
    types["GoogleCloudRunV2ProbeIn"] = t.struct(
        {
            "initialDelaySeconds": t.integer().optional(),
            "failureThreshold": t.integer().optional(),
            "timeoutSeconds": t.integer().optional(),
            "httpGet": t.proxy(renames["GoogleCloudRunV2HTTPGetActionIn"]).optional(),
            "periodSeconds": t.integer().optional(),
            "grpc": t.proxy(renames["GoogleCloudRunV2GRPCActionIn"]).optional(),
            "tcpSocket": t.proxy(
                renames["GoogleCloudRunV2TCPSocketActionIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudRunV2ProbeIn"])
    types["GoogleCloudRunV2ProbeOut"] = t.struct(
        {
            "initialDelaySeconds": t.integer().optional(),
            "failureThreshold": t.integer().optional(),
            "timeoutSeconds": t.integer().optional(),
            "httpGet": t.proxy(renames["GoogleCloudRunV2HTTPGetActionOut"]).optional(),
            "periodSeconds": t.integer().optional(),
            "grpc": t.proxy(renames["GoogleCloudRunV2GRPCActionOut"]).optional(),
            "tcpSocket": t.proxy(
                renames["GoogleCloudRunV2TCPSocketActionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2ProbeOut"])
    types["GoogleIamV1SetIamPolicyRequestIn"] = t.struct(
        {
            "policy": t.proxy(renames["GoogleIamV1PolicyIn"]).optional(),
            "updateMask": t.string().optional(),
        }
    ).named(renames["GoogleIamV1SetIamPolicyRequestIn"])
    types["GoogleIamV1SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["GoogleIamV1PolicyOut"]).optional(),
            "updateMask": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1SetIamPolicyRequestOut"])
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
    types["GoogleCloudRunV2JobIn"] = t.struct(
        {
            "client": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "template": t.proxy(renames["GoogleCloudRunV2ExecutionTemplateIn"]),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "clientVersion": t.string().optional(),
            "binaryAuthorization": t.proxy(
                renames["GoogleCloudRunV2BinaryAuthorizationIn"]
            ).optional(),
            "name": t.string().optional(),
            "launchStage": t.string().optional(),
        }
    ).named(renames["GoogleCloudRunV2JobIn"])
    types["GoogleCloudRunV2JobOut"] = t.struct(
        {
            "client": t.string().optional(),
            "generation": t.string().optional(),
            "satisfiesPzs": t.boolean().optional(),
            "expireTime": t.string().optional(),
            "observedGeneration": t.string().optional(),
            "deleteTime": t.string().optional(),
            "lastModifier": t.string().optional(),
            "creator": t.string().optional(),
            "conditions": t.array(
                t.proxy(renames["GoogleCloudRunV2ConditionOut"])
            ).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "template": t.proxy(renames["GoogleCloudRunV2ExecutionTemplateOut"]),
            "uid": t.string().optional(),
            "latestCreatedExecution": t.proxy(
                renames["GoogleCloudRunV2ExecutionReferenceOut"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "clientVersion": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "binaryAuthorization": t.proxy(
                renames["GoogleCloudRunV2BinaryAuthorizationOut"]
            ).optional(),
            "name": t.string().optional(),
            "terminalCondition": t.proxy(
                renames["GoogleCloudRunV2ConditionOut"]
            ).optional(),
            "etag": t.string().optional(),
            "reconciling": t.boolean().optional(),
            "launchStage": t.string().optional(),
            "executionCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2JobOut"])
    types["GoogleCloudRunV2HTTPGetActionIn"] = t.struct(
        {
            "port": t.integer().optional(),
            "httpHeaders": t.array(
                t.proxy(renames["GoogleCloudRunV2HTTPHeaderIn"])
            ).optional(),
            "path": t.string().optional(),
        }
    ).named(renames["GoogleCloudRunV2HTTPGetActionIn"])
    types["GoogleCloudRunV2HTTPGetActionOut"] = t.struct(
        {
            "port": t.integer().optional(),
            "httpHeaders": t.array(
                t.proxy(renames["GoogleCloudRunV2HTTPHeaderOut"])
            ).optional(),
            "path": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2HTTPGetActionOut"])
    types["GoogleCloudRunV2ServiceIn"] = t.struct(
        {
            "ingress": t.string().optional(),
            "template": t.proxy(renames["GoogleCloudRunV2RevisionTemplateIn"]),
            "client": t.string().optional(),
            "name": t.string().optional(),
            "binaryAuthorization": t.proxy(
                renames["GoogleCloudRunV2BinaryAuthorizationIn"]
            ).optional(),
            "launchStage": t.string().optional(),
            "clientVersion": t.string().optional(),
            "customAudiences": t.array(t.string()).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "traffic": t.array(
                t.proxy(renames["GoogleCloudRunV2TrafficTargetIn"])
            ).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudRunV2ServiceIn"])
    types["GoogleCloudRunV2ServiceOut"] = t.struct(
        {
            "deleteTime": t.string().optional(),
            "ingress": t.string().optional(),
            "uid": t.string().optional(),
            "conditions": t.array(
                t.proxy(renames["GoogleCloudRunV2ConditionOut"])
            ).optional(),
            "updateTime": t.string().optional(),
            "terminalCondition": t.proxy(
                renames["GoogleCloudRunV2ConditionOut"]
            ).optional(),
            "template": t.proxy(renames["GoogleCloudRunV2RevisionTemplateOut"]),
            "latestCreatedRevision": t.string().optional(),
            "expireTime": t.string().optional(),
            "client": t.string().optional(),
            "reconciling": t.boolean().optional(),
            "satisfiesPzs": t.boolean().optional(),
            "observedGeneration": t.string().optional(),
            "uri": t.string().optional(),
            "name": t.string().optional(),
            "binaryAuthorization": t.proxy(
                renames["GoogleCloudRunV2BinaryAuthorizationOut"]
            ).optional(),
            "launchStage": t.string().optional(),
            "generation": t.string().optional(),
            "clientVersion": t.string().optional(),
            "customAudiences": t.array(t.string()).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "lastModifier": t.string().optional(),
            "trafficStatuses": t.array(
                t.proxy(renames["GoogleCloudRunV2TrafficTargetStatusOut"])
            ).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "traffic": t.array(
                t.proxy(renames["GoogleCloudRunV2TrafficTargetOut"])
            ).optional(),
            "description": t.string().optional(),
            "etag": t.string().optional(),
            "latestReadyRevision": t.string().optional(),
            "creator": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2ServiceOut"])
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

    functions = {}
    functions["projectsLocationsJobsGetIamPolicy"] = run.patch(
        "v2/{name}",
        t.struct(
            {
                "allowMissing": t.boolean().optional(),
                "name": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "client": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "template": t.proxy(renames["GoogleCloudRunV2ExecutionTemplateIn"]),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "clientVersion": t.string().optional(),
                "binaryAuthorization": t.proxy(
                    renames["GoogleCloudRunV2BinaryAuthorizationIn"]
                ).optional(),
                "launchStage": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsList"] = run.patch(
        "v2/{name}",
        t.struct(
            {
                "allowMissing": t.boolean().optional(),
                "name": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "client": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "template": t.proxy(renames["GoogleCloudRunV2ExecutionTemplateIn"]),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "clientVersion": t.string().optional(),
                "binaryAuthorization": t.proxy(
                    renames["GoogleCloudRunV2BinaryAuthorizationIn"]
                ).optional(),
                "launchStage": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsCreate"] = run.patch(
        "v2/{name}",
        t.struct(
            {
                "allowMissing": t.boolean().optional(),
                "name": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "client": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "template": t.proxy(renames["GoogleCloudRunV2ExecutionTemplateIn"]),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "clientVersion": t.string().optional(),
                "binaryAuthorization": t.proxy(
                    renames["GoogleCloudRunV2BinaryAuthorizationIn"]
                ).optional(),
                "launchStage": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsTestIamPermissions"] = run.patch(
        "v2/{name}",
        t.struct(
            {
                "allowMissing": t.boolean().optional(),
                "name": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "client": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "template": t.proxy(renames["GoogleCloudRunV2ExecutionTemplateIn"]),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "clientVersion": t.string().optional(),
                "binaryAuthorization": t.proxy(
                    renames["GoogleCloudRunV2BinaryAuthorizationIn"]
                ).optional(),
                "launchStage": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsSetIamPolicy"] = run.patch(
        "v2/{name}",
        t.struct(
            {
                "allowMissing": t.boolean().optional(),
                "name": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "client": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "template": t.proxy(renames["GoogleCloudRunV2ExecutionTemplateIn"]),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "clientVersion": t.string().optional(),
                "binaryAuthorization": t.proxy(
                    renames["GoogleCloudRunV2BinaryAuthorizationIn"]
                ).optional(),
                "launchStage": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsDelete"] = run.patch(
        "v2/{name}",
        t.struct(
            {
                "allowMissing": t.boolean().optional(),
                "name": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "client": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "template": t.proxy(renames["GoogleCloudRunV2ExecutionTemplateIn"]),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "clientVersion": t.string().optional(),
                "binaryAuthorization": t.proxy(
                    renames["GoogleCloudRunV2BinaryAuthorizationIn"]
                ).optional(),
                "launchStage": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsGet"] = run.patch(
        "v2/{name}",
        t.struct(
            {
                "allowMissing": t.boolean().optional(),
                "name": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "client": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "template": t.proxy(renames["GoogleCloudRunV2ExecutionTemplateIn"]),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "clientVersion": t.string().optional(),
                "binaryAuthorization": t.proxy(
                    renames["GoogleCloudRunV2BinaryAuthorizationIn"]
                ).optional(),
                "launchStage": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsRun"] = run.patch(
        "v2/{name}",
        t.struct(
            {
                "allowMissing": t.boolean().optional(),
                "name": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "client": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "template": t.proxy(renames["GoogleCloudRunV2ExecutionTemplateIn"]),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "clientVersion": t.string().optional(),
                "binaryAuthorization": t.proxy(
                    renames["GoogleCloudRunV2BinaryAuthorizationIn"]
                ).optional(),
                "launchStage": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsPatch"] = run.patch(
        "v2/{name}",
        t.struct(
            {
                "allowMissing": t.boolean().optional(),
                "name": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "client": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "template": t.proxy(renames["GoogleCloudRunV2ExecutionTemplateIn"]),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "clientVersion": t.string().optional(),
                "binaryAuthorization": t.proxy(
                    renames["GoogleCloudRunV2BinaryAuthorizationIn"]
                ).optional(),
                "launchStage": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsExecutionsList"] = run.delete(
        "v2/{name}",
        t.struct(
            {
                "etag": t.string().optional(),
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
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
                "etag": t.string().optional(),
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
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
                "etag": t.string().optional(),
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
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
    functions["projectsLocationsServicesList"] = run.post(
        "v2/{parent}/services",
        t.struct(
            {
                "serviceId": t.string(),
                "validateOnly": t.boolean().optional(),
                "parent": t.string(),
                "ingress": t.string().optional(),
                "template": t.proxy(renames["GoogleCloudRunV2RevisionTemplateIn"]),
                "client": t.string().optional(),
                "name": t.string().optional(),
                "binaryAuthorization": t.proxy(
                    renames["GoogleCloudRunV2BinaryAuthorizationIn"]
                ).optional(),
                "launchStage": t.string().optional(),
                "clientVersion": t.string().optional(),
                "customAudiences": t.array(t.string()).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "traffic": t.array(
                    t.proxy(renames["GoogleCloudRunV2TrafficTargetIn"])
                ).optional(),
                "description": t.string().optional(),
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
                "serviceId": t.string(),
                "validateOnly": t.boolean().optional(),
                "parent": t.string(),
                "ingress": t.string().optional(),
                "template": t.proxy(renames["GoogleCloudRunV2RevisionTemplateIn"]),
                "client": t.string().optional(),
                "name": t.string().optional(),
                "binaryAuthorization": t.proxy(
                    renames["GoogleCloudRunV2BinaryAuthorizationIn"]
                ).optional(),
                "launchStage": t.string().optional(),
                "clientVersion": t.string().optional(),
                "customAudiences": t.array(t.string()).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "traffic": t.array(
                    t.proxy(renames["GoogleCloudRunV2TrafficTargetIn"])
                ).optional(),
                "description": t.string().optional(),
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
                "serviceId": t.string(),
                "validateOnly": t.boolean().optional(),
                "parent": t.string(),
                "ingress": t.string().optional(),
                "template": t.proxy(renames["GoogleCloudRunV2RevisionTemplateIn"]),
                "client": t.string().optional(),
                "name": t.string().optional(),
                "binaryAuthorization": t.proxy(
                    renames["GoogleCloudRunV2BinaryAuthorizationIn"]
                ).optional(),
                "launchStage": t.string().optional(),
                "clientVersion": t.string().optional(),
                "customAudiences": t.array(t.string()).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "traffic": t.array(
                    t.proxy(renames["GoogleCloudRunV2TrafficTargetIn"])
                ).optional(),
                "description": t.string().optional(),
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
                "serviceId": t.string(),
                "validateOnly": t.boolean().optional(),
                "parent": t.string(),
                "ingress": t.string().optional(),
                "template": t.proxy(renames["GoogleCloudRunV2RevisionTemplateIn"]),
                "client": t.string().optional(),
                "name": t.string().optional(),
                "binaryAuthorization": t.proxy(
                    renames["GoogleCloudRunV2BinaryAuthorizationIn"]
                ).optional(),
                "launchStage": t.string().optional(),
                "clientVersion": t.string().optional(),
                "customAudiences": t.array(t.string()).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "traffic": t.array(
                    t.proxy(renames["GoogleCloudRunV2TrafficTargetIn"])
                ).optional(),
                "description": t.string().optional(),
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
                "serviceId": t.string(),
                "validateOnly": t.boolean().optional(),
                "parent": t.string(),
                "ingress": t.string().optional(),
                "template": t.proxy(renames["GoogleCloudRunV2RevisionTemplateIn"]),
                "client": t.string().optional(),
                "name": t.string().optional(),
                "binaryAuthorization": t.proxy(
                    renames["GoogleCloudRunV2BinaryAuthorizationIn"]
                ).optional(),
                "launchStage": t.string().optional(),
                "clientVersion": t.string().optional(),
                "customAudiences": t.array(t.string()).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "traffic": t.array(
                    t.proxy(renames["GoogleCloudRunV2TrafficTargetIn"])
                ).optional(),
                "description": t.string().optional(),
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
                "serviceId": t.string(),
                "validateOnly": t.boolean().optional(),
                "parent": t.string(),
                "ingress": t.string().optional(),
                "template": t.proxy(renames["GoogleCloudRunV2RevisionTemplateIn"]),
                "client": t.string().optional(),
                "name": t.string().optional(),
                "binaryAuthorization": t.proxy(
                    renames["GoogleCloudRunV2BinaryAuthorizationIn"]
                ).optional(),
                "launchStage": t.string().optional(),
                "clientVersion": t.string().optional(),
                "customAudiences": t.array(t.string()).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "traffic": t.array(
                    t.proxy(renames["GoogleCloudRunV2TrafficTargetIn"])
                ).optional(),
                "description": t.string().optional(),
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
                "serviceId": t.string(),
                "validateOnly": t.boolean().optional(),
                "parent": t.string(),
                "ingress": t.string().optional(),
                "template": t.proxy(renames["GoogleCloudRunV2RevisionTemplateIn"]),
                "client": t.string().optional(),
                "name": t.string().optional(),
                "binaryAuthorization": t.proxy(
                    renames["GoogleCloudRunV2BinaryAuthorizationIn"]
                ).optional(),
                "launchStage": t.string().optional(),
                "clientVersion": t.string().optional(),
                "customAudiences": t.array(t.string()).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "traffic": t.array(
                    t.proxy(renames["GoogleCloudRunV2TrafficTargetIn"])
                ).optional(),
                "description": t.string().optional(),
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
                "serviceId": t.string(),
                "validateOnly": t.boolean().optional(),
                "parent": t.string(),
                "ingress": t.string().optional(),
                "template": t.proxy(renames["GoogleCloudRunV2RevisionTemplateIn"]),
                "client": t.string().optional(),
                "name": t.string().optional(),
                "binaryAuthorization": t.proxy(
                    renames["GoogleCloudRunV2BinaryAuthorizationIn"]
                ).optional(),
                "launchStage": t.string().optional(),
                "clientVersion": t.string().optional(),
                "customAudiences": t.array(t.string()).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "traffic": t.array(
                    t.proxy(renames["GoogleCloudRunV2TrafficTargetIn"])
                ).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesRevisionsDelete"] = run.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRunV2RevisionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesRevisionsList"] = run.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRunV2RevisionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesRevisionsGet"] = run.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRunV2RevisionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = run.get(
        "v2/{name}/operations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string(),
                "filter": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsWait"] = run.get(
        "v2/{name}/operations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string(),
                "filter": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="run", renames=renames, types=Box(types), functions=Box(functions)
    )
