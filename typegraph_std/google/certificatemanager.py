from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_certificatemanager() -> Import:
    certificatemanager = HTTPRuntime("https://certificatemanager.googleapis.com/")

    renames = {
        "ErrorResponse": "_certificatemanager_1_ErrorResponse",
        "CertificateIssuanceConfigIn": "_certificatemanager_2_CertificateIssuanceConfigIn",
        "CertificateIssuanceConfigOut": "_certificatemanager_3_CertificateIssuanceConfigOut",
        "CertificateAuthorityConfigIn": "_certificatemanager_4_CertificateAuthorityConfigIn",
        "CertificateAuthorityConfigOut": "_certificatemanager_5_CertificateAuthorityConfigOut",
        "ListCertificatesResponseIn": "_certificatemanager_6_ListCertificatesResponseIn",
        "ListCertificatesResponseOut": "_certificatemanager_7_ListCertificatesResponseOut",
        "CertificateAuthorityServiceConfigIn": "_certificatemanager_8_CertificateAuthorityServiceConfigIn",
        "CertificateAuthorityServiceConfigOut": "_certificatemanager_9_CertificateAuthorityServiceConfigOut",
        "StatusIn": "_certificatemanager_10_StatusIn",
        "StatusOut": "_certificatemanager_11_StatusOut",
        "EmptyIn": "_certificatemanager_12_EmptyIn",
        "EmptyOut": "_certificatemanager_13_EmptyOut",
        "ListCertificateMapsResponseIn": "_certificatemanager_14_ListCertificateMapsResponseIn",
        "ListCertificateMapsResponseOut": "_certificatemanager_15_ListCertificateMapsResponseOut",
        "CertificateMapIn": "_certificatemanager_16_CertificateMapIn",
        "CertificateMapOut": "_certificatemanager_17_CertificateMapOut",
        "CertificateIn": "_certificatemanager_18_CertificateIn",
        "CertificateOut": "_certificatemanager_19_CertificateOut",
        "ListTrustConfigsResponseIn": "_certificatemanager_20_ListTrustConfigsResponseIn",
        "ListTrustConfigsResponseOut": "_certificatemanager_21_ListTrustConfigsResponseOut",
        "ManagedCertificateIn": "_certificatemanager_22_ManagedCertificateIn",
        "ManagedCertificateOut": "_certificatemanager_23_ManagedCertificateOut",
        "ListCertificateIssuanceConfigsResponseIn": "_certificatemanager_24_ListCertificateIssuanceConfigsResponseIn",
        "ListCertificateIssuanceConfigsResponseOut": "_certificatemanager_25_ListCertificateIssuanceConfigsResponseOut",
        "CancelOperationRequestIn": "_certificatemanager_26_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_certificatemanager_27_CancelOperationRequestOut",
        "OperationIn": "_certificatemanager_28_OperationIn",
        "OperationOut": "_certificatemanager_29_OperationOut",
        "TrustAnchorIn": "_certificatemanager_30_TrustAnchorIn",
        "TrustAnchorOut": "_certificatemanager_31_TrustAnchorOut",
        "ListOperationsResponseIn": "_certificatemanager_32_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_certificatemanager_33_ListOperationsResponseOut",
        "IpConfigIn": "_certificatemanager_34_IpConfigIn",
        "IpConfigOut": "_certificatemanager_35_IpConfigOut",
        "SelfManagedCertificateIn": "_certificatemanager_36_SelfManagedCertificateIn",
        "SelfManagedCertificateOut": "_certificatemanager_37_SelfManagedCertificateOut",
        "CertificateMapEntryIn": "_certificatemanager_38_CertificateMapEntryIn",
        "CertificateMapEntryOut": "_certificatemanager_39_CertificateMapEntryOut",
        "AuthorizationAttemptInfoIn": "_certificatemanager_40_AuthorizationAttemptInfoIn",
        "AuthorizationAttemptInfoOut": "_certificatemanager_41_AuthorizationAttemptInfoOut",
        "ListLocationsResponseIn": "_certificatemanager_42_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_certificatemanager_43_ListLocationsResponseOut",
        "DnsAuthorizationIn": "_certificatemanager_44_DnsAuthorizationIn",
        "DnsAuthorizationOut": "_certificatemanager_45_DnsAuthorizationOut",
        "OperationMetadataIn": "_certificatemanager_46_OperationMetadataIn",
        "OperationMetadataOut": "_certificatemanager_47_OperationMetadataOut",
        "DnsResourceRecordIn": "_certificatemanager_48_DnsResourceRecordIn",
        "DnsResourceRecordOut": "_certificatemanager_49_DnsResourceRecordOut",
        "ListDnsAuthorizationsResponseIn": "_certificatemanager_50_ListDnsAuthorizationsResponseIn",
        "ListDnsAuthorizationsResponseOut": "_certificatemanager_51_ListDnsAuthorizationsResponseOut",
        "GclbTargetIn": "_certificatemanager_52_GclbTargetIn",
        "GclbTargetOut": "_certificatemanager_53_GclbTargetOut",
        "IntermediateCAIn": "_certificatemanager_54_IntermediateCAIn",
        "IntermediateCAOut": "_certificatemanager_55_IntermediateCAOut",
        "ListCertificateMapEntriesResponseIn": "_certificatemanager_56_ListCertificateMapEntriesResponseIn",
        "ListCertificateMapEntriesResponseOut": "_certificatemanager_57_ListCertificateMapEntriesResponseOut",
        "TrustConfigIn": "_certificatemanager_58_TrustConfigIn",
        "TrustConfigOut": "_certificatemanager_59_TrustConfigOut",
        "TrustStoreIn": "_certificatemanager_60_TrustStoreIn",
        "TrustStoreOut": "_certificatemanager_61_TrustStoreOut",
        "LocationIn": "_certificatemanager_62_LocationIn",
        "LocationOut": "_certificatemanager_63_LocationOut",
        "ProvisioningIssueIn": "_certificatemanager_64_ProvisioningIssueIn",
        "ProvisioningIssueOut": "_certificatemanager_65_ProvisioningIssueOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["CertificateIssuanceConfigIn"] = t.struct(
        {
            "description": t.string().optional(),
            "certificateAuthorityConfig": t.proxy(
                renames["CertificateAuthorityConfigIn"]
            ),
            "name": t.string().optional(),
            "rotationWindowPercentage": t.integer(),
            "keyAlgorithm": t.string(),
            "lifetime": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["CertificateIssuanceConfigIn"])
    types["CertificateIssuanceConfigOut"] = t.struct(
        {
            "description": t.string().optional(),
            "certificateAuthorityConfig": t.proxy(
                renames["CertificateAuthorityConfigOut"]
            ),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "rotationWindowPercentage": t.integer(),
            "keyAlgorithm": t.string(),
            "lifetime": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateIssuanceConfigOut"])
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
    types["ListCertificatesResponseIn"] = t.struct(
        {
            "certificates": t.array(t.proxy(renames["CertificateIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListCertificatesResponseIn"])
    types["ListCertificatesResponseOut"] = t.struct(
        {
            "certificates": t.array(t.proxy(renames["CertificateOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCertificatesResponseOut"])
    types["CertificateAuthorityServiceConfigIn"] = t.struct(
        {"caPool": t.string()}
    ).named(renames["CertificateAuthorityServiceConfigIn"])
    types["CertificateAuthorityServiceConfigOut"] = t.struct(
        {"caPool": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CertificateAuthorityServiceConfigOut"])
    types["StatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ListCertificateMapsResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "certificateMaps": t.array(t.proxy(renames["CertificateMapIn"])).optional(),
        }
    ).named(renames["ListCertificateMapsResponseIn"])
    types["ListCertificateMapsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "certificateMaps": t.array(
                t.proxy(renames["CertificateMapOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCertificateMapsResponseOut"])
    types["CertificateMapIn"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["CertificateMapIn"])
    types["CertificateMapOut"] = t.struct(
        {
            "gclbTargets": t.array(t.proxy(renames["GclbTargetOut"])).optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateMapOut"])
    types["CertificateIn"] = t.struct(
        {
            "name": t.string().optional(),
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "scope": t.string().optional(),
            "managed": t.proxy(renames["ManagedCertificateIn"]).optional(),
            "selfManaged": t.proxy(renames["SelfManagedCertificateIn"]).optional(),
        }
    ).named(renames["CertificateIn"])
    types["CertificateOut"] = t.struct(
        {
            "name": t.string().optional(),
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "pemCertificate": t.string().optional(),
            "scope": t.string().optional(),
            "sanDnsnames": t.array(t.string()).optional(),
            "managed": t.proxy(renames["ManagedCertificateOut"]).optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "selfManaged": t.proxy(renames["SelfManagedCertificateOut"]).optional(),
            "expireTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateOut"])
    types["ListTrustConfigsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "trustConfigs": t.array(t.proxy(renames["TrustConfigIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListTrustConfigsResponseIn"])
    types["ListTrustConfigsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "trustConfigs": t.array(t.proxy(renames["TrustConfigOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTrustConfigsResponseOut"])
    types["ManagedCertificateIn"] = t.struct(
        {
            "issuanceConfig": t.string().optional(),
            "dnsAuthorizations": t.array(t.string()).optional(),
            "domains": t.array(t.string()).optional(),
        }
    ).named(renames["ManagedCertificateIn"])
    types["ManagedCertificateOut"] = t.struct(
        {
            "issuanceConfig": t.string().optional(),
            "dnsAuthorizations": t.array(t.string()).optional(),
            "domains": t.array(t.string()).optional(),
            "provisioningIssue": t.proxy(renames["ProvisioningIssueOut"]).optional(),
            "state": t.string().optional(),
            "authorizationAttemptInfo": t.array(
                t.proxy(renames["AuthorizationAttemptInfoOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedCertificateOut"])
    types["ListCertificateIssuanceConfigsResponseIn"] = t.struct(
        {
            "certificateIssuanceConfigs": t.array(
                t.proxy(renames["CertificateIssuanceConfigIn"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListCertificateIssuanceConfigsResponseIn"])
    types["ListCertificateIssuanceConfigsResponseOut"] = t.struct(
        {
            "certificateIssuanceConfigs": t.array(
                t.proxy(renames["CertificateIssuanceConfigOut"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCertificateIssuanceConfigsResponseOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["OperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
    types["TrustAnchorIn"] = t.struct({"pemCertificate": t.string().optional()}).named(
        renames["TrustAnchorIn"]
    )
    types["TrustAnchorOut"] = t.struct(
        {
            "pemCertificate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrustAnchorOut"])
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
    types["CertificateMapEntryIn"] = t.struct(
        {
            "certificates": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "hostname": t.string().optional(),
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "matcher": t.string().optional(),
        }
    ).named(renames["CertificateMapEntryIn"])
    types["CertificateMapEntryOut"] = t.struct(
        {
            "certificates": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "hostname": t.string().optional(),
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "matcher": t.string().optional(),
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateMapEntryOut"])
    types["AuthorizationAttemptInfoIn"] = t.struct(
        {"domain": t.string().optional()}
    ).named(renames["AuthorizationAttemptInfoIn"])
    types["AuthorizationAttemptInfoOut"] = t.struct(
        {
            "failureReason": t.string().optional(),
            "details": t.string().optional(),
            "state": t.string().optional(),
            "domain": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthorizationAttemptInfoOut"])
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
    types["DnsAuthorizationIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "domain": t.string(),
            "name": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["DnsAuthorizationIn"])
    types["DnsAuthorizationOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "domain": t.string(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "description": t.string().optional(),
            "updateTime": t.string().optional(),
            "dnsResourceRecord": t.proxy(renames["DnsResourceRecordOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DnsAuthorizationOut"])
    types["OperationMetadataIn"] = t.struct(
        {
            "target": t.string().optional(),
            "createTime": t.string().optional(),
            "verb": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "endTime": t.string().optional(),
            "statusMessage": t.string().optional(),
            "apiVersion": t.string().optional(),
        }
    ).named(renames["OperationMetadataIn"])
    types["OperationMetadataOut"] = t.struct(
        {
            "target": t.string().optional(),
            "createTime": t.string().optional(),
            "verb": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "endTime": t.string().optional(),
            "statusMessage": t.string().optional(),
            "apiVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["DnsResourceRecordIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DnsResourceRecordIn"]
    )
    types["DnsResourceRecordOut"] = t.struct(
        {
            "name": t.string().optional(),
            "type": t.string().optional(),
            "data": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DnsResourceRecordOut"])
    types["ListDnsAuthorizationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "dnsAuthorizations": t.array(
                t.proxy(renames["DnsAuthorizationIn"])
            ).optional(),
        }
    ).named(renames["ListDnsAuthorizationsResponseIn"])
    types["ListDnsAuthorizationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "dnsAuthorizations": t.array(
                t.proxy(renames["DnsAuthorizationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDnsAuthorizationsResponseOut"])
    types["GclbTargetIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GclbTargetIn"]
    )
    types["GclbTargetOut"] = t.struct(
        {
            "ipConfigs": t.array(t.proxy(renames["IpConfigOut"])).optional(),
            "targetHttpsProxy": t.string().optional(),
            "targetSslProxy": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GclbTargetOut"])
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
            "unreachable": t.array(t.string()).optional(),
            "certificateMapEntries": t.array(
                t.proxy(renames["CertificateMapEntryIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListCertificateMapEntriesResponseIn"])
    types["ListCertificateMapEntriesResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "certificateMapEntries": t.array(
                t.proxy(renames["CertificateMapEntryOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCertificateMapEntriesResponseOut"])
    types["TrustConfigIn"] = t.struct(
        {
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "etag": t.string().optional(),
            "trustStores": t.array(t.proxy(renames["TrustStoreIn"])).optional(),
        }
    ).named(renames["TrustConfigIn"])
    types["TrustConfigOut"] = t.struct(
        {
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "etag": t.string().optional(),
            "trustStores": t.array(t.proxy(renames["TrustStoreOut"])).optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrustConfigOut"])
    types["TrustStoreIn"] = t.struct(
        {
            "trustAnchors": t.array(t.proxy(renames["TrustAnchorIn"])).optional(),
            "intermediateCas": t.array(t.proxy(renames["IntermediateCAIn"])).optional(),
        }
    ).named(renames["TrustStoreIn"])
    types["TrustStoreOut"] = t.struct(
        {
            "trustAnchors": t.array(t.proxy(renames["TrustAnchorOut"])).optional(),
            "intermediateCas": t.array(
                t.proxy(renames["IntermediateCAOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrustStoreOut"])
    types["LocationIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
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
    functions["projectsLocationsOperationsList"] = certificatemanager.post(
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
    functions["projectsLocationsOperationsGet"] = certificatemanager.post(
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
    functions["projectsLocationsOperationsDelete"] = certificatemanager.post(
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
    functions["projectsLocationsOperationsCancel"] = certificatemanager.post(
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
    functions["projectsLocationsCertificatesList"] = certificatemanager.post(
        "v1/{parent}/certificates",
        t.struct(
            {
                "parent": t.string(),
                "certificateId": t.string(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "scope": t.string().optional(),
                "managed": t.proxy(renames["ManagedCertificateIn"]).optional(),
                "selfManaged": t.proxy(renames["SelfManagedCertificateIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCertificatesPatch"] = certificatemanager.post(
        "v1/{parent}/certificates",
        t.struct(
            {
                "parent": t.string(),
                "certificateId": t.string(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "scope": t.string().optional(),
                "managed": t.proxy(renames["ManagedCertificateIn"]).optional(),
                "selfManaged": t.proxy(renames["SelfManagedCertificateIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCertificatesGet"] = certificatemanager.post(
        "v1/{parent}/certificates",
        t.struct(
            {
                "parent": t.string(),
                "certificateId": t.string(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "scope": t.string().optional(),
                "managed": t.proxy(renames["ManagedCertificateIn"]).optional(),
                "selfManaged": t.proxy(renames["SelfManagedCertificateIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCertificatesDelete"] = certificatemanager.post(
        "v1/{parent}/certificates",
        t.struct(
            {
                "parent": t.string(),
                "certificateId": t.string(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "scope": t.string().optional(),
                "managed": t.proxy(renames["ManagedCertificateIn"]).optional(),
                "selfManaged": t.proxy(renames["SelfManagedCertificateIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCertificatesCreate"] = certificatemanager.post(
        "v1/{parent}/certificates",
        t.struct(
            {
                "parent": t.string(),
                "certificateId": t.string(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "scope": t.string().optional(),
                "managed": t.proxy(renames["ManagedCertificateIn"]).optional(),
                "selfManaged": t.proxy(renames["SelfManagedCertificateIn"]).optional(),
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
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
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
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
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
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
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
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
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
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCertificateMapsCertificateMapEntriesPatch"
    ] = certificatemanager.post(
        "v1/{parent}/certificateMapEntries",
        t.struct(
            {
                "certificateMapEntryId": t.string(),
                "parent": t.string(),
                "certificates": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "hostname": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "matcher": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCertificateMapsCertificateMapEntriesList"
    ] = certificatemanager.post(
        "v1/{parent}/certificateMapEntries",
        t.struct(
            {
                "certificateMapEntryId": t.string(),
                "parent": t.string(),
                "certificates": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "hostname": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "matcher": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCertificateMapsCertificateMapEntriesDelete"
    ] = certificatemanager.post(
        "v1/{parent}/certificateMapEntries",
        t.struct(
            {
                "certificateMapEntryId": t.string(),
                "parent": t.string(),
                "certificates": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "hostname": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "matcher": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCertificateMapsCertificateMapEntriesGet"
    ] = certificatemanager.post(
        "v1/{parent}/certificateMapEntries",
        t.struct(
            {
                "certificateMapEntryId": t.string(),
                "parent": t.string(),
                "certificates": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "hostname": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "matcher": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCertificateMapsCertificateMapEntriesCreate"
    ] = certificatemanager.post(
        "v1/{parent}/certificateMapEntries",
        t.struct(
            {
                "certificateMapEntryId": t.string(),
                "parent": t.string(),
                "certificates": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "hostname": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "matcher": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDnsAuthorizationsCreate"] = certificatemanager.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "domain": t.string(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDnsAuthorizationsList"] = certificatemanager.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "domain": t.string(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDnsAuthorizationsDelete"] = certificatemanager.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "domain": t.string(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDnsAuthorizationsGet"] = certificatemanager.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "domain": t.string(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDnsAuthorizationsPatch"] = certificatemanager.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "domain": t.string(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCertificateIssuanceConfigsCreate"
    ] = certificatemanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CertificateIssuanceConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCertificateIssuanceConfigsList"
    ] = certificatemanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CertificateIssuanceConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCertificateIssuanceConfigsDelete"
    ] = certificatemanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CertificateIssuanceConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCertificateIssuanceConfigsGet"
    ] = certificatemanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CertificateIssuanceConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTrustConfigsDelete"] = certificatemanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TrustConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTrustConfigsList"] = certificatemanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TrustConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTrustConfigsPatch"] = certificatemanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TrustConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTrustConfigsCreate"] = certificatemanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TrustConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTrustConfigsGet"] = certificatemanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TrustConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="certificatemanager", renames=renames, types=types, functions=functions
    )
