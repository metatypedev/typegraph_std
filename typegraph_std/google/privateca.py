from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_privateca() -> Import:
    privateca = HTTPRuntime("https://privateca.googleapis.com/")

    renames = {
        "ErrorResponse": "_privateca_1_ErrorResponse",
        "X509ExtensionIn": "_privateca_2_X509ExtensionIn",
        "X509ExtensionOut": "_privateca_3_X509ExtensionOut",
        "CertificateIn": "_privateca_4_CertificateIn",
        "CertificateOut": "_privateca_5_CertificateOut",
        "EnableCertificateAuthorityRequestIn": "_privateca_6_EnableCertificateAuthorityRequestIn",
        "EnableCertificateAuthorityRequestOut": "_privateca_7_EnableCertificateAuthorityRequestOut",
        "PublishingOptionsIn": "_privateca_8_PublishingOptionsIn",
        "PublishingOptionsOut": "_privateca_9_PublishingOptionsOut",
        "ActivateCertificateAuthorityRequestIn": "_privateca_10_ActivateCertificateAuthorityRequestIn",
        "ActivateCertificateAuthorityRequestOut": "_privateca_11_ActivateCertificateAuthorityRequestOut",
        "TestIamPermissionsRequestIn": "_privateca_12_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_privateca_13_TestIamPermissionsRequestOut",
        "NameConstraintsIn": "_privateca_14_NameConstraintsIn",
        "NameConstraintsOut": "_privateca_15_NameConstraintsOut",
        "ExtendedKeyUsageOptionsIn": "_privateca_16_ExtendedKeyUsageOptionsIn",
        "ExtendedKeyUsageOptionsOut": "_privateca_17_ExtendedKeyUsageOptionsOut",
        "ListCertificateRevocationListsResponseIn": "_privateca_18_ListCertificateRevocationListsResponseIn",
        "ListCertificateRevocationListsResponseOut": "_privateca_19_ListCertificateRevocationListsResponseOut",
        "RsaKeyTypeIn": "_privateca_20_RsaKeyTypeIn",
        "RsaKeyTypeOut": "_privateca_21_RsaKeyTypeOut",
        "RevocationDetailsIn": "_privateca_22_RevocationDetailsIn",
        "RevocationDetailsOut": "_privateca_23_RevocationDetailsOut",
        "RevokeCertificateRequestIn": "_privateca_24_RevokeCertificateRequestIn",
        "RevokeCertificateRequestOut": "_privateca_25_RevokeCertificateRequestOut",
        "LocationIn": "_privateca_26_LocationIn",
        "LocationOut": "_privateca_27_LocationOut",
        "ListLocationsResponseIn": "_privateca_28_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_privateca_29_ListLocationsResponseOut",
        "CertificateTemplateIn": "_privateca_30_CertificateTemplateIn",
        "CertificateTemplateOut": "_privateca_31_CertificateTemplateOut",
        "CertificateConfigIn": "_privateca_32_CertificateConfigIn",
        "CertificateConfigOut": "_privateca_33_CertificateConfigOut",
        "DisableCertificateAuthorityRequestIn": "_privateca_34_DisableCertificateAuthorityRequestIn",
        "DisableCertificateAuthorityRequestOut": "_privateca_35_DisableCertificateAuthorityRequestOut",
        "ExprIn": "_privateca_36_ExprIn",
        "ExprOut": "_privateca_37_ExprOut",
        "AuditConfigIn": "_privateca_38_AuditConfigIn",
        "AuditConfigOut": "_privateca_39_AuditConfigOut",
        "SubordinateConfigChainIn": "_privateca_40_SubordinateConfigChainIn",
        "SubordinateConfigChainOut": "_privateca_41_SubordinateConfigChainOut",
        "FetchCaCertsResponseIn": "_privateca_42_FetchCaCertsResponseIn",
        "FetchCaCertsResponseOut": "_privateca_43_FetchCaCertsResponseOut",
        "OperationIn": "_privateca_44_OperationIn",
        "OperationOut": "_privateca_45_OperationOut",
        "CaPoolIn": "_privateca_46_CaPoolIn",
        "CaPoolOut": "_privateca_47_CaPoolOut",
        "SubjectConfigIn": "_privateca_48_SubjectConfigIn",
        "SubjectConfigOut": "_privateca_49_SubjectConfigOut",
        "PolicyIn": "_privateca_50_PolicyIn",
        "PolicyOut": "_privateca_51_PolicyOut",
        "EcKeyTypeIn": "_privateca_52_EcKeyTypeIn",
        "EcKeyTypeOut": "_privateca_53_EcKeyTypeOut",
        "IssuanceModesIn": "_privateca_54_IssuanceModesIn",
        "IssuanceModesOut": "_privateca_55_IssuanceModesOut",
        "ObjectIdIn": "_privateca_56_ObjectIdIn",
        "ObjectIdOut": "_privateca_57_ObjectIdOut",
        "SetIamPolicyRequestIn": "_privateca_58_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_privateca_59_SetIamPolicyRequestOut",
        "CertificateDescriptionIn": "_privateca_60_CertificateDescriptionIn",
        "CertificateDescriptionOut": "_privateca_61_CertificateDescriptionOut",
        "CertificateIdentityConstraintsIn": "_privateca_62_CertificateIdentityConstraintsIn",
        "CertificateIdentityConstraintsOut": "_privateca_63_CertificateIdentityConstraintsOut",
        "CertChainIn": "_privateca_64_CertChainIn",
        "CertChainOut": "_privateca_65_CertChainOut",
        "CertificateAuthorityIn": "_privateca_66_CertificateAuthorityIn",
        "CertificateAuthorityOut": "_privateca_67_CertificateAuthorityOut",
        "CertificateRevocationListIn": "_privateca_68_CertificateRevocationListIn",
        "CertificateRevocationListOut": "_privateca_69_CertificateRevocationListOut",
        "ListCertificateAuthoritiesResponseIn": "_privateca_70_ListCertificateAuthoritiesResponseIn",
        "ListCertificateAuthoritiesResponseOut": "_privateca_71_ListCertificateAuthoritiesResponseOut",
        "KeyIdIn": "_privateca_72_KeyIdIn",
        "KeyIdOut": "_privateca_73_KeyIdOut",
        "KeyUsageOptionsIn": "_privateca_74_KeyUsageOptionsIn",
        "KeyUsageOptionsOut": "_privateca_75_KeyUsageOptionsOut",
        "StatusIn": "_privateca_76_StatusIn",
        "StatusOut": "_privateca_77_StatusOut",
        "CertificateExtensionConstraintsIn": "_privateca_78_CertificateExtensionConstraintsIn",
        "CertificateExtensionConstraintsOut": "_privateca_79_CertificateExtensionConstraintsOut",
        "SubordinateConfigIn": "_privateca_80_SubordinateConfigIn",
        "SubordinateConfigOut": "_privateca_81_SubordinateConfigOut",
        "ListCertificateTemplatesResponseIn": "_privateca_82_ListCertificateTemplatesResponseIn",
        "ListCertificateTemplatesResponseOut": "_privateca_83_ListCertificateTemplatesResponseOut",
        "OperationMetadataIn": "_privateca_84_OperationMetadataIn",
        "OperationMetadataOut": "_privateca_85_OperationMetadataOut",
        "AccessUrlsIn": "_privateca_86_AccessUrlsIn",
        "AccessUrlsOut": "_privateca_87_AccessUrlsOut",
        "TestIamPermissionsResponseIn": "_privateca_88_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_privateca_89_TestIamPermissionsResponseOut",
        "X509ParametersIn": "_privateca_90_X509ParametersIn",
        "X509ParametersOut": "_privateca_91_X509ParametersOut",
        "EmptyIn": "_privateca_92_EmptyIn",
        "EmptyOut": "_privateca_93_EmptyOut",
        "SubjectIn": "_privateca_94_SubjectIn",
        "SubjectOut": "_privateca_95_SubjectOut",
        "RevokedCertificateIn": "_privateca_96_RevokedCertificateIn",
        "RevokedCertificateOut": "_privateca_97_RevokedCertificateOut",
        "FetchCertificateAuthorityCsrResponseIn": "_privateca_98_FetchCertificateAuthorityCsrResponseIn",
        "FetchCertificateAuthorityCsrResponseOut": "_privateca_99_FetchCertificateAuthorityCsrResponseOut",
        "SubjectDescriptionIn": "_privateca_100_SubjectDescriptionIn",
        "SubjectDescriptionOut": "_privateca_101_SubjectDescriptionOut",
        "UndeleteCertificateAuthorityRequestIn": "_privateca_102_UndeleteCertificateAuthorityRequestIn",
        "UndeleteCertificateAuthorityRequestOut": "_privateca_103_UndeleteCertificateAuthorityRequestOut",
        "KeyVersionSpecIn": "_privateca_104_KeyVersionSpecIn",
        "KeyVersionSpecOut": "_privateca_105_KeyVersionSpecOut",
        "ListCertificatesResponseIn": "_privateca_106_ListCertificatesResponseIn",
        "ListCertificatesResponseOut": "_privateca_107_ListCertificatesResponseOut",
        "CancelOperationRequestIn": "_privateca_108_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_privateca_109_CancelOperationRequestOut",
        "CaOptionsIn": "_privateca_110_CaOptionsIn",
        "CaOptionsOut": "_privateca_111_CaOptionsOut",
        "FetchCaCertsRequestIn": "_privateca_112_FetchCaCertsRequestIn",
        "FetchCaCertsRequestOut": "_privateca_113_FetchCaCertsRequestOut",
        "CertificateFingerprintIn": "_privateca_114_CertificateFingerprintIn",
        "CertificateFingerprintOut": "_privateca_115_CertificateFingerprintOut",
        "ListCaPoolsResponseIn": "_privateca_116_ListCaPoolsResponseIn",
        "ListCaPoolsResponseOut": "_privateca_117_ListCaPoolsResponseOut",
        "AllowedKeyTypeIn": "_privateca_118_AllowedKeyTypeIn",
        "AllowedKeyTypeOut": "_privateca_119_AllowedKeyTypeOut",
        "BindingIn": "_privateca_120_BindingIn",
        "BindingOut": "_privateca_121_BindingOut",
        "SubjectAltNamesIn": "_privateca_122_SubjectAltNamesIn",
        "SubjectAltNamesOut": "_privateca_123_SubjectAltNamesOut",
        "ReconciliationOperationMetadataIn": "_privateca_124_ReconciliationOperationMetadataIn",
        "ReconciliationOperationMetadataOut": "_privateca_125_ReconciliationOperationMetadataOut",
        "PublicKeyIn": "_privateca_126_PublicKeyIn",
        "PublicKeyOut": "_privateca_127_PublicKeyOut",
        "KeyUsageIn": "_privateca_128_KeyUsageIn",
        "KeyUsageOut": "_privateca_129_KeyUsageOut",
        "IssuancePolicyIn": "_privateca_130_IssuancePolicyIn",
        "IssuancePolicyOut": "_privateca_131_IssuancePolicyOut",
        "ListOperationsResponseIn": "_privateca_132_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_privateca_133_ListOperationsResponseOut",
        "AuditLogConfigIn": "_privateca_134_AuditLogConfigIn",
        "AuditLogConfigOut": "_privateca_135_AuditLogConfigOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["X509ExtensionIn"] = t.struct(
        {
            "critical": t.boolean().optional(),
            "value": t.string(),
            "objectId": t.proxy(renames["ObjectIdIn"]),
        }
    ).named(renames["X509ExtensionIn"])
    types["X509ExtensionOut"] = t.struct(
        {
            "critical": t.boolean().optional(),
            "value": t.string(),
            "objectId": t.proxy(renames["ObjectIdOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["X509ExtensionOut"])
    types["CertificateIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "lifetime": t.string(),
            "pemCsr": t.string().optional(),
            "certificateTemplate": t.string().optional(),
            "config": t.proxy(renames["CertificateConfigIn"]).optional(),
            "subjectMode": t.string().optional(),
        }
    ).named(renames["CertificateIn"])
    types["CertificateOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "lifetime": t.string(),
            "createTime": t.string().optional(),
            "issuerCertificateAuthority": t.string().optional(),
            "pemCsr": t.string().optional(),
            "certificateTemplate": t.string().optional(),
            "certificateDescription": t.proxy(
                renames["CertificateDescriptionOut"]
            ).optional(),
            "config": t.proxy(renames["CertificateConfigOut"]).optional(),
            "updateTime": t.string().optional(),
            "pemCertificate": t.string().optional(),
            "name": t.string().optional(),
            "subjectMode": t.string().optional(),
            "revocationDetails": t.proxy(renames["RevocationDetailsOut"]).optional(),
            "pemCertificateChain": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateOut"])
    types["EnableCertificateAuthorityRequestIn"] = t.struct(
        {"requestId": t.string().optional()}
    ).named(renames["EnableCertificateAuthorityRequestIn"])
    types["EnableCertificateAuthorityRequestOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnableCertificateAuthorityRequestOut"])
    types["PublishingOptionsIn"] = t.struct(
        {
            "publishCaCert": t.boolean().optional(),
            "encodingFormat": t.string().optional(),
            "publishCrl": t.boolean().optional(),
        }
    ).named(renames["PublishingOptionsIn"])
    types["PublishingOptionsOut"] = t.struct(
        {
            "publishCaCert": t.boolean().optional(),
            "encodingFormat": t.string().optional(),
            "publishCrl": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublishingOptionsOut"])
    types["ActivateCertificateAuthorityRequestIn"] = t.struct(
        {
            "pemCaCertificate": t.string(),
            "requestId": t.string().optional(),
            "subordinateConfig": t.proxy(renames["SubordinateConfigIn"]),
        }
    ).named(renames["ActivateCertificateAuthorityRequestIn"])
    types["ActivateCertificateAuthorityRequestOut"] = t.struct(
        {
            "pemCaCertificate": t.string(),
            "requestId": t.string().optional(),
            "subordinateConfig": t.proxy(renames["SubordinateConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActivateCertificateAuthorityRequestOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["NameConstraintsIn"] = t.struct(
        {
            "excludedUris": t.array(t.string()).optional(),
            "permittedUris": t.array(t.string()).optional(),
            "excludedEmailAddresses": t.array(t.string()).optional(),
            "permittedEmailAddresses": t.array(t.string()).optional(),
            "permittedDnsNames": t.array(t.string()).optional(),
            "excludedDnsNames": t.array(t.string()).optional(),
            "critical": t.boolean().optional(),
            "permittedIpRanges": t.array(t.string()).optional(),
            "excludedIpRanges": t.array(t.string()).optional(),
        }
    ).named(renames["NameConstraintsIn"])
    types["NameConstraintsOut"] = t.struct(
        {
            "excludedUris": t.array(t.string()).optional(),
            "permittedUris": t.array(t.string()).optional(),
            "excludedEmailAddresses": t.array(t.string()).optional(),
            "permittedEmailAddresses": t.array(t.string()).optional(),
            "permittedDnsNames": t.array(t.string()).optional(),
            "excludedDnsNames": t.array(t.string()).optional(),
            "critical": t.boolean().optional(),
            "permittedIpRanges": t.array(t.string()).optional(),
            "excludedIpRanges": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NameConstraintsOut"])
    types["ExtendedKeyUsageOptionsIn"] = t.struct(
        {
            "serverAuth": t.boolean().optional(),
            "timeStamping": t.boolean().optional(),
            "ocspSigning": t.boolean().optional(),
            "emailProtection": t.boolean().optional(),
            "codeSigning": t.boolean().optional(),
            "clientAuth": t.boolean().optional(),
        }
    ).named(renames["ExtendedKeyUsageOptionsIn"])
    types["ExtendedKeyUsageOptionsOut"] = t.struct(
        {
            "serverAuth": t.boolean().optional(),
            "timeStamping": t.boolean().optional(),
            "ocspSigning": t.boolean().optional(),
            "emailProtection": t.boolean().optional(),
            "codeSigning": t.boolean().optional(),
            "clientAuth": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExtendedKeyUsageOptionsOut"])
    types["ListCertificateRevocationListsResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "certificateRevocationLists": t.array(
                t.proxy(renames["CertificateRevocationListIn"])
            ).optional(),
        }
    ).named(renames["ListCertificateRevocationListsResponseIn"])
    types["ListCertificateRevocationListsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "certificateRevocationLists": t.array(
                t.proxy(renames["CertificateRevocationListOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCertificateRevocationListsResponseOut"])
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
    types["CertificateTemplateIn"] = t.struct(
        {
            "predefinedValues": t.proxy(renames["X509ParametersIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "identityConstraints": t.proxy(
                renames["CertificateIdentityConstraintsIn"]
            ).optional(),
            "passthroughExtensions": t.proxy(
                renames["CertificateExtensionConstraintsIn"]
            ).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["CertificateTemplateIn"])
    types["CertificateTemplateOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "predefinedValues": t.proxy(renames["X509ParametersOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "identityConstraints": t.proxy(
                renames["CertificateIdentityConstraintsOut"]
            ).optional(),
            "name": t.string().optional(),
            "passthroughExtensions": t.proxy(
                renames["CertificateExtensionConstraintsOut"]
            ).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateTemplateOut"])
    types["CertificateConfigIn"] = t.struct(
        {
            "publicKey": t.proxy(renames["PublicKeyIn"]).optional(),
            "x509Config": t.proxy(renames["X509ParametersIn"]),
            "subjectConfig": t.proxy(renames["SubjectConfigIn"]),
        }
    ).named(renames["CertificateConfigIn"])
    types["CertificateConfigOut"] = t.struct(
        {
            "publicKey": t.proxy(renames["PublicKeyOut"]).optional(),
            "x509Config": t.proxy(renames["X509ParametersOut"]),
            "subjectConfig": t.proxy(renames["SubjectConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateConfigOut"])
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
    types["OperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
    types["CaPoolIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "publishingOptions": t.proxy(renames["PublishingOptionsIn"]).optional(),
            "issuancePolicy": t.proxy(renames["IssuancePolicyIn"]).optional(),
            "tier": t.string(),
        }
    ).named(renames["CaPoolIn"])
    types["CaPoolOut"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "publishingOptions": t.proxy(renames["PublishingOptionsOut"]).optional(),
            "issuancePolicy": t.proxy(renames["IssuancePolicyOut"]).optional(),
            "tier": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CaPoolOut"])
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
    types["PolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["EcKeyTypeIn"] = t.struct(
        {"signatureAlgorithm": t.string().optional()}
    ).named(renames["EcKeyTypeIn"])
    types["EcKeyTypeOut"] = t.struct(
        {
            "signatureAlgorithm": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EcKeyTypeOut"])
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
    types["ObjectIdIn"] = t.struct({"objectIdPath": t.array(t.integer())}).named(
        renames["ObjectIdIn"]
    )
    types["ObjectIdOut"] = t.struct(
        {
            "objectIdPath": t.array(t.integer()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ObjectIdOut"])
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
    types["CertificateDescriptionIn"] = t.struct(
        {
            "authorityKeyId": t.proxy(renames["KeyIdIn"]).optional(),
            "crlDistributionPoints": t.array(t.string()).optional(),
            "subjectKeyId": t.proxy(renames["KeyIdIn"]).optional(),
            "certFingerprint": t.proxy(renames["CertificateFingerprintIn"]).optional(),
            "publicKey": t.proxy(renames["PublicKeyIn"]).optional(),
            "subjectDescription": t.proxy(renames["SubjectDescriptionIn"]).optional(),
            "x509Description": t.proxy(renames["X509ParametersIn"]).optional(),
            "aiaIssuingCertificateUrls": t.array(t.string()).optional(),
        }
    ).named(renames["CertificateDescriptionIn"])
    types["CertificateDescriptionOut"] = t.struct(
        {
            "authorityKeyId": t.proxy(renames["KeyIdOut"]).optional(),
            "crlDistributionPoints": t.array(t.string()).optional(),
            "subjectKeyId": t.proxy(renames["KeyIdOut"]).optional(),
            "certFingerprint": t.proxy(renames["CertificateFingerprintOut"]).optional(),
            "publicKey": t.proxy(renames["PublicKeyOut"]).optional(),
            "subjectDescription": t.proxy(renames["SubjectDescriptionOut"]).optional(),
            "x509Description": t.proxy(renames["X509ParametersOut"]).optional(),
            "aiaIssuingCertificateUrls": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateDescriptionOut"])
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
    types["CertChainIn"] = t.struct(
        {"certificates": t.array(t.string()).optional()}
    ).named(renames["CertChainIn"])
    types["CertChainOut"] = t.struct(
        {
            "certificates": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertChainOut"])
    types["CertificateAuthorityIn"] = t.struct(
        {
            "config": t.proxy(renames["CertificateConfigIn"]),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "subordinateConfig": t.proxy(renames["SubordinateConfigIn"]).optional(),
            "type": t.string(),
            "gcsBucket": t.string().optional(),
            "lifetime": t.string(),
            "keySpec": t.proxy(renames["KeyVersionSpecIn"]),
        }
    ).named(renames["CertificateAuthorityIn"])
    types["CertificateAuthorityOut"] = t.struct(
        {
            "expireTime": t.string().optional(),
            "config": t.proxy(renames["CertificateConfigOut"]),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "tier": t.string().optional(),
            "subordinateConfig": t.proxy(renames["SubordinateConfigOut"]).optional(),
            "type": t.string(),
            "caCertificateDescriptions": t.array(
                t.proxy(renames["CertificateDescriptionOut"])
            ).optional(),
            "pemCaCertificates": t.array(t.string()).optional(),
            "state": t.string().optional(),
            "gcsBucket": t.string().optional(),
            "deleteTime": t.string().optional(),
            "lifetime": t.string(),
            "updateTime": t.string().optional(),
            "keySpec": t.proxy(renames["KeyVersionSpecOut"]),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "accessUrls": t.proxy(renames["AccessUrlsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateAuthorityOut"])
    types["CertificateRevocationListIn"] = t.struct(
        {"labels": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["CertificateRevocationListIn"])
    types["CertificateRevocationListOut"] = t.struct(
        {
            "accessUrl": t.string().optional(),
            "sequenceNumber": t.string().optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "pemCrl": t.string().optional(),
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "revisionId": t.string().optional(),
            "revokedCertificates": t.array(
                t.proxy(renames["RevokedCertificateOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateRevocationListOut"])
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
    types["KeyIdIn"] = t.struct({"keyId": t.string().optional()}).named(
        renames["KeyIdIn"]
    )
    types["KeyIdOut"] = t.struct(
        {
            "keyId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyIdOut"])
    types["KeyUsageOptionsIn"] = t.struct(
        {
            "contentCommitment": t.boolean().optional(),
            "keyAgreement": t.boolean().optional(),
            "dataEncipherment": t.boolean().optional(),
            "decipherOnly": t.boolean().optional(),
            "certSign": t.boolean().optional(),
            "digitalSignature": t.boolean().optional(),
            "crlSign": t.boolean().optional(),
            "encipherOnly": t.boolean().optional(),
            "keyEncipherment": t.boolean().optional(),
        }
    ).named(renames["KeyUsageOptionsIn"])
    types["KeyUsageOptionsOut"] = t.struct(
        {
            "contentCommitment": t.boolean().optional(),
            "keyAgreement": t.boolean().optional(),
            "dataEncipherment": t.boolean().optional(),
            "decipherOnly": t.boolean().optional(),
            "certSign": t.boolean().optional(),
            "digitalSignature": t.boolean().optional(),
            "crlSign": t.boolean().optional(),
            "encipherOnly": t.boolean().optional(),
            "keyEncipherment": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyUsageOptionsOut"])
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
    types["SubordinateConfigIn"] = t.struct(
        {
            "certificateAuthority": t.string(),
            "pemIssuerChain": t.proxy(renames["SubordinateConfigChainIn"]),
        }
    ).named(renames["SubordinateConfigIn"])
    types["SubordinateConfigOut"] = t.struct(
        {
            "certificateAuthority": t.string(),
            "pemIssuerChain": t.proxy(renames["SubordinateConfigChainOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubordinateConfigOut"])
    types["ListCertificateTemplatesResponseIn"] = t.struct(
        {
            "certificateTemplates": t.array(
                t.proxy(renames["CertificateTemplateIn"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListCertificateTemplatesResponseIn"])
    types["ListCertificateTemplatesResponseOut"] = t.struct(
        {
            "certificateTemplates": t.array(
                t.proxy(renames["CertificateTemplateOut"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCertificateTemplatesResponseOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "apiVersion": t.string().optional(),
            "createTime": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "endTime": t.string().optional(),
            "target": t.string().optional(),
            "verb": t.string().optional(),
            "statusMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
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
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["X509ParametersIn"] = t.struct(
        {
            "policyIds": t.array(t.proxy(renames["ObjectIdIn"])).optional(),
            "caOptions": t.proxy(renames["CaOptionsIn"]).optional(),
            "nameConstraints": t.proxy(renames["NameConstraintsIn"]).optional(),
            "aiaOcspServers": t.array(t.string()).optional(),
            "keyUsage": t.proxy(renames["KeyUsageIn"]).optional(),
            "additionalExtensions": t.array(
                t.proxy(renames["X509ExtensionIn"])
            ).optional(),
        }
    ).named(renames["X509ParametersIn"])
    types["X509ParametersOut"] = t.struct(
        {
            "policyIds": t.array(t.proxy(renames["ObjectIdOut"])).optional(),
            "caOptions": t.proxy(renames["CaOptionsOut"]).optional(),
            "nameConstraints": t.proxy(renames["NameConstraintsOut"]).optional(),
            "aiaOcspServers": t.array(t.string()).optional(),
            "keyUsage": t.proxy(renames["KeyUsageOut"]).optional(),
            "additionalExtensions": t.array(
                t.proxy(renames["X509ExtensionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["X509ParametersOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["SubjectIn"] = t.struct(
        {
            "organization": t.string().optional(),
            "streetAddress": t.string().optional(),
            "locality": t.string().optional(),
            "commonName": t.string().optional(),
            "countryCode": t.string().optional(),
            "province": t.string().optional(),
            "organizationalUnit": t.string().optional(),
            "postalCode": t.string().optional(),
        }
    ).named(renames["SubjectIn"])
    types["SubjectOut"] = t.struct(
        {
            "organization": t.string().optional(),
            "streetAddress": t.string().optional(),
            "locality": t.string().optional(),
            "commonName": t.string().optional(),
            "countryCode": t.string().optional(),
            "province": t.string().optional(),
            "organizationalUnit": t.string().optional(),
            "postalCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubjectOut"])
    types["RevokedCertificateIn"] = t.struct(
        {
            "hexSerialNumber": t.string().optional(),
            "certificate": t.string().optional(),
            "revocationReason": t.string().optional(),
        }
    ).named(renames["RevokedCertificateIn"])
    types["RevokedCertificateOut"] = t.struct(
        {
            "hexSerialNumber": t.string().optional(),
            "certificate": t.string().optional(),
            "revocationReason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RevokedCertificateOut"])
    types["FetchCertificateAuthorityCsrResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["FetchCertificateAuthorityCsrResponseIn"])
    types["FetchCertificateAuthorityCsrResponseOut"] = t.struct(
        {
            "pemCsr": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FetchCertificateAuthorityCsrResponseOut"])
    types["SubjectDescriptionIn"] = t.struct(
        {
            "notAfterTime": t.string().optional(),
            "subjectAltName": t.proxy(renames["SubjectAltNamesIn"]).optional(),
            "notBeforeTime": t.string().optional(),
            "subject": t.proxy(renames["SubjectIn"]).optional(),
            "hexSerialNumber": t.string().optional(),
            "lifetime": t.string().optional(),
        }
    ).named(renames["SubjectDescriptionIn"])
    types["SubjectDescriptionOut"] = t.struct(
        {
            "notAfterTime": t.string().optional(),
            "subjectAltName": t.proxy(renames["SubjectAltNamesOut"]).optional(),
            "notBeforeTime": t.string().optional(),
            "subject": t.proxy(renames["SubjectOut"]).optional(),
            "hexSerialNumber": t.string().optional(),
            "lifetime": t.string().optional(),
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
    types["KeyVersionSpecIn"] = t.struct(
        {
            "cloudKmsKeyVersion": t.string().optional(),
            "algorithm": t.string().optional(),
        }
    ).named(renames["KeyVersionSpecIn"])
    types["KeyVersionSpecOut"] = t.struct(
        {
            "cloudKmsKeyVersion": t.string().optional(),
            "algorithm": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyVersionSpecOut"])
    types["ListCertificatesResponseIn"] = t.struct(
        {
            "certificates": t.array(t.proxy(renames["CertificateIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListCertificatesResponseIn"])
    types["ListCertificatesResponseOut"] = t.struct(
        {
            "certificates": t.array(t.proxy(renames["CertificateOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCertificatesResponseOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
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
    types["FetchCaCertsRequestIn"] = t.struct(
        {"requestId": t.string().optional()}
    ).named(renames["FetchCaCertsRequestIn"])
    types["FetchCaCertsRequestOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FetchCaCertsRequestOut"])
    types["CertificateFingerprintIn"] = t.struct(
        {"sha256Hash": t.string().optional()}
    ).named(renames["CertificateFingerprintIn"])
    types["CertificateFingerprintOut"] = t.struct(
        {
            "sha256Hash": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateFingerprintOut"])
    types["ListCaPoolsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "caPools": t.array(t.proxy(renames["CaPoolIn"])).optional(),
        }
    ).named(renames["ListCaPoolsResponseIn"])
    types["ListCaPoolsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "caPools": t.array(t.proxy(renames["CaPoolOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCaPoolsResponseOut"])
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
    types["BindingIn"] = t.struct(
        {
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["SubjectAltNamesIn"] = t.struct(
        {
            "customSans": t.array(t.proxy(renames["X509ExtensionIn"])).optional(),
            "uris": t.array(t.string()).optional(),
            "emailAddresses": t.array(t.string()).optional(),
            "dnsNames": t.array(t.string()).optional(),
            "ipAddresses": t.array(t.string()).optional(),
        }
    ).named(renames["SubjectAltNamesIn"])
    types["SubjectAltNamesOut"] = t.struct(
        {
            "customSans": t.array(t.proxy(renames["X509ExtensionOut"])).optional(),
            "uris": t.array(t.string()).optional(),
            "emailAddresses": t.array(t.string()).optional(),
            "dnsNames": t.array(t.string()).optional(),
            "ipAddresses": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubjectAltNamesOut"])
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
    types["IssuancePolicyIn"] = t.struct(
        {
            "allowedKeyTypes": t.array(t.proxy(renames["AllowedKeyTypeIn"])).optional(),
            "allowedIssuanceModes": t.proxy(renames["IssuanceModesIn"]).optional(),
            "maximumLifetime": t.string().optional(),
            "baselineValues": t.proxy(renames["X509ParametersIn"]).optional(),
            "identityConstraints": t.proxy(
                renames["CertificateIdentityConstraintsIn"]
            ).optional(),
            "passthroughExtensions": t.proxy(
                renames["CertificateExtensionConstraintsIn"]
            ).optional(),
        }
    ).named(renames["IssuancePolicyIn"])
    types["IssuancePolicyOut"] = t.struct(
        {
            "allowedKeyTypes": t.array(
                t.proxy(renames["AllowedKeyTypeOut"])
            ).optional(),
            "allowedIssuanceModes": t.proxy(renames["IssuanceModesOut"]).optional(),
            "maximumLifetime": t.string().optional(),
            "baselineValues": t.proxy(renames["X509ParametersOut"]).optional(),
            "identityConstraints": t.proxy(
                renames["CertificateIdentityConstraintsOut"]
            ).optional(),
            "passthroughExtensions": t.proxy(
                renames["CertificateExtensionConstraintsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IssuancePolicyOut"])
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
    functions["projectsLocationsCertificateTemplatesPatch"] = privateca.post(
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
    functions["projectsLocationsCertificateTemplatesSetIamPolicy"] = privateca.post(
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
    functions["projectsLocationsCertificateTemplatesGet"] = privateca.post(
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
    functions["projectsLocationsCertificateTemplatesList"] = privateca.post(
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
    functions["projectsLocationsCertificateTemplatesCreate"] = privateca.post(
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
    functions["projectsLocationsCertificateTemplatesGetIamPolicy"] = privateca.post(
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
    functions["projectsLocationsCertificateTemplatesDelete"] = privateca.post(
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
        "projectsLocationsCertificateTemplatesTestIamPermissions"
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
    functions["projectsLocationsCaPoolsCreate"] = privateca.post(
        "v1/{caPool}:fetchCaCerts",
        t.struct(
            {
                "caPool": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FetchCaCertsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsPatch"] = privateca.post(
        "v1/{caPool}:fetchCaCerts",
        t.struct(
            {
                "caPool": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FetchCaCertsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsSetIamPolicy"] = privateca.post(
        "v1/{caPool}:fetchCaCerts",
        t.struct(
            {
                "caPool": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FetchCaCertsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsGet"] = privateca.post(
        "v1/{caPool}:fetchCaCerts",
        t.struct(
            {
                "caPool": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FetchCaCertsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsList"] = privateca.post(
        "v1/{caPool}:fetchCaCerts",
        t.struct(
            {
                "caPool": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FetchCaCertsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsGetIamPolicy"] = privateca.post(
        "v1/{caPool}:fetchCaCerts",
        t.struct(
            {
                "caPool": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FetchCaCertsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsDelete"] = privateca.post(
        "v1/{caPool}:fetchCaCerts",
        t.struct(
            {
                "caPool": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FetchCaCertsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsTestIamPermissions"] = privateca.post(
        "v1/{caPool}:fetchCaCerts",
        t.struct(
            {
                "caPool": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FetchCaCertsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsFetchCaCerts"] = privateca.post(
        "v1/{caPool}:fetchCaCerts",
        t.struct(
            {
                "caPool": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FetchCaCertsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsCertificatesList"] = privateca.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CertificateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsCertificatesPatch"] = privateca.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CertificateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsCertificatesRevoke"] = privateca.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CertificateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsCertificatesCreate"] = privateca.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CertificateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsCertificatesGet"] = privateca.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CertificateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsCertificateAuthoritiesDisable"] = privateca.post(
        "v1/{parent}/certificateAuthorities",
        t.struct(
            {
                "certificateAuthorityId": t.string(),
                "parent": t.string(),
                "requestId": t.string().optional(),
                "config": t.proxy(renames["CertificateConfigIn"]),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "subordinateConfig": t.proxy(renames["SubordinateConfigIn"]).optional(),
                "type": t.string(),
                "gcsBucket": t.string().optional(),
                "lifetime": t.string(),
                "keySpec": t.proxy(renames["KeyVersionSpecIn"]),
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
        "v1/{parent}/certificateAuthorities",
        t.struct(
            {
                "certificateAuthorityId": t.string(),
                "parent": t.string(),
                "requestId": t.string().optional(),
                "config": t.proxy(renames["CertificateConfigIn"]),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "subordinateConfig": t.proxy(renames["SubordinateConfigIn"]).optional(),
                "type": t.string(),
                "gcsBucket": t.string().optional(),
                "lifetime": t.string(),
                "keySpec": t.proxy(renames["KeyVersionSpecIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsCertificateAuthoritiesList"] = privateca.post(
        "v1/{parent}/certificateAuthorities",
        t.struct(
            {
                "certificateAuthorityId": t.string(),
                "parent": t.string(),
                "requestId": t.string().optional(),
                "config": t.proxy(renames["CertificateConfigIn"]),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "subordinateConfig": t.proxy(renames["SubordinateConfigIn"]).optional(),
                "type": t.string(),
                "gcsBucket": t.string().optional(),
                "lifetime": t.string(),
                "keySpec": t.proxy(renames["KeyVersionSpecIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsCertificateAuthoritiesFetch"] = privateca.post(
        "v1/{parent}/certificateAuthorities",
        t.struct(
            {
                "certificateAuthorityId": t.string(),
                "parent": t.string(),
                "requestId": t.string().optional(),
                "config": t.proxy(renames["CertificateConfigIn"]),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "subordinateConfig": t.proxy(renames["SubordinateConfigIn"]).optional(),
                "type": t.string(),
                "gcsBucket": t.string().optional(),
                "lifetime": t.string(),
                "keySpec": t.proxy(renames["KeyVersionSpecIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsCertificateAuthoritiesEnable"] = privateca.post(
        "v1/{parent}/certificateAuthorities",
        t.struct(
            {
                "certificateAuthorityId": t.string(),
                "parent": t.string(),
                "requestId": t.string().optional(),
                "config": t.proxy(renames["CertificateConfigIn"]),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "subordinateConfig": t.proxy(renames["SubordinateConfigIn"]).optional(),
                "type": t.string(),
                "gcsBucket": t.string().optional(),
                "lifetime": t.string(),
                "keySpec": t.proxy(renames["KeyVersionSpecIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsCertificateAuthoritiesPatch"] = privateca.post(
        "v1/{parent}/certificateAuthorities",
        t.struct(
            {
                "certificateAuthorityId": t.string(),
                "parent": t.string(),
                "requestId": t.string().optional(),
                "config": t.proxy(renames["CertificateConfigIn"]),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "subordinateConfig": t.proxy(renames["SubordinateConfigIn"]).optional(),
                "type": t.string(),
                "gcsBucket": t.string().optional(),
                "lifetime": t.string(),
                "keySpec": t.proxy(renames["KeyVersionSpecIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsCertificateAuthoritiesDelete"] = privateca.post(
        "v1/{parent}/certificateAuthorities",
        t.struct(
            {
                "certificateAuthorityId": t.string(),
                "parent": t.string(),
                "requestId": t.string().optional(),
                "config": t.proxy(renames["CertificateConfigIn"]),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "subordinateConfig": t.proxy(renames["SubordinateConfigIn"]).optional(),
                "type": t.string(),
                "gcsBucket": t.string().optional(),
                "lifetime": t.string(),
                "keySpec": t.proxy(renames["KeyVersionSpecIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsCertificateAuthoritiesGet"] = privateca.post(
        "v1/{parent}/certificateAuthorities",
        t.struct(
            {
                "certificateAuthorityId": t.string(),
                "parent": t.string(),
                "requestId": t.string().optional(),
                "config": t.proxy(renames["CertificateConfigIn"]),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "subordinateConfig": t.proxy(renames["SubordinateConfigIn"]).optional(),
                "type": t.string(),
                "gcsBucket": t.string().optional(),
                "lifetime": t.string(),
                "keySpec": t.proxy(renames["KeyVersionSpecIn"]),
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
        "v1/{parent}/certificateAuthorities",
        t.struct(
            {
                "certificateAuthorityId": t.string(),
                "parent": t.string(),
                "requestId": t.string().optional(),
                "config": t.proxy(renames["CertificateConfigIn"]),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "subordinateConfig": t.proxy(renames["SubordinateConfigIn"]).optional(),
                "type": t.string(),
                "gcsBucket": t.string().optional(),
                "lifetime": t.string(),
                "keySpec": t.proxy(renames["KeyVersionSpecIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsCertificateAuthoritiesCreate"] = privateca.post(
        "v1/{parent}/certificateAuthorities",
        t.struct(
            {
                "certificateAuthorityId": t.string(),
                "parent": t.string(),
                "requestId": t.string().optional(),
                "config": t.proxy(renames["CertificateConfigIn"]),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "subordinateConfig": t.proxy(renames["SubordinateConfigIn"]).optional(),
                "type": t.string(),
                "gcsBucket": t.string().optional(),
                "lifetime": t.string(),
                "keySpec": t.proxy(renames["KeyVersionSpecIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
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

    return Import(
        importer="privateca",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
