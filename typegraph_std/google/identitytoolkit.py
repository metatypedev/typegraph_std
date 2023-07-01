from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_identitytoolkit():
    identitytoolkit = HTTPRuntime("https://www.googleapis.com/")

    renames = {
        "ErrorResponse": "_identitytoolkit_1_ErrorResponse",
        "EmailTemplateIn": "_identitytoolkit_2_EmailTemplateIn",
        "EmailTemplateOut": "_identitytoolkit_3_EmailTemplateOut",
        "IdentitytoolkitRelyingpartySendVerificationCodeRequestIn": "_identitytoolkit_4_IdentitytoolkitRelyingpartySendVerificationCodeRequestIn",
        "IdentitytoolkitRelyingpartySendVerificationCodeRequestOut": "_identitytoolkit_5_IdentitytoolkitRelyingpartySendVerificationCodeRequestOut",
        "DeleteAccountResponseIn": "_identitytoolkit_6_DeleteAccountResponseIn",
        "DeleteAccountResponseOut": "_identitytoolkit_7_DeleteAccountResponseOut",
        "IdpConfigIn": "_identitytoolkit_8_IdpConfigIn",
        "IdpConfigOut": "_identitytoolkit_9_IdpConfigOut",
        "GetRecaptchaParamResponseIn": "_identitytoolkit_10_GetRecaptchaParamResponseIn",
        "GetRecaptchaParamResponseOut": "_identitytoolkit_11_GetRecaptchaParamResponseOut",
        "GetOobConfirmationCodeResponseIn": "_identitytoolkit_12_GetOobConfirmationCodeResponseIn",
        "GetOobConfirmationCodeResponseOut": "_identitytoolkit_13_GetOobConfirmationCodeResponseOut",
        "UserInfoIn": "_identitytoolkit_14_UserInfoIn",
        "UserInfoOut": "_identitytoolkit_15_UserInfoOut",
        "IdentitytoolkitRelyingpartySetProjectConfigRequestIn": "_identitytoolkit_16_IdentitytoolkitRelyingpartySetProjectConfigRequestIn",
        "IdentitytoolkitRelyingpartySetProjectConfigRequestOut": "_identitytoolkit_17_IdentitytoolkitRelyingpartySetProjectConfigRequestOut",
        "GetAccountInfoResponseIn": "_identitytoolkit_18_GetAccountInfoResponseIn",
        "GetAccountInfoResponseOut": "_identitytoolkit_19_GetAccountInfoResponseOut",
        "IdentitytoolkitRelyingpartyDownloadAccountRequestIn": "_identitytoolkit_20_IdentitytoolkitRelyingpartyDownloadAccountRequestIn",
        "IdentitytoolkitRelyingpartyDownloadAccountRequestOut": "_identitytoolkit_21_IdentitytoolkitRelyingpartyDownloadAccountRequestOut",
        "IdentitytoolkitRelyingpartyVerifyPhoneNumberRequestIn": "_identitytoolkit_22_IdentitytoolkitRelyingpartyVerifyPhoneNumberRequestIn",
        "IdentitytoolkitRelyingpartyVerifyPhoneNumberRequestOut": "_identitytoolkit_23_IdentitytoolkitRelyingpartyVerifyPhoneNumberRequestOut",
        "ResetPasswordResponseIn": "_identitytoolkit_24_ResetPasswordResponseIn",
        "ResetPasswordResponseOut": "_identitytoolkit_25_ResetPasswordResponseOut",
        "IdentitytoolkitRelyingpartyVerifyCustomTokenRequestIn": "_identitytoolkit_26_IdentitytoolkitRelyingpartyVerifyCustomTokenRequestIn",
        "IdentitytoolkitRelyingpartyVerifyCustomTokenRequestOut": "_identitytoolkit_27_IdentitytoolkitRelyingpartyVerifyCustomTokenRequestOut",
        "SignupNewUserResponseIn": "_identitytoolkit_28_SignupNewUserResponseIn",
        "SignupNewUserResponseOut": "_identitytoolkit_29_SignupNewUserResponseOut",
        "RelyingpartyIn": "_identitytoolkit_30_RelyingpartyIn",
        "RelyingpartyOut": "_identitytoolkit_31_RelyingpartyOut",
        "IdentitytoolkitRelyingpartySignOutUserResponseIn": "_identitytoolkit_32_IdentitytoolkitRelyingpartySignOutUserResponseIn",
        "IdentitytoolkitRelyingpartySignOutUserResponseOut": "_identitytoolkit_33_IdentitytoolkitRelyingpartySignOutUserResponseOut",
        "IdentitytoolkitRelyingpartyResetPasswordRequestIn": "_identitytoolkit_34_IdentitytoolkitRelyingpartyResetPasswordRequestIn",
        "IdentitytoolkitRelyingpartyResetPasswordRequestOut": "_identitytoolkit_35_IdentitytoolkitRelyingpartyResetPasswordRequestOut",
        "IdentitytoolkitRelyingpartyVerifyPhoneNumberResponseIn": "_identitytoolkit_36_IdentitytoolkitRelyingpartyVerifyPhoneNumberResponseIn",
        "IdentitytoolkitRelyingpartyVerifyPhoneNumberResponseOut": "_identitytoolkit_37_IdentitytoolkitRelyingpartyVerifyPhoneNumberResponseOut",
        "VerifyAssertionResponseIn": "_identitytoolkit_38_VerifyAssertionResponseIn",
        "VerifyAssertionResponseOut": "_identitytoolkit_39_VerifyAssertionResponseOut",
        "VerifyPasswordResponseIn": "_identitytoolkit_40_VerifyPasswordResponseIn",
        "VerifyPasswordResponseOut": "_identitytoolkit_41_VerifyPasswordResponseOut",
        "IdentitytoolkitRelyingpartyGetProjectConfigResponseIn": "_identitytoolkit_42_IdentitytoolkitRelyingpartyGetProjectConfigResponseIn",
        "IdentitytoolkitRelyingpartyGetProjectConfigResponseOut": "_identitytoolkit_43_IdentitytoolkitRelyingpartyGetProjectConfigResponseOut",
        "IdentitytoolkitRelyingpartySignupNewUserRequestIn": "_identitytoolkit_44_IdentitytoolkitRelyingpartySignupNewUserRequestIn",
        "IdentitytoolkitRelyingpartySignupNewUserRequestOut": "_identitytoolkit_45_IdentitytoolkitRelyingpartySignupNewUserRequestOut",
        "UploadAccountResponseIn": "_identitytoolkit_46_UploadAccountResponseIn",
        "UploadAccountResponseOut": "_identitytoolkit_47_UploadAccountResponseOut",
        "VerifyCustomTokenResponseIn": "_identitytoolkit_48_VerifyCustomTokenResponseIn",
        "VerifyCustomTokenResponseOut": "_identitytoolkit_49_VerifyCustomTokenResponseOut",
        "DownloadAccountResponseIn": "_identitytoolkit_50_DownloadAccountResponseIn",
        "DownloadAccountResponseOut": "_identitytoolkit_51_DownloadAccountResponseOut",
        "IdentitytoolkitRelyingpartyGetPublicKeysResponseIn": "_identitytoolkit_52_IdentitytoolkitRelyingpartyGetPublicKeysResponseIn",
        "IdentitytoolkitRelyingpartyGetPublicKeysResponseOut": "_identitytoolkit_53_IdentitytoolkitRelyingpartyGetPublicKeysResponseOut",
        "IdentitytoolkitRelyingpartyCreateAuthUriRequestIn": "_identitytoolkit_54_IdentitytoolkitRelyingpartyCreateAuthUriRequestIn",
        "IdentitytoolkitRelyingpartyCreateAuthUriRequestOut": "_identitytoolkit_55_IdentitytoolkitRelyingpartyCreateAuthUriRequestOut",
        "EmailLinkSigninResponseIn": "_identitytoolkit_56_EmailLinkSigninResponseIn",
        "EmailLinkSigninResponseOut": "_identitytoolkit_57_EmailLinkSigninResponseOut",
        "IdentitytoolkitRelyingpartySetAccountInfoRequestIn": "_identitytoolkit_58_IdentitytoolkitRelyingpartySetAccountInfoRequestIn",
        "IdentitytoolkitRelyingpartySetAccountInfoRequestOut": "_identitytoolkit_59_IdentitytoolkitRelyingpartySetAccountInfoRequestOut",
        "IdentitytoolkitRelyingpartySignOutUserRequestIn": "_identitytoolkit_60_IdentitytoolkitRelyingpartySignOutUserRequestIn",
        "IdentitytoolkitRelyingpartySignOutUserRequestOut": "_identitytoolkit_61_IdentitytoolkitRelyingpartySignOutUserRequestOut",
        "IdentitytoolkitRelyingpartySetProjectConfigResponseIn": "_identitytoolkit_62_IdentitytoolkitRelyingpartySetProjectConfigResponseIn",
        "IdentitytoolkitRelyingpartySetProjectConfigResponseOut": "_identitytoolkit_63_IdentitytoolkitRelyingpartySetProjectConfigResponseOut",
        "IdentitytoolkitRelyingpartyEmailLinkSigninRequestIn": "_identitytoolkit_64_IdentitytoolkitRelyingpartyEmailLinkSigninRequestIn",
        "IdentitytoolkitRelyingpartyEmailLinkSigninRequestOut": "_identitytoolkit_65_IdentitytoolkitRelyingpartyEmailLinkSigninRequestOut",
        "IdentitytoolkitRelyingpartyDeleteAccountRequestIn": "_identitytoolkit_66_IdentitytoolkitRelyingpartyDeleteAccountRequestIn",
        "IdentitytoolkitRelyingpartyDeleteAccountRequestOut": "_identitytoolkit_67_IdentitytoolkitRelyingpartyDeleteAccountRequestOut",
        "CreateAuthUriResponseIn": "_identitytoolkit_68_CreateAuthUriResponseIn",
        "CreateAuthUriResponseOut": "_identitytoolkit_69_CreateAuthUriResponseOut",
        "SetAccountInfoResponseIn": "_identitytoolkit_70_SetAccountInfoResponseIn",
        "SetAccountInfoResponseOut": "_identitytoolkit_71_SetAccountInfoResponseOut",
        "IdentitytoolkitRelyingpartyGetAccountInfoRequestIn": "_identitytoolkit_72_IdentitytoolkitRelyingpartyGetAccountInfoRequestIn",
        "IdentitytoolkitRelyingpartyGetAccountInfoRequestOut": "_identitytoolkit_73_IdentitytoolkitRelyingpartyGetAccountInfoRequestOut",
        "IdentitytoolkitRelyingpartySendVerificationCodeResponseIn": "_identitytoolkit_74_IdentitytoolkitRelyingpartySendVerificationCodeResponseIn",
        "IdentitytoolkitRelyingpartySendVerificationCodeResponseOut": "_identitytoolkit_75_IdentitytoolkitRelyingpartySendVerificationCodeResponseOut",
        "IdentitytoolkitRelyingpartyUploadAccountRequestIn": "_identitytoolkit_76_IdentitytoolkitRelyingpartyUploadAccountRequestIn",
        "IdentitytoolkitRelyingpartyUploadAccountRequestOut": "_identitytoolkit_77_IdentitytoolkitRelyingpartyUploadAccountRequestOut",
        "IdentitytoolkitRelyingpartyVerifyPasswordRequestIn": "_identitytoolkit_78_IdentitytoolkitRelyingpartyVerifyPasswordRequestIn",
        "IdentitytoolkitRelyingpartyVerifyPasswordRequestOut": "_identitytoolkit_79_IdentitytoolkitRelyingpartyVerifyPasswordRequestOut",
        "IdentitytoolkitRelyingpartyVerifyAssertionRequestIn": "_identitytoolkit_80_IdentitytoolkitRelyingpartyVerifyAssertionRequestIn",
        "IdentitytoolkitRelyingpartyVerifyAssertionRequestOut": "_identitytoolkit_81_IdentitytoolkitRelyingpartyVerifyAssertionRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["EmailTemplateIn"] = t.struct(
        {
            "fromDisplayName": t.string().optional(),
            "from": t.string().optional(),
            "replyTo": t.string().optional(),
            "format": t.string().optional(),
            "subject": t.string().optional(),
            "body": t.string().optional(),
        }
    ).named(renames["EmailTemplateIn"])
    types["EmailTemplateOut"] = t.struct(
        {
            "fromDisplayName": t.string().optional(),
            "from": t.string().optional(),
            "replyTo": t.string().optional(),
            "format": t.string().optional(),
            "subject": t.string().optional(),
            "body": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EmailTemplateOut"])
    types["IdentitytoolkitRelyingpartySendVerificationCodeRequestIn"] = t.struct(
        {
            "iosReceipt": t.string().optional(),
            "recaptchaToken": t.string().optional(),
            "iosSecret": t.string().optional(),
            "phoneNumber": t.string().optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartySendVerificationCodeRequestIn"])
    types["IdentitytoolkitRelyingpartySendVerificationCodeRequestOut"] = t.struct(
        {
            "iosReceipt": t.string().optional(),
            "recaptchaToken": t.string().optional(),
            "iosSecret": t.string().optional(),
            "phoneNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartySendVerificationCodeRequestOut"])
    types["DeleteAccountResponseIn"] = t.struct({"kind": t.string().optional()}).named(
        renames["DeleteAccountResponseIn"]
    )
    types["DeleteAccountResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteAccountResponseOut"])
    types["IdpConfigIn"] = t.struct(
        {
            "whitelistedAudiences": t.array(t.string()).optional(),
            "clientId": t.string().optional(),
            "provider": t.string().optional(),
            "experimentPercent": t.integer().optional(),
            "enabled": t.boolean().optional(),
            "secret": t.string().optional(),
        }
    ).named(renames["IdpConfigIn"])
    types["IdpConfigOut"] = t.struct(
        {
            "whitelistedAudiences": t.array(t.string()).optional(),
            "clientId": t.string().optional(),
            "provider": t.string().optional(),
            "experimentPercent": t.integer().optional(),
            "enabled": t.boolean().optional(),
            "secret": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdpConfigOut"])
    types["GetRecaptchaParamResponseIn"] = t.struct(
        {
            "recaptchaSiteKey": t.string().optional(),
            "recaptchaStoken": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["GetRecaptchaParamResponseIn"])
    types["GetRecaptchaParamResponseOut"] = t.struct(
        {
            "recaptchaSiteKey": t.string().optional(),
            "recaptchaStoken": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetRecaptchaParamResponseOut"])
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
    types["UserInfoIn"] = t.struct(
        {
            "passwordHash": t.string().optional(),
            "passwordUpdatedAt": t.number().optional(),
            "phoneNumber": t.string().optional(),
            "rawPassword": t.string().optional(),
            "version": t.integer().optional(),
            "displayName": t.string().optional(),
            "customAttributes": t.string().optional(),
            "photoUrl": t.string().optional(),
            "screenName": t.string().optional(),
            "disabled": t.boolean().optional(),
            "customAuth": t.boolean().optional(),
            "providerUserInfo": t.array(
                t.struct(
                    {
                        "photoUrl": t.string().optional(),
                        "providerId": t.string().optional(),
                        "screenName": t.string().optional(),
                        "rawId": t.string().optional(),
                        "phoneNumber": t.string().optional(),
                        "email": t.string().optional(),
                        "federatedId": t.string().optional(),
                        "displayName": t.string().optional(),
                    }
                )
            ).optional(),
            "lastLoginAt": t.string().optional(),
            "salt": t.string().optional(),
            "email": t.string().optional(),
            "localId": t.string().optional(),
            "emailVerified": t.boolean().optional(),
            "validSince": t.string().optional(),
            "createdAt": t.string().optional(),
        }
    ).named(renames["UserInfoIn"])
    types["UserInfoOut"] = t.struct(
        {
            "passwordHash": t.string().optional(),
            "passwordUpdatedAt": t.number().optional(),
            "phoneNumber": t.string().optional(),
            "rawPassword": t.string().optional(),
            "version": t.integer().optional(),
            "displayName": t.string().optional(),
            "customAttributes": t.string().optional(),
            "photoUrl": t.string().optional(),
            "screenName": t.string().optional(),
            "disabled": t.boolean().optional(),
            "customAuth": t.boolean().optional(),
            "providerUserInfo": t.array(
                t.struct(
                    {
                        "photoUrl": t.string().optional(),
                        "providerId": t.string().optional(),
                        "screenName": t.string().optional(),
                        "rawId": t.string().optional(),
                        "phoneNumber": t.string().optional(),
                        "email": t.string().optional(),
                        "federatedId": t.string().optional(),
                        "displayName": t.string().optional(),
                    }
                )
            ).optional(),
            "lastLoginAt": t.string().optional(),
            "salt": t.string().optional(),
            "email": t.string().optional(),
            "localId": t.string().optional(),
            "emailVerified": t.boolean().optional(),
            "validSince": t.string().optional(),
            "createdAt": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserInfoOut"])
    types["IdentitytoolkitRelyingpartySetProjectConfigRequestIn"] = t.struct(
        {
            "authorizedDomains": t.array(t.string()).optional(),
            "changeEmailTemplate": t.proxy(renames["EmailTemplateIn"]).optional(),
            "apiKey": t.string().optional(),
            "delegatedProjectNumber": t.string().optional(),
            "legacyResetPasswordTemplate": t.proxy(
                renames["EmailTemplateIn"]
            ).optional(),
            "resetPasswordTemplate": t.proxy(renames["EmailTemplateIn"]).optional(),
            "enableAnonymousUser": t.boolean().optional(),
            "idpConfig": t.array(t.proxy(renames["IdpConfigIn"])).optional(),
            "verifyEmailTemplate": t.proxy(renames["EmailTemplateIn"]).optional(),
            "allowPasswordUser": t.boolean().optional(),
            "useEmailSending": t.boolean().optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartySetProjectConfigRequestIn"])
    types["IdentitytoolkitRelyingpartySetProjectConfigRequestOut"] = t.struct(
        {
            "authorizedDomains": t.array(t.string()).optional(),
            "changeEmailTemplate": t.proxy(renames["EmailTemplateOut"]).optional(),
            "apiKey": t.string().optional(),
            "delegatedProjectNumber": t.string().optional(),
            "legacyResetPasswordTemplate": t.proxy(
                renames["EmailTemplateOut"]
            ).optional(),
            "resetPasswordTemplate": t.proxy(renames["EmailTemplateOut"]).optional(),
            "enableAnonymousUser": t.boolean().optional(),
            "idpConfig": t.array(t.proxy(renames["IdpConfigOut"])).optional(),
            "verifyEmailTemplate": t.proxy(renames["EmailTemplateOut"]).optional(),
            "allowPasswordUser": t.boolean().optional(),
            "useEmailSending": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartySetProjectConfigRequestOut"])
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
    types["IdentitytoolkitRelyingpartyDownloadAccountRequestIn"] = t.struct(
        {
            "delegatedProjectNumber": t.string().optional(),
            "targetProjectId": t.string().optional(),
            "maxResults": t.integer().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartyDownloadAccountRequestIn"])
    types["IdentitytoolkitRelyingpartyDownloadAccountRequestOut"] = t.struct(
        {
            "delegatedProjectNumber": t.string().optional(),
            "targetProjectId": t.string().optional(),
            "maxResults": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartyDownloadAccountRequestOut"])
    types["IdentitytoolkitRelyingpartyVerifyPhoneNumberRequestIn"] = t.struct(
        {
            "idToken": t.string(),
            "verificationProof": t.string(),
            "temporaryProof": t.string(),
            "code": t.string(),
            "operation": t.string(),
            "sessionInfo": t.string().optional(),
            "phoneNumber": t.string(),
        }
    ).named(renames["IdentitytoolkitRelyingpartyVerifyPhoneNumberRequestIn"])
    types["IdentitytoolkitRelyingpartyVerifyPhoneNumberRequestOut"] = t.struct(
        {
            "idToken": t.string(),
            "verificationProof": t.string(),
            "temporaryProof": t.string(),
            "code": t.string(),
            "operation": t.string(),
            "sessionInfo": t.string().optional(),
            "phoneNumber": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartyVerifyPhoneNumberRequestOut"])
    types["ResetPasswordResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "newEmail": t.string().optional(),
            "email": t.string().optional(),
            "requestType": t.string().optional(),
        }
    ).named(renames["ResetPasswordResponseIn"])
    types["ResetPasswordResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "newEmail": t.string().optional(),
            "email": t.string().optional(),
            "requestType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResetPasswordResponseOut"])
    types["IdentitytoolkitRelyingpartyVerifyCustomTokenRequestIn"] = t.struct(
        {
            "delegatedProjectNumber": t.string().optional(),
            "token": t.string().optional(),
            "returnSecureToken": t.boolean().optional(),
            "instanceId": t.string().optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartyVerifyCustomTokenRequestIn"])
    types["IdentitytoolkitRelyingpartyVerifyCustomTokenRequestOut"] = t.struct(
        {
            "delegatedProjectNumber": t.string().optional(),
            "token": t.string().optional(),
            "returnSecureToken": t.boolean().optional(),
            "instanceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartyVerifyCustomTokenRequestOut"])
    types["SignupNewUserResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "expiresIn": t.string().optional(),
            "localId": t.string().optional(),
            "displayName": t.string().optional(),
            "refreshToken": t.string().optional(),
            "email": t.string().optional(),
            "idToken": t.string().optional(),
        }
    ).named(renames["SignupNewUserResponseIn"])
    types["SignupNewUserResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "expiresIn": t.string().optional(),
            "localId": t.string().optional(),
            "displayName": t.string().optional(),
            "refreshToken": t.string().optional(),
            "email": t.string().optional(),
            "idToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SignupNewUserResponseOut"])
    types["RelyingpartyIn"] = t.struct(
        {
            "captchaResp": t.string().optional(),
            "email": t.string().optional(),
            "userIp": t.string().optional(),
            "androidMinimumVersion": t.string().optional(),
            "continueUrl": t.string().optional(),
            "kind": t.string().optional(),
            "iOSAppStoreId": t.string().optional(),
            "idToken": t.string().optional(),
            "challenge": t.string().optional(),
            "androidPackageName": t.string().optional(),
            "canHandleCodeInApp": t.boolean().optional(),
            "iOSBundleId": t.string().optional(),
            "androidInstallApp": t.boolean().optional(),
            "newEmail": t.string().optional(),
            "requestType": t.string().optional(),
        }
    ).named(renames["RelyingpartyIn"])
    types["RelyingpartyOut"] = t.struct(
        {
            "captchaResp": t.string().optional(),
            "email": t.string().optional(),
            "userIp": t.string().optional(),
            "androidMinimumVersion": t.string().optional(),
            "continueUrl": t.string().optional(),
            "kind": t.string().optional(),
            "iOSAppStoreId": t.string().optional(),
            "idToken": t.string().optional(),
            "challenge": t.string().optional(),
            "androidPackageName": t.string().optional(),
            "canHandleCodeInApp": t.boolean().optional(),
            "iOSBundleId": t.string().optional(),
            "androidInstallApp": t.boolean().optional(),
            "newEmail": t.string().optional(),
            "requestType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RelyingpartyOut"])
    types["IdentitytoolkitRelyingpartySignOutUserResponseIn"] = t.struct(
        {"localId": t.string().optional()}
    ).named(renames["IdentitytoolkitRelyingpartySignOutUserResponseIn"])
    types["IdentitytoolkitRelyingpartySignOutUserResponseOut"] = t.struct(
        {
            "localId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartySignOutUserResponseOut"])
    types["IdentitytoolkitRelyingpartyResetPasswordRequestIn"] = t.struct(
        {
            "oldPassword": t.string().optional(),
            "oobCode": t.string().optional(),
            "email": t.string().optional(),
            "newPassword": t.string().optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartyResetPasswordRequestIn"])
    types["IdentitytoolkitRelyingpartyResetPasswordRequestOut"] = t.struct(
        {
            "oldPassword": t.string().optional(),
            "oobCode": t.string().optional(),
            "email": t.string().optional(),
            "newPassword": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartyResetPasswordRequestOut"])
    types["IdentitytoolkitRelyingpartyVerifyPhoneNumberResponseIn"] = t.struct(
        {
            "verificationProofExpiresIn": t.string(),
            "localId": t.string(),
            "temporaryProof": t.string(),
            "temporaryProofExpiresIn": t.string(),
            "verificationProof": t.string(),
            "idToken": t.string(),
            "expiresIn": t.string(),
            "refreshToken": t.string(),
            "phoneNumber": t.string(),
            "isNewUser": t.boolean(),
        }
    ).named(renames["IdentitytoolkitRelyingpartyVerifyPhoneNumberResponseIn"])
    types["IdentitytoolkitRelyingpartyVerifyPhoneNumberResponseOut"] = t.struct(
        {
            "verificationProofExpiresIn": t.string(),
            "localId": t.string(),
            "temporaryProof": t.string(),
            "temporaryProofExpiresIn": t.string(),
            "verificationProof": t.string(),
            "idToken": t.string(),
            "expiresIn": t.string(),
            "refreshToken": t.string(),
            "phoneNumber": t.string(),
            "isNewUser": t.boolean(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartyVerifyPhoneNumberResponseOut"])
    types["VerifyAssertionResponseIn"] = t.struct(
        {
            "federatedId": t.string().optional(),
            "action": t.string().optional(),
            "inputEmail": t.string().optional(),
            "emailVerified": t.boolean().optional(),
            "fullName": t.string().optional(),
            "emailRecycled": t.boolean().optional(),
            "oauthIdToken": t.string().optional(),
            "oauthRequestToken": t.string().optional(),
            "photoUrl": t.string().optional(),
            "idToken": t.string().optional(),
            "lastName": t.string().optional(),
            "nickName": t.string().optional(),
            "oauthAccessToken": t.string().optional(),
            "verifiedProvider": t.array(t.string()).optional(),
            "firstName": t.string().optional(),
            "expiresIn": t.string().optional(),
            "localId": t.string().optional(),
            "screenName": t.string().optional(),
            "email": t.string().optional(),
            "originalEmail": t.string().optional(),
            "timeZone": t.string().optional(),
            "refreshToken": t.string().optional(),
            "displayName": t.string().optional(),
            "oauthScope": t.string().optional(),
            "appInstallationUrl": t.string().optional(),
            "providerId": t.string().optional(),
            "isNewUser": t.boolean().optional(),
            "rawUserInfo": t.string().optional(),
            "needEmail": t.boolean().optional(),
            "kind": t.string().optional(),
            "oauthExpireIn": t.integer().optional(),
            "context": t.string().optional(),
            "oauthTokenSecret": t.string().optional(),
            "errorMessage": t.string().optional(),
            "oauthAuthorizationCode": t.string().optional(),
            "needConfirmation": t.boolean().optional(),
            "appScheme": t.string().optional(),
            "language": t.string().optional(),
            "dateOfBirth": t.string().optional(),
        }
    ).named(renames["VerifyAssertionResponseIn"])
    types["VerifyAssertionResponseOut"] = t.struct(
        {
            "federatedId": t.string().optional(),
            "action": t.string().optional(),
            "inputEmail": t.string().optional(),
            "emailVerified": t.boolean().optional(),
            "fullName": t.string().optional(),
            "emailRecycled": t.boolean().optional(),
            "oauthIdToken": t.string().optional(),
            "oauthRequestToken": t.string().optional(),
            "photoUrl": t.string().optional(),
            "idToken": t.string().optional(),
            "lastName": t.string().optional(),
            "nickName": t.string().optional(),
            "oauthAccessToken": t.string().optional(),
            "verifiedProvider": t.array(t.string()).optional(),
            "firstName": t.string().optional(),
            "expiresIn": t.string().optional(),
            "localId": t.string().optional(),
            "screenName": t.string().optional(),
            "email": t.string().optional(),
            "originalEmail": t.string().optional(),
            "timeZone": t.string().optional(),
            "refreshToken": t.string().optional(),
            "displayName": t.string().optional(),
            "oauthScope": t.string().optional(),
            "appInstallationUrl": t.string().optional(),
            "providerId": t.string().optional(),
            "isNewUser": t.boolean().optional(),
            "rawUserInfo": t.string().optional(),
            "needEmail": t.boolean().optional(),
            "kind": t.string().optional(),
            "oauthExpireIn": t.integer().optional(),
            "context": t.string().optional(),
            "oauthTokenSecret": t.string().optional(),
            "errorMessage": t.string().optional(),
            "oauthAuthorizationCode": t.string().optional(),
            "needConfirmation": t.boolean().optional(),
            "appScheme": t.string().optional(),
            "language": t.string().optional(),
            "dateOfBirth": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VerifyAssertionResponseOut"])
    types["VerifyPasswordResponseIn"] = t.struct(
        {
            "photoUrl": t.string().optional(),
            "refreshToken": t.string().optional(),
            "expiresIn": t.string().optional(),
            "idToken": t.string().optional(),
            "oauthAuthorizationCode": t.string().optional(),
            "kind": t.string().optional(),
            "registered": t.boolean().optional(),
            "oauthAccessToken": t.string().optional(),
            "email": t.string().optional(),
            "oauthExpireIn": t.integer().optional(),
            "localId": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["VerifyPasswordResponseIn"])
    types["VerifyPasswordResponseOut"] = t.struct(
        {
            "photoUrl": t.string().optional(),
            "refreshToken": t.string().optional(),
            "expiresIn": t.string().optional(),
            "idToken": t.string().optional(),
            "oauthAuthorizationCode": t.string().optional(),
            "kind": t.string().optional(),
            "registered": t.boolean().optional(),
            "oauthAccessToken": t.string().optional(),
            "email": t.string().optional(),
            "oauthExpireIn": t.integer().optional(),
            "localId": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VerifyPasswordResponseOut"])
    types["IdentitytoolkitRelyingpartyGetProjectConfigResponseIn"] = t.struct(
        {
            "allowPasswordUser": t.boolean().optional(),
            "verifyEmailTemplate": t.proxy(renames["EmailTemplateIn"]).optional(),
            "dynamicLinksDomain": t.string(),
            "authorizedDomains": t.array(t.string()).optional(),
            "enableAnonymousUser": t.boolean().optional(),
            "resetPasswordTemplate": t.proxy(renames["EmailTemplateIn"]).optional(),
            "projectId": t.string().optional(),
            "apiKey": t.string().optional(),
            "legacyResetPasswordTemplate": t.proxy(
                renames["EmailTemplateIn"]
            ).optional(),
            "useEmailSending": t.boolean().optional(),
            "idpConfig": t.array(t.proxy(renames["IdpConfigIn"])).optional(),
            "changeEmailTemplate": t.proxy(renames["EmailTemplateIn"]).optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartyGetProjectConfigResponseIn"])
    types["IdentitytoolkitRelyingpartyGetProjectConfigResponseOut"] = t.struct(
        {
            "allowPasswordUser": t.boolean().optional(),
            "verifyEmailTemplate": t.proxy(renames["EmailTemplateOut"]).optional(),
            "dynamicLinksDomain": t.string(),
            "authorizedDomains": t.array(t.string()).optional(),
            "enableAnonymousUser": t.boolean().optional(),
            "resetPasswordTemplate": t.proxy(renames["EmailTemplateOut"]).optional(),
            "projectId": t.string().optional(),
            "apiKey": t.string().optional(),
            "legacyResetPasswordTemplate": t.proxy(
                renames["EmailTemplateOut"]
            ).optional(),
            "useEmailSending": t.boolean().optional(),
            "idpConfig": t.array(t.proxy(renames["IdpConfigOut"])).optional(),
            "changeEmailTemplate": t.proxy(renames["EmailTemplateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartyGetProjectConfigResponseOut"])
    types["IdentitytoolkitRelyingpartySignupNewUserRequestIn"] = t.struct(
        {
            "captchaChallenge": t.string().optional(),
            "localId": t.string().optional(),
            "tenantId": t.string().optional(),
            "email": t.string().optional(),
            "captchaResponse": t.string().optional(),
            "password": t.string().optional(),
            "idToken": t.string().optional(),
            "phoneNumber": t.string().optional(),
            "photoUrl": t.string().optional(),
            "emailVerified": t.boolean().optional(),
            "displayName": t.string().optional(),
            "disabled": t.boolean().optional(),
            "instanceId": t.string().optional(),
            "tenantProjectNumber": t.string().optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartySignupNewUserRequestIn"])
    types["IdentitytoolkitRelyingpartySignupNewUserRequestOut"] = t.struct(
        {
            "captchaChallenge": t.string().optional(),
            "localId": t.string().optional(),
            "tenantId": t.string().optional(),
            "email": t.string().optional(),
            "captchaResponse": t.string().optional(),
            "password": t.string().optional(),
            "idToken": t.string().optional(),
            "phoneNumber": t.string().optional(),
            "photoUrl": t.string().optional(),
            "emailVerified": t.boolean().optional(),
            "displayName": t.string().optional(),
            "disabled": t.boolean().optional(),
            "instanceId": t.string().optional(),
            "tenantProjectNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartySignupNewUserRequestOut"])
    types["UploadAccountResponseIn"] = t.struct(
        {
            "error": t.array(
                t.struct(
                    {"message": t.string().optional(), "index": t.integer().optional()}
                )
            ).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["UploadAccountResponseIn"])
    types["UploadAccountResponseOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["UploadAccountResponseOut"])
    types["VerifyCustomTokenResponseIn"] = t.struct(
        {
            "idToken": t.string().optional(),
            "refreshToken": t.string().optional(),
            "isNewUser": t.boolean().optional(),
            "kind": t.string().optional(),
            "expiresIn": t.string().optional(),
        }
    ).named(renames["VerifyCustomTokenResponseIn"])
    types["VerifyCustomTokenResponseOut"] = t.struct(
        {
            "idToken": t.string().optional(),
            "refreshToken": t.string().optional(),
            "isNewUser": t.boolean().optional(),
            "kind": t.string().optional(),
            "expiresIn": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VerifyCustomTokenResponseOut"])
    types["DownloadAccountResponseIn"] = t.struct(
        {
            "users": t.array(t.proxy(renames["UserInfoIn"])).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["DownloadAccountResponseIn"])
    types["DownloadAccountResponseOut"] = t.struct(
        {
            "users": t.array(t.proxy(renames["UserInfoOut"])).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DownloadAccountResponseOut"])
    types["IdentitytoolkitRelyingpartyGetPublicKeysResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["IdentitytoolkitRelyingpartyGetPublicKeysResponseIn"])
    types["IdentitytoolkitRelyingpartyGetPublicKeysResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["IdentitytoolkitRelyingpartyGetPublicKeysResponseOut"])
    types["IdentitytoolkitRelyingpartyCreateAuthUriRequestIn"] = t.struct(
        {
            "oauthScope": t.string().optional(),
            "tenantId": t.string().optional(),
            "sessionId": t.string().optional(),
            "clientId": t.string().optional(),
            "hostedDomain": t.string().optional(),
            "oauthConsumerKey": t.string().optional(),
            "continueUri": t.string().optional(),
            "customParameter": t.struct({"_": t.string().optional()}).optional(),
            "openidRealm": t.string().optional(),
            "providerId": t.string().optional(),
            "identifier": t.string().optional(),
            "authFlowType": t.string().optional(),
            "appId": t.string().optional(),
            "context": t.string().optional(),
            "otaApp": t.string().optional(),
            "tenantProjectNumber": t.string().optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartyCreateAuthUriRequestIn"])
    types["IdentitytoolkitRelyingpartyCreateAuthUriRequestOut"] = t.struct(
        {
            "oauthScope": t.string().optional(),
            "tenantId": t.string().optional(),
            "sessionId": t.string().optional(),
            "clientId": t.string().optional(),
            "hostedDomain": t.string().optional(),
            "oauthConsumerKey": t.string().optional(),
            "continueUri": t.string().optional(),
            "customParameter": t.struct({"_": t.string().optional()}).optional(),
            "openidRealm": t.string().optional(),
            "providerId": t.string().optional(),
            "identifier": t.string().optional(),
            "authFlowType": t.string().optional(),
            "appId": t.string().optional(),
            "context": t.string().optional(),
            "otaApp": t.string().optional(),
            "tenantProjectNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartyCreateAuthUriRequestOut"])
    types["EmailLinkSigninResponseIn"] = t.struct(
        {
            "idToken": t.string().optional(),
            "expiresIn": t.string().optional(),
            "kind": t.string().optional(),
            "refreshToken": t.string().optional(),
            "localId": t.string().optional(),
            "isNewUser": t.boolean().optional(),
            "email": t.string().optional(),
        }
    ).named(renames["EmailLinkSigninResponseIn"])
    types["EmailLinkSigninResponseOut"] = t.struct(
        {
            "idToken": t.string().optional(),
            "expiresIn": t.string().optional(),
            "kind": t.string().optional(),
            "refreshToken": t.string().optional(),
            "localId": t.string().optional(),
            "isNewUser": t.boolean().optional(),
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EmailLinkSigninResponseOut"])
    types["IdentitytoolkitRelyingpartySetAccountInfoRequestIn"] = t.struct(
        {
            "localId": t.string().optional(),
            "provider": t.array(t.string()).optional(),
            "lastLoginAt": t.string().optional(),
            "captchaChallenge": t.string().optional(),
            "photoUrl": t.string().optional(),
            "customAttributes": t.string().optional(),
            "phoneNumber": t.string().optional(),
            "returnSecureToken": t.boolean().optional(),
            "oobCode": t.string().optional(),
            "deleteProvider": t.array(t.string()).optional(),
            "captchaResponse": t.string().optional(),
            "instanceId": t.string().optional(),
            "emailVerified": t.boolean().optional(),
            "createdAt": t.string().optional(),
            "disableUser": t.boolean().optional(),
            "delegatedProjectNumber": t.string().optional(),
            "email": t.string().optional(),
            "deleteAttribute": t.array(t.string()).optional(),
            "upgradeToFederatedLogin": t.boolean().optional(),
            "idToken": t.string().optional(),
            "validSince": t.string().optional(),
            "password": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartySetAccountInfoRequestIn"])
    types["IdentitytoolkitRelyingpartySetAccountInfoRequestOut"] = t.struct(
        {
            "localId": t.string().optional(),
            "provider": t.array(t.string()).optional(),
            "lastLoginAt": t.string().optional(),
            "captchaChallenge": t.string().optional(),
            "photoUrl": t.string().optional(),
            "customAttributes": t.string().optional(),
            "phoneNumber": t.string().optional(),
            "returnSecureToken": t.boolean().optional(),
            "oobCode": t.string().optional(),
            "deleteProvider": t.array(t.string()).optional(),
            "captchaResponse": t.string().optional(),
            "instanceId": t.string().optional(),
            "emailVerified": t.boolean().optional(),
            "createdAt": t.string().optional(),
            "disableUser": t.boolean().optional(),
            "delegatedProjectNumber": t.string().optional(),
            "email": t.string().optional(),
            "deleteAttribute": t.array(t.string()).optional(),
            "upgradeToFederatedLogin": t.boolean().optional(),
            "idToken": t.string().optional(),
            "validSince": t.string().optional(),
            "password": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartySetAccountInfoRequestOut"])
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
    types["IdentitytoolkitRelyingpartySetProjectConfigResponseIn"] = t.struct(
        {"projectId": t.string().optional()}
    ).named(renames["IdentitytoolkitRelyingpartySetProjectConfigResponseIn"])
    types["IdentitytoolkitRelyingpartySetProjectConfigResponseOut"] = t.struct(
        {
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartySetProjectConfigResponseOut"])
    types["IdentitytoolkitRelyingpartyEmailLinkSigninRequestIn"] = t.struct(
        {
            "email": t.string().optional(),
            "idToken": t.string().optional(),
            "oobCode": t.string().optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartyEmailLinkSigninRequestIn"])
    types["IdentitytoolkitRelyingpartyEmailLinkSigninRequestOut"] = t.struct(
        {
            "email": t.string().optional(),
            "idToken": t.string().optional(),
            "oobCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartyEmailLinkSigninRequestOut"])
    types["IdentitytoolkitRelyingpartyDeleteAccountRequestIn"] = t.struct(
        {
            "idToken": t.string().optional(),
            "localId": t.string().optional(),
            "delegatedProjectNumber": t.string().optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartyDeleteAccountRequestIn"])
    types["IdentitytoolkitRelyingpartyDeleteAccountRequestOut"] = t.struct(
        {
            "idToken": t.string().optional(),
            "localId": t.string().optional(),
            "delegatedProjectNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartyDeleteAccountRequestOut"])
    types["CreateAuthUriResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "sessionId": t.string().optional(),
            "captchaRequired": t.boolean().optional(),
            "authUri": t.string().optional(),
            "registered": t.boolean().optional(),
            "forExistingProvider": t.boolean().optional(),
            "allProviders": t.array(t.string()).optional(),
            "providerId": t.string().optional(),
            "signinMethods": t.array(t.string()).optional(),
        }
    ).named(renames["CreateAuthUriResponseIn"])
    types["CreateAuthUriResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "sessionId": t.string().optional(),
            "captchaRequired": t.boolean().optional(),
            "authUri": t.string().optional(),
            "registered": t.boolean().optional(),
            "forExistingProvider": t.boolean().optional(),
            "allProviders": t.array(t.string()).optional(),
            "providerId": t.string().optional(),
            "signinMethods": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateAuthUriResponseOut"])
    types["SetAccountInfoResponseIn"] = t.struct(
        {
            "refreshToken": t.string().optional(),
            "kind": t.string().optional(),
            "email": t.string().optional(),
            "newEmail": t.string().optional(),
            "photoUrl": t.string().optional(),
            "idToken": t.string().optional(),
            "passwordHash": t.string().optional(),
            "displayName": t.string().optional(),
            "expiresIn": t.string().optional(),
            "localId": t.string().optional(),
            "emailVerified": t.boolean().optional(),
            "providerUserInfo": t.array(
                t.struct(
                    {
                        "displayName": t.string().optional(),
                        "photoUrl": t.string().optional(),
                        "providerId": t.string().optional(),
                        "federatedId": t.string().optional(),
                    }
                )
            ).optional(),
        }
    ).named(renames["SetAccountInfoResponseIn"])
    types["SetAccountInfoResponseOut"] = t.struct(
        {
            "refreshToken": t.string().optional(),
            "kind": t.string().optional(),
            "email": t.string().optional(),
            "newEmail": t.string().optional(),
            "photoUrl": t.string().optional(),
            "idToken": t.string().optional(),
            "passwordHash": t.string().optional(),
            "displayName": t.string().optional(),
            "expiresIn": t.string().optional(),
            "localId": t.string().optional(),
            "emailVerified": t.boolean().optional(),
            "providerUserInfo": t.array(
                t.struct(
                    {
                        "displayName": t.string().optional(),
                        "photoUrl": t.string().optional(),
                        "providerId": t.string().optional(),
                        "federatedId": t.string().optional(),
                    }
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetAccountInfoResponseOut"])
    types["IdentitytoolkitRelyingpartyGetAccountInfoRequestIn"] = t.struct(
        {
            "delegatedProjectNumber": t.string().optional(),
            "idToken": t.string().optional(),
            "phoneNumber": t.array(t.string()).optional(),
            "localId": t.array(t.string()).optional(),
            "email": t.array(t.string()).optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartyGetAccountInfoRequestIn"])
    types["IdentitytoolkitRelyingpartyGetAccountInfoRequestOut"] = t.struct(
        {
            "delegatedProjectNumber": t.string().optional(),
            "idToken": t.string().optional(),
            "phoneNumber": t.array(t.string()).optional(),
            "localId": t.array(t.string()).optional(),
            "email": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartyGetAccountInfoRequestOut"])
    types["IdentitytoolkitRelyingpartySendVerificationCodeResponseIn"] = t.struct(
        {"sessionInfo": t.string().optional()}
    ).named(renames["IdentitytoolkitRelyingpartySendVerificationCodeResponseIn"])
    types["IdentitytoolkitRelyingpartySendVerificationCodeResponseOut"] = t.struct(
        {
            "sessionInfo": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartySendVerificationCodeResponseOut"])
    types["IdentitytoolkitRelyingpartyUploadAccountRequestIn"] = t.struct(
        {
            "delegatedProjectNumber": t.string().optional(),
            "saltSeparator": t.string().optional(),
            "memoryCost": t.integer().optional(),
            "hashAlgorithm": t.string().optional(),
            "blockSize": t.integer(),
            "allowOverwrite": t.boolean().optional(),
            "dkLen": t.integer(),
            "rounds": t.integer().optional(),
            "targetProjectId": t.string().optional(),
            "cpuMemCost": t.integer().optional(),
            "parallelization": t.integer(),
            "users": t.array(t.proxy(renames["UserInfoIn"])).optional(),
            "signerKey": t.string().optional(),
            "sanityCheck": t.boolean().optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartyUploadAccountRequestIn"])
    types["IdentitytoolkitRelyingpartyUploadAccountRequestOut"] = t.struct(
        {
            "delegatedProjectNumber": t.string().optional(),
            "saltSeparator": t.string().optional(),
            "memoryCost": t.integer().optional(),
            "hashAlgorithm": t.string().optional(),
            "blockSize": t.integer(),
            "allowOverwrite": t.boolean().optional(),
            "dkLen": t.integer(),
            "rounds": t.integer().optional(),
            "targetProjectId": t.string().optional(),
            "cpuMemCost": t.integer().optional(),
            "parallelization": t.integer(),
            "users": t.array(t.proxy(renames["UserInfoOut"])).optional(),
            "signerKey": t.string().optional(),
            "sanityCheck": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartyUploadAccountRequestOut"])
    types["IdentitytoolkitRelyingpartyVerifyPasswordRequestIn"] = t.struct(
        {
            "idToken": t.string().optional(),
            "delegatedProjectNumber": t.string().optional(),
            "tenantProjectNumber": t.string().optional(),
            "email": t.string().optional(),
            "pendingIdToken": t.string().optional(),
            "password": t.string().optional(),
            "tenantId": t.string().optional(),
            "captchaChallenge": t.string().optional(),
            "returnSecureToken": t.boolean().optional(),
            "captchaResponse": t.string().optional(),
            "instanceId": t.string().optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartyVerifyPasswordRequestIn"])
    types["IdentitytoolkitRelyingpartyVerifyPasswordRequestOut"] = t.struct(
        {
            "idToken": t.string().optional(),
            "delegatedProjectNumber": t.string().optional(),
            "tenantProjectNumber": t.string().optional(),
            "email": t.string().optional(),
            "pendingIdToken": t.string().optional(),
            "password": t.string().optional(),
            "tenantId": t.string().optional(),
            "captchaChallenge": t.string().optional(),
            "returnSecureToken": t.boolean().optional(),
            "captchaResponse": t.string().optional(),
            "instanceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartyVerifyPasswordRequestOut"])
    types["IdentitytoolkitRelyingpartyVerifyAssertionRequestIn"] = t.struct(
        {
            "sessionId": t.string().optional(),
            "instanceId": t.string().optional(),
            "tenantId": t.string().optional(),
            "idToken": t.string().optional(),
            "tenantProjectNumber": t.string().optional(),
            "returnSecureToken": t.boolean().optional(),
            "autoCreate": t.boolean().optional(),
            "returnRefreshToken": t.boolean().optional(),
            "pendingIdToken": t.string().optional(),
            "returnIdpCredential": t.boolean().optional(),
            "requestUri": t.string().optional(),
            "postBody": t.string().optional(),
            "delegatedProjectNumber": t.string().optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartyVerifyAssertionRequestIn"])
    types["IdentitytoolkitRelyingpartyVerifyAssertionRequestOut"] = t.struct(
        {
            "sessionId": t.string().optional(),
            "instanceId": t.string().optional(),
            "tenantId": t.string().optional(),
            "idToken": t.string().optional(),
            "tenantProjectNumber": t.string().optional(),
            "returnSecureToken": t.boolean().optional(),
            "autoCreate": t.boolean().optional(),
            "returnRefreshToken": t.boolean().optional(),
            "pendingIdToken": t.string().optional(),
            "returnIdpCredential": t.boolean().optional(),
            "requestUri": t.string().optional(),
            "postBody": t.string().optional(),
            "delegatedProjectNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentitytoolkitRelyingpartyVerifyAssertionRequestOut"])

    functions = {}
    functions["relyingpartyResetPassword"] = identitytoolkit.post(
        "setAccountInfo",
        t.struct(
            {
                "localId": t.string().optional(),
                "provider": t.array(t.string()).optional(),
                "lastLoginAt": t.string().optional(),
                "captchaChallenge": t.string().optional(),
                "photoUrl": t.string().optional(),
                "customAttributes": t.string().optional(),
                "phoneNumber": t.string().optional(),
                "returnSecureToken": t.boolean().optional(),
                "oobCode": t.string().optional(),
                "deleteProvider": t.array(t.string()).optional(),
                "captchaResponse": t.string().optional(),
                "instanceId": t.string().optional(),
                "emailVerified": t.boolean().optional(),
                "createdAt": t.string().optional(),
                "disableUser": t.boolean().optional(),
                "delegatedProjectNumber": t.string().optional(),
                "email": t.string().optional(),
                "deleteAttribute": t.array(t.string()).optional(),
                "upgradeToFederatedLogin": t.boolean().optional(),
                "idToken": t.string().optional(),
                "validSince": t.string().optional(),
                "password": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SetAccountInfoResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["relyingpartySignOutUser"] = identitytoolkit.post(
        "setAccountInfo",
        t.struct(
            {
                "localId": t.string().optional(),
                "provider": t.array(t.string()).optional(),
                "lastLoginAt": t.string().optional(),
                "captchaChallenge": t.string().optional(),
                "photoUrl": t.string().optional(),
                "customAttributes": t.string().optional(),
                "phoneNumber": t.string().optional(),
                "returnSecureToken": t.boolean().optional(),
                "oobCode": t.string().optional(),
                "deleteProvider": t.array(t.string()).optional(),
                "captchaResponse": t.string().optional(),
                "instanceId": t.string().optional(),
                "emailVerified": t.boolean().optional(),
                "createdAt": t.string().optional(),
                "disableUser": t.boolean().optional(),
                "delegatedProjectNumber": t.string().optional(),
                "email": t.string().optional(),
                "deleteAttribute": t.array(t.string()).optional(),
                "upgradeToFederatedLogin": t.boolean().optional(),
                "idToken": t.string().optional(),
                "validSince": t.string().optional(),
                "password": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SetAccountInfoResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["relyingpartyGetRecaptchaParam"] = identitytoolkit.post(
        "setAccountInfo",
        t.struct(
            {
                "localId": t.string().optional(),
                "provider": t.array(t.string()).optional(),
                "lastLoginAt": t.string().optional(),
                "captchaChallenge": t.string().optional(),
                "photoUrl": t.string().optional(),
                "customAttributes": t.string().optional(),
                "phoneNumber": t.string().optional(),
                "returnSecureToken": t.boolean().optional(),
                "oobCode": t.string().optional(),
                "deleteProvider": t.array(t.string()).optional(),
                "captchaResponse": t.string().optional(),
                "instanceId": t.string().optional(),
                "emailVerified": t.boolean().optional(),
                "createdAt": t.string().optional(),
                "disableUser": t.boolean().optional(),
                "delegatedProjectNumber": t.string().optional(),
                "email": t.string().optional(),
                "deleteAttribute": t.array(t.string()).optional(),
                "upgradeToFederatedLogin": t.boolean().optional(),
                "idToken": t.string().optional(),
                "validSince": t.string().optional(),
                "password": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SetAccountInfoResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["relyingpartyGetPublicKeys"] = identitytoolkit.post(
        "setAccountInfo",
        t.struct(
            {
                "localId": t.string().optional(),
                "provider": t.array(t.string()).optional(),
                "lastLoginAt": t.string().optional(),
                "captchaChallenge": t.string().optional(),
                "photoUrl": t.string().optional(),
                "customAttributes": t.string().optional(),
                "phoneNumber": t.string().optional(),
                "returnSecureToken": t.boolean().optional(),
                "oobCode": t.string().optional(),
                "deleteProvider": t.array(t.string()).optional(),
                "captchaResponse": t.string().optional(),
                "instanceId": t.string().optional(),
                "emailVerified": t.boolean().optional(),
                "createdAt": t.string().optional(),
                "disableUser": t.boolean().optional(),
                "delegatedProjectNumber": t.string().optional(),
                "email": t.string().optional(),
                "deleteAttribute": t.array(t.string()).optional(),
                "upgradeToFederatedLogin": t.boolean().optional(),
                "idToken": t.string().optional(),
                "validSince": t.string().optional(),
                "password": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SetAccountInfoResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["relyingpartyVerifyCustomToken"] = identitytoolkit.post(
        "setAccountInfo",
        t.struct(
            {
                "localId": t.string().optional(),
                "provider": t.array(t.string()).optional(),
                "lastLoginAt": t.string().optional(),
                "captchaChallenge": t.string().optional(),
                "photoUrl": t.string().optional(),
                "customAttributes": t.string().optional(),
                "phoneNumber": t.string().optional(),
                "returnSecureToken": t.boolean().optional(),
                "oobCode": t.string().optional(),
                "deleteProvider": t.array(t.string()).optional(),
                "captchaResponse": t.string().optional(),
                "instanceId": t.string().optional(),
                "emailVerified": t.boolean().optional(),
                "createdAt": t.string().optional(),
                "disableUser": t.boolean().optional(),
                "delegatedProjectNumber": t.string().optional(),
                "email": t.string().optional(),
                "deleteAttribute": t.array(t.string()).optional(),
                "upgradeToFederatedLogin": t.boolean().optional(),
                "idToken": t.string().optional(),
                "validSince": t.string().optional(),
                "password": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SetAccountInfoResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["relyingpartyVerifyAssertion"] = identitytoolkit.post(
        "setAccountInfo",
        t.struct(
            {
                "localId": t.string().optional(),
                "provider": t.array(t.string()).optional(),
                "lastLoginAt": t.string().optional(),
                "captchaChallenge": t.string().optional(),
                "photoUrl": t.string().optional(),
                "customAttributes": t.string().optional(),
                "phoneNumber": t.string().optional(),
                "returnSecureToken": t.boolean().optional(),
                "oobCode": t.string().optional(),
                "deleteProvider": t.array(t.string()).optional(),
                "captchaResponse": t.string().optional(),
                "instanceId": t.string().optional(),
                "emailVerified": t.boolean().optional(),
                "createdAt": t.string().optional(),
                "disableUser": t.boolean().optional(),
                "delegatedProjectNumber": t.string().optional(),
                "email": t.string().optional(),
                "deleteAttribute": t.array(t.string()).optional(),
                "upgradeToFederatedLogin": t.boolean().optional(),
                "idToken": t.string().optional(),
                "validSince": t.string().optional(),
                "password": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SetAccountInfoResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["relyingpartyVerifyPhoneNumber"] = identitytoolkit.post(
        "setAccountInfo",
        t.struct(
            {
                "localId": t.string().optional(),
                "provider": t.array(t.string()).optional(),
                "lastLoginAt": t.string().optional(),
                "captchaChallenge": t.string().optional(),
                "photoUrl": t.string().optional(),
                "customAttributes": t.string().optional(),
                "phoneNumber": t.string().optional(),
                "returnSecureToken": t.boolean().optional(),
                "oobCode": t.string().optional(),
                "deleteProvider": t.array(t.string()).optional(),
                "captchaResponse": t.string().optional(),
                "instanceId": t.string().optional(),
                "emailVerified": t.boolean().optional(),
                "createdAt": t.string().optional(),
                "disableUser": t.boolean().optional(),
                "delegatedProjectNumber": t.string().optional(),
                "email": t.string().optional(),
                "deleteAttribute": t.array(t.string()).optional(),
                "upgradeToFederatedLogin": t.boolean().optional(),
                "idToken": t.string().optional(),
                "validSince": t.string().optional(),
                "password": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SetAccountInfoResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["relyingpartySignupNewUser"] = identitytoolkit.post(
        "setAccountInfo",
        t.struct(
            {
                "localId": t.string().optional(),
                "provider": t.array(t.string()).optional(),
                "lastLoginAt": t.string().optional(),
                "captchaChallenge": t.string().optional(),
                "photoUrl": t.string().optional(),
                "customAttributes": t.string().optional(),
                "phoneNumber": t.string().optional(),
                "returnSecureToken": t.boolean().optional(),
                "oobCode": t.string().optional(),
                "deleteProvider": t.array(t.string()).optional(),
                "captchaResponse": t.string().optional(),
                "instanceId": t.string().optional(),
                "emailVerified": t.boolean().optional(),
                "createdAt": t.string().optional(),
                "disableUser": t.boolean().optional(),
                "delegatedProjectNumber": t.string().optional(),
                "email": t.string().optional(),
                "deleteAttribute": t.array(t.string()).optional(),
                "upgradeToFederatedLogin": t.boolean().optional(),
                "idToken": t.string().optional(),
                "validSince": t.string().optional(),
                "password": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SetAccountInfoResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["relyingpartyCreateAuthUri"] = identitytoolkit.post(
        "setAccountInfo",
        t.struct(
            {
                "localId": t.string().optional(),
                "provider": t.array(t.string()).optional(),
                "lastLoginAt": t.string().optional(),
                "captchaChallenge": t.string().optional(),
                "photoUrl": t.string().optional(),
                "customAttributes": t.string().optional(),
                "phoneNumber": t.string().optional(),
                "returnSecureToken": t.boolean().optional(),
                "oobCode": t.string().optional(),
                "deleteProvider": t.array(t.string()).optional(),
                "captchaResponse": t.string().optional(),
                "instanceId": t.string().optional(),
                "emailVerified": t.boolean().optional(),
                "createdAt": t.string().optional(),
                "disableUser": t.boolean().optional(),
                "delegatedProjectNumber": t.string().optional(),
                "email": t.string().optional(),
                "deleteAttribute": t.array(t.string()).optional(),
                "upgradeToFederatedLogin": t.boolean().optional(),
                "idToken": t.string().optional(),
                "validSince": t.string().optional(),
                "password": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SetAccountInfoResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["relyingpartySetProjectConfig"] = identitytoolkit.post(
        "setAccountInfo",
        t.struct(
            {
                "localId": t.string().optional(),
                "provider": t.array(t.string()).optional(),
                "lastLoginAt": t.string().optional(),
                "captchaChallenge": t.string().optional(),
                "photoUrl": t.string().optional(),
                "customAttributes": t.string().optional(),
                "phoneNumber": t.string().optional(),
                "returnSecureToken": t.boolean().optional(),
                "oobCode": t.string().optional(),
                "deleteProvider": t.array(t.string()).optional(),
                "captchaResponse": t.string().optional(),
                "instanceId": t.string().optional(),
                "emailVerified": t.boolean().optional(),
                "createdAt": t.string().optional(),
                "disableUser": t.boolean().optional(),
                "delegatedProjectNumber": t.string().optional(),
                "email": t.string().optional(),
                "deleteAttribute": t.array(t.string()).optional(),
                "upgradeToFederatedLogin": t.boolean().optional(),
                "idToken": t.string().optional(),
                "validSince": t.string().optional(),
                "password": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SetAccountInfoResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["relyingpartyEmailLinkSignin"] = identitytoolkit.post(
        "setAccountInfo",
        t.struct(
            {
                "localId": t.string().optional(),
                "provider": t.array(t.string()).optional(),
                "lastLoginAt": t.string().optional(),
                "captchaChallenge": t.string().optional(),
                "photoUrl": t.string().optional(),
                "customAttributes": t.string().optional(),
                "phoneNumber": t.string().optional(),
                "returnSecureToken": t.boolean().optional(),
                "oobCode": t.string().optional(),
                "deleteProvider": t.array(t.string()).optional(),
                "captchaResponse": t.string().optional(),
                "instanceId": t.string().optional(),
                "emailVerified": t.boolean().optional(),
                "createdAt": t.string().optional(),
                "disableUser": t.boolean().optional(),
                "delegatedProjectNumber": t.string().optional(),
                "email": t.string().optional(),
                "deleteAttribute": t.array(t.string()).optional(),
                "upgradeToFederatedLogin": t.boolean().optional(),
                "idToken": t.string().optional(),
                "validSince": t.string().optional(),
                "password": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SetAccountInfoResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["relyingpartyVerifyPassword"] = identitytoolkit.post(
        "setAccountInfo",
        t.struct(
            {
                "localId": t.string().optional(),
                "provider": t.array(t.string()).optional(),
                "lastLoginAt": t.string().optional(),
                "captchaChallenge": t.string().optional(),
                "photoUrl": t.string().optional(),
                "customAttributes": t.string().optional(),
                "phoneNumber": t.string().optional(),
                "returnSecureToken": t.boolean().optional(),
                "oobCode": t.string().optional(),
                "deleteProvider": t.array(t.string()).optional(),
                "captchaResponse": t.string().optional(),
                "instanceId": t.string().optional(),
                "emailVerified": t.boolean().optional(),
                "createdAt": t.string().optional(),
                "disableUser": t.boolean().optional(),
                "delegatedProjectNumber": t.string().optional(),
                "email": t.string().optional(),
                "deleteAttribute": t.array(t.string()).optional(),
                "upgradeToFederatedLogin": t.boolean().optional(),
                "idToken": t.string().optional(),
                "validSince": t.string().optional(),
                "password": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SetAccountInfoResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["relyingpartyUploadAccount"] = identitytoolkit.post(
        "setAccountInfo",
        t.struct(
            {
                "localId": t.string().optional(),
                "provider": t.array(t.string()).optional(),
                "lastLoginAt": t.string().optional(),
                "captchaChallenge": t.string().optional(),
                "photoUrl": t.string().optional(),
                "customAttributes": t.string().optional(),
                "phoneNumber": t.string().optional(),
                "returnSecureToken": t.boolean().optional(),
                "oobCode": t.string().optional(),
                "deleteProvider": t.array(t.string()).optional(),
                "captchaResponse": t.string().optional(),
                "instanceId": t.string().optional(),
                "emailVerified": t.boolean().optional(),
                "createdAt": t.string().optional(),
                "disableUser": t.boolean().optional(),
                "delegatedProjectNumber": t.string().optional(),
                "email": t.string().optional(),
                "deleteAttribute": t.array(t.string()).optional(),
                "upgradeToFederatedLogin": t.boolean().optional(),
                "idToken": t.string().optional(),
                "validSince": t.string().optional(),
                "password": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SetAccountInfoResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["relyingpartyGetAccountInfo"] = identitytoolkit.post(
        "setAccountInfo",
        t.struct(
            {
                "localId": t.string().optional(),
                "provider": t.array(t.string()).optional(),
                "lastLoginAt": t.string().optional(),
                "captchaChallenge": t.string().optional(),
                "photoUrl": t.string().optional(),
                "customAttributes": t.string().optional(),
                "phoneNumber": t.string().optional(),
                "returnSecureToken": t.boolean().optional(),
                "oobCode": t.string().optional(),
                "deleteProvider": t.array(t.string()).optional(),
                "captchaResponse": t.string().optional(),
                "instanceId": t.string().optional(),
                "emailVerified": t.boolean().optional(),
                "createdAt": t.string().optional(),
                "disableUser": t.boolean().optional(),
                "delegatedProjectNumber": t.string().optional(),
                "email": t.string().optional(),
                "deleteAttribute": t.array(t.string()).optional(),
                "upgradeToFederatedLogin": t.boolean().optional(),
                "idToken": t.string().optional(),
                "validSince": t.string().optional(),
                "password": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SetAccountInfoResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["relyingpartyGetOobConfirmationCode"] = identitytoolkit.post(
        "setAccountInfo",
        t.struct(
            {
                "localId": t.string().optional(),
                "provider": t.array(t.string()).optional(),
                "lastLoginAt": t.string().optional(),
                "captchaChallenge": t.string().optional(),
                "photoUrl": t.string().optional(),
                "customAttributes": t.string().optional(),
                "phoneNumber": t.string().optional(),
                "returnSecureToken": t.boolean().optional(),
                "oobCode": t.string().optional(),
                "deleteProvider": t.array(t.string()).optional(),
                "captchaResponse": t.string().optional(),
                "instanceId": t.string().optional(),
                "emailVerified": t.boolean().optional(),
                "createdAt": t.string().optional(),
                "disableUser": t.boolean().optional(),
                "delegatedProjectNumber": t.string().optional(),
                "email": t.string().optional(),
                "deleteAttribute": t.array(t.string()).optional(),
                "upgradeToFederatedLogin": t.boolean().optional(),
                "idToken": t.string().optional(),
                "validSince": t.string().optional(),
                "password": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SetAccountInfoResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["relyingpartyDownloadAccount"] = identitytoolkit.post(
        "setAccountInfo",
        t.struct(
            {
                "localId": t.string().optional(),
                "provider": t.array(t.string()).optional(),
                "lastLoginAt": t.string().optional(),
                "captchaChallenge": t.string().optional(),
                "photoUrl": t.string().optional(),
                "customAttributes": t.string().optional(),
                "phoneNumber": t.string().optional(),
                "returnSecureToken": t.boolean().optional(),
                "oobCode": t.string().optional(),
                "deleteProvider": t.array(t.string()).optional(),
                "captchaResponse": t.string().optional(),
                "instanceId": t.string().optional(),
                "emailVerified": t.boolean().optional(),
                "createdAt": t.string().optional(),
                "disableUser": t.boolean().optional(),
                "delegatedProjectNumber": t.string().optional(),
                "email": t.string().optional(),
                "deleteAttribute": t.array(t.string()).optional(),
                "upgradeToFederatedLogin": t.boolean().optional(),
                "idToken": t.string().optional(),
                "validSince": t.string().optional(),
                "password": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SetAccountInfoResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["relyingpartyGetProjectConfig"] = identitytoolkit.post(
        "setAccountInfo",
        t.struct(
            {
                "localId": t.string().optional(),
                "provider": t.array(t.string()).optional(),
                "lastLoginAt": t.string().optional(),
                "captchaChallenge": t.string().optional(),
                "photoUrl": t.string().optional(),
                "customAttributes": t.string().optional(),
                "phoneNumber": t.string().optional(),
                "returnSecureToken": t.boolean().optional(),
                "oobCode": t.string().optional(),
                "deleteProvider": t.array(t.string()).optional(),
                "captchaResponse": t.string().optional(),
                "instanceId": t.string().optional(),
                "emailVerified": t.boolean().optional(),
                "createdAt": t.string().optional(),
                "disableUser": t.boolean().optional(),
                "delegatedProjectNumber": t.string().optional(),
                "email": t.string().optional(),
                "deleteAttribute": t.array(t.string()).optional(),
                "upgradeToFederatedLogin": t.boolean().optional(),
                "idToken": t.string().optional(),
                "validSince": t.string().optional(),
                "password": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SetAccountInfoResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["relyingpartyDeleteAccount"] = identitytoolkit.post(
        "setAccountInfo",
        t.struct(
            {
                "localId": t.string().optional(),
                "provider": t.array(t.string()).optional(),
                "lastLoginAt": t.string().optional(),
                "captchaChallenge": t.string().optional(),
                "photoUrl": t.string().optional(),
                "customAttributes": t.string().optional(),
                "phoneNumber": t.string().optional(),
                "returnSecureToken": t.boolean().optional(),
                "oobCode": t.string().optional(),
                "deleteProvider": t.array(t.string()).optional(),
                "captchaResponse": t.string().optional(),
                "instanceId": t.string().optional(),
                "emailVerified": t.boolean().optional(),
                "createdAt": t.string().optional(),
                "disableUser": t.boolean().optional(),
                "delegatedProjectNumber": t.string().optional(),
                "email": t.string().optional(),
                "deleteAttribute": t.array(t.string()).optional(),
                "upgradeToFederatedLogin": t.boolean().optional(),
                "idToken": t.string().optional(),
                "validSince": t.string().optional(),
                "password": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SetAccountInfoResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["relyingpartySendVerificationCode"] = identitytoolkit.post(
        "setAccountInfo",
        t.struct(
            {
                "localId": t.string().optional(),
                "provider": t.array(t.string()).optional(),
                "lastLoginAt": t.string().optional(),
                "captchaChallenge": t.string().optional(),
                "photoUrl": t.string().optional(),
                "customAttributes": t.string().optional(),
                "phoneNumber": t.string().optional(),
                "returnSecureToken": t.boolean().optional(),
                "oobCode": t.string().optional(),
                "deleteProvider": t.array(t.string()).optional(),
                "captchaResponse": t.string().optional(),
                "instanceId": t.string().optional(),
                "emailVerified": t.boolean().optional(),
                "createdAt": t.string().optional(),
                "disableUser": t.boolean().optional(),
                "delegatedProjectNumber": t.string().optional(),
                "email": t.string().optional(),
                "deleteAttribute": t.array(t.string()).optional(),
                "upgradeToFederatedLogin": t.boolean().optional(),
                "idToken": t.string().optional(),
                "validSince": t.string().optional(),
                "password": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SetAccountInfoResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["relyingpartySetAccountInfo"] = identitytoolkit.post(
        "setAccountInfo",
        t.struct(
            {
                "localId": t.string().optional(),
                "provider": t.array(t.string()).optional(),
                "lastLoginAt": t.string().optional(),
                "captchaChallenge": t.string().optional(),
                "photoUrl": t.string().optional(),
                "customAttributes": t.string().optional(),
                "phoneNumber": t.string().optional(),
                "returnSecureToken": t.boolean().optional(),
                "oobCode": t.string().optional(),
                "deleteProvider": t.array(t.string()).optional(),
                "captchaResponse": t.string().optional(),
                "instanceId": t.string().optional(),
                "emailVerified": t.boolean().optional(),
                "createdAt": t.string().optional(),
                "disableUser": t.boolean().optional(),
                "delegatedProjectNumber": t.string().optional(),
                "email": t.string().optional(),
                "deleteAttribute": t.array(t.string()).optional(),
                "upgradeToFederatedLogin": t.boolean().optional(),
                "idToken": t.string().optional(),
                "validSince": t.string().optional(),
                "password": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SetAccountInfoResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="identitytoolkit",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
