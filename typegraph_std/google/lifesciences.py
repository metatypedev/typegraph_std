from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_lifesciences() -> Import:
    lifesciences = HTTPRuntime("https://lifesciences.googleapis.com/")

    renames = {
        "ErrorResponse": "_lifesciences_1_ErrorResponse",
        "ListLocationsResponseIn": "_lifesciences_2_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_lifesciences_3_ListLocationsResponseOut",
        "RunPipelineResponseIn": "_lifesciences_4_RunPipelineResponseIn",
        "RunPipelineResponseOut": "_lifesciences_5_RunPipelineResponseOut",
        "EmptyIn": "_lifesciences_6_EmptyIn",
        "EmptyOut": "_lifesciences_7_EmptyOut",
        "ServiceAccountIn": "_lifesciences_8_ServiceAccountIn",
        "ServiceAccountOut": "_lifesciences_9_ServiceAccountOut",
        "AcceleratorIn": "_lifesciences_10_AcceleratorIn",
        "AcceleratorOut": "_lifesciences_11_AcceleratorOut",
        "WorkerReleasedEventIn": "_lifesciences_12_WorkerReleasedEventIn",
        "WorkerReleasedEventOut": "_lifesciences_13_WorkerReleasedEventOut",
        "UnexpectedExitStatusEventIn": "_lifesciences_14_UnexpectedExitStatusEventIn",
        "UnexpectedExitStatusEventOut": "_lifesciences_15_UnexpectedExitStatusEventOut",
        "FailedEventIn": "_lifesciences_16_FailedEventIn",
        "FailedEventOut": "_lifesciences_17_FailedEventOut",
        "ContainerKilledEventIn": "_lifesciences_18_ContainerKilledEventIn",
        "ContainerKilledEventOut": "_lifesciences_19_ContainerKilledEventOut",
        "NetworkIn": "_lifesciences_20_NetworkIn",
        "NetworkOut": "_lifesciences_21_NetworkOut",
        "EventIn": "_lifesciences_22_EventIn",
        "EventOut": "_lifesciences_23_EventOut",
        "OperationIn": "_lifesciences_24_OperationIn",
        "OperationOut": "_lifesciences_25_OperationOut",
        "PullStoppedEventIn": "_lifesciences_26_PullStoppedEventIn",
        "PullStoppedEventOut": "_lifesciences_27_PullStoppedEventOut",
        "SecretIn": "_lifesciences_28_SecretIn",
        "SecretOut": "_lifesciences_29_SecretOut",
        "MountIn": "_lifesciences_30_MountIn",
        "MountOut": "_lifesciences_31_MountOut",
        "CancelOperationRequestIn": "_lifesciences_32_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_lifesciences_33_CancelOperationRequestOut",
        "RunPipelineRequestIn": "_lifesciences_34_RunPipelineRequestIn",
        "RunPipelineRequestOut": "_lifesciences_35_RunPipelineRequestOut",
        "VirtualMachineIn": "_lifesciences_36_VirtualMachineIn",
        "VirtualMachineOut": "_lifesciences_37_VirtualMachineOut",
        "ListOperationsResponseIn": "_lifesciences_38_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_lifesciences_39_ListOperationsResponseOut",
        "PersistentDiskIn": "_lifesciences_40_PersistentDiskIn",
        "PersistentDiskOut": "_lifesciences_41_PersistentDiskOut",
        "MetadataIn": "_lifesciences_42_MetadataIn",
        "MetadataOut": "_lifesciences_43_MetadataOut",
        "ActionIn": "_lifesciences_44_ActionIn",
        "ActionOut": "_lifesciences_45_ActionOut",
        "LocationIn": "_lifesciences_46_LocationIn",
        "LocationOut": "_lifesciences_47_LocationOut",
        "ExistingDiskIn": "_lifesciences_48_ExistingDiskIn",
        "ExistingDiskOut": "_lifesciences_49_ExistingDiskOut",
        "VolumeIn": "_lifesciences_50_VolumeIn",
        "VolumeOut": "_lifesciences_51_VolumeOut",
        "StatusIn": "_lifesciences_52_StatusIn",
        "StatusOut": "_lifesciences_53_StatusOut",
        "ContainerStartedEventIn": "_lifesciences_54_ContainerStartedEventIn",
        "ContainerStartedEventOut": "_lifesciences_55_ContainerStartedEventOut",
        "ResourcesIn": "_lifesciences_56_ResourcesIn",
        "ResourcesOut": "_lifesciences_57_ResourcesOut",
        "PullStartedEventIn": "_lifesciences_58_PullStartedEventIn",
        "PullStartedEventOut": "_lifesciences_59_PullStartedEventOut",
        "DelayedEventIn": "_lifesciences_60_DelayedEventIn",
        "DelayedEventOut": "_lifesciences_61_DelayedEventOut",
        "WorkerAssignedEventIn": "_lifesciences_62_WorkerAssignedEventIn",
        "WorkerAssignedEventOut": "_lifesciences_63_WorkerAssignedEventOut",
        "DiskIn": "_lifesciences_64_DiskIn",
        "DiskOut": "_lifesciences_65_DiskOut",
        "ContainerStoppedEventIn": "_lifesciences_66_ContainerStoppedEventIn",
        "ContainerStoppedEventOut": "_lifesciences_67_ContainerStoppedEventOut",
        "NFSMountIn": "_lifesciences_68_NFSMountIn",
        "NFSMountOut": "_lifesciences_69_NFSMountOut",
        "PipelineIn": "_lifesciences_70_PipelineIn",
        "PipelineOut": "_lifesciences_71_PipelineOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["RunPipelineResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RunPipelineResponseIn"]
    )
    types["RunPipelineResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RunPipelineResponseOut"])
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
    types["WorkerReleasedEventIn"] = t.struct(
        {"zone": t.string().optional(), "instance": t.string().optional()}
    ).named(renames["WorkerReleasedEventIn"])
    types["WorkerReleasedEventOut"] = t.struct(
        {
            "zone": t.string().optional(),
            "instance": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkerReleasedEventOut"])
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
    types["ContainerKilledEventIn"] = t.struct(
        {"actionId": t.integer().optional()}
    ).named(renames["ContainerKilledEventIn"])
    types["ContainerKilledEventOut"] = t.struct(
        {
            "actionId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContainerKilledEventOut"])
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
    types["EventIn"] = t.struct(
        {
            "containerStopped": t.proxy(renames["ContainerStoppedEventIn"]).optional(),
            "workerReleased": t.proxy(renames["WorkerReleasedEventIn"]).optional(),
            "timestamp": t.string().optional(),
            "pullStarted": t.proxy(renames["PullStartedEventIn"]).optional(),
            "delayed": t.proxy(renames["DelayedEventIn"]).optional(),
            "containerStarted": t.proxy(renames["ContainerStartedEventIn"]).optional(),
            "containerKilled": t.proxy(renames["ContainerKilledEventIn"]).optional(),
            "workerAssigned": t.proxy(renames["WorkerAssignedEventIn"]).optional(),
            "failed": t.proxy(renames["FailedEventIn"]).optional(),
            "unexpectedExitStatus": t.proxy(
                renames["UnexpectedExitStatusEventIn"]
            ).optional(),
            "pullStopped": t.proxy(renames["PullStoppedEventIn"]).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["EventIn"])
    types["EventOut"] = t.struct(
        {
            "containerStopped": t.proxy(renames["ContainerStoppedEventOut"]).optional(),
            "workerReleased": t.proxy(renames["WorkerReleasedEventOut"]).optional(),
            "timestamp": t.string().optional(),
            "pullStarted": t.proxy(renames["PullStartedEventOut"]).optional(),
            "delayed": t.proxy(renames["DelayedEventOut"]).optional(),
            "containerStarted": t.proxy(renames["ContainerStartedEventOut"]).optional(),
            "containerKilled": t.proxy(renames["ContainerKilledEventOut"]).optional(),
            "workerAssigned": t.proxy(renames["WorkerAssignedEventOut"]).optional(),
            "failed": t.proxy(renames["FailedEventOut"]).optional(),
            "unexpectedExitStatus": t.proxy(
                renames["UnexpectedExitStatusEventOut"]
            ).optional(),
            "pullStopped": t.proxy(renames["PullStoppedEventOut"]).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventOut"])
    types["OperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["PullStoppedEventIn"] = t.struct({"imageUri": t.string().optional()}).named(
        renames["PullStoppedEventIn"]
    )
    types["PullStoppedEventOut"] = t.struct(
        {
            "imageUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PullStoppedEventOut"])
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
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["RunPipelineRequestIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "pubSubTopic": t.string().optional(),
            "pipeline": t.proxy(renames["PipelineIn"]),
        }
    ).named(renames["RunPipelineRequestIn"])
    types["RunPipelineRequestOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "pubSubTopic": t.string().optional(),
            "pipeline": t.proxy(renames["PipelineOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunPipelineRequestOut"])
    types["VirtualMachineIn"] = t.struct(
        {
            "bootImage": t.string().optional(),
            "nvidiaDriverVersion": t.string().optional(),
            "reservation": t.string().optional(),
            "volumes": t.array(t.proxy(renames["VolumeIn"])).optional(),
            "preemptible": t.boolean().optional(),
            "machineType": t.string(),
            "accelerators": t.array(t.proxy(renames["AcceleratorIn"])).optional(),
            "dockerCacheImages": t.array(t.string()).optional(),
            "network": t.proxy(renames["NetworkIn"]).optional(),
            "enableStackdriverMonitoring": t.boolean().optional(),
            "disks": t.array(t.proxy(renames["DiskIn"])).optional(),
            "bootDiskSizeGb": t.integer().optional(),
            "serviceAccount": t.proxy(renames["ServiceAccountIn"]).optional(),
            "cpuPlatform": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["VirtualMachineIn"])
    types["VirtualMachineOut"] = t.struct(
        {
            "bootImage": t.string().optional(),
            "nvidiaDriverVersion": t.string().optional(),
            "reservation": t.string().optional(),
            "volumes": t.array(t.proxy(renames["VolumeOut"])).optional(),
            "preemptible": t.boolean().optional(),
            "machineType": t.string(),
            "accelerators": t.array(t.proxy(renames["AcceleratorOut"])).optional(),
            "dockerCacheImages": t.array(t.string()).optional(),
            "network": t.proxy(renames["NetworkOut"]).optional(),
            "enableStackdriverMonitoring": t.boolean().optional(),
            "disks": t.array(t.proxy(renames["DiskOut"])).optional(),
            "bootDiskSizeGb": t.integer().optional(),
            "serviceAccount": t.proxy(renames["ServiceAccountOut"]).optional(),
            "cpuPlatform": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VirtualMachineOut"])
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
    types["MetadataIn"] = t.struct(
        {
            "events": t.array(t.proxy(renames["EventIn"])).optional(),
            "startTime": t.string().optional(),
            "pipeline": t.proxy(renames["PipelineIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "pubSubTopic": t.string().optional(),
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["MetadataIn"])
    types["MetadataOut"] = t.struct(
        {
            "events": t.array(t.proxy(renames["EventOut"])).optional(),
            "startTime": t.string().optional(),
            "pipeline": t.proxy(renames["PipelineOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "pubSubTopic": t.string().optional(),
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetadataOut"])
    types["ActionIn"] = t.struct(
        {
            "encryptedEnvironment": t.proxy(renames["SecretIn"]).optional(),
            "credentials": t.proxy(renames["SecretIn"]).optional(),
            "disableStandardErrorCapture": t.boolean().optional(),
            "containerName": t.string().optional(),
            "enableFuse": t.boolean().optional(),
            "ignoreExitStatus": t.boolean().optional(),
            "portMappings": t.struct({"_": t.string().optional()}).optional(),
            "runInBackground": t.boolean().optional(),
            "timeout": t.string().optional(),
            "imageUri": t.string(),
            "pidNamespace": t.string().optional(),
            "entrypoint": t.string().optional(),
            "commands": t.array(t.string()).optional(),
            "disableImagePrefetch": t.boolean().optional(),
            "mounts": t.array(t.proxy(renames["MountIn"])).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "alwaysRun": t.boolean().optional(),
            "blockExternalNetwork": t.boolean().optional(),
            "publishExposedPorts": t.boolean().optional(),
            "environment": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ActionIn"])
    types["ActionOut"] = t.struct(
        {
            "encryptedEnvironment": t.proxy(renames["SecretOut"]).optional(),
            "credentials": t.proxy(renames["SecretOut"]).optional(),
            "disableStandardErrorCapture": t.boolean().optional(),
            "containerName": t.string().optional(),
            "enableFuse": t.boolean().optional(),
            "ignoreExitStatus": t.boolean().optional(),
            "portMappings": t.struct({"_": t.string().optional()}).optional(),
            "runInBackground": t.boolean().optional(),
            "timeout": t.string().optional(),
            "imageUri": t.string(),
            "pidNamespace": t.string().optional(),
            "entrypoint": t.string().optional(),
            "commands": t.array(t.string()).optional(),
            "disableImagePrefetch": t.boolean().optional(),
            "mounts": t.array(t.proxy(renames["MountOut"])).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "alwaysRun": t.boolean().optional(),
            "blockExternalNetwork": t.boolean().optional(),
            "publishExposedPorts": t.boolean().optional(),
            "environment": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActionOut"])
    types["LocationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["ExistingDiskIn"] = t.struct({"disk": t.string().optional()}).named(
        renames["ExistingDiskIn"]
    )
    types["ExistingDiskOut"] = t.struct(
        {
            "disk": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExistingDiskOut"])
    types["VolumeIn"] = t.struct(
        {
            "existingDisk": t.proxy(renames["ExistingDiskIn"]).optional(),
            "volume": t.string().optional(),
            "persistentDisk": t.proxy(renames["PersistentDiskIn"]).optional(),
            "nfsMount": t.proxy(renames["NFSMountIn"]).optional(),
        }
    ).named(renames["VolumeIn"])
    types["VolumeOut"] = t.struct(
        {
            "existingDisk": t.proxy(renames["ExistingDiskOut"]).optional(),
            "volume": t.string().optional(),
            "persistentDisk": t.proxy(renames["PersistentDiskOut"]).optional(),
            "nfsMount": t.proxy(renames["NFSMountOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VolumeOut"])
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
    types["ContainerStartedEventIn"] = t.struct(
        {
            "ipAddress": t.string().optional(),
            "actionId": t.integer().optional(),
            "portMappings": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ContainerStartedEventIn"])
    types["ContainerStartedEventOut"] = t.struct(
        {
            "ipAddress": t.string().optional(),
            "actionId": t.integer().optional(),
            "portMappings": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContainerStartedEventOut"])
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
    types["PullStartedEventIn"] = t.struct({"imageUri": t.string().optional()}).named(
        renames["PullStartedEventIn"]
    )
    types["PullStartedEventOut"] = t.struct(
        {
            "imageUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PullStartedEventOut"])
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
    types["DiskIn"] = t.struct(
        {
            "sizeGb": t.integer().optional(),
            "sourceImage": t.string().optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["DiskIn"])
    types["DiskOut"] = t.struct(
        {
            "sizeGb": t.integer().optional(),
            "sourceImage": t.string().optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiskOut"])
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
    types["NFSMountIn"] = t.struct({"target": t.string().optional()}).named(
        renames["NFSMountIn"]
    )
    types["NFSMountOut"] = t.struct(
        {
            "target": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NFSMountOut"])
    types["PipelineIn"] = t.struct(
        {
            "actions": t.array(t.proxy(renames["ActionIn"])).optional(),
            "encryptedEnvironment": t.proxy(renames["SecretIn"]).optional(),
            "environment": t.struct({"_": t.string().optional()}).optional(),
            "resources": t.proxy(renames["ResourcesIn"]).optional(),
            "timeout": t.string().optional(),
        }
    ).named(renames["PipelineIn"])
    types["PipelineOut"] = t.struct(
        {
            "actions": t.array(t.proxy(renames["ActionOut"])).optional(),
            "encryptedEnvironment": t.proxy(renames["SecretOut"]).optional(),
            "environment": t.struct({"_": t.string().optional()}).optional(),
            "resources": t.proxy(renames["ResourcesOut"]).optional(),
            "timeout": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PipelineOut"])

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
    functions["projectsLocationsOperationsCancel"] = lifesciences.get(
        "v2beta/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = lifesciences.get(
        "v2beta/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = lifesciences.get(
        "v2beta/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPipelinesRun"] = lifesciences.post(
        "v2beta/{parent}/pipelines:run",
        t.struct(
            {
                "parent": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "pubSubTopic": t.string().optional(),
                "pipeline": t.proxy(renames["PipelineIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="lifesciences",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
