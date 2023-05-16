from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    PullStoppedEventIn: t.typedef = ...
    PullStoppedEventOut: t.typedef = ...
    RunPipelineResponseIn: t.typedef = ...
    RunPipelineResponseOut: t.typedef = ...
    RunPipelineRequestIn: t.typedef = ...
    RunPipelineRequestOut: t.typedef = ...
    PersistentDiskIn: t.typedef = ...
    PersistentDiskOut: t.typedef = ...
    PullStartedEventIn: t.typedef = ...
    PullStartedEventOut: t.typedef = ...
    WorkerAssignedEventIn: t.typedef = ...
    WorkerAssignedEventOut: t.typedef = ...
    EventIn: t.typedef = ...
    EventOut: t.typedef = ...
    SecretIn: t.typedef = ...
    SecretOut: t.typedef = ...
    ActionIn: t.typedef = ...
    ActionOut: t.typedef = ...
    DelayedEventIn: t.typedef = ...
    DelayedEventOut: t.typedef = ...
    CheckInResponseIn: t.typedef = ...
    CheckInResponseOut: t.typedef = ...
    CheckInRequestIn: t.typedef = ...
    CheckInRequestOut: t.typedef = ...
    ResourcesIn: t.typedef = ...
    ResourcesOut: t.typedef = ...
    ContainerKilledEventIn: t.typedef = ...
    ContainerKilledEventOut: t.typedef = ...
    EmptyIn: t.typedef = ...
    EmptyOut: t.typedef = ...
    DiskStatusIn: t.typedef = ...
    DiskStatusOut: t.typedef = ...
    WorkerReleasedEventIn: t.typedef = ...
    WorkerReleasedEventOut: t.typedef = ...
    ExistingDiskIn: t.typedef = ...
    ExistingDiskOut: t.typedef = ...
    NetworkIn: t.typedef = ...
    NetworkOut: t.typedef = ...
    CancelOperationRequestIn: t.typedef = ...
    CancelOperationRequestOut: t.typedef = ...
    DiskIn: t.typedef = ...
    DiskOut: t.typedef = ...
    NFSMountIn: t.typedef = ...
    NFSMountOut: t.typedef = ...
    VolumeIn: t.typedef = ...
    VolumeOut: t.typedef = ...
    WorkerStatusIn: t.typedef = ...
    WorkerStatusOut: t.typedef = ...
    FailedEventIn: t.typedef = ...
    FailedEventOut: t.typedef = ...
    VirtualMachineIn: t.typedef = ...
    VirtualMachineOut: t.typedef = ...
    OperationIn: t.typedef = ...
    OperationOut: t.typedef = ...
    ContainerStartedEventIn: t.typedef = ...
    ContainerStartedEventOut: t.typedef = ...
    ServiceAccountIn: t.typedef = ...
    ServiceAccountOut: t.typedef = ...
    ContainerStoppedEventIn: t.typedef = ...
    ContainerStoppedEventOut: t.typedef = ...
    TimestampedEventIn: t.typedef = ...
    TimestampedEventOut: t.typedef = ...
    AcceleratorIn: t.typedef = ...
    AcceleratorOut: t.typedef = ...
    MountIn: t.typedef = ...
    MountOut: t.typedef = ...
    UnexpectedExitStatusEventIn: t.typedef = ...
    UnexpectedExitStatusEventOut: t.typedef = ...
    StatusIn: t.typedef = ...
    StatusOut: t.typedef = ...
    PipelineIn: t.typedef = ...
    PipelineOut: t.typedef = ...
    ListOperationsResponseIn: t.typedef = ...
    ListOperationsResponseOut: t.typedef = ...
    MetadataIn: t.typedef = ...
    MetadataOut: t.typedef = ...

class FuncList:
    workersCheckIn: t.func = ...
    pipelinesRun: t.func = ...
    projectsWorkersCheckIn: t.func = ...
    projectsOperationsGet: t.func = ...
    projectsOperationsCancel: t.func = ...
    projectsOperationsList: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_genomics() -> Import: ...
