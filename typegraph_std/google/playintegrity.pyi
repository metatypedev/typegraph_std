from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    AppIntegrityIn: t.typedef = ...
    AppIntegrityOut: t.typedef = ...
    TestingDetailsIn: t.typedef = ...
    TestingDetailsOut: t.typedef = ...
    DecodeIntegrityTokenRequestIn: t.typedef = ...
    DecodeIntegrityTokenRequestOut: t.typedef = ...
    TokenPayloadExternalIn: t.typedef = ...
    TokenPayloadExternalOut: t.typedef = ...
    RequestDetailsIn: t.typedef = ...
    RequestDetailsOut: t.typedef = ...
    GuidanceDetailsIn: t.typedef = ...
    GuidanceDetailsOut: t.typedef = ...
    AccountDetailsIn: t.typedef = ...
    AccountDetailsOut: t.typedef = ...
    DecodeIntegrityTokenResponseIn: t.typedef = ...
    DecodeIntegrityTokenResponseOut: t.typedef = ...
    AccountActivityIn: t.typedef = ...
    AccountActivityOut: t.typedef = ...
    DeviceIntegrityIn: t.typedef = ...
    DeviceIntegrityOut: t.typedef = ...

class FuncList:
    v1DecodeIntegrityToken: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_playintegrity() -> Import: ...
