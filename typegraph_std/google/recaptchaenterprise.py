from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_recaptchaenterprise():
    recaptchaenterprise = HTTPRuntime("https://recaptchaenterprise.googleapis.com/")

    renames = {
        "ErrorResponse": "_recaptchaenterprise_1_ErrorResponse",
        "GoogleCloudRecaptchaenterpriseV1FirewallActionRedirectActionIn": "_recaptchaenterprise_2_GoogleCloudRecaptchaenterpriseV1FirewallActionRedirectActionIn",
        "GoogleCloudRecaptchaenterpriseV1FirewallActionRedirectActionOut": "_recaptchaenterprise_3_GoogleCloudRecaptchaenterpriseV1FirewallActionRedirectActionOut",
        "GoogleCloudRecaptchaenterpriseV1TestingOptionsIn": "_recaptchaenterprise_4_GoogleCloudRecaptchaenterpriseV1TestingOptionsIn",
        "GoogleCloudRecaptchaenterpriseV1TestingOptionsOut": "_recaptchaenterprise_5_GoogleCloudRecaptchaenterpriseV1TestingOptionsOut",
        "GoogleCloudRecaptchaenterpriseV1MigrateKeyRequestIn": "_recaptchaenterprise_6_GoogleCloudRecaptchaenterpriseV1MigrateKeyRequestIn",
        "GoogleCloudRecaptchaenterpriseV1MigrateKeyRequestOut": "_recaptchaenterprise_7_GoogleCloudRecaptchaenterpriseV1MigrateKeyRequestOut",
        "GoogleCloudRecaptchaenterpriseV1RiskAnalysisIn": "_recaptchaenterprise_8_GoogleCloudRecaptchaenterpriseV1RiskAnalysisIn",
        "GoogleCloudRecaptchaenterpriseV1RiskAnalysisOut": "_recaptchaenterprise_9_GoogleCloudRecaptchaenterpriseV1RiskAnalysisOut",
        "GoogleCloudRecaptchaenterpriseV1WafSettingsIn": "_recaptchaenterprise_10_GoogleCloudRecaptchaenterpriseV1WafSettingsIn",
        "GoogleCloudRecaptchaenterpriseV1WafSettingsOut": "_recaptchaenterprise_11_GoogleCloudRecaptchaenterpriseV1WafSettingsOut",
        "GoogleCloudRecaptchaenterpriseV1AccountVerificationInfoIn": "_recaptchaenterprise_12_GoogleCloudRecaptchaenterpriseV1AccountVerificationInfoIn",
        "GoogleCloudRecaptchaenterpriseV1AccountVerificationInfoOut": "_recaptchaenterprise_13_GoogleCloudRecaptchaenterpriseV1AccountVerificationInfoOut",
        "GoogleCloudRecaptchaenterpriseV1FirewallActionAllowActionIn": "_recaptchaenterprise_14_GoogleCloudRecaptchaenterpriseV1FirewallActionAllowActionIn",
        "GoogleCloudRecaptchaenterpriseV1FirewallActionAllowActionOut": "_recaptchaenterprise_15_GoogleCloudRecaptchaenterpriseV1FirewallActionAllowActionOut",
        "GoogleCloudRecaptchaenterpriseV1AndroidKeySettingsIn": "_recaptchaenterprise_16_GoogleCloudRecaptchaenterpriseV1AndroidKeySettingsIn",
        "GoogleCloudRecaptchaenterpriseV1AndroidKeySettingsOut": "_recaptchaenterprise_17_GoogleCloudRecaptchaenterpriseV1AndroidKeySettingsOut",
        "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentIn": "_recaptchaenterprise_18_GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentIn",
        "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentOut": "_recaptchaenterprise_19_GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentOut",
        "GoogleCloudRecaptchaenterpriseV1RetrieveLegacySecretKeyResponseIn": "_recaptchaenterprise_20_GoogleCloudRecaptchaenterpriseV1RetrieveLegacySecretKeyResponseIn",
        "GoogleCloudRecaptchaenterpriseV1RetrieveLegacySecretKeyResponseOut": "_recaptchaenterprise_21_GoogleCloudRecaptchaenterpriseV1RetrieveLegacySecretKeyResponseOut",
        "GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupMembershipsResponseIn": "_recaptchaenterprise_22_GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupMembershipsResponseIn",
        "GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupMembershipsResponseOut": "_recaptchaenterprise_23_GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupMembershipsResponseOut",
        "GoogleCloudRecaptchaenterpriseV1ListFirewallPoliciesResponseIn": "_recaptchaenterprise_24_GoogleCloudRecaptchaenterpriseV1ListFirewallPoliciesResponseIn",
        "GoogleCloudRecaptchaenterpriseV1ListFirewallPoliciesResponseOut": "_recaptchaenterprise_25_GoogleCloudRecaptchaenterpriseV1ListFirewallPoliciesResponseOut",
        "GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentRequestIn": "_recaptchaenterprise_26_GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentRequestIn",
        "GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentRequestOut": "_recaptchaenterprise_27_GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentRequestOut",
        "GoogleCloudRecaptchaenterpriseV1IOSKeySettingsIn": "_recaptchaenterprise_28_GoogleCloudRecaptchaenterpriseV1IOSKeySettingsIn",
        "GoogleCloudRecaptchaenterpriseV1IOSKeySettingsOut": "_recaptchaenterprise_29_GoogleCloudRecaptchaenterpriseV1IOSKeySettingsOut",
        "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentBehavioralTrustVerdictIn": "_recaptchaenterprise_30_GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentBehavioralTrustVerdictIn",
        "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentBehavioralTrustVerdictOut": "_recaptchaenterprise_31_GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentBehavioralTrustVerdictOut",
        "GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentResponseIn": "_recaptchaenterprise_32_GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentResponseIn",
        "GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentResponseOut": "_recaptchaenterprise_33_GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentResponseOut",
        "GoogleCloudRecaptchaenterpriseV1FirewallActionIn": "_recaptchaenterprise_34_GoogleCloudRecaptchaenterpriseV1FirewallActionIn",
        "GoogleCloudRecaptchaenterpriseV1FirewallActionOut": "_recaptchaenterprise_35_GoogleCloudRecaptchaenterpriseV1FirewallActionOut",
        "GoogleCloudRecaptchaenterpriseV1MetricsIn": "_recaptchaenterprise_36_GoogleCloudRecaptchaenterpriseV1MetricsIn",
        "GoogleCloudRecaptchaenterpriseV1MetricsOut": "_recaptchaenterprise_37_GoogleCloudRecaptchaenterpriseV1MetricsOut",
        "GoogleCloudRecaptchaenterpriseV1TransactionDataAddressIn": "_recaptchaenterprise_38_GoogleCloudRecaptchaenterpriseV1TransactionDataAddressIn",
        "GoogleCloudRecaptchaenterpriseV1TransactionDataAddressOut": "_recaptchaenterprise_39_GoogleCloudRecaptchaenterpriseV1TransactionDataAddressOut",
        "GoogleRpcStatusIn": "_recaptchaenterprise_40_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_recaptchaenterprise_41_GoogleRpcStatusOut",
        "GoogleCloudRecaptchaenterpriseV1ChallengeMetricsIn": "_recaptchaenterprise_42_GoogleCloudRecaptchaenterpriseV1ChallengeMetricsIn",
        "GoogleCloudRecaptchaenterpriseV1ChallengeMetricsOut": "_recaptchaenterprise_43_GoogleCloudRecaptchaenterpriseV1ChallengeMetricsOut",
        "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentStolenInstrumentVerdictIn": "_recaptchaenterprise_44_GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentStolenInstrumentVerdictIn",
        "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentStolenInstrumentVerdictOut": "_recaptchaenterprise_45_GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentStolenInstrumentVerdictOut",
        "GoogleCloudRecaptchaenterpriseV1TransactionDataUserIn": "_recaptchaenterprise_46_GoogleCloudRecaptchaenterpriseV1TransactionDataUserIn",
        "GoogleCloudRecaptchaenterpriseV1TransactionDataUserOut": "_recaptchaenterprise_47_GoogleCloudRecaptchaenterpriseV1TransactionDataUserOut",
        "GoogleCloudRecaptchaenterpriseV1KeyIn": "_recaptchaenterprise_48_GoogleCloudRecaptchaenterpriseV1KeyIn",
        "GoogleCloudRecaptchaenterpriseV1KeyOut": "_recaptchaenterprise_49_GoogleCloudRecaptchaenterpriseV1KeyOut",
        "GoogleCloudRecaptchaenterpriseV1TransactionDataItemIn": "_recaptchaenterprise_50_GoogleCloudRecaptchaenterpriseV1TransactionDataItemIn",
        "GoogleCloudRecaptchaenterpriseV1TransactionDataItemOut": "_recaptchaenterprise_51_GoogleCloudRecaptchaenterpriseV1TransactionDataItemOut",
        "GoogleCloudRecaptchaenterpriseV1ScoreMetricsIn": "_recaptchaenterprise_52_GoogleCloudRecaptchaenterpriseV1ScoreMetricsIn",
        "GoogleCloudRecaptchaenterpriseV1ScoreMetricsOut": "_recaptchaenterprise_53_GoogleCloudRecaptchaenterpriseV1ScoreMetricsOut",
        "GoogleCloudRecaptchaenterpriseV1AccountDefenderAssessmentIn": "_recaptchaenterprise_54_GoogleCloudRecaptchaenterpriseV1AccountDefenderAssessmentIn",
        "GoogleCloudRecaptchaenterpriseV1AccountDefenderAssessmentOut": "_recaptchaenterprise_55_GoogleCloudRecaptchaenterpriseV1AccountDefenderAssessmentOut",
        "GoogleCloudRecaptchaenterpriseV1EndpointVerificationInfoIn": "_recaptchaenterprise_56_GoogleCloudRecaptchaenterpriseV1EndpointVerificationInfoIn",
        "GoogleCloudRecaptchaenterpriseV1EndpointVerificationInfoOut": "_recaptchaenterprise_57_GoogleCloudRecaptchaenterpriseV1EndpointVerificationInfoOut",
        "GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsResponseIn": "_recaptchaenterprise_58_GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsResponseIn",
        "GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsResponseOut": "_recaptchaenterprise_59_GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsResponseOut",
        "GoogleCloudRecaptchaenterpriseV1AssessmentIn": "_recaptchaenterprise_60_GoogleCloudRecaptchaenterpriseV1AssessmentIn",
        "GoogleCloudRecaptchaenterpriseV1AssessmentOut": "_recaptchaenterprise_61_GoogleCloudRecaptchaenterpriseV1AssessmentOut",
        "GoogleProtobufEmptyIn": "_recaptchaenterprise_62_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_recaptchaenterprise_63_GoogleProtobufEmptyOut",
        "GoogleCloudRecaptchaenterpriseV1PrivatePasswordLeakVerificationIn": "_recaptchaenterprise_64_GoogleCloudRecaptchaenterpriseV1PrivatePasswordLeakVerificationIn",
        "GoogleCloudRecaptchaenterpriseV1PrivatePasswordLeakVerificationOut": "_recaptchaenterprise_65_GoogleCloudRecaptchaenterpriseV1PrivatePasswordLeakVerificationOut",
        "GoogleCloudRecaptchaenterpriseV1TokenPropertiesIn": "_recaptchaenterprise_66_GoogleCloudRecaptchaenterpriseV1TokenPropertiesIn",
        "GoogleCloudRecaptchaenterpriseV1TokenPropertiesOut": "_recaptchaenterprise_67_GoogleCloudRecaptchaenterpriseV1TokenPropertiesOut",
        "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentCardTestingVerdictIn": "_recaptchaenterprise_68_GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentCardTestingVerdictIn",
        "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentCardTestingVerdictOut": "_recaptchaenterprise_69_GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentCardTestingVerdictOut",
        "GoogleCloudRecaptchaenterpriseV1EventIn": "_recaptchaenterprise_70_GoogleCloudRecaptchaenterpriseV1EventIn",
        "GoogleCloudRecaptchaenterpriseV1EventOut": "_recaptchaenterprise_71_GoogleCloudRecaptchaenterpriseV1EventOut",
        "GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupsResponseIn": "_recaptchaenterprise_72_GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupsResponseIn",
        "GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupsResponseOut": "_recaptchaenterprise_73_GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupsResponseOut",
        "GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupIn": "_recaptchaenterprise_74_GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupIn",
        "GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupOut": "_recaptchaenterprise_75_GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupOut",
        "GoogleCloudRecaptchaenterpriseV1FirewallActionSetHeaderActionIn": "_recaptchaenterprise_76_GoogleCloudRecaptchaenterpriseV1FirewallActionSetHeaderActionIn",
        "GoogleCloudRecaptchaenterpriseV1FirewallActionSetHeaderActionOut": "_recaptchaenterprise_77_GoogleCloudRecaptchaenterpriseV1FirewallActionSetHeaderActionOut",
        "GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsRequestIn": "_recaptchaenterprise_78_GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsRequestIn",
        "GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsRequestOut": "_recaptchaenterprise_79_GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsRequestOut",
        "GoogleCloudRecaptchaenterpriseV1TransactionDataGatewayInfoIn": "_recaptchaenterprise_80_GoogleCloudRecaptchaenterpriseV1TransactionDataGatewayInfoIn",
        "GoogleCloudRecaptchaenterpriseV1TransactionDataGatewayInfoOut": "_recaptchaenterprise_81_GoogleCloudRecaptchaenterpriseV1TransactionDataGatewayInfoOut",
        "GoogleCloudRecaptchaenterpriseV1FirewallPolicyIn": "_recaptchaenterprise_82_GoogleCloudRecaptchaenterpriseV1FirewallPolicyIn",
        "GoogleCloudRecaptchaenterpriseV1FirewallPolicyOut": "_recaptchaenterprise_83_GoogleCloudRecaptchaenterpriseV1FirewallPolicyOut",
        "GoogleCloudRecaptchaenterpriseV1ScoreDistributionIn": "_recaptchaenterprise_84_GoogleCloudRecaptchaenterpriseV1ScoreDistributionIn",
        "GoogleCloudRecaptchaenterpriseV1ScoreDistributionOut": "_recaptchaenterprise_85_GoogleCloudRecaptchaenterpriseV1ScoreDistributionOut",
        "GoogleCloudRecaptchaenterpriseV1TransactionDataIn": "_recaptchaenterprise_86_GoogleCloudRecaptchaenterpriseV1TransactionDataIn",
        "GoogleCloudRecaptchaenterpriseV1TransactionDataOut": "_recaptchaenterprise_87_GoogleCloudRecaptchaenterpriseV1TransactionDataOut",
        "GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupMembershipIn": "_recaptchaenterprise_88_GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupMembershipIn",
        "GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupMembershipOut": "_recaptchaenterprise_89_GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupMembershipOut",
        "GoogleCloudRecaptchaenterpriseV1FirewallActionSubstituteActionIn": "_recaptchaenterprise_90_GoogleCloudRecaptchaenterpriseV1FirewallActionSubstituteActionIn",
        "GoogleCloudRecaptchaenterpriseV1FirewallActionSubstituteActionOut": "_recaptchaenterprise_91_GoogleCloudRecaptchaenterpriseV1FirewallActionSubstituteActionOut",
        "GoogleCloudRecaptchaenterpriseV1FirewallPolicyAssessmentIn": "_recaptchaenterprise_92_GoogleCloudRecaptchaenterpriseV1FirewallPolicyAssessmentIn",
        "GoogleCloudRecaptchaenterpriseV1FirewallPolicyAssessmentOut": "_recaptchaenterprise_93_GoogleCloudRecaptchaenterpriseV1FirewallPolicyAssessmentOut",
        "GoogleCloudRecaptchaenterpriseV1TransactionEventIn": "_recaptchaenterprise_94_GoogleCloudRecaptchaenterpriseV1TransactionEventIn",
        "GoogleCloudRecaptchaenterpriseV1TransactionEventOut": "_recaptchaenterprise_95_GoogleCloudRecaptchaenterpriseV1TransactionEventOut",
        "GoogleCloudRecaptchaenterpriseV1AppleDeveloperIdIn": "_recaptchaenterprise_96_GoogleCloudRecaptchaenterpriseV1AppleDeveloperIdIn",
        "GoogleCloudRecaptchaenterpriseV1AppleDeveloperIdOut": "_recaptchaenterprise_97_GoogleCloudRecaptchaenterpriseV1AppleDeveloperIdOut",
        "GoogleCloudRecaptchaenterpriseV1WebKeySettingsIn": "_recaptchaenterprise_98_GoogleCloudRecaptchaenterpriseV1WebKeySettingsIn",
        "GoogleCloudRecaptchaenterpriseV1WebKeySettingsOut": "_recaptchaenterprise_99_GoogleCloudRecaptchaenterpriseV1WebKeySettingsOut",
        "GoogleCloudRecaptchaenterpriseV1ListKeysResponseIn": "_recaptchaenterprise_100_GoogleCloudRecaptchaenterpriseV1ListKeysResponseIn",
        "GoogleCloudRecaptchaenterpriseV1ListKeysResponseOut": "_recaptchaenterprise_101_GoogleCloudRecaptchaenterpriseV1ListKeysResponseOut",
        "GoogleCloudRecaptchaenterpriseV1FirewallActionBlockActionIn": "_recaptchaenterprise_102_GoogleCloudRecaptchaenterpriseV1FirewallActionBlockActionIn",
        "GoogleCloudRecaptchaenterpriseV1FirewallActionBlockActionOut": "_recaptchaenterprise_103_GoogleCloudRecaptchaenterpriseV1FirewallActionBlockActionOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudRecaptchaenterpriseV1FirewallActionRedirectActionIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1FirewallActionRedirectActionIn"])
    types["GoogleCloudRecaptchaenterpriseV1FirewallActionRedirectActionOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1FirewallActionRedirectActionOut"])
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
    types["GoogleCloudRecaptchaenterpriseV1MigrateKeyRequestIn"] = t.struct(
        {"skipBillingCheck": t.boolean().optional()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1MigrateKeyRequestIn"])
    types["GoogleCloudRecaptchaenterpriseV1MigrateKeyRequestOut"] = t.struct(
        {
            "skipBillingCheck": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1MigrateKeyRequestOut"])
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
    types["GoogleCloudRecaptchaenterpriseV1WafSettingsIn"] = t.struct(
        {"wafService": t.string(), "wafFeature": t.string()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1WafSettingsIn"])
    types["GoogleCloudRecaptchaenterpriseV1WafSettingsOut"] = t.struct(
        {
            "wafService": t.string(),
            "wafFeature": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1WafSettingsOut"])
    types["GoogleCloudRecaptchaenterpriseV1AccountVerificationInfoIn"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "username": t.string().optional(),
            "endpoints": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudRecaptchaenterpriseV1EndpointVerificationInfoIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1AccountVerificationInfoIn"])
    types["GoogleCloudRecaptchaenterpriseV1AccountVerificationInfoOut"] = t.struct(
        {
            "latestVerificationResult": t.string().optional(),
            "languageCode": t.string().optional(),
            "username": t.string().optional(),
            "endpoints": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudRecaptchaenterpriseV1EndpointVerificationInfoOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1AccountVerificationInfoOut"])
    types["GoogleCloudRecaptchaenterpriseV1FirewallActionAllowActionIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1FirewallActionAllowActionIn"])
    types["GoogleCloudRecaptchaenterpriseV1FirewallActionAllowActionOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1FirewallActionAllowActionOut"])
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
    types["GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentIn"] = t.struct(
        {
            "cardTestingVerdict": t.proxy(
                renames[
                    "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentCardTestingVerdictIn"
                ]
            ).optional(),
            "transactionRisk": t.number().optional(),
            "behavioralTrustVerdict": t.proxy(
                renames[
                    "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentBehavioralTrustVerdictIn"
                ]
            ).optional(),
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
            "transactionRisk": t.number().optional(),
            "behavioralTrustVerdict": t.proxy(
                renames[
                    "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentBehavioralTrustVerdictOut"
                ]
            ).optional(),
            "stolenInstrumentVerdict": t.proxy(
                renames[
                    "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentStolenInstrumentVerdictOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentOut"])
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
    types["GoogleCloudRecaptchaenterpriseV1ListFirewallPoliciesResponseIn"] = t.struct(
        {
            "firewallPolicies": t.array(
                t.proxy(renames["GoogleCloudRecaptchaenterpriseV1FirewallPolicyIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1ListFirewallPoliciesResponseIn"])
    types["GoogleCloudRecaptchaenterpriseV1ListFirewallPoliciesResponseOut"] = t.struct(
        {
            "firewallPolicies": t.array(
                t.proxy(renames["GoogleCloudRecaptchaenterpriseV1FirewallPolicyOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1ListFirewallPoliciesResponseOut"])
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
    types["GoogleCloudRecaptchaenterpriseV1IOSKeySettingsIn"] = t.struct(
        {
            "allowAllBundleIds": t.boolean().optional(),
            "allowedBundleIds": t.array(t.string()).optional(),
            "appleDeveloperId": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1AppleDeveloperIdIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1IOSKeySettingsIn"])
    types["GoogleCloudRecaptchaenterpriseV1IOSKeySettingsOut"] = t.struct(
        {
            "allowAllBundleIds": t.boolean().optional(),
            "allowedBundleIds": t.array(t.string()).optional(),
            "appleDeveloperId": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1AppleDeveloperIdOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1IOSKeySettingsOut"])
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
    types["GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentResponseIn"])
    types["GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentResponseOut"])
    types["GoogleCloudRecaptchaenterpriseV1FirewallActionIn"] = t.struct(
        {
            "allow": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1FirewallActionAllowActionIn"]
            ).optional(),
            "substitute": t.proxy(
                renames[
                    "GoogleCloudRecaptchaenterpriseV1FirewallActionSubstituteActionIn"
                ]
            ).optional(),
            "redirect": t.proxy(
                renames[
                    "GoogleCloudRecaptchaenterpriseV1FirewallActionRedirectActionIn"
                ]
            ).optional(),
            "setHeader": t.proxy(
                renames[
                    "GoogleCloudRecaptchaenterpriseV1FirewallActionSetHeaderActionIn"
                ]
            ).optional(),
            "block": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1FirewallActionBlockActionIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1FirewallActionIn"])
    types["GoogleCloudRecaptchaenterpriseV1FirewallActionOut"] = t.struct(
        {
            "allow": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1FirewallActionAllowActionOut"]
            ).optional(),
            "substitute": t.proxy(
                renames[
                    "GoogleCloudRecaptchaenterpriseV1FirewallActionSubstituteActionOut"
                ]
            ).optional(),
            "redirect": t.proxy(
                renames[
                    "GoogleCloudRecaptchaenterpriseV1FirewallActionRedirectActionOut"
                ]
            ).optional(),
            "setHeader": t.proxy(
                renames[
                    "GoogleCloudRecaptchaenterpriseV1FirewallActionSetHeaderActionOut"
                ]
            ).optional(),
            "block": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1FirewallActionBlockActionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1FirewallActionOut"])
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
            "challengeMetrics": t.array(
                t.proxy(renames["GoogleCloudRecaptchaenterpriseV1ChallengeMetricsOut"])
            ).optional(),
            "scoreMetrics": t.array(
                t.proxy(renames["GoogleCloudRecaptchaenterpriseV1ScoreMetricsOut"])
            ).optional(),
            "name": t.string().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1MetricsOut"])
    types["GoogleCloudRecaptchaenterpriseV1TransactionDataAddressIn"] = t.struct(
        {
            "regionCode": t.string().optional(),
            "recipient": t.string().optional(),
            "administrativeArea": t.string().optional(),
            "locality": t.string().optional(),
            "postalCode": t.string().optional(),
            "address": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TransactionDataAddressIn"])
    types["GoogleCloudRecaptchaenterpriseV1TransactionDataAddressOut"] = t.struct(
        {
            "regionCode": t.string().optional(),
            "recipient": t.string().optional(),
            "administrativeArea": t.string().optional(),
            "locality": t.string().optional(),
            "postalCode": t.string().optional(),
            "address": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TransactionDataAddressOut"])
    types["GoogleRpcStatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["GoogleRpcStatusIn"])
    types["GoogleRpcStatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleRpcStatusOut"])
    types["GoogleCloudRecaptchaenterpriseV1ChallengeMetricsIn"] = t.struct(
        {
            "nocaptchaCount": t.string().optional(),
            "pageloadCount": t.string().optional(),
            "failedCount": t.string().optional(),
            "passedCount": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1ChallengeMetricsIn"])
    types["GoogleCloudRecaptchaenterpriseV1ChallengeMetricsOut"] = t.struct(
        {
            "nocaptchaCount": t.string().optional(),
            "pageloadCount": t.string().optional(),
            "failedCount": t.string().optional(),
            "passedCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1ChallengeMetricsOut"])
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
    types["GoogleCloudRecaptchaenterpriseV1TransactionDataUserIn"] = t.struct(
        {
            "phoneVerified": t.boolean().optional(),
            "emailVerified": t.boolean().optional(),
            "creationMs": t.string().optional(),
            "email": t.string().optional(),
            "phoneNumber": t.string().optional(),
            "accountId": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TransactionDataUserIn"])
    types["GoogleCloudRecaptchaenterpriseV1TransactionDataUserOut"] = t.struct(
        {
            "phoneVerified": t.boolean().optional(),
            "emailVerified": t.boolean().optional(),
            "creationMs": t.string().optional(),
            "email": t.string().optional(),
            "phoneNumber": t.string().optional(),
            "accountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TransactionDataUserOut"])
    types["GoogleCloudRecaptchaenterpriseV1KeyIn"] = t.struct(
        {
            "androidSettings": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1AndroidKeySettingsIn"]
            ).optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "webSettings": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1WebKeySettingsIn"]
            ).optional(),
            "wafSettings": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1WafSettingsIn"]
            ).optional(),
            "testingOptions": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TestingOptionsIn"]
            ).optional(),
            "iosSettings": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1IOSKeySettingsIn"]
            ).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1KeyIn"])
    types["GoogleCloudRecaptchaenterpriseV1KeyOut"] = t.struct(
        {
            "androidSettings": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1AndroidKeySettingsOut"]
            ).optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "webSettings": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1WebKeySettingsOut"]
            ).optional(),
            "wafSettings": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1WafSettingsOut"]
            ).optional(),
            "testingOptions": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TestingOptionsOut"]
            ).optional(),
            "iosSettings": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1IOSKeySettingsOut"]
            ).optional(),
            "displayName": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1KeyOut"])
    types["GoogleCloudRecaptchaenterpriseV1TransactionDataItemIn"] = t.struct(
        {
            "quantity": t.string().optional(),
            "value": t.number().optional(),
            "merchantAccountId": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TransactionDataItemIn"])
    types["GoogleCloudRecaptchaenterpriseV1TransactionDataItemOut"] = t.struct(
        {
            "quantity": t.string().optional(),
            "value": t.number().optional(),
            "merchantAccountId": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TransactionDataItemOut"])
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
    types["GoogleCloudRecaptchaenterpriseV1AccountDefenderAssessmentIn"] = t.struct(
        {"labels": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1AccountDefenderAssessmentIn"])
    types["GoogleCloudRecaptchaenterpriseV1AccountDefenderAssessmentOut"] = t.struct(
        {
            "labels": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1AccountDefenderAssessmentOut"])
    types["GoogleCloudRecaptchaenterpriseV1EndpointVerificationInfoIn"] = t.struct(
        {"emailAddress": t.string().optional(), "phoneNumber": t.string().optional()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1EndpointVerificationInfoIn"])
    types["GoogleCloudRecaptchaenterpriseV1EndpointVerificationInfoOut"] = t.struct(
        {
            "emailAddress": t.string().optional(),
            "requestToken": t.string().optional(),
            "lastVerificationTime": t.string().optional(),
            "phoneNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1EndpointVerificationInfoOut"])
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
    types["GoogleCloudRecaptchaenterpriseV1AssessmentIn"] = t.struct(
        {
            "event": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1EventIn"]
            ).optional(),
            "fraudPreventionAssessment": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentIn"]
            ).optional(),
            "firewallPolicyAssessment": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1FirewallPolicyAssessmentIn"]
            ).optional(),
            "accountVerification": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1AccountVerificationInfoIn"]
            ).optional(),
            "accountDefenderAssessment": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1AccountDefenderAssessmentIn"]
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
            "event": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1EventOut"]
            ).optional(),
            "name": t.string().optional(),
            "riskAnalysis": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1RiskAnalysisOut"]
            ).optional(),
            "fraudPreventionAssessment": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentOut"]
            ).optional(),
            "firewallPolicyAssessment": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1FirewallPolicyAssessmentOut"]
            ).optional(),
            "accountVerification": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1AccountVerificationInfoOut"]
            ).optional(),
            "accountDefenderAssessment": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1AccountDefenderAssessmentOut"]
            ).optional(),
            "privatePasswordLeakVerification": t.proxy(
                renames[
                    "GoogleCloudRecaptchaenterpriseV1PrivatePasswordLeakVerificationOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1AssessmentOut"])
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
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
            "lookupHashPrefix": t.string().optional(),
            "reencryptedUserCredentialsHash": t.string().optional(),
            "encryptedUserCredentialsHash": t.string().optional(),
            "encryptedLeakMatchPrefixes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudRecaptchaenterpriseV1PrivatePasswordLeakVerificationOut"]
    )
    types["GoogleCloudRecaptchaenterpriseV1TokenPropertiesIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "iosBundleId": t.string().optional(),
            "hostname": t.string().optional(),
            "androidPackageName": t.string().optional(),
            "action": t.string().optional(),
            "invalidReason": t.string().optional(),
            "valid": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TokenPropertiesIn"])
    types["GoogleCloudRecaptchaenterpriseV1TokenPropertiesOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "iosBundleId": t.string().optional(),
            "hostname": t.string().optional(),
            "androidPackageName": t.string().optional(),
            "action": t.string().optional(),
            "invalidReason": t.string().optional(),
            "valid": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TokenPropertiesOut"])
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
    types["GoogleCloudRecaptchaenterpriseV1EventIn"] = t.struct(
        {
            "ja3": t.string().optional(),
            "userAgent": t.string().optional(),
            "headers": t.array(t.string()).optional(),
            "requestedUri": t.string().optional(),
            "express": t.boolean().optional(),
            "siteKey": t.string().optional(),
            "transactionData": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TransactionDataIn"]
            ).optional(),
            "expectedAction": t.string().optional(),
            "firewallPolicyEvaluation": t.boolean().optional(),
            "hashedAccountId": t.string().optional(),
            "token": t.string().optional(),
            "userIpAddress": t.string().optional(),
            "wafTokenAssessment": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1EventIn"])
    types["GoogleCloudRecaptchaenterpriseV1EventOut"] = t.struct(
        {
            "ja3": t.string().optional(),
            "userAgent": t.string().optional(),
            "headers": t.array(t.string()).optional(),
            "requestedUri": t.string().optional(),
            "express": t.boolean().optional(),
            "siteKey": t.string().optional(),
            "transactionData": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TransactionDataOut"]
            ).optional(),
            "expectedAction": t.string().optional(),
            "firewallPolicyEvaluation": t.boolean().optional(),
            "hashedAccountId": t.string().optional(),
            "token": t.string().optional(),
            "userIpAddress": t.string().optional(),
            "wafTokenAssessment": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1EventOut"])
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
    types["GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupIn"] = t.struct(
        {"name": t.string()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupIn"])
    types["GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupOut"] = t.struct(
        {"name": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupOut"])
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
        "GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsRequestIn"
    ] = t.struct(
        {
            "hashedAccountId": t.string().optional(),
            "pageToken": t.string().optional(),
            "pageSize": t.integer().optional(),
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
            "pageToken": t.string().optional(),
            "pageSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsRequestOut"
        ]
    )
    types["GoogleCloudRecaptchaenterpriseV1TransactionDataGatewayInfoIn"] = t.struct(
        {
            "name": t.string().optional(),
            "avsResponseCode": t.string().optional(),
            "cvvResponseCode": t.string().optional(),
            "gatewayResponseCode": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TransactionDataGatewayInfoIn"])
    types["GoogleCloudRecaptchaenterpriseV1TransactionDataGatewayInfoOut"] = t.struct(
        {
            "name": t.string().optional(),
            "avsResponseCode": t.string().optional(),
            "cvvResponseCode": t.string().optional(),
            "gatewayResponseCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TransactionDataGatewayInfoOut"])
    types["GoogleCloudRecaptchaenterpriseV1FirewallPolicyIn"] = t.struct(
        {
            "path": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "actions": t.array(
                t.proxy(renames["GoogleCloudRecaptchaenterpriseV1FirewallActionIn"])
            ).optional(),
            "condition": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1FirewallPolicyIn"])
    types["GoogleCloudRecaptchaenterpriseV1FirewallPolicyOut"] = t.struct(
        {
            "path": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "actions": t.array(
                t.proxy(renames["GoogleCloudRecaptchaenterpriseV1FirewallActionOut"])
            ).optional(),
            "condition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1FirewallPolicyOut"])
    types["GoogleCloudRecaptchaenterpriseV1ScoreDistributionIn"] = t.struct(
        {"scoreBuckets": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1ScoreDistributionIn"])
    types["GoogleCloudRecaptchaenterpriseV1ScoreDistributionOut"] = t.struct(
        {
            "scoreBuckets": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1ScoreDistributionOut"])
    types["GoogleCloudRecaptchaenterpriseV1TransactionDataIn"] = t.struct(
        {
            "currencyCode": t.string().optional(),
            "shippingValue": t.number().optional(),
            "transactionId": t.string().optional(),
            "gatewayInfo": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TransactionDataGatewayInfoIn"]
            ).optional(),
            "paymentMethod": t.string().optional(),
            "user": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TransactionDataUserIn"]
            ).optional(),
            "value": t.number().optional(),
            "cardLastFour": t.string().optional(),
            "merchants": t.array(
                t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1TransactionDataUserIn"]
                )
            ).optional(),
            "cardBin": t.string().optional(),
            "shippingAddress": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TransactionDataAddressIn"]
            ).optional(),
            "billingAddress": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TransactionDataAddressIn"]
            ).optional(),
            "items": t.array(
                t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1TransactionDataItemIn"]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TransactionDataIn"])
    types["GoogleCloudRecaptchaenterpriseV1TransactionDataOut"] = t.struct(
        {
            "currencyCode": t.string().optional(),
            "shippingValue": t.number().optional(),
            "transactionId": t.string().optional(),
            "gatewayInfo": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TransactionDataGatewayInfoOut"]
            ).optional(),
            "paymentMethod": t.string().optional(),
            "user": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TransactionDataUserOut"]
            ).optional(),
            "value": t.number().optional(),
            "cardLastFour": t.string().optional(),
            "merchants": t.array(
                t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1TransactionDataUserOut"]
                )
            ).optional(),
            "cardBin": t.string().optional(),
            "shippingAddress": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TransactionDataAddressOut"]
            ).optional(),
            "billingAddress": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TransactionDataAddressOut"]
            ).optional(),
            "items": t.array(
                t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1TransactionDataItemOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TransactionDataOut"])
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
    types["GoogleCloudRecaptchaenterpriseV1FirewallPolicyAssessmentIn"] = t.struct(
        {"error": t.proxy(renames["GoogleRpcStatusIn"]).optional()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1FirewallPolicyAssessmentIn"])
    types["GoogleCloudRecaptchaenterpriseV1FirewallPolicyAssessmentOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "firewallPolicy": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1FirewallPolicyOut"]
            ).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1FirewallPolicyAssessmentOut"])
    types["GoogleCloudRecaptchaenterpriseV1TransactionEventIn"] = t.struct(
        {
            "eventType": t.string().optional(),
            "value": t.number().optional(),
            "eventTime": t.string().optional(),
            "reason": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TransactionEventIn"])
    types["GoogleCloudRecaptchaenterpriseV1TransactionEventOut"] = t.struct(
        {
            "eventType": t.string().optional(),
            "value": t.number().optional(),
            "eventTime": t.string().optional(),
            "reason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TransactionEventOut"])
    types["GoogleCloudRecaptchaenterpriseV1AppleDeveloperIdIn"] = t.struct(
        {"keyId": t.string(), "privateKey": t.string(), "teamId": t.string()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1AppleDeveloperIdIn"])
    types["GoogleCloudRecaptchaenterpriseV1AppleDeveloperIdOut"] = t.struct(
        {
            "keyId": t.string(),
            "privateKey": t.string(),
            "teamId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1AppleDeveloperIdOut"])
    types["GoogleCloudRecaptchaenterpriseV1WebKeySettingsIn"] = t.struct(
        {
            "integrationType": t.string(),
            "allowedDomains": t.array(t.string()).optional(),
            "challengeSecurityPreference": t.string().optional(),
            "allowAmpTraffic": t.boolean().optional(),
            "allowAllDomains": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1WebKeySettingsIn"])
    types["GoogleCloudRecaptchaenterpriseV1WebKeySettingsOut"] = t.struct(
        {
            "integrationType": t.string(),
            "allowedDomains": t.array(t.string()).optional(),
            "challengeSecurityPreference": t.string().optional(),
            "allowAmpTraffic": t.boolean().optional(),
            "allowAllDomains": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1WebKeySettingsOut"])
    types["GoogleCloudRecaptchaenterpriseV1ListKeysResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "keys": t.array(
                t.proxy(renames["GoogleCloudRecaptchaenterpriseV1KeyIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1ListKeysResponseIn"])
    types["GoogleCloudRecaptchaenterpriseV1ListKeysResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "keys": t.array(
                t.proxy(renames["GoogleCloudRecaptchaenterpriseV1KeyOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1ListKeysResponseOut"])
    types["GoogleCloudRecaptchaenterpriseV1FirewallActionBlockActionIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1FirewallActionBlockActionIn"])
    types["GoogleCloudRecaptchaenterpriseV1FirewallActionBlockActionOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1FirewallActionBlockActionOut"])

    functions = {}
    functions["projectsAssessmentsAnnotate"] = recaptchaenterprise.post(
        "v1/{parent}/assessments",
        t.struct(
            {
                "parent": t.string(),
                "event": t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1EventIn"]
                ).optional(),
                "fraudPreventionAssessment": t.proxy(
                    renames[
                        "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentIn"
                    ]
                ).optional(),
                "firewallPolicyAssessment": t.proxy(
                    renames[
                        "GoogleCloudRecaptchaenterpriseV1FirewallPolicyAssessmentIn"
                    ]
                ).optional(),
                "accountVerification": t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1AccountVerificationInfoIn"]
                ).optional(),
                "accountDefenderAssessment": t.proxy(
                    renames[
                        "GoogleCloudRecaptchaenterpriseV1AccountDefenderAssessmentIn"
                    ]
                ).optional(),
                "privatePasswordLeakVerification": t.proxy(
                    renames[
                        "GoogleCloudRecaptchaenterpriseV1PrivatePasswordLeakVerificationIn"
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
                "event": t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1EventIn"]
                ).optional(),
                "fraudPreventionAssessment": t.proxy(
                    renames[
                        "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentIn"
                    ]
                ).optional(),
                "firewallPolicyAssessment": t.proxy(
                    renames[
                        "GoogleCloudRecaptchaenterpriseV1FirewallPolicyAssessmentIn"
                    ]
                ).optional(),
                "accountVerification": t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1AccountVerificationInfoIn"]
                ).optional(),
                "accountDefenderAssessment": t.proxy(
                    renames[
                        "GoogleCloudRecaptchaenterpriseV1AccountDefenderAssessmentIn"
                    ]
                ).optional(),
                "privatePasswordLeakVerification": t.proxy(
                    renames[
                        "GoogleCloudRecaptchaenterpriseV1PrivatePasswordLeakVerificationIn"
                    ]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecaptchaenterpriseV1AssessmentOut"]),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
    functions["projectsKeysCreate"] = recaptchaenterprise.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsKeysMigrate"] = recaptchaenterprise.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsKeysGetMetrics"] = recaptchaenterprise.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsKeysPatch"] = recaptchaenterprise.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsKeysList"] = recaptchaenterprise.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsKeysGet"] = recaptchaenterprise.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsKeysRetrieveLegacySecretKey"] = recaptchaenterprise.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsKeysDelete"] = recaptchaenterprise.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
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
    functions["projectsFirewallpoliciesCreate"] = recaptchaenterprise.get(
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
    functions["projectsRelatedaccountgroupsList"] = recaptchaenterprise.get(
        "v1/{parent}/relatedaccountgroups",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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

    return Import(
        importer="recaptchaenterprise",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
