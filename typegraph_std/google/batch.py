from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_batch() -> Import:
    batch = HTTPRuntime("https://batch.googleapis.com/")

    renames = {
        "ErrorResponse": "_batch_1_ErrorResponse",
        "TaskSpecIn": "_batch_2_TaskSpecIn",
        "TaskSpecOut": "_batch_3_TaskSpecOut",
        "AgentTimingInfoIn": "_batch_4_AgentTimingInfoIn",
        "AgentTimingInfoOut": "_batch_5_AgentTimingInfoOut",
        "AgentMetadataIn": "_batch_6_AgentMetadataIn",
        "AgentMetadataOut": "_batch_7_AgentMetadataOut",
        "AgentInfoIn": "_batch_8_AgentInfoIn",
        "AgentInfoOut": "_batch_9_AgentInfoOut",
        "TaskExecutionIn": "_batch_10_TaskExecutionIn",
        "TaskExecutionOut": "_batch_11_TaskExecutionOut",
        "InstanceStatusIn": "_batch_12_InstanceStatusIn",
        "InstanceStatusOut": "_batch_13_InstanceStatusOut",
        "OperationIn": "_batch_14_OperationIn",
        "OperationOut": "_batch_15_OperationOut",
        "LocationIn": "_batch_16_LocationIn",
        "LocationOut": "_batch_17_LocationOut",
        "StatusIn": "_batch_18_StatusIn",
        "StatusOut": "_batch_19_StatusOut",
        "LifecyclePolicyIn": "_batch_20_LifecyclePolicyIn",
        "LifecyclePolicyOut": "_batch_21_LifecyclePolicyOut",
        "LogsPolicyIn": "_batch_22_LogsPolicyIn",
        "LogsPolicyOut": "_batch_23_LogsPolicyOut",
        "AttachedDiskIn": "_batch_24_AttachedDiskIn",
        "AttachedDiskOut": "_batch_25_AttachedDiskOut",
        "TaskStatusIn": "_batch_26_TaskStatusIn",
        "TaskStatusOut": "_batch_27_TaskStatusOut",
        "TaskIn": "_batch_28_TaskIn",
        "TaskOut": "_batch_29_TaskOut",
        "InstancePolicyOrTemplateIn": "_batch_30_InstancePolicyOrTemplateIn",
        "InstancePolicyOrTemplateOut": "_batch_31_InstancePolicyOrTemplateOut",
        "OperationMetadataIn": "_batch_32_OperationMetadataIn",
        "OperationMetadataOut": "_batch_33_OperationMetadataOut",
        "EmptyIn": "_batch_34_EmptyIn",
        "EmptyOut": "_batch_35_EmptyOut",
        "AgentTaskIn": "_batch_36_AgentTaskIn",
        "AgentTaskOut": "_batch_37_AgentTaskOut",
        "ListOperationsResponseIn": "_batch_38_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_batch_39_ListOperationsResponseOut",
        "ListTasksResponseIn": "_batch_40_ListTasksResponseIn",
        "ListTasksResponseOut": "_batch_41_ListTasksResponseOut",
        "TaskGroupStatusIn": "_batch_42_TaskGroupStatusIn",
        "TaskGroupStatusOut": "_batch_43_TaskGroupStatusOut",
        "RunnableIn": "_batch_44_RunnableIn",
        "RunnableOut": "_batch_45_RunnableOut",
        "NetworkPolicyIn": "_batch_46_NetworkPolicyIn",
        "NetworkPolicyOut": "_batch_47_NetworkPolicyOut",
        "ScriptIn": "_batch_48_ScriptIn",
        "ScriptOut": "_batch_49_ScriptOut",
        "NetworkInterfaceIn": "_batch_50_NetworkInterfaceIn",
        "NetworkInterfaceOut": "_batch_51_NetworkInterfaceOut",
        "BarrierIn": "_batch_52_BarrierIn",
        "BarrierOut": "_batch_53_BarrierOut",
        "JobIn": "_batch_54_JobIn",
        "JobOut": "_batch_55_JobOut",
        "ServiceAccountIn": "_batch_56_ServiceAccountIn",
        "ServiceAccountOut": "_batch_57_ServiceAccountOut",
        "PlacementPolicyIn": "_batch_58_PlacementPolicyIn",
        "PlacementPolicyOut": "_batch_59_PlacementPolicyOut",
        "ListLocationsResponseIn": "_batch_60_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_batch_61_ListLocationsResponseOut",
        "ContainerIn": "_batch_62_ContainerIn",
        "ContainerOut": "_batch_63_ContainerOut",
        "VolumeIn": "_batch_64_VolumeIn",
        "VolumeOut": "_batch_65_VolumeOut",
        "ListJobsResponseIn": "_batch_66_ListJobsResponseIn",
        "ListJobsResponseOut": "_batch_67_ListJobsResponseOut",
        "EnvironmentIn": "_batch_68_EnvironmentIn",
        "EnvironmentOut": "_batch_69_EnvironmentOut",
        "JobNotificationIn": "_batch_70_JobNotificationIn",
        "JobNotificationOut": "_batch_71_JobNotificationOut",
        "AgentTaskInfoIn": "_batch_72_AgentTaskInfoIn",
        "AgentTaskInfoOut": "_batch_73_AgentTaskInfoOut",
        "MessageIn": "_batch_74_MessageIn",
        "MessageOut": "_batch_75_MessageOut",
        "DiskIn": "_batch_76_DiskIn",
        "DiskOut": "_batch_77_DiskOut",
        "NFSIn": "_batch_78_NFSIn",
        "NFSOut": "_batch_79_NFSOut",
        "TaskGroupIn": "_batch_80_TaskGroupIn",
        "TaskGroupOut": "_batch_81_TaskGroupOut",
        "AllocationPolicyIn": "_batch_82_AllocationPolicyIn",
        "AllocationPolicyOut": "_batch_83_AllocationPolicyOut",
        "ComputeResourceIn": "_batch_84_ComputeResourceIn",
        "ComputeResourceOut": "_batch_85_ComputeResourceOut",
        "GCSIn": "_batch_86_GCSIn",
        "GCSOut": "_batch_87_GCSOut",
        "KMSEnvMapIn": "_batch_88_KMSEnvMapIn",
        "KMSEnvMapOut": "_batch_89_KMSEnvMapOut",
        "ReportAgentStateRequestIn": "_batch_90_ReportAgentStateRequestIn",
        "ReportAgentStateRequestOut": "_batch_91_ReportAgentStateRequestOut",
        "InstancePolicyIn": "_batch_92_InstancePolicyIn",
        "InstancePolicyOut": "_batch_93_InstancePolicyOut",
        "JobStatusIn": "_batch_94_JobStatusIn",
        "JobStatusOut": "_batch_95_JobStatusOut",
        "ActionConditionIn": "_batch_96_ActionConditionIn",
        "ActionConditionOut": "_batch_97_ActionConditionOut",
        "AcceleratorIn": "_batch_98_AcceleratorIn",
        "AcceleratorOut": "_batch_99_AcceleratorOut",
        "CancelOperationRequestIn": "_batch_100_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_batch_101_CancelOperationRequestOut",
        "LocationPolicyIn": "_batch_102_LocationPolicyIn",
        "LocationPolicyOut": "_batch_103_LocationPolicyOut",
        "StatusEventIn": "_batch_104_StatusEventIn",
        "StatusEventOut": "_batch_105_StatusEventOut",
        "ReportAgentStateResponseIn": "_batch_106_ReportAgentStateResponseIn",
        "ReportAgentStateResponseOut": "_batch_107_ReportAgentStateResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["TaskSpecIn"] = t.struct(
        {
            "maxRunDuration": t.string().optional(),
            "environment": t.proxy(renames["EnvironmentIn"]).optional(),
            "environments": t.struct({"_": t.string().optional()}).optional(),
            "runnables": t.array(t.proxy(renames["RunnableIn"])).optional(),
            "volumes": t.array(t.proxy(renames["VolumeIn"])).optional(),
            "maxRetryCount": t.integer().optional(),
            "lifecyclePolicies": t.array(
                t.proxy(renames["LifecyclePolicyIn"])
            ).optional(),
            "computeResource": t.proxy(renames["ComputeResourceIn"]).optional(),
        }
    ).named(renames["TaskSpecIn"])
    types["TaskSpecOut"] = t.struct(
        {
            "maxRunDuration": t.string().optional(),
            "environment": t.proxy(renames["EnvironmentOut"]).optional(),
            "environments": t.struct({"_": t.string().optional()}).optional(),
            "runnables": t.array(t.proxy(renames["RunnableOut"])).optional(),
            "volumes": t.array(t.proxy(renames["VolumeOut"])).optional(),
            "maxRetryCount": t.integer().optional(),
            "lifecyclePolicies": t.array(
                t.proxy(renames["LifecyclePolicyOut"])
            ).optional(),
            "computeResource": t.proxy(renames["ComputeResourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TaskSpecOut"])
    types["AgentTimingInfoIn"] = t.struct(
        {
            "agentStartupTime": t.string().optional(),
            "bootTime": t.string().optional(),
            "scriptStartupTime": t.string().optional(),
        }
    ).named(renames["AgentTimingInfoIn"])
    types["AgentTimingInfoOut"] = t.struct(
        {
            "agentStartupTime": t.string().optional(),
            "bootTime": t.string().optional(),
            "scriptStartupTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AgentTimingInfoOut"])
    types["AgentMetadataIn"] = t.struct(
        {
            "zone": t.string().optional(),
            "osRelease": t.struct({"_": t.string().optional()}).optional(),
            "instancePreemptionNoticeReceived": t.boolean().optional(),
            "instance": t.string().optional(),
            "creationTime": t.string().optional(),
            "creator": t.string().optional(),
            "version": t.string().optional(),
            "imageVersion": t.string().optional(),
            "instanceId": t.string().optional(),
        }
    ).named(renames["AgentMetadataIn"])
    types["AgentMetadataOut"] = t.struct(
        {
            "zone": t.string().optional(),
            "osRelease": t.struct({"_": t.string().optional()}).optional(),
            "instancePreemptionNoticeReceived": t.boolean().optional(),
            "instance": t.string().optional(),
            "creationTime": t.string().optional(),
            "creator": t.string().optional(),
            "version": t.string().optional(),
            "imageVersion": t.string().optional(),
            "instanceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AgentMetadataOut"])
    types["AgentInfoIn"] = t.struct(
        {
            "jobId": t.string().optional(),
            "state": t.string().optional(),
            "taskGroupId": t.string().optional(),
            "reportTime": t.string().optional(),
            "tasks": t.array(t.proxy(renames["AgentTaskInfoIn"])).optional(),
        }
    ).named(renames["AgentInfoIn"])
    types["AgentInfoOut"] = t.struct(
        {
            "jobId": t.string().optional(),
            "state": t.string().optional(),
            "taskGroupId": t.string().optional(),
            "reportTime": t.string().optional(),
            "tasks": t.array(t.proxy(renames["AgentTaskInfoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AgentInfoOut"])
    types["TaskExecutionIn"] = t.struct({"exitCode": t.integer().optional()}).named(
        renames["TaskExecutionIn"]
    )
    types["TaskExecutionOut"] = t.struct(
        {
            "exitCode": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TaskExecutionOut"])
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
    types["OperationIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["LocationIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
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
    types["InstancePolicyOrTemplateIn"] = t.struct(
        {
            "policy": t.proxy(renames["InstancePolicyIn"]).optional(),
            "installGpuDrivers": t.boolean().optional(),
            "instanceTemplate": t.string().optional(),
        }
    ).named(renames["InstancePolicyOrTemplateIn"])
    types["InstancePolicyOrTemplateOut"] = t.struct(
        {
            "policy": t.proxy(renames["InstancePolicyOut"]).optional(),
            "installGpuDrivers": t.boolean().optional(),
            "instanceTemplate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstancePolicyOrTemplateOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "apiVersion": t.string().optional(),
            "statusMessage": t.string().optional(),
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
            "target": t.string().optional(),
            "verb": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["AgentTaskIn"] = t.struct(
        {
            "task": t.string().optional(),
            "taskSource": t.string().optional(),
            "status": t.proxy(renames["TaskStatusIn"]).optional(),
            "spec": t.proxy(renames["TaskSpecIn"]).optional(),
            "intendedState": t.string().optional(),
            "reachedBarrier": t.string().optional(),
        }
    ).named(renames["AgentTaskIn"])
    types["AgentTaskOut"] = t.struct(
        {
            "task": t.string().optional(),
            "taskSource": t.string().optional(),
            "status": t.proxy(renames["TaskStatusOut"]).optional(),
            "spec": t.proxy(renames["TaskSpecOut"]).optional(),
            "intendedState": t.string().optional(),
            "reachedBarrier": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AgentTaskOut"])
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
    types["ListTasksResponseIn"] = t.struct(
        {
            "tasks": t.array(t.proxy(renames["TaskIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListTasksResponseIn"])
    types["ListTasksResponseOut"] = t.struct(
        {
            "tasks": t.array(t.proxy(renames["TaskOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTasksResponseOut"])
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
    types["RunnableIn"] = t.struct(
        {
            "container": t.proxy(renames["ContainerIn"]).optional(),
            "barrier": t.proxy(renames["BarrierIn"]).optional(),
            "alwaysRun": t.boolean().optional(),
            "environment": t.proxy(renames["EnvironmentIn"]).optional(),
            "script": t.proxy(renames["ScriptIn"]).optional(),
            "ignoreExitStatus": t.boolean().optional(),
            "background": t.boolean().optional(),
            "timeout": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["RunnableIn"])
    types["RunnableOut"] = t.struct(
        {
            "container": t.proxy(renames["ContainerOut"]).optional(),
            "barrier": t.proxy(renames["BarrierOut"]).optional(),
            "alwaysRun": t.boolean().optional(),
            "environment": t.proxy(renames["EnvironmentOut"]).optional(),
            "script": t.proxy(renames["ScriptOut"]).optional(),
            "ignoreExitStatus": t.boolean().optional(),
            "background": t.boolean().optional(),
            "timeout": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunnableOut"])
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
    types["ScriptIn"] = t.struct(
        {"text": t.string().optional(), "path": t.string().optional()}
    ).named(renames["ScriptIn"])
    types["ScriptOut"] = t.struct(
        {
            "text": t.string().optional(),
            "path": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScriptOut"])
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
    types["BarrierIn"] = t.struct({"name": t.string().optional()}).named(
        renames["BarrierIn"]
    )
    types["BarrierOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BarrierOut"])
    types["JobIn"] = t.struct(
        {
            "priority": t.string().optional(),
            "allocationPolicy": t.proxy(renames["AllocationPolicyIn"]).optional(),
            "logsPolicy": t.proxy(renames["LogsPolicyIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "notifications": t.array(t.proxy(renames["JobNotificationIn"])).optional(),
            "taskGroups": t.array(t.proxy(renames["TaskGroupIn"])),
        }
    ).named(renames["JobIn"])
    types["JobOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "priority": t.string().optional(),
            "status": t.proxy(renames["JobStatusOut"]).optional(),
            "allocationPolicy": t.proxy(renames["AllocationPolicyOut"]).optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "logsPolicy": t.proxy(renames["LogsPolicyOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "notifications": t.array(t.proxy(renames["JobNotificationOut"])).optional(),
            "taskGroups": t.array(t.proxy(renames["TaskGroupOut"])),
            "uid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobOut"])
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
    types["ContainerIn"] = t.struct(
        {
            "imageUri": t.string().optional(),
            "volumes": t.array(t.string()).optional(),
            "password": t.string().optional(),
            "username": t.string().optional(),
            "options": t.string().optional(),
            "blockExternalNetwork": t.boolean().optional(),
            "entrypoint": t.string().optional(),
            "commands": t.array(t.string()).optional(),
        }
    ).named(renames["ContainerIn"])
    types["ContainerOut"] = t.struct(
        {
            "imageUri": t.string().optional(),
            "volumes": t.array(t.string()).optional(),
            "password": t.string().optional(),
            "username": t.string().optional(),
            "options": t.string().optional(),
            "blockExternalNetwork": t.boolean().optional(),
            "entrypoint": t.string().optional(),
            "commands": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContainerOut"])
    types["VolumeIn"] = t.struct(
        {
            "deviceName": t.string().optional(),
            "gcs": t.proxy(renames["GCSIn"]).optional(),
            "mountPath": t.string().optional(),
            "mountOptions": t.array(t.string()).optional(),
            "nfs": t.proxy(renames["NFSIn"]).optional(),
        }
    ).named(renames["VolumeIn"])
    types["VolumeOut"] = t.struct(
        {
            "deviceName": t.string().optional(),
            "gcs": t.proxy(renames["GCSOut"]).optional(),
            "mountPath": t.string().optional(),
            "mountOptions": t.array(t.string()).optional(),
            "nfs": t.proxy(renames["NFSOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VolumeOut"])
    types["ListJobsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "jobs": t.array(t.proxy(renames["JobIn"])).optional(),
        }
    ).named(renames["ListJobsResponseIn"])
    types["ListJobsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "jobs": t.array(t.proxy(renames["JobOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListJobsResponseOut"])
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
    types["AgentTaskInfoIn"] = t.struct(
        {
            "runnable": t.string().optional(),
            "taskStatus": t.proxy(renames["TaskStatusIn"]).optional(),
            "taskId": t.string().optional(),
        }
    ).named(renames["AgentTaskInfoIn"])
    types["AgentTaskInfoOut"] = t.struct(
        {
            "runnable": t.string().optional(),
            "taskStatus": t.proxy(renames["TaskStatusOut"]).optional(),
            "taskId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AgentTaskInfoOut"])
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
    types["DiskIn"] = t.struct(
        {
            "diskInterface": t.string().optional(),
            "sizeGb": t.string().optional(),
            "snapshot": t.string().optional(),
            "image": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["DiskIn"])
    types["DiskOut"] = t.struct(
        {
            "diskInterface": t.string().optional(),
            "sizeGb": t.string().optional(),
            "snapshot": t.string().optional(),
            "image": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiskOut"])
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
    types["TaskGroupIn"] = t.struct(
        {
            "parallelism": t.string().optional(),
            "taskEnvironments": t.array(t.proxy(renames["EnvironmentIn"])).optional(),
            "taskSpec": t.proxy(renames["TaskSpecIn"]),
            "taskCount": t.string().optional(),
            "permissiveSsh": t.boolean().optional(),
            "taskCountPerNode": t.string().optional(),
            "requireHostsFile": t.boolean().optional(),
        }
    ).named(renames["TaskGroupIn"])
    types["TaskGroupOut"] = t.struct(
        {
            "name": t.string().optional(),
            "parallelism": t.string().optional(),
            "taskEnvironments": t.array(t.proxy(renames["EnvironmentOut"])).optional(),
            "taskSpec": t.proxy(renames["TaskSpecOut"]),
            "taskCount": t.string().optional(),
            "permissiveSsh": t.boolean().optional(),
            "taskCountPerNode": t.string().optional(),
            "requireHostsFile": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TaskGroupOut"])
    types["AllocationPolicyIn"] = t.struct(
        {
            "instances": t.array(
                t.proxy(renames["InstancePolicyOrTemplateIn"])
            ).optional(),
            "network": t.proxy(renames["NetworkPolicyIn"]).optional(),
            "placement": t.proxy(renames["PlacementPolicyIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "location": t.proxy(renames["LocationPolicyIn"]).optional(),
            "serviceAccount": t.proxy(renames["ServiceAccountIn"]).optional(),
        }
    ).named(renames["AllocationPolicyIn"])
    types["AllocationPolicyOut"] = t.struct(
        {
            "instances": t.array(
                t.proxy(renames["InstancePolicyOrTemplateOut"])
            ).optional(),
            "network": t.proxy(renames["NetworkPolicyOut"]).optional(),
            "placement": t.proxy(renames["PlacementPolicyOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "location": t.proxy(renames["LocationPolicyOut"]).optional(),
            "serviceAccount": t.proxy(renames["ServiceAccountOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AllocationPolicyOut"])
    types["ComputeResourceIn"] = t.struct(
        {
            "memoryMib": t.string().optional(),
            "cpuMilli": t.string().optional(),
            "bootDiskMib": t.string().optional(),
        }
    ).named(renames["ComputeResourceIn"])
    types["ComputeResourceOut"] = t.struct(
        {
            "memoryMib": t.string().optional(),
            "cpuMilli": t.string().optional(),
            "bootDiskMib": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComputeResourceOut"])
    types["GCSIn"] = t.struct({"remotePath": t.string().optional()}).named(
        renames["GCSIn"]
    )
    types["GCSOut"] = t.struct(
        {
            "remotePath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GCSOut"])
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
    types["InstancePolicyIn"] = t.struct(
        {
            "accelerators": t.array(t.proxy(renames["AcceleratorIn"])).optional(),
            "disks": t.array(t.proxy(renames["AttachedDiskIn"])).optional(),
            "bootDisk": t.proxy(renames["DiskIn"]).optional(),
            "provisioningModel": t.string().optional(),
            "machineType": t.string().optional(),
            "minCpuPlatform": t.string().optional(),
        }
    ).named(renames["InstancePolicyIn"])
    types["InstancePolicyOut"] = t.struct(
        {
            "accelerators": t.array(t.proxy(renames["AcceleratorOut"])).optional(),
            "disks": t.array(t.proxy(renames["AttachedDiskOut"])).optional(),
            "bootDisk": t.proxy(renames["DiskOut"]).optional(),
            "provisioningModel": t.string().optional(),
            "machineType": t.string().optional(),
            "minCpuPlatform": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstancePolicyOut"])
    types["JobStatusIn"] = t.struct(
        {
            "statusEvents": t.array(t.proxy(renames["StatusEventIn"])).optional(),
            "runDuration": t.string().optional(),
            "state": t.string().optional(),
            "taskGroups": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["JobStatusIn"])
    types["JobStatusOut"] = t.struct(
        {
            "statusEvents": t.array(t.proxy(renames["StatusEventOut"])).optional(),
            "runDuration": t.string().optional(),
            "state": t.string().optional(),
            "taskGroups": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobStatusOut"])
    types["ActionConditionIn"] = t.struct(
        {"exitCodes": t.array(t.integer()).optional()}
    ).named(renames["ActionConditionIn"])
    types["ActionConditionOut"] = t.struct(
        {
            "exitCodes": t.array(t.integer()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActionConditionOut"])
    types["AcceleratorIn"] = t.struct(
        {
            "count": t.string().optional(),
            "installGpuDrivers": t.boolean().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["AcceleratorIn"])
    types["AcceleratorOut"] = t.struct(
        {
            "count": t.string().optional(),
            "installGpuDrivers": t.boolean().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AcceleratorOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["LocationPolicyIn"] = t.struct(
        {"allowedLocations": t.array(t.string()).optional()}
    ).named(renames["LocationPolicyIn"])
    types["LocationPolicyOut"] = t.struct(
        {
            "allowedLocations": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationPolicyOut"])
    types["StatusEventIn"] = t.struct(
        {
            "type": t.string().optional(),
            "taskExecution": t.proxy(renames["TaskExecutionIn"]).optional(),
            "taskState": t.string().optional(),
            "description": t.string().optional(),
            "eventTime": t.string().optional(),
        }
    ).named(renames["StatusEventIn"])
    types["StatusEventOut"] = t.struct(
        {
            "type": t.string().optional(),
            "taskExecution": t.proxy(renames["TaskExecutionOut"]).optional(),
            "taskState": t.string().optional(),
            "description": t.string().optional(),
            "eventTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusEventOut"])
    types["ReportAgentStateResponseIn"] = t.struct(
        {
            "defaultReportInterval": t.string().optional(),
            "minReportInterval": t.string().optional(),
            "tasks": t.array(t.proxy(renames["AgentTaskIn"])).optional(),
        }
    ).named(renames["ReportAgentStateResponseIn"])
    types["ReportAgentStateResponseOut"] = t.struct(
        {
            "defaultReportInterval": t.string().optional(),
            "minReportInterval": t.string().optional(),
            "tasks": t.array(t.proxy(renames["AgentTaskOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportAgentStateResponseOut"])

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
    functions["projectsLocationsJobsGet"] = batch.get(
        "v1/{parent}/jobs",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsDelete"] = batch.get(
        "v1/{parent}/jobs",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsCreate"] = batch.get(
        "v1/{parent}/jobs",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsList"] = batch.get(
        "v1/{parent}/jobs",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListJobsResponseOut"]),
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
    functions["projectsLocationsOperationsDelete"] = batch.get(
        "v1/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = batch.get(
        "v1/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(importer="batch", renames=renames, types=types, functions=functions)
