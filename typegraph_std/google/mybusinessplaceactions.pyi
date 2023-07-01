from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    PlaceActionLinkIn: t.typedef = ...
    PlaceActionLinkOut: t.typedef = ...
    ListPlaceActionLinksResponseIn: t.typedef = ...
    ListPlaceActionLinksResponseOut: t.typedef = ...
    EmptyIn: t.typedef = ...
    EmptyOut: t.typedef = ...
    ListPlaceActionTypeMetadataResponseIn: t.typedef = ...
    ListPlaceActionTypeMetadataResponseOut: t.typedef = ...
    PlaceActionTypeMetadataIn: t.typedef = ...
    PlaceActionTypeMetadataOut: t.typedef = ...

class FuncList:
    placeActionTypeMetadataList: t.func = ...
    locationsPlaceActionLinksCreate: t.func = ...
    locationsPlaceActionLinksGet: t.func = ...
    locationsPlaceActionLinksDelete: t.func = ...
    locationsPlaceActionLinksPatch: t.func = ...
    locationsPlaceActionLinksList: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_mybusinessplaceactions() -> Import: ...
