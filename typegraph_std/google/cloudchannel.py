from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_cloudchannel() -> Import:
    cloudchannel = HTTPRuntime("https://cloudchannel.googleapis.com/")

    renames = {
        "ErrorResponse": "_cloudchannel_1_ErrorResponse",
        "GoogleLongrunningCancelOperationRequestIn": "_cloudchannel_2_GoogleLongrunningCancelOperationRequestIn",
        "GoogleLongrunningCancelOperationRequestOut": "_cloudchannel_3_GoogleLongrunningCancelOperationRequestOut",
        "GoogleCloudChannelV1alpha1AssociationInfoIn": "_cloudchannel_4_GoogleCloudChannelV1alpha1AssociationInfoIn",
        "GoogleCloudChannelV1alpha1AssociationInfoOut": "_cloudchannel_5_GoogleCloudChannelV1alpha1AssociationInfoOut",
        "GoogleCloudChannelV1ChangeOfferRequestIn": "_cloudchannel_6_GoogleCloudChannelV1ChangeOfferRequestIn",
        "GoogleCloudChannelV1ChangeOfferRequestOut": "_cloudchannel_7_GoogleCloudChannelV1ChangeOfferRequestOut",
        "GoogleTypeMoneyIn": "_cloudchannel_8_GoogleTypeMoneyIn",
        "GoogleTypeMoneyOut": "_cloudchannel_9_GoogleTypeMoneyOut",
        "GoogleCloudChannelV1SkuIn": "_cloudchannel_10_GoogleCloudChannelV1SkuIn",
        "GoogleCloudChannelV1SkuOut": "_cloudchannel_11_GoogleCloudChannelV1SkuOut",
        "GoogleCloudChannelV1ListOffersResponseIn": "_cloudchannel_12_GoogleCloudChannelV1ListOffersResponseIn",
        "GoogleCloudChannelV1ListOffersResponseOut": "_cloudchannel_13_GoogleCloudChannelV1ListOffersResponseOut",
        "GoogleCloudChannelV1CreateEntitlementRequestIn": "_cloudchannel_14_GoogleCloudChannelV1CreateEntitlementRequestIn",
        "GoogleCloudChannelV1CreateEntitlementRequestOut": "_cloudchannel_15_GoogleCloudChannelV1CreateEntitlementRequestOut",
        "GoogleCloudChannelV1RegisterSubscriberRequestIn": "_cloudchannel_16_GoogleCloudChannelV1RegisterSubscriberRequestIn",
        "GoogleCloudChannelV1RegisterSubscriberRequestOut": "_cloudchannel_17_GoogleCloudChannelV1RegisterSubscriberRequestOut",
        "GoogleCloudChannelV1CommitmentSettingsIn": "_cloudchannel_18_GoogleCloudChannelV1CommitmentSettingsIn",
        "GoogleCloudChannelV1CommitmentSettingsOut": "_cloudchannel_19_GoogleCloudChannelV1CommitmentSettingsOut",
        "GoogleCloudChannelV1PlanIn": "_cloudchannel_20_GoogleCloudChannelV1PlanIn",
        "GoogleCloudChannelV1PlanOut": "_cloudchannel_21_GoogleCloudChannelV1PlanOut",
        "GoogleCloudChannelV1alpha1SubscriberEventIn": "_cloudchannel_22_GoogleCloudChannelV1alpha1SubscriberEventIn",
        "GoogleCloudChannelV1alpha1SubscriberEventOut": "_cloudchannel_23_GoogleCloudChannelV1alpha1SubscriberEventOut",
        "GoogleCloudChannelV1ListProductsResponseIn": "_cloudchannel_24_GoogleCloudChannelV1ListProductsResponseIn",
        "GoogleCloudChannelV1ListProductsResponseOut": "_cloudchannel_25_GoogleCloudChannelV1ListProductsResponseOut",
        "GoogleCloudChannelV1alpha1CommitmentSettingsIn": "_cloudchannel_26_GoogleCloudChannelV1alpha1CommitmentSettingsIn",
        "GoogleCloudChannelV1alpha1CommitmentSettingsOut": "_cloudchannel_27_GoogleCloudChannelV1alpha1CommitmentSettingsOut",
        "GoogleCloudChannelV1MediaIn": "_cloudchannel_28_GoogleCloudChannelV1MediaIn",
        "GoogleCloudChannelV1MediaOut": "_cloudchannel_29_GoogleCloudChannelV1MediaOut",
        "GoogleCloudChannelV1CustomerIn": "_cloudchannel_30_GoogleCloudChannelV1CustomerIn",
        "GoogleCloudChannelV1CustomerOut": "_cloudchannel_31_GoogleCloudChannelV1CustomerOut",
        "GoogleCloudChannelV1TransferableSkuIn": "_cloudchannel_32_GoogleCloudChannelV1TransferableSkuIn",
        "GoogleCloudChannelV1TransferableSkuOut": "_cloudchannel_33_GoogleCloudChannelV1TransferableSkuOut",
        "GoogleCloudChannelV1FetchReportResultsResponseIn": "_cloudchannel_34_GoogleCloudChannelV1FetchReportResultsResponseIn",
        "GoogleCloudChannelV1FetchReportResultsResponseOut": "_cloudchannel_35_GoogleCloudChannelV1FetchReportResultsResponseOut",
        "GoogleCloudChannelV1alpha1RunReportJobResponseIn": "_cloudchannel_36_GoogleCloudChannelV1alpha1RunReportJobResponseIn",
        "GoogleCloudChannelV1alpha1RunReportJobResponseOut": "_cloudchannel_37_GoogleCloudChannelV1alpha1RunReportJobResponseOut",
        "GoogleCloudChannelV1TransferEligibilityIn": "_cloudchannel_38_GoogleCloudChannelV1TransferEligibilityIn",
        "GoogleCloudChannelV1TransferEligibilityOut": "_cloudchannel_39_GoogleCloudChannelV1TransferEligibilityOut",
        "GoogleCloudChannelV1PricePhaseIn": "_cloudchannel_40_GoogleCloudChannelV1PricePhaseIn",
        "GoogleCloudChannelV1PricePhaseOut": "_cloudchannel_41_GoogleCloudChannelV1PricePhaseOut",
        "GoogleCloudChannelV1RepricingAdjustmentIn": "_cloudchannel_42_GoogleCloudChannelV1RepricingAdjustmentIn",
        "GoogleCloudChannelV1RepricingAdjustmentOut": "_cloudchannel_43_GoogleCloudChannelV1RepricingAdjustmentOut",
        "GoogleCloudChannelV1ValueIn": "_cloudchannel_44_GoogleCloudChannelV1ValueIn",
        "GoogleCloudChannelV1ValueOut": "_cloudchannel_45_GoogleCloudChannelV1ValueOut",
        "GoogleCloudChannelV1DateRangeIn": "_cloudchannel_46_GoogleCloudChannelV1DateRangeIn",
        "GoogleCloudChannelV1DateRangeOut": "_cloudchannel_47_GoogleCloudChannelV1DateRangeOut",
        "GoogleCloudChannelV1CustomerRepricingConfigIn": "_cloudchannel_48_GoogleCloudChannelV1CustomerRepricingConfigIn",
        "GoogleCloudChannelV1CustomerRepricingConfigOut": "_cloudchannel_49_GoogleCloudChannelV1CustomerRepricingConfigOut",
        "GoogleCloudChannelV1SkuGroupConditionIn": "_cloudchannel_50_GoogleCloudChannelV1SkuGroupConditionIn",
        "GoogleCloudChannelV1SkuGroupConditionOut": "_cloudchannel_51_GoogleCloudChannelV1SkuGroupConditionOut",
        "GoogleCloudChannelV1ColumnIn": "_cloudchannel_52_GoogleCloudChannelV1ColumnIn",
        "GoogleCloudChannelV1ColumnOut": "_cloudchannel_53_GoogleCloudChannelV1ColumnOut",
        "GoogleProtobufEmptyIn": "_cloudchannel_54_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_cloudchannel_55_GoogleProtobufEmptyOut",
        "GoogleCloudChannelV1RowIn": "_cloudchannel_56_GoogleCloudChannelV1RowIn",
        "GoogleCloudChannelV1RowOut": "_cloudchannel_57_GoogleCloudChannelV1RowOut",
        "GoogleCloudChannelV1ImportCustomerRequestIn": "_cloudchannel_58_GoogleCloudChannelV1ImportCustomerRequestIn",
        "GoogleCloudChannelV1ImportCustomerRequestOut": "_cloudchannel_59_GoogleCloudChannelV1ImportCustomerRequestOut",
        "GoogleCloudChannelV1RepricingConditionIn": "_cloudchannel_60_GoogleCloudChannelV1RepricingConditionIn",
        "GoogleCloudChannelV1RepricingConditionOut": "_cloudchannel_61_GoogleCloudChannelV1RepricingConditionOut",
        "GoogleCloudChannelV1UnregisterSubscriberResponseIn": "_cloudchannel_62_GoogleCloudChannelV1UnregisterSubscriberResponseIn",
        "GoogleCloudChannelV1UnregisterSubscriberResponseOut": "_cloudchannel_63_GoogleCloudChannelV1UnregisterSubscriberResponseOut",
        "GoogleCloudChannelV1TransferEntitlementsResponseIn": "_cloudchannel_64_GoogleCloudChannelV1TransferEntitlementsResponseIn",
        "GoogleCloudChannelV1TransferEntitlementsResponseOut": "_cloudchannel_65_GoogleCloudChannelV1TransferEntitlementsResponseOut",
        "GoogleCloudChannelV1ListSkusResponseIn": "_cloudchannel_66_GoogleCloudChannelV1ListSkusResponseIn",
        "GoogleCloudChannelV1ListSkusResponseOut": "_cloudchannel_67_GoogleCloudChannelV1ListSkusResponseOut",
        "GoogleCloudChannelV1alpha1ReportIn": "_cloudchannel_68_GoogleCloudChannelV1alpha1ReportIn",
        "GoogleCloudChannelV1alpha1ReportOut": "_cloudchannel_69_GoogleCloudChannelV1alpha1ReportOut",
        "GoogleCloudChannelV1PercentageAdjustmentIn": "_cloudchannel_70_GoogleCloudChannelV1PercentageAdjustmentIn",
        "GoogleCloudChannelV1PercentageAdjustmentOut": "_cloudchannel_71_GoogleCloudChannelV1PercentageAdjustmentOut",
        "GoogleCloudChannelV1TransferableOfferIn": "_cloudchannel_72_GoogleCloudChannelV1TransferableOfferIn",
        "GoogleCloudChannelV1TransferableOfferOut": "_cloudchannel_73_GoogleCloudChannelV1TransferableOfferOut",
        "GoogleCloudChannelV1ListTransferableSkusResponseIn": "_cloudchannel_74_GoogleCloudChannelV1ListTransferableSkusResponseIn",
        "GoogleCloudChannelV1ListTransferableSkusResponseOut": "_cloudchannel_75_GoogleCloudChannelV1ListTransferableSkusResponseOut",
        "GoogleCloudChannelV1CheckCloudIdentityAccountsExistRequestIn": "_cloudchannel_76_GoogleCloudChannelV1CheckCloudIdentityAccountsExistRequestIn",
        "GoogleCloudChannelV1CheckCloudIdentityAccountsExistRequestOut": "_cloudchannel_77_GoogleCloudChannelV1CheckCloudIdentityAccountsExistRequestOut",
        "GoogleCloudChannelV1EntitlementIn": "_cloudchannel_78_GoogleCloudChannelV1EntitlementIn",
        "GoogleCloudChannelV1EntitlementOut": "_cloudchannel_79_GoogleCloudChannelV1EntitlementOut",
        "GoogleCloudChannelV1ListSubscribersResponseIn": "_cloudchannel_80_GoogleCloudChannelV1ListSubscribersResponseIn",
        "GoogleCloudChannelV1ListSubscribersResponseOut": "_cloudchannel_81_GoogleCloudChannelV1ListSubscribersResponseOut",
        "GoogleCloudChannelV1TransferEntitlementsRequestIn": "_cloudchannel_82_GoogleCloudChannelV1TransferEntitlementsRequestIn",
        "GoogleCloudChannelV1TransferEntitlementsRequestOut": "_cloudchannel_83_GoogleCloudChannelV1TransferEntitlementsRequestOut",
        "GoogleCloudChannelV1RunReportJobResponseIn": "_cloudchannel_84_GoogleCloudChannelV1RunReportJobResponseIn",
        "GoogleCloudChannelV1RunReportJobResponseOut": "_cloudchannel_85_GoogleCloudChannelV1RunReportJobResponseOut",
        "GoogleCloudChannelV1CustomerEventIn": "_cloudchannel_86_GoogleCloudChannelV1CustomerEventIn",
        "GoogleCloudChannelV1CustomerEventOut": "_cloudchannel_87_GoogleCloudChannelV1CustomerEventOut",
        "GoogleCloudChannelV1PriceIn": "_cloudchannel_88_GoogleCloudChannelV1PriceIn",
        "GoogleCloudChannelV1PriceOut": "_cloudchannel_89_GoogleCloudChannelV1PriceOut",
        "GoogleCloudChannelV1CheckCloudIdentityAccountsExistResponseIn": "_cloudchannel_90_GoogleCloudChannelV1CheckCloudIdentityAccountsExistResponseIn",
        "GoogleCloudChannelV1CheckCloudIdentityAccountsExistResponseOut": "_cloudchannel_91_GoogleCloudChannelV1CheckCloudIdentityAccountsExistResponseOut",
        "GoogleCloudChannelV1RegisterSubscriberResponseIn": "_cloudchannel_92_GoogleCloudChannelV1RegisterSubscriberResponseIn",
        "GoogleCloudChannelV1RegisterSubscriberResponseOut": "_cloudchannel_93_GoogleCloudChannelV1RegisterSubscriberResponseOut",
        "GoogleCloudChannelV1ListCustomerRepricingConfigsResponseIn": "_cloudchannel_94_GoogleCloudChannelV1ListCustomerRepricingConfigsResponseIn",
        "GoogleCloudChannelV1ListCustomerRepricingConfigsResponseOut": "_cloudchannel_95_GoogleCloudChannelV1ListCustomerRepricingConfigsResponseOut",
        "GoogleCloudChannelV1alpha1DateRangeIn": "_cloudchannel_96_GoogleCloudChannelV1alpha1DateRangeIn",
        "GoogleCloudChannelV1alpha1DateRangeOut": "_cloudchannel_97_GoogleCloudChannelV1alpha1DateRangeOut",
        "GoogleCloudChannelV1alpha1ReportStatusIn": "_cloudchannel_98_GoogleCloudChannelV1alpha1ReportStatusIn",
        "GoogleCloudChannelV1alpha1ReportStatusOut": "_cloudchannel_99_GoogleCloudChannelV1alpha1ReportStatusOut",
        "GoogleCloudChannelV1alpha1ReportJobIn": "_cloudchannel_100_GoogleCloudChannelV1alpha1ReportJobIn",
        "GoogleCloudChannelV1alpha1ReportJobOut": "_cloudchannel_101_GoogleCloudChannelV1alpha1ReportJobOut",
        "GoogleCloudChannelV1OfferIn": "_cloudchannel_102_GoogleCloudChannelV1OfferIn",
        "GoogleCloudChannelV1OfferOut": "_cloudchannel_103_GoogleCloudChannelV1OfferOut",
        "GoogleCloudChannelV1alpha1EntitlementIn": "_cloudchannel_104_GoogleCloudChannelV1alpha1EntitlementIn",
        "GoogleCloudChannelV1alpha1EntitlementOut": "_cloudchannel_105_GoogleCloudChannelV1alpha1EntitlementOut",
        "GoogleTypeDateIn": "_cloudchannel_106_GoogleTypeDateIn",
        "GoogleTypeDateOut": "_cloudchannel_107_GoogleTypeDateOut",
        "GoogleCloudChannelV1ProvisionCloudIdentityRequestIn": "_cloudchannel_108_GoogleCloudChannelV1ProvisionCloudIdentityRequestIn",
        "GoogleCloudChannelV1ProvisionCloudIdentityRequestOut": "_cloudchannel_109_GoogleCloudChannelV1ProvisionCloudIdentityRequestOut",
        "GoogleCloudChannelV1ListReportsResponseIn": "_cloudchannel_110_GoogleCloudChannelV1ListReportsResponseIn",
        "GoogleCloudChannelV1ListReportsResponseOut": "_cloudchannel_111_GoogleCloudChannelV1ListReportsResponseOut",
        "GoogleCloudChannelV1alpha1OperationMetadataIn": "_cloudchannel_112_GoogleCloudChannelV1alpha1OperationMetadataIn",
        "GoogleCloudChannelV1alpha1OperationMetadataOut": "_cloudchannel_113_GoogleCloudChannelV1alpha1OperationMetadataOut",
        "GoogleCloudChannelV1ListPurchasableOffersResponseIn": "_cloudchannel_114_GoogleCloudChannelV1ListPurchasableOffersResponseIn",
        "GoogleCloudChannelV1ListPurchasableOffersResponseOut": "_cloudchannel_115_GoogleCloudChannelV1ListPurchasableOffersResponseOut",
        "GoogleCloudChannelV1ChannelPartnerRepricingConfigIn": "_cloudchannel_116_GoogleCloudChannelV1ChannelPartnerRepricingConfigIn",
        "GoogleCloudChannelV1ChannelPartnerRepricingConfigOut": "_cloudchannel_117_GoogleCloudChannelV1ChannelPartnerRepricingConfigOut",
        "GoogleCloudChannelV1SuspendEntitlementRequestIn": "_cloudchannel_118_GoogleCloudChannelV1SuspendEntitlementRequestIn",
        "GoogleCloudChannelV1SuspendEntitlementRequestOut": "_cloudchannel_119_GoogleCloudChannelV1SuspendEntitlementRequestOut",
        "GoogleCloudChannelV1MarketingInfoIn": "_cloudchannel_120_GoogleCloudChannelV1MarketingInfoIn",
        "GoogleCloudChannelV1MarketingInfoOut": "_cloudchannel_121_GoogleCloudChannelV1MarketingInfoOut",
        "GoogleCloudChannelV1AssociationInfoIn": "_cloudchannel_122_GoogleCloudChannelV1AssociationInfoIn",
        "GoogleCloudChannelV1AssociationInfoOut": "_cloudchannel_123_GoogleCloudChannelV1AssociationInfoOut",
        "GoogleCloudChannelV1PurchasableSkuIn": "_cloudchannel_124_GoogleCloudChannelV1PurchasableSkuIn",
        "GoogleCloudChannelV1PurchasableSkuOut": "_cloudchannel_125_GoogleCloudChannelV1PurchasableSkuOut",
        "GoogleCloudChannelV1FetchReportResultsRequestIn": "_cloudchannel_126_GoogleCloudChannelV1FetchReportResultsRequestIn",
        "GoogleCloudChannelV1FetchReportResultsRequestOut": "_cloudchannel_127_GoogleCloudChannelV1FetchReportResultsRequestOut",
        "GoogleCloudChannelV1RunReportJobRequestIn": "_cloudchannel_128_GoogleCloudChannelV1RunReportJobRequestIn",
        "GoogleCloudChannelV1RunReportJobRequestOut": "_cloudchannel_129_GoogleCloudChannelV1RunReportJobRequestOut",
        "GoogleCloudChannelV1alpha1ValueIn": "_cloudchannel_130_GoogleCloudChannelV1alpha1ValueIn",
        "GoogleCloudChannelV1alpha1ValueOut": "_cloudchannel_131_GoogleCloudChannelV1alpha1ValueOut",
        "GoogleCloudChannelV1ActivateEntitlementRequestIn": "_cloudchannel_132_GoogleCloudChannelV1ActivateEntitlementRequestIn",
        "GoogleCloudChannelV1ActivateEntitlementRequestOut": "_cloudchannel_133_GoogleCloudChannelV1ActivateEntitlementRequestOut",
        "GoogleCloudChannelV1ChangeRenewalSettingsRequestIn": "_cloudchannel_134_GoogleCloudChannelV1ChangeRenewalSettingsRequestIn",
        "GoogleCloudChannelV1ChangeRenewalSettingsRequestOut": "_cloudchannel_135_GoogleCloudChannelV1ChangeRenewalSettingsRequestOut",
        "GoogleCloudChannelV1UnregisterSubscriberRequestIn": "_cloudchannel_136_GoogleCloudChannelV1UnregisterSubscriberRequestIn",
        "GoogleCloudChannelV1UnregisterSubscriberRequestOut": "_cloudchannel_137_GoogleCloudChannelV1UnregisterSubscriberRequestOut",
        "GoogleCloudChannelV1ReportResultsMetadataIn": "_cloudchannel_138_GoogleCloudChannelV1ReportResultsMetadataIn",
        "GoogleCloudChannelV1ReportResultsMetadataOut": "_cloudchannel_139_GoogleCloudChannelV1ReportResultsMetadataOut",
        "GoogleCloudChannelV1ReportIn": "_cloudchannel_140_GoogleCloudChannelV1ReportIn",
        "GoogleCloudChannelV1ReportOut": "_cloudchannel_141_GoogleCloudChannelV1ReportOut",
        "GoogleCloudChannelV1OperationMetadataIn": "_cloudchannel_142_GoogleCloudChannelV1OperationMetadataIn",
        "GoogleCloudChannelV1OperationMetadataOut": "_cloudchannel_143_GoogleCloudChannelV1OperationMetadataOut",
        "GoogleCloudChannelV1BillingAccountPurchaseInfoIn": "_cloudchannel_144_GoogleCloudChannelV1BillingAccountPurchaseInfoIn",
        "GoogleCloudChannelV1BillingAccountPurchaseInfoOut": "_cloudchannel_145_GoogleCloudChannelV1BillingAccountPurchaseInfoOut",
        "GoogleCloudChannelV1ChangeParametersRequestIn": "_cloudchannel_146_GoogleCloudChannelV1ChangeParametersRequestIn",
        "GoogleCloudChannelV1ChangeParametersRequestOut": "_cloudchannel_147_GoogleCloudChannelV1ChangeParametersRequestOut",
        "GoogleCloudChannelV1alpha1TrialSettingsIn": "_cloudchannel_148_GoogleCloudChannelV1alpha1TrialSettingsIn",
        "GoogleCloudChannelV1alpha1TrialSettingsOut": "_cloudchannel_149_GoogleCloudChannelV1alpha1TrialSettingsOut",
        "GoogleCloudChannelV1SubscriberEventIn": "_cloudchannel_150_GoogleCloudChannelV1SubscriberEventIn",
        "GoogleCloudChannelV1SubscriberEventOut": "_cloudchannel_151_GoogleCloudChannelV1SubscriberEventOut",
        "GoogleCloudChannelV1ConstraintsIn": "_cloudchannel_152_GoogleCloudChannelV1ConstraintsIn",
        "GoogleCloudChannelV1ConstraintsOut": "_cloudchannel_153_GoogleCloudChannelV1ConstraintsOut",
        "GoogleCloudChannelV1alpha1PeriodIn": "_cloudchannel_154_GoogleCloudChannelV1alpha1PeriodIn",
        "GoogleCloudChannelV1alpha1PeriodOut": "_cloudchannel_155_GoogleCloudChannelV1alpha1PeriodOut",
        "GoogleTypeTimeZoneIn": "_cloudchannel_156_GoogleTypeTimeZoneIn",
        "GoogleTypeTimeZoneOut": "_cloudchannel_157_GoogleTypeTimeZoneOut",
        "GoogleRpcStatusIn": "_cloudchannel_158_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_cloudchannel_159_GoogleRpcStatusOut",
        "GoogleCloudChannelV1ListTransferableOffersResponseIn": "_cloudchannel_160_GoogleCloudChannelV1ListTransferableOffersResponseIn",
        "GoogleCloudChannelV1ListTransferableOffersResponseOut": "_cloudchannel_161_GoogleCloudChannelV1ListTransferableOffersResponseOut",
        "GoogleCloudChannelV1RepricingConfigEntitlementGranularityIn": "_cloudchannel_162_GoogleCloudChannelV1RepricingConfigEntitlementGranularityIn",
        "GoogleCloudChannelV1RepricingConfigEntitlementGranularityOut": "_cloudchannel_163_GoogleCloudChannelV1RepricingConfigEntitlementGranularityOut",
        "GoogleCloudChannelV1PriceTierIn": "_cloudchannel_164_GoogleCloudChannelV1PriceTierIn",
        "GoogleCloudChannelV1PriceTierOut": "_cloudchannel_165_GoogleCloudChannelV1PriceTierOut",
        "GoogleCloudChannelV1alpha1EntitlementEventIn": "_cloudchannel_166_GoogleCloudChannelV1alpha1EntitlementEventIn",
        "GoogleCloudChannelV1alpha1EntitlementEventOut": "_cloudchannel_167_GoogleCloudChannelV1alpha1EntitlementEventOut",
        "GoogleCloudChannelV1ReportStatusIn": "_cloudchannel_168_GoogleCloudChannelV1ReportStatusIn",
        "GoogleCloudChannelV1ReportStatusOut": "_cloudchannel_169_GoogleCloudChannelV1ReportStatusOut",
        "GoogleCloudChannelV1alpha1ParameterIn": "_cloudchannel_170_GoogleCloudChannelV1alpha1ParameterIn",
        "GoogleCloudChannelV1alpha1ParameterOut": "_cloudchannel_171_GoogleCloudChannelV1alpha1ParameterOut",
        "GoogleCloudChannelV1CloudIdentityInfoIn": "_cloudchannel_172_GoogleCloudChannelV1CloudIdentityInfoIn",
        "GoogleCloudChannelV1CloudIdentityInfoOut": "_cloudchannel_173_GoogleCloudChannelV1CloudIdentityInfoOut",
        "GoogleCloudChannelV1alpha1ReportResultsMetadataIn": "_cloudchannel_174_GoogleCloudChannelV1alpha1ReportResultsMetadataIn",
        "GoogleCloudChannelV1alpha1ReportResultsMetadataOut": "_cloudchannel_175_GoogleCloudChannelV1alpha1ReportResultsMetadataOut",
        "GoogleCloudChannelV1alpha1CustomerEventIn": "_cloudchannel_176_GoogleCloudChannelV1alpha1CustomerEventIn",
        "GoogleCloudChannelV1alpha1CustomerEventOut": "_cloudchannel_177_GoogleCloudChannelV1alpha1CustomerEventOut",
        "GoogleCloudChannelV1BillingAccountIn": "_cloudchannel_178_GoogleCloudChannelV1BillingAccountIn",
        "GoogleCloudChannelV1BillingAccountOut": "_cloudchannel_179_GoogleCloudChannelV1BillingAccountOut",
        "GoogleCloudChannelV1RepricingConfigIn": "_cloudchannel_180_GoogleCloudChannelV1RepricingConfigIn",
        "GoogleCloudChannelV1RepricingConfigOut": "_cloudchannel_181_GoogleCloudChannelV1RepricingConfigOut",
        "GoogleCloudChannelV1UpdateChannelPartnerLinkRequestIn": "_cloudchannel_182_GoogleCloudChannelV1UpdateChannelPartnerLinkRequestIn",
        "GoogleCloudChannelV1UpdateChannelPartnerLinkRequestOut": "_cloudchannel_183_GoogleCloudChannelV1UpdateChannelPartnerLinkRequestOut",
        "GoogleCloudChannelV1ContactInfoIn": "_cloudchannel_184_GoogleCloudChannelV1ContactInfoIn",
        "GoogleCloudChannelV1ContactInfoOut": "_cloudchannel_185_GoogleCloudChannelV1ContactInfoOut",
        "GoogleCloudChannelV1ParameterIn": "_cloudchannel_186_GoogleCloudChannelV1ParameterIn",
        "GoogleCloudChannelV1ParameterOut": "_cloudchannel_187_GoogleCloudChannelV1ParameterOut",
        "GoogleCloudChannelV1alpha1ColumnIn": "_cloudchannel_188_GoogleCloudChannelV1alpha1ColumnIn",
        "GoogleCloudChannelV1alpha1ColumnOut": "_cloudchannel_189_GoogleCloudChannelV1alpha1ColumnOut",
        "GoogleCloudChannelV1ChannelPartnerLinkIn": "_cloudchannel_190_GoogleCloudChannelV1ChannelPartnerLinkIn",
        "GoogleCloudChannelV1ChannelPartnerLinkOut": "_cloudchannel_191_GoogleCloudChannelV1ChannelPartnerLinkOut",
        "GoogleCloudChannelV1StartPaidServiceRequestIn": "_cloudchannel_192_GoogleCloudChannelV1StartPaidServiceRequestIn",
        "GoogleCloudChannelV1StartPaidServiceRequestOut": "_cloudchannel_193_GoogleCloudChannelV1StartPaidServiceRequestOut",
        "GoogleCloudChannelV1ListChannelPartnerLinksResponseIn": "_cloudchannel_194_GoogleCloudChannelV1ListChannelPartnerLinksResponseIn",
        "GoogleCloudChannelV1ListChannelPartnerLinksResponseOut": "_cloudchannel_195_GoogleCloudChannelV1ListChannelPartnerLinksResponseOut",
        "GoogleLongrunningListOperationsResponseIn": "_cloudchannel_196_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_cloudchannel_197_GoogleLongrunningListOperationsResponseOut",
        "GoogleCloudChannelV1RenewalSettingsIn": "_cloudchannel_198_GoogleCloudChannelV1RenewalSettingsIn",
        "GoogleCloudChannelV1RenewalSettingsOut": "_cloudchannel_199_GoogleCloudChannelV1RenewalSettingsOut",
        "GoogleCloudChannelV1alpha1RenewalSettingsIn": "_cloudchannel_200_GoogleCloudChannelV1alpha1RenewalSettingsIn",
        "GoogleCloudChannelV1alpha1RenewalSettingsOut": "_cloudchannel_201_GoogleCloudChannelV1alpha1RenewalSettingsOut",
        "GoogleCloudChannelV1ListCustomersResponseIn": "_cloudchannel_202_GoogleCloudChannelV1ListCustomersResponseIn",
        "GoogleCloudChannelV1ListCustomersResponseOut": "_cloudchannel_203_GoogleCloudChannelV1ListCustomersResponseOut",
        "GoogleCloudChannelV1CustomerConstraintsIn": "_cloudchannel_204_GoogleCloudChannelV1CustomerConstraintsIn",
        "GoogleCloudChannelV1CustomerConstraintsOut": "_cloudchannel_205_GoogleCloudChannelV1CustomerConstraintsOut",
        "GoogleCloudChannelV1ListTransferableSkusRequestIn": "_cloudchannel_206_GoogleCloudChannelV1ListTransferableSkusRequestIn",
        "GoogleCloudChannelV1ListTransferableSkusRequestOut": "_cloudchannel_207_GoogleCloudChannelV1ListTransferableSkusRequestOut",
        "GoogleCloudChannelV1PurchasableOfferIn": "_cloudchannel_208_GoogleCloudChannelV1PurchasableOfferIn",
        "GoogleCloudChannelV1PurchasableOfferOut": "_cloudchannel_209_GoogleCloudChannelV1PurchasableOfferOut",
        "GoogleCloudChannelV1ListEntitlementsResponseIn": "_cloudchannel_210_GoogleCloudChannelV1ListEntitlementsResponseIn",
        "GoogleCloudChannelV1ListEntitlementsResponseOut": "_cloudchannel_211_GoogleCloudChannelV1ListEntitlementsResponseOut",
        "GoogleCloudChannelV1TransferEntitlementsToGoogleRequestIn": "_cloudchannel_212_GoogleCloudChannelV1TransferEntitlementsToGoogleRequestIn",
        "GoogleCloudChannelV1TransferEntitlementsToGoogleRequestOut": "_cloudchannel_213_GoogleCloudChannelV1TransferEntitlementsToGoogleRequestOut",
        "GoogleCloudChannelV1ProductIn": "_cloudchannel_214_GoogleCloudChannelV1ProductIn",
        "GoogleCloudChannelV1ProductOut": "_cloudchannel_215_GoogleCloudChannelV1ProductOut",
        "GoogleCloudChannelV1AdminUserIn": "_cloudchannel_216_GoogleCloudChannelV1AdminUserIn",
        "GoogleCloudChannelV1AdminUserOut": "_cloudchannel_217_GoogleCloudChannelV1AdminUserOut",
        "GoogleCloudChannelV1EntitlementChangeIn": "_cloudchannel_218_GoogleCloudChannelV1EntitlementChangeIn",
        "GoogleCloudChannelV1EntitlementChangeOut": "_cloudchannel_219_GoogleCloudChannelV1EntitlementChangeOut",
        "GoogleCloudChannelV1PeriodIn": "_cloudchannel_220_GoogleCloudChannelV1PeriodIn",
        "GoogleCloudChannelV1PeriodOut": "_cloudchannel_221_GoogleCloudChannelV1PeriodOut",
        "GoogleCloudChannelV1ConditionalOverrideIn": "_cloudchannel_222_GoogleCloudChannelV1ConditionalOverrideIn",
        "GoogleCloudChannelV1ConditionalOverrideOut": "_cloudchannel_223_GoogleCloudChannelV1ConditionalOverrideOut",
        "GoogleCloudChannelV1ListChannelPartnerRepricingConfigsResponseIn": "_cloudchannel_224_GoogleCloudChannelV1ListChannelPartnerRepricingConfigsResponseIn",
        "GoogleCloudChannelV1ListChannelPartnerRepricingConfigsResponseOut": "_cloudchannel_225_GoogleCloudChannelV1ListChannelPartnerRepricingConfigsResponseOut",
        "GoogleTypePostalAddressIn": "_cloudchannel_226_GoogleTypePostalAddressIn",
        "GoogleTypePostalAddressOut": "_cloudchannel_227_GoogleTypePostalAddressOut",
        "GoogleCloudChannelV1ReportJobIn": "_cloudchannel_228_GoogleCloudChannelV1ReportJobIn",
        "GoogleCloudChannelV1ReportJobOut": "_cloudchannel_229_GoogleCloudChannelV1ReportJobOut",
        "GoogleLongrunningOperationIn": "_cloudchannel_230_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_cloudchannel_231_GoogleLongrunningOperationOut",
        "GoogleCloudChannelV1PriceByResourceIn": "_cloudchannel_232_GoogleCloudChannelV1PriceByResourceIn",
        "GoogleCloudChannelV1PriceByResourceOut": "_cloudchannel_233_GoogleCloudChannelV1PriceByResourceOut",
        "GoogleCloudChannelV1ListPurchasableSkusResponseIn": "_cloudchannel_234_GoogleCloudChannelV1ListPurchasableSkusResponseIn",
        "GoogleCloudChannelV1ListPurchasableSkusResponseOut": "_cloudchannel_235_GoogleCloudChannelV1ListPurchasableSkusResponseOut",
        "GoogleCloudChannelV1QueryEligibleBillingAccountsResponseIn": "_cloudchannel_236_GoogleCloudChannelV1QueryEligibleBillingAccountsResponseIn",
        "GoogleCloudChannelV1QueryEligibleBillingAccountsResponseOut": "_cloudchannel_237_GoogleCloudChannelV1QueryEligibleBillingAccountsResponseOut",
        "GoogleCloudChannelV1RepricingConfigChannelPartnerGranularityIn": "_cloudchannel_238_GoogleCloudChannelV1RepricingConfigChannelPartnerGranularityIn",
        "GoogleCloudChannelV1RepricingConfigChannelPartnerGranularityOut": "_cloudchannel_239_GoogleCloudChannelV1RepricingConfigChannelPartnerGranularityOut",
        "GoogleCloudChannelV1ReportValueIn": "_cloudchannel_240_GoogleCloudChannelV1ReportValueIn",
        "GoogleCloudChannelV1ReportValueOut": "_cloudchannel_241_GoogleCloudChannelV1ReportValueOut",
        "GoogleCloudChannelV1ListTransferableOffersRequestIn": "_cloudchannel_242_GoogleCloudChannelV1ListTransferableOffersRequestIn",
        "GoogleCloudChannelV1ListTransferableOffersRequestOut": "_cloudchannel_243_GoogleCloudChannelV1ListTransferableOffersRequestOut",
        "GoogleCloudChannelV1ListEntitlementChangesResponseIn": "_cloudchannel_244_GoogleCloudChannelV1ListEntitlementChangesResponseIn",
        "GoogleCloudChannelV1ListEntitlementChangesResponseOut": "_cloudchannel_245_GoogleCloudChannelV1ListEntitlementChangesResponseOut",
        "GoogleCloudChannelV1alpha1ProvisionedServiceIn": "_cloudchannel_246_GoogleCloudChannelV1alpha1ProvisionedServiceIn",
        "GoogleCloudChannelV1alpha1ProvisionedServiceOut": "_cloudchannel_247_GoogleCloudChannelV1alpha1ProvisionedServiceOut",
        "GoogleCloudChannelV1TrialSettingsIn": "_cloudchannel_248_GoogleCloudChannelV1TrialSettingsIn",
        "GoogleCloudChannelV1TrialSettingsOut": "_cloudchannel_249_GoogleCloudChannelV1TrialSettingsOut",
        "GoogleCloudChannelV1EntitlementEventIn": "_cloudchannel_250_GoogleCloudChannelV1EntitlementEventIn",
        "GoogleCloudChannelV1EntitlementEventOut": "_cloudchannel_251_GoogleCloudChannelV1EntitlementEventOut",
        "GoogleCloudChannelV1CancelEntitlementRequestIn": "_cloudchannel_252_GoogleCloudChannelV1CancelEntitlementRequestIn",
        "GoogleCloudChannelV1CancelEntitlementRequestOut": "_cloudchannel_253_GoogleCloudChannelV1CancelEntitlementRequestOut",
        "GoogleTypeDecimalIn": "_cloudchannel_254_GoogleTypeDecimalIn",
        "GoogleTypeDecimalOut": "_cloudchannel_255_GoogleTypeDecimalOut",
        "GoogleCloudChannelV1ParameterDefinitionIn": "_cloudchannel_256_GoogleCloudChannelV1ParameterDefinitionIn",
        "GoogleCloudChannelV1ParameterDefinitionOut": "_cloudchannel_257_GoogleCloudChannelV1ParameterDefinitionOut",
        "GoogleCloudChannelV1ProvisionedServiceIn": "_cloudchannel_258_GoogleCloudChannelV1ProvisionedServiceIn",
        "GoogleCloudChannelV1ProvisionedServiceOut": "_cloudchannel_259_GoogleCloudChannelV1ProvisionedServiceOut",
        "GoogleCloudChannelV1EduDataIn": "_cloudchannel_260_GoogleCloudChannelV1EduDataIn",
        "GoogleCloudChannelV1EduDataOut": "_cloudchannel_261_GoogleCloudChannelV1EduDataOut",
        "GoogleCloudChannelV1SkuPurchaseGroupIn": "_cloudchannel_262_GoogleCloudChannelV1SkuPurchaseGroupIn",
        "GoogleCloudChannelV1SkuPurchaseGroupOut": "_cloudchannel_263_GoogleCloudChannelV1SkuPurchaseGroupOut",
        "GoogleCloudChannelV1alpha1ChannelPartnerEventIn": "_cloudchannel_264_GoogleCloudChannelV1alpha1ChannelPartnerEventIn",
        "GoogleCloudChannelV1alpha1ChannelPartnerEventOut": "_cloudchannel_265_GoogleCloudChannelV1alpha1ChannelPartnerEventOut",
        "GoogleCloudChannelV1CloudIdentityCustomerAccountIn": "_cloudchannel_266_GoogleCloudChannelV1CloudIdentityCustomerAccountIn",
        "GoogleCloudChannelV1CloudIdentityCustomerAccountOut": "_cloudchannel_267_GoogleCloudChannelV1CloudIdentityCustomerAccountOut",
        "GoogleCloudChannelV1alpha1TransferEntitlementsResponseIn": "_cloudchannel_268_GoogleCloudChannelV1alpha1TransferEntitlementsResponseIn",
        "GoogleCloudChannelV1alpha1TransferEntitlementsResponseOut": "_cloudchannel_269_GoogleCloudChannelV1alpha1TransferEntitlementsResponseOut",
        "GoogleTypeDateTimeIn": "_cloudchannel_270_GoogleTypeDateTimeIn",
        "GoogleTypeDateTimeOut": "_cloudchannel_271_GoogleTypeDateTimeOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleLongrunningCancelOperationRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestIn"])
    types["GoogleLongrunningCancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestOut"])
    types["GoogleCloudChannelV1alpha1AssociationInfoIn"] = t.struct(
        {"baseEntitlement": t.string().optional()}
    ).named(renames["GoogleCloudChannelV1alpha1AssociationInfoIn"])
    types["GoogleCloudChannelV1alpha1AssociationInfoOut"] = t.struct(
        {
            "baseEntitlement": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1alpha1AssociationInfoOut"])
    types["GoogleCloudChannelV1ChangeOfferRequestIn"] = t.struct(
        {
            "parameters": t.array(
                t.proxy(renames["GoogleCloudChannelV1ParameterIn"])
            ).optional(),
            "offer": t.string(),
            "purchaseOrderId": t.string().optional(),
            "requestId": t.string().optional(),
        }
    ).named(renames["GoogleCloudChannelV1ChangeOfferRequestIn"])
    types["GoogleCloudChannelV1ChangeOfferRequestOut"] = t.struct(
        {
            "parameters": t.array(
                t.proxy(renames["GoogleCloudChannelV1ParameterOut"])
            ).optional(),
            "offer": t.string(),
            "purchaseOrderId": t.string().optional(),
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1ChangeOfferRequestOut"])
    types["GoogleTypeMoneyIn"] = t.struct(
        {
            "currencyCode": t.string().optional(),
            "nanos": t.integer().optional(),
            "units": t.string().optional(),
        }
    ).named(renames["GoogleTypeMoneyIn"])
    types["GoogleTypeMoneyOut"] = t.struct(
        {
            "currencyCode": t.string().optional(),
            "nanos": t.integer().optional(),
            "units": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeMoneyOut"])
    types["GoogleCloudChannelV1SkuIn"] = t.struct(
        {
            "product": t.proxy(renames["GoogleCloudChannelV1ProductIn"]).optional(),
            "marketingInfo": t.proxy(
                renames["GoogleCloudChannelV1MarketingInfoIn"]
            ).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudChannelV1SkuIn"])
    types["GoogleCloudChannelV1SkuOut"] = t.struct(
        {
            "product": t.proxy(renames["GoogleCloudChannelV1ProductOut"]).optional(),
            "marketingInfo": t.proxy(
                renames["GoogleCloudChannelV1MarketingInfoOut"]
            ).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1SkuOut"])
    types["GoogleCloudChannelV1ListOffersResponseIn"] = t.struct(
        {
            "offers": t.array(
                t.proxy(renames["GoogleCloudChannelV1OfferIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudChannelV1ListOffersResponseIn"])
    types["GoogleCloudChannelV1ListOffersResponseOut"] = t.struct(
        {
            "offers": t.array(
                t.proxy(renames["GoogleCloudChannelV1OfferOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1ListOffersResponseOut"])
    types["GoogleCloudChannelV1CreateEntitlementRequestIn"] = t.struct(
        {
            "requestId": t.string().optional(),
            "entitlement": t.proxy(renames["GoogleCloudChannelV1EntitlementIn"]),
        }
    ).named(renames["GoogleCloudChannelV1CreateEntitlementRequestIn"])
    types["GoogleCloudChannelV1CreateEntitlementRequestOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "entitlement": t.proxy(renames["GoogleCloudChannelV1EntitlementOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1CreateEntitlementRequestOut"])
    types["GoogleCloudChannelV1RegisterSubscriberRequestIn"] = t.struct(
        {"serviceAccount": t.string()}
    ).named(renames["GoogleCloudChannelV1RegisterSubscriberRequestIn"])
    types["GoogleCloudChannelV1RegisterSubscriberRequestOut"] = t.struct(
        {
            "serviceAccount": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1RegisterSubscriberRequestOut"])
    types["GoogleCloudChannelV1CommitmentSettingsIn"] = t.struct(
        {
            "renewalSettings": t.proxy(
                renames["GoogleCloudChannelV1RenewalSettingsIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudChannelV1CommitmentSettingsIn"])
    types["GoogleCloudChannelV1CommitmentSettingsOut"] = t.struct(
        {
            "renewalSettings": t.proxy(
                renames["GoogleCloudChannelV1RenewalSettingsOut"]
            ).optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1CommitmentSettingsOut"])
    types["GoogleCloudChannelV1PlanIn"] = t.struct(
        {
            "billingAccount": t.string().optional(),
            "paymentCycle": t.proxy(renames["GoogleCloudChannelV1PeriodIn"]).optional(),
            "trialPeriod": t.proxy(renames["GoogleCloudChannelV1PeriodIn"]).optional(),
            "paymentPlan": t.string().optional(),
            "paymentType": t.string().optional(),
        }
    ).named(renames["GoogleCloudChannelV1PlanIn"])
    types["GoogleCloudChannelV1PlanOut"] = t.struct(
        {
            "billingAccount": t.string().optional(),
            "paymentCycle": t.proxy(
                renames["GoogleCloudChannelV1PeriodOut"]
            ).optional(),
            "trialPeriod": t.proxy(renames["GoogleCloudChannelV1PeriodOut"]).optional(),
            "paymentPlan": t.string().optional(),
            "paymentType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1PlanOut"])
    types["GoogleCloudChannelV1alpha1SubscriberEventIn"] = t.struct(
        {
            "entitlementEvent": t.proxy(
                renames["GoogleCloudChannelV1alpha1EntitlementEventIn"]
            ).optional(),
            "customerEvent": t.proxy(
                renames["GoogleCloudChannelV1alpha1CustomerEventIn"]
            ).optional(),
            "channelPartnerEvent": t.proxy(
                renames["GoogleCloudChannelV1alpha1ChannelPartnerEventIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudChannelV1alpha1SubscriberEventIn"])
    types["GoogleCloudChannelV1alpha1SubscriberEventOut"] = t.struct(
        {
            "entitlementEvent": t.proxy(
                renames["GoogleCloudChannelV1alpha1EntitlementEventOut"]
            ).optional(),
            "customerEvent": t.proxy(
                renames["GoogleCloudChannelV1alpha1CustomerEventOut"]
            ).optional(),
            "channelPartnerEvent": t.proxy(
                renames["GoogleCloudChannelV1alpha1ChannelPartnerEventOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1alpha1SubscriberEventOut"])
    types["GoogleCloudChannelV1ListProductsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "products": t.array(
                t.proxy(renames["GoogleCloudChannelV1ProductIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudChannelV1ListProductsResponseIn"])
    types["GoogleCloudChannelV1ListProductsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "products": t.array(
                t.proxy(renames["GoogleCloudChannelV1ProductOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1ListProductsResponseOut"])
    types["GoogleCloudChannelV1alpha1CommitmentSettingsIn"] = t.struct(
        {
            "renewalSettings": t.proxy(
                renames["GoogleCloudChannelV1alpha1RenewalSettingsIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudChannelV1alpha1CommitmentSettingsIn"])
    types["GoogleCloudChannelV1alpha1CommitmentSettingsOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "renewalSettings": t.proxy(
                renames["GoogleCloudChannelV1alpha1RenewalSettingsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1alpha1CommitmentSettingsOut"])
    types["GoogleCloudChannelV1MediaIn"] = t.struct(
        {
            "type": t.string().optional(),
            "title": t.string().optional(),
            "content": t.string().optional(),
        }
    ).named(renames["GoogleCloudChannelV1MediaIn"])
    types["GoogleCloudChannelV1MediaOut"] = t.struct(
        {
            "type": t.string().optional(),
            "title": t.string().optional(),
            "content": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1MediaOut"])
    types["GoogleCloudChannelV1CustomerIn"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "orgPostalAddress": t.proxy(renames["GoogleTypePostalAddressIn"]),
            "alternateEmail": t.string().optional(),
            "channelPartnerId": t.string().optional(),
            "domain": t.string(),
            "orgDisplayName": t.string(),
            "correlationId": t.string().optional(),
            "primaryContactInfo": t.proxy(
                renames["GoogleCloudChannelV1ContactInfoIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudChannelV1CustomerIn"])
    types["GoogleCloudChannelV1CustomerOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "orgPostalAddress": t.proxy(renames["GoogleTypePostalAddressOut"]),
            "alternateEmail": t.string().optional(),
            "channelPartnerId": t.string().optional(),
            "updateTime": t.string().optional(),
            "domain": t.string(),
            "cloudIdentityId": t.string().optional(),
            "orgDisplayName": t.string(),
            "correlationId": t.string().optional(),
            "name": t.string().optional(),
            "primaryContactInfo": t.proxy(
                renames["GoogleCloudChannelV1ContactInfoOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "cloudIdentityInfo": t.proxy(
                renames["GoogleCloudChannelV1CloudIdentityInfoOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1CustomerOut"])
    types["GoogleCloudChannelV1TransferableSkuIn"] = t.struct(
        {
            "legacySku": t.proxy(renames["GoogleCloudChannelV1SkuIn"]).optional(),
            "transferEligibility": t.proxy(
                renames["GoogleCloudChannelV1TransferEligibilityIn"]
            ).optional(),
            "sku": t.proxy(renames["GoogleCloudChannelV1SkuIn"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1TransferableSkuIn"])
    types["GoogleCloudChannelV1TransferableSkuOut"] = t.struct(
        {
            "legacySku": t.proxy(renames["GoogleCloudChannelV1SkuOut"]).optional(),
            "transferEligibility": t.proxy(
                renames["GoogleCloudChannelV1TransferEligibilityOut"]
            ).optional(),
            "sku": t.proxy(renames["GoogleCloudChannelV1SkuOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1TransferableSkuOut"])
    types["GoogleCloudChannelV1FetchReportResultsResponseIn"] = t.struct(
        {
            "rows": t.array(t.proxy(renames["GoogleCloudChannelV1RowIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "reportMetadata": t.proxy(
                renames["GoogleCloudChannelV1ReportResultsMetadataIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudChannelV1FetchReportResultsResponseIn"])
    types["GoogleCloudChannelV1FetchReportResultsResponseOut"] = t.struct(
        {
            "rows": t.array(t.proxy(renames["GoogleCloudChannelV1RowOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "reportMetadata": t.proxy(
                renames["GoogleCloudChannelV1ReportResultsMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1FetchReportResultsResponseOut"])
    types["GoogleCloudChannelV1alpha1RunReportJobResponseIn"] = t.struct(
        {
            "reportJob": t.proxy(
                renames["GoogleCloudChannelV1alpha1ReportJobIn"]
            ).optional(),
            "reportMetadata": t.proxy(
                renames["GoogleCloudChannelV1alpha1ReportResultsMetadataIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudChannelV1alpha1RunReportJobResponseIn"])
    types["GoogleCloudChannelV1alpha1RunReportJobResponseOut"] = t.struct(
        {
            "reportJob": t.proxy(
                renames["GoogleCloudChannelV1alpha1ReportJobOut"]
            ).optional(),
            "reportMetadata": t.proxy(
                renames["GoogleCloudChannelV1alpha1ReportResultsMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1alpha1RunReportJobResponseOut"])
    types["GoogleCloudChannelV1TransferEligibilityIn"] = t.struct(
        {
            "description": t.string().optional(),
            "isEligible": t.boolean().optional(),
            "ineligibilityReason": t.string().optional(),
        }
    ).named(renames["GoogleCloudChannelV1TransferEligibilityIn"])
    types["GoogleCloudChannelV1TransferEligibilityOut"] = t.struct(
        {
            "description": t.string().optional(),
            "isEligible": t.boolean().optional(),
            "ineligibilityReason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1TransferEligibilityOut"])
    types["GoogleCloudChannelV1PricePhaseIn"] = t.struct(
        {
            "firstPeriod": t.integer().optional(),
            "lastPeriod": t.integer().optional(),
            "periodType": t.string().optional(),
            "price": t.proxy(renames["GoogleCloudChannelV1PriceIn"]).optional(),
            "priceTiers": t.array(
                t.proxy(renames["GoogleCloudChannelV1PriceTierIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudChannelV1PricePhaseIn"])
    types["GoogleCloudChannelV1PricePhaseOut"] = t.struct(
        {
            "firstPeriod": t.integer().optional(),
            "lastPeriod": t.integer().optional(),
            "periodType": t.string().optional(),
            "price": t.proxy(renames["GoogleCloudChannelV1PriceOut"]).optional(),
            "priceTiers": t.array(
                t.proxy(renames["GoogleCloudChannelV1PriceTierOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1PricePhaseOut"])
    types["GoogleCloudChannelV1RepricingAdjustmentIn"] = t.struct(
        {
            "percentageAdjustment": t.proxy(
                renames["GoogleCloudChannelV1PercentageAdjustmentIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudChannelV1RepricingAdjustmentIn"])
    types["GoogleCloudChannelV1RepricingAdjustmentOut"] = t.struct(
        {
            "percentageAdjustment": t.proxy(
                renames["GoogleCloudChannelV1PercentageAdjustmentOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1RepricingAdjustmentOut"])
    types["GoogleCloudChannelV1ValueIn"] = t.struct(
        {
            "int64Value": t.string().optional(),
            "stringValue": t.string().optional(),
            "doubleValue": t.number().optional(),
            "boolValue": t.boolean().optional(),
            "protoValue": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudChannelV1ValueIn"])
    types["GoogleCloudChannelV1ValueOut"] = t.struct(
        {
            "int64Value": t.string().optional(),
            "stringValue": t.string().optional(),
            "doubleValue": t.number().optional(),
            "boolValue": t.boolean().optional(),
            "protoValue": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1ValueOut"])
    types["GoogleCloudChannelV1DateRangeIn"] = t.struct(
        {
            "invoiceStartDate": t.proxy(renames["GoogleTypeDateIn"]).optional(),
            "invoiceEndDate": t.proxy(renames["GoogleTypeDateIn"]).optional(),
            "usageStartDateTime": t.proxy(renames["GoogleTypeDateTimeIn"]).optional(),
            "usageEndDateTime": t.proxy(renames["GoogleTypeDateTimeIn"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1DateRangeIn"])
    types["GoogleCloudChannelV1DateRangeOut"] = t.struct(
        {
            "invoiceStartDate": t.proxy(renames["GoogleTypeDateOut"]).optional(),
            "invoiceEndDate": t.proxy(renames["GoogleTypeDateOut"]).optional(),
            "usageStartDateTime": t.proxy(renames["GoogleTypeDateTimeOut"]).optional(),
            "usageEndDateTime": t.proxy(renames["GoogleTypeDateTimeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1DateRangeOut"])
    types["GoogleCloudChannelV1CustomerRepricingConfigIn"] = t.struct(
        {"repricingConfig": t.proxy(renames["GoogleCloudChannelV1RepricingConfigIn"])}
    ).named(renames["GoogleCloudChannelV1CustomerRepricingConfigIn"])
    types["GoogleCloudChannelV1CustomerRepricingConfigOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "repricingConfig": t.proxy(
                renames["GoogleCloudChannelV1RepricingConfigOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1CustomerRepricingConfigOut"])
    types["GoogleCloudChannelV1SkuGroupConditionIn"] = t.struct(
        {"skuGroup": t.string().optional()}
    ).named(renames["GoogleCloudChannelV1SkuGroupConditionIn"])
    types["GoogleCloudChannelV1SkuGroupConditionOut"] = t.struct(
        {
            "skuGroup": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1SkuGroupConditionOut"])
    types["GoogleCloudChannelV1ColumnIn"] = t.struct(
        {
            "columnId": t.string().optional(),
            "dataType": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["GoogleCloudChannelV1ColumnIn"])
    types["GoogleCloudChannelV1ColumnOut"] = t.struct(
        {
            "columnId": t.string().optional(),
            "dataType": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1ColumnOut"])
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
    types["GoogleCloudChannelV1RowIn"] = t.struct(
        {
            "partitionKey": t.string().optional(),
            "values": t.array(
                t.proxy(renames["GoogleCloudChannelV1ReportValueIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudChannelV1RowIn"])
    types["GoogleCloudChannelV1RowOut"] = t.struct(
        {
            "partitionKey": t.string().optional(),
            "values": t.array(
                t.proxy(renames["GoogleCloudChannelV1ReportValueOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1RowOut"])
    types["GoogleCloudChannelV1ImportCustomerRequestIn"] = t.struct(
        {
            "channelPartnerId": t.string().optional(),
            "authToken": t.string().optional(),
            "cloudIdentityId": t.string(),
            "domain": t.string(),
            "customer": t.string().optional(),
            "overwriteIfExists": t.boolean(),
        }
    ).named(renames["GoogleCloudChannelV1ImportCustomerRequestIn"])
    types["GoogleCloudChannelV1ImportCustomerRequestOut"] = t.struct(
        {
            "channelPartnerId": t.string().optional(),
            "authToken": t.string().optional(),
            "cloudIdentityId": t.string(),
            "domain": t.string(),
            "customer": t.string().optional(),
            "overwriteIfExists": t.boolean(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1ImportCustomerRequestOut"])
    types["GoogleCloudChannelV1RepricingConditionIn"] = t.struct(
        {
            "skuGroupCondition": t.proxy(
                renames["GoogleCloudChannelV1SkuGroupConditionIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudChannelV1RepricingConditionIn"])
    types["GoogleCloudChannelV1RepricingConditionOut"] = t.struct(
        {
            "skuGroupCondition": t.proxy(
                renames["GoogleCloudChannelV1SkuGroupConditionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1RepricingConditionOut"])
    types["GoogleCloudChannelV1UnregisterSubscriberResponseIn"] = t.struct(
        {"topic": t.string().optional()}
    ).named(renames["GoogleCloudChannelV1UnregisterSubscriberResponseIn"])
    types["GoogleCloudChannelV1UnregisterSubscriberResponseOut"] = t.struct(
        {
            "topic": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1UnregisterSubscriberResponseOut"])
    types["GoogleCloudChannelV1TransferEntitlementsResponseIn"] = t.struct(
        {
            "entitlements": t.array(
                t.proxy(renames["GoogleCloudChannelV1EntitlementIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudChannelV1TransferEntitlementsResponseIn"])
    types["GoogleCloudChannelV1TransferEntitlementsResponseOut"] = t.struct(
        {
            "entitlements": t.array(
                t.proxy(renames["GoogleCloudChannelV1EntitlementOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1TransferEntitlementsResponseOut"])
    types["GoogleCloudChannelV1ListSkusResponseIn"] = t.struct(
        {
            "skus": t.array(t.proxy(renames["GoogleCloudChannelV1SkuIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudChannelV1ListSkusResponseIn"])
    types["GoogleCloudChannelV1ListSkusResponseOut"] = t.struct(
        {
            "skus": t.array(t.proxy(renames["GoogleCloudChannelV1SkuOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1ListSkusResponseOut"])
    types["GoogleCloudChannelV1alpha1ReportIn"] = t.struct(
        {
            "name": t.string(),
            "description": t.string().optional(),
            "columns": t.array(
                t.proxy(renames["GoogleCloudChannelV1alpha1ColumnIn"])
            ).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["GoogleCloudChannelV1alpha1ReportIn"])
    types["GoogleCloudChannelV1alpha1ReportOut"] = t.struct(
        {
            "name": t.string(),
            "description": t.string().optional(),
            "columns": t.array(
                t.proxy(renames["GoogleCloudChannelV1alpha1ColumnOut"])
            ).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1alpha1ReportOut"])
    types["GoogleCloudChannelV1PercentageAdjustmentIn"] = t.struct(
        {"percentage": t.proxy(renames["GoogleTypeDecimalIn"]).optional()}
    ).named(renames["GoogleCloudChannelV1PercentageAdjustmentIn"])
    types["GoogleCloudChannelV1PercentageAdjustmentOut"] = t.struct(
        {
            "percentage": t.proxy(renames["GoogleTypeDecimalOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1PercentageAdjustmentOut"])
    types["GoogleCloudChannelV1TransferableOfferIn"] = t.struct(
        {"offer": t.proxy(renames["GoogleCloudChannelV1OfferIn"]).optional()}
    ).named(renames["GoogleCloudChannelV1TransferableOfferIn"])
    types["GoogleCloudChannelV1TransferableOfferOut"] = t.struct(
        {
            "offer": t.proxy(renames["GoogleCloudChannelV1OfferOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1TransferableOfferOut"])
    types["GoogleCloudChannelV1ListTransferableSkusResponseIn"] = t.struct(
        {
            "transferableSkus": t.array(
                t.proxy(renames["GoogleCloudChannelV1TransferableSkuIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudChannelV1ListTransferableSkusResponseIn"])
    types["GoogleCloudChannelV1ListTransferableSkusResponseOut"] = t.struct(
        {
            "transferableSkus": t.array(
                t.proxy(renames["GoogleCloudChannelV1TransferableSkuOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1ListTransferableSkusResponseOut"])
    types["GoogleCloudChannelV1CheckCloudIdentityAccountsExistRequestIn"] = t.struct(
        {"domain": t.string()}
    ).named(renames["GoogleCloudChannelV1CheckCloudIdentityAccountsExistRequestIn"])
    types["GoogleCloudChannelV1CheckCloudIdentityAccountsExistRequestOut"] = t.struct(
        {"domain": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudChannelV1CheckCloudIdentityAccountsExistRequestOut"])
    types["GoogleCloudChannelV1EntitlementIn"] = t.struct(
        {
            "billingAccount": t.string().optional(),
            "parameters": t.array(
                t.proxy(renames["GoogleCloudChannelV1ParameterIn"])
            ).optional(),
            "purchaseOrderId": t.string().optional(),
            "associationInfo": t.proxy(
                renames["GoogleCloudChannelV1AssociationInfoIn"]
            ).optional(),
            "offer": t.string(),
            "commitmentSettings": t.proxy(
                renames["GoogleCloudChannelV1CommitmentSettingsIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudChannelV1EntitlementIn"])
    types["GoogleCloudChannelV1EntitlementOut"] = t.struct(
        {
            "billingAccount": t.string().optional(),
            "trialSettings": t.proxy(
                renames["GoogleCloudChannelV1TrialSettingsOut"]
            ).optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "parameters": t.array(
                t.proxy(renames["GoogleCloudChannelV1ParameterOut"])
            ).optional(),
            "purchaseOrderId": t.string().optional(),
            "suspensionReasons": t.array(t.string()).optional(),
            "provisionedService": t.proxy(
                renames["GoogleCloudChannelV1ProvisionedServiceOut"]
            ).optional(),
            "provisioningState": t.string().optional(),
            "updateTime": t.string().optional(),
            "associationInfo": t.proxy(
                renames["GoogleCloudChannelV1AssociationInfoOut"]
            ).optional(),
            "offer": t.string(),
            "commitmentSettings": t.proxy(
                renames["GoogleCloudChannelV1CommitmentSettingsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1EntitlementOut"])
    types["GoogleCloudChannelV1ListSubscribersResponseIn"] = t.struct(
        {
            "serviceAccounts": t.array(t.string()).optional(),
            "topic": t.string().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudChannelV1ListSubscribersResponseIn"])
    types["GoogleCloudChannelV1ListSubscribersResponseOut"] = t.struct(
        {
            "serviceAccounts": t.array(t.string()).optional(),
            "topic": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1ListSubscribersResponseOut"])
    types["GoogleCloudChannelV1TransferEntitlementsRequestIn"] = t.struct(
        {
            "authToken": t.string().optional(),
            "requestId": t.string().optional(),
            "entitlements": t.array(
                t.proxy(renames["GoogleCloudChannelV1EntitlementIn"])
            ),
        }
    ).named(renames["GoogleCloudChannelV1TransferEntitlementsRequestIn"])
    types["GoogleCloudChannelV1TransferEntitlementsRequestOut"] = t.struct(
        {
            "authToken": t.string().optional(),
            "requestId": t.string().optional(),
            "entitlements": t.array(
                t.proxy(renames["GoogleCloudChannelV1EntitlementOut"])
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1TransferEntitlementsRequestOut"])
    types["GoogleCloudChannelV1RunReportJobResponseIn"] = t.struct(
        {
            "reportJob": t.proxy(renames["GoogleCloudChannelV1ReportJobIn"]).optional(),
            "reportMetadata": t.proxy(
                renames["GoogleCloudChannelV1ReportResultsMetadataIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudChannelV1RunReportJobResponseIn"])
    types["GoogleCloudChannelV1RunReportJobResponseOut"] = t.struct(
        {
            "reportJob": t.proxy(
                renames["GoogleCloudChannelV1ReportJobOut"]
            ).optional(),
            "reportMetadata": t.proxy(
                renames["GoogleCloudChannelV1ReportResultsMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1RunReportJobResponseOut"])
    types["GoogleCloudChannelV1CustomerEventIn"] = t.struct(
        {"eventType": t.string().optional(), "customer": t.string().optional()}
    ).named(renames["GoogleCloudChannelV1CustomerEventIn"])
    types["GoogleCloudChannelV1CustomerEventOut"] = t.struct(
        {
            "eventType": t.string().optional(),
            "customer": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1CustomerEventOut"])
    types["GoogleCloudChannelV1PriceIn"] = t.struct(
        {
            "externalPriceUri": t.string().optional(),
            "discount": t.number().optional(),
            "effectivePrice": t.proxy(renames["GoogleTypeMoneyIn"]).optional(),
            "basePrice": t.proxy(renames["GoogleTypeMoneyIn"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1PriceIn"])
    types["GoogleCloudChannelV1PriceOut"] = t.struct(
        {
            "externalPriceUri": t.string().optional(),
            "discount": t.number().optional(),
            "effectivePrice": t.proxy(renames["GoogleTypeMoneyOut"]).optional(),
            "basePrice": t.proxy(renames["GoogleTypeMoneyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1PriceOut"])
    types["GoogleCloudChannelV1CheckCloudIdentityAccountsExistResponseIn"] = t.struct(
        {
            "cloudIdentityAccounts": t.array(
                t.proxy(renames["GoogleCloudChannelV1CloudIdentityCustomerAccountIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudChannelV1CheckCloudIdentityAccountsExistResponseIn"])
    types["GoogleCloudChannelV1CheckCloudIdentityAccountsExistResponseOut"] = t.struct(
        {
            "cloudIdentityAccounts": t.array(
                t.proxy(renames["GoogleCloudChannelV1CloudIdentityCustomerAccountOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1CheckCloudIdentityAccountsExistResponseOut"])
    types["GoogleCloudChannelV1RegisterSubscriberResponseIn"] = t.struct(
        {"topic": t.string().optional()}
    ).named(renames["GoogleCloudChannelV1RegisterSubscriberResponseIn"])
    types["GoogleCloudChannelV1RegisterSubscriberResponseOut"] = t.struct(
        {
            "topic": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1RegisterSubscriberResponseOut"])
    types["GoogleCloudChannelV1ListCustomerRepricingConfigsResponseIn"] = t.struct(
        {
            "customerRepricingConfigs": t.array(
                t.proxy(renames["GoogleCloudChannelV1CustomerRepricingConfigIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudChannelV1ListCustomerRepricingConfigsResponseIn"])
    types["GoogleCloudChannelV1ListCustomerRepricingConfigsResponseOut"] = t.struct(
        {
            "customerRepricingConfigs": t.array(
                t.proxy(renames["GoogleCloudChannelV1CustomerRepricingConfigOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1ListCustomerRepricingConfigsResponseOut"])
    types["GoogleCloudChannelV1alpha1DateRangeIn"] = t.struct(
        {
            "usageStartDateTime": t.proxy(renames["GoogleTypeDateTimeIn"]).optional(),
            "usageEndDateTime": t.proxy(renames["GoogleTypeDateTimeIn"]).optional(),
            "invoiceStartDate": t.proxy(renames["GoogleTypeDateIn"]).optional(),
            "invoiceEndDate": t.proxy(renames["GoogleTypeDateIn"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1alpha1DateRangeIn"])
    types["GoogleCloudChannelV1alpha1DateRangeOut"] = t.struct(
        {
            "usageStartDateTime": t.proxy(renames["GoogleTypeDateTimeOut"]).optional(),
            "usageEndDateTime": t.proxy(renames["GoogleTypeDateTimeOut"]).optional(),
            "invoiceStartDate": t.proxy(renames["GoogleTypeDateOut"]).optional(),
            "invoiceEndDate": t.proxy(renames["GoogleTypeDateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1alpha1DateRangeOut"])
    types["GoogleCloudChannelV1alpha1ReportStatusIn"] = t.struct(
        {
            "startTime": t.string().optional(),
            "state": t.string().optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudChannelV1alpha1ReportStatusIn"])
    types["GoogleCloudChannelV1alpha1ReportStatusOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "state": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1alpha1ReportStatusOut"])
    types["GoogleCloudChannelV1alpha1ReportJobIn"] = t.struct(
        {
            "name": t.string(),
            "reportStatus": t.proxy(
                renames["GoogleCloudChannelV1alpha1ReportStatusIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudChannelV1alpha1ReportJobIn"])
    types["GoogleCloudChannelV1alpha1ReportJobOut"] = t.struct(
        {
            "name": t.string(),
            "reportStatus": t.proxy(
                renames["GoogleCloudChannelV1alpha1ReportStatusOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1alpha1ReportJobOut"])
    types["GoogleCloudChannelV1OfferIn"] = t.struct(
        {
            "startTime": t.string().optional(),
            "priceByResources": t.array(
                t.proxy(renames["GoogleCloudChannelV1PriceByResourceIn"])
            ).optional(),
            "marketingInfo": t.proxy(
                renames["GoogleCloudChannelV1MarketingInfoIn"]
            ).optional(),
            "plan": t.proxy(renames["GoogleCloudChannelV1PlanIn"]).optional(),
            "name": t.string().optional(),
            "dealCode": t.string().optional(),
            "constraints": t.proxy(
                renames["GoogleCloudChannelV1ConstraintsIn"]
            ).optional(),
            "parameterDefinitions": t.array(
                t.proxy(renames["GoogleCloudChannelV1ParameterDefinitionIn"])
            ).optional(),
            "sku": t.proxy(renames["GoogleCloudChannelV1SkuIn"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1OfferIn"])
    types["GoogleCloudChannelV1OfferOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "priceByResources": t.array(
                t.proxy(renames["GoogleCloudChannelV1PriceByResourceOut"])
            ).optional(),
            "marketingInfo": t.proxy(
                renames["GoogleCloudChannelV1MarketingInfoOut"]
            ).optional(),
            "plan": t.proxy(renames["GoogleCloudChannelV1PlanOut"]).optional(),
            "name": t.string().optional(),
            "endTime": t.string().optional(),
            "dealCode": t.string().optional(),
            "constraints": t.proxy(
                renames["GoogleCloudChannelV1ConstraintsOut"]
            ).optional(),
            "parameterDefinitions": t.array(
                t.proxy(renames["GoogleCloudChannelV1ParameterDefinitionOut"])
            ).optional(),
            "sku": t.proxy(renames["GoogleCloudChannelV1SkuOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1OfferOut"])
    types["GoogleCloudChannelV1alpha1EntitlementIn"] = t.struct(
        {
            "channelPartnerId": t.string().optional(),
            "parameters": t.array(
                t.proxy(renames["GoogleCloudChannelV1alpha1ParameterIn"])
            ).optional(),
            "commitmentSettings": t.proxy(
                renames["GoogleCloudChannelV1alpha1CommitmentSettingsIn"]
            ).optional(),
            "assignedUnits": t.integer().optional(),
            "billingAccount": t.string().optional(),
            "offer": t.string(),
            "associationInfo": t.proxy(
                renames["GoogleCloudChannelV1alpha1AssociationInfoIn"]
            ).optional(),
            "maxUnits": t.integer().optional(),
            "purchaseOrderId": t.string().optional(),
            "numUnits": t.integer().optional(),
        }
    ).named(renames["GoogleCloudChannelV1alpha1EntitlementIn"])
    types["GoogleCloudChannelV1alpha1EntitlementOut"] = t.struct(
        {
            "channelPartnerId": t.string().optional(),
            "provisioningState": t.string().optional(),
            "provisionedService": t.proxy(
                renames["GoogleCloudChannelV1alpha1ProvisionedServiceOut"]
            ).optional(),
            "parameters": t.array(
                t.proxy(renames["GoogleCloudChannelV1alpha1ParameterOut"])
            ).optional(),
            "createTime": t.string().optional(),
            "commitmentSettings": t.proxy(
                renames["GoogleCloudChannelV1alpha1CommitmentSettingsOut"]
            ).optional(),
            "suspensionReasons": t.array(t.string()).optional(),
            "assignedUnits": t.integer().optional(),
            "billingAccount": t.string().optional(),
            "updateTime": t.string().optional(),
            "offer": t.string(),
            "associationInfo": t.proxy(
                renames["GoogleCloudChannelV1alpha1AssociationInfoOut"]
            ).optional(),
            "name": t.string().optional(),
            "trialSettings": t.proxy(
                renames["GoogleCloudChannelV1alpha1TrialSettingsOut"]
            ).optional(),
            "maxUnits": t.integer().optional(),
            "purchaseOrderId": t.string().optional(),
            "numUnits": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1alpha1EntitlementOut"])
    types["GoogleTypeDateIn"] = t.struct(
        {
            "month": t.integer().optional(),
            "year": t.integer().optional(),
            "day": t.integer().optional(),
        }
    ).named(renames["GoogleTypeDateIn"])
    types["GoogleTypeDateOut"] = t.struct(
        {
            "month": t.integer().optional(),
            "year": t.integer().optional(),
            "day": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeDateOut"])
    types["GoogleCloudChannelV1ProvisionCloudIdentityRequestIn"] = t.struct(
        {
            "cloudIdentityInfo": t.proxy(
                renames["GoogleCloudChannelV1CloudIdentityInfoIn"]
            ).optional(),
            "validateOnly": t.boolean().optional(),
            "user": t.proxy(renames["GoogleCloudChannelV1AdminUserIn"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1ProvisionCloudIdentityRequestIn"])
    types["GoogleCloudChannelV1ProvisionCloudIdentityRequestOut"] = t.struct(
        {
            "cloudIdentityInfo": t.proxy(
                renames["GoogleCloudChannelV1CloudIdentityInfoOut"]
            ).optional(),
            "validateOnly": t.boolean().optional(),
            "user": t.proxy(renames["GoogleCloudChannelV1AdminUserOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1ProvisionCloudIdentityRequestOut"])
    types["GoogleCloudChannelV1ListReportsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "reports": t.array(
                t.proxy(renames["GoogleCloudChannelV1ReportIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudChannelV1ListReportsResponseIn"])
    types["GoogleCloudChannelV1ListReportsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "reports": t.array(
                t.proxy(renames["GoogleCloudChannelV1ReportOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1ListReportsResponseOut"])
    types["GoogleCloudChannelV1alpha1OperationMetadataIn"] = t.struct(
        {"operationType": t.string().optional()}
    ).named(renames["GoogleCloudChannelV1alpha1OperationMetadataIn"])
    types["GoogleCloudChannelV1alpha1OperationMetadataOut"] = t.struct(
        {
            "operationType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1alpha1OperationMetadataOut"])
    types["GoogleCloudChannelV1ListPurchasableOffersResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "purchasableOffers": t.array(
                t.proxy(renames["GoogleCloudChannelV1PurchasableOfferIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudChannelV1ListPurchasableOffersResponseIn"])
    types["GoogleCloudChannelV1ListPurchasableOffersResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "purchasableOffers": t.array(
                t.proxy(renames["GoogleCloudChannelV1PurchasableOfferOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1ListPurchasableOffersResponseOut"])
    types["GoogleCloudChannelV1ChannelPartnerRepricingConfigIn"] = t.struct(
        {"repricingConfig": t.proxy(renames["GoogleCloudChannelV1RepricingConfigIn"])}
    ).named(renames["GoogleCloudChannelV1ChannelPartnerRepricingConfigIn"])
    types["GoogleCloudChannelV1ChannelPartnerRepricingConfigOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "repricingConfig": t.proxy(
                renames["GoogleCloudChannelV1RepricingConfigOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1ChannelPartnerRepricingConfigOut"])
    types["GoogleCloudChannelV1SuspendEntitlementRequestIn"] = t.struct(
        {"requestId": t.string().optional()}
    ).named(renames["GoogleCloudChannelV1SuspendEntitlementRequestIn"])
    types["GoogleCloudChannelV1SuspendEntitlementRequestOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1SuspendEntitlementRequestOut"])
    types["GoogleCloudChannelV1MarketingInfoIn"] = t.struct(
        {
            "description": t.string().optional(),
            "defaultLogo": t.proxy(renames["GoogleCloudChannelV1MediaIn"]).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["GoogleCloudChannelV1MarketingInfoIn"])
    types["GoogleCloudChannelV1MarketingInfoOut"] = t.struct(
        {
            "description": t.string().optional(),
            "defaultLogo": t.proxy(renames["GoogleCloudChannelV1MediaOut"]).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1MarketingInfoOut"])
    types["GoogleCloudChannelV1AssociationInfoIn"] = t.struct(
        {"baseEntitlement": t.string().optional()}
    ).named(renames["GoogleCloudChannelV1AssociationInfoIn"])
    types["GoogleCloudChannelV1AssociationInfoOut"] = t.struct(
        {
            "baseEntitlement": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1AssociationInfoOut"])
    types["GoogleCloudChannelV1PurchasableSkuIn"] = t.struct(
        {"sku": t.proxy(renames["GoogleCloudChannelV1SkuIn"]).optional()}
    ).named(renames["GoogleCloudChannelV1PurchasableSkuIn"])
    types["GoogleCloudChannelV1PurchasableSkuOut"] = t.struct(
        {
            "sku": t.proxy(renames["GoogleCloudChannelV1SkuOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1PurchasableSkuOut"])
    types["GoogleCloudChannelV1FetchReportResultsRequestIn"] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "partitionKeys": t.array(t.string()).optional(),
            "pageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudChannelV1FetchReportResultsRequestIn"])
    types["GoogleCloudChannelV1FetchReportResultsRequestOut"] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "partitionKeys": t.array(t.string()).optional(),
            "pageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1FetchReportResultsRequestOut"])
    types["GoogleCloudChannelV1RunReportJobRequestIn"] = t.struct(
        {
            "dateRange": t.proxy(renames["GoogleCloudChannelV1DateRangeIn"]).optional(),
            "filter": t.string().optional(),
            "languageCode": t.string().optional(),
        }
    ).named(renames["GoogleCloudChannelV1RunReportJobRequestIn"])
    types["GoogleCloudChannelV1RunReportJobRequestOut"] = t.struct(
        {
            "dateRange": t.proxy(
                renames["GoogleCloudChannelV1DateRangeOut"]
            ).optional(),
            "filter": t.string().optional(),
            "languageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1RunReportJobRequestOut"])
    types["GoogleCloudChannelV1alpha1ValueIn"] = t.struct(
        {
            "protoValue": t.struct({"_": t.string().optional()}).optional(),
            "doubleValue": t.number().optional(),
            "int64Value": t.string().optional(),
            "stringValue": t.string().optional(),
            "boolValue": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudChannelV1alpha1ValueIn"])
    types["GoogleCloudChannelV1alpha1ValueOut"] = t.struct(
        {
            "protoValue": t.struct({"_": t.string().optional()}).optional(),
            "doubleValue": t.number().optional(),
            "int64Value": t.string().optional(),
            "stringValue": t.string().optional(),
            "boolValue": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1alpha1ValueOut"])
    types["GoogleCloudChannelV1ActivateEntitlementRequestIn"] = t.struct(
        {"requestId": t.string().optional()}
    ).named(renames["GoogleCloudChannelV1ActivateEntitlementRequestIn"])
    types["GoogleCloudChannelV1ActivateEntitlementRequestOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1ActivateEntitlementRequestOut"])
    types["GoogleCloudChannelV1ChangeRenewalSettingsRequestIn"] = t.struct(
        {
            "requestId": t.string().optional(),
            "renewalSettings": t.proxy(
                renames["GoogleCloudChannelV1RenewalSettingsIn"]
            ),
        }
    ).named(renames["GoogleCloudChannelV1ChangeRenewalSettingsRequestIn"])
    types["GoogleCloudChannelV1ChangeRenewalSettingsRequestOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "renewalSettings": t.proxy(
                renames["GoogleCloudChannelV1RenewalSettingsOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1ChangeRenewalSettingsRequestOut"])
    types["GoogleCloudChannelV1UnregisterSubscriberRequestIn"] = t.struct(
        {"serviceAccount": t.string()}
    ).named(renames["GoogleCloudChannelV1UnregisterSubscriberRequestIn"])
    types["GoogleCloudChannelV1UnregisterSubscriberRequestOut"] = t.struct(
        {
            "serviceAccount": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1UnregisterSubscriberRequestOut"])
    types["GoogleCloudChannelV1ReportResultsMetadataIn"] = t.struct(
        {
            "precedingDateRange": t.proxy(
                renames["GoogleCloudChannelV1DateRangeIn"]
            ).optional(),
            "rowCount": t.string().optional(),
            "dateRange": t.proxy(renames["GoogleCloudChannelV1DateRangeIn"]).optional(),
            "report": t.proxy(renames["GoogleCloudChannelV1ReportIn"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1ReportResultsMetadataIn"])
    types["GoogleCloudChannelV1ReportResultsMetadataOut"] = t.struct(
        {
            "precedingDateRange": t.proxy(
                renames["GoogleCloudChannelV1DateRangeOut"]
            ).optional(),
            "rowCount": t.string().optional(),
            "dateRange": t.proxy(
                renames["GoogleCloudChannelV1DateRangeOut"]
            ).optional(),
            "report": t.proxy(renames["GoogleCloudChannelV1ReportOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1ReportResultsMetadataOut"])
    types["GoogleCloudChannelV1ReportIn"] = t.struct(
        {
            "name": t.string(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "columns": t.array(
                t.proxy(renames["GoogleCloudChannelV1ColumnIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudChannelV1ReportIn"])
    types["GoogleCloudChannelV1ReportOut"] = t.struct(
        {
            "name": t.string(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "columns": t.array(
                t.proxy(renames["GoogleCloudChannelV1ColumnOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1ReportOut"])
    types["GoogleCloudChannelV1OperationMetadataIn"] = t.struct(
        {"operationType": t.string().optional()}
    ).named(renames["GoogleCloudChannelV1OperationMetadataIn"])
    types["GoogleCloudChannelV1OperationMetadataOut"] = t.struct(
        {
            "operationType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1OperationMetadataOut"])
    types["GoogleCloudChannelV1BillingAccountPurchaseInfoIn"] = t.struct(
        {
            "billingAccount": t.proxy(
                renames["GoogleCloudChannelV1BillingAccountIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudChannelV1BillingAccountPurchaseInfoIn"])
    types["GoogleCloudChannelV1BillingAccountPurchaseInfoOut"] = t.struct(
        {
            "billingAccount": t.proxy(
                renames["GoogleCloudChannelV1BillingAccountOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1BillingAccountPurchaseInfoOut"])
    types["GoogleCloudChannelV1ChangeParametersRequestIn"] = t.struct(
        {
            "requestId": t.string().optional(),
            "parameters": t.array(t.proxy(renames["GoogleCloudChannelV1ParameterIn"])),
            "purchaseOrderId": t.string().optional(),
        }
    ).named(renames["GoogleCloudChannelV1ChangeParametersRequestIn"])
    types["GoogleCloudChannelV1ChangeParametersRequestOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "parameters": t.array(t.proxy(renames["GoogleCloudChannelV1ParameterOut"])),
            "purchaseOrderId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1ChangeParametersRequestOut"])
    types["GoogleCloudChannelV1alpha1TrialSettingsIn"] = t.struct(
        {"endTime": t.string().optional(), "trial": t.boolean().optional()}
    ).named(renames["GoogleCloudChannelV1alpha1TrialSettingsIn"])
    types["GoogleCloudChannelV1alpha1TrialSettingsOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "trial": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1alpha1TrialSettingsOut"])
    types["GoogleCloudChannelV1SubscriberEventIn"] = t.struct(
        {
            "entitlementEvent": t.proxy(
                renames["GoogleCloudChannelV1EntitlementEventIn"]
            ).optional(),
            "customerEvent": t.proxy(
                renames["GoogleCloudChannelV1CustomerEventIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudChannelV1SubscriberEventIn"])
    types["GoogleCloudChannelV1SubscriberEventOut"] = t.struct(
        {
            "entitlementEvent": t.proxy(
                renames["GoogleCloudChannelV1EntitlementEventOut"]
            ).optional(),
            "customerEvent": t.proxy(
                renames["GoogleCloudChannelV1CustomerEventOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1SubscriberEventOut"])
    types["GoogleCloudChannelV1ConstraintsIn"] = t.struct(
        {
            "customerConstraints": t.proxy(
                renames["GoogleCloudChannelV1CustomerConstraintsIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudChannelV1ConstraintsIn"])
    types["GoogleCloudChannelV1ConstraintsOut"] = t.struct(
        {
            "customerConstraints": t.proxy(
                renames["GoogleCloudChannelV1CustomerConstraintsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1ConstraintsOut"])
    types["GoogleCloudChannelV1alpha1PeriodIn"] = t.struct(
        {"periodType": t.string().optional(), "duration": t.integer().optional()}
    ).named(renames["GoogleCloudChannelV1alpha1PeriodIn"])
    types["GoogleCloudChannelV1alpha1PeriodOut"] = t.struct(
        {
            "periodType": t.string().optional(),
            "duration": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1alpha1PeriodOut"])
    types["GoogleTypeTimeZoneIn"] = t.struct(
        {"id": t.string().optional(), "version": t.string().optional()}
    ).named(renames["GoogleTypeTimeZoneIn"])
    types["GoogleTypeTimeZoneOut"] = t.struct(
        {
            "id": t.string().optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeTimeZoneOut"])
    types["GoogleRpcStatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["GoogleRpcStatusIn"])
    types["GoogleRpcStatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleRpcStatusOut"])
    types["GoogleCloudChannelV1ListTransferableOffersResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "transferableOffers": t.array(
                t.proxy(renames["GoogleCloudChannelV1TransferableOfferIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudChannelV1ListTransferableOffersResponseIn"])
    types["GoogleCloudChannelV1ListTransferableOffersResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "transferableOffers": t.array(
                t.proxy(renames["GoogleCloudChannelV1TransferableOfferOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1ListTransferableOffersResponseOut"])
    types["GoogleCloudChannelV1RepricingConfigEntitlementGranularityIn"] = t.struct(
        {"entitlement": t.string().optional()}
    ).named(renames["GoogleCloudChannelV1RepricingConfigEntitlementGranularityIn"])
    types["GoogleCloudChannelV1RepricingConfigEntitlementGranularityOut"] = t.struct(
        {
            "entitlement": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1RepricingConfigEntitlementGranularityOut"])
    types["GoogleCloudChannelV1PriceTierIn"] = t.struct(
        {
            "price": t.proxy(renames["GoogleCloudChannelV1PriceIn"]).optional(),
            "firstResource": t.integer().optional(),
            "lastResource": t.integer().optional(),
        }
    ).named(renames["GoogleCloudChannelV1PriceTierIn"])
    types["GoogleCloudChannelV1PriceTierOut"] = t.struct(
        {
            "price": t.proxy(renames["GoogleCloudChannelV1PriceOut"]).optional(),
            "firstResource": t.integer().optional(),
            "lastResource": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1PriceTierOut"])
    types["GoogleCloudChannelV1alpha1EntitlementEventIn"] = t.struct(
        {"entitlement": t.string().optional(), "eventType": t.string().optional()}
    ).named(renames["GoogleCloudChannelV1alpha1EntitlementEventIn"])
    types["GoogleCloudChannelV1alpha1EntitlementEventOut"] = t.struct(
        {
            "entitlement": t.string().optional(),
            "eventType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1alpha1EntitlementEventOut"])
    types["GoogleCloudChannelV1ReportStatusIn"] = t.struct(
        {
            "state": t.string().optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudChannelV1ReportStatusIn"])
    types["GoogleCloudChannelV1ReportStatusOut"] = t.struct(
        {
            "state": t.string().optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1ReportStatusOut"])
    types["GoogleCloudChannelV1alpha1ParameterIn"] = t.struct(
        {
            "value": t.proxy(renames["GoogleCloudChannelV1alpha1ValueIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudChannelV1alpha1ParameterIn"])
    types["GoogleCloudChannelV1alpha1ParameterOut"] = t.struct(
        {
            "editable": t.boolean().optional(),
            "value": t.proxy(renames["GoogleCloudChannelV1alpha1ValueOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1alpha1ParameterOut"])
    types["GoogleCloudChannelV1CloudIdentityInfoIn"] = t.struct(
        {
            "eduData": t.proxy(renames["GoogleCloudChannelV1EduDataIn"]).optional(),
            "alternateEmail": t.string().optional(),
            "customerType": t.string().optional(),
            "languageCode": t.string().optional(),
            "phoneNumber": t.string().optional(),
        }
    ).named(renames["GoogleCloudChannelV1CloudIdentityInfoIn"])
    types["GoogleCloudChannelV1CloudIdentityInfoOut"] = t.struct(
        {
            "eduData": t.proxy(renames["GoogleCloudChannelV1EduDataOut"]).optional(),
            "adminConsoleUri": t.string().optional(),
            "isDomainVerified": t.boolean().optional(),
            "primaryDomain": t.string().optional(),
            "alternateEmail": t.string().optional(),
            "customerType": t.string().optional(),
            "languageCode": t.string().optional(),
            "phoneNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1CloudIdentityInfoOut"])
    types["GoogleCloudChannelV1alpha1ReportResultsMetadataIn"] = t.struct(
        {
            "dateRange": t.proxy(
                renames["GoogleCloudChannelV1alpha1DateRangeIn"]
            ).optional(),
            "rowCount": t.string().optional(),
            "precedingDateRange": t.proxy(
                renames["GoogleCloudChannelV1alpha1DateRangeIn"]
            ).optional(),
            "report": t.proxy(renames["GoogleCloudChannelV1alpha1ReportIn"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1alpha1ReportResultsMetadataIn"])
    types["GoogleCloudChannelV1alpha1ReportResultsMetadataOut"] = t.struct(
        {
            "dateRange": t.proxy(
                renames["GoogleCloudChannelV1alpha1DateRangeOut"]
            ).optional(),
            "rowCount": t.string().optional(),
            "precedingDateRange": t.proxy(
                renames["GoogleCloudChannelV1alpha1DateRangeOut"]
            ).optional(),
            "report": t.proxy(
                renames["GoogleCloudChannelV1alpha1ReportOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1alpha1ReportResultsMetadataOut"])
    types["GoogleCloudChannelV1alpha1CustomerEventIn"] = t.struct(
        {"eventType": t.string().optional(), "customer": t.string().optional()}
    ).named(renames["GoogleCloudChannelV1alpha1CustomerEventIn"])
    types["GoogleCloudChannelV1alpha1CustomerEventOut"] = t.struct(
        {
            "eventType": t.string().optional(),
            "customer": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1alpha1CustomerEventOut"])
    types["GoogleCloudChannelV1BillingAccountIn"] = t.struct(
        {"displayName": t.string().optional()}
    ).named(renames["GoogleCloudChannelV1BillingAccountIn"])
    types["GoogleCloudChannelV1BillingAccountOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "currencyCode": t.string().optional(),
            "createTime": t.string().optional(),
            "regionCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1BillingAccountOut"])
    types["GoogleCloudChannelV1RepricingConfigIn"] = t.struct(
        {
            "adjustment": t.proxy(renames["GoogleCloudChannelV1RepricingAdjustmentIn"]),
            "effectiveInvoiceMonth": t.proxy(renames["GoogleTypeDateIn"]),
            "channelPartnerGranularity": t.proxy(
                renames[
                    "GoogleCloudChannelV1RepricingConfigChannelPartnerGranularityIn"
                ]
            ).optional(),
            "rebillingBasis": t.string(),
            "conditionalOverrides": t.array(
                t.proxy(renames["GoogleCloudChannelV1ConditionalOverrideIn"])
            ).optional(),
            "entitlementGranularity": t.proxy(
                renames["GoogleCloudChannelV1RepricingConfigEntitlementGranularityIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudChannelV1RepricingConfigIn"])
    types["GoogleCloudChannelV1RepricingConfigOut"] = t.struct(
        {
            "adjustment": t.proxy(
                renames["GoogleCloudChannelV1RepricingAdjustmentOut"]
            ),
            "effectiveInvoiceMonth": t.proxy(renames["GoogleTypeDateOut"]),
            "channelPartnerGranularity": t.proxy(
                renames[
                    "GoogleCloudChannelV1RepricingConfigChannelPartnerGranularityOut"
                ]
            ).optional(),
            "rebillingBasis": t.string(),
            "conditionalOverrides": t.array(
                t.proxy(renames["GoogleCloudChannelV1ConditionalOverrideOut"])
            ).optional(),
            "entitlementGranularity": t.proxy(
                renames["GoogleCloudChannelV1RepricingConfigEntitlementGranularityOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1RepricingConfigOut"])
    types["GoogleCloudChannelV1UpdateChannelPartnerLinkRequestIn"] = t.struct(
        {
            "updateMask": t.string(),
            "channelPartnerLink": t.proxy(
                renames["GoogleCloudChannelV1ChannelPartnerLinkIn"]
            ),
        }
    ).named(renames["GoogleCloudChannelV1UpdateChannelPartnerLinkRequestIn"])
    types["GoogleCloudChannelV1UpdateChannelPartnerLinkRequestOut"] = t.struct(
        {
            "updateMask": t.string(),
            "channelPartnerLink": t.proxy(
                renames["GoogleCloudChannelV1ChannelPartnerLinkOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1UpdateChannelPartnerLinkRequestOut"])
    types["GoogleCloudChannelV1ContactInfoIn"] = t.struct(
        {
            "phone": t.string().optional(),
            "lastName": t.string().optional(),
            "title": t.string().optional(),
            "firstName": t.string().optional(),
            "email": t.string().optional(),
        }
    ).named(renames["GoogleCloudChannelV1ContactInfoIn"])
    types["GoogleCloudChannelV1ContactInfoOut"] = t.struct(
        {
            "phone": t.string().optional(),
            "lastName": t.string().optional(),
            "title": t.string().optional(),
            "firstName": t.string().optional(),
            "email": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1ContactInfoOut"])
    types["GoogleCloudChannelV1ParameterIn"] = t.struct(
        {
            "value": t.proxy(renames["GoogleCloudChannelV1ValueIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudChannelV1ParameterIn"])
    types["GoogleCloudChannelV1ParameterOut"] = t.struct(
        {
            "value": t.proxy(renames["GoogleCloudChannelV1ValueOut"]).optional(),
            "editable": t.boolean().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1ParameterOut"])
    types["GoogleCloudChannelV1alpha1ColumnIn"] = t.struct(
        {
            "columnId": t.string().optional(),
            "displayName": t.string().optional(),
            "dataType": t.string().optional(),
        }
    ).named(renames["GoogleCloudChannelV1alpha1ColumnIn"])
    types["GoogleCloudChannelV1alpha1ColumnOut"] = t.struct(
        {
            "columnId": t.string().optional(),
            "displayName": t.string().optional(),
            "dataType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1alpha1ColumnOut"])
    types["GoogleCloudChannelV1ChannelPartnerLinkIn"] = t.struct(
        {"linkState": t.string(), "resellerCloudIdentityId": t.string()}
    ).named(renames["GoogleCloudChannelV1ChannelPartnerLinkIn"])
    types["GoogleCloudChannelV1ChannelPartnerLinkOut"] = t.struct(
        {
            "channelPartnerCloudIdentityInfo": t.proxy(
                renames["GoogleCloudChannelV1CloudIdentityInfoOut"]
            ).optional(),
            "updateTime": t.string().optional(),
            "linkState": t.string(),
            "resellerCloudIdentityId": t.string(),
            "inviteLinkUri": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "publicId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1ChannelPartnerLinkOut"])
    types["GoogleCloudChannelV1StartPaidServiceRequestIn"] = t.struct(
        {"requestId": t.string().optional()}
    ).named(renames["GoogleCloudChannelV1StartPaidServiceRequestIn"])
    types["GoogleCloudChannelV1StartPaidServiceRequestOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1StartPaidServiceRequestOut"])
    types["GoogleCloudChannelV1ListChannelPartnerLinksResponseIn"] = t.struct(
        {
            "channelPartnerLinks": t.array(
                t.proxy(renames["GoogleCloudChannelV1ChannelPartnerLinkIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudChannelV1ListChannelPartnerLinksResponseIn"])
    types["GoogleCloudChannelV1ListChannelPartnerLinksResponseOut"] = t.struct(
        {
            "channelPartnerLinks": t.array(
                t.proxy(renames["GoogleCloudChannelV1ChannelPartnerLinkOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1ListChannelPartnerLinksResponseOut"])
    types["GoogleLongrunningListOperationsResponseIn"] = t.struct(
        {
            "operations": t.array(
                t.proxy(renames["GoogleLongrunningOperationIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleLongrunningListOperationsResponseIn"])
    types["GoogleLongrunningListOperationsResponseOut"] = t.struct(
        {
            "operations": t.array(
                t.proxy(renames["GoogleLongrunningOperationOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleLongrunningListOperationsResponseOut"])
    types["GoogleCloudChannelV1RenewalSettingsIn"] = t.struct(
        {
            "paymentCycle": t.proxy(renames["GoogleCloudChannelV1PeriodIn"]).optional(),
            "paymentPlan": t.string().optional(),
            "resizeUnitCount": t.boolean().optional(),
            "enableRenewal": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudChannelV1RenewalSettingsIn"])
    types["GoogleCloudChannelV1RenewalSettingsOut"] = t.struct(
        {
            "paymentCycle": t.proxy(
                renames["GoogleCloudChannelV1PeriodOut"]
            ).optional(),
            "paymentPlan": t.string().optional(),
            "resizeUnitCount": t.boolean().optional(),
            "enableRenewal": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1RenewalSettingsOut"])
    types["GoogleCloudChannelV1alpha1RenewalSettingsIn"] = t.struct(
        {
            "resizeUnitCount": t.boolean().optional(),
            "enableRenewal": t.boolean().optional(),
            "disableCommitment": t.boolean().optional(),
            "paymentPlan": t.string().optional(),
            "paymentCycle": t.proxy(
                renames["GoogleCloudChannelV1alpha1PeriodIn"]
            ).optional(),
            "paymentOption": t.string().optional(),
        }
    ).named(renames["GoogleCloudChannelV1alpha1RenewalSettingsIn"])
    types["GoogleCloudChannelV1alpha1RenewalSettingsOut"] = t.struct(
        {
            "resizeUnitCount": t.boolean().optional(),
            "enableRenewal": t.boolean().optional(),
            "scheduledRenewalOffer": t.string().optional(),
            "disableCommitment": t.boolean().optional(),
            "paymentPlan": t.string().optional(),
            "paymentCycle": t.proxy(
                renames["GoogleCloudChannelV1alpha1PeriodOut"]
            ).optional(),
            "paymentOption": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1alpha1RenewalSettingsOut"])
    types["GoogleCloudChannelV1ListCustomersResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "customers": t.array(
                t.proxy(renames["GoogleCloudChannelV1CustomerIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudChannelV1ListCustomersResponseIn"])
    types["GoogleCloudChannelV1ListCustomersResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "customers": t.array(
                t.proxy(renames["GoogleCloudChannelV1CustomerOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1ListCustomersResponseOut"])
    types["GoogleCloudChannelV1CustomerConstraintsIn"] = t.struct(
        {
            "allowedCustomerTypes": t.array(t.string()).optional(),
            "promotionalOrderTypes": t.array(t.string()).optional(),
            "allowedRegions": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudChannelV1CustomerConstraintsIn"])
    types["GoogleCloudChannelV1CustomerConstraintsOut"] = t.struct(
        {
            "allowedCustomerTypes": t.array(t.string()).optional(),
            "promotionalOrderTypes": t.array(t.string()).optional(),
            "allowedRegions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1CustomerConstraintsOut"])
    types["GoogleCloudChannelV1ListTransferableSkusRequestIn"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "pageToken": t.string().optional(),
            "pageSize": t.integer().optional(),
            "cloudIdentityId": t.string().optional(),
            "customerName": t.string().optional(),
            "authToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudChannelV1ListTransferableSkusRequestIn"])
    types["GoogleCloudChannelV1ListTransferableSkusRequestOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "pageToken": t.string().optional(),
            "pageSize": t.integer().optional(),
            "cloudIdentityId": t.string().optional(),
            "customerName": t.string().optional(),
            "authToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1ListTransferableSkusRequestOut"])
    types["GoogleCloudChannelV1PurchasableOfferIn"] = t.struct(
        {"offer": t.proxy(renames["GoogleCloudChannelV1OfferIn"]).optional()}
    ).named(renames["GoogleCloudChannelV1PurchasableOfferIn"])
    types["GoogleCloudChannelV1PurchasableOfferOut"] = t.struct(
        {
            "offer": t.proxy(renames["GoogleCloudChannelV1OfferOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1PurchasableOfferOut"])
    types["GoogleCloudChannelV1ListEntitlementsResponseIn"] = t.struct(
        {
            "entitlements": t.array(
                t.proxy(renames["GoogleCloudChannelV1EntitlementIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudChannelV1ListEntitlementsResponseIn"])
    types["GoogleCloudChannelV1ListEntitlementsResponseOut"] = t.struct(
        {
            "entitlements": t.array(
                t.proxy(renames["GoogleCloudChannelV1EntitlementOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1ListEntitlementsResponseOut"])
    types["GoogleCloudChannelV1TransferEntitlementsToGoogleRequestIn"] = t.struct(
        {
            "entitlements": t.array(
                t.proxy(renames["GoogleCloudChannelV1EntitlementIn"])
            ),
            "requestId": t.string().optional(),
        }
    ).named(renames["GoogleCloudChannelV1TransferEntitlementsToGoogleRequestIn"])
    types["GoogleCloudChannelV1TransferEntitlementsToGoogleRequestOut"] = t.struct(
        {
            "entitlements": t.array(
                t.proxy(renames["GoogleCloudChannelV1EntitlementOut"])
            ),
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1TransferEntitlementsToGoogleRequestOut"])
    types["GoogleCloudChannelV1ProductIn"] = t.struct(
        {
            "marketingInfo": t.proxy(
                renames["GoogleCloudChannelV1MarketingInfoIn"]
            ).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudChannelV1ProductIn"])
    types["GoogleCloudChannelV1ProductOut"] = t.struct(
        {
            "marketingInfo": t.proxy(
                renames["GoogleCloudChannelV1MarketingInfoOut"]
            ).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1ProductOut"])
    types["GoogleCloudChannelV1AdminUserIn"] = t.struct(
        {
            "givenName": t.string().optional(),
            "familyName": t.string().optional(),
            "email": t.string().optional(),
        }
    ).named(renames["GoogleCloudChannelV1AdminUserIn"])
    types["GoogleCloudChannelV1AdminUserOut"] = t.struct(
        {
            "givenName": t.string().optional(),
            "familyName": t.string().optional(),
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1AdminUserOut"])
    types["GoogleCloudChannelV1EntitlementChangeIn"] = t.struct(
        {
            "provisionedService": t.proxy(
                renames["GoogleCloudChannelV1ProvisionedServiceIn"]
            ).optional(),
            "parameters": t.array(
                t.proxy(renames["GoogleCloudChannelV1ParameterIn"])
            ).optional(),
            "operatorType": t.string().optional(),
            "suspensionReason": t.string().optional(),
            "changeType": t.string().optional(),
            "activationReason": t.string().optional(),
            "offer": t.string(),
            "operator": t.string().optional(),
            "entitlement": t.string(),
            "createTime": t.string().optional(),
            "cancellationReason": t.string().optional(),
            "otherChangeReason": t.string().optional(),
        }
    ).named(renames["GoogleCloudChannelV1EntitlementChangeIn"])
    types["GoogleCloudChannelV1EntitlementChangeOut"] = t.struct(
        {
            "provisionedService": t.proxy(
                renames["GoogleCloudChannelV1ProvisionedServiceOut"]
            ).optional(),
            "parameters": t.array(
                t.proxy(renames["GoogleCloudChannelV1ParameterOut"])
            ).optional(),
            "operatorType": t.string().optional(),
            "suspensionReason": t.string().optional(),
            "changeType": t.string().optional(),
            "activationReason": t.string().optional(),
            "offer": t.string(),
            "operator": t.string().optional(),
            "entitlement": t.string(),
            "createTime": t.string().optional(),
            "cancellationReason": t.string().optional(),
            "otherChangeReason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1EntitlementChangeOut"])
    types["GoogleCloudChannelV1PeriodIn"] = t.struct(
        {"duration": t.integer().optional(), "periodType": t.string().optional()}
    ).named(renames["GoogleCloudChannelV1PeriodIn"])
    types["GoogleCloudChannelV1PeriodOut"] = t.struct(
        {
            "duration": t.integer().optional(),
            "periodType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1PeriodOut"])
    types["GoogleCloudChannelV1ConditionalOverrideIn"] = t.struct(
        {
            "adjustment": t.proxy(renames["GoogleCloudChannelV1RepricingAdjustmentIn"]),
            "rebillingBasis": t.string(),
            "repricingCondition": t.proxy(
                renames["GoogleCloudChannelV1RepricingConditionIn"]
            ),
        }
    ).named(renames["GoogleCloudChannelV1ConditionalOverrideIn"])
    types["GoogleCloudChannelV1ConditionalOverrideOut"] = t.struct(
        {
            "adjustment": t.proxy(
                renames["GoogleCloudChannelV1RepricingAdjustmentOut"]
            ),
            "rebillingBasis": t.string(),
            "repricingCondition": t.proxy(
                renames["GoogleCloudChannelV1RepricingConditionOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1ConditionalOverrideOut"])
    types[
        "GoogleCloudChannelV1ListChannelPartnerRepricingConfigsResponseIn"
    ] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "channelPartnerRepricingConfigs": t.array(
                t.proxy(renames["GoogleCloudChannelV1ChannelPartnerRepricingConfigIn"])
            ).optional(),
        }
    ).named(
        renames["GoogleCloudChannelV1ListChannelPartnerRepricingConfigsResponseIn"]
    )
    types[
        "GoogleCloudChannelV1ListChannelPartnerRepricingConfigsResponseOut"
    ] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "channelPartnerRepricingConfigs": t.array(
                t.proxy(renames["GoogleCloudChannelV1ChannelPartnerRepricingConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudChannelV1ListChannelPartnerRepricingConfigsResponseOut"]
    )
    types["GoogleTypePostalAddressIn"] = t.struct(
        {
            "administrativeArea": t.string().optional(),
            "regionCode": t.string(),
            "recipients": t.array(t.string()).optional(),
            "revision": t.integer().optional(),
            "sublocality": t.string().optional(),
            "organization": t.string().optional(),
            "sortingCode": t.string().optional(),
            "languageCode": t.string().optional(),
            "locality": t.string().optional(),
            "postalCode": t.string().optional(),
            "addressLines": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleTypePostalAddressIn"])
    types["GoogleTypePostalAddressOut"] = t.struct(
        {
            "administrativeArea": t.string().optional(),
            "regionCode": t.string(),
            "recipients": t.array(t.string()).optional(),
            "revision": t.integer().optional(),
            "sublocality": t.string().optional(),
            "organization": t.string().optional(),
            "sortingCode": t.string().optional(),
            "languageCode": t.string().optional(),
            "locality": t.string().optional(),
            "postalCode": t.string().optional(),
            "addressLines": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypePostalAddressOut"])
    types["GoogleCloudChannelV1ReportJobIn"] = t.struct(
        {
            "name": t.string(),
            "reportStatus": t.proxy(
                renames["GoogleCloudChannelV1ReportStatusIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudChannelV1ReportJobIn"])
    types["GoogleCloudChannelV1ReportJobOut"] = t.struct(
        {
            "name": t.string(),
            "reportStatus": t.proxy(
                renames["GoogleCloudChannelV1ReportStatusOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1ReportJobOut"])
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
    types["GoogleCloudChannelV1PriceByResourceIn"] = t.struct(
        {
            "resourceType": t.string().optional(),
            "price": t.proxy(renames["GoogleCloudChannelV1PriceIn"]).optional(),
            "pricePhases": t.array(
                t.proxy(renames["GoogleCloudChannelV1PricePhaseIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudChannelV1PriceByResourceIn"])
    types["GoogleCloudChannelV1PriceByResourceOut"] = t.struct(
        {
            "resourceType": t.string().optional(),
            "price": t.proxy(renames["GoogleCloudChannelV1PriceOut"]).optional(),
            "pricePhases": t.array(
                t.proxy(renames["GoogleCloudChannelV1PricePhaseOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1PriceByResourceOut"])
    types["GoogleCloudChannelV1ListPurchasableSkusResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "purchasableSkus": t.array(
                t.proxy(renames["GoogleCloudChannelV1PurchasableSkuIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudChannelV1ListPurchasableSkusResponseIn"])
    types["GoogleCloudChannelV1ListPurchasableSkusResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "purchasableSkus": t.array(
                t.proxy(renames["GoogleCloudChannelV1PurchasableSkuOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1ListPurchasableSkusResponseOut"])
    types["GoogleCloudChannelV1QueryEligibleBillingAccountsResponseIn"] = t.struct(
        {
            "skuPurchaseGroups": t.array(
                t.proxy(renames["GoogleCloudChannelV1SkuPurchaseGroupIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudChannelV1QueryEligibleBillingAccountsResponseIn"])
    types["GoogleCloudChannelV1QueryEligibleBillingAccountsResponseOut"] = t.struct(
        {
            "skuPurchaseGroups": t.array(
                t.proxy(renames["GoogleCloudChannelV1SkuPurchaseGroupOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1QueryEligibleBillingAccountsResponseOut"])
    types["GoogleCloudChannelV1RepricingConfigChannelPartnerGranularityIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudChannelV1RepricingConfigChannelPartnerGranularityIn"])
    types["GoogleCloudChannelV1RepricingConfigChannelPartnerGranularityOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudChannelV1RepricingConfigChannelPartnerGranularityOut"])
    types["GoogleCloudChannelV1ReportValueIn"] = t.struct(
        {
            "moneyValue": t.proxy(renames["GoogleTypeMoneyIn"]).optional(),
            "intValue": t.string().optional(),
            "dateValue": t.proxy(renames["GoogleTypeDateIn"]).optional(),
            "dateTimeValue": t.proxy(renames["GoogleTypeDateTimeIn"]).optional(),
            "stringValue": t.string().optional(),
            "decimalValue": t.proxy(renames["GoogleTypeDecimalIn"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1ReportValueIn"])
    types["GoogleCloudChannelV1ReportValueOut"] = t.struct(
        {
            "moneyValue": t.proxy(renames["GoogleTypeMoneyOut"]).optional(),
            "intValue": t.string().optional(),
            "dateValue": t.proxy(renames["GoogleTypeDateOut"]).optional(),
            "dateTimeValue": t.proxy(renames["GoogleTypeDateTimeOut"]).optional(),
            "stringValue": t.string().optional(),
            "decimalValue": t.proxy(renames["GoogleTypeDecimalOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1ReportValueOut"])
    types["GoogleCloudChannelV1ListTransferableOffersRequestIn"] = t.struct(
        {
            "cloudIdentityId": t.string().optional(),
            "pageSize": t.integer().optional(),
            "sku": t.string(),
            "customerName": t.string().optional(),
            "pageToken": t.string().optional(),
            "languageCode": t.string().optional(),
        }
    ).named(renames["GoogleCloudChannelV1ListTransferableOffersRequestIn"])
    types["GoogleCloudChannelV1ListTransferableOffersRequestOut"] = t.struct(
        {
            "cloudIdentityId": t.string().optional(),
            "pageSize": t.integer().optional(),
            "sku": t.string(),
            "customerName": t.string().optional(),
            "pageToken": t.string().optional(),
            "languageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1ListTransferableOffersRequestOut"])
    types["GoogleCloudChannelV1ListEntitlementChangesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "entitlementChanges": t.array(
                t.proxy(renames["GoogleCloudChannelV1EntitlementChangeIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudChannelV1ListEntitlementChangesResponseIn"])
    types["GoogleCloudChannelV1ListEntitlementChangesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "entitlementChanges": t.array(
                t.proxy(renames["GoogleCloudChannelV1EntitlementChangeOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1ListEntitlementChangesResponseOut"])
    types["GoogleCloudChannelV1alpha1ProvisionedServiceIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudChannelV1alpha1ProvisionedServiceIn"])
    types["GoogleCloudChannelV1alpha1ProvisionedServiceOut"] = t.struct(
        {
            "skuId": t.string().optional(),
            "provisioningId": t.string().optional(),
            "productId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1alpha1ProvisionedServiceOut"])
    types["GoogleCloudChannelV1TrialSettingsIn"] = t.struct(
        {"trial": t.boolean().optional(), "endTime": t.string().optional()}
    ).named(renames["GoogleCloudChannelV1TrialSettingsIn"])
    types["GoogleCloudChannelV1TrialSettingsOut"] = t.struct(
        {
            "trial": t.boolean().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1TrialSettingsOut"])
    types["GoogleCloudChannelV1EntitlementEventIn"] = t.struct(
        {"eventType": t.string().optional(), "entitlement": t.string().optional()}
    ).named(renames["GoogleCloudChannelV1EntitlementEventIn"])
    types["GoogleCloudChannelV1EntitlementEventOut"] = t.struct(
        {
            "eventType": t.string().optional(),
            "entitlement": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1EntitlementEventOut"])
    types["GoogleCloudChannelV1CancelEntitlementRequestIn"] = t.struct(
        {"requestId": t.string().optional()}
    ).named(renames["GoogleCloudChannelV1CancelEntitlementRequestIn"])
    types["GoogleCloudChannelV1CancelEntitlementRequestOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1CancelEntitlementRequestOut"])
    types["GoogleTypeDecimalIn"] = t.struct({"value": t.string().optional()}).named(
        renames["GoogleTypeDecimalIn"]
    )
    types["GoogleTypeDecimalOut"] = t.struct(
        {
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeDecimalOut"])
    types["GoogleCloudChannelV1ParameterDefinitionIn"] = t.struct(
        {
            "allowedValues": t.array(
                t.proxy(renames["GoogleCloudChannelV1ValueIn"])
            ).optional(),
            "minValue": t.proxy(renames["GoogleCloudChannelV1ValueIn"]).optional(),
            "optional": t.boolean().optional(),
            "name": t.string().optional(),
            "maxValue": t.proxy(renames["GoogleCloudChannelV1ValueIn"]).optional(),
            "parameterType": t.string().optional(),
        }
    ).named(renames["GoogleCloudChannelV1ParameterDefinitionIn"])
    types["GoogleCloudChannelV1ParameterDefinitionOut"] = t.struct(
        {
            "allowedValues": t.array(
                t.proxy(renames["GoogleCloudChannelV1ValueOut"])
            ).optional(),
            "minValue": t.proxy(renames["GoogleCloudChannelV1ValueOut"]).optional(),
            "optional": t.boolean().optional(),
            "name": t.string().optional(),
            "maxValue": t.proxy(renames["GoogleCloudChannelV1ValueOut"]).optional(),
            "parameterType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1ParameterDefinitionOut"])
    types["GoogleCloudChannelV1ProvisionedServiceIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudChannelV1ProvisionedServiceIn"])
    types["GoogleCloudChannelV1ProvisionedServiceOut"] = t.struct(
        {
            "provisioningId": t.string().optional(),
            "productId": t.string().optional(),
            "skuId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1ProvisionedServiceOut"])
    types["GoogleCloudChannelV1EduDataIn"] = t.struct(
        {
            "instituteSize": t.string().optional(),
            "instituteType": t.string().optional(),
            "website": t.string().optional(),
        }
    ).named(renames["GoogleCloudChannelV1EduDataIn"])
    types["GoogleCloudChannelV1EduDataOut"] = t.struct(
        {
            "instituteSize": t.string().optional(),
            "instituteType": t.string().optional(),
            "website": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1EduDataOut"])
    types["GoogleCloudChannelV1SkuPurchaseGroupIn"] = t.struct(
        {
            "billingAccountPurchaseInfos": t.array(
                t.proxy(renames["GoogleCloudChannelV1BillingAccountPurchaseInfoIn"])
            ).optional(),
            "skus": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudChannelV1SkuPurchaseGroupIn"])
    types["GoogleCloudChannelV1SkuPurchaseGroupOut"] = t.struct(
        {
            "billingAccountPurchaseInfos": t.array(
                t.proxy(renames["GoogleCloudChannelV1BillingAccountPurchaseInfoOut"])
            ).optional(),
            "skus": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1SkuPurchaseGroupOut"])
    types["GoogleCloudChannelV1alpha1ChannelPartnerEventIn"] = t.struct(
        {"channelPartner": t.string().optional(), "eventType": t.string().optional()}
    ).named(renames["GoogleCloudChannelV1alpha1ChannelPartnerEventIn"])
    types["GoogleCloudChannelV1alpha1ChannelPartnerEventOut"] = t.struct(
        {
            "channelPartner": t.string().optional(),
            "eventType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1alpha1ChannelPartnerEventOut"])
    types["GoogleCloudChannelV1CloudIdentityCustomerAccountIn"] = t.struct(
        {
            "existing": t.boolean().optional(),
            "owned": t.boolean().optional(),
            "customerCloudIdentityId": t.string().optional(),
            "customerName": t.string().optional(),
        }
    ).named(renames["GoogleCloudChannelV1CloudIdentityCustomerAccountIn"])
    types["GoogleCloudChannelV1CloudIdentityCustomerAccountOut"] = t.struct(
        {
            "existing": t.boolean().optional(),
            "owned": t.boolean().optional(),
            "customerCloudIdentityId": t.string().optional(),
            "customerName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1CloudIdentityCustomerAccountOut"])
    types["GoogleCloudChannelV1alpha1TransferEntitlementsResponseIn"] = t.struct(
        {
            "entitlements": t.array(
                t.proxy(renames["GoogleCloudChannelV1alpha1EntitlementIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudChannelV1alpha1TransferEntitlementsResponseIn"])
    types["GoogleCloudChannelV1alpha1TransferEntitlementsResponseOut"] = t.struct(
        {
            "entitlements": t.array(
                t.proxy(renames["GoogleCloudChannelV1alpha1EntitlementOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudChannelV1alpha1TransferEntitlementsResponseOut"])
    types["GoogleTypeDateTimeIn"] = t.struct(
        {
            "day": t.integer().optional(),
            "seconds": t.integer().optional(),
            "utcOffset": t.string().optional(),
            "month": t.integer().optional(),
            "timeZone": t.proxy(renames["GoogleTypeTimeZoneIn"]).optional(),
            "year": t.integer().optional(),
            "minutes": t.integer().optional(),
            "nanos": t.integer().optional(),
            "hours": t.integer().optional(),
        }
    ).named(renames["GoogleTypeDateTimeIn"])
    types["GoogleTypeDateTimeOut"] = t.struct(
        {
            "day": t.integer().optional(),
            "seconds": t.integer().optional(),
            "utcOffset": t.string().optional(),
            "month": t.integer().optional(),
            "timeZone": t.proxy(renames["GoogleTypeTimeZoneOut"]).optional(),
            "year": t.integer().optional(),
            "minutes": t.integer().optional(),
            "nanos": t.integer().optional(),
            "hours": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeDateTimeOut"])

    functions = {}
    functions["accountsCheckCloudIdentityAccountsExist"] = cloudchannel.post(
        "v1/{parent}:listTransferableSkus",
        t.struct(
            {
                "parent": t.string(),
                "languageCode": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "cloudIdentityId": t.string().optional(),
                "customerName": t.string().optional(),
                "authToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudChannelV1ListTransferableSkusResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsRegister"] = cloudchannel.post(
        "v1/{parent}:listTransferableSkus",
        t.struct(
            {
                "parent": t.string(),
                "languageCode": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "cloudIdentityId": t.string().optional(),
                "customerName": t.string().optional(),
                "authToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudChannelV1ListTransferableSkusResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsUnregister"] = cloudchannel.post(
        "v1/{parent}:listTransferableSkus",
        t.struct(
            {
                "parent": t.string(),
                "languageCode": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "cloudIdentityId": t.string().optional(),
                "customerName": t.string().optional(),
                "authToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudChannelV1ListTransferableSkusResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsListTransferableOffers"] = cloudchannel.post(
        "v1/{parent}:listTransferableSkus",
        t.struct(
            {
                "parent": t.string(),
                "languageCode": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "cloudIdentityId": t.string().optional(),
                "customerName": t.string().optional(),
                "authToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudChannelV1ListTransferableSkusResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsListSubscribers"] = cloudchannel.post(
        "v1/{parent}:listTransferableSkus",
        t.struct(
            {
                "parent": t.string(),
                "languageCode": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "cloudIdentityId": t.string().optional(),
                "customerName": t.string().optional(),
                "authToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudChannelV1ListTransferableSkusResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsListTransferableSkus"] = cloudchannel.post(
        "v1/{parent}:listTransferableSkus",
        t.struct(
            {
                "parent": t.string(),
                "languageCode": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "cloudIdentityId": t.string().optional(),
                "customerName": t.string().optional(),
                "authToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudChannelV1ListTransferableSkusResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCustomersCreate"] = cloudchannel.post(
        "v1/{parent}:transferEntitlementsToGoogle",
        t.struct(
            {
                "parent": t.string(),
                "entitlements": t.array(
                    t.proxy(renames["GoogleCloudChannelV1EntitlementIn"])
                ),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCustomersListPurchasableSkus"] = cloudchannel.post(
        "v1/{parent}:transferEntitlementsToGoogle",
        t.struct(
            {
                "parent": t.string(),
                "entitlements": t.array(
                    t.proxy(renames["GoogleCloudChannelV1EntitlementIn"])
                ),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCustomersPatch"] = cloudchannel.post(
        "v1/{parent}:transferEntitlementsToGoogle",
        t.struct(
            {
                "parent": t.string(),
                "entitlements": t.array(
                    t.proxy(renames["GoogleCloudChannelV1EntitlementIn"])
                ),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCustomersListPurchasableOffers"] = cloudchannel.post(
        "v1/{parent}:transferEntitlementsToGoogle",
        t.struct(
            {
                "parent": t.string(),
                "entitlements": t.array(
                    t.proxy(renames["GoogleCloudChannelV1EntitlementIn"])
                ),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCustomersGet"] = cloudchannel.post(
        "v1/{parent}:transferEntitlementsToGoogle",
        t.struct(
            {
                "parent": t.string(),
                "entitlements": t.array(
                    t.proxy(renames["GoogleCloudChannelV1EntitlementIn"])
                ),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCustomersList"] = cloudchannel.post(
        "v1/{parent}:transferEntitlementsToGoogle",
        t.struct(
            {
                "parent": t.string(),
                "entitlements": t.array(
                    t.proxy(renames["GoogleCloudChannelV1EntitlementIn"])
                ),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCustomersQueryEligibleBillingAccounts"] = cloudchannel.post(
        "v1/{parent}:transferEntitlementsToGoogle",
        t.struct(
            {
                "parent": t.string(),
                "entitlements": t.array(
                    t.proxy(renames["GoogleCloudChannelV1EntitlementIn"])
                ),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCustomersTransferEntitlements"] = cloudchannel.post(
        "v1/{parent}:transferEntitlementsToGoogle",
        t.struct(
            {
                "parent": t.string(),
                "entitlements": t.array(
                    t.proxy(renames["GoogleCloudChannelV1EntitlementIn"])
                ),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCustomersImport"] = cloudchannel.post(
        "v1/{parent}:transferEntitlementsToGoogle",
        t.struct(
            {
                "parent": t.string(),
                "entitlements": t.array(
                    t.proxy(renames["GoogleCloudChannelV1EntitlementIn"])
                ),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCustomersProvisionCloudIdentity"] = cloudchannel.post(
        "v1/{parent}:transferEntitlementsToGoogle",
        t.struct(
            {
                "parent": t.string(),
                "entitlements": t.array(
                    t.proxy(renames["GoogleCloudChannelV1EntitlementIn"])
                ),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCustomersDelete"] = cloudchannel.post(
        "v1/{parent}:transferEntitlementsToGoogle",
        t.struct(
            {
                "parent": t.string(),
                "entitlements": t.array(
                    t.proxy(renames["GoogleCloudChannelV1EntitlementIn"])
                ),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCustomersTransferEntitlementsToGoogle"] = cloudchannel.post(
        "v1/{parent}:transferEntitlementsToGoogle",
        t.struct(
            {
                "parent": t.string(),
                "entitlements": t.array(
                    t.proxy(renames["GoogleCloudChannelV1EntitlementIn"])
                ),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCustomersCustomerRepricingConfigsDelete"] = cloudchannel.post(
        "v1/{parent}/customerRepricingConfigs",
        t.struct(
            {
                "parent": t.string(),
                "repricingConfig": t.proxy(
                    renames["GoogleCloudChannelV1RepricingConfigIn"]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudChannelV1CustomerRepricingConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCustomersCustomerRepricingConfigsList"] = cloudchannel.post(
        "v1/{parent}/customerRepricingConfigs",
        t.struct(
            {
                "parent": t.string(),
                "repricingConfig": t.proxy(
                    renames["GoogleCloudChannelV1RepricingConfigIn"]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudChannelV1CustomerRepricingConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCustomersCustomerRepricingConfigsGet"] = cloudchannel.post(
        "v1/{parent}/customerRepricingConfigs",
        t.struct(
            {
                "parent": t.string(),
                "repricingConfig": t.proxy(
                    renames["GoogleCloudChannelV1RepricingConfigIn"]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudChannelV1CustomerRepricingConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCustomersCustomerRepricingConfigsPatch"] = cloudchannel.post(
        "v1/{parent}/customerRepricingConfigs",
        t.struct(
            {
                "parent": t.string(),
                "repricingConfig": t.proxy(
                    renames["GoogleCloudChannelV1RepricingConfigIn"]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudChannelV1CustomerRepricingConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCustomersCustomerRepricingConfigsCreate"] = cloudchannel.post(
        "v1/{parent}/customerRepricingConfigs",
        t.struct(
            {
                "parent": t.string(),
                "repricingConfig": t.proxy(
                    renames["GoogleCloudChannelV1RepricingConfigIn"]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudChannelV1CustomerRepricingConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCustomersEntitlementsList"] = cloudchannel.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudChannelV1EntitlementOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCustomersEntitlementsListEntitlementChanges"] = cloudchannel.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudChannelV1EntitlementOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCustomersEntitlementsLookupOffer"] = cloudchannel.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudChannelV1EntitlementOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCustomersEntitlementsStartPaidService"] = cloudchannel.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudChannelV1EntitlementOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCustomersEntitlementsCancel"] = cloudchannel.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudChannelV1EntitlementOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCustomersEntitlementsChangeParameters"] = cloudchannel.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudChannelV1EntitlementOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCustomersEntitlementsChangeRenewalSettings"] = cloudchannel.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudChannelV1EntitlementOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCustomersEntitlementsSuspend"] = cloudchannel.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudChannelV1EntitlementOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCustomersEntitlementsChangeOffer"] = cloudchannel.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudChannelV1EntitlementOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCustomersEntitlementsCreate"] = cloudchannel.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudChannelV1EntitlementOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCustomersEntitlementsActivate"] = cloudchannel.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudChannelV1EntitlementOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCustomersEntitlementsGet"] = cloudchannel.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudChannelV1EntitlementOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsOffersList"] = cloudchannel.get(
        "v1/{parent}/offers",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "showFutureOffers": t.boolean().optional(),
                "languageCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudChannelV1ListOffersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsReportJobsFetchReportResults"] = cloudchannel.post(
        "v1/{reportJob}:fetchReportResults",
        t.struct(
            {
                "reportJob": t.string(),
                "pageSize": t.integer().optional(),
                "partitionKeys": t.array(t.string()).optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudChannelV1FetchReportResultsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsReportsRun"] = cloudchannel.get(
        "v1/{parent}/reports",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "languageCode": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudChannelV1ListReportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsReportsList"] = cloudchannel.get(
        "v1/{parent}/reports",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "languageCode": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudChannelV1ListReportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsChannelPartnerLinksCreate"] = cloudchannel.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudChannelV1ChannelPartnerLinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsChannelPartnerLinksList"] = cloudchannel.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudChannelV1ChannelPartnerLinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsChannelPartnerLinksPatch"] = cloudchannel.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudChannelV1ChannelPartnerLinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsChannelPartnerLinksGet"] = cloudchannel.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudChannelV1ChannelPartnerLinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "accountsChannelPartnerLinksChannelPartnerRepricingConfigsPatch"
    ] = cloudchannel.post(
        "v1/{parent}/channelPartnerRepricingConfigs",
        t.struct(
            {
                "parent": t.string(),
                "repricingConfig": t.proxy(
                    renames["GoogleCloudChannelV1RepricingConfigIn"]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudChannelV1ChannelPartnerRepricingConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "accountsChannelPartnerLinksChannelPartnerRepricingConfigsList"
    ] = cloudchannel.post(
        "v1/{parent}/channelPartnerRepricingConfigs",
        t.struct(
            {
                "parent": t.string(),
                "repricingConfig": t.proxy(
                    renames["GoogleCloudChannelV1RepricingConfigIn"]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudChannelV1ChannelPartnerRepricingConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "accountsChannelPartnerLinksChannelPartnerRepricingConfigsDelete"
    ] = cloudchannel.post(
        "v1/{parent}/channelPartnerRepricingConfigs",
        t.struct(
            {
                "parent": t.string(),
                "repricingConfig": t.proxy(
                    renames["GoogleCloudChannelV1RepricingConfigIn"]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudChannelV1ChannelPartnerRepricingConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "accountsChannelPartnerLinksChannelPartnerRepricingConfigsGet"
    ] = cloudchannel.post(
        "v1/{parent}/channelPartnerRepricingConfigs",
        t.struct(
            {
                "parent": t.string(),
                "repricingConfig": t.proxy(
                    renames["GoogleCloudChannelV1RepricingConfigIn"]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudChannelV1ChannelPartnerRepricingConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "accountsChannelPartnerLinksChannelPartnerRepricingConfigsCreate"
    ] = cloudchannel.post(
        "v1/{parent}/channelPartnerRepricingConfigs",
        t.struct(
            {
                "parent": t.string(),
                "repricingConfig": t.proxy(
                    renames["GoogleCloudChannelV1RepricingConfigIn"]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudChannelV1ChannelPartnerRepricingConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsChannelPartnerLinksCustomersCreate"] = cloudchannel.get(
        "v1/{parent}/customers",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudChannelV1ListCustomersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsChannelPartnerLinksCustomersGet"] = cloudchannel.get(
        "v1/{parent}/customers",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudChannelV1ListCustomersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsChannelPartnerLinksCustomersPatch"] = cloudchannel.get(
        "v1/{parent}/customers",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudChannelV1ListCustomersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsChannelPartnerLinksCustomersImport"] = cloudchannel.get(
        "v1/{parent}/customers",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudChannelV1ListCustomersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsChannelPartnerLinksCustomersDelete"] = cloudchannel.get(
        "v1/{parent}/customers",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudChannelV1ListCustomersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsChannelPartnerLinksCustomersList"] = cloudchannel.get(
        "v1/{parent}/customers",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudChannelV1ListCustomersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["productsList"] = cloudchannel.get(
        "v1/products",
        t.struct(
            {
                "languageCode": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "account": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudChannelV1ListProductsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["productsSkusList"] = cloudchannel.get(
        "v1/{parent}/skus",
        t.struct(
            {
                "languageCode": t.string().optional(),
                "pageToken": t.string().optional(),
                "account": t.string(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudChannelV1ListSkusResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsDelete"] = cloudchannel.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsCancel"] = cloudchannel.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsGet"] = cloudchannel.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsList"] = cloudchannel.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="cloudchannel",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
