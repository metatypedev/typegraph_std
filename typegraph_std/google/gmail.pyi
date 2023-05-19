from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    ModifyThreadRequestIn: t.typedef = ...
    ModifyThreadRequestOut: t.typedef = ...
    ListDelegatesResponseIn: t.typedef = ...
    ListDelegatesResponseOut: t.typedef = ...
    DisableCseKeyPairRequestIn: t.typedef = ...
    DisableCseKeyPairRequestOut: t.typedef = ...
    BatchDeleteMessagesRequestIn: t.typedef = ...
    BatchDeleteMessagesRequestOut: t.typedef = ...
    MessageIn: t.typedef = ...
    MessageOut: t.typedef = ...
    VacationSettingsIn: t.typedef = ...
    VacationSettingsOut: t.typedef = ...
    FilterIn: t.typedef = ...
    FilterOut: t.typedef = ...
    ListThreadsResponseIn: t.typedef = ...
    ListThreadsResponseOut: t.typedef = ...
    LabelIn: t.typedef = ...
    LabelOut: t.typedef = ...
    ListLabelsResponseIn: t.typedef = ...
    ListLabelsResponseOut: t.typedef = ...
    ForwardingAddressIn: t.typedef = ...
    ForwardingAddressOut: t.typedef = ...
    WatchResponseIn: t.typedef = ...
    WatchResponseOut: t.typedef = ...
    BatchModifyMessagesRequestIn: t.typedef = ...
    BatchModifyMessagesRequestOut: t.typedef = ...
    LanguageSettingsIn: t.typedef = ...
    LanguageSettingsOut: t.typedef = ...
    EnableCseKeyPairRequestIn: t.typedef = ...
    EnableCseKeyPairRequestOut: t.typedef = ...
    SmtpMsaIn: t.typedef = ...
    SmtpMsaOut: t.typedef = ...
    HistoryMessageAddedIn: t.typedef = ...
    HistoryMessageAddedOut: t.typedef = ...
    WatchRequestIn: t.typedef = ...
    WatchRequestOut: t.typedef = ...
    MessagePartBodyIn: t.typedef = ...
    MessagePartBodyOut: t.typedef = ...
    CseIdentityIn: t.typedef = ...
    CseIdentityOut: t.typedef = ...
    MessagePartIn: t.typedef = ...
    MessagePartOut: t.typedef = ...
    ListDraftsResponseIn: t.typedef = ...
    ListDraftsResponseOut: t.typedef = ...
    ListCseKeyPairsResponseIn: t.typedef = ...
    ListCseKeyPairsResponseOut: t.typedef = ...
    ListCseIdentitiesResponseIn: t.typedef = ...
    ListCseIdentitiesResponseOut: t.typedef = ...
    DelegateIn: t.typedef = ...
    DelegateOut: t.typedef = ...
    AutoForwardingIn: t.typedef = ...
    AutoForwardingOut: t.typedef = ...
    HistoryLabelRemovedIn: t.typedef = ...
    HistoryLabelRemovedOut: t.typedef = ...
    MessagePartHeaderIn: t.typedef = ...
    MessagePartHeaderOut: t.typedef = ...
    ListFiltersResponseIn: t.typedef = ...
    ListFiltersResponseOut: t.typedef = ...
    ThreadIn: t.typedef = ...
    ThreadOut: t.typedef = ...
    ModifyMessageRequestIn: t.typedef = ...
    ModifyMessageRequestOut: t.typedef = ...
    KaclsKeyMetadataIn: t.typedef = ...
    KaclsKeyMetadataOut: t.typedef = ...
    ListForwardingAddressesResponseIn: t.typedef = ...
    ListForwardingAddressesResponseOut: t.typedef = ...
    ListSendAsResponseIn: t.typedef = ...
    ListSendAsResponseOut: t.typedef = ...
    CsePrivateKeyMetadataIn: t.typedef = ...
    CsePrivateKeyMetadataOut: t.typedef = ...
    ProfileIn: t.typedef = ...
    ProfileOut: t.typedef = ...
    LabelColorIn: t.typedef = ...
    LabelColorOut: t.typedef = ...
    ListMessagesResponseIn: t.typedef = ...
    ListMessagesResponseOut: t.typedef = ...
    FilterCriteriaIn: t.typedef = ...
    FilterCriteriaOut: t.typedef = ...
    FilterActionIn: t.typedef = ...
    FilterActionOut: t.typedef = ...
    ObliterateCseKeyPairRequestIn: t.typedef = ...
    ObliterateCseKeyPairRequestOut: t.typedef = ...
    SmimeInfoIn: t.typedef = ...
    SmimeInfoOut: t.typedef = ...
    HistoryLabelAddedIn: t.typedef = ...
    HistoryLabelAddedOut: t.typedef = ...
    HistoryMessageDeletedIn: t.typedef = ...
    HistoryMessageDeletedOut: t.typedef = ...
    SendAsIn: t.typedef = ...
    SendAsOut: t.typedef = ...
    CseKeyPairIn: t.typedef = ...
    CseKeyPairOut: t.typedef = ...
    DraftIn: t.typedef = ...
    DraftOut: t.typedef = ...
    HistoryIn: t.typedef = ...
    HistoryOut: t.typedef = ...
    PopSettingsIn: t.typedef = ...
    PopSettingsOut: t.typedef = ...
    ListSmimeInfoResponseIn: t.typedef = ...
    ListSmimeInfoResponseOut: t.typedef = ...
    ImapSettingsIn: t.typedef = ...
    ImapSettingsOut: t.typedef = ...
    ListHistoryResponseIn: t.typedef = ...
    ListHistoryResponseOut: t.typedef = ...

