from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_cloudkms() -> Import:
    cloudkms = HTTPRuntime("https://cloudkms.googleapis.com/")

    renames = {
        "ErrorResponse": "_cloudkms_1_ErrorResponse",
        "DecryptResponseIn": "_cloudkms_2_DecryptResponseIn",
        "DecryptResponseOut": "_cloudkms_3_DecryptResponseOut",
        "ListLocationsResponseIn": "_cloudkms_4_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_cloudkms_5_ListLocationsResponseOut",
        "KeyOperationAttestationIn": "_cloudkms_6_KeyOperationAttestationIn",
        "KeyOperationAttestationOut": "_cloudkms_7_KeyOperationAttestationOut",
        "ImportJobIn": "_cloudkms_8_ImportJobIn",
        "ImportJobOut": "_cloudkms_9_ImportJobOut",
        "EkmConfigIn": "_cloudkms_10_EkmConfigIn",
        "EkmConfigOut": "_cloudkms_11_EkmConfigOut",
        "CertificateIn": "_cloudkms_12_CertificateIn",
        "CertificateOut": "_cloudkms_13_CertificateOut",
        "LocationMetadataIn": "_cloudkms_14_LocationMetadataIn",
        "LocationMetadataOut": "_cloudkms_15_LocationMetadataOut",
        "CryptoKeyIn": "_cloudkms_16_CryptoKeyIn",
        "CryptoKeyOut": "_cloudkms_17_CryptoKeyOut",
        "EncryptRequestIn": "_cloudkms_18_EncryptRequestIn",
        "EncryptRequestOut": "_cloudkms_19_EncryptRequestOut",
        "MacVerifyResponseIn": "_cloudkms_20_MacVerifyResponseIn",
        "MacVerifyResponseOut": "_cloudkms_21_MacVerifyResponseOut",
        "ExternalProtectionLevelOptionsIn": "_cloudkms_22_ExternalProtectionLevelOptionsIn",
        "ExternalProtectionLevelOptionsOut": "_cloudkms_23_ExternalProtectionLevelOptionsOut",
        "CryptoKeyVersionIn": "_cloudkms_24_CryptoKeyVersionIn",
        "CryptoKeyVersionOut": "_cloudkms_25_CryptoKeyVersionOut",
        "AsymmetricSignResponseIn": "_cloudkms_26_AsymmetricSignResponseIn",
        "AsymmetricSignResponseOut": "_cloudkms_27_AsymmetricSignResponseOut",
        "DecryptRequestIn": "_cloudkms_28_DecryptRequestIn",
        "DecryptRequestOut": "_cloudkms_29_DecryptRequestOut",
        "ListImportJobsResponseIn": "_cloudkms_30_ListImportJobsResponseIn",
        "ListImportJobsResponseOut": "_cloudkms_31_ListImportJobsResponseOut",
        "LocationIn": "_cloudkms_32_LocationIn",
        "LocationOut": "_cloudkms_33_LocationOut",
        "CryptoKeyVersionTemplateIn": "_cloudkms_34_CryptoKeyVersionTemplateIn",
        "CryptoKeyVersionTemplateOut": "_cloudkms_35_CryptoKeyVersionTemplateOut",
        "AuditLogConfigIn": "_cloudkms_36_AuditLogConfigIn",
        "AuditLogConfigOut": "_cloudkms_37_AuditLogConfigOut",
        "DigestIn": "_cloudkms_38_DigestIn",
        "DigestOut": "_cloudkms_39_DigestOut",
        "ExprIn": "_cloudkms_40_ExprIn",
        "ExprOut": "_cloudkms_41_ExprOut",
        "PolicyIn": "_cloudkms_42_PolicyIn",
        "PolicyOut": "_cloudkms_43_PolicyOut",
        "TestIamPermissionsResponseIn": "_cloudkms_44_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_cloudkms_45_TestIamPermissionsResponseOut",
        "AsymmetricDecryptRequestIn": "_cloudkms_46_AsymmetricDecryptRequestIn",
        "AsymmetricDecryptRequestOut": "_cloudkms_47_AsymmetricDecryptRequestOut",
        "WrappingPublicKeyIn": "_cloudkms_48_WrappingPublicKeyIn",
        "WrappingPublicKeyOut": "_cloudkms_49_WrappingPublicKeyOut",
        "AsymmetricSignRequestIn": "_cloudkms_50_AsymmetricSignRequestIn",
        "AsymmetricSignRequestOut": "_cloudkms_51_AsymmetricSignRequestOut",
        "UpdateCryptoKeyPrimaryVersionRequestIn": "_cloudkms_52_UpdateCryptoKeyPrimaryVersionRequestIn",
        "UpdateCryptoKeyPrimaryVersionRequestOut": "_cloudkms_53_UpdateCryptoKeyPrimaryVersionRequestOut",
        "PublicKeyIn": "_cloudkms_54_PublicKeyIn",
        "PublicKeyOut": "_cloudkms_55_PublicKeyOut",
        "KeyRingIn": "_cloudkms_56_KeyRingIn",
        "KeyRingOut": "_cloudkms_57_KeyRingOut",
        "MacSignRequestIn": "_cloudkms_58_MacSignRequestIn",
        "MacSignRequestOut": "_cloudkms_59_MacSignRequestOut",
        "EkmConnectionIn": "_cloudkms_60_EkmConnectionIn",
        "EkmConnectionOut": "_cloudkms_61_EkmConnectionOut",
        "AsymmetricDecryptResponseIn": "_cloudkms_62_AsymmetricDecryptResponseIn",
        "AsymmetricDecryptResponseOut": "_cloudkms_63_AsymmetricDecryptResponseOut",
        "VerifyConnectivityResponseIn": "_cloudkms_64_VerifyConnectivityResponseIn",
        "VerifyConnectivityResponseOut": "_cloudkms_65_VerifyConnectivityResponseOut",
        "ListCryptoKeysResponseIn": "_cloudkms_66_ListCryptoKeysResponseIn",
        "ListCryptoKeysResponseOut": "_cloudkms_67_ListCryptoKeysResponseOut",
        "SetIamPolicyRequestIn": "_cloudkms_68_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_cloudkms_69_SetIamPolicyRequestOut",
        "RestoreCryptoKeyVersionRequestIn": "_cloudkms_70_RestoreCryptoKeyVersionRequestIn",
        "RestoreCryptoKeyVersionRequestOut": "_cloudkms_71_RestoreCryptoKeyVersionRequestOut",
        "EncryptResponseIn": "_cloudkms_72_EncryptResponseIn",
        "EncryptResponseOut": "_cloudkms_73_EncryptResponseOut",
        "DestroyCryptoKeyVersionRequestIn": "_cloudkms_74_DestroyCryptoKeyVersionRequestIn",
        "DestroyCryptoKeyVersionRequestOut": "_cloudkms_75_DestroyCryptoKeyVersionRequestOut",
        "ServiceResolverIn": "_cloudkms_76_ServiceResolverIn",
        "ServiceResolverOut": "_cloudkms_77_ServiceResolverOut",
        "BindingIn": "_cloudkms_78_BindingIn",
        "BindingOut": "_cloudkms_79_BindingOut",
        "MacVerifyRequestIn": "_cloudkms_80_MacVerifyRequestIn",
        "MacVerifyRequestOut": "_cloudkms_81_MacVerifyRequestOut",
        "ListKeyRingsResponseIn": "_cloudkms_82_ListKeyRingsResponseIn",
        "ListKeyRingsResponseOut": "_cloudkms_83_ListKeyRingsResponseOut",
        "ListEkmConnectionsResponseIn": "_cloudkms_84_ListEkmConnectionsResponseIn",
        "ListEkmConnectionsResponseOut": "_cloudkms_85_ListEkmConnectionsResponseOut",
        "AuditConfigIn": "_cloudkms_86_AuditConfigIn",
        "AuditConfigOut": "_cloudkms_87_AuditConfigOut",
        "CertificateChainsIn": "_cloudkms_88_CertificateChainsIn",
        "CertificateChainsOut": "_cloudkms_89_CertificateChainsOut",
        "ImportCryptoKeyVersionRequestIn": "_cloudkms_90_ImportCryptoKeyVersionRequestIn",
        "ImportCryptoKeyVersionRequestOut": "_cloudkms_91_ImportCryptoKeyVersionRequestOut",
        "GenerateRandomBytesRequestIn": "_cloudkms_92_GenerateRandomBytesRequestIn",
        "GenerateRandomBytesRequestOut": "_cloudkms_93_GenerateRandomBytesRequestOut",
        "MacSignResponseIn": "_cloudkms_94_MacSignResponseIn",
        "MacSignResponseOut": "_cloudkms_95_MacSignResponseOut",
        "TestIamPermissionsRequestIn": "_cloudkms_96_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_cloudkms_97_TestIamPermissionsRequestOut",
        "GenerateRandomBytesResponseIn": "_cloudkms_98_GenerateRandomBytesResponseIn",
        "GenerateRandomBytesResponseOut": "_cloudkms_99_GenerateRandomBytesResponseOut",
        "ListCryptoKeyVersionsResponseIn": "_cloudkms_100_ListCryptoKeyVersionsResponseIn",
        "ListCryptoKeyVersionsResponseOut": "_cloudkms_101_ListCryptoKeyVersionsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["DecryptResponseIn"] = t.struct(
        {
            "plaintextCrc32c": t.string().optional(),
            "usedPrimary": t.boolean().optional(),
            "protectionLevel": t.string().optional(),
            "plaintext": t.string().optional(),
        }
    ).named(renames["DecryptResponseIn"])
    types["DecryptResponseOut"] = t.struct(
        {
            "plaintextCrc32c": t.string().optional(),
            "usedPrimary": t.boolean().optional(),
            "protectionLevel": t.string().optional(),
            "plaintext": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DecryptResponseOut"])
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
    types["ImportJobIn"] = t.struct(
        {"protectionLevel": t.string(), "importMethod": t.string()}
    ).named(renames["ImportJobIn"])
    types["ImportJobOut"] = t.struct(
        {
            "state": t.string().optional(),
            "protectionLevel": t.string(),
            "generateTime": t.string().optional(),
            "name": t.string().optional(),
            "publicKey": t.proxy(renames["WrappingPublicKeyOut"]).optional(),
            "importMethod": t.string(),
            "attestation": t.proxy(renames["KeyOperationAttestationOut"]).optional(),
            "createTime": t.string().optional(),
            "expireTime": t.string().optional(),
            "expireEventTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportJobOut"])
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
    types["CertificateIn"] = t.struct({"rawDer": t.string()}).named(
        renames["CertificateIn"]
    )
    types["CertificateOut"] = t.struct(
        {
            "serialNumber": t.string().optional(),
            "subject": t.string().optional(),
            "issuer": t.string().optional(),
            "subjectAlternativeDnsNames": t.array(t.string()).optional(),
            "rawDer": t.string(),
            "notBeforeTime": t.string().optional(),
            "notAfterTime": t.string().optional(),
            "sha256Fingerprint": t.string().optional(),
            "parsed": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateOut"])
    types["LocationMetadataIn"] = t.struct(
        {"ekmAvailable": t.boolean().optional(), "hsmAvailable": t.boolean().optional()}
    ).named(renames["LocationMetadataIn"])
    types["LocationMetadataOut"] = t.struct(
        {
            "ekmAvailable": t.boolean().optional(),
            "hsmAvailable": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationMetadataOut"])
    types["CryptoKeyIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "nextRotationTime": t.string().optional(),
            "importOnly": t.boolean().optional(),
            "cryptoKeyBackend": t.string().optional(),
            "purpose": t.string().optional(),
            "rotationPeriod": t.string().optional(),
            "destroyScheduledDuration": t.string().optional(),
            "versionTemplate": t.proxy(
                renames["CryptoKeyVersionTemplateIn"]
            ).optional(),
        }
    ).named(renames["CryptoKeyIn"])
    types["CryptoKeyOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "nextRotationTime": t.string().optional(),
            "importOnly": t.boolean().optional(),
            "cryptoKeyBackend": t.string().optional(),
            "purpose": t.string().optional(),
            "rotationPeriod": t.string().optional(),
            "primary": t.proxy(renames["CryptoKeyVersionOut"]).optional(),
            "createTime": t.string().optional(),
            "destroyScheduledDuration": t.string().optional(),
            "versionTemplate": t.proxy(
                renames["CryptoKeyVersionTemplateOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CryptoKeyOut"])
    types["EncryptRequestIn"] = t.struct(
        {
            "plaintext": t.string(),
            "additionalAuthenticatedData": t.string().optional(),
            "additionalAuthenticatedDataCrc32c": t.string().optional(),
            "plaintextCrc32c": t.string().optional(),
        }
    ).named(renames["EncryptRequestIn"])
    types["EncryptRequestOut"] = t.struct(
        {
            "plaintext": t.string(),
            "additionalAuthenticatedData": t.string().optional(),
            "additionalAuthenticatedDataCrc32c": t.string().optional(),
            "plaintextCrc32c": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EncryptRequestOut"])
    types["MacVerifyResponseIn"] = t.struct(
        {
            "name": t.string().optional(),
            "success": t.boolean().optional(),
            "protectionLevel": t.string().optional(),
            "verifiedSuccessIntegrity": t.boolean().optional(),
            "verifiedDataCrc32c": t.boolean().optional(),
            "verifiedMacCrc32c": t.boolean().optional(),
        }
    ).named(renames["MacVerifyResponseIn"])
    types["MacVerifyResponseOut"] = t.struct(
        {
            "name": t.string().optional(),
            "success": t.boolean().optional(),
            "protectionLevel": t.string().optional(),
            "verifiedSuccessIntegrity": t.boolean().optional(),
            "verifiedDataCrc32c": t.boolean().optional(),
            "verifiedMacCrc32c": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MacVerifyResponseOut"])
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
            "protectionLevel": t.string().optional(),
            "state": t.string().optional(),
            "attestation": t.proxy(renames["KeyOperationAttestationOut"]).optional(),
            "createTime": t.string().optional(),
            "generationFailureReason": t.string().optional(),
            "externalDestructionFailureReason": t.string().optional(),
            "generateTime": t.string().optional(),
            "externalProtectionLevelOptions": t.proxy(
                renames["ExternalProtectionLevelOptionsOut"]
            ).optional(),
            "destroyTime": t.string().optional(),
            "importFailureReason": t.string().optional(),
            "algorithm": t.string().optional(),
            "importTime": t.string().optional(),
            "name": t.string().optional(),
            "destroyEventTime": t.string().optional(),
            "importJob": t.string().optional(),
            "reimportEligible": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CryptoKeyVersionOut"])
    types["AsymmetricSignResponseIn"] = t.struct(
        {
            "protectionLevel": t.string().optional(),
            "signatureCrc32c": t.string().optional(),
            "verifiedDataCrc32c": t.boolean().optional(),
            "name": t.string().optional(),
            "signature": t.string().optional(),
            "verifiedDigestCrc32c": t.boolean().optional(),
        }
    ).named(renames["AsymmetricSignResponseIn"])
    types["AsymmetricSignResponseOut"] = t.struct(
        {
            "protectionLevel": t.string().optional(),
            "signatureCrc32c": t.string().optional(),
            "verifiedDataCrc32c": t.boolean().optional(),
            "name": t.string().optional(),
            "signature": t.string().optional(),
            "verifiedDigestCrc32c": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AsymmetricSignResponseOut"])
    types["DecryptRequestIn"] = t.struct(
        {
            "additionalAuthenticatedData": t.string().optional(),
            "ciphertextCrc32c": t.string().optional(),
            "additionalAuthenticatedDataCrc32c": t.string().optional(),
            "ciphertext": t.string(),
        }
    ).named(renames["DecryptRequestIn"])
    types["DecryptRequestOut"] = t.struct(
        {
            "additionalAuthenticatedData": t.string().optional(),
            "ciphertextCrc32c": t.string().optional(),
            "additionalAuthenticatedDataCrc32c": t.string().optional(),
            "ciphertext": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DecryptRequestOut"])
    types["ListImportJobsResponseIn"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "importJobs": t.array(t.proxy(renames["ImportJobIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListImportJobsResponseIn"])
    types["ListImportJobsResponseOut"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "importJobs": t.array(t.proxy(renames["ImportJobOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListImportJobsResponseOut"])
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
    types["CryptoKeyVersionTemplateIn"] = t.struct(
        {"algorithm": t.string(), "protectionLevel": t.string().optional()}
    ).named(renames["CryptoKeyVersionTemplateIn"])
    types["CryptoKeyVersionTemplateOut"] = t.struct(
        {
            "algorithm": t.string(),
            "protectionLevel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CryptoKeyVersionTemplateOut"])
    types["AuditLogConfigIn"] = t.struct(
        {
            "exemptedMembers": t.array(t.string()).optional(),
            "logType": t.string().optional(),
        }
    ).named(renames["AuditLogConfigIn"])
    types["AuditLogConfigOut"] = t.struct(
        {
            "exemptedMembers": t.array(t.string()).optional(),
            "logType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditLogConfigOut"])
    types["DigestIn"] = t.struct(
        {
            "sha256": t.string().optional(),
            "sha384": t.string().optional(),
            "sha512": t.string().optional(),
        }
    ).named(renames["DigestIn"])
    types["DigestOut"] = t.struct(
        {
            "sha256": t.string().optional(),
            "sha384": t.string().optional(),
            "sha512": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DigestOut"])
    types["ExprIn"] = t.struct(
        {
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["PolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "version": t.integer().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "version": t.integer().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
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
    types["WrappingPublicKeyIn"] = t.struct({"pem": t.string().optional()}).named(
        renames["WrappingPublicKeyIn"]
    )
    types["WrappingPublicKeyOut"] = t.struct(
        {
            "pem": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WrappingPublicKeyOut"])
    types["AsymmetricSignRequestIn"] = t.struct(
        {
            "digest": t.proxy(renames["DigestIn"]).optional(),
            "dataCrc32c": t.string().optional(),
            "digestCrc32c": t.string().optional(),
            "data": t.string().optional(),
        }
    ).named(renames["AsymmetricSignRequestIn"])
    types["AsymmetricSignRequestOut"] = t.struct(
        {
            "digest": t.proxy(renames["DigestOut"]).optional(),
            "dataCrc32c": t.string().optional(),
            "digestCrc32c": t.string().optional(),
            "data": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AsymmetricSignRequestOut"])
    types["UpdateCryptoKeyPrimaryVersionRequestIn"] = t.struct(
        {"cryptoKeyVersionId": t.string()}
    ).named(renames["UpdateCryptoKeyPrimaryVersionRequestIn"])
    types["UpdateCryptoKeyPrimaryVersionRequestOut"] = t.struct(
        {
            "cryptoKeyVersionId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateCryptoKeyPrimaryVersionRequestOut"])
    types["PublicKeyIn"] = t.struct(
        {
            "name": t.string().optional(),
            "pemCrc32c": t.string().optional(),
            "protectionLevel": t.string().optional(),
            "pem": t.string().optional(),
            "algorithm": t.string().optional(),
        }
    ).named(renames["PublicKeyIn"])
    types["PublicKeyOut"] = t.struct(
        {
            "name": t.string().optional(),
            "pemCrc32c": t.string().optional(),
            "protectionLevel": t.string().optional(),
            "pem": t.string().optional(),
            "algorithm": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublicKeyOut"])
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
    types["EkmConnectionIn"] = t.struct(
        {
            "cryptoSpacePath": t.string().optional(),
            "serviceResolvers": t.array(
                t.proxy(renames["ServiceResolverIn"])
            ).optional(),
            "etag": t.string().optional(),
            "keyManagementMode": t.string().optional(),
        }
    ).named(renames["EkmConnectionIn"])
    types["EkmConnectionOut"] = t.struct(
        {
            "name": t.string().optional(),
            "cryptoSpacePath": t.string().optional(),
            "serviceResolvers": t.array(
                t.proxy(renames["ServiceResolverOut"])
            ).optional(),
            "createTime": t.string().optional(),
            "etag": t.string().optional(),
            "keyManagementMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EkmConnectionOut"])
    types["AsymmetricDecryptResponseIn"] = t.struct(
        {
            "plaintextCrc32c": t.string().optional(),
            "protectionLevel": t.string().optional(),
            "verifiedCiphertextCrc32c": t.boolean().optional(),
            "plaintext": t.string().optional(),
        }
    ).named(renames["AsymmetricDecryptResponseIn"])
    types["AsymmetricDecryptResponseOut"] = t.struct(
        {
            "plaintextCrc32c": t.string().optional(),
            "protectionLevel": t.string().optional(),
            "verifiedCiphertextCrc32c": t.boolean().optional(),
            "plaintext": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AsymmetricDecryptResponseOut"])
    types["VerifyConnectivityResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["VerifyConnectivityResponseIn"])
    types["VerifyConnectivityResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["VerifyConnectivityResponseOut"])
    types["ListCryptoKeysResponseIn"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "cryptoKeys": t.array(t.proxy(renames["CryptoKeyIn"])).optional(),
        }
    ).named(renames["ListCryptoKeysResponseIn"])
    types["ListCryptoKeysResponseOut"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "cryptoKeys": t.array(t.proxy(renames["CryptoKeyOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCryptoKeysResponseOut"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "policy": t.proxy(renames["PolicyIn"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
    types["RestoreCryptoKeyVersionRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["RestoreCryptoKeyVersionRequestIn"])
    types["RestoreCryptoKeyVersionRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RestoreCryptoKeyVersionRequestOut"])
    types["EncryptResponseIn"] = t.struct(
        {
            "verifiedAdditionalAuthenticatedDataCrc32c": t.boolean().optional(),
            "protectionLevel": t.string().optional(),
            "ciphertext": t.string().optional(),
            "ciphertextCrc32c": t.string().optional(),
            "name": t.string().optional(),
            "verifiedPlaintextCrc32c": t.boolean().optional(),
        }
    ).named(renames["EncryptResponseIn"])
    types["EncryptResponseOut"] = t.struct(
        {
            "verifiedAdditionalAuthenticatedDataCrc32c": t.boolean().optional(),
            "protectionLevel": t.string().optional(),
            "ciphertext": t.string().optional(),
            "ciphertextCrc32c": t.string().optional(),
            "name": t.string().optional(),
            "verifiedPlaintextCrc32c": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EncryptResponseOut"])
    types["DestroyCryptoKeyVersionRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DestroyCryptoKeyVersionRequestIn"])
    types["DestroyCryptoKeyVersionRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DestroyCryptoKeyVersionRequestOut"])
    types["ServiceResolverIn"] = t.struct(
        {
            "serviceDirectoryService": t.string(),
            "endpointFilter": t.string().optional(),
            "serverCertificates": t.array(t.proxy(renames["CertificateIn"])),
            "hostname": t.string(),
        }
    ).named(renames["ServiceResolverIn"])
    types["ServiceResolverOut"] = t.struct(
        {
            "serviceDirectoryService": t.string(),
            "endpointFilter": t.string().optional(),
            "serverCertificates": t.array(t.proxy(renames["CertificateOut"])),
            "hostname": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceResolverOut"])
    types["BindingIn"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "role": t.string().optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["MacVerifyRequestIn"] = t.struct(
        {
            "macCrc32c": t.string().optional(),
            "dataCrc32c": t.string().optional(),
            "mac": t.string(),
            "data": t.string(),
        }
    ).named(renames["MacVerifyRequestIn"])
    types["MacVerifyRequestOut"] = t.struct(
        {
            "macCrc32c": t.string().optional(),
            "dataCrc32c": t.string().optional(),
            "mac": t.string(),
            "data": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MacVerifyRequestOut"])
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
    types["ListEkmConnectionsResponseIn"] = t.struct(
        {
            "ekmConnections": t.array(t.proxy(renames["EkmConnectionIn"])).optional(),
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListEkmConnectionsResponseIn"])
    types["ListEkmConnectionsResponseOut"] = t.struct(
        {
            "ekmConnections": t.array(t.proxy(renames["EkmConnectionOut"])).optional(),
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListEkmConnectionsResponseOut"])
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
    types["CertificateChainsIn"] = t.struct(
        {
            "googleCardCerts": t.array(t.string()).optional(),
            "googlePartitionCerts": t.array(t.string()).optional(),
            "caviumCerts": t.array(t.string()).optional(),
        }
    ).named(renames["CertificateChainsIn"])
    types["CertificateChainsOut"] = t.struct(
        {
            "googleCardCerts": t.array(t.string()).optional(),
            "googlePartitionCerts": t.array(t.string()).optional(),
            "caviumCerts": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateChainsOut"])
    types["ImportCryptoKeyVersionRequestIn"] = t.struct(
        {
            "importJob": t.string(),
            "algorithm": t.string(),
            "rsaAesWrappedKey": t.string().optional(),
            "cryptoKeyVersion": t.string().optional(),
            "wrappedKey": t.string().optional(),
        }
    ).named(renames["ImportCryptoKeyVersionRequestIn"])
    types["ImportCryptoKeyVersionRequestOut"] = t.struct(
        {
            "importJob": t.string(),
            "algorithm": t.string(),
            "rsaAesWrappedKey": t.string().optional(),
            "cryptoKeyVersion": t.string().optional(),
            "wrappedKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportCryptoKeyVersionRequestOut"])
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
    types["MacSignResponseIn"] = t.struct(
        {
            "protectionLevel": t.string().optional(),
            "name": t.string().optional(),
            "macCrc32c": t.string().optional(),
            "verifiedDataCrc32c": t.boolean().optional(),
            "mac": t.string().optional(),
        }
    ).named(renames["MacSignResponseIn"])
    types["MacSignResponseOut"] = t.struct(
        {
            "protectionLevel": t.string().optional(),
            "name": t.string().optional(),
            "macCrc32c": t.string().optional(),
            "verifiedDataCrc32c": t.boolean().optional(),
            "mac": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MacSignResponseOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
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
    types["ListCryptoKeyVersionsResponseIn"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "cryptoKeyVersions": t.array(
                t.proxy(renames["CryptoKeyVersionIn"])
            ).optional(),
        }
    ).named(renames["ListCryptoKeyVersionsResponseIn"])
    types["ListCryptoKeyVersionsResponseOut"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "cryptoKeyVersions": t.array(
                t.proxy(renames["CryptoKeyVersionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCryptoKeyVersionsResponseOut"])

    functions = {}
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
    functions["projectsLocationsKeyRingsCryptoKeysUpdatePrimaryVersion"] = cloudkms.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CryptoKeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsCryptoKeysPatch"] = cloudkms.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CryptoKeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsCryptoKeysSetIamPolicy"] = cloudkms.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CryptoKeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsCryptoKeysTestIamPermissions"] = cloudkms.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CryptoKeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsCryptoKeysDecrypt"] = cloudkms.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CryptoKeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsCryptoKeysList"] = cloudkms.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CryptoKeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsCryptoKeysEncrypt"] = cloudkms.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CryptoKeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsCryptoKeysGetIamPolicy"] = cloudkms.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CryptoKeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsCryptoKeysCreate"] = cloudkms.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CryptoKeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsCryptoKeysGet"] = cloudkms.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CryptoKeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsKeyRingsCryptoKeysCryptoKeyVersionsMacSign"
    ] = cloudkms.post(
        "v1/{parent}/cryptoKeyVersions:import",
        t.struct(
            {
                "parent": t.string(),
                "importJob": t.string(),
                "algorithm": t.string(),
                "rsaAesWrappedKey": t.string().optional(),
                "cryptoKeyVersion": t.string().optional(),
                "wrappedKey": t.string().optional(),
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
        "v1/{parent}/cryptoKeyVersions:import",
        t.struct(
            {
                "parent": t.string(),
                "importJob": t.string(),
                "algorithm": t.string(),
                "rsaAesWrappedKey": t.string().optional(),
                "cryptoKeyVersion": t.string().optional(),
                "wrappedKey": t.string().optional(),
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
        "v1/{parent}/cryptoKeyVersions:import",
        t.struct(
            {
                "parent": t.string(),
                "importJob": t.string(),
                "algorithm": t.string(),
                "rsaAesWrappedKey": t.string().optional(),
                "cryptoKeyVersion": t.string().optional(),
                "wrappedKey": t.string().optional(),
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
        "v1/{parent}/cryptoKeyVersions:import",
        t.struct(
            {
                "parent": t.string(),
                "importJob": t.string(),
                "algorithm": t.string(),
                "rsaAesWrappedKey": t.string().optional(),
                "cryptoKeyVersion": t.string().optional(),
                "wrappedKey": t.string().optional(),
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
        "v1/{parent}/cryptoKeyVersions:import",
        t.struct(
            {
                "parent": t.string(),
                "importJob": t.string(),
                "algorithm": t.string(),
                "rsaAesWrappedKey": t.string().optional(),
                "cryptoKeyVersion": t.string().optional(),
                "wrappedKey": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CryptoKeyVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsKeyRingsCryptoKeysCryptoKeyVersionsGetPublicKey"
    ] = cloudkms.post(
        "v1/{parent}/cryptoKeyVersions:import",
        t.struct(
            {
                "parent": t.string(),
                "importJob": t.string(),
                "algorithm": t.string(),
                "rsaAesWrappedKey": t.string().optional(),
                "cryptoKeyVersion": t.string().optional(),
                "wrappedKey": t.string().optional(),
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
        "v1/{parent}/cryptoKeyVersions:import",
        t.struct(
            {
                "parent": t.string(),
                "importJob": t.string(),
                "algorithm": t.string(),
                "rsaAesWrappedKey": t.string().optional(),
                "cryptoKeyVersion": t.string().optional(),
                "wrappedKey": t.string().optional(),
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
        "v1/{parent}/cryptoKeyVersions:import",
        t.struct(
            {
                "parent": t.string(),
                "importJob": t.string(),
                "algorithm": t.string(),
                "rsaAesWrappedKey": t.string().optional(),
                "cryptoKeyVersion": t.string().optional(),
                "wrappedKey": t.string().optional(),
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
        "v1/{parent}/cryptoKeyVersions:import",
        t.struct(
            {
                "parent": t.string(),
                "importJob": t.string(),
                "algorithm": t.string(),
                "rsaAesWrappedKey": t.string().optional(),
                "cryptoKeyVersion": t.string().optional(),
                "wrappedKey": t.string().optional(),
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
        "v1/{parent}/cryptoKeyVersions:import",
        t.struct(
            {
                "parent": t.string(),
                "importJob": t.string(),
                "algorithm": t.string(),
                "rsaAesWrappedKey": t.string().optional(),
                "cryptoKeyVersion": t.string().optional(),
                "wrappedKey": t.string().optional(),
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
        "v1/{parent}/cryptoKeyVersions:import",
        t.struct(
            {
                "parent": t.string(),
                "importJob": t.string(),
                "algorithm": t.string(),
                "rsaAesWrappedKey": t.string().optional(),
                "cryptoKeyVersion": t.string().optional(),
                "wrappedKey": t.string().optional(),
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
        "v1/{parent}/cryptoKeyVersions:import",
        t.struct(
            {
                "parent": t.string(),
                "importJob": t.string(),
                "algorithm": t.string(),
                "rsaAesWrappedKey": t.string().optional(),
                "cryptoKeyVersion": t.string().optional(),
                "wrappedKey": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CryptoKeyVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsImportJobsList"] = cloudkms.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsImportJobsGetIamPolicy"] = cloudkms.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsImportJobsGet"] = cloudkms.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsImportJobsCreate"] = cloudkms.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsImportJobsTestIamPermissions"] = cloudkms.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsImportJobsSetIamPolicy"] = cloudkms.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEkmConnectionsPatch"] = cloudkms.post(
        "v1/{parent}/ekmConnections",
        t.struct(
            {
                "ekmConnectionId": t.string(),
                "parent": t.string(),
                "cryptoSpacePath": t.string().optional(),
                "serviceResolvers": t.array(
                    t.proxy(renames["ServiceResolverIn"])
                ).optional(),
                "etag": t.string().optional(),
                "keyManagementMode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EkmConnectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEkmConnectionsList"] = cloudkms.post(
        "v1/{parent}/ekmConnections",
        t.struct(
            {
                "ekmConnectionId": t.string(),
                "parent": t.string(),
                "cryptoSpacePath": t.string().optional(),
                "serviceResolvers": t.array(
                    t.proxy(renames["ServiceResolverIn"])
                ).optional(),
                "etag": t.string().optional(),
                "keyManagementMode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EkmConnectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEkmConnectionsVerifyConnectivity"] = cloudkms.post(
        "v1/{parent}/ekmConnections",
        t.struct(
            {
                "ekmConnectionId": t.string(),
                "parent": t.string(),
                "cryptoSpacePath": t.string().optional(),
                "serviceResolvers": t.array(
                    t.proxy(renames["ServiceResolverIn"])
                ).optional(),
                "etag": t.string().optional(),
                "keyManagementMode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EkmConnectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEkmConnectionsGet"] = cloudkms.post(
        "v1/{parent}/ekmConnections",
        t.struct(
            {
                "ekmConnectionId": t.string(),
                "parent": t.string(),
                "cryptoSpacePath": t.string().optional(),
                "serviceResolvers": t.array(
                    t.proxy(renames["ServiceResolverIn"])
                ).optional(),
                "etag": t.string().optional(),
                "keyManagementMode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EkmConnectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEkmConnectionsSetIamPolicy"] = cloudkms.post(
        "v1/{parent}/ekmConnections",
        t.struct(
            {
                "ekmConnectionId": t.string(),
                "parent": t.string(),
                "cryptoSpacePath": t.string().optional(),
                "serviceResolvers": t.array(
                    t.proxy(renames["ServiceResolverIn"])
                ).optional(),
                "etag": t.string().optional(),
                "keyManagementMode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EkmConnectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEkmConnectionsGetIamPolicy"] = cloudkms.post(
        "v1/{parent}/ekmConnections",
        t.struct(
            {
                "ekmConnectionId": t.string(),
                "parent": t.string(),
                "cryptoSpacePath": t.string().optional(),
                "serviceResolvers": t.array(
                    t.proxy(renames["ServiceResolverIn"])
                ).optional(),
                "etag": t.string().optional(),
                "keyManagementMode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EkmConnectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEkmConnectionsTestIamPermissions"] = cloudkms.post(
        "v1/{parent}/ekmConnections",
        t.struct(
            {
                "ekmConnectionId": t.string(),
                "parent": t.string(),
                "cryptoSpacePath": t.string().optional(),
                "serviceResolvers": t.array(
                    t.proxy(renames["ServiceResolverIn"])
                ).optional(),
                "etag": t.string().optional(),
                "keyManagementMode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EkmConnectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEkmConnectionsCreate"] = cloudkms.post(
        "v1/{parent}/ekmConnections",
        t.struct(
            {
                "ekmConnectionId": t.string(),
                "parent": t.string(),
                "cryptoSpacePath": t.string().optional(),
                "serviceResolvers": t.array(
                    t.proxy(renames["ServiceResolverIn"])
                ).optional(),
                "etag": t.string().optional(),
                "keyManagementMode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EkmConnectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEkmConfigGetIamPolicy"] = cloudkms.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEkmConfigTestIamPermissions"] = cloudkms.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
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
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
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
