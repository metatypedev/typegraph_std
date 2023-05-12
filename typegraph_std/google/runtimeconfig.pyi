from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    ListOperationsResponseIn: t.typedef = ...
    ListOperationsResponseOut: t.typedef = ...
    EmptyIn: t.typedef = ...
    EmptyOut: t.typedef = ...
    CancelOperationRequestIn: t.typedef = ...
    CancelOperationRequestOut: t.typedef = ...
    OperationIn: t.typedef = ...
    OperationOut: t.typedef = ...
    StatusIn: t.typedef = ...
    StatusOut: t.typedef = ...

class FuncList:
    operationsCancel: t.func = ...
    operationsList: t.func = ...
    operationsDelete: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_runtimeconfig() -> Import: ...
