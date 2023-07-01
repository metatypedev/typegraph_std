from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_lifesciences():
    lifesciences = HTTPRuntime("https://lifesciences.googleapis.com/")

    renames = {
        "ErrorResponse": "_lifesciences_1_ErrorResponse",
        "FailedEventIn": "_lifesciences_2_FailedEventIn",
        "FailedEventOut": "_lifesciences_3_FailedEventOut",
        "PersistentDiskIn": "_lifesciences_4_PersistentDiskIn",
        "PersistentDiskOut": "_lifesciences_5_PersistentDiskOut",
        "CancelOperationRequestIn": "_lifesciences_6_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_lifesciences_7_CancelOperationRequestOut",
        "ContainerKilledEventIn": "_lifesciences_8_ContainerKilledEventIn",
        "ContainerKilledEventOut": "_lifesciences_9_ContainerKilledEventOut",
        "SecretIn": "_lifesciences_10_SecretIn",
        "SecretOut": "_lifesciences_11_SecretOut",
        "EventIn": "_lifesciences_12_EventIn",
        "EventOut": "_lifesciences_13_EventOut",
        "RunPipelineResponseIn": "_lifesciences_14_RunPipelineResponseIn",
        "RunPipelineResponseOut": "_lifesciences_15_RunPipelineResponseOut",
        "RunPipelineRequestIn": "_lifesciences_16_RunPipelineRequestIn",
        "RunPipelineRequestOut": "_lifesciences_17_RunPipelineRequestOut",
        "MetadataIn": "_lifesciences_18_MetadataIn",
        "MetadataOut": "_lifesciences_19_MetadataOut",
        "WorkerAssignedEventIn": "_lifesciences_20_WorkerAssignedEventIn",
        "WorkerAssignedEventOut": "_lifesciences_21_WorkerAssignedEventOut",
        "ListOperationsResponseIn": "_lifesciences_22_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_lifesciences_23_ListOperationsResponseOut",
        "NetworkIn": "_lifesciences_24_NetworkIn",
        "NetworkOut": "_lifesciences_25_NetworkOut",
        "ContainerStartedEventIn": "_lifesciences_26_ContainerStartedEventIn",
        "ContainerStartedEventOut": "_lifesciences_27_ContainerStartedEventOut",
        "StatusIn": "_lifesciences_28_StatusIn",
        "StatusOut": "_lifesciences_29_StatusOut",
        "PullStoppedEventIn": "_lifesciences_30_PullStoppedEventIn",
        "PullStoppedEventOut": "_lifesciences_31_PullStoppedEventOut",
        "ExistingDiskIn": "_lifesciences_32_ExistingDiskIn",
        "ExistingDiskOut": "_lifesciences_33_ExistingDiskOut",
        "PipelineIn": "_lifesciences_34_PipelineIn",
        "PipelineOut": "_lifesciences_35_PipelineOut",
        "MountIn": "_lifesciences_36_MountIn",
        "MountOut": "_lifesciences_37_MountOut",
        "LocationIn": "_lifesciences_38_LocationIn",
        "LocationOut": "_lifesciences_39_LocationOut",
        "OperationIn": "_lifesciences_40_OperationIn",
        "OperationOut": "_lifesciences_41_OperationOut",
        "NFSMountIn": "_lifesciences_42_NFSMountIn",
        "NFSMountOut": "_lifesciences_43_NFSMountOut",
        "ServiceAccountIn": "_lifesciences_44_ServiceAccountIn",
        "ServiceAccountOut": "_lifesciences_45_ServiceAccountOut",
        "DelayedEventIn": "_lifesciences_46_DelayedEventIn",
        "DelayedEventOut": "_lifesciences_47_DelayedEventOut",
        "ContainerStoppedEventIn": "_lifesciences_48_ContainerStoppedEventIn",
        "ContainerStoppedEventOut": "_lifesciences_49_ContainerStoppedEventOut",
        "AcceleratorIn": "_lifesciences_50_AcceleratorIn",
        "AcceleratorOut": "_lifesciences_51_AcceleratorOut",
        "EmptyIn": "_lifesciences_52_EmptyIn",
        "EmptyOut": "_lifesciences_53_EmptyOut",
        "PullStartedEventIn": "_lifesciences_54_PullStartedEventIn",
        "PullStartedEventOut": "_lifesciences_55_PullStartedEventOut",
        "ListLocationsResponseIn": "_lifesciences_56_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_lifesciences_57_ListLocationsResponseOut",
        "VolumeIn": "_lifesciences_58_VolumeIn",
        "VolumeOut": "_lifesciences_59_VolumeOut",
        "VirtualMachineIn": "_lifesciences_60_VirtualMachineIn",
        "VirtualMachineOut": "_lifesciences_61_VirtualMachineOut",
        "ActionIn": "_lifesciences_62_ActionIn",
        "ActionOut": "_lifesciences_63_ActionOut",
        "ResourcesIn": "_lifesciences_64_ResourcesIn",
        "ResourcesOut": "_lifesciences_65_ResourcesOut",
        "UnexpectedExitStatusEventIn": "_lifesciences_66_UnexpectedExitStatusEventIn",
        "UnexpectedExitStatusEventOut": "_lifesciences_67_UnexpectedExitStatusEventOut",
        "DiskIn": "_lifesciences_68_DiskIn",
        "DiskOut": "_lifesciences_69_DiskOut",
        "WorkerReleasedEventIn": "_lifesciences_70_WorkerReleasedEventIn",
        "WorkerReleasedEventOut": "_lifesciences_71_WorkerReleasedEventOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["ContainerKilledEventIn"] = t.struct(
        {"actionId": t.integer().optional()}
    ).named(renames["ContainerKilledEventIn"])
    types["ContainerKilledEventOut"] = t.struct(
        {
            "actionId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContainerKilledEventOut"])
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
    types["EventIn"] = t.struct(
        {
            "workerReleased": t.proxy(renames["WorkerReleasedEventIn"]).optional(),
            "containerStopped": t.proxy(renames["ContainerStoppedEventIn"]).optional(),
            "description": t.string().optional(),
            "containerKilled": t.proxy(renames["ContainerKilledEventIn"]).optional(),
            "delayed": t.proxy(renames["DelayedEventIn"]).optional(),
            "containerStarted": t.proxy(renames["ContainerStartedEventIn"]).optional(),
            "pullStarted": t.proxy(renames["PullStartedEventIn"]).optional(),
            "unexpectedExitStatus": t.proxy(
                renames["UnexpectedExitStatusEventIn"]
            ).optional(),
            "pullStopped": t.proxy(renames["PullStoppedEventIn"]).optional(),
            "timestamp": t.string().optional(),
            "failed": t.proxy(renames["FailedEventIn"]).optional(),
            "workerAssigned": t.proxy(renames["WorkerAssignedEventIn"]).optional(),
        }
    ).named(renames["EventIn"])
    types["EventOut"] = t.struct(
        {
            "workerReleased": t.proxy(renames["WorkerReleasedEventOut"]).optional(),
            "containerStopped": t.proxy(renames["ContainerStoppedEventOut"]).optional(),
            "description": t.string().optional(),
            "containerKilled": t.proxy(renames["ContainerKilledEventOut"]).optional(),
            "delayed": t.proxy(renames["DelayedEventOut"]).optional(),
            "containerStarted": t.proxy(renames["ContainerStartedEventOut"]).optional(),
            "pullStarted": t.proxy(renames["PullStartedEventOut"]).optional(),
            "unexpectedExitStatus": t.proxy(
                renames["UnexpectedExitStatusEventOut"]
            ).optional(),
            "pullStopped": t.proxy(renames["PullStoppedEventOut"]).optional(),
            "timestamp": t.string().optional(),
            "failed": t.proxy(renames["FailedEventOut"]).optional(),
            "workerAssigned": t.proxy(renames["WorkerAssignedEventOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventOut"])
    types["RunPipelineResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RunPipelineResponseIn"]
    )
    types["RunPipelineResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RunPipelineResponseOut"])
    types["RunPipelineRequestIn"] = t.struct(
        {
            "pubSubTopic": t.string().optional(),
            "pipeline": t.proxy(renames["PipelineIn"]),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["RunPipelineRequestIn"])
    types["RunPipelineRequestOut"] = t.struct(
        {
            "pubSubTopic": t.string().optional(),
            "pipeline": t.proxy(renames["PipelineOut"]),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunPipelineRequestOut"])
    types["MetadataIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "endTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "pubSubTopic": t.string().optional(),
            "events": t.array(t.proxy(renames["EventIn"])).optional(),
            "pipeline": t.proxy(renames["PipelineIn"]).optional(),
            "startTime": t.string().optional(),
        }
    ).named(renames["MetadataIn"])
    types["MetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "endTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "pubSubTopic": t.string().optional(),
            "events": t.array(t.proxy(renames["EventOut"])).optional(),
            "pipeline": t.proxy(renames["PipelineOut"]).optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetadataOut"])
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
    types["NetworkIn"] = t.struct(
        {
            "subnetwork": t.string().optional(),
            "usePrivateAddress": t.boolean().optional(),
            "network": t.string().optional(),
        }
    ).named(renames["NetworkIn"])
    types["NetworkOut"] = t.struct(
        {
            "subnetwork": t.string().optional(),
            "usePrivateAddress": t.boolean().optional(),
            "network": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkOut"])
    types["ContainerStartedEventIn"] = t.struct(
        {
            "portMappings": t.struct({"_": t.string().optional()}).optional(),
            "actionId": t.integer().optional(),
            "ipAddress": t.string().optional(),
        }
    ).named(renames["ContainerStartedEventIn"])
    types["ContainerStartedEventOut"] = t.struct(
        {
            "portMappings": t.struct({"_": t.string().optional()}).optional(),
            "actionId": t.integer().optional(),
            "ipAddress": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContainerStartedEventOut"])
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
    types["PullStoppedEventIn"] = t.struct({"imageUri": t.string().optional()}).named(
        renames["PullStoppedEventIn"]
    )
    types["PullStoppedEventOut"] = t.struct(
        {
            "imageUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PullStoppedEventOut"])
    types["ExistingDiskIn"] = t.struct({"disk": t.string().optional()}).named(
        renames["ExistingDiskIn"]
    )
    types["ExistingDiskOut"] = t.struct(
        {
            "disk": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExistingDiskOut"])
    types["PipelineIn"] = t.struct(
        {
            "timeout": t.string().optional(),
            "resources": t.proxy(renames["ResourcesIn"]).optional(),
            "environment": t.struct({"_": t.string().optional()}).optional(),
            "actions": t.array(t.proxy(renames["ActionIn"])).optional(),
            "encryptedEnvironment": t.proxy(renames["SecretIn"]).optional(),
        }
    ).named(renames["PipelineIn"])
    types["PipelineOut"] = t.struct(
        {
            "timeout": t.string().optional(),
            "resources": t.proxy(renames["ResourcesOut"]).optional(),
            "environment": t.struct({"_": t.string().optional()}).optional(),
            "actions": t.array(t.proxy(renames["ActionOut"])).optional(),
            "encryptedEnvironment": t.proxy(renames["SecretOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PipelineOut"])
    types["MountIn"] = t.struct(
        {
            "disk": t.string().optional(),
            "path": t.string().optional(),
            "readOnly": t.boolean().optional(),
        }
    ).named(renames["MountIn"])
    types["MountOut"] = t.struct(
        {
            "disk": t.string().optional(),
            "path": t.string().optional(),
            "readOnly": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MountOut"])
    types["LocationIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["OperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["NFSMountIn"] = t.struct({"target": t.string().optional()}).named(
        renames["NFSMountIn"]
    )
    types["NFSMountOut"] = t.struct(
        {
            "target": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NFSMountOut"])
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
    types["ContainerStoppedEventIn"] = t.struct(
        {
            "exitStatus": t.integer().optional(),
            "actionId": t.integer().optional(),
            "stderr": t.string().optional(),
        }
    ).named(renames["ContainerStoppedEventIn"])
    types["ContainerStoppedEventOut"] = t.struct(
        {
            "exitStatus": t.integer().optional(),
            "actionId": t.integer().optional(),
            "stderr": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContainerStoppedEventOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["PullStartedEventIn"] = t.struct({"imageUri": t.string().optional()}).named(
        renames["PullStartedEventIn"]
    )
    types["PullStartedEventOut"] = t.struct(
        {
            "imageUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PullStartedEventOut"])
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
    types["VolumeIn"] = t.struct(
        {
            "existingDisk": t.proxy(renames["ExistingDiskIn"]).optional(),
            "nfsMount": t.proxy(renames["NFSMountIn"]).optional(),
            "volume": t.string().optional(),
            "persistentDisk": t.proxy(renames["PersistentDiskIn"]).optional(),
        }
    ).named(renames["VolumeIn"])
    types["VolumeOut"] = t.struct(
        {
            "existingDisk": t.proxy(renames["ExistingDiskOut"]).optional(),
            "nfsMount": t.proxy(renames["NFSMountOut"]).optional(),
            "volume": t.string().optional(),
            "persistentDisk": t.proxy(renames["PersistentDiskOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VolumeOut"])
    types["VirtualMachineIn"] = t.struct(
        {
            "disks": t.array(t.proxy(renames["DiskIn"])).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "network": t.proxy(renames["NetworkIn"]).optional(),
            "machineType": t.string(),
            "preemptible": t.boolean().optional(),
            "cpuPlatform": t.string().optional(),
            "bootDiskSizeGb": t.integer().optional(),
            "nvidiaDriverVersion": t.string().optional(),
            "volumes": t.array(t.proxy(renames["VolumeIn"])).optional(),
            "accelerators": t.array(t.proxy(renames["AcceleratorIn"])).optional(),
            "serviceAccount": t.proxy(renames["ServiceAccountIn"]).optional(),
            "reservation": t.string().optional(),
            "dockerCacheImages": t.array(t.string()).optional(),
            "bootImage": t.string().optional(),
            "enableStackdriverMonitoring": t.boolean().optional(),
        }
    ).named(renames["VirtualMachineIn"])
    types["VirtualMachineOut"] = t.struct(
        {
            "disks": t.array(t.proxy(renames["DiskOut"])).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "network": t.proxy(renames["NetworkOut"]).optional(),
            "machineType": t.string(),
            "preemptible": t.boolean().optional(),
            "cpuPlatform": t.string().optional(),
            "bootDiskSizeGb": t.integer().optional(),
            "nvidiaDriverVersion": t.string().optional(),
            "volumes": t.array(t.proxy(renames["VolumeOut"])).optional(),
            "accelerators": t.array(t.proxy(renames["AcceleratorOut"])).optional(),
            "serviceAccount": t.proxy(renames["ServiceAccountOut"]).optional(),
            "reservation": t.string().optional(),
            "dockerCacheImages": t.array(t.string()).optional(),
            "bootImage": t.string().optional(),
            "enableStackdriverMonitoring": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VirtualMachineOut"])
    types["ActionIn"] = t.struct(
        {
            "enableFuse": t.boolean().optional(),
            "blockExternalNetwork": t.boolean().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "disableStandardErrorCapture": t.boolean().optional(),
            "portMappings": t.struct({"_": t.string().optional()}).optional(),
            "publishExposedPorts": t.boolean().optional(),
            "ignoreExitStatus": t.boolean().optional(),
            "entrypoint": t.string().optional(),
            "runInBackground": t.boolean().optional(),
            "disableImagePrefetch": t.boolean().optional(),
            "timeout": t.string().optional(),
            "encryptedEnvironment": t.proxy(renames["SecretIn"]).optional(),
            "containerName": t.string().optional(),
            "credentials": t.proxy(renames["SecretIn"]).optional(),
            "environment": t.struct({"_": t.string().optional()}).optional(),
            "mounts": t.array(t.proxy(renames["MountIn"])).optional(),
            "commands": t.array(t.string()).optional(),
            "pidNamespace": t.string().optional(),
            "alwaysRun": t.boolean().optional(),
            "imageUri": t.string(),
        }
    ).named(renames["ActionIn"])
    types["ActionOut"] = t.struct(
        {
            "enableFuse": t.boolean().optional(),
            "blockExternalNetwork": t.boolean().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "disableStandardErrorCapture": t.boolean().optional(),
            "portMappings": t.struct({"_": t.string().optional()}).optional(),
            "publishExposedPorts": t.boolean().optional(),
            "ignoreExitStatus": t.boolean().optional(),
            "entrypoint": t.string().optional(),
            "runInBackground": t.boolean().optional(),
            "disableImagePrefetch": t.boolean().optional(),
            "timeout": t.string().optional(),
            "encryptedEnvironment": t.proxy(renames["SecretOut"]).optional(),
            "containerName": t.string().optional(),
            "credentials": t.proxy(renames["SecretOut"]).optional(),
            "environment": t.struct({"_": t.string().optional()}).optional(),
            "mounts": t.array(t.proxy(renames["MountOut"])).optional(),
            "commands": t.array(t.string()).optional(),
            "pidNamespace": t.string().optional(),
            "alwaysRun": t.boolean().optional(),
            "imageUri": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActionOut"])
    types["ResourcesIn"] = t.struct(
        {
            "virtualMachine": t.proxy(renames["VirtualMachineIn"]).optional(),
            "regions": t.array(t.string()).optional(),
            "zones": t.array(t.string()).optional(),
        }
    ).named(renames["ResourcesIn"])
    types["ResourcesOut"] = t.struct(
        {
            "virtualMachine": t.proxy(renames["VirtualMachineOut"]).optional(),
            "regions": t.array(t.string()).optional(),
            "zones": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourcesOut"])
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
                "pubSubTopic": t.string().optional(),
                "pipeline": t.proxy(renames["PipelineIn"]),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = lifesciences.get(
        "v2beta/{name}/operations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = lifesciences.get(
        "v2beta/{name}/operations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = lifesciences.get(
        "v2beta/{name}/operations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="lifesciences",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
