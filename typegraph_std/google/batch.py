from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_batch():
    batch = HTTPRuntime("https://batch.googleapis.com/")

    renames = {
        "ErrorResponse": "_batch_1_ErrorResponse",
        "ReportAgentStateRequestIn": "_batch_2_ReportAgentStateRequestIn",
        "ReportAgentStateRequestOut": "_batch_3_ReportAgentStateRequestOut",
        "JobStatusIn": "_batch_4_JobStatusIn",
        "JobStatusOut": "_batch_5_JobStatusOut",
        "AttachedDiskIn": "_batch_6_AttachedDiskIn",
        "AttachedDiskOut": "_batch_7_AttachedDiskOut",
        "TaskIn": "_batch_8_TaskIn",
        "TaskOut": "_batch_9_TaskOut",
        "InstanceStatusIn": "_batch_10_InstanceStatusIn",
        "InstanceStatusOut": "_batch_11_InstanceStatusOut",
        "RunnableIn": "_batch_12_RunnableIn",
        "RunnableOut": "_batch_13_RunnableOut",
        "JobIn": "_batch_14_JobIn",
        "JobOut": "_batch_15_JobOut",
        "ListTasksResponseIn": "_batch_16_ListTasksResponseIn",
        "ListTasksResponseOut": "_batch_17_ListTasksResponseOut",
        "ActionConditionIn": "_batch_18_ActionConditionIn",
        "ActionConditionOut": "_batch_19_ActionConditionOut",
        "ListJobsResponseIn": "_batch_20_ListJobsResponseIn",
        "ListJobsResponseOut": "_batch_21_ListJobsResponseOut",
        "AgentTimingInfoIn": "_batch_22_AgentTimingInfoIn",
        "AgentTimingInfoOut": "_batch_23_AgentTimingInfoOut",
        "ContainerIn": "_batch_24_ContainerIn",
        "ContainerOut": "_batch_25_ContainerOut",
        "ComputeResourceIn": "_batch_26_ComputeResourceIn",
        "ComputeResourceOut": "_batch_27_ComputeResourceOut",
        "LifecyclePolicyIn": "_batch_28_LifecyclePolicyIn",
        "LifecyclePolicyOut": "_batch_29_LifecyclePolicyOut",
        "NetworkInterfaceIn": "_batch_30_NetworkInterfaceIn",
        "NetworkInterfaceOut": "_batch_31_NetworkInterfaceOut",
        "NetworkPolicyIn": "_batch_32_NetworkPolicyIn",
        "NetworkPolicyOut": "_batch_33_NetworkPolicyOut",
        "AgentTaskInfoIn": "_batch_34_AgentTaskInfoIn",
        "AgentTaskInfoOut": "_batch_35_AgentTaskInfoOut",
        "AgentMetadataIn": "_batch_36_AgentMetadataIn",
        "AgentMetadataOut": "_batch_37_AgentMetadataOut",
        "BarrierIn": "_batch_38_BarrierIn",
        "BarrierOut": "_batch_39_BarrierOut",
        "GCSIn": "_batch_40_GCSIn",
        "GCSOut": "_batch_41_GCSOut",
        "MessageIn": "_batch_42_MessageIn",
        "MessageOut": "_batch_43_MessageOut",
        "AgentContainerIn": "_batch_44_AgentContainerIn",
        "AgentContainerOut": "_batch_45_AgentContainerOut",
        "LogsPolicyIn": "_batch_46_LogsPolicyIn",
        "LogsPolicyOut": "_batch_47_LogsPolicyOut",
        "KMSEnvMapIn": "_batch_48_KMSEnvMapIn",
        "KMSEnvMapOut": "_batch_49_KMSEnvMapOut",
        "AgentTaskIn": "_batch_50_AgentTaskIn",
        "AgentTaskOut": "_batch_51_AgentTaskOut",
        "InstancePolicyOrTemplateIn": "_batch_52_InstancePolicyOrTemplateIn",
        "InstancePolicyOrTemplateOut": "_batch_53_InstancePolicyOrTemplateOut",
        "TaskGroupStatusIn": "_batch_54_TaskGroupStatusIn",
        "TaskGroupStatusOut": "_batch_55_TaskGroupStatusOut",
        "ScriptIn": "_batch_56_ScriptIn",
        "ScriptOut": "_batch_57_ScriptOut",
        "LocationIn": "_batch_58_LocationIn",
        "LocationOut": "_batch_59_LocationOut",
        "AcceleratorIn": "_batch_60_AcceleratorIn",
        "AcceleratorOut": "_batch_61_AcceleratorOut",
        "AgentScriptIn": "_batch_62_AgentScriptIn",
        "AgentScriptOut": "_batch_63_AgentScriptOut",
        "AgentInfoIn": "_batch_64_AgentInfoIn",
        "AgentInfoOut": "_batch_65_AgentInfoOut",
        "ListLocationsResponseIn": "_batch_66_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_batch_67_ListLocationsResponseOut",
        "LocationPolicyIn": "_batch_68_LocationPolicyIn",
        "LocationPolicyOut": "_batch_69_LocationPolicyOut",
        "AgentTaskRunnableIn": "_batch_70_AgentTaskRunnableIn",
        "AgentTaskRunnableOut": "_batch_71_AgentTaskRunnableOut",
        "OperationIn": "_batch_72_OperationIn",
        "OperationOut": "_batch_73_OperationOut",
        "TaskExecutionIn": "_batch_74_TaskExecutionIn",
        "TaskExecutionOut": "_batch_75_TaskExecutionOut",
        "TaskGroupIn": "_batch_76_TaskGroupIn",
        "TaskGroupOut": "_batch_77_TaskGroupOut",
        "ListOperationsResponseIn": "_batch_78_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_batch_79_ListOperationsResponseOut",
        "ReportAgentStateResponseIn": "_batch_80_ReportAgentStateResponseIn",
        "ReportAgentStateResponseOut": "_batch_81_ReportAgentStateResponseOut",
        "TaskSpecIn": "_batch_82_TaskSpecIn",
        "TaskSpecOut": "_batch_83_TaskSpecOut",
        "InstancePolicyIn": "_batch_84_InstancePolicyIn",
        "InstancePolicyOut": "_batch_85_InstancePolicyOut",
        "DiskIn": "_batch_86_DiskIn",
        "DiskOut": "_batch_87_DiskOut",
        "CancelOperationRequestIn": "_batch_88_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_batch_89_CancelOperationRequestOut",
        "JobNotificationIn": "_batch_90_JobNotificationIn",
        "JobNotificationOut": "_batch_91_JobNotificationOut",
        "StatusIn": "_batch_92_StatusIn",
        "StatusOut": "_batch_93_StatusOut",
        "AgentTaskSpecIn": "_batch_94_AgentTaskSpecIn",
        "AgentTaskSpecOut": "_batch_95_AgentTaskSpecOut",
        "EnvironmentIn": "_batch_96_EnvironmentIn",
        "EnvironmentOut": "_batch_97_EnvironmentOut",
        "OperationMetadataIn": "_batch_98_OperationMetadataIn",
        "OperationMetadataOut": "_batch_99_OperationMetadataOut",
        "NFSIn": "_batch_100_NFSIn",
        "NFSOut": "_batch_101_NFSOut",
        "AgentKMSEnvMapIn": "_batch_102_AgentKMSEnvMapIn",
        "AgentKMSEnvMapOut": "_batch_103_AgentKMSEnvMapOut",
        "AgentEnvironmentIn": "_batch_104_AgentEnvironmentIn",
        "AgentEnvironmentOut": "_batch_105_AgentEnvironmentOut",
        "EmptyIn": "_batch_106_EmptyIn",
        "EmptyOut": "_batch_107_EmptyOut",
        "StatusEventIn": "_batch_108_StatusEventIn",
        "StatusEventOut": "_batch_109_StatusEventOut",
        "AllocationPolicyIn": "_batch_110_AllocationPolicyIn",
        "AllocationPolicyOut": "_batch_111_AllocationPolicyOut",
        "TaskStatusIn": "_batch_112_TaskStatusIn",
        "TaskStatusOut": "_batch_113_TaskStatusOut",
        "VolumeIn": "_batch_114_VolumeIn",
        "VolumeOut": "_batch_115_VolumeOut",
        "ServiceAccountIn": "_batch_116_ServiceAccountIn",
        "ServiceAccountOut": "_batch_117_ServiceAccountOut",
        "PlacementPolicyIn": "_batch_118_PlacementPolicyIn",
        "PlacementPolicyOut": "_batch_119_PlacementPolicyOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ReportAgentStateRequestIn"] = t.struct(
        {
            "metadata": t.proxy(renames["AgentMetadataIn"]).optional(),
            "agentInfo": t.proxy(renames["AgentInfoIn"]).optional(),
            "agentTimingInfo": t.proxy(renames["AgentTimingInfoIn"]).optional(),
        }
    ).named(renames["ReportAgentStateRequestIn"])
    types["ReportAgentStateRequestOut"] = t.struct(
        {
            "metadata": t.proxy(renames["AgentMetadataOut"]).optional(),
            "agentInfo": t.proxy(renames["AgentInfoOut"]).optional(),
            "agentTimingInfo": t.proxy(renames["AgentTimingInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportAgentStateRequestOut"])
    types["JobStatusIn"] = t.struct(
        {
            "runDuration": t.string().optional(),
            "taskGroups": t.struct({"_": t.string().optional()}).optional(),
            "state": t.string().optional(),
            "statusEvents": t.array(t.proxy(renames["StatusEventIn"])).optional(),
        }
    ).named(renames["JobStatusIn"])
    types["JobStatusOut"] = t.struct(
        {
            "runDuration": t.string().optional(),
            "taskGroups": t.struct({"_": t.string().optional()}).optional(),
            "state": t.string().optional(),
            "statusEvents": t.array(t.proxy(renames["StatusEventOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobStatusOut"])
    types["AttachedDiskIn"] = t.struct(
        {
            "newDisk": t.proxy(renames["DiskIn"]),
            "deviceName": t.string().optional(),
            "existingDisk": t.string().optional(),
        }
    ).named(renames["AttachedDiskIn"])
    types["AttachedDiskOut"] = t.struct(
        {
            "newDisk": t.proxy(renames["DiskOut"]),
            "deviceName": t.string().optional(),
            "existingDisk": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttachedDiskOut"])
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
    types["InstanceStatusIn"] = t.struct(
        {
            "taskPack": t.string().optional(),
            "machineType": t.string().optional(),
            "provisioningModel": t.string().optional(),
            "bootDisk": t.proxy(renames["DiskIn"]).optional(),
        }
    ).named(renames["InstanceStatusIn"])
    types["InstanceStatusOut"] = t.struct(
        {
            "taskPack": t.string().optional(),
            "machineType": t.string().optional(),
            "provisioningModel": t.string().optional(),
            "bootDisk": t.proxy(renames["DiskOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceStatusOut"])
    types["RunnableIn"] = t.struct(
        {
            "timeout": t.string().optional(),
            "container": t.proxy(renames["ContainerIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "background": t.boolean().optional(),
            "alwaysRun": t.boolean().optional(),
            "ignoreExitStatus": t.boolean().optional(),
            "script": t.proxy(renames["ScriptIn"]).optional(),
            "environment": t.proxy(renames["EnvironmentIn"]).optional(),
            "barrier": t.proxy(renames["BarrierIn"]).optional(),
        }
    ).named(renames["RunnableIn"])
    types["RunnableOut"] = t.struct(
        {
            "timeout": t.string().optional(),
            "container": t.proxy(renames["ContainerOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "background": t.boolean().optional(),
            "alwaysRun": t.boolean().optional(),
            "ignoreExitStatus": t.boolean().optional(),
            "script": t.proxy(renames["ScriptOut"]).optional(),
            "environment": t.proxy(renames["EnvironmentOut"]).optional(),
            "barrier": t.proxy(renames["BarrierOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunnableOut"])
    types["JobIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "allocationPolicy": t.proxy(renames["AllocationPolicyIn"]).optional(),
            "logsPolicy": t.proxy(renames["LogsPolicyIn"]).optional(),
            "priority": t.string().optional(),
            "taskGroups": t.array(t.proxy(renames["TaskGroupIn"])),
            "notifications": t.array(t.proxy(renames["JobNotificationIn"])).optional(),
        }
    ).named(renames["JobIn"])
    types["JobOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "allocationPolicy": t.proxy(renames["AllocationPolicyOut"]).optional(),
            "updateTime": t.string().optional(),
            "logsPolicy": t.proxy(renames["LogsPolicyOut"]).optional(),
            "uid": t.string().optional(),
            "createTime": t.string().optional(),
            "status": t.proxy(renames["JobStatusOut"]).optional(),
            "priority": t.string().optional(),
            "name": t.string().optional(),
            "taskGroups": t.array(t.proxy(renames["TaskGroupOut"])),
            "notifications": t.array(t.proxy(renames["JobNotificationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobOut"])
    types["ListTasksResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "tasks": t.array(t.proxy(renames["TaskIn"])).optional(),
        }
    ).named(renames["ListTasksResponseIn"])
    types["ListTasksResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "tasks": t.array(t.proxy(renames["TaskOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTasksResponseOut"])
    types["ActionConditionIn"] = t.struct(
        {"exitCodes": t.array(t.integer()).optional()}
    ).named(renames["ActionConditionIn"])
    types["ActionConditionOut"] = t.struct(
        {
            "exitCodes": t.array(t.integer()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActionConditionOut"])
    types["ListJobsResponseIn"] = t.struct(
        {
            "jobs": t.array(t.proxy(renames["JobIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListJobsResponseIn"])
    types["ListJobsResponseOut"] = t.struct(
        {
            "jobs": t.array(t.proxy(renames["JobOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListJobsResponseOut"])
    types["AgentTimingInfoIn"] = t.struct(
        {
            "bootTime": t.string().optional(),
            "scriptStartupTime": t.string().optional(),
            "agentStartupTime": t.string().optional(),
        }
    ).named(renames["AgentTimingInfoIn"])
    types["AgentTimingInfoOut"] = t.struct(
        {
            "bootTime": t.string().optional(),
            "scriptStartupTime": t.string().optional(),
            "agentStartupTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AgentTimingInfoOut"])
    types["ContainerIn"] = t.struct(
        {
            "entrypoint": t.string().optional(),
            "password": t.string().optional(),
            "imageUri": t.string().optional(),
            "blockExternalNetwork": t.boolean().optional(),
            "commands": t.array(t.string()).optional(),
            "options": t.string().optional(),
            "username": t.string().optional(),
            "volumes": t.array(t.string()).optional(),
        }
    ).named(renames["ContainerIn"])
    types["ContainerOut"] = t.struct(
        {
            "entrypoint": t.string().optional(),
            "password": t.string().optional(),
            "imageUri": t.string().optional(),
            "blockExternalNetwork": t.boolean().optional(),
            "commands": t.array(t.string()).optional(),
            "options": t.string().optional(),
            "username": t.string().optional(),
            "volumes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContainerOut"])
    types["ComputeResourceIn"] = t.struct(
        {
            "cpuMilli": t.string().optional(),
            "memoryMib": t.string().optional(),
            "bootDiskMib": t.string().optional(),
        }
    ).named(renames["ComputeResourceIn"])
    types["ComputeResourceOut"] = t.struct(
        {
            "cpuMilli": t.string().optional(),
            "memoryMib": t.string().optional(),
            "bootDiskMib": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComputeResourceOut"])
    types["LifecyclePolicyIn"] = t.struct(
        {
            "actionCondition": t.proxy(renames["ActionConditionIn"]).optional(),
            "action": t.string().optional(),
        }
    ).named(renames["LifecyclePolicyIn"])
    types["LifecyclePolicyOut"] = t.struct(
        {
            "actionCondition": t.proxy(renames["ActionConditionOut"]).optional(),
            "action": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LifecyclePolicyOut"])
    types["NetworkInterfaceIn"] = t.struct(
        {
            "network": t.string().optional(),
            "subnetwork": t.string().optional(),
            "noExternalIpAddress": t.boolean().optional(),
        }
    ).named(renames["NetworkInterfaceIn"])
    types["NetworkInterfaceOut"] = t.struct(
        {
            "network": t.string().optional(),
            "subnetwork": t.string().optional(),
            "noExternalIpAddress": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkInterfaceOut"])
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
    types["AgentMetadataIn"] = t.struct(
        {
            "instanceId": t.string().optional(),
            "creator": t.string().optional(),
            "instancePreemptionNoticeReceived": t.boolean().optional(),
            "version": t.string().optional(),
            "instance": t.string().optional(),
            "zone": t.string().optional(),
            "imageVersion": t.string().optional(),
            "creationTime": t.string().optional(),
            "osRelease": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["AgentMetadataIn"])
    types["AgentMetadataOut"] = t.struct(
        {
            "instanceId": t.string().optional(),
            "creator": t.string().optional(),
            "instancePreemptionNoticeReceived": t.boolean().optional(),
            "version": t.string().optional(),
            "instance": t.string().optional(),
            "zone": t.string().optional(),
            "imageVersion": t.string().optional(),
            "creationTime": t.string().optional(),
            "osRelease": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AgentMetadataOut"])
    types["BarrierIn"] = t.struct({"name": t.string().optional()}).named(
        renames["BarrierIn"]
    )
    types["BarrierOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BarrierOut"])
    types["GCSIn"] = t.struct({"remotePath": t.string().optional()}).named(
        renames["GCSIn"]
    )
    types["GCSOut"] = t.struct(
        {
            "remotePath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GCSOut"])
    types["MessageIn"] = t.struct(
        {
            "newJobState": t.string().optional(),
            "newTaskState": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["MessageIn"])
    types["MessageOut"] = t.struct(
        {
            "newJobState": t.string().optional(),
            "newTaskState": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MessageOut"])
    types["AgentContainerIn"] = t.struct(
        {
            "entrypoint": t.string().optional(),
            "imageUri": t.string().optional(),
            "volumes": t.array(t.string()).optional(),
            "commands": t.array(t.string()).optional(),
            "options": t.string().optional(),
        }
    ).named(renames["AgentContainerIn"])
    types["AgentContainerOut"] = t.struct(
        {
            "entrypoint": t.string().optional(),
            "imageUri": t.string().optional(),
            "volumes": t.array(t.string()).optional(),
            "commands": t.array(t.string()).optional(),
            "options": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AgentContainerOut"])
    types["LogsPolicyIn"] = t.struct(
        {"logsPath": t.string().optional(), "destination": t.string().optional()}
    ).named(renames["LogsPolicyIn"])
    types["LogsPolicyOut"] = t.struct(
        {
            "logsPath": t.string().optional(),
            "destination": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogsPolicyOut"])
    types["KMSEnvMapIn"] = t.struct(
        {"cipherText": t.string().optional(), "keyName": t.string().optional()}
    ).named(renames["KMSEnvMapIn"])
    types["KMSEnvMapOut"] = t.struct(
        {
            "cipherText": t.string().optional(),
            "keyName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KMSEnvMapOut"])
    types["AgentTaskIn"] = t.struct(
        {
            "reachedBarrier": t.string().optional(),
            "agentTaskSpec": t.proxy(renames["AgentTaskSpecIn"]).optional(),
            "status": t.proxy(renames["TaskStatusIn"]).optional(),
            "spec": t.proxy(renames["TaskSpecIn"]).optional(),
            "taskSource": t.string().optional(),
            "task": t.string().optional(),
            "intendedState": t.string().optional(),
        }
    ).named(renames["AgentTaskIn"])
    types["AgentTaskOut"] = t.struct(
        {
            "reachedBarrier": t.string().optional(),
            "agentTaskSpec": t.proxy(renames["AgentTaskSpecOut"]).optional(),
            "status": t.proxy(renames["TaskStatusOut"]).optional(),
            "spec": t.proxy(renames["TaskSpecOut"]).optional(),
            "taskSource": t.string().optional(),
            "task": t.string().optional(),
            "intendedState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AgentTaskOut"])
    types["InstancePolicyOrTemplateIn"] = t.struct(
        {
            "instanceTemplate": t.string().optional(),
            "installGpuDrivers": t.boolean().optional(),
            "policy": t.proxy(renames["InstancePolicyIn"]).optional(),
        }
    ).named(renames["InstancePolicyOrTemplateIn"])
    types["InstancePolicyOrTemplateOut"] = t.struct(
        {
            "instanceTemplate": t.string().optional(),
            "installGpuDrivers": t.boolean().optional(),
            "policy": t.proxy(renames["InstancePolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstancePolicyOrTemplateOut"])
    types["TaskGroupStatusIn"] = t.struct(
        {
            "instances": t.array(t.proxy(renames["InstanceStatusIn"])).optional(),
            "counts": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["TaskGroupStatusIn"])
    types["TaskGroupStatusOut"] = t.struct(
        {
            "instances": t.array(t.proxy(renames["InstanceStatusOut"])).optional(),
            "counts": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TaskGroupStatusOut"])
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
    types["LocationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["AcceleratorIn"] = t.struct(
        {
            "type": t.string().optional(),
            "installGpuDrivers": t.boolean().optional(),
            "count": t.string().optional(),
        }
    ).named(renames["AcceleratorIn"])
    types["AcceleratorOut"] = t.struct(
        {
            "type": t.string().optional(),
            "installGpuDrivers": t.boolean().optional(),
            "count": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AcceleratorOut"])
    types["AgentScriptIn"] = t.struct(
        {"text": t.string().optional(), "path": t.string().optional()}
    ).named(renames["AgentScriptIn"])
    types["AgentScriptOut"] = t.struct(
        {
            "text": t.string().optional(),
            "path": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AgentScriptOut"])
    types["AgentInfoIn"] = t.struct(
        {
            "reportTime": t.string().optional(),
            "state": t.string().optional(),
            "taskGroupId": t.string().optional(),
            "jobId": t.string().optional(),
            "tasks": t.array(t.proxy(renames["AgentTaskInfoIn"])).optional(),
        }
    ).named(renames["AgentInfoIn"])
    types["AgentInfoOut"] = t.struct(
        {
            "reportTime": t.string().optional(),
            "state": t.string().optional(),
            "taskGroupId": t.string().optional(),
            "jobId": t.string().optional(),
            "tasks": t.array(t.proxy(renames["AgentTaskInfoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AgentInfoOut"])
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
    types["LocationPolicyIn"] = t.struct(
        {"allowedLocations": t.array(t.string()).optional()}
    ).named(renames["LocationPolicyIn"])
    types["LocationPolicyOut"] = t.struct(
        {
            "allowedLocations": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationPolicyOut"])
    types["AgentTaskRunnableIn"] = t.struct(
        {
            "environment": t.proxy(renames["AgentEnvironmentIn"]).optional(),
            "background": t.boolean().optional(),
            "alwaysRun": t.boolean().optional(),
            "timeout": t.string().optional(),
            "ignoreExitStatus": t.boolean().optional(),
            "script": t.proxy(renames["AgentScriptIn"]).optional(),
            "container": t.proxy(renames["AgentContainerIn"]).optional(),
        }
    ).named(renames["AgentTaskRunnableIn"])
    types["AgentTaskRunnableOut"] = t.struct(
        {
            "environment": t.proxy(renames["AgentEnvironmentOut"]).optional(),
            "background": t.boolean().optional(),
            "alwaysRun": t.boolean().optional(),
            "timeout": t.string().optional(),
            "ignoreExitStatus": t.boolean().optional(),
            "script": t.proxy(renames["AgentScriptOut"]).optional(),
            "container": t.proxy(renames["AgentContainerOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AgentTaskRunnableOut"])
    types["OperationIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationOut"])
    types["TaskExecutionIn"] = t.struct({"exitCode": t.integer().optional()}).named(
        renames["TaskExecutionIn"]
    )
    types["TaskExecutionOut"] = t.struct(
        {
            "exitCode": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TaskExecutionOut"])
    types["TaskGroupIn"] = t.struct(
        {
            "permissiveSsh": t.boolean().optional(),
            "taskSpec": t.proxy(renames["TaskSpecIn"]),
            "parallelism": t.string().optional(),
            "requireHostsFile": t.boolean().optional(),
            "taskCountPerNode": t.string().optional(),
            "schedulingPolicy": t.string().optional(),
            "taskEnvironments": t.array(t.proxy(renames["EnvironmentIn"])).optional(),
            "taskCount": t.string().optional(),
        }
    ).named(renames["TaskGroupIn"])
    types["TaskGroupOut"] = t.struct(
        {
            "permissiveSsh": t.boolean().optional(),
            "taskSpec": t.proxy(renames["TaskSpecOut"]),
            "parallelism": t.string().optional(),
            "name": t.string().optional(),
            "requireHostsFile": t.boolean().optional(),
            "taskCountPerNode": t.string().optional(),
            "schedulingPolicy": t.string().optional(),
            "taskEnvironments": t.array(t.proxy(renames["EnvironmentOut"])).optional(),
            "taskCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TaskGroupOut"])
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
    types["TaskSpecIn"] = t.struct(
        {
            "environments": t.struct({"_": t.string().optional()}).optional(),
            "computeResource": t.proxy(renames["ComputeResourceIn"]).optional(),
            "volumes": t.array(t.proxy(renames["VolumeIn"])).optional(),
            "maxRetryCount": t.integer().optional(),
            "runnables": t.array(t.proxy(renames["RunnableIn"])).optional(),
            "environment": t.proxy(renames["EnvironmentIn"]).optional(),
            "lifecyclePolicies": t.array(
                t.proxy(renames["LifecyclePolicyIn"])
            ).optional(),
            "maxRunDuration": t.string().optional(),
        }
    ).named(renames["TaskSpecIn"])
    types["TaskSpecOut"] = t.struct(
        {
            "environments": t.struct({"_": t.string().optional()}).optional(),
            "computeResource": t.proxy(renames["ComputeResourceOut"]).optional(),
            "volumes": t.array(t.proxy(renames["VolumeOut"])).optional(),
            "maxRetryCount": t.integer().optional(),
            "runnables": t.array(t.proxy(renames["RunnableOut"])).optional(),
            "environment": t.proxy(renames["EnvironmentOut"]).optional(),
            "lifecyclePolicies": t.array(
                t.proxy(renames["LifecyclePolicyOut"])
            ).optional(),
            "maxRunDuration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TaskSpecOut"])
    types["InstancePolicyIn"] = t.struct(
        {
            "provisioningModel": t.string().optional(),
            "machineType": t.string().optional(),
            "minCpuPlatform": t.string().optional(),
            "accelerators": t.array(t.proxy(renames["AcceleratorIn"])).optional(),
            "bootDisk": t.proxy(renames["DiskIn"]).optional(),
            "disks": t.array(t.proxy(renames["AttachedDiskIn"])).optional(),
        }
    ).named(renames["InstancePolicyIn"])
    types["InstancePolicyOut"] = t.struct(
        {
            "provisioningModel": t.string().optional(),
            "machineType": t.string().optional(),
            "minCpuPlatform": t.string().optional(),
            "accelerators": t.array(t.proxy(renames["AcceleratorOut"])).optional(),
            "bootDisk": t.proxy(renames["DiskOut"]).optional(),
            "disks": t.array(t.proxy(renames["AttachedDiskOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstancePolicyOut"])
    types["DiskIn"] = t.struct(
        {
            "sizeGb": t.string().optional(),
            "diskInterface": t.string().optional(),
            "type": t.string().optional(),
            "snapshot": t.string().optional(),
            "image": t.string().optional(),
        }
    ).named(renames["DiskIn"])
    types["DiskOut"] = t.struct(
        {
            "sizeGb": t.string().optional(),
            "diskInterface": t.string().optional(),
            "type": t.string().optional(),
            "snapshot": t.string().optional(),
            "image": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiskOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["JobNotificationIn"] = t.struct(
        {
            "pubsubTopic": t.string().optional(),
            "message": t.proxy(renames["MessageIn"]).optional(),
        }
    ).named(renames["JobNotificationIn"])
    types["JobNotificationOut"] = t.struct(
        {
            "pubsubTopic": t.string().optional(),
            "message": t.proxy(renames["MessageOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobNotificationOut"])
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
    types["AgentTaskSpecIn"] = t.struct(
        {
            "environment": t.proxy(renames["AgentEnvironmentIn"]).optional(),
            "maxRunDuration": t.string().optional(),
            "runnables": t.array(t.proxy(renames["AgentTaskRunnableIn"])).optional(),
        }
    ).named(renames["AgentTaskSpecIn"])
    types["AgentTaskSpecOut"] = t.struct(
        {
            "environment": t.proxy(renames["AgentEnvironmentOut"]).optional(),
            "maxRunDuration": t.string().optional(),
            "runnables": t.array(t.proxy(renames["AgentTaskRunnableOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AgentTaskSpecOut"])
    types["EnvironmentIn"] = t.struct(
        {
            "variables": t.struct({"_": t.string().optional()}).optional(),
            "secretVariables": t.struct({"_": t.string().optional()}).optional(),
            "encryptedVariables": t.proxy(renames["KMSEnvMapIn"]).optional(),
        }
    ).named(renames["EnvironmentIn"])
    types["EnvironmentOut"] = t.struct(
        {
            "variables": t.struct({"_": t.string().optional()}).optional(),
            "secretVariables": t.struct({"_": t.string().optional()}).optional(),
            "encryptedVariables": t.proxy(renames["KMSEnvMapOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnvironmentOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "apiVersion": t.string().optional(),
            "target": t.string().optional(),
            "verb": t.string().optional(),
            "statusMessage": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
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
    types["AgentKMSEnvMapIn"] = t.struct(
        {"keyName": t.string().optional(), "cipherText": t.string().optional()}
    ).named(renames["AgentKMSEnvMapIn"])
    types["AgentKMSEnvMapOut"] = t.struct(
        {
            "keyName": t.string().optional(),
            "cipherText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AgentKMSEnvMapOut"])
    types["AgentEnvironmentIn"] = t.struct(
        {
            "encryptedVariables": t.proxy(renames["AgentKMSEnvMapIn"]).optional(),
            "variables": t.struct({"_": t.string().optional()}).optional(),
            "secretVariables": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["AgentEnvironmentIn"])
    types["AgentEnvironmentOut"] = t.struct(
        {
            "encryptedVariables": t.proxy(renames["AgentKMSEnvMapOut"]).optional(),
            "variables": t.struct({"_": t.string().optional()}).optional(),
            "secretVariables": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AgentEnvironmentOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["StatusEventIn"] = t.struct(
        {
            "type": t.string().optional(),
            "eventTime": t.string().optional(),
            "taskState": t.string().optional(),
            "taskExecution": t.proxy(renames["TaskExecutionIn"]).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["StatusEventIn"])
    types["StatusEventOut"] = t.struct(
        {
            "type": t.string().optional(),
            "eventTime": t.string().optional(),
            "taskState": t.string().optional(),
            "taskExecution": t.proxy(renames["TaskExecutionOut"]).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusEventOut"])
    types["AllocationPolicyIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "location": t.proxy(renames["LocationPolicyIn"]).optional(),
            "serviceAccount": t.proxy(renames["ServiceAccountIn"]).optional(),
            "instances": t.array(
                t.proxy(renames["InstancePolicyOrTemplateIn"])
            ).optional(),
            "placement": t.proxy(renames["PlacementPolicyIn"]).optional(),
            "network": t.proxy(renames["NetworkPolicyIn"]).optional(),
        }
    ).named(renames["AllocationPolicyIn"])
    types["AllocationPolicyOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "location": t.proxy(renames["LocationPolicyOut"]).optional(),
            "serviceAccount": t.proxy(renames["ServiceAccountOut"]).optional(),
            "instances": t.array(
                t.proxy(renames["InstancePolicyOrTemplateOut"])
            ).optional(),
            "placement": t.proxy(renames["PlacementPolicyOut"]).optional(),
            "network": t.proxy(renames["NetworkPolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AllocationPolicyOut"])
    types["TaskStatusIn"] = t.struct(
        {
            "statusEvents": t.array(t.proxy(renames["StatusEventIn"])).optional(),
            "state": t.string().optional(),
        }
    ).named(renames["TaskStatusIn"])
    types["TaskStatusOut"] = t.struct(
        {
            "statusEvents": t.array(t.proxy(renames["StatusEventOut"])).optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TaskStatusOut"])
    types["VolumeIn"] = t.struct(
        {
            "nfs": t.proxy(renames["NFSIn"]).optional(),
            "deviceName": t.string().optional(),
            "gcs": t.proxy(renames["GCSIn"]).optional(),
            "mountOptions": t.array(t.string()).optional(),
            "mountPath": t.string().optional(),
        }
    ).named(renames["VolumeIn"])
    types["VolumeOut"] = t.struct(
        {
            "nfs": t.proxy(renames["NFSOut"]).optional(),
            "deviceName": t.string().optional(),
            "gcs": t.proxy(renames["GCSOut"]).optional(),
            "mountOptions": t.array(t.string()).optional(),
            "mountPath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VolumeOut"])
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
    types["PlacementPolicyIn"] = t.struct(
        {"collocation": t.string().optional(), "maxDistance": t.string().optional()}
    ).named(renames["PlacementPolicyIn"])
    types["PlacementPolicyOut"] = t.struct(
        {
            "collocation": t.string().optional(),
            "maxDistance": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlacementPolicyOut"])

    functions = {}
    functions["projectsLocationsGet"] = batch.get(
        "v1/{name}/locations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
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
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStateReport"] = batch.post(
        "v1/{parent}/state:report",
        t.struct(
            {
                "parent": t.string(),
                "metadata": t.proxy(renames["AgentMetadataIn"]).optional(),
                "agentInfo": t.proxy(renames["AgentInfoIn"]).optional(),
                "agentTimingInfo": t.proxy(renames["AgentTimingInfoIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReportAgentStateResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsList"] = batch.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsCreate"] = batch.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsDelete"] = batch.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsGet"] = batch.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
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
                "filter": t.string().optional(),
                "name": t.string().optional(),
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
                "filter": t.string().optional(),
                "name": t.string().optional(),
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
                "filter": t.string().optional(),
                "name": t.string().optional(),
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
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="batch", renames=renames, types=Box(types), functions=Box(functions)
    )
