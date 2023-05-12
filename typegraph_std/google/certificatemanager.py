from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_certificatemanager() -> Import:
    certificatemanager = HTTPRuntime("https://certificatemanager.googleapis.com/")

    renames = {
        "ErrorResponse": "_certificatemanager_1_ErrorResponse",
        "ListCertificateMapsResponseIn": "_certificatemanager_2_ListCertificateMapsResponseIn",
        "ListCertificateMapsResponseOut": "_certificatemanager_3_ListCertificateMapsResponseOut",
        "LocationIn": "_certificatemanager_4_LocationIn",
        "LocationOut": "_certificatemanager_5_LocationOut",
        "OperationMetadataIn": "_certificatemanager_6_OperationMetadataIn",
        "OperationMetadataOut": "_certificatemanager_7_OperationMetadataOut",
        "CertificateIssuanceConfigIn": "_certificatemanager_8_CertificateIssuanceConfigIn",
        "CertificateIssuanceConfigOut": "_certificatemanager_9_CertificateIssuanceConfigOut",
        "ListCertificateIssuanceConfigsResponseIn": "_certificatemanager_10_ListCertificateIssuanceConfigsResponseIn",
        "ListCertificateIssuanceConfigsResponseOut": "_certificatemanager_11_ListCertificateIssuanceConfigsResponseOut",
        "OperationIn": "_certificatemanager_12_OperationIn",
        "OperationOut": "_certificatemanager_13_OperationOut",
        "EmptyIn": "_certificatemanager_14_EmptyIn",
        "EmptyOut": "_certificatemanager_15_EmptyOut",
        "CertificateMapIn": "_certificatemanager_16_CertificateMapIn",
        "CertificateMapOut": "_certificatemanager_17_CertificateMapOut",
        "ListOperationsResponseIn": "_certificatemanager_18_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_certificatemanager_19_ListOperationsResponseOut",
        "SelfManagedCertificateIn": "_certificatemanager_20_SelfManagedCertificateIn",
        "SelfManagedCertificateOut": "_certificatemanager_21_SelfManagedCertificateOut",
        "StatusIn": "_certificatemanager_22_StatusIn",
        "StatusOut": "_certificatemanager_23_StatusOut",
        "CertificateAuthorityConfigIn": "_certificatemanager_24_CertificateAuthorityConfigIn",
        "CertificateAuthorityConfigOut": "_certificatemanager_25_CertificateAuthorityConfigOut",
        "CancelOperationRequestIn": "_certificatemanager_26_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_certificatemanager_27_CancelOperationRequestOut",
        "IpConfigIn": "_certificatemanager_28_IpConfigIn",
        "IpConfigOut": "_certificatemanager_29_IpConfigOut",
        "ListLocationsResponseIn": "_certificatemanager_30_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_certificatemanager_31_ListLocationsResponseOut",
        "AuthorizationAttemptInfoIn": "_certificatemanager_32_AuthorizationAttemptInfoIn",
        "AuthorizationAttemptInfoOut": "_certificatemanager_33_AuthorizationAttemptInfoOut",
        "ManagedCertificateIn": "_certificatemanager_34_ManagedCertificateIn",
        "ManagedCertificateOut": "_certificatemanager_35_ManagedCertificateOut",
        "ProvisioningIssueIn": "_certificatemanager_36_ProvisioningIssueIn",
        "ProvisioningIssueOut": "_certificatemanager_37_ProvisioningIssueOut",
        "CertificateAuthorityServiceConfigIn": "_certificatemanager_38_CertificateAuthorityServiceConfigIn",
        "CertificateAuthorityServiceConfigOut": "_certificatemanager_39_CertificateAuthorityServiceConfigOut",
        "TrustStoreIn": "_certificatemanager_40_TrustStoreIn",
        "TrustStoreOut": "_certificatemanager_41_TrustStoreOut",
        "DnsAuthorizationIn": "_certificatemanager_42_DnsAuthorizationIn",
        "DnsAuthorizationOut": "_certificatemanager_43_DnsAuthorizationOut",
        "CertificateIn": "_certificatemanager_44_CertificateIn",
        "CertificateOut": "_certificatemanager_45_CertificateOut",
        "DnsResourceRecordIn": "_certificatemanager_46_DnsResourceRecordIn",
        "DnsResourceRecordOut": "_certificatemanager_47_DnsResourceRecordOut",
        "TrustAnchorIn": "_certificatemanager_48_TrustAnchorIn",
        "TrustAnchorOut": "_certificatemanager_49_TrustAnchorOut",
        "ListCertificateMapEntriesResponseIn": "_certificatemanager_50_ListCertificateMapEntriesResponseIn",
        "ListCertificateMapEntriesResponseOut": "_certificatemanager_51_ListCertificateMapEntriesResponseOut",
        "ListCertificatesResponseIn": "_certificatemanager_52_ListCertificatesResponseIn",
        "ListCertificatesResponseOut": "_certificatemanager_53_ListCertificatesResponseOut",
        "CertificateMapEntryIn": "_certificatemanager_54_CertificateMapEntryIn",
        "CertificateMapEntryOut": "_certificatemanager_55_CertificateMapEntryOut",
        "ListTrustConfigsResponseIn": "_certificatemanager_56_ListTrustConfigsResponseIn",
        "ListTrustConfigsResponseOut": "_certificatemanager_57_ListTrustConfigsResponseOut",
        "TrustConfigIn": "_certificatemanager_58_TrustConfigIn",
        "TrustConfigOut": "_certificatemanager_59_TrustConfigOut",
        "IntermediateCAIn": "_certificatemanager_60_IntermediateCAIn",
        "IntermediateCAOut": "_certificatemanager_61_IntermediateCAOut",
        "GclbTargetIn": "_certificatemanager_62_GclbTargetIn",
        "GclbTargetOut": "_certificatemanager_63_GclbTargetOut",
        "ListDnsAuthorizationsResponseIn": "_certificatemanager_64_ListDnsAuthorizationsResponseIn",
        "ListDnsAuthorizationsResponseOut": "_certificatemanager_65_ListDnsAuthorizationsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ListCertificateMapsResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "certificateMaps": t.array(t.proxy(renames["CertificateMapIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListCertificateMapsResponseIn"])
    types["ListCertificateMapsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "certificateMaps": t.array(
                t.proxy(renames["CertificateMapOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCertificateMapsResponseOut"])
    types["LocationIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["OperationMetadataIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "endTime": t.string().optional(),
            "statusMessage": t.string().optional(),
            "verb": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "target": t.string().optional(),
        }
    ).named(renames["OperationMetadataIn"])
    types["OperationMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "endTime": t.string().optional(),
            "statusMessage": t.string().optional(),
            "verb": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "target": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["CertificateIssuanceConfigIn"] = t.struct(
        {
            "keyAlgorithm": t.string(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "rotationWindowPercentage": t.integer(),
            "description": t.string().optional(),
            "lifetime": t.string(),
            "certificateAuthorityConfig": t.proxy(
                renames["CertificateAuthorityConfigIn"]
            ),
        }
    ).named(renames["CertificateIssuanceConfigIn"])
    types["CertificateIssuanceConfigOut"] = t.struct(
        {
            "keyAlgorithm": t.string(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "rotationWindowPercentage": t.integer(),
            "description": t.string().optional(),
            "lifetime": t.string(),
            "certificateAuthorityConfig": t.proxy(
                renames["CertificateAuthorityConfigOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateIssuanceConfigOut"])
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
    types["OperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["CertificateMapIn"] = t.struct(
        {
            "description": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["CertificateMapIn"])
    types["CertificateMapOut"] = t.struct(
        {
            "description": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "gclbTargets": t.array(t.proxy(renames["GclbTargetOut"])).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateMapOut"])
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
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
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
    types["AuthorizationAttemptInfoIn"] = t.struct(
        {"domain": t.string().optional()}
    ).named(renames["AuthorizationAttemptInfoIn"])
    types["AuthorizationAttemptInfoOut"] = t.struct(
        {
            "state": t.string().optional(),
            "failureReason": t.string().optional(),
            "domain": t.string().optional(),
            "details": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthorizationAttemptInfoOut"])
    types["ManagedCertificateIn"] = t.struct(
        {
            "domains": t.array(t.string()).optional(),
            "dnsAuthorizations": t.array(t.string()).optional(),
            "issuanceConfig": t.string().optional(),
        }
    ).named(renames["ManagedCertificateIn"])
    types["ManagedCertificateOut"] = t.struct(
        {
            "provisioningIssue": t.proxy(renames["ProvisioningIssueOut"]).optional(),
            "state": t.string().optional(),
            "domains": t.array(t.string()).optional(),
            "dnsAuthorizations": t.array(t.string()).optional(),
            "issuanceConfig": t.string().optional(),
            "authorizationAttemptInfo": t.array(
                t.proxy(renames["AuthorizationAttemptInfoOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedCertificateOut"])
    types["ProvisioningIssueIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ProvisioningIssueIn"]
    )
    types["ProvisioningIssueOut"] = t.struct(
        {
            "reason": t.string().optional(),
            "details": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProvisioningIssueOut"])
    types["CertificateAuthorityServiceConfigIn"] = t.struct(
        {"caPool": t.string()}
    ).named(renames["CertificateAuthorityServiceConfigIn"])
    types["CertificateAuthorityServiceConfigOut"] = t.struct(
        {"caPool": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CertificateAuthorityServiceConfigOut"])
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
    types["DnsAuthorizationIn"] = t.struct(
        {
            "description": t.string().optional(),
            "name": t.string().optional(),
            "domain": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["DnsAuthorizationIn"])
    types["DnsAuthorizationOut"] = t.struct(
        {
            "description": t.string().optional(),
            "name": t.string().optional(),
            "domain": t.string(),
            "dnsResourceRecord": t.proxy(renames["DnsResourceRecordOut"]).optional(),
            "updateTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DnsAuthorizationOut"])
    types["CertificateIn"] = t.struct(
        {
            "selfManaged": t.proxy(renames["SelfManagedCertificateIn"]).optional(),
            "description": t.string().optional(),
            "managed": t.proxy(renames["ManagedCertificateIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "scope": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["CertificateIn"])
    types["CertificateOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "selfManaged": t.proxy(renames["SelfManagedCertificateOut"]).optional(),
            "description": t.string().optional(),
            "managed": t.proxy(renames["ManagedCertificateOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "scope": t.string().optional(),
            "sanDnsnames": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "expireTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "pemCertificate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateOut"])
    types["DnsResourceRecordIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DnsResourceRecordIn"]
    )
    types["DnsResourceRecordOut"] = t.struct(
        {
            "type": t.string().optional(),
            "name": t.string().optional(),
            "data": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DnsResourceRecordOut"])
    types["TrustAnchorIn"] = t.struct({"pemCertificate": t.string().optional()}).named(
        renames["TrustAnchorIn"]
    )
    types["TrustAnchorOut"] = t.struct(
        {
            "pemCertificate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrustAnchorOut"])
    types["ListCertificateMapEntriesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "certificateMapEntries": t.array(
                t.proxy(renames["CertificateMapEntryIn"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListCertificateMapEntriesResponseIn"])
    types["ListCertificateMapEntriesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "certificateMapEntries": t.array(
                t.proxy(renames["CertificateMapEntryOut"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCertificateMapEntriesResponseOut"])
    types["ListCertificatesResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "certificates": t.array(t.proxy(renames["CertificateIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListCertificatesResponseIn"])
    types["ListCertificatesResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "certificates": t.array(t.proxy(renames["CertificateOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCertificatesResponseOut"])
    types["CertificateMapEntryIn"] = t.struct(
        {
            "name": t.string().optional(),
            "hostname": t.string().optional(),
            "description": t.string().optional(),
            "certificates": t.array(t.string()).optional(),
            "matcher": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["CertificateMapEntryIn"])
    types["CertificateMapEntryOut"] = t.struct(
        {
            "name": t.string().optional(),
            "hostname": t.string().optional(),
            "description": t.string().optional(),
            "certificates": t.array(t.string()).optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "matcher": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateMapEntryOut"])
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
    types["TrustConfigIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "trustStores": t.array(t.proxy(renames["TrustStoreIn"])).optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["TrustConfigIn"])
    types["TrustConfigOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "etag": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "trustStores": t.array(t.proxy(renames["TrustStoreOut"])).optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrustConfigOut"])
    types["IntermediateCAIn"] = t.struct(
        {"pemCertificate": t.string().optional()}
    ).named(renames["IntermediateCAIn"])
    types["IntermediateCAOut"] = t.struct(
        {
            "pemCertificate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntermediateCAOut"])
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
    types["ListDnsAuthorizationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "dnsAuthorizations": t.array(
                t.proxy(renames["DnsAuthorizationIn"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListDnsAuthorizationsResponseIn"])
    types["ListDnsAuthorizationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "dnsAuthorizations": t.array(
                t.proxy(renames["DnsAuthorizationOut"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDnsAuthorizationsResponseOut"])

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
    functions["projectsLocationsTrustConfigsDelete"] = certificatemanager.get(
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
    functions["projectsLocationsDnsAuthorizationsDelete"] = certificatemanager.get(
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
    functions["projectsLocationsDnsAuthorizationsCreate"] = certificatemanager.get(
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
    functions["projectsLocationsDnsAuthorizationsGet"] = certificatemanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["DnsAuthorizationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCertificateMapsCreate"] = certificatemanager.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCertificateMapsGet"] = certificatemanager.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCertificateMapsList"] = certificatemanager.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCertificateMapsDelete"] = certificatemanager.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCertificateMapsPatch"] = certificatemanager.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCertificateMapsCertificateMapEntriesGet"
    ] = certificatemanager.get(
        "v1/{parent}/certificateMapEntries",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCertificateMapEntriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCertificateMapsCertificateMapEntriesCreate"
    ] = certificatemanager.get(
        "v1/{parent}/certificateMapEntries",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCertificateMapEntriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCertificateMapsCertificateMapEntriesDelete"
    ] = certificatemanager.get(
        "v1/{parent}/certificateMapEntries",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCertificateMapEntriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCertificateMapsCertificateMapEntriesPatch"
    ] = certificatemanager.get(
        "v1/{parent}/certificateMapEntries",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCertificateMapEntriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCertificateMapsCertificateMapEntriesList"
    ] = certificatemanager.get(
        "v1/{parent}/certificateMapEntries",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCertificateMapEntriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCertificatesPatch"] = certificatemanager.post(
        "v1/{parent}/certificates",
        t.struct(
            {
                "certificateId": t.string(),
                "parent": t.string(),
                "selfManaged": t.proxy(renames["SelfManagedCertificateIn"]).optional(),
                "description": t.string().optional(),
                "managed": t.proxy(renames["ManagedCertificateIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "scope": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCertificatesList"] = certificatemanager.post(
        "v1/{parent}/certificates",
        t.struct(
            {
                "certificateId": t.string(),
                "parent": t.string(),
                "selfManaged": t.proxy(renames["SelfManagedCertificateIn"]).optional(),
                "description": t.string().optional(),
                "managed": t.proxy(renames["ManagedCertificateIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "scope": t.string().optional(),
                "name": t.string().optional(),
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
                "certificateId": t.string(),
                "parent": t.string(),
                "selfManaged": t.proxy(renames["SelfManagedCertificateIn"]).optional(),
                "description": t.string().optional(),
                "managed": t.proxy(renames["ManagedCertificateIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "scope": t.string().optional(),
                "name": t.string().optional(),
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
                "certificateId": t.string(),
                "parent": t.string(),
                "selfManaged": t.proxy(renames["SelfManagedCertificateIn"]).optional(),
                "description": t.string().optional(),
                "managed": t.proxy(renames["ManagedCertificateIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "scope": t.string().optional(),
                "name": t.string().optional(),
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
                "certificateId": t.string(),
                "parent": t.string(),
                "selfManaged": t.proxy(renames["SelfManagedCertificateIn"]).optional(),
                "description": t.string().optional(),
                "managed": t.proxy(renames["ManagedCertificateIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "scope": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="certificatemanager",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
