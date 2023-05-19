from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_poly() -> Import:
    poly = HTTPRuntime("https://poly.googleapis.com/")

    renames = {
        "ErrorResponse": "_poly_1_ErrorResponse",
        "AssetIn": "_poly_2_AssetIn",
        "AssetOut": "_poly_3_AssetOut",
        "ImageErrorIn": "_poly_4_ImageErrorIn",
        "ImageErrorOut": "_poly_5_ImageErrorOut",
        "RemixInfoIn": "_poly_6_RemixInfoIn",
        "RemixInfoOut": "_poly_7_RemixInfoOut",
        "PresentationParamsIn": "_poly_8_PresentationParamsIn",
        "PresentationParamsOut": "_poly_9_PresentationParamsOut",
        "UserAssetIn": "_poly_10_UserAssetIn",
        "UserAssetOut": "_poly_11_UserAssetOut",
        "FileIn": "_poly_12_FileIn",
        "FileOut": "_poly_13_FileOut",
        "QuaternionIn": "_poly_14_QuaternionIn",
        "QuaternionOut": "_poly_15_QuaternionOut",
        "AssetImportMessageIn": "_poly_16_AssetImportMessageIn",
        "AssetImportMessageOut": "_poly_17_AssetImportMessageOut",
        "ObjParseErrorIn": "_poly_18_ObjParseErrorIn",
        "ObjParseErrorOut": "_poly_19_ObjParseErrorOut",
        "StartAssetImportResponseIn": "_poly_20_StartAssetImportResponseIn",
        "StartAssetImportResponseOut": "_poly_21_StartAssetImportResponseOut",
        "ListAssetsResponseIn": "_poly_22_ListAssetsResponseIn",
        "ListAssetsResponseOut": "_poly_23_ListAssetsResponseOut",
        "ListUserAssetsResponseIn": "_poly_24_ListUserAssetsResponseIn",
        "ListUserAssetsResponseOut": "_poly_25_ListUserAssetsResponseOut",
        "FormatComplexityIn": "_poly_26_FormatComplexityIn",
        "FormatComplexityOut": "_poly_27_FormatComplexityOut",
        "FormatIn": "_poly_28_FormatIn",
        "FormatOut": "_poly_29_FormatOut",
        "ListLikedAssetsResponseIn": "_poly_30_ListLikedAssetsResponseIn",
        "ListLikedAssetsResponseOut": "_poly_31_ListLikedAssetsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["AssetIn"] = t.struct(
        {
            "authorName": t.string().optional(),
            "formats": t.array(t.proxy(renames["FormatIn"])).optional(),
            "name": t.string().optional(),
            "isCurated": t.boolean().optional(),
            "metadata": t.string().optional(),
            "visibility": t.string().optional(),
            "createTime": t.string().optional(),
            "description": t.string().optional(),
            "thumbnail": t.proxy(renames["FileIn"]).optional(),
            "displayName": t.string().optional(),
            "presentationParams": t.proxy(renames["PresentationParamsIn"]).optional(),
            "updateTime": t.string().optional(),
            "license": t.string().optional(),
            "remixInfo": t.proxy(renames["RemixInfoIn"]).optional(),
        }
    ).named(renames["AssetIn"])
    types["AssetOut"] = t.struct(
        {
            "authorName": t.string().optional(),
            "formats": t.array(t.proxy(renames["FormatOut"])).optional(),
            "name": t.string().optional(),
            "isCurated": t.boolean().optional(),
            "metadata": t.string().optional(),
            "visibility": t.string().optional(),
            "createTime": t.string().optional(),
            "description": t.string().optional(),
            "thumbnail": t.proxy(renames["FileOut"]).optional(),
            "displayName": t.string().optional(),
            "presentationParams": t.proxy(renames["PresentationParamsOut"]).optional(),
            "updateTime": t.string().optional(),
            "license": t.string().optional(),
            "remixInfo": t.proxy(renames["RemixInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssetOut"])
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
    types["RemixInfoIn"] = t.struct(
        {"sourceAsset": t.array(t.string()).optional()}
    ).named(renames["RemixInfoIn"])
    types["RemixInfoOut"] = t.struct(
        {
            "sourceAsset": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemixInfoOut"])
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
            "relativePath": t.string().optional(),
            "contentType": t.string().optional(),
            "url": t.string().optional(),
        }
    ).named(renames["FileIn"])
    types["FileOut"] = t.struct(
        {
            "relativePath": t.string().optional(),
            "contentType": t.string().optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileOut"])
    types["QuaternionIn"] = t.struct(
        {
            "w": t.number().optional(),
            "x": t.number().optional(),
            "z": t.number().optional(),
            "y": t.number().optional(),
        }
    ).named(renames["QuaternionIn"])
    types["QuaternionOut"] = t.struct(
        {
            "w": t.number().optional(),
            "x": t.number().optional(),
            "z": t.number().optional(),
            "y": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuaternionOut"])
    types["AssetImportMessageIn"] = t.struct(
        {
            "objParseError": t.proxy(renames["ObjParseErrorIn"]).optional(),
            "filePath": t.string().optional(),
            "code": t.string().optional(),
            "imageError": t.proxy(renames["ImageErrorIn"]).optional(),
        }
    ).named(renames["AssetImportMessageIn"])
    types["AssetImportMessageOut"] = t.struct(
        {
            "objParseError": t.proxy(renames["ObjParseErrorOut"]).optional(),
            "filePath": t.string().optional(),
            "code": t.string().optional(),
            "imageError": t.proxy(renames["ImageErrorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssetImportMessageOut"])
    types["ObjParseErrorIn"] = t.struct(
        {
            "filePath": t.string().optional(),
            "code": t.string().optional(),
            "lineNumber": t.integer().optional(),
            "startIndex": t.integer().optional(),
            "endIndex": t.integer().optional(),
            "line": t.string().optional(),
        }
    ).named(renames["ObjParseErrorIn"])
    types["ObjParseErrorOut"] = t.struct(
        {
            "filePath": t.string().optional(),
            "code": t.string().optional(),
            "lineNumber": t.integer().optional(),
            "startIndex": t.integer().optional(),
            "endIndex": t.integer().optional(),
            "line": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ObjParseErrorOut"])
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
    types["ListAssetsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "assets": t.array(t.proxy(renames["AssetIn"])).optional(),
        }
    ).named(renames["ListAssetsResponseIn"])
    types["ListAssetsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "assets": t.array(t.proxy(renames["AssetOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAssetsResponseOut"])
    types["ListUserAssetsResponseIn"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "userAssets": t.array(t.proxy(renames["UserAssetIn"])).optional(),
        }
    ).named(renames["ListUserAssetsResponseIn"])
    types["ListUserAssetsResponseOut"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "userAssets": t.array(t.proxy(renames["UserAssetOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListUserAssetsResponseOut"])
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
    types["FormatIn"] = t.struct(
        {
            "root": t.proxy(renames["FileIn"]).optional(),
            "formatComplexity": t.proxy(renames["FormatComplexityIn"]).optional(),
            "resources": t.array(t.proxy(renames["FileIn"])).optional(),
            "formatType": t.string().optional(),
        }
    ).named(renames["FormatIn"])
    types["FormatOut"] = t.struct(
        {
            "root": t.proxy(renames["FileOut"]).optional(),
            "formatComplexity": t.proxy(renames["FormatComplexityOut"]).optional(),
            "resources": t.array(t.proxy(renames["FileOut"])).optional(),
            "formatType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FormatOut"])
    types["ListLikedAssetsResponseIn"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "assets": t.array(t.proxy(renames["AssetIn"])).optional(),
        }
    ).named(renames["ListLikedAssetsResponseIn"])
    types["ListLikedAssetsResponseOut"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "assets": t.array(t.proxy(renames["AssetOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLikedAssetsResponseOut"])

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
                "pageSize": t.integer().optional(),
                "visibility": t.string().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "format": t.string().optional(),
                "orderBy": t.string().optional(),
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

    return Import(
        importer="poly", renames=renames, types=Box(types), functions=Box(functions)
    )
