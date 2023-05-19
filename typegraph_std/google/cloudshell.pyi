from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    AuthorizeEnvironmentResponseIn: t.typedef = ...
    AuthorizeEnvironmentResponseOut: t.typedef = ...
    RemovePublicKeyRequestIn: t.typedef = ...
    RemovePublicKeyRequestOut: t.typedef = ...
    AddPublicKeyResponseIn: t.typedef = ...
    AddPublicKeyResponseOut: t.typedef = ...
    StartEnvironmentRequestIn: t.typedef = ...
    StartEnvironmentRequestOut: t.typedef = ...
    RemovePublicKeyMetadataIn: t.typedef = ...
    RemovePublicKeyMetadataOut: t.typedef = ...
    RemovePublicKeyResponseIn: t.typedef = ...
    RemovePublicKeyResponseOut: t.typedef = ...
    StatusIn: t.typedef = ...
    StatusOut: t.typedef = ...
    EnvironmentIn: t.typedef = ...
    EnvironmentOut: t.typedef = ...
    EmptyIn: t.typedef = ...
    EmptyOut: t.typedef = ...
    ListOperationsResponseIn: t.typedef = ...
    ListOperationsResponseOut: t.typedef = ...
    CancelOperationRequestIn: t.typedef = ...
    CancelOperationRequestOut: t.typedef = ...
    DeleteEnvironmentMetadataIn: t.typedef = ...
    DeleteEnvironmentMetadataOut: t.typedef = ...
    StartEnvironmentMetadataIn: t.typedef = ...
    StartEnvironmentMetadataOut: t.typedef = ...
    CreateEnvironmentMetadataIn: t.typedef = ...
    CreateEnvironmentMetadataOut: t.typedef = ...
    OperationIn: t.typedef = ...
    OperationOut: t.typedef = ...
    AddPublicKeyMetadataIn: t.typedef = ...
    AddPublicKeyMetadataOut: t.typedef = ...
    StartEnvironmentResponseIn: t.typedef = ...
    StartEnvironmentResponseOut: t.typedef = ...
    AddPublicKeyRequestIn: t.typedef = ...
    AddPublicKeyRequestOut: t.typedef = ...
    AuthorizeEnvironmentMetadataIn: t.typedef = ...
    AuthorizeEnvironmentMetadataOut: t.typedef = ...
    AuthorizeEnvironmentRequestIn: t.typedef = ...
    AuthorizeEnvironmentRequestOut: t.typedef = ...

class FuncList:
    operationsList: t.func = ...
    operationsGet: t.func = ...
    operationsDelete: t.func = ...
    operationsCancel: t.func = ...
    usersEnvironmentsRemovePublicKey: t.func = ...
    usersEnvironmentsAuthorize: t.func = ...
    usersEnvironmentsStart: t.func = ...
    usersEnvironmentsGet: t.func = ...
    usersEnvironmentsAddPublicKey: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_cloudshell() -> Import: ...
