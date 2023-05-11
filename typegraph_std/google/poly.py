from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_poly() -> Import:
    poly = HTTPRuntime("https://poly.googleapis.com/")

    renames = {
        "ErrorResponse": "_poly_1_ErrorResponse",
        "AssetIn": "_poly_2_AssetIn",
        "AssetOut": "_poly_3_AssetOut",
        "ListUserAssetsResponseIn": "_poly_4_ListUserAssetsResponseIn",
        "ListUserAssetsResponseOut": "_poly_5_ListUserAssetsResponseOut",
        "FormatIn": "_poly_6_FormatIn",
        "FormatOut": "_poly_7_FormatOut",
        "QuaternionIn": "_poly_8_QuaternionIn",
        "QuaternionOut": "_poly_9_QuaternionOut",
        "ListAssetsResponseIn": "_poly_10_ListAssetsResponseIn",
        "ListAssetsResponseOut": "_poly_11_ListAssetsResponseOut",
        "ImageErrorIn": "_poly_12_ImageErrorIn",
        "ImageErrorOut": "_poly_13_ImageErrorOut",
        "AssetImportMessageIn": "_poly_14_AssetImportMessageIn",
        "AssetImportMessageOut": "_poly_15_AssetImportMessageOut",
        "RemixInfoIn": "_poly_16_RemixInfoIn",
        "RemixInfoOut": "_poly_17_RemixInfoOut",
        "FormatComplexityIn": "_poly_18_FormatComplexityIn",
        "FormatComplexityOut": "_poly_19_FormatComplexityOut",
        "UserAssetIn": "_poly_20_UserAssetIn",
        "UserAssetOut": "_poly_21_UserAssetOut",
        "FileIn": "_poly_22_FileIn",
        "FileOut": "_poly_23_FileOut",
        "ListLikedAssetsResponseIn": "_poly_24_ListLikedAssetsResponseIn",
        "ListLikedAssetsResponseOut": "_poly_25_ListLikedAssetsResponseOut",
        "StartAssetImportResponseIn": "_poly_26_StartAssetImportResponseIn",
        "StartAssetImportResponseOut": "_poly_27_StartAssetImportResponseOut",
        "ObjParseErrorIn": "_poly_28_ObjParseErrorIn",
        "ObjParseErrorOut": "_poly_29_ObjParseErrorOut",
        "PresentationParamsIn": "_poly_30_PresentationParamsIn",
        "PresentationParamsOut": "_poly_31_PresentationParamsOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["AssetIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "formats": t.array(t.proxy(renames["FormatIn"])).optional(),
            "metadata": t.string().optional(),
            "license": t.string().optional(),
            "visibility": t.string().optional(),
            "authorName": t.string().optional(),
            "isCurated": t.boolean().optional(),
            "presentationParams": t.proxy(renames["PresentationParamsIn"]).optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "remixInfo": t.proxy(renames["RemixInfoIn"]).optional(),
            "description": t.string().optional(),
            "thumbnail": t.proxy(renames["FileIn"]).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["AssetIn"])
    types["AssetOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "formats": t.array(t.proxy(renames["FormatOut"])).optional(),
            "metadata": t.string().optional(),
            "license": t.string().optional(),
            "visibility": t.string().optional(),
            "authorName": t.string().optional(),
            "isCurated": t.boolean().optional(),
            "presentationParams": t.proxy(renames["PresentationParamsOut"]).optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "remixInfo": t.proxy(renames["RemixInfoOut"]).optional(),
            "description": t.string().optional(),
            "thumbnail": t.proxy(renames["FileOut"]).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssetOut"])
    types["ListUserAssetsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "userAssets": t.array(t.proxy(renames["UserAssetIn"])).optional(),
        }
    ).named(renames["ListUserAssetsResponseIn"])
    types["ListUserAssetsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "userAssets": t.array(t.proxy(renames["UserAssetOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListUserAssetsResponseOut"])
    types["FormatIn"] = t.struct(
        {
            "root": t.proxy(renames["FileIn"]).optional(),
            "formatComplexity": t.proxy(renames["FormatComplexityIn"]).optional(),
            "formatType": t.string().optional(),
            "resources": t.array(t.proxy(renames["FileIn"])).optional(),
        }
    ).named(renames["FormatIn"])
    types["FormatOut"] = t.struct(
        {
            "root": t.proxy(renames["FileOut"]).optional(),
            "formatComplexity": t.proxy(renames["FormatComplexityOut"]).optional(),
            "formatType": t.string().optional(),
            "resources": t.array(t.proxy(renames["FileOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FormatOut"])
    types["QuaternionIn"] = t.struct(
        {
            "x": t.number().optional(),
            "y": t.number().optional(),
            "z": t.number().optional(),
            "w": t.number().optional(),
        }
    ).named(renames["QuaternionIn"])
    types["QuaternionOut"] = t.struct(
        {
            "x": t.number().optional(),
            "y": t.number().optional(),
            "z": t.number().optional(),
            "w": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuaternionOut"])
    types["ListAssetsResponseIn"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "assets": t.array(t.proxy(renames["AssetIn"])).optional(),
        }
    ).named(renames["ListAssetsResponseIn"])
    types["ListAssetsResponseOut"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "assets": t.array(t.proxy(renames["AssetOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAssetsResponseOut"])
    types["ImageErrorIn"] = t.struct(
        {"filePath": t.string().optional(), "code": t.string().optional()}
    ).named(renames["ImageErrorIn"])
    types["ImageErrorOut"] = t.struct(
        {
            "filePath": t.string().optional(),
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageErrorOut"])
    types["AssetImportMessageIn"] = t.struct(
        {
            "imageError": t.proxy(renames["ImageErrorIn"]).optional(),
            "filePath": t.string().optional(),
            "objParseError": t.proxy(renames["ObjParseErrorIn"]).optional(),
            "code": t.string().optional(),
        }
    ).named(renames["AssetImportMessageIn"])
    types["AssetImportMessageOut"] = t.struct(
        {
            "imageError": t.proxy(renames["ImageErrorOut"]).optional(),
            "filePath": t.string().optional(),
            "objParseError": t.proxy(renames["ObjParseErrorOut"]).optional(),
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssetImportMessageOut"])
    types["RemixInfoIn"] = t.struct(
        {"sourceAsset": t.array(t.string()).optional()}
    ).named(renames["RemixInfoIn"])
    types["RemixInfoOut"] = t.struct(
        {
            "sourceAsset": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemixInfoOut"])
    types["FormatComplexityIn"] = t.struct(
        {"lodHint": t.integer().optional(), "triangleCount": t.string().optional()}
    ).named(renames["FormatComplexityIn"])
    types["FormatComplexityOut"] = t.struct(
        {
            "lodHint": t.integer().optional(),
            "triangleCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FormatComplexityOut"])
    types["UserAssetIn"] = t.struct(
        {"asset": t.proxy(renames["AssetIn"]).optional()}
    ).named(renames["UserAssetIn"])
    types["UserAssetOut"] = t.struct(
        {
            "asset": t.proxy(renames["AssetOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserAssetOut"])
    types["FileIn"] = t.struct(
        {
            "contentType": t.string().optional(),
            "url": t.string().optional(),
            "relativePath": t.string().optional(),
        }
    ).named(renames["FileIn"])
    types["FileOut"] = t.struct(
        {
            "contentType": t.string().optional(),
            "url": t.string().optional(),
            "relativePath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileOut"])
    types["ListLikedAssetsResponseIn"] = t.struct(
        {
            "assets": t.array(t.proxy(renames["AssetIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
        }
    ).named(renames["ListLikedAssetsResponseIn"])
    types["ListLikedAssetsResponseOut"] = t.struct(
        {
            "assets": t.array(t.proxy(renames["AssetOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLikedAssetsResponseOut"])
    types["StartAssetImportResponseIn"] = t.struct(
        {
            "assetId": t.string().optional(),
            "assetImportMessages": t.array(
                t.proxy(renames["AssetImportMessageIn"])
            ).optional(),
            "publishUrl": t.string().optional(),
            "assetImportId": t.string().optional(),
        }
    ).named(renames["StartAssetImportResponseIn"])
    types["StartAssetImportResponseOut"] = t.struct(
        {
            "assetId": t.string().optional(),
            "assetImportMessages": t.array(
                t.proxy(renames["AssetImportMessageOut"])
            ).optional(),
            "publishUrl": t.string().optional(),
            "assetImportId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StartAssetImportResponseOut"])
    types["ObjParseErrorIn"] = t.struct(
        {
            "startIndex": t.integer().optional(),
            "line": t.string().optional(),
            "endIndex": t.integer().optional(),
            "lineNumber": t.integer().optional(),
            "filePath": t.string().optional(),
            "code": t.string().optional(),
        }
    ).named(renames["ObjParseErrorIn"])
    types["ObjParseErrorOut"] = t.struct(
        {
            "startIndex": t.integer().optional(),
            "line": t.string().optional(),
            "endIndex": t.integer().optional(),
            "lineNumber": t.integer().optional(),
            "filePath": t.string().optional(),
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ObjParseErrorOut"])
    types["PresentationParamsIn"] = t.struct(
        {
            "orientingRotation": t.proxy(renames["QuaternionIn"]).optional(),
            "backgroundColor": t.string().optional(),
            "colorSpace": t.string().optional(),
        }
    ).named(renames["PresentationParamsIn"])
    types["PresentationParamsOut"] = t.struct(
        {
            "orientingRotation": t.proxy(renames["QuaternionOut"]).optional(),
            "backgroundColor": t.string().optional(),
            "colorSpace": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PresentationParamsOut"])

    functions = {}
    functions["assetsList"] = poly.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["AssetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["assetsGet"] = poly.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["AssetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersAssetsList"] = poly.get(
        "v1/{name}/assets",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "visibility": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "format": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListUserAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersLikedassetsList"] = poly.get(
        "v1/{name}/likedassets",
        t.struct(
            {
                "format": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLikedAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(importer="poly", renames=renames, types=types, functions=functions)
