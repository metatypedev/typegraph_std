from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_apikeys() -> Import:
    apikeys = HTTPRuntime("https://apikeys.googleapis.com/")

    renames = {
        "ErrorResponse": "_apikeys_1_ErrorResponse",
        "StatusIn": "_apikeys_2_StatusIn",
        "StatusOut": "_apikeys_3_StatusOut",
        "V2BrowserKeyRestrictionsIn": "_apikeys_4_V2BrowserKeyRestrictionsIn",
        "V2BrowserKeyRestrictionsOut": "_apikeys_5_V2BrowserKeyRestrictionsOut",
        "V2KeyIn": "_apikeys_6_V2KeyIn",
        "V2KeyOut": "_apikeys_7_V2KeyOut",
        "V2ListKeysResponseIn": "_apikeys_8_V2ListKeysResponseIn",
        "V2ListKeysResponseOut": "_apikeys_9_V2ListKeysResponseOut",
        "V2IosKeyRestrictionsIn": "_apikeys_10_V2IosKeyRestrictionsIn",
        "V2IosKeyRestrictionsOut": "_apikeys_11_V2IosKeyRestrictionsOut",
        "V2ApiTargetIn": "_apikeys_12_V2ApiTargetIn",
        "V2ApiTargetOut": "_apikeys_13_V2ApiTargetOut",
        "V2GetKeyStringResponseIn": "_apikeys_14_V2GetKeyStringResponseIn",
        "V2GetKeyStringResponseOut": "_apikeys_15_V2GetKeyStringResponseOut",
        "V2AndroidKeyRestrictionsIn": "_apikeys_16_V2AndroidKeyRestrictionsIn",
        "V2AndroidKeyRestrictionsOut": "_apikeys_17_V2AndroidKeyRestrictionsOut",
        "V2AndroidApplicationIn": "_apikeys_18_V2AndroidApplicationIn",
        "V2AndroidApplicationOut": "_apikeys_19_V2AndroidApplicationOut",
        "V2ServerKeyRestrictionsIn": "_apikeys_20_V2ServerKeyRestrictionsIn",
        "V2ServerKeyRestrictionsOut": "_apikeys_21_V2ServerKeyRestrictionsOut",
        "V2RestrictionsIn": "_apikeys_22_V2RestrictionsIn",
        "V2RestrictionsOut": "_apikeys_23_V2RestrictionsOut",
        "OperationIn": "_apikeys_24_OperationIn",
        "OperationOut": "_apikeys_25_OperationOut",
        "V2LookupKeyResponseIn": "_apikeys_26_V2LookupKeyResponseIn",
        "V2LookupKeyResponseOut": "_apikeys_27_V2LookupKeyResponseOut",
        "V2UndeleteKeyRequestIn": "_apikeys_28_V2UndeleteKeyRequestIn",
        "V2UndeleteKeyRequestOut": "_apikeys_29_V2UndeleteKeyRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["StatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["V2BrowserKeyRestrictionsIn"] = t.struct(
        {"allowedReferrers": t.array(t.string()).optional()}
    ).named(renames["V2BrowserKeyRestrictionsIn"])
    types["V2BrowserKeyRestrictionsOut"] = t.struct(
        {
            "allowedReferrers": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V2BrowserKeyRestrictionsOut"])
    types["V2KeyIn"] = t.struct(
        {
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "restrictions": t.proxy(renames["V2RestrictionsIn"]).optional(),
        }
    ).named(renames["V2KeyIn"])
    types["V2KeyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "createTime": t.string().optional(),
            "deleteTime": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "restrictions": t.proxy(renames["V2RestrictionsOut"]).optional(),
            "updateTime": t.string().optional(),
            "keyString": t.string().optional(),
            "uid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V2KeyOut"])
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
    types["V2IosKeyRestrictionsIn"] = t.struct(
        {"allowedBundleIds": t.array(t.string()).optional()}
    ).named(renames["V2IosKeyRestrictionsIn"])
    types["V2IosKeyRestrictionsOut"] = t.struct(
        {
            "allowedBundleIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V2IosKeyRestrictionsOut"])
    types["V2ApiTargetIn"] = t.struct(
        {"service": t.string().optional(), "methods": t.array(t.string()).optional()}
    ).named(renames["V2ApiTargetIn"])
    types["V2ApiTargetOut"] = t.struct(
        {
            "service": t.string().optional(),
            "methods": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V2ApiTargetOut"])
    types["V2GetKeyStringResponseIn"] = t.struct(
        {"keyString": t.string().optional()}
    ).named(renames["V2GetKeyStringResponseIn"])
    types["V2GetKeyStringResponseOut"] = t.struct(
        {
            "keyString": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V2GetKeyStringResponseOut"])
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
    types["V2ServerKeyRestrictionsIn"] = t.struct(
        {"allowedIps": t.array(t.string()).optional()}
    ).named(renames["V2ServerKeyRestrictionsIn"])
    types["V2ServerKeyRestrictionsOut"] = t.struct(
        {
            "allowedIps": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V2ServerKeyRestrictionsOut"])
    types["V2RestrictionsIn"] = t.struct(
        {
            "serverKeyRestrictions": t.proxy(
                renames["V2ServerKeyRestrictionsIn"]
            ).optional(),
            "apiTargets": t.array(t.proxy(renames["V2ApiTargetIn"])).optional(),
            "iosKeyRestrictions": t.proxy(renames["V2IosKeyRestrictionsIn"]).optional(),
            "browserKeyRestrictions": t.proxy(
                renames["V2BrowserKeyRestrictionsIn"]
            ).optional(),
            "androidKeyRestrictions": t.proxy(
                renames["V2AndroidKeyRestrictionsIn"]
            ).optional(),
        }
    ).named(renames["V2RestrictionsIn"])
    types["V2RestrictionsOut"] = t.struct(
        {
            "serverKeyRestrictions": t.proxy(
                renames["V2ServerKeyRestrictionsOut"]
            ).optional(),
            "apiTargets": t.array(t.proxy(renames["V2ApiTargetOut"])).optional(),
            "iosKeyRestrictions": t.proxy(
                renames["V2IosKeyRestrictionsOut"]
            ).optional(),
            "browserKeyRestrictions": t.proxy(
                renames["V2BrowserKeyRestrictionsOut"]
            ).optional(),
            "androidKeyRestrictions": t.proxy(
                renames["V2AndroidKeyRestrictionsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V2RestrictionsOut"])
    types["OperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationOut"])
    types["V2LookupKeyResponseIn"] = t.struct(
        {"parent": t.string().optional(), "name": t.string().optional()}
    ).named(renames["V2LookupKeyResponseIn"])
    types["V2LookupKeyResponseOut"] = t.struct(
        {
            "parent": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V2LookupKeyResponseOut"])
    types["V2UndeleteKeyRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["V2UndeleteKeyRequestIn"]
    )
    types["V2UndeleteKeyRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["V2UndeleteKeyRequestOut"])

    functions = {}
    functions["projectsLocationsKeysGetKeyString"] = apikeys.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["V2KeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeysUndelete"] = apikeys.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["V2KeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeysList"] = apikeys.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["V2KeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeysCreate"] = apikeys.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["V2KeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeysDelete"] = apikeys.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["V2KeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeysPatch"] = apikeys.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["V2KeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeysGet"] = apikeys.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["V2KeyOut"]),
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
    functions["operationsGet"] = apikeys.get(
        "v2/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="apikeys", renames=renames, types=Box(types), functions=Box(functions)
    )
