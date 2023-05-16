from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_identitytoolkit() -> Import:
    identitytoolkit = HTTPRuntime("https://www.googleapis.com/")

    renames = {
        "ErrorResponse": "_identitytoolkit_1_ErrorResponse",
        "IdentitytoolkitRelyingpartyGetPublicKeysResponseIn": "_identitytoolkit_2_IdentitytoolkitRelyingpartyGetPublicKeysResponseIn",
        "IdentitytoolkitRelyingpartyGetPublicKeysResponseOut": "_identitytoolkit_3_IdentitytoolkitRelyingpartyGetPublicKeysResponseOut",
        "SignupNewUserResponseIn": "_identitytoolkit_4_SignupNewUserResponseIn",
        "SignupNewUserResponseOut": "_identitytoolkit_5_SignupNewUserResponseOut",
        "SetAccountInfoResponseIn": "_identitytoolkit_6_SetAccountInfoResponseIn",
        "SetAccountInfoResponseOut": "_identitytoolkit_7_SetAccountInfoResponseOut",
        "IdentitytoolkitRelyingpartyGetAccountInfoRequestIn": "_identitytoolkit_8_IdentitytoolkitRelyingpartyGetAccountInfoRequestIn",
        "IdentitytoolkitRelyingpartyGetAccountInfoRequestOut": "_identitytoolkit_9_IdentitytoolkitRelyingpartyGetAccountInfoRequestOut",
        "VerifyCustomTokenResponseIn": "_identitytoolkit_10_VerifyCustomTokenResponseIn",
        "VerifyCustomTokenResponseOut": "_identitytoolkit_11_VerifyCustomTokenResponseOut",
        "IdentitytoolkitRelyingpartyVerifyPhoneNumberResponseIn": "_identitytoolkit_12_IdentitytoolkitRelyingpartyVerifyPhoneNumberResponseIn",
        "IdentitytoolkitRelyingpartyVerifyPhoneNumberResponseOut": "_identitytoolkit_13_IdentitytoolkitRelyingpartyVerifyPhoneNumberResponseOut",
        "IdentitytoolkitRelyingpartySetAccountInfoRequestIn": "_identitytoolkit_14_IdentitytoolkitRelyingpartySetAccountInfoRequestIn",
        "IdentitytoolkitRelyingpartySetAccountInfoRequestOut": "_identitytoolkit_15_IdentitytoolkitRelyingpartySetAccountInfoRequestOut",
        "DownloadAccountResponseIn": "_identitytoolkit_16_DownloadAccountResponseIn",
        "DownloadAccountResponseOut": "_identitytoolkit_17_DownloadAccountResponseOut",
        "IdentitytoolkitRelyingpartySignOutUserResponseIn": "_identitytoolkit_18_IdentitytoolkitRelyingpartySignOutUserResponseIn",
        "IdentitytoolkitRelyingpartySignOutUserResponseOut": "_identitytoolkit_19_IdentitytoolkitRelyingpartySignOutUserResponseOut",
        "IdentitytoolkitRelyingpartyUploadAccountRequestIn": "_identitytoolkit_20_IdentitytoolkitRelyingpartyUploadAccountRequestIn",
        "IdentitytoolkitRelyingpartyUploadAccountRequestOut": "_identitytoolkit_21_IdentitytoolkitRelyingpartyUploadAccountRequestOut",
        "IdentitytoolkitRelyingpartySendVerificationCodeResponseIn": "_identitytoolkit_22_IdentitytoolkitRelyingpartySendVerificationCodeResponseIn",
        "IdentitytoolkitRelyingpartySendVerificationCodeResponseOut": "_identitytoolkit_23_IdentitytoolkitRelyingpartySendVerificationCodeResponseOut",
        "ResetPasswordResponseIn": "_identitytoolkit_24_ResetPasswordResponseIn",
        "ResetPasswordResponseOut": "_identitytoolkit_25_ResetPasswordResponseOut",
        "IdentitytoolkitRelyingpartySignOutUserRequestIn": "_identitytoolkit_26_IdentitytoolkitRelyingpartySignOutUserRequestIn",
        "IdentitytoolkitRelyingpartySignOutUserRequestOut": "_identitytoolkit_27_IdentitytoolkitRelyingpartySignOutUserRequestOut",
        "IdentitytoolkitRelyingpartyVerifyPasswordRequestIn": "_identitytoolkit_28_IdentitytoolkitRelyingpartyVerifyPasswordRequestIn",
        "IdentitytoolkitRelyingpartyVerifyPasswordRequestOut": "_identitytoolkit_29_IdentitytoolkitRelyingpartyVerifyPasswordRequestOut",
        "IdentitytoolkitRelyingpartyVerifyAssertionRequestIn": "_identitytoolkit_30_IdentitytoolkitRelyingpartyVerifyAssertionRequestIn",
        "IdentitytoolkitRelyingpartyVerifyAssertionRequestOut": "_identitytoolkit_31_IdentitytoolkitRelyingpartyVerifyAssertionRequestOut",
        "IdentitytoolkitRelyingpartyVerifyPhoneNumberRequestIn": "_identitytoolkit_32_IdentitytoolkitRelyingpartyVerifyPhoneNumberRequestIn",
        "IdentitytoolkitRelyingpartyVerifyPhoneNumberRequestOut": "_identitytoolkit_33_IdentitytoolkitRelyingpartyVerifyPhoneNumberRequestOut",
        "IdentitytoolkitRelyingpartyGetProjectConfigResponseIn": "_identitytoolkit_34_IdentitytoolkitRelyingpartyGetProjectConfigResponseIn",
        "IdentitytoolkitRelyingpartyGetProjectConfigResponseOut": "_identitytoolkit_35_IdentitytoolkitRelyingpartyGetProjectConfigResponseOut",
        "GetOobConfirmationCodeResponseIn": "_identitytoolkit_36_GetOobConfirmationCodeResponseIn",
        "GetOobConfirmationCodeResponseOut": "_identitytoolkit_37_GetOobConfirmationCodeResponseOut",
        "IdentitytoolkitRelyingpartyEmailLinkSigninRequestIn": "_identitytoolkit_38_IdentitytoolkitRelyingpartyEmailLinkSigninRequestIn",
        "IdentitytoolkitRelyingpartyEmailLinkSigninRequestOut": "_identitytoolkit_39_IdentitytoolkitRelyingpartyEmailLinkSigninRequestOut",
        "IdpConfigIn": "_identitytoolkit_40_IdpConfigIn",
        "IdpConfigOut": "_identitytoolkit_41_IdpConfigOut",
        "GetAccountInfoResponseIn": "_identitytoolkit_42_GetAccountInfoResponseIn",
        "GetAccountInfoResponseOut": "_identitytoolkit_43_GetAccountInfoResponseOut",
        "DeleteAccountResponseIn": "_identitytoolkit_44_DeleteAccountResponseIn",
        "DeleteAccountResponseOut": "_identitytoolkit_45_DeleteAccountResponseOut",
        "IdentitytoolkitRelyingpartySignupNewUserRequestIn": "_identitytoolkit_46_IdentitytoolkitRelyingpartySignupNewUserRequestIn",
        "IdentitytoolkitRelyingpartySignupNewUserRequestOut": "_identitytoolkit_47_IdentitytoolkitRelyingpartySignupNewUserRequestOut",
        "IdentitytoolkitRelyingpartyCreateAuthUriRequestIn": "_identitytoolkit_48_IdentitytoolkitRelyingpartyCreateAuthUriRequestIn",
        "IdentitytoolkitRelyingpartyCreateAuthUriRequestOut": "_identitytoolkit_49_IdentitytoolkitRelyingpartyCreateAuthUriRequestOut",
        "VerifyPasswordResponseIn": "_identitytoolkit_50_VerifyPasswordResponseIn",
        "VerifyPasswordResponseOut": "_identitytoolkit_51_VerifyPasswordResponseOut",
        "IdentitytoolkitRelyingpartyResetPasswordRequestIn": "_identitytoolkit_52_IdentitytoolkitRelyingpartyResetPasswordRequestIn",
        "IdentitytoolkitRelyingpartyResetPasswordRequestOut": "_identitytoolkit_53_IdentitytoolkitRelyingpartyResetPasswordRequestOut",
        "IdentitytoolkitRelyingpartySendVerificationCodeRequestIn": "_identitytoolkit_54_IdentitytoolkitRelyingpartySendVerificationCodeRequestIn",
        "IdentitytoolkitRelyingpartySendVerificationCodeRequestOut": "_identitytoolkit_55_IdentitytoolkitRelyingpartySendVerificationCodeRequestOut",
        "CreateAuthUriResponseIn": "_identitytoolkit_56_CreateAuthUriResponseIn",
        "CreateAuthUriResponseOut": "_identitytoolkit_57_CreateAuthUriResponseOut",
        "GetRecaptchaParamResponseIn": "_identitytoolkit_58_GetRecaptchaParamResponseIn",
        "GetRecaptchaParamResponseOut": "_identitytoolkit_59_GetRecaptchaParamResponseOut",
        "IdentitytoolkitRelyingpartySetProjectConfigResponseIn": "_identitytoolkit_60_IdentitytoolkitRelyingpartySetProjectConfigResponseIn",
        "IdentitytoolkitRelyingpartySetProjectConfigResponseOut": "_identitytoolkit_61_IdentitytoolkitRelyingpartySetProjectConfigResponseOut",
        "IdentitytoolkitRelyingpartyDownloadAccountRequestIn": "_identitytoolkit_62_IdentitytoolkitRelyingpartyDownloadAccountRequestIn",
        "IdentitytoolkitRelyingpartyDownloadAccountRequestOut": "_identitytoolkit_63_IdentitytoolkitRelyingpartyDownloadAccountRequestOut",
        "EmailTemplateIn": "_identitytoolkit_64_EmailTemplateIn",
        "EmailTemplateOut": "_identitytoolkit_65_EmailTemplateOut",
        "UserInfoIn": "_identitytoolkit_66_UserInfoIn",
        "UserInfoOut": "_identitytoolkit_67_UserInfoOut",
        "IdentitytoolkitRelyingpartySetProjectConfigRequestIn": "_identitytoolkit_68_IdentitytoolkitRelyingpartySetProjectConfigRequestIn",
        "IdentitytoolkitRelyingpartySetProjectConfigRequestOut": "_identitytoolkit_69_IdentitytoolkitRelyingpartySetProjectConfigRequestOut",
        "IdentitytoolkitRelyingpartyVerifyCustomTokenRequestIn": "_identitytoolkit_70_IdentitytoolkitRelyingpartyVerifyCustomTokenRequestIn",
        "IdentitytoolkitRelyingpartyVerifyCustomTokenRequestOut": "_identitytoolkit_71_IdentitytoolkitRelyingpartyVerifyCustomTokenRequestOut",
        "EmailLinkSigninResponseIn": "_identitytoolkit_72_EmailLinkSigninResponseIn",
        "EmailLinkSigninResponseOut": "_identitytoolkit_73_EmailLinkSigninResponseOut",
        "IdentitytoolkitRelyingpartyDeleteAccountRequestIn": "_identitytoolkit_74_IdentitytoolkitRelyingpartyDeleteAccountRequestIn",
        "IdentitytoolkitRelyingpartyDeleteAccountRequestOut": "_identitytoolkit_75_IdentitytoolkitRelyingpartyDeleteAccountRequestOut",
        "RelyingpartyIn": "_identitytoolkit_76_RelyingpartyIn",
        "RelyingpartyOut": "_identitytoolkit_77_RelyingpartyOut",
        "VerifyAssertionResponseIn": "_identitytoolkit_78_VerifyAssertionResponseIn",
        "VerifyAssertionResponseOut": "_identitytoolkit_79_VerifyAssertionResponseOut",
        "UploadAccountResponseIn": "_identitytoolkit_80_UploadAccountResponseIn",
        "UploadAccountResponseOut": "_identitytoolkit_81_UploadAccountResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["IdentitytoolkitRelyingpartyGetPublicKeysResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["IdentitytoolkitRelyingpartyGetPublicKeysResponseIn"])
    types["IdentitytoolkitRelyingpartyGetPublicKeysResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["IdentitytoolkitRelyingpartyGetPublicKeysResponseOut"])
    types["SignupNewUserResponseIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "expiresIn": t.string().optional(),
            "refreshToken": t.string().optional(),
            "idToken": t.string().optional(),
            "kind": t.string().optional(),
            "localId": t.string().optional(),
            "email": t.string().optional(),
        }
    ).named(renames["SignupNewUserResponseIn"])
    types["SignupNewUserResponseOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "expiresIn": t.string().optional(),
            "refreshToken": t.string().optional(),
            "idToken": t.string().optional(),
            "kind": t.string().optional(),
            "localId": t.string().optional(),
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SignupNewUserResponseOut"])
    types["SetAccountInfoResponseIn"] = t.struct(
        {
            "photoUrl": t.string().optional(),
            "kind": t.string().optional(),
            "newEmail": t.string().optional(),
            "refreshToken": t.string().optional(),
            "expiresIn": t.string().optional(),
            "idToken": t.string().optional(),
            "email": t.string().optional(),
            "localId": t.string().optional(),
            "passwordHash": t.string().optional(),
            "displayName": t.string().optional(),
            "emailVerified": t.boolean().optional(),
            "providerUserInfo": t.array(
                t.struct(
                    {
                        "displayName": t.string().optional(),
                        "photoUrl": t.string().optional(),
                        "federatedId": t.string().optional(),
                        "providerId": t.string().optional(),
                    }
                )
            ).optional(),
        }
    ).named(renames["SetAccountInfoResponseIn"])
    types["SetAccountInfoResponseOut"] = t.struct(
        {
            "photoUrl": t.string().optional(),
            "kind": t.string().optional(),
            "newEmail": t.string().optional(),
            "refreshToken": t.string().optional(),
            "expiresIn": t.string().optional(),
            "idToken": t.string().optional(),
            "email": t.string().optional(),
            "localId": t.string().optional(),
            "passwordHash": t.string().optional(),
            "displayName": t.string().optional(),
            "emailVerified": t.boolean().optional(),
            "providerUserInfo": t.array(
                t.struct(
                    {
                        "displayName": t.string().optional(),
                        "photoUrl": t.string().optional(),
                        "federatedId": t.string().optional(),
                        "providerId": t.string().optional(),
                    }
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetAccountInfoResponseOut"])
    types["IdentitytoolkitRelyingpartyGetAccountInfoRequestIn"] = t.struct(
        {
            "idToken": t.string().optional(),
            "phoneNumber": t.array(t.string()).optional(),
            "delegatedProjectNumber": t.string().optional(),
            "email": t.array(t.string()).optional(),
            "localId": t.array(t.string()).optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartyGetAccountInfoRequestIn"])
    types["IdentitytoolkitRelyingpartyGetAccountInfoRequestOut"] = t.struct(
        {
            "idToken": t.string().optional(),
            "phoneNumber": t.array(t.string()).optional(),
            "delegatedProjectNumber": t.string().optional(),
            "email": t.array(t.string()).optional(),
            "localId": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartyGetAccountInfoRequestOut"])
    types["VerifyCustomTokenResponseIn"] = t.struct(
        {
            "isNewUser": t.boolean().optional(),
            "refreshToken": t.string().optional(),
            "expiresIn": t.string().optional(),
            "idToken": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["VerifyCustomTokenResponseIn"])
    types["VerifyCustomTokenResponseOut"] = t.struct(
        {
            "isNewUser": t.boolean().optional(),
            "refreshToken": t.string().optional(),
            "expiresIn": t.string().optional(),
            "idToken": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VerifyCustomTokenResponseOut"])
    types["IdentitytoolkitRelyingpartyVerifyPhoneNumberResponseIn"] = t.struct(
        {
            "temporaryProofExpiresIn": t.string(),
            "refreshToken": t.string(),
            "verificationProofExpiresIn": t.string(),
            "phoneNumber": t.string(),
            "temporaryProof": t.string(),
            "verificationProof": t.string(),
            "isNewUser": t.boolean(),
            "expiresIn": t.string(),
            "idToken": t.string(),
            "localId": t.string(),
        }
    ).named(renames["IdentitytoolkitRelyingpartyVerifyPhoneNumberResponseIn"])
    types["IdentitytoolkitRelyingpartyVerifyPhoneNumberResponseOut"] = t.struct(
        {
            "temporaryProofExpiresIn": t.string(),
            "refreshToken": t.string(),
            "verificationProofExpiresIn": t.string(),
            "phoneNumber": t.string(),
            "temporaryProof": t.string(),
            "verificationProof": t.string(),
            "isNewUser": t.boolean(),
            "expiresIn": t.string(),
            "idToken": t.string(),
            "localId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartyVerifyPhoneNumberResponseOut"])
    types["IdentitytoolkitRelyingpartySetAccountInfoRequestIn"] = t.struct(
        {
            "oobCode": t.string().optional(),
            "instanceId": t.string().optional(),
            "provider": t.array(t.string()).optional(),
            "captchaChallenge": t.string().optional(),
            "displayName": t.string().optional(),
            "password": t.string().optional(),
            "localId": t.string().optional(),
            "phoneNumber": t.string().optional(),
            "captchaResponse": t.string().optional(),
            "returnSecureToken": t.boolean().optional(),
            "customAttributes": t.string().optional(),
            "email": t.string().optional(),
            "idToken": t.string().optional(),
            "delegatedProjectNumber": t.string().optional(),
            "deleteProvider": t.array(t.string()).optional(),
            "photoUrl": t.string().optional(),
            "upgradeToFederatedLogin": t.boolean().optional(),
            "validSince": t.string().optional(),
            "deleteAttribute": t.array(t.string()).optional(),
            "createdAt": t.string().optional(),
            "lastLoginAt": t.string().optional(),
            "emailVerified": t.boolean().optional(),
            "disableUser": t.boolean().optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartySetAccountInfoRequestIn"])
    types["IdentitytoolkitRelyingpartySetAccountInfoRequestOut"] = t.struct(
        {
            "oobCode": t.string().optional(),
            "instanceId": t.string().optional(),
            "provider": t.array(t.string()).optional(),
            "captchaChallenge": t.string().optional(),
            "displayName": t.string().optional(),
            "password": t.string().optional(),
            "localId": t.string().optional(),
            "phoneNumber": t.string().optional(),
            "captchaResponse": t.string().optional(),
            "returnSecureToken": t.boolean().optional(),
            "customAttributes": t.string().optional(),
            "email": t.string().optional(),
            "idToken": t.string().optional(),
            "delegatedProjectNumber": t.string().optional(),
            "deleteProvider": t.array(t.string()).optional(),
            "photoUrl": t.string().optional(),
            "upgradeToFederatedLogin": t.boolean().optional(),
            "validSince": t.string().optional(),
            "deleteAttribute": t.array(t.string()).optional(),
            "createdAt": t.string().optional(),
            "lastLoginAt": t.string().optional(),
            "emailVerified": t.boolean().optional(),
            "disableUser": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartySetAccountInfoRequestOut"])
    types["DownloadAccountResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "users": t.array(t.proxy(renames["UserInfoIn"])).optional(),
        }
    ).named(renames["DownloadAccountResponseIn"])
    types["DownloadAccountResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "users": t.array(t.proxy(renames["UserInfoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DownloadAccountResponseOut"])
    types["IdentitytoolkitRelyingpartySignOutUserResponseIn"] = t.struct(
        {"localId": t.string().optional()}
    ).named(renames["IdentitytoolkitRelyingpartySignOutUserResponseIn"])
    types["IdentitytoolkitRelyingpartySignOutUserResponseOut"] = t.struct(
        {
            "localId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartySignOutUserResponseOut"])
    types["IdentitytoolkitRelyingpartyUploadAccountRequestIn"] = t.struct(
        {
            "signerKey": t.string().optional(),
            "allowOverwrite": t.boolean().optional(),
            "blockSize": t.integer(),
            "saltSeparator": t.string().optional(),
            "sanityCheck": t.boolean().optional(),
            "parallelization": t.integer(),
            "delegatedProjectNumber": t.string().optional(),
            "memoryCost": t.integer().optional(),
            "rounds": t.integer().optional(),
            "hashAlgorithm": t.string().optional(),
            "cpuMemCost": t.integer().optional(),
            "dkLen": t.integer(),
            "targetProjectId": t.string().optional(),
            "users": t.array(t.proxy(renames["UserInfoIn"])).optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartyUploadAccountRequestIn"])
    types["IdentitytoolkitRelyingpartyUploadAccountRequestOut"] = t.struct(
        {
            "signerKey": t.string().optional(),
            "allowOverwrite": t.boolean().optional(),
            "blockSize": t.integer(),
            "saltSeparator": t.string().optional(),
            "sanityCheck": t.boolean().optional(),
            "parallelization": t.integer(),
            "delegatedProjectNumber": t.string().optional(),
            "memoryCost": t.integer().optional(),
            "rounds": t.integer().optional(),
            "hashAlgorithm": t.string().optional(),
            "cpuMemCost": t.integer().optional(),
            "dkLen": t.integer(),
            "targetProjectId": t.string().optional(),
            "users": t.array(t.proxy(renames["UserInfoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartyUploadAccountRequestOut"])
    types["IdentitytoolkitRelyingpartySendVerificationCodeResponseIn"] = t.struct(
        {"sessionInfo": t.string().optional()}
    ).named(renames["IdentitytoolkitRelyingpartySendVerificationCodeResponseIn"])
    types["IdentitytoolkitRelyingpartySendVerificationCodeResponseOut"] = t.struct(
        {
            "sessionInfo": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartySendVerificationCodeResponseOut"])
    types["ResetPasswordResponseIn"] = t.struct(
        {
            "requestType": t.string().optional(),
            "kind": t.string().optional(),
            "email": t.string().optional(),
            "newEmail": t.string().optional(),
        }
    ).named(renames["ResetPasswordResponseIn"])
    types["ResetPasswordResponseOut"] = t.struct(
        {
            "requestType": t.string().optional(),
            "kind": t.string().optional(),
            "email": t.string().optional(),
            "newEmail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResetPasswordResponseOut"])
    types["IdentitytoolkitRelyingpartySignOutUserRequestIn"] = t.struct(
        {"localId": t.string().optional(), "instanceId": t.string().optional()}
    ).named(renames["IdentitytoolkitRelyingpartySignOutUserRequestIn"])
    types["IdentitytoolkitRelyingpartySignOutUserRequestOut"] = t.struct(
        {
            "localId": t.string().optional(),
            "instanceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartySignOutUserRequestOut"])
    types["IdentitytoolkitRelyingpartyVerifyPasswordRequestIn"] = t.struct(
        {
            "idToken": t.string().optional(),
            "captchaResponse": t.string().optional(),
            "returnSecureToken": t.boolean().optional(),
            "tenantProjectNumber": t.string().optional(),
            "instanceId": t.string().optional(),
            "pendingIdToken": t.string().optional(),
            "email": t.string().optional(),
            "tenantId": t.string().optional(),
            "delegatedProjectNumber": t.string().optional(),
            "password": t.string().optional(),
            "captchaChallenge": t.string().optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartyVerifyPasswordRequestIn"])
    types["IdentitytoolkitRelyingpartyVerifyPasswordRequestOut"] = t.struct(
        {
            "idToken": t.string().optional(),
            "captchaResponse": t.string().optional(),
            "returnSecureToken": t.boolean().optional(),
            "tenantProjectNumber": t.string().optional(),
            "instanceId": t.string().optional(),
            "pendingIdToken": t.string().optional(),
            "email": t.string().optional(),
            "tenantId": t.string().optional(),
            "delegatedProjectNumber": t.string().optional(),
            "password": t.string().optional(),
            "captchaChallenge": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartyVerifyPasswordRequestOut"])
    types["IdentitytoolkitRelyingpartyVerifyAssertionRequestIn"] = t.struct(
        {
            "idToken": t.string().optional(),
            "requestUri": t.string().optional(),
            "tenantProjectNumber": t.string().optional(),
            "instanceId": t.string().optional(),
            "postBody": t.string().optional(),
            "tenantId": t.string().optional(),
            "returnSecureToken": t.boolean().optional(),
            "returnIdpCredential": t.boolean().optional(),
            "sessionId": t.string().optional(),
            "returnRefreshToken": t.boolean().optional(),
            "delegatedProjectNumber": t.string().optional(),
            "pendingIdToken": t.string().optional(),
            "autoCreate": t.boolean().optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartyVerifyAssertionRequestIn"])
    types["IdentitytoolkitRelyingpartyVerifyAssertionRequestOut"] = t.struct(
        {
            "idToken": t.string().optional(),
            "requestUri": t.string().optional(),
            "tenantProjectNumber": t.string().optional(),
            "instanceId": t.string().optional(),
            "postBody": t.string().optional(),
            "tenantId": t.string().optional(),
            "returnSecureToken": t.boolean().optional(),
            "returnIdpCredential": t.boolean().optional(),
            "sessionId": t.string().optional(),
            "returnRefreshToken": t.boolean().optional(),
            "delegatedProjectNumber": t.string().optional(),
            "pendingIdToken": t.string().optional(),
            "autoCreate": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartyVerifyAssertionRequestOut"])
    types["IdentitytoolkitRelyingpartyVerifyPhoneNumberRequestIn"] = t.struct(
        {
            "temporaryProof": t.string(),
            "phoneNumber": t.string(),
            "sessionInfo": t.string().optional(),
            "verificationProof": t.string(),
            "idToken": t.string(),
            "code": t.string(),
            "operation": t.string(),
        }
    ).named(renames["IdentitytoolkitRelyingpartyVerifyPhoneNumberRequestIn"])
    types["IdentitytoolkitRelyingpartyVerifyPhoneNumberRequestOut"] = t.struct(
        {
            "temporaryProof": t.string(),
            "phoneNumber": t.string(),
            "sessionInfo": t.string().optional(),
            "verificationProof": t.string(),
            "idToken": t.string(),
            "code": t.string(),
            "operation": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartyVerifyPhoneNumberRequestOut"])
    types["IdentitytoolkitRelyingpartyGetProjectConfigResponseIn"] = t.struct(
        {
            "changeEmailTemplate": t.proxy(renames["EmailTemplateIn"]).optional(),
            "authorizedDomains": t.array(t.string()).optional(),
            "resetPasswordTemplate": t.proxy(renames["EmailTemplateIn"]).optional(),
            "legacyResetPasswordTemplate": t.proxy(
                renames["EmailTemplateIn"]
            ).optional(),
            "enableAnonymousUser": t.boolean().optional(),
            "idpConfig": t.array(t.proxy(renames["IdpConfigIn"])).optional(),
            "verifyEmailTemplate": t.proxy(renames["EmailTemplateIn"]).optional(),
            "useEmailSending": t.boolean().optional(),
            "dynamicLinksDomain": t.string(),
            "projectId": t.string().optional(),
            "allowPasswordUser": t.boolean().optional(),
            "apiKey": t.string().optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartyGetProjectConfigResponseIn"])
    types["IdentitytoolkitRelyingpartyGetProjectConfigResponseOut"] = t.struct(
        {
            "changeEmailTemplate": t.proxy(renames["EmailTemplateOut"]).optional(),
            "authorizedDomains": t.array(t.string()).optional(),
            "resetPasswordTemplate": t.proxy(renames["EmailTemplateOut"]).optional(),
            "legacyResetPasswordTemplate": t.proxy(
                renames["EmailTemplateOut"]
            ).optional(),
            "enableAnonymousUser": t.boolean().optional(),
            "idpConfig": t.array(t.proxy(renames["IdpConfigOut"])).optional(),
            "verifyEmailTemplate": t.proxy(renames["EmailTemplateOut"]).optional(),
            "useEmailSending": t.boolean().optional(),
            "dynamicLinksDomain": t.string(),
            "projectId": t.string().optional(),
            "allowPasswordUser": t.boolean().optional(),
            "apiKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartyGetProjectConfigResponseOut"])
    types["GetOobConfirmationCodeResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "oobCode": t.string().optional(),
            "email": t.string().optional(),
        }
    ).named(renames["GetOobConfirmationCodeResponseIn"])
    types["GetOobConfirmationCodeResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "oobCode": t.string().optional(),
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetOobConfirmationCodeResponseOut"])
    types["IdentitytoolkitRelyingpartyEmailLinkSigninRequestIn"] = t.struct(
        {
            "email": t.string().optional(),
            "oobCode": t.string().optional(),
            "idToken": t.string().optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartyEmailLinkSigninRequestIn"])
    types["IdentitytoolkitRelyingpartyEmailLinkSigninRequestOut"] = t.struct(
        {
            "email": t.string().optional(),
            "oobCode": t.string().optional(),
            "idToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartyEmailLinkSigninRequestOut"])
    types["IdpConfigIn"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "provider": t.string().optional(),
            "secret": t.string().optional(),
            "whitelistedAudiences": t.array(t.string()).optional(),
            "clientId": t.string().optional(),
            "experimentPercent": t.integer().optional(),
        }
    ).named(renames["IdpConfigIn"])
    types["IdpConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "provider": t.string().optional(),
            "secret": t.string().optional(),
            "whitelistedAudiences": t.array(t.string()).optional(),
            "clientId": t.string().optional(),
            "experimentPercent": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdpConfigOut"])
    types["GetAccountInfoResponseIn"] = t.struct(
        {
            "users": t.array(t.proxy(renames["UserInfoIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["GetAccountInfoResponseIn"])
    types["GetAccountInfoResponseOut"] = t.struct(
        {
            "users": t.array(t.proxy(renames["UserInfoOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetAccountInfoResponseOut"])
    types["DeleteAccountResponseIn"] = t.struct({"kind": t.string().optional()}).named(
        renames["DeleteAccountResponseIn"]
    )
    types["DeleteAccountResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteAccountResponseOut"])
    types["IdentitytoolkitRelyingpartySignupNewUserRequestIn"] = t.struct(
        {
            "idToken": t.string().optional(),
            "localId": t.string().optional(),
            "password": t.string().optional(),
            "displayName": t.string().optional(),
            "tenantProjectNumber": t.string().optional(),
            "photoUrl": t.string().optional(),
            "instanceId": t.string().optional(),
            "email": t.string().optional(),
            "tenantId": t.string().optional(),
            "disabled": t.boolean().optional(),
            "emailVerified": t.boolean().optional(),
            "phoneNumber": t.string().optional(),
            "captchaResponse": t.string().optional(),
            "captchaChallenge": t.string().optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartySignupNewUserRequestIn"])
    types["IdentitytoolkitRelyingpartySignupNewUserRequestOut"] = t.struct(
        {
            "idToken": t.string().optional(),
            "localId": t.string().optional(),
            "password": t.string().optional(),
            "displayName": t.string().optional(),
            "tenantProjectNumber": t.string().optional(),
            "photoUrl": t.string().optional(),
            "instanceId": t.string().optional(),
            "email": t.string().optional(),
            "tenantId": t.string().optional(),
            "disabled": t.boolean().optional(),
            "emailVerified": t.boolean().optional(),
            "phoneNumber": t.string().optional(),
            "captchaResponse": t.string().optional(),
            "captchaChallenge": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartySignupNewUserRequestOut"])
    types["IdentitytoolkitRelyingpartyCreateAuthUriRequestIn"] = t.struct(
        {
            "oauthScope": t.string().optional(),
            "authFlowType": t.string().optional(),
            "customParameter": t.struct({"_": t.string().optional()}).optional(),
            "appId": t.string().optional(),
            "clientId": t.string().optional(),
            "providerId": t.string().optional(),
            "continueUri": t.string().optional(),
            "hostedDomain": t.string().optional(),
            "tenantProjectNumber": t.string().optional(),
            "identifier": t.string().optional(),
            "openidRealm": t.string().optional(),
            "sessionId": t.string().optional(),
            "context": t.string().optional(),
            "tenantId": t.string().optional(),
            "oauthConsumerKey": t.string().optional(),
            "otaApp": t.string().optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartyCreateAuthUriRequestIn"])
    types["IdentitytoolkitRelyingpartyCreateAuthUriRequestOut"] = t.struct(
        {
            "oauthScope": t.string().optional(),
            "authFlowType": t.string().optional(),
            "customParameter": t.struct({"_": t.string().optional()}).optional(),
            "appId": t.string().optional(),
            "clientId": t.string().optional(),
            "providerId": t.string().optional(),
            "continueUri": t.string().optional(),
            "hostedDomain": t.string().optional(),
            "tenantProjectNumber": t.string().optional(),
            "identifier": t.string().optional(),
            "openidRealm": t.string().optional(),
            "sessionId": t.string().optional(),
            "context": t.string().optional(),
            "tenantId": t.string().optional(),
            "oauthConsumerKey": t.string().optional(),
            "otaApp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartyCreateAuthUriRequestOut"])
    types["VerifyPasswordResponseIn"] = t.struct(
        {
            "registered": t.boolean().optional(),
            "localId": t.string().optional(),
            "expiresIn": t.string().optional(),
            "oauthExpireIn": t.integer().optional(),
            "email": t.string().optional(),
            "oauthAuthorizationCode": t.string().optional(),
            "kind": t.string().optional(),
            "photoUrl": t.string().optional(),
            "idToken": t.string().optional(),
            "displayName": t.string().optional(),
            "oauthAccessToken": t.string().optional(),
            "refreshToken": t.string().optional(),
        }
    ).named(renames["VerifyPasswordResponseIn"])
    types["VerifyPasswordResponseOut"] = t.struct(
        {
            "registered": t.boolean().optional(),
            "localId": t.string().optional(),
            "expiresIn": t.string().optional(),
            "oauthExpireIn": t.integer().optional(),
            "email": t.string().optional(),
            "oauthAuthorizationCode": t.string().optional(),
            "kind": t.string().optional(),
            "photoUrl": t.string().optional(),
            "idToken": t.string().optional(),
            "displayName": t.string().optional(),
            "oauthAccessToken": t.string().optional(),
            "refreshToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VerifyPasswordResponseOut"])
    types["IdentitytoolkitRelyingpartyResetPasswordRequestIn"] = t.struct(
        {
            "email": t.string().optional(),
            "newPassword": t.string().optional(),
            "oobCode": t.string().optional(),
            "oldPassword": t.string().optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartyResetPasswordRequestIn"])
    types["IdentitytoolkitRelyingpartyResetPasswordRequestOut"] = t.struct(
        {
            "email": t.string().optional(),
            "newPassword": t.string().optional(),
            "oobCode": t.string().optional(),
            "oldPassword": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartyResetPasswordRequestOut"])
    types["IdentitytoolkitRelyingpartySendVerificationCodeRequestIn"] = t.struct(
        {
            "recaptchaToken": t.string().optional(),
            "iosReceipt": t.string().optional(),
            "iosSecret": t.string().optional(),
            "phoneNumber": t.string().optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartySendVerificationCodeRequestIn"])
    types["IdentitytoolkitRelyingpartySendVerificationCodeRequestOut"] = t.struct(
        {
            "recaptchaToken": t.string().optional(),
            "iosReceipt": t.string().optional(),
            "iosSecret": t.string().optional(),
            "phoneNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartySendVerificationCodeRequestOut"])
    types["CreateAuthUriResponseIn"] = t.struct(
        {
            "allProviders": t.array(t.string()).optional(),
            "kind": t.string().optional(),
            "captchaRequired": t.boolean().optional(),
            "forExistingProvider": t.boolean().optional(),
            "signinMethods": t.array(t.string()).optional(),
            "sessionId": t.string().optional(),
            "providerId": t.string().optional(),
            "registered": t.boolean().optional(),
            "authUri": t.string().optional(),
        }
    ).named(renames["CreateAuthUriResponseIn"])
    types["CreateAuthUriResponseOut"] = t.struct(
        {
            "allProviders": t.array(t.string()).optional(),
            "kind": t.string().optional(),
            "captchaRequired": t.boolean().optional(),
            "forExistingProvider": t.boolean().optional(),
            "signinMethods": t.array(t.string()).optional(),
            "sessionId": t.string().optional(),
            "providerId": t.string().optional(),
            "registered": t.boolean().optional(),
            "authUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateAuthUriResponseOut"])
    types["GetRecaptchaParamResponseIn"] = t.struct(
        {
            "recaptchaStoken": t.string().optional(),
            "recaptchaSiteKey": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["GetRecaptchaParamResponseIn"])
    types["GetRecaptchaParamResponseOut"] = t.struct(
        {
            "recaptchaStoken": t.string().optional(),
            "recaptchaSiteKey": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetRecaptchaParamResponseOut"])
    types["IdentitytoolkitRelyingpartySetProjectConfigResponseIn"] = t.struct(
        {"projectId": t.string().optional()}
    ).named(renames["IdentitytoolkitRelyingpartySetProjectConfigResponseIn"])
    types["IdentitytoolkitRelyingpartySetProjectConfigResponseOut"] = t.struct(
        {
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartySetProjectConfigResponseOut"])
    types["IdentitytoolkitRelyingpartyDownloadAccountRequestIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "targetProjectId": t.string().optional(),
            "maxResults": t.integer().optional(),
            "delegatedProjectNumber": t.string().optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartyDownloadAccountRequestIn"])
    types["IdentitytoolkitRelyingpartyDownloadAccountRequestOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "targetProjectId": t.string().optional(),
            "maxResults": t.integer().optional(),
            "delegatedProjectNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartyDownloadAccountRequestOut"])
    types["EmailTemplateIn"] = t.struct(
        {
            "replyTo": t.string().optional(),
            "format": t.string().optional(),
            "body": t.string().optional(),
            "from": t.string().optional(),
            "fromDisplayName": t.string().optional(),
            "subject": t.string().optional(),
        }
    ).named(renames["EmailTemplateIn"])
    types["EmailTemplateOut"] = t.struct(
        {
            "replyTo": t.string().optional(),
            "format": t.string().optional(),
            "body": t.string().optional(),
            "from": t.string().optional(),
            "fromDisplayName": t.string().optional(),
            "subject": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EmailTemplateOut"])
    types["UserInfoIn"] = t.struct(
        {
            "photoUrl": t.string().optional(),
            "passwordUpdatedAt": t.number().optional(),
            "rawPassword": t.string().optional(),
            "screenName": t.string().optional(),
            "createdAt": t.string().optional(),
            "email": t.string().optional(),
            "displayName": t.string().optional(),
            "providerUserInfo": t.array(
                t.struct(
                    {
                        "photoUrl": t.string().optional(),
                        "rawId": t.string().optional(),
                        "phoneNumber": t.string().optional(),
                        "federatedId": t.string().optional(),
                        "email": t.string().optional(),
                        "displayName": t.string().optional(),
                        "screenName": t.string().optional(),
                        "providerId": t.string().optional(),
                    }
                )
            ).optional(),
            "validSince": t.string().optional(),
            "emailVerified": t.boolean().optional(),
            "salt": t.string().optional(),
            "localId": t.string().optional(),
            "lastLoginAt": t.string().optional(),
            "phoneNumber": t.string().optional(),
            "customAttributes": t.string().optional(),
            "passwordHash": t.string().optional(),
            "version": t.integer().optional(),
            "customAuth": t.boolean().optional(),
            "disabled": t.boolean().optional(),
        }
    ).named(renames["UserInfoIn"])
    types["UserInfoOut"] = t.struct(
        {
            "photoUrl": t.string().optional(),
            "passwordUpdatedAt": t.number().optional(),
            "rawPassword": t.string().optional(),
            "screenName": t.string().optional(),
            "createdAt": t.string().optional(),
            "email": t.string().optional(),
            "displayName": t.string().optional(),
            "providerUserInfo": t.array(
                t.struct(
                    {
                        "photoUrl": t.string().optional(),
                        "rawId": t.string().optional(),
                        "phoneNumber": t.string().optional(),
                        "federatedId": t.string().optional(),
                        "email": t.string().optional(),
                        "displayName": t.string().optional(),
                        "screenName": t.string().optional(),
                        "providerId": t.string().optional(),
                    }
                )
            ).optional(),
            "validSince": t.string().optional(),
            "emailVerified": t.boolean().optional(),
            "salt": t.string().optional(),
            "localId": t.string().optional(),
            "lastLoginAt": t.string().optional(),
            "phoneNumber": t.string().optional(),
            "customAttributes": t.string().optional(),
            "passwordHash": t.string().optional(),
            "version": t.integer().optional(),
            "customAuth": t.boolean().optional(),
            "disabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserInfoOut"])
    types["IdentitytoolkitRelyingpartySetProjectConfigRequestIn"] = t.struct(
        {
            "resetPasswordTemplate": t.proxy(renames["EmailTemplateIn"]).optional(),
            "verifyEmailTemplate": t.proxy(renames["EmailTemplateIn"]).optional(),
            "apiKey": t.string().optional(),
            "delegatedProjectNumber": t.string().optional(),
            "enableAnonymousUser": t.boolean().optional(),
            "authorizedDomains": t.array(t.string()).optional(),
            "idpConfig": t.array(t.proxy(renames["IdpConfigIn"])).optional(),
            "changeEmailTemplate": t.proxy(renames["EmailTemplateIn"]).optional(),
            "legacyResetPasswordTemplate": t.proxy(
                renames["EmailTemplateIn"]
            ).optional(),
            "allowPasswordUser": t.boolean().optional(),
            "useEmailSending": t.boolean().optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartySetProjectConfigRequestIn"])
    types["IdentitytoolkitRelyingpartySetProjectConfigRequestOut"] = t.struct(
        {
            "resetPasswordTemplate": t.proxy(renames["EmailTemplateOut"]).optional(),
            "verifyEmailTemplate": t.proxy(renames["EmailTemplateOut"]).optional(),
            "apiKey": t.string().optional(),
            "delegatedProjectNumber": t.string().optional(),
            "enableAnonymousUser": t.boolean().optional(),
            "authorizedDomains": t.array(t.string()).optional(),
            "idpConfig": t.array(t.proxy(renames["IdpConfigOut"])).optional(),
            "changeEmailTemplate": t.proxy(renames["EmailTemplateOut"]).optional(),
            "legacyResetPasswordTemplate": t.proxy(
                renames["EmailTemplateOut"]
            ).optional(),
            "allowPasswordUser": t.boolean().optional(),
            "useEmailSending": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartySetProjectConfigRequestOut"])
    types["IdentitytoolkitRelyingpartyVerifyCustomTokenRequestIn"] = t.struct(
        {
            "token": t.string().optional(),
            "delegatedProjectNumber": t.string().optional(),
            "instanceId": t.string().optional(),
            "returnSecureToken": t.boolean().optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartyVerifyCustomTokenRequestIn"])
    types["IdentitytoolkitRelyingpartyVerifyCustomTokenRequestOut"] = t.struct(
        {
            "token": t.string().optional(),
            "delegatedProjectNumber": t.string().optional(),
            "instanceId": t.string().optional(),
            "returnSecureToken": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartyVerifyCustomTokenRequestOut"])
    types["EmailLinkSigninResponseIn"] = t.struct(
        {
            "expiresIn": t.string().optional(),
            "refreshToken": t.string().optional(),
            "isNewUser": t.boolean().optional(),
            "localId": t.string().optional(),
            "email": t.string().optional(),
            "kind": t.string().optional(),
            "idToken": t.string().optional(),
        }
    ).named(renames["EmailLinkSigninResponseIn"])
    types["EmailLinkSigninResponseOut"] = t.struct(
        {
            "expiresIn": t.string().optional(),
            "refreshToken": t.string().optional(),
            "isNewUser": t.boolean().optional(),
            "localId": t.string().optional(),
            "email": t.string().optional(),
            "kind": t.string().optional(),
            "idToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EmailLinkSigninResponseOut"])
    types["IdentitytoolkitRelyingpartyDeleteAccountRequestIn"] = t.struct(
        {
            "localId": t.string().optional(),
            "delegatedProjectNumber": t.string().optional(),
            "idToken": t.string().optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartyDeleteAccountRequestIn"])
    types["IdentitytoolkitRelyingpartyDeleteAccountRequestOut"] = t.struct(
        {
            "localId": t.string().optional(),
            "delegatedProjectNumber": t.string().optional(),
            "idToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartyDeleteAccountRequestOut"])
    types["RelyingpartyIn"] = t.struct(
        {
            "userIp": t.string().optional(),
            "newEmail": t.string().optional(),
            "androidInstallApp": t.boolean().optional(),
            "androidPackageName": t.string().optional(),
            "challenge": t.string().optional(),
            "kind": t.string().optional(),
            "iOSAppStoreId": t.string().optional(),
            "captchaResp": t.string().optional(),
            "idToken": t.string().optional(),
            "canHandleCodeInApp": t.boolean().optional(),
            "androidMinimumVersion": t.string().optional(),
            "iOSBundleId": t.string().optional(),
            "continueUrl": t.string().optional(),
            "requestType": t.string().optional(),
            "email": t.string().optional(),
        }
    ).named(renames["RelyingpartyIn"])
    types["RelyingpartyOut"] = t.struct(
        {
            "userIp": t.string().optional(),
            "newEmail": t.string().optional(),
            "androidInstallApp": t.boolean().optional(),
            "androidPackageName": t.string().optional(),
            "challenge": t.string().optional(),
            "kind": t.string().optional(),
            "iOSAppStoreId": t.string().optional(),
            "captchaResp": t.string().optional(),
            "idToken": t.string().optional(),
            "canHandleCodeInApp": t.boolean().optional(),
            "androidMinimumVersion": t.string().optional(),
            "iOSBundleId": t.string().optional(),
            "continueUrl": t.string().optional(),
            "requestType": t.string().optional(),
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RelyingpartyOut"])
    types["VerifyAssertionResponseIn"] = t.struct(
        {
            "rawUserInfo": t.string().optional(),
            "isNewUser": t.boolean().optional(),
            "nickName": t.string().optional(),
            "appScheme": t.string().optional(),
            "displayName": t.string().optional(),
            "dateOfBirth": t.string().optional(),
            "oauthIdToken": t.string().optional(),
            "expiresIn": t.string().optional(),
            "oauthExpireIn": t.integer().optional(),
            "needConfirmation": t.boolean().optional(),
            "context": t.string().optional(),
            "providerId": t.string().optional(),
            "oauthAuthorizationCode": t.string().optional(),
            "language": t.string().optional(),
            "oauthAccessToken": t.string().optional(),
            "federatedId": t.string().optional(),
            "inputEmail": t.string().optional(),
            "action": t.string().optional(),
            "verifiedProvider": t.array(t.string()).optional(),
            "kind": t.string().optional(),
            "lastName": t.string().optional(),
            "oauthRequestToken": t.string().optional(),
            "emailRecycled": t.boolean().optional(),
            "screenName": t.string().optional(),
            "timeZone": t.string().optional(),
            "needEmail": t.boolean().optional(),
            "errorMessage": t.string().optional(),
            "idToken": t.string().optional(),
            "oauthScope": t.string().optional(),
            "firstName": t.string().optional(),
            "oauthTokenSecret": t.string().optional(),
            "photoUrl": t.string().optional(),
            "emailVerified": t.boolean().optional(),
            "email": t.string().optional(),
            "refreshToken": t.string().optional(),
            "localId": t.string().optional(),
            "originalEmail": t.string().optional(),
            "fullName": t.string().optional(),
            "appInstallationUrl": t.string().optional(),
        }
    ).named(renames["VerifyAssertionResponseIn"])
    types["VerifyAssertionResponseOut"] = t.struct(
        {
            "rawUserInfo": t.string().optional(),
            "isNewUser": t.boolean().optional(),
            "nickName": t.string().optional(),
            "appScheme": t.string().optional(),
            "displayName": t.string().optional(),
            "dateOfBirth": t.string().optional(),
            "oauthIdToken": t.string().optional(),
            "expiresIn": t.string().optional(),
            "oauthExpireIn": t.integer().optional(),
            "needConfirmation": t.boolean().optional(),
            "context": t.string().optional(),
            "providerId": t.string().optional(),
            "oauthAuthorizationCode": t.string().optional(),
            "language": t.string().optional(),
            "oauthAccessToken": t.string().optional(),
            "federatedId": t.string().optional(),
            "inputEmail": t.string().optional(),
            "action": t.string().optional(),
            "verifiedProvider": t.array(t.string()).optional(),
            "kind": t.string().optional(),
            "lastName": t.string().optional(),
            "oauthRequestToken": t.string().optional(),
            "emailRecycled": t.boolean().optional(),
            "screenName": t.string().optional(),
            "timeZone": t.string().optional(),
            "needEmail": t.boolean().optional(),
            "errorMessage": t.string().optional(),
            "idToken": t.string().optional(),
            "oauthScope": t.string().optional(),
            "firstName": t.string().optional(),
            "oauthTokenSecret": t.string().optional(),
            "photoUrl": t.string().optional(),
            "emailVerified": t.boolean().optional(),
            "email": t.string().optional(),
            "refreshToken": t.string().optional(),
            "localId": t.string().optional(),
            "originalEmail": t.string().optional(),
            "fullName": t.string().optional(),
            "appInstallationUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VerifyAssertionResponseOut"])
    types["UploadAccountResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "error": t.array(
                t.struct(
                    {"index": t.integer().optional(), "message": t.string().optional()}
                )
            ).optional(),
        }
    ).named(renames["UploadAccountResponseIn"])
    types["UploadAccountResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UploadAccountResponseOut"])

    functions = {}
    functions["relyingpartyEmailLinkSignin"] = identitytoolkit.post(
        "getAccountInfo",
        t.struct(
            {
                "idToken": t.string().optional(),
                "phoneNumber": t.array(t.string()).optional(),
                "delegatedProjectNumber": t.string().optional(),
                "email": t.array(t.string()).optional(),
                "localId": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetAccountInfoResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["relyingpartyGetOobConfirmationCode"] = identitytoolkit.post(
        "getAccountInfo",
        t.struct(
            {
                "idToken": t.string().optional(),
                "phoneNumber": t.array(t.string()).optional(),
                "delegatedProjectNumber": t.string().optional(),
                "email": t.array(t.string()).optional(),
                "localId": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetAccountInfoResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["relyingpartyVerifyAssertion"] = identitytoolkit.post(
        "getAccountInfo",
        t.struct(
            {
                "idToken": t.string().optional(),
                "phoneNumber": t.array(t.string()).optional(),
                "delegatedProjectNumber": t.string().optional(),
                "email": t.array(t.string()).optional(),
                "localId": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetAccountInfoResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["relyingpartyDeleteAccount"] = identitytoolkit.post(
        "getAccountInfo",
        t.struct(
            {
                "idToken": t.string().optional(),
                "phoneNumber": t.array(t.string()).optional(),
                "delegatedProjectNumber": t.string().optional(),
                "email": t.array(t.string()).optional(),
                "localId": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetAccountInfoResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["relyingpartyVerifyPassword"] = identitytoolkit.post(
        "getAccountInfo",
        t.struct(
            {
                "idToken": t.string().optional(),
                "phoneNumber": t.array(t.string()).optional(),
                "delegatedProjectNumber": t.string().optional(),
                "email": t.array(t.string()).optional(),
                "localId": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetAccountInfoResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["relyingpartyGetRecaptchaParam"] = identitytoolkit.post(
        "getAccountInfo",
        t.struct(
            {
                "idToken": t.string().optional(),
                "phoneNumber": t.array(t.string()).optional(),
                "delegatedProjectNumber": t.string().optional(),
                "email": t.array(t.string()).optional(),
                "localId": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetAccountInfoResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["relyingpartyCreateAuthUri"] = identitytoolkit.post(
        "getAccountInfo",
        t.struct(
            {
                "idToken": t.string().optional(),
                "phoneNumber": t.array(t.string()).optional(),
                "delegatedProjectNumber": t.string().optional(),
                "email": t.array(t.string()).optional(),
                "localId": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetAccountInfoResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["relyingpartyVerifyCustomToken"] = identitytoolkit.post(
        "getAccountInfo",
        t.struct(
            {
                "idToken": t.string().optional(),
                "phoneNumber": t.array(t.string()).optional(),
                "delegatedProjectNumber": t.string().optional(),
                "email": t.array(t.string()).optional(),
                "localId": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetAccountInfoResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["relyingpartyVerifyPhoneNumber"] = identitytoolkit.post(
        "getAccountInfo",
        t.struct(
            {
                "idToken": t.string().optional(),
                "phoneNumber": t.array(t.string()).optional(),
                "delegatedProjectNumber": t.string().optional(),
                "email": t.array(t.string()).optional(),
                "localId": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetAccountInfoResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["relyingpartySetProjectConfig"] = identitytoolkit.post(
        "getAccountInfo",
        t.struct(
            {
                "idToken": t.string().optional(),
                "phoneNumber": t.array(t.string()).optional(),
                "delegatedProjectNumber": t.string().optional(),
                "email": t.array(t.string()).optional(),
                "localId": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetAccountInfoResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["relyingpartyDownloadAccount"] = identitytoolkit.post(
        "getAccountInfo",
        t.struct(
            {
                "idToken": t.string().optional(),
                "phoneNumber": t.array(t.string()).optional(),
                "delegatedProjectNumber": t.string().optional(),
                "email": t.array(t.string()).optional(),
                "localId": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetAccountInfoResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["relyingpartyUploadAccount"] = identitytoolkit.post(
        "getAccountInfo",
        t.struct(
            {
                "idToken": t.string().optional(),
                "phoneNumber": t.array(t.string()).optional(),
                "delegatedProjectNumber": t.string().optional(),
                "email": t.array(t.string()).optional(),
                "localId": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetAccountInfoResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["relyingpartyResetPassword"] = identitytoolkit.post(
        "getAccountInfo",
        t.struct(
            {
                "idToken": t.string().optional(),
                "phoneNumber": t.array(t.string()).optional(),
                "delegatedProjectNumber": t.string().optional(),
                "email": t.array(t.string()).optional(),
                "localId": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetAccountInfoResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["relyingpartySignOutUser"] = identitytoolkit.post(
        "getAccountInfo",
        t.struct(
            {
                "idToken": t.string().optional(),
                "phoneNumber": t.array(t.string()).optional(),
                "delegatedProjectNumber": t.string().optional(),
                "email": t.array(t.string()).optional(),
                "localId": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetAccountInfoResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["relyingpartySignupNewUser"] = identitytoolkit.post(
        "getAccountInfo",
        t.struct(
            {
                "idToken": t.string().optional(),
                "phoneNumber": t.array(t.string()).optional(),
                "delegatedProjectNumber": t.string().optional(),
                "email": t.array(t.string()).optional(),
                "localId": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetAccountInfoResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["relyingpartySendVerificationCode"] = identitytoolkit.post(
        "getAccountInfo",
        t.struct(
            {
                "idToken": t.string().optional(),
                "phoneNumber": t.array(t.string()).optional(),
                "delegatedProjectNumber": t.string().optional(),
                "email": t.array(t.string()).optional(),
                "localId": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetAccountInfoResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["relyingpartyGetProjectConfig"] = identitytoolkit.post(
        "getAccountInfo",
        t.struct(
            {
                "idToken": t.string().optional(),
                "phoneNumber": t.array(t.string()).optional(),
                "delegatedProjectNumber": t.string().optional(),
                "email": t.array(t.string()).optional(),
                "localId": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetAccountInfoResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["relyingpartySetAccountInfo"] = identitytoolkit.post(
        "getAccountInfo",
        t.struct(
            {
                "idToken": t.string().optional(),
                "phoneNumber": t.array(t.string()).optional(),
                "delegatedProjectNumber": t.string().optional(),
                "email": t.array(t.string()).optional(),
                "localId": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetAccountInfoResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["relyingpartyGetPublicKeys"] = identitytoolkit.post(
        "getAccountInfo",
        t.struct(
            {
                "idToken": t.string().optional(),
                "phoneNumber": t.array(t.string()).optional(),
                "delegatedProjectNumber": t.string().optional(),
                "email": t.array(t.string()).optional(),
                "localId": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetAccountInfoResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["relyingpartyGetAccountInfo"] = identitytoolkit.post(
        "getAccountInfo",
        t.struct(
            {
                "idToken": t.string().optional(),
                "phoneNumber": t.array(t.string()).optional(),
                "delegatedProjectNumber": t.string().optional(),
                "email": t.array(t.string()).optional(),
                "localId": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetAccountInfoResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="identitytoolkit",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
