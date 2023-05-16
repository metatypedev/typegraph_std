from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_mybusinessplaceactions() -> Import:
    mybusinessplaceactions = HTTPRuntime(
        "https://mybusinessplaceactions.googleapis.com/"
    )

    renames = {
        "ErrorResponse": "_mybusinessplaceactions_1_ErrorResponse",
        "EmptyIn": "_mybusinessplaceactions_2_EmptyIn",
        "EmptyOut": "_mybusinessplaceactions_3_EmptyOut",
        "ListPlaceActionLinksResponseIn": "_mybusinessplaceactions_4_ListPlaceActionLinksResponseIn",
        "ListPlaceActionLinksResponseOut": "_mybusinessplaceactions_5_ListPlaceActionLinksResponseOut",
        "PlaceActionTypeMetadataIn": "_mybusinessplaceactions_6_PlaceActionTypeMetadataIn",
        "PlaceActionTypeMetadataOut": "_mybusinessplaceactions_7_PlaceActionTypeMetadataOut",
        "ListPlaceActionTypeMetadataResponseIn": "_mybusinessplaceactions_8_ListPlaceActionTypeMetadataResponseIn",
        "ListPlaceActionTypeMetadataResponseOut": "_mybusinessplaceactions_9_ListPlaceActionTypeMetadataResponseOut",
        "PlaceActionLinkIn": "_mybusinessplaceactions_10_PlaceActionLinkIn",
        "PlaceActionLinkOut": "_mybusinessplaceactions_11_PlaceActionLinkOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ListPlaceActionLinksResponseIn"] = t.struct(
        {
            "placeActionLinks": t.array(
                t.proxy(renames["PlaceActionLinkIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListPlaceActionLinksResponseIn"])
    types["ListPlaceActionLinksResponseOut"] = t.struct(
        {
            "placeActionLinks": t.array(
                t.proxy(renames["PlaceActionLinkOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPlaceActionLinksResponseOut"])
    types["PlaceActionTypeMetadataIn"] = t.struct(
        {"placeActionType": t.string().optional(), "displayName": t.string().optional()}
    ).named(renames["PlaceActionTypeMetadataIn"])
    types["PlaceActionTypeMetadataOut"] = t.struct(
        {
            "placeActionType": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlaceActionTypeMetadataOut"])
    types["ListPlaceActionTypeMetadataResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "placeActionTypeMetadata": t.array(
                t.proxy(renames["PlaceActionTypeMetadataIn"])
            ).optional(),
        }
    ).named(renames["ListPlaceActionTypeMetadataResponseIn"])
    types["ListPlaceActionTypeMetadataResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "placeActionTypeMetadata": t.array(
                t.proxy(renames["PlaceActionTypeMetadataOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPlaceActionTypeMetadataResponseOut"])
    types["PlaceActionLinkIn"] = t.struct(
        {
            "isPreferred": t.boolean().optional(),
            "placeActionType": t.string(),
            "uri": t.string(),
            "name": t.string().optional(),
        }
    ).named(renames["PlaceActionLinkIn"])
    types["PlaceActionLinkOut"] = t.struct(
        {
            "isPreferred": t.boolean().optional(),
            "isEditable": t.boolean().optional(),
            "providerType": t.string().optional(),
            "placeActionType": t.string(),
            "updateTime": t.string().optional(),
            "uri": t.string(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlaceActionLinkOut"])

    functions = {}
    functions["placeActionTypeMetadataList"] = mybusinessplaceactions.get(
        "v1/placeActionTypeMetadata",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "languageCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPlaceActionTypeMetadataResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsPlaceActionLinksList"] = mybusinessplaceactions.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsPlaceActionLinksPatch"] = mybusinessplaceactions.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsPlaceActionLinksCreate"] = mybusinessplaceactions.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsPlaceActionLinksGet"] = mybusinessplaceactions.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsPlaceActionLinksDelete"] = mybusinessplaceactions.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="mybusinessplaceactions",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
