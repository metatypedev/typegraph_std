from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_playintegrity() -> Import:
    playintegrity = HTTPRuntime("https://playintegrity.googleapis.com/")

    renames = {
        "ErrorResponse": "_playintegrity_1_ErrorResponse",
        "DecodeIntegrityTokenResponseIn": "_playintegrity_2_DecodeIntegrityTokenResponseIn",
        "DecodeIntegrityTokenResponseOut": "_playintegrity_3_DecodeIntegrityTokenResponseOut",
        "TokenPayloadExternalIn": "_playintegrity_4_TokenPayloadExternalIn",
        "TokenPayloadExternalOut": "_playintegrity_5_TokenPayloadExternalOut",
        "TestingDetailsIn": "_playintegrity_6_TestingDetailsIn",
        "TestingDetailsOut": "_playintegrity_7_TestingDetailsOut",
        "AccountDetailsIn": "_playintegrity_8_AccountDetailsIn",
        "AccountDetailsOut": "_playintegrity_9_AccountDetailsOut",
        "DeviceIntegrityIn": "_playintegrity_10_DeviceIntegrityIn",
        "DeviceIntegrityOut": "_playintegrity_11_DeviceIntegrityOut",
        "DecodeIntegrityTokenRequestIn": "_playintegrity_12_DecodeIntegrityTokenRequestIn",
        "DecodeIntegrityTokenRequestOut": "_playintegrity_13_DecodeIntegrityTokenRequestOut",
        "AppIntegrityIn": "_playintegrity_14_AppIntegrityIn",
        "AppIntegrityOut": "_playintegrity_15_AppIntegrityOut",
        "AccountActivityIn": "_playintegrity_16_AccountActivityIn",
        "AccountActivityOut": "_playintegrity_17_AccountActivityOut",
        "RequestDetailsIn": "_playintegrity_18_RequestDetailsIn",
        "RequestDetailsOut": "_playintegrity_19_RequestDetailsOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["TokenPayloadExternalIn"] = t.struct(
        {
            "appIntegrity": t.proxy(renames["AppIntegrityIn"]),
            "requestDetails": t.proxy(renames["RequestDetailsIn"]),
            "accountDetails": t.proxy(renames["AccountDetailsIn"]),
            "testingDetails": t.proxy(renames["TestingDetailsIn"]).optional(),
            "deviceIntegrity": t.proxy(renames["DeviceIntegrityIn"]),
        }
    ).named(renames["TokenPayloadExternalIn"])
    types["TokenPayloadExternalOut"] = t.struct(
        {
            "appIntegrity": t.proxy(renames["AppIntegrityOut"]),
            "requestDetails": t.proxy(renames["RequestDetailsOut"]),
            "accountDetails": t.proxy(renames["AccountDetailsOut"]),
            "testingDetails": t.proxy(renames["TestingDetailsOut"]).optional(),
            "deviceIntegrity": t.proxy(renames["DeviceIntegrityOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TokenPayloadExternalOut"])
    types["TestingDetailsIn"] = t.struct({"isTestingResponse": t.boolean()}).named(
        renames["TestingDetailsIn"]
    )
    types["TestingDetailsOut"] = t.struct(
        {
            "isTestingResponse": t.boolean(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestingDetailsOut"])
    types["AccountDetailsIn"] = t.struct(
        {
            "appLicensingVerdict": t.string(),
            "accountActivity": t.proxy(renames["AccountActivityIn"]).optional(),
        }
    ).named(renames["AccountDetailsIn"])
    types["AccountDetailsOut"] = t.struct(
        {
            "appLicensingVerdict": t.string(),
            "accountActivity": t.proxy(renames["AccountActivityOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountDetailsOut"])
    types["DeviceIntegrityIn"] = t.struct(
        {"deviceRecognitionVerdict": t.array(t.string()).optional()}
    ).named(renames["DeviceIntegrityIn"])
    types["DeviceIntegrityOut"] = t.struct(
        {
            "deviceRecognitionVerdict": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceIntegrityOut"])
    types["DecodeIntegrityTokenRequestIn"] = t.struct(
        {"integrityToken": t.string().optional()}
    ).named(renames["DecodeIntegrityTokenRequestIn"])
    types["DecodeIntegrityTokenRequestOut"] = t.struct(
        {
            "integrityToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DecodeIntegrityTokenRequestOut"])
    types["AppIntegrityIn"] = t.struct(
        {
            "appRecognitionVerdict": t.string(),
            "certificateSha256Digest": t.array(t.string()).optional(),
            "versionCode": t.string().optional(),
            "packageName": t.string().optional(),
        }
    ).named(renames["AppIntegrityIn"])
    types["AppIntegrityOut"] = t.struct(
        {
            "appRecognitionVerdict": t.string(),
            "certificateSha256Digest": t.array(t.string()).optional(),
            "versionCode": t.string().optional(),
            "packageName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppIntegrityOut"])
    types["AccountActivityIn"] = t.struct({"activityLevel": t.string()}).named(
        renames["AccountActivityIn"]
    )
    types["AccountActivityOut"] = t.struct(
        {
            "activityLevel": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountActivityOut"])
    types["RequestDetailsIn"] = t.struct(
        {
            "timestampMillis": t.string(),
            "nonce": t.string().optional(),
            "requestPackageName": t.string(),
            "requestHash": t.string().optional(),
        }
    ).named(renames["RequestDetailsIn"])
    types["RequestDetailsOut"] = t.struct(
        {
            "timestampMillis": t.string(),
            "nonce": t.string().optional(),
            "requestPackageName": t.string(),
            "requestHash": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestDetailsOut"])

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
        importer="playintegrity", renames=renames, types=types, functions=functions
    )
