from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    ListInvitationsResponseIn: t.typedef = ...
    ListInvitationsResponseOut: t.typedef = ...
    TargetLocationIn: t.typedef = ...
    TargetLocationOut: t.typedef = ...
    ListLocationAdminsResponseIn: t.typedef = ...
    ListLocationAdminsResponseOut: t.typedef = ...
    EmptyIn: t.typedef = ...
    EmptyOut: t.typedef = ...
    InvitationIn: t.typedef = ...
    InvitationOut: t.typedef = ...
    AdminIn: t.typedef = ...
    AdminOut: t.typedef = ...
    TransferLocationRequestIn: t.typedef = ...
    TransferLocationRequestOut: t.typedef = ...
    AccountIn: t.typedef = ...
    AccountOut: t.typedef = ...
    DeclineInvitationRequestIn: t.typedef = ...
    DeclineInvitationRequestOut: t.typedef = ...
    PostalAddressIn: t.typedef = ...
    PostalAddressOut: t.typedef = ...
    ListAccountAdminsResponseIn: t.typedef = ...
    ListAccountAdminsResponseOut: t.typedef = ...
    AcceptInvitationRequestIn: t.typedef = ...
    AcceptInvitationRequestOut: t.typedef = ...
    ListAccountsResponseIn: t.typedef = ...
    ListAccountsResponseOut: t.typedef = ...
    OrganizationInfoIn: t.typedef = ...
    OrganizationInfoOut: t.typedef = ...

class FuncList:
    locationsTransfer: t.func = ...
    locationsAdminsCreate: t.func = ...
    locationsAdminsList: t.func = ...
    locationsAdminsPatch: t.func = ...
    locationsAdminsDelete: t.func = ...
    accountsPatch: t.func = ...
    accountsCreate: t.func = ...
    accountsGet: t.func = ...
    accountsList: t.func = ...
    accountsInvitationsAccept: t.func = ...
    accountsInvitationsDecline: t.func = ...
    accountsInvitationsList: t.func = ...
    accountsAdminsDelete: t.func = ...
    accountsAdminsCreate: t.func = ...
    accountsAdminsList: t.func = ...
    accountsAdminsPatch: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_mybusinessaccountmanagement() -> Import: ...
