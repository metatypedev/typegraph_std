from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_privateca():
    privateca = HTTPRuntime("https://privateca.googleapis.com/")

    renames = {
        "ErrorResponse": "_privateca_1_ErrorResponse",
        "SetIamPolicyRequestIn": "_privateca_2_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_privateca_3_SetIamPolicyRequestOut",
        "ListCertificateRevocationListsResponseIn": "_privateca_4_ListCertificateRevocationListsResponseIn",
        "ListCertificateRevocationListsResponseOut": "_privateca_5_ListCertificateRevocationListsResponseOut",
        "SubjectConfigIn": "_privateca_6_SubjectConfigIn",
        "SubjectConfigOut": "_privateca_7_SubjectConfigOut",
        "X509ExtensionIn": "_privateca_8_X509ExtensionIn",
        "X509ExtensionOut": "_privateca_9_X509ExtensionOut",
        "RevokeCertificateRequestIn": "_privateca_10_RevokeCertificateRequestIn",
        "RevokeCertificateRequestOut": "_privateca_11_RevokeCertificateRequestOut",
        "AuditLogConfigIn": "_privateca_12_AuditLogConfigIn",
        "AuditLogConfigOut": "_privateca_13_AuditLogConfigOut",
        "OperationIn": "_privateca_14_OperationIn",
        "OperationOut": "_privateca_15_OperationOut",
        "EnableCertificateAuthorityRequestIn": "_privateca_16_EnableCertificateAuthorityRequestIn",
        "EnableCertificateAuthorityRequestOut": "_privateca_17_EnableCertificateAuthorityRequestOut",
        "SubjectAltNamesIn": "_privateca_18_SubjectAltNamesIn",
        "SubjectAltNamesOut": "_privateca_19_SubjectAltNamesOut",
        "OperationMetadataIn": "_privateca_20_OperationMetadataIn",
        "OperationMetadataOut": "_privateca_21_OperationMetadataOut",
        "SubordinateConfigChainIn": "_privateca_22_SubordinateConfigChainIn",
        "SubordinateConfigChainOut": "_privateca_23_SubordinateConfigChainOut",
        "RevokedCertificateIn": "_privateca_24_RevokedCertificateIn",
        "RevokedCertificateOut": "_privateca_25_RevokedCertificateOut",
        "SubjectDescriptionIn": "_privateca_26_SubjectDescriptionIn",
        "SubjectDescriptionOut": "_privateca_27_SubjectDescriptionOut",
        "X509ParametersIn": "_privateca_28_X509ParametersIn",
        "X509ParametersOut": "_privateca_29_X509ParametersOut",
        "FetchCaCertsRequestIn": "_privateca_30_FetchCaCertsRequestIn",
        "FetchCaCertsRequestOut": "_privateca_31_FetchCaCertsRequestOut",
        "AccessUrlsIn": "_privateca_32_AccessUrlsIn",
        "AccessUrlsOut": "_privateca_33_AccessUrlsOut",
        "ExtendedKeyUsageOptionsIn": "_privateca_34_ExtendedKeyUsageOptionsIn",
        "ExtendedKeyUsageOptionsOut": "_privateca_35_ExtendedKeyUsageOptionsOut",
        "CancelOperationRequestIn": "_privateca_36_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_privateca_37_CancelOperationRequestOut",
        "CertChainIn": "_privateca_38_CertChainIn",
        "CertChainOut": "_privateca_39_CertChainOut",
        "ExprIn": "_privateca_40_ExprIn",
        "ExprOut": "_privateca_41_ExprOut",
        "CertificateIn": "_privateca_42_CertificateIn",
        "CertificateOut": "_privateca_43_CertificateOut",
        "PolicyIn": "_privateca_44_PolicyIn",
        "PolicyOut": "_privateca_45_PolicyOut",
        "RevocationDetailsIn": "_privateca_46_RevocationDetailsIn",
        "RevocationDetailsOut": "_privateca_47_RevocationDetailsOut",
        "TestIamPermissionsResponseIn": "_privateca_48_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_privateca_49_TestIamPermissionsResponseOut",
        "PublicKeyIn": "_privateca_50_PublicKeyIn",
        "PublicKeyOut": "_privateca_51_PublicKeyOut",
        "BindingIn": "_privateca_52_BindingIn",
        "BindingOut": "_privateca_53_BindingOut",
        "ListCertificatesResponseIn": "_privateca_54_ListCertificatesResponseIn",
        "ListCertificatesResponseOut": "_privateca_55_ListCertificatesResponseOut",
        "EcKeyTypeIn": "_privateca_56_EcKeyTypeIn",
        "EcKeyTypeOut": "_privateca_57_EcKeyTypeOut",
        "NameConstraintsIn": "_privateca_58_NameConstraintsIn",
        "NameConstraintsOut": "_privateca_59_NameConstraintsOut",
        "KeyUsageOptionsIn": "_privateca_60_KeyUsageOptionsIn",
        "KeyUsageOptionsOut": "_privateca_61_KeyUsageOptionsOut",
        "CertificateIdentityConstraintsIn": "_privateca_62_CertificateIdentityConstraintsIn",
        "CertificateIdentityConstraintsOut": "_privateca_63_CertificateIdentityConstraintsOut",
        "CertificateConfigIn": "_privateca_64_CertificateConfigIn",
        "CertificateConfigOut": "_privateca_65_CertificateConfigOut",
        "ListOperationsResponseIn": "_privateca_66_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_privateca_67_ListOperationsResponseOut",
        "CertificateDescriptionIn": "_privateca_68_CertificateDescriptionIn",
        "CertificateDescriptionOut": "_privateca_69_CertificateDescriptionOut",
        "ListCertificateAuthoritiesResponseIn": "_privateca_70_ListCertificateAuthoritiesResponseIn",
        "ListCertificateAuthoritiesResponseOut": "_privateca_71_ListCertificateAuthoritiesResponseOut",
        "IssuancePolicyIn": "_privateca_72_IssuancePolicyIn",
        "IssuancePolicyOut": "_privateca_73_IssuancePolicyOut",
        "KeyIdIn": "_privateca_74_KeyIdIn",
        "KeyIdOut": "_privateca_75_KeyIdOut",
        "FetchCaCertsResponseIn": "_privateca_76_FetchCaCertsResponseIn",
        "FetchCaCertsResponseOut": "_privateca_77_FetchCaCertsResponseOut",
        "SubjectIn": "_privateca_78_SubjectIn",
        "SubjectOut": "_privateca_79_SubjectOut",
        "ActivateCertificateAuthorityRequestIn": "_privateca_80_ActivateCertificateAuthorityRequestIn",
        "ActivateCertificateAuthorityRequestOut": "_privateca_81_ActivateCertificateAuthorityRequestOut",
        "CertificateFingerprintIn": "_privateca_82_CertificateFingerprintIn",
        "CertificateFingerprintOut": "_privateca_83_CertificateFingerprintOut",
        "ListCaPoolsResponseIn": "_privateca_84_ListCaPoolsResponseIn",
        "ListCaPoolsResponseOut": "_privateca_85_ListCaPoolsResponseOut",
        "IssuanceModesIn": "_privateca_86_IssuanceModesIn",
        "IssuanceModesOut": "_privateca_87_IssuanceModesOut",
        "CertificateRevocationListIn": "_privateca_88_CertificateRevocationListIn",
        "CertificateRevocationListOut": "_privateca_89_CertificateRevocationListOut",
        "SubordinateConfigIn": "_privateca_90_SubordinateConfigIn",
        "SubordinateConfigOut": "_privateca_91_SubordinateConfigOut",
        "CertificateTemplateIn": "_privateca_92_CertificateTemplateIn",
        "CertificateTemplateOut": "_privateca_93_CertificateTemplateOut",
        "ObjectIdIn": "_privateca_94_ObjectIdIn",
        "ObjectIdOut": "_privateca_95_ObjectIdOut",
        "LocationIn": "_privateca_96_LocationIn",
        "LocationOut": "_privateca_97_LocationOut",
        "UndeleteCertificateAuthorityRequestIn": "_privateca_98_UndeleteCertificateAuthorityRequestIn",
        "UndeleteCertificateAuthorityRequestOut": "_privateca_99_UndeleteCertificateAuthorityRequestOut",
        "StatusIn": "_privateca_100_StatusIn",
        "StatusOut": "_privateca_101_StatusOut",
        "CaOptionsIn": "_privateca_102_CaOptionsIn",
        "CaOptionsOut": "_privateca_103_CaOptionsOut",
        "ListLocationsResponseIn": "_privateca_104_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_privateca_105_ListLocationsResponseOut",
        "ListCertificateTemplatesResponseIn": "_privateca_106_ListCertificateTemplatesResponseIn",
        "ListCertificateTemplatesResponseOut": "_privateca_107_ListCertificateTemplatesResponseOut",
        "TestIamPermissionsRequestIn": "_privateca_108_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_privateca_109_TestIamPermissionsRequestOut",
        "CaPoolIn": "_privateca_110_CaPoolIn",
        "CaPoolOut": "_privateca_111_CaPoolOut",
        "RsaKeyTypeIn": "_privateca_112_RsaKeyTypeIn",
        "RsaKeyTypeOut": "_privateca_113_RsaKeyTypeOut",
        "EmptyIn": "_privateca_114_EmptyIn",
        "EmptyOut": "_privateca_115_EmptyOut",
        "ReconciliationOperationMetadataIn": "_privateca_116_ReconciliationOperationMetadataIn",
        "ReconciliationOperationMetadataOut": "_privateca_117_ReconciliationOperationMetadataOut",
        "KeyVersionSpecIn": "_privateca_118_KeyVersionSpecIn",
        "KeyVersionSpecOut": "_privateca_119_KeyVersionSpecOut",
        "PublishingOptionsIn": "_privateca_120_PublishingOptionsIn",
        "PublishingOptionsOut": "_privateca_121_PublishingOptionsOut",
        "CertificateAuthorityIn": "_privateca_122_CertificateAuthorityIn",
        "CertificateAuthorityOut": "_privateca_123_CertificateAuthorityOut",
        "CertificateExtensionConstraintsIn": "_privateca_124_CertificateExtensionConstraintsIn",
        "CertificateExtensionConstraintsOut": "_privateca_125_CertificateExtensionConstraintsOut",
        "FetchCertificateAuthorityCsrResponseIn": "_privateca_126_FetchCertificateAuthorityCsrResponseIn",
        "FetchCertificateAuthorityCsrResponseOut": "_privateca_127_FetchCertificateAuthorityCsrResponseOut",
        "AllowedKeyTypeIn": "_privateca_128_AllowedKeyTypeIn",
        "AllowedKeyTypeOut": "_privateca_129_AllowedKeyTypeOut",
        "DisableCertificateAuthorityRequestIn": "_privateca_130_DisableCertificateAuthorityRequestIn",
        "DisableCertificateAuthorityRequestOut": "_privateca_131_DisableCertificateAuthorityRequestOut",
        "KeyUsageIn": "_privateca_132_KeyUsageIn",
        "KeyUsageOut": "_privateca_133_KeyUsageOut",
        "AuditConfigIn": "_privateca_134_AuditConfigIn",
        "AuditConfigOut": "_privateca_135_AuditConfigOut",
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
    types["X509ExtensionIn"] = t.struct(
        {
            "value": t.string(),
            "critical": t.boolean().optional(),
            "objectId": t.proxy(renames["ObjectIdIn"]),
        }
    ).named(renames["X509ExtensionIn"])
    types["X509ExtensionOut"] = t.struct(
        {
            "value": t.string(),
            "critical": t.boolean().optional(),
            "objectId": t.proxy(renames["ObjectIdOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["X509ExtensionOut"])
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
    types["OperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["EnableCertificateAuthorityRequestIn"] = t.struct(
        {"requestId": t.string().optional()}
    ).named(renames["EnableCertificateAuthorityRequestIn"])
    types["EnableCertificateAuthorityRequestOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnableCertificateAuthorityRequestOut"])
    types["SubjectAltNamesIn"] = t.struct(
        {
            "dnsNames": t.array(t.string()).optional(),
            "emailAddresses": t.array(t.string()).optional(),
            "ipAddresses": t.array(t.string()).optional(),
            "uris": t.array(t.string()).optional(),
            "customSans": t.array(t.proxy(renames["X509ExtensionIn"])).optional(),
        }
    ).named(renames["SubjectAltNamesIn"])
    types["SubjectAltNamesOut"] = t.struct(
        {
            "dnsNames": t.array(t.string()).optional(),
            "emailAddresses": t.array(t.string()).optional(),
            "ipAddresses": t.array(t.string()).optional(),
            "uris": t.array(t.string()).optional(),
            "customSans": t.array(t.proxy(renames["X509ExtensionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubjectAltNamesOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "target": t.string().optional(),
            "apiVersion": t.string().optional(),
            "createTime": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "endTime": t.string().optional(),
            "statusMessage": t.string().optional(),
            "verb": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["SubordinateConfigChainIn"] = t.struct(
        {"pemCertificates": t.array(t.string())}
    ).named(renames["SubordinateConfigChainIn"])
    types["SubordinateConfigChainOut"] = t.struct(
        {
            "pemCertificates": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubordinateConfigChainOut"])
    types["RevokedCertificateIn"] = t.struct(
        {
            "revocationReason": t.string().optional(),
            "certificate": t.string().optional(),
            "hexSerialNumber": t.string().optional(),
        }
    ).named(renames["RevokedCertificateIn"])
    types["RevokedCertificateOut"] = t.struct(
        {
            "revocationReason": t.string().optional(),
            "certificate": t.string().optional(),
            "hexSerialNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RevokedCertificateOut"])
    types["SubjectDescriptionIn"] = t.struct(
        {
            "subject": t.proxy(renames["SubjectIn"]).optional(),
            "notBeforeTime": t.string().optional(),
            "notAfterTime": t.string().optional(),
            "hexSerialNumber": t.string().optional(),
            "lifetime": t.string().optional(),
            "subjectAltName": t.proxy(renames["SubjectAltNamesIn"]).optional(),
        }
    ).named(renames["SubjectDescriptionIn"])
    types["SubjectDescriptionOut"] = t.struct(
        {
            "subject": t.proxy(renames["SubjectOut"]).optional(),
            "notBeforeTime": t.string().optional(),
            "notAfterTime": t.string().optional(),
            "hexSerialNumber": t.string().optional(),
            "lifetime": t.string().optional(),
            "subjectAltName": t.proxy(renames["SubjectAltNamesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubjectDescriptionOut"])
    types["X509ParametersIn"] = t.struct(
        {
            "policyIds": t.array(t.proxy(renames["ObjectIdIn"])).optional(),
            "nameConstraints": t.proxy(renames["NameConstraintsIn"]).optional(),
            "aiaOcspServers": t.array(t.string()).optional(),
            "additionalExtensions": t.array(
                t.proxy(renames["X509ExtensionIn"])
            ).optional(),
            "caOptions": t.proxy(renames["CaOptionsIn"]).optional(),
            "keyUsage": t.proxy(renames["KeyUsageIn"]).optional(),
        }
    ).named(renames["X509ParametersIn"])
    types["X509ParametersOut"] = t.struct(
        {
            "policyIds": t.array(t.proxy(renames["ObjectIdOut"])).optional(),
            "nameConstraints": t.proxy(renames["NameConstraintsOut"]).optional(),
            "aiaOcspServers": t.array(t.string()).optional(),
            "additionalExtensions": t.array(
                t.proxy(renames["X509ExtensionOut"])
            ).optional(),
            "caOptions": t.proxy(renames["CaOptionsOut"]).optional(),
            "keyUsage": t.proxy(renames["KeyUsageOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["X509ParametersOut"])
    types["FetchCaCertsRequestIn"] = t.struct(
        {"requestId": t.string().optional()}
    ).named(renames["FetchCaCertsRequestIn"])
    types["FetchCaCertsRequestOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FetchCaCertsRequestOut"])
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
    types["ExtendedKeyUsageOptionsIn"] = t.struct(
        {
            "ocspSigning": t.boolean().optional(),
            "serverAuth": t.boolean().optional(),
            "codeSigning": t.boolean().optional(),
            "timeStamping": t.boolean().optional(),
            "clientAuth": t.boolean().optional(),
            "emailProtection": t.boolean().optional(),
        }
    ).named(renames["ExtendedKeyUsageOptionsIn"])
    types["ExtendedKeyUsageOptionsOut"] = t.struct(
        {
            "ocspSigning": t.boolean().optional(),
            "serverAuth": t.boolean().optional(),
            "codeSigning": t.boolean().optional(),
            "timeStamping": t.boolean().optional(),
            "clientAuth": t.boolean().optional(),
            "emailProtection": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExtendedKeyUsageOptionsOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["CertChainIn"] = t.struct(
        {"certificates": t.array(t.string()).optional()}
    ).named(renames["CertChainIn"])
    types["CertChainOut"] = t.struct(
        {
            "certificates": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertChainOut"])
    types["ExprIn"] = t.struct(
        {
            "description": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "description": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["CertificateIn"] = t.struct(
        {
            "pemCsr": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "certificateTemplate": t.string().optional(),
            "subjectMode": t.string().optional(),
            "lifetime": t.string(),
            "config": t.proxy(renames["CertificateConfigIn"]).optional(),
        }
    ).named(renames["CertificateIn"])
    types["CertificateOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "pemCsr": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "certificateTemplate": t.string().optional(),
            "pemCertificateChain": t.array(t.string()).optional(),
            "subjectMode": t.string().optional(),
            "revocationDetails": t.proxy(renames["RevocationDetailsOut"]).optional(),
            "lifetime": t.string(),
            "issuerCertificateAuthority": t.string().optional(),
            "config": t.proxy(renames["CertificateConfigOut"]).optional(),
            "certificateDescription": t.proxy(
                renames["CertificateDescriptionOut"]
            ).optional(),
            "updateTime": t.string().optional(),
            "pemCertificate": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateOut"])
    types["PolicyIn"] = t.struct(
        {
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
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
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["PublicKeyIn"] = t.struct({"format": t.string(), "key": t.string()}).named(
        renames["PublicKeyIn"]
    )
    types["PublicKeyOut"] = t.struct(
        {
            "format": t.string(),
            "key": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublicKeyOut"])
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
    types["ListCertificatesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "certificates": t.array(t.proxy(renames["CertificateIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListCertificatesResponseIn"])
    types["ListCertificatesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "certificates": t.array(t.proxy(renames["CertificateOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCertificatesResponseOut"])
    types["EcKeyTypeIn"] = t.struct(
        {"signatureAlgorithm": t.string().optional()}
    ).named(renames["EcKeyTypeIn"])
    types["EcKeyTypeOut"] = t.struct(
        {
            "signatureAlgorithm": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EcKeyTypeOut"])
    types["NameConstraintsIn"] = t.struct(
        {
            "excludedIpRanges": t.array(t.string()).optional(),
            "permittedIpRanges": t.array(t.string()).optional(),
            "excludedDnsNames": t.array(t.string()).optional(),
            "permittedDnsNames": t.array(t.string()).optional(),
            "critical": t.boolean().optional(),
            "permittedEmailAddresses": t.array(t.string()).optional(),
            "excludedUris": t.array(t.string()).optional(),
            "excludedEmailAddresses": t.array(t.string()).optional(),
            "permittedUris": t.array(t.string()).optional(),
        }
    ).named(renames["NameConstraintsIn"])
    types["NameConstraintsOut"] = t.struct(
        {
            "excludedIpRanges": t.array(t.string()).optional(),
            "permittedIpRanges": t.array(t.string()).optional(),
            "excludedDnsNames": t.array(t.string()).optional(),
            "permittedDnsNames": t.array(t.string()).optional(),
            "critical": t.boolean().optional(),
            "permittedEmailAddresses": t.array(t.string()).optional(),
            "excludedUris": t.array(t.string()).optional(),
            "excludedEmailAddresses": t.array(t.string()).optional(),
            "permittedUris": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NameConstraintsOut"])
    types["KeyUsageOptionsIn"] = t.struct(
        {
            "digitalSignature": t.boolean().optional(),
            "keyAgreement": t.boolean().optional(),
            "decipherOnly": t.boolean().optional(),
            "keyEncipherment": t.boolean().optional(),
            "certSign": t.boolean().optional(),
            "contentCommitment": t.boolean().optional(),
            "crlSign": t.boolean().optional(),
            "dataEncipherment": t.boolean().optional(),
            "encipherOnly": t.boolean().optional(),
        }
    ).named(renames["KeyUsageOptionsIn"])
    types["KeyUsageOptionsOut"] = t.struct(
        {
            "digitalSignature": t.boolean().optional(),
            "keyAgreement": t.boolean().optional(),
            "decipherOnly": t.boolean().optional(),
            "keyEncipherment": t.boolean().optional(),
            "certSign": t.boolean().optional(),
            "contentCommitment": t.boolean().optional(),
            "crlSign": t.boolean().optional(),
            "dataEncipherment": t.boolean().optional(),
            "encipherOnly": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyUsageOptionsOut"])
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
    types["CertificateConfigIn"] = t.struct(
        {
            "publicKey": t.proxy(renames["PublicKeyIn"]).optional(),
            "subjectConfig": t.proxy(renames["SubjectConfigIn"]),
            "x509Config": t.proxy(renames["X509ParametersIn"]),
        }
    ).named(renames["CertificateConfigIn"])
    types["CertificateConfigOut"] = t.struct(
        {
            "publicKey": t.proxy(renames["PublicKeyOut"]).optional(),
            "subjectConfig": t.proxy(renames["SubjectConfigOut"]),
            "x509Config": t.proxy(renames["X509ParametersOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateConfigOut"])
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
    types["CertificateDescriptionIn"] = t.struct(
        {
            "x509Description": t.proxy(renames["X509ParametersIn"]).optional(),
            "certFingerprint": t.proxy(renames["CertificateFingerprintIn"]).optional(),
            "publicKey": t.proxy(renames["PublicKeyIn"]).optional(),
            "crlDistributionPoints": t.array(t.string()).optional(),
            "subjectKeyId": t.proxy(renames["KeyIdIn"]).optional(),
            "authorityKeyId": t.proxy(renames["KeyIdIn"]).optional(),
            "subjectDescription": t.proxy(renames["SubjectDescriptionIn"]).optional(),
            "aiaIssuingCertificateUrls": t.array(t.string()).optional(),
        }
    ).named(renames["CertificateDescriptionIn"])
    types["CertificateDescriptionOut"] = t.struct(
        {
            "x509Description": t.proxy(renames["X509ParametersOut"]).optional(),
            "certFingerprint": t.proxy(renames["CertificateFingerprintOut"]).optional(),
            "publicKey": t.proxy(renames["PublicKeyOut"]).optional(),
            "crlDistributionPoints": t.array(t.string()).optional(),
            "subjectKeyId": t.proxy(renames["KeyIdOut"]).optional(),
            "authorityKeyId": t.proxy(renames["KeyIdOut"]).optional(),
            "subjectDescription": t.proxy(renames["SubjectDescriptionOut"]).optional(),
            "aiaIssuingCertificateUrls": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateDescriptionOut"])
    types["ListCertificateAuthoritiesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "certificateAuthorities": t.array(
                t.proxy(renames["CertificateAuthorityIn"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListCertificateAuthoritiesResponseIn"])
    types["ListCertificateAuthoritiesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "certificateAuthorities": t.array(
                t.proxy(renames["CertificateAuthorityOut"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCertificateAuthoritiesResponseOut"])
    types["IssuancePolicyIn"] = t.struct(
        {
            "baselineValues": t.proxy(renames["X509ParametersIn"]).optional(),
            "allowedIssuanceModes": t.proxy(renames["IssuanceModesIn"]).optional(),
            "allowedKeyTypes": t.array(t.proxy(renames["AllowedKeyTypeIn"])).optional(),
            "maximumLifetime": t.string().optional(),
            "passthroughExtensions": t.proxy(
                renames["CertificateExtensionConstraintsIn"]
            ).optional(),
            "identityConstraints": t.proxy(
                renames["CertificateIdentityConstraintsIn"]
            ).optional(),
        }
    ).named(renames["IssuancePolicyIn"])
    types["IssuancePolicyOut"] = t.struct(
        {
            "baselineValues": t.proxy(renames["X509ParametersOut"]).optional(),
            "allowedIssuanceModes": t.proxy(renames["IssuanceModesOut"]).optional(),
            "allowedKeyTypes": t.array(
                t.proxy(renames["AllowedKeyTypeOut"])
            ).optional(),
            "maximumLifetime": t.string().optional(),
            "passthroughExtensions": t.proxy(
                renames["CertificateExtensionConstraintsOut"]
            ).optional(),
            "identityConstraints": t.proxy(
                renames["CertificateIdentityConstraintsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IssuancePolicyOut"])
    types["KeyIdIn"] = t.struct({"keyId": t.string().optional()}).named(
        renames["KeyIdIn"]
    )
    types["KeyIdOut"] = t.struct(
        {
            "keyId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyIdOut"])
    types["FetchCaCertsResponseIn"] = t.struct(
        {"caCerts": t.array(t.proxy(renames["CertChainIn"])).optional()}
    ).named(renames["FetchCaCertsResponseIn"])
    types["FetchCaCertsResponseOut"] = t.struct(
        {
            "caCerts": t.array(t.proxy(renames["CertChainOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FetchCaCertsResponseOut"])
    types["SubjectIn"] = t.struct(
        {
            "organization": t.string().optional(),
            "postalCode": t.string().optional(),
            "organizationalUnit": t.string().optional(),
            "province": t.string().optional(),
            "countryCode": t.string().optional(),
            "streetAddress": t.string().optional(),
            "locality": t.string().optional(),
            "commonName": t.string().optional(),
        }
    ).named(renames["SubjectIn"])
    types["SubjectOut"] = t.struct(
        {
            "organization": t.string().optional(),
            "postalCode": t.string().optional(),
            "organizationalUnit": t.string().optional(),
            "province": t.string().optional(),
            "countryCode": t.string().optional(),
            "streetAddress": t.string().optional(),
            "locality": t.string().optional(),
            "commonName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubjectOut"])
    types["ActivateCertificateAuthorityRequestIn"] = t.struct(
        {
            "subordinateConfig": t.proxy(renames["SubordinateConfigIn"]),
            "requestId": t.string().optional(),
            "pemCaCertificate": t.string(),
        }
    ).named(renames["ActivateCertificateAuthorityRequestIn"])
    types["ActivateCertificateAuthorityRequestOut"] = t.struct(
        {
            "subordinateConfig": t.proxy(renames["SubordinateConfigOut"]),
            "requestId": t.string().optional(),
            "pemCaCertificate": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActivateCertificateAuthorityRequestOut"])
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
            "caPools": t.array(t.proxy(renames["CaPoolIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListCaPoolsResponseIn"])
    types["ListCaPoolsResponseOut"] = t.struct(
        {
            "caPools": t.array(t.proxy(renames["CaPoolOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCaPoolsResponseOut"])
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
    types["CertificateRevocationListIn"] = t.struct(
        {"labels": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["CertificateRevocationListIn"])
    types["CertificateRevocationListOut"] = t.struct(
        {
            "state": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "sequenceNumber": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "pemCrl": t.string().optional(),
            "revisionId": t.string().optional(),
            "accessUrl": t.string().optional(),
            "revokedCertificates": t.array(
                t.proxy(renames["RevokedCertificateOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateRevocationListOut"])
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
    types["CertificateTemplateIn"] = t.struct(
        {
            "passthroughExtensions": t.proxy(
                renames["CertificateExtensionConstraintsIn"]
            ).optional(),
            "predefinedValues": t.proxy(renames["X509ParametersIn"]).optional(),
            "description": t.string().optional(),
            "identityConstraints": t.proxy(
                renames["CertificateIdentityConstraintsIn"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["CertificateTemplateIn"])
    types["CertificateTemplateOut"] = t.struct(
        {
            "passthroughExtensions": t.proxy(
                renames["CertificateExtensionConstraintsOut"]
            ).optional(),
            "name": t.string().optional(),
            "predefinedValues": t.proxy(renames["X509ParametersOut"]).optional(),
            "description": t.string().optional(),
            "identityConstraints": t.proxy(
                renames["CertificateIdentityConstraintsOut"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateTemplateOut"])
    types["ObjectIdIn"] = t.struct({"objectIdPath": t.array(t.integer())}).named(
        renames["ObjectIdIn"]
    )
    types["ObjectIdOut"] = t.struct(
        {
            "objectIdPath": t.array(t.integer()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ObjectIdOut"])
    types["LocationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["UndeleteCertificateAuthorityRequestIn"] = t.struct(
        {"requestId": t.string().optional()}
    ).named(renames["UndeleteCertificateAuthorityRequestIn"])
    types["UndeleteCertificateAuthorityRequestOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UndeleteCertificateAuthorityRequestOut"])
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
    types["ListCertificateTemplatesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "certificateTemplates": t.array(
                t.proxy(renames["CertificateTemplateIn"])
            ).optional(),
        }
    ).named(renames["ListCertificateTemplatesResponseIn"])
    types["ListCertificateTemplatesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "certificateTemplates": t.array(
                t.proxy(renames["CertificateTemplateOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCertificateTemplatesResponseOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["CaPoolIn"] = t.struct(
        {
            "tier": t.string(),
            "publishingOptions": t.proxy(renames["PublishingOptionsIn"]).optional(),
            "issuancePolicy": t.proxy(renames["IssuancePolicyIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["CaPoolIn"])
    types["CaPoolOut"] = t.struct(
        {
            "tier": t.string(),
            "name": t.string().optional(),
            "publishingOptions": t.proxy(renames["PublishingOptionsOut"]).optional(),
            "issuancePolicy": t.proxy(renames["IssuancePolicyOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CaPoolOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["PublishingOptionsIn"] = t.struct(
        {
            "publishCrl": t.boolean().optional(),
            "publishCaCert": t.boolean().optional(),
            "encodingFormat": t.string().optional(),
        }
    ).named(renames["PublishingOptionsIn"])
    types["PublishingOptionsOut"] = t.struct(
        {
            "publishCrl": t.boolean().optional(),
            "publishCaCert": t.boolean().optional(),
            "encodingFormat": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublishingOptionsOut"])
    types["CertificateAuthorityIn"] = t.struct(
        {
            "lifetime": t.string(),
            "subordinateConfig": t.proxy(renames["SubordinateConfigIn"]).optional(),
            "gcsBucket": t.string().optional(),
            "config": t.proxy(renames["CertificateConfigIn"]),
            "keySpec": t.proxy(renames["KeyVersionSpecIn"]),
            "type": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["CertificateAuthorityIn"])
    types["CertificateAuthorityOut"] = t.struct(
        {
            "expireTime": t.string().optional(),
            "name": t.string().optional(),
            "deleteTime": t.string().optional(),
            "state": t.string().optional(),
            "caCertificateDescriptions": t.array(
                t.proxy(renames["CertificateDescriptionOut"])
            ).optional(),
            "accessUrls": t.proxy(renames["AccessUrlsOut"]).optional(),
            "updateTime": t.string().optional(),
            "lifetime": t.string(),
            "subordinateConfig": t.proxy(renames["SubordinateConfigOut"]).optional(),
            "gcsBucket": t.string().optional(),
            "config": t.proxy(renames["CertificateConfigOut"]),
            "tier": t.string().optional(),
            "keySpec": t.proxy(renames["KeyVersionSpecOut"]),
            "type": t.string(),
            "pemCaCertificates": t.array(t.string()).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateAuthorityOut"])
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
    types["FetchCertificateAuthorityCsrResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["FetchCertificateAuthorityCsrResponseIn"])
    types["FetchCertificateAuthorityCsrResponseOut"] = t.struct(
        {
            "pemCsr": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FetchCertificateAuthorityCsrResponseOut"])
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

    functions = {}
    functions["projectsLocationsGet"] = privateca.get(
        "v1/{name}/locations",
        t.struct(
            {
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCertificateTemplatesCreate"] = privateca.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "requestId": t.string().optional(),
                "updateMask": t.string(),
                "passthroughExtensions": t.proxy(
                    renames["CertificateExtensionConstraintsIn"]
                ).optional(),
                "predefinedValues": t.proxy(renames["X509ParametersIn"]).optional(),
                "description": t.string().optional(),
                "identityConstraints": t.proxy(
                    renames["CertificateIdentityConstraintsIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCertificateTemplatesList"] = privateca.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "requestId": t.string().optional(),
                "updateMask": t.string(),
                "passthroughExtensions": t.proxy(
                    renames["CertificateExtensionConstraintsIn"]
                ).optional(),
                "predefinedValues": t.proxy(renames["X509ParametersIn"]).optional(),
                "description": t.string().optional(),
                "identityConstraints": t.proxy(
                    renames["CertificateIdentityConstraintsIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCertificateTemplatesDelete"] = privateca.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "requestId": t.string().optional(),
                "updateMask": t.string(),
                "passthroughExtensions": t.proxy(
                    renames["CertificateExtensionConstraintsIn"]
                ).optional(),
                "predefinedValues": t.proxy(renames["X509ParametersIn"]).optional(),
                "description": t.string().optional(),
                "identityConstraints": t.proxy(
                    renames["CertificateIdentityConstraintsIn"]
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
    ] = privateca.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "requestId": t.string().optional(),
                "updateMask": t.string(),
                "passthroughExtensions": t.proxy(
                    renames["CertificateExtensionConstraintsIn"]
                ).optional(),
                "predefinedValues": t.proxy(renames["X509ParametersIn"]).optional(),
                "description": t.string().optional(),
                "identityConstraints": t.proxy(
                    renames["CertificateIdentityConstraintsIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCertificateTemplatesGetIamPolicy"] = privateca.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "requestId": t.string().optional(),
                "updateMask": t.string(),
                "passthroughExtensions": t.proxy(
                    renames["CertificateExtensionConstraintsIn"]
                ).optional(),
                "predefinedValues": t.proxy(renames["X509ParametersIn"]).optional(),
                "description": t.string().optional(),
                "identityConstraints": t.proxy(
                    renames["CertificateIdentityConstraintsIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCertificateTemplatesSetIamPolicy"] = privateca.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "requestId": t.string().optional(),
                "updateMask": t.string(),
                "passthroughExtensions": t.proxy(
                    renames["CertificateExtensionConstraintsIn"]
                ).optional(),
                "predefinedValues": t.proxy(renames["X509ParametersIn"]).optional(),
                "description": t.string().optional(),
                "identityConstraints": t.proxy(
                    renames["CertificateIdentityConstraintsIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCertificateTemplatesGet"] = privateca.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "requestId": t.string().optional(),
                "updateMask": t.string(),
                "passthroughExtensions": t.proxy(
                    renames["CertificateExtensionConstraintsIn"]
                ).optional(),
                "predefinedValues": t.proxy(renames["X509ParametersIn"]).optional(),
                "description": t.string().optional(),
                "identityConstraints": t.proxy(
                    renames["CertificateIdentityConstraintsIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCertificateTemplatesPatch"] = privateca.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "requestId": t.string().optional(),
                "updateMask": t.string(),
                "passthroughExtensions": t.proxy(
                    renames["CertificateExtensionConstraintsIn"]
                ).optional(),
                "predefinedValues": t.proxy(renames["X509ParametersIn"]).optional(),
                "description": t.string().optional(),
                "identityConstraints": t.proxy(
                    renames["CertificateIdentityConstraintsIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = privateca.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = privateca.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = privateca.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = privateca.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsGet"] = privateca.post(
        "v1/{parent}/caPools",
        t.struct(
            {
                "caPoolId": t.string(),
                "parent": t.string(),
                "requestId": t.string().optional(),
                "tier": t.string(),
                "publishingOptions": t.proxy(renames["PublishingOptionsIn"]).optional(),
                "issuancePolicy": t.proxy(renames["IssuancePolicyIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsDelete"] = privateca.post(
        "v1/{parent}/caPools",
        t.struct(
            {
                "caPoolId": t.string(),
                "parent": t.string(),
                "requestId": t.string().optional(),
                "tier": t.string(),
                "publishingOptions": t.proxy(renames["PublishingOptionsIn"]).optional(),
                "issuancePolicy": t.proxy(renames["IssuancePolicyIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsSetIamPolicy"] = privateca.post(
        "v1/{parent}/caPools",
        t.struct(
            {
                "caPoolId": t.string(),
                "parent": t.string(),
                "requestId": t.string().optional(),
                "tier": t.string(),
                "publishingOptions": t.proxy(renames["PublishingOptionsIn"]).optional(),
                "issuancePolicy": t.proxy(renames["IssuancePolicyIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsTestIamPermissions"] = privateca.post(
        "v1/{parent}/caPools",
        t.struct(
            {
                "caPoolId": t.string(),
                "parent": t.string(),
                "requestId": t.string().optional(),
                "tier": t.string(),
                "publishingOptions": t.proxy(renames["PublishingOptionsIn"]).optional(),
                "issuancePolicy": t.proxy(renames["IssuancePolicyIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsList"] = privateca.post(
        "v1/{parent}/caPools",
        t.struct(
            {
                "caPoolId": t.string(),
                "parent": t.string(),
                "requestId": t.string().optional(),
                "tier": t.string(),
                "publishingOptions": t.proxy(renames["PublishingOptionsIn"]).optional(),
                "issuancePolicy": t.proxy(renames["IssuancePolicyIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsPatch"] = privateca.post(
        "v1/{parent}/caPools",
        t.struct(
            {
                "caPoolId": t.string(),
                "parent": t.string(),
                "requestId": t.string().optional(),
                "tier": t.string(),
                "publishingOptions": t.proxy(renames["PublishingOptionsIn"]).optional(),
                "issuancePolicy": t.proxy(renames["IssuancePolicyIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsGetIamPolicy"] = privateca.post(
        "v1/{parent}/caPools",
        t.struct(
            {
                "caPoolId": t.string(),
                "parent": t.string(),
                "requestId": t.string().optional(),
                "tier": t.string(),
                "publishingOptions": t.proxy(renames["PublishingOptionsIn"]).optional(),
                "issuancePolicy": t.proxy(renames["IssuancePolicyIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsFetchCaCerts"] = privateca.post(
        "v1/{parent}/caPools",
        t.struct(
            {
                "caPoolId": t.string(),
                "parent": t.string(),
                "requestId": t.string().optional(),
                "tier": t.string(),
                "publishingOptions": t.proxy(renames["PublishingOptionsIn"]).optional(),
                "issuancePolicy": t.proxy(renames["IssuancePolicyIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsCreate"] = privateca.post(
        "v1/{parent}/caPools",
        t.struct(
            {
                "caPoolId": t.string(),
                "parent": t.string(),
                "requestId": t.string().optional(),
                "tier": t.string(),
                "publishingOptions": t.proxy(renames["PublishingOptionsIn"]).optional(),
                "issuancePolicy": t.proxy(renames["IssuancePolicyIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsCertificateAuthoritiesDelete"] = privateca.post(
        "v1/{name}:undelete",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsCertificateAuthoritiesList"] = privateca.post(
        "v1/{name}:undelete",
        t.struct(
            {
                "name": t.string(),
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
        "v1/{name}:undelete",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsCertificateAuthoritiesEnable"] = privateca.post(
        "v1/{name}:undelete",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsCertificateAuthoritiesCreate"] = privateca.post(
        "v1/{name}:undelete",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsCertificateAuthoritiesPatch"] = privateca.post(
        "v1/{name}:undelete",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsCertificateAuthoritiesFetch"] = privateca.post(
        "v1/{name}:undelete",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsCertificateAuthoritiesDisable"] = privateca.post(
        "v1/{name}:undelete",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsCertificateAuthoritiesGet"] = privateca.post(
        "v1/{name}:undelete",
        t.struct(
            {
                "name": t.string(),
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
        "v1/{name}:undelete",
        t.struct(
            {
                "name": t.string(),
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
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CertificateRevocationListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCaPoolsCertificateAuthoritiesCertificateRevocationListsTestIamPermissions"
    ] = privateca.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CertificateRevocationListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCaPoolsCertificateAuthoritiesCertificateRevocationListsGetIamPolicy"
    ] = privateca.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CertificateRevocationListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCaPoolsCertificateAuthoritiesCertificateRevocationListsList"
    ] = privateca.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CertificateRevocationListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCaPoolsCertificateAuthoritiesCertificateRevocationListsPatch"
    ] = privateca.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CertificateRevocationListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCaPoolsCertificateAuthoritiesCertificateRevocationListsGet"
    ] = privateca.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CertificateRevocationListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsCertificatesCreate"] = privateca.post(
        "v1/{name}:revoke",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "reason": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CertificateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsCertificatesPatch"] = privateca.post(
        "v1/{name}:revoke",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "reason": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CertificateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsCertificatesGet"] = privateca.post(
        "v1/{name}:revoke",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "reason": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CertificateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsCertificatesList"] = privateca.post(
        "v1/{name}:revoke",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "reason": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CertificateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCaPoolsCertificatesRevoke"] = privateca.post(
        "v1/{name}:revoke",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "reason": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CertificateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="privateca",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
