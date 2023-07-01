from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_apikeys():
    apikeys = HTTPRuntime("https://apikeys.googleapis.com/")

    renames = {
        "ErrorResponse": "_apikeys_1_ErrorResponse",
        "V2KeyIn": "_apikeys_2_V2KeyIn",
        "V2KeyOut": "_apikeys_3_V2KeyOut",
        "V2AndroidKeyRestrictionsIn": "_apikeys_4_V2AndroidKeyRestrictionsIn",
        "V2AndroidKeyRestrictionsOut": "_apikeys_5_V2AndroidKeyRestrictionsOut",
        "OperationIn": "_apikeys_6_OperationIn",
        "OperationOut": "_apikeys_7_OperationOut",
        "V2AndroidApplicationIn": "_apikeys_8_V2AndroidApplicationIn",
        "V2AndroidApplicationOut": "_apikeys_9_V2AndroidApplicationOut",
        "V2ListKeysResponseIn": "_apikeys_10_V2ListKeysResponseIn",
        "V2ListKeysResponseOut": "_apikeys_11_V2ListKeysResponseOut",
        "StatusIn": "_apikeys_12_StatusIn",
        "StatusOut": "_apikeys_13_StatusOut",
        "V2IosKeyRestrictionsIn": "_apikeys_14_V2IosKeyRestrictionsIn",
        "V2IosKeyRestrictionsOut": "_apikeys_15_V2IosKeyRestrictionsOut",
        "V2BrowserKeyRestrictionsIn": "_apikeys_16_V2BrowserKeyRestrictionsIn",
        "V2BrowserKeyRestrictionsOut": "_apikeys_17_V2BrowserKeyRestrictionsOut",
        "V2LookupKeyResponseIn": "_apikeys_18_V2LookupKeyResponseIn",
        "V2LookupKeyResponseOut": "_apikeys_19_V2LookupKeyResponseOut",
        "V2GetKeyStringResponseIn": "_apikeys_20_V2GetKeyStringResponseIn",
        "V2GetKeyStringResponseOut": "_apikeys_21_V2GetKeyStringResponseOut",
        "V2UndeleteKeyRequestIn": "_apikeys_22_V2UndeleteKeyRequestIn",
        "V2UndeleteKeyRequestOut": "_apikeys_23_V2UndeleteKeyRequestOut",
        "V2ApiTargetIn": "_apikeys_24_V2ApiTargetIn",
        "V2ApiTargetOut": "_apikeys_25_V2ApiTargetOut",
        "V2RestrictionsIn": "_apikeys_26_V2RestrictionsIn",
        "V2RestrictionsOut": "_apikeys_27_V2RestrictionsOut",
        "V2ServerKeyRestrictionsIn": "_apikeys_28_V2ServerKeyRestrictionsIn",
        "V2ServerKeyRestrictionsOut": "_apikeys_29_V2ServerKeyRestrictionsOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["V2KeyIn"] = t.struct(
        {
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "restrictions": t.proxy(renames["V2RestrictionsIn"]).optional(),
        }
    ).named(renames["V2KeyIn"])
    types["V2KeyOut"] = t.struct(
        {
            "deleteTime": t.string().optional(),
            "etag": t.string().optional(),
            "updateTime": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "createTime": t.string().optional(),
            "keyString": t.string().optional(),
            "restrictions": t.proxy(renames["V2RestrictionsOut"]).optional(),
            "name": t.string().optional(),
            "uid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V2KeyOut"])
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
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
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
    types["StatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["V2IosKeyRestrictionsIn"] = t.struct(
        {"allowedBundleIds": t.array(t.string()).optional()}
    ).named(renames["V2IosKeyRestrictionsIn"])
    types["V2IosKeyRestrictionsOut"] = t.struct(
        {
            "allowedBundleIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V2IosKeyRestrictionsOut"])
    types["V2BrowserKeyRestrictionsIn"] = t.struct(
        {"allowedReferrers": t.array(t.string()).optional()}
    ).named(renames["V2BrowserKeyRestrictionsIn"])
    types["V2BrowserKeyRestrictionsOut"] = t.struct(
        {
            "allowedReferrers": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V2BrowserKeyRestrictionsOut"])
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
    types["V2RestrictionsIn"] = t.struct(
        {
            "browserKeyRestrictions": t.proxy(
                renames["V2BrowserKeyRestrictionsIn"]
            ).optional(),
            "serverKeyRestrictions": t.proxy(
                renames["V2ServerKeyRestrictionsIn"]
            ).optional(),
            "apiTargets": t.array(t.proxy(renames["V2ApiTargetIn"])).optional(),
            "androidKeyRestrictions": t.proxy(
                renames["V2AndroidKeyRestrictionsIn"]
            ).optional(),
            "iosKeyRestrictions": t.proxy(renames["V2IosKeyRestrictionsIn"]).optional(),
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
            "apiTargets": t.array(t.proxy(renames["V2ApiTargetOut"])).optional(),
            "androidKeyRestrictions": t.proxy(
                renames["V2AndroidKeyRestrictionsOut"]
            ).optional(),
            "iosKeyRestrictions": t.proxy(
                renames["V2IosKeyRestrictionsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V2RestrictionsOut"])
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
    functions["projectsLocationsKeysGet"] = apikeys.post(
        "v2/{parent}/keys",
        t.struct(
            {
                "keyId": t.string().optional(),
                "parent": t.string(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "restrictions": t.proxy(renames["V2RestrictionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeysGetKeyString"] = apikeys.post(
        "v2/{parent}/keys",
        t.struct(
            {
                "keyId": t.string().optional(),
                "parent": t.string(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "restrictions": t.proxy(renames["V2RestrictionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeysUndelete"] = apikeys.post(
        "v2/{parent}/keys",
        t.struct(
            {
                "keyId": t.string().optional(),
                "parent": t.string(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "restrictions": t.proxy(renames["V2RestrictionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeysPatch"] = apikeys.post(
        "v2/{parent}/keys",
        t.struct(
            {
                "keyId": t.string().optional(),
                "parent": t.string(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "restrictions": t.proxy(renames["V2RestrictionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeysDelete"] = apikeys.post(
        "v2/{parent}/keys",
        t.struct(
            {
                "keyId": t.string().optional(),
                "parent": t.string(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "restrictions": t.proxy(renames["V2RestrictionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeysList"] = apikeys.post(
        "v2/{parent}/keys",
        t.struct(
            {
                "keyId": t.string().optional(),
                "parent": t.string(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "restrictions": t.proxy(renames["V2RestrictionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeysCreate"] = apikeys.post(
        "v2/{parent}/keys",
        t.struct(
            {
                "keyId": t.string().optional(),
                "parent": t.string(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "restrictions": t.proxy(renames["V2RestrictionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="apikeys", renames=renames, types=Box(types), functions=Box(functions)
    )
