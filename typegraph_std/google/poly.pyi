from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    StartAssetImportResponseIn: t.typedef = ...
    StartAssetImportResponseOut: t.typedef = ...
    FormatIn: t.typedef = ...
    FormatOut: t.typedef = ...
    ListAssetsResponseIn: t.typedef = ...
    ListAssetsResponseOut: t.typedef = ...
    ObjParseErrorIn: t.typedef = ...
    ObjParseErrorOut: t.typedef = ...
    FileIn: t.typedef = ...
    FileOut: t.typedef = ...
    AssetIn: t.typedef = ...
    AssetOut: t.typedef = ...
    PresentationParamsIn: t.typedef = ...
    PresentationParamsOut: t.typedef = ...
    AssetImportMessageIn: t.typedef = ...
    AssetImportMessageOut: t.typedef = ...
    QuaternionIn: t.typedef = ...
    QuaternionOut: t.typedef = ...
    ListUserAssetsResponseIn: t.typedef = ...
    ListUserAssetsResponseOut: t.typedef = ...
    UserAssetIn: t.typedef = ...
    UserAssetOut: t.typedef = ...
    ImageErrorIn: t.typedef = ...
    ImageErrorOut: t.typedef = ...
    FormatComplexityIn: t.typedef = ...
    FormatComplexityOut: t.typedef = ...
    RemixInfoIn: t.typedef = ...
    RemixInfoOut: t.typedef = ...
    ListLikedAssetsResponseIn: t.typedef = ...
    ListLikedAssetsResponseOut: t.typedef = ...

class FuncList:
    usersAssetsList: t.func = ...
    usersLikedassetsList: t.func = ...
    assetsGet: t.func = ...
    assetsList: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_poly() -> Import: ...
