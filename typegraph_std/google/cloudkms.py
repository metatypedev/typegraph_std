from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_cloudkms() -> Import:
    cloudkms = HTTPRuntime("https://cloudkms.googleapis.com/")

    renames = {
        "ErrorResponse": "_cloudkms_1_ErrorResponse",
        "AsymmetricSignResponseIn": "_cloudkms_2_AsymmetricSignResponseIn",
        "AsymmetricSignResponseOut": "_cloudkms_3_AsymmetricSignResponseOut",
        "CertificateIn": "_cloudkms_4_CertificateIn",
        "CertificateOut": "_cloudkms_5_CertificateOut",
        "MacSignResponseIn": "_cloudkms_6_MacSignResponseIn",
        "MacSignResponseOut": "_cloudkms_7_MacSignResponseOut",
        "ExprIn": "_cloudkms_8_ExprIn",
        "ExprOut": "_cloudkms_9_ExprOut",
        "ListEkmConnectionsResponseIn": "_cloudkms_10_ListEkmConnectionsResponseIn",
        "ListEkmConnectionsResponseOut": "_cloudkms_11_ListEkmConnectionsResponseOut",
        "BindingIn": "_cloudkms_12_BindingIn",
        "BindingOut": "_cloudkms_13_BindingOut",
        "UpdateCryptoKeyPrimaryVersionRequestIn": "_cloudkms_14_UpdateCryptoKeyPrimaryVersionRequestIn",
        "UpdateCryptoKeyPrimaryVersionRequestOut": "_cloudkms_15_UpdateCryptoKeyPrimaryVersionRequestOut",
        "AuditLogConfigIn": "_cloudkms_16_AuditLogConfigIn",
        "AuditLogConfigOut": "_cloudkms_17_AuditLogConfigOut",
        "ServiceResolverIn": "_cloudkms_18_ServiceResolverIn",
        "ServiceResolverOut": "_cloudkms_19_ServiceResolverOut",
        "EncryptResponseIn": "_cloudkms_20_EncryptResponseIn",
        "EncryptResponseOut": "_cloudkms_21_EncryptResponseOut",
        "TestIamPermissionsResponseIn": "_cloudkms_22_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_cloudkms_23_TestIamPermissionsResponseOut",
        "DecryptRequestIn": "_cloudkms_24_DecryptRequestIn",
        "DecryptRequestOut": "_cloudkms_25_DecryptRequestOut",
        "CryptoKeyVersionTemplateIn": "_cloudkms_26_CryptoKeyVersionTemplateIn",
        "CryptoKeyVersionTemplateOut": "_cloudkms_27_CryptoKeyVersionTemplateOut",
        "ImportCryptoKeyVersionRequestIn": "_cloudkms_28_ImportCryptoKeyVersionRequestIn",
        "ImportCryptoKeyVersionRequestOut": "_cloudkms_29_ImportCryptoKeyVersionRequestOut",
        "AsymmetricDecryptRequestIn": "_cloudkms_30_AsymmetricDecryptRequestIn",
        "AsymmetricDecryptRequestOut": "_cloudkms_31_AsymmetricDecryptRequestOut",
        "GenerateRandomBytesRequestIn": "_cloudkms_32_GenerateRandomBytesRequestIn",
        "GenerateRandomBytesRequestOut": "_cloudkms_33_GenerateRandomBytesRequestOut",
        "PublicKeyIn": "_cloudkms_34_PublicKeyIn",
        "PublicKeyOut": "_cloudkms_35_PublicKeyOut",
        "MacSignRequestIn": "_cloudkms_36_MacSignRequestIn",
        "MacSignRequestOut": "_cloudkms_37_MacSignRequestOut",
        "CertificateChainsIn": "_cloudkms_38_CertificateChainsIn",
        "CertificateChainsOut": "_cloudkms_39_CertificateChainsOut",
        "CryptoKeyIn": "_cloudkms_40_CryptoKeyIn",
        "CryptoKeyOut": "_cloudkms_41_CryptoKeyOut",
        "ExternalProtectionLevelOptionsIn": "_cloudkms_42_ExternalProtectionLevelOptionsIn",
        "ExternalProtectionLevelOptionsOut": "_cloudkms_43_ExternalProtectionLevelOptionsOut",
        "ImportJobIn": "_cloudkms_44_ImportJobIn",
        "ImportJobOut": "_cloudkms_45_ImportJobOut",
        "ListCryptoKeysResponseIn": "_cloudkms_46_ListCryptoKeysResponseIn",
        "ListCryptoKeysResponseOut": "_cloudkms_47_ListCryptoKeysResponseOut",
        "EkmConnectionIn": "_cloudkms_48_EkmConnectionIn",
        "EkmConnectionOut": "_cloudkms_49_EkmConnectionOut",
        "AsymmetricDecryptResponseIn": "_cloudkms_50_AsymmetricDecryptResponseIn",
        "AsymmetricDecryptResponseOut": "_cloudkms_51_AsymmetricDecryptResponseOut",
        "DigestIn": "_cloudkms_52_DigestIn",
        "DigestOut": "_cloudkms_53_DigestOut",
        "EncryptRequestIn": "_cloudkms_54_EncryptRequestIn",
        "EncryptRequestOut": "_cloudkms_55_EncryptRequestOut",
        "ListCryptoKeyVersionsResponseIn": "_cloudkms_56_ListCryptoKeyVersionsResponseIn",
        "ListCryptoKeyVersionsResponseOut": "_cloudkms_57_ListCryptoKeyVersionsResponseOut",
        "LocationMetadataIn": "_cloudkms_58_LocationMetadataIn",
        "LocationMetadataOut": "_cloudkms_59_LocationMetadataOut",
        "RestoreCryptoKeyVersionRequestIn": "_cloudkms_60_RestoreCryptoKeyVersionRequestIn",
        "RestoreCryptoKeyVersionRequestOut": "_cloudkms_61_RestoreCryptoKeyVersionRequestOut",
        "PolicyIn": "_cloudkms_62_PolicyIn",
        "PolicyOut": "_cloudkms_63_PolicyOut",
        "GenerateRandomBytesResponseIn": "_cloudkms_64_GenerateRandomBytesResponseIn",
        "GenerateRandomBytesResponseOut": "_cloudkms_65_GenerateRandomBytesResponseOut",
        "WrappingPublicKeyIn": "_cloudkms_66_WrappingPublicKeyIn",
        "WrappingPublicKeyOut": "_cloudkms_67_WrappingPublicKeyOut",
        "SetIamPolicyRequestIn": "_cloudkms_68_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_cloudkms_69_SetIamPolicyRequestOut",
        "EkmConfigIn": "_cloudkms_70_EkmConfigIn",
        "EkmConfigOut": "_cloudkms_71_EkmConfigOut",
        "DestroyCryptoKeyVersionRequestIn": "_cloudkms_72_DestroyCryptoKeyVersionRequestIn",
        "DestroyCryptoKeyVersionRequestOut": "_cloudkms_73_DestroyCryptoKeyVersionRequestOut",
        "CryptoKeyVersionIn": "_cloudkms_74_CryptoKeyVersionIn",
        "CryptoKeyVersionOut": "_cloudkms_75_CryptoKeyVersionOut",
        "VerifyConnectivityResponseIn": "_cloudkms_76_VerifyConnectivityResponseIn",
        "VerifyConnectivityResponseOut": "_cloudkms_77_VerifyConnectivityResponseOut",
        "DecryptResponseIn": "_cloudkms_78_DecryptResponseIn",
        "DecryptResponseOut": "_cloudkms_79_DecryptResponseOut",
        "ListKeyRingsResponseIn": "_cloudkms_80_ListKeyRingsResponseIn",
        "ListKeyRingsResponseOut": "_cloudkms_81_ListKeyRingsResponseOut",
        "LocationIn": "_cloudkms_82_LocationIn",
        "LocationOut": "_cloudkms_83_LocationOut",
        "ListImportJobsResponseIn": "_cloudkms_84_ListImportJobsResponseIn",
        "ListImportJobsResponseOut": "_cloudkms_85_ListImportJobsResponseOut",
        "MacVerifyRequestIn": "_cloudkms_86_MacVerifyRequestIn",
        "MacVerifyRequestOut": "_cloudkms_87_MacVerifyRequestOut",
        "AuditConfigIn": "_cloudkms_88_AuditConfigIn",
        "AuditConfigOut": "_cloudkms_89_AuditConfigOut",
        "KeyRingIn": "_cloudkms_90_KeyRingIn",
        "KeyRingOut": "_cloudkms_91_KeyRingOut",
        "KeyOperationAttestationIn": "_cloudkms_92_KeyOperationAttestationIn",
        "KeyOperationAttestationOut": "_cloudkms_93_KeyOperationAttestationOut",
        "TestIamPermissionsRequestIn": "_cloudkms_94_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_cloudkms_95_TestIamPermissionsRequestOut",
        "AsymmetricSignRequestIn": "_cloudkms_96_AsymmetricSignRequestIn",
        "AsymmetricSignRequestOut": "_cloudkms_97_AsymmetricSignRequestOut",
        "ListLocationsResponseIn": "_cloudkms_98_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_cloudkms_99_ListLocationsResponseOut",
        "MacVerifyResponseIn": "_cloudkms_100_MacVerifyResponseIn",
        "MacVerifyResponseOut": "_cloudkms_101_MacVerifyResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["AsymmetricSignResponseIn"] = t.struct(
        {
            "verifiedDigestCrc32c": t.boolean().optional(),
            "signatureCrc32c": t.string().optional(),
            "signature": t.string().optional(),
            "name": t.string().optional(),
            "protectionLevel": t.string().optional(),
            "verifiedDataCrc32c": t.boolean().optional(),
        }
    ).named(renames["AsymmetricSignResponseIn"])
    types["AsymmetricSignResponseOut"] = t.struct(
        {
            "verifiedDigestCrc32c": t.boolean().optional(),
            "signatureCrc32c": t.string().optional(),
            "signature": t.string().optional(),
            "name": t.string().optional(),
            "protectionLevel": t.string().optional(),
            "verifiedDataCrc32c": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AsymmetricSignResponseOut"])
    types["CertificateIn"] = t.struct({"rawDer": t.string()}).named(
        renames["CertificateIn"]
    )
    types["CertificateOut"] = t.struct(
        {
            "issuer": t.string().optional(),
            "rawDer": t.string(),
            "sha256Fingerprint": t.string().optional(),
            "subject": t.string().optional(),
            "subjectAlternativeDnsNames": t.array(t.string()).optional(),
            "parsed": t.boolean().optional(),
            "notBeforeTime": t.string().optional(),
            "serialNumber": t.string().optional(),
            "notAfterTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateOut"])
    types["MacSignResponseIn"] = t.struct(
        {
            "name": t.string().optional(),
            "verifiedDataCrc32c": t.boolean().optional(),
            "macCrc32c": t.string().optional(),
            "protectionLevel": t.string().optional(),
            "mac": t.string().optional(),
        }
    ).named(renames["MacSignResponseIn"])
    types["MacSignResponseOut"] = t.struct(
        {
            "name": t.string().optional(),
            "verifiedDataCrc32c": t.boolean().optional(),
            "macCrc32c": t.string().optional(),
            "protectionLevel": t.string().optional(),
            "mac": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MacSignResponseOut"])
    types["ExprIn"] = t.struct(
        {
            "description": t.string().optional(),
            "title": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "description": t.string().optional(),
            "title": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["ListEkmConnectionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "ekmConnections": t.array(t.proxy(renames["EkmConnectionIn"])).optional(),
        }
    ).named(renames["ListEkmConnectionsResponseIn"])
    types["ListEkmConnectionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "ekmConnections": t.array(t.proxy(renames["EkmConnectionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListEkmConnectionsResponseOut"])
    types["BindingIn"] = t.struct(
        {
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "members": t.array(t.string()).optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "members": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["UpdateCryptoKeyPrimaryVersionRequestIn"] = t.struct(
        {"cryptoKeyVersionId": t.string()}
    ).named(renames["UpdateCryptoKeyPrimaryVersionRequestIn"])
    types["UpdateCryptoKeyPrimaryVersionRequestOut"] = t.struct(
        {
            "cryptoKeyVersionId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateCryptoKeyPrimaryVersionRequestOut"])
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
    types["ServiceResolverIn"] = t.struct(
        {
            "endpointFilter": t.string().optional(),
            "hostname": t.string(),
            "serviceDirectoryService": t.string(),
            "serverCertificates": t.array(t.proxy(renames["CertificateIn"])),
        }
    ).named(renames["ServiceResolverIn"])
    types["ServiceResolverOut"] = t.struct(
        {
            "endpointFilter": t.string().optional(),
            "hostname": t.string(),
            "serviceDirectoryService": t.string(),
            "serverCertificates": t.array(t.proxy(renames["CertificateOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceResolverOut"])
    types["EncryptResponseIn"] = t.struct(
        {
            "protectionLevel": t.string().optional(),
            "name": t.string().optional(),
            "verifiedAdditionalAuthenticatedDataCrc32c": t.boolean().optional(),
            "ciphertextCrc32c": t.string().optional(),
            "verifiedPlaintextCrc32c": t.boolean().optional(),
            "ciphertext": t.string().optional(),
        }
    ).named(renames["EncryptResponseIn"])
    types["EncryptResponseOut"] = t.struct(
        {
            "protectionLevel": t.string().optional(),
            "name": t.string().optional(),
            "verifiedAdditionalAuthenticatedDataCrc32c": t.boolean().optional(),
            "ciphertextCrc32c": t.string().optional(),
            "verifiedPlaintextCrc32c": t.boolean().optional(),
            "ciphertext": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EncryptResponseOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["DecryptRequestIn"] = t.struct(
        {
            "additionalAuthenticatedDataCrc32c": t.string().optional(),
            "additionalAuthenticatedData": t.string().optional(),
            "ciphertext": t.string(),
            "ciphertextCrc32c": t.string().optional(),
        }
    ).named(renames["DecryptRequestIn"])
    types["DecryptRequestOut"] = t.struct(
        {
            "additionalAuthenticatedDataCrc32c": t.string().optional(),
            "additionalAuthenticatedData": t.string().optional(),
            "ciphertext": t.string(),
            "ciphertextCrc32c": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DecryptRequestOut"])
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
    types["ImportCryptoKeyVersionRequestIn"] = t.struct(
        {
            "algorithm": t.string(),
            "rsaAesWrappedKey": t.string().optional(),
            "importJob": t.string(),
            "cryptoKeyVersion": t.string().optional(),
            "wrappedKey": t.string().optional(),
        }
    ).named(renames["ImportCryptoKeyVersionRequestIn"])
    types["ImportCryptoKeyVersionRequestOut"] = t.struct(
        {
            "algorithm": t.string(),
            "rsaAesWrappedKey": t.string().optional(),
            "importJob": t.string(),
            "cryptoKeyVersion": t.string().optional(),
            "wrappedKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportCryptoKeyVersionRequestOut"])
    types["AsymmetricDecryptRequestIn"] = t.struct(
        {"ciphertextCrc32c": t.string().optional(), "ciphertext": t.string()}
    ).named(renames["AsymmetricDecryptRequestIn"])
    types["AsymmetricDecryptRequestOut"] = t.struct(
        {
            "ciphertextCrc32c": t.string().optional(),
            "ciphertext": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AsymmetricDecryptRequestOut"])
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
    types["PublicKeyIn"] = t.struct(
        {
            "protectionLevel": t.string().optional(),
            "algorithm": t.string().optional(),
            "name": t.string().optional(),
            "pem": t.string().optional(),
            "pemCrc32c": t.string().optional(),
        }
    ).named(renames["PublicKeyIn"])
    types["PublicKeyOut"] = t.struct(
        {
            "protectionLevel": t.string().optional(),
            "algorithm": t.string().optional(),
            "name": t.string().optional(),
            "pem": t.string().optional(),
            "pemCrc32c": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublicKeyOut"])
    types["MacSignRequestIn"] = t.struct(
        {"data": t.string(), "dataCrc32c": t.string().optional()}
    ).named(renames["MacSignRequestIn"])
    types["MacSignRequestOut"] = t.struct(
        {
            "data": t.string(),
            "dataCrc32c": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MacSignRequestOut"])
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
    types["CryptoKeyIn"] = t.struct(
        {
            "importOnly": t.boolean().optional(),
            "versionTemplate": t.proxy(
                renames["CryptoKeyVersionTemplateIn"]
            ).optional(),
            "destroyScheduledDuration": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "purpose": t.string().optional(),
            "rotationPeriod": t.string().optional(),
            "nextRotationTime": t.string().optional(),
            "cryptoKeyBackend": t.string().optional(),
        }
    ).named(renames["CryptoKeyIn"])
    types["CryptoKeyOut"] = t.struct(
        {
            "importOnly": t.boolean().optional(),
            "versionTemplate": t.proxy(
                renames["CryptoKeyVersionTemplateOut"]
            ).optional(),
            "destroyScheduledDuration": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "purpose": t.string().optional(),
            "rotationPeriod": t.string().optional(),
            "name": t.string().optional(),
            "nextRotationTime": t.string().optional(),
            "cryptoKeyBackend": t.string().optional(),
            "primary": t.proxy(renames["CryptoKeyVersionOut"]).optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CryptoKeyOut"])
    types["ExternalProtectionLevelOptionsIn"] = t.struct(
        {
            "externalKeyUri": t.string().optional(),
            "ekmConnectionKeyPath": t.string().optional(),
        }
    ).named(renames["ExternalProtectionLevelOptionsIn"])
    types["ExternalProtectionLevelOptionsOut"] = t.struct(
        {
            "externalKeyUri": t.string().optional(),
            "ekmConnectionKeyPath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExternalProtectionLevelOptionsOut"])
    types["ImportJobIn"] = t.struct(
        {"importMethod": t.string(), "protectionLevel": t.string()}
    ).named(renames["ImportJobIn"])
    types["ImportJobOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "expireTime": t.string().optional(),
            "state": t.string().optional(),
            "importMethod": t.string(),
            "publicKey": t.proxy(renames["WrappingPublicKeyOut"]).optional(),
            "name": t.string().optional(),
            "attestation": t.proxy(renames["KeyOperationAttestationOut"]).optional(),
            "protectionLevel": t.string(),
            "generateTime": t.string().optional(),
            "expireEventTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportJobOut"])
    types["ListCryptoKeysResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "cryptoKeys": t.array(t.proxy(renames["CryptoKeyIn"])).optional(),
            "totalSize": t.integer().optional(),
        }
    ).named(renames["ListCryptoKeysResponseIn"])
    types["ListCryptoKeysResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "cryptoKeys": t.array(t.proxy(renames["CryptoKeyOut"])).optional(),
            "totalSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCryptoKeysResponseOut"])
    types["EkmConnectionIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "cryptoSpacePath": t.string().optional(),
            "serviceResolvers": t.array(
                t.proxy(renames["ServiceResolverIn"])
            ).optional(),
            "keyManagementMode": t.string().optional(),
        }
    ).named(renames["EkmConnectionIn"])
    types["EkmConnectionOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "cryptoSpacePath": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "serviceResolvers": t.array(
                t.proxy(renames["ServiceResolverOut"])
            ).optional(),
            "keyManagementMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EkmConnectionOut"])
    types["AsymmetricDecryptResponseIn"] = t.struct(
        {
            "plaintext": t.string().optional(),
            "verifiedCiphertextCrc32c": t.boolean().optional(),
            "protectionLevel": t.string().optional(),
            "plaintextCrc32c": t.string().optional(),
        }
    ).named(renames["AsymmetricDecryptResponseIn"])
    types["AsymmetricDecryptResponseOut"] = t.struct(
        {
            "plaintext": t.string().optional(),
            "verifiedCiphertextCrc32c": t.boolean().optional(),
            "protectionLevel": t.string().optional(),
            "plaintextCrc32c": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AsymmetricDecryptResponseOut"])
    types["DigestIn"] = t.struct(
        {
            "sha512": t.string().optional(),
            "sha256": t.string().optional(),
            "sha384": t.string().optional(),
        }
    ).named(renames["DigestIn"])
    types["DigestOut"] = t.struct(
        {
            "sha512": t.string().optional(),
            "sha256": t.string().optional(),
            "sha384": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DigestOut"])
    types["EncryptRequestIn"] = t.struct(
        {
            "additionalAuthenticatedData": t.string().optional(),
            "plaintext": t.string(),
            "plaintextCrc32c": t.string().optional(),
            "additionalAuthenticatedDataCrc32c": t.string().optional(),
        }
    ).named(renames["EncryptRequestIn"])
    types["EncryptRequestOut"] = t.struct(
        {
            "additionalAuthenticatedData": t.string().optional(),
            "plaintext": t.string(),
            "plaintextCrc32c": t.string().optional(),
            "additionalAuthenticatedDataCrc32c": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EncryptRequestOut"])
    types["ListCryptoKeyVersionsResponseIn"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "cryptoKeyVersions": t.array(
                t.proxy(renames["CryptoKeyVersionIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListCryptoKeyVersionsResponseIn"])
    types["ListCryptoKeyVersionsResponseOut"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "cryptoKeyVersions": t.array(
                t.proxy(renames["CryptoKeyVersionOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCryptoKeyVersionsResponseOut"])
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
    types["RestoreCryptoKeyVersionRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["RestoreCryptoKeyVersionRequestIn"])
    types["RestoreCryptoKeyVersionRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RestoreCryptoKeyVersionRequestOut"])
    types["PolicyIn"] = t.struct(
        {
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["GenerateRandomBytesResponseIn"] = t.struct(
        {"dataCrc32c": t.string().optional(), "data": t.string().optional()}
    ).named(renames["GenerateRandomBytesResponseIn"])
    types["GenerateRandomBytesResponseOut"] = t.struct(
        {
            "dataCrc32c": t.string().optional(),
            "data": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateRandomBytesResponseOut"])
    types["WrappingPublicKeyIn"] = t.struct({"pem": t.string().optional()}).named(
        renames["WrappingPublicKeyIn"]
    )
    types["WrappingPublicKeyOut"] = t.struct(
        {
            "pem": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WrappingPublicKeyOut"])
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
    types["EkmConfigIn"] = t.struct(
        {"defaultEkmConnection": t.string().optional()}
    ).named(renames["EkmConfigIn"])
    types["EkmConfigOut"] = t.struct(
        {
            "name": t.string().optional(),
            "defaultEkmConnection": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EkmConfigOut"])
    types["DestroyCryptoKeyVersionRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DestroyCryptoKeyVersionRequestIn"])
    types["DestroyCryptoKeyVersionRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DestroyCryptoKeyVersionRequestOut"])
    types["CryptoKeyVersionIn"] = t.struct(
        {
            "externalProtectionLevelOptions": t.proxy(
                renames["ExternalProtectionLevelOptionsIn"]
            ).optional(),
            "state": t.string().optional(),
        }
    ).named(renames["CryptoKeyVersionIn"])
    types["CryptoKeyVersionOut"] = t.struct(
        {
            "importFailureReason": t.string().optional(),
            "importTime": t.string().optional(),
            "generationFailureReason": t.string().optional(),
            "createTime": t.string().optional(),
            "protectionLevel": t.string().optional(),
            "destroyTime": t.string().optional(),
            "attestation": t.proxy(renames["KeyOperationAttestationOut"]).optional(),
            "importJob": t.string().optional(),
            "generateTime": t.string().optional(),
            "name": t.string().optional(),
            "algorithm": t.string().optional(),
            "externalProtectionLevelOptions": t.proxy(
                renames["ExternalProtectionLevelOptionsOut"]
            ).optional(),
            "reimportEligible": t.boolean().optional(),
            "state": t.string().optional(),
            "destroyEventTime": t.string().optional(),
            "externalDestructionFailureReason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CryptoKeyVersionOut"])
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
    types["LocationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["ListImportJobsResponseIn"] = t.struct(
        {
            "importJobs": t.array(t.proxy(renames["ImportJobIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
        }
    ).named(renames["ListImportJobsResponseIn"])
    types["ListImportJobsResponseOut"] = t.struct(
        {
            "importJobs": t.array(t.proxy(renames["ImportJobOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListImportJobsResponseOut"])
    types["MacVerifyRequestIn"] = t.struct(
        {
            "data": t.string(),
            "macCrc32c": t.string().optional(),
            "mac": t.string(),
            "dataCrc32c": t.string().optional(),
        }
    ).named(renames["MacVerifyRequestIn"])
    types["MacVerifyRequestOut"] = t.struct(
        {
            "data": t.string(),
            "macCrc32c": t.string().optional(),
            "mac": t.string(),
            "dataCrc32c": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MacVerifyRequestOut"])
    types["AuditConfigIn"] = t.struct(
        {
            "service": t.string().optional(),
            "auditLogConfigs": t.array(t.proxy(renames["AuditLogConfigIn"])).optional(),
        }
    ).named(renames["AuditConfigIn"])
    types["AuditConfigOut"] = t.struct(
        {
            "service": t.string().optional(),
            "auditLogConfigs": t.array(
                t.proxy(renames["AuditLogConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditConfigOut"])
    types["KeyRingIn"] = t.struct({"_": t.string().optional()}).named(
        renames["KeyRingIn"]
    )
    types["KeyRingOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyRingOut"])
    types["KeyOperationAttestationIn"] = t.struct({"_": t.string().optional()}).named(
        renames["KeyOperationAttestationIn"]
    )
    types["KeyOperationAttestationOut"] = t.struct(
        {
            "content": t.string().optional(),
            "certChains": t.proxy(renames["CertificateChainsOut"]).optional(),
            "format": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyOperationAttestationOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["AsymmetricSignRequestIn"] = t.struct(
        {
            "digest": t.proxy(renames["DigestIn"]).optional(),
            "data": t.string().optional(),
            "dataCrc32c": t.string().optional(),
            "digestCrc32c": t.string().optional(),
        }
    ).named(renames["AsymmetricSignRequestIn"])
    types["AsymmetricSignRequestOut"] = t.struct(
        {
            "digest": t.proxy(renames["DigestOut"]).optional(),
            "data": t.string().optional(),
            "dataCrc32c": t.string().optional(),
            "digestCrc32c": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AsymmetricSignRequestOut"])
    types["ListLocationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
        }
    ).named(renames["ListLocationsResponseIn"])
    types["ListLocationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "locations": t.array(t.proxy(renames["LocationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLocationsResponseOut"])
    types["MacVerifyResponseIn"] = t.struct(
        {
            "protectionLevel": t.string().optional(),
            "success": t.boolean().optional(),
            "verifiedMacCrc32c": t.boolean().optional(),
            "verifiedSuccessIntegrity": t.boolean().optional(),
            "verifiedDataCrc32c": t.boolean().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["MacVerifyResponseIn"])
    types["MacVerifyResponseOut"] = t.struct(
        {
            "protectionLevel": t.string().optional(),
            "success": t.boolean().optional(),
            "verifiedMacCrc32c": t.boolean().optional(),
            "verifiedSuccessIntegrity": t.boolean().optional(),
            "verifiedDataCrc32c": t.boolean().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MacVerifyResponseOut"])

    functions = {}
    functions["projectsLocationsGetEkmConfig"] = cloudkms.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsList"] = cloudkms.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGenerateRandomBytes"] = cloudkms.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsUpdateEkmConfig"] = cloudkms.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = cloudkms.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsGet"] = cloudkms.post(
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
    functions["projectsLocationsKeyRingsGetIamPolicy"] = cloudkms.post(
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
    functions["projectsLocationsKeyRingsList"] = cloudkms.post(
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
    functions["projectsLocationsKeyRingsCreate"] = cloudkms.post(
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
    functions["projectsLocationsKeyRingsTestIamPermissions"] = cloudkms.post(
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
    functions["projectsLocationsKeyRingsSetIamPolicy"] = cloudkms.post(
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
    functions["projectsLocationsKeyRingsImportJobsSetIamPolicy"] = cloudkms.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsImportJobsList"] = cloudkms.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsImportJobsGet"] = cloudkms.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsImportJobsTestIamPermissions"] = cloudkms.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsImportJobsCreate"] = cloudkms.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsImportJobsGetIamPolicy"] = cloudkms.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsCryptoKeysTestIamPermissions"] = cloudkms.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsCryptoKeysList"] = cloudkms.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsCryptoKeysEncrypt"] = cloudkms.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsCryptoKeysPatch"] = cloudkms.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsCryptoKeysGet"] = cloudkms.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsCryptoKeysUpdatePrimaryVersion"] = cloudkms.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsCryptoKeysDecrypt"] = cloudkms.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsCryptoKeysCreate"] = cloudkms.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsCryptoKeysSetIamPolicy"] = cloudkms.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsCryptoKeysGetIamPolicy"] = cloudkms.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsKeyRingsCryptoKeysCryptoKeyVersionsImport"
    ] = cloudkms.post(
        "v1/{name}:macSign",
        t.struct(
            {
                "name": t.string(),
                "data": t.string(),
                "dataCrc32c": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MacSignResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsKeyRingsCryptoKeysCryptoKeyVersionsList"
    ] = cloudkms.post(
        "v1/{name}:macSign",
        t.struct(
            {
                "name": t.string(),
                "data": t.string(),
                "dataCrc32c": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MacSignResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsKeyRingsCryptoKeysCryptoKeyVersionsRestore"
    ] = cloudkms.post(
        "v1/{name}:macSign",
        t.struct(
            {
                "name": t.string(),
                "data": t.string(),
                "dataCrc32c": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MacSignResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsKeyRingsCryptoKeysCryptoKeyVersionsCreate"
    ] = cloudkms.post(
        "v1/{name}:macSign",
        t.struct(
            {
                "name": t.string(),
                "data": t.string(),
                "dataCrc32c": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MacSignResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsKeyRingsCryptoKeysCryptoKeyVersionsAsymmetricDecrypt"
    ] = cloudkms.post(
        "v1/{name}:macSign",
        t.struct(
            {
                "name": t.string(),
                "data": t.string(),
                "dataCrc32c": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MacSignResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsKeyRingsCryptoKeysCryptoKeyVersionsAsymmetricSign"
    ] = cloudkms.post(
        "v1/{name}:macSign",
        t.struct(
            {
                "name": t.string(),
                "data": t.string(),
                "dataCrc32c": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MacSignResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsKeyRingsCryptoKeysCryptoKeyVersionsGetPublicKey"
    ] = cloudkms.post(
        "v1/{name}:macSign",
        t.struct(
            {
                "name": t.string(),
                "data": t.string(),
                "dataCrc32c": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MacSignResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsKeyRingsCryptoKeysCryptoKeyVersionsMacVerify"
    ] = cloudkms.post(
        "v1/{name}:macSign",
        t.struct(
            {
                "name": t.string(),
                "data": t.string(),
                "dataCrc32c": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MacSignResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsKeyRingsCryptoKeysCryptoKeyVersionsPatch"
    ] = cloudkms.post(
        "v1/{name}:macSign",
        t.struct(
            {
                "name": t.string(),
                "data": t.string(),
                "dataCrc32c": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MacSignResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsKeyRingsCryptoKeysCryptoKeyVersionsGet"
    ] = cloudkms.post(
        "v1/{name}:macSign",
        t.struct(
            {
                "name": t.string(),
                "data": t.string(),
                "dataCrc32c": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MacSignResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsKeyRingsCryptoKeysCryptoKeyVersionsDestroy"
    ] = cloudkms.post(
        "v1/{name}:macSign",
        t.struct(
            {
                "name": t.string(),
                "data": t.string(),
                "dataCrc32c": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MacSignResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsKeyRingsCryptoKeysCryptoKeyVersionsMacSign"
    ] = cloudkms.post(
        "v1/{name}:macSign",
        t.struct(
            {
                "name": t.string(),
                "data": t.string(),
                "dataCrc32c": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MacSignResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEkmConnectionsList"] = cloudkms.post(
        "v1/{parent}/ekmConnections",
        t.struct(
            {
                "ekmConnectionId": t.string(),
                "parent": t.string(),
                "etag": t.string().optional(),
                "cryptoSpacePath": t.string().optional(),
                "serviceResolvers": t.array(
                    t.proxy(renames["ServiceResolverIn"])
                ).optional(),
                "keyManagementMode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EkmConnectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEkmConnectionsPatch"] = cloudkms.post(
        "v1/{parent}/ekmConnections",
        t.struct(
            {
                "ekmConnectionId": t.string(),
                "parent": t.string(),
                "etag": t.string().optional(),
                "cryptoSpacePath": t.string().optional(),
                "serviceResolvers": t.array(
                    t.proxy(renames["ServiceResolverIn"])
                ).optional(),
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
                "etag": t.string().optional(),
                "cryptoSpacePath": t.string().optional(),
                "serviceResolvers": t.array(
                    t.proxy(renames["ServiceResolverIn"])
                ).optional(),
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
                "etag": t.string().optional(),
                "cryptoSpacePath": t.string().optional(),
                "serviceResolvers": t.array(
                    t.proxy(renames["ServiceResolverIn"])
                ).optional(),
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
                "etag": t.string().optional(),
                "cryptoSpacePath": t.string().optional(),
                "serviceResolvers": t.array(
                    t.proxy(renames["ServiceResolverIn"])
                ).optional(),
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
                "etag": t.string().optional(),
                "cryptoSpacePath": t.string().optional(),
                "serviceResolvers": t.array(
                    t.proxy(renames["ServiceResolverIn"])
                ).optional(),
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
                "etag": t.string().optional(),
                "cryptoSpacePath": t.string().optional(),
                "serviceResolvers": t.array(
                    t.proxy(renames["ServiceResolverIn"])
                ).optional(),
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
                "etag": t.string().optional(),
                "cryptoSpacePath": t.string().optional(),
                "serviceResolvers": t.array(
                    t.proxy(renames["ServiceResolverIn"])
                ).optional(),
                "keyManagementMode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EkmConnectionOut"]),
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
        importer="cloudkms", renames=renames, types=types, functions=functions
    )
