from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_mybusinessverifications():
    mybusinessverifications = HTTPRuntime(
        "https://mybusinessverifications.googleapis.com/"
    )

    renames = {
        "ErrorResponse": "_mybusinessverifications_1_ErrorResponse",
        "WaitForVoiceOfMerchantIn": "_mybusinessverifications_2_WaitForVoiceOfMerchantIn",
        "WaitForVoiceOfMerchantOut": "_mybusinessverifications_3_WaitForVoiceOfMerchantOut",
        "EmailVerificationDataIn": "_mybusinessverifications_4_EmailVerificationDataIn",
        "EmailVerificationDataOut": "_mybusinessverifications_5_EmailVerificationDataOut",
        "VerifyLocationRequestIn": "_mybusinessverifications_6_VerifyLocationRequestIn",
        "VerifyLocationRequestOut": "_mybusinessverifications_7_VerifyLocationRequestOut",
        "PostalAddressIn": "_mybusinessverifications_8_PostalAddressIn",
        "PostalAddressOut": "_mybusinessverifications_9_PostalAddressOut",
        "FetchVerificationOptionsResponseIn": "_mybusinessverifications_10_FetchVerificationOptionsResponseIn",
        "FetchVerificationOptionsResponseOut": "_mybusinessverifications_11_FetchVerificationOptionsResponseOut",
        "VerifyIn": "_mybusinessverifications_12_VerifyIn",
        "VerifyOut": "_mybusinessverifications_13_VerifyOut",
        "AddressVerificationDataIn": "_mybusinessverifications_14_AddressVerificationDataIn",
        "AddressVerificationDataOut": "_mybusinessverifications_15_AddressVerificationDataOut",
        "ComplyWithGuidelinesIn": "_mybusinessverifications_16_ComplyWithGuidelinesIn",
        "ComplyWithGuidelinesOut": "_mybusinessverifications_17_ComplyWithGuidelinesOut",
        "ServiceBusinessContextIn": "_mybusinessverifications_18_ServiceBusinessContextIn",
        "ServiceBusinessContextOut": "_mybusinessverifications_19_ServiceBusinessContextOut",
        "VoiceOfMerchantStateIn": "_mybusinessverifications_20_VoiceOfMerchantStateIn",
        "VoiceOfMerchantStateOut": "_mybusinessverifications_21_VoiceOfMerchantStateOut",
        "ListVerificationsResponseIn": "_mybusinessverifications_22_ListVerificationsResponseIn",
        "ListVerificationsResponseOut": "_mybusinessverifications_23_ListVerificationsResponseOut",
        "VerificationOptionIn": "_mybusinessverifications_24_VerificationOptionIn",
        "VerificationOptionOut": "_mybusinessverifications_25_VerificationOptionOut",
        "GenerateVerificationTokenRequestIn": "_mybusinessverifications_26_GenerateVerificationTokenRequestIn",
        "GenerateVerificationTokenRequestOut": "_mybusinessverifications_27_GenerateVerificationTokenRequestOut",
        "VerificationIn": "_mybusinessverifications_28_VerificationIn",
        "VerificationOut": "_mybusinessverifications_29_VerificationOut",
        "FetchVerificationOptionsRequestIn": "_mybusinessverifications_30_FetchVerificationOptionsRequestIn",
        "FetchVerificationOptionsRequestOut": "_mybusinessverifications_31_FetchVerificationOptionsRequestOut",
        "CompleteVerificationRequestIn": "_mybusinessverifications_32_CompleteVerificationRequestIn",
        "CompleteVerificationRequestOut": "_mybusinessverifications_33_CompleteVerificationRequestOut",
        "VerifyLocationResponseIn": "_mybusinessverifications_34_VerifyLocationResponseIn",
        "VerifyLocationResponseOut": "_mybusinessverifications_35_VerifyLocationResponseOut",
        "LocationIn": "_mybusinessverifications_36_LocationIn",
        "LocationOut": "_mybusinessverifications_37_LocationOut",
        "VerificationTokenIn": "_mybusinessverifications_38_VerificationTokenIn",
        "VerificationTokenOut": "_mybusinessverifications_39_VerificationTokenOut",
        "ResolveOwnershipConflictIn": "_mybusinessverifications_40_ResolveOwnershipConflictIn",
        "ResolveOwnershipConflictOut": "_mybusinessverifications_41_ResolveOwnershipConflictOut",
        "GenerateVerificationTokenResponseIn": "_mybusinessverifications_42_GenerateVerificationTokenResponseIn",
        "GenerateVerificationTokenResponseOut": "_mybusinessverifications_43_GenerateVerificationTokenResponseOut",
        "CompleteVerificationResponseIn": "_mybusinessverifications_44_CompleteVerificationResponseIn",
        "CompleteVerificationResponseOut": "_mybusinessverifications_45_CompleteVerificationResponseOut",
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
    types["VerifyLocationRequestIn"] = t.struct(
        {
            "token": t.proxy(renames["VerificationTokenIn"]).optional(),
            "languageCode": t.string().optional(),
            "mailerContact": t.string().optional(),
            "context": t.proxy(renames["ServiceBusinessContextIn"]).optional(),
            "emailAddress": t.string().optional(),
            "phoneNumber": t.string().optional(),
            "method": t.string(),
        }
    ).named(renames["VerifyLocationRequestIn"])
    types["VerifyLocationRequestOut"] = t.struct(
        {
            "token": t.proxy(renames["VerificationTokenOut"]).optional(),
            "languageCode": t.string().optional(),
            "mailerContact": t.string().optional(),
            "context": t.proxy(renames["ServiceBusinessContextOut"]).optional(),
            "emailAddress": t.string().optional(),
            "phoneNumber": t.string().optional(),
            "method": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VerifyLocationRequestOut"])
    types["PostalAddressIn"] = t.struct(
        {
            "sortingCode": t.string().optional(),
            "languageCode": t.string().optional(),
            "organization": t.string().optional(),
            "recipients": t.array(t.string()).optional(),
            "postalCode": t.string().optional(),
            "revision": t.integer().optional(),
            "sublocality": t.string().optional(),
            "administrativeArea": t.string().optional(),
            "addressLines": t.array(t.string()).optional(),
            "regionCode": t.string(),
            "locality": t.string().optional(),
        }
    ).named(renames["PostalAddressIn"])
    types["PostalAddressOut"] = t.struct(
        {
            "sortingCode": t.string().optional(),
            "languageCode": t.string().optional(),
            "organization": t.string().optional(),
            "recipients": t.array(t.string()).optional(),
            "postalCode": t.string().optional(),
            "revision": t.integer().optional(),
            "sublocality": t.string().optional(),
            "administrativeArea": t.string().optional(),
            "addressLines": t.array(t.string()).optional(),
            "regionCode": t.string(),
            "locality": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostalAddressOut"])
    types["FetchVerificationOptionsResponseIn"] = t.struct(
        {"options": t.array(t.proxy(renames["VerificationOptionIn"])).optional()}
    ).named(renames["FetchVerificationOptionsResponseIn"])
    types["FetchVerificationOptionsResponseOut"] = t.struct(
        {
            "options": t.array(t.proxy(renames["VerificationOptionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FetchVerificationOptionsResponseOut"])
    types["VerifyIn"] = t.struct(
        {"hasPendingVerification": t.boolean().optional()}
    ).named(renames["VerifyIn"])
    types["VerifyOut"] = t.struct(
        {
            "hasPendingVerification": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VerifyOut"])
    types["AddressVerificationDataIn"] = t.struct(
        {
            "expectedDeliveryDaysRegion": t.integer().optional(),
            "business": t.string().optional(),
            "address": t.proxy(renames["PostalAddressIn"]).optional(),
        }
    ).named(renames["AddressVerificationDataIn"])
    types["AddressVerificationDataOut"] = t.struct(
        {
            "expectedDeliveryDaysRegion": t.integer().optional(),
            "business": t.string().optional(),
            "address": t.proxy(renames["PostalAddressOut"]).optional(),
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
            "waitForVoiceOfMerchant": t.proxy(
                renames["WaitForVoiceOfMerchantIn"]
            ).optional(),
            "complyWithGuidelines": t.proxy(
                renames["ComplyWithGuidelinesIn"]
            ).optional(),
            "verify": t.proxy(renames["VerifyIn"]).optional(),
            "resolveOwnershipConflict": t.proxy(
                renames["ResolveOwnershipConflictIn"]
            ).optional(),
            "hasBusinessAuthority": t.boolean().optional(),
            "hasVoiceOfMerchant": t.boolean().optional(),
        }
    ).named(renames["VoiceOfMerchantStateIn"])
    types["VoiceOfMerchantStateOut"] = t.struct(
        {
            "waitForVoiceOfMerchant": t.proxy(
                renames["WaitForVoiceOfMerchantOut"]
            ).optional(),
            "complyWithGuidelines": t.proxy(
                renames["ComplyWithGuidelinesOut"]
            ).optional(),
            "verify": t.proxy(renames["VerifyOut"]).optional(),
            "resolveOwnershipConflict": t.proxy(
                renames["ResolveOwnershipConflictOut"]
            ).optional(),
            "hasBusinessAuthority": t.boolean().optional(),
            "hasVoiceOfMerchant": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VoiceOfMerchantStateOut"])
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
    types["VerificationOptionIn"] = t.struct(
        {
            "announcement": t.string().optional(),
            "verificationMethod": t.string().optional(),
            "emailData": t.proxy(renames["EmailVerificationDataIn"]).optional(),
            "addressData": t.proxy(renames["AddressVerificationDataIn"]).optional(),
            "phoneNumber": t.string().optional(),
        }
    ).named(renames["VerificationOptionIn"])
    types["VerificationOptionOut"] = t.struct(
        {
            "announcement": t.string().optional(),
            "verificationMethod": t.string().optional(),
            "emailData": t.proxy(renames["EmailVerificationDataOut"]).optional(),
            "addressData": t.proxy(renames["AddressVerificationDataOut"]).optional(),
            "phoneNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VerificationOptionOut"])
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
            "announcement": t.string().optional(),
            "createTime": t.string().optional(),
            "method": t.string().optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
        }
    ).named(renames["VerificationIn"])
    types["VerificationOut"] = t.struct(
        {
            "announcement": t.string().optional(),
            "createTime": t.string().optional(),
            "method": t.string().optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VerificationOut"])
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
    types["CompleteVerificationRequestIn"] = t.struct({"pin": t.string()}).named(
        renames["CompleteVerificationRequestIn"]
    )
    types["CompleteVerificationRequestOut"] = t.struct(
        {"pin": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CompleteVerificationRequestOut"])
    types["VerifyLocationResponseIn"] = t.struct(
        {"verification": t.proxy(renames["VerificationIn"]).optional()}
    ).named(renames["VerifyLocationResponseIn"])
    types["VerifyLocationResponseOut"] = t.struct(
        {
            "verification": t.proxy(renames["VerificationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VerifyLocationResponseOut"])
    types["LocationIn"] = t.struct(
        {
            "primaryPhone": t.string().optional(),
            "primaryCategoryId": t.string(),
            "name": t.string(),
            "websiteUri": t.string().optional(),
            "address": t.proxy(renames["PostalAddressIn"]),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "primaryPhone": t.string().optional(),
            "primaryCategoryId": t.string(),
            "name": t.string(),
            "websiteUri": t.string().optional(),
            "address": t.proxy(renames["PostalAddressOut"]),
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
    types["ResolveOwnershipConflictIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ResolveOwnershipConflictIn"]
    )
    types["ResolveOwnershipConflictOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ResolveOwnershipConflictOut"])
    types["GenerateVerificationTokenResponseIn"] = t.struct(
        {"token": t.proxy(renames["VerificationTokenIn"]).optional()}
    ).named(renames["GenerateVerificationTokenResponseIn"])
    types["GenerateVerificationTokenResponseOut"] = t.struct(
        {
            "token": t.proxy(renames["VerificationTokenOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateVerificationTokenResponseOut"])
    types["CompleteVerificationResponseIn"] = t.struct(
        {"verification": t.proxy(renames["VerificationIn"]).optional()}
    ).named(renames["CompleteVerificationResponseIn"])
    types["CompleteVerificationResponseOut"] = t.struct(
        {
            "verification": t.proxy(renames["VerificationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CompleteVerificationResponseOut"])

    functions = {}
    functions["verificationTokensGenerate"] = mybusinessverifications.post(
        "v1/verificationTokens:generate",
        t.struct(
            {"location": t.proxy(renames["LocationIn"]), "auth": t.string().optional()}
        ),
        t.proxy(renames["GenerateVerificationTokenResponseOut"]),
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
    functions["locationsVerify"] = mybusinessverifications.get(
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
    functions["locationsVerificationsList"] = mybusinessverifications.post(
        "v1/{name}:complete",
        t.struct(
            {"name": t.string(), "pin": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["CompleteVerificationResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsVerificationsComplete"] = mybusinessverifications.post(
        "v1/{name}:complete",
        t.struct(
            {"name": t.string(), "pin": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["CompleteVerificationResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="mybusinessverifications",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
