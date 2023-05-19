from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


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
        "ListGroupsResponseIn": "_youtubeAnalytics_8_ListGroupsResponseIn",
        "ListGroupsResponseOut": "_youtubeAnalytics_9_ListGroupsResponseOut",
        "QueryResponseIn": "_youtubeAnalytics_10_QueryResponseIn",
        "QueryResponseOut": "_youtubeAnalytics_11_QueryResponseOut",
        "ResultTableColumnHeaderIn": "_youtubeAnalytics_12_ResultTableColumnHeaderIn",
        "ResultTableColumnHeaderOut": "_youtubeAnalytics_13_ResultTableColumnHeaderOut",
        "GroupItemResourceIn": "_youtubeAnalytics_14_GroupItemResourceIn",
        "GroupItemResourceOut": "_youtubeAnalytics_15_GroupItemResourceOut",
        "ErrorProtoIn": "_youtubeAnalytics_16_ErrorProtoIn",
        "ErrorProtoOut": "_youtubeAnalytics_17_ErrorProtoOut",
        "ErrorsIn": "_youtubeAnalytics_18_ErrorsIn",
        "ErrorsOut": "_youtubeAnalytics_19_ErrorsOut",
        "GroupIn": "_youtubeAnalytics_20_GroupIn",
        "GroupOut": "_youtubeAnalytics_21_GroupOut",
        "EmptyResponseIn": "_youtubeAnalytics_22_EmptyResponseIn",
        "EmptyResponseOut": "_youtubeAnalytics_23_EmptyResponseOut",
        "ListGroupItemsResponseIn": "_youtubeAnalytics_24_ListGroupItemsResponseIn",
        "ListGroupItemsResponseOut": "_youtubeAnalytics_25_ListGroupItemsResponseOut",
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
        {"itemCount": t.string().optional(), "itemType": t.string().optional()}
    ).named(renames["GroupContentDetailsIn"])
    types["GroupContentDetailsOut"] = t.struct(
        {
            "itemCount": t.string().optional(),
            "itemType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupContentDetailsOut"])
    types["GroupItemIn"] = t.struct(
        {
            "groupId": t.string().optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "errors": t.proxy(renames["ErrorsIn"]).optional(),
            "resource": t.proxy(renames["GroupItemResourceIn"]).optional(),
            "id": t.string().optional(),
        }
    ).named(renames["GroupItemIn"])
    types["GroupItemOut"] = t.struct(
        {
            "groupId": t.string().optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "errors": t.proxy(renames["ErrorsOut"]).optional(),
            "resource": t.proxy(renames["GroupItemResourceOut"]).optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupItemOut"])
    types["ListGroupsResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "etag": t.string().optional(),
            "items": t.array(t.proxy(renames["GroupIn"])).optional(),
            "errors": t.proxy(renames["ErrorsIn"]).optional(),
        }
    ).named(renames["ListGroupsResponseIn"])
    types["ListGroupsResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "etag": t.string().optional(),
            "items": t.array(t.proxy(renames["GroupOut"])).optional(),
            "errors": t.proxy(renames["ErrorsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListGroupsResponseOut"])
    types["QueryResponseIn"] = t.struct(
        {
            "errors": t.proxy(renames["ErrorsIn"]).optional(),
            "columnHeaders": t.array(
                t.proxy(renames["ResultTableColumnHeaderIn"])
            ).optional(),
            "rows": t.array(t.array(t.struct({"_": t.string().optional()}))).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["QueryResponseIn"])
    types["QueryResponseOut"] = t.struct(
        {
            "errors": t.proxy(renames["ErrorsOut"]).optional(),
            "columnHeaders": t.array(
                t.proxy(renames["ResultTableColumnHeaderOut"])
            ).optional(),
            "rows": t.array(t.array(t.struct({"_": t.string().optional()}))).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryResponseOut"])
    types["ResultTableColumnHeaderIn"] = t.struct(
        {
            "dataType": t.string().optional(),
            "columnType": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ResultTableColumnHeaderIn"])
    types["ResultTableColumnHeaderOut"] = t.struct(
        {
            "dataType": t.string().optional(),
            "columnType": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResultTableColumnHeaderOut"])
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
    types["ErrorProtoIn"] = t.struct(
        {
            "argument": t.array(t.string()).optional(),
            "domain": t.string().optional(),
            "debugInfo": t.string().optional(),
            "code": t.string().optional(),
            "location": t.string().optional(),
            "locationType": t.string(),
            "externalErrorMessage": t.string().optional(),
        }
    ).named(renames["ErrorProtoIn"])
    types["ErrorProtoOut"] = t.struct(
        {
            "argument": t.array(t.string()).optional(),
            "domain": t.string().optional(),
            "debugInfo": t.string().optional(),
            "code": t.string().optional(),
            "location": t.string().optional(),
            "locationType": t.string(),
            "externalErrorMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ErrorProtoOut"])
    types["ErrorsIn"] = t.struct(
        {
            "requestId": t.string().optional(),
            "code": t.string().optional(),
            "error": t.array(t.proxy(renames["ErrorProtoIn"])).optional(),
        }
    ).named(renames["ErrorsIn"])
    types["ErrorsOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ErrorsOut"])
    types["GroupIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "contentDetails": t.proxy(renames["GroupContentDetailsIn"]).optional(),
            "snippet": t.proxy(renames["GroupSnippetIn"]).optional(),
            "id": t.string().optional(),
            "errors": t.proxy(renames["ErrorsIn"]).optional(),
        }
    ).named(renames["GroupIn"])
    types["GroupOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "contentDetails": t.proxy(renames["GroupContentDetailsOut"]).optional(),
            "snippet": t.proxy(renames["GroupSnippetOut"]).optional(),
            "id": t.string().optional(),
            "errors": t.proxy(renames["ErrorsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupOut"])
    types["EmptyResponseIn"] = t.struct(
        {"errors": t.proxy(renames["ErrorsIn"]).optional()}
    ).named(renames["EmptyResponseIn"])
    types["EmptyResponseOut"] = t.struct(
        {
            "errors": t.proxy(renames["ErrorsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EmptyResponseOut"])
    types["ListGroupItemsResponseIn"] = t.struct(
        {
            "errors": t.proxy(renames["ErrorsIn"]).optional(),
            "etag": t.string().optional(),
            "items": t.array(t.proxy(renames["GroupItemIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ListGroupItemsResponseIn"])
    types["ListGroupItemsResponseOut"] = t.struct(
        {
            "errors": t.proxy(renames["ErrorsOut"]).optional(),
            "etag": t.string().optional(),
            "items": t.array(t.proxy(renames["GroupItemOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListGroupItemsResponseOut"])

    functions = {}
    functions["reportsQuery"] = youtubeAnalytics.get(
        "v2/reports",
        t.struct(
            {
                "startIndex": t.integer().optional(),
                "maxResults": t.integer().optional(),
                "filters": t.string().optional(),
                "dimensions": t.string().optional(),
                "sort": t.string().optional(),
                "currency": t.string().optional(),
                "startDate": t.string().optional(),
                "endDate": t.string().optional(),
                "metrics": t.string().optional(),
                "includeHistoricalChannelData": t.boolean().optional(),
                "ids": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupItemsList"] = youtubeAnalytics.post(
        "v2/groupItems",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "groupId": t.string().optional(),
                "kind": t.string().optional(),
                "etag": t.string().optional(),
                "errors": t.proxy(renames["ErrorsIn"]).optional(),
                "resource": t.proxy(renames["GroupItemResourceIn"]).optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GroupItemOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupItemsDelete"] = youtubeAnalytics.post(
        "v2/groupItems",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "groupId": t.string().optional(),
                "kind": t.string().optional(),
                "etag": t.string().optional(),
                "errors": t.proxy(renames["ErrorsIn"]).optional(),
                "resource": t.proxy(renames["GroupItemResourceIn"]).optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GroupItemOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupItemsInsert"] = youtubeAnalytics.post(
        "v2/groupItems",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "groupId": t.string().optional(),
                "kind": t.string().optional(),
                "etag": t.string().optional(),
                "errors": t.proxy(renames["ErrorsIn"]).optional(),
                "resource": t.proxy(renames["GroupItemResourceIn"]).optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GroupItemOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsUpdate"] = youtubeAnalytics.post(
        "v2/groups",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "kind": t.string().optional(),
                "etag": t.string().optional(),
                "contentDetails": t.proxy(renames["GroupContentDetailsIn"]).optional(),
                "snippet": t.proxy(renames["GroupSnippetIn"]).optional(),
                "id": t.string().optional(),
                "errors": t.proxy(renames["ErrorsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsDelete"] = youtubeAnalytics.post(
        "v2/groups",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "kind": t.string().optional(),
                "etag": t.string().optional(),
                "contentDetails": t.proxy(renames["GroupContentDetailsIn"]).optional(),
                "snippet": t.proxy(renames["GroupSnippetIn"]).optional(),
                "id": t.string().optional(),
                "errors": t.proxy(renames["ErrorsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsList"] = youtubeAnalytics.post(
        "v2/groups",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "kind": t.string().optional(),
                "etag": t.string().optional(),
                "contentDetails": t.proxy(renames["GroupContentDetailsIn"]).optional(),
                "snippet": t.proxy(renames["GroupSnippetIn"]).optional(),
                "id": t.string().optional(),
                "errors": t.proxy(renames["ErrorsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsInsert"] = youtubeAnalytics.post(
        "v2/groups",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "kind": t.string().optional(),
                "etag": t.string().optional(),
                "contentDetails": t.proxy(renames["GroupContentDetailsIn"]).optional(),
                "snippet": t.proxy(renames["GroupSnippetIn"]).optional(),
                "id": t.string().optional(),
                "errors": t.proxy(renames["ErrorsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="youtubeAnalytics",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
