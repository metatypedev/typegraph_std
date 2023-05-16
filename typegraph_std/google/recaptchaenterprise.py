from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_recaptchaenterprise() -> Import:
    recaptchaenterprise = HTTPRuntime("https://recaptchaenterprise.googleapis.com/")

    renames = {
        "ErrorResponse": "_recaptchaenterprise_1_ErrorResponse",
        "GoogleCloudRecaptchaenterpriseV1PrivatePasswordLeakVerificationIn": "_recaptchaenterprise_2_GoogleCloudRecaptchaenterpriseV1PrivatePasswordLeakVerificationIn",
        "GoogleCloudRecaptchaenterpriseV1PrivatePasswordLeakVerificationOut": "_recaptchaenterprise_3_GoogleCloudRecaptchaenterpriseV1PrivatePasswordLeakVerificationOut",
        "GoogleCloudRecaptchaenterpriseV1TransactionDataGatewayInfoIn": "_recaptchaenterprise_4_GoogleCloudRecaptchaenterpriseV1TransactionDataGatewayInfoIn",
        "GoogleCloudRecaptchaenterpriseV1TransactionDataGatewayInfoOut": "_recaptchaenterprise_5_GoogleCloudRecaptchaenterpriseV1TransactionDataGatewayInfoOut",
        "GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupIn": "_recaptchaenterprise_6_GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupIn",
        "GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupOut": "_recaptchaenterprise_7_GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupOut",
        "GoogleCloudRecaptchaenterpriseV1ScoreMetricsIn": "_recaptchaenterprise_8_GoogleCloudRecaptchaenterpriseV1ScoreMetricsIn",
        "GoogleCloudRecaptchaenterpriseV1ScoreMetricsOut": "_recaptchaenterprise_9_GoogleCloudRecaptchaenterpriseV1ScoreMetricsOut",
        "GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupMembershipIn": "_recaptchaenterprise_10_GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupMembershipIn",
        "GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupMembershipOut": "_recaptchaenterprise_11_GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupMembershipOut",
        "GoogleCloudRecaptchaenterpriseV1FirewallActionSubstituteActionIn": "_recaptchaenterprise_12_GoogleCloudRecaptchaenterpriseV1FirewallActionSubstituteActionIn",
        "GoogleCloudRecaptchaenterpriseV1FirewallActionSubstituteActionOut": "_recaptchaenterprise_13_GoogleCloudRecaptchaenterpriseV1FirewallActionSubstituteActionOut",
        "GoogleCloudRecaptchaenterpriseV1RiskAnalysisIn": "_recaptchaenterprise_14_GoogleCloudRecaptchaenterpriseV1RiskAnalysisIn",
        "GoogleCloudRecaptchaenterpriseV1RiskAnalysisOut": "_recaptchaenterprise_15_GoogleCloudRecaptchaenterpriseV1RiskAnalysisOut",
        "GoogleCloudRecaptchaenterpriseV1FirewallPolicyAssessmentIn": "_recaptchaenterprise_16_GoogleCloudRecaptchaenterpriseV1FirewallPolicyAssessmentIn",
        "GoogleCloudRecaptchaenterpriseV1FirewallPolicyAssessmentOut": "_recaptchaenterprise_17_GoogleCloudRecaptchaenterpriseV1FirewallPolicyAssessmentOut",
        "GoogleRpcStatusIn": "_recaptchaenterprise_18_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_recaptchaenterprise_19_GoogleRpcStatusOut",
        "GoogleCloudRecaptchaenterpriseV1FirewallActionIn": "_recaptchaenterprise_20_GoogleCloudRecaptchaenterpriseV1FirewallActionIn",
        "GoogleCloudRecaptchaenterpriseV1FirewallActionOut": "_recaptchaenterprise_21_GoogleCloudRecaptchaenterpriseV1FirewallActionOut",
        "GoogleCloudRecaptchaenterpriseV1MetricsIn": "_recaptchaenterprise_22_GoogleCloudRecaptchaenterpriseV1MetricsIn",
        "GoogleCloudRecaptchaenterpriseV1MetricsOut": "_recaptchaenterprise_23_GoogleCloudRecaptchaenterpriseV1MetricsOut",
        "GoogleCloudRecaptchaenterpriseV1FirewallActionSetHeaderActionIn": "_recaptchaenterprise_24_GoogleCloudRecaptchaenterpriseV1FirewallActionSetHeaderActionIn",
        "GoogleCloudRecaptchaenterpriseV1FirewallActionSetHeaderActionOut": "_recaptchaenterprise_25_GoogleCloudRecaptchaenterpriseV1FirewallActionSetHeaderActionOut",
        "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentBehavioralTrustVerdictIn": "_recaptchaenterprise_26_GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentBehavioralTrustVerdictIn",
        "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentBehavioralTrustVerdictOut": "_recaptchaenterprise_27_GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentBehavioralTrustVerdictOut",
        "GoogleCloudRecaptchaenterpriseV1AndroidKeySettingsIn": "_recaptchaenterprise_28_GoogleCloudRecaptchaenterpriseV1AndroidKeySettingsIn",
        "GoogleCloudRecaptchaenterpriseV1AndroidKeySettingsOut": "_recaptchaenterprise_29_GoogleCloudRecaptchaenterpriseV1AndroidKeySettingsOut",
        "GoogleCloudRecaptchaenterpriseV1FirewallPolicyIn": "_recaptchaenterprise_30_GoogleCloudRecaptchaenterpriseV1FirewallPolicyIn",
        "GoogleCloudRecaptchaenterpriseV1FirewallPolicyOut": "_recaptchaenterprise_31_GoogleCloudRecaptchaenterpriseV1FirewallPolicyOut",
        "GoogleCloudRecaptchaenterpriseV1AppleDeveloperIdIn": "_recaptchaenterprise_32_GoogleCloudRecaptchaenterpriseV1AppleDeveloperIdIn",
        "GoogleCloudRecaptchaenterpriseV1AppleDeveloperIdOut": "_recaptchaenterprise_33_GoogleCloudRecaptchaenterpriseV1AppleDeveloperIdOut",
        "GoogleCloudRecaptchaenterpriseV1ScoreDistributionIn": "_recaptchaenterprise_34_GoogleCloudRecaptchaenterpriseV1ScoreDistributionIn",
        "GoogleCloudRecaptchaenterpriseV1ScoreDistributionOut": "_recaptchaenterprise_35_GoogleCloudRecaptchaenterpriseV1ScoreDistributionOut",
        "GoogleCloudRecaptchaenterpriseV1FirewallActionAllowActionIn": "_recaptchaenterprise_36_GoogleCloudRecaptchaenterpriseV1FirewallActionAllowActionIn",
        "GoogleCloudRecaptchaenterpriseV1FirewallActionAllowActionOut": "_recaptchaenterprise_37_GoogleCloudRecaptchaenterpriseV1FirewallActionAllowActionOut",
        "GoogleCloudRecaptchaenterpriseV1TransactionEventIn": "_recaptchaenterprise_38_GoogleCloudRecaptchaenterpriseV1TransactionEventIn",
        "GoogleCloudRecaptchaenterpriseV1TransactionEventOut": "_recaptchaenterprise_39_GoogleCloudRecaptchaenterpriseV1TransactionEventOut",
        "GoogleCloudRecaptchaenterpriseV1AssessmentIn": "_recaptchaenterprise_40_GoogleCloudRecaptchaenterpriseV1AssessmentIn",
        "GoogleCloudRecaptchaenterpriseV1AssessmentOut": "_recaptchaenterprise_41_GoogleCloudRecaptchaenterpriseV1AssessmentOut",
        "GoogleCloudRecaptchaenterpriseV1TransactionDataIn": "_recaptchaenterprise_42_GoogleCloudRecaptchaenterpriseV1TransactionDataIn",
        "GoogleCloudRecaptchaenterpriseV1TransactionDataOut": "_recaptchaenterprise_43_GoogleCloudRecaptchaenterpriseV1TransactionDataOut",
        "GoogleCloudRecaptchaenterpriseV1KeyIn": "_recaptchaenterprise_44_GoogleCloudRecaptchaenterpriseV1KeyIn",
        "GoogleCloudRecaptchaenterpriseV1KeyOut": "_recaptchaenterprise_45_GoogleCloudRecaptchaenterpriseV1KeyOut",
        "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentStolenInstrumentVerdictIn": "_recaptchaenterprise_46_GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentStolenInstrumentVerdictIn",
        "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentStolenInstrumentVerdictOut": "_recaptchaenterprise_47_GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentStolenInstrumentVerdictOut",
        "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentCardTestingVerdictIn": "_recaptchaenterprise_48_GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentCardTestingVerdictIn",
        "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentCardTestingVerdictOut": "_recaptchaenterprise_49_GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentCardTestingVerdictOut",
        "GoogleCloudRecaptchaenterpriseV1WebKeySettingsIn": "_recaptchaenterprise_50_GoogleCloudRecaptchaenterpriseV1WebKeySettingsIn",
        "GoogleCloudRecaptchaenterpriseV1WebKeySettingsOut": "_recaptchaenterprise_51_GoogleCloudRecaptchaenterpriseV1WebKeySettingsOut",
        "GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupsResponseIn": "_recaptchaenterprise_52_GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupsResponseIn",
        "GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupsResponseOut": "_recaptchaenterprise_53_GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupsResponseOut",
        "GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentRequestIn": "_recaptchaenterprise_54_GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentRequestIn",
        "GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentRequestOut": "_recaptchaenterprise_55_GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentRequestOut",
        "GoogleCloudRecaptchaenterpriseV1TransactionDataItemIn": "_recaptchaenterprise_56_GoogleCloudRecaptchaenterpriseV1TransactionDataItemIn",
        "GoogleCloudRecaptchaenterpriseV1TransactionDataItemOut": "_recaptchaenterprise_57_GoogleCloudRecaptchaenterpriseV1TransactionDataItemOut",
        "GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsResponseIn": "_recaptchaenterprise_58_GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsResponseIn",
        "GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsResponseOut": "_recaptchaenterprise_59_GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsResponseOut",
        "GoogleCloudRecaptchaenterpriseV1TransactionDataUserIn": "_recaptchaenterprise_60_GoogleCloudRecaptchaenterpriseV1TransactionDataUserIn",
        "GoogleCloudRecaptchaenterpriseV1TransactionDataUserOut": "_recaptchaenterprise_61_GoogleCloudRecaptchaenterpriseV1TransactionDataUserOut",
        "GoogleCloudRecaptchaenterpriseV1TokenPropertiesIn": "_recaptchaenterprise_62_GoogleCloudRecaptchaenterpriseV1TokenPropertiesIn",
        "GoogleCloudRecaptchaenterpriseV1TokenPropertiesOut": "_recaptchaenterprise_63_GoogleCloudRecaptchaenterpriseV1TokenPropertiesOut",
        "GoogleCloudRecaptchaenterpriseV1WafSettingsIn": "_recaptchaenterprise_64_GoogleCloudRecaptchaenterpriseV1WafSettingsIn",
        "GoogleCloudRecaptchaenterpriseV1WafSettingsOut": "_recaptchaenterprise_65_GoogleCloudRecaptchaenterpriseV1WafSettingsOut",
        "GoogleCloudRecaptchaenterpriseV1FirewallActionRedirectActionIn": "_recaptchaenterprise_66_GoogleCloudRecaptchaenterpriseV1FirewallActionRedirectActionIn",
        "GoogleCloudRecaptchaenterpriseV1FirewallActionRedirectActionOut": "_recaptchaenterprise_67_GoogleCloudRecaptchaenterpriseV1FirewallActionRedirectActionOut",
        "GoogleCloudRecaptchaenterpriseV1ListKeysResponseIn": "_recaptchaenterprise_68_GoogleCloudRecaptchaenterpriseV1ListKeysResponseIn",
        "GoogleCloudRecaptchaenterpriseV1ListKeysResponseOut": "_recaptchaenterprise_69_GoogleCloudRecaptchaenterpriseV1ListKeysResponseOut",
        "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentIn": "_recaptchaenterprise_70_GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentIn",
        "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentOut": "_recaptchaenterprise_71_GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentOut",
        "GoogleCloudRecaptchaenterpriseV1AccountDefenderAssessmentIn": "_recaptchaenterprise_72_GoogleCloudRecaptchaenterpriseV1AccountDefenderAssessmentIn",
        "GoogleCloudRecaptchaenterpriseV1AccountDefenderAssessmentOut": "_recaptchaenterprise_73_GoogleCloudRecaptchaenterpriseV1AccountDefenderAssessmentOut",
        "GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsRequestIn": "_recaptchaenterprise_74_GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsRequestIn",
        "GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsRequestOut": "_recaptchaenterprise_75_GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsRequestOut",
        "GoogleCloudRecaptchaenterpriseV1TestingOptionsIn": "_recaptchaenterprise_76_GoogleCloudRecaptchaenterpriseV1TestingOptionsIn",
        "GoogleCloudRecaptchaenterpriseV1TestingOptionsOut": "_recaptchaenterprise_77_GoogleCloudRecaptchaenterpriseV1TestingOptionsOut",
        "GoogleCloudRecaptchaenterpriseV1FirewallActionBlockActionIn": "_recaptchaenterprise_78_GoogleCloudRecaptchaenterpriseV1FirewallActionBlockActionIn",
        "GoogleCloudRecaptchaenterpriseV1FirewallActionBlockActionOut": "_recaptchaenterprise_79_GoogleCloudRecaptchaenterpriseV1FirewallActionBlockActionOut",
        "GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentResponseIn": "_recaptchaenterprise_80_GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentResponseIn",
        "GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentResponseOut": "_recaptchaenterprise_81_GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentResponseOut",
        "GoogleProtobufEmptyIn": "_recaptchaenterprise_82_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_recaptchaenterprise_83_GoogleProtobufEmptyOut",
        "GoogleCloudRecaptchaenterpriseV1RetrieveLegacySecretKeyResponseIn": "_recaptchaenterprise_84_GoogleCloudRecaptchaenterpriseV1RetrieveLegacySecretKeyResponseIn",
        "GoogleCloudRecaptchaenterpriseV1RetrieveLegacySecretKeyResponseOut": "_recaptchaenterprise_85_GoogleCloudRecaptchaenterpriseV1RetrieveLegacySecretKeyResponseOut",
        "GoogleCloudRecaptchaenterpriseV1IOSKeySettingsIn": "_recaptchaenterprise_86_GoogleCloudRecaptchaenterpriseV1IOSKeySettingsIn",
        "GoogleCloudRecaptchaenterpriseV1IOSKeySettingsOut": "_recaptchaenterprise_87_GoogleCloudRecaptchaenterpriseV1IOSKeySettingsOut",
        "GoogleCloudRecaptchaenterpriseV1EndpointVerificationInfoIn": "_recaptchaenterprise_88_GoogleCloudRecaptchaenterpriseV1EndpointVerificationInfoIn",
        "GoogleCloudRecaptchaenterpriseV1EndpointVerificationInfoOut": "_recaptchaenterprise_89_GoogleCloudRecaptchaenterpriseV1EndpointVerificationInfoOut",
        "GoogleCloudRecaptchaenterpriseV1ListFirewallPoliciesResponseIn": "_recaptchaenterprise_90_GoogleCloudRecaptchaenterpriseV1ListFirewallPoliciesResponseIn",
        "GoogleCloudRecaptchaenterpriseV1ListFirewallPoliciesResponseOut": "_recaptchaenterprise_91_GoogleCloudRecaptchaenterpriseV1ListFirewallPoliciesResponseOut",
        "GoogleCloudRecaptchaenterpriseV1ChallengeMetricsIn": "_recaptchaenterprise_92_GoogleCloudRecaptchaenterpriseV1ChallengeMetricsIn",
        "GoogleCloudRecaptchaenterpriseV1ChallengeMetricsOut": "_recaptchaenterprise_93_GoogleCloudRecaptchaenterpriseV1ChallengeMetricsOut",
        "GoogleCloudRecaptchaenterpriseV1AccountVerificationInfoIn": "_recaptchaenterprise_94_GoogleCloudRecaptchaenterpriseV1AccountVerificationInfoIn",
        "GoogleCloudRecaptchaenterpriseV1AccountVerificationInfoOut": "_recaptchaenterprise_95_GoogleCloudRecaptchaenterpriseV1AccountVerificationInfoOut",
        "GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupMembershipsResponseIn": "_recaptchaenterprise_96_GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupMembershipsResponseIn",
        "GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupMembershipsResponseOut": "_recaptchaenterprise_97_GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupMembershipsResponseOut",
        "GoogleCloudRecaptchaenterpriseV1MigrateKeyRequestIn": "_recaptchaenterprise_98_GoogleCloudRecaptchaenterpriseV1MigrateKeyRequestIn",
        "GoogleCloudRecaptchaenterpriseV1MigrateKeyRequestOut": "_recaptchaenterprise_99_GoogleCloudRecaptchaenterpriseV1MigrateKeyRequestOut",
        "GoogleCloudRecaptchaenterpriseV1TransactionDataAddressIn": "_recaptchaenterprise_100_GoogleCloudRecaptchaenterpriseV1TransactionDataAddressIn",
        "GoogleCloudRecaptchaenterpriseV1TransactionDataAddressOut": "_recaptchaenterprise_101_GoogleCloudRecaptchaenterpriseV1TransactionDataAddressOut",
        "GoogleCloudRecaptchaenterpriseV1EventIn": "_recaptchaenterprise_102_GoogleCloudRecaptchaenterpriseV1EventIn",
        "GoogleCloudRecaptchaenterpriseV1EventOut": "_recaptchaenterprise_103_GoogleCloudRecaptchaenterpriseV1EventOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types[
        "GoogleCloudRecaptchaenterpriseV1PrivatePasswordLeakVerificationIn"
    ] = t.struct(
        {
            "lookupHashPrefix": t.string().optional(),
            "encryptedUserCredentialsHash": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudRecaptchaenterpriseV1PrivatePasswordLeakVerificationIn"]
    )
    types[
        "GoogleCloudRecaptchaenterpriseV1PrivatePasswordLeakVerificationOut"
    ] = t.struct(
        {
            "reencryptedUserCredentialsHash": t.string().optional(),
            "lookupHashPrefix": t.string().optional(),
            "encryptedUserCredentialsHash": t.string().optional(),
            "encryptedLeakMatchPrefixes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudRecaptchaenterpriseV1PrivatePasswordLeakVerificationOut"]
    )
    types["GoogleCloudRecaptchaenterpriseV1TransactionDataGatewayInfoIn"] = t.struct(
        {
            "gatewayResponseCode": t.string().optional(),
            "name": t.string().optional(),
            "avsResponseCode": t.string().optional(),
            "cvvResponseCode": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TransactionDataGatewayInfoIn"])
    types["GoogleCloudRecaptchaenterpriseV1TransactionDataGatewayInfoOut"] = t.struct(
        {
            "gatewayResponseCode": t.string().optional(),
            "name": t.string().optional(),
            "avsResponseCode": t.string().optional(),
            "cvvResponseCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TransactionDataGatewayInfoOut"])
    types["GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupIn"] = t.struct(
        {"name": t.string()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupIn"])
    types["GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupOut"] = t.struct(
        {"name": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupOut"])
    types["GoogleCloudRecaptchaenterpriseV1ScoreMetricsIn"] = t.struct(
        {
            "overallMetrics": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1ScoreDistributionIn"]
            ).optional(),
            "actionMetrics": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1ScoreMetricsIn"])
    types["GoogleCloudRecaptchaenterpriseV1ScoreMetricsOut"] = t.struct(
        {
            "overallMetrics": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1ScoreDistributionOut"]
            ).optional(),
            "actionMetrics": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1ScoreMetricsOut"])
    types["GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupMembershipIn"] = t.struct(
        {"name": t.string(), "hashedAccountId": t.string().optional()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupMembershipIn"])
    types[
        "GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupMembershipOut"
    ] = t.struct(
        {
            "name": t.string(),
            "hashedAccountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupMembershipOut"]
    )
    types[
        "GoogleCloudRecaptchaenterpriseV1FirewallActionSubstituteActionIn"
    ] = t.struct({"path": t.string().optional()}).named(
        renames["GoogleCloudRecaptchaenterpriseV1FirewallActionSubstituteActionIn"]
    )
    types[
        "GoogleCloudRecaptchaenterpriseV1FirewallActionSubstituteActionOut"
    ] = t.struct(
        {
            "path": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudRecaptchaenterpriseV1FirewallActionSubstituteActionOut"]
    )
    types["GoogleCloudRecaptchaenterpriseV1RiskAnalysisIn"] = t.struct(
        {
            "extendedVerdictReasons": t.array(t.string()).optional(),
            "score": t.number().optional(),
            "reasons": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1RiskAnalysisIn"])
    types["GoogleCloudRecaptchaenterpriseV1RiskAnalysisOut"] = t.struct(
        {
            "extendedVerdictReasons": t.array(t.string()).optional(),
            "score": t.number().optional(),
            "reasons": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1RiskAnalysisOut"])
    types["GoogleCloudRecaptchaenterpriseV1FirewallPolicyAssessmentIn"] = t.struct(
        {"error": t.proxy(renames["GoogleRpcStatusIn"]).optional()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1FirewallPolicyAssessmentIn"])
    types["GoogleCloudRecaptchaenterpriseV1FirewallPolicyAssessmentOut"] = t.struct(
        {
            "firewallPolicy": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1FirewallPolicyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1FirewallPolicyAssessmentOut"])
    types["GoogleRpcStatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
        }
    ).named(renames["GoogleRpcStatusIn"])
    types["GoogleRpcStatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleRpcStatusOut"])
    types["GoogleCloudRecaptchaenterpriseV1FirewallActionIn"] = t.struct(
        {
            "redirect": t.proxy(
                renames[
                    "GoogleCloudRecaptchaenterpriseV1FirewallActionRedirectActionIn"
                ]
            ).optional(),
            "allow": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1FirewallActionAllowActionIn"]
            ).optional(),
            "setHeader": t.proxy(
                renames[
                    "GoogleCloudRecaptchaenterpriseV1FirewallActionSetHeaderActionIn"
                ]
            ).optional(),
            "block": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1FirewallActionBlockActionIn"]
            ).optional(),
            "substitute": t.proxy(
                renames[
                    "GoogleCloudRecaptchaenterpriseV1FirewallActionSubstituteActionIn"
                ]
            ).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1FirewallActionIn"])
    types["GoogleCloudRecaptchaenterpriseV1FirewallActionOut"] = t.struct(
        {
            "redirect": t.proxy(
                renames[
                    "GoogleCloudRecaptchaenterpriseV1FirewallActionRedirectActionOut"
                ]
            ).optional(),
            "allow": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1FirewallActionAllowActionOut"]
            ).optional(),
            "setHeader": t.proxy(
                renames[
                    "GoogleCloudRecaptchaenterpriseV1FirewallActionSetHeaderActionOut"
                ]
            ).optional(),
            "block": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1FirewallActionBlockActionOut"]
            ).optional(),
            "substitute": t.proxy(
                renames[
                    "GoogleCloudRecaptchaenterpriseV1FirewallActionSubstituteActionOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1FirewallActionOut"])
    types["GoogleCloudRecaptchaenterpriseV1MetricsIn"] = t.struct(
        {
            "startTime": t.string().optional(),
            "challengeMetrics": t.array(
                t.proxy(renames["GoogleCloudRecaptchaenterpriseV1ChallengeMetricsIn"])
            ).optional(),
            "scoreMetrics": t.array(
                t.proxy(renames["GoogleCloudRecaptchaenterpriseV1ScoreMetricsIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1MetricsIn"])
    types["GoogleCloudRecaptchaenterpriseV1MetricsOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "name": t.string().optional(),
            "challengeMetrics": t.array(
                t.proxy(renames["GoogleCloudRecaptchaenterpriseV1ChallengeMetricsOut"])
            ).optional(),
            "scoreMetrics": t.array(
                t.proxy(renames["GoogleCloudRecaptchaenterpriseV1ScoreMetricsOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1MetricsOut"])
    types["GoogleCloudRecaptchaenterpriseV1FirewallActionSetHeaderActionIn"] = t.struct(
        {"value": t.string().optional(), "key": t.string().optional()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1FirewallActionSetHeaderActionIn"])
    types[
        "GoogleCloudRecaptchaenterpriseV1FirewallActionSetHeaderActionOut"
    ] = t.struct(
        {
            "value": t.string().optional(),
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudRecaptchaenterpriseV1FirewallActionSetHeaderActionOut"]
    )
    types[
        "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentBehavioralTrustVerdictIn"
    ] = t.struct({"trust": t.number().optional()}).named(
        renames[
            "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentBehavioralTrustVerdictIn"
        ]
    )
    types[
        "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentBehavioralTrustVerdictOut"
    ] = t.struct(
        {
            "trust": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentBehavioralTrustVerdictOut"
        ]
    )
    types["GoogleCloudRecaptchaenterpriseV1AndroidKeySettingsIn"] = t.struct(
        {
            "allowAllPackageNames": t.boolean().optional(),
            "allowedPackageNames": t.array(t.string()).optional(),
            "supportNonGoogleAppStoreDistribution": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1AndroidKeySettingsIn"])
    types["GoogleCloudRecaptchaenterpriseV1AndroidKeySettingsOut"] = t.struct(
        {
            "allowAllPackageNames": t.boolean().optional(),
            "allowedPackageNames": t.array(t.string()).optional(),
            "supportNonGoogleAppStoreDistribution": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1AndroidKeySettingsOut"])
    types["GoogleCloudRecaptchaenterpriseV1FirewallPolicyIn"] = t.struct(
        {
            "description": t.string().optional(),
            "path": t.string().optional(),
            "actions": t.array(
                t.proxy(renames["GoogleCloudRecaptchaenterpriseV1FirewallActionIn"])
            ).optional(),
            "condition": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1FirewallPolicyIn"])
    types["GoogleCloudRecaptchaenterpriseV1FirewallPolicyOut"] = t.struct(
        {
            "description": t.string().optional(),
            "path": t.string().optional(),
            "actions": t.array(
                t.proxy(renames["GoogleCloudRecaptchaenterpriseV1FirewallActionOut"])
            ).optional(),
            "condition": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1FirewallPolicyOut"])
    types["GoogleCloudRecaptchaenterpriseV1AppleDeveloperIdIn"] = t.struct(
        {"teamId": t.string(), "keyId": t.string(), "privateKey": t.string()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1AppleDeveloperIdIn"])
    types["GoogleCloudRecaptchaenterpriseV1AppleDeveloperIdOut"] = t.struct(
        {
            "teamId": t.string(),
            "keyId": t.string(),
            "privateKey": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1AppleDeveloperIdOut"])
    types["GoogleCloudRecaptchaenterpriseV1ScoreDistributionIn"] = t.struct(
        {"scoreBuckets": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1ScoreDistributionIn"])
    types["GoogleCloudRecaptchaenterpriseV1ScoreDistributionOut"] = t.struct(
        {
            "scoreBuckets": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1ScoreDistributionOut"])
    types["GoogleCloudRecaptchaenterpriseV1FirewallActionAllowActionIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1FirewallActionAllowActionIn"])
    types["GoogleCloudRecaptchaenterpriseV1FirewallActionAllowActionOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1FirewallActionAllowActionOut"])
    types["GoogleCloudRecaptchaenterpriseV1TransactionEventIn"] = t.struct(
        {
            "eventType": t.string().optional(),
            "eventTime": t.string().optional(),
            "value": t.number().optional(),
            "reason": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TransactionEventIn"])
    types["GoogleCloudRecaptchaenterpriseV1TransactionEventOut"] = t.struct(
        {
            "eventType": t.string().optional(),
            "eventTime": t.string().optional(),
            "value": t.number().optional(),
            "reason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TransactionEventOut"])
    types["GoogleCloudRecaptchaenterpriseV1AssessmentIn"] = t.struct(
        {
            "accountVerification": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1AccountVerificationInfoIn"]
            ).optional(),
            "privatePasswordLeakVerification": t.proxy(
                renames[
                    "GoogleCloudRecaptchaenterpriseV1PrivatePasswordLeakVerificationIn"
                ]
            ).optional(),
            "fraudPreventionAssessment": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentIn"]
            ).optional(),
            "accountDefenderAssessment": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1AccountDefenderAssessmentIn"]
            ).optional(),
            "event": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1EventIn"]
            ).optional(),
            "firewallPolicyAssessment": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1FirewallPolicyAssessmentIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1AssessmentIn"])
    types["GoogleCloudRecaptchaenterpriseV1AssessmentOut"] = t.struct(
        {
            "accountVerification": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1AccountVerificationInfoOut"]
            ).optional(),
            "name": t.string().optional(),
            "privatePasswordLeakVerification": t.proxy(
                renames[
                    "GoogleCloudRecaptchaenterpriseV1PrivatePasswordLeakVerificationOut"
                ]
            ).optional(),
            "tokenProperties": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TokenPropertiesOut"]
            ).optional(),
            "fraudPreventionAssessment": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentOut"]
            ).optional(),
            "accountDefenderAssessment": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1AccountDefenderAssessmentOut"]
            ).optional(),
            "event": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1EventOut"]
            ).optional(),
            "riskAnalysis": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1RiskAnalysisOut"]
            ).optional(),
            "firewallPolicyAssessment": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1FirewallPolicyAssessmentOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1AssessmentOut"])
    types["GoogleCloudRecaptchaenterpriseV1TransactionDataIn"] = t.struct(
        {
            "cardBin": t.string().optional(),
            "merchants": t.array(
                t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1TransactionDataUserIn"]
                )
            ).optional(),
            "shippingValue": t.number().optional(),
            "items": t.array(
                t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1TransactionDataItemIn"]
                )
            ).optional(),
            "paymentMethod": t.string().optional(),
            "gatewayInfo": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TransactionDataGatewayInfoIn"]
            ).optional(),
            "cardLastFour": t.string().optional(),
            "value": t.number().optional(),
            "user": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TransactionDataUserIn"]
            ).optional(),
            "billingAddress": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TransactionDataAddressIn"]
            ).optional(),
            "shippingAddress": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TransactionDataAddressIn"]
            ).optional(),
            "currencyCode": t.string().optional(),
            "transactionId": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TransactionDataIn"])
    types["GoogleCloudRecaptchaenterpriseV1TransactionDataOut"] = t.struct(
        {
            "cardBin": t.string().optional(),
            "merchants": t.array(
                t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1TransactionDataUserOut"]
                )
            ).optional(),
            "shippingValue": t.number().optional(),
            "items": t.array(
                t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1TransactionDataItemOut"]
                )
            ).optional(),
            "paymentMethod": t.string().optional(),
            "gatewayInfo": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TransactionDataGatewayInfoOut"]
            ).optional(),
            "cardLastFour": t.string().optional(),
            "value": t.number().optional(),
            "user": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TransactionDataUserOut"]
            ).optional(),
            "billingAddress": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TransactionDataAddressOut"]
            ).optional(),
            "shippingAddress": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TransactionDataAddressOut"]
            ).optional(),
            "currencyCode": t.string().optional(),
            "transactionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TransactionDataOut"])
    types["GoogleCloudRecaptchaenterpriseV1KeyIn"] = t.struct(
        {
            "wafSettings": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1WafSettingsIn"]
            ).optional(),
            "webSettings": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1WebKeySettingsIn"]
            ).optional(),
            "iosSettings": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1IOSKeySettingsIn"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "testingOptions": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TestingOptionsIn"]
            ).optional(),
            "androidSettings": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1AndroidKeySettingsIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1KeyIn"])
    types["GoogleCloudRecaptchaenterpriseV1KeyOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "wafSettings": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1WafSettingsOut"]
            ).optional(),
            "webSettings": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1WebKeySettingsOut"]
            ).optional(),
            "iosSettings": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1IOSKeySettingsOut"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "testingOptions": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TestingOptionsOut"]
            ).optional(),
            "androidSettings": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1AndroidKeySettingsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1KeyOut"])
    types[
        "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentStolenInstrumentVerdictIn"
    ] = t.struct({"risk": t.number().optional()}).named(
        renames[
            "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentStolenInstrumentVerdictIn"
        ]
    )
    types[
        "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentStolenInstrumentVerdictOut"
    ] = t.struct(
        {
            "risk": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentStolenInstrumentVerdictOut"
        ]
    )
    types[
        "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentCardTestingVerdictIn"
    ] = t.struct({"risk": t.number().optional()}).named(
        renames[
            "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentCardTestingVerdictIn"
        ]
    )
    types[
        "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentCardTestingVerdictOut"
    ] = t.struct(
        {
            "risk": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentCardTestingVerdictOut"
        ]
    )
    types["GoogleCloudRecaptchaenterpriseV1WebKeySettingsIn"] = t.struct(
        {
            "allowAllDomains": t.boolean().optional(),
            "challengeSecurityPreference": t.string().optional(),
            "allowedDomains": t.array(t.string()).optional(),
            "allowAmpTraffic": t.boolean().optional(),
            "integrationType": t.string(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1WebKeySettingsIn"])
    types["GoogleCloudRecaptchaenterpriseV1WebKeySettingsOut"] = t.struct(
        {
            "allowAllDomains": t.boolean().optional(),
            "challengeSecurityPreference": t.string().optional(),
            "allowedDomains": t.array(t.string()).optional(),
            "allowAmpTraffic": t.boolean().optional(),
            "integrationType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1WebKeySettingsOut"])
    types[
        "GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupsResponseIn"
    ] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "relatedAccountGroups": t.array(
                t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupIn"]
                )
            ).optional(),
        }
    ).named(
        renames["GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupsResponseIn"]
    )
    types[
        "GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupsResponseOut"
    ] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "relatedAccountGroups": t.array(
                t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupsResponseOut"]
    )
    types["GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentRequestIn"] = t.struct(
        {
            "annotation": t.string().optional(),
            "transactionEvent": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TransactionEventIn"]
            ).optional(),
            "reasons": t.array(t.string()).optional(),
            "hashedAccountId": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentRequestIn"])
    types["GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentRequestOut"] = t.struct(
        {
            "annotation": t.string().optional(),
            "transactionEvent": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TransactionEventOut"]
            ).optional(),
            "reasons": t.array(t.string()).optional(),
            "hashedAccountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentRequestOut"])
    types["GoogleCloudRecaptchaenterpriseV1TransactionDataItemIn"] = t.struct(
        {
            "merchantAccountId": t.string().optional(),
            "value": t.number().optional(),
            "quantity": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TransactionDataItemIn"])
    types["GoogleCloudRecaptchaenterpriseV1TransactionDataItemOut"] = t.struct(
        {
            "merchantAccountId": t.string().optional(),
            "value": t.number().optional(),
            "quantity": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TransactionDataItemOut"])
    types[
        "GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsResponseIn"
    ] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "relatedAccountGroupMemberships": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupMembershipIn"
                    ]
                )
            ).optional(),
        }
    ).named(
        renames[
            "GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsResponseIn"
        ]
    )
    types[
        "GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsResponseOut"
    ] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "relatedAccountGroupMemberships": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupMembershipOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsResponseOut"
        ]
    )
    types["GoogleCloudRecaptchaenterpriseV1TransactionDataUserIn"] = t.struct(
        {
            "creationMs": t.string().optional(),
            "phoneNumber": t.string().optional(),
            "accountId": t.string().optional(),
            "phoneVerified": t.boolean().optional(),
            "emailVerified": t.boolean().optional(),
            "email": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TransactionDataUserIn"])
    types["GoogleCloudRecaptchaenterpriseV1TransactionDataUserOut"] = t.struct(
        {
            "creationMs": t.string().optional(),
            "phoneNumber": t.string().optional(),
            "accountId": t.string().optional(),
            "phoneVerified": t.boolean().optional(),
            "emailVerified": t.boolean().optional(),
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TransactionDataUserOut"])
    types["GoogleCloudRecaptchaenterpriseV1TokenPropertiesIn"] = t.struct(
        {
            "action": t.string().optional(),
            "valid": t.boolean().optional(),
            "createTime": t.string().optional(),
            "androidPackageName": t.string().optional(),
            "iosBundleId": t.string().optional(),
            "invalidReason": t.string().optional(),
            "hostname": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TokenPropertiesIn"])
    types["GoogleCloudRecaptchaenterpriseV1TokenPropertiesOut"] = t.struct(
        {
            "action": t.string().optional(),
            "valid": t.boolean().optional(),
            "createTime": t.string().optional(),
            "androidPackageName": t.string().optional(),
            "iosBundleId": t.string().optional(),
            "invalidReason": t.string().optional(),
            "hostname": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TokenPropertiesOut"])
    types["GoogleCloudRecaptchaenterpriseV1WafSettingsIn"] = t.struct(
        {"wafFeature": t.string(), "wafService": t.string()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1WafSettingsIn"])
    types["GoogleCloudRecaptchaenterpriseV1WafSettingsOut"] = t.struct(
        {
            "wafFeature": t.string(),
            "wafService": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1WafSettingsOut"])
    types["GoogleCloudRecaptchaenterpriseV1FirewallActionRedirectActionIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1FirewallActionRedirectActionIn"])
    types["GoogleCloudRecaptchaenterpriseV1FirewallActionRedirectActionOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1FirewallActionRedirectActionOut"])
    types["GoogleCloudRecaptchaenterpriseV1ListKeysResponseIn"] = t.struct(
        {
            "keys": t.array(
                t.proxy(renames["GoogleCloudRecaptchaenterpriseV1KeyIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1ListKeysResponseIn"])
    types["GoogleCloudRecaptchaenterpriseV1ListKeysResponseOut"] = t.struct(
        {
            "keys": t.array(
                t.proxy(renames["GoogleCloudRecaptchaenterpriseV1KeyOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1ListKeysResponseOut"])
    types["GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentIn"] = t.struct(
        {
            "transactionRisk": t.number().optional(),
            "stolenInstrumentVerdict": t.proxy(
                renames[
                    "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentStolenInstrumentVerdictIn"
                ]
            ).optional(),
            "cardTestingVerdict": t.proxy(
                renames[
                    "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentCardTestingVerdictIn"
                ]
            ).optional(),
            "behavioralTrustVerdict": t.proxy(
                renames[
                    "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentBehavioralTrustVerdictIn"
                ]
            ).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentIn"])
    types["GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentOut"] = t.struct(
        {
            "transactionRisk": t.number().optional(),
            "stolenInstrumentVerdict": t.proxy(
                renames[
                    "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentStolenInstrumentVerdictOut"
                ]
            ).optional(),
            "cardTestingVerdict": t.proxy(
                renames[
                    "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentCardTestingVerdictOut"
                ]
            ).optional(),
            "behavioralTrustVerdict": t.proxy(
                renames[
                    "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentBehavioralTrustVerdictOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentOut"])
    types["GoogleCloudRecaptchaenterpriseV1AccountDefenderAssessmentIn"] = t.struct(
        {"labels": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1AccountDefenderAssessmentIn"])
    types["GoogleCloudRecaptchaenterpriseV1AccountDefenderAssessmentOut"] = t.struct(
        {
            "labels": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1AccountDefenderAssessmentOut"])
    types[
        "GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsRequestIn"
    ] = t.struct(
        {
            "hashedAccountId": t.string().optional(),
            "pageSize": t.integer().optional(),
            "pageToken": t.string().optional(),
        }
    ).named(
        renames[
            "GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsRequestIn"
        ]
    )
    types[
        "GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsRequestOut"
    ] = t.struct(
        {
            "hashedAccountId": t.string().optional(),
            "pageSize": t.integer().optional(),
            "pageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsRequestOut"
        ]
    )
    types["GoogleCloudRecaptchaenterpriseV1TestingOptionsIn"] = t.struct(
        {
            "testingChallenge": t.string().optional(),
            "testingScore": t.number().optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TestingOptionsIn"])
    types["GoogleCloudRecaptchaenterpriseV1TestingOptionsOut"] = t.struct(
        {
            "testingChallenge": t.string().optional(),
            "testingScore": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TestingOptionsOut"])
    types["GoogleCloudRecaptchaenterpriseV1FirewallActionBlockActionIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1FirewallActionBlockActionIn"])
    types["GoogleCloudRecaptchaenterpriseV1FirewallActionBlockActionOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1FirewallActionBlockActionOut"])
    types["GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentResponseIn"])
    types["GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentResponseOut"])
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
    types[
        "GoogleCloudRecaptchaenterpriseV1RetrieveLegacySecretKeyResponseIn"
    ] = t.struct({"legacySecretKey": t.string().optional()}).named(
        renames["GoogleCloudRecaptchaenterpriseV1RetrieveLegacySecretKeyResponseIn"]
    )
    types[
        "GoogleCloudRecaptchaenterpriseV1RetrieveLegacySecretKeyResponseOut"
    ] = t.struct(
        {
            "legacySecretKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudRecaptchaenterpriseV1RetrieveLegacySecretKeyResponseOut"]
    )
    types["GoogleCloudRecaptchaenterpriseV1IOSKeySettingsIn"] = t.struct(
        {
            "allowedBundleIds": t.array(t.string()).optional(),
            "allowAllBundleIds": t.boolean().optional(),
            "appleDeveloperId": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1AppleDeveloperIdIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1IOSKeySettingsIn"])
    types["GoogleCloudRecaptchaenterpriseV1IOSKeySettingsOut"] = t.struct(
        {
            "allowedBundleIds": t.array(t.string()).optional(),
            "allowAllBundleIds": t.boolean().optional(),
            "appleDeveloperId": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1AppleDeveloperIdOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1IOSKeySettingsOut"])
    types["GoogleCloudRecaptchaenterpriseV1EndpointVerificationInfoIn"] = t.struct(
        {"phoneNumber": t.string().optional(), "emailAddress": t.string().optional()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1EndpointVerificationInfoIn"])
    types["GoogleCloudRecaptchaenterpriseV1EndpointVerificationInfoOut"] = t.struct(
        {
            "phoneNumber": t.string().optional(),
            "requestToken": t.string().optional(),
            "emailAddress": t.string().optional(),
            "lastVerificationTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1EndpointVerificationInfoOut"])
    types["GoogleCloudRecaptchaenterpriseV1ListFirewallPoliciesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "firewallPolicies": t.array(
                t.proxy(renames["GoogleCloudRecaptchaenterpriseV1FirewallPolicyIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1ListFirewallPoliciesResponseIn"])
    types["GoogleCloudRecaptchaenterpriseV1ListFirewallPoliciesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "firewallPolicies": t.array(
                t.proxy(renames["GoogleCloudRecaptchaenterpriseV1FirewallPolicyOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1ListFirewallPoliciesResponseOut"])
    types["GoogleCloudRecaptchaenterpriseV1ChallengeMetricsIn"] = t.struct(
        {
            "pageloadCount": t.string().optional(),
            "nocaptchaCount": t.string().optional(),
            "passedCount": t.string().optional(),
            "failedCount": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1ChallengeMetricsIn"])
    types["GoogleCloudRecaptchaenterpriseV1ChallengeMetricsOut"] = t.struct(
        {
            "pageloadCount": t.string().optional(),
            "nocaptchaCount": t.string().optional(),
            "passedCount": t.string().optional(),
            "failedCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1ChallengeMetricsOut"])
    types["GoogleCloudRecaptchaenterpriseV1AccountVerificationInfoIn"] = t.struct(
        {
            "endpoints": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudRecaptchaenterpriseV1EndpointVerificationInfoIn"
                    ]
                )
            ).optional(),
            "languageCode": t.string().optional(),
            "username": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1AccountVerificationInfoIn"])
    types["GoogleCloudRecaptchaenterpriseV1AccountVerificationInfoOut"] = t.struct(
        {
            "latestVerificationResult": t.string().optional(),
            "endpoints": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudRecaptchaenterpriseV1EndpointVerificationInfoOut"
                    ]
                )
            ).optional(),
            "languageCode": t.string().optional(),
            "username": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1AccountVerificationInfoOut"])
    types[
        "GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupMembershipsResponseIn"
    ] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "relatedAccountGroupMemberships": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupMembershipIn"
                    ]
                )
            ).optional(),
        }
    ).named(
        renames[
            "GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupMembershipsResponseIn"
        ]
    )
    types[
        "GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupMembershipsResponseOut"
    ] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "relatedAccountGroupMemberships": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupMembershipOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupMembershipsResponseOut"
        ]
    )
    types["GoogleCloudRecaptchaenterpriseV1MigrateKeyRequestIn"] = t.struct(
        {"skipBillingCheck": t.boolean().optional()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1MigrateKeyRequestIn"])
    types["GoogleCloudRecaptchaenterpriseV1MigrateKeyRequestOut"] = t.struct(
        {
            "skipBillingCheck": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1MigrateKeyRequestOut"])
    types["GoogleCloudRecaptchaenterpriseV1TransactionDataAddressIn"] = t.struct(
        {
            "regionCode": t.string().optional(),
            "recipient": t.string().optional(),
            "postalCode": t.string().optional(),
            "address": t.array(t.string()).optional(),
            "administrativeArea": t.string().optional(),
            "locality": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TransactionDataAddressIn"])
    types["GoogleCloudRecaptchaenterpriseV1TransactionDataAddressOut"] = t.struct(
        {
            "regionCode": t.string().optional(),
            "recipient": t.string().optional(),
            "postalCode": t.string().optional(),
            "address": t.array(t.string()).optional(),
            "administrativeArea": t.string().optional(),
            "locality": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TransactionDataAddressOut"])
    types["GoogleCloudRecaptchaenterpriseV1EventIn"] = t.struct(
        {
            "express": t.boolean().optional(),
            "firewallPolicyEvaluation": t.boolean().optional(),
            "requestedUri": t.string().optional(),
            "expectedAction": t.string().optional(),
            "userIpAddress": t.string().optional(),
            "token": t.string().optional(),
            "wafTokenAssessment": t.boolean().optional(),
            "ja3": t.string().optional(),
            "transactionData": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TransactionDataIn"]
            ).optional(),
            "siteKey": t.string().optional(),
            "userAgent": t.string().optional(),
            "hashedAccountId": t.string().optional(),
            "headers": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1EventIn"])
    types["GoogleCloudRecaptchaenterpriseV1EventOut"] = t.struct(
        {
            "express": t.boolean().optional(),
            "firewallPolicyEvaluation": t.boolean().optional(),
            "requestedUri": t.string().optional(),
            "expectedAction": t.string().optional(),
            "userIpAddress": t.string().optional(),
            "token": t.string().optional(),
            "wafTokenAssessment": t.boolean().optional(),
            "ja3": t.string().optional(),
            "transactionData": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TransactionDataOut"]
            ).optional(),
            "siteKey": t.string().optional(),
            "userAgent": t.string().optional(),
            "hashedAccountId": t.string().optional(),
            "headers": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1EventOut"])

    functions = {}
    functions["projectsAssessmentsAnnotate"] = recaptchaenterprise.post(
        "v1/{parent}/assessments",
        t.struct(
            {
                "parent": t.string(),
                "accountVerification": t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1AccountVerificationInfoIn"]
                ).optional(),
                "privatePasswordLeakVerification": t.proxy(
                    renames[
                        "GoogleCloudRecaptchaenterpriseV1PrivatePasswordLeakVerificationIn"
                    ]
                ).optional(),
                "fraudPreventionAssessment": t.proxy(
                    renames[
                        "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentIn"
                    ]
                ).optional(),
                "accountDefenderAssessment": t.proxy(
                    renames[
                        "GoogleCloudRecaptchaenterpriseV1AccountDefenderAssessmentIn"
                    ]
                ).optional(),
                "event": t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1EventIn"]
                ).optional(),
                "firewallPolicyAssessment": t.proxy(
                    renames[
                        "GoogleCloudRecaptchaenterpriseV1FirewallPolicyAssessmentIn"
                    ]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecaptchaenterpriseV1AssessmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAssessmentsCreate"] = recaptchaenterprise.post(
        "v1/{parent}/assessments",
        t.struct(
            {
                "parent": t.string(),
                "accountVerification": t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1AccountVerificationInfoIn"]
                ).optional(),
                "privatePasswordLeakVerification": t.proxy(
                    renames[
                        "GoogleCloudRecaptchaenterpriseV1PrivatePasswordLeakVerificationIn"
                    ]
                ).optional(),
                "fraudPreventionAssessment": t.proxy(
                    renames[
                        "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentIn"
                    ]
                ).optional(),
                "accountDefenderAssessment": t.proxy(
                    renames[
                        "GoogleCloudRecaptchaenterpriseV1AccountDefenderAssessmentIn"
                    ]
                ).optional(),
                "event": t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1EventIn"]
                ).optional(),
                "firewallPolicyAssessment": t.proxy(
                    renames[
                        "GoogleCloudRecaptchaenterpriseV1FirewallPolicyAssessmentIn"
                    ]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecaptchaenterpriseV1AssessmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRelatedaccountgroupsList"] = recaptchaenterprise.get(
        "v1/{parent}/relatedaccountgroups",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames[
                "GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupsResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRelatedaccountgroupsMembershipsList"] = recaptchaenterprise.get(
        "v1/{parent}/memberships",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames[
                "GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupMembershipsResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsFirewallpoliciesCreate"] = recaptchaenterprise.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRecaptchaenterpriseV1FirewallPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsFirewallpoliciesDelete"] = recaptchaenterprise.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRecaptchaenterpriseV1FirewallPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsFirewallpoliciesPatch"] = recaptchaenterprise.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRecaptchaenterpriseV1FirewallPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsFirewallpoliciesList"] = recaptchaenterprise.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRecaptchaenterpriseV1FirewallPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsFirewallpoliciesGet"] = recaptchaenterprise.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRecaptchaenterpriseV1FirewallPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsKeysPatch"] = recaptchaenterprise.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRecaptchaenterpriseV1MetricsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsKeysDelete"] = recaptchaenterprise.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRecaptchaenterpriseV1MetricsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsKeysCreate"] = recaptchaenterprise.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRecaptchaenterpriseV1MetricsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsKeysRetrieveLegacySecretKey"] = recaptchaenterprise.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRecaptchaenterpriseV1MetricsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsKeysList"] = recaptchaenterprise.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRecaptchaenterpriseV1MetricsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsKeysGet"] = recaptchaenterprise.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRecaptchaenterpriseV1MetricsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsKeysMigrate"] = recaptchaenterprise.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRecaptchaenterpriseV1MetricsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsKeysGetMetrics"] = recaptchaenterprise.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRecaptchaenterpriseV1MetricsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsRelatedaccountgroupmembershipsSearch"
    ] = recaptchaenterprise.post(
        "v1/{project}/relatedaccountgroupmemberships:search",
        t.struct(
            {
                "project": t.string(),
                "hashedAccountId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames[
                "GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="recaptchaenterprise",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
