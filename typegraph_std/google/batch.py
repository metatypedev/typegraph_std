from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_batch() -> Import:
    batch = HTTPRuntime("https://batch.googleapis.com/")

    renames = {
        "ErrorResponse": "_batch_1_ErrorResponse",
        "LifecyclePolicyIn": "_batch_2_LifecyclePolicyIn",
        "LifecyclePolicyOut": "_batch_3_LifecyclePolicyOut",
        "ActionConditionIn": "_batch_4_ActionConditionIn",
        "ActionConditionOut": "_batch_5_ActionConditionOut",
        "KMSEnvMapIn": "_batch_6_KMSEnvMapIn",
        "KMSEnvMapOut": "_batch_7_KMSEnvMapOut",
        "AgentInfoIn": "_batch_8_AgentInfoIn",
        "AgentInfoOut": "_batch_9_AgentInfoOut",
        "NetworkPolicyIn": "_batch_10_NetworkPolicyIn",
        "NetworkPolicyOut": "_batch_11_NetworkPolicyOut",
        "DiskIn": "_batch_12_DiskIn",
        "DiskOut": "_batch_13_DiskOut",
        "ReportAgentStateResponseIn": "_batch_14_ReportAgentStateResponseIn",
        "ReportAgentStateResponseOut": "_batch_15_ReportAgentStateResponseOut",
        "VolumeIn": "_batch_16_VolumeIn",
        "VolumeOut": "_batch_17_VolumeOut",
        "TaskGroupStatusIn": "_batch_18_TaskGroupStatusIn",
        "TaskGroupStatusOut": "_batch_19_TaskGroupStatusOut",
        "OperationMetadataIn": "_batch_20_OperationMetadataIn",
        "OperationMetadataOut": "_batch_21_OperationMetadataOut",
        "ListTasksResponseIn": "_batch_22_ListTasksResponseIn",
        "ListTasksResponseOut": "_batch_23_ListTasksResponseOut",
        "RunnableIn": "_batch_24_RunnableIn",
        "RunnableOut": "_batch_25_RunnableOut",
        "TaskStatusIn": "_batch_26_TaskStatusIn",
        "TaskStatusOut": "_batch_27_TaskStatusOut",
        "EmptyIn": "_batch_28_EmptyIn",
        "EmptyOut": "_batch_29_EmptyOut",
        "NetworkInterfaceIn": "_batch_30_NetworkInterfaceIn",
        "NetworkInterfaceOut": "_batch_31_NetworkInterfaceOut",
        "AllocationPolicyIn": "_batch_32_AllocationPolicyIn",
        "AllocationPolicyOut": "_batch_33_AllocationPolicyOut",
        "StatusEventIn": "_batch_34_StatusEventIn",
        "StatusEventOut": "_batch_35_StatusEventOut",
        "AgentTaskIn": "_batch_36_AgentTaskIn",
        "AgentTaskOut": "_batch_37_AgentTaskOut",
        "JobNotificationIn": "_batch_38_JobNotificationIn",
        "JobNotificationOut": "_batch_39_JobNotificationOut",
        "AgentMetadataIn": "_batch_40_AgentMetadataIn",
        "AgentMetadataOut": "_batch_41_AgentMetadataOut",
        "JobStatusIn": "_batch_42_JobStatusIn",
        "JobStatusOut": "_batch_43_JobStatusOut",
        "MessageIn": "_batch_44_MessageIn",
        "MessageOut": "_batch_45_MessageOut",
        "BarrierIn": "_batch_46_BarrierIn",
        "BarrierOut": "_batch_47_BarrierOut",
        "ScriptIn": "_batch_48_ScriptIn",
        "ScriptOut": "_batch_49_ScriptOut",
        "InstancePolicyIn": "_batch_50_InstancePolicyIn",
        "InstancePolicyOut": "_batch_51_InstancePolicyOut",
        "InstanceStatusIn": "_batch_52_InstanceStatusIn",
        "InstanceStatusOut": "_batch_53_InstanceStatusOut",
        "LocationIn": "_batch_54_LocationIn",
        "LocationOut": "_batch_55_LocationOut",
        "JobIn": "_batch_56_JobIn",
        "JobOut": "_batch_57_JobOut",
        "StatusIn": "_batch_58_StatusIn",
        "StatusOut": "_batch_59_StatusOut",
        "TaskGroupIn": "_batch_60_TaskGroupIn",
        "TaskGroupOut": "_batch_61_TaskGroupOut",
        "AcceleratorIn": "_batch_62_AcceleratorIn",
        "AcceleratorOut": "_batch_63_AcceleratorOut",
        "TaskExecutionIn": "_batch_64_TaskExecutionIn",
        "TaskExecutionOut": "_batch_65_TaskExecutionOut",
        "InstancePolicyOrTemplateIn": "_batch_66_InstancePolicyOrTemplateIn",
        "InstancePolicyOrTemplateOut": "_batch_67_InstancePolicyOrTemplateOut",
        "EnvironmentIn": "_batch_68_EnvironmentIn",
        "EnvironmentOut": "_batch_69_EnvironmentOut",
        "ListLocationsResponseIn": "_batch_70_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_batch_71_ListLocationsResponseOut",
        "ReportAgentStateRequestIn": "_batch_72_ReportAgentStateRequestIn",
        "ReportAgentStateRequestOut": "_batch_73_ReportAgentStateRequestOut",
        "ListOperationsResponseIn": "_batch_74_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_batch_75_ListOperationsResponseOut",
        "AgentTaskInfoIn": "_batch_76_AgentTaskInfoIn",
        "AgentTaskInfoOut": "_batch_77_AgentTaskInfoOut",
        "TaskSpecIn": "_batch_78_TaskSpecIn",
        "TaskSpecOut": "_batch_79_TaskSpecOut",
        "CancelOperationRequestIn": "_batch_80_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_batch_81_CancelOperationRequestOut",
        "ListJobsResponseIn": "_batch_82_ListJobsResponseIn",
        "ListJobsResponseOut": "_batch_83_ListJobsResponseOut",
        "GCSIn": "_batch_84_GCSIn",
        "GCSOut": "_batch_85_GCSOut",
        "LocationPolicyIn": "_batch_86_LocationPolicyIn",
        "LocationPolicyOut": "_batch_87_LocationPolicyOut",
        "AttachedDiskIn": "_batch_88_AttachedDiskIn",
        "AttachedDiskOut": "_batch_89_AttachedDiskOut",
        "ComputeResourceIn": "_batch_90_ComputeResourceIn",
        "ComputeResourceOut": "_batch_91_ComputeResourceOut",
        "AgentTimingInfoIn": "_batch_92_AgentTimingInfoIn",
        "AgentTimingInfoOut": "_batch_93_AgentTimingInfoOut",
        "PlacementPolicyIn": "_batch_94_PlacementPolicyIn",
        "PlacementPolicyOut": "_batch_95_PlacementPolicyOut",
        "NFSIn": "_batch_96_NFSIn",
        "NFSOut": "_batch_97_NFSOut",
        "ServiceAccountIn": "_batch_98_ServiceAccountIn",
        "ServiceAccountOut": "_batch_99_ServiceAccountOut",
        "LogsPolicyIn": "_batch_100_LogsPolicyIn",
        "LogsPolicyOut": "_batch_101_LogsPolicyOut",
        "TaskIn": "_batch_102_TaskIn",
        "TaskOut": "_batch_103_TaskOut",
        "OperationIn": "_batch_104_OperationIn",
        "OperationOut": "_batch_105_OperationOut",
        "ContainerIn": "_batch_106_ContainerIn",
        "ContainerOut": "_batch_107_ContainerOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["LifecyclePolicyIn"] = t.struct(
        {
            "action": t.string().optional(),
            "actionCondition": t.proxy(renames["ActionConditionIn"]).optional(),
        }
    ).named(renames["LifecyclePolicyIn"])
    types["LifecyclePolicyOut"] = t.struct(
        {
            "action": t.string().optional(),
            "actionCondition": t.proxy(renames["ActionConditionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LifecyclePolicyOut"])
    types["ActionConditionIn"] = t.struct(
        {"exitCodes": t.array(t.integer()).optional()}
    ).named(renames["ActionConditionIn"])
    types["ActionConditionOut"] = t.struct(
        {
            "exitCodes": t.array(t.integer()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActionConditionOut"])
    types["KMSEnvMapIn"] = t.struct(
        {"keyName": t.string().optional(), "cipherText": t.string().optional()}
    ).named(renames["KMSEnvMapIn"])
    types["KMSEnvMapOut"] = t.struct(
        {
            "keyName": t.string().optional(),
            "cipherText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KMSEnvMapOut"])
    types["AgentInfoIn"] = t.struct(
        {
            "tasks": t.array(t.proxy(renames["AgentTaskInfoIn"])).optional(),
            "taskGroupId": t.string().optional(),
            "state": t.string().optional(),
            "reportTime": t.string().optional(),
            "jobId": t.string().optional(),
        }
    ).named(renames["AgentInfoIn"])
    types["AgentInfoOut"] = t.struct(
        {
            "tasks": t.array(t.proxy(renames["AgentTaskInfoOut"])).optional(),
            "taskGroupId": t.string().optional(),
            "state": t.string().optional(),
            "reportTime": t.string().optional(),
            "jobId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AgentInfoOut"])
    types["NetworkPolicyIn"] = t.struct(
        {
            "networkInterfaces": t.array(
                t.proxy(renames["NetworkInterfaceIn"])
            ).optional()
        }
    ).named(renames["NetworkPolicyIn"])
    types["NetworkPolicyOut"] = t.struct(
        {
            "networkInterfaces": t.array(
                t.proxy(renames["NetworkInterfaceOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkPolicyOut"])
    types["DiskIn"] = t.struct(
        {
            "image": t.string().optional(),
            "snapshot": t.string().optional(),
            "sizeGb": t.string().optional(),
            "diskInterface": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["DiskIn"])
    types["DiskOut"] = t.struct(
        {
            "image": t.string().optional(),
            "snapshot": t.string().optional(),
            "sizeGb": t.string().optional(),
            "diskInterface": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiskOut"])
    types["ReportAgentStateResponseIn"] = t.struct(
        {
            "minReportInterval": t.string().optional(),
            "defaultReportInterval": t.string().optional(),
            "tasks": t.array(t.proxy(renames["AgentTaskIn"])).optional(),
        }
    ).named(renames["ReportAgentStateResponseIn"])
    types["ReportAgentStateResponseOut"] = t.struct(
        {
            "minReportInterval": t.string().optional(),
            "defaultReportInterval": t.string().optional(),
            "tasks": t.array(t.proxy(renames["AgentTaskOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportAgentStateResponseOut"])
    types["VolumeIn"] = t.struct(
        {
            "mountOptions": t.array(t.string()).optional(),
            "nfs": t.proxy(renames["NFSIn"]).optional(),
            "gcs": t.proxy(renames["GCSIn"]).optional(),
            "deviceName": t.string().optional(),
            "mountPath": t.string().optional(),
        }
    ).named(renames["VolumeIn"])
    types["VolumeOut"] = t.struct(
        {
            "mountOptions": t.array(t.string()).optional(),
            "nfs": t.proxy(renames["NFSOut"]).optional(),
            "gcs": t.proxy(renames["GCSOut"]).optional(),
            "deviceName": t.string().optional(),
            "mountPath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VolumeOut"])
    types["TaskGroupStatusIn"] = t.struct(
        {
            "counts": t.struct({"_": t.string().optional()}).optional(),
            "instances": t.array(t.proxy(renames["InstanceStatusIn"])).optional(),
        }
    ).named(renames["TaskGroupStatusIn"])
    types["TaskGroupStatusOut"] = t.struct(
        {
            "counts": t.struct({"_": t.string().optional()}).optional(),
            "instances": t.array(t.proxy(renames["InstanceStatusOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TaskGroupStatusOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "verb": t.string().optional(),
            "target": t.string().optional(),
            "createTime": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "statusMessage": t.string().optional(),
            "apiVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["ListTasksResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "tasks": t.array(t.proxy(renames["TaskIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListTasksResponseIn"])
    types["ListTasksResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "tasks": t.array(t.proxy(renames["TaskOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTasksResponseOut"])
    types["RunnableIn"] = t.struct(
        {
            "script": t.proxy(renames["ScriptIn"]).optional(),
            "ignoreExitStatus": t.boolean().optional(),
            "container": t.proxy(renames["ContainerIn"]).optional(),
            "environment": t.proxy(renames["EnvironmentIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "barrier": t.proxy(renames["BarrierIn"]).optional(),
            "timeout": t.string().optional(),
            "alwaysRun": t.boolean().optional(),
            "background": t.boolean().optional(),
        }
    ).named(renames["RunnableIn"])
    types["RunnableOut"] = t.struct(
        {
            "script": t.proxy(renames["ScriptOut"]).optional(),
            "ignoreExitStatus": t.boolean().optional(),
            "container": t.proxy(renames["ContainerOut"]).optional(),
            "environment": t.proxy(renames["EnvironmentOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "barrier": t.proxy(renames["BarrierOut"]).optional(),
            "timeout": t.string().optional(),
            "alwaysRun": t.boolean().optional(),
            "background": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunnableOut"])
    types["TaskStatusIn"] = t.struct(
        {
            "state": t.string().optional(),
            "statusEvents": t.array(t.proxy(renames["StatusEventIn"])).optional(),
        }
    ).named(renames["TaskStatusIn"])
    types["TaskStatusOut"] = t.struct(
        {
            "state": t.string().optional(),
            "statusEvents": t.array(t.proxy(renames["StatusEventOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TaskStatusOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["NetworkInterfaceIn"] = t.struct(
        {
            "subnetwork": t.string().optional(),
            "network": t.string().optional(),
            "noExternalIpAddress": t.boolean().optional(),
        }
    ).named(renames["NetworkInterfaceIn"])
    types["NetworkInterfaceOut"] = t.struct(
        {
            "subnetwork": t.string().optional(),
            "network": t.string().optional(),
            "noExternalIpAddress": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkInterfaceOut"])
    types["AllocationPolicyIn"] = t.struct(
        {
            "serviceAccount": t.proxy(renames["ServiceAccountIn"]).optional(),
            "network": t.proxy(renames["NetworkPolicyIn"]).optional(),
            "placement": t.proxy(renames["PlacementPolicyIn"]).optional(),
            "location": t.proxy(renames["LocationPolicyIn"]).optional(),
            "instances": t.array(
                t.proxy(renames["InstancePolicyOrTemplateIn"])
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["AllocationPolicyIn"])
    types["AllocationPolicyOut"] = t.struct(
        {
            "serviceAccount": t.proxy(renames["ServiceAccountOut"]).optional(),
            "network": t.proxy(renames["NetworkPolicyOut"]).optional(),
            "placement": t.proxy(renames["PlacementPolicyOut"]).optional(),
            "location": t.proxy(renames["LocationPolicyOut"]).optional(),
            "instances": t.array(
                t.proxy(renames["InstancePolicyOrTemplateOut"])
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AllocationPolicyOut"])
    types["StatusEventIn"] = t.struct(
        {
            "taskState": t.string().optional(),
            "description": t.string().optional(),
            "taskExecution": t.proxy(renames["TaskExecutionIn"]).optional(),
            "eventTime": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["StatusEventIn"])
    types["StatusEventOut"] = t.struct(
        {
            "taskState": t.string().optional(),
            "description": t.string().optional(),
            "taskExecution": t.proxy(renames["TaskExecutionOut"]).optional(),
            "eventTime": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusEventOut"])
    types["AgentTaskIn"] = t.struct(
        {
            "taskSource": t.string().optional(),
            "reachedBarrier": t.string().optional(),
            "intendedState": t.string().optional(),
            "spec": t.proxy(renames["TaskSpecIn"]).optional(),
            "status": t.proxy(renames["TaskStatusIn"]).optional(),
            "task": t.string().optional(),
        }
    ).named(renames["AgentTaskIn"])
    types["AgentTaskOut"] = t.struct(
        {
            "taskSource": t.string().optional(),
            "reachedBarrier": t.string().optional(),
            "intendedState": t.string().optional(),
            "spec": t.proxy(renames["TaskSpecOut"]).optional(),
            "status": t.proxy(renames["TaskStatusOut"]).optional(),
            "task": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AgentTaskOut"])
    types["JobNotificationIn"] = t.struct(
        {
            "message": t.proxy(renames["MessageIn"]).optional(),
            "pubsubTopic": t.string().optional(),
        }
    ).named(renames["JobNotificationIn"])
    types["JobNotificationOut"] = t.struct(
        {
            "message": t.proxy(renames["MessageOut"]).optional(),
            "pubsubTopic": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobNotificationOut"])
    types["AgentMetadataIn"] = t.struct(
        {
            "creator": t.string().optional(),
            "osRelease": t.struct({"_": t.string().optional()}).optional(),
            "creationTime": t.string().optional(),
            "zone": t.string().optional(),
            "imageVersion": t.string().optional(),
            "instancePreemptionNoticeReceived": t.boolean().optional(),
            "version": t.string().optional(),
            "instance": t.string().optional(),
            "instanceId": t.string().optional(),
        }
    ).named(renames["AgentMetadataIn"])
    types["AgentMetadataOut"] = t.struct(
        {
            "creator": t.string().optional(),
            "osRelease": t.struct({"_": t.string().optional()}).optional(),
            "creationTime": t.string().optional(),
            "zone": t.string().optional(),
            "imageVersion": t.string().optional(),
            "instancePreemptionNoticeReceived": t.boolean().optional(),
            "version": t.string().optional(),
            "instance": t.string().optional(),
            "instanceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AgentMetadataOut"])
    types["JobStatusIn"] = t.struct(
        {
            "taskGroups": t.struct({"_": t.string().optional()}).optional(),
            "runDuration": t.string().optional(),
            "state": t.string().optional(),
            "statusEvents": t.array(t.proxy(renames["StatusEventIn"])).optional(),
        }
    ).named(renames["JobStatusIn"])
    types["JobStatusOut"] = t.struct(
        {
            "taskGroups": t.struct({"_": t.string().optional()}).optional(),
            "runDuration": t.string().optional(),
            "state": t.string().optional(),
            "statusEvents": t.array(t.proxy(renames["StatusEventOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobStatusOut"])
    types["MessageIn"] = t.struct(
        {
            "newTaskState": t.string().optional(),
            "newJobState": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["MessageIn"])
    types["MessageOut"] = t.struct(
        {
            "newTaskState": t.string().optional(),
            "newJobState": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MessageOut"])
    types["BarrierIn"] = t.struct({"name": t.string().optional()}).named(
        renames["BarrierIn"]
    )
    types["BarrierOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BarrierOut"])
    types["ScriptIn"] = t.struct(
        {"path": t.string().optional(), "text": t.string().optional()}
    ).named(renames["ScriptIn"])
    types["ScriptOut"] = t.struct(
        {
            "path": t.string().optional(),
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScriptOut"])
    types["InstancePolicyIn"] = t.struct(
        {
            "accelerators": t.array(t.proxy(renames["AcceleratorIn"])).optional(),
            "minCpuPlatform": t.string().optional(),
            "disks": t.array(t.proxy(renames["AttachedDiskIn"])).optional(),
            "bootDisk": t.proxy(renames["DiskIn"]).optional(),
            "provisioningModel": t.string().optional(),
            "machineType": t.string().optional(),
        }
    ).named(renames["InstancePolicyIn"])
    types["InstancePolicyOut"] = t.struct(
        {
            "accelerators": t.array(t.proxy(renames["AcceleratorOut"])).optional(),
            "minCpuPlatform": t.string().optional(),
            "disks": t.array(t.proxy(renames["AttachedDiskOut"])).optional(),
            "bootDisk": t.proxy(renames["DiskOut"]).optional(),
            "provisioningModel": t.string().optional(),
            "machineType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstancePolicyOut"])
    types["InstanceStatusIn"] = t.struct(
        {
            "machineType": t.string().optional(),
            "taskPack": t.string().optional(),
            "provisioningModel": t.string().optional(),
            "bootDisk": t.proxy(renames["DiskIn"]).optional(),
        }
    ).named(renames["InstanceStatusIn"])
    types["InstanceStatusOut"] = t.struct(
        {
            "machineType": t.string().optional(),
            "taskPack": t.string().optional(),
            "provisioningModel": t.string().optional(),
            "bootDisk": t.proxy(renames["DiskOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceStatusOut"])
    types["LocationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["JobIn"] = t.struct(
        {
            "priority": t.string().optional(),
            "taskGroups": t.array(t.proxy(renames["TaskGroupIn"])),
            "notifications": t.array(t.proxy(renames["JobNotificationIn"])).optional(),
            "logsPolicy": t.proxy(renames["LogsPolicyIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "allocationPolicy": t.proxy(renames["AllocationPolicyIn"]).optional(),
        }
    ).named(renames["JobIn"])
    types["JobOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "priority": t.string().optional(),
            "name": t.string().optional(),
            "taskGroups": t.array(t.proxy(renames["TaskGroupOut"])),
            "uid": t.string().optional(),
            "notifications": t.array(t.proxy(renames["JobNotificationOut"])).optional(),
            "logsPolicy": t.proxy(renames["LogsPolicyOut"]).optional(),
            "status": t.proxy(renames["JobStatusOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "allocationPolicy": t.proxy(renames["AllocationPolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobOut"])
    types["StatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["TaskGroupIn"] = t.struct(
        {
            "schedulingPolicy": t.string().optional(),
            "taskCount": t.string().optional(),
            "requireHostsFile": t.boolean().optional(),
            "taskCountPerNode": t.string().optional(),
            "parallelism": t.string().optional(),
            "permissiveSsh": t.boolean().optional(),
            "taskSpec": t.proxy(renames["TaskSpecIn"]),
            "taskEnvironments": t.array(t.proxy(renames["EnvironmentIn"])).optional(),
        }
    ).named(renames["TaskGroupIn"])
    types["TaskGroupOut"] = t.struct(
        {
            "schedulingPolicy": t.string().optional(),
            "taskCount": t.string().optional(),
            "requireHostsFile": t.boolean().optional(),
            "taskCountPerNode": t.string().optional(),
            "parallelism": t.string().optional(),
            "name": t.string().optional(),
            "permissiveSsh": t.boolean().optional(),
            "taskSpec": t.proxy(renames["TaskSpecOut"]),
            "taskEnvironments": t.array(t.proxy(renames["EnvironmentOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TaskGroupOut"])
    types["AcceleratorIn"] = t.struct(
        {
            "installGpuDrivers": t.boolean().optional(),
            "count": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["AcceleratorIn"])
    types["AcceleratorOut"] = t.struct(
        {
            "installGpuDrivers": t.boolean().optional(),
            "count": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AcceleratorOut"])
    types["TaskExecutionIn"] = t.struct({"exitCode": t.integer().optional()}).named(
        renames["TaskExecutionIn"]
    )
    types["TaskExecutionOut"] = t.struct(
        {
            "exitCode": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TaskExecutionOut"])
    types["InstancePolicyOrTemplateIn"] = t.struct(
        {
            "installGpuDrivers": t.boolean().optional(),
            "instanceTemplate": t.string().optional(),
            "policy": t.proxy(renames["InstancePolicyIn"]).optional(),
        }
    ).named(renames["InstancePolicyOrTemplateIn"])
    types["InstancePolicyOrTemplateOut"] = t.struct(
        {
            "installGpuDrivers": t.boolean().optional(),
            "instanceTemplate": t.string().optional(),
            "policy": t.proxy(renames["InstancePolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstancePolicyOrTemplateOut"])
    types["EnvironmentIn"] = t.struct(
        {
            "variables": t.struct({"_": t.string().optional()}).optional(),
            "encryptedVariables": t.proxy(renames["KMSEnvMapIn"]).optional(),
            "secretVariables": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["EnvironmentIn"])
    types["EnvironmentOut"] = t.struct(
        {
            "variables": t.struct({"_": t.string().optional()}).optional(),
            "encryptedVariables": t.proxy(renames["KMSEnvMapOut"]).optional(),
            "secretVariables": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnvironmentOut"])
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
    types["ReportAgentStateRequestIn"] = t.struct(
        {
            "agentTimingInfo": t.proxy(renames["AgentTimingInfoIn"]).optional(),
            "metadata": t.proxy(renames["AgentMetadataIn"]).optional(),
            "agentInfo": t.proxy(renames["AgentInfoIn"]).optional(),
        }
    ).named(renames["ReportAgentStateRequestIn"])
    types["ReportAgentStateRequestOut"] = t.struct(
        {
            "agentTimingInfo": t.proxy(renames["AgentTimingInfoOut"]).optional(),
            "metadata": t.proxy(renames["AgentMetadataOut"]).optional(),
            "agentInfo": t.proxy(renames["AgentInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportAgentStateRequestOut"])
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
    types["AgentTaskInfoIn"] = t.struct(
        {
            "taskId": t.string().optional(),
            "runnable": t.string().optional(),
            "taskStatus": t.proxy(renames["TaskStatusIn"]).optional(),
        }
    ).named(renames["AgentTaskInfoIn"])
    types["AgentTaskInfoOut"] = t.struct(
        {
            "taskId": t.string().optional(),
            "runnable": t.string().optional(),
            "taskStatus": t.proxy(renames["TaskStatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AgentTaskInfoOut"])
    types["TaskSpecIn"] = t.struct(
        {
            "maxRunDuration": t.string().optional(),
            "runnables": t.array(t.proxy(renames["RunnableIn"])).optional(),
            "lifecyclePolicies": t.array(
                t.proxy(renames["LifecyclePolicyIn"])
            ).optional(),
            "maxRetryCount": t.integer().optional(),
            "environment": t.proxy(renames["EnvironmentIn"]).optional(),
            "environments": t.struct({"_": t.string().optional()}).optional(),
            "computeResource": t.proxy(renames["ComputeResourceIn"]).optional(),
            "volumes": t.array(t.proxy(renames["VolumeIn"])).optional(),
        }
    ).named(renames["TaskSpecIn"])
    types["TaskSpecOut"] = t.struct(
        {
            "maxRunDuration": t.string().optional(),
            "runnables": t.array(t.proxy(renames["RunnableOut"])).optional(),
            "lifecyclePolicies": t.array(
                t.proxy(renames["LifecyclePolicyOut"])
            ).optional(),
            "maxRetryCount": t.integer().optional(),
            "environment": t.proxy(renames["EnvironmentOut"]).optional(),
            "environments": t.struct({"_": t.string().optional()}).optional(),
            "computeResource": t.proxy(renames["ComputeResourceOut"]).optional(),
            "volumes": t.array(t.proxy(renames["VolumeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TaskSpecOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["ListJobsResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "jobs": t.array(t.proxy(renames["JobIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListJobsResponseIn"])
    types["ListJobsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "jobs": t.array(t.proxy(renames["JobOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListJobsResponseOut"])
    types["GCSIn"] = t.struct({"remotePath": t.string().optional()}).named(
        renames["GCSIn"]
    )
    types["GCSOut"] = t.struct(
        {
            "remotePath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GCSOut"])
    types["LocationPolicyIn"] = t.struct(
        {"allowedLocations": t.array(t.string()).optional()}
    ).named(renames["LocationPolicyIn"])
    types["LocationPolicyOut"] = t.struct(
        {
            "allowedLocations": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationPolicyOut"])
    types["AttachedDiskIn"] = t.struct(
        {
            "existingDisk": t.string().optional(),
            "newDisk": t.proxy(renames["DiskIn"]),
            "deviceName": t.string().optional(),
        }
    ).named(renames["AttachedDiskIn"])
    types["AttachedDiskOut"] = t.struct(
        {
            "existingDisk": t.string().optional(),
            "newDisk": t.proxy(renames["DiskOut"]),
            "deviceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttachedDiskOut"])
    types["ComputeResourceIn"] = t.struct(
        {
            "bootDiskMib": t.string().optional(),
            "cpuMilli": t.string().optional(),
            "memoryMib": t.string().optional(),
        }
    ).named(renames["ComputeResourceIn"])
    types["ComputeResourceOut"] = t.struct(
        {
            "bootDiskMib": t.string().optional(),
            "cpuMilli": t.string().optional(),
            "memoryMib": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComputeResourceOut"])
    types["AgentTimingInfoIn"] = t.struct(
        {
            "scriptStartupTime": t.string().optional(),
            "bootTime": t.string().optional(),
            "agentStartupTime": t.string().optional(),
        }
    ).named(renames["AgentTimingInfoIn"])
    types["AgentTimingInfoOut"] = t.struct(
        {
            "scriptStartupTime": t.string().optional(),
            "bootTime": t.string().optional(),
            "agentStartupTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AgentTimingInfoOut"])
    types["PlacementPolicyIn"] = t.struct(
        {"maxDistance": t.string().optional(), "collocation": t.string().optional()}
    ).named(renames["PlacementPolicyIn"])
    types["PlacementPolicyOut"] = t.struct(
        {
            "maxDistance": t.string().optional(),
            "collocation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlacementPolicyOut"])
    types["NFSIn"] = t.struct(
        {"server": t.string().optional(), "remotePath": t.string().optional()}
    ).named(renames["NFSIn"])
    types["NFSOut"] = t.struct(
        {
            "server": t.string().optional(),
            "remotePath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NFSOut"])
    types["ServiceAccountIn"] = t.struct(
        {"scopes": t.array(t.string()).optional(), "email": t.string().optional()}
    ).named(renames["ServiceAccountIn"])
    types["ServiceAccountOut"] = t.struct(
        {
            "scopes": t.array(t.string()).optional(),
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceAccountOut"])
    types["LogsPolicyIn"] = t.struct(
        {"destination": t.string().optional(), "logsPath": t.string().optional()}
    ).named(renames["LogsPolicyIn"])
    types["LogsPolicyOut"] = t.struct(
        {
            "destination": t.string().optional(),
            "logsPath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogsPolicyOut"])
    types["TaskIn"] = t.struct(
        {
            "status": t.proxy(renames["TaskStatusIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["TaskIn"])
    types["TaskOut"] = t.struct(
        {
            "status": t.proxy(renames["TaskStatusOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TaskOut"])
    types["OperationIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
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
    types["ContainerIn"] = t.struct(
        {
            "entrypoint": t.string().optional(),
            "imageUri": t.string().optional(),
            "volumes": t.array(t.string()).optional(),
            "username": t.string().optional(),
            "password": t.string().optional(),
            "options": t.string().optional(),
            "blockExternalNetwork": t.boolean().optional(),
            "commands": t.array(t.string()).optional(),
        }
    ).named(renames["ContainerIn"])
    types["ContainerOut"] = t.struct(
        {
            "entrypoint": t.string().optional(),
            "imageUri": t.string().optional(),
            "volumes": t.array(t.string()).optional(),
            "username": t.string().optional(),
            "password": t.string().optional(),
            "options": t.string().optional(),
            "blockExternalNetwork": t.boolean().optional(),
            "commands": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContainerOut"])

    functions = {}
    functions["projectsLocationsGet"] = batch.get(
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
    functions["projectsLocationsList"] = batch.get(
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
    functions["projectsLocationsJobsDelete"] = batch.post(
        "v1/{parent}/jobs",
        t.struct(
            {
                "parent": t.string(),
                "requestId": t.string().optional(),
                "jobId": t.string().optional(),
                "priority": t.string().optional(),
                "taskGroups": t.array(t.proxy(renames["TaskGroupIn"])),
                "notifications": t.array(
                    t.proxy(renames["JobNotificationIn"])
                ).optional(),
                "logsPolicy": t.proxy(renames["LogsPolicyIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "allocationPolicy": t.proxy(renames["AllocationPolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsList"] = batch.post(
        "v1/{parent}/jobs",
        t.struct(
            {
                "parent": t.string(),
                "requestId": t.string().optional(),
                "jobId": t.string().optional(),
                "priority": t.string().optional(),
                "taskGroups": t.array(t.proxy(renames["TaskGroupIn"])),
                "notifications": t.array(
                    t.proxy(renames["JobNotificationIn"])
                ).optional(),
                "logsPolicy": t.proxy(renames["LogsPolicyIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "allocationPolicy": t.proxy(renames["AllocationPolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsGet"] = batch.post(
        "v1/{parent}/jobs",
        t.struct(
            {
                "parent": t.string(),
                "requestId": t.string().optional(),
                "jobId": t.string().optional(),
                "priority": t.string().optional(),
                "taskGroups": t.array(t.proxy(renames["TaskGroupIn"])),
                "notifications": t.array(
                    t.proxy(renames["JobNotificationIn"])
                ).optional(),
                "logsPolicy": t.proxy(renames["LogsPolicyIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "allocationPolicy": t.proxy(renames["AllocationPolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsCreate"] = batch.post(
        "v1/{parent}/jobs",
        t.struct(
            {
                "parent": t.string(),
                "requestId": t.string().optional(),
                "jobId": t.string().optional(),
                "priority": t.string().optional(),
                "taskGroups": t.array(t.proxy(renames["TaskGroupIn"])),
                "notifications": t.array(
                    t.proxy(renames["JobNotificationIn"])
                ).optional(),
                "logsPolicy": t.proxy(renames["LogsPolicyIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "allocationPolicy": t.proxy(renames["AllocationPolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsTaskGroupsTasksList"] = batch.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TaskOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsTaskGroupsTasksGet"] = batch.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TaskOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = batch.get(
        "v1/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = batch.get(
        "v1/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = batch.get(
        "v1/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = batch.get(
        "v1/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStateReport"] = batch.post(
        "v1/{parent}/state:report",
        t.struct(
            {
                "parent": t.string(),
                "agentTimingInfo": t.proxy(renames["AgentTimingInfoIn"]).optional(),
                "metadata": t.proxy(renames["AgentMetadataIn"]).optional(),
                "agentInfo": t.proxy(renames["AgentInfoIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReportAgentStateResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="batch", renames=renames, types=Box(types), functions=Box(functions)
    )
