from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    SiteSummaryResponseIn: t.typedef = ...
    SiteSummaryResponseOut: t.typedef = ...
    PlatformSummaryIn: t.typedef = ...
    PlatformSummaryOut: t.typedef = ...
    ViolatingSitesResponseIn: t.typedef = ...
    ViolatingSitesResponseOut: t.typedef = ...

class FuncList:
    violatingSitesList: t.func = ...
    sitesGet: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_adexperiencereport() -> Import: ...
