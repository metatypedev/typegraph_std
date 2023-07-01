from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_youtubeAnalytics():
    youtubeAnalytics = HTTPRuntime("https://youtubeanalytics.googleapis.com/")

    renames = {
        "ErrorResponse": "_youtubeAnalytics_1_ErrorResponse",
        "GroupContentDetailsIn": "_youtubeAnalytics_2_GroupContentDetailsIn",
        "GroupContentDetailsOut": "_youtubeAnalytics_3_GroupContentDetailsOut",
        "GroupItemResourceIn": "_youtubeAnalytics_4_GroupItemResourceIn",
        "GroupItemResourceOut": "_youtubeAnalytics_5_GroupItemResourceOut",
        "QueryResponseIn": "_youtubeAnalytics_6_QueryResponseIn",
        "QueryResponseOut": "_youtubeAnalytics_7_QueryResponseOut",
        "ResultTableColumnHeaderIn": "_youtubeAnalytics_8_ResultTableColumnHeaderIn",
        "ResultTableColumnHeaderOut": "_youtubeAnalytics_9_ResultTableColumnHeaderOut",
        "GroupSnippetIn": "_youtubeAnalytics_10_GroupSnippetIn",
        "GroupSnippetOut": "_youtubeAnalytics_11_GroupSnippetOut",
        "ListGroupItemsResponseIn": "_youtubeAnalytics_12_ListGroupItemsResponseIn",
        "ListGroupItemsResponseOut": "_youtubeAnalytics_13_ListGroupItemsResponseOut",
        "ListGroupsResponseIn": "_youtubeAnalytics_14_ListGroupsResponseIn",
        "ListGroupsResponseOut": "_youtubeAnalytics_15_ListGroupsResponseOut",
        "EmptyResponseIn": "_youtubeAnalytics_16_EmptyResponseIn",
        "EmptyResponseOut": "_youtubeAnalytics_17_EmptyResponseOut",
        "ErrorsIn": "_youtubeAnalytics_18_ErrorsIn",
        "ErrorsOut": "_youtubeAnalytics_19_ErrorsOut",
        "GroupItemIn": "_youtubeAnalytics_20_GroupItemIn",
        "GroupItemOut": "_youtubeAnalytics_21_GroupItemOut",
        "GroupIn": "_youtubeAnalytics_22_GroupIn",
        "GroupOut": "_youtubeAnalytics_23_GroupOut",
        "ErrorProtoIn": "_youtubeAnalytics_24_ErrorProtoIn",
        "ErrorProtoOut": "_youtubeAnalytics_25_ErrorProtoOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GroupContentDetailsIn"] = t.struct(
        {"itemType": t.string().optional(), "itemCount": t.string().optional()}
    ).named(renames["GroupContentDetailsIn"])
    types["GroupContentDetailsOut"] = t.struct(
        {
            "itemType": t.string().optional(),
            "itemCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupContentDetailsOut"])
    types["GroupItemResourceIn"] = t.struct(
        {"id": t.string().optional(), "kind": t.string().optional()}
    ).named(renames["GroupItemResourceIn"])
    types["GroupItemResourceOut"] = t.struct(
        {
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupItemResourceOut"])
    types["QueryResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "errors": t.proxy(renames["ErrorsIn"]).optional(),
            "rows": t.array(t.array(t.struct({"_": t.string().optional()}))).optional(),
            "columnHeaders": t.array(
                t.proxy(renames["ResultTableColumnHeaderIn"])
            ).optional(),
        }
    ).named(renames["QueryResponseIn"])
    types["QueryResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "errors": t.proxy(renames["ErrorsOut"]).optional(),
            "rows": t.array(t.array(t.struct({"_": t.string().optional()}))).optional(),
            "columnHeaders": t.array(
                t.proxy(renames["ResultTableColumnHeaderOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryResponseOut"])
    types["ResultTableColumnHeaderIn"] = t.struct(
        {
            "name": t.string().optional(),
            "columnType": t.string().optional(),
            "dataType": t.string().optional(),
        }
    ).named(renames["ResultTableColumnHeaderIn"])
    types["ResultTableColumnHeaderOut"] = t.struct(
        {
            "name": t.string().optional(),
            "columnType": t.string().optional(),
            "dataType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResultTableColumnHeaderOut"])
    types["GroupSnippetIn"] = t.struct(
        {"title": t.string().optional(), "publishedAt": t.string().optional()}
    ).named(renames["GroupSnippetIn"])
    types["GroupSnippetOut"] = t.struct(
        {
            "title": t.string().optional(),
            "publishedAt": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupSnippetOut"])
    types["ListGroupItemsResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["GroupItemIn"])).optional(),
            "errors": t.proxy(renames["ErrorsIn"]).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["ListGroupItemsResponseIn"])
    types["ListGroupItemsResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["GroupItemOut"])).optional(),
            "errors": t.proxy(renames["ErrorsOut"]).optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListGroupItemsResponseOut"])
    types["ListGroupsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "etag": t.string().optional(),
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["GroupIn"])).optional(),
            "errors": t.proxy(renames["ErrorsIn"]).optional(),
        }
    ).named(renames["ListGroupsResponseIn"])
    types["ListGroupsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "etag": t.string().optional(),
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["GroupOut"])).optional(),
            "errors": t.proxy(renames["ErrorsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListGroupsResponseOut"])
    types["EmptyResponseIn"] = t.struct(
        {"errors": t.proxy(renames["ErrorsIn"]).optional()}
    ).named(renames["EmptyResponseIn"])
    types["EmptyResponseOut"] = t.struct(
        {
            "errors": t.proxy(renames["ErrorsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EmptyResponseOut"])
    types["ErrorsIn"] = t.struct(
        {
            "requestId": t.string().optional(),
            "error": t.array(t.proxy(renames["ErrorProtoIn"])).optional(),
            "code": t.string().optional(),
        }
    ).named(renames["ErrorsIn"])
    types["ErrorsOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "code": t.string().optional(),
        }
    ).named(renames["ErrorsOut"])
    types["GroupItemIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "kind": t.string().optional(),
            "errors": t.proxy(renames["ErrorsIn"]).optional(),
            "groupId": t.string().optional(),
            "resource": t.proxy(renames["GroupItemResourceIn"]).optional(),
            "id": t.string().optional(),
        }
    ).named(renames["GroupItemIn"])
    types["GroupItemOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "kind": t.string().optional(),
            "errors": t.proxy(renames["ErrorsOut"]).optional(),
            "groupId": t.string().optional(),
            "resource": t.proxy(renames["GroupItemResourceOut"]).optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupItemOut"])
    types["GroupIn"] = t.struct(
        {
            "id": t.string().optional(),
            "contentDetails": t.proxy(renames["GroupContentDetailsIn"]).optional(),
            "errors": t.proxy(renames["ErrorsIn"]).optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "snippet": t.proxy(renames["GroupSnippetIn"]).optional(),
        }
    ).named(renames["GroupIn"])
    types["GroupOut"] = t.struct(
        {
            "id": t.string().optional(),
            "contentDetails": t.proxy(renames["GroupContentDetailsOut"]).optional(),
            "errors": t.proxy(renames["ErrorsOut"]).optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "snippet": t.proxy(renames["GroupSnippetOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupOut"])
    types["ErrorProtoIn"] = t.struct(
        {
            "externalErrorMessage": t.string().optional(),
            "location": t.string().optional(),
            "domain": t.string().optional(),
            "argument": t.array(t.string()).optional(),
            "code": t.string().optional(),
            "locationType": t.string(),
            "debugInfo": t.string().optional(),
        }
    ).named(renames["ErrorProtoIn"])
    types["ErrorProtoOut"] = t.struct(
        {
            "externalErrorMessage": t.string().optional(),
            "location": t.string().optional(),
            "domain": t.string().optional(),
            "argument": t.array(t.string()).optional(),
            "code": t.string().optional(),
            "locationType": t.string(),
            "debugInfo": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ErrorProtoOut"])

    functions = {}
    functions["groupsUpdate"] = youtubeAnalytics.get(
        "v2/groups",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "mine": t.boolean().optional(),
                "id": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListGroupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsDelete"] = youtubeAnalytics.get(
        "v2/groups",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "mine": t.boolean().optional(),
                "id": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListGroupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsInsert"] = youtubeAnalytics.get(
        "v2/groups",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "mine": t.boolean().optional(),
                "id": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListGroupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsList"] = youtubeAnalytics.get(
        "v2/groups",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "mine": t.boolean().optional(),
                "id": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListGroupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupItemsDelete"] = youtubeAnalytics.get(
        "v2/groupItems",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "groupId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListGroupItemsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupItemsInsert"] = youtubeAnalytics.get(
        "v2/groupItems",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "groupId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListGroupItemsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupItemsList"] = youtubeAnalytics.get(
        "v2/groupItems",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "groupId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListGroupItemsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["reportsQuery"] = youtubeAnalytics.get(
        "v2/reports",
        t.struct(
            {
                "metrics": t.string().optional(),
                "dimensions": t.string().optional(),
                "includeHistoricalChannelData": t.boolean().optional(),
                "startDate": t.string().optional(),
                "filters": t.string().optional(),
                "maxResults": t.integer().optional(),
                "startIndex": t.integer().optional(),
                "sort": t.string().optional(),
                "endDate": t.string().optional(),
                "currency": t.string().optional(),
                "ids": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="youtubeAnalytics",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
