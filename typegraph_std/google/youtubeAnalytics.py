from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_youtubeAnalytics() -> Import:
    youtubeAnalytics = HTTPRuntime("https://youtubeanalytics.googleapis.com/")

    renames = {
        "ErrorResponse": "_youtubeAnalytics_1_ErrorResponse",
        "GroupSnippetIn": "_youtubeAnalytics_2_GroupSnippetIn",
        "GroupSnippetOut": "_youtubeAnalytics_3_GroupSnippetOut",
        "GroupContentDetailsIn": "_youtubeAnalytics_4_GroupContentDetailsIn",
        "GroupContentDetailsOut": "_youtubeAnalytics_5_GroupContentDetailsOut",
        "GroupItemIn": "_youtubeAnalytics_6_GroupItemIn",
        "GroupItemOut": "_youtubeAnalytics_7_GroupItemOut",
        "QueryResponseIn": "_youtubeAnalytics_8_QueryResponseIn",
        "QueryResponseOut": "_youtubeAnalytics_9_QueryResponseOut",
        "ErrorsIn": "_youtubeAnalytics_10_ErrorsIn",
        "ErrorsOut": "_youtubeAnalytics_11_ErrorsOut",
        "ErrorProtoIn": "_youtubeAnalytics_12_ErrorProtoIn",
        "ErrorProtoOut": "_youtubeAnalytics_13_ErrorProtoOut",
        "GroupItemResourceIn": "_youtubeAnalytics_14_GroupItemResourceIn",
        "GroupItemResourceOut": "_youtubeAnalytics_15_GroupItemResourceOut",
        "ListGroupItemsResponseIn": "_youtubeAnalytics_16_ListGroupItemsResponseIn",
        "ListGroupItemsResponseOut": "_youtubeAnalytics_17_ListGroupItemsResponseOut",
        "ResultTableColumnHeaderIn": "_youtubeAnalytics_18_ResultTableColumnHeaderIn",
        "ResultTableColumnHeaderOut": "_youtubeAnalytics_19_ResultTableColumnHeaderOut",
        "ListGroupsResponseIn": "_youtubeAnalytics_20_ListGroupsResponseIn",
        "ListGroupsResponseOut": "_youtubeAnalytics_21_ListGroupsResponseOut",
        "EmptyResponseIn": "_youtubeAnalytics_22_EmptyResponseIn",
        "EmptyResponseOut": "_youtubeAnalytics_23_EmptyResponseOut",
        "GroupIn": "_youtubeAnalytics_24_GroupIn",
        "GroupOut": "_youtubeAnalytics_25_GroupOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["GroupItemIn"] = t.struct(
        {
            "resource": t.proxy(renames["GroupItemResourceIn"]).optional(),
            "groupId": t.string().optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "etag": t.string().optional(),
            "errors": t.proxy(renames["ErrorsIn"]).optional(),
        }
    ).named(renames["GroupItemIn"])
    types["GroupItemOut"] = t.struct(
        {
            "resource": t.proxy(renames["GroupItemResourceOut"]).optional(),
            "groupId": t.string().optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "etag": t.string().optional(),
            "errors": t.proxy(renames["ErrorsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupItemOut"])
    types["QueryResponseIn"] = t.struct(
        {
            "columnHeaders": t.array(
                t.proxy(renames["ResultTableColumnHeaderIn"])
            ).optional(),
            "kind": t.string().optional(),
            "errors": t.proxy(renames["ErrorsIn"]).optional(),
            "rows": t.array(t.array(t.struct({"_": t.string().optional()}))).optional(),
        }
    ).named(renames["QueryResponseIn"])
    types["QueryResponseOut"] = t.struct(
        {
            "columnHeaders": t.array(
                t.proxy(renames["ResultTableColumnHeaderOut"])
            ).optional(),
            "kind": t.string().optional(),
            "errors": t.proxy(renames["ErrorsOut"]).optional(),
            "rows": t.array(t.array(t.struct({"_": t.string().optional()}))).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryResponseOut"])
    types["ErrorsIn"] = t.struct(
        {
            "code": t.string().optional(),
            "error": t.array(t.proxy(renames["ErrorProtoIn"])).optional(),
            "requestId": t.string().optional(),
        }
    ).named(renames["ErrorsIn"])
    types["ErrorsOut"] = t.struct(
        {
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "requestId": t.string().optional(),
        }
    ).named(renames["ErrorsOut"])
    types["ErrorProtoIn"] = t.struct(
        {
            "argument": t.array(t.string()).optional(),
            "locationType": t.string(),
            "domain": t.string().optional(),
            "debugInfo": t.string().optional(),
            "code": t.string().optional(),
            "externalErrorMessage": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["ErrorProtoIn"])
    types["ErrorProtoOut"] = t.struct(
        {
            "argument": t.array(t.string()).optional(),
            "locationType": t.string(),
            "domain": t.string().optional(),
            "debugInfo": t.string().optional(),
            "code": t.string().optional(),
            "externalErrorMessage": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ErrorProtoOut"])
    types["GroupItemResourceIn"] = t.struct(
        {"kind": t.string().optional(), "id": t.string().optional()}
    ).named(renames["GroupItemResourceIn"])
    types["GroupItemResourceOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupItemResourceOut"])
    types["ListGroupItemsResponseIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["GroupItemIn"])).optional(),
            "errors": t.proxy(renames["ErrorsIn"]).optional(),
            "etag": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ListGroupItemsResponseIn"])
    types["ListGroupItemsResponseOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["GroupItemOut"])).optional(),
            "errors": t.proxy(renames["ErrorsOut"]).optional(),
            "etag": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListGroupItemsResponseOut"])
    types["ResultTableColumnHeaderIn"] = t.struct(
        {
            "columnType": t.string().optional(),
            "dataType": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ResultTableColumnHeaderIn"])
    types["ResultTableColumnHeaderOut"] = t.struct(
        {
            "columnType": t.string().optional(),
            "dataType": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResultTableColumnHeaderOut"])
    types["ListGroupsResponseIn"] = t.struct(
        {
            "errors": t.proxy(renames["ErrorsIn"]).optional(),
            "etag": t.string().optional(),
            "items": t.array(t.proxy(renames["GroupIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ListGroupsResponseIn"])
    types["ListGroupsResponseOut"] = t.struct(
        {
            "errors": t.proxy(renames["ErrorsOut"]).optional(),
            "etag": t.string().optional(),
            "items": t.array(t.proxy(renames["GroupOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
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
    types["GroupIn"] = t.struct(
        {
            "snippet": t.proxy(renames["GroupSnippetIn"]).optional(),
            "kind": t.string().optional(),
            "contentDetails": t.proxy(renames["GroupContentDetailsIn"]).optional(),
            "etag": t.string().optional(),
            "errors": t.proxy(renames["ErrorsIn"]).optional(),
            "id": t.string().optional(),
        }
    ).named(renames["GroupIn"])
    types["GroupOut"] = t.struct(
        {
            "snippet": t.proxy(renames["GroupSnippetOut"]).optional(),
            "kind": t.string().optional(),
            "contentDetails": t.proxy(renames["GroupContentDetailsOut"]).optional(),
            "etag": t.string().optional(),
            "errors": t.proxy(renames["ErrorsOut"]).optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupOut"])

    functions = {}
    functions["groupItemsDelete"] = youtubeAnalytics.get(
        "v2/groupItems",
        t.struct(
            {
                "groupId": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
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
                "groupId": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
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
                "groupId": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListGroupItemsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsDelete"] = youtubeAnalytics.put(
        "v2/groups",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "snippet": t.proxy(renames["GroupSnippetIn"]).optional(),
                "kind": t.string().optional(),
                "contentDetails": t.proxy(renames["GroupContentDetailsIn"]).optional(),
                "etag": t.string().optional(),
                "errors": t.proxy(renames["ErrorsIn"]).optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsList"] = youtubeAnalytics.put(
        "v2/groups",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "snippet": t.proxy(renames["GroupSnippetIn"]).optional(),
                "kind": t.string().optional(),
                "contentDetails": t.proxy(renames["GroupContentDetailsIn"]).optional(),
                "etag": t.string().optional(),
                "errors": t.proxy(renames["ErrorsIn"]).optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsInsert"] = youtubeAnalytics.put(
        "v2/groups",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "snippet": t.proxy(renames["GroupSnippetIn"]).optional(),
                "kind": t.string().optional(),
                "contentDetails": t.proxy(renames["GroupContentDetailsIn"]).optional(),
                "etag": t.string().optional(),
                "errors": t.proxy(renames["ErrorsIn"]).optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsUpdate"] = youtubeAnalytics.put(
        "v2/groups",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "snippet": t.proxy(renames["GroupSnippetIn"]).optional(),
                "kind": t.string().optional(),
                "contentDetails": t.proxy(renames["GroupContentDetailsIn"]).optional(),
                "etag": t.string().optional(),
                "errors": t.proxy(renames["ErrorsIn"]).optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["reportsQuery"] = youtubeAnalytics.get(
        "v2/reports",
        t.struct(
            {
                "currency": t.string().optional(),
                "includeHistoricalChannelData": t.boolean().optional(),
                "startIndex": t.integer().optional(),
                "filters": t.string().optional(),
                "dimensions": t.string().optional(),
                "ids": t.string().optional(),
                "maxResults": t.integer().optional(),
                "metrics": t.string().optional(),
                "endDate": t.string().optional(),
                "startDate": t.string().optional(),
                "sort": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="youtubeAnalytics", renames=renames, types=types, functions=functions
    )
