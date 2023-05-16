from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_certificatemanager() -> Import:
    certificatemanager = HTTPRuntime("https://certificatemanager.googleapis.com/")

    renames = {
        "ErrorResponse": "_certificatemanager_1_ErrorResponse",
        "CertificateAuthorityConfigIn": "_certificatemanager_2_CertificateAuthorityConfigIn",
        "CertificateAuthorityConfigOut": "_certificatemanager_3_CertificateAuthorityConfigOut",
        "IpConfigIn": "_certificatemanager_4_IpConfigIn",
        "IpConfigOut": "_certificatemanager_5_IpConfigOut",
        "EmptyIn": "_certificatemanager_6_EmptyIn",
        "EmptyOut": "_certificatemanager_7_EmptyOut",
        "ListLocationsResponseIn": "_certificatemanager_8_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_certificatemanager_9_ListLocationsResponseOut",
        "ListDnsAuthorizationsResponseIn": "_certificatemanager_10_ListDnsAuthorizationsResponseIn",
        "ListDnsAuthorizationsResponseOut": "_certificatemanager_11_ListDnsAuthorizationsResponseOut",
        "ListCertificateIssuanceConfigsResponseIn": "_certificatemanager_12_ListCertificateIssuanceConfigsResponseIn",
        "ListCertificateIssuanceConfigsResponseOut": "_certificatemanager_13_ListCertificateIssuanceConfigsResponseOut",
        "IntermediateCAIn": "_certificatemanager_14_IntermediateCAIn",
        "IntermediateCAOut": "_certificatemanager_15_IntermediateCAOut",
        "ListCertificateMapEntriesResponseIn": "_certificatemanager_16_ListCertificateMapEntriesResponseIn",
        "ListCertificateMapEntriesResponseOut": "_certificatemanager_17_ListCertificateMapEntriesResponseOut",
        "CertificateMapEntryIn": "_certificatemanager_18_CertificateMapEntryIn",
        "CertificateMapEntryOut": "_certificatemanager_19_CertificateMapEntryOut",
        "SelfManagedCertificateIn": "_certificatemanager_20_SelfManagedCertificateIn",
        "SelfManagedCertificateOut": "_certificatemanager_21_SelfManagedCertificateOut",
        "AuthorizationAttemptInfoIn": "_certificatemanager_22_AuthorizationAttemptInfoIn",
        "AuthorizationAttemptInfoOut": "_certificatemanager_23_AuthorizationAttemptInfoOut",
        "OperationMetadataIn": "_certificatemanager_24_OperationMetadataIn",
        "OperationMetadataOut": "_certificatemanager_25_OperationMetadataOut",
        "StatusIn": "_certificatemanager_26_StatusIn",
        "StatusOut": "_certificatemanager_27_StatusOut",
        "CertificateIssuanceConfigIn": "_certificatemanager_28_CertificateIssuanceConfigIn",
        "CertificateIssuanceConfigOut": "_certificatemanager_29_CertificateIssuanceConfigOut",
        "CertificateMapIn": "_certificatemanager_30_CertificateMapIn",
        "CertificateMapOut": "_certificatemanager_31_CertificateMapOut",
        "ProvisioningIssueIn": "_certificatemanager_32_ProvisioningIssueIn",
        "ProvisioningIssueOut": "_certificatemanager_33_ProvisioningIssueOut",
        "CertificateAuthorityServiceConfigIn": "_certificatemanager_34_CertificateAuthorityServiceConfigIn",
        "CertificateAuthorityServiceConfigOut": "_certificatemanager_35_CertificateAuthorityServiceConfigOut",
        "ListTrustConfigsResponseIn": "_certificatemanager_36_ListTrustConfigsResponseIn",
        "ListTrustConfigsResponseOut": "_certificatemanager_37_ListTrustConfigsResponseOut",
        "TrustConfigIn": "_certificatemanager_38_TrustConfigIn",
        "TrustConfigOut": "_certificatemanager_39_TrustConfigOut",
        "ManagedCertificateIn": "_certificatemanager_40_ManagedCertificateIn",
        "ManagedCertificateOut": "_certificatemanager_41_ManagedCertificateOut",
        "OperationIn": "_certificatemanager_42_OperationIn",
        "OperationOut": "_certificatemanager_43_OperationOut",
        "CertificateIn": "_certificatemanager_44_CertificateIn",
        "CertificateOut": "_certificatemanager_45_CertificateOut",
        "TrustAnchorIn": "_certificatemanager_46_TrustAnchorIn",
        "TrustAnchorOut": "_certificatemanager_47_TrustAnchorOut",
        "DnsAuthorizationIn": "_certificatemanager_48_DnsAuthorizationIn",
        "DnsAuthorizationOut": "_certificatemanager_49_DnsAuthorizationOut",
        "ListCertificateMapsResponseIn": "_certificatemanager_50_ListCertificateMapsResponseIn",
        "ListCertificateMapsResponseOut": "_certificatemanager_51_ListCertificateMapsResponseOut",
        "TrustStoreIn": "_certificatemanager_52_TrustStoreIn",
        "TrustStoreOut": "_certificatemanager_53_TrustStoreOut",
        "ListCertificatesResponseIn": "_certificatemanager_54_ListCertificatesResponseIn",
        "ListCertificatesResponseOut": "_certificatemanager_55_ListCertificatesResponseOut",
        "DnsResourceRecordIn": "_certificatemanager_56_DnsResourceRecordIn",
        "DnsResourceRecordOut": "_certificatemanager_57_DnsResourceRecordOut",
        "CancelOperationRequestIn": "_certificatemanager_58_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_certificatemanager_59_CancelOperationRequestOut",
        "ListOperationsResponseIn": "_certificatemanager_60_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_certificatemanager_61_ListOperationsResponseOut",
        "LocationIn": "_certificatemanager_62_LocationIn",
        "LocationOut": "_certificatemanager_63_LocationOut",
        "GclbTargetIn": "_certificatemanager_64_GclbTargetIn",
        "GclbTargetOut": "_certificatemanager_65_GclbTargetOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["CertificateAuthorityConfigIn"] = t.struct(
        {
            "certificateAuthorityServiceConfig": t.proxy(
                renames["CertificateAuthorityServiceConfigIn"]
            ).optional()
        }
    ).named(renames["CertificateAuthorityConfigIn"])
    types["CertificateAuthorityConfigOut"] = t.struct(
        {
            "certificateAuthorityServiceConfig": t.proxy(
                renames["CertificateAuthorityServiceConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateAuthorityConfigOut"])
    types["IpConfigIn"] = t.struct({"_": t.string().optional()}).named(
        renames["IpConfigIn"]
    )
    types["IpConfigOut"] = t.struct(
        {
            "ipAddress": t.string().optional(),
            "ports": t.array(t.integer()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IpConfigOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["ListDnsAuthorizationsResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "dnsAuthorizations": t.array(
                t.proxy(renames["DnsAuthorizationIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListDnsAuthorizationsResponseIn"])
    types["ListDnsAuthorizationsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "dnsAuthorizations": t.array(
                t.proxy(renames["DnsAuthorizationOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDnsAuthorizationsResponseOut"])
    types["ListCertificateIssuanceConfigsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "certificateIssuanceConfigs": t.array(
                t.proxy(renames["CertificateIssuanceConfigIn"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListCertificateIssuanceConfigsResponseIn"])
    types["ListCertificateIssuanceConfigsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "certificateIssuanceConfigs": t.array(
                t.proxy(renames["CertificateIssuanceConfigOut"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCertificateIssuanceConfigsResponseOut"])
    types["IntermediateCAIn"] = t.struct(
        {"pemCertificate": t.string().optional()}
    ).named(renames["IntermediateCAIn"])
    types["IntermediateCAOut"] = t.struct(
        {
            "pemCertificate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntermediateCAOut"])
    types["ListCertificateMapEntriesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "certificateMapEntries": t.array(
                t.proxy(renames["CertificateMapEntryIn"])
            ).optional(),
        }
    ).named(renames["ListCertificateMapEntriesResponseIn"])
    types["ListCertificateMapEntriesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "certificateMapEntries": t.array(
                t.proxy(renames["CertificateMapEntryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCertificateMapEntriesResponseOut"])
    types["CertificateMapEntryIn"] = t.struct(
        {
            "certificates": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "matcher": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "hostname": t.string().optional(),
        }
    ).named(renames["CertificateMapEntryIn"])
    types["CertificateMapEntryOut"] = t.struct(
        {
            "certificates": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "matcher": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "hostname": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateMapEntryOut"])
    types["SelfManagedCertificateIn"] = t.struct(
        {
            "pemCertificate": t.string().optional(),
            "pemPrivateKey": t.string().optional(),
        }
    ).named(renames["SelfManagedCertificateIn"])
    types["SelfManagedCertificateOut"] = t.struct(
        {
            "pemCertificate": t.string().optional(),
            "pemPrivateKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SelfManagedCertificateOut"])
    types["AuthorizationAttemptInfoIn"] = t.struct(
        {"domain": t.string().optional()}
    ).named(renames["AuthorizationAttemptInfoIn"])
    types["AuthorizationAttemptInfoOut"] = t.struct(
        {
            "failureReason": t.string().optional(),
            "details": t.string().optional(),
            "domain": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthorizationAttemptInfoOut"])
    types["OperationMetadataIn"] = t.struct(
        {
            "requestedCancellation": t.boolean().optional(),
            "target": t.string().optional(),
            "endTime": t.string().optional(),
            "statusMessage": t.string().optional(),
            "apiVersion": t.string().optional(),
            "createTime": t.string().optional(),
            "verb": t.string().optional(),
        }
    ).named(renames["OperationMetadataIn"])
    types["OperationMetadataOut"] = t.struct(
        {
            "requestedCancellation": t.boolean().optional(),
            "target": t.string().optional(),
            "endTime": t.string().optional(),
            "statusMessage": t.string().optional(),
            "apiVersion": t.string().optional(),
            "createTime": t.string().optional(),
            "verb": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["StatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["CertificateIssuanceConfigIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "certificateAuthorityConfig": t.proxy(
                renames["CertificateAuthorityConfigIn"]
            ),
            "name": t.string().optional(),
            "lifetime": t.string(),
            "keyAlgorithm": t.string(),
            "rotationWindowPercentage": t.integer(),
        }
    ).named(renames["CertificateIssuanceConfigIn"])
    types["CertificateIssuanceConfigOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "description": t.string().optional(),
            "certificateAuthorityConfig": t.proxy(
                renames["CertificateAuthorityConfigOut"]
            ),
            "name": t.string().optional(),
            "lifetime": t.string(),
            "keyAlgorithm": t.string(),
            "rotationWindowPercentage": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateIssuanceConfigOut"])
    types["CertificateMapIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["CertificateMapIn"])
    types["CertificateMapOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "gclbTargets": t.array(t.proxy(renames["GclbTargetOut"])).optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateMapOut"])
    types["ProvisioningIssueIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ProvisioningIssueIn"]
    )
    types["ProvisioningIssueOut"] = t.struct(
        {
            "details": t.string().optional(),
            "reason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProvisioningIssueOut"])
    types["CertificateAuthorityServiceConfigIn"] = t.struct(
        {"caPool": t.string()}
    ).named(renames["CertificateAuthorityServiceConfigIn"])
    types["CertificateAuthorityServiceConfigOut"] = t.struct(
        {"caPool": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CertificateAuthorityServiceConfigOut"])
    types["ListTrustConfigsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "trustConfigs": t.array(t.proxy(renames["TrustConfigIn"])).optional(),
        }
    ).named(renames["ListTrustConfigsResponseIn"])
    types["ListTrustConfigsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "trustConfigs": t.array(t.proxy(renames["TrustConfigOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTrustConfigsResponseOut"])
    types["TrustConfigIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "trustStores": t.array(t.proxy(renames["TrustStoreIn"])).optional(),
        }
    ).named(renames["TrustConfigIn"])
    types["TrustConfigOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "trustStores": t.array(t.proxy(renames["TrustStoreOut"])).optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrustConfigOut"])
    types["ManagedCertificateIn"] = t.struct(
        {
            "dnsAuthorizations": t.array(t.string()).optional(),
            "domains": t.array(t.string()).optional(),
            "issuanceConfig": t.string().optional(),
        }
    ).named(renames["ManagedCertificateIn"])
    types["ManagedCertificateOut"] = t.struct(
        {
            "dnsAuthorizations": t.array(t.string()).optional(),
            "authorizationAttemptInfo": t.array(
                t.proxy(renames["AuthorizationAttemptInfoOut"])
            ).optional(),
            "state": t.string().optional(),
            "domains": t.array(t.string()).optional(),
            "provisioningIssue": t.proxy(renames["ProvisioningIssueOut"]).optional(),
            "issuanceConfig": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedCertificateOut"])
    types["OperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationOut"])
    types["CertificateIn"] = t.struct(
        {
            "scope": t.string().optional(),
            "selfManaged": t.proxy(renames["SelfManagedCertificateIn"]).optional(),
            "managed": t.proxy(renames["ManagedCertificateIn"]).optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["CertificateIn"])
    types["CertificateOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "pemCertificate": t.string().optional(),
            "sanDnsnames": t.array(t.string()).optional(),
            "expireTime": t.string().optional(),
            "scope": t.string().optional(),
            "updateTime": t.string().optional(),
            "selfManaged": t.proxy(renames["SelfManagedCertificateOut"]).optional(),
            "managed": t.proxy(renames["ManagedCertificateOut"]).optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateOut"])
    types["TrustAnchorIn"] = t.struct({"pemCertificate": t.string().optional()}).named(
        renames["TrustAnchorIn"]
    )
    types["TrustAnchorOut"] = t.struct(
        {
            "pemCertificate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrustAnchorOut"])
    types["DnsAuthorizationIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "domain": t.string(),
        }
    ).named(renames["DnsAuthorizationIn"])
    types["DnsAuthorizationOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "dnsResourceRecord": t.proxy(renames["DnsResourceRecordOut"]).optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "domain": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DnsAuthorizationOut"])
    types["ListCertificateMapsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "certificateMaps": t.array(t.proxy(renames["CertificateMapIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListCertificateMapsResponseIn"])
    types["ListCertificateMapsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "certificateMaps": t.array(
                t.proxy(renames["CertificateMapOut"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCertificateMapsResponseOut"])
    types["TrustStoreIn"] = t.struct(
        {
            "intermediateCas": t.array(t.proxy(renames["IntermediateCAIn"])).optional(),
            "trustAnchors": t.array(t.proxy(renames["TrustAnchorIn"])).optional(),
        }
    ).named(renames["TrustStoreIn"])
    types["TrustStoreOut"] = t.struct(
        {
            "intermediateCas": t.array(
                t.proxy(renames["IntermediateCAOut"])
            ).optional(),
            "trustAnchors": t.array(t.proxy(renames["TrustAnchorOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrustStoreOut"])
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
    types["DnsResourceRecordIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DnsResourceRecordIn"]
    )
    types["DnsResourceRecordOut"] = t.struct(
        {
            "data": t.string().optional(),
            "type": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DnsResourceRecordOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
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
    types["LocationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["GclbTargetIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GclbTargetIn"]
    )
    types["GclbTargetOut"] = t.struct(
        {
            "targetSslProxy": t.string().optional(),
            "ipConfigs": t.array(t.proxy(renames["IpConfigOut"])).optional(),
            "targetHttpsProxy": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GclbTargetOut"])

    functions = {}
    functions["projectsLocationsList"] = certificatemanager.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = certificatemanager.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCertificateIssuanceConfigsList"
    ] = certificatemanager.post(
        "v1/{parent}/certificateIssuanceConfigs",
        t.struct(
            {
                "parent": t.string(),
                "certificateIssuanceConfigId": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "certificateAuthorityConfig": t.proxy(
                    renames["CertificateAuthorityConfigIn"]
                ),
                "name": t.string().optional(),
                "lifetime": t.string(),
                "keyAlgorithm": t.string(),
                "rotationWindowPercentage": t.integer(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCertificateIssuanceConfigsGet"
    ] = certificatemanager.post(
        "v1/{parent}/certificateIssuanceConfigs",
        t.struct(
            {
                "parent": t.string(),
                "certificateIssuanceConfigId": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "certificateAuthorityConfig": t.proxy(
                    renames["CertificateAuthorityConfigIn"]
                ),
                "name": t.string().optional(),
                "lifetime": t.string(),
                "keyAlgorithm": t.string(),
                "rotationWindowPercentage": t.integer(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCertificateIssuanceConfigsDelete"
    ] = certificatemanager.post(
        "v1/{parent}/certificateIssuanceConfigs",
        t.struct(
            {
                "parent": t.string(),
                "certificateIssuanceConfigId": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "certificateAuthorityConfig": t.proxy(
                    renames["CertificateAuthorityConfigIn"]
                ),
                "name": t.string().optional(),
                "lifetime": t.string(),
                "keyAlgorithm": t.string(),
                "rotationWindowPercentage": t.integer(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCertificateIssuanceConfigsCreate"
    ] = certificatemanager.post(
        "v1/{parent}/certificateIssuanceConfigs",
        t.struct(
            {
                "parent": t.string(),
                "certificateIssuanceConfigId": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "certificateAuthorityConfig": t.proxy(
                    renames["CertificateAuthorityConfigIn"]
                ),
                "name": t.string().optional(),
                "lifetime": t.string(),
                "keyAlgorithm": t.string(),
                "rotationWindowPercentage": t.integer(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = certificatemanager.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = certificatemanager.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = certificatemanager.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = certificatemanager.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDnsAuthorizationsDelete"] = certificatemanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["DnsAuthorizationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDnsAuthorizationsPatch"] = certificatemanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["DnsAuthorizationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDnsAuthorizationsCreate"] = certificatemanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["DnsAuthorizationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDnsAuthorizationsList"] = certificatemanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["DnsAuthorizationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDnsAuthorizationsGet"] = certificatemanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["DnsAuthorizationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTrustConfigsList"] = certificatemanager.post(
        "v1/{parent}/trustConfigs",
        t.struct(
            {
                "trustConfigId": t.string(),
                "parent": t.string(),
                "etag": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "trustStores": t.array(t.proxy(renames["TrustStoreIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTrustConfigsGet"] = certificatemanager.post(
        "v1/{parent}/trustConfigs",
        t.struct(
            {
                "trustConfigId": t.string(),
                "parent": t.string(),
                "etag": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "trustStores": t.array(t.proxy(renames["TrustStoreIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTrustConfigsDelete"] = certificatemanager.post(
        "v1/{parent}/trustConfigs",
        t.struct(
            {
                "trustConfigId": t.string(),
                "parent": t.string(),
                "etag": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "trustStores": t.array(t.proxy(renames["TrustStoreIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTrustConfigsPatch"] = certificatemanager.post(
        "v1/{parent}/trustConfigs",
        t.struct(
            {
                "trustConfigId": t.string(),
                "parent": t.string(),
                "etag": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "trustStores": t.array(t.proxy(renames["TrustStoreIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTrustConfigsCreate"] = certificatemanager.post(
        "v1/{parent}/trustConfigs",
        t.struct(
            {
                "trustConfigId": t.string(),
                "parent": t.string(),
                "etag": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "trustStores": t.array(t.proxy(renames["TrustStoreIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCertificateMapsDelete"] = certificatemanager.post(
        "v1/{parent}/certificateMaps",
        t.struct(
            {
                "certificateMapId": t.string(),
                "parent": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCertificateMapsPatch"] = certificatemanager.post(
        "v1/{parent}/certificateMaps",
        t.struct(
            {
                "certificateMapId": t.string(),
                "parent": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCertificateMapsList"] = certificatemanager.post(
        "v1/{parent}/certificateMaps",
        t.struct(
            {
                "certificateMapId": t.string(),
                "parent": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCertificateMapsGet"] = certificatemanager.post(
        "v1/{parent}/certificateMaps",
        t.struct(
            {
                "certificateMapId": t.string(),
                "parent": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCertificateMapsCreate"] = certificatemanager.post(
        "v1/{parent}/certificateMaps",
        t.struct(
            {
                "certificateMapId": t.string(),
                "parent": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCertificateMapsCertificateMapEntriesDelete"
    ] = certificatemanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CertificateMapEntryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCertificateMapsCertificateMapEntriesCreate"
    ] = certificatemanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CertificateMapEntryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCertificateMapsCertificateMapEntriesList"
    ] = certificatemanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CertificateMapEntryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCertificateMapsCertificateMapEntriesPatch"
    ] = certificatemanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CertificateMapEntryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCertificateMapsCertificateMapEntriesGet"
    ] = certificatemanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CertificateMapEntryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCertificatesList"] = certificatemanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CertificateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCertificatesCreate"] = certificatemanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CertificateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCertificatesPatch"] = certificatemanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CertificateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCertificatesDelete"] = certificatemanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CertificateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCertificatesGet"] = certificatemanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CertificateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="certificatemanager",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
