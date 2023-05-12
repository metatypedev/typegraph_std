from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_mybusinessplaceactions() -> Import:
    mybusinessplaceactions = HTTPRuntime(
        "https://mybusinessplaceactions.googleapis.com/"
    )

    renames = {
        "ErrorResponse": "_mybusinessplaceactions_1_ErrorResponse",
        "EmptyIn": "_mybusinessplaceactions_2_EmptyIn",
        "EmptyOut": "_mybusinessplaceactions_3_EmptyOut",
        "ListPlaceActionTypeMetadataResponseIn": "_mybusinessplaceactions_4_ListPlaceActionTypeMetadataResponseIn",
        "ListPlaceActionTypeMetadataResponseOut": "_mybusinessplaceactions_5_ListPlaceActionTypeMetadataResponseOut",
        "ListPlaceActionLinksResponseIn": "_mybusinessplaceactions_6_ListPlaceActionLinksResponseIn",
        "ListPlaceActionLinksResponseOut": "_mybusinessplaceactions_7_ListPlaceActionLinksResponseOut",
        "PlaceActionTypeMetadataIn": "_mybusinessplaceactions_8_PlaceActionTypeMetadataIn",
        "PlaceActionTypeMetadataOut": "_mybusinessplaceactions_9_PlaceActionTypeMetadataOut",
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
    types["PlaceActionLinkIn"] = t.struct(
        {
            "placeActionType": t.string(),
            "uri": t.string(),
            "isPreferred": t.boolean().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["PlaceActionLinkIn"])
    types["PlaceActionLinkOut"] = t.struct(
        {
            "isEditable": t.boolean().optional(),
            "providerType": t.string().optional(),
            "placeActionType": t.string(),
            "uri": t.string(),
            "createTime": t.string().optional(),
            "isPreferred": t.boolean().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlaceActionLinkOut"])

    functions = {}
    functions["locationsPlaceActionLinksPatch"] = mybusinessplaceactions.get(
        "v1/{parent}/placeActionLinks",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPlaceActionLinksResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsPlaceActionLinksCreate"] = mybusinessplaceactions.get(
        "v1/{parent}/placeActionLinks",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPlaceActionLinksResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["placeActionTypeMetadataList"] = mybusinessplaceactions.get(
        "v1/placeActionTypeMetadata",
        t.struct(
            {
                "languageCode": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPlaceActionTypeMetadataResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="mybusinessplaceactions",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
