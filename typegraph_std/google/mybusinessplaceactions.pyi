from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    EmptyIn: t.typedef = ...
    EmptyOut: t.typedef = ...
    ListPlaceActionTypeMetadataResponseIn: t.typedef = ...
    ListPlaceActionTypeMetadataResponseOut: t.typedef = ...
    ListPlaceActionLinksResponseIn: t.typedef = ...
    ListPlaceActionLinksResponseOut: t.typedef = ...
    PlaceActionTypeMetadataIn: t.typedef = ...
    PlaceActionTypeMetadataOut: t.typedef = ...
    PlaceActionLinkIn: t.typedef = ...
    PlaceActionLinkOut: t.typedef = ...

class FuncList:
    locationsPlaceActionLinksPatch: t.func = ...
    locationsPlaceActionLinksGet: t.func = ...
    locationsPlaceActionLinksDelete: t.func = ...
    locationsPlaceActionLinksCreate: t.func = ...
    locationsPlaceActionLinksList: t.func = ...
    placeActionTypeMetadataList: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_mybusinessplaceactions() -> Import: ...
