from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_poly():
    poly = HTTPRuntime("https://poly.googleapis.com/")

    renames = {
        "ErrorResponse": "_poly_1_ErrorResponse",
        "StartAssetImportResponseIn": "_poly_2_StartAssetImportResponseIn",
        "StartAssetImportResponseOut": "_poly_3_StartAssetImportResponseOut",
        "FormatIn": "_poly_4_FormatIn",
        "FormatOut": "_poly_5_FormatOut",
        "ListAssetsResponseIn": "_poly_6_ListAssetsResponseIn",
        "ListAssetsResponseOut": "_poly_7_ListAssetsResponseOut",
        "ObjParseErrorIn": "_poly_8_ObjParseErrorIn",
        "ObjParseErrorOut": "_poly_9_ObjParseErrorOut",
        "FileIn": "_poly_10_FileIn",
        "FileOut": "_poly_11_FileOut",
        "AssetIn": "_poly_12_AssetIn",
        "AssetOut": "_poly_13_AssetOut",
        "PresentationParamsIn": "_poly_14_PresentationParamsIn",
        "PresentationParamsOut": "_poly_15_PresentationParamsOut",
        "AssetImportMessageIn": "_poly_16_AssetImportMessageIn",
        "AssetImportMessageOut": "_poly_17_AssetImportMessageOut",
        "QuaternionIn": "_poly_18_QuaternionIn",
        "QuaternionOut": "_poly_19_QuaternionOut",
        "ListUserAssetsResponseIn": "_poly_20_ListUserAssetsResponseIn",
        "ListUserAssetsResponseOut": "_poly_21_ListUserAssetsResponseOut",
        "UserAssetIn": "_poly_22_UserAssetIn",
        "UserAssetOut": "_poly_23_UserAssetOut",
        "ImageErrorIn": "_poly_24_ImageErrorIn",
        "ImageErrorOut": "_poly_25_ImageErrorOut",
        "FormatComplexityIn": "_poly_26_FormatComplexityIn",
        "FormatComplexityOut": "_poly_27_FormatComplexityOut",
        "RemixInfoIn": "_poly_28_RemixInfoIn",
        "RemixInfoOut": "_poly_29_RemixInfoOut",
        "ListLikedAssetsResponseIn": "_poly_30_ListLikedAssetsResponseIn",
        "ListLikedAssetsResponseOut": "_poly_31_ListLikedAssetsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["StartAssetImportResponseIn"] = t.struct(
        {
            "assetImportId": t.string().optional(),
            "assetId": t.string().optional(),
            "publishUrl": t.string().optional(),
            "assetImportMessages": t.array(
                t.proxy(renames["AssetImportMessageIn"])
            ).optional(),
        }
    ).named(renames["StartAssetImportResponseIn"])
    types["StartAssetImportResponseOut"] = t.struct(
        {
            "assetImportId": t.string().optional(),
            "assetId": t.string().optional(),
            "publishUrl": t.string().optional(),
            "assetImportMessages": t.array(
                t.proxy(renames["AssetImportMessageOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StartAssetImportResponseOut"])
    types["FormatIn"] = t.struct(
        {
            "resources": t.array(t.proxy(renames["FileIn"])).optional(),
            "formatType": t.string().optional(),
            "formatComplexity": t.proxy(renames["FormatComplexityIn"]).optional(),
            "root": t.proxy(renames["FileIn"]).optional(),
        }
    ).named(renames["FormatIn"])
    types["FormatOut"] = t.struct(
        {
            "resources": t.array(t.proxy(renames["FileOut"])).optional(),
            "formatType": t.string().optional(),
            "formatComplexity": t.proxy(renames["FormatComplexityOut"]).optional(),
            "root": t.proxy(renames["FileOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FormatOut"])
    types["ListAssetsResponseIn"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "assets": t.array(t.proxy(renames["AssetIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListAssetsResponseIn"])
    types["ListAssetsResponseOut"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "assets": t.array(t.proxy(renames["AssetOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAssetsResponseOut"])
    types["ObjParseErrorIn"] = t.struct(
        {
            "line": t.string().optional(),
            "lineNumber": t.integer().optional(),
            "startIndex": t.integer().optional(),
            "filePath": t.string().optional(),
            "code": t.string().optional(),
            "endIndex": t.integer().optional(),
        }
    ).named(renames["ObjParseErrorIn"])
    types["ObjParseErrorOut"] = t.struct(
        {
            "line": t.string().optional(),
            "lineNumber": t.integer().optional(),
            "startIndex": t.integer().optional(),
            "filePath": t.string().optional(),
            "code": t.string().optional(),
            "endIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ObjParseErrorOut"])
    types["FileIn"] = t.struct(
        {
            "contentType": t.string().optional(),
            "relativePath": t.string().optional(),
            "url": t.string().optional(),
        }
    ).named(renames["FileIn"])
    types["FileOut"] = t.struct(
        {
            "contentType": t.string().optional(),
            "relativePath": t.string().optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileOut"])
    types["AssetIn"] = t.struct(
        {
            "presentationParams": t.proxy(renames["PresentationParamsIn"]).optional(),
            "isCurated": t.boolean().optional(),
            "authorName": t.string().optional(),
            "license": t.string().optional(),
            "metadata": t.string().optional(),
            "thumbnail": t.proxy(renames["FileIn"]).optional(),
            "updateTime": t.string().optional(),
            "remixInfo": t.proxy(renames["RemixInfoIn"]).optional(),
            "createTime": t.string().optional(),
            "description": t.string().optional(),
            "visibility": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "formats": t.array(t.proxy(renames["FormatIn"])).optional(),
        }
    ).named(renames["AssetIn"])
    types["AssetOut"] = t.struct(
        {
            "presentationParams": t.proxy(renames["PresentationParamsOut"]).optional(),
            "isCurated": t.boolean().optional(),
            "authorName": t.string().optional(),
            "license": t.string().optional(),
            "metadata": t.string().optional(),
            "thumbnail": t.proxy(renames["FileOut"]).optional(),
            "updateTime": t.string().optional(),
            "remixInfo": t.proxy(renames["RemixInfoOut"]).optional(),
            "createTime": t.string().optional(),
            "description": t.string().optional(),
            "visibility": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "formats": t.array(t.proxy(renames["FormatOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssetOut"])
    types["PresentationParamsIn"] = t.struct(
        {
            "colorSpace": t.string().optional(),
            "orientingRotation": t.proxy(renames["QuaternionIn"]).optional(),
            "backgroundColor": t.string().optional(),
        }
    ).named(renames["PresentationParamsIn"])
    types["PresentationParamsOut"] = t.struct(
        {
            "colorSpace": t.string().optional(),
            "orientingRotation": t.proxy(renames["QuaternionOut"]).optional(),
            "backgroundColor": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PresentationParamsOut"])
    types["AssetImportMessageIn"] = t.struct(
        {
            "objParseError": t.proxy(renames["ObjParseErrorIn"]).optional(),
            "imageError": t.proxy(renames["ImageErrorIn"]).optional(),
            "code": t.string().optional(),
            "filePath": t.string().optional(),
        }
    ).named(renames["AssetImportMessageIn"])
    types["AssetImportMessageOut"] = t.struct(
        {
            "objParseError": t.proxy(renames["ObjParseErrorOut"]).optional(),
            "imageError": t.proxy(renames["ImageErrorOut"]).optional(),
            "code": t.string().optional(),
            "filePath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssetImportMessageOut"])
    types["QuaternionIn"] = t.struct(
        {
            "y": t.number().optional(),
            "x": t.number().optional(),
            "z": t.number().optional(),
            "w": t.number().optional(),
        }
    ).named(renames["QuaternionIn"])
    types["QuaternionOut"] = t.struct(
        {
            "y": t.number().optional(),
            "x": t.number().optional(),
            "z": t.number().optional(),
            "w": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuaternionOut"])
    types["ListUserAssetsResponseIn"] = t.struct(
        {
            "userAssets": t.array(t.proxy(renames["UserAssetIn"])).optional(),
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListUserAssetsResponseIn"])
    types["ListUserAssetsResponseOut"] = t.struct(
        {
            "userAssets": t.array(t.proxy(renames["UserAssetOut"])).optional(),
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListUserAssetsResponseOut"])
    types["UserAssetIn"] = t.struct(
        {"asset": t.proxy(renames["AssetIn"]).optional()}
    ).named(renames["UserAssetIn"])
    types["UserAssetOut"] = t.struct(
        {
            "asset": t.proxy(renames["AssetOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserAssetOut"])
    types["ImageErrorIn"] = t.struct(
        {"code": t.string().optional(), "filePath": t.string().optional()}
    ).named(renames["ImageErrorIn"])
    types["ImageErrorOut"] = t.struct(
        {
            "code": t.string().optional(),
            "filePath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageErrorOut"])
    types["FormatComplexityIn"] = t.struct(
        {"triangleCount": t.string().optional(), "lodHint": t.integer().optional()}
    ).named(renames["FormatComplexityIn"])
    types["FormatComplexityOut"] = t.struct(
        {
            "triangleCount": t.string().optional(),
            "lodHint": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FormatComplexityOut"])
    types["RemixInfoIn"] = t.struct(
        {"sourceAsset": t.array(t.string()).optional()}
    ).named(renames["RemixInfoIn"])
    types["RemixInfoOut"] = t.struct(
        {
            "sourceAsset": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemixInfoOut"])
    types["ListLikedAssetsResponseIn"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "assets": t.array(t.proxy(renames["AssetIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListLikedAssetsResponseIn"])
    types["ListLikedAssetsResponseOut"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "assets": t.array(t.proxy(renames["AssetOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLikedAssetsResponseOut"])

    functions = {}
    functions["usersAssetsList"] = poly.get(
        "v1/{name}/assets",
        t.struct(
            {
                "visibility": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "format": t.string().optional(),
                "name": t.string().optional(),
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
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "format": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLikedAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["assetsGet"] = poly.get(
        "v1/assets",
        t.struct(
            {
                "maxComplexity": t.string().optional(),
                "format": t.string().optional(),
                "pageSize": t.integer().optional(),
                "category": t.string().optional(),
                "curated": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "keywords": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["assetsList"] = poly.get(
        "v1/assets",
        t.struct(
            {
                "maxComplexity": t.string().optional(),
                "format": t.string().optional(),
                "pageSize": t.integer().optional(),
                "category": t.string().optional(),
                "curated": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "keywords": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="poly", renames=renames, types=Box(types), functions=Box(functions)
    )
