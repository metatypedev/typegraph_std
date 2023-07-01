from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_essentialcontacts():
    essentialcontacts = HTTPRuntime("https://essentialcontacts.googleapis.com/")

    renames = {
        "ErrorResponse": "_essentialcontacts_1_ErrorResponse",
        "GoogleCloudEssentialcontactsV1ComputeContactsResponseIn": "_essentialcontacts_2_GoogleCloudEssentialcontactsV1ComputeContactsResponseIn",
        "GoogleCloudEssentialcontactsV1ComputeContactsResponseOut": "_essentialcontacts_3_GoogleCloudEssentialcontactsV1ComputeContactsResponseOut",
        "GoogleCloudEssentialcontactsV1ContactIn": "_essentialcontacts_4_GoogleCloudEssentialcontactsV1ContactIn",
        "GoogleCloudEssentialcontactsV1ContactOut": "_essentialcontacts_5_GoogleCloudEssentialcontactsV1ContactOut",
        "GoogleProtobufEmptyIn": "_essentialcontacts_6_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_essentialcontacts_7_GoogleProtobufEmptyOut",
        "GoogleCloudEssentialcontactsV1ListContactsResponseIn": "_essentialcontacts_8_GoogleCloudEssentialcontactsV1ListContactsResponseIn",
        "GoogleCloudEssentialcontactsV1ListContactsResponseOut": "_essentialcontacts_9_GoogleCloudEssentialcontactsV1ListContactsResponseOut",
        "GoogleCloudEssentialcontactsV1SendTestMessageRequestIn": "_essentialcontacts_10_GoogleCloudEssentialcontactsV1SendTestMessageRequestIn",
        "GoogleCloudEssentialcontactsV1SendTestMessageRequestOut": "_essentialcontacts_11_GoogleCloudEssentialcontactsV1SendTestMessageRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudEssentialcontactsV1ComputeContactsResponseIn"] = t.struct(
        {
            "contacts": t.array(
                t.proxy(renames["GoogleCloudEssentialcontactsV1ContactIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudEssentialcontactsV1ComputeContactsResponseIn"])
    types["GoogleCloudEssentialcontactsV1ComputeContactsResponseOut"] = t.struct(
        {
            "contacts": t.array(
                t.proxy(renames["GoogleCloudEssentialcontactsV1ContactOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudEssentialcontactsV1ComputeContactsResponseOut"])
    types["GoogleCloudEssentialcontactsV1ContactIn"] = t.struct(
        {
            "validateTime": t.string().optional(),
            "notificationCategorySubscriptions": t.array(t.string()),
            "languageTag": t.string(),
            "email": t.string(),
            "validationState": t.string().optional(),
        }
    ).named(renames["GoogleCloudEssentialcontactsV1ContactIn"])
    types["GoogleCloudEssentialcontactsV1ContactOut"] = t.struct(
        {
            "validateTime": t.string().optional(),
            "notificationCategorySubscriptions": t.array(t.string()),
            "languageTag": t.string(),
            "name": t.string().optional(),
            "email": t.string(),
            "validationState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudEssentialcontactsV1ContactOut"])
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
    types["GoogleCloudEssentialcontactsV1ListContactsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "contacts": t.array(
                t.proxy(renames["GoogleCloudEssentialcontactsV1ContactIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudEssentialcontactsV1ListContactsResponseIn"])
    types["GoogleCloudEssentialcontactsV1ListContactsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "contacts": t.array(
                t.proxy(renames["GoogleCloudEssentialcontactsV1ContactOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudEssentialcontactsV1ListContactsResponseOut"])
    types["GoogleCloudEssentialcontactsV1SendTestMessageRequestIn"] = t.struct(
        {"contacts": t.array(t.string()), "notificationCategory": t.string()}
    ).named(renames["GoogleCloudEssentialcontactsV1SendTestMessageRequestIn"])
    types["GoogleCloudEssentialcontactsV1SendTestMessageRequestOut"] = t.struct(
        {
            "contacts": t.array(t.string()),
            "notificationCategory": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudEssentialcontactsV1SendTestMessageRequestOut"])

    functions = {}
    functions["foldersContactsCompute"] = essentialcontacts.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersContactsSendTestMessage"] = essentialcontacts.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersContactsGet"] = essentialcontacts.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersContactsList"] = essentialcontacts.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersContactsCreate"] = essentialcontacts.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersContactsPatch"] = essentialcontacts.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersContactsDelete"] = essentialcontacts.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsContactsDelete"] = essentialcontacts.get(
        "v1/{parent}/contacts:compute",
        t.struct(
            {
                "notificationCategories": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudEssentialcontactsV1ComputeContactsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsContactsSendTestMessage"] = essentialcontacts.get(
        "v1/{parent}/contacts:compute",
        t.struct(
            {
                "notificationCategories": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudEssentialcontactsV1ComputeContactsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsContactsList"] = essentialcontacts.get(
        "v1/{parent}/contacts:compute",
        t.struct(
            {
                "notificationCategories": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudEssentialcontactsV1ComputeContactsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsContactsCreate"] = essentialcontacts.get(
        "v1/{parent}/contacts:compute",
        t.struct(
            {
                "notificationCategories": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudEssentialcontactsV1ComputeContactsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsContactsPatch"] = essentialcontacts.get(
        "v1/{parent}/contacts:compute",
        t.struct(
            {
                "notificationCategories": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudEssentialcontactsV1ComputeContactsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsContactsGet"] = essentialcontacts.get(
        "v1/{parent}/contacts:compute",
        t.struct(
            {
                "notificationCategories": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudEssentialcontactsV1ComputeContactsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsContactsCompute"] = essentialcontacts.get(
        "v1/{parent}/contacts:compute",
        t.struct(
            {
                "notificationCategories": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudEssentialcontactsV1ComputeContactsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsContactsCompute"] = essentialcontacts.get(
        "v1/{parent}/contacts",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudEssentialcontactsV1ListContactsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsContactsCreate"] = essentialcontacts.get(
        "v1/{parent}/contacts",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudEssentialcontactsV1ListContactsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsContactsDelete"] = essentialcontacts.get(
        "v1/{parent}/contacts",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudEssentialcontactsV1ListContactsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsContactsSendTestMessage"] = essentialcontacts.get(
        "v1/{parent}/contacts",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudEssentialcontactsV1ListContactsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsContactsGet"] = essentialcontacts.get(
        "v1/{parent}/contacts",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudEssentialcontactsV1ListContactsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsContactsPatch"] = essentialcontacts.get(
        "v1/{parent}/contacts",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudEssentialcontactsV1ListContactsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsContactsList"] = essentialcontacts.get(
        "v1/{parent}/contacts",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudEssentialcontactsV1ListContactsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="essentialcontacts",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
