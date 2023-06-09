from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    FailedEventIn: t.typedef = ...
    FailedEventOut: t.typedef = ...
    PersistentDiskIn: t.typedef = ...
    PersistentDiskOut: t.typedef = ...
    CancelOperationRequestIn: t.typedef = ...
    CancelOperationRequestOut: t.typedef = ...
    ContainerKilledEventIn: t.typedef = ...
    ContainerKilledEventOut: t.typedef = ...
    SecretIn: t.typedef = ...
    SecretOut: t.typedef = ...
    EventIn: t.typedef = ...
    EventOut: t.typedef = ...
    RunPipelineResponseIn: t.typedef = ...
    RunPipelineResponseOut: t.typedef = ...
    RunPipelineRequestIn: t.typedef = ...
    RunPipelineRequestOut: t.typedef = ...
    MetadataIn: t.typedef = ...
    MetadataOut: t.typedef = ...
    WorkerAssignedEventIn: t.typedef = ...
    WorkerAssignedEventOut: t.typedef = ...
    ListOperationsResponseIn: t.typedef = ...
    ListOperationsResponseOut: t.typedef = ...
    NetworkIn: t.typedef = ...
    NetworkOut: t.typedef = ...
    ContainerStartedEventIn: t.typedef = ...
    ContainerStartedEventOut: t.typedef = ...
    StatusIn: t.typedef = ...
    StatusOut: t.typedef = ...
    PullStoppedEventIn: t.typedef = ...
    PullStoppedEventOut: t.typedef = ...
    ExistingDiskIn: t.typedef = ...
    ExistingDiskOut: t.typedef = ...
    PipelineIn: t.typedef = ...
    PipelineOut: t.typedef = ...
    MountIn: t.typedef = ...
    MountOut: t.typedef = ...
    LocationIn: t.typedef = ...
    LocationOut: t.typedef = ...
    OperationIn: t.typedef = ...
    OperationOut: t.typedef = ...
    NFSMountIn: t.typedef = ...
    NFSMountOut: t.typedef = ...
    ServiceAccountIn: t.typedef = ...
    ServiceAccountOut: t.typedef = ...
    DelayedEventIn: t.typedef = ...
    DelayedEventOut: t.typedef = ...
    ContainerStoppedEventIn: t.typedef = ...
    ContainerStoppedEventOut: t.typedef = ...
    AcceleratorIn: t.typedef = ...
    AcceleratorOut: t.typedef = ...
    EmptyIn: t.typedef = ...
    EmptyOut: t.typedef = ...
    PullStartedEventIn: t.typedef = ...
    PullStartedEventOut: t.typedef = ...
    ListLocationsResponseIn: t.typedef = ...
    ListLocationsResponseOut: t.typedef = ...
    VolumeIn: t.typedef = ...
    VolumeOut: t.typedef = ...
    VirtualMachineIn: t.typedef = ...
    VirtualMachineOut: t.typedef = ...
    ActionIn: t.typedef = ...
    ActionOut: t.typedef = ...
    ResourcesIn: t.typedef = ...
    ResourcesOut: t.typedef = ...
    UnexpectedExitStatusEventIn: t.typedef = ...
    UnexpectedExitStatusEventOut: t.typedef = ...
    DiskIn: t.typedef = ...
    DiskOut: t.typedef = ...
    WorkerReleasedEventIn: t.typedef = ...
    WorkerReleasedEventOut: t.typedef = ...

class FuncList:
    projectsLocationsList: t.func = ...
    projectsLocationsGet: t.func = ...
    projectsLocationsPipelinesRun: t.func = ...
    projectsLocationsOperationsCancel: t.func = ...
    projectsLocationsOperationsGet: t.func = ...
    projectsLocationsOperationsList: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_lifesciences() -> Import: ...
