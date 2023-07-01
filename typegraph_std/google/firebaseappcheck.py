from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_firebaseappcheck():
    firebaseappcheck = HTTPRuntime("https://firebaseappcheck.googleapis.com/")

    renames = {
        "ErrorResponse": "_firebaseappcheck_1_ErrorResponse",
        "GoogleFirebaseAppcheckV1ServiceIn": "_firebaseappcheck_2_GoogleFirebaseAppcheckV1ServiceIn",
        "GoogleFirebaseAppcheckV1ServiceOut": "_firebaseappcheck_3_GoogleFirebaseAppcheckV1ServiceOut",
        "GoogleFirebaseAppcheckV1BatchUpdateServicesResponseIn": "_firebaseappcheck_4_GoogleFirebaseAppcheckV1BatchUpdateServicesResponseIn",
        "GoogleFirebaseAppcheckV1BatchUpdateServicesResponseOut": "_firebaseappcheck_5_GoogleFirebaseAppcheckV1BatchUpdateServicesResponseOut",
        "GoogleFirebaseAppcheckV1ExchangeSafetyNetTokenRequestIn": "_firebaseappcheck_6_GoogleFirebaseAppcheckV1ExchangeSafetyNetTokenRequestIn",
        "GoogleFirebaseAppcheckV1ExchangeSafetyNetTokenRequestOut": "_firebaseappcheck_7_GoogleFirebaseAppcheckV1ExchangeSafetyNetTokenRequestOut",
        "GoogleFirebaseAppcheckV1PublicJwkIn": "_firebaseappcheck_8_GoogleFirebaseAppcheckV1PublicJwkIn",
        "GoogleFirebaseAppcheckV1PublicJwkOut": "_firebaseappcheck_9_GoogleFirebaseAppcheckV1PublicJwkOut",
        "GoogleFirebaseAppcheckV1GenerateAppAttestChallengeRequestIn": "_firebaseappcheck_10_GoogleFirebaseAppcheckV1GenerateAppAttestChallengeRequestIn",
        "GoogleFirebaseAppcheckV1GenerateAppAttestChallengeRequestOut": "_firebaseappcheck_11_GoogleFirebaseAppcheckV1GenerateAppAttestChallengeRequestOut",
        "GoogleFirebaseAppcheckV1BatchGetDeviceCheckConfigsResponseIn": "_firebaseappcheck_12_GoogleFirebaseAppcheckV1BatchGetDeviceCheckConfigsResponseIn",
        "GoogleFirebaseAppcheckV1BatchGetDeviceCheckConfigsResponseOut": "_firebaseappcheck_13_GoogleFirebaseAppcheckV1BatchGetDeviceCheckConfigsResponseOut",
        "GoogleFirebaseAppcheckV1ListServicesResponseIn": "_firebaseappcheck_14_GoogleFirebaseAppcheckV1ListServicesResponseIn",
        "GoogleFirebaseAppcheckV1ListServicesResponseOut": "_firebaseappcheck_15_GoogleFirebaseAppcheckV1ListServicesResponseOut",
        "GoogleProtobufEmptyIn": "_firebaseappcheck_16_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_firebaseappcheck_17_GoogleProtobufEmptyOut",
        "GoogleFirebaseAppcheckV1ExchangeAppAttestAssertionRequestIn": "_firebaseappcheck_18_GoogleFirebaseAppcheckV1ExchangeAppAttestAssertionRequestIn",
        "GoogleFirebaseAppcheckV1ExchangeAppAttestAssertionRequestOut": "_firebaseappcheck_19_GoogleFirebaseAppcheckV1ExchangeAppAttestAssertionRequestOut",
        "GoogleFirebaseAppcheckV1GenerateAppAttestChallengeResponseIn": "_firebaseappcheck_20_GoogleFirebaseAppcheckV1GenerateAppAttestChallengeResponseIn",
        "GoogleFirebaseAppcheckV1GenerateAppAttestChallengeResponseOut": "_firebaseappcheck_21_GoogleFirebaseAppcheckV1GenerateAppAttestChallengeResponseOut",
        "GoogleFirebaseAppcheckV1ExchangeRecaptchaEnterpriseTokenRequestIn": "_firebaseappcheck_22_GoogleFirebaseAppcheckV1ExchangeRecaptchaEnterpriseTokenRequestIn",
        "GoogleFirebaseAppcheckV1ExchangeRecaptchaEnterpriseTokenRequestOut": "_firebaseappcheck_23_GoogleFirebaseAppcheckV1ExchangeRecaptchaEnterpriseTokenRequestOut",
        "GoogleFirebaseAppcheckV1BatchGetAppAttestConfigsResponseIn": "_firebaseappcheck_24_GoogleFirebaseAppcheckV1BatchGetAppAttestConfigsResponseIn",
        "GoogleFirebaseAppcheckV1BatchGetAppAttestConfigsResponseOut": "_firebaseappcheck_25_GoogleFirebaseAppcheckV1BatchGetAppAttestConfigsResponseOut",
        "GoogleFirebaseAppcheckV1AppCheckTokenIn": "_firebaseappcheck_26_GoogleFirebaseAppcheckV1AppCheckTokenIn",
        "GoogleFirebaseAppcheckV1AppCheckTokenOut": "_firebaseappcheck_27_GoogleFirebaseAppcheckV1AppCheckTokenOut",
        "GoogleFirebaseAppcheckV1RecaptchaV3ConfigIn": "_firebaseappcheck_28_GoogleFirebaseAppcheckV1RecaptchaV3ConfigIn",
        "GoogleFirebaseAppcheckV1RecaptchaV3ConfigOut": "_firebaseappcheck_29_GoogleFirebaseAppcheckV1RecaptchaV3ConfigOut",
        "GoogleFirebaseAppcheckV1ExchangeRecaptchaV3TokenRequestIn": "_firebaseappcheck_30_GoogleFirebaseAppcheckV1ExchangeRecaptchaV3TokenRequestIn",
        "GoogleFirebaseAppcheckV1ExchangeRecaptchaV3TokenRequestOut": "_firebaseappcheck_31_GoogleFirebaseAppcheckV1ExchangeRecaptchaV3TokenRequestOut",
        "GoogleFirebaseAppcheckV1BatchGetSafetyNetConfigsResponseIn": "_firebaseappcheck_32_GoogleFirebaseAppcheckV1BatchGetSafetyNetConfigsResponseIn",
        "GoogleFirebaseAppcheckV1BatchGetSafetyNetConfigsResponseOut": "_firebaseappcheck_33_GoogleFirebaseAppcheckV1BatchGetSafetyNetConfigsResponseOut",
        "GoogleFirebaseAppcheckV1BatchGetPlayIntegrityConfigsResponseIn": "_firebaseappcheck_34_GoogleFirebaseAppcheckV1BatchGetPlayIntegrityConfigsResponseIn",
        "GoogleFirebaseAppcheckV1BatchGetPlayIntegrityConfigsResponseOut": "_firebaseappcheck_35_GoogleFirebaseAppcheckV1BatchGetPlayIntegrityConfigsResponseOut",
        "GoogleFirebaseAppcheckV1PlayIntegrityConfigIn": "_firebaseappcheck_36_GoogleFirebaseAppcheckV1PlayIntegrityConfigIn",
        "GoogleFirebaseAppcheckV1PlayIntegrityConfigOut": "_firebaseappcheck_37_GoogleFirebaseAppcheckV1PlayIntegrityConfigOut",
        "GoogleFirebaseAppcheckV1BatchUpdateServicesRequestIn": "_firebaseappcheck_38_GoogleFirebaseAppcheckV1BatchUpdateServicesRequestIn",
        "GoogleFirebaseAppcheckV1BatchUpdateServicesRequestOut": "_firebaseappcheck_39_GoogleFirebaseAppcheckV1BatchUpdateServicesRequestOut",
        "GoogleFirebaseAppcheckV1PublicJwkSetIn": "_firebaseappcheck_40_GoogleFirebaseAppcheckV1PublicJwkSetIn",
        "GoogleFirebaseAppcheckV1PublicJwkSetOut": "_firebaseappcheck_41_GoogleFirebaseAppcheckV1PublicJwkSetOut",
        "GoogleFirebaseAppcheckV1BatchGetRecaptchaEnterpriseConfigsResponseIn": "_firebaseappcheck_42_GoogleFirebaseAppcheckV1BatchGetRecaptchaEnterpriseConfigsResponseIn",
        "GoogleFirebaseAppcheckV1BatchGetRecaptchaEnterpriseConfigsResponseOut": "_firebaseappcheck_43_GoogleFirebaseAppcheckV1BatchGetRecaptchaEnterpriseConfigsResponseOut",
        "GoogleFirebaseAppcheckV1AppAttestConfigIn": "_firebaseappcheck_44_GoogleFirebaseAppcheckV1AppAttestConfigIn",
        "GoogleFirebaseAppcheckV1AppAttestConfigOut": "_firebaseappcheck_45_GoogleFirebaseAppcheckV1AppAttestConfigOut",
        "GoogleFirebaseAppcheckV1DebugTokenIn": "_firebaseappcheck_46_GoogleFirebaseAppcheckV1DebugTokenIn",
        "GoogleFirebaseAppcheckV1DebugTokenOut": "_firebaseappcheck_47_GoogleFirebaseAppcheckV1DebugTokenOut",
        "GoogleFirebaseAppcheckV1ListDebugTokensResponseIn": "_firebaseappcheck_48_GoogleFirebaseAppcheckV1ListDebugTokensResponseIn",
        "GoogleFirebaseAppcheckV1ListDebugTokensResponseOut": "_firebaseappcheck_49_GoogleFirebaseAppcheckV1ListDebugTokensResponseOut",
        "GoogleFirebaseAppcheckV1ExchangeDebugTokenRequestIn": "_firebaseappcheck_50_GoogleFirebaseAppcheckV1ExchangeDebugTokenRequestIn",
        "GoogleFirebaseAppcheckV1ExchangeDebugTokenRequestOut": "_firebaseappcheck_51_GoogleFirebaseAppcheckV1ExchangeDebugTokenRequestOut",
        "GoogleFirebaseAppcheckV1GeneratePlayIntegrityChallengeRequestIn": "_firebaseappcheck_52_GoogleFirebaseAppcheckV1GeneratePlayIntegrityChallengeRequestIn",
        "GoogleFirebaseAppcheckV1GeneratePlayIntegrityChallengeRequestOut": "_firebaseappcheck_53_GoogleFirebaseAppcheckV1GeneratePlayIntegrityChallengeRequestOut",
        "GoogleFirebaseAppcheckV1BatchGetRecaptchaV3ConfigsResponseIn": "_firebaseappcheck_54_GoogleFirebaseAppcheckV1BatchGetRecaptchaV3ConfigsResponseIn",
        "GoogleFirebaseAppcheckV1BatchGetRecaptchaV3ConfigsResponseOut": "_firebaseappcheck_55_GoogleFirebaseAppcheckV1BatchGetRecaptchaV3ConfigsResponseOut",
        "GoogleFirebaseAppcheckV1GeneratePlayIntegrityChallengeResponseIn": "_firebaseappcheck_56_GoogleFirebaseAppcheckV1GeneratePlayIntegrityChallengeResponseIn",
        "GoogleFirebaseAppcheckV1GeneratePlayIntegrityChallengeResponseOut": "_firebaseappcheck_57_GoogleFirebaseAppcheckV1GeneratePlayIntegrityChallengeResponseOut",
        "GoogleFirebaseAppcheckV1ExchangePlayIntegrityTokenRequestIn": "_firebaseappcheck_58_GoogleFirebaseAppcheckV1ExchangePlayIntegrityTokenRequestIn",
        "GoogleFirebaseAppcheckV1ExchangePlayIntegrityTokenRequestOut": "_firebaseappcheck_59_GoogleFirebaseAppcheckV1ExchangePlayIntegrityTokenRequestOut",
        "GoogleFirebaseAppcheckV1UpdateServiceRequestIn": "_firebaseappcheck_60_GoogleFirebaseAppcheckV1UpdateServiceRequestIn",
        "GoogleFirebaseAppcheckV1UpdateServiceRequestOut": "_firebaseappcheck_61_GoogleFirebaseAppcheckV1UpdateServiceRequestOut",
        "GoogleFirebaseAppcheckV1ExchangeCustomTokenRequestIn": "_firebaseappcheck_62_GoogleFirebaseAppcheckV1ExchangeCustomTokenRequestIn",
        "GoogleFirebaseAppcheckV1ExchangeCustomTokenRequestOut": "_firebaseappcheck_63_GoogleFirebaseAppcheckV1ExchangeCustomTokenRequestOut",
        "GoogleFirebaseAppcheckV1ExchangeAppAttestAttestationResponseIn": "_firebaseappcheck_64_GoogleFirebaseAppcheckV1ExchangeAppAttestAttestationResponseIn",
        "GoogleFirebaseAppcheckV1ExchangeAppAttestAttestationResponseOut": "_firebaseappcheck_65_GoogleFirebaseAppcheckV1ExchangeAppAttestAttestationResponseOut",
        "GoogleFirebaseAppcheckV1DeviceCheckConfigIn": "_firebaseappcheck_66_GoogleFirebaseAppcheckV1DeviceCheckConfigIn",
        "GoogleFirebaseAppcheckV1DeviceCheckConfigOut": "_firebaseappcheck_67_GoogleFirebaseAppcheckV1DeviceCheckConfigOut",
        "GoogleFirebaseAppcheckV1ExchangeDeviceCheckTokenRequestIn": "_firebaseappcheck_68_GoogleFirebaseAppcheckV1ExchangeDeviceCheckTokenRequestIn",
        "GoogleFirebaseAppcheckV1ExchangeDeviceCheckTokenRequestOut": "_firebaseappcheck_69_GoogleFirebaseAppcheckV1ExchangeDeviceCheckTokenRequestOut",
        "GoogleFirebaseAppcheckV1ExchangeAppAttestAttestationRequestIn": "_firebaseappcheck_70_GoogleFirebaseAppcheckV1ExchangeAppAttestAttestationRequestIn",
        "GoogleFirebaseAppcheckV1ExchangeAppAttestAttestationRequestOut": "_firebaseappcheck_71_GoogleFirebaseAppcheckV1ExchangeAppAttestAttestationRequestOut",
        "GoogleFirebaseAppcheckV1RecaptchaEnterpriseConfigIn": "_firebaseappcheck_72_GoogleFirebaseAppcheckV1RecaptchaEnterpriseConfigIn",
        "GoogleFirebaseAppcheckV1RecaptchaEnterpriseConfigOut": "_firebaseappcheck_73_GoogleFirebaseAppcheckV1RecaptchaEnterpriseConfigOut",
        "GoogleFirebaseAppcheckV1SafetyNetConfigIn": "_firebaseappcheck_74_GoogleFirebaseAppcheckV1SafetyNetConfigIn",
        "GoogleFirebaseAppcheckV1SafetyNetConfigOut": "_firebaseappcheck_75_GoogleFirebaseAppcheckV1SafetyNetConfigOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleFirebaseAppcheckV1ServiceIn"] = t.struct(
        {"enforcementMode": t.string(), "name": t.string()}
    ).named(renames["GoogleFirebaseAppcheckV1ServiceIn"])
    types["GoogleFirebaseAppcheckV1ServiceOut"] = t.struct(
        {
            "enforcementMode": t.string(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppcheckV1ServiceOut"])
    types["GoogleFirebaseAppcheckV1BatchUpdateServicesResponseIn"] = t.struct(
        {
            "services": t.array(
                t.proxy(renames["GoogleFirebaseAppcheckV1ServiceIn"])
            ).optional()
        }
    ).named(renames["GoogleFirebaseAppcheckV1BatchUpdateServicesResponseIn"])
    types["GoogleFirebaseAppcheckV1BatchUpdateServicesResponseOut"] = t.struct(
        {
            "services": t.array(
                t.proxy(renames["GoogleFirebaseAppcheckV1ServiceOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppcheckV1BatchUpdateServicesResponseOut"])
    types["GoogleFirebaseAppcheckV1ExchangeSafetyNetTokenRequestIn"] = t.struct(
        {"safetyNetToken": t.string()}
    ).named(renames["GoogleFirebaseAppcheckV1ExchangeSafetyNetTokenRequestIn"])
    types["GoogleFirebaseAppcheckV1ExchangeSafetyNetTokenRequestOut"] = t.struct(
        {
            "safetyNetToken": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppcheckV1ExchangeSafetyNetTokenRequestOut"])
    types["GoogleFirebaseAppcheckV1PublicJwkIn"] = t.struct(
        {
            "n": t.string().optional(),
            "use": t.string().optional(),
            "e": t.string().optional(),
            "kid": t.string().optional(),
            "alg": t.string().optional(),
            "kty": t.string().optional(),
        }
    ).named(renames["GoogleFirebaseAppcheckV1PublicJwkIn"])
    types["GoogleFirebaseAppcheckV1PublicJwkOut"] = t.struct(
        {
            "n": t.string().optional(),
            "use": t.string().optional(),
            "e": t.string().optional(),
            "kid": t.string().optional(),
            "alg": t.string().optional(),
            "kty": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppcheckV1PublicJwkOut"])
    types["GoogleFirebaseAppcheckV1GenerateAppAttestChallengeRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleFirebaseAppcheckV1GenerateAppAttestChallengeRequestIn"])
    types["GoogleFirebaseAppcheckV1GenerateAppAttestChallengeRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleFirebaseAppcheckV1GenerateAppAttestChallengeRequestOut"])
    types["GoogleFirebaseAppcheckV1BatchGetDeviceCheckConfigsResponseIn"] = t.struct(
        {
            "configs": t.array(
                t.proxy(renames["GoogleFirebaseAppcheckV1DeviceCheckConfigIn"])
            ).optional()
        }
    ).named(renames["GoogleFirebaseAppcheckV1BatchGetDeviceCheckConfigsResponseIn"])
    types["GoogleFirebaseAppcheckV1BatchGetDeviceCheckConfigsResponseOut"] = t.struct(
        {
            "configs": t.array(
                t.proxy(renames["GoogleFirebaseAppcheckV1DeviceCheckConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppcheckV1BatchGetDeviceCheckConfigsResponseOut"])
    types["GoogleFirebaseAppcheckV1ListServicesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "services": t.array(
                t.proxy(renames["GoogleFirebaseAppcheckV1ServiceIn"])
            ).optional(),
        }
    ).named(renames["GoogleFirebaseAppcheckV1ListServicesResponseIn"])
    types["GoogleFirebaseAppcheckV1ListServicesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "services": t.array(
                t.proxy(renames["GoogleFirebaseAppcheckV1ServiceOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppcheckV1ListServicesResponseOut"])
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
    types["GoogleFirebaseAppcheckV1ExchangeAppAttestAssertionRequestIn"] = t.struct(
        {
            "assertion": t.string(),
            "artifact": t.string(),
            "limitedUse": t.boolean().optional(),
            "challenge": t.string(),
        }
    ).named(renames["GoogleFirebaseAppcheckV1ExchangeAppAttestAssertionRequestIn"])
    types["GoogleFirebaseAppcheckV1ExchangeAppAttestAssertionRequestOut"] = t.struct(
        {
            "assertion": t.string(),
            "artifact": t.string(),
            "limitedUse": t.boolean().optional(),
            "challenge": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppcheckV1ExchangeAppAttestAssertionRequestOut"])
    types["GoogleFirebaseAppcheckV1GenerateAppAttestChallengeResponseIn"] = t.struct(
        {"ttl": t.string().optional(), "challenge": t.string().optional()}
    ).named(renames["GoogleFirebaseAppcheckV1GenerateAppAttestChallengeResponseIn"])
    types["GoogleFirebaseAppcheckV1GenerateAppAttestChallengeResponseOut"] = t.struct(
        {
            "ttl": t.string().optional(),
            "challenge": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppcheckV1GenerateAppAttestChallengeResponseOut"])
    types[
        "GoogleFirebaseAppcheckV1ExchangeRecaptchaEnterpriseTokenRequestIn"
    ] = t.struct(
        {"recaptchaEnterpriseToken": t.string(), "limitedUse": t.boolean().optional()}
    ).named(
        renames["GoogleFirebaseAppcheckV1ExchangeRecaptchaEnterpriseTokenRequestIn"]
    )
    types[
        "GoogleFirebaseAppcheckV1ExchangeRecaptchaEnterpriseTokenRequestOut"
    ] = t.struct(
        {
            "recaptchaEnterpriseToken": t.string(),
            "limitedUse": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleFirebaseAppcheckV1ExchangeRecaptchaEnterpriseTokenRequestOut"]
    )
    types["GoogleFirebaseAppcheckV1BatchGetAppAttestConfigsResponseIn"] = t.struct(
        {
            "configs": t.array(
                t.proxy(renames["GoogleFirebaseAppcheckV1AppAttestConfigIn"])
            ).optional()
        }
    ).named(renames["GoogleFirebaseAppcheckV1BatchGetAppAttestConfigsResponseIn"])
    types["GoogleFirebaseAppcheckV1BatchGetAppAttestConfigsResponseOut"] = t.struct(
        {
            "configs": t.array(
                t.proxy(renames["GoogleFirebaseAppcheckV1AppAttestConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppcheckV1BatchGetAppAttestConfigsResponseOut"])
    types["GoogleFirebaseAppcheckV1AppCheckTokenIn"] = t.struct(
        {"ttl": t.string().optional(), "token": t.string().optional()}
    ).named(renames["GoogleFirebaseAppcheckV1AppCheckTokenIn"])
    types["GoogleFirebaseAppcheckV1AppCheckTokenOut"] = t.struct(
        {
            "ttl": t.string().optional(),
            "token": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppcheckV1AppCheckTokenOut"])
    types["GoogleFirebaseAppcheckV1RecaptchaV3ConfigIn"] = t.struct(
        {
            "tokenTtl": t.string().optional(),
            "name": t.string(),
            "siteSecret": t.string(),
        }
    ).named(renames["GoogleFirebaseAppcheckV1RecaptchaV3ConfigIn"])
    types["GoogleFirebaseAppcheckV1RecaptchaV3ConfigOut"] = t.struct(
        {
            "tokenTtl": t.string().optional(),
            "name": t.string(),
            "siteSecret": t.string(),
            "siteSecretSet": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppcheckV1RecaptchaV3ConfigOut"])
    types["GoogleFirebaseAppcheckV1ExchangeRecaptchaV3TokenRequestIn"] = t.struct(
        {"limitedUse": t.boolean().optional(), "recaptchaV3Token": t.string()}
    ).named(renames["GoogleFirebaseAppcheckV1ExchangeRecaptchaV3TokenRequestIn"])
    types["GoogleFirebaseAppcheckV1ExchangeRecaptchaV3TokenRequestOut"] = t.struct(
        {
            "limitedUse": t.boolean().optional(),
            "recaptchaV3Token": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppcheckV1ExchangeRecaptchaV3TokenRequestOut"])
    types["GoogleFirebaseAppcheckV1BatchGetSafetyNetConfigsResponseIn"] = t.struct(
        {
            "configs": t.array(
                t.proxy(renames["GoogleFirebaseAppcheckV1SafetyNetConfigIn"])
            ).optional()
        }
    ).named(renames["GoogleFirebaseAppcheckV1BatchGetSafetyNetConfigsResponseIn"])
    types["GoogleFirebaseAppcheckV1BatchGetSafetyNetConfigsResponseOut"] = t.struct(
        {
            "configs": t.array(
                t.proxy(renames["GoogleFirebaseAppcheckV1SafetyNetConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppcheckV1BatchGetSafetyNetConfigsResponseOut"])
    types["GoogleFirebaseAppcheckV1BatchGetPlayIntegrityConfigsResponseIn"] = t.struct(
        {
            "configs": t.array(
                t.proxy(renames["GoogleFirebaseAppcheckV1PlayIntegrityConfigIn"])
            ).optional()
        }
    ).named(renames["GoogleFirebaseAppcheckV1BatchGetPlayIntegrityConfigsResponseIn"])
    types["GoogleFirebaseAppcheckV1BatchGetPlayIntegrityConfigsResponseOut"] = t.struct(
        {
            "configs": t.array(
                t.proxy(renames["GoogleFirebaseAppcheckV1PlayIntegrityConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppcheckV1BatchGetPlayIntegrityConfigsResponseOut"])
    types["GoogleFirebaseAppcheckV1PlayIntegrityConfigIn"] = t.struct(
        {"tokenTtl": t.string().optional(), "name": t.string()}
    ).named(renames["GoogleFirebaseAppcheckV1PlayIntegrityConfigIn"])
    types["GoogleFirebaseAppcheckV1PlayIntegrityConfigOut"] = t.struct(
        {
            "tokenTtl": t.string().optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppcheckV1PlayIntegrityConfigOut"])
    types["GoogleFirebaseAppcheckV1BatchUpdateServicesRequestIn"] = t.struct(
        {
            "requests": t.array(
                t.proxy(renames["GoogleFirebaseAppcheckV1UpdateServiceRequestIn"])
            ),
            "updateMask": t.string().optional(),
        }
    ).named(renames["GoogleFirebaseAppcheckV1BatchUpdateServicesRequestIn"])
    types["GoogleFirebaseAppcheckV1BatchUpdateServicesRequestOut"] = t.struct(
        {
            "requests": t.array(
                t.proxy(renames["GoogleFirebaseAppcheckV1UpdateServiceRequestOut"])
            ),
            "updateMask": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppcheckV1BatchUpdateServicesRequestOut"])
    types["GoogleFirebaseAppcheckV1PublicJwkSetIn"] = t.struct(
        {
            "keys": t.array(
                t.proxy(renames["GoogleFirebaseAppcheckV1PublicJwkIn"])
            ).optional()
        }
    ).named(renames["GoogleFirebaseAppcheckV1PublicJwkSetIn"])
    types["GoogleFirebaseAppcheckV1PublicJwkSetOut"] = t.struct(
        {
            "keys": t.array(
                t.proxy(renames["GoogleFirebaseAppcheckV1PublicJwkOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppcheckV1PublicJwkSetOut"])
    types[
        "GoogleFirebaseAppcheckV1BatchGetRecaptchaEnterpriseConfigsResponseIn"
    ] = t.struct(
        {
            "configs": t.array(
                t.proxy(renames["GoogleFirebaseAppcheckV1RecaptchaEnterpriseConfigIn"])
            ).optional()
        }
    ).named(
        renames["GoogleFirebaseAppcheckV1BatchGetRecaptchaEnterpriseConfigsResponseIn"]
    )
    types[
        "GoogleFirebaseAppcheckV1BatchGetRecaptchaEnterpriseConfigsResponseOut"
    ] = t.struct(
        {
            "configs": t.array(
                t.proxy(renames["GoogleFirebaseAppcheckV1RecaptchaEnterpriseConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleFirebaseAppcheckV1BatchGetRecaptchaEnterpriseConfigsResponseOut"]
    )
    types["GoogleFirebaseAppcheckV1AppAttestConfigIn"] = t.struct(
        {"tokenTtl": t.string().optional(), "name": t.string()}
    ).named(renames["GoogleFirebaseAppcheckV1AppAttestConfigIn"])
    types["GoogleFirebaseAppcheckV1AppAttestConfigOut"] = t.struct(
        {
            "tokenTtl": t.string().optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppcheckV1AppAttestConfigOut"])
    types["GoogleFirebaseAppcheckV1DebugTokenIn"] = t.struct(
        {"token": t.string(), "name": t.string(), "displayName": t.string()}
    ).named(renames["GoogleFirebaseAppcheckV1DebugTokenIn"])
    types["GoogleFirebaseAppcheckV1DebugTokenOut"] = t.struct(
        {
            "token": t.string(),
            "name": t.string(),
            "displayName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppcheckV1DebugTokenOut"])
    types["GoogleFirebaseAppcheckV1ListDebugTokensResponseIn"] = t.struct(
        {
            "debugTokens": t.array(
                t.proxy(renames["GoogleFirebaseAppcheckV1DebugTokenIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleFirebaseAppcheckV1ListDebugTokensResponseIn"])
    types["GoogleFirebaseAppcheckV1ListDebugTokensResponseOut"] = t.struct(
        {
            "debugTokens": t.array(
                t.proxy(renames["GoogleFirebaseAppcheckV1DebugTokenOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppcheckV1ListDebugTokensResponseOut"])
    types["GoogleFirebaseAppcheckV1ExchangeDebugTokenRequestIn"] = t.struct(
        {"limitedUse": t.boolean().optional(), "debugToken": t.string()}
    ).named(renames["GoogleFirebaseAppcheckV1ExchangeDebugTokenRequestIn"])
    types["GoogleFirebaseAppcheckV1ExchangeDebugTokenRequestOut"] = t.struct(
        {
            "limitedUse": t.boolean().optional(),
            "debugToken": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppcheckV1ExchangeDebugTokenRequestOut"])
    types["GoogleFirebaseAppcheckV1GeneratePlayIntegrityChallengeRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleFirebaseAppcheckV1GeneratePlayIntegrityChallengeRequestIn"])
    types[
        "GoogleFirebaseAppcheckV1GeneratePlayIntegrityChallengeRequestOut"
    ] = t.struct({"error": t.proxy(renames["ErrorResponse"]).optional()}).named(
        renames["GoogleFirebaseAppcheckV1GeneratePlayIntegrityChallengeRequestOut"]
    )
    types["GoogleFirebaseAppcheckV1BatchGetRecaptchaV3ConfigsResponseIn"] = t.struct(
        {
            "configs": t.array(
                t.proxy(renames["GoogleFirebaseAppcheckV1RecaptchaV3ConfigIn"])
            ).optional()
        }
    ).named(renames["GoogleFirebaseAppcheckV1BatchGetRecaptchaV3ConfigsResponseIn"])
    types["GoogleFirebaseAppcheckV1BatchGetRecaptchaV3ConfigsResponseOut"] = t.struct(
        {
            "configs": t.array(
                t.proxy(renames["GoogleFirebaseAppcheckV1RecaptchaV3ConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppcheckV1BatchGetRecaptchaV3ConfigsResponseOut"])
    types[
        "GoogleFirebaseAppcheckV1GeneratePlayIntegrityChallengeResponseIn"
    ] = t.struct(
        {"challenge": t.string().optional(), "ttl": t.string().optional()}
    ).named(
        renames["GoogleFirebaseAppcheckV1GeneratePlayIntegrityChallengeResponseIn"]
    )
    types[
        "GoogleFirebaseAppcheckV1GeneratePlayIntegrityChallengeResponseOut"
    ] = t.struct(
        {
            "challenge": t.string().optional(),
            "ttl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleFirebaseAppcheckV1GeneratePlayIntegrityChallengeResponseOut"]
    )
    types["GoogleFirebaseAppcheckV1ExchangePlayIntegrityTokenRequestIn"] = t.struct(
        {"playIntegrityToken": t.string(), "limitedUse": t.boolean().optional()}
    ).named(renames["GoogleFirebaseAppcheckV1ExchangePlayIntegrityTokenRequestIn"])
    types["GoogleFirebaseAppcheckV1ExchangePlayIntegrityTokenRequestOut"] = t.struct(
        {
            "playIntegrityToken": t.string(),
            "limitedUse": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppcheckV1ExchangePlayIntegrityTokenRequestOut"])
    types["GoogleFirebaseAppcheckV1UpdateServiceRequestIn"] = t.struct(
        {
            "updateMask": t.string(),
            "service": t.proxy(renames["GoogleFirebaseAppcheckV1ServiceIn"]),
        }
    ).named(renames["GoogleFirebaseAppcheckV1UpdateServiceRequestIn"])
    types["GoogleFirebaseAppcheckV1UpdateServiceRequestOut"] = t.struct(
        {
            "updateMask": t.string(),
            "service": t.proxy(renames["GoogleFirebaseAppcheckV1ServiceOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppcheckV1UpdateServiceRequestOut"])
    types["GoogleFirebaseAppcheckV1ExchangeCustomTokenRequestIn"] = t.struct(
        {"limitedUse": t.boolean().optional(), "customToken": t.string()}
    ).named(renames["GoogleFirebaseAppcheckV1ExchangeCustomTokenRequestIn"])
    types["GoogleFirebaseAppcheckV1ExchangeCustomTokenRequestOut"] = t.struct(
        {
            "limitedUse": t.boolean().optional(),
            "customToken": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppcheckV1ExchangeCustomTokenRequestOut"])
    types["GoogleFirebaseAppcheckV1ExchangeAppAttestAttestationResponseIn"] = t.struct(
        {
            "artifact": t.string().optional(),
            "appCheckToken": t.proxy(
                renames["GoogleFirebaseAppcheckV1AppCheckTokenIn"]
            ).optional(),
        }
    ).named(renames["GoogleFirebaseAppcheckV1ExchangeAppAttestAttestationResponseIn"])
    types["GoogleFirebaseAppcheckV1ExchangeAppAttestAttestationResponseOut"] = t.struct(
        {
            "artifact": t.string().optional(),
            "appCheckToken": t.proxy(
                renames["GoogleFirebaseAppcheckV1AppCheckTokenOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppcheckV1ExchangeAppAttestAttestationResponseOut"])
    types["GoogleFirebaseAppcheckV1DeviceCheckConfigIn"] = t.struct(
        {
            "privateKey": t.string(),
            "tokenTtl": t.string().optional(),
            "keyId": t.string(),
            "name": t.string(),
        }
    ).named(renames["GoogleFirebaseAppcheckV1DeviceCheckConfigIn"])
    types["GoogleFirebaseAppcheckV1DeviceCheckConfigOut"] = t.struct(
        {
            "privateKeySet": t.boolean().optional(),
            "privateKey": t.string(),
            "tokenTtl": t.string().optional(),
            "keyId": t.string(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppcheckV1DeviceCheckConfigOut"])
    types["GoogleFirebaseAppcheckV1ExchangeDeviceCheckTokenRequestIn"] = t.struct(
        {"deviceToken": t.string(), "limitedUse": t.boolean().optional()}
    ).named(renames["GoogleFirebaseAppcheckV1ExchangeDeviceCheckTokenRequestIn"])
    types["GoogleFirebaseAppcheckV1ExchangeDeviceCheckTokenRequestOut"] = t.struct(
        {
            "deviceToken": t.string(),
            "limitedUse": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppcheckV1ExchangeDeviceCheckTokenRequestOut"])
    types["GoogleFirebaseAppcheckV1ExchangeAppAttestAttestationRequestIn"] = t.struct(
        {
            "keyId": t.string(),
            "challenge": t.string(),
            "limitedUse": t.boolean().optional(),
            "attestationStatement": t.string(),
        }
    ).named(renames["GoogleFirebaseAppcheckV1ExchangeAppAttestAttestationRequestIn"])
    types["GoogleFirebaseAppcheckV1ExchangeAppAttestAttestationRequestOut"] = t.struct(
        {
            "keyId": t.string(),
            "challenge": t.string(),
            "limitedUse": t.boolean().optional(),
            "attestationStatement": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppcheckV1ExchangeAppAttestAttestationRequestOut"])
    types["GoogleFirebaseAppcheckV1RecaptchaEnterpriseConfigIn"] = t.struct(
        {
            "siteKey": t.string().optional(),
            "name": t.string(),
            "tokenTtl": t.string().optional(),
        }
    ).named(renames["GoogleFirebaseAppcheckV1RecaptchaEnterpriseConfigIn"])
    types["GoogleFirebaseAppcheckV1RecaptchaEnterpriseConfigOut"] = t.struct(
        {
            "siteKey": t.string().optional(),
            "name": t.string(),
            "tokenTtl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppcheckV1RecaptchaEnterpriseConfigOut"])
    types["GoogleFirebaseAppcheckV1SafetyNetConfigIn"] = t.struct(
        {"tokenTtl": t.string().optional(), "name": t.string()}
    ).named(renames["GoogleFirebaseAppcheckV1SafetyNetConfigIn"])
    types["GoogleFirebaseAppcheckV1SafetyNetConfigOut"] = t.struct(
        {
            "tokenTtl": t.string().optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppcheckV1SafetyNetConfigOut"])

    functions = {}
    functions["jwksGet"] = firebaseappcheck.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleFirebaseAppcheckV1PublicJwkSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsExchangeRecaptchaEnterpriseToken"] = firebaseappcheck.post(
        "v1/{app}:exchangeDebugToken",
        t.struct(
            {
                "app": t.string(),
                "limitedUse": t.boolean().optional(),
                "debugToken": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirebaseAppcheckV1AppCheckTokenOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsExchangeSafetyNetToken"] = firebaseappcheck.post(
        "v1/{app}:exchangeDebugToken",
        t.struct(
            {
                "app": t.string(),
                "limitedUse": t.boolean().optional(),
                "debugToken": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirebaseAppcheckV1AppCheckTokenOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsExchangeCustomToken"] = firebaseappcheck.post(
        "v1/{app}:exchangeDebugToken",
        t.struct(
            {
                "app": t.string(),
                "limitedUse": t.boolean().optional(),
                "debugToken": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirebaseAppcheckV1AppCheckTokenOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsExchangeAppAttestAttestation"] = firebaseappcheck.post(
        "v1/{app}:exchangeDebugToken",
        t.struct(
            {
                "app": t.string(),
                "limitedUse": t.boolean().optional(),
                "debugToken": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirebaseAppcheckV1AppCheckTokenOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsGeneratePlayIntegrityChallenge"] = firebaseappcheck.post(
        "v1/{app}:exchangeDebugToken",
        t.struct(
            {
                "app": t.string(),
                "limitedUse": t.boolean().optional(),
                "debugToken": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirebaseAppcheckV1AppCheckTokenOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsExchangeRecaptchaV3Token"] = firebaseappcheck.post(
        "v1/{app}:exchangeDebugToken",
        t.struct(
            {
                "app": t.string(),
                "limitedUse": t.boolean().optional(),
                "debugToken": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirebaseAppcheckV1AppCheckTokenOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsExchangeDeviceCheckToken"] = firebaseappcheck.post(
        "v1/{app}:exchangeDebugToken",
        t.struct(
            {
                "app": t.string(),
                "limitedUse": t.boolean().optional(),
                "debugToken": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirebaseAppcheckV1AppCheckTokenOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsExchangePlayIntegrityToken"] = firebaseappcheck.post(
        "v1/{app}:exchangeDebugToken",
        t.struct(
            {
                "app": t.string(),
                "limitedUse": t.boolean().optional(),
                "debugToken": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirebaseAppcheckV1AppCheckTokenOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsExchangeAppAttestAssertion"] = firebaseappcheck.post(
        "v1/{app}:exchangeDebugToken",
        t.struct(
            {
                "app": t.string(),
                "limitedUse": t.boolean().optional(),
                "debugToken": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirebaseAppcheckV1AppCheckTokenOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsGenerateAppAttestChallenge"] = firebaseappcheck.post(
        "v1/{app}:exchangeDebugToken",
        t.struct(
            {
                "app": t.string(),
                "limitedUse": t.boolean().optional(),
                "debugToken": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirebaseAppcheckV1AppCheckTokenOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsExchangeDebugToken"] = firebaseappcheck.post(
        "v1/{app}:exchangeDebugToken",
        t.struct(
            {
                "app": t.string(),
                "limitedUse": t.boolean().optional(),
                "debugToken": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirebaseAppcheckV1AppCheckTokenOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsRecaptchaV3ConfigBatchGet"] = firebaseappcheck.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleFirebaseAppcheckV1RecaptchaV3ConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsRecaptchaV3ConfigPatch"] = firebaseappcheck.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleFirebaseAppcheckV1RecaptchaV3ConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsRecaptchaV3ConfigGet"] = firebaseappcheck.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleFirebaseAppcheckV1RecaptchaV3ConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsAppAttestConfigGet"] = firebaseappcheck.get(
        "v1/{parent}/apps/-/appAttestConfig:batchGet",
        t.struct(
            {"names": t.string(), "parent": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["GoogleFirebaseAppcheckV1BatchGetAppAttestConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsAppAttestConfigPatch"] = firebaseappcheck.get(
        "v1/{parent}/apps/-/appAttestConfig:batchGet",
        t.struct(
            {"names": t.string(), "parent": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["GoogleFirebaseAppcheckV1BatchGetAppAttestConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsAppAttestConfigBatchGet"] = firebaseappcheck.get(
        "v1/{parent}/apps/-/appAttestConfig:batchGet",
        t.struct(
            {"names": t.string(), "parent": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["GoogleFirebaseAppcheckV1BatchGetAppAttestConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsDeviceCheckConfigBatchGet"] = firebaseappcheck.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleFirebaseAppcheckV1DeviceCheckConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsDeviceCheckConfigPatch"] = firebaseappcheck.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleFirebaseAppcheckV1DeviceCheckConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsDeviceCheckConfigGet"] = firebaseappcheck.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleFirebaseAppcheckV1DeviceCheckConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsPlayIntegrityConfigGet"] = firebaseappcheck.get(
        "v1/{parent}/apps/-/playIntegrityConfig:batchGet",
        t.struct(
            {"names": t.string(), "parent": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(
            renames["GoogleFirebaseAppcheckV1BatchGetPlayIntegrityConfigsResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsPlayIntegrityConfigPatch"] = firebaseappcheck.get(
        "v1/{parent}/apps/-/playIntegrityConfig:batchGet",
        t.struct(
            {"names": t.string(), "parent": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(
            renames["GoogleFirebaseAppcheckV1BatchGetPlayIntegrityConfigsResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsPlayIntegrityConfigBatchGet"] = firebaseappcheck.get(
        "v1/{parent}/apps/-/playIntegrityConfig:batchGet",
        t.struct(
            {"names": t.string(), "parent": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(
            renames["GoogleFirebaseAppcheckV1BatchGetPlayIntegrityConfigsResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsRecaptchaEnterpriseConfigPatch"] = firebaseappcheck.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleFirebaseAppcheckV1RecaptchaEnterpriseConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsRecaptchaEnterpriseConfigBatchGet"] = firebaseappcheck.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleFirebaseAppcheckV1RecaptchaEnterpriseConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsRecaptchaEnterpriseConfigGet"] = firebaseappcheck.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleFirebaseAppcheckV1RecaptchaEnterpriseConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsDebugTokensDelete"] = firebaseappcheck.post(
        "v1/{parent}/debugTokens",
        t.struct(
            {
                "parent": t.string(),
                "token": t.string(),
                "name": t.string(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirebaseAppcheckV1DebugTokenOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsDebugTokensList"] = firebaseappcheck.post(
        "v1/{parent}/debugTokens",
        t.struct(
            {
                "parent": t.string(),
                "token": t.string(),
                "name": t.string(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirebaseAppcheckV1DebugTokenOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsDebugTokensPatch"] = firebaseappcheck.post(
        "v1/{parent}/debugTokens",
        t.struct(
            {
                "parent": t.string(),
                "token": t.string(),
                "name": t.string(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirebaseAppcheckV1DebugTokenOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsDebugTokensGet"] = firebaseappcheck.post(
        "v1/{parent}/debugTokens",
        t.struct(
            {
                "parent": t.string(),
                "token": t.string(),
                "name": t.string(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirebaseAppcheckV1DebugTokenOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsDebugTokensCreate"] = firebaseappcheck.post(
        "v1/{parent}/debugTokens",
        t.struct(
            {
                "parent": t.string(),
                "token": t.string(),
                "name": t.string(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirebaseAppcheckV1DebugTokenOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsSafetyNetConfigPatch"] = firebaseappcheck.get(
        "v1/{parent}/apps/-/safetyNetConfig:batchGet",
        t.struct(
            {"parent": t.string(), "names": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["GoogleFirebaseAppcheckV1BatchGetSafetyNetConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsSafetyNetConfigGet"] = firebaseappcheck.get(
        "v1/{parent}/apps/-/safetyNetConfig:batchGet",
        t.struct(
            {"parent": t.string(), "names": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["GoogleFirebaseAppcheckV1BatchGetSafetyNetConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsSafetyNetConfigBatchGet"] = firebaseappcheck.get(
        "v1/{parent}/apps/-/safetyNetConfig:batchGet",
        t.struct(
            {"parent": t.string(), "names": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["GoogleFirebaseAppcheckV1BatchGetSafetyNetConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsServicesList"] = firebaseappcheck.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleFirebaseAppcheckV1ServiceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsServicesPatch"] = firebaseappcheck.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleFirebaseAppcheckV1ServiceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsServicesBatchUpdate"] = firebaseappcheck.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleFirebaseAppcheckV1ServiceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsServicesGet"] = firebaseappcheck.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleFirebaseAppcheckV1ServiceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="firebaseappcheck",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
