from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_youtubeAnalytics() -> Import:
    youtubeAnalytics = HTTPRuntime("https://youtubeanalytics.googleapis.com/")

    renames = {
        "ErrorResponse": "_youtubeAnalytics_1_ErrorResponse",
        "QueryResponseIn": "_youtubeAnalytics_2_QueryResponseIn",
        "QueryResponseOut": "_youtubeAnalytics_3_QueryResponseOut",
        "GroupItemIn": "_youtubeAnalytics_4_GroupItemIn",
        "GroupItemOut": "_youtubeAnalytics_5_GroupItemOut",
        "EmptyResponseIn": "_youtubeAnalytics_6_EmptyResponseIn",
        "EmptyResponseOut": "_youtubeAnalytics_7_EmptyResponseOut",
        "GroupContentDetailsIn": "_youtubeAnalytics_8_GroupContentDetailsIn",
        "GroupContentDetailsOut": "_youtubeAnalytics_9_GroupContentDetailsOut",
        "ResultTableColumnHeaderIn": "_youtubeAnalytics_10_ResultTableColumnHeaderIn",
        "ResultTableColumnHeaderOut": "_youtubeAnalytics_11_ResultTableColumnHeaderOut",
        "GroupItemResourceIn": "_youtubeAnalytics_12_GroupItemResourceIn",
        "GroupItemResourceOut": "_youtubeAnalytics_13_GroupItemResourceOut",
        "ErrorsIn": "_youtubeAnalytics_14_ErrorsIn",
        "ErrorsOut": "_youtubeAnalytics_15_ErrorsOut",
        "GroupIn": "_youtubeAnalytics_16_GroupIn",
        "GroupOut": "_youtubeAnalytics_17_GroupOut",
        "ErrorProtoIn": "_youtubeAnalytics_18_ErrorProtoIn",
        "ErrorProtoOut": "_youtubeAnalytics_19_ErrorProtoOut",
        "GroupSnippetIn": "_youtubeAnalytics_20_GroupSnippetIn",
        "GroupSnippetOut": "_youtubeAnalytics_21_GroupSnippetOut",
        "ListGroupsResponseIn": "_youtubeAnalytics_22_ListGroupsResponseIn",
        "ListGroupsResponseOut": "_youtubeAnalytics_23_ListGroupsResponseOut",
        "ListGroupItemsResponseIn": "_youtubeAnalytics_24_ListGroupItemsResponseIn",
        "ListGroupItemsResponseOut": "_youtubeAnalytics_25_ListGroupItemsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["QueryResponseIn"] = t.struct(
        {
            "rows": t.array(t.array(t.struct({"_": t.string().optional()}))).optional(),
            "kind": t.string().optional(),
            "columnHeaders": t.array(
                t.proxy(renames["ResultTableColumnHeaderIn"])
            ).optional(),
            "errors": t.proxy(renames["ErrorsIn"]).optional(),
        }
    ).named(renames["QueryResponseIn"])
    types["QueryResponseOut"] = t.struct(
        {
            "rows": t.array(t.array(t.struct({"_": t.string().optional()}))).optional(),
            "kind": t.string().optional(),
            "columnHeaders": t.array(
                t.proxy(renames["ResultTableColumnHeaderOut"])
            ).optional(),
            "errors": t.proxy(renames["ErrorsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryResponseOut"])
    types["GroupItemIn"] = t.struct(
        {
            "groupId": t.string().optional(),
            "kind": t.string().optional(),
            "errors": t.proxy(renames["ErrorsIn"]).optional(),
            "id": t.string().optional(),
            "resource": t.proxy(renames["GroupItemResourceIn"]).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["GroupItemIn"])
    types["GroupItemOut"] = t.struct(
        {
            "groupId": t.string().optional(),
            "kind": t.string().optional(),
            "errors": t.proxy(renames["ErrorsOut"]).optional(),
            "id": t.string().optional(),
            "resource": t.proxy(renames["GroupItemResourceOut"]).optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupItemOut"])
    types["EmptyResponseIn"] = t.struct(
        {"errors": t.proxy(renames["ErrorsIn"]).optional()}
    ).named(renames["EmptyResponseIn"])
    types["EmptyResponseOut"] = t.struct(
        {
            "errors": t.proxy(renames["ErrorsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EmptyResponseOut"])
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
    types["ResultTableColumnHeaderIn"] = t.struct(
        {
            "name": t.string().optional(),
            "dataType": t.string().optional(),
            "columnType": t.string().optional(),
        }
    ).named(renames["ResultTableColumnHeaderIn"])
    types["ResultTableColumnHeaderOut"] = t.struct(
        {
            "name": t.string().optional(),
            "dataType": t.string().optional(),
            "columnType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResultTableColumnHeaderOut"])
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
    types["ErrorsIn"] = t.struct(
        {
            "error": t.array(t.proxy(renames["ErrorProtoIn"])).optional(),
            "code": t.string().optional(),
            "requestId": t.string().optional(),
        }
    ).named(renames["ErrorsIn"])
    types["ErrorsOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "code": t.string().optional(),
            "requestId": t.string().optional(),
        }
    ).named(renames["ErrorsOut"])
    types["GroupIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "id": t.string().optional(),
            "errors": t.proxy(renames["ErrorsIn"]).optional(),
            "kind": t.string().optional(),
            "snippet": t.proxy(renames["GroupSnippetIn"]).optional(),
            "contentDetails": t.proxy(renames["GroupContentDetailsIn"]).optional(),
        }
    ).named(renames["GroupIn"])
    types["GroupOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "id": t.string().optional(),
            "errors": t.proxy(renames["ErrorsOut"]).optional(),
            "kind": t.string().optional(),
            "snippet": t.proxy(renames["GroupSnippetOut"]).optional(),
            "contentDetails": t.proxy(renames["GroupContentDetailsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupOut"])
    types["ErrorProtoIn"] = t.struct(
        {
            "domain": t.string().optional(),
            "debugInfo": t.string().optional(),
            "argument": t.array(t.string()).optional(),
            "externalErrorMessage": t.string().optional(),
            "locationType": t.string(),
            "location": t.string().optional(),
            "code": t.string().optional(),
        }
    ).named(renames["ErrorProtoIn"])
    types["ErrorProtoOut"] = t.struct(
        {
            "domain": t.string().optional(),
            "debugInfo": t.string().optional(),
            "argument": t.array(t.string()).optional(),
            "externalErrorMessage": t.string().optional(),
            "locationType": t.string(),
            "location": t.string().optional(),
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ErrorProtoOut"])
    types["GroupSnippetIn"] = t.struct(
        {"publishedAt": t.string().optional(), "title": t.string().optional()}
    ).named(renames["GroupSnippetIn"])
    types["GroupSnippetOut"] = t.struct(
        {
            "publishedAt": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupSnippetOut"])
    types["ListGroupsResponseIn"] = t.struct(
        {
            "errors": t.proxy(renames["ErrorsIn"]).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "etag": t.string().optional(),
            "items": t.array(t.proxy(renames["GroupIn"])).optional(),
        }
    ).named(renames["ListGroupsResponseIn"])
    types["ListGroupsResponseOut"] = t.struct(
        {
            "errors": t.proxy(renames["ErrorsOut"]).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "etag": t.string().optional(),
            "items": t.array(t.proxy(renames["GroupOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListGroupsResponseOut"])
    types["ListGroupItemsResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "errors": t.proxy(renames["ErrorsIn"]).optional(),
            "items": t.array(t.proxy(renames["GroupItemIn"])).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["ListGroupItemsResponseIn"])
    types["ListGroupItemsResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "errors": t.proxy(renames["ErrorsOut"]).optional(),
            "items": t.array(t.proxy(renames["GroupItemOut"])).optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListGroupItemsResponseOut"])

    functions = {}
    functions["groupItemsList"] = youtubeAnalytics.delete(
        "v2/groupItems",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupItemsInsert"] = youtubeAnalytics.delete(
        "v2/groupItems",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupItemsDelete"] = youtubeAnalytics.delete(
        "v2/groupItems",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsUpdate"] = youtubeAnalytics.post(
        "v2/groups",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "etag": t.string().optional(),
                "id": t.string().optional(),
                "errors": t.proxy(renames["ErrorsIn"]).optional(),
                "kind": t.string().optional(),
                "snippet": t.proxy(renames["GroupSnippetIn"]).optional(),
                "contentDetails": t.proxy(renames["GroupContentDetailsIn"]).optional(),
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
                "etag": t.string().optional(),
                "id": t.string().optional(),
                "errors": t.proxy(renames["ErrorsIn"]).optional(),
                "kind": t.string().optional(),
                "snippet": t.proxy(renames["GroupSnippetIn"]).optional(),
                "contentDetails": t.proxy(renames["GroupContentDetailsIn"]).optional(),
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
                "etag": t.string().optional(),
                "id": t.string().optional(),
                "errors": t.proxy(renames["ErrorsIn"]).optional(),
                "kind": t.string().optional(),
                "snippet": t.proxy(renames["GroupSnippetIn"]).optional(),
                "contentDetails": t.proxy(renames["GroupContentDetailsIn"]).optional(),
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
                "etag": t.string().optional(),
                "id": t.string().optional(),
                "errors": t.proxy(renames["ErrorsIn"]).optional(),
                "kind": t.string().optional(),
                "snippet": t.proxy(renames["GroupSnippetIn"]).optional(),
                "contentDetails": t.proxy(renames["GroupContentDetailsIn"]).optional(),
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
                "startIndex": t.integer().optional(),
                "currency": t.string().optional(),
                "dimensions": t.string().optional(),
                "sort": t.string().optional(),
                "metrics": t.string().optional(),
                "startDate": t.string().optional(),
                "filters": t.string().optional(),
                "maxResults": t.integer().optional(),
                "endDate": t.string().optional(),
                "includeHistoricalChannelData": t.boolean().optional(),
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
