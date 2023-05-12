from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_playintegrity() -> Import:
    playintegrity = HTTPRuntime("https://playintegrity.googleapis.com/")

    renames = {
        "ErrorResponse": "_playintegrity_1_ErrorResponse",
        "DeviceIntegrityIn": "_playintegrity_2_DeviceIntegrityIn",
        "DeviceIntegrityOut": "_playintegrity_3_DeviceIntegrityOut",
        "DecodeIntegrityTokenResponseIn": "_playintegrity_4_DecodeIntegrityTokenResponseIn",
        "DecodeIntegrityTokenResponseOut": "_playintegrity_5_DecodeIntegrityTokenResponseOut",
        "DecodeIntegrityTokenRequestIn": "_playintegrity_6_DecodeIntegrityTokenRequestIn",
        "DecodeIntegrityTokenRequestOut": "_playintegrity_7_DecodeIntegrityTokenRequestOut",
        "TokenPayloadExternalIn": "_playintegrity_8_TokenPayloadExternalIn",
        "TokenPayloadExternalOut": "_playintegrity_9_TokenPayloadExternalOut",
        "AccountActivityIn": "_playintegrity_10_AccountActivityIn",
        "AccountActivityOut": "_playintegrity_11_AccountActivityOut",
        "TestingDetailsIn": "_playintegrity_12_TestingDetailsIn",
        "TestingDetailsOut": "_playintegrity_13_TestingDetailsOut",
        "RequestDetailsIn": "_playintegrity_14_RequestDetailsIn",
        "RequestDetailsOut": "_playintegrity_15_RequestDetailsOut",
        "AppIntegrityIn": "_playintegrity_16_AppIntegrityIn",
        "AppIntegrityOut": "_playintegrity_17_AppIntegrityOut",
        "AccountDetailsIn": "_playintegrity_18_AccountDetailsIn",
        "AccountDetailsOut": "_playintegrity_19_AccountDetailsOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["DeviceIntegrityIn"] = t.struct(
        {"deviceRecognitionVerdict": t.array(t.string()).optional()}
    ).named(renames["DeviceIntegrityIn"])
    types["DeviceIntegrityOut"] = t.struct(
        {
            "deviceRecognitionVerdict": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceIntegrityOut"])
    types["DecodeIntegrityTokenResponseIn"] = t.struct(
        {"tokenPayloadExternal": t.proxy(renames["TokenPayloadExternalIn"]).optional()}
    ).named(renames["DecodeIntegrityTokenResponseIn"])
    types["DecodeIntegrityTokenResponseOut"] = t.struct(
        {
            "tokenPayloadExternal": t.proxy(
                renames["TokenPayloadExternalOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DecodeIntegrityTokenResponseOut"])
    types["DecodeIntegrityTokenRequestIn"] = t.struct(
        {"integrityToken": t.string().optional()}
    ).named(renames["DecodeIntegrityTokenRequestIn"])
    types["DecodeIntegrityTokenRequestOut"] = t.struct(
        {
            "integrityToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DecodeIntegrityTokenRequestOut"])
    types["TokenPayloadExternalIn"] = t.struct(
        {
            "testingDetails": t.proxy(renames["TestingDetailsIn"]).optional(),
            "requestDetails": t.proxy(renames["RequestDetailsIn"]),
            "appIntegrity": t.proxy(renames["AppIntegrityIn"]),
            "accountDetails": t.proxy(renames["AccountDetailsIn"]),
            "deviceIntegrity": t.proxy(renames["DeviceIntegrityIn"]),
        }
    ).named(renames["TokenPayloadExternalIn"])
    types["TokenPayloadExternalOut"] = t.struct(
        {
            "testingDetails": t.proxy(renames["TestingDetailsOut"]).optional(),
            "requestDetails": t.proxy(renames["RequestDetailsOut"]),
            "appIntegrity": t.proxy(renames["AppIntegrityOut"]),
            "accountDetails": t.proxy(renames["AccountDetailsOut"]),
            "deviceIntegrity": t.proxy(renames["DeviceIntegrityOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TokenPayloadExternalOut"])
    types["AccountActivityIn"] = t.struct({"activityLevel": t.string()}).named(
        renames["AccountActivityIn"]
    )
    types["AccountActivityOut"] = t.struct(
        {
            "activityLevel": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountActivityOut"])
    types["TestingDetailsIn"] = t.struct({"isTestingResponse": t.boolean()}).named(
        renames["TestingDetailsIn"]
    )
    types["TestingDetailsOut"] = t.struct(
        {
            "isTestingResponse": t.boolean(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestingDetailsOut"])
    types["RequestDetailsIn"] = t.struct(
        {
            "requestHash": t.string().optional(),
            "requestPackageName": t.string(),
            "timestampMillis": t.string(),
            "nonce": t.string().optional(),
        }
    ).named(renames["RequestDetailsIn"])
    types["RequestDetailsOut"] = t.struct(
        {
            "requestHash": t.string().optional(),
            "requestPackageName": t.string(),
            "timestampMillis": t.string(),
            "nonce": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestDetailsOut"])
    types["AppIntegrityIn"] = t.struct(
        {
            "certificateSha256Digest": t.array(t.string()).optional(),
            "versionCode": t.string().optional(),
            "appRecognitionVerdict": t.string(),
            "packageName": t.string().optional(),
        }
    ).named(renames["AppIntegrityIn"])
    types["AppIntegrityOut"] = t.struct(
        {
            "certificateSha256Digest": t.array(t.string()).optional(),
            "versionCode": t.string().optional(),
            "appRecognitionVerdict": t.string(),
            "packageName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppIntegrityOut"])
    types["AccountDetailsIn"] = t.struct(
        {
            "accountActivity": t.proxy(renames["AccountActivityIn"]).optional(),
            "appLicensingVerdict": t.string(),
        }
    ).named(renames["AccountDetailsIn"])
    types["AccountDetailsOut"] = t.struct(
        {
            "accountActivity": t.proxy(renames["AccountActivityOut"]).optional(),
            "appLicensingVerdict": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountDetailsOut"])

    functions = {}
    functions["v1DecodeIntegrityToken"] = playintegrity.post(
        "v1/{packageName}:decodeIntegrityToken",
        t.struct(
            {
                "packageName": t.string().optional(),
                "integrityToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DecodeIntegrityTokenResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="playintegrity",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
