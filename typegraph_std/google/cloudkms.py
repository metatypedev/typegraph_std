from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_cloudkms() -> Import:
    cloudkms = HTTPRuntime("https://cloudkms.googleapis.com/")

    renames = {
        "ErrorResponse": "_cloudkms_1_ErrorResponse",
        "SetIamPolicyRequestIn": "_cloudkms_2_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_cloudkms_3_SetIamPolicyRequestOut",
        "KeyOperationAttestationIn": "_cloudkms_4_KeyOperationAttestationIn",
        "KeyOperationAttestationOut": "_cloudkms_5_KeyOperationAttestationOut",
        "WrappingPublicKeyIn": "_cloudkms_6_WrappingPublicKeyIn",
        "WrappingPublicKeyOut": "_cloudkms_7_WrappingPublicKeyOut",
        "PolicyIn": "_cloudkms_8_PolicyIn",
        "PolicyOut": "_cloudkms_9_PolicyOut",
        "ListCryptoKeysResponseIn": "_cloudkms_10_ListCryptoKeysResponseIn",
        "ListCryptoKeysResponseOut": "_cloudkms_11_ListCryptoKeysResponseOut",
        "PublicKeyIn": "_cloudkms_12_PublicKeyIn",
        "PublicKeyOut": "_cloudkms_13_PublicKeyOut",
        "TestIamPermissionsResponseIn": "_cloudkms_14_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_cloudkms_15_TestIamPermissionsResponseOut",
        "VerifyConnectivityResponseIn": "_cloudkms_16_VerifyConnectivityResponseIn",
        "VerifyConnectivityResponseOut": "_cloudkms_17_VerifyConnectivityResponseOut",
        "DecryptResponseIn": "_cloudkms_18_DecryptResponseIn",
        "DecryptResponseOut": "_cloudkms_19_DecryptResponseOut",
        "EncryptResponseIn": "_cloudkms_20_EncryptResponseIn",
        "EncryptResponseOut": "_cloudkms_21_EncryptResponseOut",
        "EkmConnectionIn": "_cloudkms_22_EkmConnectionIn",
        "EkmConnectionOut": "_cloudkms_23_EkmConnectionOut",
        "ListLocationsResponseIn": "_cloudkms_24_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_cloudkms_25_ListLocationsResponseOut",
        "DecryptRequestIn": "_cloudkms_26_DecryptRequestIn",
        "DecryptRequestOut": "_cloudkms_27_DecryptRequestOut",
        "CryptoKeyVersionIn": "_cloudkms_28_CryptoKeyVersionIn",
        "CryptoKeyVersionOut": "_cloudkms_29_CryptoKeyVersionOut",
        "DestroyCryptoKeyVersionRequestIn": "_cloudkms_30_DestroyCryptoKeyVersionRequestIn",
        "DestroyCryptoKeyVersionRequestOut": "_cloudkms_31_DestroyCryptoKeyVersionRequestOut",
        "MacVerifyResponseIn": "_cloudkms_32_MacVerifyResponseIn",
        "MacVerifyResponseOut": "_cloudkms_33_MacVerifyResponseOut",
        "BindingIn": "_cloudkms_34_BindingIn",
        "BindingOut": "_cloudkms_35_BindingOut",
        "TestIamPermissionsRequestIn": "_cloudkms_36_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_cloudkms_37_TestIamPermissionsRequestOut",
        "UpdateCryptoKeyPrimaryVersionRequestIn": "_cloudkms_38_UpdateCryptoKeyPrimaryVersionRequestIn",
        "UpdateCryptoKeyPrimaryVersionRequestOut": "_cloudkms_39_UpdateCryptoKeyPrimaryVersionRequestOut",
        "DigestIn": "_cloudkms_40_DigestIn",
        "DigestOut": "_cloudkms_41_DigestOut",
        "MacSignResponseIn": "_cloudkms_42_MacSignResponseIn",
        "MacSignResponseOut": "_cloudkms_43_MacSignResponseOut",
        "GenerateRandomBytesRequestIn": "_cloudkms_44_GenerateRandomBytesRequestIn",
        "GenerateRandomBytesRequestOut": "_cloudkms_45_GenerateRandomBytesRequestOut",
        "LocationMetadataIn": "_cloudkms_46_LocationMetadataIn",
        "LocationMetadataOut": "_cloudkms_47_LocationMetadataOut",
        "MacVerifyRequestIn": "_cloudkms_48_MacVerifyRequestIn",
        "MacVerifyRequestOut": "_cloudkms_49_MacVerifyRequestOut",
        "ExprIn": "_cloudkms_50_ExprIn",
        "ExprOut": "_cloudkms_51_ExprOut",
        "GenerateRandomBytesResponseIn": "_cloudkms_52_GenerateRandomBytesResponseIn",
        "GenerateRandomBytesResponseOut": "_cloudkms_53_GenerateRandomBytesResponseOut",
        "ImportCryptoKeyVersionRequestIn": "_cloudkms_54_ImportCryptoKeyVersionRequestIn",
        "ImportCryptoKeyVersionRequestOut": "_cloudkms_55_ImportCryptoKeyVersionRequestOut",
        "RestoreCryptoKeyVersionRequestIn": "_cloudkms_56_RestoreCryptoKeyVersionRequestIn",
        "RestoreCryptoKeyVersionRequestOut": "_cloudkms_57_RestoreCryptoKeyVersionRequestOut",
        "AsymmetricSignRequestIn": "_cloudkms_58_AsymmetricSignRequestIn",
        "AsymmetricSignRequestOut": "_cloudkms_59_AsymmetricSignRequestOut",
        "ListEkmConnectionsResponseIn": "_cloudkms_60_ListEkmConnectionsResponseIn",
        "ListEkmConnectionsResponseOut": "_cloudkms_61_ListEkmConnectionsResponseOut",
        "AsymmetricDecryptRequestIn": "_cloudkms_62_AsymmetricDecryptRequestIn",
        "AsymmetricDecryptRequestOut": "_cloudkms_63_AsymmetricDecryptRequestOut",
        "AsymmetricDecryptResponseIn": "_cloudkms_64_AsymmetricDecryptResponseIn",
        "AsymmetricDecryptResponseOut": "_cloudkms_65_AsymmetricDecryptResponseOut",
        "ListImportJobsResponseIn": "_cloudkms_66_ListImportJobsResponseIn",
        "ListImportJobsResponseOut": "_cloudkms_67_ListImportJobsResponseOut",
        "CryptoKeyIn": "_cloudkms_68_CryptoKeyIn",
        "CryptoKeyOut": "_cloudkms_69_CryptoKeyOut",
        "ExternalProtectionLevelOptionsIn": "_cloudkms_70_ExternalProtectionLevelOptionsIn",
        "ExternalProtectionLevelOptionsOut": "_cloudkms_71_ExternalProtectionLevelOptionsOut",
        "LocationIn": "_cloudkms_72_LocationIn",
        "LocationOut": "_cloudkms_73_LocationOut",
        "CertificateChainsIn": "_cloudkms_74_CertificateChainsIn",
        "CertificateChainsOut": "_cloudkms_75_CertificateChainsOut",
        "CertificateIn": "_cloudkms_76_CertificateIn",
        "CertificateOut": "_cloudkms_77_CertificateOut",
        "EkmConfigIn": "_cloudkms_78_EkmConfigIn",
        "EkmConfigOut": "_cloudkms_79_EkmConfigOut",
        "ImportJobIn": "_cloudkms_80_ImportJobIn",
        "ImportJobOut": "_cloudkms_81_ImportJobOut",
        "KeyRingIn": "_cloudkms_82_KeyRingIn",
        "KeyRingOut": "_cloudkms_83_KeyRingOut",
        "CryptoKeyVersionTemplateIn": "_cloudkms_84_CryptoKeyVersionTemplateIn",
        "CryptoKeyVersionTemplateOut": "_cloudkms_85_CryptoKeyVersionTemplateOut",
        "MacSignRequestIn": "_cloudkms_86_MacSignRequestIn",
        "MacSignRequestOut": "_cloudkms_87_MacSignRequestOut",
        "AuditLogConfigIn": "_cloudkms_88_AuditLogConfigIn",
        "AuditLogConfigOut": "_cloudkms_89_AuditLogConfigOut",
        "EncryptRequestIn": "_cloudkms_90_EncryptRequestIn",
        "EncryptRequestOut": "_cloudkms_91_EncryptRequestOut",
        "ListKeyRingsResponseIn": "_cloudkms_92_ListKeyRingsResponseIn",
        "ListKeyRingsResponseOut": "_cloudkms_93_ListKeyRingsResponseOut",
        "AuditConfigIn": "_cloudkms_94_AuditConfigIn",
        "AuditConfigOut": "_cloudkms_95_AuditConfigOut",
        "ServiceResolverIn": "_cloudkms_96_ServiceResolverIn",
        "ServiceResolverOut": "_cloudkms_97_ServiceResolverOut",
        "AsymmetricSignResponseIn": "_cloudkms_98_AsymmetricSignResponseIn",
        "AsymmetricSignResponseOut": "_cloudkms_99_AsymmetricSignResponseOut",
        "ListCryptoKeyVersionsResponseIn": "_cloudkms_100_ListCryptoKeyVersionsResponseIn",
        "ListCryptoKeyVersionsResponseOut": "_cloudkms_101_ListCryptoKeyVersionsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyIn"]).optional(),
            "updateMask": t.string().optional(),
        }
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "updateMask": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
    types["KeyOperationAttestationIn"] = t.struct({"_": t.string().optional()}).named(
        renames["KeyOperationAttestationIn"]
    )
    types["KeyOperationAttestationOut"] = t.struct(
        {
            "content": t.string().optional(),
            "format": t.string().optional(),
            "certChains": t.proxy(renames["CertificateChainsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyOperationAttestationOut"])
    types["WrappingPublicKeyIn"] = t.struct({"pem": t.string().optional()}).named(
        renames["WrappingPublicKeyIn"]
    )
    types["WrappingPublicKeyOut"] = t.struct(
        {
            "pem": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WrappingPublicKeyOut"])
    types["PolicyIn"] = t.struct(
        {
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["ListCryptoKeysResponseIn"] = t.struct(
        {
            "cryptoKeys": t.array(t.proxy(renames["CryptoKeyIn"])).optional(),
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListCryptoKeysResponseIn"])
    types["ListCryptoKeysResponseOut"] = t.struct(
        {
            "cryptoKeys": t.array(t.proxy(renames["CryptoKeyOut"])).optional(),
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCryptoKeysResponseOut"])
    types["PublicKeyIn"] = t.struct(
        {
            "protectionLevel": t.string().optional(),
            "pem": t.string().optional(),
            "algorithm": t.string().optional(),
            "name": t.string().optional(),
            "pemCrc32c": t.string().optional(),
        }
    ).named(renames["PublicKeyIn"])
    types["PublicKeyOut"] = t.struct(
        {
            "protectionLevel": t.string().optional(),
            "pem": t.string().optional(),
            "algorithm": t.string().optional(),
            "name": t.string().optional(),
            "pemCrc32c": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublicKeyOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["VerifyConnectivityResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["VerifyConnectivityResponseIn"])
    types["VerifyConnectivityResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["VerifyConnectivityResponseOut"])
    types["DecryptResponseIn"] = t.struct(
        {
            "usedPrimary": t.boolean().optional(),
            "plaintextCrc32c": t.string().optional(),
            "protectionLevel": t.string().optional(),
            "plaintext": t.string().optional(),
        }
    ).named(renames["DecryptResponseIn"])
    types["DecryptResponseOut"] = t.struct(
        {
            "usedPrimary": t.boolean().optional(),
            "plaintextCrc32c": t.string().optional(),
            "protectionLevel": t.string().optional(),
            "plaintext": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DecryptResponseOut"])
    types["EncryptResponseIn"] = t.struct(
        {
            "verifiedAdditionalAuthenticatedDataCrc32c": t.boolean().optional(),
            "ciphertextCrc32c": t.string().optional(),
            "name": t.string().optional(),
            "verifiedPlaintextCrc32c": t.boolean().optional(),
            "protectionLevel": t.string().optional(),
            "ciphertext": t.string().optional(),
        }
    ).named(renames["EncryptResponseIn"])
    types["EncryptResponseOut"] = t.struct(
        {
            "verifiedAdditionalAuthenticatedDataCrc32c": t.boolean().optional(),
            "ciphertextCrc32c": t.string().optional(),
            "name": t.string().optional(),
            "verifiedPlaintextCrc32c": t.boolean().optional(),
            "protectionLevel": t.string().optional(),
            "ciphertext": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EncryptResponseOut"])
    types["EkmConnectionIn"] = t.struct(
        {
            "keyManagementMode": t.string().optional(),
            "cryptoSpacePath": t.string().optional(),
            "serviceResolvers": t.array(
                t.proxy(renames["ServiceResolverIn"])
            ).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["EkmConnectionIn"])
    types["EkmConnectionOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "keyManagementMode": t.string().optional(),
            "cryptoSpacePath": t.string().optional(),
            "name": t.string().optional(),
            "serviceResolvers": t.array(
                t.proxy(renames["ServiceResolverOut"])
            ).optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EkmConnectionOut"])
    types["ListLocationsResponseIn"] = t.struct(
        {
            "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListLocationsResponseIn"])
    types["ListLocationsResponseOut"] = t.struct(
        {
            "locations": t.array(t.proxy(renames["LocationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLocationsResponseOut"])
    types["DecryptRequestIn"] = t.struct(
        {
            "additionalAuthenticatedDataCrc32c": t.string().optional(),
            "additionalAuthenticatedData": t.string().optional(),
            "ciphertextCrc32c": t.string().optional(),
            "ciphertext": t.string(),
        }
    ).named(renames["DecryptRequestIn"])
    types["DecryptRequestOut"] = t.struct(
        {
            "additionalAuthenticatedDataCrc32c": t.string().optional(),
            "additionalAuthenticatedData": t.string().optional(),
            "ciphertextCrc32c": t.string().optional(),
            "ciphertext": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DecryptRequestOut"])
    types["CryptoKeyVersionIn"] = t.struct(
        {
            "state": t.string().optional(),
            "externalProtectionLevelOptions": t.proxy(
                renames["ExternalProtectionLevelOptionsIn"]
            ).optional(),
        }
    ).named(renames["CryptoKeyVersionIn"])
    types["CryptoKeyVersionOut"] = t.struct(
        {
            "importJob": t.string().optional(),
            "destroyTime": t.string().optional(),
            "state": t.string().optional(),
            "externalProtectionLevelOptions": t.proxy(
                renames["ExternalProtectionLevelOptionsOut"]
            ).optional(),
            "name": t.string().optional(),
            "generationFailureReason": t.string().optional(),
            "algorithm": t.string().optional(),
            "importTime": t.string().optional(),
            "reimportEligible": t.boolean().optional(),
            "protectionLevel": t.string().optional(),
            "externalDestructionFailureReason": t.string().optional(),
            "generateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "destroyEventTime": t.string().optional(),
            "importFailureReason": t.string().optional(),
            "attestation": t.proxy(renames["KeyOperationAttestationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CryptoKeyVersionOut"])
    types["DestroyCryptoKeyVersionRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DestroyCryptoKeyVersionRequestIn"])
    types["DestroyCryptoKeyVersionRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DestroyCryptoKeyVersionRequestOut"])
    types["MacVerifyResponseIn"] = t.struct(
        {
            "verifiedDataCrc32c": t.boolean().optional(),
            "name": t.string().optional(),
            "verifiedMacCrc32c": t.boolean().optional(),
            "verifiedSuccessIntegrity": t.boolean().optional(),
            "success": t.boolean().optional(),
            "protectionLevel": t.string().optional(),
        }
    ).named(renames["MacVerifyResponseIn"])
    types["MacVerifyResponseOut"] = t.struct(
        {
            "verifiedDataCrc32c": t.boolean().optional(),
            "name": t.string().optional(),
            "verifiedMacCrc32c": t.boolean().optional(),
            "verifiedSuccessIntegrity": t.boolean().optional(),
            "success": t.boolean().optional(),
            "protectionLevel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MacVerifyResponseOut"])
    types["BindingIn"] = t.struct(
        {
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["UpdateCryptoKeyPrimaryVersionRequestIn"] = t.struct(
        {"cryptoKeyVersionId": t.string()}
    ).named(renames["UpdateCryptoKeyPrimaryVersionRequestIn"])
    types["UpdateCryptoKeyPrimaryVersionRequestOut"] = t.struct(
        {
            "cryptoKeyVersionId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateCryptoKeyPrimaryVersionRequestOut"])
    types["DigestIn"] = t.struct(
        {
            "sha256": t.string().optional(),
            "sha512": t.string().optional(),
            "sha384": t.string().optional(),
        }
    ).named(renames["DigestIn"])
    types["DigestOut"] = t.struct(
        {
            "sha256": t.string().optional(),
            "sha512": t.string().optional(),
            "sha384": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DigestOut"])
    types["MacSignResponseIn"] = t.struct(
        {
            "verifiedDataCrc32c": t.boolean().optional(),
            "mac": t.string().optional(),
            "protectionLevel": t.string().optional(),
            "macCrc32c": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["MacSignResponseIn"])
    types["MacSignResponseOut"] = t.struct(
        {
            "verifiedDataCrc32c": t.boolean().optional(),
            "mac": t.string().optional(),
            "protectionLevel": t.string().optional(),
            "macCrc32c": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MacSignResponseOut"])
    types["GenerateRandomBytesRequestIn"] = t.struct(
        {
            "protectionLevel": t.string().optional(),
            "lengthBytes": t.integer().optional(),
        }
    ).named(renames["GenerateRandomBytesRequestIn"])
    types["GenerateRandomBytesRequestOut"] = t.struct(
        {
            "protectionLevel": t.string().optional(),
            "lengthBytes": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateRandomBytesRequestOut"])
    types["LocationMetadataIn"] = t.struct(
        {"hsmAvailable": t.boolean().optional(), "ekmAvailable": t.boolean().optional()}
    ).named(renames["LocationMetadataIn"])
    types["LocationMetadataOut"] = t.struct(
        {
            "hsmAvailable": t.boolean().optional(),
            "ekmAvailable": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationMetadataOut"])
    types["MacVerifyRequestIn"] = t.struct(
        {
            "dataCrc32c": t.string().optional(),
            "data": t.string(),
            "macCrc32c": t.string().optional(),
            "mac": t.string(),
        }
    ).named(renames["MacVerifyRequestIn"])
    types["MacVerifyRequestOut"] = t.struct(
        {
            "dataCrc32c": t.string().optional(),
            "data": t.string(),
            "macCrc32c": t.string().optional(),
            "mac": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MacVerifyRequestOut"])
    types["ExprIn"] = t.struct(
        {
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["GenerateRandomBytesResponseIn"] = t.struct(
        {"data": t.string().optional(), "dataCrc32c": t.string().optional()}
    ).named(renames["GenerateRandomBytesResponseIn"])
    types["GenerateRandomBytesResponseOut"] = t.struct(
        {
            "data": t.string().optional(),
            "dataCrc32c": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateRandomBytesResponseOut"])
    types["ImportCryptoKeyVersionRequestIn"] = t.struct(
        {
            "algorithm": t.string(),
            "importJob": t.string(),
            "rsaAesWrappedKey": t.string().optional(),
            "wrappedKey": t.string().optional(),
            "cryptoKeyVersion": t.string().optional(),
        }
    ).named(renames["ImportCryptoKeyVersionRequestIn"])
    types["ImportCryptoKeyVersionRequestOut"] = t.struct(
        {
            "algorithm": t.string(),
            "importJob": t.string(),
            "rsaAesWrappedKey": t.string().optional(),
            "wrappedKey": t.string().optional(),
            "cryptoKeyVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportCryptoKeyVersionRequestOut"])
    types["RestoreCryptoKeyVersionRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["RestoreCryptoKeyVersionRequestIn"])
    types["RestoreCryptoKeyVersionRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RestoreCryptoKeyVersionRequestOut"])
    types["AsymmetricSignRequestIn"] = t.struct(
        {
            "data": t.string().optional(),
            "dataCrc32c": t.string().optional(),
            "digest": t.proxy(renames["DigestIn"]).optional(),
            "digestCrc32c": t.string().optional(),
        }
    ).named(renames["AsymmetricSignRequestIn"])
    types["AsymmetricSignRequestOut"] = t.struct(
        {
            "data": t.string().optional(),
            "dataCrc32c": t.string().optional(),
            "digest": t.proxy(renames["DigestOut"]).optional(),
            "digestCrc32c": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AsymmetricSignRequestOut"])
    types["ListEkmConnectionsResponseIn"] = t.struct(
        {
            "ekmConnections": t.array(t.proxy(renames["EkmConnectionIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
        }
    ).named(renames["ListEkmConnectionsResponseIn"])
    types["ListEkmConnectionsResponseOut"] = t.struct(
        {
            "ekmConnections": t.array(t.proxy(renames["EkmConnectionOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListEkmConnectionsResponseOut"])
    types["AsymmetricDecryptRequestIn"] = t.struct(
        {"ciphertext": t.string(), "ciphertextCrc32c": t.string().optional()}
    ).named(renames["AsymmetricDecryptRequestIn"])
    types["AsymmetricDecryptRequestOut"] = t.struct(
        {
            "ciphertext": t.string(),
            "ciphertextCrc32c": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AsymmetricDecryptRequestOut"])
    types["AsymmetricDecryptResponseIn"] = t.struct(
        {
            "plaintext": t.string().optional(),
            "verifiedCiphertextCrc32c": t.boolean().optional(),
            "plaintextCrc32c": t.string().optional(),
            "protectionLevel": t.string().optional(),
        }
    ).named(renames["AsymmetricDecryptResponseIn"])
    types["AsymmetricDecryptResponseOut"] = t.struct(
        {
            "plaintext": t.string().optional(),
            "verifiedCiphertextCrc32c": t.boolean().optional(),
            "plaintextCrc32c": t.string().optional(),
            "protectionLevel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AsymmetricDecryptResponseOut"])
    types["ListImportJobsResponseIn"] = t.struct(
        {
            "importJobs": t.array(t.proxy(renames["ImportJobIn"])).optional(),
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListImportJobsResponseIn"])
    types["ListImportJobsResponseOut"] = t.struct(
        {
            "importJobs": t.array(t.proxy(renames["ImportJobOut"])).optional(),
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListImportJobsResponseOut"])
    types["CryptoKeyIn"] = t.struct(
        {
            "rotationPeriod": t.string().optional(),
            "versionTemplate": t.proxy(
                renames["CryptoKeyVersionTemplateIn"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "destroyScheduledDuration": t.string().optional(),
            "nextRotationTime": t.string().optional(),
            "importOnly": t.boolean().optional(),
            "purpose": t.string().optional(),
            "cryptoKeyBackend": t.string().optional(),
        }
    ).named(renames["CryptoKeyIn"])
    types["CryptoKeyOut"] = t.struct(
        {
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "rotationPeriod": t.string().optional(),
            "versionTemplate": t.proxy(
                renames["CryptoKeyVersionTemplateOut"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "destroyScheduledDuration": t.string().optional(),
            "nextRotationTime": t.string().optional(),
            "primary": t.proxy(renames["CryptoKeyVersionOut"]).optional(),
            "importOnly": t.boolean().optional(),
            "purpose": t.string().optional(),
            "cryptoKeyBackend": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CryptoKeyOut"])
    types["ExternalProtectionLevelOptionsIn"] = t.struct(
        {
            "ekmConnectionKeyPath": t.string().optional(),
            "externalKeyUri": t.string().optional(),
        }
    ).named(renames["ExternalProtectionLevelOptionsIn"])
    types["ExternalProtectionLevelOptionsOut"] = t.struct(
        {
            "ekmConnectionKeyPath": t.string().optional(),
            "externalKeyUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExternalProtectionLevelOptionsOut"])
    types["LocationIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["CertificateChainsIn"] = t.struct(
        {
            "googleCardCerts": t.array(t.string()).optional(),
            "caviumCerts": t.array(t.string()).optional(),
            "googlePartitionCerts": t.array(t.string()).optional(),
        }
    ).named(renames["CertificateChainsIn"])
    types["CertificateChainsOut"] = t.struct(
        {
            "googleCardCerts": t.array(t.string()).optional(),
            "caviumCerts": t.array(t.string()).optional(),
            "googlePartitionCerts": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateChainsOut"])
    types["CertificateIn"] = t.struct({"rawDer": t.string()}).named(
        renames["CertificateIn"]
    )
    types["CertificateOut"] = t.struct(
        {
            "subjectAlternativeDnsNames": t.array(t.string()).optional(),
            "issuer": t.string().optional(),
            "notAfterTime": t.string().optional(),
            "rawDer": t.string(),
            "serialNumber": t.string().optional(),
            "sha256Fingerprint": t.string().optional(),
            "parsed": t.boolean().optional(),
            "subject": t.string().optional(),
            "notBeforeTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateOut"])
    types["EkmConfigIn"] = t.struct(
        {"defaultEkmConnection": t.string().optional()}
    ).named(renames["EkmConfigIn"])
    types["EkmConfigOut"] = t.struct(
        {
            "defaultEkmConnection": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EkmConfigOut"])
    types["ImportJobIn"] = t.struct(
        {"protectionLevel": t.string(), "importMethod": t.string()}
    ).named(renames["ImportJobIn"])
    types["ImportJobOut"] = t.struct(
        {
            "name": t.string().optional(),
            "expireTime": t.string().optional(),
            "publicKey": t.proxy(renames["WrappingPublicKeyOut"]).optional(),
            "protectionLevel": t.string(),
            "generateTime": t.string().optional(),
            "expireEventTime": t.string().optional(),
            "state": t.string().optional(),
            "attestation": t.proxy(renames["KeyOperationAttestationOut"]).optional(),
            "createTime": t.string().optional(),
            "importMethod": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportJobOut"])
    types["KeyRingIn"] = t.struct({"_": t.string().optional()}).named(
        renames["KeyRingIn"]
    )
    types["KeyRingOut"] = t.struct(
        {
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyRingOut"])
    types["CryptoKeyVersionTemplateIn"] = t.struct(
        {"protectionLevel": t.string().optional(), "algorithm": t.string()}
    ).named(renames["CryptoKeyVersionTemplateIn"])
    types["CryptoKeyVersionTemplateOut"] = t.struct(
        {
            "protectionLevel": t.string().optional(),
            "algorithm": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CryptoKeyVersionTemplateOut"])
    types["MacSignRequestIn"] = t.struct(
        {"dataCrc32c": t.string().optional(), "data": t.string()}
    ).named(renames["MacSignRequestIn"])
    types["MacSignRequestOut"] = t.struct(
        {
            "dataCrc32c": t.string().optional(),
            "data": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MacSignRequestOut"])
    types["AuditLogConfigIn"] = t.struct(
        {
            "logType": t.string().optional(),
            "exemptedMembers": t.array(t.string()).optional(),
        }
    ).named(renames["AuditLogConfigIn"])
    types["AuditLogConfigOut"] = t.struct(
        {
            "logType": t.string().optional(),
            "exemptedMembers": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditLogConfigOut"])
    types["EncryptRequestIn"] = t.struct(
        {
            "additionalAuthenticatedDataCrc32c": t.string().optional(),
            "plaintextCrc32c": t.string().optional(),
            "plaintext": t.string(),
            "additionalAuthenticatedData": t.string().optional(),
        }
    ).named(renames["EncryptRequestIn"])
    types["EncryptRequestOut"] = t.struct(
        {
            "additionalAuthenticatedDataCrc32c": t.string().optional(),
            "plaintextCrc32c": t.string().optional(),
            "plaintext": t.string(),
            "additionalAuthenticatedData": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EncryptRequestOut"])
    types["ListKeyRingsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "keyRings": t.array(t.proxy(renames["KeyRingIn"])).optional(),
        }
    ).named(renames["ListKeyRingsResponseIn"])
    types["ListKeyRingsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "keyRings": t.array(t.proxy(renames["KeyRingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListKeyRingsResponseOut"])
    types["AuditConfigIn"] = t.struct(
        {
            "auditLogConfigs": t.array(t.proxy(renames["AuditLogConfigIn"])).optional(),
            "service": t.string().optional(),
        }
    ).named(renames["AuditConfigIn"])
    types["AuditConfigOut"] = t.struct(
        {
            "auditLogConfigs": t.array(
                t.proxy(renames["AuditLogConfigOut"])
            ).optional(),
            "service": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditConfigOut"])
    types["ServiceResolverIn"] = t.struct(
        {
            "hostname": t.string(),
            "endpointFilter": t.string().optional(),
            "serverCertificates": t.array(t.proxy(renames["CertificateIn"])),
            "serviceDirectoryService": t.string(),
        }
    ).named(renames["ServiceResolverIn"])
    types["ServiceResolverOut"] = t.struct(
        {
            "hostname": t.string(),
            "endpointFilter": t.string().optional(),
            "serverCertificates": t.array(t.proxy(renames["CertificateOut"])),
            "serviceDirectoryService": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceResolverOut"])
    types["AsymmetricSignResponseIn"] = t.struct(
        {
            "protectionLevel": t.string().optional(),
            "verifiedDigestCrc32c": t.boolean().optional(),
            "verifiedDataCrc32c": t.boolean().optional(),
            "signature": t.string().optional(),
            "signatureCrc32c": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["AsymmetricSignResponseIn"])
    types["AsymmetricSignResponseOut"] = t.struct(
        {
            "protectionLevel": t.string().optional(),
            "verifiedDigestCrc32c": t.boolean().optional(),
            "verifiedDataCrc32c": t.boolean().optional(),
            "signature": t.string().optional(),
            "signatureCrc32c": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AsymmetricSignResponseOut"])
    types["ListCryptoKeyVersionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "cryptoKeyVersions": t.array(
                t.proxy(renames["CryptoKeyVersionIn"])
            ).optional(),
        }
    ).named(renames["ListCryptoKeyVersionsResponseIn"])
    types["ListCryptoKeyVersionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "cryptoKeyVersions": t.array(
                t.proxy(renames["CryptoKeyVersionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCryptoKeyVersionsResponseOut"])

    functions = {}
    functions["projectsLocationsGet"] = cloudkms.post(
        "v1/{location}:generateRandomBytes",
        t.struct(
            {
                "location": t.string().optional(),
                "protectionLevel": t.string().optional(),
                "lengthBytes": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GenerateRandomBytesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsList"] = cloudkms.post(
        "v1/{location}:generateRandomBytes",
        t.struct(
            {
                "location": t.string().optional(),
                "protectionLevel": t.string().optional(),
                "lengthBytes": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GenerateRandomBytesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGetEkmConfig"] = cloudkms.post(
        "v1/{location}:generateRandomBytes",
        t.struct(
            {
                "location": t.string().optional(),
                "protectionLevel": t.string().optional(),
                "lengthBytes": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GenerateRandomBytesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsUpdateEkmConfig"] = cloudkms.post(
        "v1/{location}:generateRandomBytes",
        t.struct(
            {
                "location": t.string().optional(),
                "protectionLevel": t.string().optional(),
                "lengthBytes": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GenerateRandomBytesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGenerateRandomBytes"] = cloudkms.post(
        "v1/{location}:generateRandomBytes",
        t.struct(
            {
                "location": t.string().optional(),
                "protectionLevel": t.string().optional(),
                "lengthBytes": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GenerateRandomBytesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEkmConnectionsCreate"] = cloudkms.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEkmConnectionsList"] = cloudkms.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEkmConnectionsPatch"] = cloudkms.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEkmConnectionsVerifyConnectivity"] = cloudkms.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEkmConnectionsTestIamPermissions"] = cloudkms.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEkmConnectionsGetIamPolicy"] = cloudkms.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEkmConnectionsGet"] = cloudkms.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEkmConnectionsSetIamPolicy"] = cloudkms.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsGetIamPolicy"] = cloudkms.post(
        "v1/{parent}/keyRings",
        t.struct(
            {
                "keyRingId": t.string(),
                "parent": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["KeyRingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsSetIamPolicy"] = cloudkms.post(
        "v1/{parent}/keyRings",
        t.struct(
            {
                "keyRingId": t.string(),
                "parent": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["KeyRingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsGet"] = cloudkms.post(
        "v1/{parent}/keyRings",
        t.struct(
            {
                "keyRingId": t.string(),
                "parent": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["KeyRingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsList"] = cloudkms.post(
        "v1/{parent}/keyRings",
        t.struct(
            {
                "keyRingId": t.string(),
                "parent": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["KeyRingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsTestIamPermissions"] = cloudkms.post(
        "v1/{parent}/keyRings",
        t.struct(
            {
                "keyRingId": t.string(),
                "parent": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["KeyRingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsCreate"] = cloudkms.post(
        "v1/{parent}/keyRings",
        t.struct(
            {
                "keyRingId": t.string(),
                "parent": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["KeyRingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsCryptoKeysGet"] = cloudkms.post(
        "v1/{name}:decrypt",
        t.struct(
            {
                "name": t.string(),
                "additionalAuthenticatedDataCrc32c": t.string().optional(),
                "additionalAuthenticatedData": t.string().optional(),
                "ciphertextCrc32c": t.string().optional(),
                "ciphertext": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DecryptResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsCryptoKeysEncrypt"] = cloudkms.post(
        "v1/{name}:decrypt",
        t.struct(
            {
                "name": t.string(),
                "additionalAuthenticatedDataCrc32c": t.string().optional(),
                "additionalAuthenticatedData": t.string().optional(),
                "ciphertextCrc32c": t.string().optional(),
                "ciphertext": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DecryptResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsCryptoKeysGetIamPolicy"] = cloudkms.post(
        "v1/{name}:decrypt",
        t.struct(
            {
                "name": t.string(),
                "additionalAuthenticatedDataCrc32c": t.string().optional(),
                "additionalAuthenticatedData": t.string().optional(),
                "ciphertextCrc32c": t.string().optional(),
                "ciphertext": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DecryptResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsCryptoKeysPatch"] = cloudkms.post(
        "v1/{name}:decrypt",
        t.struct(
            {
                "name": t.string(),
                "additionalAuthenticatedDataCrc32c": t.string().optional(),
                "additionalAuthenticatedData": t.string().optional(),
                "ciphertextCrc32c": t.string().optional(),
                "ciphertext": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DecryptResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsCryptoKeysCreate"] = cloudkms.post(
        "v1/{name}:decrypt",
        t.struct(
            {
                "name": t.string(),
                "additionalAuthenticatedDataCrc32c": t.string().optional(),
                "additionalAuthenticatedData": t.string().optional(),
                "ciphertextCrc32c": t.string().optional(),
                "ciphertext": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DecryptResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsKeyRingsCryptoKeysUpdatePrimaryVersion"
    ] = cloudkms.post(
        "v1/{name}:decrypt",
        t.struct(
            {
                "name": t.string(),
                "additionalAuthenticatedDataCrc32c": t.string().optional(),
                "additionalAuthenticatedData": t.string().optional(),
                "ciphertextCrc32c": t.string().optional(),
                "ciphertext": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DecryptResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsCryptoKeysTestIamPermissions"] = cloudkms.post(
        "v1/{name}:decrypt",
        t.struct(
            {
                "name": t.string(),
                "additionalAuthenticatedDataCrc32c": t.string().optional(),
                "additionalAuthenticatedData": t.string().optional(),
                "ciphertextCrc32c": t.string().optional(),
                "ciphertext": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DecryptResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsCryptoKeysSetIamPolicy"] = cloudkms.post(
        "v1/{name}:decrypt",
        t.struct(
            {
                "name": t.string(),
                "additionalAuthenticatedDataCrc32c": t.string().optional(),
                "additionalAuthenticatedData": t.string().optional(),
                "ciphertextCrc32c": t.string().optional(),
                "ciphertext": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DecryptResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsCryptoKeysList"] = cloudkms.post(
        "v1/{name}:decrypt",
        t.struct(
            {
                "name": t.string(),
                "additionalAuthenticatedDataCrc32c": t.string().optional(),
                "additionalAuthenticatedData": t.string().optional(),
                "ciphertextCrc32c": t.string().optional(),
                "ciphertext": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DecryptResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsCryptoKeysDecrypt"] = cloudkms.post(
        "v1/{name}:decrypt",
        t.struct(
            {
                "name": t.string(),
                "additionalAuthenticatedDataCrc32c": t.string().optional(),
                "additionalAuthenticatedData": t.string().optional(),
                "ciphertextCrc32c": t.string().optional(),
                "ciphertext": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DecryptResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsKeyRingsCryptoKeysCryptoKeyVersionsGetPublicKey"
    ] = cloudkms.post(
        "v1/{parent}/cryptoKeyVersions",
        t.struct(
            {
                "parent": t.string(),
                "state": t.string().optional(),
                "externalProtectionLevelOptions": t.proxy(
                    renames["ExternalProtectionLevelOptionsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CryptoKeyVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsKeyRingsCryptoKeysCryptoKeyVersionsMacVerify"
    ] = cloudkms.post(
        "v1/{parent}/cryptoKeyVersions",
        t.struct(
            {
                "parent": t.string(),
                "state": t.string().optional(),
                "externalProtectionLevelOptions": t.proxy(
                    renames["ExternalProtectionLevelOptionsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CryptoKeyVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsKeyRingsCryptoKeysCryptoKeyVersionsPatch"
    ] = cloudkms.post(
        "v1/{parent}/cryptoKeyVersions",
        t.struct(
            {
                "parent": t.string(),
                "state": t.string().optional(),
                "externalProtectionLevelOptions": t.proxy(
                    renames["ExternalProtectionLevelOptionsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CryptoKeyVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsKeyRingsCryptoKeysCryptoKeyVersionsDestroy"
    ] = cloudkms.post(
        "v1/{parent}/cryptoKeyVersions",
        t.struct(
            {
                "parent": t.string(),
                "state": t.string().optional(),
                "externalProtectionLevelOptions": t.proxy(
                    renames["ExternalProtectionLevelOptionsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CryptoKeyVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsKeyRingsCryptoKeysCryptoKeyVersionsAsymmetricDecrypt"
    ] = cloudkms.post(
        "v1/{parent}/cryptoKeyVersions",
        t.struct(
            {
                "parent": t.string(),
                "state": t.string().optional(),
                "externalProtectionLevelOptions": t.proxy(
                    renames["ExternalProtectionLevelOptionsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CryptoKeyVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsKeyRingsCryptoKeysCryptoKeyVersionsList"
    ] = cloudkms.post(
        "v1/{parent}/cryptoKeyVersions",
        t.struct(
            {
                "parent": t.string(),
                "state": t.string().optional(),
                "externalProtectionLevelOptions": t.proxy(
                    renames["ExternalProtectionLevelOptionsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CryptoKeyVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsKeyRingsCryptoKeysCryptoKeyVersionsAsymmetricSign"
    ] = cloudkms.post(
        "v1/{parent}/cryptoKeyVersions",
        t.struct(
            {
                "parent": t.string(),
                "state": t.string().optional(),
                "externalProtectionLevelOptions": t.proxy(
                    renames["ExternalProtectionLevelOptionsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CryptoKeyVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsKeyRingsCryptoKeysCryptoKeyVersionsMacSign"
    ] = cloudkms.post(
        "v1/{parent}/cryptoKeyVersions",
        t.struct(
            {
                "parent": t.string(),
                "state": t.string().optional(),
                "externalProtectionLevelOptions": t.proxy(
                    renames["ExternalProtectionLevelOptionsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CryptoKeyVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsKeyRingsCryptoKeysCryptoKeyVersionsImport"
    ] = cloudkms.post(
        "v1/{parent}/cryptoKeyVersions",
        t.struct(
            {
                "parent": t.string(),
                "state": t.string().optional(),
                "externalProtectionLevelOptions": t.proxy(
                    renames["ExternalProtectionLevelOptionsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CryptoKeyVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsKeyRingsCryptoKeysCryptoKeyVersionsGet"
    ] = cloudkms.post(
        "v1/{parent}/cryptoKeyVersions",
        t.struct(
            {
                "parent": t.string(),
                "state": t.string().optional(),
                "externalProtectionLevelOptions": t.proxy(
                    renames["ExternalProtectionLevelOptionsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CryptoKeyVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsKeyRingsCryptoKeysCryptoKeyVersionsRestore"
    ] = cloudkms.post(
        "v1/{parent}/cryptoKeyVersions",
        t.struct(
            {
                "parent": t.string(),
                "state": t.string().optional(),
                "externalProtectionLevelOptions": t.proxy(
                    renames["ExternalProtectionLevelOptionsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CryptoKeyVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsKeyRingsCryptoKeysCryptoKeyVersionsCreate"
    ] = cloudkms.post(
        "v1/{parent}/cryptoKeyVersions",
        t.struct(
            {
                "parent": t.string(),
                "state": t.string().optional(),
                "externalProtectionLevelOptions": t.proxy(
                    renames["ExternalProtectionLevelOptionsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CryptoKeyVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsImportJobsTestIamPermissions"] = cloudkms.post(
        "v1/{parent}/importJobs",
        t.struct(
            {
                "importJobId": t.string(),
                "parent": t.string(),
                "protectionLevel": t.string(),
                "importMethod": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ImportJobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsImportJobsSetIamPolicy"] = cloudkms.post(
        "v1/{parent}/importJobs",
        t.struct(
            {
                "importJobId": t.string(),
                "parent": t.string(),
                "protectionLevel": t.string(),
                "importMethod": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ImportJobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsImportJobsGet"] = cloudkms.post(
        "v1/{parent}/importJobs",
        t.struct(
            {
                "importJobId": t.string(),
                "parent": t.string(),
                "protectionLevel": t.string(),
                "importMethod": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ImportJobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsImportJobsList"] = cloudkms.post(
        "v1/{parent}/importJobs",
        t.struct(
            {
                "importJobId": t.string(),
                "parent": t.string(),
                "protectionLevel": t.string(),
                "importMethod": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ImportJobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsImportJobsGetIamPolicy"] = cloudkms.post(
        "v1/{parent}/importJobs",
        t.struct(
            {
                "importJobId": t.string(),
                "parent": t.string(),
                "protectionLevel": t.string(),
                "importMethod": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ImportJobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsImportJobsCreate"] = cloudkms.post(
        "v1/{parent}/importJobs",
        t.struct(
            {
                "importJobId": t.string(),
                "parent": t.string(),
                "protectionLevel": t.string(),
                "importMethod": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ImportJobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEkmConfigTestIamPermissions"] = cloudkms.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEkmConfigGetIamPolicy"] = cloudkms.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEkmConfigSetIamPolicy"] = cloudkms.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="cloudkms", renames=renames, types=Box(types), functions=Box(functions)
    )
