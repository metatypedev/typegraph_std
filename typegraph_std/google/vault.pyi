from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    HangoutsChatExportOptionsIn: t.typedef = ...
    HangoutsChatExportOptionsOut: t.typedef = ...
    HangoutsChatOptionsIn: t.typedef = ...
    HangoutsChatOptionsOut: t.typedef = ...
    HeldAccountIn: t.typedef = ...
    HeldAccountOut: t.typedef = ...
    HeldGroupsQueryIn: t.typedef = ...
    HeldGroupsQueryOut: t.typedef = ...
    CloseMatterResponseIn: t.typedef = ...
    CloseMatterResponseOut: t.typedef = ...
    CountArtifactsResponseIn: t.typedef = ...
    CountArtifactsResponseOut: t.typedef = ...
    VoiceOptionsIn: t.typedef = ...
    VoiceOptionsOut: t.typedef = ...
    CloudStorageFileIn: t.typedef = ...
    CloudStorageFileOut: t.typedef = ...
    HangoutsChatInfoIn: t.typedef = ...
    HangoutsChatInfoOut: t.typedef = ...
    OrgUnitInfoIn: t.typedef = ...
    OrgUnitInfoOut: t.typedef = ...
    UserInfoIn: t.typedef = ...
    UserInfoOut: t.typedef = ...
    SitesUrlInfoIn: t.typedef = ...
    SitesUrlInfoOut: t.typedef = ...
    DriveExportOptionsIn: t.typedef = ...
    DriveExportOptionsOut: t.typedef = ...
    ReopenMatterResponseIn: t.typedef = ...
    ReopenMatterResponseOut: t.typedef = ...
    ListExportsResponseIn: t.typedef = ...
    ListExportsResponseOut: t.typedef = ...
    RemoveMatterPermissionsRequestIn: t.typedef = ...
    RemoveMatterPermissionsRequestOut: t.typedef = ...
    GroupsCountResultIn: t.typedef = ...
    GroupsCountResultOut: t.typedef = ...
    HeldMailQueryIn: t.typedef = ...
    HeldMailQueryOut: t.typedef = ...
    AddHeldAccountsResponseIn: t.typedef = ...
    AddHeldAccountsResponseOut: t.typedef = ...
    ExportOptionsIn: t.typedef = ...
    ExportOptionsOut: t.typedef = ...
    UndeleteMatterRequestIn: t.typedef = ...
    UndeleteMatterRequestOut: t.typedef = ...
    GroupsExportOptionsIn: t.typedef = ...
    GroupsExportOptionsOut: t.typedef = ...
    HeldHangoutsChatQueryIn: t.typedef = ...
    HeldHangoutsChatQueryOut: t.typedef = ...
    ListMattersResponseIn: t.typedef = ...
    ListMattersResponseOut: t.typedef = ...
    ListHoldsResponseIn: t.typedef = ...
    ListHoldsResponseOut: t.typedef = ...
    ExportStatsIn: t.typedef = ...
    ExportStatsOut: t.typedef = ...
    AccountCountIn: t.typedef = ...
    AccountCountOut: t.typedef = ...
    QueryIn: t.typedef = ...
    QueryOut: t.typedef = ...
    ListHeldAccountsResponseIn: t.typedef = ...
    ListHeldAccountsResponseOut: t.typedef = ...
    MailOptionsIn: t.typedef = ...
    MailOptionsOut: t.typedef = ...
    CorpusQueryIn: t.typedef = ...
    CorpusQueryOut: t.typedef = ...
    MatterIn: t.typedef = ...
    MatterOut: t.typedef = ...
    HoldIn: t.typedef = ...
    HoldOut: t.typedef = ...
    CancelOperationRequestIn: t.typedef = ...
    CancelOperationRequestOut: t.typedef = ...
    MatterPermissionIn: t.typedef = ...
    MatterPermissionOut: t.typedef = ...
    AddHeldAccountsRequestIn: t.typedef = ...
    AddHeldAccountsRequestOut: t.typedef = ...
    CountArtifactsMetadataIn: t.typedef = ...
    CountArtifactsMetadataOut: t.typedef = ...
    CloudStorageSinkIn: t.typedef = ...
    CloudStorageSinkOut: t.typedef = ...
    SharedDriveInfoIn: t.typedef = ...
    SharedDriveInfoOut: t.typedef = ...
    ReopenMatterRequestIn: t.typedef = ...
    ReopenMatterRequestOut: t.typedef = ...
    HeldVoiceQueryIn: t.typedef = ...
    HeldVoiceQueryOut: t.typedef = ...
    RemoveHeldAccountsRequestIn: t.typedef = ...
    RemoveHeldAccountsRequestOut: t.typedef = ...
    MailCountResultIn: t.typedef = ...
    MailCountResultOut: t.typedef = ...
    VoiceExportOptionsIn: t.typedef = ...
    VoiceExportOptionsOut: t.typedef = ...
    AddMatterPermissionsRequestIn: t.typedef = ...
    AddMatterPermissionsRequestOut: t.typedef = ...
    CloseMatterRequestIn: t.typedef = ...
    CloseMatterRequestOut: t.typedef = ...
    ListSavedQueriesResponseIn: t.typedef = ...
    ListSavedQueriesResponseOut: t.typedef = ...
    DriveOptionsIn: t.typedef = ...
    DriveOptionsOut: t.typedef = ...
    ExportIn: t.typedef = ...
    ExportOut: t.typedef = ...
    ListOperationsResponseIn: t.typedef = ...
    ListOperationsResponseOut: t.typedef = ...
    AccountInfoIn: t.typedef = ...
    AccountInfoOut: t.typedef = ...
    TeamDriveInfoIn: t.typedef = ...
    TeamDriveInfoOut: t.typedef = ...
    AccountCountErrorIn: t.typedef = ...
    AccountCountErrorOut: t.typedef = ...
    SavedQueryIn: t.typedef = ...
    SavedQueryOut: t.typedef = ...
    MailExportOptionsIn: t.typedef = ...
    MailExportOptionsOut: t.typedef = ...
    HeldDriveQueryIn: t.typedef = ...
    HeldDriveQueryOut: t.typedef = ...
    OperationIn: t.typedef = ...
    OperationOut: t.typedef = ...
    StatusIn: t.typedef = ...
    StatusOut: t.typedef = ...
    EmptyIn: t.typedef = ...
    EmptyOut: t.typedef = ...
    HeldOrgUnitIn: t.typedef = ...
    HeldOrgUnitOut: t.typedef = ...
    RemoveHeldAccountsResponseIn: t.typedef = ...
    RemoveHeldAccountsResponseOut: t.typedef = ...
    CountArtifactsRequestIn: t.typedef = ...
    CountArtifactsRequestOut: t.typedef = ...
    AddHeldAccountResultIn: t.typedef = ...
    AddHeldAccountResultOut: t.typedef = ...

