from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_mybusinessverifications() -> Import:
    mybusinessverifications = HTTPRuntime(
        "https://mybusinessverifications.googleapis.com/"
    )

    renames = {
        "ErrorResponse": "_mybusinessverifications_1_ErrorResponse",
        "ListVerificationsResponseIn": "_mybusinessverifications_2_ListVerificationsResponseIn",
        "ListVerificationsResponseOut": "_mybusinessverifications_3_ListVerificationsResponseOut",
        "FetchVerificationOptionsRequestIn": "_mybusinessverifications_4_FetchVerificationOptionsRequestIn",
        "FetchVerificationOptionsRequestOut": "_mybusinessverifications_5_FetchVerificationOptionsRequestOut",
        "WaitForVoiceOfMerchantIn": "_mybusinessverifications_6_WaitForVoiceOfMerchantIn",
        "WaitForVoiceOfMerchantOut": "_mybusinessverifications_7_WaitForVoiceOfMerchantOut",
        "GenerateVerificationTokenResponseIn": "_mybusinessverifications_8_GenerateVerificationTokenResponseIn",
        "GenerateVerificationTokenResponseOut": "_mybusinessverifications_9_GenerateVerificationTokenResponseOut",
        "VerifyIn": "_mybusinessverifications_10_VerifyIn",
        "VerifyOut": "_mybusinessverifications_11_VerifyOut",
        "PostalAddressIn": "_mybusinessverifications_12_PostalAddressIn",
        "PostalAddressOut": "_mybusinessverifications_13_PostalAddressOut",
        "ServiceBusinessContextIn": "_mybusinessverifications_14_ServiceBusinessContextIn",
        "ServiceBusinessContextOut": "_mybusinessverifications_15_ServiceBusinessContextOut",
        "VoiceOfMerchantStateIn": "_mybusinessverifications_16_VoiceOfMerchantStateIn",
        "VoiceOfMerchantStateOut": "_mybusinessverifications_17_VoiceOfMerchantStateOut",
        "VerifyLocationResponseIn": "_mybusinessverifications_18_VerifyLocationResponseIn",
        "VerifyLocationResponseOut": "_mybusinessverifications_19_VerifyLocationResponseOut",
        "CompleteVerificationRequestIn": "_mybusinessverifications_20_CompleteVerificationRequestIn",
        "CompleteVerificationRequestOut": "_mybusinessverifications_21_CompleteVerificationRequestOut",
        "ResolveOwnershipConflictIn": "_mybusinessverifications_22_ResolveOwnershipConflictIn",
        "ResolveOwnershipConflictOut": "_mybusinessverifications_23_ResolveOwnershipConflictOut",
        "VerificationOptionIn": "_mybusinessverifications_24_VerificationOptionIn",
        "VerificationOptionOut": "_mybusinessverifications_25_VerificationOptionOut",
        "AddressVerificationDataIn": "_mybusinessverifications_26_AddressVerificationDataIn",
        "AddressVerificationDataOut": "_mybusinessverifications_27_AddressVerificationDataOut",
        "ComplyWithGuidelinesIn": "_mybusinessverifications_28_ComplyWithGuidelinesIn",
        "ComplyWithGuidelinesOut": "_mybusinessverifications_29_ComplyWithGuidelinesOut",
        "CompleteVerificationResponseIn": "_mybusinessverifications_30_CompleteVerificationResponseIn",
        "CompleteVerificationResponseOut": "_mybusinessverifications_31_CompleteVerificationResponseOut",
        "VerifyLocationRequestIn": "_mybusinessverifications_32_VerifyLocationRequestIn",
        "VerifyLocationRequestOut": "_mybusinessverifications_33_VerifyLocationRequestOut",
        "LocationIn": "_mybusinessverifications_34_LocationIn",
        "LocationOut": "_mybusinessverifications_35_LocationOut",
        "VerificationTokenIn": "_mybusinessverifications_36_VerificationTokenIn",
        "VerificationTokenOut": "_mybusinessverifications_37_VerificationTokenOut",
        "GenerateVerificationTokenRequestIn": "_mybusinessverifications_38_GenerateVerificationTokenRequestIn",
        "GenerateVerificationTokenRequestOut": "_mybusinessverifications_39_GenerateVerificationTokenRequestOut",
        "VerificationIn": "_mybusinessverifications_40_VerificationIn",
        "VerificationOut": "_mybusinessverifications_41_VerificationOut",
        "FetchVerificationOptionsResponseIn": "_mybusinessverifications_42_FetchVerificationOptionsResponseIn",
        "FetchVerificationOptionsResponseOut": "_mybusinessverifications_43_FetchVerificationOptionsResponseOut",
        "EmailVerificationDataIn": "_mybusinessverifications_44_EmailVerificationDataIn",
        "EmailVerificationDataOut": "_mybusinessverifications_45_EmailVerificationDataOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ListVerificationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "verifications": t.array(t.proxy(renames["VerificationIn"])).optional(),
        }
    ).named(renames["ListVerificationsResponseIn"])
    types["ListVerificationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "verifications": t.array(t.proxy(renames["VerificationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListVerificationsResponseOut"])
    types["FetchVerificationOptionsRequestIn"] = t.struct(
        {
            "languageCode": t.string(),
            "context": t.proxy(renames["ServiceBusinessContextIn"]).optional(),
        }
    ).named(renames["FetchVerificationOptionsRequestIn"])
    types["FetchVerificationOptionsRequestOut"] = t.struct(
        {
            "languageCode": t.string(),
            "context": t.proxy(renames["ServiceBusinessContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FetchVerificationOptionsRequestOut"])
    types["WaitForVoiceOfMerchantIn"] = t.struct({"_": t.string().optional()}).named(
        renames["WaitForVoiceOfMerchantIn"]
    )
    types["WaitForVoiceOfMerchantOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["WaitForVoiceOfMerchantOut"])
    types["GenerateVerificationTokenResponseIn"] = t.struct(
        {"token": t.proxy(renames["VerificationTokenIn"]).optional()}
    ).named(renames["GenerateVerificationTokenResponseIn"])
    types["GenerateVerificationTokenResponseOut"] = t.struct(
        {
            "token": t.proxy(renames["VerificationTokenOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateVerificationTokenResponseOut"])
    types["VerifyIn"] = t.struct(
        {"hasPendingVerification": t.boolean().optional()}
    ).named(renames["VerifyIn"])
    types["VerifyOut"] = t.struct(
        {
            "hasPendingVerification": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VerifyOut"])
    types["PostalAddressIn"] = t.struct(
        {
            "sortingCode": t.string().optional(),
            "revision": t.integer().optional(),
            "locality": t.string().optional(),
            "recipients": t.array(t.string()).optional(),
            "organization": t.string().optional(),
            "regionCode": t.string(),
            "postalCode": t.string().optional(),
            "sublocality": t.string().optional(),
            "administrativeArea": t.string().optional(),
            "addressLines": t.array(t.string()).optional(),
            "languageCode": t.string().optional(),
        }
    ).named(renames["PostalAddressIn"])
    types["PostalAddressOut"] = t.struct(
        {
            "sortingCode": t.string().optional(),
            "revision": t.integer().optional(),
            "locality": t.string().optional(),
            "recipients": t.array(t.string()).optional(),
            "organization": t.string().optional(),
            "regionCode": t.string(),
            "postalCode": t.string().optional(),
            "sublocality": t.string().optional(),
            "administrativeArea": t.string().optional(),
            "addressLines": t.array(t.string()).optional(),
            "languageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostalAddressOut"])
    types["ServiceBusinessContextIn"] = t.struct(
        {"address": t.proxy(renames["PostalAddressIn"]).optional()}
    ).named(renames["ServiceBusinessContextIn"])
    types["ServiceBusinessContextOut"] = t.struct(
        {
            "address": t.proxy(renames["PostalAddressOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceBusinessContextOut"])
    types["VoiceOfMerchantStateIn"] = t.struct(
        {
            "complyWithGuidelines": t.proxy(
                renames["ComplyWithGuidelinesIn"]
            ).optional(),
            "resolveOwnershipConflict": t.proxy(
                renames["ResolveOwnershipConflictIn"]
            ).optional(),
            "verify": t.proxy(renames["VerifyIn"]).optional(),
            "hasVoiceOfMerchant": t.boolean().optional(),
            "waitForVoiceOfMerchant": t.proxy(
                renames["WaitForVoiceOfMerchantIn"]
            ).optional(),
            "hasBusinessAuthority": t.boolean().optional(),
        }
    ).named(renames["VoiceOfMerchantStateIn"])
    types["VoiceOfMerchantStateOut"] = t.struct(
        {
            "complyWithGuidelines": t.proxy(
                renames["ComplyWithGuidelinesOut"]
            ).optional(),
            "resolveOwnershipConflict": t.proxy(
                renames["ResolveOwnershipConflictOut"]
            ).optional(),
            "verify": t.proxy(renames["VerifyOut"]).optional(),
            "hasVoiceOfMerchant": t.boolean().optional(),
            "waitForVoiceOfMerchant": t.proxy(
                renames["WaitForVoiceOfMerchantOut"]
            ).optional(),
            "hasBusinessAuthority": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VoiceOfMerchantStateOut"])
    types["VerifyLocationResponseIn"] = t.struct(
        {"verification": t.proxy(renames["VerificationIn"]).optional()}
    ).named(renames["VerifyLocationResponseIn"])
    types["VerifyLocationResponseOut"] = t.struct(
        {
            "verification": t.proxy(renames["VerificationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VerifyLocationResponseOut"])
    types["CompleteVerificationRequestIn"] = t.struct({"pin": t.string()}).named(
        renames["CompleteVerificationRequestIn"]
    )
    types["CompleteVerificationRequestOut"] = t.struct(
        {"pin": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CompleteVerificationRequestOut"])
    types["ResolveOwnershipConflictIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ResolveOwnershipConflictIn"]
    )
    types["ResolveOwnershipConflictOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ResolveOwnershipConflictOut"])
    types["VerificationOptionIn"] = t.struct(
        {
            "addressData": t.proxy(renames["AddressVerificationDataIn"]).optional(),
            "verificationMethod": t.string().optional(),
            "emailData": t.proxy(renames["EmailVerificationDataIn"]).optional(),
            "phoneNumber": t.string().optional(),
            "announcement": t.string().optional(),
        }
    ).named(renames["VerificationOptionIn"])
    types["VerificationOptionOut"] = t.struct(
        {
            "addressData": t.proxy(renames["AddressVerificationDataOut"]).optional(),
            "verificationMethod": t.string().optional(),
            "emailData": t.proxy(renames["EmailVerificationDataOut"]).optional(),
            "phoneNumber": t.string().optional(),
            "announcement": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VerificationOptionOut"])
    types["AddressVerificationDataIn"] = t.struct(
        {
            "business": t.string().optional(),
            "address": t.proxy(renames["PostalAddressIn"]).optional(),
            "expectedDeliveryDaysRegion": t.integer().optional(),
        }
    ).named(renames["AddressVerificationDataIn"])
    types["AddressVerificationDataOut"] = t.struct(
        {
            "business": t.string().optional(),
            "address": t.proxy(renames["PostalAddressOut"]).optional(),
            "expectedDeliveryDaysRegion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddressVerificationDataOut"])
    types["ComplyWithGuidelinesIn"] = t.struct(
        {"recommendationReason": t.string().optional()}
    ).named(renames["ComplyWithGuidelinesIn"])
    types["ComplyWithGuidelinesOut"] = t.struct(
        {
            "recommendationReason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComplyWithGuidelinesOut"])
    types["CompleteVerificationResponseIn"] = t.struct(
        {"verification": t.proxy(renames["VerificationIn"]).optional()}
    ).named(renames["CompleteVerificationResponseIn"])
    types["CompleteVerificationResponseOut"] = t.struct(
        {
            "verification": t.proxy(renames["VerificationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CompleteVerificationResponseOut"])
    types["VerifyLocationRequestIn"] = t.struct(
        {
            "mailerContact": t.string().optional(),
            "languageCode": t.string().optional(),
            "context": t.proxy(renames["ServiceBusinessContextIn"]).optional(),
            "emailAddress": t.string().optional(),
            "token": t.proxy(renames["VerificationTokenIn"]).optional(),
            "phoneNumber": t.string().optional(),
            "method": t.string(),
        }
    ).named(renames["VerifyLocationRequestIn"])
    types["VerifyLocationRequestOut"] = t.struct(
        {
            "mailerContact": t.string().optional(),
            "languageCode": t.string().optional(),
            "context": t.proxy(renames["ServiceBusinessContextOut"]).optional(),
            "emailAddress": t.string().optional(),
            "token": t.proxy(renames["VerificationTokenOut"]).optional(),
            "phoneNumber": t.string().optional(),
            "method": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VerifyLocationRequestOut"])
    types["LocationIn"] = t.struct(
        {
            "primaryPhone": t.string().optional(),
            "name": t.string(),
            "address": t.proxy(renames["PostalAddressIn"]),
            "primaryCategoryId": t.string(),
            "websiteUri": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "primaryPhone": t.string().optional(),
            "name": t.string(),
            "address": t.proxy(renames["PostalAddressOut"]),
            "primaryCategoryId": t.string(),
            "websiteUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["VerificationTokenIn"] = t.struct(
        {"tokenString": t.string().optional()}
    ).named(renames["VerificationTokenIn"])
    types["VerificationTokenOut"] = t.struct(
        {
            "tokenString": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VerificationTokenOut"])
    types["GenerateVerificationTokenRequestIn"] = t.struct(
        {"location": t.proxy(renames["LocationIn"])}
    ).named(renames["GenerateVerificationTokenRequestIn"])
    types["GenerateVerificationTokenRequestOut"] = t.struct(
        {
            "location": t.proxy(renames["LocationOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateVerificationTokenRequestOut"])
    types["VerificationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "method": t.string().optional(),
            "state": t.string().optional(),
            "announcement": t.string().optional(),
        }
    ).named(renames["VerificationIn"])
    types["VerificationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "method": t.string().optional(),
            "state": t.string().optional(),
            "announcement": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VerificationOut"])
    types["FetchVerificationOptionsResponseIn"] = t.struct(
        {"options": t.array(t.proxy(renames["VerificationOptionIn"])).optional()}
    ).named(renames["FetchVerificationOptionsResponseIn"])
    types["FetchVerificationOptionsResponseOut"] = t.struct(
        {
            "options": t.array(t.proxy(renames["VerificationOptionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FetchVerificationOptionsResponseOut"])
    types["EmailVerificationDataIn"] = t.struct(
        {
            "isUserNameEditable": t.boolean().optional(),
            "domain": t.string().optional(),
            "user": t.string().optional(),
        }
    ).named(renames["EmailVerificationDataIn"])
    types["EmailVerificationDataOut"] = t.struct(
        {
            "isUserNameEditable": t.boolean().optional(),
            "domain": t.string().optional(),
            "user": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EmailVerificationDataOut"])

    functions = {}
    functions["locationsVerify"] = mybusinessverifications.get(
        "v1/{name}/VoiceOfMerchantState",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["VoiceOfMerchantStateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsFetchVerificationOptions"] = mybusinessverifications.get(
        "v1/{name}/VoiceOfMerchantState",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["VoiceOfMerchantStateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsGetVoiceOfMerchantState"] = mybusinessverifications.get(
        "v1/{name}/VoiceOfMerchantState",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["VoiceOfMerchantStateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsVerificationsComplete"] = mybusinessverifications.get(
        "v1/{parent}/verifications",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListVerificationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsVerificationsList"] = mybusinessverifications.get(
        "v1/{parent}/verifications",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListVerificationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["verificationTokensGenerate"] = mybusinessverifications.post(
        "v1/verificationTokens:generate",
        t.struct(
            {"location": t.proxy(renames["LocationIn"]), "auth": t.string().optional()}
        ),
        t.proxy(renames["GenerateVerificationTokenResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="mybusinessverifications",
        renames=renames,
        types=types,
        functions=functions,
    )
