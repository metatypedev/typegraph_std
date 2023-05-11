from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_readerrevenuesubscriptionlinking() -> Import:
    readerrevenuesubscriptionlinking = HTTPRuntime(
        "https://readerrevenuesubscriptionlinking.googleapis.com/"
    )

    renames = {
        "ErrorResponse": "_readerrevenuesubscriptionlinking_1_ErrorResponse",
        "ReaderEntitlementsIn": "_readerrevenuesubscriptionlinking_2_ReaderEntitlementsIn",
        "ReaderEntitlementsOut": "_readerrevenuesubscriptionlinking_3_ReaderEntitlementsOut",
        "ReaderIn": "_readerrevenuesubscriptionlinking_4_ReaderIn",
        "ReaderOut": "_readerrevenuesubscriptionlinking_5_ReaderOut",
        "DeleteReaderResponseIn": "_readerrevenuesubscriptionlinking_6_DeleteReaderResponseIn",
        "DeleteReaderResponseOut": "_readerrevenuesubscriptionlinking_7_DeleteReaderResponseOut",
        "EntitlementIn": "_readerrevenuesubscriptionlinking_8_EntitlementIn",
        "EntitlementOut": "_readerrevenuesubscriptionlinking_9_EntitlementOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ReaderEntitlementsIn"] = t.struct(
        {"entitlements": t.array(t.proxy(renames["EntitlementIn"])).optional()}
    ).named(renames["ReaderEntitlementsIn"])
    types["ReaderEntitlementsOut"] = t.struct(
        {
            "entitlements": t.array(t.proxy(renames["EntitlementOut"])).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReaderEntitlementsOut"])
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
    types["DeleteReaderResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeleteReaderResponseIn"]
    )
    types["DeleteReaderResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteReaderResponseOut"])
    types["EntitlementIn"] = t.struct(
        {
            "subscriptionToken": t.string().optional(),
            "productId": t.string(),
            "detail": t.string().optional(),
            "expireTime": t.string(),
        }
    ).named(renames["EntitlementIn"])
    types["EntitlementOut"] = t.struct(
        {
            "subscriptionToken": t.string().optional(),
            "productId": t.string(),
            "detail": t.string().optional(),
            "expireTime": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntitlementOut"])

    functions = {}
    functions[
        "publicationsReadersGetEntitlements"
    ] = readerrevenuesubscriptionlinking.delete(
        "v1/{name}",
        t.struct(
            {
                "force": t.boolean().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeleteReaderResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["publicationsReadersGet"] = readerrevenuesubscriptionlinking.delete(
        "v1/{name}",
        t.struct(
            {
                "force": t.boolean().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeleteReaderResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "publicationsReadersUpdateEntitlements"
    ] = readerrevenuesubscriptionlinking.delete(
        "v1/{name}",
        t.struct(
            {
                "force": t.boolean().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeleteReaderResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["publicationsReadersDelete"] = readerrevenuesubscriptionlinking.delete(
        "v1/{name}",
        t.struct(
            {
                "force": t.boolean().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeleteReaderResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="readerrevenuesubscriptionlinking",
        renames=renames,
        types=types,
        functions=functions,
    )
