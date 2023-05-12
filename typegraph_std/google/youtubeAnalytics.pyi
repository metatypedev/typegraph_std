from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    QueryResponseIn: t.typedef = ...
    QueryResponseOut: t.typedef = ...
    GroupItemIn: t.typedef = ...
    GroupItemOut: t.typedef = ...
    EmptyResponseIn: t.typedef = ...
    EmptyResponseOut: t.typedef = ...
    GroupContentDetailsIn: t.typedef = ...
    GroupContentDetailsOut: t.typedef = ...
    ResultTableColumnHeaderIn: t.typedef = ...
    ResultTableColumnHeaderOut: t.typedef = ...
    GroupItemResourceIn: t.typedef = ...
    GroupItemResourceOut: t.typedef = ...
    ErrorsIn: t.typedef = ...
    ErrorsOut: t.typedef = ...
    GroupIn: t.typedef = ...
    GroupOut: t.typedef = ...
    ErrorProtoIn: t.typedef = ...
    ErrorProtoOut: t.typedef = ...
    GroupSnippetIn: t.typedef = ...
    GroupSnippetOut: t.typedef = ...
    ListGroupsResponseIn: t.typedef = ...
    ListGroupsResponseOut: t.typedef = ...
    ListGroupItemsResponseIn: t.typedef = ...
    ListGroupItemsResponseOut: t.typedef = ...

class FuncList:
    groupItemsList: t.func = ...
    groupItemsInsert: t.func = ...
    groupItemsDelete: t.func = ...
    groupsUpdate: t.func = ...
    groupsDelete: t.func = ...
    groupsList: t.func = ...
    groupsInsert: t.func = ...
    reportsQuery: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_youtubeAnalytics() -> Import: ...