class FuncList:
    operationsGet: t.func = ...
    operationsDelete: t.func = ...
    operationsList: t.func = ...
    operationsCancel: t.func = ...
    mattersRemovePermissions: t.func = ...
    mattersList: t.func = ...
    mattersGet: t.func = ...
    mattersCount: t.func = ...
    mattersDelete: t.func = ...
    mattersUpdate: t.func = ...
    mattersAddPermissions: t.func = ...
    mattersClose: t.func = ...
    mattersCreate: t.func = ...
    mattersUndelete: t.func = ...
    mattersReopen: t.func = ...
    mattersSavedQueriesGet: t.func = ...
    mattersSavedQueriesCreate: t.func = ...
    mattersSavedQueriesDelete: t.func = ...
    mattersSavedQueriesList: t.func = ...
    mattersHoldsRemoveHeldAccounts: t.func = ...
    mattersHoldsList: t.func = ...
    mattersHoldsDelete: t.func = ...
    mattersHoldsCreate: t.func = ...
    mattersHoldsUpdate: t.func = ...
    mattersHoldsGet: t.func = ...
    mattersHoldsAddHeldAccounts: t.func = ...
    mattersHoldsAccountsList: t.func = ...
    mattersHoldsAccountsCreate: t.func = ...
    mattersHoldsAccountsDelete: t.func = ...
    mattersExportsCreate: t.func = ...
    mattersExportsGet: t.func = ...
    mattersExportsDelete: t.func = ...
    mattersExportsList: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_vault() -> Import: ...
