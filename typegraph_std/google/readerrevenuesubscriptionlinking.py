from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_readerrevenuesubscriptionlinking():
    readerrevenuesubscriptionlinking = HTTPRuntime(
        "https://readerrevenuesubscriptionlinking.googleapis.com/"
    )

    renames = {
        "ErrorResponse": "_readerrevenuesubscriptionlinking_1_ErrorResponse",
        "ReaderIn": "_readerrevenuesubscriptionlinking_2_ReaderIn",
        "ReaderOut": "_readerrevenuesubscriptionlinking_3_ReaderOut",
        "EntitlementIn": "_readerrevenuesubscriptionlinking_4_EntitlementIn",
        "EntitlementOut": "_readerrevenuesubscriptionlinking_5_EntitlementOut",
        "DeleteReaderResponseIn": "_readerrevenuesubscriptionlinking_6_DeleteReaderResponseIn",
        "DeleteReaderResponseOut": "_readerrevenuesubscriptionlinking_7_DeleteReaderResponseOut",
        "ReaderEntitlementsIn": "_readerrevenuesubscriptionlinking_8_ReaderEntitlementsIn",
        "ReaderEntitlementsOut": "_readerrevenuesubscriptionlinking_9_ReaderEntitlementsOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ReaderIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ReaderIn"]
    )
    types["ReaderOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReaderOut"])
    types["EntitlementIn"] = t.struct(
        {
            "expireTime": t.string(),
            "productId": t.string(),
            "detail": t.string().optional(),
            "subscriptionToken": t.string().optional(),
        }
    ).named(renames["EntitlementIn"])
    types["EntitlementOut"] = t.struct(
        {
            "expireTime": t.string(),
            "productId": t.string(),
            "detail": t.string().optional(),
            "subscriptionToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntitlementOut"])
    types["DeleteReaderResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeleteReaderResponseIn"]
    )
    types["DeleteReaderResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteReaderResponseOut"])
    types["ReaderEntitlementsIn"] = t.struct(
        {"entitlements": t.array(t.proxy(renames["EntitlementIn"])).optional()}
    ).named(renames["ReaderEntitlementsIn"])
    types["ReaderEntitlementsOut"] = t.struct(
        {
            "name": t.string().optional(),
            "entitlements": t.array(t.proxy(renames["EntitlementOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReaderEntitlementsOut"])

    functions = {}
    functions["publicationsReadersGet"] = readerrevenuesubscriptionlinking.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ReaderEntitlementsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "publicationsReadersUpdateEntitlements"
    ] = readerrevenuesubscriptionlinking.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ReaderEntitlementsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["publicationsReadersDelete"] = readerrevenuesubscriptionlinking.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ReaderEntitlementsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "publicationsReadersGetEntitlements"
    ] = readerrevenuesubscriptionlinking.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ReaderEntitlementsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="readerrevenuesubscriptionlinking",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
