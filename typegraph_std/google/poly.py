from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_poly() -> Import:
    poly = HTTPRuntime("https://poly.googleapis.com/")

    renames = {
        "ErrorResponse": "_poly_1_ErrorResponse",
        "ObjParseErrorIn": "_poly_2_ObjParseErrorIn",
        "ObjParseErrorOut": "_poly_3_ObjParseErrorOut",
        "AssetImportMessageIn": "_poly_4_AssetImportMessageIn",
        "AssetImportMessageOut": "_poly_5_AssetImportMessageOut",
        "ListLikedAssetsResponseIn": "_poly_6_ListLikedAssetsResponseIn",
        "ListLikedAssetsResponseOut": "_poly_7_ListLikedAssetsResponseOut",
        "StartAssetImportResponseIn": "_poly_8_StartAssetImportResponseIn",
        "StartAssetImportResponseOut": "_poly_9_StartAssetImportResponseOut",
        "PresentationParamsIn": "_poly_10_PresentationParamsIn",
        "PresentationParamsOut": "_poly_11_PresentationParamsOut",
        "QuaternionIn": "_poly_12_QuaternionIn",
        "QuaternionOut": "_poly_13_QuaternionOut",
        "ListUserAssetsResponseIn": "_poly_14_ListUserAssetsResponseIn",
        "ListUserAssetsResponseOut": "_poly_15_ListUserAssetsResponseOut",
        "ImageErrorIn": "_poly_16_ImageErrorIn",
        "ImageErrorOut": "_poly_17_ImageErrorOut",
        "UserAssetIn": "_poly_18_UserAssetIn",
        "UserAssetOut": "_poly_19_UserAssetOut",
        "AssetIn": "_poly_20_AssetIn",
        "AssetOut": "_poly_21_AssetOut",
        "RemixInfoIn": "_poly_22_RemixInfoIn",
        "RemixInfoOut": "_poly_23_RemixInfoOut",
        "FileIn": "_poly_24_FileIn",
        "FileOut": "_poly_25_FileOut",
        "FormatComplexityIn": "_poly_26_FormatComplexityIn",
        "FormatComplexityOut": "_poly_27_FormatComplexityOut",
        "ListAssetsResponseIn": "_poly_28_ListAssetsResponseIn",
        "ListAssetsResponseOut": "_poly_29_ListAssetsResponseOut",
        "FormatIn": "_poly_30_FormatIn",
        "FormatOut": "_poly_31_FormatOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ObjParseErrorIn"] = t.struct(
        {
            "filePath": t.string().optional(),
            "code": t.string().optional(),
            "line": t.string().optional(),
            "lineNumber": t.integer().optional(),
            "startIndex": t.integer().optional(),
            "endIndex": t.integer().optional(),
        }
    ).named(renames["ObjParseErrorIn"])
    types["ObjParseErrorOut"] = t.struct(
        {
            "filePath": t.string().optional(),
            "code": t.string().optional(),
            "line": t.string().optional(),
            "lineNumber": t.integer().optional(),
            "startIndex": t.integer().optional(),
            "endIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ObjParseErrorOut"])
    types["AssetImportMessageIn"] = t.struct(
        {
            "imageError": t.proxy(renames["ImageErrorIn"]).optional(),
            "objParseError": t.proxy(renames["ObjParseErrorIn"]).optional(),
            "filePath": t.string().optional(),
            "code": t.string().optional(),
        }
    ).named(renames["AssetImportMessageIn"])
    types["AssetImportMessageOut"] = t.struct(
        {
            "imageError": t.proxy(renames["ImageErrorOut"]).optional(),
            "objParseError": t.proxy(renames["ObjParseErrorOut"]).optional(),
            "filePath": t.string().optional(),
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssetImportMessageOut"])
    types["ListLikedAssetsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "assets": t.array(t.proxy(renames["AssetIn"])).optional(),
            "totalSize": t.integer().optional(),
        }
    ).named(renames["ListLikedAssetsResponseIn"])
    types["ListLikedAssetsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "assets": t.array(t.proxy(renames["AssetOut"])).optional(),
            "totalSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLikedAssetsResponseOut"])
    types["StartAssetImportResponseIn"] = t.struct(
        {
            "assetImportId": t.string().optional(),
            "assetImportMessages": t.array(
                t.proxy(renames["AssetImportMessageIn"])
            ).optional(),
            "publishUrl": t.string().optional(),
            "assetId": t.string().optional(),
        }
    ).named(renames["StartAssetImportResponseIn"])
    types["StartAssetImportResponseOut"] = t.struct(
        {
            "assetImportId": t.string().optional(),
            "assetImportMessages": t.array(
                t.proxy(renames["AssetImportMessageOut"])
            ).optional(),
            "publishUrl": t.string().optional(),
            "assetId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StartAssetImportResponseOut"])
    types["PresentationParamsIn"] = t.struct(
        {
            "colorSpace": t.string().optional(),
            "backgroundColor": t.string().optional(),
            "orientingRotation": t.proxy(renames["QuaternionIn"]).optional(),
        }
    ).named(renames["PresentationParamsIn"])
    types["PresentationParamsOut"] = t.struct(
        {
            "colorSpace": t.string().optional(),
            "backgroundColor": t.string().optional(),
            "orientingRotation": t.proxy(renames["QuaternionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PresentationParamsOut"])
    types["QuaternionIn"] = t.struct(
        {
            "x": t.number().optional(),
            "y": t.number().optional(),
            "w": t.number().optional(),
            "z": t.number().optional(),
        }
    ).named(renames["QuaternionIn"])
    types["QuaternionOut"] = t.struct(
        {
            "x": t.number().optional(),
            "y": t.number().optional(),
            "w": t.number().optional(),
            "z": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuaternionOut"])
    types["ListUserAssetsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "userAssets": t.array(t.proxy(renames["UserAssetIn"])).optional(),
            "totalSize": t.integer().optional(),
        }
    ).named(renames["ListUserAssetsResponseIn"])
    types["ListUserAssetsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "userAssets": t.array(t.proxy(renames["UserAssetOut"])).optional(),
            "totalSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListUserAssetsResponseOut"])
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
    types["UserAssetIn"] = t.struct(
        {"asset": t.proxy(renames["AssetIn"]).optional()}
    ).named(renames["UserAssetIn"])
    types["UserAssetOut"] = t.struct(
        {
            "asset": t.proxy(renames["AssetOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserAssetOut"])
    types["AssetIn"] = t.struct(
        {
            "visibility": t.string().optional(),
            "description": t.string().optional(),
            "thumbnail": t.proxy(renames["FileIn"]).optional(),
            "updateTime": t.string().optional(),
            "metadata": t.string().optional(),
            "formats": t.array(t.proxy(renames["FormatIn"])).optional(),
            "remixInfo": t.proxy(renames["RemixInfoIn"]).optional(),
            "authorName": t.string().optional(),
            "license": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "isCurated": t.boolean().optional(),
            "presentationParams": t.proxy(renames["PresentationParamsIn"]).optional(),
        }
    ).named(renames["AssetIn"])
    types["AssetOut"] = t.struct(
        {
            "visibility": t.string().optional(),
            "description": t.string().optional(),
            "thumbnail": t.proxy(renames["FileOut"]).optional(),
            "updateTime": t.string().optional(),
            "metadata": t.string().optional(),
            "formats": t.array(t.proxy(renames["FormatOut"])).optional(),
            "remixInfo": t.proxy(renames["RemixInfoOut"]).optional(),
            "authorName": t.string().optional(),
            "license": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "isCurated": t.boolean().optional(),
            "presentationParams": t.proxy(renames["PresentationParamsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssetOut"])
    types["RemixInfoIn"] = t.struct(
        {"sourceAsset": t.array(t.string()).optional()}
    ).named(renames["RemixInfoIn"])
    types["RemixInfoOut"] = t.struct(
        {
            "sourceAsset": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemixInfoOut"])
    types["FileIn"] = t.struct(
        {
            "url": t.string().optional(),
            "contentType": t.string().optional(),
            "relativePath": t.string().optional(),
        }
    ).named(renames["FileIn"])
    types["FileOut"] = t.struct(
        {
            "url": t.string().optional(),
            "contentType": t.string().optional(),
            "relativePath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileOut"])
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
    types["ListAssetsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "assets": t.array(t.proxy(renames["AssetIn"])).optional(),
            "totalSize": t.integer().optional(),
        }
    ).named(renames["ListAssetsResponseIn"])
    types["ListAssetsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "assets": t.array(t.proxy(renames["AssetOut"])).optional(),
            "totalSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAssetsResponseOut"])
    types["FormatIn"] = t.struct(
        {
            "formatType": t.string().optional(),
            "formatComplexity": t.proxy(renames["FormatComplexityIn"]).optional(),
            "resources": t.array(t.proxy(renames["FileIn"])).optional(),
            "root": t.proxy(renames["FileIn"]).optional(),
        }
    ).named(renames["FormatIn"])
    types["FormatOut"] = t.struct(
        {
            "formatType": t.string().optional(),
            "formatComplexity": t.proxy(renames["FormatComplexityOut"]).optional(),
            "resources": t.array(t.proxy(renames["FileOut"])).optional(),
            "root": t.proxy(renames["FileOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FormatOut"])

    functions = {}
    functions["usersAssetsList"] = poly.get(
        "v1/{name}/assets",
        t.struct(
            {
                "visibility": t.string().optional(),
                "orderBy": t.string().optional(),
                "name": t.string().optional(),
                "format": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "orderBy": t.string().optional(),
                "format": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
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
                "format": t.string().optional(),
                "maxComplexity": t.string().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "category": t.string().optional(),
                "curated": t.boolean().optional(),
                "pageSize": t.integer().optional(),
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
                "format": t.string().optional(),
                "maxComplexity": t.string().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "category": t.string().optional(),
                "curated": t.boolean().optional(),
                "pageSize": t.integer().optional(),
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
