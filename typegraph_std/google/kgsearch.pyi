from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    SearchResponseIn: t.typedef = ...
    SearchResponseOut: t.typedef = ...

class FuncList:
    entitiesSearch: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_kgsearch() -> Import: ...