from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    ResumeTransferOperationRequestIn: t.typedef = ...
    ResumeTransferOperationRequestOut: t.typedef = ...
    TransferCountersIn: t.typedef = ...
    TransferCountersOut: t.typedef = ...
    TransferSpecIn: t.typedef = ...
    TransferSpecOut: t.typedef = ...
    ListAgentPoolsResponseIn: t.typedef = ...
    ListAgentPoolsResponseOut: t.typedef = ...
    AzureCredentialsIn: t.typedef = ...
    AzureCredentialsOut: t.typedef = ...
    DateIn: t.typedef = ...
    DateOut: t.typedef = ...
    StatusIn: t.typedef = ...
    StatusOut: t.typedef = ...
    PauseTransferOperationRequestIn: t.typedef = ...
    PauseTransferOperationRequestOut: t.typedef = ...
    TransferOptionsIn: t.typedef = ...
    TransferOptionsOut: t.typedef = ...
    ObjectConditionsIn: t.typedef = ...
    ObjectConditionsOut: t.typedef = ...
    PosixFilesystemIn: t.typedef = ...
    PosixFilesystemOut: t.typedef = ...
    GcsDataIn: t.typedef = ...
    GcsDataOut: t.typedef = ...
    AwsAccessKeyIn: t.typedef = ...
    AwsAccessKeyOut: t.typedef = ...
    RunTransferJobRequestIn: t.typedef = ...
    RunTransferJobRequestOut: t.typedef = ...
    AgentPoolIn: t.typedef = ...
    AgentPoolOut: t.typedef = ...
    EmptyIn: t.typedef = ...
    EmptyOut: t.typedef = ...
    GoogleServiceAccountIn: t.typedef = ...
    GoogleServiceAccountOut: t.typedef = ...
    AzureBlobStorageDataIn: t.typedef = ...
    AzureBlobStorageDataOut: t.typedef = ...
    TransferManifestIn: t.typedef = ...
    TransferManifestOut: t.typedef = ...
    ScheduleIn: t.typedef = ...
    ScheduleOut: t.typedef = ...
    AwsS3CompatibleDataIn: t.typedef = ...
    AwsS3CompatibleDataOut: t.typedef = ...
    ErrorSummaryIn: t.typedef = ...
    ErrorSummaryOut: t.typedef = ...
    TimeOfDayIn: t.typedef = ...
    TimeOfDayOut: t.typedef = ...
    ErrorLogEntryIn: t.typedef = ...
    ErrorLogEntryOut: t.typedef = ...
    HttpDataIn: t.typedef = ...
    HttpDataOut: t.typedef = ...
    BandwidthLimitIn: t.typedef = ...
    BandwidthLimitOut: t.typedef = ...
    OperationIn: t.typedef = ...
    OperationOut: t.typedef = ...
    MetadataOptionsIn: t.typedef = ...
    MetadataOptionsOut: t.typedef = ...
    S3CompatibleMetadataIn: t.typedef = ...
    S3CompatibleMetadataOut: t.typedef = ...
    EventStreamIn: t.typedef = ...
    EventStreamOut: t.typedef = ...
    TransferOperationIn: t.typedef = ...
    TransferOperationOut: t.typedef = ...
    NotificationConfigIn: t.typedef = ...
    NotificationConfigOut: t.typedef = ...
    ListTransferJobsResponseIn: t.typedef = ...
    ListTransferJobsResponseOut: t.typedef = ...
    CancelOperationRequestIn: t.typedef = ...
    CancelOperationRequestOut: t.typedef = ...
    TransferJobIn: t.typedef = ...
    TransferJobOut: t.typedef = ...
    AwsS3DataIn: t.typedef = ...
    AwsS3DataOut: t.typedef = ...
    ListOperationsResponseIn: t.typedef = ...
    ListOperationsResponseOut: t.typedef = ...
    LoggingConfigIn: t.typedef = ...
    LoggingConfigOut: t.typedef = ...
    UpdateTransferJobRequestIn: t.typedef = ...
    UpdateTransferJobRequestOut: t.typedef = ...

class FuncList:
    projectsAgentPoolsGet: t.func = ...
    projectsAgentPoolsPatch: t.func = ...
    projectsAgentPoolsList: t.func = ...
    projectsAgentPoolsDelete: t.func = ...
    projectsAgentPoolsCreate: t.func = ...
    transferOperationsGet: t.func = ...
    transferOperationsResume: t.func = ...
    transferOperationsPause: t.func = ...
    transferOperationsCancel: t.func = ...
    transferOperationsList: t.func = ...
    transferJobsList: t.func = ...
    transferJobsGet: t.func = ...
    transferJobsCreate: t.func = ...
    transferJobsPatch: t.func = ...
    transferJobsRun: t.func = ...
    transferJobsDelete: t.func = ...
    googleServiceAccountsGet: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_storagetransfer() -> Import: ...
