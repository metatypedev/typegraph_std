from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_mybusinessplaceactions() -> Import:
    mybusinessplaceactions = HTTPRuntime(
        "https://mybusinessplaceactions.googleapis.com/"
    )

    renames = {
        "ErrorResponse": "_mybusinessplaceactions_1_ErrorResponse",
        "EmptyIn": "_mybusinessplaceactions_2_EmptyIn",
        "EmptyOut": "_mybusinessplaceactions_3_EmptyOut",
        "PlaceActionTypeMetadataIn": "_mybusinessplaceactions_4_PlaceActionTypeMetadataIn",
        "PlaceActionTypeMetadataOut": "_mybusinessplaceactions_5_PlaceActionTypeMetadataOut",
        "PlaceActionLinkIn": "_mybusinessplaceactions_6_PlaceActionLinkIn",
        "PlaceActionLinkOut": "_mybusinessplaceactions_7_PlaceActionLinkOut",
        "ListPlaceActionTypeMetadataResponseIn": "_mybusinessplaceactions_8_ListPlaceActionTypeMetadataResponseIn",
        "ListPlaceActionTypeMetadataResponseOut": "_mybusinessplaceactions_9_ListPlaceActionTypeMetadataResponseOut",
        "ListPlaceActionLinksResponseIn": "_mybusinessplaceactions_10_ListPlaceActionLinksResponseIn",
        "ListPlaceActionLinksResponseOut": "_mybusinessplaceactions_11_ListPlaceActionLinksResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
            "name": t.string().optional(),
            "placeActionType": t.string(),
            "isPreferred": t.boolean().optional(),
            "uri": t.string(),
        }
    ).named(renames["PlaceActionLinkIn"])
    types["PlaceActionLinkOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "providerType": t.string().optional(),
            "name": t.string().optional(),
            "isEditable": t.boolean().optional(),
            "placeActionType": t.string(),
            "isPreferred": t.boolean().optional(),
            "uri": t.string(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlaceActionLinkOut"])
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

    functions = {}
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
    functions["locationsPlaceActionLinksDelete"] = mybusinessplaceactions.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["placeActionTypeMetadataList"] = mybusinessplaceactions.get(
        "v1/placeActionTypeMetadata",
        t.struct(
            {
                "filter": t.string().optional(),
                "languageCode": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
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
        types=types,
        functions=functions,
    )
