from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_essentialcontacts() -> Import:
    essentialcontacts = HTTPRuntime("https://essentialcontacts.googleapis.com/")

    renames = {
        "ErrorResponse": "_essentialcontacts_1_ErrorResponse",
        "GoogleCloudEssentialcontactsV1ContactIn": "_essentialcontacts_2_GoogleCloudEssentialcontactsV1ContactIn",
        "GoogleCloudEssentialcontactsV1ContactOut": "_essentialcontacts_3_GoogleCloudEssentialcontactsV1ContactOut",
        "GoogleCloudEssentialcontactsV1ListContactsResponseIn": "_essentialcontacts_4_GoogleCloudEssentialcontactsV1ListContactsResponseIn",
        "GoogleCloudEssentialcontactsV1ListContactsResponseOut": "_essentialcontacts_5_GoogleCloudEssentialcontactsV1ListContactsResponseOut",
        "GoogleCloudEssentialcontactsV1ComputeContactsResponseIn": "_essentialcontacts_6_GoogleCloudEssentialcontactsV1ComputeContactsResponseIn",
        "GoogleCloudEssentialcontactsV1ComputeContactsResponseOut": "_essentialcontacts_7_GoogleCloudEssentialcontactsV1ComputeContactsResponseOut",
        "GoogleProtobufEmptyIn": "_essentialcontacts_8_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_essentialcontacts_9_GoogleProtobufEmptyOut",
        "GoogleCloudEssentialcontactsV1SendTestMessageRequestIn": "_essentialcontacts_10_GoogleCloudEssentialcontactsV1SendTestMessageRequestIn",
        "GoogleCloudEssentialcontactsV1SendTestMessageRequestOut": "_essentialcontacts_11_GoogleCloudEssentialcontactsV1SendTestMessageRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudEssentialcontactsV1ContactIn"] = t.struct(
        {
            "email": t.string(),
            "validationState": t.string().optional(),
            "validateTime": t.string().optional(),
            "languageTag": t.string(),
            "notificationCategorySubscriptions": t.array(t.string()),
        }
    ).named(renames["GoogleCloudEssentialcontactsV1ContactIn"])
    types["GoogleCloudEssentialcontactsV1ContactOut"] = t.struct(
        {
            "email": t.string(),
            "validationState": t.string().optional(),
            "validateTime": t.string().optional(),
            "languageTag": t.string(),
            "name": t.string().optional(),
            "notificationCategorySubscriptions": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudEssentialcontactsV1ContactOut"])
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
    types["GoogleCloudEssentialcontactsV1ComputeContactsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "contacts": t.array(
                t.proxy(renames["GoogleCloudEssentialcontactsV1ContactIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudEssentialcontactsV1ComputeContactsResponseIn"])
    types["GoogleCloudEssentialcontactsV1ComputeContactsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "contacts": t.array(
                t.proxy(renames["GoogleCloudEssentialcontactsV1ContactOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudEssentialcontactsV1ComputeContactsResponseOut"])
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
    types["GoogleCloudEssentialcontactsV1SendTestMessageRequestIn"] = t.struct(
        {"notificationCategory": t.string(), "contacts": t.array(t.string())}
    ).named(renames["GoogleCloudEssentialcontactsV1SendTestMessageRequestIn"])
    types["GoogleCloudEssentialcontactsV1SendTestMessageRequestOut"] = t.struct(
        {
            "notificationCategory": t.string(),
            "contacts": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudEssentialcontactsV1SendTestMessageRequestOut"])

    functions = {}
    functions["projectsContactsList"] = essentialcontacts.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsContactsGet"] = essentialcontacts.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsContactsSendTestMessage"] = essentialcontacts.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsContactsCompute"] = essentialcontacts.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsContactsCreate"] = essentialcontacts.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsContactsPatch"] = essentialcontacts.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsContactsDelete"] = essentialcontacts.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersContactsCompute"] = essentialcontacts.post(
        "v1/{resource}/contacts:sendTestMessage",
        t.struct(
            {
                "resource": t.string(),
                "notificationCategory": t.string(),
                "contacts": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersContactsGet"] = essentialcontacts.post(
        "v1/{resource}/contacts:sendTestMessage",
        t.struct(
            {
                "resource": t.string(),
                "notificationCategory": t.string(),
                "contacts": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersContactsPatch"] = essentialcontacts.post(
        "v1/{resource}/contacts:sendTestMessage",
        t.struct(
            {
                "resource": t.string(),
                "notificationCategory": t.string(),
                "contacts": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersContactsDelete"] = essentialcontacts.post(
        "v1/{resource}/contacts:sendTestMessage",
        t.struct(
            {
                "resource": t.string(),
                "notificationCategory": t.string(),
                "contacts": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersContactsCreate"] = essentialcontacts.post(
        "v1/{resource}/contacts:sendTestMessage",
        t.struct(
            {
                "resource": t.string(),
                "notificationCategory": t.string(),
                "contacts": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersContactsList"] = essentialcontacts.post(
        "v1/{resource}/contacts:sendTestMessage",
        t.struct(
            {
                "resource": t.string(),
                "notificationCategory": t.string(),
                "contacts": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersContactsSendTestMessage"] = essentialcontacts.post(
        "v1/{resource}/contacts:sendTestMessage",
        t.struct(
            {
                "resource": t.string(),
                "notificationCategory": t.string(),
                "contacts": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsContactsGet"] = essentialcontacts.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsContactsSendTestMessage"] = essentialcontacts.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsContactsPatch"] = essentialcontacts.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsContactsCompute"] = essentialcontacts.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsContactsCreate"] = essentialcontacts.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsContactsList"] = essentialcontacts.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsContactsDelete"] = essentialcontacts.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="essentialcontacts", renames=renames, types=types, functions=functions
    )
