from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_mybusinessplaceactions():
    mybusinessplaceactions = HTTPRuntime(
        "https://mybusinessplaceactions.googleapis.com/"
    )

    renames = {
        "ErrorResponse": "_mybusinessplaceactions_1_ErrorResponse",
        "PlaceActionLinkIn": "_mybusinessplaceactions_2_PlaceActionLinkIn",
        "PlaceActionLinkOut": "_mybusinessplaceactions_3_PlaceActionLinkOut",
        "ListPlaceActionLinksResponseIn": "_mybusinessplaceactions_4_ListPlaceActionLinksResponseIn",
        "ListPlaceActionLinksResponseOut": "_mybusinessplaceactions_5_ListPlaceActionLinksResponseOut",
        "EmptyIn": "_mybusinessplaceactions_6_EmptyIn",
        "EmptyOut": "_mybusinessplaceactions_7_EmptyOut",
        "ListPlaceActionTypeMetadataResponseIn": "_mybusinessplaceactions_8_ListPlaceActionTypeMetadataResponseIn",
        "ListPlaceActionTypeMetadataResponseOut": "_mybusinessplaceactions_9_ListPlaceActionTypeMetadataResponseOut",
        "PlaceActionTypeMetadataIn": "_mybusinessplaceactions_10_PlaceActionTypeMetadataIn",
        "PlaceActionTypeMetadataOut": "_mybusinessplaceactions_11_PlaceActionTypeMetadataOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["PlaceActionLinkIn"] = t.struct(
        {
            "isPreferred": t.boolean().optional(),
            "name": t.string().optional(),
            "placeActionType": t.string(),
            "uri": t.string(),
        }
    ).named(renames["PlaceActionLinkIn"])
    types["PlaceActionLinkOut"] = t.struct(
        {
            "isPreferred": t.boolean().optional(),
            "providerType": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "placeActionType": t.string(),
            "uri": t.string(),
            "updateTime": t.string().optional(),
            "isEditable": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlaceActionLinkOut"])
    types["ListPlaceActionLinksResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "placeActionLinks": t.array(
                t.proxy(renames["PlaceActionLinkIn"])
            ).optional(),
        }
    ).named(renames["ListPlaceActionLinksResponseIn"])
    types["ListPlaceActionLinksResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "placeActionLinks": t.array(
                t.proxy(renames["PlaceActionLinkOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPlaceActionLinksResponseOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ListPlaceActionTypeMetadataResponseIn"] = t.struct(
        {
            "placeActionTypeMetadata": t.array(
                t.proxy(renames["PlaceActionTypeMetadataIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListPlaceActionTypeMetadataResponseIn"])
    types["ListPlaceActionTypeMetadataResponseOut"] = t.struct(
        {
            "placeActionTypeMetadata": t.array(
                t.proxy(renames["PlaceActionTypeMetadataOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPlaceActionTypeMetadataResponseOut"])
    types["PlaceActionTypeMetadataIn"] = t.struct(
        {"displayName": t.string().optional(), "placeActionType": t.string().optional()}
    ).named(renames["PlaceActionTypeMetadataIn"])
    types["PlaceActionTypeMetadataOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "placeActionType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlaceActionTypeMetadataOut"])

    functions = {}
    functions["placeActionTypeMetadataList"] = mybusinessplaceactions.get(
        "v1/placeActionTypeMetadata",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "languageCode": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPlaceActionTypeMetadataResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsPlaceActionLinksCreate"] = mybusinessplaceactions.get(
        "v1/{parent}/placeActionLinks",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPlaceActionLinksResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsPlaceActionLinksGet"] = mybusinessplaceactions.get(
        "v1/{parent}/placeActionLinks",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPlaceActionLinksResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsPlaceActionLinksDelete"] = mybusinessplaceactions.get(
        "v1/{parent}/placeActionLinks",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPlaceActionLinksResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsPlaceActionLinksPatch"] = mybusinessplaceactions.get(
        "v1/{parent}/placeActionLinks",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPlaceActionLinksResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsPlaceActionLinksList"] = mybusinessplaceactions.get(
        "v1/{parent}/placeActionLinks",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPlaceActionLinksResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="mybusinessplaceactions",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
