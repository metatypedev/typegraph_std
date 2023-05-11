from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_recaptchaenterprise() -> Import:
    recaptchaenterprise = HTTPRuntime("https://recaptchaenterprise.googleapis.com/")

    renames = {
        "ErrorResponse": "_recaptchaenterprise_1_ErrorResponse",
        "GoogleCloudRecaptchaenterpriseV1ScoreDistributionIn": "_recaptchaenterprise_2_GoogleCloudRecaptchaenterpriseV1ScoreDistributionIn",
        "GoogleCloudRecaptchaenterpriseV1ScoreDistributionOut": "_recaptchaenterprise_3_GoogleCloudRecaptchaenterpriseV1ScoreDistributionOut",
        "GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupMembershipsResponseIn": "_recaptchaenterprise_4_GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupMembershipsResponseIn",
        "GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupMembershipsResponseOut": "_recaptchaenterprise_5_GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupMembershipsResponseOut",
        "GoogleCloudRecaptchaenterpriseV1EventIn": "_recaptchaenterprise_6_GoogleCloudRecaptchaenterpriseV1EventIn",
        "GoogleCloudRecaptchaenterpriseV1EventOut": "_recaptchaenterprise_7_GoogleCloudRecaptchaenterpriseV1EventOut",
        "GoogleCloudRecaptchaenterpriseV1TransactionDataGatewayInfoIn": "_recaptchaenterprise_8_GoogleCloudRecaptchaenterpriseV1TransactionDataGatewayInfoIn",
        "GoogleCloudRecaptchaenterpriseV1TransactionDataGatewayInfoOut": "_recaptchaenterprise_9_GoogleCloudRecaptchaenterpriseV1TransactionDataGatewayInfoOut",
        "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentIn": "_recaptchaenterprise_10_GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentIn",
        "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentOut": "_recaptchaenterprise_11_GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentOut",
        "GoogleCloudRecaptchaenterpriseV1ScoreMetricsIn": "_recaptchaenterprise_12_GoogleCloudRecaptchaenterpriseV1ScoreMetricsIn",
        "GoogleCloudRecaptchaenterpriseV1ScoreMetricsOut": "_recaptchaenterprise_13_GoogleCloudRecaptchaenterpriseV1ScoreMetricsOut",
        "GoogleCloudRecaptchaenterpriseV1TransactionDataAddressIn": "_recaptchaenterprise_14_GoogleCloudRecaptchaenterpriseV1TransactionDataAddressIn",
        "GoogleCloudRecaptchaenterpriseV1TransactionDataAddressOut": "_recaptchaenterprise_15_GoogleCloudRecaptchaenterpriseV1TransactionDataAddressOut",
        "GoogleCloudRecaptchaenterpriseV1FirewallActionBlockActionIn": "_recaptchaenterprise_16_GoogleCloudRecaptchaenterpriseV1FirewallActionBlockActionIn",
        "GoogleCloudRecaptchaenterpriseV1FirewallActionBlockActionOut": "_recaptchaenterprise_17_GoogleCloudRecaptchaenterpriseV1FirewallActionBlockActionOut",
        "GoogleCloudRecaptchaenterpriseV1MigrateKeyRequestIn": "_recaptchaenterprise_18_GoogleCloudRecaptchaenterpriseV1MigrateKeyRequestIn",
        "GoogleCloudRecaptchaenterpriseV1MigrateKeyRequestOut": "_recaptchaenterprise_19_GoogleCloudRecaptchaenterpriseV1MigrateKeyRequestOut",
        "GoogleCloudRecaptchaenterpriseV1FirewallActionRedirectActionIn": "_recaptchaenterprise_20_GoogleCloudRecaptchaenterpriseV1FirewallActionRedirectActionIn",
        "GoogleCloudRecaptchaenterpriseV1FirewallActionRedirectActionOut": "_recaptchaenterprise_21_GoogleCloudRecaptchaenterpriseV1FirewallActionRedirectActionOut",
        "GoogleCloudRecaptchaenterpriseV1IOSKeySettingsIn": "_recaptchaenterprise_22_GoogleCloudRecaptchaenterpriseV1IOSKeySettingsIn",
        "GoogleCloudRecaptchaenterpriseV1IOSKeySettingsOut": "_recaptchaenterprise_23_GoogleCloudRecaptchaenterpriseV1IOSKeySettingsOut",
        "GoogleCloudRecaptchaenterpriseV1AccountDefenderAssessmentIn": "_recaptchaenterprise_24_GoogleCloudRecaptchaenterpriseV1AccountDefenderAssessmentIn",
        "GoogleCloudRecaptchaenterpriseV1AccountDefenderAssessmentOut": "_recaptchaenterprise_25_GoogleCloudRecaptchaenterpriseV1AccountDefenderAssessmentOut",
        "GoogleCloudRecaptchaenterpriseV1TestingOptionsIn": "_recaptchaenterprise_26_GoogleCloudRecaptchaenterpriseV1TestingOptionsIn",
        "GoogleCloudRecaptchaenterpriseV1TestingOptionsOut": "_recaptchaenterprise_27_GoogleCloudRecaptchaenterpriseV1TestingOptionsOut",
        "GoogleCloudRecaptchaenterpriseV1FirewallPolicyIn": "_recaptchaenterprise_28_GoogleCloudRecaptchaenterpriseV1FirewallPolicyIn",
        "GoogleCloudRecaptchaenterpriseV1FirewallPolicyOut": "_recaptchaenterprise_29_GoogleCloudRecaptchaenterpriseV1FirewallPolicyOut",
        "GoogleCloudRecaptchaenterpriseV1WafSettingsIn": "_recaptchaenterprise_30_GoogleCloudRecaptchaenterpriseV1WafSettingsIn",
        "GoogleCloudRecaptchaenterpriseV1WafSettingsOut": "_recaptchaenterprise_31_GoogleCloudRecaptchaenterpriseV1WafSettingsOut",
        "GoogleCloudRecaptchaenterpriseV1RiskAnalysisIn": "_recaptchaenterprise_32_GoogleCloudRecaptchaenterpriseV1RiskAnalysisIn",
        "GoogleCloudRecaptchaenterpriseV1RiskAnalysisOut": "_recaptchaenterprise_33_GoogleCloudRecaptchaenterpriseV1RiskAnalysisOut",
        "GoogleRpcStatusIn": "_recaptchaenterprise_34_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_recaptchaenterprise_35_GoogleRpcStatusOut",
        "GoogleCloudRecaptchaenterpriseV1ListFirewallPoliciesResponseIn": "_recaptchaenterprise_36_GoogleCloudRecaptchaenterpriseV1ListFirewallPoliciesResponseIn",
        "GoogleCloudRecaptchaenterpriseV1ListFirewallPoliciesResponseOut": "_recaptchaenterprise_37_GoogleCloudRecaptchaenterpriseV1ListFirewallPoliciesResponseOut",
        "GoogleCloudRecaptchaenterpriseV1AccountVerificationInfoIn": "_recaptchaenterprise_38_GoogleCloudRecaptchaenterpriseV1AccountVerificationInfoIn",
        "GoogleCloudRecaptchaenterpriseV1AccountVerificationInfoOut": "_recaptchaenterprise_39_GoogleCloudRecaptchaenterpriseV1AccountVerificationInfoOut",
        "GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentRequestIn": "_recaptchaenterprise_40_GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentRequestIn",
        "GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentRequestOut": "_recaptchaenterprise_41_GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentRequestOut",
        "GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsRequestIn": "_recaptchaenterprise_42_GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsRequestIn",
        "GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsRequestOut": "_recaptchaenterprise_43_GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsRequestOut",
        "GoogleCloudRecaptchaenterpriseV1TransactionDataUserIn": "_recaptchaenterprise_44_GoogleCloudRecaptchaenterpriseV1TransactionDataUserIn",
        "GoogleCloudRecaptchaenterpriseV1TransactionDataUserOut": "_recaptchaenterprise_45_GoogleCloudRecaptchaenterpriseV1TransactionDataUserOut",
        "GoogleCloudRecaptchaenterpriseV1FirewallPolicyAssessmentIn": "_recaptchaenterprise_46_GoogleCloudRecaptchaenterpriseV1FirewallPolicyAssessmentIn",
        "GoogleCloudRecaptchaenterpriseV1FirewallPolicyAssessmentOut": "_recaptchaenterprise_47_GoogleCloudRecaptchaenterpriseV1FirewallPolicyAssessmentOut",
        "GoogleProtobufEmptyIn": "_recaptchaenterprise_48_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_recaptchaenterprise_49_GoogleProtobufEmptyOut",
        "GoogleCloudRecaptchaenterpriseV1FirewallActionSetHeaderActionIn": "_recaptchaenterprise_50_GoogleCloudRecaptchaenterpriseV1FirewallActionSetHeaderActionIn",
        "GoogleCloudRecaptchaenterpriseV1FirewallActionSetHeaderActionOut": "_recaptchaenterprise_51_GoogleCloudRecaptchaenterpriseV1FirewallActionSetHeaderActionOut",
        "GoogleCloudRecaptchaenterpriseV1EndpointVerificationInfoIn": "_recaptchaenterprise_52_GoogleCloudRecaptchaenterpriseV1EndpointVerificationInfoIn",
        "GoogleCloudRecaptchaenterpriseV1EndpointVerificationInfoOut": "_recaptchaenterprise_53_GoogleCloudRecaptchaenterpriseV1EndpointVerificationInfoOut",
        "GoogleCloudRecaptchaenterpriseV1FirewallActionIn": "_recaptchaenterprise_54_GoogleCloudRecaptchaenterpriseV1FirewallActionIn",
        "GoogleCloudRecaptchaenterpriseV1FirewallActionOut": "_recaptchaenterprise_55_GoogleCloudRecaptchaenterpriseV1FirewallActionOut",
        "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentCardTestingVerdictIn": "_recaptchaenterprise_56_GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentCardTestingVerdictIn",
        "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentCardTestingVerdictOut": "_recaptchaenterprise_57_GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentCardTestingVerdictOut",
        "GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupsResponseIn": "_recaptchaenterprise_58_GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupsResponseIn",
        "GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupsResponseOut": "_recaptchaenterprise_59_GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupsResponseOut",
        "GoogleCloudRecaptchaenterpriseV1MetricsIn": "_recaptchaenterprise_60_GoogleCloudRecaptchaenterpriseV1MetricsIn",
        "GoogleCloudRecaptchaenterpriseV1MetricsOut": "_recaptchaenterprise_61_GoogleCloudRecaptchaenterpriseV1MetricsOut",
        "GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsResponseIn": "_recaptchaenterprise_62_GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsResponseIn",
        "GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsResponseOut": "_recaptchaenterprise_63_GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsResponseOut",
        "GoogleCloudRecaptchaenterpriseV1WebKeySettingsIn": "_recaptchaenterprise_64_GoogleCloudRecaptchaenterpriseV1WebKeySettingsIn",
        "GoogleCloudRecaptchaenterpriseV1WebKeySettingsOut": "_recaptchaenterprise_65_GoogleCloudRecaptchaenterpriseV1WebKeySettingsOut",
        "GoogleCloudRecaptchaenterpriseV1TransactionDataItemIn": "_recaptchaenterprise_66_GoogleCloudRecaptchaenterpriseV1TransactionDataItemIn",
        "GoogleCloudRecaptchaenterpriseV1TransactionDataItemOut": "_recaptchaenterprise_67_GoogleCloudRecaptchaenterpriseV1TransactionDataItemOut",
        "GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentResponseIn": "_recaptchaenterprise_68_GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentResponseIn",
        "GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentResponseOut": "_recaptchaenterprise_69_GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentResponseOut",
        "GoogleCloudRecaptchaenterpriseV1FirewallActionAllowActionIn": "_recaptchaenterprise_70_GoogleCloudRecaptchaenterpriseV1FirewallActionAllowActionIn",
        "GoogleCloudRecaptchaenterpriseV1FirewallActionAllowActionOut": "_recaptchaenterprise_71_GoogleCloudRecaptchaenterpriseV1FirewallActionAllowActionOut",
        "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentBehavioralTrustVerdictIn": "_recaptchaenterprise_72_GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentBehavioralTrustVerdictIn",
        "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentBehavioralTrustVerdictOut": "_recaptchaenterprise_73_GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentBehavioralTrustVerdictOut",
        "GoogleCloudRecaptchaenterpriseV1FirewallActionSubstituteActionIn": "_recaptchaenterprise_74_GoogleCloudRecaptchaenterpriseV1FirewallActionSubstituteActionIn",
        "GoogleCloudRecaptchaenterpriseV1FirewallActionSubstituteActionOut": "_recaptchaenterprise_75_GoogleCloudRecaptchaenterpriseV1FirewallActionSubstituteActionOut",
        "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentStolenInstrumentVerdictIn": "_recaptchaenterprise_76_GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentStolenInstrumentVerdictIn",
        "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentStolenInstrumentVerdictOut": "_recaptchaenterprise_77_GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentStolenInstrumentVerdictOut",
        "GoogleCloudRecaptchaenterpriseV1TransactionDataIn": "_recaptchaenterprise_78_GoogleCloudRecaptchaenterpriseV1TransactionDataIn",
        "GoogleCloudRecaptchaenterpriseV1TransactionDataOut": "_recaptchaenterprise_79_GoogleCloudRecaptchaenterpriseV1TransactionDataOut",
        "GoogleCloudRecaptchaenterpriseV1ChallengeMetricsIn": "_recaptchaenterprise_80_GoogleCloudRecaptchaenterpriseV1ChallengeMetricsIn",
        "GoogleCloudRecaptchaenterpriseV1ChallengeMetricsOut": "_recaptchaenterprise_81_GoogleCloudRecaptchaenterpriseV1ChallengeMetricsOut",
        "GoogleCloudRecaptchaenterpriseV1ListKeysResponseIn": "_recaptchaenterprise_82_GoogleCloudRecaptchaenterpriseV1ListKeysResponseIn",
        "GoogleCloudRecaptchaenterpriseV1ListKeysResponseOut": "_recaptchaenterprise_83_GoogleCloudRecaptchaenterpriseV1ListKeysResponseOut",
        "GoogleCloudRecaptchaenterpriseV1RetrieveLegacySecretKeyResponseIn": "_recaptchaenterprise_84_GoogleCloudRecaptchaenterpriseV1RetrieveLegacySecretKeyResponseIn",
        "GoogleCloudRecaptchaenterpriseV1RetrieveLegacySecretKeyResponseOut": "_recaptchaenterprise_85_GoogleCloudRecaptchaenterpriseV1RetrieveLegacySecretKeyResponseOut",
        "GoogleCloudRecaptchaenterpriseV1TransactionEventIn": "_recaptchaenterprise_86_GoogleCloudRecaptchaenterpriseV1TransactionEventIn",
        "GoogleCloudRecaptchaenterpriseV1TransactionEventOut": "_recaptchaenterprise_87_GoogleCloudRecaptchaenterpriseV1TransactionEventOut",
        "GoogleCloudRecaptchaenterpriseV1AndroidKeySettingsIn": "_recaptchaenterprise_88_GoogleCloudRecaptchaenterpriseV1AndroidKeySettingsIn",
        "GoogleCloudRecaptchaenterpriseV1AndroidKeySettingsOut": "_recaptchaenterprise_89_GoogleCloudRecaptchaenterpriseV1AndroidKeySettingsOut",
        "GoogleCloudRecaptchaenterpriseV1AssessmentIn": "_recaptchaenterprise_90_GoogleCloudRecaptchaenterpriseV1AssessmentIn",
        "GoogleCloudRecaptchaenterpriseV1AssessmentOut": "_recaptchaenterprise_91_GoogleCloudRecaptchaenterpriseV1AssessmentOut",
        "GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupIn": "_recaptchaenterprise_92_GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupIn",
        "GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupOut": "_recaptchaenterprise_93_GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupOut",
        "GoogleCloudRecaptchaenterpriseV1PrivatePasswordLeakVerificationIn": "_recaptchaenterprise_94_GoogleCloudRecaptchaenterpriseV1PrivatePasswordLeakVerificationIn",
        "GoogleCloudRecaptchaenterpriseV1PrivatePasswordLeakVerificationOut": "_recaptchaenterprise_95_GoogleCloudRecaptchaenterpriseV1PrivatePasswordLeakVerificationOut",
        "GoogleCloudRecaptchaenterpriseV1TokenPropertiesIn": "_recaptchaenterprise_96_GoogleCloudRecaptchaenterpriseV1TokenPropertiesIn",
        "GoogleCloudRecaptchaenterpriseV1TokenPropertiesOut": "_recaptchaenterprise_97_GoogleCloudRecaptchaenterpriseV1TokenPropertiesOut",
        "GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupMembershipIn": "_recaptchaenterprise_98_GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupMembershipIn",
        "GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupMembershipOut": "_recaptchaenterprise_99_GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupMembershipOut",
        "GoogleCloudRecaptchaenterpriseV1KeyIn": "_recaptchaenterprise_100_GoogleCloudRecaptchaenterpriseV1KeyIn",
        "GoogleCloudRecaptchaenterpriseV1KeyOut": "_recaptchaenterprise_101_GoogleCloudRecaptchaenterpriseV1KeyOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudRecaptchaenterpriseV1ScoreDistributionIn"] = t.struct(
        {"scoreBuckets": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1ScoreDistributionIn"])
    types["GoogleCloudRecaptchaenterpriseV1ScoreDistributionOut"] = t.struct(
        {
            "scoreBuckets": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1ScoreDistributionOut"])
    types[
        "GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupMembershipsResponseIn"
    ] = t.struct(
        {
            "relatedAccountGroupMemberships": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupMembershipIn"
                    ]
                )
            ).optional(),
            "nextPageToken": t.string().optional(),
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
            "relatedAccountGroupMemberships": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupMembershipOut"
                    ]
                )
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupMembershipsResponseOut"
        ]
    )
    types["GoogleCloudRecaptchaenterpriseV1EventIn"] = t.struct(
        {
            "transactionData": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TransactionDataIn"]
            ).optional(),
            "wafTokenAssessment": t.boolean().optional(),
            "token": t.string().optional(),
            "firewallPolicyEvaluation": t.boolean().optional(),
            "requestedUri": t.string().optional(),
            "express": t.boolean().optional(),
            "hashedAccountId": t.string().optional(),
            "headers": t.array(t.string()).optional(),
            "userAgent": t.string().optional(),
            "ja3": t.string().optional(),
            "userIpAddress": t.string().optional(),
            "expectedAction": t.string().optional(),
            "siteKey": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1EventIn"])
    types["GoogleCloudRecaptchaenterpriseV1EventOut"] = t.struct(
        {
            "transactionData": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TransactionDataOut"]
            ).optional(),
            "wafTokenAssessment": t.boolean().optional(),
            "token": t.string().optional(),
            "firewallPolicyEvaluation": t.boolean().optional(),
            "requestedUri": t.string().optional(),
            "express": t.boolean().optional(),
            "hashedAccountId": t.string().optional(),
            "headers": t.array(t.string()).optional(),
            "userAgent": t.string().optional(),
            "ja3": t.string().optional(),
            "userIpAddress": t.string().optional(),
            "expectedAction": t.string().optional(),
            "siteKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1EventOut"])
    types["GoogleCloudRecaptchaenterpriseV1TransactionDataGatewayInfoIn"] = t.struct(
        {
            "name": t.string().optional(),
            "cvvResponseCode": t.string().optional(),
            "avsResponseCode": t.string().optional(),
            "gatewayResponseCode": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TransactionDataGatewayInfoIn"])
    types["GoogleCloudRecaptchaenterpriseV1TransactionDataGatewayInfoOut"] = t.struct(
        {
            "name": t.string().optional(),
            "cvvResponseCode": t.string().optional(),
            "avsResponseCode": t.string().optional(),
            "gatewayResponseCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TransactionDataGatewayInfoOut"])
    types["GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentIn"] = t.struct(
        {
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
            "transactionRisk": t.number().optional(),
            "stolenInstrumentVerdict": t.proxy(
                renames[
                    "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentStolenInstrumentVerdictIn"
                ]
            ).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentIn"])
    types["GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentOut"] = t.struct(
        {
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
            "transactionRisk": t.number().optional(),
            "stolenInstrumentVerdict": t.proxy(
                renames[
                    "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentStolenInstrumentVerdictOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentOut"])
    types["GoogleCloudRecaptchaenterpriseV1ScoreMetricsIn"] = t.struct(
        {
            "actionMetrics": t.struct({"_": t.string().optional()}).optional(),
            "overallMetrics": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1ScoreDistributionIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1ScoreMetricsIn"])
    types["GoogleCloudRecaptchaenterpriseV1ScoreMetricsOut"] = t.struct(
        {
            "actionMetrics": t.struct({"_": t.string().optional()}).optional(),
            "overallMetrics": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1ScoreDistributionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1ScoreMetricsOut"])
    types["GoogleCloudRecaptchaenterpriseV1TransactionDataAddressIn"] = t.struct(
        {
            "recipient": t.string().optional(),
            "address": t.array(t.string()).optional(),
            "regionCode": t.string().optional(),
            "postalCode": t.string().optional(),
            "locality": t.string().optional(),
            "administrativeArea": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TransactionDataAddressIn"])
    types["GoogleCloudRecaptchaenterpriseV1TransactionDataAddressOut"] = t.struct(
        {
            "recipient": t.string().optional(),
            "address": t.array(t.string()).optional(),
            "regionCode": t.string().optional(),
            "postalCode": t.string().optional(),
            "locality": t.string().optional(),
            "administrativeArea": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TransactionDataAddressOut"])
    types["GoogleCloudRecaptchaenterpriseV1FirewallActionBlockActionIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1FirewallActionBlockActionIn"])
    types["GoogleCloudRecaptchaenterpriseV1FirewallActionBlockActionOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1FirewallActionBlockActionOut"])
    types["GoogleCloudRecaptchaenterpriseV1MigrateKeyRequestIn"] = t.struct(
        {"skipBillingCheck": t.boolean().optional()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1MigrateKeyRequestIn"])
    types["GoogleCloudRecaptchaenterpriseV1MigrateKeyRequestOut"] = t.struct(
        {
            "skipBillingCheck": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1MigrateKeyRequestOut"])
    types["GoogleCloudRecaptchaenterpriseV1FirewallActionRedirectActionIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1FirewallActionRedirectActionIn"])
    types["GoogleCloudRecaptchaenterpriseV1FirewallActionRedirectActionOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1FirewallActionRedirectActionOut"])
    types["GoogleCloudRecaptchaenterpriseV1IOSKeySettingsIn"] = t.struct(
        {
            "allowedBundleIds": t.array(t.string()).optional(),
            "allowAllBundleIds": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1IOSKeySettingsIn"])
    types["GoogleCloudRecaptchaenterpriseV1IOSKeySettingsOut"] = t.struct(
        {
            "allowedBundleIds": t.array(t.string()).optional(),
            "allowAllBundleIds": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1IOSKeySettingsOut"])
    types["GoogleCloudRecaptchaenterpriseV1AccountDefenderAssessmentIn"] = t.struct(
        {"labels": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1AccountDefenderAssessmentIn"])
    types["GoogleCloudRecaptchaenterpriseV1AccountDefenderAssessmentOut"] = t.struct(
        {
            "labels": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1AccountDefenderAssessmentOut"])
    types["GoogleCloudRecaptchaenterpriseV1TestingOptionsIn"] = t.struct(
        {
            "testingScore": t.number().optional(),
            "testingChallenge": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TestingOptionsIn"])
    types["GoogleCloudRecaptchaenterpriseV1TestingOptionsOut"] = t.struct(
        {
            "testingScore": t.number().optional(),
            "testingChallenge": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TestingOptionsOut"])
    types["GoogleCloudRecaptchaenterpriseV1FirewallPolicyIn"] = t.struct(
        {
            "description": t.string().optional(),
            "actions": t.array(
                t.proxy(renames["GoogleCloudRecaptchaenterpriseV1FirewallActionIn"])
            ).optional(),
            "name": t.string().optional(),
            "path": t.string().optional(),
            "condition": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1FirewallPolicyIn"])
    types["GoogleCloudRecaptchaenterpriseV1FirewallPolicyOut"] = t.struct(
        {
            "description": t.string().optional(),
            "actions": t.array(
                t.proxy(renames["GoogleCloudRecaptchaenterpriseV1FirewallActionOut"])
            ).optional(),
            "name": t.string().optional(),
            "path": t.string().optional(),
            "condition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1FirewallPolicyOut"])
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
    types["GoogleCloudRecaptchaenterpriseV1RiskAnalysisIn"] = t.struct(
        {
            "reasons": t.array(t.string()).optional(),
            "extendedVerdictReasons": t.array(t.string()).optional(),
            "score": t.number().optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1RiskAnalysisIn"])
    types["GoogleCloudRecaptchaenterpriseV1RiskAnalysisOut"] = t.struct(
        {
            "reasons": t.array(t.string()).optional(),
            "extendedVerdictReasons": t.array(t.string()).optional(),
            "score": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1RiskAnalysisOut"])
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
    types["GoogleCloudRecaptchaenterpriseV1AccountVerificationInfoIn"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "endpoints": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudRecaptchaenterpriseV1EndpointVerificationInfoIn"
                    ]
                )
            ).optional(),
            "username": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1AccountVerificationInfoIn"])
    types["GoogleCloudRecaptchaenterpriseV1AccountVerificationInfoOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "endpoints": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudRecaptchaenterpriseV1EndpointVerificationInfoOut"
                    ]
                )
            ).optional(),
            "username": t.string().optional(),
            "latestVerificationResult": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1AccountVerificationInfoOut"])
    types["GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentRequestIn"] = t.struct(
        {
            "annotation": t.string().optional(),
            "hashedAccountId": t.string().optional(),
            "transactionEvent": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TransactionEventIn"]
            ).optional(),
            "reasons": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentRequestIn"])
    types["GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentRequestOut"] = t.struct(
        {
            "annotation": t.string().optional(),
            "hashedAccountId": t.string().optional(),
            "transactionEvent": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TransactionEventOut"]
            ).optional(),
            "reasons": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentRequestOut"])
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
    types["GoogleCloudRecaptchaenterpriseV1TransactionDataUserIn"] = t.struct(
        {
            "emailVerified": t.boolean().optional(),
            "phoneNumber": t.string().optional(),
            "creationMs": t.string().optional(),
            "accountId": t.string().optional(),
            "email": t.string().optional(),
            "phoneVerified": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TransactionDataUserIn"])
    types["GoogleCloudRecaptchaenterpriseV1TransactionDataUserOut"] = t.struct(
        {
            "emailVerified": t.boolean().optional(),
            "phoneNumber": t.string().optional(),
            "creationMs": t.string().optional(),
            "accountId": t.string().optional(),
            "email": t.string().optional(),
            "phoneVerified": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TransactionDataUserOut"])
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
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
    types["GoogleCloudRecaptchaenterpriseV1FirewallActionSetHeaderActionIn"] = t.struct(
        {"key": t.string().optional(), "value": t.string().optional()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1FirewallActionSetHeaderActionIn"])
    types[
        "GoogleCloudRecaptchaenterpriseV1FirewallActionSetHeaderActionOut"
    ] = t.struct(
        {
            "key": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudRecaptchaenterpriseV1FirewallActionSetHeaderActionOut"]
    )
    types["GoogleCloudRecaptchaenterpriseV1EndpointVerificationInfoIn"] = t.struct(
        {"emailAddress": t.string().optional(), "phoneNumber": t.string().optional()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1EndpointVerificationInfoIn"])
    types["GoogleCloudRecaptchaenterpriseV1EndpointVerificationInfoOut"] = t.struct(
        {
            "requestToken": t.string().optional(),
            "emailAddress": t.string().optional(),
            "phoneNumber": t.string().optional(),
            "lastVerificationTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1EndpointVerificationInfoOut"])
    types["GoogleCloudRecaptchaenterpriseV1FirewallActionIn"] = t.struct(
        {
            "setHeader": t.proxy(
                renames[
                    "GoogleCloudRecaptchaenterpriseV1FirewallActionSetHeaderActionIn"
                ]
            ).optional(),
            "allow": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1FirewallActionAllowActionIn"]
            ).optional(),
            "substitute": t.proxy(
                renames[
                    "GoogleCloudRecaptchaenterpriseV1FirewallActionSubstituteActionIn"
                ]
            ).optional(),
            "block": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1FirewallActionBlockActionIn"]
            ).optional(),
            "redirect": t.proxy(
                renames[
                    "GoogleCloudRecaptchaenterpriseV1FirewallActionRedirectActionIn"
                ]
            ).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1FirewallActionIn"])
    types["GoogleCloudRecaptchaenterpriseV1FirewallActionOut"] = t.struct(
        {
            "setHeader": t.proxy(
                renames[
                    "GoogleCloudRecaptchaenterpriseV1FirewallActionSetHeaderActionOut"
                ]
            ).optional(),
            "allow": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1FirewallActionAllowActionOut"]
            ).optional(),
            "substitute": t.proxy(
                renames[
                    "GoogleCloudRecaptchaenterpriseV1FirewallActionSubstituteActionOut"
                ]
            ).optional(),
            "block": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1FirewallActionBlockActionOut"]
            ).optional(),
            "redirect": t.proxy(
                renames[
                    "GoogleCloudRecaptchaenterpriseV1FirewallActionRedirectActionOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1FirewallActionOut"])
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
    types["GoogleCloudRecaptchaenterpriseV1MetricsIn"] = t.struct(
        {
            "challengeMetrics": t.array(
                t.proxy(renames["GoogleCloudRecaptchaenterpriseV1ChallengeMetricsIn"])
            ).optional(),
            "scoreMetrics": t.array(
                t.proxy(renames["GoogleCloudRecaptchaenterpriseV1ScoreMetricsIn"])
            ).optional(),
            "startTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1MetricsIn"])
    types["GoogleCloudRecaptchaenterpriseV1MetricsOut"] = t.struct(
        {
            "name": t.string().optional(),
            "challengeMetrics": t.array(
                t.proxy(renames["GoogleCloudRecaptchaenterpriseV1ChallengeMetricsOut"])
            ).optional(),
            "scoreMetrics": t.array(
                t.proxy(renames["GoogleCloudRecaptchaenterpriseV1ScoreMetricsOut"])
            ).optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1MetricsOut"])
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
    types["GoogleCloudRecaptchaenterpriseV1WebKeySettingsIn"] = t.struct(
        {
            "integrationType": t.string(),
            "allowAllDomains": t.boolean().optional(),
            "challengeSecurityPreference": t.string().optional(),
            "allowedDomains": t.array(t.string()).optional(),
            "allowAmpTraffic": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1WebKeySettingsIn"])
    types["GoogleCloudRecaptchaenterpriseV1WebKeySettingsOut"] = t.struct(
        {
            "integrationType": t.string(),
            "allowAllDomains": t.boolean().optional(),
            "challengeSecurityPreference": t.string().optional(),
            "allowedDomains": t.array(t.string()).optional(),
            "allowAmpTraffic": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1WebKeySettingsOut"])
    types["GoogleCloudRecaptchaenterpriseV1TransactionDataItemIn"] = t.struct(
        {
            "name": t.string().optional(),
            "merchantAccountId": t.string().optional(),
            "value": t.number().optional(),
            "quantity": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TransactionDataItemIn"])
    types["GoogleCloudRecaptchaenterpriseV1TransactionDataItemOut"] = t.struct(
        {
            "name": t.string().optional(),
            "merchantAccountId": t.string().optional(),
            "value": t.number().optional(),
            "quantity": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TransactionDataItemOut"])
    types["GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentResponseIn"])
    types["GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentResponseOut"])
    types["GoogleCloudRecaptchaenterpriseV1FirewallActionAllowActionIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1FirewallActionAllowActionIn"])
    types["GoogleCloudRecaptchaenterpriseV1FirewallActionAllowActionOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1FirewallActionAllowActionOut"])
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
    types["GoogleCloudRecaptchaenterpriseV1TransactionDataIn"] = t.struct(
        {
            "cardBin": t.string().optional(),
            "value": t.number().optional(),
            "items": t.array(
                t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1TransactionDataItemIn"]
                )
            ).optional(),
            "shippingAddress": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TransactionDataAddressIn"]
            ).optional(),
            "gatewayInfo": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TransactionDataGatewayInfoIn"]
            ).optional(),
            "paymentMethod": t.string().optional(),
            "merchants": t.array(
                t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1TransactionDataUserIn"]
                )
            ).optional(),
            "shippingValue": t.number().optional(),
            "transactionId": t.string().optional(),
            "billingAddress": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TransactionDataAddressIn"]
            ).optional(),
            "user": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TransactionDataUserIn"]
            ).optional(),
            "currencyCode": t.string().optional(),
            "cardLastFour": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TransactionDataIn"])
    types["GoogleCloudRecaptchaenterpriseV1TransactionDataOut"] = t.struct(
        {
            "cardBin": t.string().optional(),
            "value": t.number().optional(),
            "items": t.array(
                t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1TransactionDataItemOut"]
                )
            ).optional(),
            "shippingAddress": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TransactionDataAddressOut"]
            ).optional(),
            "gatewayInfo": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TransactionDataGatewayInfoOut"]
            ).optional(),
            "paymentMethod": t.string().optional(),
            "merchants": t.array(
                t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1TransactionDataUserOut"]
                )
            ).optional(),
            "shippingValue": t.number().optional(),
            "transactionId": t.string().optional(),
            "billingAddress": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TransactionDataAddressOut"]
            ).optional(),
            "user": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TransactionDataUserOut"]
            ).optional(),
            "currencyCode": t.string().optional(),
            "cardLastFour": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TransactionDataOut"])
    types["GoogleCloudRecaptchaenterpriseV1ChallengeMetricsIn"] = t.struct(
        {
            "passedCount": t.string().optional(),
            "nocaptchaCount": t.string().optional(),
            "failedCount": t.string().optional(),
            "pageloadCount": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1ChallengeMetricsIn"])
    types["GoogleCloudRecaptchaenterpriseV1ChallengeMetricsOut"] = t.struct(
        {
            "passedCount": t.string().optional(),
            "nocaptchaCount": t.string().optional(),
            "failedCount": t.string().optional(),
            "pageloadCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1ChallengeMetricsOut"])
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
    types["GoogleCloudRecaptchaenterpriseV1TransactionEventIn"] = t.struct(
        {
            "value": t.number().optional(),
            "eventTime": t.string().optional(),
            "eventType": t.string().optional(),
            "reason": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TransactionEventIn"])
    types["GoogleCloudRecaptchaenterpriseV1TransactionEventOut"] = t.struct(
        {
            "value": t.number().optional(),
            "eventTime": t.string().optional(),
            "eventType": t.string().optional(),
            "reason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TransactionEventOut"])
    types["GoogleCloudRecaptchaenterpriseV1AndroidKeySettingsIn"] = t.struct(
        {
            "supportNonGoogleAppStoreDistribution": t.boolean().optional(),
            "allowAllPackageNames": t.boolean().optional(),
            "allowedPackageNames": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1AndroidKeySettingsIn"])
    types["GoogleCloudRecaptchaenterpriseV1AndroidKeySettingsOut"] = t.struct(
        {
            "supportNonGoogleAppStoreDistribution": t.boolean().optional(),
            "allowAllPackageNames": t.boolean().optional(),
            "allowedPackageNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1AndroidKeySettingsOut"])
    types["GoogleCloudRecaptchaenterpriseV1AssessmentIn"] = t.struct(
        {
            "fraudPreventionAssessment": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentIn"]
            ).optional(),
            "event": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1EventIn"]
            ).optional(),
            "accountVerification": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1AccountVerificationInfoIn"]
            ).optional(),
            "accountDefenderAssessment": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1AccountDefenderAssessmentIn"]
            ).optional(),
            "firewallPolicyAssessment": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1FirewallPolicyAssessmentIn"]
            ).optional(),
            "privatePasswordLeakVerification": t.proxy(
                renames[
                    "GoogleCloudRecaptchaenterpriseV1PrivatePasswordLeakVerificationIn"
                ]
            ).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1AssessmentIn"])
    types["GoogleCloudRecaptchaenterpriseV1AssessmentOut"] = t.struct(
        {
            "tokenProperties": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TokenPropertiesOut"]
            ).optional(),
            "fraudPreventionAssessment": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentOut"]
            ).optional(),
            "event": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1EventOut"]
            ).optional(),
            "name": t.string().optional(),
            "accountVerification": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1AccountVerificationInfoOut"]
            ).optional(),
            "riskAnalysis": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1RiskAnalysisOut"]
            ).optional(),
            "accountDefenderAssessment": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1AccountDefenderAssessmentOut"]
            ).optional(),
            "firewallPolicyAssessment": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1FirewallPolicyAssessmentOut"]
            ).optional(),
            "privatePasswordLeakVerification": t.proxy(
                renames[
                    "GoogleCloudRecaptchaenterpriseV1PrivatePasswordLeakVerificationOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1AssessmentOut"])
    types["GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupIn"] = t.struct(
        {"name": t.string()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupIn"])
    types["GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupOut"] = t.struct(
        {"name": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupOut"])
    types[
        "GoogleCloudRecaptchaenterpriseV1PrivatePasswordLeakVerificationIn"
    ] = t.struct(
        {
            "encryptedUserCredentialsHash": t.string().optional(),
            "lookupHashPrefix": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudRecaptchaenterpriseV1PrivatePasswordLeakVerificationIn"]
    )
    types[
        "GoogleCloudRecaptchaenterpriseV1PrivatePasswordLeakVerificationOut"
    ] = t.struct(
        {
            "encryptedUserCredentialsHash": t.string().optional(),
            "reencryptedUserCredentialsHash": t.string().optional(),
            "lookupHashPrefix": t.string().optional(),
            "encryptedLeakMatchPrefixes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudRecaptchaenterpriseV1PrivatePasswordLeakVerificationOut"]
    )
    types["GoogleCloudRecaptchaenterpriseV1TokenPropertiesIn"] = t.struct(
        {
            "androidPackageName": t.string().optional(),
            "iosBundleId": t.string().optional(),
            "action": t.string().optional(),
            "valid": t.boolean().optional(),
            "createTime": t.string().optional(),
            "invalidReason": t.string().optional(),
            "hostname": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TokenPropertiesIn"])
    types["GoogleCloudRecaptchaenterpriseV1TokenPropertiesOut"] = t.struct(
        {
            "androidPackageName": t.string().optional(),
            "iosBundleId": t.string().optional(),
            "action": t.string().optional(),
            "valid": t.boolean().optional(),
            "createTime": t.string().optional(),
            "invalidReason": t.string().optional(),
            "hostname": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TokenPropertiesOut"])
    types["GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupMembershipIn"] = t.struct(
        {"hashedAccountId": t.string().optional(), "name": t.string()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupMembershipIn"])
    types[
        "GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupMembershipOut"
    ] = t.struct(
        {
            "hashedAccountId": t.string().optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupMembershipOut"]
    )
    types["GoogleCloudRecaptchaenterpriseV1KeyIn"] = t.struct(
        {
            "iosSettings": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1IOSKeySettingsIn"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "webSettings": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1WebKeySettingsIn"]
            ).optional(),
            "name": t.string().optional(),
            "testingOptions": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TestingOptionsIn"]
            ).optional(),
            "displayName": t.string().optional(),
            "wafSettings": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1WafSettingsIn"]
            ).optional(),
            "androidSettings": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1AndroidKeySettingsIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1KeyIn"])
    types["GoogleCloudRecaptchaenterpriseV1KeyOut"] = t.struct(
        {
            "iosSettings": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1IOSKeySettingsOut"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "webSettings": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1WebKeySettingsOut"]
            ).optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "testingOptions": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TestingOptionsOut"]
            ).optional(),
            "displayName": t.string().optional(),
            "wafSettings": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1WafSettingsOut"]
            ).optional(),
            "androidSettings": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1AndroidKeySettingsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1KeyOut"])

    functions = {}
    functions["projectsKeysList"] = recaptchaenterprise.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRecaptchaenterpriseV1KeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsKeysDelete"] = recaptchaenterprise.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRecaptchaenterpriseV1KeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsKeysRetrieveLegacySecretKey"] = recaptchaenterprise.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRecaptchaenterpriseV1KeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsKeysGetMetrics"] = recaptchaenterprise.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRecaptchaenterpriseV1KeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsKeysCreate"] = recaptchaenterprise.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRecaptchaenterpriseV1KeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsKeysPatch"] = recaptchaenterprise.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRecaptchaenterpriseV1KeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsKeysMigrate"] = recaptchaenterprise.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRecaptchaenterpriseV1KeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsKeysGet"] = recaptchaenterprise.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRecaptchaenterpriseV1KeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRelatedaccountgroupsList"] = recaptchaenterprise.get(
        "v1/{parent}/relatedaccountgroups",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
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
                "parent": t.string(),
                "pageToken": t.string().optional(),
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
    functions["projectsFirewallpoliciesList"] = recaptchaenterprise.post(
        "v1/{parent}/firewallpolicies",
        t.struct(
            {
                "parent": t.string(),
                "description": t.string().optional(),
                "actions": t.array(
                    t.proxy(renames["GoogleCloudRecaptchaenterpriseV1FirewallActionIn"])
                ).optional(),
                "name": t.string().optional(),
                "path": t.string().optional(),
                "condition": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecaptchaenterpriseV1FirewallPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsFirewallpoliciesDelete"] = recaptchaenterprise.post(
        "v1/{parent}/firewallpolicies",
        t.struct(
            {
                "parent": t.string(),
                "description": t.string().optional(),
                "actions": t.array(
                    t.proxy(renames["GoogleCloudRecaptchaenterpriseV1FirewallActionIn"])
                ).optional(),
                "name": t.string().optional(),
                "path": t.string().optional(),
                "condition": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecaptchaenterpriseV1FirewallPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsFirewallpoliciesGet"] = recaptchaenterprise.post(
        "v1/{parent}/firewallpolicies",
        t.struct(
            {
                "parent": t.string(),
                "description": t.string().optional(),
                "actions": t.array(
                    t.proxy(renames["GoogleCloudRecaptchaenterpriseV1FirewallActionIn"])
                ).optional(),
                "name": t.string().optional(),
                "path": t.string().optional(),
                "condition": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecaptchaenterpriseV1FirewallPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsFirewallpoliciesPatch"] = recaptchaenterprise.post(
        "v1/{parent}/firewallpolicies",
        t.struct(
            {
                "parent": t.string(),
                "description": t.string().optional(),
                "actions": t.array(
                    t.proxy(renames["GoogleCloudRecaptchaenterpriseV1FirewallActionIn"])
                ).optional(),
                "name": t.string().optional(),
                "path": t.string().optional(),
                "condition": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecaptchaenterpriseV1FirewallPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsFirewallpoliciesCreate"] = recaptchaenterprise.post(
        "v1/{parent}/firewallpolicies",
        t.struct(
            {
                "parent": t.string(),
                "description": t.string().optional(),
                "actions": t.array(
                    t.proxy(renames["GoogleCloudRecaptchaenterpriseV1FirewallActionIn"])
                ).optional(),
                "name": t.string().optional(),
                "path": t.string().optional(),
                "condition": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecaptchaenterpriseV1FirewallPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAssessmentsCreate"] = recaptchaenterprise.post(
        "v1/{name}:annotate",
        t.struct(
            {
                "name": t.string(),
                "annotation": t.string().optional(),
                "hashedAccountId": t.string().optional(),
                "transactionEvent": t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1TransactionEventIn"]
                ).optional(),
                "reasons": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAssessmentsAnnotate"] = recaptchaenterprise.post(
        "v1/{name}:annotate",
        t.struct(
            {
                "name": t.string(),
                "annotation": t.string().optional(),
                "hashedAccountId": t.string().optional(),
                "transactionEvent": t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1TransactionEventIn"]
                ).optional(),
                "reasons": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="recaptchaenterprise",
        renames=renames,
        types=types,
        functions=functions,
    )
