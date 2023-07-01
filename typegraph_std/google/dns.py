from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_dns():
    dns = HTTPRuntime("https://dns.googleapis.com/")

    renames = {
        "ErrorResponse": "_dns_1_ErrorResponse",
        "RRSetRoutingPolicyPrimaryBackupPolicyIn": "_dns_2_RRSetRoutingPolicyPrimaryBackupPolicyIn",
        "RRSetRoutingPolicyPrimaryBackupPolicyOut": "_dns_3_RRSetRoutingPolicyPrimaryBackupPolicyOut",
        "PoliciesPatchResponseIn": "_dns_4_PoliciesPatchResponseIn",
        "PoliciesPatchResponseOut": "_dns_5_PoliciesPatchResponseOut",
        "GoogleIamV1BindingIn": "_dns_6_GoogleIamV1BindingIn",
        "GoogleIamV1BindingOut": "_dns_7_GoogleIamV1BindingOut",
        "ManagedZoneCloudLoggingConfigIn": "_dns_8_ManagedZoneCloudLoggingConfigIn",
        "ManagedZoneCloudLoggingConfigOut": "_dns_9_ManagedZoneCloudLoggingConfigOut",
        "ManagedZoneForwardingConfigNameServerTargetIn": "_dns_10_ManagedZoneForwardingConfigNameServerTargetIn",
        "ManagedZoneForwardingConfigNameServerTargetOut": "_dns_11_ManagedZoneForwardingConfigNameServerTargetOut",
        "GoogleIamV1SetIamPolicyRequestIn": "_dns_12_GoogleIamV1SetIamPolicyRequestIn",
        "GoogleIamV1SetIamPolicyRequestOut": "_dns_13_GoogleIamV1SetIamPolicyRequestOut",
        "ManagedZoneServiceDirectoryConfigIn": "_dns_14_ManagedZoneServiceDirectoryConfigIn",
        "ManagedZoneServiceDirectoryConfigOut": "_dns_15_ManagedZoneServiceDirectoryConfigOut",
        "GoogleIamV1TestIamPermissionsResponseIn": "_dns_16_GoogleIamV1TestIamPermissionsResponseIn",
        "GoogleIamV1TestIamPermissionsResponseOut": "_dns_17_GoogleIamV1TestIamPermissionsResponseOut",
        "ResponseHeaderIn": "_dns_18_ResponseHeaderIn",
        "ResponseHeaderOut": "_dns_19_ResponseHeaderOut",
        "PoliciesUpdateResponseIn": "_dns_20_PoliciesUpdateResponseIn",
        "PoliciesUpdateResponseOut": "_dns_21_PoliciesUpdateResponseOut",
        "GoogleIamV1GetIamPolicyRequestIn": "_dns_22_GoogleIamV1GetIamPolicyRequestIn",
        "GoogleIamV1GetIamPolicyRequestOut": "_dns_23_GoogleIamV1GetIamPolicyRequestOut",
        "ResponsePolicyRuleLocalDataIn": "_dns_24_ResponsePolicyRuleLocalDataIn",
        "ResponsePolicyRuleLocalDataOut": "_dns_25_ResponsePolicyRuleLocalDataOut",
        "ResourceRecordSetIn": "_dns_26_ResourceRecordSetIn",
        "ResourceRecordSetOut": "_dns_27_ResourceRecordSetOut",
        "ManagedZoneForwardingConfigIn": "_dns_28_ManagedZoneForwardingConfigIn",
        "ManagedZoneForwardingConfigOut": "_dns_29_ManagedZoneForwardingConfigOut",
        "RRSetRoutingPolicyWrrPolicyIn": "_dns_30_RRSetRoutingPolicyWrrPolicyIn",
        "RRSetRoutingPolicyWrrPolicyOut": "_dns_31_RRSetRoutingPolicyWrrPolicyOut",
        "ManagedZonePeeringConfigTargetNetworkIn": "_dns_32_ManagedZonePeeringConfigTargetNetworkIn",
        "ManagedZonePeeringConfigTargetNetworkOut": "_dns_33_ManagedZonePeeringConfigTargetNetworkOut",
        "ManagedZoneOperationsListResponseIn": "_dns_34_ManagedZoneOperationsListResponseIn",
        "ManagedZoneOperationsListResponseOut": "_dns_35_ManagedZoneOperationsListResponseOut",
        "RRSetRoutingPolicyGeoPolicyIn": "_dns_36_RRSetRoutingPolicyGeoPolicyIn",
        "RRSetRoutingPolicyGeoPolicyOut": "_dns_37_RRSetRoutingPolicyGeoPolicyOut",
        "ResponsePoliciesPatchResponseIn": "_dns_38_ResponsePoliciesPatchResponseIn",
        "ResponsePoliciesPatchResponseOut": "_dns_39_ResponsePoliciesPatchResponseOut",
        "ResponsePolicyGKEClusterIn": "_dns_40_ResponsePolicyGKEClusterIn",
        "ResponsePolicyGKEClusterOut": "_dns_41_ResponsePolicyGKEClusterOut",
        "GoogleIamV1TestIamPermissionsRequestIn": "_dns_42_GoogleIamV1TestIamPermissionsRequestIn",
        "GoogleIamV1TestIamPermissionsRequestOut": "_dns_43_GoogleIamV1TestIamPermissionsRequestOut",
        "RRSetRoutingPolicyHealthCheckTargetsIn": "_dns_44_RRSetRoutingPolicyHealthCheckTargetsIn",
        "RRSetRoutingPolicyHealthCheckTargetsOut": "_dns_45_RRSetRoutingPolicyHealthCheckTargetsOut",
        "PoliciesListResponseIn": "_dns_46_PoliciesListResponseIn",
        "PoliciesListResponseOut": "_dns_47_PoliciesListResponseOut",
        "GoogleIamV1PolicyIn": "_dns_48_GoogleIamV1PolicyIn",
        "GoogleIamV1PolicyOut": "_dns_49_GoogleIamV1PolicyOut",
        "ResourceRecordSetsDeleteResponseIn": "_dns_50_ResourceRecordSetsDeleteResponseIn",
        "ResourceRecordSetsDeleteResponseOut": "_dns_51_ResourceRecordSetsDeleteResponseOut",
        "ChangeIn": "_dns_52_ChangeIn",
        "ChangeOut": "_dns_53_ChangeOut",
        "ManagedZoneIn": "_dns_54_ManagedZoneIn",
        "ManagedZoneOut": "_dns_55_ManagedZoneOut",
        "ExprIn": "_dns_56_ExprIn",
        "ExprOut": "_dns_57_ExprOut",
        "DnsKeySpecIn": "_dns_58_DnsKeySpecIn",
        "DnsKeySpecOut": "_dns_59_DnsKeySpecOut",
        "GoogleIamV1AuditLogConfigIn": "_dns_60_GoogleIamV1AuditLogConfigIn",
        "GoogleIamV1AuditLogConfigOut": "_dns_61_GoogleIamV1AuditLogConfigOut",
        "ManagedZoneDnsSecConfigIn": "_dns_62_ManagedZoneDnsSecConfigIn",
        "ManagedZoneDnsSecConfigOut": "_dns_63_ManagedZoneDnsSecConfigOut",
        "ChangesListResponseIn": "_dns_64_ChangesListResponseIn",
        "ChangesListResponseOut": "_dns_65_ChangesListResponseOut",
        "ManagedZonePeeringConfigIn": "_dns_66_ManagedZonePeeringConfigIn",
        "ManagedZonePeeringConfigOut": "_dns_67_ManagedZonePeeringConfigOut",
        "RRSetRoutingPolicyGeoPolicyGeoPolicyItemIn": "_dns_68_RRSetRoutingPolicyGeoPolicyGeoPolicyItemIn",
        "RRSetRoutingPolicyGeoPolicyGeoPolicyItemOut": "_dns_69_RRSetRoutingPolicyGeoPolicyGeoPolicyItemOut",
        "DnsKeyIn": "_dns_70_DnsKeyIn",
        "DnsKeyOut": "_dns_71_DnsKeyOut",
        "ProjectIn": "_dns_72_ProjectIn",
        "ProjectOut": "_dns_73_ProjectOut",
        "QuotaIn": "_dns_74_QuotaIn",
        "QuotaOut": "_dns_75_QuotaOut",
        "ManagedZoneReverseLookupConfigIn": "_dns_76_ManagedZoneReverseLookupConfigIn",
        "ManagedZoneReverseLookupConfigOut": "_dns_77_ManagedZoneReverseLookupConfigOut",
        "RRSetRoutingPolicyLoadBalancerTargetIn": "_dns_78_RRSetRoutingPolicyLoadBalancerTargetIn",
        "RRSetRoutingPolicyLoadBalancerTargetOut": "_dns_79_RRSetRoutingPolicyLoadBalancerTargetOut",
        "PolicyAlternativeNameServerConfigTargetNameServerIn": "_dns_80_PolicyAlternativeNameServerConfigTargetNameServerIn",
        "PolicyAlternativeNameServerConfigTargetNameServerOut": "_dns_81_PolicyAlternativeNameServerConfigTargetNameServerOut",
        "PolicyIn": "_dns_82_PolicyIn",
        "PolicyOut": "_dns_83_PolicyOut",
        "ManagedZonesListResponseIn": "_dns_84_ManagedZonesListResponseIn",
        "ManagedZonesListResponseOut": "_dns_85_ManagedZonesListResponseOut",
        "ResourceRecordSetsListResponseIn": "_dns_86_ResourceRecordSetsListResponseIn",
        "ResourceRecordSetsListResponseOut": "_dns_87_ResourceRecordSetsListResponseOut",
        "OperationManagedZoneContextIn": "_dns_88_OperationManagedZoneContextIn",
        "OperationManagedZoneContextOut": "_dns_89_OperationManagedZoneContextOut",
        "ResponsePolicyNetworkIn": "_dns_90_ResponsePolicyNetworkIn",
        "ResponsePolicyNetworkOut": "_dns_91_ResponsePolicyNetworkOut",
        "ManagedZonePrivateVisibilityConfigGKEClusterIn": "_dns_92_ManagedZonePrivateVisibilityConfigGKEClusterIn",
        "ManagedZonePrivateVisibilityConfigGKEClusterOut": "_dns_93_ManagedZonePrivateVisibilityConfigGKEClusterOut",
        "ManagedZonePrivateVisibilityConfigIn": "_dns_94_ManagedZonePrivateVisibilityConfigIn",
        "ManagedZonePrivateVisibilityConfigOut": "_dns_95_ManagedZonePrivateVisibilityConfigOut",
        "GoogleIamV1GetPolicyOptionsIn": "_dns_96_GoogleIamV1GetPolicyOptionsIn",
        "GoogleIamV1GetPolicyOptionsOut": "_dns_97_GoogleIamV1GetPolicyOptionsOut",
        "ResponsePoliciesListResponseIn": "_dns_98_ResponsePoliciesListResponseIn",
        "ResponsePoliciesListResponseOut": "_dns_99_ResponsePoliciesListResponseOut",
        "DnsKeysListResponseIn": "_dns_100_DnsKeysListResponseIn",
        "DnsKeysListResponseOut": "_dns_101_DnsKeysListResponseOut",
        "OperationIn": "_dns_102_OperationIn",
        "OperationOut": "_dns_103_OperationOut",
        "RRSetRoutingPolicyWrrPolicyWrrPolicyItemIn": "_dns_104_RRSetRoutingPolicyWrrPolicyWrrPolicyItemIn",
        "RRSetRoutingPolicyWrrPolicyWrrPolicyItemOut": "_dns_105_RRSetRoutingPolicyWrrPolicyWrrPolicyItemOut",
        "DnsKeyDigestIn": "_dns_106_DnsKeyDigestIn",
        "DnsKeyDigestOut": "_dns_107_DnsKeyDigestOut",
        "PolicyAlternativeNameServerConfigIn": "_dns_108_PolicyAlternativeNameServerConfigIn",
        "PolicyAlternativeNameServerConfigOut": "_dns_109_PolicyAlternativeNameServerConfigOut",
        "ResponsePoliciesUpdateResponseIn": "_dns_110_ResponsePoliciesUpdateResponseIn",
        "ResponsePoliciesUpdateResponseOut": "_dns_111_ResponsePoliciesUpdateResponseOut",
        "ResponsePolicyRulesListResponseIn": "_dns_112_ResponsePolicyRulesListResponseIn",
        "ResponsePolicyRulesListResponseOut": "_dns_113_ResponsePolicyRulesListResponseOut",
        "PolicyNetworkIn": "_dns_114_PolicyNetworkIn",
        "PolicyNetworkOut": "_dns_115_PolicyNetworkOut",
        "RRSetRoutingPolicyIn": "_dns_116_RRSetRoutingPolicyIn",
        "RRSetRoutingPolicyOut": "_dns_117_RRSetRoutingPolicyOut",
        "ManagedZonePrivateVisibilityConfigNetworkIn": "_dns_118_ManagedZonePrivateVisibilityConfigNetworkIn",
        "ManagedZonePrivateVisibilityConfigNetworkOut": "_dns_119_ManagedZonePrivateVisibilityConfigNetworkOut",
        "OperationDnsKeyContextIn": "_dns_120_OperationDnsKeyContextIn",
        "OperationDnsKeyContextOut": "_dns_121_OperationDnsKeyContextOut",
        "ResponsePolicyRulesUpdateResponseIn": "_dns_122_ResponsePolicyRulesUpdateResponseIn",
        "ResponsePolicyRulesUpdateResponseOut": "_dns_123_ResponsePolicyRulesUpdateResponseOut",
        "ResponsePolicyRuleIn": "_dns_124_ResponsePolicyRuleIn",
        "ResponsePolicyRuleOut": "_dns_125_ResponsePolicyRuleOut",
        "ManagedZoneServiceDirectoryConfigNamespaceIn": "_dns_126_ManagedZoneServiceDirectoryConfigNamespaceIn",
        "ManagedZoneServiceDirectoryConfigNamespaceOut": "_dns_127_ManagedZoneServiceDirectoryConfigNamespaceOut",
        "ResponsePolicyRulesPatchResponseIn": "_dns_128_ResponsePolicyRulesPatchResponseIn",
        "ResponsePolicyRulesPatchResponseOut": "_dns_129_ResponsePolicyRulesPatchResponseOut",
        "ResponsePolicyIn": "_dns_130_ResponsePolicyIn",
        "ResponsePolicyOut": "_dns_131_ResponsePolicyOut",
        "GoogleIamV1AuditConfigIn": "_dns_132_GoogleIamV1AuditConfigIn",
        "GoogleIamV1AuditConfigOut": "_dns_133_GoogleIamV1AuditConfigOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["RRSetRoutingPolicyPrimaryBackupPolicyIn"] = t.struct(
        {
            "backupGeoTargets": t.proxy(
                renames["RRSetRoutingPolicyGeoPolicyIn"]
            ).optional(),
            "kind": t.string(),
            "trickleTraffic": t.number().optional(),
            "primaryTargets": t.proxy(
                renames["RRSetRoutingPolicyHealthCheckTargetsIn"]
            ),
        }
    ).named(renames["RRSetRoutingPolicyPrimaryBackupPolicyIn"])
    types["RRSetRoutingPolicyPrimaryBackupPolicyOut"] = t.struct(
        {
            "backupGeoTargets": t.proxy(
                renames["RRSetRoutingPolicyGeoPolicyOut"]
            ).optional(),
            "kind": t.string(),
            "trickleTraffic": t.number().optional(),
            "primaryTargets": t.proxy(
                renames["RRSetRoutingPolicyHealthCheckTargetsOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RRSetRoutingPolicyPrimaryBackupPolicyOut"])
    types["PoliciesPatchResponseIn"] = t.struct(
        {
            "header": t.proxy(renames["ResponseHeaderIn"]),
            "policy": t.proxy(renames["PolicyIn"]),
        }
    ).named(renames["PoliciesPatchResponseIn"])
    types["PoliciesPatchResponseOut"] = t.struct(
        {
            "header": t.proxy(renames["ResponseHeaderOut"]),
            "policy": t.proxy(renames["PolicyOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PoliciesPatchResponseOut"])
    types["GoogleIamV1BindingIn"] = t.struct(
        {
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "members": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleIamV1BindingIn"])
    types["GoogleIamV1BindingOut"] = t.struct(
        {
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "members": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1BindingOut"])
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
    types["ManagedZoneForwardingConfigNameServerTargetIn"] = t.struct(
        {
            "ipv6Address": t.string().optional(),
            "forwardingPath": t.string().optional(),
            "kind": t.string(),
            "ipv4Address": t.string().optional(),
        }
    ).named(renames["ManagedZoneForwardingConfigNameServerTargetIn"])
    types["ManagedZoneForwardingConfigNameServerTargetOut"] = t.struct(
        {
            "ipv6Address": t.string().optional(),
            "forwardingPath": t.string().optional(),
            "kind": t.string(),
            "ipv4Address": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedZoneForwardingConfigNameServerTargetOut"])
    types["GoogleIamV1SetIamPolicyRequestIn"] = t.struct(
        {
            "policy": t.proxy(renames["GoogleIamV1PolicyIn"]).optional(),
            "updateMask": t.string().optional(),
        }
    ).named(renames["GoogleIamV1SetIamPolicyRequestIn"])
    types["GoogleIamV1SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["GoogleIamV1PolicyOut"]).optional(),
            "updateMask": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1SetIamPolicyRequestOut"])
    types["ManagedZoneServiceDirectoryConfigIn"] = t.struct(
        {
            "namespace": t.proxy(
                renames["ManagedZoneServiceDirectoryConfigNamespaceIn"]
            ).optional(),
            "kind": t.string(),
        }
    ).named(renames["ManagedZoneServiceDirectoryConfigIn"])
    types["ManagedZoneServiceDirectoryConfigOut"] = t.struct(
        {
            "namespace": t.proxy(
                renames["ManagedZoneServiceDirectoryConfigNamespaceOut"]
            ).optional(),
            "kind": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedZoneServiceDirectoryConfigOut"])
    types["GoogleIamV1TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["GoogleIamV1TestIamPermissionsResponseIn"])
    types["GoogleIamV1TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1TestIamPermissionsResponseOut"])
    types["ResponseHeaderIn"] = t.struct({"operationId": t.string().optional()}).named(
        renames["ResponseHeaderIn"]
    )
    types["ResponseHeaderOut"] = t.struct(
        {
            "operationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResponseHeaderOut"])
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
    types["GoogleIamV1GetIamPolicyRequestIn"] = t.struct(
        {"options": t.proxy(renames["GoogleIamV1GetPolicyOptionsIn"]).optional()}
    ).named(renames["GoogleIamV1GetIamPolicyRequestIn"])
    types["GoogleIamV1GetIamPolicyRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["GoogleIamV1GetPolicyOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1GetIamPolicyRequestOut"])
    types["ResponsePolicyRuleLocalDataIn"] = t.struct(
        {"localDatas": t.array(t.proxy(renames["ResourceRecordSetIn"])).optional()}
    ).named(renames["ResponsePolicyRuleLocalDataIn"])
    types["ResponsePolicyRuleLocalDataOut"] = t.struct(
        {
            "localDatas": t.array(t.proxy(renames["ResourceRecordSetOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResponsePolicyRuleLocalDataOut"])
    types["ResourceRecordSetIn"] = t.struct(
        {
            "type": t.string().optional(),
            "signatureRrdatas": t.array(t.string()).optional(),
            "kind": t.string(),
            "routingPolicy": t.proxy(renames["RRSetRoutingPolicyIn"]).optional(),
            "rrdatas": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "ttl": t.integer().optional(),
        }
    ).named(renames["ResourceRecordSetIn"])
    types["ResourceRecordSetOut"] = t.struct(
        {
            "type": t.string().optional(),
            "signatureRrdatas": t.array(t.string()).optional(),
            "kind": t.string(),
            "routingPolicy": t.proxy(renames["RRSetRoutingPolicyOut"]).optional(),
            "rrdatas": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "ttl": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceRecordSetOut"])
    types["ManagedZoneForwardingConfigIn"] = t.struct(
        {
            "kind": t.string(),
            "targetNameServers": t.array(
                t.proxy(renames["ManagedZoneForwardingConfigNameServerTargetIn"])
            ).optional(),
        }
    ).named(renames["ManagedZoneForwardingConfigIn"])
    types["ManagedZoneForwardingConfigOut"] = t.struct(
        {
            "kind": t.string(),
            "targetNameServers": t.array(
                t.proxy(renames["ManagedZoneForwardingConfigNameServerTargetOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedZoneForwardingConfigOut"])
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
    types["ManagedZonePeeringConfigTargetNetworkIn"] = t.struct(
        {
            "deactivateTime": t.string().optional(),
            "kind": t.string(),
            "networkUrl": t.string().optional(),
        }
    ).named(renames["ManagedZonePeeringConfigTargetNetworkIn"])
    types["ManagedZonePeeringConfigTargetNetworkOut"] = t.struct(
        {
            "deactivateTime": t.string().optional(),
            "kind": t.string(),
            "networkUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedZonePeeringConfigTargetNetworkOut"])
    types["ManagedZoneOperationsListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(t.proxy(renames["OperationIn"])).optional(),
            "header": t.proxy(renames["ResponseHeaderIn"]),
            "kind": t.string().optional(),
        }
    ).named(renames["ManagedZoneOperationsListResponseIn"])
    types["ManagedZoneOperationsListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(t.proxy(renames["OperationOut"])).optional(),
            "header": t.proxy(renames["ResponseHeaderOut"]),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedZoneOperationsListResponseOut"])
    types["RRSetRoutingPolicyGeoPolicyIn"] = t.struct(
        {
            "kind": t.string(),
            "items": t.array(
                t.proxy(renames["RRSetRoutingPolicyGeoPolicyGeoPolicyItemIn"])
            ).optional(),
            "enableFencing": t.boolean().optional(),
        }
    ).named(renames["RRSetRoutingPolicyGeoPolicyIn"])
    types["RRSetRoutingPolicyGeoPolicyOut"] = t.struct(
        {
            "kind": t.string(),
            "items": t.array(
                t.proxy(renames["RRSetRoutingPolicyGeoPolicyGeoPolicyItemOut"])
            ).optional(),
            "enableFencing": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RRSetRoutingPolicyGeoPolicyOut"])
    types["ResponsePoliciesPatchResponseIn"] = t.struct(
        {
            "responsePolicy": t.proxy(renames["ResponsePolicyIn"]),
            "header": t.proxy(renames["ResponseHeaderIn"]),
        }
    ).named(renames["ResponsePoliciesPatchResponseIn"])
    types["ResponsePoliciesPatchResponseOut"] = t.struct(
        {
            "responsePolicy": t.proxy(renames["ResponsePolicyOut"]),
            "header": t.proxy(renames["ResponseHeaderOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResponsePoliciesPatchResponseOut"])
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
    types["GoogleIamV1TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["GoogleIamV1TestIamPermissionsRequestIn"])
    types["GoogleIamV1TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1TestIamPermissionsRequestOut"])
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
    types["PoliciesListResponseIn"] = t.struct(
        {
            "policies": t.array(t.proxy(renames["PolicyIn"])).optional(),
            "kind": t.string().optional(),
            "header": t.proxy(renames["ResponseHeaderIn"]),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["PoliciesListResponseIn"])
    types["PoliciesListResponseOut"] = t.struct(
        {
            "policies": t.array(t.proxy(renames["PolicyOut"])).optional(),
            "kind": t.string().optional(),
            "header": t.proxy(renames["ResponseHeaderOut"]),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PoliciesListResponseOut"])
    types["GoogleIamV1PolicyIn"] = t.struct(
        {
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["GoogleIamV1BindingIn"])).optional(),
            "etag": t.string().optional(),
            "auditConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditConfigIn"])
            ).optional(),
        }
    ).named(renames["GoogleIamV1PolicyIn"])
    types["GoogleIamV1PolicyOut"] = t.struct(
        {
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["GoogleIamV1BindingOut"])).optional(),
            "etag": t.string().optional(),
            "auditConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1PolicyOut"])
    types["ResourceRecordSetsDeleteResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ResourceRecordSetsDeleteResponseIn"])
    types["ResourceRecordSetsDeleteResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ResourceRecordSetsDeleteResponseOut"])
    types["ChangeIn"] = t.struct(
        {
            "id": t.string().optional(),
            "additions": t.array(t.proxy(renames["ResourceRecordSetIn"])).optional(),
            "isServing": t.boolean().optional(),
            "status": t.string().optional(),
            "startTime": t.string().optional(),
            "kind": t.string(),
            "deletions": t.array(t.proxy(renames["ResourceRecordSetIn"])).optional(),
        }
    ).named(renames["ChangeIn"])
    types["ChangeOut"] = t.struct(
        {
            "id": t.string().optional(),
            "additions": t.array(t.proxy(renames["ResourceRecordSetOut"])).optional(),
            "isServing": t.boolean().optional(),
            "status": t.string().optional(),
            "startTime": t.string().optional(),
            "kind": t.string(),
            "deletions": t.array(t.proxy(renames["ResourceRecordSetOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChangeOut"])
    types["ManagedZoneIn"] = t.struct(
        {
            "kind": t.string(),
            "serviceDirectoryConfig": t.proxy(
                renames["ManagedZoneServiceDirectoryConfigIn"]
            ).optional(),
            "name": t.string().optional(),
            "privateVisibilityConfig": t.proxy(
                renames["ManagedZonePrivateVisibilityConfigIn"]
            ).optional(),
            "nameServerSet": t.string().optional(),
            "dnssecConfig": t.proxy(renames["ManagedZoneDnsSecConfigIn"]).optional(),
            "description": t.string().optional(),
            "creationTime": t.string().optional(),
            "visibility": t.string().optional(),
            "id": t.string().optional(),
            "cloudLoggingConfig": t.proxy(renames["ManagedZoneCloudLoggingConfigIn"]),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "reverseLookupConfig": t.proxy(
                renames["ManagedZoneReverseLookupConfigIn"]
            ).optional(),
            "nameServers": t.array(t.string()).optional(),
            "peeringConfig": t.proxy(renames["ManagedZonePeeringConfigIn"]).optional(),
            "forwardingConfig": t.proxy(
                renames["ManagedZoneForwardingConfigIn"]
            ).optional(),
            "dnsName": t.string().optional(),
        }
    ).named(renames["ManagedZoneIn"])
    types["ManagedZoneOut"] = t.struct(
        {
            "kind": t.string(),
            "serviceDirectoryConfig": t.proxy(
                renames["ManagedZoneServiceDirectoryConfigOut"]
            ).optional(),
            "name": t.string().optional(),
            "privateVisibilityConfig": t.proxy(
                renames["ManagedZonePrivateVisibilityConfigOut"]
            ).optional(),
            "nameServerSet": t.string().optional(),
            "dnssecConfig": t.proxy(renames["ManagedZoneDnsSecConfigOut"]).optional(),
            "description": t.string().optional(),
            "creationTime": t.string().optional(),
            "visibility": t.string().optional(),
            "id": t.string().optional(),
            "cloudLoggingConfig": t.proxy(renames["ManagedZoneCloudLoggingConfigOut"]),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "reverseLookupConfig": t.proxy(
                renames["ManagedZoneReverseLookupConfigOut"]
            ).optional(),
            "nameServers": t.array(t.string()).optional(),
            "peeringConfig": t.proxy(renames["ManagedZonePeeringConfigOut"]).optional(),
            "forwardingConfig": t.proxy(
                renames["ManagedZoneForwardingConfigOut"]
            ).optional(),
            "dnsName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedZoneOut"])
    types["ExprIn"] = t.struct(
        {
            "description": t.string().optional(),
            "location": t.string().optional(),
            "title": t.string().optional(),
            "expression": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "description": t.string().optional(),
            "location": t.string().optional(),
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["DnsKeySpecIn"] = t.struct(
        {
            "keyType": t.string().optional(),
            "algorithm": t.string().optional(),
            "keyLength": t.integer().optional(),
            "kind": t.string(),
        }
    ).named(renames["DnsKeySpecIn"])
    types["DnsKeySpecOut"] = t.struct(
        {
            "keyType": t.string().optional(),
            "algorithm": t.string().optional(),
            "keyLength": t.integer().optional(),
            "kind": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DnsKeySpecOut"])
    types["GoogleIamV1AuditLogConfigIn"] = t.struct(
        {
            "logType": t.string().optional(),
            "exemptedMembers": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleIamV1AuditLogConfigIn"])
    types["GoogleIamV1AuditLogConfigOut"] = t.struct(
        {
            "logType": t.string().optional(),
            "exemptedMembers": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1AuditLogConfigOut"])
    types["ManagedZoneDnsSecConfigIn"] = t.struct(
        {
            "kind": t.string(),
            "state": t.string().optional(),
            "nonExistence": t.string().optional(),
            "defaultKeySpecs": t.array(t.proxy(renames["DnsKeySpecIn"])).optional(),
        }
    ).named(renames["ManagedZoneDnsSecConfigIn"])
    types["ManagedZoneDnsSecConfigOut"] = t.struct(
        {
            "kind": t.string(),
            "state": t.string().optional(),
            "nonExistence": t.string().optional(),
            "defaultKeySpecs": t.array(t.proxy(renames["DnsKeySpecOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedZoneDnsSecConfigOut"])
    types["ChangesListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "header": t.proxy(renames["ResponseHeaderIn"]),
            "changes": t.array(t.proxy(renames["ChangeIn"])).optional(),
        }
    ).named(renames["ChangesListResponseIn"])
    types["ChangesListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "header": t.proxy(renames["ResponseHeaderOut"]),
            "changes": t.array(t.proxy(renames["ChangeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChangesListResponseOut"])
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
    types["RRSetRoutingPolicyGeoPolicyGeoPolicyItemIn"] = t.struct(
        {
            "location": t.string().optional(),
            "kind": t.string(),
            "rrdatas": t.array(t.string()),
            "healthCheckedTargets": t.proxy(
                renames["RRSetRoutingPolicyHealthCheckTargetsIn"]
            ).optional(),
            "signatureRrdatas": t.array(t.string()).optional(),
        }
    ).named(renames["RRSetRoutingPolicyGeoPolicyGeoPolicyItemIn"])
    types["RRSetRoutingPolicyGeoPolicyGeoPolicyItemOut"] = t.struct(
        {
            "location": t.string().optional(),
            "kind": t.string(),
            "rrdatas": t.array(t.string()),
            "healthCheckedTargets": t.proxy(
                renames["RRSetRoutingPolicyHealthCheckTargetsOut"]
            ).optional(),
            "signatureRrdatas": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RRSetRoutingPolicyGeoPolicyGeoPolicyItemOut"])
    types["DnsKeyIn"] = t.struct(
        {
            "description": t.string().optional(),
            "algorithm": t.string().optional(),
            "keyTag": t.integer().optional(),
            "publicKey": t.string().optional(),
            "creationTime": t.string().optional(),
            "id": t.string().optional(),
            "type": t.string().optional(),
            "isActive": t.boolean().optional(),
            "digests": t.array(t.proxy(renames["DnsKeyDigestIn"])).optional(),
            "kind": t.string(),
            "keyLength": t.integer().optional(),
        }
    ).named(renames["DnsKeyIn"])
    types["DnsKeyOut"] = t.struct(
        {
            "description": t.string().optional(),
            "algorithm": t.string().optional(),
            "keyTag": t.integer().optional(),
            "publicKey": t.string().optional(),
            "creationTime": t.string().optional(),
            "id": t.string().optional(),
            "type": t.string().optional(),
            "isActive": t.boolean().optional(),
            "digests": t.array(t.proxy(renames["DnsKeyDigestOut"])).optional(),
            "kind": t.string(),
            "keyLength": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DnsKeyOut"])
    types["ProjectIn"] = t.struct(
        {
            "id": t.string().optional(),
            "number": t.string().optional(),
            "quota": t.proxy(renames["QuotaIn"]).optional(),
            "kind": t.string(),
        }
    ).named(renames["ProjectIn"])
    types["ProjectOut"] = t.struct(
        {
            "id": t.string().optional(),
            "number": t.string().optional(),
            "quota": t.proxy(renames["QuotaOut"]).optional(),
            "kind": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProjectOut"])
    types["QuotaIn"] = t.struct(
        {
            "kind": t.string(),
            "itemsPerRoutingPolicy": t.integer().optional(),
            "managedZones": t.integer().optional(),
            "targetNameServersPerPolicy": t.integer().optional(),
            "whitelistedKeySpecs": t.array(t.proxy(renames["DnsKeySpecIn"])).optional(),
            "networksPerPolicy": t.integer().optional(),
            "peeringZonesPerTargetNetwork": t.integer().optional(),
            "responsePolicies": t.integer().optional(),
            "dnsKeysPerManagedZone": t.integer().optional(),
            "totalRrdataSizePerChange": t.integer().optional(),
            "rrsetsPerManagedZone": t.integer().optional(),
            "networksPerResponsePolicy": t.integer().optional(),
            "managedZonesPerGkeCluster": t.integer().optional(),
            "gkeClustersPerResponsePolicy": t.integer().optional(),
            "policies": t.integer().optional(),
            "gkeClustersPerPolicy": t.integer().optional(),
            "gkeClustersPerManagedZone": t.integer().optional(),
            "responsePolicyRulesPerResponsePolicy": t.integer().optional(),
            "resourceRecordsPerRrset": t.integer().optional(),
            "rrsetDeletionsPerChange": t.integer().optional(),
            "managedZonesPerNetwork": t.integer().optional(),
            "networksPerManagedZone": t.integer().optional(),
            "targetNameServersPerManagedZone": t.integer().optional(),
            "rrsetAdditionsPerChange": t.integer().optional(),
        }
    ).named(renames["QuotaIn"])
    types["QuotaOut"] = t.struct(
        {
            "kind": t.string(),
            "itemsPerRoutingPolicy": t.integer().optional(),
            "managedZones": t.integer().optional(),
            "targetNameServersPerPolicy": t.integer().optional(),
            "whitelistedKeySpecs": t.array(
                t.proxy(renames["DnsKeySpecOut"])
            ).optional(),
            "networksPerPolicy": t.integer().optional(),
            "peeringZonesPerTargetNetwork": t.integer().optional(),
            "responsePolicies": t.integer().optional(),
            "dnsKeysPerManagedZone": t.integer().optional(),
            "totalRrdataSizePerChange": t.integer().optional(),
            "rrsetsPerManagedZone": t.integer().optional(),
            "networksPerResponsePolicy": t.integer().optional(),
            "managedZonesPerGkeCluster": t.integer().optional(),
            "gkeClustersPerResponsePolicy": t.integer().optional(),
            "policies": t.integer().optional(),
            "gkeClustersPerPolicy": t.integer().optional(),
            "gkeClustersPerManagedZone": t.integer().optional(),
            "responsePolicyRulesPerResponsePolicy": t.integer().optional(),
            "resourceRecordsPerRrset": t.integer().optional(),
            "rrsetDeletionsPerChange": t.integer().optional(),
            "managedZonesPerNetwork": t.integer().optional(),
            "networksPerManagedZone": t.integer().optional(),
            "targetNameServersPerManagedZone": t.integer().optional(),
            "rrsetAdditionsPerChange": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuotaOut"])
    types["ManagedZoneReverseLookupConfigIn"] = t.struct({"kind": t.string()}).named(
        renames["ManagedZoneReverseLookupConfigIn"]
    )
    types["ManagedZoneReverseLookupConfigOut"] = t.struct(
        {"kind": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ManagedZoneReverseLookupConfigOut"])
    types["RRSetRoutingPolicyLoadBalancerTargetIn"] = t.struct(
        {
            "ipAddress": t.string().optional(),
            "kind": t.string(),
            "networkUrl": t.string().optional(),
            "port": t.string().optional(),
            "project": t.string().optional(),
            "region": t.string().optional(),
            "loadBalancerType": t.string().optional(),
            "ipProtocol": t.string(),
        }
    ).named(renames["RRSetRoutingPolicyLoadBalancerTargetIn"])
    types["RRSetRoutingPolicyLoadBalancerTargetOut"] = t.struct(
        {
            "ipAddress": t.string().optional(),
            "kind": t.string(),
            "networkUrl": t.string().optional(),
            "port": t.string().optional(),
            "project": t.string().optional(),
            "region": t.string().optional(),
            "loadBalancerType": t.string().optional(),
            "ipProtocol": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RRSetRoutingPolicyLoadBalancerTargetOut"])
    types["PolicyAlternativeNameServerConfigTargetNameServerIn"] = t.struct(
        {
            "kind": t.string(),
            "forwardingPath": t.string().optional(),
            "ipv4Address": t.string().optional(),
            "ipv6Address": t.string().optional(),
        }
    ).named(renames["PolicyAlternativeNameServerConfigTargetNameServerIn"])
    types["PolicyAlternativeNameServerConfigTargetNameServerOut"] = t.struct(
        {
            "kind": t.string(),
            "forwardingPath": t.string().optional(),
            "ipv4Address": t.string().optional(),
            "ipv6Address": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyAlternativeNameServerConfigTargetNameServerOut"])
    types["PolicyIn"] = t.struct(
        {
            "description": t.string().optional(),
            "kind": t.string(),
            "alternativeNameServerConfig": t.proxy(
                renames["PolicyAlternativeNameServerConfigIn"]
            ).optional(),
            "networks": t.array(t.proxy(renames["PolicyNetworkIn"])).optional(),
            "name": t.string().optional(),
            "enableLogging": t.boolean().optional(),
            "enableInboundForwarding": t.boolean().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "description": t.string().optional(),
            "kind": t.string(),
            "alternativeNameServerConfig": t.proxy(
                renames["PolicyAlternativeNameServerConfigOut"]
            ).optional(),
            "networks": t.array(t.proxy(renames["PolicyNetworkOut"])).optional(),
            "name": t.string().optional(),
            "enableLogging": t.boolean().optional(),
            "enableInboundForwarding": t.boolean().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["ManagedZonesListResponseIn"] = t.struct(
        {
            "managedZones": t.array(t.proxy(renames["ManagedZoneIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "header": t.proxy(renames["ResponseHeaderIn"]),
        }
    ).named(renames["ManagedZonesListResponseIn"])
    types["ManagedZonesListResponseOut"] = t.struct(
        {
            "managedZones": t.array(t.proxy(renames["ManagedZoneOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "header": t.proxy(renames["ResponseHeaderOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedZonesListResponseOut"])
    types["ResourceRecordSetsListResponseIn"] = t.struct(
        {
            "rrsets": t.array(t.proxy(renames["ResourceRecordSetIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "header": t.proxy(renames["ResponseHeaderIn"]),
        }
    ).named(renames["ResourceRecordSetsListResponseIn"])
    types["ResourceRecordSetsListResponseOut"] = t.struct(
        {
            "rrsets": t.array(t.proxy(renames["ResourceRecordSetOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "header": t.proxy(renames["ResponseHeaderOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceRecordSetsListResponseOut"])
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
    types["ResponsePolicyNetworkIn"] = t.struct(
        {"networkUrl": t.string().optional(), "kind": t.string()}
    ).named(renames["ResponsePolicyNetworkIn"])
    types["ResponsePolicyNetworkOut"] = t.struct(
        {
            "networkUrl": t.string().optional(),
            "kind": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResponsePolicyNetworkOut"])
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
    types["ManagedZonePrivateVisibilityConfigIn"] = t.struct(
        {
            "networks": t.array(
                t.proxy(renames["ManagedZonePrivateVisibilityConfigNetworkIn"])
            ).optional(),
            "gkeClusters": t.array(
                t.proxy(renames["ManagedZonePrivateVisibilityConfigGKEClusterIn"])
            ).optional(),
            "kind": t.string(),
        }
    ).named(renames["ManagedZonePrivateVisibilityConfigIn"])
    types["ManagedZonePrivateVisibilityConfigOut"] = t.struct(
        {
            "networks": t.array(
                t.proxy(renames["ManagedZonePrivateVisibilityConfigNetworkOut"])
            ).optional(),
            "gkeClusters": t.array(
                t.proxy(renames["ManagedZonePrivateVisibilityConfigGKEClusterOut"])
            ).optional(),
            "kind": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedZonePrivateVisibilityConfigOut"])
    types["GoogleIamV1GetPolicyOptionsIn"] = t.struct(
        {"requestedPolicyVersion": t.integer().optional()}
    ).named(renames["GoogleIamV1GetPolicyOptionsIn"])
    types["GoogleIamV1GetPolicyOptionsOut"] = t.struct(
        {
            "requestedPolicyVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1GetPolicyOptionsOut"])
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
    types["DnsKeysListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "header": t.proxy(renames["ResponseHeaderIn"]),
            "dnsKeys": t.array(t.proxy(renames["DnsKeyIn"])).optional(),
        }
    ).named(renames["DnsKeysListResponseIn"])
    types["DnsKeysListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "header": t.proxy(renames["ResponseHeaderOut"]),
            "dnsKeys": t.array(t.proxy(renames["DnsKeyOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DnsKeysListResponseOut"])
    types["OperationIn"] = t.struct(
        {
            "user": t.string().optional(),
            "dnsKeyContext": t.proxy(renames["OperationDnsKeyContextIn"]).optional(),
            "id": t.string().optional(),
            "type": t.string().optional(),
            "startTime": t.string().optional(),
            "status": t.string().optional(),
            "zoneContext": t.proxy(renames["OperationManagedZoneContextIn"]).optional(),
            "kind": t.string(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "user": t.string().optional(),
            "dnsKeyContext": t.proxy(renames["OperationDnsKeyContextOut"]).optional(),
            "id": t.string().optional(),
            "type": t.string().optional(),
            "startTime": t.string().optional(),
            "status": t.string().optional(),
            "zoneContext": t.proxy(
                renames["OperationManagedZoneContextOut"]
            ).optional(),
            "kind": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
    types["RRSetRoutingPolicyWrrPolicyWrrPolicyItemIn"] = t.struct(
        {
            "signatureRrdatas": t.array(t.string()).optional(),
            "rrdatas": t.array(t.string()),
            "healthCheckedTargets": t.proxy(
                renames["RRSetRoutingPolicyHealthCheckTargetsIn"]
            ).optional(),
            "kind": t.string(),
            "weight": t.number().optional(),
        }
    ).named(renames["RRSetRoutingPolicyWrrPolicyWrrPolicyItemIn"])
    types["RRSetRoutingPolicyWrrPolicyWrrPolicyItemOut"] = t.struct(
        {
            "signatureRrdatas": t.array(t.string()).optional(),
            "rrdatas": t.array(t.string()),
            "healthCheckedTargets": t.proxy(
                renames["RRSetRoutingPolicyHealthCheckTargetsOut"]
            ).optional(),
            "kind": t.string(),
            "weight": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RRSetRoutingPolicyWrrPolicyWrrPolicyItemOut"])
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
    types["ResponsePolicyRulesListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "responsePolicyRules": t.array(
                t.proxy(renames["ResponsePolicyRuleIn"])
            ).optional(),
            "header": t.proxy(renames["ResponseHeaderIn"]),
        }
    ).named(renames["ResponsePolicyRulesListResponseIn"])
    types["ResponsePolicyRulesListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "responsePolicyRules": t.array(
                t.proxy(renames["ResponsePolicyRuleOut"])
            ).optional(),
            "header": t.proxy(renames["ResponseHeaderOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResponsePolicyRulesListResponseOut"])
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
    types["RRSetRoutingPolicyIn"] = t.struct(
        {
            "geo": t.proxy(renames["RRSetRoutingPolicyGeoPolicyIn"]),
            "primaryBackup": t.proxy(
                renames["RRSetRoutingPolicyPrimaryBackupPolicyIn"]
            ),
            "kind": t.string(),
            "wrr": t.proxy(renames["RRSetRoutingPolicyWrrPolicyIn"]),
        }
    ).named(renames["RRSetRoutingPolicyIn"])
    types["RRSetRoutingPolicyOut"] = t.struct(
        {
            "geo": t.proxy(renames["RRSetRoutingPolicyGeoPolicyOut"]),
            "primaryBackup": t.proxy(
                renames["RRSetRoutingPolicyPrimaryBackupPolicyOut"]
            ),
            "kind": t.string(),
            "wrr": t.proxy(renames["RRSetRoutingPolicyWrrPolicyOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RRSetRoutingPolicyOut"])
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
            "newValue": t.proxy(renames["DnsKeyIn"]).optional(),
            "oldValue": t.proxy(renames["DnsKeyIn"]).optional(),
        }
    ).named(renames["OperationDnsKeyContextIn"])
    types["OperationDnsKeyContextOut"] = t.struct(
        {
            "newValue": t.proxy(renames["DnsKeyOut"]).optional(),
            "oldValue": t.proxy(renames["DnsKeyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationDnsKeyContextOut"])
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
    types["ResponsePolicyRuleIn"] = t.struct(
        {
            "kind": t.string(),
            "dnsName": t.string().optional(),
            "ruleName": t.string().optional(),
            "behavior": t.string().optional(),
            "localData": t.proxy(renames["ResponsePolicyRuleLocalDataIn"]).optional(),
        }
    ).named(renames["ResponsePolicyRuleIn"])
    types["ResponsePolicyRuleOut"] = t.struct(
        {
            "kind": t.string(),
            "dnsName": t.string().optional(),
            "ruleName": t.string().optional(),
            "behavior": t.string().optional(),
            "localData": t.proxy(renames["ResponsePolicyRuleLocalDataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResponsePolicyRuleOut"])
    types["ManagedZoneServiceDirectoryConfigNamespaceIn"] = t.struct(
        {
            "deletionTime": t.string().optional(),
            "namespaceUrl": t.string().optional(),
            "kind": t.string(),
        }
    ).named(renames["ManagedZoneServiceDirectoryConfigNamespaceIn"])
    types["ManagedZoneServiceDirectoryConfigNamespaceOut"] = t.struct(
        {
            "deletionTime": t.string().optional(),
            "namespaceUrl": t.string().optional(),
            "kind": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedZoneServiceDirectoryConfigNamespaceOut"])
    types["ResponsePolicyRulesPatchResponseIn"] = t.struct(
        {
            "responsePolicyRule": t.proxy(renames["ResponsePolicyRuleIn"]),
            "header": t.proxy(renames["ResponseHeaderIn"]),
        }
    ).named(renames["ResponsePolicyRulesPatchResponseIn"])
    types["ResponsePolicyRulesPatchResponseOut"] = t.struct(
        {
            "responsePolicyRule": t.proxy(renames["ResponsePolicyRuleOut"]),
            "header": t.proxy(renames["ResponseHeaderOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResponsePolicyRulesPatchResponseOut"])
    types["ResponsePolicyIn"] = t.struct(
        {
            "responsePolicyName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "gkeClusters": t.array(
                t.proxy(renames["ResponsePolicyGKEClusterIn"])
            ).optional(),
            "kind": t.string(),
            "networks": t.array(t.proxy(renames["ResponsePolicyNetworkIn"])).optional(),
            "id": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ResponsePolicyIn"])
    types["ResponsePolicyOut"] = t.struct(
        {
            "responsePolicyName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "gkeClusters": t.array(
                t.proxy(renames["ResponsePolicyGKEClusterOut"])
            ).optional(),
            "kind": t.string(),
            "networks": t.array(
                t.proxy(renames["ResponsePolicyNetworkOut"])
            ).optional(),
            "id": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResponsePolicyOut"])
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

    functions = {}
    functions["managedZoneOperationsGet"] = dns.get(
        "dns/v1/projects/{project}/managedZones/{managedZone}/operations",
        t.struct(
            {
                "project": t.string().optional(),
                "maxResults": t.integer().optional(),
                "sortBy": t.string().optional(),
                "managedZone": t.string().optional(),
                "pageToken": t.string().optional(),
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
                "project": t.string().optional(),
                "maxResults": t.integer().optional(),
                "sortBy": t.string().optional(),
                "managedZone": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ManagedZoneOperationsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["policiesCreate"] = dns.delete(
        "dns/v1/projects/{project}/policies/{policy}",
        t.struct(
            {
                "project": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "policy": t.string().optional(),
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
                "project": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "policy": t.string().optional(),
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
                "project": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "policy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["policiesUpdate"] = dns.delete(
        "dns/v1/projects/{project}/policies/{policy}",
        t.struct(
            {
                "project": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "policy": t.string().optional(),
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
                "project": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "policy": t.string().optional(),
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
                "project": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "policy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managedZonesCreate"] = dns.patch(
        "dns/v1/projects/{project}/managedZones/{managedZone}",
        t.struct(
            {
                "managedZone": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "project": t.string().optional(),
                "kind": t.string(),
                "serviceDirectoryConfig": t.proxy(
                    renames["ManagedZoneServiceDirectoryConfigIn"]
                ).optional(),
                "name": t.string().optional(),
                "privateVisibilityConfig": t.proxy(
                    renames["ManagedZonePrivateVisibilityConfigIn"]
                ).optional(),
                "nameServerSet": t.string().optional(),
                "dnssecConfig": t.proxy(
                    renames["ManagedZoneDnsSecConfigIn"]
                ).optional(),
                "description": t.string().optional(),
                "creationTime": t.string().optional(),
                "visibility": t.string().optional(),
                "id": t.string().optional(),
                "cloudLoggingConfig": t.proxy(
                    renames["ManagedZoneCloudLoggingConfigIn"]
                ),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "reverseLookupConfig": t.proxy(
                    renames["ManagedZoneReverseLookupConfigIn"]
                ).optional(),
                "nameServers": t.array(t.string()).optional(),
                "peeringConfig": t.proxy(
                    renames["ManagedZonePeeringConfigIn"]
                ).optional(),
                "forwardingConfig": t.proxy(
                    renames["ManagedZoneForwardingConfigIn"]
                ).optional(),
                "dnsName": t.string().optional(),
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
                "managedZone": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "project": t.string().optional(),
                "kind": t.string(),
                "serviceDirectoryConfig": t.proxy(
                    renames["ManagedZoneServiceDirectoryConfigIn"]
                ).optional(),
                "name": t.string().optional(),
                "privateVisibilityConfig": t.proxy(
                    renames["ManagedZonePrivateVisibilityConfigIn"]
                ).optional(),
                "nameServerSet": t.string().optional(),
                "dnssecConfig": t.proxy(
                    renames["ManagedZoneDnsSecConfigIn"]
                ).optional(),
                "description": t.string().optional(),
                "creationTime": t.string().optional(),
                "visibility": t.string().optional(),
                "id": t.string().optional(),
                "cloudLoggingConfig": t.proxy(
                    renames["ManagedZoneCloudLoggingConfigIn"]
                ),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "reverseLookupConfig": t.proxy(
                    renames["ManagedZoneReverseLookupConfigIn"]
                ).optional(),
                "nameServers": t.array(t.string()).optional(),
                "peeringConfig": t.proxy(
                    renames["ManagedZonePeeringConfigIn"]
                ).optional(),
                "forwardingConfig": t.proxy(
                    renames["ManagedZoneForwardingConfigIn"]
                ).optional(),
                "dnsName": t.string().optional(),
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
                "managedZone": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "project": t.string().optional(),
                "kind": t.string(),
                "serviceDirectoryConfig": t.proxy(
                    renames["ManagedZoneServiceDirectoryConfigIn"]
                ).optional(),
                "name": t.string().optional(),
                "privateVisibilityConfig": t.proxy(
                    renames["ManagedZonePrivateVisibilityConfigIn"]
                ).optional(),
                "nameServerSet": t.string().optional(),
                "dnssecConfig": t.proxy(
                    renames["ManagedZoneDnsSecConfigIn"]
                ).optional(),
                "description": t.string().optional(),
                "creationTime": t.string().optional(),
                "visibility": t.string().optional(),
                "id": t.string().optional(),
                "cloudLoggingConfig": t.proxy(
                    renames["ManagedZoneCloudLoggingConfigIn"]
                ),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "reverseLookupConfig": t.proxy(
                    renames["ManagedZoneReverseLookupConfigIn"]
                ).optional(),
                "nameServers": t.array(t.string()).optional(),
                "peeringConfig": t.proxy(
                    renames["ManagedZonePeeringConfigIn"]
                ).optional(),
                "forwardingConfig": t.proxy(
                    renames["ManagedZoneForwardingConfigIn"]
                ).optional(),
                "dnsName": t.string().optional(),
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
                "managedZone": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "project": t.string().optional(),
                "kind": t.string(),
                "serviceDirectoryConfig": t.proxy(
                    renames["ManagedZoneServiceDirectoryConfigIn"]
                ).optional(),
                "name": t.string().optional(),
                "privateVisibilityConfig": t.proxy(
                    renames["ManagedZonePrivateVisibilityConfigIn"]
                ).optional(),
                "nameServerSet": t.string().optional(),
                "dnssecConfig": t.proxy(
                    renames["ManagedZoneDnsSecConfigIn"]
                ).optional(),
                "description": t.string().optional(),
                "creationTime": t.string().optional(),
                "visibility": t.string().optional(),
                "id": t.string().optional(),
                "cloudLoggingConfig": t.proxy(
                    renames["ManagedZoneCloudLoggingConfigIn"]
                ),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "reverseLookupConfig": t.proxy(
                    renames["ManagedZoneReverseLookupConfigIn"]
                ).optional(),
                "nameServers": t.array(t.string()).optional(),
                "peeringConfig": t.proxy(
                    renames["ManagedZonePeeringConfigIn"]
                ).optional(),
                "forwardingConfig": t.proxy(
                    renames["ManagedZoneForwardingConfigIn"]
                ).optional(),
                "dnsName": t.string().optional(),
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
                "managedZone": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "project": t.string().optional(),
                "kind": t.string(),
                "serviceDirectoryConfig": t.proxy(
                    renames["ManagedZoneServiceDirectoryConfigIn"]
                ).optional(),
                "name": t.string().optional(),
                "privateVisibilityConfig": t.proxy(
                    renames["ManagedZonePrivateVisibilityConfigIn"]
                ).optional(),
                "nameServerSet": t.string().optional(),
                "dnssecConfig": t.proxy(
                    renames["ManagedZoneDnsSecConfigIn"]
                ).optional(),
                "description": t.string().optional(),
                "creationTime": t.string().optional(),
                "visibility": t.string().optional(),
                "id": t.string().optional(),
                "cloudLoggingConfig": t.proxy(
                    renames["ManagedZoneCloudLoggingConfigIn"]
                ),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "reverseLookupConfig": t.proxy(
                    renames["ManagedZoneReverseLookupConfigIn"]
                ).optional(),
                "nameServers": t.array(t.string()).optional(),
                "peeringConfig": t.proxy(
                    renames["ManagedZonePeeringConfigIn"]
                ).optional(),
                "forwardingConfig": t.proxy(
                    renames["ManagedZoneForwardingConfigIn"]
                ).optional(),
                "dnsName": t.string().optional(),
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
                "managedZone": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "project": t.string().optional(),
                "kind": t.string(),
                "serviceDirectoryConfig": t.proxy(
                    renames["ManagedZoneServiceDirectoryConfigIn"]
                ).optional(),
                "name": t.string().optional(),
                "privateVisibilityConfig": t.proxy(
                    renames["ManagedZonePrivateVisibilityConfigIn"]
                ).optional(),
                "nameServerSet": t.string().optional(),
                "dnssecConfig": t.proxy(
                    renames["ManagedZoneDnsSecConfigIn"]
                ).optional(),
                "description": t.string().optional(),
                "creationTime": t.string().optional(),
                "visibility": t.string().optional(),
                "id": t.string().optional(),
                "cloudLoggingConfig": t.proxy(
                    renames["ManagedZoneCloudLoggingConfigIn"]
                ),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "reverseLookupConfig": t.proxy(
                    renames["ManagedZoneReverseLookupConfigIn"]
                ).optional(),
                "nameServers": t.array(t.string()).optional(),
                "peeringConfig": t.proxy(
                    renames["ManagedZonePeeringConfigIn"]
                ).optional(),
                "forwardingConfig": t.proxy(
                    renames["ManagedZoneForwardingConfigIn"]
                ).optional(),
                "dnsName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managedZonesGetIamPolicy"] = dns.patch(
        "dns/v1/projects/{project}/managedZones/{managedZone}",
        t.struct(
            {
                "managedZone": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "project": t.string().optional(),
                "kind": t.string(),
                "serviceDirectoryConfig": t.proxy(
                    renames["ManagedZoneServiceDirectoryConfigIn"]
                ).optional(),
                "name": t.string().optional(),
                "privateVisibilityConfig": t.proxy(
                    renames["ManagedZonePrivateVisibilityConfigIn"]
                ).optional(),
                "nameServerSet": t.string().optional(),
                "dnssecConfig": t.proxy(
                    renames["ManagedZoneDnsSecConfigIn"]
                ).optional(),
                "description": t.string().optional(),
                "creationTime": t.string().optional(),
                "visibility": t.string().optional(),
                "id": t.string().optional(),
                "cloudLoggingConfig": t.proxy(
                    renames["ManagedZoneCloudLoggingConfigIn"]
                ),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "reverseLookupConfig": t.proxy(
                    renames["ManagedZoneReverseLookupConfigIn"]
                ).optional(),
                "nameServers": t.array(t.string()).optional(),
                "peeringConfig": t.proxy(
                    renames["ManagedZonePeeringConfigIn"]
                ).optional(),
                "forwardingConfig": t.proxy(
                    renames["ManagedZoneForwardingConfigIn"]
                ).optional(),
                "dnsName": t.string().optional(),
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
                "managedZone": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "project": t.string().optional(),
                "kind": t.string(),
                "serviceDirectoryConfig": t.proxy(
                    renames["ManagedZoneServiceDirectoryConfigIn"]
                ).optional(),
                "name": t.string().optional(),
                "privateVisibilityConfig": t.proxy(
                    renames["ManagedZonePrivateVisibilityConfigIn"]
                ).optional(),
                "nameServerSet": t.string().optional(),
                "dnssecConfig": t.proxy(
                    renames["ManagedZoneDnsSecConfigIn"]
                ).optional(),
                "description": t.string().optional(),
                "creationTime": t.string().optional(),
                "visibility": t.string().optional(),
                "id": t.string().optional(),
                "cloudLoggingConfig": t.proxy(
                    renames["ManagedZoneCloudLoggingConfigIn"]
                ),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "reverseLookupConfig": t.proxy(
                    renames["ManagedZoneReverseLookupConfigIn"]
                ).optional(),
                "nameServers": t.array(t.string()).optional(),
                "peeringConfig": t.proxy(
                    renames["ManagedZonePeeringConfigIn"]
                ).optional(),
                "forwardingConfig": t.proxy(
                    renames["ManagedZoneForwardingConfigIn"]
                ).optional(),
                "dnsName": t.string().optional(),
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
                "managedZone": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "project": t.string().optional(),
                "kind": t.string(),
                "serviceDirectoryConfig": t.proxy(
                    renames["ManagedZoneServiceDirectoryConfigIn"]
                ).optional(),
                "name": t.string().optional(),
                "privateVisibilityConfig": t.proxy(
                    renames["ManagedZonePrivateVisibilityConfigIn"]
                ).optional(),
                "nameServerSet": t.string().optional(),
                "dnssecConfig": t.proxy(
                    renames["ManagedZoneDnsSecConfigIn"]
                ).optional(),
                "description": t.string().optional(),
                "creationTime": t.string().optional(),
                "visibility": t.string().optional(),
                "id": t.string().optional(),
                "cloudLoggingConfig": t.proxy(
                    renames["ManagedZoneCloudLoggingConfigIn"]
                ),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "reverseLookupConfig": t.proxy(
                    renames["ManagedZoneReverseLookupConfigIn"]
                ).optional(),
                "nameServers": t.array(t.string()).optional(),
                "peeringConfig": t.proxy(
                    renames["ManagedZonePeeringConfigIn"]
                ).optional(),
                "forwardingConfig": t.proxy(
                    renames["ManagedZoneForwardingConfigIn"]
                ).optional(),
                "dnsName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGet"] = dns.get(
        "dns/v1/projects/{project}",
        t.struct(
            {
                "clientOperationId": t.string().optional(),
                "project": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProjectOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["dnsKeysList"] = dns.get(
        "dns/v1/projects/{project}/managedZones/{managedZone}/dnsKeys/{dnsKeyId}",
        t.struct(
            {
                "managedZone": t.string().optional(),
                "digestType": t.string().optional(),
                "project": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "dnsKeyId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DnsKeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["dnsKeysGet"] = dns.get(
        "dns/v1/projects/{project}/managedZones/{managedZone}/dnsKeys/{dnsKeyId}",
        t.struct(
            {
                "managedZone": t.string().optional(),
                "digestType": t.string().optional(),
                "project": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "dnsKeyId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DnsKeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["changesGet"] = dns.get(
        "dns/v1/projects/{project}/managedZones/{managedZone}/changes",
        t.struct(
            {
                "sortBy": t.string().optional(),
                "project": t.string().optional(),
                "maxResults": t.integer().optional(),
                "sortOrder": t.string().optional(),
                "managedZone": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChangesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["changesCreate"] = dns.get(
        "dns/v1/projects/{project}/managedZones/{managedZone}/changes",
        t.struct(
            {
                "sortBy": t.string().optional(),
                "project": t.string().optional(),
                "maxResults": t.integer().optional(),
                "sortOrder": t.string().optional(),
                "managedZone": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChangesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["changesList"] = dns.get(
        "dns/v1/projects/{project}/managedZones/{managedZone}/changes",
        t.struct(
            {
                "sortBy": t.string().optional(),
                "project": t.string().optional(),
                "maxResults": t.integer().optional(),
                "sortOrder": t.string().optional(),
                "managedZone": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChangesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["responsePoliciesDelete"] = dns.put(
        "dns/v1/projects/{project}/responsePolicies/{responsePolicy}",
        t.struct(
            {
                "project": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "responsePolicy": t.string().optional(),
                "responsePolicyName": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "gkeClusters": t.array(
                    t.proxy(renames["ResponsePolicyGKEClusterIn"])
                ).optional(),
                "kind": t.string(),
                "networks": t.array(
                    t.proxy(renames["ResponsePolicyNetworkIn"])
                ).optional(),
                "id": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ResponsePoliciesUpdateResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["responsePoliciesList"] = dns.put(
        "dns/v1/projects/{project}/responsePolicies/{responsePolicy}",
        t.struct(
            {
                "project": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "responsePolicy": t.string().optional(),
                "responsePolicyName": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "gkeClusters": t.array(
                    t.proxy(renames["ResponsePolicyGKEClusterIn"])
                ).optional(),
                "kind": t.string(),
                "networks": t.array(
                    t.proxy(renames["ResponsePolicyNetworkIn"])
                ).optional(),
                "id": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ResponsePoliciesUpdateResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["responsePoliciesCreate"] = dns.put(
        "dns/v1/projects/{project}/responsePolicies/{responsePolicy}",
        t.struct(
            {
                "project": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "responsePolicy": t.string().optional(),
                "responsePolicyName": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "gkeClusters": t.array(
                    t.proxy(renames["ResponsePolicyGKEClusterIn"])
                ).optional(),
                "kind": t.string(),
                "networks": t.array(
                    t.proxy(renames["ResponsePolicyNetworkIn"])
                ).optional(),
                "id": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ResponsePoliciesUpdateResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["responsePoliciesGet"] = dns.put(
        "dns/v1/projects/{project}/responsePolicies/{responsePolicy}",
        t.struct(
            {
                "project": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "responsePolicy": t.string().optional(),
                "responsePolicyName": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "gkeClusters": t.array(
                    t.proxy(renames["ResponsePolicyGKEClusterIn"])
                ).optional(),
                "kind": t.string(),
                "networks": t.array(
                    t.proxy(renames["ResponsePolicyNetworkIn"])
                ).optional(),
                "id": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ResponsePoliciesUpdateResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["responsePoliciesPatch"] = dns.put(
        "dns/v1/projects/{project}/responsePolicies/{responsePolicy}",
        t.struct(
            {
                "project": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "responsePolicy": t.string().optional(),
                "responsePolicyName": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "gkeClusters": t.array(
                    t.proxy(renames["ResponsePolicyGKEClusterIn"])
                ).optional(),
                "kind": t.string(),
                "networks": t.array(
                    t.proxy(renames["ResponsePolicyNetworkIn"])
                ).optional(),
                "id": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ResponsePoliciesUpdateResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["responsePoliciesUpdate"] = dns.put(
        "dns/v1/projects/{project}/responsePolicies/{responsePolicy}",
        t.struct(
            {
                "project": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "responsePolicy": t.string().optional(),
                "responsePolicyName": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "gkeClusters": t.array(
                    t.proxy(renames["ResponsePolicyGKEClusterIn"])
                ).optional(),
                "kind": t.string(),
                "networks": t.array(
                    t.proxy(renames["ResponsePolicyNetworkIn"])
                ).optional(),
                "id": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ResponsePoliciesUpdateResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["resourceRecordSetsList"] = dns.patch(
        "dns/v1/projects/{project}/managedZones/{managedZone}/rrsets/{name}/{type}",
        t.struct(
            {
                "managedZone": t.string().optional(),
                "type": t.string().optional(),
                "project": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "name": t.string().optional(),
                "signatureRrdatas": t.array(t.string()).optional(),
                "kind": t.string(),
                "routingPolicy": t.proxy(renames["RRSetRoutingPolicyIn"]).optional(),
                "rrdatas": t.array(t.string()).optional(),
                "ttl": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ResourceRecordSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["resourceRecordSetsCreate"] = dns.patch(
        "dns/v1/projects/{project}/managedZones/{managedZone}/rrsets/{name}/{type}",
        t.struct(
            {
                "managedZone": t.string().optional(),
                "type": t.string().optional(),
                "project": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "name": t.string().optional(),
                "signatureRrdatas": t.array(t.string()).optional(),
                "kind": t.string(),
                "routingPolicy": t.proxy(renames["RRSetRoutingPolicyIn"]).optional(),
                "rrdatas": t.array(t.string()).optional(),
                "ttl": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ResourceRecordSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["resourceRecordSetsGet"] = dns.patch(
        "dns/v1/projects/{project}/managedZones/{managedZone}/rrsets/{name}/{type}",
        t.struct(
            {
                "managedZone": t.string().optional(),
                "type": t.string().optional(),
                "project": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "name": t.string().optional(),
                "signatureRrdatas": t.array(t.string()).optional(),
                "kind": t.string(),
                "routingPolicy": t.proxy(renames["RRSetRoutingPolicyIn"]).optional(),
                "rrdatas": t.array(t.string()).optional(),
                "ttl": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ResourceRecordSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["resourceRecordSetsDelete"] = dns.patch(
        "dns/v1/projects/{project}/managedZones/{managedZone}/rrsets/{name}/{type}",
        t.struct(
            {
                "managedZone": t.string().optional(),
                "type": t.string().optional(),
                "project": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "name": t.string().optional(),
                "signatureRrdatas": t.array(t.string()).optional(),
                "kind": t.string(),
                "routingPolicy": t.proxy(renames["RRSetRoutingPolicyIn"]).optional(),
                "rrdatas": t.array(t.string()).optional(),
                "ttl": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ResourceRecordSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["resourceRecordSetsPatch"] = dns.patch(
        "dns/v1/projects/{project}/managedZones/{managedZone}/rrsets/{name}/{type}",
        t.struct(
            {
                "managedZone": t.string().optional(),
                "type": t.string().optional(),
                "project": t.string().optional(),
                "clientOperationId": t.string().optional(),
                "name": t.string().optional(),
                "signatureRrdatas": t.array(t.string()).optional(),
                "kind": t.string(),
                "routingPolicy": t.proxy(renames["RRSetRoutingPolicyIn"]).optional(),
                "rrdatas": t.array(t.string()).optional(),
                "ttl": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ResourceRecordSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["responsePolicyRulesPatch"] = dns.delete(
        "dns/v1/projects/{project}/responsePolicies/{responsePolicy}/rules/{responsePolicyRule}",
        t.struct(
            {
                "clientOperationId": t.string().optional(),
                "project": t.string().optional(),
                "responsePolicyRule": t.string().optional(),
                "responsePolicy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["responsePolicyRulesCreate"] = dns.delete(
        "dns/v1/projects/{project}/responsePolicies/{responsePolicy}/rules/{responsePolicyRule}",
        t.struct(
            {
                "clientOperationId": t.string().optional(),
                "project": t.string().optional(),
                "responsePolicyRule": t.string().optional(),
                "responsePolicy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["responsePolicyRulesGet"] = dns.delete(
        "dns/v1/projects/{project}/responsePolicies/{responsePolicy}/rules/{responsePolicyRule}",
        t.struct(
            {
                "clientOperationId": t.string().optional(),
                "project": t.string().optional(),
                "responsePolicyRule": t.string().optional(),
                "responsePolicy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["responsePolicyRulesList"] = dns.delete(
        "dns/v1/projects/{project}/responsePolicies/{responsePolicy}/rules/{responsePolicyRule}",
        t.struct(
            {
                "clientOperationId": t.string().optional(),
                "project": t.string().optional(),
                "responsePolicyRule": t.string().optional(),
                "responsePolicy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["responsePolicyRulesUpdate"] = dns.delete(
        "dns/v1/projects/{project}/responsePolicies/{responsePolicy}/rules/{responsePolicyRule}",
        t.struct(
            {
                "clientOperationId": t.string().optional(),
                "project": t.string().optional(),
                "responsePolicyRule": t.string().optional(),
                "responsePolicy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["responsePolicyRulesDelete"] = dns.delete(
        "dns/v1/projects/{project}/responsePolicies/{responsePolicy}/rules/{responsePolicyRule}",
        t.struct(
            {
                "clientOperationId": t.string().optional(),
                "project": t.string().optional(),
                "responsePolicyRule": t.string().optional(),
                "responsePolicy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="dns", renames=renames, types=Box(types), functions=Box(functions)
    )
