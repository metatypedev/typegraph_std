from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    V2KeyIn: t.typedef = ...
    V2KeyOut: t.typedef = ...
    V2AndroidKeyRestrictionsIn: t.typedef = ...
    V2AndroidKeyRestrictionsOut: t.typedef = ...
    OperationIn: t.typedef = ...
    OperationOut: t.typedef = ...
    V2AndroidApplicationIn: t.typedef = ...
    V2AndroidApplicationOut: t.typedef = ...
    V2ListKeysResponseIn: t.typedef = ...
    V2ListKeysResponseOut: t.typedef = ...
    StatusIn: t.typedef = ...
    StatusOut: t.typedef = ...
    V2IosKeyRestrictionsIn: t.typedef = ...
    V2IosKeyRestrictionsOut: t.typedef = ...
    V2BrowserKeyRestrictionsIn: t.typedef = ...
    V2BrowserKeyRestrictionsOut: t.typedef = ...
    V2LookupKeyResponseIn: t.typedef = ...
    V2LookupKeyResponseOut: t.typedef = ...
    V2GetKeyStringResponseIn: t.typedef = ...
    V2GetKeyStringResponseOut: t.typedef = ...
    V2UndeleteKeyRequestIn: t.typedef = ...
    V2UndeleteKeyRequestOut: t.typedef = ...
    V2ApiTargetIn: t.typedef = ...
    V2ApiTargetOut: t.typedef = ...
    V2RestrictionsIn: t.typedef = ...
    V2RestrictionsOut: t.typedef = ...
    V2ServerKeyRestrictionsIn: t.typedef = ...
    V2ServerKeyRestrictionsOut: t.typedef = ...

class FuncList:
    keysLookupKey: t.func = ...
    operationsGet: t.func = ...
    projectsLocationsKeysGet: t.func = ...
    projectsLocationsKeysGetKeyString: t.func = ...
    projectsLocationsKeysUndelete: t.func = ...
    projectsLocationsKeysPatch: t.func = ...
    projectsLocationsKeysDelete: t.func = ...
    projectsLocationsKeysList: t.func = ...
    projectsLocationsKeysCreate: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_apikeys() -> Import: ...
