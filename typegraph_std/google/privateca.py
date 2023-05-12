from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_privateca() -> Import:
    privateca = HTTPRuntime("https://privateca.googleapis.com/")

    renames = {
        "ErrorResponse": "_privateca_1_ErrorResponse",
        "SubjectIn": "_privateca_2_SubjectIn",
        "SubjectOut": "_privateca_3_SubjectOut",
        "RevokedCertificateIn": "_privateca_4_RevokedCertificateIn",
        "RevokedCertificateOut": "_privateca_5_RevokedCertificateOut",
        "PublicKeyIn": "_privateca_6_PublicKeyIn",
        "PublicKeyOut": "_privateca_7_PublicKeyOut",
        "PublishingOptionsIn": "_privateca_8_PublishingOptionsIn",
        "PublishingOptionsOut": "_privateca_9_PublishingOptionsOut",
        "IssuanceModesIn": "_privateca_10_IssuanceModesIn",
        "IssuanceModesOut": "_privateca_11_IssuanceModesOut",
        "CertificateTemplateIn": "_privateca_12_CertificateTemplateIn",
        "CertificateTemplateOut": "_privateca_13_CertificateTemplateOut",
        "DisableCertificateAuthorityRequestIn": "_privateca_14_DisableCertificateAuthorityRequestIn",
        "DisableCertificateAuthorityRequestOut": "_privateca_15_DisableCertificateAuthorityRequestOut",
        "AccessUrlsIn": "_privateca_16_AccessUrlsIn",
        "AccessUrlsOut": "_privateca_17_AccessUrlsOut",
        "EmptyIn": "_privateca_18_EmptyIn",
        "EmptyOut": "_privateca_19_EmptyOut",
        "CaPoolIn": "_privateca_20_CaPoolIn",
        "CaPoolOut": "_privateca_21_CaPoolOut",
        "CertificateRevocationListIn": "_privateca_22_CertificateRevocationListIn",
        "CertificateRevocationListOut": "_privateca_23_CertificateRevocationListOut",
        "FetchCaCertsResponseIn": "_privateca_24_FetchCaCertsResponseIn",
        "FetchCaCertsResponseOut": "_privateca_25_FetchCaCertsResponseOut",
        "NameConstraintsIn": "_privateca_26_NameConstraintsIn",
        "NameConstraintsOut": "_privateca_27_NameConstraintsOut",
        "X509ExtensionIn": "_privateca_28_X509ExtensionIn",
        "X509ExtensionOut": "_privateca_29_X509ExtensionOut",
        "StatusIn": "_privateca_30_StatusIn",
        "StatusOut": "_privateca_31_StatusOut",
        "CertificateConfigIn": "_privateca_32_CertificateConfigIn",
        "CertificateConfigOut": "_privateca_33_CertificateConfigOut",
        "LocationIn": "_privateca_34_LocationIn",
        "LocationOut": "_privateca_35_LocationOut",
        "ListLocationsResponseIn": "_privateca_36_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_privateca_37_ListLocationsResponseOut",
        "AuditLogConfigIn": "_privateca_38_AuditLogConfigIn",
        "AuditLogConfigOut": "_privateca_39_AuditLogConfigOut",
        "ListCertificateRevocationListsResponseIn": "_privateca_40_ListCertificateRevocationListsResponseIn",
        "ListCertificateRevocationListsResponseOut": "_privateca_41_ListCertificateRevocationListsResponseOut",
        "TestIamPermissionsResponseIn": "_privateca_42_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_privateca_43_TestIamPermissionsResponseOut",
        "CertificateExtensionConstraintsIn": "_privateca_44_CertificateExtensionConstraintsIn",
        "CertificateExtensionConstraintsOut": "_privateca_45_CertificateExtensionConstraintsOut",
        "SubjectAltNamesIn": "_privateca_46_SubjectAltNamesIn",
        "SubjectAltNamesOut": "_privateca_47_SubjectAltNamesOut",
        "ObjectIdIn": "_privateca_48_ObjectIdIn",
        "ObjectIdOut": "_privateca_49_ObjectIdOut",
        "FetchCaCertsRequestIn": "_privateca_50_FetchCaCertsRequestIn",
        "FetchCaCertsRequestOut": "_privateca_51_FetchCaCertsRequestOut",
        "FetchCertificateAuthorityCsrResponseIn": "_privateca_52_FetchCertificateAuthorityCsrResponseIn",
        "FetchCertificateAuthorityCsrResponseOut": "_privateca_53_FetchCertificateAuthorityCsrResponseOut",
        "EcKeyTypeIn": "_privateca_54_EcKeyTypeIn",
        "EcKeyTypeOut": "_privateca_55_EcKeyTypeOut",
        "CaOptionsIn": "_privateca_56_CaOptionsIn",
        "CaOptionsOut": "_privateca_57_CaOptionsOut",
        "CertificateFingerprintIn": "_privateca_58_CertificateFingerprintIn",
        "CertificateFingerprintOut": "_privateca_59_CertificateFingerprintOut",
        "CertificateAuthorityIn": "_privateca_60_CertificateAuthorityIn",
        "CertificateAuthorityOut": "_privateca_61_CertificateAuthorityOut",
        "SubordinateConfigIn": "_privateca_62_SubordinateConfigIn",
        "SubordinateConfigOut": "_privateca_63_SubordinateConfigOut",
        "ListCertificateTemplatesResponseIn": "_privateca_64_ListCertificateTemplatesResponseIn",
        "ListCertificateTemplatesResponseOut": "_privateca_65_ListCertificateTemplatesResponseOut",
        "SetIamPolicyRequestIn": "_privateca_66_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_privateca_67_SetIamPolicyRequestOut",
        "SubordinateConfigChainIn": "_privateca_68_SubordinateConfigChainIn",
        "SubordinateConfigChainOut": "_privateca_69_SubordinateConfigChainOut",
        "CertificateIn": "_privateca_70_CertificateIn",
        "CertificateOut": "_privateca_71_CertificateOut",
        "CertificateDescriptionIn": "_privateca_72_CertificateDescriptionIn",
        "CertificateDescriptionOut": "_privateca_73_CertificateDescriptionOut",
        "SubjectConfigIn": "_privateca_74_SubjectConfigIn",
        "SubjectConfigOut": "_privateca_75_SubjectConfigOut",
        "KeyUsageIn": "_privateca_76_KeyUsageIn",
        "KeyUsageOut": "_privateca_77_KeyUsageOut",
        "ListCertificatesResponseIn": "_privateca_78_ListCertificatesResponseIn",
        "ListCertificatesResponseOut": "_privateca_79_ListCertificatesResponseOut",
        "CancelOperationRequestIn": "_privateca_80_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_privateca_81_CancelOperationRequestOut",
        "ExprIn": "_privateca_82_ExprIn",
        "ExprOut": "_privateca_83_ExprOut",
        "KeyIdIn": "_privateca_84_KeyIdIn",
        "KeyIdOut": "_privateca_85_KeyIdOut",
        "ListCertificateAuthoritiesResponseIn": "_privateca_86_ListCertificateAuthoritiesResponseIn",
        "ListCertificateAuthoritiesResponseOut": "_privateca_87_ListCertificateAuthoritiesResponseOut",
        "AllowedKeyTypeIn": "_privateca_88_AllowedKeyTypeIn",
        "AllowedKeyTypeOut": "_privateca_89_AllowedKeyTypeOut",
        "UndeleteCertificateAuthorityRequestIn": "_privateca_90_UndeleteCertificateAuthorityRequestIn",
        "UndeleteCertificateAuthorityRequestOut": "_privateca_91_UndeleteCertificateAuthorityRequestOut",
        "BindingIn": "_privateca_92_BindingIn",
        "BindingOut": "_privateca_93_BindingOut",
        "OperationIn": "_privateca_94_OperationIn",
        "OperationOut": "_privateca_95_OperationOut",
        "SubjectDescriptionIn": "_privateca_96_SubjectDescriptionIn",
        "SubjectDescriptionOut": "_privateca_97_SubjectDescriptionOut",
        "X509ParametersIn": "_privateca_98_X509ParametersIn",
        "X509ParametersOut": "_privateca_99_X509ParametersOut",
        "ExtendedKeyUsageOptionsIn": "_privateca_100_ExtendedKeyUsageOptionsIn",
        "ExtendedKeyUsageOptionsOut": "_privateca_101_ExtendedKeyUsageOptionsOut",
        "ListOperationsResponseIn": "_privateca_102_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_privateca_103_ListOperationsResponseOut",
        "AuditConfigIn": "_privateca_104_AuditConfigIn",
        "AuditConfigOut": "_privateca_105_AuditConfigOut",
        "KeyVersionSpecIn": "_privateca_106_KeyVersionSpecIn",
        "KeyVersionSpecOut": "_privateca_107_KeyVersionSpecOut",
        "TestIamPermissionsRequestIn": "_privateca_108_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_privateca_109_TestIamPermissionsRequestOut",
        "ReconciliationOperationMetadataIn": "_privateca_110_ReconciliationOperationMetadataIn",
        "ReconciliationOperationMetadataOut": "_privateca_111_ReconciliationOperationMetadataOut",
        "IssuancePolicyIn": "_privateca_112_IssuancePolicyIn",
        "IssuancePolicyOut": "_privateca_113_IssuancePolicyOut",
        "RevokeCertificateRequestIn": "_privateca_114_RevokeCertificateRequestIn",
        "RevokeCertificateRequestOut": "_privateca_115_RevokeCertificateRequestOut",
        "PolicyIn": "_privateca_116_PolicyIn",
        "PolicyOut": "_privateca_117_PolicyOut",
        "ListCaPoolsResponseIn": "_privateca_118_ListCaPoolsResponseIn",
        "ListCaPoolsResponseOut": "_privateca_119_ListCaPoolsResponseOut",
        "KeyUsageOptionsIn": "_privateca_120_KeyUsageOptionsIn",
        "KeyUsageOptionsOut": "_privateca_121_KeyUsageOptionsOut",
        "EnableCertificateAuthorityRequestIn": "_privateca_122_EnableCertificateAuthorityRequestIn",
        "EnableCertificateAuthorityRequestOut": "_privateca_123_EnableCertificateAuthorityRequestOut",
        "ActivateCertificateAuthorityRequestIn": "_privateca_124_ActivateCertificateAuthorityRequestIn",
        "ActivateCertificateAuthorityRequestOut": "_privateca_125_ActivateCertificateAuthorityRequestOut",
        "CertChainIn": "_privateca_126_CertChainIn",
        "CertChainOut": "_privateca_127_CertChainOut",
        "RevocationDetailsIn": "_privateca_128_RevocationDetailsIn",
        "RevocationDetailsOut": "_privateca_129_RevocationDetailsOut",
        "RsaKeyTypeIn": "_privateca_130_RsaKeyTypeIn",
        "RsaKeyTypeOut": "_privateca_131_RsaKeyTypeOut",
        "OperationMetadataIn": "_privateca_132_OperationMetadataIn",
        "OperationMetadataOut": "_privateca_133_OperationMetadataOut",
        "CertificateIdentityConstraintsIn": "_privateca_134_CertificateIdentityConstraintsIn",
        "CertificateIdentityConstraintsOut": "_privateca_135_CertificateIdentityConstraintsOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["SubjectIn"] = t.struct(
        {
            "streetAddress": t.string().optional(),
            "organization": t.string().optional(),
            "locality": t.string().optional(),
            "province": t.string().optional(),
            "postalCode": t.string().optional(),
            "countryCode": t.string().optional(),
            "organizationalUnit": t.string().optional(),
            "commonName": t.string().optional(),
        }
    ).named(renames["SubjectIn"])
    types["SubjectOut"] = t.struct(
        {
            "streetAddress": t.string().optional(),
            "organization": t.string().optional(),
            "locality": t.string().optional(),
            "province": t.string().optional(),
            "postalCode": t.string().optional(),
            "countryCode": t.string().optional(),
            "organizationalUnit": t.string().optional(),
            "commonName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubjectOut"])
    types["RevokedCertificateIn"] = t.struct(
        {
            "hexSerialNumber": t.string().optional(),
            "revocationReason": t.string().optional(),
            "certificate": t.string().optional(),
        }
    ).named(renames["RevokedCertificateIn"])
    types["RevokedCertificateOut"] = t.struct(
        {
            "hexSerialNumber": t.string().optional(),
            "revocationReason": t.string().optional(),
            "certificate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RevokedCertificateOut"])
    types["PublicKeyIn"] = t.struct({"key": t.string(), "format": t.string()}).named(
        renames["PublicKeyIn"]
    )
    types["PublicKeyOut"] = t.struct(
        {
            "key": t.string(),
            "format": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublicKeyOut"])
    types["PublishingOptionsIn"] = t.struct(
        {"publishCrl": t.boolean().optional(), "publishCaCert": t.boolean().optional()}
    ).named(renames["PublishingOptionsIn"])
    types["PublishingOptionsOut"] = t.struct(
        {
            "publishCrl": t.boolean().optional(),
            "publishCaCert": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublishingOptionsOut"])
    types["IssuanceModesIn"] = t.struct(
        {
            "allowCsrBasedIssuance": t.boolean().optional(),
            "allowConfigBasedIssuance": t.boolean().optional(),
        }
    ).named(renames["IssuanceModesIn"])
    types["IssuanceModesOut"] = t.struct(
        {
            "allowCsrBasedIssuance": t.boolean().optional(),
            "allowConfigBasedIssuance": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IssuanceModesOut"])
    types["CertificateTemplateIn"] = t.struct(
        {
            "description": t.string().optional(),
            "predefinedValues": t.proxy(renames["X509ParametersIn"]).optional(),
            "identityConstraints": t.proxy(
                renames["CertificateIdentityConstraintsIn"]
            ).optional(),
            "passthroughExtensions": t.proxy(
                renames["CertificateExtensionConstraintsIn"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["CertificateTemplateIn"])
    types["CertificateTemplateOut"] = t.struct(
        {
            "description": t.string().optional(),
            "predefinedValues": t.proxy(renames["X509ParametersOut"]).optional(),
            "identityConstraints": t.proxy(
                renames["CertificateIdentityConstraintsOut"]
            ).optional(),
            "passthroughExtensions": t.proxy(
                renames["CertificateExtensionConstraintsOut"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateTemplateOut"])
    types["DisableCertificateAuthorityRequestIn"] = t.struct(
        {
            "requestId": t.string().optional(),
            "ignoreDependentResources": t.boolean().optional(),
        }
    ).named(renames["DisableCertificateAuthorityRequestIn"])
    types["DisableCertificateAuthorityRequestOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "ignoreDependentResources": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DisableCertificateAuthorityRequestOut"])
    types["AccessUrlsIn"] = t.struct(
        {
            "caCertificateAccessUrl": t.string().optional(),
            "crlAccessUrls": t.array(t.string()).optional(),
        }
    ).named(renames["AccessUrlsIn"])
    types["AccessUrlsOut"] = t.struct(
        {
            "caCertificateAccessUrl": t.string().optional(),
            "crlAccessUrls": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccessUrlsOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["CaPoolIn"] = t.struct(
        {
            "publishingOptions": t.proxy(renames["PublishingOptionsIn"]).optional(),
            "issuancePolicy": t.proxy(renames["IssuancePolicyIn"]).optional(),
            "tier": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["CaPoolIn"])
    types["CaPoolOut"] = t.struct(
        {
            "name": t.string().optional(),
            "publishingOptions": t.proxy(renames["PublishingOptionsOut"]).optional(),
            "issuancePolicy": t.proxy(renames["IssuancePolicyOut"]).optional(),
            "tier": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CaPoolOut"])
    types["CertificateRevocationListIn"] = t.struct(
        {"labels": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["CertificateRevocationListIn"])
    types["CertificateRevocationListOut"] = t.struct(
        {
            "name": t.string().optional(),
            "revokedCertificates": t.array(
                t.proxy(renames["RevokedCertificateOut"])
            ).optional(),
            "pemCrl": t.string().optional(),
            "accessUrl": t.string().optional(),
            "sequenceNumber": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "revisionId": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateRevocationListOut"])
    types["FetchCaCertsResponseIn"] = t.struct(
        {"caCerts": t.array(t.proxy(renames["CertChainIn"])).optional()}
    ).named(renames["FetchCaCertsResponseIn"])
    types["FetchCaCertsResponseOut"] = t.struct(
        {
            "caCerts": t.array(t.proxy(renames["CertChainOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FetchCaCertsResponseOut"])
    types["NameConstraintsIn"] = t.struct(
        {
            "permittedEmailAddresses": t.array(t.string()).optional(),
            "excludedEmailAddresses": t.array(t.string()).optional(),
            "permittedIpRanges": t.array(t.string()).optional(),
            "excludedIpRanges": t.array(t.string()).optional(),
            "permittedDnsNames": t.array(t.string()).optional(),
            "permittedUris": t.array(t.string()).optional(),
            "critical": t.boolean().optional(),
            "excludedDnsNames": t.array(t.string()).optional(),
            "excludedUris": t.array(t.string()).optional(),
        }
    ).named(renames["NameConstraintsIn"])
    types["NameConstraintsOut"] = t.struct(
        {
            "permittedEmailAddresses": t.array(t.string()).optional(),
            "excludedEmailAddresses": t.array(t.string()).optional(),
            "permittedIpRanges": t.array(t.string()).optional(),
            "excludedIpRanges": t.array(t.string()).optional(),
            "permittedDnsNames": t.array(t.string()).optional(),
            "permittedUris": t.array(t.string()).optional(),
            "critical": t.boolean().optional(),
            "excludedDnsNames": t.array(t.string()).optional(),
            "excludedUris": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NameConstraintsOut"])
    types["X509ExtensionIn"] = t.struct(
        {
            "value": t.string(),
            "objectId": t.proxy(renames["ObjectIdIn"]),
            "critical": t.boolean().optional(),
        }
    ).named(renames["X509ExtensionIn"])
    types["X509ExtensionOut"] = t.struct(
        {
            "value": t.string(),
            "objectId": t.proxy(renames["ObjectIdOut"]),
            "critical": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["X509ExtensionOut"])
    types["StatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["CertificateConfigIn"] = t.struct(
        {
            "subjectConfig": t.proxy(renames["SubjectConfigIn"]),
            "publicKey": t.proxy(renames["PublicKeyIn"]).optional(),
            "x509Config": t.proxy(renames["X509ParametersIn"]),
        }
    ).named(renames["CertificateConfigIn"])
    types["CertificateConfigOut"] = t.struct(
        {
            "subjectConfig": t.proxy(renames["SubjectConfigOut"]),
            "publicKey": t.proxy(renames["PublicKeyOut"]).optional(),
            "x509Config": t.proxy(renames["X509ParametersOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateConfigOut"])
    types["LocationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
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
    types["ListCertificateRevocationListsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "certificateRevocationLists": t.array(
                t.proxy(renames["CertificateRevocationListIn"])
            ).optional(),
        }
    ).named(renames["ListCertificateRevocationListsResponseIn"])
    types["ListCertificateRevocationListsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "certificateRevocationLists": t.array(
                t.proxy(renames["CertificateRevocationListOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCertificateRevocationListsResponseOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["CertificateExtensionConstraintsIn"] = t.struct(
        {
            "knownExtensions": t.array(t.string()).optional(),
            "additionalExtensions": t.array(t.proxy(renames["ObjectIdIn"])).optional(),
        }
    ).named(renames["CertificateExtensionConstraintsIn"])
    types["CertificateExtensionConstraintsOut"] = t.struct(
        {
            "knownExtensions": t.array(t.string()).optional(),
            "additionalExtensions": t.array(t.proxy(renames["ObjectIdOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateExtensionConstraintsOut"])
    types["SubjectAltNamesIn"] = t.struct(
        {
            "ipAddresses": t.array(t.string()).optional(),
            "emailAddresses": t.array(t.string()).optional(),
            "dnsNames": t.array(t.string()).optional(),
            "uris": t.array(t.string()).optional(),
            "customSans": t.array(t.proxy(renames["X509ExtensionIn"])).optional(),
        }
    ).named(renames["SubjectAltNamesIn"])
    types["SubjectAltNamesOut"] = t.struct(
        {
            "ipAddresses": t.array(t.string()).optional(),
            "emailAddresses": t.array(t.string()).optional(),
            "dnsNames": t.array(t.string()).optional(),
            "uris": t.array(t.string()).optional(),
            "customSans": t.array(t.proxy(renames["X509ExtensionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubjectAltNamesOut"])
    types["ObjectIdIn"] = t.struct({"objectIdPath": t.array(t.integer())}).named(
        renames["ObjectIdIn"]
    )
    types["ObjectIdOut"] = t.struct(
        {
            "objectIdPath": t.array(t.integer()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ObjectIdOut"])
    types["FetchCaCertsRequestIn"] = t.struct(
        {"requestId": t.string().optional()}
    ).named(renames["FetchCaCertsRequestIn"])
    types["FetchCaCertsRequestOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FetchCaCertsRequestOut"])
    types["FetchCertificateAuthorityCsrResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["FetchCertificateAuthorityCsrResponseIn"])
    types["FetchCertificateAuthorityCsrResponseOut"] = t.struct(
        {
            "pemCsr": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FetchCertificateAuthorityCsrResponseOut"])
    types["EcKeyTypeIn"] = t.struct(
        {"signatureAlgorithm": t.string().optional()}
    ).named(renames["EcKeyTypeIn"])
    types["EcKeyTypeOut"] = t.struct(
        {
            "signatureAlgorithm": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EcKeyTypeOut"])
    types["CaOptionsIn"] = t.struct(
        {"isCa": t.boolean().optional(), "maxIssuerPathLength": t.integer().optional()}
    ).named(renames["CaOptionsIn"])
    types["CaOptionsOut"] = t.struct(
        {
            "isCa": t.boolean().optional(),
            "maxIssuerPathLength": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CaOptionsOut"])
    types["CertificateFingerprintIn"] = t.struct(
        {"sha256Hash": t.string().optional()}
    ).named(renames["CertificateFingerprintIn"])
    types["CertificateFingerprintOut"] = t.struct(
        {
            "sha256Hash": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateFingerprintOut"])
    types["CertificateAuthorityIn"] = t.struct(
        {
            "type": t.string(),
            "subordinateConfig": t.proxy(renames["SubordinateConfigIn"]).optional(),
            "lifetime": t.string(),
            "config": t.proxy(renames["CertificateConfigIn"]),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "gcsBucket": t.string().optional(),
            "keySpec": t.proxy(renames["KeyVersionSpecIn"]),
        }
    ).named(renames["CertificateAuthorityIn"])
    types["CertificateAuthorityOut"] = t.struct(
        {
            "caCertificateDescriptions": t.array(
                t.proxy(renames["CertificateDescriptionOut"])
            ).optional(),
            "type": t.string(),
            "accessUrls": t.proxy(renames["AccessUrlsOut"]).optional(),
            "subordinateConfig": t.proxy(renames["SubordinateConfigOut"]).optional(),
            "expireTime": t.string().optional(),
            "lifetime": t.string(),
            "config": t.proxy(renames["CertificateConfigOut"]),
            "deleteTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "gcsBucket": t.string().optional(),
            "createTime": t.string().optional(),
            "keySpec": t.proxy(renames["KeyVersionSpecOut"]),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "tier": t.string().optional(),
            "updateTime": t.string().optional(),
            "pemCaCertificates": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateAuthorityOut"])
    types["SubordinateConfigIn"] = t.struct(
        {
            "pemIssuerChain": t.proxy(renames["SubordinateConfigChainIn"]),
            "certificateAuthority": t.string(),
        }
    ).named(renames["SubordinateConfigIn"])
    types["SubordinateConfigOut"] = t.struct(
        {
            "pemIssuerChain": t.proxy(renames["SubordinateConfigChainOut"]),
            "certificateAuthority": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubordinateConfigOut"])
    types["ListCertificateTemplatesResponseIn"] = t.struct(
        {
            "certificateTemplates": t.array(
                t.proxy(renames["CertificateTemplateIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListCertificateTemplatesResponseIn"])
    types["ListCertificateTemplatesResponseOut"] = t.struct(
        {
            "certificateTemplates": t.array(
                t.proxy(renames["CertificateTemplateOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCertificateTemplatesResponseOut"])
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
    types["SubordinateConfigChainIn"] = t.struct(
        {"pemCertificates": t.array(t.string())}
    ).named(renames["SubordinateConfigChainIn"])
    types["SubordinateConfigChainOut"] = t.struct(
        {
            "pemCertificates": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubordinateConfigChainOut"])
    types["CertificateIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "pemCsr": t.string().optional(),
            "certificateTemplate": t.string().optional(),
            "subjectMode": t.string().optional(),
            "lifetime": t.string(),
            "config": t.proxy(renames["CertificateConfigIn"]).optional(),
        }
    ).named(renames["CertificateIn"])
    types["CertificateOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "pemCertificateChain": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "pemCsr": t.string().optional(),
            "certificateTemplate": t.string().optional(),
            "subjectMode": t.string().optional(),
            "revocationDetails": t.proxy(renames["RevocationDetailsOut"]).optional(),
            "createTime": t.string().optional(),
            "certificateDescription": t.proxy(
                renames["CertificateDescriptionOut"]
            ).optional(),
            "pemCertificate": t.string().optional(),
            "lifetime": t.string(),
            "issuerCertificateAuthority": t.string().optional(),
            "config": t.proxy(renames["CertificateConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateOut"])
    types["CertificateDescriptionIn"] = t.struct(
        {
            "subjectDescription": t.proxy(renames["SubjectDescriptionIn"]).optional(),
            "x509Description": t.proxy(renames["X509ParametersIn"]).optional(),
            "aiaIssuingCertificateUrls": t.array(t.string()).optional(),
            "authorityKeyId": t.proxy(renames["KeyIdIn"]).optional(),
            "crlDistributionPoints": t.array(t.string()).optional(),
            "certFingerprint": t.proxy(renames["CertificateFingerprintIn"]).optional(),
            "subjectKeyId": t.proxy(renames["KeyIdIn"]).optional(),
            "publicKey": t.proxy(renames["PublicKeyIn"]).optional(),
        }
    ).named(renames["CertificateDescriptionIn"])
    types["CertificateDescriptionOut"] = t.struct(
        {
            "subjectDescription": t.proxy(renames["SubjectDescriptionOut"]).optional(),
            "x509Description": t.proxy(renames["X509ParametersOut"]).optional(),
            "aiaIssuingCertificateUrls": t.array(t.string()).optional(),
            "authorityKeyId": t.proxy(renames["KeyIdOut"]).optional(),
            "crlDistributionPoints": t.array(t.string()).optional(),
            "certFingerprint": t.proxy(renames["CertificateFingerprintOut"]).optional(),
            "subjectKeyId": t.proxy(renames["KeyIdOut"]).optional(),
            "publicKey": t.proxy(renames["PublicKeyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateDescriptionOut"])
    types["SubjectConfigIn"] = t.struct(
        {
            "subjectAltName": t.proxy(renames["SubjectAltNamesIn"]).optional(),
            "subject": t.proxy(renames["SubjectIn"]),
        }
    ).named(renames["SubjectConfigIn"])
    types["SubjectConfigOut"] = t.struct(
        {
            "subjectAltName": t.proxy(renames["SubjectAltNamesOut"]).optional(),
            "subject": t.proxy(renames["SubjectOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubjectConfigOut"])
    types["KeyUsageIn"] = t.struct(
        {
            "baseKeyUsage": t.proxy(renames["KeyUsageOptionsIn"]).optional(),
            "unknownExtendedKeyUsages": t.array(
                t.proxy(renames["ObjectIdIn"])
            ).optional(),
            "extendedKeyUsage": t.proxy(
                renames["ExtendedKeyUsageOptionsIn"]
            ).optional(),
        }
    ).named(renames["KeyUsageIn"])
    types["KeyUsageOut"] = t.struct(
        {
            "baseKeyUsage": t.proxy(renames["KeyUsageOptionsOut"]).optional(),
            "unknownExtendedKeyUsages": t.array(
                t.proxy(renames["ObjectIdOut"])
            ).optional(),
            "extendedKeyUsage": t.proxy(
                renames["ExtendedKeyUsageOptionsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyUsageOut"])
    types["ListCertificatesResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "certificates": t.array(t.proxy(renames["CertificateIn"])).optional(),
        }
    ).named(renames["ListCertificatesResponseIn"])
    types["ListCertificatesResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "certificates": t.array(t.proxy(renames["CertificateOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCertificatesResponseOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
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
    types["KeyIdIn"] = t.struct({"keyId": t.string().optional()}).named(
        renames["KeyIdIn"]
    )
    types["KeyIdOut"] = t.struct(
        {
            "keyId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyIdOut"])
    types["ListCertificateAuthoritiesResponseIn"] = t.struct(
        {
            "certificateAuthorities": t.array(
                t.proxy(renames["CertificateAuthorityIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListCertificateAuthoritiesResponseIn"])
    types["ListCertificateAuthoritiesResponseOut"] = t.struct(
        {
            "certificateAuthorities": t.array(
                t.proxy(renames["CertificateAuthorityOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCertificateAuthoritiesResponseOut"])
    types["AllowedKeyTypeIn"] = t.struct(
        {
            "ellipticCurve": t.proxy(renames["EcKeyTypeIn"]).optional(),
            "rsa": t.proxy(renames["RsaKeyTypeIn"]).optional(),
        }
    ).named(renames["AllowedKeyTypeIn"])
    types["AllowedKeyTypeOut"] = t.struct(
        {
            "ellipticCurve": t.proxy(renames["EcKeyTypeOut"]).optional(),
            "rsa": t.proxy(renames["RsaKeyTypeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AllowedKeyTypeOut"])
    types["UndeleteCertificateAuthorityRequestIn"] = t.struct(
        {"requestId": t.string().optional()}
    ).named(renames["UndeleteCertificateAuthorityRequestIn"])
    types["UndeleteCertificateAuthorityRequestOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UndeleteCertificateAuthorityRequestOut"])
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
    types["OperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["SubjectDescriptionIn"] = t.struct(
        {
            "notBeforeTime": t.string().optional(),
            "subject": t.proxy(renames["SubjectIn"]).optional(),
            "notAfterTime": t.string().optional(),
            "subjectAltName": t.proxy(renames["SubjectAltNamesIn"]).optional(),
            "lifetime": t.string().optional(),
            "hexSerialNumber": t.string().optional(),
        }
    ).named(renames["SubjectDescriptionIn"])
    types["SubjectDescriptionOut"] = t.struct(
        {
            "notBeforeTime": t.string().optional(),
            "subject": t.proxy(renames["SubjectOut"]).optional(),
            "notAfterTime": t.string().optional(),
            "subjectAltName": t.proxy(renames["SubjectAltNamesOut"]).optional(),
            "lifetime": t.string().optional(),
            "hexSerialNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubjectDescriptionOut"])
    types["X509ParametersIn"] = t.struct(
        {
            "additionalExtensions": t.array(
                t.proxy(renames["X509ExtensionIn"])
            ).optional(),
            "policyIds": t.array(t.proxy(renames["ObjectIdIn"])).optional(),
            "nameConstraints": t.proxy(renames["NameConstraintsIn"]).optional(),
            "keyUsage": t.proxy(renames["KeyUsageIn"]).optional(),
            "aiaOcspServers": t.array(t.string()).optional(),
            "caOptions": t.proxy(renames["CaOptionsIn"]).optional(),
        }
    ).named(renames["X509ParametersIn"])
    types["X509ParametersOut"] = t.struct(
        {
            "additionalExtensions": t.array(
                t.proxy(renames["X509ExtensionOut"])
            ).optional(),
            "policyIds": t.array(t.proxy(renames["ObjectIdOut"])).optional(),
            "nameConstraints": t.proxy(renames["NameConstraintsOut"]).optional(),
            "keyUsage": t.proxy(renames["KeyUsageOut"]).optional(),
            "aiaOcspServers": t.array(t.string()).optional(),
            "caOptions": t.proxy(renames["CaOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["X509ParametersOut"])
    types["ExtendedKeyUsageOptionsIn"] = t.struct(
        {
            "serverAuth": t.boolean().optional(),
            "codeSigning": t.boolean().optional(),
            "timeStamping": t.boolean().optional(),
            "ocspSigning": t.boolean().optional(),
            "emailProtection": t.boolean().optional(),
            "clientAuth": t.boolean().optional(),
        }
    ).named(renames["ExtendedKeyUsageOptionsIn"])
    types["ExtendedKeyUsageOptionsOut"] = t.struct(
        {
            "serverAuth": t.boolean().optional(),
            "codeSigning": t.boolean().optional(),
            "timeStamping": t.boolean().optional(),
            "ocspSigning": t.boolean().optional(),
            "emailProtection": t.boolean().optional(),
            "clientAuth": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExtendedKeyUsageOptionsOut"])
    types["ListOperationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(t.proxy(renames["OperationIn"])).optional(),
        }
    ).named(renames["ListOperationsResponseIn"])
    types["ListOperationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(t.proxy(renames["OperationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListOperationsResponseOut"])
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
    types["KeyVersionSpecIn"] = t.struct(
        {
            "algorithm": t.string().optional(),
            "cloudKmsKeyVersion": t.string().optional(),
        }
    ).named(renames["KeyVersionSpecIn"])
    types["KeyVersionSpecOut"] = t.struct(
        {
            "algorithm": t.string().optional(),
            "cloudKmsKeyVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyVersionSpecOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["ReconciliationOperationMetadataIn"] = t.struct(
        {
            "exclusiveAction": t.string().optional(),
            "deleteResource": t.boolean().optional(),
        }
    ).named(renames["ReconciliationOperationMetadataIn"])
    types["ReconciliationOperationMetadataOut"] = t.struct(
        {
            "exclusiveAction": t.string().optional(),
            "deleteResource": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReconciliationOperationMetadataOut"])
    types["IssuancePolicyIn"] = t.struct(
        {
            "allowedKeyTypes": t.array(t.proxy(renames["AllowedKeyTypeIn"])).optional(),
            "baselineValues": t.proxy(renames["X509ParametersIn"]).optional(),
            "maximumLifetime": t.string().optional(),
            "passthroughExtensions": t.proxy(
                renames["CertificateExtensionConstraintsIn"]
            ).optional(),
            "identityConstraints": t.proxy(
                renames["CertificateIdentityConstraintsIn"]
            ).optional(),
            "allowedIssuanceModes": t.proxy(renames["IssuanceModesIn"]).optional(),
        }
    ).named(renames["IssuancePolicyIn"])
    types["IssuancePolicyOut"] = t.struct(
        {
            "allowedKeyTypes": t.array(
                t.proxy(renames["AllowedKeyTypeOut"])
            ).optional(),
            "baselineValues": t.proxy(renames["X509ParametersOut"]).optional(),
            "maximumLifetime": t.string().optional(),
            "passthroughExtensions": t.proxy(
                renames["CertificateExtensionConstraintsOut"]
            ).optional(),
            "identityConstraints": t.proxy(
                renames["CertificateIdentityConstraintsOut"]
            ).optional(),
            "allowedIssuanceModes": t.proxy(renames["IssuanceModesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IssuancePolicyOut"])
    types["RevokeCertificateRequestIn"] = t.struct(
        {"requestId": t.string().optional(), "reason": t.string()}
    ).named(renames["RevokeCertificateRequestIn"])
    types["RevokeCertificateRequestOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "reason": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RevokeCertificateRequestOut"])
    types["PolicyIn"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "version": t.integer().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "version": t.integer().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["ListCaPoolsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "caPools": t.array(t.proxy(renames["CaPoolIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListCaPoolsResponseIn"])
    types["ListCaPoolsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "caPools": t.array(t.proxy(renames["CaPoolOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCaPoolsResponseOut"])
    types["KeyUsageOptionsIn"] = t.struct(
        {
            "contentCommitment": t.boolean().optional(),
            "decipherOnly": t.boolean().optional(),
            "encipherOnly": t.boolean().optional(),
            "keyAgreement": t.boolean().optional(),
            "certSign": t.boolean().optional(),
            "dataEncipherment": t.boolean().optional(),
            "keyEncipherment": t.boolean().optional(),
            "digitalSignature": t.boolean().optional(),
            "crlSign": t.boolean().optional(),
        }
    ).named(renames["KeyUsageOptionsIn"])
    types["KeyUsageOptionsOut"] = t.struct(
        {
            "contentCommitment": t.boolean().optional(),
            "decipherOnly": t.boolean().optional(),
            "encipherOnly": t.boolean().optional(),
            "keyAgreement": t.boolean().optional(),
            "certSign": t.boolean().optional(),
            "dataEncipherment": t.boolean().optional(),
            "keyEncipherment": t.boolean().optional(),
            "digitalSignature": t.boolean().optional(),
            "crlSign": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyUsageOptionsOut"])
    types["EnableCertificateAuthorityRequestIn"] = t.struct(
        {"requestId": t.string().optional()}
    ).named(renames["EnableCertificateAuthorityRequestIn"])
    types["EnableCertificateAuthorityRequestOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnableCertificateAuthorityRequestOut"])
    types["ActivateCertificateAuthorityRequestIn"] = t.struct(
        {
            "subordinateConfig": t.proxy(renames["SubordinateConfigIn"]),
            "pemCaCertificate": t.string(),
            "requestId": t.string().optional(),
        }
    ).named(renames["ActivateCertificateAuthorityRequestIn"])
    types["ActivateCertificateAuthorityRequestOut"] = t.struct(
        {
            "subordinateConfig": t.proxy(renames["SubordinateConfigOut"]),
            "pemCaCertificate": t.string(),
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActivateCertificateAuthorityRequestOut"])
    types["CertChainIn"] = t.struct(
        {"certificates": t.array(t.string()).optional()}
    ).named(renames["CertChainIn"])
    types["CertChainOut"] = t.struct(
        {
            "certificates": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertChainOut"])
    types["RevocationDetailsIn"] = t.struct(
        {
            "revocationTime": t.string().optional(),
            "revocationState": t.string().optional(),
        }
    ).named(renames["RevocationDetailsIn"])
    types["RevocationDetailsOut"] = t.struct(
        {
            "revocationTime": t.string().optional(),
            "revocationState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RevocationDetailsOut"])
    types["RsaKeyTypeIn"] = t.struct(
        {
            "minModulusSize": t.string().optional(),
            "maxModulusSize": t.string().optional(),
        }
    ).named(renames["RsaKeyTypeIn"])
    types["RsaKeyTypeOut"] = t.struct(
        {
            "minModulusSize": t.string().optional(),
            "maxModulusSize": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RsaKeyTypeOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "apiVersion": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "endTime": t.string().optional(),
            "target": t.string().optional(),
            "verb": t.string().optional(),
            "createTime": t.string().optional(),
            "statusMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["CertificateIdentityConstraintsIn"] = t.struct(
        {
            "allowSubjectPassthrough": t.boolean(),
            "allowSubjectAltNamesPassthrough": t.boolean(),
            "celExpression": t.proxy(renames["ExprIn"]).optional(),
        }
    ).named(renames["CertificateIdentityConstraintsIn"])
    types["CertificateIdentityConstraintsOut"] = t.struct(
        {
            "allowSubjectPassthrough": t.boolean(),
            "allowSubjectAltNamesPassthrough": t.boolean(),
            "celExpression": t.proxy(renames["ExprOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateIdentityConstraintsOut"])

    functions = {}
    functions["projectsLocationsGet"] = privateca.get(
        "v1/{name}/locations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsList"] = privateca.get(
        "v1/{name}/locations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsList"] = privateca.post(
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
    functions["projectsLocationsCaPoolsDelete"] = privateca.post(
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
    functions["projectsLocationsCaPoolsPatch"] = privateca.post(
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
    functions["projectsLocationsCaPoolsFetchCaCerts"] = privateca.post(
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
    functions["projectsLocationsCaPoolsGet"] = privateca.post(
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
    functions["projectsLocationsCaPoolsGetIamPolicy"] = privateca.post(
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
    functions["projectsLocationsCaPoolsSetIamPolicy"] = privateca.post(
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
    functions["projectsLocationsCaPoolsCreate"] = privateca.post(
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
    functions["projectsLocationsCaPoolsTestIamPermissions"] = privateca.post(
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
    functions["projectsLocationsCaPoolsCertificatesList"] = privateca.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "requestId": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "pemCsr": t.string().optional(),
                "certificateTemplate": t.string().optional(),
                "subjectMode": t.string().optional(),
                "lifetime": t.string(),
                "config": t.proxy(renames["CertificateConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CertificateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsCertificatesGet"] = privateca.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "requestId": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "pemCsr": t.string().optional(),
                "certificateTemplate": t.string().optional(),
                "subjectMode": t.string().optional(),
                "lifetime": t.string(),
                "config": t.proxy(renames["CertificateConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CertificateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsCertificatesRevoke"] = privateca.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "requestId": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "pemCsr": t.string().optional(),
                "certificateTemplate": t.string().optional(),
                "subjectMode": t.string().optional(),
                "lifetime": t.string(),
                "config": t.proxy(renames["CertificateConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CertificateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsCertificatesCreate"] = privateca.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "requestId": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "pemCsr": t.string().optional(),
                "certificateTemplate": t.string().optional(),
                "subjectMode": t.string().optional(),
                "lifetime": t.string(),
                "config": t.proxy(renames["CertificateConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CertificateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsCertificatesPatch"] = privateca.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "requestId": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "pemCsr": t.string().optional(),
                "certificateTemplate": t.string().optional(),
                "subjectMode": t.string().optional(),
                "lifetime": t.string(),
                "config": t.proxy(renames["CertificateConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CertificateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsCertificateAuthoritiesGet"] = privateca.delete(
        "v1/{name}",
        t.struct(
            {
                "ignoreActiveCertificates": t.boolean().optional(),
                "requestId": t.string().optional(),
                "skipGracePeriod": t.boolean().optional(),
                "name": t.string(),
                "ignoreDependentResources": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCaPoolsCertificateAuthoritiesDisable"
    ] = privateca.delete(
        "v1/{name}",
        t.struct(
            {
                "ignoreActiveCertificates": t.boolean().optional(),
                "requestId": t.string().optional(),
                "skipGracePeriod": t.boolean().optional(),
                "name": t.string(),
                "ignoreDependentResources": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCaPoolsCertificateAuthoritiesCreate"
    ] = privateca.delete(
        "v1/{name}",
        t.struct(
            {
                "ignoreActiveCertificates": t.boolean().optional(),
                "requestId": t.string().optional(),
                "skipGracePeriod": t.boolean().optional(),
                "name": t.string(),
                "ignoreDependentResources": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCaPoolsCertificateAuthoritiesActivate"
    ] = privateca.delete(
        "v1/{name}",
        t.struct(
            {
                "ignoreActiveCertificates": t.boolean().optional(),
                "requestId": t.string().optional(),
                "skipGracePeriod": t.boolean().optional(),
                "name": t.string(),
                "ignoreDependentResources": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsCertificateAuthoritiesList"] = privateca.delete(
        "v1/{name}",
        t.struct(
            {
                "ignoreActiveCertificates": t.boolean().optional(),
                "requestId": t.string().optional(),
                "skipGracePeriod": t.boolean().optional(),
                "name": t.string(),
                "ignoreDependentResources": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsCertificateAuthoritiesPatch"] = privateca.delete(
        "v1/{name}",
        t.struct(
            {
                "ignoreActiveCertificates": t.boolean().optional(),
                "requestId": t.string().optional(),
                "skipGracePeriod": t.boolean().optional(),
                "name": t.string(),
                "ignoreDependentResources": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCaPoolsCertificateAuthoritiesUndelete"
    ] = privateca.delete(
        "v1/{name}",
        t.struct(
            {
                "ignoreActiveCertificates": t.boolean().optional(),
                "requestId": t.string().optional(),
                "skipGracePeriod": t.boolean().optional(),
                "name": t.string(),
                "ignoreDependentResources": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCaPoolsCertificateAuthoritiesEnable"
    ] = privateca.delete(
        "v1/{name}",
        t.struct(
            {
                "ignoreActiveCertificates": t.boolean().optional(),
                "requestId": t.string().optional(),
                "skipGracePeriod": t.boolean().optional(),
                "name": t.string(),
                "ignoreDependentResources": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsCertificateAuthoritiesFetch"] = privateca.delete(
        "v1/{name}",
        t.struct(
            {
                "ignoreActiveCertificates": t.boolean().optional(),
                "requestId": t.string().optional(),
                "skipGracePeriod": t.boolean().optional(),
                "name": t.string(),
                "ignoreDependentResources": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCaPoolsCertificateAuthoritiesDelete"
    ] = privateca.delete(
        "v1/{name}",
        t.struct(
            {
                "ignoreActiveCertificates": t.boolean().optional(),
                "requestId": t.string().optional(),
                "skipGracePeriod": t.boolean().optional(),
                "name": t.string(),
                "ignoreDependentResources": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCaPoolsCertificateAuthoritiesCertificateRevocationListsSetIamPolicy"
    ] = privateca.post(
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
    functions[
        "projectsLocationsCaPoolsCertificateAuthoritiesCertificateRevocationListsList"
    ] = privateca.post(
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
    functions[
        "projectsLocationsCaPoolsCertificateAuthoritiesCertificateRevocationListsPatch"
    ] = privateca.post(
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
    functions[
        "projectsLocationsCaPoolsCertificateAuthoritiesCertificateRevocationListsGet"
    ] = privateca.post(
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
    functions[
        "projectsLocationsCaPoolsCertificateAuthoritiesCertificateRevocationListsGetIamPolicy"
    ] = privateca.post(
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
    functions[
        "projectsLocationsCaPoolsCertificateAuthoritiesCertificateRevocationListsTestIamPermissions"
    ] = privateca.post(
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
    functions["projectsLocationsOperationsCancel"] = privateca.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = privateca.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = privateca.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = privateca.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCertificateTemplatesDelete"] = privateca.post(
        "v1/{parent}/certificateTemplates",
        t.struct(
            {
                "certificateTemplateId": t.string(),
                "requestId": t.string().optional(),
                "parent": t.string(),
                "description": t.string().optional(),
                "predefinedValues": t.proxy(renames["X509ParametersIn"]).optional(),
                "identityConstraints": t.proxy(
                    renames["CertificateIdentityConstraintsIn"]
                ).optional(),
                "passthroughExtensions": t.proxy(
                    renames["CertificateExtensionConstraintsIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCertificateTemplatesList"] = privateca.post(
        "v1/{parent}/certificateTemplates",
        t.struct(
            {
                "certificateTemplateId": t.string(),
                "requestId": t.string().optional(),
                "parent": t.string(),
                "description": t.string().optional(),
                "predefinedValues": t.proxy(renames["X509ParametersIn"]).optional(),
                "identityConstraints": t.proxy(
                    renames["CertificateIdentityConstraintsIn"]
                ).optional(),
                "passthroughExtensions": t.proxy(
                    renames["CertificateExtensionConstraintsIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCertificateTemplatesGetIamPolicy"] = privateca.post(
        "v1/{parent}/certificateTemplates",
        t.struct(
            {
                "certificateTemplateId": t.string(),
                "requestId": t.string().optional(),
                "parent": t.string(),
                "description": t.string().optional(),
                "predefinedValues": t.proxy(renames["X509ParametersIn"]).optional(),
                "identityConstraints": t.proxy(
                    renames["CertificateIdentityConstraintsIn"]
                ).optional(),
                "passthroughExtensions": t.proxy(
                    renames["CertificateExtensionConstraintsIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCertificateTemplatesSetIamPolicy"] = privateca.post(
        "v1/{parent}/certificateTemplates",
        t.struct(
            {
                "certificateTemplateId": t.string(),
                "requestId": t.string().optional(),
                "parent": t.string(),
                "description": t.string().optional(),
                "predefinedValues": t.proxy(renames["X509ParametersIn"]).optional(),
                "identityConstraints": t.proxy(
                    renames["CertificateIdentityConstraintsIn"]
                ).optional(),
                "passthroughExtensions": t.proxy(
                    renames["CertificateExtensionConstraintsIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCertificateTemplatesPatch"] = privateca.post(
        "v1/{parent}/certificateTemplates",
        t.struct(
            {
                "certificateTemplateId": t.string(),
                "requestId": t.string().optional(),
                "parent": t.string(),
                "description": t.string().optional(),
                "predefinedValues": t.proxy(renames["X509ParametersIn"]).optional(),
                "identityConstraints": t.proxy(
                    renames["CertificateIdentityConstraintsIn"]
                ).optional(),
                "passthroughExtensions": t.proxy(
                    renames["CertificateExtensionConstraintsIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCertificateTemplatesTestIamPermissions"
    ] = privateca.post(
        "v1/{parent}/certificateTemplates",
        t.struct(
            {
                "certificateTemplateId": t.string(),
                "requestId": t.string().optional(),
                "parent": t.string(),
                "description": t.string().optional(),
                "predefinedValues": t.proxy(renames["X509ParametersIn"]).optional(),
                "identityConstraints": t.proxy(
                    renames["CertificateIdentityConstraintsIn"]
                ).optional(),
                "passthroughExtensions": t.proxy(
                    renames["CertificateExtensionConstraintsIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCertificateTemplatesGet"] = privateca.post(
        "v1/{parent}/certificateTemplates",
        t.struct(
            {
                "certificateTemplateId": t.string(),
                "requestId": t.string().optional(),
                "parent": t.string(),
                "description": t.string().optional(),
                "predefinedValues": t.proxy(renames["X509ParametersIn"]).optional(),
                "identityConstraints": t.proxy(
                    renames["CertificateIdentityConstraintsIn"]
                ).optional(),
                "passthroughExtensions": t.proxy(
                    renames["CertificateExtensionConstraintsIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCertificateTemplatesCreate"] = privateca.post(
        "v1/{parent}/certificateTemplates",
        t.struct(
            {
                "certificateTemplateId": t.string(),
                "requestId": t.string().optional(),
                "parent": t.string(),
                "description": t.string().optional(),
                "predefinedValues": t.proxy(renames["X509ParametersIn"]).optional(),
                "identityConstraints": t.proxy(
                    renames["CertificateIdentityConstraintsIn"]
                ).optional(),
                "passthroughExtensions": t.proxy(
                    renames["CertificateExtensionConstraintsIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="privateca",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
