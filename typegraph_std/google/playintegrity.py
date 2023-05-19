from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_playintegrity() -> Import:
    playintegrity = HTTPRuntime("https://playintegrity.googleapis.com/")

    renames = {
        "ErrorResponse": "_playintegrity_1_ErrorResponse",
        "AppIntegrityIn": "_playintegrity_2_AppIntegrityIn",
        "AppIntegrityOut": "_playintegrity_3_AppIntegrityOut",
        "TestingDetailsIn": "_playintegrity_4_TestingDetailsIn",
        "TestingDetailsOut": "_playintegrity_5_TestingDetailsOut",
        "DecodeIntegrityTokenRequestIn": "_playintegrity_6_DecodeIntegrityTokenRequestIn",
        "DecodeIntegrityTokenRequestOut": "_playintegrity_7_DecodeIntegrityTokenRequestOut",
        "TokenPayloadExternalIn": "_playintegrity_8_TokenPayloadExternalIn",
        "TokenPayloadExternalOut": "_playintegrity_9_TokenPayloadExternalOut",
        "RequestDetailsIn": "_playintegrity_10_RequestDetailsIn",
        "RequestDetailsOut": "_playintegrity_11_RequestDetailsOut",
        "GuidanceDetailsIn": "_playintegrity_12_GuidanceDetailsIn",
        "GuidanceDetailsOut": "_playintegrity_13_GuidanceDetailsOut",
        "AccountDetailsIn": "_playintegrity_14_AccountDetailsIn",
        "AccountDetailsOut": "_playintegrity_15_AccountDetailsOut",
        "DecodeIntegrityTokenResponseIn": "_playintegrity_16_DecodeIntegrityTokenResponseIn",
        "DecodeIntegrityTokenResponseOut": "_playintegrity_17_DecodeIntegrityTokenResponseOut",
        "AccountActivityIn": "_playintegrity_18_AccountActivityIn",
        "AccountActivityOut": "_playintegrity_19_AccountActivityOut",
        "DeviceIntegrityIn": "_playintegrity_20_DeviceIntegrityIn",
        "DeviceIntegrityOut": "_playintegrity_21_DeviceIntegrityOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["AppIntegrityIn"] = t.struct(
        {
            "packageName": t.string().optional(),
            "appRecognitionVerdict": t.string(),
            "certificateSha256Digest": t.array(t.string()).optional(),
            "versionCode": t.string().optional(),
        }
    ).named(renames["AppIntegrityIn"])
    types["AppIntegrityOut"] = t.struct(
        {
            "packageName": t.string().optional(),
            "appRecognitionVerdict": t.string(),
            "certificateSha256Digest": t.array(t.string()).optional(),
            "versionCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppIntegrityOut"])
    types["TestingDetailsIn"] = t.struct({"isTestingResponse": t.boolean()}).named(
        renames["TestingDetailsIn"]
    )
    types["TestingDetailsOut"] = t.struct(
        {
            "isTestingResponse": t.boolean(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestingDetailsOut"])
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
            "appIntegrity": t.proxy(renames["AppIntegrityIn"]),
            "requestDetails": t.proxy(renames["RequestDetailsIn"]),
            "accountDetails": t.proxy(renames["AccountDetailsIn"]),
            "deviceIntegrity": t.proxy(renames["DeviceIntegrityIn"]),
            "guidanceDetails": t.proxy(renames["GuidanceDetailsIn"]).optional(),
            "testingDetails": t.proxy(renames["TestingDetailsIn"]).optional(),
        }
    ).named(renames["TokenPayloadExternalIn"])
    types["TokenPayloadExternalOut"] = t.struct(
        {
            "appIntegrity": t.proxy(renames["AppIntegrityOut"]),
            "requestDetails": t.proxy(renames["RequestDetailsOut"]),
            "accountDetails": t.proxy(renames["AccountDetailsOut"]),
            "deviceIntegrity": t.proxy(renames["DeviceIntegrityOut"]),
            "guidanceDetails": t.proxy(renames["GuidanceDetailsOut"]).optional(),
            "testingDetails": t.proxy(renames["TestingDetailsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TokenPayloadExternalOut"])
    types["RequestDetailsIn"] = t.struct(
        {
            "nonce": t.string().optional(),
            "timestampMillis": t.string(),
            "requestHash": t.string().optional(),
            "requestPackageName": t.string(),
        }
    ).named(renames["RequestDetailsIn"])
    types["RequestDetailsOut"] = t.struct(
        {
            "nonce": t.string().optional(),
            "timestampMillis": t.string(),
            "requestHash": t.string().optional(),
            "requestPackageName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestDetailsOut"])
    types["GuidanceDetailsIn"] = t.struct(
        {"userRemediation": t.array(t.string()).optional()}
    ).named(renames["GuidanceDetailsIn"])
    types["GuidanceDetailsOut"] = t.struct(
        {
            "userRemediation": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GuidanceDetailsOut"])
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
    types["AccountActivityIn"] = t.struct({"activityLevel": t.string()}).named(
        renames["AccountActivityIn"]
    )
    types["AccountActivityOut"] = t.struct(
        {
            "activityLevel": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountActivityOut"])
    types["DeviceIntegrityIn"] = t.struct(
        {"deviceRecognitionVerdict": t.array(t.string()).optional()}
    ).named(renames["DeviceIntegrityIn"])
    types["DeviceIntegrityOut"] = t.struct(
        {
            "deviceRecognitionVerdict": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceIntegrityOut"])

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
