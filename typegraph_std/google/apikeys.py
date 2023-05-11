from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_apikeys() -> Import:
    apikeys = HTTPRuntime("https://apikeys.googleapis.com/")

    renames = {
        "ErrorResponse": "_apikeys_1_ErrorResponse",
        "V2RestrictionsIn": "_apikeys_2_V2RestrictionsIn",
        "V2RestrictionsOut": "_apikeys_3_V2RestrictionsOut",
        "V2BrowserKeyRestrictionsIn": "_apikeys_4_V2BrowserKeyRestrictionsIn",
        "V2BrowserKeyRestrictionsOut": "_apikeys_5_V2BrowserKeyRestrictionsOut",
        "StatusIn": "_apikeys_6_StatusIn",
        "StatusOut": "_apikeys_7_StatusOut",
        "V2GetKeyStringResponseIn": "_apikeys_8_V2GetKeyStringResponseIn",
        "V2GetKeyStringResponseOut": "_apikeys_9_V2GetKeyStringResponseOut",
        "V2UndeleteKeyRequestIn": "_apikeys_10_V2UndeleteKeyRequestIn",
        "V2UndeleteKeyRequestOut": "_apikeys_11_V2UndeleteKeyRequestOut",
        "V2AndroidApplicationIn": "_apikeys_12_V2AndroidApplicationIn",
        "V2AndroidApplicationOut": "_apikeys_13_V2AndroidApplicationOut",
        "V2AndroidKeyRestrictionsIn": "_apikeys_14_V2AndroidKeyRestrictionsIn",
        "V2AndroidKeyRestrictionsOut": "_apikeys_15_V2AndroidKeyRestrictionsOut",
        "OperationIn": "_apikeys_16_OperationIn",
        "OperationOut": "_apikeys_17_OperationOut",
        "V2ListKeysResponseIn": "_apikeys_18_V2ListKeysResponseIn",
        "V2ListKeysResponseOut": "_apikeys_19_V2ListKeysResponseOut",
        "V2LookupKeyResponseIn": "_apikeys_20_V2LookupKeyResponseIn",
        "V2LookupKeyResponseOut": "_apikeys_21_V2LookupKeyResponseOut",
        "V2IosKeyRestrictionsIn": "_apikeys_22_V2IosKeyRestrictionsIn",
        "V2IosKeyRestrictionsOut": "_apikeys_23_V2IosKeyRestrictionsOut",
        "V2KeyIn": "_apikeys_24_V2KeyIn",
        "V2KeyOut": "_apikeys_25_V2KeyOut",
        "V2ApiTargetIn": "_apikeys_26_V2ApiTargetIn",
        "V2ApiTargetOut": "_apikeys_27_V2ApiTargetOut",
        "V2ServerKeyRestrictionsIn": "_apikeys_28_V2ServerKeyRestrictionsIn",
        "V2ServerKeyRestrictionsOut": "_apikeys_29_V2ServerKeyRestrictionsOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["V2RestrictionsIn"] = t.struct(
        {
            "browserKeyRestrictions": t.proxy(
                renames["V2BrowserKeyRestrictionsIn"]
            ).optional(),
            "serverKeyRestrictions": t.proxy(
                renames["V2ServerKeyRestrictionsIn"]
            ).optional(),
            "iosKeyRestrictions": t.proxy(renames["V2IosKeyRestrictionsIn"]).optional(),
            "apiTargets": t.array(t.proxy(renames["V2ApiTargetIn"])).optional(),
            "androidKeyRestrictions": t.proxy(
                renames["V2AndroidKeyRestrictionsIn"]
            ).optional(),
        }
    ).named(renames["V2RestrictionsIn"])
    types["V2RestrictionsOut"] = t.struct(
        {
            "browserKeyRestrictions": t.proxy(
                renames["V2BrowserKeyRestrictionsOut"]
            ).optional(),
            "serverKeyRestrictions": t.proxy(
                renames["V2ServerKeyRestrictionsOut"]
            ).optional(),
            "iosKeyRestrictions": t.proxy(
                renames["V2IosKeyRestrictionsOut"]
            ).optional(),
            "apiTargets": t.array(t.proxy(renames["V2ApiTargetOut"])).optional(),
            "androidKeyRestrictions": t.proxy(
                renames["V2AndroidKeyRestrictionsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V2RestrictionsOut"])
    types["V2BrowserKeyRestrictionsIn"] = t.struct(
        {"allowedReferrers": t.array(t.string()).optional()}
    ).named(renames["V2BrowserKeyRestrictionsIn"])
    types["V2BrowserKeyRestrictionsOut"] = t.struct(
        {
            "allowedReferrers": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V2BrowserKeyRestrictionsOut"])
    types["StatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["V2GetKeyStringResponseIn"] = t.struct(
        {"keyString": t.string().optional()}
    ).named(renames["V2GetKeyStringResponseIn"])
    types["V2GetKeyStringResponseOut"] = t.struct(
        {
            "keyString": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V2GetKeyStringResponseOut"])
    types["V2UndeleteKeyRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["V2UndeleteKeyRequestIn"]
    )
    types["V2UndeleteKeyRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["V2UndeleteKeyRequestOut"])
    types["V2AndroidApplicationIn"] = t.struct(
        {"packageName": t.string().optional(), "sha1Fingerprint": t.string().optional()}
    ).named(renames["V2AndroidApplicationIn"])
    types["V2AndroidApplicationOut"] = t.struct(
        {
            "packageName": t.string().optional(),
            "sha1Fingerprint": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V2AndroidApplicationOut"])
    types["V2AndroidKeyRestrictionsIn"] = t.struct(
        {
            "allowedApplications": t.array(
                t.proxy(renames["V2AndroidApplicationIn"])
            ).optional()
        }
    ).named(renames["V2AndroidKeyRestrictionsIn"])
    types["V2AndroidKeyRestrictionsOut"] = t.struct(
        {
            "allowedApplications": t.array(
                t.proxy(renames["V2AndroidApplicationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V2AndroidKeyRestrictionsOut"])
    types["OperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationOut"])
    types["V2ListKeysResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "keys": t.array(t.proxy(renames["V2KeyIn"])).optional(),
        }
    ).named(renames["V2ListKeysResponseIn"])
    types["V2ListKeysResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "keys": t.array(t.proxy(renames["V2KeyOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V2ListKeysResponseOut"])
    types["V2LookupKeyResponseIn"] = t.struct(
        {"name": t.string().optional(), "parent": t.string().optional()}
    ).named(renames["V2LookupKeyResponseIn"])
    types["V2LookupKeyResponseOut"] = t.struct(
        {
            "name": t.string().optional(),
            "parent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V2LookupKeyResponseOut"])
    types["V2IosKeyRestrictionsIn"] = t.struct(
        {"allowedBundleIds": t.array(t.string()).optional()}
    ).named(renames["V2IosKeyRestrictionsIn"])
    types["V2IosKeyRestrictionsOut"] = t.struct(
        {
            "allowedBundleIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V2IosKeyRestrictionsOut"])
    types["V2KeyIn"] = t.struct(
        {
            "restrictions": t.proxy(renames["V2RestrictionsIn"]).optional(),
            "displayName": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["V2KeyIn"])
    types["V2KeyOut"] = t.struct(
        {
            "restrictions": t.proxy(renames["V2RestrictionsOut"]).optional(),
            "deleteTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "etag": t.string().optional(),
            "name": t.string().optional(),
            "keyString": t.string().optional(),
            "displayName": t.string().optional(),
            "createTime": t.string().optional(),
            "uid": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V2KeyOut"])
    types["V2ApiTargetIn"] = t.struct(
        {"methods": t.array(t.string()).optional(), "service": t.string().optional()}
    ).named(renames["V2ApiTargetIn"])
    types["V2ApiTargetOut"] = t.struct(
        {
            "methods": t.array(t.string()).optional(),
            "service": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V2ApiTargetOut"])
    types["V2ServerKeyRestrictionsIn"] = t.struct(
        {"allowedIps": t.array(t.string()).optional()}
    ).named(renames["V2ServerKeyRestrictionsIn"])
    types["V2ServerKeyRestrictionsOut"] = t.struct(
        {
            "allowedIps": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V2ServerKeyRestrictionsOut"])

    functions = {}
    functions["operationsGet"] = apikeys.get(
        "v2/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeysPatch"] = apikeys.post(
        "v2/{name}:undelete",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeysGet"] = apikeys.post(
        "v2/{name}:undelete",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeysDelete"] = apikeys.post(
        "v2/{name}:undelete",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeysGetKeyString"] = apikeys.post(
        "v2/{name}:undelete",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeysCreate"] = apikeys.post(
        "v2/{name}:undelete",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeysList"] = apikeys.post(
        "v2/{name}:undelete",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeysUndelete"] = apikeys.post(
        "v2/{name}:undelete",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["keysLookupKey"] = apikeys.get(
        "v2/keys:lookupKey",
        t.struct({"keyString": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["V2LookupKeyResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(importer="apikeys", renames=renames, types=types, functions=functions)
