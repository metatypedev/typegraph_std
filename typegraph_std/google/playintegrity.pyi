from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    DeviceIntegrityIn: t.typedef = ...
    DeviceIntegrityOut: t.typedef = ...
    DecodeIntegrityTokenResponseIn: t.typedef = ...
    DecodeIntegrityTokenResponseOut: t.typedef = ...
    DecodeIntegrityTokenRequestIn: t.typedef = ...
    DecodeIntegrityTokenRequestOut: t.typedef = ...
    TokenPayloadExternalIn: t.typedef = ...
    TokenPayloadExternalOut: t.typedef = ...
    AccountActivityIn: t.typedef = ...
    AccountActivityOut: t.typedef = ...
    TestingDetailsIn: t.typedef = ...
    TestingDetailsOut: t.typedef = ...
    RequestDetailsIn: t.typedef = ...
    RequestDetailsOut: t.typedef = ...
    AppIntegrityIn: t.typedef = ...
    AppIntegrityOut: t.typedef = ...
    AccountDetailsIn: t.typedef = ...
    AccountDetailsOut: t.typedef = ...

class FuncList:
    v1DecodeIntegrityToken: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_playintegrity() -> Import: ...