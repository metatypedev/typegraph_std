from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_dns() -> Import:
    dns = HTTPRuntime("https://dns.googleapis.com/")

    renames = {
        "ErrorResponse": "_dns_1_ErrorResponse",
        "ChangeIn": "_dns_2_ChangeIn",
        "ChangeOut": "_dns_3_ChangeOut",
        "RRSetRoutingPolicyWrrPolicyIn": "_dns_4_RRSetRoutingPolicyWrrPolicyIn",
        "RRSetRoutingPolicyWrrPolicyOut": "_dns_5_RRSetRoutingPolicyWrrPolicyOut",
        "ResponsePolicyRuleIn": "_dns_6_ResponsePolicyRuleIn",
        "ResponsePolicyRuleOut": "_dns_7_ResponsePolicyRuleOut",
        "ResourceRecordSetsDeleteResponseIn": "_dns_8_ResourceRecordSetsDeleteResponseIn",
        "ResourceRecordSetsDeleteResponseOut": "_dns_9_ResourceRecordSetsDeleteResponseOut",
        "DnsKeySpecIn": "_dns_10_DnsKeySpecIn",
        "DnsKeySpecOut": "_dns_11_DnsKeySpecOut",
        "ManagedZoneOperationsListResponseIn": "_dns_12_ManagedZoneOperationsListResponseIn",
        "ManagedZoneOperationsListResponseOut": "_dns_13_ManagedZoneOperationsListResponseOut",
        "GoogleIamV1TestIamPermissionsResponseIn": "_dns_14_GoogleIamV1TestIamPermissionsResponseIn",
        "GoogleIamV1TestIamPermissionsResponseOut": "_dns_15_GoogleIamV1TestIamPermissionsResponseOut",
        "DnsKeyIn": "_dns_16_DnsKeyIn",
        "DnsKeyOut": "_dns_17_DnsKeyOut",
        "ManagedZoneForwardingConfigIn": "_dns_18_ManagedZoneForwardingConfigIn",
        "ManagedZoneForwardingConfigOut": "_dns_19_ManagedZoneForwardingConfigOut",
        "PoliciesListResponseIn": "_dns_20_PoliciesListResponseIn",
        "PoliciesListResponseOut": "_dns_21_PoliciesListResponseOut",
        "ManagedZonesListResponseIn": "_dns_22_ManagedZonesListResponseIn",
        "ManagedZonesListResponseOut": "_dns_23_ManagedZonesListResponseOut",
        "ManagedZoneCloudLoggingConfigIn": "_dns_24_ManagedZoneCloudLoggingConfigIn",
        "ManagedZoneCloudLoggingConfigOut": "_dns_25_ManagedZoneCloudLoggingConfigOut",
        "ResponsePolicyRulesPatchResponseIn": "_dns_26_ResponsePolicyRulesPatchResponseIn",
        "ResponsePolicyRulesPatchResponseOut": "_dns_27_ResponsePolicyRulesPatchResponseOut",
        "ManagedZoneServiceDirectoryConfigNamespaceIn": "_dns_28_ManagedZoneServiceDirectoryConfigNamespaceIn",
        "ManagedZoneServiceDirectoryConfigNamespaceOut": "_dns_29_ManagedZoneServiceDirectoryConfigNamespaceOut",
        "ManagedZonePeeringConfigIn": "_dns_30_ManagedZonePeeringConfigIn",
        "ManagedZonePeeringConfigOut": "_dns_31_ManagedZonePeeringConfigOut",
        "ManagedZoneServiceDirectoryConfigIn": "_dns_32_ManagedZoneServiceDirectoryConfigIn",
        "ManagedZoneServiceDirectoryConfigOut": "_dns_33_ManagedZoneServiceDirectoryConfigOut",
        "ResponsePoliciesListResponseIn": "_dns_34_ResponsePoliciesListResponseIn",
        "ResponsePoliciesListResponseOut": "_dns_35_ResponsePoliciesListResponseOut",
        "ResourceRecordSetsListResponseIn": "_dns_36_ResourceRecordSetsListResponseIn",
        "ResourceRecordSetsListResponseOut": "_dns_37_ResourceRecordSetsListResponseOut",
        "GoogleIamV1GetPolicyOptionsIn": "_dns_38_GoogleIamV1GetPolicyOptionsIn",
        "GoogleIamV1GetPolicyOptionsOut": "_dns_39_GoogleIamV1GetPolicyOptionsOut",
        "RRSetRoutingPolicyIn": "_dns_40_RRSetRoutingPolicyIn",
        "RRSetRoutingPolicyOut": "_dns_41_RRSetRoutingPolicyOut",
        "ResponsePolicyNetworkIn": "_dns_42_ResponsePolicyNetworkIn",
        "ResponsePolicyNetworkOut": "_dns_43_ResponsePolicyNetworkOut",
        "PolicyNetworkIn": "_dns_44_PolicyNetworkIn",
        "PolicyNetworkOut": "_dns_45_PolicyNetworkOut",
        "QuotaIn": "_dns_46_QuotaIn",
        "QuotaOut": "_dns_47_QuotaOut",
        "GoogleIamV1AuditLogConfigIn": "_dns_48_GoogleIamV1AuditLogConfigIn",
        "GoogleIamV1AuditLogConfigOut": "_dns_49_GoogleIamV1AuditLogConfigOut",
        "PoliciesPatchResponseIn": "_dns_50_PoliciesPatchResponseIn",
        "PoliciesPatchResponseOut": "_dns_51_PoliciesPatchResponseOut",
        "DnsKeysListResponseIn": "_dns_52_DnsKeysListResponseIn",
        "DnsKeysListResponseOut": "_dns_53_DnsKeysListResponseOut",
        "ManagedZonePeeringConfigTargetNetworkIn": "_dns_54_ManagedZonePeeringConfigTargetNetworkIn",
        "ManagedZonePeeringConfigTargetNetworkOut": "_dns_55_ManagedZonePeeringConfigTargetNetworkOut",
        "RRSetRoutingPolicyLoadBalancerTargetIn": "_dns_56_RRSetRoutingPolicyLoadBalancerTargetIn",
        "RRSetRoutingPolicyLoadBalancerTargetOut": "_dns_57_RRSetRoutingPolicyLoadBalancerTargetOut",
        "GoogleIamV1AuditConfigIn": "_dns_58_GoogleIamV1AuditConfigIn",
        "GoogleIamV1AuditConfigOut": "_dns_59_GoogleIamV1AuditConfigOut",
        "OperationIn": "_dns_60_OperationIn",
        "OperationOut": "_dns_61_OperationOut",
        "RRSetRoutingPolicyGeoPolicyIn": "_dns_62_RRSetRoutingPolicyGeoPolicyIn",
        "RRSetRoutingPolicyGeoPolicyOut": "_dns_63_RRSetRoutingPolicyGeoPolicyOut",
        "GoogleIamV1GetIamPolicyRequestIn": "_dns_64_GoogleIamV1GetIamPolicyRequestIn",
        "GoogleIamV1GetIamPolicyRequestOut": "_dns_65_GoogleIamV1GetIamPolicyRequestOut",
        "OperationManagedZoneContextIn": "_dns_66_OperationManagedZoneContextIn",
        "OperationManagedZoneContextOut": "_dns_67_OperationManagedZoneContextOut",
        "ManagedZoneDnsSecConfigIn": "_dns_68_ManagedZoneDnsSecConfigIn",
        "ManagedZoneDnsSecConfigOut": "_dns_69_ManagedZoneDnsSecConfigOut",
        "ResponsePoliciesUpdateResponseIn": "_dns_70_ResponsePoliciesUpdateResponseIn",
        "ResponsePoliciesUpdateResponseOut": "_dns_71_ResponsePoliciesUpdateResponseOut",
        "ProjectIn": "_dns_72_ProjectIn",
        "ProjectOut": "_dns_73_ProjectOut",
        "RRSetRoutingPolicyHealthCheckTargetsIn": "_dns_74_RRSetRoutingPolicyHealthCheckTargetsIn",
        "RRSetRoutingPolicyHealthCheckTargetsOut": "_dns_75_RRSetRoutingPolicyHealthCheckTargetsOut",
        "ResponsePolicyRulesUpdateResponseIn": "_dns_76_ResponsePolicyRulesUpdateResponseIn",
        "ResponsePolicyRulesUpdateResponseOut": "_dns_77_ResponsePolicyRulesUpdateResponseOut",
        "ResponsePoliciesPatchResponseIn": "_dns_78_ResponsePoliciesPatchResponseIn",
        "ResponsePoliciesPatchResponseOut": "_dns_79_ResponsePoliciesPatchResponseOut",
        "ResourceRecordSetIn": "_dns_80_ResourceRecordSetIn",
        "ResourceRecordSetOut": "_dns_81_ResourceRecordSetOut",
        "PolicyIn": "_dns_82_PolicyIn",
        "PolicyOut": "_dns_83_PolicyOut",
        "GoogleIamV1PolicyIn": "_dns_84_GoogleIamV1PolicyIn",
        "GoogleIamV1PolicyOut": "_dns_85_GoogleIamV1PolicyOut",
        "ManagedZonePrivateVisibilityConfigGKEClusterIn": "_dns_86_ManagedZonePrivateVisibilityConfigGKEClusterIn",
        "ManagedZonePrivateVisibilityConfigGKEClusterOut": "_dns_87_ManagedZonePrivateVisibilityConfigGKEClusterOut",
        "ManagedZoneIn": "_dns_88_ManagedZoneIn",
        "ManagedZoneOut": "_dns_89_ManagedZoneOut",
        "ResponsePolicyIn": "_dns_90_ResponsePolicyIn",
        "ResponsePolicyOut": "_dns_91_ResponsePolicyOut",
        "ManagedZonePrivateVisibilityConfigIn": "_dns_92_ManagedZonePrivateVisibilityConfigIn",
        "ManagedZonePrivateVisibilityConfigOut": "_dns_93_ManagedZonePrivateVisibilityConfigOut",
        "ManagedZonePrivateVisibilityConfigNetworkIn": "_dns_94_ManagedZonePrivateVisibilityConfigNetworkIn",
        "ManagedZonePrivateVisibilityConfigNetworkOut": "_dns_95_ManagedZonePrivateVisibilityConfigNetworkOut",
        "OperationDnsKeyContextIn": "_dns_96_OperationDnsKeyContextIn",
        "OperationDnsKeyContextOut": "_dns_97_OperationDnsKeyContextOut",
        "RRSetRoutingPolicyPrimaryBackupPolicyIn": "_dns_98_RRSetRoutingPolicyPrimaryBackupPolicyIn",
        "RRSetRoutingPolicyPrimaryBackupPolicyOut": "_dns_99_RRSetRoutingPolicyPrimaryBackupPolicyOut",
        "PolicyAlternativeNameServerConfigIn": "_dns_100_PolicyAlternativeNameServerConfigIn",
        "PolicyAlternativeNameServerConfigOut": "_dns_101_PolicyAlternativeNameServerConfigOut",
        "RRSetRoutingPolicyGeoPolicyGeoPolicyItemIn": "_dns_102_RRSetRoutingPolicyGeoPolicyGeoPolicyItemIn",
        "RRSetRoutingPolicyGeoPolicyGeoPolicyItemOut": "_dns_103_RRSetRoutingPolicyGeoPolicyGeoPolicyItemOut",
        "GoogleIamV1TestIamPermissionsRequestIn": "_dns_104_GoogleIamV1TestIamPermissionsRequestIn",
        "GoogleIamV1TestIamPermissionsRequestOut": "_dns_105_GoogleIamV1TestIamPermissionsRequestOut",
        "ManagedZoneForwardingConfigNameServerTargetIn": "_dns_106_ManagedZoneForwardingConfigNameServerTargetIn",
        "ManagedZoneForwardingConfigNameServerTargetOut": "_dns_107_ManagedZoneForwardingConfigNameServerTargetOut",
        "ChangesListResponseIn": "_dns_108_ChangesListResponseIn",
        "ChangesListResponseOut": "_dns_109_ChangesListResponseOut",
        "PoliciesUpdateResponseIn": "_dns_110_PoliciesUpdateResponseIn",
        "PoliciesUpdateResponseOut": "_dns_111_PoliciesUpdateResponseOut",
        "ManagedZoneReverseLookupConfigIn": "_dns_112_ManagedZoneReverseLookupConfigIn",
        "ManagedZoneReverseLookupConfigOut": "_dns_113_ManagedZoneReverseLookupConfigOut",
        "GoogleIamV1BindingIn": "_dns_114_GoogleIamV1BindingIn",
        "GoogleIamV1BindingOut": "_dns_115_GoogleIamV1BindingOut",
        "ResponseHeaderIn": "_dns_116_ResponseHeaderIn",
        "ResponseHeaderOut": "_dns_117_ResponseHeaderOut",
        "ResponsePolicyGKEClusterIn": "_dns_118_ResponsePolicyGKEClusterIn",
        "ResponsePolicyGKEClusterOut": "_dns_119_ResponsePolicyGKEClusterOut",
        "GoogleIamV1SetIamPolicyRequestIn": "_dns_120_GoogleIamV1SetIamPolicyRequestIn",
        "GoogleIamV1SetIamPolicyRequestOut": "_dns_121_GoogleIamV1SetIamPolicyRequestOut",
        "RRSetRoutingPolicyWrrPolicyWrrPolicyItemIn": "_dns_122_RRSetRoutingPolicyWrrPolicyWrrPolicyItemIn",
        "RRSetRoutingPolicyWrrPolicyWrrPolicyItemOut": "_dns_123_RRSetRoutingPolicyWrrPolicyWrrPolicyItemOut",
        "ResponsePolicyRuleLocalDataIn": "_dns_124_ResponsePolicyRuleLocalDataIn",
        "ResponsePolicyRuleLocalDataOut": "_dns_125_ResponsePolicyRuleLocalDataOut",
        "ExprIn": "_dns_126_ExprIn",
        "ExprOut": "_dns_127_ExprOut",
        "ResponsePolicyRulesListResponseIn": "_dns_128_ResponsePolicyRulesListResponseIn",
        "ResponsePolicyRulesListResponseOut": "_dns_129_ResponsePolicyRulesListResponseOut",
        "PolicyAlternativeNameServerConfigTargetNameServerIn": "_dns_130_PolicyAlternativeNameServerConfigTargetNameServerIn",
        "PolicyAlternativeNameServerConfigTargetNameServerOut": "_dns_131_PolicyAlternativeNameServerConfigTargetNameServerOut",
        "DnsKeyDigestIn": "_dns_132_DnsKeyDigestIn",
        "DnsKeyDigestOut": "_dns_133_DnsKeyDigestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ChangeIn"] = t.struct(
        {
            "kind": t.string(),
            "startTime": t.string().optional(),
            "deletions": t.array(t.proxy(renames["ResourceRecordSetIn"])).optional(),
            "status": t.string().optional(),
            "isServing": t.boolean().optional(),
            "id": t.string().optional(),
            "additions": t.array(t.proxy(renames["ResourceRecordSetIn"])).optional(),
        }
    ).named(renames["ChangeIn"])
    types["ChangeOut"] = t.struct(
        {
            "kind": t.string(),
            "startTime": t.string().optional(),
            "deletions": t.array(t.proxy(renames["ResourceRecordSetOut"])).optional(),
            "status": t.string().optional(),
            "isServing": t.boolean().optional(),
            "id": t.string().optional(),
            "additions": t.array(t.proxy(renames["ResourceRecordSetOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChangeOut"])
    types["RRSetRoutingPolicyWrrPolicyIn"] = t.struct(
        {
            "kind": t.string(),
            "items": t.array(
                t.proxy(renames["RRSetRoutingPolicyWrrPolicyWrrPolicyItemIn"])
            ),
        }
    ).named(renames["RRSetRoutingPolicyWrrPolicyIn"])
    types["RRSetRoutingPolicyWrrPolicyOut"] = t.struct(
        {
            "kind": t.string(),
            "items": t.array(
                t.proxy(renames["RRSetRoutingPolicyWrrPolicyWrrPolicyItemOut"])
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RRSetRoutingPolicyWrrPolicyOut"])
    types["ResponsePolicyRuleIn"] = t.struct(
        {
            "kind": t.string(),
            "ruleName": t.string().optional(),
            "behavior": t.string().optional(),
            "localData": t.proxy(renames["ResponsePolicyRuleLocalDataIn"]).optional(),
            "dnsName": t.string().optional(),
        }
    ).named(renames["ResponsePolicyRuleIn"])
    types["ResponsePolicyRuleOut"] = t.struct(
        {
            "kind": t.string(),
            "ruleName": t.string().optional(),
            "behavior": t.string().optional(),
            "localData": t.proxy(renames["ResponsePolicyRuleLocalDataOut"]).optional(),
            "dnsName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResponsePolicyRuleOut"])
    types["ResourceRecordSetsDeleteResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ResourceRecordSetsDeleteResponseIn"])
    types["ResourceRecordSetsDeleteResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ResourceRecordSetsDeleteResponseOut"])
    types["DnsKeySpecIn"] = t.struct(
        {
            "keyLength": t.integer().optional(),
            "keyType": t.string().optional(),
            "kind": t.string(),
            "algorithm": t.string().optional(),
        }
    ).named(renames["DnsKeySpecIn"])
    types["DnsKeySpecOut"] = t.struct(
        {
            "keyLength": t.integer().optional(),
            "keyType": t.string().optional(),
            "kind": t.string(),
            "algorithm": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DnsKeySpecOut"])
    types["ManagedZoneOperationsListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "header": t.proxy(renames["ResponseHeaderIn"]),
            "operations": t.array(t.proxy(renames["OperationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ManagedZoneOperationsListResponseIn"])
    types["ManagedZoneOperationsListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "header": t.proxy(renames["ResponseHeaderOut"]),
            "operations": t.array(t.proxy(renames["OperationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedZoneOperationsListResponseOut"])
    types["GoogleIamV1TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["GoogleIamV1TestIamPermissionsResponseIn"])
    types["GoogleIamV1TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1TestIamPermissionsResponseOut"])
    types["DnsKeyIn"] = t.struct(
        {
            "id": t.string().optional(),
            "keyLength": t.integer().optional(),
            "kind": t.string(),
            "description": t.string().optional(),
            "isActive": t.boolean().optional(),
            "algorithm": t.string().optional(),
            "creationTime": t.string().optional(),
            "type": t.string().optional(),
            "publicKey": t.string().optional(),
            "keyTag": t.integer().optional(),
            "digests": t.array(t.proxy(renames["DnsKeyDigestIn"])).optional(),
        }
    ).named(renames["DnsKeyIn"])
    types["DnsKeyOut"] = t.struct(
        {
            "id": t.string().optional(),
            "keyLength": t.integer().optional(),
            "kind": t.string(),
            "description": t.string().optional(),
            "isActive": t.boolean().optional(),
            "algorithm": t.string().optional(),
            "creationTime": t.string().optional(),
            "type": t.string().optional(),
            "publicKey": t.string().optional(),
            "keyTag": t.integer().optional(),
            "digests": t.array(t.proxy(renames["DnsKeyDigestOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DnsKeyOut"])
    types["ManagedZoneForwardingConfigIn"] = t.struct(
        {
            "targetNameServers": t.array(
                t.proxy(renames["ManagedZoneForwardingConfigNameServerTargetIn"])
            ).optional(),
            "kind": t.string(),
        }
    ).named(renames["ManagedZoneForwardingConfigIn"])
    types["ManagedZoneForwardingConfigOut"] = t.struct(
        {
            "targetNameServers": t.array(
                t.proxy(renames["ManagedZoneForwardingConfigNameServerTargetOut"])
            ).optional(),
            "kind": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedZoneForwardingConfigOut"])
    types["PoliciesListResponseIn"] = t.struct(
        {
            "policies": t.array(t.proxy(renames["PolicyIn"])).optional(),
            "header": t.proxy(renames["ResponseHeaderIn"]),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["PoliciesListResponseIn"])
    types["PoliciesListResponseOut"] = t.struct(
        {
            "policies": t.array(t.proxy(renames["PolicyOut"])).optional(),
            "header": t.proxy(renames["ResponseHeaderOut"]),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PoliciesListResponseOut"])
    types["ManagedZonesListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "managedZones": t.array(t.proxy(renames["ManagedZoneIn"])).optional(),
            "header": t.proxy(renames["ResponseHeaderIn"]),
            "kind": t.string().optional(),
        }
    ).named(renames["ManagedZonesListResponseIn"])
    types["ManagedZonesListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "managedZones": t.array(t.proxy(renames["ManagedZoneOut"])).optional(),
            "header": t.proxy(renames["ResponseHeaderOut"]),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedZonesListResponseOut"])
    types["ManagedZoneCloudLoggingConfigIn"] = t.struct(
        {"kind": t.string(), "enableLogging": t.boolean().optional()}
    ).named(renames["ManagedZoneCloudLoggingConfigIn"])
    types["ManagedZoneCloudLoggingConfigOut"] = t.struct(
        {
            "kind": t.string(),
            "enableLogging": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedZoneCloudLoggingConfigOut"])
    types["ResponsePolicyRulesPatchResponseIn"] = t.struct(
        {
            "header": t.proxy(renames["ResponseHeaderIn"]),
            "responsePolicyRule": t.proxy(renames["ResponsePolicyRuleIn"]),
        }
    ).named(renames["ResponsePolicyRulesPatchResponseIn"])
    types["ResponsePolicyRulesPatchResponseOut"] = t.struct(
        {
            "header": t.proxy(renames["ResponseHeaderOut"]),
            "responsePolicyRule": t.proxy(renames["ResponsePolicyRuleOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResponsePolicyRulesPatchResponseOut"])
    types["ManagedZoneServiceDirectoryConfigNamespaceIn"] = t.struct(
        {
            "kind": t.string(),
            "deletionTime": t.string().optional(),
            "namespaceUrl": t.string().optional(),
        }
    ).named(renames["ManagedZoneServiceDirectoryConfigNamespaceIn"])
    types["ManagedZoneServiceDirectoryConfigNamespaceOut"] = t.struct(
        {
            "kind": t.string(),
            "deletionTime": t.string().optional(),
            "namespaceUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedZoneServiceDirectoryConfigNamespaceOut"])
    types["ManagedZonePeeringConfigIn"] = t.struct(
        {
            "targetNetwork": t.proxy(
                renames["ManagedZonePeeringConfigTargetNetworkIn"]
            ).optional(),
            "kind": t.string(),
        }
    ).named(renames["ManagedZonePeeringConfigIn"])
    types["ManagedZonePeeringConfigOut"] = t.struct(
        {
            "targetNetwork": t.proxy(
                renames["ManagedZonePeeringConfigTargetNetworkOut"]
            ).optional(),
            "kind": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedZonePeeringConfigOut"])
    types["ManagedZoneServiceDirectoryConfigIn"] = t.struct(
        {
            "kind": t.string(),
            "namespace": t.proxy(
                renames["ManagedZoneServiceDirectoryConfigNamespaceIn"]
            ).optional(),
        }
    ).named(renames["ManagedZoneServiceDirectoryConfigIn"])
    types["ManagedZoneServiceDirectoryConfigOut"] = t.struct(
        {
            "kind": t.string(),
            "namespace": t.proxy(
                renames["ManagedZoneServiceDirectoryConfigNamespaceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedZoneServiceDirectoryConfigOut"])
    types["ResponsePoliciesListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "responsePolicies": t.array(
                t.proxy(renames["ResponsePolicyIn"])
            ).optional(),
            "header": t.proxy(renames["ResponseHeaderIn"]),
        }
    ).named(renames["ResponsePoliciesListResponseIn"])
    types["ResponsePoliciesListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "responsePolicies": t.array(
                t.proxy(renames["ResponsePolicyOut"])
            ).optional(),
            "header": t.proxy(renames["ResponseHeaderOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResponsePoliciesListResponseOut"])
    types["ResourceRecordSetsListResponseIn"] = t.struct(
        {
            "header": t.proxy(renames["ResponseHeaderIn"]),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "rrsets": t.array(t.proxy(renames["ResourceRecordSetIn"])).optional(),
        }
    ).named(renames["ResourceRecordSetsListResponseIn"])
    types["ResourceRecordSetsListResponseOut"] = t.struct(
        {
            "header": t.proxy(renames["ResponseHeaderOut"]),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "rrsets": t.array(t.proxy(renames["ResourceRecordSetOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceRecordSetsListResponseOut"])
    types["GoogleIamV1GetPolicyOptionsIn"] = t.struct(
        {"requestedPolicyVersion": t.integer().optional()}
    ).named(renames["GoogleIamV1GetPolicyOptionsIn"])
    types["GoogleIamV1GetPolicyOptionsOut"] = t.struct(
        {
            "requestedPolicyVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1GetPolicyOptionsOut"])
    types["RRSetRoutingPolicyIn"] = t.struct(
        {
            "geo": t.proxy(renames["RRSetRoutingPolicyGeoPolicyIn"]),
            "primaryBackup": t.proxy(
                renames["RRSetRoutingPolicyPrimaryBackupPolicyIn"]
            ),
            "wrr": t.proxy(renames["RRSetRoutingPolicyWrrPolicyIn"]),
            "kind": t.string(),
        }
    ).named(renames["RRSetRoutingPolicyIn"])
    types["RRSetRoutingPolicyOut"] = t.struct(
        {
            "geo": t.proxy(renames["RRSetRoutingPolicyGeoPolicyOut"]),
            "primaryBackup": t.proxy(
                renames["RRSetRoutingPolicyPrimaryBackupPolicyOut"]
            ),
            "wrr": t.proxy(renames["RRSetRoutingPolicyWrrPolicyOut"]),
            "kind": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RRSetRoutingPolicyOut"])
    types["ResponsePolicyNetworkIn"] = t.struct(
        {"kind": t.string(), "networkUrl": t.string().optional()}
    ).named(renames["ResponsePolicyNetworkIn"])
    types["ResponsePolicyNetworkOut"] = t.struct(
        {
            "kind": t.string(),
            "networkUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResponsePolicyNetworkOut"])
    types["PolicyNetworkIn"] = t.struct(
        {"networkUrl": t.string().optional(), "kind": t.string()}
    ).named(renames["PolicyNetworkIn"])
    types["PolicyNetworkOut"] = t.struct(
        {
            "networkUrl": t.string().optional(),
            "kind": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyNetworkOut"])
    types["QuotaIn"] = t.struct(
        {
            "gkeClustersPerManagedZone": t.integer().optional(),
            "networksPerResponsePolicy": t.integer().optional(),
            "totalRrdataSizePerChange": t.integer().optional(),
            "policies": t.integer().optional(),
            "itemsPerRoutingPolicy": t.integer().optional(),
            "responsePolicyRulesPerResponsePolicy": t.integer().optional(),
            "rrsetDeletionsPerChange": t.integer().optional(),
            "gkeClustersPerResponsePolicy": t.integer().optional(),
            "kind": t.string(),
            "managedZones": t.integer().optional(),
            "managedZonesPerNetwork": t.integer().optional(),
            "networksPerManagedZone": t.integer().optional(),
            "dnsKeysPerManagedZone": t.integer().optional(),
            "targetNameServersPerPolicy": t.integer().optional(),
            "rrsetAdditionsPerChange": t.integer().optional(),
            "peeringZonesPerTargetNetwork": t.integer().optional(),
            "gkeClustersPerPolicy": t.integer().optional(),
            "managedZonesPerGkeCluster": t.integer().optional(),
            "rrsetsPerManagedZone": t.integer().optional(),
            "responsePolicies": t.integer().optional(),
            "targetNameServersPerManagedZone": t.integer().optional(),
            "networksPerPolicy": t.integer().optional(),
            "whitelistedKeySpecs": t.array(t.proxy(renames["DnsKeySpecIn"])).optional(),
            "resourceRecordsPerRrset": t.integer().optional(),
        }
    ).named(renames["QuotaIn"])
    types["QuotaOut"] = t.struct(
        {
            "gkeClustersPerManagedZone": t.integer().optional(),
            "networksPerResponsePolicy": t.integer().optional(),
            "totalRrdataSizePerChange": t.integer().optional(),
            "policies": t.integer().optional(),
            "itemsPerRoutingPolicy": t.integer().optional(),
            "responsePolicyRulesPerResponsePolicy": t.integer().optional(),
            "rrsetDeletionsPerChange": t.integer().optional(),
            "gkeClustersPerResponsePolicy": t.integer().optional(),
            "kind": t.string(),
            "managedZones": t.integer().optional(),
            "managedZonesPerNetwork": t.integer().optional(),
            "networksPerManagedZone": t.integer().optional(),
            "dnsKeysPerManagedZone": t.integer().optional(),
            "targetNameServersPerPolicy": t.integer().optional(),
            "rrsetAdditionsPerChange": t.integer().optional(),
            "peeringZonesPerTargetNetwork": t.integer().optional(),
            "gkeClustersPerPolicy": t.integer().optional(),
            "managedZonesPerGkeCluster": t.integer().optional(),
            "rrsetsPerManagedZone": t.integer().optional(),
            "responsePolicies": t.integer().optional(),
            "targetNameServersPerManagedZone": t.integer().optional(),
            "networksPerPolicy": t.integer().optional(),
            "whitelistedKeySpecs": t.array(
                t.proxy(renames["DnsKeySpecOut"])
            ).optional(),
            "resourceRecordsPerRrset": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuotaOut"])
    types["GoogleIamV1AuditLogConfigIn"] = t.struct(
        {
            "exemptedMembers": t.array(t.string()).optional(),
            "logType": t.string().optional(),
        }
    ).named(renames["GoogleIamV1AuditLogConfigIn"])
    types["GoogleIamV1AuditLogConfigOut"] = t.struct(
        {
            "exemptedMembers": t.array(t.string()).optional(),
            "logType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1AuditLogConfigOut"])
    types["PoliciesPatchResponseIn"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyIn"]),
            "header": t.proxy(renames["ResponseHeaderIn"]),
        }
    ).named(renames["PoliciesPatchResponseIn"])
    types["PoliciesPatchResponseOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]),
            "header": t.proxy(renames["ResponseHeaderOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PoliciesPatchResponseOut"])
    types["DnsKeysListResponseIn"] = t.struct(
        {
            "header": t.proxy(renames["ResponseHeaderIn"]),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "dnsKeys": t.array(t.proxy(renames["DnsKeyIn"])).optional(),
        }
    ).named(renames["DnsKeysListResponseIn"])
    types["DnsKeysListResponseOut"] = t.struct(
        {
            "header": t.proxy(renames["ResponseHeaderOut"]),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "dnsKeys": t.array(t.proxy(renames["DnsKeyOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DnsKeysListResponseOut"])
    types["ManagedZonePeeringConfigTargetNetworkIn"] = t.struct(
        {
            "kind": t.string(),
            "networkUrl": t.string().optional(),
            "deactivateTime": t.string().optional(),
        }
    ).named(renames["ManagedZonePeeringConfigTargetNetworkIn"])
    types["ManagedZonePeeringConfigTargetNetworkOut"] = t.struct(
        {
            "kind": t.string(),
            "networkUrl": t.string().optional(),
            "deactivateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedZonePeeringConfigTargetNetworkOut"])
    types["RRSetRoutingPolicyLoadBalancerTargetIn"] = t.struct(
        {
            "region": t.string().optional(),
            "port": t.string().optional(),
            "ipProtocol": t.string(),
            "kind": t.string(),
            "project": t.string().optional(),
            "networkUrl": t.string().optional(),
            "ipAddress": t.string().optional(),
            "loadBalancerType": t.string().optional(),
        }
    ).named(renames["RRSetRoutingPolicyLoadBalancerTargetIn"])
    types["RRSetRoutingPolicyLoadBalancerTargetOut"] = t.struct(
        {
            "region": t.string().optional(),
            "port": t.string().optional(),
            "ipProtocol": t.string(),
            "kind": t.string(),
            "project": t.string().optional(),
            "networkUrl": t.string().optional(),
            "ipAddress": t.string().optional(),
            "loadBalancerType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RRSetRoutingPolicyLoadBalancerTargetOut"])
    types["GoogleIamV1AuditConfigIn"] = t.struct(
        {
            "service": t.string().optional(),
            "auditLogConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditLogConfigIn"])
            ).optional(),
        }
    ).named(renames["GoogleIamV1AuditConfigIn"])
    types["GoogleIamV1AuditConfigOut"] = t.struct(
        {
            "service": t.string().optional(),
            "auditLogConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditLogConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1AuditConfigOut"])
    types["OperationIn"] = t.struct(
        {
            "dnsKeyContext": t.proxy(renames["OperationDnsKeyContextIn"]).optional(),
            "type": t.string().optional(),
            "user": t.string().optional(),
            "id": t.string().optional(),
            "status": t.string().optional(),
            "kind": t.string(),
            "zoneContext": t.proxy(renames["OperationManagedZoneContextIn"]).optional(),
            "startTime": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "dnsKeyContext": t.proxy(renames["OperationDnsKeyContextOut"]).optional(),
            "type": t.string().optional(),
            "user": t.string().optional(),
            "id": t.string().optional(),
            "status": t.string().optional(),
            "kind": t.string(),
            "zoneContext": t.proxy(
                renames["OperationManagedZoneContextOut"]
            ).optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
    types["RRSetRoutingPolicyGeoPolicyIn"] = t.struct(
        {
            "kind": t.string(),
            "enableFencing": t.boolean().optional(),
            "items": t.array(
                t.proxy(renames["RRSetRoutingPolicyGeoPolicyGeoPolicyItemIn"])
            ).optional(),
        }
    ).named(renames["RRSetRoutingPolicyGeoPolicyIn"])
    types["RRSetRoutingPolicyGeoPolicyOut"] = t.struct(
        {
            "kind": t.string(),
            "enableFencing": t.boolean().optional(),
            "items": t.array(
                t.proxy(renames["RRSetRoutingPolicyGeoPolicyGeoPolicyItemOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RRSetRoutingPolicyGeoPolicyOut"])
    types["GoogleIamV1GetIamPolicyRequestIn"] = t.struct(
        {"options": t.proxy(renames["GoogleIamV1GetPolicyOptionsIn"]).optional()}
    ).named(renames["GoogleIamV1GetIamPolicyRequestIn"])
    types["GoogleIamV1GetIamPolicyRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["GoogleIamV1GetPolicyOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1GetIamPolicyRequestOut"])
    types["OperationManagedZoneContextIn"] = t.struct(
        {
            "newValue": t.proxy(renames["ManagedZoneIn"]).optional(),
            "oldValue": t.proxy(renames["ManagedZoneIn"]).optional(),
        }
    ).named(renames["OperationManagedZoneContextIn"])
    types["OperationManagedZoneContextOut"] = t.struct(
        {
            "newValue": t.proxy(renames["ManagedZoneOut"]).optional(),
            "oldValue": t.proxy(renames["ManagedZoneOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationManagedZoneContextOut"])
    types["ManagedZoneDnsSecConfigIn"] = t.struct(
        {
            "defaultKeySpecs": t.array(t.proxy(renames["DnsKeySpecIn"])).optional(),
            "nonExistence": t.string().optional(),
            "state": t.string().optional(),
            "kind": t.string(),
        }
    ).named(renames["ManagedZoneDnsSecConfigIn"])
    types["ManagedZoneDnsSecConfigOut"] = t.struct(
        {
            "defaultKeySpecs": t.array(t.proxy(renames["DnsKeySpecOut"])).optional(),
            "nonExistence": t.string().optional(),
            "state": t.string().optional(),
            "kind": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedZoneDnsSecConfigOut"])
    types["ResponsePoliciesUpdateResponseIn"] = t.struct(
        {
            "header": t.proxy(renames["ResponseHeaderIn"]),
            "responsePolicy": t.proxy(renames["ResponsePolicyIn"]),
        }
    ).named(renames["ResponsePoliciesUpdateResponseIn"])
    types["ResponsePoliciesUpdateResponseOut"] = t.struct(
        {
            "header": t.proxy(renames["ResponseHeaderOut"]),
            "responsePolicy": t.proxy(renames["ResponsePolicyOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResponsePoliciesUpdateResponseOut"])
    types["ProjectIn"] = t.struct(
        {
            "kind": t.string(),
            "id": t.string().optional(),
            "quota": t.proxy(renames["QuotaIn"]).optional(),
            "number": t.string().optional(),
        }
    ).named(renames["ProjectIn"])
    types["ProjectOut"] = t.struct(
        {
            "kind": t.string(),
            "id": t.string().optional(),
            "quota": t.proxy(renames["QuotaOut"]).optional(),
            "number": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProjectOut"])
    types["RRSetRoutingPolicyHealthCheckTargetsIn"] = t.struct(
        {
            "internalLoadBalancers": t.array(
                t.proxy(renames["RRSetRoutingPolicyLoadBalancerTargetIn"])
            )
        }
    ).named(renames["RRSetRoutingPolicyHealthCheckTargetsIn"])
    types["RRSetRoutingPolicyHealthCheckTargetsOut"] = t.struct(
        {
            "internalLoadBalancers": t.array(
                t.proxy(renames["RRSetRoutingPolicyLoadBalancerTargetOut"])
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RRSetRoutingPolicyHealthCheckTargetsOut"])
    types["ResponsePolicyRulesUpdateResponseIn"] = t.struct(
        {
            "header": t.proxy(renames["ResponseHeaderIn"]),
            "responsePolicyRule": t.proxy(renames["ResponsePolicyRuleIn"]),
        }
    ).named(renames["ResponsePolicyRulesUpdateResponseIn"])
    types["ResponsePolicyRulesUpdateResponseOut"] = t.struct(
        {
            "header": t.proxy(renames["ResponseHeaderOut"]),
            "responsePolicyRule": t.proxy(renames["ResponsePolicyRuleOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResponsePolicyRulesUpdateResponseOut"])
    types["ResponsePoliciesPatchResponseIn"] = t.struct(
        {
            "header": t.proxy(renames["ResponseHeaderIn"]),
            "responsePolicy": t.proxy(renames["ResponsePolicyIn"]),
        }
    ).named(renames["ResponsePoliciesPatchResponseIn"])
    types["ResponsePoliciesPatchResponseOut"] = t.struct(
        {
            "header": t.proxy(renames["ResponseHeaderOut"]),
            "responsePolicy": t.proxy(renames["ResponsePolicyOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResponsePoliciesPatchResponseOut"])
    types["ResourceRecordSetIn"] = t.struct(
        {
            "routingPolicy": t.proxy(renames["RRSetRoutingPolicyIn"]).optional(),
            "name": t.string().optional(),
            "kind": t.string(),
            "type": t.string().optional(),
            "rrdatas": t.array(t.string()).optional(),
            "signatureRrdatas": t.array(t.string()).optional(),
            "ttl": t.integer().optional(),
        }
    ).named(renames["ResourceRecordSetIn"])
    types["ResourceRecordSetOut"] = t.struct(
        {
            "routingPolicy": t.proxy(renames["RRSetRoutingPolicyOut"]).optional(),
            "name": t.string().optional(),
            "kind": t.string(),
            "type": t.string().optional(),
            "rrdatas": t.array(t.string()).optional(),
            "signatureRrdatas": t.array(t.string()).optional(),
            "ttl": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceRecordSetOut"])
    types["PolicyIn"] = t.struct(
        {
            "networks": t.array(t.proxy(renames["PolicyNetworkIn"])).optional(),
            "id": t.string().optional(),
            "kind": t.string(),
            "enableLogging": t.boolean().optional(),
            "name": t.string().optional(),
            "alternativeNameServerConfig": t.proxy(
                renames["PolicyAlternativeNameServerConfigIn"]
            ).optional(),
            "enableInboundForwarding": t.boolean().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "networks": t.array(t.proxy(renames["PolicyNetworkOut"])).optional(),
            "id": t.string().optional(),
            "kind": t.string(),
            "enableLogging": t.boolean().optional(),
            "name": t.string().optional(),
            "alternativeNameServerConfig": t.proxy(
                renames["PolicyAlternativeNameServerConfigOut"]
            ).optional(),
            "enableInboundForwarding": t.boolean().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["GoogleIamV1PolicyIn"] = t.struct(
        {
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["GoogleIamV1BindingIn"])).optional(),
            "auditConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditConfigIn"])
            ).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["GoogleIamV1PolicyIn"])
    types["GoogleIamV1PolicyOut"] = t.struct(
        {
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["GoogleIamV1BindingOut"])).optional(),
            "auditConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditConfigOut"])
            ).optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1PolicyOut"])
    types["ManagedZonePrivateVisibilityConfigGKEClusterIn"] = t.struct(
        {"gkeClusterName": t.string().optional(), "kind": t.string()}
    ).named(renames["ManagedZonePrivateVisibilityConfigGKEClusterIn"])
    types["ManagedZonePrivateVisibilityConfigGKEClusterOut"] = t.struct(
        {
            "gkeClusterName": t.string().optional(),
            "kind": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedZonePrivateVisibilityConfigGKEClusterOut"])
    types["ManagedZoneIn"] = t.struct(
        {
            "visibility": t.string().optional(),
            "name": t.string().optional(),
            "serviceDirectoryConfig": t.proxy(
                renames["ManagedZoneServiceDirectoryConfigIn"]
            ).optional(),
            "cloudLoggingConfig": t.proxy(renames["ManagedZoneCloudLoggingConfigIn"]),
            "id": t.string().optional(),
            "description": t.string().optional(),
            "nameServerSet": t.string().optional(),
            "forwardingConfig": t.proxy(
                renames["ManagedZoneForwardingConfigIn"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "privateVisibilityConfig": t.proxy(
                renames["ManagedZonePrivateVisibilityConfigIn"]
            ).optional(),
            "peeringConfig": t.proxy(renames["ManagedZonePeeringConfigIn"]).optional(),
            "reverseLookupConfig": t.proxy(
                renames["ManagedZoneReverseLookupConfigIn"]
            ).optional(),
            "creationTime": t.string().optional(),
            "nameServers": t.array(t.string()).optional(),
            "dnsName": t.string().optional(),
            "kind": t.string(),
            "dnssecConfig": t.proxy(renames["ManagedZoneDnsSecConfigIn"]).optional(),
        }
    ).named(renames["ManagedZoneIn"])
    types["ManagedZoneOut"] = t.struct(
        {
            "visibility": t.string().optional(),
            "name": t.string().optional(),
            "serviceDirectoryConfig": t.proxy(
                renames["ManagedZoneServiceDirectoryConfigOut"]
            ).optional(),
            "cloudLoggingConfig": t.proxy(renames["ManagedZoneCloudLoggingConfigOut"]),
            "id": t.string().optional(),
            "description": t.string().optional(),
            "nameServerSet": t.string().optional(),
            "forwardingConfig": t.proxy(
                renames["ManagedZoneForwardingConfigOut"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "privateVisibilityConfig": t.proxy(
                renames["ManagedZonePrivateVisibilityConfigOut"]
            ).optional(),
            "peeringConfig": t.proxy(renames["ManagedZonePeeringConfigOut"]).optional(),
            "reverseLookupConfig": t.proxy(
                renames["ManagedZoneReverseLookupConfigOut"]
            ).optional(),
            "creationTime": t.string().optional(),
            "nameServers": t.array(t.string()).optional(),
            "dnsName": t.string().optional(),
            "kind": t.string(),
            "dnssecConfig": t.proxy(renames["ManagedZoneDnsSecConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedZoneOut"])
    types["ResponsePolicyIn"] = t.struct(
        {
            "id": t.string().optional(),
            "gkeClusters": t.array(
                t.proxy(renames["ResponsePolicyGKEClusterIn"])
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "networks": t.array(t.proxy(renames["ResponsePolicyNetworkIn"])).optional(),
            "kind": t.string(),
            "responsePolicyName": t.string().optional(),
        }
    ).named(renames["ResponsePolicyIn"])
    types["ResponsePolicyOut"] = t.struct(
        {
            "id": t.string().optional(),
            "gkeClusters": t.array(
                t.proxy(renames["ResponsePolicyGKEClusterOut"])
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "networks": t.array(
                t.proxy(renames["ResponsePolicyNetworkOut"])
            ).optional(),
            "kind": t.string(),
            "responsePolicyName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResponsePolicyOut"])
    types["ManagedZonePrivateVisibilityConfigIn"] = t.struct(
        {
            "networks": t.array(
                t.proxy(renames["ManagedZonePrivateVisibilityConfigNetworkIn"])
            ).optional(),
            "kind": t.string(),
            "gkeClusters": t.array(
                t.proxy(renames["ManagedZonePrivateVisibilityConfigGKEClusterIn"])
            ).optional(),
        }
    ).named(renames["ManagedZonePrivateVisibilityConfigIn"])
    types["ManagedZonePrivateVisibilityConfigOut"] = t.struct(
        {
            "networks": t.array(
                t.proxy(renames["ManagedZonePrivateVisibilityConfigNetworkOut"])
            ).optional(),
            "kind": t.string(),
            "gkeClusters": t.array(
                t.proxy(renames["ManagedZonePrivateVisibilityConfigGKEClusterOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedZonePrivateVisibilityConfigOut"])
    types["ManagedZonePrivateVisibilityConfigNetworkIn"] = t.struct(
        {"kind": t.string(), "networkUrl": t.string().optional()}
    ).named(renames["ManagedZonePrivateVisibilityConfigNetworkIn"])
    types["ManagedZonePrivateVisibilityConfigNetworkOut"] = t.struct(
        {
            "kind": t.string(),
            "networkUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedZonePrivateVisibilityConfigNetworkOut"])
    types["OperationDnsKeyContextIn"] = t.struct(
        {
            "oldValue": t.proxy(renames["DnsKeyIn"]).optional(),
            "newValue": t.proxy(renames["DnsKeyIn"]).optional(),
        }
    ).named(renames["OperationDnsKeyContextIn"])
    types["OperationDnsKeyContextOut"] = t.struct(
        {
            "oldValue": t.proxy(renames["DnsKeyOut"]).optional(),
            "newValue": t.proxy(renames["DnsKeyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationDnsKeyContextOut"])
    types["RRSetRoutingPolicyPrimaryBackupPolicyIn"] = t.struct(
        {
            "primaryTargets": t.proxy(
                renames["RRSetRoutingPolicyHealthCheckTargetsIn"]
            ),
            "kind": t.string(),
            "backupGeoTargets": t.proxy(
                renames["RRSetRoutingPolicyGeoPolicyIn"]
            ).optional(),
            "trickleTraffic": t.number().optional(),
        }
    ).named(renames["RRSetRoutingPolicyPrimaryBackupPolicyIn"])
    types["RRSetRoutingPolicyPrimaryBackupPolicyOut"] = t.struct(
        {
            "primaryTargets": t.proxy(
                renames["RRSetRoutingPolicyHealthCheckTargetsOut"]
            ),
            "kind": t.string(),
            "backupGeoTargets": t.proxy(
                renames["RRSetRoutingPolicyGeoPolicyOut"]
            ).optional(),
            "trickleTraffic": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RRSetRoutingPolicyPrimaryBackupPolicyOut"])
    types["PolicyAlternativeNameServerConfigIn"] = t.struct(
        {
            "kind": t.string(),
            "targetNameServers": t.array(
                t.proxy(renames["PolicyAlternativeNameServerConfigTargetNameServerIn"])
            ).optional(),
        }
    ).named(renames["PolicyAlternativeNameServerConfigIn"])
    types["PolicyAlternativeNameServerConfigOut"] = t.struct(
        {
            "kind": t.string(),
            "targetNameServers": t.array(
                t.proxy(renames["PolicyAlternativeNameServerConfigTargetNameServerOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyAlternativeNameServerConfigOut"])
    types["RRSetRoutingPolicyGeoPolicyGeoPolicyItemIn"] = t.struct(
        {
            "rrdatas": t.array(t.string()),
            "location": t.string().optional(),
            "signatureRrdatas": t.array(t.string()).optional(),
            "kind": t.string(),
            "healthCheckedTargets": t.proxy(
                renames["RRSetRoutingPolicyHealthCheckTargetsIn"]
            ).optional(),
        }
    ).named(renames["RRSetRoutingPolicyGeoPolicyGeoPolicyItemIn"])
    types["RRSetRoutingPolicyGeoPolicyGeoPolicyItemOut"] = t.struct(
        {
            "rrdatas": t.array(t.string()),
            "location": t.string().optional(),
            "signatureRrdatas": t.array(t.string()).optional(),
            "kind": t.string(),
            "healthCheckedTargets": t.proxy(
                renames["RRSetRoutingPolicyHealthCheckTargetsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RRSetRoutingPolicyGeoPolicyGeoPolicyItemOut"])
    types["GoogleIamV1TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["GoogleIamV1TestIamPermissionsRequestIn"])
    types["GoogleIamV1TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1TestIamPermissionsRequestOut"])
    types["ManagedZoneForwardingConfigNameServerTargetIn"] = t.struct(
        {
            "kind": t.string(),
            "forwardingPath": t.string().optional(),
            "ipv4Address": t.string().optional(),
            "ipv6Address": t.string().optional(),
        }
    ).named(renames["ManagedZoneForwardingConfigNameServerTargetIn"])
    types["ManagedZoneForwardingConfigNameServerTargetOut"] = t.struct(
        {
            "kind": t.string(),
            "forwardingPath": t.string().optional(),
            "ipv4Address": t.string().optional(),
            "ipv6Address": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedZoneForwardingConfigNameServerTargetOut"])
    types["ChangesListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "changes": t.array(t.proxy(renames["ChangeIn"])).optional(),
            "header": t.proxy(renames["ResponseHeaderIn"]),
        }
    ).named(renames["ChangesListResponseIn"])
    types["ChangesListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "changes": t.array(t.proxy(renames["ChangeOut"])).optional(),
            "header": t.proxy(renames["ResponseHeaderOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChangesListResponseOut"])
    types["PoliciesUpdateResponseIn"] = t.struct(
        {
            "header": t.proxy(renames["ResponseHeaderIn"]),
            "policy": t.proxy(renames["PolicyIn"]),
        }
    ).named(renames["PoliciesUpdateResponseIn"])
    types["PoliciesUpdateResponseOut"] = t.struct(
        {
            "header": t.proxy(renames["ResponseHeaderOut"]),
            "policy": t.proxy(renames["PolicyOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PoliciesUpdateResponseOut"])
    types["ManagedZoneReverseLookupConfigIn"] = t.struct({"kind": t.string()}).named(
        renames["ManagedZoneReverseLookupConfigIn"]
    )
    types["ManagedZoneReverseLookupConfigOut"] = t.struct(
        {"kind": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ManagedZoneReverseLookupConfigOut"])
    types["GoogleIamV1BindingIn"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
        }
    ).named(renames["GoogleIamV1BindingIn"])
    types["GoogleIamV1BindingOut"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1BindingOut"])
    types["ResponseHeaderIn"] = t.struct({"operationId": t.string().optional()}).named(
        renames["ResponseHeaderIn"]
    )
    types["ResponseHeaderOut"] = t.struct(
        {
            "operationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResponseHeaderOut"])
    types["ResponsePolicyGKEClusterIn"] = t.struct(
        {"gkeClusterName": t.string().optional(), "kind": t.string()}
    ).named(renames["ResponsePolicyGKEClusterIn"])
    types["ResponsePolicyGKEClusterOut"] = t.struct(
        {
            "gkeClusterName": t.string().optional(),
            "kind": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResponsePolicyGKEClusterOut"])
    types["GoogleIamV1SetIamPolicyRequestIn"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "policy": t.proxy(renames["GoogleIamV1PolicyIn"]).optional(),
        }
    ).named(renames["GoogleIamV1SetIamPolicyRequestIn"])
    types["GoogleIamV1SetIamPolicyRequestOut"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "policy": t.proxy(renames["GoogleIamV1PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1SetIamPolicyRequestOut"])
    types["RRSetRoutingPolicyWrrPolicyWrrPolicyItemIn"] = t.struct(
        {
            "rrdatas": t.array(t.string()),
            "weight": t.number().optional(),
            "healthCheckedTargets": t.proxy(
                renames["RRSetRoutingPolicyHealthCheckTargetsIn"]
            ).optional(),
            "kind": t.string(),
            "signatureRrdatas": t.array(t.string()).optional(),
        }
    ).named(renames["RRSetRoutingPolicyWrrPolicyWrrPolicyItemIn"])
    types["RRSetRoutingPolicyWrrPolicyWrrPolicyItemOut"] = t.struct(
        {
            "rrdatas": t.array(t.string()),
            "weight": t.number().optional(),
            "healthCheckedTargets": t.proxy(
                renames["RRSetRoutingPolicyHealthCheckTargetsOut"]
            ).optional(),
            "kind": t.string(),
            "signatureRrdatas": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RRSetRoutingPolicyWrrPolicyWrrPolicyItemOut"])
    types["ResponsePolicyRuleLocalDataIn"] = t.struct(
        {"localDatas": t.array(t.proxy(renames["ResourceRecordSetIn"])).optional()}
    ).named(renames["ResponsePolicyRuleLocalDataIn"])
    types["ResponsePolicyRuleLocalDataOut"] = t.struct(
        {
            "localDatas": t.array(t.proxy(renames["ResourceRecordSetOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResponsePolicyRuleLocalDataOut"])
    types["ExprIn"] = t.struct(
        {
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["ResponsePolicyRulesListResponseIn"] = t.struct(
        {
            "header": t.proxy(renames["ResponseHeaderIn"]),
            "responsePolicyRules": t.array(
                t.proxy(renames["ResponsePolicyRuleIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ResponsePolicyRulesListResponseIn"])
    types["ResponsePolicyRulesListResponseOut"] = t.struct(
        {
            "header": t.proxy(renames["ResponseHeaderOut"]),
            "responsePolicyRules": t.array(
                t.proxy(renames["ResponsePolicyRuleOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResponsePolicyRulesListResponseOut"])
    types["PolicyAlternativeNameServerConfigTargetNameServerIn"] = t.struct(
        {
            "kind": t.string(),
            "ipv4Address": t.string().optional(),
            "ipv6Address": t.string().optional(),
            "forwardingPath": t.string().optional(),
        }
    ).named(renames["PolicyAlternativeNameServerConfigTargetNameServerIn"])
    types["PolicyAlternativeNameServerConfigTargetNameServerOut"] = t.struct(
        {
            "kind": t.string(),
            "ipv4Address": t.string().optional(),
            "ipv6Address": t.string().optional(),
            "forwardingPath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyAlternativeNameServerConfigTargetNameServerOut"])
    types["DnsKeyDigestIn"] = t.struct(
        {"type": t.string().optional(), "digest": t.string().optional()}
    ).named(renames["DnsKeyDigestIn"])
    types["DnsKeyDigestOut"] = t.struct(
        {
            "type": t.string().optional(),
            "digest": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DnsKeyDigestOut"])

    functions = {}
    functions["policiesUpdate"] = dns.delete(
        "dns/v1/projects/{project}/policies/{policy}",
        t.struct(
            {
                "policy": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "project": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["policiesGet"] = dns.delete(
        "dns/v1/projects/{project}/policies/{policy}",
        t.struct(
            {
                "policy": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "project": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["policiesList"] = dns.delete(
        "dns/v1/projects/{project}/policies/{policy}",
        t.struct(
            {
                "policy": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "project": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["policiesCreate"] = dns.delete(
        "dns/v1/projects/{project}/policies/{policy}",
        t.struct(
            {
                "policy": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "project": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["policiesPatch"] = dns.delete(
        "dns/v1/projects/{project}/policies/{policy}",
        t.struct(
            {
                "policy": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "project": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["policiesDelete"] = dns.delete(
        "dns/v1/projects/{project}/policies/{policy}",
        t.struct(
            {
                "policy": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "project": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGet"] = dns.get(
        "dns/v1/projects/{project}",
        t.struct(
            {
                "project": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProjectOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["resourceRecordSetsPatch"] = dns.get(
        "dns/v1/projects/{project}/managedZones/{managedZone}/rrsets/{name}/{type}",
        t.struct(
            {
                "name": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "managedZone": t.string().optional(),
                "project": t.string().optional(),
                "type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ResourceRecordSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["resourceRecordSetsDelete"] = dns.get(
        "dns/v1/projects/{project}/managedZones/{managedZone}/rrsets/{name}/{type}",
        t.struct(
            {
                "name": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "managedZone": t.string().optional(),
                "project": t.string().optional(),
                "type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ResourceRecordSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["resourceRecordSetsCreate"] = dns.get(
        "dns/v1/projects/{project}/managedZones/{managedZone}/rrsets/{name}/{type}",
        t.struct(
            {
                "name": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "managedZone": t.string().optional(),
                "project": t.string().optional(),
                "type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ResourceRecordSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["resourceRecordSetsList"] = dns.get(
        "dns/v1/projects/{project}/managedZones/{managedZone}/rrsets/{name}/{type}",
        t.struct(
            {
                "name": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "managedZone": t.string().optional(),
                "project": t.string().optional(),
                "type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ResourceRecordSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["resourceRecordSetsGet"] = dns.get(
        "dns/v1/projects/{project}/managedZones/{managedZone}/rrsets/{name}/{type}",
        t.struct(
            {
                "name": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "managedZone": t.string().optional(),
                "project": t.string().optional(),
                "type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ResourceRecordSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["responsePoliciesDelete"] = dns.patch(
        "dns/v1/projects/{project}/responsePolicies/{responsePolicy}",
        t.struct(
            {
                "responsePolicy": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "project": t.string().optional(),
                "id": t.string().optional(),
                "gkeClusters": t.array(
                    t.proxy(renames["ResponsePolicyGKEClusterIn"])
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "networks": t.array(
                    t.proxy(renames["ResponsePolicyNetworkIn"])
                ).optional(),
                "kind": t.string(),
                "responsePolicyName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ResponsePoliciesPatchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["responsePoliciesList"] = dns.patch(
        "dns/v1/projects/{project}/responsePolicies/{responsePolicy}",
        t.struct(
            {
                "responsePolicy": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "project": t.string().optional(),
                "id": t.string().optional(),
                "gkeClusters": t.array(
                    t.proxy(renames["ResponsePolicyGKEClusterIn"])
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "networks": t.array(
                    t.proxy(renames["ResponsePolicyNetworkIn"])
                ).optional(),
                "kind": t.string(),
                "responsePolicyName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ResponsePoliciesPatchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["responsePoliciesCreate"] = dns.patch(
        "dns/v1/projects/{project}/responsePolicies/{responsePolicy}",
        t.struct(
            {
                "responsePolicy": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "project": t.string().optional(),
                "id": t.string().optional(),
                "gkeClusters": t.array(
                    t.proxy(renames["ResponsePolicyGKEClusterIn"])
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "networks": t.array(
                    t.proxy(renames["ResponsePolicyNetworkIn"])
                ).optional(),
                "kind": t.string(),
                "responsePolicyName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ResponsePoliciesPatchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["responsePoliciesUpdate"] = dns.patch(
        "dns/v1/projects/{project}/responsePolicies/{responsePolicy}",
        t.struct(
            {
                "responsePolicy": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "project": t.string().optional(),
                "id": t.string().optional(),
                "gkeClusters": t.array(
                    t.proxy(renames["ResponsePolicyGKEClusterIn"])
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "networks": t.array(
                    t.proxy(renames["ResponsePolicyNetworkIn"])
                ).optional(),
                "kind": t.string(),
                "responsePolicyName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ResponsePoliciesPatchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["responsePoliciesGet"] = dns.patch(
        "dns/v1/projects/{project}/responsePolicies/{responsePolicy}",
        t.struct(
            {
                "responsePolicy": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "project": t.string().optional(),
                "id": t.string().optional(),
                "gkeClusters": t.array(
                    t.proxy(renames["ResponsePolicyGKEClusterIn"])
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "networks": t.array(
                    t.proxy(renames["ResponsePolicyNetworkIn"])
                ).optional(),
                "kind": t.string(),
                "responsePolicyName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ResponsePoliciesPatchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["responsePoliciesPatch"] = dns.patch(
        "dns/v1/projects/{project}/responsePolicies/{responsePolicy}",
        t.struct(
            {
                "responsePolicy": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "project": t.string().optional(),
                "id": t.string().optional(),
                "gkeClusters": t.array(
                    t.proxy(renames["ResponsePolicyGKEClusterIn"])
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "networks": t.array(
                    t.proxy(renames["ResponsePolicyNetworkIn"])
                ).optional(),
                "kind": t.string(),
                "responsePolicyName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ResponsePoliciesPatchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managedZonesGetIamPolicy"] = dns.patch(
        "dns/v1/projects/{project}/managedZones/{managedZone}",
        t.struct(
            {
                "project": t.string().optional(),
                "managedZone": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "visibility": t.string().optional(),
                "name": t.string().optional(),
                "serviceDirectoryConfig": t.proxy(
                    renames["ManagedZoneServiceDirectoryConfigIn"]
                ).optional(),
                "cloudLoggingConfig": t.proxy(
                    renames["ManagedZoneCloudLoggingConfigIn"]
                ),
                "id": t.string().optional(),
                "description": t.string().optional(),
                "nameServerSet": t.string().optional(),
                "forwardingConfig": t.proxy(
                    renames["ManagedZoneForwardingConfigIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "privateVisibilityConfig": t.proxy(
                    renames["ManagedZonePrivateVisibilityConfigIn"]
                ).optional(),
                "peeringConfig": t.proxy(
                    renames["ManagedZonePeeringConfigIn"]
                ).optional(),
                "reverseLookupConfig": t.proxy(
                    renames["ManagedZoneReverseLookupConfigIn"]
                ).optional(),
                "creationTime": t.string().optional(),
                "nameServers": t.array(t.string()).optional(),
                "dnsName": t.string().optional(),
                "kind": t.string(),
                "dnssecConfig": t.proxy(
                    renames["ManagedZoneDnsSecConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managedZonesList"] = dns.patch(
        "dns/v1/projects/{project}/managedZones/{managedZone}",
        t.struct(
            {
                "project": t.string().optional(),
                "managedZone": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "visibility": t.string().optional(),
                "name": t.string().optional(),
                "serviceDirectoryConfig": t.proxy(
                    renames["ManagedZoneServiceDirectoryConfigIn"]
                ).optional(),
                "cloudLoggingConfig": t.proxy(
                    renames["ManagedZoneCloudLoggingConfigIn"]
                ),
                "id": t.string().optional(),
                "description": t.string().optional(),
                "nameServerSet": t.string().optional(),
                "forwardingConfig": t.proxy(
                    renames["ManagedZoneForwardingConfigIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "privateVisibilityConfig": t.proxy(
                    renames["ManagedZonePrivateVisibilityConfigIn"]
                ).optional(),
                "peeringConfig": t.proxy(
                    renames["ManagedZonePeeringConfigIn"]
                ).optional(),
                "reverseLookupConfig": t.proxy(
                    renames["ManagedZoneReverseLookupConfigIn"]
                ).optional(),
                "creationTime": t.string().optional(),
                "nameServers": t.array(t.string()).optional(),
                "dnsName": t.string().optional(),
                "kind": t.string(),
                "dnssecConfig": t.proxy(
                    renames["ManagedZoneDnsSecConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managedZonesDelete"] = dns.patch(
        "dns/v1/projects/{project}/managedZones/{managedZone}",
        t.struct(
            {
                "project": t.string().optional(),
                "managedZone": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "visibility": t.string().optional(),
                "name": t.string().optional(),
                "serviceDirectoryConfig": t.proxy(
                    renames["ManagedZoneServiceDirectoryConfigIn"]
                ).optional(),
                "cloudLoggingConfig": t.proxy(
                    renames["ManagedZoneCloudLoggingConfigIn"]
                ),
                "id": t.string().optional(),
                "description": t.string().optional(),
                "nameServerSet": t.string().optional(),
                "forwardingConfig": t.proxy(
                    renames["ManagedZoneForwardingConfigIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "privateVisibilityConfig": t.proxy(
                    renames["ManagedZonePrivateVisibilityConfigIn"]
                ).optional(),
                "peeringConfig": t.proxy(
                    renames["ManagedZonePeeringConfigIn"]
                ).optional(),
                "reverseLookupConfig": t.proxy(
                    renames["ManagedZoneReverseLookupConfigIn"]
                ).optional(),
                "creationTime": t.string().optional(),
                "nameServers": t.array(t.string()).optional(),
                "dnsName": t.string().optional(),
                "kind": t.string(),
                "dnssecConfig": t.proxy(
                    renames["ManagedZoneDnsSecConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managedZonesGet"] = dns.patch(
        "dns/v1/projects/{project}/managedZones/{managedZone}",
        t.struct(
            {
                "project": t.string().optional(),
                "managedZone": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "visibility": t.string().optional(),
                "name": t.string().optional(),
                "serviceDirectoryConfig": t.proxy(
                    renames["ManagedZoneServiceDirectoryConfigIn"]
                ).optional(),
                "cloudLoggingConfig": t.proxy(
                    renames["ManagedZoneCloudLoggingConfigIn"]
                ),
                "id": t.string().optional(),
                "description": t.string().optional(),
                "nameServerSet": t.string().optional(),
                "forwardingConfig": t.proxy(
                    renames["ManagedZoneForwardingConfigIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "privateVisibilityConfig": t.proxy(
                    renames["ManagedZonePrivateVisibilityConfigIn"]
                ).optional(),
                "peeringConfig": t.proxy(
                    renames["ManagedZonePeeringConfigIn"]
                ).optional(),
                "reverseLookupConfig": t.proxy(
                    renames["ManagedZoneReverseLookupConfigIn"]
                ).optional(),
                "creationTime": t.string().optional(),
                "nameServers": t.array(t.string()).optional(),
                "dnsName": t.string().optional(),
                "kind": t.string(),
                "dnssecConfig": t.proxy(
                    renames["ManagedZoneDnsSecConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managedZonesTestIamPermissions"] = dns.patch(
        "dns/v1/projects/{project}/managedZones/{managedZone}",
        t.struct(
            {
                "project": t.string().optional(),
                "managedZone": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "visibility": t.string().optional(),
                "name": t.string().optional(),
                "serviceDirectoryConfig": t.proxy(
                    renames["ManagedZoneServiceDirectoryConfigIn"]
                ).optional(),
                "cloudLoggingConfig": t.proxy(
                    renames["ManagedZoneCloudLoggingConfigIn"]
                ),
                "id": t.string().optional(),
                "description": t.string().optional(),
                "nameServerSet": t.string().optional(),
                "forwardingConfig": t.proxy(
                    renames["ManagedZoneForwardingConfigIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "privateVisibilityConfig": t.proxy(
                    renames["ManagedZonePrivateVisibilityConfigIn"]
                ).optional(),
                "peeringConfig": t.proxy(
                    renames["ManagedZonePeeringConfigIn"]
                ).optional(),
                "reverseLookupConfig": t.proxy(
                    renames["ManagedZoneReverseLookupConfigIn"]
                ).optional(),
                "creationTime": t.string().optional(),
                "nameServers": t.array(t.string()).optional(),
                "dnsName": t.string().optional(),
                "kind": t.string(),
                "dnssecConfig": t.proxy(
                    renames["ManagedZoneDnsSecConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managedZonesUpdate"] = dns.patch(
        "dns/v1/projects/{project}/managedZones/{managedZone}",
        t.struct(
            {
                "project": t.string().optional(),
                "managedZone": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "visibility": t.string().optional(),
                "name": t.string().optional(),
                "serviceDirectoryConfig": t.proxy(
                    renames["ManagedZoneServiceDirectoryConfigIn"]
                ).optional(),
                "cloudLoggingConfig": t.proxy(
                    renames["ManagedZoneCloudLoggingConfigIn"]
                ),
                "id": t.string().optional(),
                "description": t.string().optional(),
                "nameServerSet": t.string().optional(),
                "forwardingConfig": t.proxy(
                    renames["ManagedZoneForwardingConfigIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "privateVisibilityConfig": t.proxy(
                    renames["ManagedZonePrivateVisibilityConfigIn"]
                ).optional(),
                "peeringConfig": t.proxy(
                    renames["ManagedZonePeeringConfigIn"]
                ).optional(),
                "reverseLookupConfig": t.proxy(
                    renames["ManagedZoneReverseLookupConfigIn"]
                ).optional(),
                "creationTime": t.string().optional(),
                "nameServers": t.array(t.string()).optional(),
                "dnsName": t.string().optional(),
                "kind": t.string(),
                "dnssecConfig": t.proxy(
                    renames["ManagedZoneDnsSecConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managedZonesSetIamPolicy"] = dns.patch(
        "dns/v1/projects/{project}/managedZones/{managedZone}",
        t.struct(
            {
                "project": t.string().optional(),
                "managedZone": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "visibility": t.string().optional(),
                "name": t.string().optional(),
                "serviceDirectoryConfig": t.proxy(
                    renames["ManagedZoneServiceDirectoryConfigIn"]
                ).optional(),
                "cloudLoggingConfig": t.proxy(
                    renames["ManagedZoneCloudLoggingConfigIn"]
                ),
                "id": t.string().optional(),
                "description": t.string().optional(),
                "nameServerSet": t.string().optional(),
                "forwardingConfig": t.proxy(
                    renames["ManagedZoneForwardingConfigIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "privateVisibilityConfig": t.proxy(
                    renames["ManagedZonePrivateVisibilityConfigIn"]
                ).optional(),
                "peeringConfig": t.proxy(
                    renames["ManagedZonePeeringConfigIn"]
                ).optional(),
                "reverseLookupConfig": t.proxy(
                    renames["ManagedZoneReverseLookupConfigIn"]
                ).optional(),
                "creationTime": t.string().optional(),
                "nameServers": t.array(t.string()).optional(),
                "dnsName": t.string().optional(),
                "kind": t.string(),
                "dnssecConfig": t.proxy(
                    renames["ManagedZoneDnsSecConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managedZonesCreate"] = dns.patch(
        "dns/v1/projects/{project}/managedZones/{managedZone}",
        t.struct(
            {
                "project": t.string().optional(),
                "managedZone": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "visibility": t.string().optional(),
                "name": t.string().optional(),
                "serviceDirectoryConfig": t.proxy(
                    renames["ManagedZoneServiceDirectoryConfigIn"]
                ).optional(),
                "cloudLoggingConfig": t.proxy(
                    renames["ManagedZoneCloudLoggingConfigIn"]
                ),
                "id": t.string().optional(),
                "description": t.string().optional(),
                "nameServerSet": t.string().optional(),
                "forwardingConfig": t.proxy(
                    renames["ManagedZoneForwardingConfigIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "privateVisibilityConfig": t.proxy(
                    renames["ManagedZonePrivateVisibilityConfigIn"]
                ).optional(),
                "peeringConfig": t.proxy(
                    renames["ManagedZonePeeringConfigIn"]
                ).optional(),
                "reverseLookupConfig": t.proxy(
                    renames["ManagedZoneReverseLookupConfigIn"]
                ).optional(),
                "creationTime": t.string().optional(),
                "nameServers": t.array(t.string()).optional(),
                "dnsName": t.string().optional(),
                "kind": t.string(),
                "dnssecConfig": t.proxy(
                    renames["ManagedZoneDnsSecConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managedZonesPatch"] = dns.patch(
        "dns/v1/projects/{project}/managedZones/{managedZone}",
        t.struct(
            {
                "project": t.string().optional(),
                "managedZone": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "visibility": t.string().optional(),
                "name": t.string().optional(),
                "serviceDirectoryConfig": t.proxy(
                    renames["ManagedZoneServiceDirectoryConfigIn"]
                ).optional(),
                "cloudLoggingConfig": t.proxy(
                    renames["ManagedZoneCloudLoggingConfigIn"]
                ),
                "id": t.string().optional(),
                "description": t.string().optional(),
                "nameServerSet": t.string().optional(),
                "forwardingConfig": t.proxy(
                    renames["ManagedZoneForwardingConfigIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "privateVisibilityConfig": t.proxy(
                    renames["ManagedZonePrivateVisibilityConfigIn"]
                ).optional(),
                "peeringConfig": t.proxy(
                    renames["ManagedZonePeeringConfigIn"]
                ).optional(),
                "reverseLookupConfig": t.proxy(
                    renames["ManagedZoneReverseLookupConfigIn"]
                ).optional(),
                "creationTime": t.string().optional(),
                "nameServers": t.array(t.string()).optional(),
                "dnsName": t.string().optional(),
                "kind": t.string(),
                "dnssecConfig": t.proxy(
                    renames["ManagedZoneDnsSecConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["dnsKeysGet"] = dns.get(
        "dns/v1/projects/{project}/managedZones/{managedZone}/dnsKeys",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "project": t.string().optional(),
                "digestType": t.string().optional(),
                "maxResults": t.integer().optional(),
                "managedZone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DnsKeysListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["dnsKeysList"] = dns.get(
        "dns/v1/projects/{project}/managedZones/{managedZone}/dnsKeys",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "project": t.string().optional(),
                "digestType": t.string().optional(),
                "maxResults": t.integer().optional(),
                "managedZone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DnsKeysListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managedZoneOperationsGet"] = dns.get(
        "dns/v1/projects/{project}/managedZones/{managedZone}/operations",
        t.struct(
            {
                "sortBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "managedZone": t.string().optional(),
                "project": t.string().optional(),
                "maxResults": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ManagedZoneOperationsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managedZoneOperationsList"] = dns.get(
        "dns/v1/projects/{project}/managedZones/{managedZone}/operations",
        t.struct(
            {
                "sortBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "managedZone": t.string().optional(),
                "project": t.string().optional(),
                "maxResults": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ManagedZoneOperationsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["responsePolicyRulesList"] = dns.patch(
        "dns/v1/projects/{project}/responsePolicies/{responsePolicy}/rules/{responsePolicyRule}",
        t.struct(
            {
                "clientOperationId": t.string().optional(),
                "project": t.string().optional(),
                "responsePolicy": t.string().optional(),
                "responsePolicyRule": t.string().optional(),
                "kind": t.string(),
                "ruleName": t.string().optional(),
                "behavior": t.string().optional(),
                "localData": t.proxy(
                    renames["ResponsePolicyRuleLocalDataIn"]
                ).optional(),
                "dnsName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ResponsePolicyRulesPatchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["responsePolicyRulesDelete"] = dns.patch(
        "dns/v1/projects/{project}/responsePolicies/{responsePolicy}/rules/{responsePolicyRule}",
        t.struct(
            {
                "clientOperationId": t.string().optional(),
                "project": t.string().optional(),
                "responsePolicy": t.string().optional(),
                "responsePolicyRule": t.string().optional(),
                "kind": t.string(),
                "ruleName": t.string().optional(),
                "behavior": t.string().optional(),
                "localData": t.proxy(
                    renames["ResponsePolicyRuleLocalDataIn"]
                ).optional(),
                "dnsName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ResponsePolicyRulesPatchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["responsePolicyRulesUpdate"] = dns.patch(
        "dns/v1/projects/{project}/responsePolicies/{responsePolicy}/rules/{responsePolicyRule}",
        t.struct(
            {
                "clientOperationId": t.string().optional(),
                "project": t.string().optional(),
                "responsePolicy": t.string().optional(),
                "responsePolicyRule": t.string().optional(),
                "kind": t.string(),
                "ruleName": t.string().optional(),
                "behavior": t.string().optional(),
                "localData": t.proxy(
                    renames["ResponsePolicyRuleLocalDataIn"]
                ).optional(),
                "dnsName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ResponsePolicyRulesPatchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["responsePolicyRulesGet"] = dns.patch(
        "dns/v1/projects/{project}/responsePolicies/{responsePolicy}/rules/{responsePolicyRule}",
        t.struct(
            {
                "clientOperationId": t.string().optional(),
                "project": t.string().optional(),
                "responsePolicy": t.string().optional(),
                "responsePolicyRule": t.string().optional(),
                "kind": t.string(),
                "ruleName": t.string().optional(),
                "behavior": t.string().optional(),
                "localData": t.proxy(
                    renames["ResponsePolicyRuleLocalDataIn"]
                ).optional(),
                "dnsName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ResponsePolicyRulesPatchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["responsePolicyRulesCreate"] = dns.patch(
        "dns/v1/projects/{project}/responsePolicies/{responsePolicy}/rules/{responsePolicyRule}",
        t.struct(
            {
                "clientOperationId": t.string().optional(),
                "project": t.string().optional(),
                "responsePolicy": t.string().optional(),
                "responsePolicyRule": t.string().optional(),
                "kind": t.string(),
                "ruleName": t.string().optional(),
                "behavior": t.string().optional(),
                "localData": t.proxy(
                    renames["ResponsePolicyRuleLocalDataIn"]
                ).optional(),
                "dnsName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ResponsePolicyRulesPatchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["responsePolicyRulesPatch"] = dns.patch(
        "dns/v1/projects/{project}/responsePolicies/{responsePolicy}/rules/{responsePolicyRule}",
        t.struct(
            {
                "clientOperationId": t.string().optional(),
                "project": t.string().optional(),
                "responsePolicy": t.string().optional(),
                "responsePolicyRule": t.string().optional(),
                "kind": t.string(),
                "ruleName": t.string().optional(),
                "behavior": t.string().optional(),
                "localData": t.proxy(
                    renames["ResponsePolicyRuleLocalDataIn"]
                ).optional(),
                "dnsName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ResponsePolicyRulesPatchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["changesList"] = dns.post(
        "dns/v1/projects/{project}/managedZones/{managedZone}/changes",
        t.struct(
            {
                "project": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "managedZone": t.string().optional(),
                "kind": t.string(),
                "startTime": t.string().optional(),
                "deletions": t.array(
                    t.proxy(renames["ResourceRecordSetIn"])
                ).optional(),
                "status": t.string().optional(),
                "isServing": t.boolean().optional(),
                "id": t.string().optional(),
                "additions": t.array(
                    t.proxy(renames["ResourceRecordSetIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChangeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["changesGet"] = dns.post(
        "dns/v1/projects/{project}/managedZones/{managedZone}/changes",
        t.struct(
            {
                "project": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "managedZone": t.string().optional(),
                "kind": t.string(),
                "startTime": t.string().optional(),
                "deletions": t.array(
                    t.proxy(renames["ResourceRecordSetIn"])
                ).optional(),
                "status": t.string().optional(),
                "isServing": t.boolean().optional(),
                "id": t.string().optional(),
                "additions": t.array(
                    t.proxy(renames["ResourceRecordSetIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChangeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["changesCreate"] = dns.post(
        "dns/v1/projects/{project}/managedZones/{managedZone}/changes",
        t.struct(
            {
                "project": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "managedZone": t.string().optional(),
                "kind": t.string(),
                "startTime": t.string().optional(),
                "deletions": t.array(
                    t.proxy(renames["ResourceRecordSetIn"])
                ).optional(),
                "status": t.string().optional(),
                "isServing": t.boolean().optional(),
                "id": t.string().optional(),
                "additions": t.array(
                    t.proxy(renames["ResourceRecordSetIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChangeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="dns", renames=renames, types=Box(types), functions=Box(functions)
    )
