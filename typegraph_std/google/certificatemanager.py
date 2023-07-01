from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_certificatemanager():
    certificatemanager = HTTPRuntime("https://certificatemanager.googleapis.com/")

    renames = {
        "ErrorResponse": "_certificatemanager_1_ErrorResponse",
        "GclbTargetIn": "_certificatemanager_2_GclbTargetIn",
        "GclbTargetOut": "_certificatemanager_3_GclbTargetOut",
        "IpConfigIn": "_certificatemanager_4_IpConfigIn",
        "IpConfigOut": "_certificatemanager_5_IpConfigOut",
        "ProvisioningIssueIn": "_certificatemanager_6_ProvisioningIssueIn",
        "ProvisioningIssueOut": "_certificatemanager_7_ProvisioningIssueOut",
        "ListTrustConfigsResponseIn": "_certificatemanager_8_ListTrustConfigsResponseIn",
        "ListTrustConfigsResponseOut": "_certificatemanager_9_ListTrustConfigsResponseOut",
        "OperationMetadataIn": "_certificatemanager_10_OperationMetadataIn",
        "OperationMetadataOut": "_certificatemanager_11_OperationMetadataOut",
        "ListDnsAuthorizationsResponseIn": "_certificatemanager_12_ListDnsAuthorizationsResponseIn",
        "ListDnsAuthorizationsResponseOut": "_certificatemanager_13_ListDnsAuthorizationsResponseOut",
        "CertificateMapIn": "_certificatemanager_14_CertificateMapIn",
        "CertificateMapOut": "_certificatemanager_15_CertificateMapOut",
        "LocationIn": "_certificatemanager_16_LocationIn",
        "LocationOut": "_certificatemanager_17_LocationOut",
        "ListCertificateMapsResponseIn": "_certificatemanager_18_ListCertificateMapsResponseIn",
        "ListCertificateMapsResponseOut": "_certificatemanager_19_ListCertificateMapsResponseOut",
        "ListOperationsResponseIn": "_certificatemanager_20_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_certificatemanager_21_ListOperationsResponseOut",
        "CancelOperationRequestIn": "_certificatemanager_22_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_certificatemanager_23_CancelOperationRequestOut",
        "StatusIn": "_certificatemanager_24_StatusIn",
        "StatusOut": "_certificatemanager_25_StatusOut",
        "ListLocationsResponseIn": "_certificatemanager_26_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_certificatemanager_27_ListLocationsResponseOut",
        "CertificateMapEntryIn": "_certificatemanager_28_CertificateMapEntryIn",
        "CertificateMapEntryOut": "_certificatemanager_29_CertificateMapEntryOut",
        "IntermediateCAIn": "_certificatemanager_30_IntermediateCAIn",
        "IntermediateCAOut": "_certificatemanager_31_IntermediateCAOut",
        "SelfManagedCertificateIn": "_certificatemanager_32_SelfManagedCertificateIn",
        "SelfManagedCertificateOut": "_certificatemanager_33_SelfManagedCertificateOut",
        "DnsAuthorizationIn": "_certificatemanager_34_DnsAuthorizationIn",
        "DnsAuthorizationOut": "_certificatemanager_35_DnsAuthorizationOut",
        "ListCertificatesResponseIn": "_certificatemanager_36_ListCertificatesResponseIn",
        "ListCertificatesResponseOut": "_certificatemanager_37_ListCertificatesResponseOut",
        "AuthorizationAttemptInfoIn": "_certificatemanager_38_AuthorizationAttemptInfoIn",
        "AuthorizationAttemptInfoOut": "_certificatemanager_39_AuthorizationAttemptInfoOut",
        "TrustStoreIn": "_certificatemanager_40_TrustStoreIn",
        "TrustStoreOut": "_certificatemanager_41_TrustStoreOut",
        "TrustConfigIn": "_certificatemanager_42_TrustConfigIn",
        "TrustConfigOut": "_certificatemanager_43_TrustConfigOut",
        "CertificateAuthorityConfigIn": "_certificatemanager_44_CertificateAuthorityConfigIn",
        "CertificateAuthorityConfigOut": "_certificatemanager_45_CertificateAuthorityConfigOut",
        "ListCertificateIssuanceConfigsResponseIn": "_certificatemanager_46_ListCertificateIssuanceConfigsResponseIn",
        "ListCertificateIssuanceConfigsResponseOut": "_certificatemanager_47_ListCertificateIssuanceConfigsResponseOut",
        "ListCertificateMapEntriesResponseIn": "_certificatemanager_48_ListCertificateMapEntriesResponseIn",
        "ListCertificateMapEntriesResponseOut": "_certificatemanager_49_ListCertificateMapEntriesResponseOut",
        "DnsResourceRecordIn": "_certificatemanager_50_DnsResourceRecordIn",
        "DnsResourceRecordOut": "_certificatemanager_51_DnsResourceRecordOut",
        "TrustAnchorIn": "_certificatemanager_52_TrustAnchorIn",
        "TrustAnchorOut": "_certificatemanager_53_TrustAnchorOut",
        "CertificateAuthorityServiceConfigIn": "_certificatemanager_54_CertificateAuthorityServiceConfigIn",
        "CertificateAuthorityServiceConfigOut": "_certificatemanager_55_CertificateAuthorityServiceConfigOut",
        "CertificateIn": "_certificatemanager_56_CertificateIn",
        "CertificateOut": "_certificatemanager_57_CertificateOut",
        "CertificateIssuanceConfigIn": "_certificatemanager_58_CertificateIssuanceConfigIn",
        "CertificateIssuanceConfigOut": "_certificatemanager_59_CertificateIssuanceConfigOut",
        "OperationIn": "_certificatemanager_60_OperationIn",
        "OperationOut": "_certificatemanager_61_OperationOut",
        "ManagedCertificateIn": "_certificatemanager_62_ManagedCertificateIn",
        "ManagedCertificateOut": "_certificatemanager_63_ManagedCertificateOut",
        "EmptyIn": "_certificatemanager_64_EmptyIn",
        "EmptyOut": "_certificatemanager_65_EmptyOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GclbTargetIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GclbTargetIn"]
    )
    types["GclbTargetOut"] = t.struct(
        {
            "targetHttpsProxy": t.string().optional(),
            "ipConfigs": t.array(t.proxy(renames["IpConfigOut"])).optional(),
            "targetSslProxy": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GclbTargetOut"])
    types["IpConfigIn"] = t.struct({"_": t.string().optional()}).named(
        renames["IpConfigIn"]
    )
    types["IpConfigOut"] = t.struct(
        {
            "ports": t.array(t.integer()).optional(),
            "ipAddress": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IpConfigOut"])
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
    types["OperationMetadataIn"] = t.struct(
        {
            "requestedCancellation": t.boolean().optional(),
            "verb": t.string().optional(),
            "apiVersion": t.string().optional(),
            "target": t.string().optional(),
            "statusMessage": t.string().optional(),
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["OperationMetadataIn"])
    types["OperationMetadataOut"] = t.struct(
        {
            "requestedCancellation": t.boolean().optional(),
            "verb": t.string().optional(),
            "apiVersion": t.string().optional(),
            "target": t.string().optional(),
            "statusMessage": t.string().optional(),
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
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
    types["CertificateMapIn"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["CertificateMapIn"])
    types["CertificateMapOut"] = t.struct(
        {
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "gclbTargets": t.array(t.proxy(renames["GclbTargetOut"])).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateMapOut"])
    types["LocationIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
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
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["StatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
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
    types["CertificateMapEntryIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "hostname": t.string().optional(),
            "name": t.string().optional(),
            "matcher": t.string().optional(),
            "certificates": t.array(t.string()).optional(),
        }
    ).named(renames["CertificateMapEntryIn"])
    types["CertificateMapEntryOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "hostname": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "matcher": t.string().optional(),
            "state": t.string().optional(),
            "certificates": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateMapEntryOut"])
    types["IntermediateCAIn"] = t.struct(
        {"pemCertificate": t.string().optional()}
    ).named(renames["IntermediateCAIn"])
    types["IntermediateCAOut"] = t.struct(
        {
            "pemCertificate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntermediateCAOut"])
    types["SelfManagedCertificateIn"] = t.struct(
        {
            "pemPrivateKey": t.string().optional(),
            "pemCertificate": t.string().optional(),
        }
    ).named(renames["SelfManagedCertificateIn"])
    types["SelfManagedCertificateOut"] = t.struct(
        {
            "pemPrivateKey": t.string().optional(),
            "pemCertificate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SelfManagedCertificateOut"])
    types["DnsAuthorizationIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "domain": t.string(),
        }
    ).named(renames["DnsAuthorizationIn"])
    types["DnsAuthorizationOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "description": t.string().optional(),
            "updateTime": t.string().optional(),
            "dnsResourceRecord": t.proxy(renames["DnsResourceRecordOut"]).optional(),
            "domain": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DnsAuthorizationOut"])
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
    types["AuthorizationAttemptInfoIn"] = t.struct(
        {"domain": t.string().optional()}
    ).named(renames["AuthorizationAttemptInfoIn"])
    types["AuthorizationAttemptInfoOut"] = t.struct(
        {
            "details": t.string().optional(),
            "state": t.string().optional(),
            "domain": t.string().optional(),
            "failureReason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthorizationAttemptInfoOut"])
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
    types["TrustConfigIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "etag": t.string().optional(),
            "trustStores": t.array(t.proxy(renames["TrustStoreIn"])).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["TrustConfigIn"])
    types["TrustConfigOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "etag": t.string().optional(),
            "updateTime": t.string().optional(),
            "trustStores": t.array(t.proxy(renames["TrustStoreOut"])).optional(),
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrustConfigOut"])
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
    types["ListCertificateMapEntriesResponseIn"] = t.struct(
        {
            "certificateMapEntries": t.array(
                t.proxy(renames["CertificateMapEntryIn"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListCertificateMapEntriesResponseIn"])
    types["ListCertificateMapEntriesResponseOut"] = t.struct(
        {
            "certificateMapEntries": t.array(
                t.proxy(renames["CertificateMapEntryOut"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCertificateMapEntriesResponseOut"])
    types["DnsResourceRecordIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DnsResourceRecordIn"]
    )
    types["DnsResourceRecordOut"] = t.struct(
        {
            "type": t.string().optional(),
            "data": t.string().optional(),
            "name": t.string().optional(),
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
    types["CertificateAuthorityServiceConfigIn"] = t.struct(
        {"caPool": t.string()}
    ).named(renames["CertificateAuthorityServiceConfigIn"])
    types["CertificateAuthorityServiceConfigOut"] = t.struct(
        {"caPool": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CertificateAuthorityServiceConfigOut"])
    types["CertificateIn"] = t.struct(
        {
            "managed": t.proxy(renames["ManagedCertificateIn"]).optional(),
            "scope": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "selfManaged": t.proxy(renames["SelfManagedCertificateIn"]).optional(),
        }
    ).named(renames["CertificateIn"])
    types["CertificateOut"] = t.struct(
        {
            "sanDnsnames": t.array(t.string()).optional(),
            "pemCertificate": t.string().optional(),
            "managed": t.proxy(renames["ManagedCertificateOut"]).optional(),
            "scope": t.string().optional(),
            "updateTime": t.string().optional(),
            "description": t.string().optional(),
            "expireTime": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "selfManaged": t.proxy(renames["SelfManagedCertificateOut"]).optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateOut"])
    types["CertificateIssuanceConfigIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "lifetime": t.string(),
            "certificateAuthorityConfig": t.proxy(
                renames["CertificateAuthorityConfigIn"]
            ),
            "rotationWindowPercentage": t.integer(),
            "keyAlgorithm": t.string(),
            "description": t.string().optional(),
        }
    ).named(renames["CertificateIssuanceConfigIn"])
    types["CertificateIssuanceConfigOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "lifetime": t.string(),
            "updateTime": t.string().optional(),
            "certificateAuthorityConfig": t.proxy(
                renames["CertificateAuthorityConfigOut"]
            ),
            "rotationWindowPercentage": t.integer(),
            "keyAlgorithm": t.string(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateIssuanceConfigOut"])
    types["OperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationOut"])
    types["ManagedCertificateIn"] = t.struct(
        {
            "dnsAuthorizations": t.array(t.string()).optional(),
            "domains": t.array(t.string()).optional(),
            "issuanceConfig": t.string().optional(),
        }
    ).named(renames["ManagedCertificateIn"])
    types["ManagedCertificateOut"] = t.struct(
        {
            "authorizationAttemptInfo": t.array(
                t.proxy(renames["AuthorizationAttemptInfoOut"])
            ).optional(),
            "dnsAuthorizations": t.array(t.string()).optional(),
            "domains": t.array(t.string()).optional(),
            "provisioningIssue": t.proxy(renames["ProvisioningIssueOut"]).optional(),
            "issuanceConfig": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedCertificateOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])

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
    functions["projectsLocationsOperationsList"] = certificatemanager.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = certificatemanager.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = certificatemanager.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = certificatemanager.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTrustConfigsList"] = certificatemanager.post(
        "v1/{parent}/trustConfigs",
        t.struct(
            {
                "trustConfigId": t.string(),
                "parent": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "etag": t.string().optional(),
                "trustStores": t.array(t.proxy(renames["TrustStoreIn"])).optional(),
                "description": t.string().optional(),
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
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "etag": t.string().optional(),
                "trustStores": t.array(t.proxy(renames["TrustStoreIn"])).optional(),
                "description": t.string().optional(),
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
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "etag": t.string().optional(),
                "trustStores": t.array(t.proxy(renames["TrustStoreIn"])).optional(),
                "description": t.string().optional(),
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
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "etag": t.string().optional(),
                "trustStores": t.array(t.proxy(renames["TrustStoreIn"])).optional(),
                "description": t.string().optional(),
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
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "etag": t.string().optional(),
                "trustStores": t.array(t.proxy(renames["TrustStoreIn"])).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCertificateIssuanceConfigsDelete"
    ] = certificatemanager.get(
        "v1/{parent}/certificateIssuanceConfigs",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCertificateIssuanceConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCertificateIssuanceConfigsCreate"
    ] = certificatemanager.get(
        "v1/{parent}/certificateIssuanceConfigs",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCertificateIssuanceConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCertificateIssuanceConfigsGet"
    ] = certificatemanager.get(
        "v1/{parent}/certificateIssuanceConfigs",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCertificateIssuanceConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCertificateIssuanceConfigsList"
    ] = certificatemanager.get(
        "v1/{parent}/certificateIssuanceConfigs",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCertificateIssuanceConfigsResponseOut"]),
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
        "projectsLocationsCertificateMapsCertificateMapEntriesGet"
    ] = certificatemanager.get(
        "v1/{parent}/certificateMapEntries",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCertificateMapEntriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDnsAuthorizationsDelete"] = certificatemanager.post(
        "v1/{parent}/dnsAuthorizations",
        t.struct(
            {
                "dnsAuthorizationId": t.string(),
                "parent": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "domain": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDnsAuthorizationsGet"] = certificatemanager.post(
        "v1/{parent}/dnsAuthorizations",
        t.struct(
            {
                "dnsAuthorizationId": t.string(),
                "parent": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "domain": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDnsAuthorizationsList"] = certificatemanager.post(
        "v1/{parent}/dnsAuthorizations",
        t.struct(
            {
                "dnsAuthorizationId": t.string(),
                "parent": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "domain": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDnsAuthorizationsPatch"] = certificatemanager.post(
        "v1/{parent}/dnsAuthorizations",
        t.struct(
            {
                "dnsAuthorizationId": t.string(),
                "parent": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "domain": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDnsAuthorizationsCreate"] = certificatemanager.post(
        "v1/{parent}/dnsAuthorizations",
        t.struct(
            {
                "dnsAuthorizationId": t.string(),
                "parent": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "domain": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCertificatesGet"] = certificatemanager.get(
        "v1/{parent}/certificates",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCertificatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCertificatesPatch"] = certificatemanager.get(
        "v1/{parent}/certificates",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCertificatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCertificatesDelete"] = certificatemanager.get(
        "v1/{parent}/certificates",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCertificatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCertificatesCreate"] = certificatemanager.get(
        "v1/{parent}/certificates",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCertificatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCertificatesList"] = certificatemanager.get(
        "v1/{parent}/certificates",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCertificatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="certificatemanager",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
