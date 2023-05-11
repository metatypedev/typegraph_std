from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_privateca() -> Import:
    privateca = HTTPRuntime("https://privateca.googleapis.com/")

    renames = {
        "ErrorResponse": "_privateca_1_ErrorResponse",
        "AuditLogConfigIn": "_privateca_2_AuditLogConfigIn",
        "AuditLogConfigOut": "_privateca_3_AuditLogConfigOut",
        "KeyIdIn": "_privateca_4_KeyIdIn",
        "KeyIdOut": "_privateca_5_KeyIdOut",
        "ListCertificateRevocationListsResponseIn": "_privateca_6_ListCertificateRevocationListsResponseIn",
        "ListCertificateRevocationListsResponseOut": "_privateca_7_ListCertificateRevocationListsResponseOut",
        "SubordinateConfigIn": "_privateca_8_SubordinateConfigIn",
        "SubordinateConfigOut": "_privateca_9_SubordinateConfigOut",
        "PublicKeyIn": "_privateca_10_PublicKeyIn",
        "PublicKeyOut": "_privateca_11_PublicKeyOut",
        "ListCertificateAuthoritiesResponseIn": "_privateca_12_ListCertificateAuthoritiesResponseIn",
        "ListCertificateAuthoritiesResponseOut": "_privateca_13_ListCertificateAuthoritiesResponseOut",
        "TestIamPermissionsRequestIn": "_privateca_14_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_privateca_15_TestIamPermissionsRequestOut",
        "ListCertificateTemplatesResponseIn": "_privateca_16_ListCertificateTemplatesResponseIn",
        "ListCertificateTemplatesResponseOut": "_privateca_17_ListCertificateTemplatesResponseOut",
        "EcKeyTypeIn": "_privateca_18_EcKeyTypeIn",
        "EcKeyTypeOut": "_privateca_19_EcKeyTypeOut",
        "SubjectAltNamesIn": "_privateca_20_SubjectAltNamesIn",
        "SubjectAltNamesOut": "_privateca_21_SubjectAltNamesOut",
        "CertChainIn": "_privateca_22_CertChainIn",
        "CertChainOut": "_privateca_23_CertChainOut",
        "IssuanceModesIn": "_privateca_24_IssuanceModesIn",
        "IssuanceModesOut": "_privateca_25_IssuanceModesOut",
        "EmptyIn": "_privateca_26_EmptyIn",
        "EmptyOut": "_privateca_27_EmptyOut",
        "ListCaPoolsResponseIn": "_privateca_28_ListCaPoolsResponseIn",
        "ListCaPoolsResponseOut": "_privateca_29_ListCaPoolsResponseOut",
        "TestIamPermissionsResponseIn": "_privateca_30_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_privateca_31_TestIamPermissionsResponseOut",
        "AuditConfigIn": "_privateca_32_AuditConfigIn",
        "AuditConfigOut": "_privateca_33_AuditConfigOut",
        "StatusIn": "_privateca_34_StatusIn",
        "StatusOut": "_privateca_35_StatusOut",
        "RevocationDetailsIn": "_privateca_36_RevocationDetailsIn",
        "RevocationDetailsOut": "_privateca_37_RevocationDetailsOut",
        "FetchCaCertsRequestIn": "_privateca_38_FetchCaCertsRequestIn",
        "FetchCaCertsRequestOut": "_privateca_39_FetchCaCertsRequestOut",
        "KeyUsageIn": "_privateca_40_KeyUsageIn",
        "KeyUsageOut": "_privateca_41_KeyUsageOut",
        "AllowedKeyTypeIn": "_privateca_42_AllowedKeyTypeIn",
        "AllowedKeyTypeOut": "_privateca_43_AllowedKeyTypeOut",
        "ListLocationsResponseIn": "_privateca_44_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_privateca_45_ListLocationsResponseOut",
        "ObjectIdIn": "_privateca_46_ObjectIdIn",
        "ObjectIdOut": "_privateca_47_ObjectIdOut",
        "EnableCertificateAuthorityRequestIn": "_privateca_48_EnableCertificateAuthorityRequestIn",
        "EnableCertificateAuthorityRequestOut": "_privateca_49_EnableCertificateAuthorityRequestOut",
        "CertificateTemplateIn": "_privateca_50_CertificateTemplateIn",
        "CertificateTemplateOut": "_privateca_51_CertificateTemplateOut",
        "KeyUsageOptionsIn": "_privateca_52_KeyUsageOptionsIn",
        "KeyUsageOptionsOut": "_privateca_53_KeyUsageOptionsOut",
        "CertificateFingerprintIn": "_privateca_54_CertificateFingerprintIn",
        "CertificateFingerprintOut": "_privateca_55_CertificateFingerprintOut",
        "RsaKeyTypeIn": "_privateca_56_RsaKeyTypeIn",
        "RsaKeyTypeOut": "_privateca_57_RsaKeyTypeOut",
        "DisableCertificateAuthorityRequestIn": "_privateca_58_DisableCertificateAuthorityRequestIn",
        "DisableCertificateAuthorityRequestOut": "_privateca_59_DisableCertificateAuthorityRequestOut",
        "RevokedCertificateIn": "_privateca_60_RevokedCertificateIn",
        "RevokedCertificateOut": "_privateca_61_RevokedCertificateOut",
        "AccessUrlsIn": "_privateca_62_AccessUrlsIn",
        "AccessUrlsOut": "_privateca_63_AccessUrlsOut",
        "CertificateIdentityConstraintsIn": "_privateca_64_CertificateIdentityConstraintsIn",
        "CertificateIdentityConstraintsOut": "_privateca_65_CertificateIdentityConstraintsOut",
        "CaPoolIn": "_privateca_66_CaPoolIn",
        "CaPoolOut": "_privateca_67_CaPoolOut",
        "IssuancePolicyIn": "_privateca_68_IssuancePolicyIn",
        "IssuancePolicyOut": "_privateca_69_IssuancePolicyOut",
        "CertificateDescriptionIn": "_privateca_70_CertificateDescriptionIn",
        "CertificateDescriptionOut": "_privateca_71_CertificateDescriptionOut",
        "CertificateRevocationListIn": "_privateca_72_CertificateRevocationListIn",
        "CertificateRevocationListOut": "_privateca_73_CertificateRevocationListOut",
        "LocationIn": "_privateca_74_LocationIn",
        "LocationOut": "_privateca_75_LocationOut",
        "CancelOperationRequestIn": "_privateca_76_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_privateca_77_CancelOperationRequestOut",
        "CertificateExtensionConstraintsIn": "_privateca_78_CertificateExtensionConstraintsIn",
        "CertificateExtensionConstraintsOut": "_privateca_79_CertificateExtensionConstraintsOut",
        "OperationMetadataIn": "_privateca_80_OperationMetadataIn",
        "OperationMetadataOut": "_privateca_81_OperationMetadataOut",
        "CaOptionsIn": "_privateca_82_CaOptionsIn",
        "CaOptionsOut": "_privateca_83_CaOptionsOut",
        "PublishingOptionsIn": "_privateca_84_PublishingOptionsIn",
        "PublishingOptionsOut": "_privateca_85_PublishingOptionsOut",
        "X509ExtensionIn": "_privateca_86_X509ExtensionIn",
        "X509ExtensionOut": "_privateca_87_X509ExtensionOut",
        "ReconciliationOperationMetadataIn": "_privateca_88_ReconciliationOperationMetadataIn",
        "ReconciliationOperationMetadataOut": "_privateca_89_ReconciliationOperationMetadataOut",
        "NameConstraintsIn": "_privateca_90_NameConstraintsIn",
        "NameConstraintsOut": "_privateca_91_NameConstraintsOut",
        "OperationIn": "_privateca_92_OperationIn",
        "OperationOut": "_privateca_93_OperationOut",
        "SubjectIn": "_privateca_94_SubjectIn",
        "SubjectOut": "_privateca_95_SubjectOut",
        "CertificateIn": "_privateca_96_CertificateIn",
        "CertificateOut": "_privateca_97_CertificateOut",
        "ActivateCertificateAuthorityRequestIn": "_privateca_98_ActivateCertificateAuthorityRequestIn",
        "ActivateCertificateAuthorityRequestOut": "_privateca_99_ActivateCertificateAuthorityRequestOut",
        "SubordinateConfigChainIn": "_privateca_100_SubordinateConfigChainIn",
        "SubordinateConfigChainOut": "_privateca_101_SubordinateConfigChainOut",
        "FetchCaCertsResponseIn": "_privateca_102_FetchCaCertsResponseIn",
        "FetchCaCertsResponseOut": "_privateca_103_FetchCaCertsResponseOut",
        "SetIamPolicyRequestIn": "_privateca_104_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_privateca_105_SetIamPolicyRequestOut",
        "SubjectConfigIn": "_privateca_106_SubjectConfigIn",
        "SubjectConfigOut": "_privateca_107_SubjectConfigOut",
        "ListCertificatesResponseIn": "_privateca_108_ListCertificatesResponseIn",
        "ListCertificatesResponseOut": "_privateca_109_ListCertificatesResponseOut",
        "PolicyIn": "_privateca_110_PolicyIn",
        "PolicyOut": "_privateca_111_PolicyOut",
        "CertificateAuthorityIn": "_privateca_112_CertificateAuthorityIn",
        "CertificateAuthorityOut": "_privateca_113_CertificateAuthorityOut",
        "SubjectDescriptionIn": "_privateca_114_SubjectDescriptionIn",
        "SubjectDescriptionOut": "_privateca_115_SubjectDescriptionOut",
        "UndeleteCertificateAuthorityRequestIn": "_privateca_116_UndeleteCertificateAuthorityRequestIn",
        "UndeleteCertificateAuthorityRequestOut": "_privateca_117_UndeleteCertificateAuthorityRequestOut",
        "ExprIn": "_privateca_118_ExprIn",
        "ExprOut": "_privateca_119_ExprOut",
        "RevokeCertificateRequestIn": "_privateca_120_RevokeCertificateRequestIn",
        "RevokeCertificateRequestOut": "_privateca_121_RevokeCertificateRequestOut",
        "KeyVersionSpecIn": "_privateca_122_KeyVersionSpecIn",
        "KeyVersionSpecOut": "_privateca_123_KeyVersionSpecOut",
        "BindingIn": "_privateca_124_BindingIn",
        "BindingOut": "_privateca_125_BindingOut",
        "X509ParametersIn": "_privateca_126_X509ParametersIn",
        "X509ParametersOut": "_privateca_127_X509ParametersOut",
        "ListOperationsResponseIn": "_privateca_128_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_privateca_129_ListOperationsResponseOut",
        "ExtendedKeyUsageOptionsIn": "_privateca_130_ExtendedKeyUsageOptionsIn",
        "ExtendedKeyUsageOptionsOut": "_privateca_131_ExtendedKeyUsageOptionsOut",
        "FetchCertificateAuthorityCsrResponseIn": "_privateca_132_FetchCertificateAuthorityCsrResponseIn",
        "FetchCertificateAuthorityCsrResponseOut": "_privateca_133_FetchCertificateAuthorityCsrResponseOut",
        "CertificateConfigIn": "_privateca_134_CertificateConfigIn",
        "CertificateConfigOut": "_privateca_135_CertificateConfigOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["KeyIdIn"] = t.struct({"keyId": t.string().optional()}).named(
        renames["KeyIdIn"]
    )
    types["KeyIdOut"] = t.struct(
        {
            "keyId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyIdOut"])
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
    types["ListCertificateAuthoritiesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "certificateAuthorities": t.array(
                t.proxy(renames["CertificateAuthorityIn"])
            ).optional(),
        }
    ).named(renames["ListCertificateAuthoritiesResponseIn"])
    types["ListCertificateAuthoritiesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "certificateAuthorities": t.array(
                t.proxy(renames["CertificateAuthorityOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCertificateAuthoritiesResponseOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
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
    types["EcKeyTypeIn"] = t.struct(
        {"signatureAlgorithm": t.string().optional()}
    ).named(renames["EcKeyTypeIn"])
    types["EcKeyTypeOut"] = t.struct(
        {
            "signatureAlgorithm": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EcKeyTypeOut"])
    types["SubjectAltNamesIn"] = t.struct(
        {
            "ipAddresses": t.array(t.string()).optional(),
            "uris": t.array(t.string()).optional(),
            "customSans": t.array(t.proxy(renames["X509ExtensionIn"])).optional(),
            "dnsNames": t.array(t.string()).optional(),
            "emailAddresses": t.array(t.string()).optional(),
        }
    ).named(renames["SubjectAltNamesIn"])
    types["SubjectAltNamesOut"] = t.struct(
        {
            "ipAddresses": t.array(t.string()).optional(),
            "uris": t.array(t.string()).optional(),
            "customSans": t.array(t.proxy(renames["X509ExtensionOut"])).optional(),
            "dnsNames": t.array(t.string()).optional(),
            "emailAddresses": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubjectAltNamesOut"])
    types["CertChainIn"] = t.struct(
        {"certificates": t.array(t.string()).optional()}
    ).named(renames["CertChainIn"])
    types["CertChainOut"] = t.struct(
        {
            "certificates": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertChainOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
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
    types["StatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
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
    types["FetchCaCertsRequestIn"] = t.struct(
        {"requestId": t.string().optional()}
    ).named(renames["FetchCaCertsRequestIn"])
    types["FetchCaCertsRequestOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FetchCaCertsRequestOut"])
    types["KeyUsageIn"] = t.struct(
        {
            "unknownExtendedKeyUsages": t.array(
                t.proxy(renames["ObjectIdIn"])
            ).optional(),
            "baseKeyUsage": t.proxy(renames["KeyUsageOptionsIn"]).optional(),
            "extendedKeyUsage": t.proxy(
                renames["ExtendedKeyUsageOptionsIn"]
            ).optional(),
        }
    ).named(renames["KeyUsageIn"])
    types["KeyUsageOut"] = t.struct(
        {
            "unknownExtendedKeyUsages": t.array(
                t.proxy(renames["ObjectIdOut"])
            ).optional(),
            "baseKeyUsage": t.proxy(renames["KeyUsageOptionsOut"]).optional(),
            "extendedKeyUsage": t.proxy(
                renames["ExtendedKeyUsageOptionsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyUsageOut"])
    types["AllowedKeyTypeIn"] = t.struct(
        {
            "rsa": t.proxy(renames["RsaKeyTypeIn"]).optional(),
            "ellipticCurve": t.proxy(renames["EcKeyTypeIn"]).optional(),
        }
    ).named(renames["AllowedKeyTypeIn"])
    types["AllowedKeyTypeOut"] = t.struct(
        {
            "rsa": t.proxy(renames["RsaKeyTypeOut"]).optional(),
            "ellipticCurve": t.proxy(renames["EcKeyTypeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AllowedKeyTypeOut"])
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
    types["ObjectIdIn"] = t.struct({"objectIdPath": t.array(t.integer())}).named(
        renames["ObjectIdIn"]
    )
    types["ObjectIdOut"] = t.struct(
        {
            "objectIdPath": t.array(t.integer()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ObjectIdOut"])
    types["EnableCertificateAuthorityRequestIn"] = t.struct(
        {"requestId": t.string().optional()}
    ).named(renames["EnableCertificateAuthorityRequestIn"])
    types["EnableCertificateAuthorityRequestOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnableCertificateAuthorityRequestOut"])
    types["CertificateTemplateIn"] = t.struct(
        {
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "identityConstraints": t.proxy(
                renames["CertificateIdentityConstraintsIn"]
            ).optional(),
            "predefinedValues": t.proxy(renames["X509ParametersIn"]).optional(),
            "passthroughExtensions": t.proxy(
                renames["CertificateExtensionConstraintsIn"]
            ).optional(),
        }
    ).named(renames["CertificateTemplateIn"])
    types["CertificateTemplateOut"] = t.struct(
        {
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "identityConstraints": t.proxy(
                renames["CertificateIdentityConstraintsOut"]
            ).optional(),
            "predefinedValues": t.proxy(renames["X509ParametersOut"]).optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "passthroughExtensions": t.proxy(
                renames["CertificateExtensionConstraintsOut"]
            ).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateTemplateOut"])
    types["KeyUsageOptionsIn"] = t.struct(
        {
            "keyEncipherment": t.boolean().optional(),
            "dataEncipherment": t.boolean().optional(),
            "decipherOnly": t.boolean().optional(),
            "digitalSignature": t.boolean().optional(),
            "keyAgreement": t.boolean().optional(),
            "contentCommitment": t.boolean().optional(),
            "encipherOnly": t.boolean().optional(),
            "certSign": t.boolean().optional(),
            "crlSign": t.boolean().optional(),
        }
    ).named(renames["KeyUsageOptionsIn"])
    types["KeyUsageOptionsOut"] = t.struct(
        {
            "keyEncipherment": t.boolean().optional(),
            "dataEncipherment": t.boolean().optional(),
            "decipherOnly": t.boolean().optional(),
            "digitalSignature": t.boolean().optional(),
            "keyAgreement": t.boolean().optional(),
            "contentCommitment": t.boolean().optional(),
            "encipherOnly": t.boolean().optional(),
            "certSign": t.boolean().optional(),
            "crlSign": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyUsageOptionsOut"])
    types["CertificateFingerprintIn"] = t.struct(
        {"sha256Hash": t.string().optional()}
    ).named(renames["CertificateFingerprintIn"])
    types["CertificateFingerprintOut"] = t.struct(
        {
            "sha256Hash": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateFingerprintOut"])
    types["RsaKeyTypeIn"] = t.struct(
        {
            "maxModulusSize": t.string().optional(),
            "minModulusSize": t.string().optional(),
        }
    ).named(renames["RsaKeyTypeIn"])
    types["RsaKeyTypeOut"] = t.struct(
        {
            "maxModulusSize": t.string().optional(),
            "minModulusSize": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RsaKeyTypeOut"])
    types["DisableCertificateAuthorityRequestIn"] = t.struct(
        {
            "ignoreDependentResources": t.boolean().optional(),
            "requestId": t.string().optional(),
        }
    ).named(renames["DisableCertificateAuthorityRequestIn"])
    types["DisableCertificateAuthorityRequestOut"] = t.struct(
        {
            "ignoreDependentResources": t.boolean().optional(),
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DisableCertificateAuthorityRequestOut"])
    types["RevokedCertificateIn"] = t.struct(
        {
            "certificate": t.string().optional(),
            "revocationReason": t.string().optional(),
            "hexSerialNumber": t.string().optional(),
        }
    ).named(renames["RevokedCertificateIn"])
    types["RevokedCertificateOut"] = t.struct(
        {
            "certificate": t.string().optional(),
            "revocationReason": t.string().optional(),
            "hexSerialNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RevokedCertificateOut"])
    types["AccessUrlsIn"] = t.struct(
        {
            "crlAccessUrls": t.array(t.string()).optional(),
            "caCertificateAccessUrl": t.string().optional(),
        }
    ).named(renames["AccessUrlsIn"])
    types["AccessUrlsOut"] = t.struct(
        {
            "crlAccessUrls": t.array(t.string()).optional(),
            "caCertificateAccessUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccessUrlsOut"])
    types["CertificateIdentityConstraintsIn"] = t.struct(
        {
            "celExpression": t.proxy(renames["ExprIn"]).optional(),
            "allowSubjectPassthrough": t.boolean(),
            "allowSubjectAltNamesPassthrough": t.boolean(),
        }
    ).named(renames["CertificateIdentityConstraintsIn"])
    types["CertificateIdentityConstraintsOut"] = t.struct(
        {
            "celExpression": t.proxy(renames["ExprOut"]).optional(),
            "allowSubjectPassthrough": t.boolean(),
            "allowSubjectAltNamesPassthrough": t.boolean(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateIdentityConstraintsOut"])
    types["CaPoolIn"] = t.struct(
        {
            "tier": t.string(),
            "issuancePolicy": t.proxy(renames["IssuancePolicyIn"]).optional(),
            "publishingOptions": t.proxy(renames["PublishingOptionsIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["CaPoolIn"])
    types["CaPoolOut"] = t.struct(
        {
            "name": t.string().optional(),
            "tier": t.string(),
            "issuancePolicy": t.proxy(renames["IssuancePolicyOut"]).optional(),
            "publishingOptions": t.proxy(renames["PublishingOptionsOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CaPoolOut"])
    types["IssuancePolicyIn"] = t.struct(
        {
            "maximumLifetime": t.string().optional(),
            "passthroughExtensions": t.proxy(
                renames["CertificateExtensionConstraintsIn"]
            ).optional(),
            "allowedIssuanceModes": t.proxy(renames["IssuanceModesIn"]).optional(),
            "allowedKeyTypes": t.array(t.proxy(renames["AllowedKeyTypeIn"])).optional(),
            "identityConstraints": t.proxy(
                renames["CertificateIdentityConstraintsIn"]
            ).optional(),
            "baselineValues": t.proxy(renames["X509ParametersIn"]).optional(),
        }
    ).named(renames["IssuancePolicyIn"])
    types["IssuancePolicyOut"] = t.struct(
        {
            "maximumLifetime": t.string().optional(),
            "passthroughExtensions": t.proxy(
                renames["CertificateExtensionConstraintsOut"]
            ).optional(),
            "allowedIssuanceModes": t.proxy(renames["IssuanceModesOut"]).optional(),
            "allowedKeyTypes": t.array(
                t.proxy(renames["AllowedKeyTypeOut"])
            ).optional(),
            "identityConstraints": t.proxy(
                renames["CertificateIdentityConstraintsOut"]
            ).optional(),
            "baselineValues": t.proxy(renames["X509ParametersOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IssuancePolicyOut"])
    types["CertificateDescriptionIn"] = t.struct(
        {
            "crlDistributionPoints": t.array(t.string()).optional(),
            "aiaIssuingCertificateUrls": t.array(t.string()).optional(),
            "subjectKeyId": t.proxy(renames["KeyIdIn"]).optional(),
            "subjectDescription": t.proxy(renames["SubjectDescriptionIn"]).optional(),
            "x509Description": t.proxy(renames["X509ParametersIn"]).optional(),
            "publicKey": t.proxy(renames["PublicKeyIn"]).optional(),
            "authorityKeyId": t.proxy(renames["KeyIdIn"]).optional(),
            "certFingerprint": t.proxy(renames["CertificateFingerprintIn"]).optional(),
        }
    ).named(renames["CertificateDescriptionIn"])
    types["CertificateDescriptionOut"] = t.struct(
        {
            "crlDistributionPoints": t.array(t.string()).optional(),
            "aiaIssuingCertificateUrls": t.array(t.string()).optional(),
            "subjectKeyId": t.proxy(renames["KeyIdOut"]).optional(),
            "subjectDescription": t.proxy(renames["SubjectDescriptionOut"]).optional(),
            "x509Description": t.proxy(renames["X509ParametersOut"]).optional(),
            "publicKey": t.proxy(renames["PublicKeyOut"]).optional(),
            "authorityKeyId": t.proxy(renames["KeyIdOut"]).optional(),
            "certFingerprint": t.proxy(renames["CertificateFingerprintOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateDescriptionOut"])
    types["CertificateRevocationListIn"] = t.struct(
        {"labels": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["CertificateRevocationListIn"])
    types["CertificateRevocationListOut"] = t.struct(
        {
            "sequenceNumber": t.string().optional(),
            "updateTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "accessUrl": t.string().optional(),
            "revokedCertificates": t.array(
                t.proxy(renames["RevokedCertificateOut"])
            ).optional(),
            "pemCrl": t.string().optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "revisionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateRevocationListOut"])
    types["LocationIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["CertificateExtensionConstraintsIn"] = t.struct(
        {
            "additionalExtensions": t.array(t.proxy(renames["ObjectIdIn"])).optional(),
            "knownExtensions": t.array(t.string()).optional(),
        }
    ).named(renames["CertificateExtensionConstraintsIn"])
    types["CertificateExtensionConstraintsOut"] = t.struct(
        {
            "additionalExtensions": t.array(t.proxy(renames["ObjectIdOut"])).optional(),
            "knownExtensions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateExtensionConstraintsOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "target": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "statusMessage": t.string().optional(),
            "createTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "endTime": t.string().optional(),
            "verb": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["CaOptionsIn"] = t.struct(
        {"maxIssuerPathLength": t.integer().optional(), "isCa": t.boolean().optional()}
    ).named(renames["CaOptionsIn"])
    types["CaOptionsOut"] = t.struct(
        {
            "maxIssuerPathLength": t.integer().optional(),
            "isCa": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CaOptionsOut"])
    types["PublishingOptionsIn"] = t.struct(
        {"publishCaCert": t.boolean().optional(), "publishCrl": t.boolean().optional()}
    ).named(renames["PublishingOptionsIn"])
    types["PublishingOptionsOut"] = t.struct(
        {
            "publishCaCert": t.boolean().optional(),
            "publishCrl": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublishingOptionsOut"])
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
    types["ReconciliationOperationMetadataIn"] = t.struct(
        {
            "deleteResource": t.boolean().optional(),
            "exclusiveAction": t.string().optional(),
        }
    ).named(renames["ReconciliationOperationMetadataIn"])
    types["ReconciliationOperationMetadataOut"] = t.struct(
        {
            "deleteResource": t.boolean().optional(),
            "exclusiveAction": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReconciliationOperationMetadataOut"])
    types["NameConstraintsIn"] = t.struct(
        {
            "excludedEmailAddresses": t.array(t.string()).optional(),
            "permittedIpRanges": t.array(t.string()).optional(),
            "permittedEmailAddresses": t.array(t.string()).optional(),
            "excludedIpRanges": t.array(t.string()).optional(),
            "critical": t.boolean().optional(),
            "excludedDnsNames": t.array(t.string()).optional(),
            "permittedDnsNames": t.array(t.string()).optional(),
            "permittedUris": t.array(t.string()).optional(),
            "excludedUris": t.array(t.string()).optional(),
        }
    ).named(renames["NameConstraintsIn"])
    types["NameConstraintsOut"] = t.struct(
        {
            "excludedEmailAddresses": t.array(t.string()).optional(),
            "permittedIpRanges": t.array(t.string()).optional(),
            "permittedEmailAddresses": t.array(t.string()).optional(),
            "excludedIpRanges": t.array(t.string()).optional(),
            "critical": t.boolean().optional(),
            "excludedDnsNames": t.array(t.string()).optional(),
            "permittedDnsNames": t.array(t.string()).optional(),
            "permittedUris": t.array(t.string()).optional(),
            "excludedUris": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NameConstraintsOut"])
    types["OperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
    types["SubjectIn"] = t.struct(
        {
            "commonName": t.string().optional(),
            "postalCode": t.string().optional(),
            "organizationalUnit": t.string().optional(),
            "locality": t.string().optional(),
            "streetAddress": t.string().optional(),
            "countryCode": t.string().optional(),
            "organization": t.string().optional(),
            "province": t.string().optional(),
        }
    ).named(renames["SubjectIn"])
    types["SubjectOut"] = t.struct(
        {
            "commonName": t.string().optional(),
            "postalCode": t.string().optional(),
            "organizationalUnit": t.string().optional(),
            "locality": t.string().optional(),
            "streetAddress": t.string().optional(),
            "countryCode": t.string().optional(),
            "organization": t.string().optional(),
            "province": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubjectOut"])
    types["CertificateIn"] = t.struct(
        {
            "certificateTemplate": t.string().optional(),
            "lifetime": t.string(),
            "config": t.proxy(renames["CertificateConfigIn"]).optional(),
            "subjectMode": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "pemCsr": t.string().optional(),
        }
    ).named(renames["CertificateIn"])
    types["CertificateOut"] = t.struct(
        {
            "certificateTemplate": t.string().optional(),
            "lifetime": t.string(),
            "certificateDescription": t.proxy(
                renames["CertificateDescriptionOut"]
            ).optional(),
            "issuerCertificateAuthority": t.string().optional(),
            "revocationDetails": t.proxy(renames["RevocationDetailsOut"]).optional(),
            "name": t.string().optional(),
            "pemCertificateChain": t.array(t.string()).optional(),
            "config": t.proxy(renames["CertificateConfigOut"]).optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "subjectMode": t.string().optional(),
            "pemCertificate": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "pemCsr": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateOut"])
    types["ActivateCertificateAuthorityRequestIn"] = t.struct(
        {
            "requestId": t.string().optional(),
            "pemCaCertificate": t.string(),
            "subordinateConfig": t.proxy(renames["SubordinateConfigIn"]),
        }
    ).named(renames["ActivateCertificateAuthorityRequestIn"])
    types["ActivateCertificateAuthorityRequestOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "pemCaCertificate": t.string(),
            "subordinateConfig": t.proxy(renames["SubordinateConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActivateCertificateAuthorityRequestOut"])
    types["SubordinateConfigChainIn"] = t.struct(
        {"pemCertificates": t.array(t.string())}
    ).named(renames["SubordinateConfigChainIn"])
    types["SubordinateConfigChainOut"] = t.struct(
        {
            "pemCertificates": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubordinateConfigChainOut"])
    types["FetchCaCertsResponseIn"] = t.struct(
        {"caCerts": t.array(t.proxy(renames["CertChainIn"])).optional()}
    ).named(renames["FetchCaCertsResponseIn"])
    types["FetchCaCertsResponseOut"] = t.struct(
        {
            "caCerts": t.array(t.proxy(renames["CertChainOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FetchCaCertsResponseOut"])
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
    types["ListCertificatesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "certificates": t.array(t.proxy(renames["CertificateIn"])).optional(),
        }
    ).named(renames["ListCertificatesResponseIn"])
    types["ListCertificatesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "certificates": t.array(t.proxy(renames["CertificateOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCertificatesResponseOut"])
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
    types["CertificateAuthorityIn"] = t.struct(
        {
            "keySpec": t.proxy(renames["KeyVersionSpecIn"]),
            "gcsBucket": t.string().optional(),
            "type": t.string(),
            "config": t.proxy(renames["CertificateConfigIn"]),
            "subordinateConfig": t.proxy(renames["SubordinateConfigIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "lifetime": t.string(),
        }
    ).named(renames["CertificateAuthorityIn"])
    types["CertificateAuthorityOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "keySpec": t.proxy(renames["KeyVersionSpecOut"]),
            "gcsBucket": t.string().optional(),
            "deleteTime": t.string().optional(),
            "pemCaCertificates": t.array(t.string()).optional(),
            "expireTime": t.string().optional(),
            "type": t.string(),
            "state": t.string().optional(),
            "config": t.proxy(renames["CertificateConfigOut"]),
            "subordinateConfig": t.proxy(renames["SubordinateConfigOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "caCertificateDescriptions": t.array(
                t.proxy(renames["CertificateDescriptionOut"])
            ).optional(),
            "lifetime": t.string(),
            "tier": t.string().optional(),
            "accessUrls": t.proxy(renames["AccessUrlsOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateAuthorityOut"])
    types["SubjectDescriptionIn"] = t.struct(
        {
            "subjectAltName": t.proxy(renames["SubjectAltNamesIn"]).optional(),
            "notAfterTime": t.string().optional(),
            "hexSerialNumber": t.string().optional(),
            "subject": t.proxy(renames["SubjectIn"]).optional(),
            "lifetime": t.string().optional(),
            "notBeforeTime": t.string().optional(),
        }
    ).named(renames["SubjectDescriptionIn"])
    types["SubjectDescriptionOut"] = t.struct(
        {
            "subjectAltName": t.proxy(renames["SubjectAltNamesOut"]).optional(),
            "notAfterTime": t.string().optional(),
            "hexSerialNumber": t.string().optional(),
            "subject": t.proxy(renames["SubjectOut"]).optional(),
            "lifetime": t.string().optional(),
            "notBeforeTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubjectDescriptionOut"])
    types["UndeleteCertificateAuthorityRequestIn"] = t.struct(
        {"requestId": t.string().optional()}
    ).named(renames["UndeleteCertificateAuthorityRequestIn"])
    types["UndeleteCertificateAuthorityRequestOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UndeleteCertificateAuthorityRequestOut"])
    types["ExprIn"] = t.struct(
        {
            "title": t.string().optional(),
            "description": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "title": t.string().optional(),
            "description": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["RevokeCertificateRequestIn"] = t.struct(
        {"reason": t.string(), "requestId": t.string().optional()}
    ).named(renames["RevokeCertificateRequestIn"])
    types["RevokeCertificateRequestOut"] = t.struct(
        {
            "reason": t.string(),
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RevokeCertificateRequestOut"])
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
    types["X509ParametersIn"] = t.struct(
        {
            "additionalExtensions": t.array(
                t.proxy(renames["X509ExtensionIn"])
            ).optional(),
            "policyIds": t.array(t.proxy(renames["ObjectIdIn"])).optional(),
            "keyUsage": t.proxy(renames["KeyUsageIn"]).optional(),
            "caOptions": t.proxy(renames["CaOptionsIn"]).optional(),
            "aiaOcspServers": t.array(t.string()).optional(),
            "nameConstraints": t.proxy(renames["NameConstraintsIn"]).optional(),
        }
    ).named(renames["X509ParametersIn"])
    types["X509ParametersOut"] = t.struct(
        {
            "additionalExtensions": t.array(
                t.proxy(renames["X509ExtensionOut"])
            ).optional(),
            "policyIds": t.array(t.proxy(renames["ObjectIdOut"])).optional(),
            "keyUsage": t.proxy(renames["KeyUsageOut"]).optional(),
            "caOptions": t.proxy(renames["CaOptionsOut"]).optional(),
            "aiaOcspServers": t.array(t.string()).optional(),
            "nameConstraints": t.proxy(renames["NameConstraintsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["X509ParametersOut"])
    types["ListOperationsResponseIn"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["OperationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListOperationsResponseIn"])
    types["ListOperationsResponseOut"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["OperationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListOperationsResponseOut"])
    types["ExtendedKeyUsageOptionsIn"] = t.struct(
        {
            "ocspSigning": t.boolean().optional(),
            "serverAuth": t.boolean().optional(),
            "clientAuth": t.boolean().optional(),
            "emailProtection": t.boolean().optional(),
            "codeSigning": t.boolean().optional(),
            "timeStamping": t.boolean().optional(),
        }
    ).named(renames["ExtendedKeyUsageOptionsIn"])
    types["ExtendedKeyUsageOptionsOut"] = t.struct(
        {
            "ocspSigning": t.boolean().optional(),
            "serverAuth": t.boolean().optional(),
            "clientAuth": t.boolean().optional(),
            "emailProtection": t.boolean().optional(),
            "codeSigning": t.boolean().optional(),
            "timeStamping": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExtendedKeyUsageOptionsOut"])
    types["FetchCertificateAuthorityCsrResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["FetchCertificateAuthorityCsrResponseIn"])
    types["FetchCertificateAuthorityCsrResponseOut"] = t.struct(
        {
            "pemCsr": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FetchCertificateAuthorityCsrResponseOut"])
    types["CertificateConfigIn"] = t.struct(
        {
            "subjectConfig": t.proxy(renames["SubjectConfigIn"]),
            "x509Config": t.proxy(renames["X509ParametersIn"]),
            "publicKey": t.proxy(renames["PublicKeyIn"]).optional(),
        }
    ).named(renames["CertificateConfigIn"])
    types["CertificateConfigOut"] = t.struct(
        {
            "subjectConfig": t.proxy(renames["SubjectConfigOut"]),
            "x509Config": t.proxy(renames["X509ParametersOut"]),
            "publicKey": t.proxy(renames["PublicKeyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateConfigOut"])

    functions = {}
    functions["projectsLocationsList"] = privateca.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = privateca.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsFetchCaCerts"] = privateca.get(
        "v1/{parent}/caPools",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCaPoolsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsSetIamPolicy"] = privateca.get(
        "v1/{parent}/caPools",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCaPoolsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsGet"] = privateca.get(
        "v1/{parent}/caPools",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCaPoolsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsPatch"] = privateca.get(
        "v1/{parent}/caPools",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCaPoolsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsTestIamPermissions"] = privateca.get(
        "v1/{parent}/caPools",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCaPoolsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsGetIamPolicy"] = privateca.get(
        "v1/{parent}/caPools",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCaPoolsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsDelete"] = privateca.get(
        "v1/{parent}/caPools",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCaPoolsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsCreate"] = privateca.get(
        "v1/{parent}/caPools",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCaPoolsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsList"] = privateca.get(
        "v1/{parent}/caPools",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCaPoolsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsCertificateAuthoritiesFetch"] = privateca.post(
        "v1/{name}:disable",
        t.struct(
            {
                "name": t.string(),
                "ignoreDependentResources": t.boolean().optional(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCaPoolsCertificateAuthoritiesUndelete"
    ] = privateca.post(
        "v1/{name}:disable",
        t.struct(
            {
                "name": t.string(),
                "ignoreDependentResources": t.boolean().optional(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsCertificateAuthoritiesEnable"] = privateca.post(
        "v1/{name}:disable",
        t.struct(
            {
                "name": t.string(),
                "ignoreDependentResources": t.boolean().optional(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsCertificateAuthoritiesDelete"] = privateca.post(
        "v1/{name}:disable",
        t.struct(
            {
                "name": t.string(),
                "ignoreDependentResources": t.boolean().optional(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsCertificateAuthoritiesPatch"] = privateca.post(
        "v1/{name}:disable",
        t.struct(
            {
                "name": t.string(),
                "ignoreDependentResources": t.boolean().optional(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCaPoolsCertificateAuthoritiesActivate"
    ] = privateca.post(
        "v1/{name}:disable",
        t.struct(
            {
                "name": t.string(),
                "ignoreDependentResources": t.boolean().optional(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsCertificateAuthoritiesCreate"] = privateca.post(
        "v1/{name}:disable",
        t.struct(
            {
                "name": t.string(),
                "ignoreDependentResources": t.boolean().optional(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsCertificateAuthoritiesList"] = privateca.post(
        "v1/{name}:disable",
        t.struct(
            {
                "name": t.string(),
                "ignoreDependentResources": t.boolean().optional(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsCertificateAuthoritiesGet"] = privateca.post(
        "v1/{name}:disable",
        t.struct(
            {
                "name": t.string(),
                "ignoreDependentResources": t.boolean().optional(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsCertificateAuthoritiesDisable"] = privateca.post(
        "v1/{name}:disable",
        t.struct(
            {
                "name": t.string(),
                "ignoreDependentResources": t.boolean().optional(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCaPoolsCertificateAuthoritiesCertificateRevocationListsSetIamPolicy"
    ] = privateca.get(
        "v1/{parent}/certificateRevocationLists",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCertificateRevocationListsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCaPoolsCertificateAuthoritiesCertificateRevocationListsGet"
    ] = privateca.get(
        "v1/{parent}/certificateRevocationLists",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCertificateRevocationListsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCaPoolsCertificateAuthoritiesCertificateRevocationListsGetIamPolicy"
    ] = privateca.get(
        "v1/{parent}/certificateRevocationLists",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCertificateRevocationListsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCaPoolsCertificateAuthoritiesCertificateRevocationListsTestIamPermissions"
    ] = privateca.get(
        "v1/{parent}/certificateRevocationLists",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCertificateRevocationListsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCaPoolsCertificateAuthoritiesCertificateRevocationListsPatch"
    ] = privateca.get(
        "v1/{parent}/certificateRevocationLists",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCertificateRevocationListsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCaPoolsCertificateAuthoritiesCertificateRevocationListsList"
    ] = privateca.get(
        "v1/{parent}/certificateRevocationLists",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCertificateRevocationListsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsCertificatesList"] = privateca.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "certificateTemplate": t.string().optional(),
                "lifetime": t.string(),
                "config": t.proxy(renames["CertificateConfigIn"]).optional(),
                "subjectMode": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "pemCsr": t.string().optional(),
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
                "updateMask": t.string(),
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "certificateTemplate": t.string().optional(),
                "lifetime": t.string(),
                "config": t.proxy(renames["CertificateConfigIn"]).optional(),
                "subjectMode": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "pemCsr": t.string().optional(),
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
                "updateMask": t.string(),
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "certificateTemplate": t.string().optional(),
                "lifetime": t.string(),
                "config": t.proxy(renames["CertificateConfigIn"]).optional(),
                "subjectMode": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "pemCsr": t.string().optional(),
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
                "updateMask": t.string(),
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "certificateTemplate": t.string().optional(),
                "lifetime": t.string(),
                "config": t.proxy(renames["CertificateConfigIn"]).optional(),
                "subjectMode": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "pemCsr": t.string().optional(),
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
                "updateMask": t.string(),
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "certificateTemplate": t.string().optional(),
                "lifetime": t.string(),
                "config": t.proxy(renames["CertificateConfigIn"]).optional(),
                "subjectMode": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "pemCsr": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CertificateOut"]),
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
    functions["projectsLocationsOperationsGet"] = privateca.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
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
    functions["projectsLocationsOperationsDelete"] = privateca.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCertificateTemplatesPatch"] = privateca.get(
        "v1/{parent}/certificateTemplates",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCertificateTemplatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCertificateTemplatesGet"] = privateca.get(
        "v1/{parent}/certificateTemplates",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCertificateTemplatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCertificateTemplatesSetIamPolicy"] = privateca.get(
        "v1/{parent}/certificateTemplates",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCertificateTemplatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCertificateTemplatesTestIamPermissions"
    ] = privateca.get(
        "v1/{parent}/certificateTemplates",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCertificateTemplatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCertificateTemplatesCreate"] = privateca.get(
        "v1/{parent}/certificateTemplates",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCertificateTemplatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCertificateTemplatesGetIamPolicy"] = privateca.get(
        "v1/{parent}/certificateTemplates",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCertificateTemplatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCertificateTemplatesDelete"] = privateca.get(
        "v1/{parent}/certificateTemplates",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCertificateTemplatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCertificateTemplatesList"] = privateca.get(
        "v1/{parent}/certificateTemplates",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCertificateTemplatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="privateca", renames=renames, types=types, functions=functions
    )
