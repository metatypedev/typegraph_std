from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    StatusIn: t.typedef = ...
    StatusOut: t.typedef = ...
    TestIamPermissionsRequestIn: t.typedef = ...
    TestIamPermissionsRequestOut: t.typedef = ...
    ExprIn: t.typedef = ...
    ExprOut: t.typedef = ...
    ListReposResponseIn: t.typedef = ...
    ListReposResponseOut: t.typedef = ...
    UpdateRepoRequestIn: t.typedef = ...
    UpdateRepoRequestOut: t.typedef = ...
    AuditConfigIn: t.typedef = ...
    AuditConfigOut: t.typedef = ...
    BindingIn: t.typedef = ...
    BindingOut: t.typedef = ...
    EmptyIn: t.typedef = ...
    EmptyOut: t.typedef = ...
    AuditLogConfigIn: t.typedef = ...
    AuditLogConfigOut: t.typedef = ...
    ProjectConfigIn: t.typedef = ...
    ProjectConfigOut: t.typedef = ...
    PolicyIn: t.typedef = ...
    PolicyOut: t.typedef = ...
    SyncRepoRequestIn: t.typedef = ...
    SyncRepoRequestOut: t.typedef = ...
    PubsubConfigIn: t.typedef = ...
    PubsubConfigOut: t.typedef = ...
    UpdateProjectConfigRequestIn: t.typedef = ...
    UpdateProjectConfigRequestOut: t.typedef = ...
    TestIamPermissionsResponseIn: t.typedef = ...
    TestIamPermissionsResponseOut: t.typedef = ...
    OperationIn: t.typedef = ...
    OperationOut: t.typedef = ...
    SetIamPolicyRequestIn: t.typedef = ...
    SetIamPolicyRequestOut: t.typedef = ...
    RepoIn: t.typedef = ...
    RepoOut: t.typedef = ...
    SyncRepoMetadataIn: t.typedef = ...
    SyncRepoMetadataOut: t.typedef = ...
    MirrorConfigIn: t.typedef = ...
    MirrorConfigOut: t.typedef = ...

class FuncList:
    projectsGetConfig: t.func = ...
    projectsUpdateConfig: t.func = ...
    projectsReposPatch: t.func = ...
    projectsReposDelete: t.func = ...
    projectsReposGetIamPolicy: t.func = ...
    projectsReposTestIamPermissions: t.func = ...
    projectsReposList: t.func = ...
    projectsReposGet: t.func = ...
    projectsReposSync: t.func = ...
    projectsReposSetIamPolicy: t.func = ...
    projectsReposCreate: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_sourcerepo() -> Import: ...