class FuncList:
    usersGetProfile: t.func = ...
    usersStop: t.func = ...
    usersWatch: t.func = ...
    usersDraftsDelete: t.func = ...
    usersDraftsCreate: t.func = ...
    usersDraftsGet: t.func = ...
    usersDraftsSend: t.func = ...
    usersDraftsList: t.func = ...
    usersDraftsUpdate: t.func = ...
    usersThreadsList: t.func = ...
    usersThreadsDelete: t.func = ...
    usersThreadsTrash: t.func = ...
    usersThreadsGet: t.func = ...
    usersThreadsModify: t.func = ...
    usersThreadsUntrash: t.func = ...
    usersMessagesBatchDelete: t.func = ...
    usersMessagesTrash: t.func = ...
    usersMessagesInsert: t.func = ...
    usersMessagesDelete: t.func = ...
    usersMessagesList: t.func = ...
    usersMessagesModify: t.func = ...
    usersMessagesImport: t.func = ...
    usersMessagesUntrash: t.func = ...
    usersMessagesBatchModify: t.func = ...
    usersMessagesGet: t.func = ...
    usersMessagesSend: t.func = ...
    usersMessagesAttachmentsGet: t.func = ...
    usersLabelsCreate: t.func = ...
    usersLabelsPatch: t.func = ...
    usersLabelsDelete: t.func = ...
    usersLabelsGet: t.func = ...
    usersLabelsList: t.func = ...
    usersLabelsUpdate: t.func = ...
    usersSettingsUpdatePop: t.func = ...
    usersSettingsUpdateImap: t.func = ...
    usersSettingsGetPop: t.func = ...
    usersSettingsUpdateLanguage: t.func = ...
    usersSettingsGetVacation: t.func = ...
    usersSettingsUpdateVacation: t.func = ...
    usersSettingsGetLanguage: t.func = ...
    usersSettingsUpdateAutoForwarding: t.func = ...
    usersSettingsGetAutoForwarding: t.func = ...
    usersSettingsGetImap: t.func = ...
    usersSettingsDelegatesCreate: t.func = ...
    usersSettingsDelegatesGet: t.func = ...
    usersSettingsDelegatesList: t.func = ...
    usersSettingsDelegatesDelete: t.func = ...
    usersSettingsFiltersList: t.func = ...
    usersSettingsFiltersCreate: t.func = ...
    usersSettingsFiltersGet: t.func = ...
    usersSettingsFiltersDelete: t.func = ...
    usersSettingsSendAsPatch: t.func = ...
    usersSettingsSendAsGet: t.func = ...
    usersSettingsSendAsDelete: t.func = ...
    usersSettingsSendAsList: t.func = ...
    usersSettingsSendAsUpdate: t.func = ...
    usersSettingsSendAsVerify: t.func = ...
    usersSettingsSendAsCreate: t.func = ...
    usersSettingsSendAsSmimeInfoSetDefault: t.func = ...
    usersSettingsSendAsSmimeInfoGet: t.func = ...
    usersSettingsSendAsSmimeInfoList: t.func = ...
    usersSettingsSendAsSmimeInfoInsert: t.func = ...
    usersSettingsSendAsSmimeInfoDelete: t.func = ...
    usersSettingsForwardingAddressesGet: t.func = ...
    usersSettingsForwardingAddressesList: t.func = ...
    usersSettingsForwardingAddressesCreate: t.func = ...
    usersSettingsForwardingAddressesDelete: t.func = ...
    usersSettingsCseKeypairsCreate: t.func = ...
    usersSettingsCseKeypairsDisable: t.func = ...
    usersSettingsCseKeypairsObliterate: t.func = ...
    usersSettingsCseKeypairsList: t.func = ...
    usersSettingsCseKeypairsGet: t.func = ...
    usersSettingsCseKeypairsEnable: t.func = ...
    usersSettingsCseIdentitiesPatch: t.func = ...
    usersSettingsCseIdentitiesGet: t.func = ...
    usersSettingsCseIdentitiesCreate: t.func = ...
    usersSettingsCseIdentitiesList: t.func = ...
    usersSettingsCseIdentitiesDelete: t.func = ...
    usersHistoryList: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_gmail() -> Import: ...