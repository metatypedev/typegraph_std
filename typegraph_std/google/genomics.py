from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_genomics() -> Import:
    genomics = HTTPRuntime("https://genomics.googleapis.com/")

    renames = {
        "ErrorResponse": "_genomics_1_ErrorResponse",
        "PullStoppedEventIn": "_genomics_2_PullStoppedEventIn",
        "PullStoppedEventOut": "_genomics_3_PullStoppedEventOut",
        "RunPipelineResponseIn": "_genomics_4_RunPipelineResponseIn",
        "RunPipelineResponseOut": "_genomics_5_RunPipelineResponseOut",
        "RunPipelineRequestIn": "_genomics_6_RunPipelineRequestIn",
        "RunPipelineRequestOut": "_genomics_7_RunPipelineRequestOut",
        "PersistentDiskIn": "_genomics_8_PersistentDiskIn",
        "PersistentDiskOut": "_genomics_9_PersistentDiskOut",
        "PullStartedEventIn": "_genomics_10_PullStartedEventIn",
        "PullStartedEventOut": "_genomics_11_PullStartedEventOut",
        "WorkerAssignedEventIn": "_genomics_12_WorkerAssignedEventIn",
        "WorkerAssignedEventOut": "_genomics_13_WorkerAssignedEventOut",
        "EventIn": "_genomics_14_EventIn",
        "EventOut": "_genomics_15_EventOut",
        "SecretIn": "_genomics_16_SecretIn",
        "SecretOut": "_genomics_17_SecretOut",
        "ActionIn": "_genomics_18_ActionIn",
        "ActionOut": "_genomics_19_ActionOut",
        "DelayedEventIn": "_genomics_20_DelayedEventIn",
        "DelayedEventOut": "_genomics_21_DelayedEventOut",
        "CheckInResponseIn": "_genomics_22_CheckInResponseIn",
        "CheckInResponseOut": "_genomics_23_CheckInResponseOut",
        "CheckInRequestIn": "_genomics_24_CheckInRequestIn",
        "CheckInRequestOut": "_genomics_25_CheckInRequestOut",
        "ResourcesIn": "_genomics_26_ResourcesIn",
        "ResourcesOut": "_genomics_27_ResourcesOut",
        "ContainerKilledEventIn": "_genomics_28_ContainerKilledEventIn",
        "ContainerKilledEventOut": "_genomics_29_ContainerKilledEventOut",
        "EmptyIn": "_genomics_30_EmptyIn",
        "EmptyOut": "_genomics_31_EmptyOut",
        "DiskStatusIn": "_genomics_32_DiskStatusIn",
        "DiskStatusOut": "_genomics_33_DiskStatusOut",
        "WorkerReleasedEventIn": "_genomics_34_WorkerReleasedEventIn",
        "WorkerReleasedEventOut": "_genomics_35_WorkerReleasedEventOut",
        "ExistingDiskIn": "_genomics_36_ExistingDiskIn",
        "ExistingDiskOut": "_genomics_37_ExistingDiskOut",
        "NetworkIn": "_genomics_38_NetworkIn",
        "NetworkOut": "_genomics_39_NetworkOut",
        "CancelOperationRequestIn": "_genomics_40_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_genomics_41_CancelOperationRequestOut",
        "DiskIn": "_genomics_42_DiskIn",
        "DiskOut": "_genomics_43_DiskOut",
        "NFSMountIn": "_genomics_44_NFSMountIn",
        "NFSMountOut": "_genomics_45_NFSMountOut",
        "VolumeIn": "_genomics_46_VolumeIn",
        "VolumeOut": "_genomics_47_VolumeOut",
        "WorkerStatusIn": "_genomics_48_WorkerStatusIn",
        "WorkerStatusOut": "_genomics_49_WorkerStatusOut",
        "FailedEventIn": "_genomics_50_FailedEventIn",
        "FailedEventOut": "_genomics_51_FailedEventOut",
        "VirtualMachineIn": "_genomics_52_VirtualMachineIn",
        "VirtualMachineOut": "_genomics_53_VirtualMachineOut",
        "OperationIn": "_genomics_54_OperationIn",
        "OperationOut": "_genomics_55_OperationOut",
        "ContainerStartedEventIn": "_genomics_56_ContainerStartedEventIn",
        "ContainerStartedEventOut": "_genomics_57_ContainerStartedEventOut",
        "ServiceAccountIn": "_genomics_58_ServiceAccountIn",
        "ServiceAccountOut": "_genomics_59_ServiceAccountOut",
        "ContainerStoppedEventIn": "_genomics_60_ContainerStoppedEventIn",
        "ContainerStoppedEventOut": "_genomics_61_ContainerStoppedEventOut",
        "TimestampedEventIn": "_genomics_62_TimestampedEventIn",
        "TimestampedEventOut": "_genomics_63_TimestampedEventOut",
        "AcceleratorIn": "_genomics_64_AcceleratorIn",
        "AcceleratorOut": "_genomics_65_AcceleratorOut",
        "MountIn": "_genomics_66_MountIn",
        "MountOut": "_genomics_67_MountOut",
        "UnexpectedExitStatusEventIn": "_genomics_68_UnexpectedExitStatusEventIn",
        "UnexpectedExitStatusEventOut": "_genomics_69_UnexpectedExitStatusEventOut",
        "StatusIn": "_genomics_70_StatusIn",
        "StatusOut": "_genomics_71_StatusOut",
        "PipelineIn": "_genomics_72_PipelineIn",
        "PipelineOut": "_genomics_73_PipelineOut",
        "ListOperationsResponseIn": "_genomics_74_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_genomics_75_ListOperationsResponseOut",
        "MetadataIn": "_genomics_76_MetadataIn",
        "MetadataOut": "_genomics_77_MetadataOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["PullStoppedEventIn"] = t.struct({"imageUri": t.string().optional()}).named(
        renames["PullStoppedEventIn"]
    )
    types["PullStoppedEventOut"] = t.struct(
        {
            "imageUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PullStoppedEventOut"])
    types["RunPipelineResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RunPipelineResponseIn"]
    )
    types["RunPipelineResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RunPipelineResponseOut"])
    types["RunPipelineRequestIn"] = t.struct(
        {
            "pipeline": t.proxy(renames["PipelineIn"]),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "pubSubTopic": t.string().optional(),
        }
    ).named(renames["RunPipelineRequestIn"])
    types["RunPipelineRequestOut"] = t.struct(
        {
            "pipeline": t.proxy(renames["PipelineOut"]),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "pubSubTopic": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunPipelineRequestOut"])
    types["PersistentDiskIn"] = t.struct(
        {
            "type": t.string().optional(),
            "sizeGb": t.integer().optional(),
            "sourceImage": t.string().optional(),
        }
    ).named(renames["PersistentDiskIn"])
    types["PersistentDiskOut"] = t.struct(
        {
            "type": t.string().optional(),
            "sizeGb": t.integer().optional(),
            "sourceImage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PersistentDiskOut"])
    types["PullStartedEventIn"] = t.struct({"imageUri": t.string().optional()}).named(
        renames["PullStartedEventIn"]
    )
    types["PullStartedEventOut"] = t.struct(
        {
            "imageUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PullStartedEventOut"])
    types["WorkerAssignedEventIn"] = t.struct(
        {
            "instance": t.string().optional(),
            "zone": t.string().optional(),
            "machineType": t.string().optional(),
        }
    ).named(renames["WorkerAssignedEventIn"])
    types["WorkerAssignedEventOut"] = t.struct(
        {
            "instance": t.string().optional(),
            "zone": t.string().optional(),
            "machineType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkerAssignedEventOut"])
    types["EventIn"] = t.struct(
        {
            "description": t.string().optional(),
            "details": t.struct({"_": t.string().optional()}).optional(),
            "timestamp": t.string().optional(),
        }
    ).named(renames["EventIn"])
    types["EventOut"] = t.struct(
        {
            "description": t.string().optional(),
            "details": t.struct({"_": t.string().optional()}).optional(),
            "timestamp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventOut"])
    types["SecretIn"] = t.struct(
        {"cipherText": t.string().optional(), "keyName": t.string().optional()}
    ).named(renames["SecretIn"])
    types["SecretOut"] = t.struct(
        {
            "cipherText": t.string().optional(),
            "keyName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecretOut"])
    types["ActionIn"] = t.struct(
        {
            "entrypoint": t.string().optional(),
            "imageUri": t.string(),
            "credentials": t.proxy(renames["SecretIn"]).optional(),
            "timeout": t.string().optional(),
            "pidNamespace": t.string().optional(),
            "mounts": t.array(t.proxy(renames["MountIn"])).optional(),
            "portMappings": t.struct({"_": t.string().optional()}).optional(),
            "environment": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "encryptedEnvironment": t.proxy(renames["SecretIn"]).optional(),
            "name": t.string().optional(),
            "flags": t.array(t.string()).optional(),
            "commands": t.array(t.string()).optional(),
        }
    ).named(renames["ActionIn"])
    types["ActionOut"] = t.struct(
        {
            "entrypoint": t.string().optional(),
            "imageUri": t.string(),
            "credentials": t.proxy(renames["SecretOut"]).optional(),
            "timeout": t.string().optional(),
            "pidNamespace": t.string().optional(),
            "mounts": t.array(t.proxy(renames["MountOut"])).optional(),
            "portMappings": t.struct({"_": t.string().optional()}).optional(),
            "environment": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "encryptedEnvironment": t.proxy(renames["SecretOut"]).optional(),
            "name": t.string().optional(),
            "flags": t.array(t.string()).optional(),
            "commands": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActionOut"])
    types["DelayedEventIn"] = t.struct(
        {"metrics": t.array(t.string()).optional(), "cause": t.string().optional()}
    ).named(renames["DelayedEventIn"])
    types["DelayedEventOut"] = t.struct(
        {
            "metrics": t.array(t.string()).optional(),
            "cause": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DelayedEventOut"])
    types["CheckInResponseIn"] = t.struct(
        {
            "features": t.struct({"_": t.string().optional()}).optional(),
            "deadline": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["CheckInResponseIn"])
    types["CheckInResponseOut"] = t.struct(
        {
            "features": t.struct({"_": t.string().optional()}).optional(),
            "deadline": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CheckInResponseOut"])
    types["CheckInRequestIn"] = t.struct(
        {
            "sosReport": t.string().optional(),
            "workerStatus": t.proxy(renames["WorkerStatusIn"]).optional(),
            "events": t.array(t.proxy(renames["TimestampedEventIn"])).optional(),
            "result": t.proxy(renames["StatusIn"]).optional(),
            "event": t.struct({"_": t.string().optional()}).optional(),
            "deadlineExpired": t.proxy(renames["EmptyIn"]).optional(),
        }
    ).named(renames["CheckInRequestIn"])
    types["CheckInRequestOut"] = t.struct(
        {
            "sosReport": t.string().optional(),
            "workerStatus": t.proxy(renames["WorkerStatusOut"]).optional(),
            "events": t.array(t.proxy(renames["TimestampedEventOut"])).optional(),
            "result": t.proxy(renames["StatusOut"]).optional(),
            "event": t.struct({"_": t.string().optional()}).optional(),
            "deadlineExpired": t.proxy(renames["EmptyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CheckInRequestOut"])
    types["ResourcesIn"] = t.struct(
        {
            "virtualMachine": t.proxy(renames["VirtualMachineIn"]).optional(),
            "regions": t.array(t.string()).optional(),
            "projectId": t.string().optional(),
            "zones": t.array(t.string()).optional(),
        }
    ).named(renames["ResourcesIn"])
    types["ResourcesOut"] = t.struct(
        {
            "virtualMachine": t.proxy(renames["VirtualMachineOut"]).optional(),
            "regions": t.array(t.string()).optional(),
            "projectId": t.string().optional(),
            "zones": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourcesOut"])
    types["ContainerKilledEventIn"] = t.struct(
        {"actionId": t.integer().optional()}
    ).named(renames["ContainerKilledEventIn"])
    types["ContainerKilledEventOut"] = t.struct(
        {
            "actionId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContainerKilledEventOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["DiskStatusIn"] = t.struct(
        {
            "freeSpaceBytes": t.string().optional(),
            "totalSpaceBytes": t.string().optional(),
        }
    ).named(renames["DiskStatusIn"])
    types["DiskStatusOut"] = t.struct(
        {
            "freeSpaceBytes": t.string().optional(),
            "totalSpaceBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiskStatusOut"])
    types["WorkerReleasedEventIn"] = t.struct(
        {"instance": t.string().optional(), "zone": t.string().optional()}
    ).named(renames["WorkerReleasedEventIn"])
    types["WorkerReleasedEventOut"] = t.struct(
        {
            "instance": t.string().optional(),
            "zone": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkerReleasedEventOut"])
    types["ExistingDiskIn"] = t.struct({"disk": t.string().optional()}).named(
        renames["ExistingDiskIn"]
    )
    types["ExistingDiskOut"] = t.struct(
        {
            "disk": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExistingDiskOut"])
    types["NetworkIn"] = t.struct(
        {
            "name": t.string().optional(),
            "subnetwork": t.string().optional(),
            "usePrivateAddress": t.boolean().optional(),
        }
    ).named(renames["NetworkIn"])
    types["NetworkOut"] = t.struct(
        {
            "name": t.string().optional(),
            "subnetwork": t.string().optional(),
            "usePrivateAddress": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["DiskIn"] = t.struct(
        {
            "sourceImage": t.string().optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
            "sizeGb": t.integer().optional(),
        }
    ).named(renames["DiskIn"])
    types["DiskOut"] = t.struct(
        {
            "sourceImage": t.string().optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
            "sizeGb": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiskOut"])
    types["NFSMountIn"] = t.struct({"target": t.string().optional()}).named(
        renames["NFSMountIn"]
    )
    types["NFSMountOut"] = t.struct(
        {
            "target": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NFSMountOut"])
    types["VolumeIn"] = t.struct(
        {
            "volume": t.string().optional(),
            "existingDisk": t.proxy(renames["ExistingDiskIn"]).optional(),
            "persistentDisk": t.proxy(renames["PersistentDiskIn"]).optional(),
            "nfsMount": t.proxy(renames["NFSMountIn"]).optional(),
        }
    ).named(renames["VolumeIn"])
    types["VolumeOut"] = t.struct(
        {
            "volume": t.string().optional(),
            "existingDisk": t.proxy(renames["ExistingDiskOut"]).optional(),
            "persistentDisk": t.proxy(renames["PersistentDiskOut"]).optional(),
            "nfsMount": t.proxy(renames["NFSMountOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VolumeOut"])
    types["WorkerStatusIn"] = t.struct(
        {
            "freeRamBytes": t.string().optional(),
            "totalRamBytes": t.string().optional(),
            "uptimeSeconds": t.string().optional(),
            "attachedDisks": t.struct({"_": t.string().optional()}).optional(),
            "bootDisk": t.proxy(renames["DiskStatusIn"]).optional(),
        }
    ).named(renames["WorkerStatusIn"])
    types["WorkerStatusOut"] = t.struct(
        {
            "freeRamBytes": t.string().optional(),
            "totalRamBytes": t.string().optional(),
            "uptimeSeconds": t.string().optional(),
            "attachedDisks": t.struct({"_": t.string().optional()}).optional(),
            "bootDisk": t.proxy(renames["DiskStatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkerStatusOut"])
    types["FailedEventIn"] = t.struct(
        {"cause": t.string().optional(), "code": t.string().optional()}
    ).named(renames["FailedEventIn"])
    types["FailedEventOut"] = t.struct(
        {
            "cause": t.string().optional(),
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FailedEventOut"])
    types["VirtualMachineIn"] = t.struct(
        {
            "cpuPlatform": t.string().optional(),
            "dockerCacheImages": t.array(t.string()).optional(),
            "disks": t.array(t.proxy(renames["DiskIn"])).optional(),
            "network": t.proxy(renames["NetworkIn"]).optional(),
            "accelerators": t.array(t.proxy(renames["AcceleratorIn"])).optional(),
            "preemptible": t.boolean().optional(),
            "nvidiaDriverVersion": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "reservation": t.string().optional(),
            "serviceAccount": t.proxy(renames["ServiceAccountIn"]).optional(),
            "enableStackdriverMonitoring": t.boolean().optional(),
            "bootDiskSizeGb": t.integer().optional(),
            "volumes": t.array(t.proxy(renames["VolumeIn"])).optional(),
            "machineType": t.string(),
            "bootImage": t.string().optional(),
        }
    ).named(renames["VirtualMachineIn"])
    types["VirtualMachineOut"] = t.struct(
        {
            "cpuPlatform": t.string().optional(),
            "dockerCacheImages": t.array(t.string()).optional(),
            "disks": t.array(t.proxy(renames["DiskOut"])).optional(),
            "network": t.proxy(renames["NetworkOut"]).optional(),
            "accelerators": t.array(t.proxy(renames["AcceleratorOut"])).optional(),
            "preemptible": t.boolean().optional(),
            "nvidiaDriverVersion": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "reservation": t.string().optional(),
            "serviceAccount": t.proxy(renames["ServiceAccountOut"]).optional(),
            "enableStackdriverMonitoring": t.boolean().optional(),
            "bootDiskSizeGb": t.integer().optional(),
            "volumes": t.array(t.proxy(renames["VolumeOut"])).optional(),
            "machineType": t.string(),
            "bootImage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VirtualMachineOut"])
    types["OperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
    types["ContainerStartedEventIn"] = t.struct(
        {
            "actionId": t.integer().optional(),
            "ipAddress": t.string().optional(),
            "portMappings": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ContainerStartedEventIn"])
    types["ContainerStartedEventOut"] = t.struct(
        {
            "actionId": t.integer().optional(),
            "ipAddress": t.string().optional(),
            "portMappings": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContainerStartedEventOut"])
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
    types["ContainerStoppedEventIn"] = t.struct(
        {
            "stderr": t.string().optional(),
            "actionId": t.integer().optional(),
            "exitStatus": t.integer().optional(),
        }
    ).named(renames["ContainerStoppedEventIn"])
    types["ContainerStoppedEventOut"] = t.struct(
        {
            "stderr": t.string().optional(),
            "actionId": t.integer().optional(),
            "exitStatus": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContainerStoppedEventOut"])
    types["TimestampedEventIn"] = t.struct(
        {
            "timestamp": t.string().optional(),
            "data": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["TimestampedEventIn"])
    types["TimestampedEventOut"] = t.struct(
        {
            "timestamp": t.string().optional(),
            "data": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimestampedEventOut"])
    types["AcceleratorIn"] = t.struct(
        {"count": t.string().optional(), "type": t.string().optional()}
    ).named(renames["AcceleratorIn"])
    types["AcceleratorOut"] = t.struct(
        {
            "count": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AcceleratorOut"])
    types["MountIn"] = t.struct(
        {
            "readOnly": t.boolean().optional(),
            "path": t.string().optional(),
            "disk": t.string().optional(),
        }
    ).named(renames["MountIn"])
    types["MountOut"] = t.struct(
        {
            "readOnly": t.boolean().optional(),
            "path": t.string().optional(),
            "disk": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MountOut"])
    types["UnexpectedExitStatusEventIn"] = t.struct(
        {"actionId": t.integer().optional(), "exitStatus": t.integer().optional()}
    ).named(renames["UnexpectedExitStatusEventIn"])
    types["UnexpectedExitStatusEventOut"] = t.struct(
        {
            "actionId": t.integer().optional(),
            "exitStatus": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UnexpectedExitStatusEventOut"])
    types["StatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["PipelineIn"] = t.struct(
        {
            "actions": t.array(t.proxy(renames["ActionIn"])).optional(),
            "resources": t.proxy(renames["ResourcesIn"]).optional(),
            "encryptedEnvironment": t.proxy(renames["SecretIn"]).optional(),
            "timeout": t.string().optional(),
            "environment": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["PipelineIn"])
    types["PipelineOut"] = t.struct(
        {
            "actions": t.array(t.proxy(renames["ActionOut"])).optional(),
            "resources": t.proxy(renames["ResourcesOut"]).optional(),
            "encryptedEnvironment": t.proxy(renames["SecretOut"]).optional(),
            "timeout": t.string().optional(),
            "environment": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PipelineOut"])
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
    types["MetadataIn"] = t.struct(
        {
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "events": t.array(t.proxy(renames["EventIn"])).optional(),
            "pipeline": t.proxy(renames["PipelineIn"]).optional(),
            "createTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["MetadataIn"])
    types["MetadataOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "events": t.array(t.proxy(renames["EventOut"])).optional(),
            "pipeline": t.proxy(renames["PipelineOut"]).optional(),
            "createTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetadataOut"])

    functions = {}
    functions["workersCheckIn"] = genomics.post(
        "v2alpha1/workers/{id}:checkIn",
        t.struct(
            {
                "id": t.string().optional(),
                "sosReport": t.string().optional(),
                "workerStatus": t.proxy(renames["WorkerStatusIn"]).optional(),
                "events": t.array(t.proxy(renames["TimestampedEventIn"])).optional(),
                "result": t.proxy(renames["StatusIn"]).optional(),
                "event": t.struct({"_": t.string().optional()}).optional(),
                "deadlineExpired": t.proxy(renames["EmptyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CheckInResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["pipelinesRun"] = genomics.post(
        "v2alpha1/pipelines:run",
        t.struct(
            {
                "pipeline": t.proxy(renames["PipelineIn"]),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "pubSubTopic": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsWorkersCheckIn"] = genomics.post(
        "v2alpha1/{id}:checkIn",
        t.struct(
            {
                "id": t.string().optional(),
                "sosReport": t.string().optional(),
                "workerStatus": t.proxy(renames["WorkerStatusIn"]).optional(),
                "events": t.array(t.proxy(renames["TimestampedEventIn"])).optional(),
                "result": t.proxy(renames["StatusIn"]).optional(),
                "event": t.struct({"_": t.string().optional()}).optional(),
                "deadlineExpired": t.proxy(renames["EmptyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CheckInResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOperationsGet"] = genomics.get(
        "v2alpha1/{name}",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOperationsCancel"] = genomics.get(
        "v2alpha1/{name}",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOperationsList"] = genomics.get(
        "v2alpha1/{name}",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="genomics", renames=renames, types=Box(types), functions=Box(functions)
    )
