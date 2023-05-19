from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_lifesciences() -> Import:
    lifesciences = HTTPRuntime("https://lifesciences.googleapis.com/")

    renames = {
        "ErrorResponse": "_lifesciences_1_ErrorResponse",
        "CancelOperationRequestIn": "_lifesciences_2_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_lifesciences_3_CancelOperationRequestOut",
        "RunPipelineRequestIn": "_lifesciences_4_RunPipelineRequestIn",
        "RunPipelineRequestOut": "_lifesciences_5_RunPipelineRequestOut",
        "PersistentDiskIn": "_lifesciences_6_PersistentDiskIn",
        "PersistentDiskOut": "_lifesciences_7_PersistentDiskOut",
        "ResourcesIn": "_lifesciences_8_ResourcesIn",
        "ResourcesOut": "_lifesciences_9_ResourcesOut",
        "EmptyIn": "_lifesciences_10_EmptyIn",
        "EmptyOut": "_lifesciences_11_EmptyOut",
        "PipelineIn": "_lifesciences_12_PipelineIn",
        "PipelineOut": "_lifesciences_13_PipelineOut",
        "PullStoppedEventIn": "_lifesciences_14_PullStoppedEventIn",
        "PullStoppedEventOut": "_lifesciences_15_PullStoppedEventOut",
        "DelayedEventIn": "_lifesciences_16_DelayedEventIn",
        "DelayedEventOut": "_lifesciences_17_DelayedEventOut",
        "ListLocationsResponseIn": "_lifesciences_18_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_lifesciences_19_ListLocationsResponseOut",
        "ActionIn": "_lifesciences_20_ActionIn",
        "ActionOut": "_lifesciences_21_ActionOut",
        "ListOperationsResponseIn": "_lifesciences_22_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_lifesciences_23_ListOperationsResponseOut",
        "VolumeIn": "_lifesciences_24_VolumeIn",
        "VolumeOut": "_lifesciences_25_VolumeOut",
        "ExistingDiskIn": "_lifesciences_26_ExistingDiskIn",
        "ExistingDiskOut": "_lifesciences_27_ExistingDiskOut",
        "MountIn": "_lifesciences_28_MountIn",
        "MountOut": "_lifesciences_29_MountOut",
        "AcceleratorIn": "_lifesciences_30_AcceleratorIn",
        "AcceleratorOut": "_lifesciences_31_AcceleratorOut",
        "OperationIn": "_lifesciences_32_OperationIn",
        "OperationOut": "_lifesciences_33_OperationOut",
        "NetworkIn": "_lifesciences_34_NetworkIn",
        "NetworkOut": "_lifesciences_35_NetworkOut",
        "EventIn": "_lifesciences_36_EventIn",
        "EventOut": "_lifesciences_37_EventOut",
        "WorkerReleasedEventIn": "_lifesciences_38_WorkerReleasedEventIn",
        "WorkerReleasedEventOut": "_lifesciences_39_WorkerReleasedEventOut",
        "ContainerKilledEventIn": "_lifesciences_40_ContainerKilledEventIn",
        "ContainerKilledEventOut": "_lifesciences_41_ContainerKilledEventOut",
        "StatusIn": "_lifesciences_42_StatusIn",
        "StatusOut": "_lifesciences_43_StatusOut",
        "RunPipelineResponseIn": "_lifesciences_44_RunPipelineResponseIn",
        "RunPipelineResponseOut": "_lifesciences_45_RunPipelineResponseOut",
        "ContainerStoppedEventIn": "_lifesciences_46_ContainerStoppedEventIn",
        "ContainerStoppedEventOut": "_lifesciences_47_ContainerStoppedEventOut",
        "UnexpectedExitStatusEventIn": "_lifesciences_48_UnexpectedExitStatusEventIn",
        "UnexpectedExitStatusEventOut": "_lifesciences_49_UnexpectedExitStatusEventOut",
        "MetadataIn": "_lifesciences_50_MetadataIn",
        "MetadataOut": "_lifesciences_51_MetadataOut",
        "DiskIn": "_lifesciences_52_DiskIn",
        "DiskOut": "_lifesciences_53_DiskOut",
        "ContainerStartedEventIn": "_lifesciences_54_ContainerStartedEventIn",
        "ContainerStartedEventOut": "_lifesciences_55_ContainerStartedEventOut",
        "LocationIn": "_lifesciences_56_LocationIn",
        "LocationOut": "_lifesciences_57_LocationOut",
        "FailedEventIn": "_lifesciences_58_FailedEventIn",
        "FailedEventOut": "_lifesciences_59_FailedEventOut",
        "VirtualMachineIn": "_lifesciences_60_VirtualMachineIn",
        "VirtualMachineOut": "_lifesciences_61_VirtualMachineOut",
        "ServiceAccountIn": "_lifesciences_62_ServiceAccountIn",
        "ServiceAccountOut": "_lifesciences_63_ServiceAccountOut",
        "NFSMountIn": "_lifesciences_64_NFSMountIn",
        "NFSMountOut": "_lifesciences_65_NFSMountOut",
        "WorkerAssignedEventIn": "_lifesciences_66_WorkerAssignedEventIn",
        "WorkerAssignedEventOut": "_lifesciences_67_WorkerAssignedEventOut",
        "SecretIn": "_lifesciences_68_SecretIn",
        "SecretOut": "_lifesciences_69_SecretOut",
        "PullStartedEventIn": "_lifesciences_70_PullStartedEventIn",
        "PullStartedEventOut": "_lifesciences_71_PullStartedEventOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
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
            "sourceImage": t.string().optional(),
            "sizeGb": t.integer().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["PersistentDiskIn"])
    types["PersistentDiskOut"] = t.struct(
        {
            "sourceImage": t.string().optional(),
            "sizeGb": t.integer().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PersistentDiskOut"])
    types["ResourcesIn"] = t.struct(
        {
            "zones": t.array(t.string()).optional(),
            "regions": t.array(t.string()).optional(),
            "virtualMachine": t.proxy(renames["VirtualMachineIn"]).optional(),
        }
    ).named(renames["ResourcesIn"])
    types["ResourcesOut"] = t.struct(
        {
            "zones": t.array(t.string()).optional(),
            "regions": t.array(t.string()).optional(),
            "virtualMachine": t.proxy(renames["VirtualMachineOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourcesOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["PipelineIn"] = t.struct(
        {
            "actions": t.array(t.proxy(renames["ActionIn"])).optional(),
            "encryptedEnvironment": t.proxy(renames["SecretIn"]).optional(),
            "timeout": t.string().optional(),
            "resources": t.proxy(renames["ResourcesIn"]).optional(),
            "environment": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["PipelineIn"])
    types["PipelineOut"] = t.struct(
        {
            "actions": t.array(t.proxy(renames["ActionOut"])).optional(),
            "encryptedEnvironment": t.proxy(renames["SecretOut"]).optional(),
            "timeout": t.string().optional(),
            "resources": t.proxy(renames["ResourcesOut"]).optional(),
            "environment": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PipelineOut"])
    types["PullStoppedEventIn"] = t.struct({"imageUri": t.string().optional()}).named(
        renames["PullStoppedEventIn"]
    )
    types["PullStoppedEventOut"] = t.struct(
        {
            "imageUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PullStoppedEventOut"])
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
    types["ActionIn"] = t.struct(
        {
            "disableStandardErrorCapture": t.boolean().optional(),
            "commands": t.array(t.string()).optional(),
            "entrypoint": t.string().optional(),
            "alwaysRun": t.boolean().optional(),
            "blockExternalNetwork": t.boolean().optional(),
            "pidNamespace": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "timeout": t.string().optional(),
            "containerName": t.string().optional(),
            "imageUri": t.string(),
            "runInBackground": t.boolean().optional(),
            "environment": t.struct({"_": t.string().optional()}).optional(),
            "credentials": t.proxy(renames["SecretIn"]).optional(),
            "disableImagePrefetch": t.boolean().optional(),
            "publishExposedPorts": t.boolean().optional(),
            "enableFuse": t.boolean().optional(),
            "mounts": t.array(t.proxy(renames["MountIn"])).optional(),
            "ignoreExitStatus": t.boolean().optional(),
            "encryptedEnvironment": t.proxy(renames["SecretIn"]).optional(),
            "portMappings": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ActionIn"])
    types["ActionOut"] = t.struct(
        {
            "disableStandardErrorCapture": t.boolean().optional(),
            "commands": t.array(t.string()).optional(),
            "entrypoint": t.string().optional(),
            "alwaysRun": t.boolean().optional(),
            "blockExternalNetwork": t.boolean().optional(),
            "pidNamespace": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "timeout": t.string().optional(),
            "containerName": t.string().optional(),
            "imageUri": t.string(),
            "runInBackground": t.boolean().optional(),
            "environment": t.struct({"_": t.string().optional()}).optional(),
            "credentials": t.proxy(renames["SecretOut"]).optional(),
            "disableImagePrefetch": t.boolean().optional(),
            "publishExposedPorts": t.boolean().optional(),
            "enableFuse": t.boolean().optional(),
            "mounts": t.array(t.proxy(renames["MountOut"])).optional(),
            "ignoreExitStatus": t.boolean().optional(),
            "encryptedEnvironment": t.proxy(renames["SecretOut"]).optional(),
            "portMappings": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActionOut"])
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
    types["VolumeIn"] = t.struct(
        {
            "volume": t.string().optional(),
            "nfsMount": t.proxy(renames["NFSMountIn"]).optional(),
            "existingDisk": t.proxy(renames["ExistingDiskIn"]).optional(),
            "persistentDisk": t.proxy(renames["PersistentDiskIn"]).optional(),
        }
    ).named(renames["VolumeIn"])
    types["VolumeOut"] = t.struct(
        {
            "volume": t.string().optional(),
            "nfsMount": t.proxy(renames["NFSMountOut"]).optional(),
            "existingDisk": t.proxy(renames["ExistingDiskOut"]).optional(),
            "persistentDisk": t.proxy(renames["PersistentDiskOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VolumeOut"])
    types["ExistingDiskIn"] = t.struct({"disk": t.string().optional()}).named(
        renames["ExistingDiskIn"]
    )
    types["ExistingDiskOut"] = t.struct(
        {
            "disk": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExistingDiskOut"])
    types["MountIn"] = t.struct(
        {
            "path": t.string().optional(),
            "readOnly": t.boolean().optional(),
            "disk": t.string().optional(),
        }
    ).named(renames["MountIn"])
    types["MountOut"] = t.struct(
        {
            "path": t.string().optional(),
            "readOnly": t.boolean().optional(),
            "disk": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MountOut"])
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
    types["OperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
    types["NetworkIn"] = t.struct(
        {
            "usePrivateAddress": t.boolean().optional(),
            "network": t.string().optional(),
            "subnetwork": t.string().optional(),
        }
    ).named(renames["NetworkIn"])
    types["NetworkOut"] = t.struct(
        {
            "usePrivateAddress": t.boolean().optional(),
            "network": t.string().optional(),
            "subnetwork": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkOut"])
    types["EventIn"] = t.struct(
        {
            "timestamp": t.string().optional(),
            "containerStopped": t.proxy(renames["ContainerStoppedEventIn"]).optional(),
            "delayed": t.proxy(renames["DelayedEventIn"]).optional(),
            "unexpectedExitStatus": t.proxy(
                renames["UnexpectedExitStatusEventIn"]
            ).optional(),
            "containerStarted": t.proxy(renames["ContainerStartedEventIn"]).optional(),
            "containerKilled": t.proxy(renames["ContainerKilledEventIn"]).optional(),
            "pullStopped": t.proxy(renames["PullStoppedEventIn"]).optional(),
            "failed": t.proxy(renames["FailedEventIn"]).optional(),
            "description": t.string().optional(),
            "workerReleased": t.proxy(renames["WorkerReleasedEventIn"]).optional(),
            "workerAssigned": t.proxy(renames["WorkerAssignedEventIn"]).optional(),
            "pullStarted": t.proxy(renames["PullStartedEventIn"]).optional(),
        }
    ).named(renames["EventIn"])
    types["EventOut"] = t.struct(
        {
            "timestamp": t.string().optional(),
            "containerStopped": t.proxy(renames["ContainerStoppedEventOut"]).optional(),
            "delayed": t.proxy(renames["DelayedEventOut"]).optional(),
            "unexpectedExitStatus": t.proxy(
                renames["UnexpectedExitStatusEventOut"]
            ).optional(),
            "containerStarted": t.proxy(renames["ContainerStartedEventOut"]).optional(),
            "containerKilled": t.proxy(renames["ContainerKilledEventOut"]).optional(),
            "pullStopped": t.proxy(renames["PullStoppedEventOut"]).optional(),
            "failed": t.proxy(renames["FailedEventOut"]).optional(),
            "description": t.string().optional(),
            "workerReleased": t.proxy(renames["WorkerReleasedEventOut"]).optional(),
            "workerAssigned": t.proxy(renames["WorkerAssignedEventOut"]).optional(),
            "pullStarted": t.proxy(renames["PullStartedEventOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventOut"])
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
    types["ContainerKilledEventIn"] = t.struct(
        {"actionId": t.integer().optional()}
    ).named(renames["ContainerKilledEventIn"])
    types["ContainerKilledEventOut"] = t.struct(
        {
            "actionId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContainerKilledEventOut"])
    types["StatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["RunPipelineResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RunPipelineResponseIn"]
    )
    types["RunPipelineResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RunPipelineResponseOut"])
    types["ContainerStoppedEventIn"] = t.struct(
        {
            "stderr": t.string().optional(),
            "exitStatus": t.integer().optional(),
            "actionId": t.integer().optional(),
        }
    ).named(renames["ContainerStoppedEventIn"])
    types["ContainerStoppedEventOut"] = t.struct(
        {
            "stderr": t.string().optional(),
            "exitStatus": t.integer().optional(),
            "actionId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContainerStoppedEventOut"])
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
    types["MetadataIn"] = t.struct(
        {
            "pubSubTopic": t.string().optional(),
            "endTime": t.string().optional(),
            "pipeline": t.proxy(renames["PipelineIn"]).optional(),
            "events": t.array(t.proxy(renames["EventIn"])).optional(),
            "startTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["MetadataIn"])
    types["MetadataOut"] = t.struct(
        {
            "pubSubTopic": t.string().optional(),
            "endTime": t.string().optional(),
            "pipeline": t.proxy(renames["PipelineOut"]).optional(),
            "events": t.array(t.proxy(renames["EventOut"])).optional(),
            "startTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetadataOut"])
    types["DiskIn"] = t.struct(
        {
            "name": t.string().optional(),
            "sizeGb": t.integer().optional(),
            "sourceImage": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["DiskIn"])
    types["DiskOut"] = t.struct(
        {
            "name": t.string().optional(),
            "sizeGb": t.integer().optional(),
            "sourceImage": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiskOut"])
    types["ContainerStartedEventIn"] = t.struct(
        {
            "actionId": t.integer().optional(),
            "portMappings": t.struct({"_": t.string().optional()}).optional(),
            "ipAddress": t.string().optional(),
        }
    ).named(renames["ContainerStartedEventIn"])
    types["ContainerStartedEventOut"] = t.struct(
        {
            "actionId": t.integer().optional(),
            "portMappings": t.struct({"_": t.string().optional()}).optional(),
            "ipAddress": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContainerStartedEventOut"])
    types["LocationIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
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
            "accelerators": t.array(t.proxy(renames["AcceleratorIn"])).optional(),
            "volumes": t.array(t.proxy(renames["VolumeIn"])).optional(),
            "reservation": t.string().optional(),
            "disks": t.array(t.proxy(renames["DiskIn"])).optional(),
            "bootDiskSizeGb": t.integer().optional(),
            "network": t.proxy(renames["NetworkIn"]).optional(),
            "machineType": t.string(),
            "cpuPlatform": t.string().optional(),
            "nvidiaDriverVersion": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "bootImage": t.string().optional(),
            "preemptible": t.boolean().optional(),
            "enableStackdriverMonitoring": t.boolean().optional(),
            "dockerCacheImages": t.array(t.string()).optional(),
            "serviceAccount": t.proxy(renames["ServiceAccountIn"]).optional(),
        }
    ).named(renames["VirtualMachineIn"])
    types["VirtualMachineOut"] = t.struct(
        {
            "accelerators": t.array(t.proxy(renames["AcceleratorOut"])).optional(),
            "volumes": t.array(t.proxy(renames["VolumeOut"])).optional(),
            "reservation": t.string().optional(),
            "disks": t.array(t.proxy(renames["DiskOut"])).optional(),
            "bootDiskSizeGb": t.integer().optional(),
            "network": t.proxy(renames["NetworkOut"]).optional(),
            "machineType": t.string(),
            "cpuPlatform": t.string().optional(),
            "nvidiaDriverVersion": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "bootImage": t.string().optional(),
            "preemptible": t.boolean().optional(),
            "enableStackdriverMonitoring": t.boolean().optional(),
            "dockerCacheImages": t.array(t.string()).optional(),
            "serviceAccount": t.proxy(renames["ServiceAccountOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VirtualMachineOut"])
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
    types["NFSMountIn"] = t.struct({"target": t.string().optional()}).named(
        renames["NFSMountIn"]
    )
    types["NFSMountOut"] = t.struct(
        {
            "target": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NFSMountOut"])
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
    types["PullStartedEventIn"] = t.struct({"imageUri": t.string().optional()}).named(
        renames["PullStartedEventIn"]
    )
    types["PullStartedEventOut"] = t.struct(
        {
            "imageUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PullStartedEventOut"])

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
    functions["projectsLocationsOperationsCancel"] = lifesciences.get(
        "v2beta/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
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
