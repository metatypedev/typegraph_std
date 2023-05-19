from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_mybusinessverifications() -> Import:
    mybusinessverifications = HTTPRuntime(
        "https://mybusinessverifications.googleapis.com/"
    )

    renames = {
        "ErrorResponse": "_mybusinessverifications_1_ErrorResponse",
        "WaitForVoiceOfMerchantIn": "_mybusinessverifications_2_WaitForVoiceOfMerchantIn",
        "WaitForVoiceOfMerchantOut": "_mybusinessverifications_3_WaitForVoiceOfMerchantOut",
        "VerifyIn": "_mybusinessverifications_4_VerifyIn",
        "VerifyOut": "_mybusinessverifications_5_VerifyOut",
        "ServiceBusinessContextIn": "_mybusinessverifications_6_ServiceBusinessContextIn",
        "ServiceBusinessContextOut": "_mybusinessverifications_7_ServiceBusinessContextOut",
        "VerifyLocationRequestIn": "_mybusinessverifications_8_VerifyLocationRequestIn",
        "VerifyLocationRequestOut": "_mybusinessverifications_9_VerifyLocationRequestOut",
        "EmailVerificationDataIn": "_mybusinessverifications_10_EmailVerificationDataIn",
        "EmailVerificationDataOut": "_mybusinessverifications_11_EmailVerificationDataOut",
        "GenerateVerificationTokenRequestIn": "_mybusinessverifications_12_GenerateVerificationTokenRequestIn",
        "GenerateVerificationTokenRequestOut": "_mybusinessverifications_13_GenerateVerificationTokenRequestOut",
        "LocationIn": "_mybusinessverifications_14_LocationIn",
        "LocationOut": "_mybusinessverifications_15_LocationOut",
        "AddressVerificationDataIn": "_mybusinessverifications_16_AddressVerificationDataIn",
        "AddressVerificationDataOut": "_mybusinessverifications_17_AddressVerificationDataOut",
        "FetchVerificationOptionsResponseIn": "_mybusinessverifications_18_FetchVerificationOptionsResponseIn",
        "FetchVerificationOptionsResponseOut": "_mybusinessverifications_19_FetchVerificationOptionsResponseOut",
        "GenerateVerificationTokenResponseIn": "_mybusinessverifications_20_GenerateVerificationTokenResponseIn",
        "GenerateVerificationTokenResponseOut": "_mybusinessverifications_21_GenerateVerificationTokenResponseOut",
        "ComplyWithGuidelinesIn": "_mybusinessverifications_22_ComplyWithGuidelinesIn",
        "ComplyWithGuidelinesOut": "_mybusinessverifications_23_ComplyWithGuidelinesOut",
        "CompleteVerificationResponseIn": "_mybusinessverifications_24_CompleteVerificationResponseIn",
        "CompleteVerificationResponseOut": "_mybusinessverifications_25_CompleteVerificationResponseOut",
        "VoiceOfMerchantStateIn": "_mybusinessverifications_26_VoiceOfMerchantStateIn",
        "VoiceOfMerchantStateOut": "_mybusinessverifications_27_VoiceOfMerchantStateOut",
        "VerificationIn": "_mybusinessverifications_28_VerificationIn",
        "VerificationOut": "_mybusinessverifications_29_VerificationOut",
        "CompleteVerificationRequestIn": "_mybusinessverifications_30_CompleteVerificationRequestIn",
        "CompleteVerificationRequestOut": "_mybusinessverifications_31_CompleteVerificationRequestOut",
        "ListVerificationsResponseIn": "_mybusinessverifications_32_ListVerificationsResponseIn",
        "ListVerificationsResponseOut": "_mybusinessverifications_33_ListVerificationsResponseOut",
        "VerifyLocationResponseIn": "_mybusinessverifications_34_VerifyLocationResponseIn",
        "VerifyLocationResponseOut": "_mybusinessverifications_35_VerifyLocationResponseOut",
        "ResolveOwnershipConflictIn": "_mybusinessverifications_36_ResolveOwnershipConflictIn",
        "ResolveOwnershipConflictOut": "_mybusinessverifications_37_ResolveOwnershipConflictOut",
        "VerificationOptionIn": "_mybusinessverifications_38_VerificationOptionIn",
        "VerificationOptionOut": "_mybusinessverifications_39_VerificationOptionOut",
        "VerificationTokenIn": "_mybusinessverifications_40_VerificationTokenIn",
        "VerificationTokenOut": "_mybusinessverifications_41_VerificationTokenOut",
        "PostalAddressIn": "_mybusinessverifications_42_PostalAddressIn",
        "PostalAddressOut": "_mybusinessverifications_43_PostalAddressOut",
        "FetchVerificationOptionsRequestIn": "_mybusinessverifications_44_FetchVerificationOptionsRequestIn",
        "FetchVerificationOptionsRequestOut": "_mybusinessverifications_45_FetchVerificationOptionsRequestOut",
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
    types["VerifyIn"] = t.struct(
        {"hasPendingVerification": t.boolean().optional()}
    ).named(renames["VerifyIn"])
    types["VerifyOut"] = t.struct(
        {
            "hasPendingVerification": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VerifyOut"])
    types["ServiceBusinessContextIn"] = t.struct(
        {"address": t.proxy(renames["PostalAddressIn"]).optional()}
    ).named(renames["ServiceBusinessContextIn"])
    types["ServiceBusinessContextOut"] = t.struct(
        {
            "address": t.proxy(renames["PostalAddressOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceBusinessContextOut"])
    types["VerifyLocationRequestIn"] = t.struct(
        {
            "method": t.string(),
            "languageCode": t.string().optional(),
            "context": t.proxy(renames["ServiceBusinessContextIn"]).optional(),
            "phoneNumber": t.string().optional(),
            "token": t.proxy(renames["VerificationTokenIn"]).optional(),
            "mailerContact": t.string().optional(),
            "emailAddress": t.string().optional(),
        }
    ).named(renames["VerifyLocationRequestIn"])
    types["VerifyLocationRequestOut"] = t.struct(
        {
            "method": t.string(),
            "languageCode": t.string().optional(),
            "context": t.proxy(renames["ServiceBusinessContextOut"]).optional(),
            "phoneNumber": t.string().optional(),
            "token": t.proxy(renames["VerificationTokenOut"]).optional(),
            "mailerContact": t.string().optional(),
            "emailAddress": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VerifyLocationRequestOut"])
    types["EmailVerificationDataIn"] = t.struct(
        {
            "isUserNameEditable": t.boolean().optional(),
            "user": t.string().optional(),
            "domain": t.string().optional(),
        }
    ).named(renames["EmailVerificationDataIn"])
    types["EmailVerificationDataOut"] = t.struct(
        {
            "isUserNameEditable": t.boolean().optional(),
            "user": t.string().optional(),
            "domain": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EmailVerificationDataOut"])
    types["GenerateVerificationTokenRequestIn"] = t.struct(
        {"location": t.proxy(renames["LocationIn"])}
    ).named(renames["GenerateVerificationTokenRequestIn"])
    types["GenerateVerificationTokenRequestOut"] = t.struct(
        {
            "location": t.proxy(renames["LocationOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateVerificationTokenRequestOut"])
    types["LocationIn"] = t.struct(
        {
            "websiteUri": t.string().optional(),
            "address": t.proxy(renames["PostalAddressIn"]),
            "name": t.string(),
            "primaryPhone": t.string().optional(),
            "primaryCategoryId": t.string(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "websiteUri": t.string().optional(),
            "address": t.proxy(renames["PostalAddressOut"]),
            "name": t.string(),
            "primaryPhone": t.string().optional(),
            "primaryCategoryId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["AddressVerificationDataIn"] = t.struct(
        {
            "address": t.proxy(renames["PostalAddressIn"]).optional(),
            "business": t.string().optional(),
            "expectedDeliveryDaysRegion": t.integer().optional(),
        }
    ).named(renames["AddressVerificationDataIn"])
    types["AddressVerificationDataOut"] = t.struct(
        {
            "address": t.proxy(renames["PostalAddressOut"]).optional(),
            "business": t.string().optional(),
            "expectedDeliveryDaysRegion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddressVerificationDataOut"])
    types["FetchVerificationOptionsResponseIn"] = t.struct(
        {"options": t.array(t.proxy(renames["VerificationOptionIn"])).optional()}
    ).named(renames["FetchVerificationOptionsResponseIn"])
    types["FetchVerificationOptionsResponseOut"] = t.struct(
        {
            "options": t.array(t.proxy(renames["VerificationOptionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FetchVerificationOptionsResponseOut"])
    types["GenerateVerificationTokenResponseIn"] = t.struct(
        {"token": t.proxy(renames["VerificationTokenIn"]).optional()}
    ).named(renames["GenerateVerificationTokenResponseIn"])
    types["GenerateVerificationTokenResponseOut"] = t.struct(
        {
            "token": t.proxy(renames["VerificationTokenOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateVerificationTokenResponseOut"])
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
    types["VoiceOfMerchantStateIn"] = t.struct(
        {
            "verify": t.proxy(renames["VerifyIn"]).optional(),
            "resolveOwnershipConflict": t.proxy(
                renames["ResolveOwnershipConflictIn"]
            ).optional(),
            "complyWithGuidelines": t.proxy(
                renames["ComplyWithGuidelinesIn"]
            ).optional(),
            "hasBusinessAuthority": t.boolean().optional(),
            "hasVoiceOfMerchant": t.boolean().optional(),
            "waitForVoiceOfMerchant": t.proxy(
                renames["WaitForVoiceOfMerchantIn"]
            ).optional(),
        }
    ).named(renames["VoiceOfMerchantStateIn"])
    types["VoiceOfMerchantStateOut"] = t.struct(
        {
            "verify": t.proxy(renames["VerifyOut"]).optional(),
            "resolveOwnershipConflict": t.proxy(
                renames["ResolveOwnershipConflictOut"]
            ).optional(),
            "complyWithGuidelines": t.proxy(
                renames["ComplyWithGuidelinesOut"]
            ).optional(),
            "hasBusinessAuthority": t.boolean().optional(),
            "hasVoiceOfMerchant": t.boolean().optional(),
            "waitForVoiceOfMerchant": t.proxy(
                renames["WaitForVoiceOfMerchantOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VoiceOfMerchantStateOut"])
    types["VerificationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "announcement": t.string().optional(),
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "method": t.string().optional(),
        }
    ).named(renames["VerificationIn"])
    types["VerificationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "announcement": t.string().optional(),
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "method": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VerificationOut"])
    types["CompleteVerificationRequestIn"] = t.struct({"pin": t.string()}).named(
        renames["CompleteVerificationRequestIn"]
    )
    types["CompleteVerificationRequestOut"] = t.struct(
        {"pin": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CompleteVerificationRequestOut"])
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
    types["VerifyLocationResponseIn"] = t.struct(
        {"verification": t.proxy(renames["VerificationIn"]).optional()}
    ).named(renames["VerifyLocationResponseIn"])
    types["VerifyLocationResponseOut"] = t.struct(
        {
            "verification": t.proxy(renames["VerificationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VerifyLocationResponseOut"])
    types["ResolveOwnershipConflictIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ResolveOwnershipConflictIn"]
    )
    types["ResolveOwnershipConflictOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ResolveOwnershipConflictOut"])
    types["VerificationOptionIn"] = t.struct(
        {
            "announcement": t.string().optional(),
            "phoneNumber": t.string().optional(),
            "verificationMethod": t.string().optional(),
            "addressData": t.proxy(renames["AddressVerificationDataIn"]).optional(),
            "emailData": t.proxy(renames["EmailVerificationDataIn"]).optional(),
        }
    ).named(renames["VerificationOptionIn"])
    types["VerificationOptionOut"] = t.struct(
        {
            "announcement": t.string().optional(),
            "phoneNumber": t.string().optional(),
            "verificationMethod": t.string().optional(),
            "addressData": t.proxy(renames["AddressVerificationDataOut"]).optional(),
            "emailData": t.proxy(renames["EmailVerificationDataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VerificationOptionOut"])
    types["VerificationTokenIn"] = t.struct(
        {"tokenString": t.string().optional()}
    ).named(renames["VerificationTokenIn"])
    types["VerificationTokenOut"] = t.struct(
        {
            "tokenString": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VerificationTokenOut"])
    types["PostalAddressIn"] = t.struct(
        {
            "addressLines": t.array(t.string()).optional(),
            "languageCode": t.string().optional(),
            "administrativeArea": t.string().optional(),
            "organization": t.string().optional(),
            "revision": t.integer().optional(),
            "regionCode": t.string(),
            "sortingCode": t.string().optional(),
            "sublocality": t.string().optional(),
            "postalCode": t.string().optional(),
            "locality": t.string().optional(),
            "recipients": t.array(t.string()).optional(),
        }
    ).named(renames["PostalAddressIn"])
    types["PostalAddressOut"] = t.struct(
        {
            "addressLines": t.array(t.string()).optional(),
            "languageCode": t.string().optional(),
            "administrativeArea": t.string().optional(),
            "organization": t.string().optional(),
            "revision": t.integer().optional(),
            "regionCode": t.string(),
            "sortingCode": t.string().optional(),
            "sublocality": t.string().optional(),
            "postalCode": t.string().optional(),
            "locality": t.string().optional(),
            "recipients": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostalAddressOut"])
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

    functions = {}
    functions["locationsGetVoiceOfMerchantState"] = mybusinessverifications.post(
        "v1/{name}:verify",
        t.struct(
            {
                "name": t.string(),
                "method": t.string(),
                "languageCode": t.string().optional(),
                "context": t.proxy(renames["ServiceBusinessContextIn"]).optional(),
                "phoneNumber": t.string().optional(),
                "token": t.proxy(renames["VerificationTokenIn"]).optional(),
                "mailerContact": t.string().optional(),
                "emailAddress": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VerifyLocationResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsFetchVerificationOptions"] = mybusinessverifications.post(
        "v1/{name}:verify",
        t.struct(
            {
                "name": t.string(),
                "method": t.string(),
                "languageCode": t.string().optional(),
                "context": t.proxy(renames["ServiceBusinessContextIn"]).optional(),
                "phoneNumber": t.string().optional(),
                "token": t.proxy(renames["VerificationTokenIn"]).optional(),
                "mailerContact": t.string().optional(),
                "emailAddress": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VerifyLocationResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsVerify"] = mybusinessverifications.post(
        "v1/{name}:verify",
        t.struct(
            {
                "name": t.string(),
                "method": t.string(),
                "languageCode": t.string().optional(),
                "context": t.proxy(renames["ServiceBusinessContextIn"]).optional(),
                "phoneNumber": t.string().optional(),
                "token": t.proxy(renames["VerificationTokenIn"]).optional(),
                "mailerContact": t.string().optional(),
                "emailAddress": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VerifyLocationResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsVerificationsComplete"] = mybusinessverifications.get(
        "v1/{parent}/verifications",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
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
                "parent": t.string(),
                "pageToken": t.string().optional(),
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
