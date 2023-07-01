from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_cloudkms():
    cloudkms = HTTPRuntime("https://cloudkms.googleapis.com/")

    renames = {
        "ErrorResponse": "_cloudkms_1_ErrorResponse",
        "RawDecryptRequestIn": "_cloudkms_2_RawDecryptRequestIn",
        "RawDecryptRequestOut": "_cloudkms_3_RawDecryptRequestOut",
        "AsymmetricDecryptResponseIn": "_cloudkms_4_AsymmetricDecryptResponseIn",
        "AsymmetricDecryptResponseOut": "_cloudkms_5_AsymmetricDecryptResponseOut",
        "ServiceResolverIn": "_cloudkms_6_ServiceResolverIn",
        "ServiceResolverOut": "_cloudkms_7_ServiceResolverOut",
        "ListLocationsResponseIn": "_cloudkms_8_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_cloudkms_9_ListLocationsResponseOut",
        "RawEncryptResponseIn": "_cloudkms_10_RawEncryptResponseIn",
        "RawEncryptResponseOut": "_cloudkms_11_RawEncryptResponseOut",
        "MacSignRequestIn": "_cloudkms_12_MacSignRequestIn",
        "MacSignRequestOut": "_cloudkms_13_MacSignRequestOut",
        "EkmConnectionIn": "_cloudkms_14_EkmConnectionIn",
        "EkmConnectionOut": "_cloudkms_15_EkmConnectionOut",
        "LocationMetadataIn": "_cloudkms_16_LocationMetadataIn",
        "LocationMetadataOut": "_cloudkms_17_LocationMetadataOut",
        "CertificateIn": "_cloudkms_18_CertificateIn",
        "CertificateOut": "_cloudkms_19_CertificateOut",
        "MacVerifyResponseIn": "_cloudkms_20_MacVerifyResponseIn",
        "MacVerifyResponseOut": "_cloudkms_21_MacVerifyResponseOut",
        "ListCryptoKeysResponseIn": "_cloudkms_22_ListCryptoKeysResponseIn",
        "ListCryptoKeysResponseOut": "_cloudkms_23_ListCryptoKeysResponseOut",
        "WrappingPublicKeyIn": "_cloudkms_24_WrappingPublicKeyIn",
        "WrappingPublicKeyOut": "_cloudkms_25_WrappingPublicKeyOut",
        "CertificateChainsIn": "_cloudkms_26_CertificateChainsIn",
        "CertificateChainsOut": "_cloudkms_27_CertificateChainsOut",
        "RawEncryptRequestIn": "_cloudkms_28_RawEncryptRequestIn",
        "RawEncryptRequestOut": "_cloudkms_29_RawEncryptRequestOut",
        "TestIamPermissionsResponseIn": "_cloudkms_30_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_cloudkms_31_TestIamPermissionsResponseOut",
        "ImportCryptoKeyVersionRequestIn": "_cloudkms_32_ImportCryptoKeyVersionRequestIn",
        "ImportCryptoKeyVersionRequestOut": "_cloudkms_33_ImportCryptoKeyVersionRequestOut",
        "DecryptRequestIn": "_cloudkms_34_DecryptRequestIn",
        "DecryptRequestOut": "_cloudkms_35_DecryptRequestOut",
        "EncryptRequestIn": "_cloudkms_36_EncryptRequestIn",
        "EncryptRequestOut": "_cloudkms_37_EncryptRequestOut",
        "GenerateRandomBytesRequestIn": "_cloudkms_38_GenerateRandomBytesRequestIn",
        "GenerateRandomBytesRequestOut": "_cloudkms_39_GenerateRandomBytesRequestOut",
        "ListEkmConnectionsResponseIn": "_cloudkms_40_ListEkmConnectionsResponseIn",
        "ListEkmConnectionsResponseOut": "_cloudkms_41_ListEkmConnectionsResponseOut",
        "SetIamPolicyRequestIn": "_cloudkms_42_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_cloudkms_43_SetIamPolicyRequestOut",
        "ExternalProtectionLevelOptionsIn": "_cloudkms_44_ExternalProtectionLevelOptionsIn",
        "ExternalProtectionLevelOptionsOut": "_cloudkms_45_ExternalProtectionLevelOptionsOut",
        "MacVerifyRequestIn": "_cloudkms_46_MacVerifyRequestIn",
        "MacVerifyRequestOut": "_cloudkms_47_MacVerifyRequestOut",
        "UpdateCryptoKeyPrimaryVersionRequestIn": "_cloudkms_48_UpdateCryptoKeyPrimaryVersionRequestIn",
        "UpdateCryptoKeyPrimaryVersionRequestOut": "_cloudkms_49_UpdateCryptoKeyPrimaryVersionRequestOut",
        "PolicyIn": "_cloudkms_50_PolicyIn",
        "PolicyOut": "_cloudkms_51_PolicyOut",
        "KeyOperationAttestationIn": "_cloudkms_52_KeyOperationAttestationIn",
        "KeyOperationAttestationOut": "_cloudkms_53_KeyOperationAttestationOut",
        "DecryptResponseIn": "_cloudkms_54_DecryptResponseIn",
        "DecryptResponseOut": "_cloudkms_55_DecryptResponseOut",
        "ImportJobIn": "_cloudkms_56_ImportJobIn",
        "ImportJobOut": "_cloudkms_57_ImportJobOut",
        "DigestIn": "_cloudkms_58_DigestIn",
        "DigestOut": "_cloudkms_59_DigestOut",
        "AuditConfigIn": "_cloudkms_60_AuditConfigIn",
        "AuditConfigOut": "_cloudkms_61_AuditConfigOut",
        "BindingIn": "_cloudkms_62_BindingIn",
        "BindingOut": "_cloudkms_63_BindingOut",
        "EncryptResponseIn": "_cloudkms_64_EncryptResponseIn",
        "EncryptResponseOut": "_cloudkms_65_EncryptResponseOut",
        "VerifyConnectivityResponseIn": "_cloudkms_66_VerifyConnectivityResponseIn",
        "VerifyConnectivityResponseOut": "_cloudkms_67_VerifyConnectivityResponseOut",
        "CryptoKeyVersionTemplateIn": "_cloudkms_68_CryptoKeyVersionTemplateIn",
        "CryptoKeyVersionTemplateOut": "_cloudkms_69_CryptoKeyVersionTemplateOut",
        "ListImportJobsResponseIn": "_cloudkms_70_ListImportJobsResponseIn",
        "ListImportJobsResponseOut": "_cloudkms_71_ListImportJobsResponseOut",
        "PublicKeyIn": "_cloudkms_72_PublicKeyIn",
        "PublicKeyOut": "_cloudkms_73_PublicKeyOut",
        "ListKeyRingsResponseIn": "_cloudkms_74_ListKeyRingsResponseIn",
        "ListKeyRingsResponseOut": "_cloudkms_75_ListKeyRingsResponseOut",
        "GenerateRandomBytesResponseIn": "_cloudkms_76_GenerateRandomBytesResponseIn",
        "GenerateRandomBytesResponseOut": "_cloudkms_77_GenerateRandomBytesResponseOut",
        "ListCryptoKeyVersionsResponseIn": "_cloudkms_78_ListCryptoKeyVersionsResponseIn",
        "ListCryptoKeyVersionsResponseOut": "_cloudkms_79_ListCryptoKeyVersionsResponseOut",
        "LocationIn": "_cloudkms_80_LocationIn",
        "LocationOut": "_cloudkms_81_LocationOut",
        "AsymmetricSignRequestIn": "_cloudkms_82_AsymmetricSignRequestIn",
        "AsymmetricSignRequestOut": "_cloudkms_83_AsymmetricSignRequestOut",
        "AsymmetricDecryptRequestIn": "_cloudkms_84_AsymmetricDecryptRequestIn",
        "AsymmetricDecryptRequestOut": "_cloudkms_85_AsymmetricDecryptRequestOut",
        "TestIamPermissionsRequestIn": "_cloudkms_86_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_cloudkms_87_TestIamPermissionsRequestOut",
        "ExprIn": "_cloudkms_88_ExprIn",
        "ExprOut": "_cloudkms_89_ExprOut",
        "AuditLogConfigIn": "_cloudkms_90_AuditLogConfigIn",
        "AuditLogConfigOut": "_cloudkms_91_AuditLogConfigOut",
        "CryptoKeyIn": "_cloudkms_92_CryptoKeyIn",
        "CryptoKeyOut": "_cloudkms_93_CryptoKeyOut",
        "EkmConfigIn": "_cloudkms_94_EkmConfigIn",
        "EkmConfigOut": "_cloudkms_95_EkmConfigOut",
        "CryptoKeyVersionIn": "_cloudkms_96_CryptoKeyVersionIn",
        "CryptoKeyVersionOut": "_cloudkms_97_CryptoKeyVersionOut",
        "AsymmetricSignResponseIn": "_cloudkms_98_AsymmetricSignResponseIn",
        "AsymmetricSignResponseOut": "_cloudkms_99_AsymmetricSignResponseOut",
        "RestoreCryptoKeyVersionRequestIn": "_cloudkms_100_RestoreCryptoKeyVersionRequestIn",
        "RestoreCryptoKeyVersionRequestOut": "_cloudkms_101_RestoreCryptoKeyVersionRequestOut",
        "MacSignResponseIn": "_cloudkms_102_MacSignResponseIn",
        "MacSignResponseOut": "_cloudkms_103_MacSignResponseOut",
        "RawDecryptResponseIn": "_cloudkms_104_RawDecryptResponseIn",
        "RawDecryptResponseOut": "_cloudkms_105_RawDecryptResponseOut",
        "DestroyCryptoKeyVersionRequestIn": "_cloudkms_106_DestroyCryptoKeyVersionRequestIn",
        "DestroyCryptoKeyVersionRequestOut": "_cloudkms_107_DestroyCryptoKeyVersionRequestOut",
        "KeyRingIn": "_cloudkms_108_KeyRingIn",
        "KeyRingOut": "_cloudkms_109_KeyRingOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["RawDecryptRequestIn"] = t.struct(
        {
            "ciphertextCrc32c": t.string().optional(),
            "additionalAuthenticatedData": t.string().optional(),
            "tagLength": t.integer().optional(),
            "initializationVectorCrc32c": t.string().optional(),
            "ciphertext": t.string(),
            "additionalAuthenticatedDataCrc32c": t.string().optional(),
            "initializationVector": t.string(),
        }
    ).named(renames["RawDecryptRequestIn"])
    types["RawDecryptRequestOut"] = t.struct(
        {
            "ciphertextCrc32c": t.string().optional(),
            "additionalAuthenticatedData": t.string().optional(),
            "tagLength": t.integer().optional(),
            "initializationVectorCrc32c": t.string().optional(),
            "ciphertext": t.string(),
            "additionalAuthenticatedDataCrc32c": t.string().optional(),
            "initializationVector": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RawDecryptRequestOut"])
    types["AsymmetricDecryptResponseIn"] = t.struct(
        {
            "verifiedCiphertextCrc32c": t.boolean().optional(),
            "plaintextCrc32c": t.string().optional(),
            "protectionLevel": t.string().optional(),
            "plaintext": t.string().optional(),
        }
    ).named(renames["AsymmetricDecryptResponseIn"])
    types["AsymmetricDecryptResponseOut"] = t.struct(
        {
            "verifiedCiphertextCrc32c": t.boolean().optional(),
            "plaintextCrc32c": t.string().optional(),
            "protectionLevel": t.string().optional(),
            "plaintext": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AsymmetricDecryptResponseOut"])
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
    types["RawEncryptResponseIn"] = t.struct(
        {
            "ciphertext": t.string().optional(),
            "verifiedInitializationVectorCrc32c": t.boolean().optional(),
            "verifiedAdditionalAuthenticatedDataCrc32c": t.boolean().optional(),
            "protectionLevel": t.string().optional(),
            "initializationVectorCrc32c": t.string().optional(),
            "verifiedPlaintextCrc32c": t.boolean().optional(),
            "name": t.string().optional(),
            "initializationVector": t.string().optional(),
            "ciphertextCrc32c": t.string().optional(),
            "tagLength": t.integer().optional(),
        }
    ).named(renames["RawEncryptResponseIn"])
    types["RawEncryptResponseOut"] = t.struct(
        {
            "ciphertext": t.string().optional(),
            "verifiedInitializationVectorCrc32c": t.boolean().optional(),
            "verifiedAdditionalAuthenticatedDataCrc32c": t.boolean().optional(),
            "protectionLevel": t.string().optional(),
            "initializationVectorCrc32c": t.string().optional(),
            "verifiedPlaintextCrc32c": t.boolean().optional(),
            "name": t.string().optional(),
            "initializationVector": t.string().optional(),
            "ciphertextCrc32c": t.string().optional(),
            "tagLength": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RawEncryptResponseOut"])
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
    types["EkmConnectionIn"] = t.struct(
        {
            "cryptoSpacePath": t.string().optional(),
            "serviceResolvers": t.array(
                t.proxy(renames["ServiceResolverIn"])
            ).optional(),
            "keyManagementMode": t.string().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["EkmConnectionIn"])
    types["EkmConnectionOut"] = t.struct(
        {
            "name": t.string().optional(),
            "cryptoSpacePath": t.string().optional(),
            "serviceResolvers": t.array(
                t.proxy(renames["ServiceResolverOut"])
            ).optional(),
            "keyManagementMode": t.string().optional(),
            "createTime": t.string().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EkmConnectionOut"])
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
    types["CertificateIn"] = t.struct({"rawDer": t.string()}).named(
        renames["CertificateIn"]
    )
    types["CertificateOut"] = t.struct(
        {
            "serialNumber": t.string().optional(),
            "subjectAlternativeDnsNames": t.array(t.string()).optional(),
            "issuer": t.string().optional(),
            "subject": t.string().optional(),
            "sha256Fingerprint": t.string().optional(),
            "notAfterTime": t.string().optional(),
            "parsed": t.boolean().optional(),
            "rawDer": t.string(),
            "notBeforeTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateOut"])
    types["MacVerifyResponseIn"] = t.struct(
        {
            "protectionLevel": t.string().optional(),
            "verifiedDataCrc32c": t.boolean().optional(),
            "success": t.boolean().optional(),
            "verifiedSuccessIntegrity": t.boolean().optional(),
            "name": t.string().optional(),
            "verifiedMacCrc32c": t.boolean().optional(),
        }
    ).named(renames["MacVerifyResponseIn"])
    types["MacVerifyResponseOut"] = t.struct(
        {
            "protectionLevel": t.string().optional(),
            "verifiedDataCrc32c": t.boolean().optional(),
            "success": t.boolean().optional(),
            "verifiedSuccessIntegrity": t.boolean().optional(),
            "name": t.string().optional(),
            "verifiedMacCrc32c": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MacVerifyResponseOut"])
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
    types["WrappingPublicKeyIn"] = t.struct({"pem": t.string().optional()}).named(
        renames["WrappingPublicKeyIn"]
    )
    types["WrappingPublicKeyOut"] = t.struct(
        {
            "pem": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WrappingPublicKeyOut"])
    types["CertificateChainsIn"] = t.struct(
        {
            "caviumCerts": t.array(t.string()).optional(),
            "googleCardCerts": t.array(t.string()).optional(),
            "googlePartitionCerts": t.array(t.string()).optional(),
        }
    ).named(renames["CertificateChainsIn"])
    types["CertificateChainsOut"] = t.struct(
        {
            "caviumCerts": t.array(t.string()).optional(),
            "googleCardCerts": t.array(t.string()).optional(),
            "googlePartitionCerts": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateChainsOut"])
    types["RawEncryptRequestIn"] = t.struct(
        {
            "initializationVector": t.string().optional(),
            "additionalAuthenticatedData": t.string().optional(),
            "plaintextCrc32c": t.string().optional(),
            "plaintext": t.string(),
            "additionalAuthenticatedDataCrc32c": t.string().optional(),
            "initializationVectorCrc32c": t.string().optional(),
        }
    ).named(renames["RawEncryptRequestIn"])
    types["RawEncryptRequestOut"] = t.struct(
        {
            "initializationVector": t.string().optional(),
            "additionalAuthenticatedData": t.string().optional(),
            "plaintextCrc32c": t.string().optional(),
            "plaintext": t.string(),
            "additionalAuthenticatedDataCrc32c": t.string().optional(),
            "initializationVectorCrc32c": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RawEncryptRequestOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["ImportCryptoKeyVersionRequestIn"] = t.struct(
        {
            "cryptoKeyVersion": t.string().optional(),
            "algorithm": t.string(),
            "rsaAesWrappedKey": t.string().optional(),
            "wrappedKey": t.string().optional(),
            "importJob": t.string(),
        }
    ).named(renames["ImportCryptoKeyVersionRequestIn"])
    types["ImportCryptoKeyVersionRequestOut"] = t.struct(
        {
            "cryptoKeyVersion": t.string().optional(),
            "algorithm": t.string(),
            "rsaAesWrappedKey": t.string().optional(),
            "wrappedKey": t.string().optional(),
            "importJob": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportCryptoKeyVersionRequestOut"])
    types["DecryptRequestIn"] = t.struct(
        {
            "ciphertextCrc32c": t.string().optional(),
            "additionalAuthenticatedDataCrc32c": t.string().optional(),
            "ciphertext": t.string(),
            "additionalAuthenticatedData": t.string().optional(),
        }
    ).named(renames["DecryptRequestIn"])
    types["DecryptRequestOut"] = t.struct(
        {
            "ciphertextCrc32c": t.string().optional(),
            "additionalAuthenticatedDataCrc32c": t.string().optional(),
            "ciphertext": t.string(),
            "additionalAuthenticatedData": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DecryptRequestOut"])
    types["EncryptRequestIn"] = t.struct(
        {
            "additionalAuthenticatedData": t.string().optional(),
            "additionalAuthenticatedDataCrc32c": t.string().optional(),
            "plaintextCrc32c": t.string().optional(),
            "plaintext": t.string(),
        }
    ).named(renames["EncryptRequestIn"])
    types["EncryptRequestOut"] = t.struct(
        {
            "additionalAuthenticatedData": t.string().optional(),
            "additionalAuthenticatedDataCrc32c": t.string().optional(),
            "plaintextCrc32c": t.string().optional(),
            "plaintext": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EncryptRequestOut"])
    types["GenerateRandomBytesRequestIn"] = t.struct(
        {
            "lengthBytes": t.integer().optional(),
            "protectionLevel": t.string().optional(),
        }
    ).named(renames["GenerateRandomBytesRequestIn"])
    types["GenerateRandomBytesRequestOut"] = t.struct(
        {
            "lengthBytes": t.integer().optional(),
            "protectionLevel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateRandomBytesRequestOut"])
    types["ListEkmConnectionsResponseIn"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "ekmConnections": t.array(t.proxy(renames["EkmConnectionIn"])).optional(),
        }
    ).named(renames["ListEkmConnectionsResponseIn"])
    types["ListEkmConnectionsResponseOut"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "ekmConnections": t.array(t.proxy(renames["EkmConnectionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListEkmConnectionsResponseOut"])
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
    types["MacVerifyRequestIn"] = t.struct(
        {
            "macCrc32c": t.string().optional(),
            "data": t.string(),
            "mac": t.string(),
            "dataCrc32c": t.string().optional(),
        }
    ).named(renames["MacVerifyRequestIn"])
    types["MacVerifyRequestOut"] = t.struct(
        {
            "macCrc32c": t.string().optional(),
            "data": t.string(),
            "mac": t.string(),
            "dataCrc32c": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MacVerifyRequestOut"])
    types["UpdateCryptoKeyPrimaryVersionRequestIn"] = t.struct(
        {"cryptoKeyVersionId": t.string()}
    ).named(renames["UpdateCryptoKeyPrimaryVersionRequestIn"])
    types["UpdateCryptoKeyPrimaryVersionRequestOut"] = t.struct(
        {
            "cryptoKeyVersionId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateCryptoKeyPrimaryVersionRequestOut"])
    types["PolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["KeyOperationAttestationIn"] = t.struct({"_": t.string().optional()}).named(
        renames["KeyOperationAttestationIn"]
    )
    types["KeyOperationAttestationOut"] = t.struct(
        {
            "certChains": t.proxy(renames["CertificateChainsOut"]).optional(),
            "format": t.string().optional(),
            "content": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyOperationAttestationOut"])
    types["DecryptResponseIn"] = t.struct(
        {
            "usedPrimary": t.boolean().optional(),
            "plaintextCrc32c": t.string().optional(),
            "plaintext": t.string().optional(),
            "protectionLevel": t.string().optional(),
        }
    ).named(renames["DecryptResponseIn"])
    types["DecryptResponseOut"] = t.struct(
        {
            "usedPrimary": t.boolean().optional(),
            "plaintextCrc32c": t.string().optional(),
            "plaintext": t.string().optional(),
            "protectionLevel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DecryptResponseOut"])
    types["ImportJobIn"] = t.struct(
        {"importMethod": t.string(), "protectionLevel": t.string()}
    ).named(renames["ImportJobIn"])
    types["ImportJobOut"] = t.struct(
        {
            "expireTime": t.string().optional(),
            "importMethod": t.string(),
            "attestation": t.proxy(renames["KeyOperationAttestationOut"]).optional(),
            "publicKey": t.proxy(renames["WrappingPublicKeyOut"]).optional(),
            "expireEventTime": t.string().optional(),
            "createTime": t.string().optional(),
            "protectionLevel": t.string(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "generateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportJobOut"])
    types["DigestIn"] = t.struct(
        {
            "sha384": t.string().optional(),
            "sha256": t.string().optional(),
            "sha512": t.string().optional(),
        }
    ).named(renames["DigestIn"])
    types["DigestOut"] = t.struct(
        {
            "sha384": t.string().optional(),
            "sha256": t.string().optional(),
            "sha512": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DigestOut"])
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
    types["EncryptResponseIn"] = t.struct(
        {
            "ciphertextCrc32c": t.string().optional(),
            "ciphertext": t.string().optional(),
            "name": t.string().optional(),
            "verifiedAdditionalAuthenticatedDataCrc32c": t.boolean().optional(),
            "protectionLevel": t.string().optional(),
            "verifiedPlaintextCrc32c": t.boolean().optional(),
        }
    ).named(renames["EncryptResponseIn"])
    types["EncryptResponseOut"] = t.struct(
        {
            "ciphertextCrc32c": t.string().optional(),
            "ciphertext": t.string().optional(),
            "name": t.string().optional(),
            "verifiedAdditionalAuthenticatedDataCrc32c": t.boolean().optional(),
            "protectionLevel": t.string().optional(),
            "verifiedPlaintextCrc32c": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EncryptResponseOut"])
    types["VerifyConnectivityResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["VerifyConnectivityResponseIn"])
    types["VerifyConnectivityResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["VerifyConnectivityResponseOut"])
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
    types["PublicKeyIn"] = t.struct(
        {
            "name": t.string().optional(),
            "pemCrc32c": t.string().optional(),
            "protectionLevel": t.string().optional(),
            "algorithm": t.string().optional(),
            "pem": t.string().optional(),
        }
    ).named(renames["PublicKeyIn"])
    types["PublicKeyOut"] = t.struct(
        {
            "name": t.string().optional(),
            "pemCrc32c": t.string().optional(),
            "protectionLevel": t.string().optional(),
            "algorithm": t.string().optional(),
            "pem": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublicKeyOut"])
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
            "cryptoKeyVersions": t.array(
                t.proxy(renames["CryptoKeyVersionIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
        }
    ).named(renames["ListCryptoKeyVersionsResponseIn"])
    types["ListCryptoKeyVersionsResponseOut"] = t.struct(
        {
            "cryptoKeyVersions": t.array(
                t.proxy(renames["CryptoKeyVersionOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCryptoKeyVersionsResponseOut"])
    types["LocationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["AsymmetricSignRequestIn"] = t.struct(
        {
            "digest": t.proxy(renames["DigestIn"]).optional(),
            "digestCrc32c": t.string().optional(),
            "dataCrc32c": t.string().optional(),
            "data": t.string().optional(),
        }
    ).named(renames["AsymmetricSignRequestIn"])
    types["AsymmetricSignRequestOut"] = t.struct(
        {
            "digest": t.proxy(renames["DigestOut"]).optional(),
            "digestCrc32c": t.string().optional(),
            "dataCrc32c": t.string().optional(),
            "data": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AsymmetricSignRequestOut"])
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
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["ExprIn"] = t.struct(
        {
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
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
    types["CryptoKeyIn"] = t.struct(
        {
            "nextRotationTime": t.string().optional(),
            "destroyScheduledDuration": t.string().optional(),
            "rotationPeriod": t.string().optional(),
            "importOnly": t.boolean().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "versionTemplate": t.proxy(
                renames["CryptoKeyVersionTemplateIn"]
            ).optional(),
            "cryptoKeyBackend": t.string().optional(),
            "purpose": t.string().optional(),
        }
    ).named(renames["CryptoKeyIn"])
    types["CryptoKeyOut"] = t.struct(
        {
            "nextRotationTime": t.string().optional(),
            "destroyScheduledDuration": t.string().optional(),
            "createTime": t.string().optional(),
            "primary": t.proxy(renames["CryptoKeyVersionOut"]).optional(),
            "rotationPeriod": t.string().optional(),
            "importOnly": t.boolean().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "versionTemplate": t.proxy(
                renames["CryptoKeyVersionTemplateOut"]
            ).optional(),
            "cryptoKeyBackend": t.string().optional(),
            "purpose": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CryptoKeyOut"])
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
            "externalProtectionLevelOptions": t.proxy(
                renames["ExternalProtectionLevelOptionsOut"]
            ).optional(),
            "destroyEventTime": t.string().optional(),
            "importFailureReason": t.string().optional(),
            "generationFailureReason": t.string().optional(),
            "destroyTime": t.string().optional(),
            "protectionLevel": t.string().optional(),
            "state": t.string().optional(),
            "attestation": t.proxy(renames["KeyOperationAttestationOut"]).optional(),
            "externalDestructionFailureReason": t.string().optional(),
            "name": t.string().optional(),
            "importTime": t.string().optional(),
            "reimportEligible": t.boolean().optional(),
            "createTime": t.string().optional(),
            "generateTime": t.string().optional(),
            "importJob": t.string().optional(),
            "algorithm": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CryptoKeyVersionOut"])
    types["AsymmetricSignResponseIn"] = t.struct(
        {
            "protectionLevel": t.string().optional(),
            "verifiedDataCrc32c": t.boolean().optional(),
            "name": t.string().optional(),
            "verifiedDigestCrc32c": t.boolean().optional(),
            "signatureCrc32c": t.string().optional(),
            "signature": t.string().optional(),
        }
    ).named(renames["AsymmetricSignResponseIn"])
    types["AsymmetricSignResponseOut"] = t.struct(
        {
            "protectionLevel": t.string().optional(),
            "verifiedDataCrc32c": t.boolean().optional(),
            "name": t.string().optional(),
            "verifiedDigestCrc32c": t.boolean().optional(),
            "signatureCrc32c": t.string().optional(),
            "signature": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AsymmetricSignResponseOut"])
    types["RestoreCryptoKeyVersionRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["RestoreCryptoKeyVersionRequestIn"])
    types["RestoreCryptoKeyVersionRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RestoreCryptoKeyVersionRequestOut"])
    types["MacSignResponseIn"] = t.struct(
        {
            "verifiedDataCrc32c": t.boolean().optional(),
            "macCrc32c": t.string().optional(),
            "protectionLevel": t.string().optional(),
            "mac": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["MacSignResponseIn"])
    types["MacSignResponseOut"] = t.struct(
        {
            "verifiedDataCrc32c": t.boolean().optional(),
            "macCrc32c": t.string().optional(),
            "protectionLevel": t.string().optional(),
            "mac": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MacSignResponseOut"])
    types["RawDecryptResponseIn"] = t.struct(
        {
            "verifiedInitializationVectorCrc32c": t.boolean().optional(),
            "protectionLevel": t.string().optional(),
            "plaintext": t.string().optional(),
            "plaintextCrc32c": t.string().optional(),
            "verifiedAdditionalAuthenticatedDataCrc32c": t.boolean().optional(),
            "verifiedCiphertextCrc32c": t.boolean().optional(),
        }
    ).named(renames["RawDecryptResponseIn"])
    types["RawDecryptResponseOut"] = t.struct(
        {
            "verifiedInitializationVectorCrc32c": t.boolean().optional(),
            "protectionLevel": t.string().optional(),
            "plaintext": t.string().optional(),
            "plaintextCrc32c": t.string().optional(),
            "verifiedAdditionalAuthenticatedDataCrc32c": t.boolean().optional(),
            "verifiedCiphertextCrc32c": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RawDecryptResponseOut"])
    types["DestroyCryptoKeyVersionRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DestroyCryptoKeyVersionRequestIn"])
    types["DestroyCryptoKeyVersionRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DestroyCryptoKeyVersionRequestOut"])
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

    functions = {}
    functions["projectsLocationsUpdateEkmConfig"] = cloudkms.get(
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
    functions["projectsLocationsGetEkmConfig"] = cloudkms.get(
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
    functions["projectsLocationsEkmConnectionsList"] = cloudkms.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EkmConnectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEkmConnectionsVerifyConnectivity"] = cloudkms.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EkmConnectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEkmConnectionsCreate"] = cloudkms.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EkmConnectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEkmConnectionsGetIamPolicy"] = cloudkms.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EkmConnectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEkmConnectionsSetIamPolicy"] = cloudkms.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EkmConnectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEkmConnectionsTestIamPermissions"] = cloudkms.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EkmConnectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEkmConnectionsPatch"] = cloudkms.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EkmConnectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEkmConnectionsGet"] = cloudkms.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EkmConnectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEkmConfigSetIamPolicy"] = cloudkms.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEkmConfigGetIamPolicy"] = cloudkms.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEkmConfigTestIamPermissions"] = cloudkms.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsGet"] = cloudkms.get(
        "v1/{parent}/keyRings",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListKeyRingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsCreate"] = cloudkms.get(
        "v1/{parent}/keyRings",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListKeyRingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsSetIamPolicy"] = cloudkms.get(
        "v1/{parent}/keyRings",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListKeyRingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsGetIamPolicy"] = cloudkms.get(
        "v1/{parent}/keyRings",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListKeyRingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsTestIamPermissions"] = cloudkms.get(
        "v1/{parent}/keyRings",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListKeyRingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsList"] = cloudkms.get(
        "v1/{parent}/keyRings",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListKeyRingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsKeyRingsImportJobsTestIamPermissions"] = cloudkms.post(
        "v1/{parent}/importJobs",
        t.struct(
            {
                "importJobId": t.string(),
                "parent": t.string(),
                "importMethod": t.string(),
                "protectionLevel": t.string(),
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
                "importMethod": t.string(),
                "protectionLevel": t.string(),
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
                "importMethod": t.string(),
                "protectionLevel": t.string(),
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
                "importMethod": t.string(),
                "protectionLevel": t.string(),
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
                "importMethod": t.string(),
                "protectionLevel": t.string(),
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
                "importMethod": t.string(),
                "protectionLevel": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ImportJobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsKeyRingsCryptoKeysUpdatePrimaryVersion"
    ] = cloudkms.post(
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
    functions["projectsLocationsKeyRingsCryptoKeysPatch"] = cloudkms.post(
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
    functions["projectsLocationsKeyRingsCryptoKeysTestIamPermissions"] = cloudkms.post(
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
    functions["projectsLocationsKeyRingsCryptoKeysGet"] = cloudkms.post(
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
    functions["projectsLocationsKeyRingsCryptoKeysDecrypt"] = cloudkms.post(
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
    functions["projectsLocationsKeyRingsCryptoKeysGetIamPolicy"] = cloudkms.post(
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
    functions["projectsLocationsKeyRingsCryptoKeysEncrypt"] = cloudkms.post(
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
    functions["projectsLocationsKeyRingsCryptoKeysList"] = cloudkms.post(
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
    functions["projectsLocationsKeyRingsCryptoKeysCreate"] = cloudkms.post(
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
    functions["projectsLocationsKeyRingsCryptoKeysSetIamPolicy"] = cloudkms.post(
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
    functions[
        "projectsLocationsKeyRingsCryptoKeysCryptoKeyVersionsDestroy"
    ] = cloudkms.post(
        "v1/{parent}/cryptoKeyVersions",
        t.struct(
            {
                "parent": t.string(),
                "externalProtectionLevelOptions": t.proxy(
                    renames["ExternalProtectionLevelOptionsIn"]
                ).optional(),
                "state": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CryptoKeyVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsKeyRingsCryptoKeysCryptoKeyVersionsRawEncrypt"
    ] = cloudkms.post(
        "v1/{parent}/cryptoKeyVersions",
        t.struct(
            {
                "parent": t.string(),
                "externalProtectionLevelOptions": t.proxy(
                    renames["ExternalProtectionLevelOptionsIn"]
                ).optional(),
                "state": t.string().optional(),
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
                "externalProtectionLevelOptions": t.proxy(
                    renames["ExternalProtectionLevelOptionsIn"]
                ).optional(),
                "state": t.string().optional(),
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
                "externalProtectionLevelOptions": t.proxy(
                    renames["ExternalProtectionLevelOptionsIn"]
                ).optional(),
                "state": t.string().optional(),
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
                "externalProtectionLevelOptions": t.proxy(
                    renames["ExternalProtectionLevelOptionsIn"]
                ).optional(),
                "state": t.string().optional(),
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
        "v1/{parent}/cryptoKeyVersions",
        t.struct(
            {
                "parent": t.string(),
                "externalProtectionLevelOptions": t.proxy(
                    renames["ExternalProtectionLevelOptionsIn"]
                ).optional(),
                "state": t.string().optional(),
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
                "externalProtectionLevelOptions": t.proxy(
                    renames["ExternalProtectionLevelOptionsIn"]
                ).optional(),
                "state": t.string().optional(),
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
                "externalProtectionLevelOptions": t.proxy(
                    renames["ExternalProtectionLevelOptionsIn"]
                ).optional(),
                "state": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CryptoKeyVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsKeyRingsCryptoKeysCryptoKeyVersionsRawDecrypt"
    ] = cloudkms.post(
        "v1/{parent}/cryptoKeyVersions",
        t.struct(
            {
                "parent": t.string(),
                "externalProtectionLevelOptions": t.proxy(
                    renames["ExternalProtectionLevelOptionsIn"]
                ).optional(),
                "state": t.string().optional(),
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
                "externalProtectionLevelOptions": t.proxy(
                    renames["ExternalProtectionLevelOptionsIn"]
                ).optional(),
                "state": t.string().optional(),
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
                "externalProtectionLevelOptions": t.proxy(
                    renames["ExternalProtectionLevelOptionsIn"]
                ).optional(),
                "state": t.string().optional(),
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
                "externalProtectionLevelOptions": t.proxy(
                    renames["ExternalProtectionLevelOptionsIn"]
                ).optional(),
                "state": t.string().optional(),
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
                "externalProtectionLevelOptions": t.proxy(
                    renames["ExternalProtectionLevelOptionsIn"]
                ).optional(),
                "state": t.string().optional(),
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
                "externalProtectionLevelOptions": t.proxy(
                    renames["ExternalProtectionLevelOptionsIn"]
                ).optional(),
                "state": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CryptoKeyVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="cloudkms", renames=renames, types=Box(types), functions=Box(functions)
    )
