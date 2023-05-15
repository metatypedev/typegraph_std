from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    ExternalAccountKeyIn: t.typedef = ...
    ExternalAccountKeyOut: t.typedef = ...

class FuncList:
    projectsLocationsExternalAccountKeysCreate: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_publicca() -> Import: ...