from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    PromotionIn: t.typedef = ...
    PromotionOut: t.typedef = ...
    ResultIn: t.typedef = ...
    ResultOut: t.typedef = ...
    SearchIn: t.typedef = ...
    SearchOut: t.typedef = ...

class FuncList:
    cseList: t.func = ...
    cseSiterestrictList: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_customsearch() -> Import: ...
