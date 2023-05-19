from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    HttpDataIn: t.typedef = ...
    HttpDataOut: t.typedef = ...
    TimeOfDayIn: t.typedef = ...
    TimeOfDayOut: t.typedef = ...
    TransferOperationIn: t.typedef = ...
    TransferOperationOut: t.typedef = ...
    CancelOperationRequestIn: t.typedef = ...
    CancelOperationRequestOut: t.typedef = ...
    AwsAccessKeyIn: t.typedef = ...
    AwsAccessKeyOut: t.typedef = ...
    AzureBlobStorageDataIn: t.typedef = ...
    AzureBlobStorageDataOut: t.typedef = ...
    S3CompatibleMetadataIn: t.typedef = ...
    S3CompatibleMetadataOut: t.typedef = ...
    TransferJobIn: t.typedef = ...
    TransferJobOut: t.typedef = ...
    ObjectConditionsIn: t.typedef = ...
    ObjectConditionsOut: t.typedef = ...
    AgentPoolIn: t.typedef = ...
    AgentPoolOut: t.typedef = ...
    RunTransferJobRequestIn: t.typedef = ...
    RunTransferJobRequestOut: t.typedef = ...
    ErrorLogEntryIn: t.typedef = ...
    ErrorLogEntryOut: t.typedef = ...
    NotificationConfigIn: t.typedef = ...
    NotificationConfigOut: t.typedef = ...
    ErrorSummaryIn: t.typedef = ...
    ErrorSummaryOut: t.typedef = ...
    GcsDataIn: t.typedef = ...
    GcsDataOut: t.typedef = ...
    PosixFilesystemIn: t.typedef = ...
    PosixFilesystemOut: t.typedef = ...
    ListAgentPoolsResponseIn: t.typedef = ...
    ListAgentPoolsResponseOut: t.typedef = ...
    MetadataOptionsIn: t.typedef = ...
    MetadataOptionsOut: t.typedef = ...
    ListTransferJobsResponseIn: t.typedef = ...
    ListTransferJobsResponseOut: t.typedef = ...
    EventStreamIn: t.typedef = ...
    EventStreamOut: t.typedef = ...
    ListOperationsResponseIn: t.typedef = ...
    ListOperationsResponseOut: t.typedef = ...
    GoogleServiceAccountIn: t.typedef = ...
    GoogleServiceAccountOut: t.typedef = ...
    StatusIn: t.typedef = ...
    StatusOut: t.typedef = ...
    TransferManifestIn: t.typedef = ...
    TransferManifestOut: t.typedef = ...
    DateIn: t.typedef = ...
    DateOut: t.typedef = ...
    AwsS3CompatibleDataIn: t.typedef = ...
    AwsS3CompatibleDataOut: t.typedef = ...
    AwsS3DataIn: t.typedef = ...
    AwsS3DataOut: t.typedef = ...
    TransferSpecIn: t.typedef = ...
    TransferSpecOut: t.typedef = ...
    LoggingConfigIn: t.typedef = ...
    LoggingConfigOut: t.typedef = ...
    UpdateTransferJobRequestIn: t.typedef = ...
    UpdateTransferJobRequestOut: t.typedef = ...
    ScheduleIn: t.typedef = ...
    ScheduleOut: t.typedef = ...
    BandwidthLimitIn: t.typedef = ...
    BandwidthLimitOut: t.typedef = ...
    EmptyIn: t.typedef = ...
    EmptyOut: t.typedef = ...
    TransferCountersIn: t.typedef = ...
    TransferCountersOut: t.typedef = ...
    AzureCredentialsIn: t.typedef = ...
    AzureCredentialsOut: t.typedef = ...
    PauseTransferOperationRequestIn: t.typedef = ...
    PauseTransferOperationRequestOut: t.typedef = ...
    OperationIn: t.typedef = ...
    OperationOut: t.typedef = ...
    ResumeTransferOperationRequestIn: t.typedef = ...
    ResumeTransferOperationRequestOut: t.typedef = ...
    TransferOptionsIn: t.typedef = ...
    TransferOptionsOut: t.typedef = ...

class FuncList:
    transferJobsDelete: t.func = ...
    transferJobsCreate: t.func = ...
    transferJobsList: t.func = ...
    transferJobsGet: t.func = ...
    transferJobsPatch: t.func = ...
    transferJobsRun: t.func = ...
    projectsAgentPoolsDelete: t.func = ...
    projectsAgentPoolsPatch: t.func = ...
    projectsAgentPoolsList: t.func = ...
    projectsAgentPoolsGet: t.func = ...
    projectsAgentPoolsCreate: t.func = ...
    transferOperationsGet: t.func = ...
    transferOperationsList: t.func = ...
    transferOperationsPause: t.func = ...
    transferOperationsCancel: t.func = ...
    transferOperationsResume: t.func = ...
    googleServiceAccountsGet: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_storagetransfer() -> Import: ...