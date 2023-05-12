from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_batch() -> Import:
    batch = HTTPRuntime("https://batch.googleapis.com/")

    renames = {
        "ErrorResponse": "_batch_1_ErrorResponse",
        "TaskGroupIn": "_batch_2_TaskGroupIn",
        "TaskGroupOut": "_batch_3_TaskGroupOut",
        "EnvironmentIn": "_batch_4_EnvironmentIn",
        "EnvironmentOut": "_batch_5_EnvironmentOut",
        "TaskSpecIn": "_batch_6_TaskSpecIn",
        "TaskSpecOut": "_batch_7_TaskSpecOut",
        "ListTasksResponseIn": "_batch_8_ListTasksResponseIn",
        "ListTasksResponseOut": "_batch_9_ListTasksResponseOut",
        "RunnableIn": "_batch_10_RunnableIn",
        "RunnableOut": "_batch_11_RunnableOut",
        "ScriptIn": "_batch_12_ScriptIn",
        "ScriptOut": "_batch_13_ScriptOut",
        "ListJobsResponseIn": "_batch_14_ListJobsResponseIn",
        "ListJobsResponseOut": "_batch_15_ListJobsResponseOut",
        "MessageIn": "_batch_16_MessageIn",
        "MessageOut": "_batch_17_MessageOut",
        "DiskIn": "_batch_18_DiskIn",
        "DiskOut": "_batch_19_DiskOut",
        "CancelOperationRequestIn": "_batch_20_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_batch_21_CancelOperationRequestOut",
        "PlacementPolicyIn": "_batch_22_PlacementPolicyIn",
        "PlacementPolicyOut": "_batch_23_PlacementPolicyOut",
        "OperationMetadataIn": "_batch_24_OperationMetadataIn",
        "OperationMetadataOut": "_batch_25_OperationMetadataOut",
        "ComputeResourceIn": "_batch_26_ComputeResourceIn",
        "ComputeResourceOut": "_batch_27_ComputeResourceOut",
        "ListLocationsResponseIn": "_batch_28_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_batch_29_ListLocationsResponseOut",
        "EmptyIn": "_batch_30_EmptyIn",
        "EmptyOut": "_batch_31_EmptyOut",
        "AgentTimingInfoIn": "_batch_32_AgentTimingInfoIn",
        "AgentTimingInfoOut": "_batch_33_AgentTimingInfoOut",
        "BarrierIn": "_batch_34_BarrierIn",
        "BarrierOut": "_batch_35_BarrierOut",
        "NetworkPolicyIn": "_batch_36_NetworkPolicyIn",
        "NetworkPolicyOut": "_batch_37_NetworkPolicyOut",
        "TaskStatusIn": "_batch_38_TaskStatusIn",
        "TaskStatusOut": "_batch_39_TaskStatusOut",
        "VolumeIn": "_batch_40_VolumeIn",
        "VolumeOut": "_batch_41_VolumeOut",
        "TaskGroupStatusIn": "_batch_42_TaskGroupStatusIn",
        "TaskGroupStatusOut": "_batch_43_TaskGroupStatusOut",
        "ServiceAccountIn": "_batch_44_ServiceAccountIn",
        "ServiceAccountOut": "_batch_45_ServiceAccountOut",
        "JobNotificationIn": "_batch_46_JobNotificationIn",
        "JobNotificationOut": "_batch_47_JobNotificationOut",
        "NetworkInterfaceIn": "_batch_48_NetworkInterfaceIn",
        "NetworkInterfaceOut": "_batch_49_NetworkInterfaceOut",
        "StatusEventIn": "_batch_50_StatusEventIn",
        "StatusEventOut": "_batch_51_StatusEventOut",
        "TaskIn": "_batch_52_TaskIn",
        "TaskOut": "_batch_53_TaskOut",
        "AgentTaskInfoIn": "_batch_54_AgentTaskInfoIn",
        "AgentTaskInfoOut": "_batch_55_AgentTaskInfoOut",
        "OperationIn": "_batch_56_OperationIn",
        "OperationOut": "_batch_57_OperationOut",
        "AcceleratorIn": "_batch_58_AcceleratorIn",
        "AcceleratorOut": "_batch_59_AcceleratorOut",
        "LocationIn": "_batch_60_LocationIn",
        "LocationOut": "_batch_61_LocationOut",
        "ActionConditionIn": "_batch_62_ActionConditionIn",
        "ActionConditionOut": "_batch_63_ActionConditionOut",
        "LocationPolicyIn": "_batch_64_LocationPolicyIn",
        "LocationPolicyOut": "_batch_65_LocationPolicyOut",
        "JobStatusIn": "_batch_66_JobStatusIn",
        "JobStatusOut": "_batch_67_JobStatusOut",
        "LogsPolicyIn": "_batch_68_LogsPolicyIn",
        "LogsPolicyOut": "_batch_69_LogsPolicyOut",
        "AgentMetadataIn": "_batch_70_AgentMetadataIn",
        "AgentMetadataOut": "_batch_71_AgentMetadataOut",
        "AgentInfoIn": "_batch_72_AgentInfoIn",
        "AgentInfoOut": "_batch_73_AgentInfoOut",
        "LifecyclePolicyIn": "_batch_74_LifecyclePolicyIn",
        "LifecyclePolicyOut": "_batch_75_LifecyclePolicyOut",
        "TaskExecutionIn": "_batch_76_TaskExecutionIn",
        "TaskExecutionOut": "_batch_77_TaskExecutionOut",
        "ContainerIn": "_batch_78_ContainerIn",
        "ContainerOut": "_batch_79_ContainerOut",
        "JobIn": "_batch_80_JobIn",
        "JobOut": "_batch_81_JobOut",
        "AgentTaskIn": "_batch_82_AgentTaskIn",
        "AgentTaskOut": "_batch_83_AgentTaskOut",
        "KMSEnvMapIn": "_batch_84_KMSEnvMapIn",
        "KMSEnvMapOut": "_batch_85_KMSEnvMapOut",
        "InstancePolicyIn": "_batch_86_InstancePolicyIn",
        "InstancePolicyOut": "_batch_87_InstancePolicyOut",
        "AllocationPolicyIn": "_batch_88_AllocationPolicyIn",
        "AllocationPolicyOut": "_batch_89_AllocationPolicyOut",
        "ReportAgentStateResponseIn": "_batch_90_ReportAgentStateResponseIn",
        "ReportAgentStateResponseOut": "_batch_91_ReportAgentStateResponseOut",
        "InstancePolicyOrTemplateIn": "_batch_92_InstancePolicyOrTemplateIn",
        "InstancePolicyOrTemplateOut": "_batch_93_InstancePolicyOrTemplateOut",
        "AttachedDiskIn": "_batch_94_AttachedDiskIn",
        "AttachedDiskOut": "_batch_95_AttachedDiskOut",
        "StatusIn": "_batch_96_StatusIn",
        "StatusOut": "_batch_97_StatusOut",
        "ListOperationsResponseIn": "_batch_98_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_batch_99_ListOperationsResponseOut",
        "InstanceStatusIn": "_batch_100_InstanceStatusIn",
        "InstanceStatusOut": "_batch_101_InstanceStatusOut",
        "GCSIn": "_batch_102_GCSIn",
        "GCSOut": "_batch_103_GCSOut",
        "NFSIn": "_batch_104_NFSIn",
        "NFSOut": "_batch_105_NFSOut",
        "ReportAgentStateRequestIn": "_batch_106_ReportAgentStateRequestIn",
        "ReportAgentStateRequestOut": "_batch_107_ReportAgentStateRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["TaskGroupIn"] = t.struct(
        {
            "taskCount": t.string().optional(),
            "permissiveSsh": t.boolean().optional(),
            "taskEnvironments": t.array(t.proxy(renames["EnvironmentIn"])).optional(),
            "taskCountPerNode": t.string().optional(),
            "parallelism": t.string().optional(),
            "requireHostsFile": t.boolean().optional(),
            "taskSpec": t.proxy(renames["TaskSpecIn"]),
        }
    ).named(renames["TaskGroupIn"])
    types["TaskGroupOut"] = t.struct(
        {
            "taskCount": t.string().optional(),
            "permissiveSsh": t.boolean().optional(),
            "name": t.string().optional(),
            "taskEnvironments": t.array(t.proxy(renames["EnvironmentOut"])).optional(),
            "taskCountPerNode": t.string().optional(),
            "parallelism": t.string().optional(),
            "requireHostsFile": t.boolean().optional(),
            "taskSpec": t.proxy(renames["TaskSpecOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TaskGroupOut"])
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
    types["TaskSpecIn"] = t.struct(
        {
            "maxRunDuration": t.string().optional(),
            "lifecyclePolicies": t.array(
                t.proxy(renames["LifecyclePolicyIn"])
            ).optional(),
            "maxRetryCount": t.integer().optional(),
            "volumes": t.array(t.proxy(renames["VolumeIn"])).optional(),
            "environments": t.struct({"_": t.string().optional()}).optional(),
            "runnables": t.array(t.proxy(renames["RunnableIn"])).optional(),
            "environment": t.proxy(renames["EnvironmentIn"]).optional(),
            "computeResource": t.proxy(renames["ComputeResourceIn"]).optional(),
        }
    ).named(renames["TaskSpecIn"])
    types["TaskSpecOut"] = t.struct(
        {
            "maxRunDuration": t.string().optional(),
            "lifecyclePolicies": t.array(
                t.proxy(renames["LifecyclePolicyOut"])
            ).optional(),
            "maxRetryCount": t.integer().optional(),
            "volumes": t.array(t.proxy(renames["VolumeOut"])).optional(),
            "environments": t.struct({"_": t.string().optional()}).optional(),
            "runnables": t.array(t.proxy(renames["RunnableOut"])).optional(),
            "environment": t.proxy(renames["EnvironmentOut"]).optional(),
            "computeResource": t.proxy(renames["ComputeResourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TaskSpecOut"])
    types["ListTasksResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "tasks": t.array(t.proxy(renames["TaskIn"])).optional(),
        }
    ).named(renames["ListTasksResponseIn"])
    types["ListTasksResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "tasks": t.array(t.proxy(renames["TaskOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTasksResponseOut"])
    types["RunnableIn"] = t.struct(
        {
            "environment": t.proxy(renames["EnvironmentIn"]).optional(),
            "alwaysRun": t.boolean().optional(),
            "script": t.proxy(renames["ScriptIn"]).optional(),
            "container": t.proxy(renames["ContainerIn"]).optional(),
            "timeout": t.string().optional(),
            "background": t.boolean().optional(),
            "ignoreExitStatus": t.boolean().optional(),
            "barrier": t.proxy(renames["BarrierIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["RunnableIn"])
    types["RunnableOut"] = t.struct(
        {
            "environment": t.proxy(renames["EnvironmentOut"]).optional(),
            "alwaysRun": t.boolean().optional(),
            "script": t.proxy(renames["ScriptOut"]).optional(),
            "container": t.proxy(renames["ContainerOut"]).optional(),
            "timeout": t.string().optional(),
            "background": t.boolean().optional(),
            "ignoreExitStatus": t.boolean().optional(),
            "barrier": t.proxy(renames["BarrierOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunnableOut"])
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
    types["MessageIn"] = t.struct(
        {
            "newJobState": t.string().optional(),
            "type": t.string().optional(),
            "newTaskState": t.string().optional(),
        }
    ).named(renames["MessageIn"])
    types["MessageOut"] = t.struct(
        {
            "newJobState": t.string().optional(),
            "type": t.string().optional(),
            "newTaskState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MessageOut"])
    types["DiskIn"] = t.struct(
        {
            "snapshot": t.string().optional(),
            "sizeGb": t.string().optional(),
            "diskInterface": t.string().optional(),
            "type": t.string().optional(),
            "image": t.string().optional(),
        }
    ).named(renames["DiskIn"])
    types["DiskOut"] = t.struct(
        {
            "snapshot": t.string().optional(),
            "sizeGb": t.string().optional(),
            "diskInterface": t.string().optional(),
            "type": t.string().optional(),
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
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "target": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "verb": t.string().optional(),
            "apiVersion": t.string().optional(),
            "statusMessage": t.string().optional(),
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["AgentTimingInfoIn"] = t.struct(
        {
            "agentStartupTime": t.string().optional(),
            "scriptStartupTime": t.string().optional(),
            "bootTime": t.string().optional(),
        }
    ).named(renames["AgentTimingInfoIn"])
    types["AgentTimingInfoOut"] = t.struct(
        {
            "agentStartupTime": t.string().optional(),
            "scriptStartupTime": t.string().optional(),
            "bootTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AgentTimingInfoOut"])
    types["BarrierIn"] = t.struct({"name": t.string().optional()}).named(
        renames["BarrierIn"]
    )
    types["BarrierOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BarrierOut"])
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
            "deviceName": t.string().optional(),
            "gcs": t.proxy(renames["GCSIn"]).optional(),
            "mountOptions": t.array(t.string()).optional(),
            "nfs": t.proxy(renames["NFSIn"]).optional(),
            "mountPath": t.string().optional(),
        }
    ).named(renames["VolumeIn"])
    types["VolumeOut"] = t.struct(
        {
            "deviceName": t.string().optional(),
            "gcs": t.proxy(renames["GCSOut"]).optional(),
            "mountOptions": t.array(t.string()).optional(),
            "nfs": t.proxy(renames["NFSOut"]).optional(),
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
    types["ServiceAccountIn"] = t.struct(
        {"email": t.string().optional(), "scopes": t.array(t.string()).optional()}
    ).named(renames["ServiceAccountIn"])
    types["ServiceAccountOut"] = t.struct(
        {
            "email": t.string().optional(),
            "scopes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceAccountOut"])
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
    types["StatusEventIn"] = t.struct(
        {
            "taskExecution": t.proxy(renames["TaskExecutionIn"]).optional(),
            "description": t.string().optional(),
            "eventTime": t.string().optional(),
            "taskState": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["StatusEventIn"])
    types["StatusEventOut"] = t.struct(
        {
            "taskExecution": t.proxy(renames["TaskExecutionOut"]).optional(),
            "description": t.string().optional(),
            "eventTime": t.string().optional(),
            "taskState": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusEventOut"])
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
    types["AgentTaskInfoIn"] = t.struct(
        {
            "taskStatus": t.proxy(renames["TaskStatusIn"]).optional(),
            "taskId": t.string().optional(),
            "runnable": t.string().optional(),
        }
    ).named(renames["AgentTaskInfoIn"])
    types["AgentTaskInfoOut"] = t.struct(
        {
            "taskStatus": t.proxy(renames["TaskStatusOut"]).optional(),
            "taskId": t.string().optional(),
            "runnable": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AgentTaskInfoOut"])
    types["OperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationOut"])
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
    types["LocationIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["ActionConditionIn"] = t.struct(
        {"exitCodes": t.array(t.integer()).optional()}
    ).named(renames["ActionConditionIn"])
    types["ActionConditionOut"] = t.struct(
        {
            "exitCodes": t.array(t.integer()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActionConditionOut"])
    types["LocationPolicyIn"] = t.struct(
        {"allowedLocations": t.array(t.string()).optional()}
    ).named(renames["LocationPolicyIn"])
    types["LocationPolicyOut"] = t.struct(
        {
            "allowedLocations": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationPolicyOut"])
    types["JobStatusIn"] = t.struct(
        {
            "state": t.string().optional(),
            "taskGroups": t.struct({"_": t.string().optional()}).optional(),
            "statusEvents": t.array(t.proxy(renames["StatusEventIn"])).optional(),
            "runDuration": t.string().optional(),
        }
    ).named(renames["JobStatusIn"])
    types["JobStatusOut"] = t.struct(
        {
            "state": t.string().optional(),
            "taskGroups": t.struct({"_": t.string().optional()}).optional(),
            "statusEvents": t.array(t.proxy(renames["StatusEventOut"])).optional(),
            "runDuration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobStatusOut"])
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
    types["AgentMetadataIn"] = t.struct(
        {
            "creator": t.string().optional(),
            "instancePreemptionNoticeReceived": t.boolean().optional(),
            "zone": t.string().optional(),
            "instanceId": t.string().optional(),
            "creationTime": t.string().optional(),
            "imageVersion": t.string().optional(),
            "version": t.string().optional(),
            "instance": t.string().optional(),
            "osRelease": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["AgentMetadataIn"])
    types["AgentMetadataOut"] = t.struct(
        {
            "creator": t.string().optional(),
            "instancePreemptionNoticeReceived": t.boolean().optional(),
            "zone": t.string().optional(),
            "instanceId": t.string().optional(),
            "creationTime": t.string().optional(),
            "imageVersion": t.string().optional(),
            "version": t.string().optional(),
            "instance": t.string().optional(),
            "osRelease": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AgentMetadataOut"])
    types["AgentInfoIn"] = t.struct(
        {
            "tasks": t.array(t.proxy(renames["AgentTaskInfoIn"])).optional(),
            "taskGroupId": t.string().optional(),
            "reportTime": t.string().optional(),
            "jobId": t.string().optional(),
            "state": t.string().optional(),
        }
    ).named(renames["AgentInfoIn"])
    types["AgentInfoOut"] = t.struct(
        {
            "tasks": t.array(t.proxy(renames["AgentTaskInfoOut"])).optional(),
            "taskGroupId": t.string().optional(),
            "reportTime": t.string().optional(),
            "jobId": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AgentInfoOut"])
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
    types["TaskExecutionIn"] = t.struct({"exitCode": t.integer().optional()}).named(
        renames["TaskExecutionIn"]
    )
    types["TaskExecutionOut"] = t.struct(
        {
            "exitCode": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TaskExecutionOut"])
    types["ContainerIn"] = t.struct(
        {
            "options": t.string().optional(),
            "volumes": t.array(t.string()).optional(),
            "blockExternalNetwork": t.boolean().optional(),
            "imageUri": t.string().optional(),
            "username": t.string().optional(),
            "entrypoint": t.string().optional(),
            "commands": t.array(t.string()).optional(),
            "password": t.string().optional(),
        }
    ).named(renames["ContainerIn"])
    types["ContainerOut"] = t.struct(
        {
            "options": t.string().optional(),
            "volumes": t.array(t.string()).optional(),
            "blockExternalNetwork": t.boolean().optional(),
            "imageUri": t.string().optional(),
            "username": t.string().optional(),
            "entrypoint": t.string().optional(),
            "commands": t.array(t.string()).optional(),
            "password": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContainerOut"])
    types["JobIn"] = t.struct(
        {
            "priority": t.string().optional(),
            "taskGroups": t.array(t.proxy(renames["TaskGroupIn"])),
            "notifications": t.array(t.proxy(renames["JobNotificationIn"])).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "allocationPolicy": t.proxy(renames["AllocationPolicyIn"]).optional(),
            "logsPolicy": t.proxy(renames["LogsPolicyIn"]).optional(),
        }
    ).named(renames["JobIn"])
    types["JobOut"] = t.struct(
        {
            "status": t.proxy(renames["JobStatusOut"]).optional(),
            "updateTime": t.string().optional(),
            "priority": t.string().optional(),
            "taskGroups": t.array(t.proxy(renames["TaskGroupOut"])),
            "notifications": t.array(t.proxy(renames["JobNotificationOut"])).optional(),
            "uid": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "allocationPolicy": t.proxy(renames["AllocationPolicyOut"]).optional(),
            "createTime": t.string().optional(),
            "logsPolicy": t.proxy(renames["LogsPolicyOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobOut"])
    types["AgentTaskIn"] = t.struct(
        {
            "intendedState": t.string().optional(),
            "spec": t.proxy(renames["TaskSpecIn"]).optional(),
            "task": t.string().optional(),
            "taskSource": t.string().optional(),
            "status": t.proxy(renames["TaskStatusIn"]).optional(),
            "reachedBarrier": t.string().optional(),
        }
    ).named(renames["AgentTaskIn"])
    types["AgentTaskOut"] = t.struct(
        {
            "intendedState": t.string().optional(),
            "spec": t.proxy(renames["TaskSpecOut"]).optional(),
            "task": t.string().optional(),
            "taskSource": t.string().optional(),
            "status": t.proxy(renames["TaskStatusOut"]).optional(),
            "reachedBarrier": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AgentTaskOut"])
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
    types["InstancePolicyIn"] = t.struct(
        {
            "minCpuPlatform": t.string().optional(),
            "disks": t.array(t.proxy(renames["AttachedDiskIn"])).optional(),
            "bootDisk": t.proxy(renames["DiskIn"]).optional(),
            "accelerators": t.array(t.proxy(renames["AcceleratorIn"])).optional(),
            "provisioningModel": t.string().optional(),
            "machineType": t.string().optional(),
        }
    ).named(renames["InstancePolicyIn"])
    types["InstancePolicyOut"] = t.struct(
        {
            "minCpuPlatform": t.string().optional(),
            "disks": t.array(t.proxy(renames["AttachedDiskOut"])).optional(),
            "bootDisk": t.proxy(renames["DiskOut"]).optional(),
            "accelerators": t.array(t.proxy(renames["AcceleratorOut"])).optional(),
            "provisioningModel": t.string().optional(),
            "machineType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstancePolicyOut"])
    types["AllocationPolicyIn"] = t.struct(
        {
            "network": t.proxy(renames["NetworkPolicyIn"]).optional(),
            "location": t.proxy(renames["LocationPolicyIn"]).optional(),
            "instances": t.array(
                t.proxy(renames["InstancePolicyOrTemplateIn"])
            ).optional(),
            "serviceAccount": t.proxy(renames["ServiceAccountIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "placement": t.proxy(renames["PlacementPolicyIn"]).optional(),
        }
    ).named(renames["AllocationPolicyIn"])
    types["AllocationPolicyOut"] = t.struct(
        {
            "network": t.proxy(renames["NetworkPolicyOut"]).optional(),
            "location": t.proxy(renames["LocationPolicyOut"]).optional(),
            "instances": t.array(
                t.proxy(renames["InstancePolicyOrTemplateOut"])
            ).optional(),
            "serviceAccount": t.proxy(renames["ServiceAccountOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "placement": t.proxy(renames["PlacementPolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AllocationPolicyOut"])
    types["ReportAgentStateResponseIn"] = t.struct(
        {
            "tasks": t.array(t.proxy(renames["AgentTaskIn"])).optional(),
            "defaultReportInterval": t.string().optional(),
            "minReportInterval": t.string().optional(),
        }
    ).named(renames["ReportAgentStateResponseIn"])
    types["ReportAgentStateResponseOut"] = t.struct(
        {
            "tasks": t.array(t.proxy(renames["AgentTaskOut"])).optional(),
            "defaultReportInterval": t.string().optional(),
            "minReportInterval": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportAgentStateResponseOut"])
    types["InstancePolicyOrTemplateIn"] = t.struct(
        {
            "installGpuDrivers": t.boolean().optional(),
            "policy": t.proxy(renames["InstancePolicyIn"]).optional(),
            "instanceTemplate": t.string().optional(),
        }
    ).named(renames["InstancePolicyOrTemplateIn"])
    types["InstancePolicyOrTemplateOut"] = t.struct(
        {
            "installGpuDrivers": t.boolean().optional(),
            "policy": t.proxy(renames["InstancePolicyOut"]).optional(),
            "instanceTemplate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstancePolicyOrTemplateOut"])
    types["AttachedDiskIn"] = t.struct(
        {
            "newDisk": t.proxy(renames["DiskIn"]),
            "existingDisk": t.string().optional(),
            "deviceName": t.string().optional(),
        }
    ).named(renames["AttachedDiskIn"])
    types["AttachedDiskOut"] = t.struct(
        {
            "newDisk": t.proxy(renames["DiskOut"]),
            "existingDisk": t.string().optional(),
            "deviceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttachedDiskOut"])
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
    types["InstanceStatusIn"] = t.struct(
        {
            "bootDisk": t.proxy(renames["DiskIn"]).optional(),
            "provisioningModel": t.string().optional(),
            "taskPack": t.string().optional(),
            "machineType": t.string().optional(),
        }
    ).named(renames["InstanceStatusIn"])
    types["InstanceStatusOut"] = t.struct(
        {
            "bootDisk": t.proxy(renames["DiskOut"]).optional(),
            "provisioningModel": t.string().optional(),
            "taskPack": t.string().optional(),
            "machineType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceStatusOut"])
    types["GCSIn"] = t.struct({"remotePath": t.string().optional()}).named(
        renames["GCSIn"]
    )
    types["GCSOut"] = t.struct(
        {
            "remotePath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GCSOut"])
    types["NFSIn"] = t.struct(
        {"remotePath": t.string().optional(), "server": t.string().optional()}
    ).named(renames["NFSIn"])
    types["NFSOut"] = t.struct(
        {
            "remotePath": t.string().optional(),
            "server": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NFSOut"])
    types["ReportAgentStateRequestIn"] = t.struct(
        {
            "agentTimingInfo": t.proxy(renames["AgentTimingInfoIn"]).optional(),
            "agentInfo": t.proxy(renames["AgentInfoIn"]).optional(),
            "metadata": t.proxy(renames["AgentMetadataIn"]).optional(),
        }
    ).named(renames["ReportAgentStateRequestIn"])
    types["ReportAgentStateRequestOut"] = t.struct(
        {
            "agentTimingInfo": t.proxy(renames["AgentTimingInfoOut"]).optional(),
            "agentInfo": t.proxy(renames["AgentInfoOut"]).optional(),
            "metadata": t.proxy(renames["AgentMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportAgentStateRequestOut"])

    functions = {}
    functions["projectsLocationsList"] = batch.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = batch.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsList"] = batch.delete(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "reason": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsGet"] = batch.delete(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "reason": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsCreate"] = batch.delete(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "reason": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsDelete"] = batch.delete(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "reason": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsTaskGroupsTasksGet"] = batch.get(
        "v1/{parent}/tasks",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTasksResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsTaskGroupsTasksList"] = batch.get(
        "v1/{parent}/tasks",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTasksResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = batch.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = batch.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = batch.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = batch.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStateReport"] = batch.post(
        "v1/{parent}/state:report",
        t.struct(
            {
                "parent": t.string(),
                "agentTimingInfo": t.proxy(renames["AgentTimingInfoIn"]).optional(),
                "agentInfo": t.proxy(renames["AgentInfoIn"]).optional(),
                "metadata": t.proxy(renames["AgentMetadataIn"]).optional(),
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
