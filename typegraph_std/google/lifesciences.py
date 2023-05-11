from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_lifesciences() -> Import:
    lifesciences = HTTPRuntime("https://lifesciences.googleapis.com/")

    renames = {
        "ErrorResponse": "_lifesciences_1_ErrorResponse",
        "PullStoppedEventIn": "_lifesciences_2_PullStoppedEventIn",
        "PullStoppedEventOut": "_lifesciences_3_PullStoppedEventOut",
        "AcceleratorIn": "_lifesciences_4_AcceleratorIn",
        "AcceleratorOut": "_lifesciences_5_AcceleratorOut",
        "PullStartedEventIn": "_lifesciences_6_PullStartedEventIn",
        "PullStartedEventOut": "_lifesciences_7_PullStartedEventOut",
        "ActionIn": "_lifesciences_8_ActionIn",
        "ActionOut": "_lifesciences_9_ActionOut",
        "ContainerStartedEventIn": "_lifesciences_10_ContainerStartedEventIn",
        "ContainerStartedEventOut": "_lifesciences_11_ContainerStartedEventOut",
        "PipelineIn": "_lifesciences_12_PipelineIn",
        "PipelineOut": "_lifesciences_13_PipelineOut",
        "OperationIn": "_lifesciences_14_OperationIn",
        "OperationOut": "_lifesciences_15_OperationOut",
        "ContainerStoppedEventIn": "_lifesciences_16_ContainerStoppedEventIn",
        "ContainerStoppedEventOut": "_lifesciences_17_ContainerStoppedEventOut",
        "StatusIn": "_lifesciences_18_StatusIn",
        "StatusOut": "_lifesciences_19_StatusOut",
        "CancelOperationRequestIn": "_lifesciences_20_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_lifesciences_21_CancelOperationRequestOut",
        "WorkerReleasedEventIn": "_lifesciences_22_WorkerReleasedEventIn",
        "WorkerReleasedEventOut": "_lifesciences_23_WorkerReleasedEventOut",
        "DelayedEventIn": "_lifesciences_24_DelayedEventIn",
        "DelayedEventOut": "_lifesciences_25_DelayedEventOut",
        "RunPipelineResponseIn": "_lifesciences_26_RunPipelineResponseIn",
        "RunPipelineResponseOut": "_lifesciences_27_RunPipelineResponseOut",
        "SecretIn": "_lifesciences_28_SecretIn",
        "SecretOut": "_lifesciences_29_SecretOut",
        "RunPipelineRequestIn": "_lifesciences_30_RunPipelineRequestIn",
        "RunPipelineRequestOut": "_lifesciences_31_RunPipelineRequestOut",
        "PersistentDiskIn": "_lifesciences_32_PersistentDiskIn",
        "PersistentDiskOut": "_lifesciences_33_PersistentDiskOut",
        "ListOperationsResponseIn": "_lifesciences_34_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_lifesciences_35_ListOperationsResponseOut",
        "EmptyIn": "_lifesciences_36_EmptyIn",
        "EmptyOut": "_lifesciences_37_EmptyOut",
        "ServiceAccountIn": "_lifesciences_38_ServiceAccountIn",
        "ServiceAccountOut": "_lifesciences_39_ServiceAccountOut",
        "ResourcesIn": "_lifesciences_40_ResourcesIn",
        "ResourcesOut": "_lifesciences_41_ResourcesOut",
        "WorkerAssignedEventIn": "_lifesciences_42_WorkerAssignedEventIn",
        "WorkerAssignedEventOut": "_lifesciences_43_WorkerAssignedEventOut",
        "NetworkIn": "_lifesciences_44_NetworkIn",
        "NetworkOut": "_lifesciences_45_NetworkOut",
        "MetadataIn": "_lifesciences_46_MetadataIn",
        "MetadataOut": "_lifesciences_47_MetadataOut",
        "LocationIn": "_lifesciences_48_LocationIn",
        "LocationOut": "_lifesciences_49_LocationOut",
        "VirtualMachineIn": "_lifesciences_50_VirtualMachineIn",
        "VirtualMachineOut": "_lifesciences_51_VirtualMachineOut",
        "UnexpectedExitStatusEventIn": "_lifesciences_52_UnexpectedExitStatusEventIn",
        "UnexpectedExitStatusEventOut": "_lifesciences_53_UnexpectedExitStatusEventOut",
        "EventIn": "_lifesciences_54_EventIn",
        "EventOut": "_lifesciences_55_EventOut",
        "DiskIn": "_lifesciences_56_DiskIn",
        "DiskOut": "_lifesciences_57_DiskOut",
        "FailedEventIn": "_lifesciences_58_FailedEventIn",
        "FailedEventOut": "_lifesciences_59_FailedEventOut",
        "NFSMountIn": "_lifesciences_60_NFSMountIn",
        "NFSMountOut": "_lifesciences_61_NFSMountOut",
        "VolumeIn": "_lifesciences_62_VolumeIn",
        "VolumeOut": "_lifesciences_63_VolumeOut",
        "ContainerKilledEventIn": "_lifesciences_64_ContainerKilledEventIn",
        "ContainerKilledEventOut": "_lifesciences_65_ContainerKilledEventOut",
        "ExistingDiskIn": "_lifesciences_66_ExistingDiskIn",
        "ExistingDiskOut": "_lifesciences_67_ExistingDiskOut",
        "ListLocationsResponseIn": "_lifesciences_68_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_lifesciences_69_ListLocationsResponseOut",
        "MountIn": "_lifesciences_70_MountIn",
        "MountOut": "_lifesciences_71_MountOut",
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
    types["AcceleratorIn"] = t.struct(
        {"type": t.string().optional(), "count": t.string().optional()}
    ).named(renames["AcceleratorIn"])
    types["AcceleratorOut"] = t.struct(
        {
            "type": t.string().optional(),
            "count": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AcceleratorOut"])
    types["PullStartedEventIn"] = t.struct({"imageUri": t.string().optional()}).named(
        renames["PullStartedEventIn"]
    )
    types["PullStartedEventOut"] = t.struct(
        {
            "imageUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PullStartedEventOut"])
    types["ActionIn"] = t.struct(
        {
            "publishExposedPorts": t.boolean().optional(),
            "portMappings": t.struct({"_": t.string().optional()}).optional(),
            "pidNamespace": t.string().optional(),
            "timeout": t.string().optional(),
            "containerName": t.string().optional(),
            "credentials": t.proxy(renames["SecretIn"]).optional(),
            "ignoreExitStatus": t.boolean().optional(),
            "environment": t.struct({"_": t.string().optional()}).optional(),
            "mounts": t.array(t.proxy(renames["MountIn"])).optional(),
            "imageUri": t.string(),
            "runInBackground": t.boolean().optional(),
            "disableImagePrefetch": t.boolean().optional(),
            "commands": t.array(t.string()).optional(),
            "entrypoint": t.string().optional(),
            "enableFuse": t.boolean().optional(),
            "encryptedEnvironment": t.proxy(renames["SecretIn"]).optional(),
            "alwaysRun": t.boolean().optional(),
            "blockExternalNetwork": t.boolean().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "disableStandardErrorCapture": t.boolean().optional(),
        }
    ).named(renames["ActionIn"])
    types["ActionOut"] = t.struct(
        {
            "publishExposedPorts": t.boolean().optional(),
            "portMappings": t.struct({"_": t.string().optional()}).optional(),
            "pidNamespace": t.string().optional(),
            "timeout": t.string().optional(),
            "containerName": t.string().optional(),
            "credentials": t.proxy(renames["SecretOut"]).optional(),
            "ignoreExitStatus": t.boolean().optional(),
            "environment": t.struct({"_": t.string().optional()}).optional(),
            "mounts": t.array(t.proxy(renames["MountOut"])).optional(),
            "imageUri": t.string(),
            "runInBackground": t.boolean().optional(),
            "disableImagePrefetch": t.boolean().optional(),
            "commands": t.array(t.string()).optional(),
            "entrypoint": t.string().optional(),
            "enableFuse": t.boolean().optional(),
            "encryptedEnvironment": t.proxy(renames["SecretOut"]).optional(),
            "alwaysRun": t.boolean().optional(),
            "blockExternalNetwork": t.boolean().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "disableStandardErrorCapture": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActionOut"])
    types["ContainerStartedEventIn"] = t.struct(
        {
            "ipAddress": t.string().optional(),
            "portMappings": t.struct({"_": t.string().optional()}).optional(),
            "actionId": t.integer().optional(),
        }
    ).named(renames["ContainerStartedEventIn"])
    types["ContainerStartedEventOut"] = t.struct(
        {
            "ipAddress": t.string().optional(),
            "portMappings": t.struct({"_": t.string().optional()}).optional(),
            "actionId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContainerStartedEventOut"])
    types["PipelineIn"] = t.struct(
        {
            "resources": t.proxy(renames["ResourcesIn"]).optional(),
            "environment": t.struct({"_": t.string().optional()}).optional(),
            "encryptedEnvironment": t.proxy(renames["SecretIn"]).optional(),
            "timeout": t.string().optional(),
            "actions": t.array(t.proxy(renames["ActionIn"])).optional(),
        }
    ).named(renames["PipelineIn"])
    types["PipelineOut"] = t.struct(
        {
            "resources": t.proxy(renames["ResourcesOut"]).optional(),
            "environment": t.struct({"_": t.string().optional()}).optional(),
            "encryptedEnvironment": t.proxy(renames["SecretOut"]).optional(),
            "timeout": t.string().optional(),
            "actions": t.array(t.proxy(renames["ActionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PipelineOut"])
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
    types["ContainerStoppedEventIn"] = t.struct(
        {
            "actionId": t.integer().optional(),
            "exitStatus": t.integer().optional(),
            "stderr": t.string().optional(),
        }
    ).named(renames["ContainerStoppedEventIn"])
    types["ContainerStoppedEventOut"] = t.struct(
        {
            "actionId": t.integer().optional(),
            "exitStatus": t.integer().optional(),
            "stderr": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContainerStoppedEventOut"])
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
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
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
    types["DelayedEventIn"] = t.struct(
        {"cause": t.string().optional(), "metrics": t.array(t.string()).optional()}
    ).named(renames["DelayedEventIn"])
    types["DelayedEventOut"] = t.struct(
        {
            "cause": t.string().optional(),
            "metrics": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DelayedEventOut"])
    types["RunPipelineResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RunPipelineResponseIn"]
    )
    types["RunPipelineResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RunPipelineResponseOut"])
    types["SecretIn"] = t.struct(
        {"keyName": t.string().optional(), "cipherText": t.string().optional()}
    ).named(renames["SecretIn"])
    types["SecretOut"] = t.struct(
        {
            "keyName": t.string().optional(),
            "cipherText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecretOut"])
    types["RunPipelineRequestIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "pipeline": t.proxy(renames["PipelineIn"]),
            "pubSubTopic": t.string().optional(),
        }
    ).named(renames["RunPipelineRequestIn"])
    types["RunPipelineRequestOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "pipeline": t.proxy(renames["PipelineOut"]),
            "pubSubTopic": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunPipelineRequestOut"])
    types["PersistentDiskIn"] = t.struct(
        {
            "sizeGb": t.integer().optional(),
            "type": t.string().optional(),
            "sourceImage": t.string().optional(),
        }
    ).named(renames["PersistentDiskIn"])
    types["PersistentDiskOut"] = t.struct(
        {
            "sizeGb": t.integer().optional(),
            "type": t.string().optional(),
            "sourceImage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PersistentDiskOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["ResourcesIn"] = t.struct(
        {
            "regions": t.array(t.string()).optional(),
            "zones": t.array(t.string()).optional(),
            "virtualMachine": t.proxy(renames["VirtualMachineIn"]).optional(),
        }
    ).named(renames["ResourcesIn"])
    types["ResourcesOut"] = t.struct(
        {
            "regions": t.array(t.string()).optional(),
            "zones": t.array(t.string()).optional(),
            "virtualMachine": t.proxy(renames["VirtualMachineOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourcesOut"])
    types["WorkerAssignedEventIn"] = t.struct(
        {
            "machineType": t.string().optional(),
            "instance": t.string().optional(),
            "zone": t.string().optional(),
        }
    ).named(renames["WorkerAssignedEventIn"])
    types["WorkerAssignedEventOut"] = t.struct(
        {
            "machineType": t.string().optional(),
            "instance": t.string().optional(),
            "zone": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkerAssignedEventOut"])
    types["NetworkIn"] = t.struct(
        {
            "subnetwork": t.string().optional(),
            "network": t.string().optional(),
            "usePrivateAddress": t.boolean().optional(),
        }
    ).named(renames["NetworkIn"])
    types["NetworkOut"] = t.struct(
        {
            "subnetwork": t.string().optional(),
            "network": t.string().optional(),
            "usePrivateAddress": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkOut"])
    types["MetadataIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "events": t.array(t.proxy(renames["EventIn"])).optional(),
            "pubSubTopic": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "endTime": t.string().optional(),
            "pipeline": t.proxy(renames["PipelineIn"]).optional(),
            "startTime": t.string().optional(),
        }
    ).named(renames["MetadataIn"])
    types["MetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "events": t.array(t.proxy(renames["EventOut"])).optional(),
            "pubSubTopic": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "endTime": t.string().optional(),
            "pipeline": t.proxy(renames["PipelineOut"]).optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetadataOut"])
    types["LocationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["VirtualMachineIn"] = t.struct(
        {
            "serviceAccount": t.proxy(renames["ServiceAccountIn"]).optional(),
            "dockerCacheImages": t.array(t.string()).optional(),
            "preemptible": t.boolean().optional(),
            "reservation": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "enableStackdriverMonitoring": t.boolean().optional(),
            "bootImage": t.string().optional(),
            "nvidiaDriverVersion": t.string().optional(),
            "accelerators": t.array(t.proxy(renames["AcceleratorIn"])).optional(),
            "network": t.proxy(renames["NetworkIn"]).optional(),
            "bootDiskSizeGb": t.integer().optional(),
            "machineType": t.string(),
            "volumes": t.array(t.proxy(renames["VolumeIn"])).optional(),
            "disks": t.array(t.proxy(renames["DiskIn"])).optional(),
            "cpuPlatform": t.string().optional(),
        }
    ).named(renames["VirtualMachineIn"])
    types["VirtualMachineOut"] = t.struct(
        {
            "serviceAccount": t.proxy(renames["ServiceAccountOut"]).optional(),
            "dockerCacheImages": t.array(t.string()).optional(),
            "preemptible": t.boolean().optional(),
            "reservation": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "enableStackdriverMonitoring": t.boolean().optional(),
            "bootImage": t.string().optional(),
            "nvidiaDriverVersion": t.string().optional(),
            "accelerators": t.array(t.proxy(renames["AcceleratorOut"])).optional(),
            "network": t.proxy(renames["NetworkOut"]).optional(),
            "bootDiskSizeGb": t.integer().optional(),
            "machineType": t.string(),
            "volumes": t.array(t.proxy(renames["VolumeOut"])).optional(),
            "disks": t.array(t.proxy(renames["DiskOut"])).optional(),
            "cpuPlatform": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VirtualMachineOut"])
    types["UnexpectedExitStatusEventIn"] = t.struct(
        {"exitStatus": t.integer().optional(), "actionId": t.integer().optional()}
    ).named(renames["UnexpectedExitStatusEventIn"])
    types["UnexpectedExitStatusEventOut"] = t.struct(
        {
            "exitStatus": t.integer().optional(),
            "actionId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UnexpectedExitStatusEventOut"])
    types["EventIn"] = t.struct(
        {
            "containerKilled": t.proxy(renames["ContainerKilledEventIn"]).optional(),
            "failed": t.proxy(renames["FailedEventIn"]).optional(),
            "workerReleased": t.proxy(renames["WorkerReleasedEventIn"]).optional(),
            "description": t.string().optional(),
            "pullStopped": t.proxy(renames["PullStoppedEventIn"]).optional(),
            "workerAssigned": t.proxy(renames["WorkerAssignedEventIn"]).optional(),
            "containerStopped": t.proxy(renames["ContainerStoppedEventIn"]).optional(),
            "pullStarted": t.proxy(renames["PullStartedEventIn"]).optional(),
            "unexpectedExitStatus": t.proxy(
                renames["UnexpectedExitStatusEventIn"]
            ).optional(),
            "timestamp": t.string().optional(),
            "containerStarted": t.proxy(renames["ContainerStartedEventIn"]).optional(),
            "delayed": t.proxy(renames["DelayedEventIn"]).optional(),
        }
    ).named(renames["EventIn"])
    types["EventOut"] = t.struct(
        {
            "containerKilled": t.proxy(renames["ContainerKilledEventOut"]).optional(),
            "failed": t.proxy(renames["FailedEventOut"]).optional(),
            "workerReleased": t.proxy(renames["WorkerReleasedEventOut"]).optional(),
            "description": t.string().optional(),
            "pullStopped": t.proxy(renames["PullStoppedEventOut"]).optional(),
            "workerAssigned": t.proxy(renames["WorkerAssignedEventOut"]).optional(),
            "containerStopped": t.proxy(renames["ContainerStoppedEventOut"]).optional(),
            "pullStarted": t.proxy(renames["PullStartedEventOut"]).optional(),
            "unexpectedExitStatus": t.proxy(
                renames["UnexpectedExitStatusEventOut"]
            ).optional(),
            "timestamp": t.string().optional(),
            "containerStarted": t.proxy(renames["ContainerStartedEventOut"]).optional(),
            "delayed": t.proxy(renames["DelayedEventOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventOut"])
    types["DiskIn"] = t.struct(
        {
            "sizeGb": t.integer().optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
            "sourceImage": t.string().optional(),
        }
    ).named(renames["DiskIn"])
    types["DiskOut"] = t.struct(
        {
            "sizeGb": t.integer().optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
            "sourceImage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiskOut"])
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
            "persistentDisk": t.proxy(renames["PersistentDiskIn"]).optional(),
            "volume": t.string().optional(),
            "nfsMount": t.proxy(renames["NFSMountIn"]).optional(),
            "existingDisk": t.proxy(renames["ExistingDiskIn"]).optional(),
        }
    ).named(renames["VolumeIn"])
    types["VolumeOut"] = t.struct(
        {
            "persistentDisk": t.proxy(renames["PersistentDiskOut"]).optional(),
            "volume": t.string().optional(),
            "nfsMount": t.proxy(renames["NFSMountOut"]).optional(),
            "existingDisk": t.proxy(renames["ExistingDiskOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VolumeOut"])
    types["ContainerKilledEventIn"] = t.struct(
        {"actionId": t.integer().optional()}
    ).named(renames["ContainerKilledEventIn"])
    types["ContainerKilledEventOut"] = t.struct(
        {
            "actionId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContainerKilledEventOut"])
    types["ExistingDiskIn"] = t.struct({"disk": t.string().optional()}).named(
        renames["ExistingDiskIn"]
    )
    types["ExistingDiskOut"] = t.struct(
        {
            "disk": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExistingDiskOut"])
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
    types["MountIn"] = t.struct(
        {
            "path": t.string().optional(),
            "disk": t.string().optional(),
            "readOnly": t.boolean().optional(),
        }
    ).named(renames["MountIn"])
    types["MountOut"] = t.struct(
        {
            "path": t.string().optional(),
            "disk": t.string().optional(),
            "readOnly": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MountOut"])

    functions = {}
    functions["projectsLocationsList"] = lifesciences.get(
        "v2beta/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = lifesciences.get(
        "v2beta/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPipelinesRun"] = lifesciences.post(
        "v2beta/{parent}/pipelines:run",
        t.struct(
            {
                "parent": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "pipeline": t.proxy(renames["PipelineIn"]),
                "pubSubTopic": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = lifesciences.post(
        "v2beta/{name}:cancel",
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
    functions["projectsLocationsOperationsList"] = lifesciences.post(
        "v2beta/{name}:cancel",
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
    functions["projectsLocationsOperationsCancel"] = lifesciences.post(
        "v2beta/{name}:cancel",
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

    return Import(
        importer="lifesciences", renames=renames, types=types, functions=functions
    )
