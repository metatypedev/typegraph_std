from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_readerrevenuesubscriptionlinking() -> Import:
    readerrevenuesubscriptionlinking = HTTPRuntime(
        "https://readerrevenuesubscriptionlinking.googleapis.com/"
    )

    renames = {
        "ErrorResponse": "_readerrevenuesubscriptionlinking_1_ErrorResponse",
        "EntitlementIn": "_readerrevenuesubscriptionlinking_2_EntitlementIn",
        "EntitlementOut": "_readerrevenuesubscriptionlinking_3_EntitlementOut",
        "DeleteReaderResponseIn": "_readerrevenuesubscriptionlinking_4_DeleteReaderResponseIn",
        "DeleteReaderResponseOut": "_readerrevenuesubscriptionlinking_5_DeleteReaderResponseOut",
        "ReaderIn": "_readerrevenuesubscriptionlinking_6_ReaderIn",
        "ReaderOut": "_readerrevenuesubscriptionlinking_7_ReaderOut",
        "ReaderEntitlementsIn": "_readerrevenuesubscriptionlinking_8_ReaderEntitlementsIn",
        "ReaderEntitlementsOut": "_readerrevenuesubscriptionlinking_9_ReaderEntitlementsOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    functions[
        "publicationsReadersUpdateEntitlements"
    ] = readerrevenuesubscriptionlinking.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "force": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeleteReaderResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "publicationsReadersGetEntitlements"
    ] = readerrevenuesubscriptionlinking.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "force": t.boolean().optional(),
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
                "name": t.string(),
                "force": t.boolean().optional(),
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
                "name": t.string(),
                "force": t.boolean().optional(),
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
        types=Box(types),
        functions=Box(functions),
    )
