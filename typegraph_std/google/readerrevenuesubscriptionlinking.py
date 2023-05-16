from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_readerrevenuesubscriptionlinking() -> Import:
    readerrevenuesubscriptionlinking = HTTPRuntime(
        "https://readerrevenuesubscriptionlinking.googleapis.com/"
    )

    renames = {
        "ErrorResponse": "_readerrevenuesubscriptionlinking_1_ErrorResponse",
        "DeleteReaderResponseIn": "_readerrevenuesubscriptionlinking_2_DeleteReaderResponseIn",
        "DeleteReaderResponseOut": "_readerrevenuesubscriptionlinking_3_DeleteReaderResponseOut",
        "EntitlementIn": "_readerrevenuesubscriptionlinking_4_EntitlementIn",
        "EntitlementOut": "_readerrevenuesubscriptionlinking_5_EntitlementOut",
        "ReaderIn": "_readerrevenuesubscriptionlinking_6_ReaderIn",
        "ReaderOut": "_readerrevenuesubscriptionlinking_7_ReaderOut",
        "ReaderEntitlementsIn": "_readerrevenuesubscriptionlinking_8_ReaderEntitlementsIn",
        "ReaderEntitlementsOut": "_readerrevenuesubscriptionlinking_9_ReaderEntitlementsOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
            "entitlements": t.array(t.proxy(renames["EntitlementOut"])).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReaderEntitlementsOut"])

    functions = {}
    functions[
        "publicationsReadersGetEntitlements"
    ] = readerrevenuesubscriptionlinking.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "entitlements": t.array(t.proxy(renames["EntitlementIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReaderEntitlementsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["publicationsReadersDelete"] = readerrevenuesubscriptionlinking.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "entitlements": t.array(t.proxy(renames["EntitlementIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReaderEntitlementsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["publicationsReadersGet"] = readerrevenuesubscriptionlinking.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "entitlements": t.array(t.proxy(renames["EntitlementIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReaderEntitlementsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "publicationsReadersUpdateEntitlements"
    ] = readerrevenuesubscriptionlinking.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "entitlements": t.array(t.proxy(renames["EntitlementIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
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
