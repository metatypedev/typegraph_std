from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_playintegrity():
    playintegrity = HTTPRuntime("https://playintegrity.googleapis.com/")

    renames = {
        "ErrorResponse": "_playintegrity_1_ErrorResponse",
        "DecodeIntegrityTokenRequestIn": "_playintegrity_2_DecodeIntegrityTokenRequestIn",
        "DecodeIntegrityTokenRequestOut": "_playintegrity_3_DecodeIntegrityTokenRequestOut",
        "AppIntegrityIn": "_playintegrity_4_AppIntegrityIn",
        "AppIntegrityOut": "_playintegrity_5_AppIntegrityOut",
        "DeviceIntegrityIn": "_playintegrity_6_DeviceIntegrityIn",
        "DeviceIntegrityOut": "_playintegrity_7_DeviceIntegrityOut",
        "TestingDetailsIn": "_playintegrity_8_TestingDetailsIn",
        "TestingDetailsOut": "_playintegrity_9_TestingDetailsOut",
        "GuidanceDetailsIn": "_playintegrity_10_GuidanceDetailsIn",
        "GuidanceDetailsOut": "_playintegrity_11_GuidanceDetailsOut",
        "RequestDetailsIn": "_playintegrity_12_RequestDetailsIn",
        "RequestDetailsOut": "_playintegrity_13_RequestDetailsOut",
        "AccountDetailsIn": "_playintegrity_14_AccountDetailsIn",
        "AccountDetailsOut": "_playintegrity_15_AccountDetailsOut",
        "DecodeIntegrityTokenResponseIn": "_playintegrity_16_DecodeIntegrityTokenResponseIn",
        "DecodeIntegrityTokenResponseOut": "_playintegrity_17_DecodeIntegrityTokenResponseOut",
        "TokenPayloadExternalIn": "_playintegrity_18_TokenPayloadExternalIn",
        "TokenPayloadExternalOut": "_playintegrity_19_TokenPayloadExternalOut",
        "AccountActivityIn": "_playintegrity_20_AccountActivityIn",
        "AccountActivityOut": "_playintegrity_21_AccountActivityOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
            "packageName": t.string().optional(),
            "versionCode": t.string().optional(),
        }
    ).named(renames["AppIntegrityIn"])
    types["AppIntegrityOut"] = t.struct(
        {
            "appRecognitionVerdict": t.string(),
            "certificateSha256Digest": t.array(t.string()).optional(),
            "packageName": t.string().optional(),
            "versionCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppIntegrityOut"])
    types["DeviceIntegrityIn"] = t.struct(
        {"deviceRecognitionVerdict": t.array(t.string()).optional()}
    ).named(renames["DeviceIntegrityIn"])
    types["DeviceIntegrityOut"] = t.struct(
        {
            "deviceRecognitionVerdict": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceIntegrityOut"])
    types["TestingDetailsIn"] = t.struct({"isTestingResponse": t.boolean()}).named(
        renames["TestingDetailsIn"]
    )
    types["TestingDetailsOut"] = t.struct(
        {
            "isTestingResponse": t.boolean(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestingDetailsOut"])
    types["GuidanceDetailsIn"] = t.struct(
        {"userRemediation": t.array(t.string()).optional()}
    ).named(renames["GuidanceDetailsIn"])
    types["GuidanceDetailsOut"] = t.struct(
        {
            "userRemediation": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GuidanceDetailsOut"])
    types["RequestDetailsIn"] = t.struct(
        {
            "requestPackageName": t.string(),
            "nonce": t.string().optional(),
            "timestampMillis": t.string(),
            "requestHash": t.string().optional(),
        }
    ).named(renames["RequestDetailsIn"])
    types["RequestDetailsOut"] = t.struct(
        {
            "requestPackageName": t.string(),
            "nonce": t.string().optional(),
            "timestampMillis": t.string(),
            "requestHash": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestDetailsOut"])
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
            "deviceIntegrity": t.proxy(renames["DeviceIntegrityIn"]),
            "accountDetails": t.proxy(renames["AccountDetailsIn"]),
            "testingDetails": t.proxy(renames["TestingDetailsIn"]).optional(),
            "appIntegrity": t.proxy(renames["AppIntegrityIn"]),
            "requestDetails": t.proxy(renames["RequestDetailsIn"]),
            "guidanceDetails": t.proxy(renames["GuidanceDetailsIn"]).optional(),
        }
    ).named(renames["TokenPayloadExternalIn"])
    types["TokenPayloadExternalOut"] = t.struct(
        {
            "deviceIntegrity": t.proxy(renames["DeviceIntegrityOut"]),
            "accountDetails": t.proxy(renames["AccountDetailsOut"]),
            "testingDetails": t.proxy(renames["TestingDetailsOut"]).optional(),
            "appIntegrity": t.proxy(renames["AppIntegrityOut"]),
            "requestDetails": t.proxy(renames["RequestDetailsOut"]),
            "guidanceDetails": t.proxy(renames["GuidanceDetailsOut"]).optional(),
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
