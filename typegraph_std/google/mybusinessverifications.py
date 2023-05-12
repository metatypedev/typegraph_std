from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_mybusinessverifications() -> Import:
    mybusinessverifications = HTTPRuntime(
        "https://mybusinessverifications.googleapis.com/"
    )

    renames = {
        "ErrorResponse": "_mybusinessverifications_1_ErrorResponse",
        "WaitForVoiceOfMerchantIn": "_mybusinessverifications_2_WaitForVoiceOfMerchantIn",
        "WaitForVoiceOfMerchantOut": "_mybusinessverifications_3_WaitForVoiceOfMerchantOut",
        "LocationIn": "_mybusinessverifications_4_LocationIn",
        "LocationOut": "_mybusinessverifications_5_LocationOut",
        "VerifyIn": "_mybusinessverifications_6_VerifyIn",
        "VerifyOut": "_mybusinessverifications_7_VerifyOut",
        "PostalAddressIn": "_mybusinessverifications_8_PostalAddressIn",
        "PostalAddressOut": "_mybusinessverifications_9_PostalAddressOut",
        "ListVerificationsResponseIn": "_mybusinessverifications_10_ListVerificationsResponseIn",
        "ListVerificationsResponseOut": "_mybusinessverifications_11_ListVerificationsResponseOut",
        "FetchVerificationOptionsRequestIn": "_mybusinessverifications_12_FetchVerificationOptionsRequestIn",
        "FetchVerificationOptionsRequestOut": "_mybusinessverifications_13_FetchVerificationOptionsRequestOut",
        "ServiceBusinessContextIn": "_mybusinessverifications_14_ServiceBusinessContextIn",
        "ServiceBusinessContextOut": "_mybusinessverifications_15_ServiceBusinessContextOut",
        "ResolveOwnershipConflictIn": "_mybusinessverifications_16_ResolveOwnershipConflictIn",
        "ResolveOwnershipConflictOut": "_mybusinessverifications_17_ResolveOwnershipConflictOut",
        "CompleteVerificationRequestIn": "_mybusinessverifications_18_CompleteVerificationRequestIn",
        "CompleteVerificationRequestOut": "_mybusinessverifications_19_CompleteVerificationRequestOut",
        "AddressVerificationDataIn": "_mybusinessverifications_20_AddressVerificationDataIn",
        "AddressVerificationDataOut": "_mybusinessverifications_21_AddressVerificationDataOut",
        "VerificationTokenIn": "_mybusinessverifications_22_VerificationTokenIn",
        "VerificationTokenOut": "_mybusinessverifications_23_VerificationTokenOut",
        "FetchVerificationOptionsResponseIn": "_mybusinessverifications_24_FetchVerificationOptionsResponseIn",
        "FetchVerificationOptionsResponseOut": "_mybusinessverifications_25_FetchVerificationOptionsResponseOut",
        "CompleteVerificationResponseIn": "_mybusinessverifications_26_CompleteVerificationResponseIn",
        "CompleteVerificationResponseOut": "_mybusinessverifications_27_CompleteVerificationResponseOut",
        "GenerateVerificationTokenRequestIn": "_mybusinessverifications_28_GenerateVerificationTokenRequestIn",
        "GenerateVerificationTokenRequestOut": "_mybusinessverifications_29_GenerateVerificationTokenRequestOut",
        "VerifyLocationResponseIn": "_mybusinessverifications_30_VerifyLocationResponseIn",
        "VerifyLocationResponseOut": "_mybusinessverifications_31_VerifyLocationResponseOut",
        "VerificationOptionIn": "_mybusinessverifications_32_VerificationOptionIn",
        "VerificationOptionOut": "_mybusinessverifications_33_VerificationOptionOut",
        "VerifyLocationRequestIn": "_mybusinessverifications_34_VerifyLocationRequestIn",
        "VerifyLocationRequestOut": "_mybusinessverifications_35_VerifyLocationRequestOut",
        "EmailVerificationDataIn": "_mybusinessverifications_36_EmailVerificationDataIn",
        "EmailVerificationDataOut": "_mybusinessverifications_37_EmailVerificationDataOut",
        "VoiceOfMerchantStateIn": "_mybusinessverifications_38_VoiceOfMerchantStateIn",
        "VoiceOfMerchantStateOut": "_mybusinessverifications_39_VoiceOfMerchantStateOut",
        "ComplyWithGuidelinesIn": "_mybusinessverifications_40_ComplyWithGuidelinesIn",
        "ComplyWithGuidelinesOut": "_mybusinessverifications_41_ComplyWithGuidelinesOut",
        "VerificationIn": "_mybusinessverifications_42_VerificationIn",
        "VerificationOut": "_mybusinessverifications_43_VerificationOut",
        "GenerateVerificationTokenResponseIn": "_mybusinessverifications_44_GenerateVerificationTokenResponseIn",
        "GenerateVerificationTokenResponseOut": "_mybusinessverifications_45_GenerateVerificationTokenResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["WaitForVoiceOfMerchantIn"] = t.struct({"_": t.string().optional()}).named(
        renames["WaitForVoiceOfMerchantIn"]
    )
    types["WaitForVoiceOfMerchantOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["WaitForVoiceOfMerchantOut"])
    types["LocationIn"] = t.struct(
        {
            "address": t.proxy(renames["PostalAddressIn"]),
            "websiteUri": t.string().optional(),
            "primaryCategoryId": t.string(),
            "name": t.string(),
            "primaryPhone": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "address": t.proxy(renames["PostalAddressOut"]),
            "websiteUri": t.string().optional(),
            "primaryCategoryId": t.string(),
            "name": t.string(),
            "primaryPhone": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
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
            "postalCode": t.string().optional(),
            "locality": t.string().optional(),
            "regionCode": t.string(),
            "languageCode": t.string().optional(),
            "sortingCode": t.string().optional(),
            "revision": t.integer().optional(),
            "sublocality": t.string().optional(),
            "addressLines": t.array(t.string()).optional(),
            "organization": t.string().optional(),
            "administrativeArea": t.string().optional(),
            "recipients": t.array(t.string()).optional(),
        }
    ).named(renames["PostalAddressIn"])
    types["PostalAddressOut"] = t.struct(
        {
            "postalCode": t.string().optional(),
            "locality": t.string().optional(),
            "regionCode": t.string(),
            "languageCode": t.string().optional(),
            "sortingCode": t.string().optional(),
            "revision": t.integer().optional(),
            "sublocality": t.string().optional(),
            "addressLines": t.array(t.string()).optional(),
            "organization": t.string().optional(),
            "administrativeArea": t.string().optional(),
            "recipients": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostalAddressOut"])
    types["ListVerificationsResponseIn"] = t.struct(
        {
            "verifications": t.array(t.proxy(renames["VerificationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListVerificationsResponseIn"])
    types["ListVerificationsResponseOut"] = t.struct(
        {
            "verifications": t.array(t.proxy(renames["VerificationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListVerificationsResponseOut"])
    types["FetchVerificationOptionsRequestIn"] = t.struct(
        {
            "context": t.proxy(renames["ServiceBusinessContextIn"]).optional(),
            "languageCode": t.string(),
        }
    ).named(renames["FetchVerificationOptionsRequestIn"])
    types["FetchVerificationOptionsRequestOut"] = t.struct(
        {
            "context": t.proxy(renames["ServiceBusinessContextOut"]).optional(),
            "languageCode": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FetchVerificationOptionsRequestOut"])
    types["ServiceBusinessContextIn"] = t.struct(
        {"address": t.proxy(renames["PostalAddressIn"]).optional()}
    ).named(renames["ServiceBusinessContextIn"])
    types["ServiceBusinessContextOut"] = t.struct(
        {
            "address": t.proxy(renames["PostalAddressOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceBusinessContextOut"])
    types["ResolveOwnershipConflictIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ResolveOwnershipConflictIn"]
    )
    types["ResolveOwnershipConflictOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ResolveOwnershipConflictOut"])
    types["CompleteVerificationRequestIn"] = t.struct({"pin": t.string()}).named(
        renames["CompleteVerificationRequestIn"]
    )
    types["CompleteVerificationRequestOut"] = t.struct(
        {"pin": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CompleteVerificationRequestOut"])
    types["AddressVerificationDataIn"] = t.struct(
        {
            "business": t.string().optional(),
            "expectedDeliveryDaysRegion": t.integer().optional(),
            "address": t.proxy(renames["PostalAddressIn"]).optional(),
        }
    ).named(renames["AddressVerificationDataIn"])
    types["AddressVerificationDataOut"] = t.struct(
        {
            "business": t.string().optional(),
            "expectedDeliveryDaysRegion": t.integer().optional(),
            "address": t.proxy(renames["PostalAddressOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddressVerificationDataOut"])
    types["VerificationTokenIn"] = t.struct(
        {"tokenString": t.string().optional()}
    ).named(renames["VerificationTokenIn"])
    types["VerificationTokenOut"] = t.struct(
        {
            "tokenString": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VerificationTokenOut"])
    types["FetchVerificationOptionsResponseIn"] = t.struct(
        {"options": t.array(t.proxy(renames["VerificationOptionIn"])).optional()}
    ).named(renames["FetchVerificationOptionsResponseIn"])
    types["FetchVerificationOptionsResponseOut"] = t.struct(
        {
            "options": t.array(t.proxy(renames["VerificationOptionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FetchVerificationOptionsResponseOut"])
    types["CompleteVerificationResponseIn"] = t.struct(
        {"verification": t.proxy(renames["VerificationIn"]).optional()}
    ).named(renames["CompleteVerificationResponseIn"])
    types["CompleteVerificationResponseOut"] = t.struct(
        {
            "verification": t.proxy(renames["VerificationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CompleteVerificationResponseOut"])
    types["GenerateVerificationTokenRequestIn"] = t.struct(
        {"location": t.proxy(renames["LocationIn"])}
    ).named(renames["GenerateVerificationTokenRequestIn"])
    types["GenerateVerificationTokenRequestOut"] = t.struct(
        {
            "location": t.proxy(renames["LocationOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateVerificationTokenRequestOut"])
    types["VerifyLocationResponseIn"] = t.struct(
        {"verification": t.proxy(renames["VerificationIn"]).optional()}
    ).named(renames["VerifyLocationResponseIn"])
    types["VerifyLocationResponseOut"] = t.struct(
        {
            "verification": t.proxy(renames["VerificationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VerifyLocationResponseOut"])
    types["VerificationOptionIn"] = t.struct(
        {
            "phoneNumber": t.string().optional(),
            "addressData": t.proxy(renames["AddressVerificationDataIn"]).optional(),
            "announcement": t.string().optional(),
            "verificationMethod": t.string().optional(),
            "emailData": t.proxy(renames["EmailVerificationDataIn"]).optional(),
        }
    ).named(renames["VerificationOptionIn"])
    types["VerificationOptionOut"] = t.struct(
        {
            "phoneNumber": t.string().optional(),
            "addressData": t.proxy(renames["AddressVerificationDataOut"]).optional(),
            "announcement": t.string().optional(),
            "verificationMethod": t.string().optional(),
            "emailData": t.proxy(renames["EmailVerificationDataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VerificationOptionOut"])
    types["VerifyLocationRequestIn"] = t.struct(
        {
            "context": t.proxy(renames["ServiceBusinessContextIn"]).optional(),
            "mailerContact": t.string().optional(),
            "emailAddress": t.string().optional(),
            "phoneNumber": t.string().optional(),
            "token": t.proxy(renames["VerificationTokenIn"]).optional(),
            "languageCode": t.string().optional(),
            "method": t.string(),
        }
    ).named(renames["VerifyLocationRequestIn"])
    types["VerifyLocationRequestOut"] = t.struct(
        {
            "context": t.proxy(renames["ServiceBusinessContextOut"]).optional(),
            "mailerContact": t.string().optional(),
            "emailAddress": t.string().optional(),
            "phoneNumber": t.string().optional(),
            "token": t.proxy(renames["VerificationTokenOut"]).optional(),
            "languageCode": t.string().optional(),
            "method": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VerifyLocationRequestOut"])
    types["EmailVerificationDataIn"] = t.struct(
        {
            "user": t.string().optional(),
            "isUserNameEditable": t.boolean().optional(),
            "domain": t.string().optional(),
        }
    ).named(renames["EmailVerificationDataIn"])
    types["EmailVerificationDataOut"] = t.struct(
        {
            "user": t.string().optional(),
            "isUserNameEditable": t.boolean().optional(),
            "domain": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EmailVerificationDataOut"])
    types["VoiceOfMerchantStateIn"] = t.struct(
        {
            "verify": t.proxy(renames["VerifyIn"]).optional(),
            "waitForVoiceOfMerchant": t.proxy(
                renames["WaitForVoiceOfMerchantIn"]
            ).optional(),
            "hasBusinessAuthority": t.boolean().optional(),
            "resolveOwnershipConflict": t.proxy(
                renames["ResolveOwnershipConflictIn"]
            ).optional(),
            "hasVoiceOfMerchant": t.boolean().optional(),
            "complyWithGuidelines": t.proxy(
                renames["ComplyWithGuidelinesIn"]
            ).optional(),
        }
    ).named(renames["VoiceOfMerchantStateIn"])
    types["VoiceOfMerchantStateOut"] = t.struct(
        {
            "verify": t.proxy(renames["VerifyOut"]).optional(),
            "waitForVoiceOfMerchant": t.proxy(
                renames["WaitForVoiceOfMerchantOut"]
            ).optional(),
            "hasBusinessAuthority": t.boolean().optional(),
            "resolveOwnershipConflict": t.proxy(
                renames["ResolveOwnershipConflictOut"]
            ).optional(),
            "hasVoiceOfMerchant": t.boolean().optional(),
            "complyWithGuidelines": t.proxy(
                renames["ComplyWithGuidelinesOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VoiceOfMerchantStateOut"])
    types["ComplyWithGuidelinesIn"] = t.struct(
        {"recommendationReason": t.string().optional()}
    ).named(renames["ComplyWithGuidelinesIn"])
    types["ComplyWithGuidelinesOut"] = t.struct(
        {
            "recommendationReason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComplyWithGuidelinesOut"])
    types["VerificationIn"] = t.struct(
        {
            "announcement": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "method": t.string().optional(),
            "state": t.string().optional(),
        }
    ).named(renames["VerificationIn"])
    types["VerificationOut"] = t.struct(
        {
            "announcement": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "method": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VerificationOut"])
    types["GenerateVerificationTokenResponseIn"] = t.struct(
        {"token": t.proxy(renames["VerificationTokenIn"]).optional()}
    ).named(renames["GenerateVerificationTokenResponseIn"])
    types["GenerateVerificationTokenResponseOut"] = t.struct(
        {
            "token": t.proxy(renames["VerificationTokenOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateVerificationTokenResponseOut"])

    functions = {}
    functions["locationsVerify"] = mybusinessverifications.post(
        "v1/{location}:fetchVerificationOptions",
        t.struct(
            {
                "location": t.string(),
                "context": t.proxy(renames["ServiceBusinessContextIn"]).optional(),
                "languageCode": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FetchVerificationOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsGetVoiceOfMerchantState"] = mybusinessverifications.post(
        "v1/{location}:fetchVerificationOptions",
        t.struct(
            {
                "location": t.string(),
                "context": t.proxy(renames["ServiceBusinessContextIn"]).optional(),
                "languageCode": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FetchVerificationOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsFetchVerificationOptions"] = mybusinessverifications.post(
        "v1/{location}:fetchVerificationOptions",
        t.struct(
            {
                "location": t.string(),
                "context": t.proxy(renames["ServiceBusinessContextIn"]).optional(),
                "languageCode": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FetchVerificationOptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsVerificationsComplete"] = mybusinessverifications.get(
        "v1/{parent}/verifications",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
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
        types=Box(types),
        functions=Box(functions),
    )
