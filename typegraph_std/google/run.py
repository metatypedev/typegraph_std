from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_run() -> Import:
    run = HTTPRuntime("https://run.googleapis.com/")

    renames = {
        "ErrorResponse": "_run_1_ErrorResponse",
        "GoogleCloudRunV2VersionToPathIn": "_run_2_GoogleCloudRunV2VersionToPathIn",
        "GoogleCloudRunV2VersionToPathOut": "_run_3_GoogleCloudRunV2VersionToPathOut",
        "GoogleCloudRunV2VpcAccessIn": "_run_4_GoogleCloudRunV2VpcAccessIn",
        "GoogleCloudRunV2VpcAccessOut": "_run_5_GoogleCloudRunV2VpcAccessOut",
        "GoogleCloudRunV2CloudSqlInstanceIn": "_run_6_GoogleCloudRunV2CloudSqlInstanceIn",
        "GoogleCloudRunV2CloudSqlInstanceOut": "_run_7_GoogleCloudRunV2CloudSqlInstanceOut",
        "GoogleCloudRunV2SecretKeySelectorIn": "_run_8_GoogleCloudRunV2SecretKeySelectorIn",
        "GoogleCloudRunV2SecretKeySelectorOut": "_run_9_GoogleCloudRunV2SecretKeySelectorOut",
        "GoogleCloudRunV2RevisionScalingIn": "_run_10_GoogleCloudRunV2RevisionScalingIn",
        "GoogleCloudRunV2RevisionScalingOut": "_run_11_GoogleCloudRunV2RevisionScalingOut",
        "GoogleCloudRunV2ListJobsResponseIn": "_run_12_GoogleCloudRunV2ListJobsResponseIn",
        "GoogleCloudRunV2ListJobsResponseOut": "_run_13_GoogleCloudRunV2ListJobsResponseOut",
        "GoogleLongrunningOperationIn": "_run_14_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_run_15_GoogleLongrunningOperationOut",
        "GoogleCloudRunV2ListRevisionsResponseIn": "_run_16_GoogleCloudRunV2ListRevisionsResponseIn",
        "GoogleCloudRunV2ListRevisionsResponseOut": "_run_17_GoogleCloudRunV2ListRevisionsResponseOut",
        "GoogleIamV1BindingIn": "_run_18_GoogleIamV1BindingIn",
        "GoogleIamV1BindingOut": "_run_19_GoogleIamV1BindingOut",
        "GoogleCloudRunV2RevisionTemplateIn": "_run_20_GoogleCloudRunV2RevisionTemplateIn",
        "GoogleCloudRunV2RevisionTemplateOut": "_run_21_GoogleCloudRunV2RevisionTemplateOut",
        "GoogleTypeExprIn": "_run_22_GoogleTypeExprIn",
        "GoogleTypeExprOut": "_run_23_GoogleTypeExprOut",
        "GoogleLongrunningListOperationsResponseIn": "_run_24_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_run_25_GoogleLongrunningListOperationsResponseOut",
        "GoogleLongrunningWaitOperationRequestIn": "_run_26_GoogleLongrunningWaitOperationRequestIn",
        "GoogleLongrunningWaitOperationRequestOut": "_run_27_GoogleLongrunningWaitOperationRequestOut",
        "GoogleCloudRunV2ExecutionReferenceIn": "_run_28_GoogleCloudRunV2ExecutionReferenceIn",
        "GoogleCloudRunV2ExecutionReferenceOut": "_run_29_GoogleCloudRunV2ExecutionReferenceOut",
        "GoogleIamV1SetIamPolicyRequestIn": "_run_30_GoogleIamV1SetIamPolicyRequestIn",
        "GoogleIamV1SetIamPolicyRequestOut": "_run_31_GoogleIamV1SetIamPolicyRequestOut",
        "GoogleCloudRunV2JobIn": "_run_32_GoogleCloudRunV2JobIn",
        "GoogleCloudRunV2JobOut": "_run_33_GoogleCloudRunV2JobOut",
        "GoogleIamV1AuditConfigIn": "_run_34_GoogleIamV1AuditConfigIn",
        "GoogleIamV1AuditConfigOut": "_run_35_GoogleIamV1AuditConfigOut",
        "GoogleCloudRunV2ListServicesResponseIn": "_run_36_GoogleCloudRunV2ListServicesResponseIn",
        "GoogleCloudRunV2ListServicesResponseOut": "_run_37_GoogleCloudRunV2ListServicesResponseOut",
        "GoogleCloudRunV2BinaryAuthorizationIn": "_run_38_GoogleCloudRunV2BinaryAuthorizationIn",
        "GoogleCloudRunV2BinaryAuthorizationOut": "_run_39_GoogleCloudRunV2BinaryAuthorizationOut",
        "GoogleCloudRunV2ProbeIn": "_run_40_GoogleCloudRunV2ProbeIn",
        "GoogleCloudRunV2ProbeOut": "_run_41_GoogleCloudRunV2ProbeOut",
        "GoogleCloudRunV2RunJobRequestIn": "_run_42_GoogleCloudRunV2RunJobRequestIn",
        "GoogleCloudRunV2RunJobRequestOut": "_run_43_GoogleCloudRunV2RunJobRequestOut",
        "GoogleCloudRunV2VolumeIn": "_run_44_GoogleCloudRunV2VolumeIn",
        "GoogleCloudRunV2VolumeOut": "_run_45_GoogleCloudRunV2VolumeOut",
        "GoogleCloudRunV2ConditionIn": "_run_46_GoogleCloudRunV2ConditionIn",
        "GoogleCloudRunV2ConditionOut": "_run_47_GoogleCloudRunV2ConditionOut",
        "GoogleCloudRunV2TaskTemplateIn": "_run_48_GoogleCloudRunV2TaskTemplateIn",
        "GoogleCloudRunV2TaskTemplateOut": "_run_49_GoogleCloudRunV2TaskTemplateOut",
        "GoogleCloudRunV2ListTasksResponseIn": "_run_50_GoogleCloudRunV2ListTasksResponseIn",
        "GoogleCloudRunV2ListTasksResponseOut": "_run_51_GoogleCloudRunV2ListTasksResponseOut",
        "GoogleCloudRunV2GRPCActionIn": "_run_52_GoogleCloudRunV2GRPCActionIn",
        "GoogleCloudRunV2GRPCActionOut": "_run_53_GoogleCloudRunV2GRPCActionOut",
        "GoogleCloudRunV2EnvVarIn": "_run_54_GoogleCloudRunV2EnvVarIn",
        "GoogleCloudRunV2EnvVarOut": "_run_55_GoogleCloudRunV2EnvVarOut",
        "GoogleCloudRunV2ContainerPortIn": "_run_56_GoogleCloudRunV2ContainerPortIn",
        "GoogleCloudRunV2ContainerPortOut": "_run_57_GoogleCloudRunV2ContainerPortOut",
        "GoogleCloudRunV2TaskAttemptResultIn": "_run_58_GoogleCloudRunV2TaskAttemptResultIn",
        "GoogleCloudRunV2TaskAttemptResultOut": "_run_59_GoogleCloudRunV2TaskAttemptResultOut",
        "GoogleCloudRunV2ResourceRequirementsIn": "_run_60_GoogleCloudRunV2ResourceRequirementsIn",
        "GoogleCloudRunV2ResourceRequirementsOut": "_run_61_GoogleCloudRunV2ResourceRequirementsOut",
        "GoogleIamV1TestIamPermissionsRequestIn": "_run_62_GoogleIamV1TestIamPermissionsRequestIn",
        "GoogleIamV1TestIamPermissionsRequestOut": "_run_63_GoogleIamV1TestIamPermissionsRequestOut",
        "GoogleCloudRunV2TaskIn": "_run_64_GoogleCloudRunV2TaskIn",
        "GoogleCloudRunV2TaskOut": "_run_65_GoogleCloudRunV2TaskOut",
        "GoogleCloudRunV2ContainerIn": "_run_66_GoogleCloudRunV2ContainerIn",
        "GoogleCloudRunV2ContainerOut": "_run_67_GoogleCloudRunV2ContainerOut",
        "GoogleRpcStatusIn": "_run_68_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_run_69_GoogleRpcStatusOut",
        "GoogleCloudRunV2EmptyDirVolumeSourceIn": "_run_70_GoogleCloudRunV2EmptyDirVolumeSourceIn",
        "GoogleCloudRunV2EmptyDirVolumeSourceOut": "_run_71_GoogleCloudRunV2EmptyDirVolumeSourceOut",
        "GoogleCloudRunV2HTTPHeaderIn": "_run_72_GoogleCloudRunV2HTTPHeaderIn",
        "GoogleCloudRunV2HTTPHeaderOut": "_run_73_GoogleCloudRunV2HTTPHeaderOut",
        "GoogleCloudRunV2TrafficTargetStatusIn": "_run_74_GoogleCloudRunV2TrafficTargetStatusIn",
        "GoogleCloudRunV2TrafficTargetStatusOut": "_run_75_GoogleCloudRunV2TrafficTargetStatusOut",
        "GoogleCloudRunV2ServiceIn": "_run_76_GoogleCloudRunV2ServiceIn",
        "GoogleCloudRunV2ServiceOut": "_run_77_GoogleCloudRunV2ServiceOut",
        "GoogleCloudRunV2RevisionIn": "_run_78_GoogleCloudRunV2RevisionIn",
        "GoogleCloudRunV2RevisionOut": "_run_79_GoogleCloudRunV2RevisionOut",
        "GoogleCloudRunV2TrafficTargetIn": "_run_80_GoogleCloudRunV2TrafficTargetIn",
        "GoogleCloudRunV2TrafficTargetOut": "_run_81_GoogleCloudRunV2TrafficTargetOut",
        "GoogleIamV1PolicyIn": "_run_82_GoogleIamV1PolicyIn",
        "GoogleIamV1PolicyOut": "_run_83_GoogleIamV1PolicyOut",
        "GoogleCloudRunV2ExecutionIn": "_run_84_GoogleCloudRunV2ExecutionIn",
        "GoogleCloudRunV2ExecutionOut": "_run_85_GoogleCloudRunV2ExecutionOut",
        "GoogleCloudRunV2VolumeMountIn": "_run_86_GoogleCloudRunV2VolumeMountIn",
        "GoogleCloudRunV2VolumeMountOut": "_run_87_GoogleCloudRunV2VolumeMountOut",
        "GoogleCloudRunV2ExecutionTemplateIn": "_run_88_GoogleCloudRunV2ExecutionTemplateIn",
        "GoogleCloudRunV2ExecutionTemplateOut": "_run_89_GoogleCloudRunV2ExecutionTemplateOut",
        "GoogleProtobufEmptyIn": "_run_90_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_run_91_GoogleProtobufEmptyOut",
        "GoogleCloudRunV2TCPSocketActionIn": "_run_92_GoogleCloudRunV2TCPSocketActionIn",
        "GoogleCloudRunV2TCPSocketActionOut": "_run_93_GoogleCloudRunV2TCPSocketActionOut",
        "GoogleIamV1AuditLogConfigIn": "_run_94_GoogleIamV1AuditLogConfigIn",
        "GoogleIamV1AuditLogConfigOut": "_run_95_GoogleIamV1AuditLogConfigOut",
        "GoogleCloudRunV2SecretVolumeSourceIn": "_run_96_GoogleCloudRunV2SecretVolumeSourceIn",
        "GoogleCloudRunV2SecretVolumeSourceOut": "_run_97_GoogleCloudRunV2SecretVolumeSourceOut",
        "GoogleCloudRunV2ListExecutionsResponseIn": "_run_98_GoogleCloudRunV2ListExecutionsResponseIn",
        "GoogleCloudRunV2ListExecutionsResponseOut": "_run_99_GoogleCloudRunV2ListExecutionsResponseOut",
        "GoogleIamV1TestIamPermissionsResponseIn": "_run_100_GoogleIamV1TestIamPermissionsResponseIn",
        "GoogleIamV1TestIamPermissionsResponseOut": "_run_101_GoogleIamV1TestIamPermissionsResponseOut",
        "GoogleCloudRunV2HTTPGetActionIn": "_run_102_GoogleCloudRunV2HTTPGetActionIn",
        "GoogleCloudRunV2HTTPGetActionOut": "_run_103_GoogleCloudRunV2HTTPGetActionOut",
        "GoogleCloudRunV2EnvVarSourceIn": "_run_104_GoogleCloudRunV2EnvVarSourceIn",
        "GoogleCloudRunV2EnvVarSourceOut": "_run_105_GoogleCloudRunV2EnvVarSourceOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudRunV2VersionToPathIn"] = t.struct(
        {
            "version": t.string().optional(),
            "mode": t.integer().optional(),
            "path": t.string(),
        }
    ).named(renames["GoogleCloudRunV2VersionToPathIn"])
    types["GoogleCloudRunV2VersionToPathOut"] = t.struct(
        {
            "version": t.string().optional(),
            "mode": t.integer().optional(),
            "path": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2VersionToPathOut"])
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
    types["GoogleCloudRunV2CloudSqlInstanceIn"] = t.struct(
        {"instances": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudRunV2CloudSqlInstanceIn"])
    types["GoogleCloudRunV2CloudSqlInstanceOut"] = t.struct(
        {
            "instances": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2CloudSqlInstanceOut"])
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
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
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
    types["GoogleIamV1BindingIn"] = t.struct(
        {
            "role": t.string().optional(),
            "condition": t.proxy(renames["GoogleTypeExprIn"]).optional(),
            "members": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleIamV1BindingIn"])
    types["GoogleIamV1BindingOut"] = t.struct(
        {
            "role": t.string().optional(),
            "condition": t.proxy(renames["GoogleTypeExprOut"]).optional(),
            "members": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1BindingOut"])
    types["GoogleCloudRunV2RevisionTemplateIn"] = t.struct(
        {
            "executionEnvironment": t.string().optional(),
            "sessionAffinity": t.boolean().optional(),
            "vpcAccess": t.proxy(renames["GoogleCloudRunV2VpcAccessIn"]).optional(),
            "volumes": t.array(t.proxy(renames["GoogleCloudRunV2VolumeIn"])).optional(),
            "timeout": t.string().optional(),
            "maxInstanceRequestConcurrency": t.integer().optional(),
            "encryptionKey": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "revision": t.string().optional(),
            "scaling": t.proxy(renames["GoogleCloudRunV2RevisionScalingIn"]).optional(),
            "containers": t.array(
                t.proxy(renames["GoogleCloudRunV2ContainerIn"])
            ).optional(),
            "serviceAccount": t.string().optional(),
        }
    ).named(renames["GoogleCloudRunV2RevisionTemplateIn"])
    types["GoogleCloudRunV2RevisionTemplateOut"] = t.struct(
        {
            "executionEnvironment": t.string().optional(),
            "sessionAffinity": t.boolean().optional(),
            "vpcAccess": t.proxy(renames["GoogleCloudRunV2VpcAccessOut"]).optional(),
            "volumes": t.array(
                t.proxy(renames["GoogleCloudRunV2VolumeOut"])
            ).optional(),
            "timeout": t.string().optional(),
            "maxInstanceRequestConcurrency": t.integer().optional(),
            "encryptionKey": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "revision": t.string().optional(),
            "scaling": t.proxy(
                renames["GoogleCloudRunV2RevisionScalingOut"]
            ).optional(),
            "containers": t.array(
                t.proxy(renames["GoogleCloudRunV2ContainerOut"])
            ).optional(),
            "serviceAccount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2RevisionTemplateOut"])
    types["GoogleTypeExprIn"] = t.struct(
        {
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["GoogleTypeExprIn"])
    types["GoogleTypeExprOut"] = t.struct(
        {
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeExprOut"])
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
    types["GoogleLongrunningWaitOperationRequestIn"] = t.struct(
        {"timeout": t.string().optional()}
    ).named(renames["GoogleLongrunningWaitOperationRequestIn"])
    types["GoogleLongrunningWaitOperationRequestOut"] = t.struct(
        {
            "timeout": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleLongrunningWaitOperationRequestOut"])
    types["GoogleCloudRunV2ExecutionReferenceIn"] = t.struct(
        {
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "completionTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudRunV2ExecutionReferenceIn"])
    types["GoogleCloudRunV2ExecutionReferenceOut"] = t.struct(
        {
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "completionTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2ExecutionReferenceOut"])
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
    types["GoogleCloudRunV2JobIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "client": t.string().optional(),
            "launchStage": t.string().optional(),
            "name": t.string().optional(),
            "binaryAuthorization": t.proxy(
                renames["GoogleCloudRunV2BinaryAuthorizationIn"]
            ).optional(),
            "clientVersion": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "template": t.proxy(renames["GoogleCloudRunV2ExecutionTemplateIn"]),
        }
    ).named(renames["GoogleCloudRunV2JobIn"])
    types["GoogleCloudRunV2JobOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "observedGeneration": t.string().optional(),
            "client": t.string().optional(),
            "conditions": t.array(
                t.proxy(renames["GoogleCloudRunV2ConditionOut"])
            ).optional(),
            "deleteTime": t.string().optional(),
            "expireTime": t.string().optional(),
            "terminalCondition": t.proxy(
                renames["GoogleCloudRunV2ConditionOut"]
            ).optional(),
            "etag": t.string().optional(),
            "reconciling": t.boolean().optional(),
            "launchStage": t.string().optional(),
            "name": t.string().optional(),
            "binaryAuthorization": t.proxy(
                renames["GoogleCloudRunV2BinaryAuthorizationOut"]
            ).optional(),
            "satisfiesPzs": t.boolean().optional(),
            "generation": t.string().optional(),
            "clientVersion": t.string().optional(),
            "creator": t.string().optional(),
            "latestCreatedExecution": t.proxy(
                renames["GoogleCloudRunV2ExecutionReferenceOut"]
            ).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "uid": t.string().optional(),
            "template": t.proxy(renames["GoogleCloudRunV2ExecutionTemplateOut"]),
            "executionCount": t.integer().optional(),
            "createTime": t.string().optional(),
            "lastModifier": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2JobOut"])
    types["GoogleIamV1AuditConfigIn"] = t.struct(
        {
            "service": t.string().optional(),
            "auditLogConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditLogConfigIn"])
            ).optional(),
        }
    ).named(renames["GoogleIamV1AuditConfigIn"])
    types["GoogleIamV1AuditConfigOut"] = t.struct(
        {
            "service": t.string().optional(),
            "auditLogConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditLogConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1AuditConfigOut"])
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
    types["GoogleCloudRunV2ProbeIn"] = t.struct(
        {
            "failureThreshold": t.integer().optional(),
            "periodSeconds": t.integer().optional(),
            "initialDelaySeconds": t.integer().optional(),
            "httpGet": t.proxy(renames["GoogleCloudRunV2HTTPGetActionIn"]).optional(),
            "tcpSocket": t.proxy(
                renames["GoogleCloudRunV2TCPSocketActionIn"]
            ).optional(),
            "timeoutSeconds": t.integer().optional(),
            "grpc": t.proxy(renames["GoogleCloudRunV2GRPCActionIn"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2ProbeIn"])
    types["GoogleCloudRunV2ProbeOut"] = t.struct(
        {
            "failureThreshold": t.integer().optional(),
            "periodSeconds": t.integer().optional(),
            "initialDelaySeconds": t.integer().optional(),
            "httpGet": t.proxy(renames["GoogleCloudRunV2HTTPGetActionOut"]).optional(),
            "tcpSocket": t.proxy(
                renames["GoogleCloudRunV2TCPSocketActionOut"]
            ).optional(),
            "timeoutSeconds": t.integer().optional(),
            "grpc": t.proxy(renames["GoogleCloudRunV2GRPCActionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2ProbeOut"])
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
    types["GoogleCloudRunV2ConditionIn"] = t.struct(
        {
            "message": t.string().optional(),
            "revisionReason": t.string().optional(),
            "state": t.string().optional(),
            "lastTransitionTime": t.string().optional(),
            "type": t.string().optional(),
            "executionReason": t.string().optional(),
            "severity": t.string().optional(),
            "reason": t.string().optional(),
        }
    ).named(renames["GoogleCloudRunV2ConditionIn"])
    types["GoogleCloudRunV2ConditionOut"] = t.struct(
        {
            "message": t.string().optional(),
            "revisionReason": t.string().optional(),
            "state": t.string().optional(),
            "lastTransitionTime": t.string().optional(),
            "type": t.string().optional(),
            "executionReason": t.string().optional(),
            "severity": t.string().optional(),
            "reason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2ConditionOut"])
    types["GoogleCloudRunV2TaskTemplateIn"] = t.struct(
        {
            "containers": t.array(
                t.proxy(renames["GoogleCloudRunV2ContainerIn"])
            ).optional(),
            "serviceAccount": t.string().optional(),
            "maxRetries": t.integer().optional(),
            "vpcAccess": t.proxy(renames["GoogleCloudRunV2VpcAccessIn"]).optional(),
            "timeout": t.string().optional(),
            "executionEnvironment": t.string().optional(),
            "encryptionKey": t.string().optional(),
            "volumes": t.array(t.proxy(renames["GoogleCloudRunV2VolumeIn"])).optional(),
        }
    ).named(renames["GoogleCloudRunV2TaskTemplateIn"])
    types["GoogleCloudRunV2TaskTemplateOut"] = t.struct(
        {
            "containers": t.array(
                t.proxy(renames["GoogleCloudRunV2ContainerOut"])
            ).optional(),
            "serviceAccount": t.string().optional(),
            "maxRetries": t.integer().optional(),
            "vpcAccess": t.proxy(renames["GoogleCloudRunV2VpcAccessOut"]).optional(),
            "timeout": t.string().optional(),
            "executionEnvironment": t.string().optional(),
            "encryptionKey": t.string().optional(),
            "volumes": t.array(
                t.proxy(renames["GoogleCloudRunV2VolumeOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2TaskTemplateOut"])
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
    types["GoogleCloudRunV2TaskIn"] = t.struct(
        {
            "executionEnvironment": t.string().optional(),
            "maxRetries": t.integer().optional(),
            "containers": t.array(
                t.proxy(renames["GoogleCloudRunV2ContainerIn"])
            ).optional(),
            "timeout": t.string().optional(),
            "volumes": t.array(t.proxy(renames["GoogleCloudRunV2VolumeIn"])).optional(),
            "serviceAccount": t.string().optional(),
        }
    ).named(renames["GoogleCloudRunV2TaskIn"])
    types["GoogleCloudRunV2TaskOut"] = t.struct(
        {
            "expireTime": t.string().optional(),
            "etag": t.string().optional(),
            "completionTime": t.string().optional(),
            "job": t.string().optional(),
            "updateTime": t.string().optional(),
            "retried": t.integer().optional(),
            "startTime": t.string().optional(),
            "observedGeneration": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "logUri": t.string().optional(),
            "conditions": t.array(
                t.proxy(renames["GoogleCloudRunV2ConditionOut"])
            ).optional(),
            "uid": t.string().optional(),
            "lastAttemptResult": t.proxy(
                renames["GoogleCloudRunV2TaskAttemptResultOut"]
            ).optional(),
            "vpcAccess": t.proxy(renames["GoogleCloudRunV2VpcAccessOut"]).optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "generation": t.string().optional(),
            "executionEnvironment": t.string().optional(),
            "execution": t.string().optional(),
            "maxRetries": t.integer().optional(),
            "reconciling": t.boolean().optional(),
            "createTime": t.string().optional(),
            "index": t.integer().optional(),
            "containers": t.array(
                t.proxy(renames["GoogleCloudRunV2ContainerOut"])
            ).optional(),
            "timeout": t.string().optional(),
            "deleteTime": t.string().optional(),
            "volumes": t.array(
                t.proxy(renames["GoogleCloudRunV2VolumeOut"])
            ).optional(),
            "satisfiesPzs": t.boolean().optional(),
            "encryptionKey": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2TaskOut"])
    types["GoogleCloudRunV2ContainerIn"] = t.struct(
        {
            "volumeMounts": t.array(
                t.proxy(renames["GoogleCloudRunV2VolumeMountIn"])
            ).optional(),
            "command": t.array(t.string()).optional(),
            "image": t.string(),
            "args": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "dependsOn": t.array(t.string()).optional(),
            "env": t.array(t.proxy(renames["GoogleCloudRunV2EnvVarIn"])).optional(),
            "startupProbe": t.proxy(renames["GoogleCloudRunV2ProbeIn"]).optional(),
            "livenessProbe": t.proxy(renames["GoogleCloudRunV2ProbeIn"]).optional(),
            "workingDir": t.string().optional(),
            "resources": t.proxy(
                renames["GoogleCloudRunV2ResourceRequirementsIn"]
            ).optional(),
            "ports": t.array(
                t.proxy(renames["GoogleCloudRunV2ContainerPortIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudRunV2ContainerIn"])
    types["GoogleCloudRunV2ContainerOut"] = t.struct(
        {
            "volumeMounts": t.array(
                t.proxy(renames["GoogleCloudRunV2VolumeMountOut"])
            ).optional(),
            "command": t.array(t.string()).optional(),
            "image": t.string(),
            "args": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "dependsOn": t.array(t.string()).optional(),
            "env": t.array(t.proxy(renames["GoogleCloudRunV2EnvVarOut"])).optional(),
            "startupProbe": t.proxy(renames["GoogleCloudRunV2ProbeOut"]).optional(),
            "livenessProbe": t.proxy(renames["GoogleCloudRunV2ProbeOut"]).optional(),
            "workingDir": t.string().optional(),
            "resources": t.proxy(
                renames["GoogleCloudRunV2ResourceRequirementsOut"]
            ).optional(),
            "ports": t.array(
                t.proxy(renames["GoogleCloudRunV2ContainerPortOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2ContainerOut"])
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
    types["GoogleCloudRunV2TrafficTargetStatusIn"] = t.struct(
        {
            "revision": t.string().optional(),
            "tag": t.string().optional(),
            "percent": t.integer().optional(),
            "type": t.string().optional(),
            "uri": t.string().optional(),
        }
    ).named(renames["GoogleCloudRunV2TrafficTargetStatusIn"])
    types["GoogleCloudRunV2TrafficTargetStatusOut"] = t.struct(
        {
            "revision": t.string().optional(),
            "tag": t.string().optional(),
            "percent": t.integer().optional(),
            "type": t.string().optional(),
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2TrafficTargetStatusOut"])
    types["GoogleCloudRunV2ServiceIn"] = t.struct(
        {
            "template": t.proxy(renames["GoogleCloudRunV2RevisionTemplateIn"]),
            "client": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "binaryAuthorization": t.proxy(
                renames["GoogleCloudRunV2BinaryAuthorizationIn"]
            ).optional(),
            "clientVersion": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "traffic": t.array(
                t.proxy(renames["GoogleCloudRunV2TrafficTargetIn"])
            ).optional(),
            "name": t.string().optional(),
            "launchStage": t.string().optional(),
            "description": t.string().optional(),
            "ingress": t.string().optional(),
        }
    ).named(renames["GoogleCloudRunV2ServiceIn"])
    types["GoogleCloudRunV2ServiceOut"] = t.struct(
        {
            "template": t.proxy(renames["GoogleCloudRunV2RevisionTemplateOut"]),
            "observedGeneration": t.string().optional(),
            "uri": t.string().optional(),
            "etag": t.string().optional(),
            "client": t.string().optional(),
            "generation": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "trafficStatuses": t.array(
                t.proxy(renames["GoogleCloudRunV2TrafficTargetStatusOut"])
            ).optional(),
            "binaryAuthorization": t.proxy(
                renames["GoogleCloudRunV2BinaryAuthorizationOut"]
            ).optional(),
            "terminalCondition": t.proxy(
                renames["GoogleCloudRunV2ConditionOut"]
            ).optional(),
            "creator": t.string().optional(),
            "createTime": t.string().optional(),
            "deleteTime": t.string().optional(),
            "clientVersion": t.string().optional(),
            "expireTime": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "traffic": t.array(
                t.proxy(renames["GoogleCloudRunV2TrafficTargetOut"])
            ).optional(),
            "updateTime": t.string().optional(),
            "latestCreatedRevision": t.string().optional(),
            "name": t.string().optional(),
            "conditions": t.array(
                t.proxy(renames["GoogleCloudRunV2ConditionOut"])
            ).optional(),
            "reconciling": t.boolean().optional(),
            "satisfiesPzs": t.boolean().optional(),
            "launchStage": t.string().optional(),
            "description": t.string().optional(),
            "uid": t.string().optional(),
            "lastModifier": t.string().optional(),
            "ingress": t.string().optional(),
            "latestReadyRevision": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2ServiceOut"])
    types["GoogleCloudRunV2RevisionIn"] = t.struct(
        {
            "encryptionKeyShutdownDuration": t.string().optional(),
            "executionEnvironment": t.string().optional(),
            "volumes": t.array(t.proxy(renames["GoogleCloudRunV2VolumeIn"])).optional(),
            "launchStage": t.string().optional(),
            "encryptionKeyRevocationAction": t.string().optional(),
            "sessionAffinity": t.boolean().optional(),
            "vpcAccess": t.proxy(renames["GoogleCloudRunV2VpcAccessIn"]).optional(),
            "scaling": t.proxy(renames["GoogleCloudRunV2RevisionScalingIn"]).optional(),
            "containers": t.array(
                t.proxy(renames["GoogleCloudRunV2ContainerIn"])
            ).optional(),
            "maxInstanceRequestConcurrency": t.integer().optional(),
            "encryptionKey": t.string().optional(),
            "timeout": t.string().optional(),
            "serviceAccount": t.string().optional(),
        }
    ).named(renames["GoogleCloudRunV2RevisionIn"])
    types["GoogleCloudRunV2RevisionOut"] = t.struct(
        {
            "reconciling": t.boolean().optional(),
            "encryptionKeyShutdownDuration": t.string().optional(),
            "executionEnvironment": t.string().optional(),
            "volumes": t.array(
                t.proxy(renames["GoogleCloudRunV2VolumeOut"])
            ).optional(),
            "launchStage": t.string().optional(),
            "encryptionKeyRevocationAction": t.string().optional(),
            "uid": t.string().optional(),
            "expireTime": t.string().optional(),
            "sessionAffinity": t.boolean().optional(),
            "vpcAccess": t.proxy(renames["GoogleCloudRunV2VpcAccessOut"]).optional(),
            "createTime": t.string().optional(),
            "scaling": t.proxy(
                renames["GoogleCloudRunV2RevisionScalingOut"]
            ).optional(),
            "deleteTime": t.string().optional(),
            "containers": t.array(
                t.proxy(renames["GoogleCloudRunV2ContainerOut"])
            ).optional(),
            "conditions": t.array(
                t.proxy(renames["GoogleCloudRunV2ConditionOut"])
            ).optional(),
            "generation": t.string().optional(),
            "observedGeneration": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "maxInstanceRequestConcurrency": t.integer().optional(),
            "encryptionKey": t.string().optional(),
            "timeout": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "etag": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "satisfiesPzs": t.boolean().optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "service": t.string().optional(),
            "logUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2RevisionOut"])
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
    types["GoogleIamV1PolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "auditConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditConfigIn"])
            ).optional(),
            "bindings": t.array(t.proxy(renames["GoogleIamV1BindingIn"])).optional(),
            "version": t.integer().optional(),
        }
    ).named(renames["GoogleIamV1PolicyIn"])
    types["GoogleIamV1PolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "auditConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditConfigOut"])
            ).optional(),
            "bindings": t.array(t.proxy(renames["GoogleIamV1BindingOut"])).optional(),
            "version": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1PolicyOut"])
    types["GoogleCloudRunV2ExecutionIn"] = t.struct(
        {"launchStage": t.string().optional()}
    ).named(renames["GoogleCloudRunV2ExecutionIn"])
    types["GoogleCloudRunV2ExecutionOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "succeededCount": t.integer().optional(),
            "parallelism": t.integer().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "taskCount": t.integer().optional(),
            "expireTime": t.string().optional(),
            "job": t.string().optional(),
            "retriedCount": t.integer().optional(),
            "deleteTime": t.string().optional(),
            "logUri": t.string().optional(),
            "launchStage": t.string().optional(),
            "runningCount": t.integer().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "completionTime": t.string().optional(),
            "cancelledCount": t.integer().optional(),
            "startTime": t.string().optional(),
            "uid": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "reconciling": t.boolean().optional(),
            "failedCount": t.integer().optional(),
            "observedGeneration": t.string().optional(),
            "generation": t.string().optional(),
            "satisfiesPzs": t.boolean().optional(),
            "etag": t.string().optional(),
            "template": t.proxy(renames["GoogleCloudRunV2TaskTemplateOut"]).optional(),
            "conditions": t.array(
                t.proxy(renames["GoogleCloudRunV2ConditionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2ExecutionOut"])
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
    types["GoogleCloudRunV2ExecutionTemplateIn"] = t.struct(
        {
            "taskCount": t.integer().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "parallelism": t.integer().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "template": t.proxy(renames["GoogleCloudRunV2TaskTemplateIn"]),
        }
    ).named(renames["GoogleCloudRunV2ExecutionTemplateIn"])
    types["GoogleCloudRunV2ExecutionTemplateOut"] = t.struct(
        {
            "taskCount": t.integer().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "parallelism": t.integer().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "template": t.proxy(renames["GoogleCloudRunV2TaskTemplateOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2ExecutionTemplateOut"])
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
    types["GoogleCloudRunV2TCPSocketActionIn"] = t.struct(
        {"port": t.integer().optional()}
    ).named(renames["GoogleCloudRunV2TCPSocketActionIn"])
    types["GoogleCloudRunV2TCPSocketActionOut"] = t.struct(
        {
            "port": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2TCPSocketActionOut"])
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
    types["GoogleCloudRunV2SecretVolumeSourceIn"] = t.struct(
        {
            "items": t.array(
                t.proxy(renames["GoogleCloudRunV2VersionToPathIn"])
            ).optional(),
            "defaultMode": t.integer().optional(),
            "secret": t.string(),
        }
    ).named(renames["GoogleCloudRunV2SecretVolumeSourceIn"])
    types["GoogleCloudRunV2SecretVolumeSourceOut"] = t.struct(
        {
            "items": t.array(
                t.proxy(renames["GoogleCloudRunV2VersionToPathOut"])
            ).optional(),
            "defaultMode": t.integer().optional(),
            "secret": t.string(),
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
    types["GoogleIamV1TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["GoogleIamV1TestIamPermissionsResponseIn"])
    types["GoogleIamV1TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1TestIamPermissionsResponseOut"])
    types["GoogleCloudRunV2HTTPGetActionIn"] = t.struct(
        {
            "path": t.string().optional(),
            "httpHeaders": t.array(
                t.proxy(renames["GoogleCloudRunV2HTTPHeaderIn"])
            ).optional(),
            "port": t.integer().optional(),
        }
    ).named(renames["GoogleCloudRunV2HTTPGetActionIn"])
    types["GoogleCloudRunV2HTTPGetActionOut"] = t.struct(
        {
            "path": t.string().optional(),
            "httpHeaders": t.array(
                t.proxy(renames["GoogleCloudRunV2HTTPHeaderOut"])
            ).optional(),
            "port": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRunV2HTTPGetActionOut"])
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

    functions = {}
    functions["projectsLocationsOperationsDelete"] = run.get(
        "v2/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsWait"] = run.get(
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
    functions["projectsLocationsServicesSetIamPolicy"] = run.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesPatch"] = run.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesGetIamPolicy"] = run.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesGet"] = run.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesList"] = run.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesDelete"] = run.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesCreate"] = run.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesTestIamPermissions"] = run.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesRevisionsList"] = run.delete(
        "v2/{name}",
        t.struct(
            {
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
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
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
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
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsSetIamPolicy"] = run.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsRun"] = run.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsPatch"] = run.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsList"] = run.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsGetIamPolicy"] = run.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsDelete"] = run.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsGet"] = run.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsCreate"] = run.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsTestIamPermissions"] = run.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsExecutionsGet"] = run.get(
        "v2/{parent}/executions",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "showDeleted": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRunV2ListExecutionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsExecutionsDelete"] = run.get(
        "v2/{parent}/executions",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "showDeleted": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRunV2ListExecutionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsExecutionsList"] = run.get(
        "v2/{parent}/executions",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "showDeleted": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRunV2ListExecutionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsExecutionsTasksGet"] = run.get(
        "v2/{parent}/tasks",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "showDeleted": t.boolean().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
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
                "pageToken": t.string().optional(),
                "showDeleted": t.boolean().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRunV2ListTasksResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(importer="run", renames=renames, types=types, functions=functions)
