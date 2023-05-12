from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_recaptchaenterprise() -> Import:
    recaptchaenterprise = HTTPRuntime("https://recaptchaenterprise.googleapis.com/")

    renames = {
        "ErrorResponse": "_recaptchaenterprise_1_ErrorResponse",
        "GoogleCloudRecaptchaenterpriseV1PrivatePasswordLeakVerificationIn": "_recaptchaenterprise_2_GoogleCloudRecaptchaenterpriseV1PrivatePasswordLeakVerificationIn",
        "GoogleCloudRecaptchaenterpriseV1PrivatePasswordLeakVerificationOut": "_recaptchaenterprise_3_GoogleCloudRecaptchaenterpriseV1PrivatePasswordLeakVerificationOut",
        "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentBehavioralTrustVerdictIn": "_recaptchaenterprise_4_GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentBehavioralTrustVerdictIn",
        "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentBehavioralTrustVerdictOut": "_recaptchaenterprise_5_GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentBehavioralTrustVerdictOut",
        "GoogleCloudRecaptchaenterpriseV1EndpointVerificationInfoIn": "_recaptchaenterprise_6_GoogleCloudRecaptchaenterpriseV1EndpointVerificationInfoIn",
        "GoogleCloudRecaptchaenterpriseV1EndpointVerificationInfoOut": "_recaptchaenterprise_7_GoogleCloudRecaptchaenterpriseV1EndpointVerificationInfoOut",
        "GoogleCloudRecaptchaenterpriseV1RiskAnalysisIn": "_recaptchaenterprise_8_GoogleCloudRecaptchaenterpriseV1RiskAnalysisIn",
        "GoogleCloudRecaptchaenterpriseV1RiskAnalysisOut": "_recaptchaenterprise_9_GoogleCloudRecaptchaenterpriseV1RiskAnalysisOut",
        "GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupMembershipsResponseIn": "_recaptchaenterprise_10_GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupMembershipsResponseIn",
        "GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupMembershipsResponseOut": "_recaptchaenterprise_11_GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupMembershipsResponseOut",
        "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentStolenInstrumentVerdictIn": "_recaptchaenterprise_12_GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentStolenInstrumentVerdictIn",
        "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentStolenInstrumentVerdictOut": "_recaptchaenterprise_13_GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentStolenInstrumentVerdictOut",
        "GoogleRpcStatusIn": "_recaptchaenterprise_14_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_recaptchaenterprise_15_GoogleRpcStatusOut",
        "GoogleCloudRecaptchaenterpriseV1AppleDeveloperIdIn": "_recaptchaenterprise_16_GoogleCloudRecaptchaenterpriseV1AppleDeveloperIdIn",
        "GoogleCloudRecaptchaenterpriseV1AppleDeveloperIdOut": "_recaptchaenterprise_17_GoogleCloudRecaptchaenterpriseV1AppleDeveloperIdOut",
        "GoogleCloudRecaptchaenterpriseV1FirewallActionRedirectActionIn": "_recaptchaenterprise_18_GoogleCloudRecaptchaenterpriseV1FirewallActionRedirectActionIn",
        "GoogleCloudRecaptchaenterpriseV1FirewallActionRedirectActionOut": "_recaptchaenterprise_19_GoogleCloudRecaptchaenterpriseV1FirewallActionRedirectActionOut",
        "GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentResponseIn": "_recaptchaenterprise_20_GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentResponseIn",
        "GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentResponseOut": "_recaptchaenterprise_21_GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentResponseOut",
        "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentCardTestingVerdictIn": "_recaptchaenterprise_22_GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentCardTestingVerdictIn",
        "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentCardTestingVerdictOut": "_recaptchaenterprise_23_GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentCardTestingVerdictOut",
        "GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsRequestIn": "_recaptchaenterprise_24_GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsRequestIn",
        "GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsRequestOut": "_recaptchaenterprise_25_GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsRequestOut",
        "GoogleCloudRecaptchaenterpriseV1EventIn": "_recaptchaenterprise_26_GoogleCloudRecaptchaenterpriseV1EventIn",
        "GoogleCloudRecaptchaenterpriseV1EventOut": "_recaptchaenterprise_27_GoogleCloudRecaptchaenterpriseV1EventOut",
        "GoogleCloudRecaptchaenterpriseV1FirewallActionBlockActionIn": "_recaptchaenterprise_28_GoogleCloudRecaptchaenterpriseV1FirewallActionBlockActionIn",
        "GoogleCloudRecaptchaenterpriseV1FirewallActionBlockActionOut": "_recaptchaenterprise_29_GoogleCloudRecaptchaenterpriseV1FirewallActionBlockActionOut",
        "GoogleCloudRecaptchaenterpriseV1TransactionDataUserIn": "_recaptchaenterprise_30_GoogleCloudRecaptchaenterpriseV1TransactionDataUserIn",
        "GoogleCloudRecaptchaenterpriseV1TransactionDataUserOut": "_recaptchaenterprise_31_GoogleCloudRecaptchaenterpriseV1TransactionDataUserOut",
        "GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupIn": "_recaptchaenterprise_32_GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupIn",
        "GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupOut": "_recaptchaenterprise_33_GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupOut",
        "GoogleCloudRecaptchaenterpriseV1TransactionDataItemIn": "_recaptchaenterprise_34_GoogleCloudRecaptchaenterpriseV1TransactionDataItemIn",
        "GoogleCloudRecaptchaenterpriseV1TransactionDataItemOut": "_recaptchaenterprise_35_GoogleCloudRecaptchaenterpriseV1TransactionDataItemOut",
        "GoogleCloudRecaptchaenterpriseV1AccountVerificationInfoIn": "_recaptchaenterprise_36_GoogleCloudRecaptchaenterpriseV1AccountVerificationInfoIn",
        "GoogleCloudRecaptchaenterpriseV1AccountVerificationInfoOut": "_recaptchaenterprise_37_GoogleCloudRecaptchaenterpriseV1AccountVerificationInfoOut",
        "GoogleCloudRecaptchaenterpriseV1MetricsIn": "_recaptchaenterprise_38_GoogleCloudRecaptchaenterpriseV1MetricsIn",
        "GoogleCloudRecaptchaenterpriseV1MetricsOut": "_recaptchaenterprise_39_GoogleCloudRecaptchaenterpriseV1MetricsOut",
        "GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupMembershipIn": "_recaptchaenterprise_40_GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupMembershipIn",
        "GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupMembershipOut": "_recaptchaenterprise_41_GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupMembershipOut",
        "GoogleCloudRecaptchaenterpriseV1ScoreDistributionIn": "_recaptchaenterprise_42_GoogleCloudRecaptchaenterpriseV1ScoreDistributionIn",
        "GoogleCloudRecaptchaenterpriseV1ScoreDistributionOut": "_recaptchaenterprise_43_GoogleCloudRecaptchaenterpriseV1ScoreDistributionOut",
        "GoogleCloudRecaptchaenterpriseV1RetrieveLegacySecretKeyResponseIn": "_recaptchaenterprise_44_GoogleCloudRecaptchaenterpriseV1RetrieveLegacySecretKeyResponseIn",
        "GoogleCloudRecaptchaenterpriseV1RetrieveLegacySecretKeyResponseOut": "_recaptchaenterprise_45_GoogleCloudRecaptchaenterpriseV1RetrieveLegacySecretKeyResponseOut",
        "GoogleCloudRecaptchaenterpriseV1WafSettingsIn": "_recaptchaenterprise_46_GoogleCloudRecaptchaenterpriseV1WafSettingsIn",
        "GoogleCloudRecaptchaenterpriseV1WafSettingsOut": "_recaptchaenterprise_47_GoogleCloudRecaptchaenterpriseV1WafSettingsOut",
        "GoogleCloudRecaptchaenterpriseV1FirewallPolicyAssessmentIn": "_recaptchaenterprise_48_GoogleCloudRecaptchaenterpriseV1FirewallPolicyAssessmentIn",
        "GoogleCloudRecaptchaenterpriseV1FirewallPolicyAssessmentOut": "_recaptchaenterprise_49_GoogleCloudRecaptchaenterpriseV1FirewallPolicyAssessmentOut",
        "GoogleCloudRecaptchaenterpriseV1WebKeySettingsIn": "_recaptchaenterprise_50_GoogleCloudRecaptchaenterpriseV1WebKeySettingsIn",
        "GoogleCloudRecaptchaenterpriseV1WebKeySettingsOut": "_recaptchaenterprise_51_GoogleCloudRecaptchaenterpriseV1WebKeySettingsOut",
        "GoogleCloudRecaptchaenterpriseV1KeyIn": "_recaptchaenterprise_52_GoogleCloudRecaptchaenterpriseV1KeyIn",
        "GoogleCloudRecaptchaenterpriseV1KeyOut": "_recaptchaenterprise_53_GoogleCloudRecaptchaenterpriseV1KeyOut",
        "GoogleCloudRecaptchaenterpriseV1FirewallActionSubstituteActionIn": "_recaptchaenterprise_54_GoogleCloudRecaptchaenterpriseV1FirewallActionSubstituteActionIn",
        "GoogleCloudRecaptchaenterpriseV1FirewallActionSubstituteActionOut": "_recaptchaenterprise_55_GoogleCloudRecaptchaenterpriseV1FirewallActionSubstituteActionOut",
        "GoogleCloudRecaptchaenterpriseV1TestingOptionsIn": "_recaptchaenterprise_56_GoogleCloudRecaptchaenterpriseV1TestingOptionsIn",
        "GoogleCloudRecaptchaenterpriseV1TestingOptionsOut": "_recaptchaenterprise_57_GoogleCloudRecaptchaenterpriseV1TestingOptionsOut",
        "GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupsResponseIn": "_recaptchaenterprise_58_GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupsResponseIn",
        "GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupsResponseOut": "_recaptchaenterprise_59_GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupsResponseOut",
        "GoogleCloudRecaptchaenterpriseV1MigrateKeyRequestIn": "_recaptchaenterprise_60_GoogleCloudRecaptchaenterpriseV1MigrateKeyRequestIn",
        "GoogleCloudRecaptchaenterpriseV1MigrateKeyRequestOut": "_recaptchaenterprise_61_GoogleCloudRecaptchaenterpriseV1MigrateKeyRequestOut",
        "GoogleCloudRecaptchaenterpriseV1ListFirewallPoliciesResponseIn": "_recaptchaenterprise_62_GoogleCloudRecaptchaenterpriseV1ListFirewallPoliciesResponseIn",
        "GoogleCloudRecaptchaenterpriseV1ListFirewallPoliciesResponseOut": "_recaptchaenterprise_63_GoogleCloudRecaptchaenterpriseV1ListFirewallPoliciesResponseOut",
        "GoogleCloudRecaptchaenterpriseV1TransactionDataAddressIn": "_recaptchaenterprise_64_GoogleCloudRecaptchaenterpriseV1TransactionDataAddressIn",
        "GoogleCloudRecaptchaenterpriseV1TransactionDataAddressOut": "_recaptchaenterprise_65_GoogleCloudRecaptchaenterpriseV1TransactionDataAddressOut",
        "GoogleCloudRecaptchaenterpriseV1TransactionEventIn": "_recaptchaenterprise_66_GoogleCloudRecaptchaenterpriseV1TransactionEventIn",
        "GoogleCloudRecaptchaenterpriseV1TransactionEventOut": "_recaptchaenterprise_67_GoogleCloudRecaptchaenterpriseV1TransactionEventOut",
        "GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentRequestIn": "_recaptchaenterprise_68_GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentRequestIn",
        "GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentRequestOut": "_recaptchaenterprise_69_GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentRequestOut",
        "GoogleCloudRecaptchaenterpriseV1TokenPropertiesIn": "_recaptchaenterprise_70_GoogleCloudRecaptchaenterpriseV1TokenPropertiesIn",
        "GoogleCloudRecaptchaenterpriseV1TokenPropertiesOut": "_recaptchaenterprise_71_GoogleCloudRecaptchaenterpriseV1TokenPropertiesOut",
        "GoogleCloudRecaptchaenterpriseV1AccountDefenderAssessmentIn": "_recaptchaenterprise_72_GoogleCloudRecaptchaenterpriseV1AccountDefenderAssessmentIn",
        "GoogleCloudRecaptchaenterpriseV1AccountDefenderAssessmentOut": "_recaptchaenterprise_73_GoogleCloudRecaptchaenterpriseV1AccountDefenderAssessmentOut",
        "GoogleCloudRecaptchaenterpriseV1TransactionDataGatewayInfoIn": "_recaptchaenterprise_74_GoogleCloudRecaptchaenterpriseV1TransactionDataGatewayInfoIn",
        "GoogleCloudRecaptchaenterpriseV1TransactionDataGatewayInfoOut": "_recaptchaenterprise_75_GoogleCloudRecaptchaenterpriseV1TransactionDataGatewayInfoOut",
        "GoogleCloudRecaptchaenterpriseV1ScoreMetricsIn": "_recaptchaenterprise_76_GoogleCloudRecaptchaenterpriseV1ScoreMetricsIn",
        "GoogleCloudRecaptchaenterpriseV1ScoreMetricsOut": "_recaptchaenterprise_77_GoogleCloudRecaptchaenterpriseV1ScoreMetricsOut",
        "GoogleCloudRecaptchaenterpriseV1TransactionDataIn": "_recaptchaenterprise_78_GoogleCloudRecaptchaenterpriseV1TransactionDataIn",
        "GoogleCloudRecaptchaenterpriseV1TransactionDataOut": "_recaptchaenterprise_79_GoogleCloudRecaptchaenterpriseV1TransactionDataOut",
        "GoogleCloudRecaptchaenterpriseV1ListKeysResponseIn": "_recaptchaenterprise_80_GoogleCloudRecaptchaenterpriseV1ListKeysResponseIn",
        "GoogleCloudRecaptchaenterpriseV1ListKeysResponseOut": "_recaptchaenterprise_81_GoogleCloudRecaptchaenterpriseV1ListKeysResponseOut",
        "GoogleCloudRecaptchaenterpriseV1FirewallPolicyIn": "_recaptchaenterprise_82_GoogleCloudRecaptchaenterpriseV1FirewallPolicyIn",
        "GoogleCloudRecaptchaenterpriseV1FirewallPolicyOut": "_recaptchaenterprise_83_GoogleCloudRecaptchaenterpriseV1FirewallPolicyOut",
        "GoogleCloudRecaptchaenterpriseV1ChallengeMetricsIn": "_recaptchaenterprise_84_GoogleCloudRecaptchaenterpriseV1ChallengeMetricsIn",
        "GoogleCloudRecaptchaenterpriseV1ChallengeMetricsOut": "_recaptchaenterprise_85_GoogleCloudRecaptchaenterpriseV1ChallengeMetricsOut",
        "GoogleProtobufEmptyIn": "_recaptchaenterprise_86_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_recaptchaenterprise_87_GoogleProtobufEmptyOut",
        "GoogleCloudRecaptchaenterpriseV1AssessmentIn": "_recaptchaenterprise_88_GoogleCloudRecaptchaenterpriseV1AssessmentIn",
        "GoogleCloudRecaptchaenterpriseV1AssessmentOut": "_recaptchaenterprise_89_GoogleCloudRecaptchaenterpriseV1AssessmentOut",
        "GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsResponseIn": "_recaptchaenterprise_90_GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsResponseIn",
        "GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsResponseOut": "_recaptchaenterprise_91_GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsResponseOut",
        "GoogleCloudRecaptchaenterpriseV1AndroidKeySettingsIn": "_recaptchaenterprise_92_GoogleCloudRecaptchaenterpriseV1AndroidKeySettingsIn",
        "GoogleCloudRecaptchaenterpriseV1AndroidKeySettingsOut": "_recaptchaenterprise_93_GoogleCloudRecaptchaenterpriseV1AndroidKeySettingsOut",
        "GoogleCloudRecaptchaenterpriseV1FirewallActionSetHeaderActionIn": "_recaptchaenterprise_94_GoogleCloudRecaptchaenterpriseV1FirewallActionSetHeaderActionIn",
        "GoogleCloudRecaptchaenterpriseV1FirewallActionSetHeaderActionOut": "_recaptchaenterprise_95_GoogleCloudRecaptchaenterpriseV1FirewallActionSetHeaderActionOut",
        "GoogleCloudRecaptchaenterpriseV1FirewallActionAllowActionIn": "_recaptchaenterprise_96_GoogleCloudRecaptchaenterpriseV1FirewallActionAllowActionIn",
        "GoogleCloudRecaptchaenterpriseV1FirewallActionAllowActionOut": "_recaptchaenterprise_97_GoogleCloudRecaptchaenterpriseV1FirewallActionAllowActionOut",
        "GoogleCloudRecaptchaenterpriseV1FirewallActionIn": "_recaptchaenterprise_98_GoogleCloudRecaptchaenterpriseV1FirewallActionIn",
        "GoogleCloudRecaptchaenterpriseV1FirewallActionOut": "_recaptchaenterprise_99_GoogleCloudRecaptchaenterpriseV1FirewallActionOut",
        "GoogleCloudRecaptchaenterpriseV1IOSKeySettingsIn": "_recaptchaenterprise_100_GoogleCloudRecaptchaenterpriseV1IOSKeySettingsIn",
        "GoogleCloudRecaptchaenterpriseV1IOSKeySettingsOut": "_recaptchaenterprise_101_GoogleCloudRecaptchaenterpriseV1IOSKeySettingsOut",
        "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentIn": "_recaptchaenterprise_102_GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentIn",
        "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentOut": "_recaptchaenterprise_103_GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
            "encryptedLeakMatchPrefixes": t.array(t.string()).optional(),
            "reencryptedUserCredentialsHash": t.string().optional(),
            "lookupHashPrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudRecaptchaenterpriseV1PrivatePasswordLeakVerificationOut"]
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
    types["GoogleCloudRecaptchaenterpriseV1EndpointVerificationInfoIn"] = t.struct(
        {"emailAddress": t.string().optional(), "phoneNumber": t.string().optional()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1EndpointVerificationInfoIn"])
    types["GoogleCloudRecaptchaenterpriseV1EndpointVerificationInfoOut"] = t.struct(
        {
            "lastVerificationTime": t.string().optional(),
            "emailAddress": t.string().optional(),
            "requestToken": t.string().optional(),
            "phoneNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1EndpointVerificationInfoOut"])
    types["GoogleCloudRecaptchaenterpriseV1RiskAnalysisIn"] = t.struct(
        {
            "score": t.number().optional(),
            "extendedVerdictReasons": t.array(t.string()).optional(),
            "reasons": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1RiskAnalysisIn"])
    types["GoogleCloudRecaptchaenterpriseV1RiskAnalysisOut"] = t.struct(
        {
            "score": t.number().optional(),
            "extendedVerdictReasons": t.array(t.string()).optional(),
            "reasons": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1RiskAnalysisOut"])
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
    types["GoogleRpcStatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["GoogleRpcStatusIn"])
    types["GoogleRpcStatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleRpcStatusOut"])
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
    types["GoogleCloudRecaptchaenterpriseV1FirewallActionRedirectActionIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1FirewallActionRedirectActionIn"])
    types["GoogleCloudRecaptchaenterpriseV1FirewallActionRedirectActionOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1FirewallActionRedirectActionOut"])
    types["GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentResponseIn"])
    types["GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentResponseOut"])
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
        "GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsRequestIn"
    ] = t.struct(
        {
            "pageToken": t.string().optional(),
            "pageSize": t.integer().optional(),
            "hashedAccountId": t.string().optional(),
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
            "pageToken": t.string().optional(),
            "pageSize": t.integer().optional(),
            "hashedAccountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsRequestOut"
        ]
    )
    types["GoogleCloudRecaptchaenterpriseV1EventIn"] = t.struct(
        {
            "expectedAction": t.string().optional(),
            "ja3": t.string().optional(),
            "hashedAccountId": t.string().optional(),
            "token": t.string().optional(),
            "firewallPolicyEvaluation": t.boolean().optional(),
            "userIpAddress": t.string().optional(),
            "headers": t.array(t.string()).optional(),
            "express": t.boolean().optional(),
            "userAgent": t.string().optional(),
            "wafTokenAssessment": t.boolean().optional(),
            "requestedUri": t.string().optional(),
            "transactionData": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TransactionDataIn"]
            ).optional(),
            "siteKey": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1EventIn"])
    types["GoogleCloudRecaptchaenterpriseV1EventOut"] = t.struct(
        {
            "expectedAction": t.string().optional(),
            "ja3": t.string().optional(),
            "hashedAccountId": t.string().optional(),
            "token": t.string().optional(),
            "firewallPolicyEvaluation": t.boolean().optional(),
            "userIpAddress": t.string().optional(),
            "headers": t.array(t.string()).optional(),
            "express": t.boolean().optional(),
            "userAgent": t.string().optional(),
            "wafTokenAssessment": t.boolean().optional(),
            "requestedUri": t.string().optional(),
            "transactionData": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TransactionDataOut"]
            ).optional(),
            "siteKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1EventOut"])
    types["GoogleCloudRecaptchaenterpriseV1FirewallActionBlockActionIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1FirewallActionBlockActionIn"])
    types["GoogleCloudRecaptchaenterpriseV1FirewallActionBlockActionOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1FirewallActionBlockActionOut"])
    types["GoogleCloudRecaptchaenterpriseV1TransactionDataUserIn"] = t.struct(
        {
            "creationMs": t.string().optional(),
            "phoneVerified": t.boolean().optional(),
            "email": t.string().optional(),
            "accountId": t.string().optional(),
            "phoneNumber": t.string().optional(),
            "emailVerified": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TransactionDataUserIn"])
    types["GoogleCloudRecaptchaenterpriseV1TransactionDataUserOut"] = t.struct(
        {
            "creationMs": t.string().optional(),
            "phoneVerified": t.boolean().optional(),
            "email": t.string().optional(),
            "accountId": t.string().optional(),
            "phoneNumber": t.string().optional(),
            "emailVerified": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TransactionDataUserOut"])
    types["GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupIn"] = t.struct(
        {"name": t.string()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupIn"])
    types["GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupOut"] = t.struct(
        {"name": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupOut"])
    types["GoogleCloudRecaptchaenterpriseV1TransactionDataItemIn"] = t.struct(
        {
            "name": t.string().optional(),
            "merchantAccountId": t.string().optional(),
            "quantity": t.string().optional(),
            "value": t.number().optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TransactionDataItemIn"])
    types["GoogleCloudRecaptchaenterpriseV1TransactionDataItemOut"] = t.struct(
        {
            "name": t.string().optional(),
            "merchantAccountId": t.string().optional(),
            "quantity": t.string().optional(),
            "value": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TransactionDataItemOut"])
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
            "endpoints": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudRecaptchaenterpriseV1EndpointVerificationInfoOut"
                    ]
                )
            ).optional(),
            "languageCode": t.string().optional(),
            "username": t.string().optional(),
            "latestVerificationResult": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1AccountVerificationInfoOut"])
    types["GoogleCloudRecaptchaenterpriseV1MetricsIn"] = t.struct(
        {
            "challengeMetrics": t.array(
                t.proxy(renames["GoogleCloudRecaptchaenterpriseV1ChallengeMetricsIn"])
            ).optional(),
            "startTime": t.string().optional(),
            "scoreMetrics": t.array(
                t.proxy(renames["GoogleCloudRecaptchaenterpriseV1ScoreMetricsIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1MetricsIn"])
    types["GoogleCloudRecaptchaenterpriseV1MetricsOut"] = t.struct(
        {
            "challengeMetrics": t.array(
                t.proxy(renames["GoogleCloudRecaptchaenterpriseV1ChallengeMetricsOut"])
            ).optional(),
            "startTime": t.string().optional(),
            "name": t.string().optional(),
            "scoreMetrics": t.array(
                t.proxy(renames["GoogleCloudRecaptchaenterpriseV1ScoreMetricsOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1MetricsOut"])
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
    types["GoogleCloudRecaptchaenterpriseV1WebKeySettingsIn"] = t.struct(
        {
            "challengeSecurityPreference": t.string().optional(),
            "allowAllDomains": t.boolean().optional(),
            "allowedDomains": t.array(t.string()).optional(),
            "integrationType": t.string(),
            "allowAmpTraffic": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1WebKeySettingsIn"])
    types["GoogleCloudRecaptchaenterpriseV1WebKeySettingsOut"] = t.struct(
        {
            "challengeSecurityPreference": t.string().optional(),
            "allowAllDomains": t.boolean().optional(),
            "allowedDomains": t.array(t.string()).optional(),
            "integrationType": t.string(),
            "allowAmpTraffic": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1WebKeySettingsOut"])
    types["GoogleCloudRecaptchaenterpriseV1KeyIn"] = t.struct(
        {
            "wafSettings": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1WafSettingsIn"]
            ).optional(),
            "iosSettings": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1IOSKeySettingsIn"]
            ).optional(),
            "displayName": t.string().optional(),
            "androidSettings": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1AndroidKeySettingsIn"]
            ).optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "testingOptions": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TestingOptionsIn"]
            ).optional(),
            "webSettings": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1WebKeySettingsIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1KeyIn"])
    types["GoogleCloudRecaptchaenterpriseV1KeyOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "wafSettings": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1WafSettingsOut"]
            ).optional(),
            "iosSettings": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1IOSKeySettingsOut"]
            ).optional(),
            "displayName": t.string().optional(),
            "androidSettings": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1AndroidKeySettingsOut"]
            ).optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "testingOptions": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TestingOptionsOut"]
            ).optional(),
            "webSettings": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1WebKeySettingsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1KeyOut"])
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
    types[
        "GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupsResponseIn"
    ] = t.struct(
        {
            "relatedAccountGroups": t.array(
                t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupIn"]
                )
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupsResponseIn"]
    )
    types[
        "GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupsResponseOut"
    ] = t.struct(
        {
            "relatedAccountGroups": t.array(
                t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupOut"]
                )
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupsResponseOut"]
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
    types["GoogleCloudRecaptchaenterpriseV1TransactionDataAddressIn"] = t.struct(
        {
            "postalCode": t.string().optional(),
            "locality": t.string().optional(),
            "recipient": t.string().optional(),
            "address": t.array(t.string()).optional(),
            "administrativeArea": t.string().optional(),
            "regionCode": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TransactionDataAddressIn"])
    types["GoogleCloudRecaptchaenterpriseV1TransactionDataAddressOut"] = t.struct(
        {
            "postalCode": t.string().optional(),
            "locality": t.string().optional(),
            "recipient": t.string().optional(),
            "address": t.array(t.string()).optional(),
            "administrativeArea": t.string().optional(),
            "regionCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TransactionDataAddressOut"])
    types["GoogleCloudRecaptchaenterpriseV1TransactionEventIn"] = t.struct(
        {
            "reason": t.string().optional(),
            "eventTime": t.string().optional(),
            "value": t.number().optional(),
            "eventType": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TransactionEventIn"])
    types["GoogleCloudRecaptchaenterpriseV1TransactionEventOut"] = t.struct(
        {
            "reason": t.string().optional(),
            "eventTime": t.string().optional(),
            "value": t.number().optional(),
            "eventType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TransactionEventOut"])
    types["GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentRequestIn"] = t.struct(
        {
            "hashedAccountId": t.string().optional(),
            "reasons": t.array(t.string()).optional(),
            "transactionEvent": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TransactionEventIn"]
            ).optional(),
            "annotation": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentRequestIn"])
    types["GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentRequestOut"] = t.struct(
        {
            "hashedAccountId": t.string().optional(),
            "reasons": t.array(t.string()).optional(),
            "transactionEvent": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TransactionEventOut"]
            ).optional(),
            "annotation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentRequestOut"])
    types["GoogleCloudRecaptchaenterpriseV1TokenPropertiesIn"] = t.struct(
        {
            "iosBundleId": t.string().optional(),
            "createTime": t.string().optional(),
            "valid": t.boolean().optional(),
            "androidPackageName": t.string().optional(),
            "invalidReason": t.string().optional(),
            "hostname": t.string().optional(),
            "action": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TokenPropertiesIn"])
    types["GoogleCloudRecaptchaenterpriseV1TokenPropertiesOut"] = t.struct(
        {
            "iosBundleId": t.string().optional(),
            "createTime": t.string().optional(),
            "valid": t.boolean().optional(),
            "androidPackageName": t.string().optional(),
            "invalidReason": t.string().optional(),
            "hostname": t.string().optional(),
            "action": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TokenPropertiesOut"])
    types["GoogleCloudRecaptchaenterpriseV1AccountDefenderAssessmentIn"] = t.struct(
        {"labels": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1AccountDefenderAssessmentIn"])
    types["GoogleCloudRecaptchaenterpriseV1AccountDefenderAssessmentOut"] = t.struct(
        {
            "labels": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1AccountDefenderAssessmentOut"])
    types["GoogleCloudRecaptchaenterpriseV1TransactionDataGatewayInfoIn"] = t.struct(
        {
            "gatewayResponseCode": t.string().optional(),
            "name": t.string().optional(),
            "cvvResponseCode": t.string().optional(),
            "avsResponseCode": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TransactionDataGatewayInfoIn"])
    types["GoogleCloudRecaptchaenterpriseV1TransactionDataGatewayInfoOut"] = t.struct(
        {
            "gatewayResponseCode": t.string().optional(),
            "name": t.string().optional(),
            "cvvResponseCode": t.string().optional(),
            "avsResponseCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TransactionDataGatewayInfoOut"])
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
    types["GoogleCloudRecaptchaenterpriseV1TransactionDataIn"] = t.struct(
        {
            "transactionId": t.string().optional(),
            "paymentMethod": t.string().optional(),
            "currencyCode": t.string().optional(),
            "gatewayInfo": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TransactionDataGatewayInfoIn"]
            ).optional(),
            "cardBin": t.string().optional(),
            "user": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TransactionDataUserIn"]
            ).optional(),
            "cardLastFour": t.string().optional(),
            "shippingValue": t.number().optional(),
            "value": t.number().optional(),
            "items": t.array(
                t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1TransactionDataItemIn"]
                )
            ).optional(),
            "shippingAddress": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TransactionDataAddressIn"]
            ).optional(),
            "merchants": t.array(
                t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1TransactionDataUserIn"]
                )
            ).optional(),
            "billingAddress": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TransactionDataAddressIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TransactionDataIn"])
    types["GoogleCloudRecaptchaenterpriseV1TransactionDataOut"] = t.struct(
        {
            "transactionId": t.string().optional(),
            "paymentMethod": t.string().optional(),
            "currencyCode": t.string().optional(),
            "gatewayInfo": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TransactionDataGatewayInfoOut"]
            ).optional(),
            "cardBin": t.string().optional(),
            "user": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TransactionDataUserOut"]
            ).optional(),
            "cardLastFour": t.string().optional(),
            "shippingValue": t.number().optional(),
            "value": t.number().optional(),
            "items": t.array(
                t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1TransactionDataItemOut"]
                )
            ).optional(),
            "shippingAddress": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TransactionDataAddressOut"]
            ).optional(),
            "merchants": t.array(
                t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1TransactionDataUserOut"]
                )
            ).optional(),
            "billingAddress": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TransactionDataAddressOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1TransactionDataOut"])
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
    types["GoogleCloudRecaptchaenterpriseV1FirewallPolicyIn"] = t.struct(
        {
            "name": t.string().optional(),
            "condition": t.string().optional(),
            "actions": t.array(
                t.proxy(renames["GoogleCloudRecaptchaenterpriseV1FirewallActionIn"])
            ).optional(),
            "description": t.string().optional(),
            "path": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1FirewallPolicyIn"])
    types["GoogleCloudRecaptchaenterpriseV1FirewallPolicyOut"] = t.struct(
        {
            "name": t.string().optional(),
            "condition": t.string().optional(),
            "actions": t.array(
                t.proxy(renames["GoogleCloudRecaptchaenterpriseV1FirewallActionOut"])
            ).optional(),
            "description": t.string().optional(),
            "path": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1FirewallPolicyOut"])
    types["GoogleCloudRecaptchaenterpriseV1ChallengeMetricsIn"] = t.struct(
        {
            "failedCount": t.string().optional(),
            "pageloadCount": t.string().optional(),
            "passedCount": t.string().optional(),
            "nocaptchaCount": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1ChallengeMetricsIn"])
    types["GoogleCloudRecaptchaenterpriseV1ChallengeMetricsOut"] = t.struct(
        {
            "failedCount": t.string().optional(),
            "pageloadCount": t.string().optional(),
            "passedCount": t.string().optional(),
            "nocaptchaCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1ChallengeMetricsOut"])
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
    types["GoogleCloudRecaptchaenterpriseV1AssessmentIn"] = t.struct(
        {
            "fraudPreventionAssessment": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentIn"]
            ).optional(),
            "firewallPolicyAssessment": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1FirewallPolicyAssessmentIn"]
            ).optional(),
            "accountVerification": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1AccountVerificationInfoIn"]
            ).optional(),
            "privatePasswordLeakVerification": t.proxy(
                renames[
                    "GoogleCloudRecaptchaenterpriseV1PrivatePasswordLeakVerificationIn"
                ]
            ).optional(),
            "accountDefenderAssessment": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1AccountDefenderAssessmentIn"]
            ).optional(),
            "event": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1EventIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1AssessmentIn"])
    types["GoogleCloudRecaptchaenterpriseV1AssessmentOut"] = t.struct(
        {
            "fraudPreventionAssessment": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentOut"]
            ).optional(),
            "firewallPolicyAssessment": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1FirewallPolicyAssessmentOut"]
            ).optional(),
            "tokenProperties": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1TokenPropertiesOut"]
            ).optional(),
            "name": t.string().optional(),
            "accountVerification": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1AccountVerificationInfoOut"]
            ).optional(),
            "privatePasswordLeakVerification": t.proxy(
                renames[
                    "GoogleCloudRecaptchaenterpriseV1PrivatePasswordLeakVerificationOut"
                ]
            ).optional(),
            "riskAnalysis": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1RiskAnalysisOut"]
            ).optional(),
            "accountDefenderAssessment": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1AccountDefenderAssessmentOut"]
            ).optional(),
            "event": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1EventOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1AssessmentOut"])
    types[
        "GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsResponseIn"
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
            "GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsResponseIn"
        ]
    )
    types[
        "GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsResponseOut"
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
            "GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsResponseOut"
        ]
    )
    types["GoogleCloudRecaptchaenterpriseV1AndroidKeySettingsIn"] = t.struct(
        {
            "supportNonGoogleAppStoreDistribution": t.boolean().optional(),
            "allowedPackageNames": t.array(t.string()).optional(),
            "allowAllPackageNames": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1AndroidKeySettingsIn"])
    types["GoogleCloudRecaptchaenterpriseV1AndroidKeySettingsOut"] = t.struct(
        {
            "supportNonGoogleAppStoreDistribution": t.boolean().optional(),
            "allowedPackageNames": t.array(t.string()).optional(),
            "allowAllPackageNames": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1AndroidKeySettingsOut"])
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
    types["GoogleCloudRecaptchaenterpriseV1FirewallActionAllowActionIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1FirewallActionAllowActionIn"])
    types["GoogleCloudRecaptchaenterpriseV1FirewallActionAllowActionOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRecaptchaenterpriseV1FirewallActionAllowActionOut"])
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
            "block": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1FirewallActionBlockActionIn"]
            ).optional(),
            "substitute": t.proxy(
                renames[
                    "GoogleCloudRecaptchaenterpriseV1FirewallActionSubstituteActionIn"
                ]
            ).optional(),
            "setHeader": t.proxy(
                renames[
                    "GoogleCloudRecaptchaenterpriseV1FirewallActionSetHeaderActionIn"
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
            "block": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1FirewallActionBlockActionOut"]
            ).optional(),
            "substitute": t.proxy(
                renames[
                    "GoogleCloudRecaptchaenterpriseV1FirewallActionSubstituteActionOut"
                ]
            ).optional(),
            "setHeader": t.proxy(
                renames[
                    "GoogleCloudRecaptchaenterpriseV1FirewallActionSetHeaderActionOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1FirewallActionOut"])
    types["GoogleCloudRecaptchaenterpriseV1IOSKeySettingsIn"] = t.struct(
        {
            "allowAllBundleIds": t.boolean().optional(),
            "appleDeveloperId": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1AppleDeveloperIdIn"]
            ).optional(),
            "allowedBundleIds": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1IOSKeySettingsIn"])
    types["GoogleCloudRecaptchaenterpriseV1IOSKeySettingsOut"] = t.struct(
        {
            "allowAllBundleIds": t.boolean().optional(),
            "appleDeveloperId": t.proxy(
                renames["GoogleCloudRecaptchaenterpriseV1AppleDeveloperIdOut"]
            ).optional(),
            "allowedBundleIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1IOSKeySettingsOut"])
    types["GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentIn"] = t.struct(
        {
            "stolenInstrumentVerdict": t.proxy(
                renames[
                    "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentStolenInstrumentVerdictIn"
                ]
            ).optional(),
            "transactionRisk": t.number().optional(),
            "behavioralTrustVerdict": t.proxy(
                renames[
                    "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentBehavioralTrustVerdictIn"
                ]
            ).optional(),
            "cardTestingVerdict": t.proxy(
                renames[
                    "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentCardTestingVerdictIn"
                ]
            ).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentIn"])
    types["GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentOut"] = t.struct(
        {
            "stolenInstrumentVerdict": t.proxy(
                renames[
                    "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentStolenInstrumentVerdictOut"
                ]
            ).optional(),
            "transactionRisk": t.number().optional(),
            "behavioralTrustVerdict": t.proxy(
                renames[
                    "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentBehavioralTrustVerdictOut"
                ]
            ).optional(),
            "cardTestingVerdict": t.proxy(
                renames[
                    "GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentCardTestingVerdictOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentOut"])

    functions = {}
    functions[
        "projectsRelatedaccountgroupmembershipsSearch"
    ] = recaptchaenterprise.post(
        "v1/{project}/relatedaccountgroupmemberships:search",
        t.struct(
            {
                "project": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "hashedAccountId": t.string().optional(),
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
    functions["projectsKeysGet"] = recaptchaenterprise.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "wafSettings": t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1WafSettingsIn"]
                ).optional(),
                "iosSettings": t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1IOSKeySettingsIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "androidSettings": t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1AndroidKeySettingsIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "testingOptions": t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1TestingOptionsIn"]
                ).optional(),
                "webSettings": t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1WebKeySettingsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecaptchaenterpriseV1KeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsKeysList"] = recaptchaenterprise.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "wafSettings": t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1WafSettingsIn"]
                ).optional(),
                "iosSettings": t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1IOSKeySettingsIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "androidSettings": t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1AndroidKeySettingsIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "testingOptions": t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1TestingOptionsIn"]
                ).optional(),
                "webSettings": t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1WebKeySettingsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecaptchaenterpriseV1KeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsKeysGetMetrics"] = recaptchaenterprise.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "wafSettings": t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1WafSettingsIn"]
                ).optional(),
                "iosSettings": t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1IOSKeySettingsIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "androidSettings": t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1AndroidKeySettingsIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "testingOptions": t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1TestingOptionsIn"]
                ).optional(),
                "webSettings": t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1WebKeySettingsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecaptchaenterpriseV1KeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsKeysMigrate"] = recaptchaenterprise.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "wafSettings": t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1WafSettingsIn"]
                ).optional(),
                "iosSettings": t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1IOSKeySettingsIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "androidSettings": t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1AndroidKeySettingsIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "testingOptions": t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1TestingOptionsIn"]
                ).optional(),
                "webSettings": t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1WebKeySettingsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecaptchaenterpriseV1KeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsKeysDelete"] = recaptchaenterprise.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "wafSettings": t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1WafSettingsIn"]
                ).optional(),
                "iosSettings": t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1IOSKeySettingsIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "androidSettings": t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1AndroidKeySettingsIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "testingOptions": t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1TestingOptionsIn"]
                ).optional(),
                "webSettings": t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1WebKeySettingsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecaptchaenterpriseV1KeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsKeysRetrieveLegacySecretKey"] = recaptchaenterprise.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "wafSettings": t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1WafSettingsIn"]
                ).optional(),
                "iosSettings": t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1IOSKeySettingsIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "androidSettings": t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1AndroidKeySettingsIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "testingOptions": t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1TestingOptionsIn"]
                ).optional(),
                "webSettings": t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1WebKeySettingsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecaptchaenterpriseV1KeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsKeysCreate"] = recaptchaenterprise.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "wafSettings": t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1WafSettingsIn"]
                ).optional(),
                "iosSettings": t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1IOSKeySettingsIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "androidSettings": t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1AndroidKeySettingsIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "testingOptions": t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1TestingOptionsIn"]
                ).optional(),
                "webSettings": t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1WebKeySettingsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecaptchaenterpriseV1KeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsKeysPatch"] = recaptchaenterprise.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "wafSettings": t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1WafSettingsIn"]
                ).optional(),
                "iosSettings": t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1IOSKeySettingsIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "androidSettings": t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1AndroidKeySettingsIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "testingOptions": t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1TestingOptionsIn"]
                ).optional(),
                "webSettings": t.proxy(
                    renames["GoogleCloudRecaptchaenterpriseV1WebKeySettingsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecaptchaenterpriseV1KeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsFirewallpoliciesPatch"] = recaptchaenterprise.get(
        "v1/{parent}/firewallpolicies",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudRecaptchaenterpriseV1ListFirewallPoliciesResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsFirewallpoliciesCreate"] = recaptchaenterprise.get(
        "v1/{parent}/firewallpolicies",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudRecaptchaenterpriseV1ListFirewallPoliciesResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsFirewallpoliciesGet"] = recaptchaenterprise.get(
        "v1/{parent}/firewallpolicies",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudRecaptchaenterpriseV1ListFirewallPoliciesResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsFirewallpoliciesDelete"] = recaptchaenterprise.get(
        "v1/{parent}/firewallpolicies",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudRecaptchaenterpriseV1ListFirewallPoliciesResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsFirewallpoliciesList"] = recaptchaenterprise.get(
        "v1/{parent}/firewallpolicies",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudRecaptchaenterpriseV1ListFirewallPoliciesResponseOut"]
        ),
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
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
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
    functions["projectsAssessmentsAnnotate"] = recaptchaenterprise.post(
        "v1/{parent}/assessments",
        t.struct(
            {
                "parent": t.string(),
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
                "privatePasswordLeakVerification": t.proxy(
                    renames[
                        "GoogleCloudRecaptchaenterpriseV1PrivatePasswordLeakVerificationIn"
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
                "privatePasswordLeakVerification": t.proxy(
                    renames[
                        "GoogleCloudRecaptchaenterpriseV1PrivatePasswordLeakVerificationIn"
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
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecaptchaenterpriseV1AssessmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="recaptchaenterprise",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
