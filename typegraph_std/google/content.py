from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_content():
    content = HTTPRuntime("https://shoppingcontent.googleapis.com/")

    renames = {
        "ErrorResponse": "_content_1_ErrorResponse",
        "ProductTaxIn": "_content_2_ProductTaxIn",
        "ProductTaxOut": "_content_3_ProductTaxOut",
        "ServiceIn": "_content_4_ServiceIn",
        "ServiceOut": "_content_5_ServiceOut",
        "OrdersSetLineItemMetadataResponseIn": "_content_6_OrdersSetLineItemMetadataResponseIn",
        "OrdersSetLineItemMetadataResponseOut": "_content_7_OrdersSetLineItemMetadataResponseOut",
        "OrdersRefundOrderResponseIn": "_content_8_OrdersRefundOrderResponseIn",
        "OrdersRefundOrderResponseOut": "_content_9_OrdersRefundOrderResponseOut",
        "UnitInvoiceAdditionalChargeIn": "_content_10_UnitInvoiceAdditionalChargeIn",
        "UnitInvoiceAdditionalChargeOut": "_content_11_UnitInvoiceAdditionalChargeOut",
        "AccountsUpdateLabelsRequestIn": "_content_12_AccountsUpdateLabelsRequestIn",
        "AccountsUpdateLabelsRequestOut": "_content_13_AccountsUpdateLabelsRequestOut",
        "CollectionIn": "_content_14_CollectionIn",
        "CollectionOut": "_content_15_CollectionOut",
        "RepricingRuleCostOfGoodsSaleRuleIn": "_content_16_RepricingRuleCostOfGoodsSaleRuleIn",
        "RepricingRuleCostOfGoodsSaleRuleOut": "_content_17_RepricingRuleCostOfGoodsSaleRuleOut",
        "PosSaleIn": "_content_18_PosSaleIn",
        "PosSaleOut": "_content_19_PosSaleOut",
        "CollectionStatusItemLevelIssueIn": "_content_20_CollectionStatusItemLevelIssueIn",
        "CollectionStatusItemLevelIssueOut": "_content_21_CollectionStatusItemLevelIssueOut",
        "RepricingRuleEligibleOfferMatcherIn": "_content_22_RepricingRuleEligibleOfferMatcherIn",
        "RepricingRuleEligibleOfferMatcherOut": "_content_23_RepricingRuleEligibleOfferMatcherOut",
        "OrderreturnsPartialRefundIn": "_content_24_OrderreturnsPartialRefundIn",
        "OrderreturnsPartialRefundOut": "_content_25_OrderreturnsPartialRefundOut",
        "FreeListingsProgramStatusRegionStatusIn": "_content_26_FreeListingsProgramStatusRegionStatusIn",
        "FreeListingsProgramStatusRegionStatusOut": "_content_27_FreeListingsProgramStatusRegionStatusOut",
        "OrderReturnIn": "_content_28_OrderReturnIn",
        "OrderReturnOut": "_content_29_OrderReturnOut",
        "ProductStatusDestinationStatusIn": "_content_30_ProductStatusDestinationStatusIn",
        "ProductStatusDestinationStatusOut": "_content_31_ProductStatusDestinationStatusOut",
        "ProductViewItemIssueIssueSeverityPerDestinationIn": "_content_32_ProductViewItemIssueIssueSeverityPerDestinationIn",
        "ProductViewItemIssueIssueSeverityPerDestinationOut": "_content_33_ProductViewItemIssueIssueSeverityPerDestinationOut",
        "ListCollectionStatusesResponseIn": "_content_34_ListCollectionStatusesResponseIn",
        "ListCollectionStatusesResponseOut": "_content_35_ListCollectionStatusesResponseOut",
        "ReturnPolicyOnlineReturnReasonCategoryInfoIn": "_content_36_ReturnPolicyOnlineReturnReasonCategoryInfoIn",
        "ReturnPolicyOnlineReturnReasonCategoryInfoOut": "_content_37_ReturnPolicyOnlineReturnReasonCategoryInfoOut",
        "OrdersCreateTestOrderRequestIn": "_content_38_OrdersCreateTestOrderRequestIn",
        "OrdersCreateTestOrderRequestOut": "_content_39_OrdersCreateTestOrderRequestOut",
        "OrdersUpdateLineItemShippingDetailsRequestIn": "_content_40_OrdersUpdateLineItemShippingDetailsRequestIn",
        "OrdersUpdateLineItemShippingDetailsRequestOut": "_content_41_OrdersUpdateLineItemShippingDetailsRequestOut",
        "CaptureOrderResponseIn": "_content_42_CaptureOrderResponseIn",
        "CaptureOrderResponseOut": "_content_43_CaptureOrderResponseOut",
        "MerchantOrderReturnIn": "_content_44_MerchantOrderReturnIn",
        "MerchantOrderReturnOut": "_content_45_MerchantOrderReturnOut",
        "SettlementTransactionAmountCommissionIn": "_content_46_SettlementTransactionAmountCommissionIn",
        "SettlementTransactionAmountCommissionOut": "_content_47_SettlementTransactionAmountCommissionOut",
        "OrdersShipLineItemsResponseIn": "_content_48_OrdersShipLineItemsResponseIn",
        "OrdersShipLineItemsResponseOut": "_content_49_OrdersShipLineItemsResponseOut",
        "ProductstatusesCustomBatchRequestIn": "_content_50_ProductstatusesCustomBatchRequestIn",
        "ProductstatusesCustomBatchRequestOut": "_content_51_ProductstatusesCustomBatchRequestOut",
        "PosDataProvidersPosDataProviderIn": "_content_52_PosDataProvidersPosDataProviderIn",
        "PosDataProvidersPosDataProviderOut": "_content_53_PosDataProvidersPosDataProviderOut",
        "OrderreturnsRefundOperationIn": "_content_54_OrderreturnsRefundOperationIn",
        "OrderreturnsRefundOperationOut": "_content_55_OrderreturnsRefundOperationOut",
        "OrderreturnsCreateOrderReturnRequestIn": "_content_56_OrderreturnsCreateOrderReturnRequestIn",
        "OrderreturnsCreateOrderReturnRequestOut": "_content_57_OrderreturnsCreateOrderReturnRequestOut",
        "AccountstatusesCustomBatchResponseIn": "_content_58_AccountstatusesCustomBatchResponseIn",
        "AccountstatusesCustomBatchResponseOut": "_content_59_AccountstatusesCustomBatchResponseOut",
        "OrderIn": "_content_60_OrderIn",
        "OrderOut": "_content_61_OrderOut",
        "ReturnPolicyOnlineIn": "_content_62_ReturnPolicyOnlineIn",
        "ReturnPolicyOnlineOut": "_content_63_ReturnPolicyOnlineOut",
        "PromotionPromotionStatusPromotionIssueIn": "_content_64_PromotionPromotionStatusPromotionIssueIn",
        "PromotionPromotionStatusPromotionIssueOut": "_content_65_PromotionPromotionStatusPromotionIssueOut",
        "SettlementtransactionsListResponseIn": "_content_66_SettlementtransactionsListResponseIn",
        "SettlementtransactionsListResponseOut": "_content_67_SettlementtransactionsListResponseOut",
        "AccountstatusesCustomBatchRequestEntryIn": "_content_68_AccountstatusesCustomBatchRequestEntryIn",
        "AccountstatusesCustomBatchRequestEntryOut": "_content_69_AccountstatusesCustomBatchRequestEntryOut",
        "ReturnpolicyListResponseIn": "_content_70_ReturnpolicyListResponseIn",
        "ReturnpolicyListResponseOut": "_content_71_ReturnpolicyListResponseOut",
        "PosDataProvidersIn": "_content_72_PosDataProvidersIn",
        "PosDataProvidersOut": "_content_73_PosDataProvidersOut",
        "AccountAdsLinkIn": "_content_74_AccountAdsLinkIn",
        "AccountAdsLinkOut": "_content_75_AccountAdsLinkOut",
        "GenerateRecommendationsResponseIn": "_content_76_GenerateRecommendationsResponseIn",
        "GenerateRecommendationsResponseOut": "_content_77_GenerateRecommendationsResponseOut",
        "ShoppingAdsProgramStatusIn": "_content_78_ShoppingAdsProgramStatusIn",
        "ShoppingAdsProgramStatusOut": "_content_79_ShoppingAdsProgramStatusOut",
        "LiasettingsSetInventoryVerificationContactResponseIn": "_content_80_LiasettingsSetInventoryVerificationContactResponseIn",
        "LiasettingsSetInventoryVerificationContactResponseOut": "_content_81_LiasettingsSetInventoryVerificationContactResponseOut",
        "OrdersCustomBatchRequestEntryShipLineItemsShipmentInfoIn": "_content_82_OrdersCustomBatchRequestEntryShipLineItemsShipmentInfoIn",
        "OrdersCustomBatchRequestEntryShipLineItemsShipmentInfoOut": "_content_83_OrdersCustomBatchRequestEntryShipLineItemsShipmentInfoOut",
        "RecommendationIn": "_content_84_RecommendationIn",
        "RecommendationOut": "_content_85_RecommendationOut",
        "ProductstatusesCustomBatchRequestEntryIn": "_content_86_ProductstatusesCustomBatchRequestEntryIn",
        "ProductstatusesCustomBatchRequestEntryOut": "_content_87_ProductstatusesCustomBatchRequestEntryOut",
        "OrdersCustomBatchRequestEntryCreateTestReturnReturnItemIn": "_content_88_OrdersCustomBatchRequestEntryCreateTestReturnReturnItemIn",
        "OrdersCustomBatchRequestEntryCreateTestReturnReturnItemOut": "_content_89_OrdersCustomBatchRequestEntryCreateTestReturnReturnItemOut",
        "RegionPostalCodeAreaPostalCodeRangeIn": "_content_90_RegionPostalCodeAreaPostalCodeRangeIn",
        "RegionPostalCodeAreaPostalCodeRangeOut": "_content_91_RegionPostalCodeAreaPostalCodeRangeOut",
        "MethodQuotaIn": "_content_92_MethodQuotaIn",
        "MethodQuotaOut": "_content_93_MethodQuotaOut",
        "ProductUnitPricingMeasureIn": "_content_94_ProductUnitPricingMeasureIn",
        "ProductUnitPricingMeasureOut": "_content_95_ProductUnitPricingMeasureOut",
        "DatafeedsCustomBatchResponseIn": "_content_96_DatafeedsCustomBatchResponseIn",
        "DatafeedsCustomBatchResponseOut": "_content_97_DatafeedsCustomBatchResponseOut",
        "CollectionFeaturedProductIn": "_content_98_CollectionFeaturedProductIn",
        "CollectionFeaturedProductOut": "_content_99_CollectionFeaturedProductOut",
        "OrderreturnsProcessResponseIn": "_content_100_OrderreturnsProcessResponseIn",
        "OrderreturnsProcessResponseOut": "_content_101_OrderreturnsProcessResponseOut",
        "ShippingsettingsCustomBatchResponseEntryIn": "_content_102_ShippingsettingsCustomBatchResponseEntryIn",
        "ShippingsettingsCustomBatchResponseEntryOut": "_content_103_ShippingsettingsCustomBatchResponseEntryOut",
        "DatafeedsCustomBatchRequestIn": "_content_104_DatafeedsCustomBatchRequestIn",
        "DatafeedsCustomBatchRequestOut": "_content_105_DatafeedsCustomBatchRequestOut",
        "AccountstatusesCustomBatchResponseEntryIn": "_content_106_AccountstatusesCustomBatchResponseEntryIn",
        "AccountstatusesCustomBatchResponseEntryOut": "_content_107_AccountstatusesCustomBatchResponseEntryOut",
        "RepricingRuleIn": "_content_108_RepricingRuleIn",
        "RepricingRuleOut": "_content_109_RepricingRuleOut",
        "ShipmentInvoiceIn": "_content_110_ShipmentInvoiceIn",
        "ShipmentInvoiceOut": "_content_111_ShipmentInvoiceOut",
        "FreeListingsProgramStatusIn": "_content_112_FreeListingsProgramStatusIn",
        "FreeListingsProgramStatusOut": "_content_113_FreeListingsProgramStatusOut",
        "BestSellersIn": "_content_114_BestSellersIn",
        "BestSellersOut": "_content_115_BestSellersOut",
        "PostalCodeRangeIn": "_content_116_PostalCodeRangeIn",
        "PostalCodeRangeOut": "_content_117_PostalCodeRangeOut",
        "OrderLineItemShippingDetailsIn": "_content_118_OrderLineItemShippingDetailsIn",
        "OrderLineItemShippingDetailsOut": "_content_119_OrderLineItemShippingDetailsOut",
        "TestOrderPickupDetailsPickupPersonIn": "_content_120_TestOrderPickupDetailsPickupPersonIn",
        "TestOrderPickupDetailsPickupPersonOut": "_content_121_TestOrderPickupDetailsPickupPersonOut",
        "AccountsClaimWebsiteResponseIn": "_content_122_AccountsClaimWebsiteResponseIn",
        "AccountsClaimWebsiteResponseOut": "_content_123_AccountsClaimWebsiteResponseOut",
        "SearchResponseIn": "_content_124_SearchResponseIn",
        "SearchResponseOut": "_content_125_SearchResponseOut",
        "LiasettingsListResponseIn": "_content_126_LiasettingsListResponseIn",
        "LiasettingsListResponseOut": "_content_127_LiasettingsListResponseOut",
        "SettlementTransactionIdentifiersIn": "_content_128_SettlementTransactionIdentifiersIn",
        "SettlementTransactionIdentifiersOut": "_content_129_SettlementTransactionIdentifiersOut",
        "OrdersCancelLineItemRequestIn": "_content_130_OrdersCancelLineItemRequestIn",
        "OrdersCancelLineItemRequestOut": "_content_131_OrdersCancelLineItemRequestOut",
        "ProductstatusesCustomBatchResponseEntryIn": "_content_132_ProductstatusesCustomBatchResponseEntryIn",
        "ProductstatusesCustomBatchResponseEntryOut": "_content_133_ProductstatusesCustomBatchResponseEntryOut",
        "PickupServicesPickupServiceIn": "_content_134_PickupServicesPickupServiceIn",
        "PickupServicesPickupServiceOut": "_content_135_PickupServicesPickupServiceOut",
        "ReturnaddressCustomBatchRequestIn": "_content_136_ReturnaddressCustomBatchRequestIn",
        "ReturnaddressCustomBatchRequestOut": "_content_137_ReturnaddressCustomBatchRequestOut",
        "BusinessDayConfigIn": "_content_138_BusinessDayConfigIn",
        "BusinessDayConfigOut": "_content_139_BusinessDayConfigOut",
        "WarehouseCutoffTimeIn": "_content_140_WarehouseCutoffTimeIn",
        "WarehouseCutoffTimeOut": "_content_141_WarehouseCutoffTimeOut",
        "ActivateBuyOnGoogleProgramRequestIn": "_content_142_ActivateBuyOnGoogleProgramRequestIn",
        "ActivateBuyOnGoogleProgramRequestOut": "_content_143_ActivateBuyOnGoogleProgramRequestOut",
        "PubsubNotificationSettingsIn": "_content_144_PubsubNotificationSettingsIn",
        "PubsubNotificationSettingsOut": "_content_145_PubsubNotificationSettingsOut",
        "RepricingRuleReportIn": "_content_146_RepricingRuleReportIn",
        "RepricingRuleReportOut": "_content_147_RepricingRuleReportOut",
        "LiaCountrySettingsIn": "_content_148_LiaCountrySettingsIn",
        "LiaCountrySettingsOut": "_content_149_LiaCountrySettingsOut",
        "CollectionStatusIn": "_content_150_CollectionStatusIn",
        "CollectionStatusOut": "_content_151_CollectionStatusOut",
        "CustomerReturnReasonIn": "_content_152_CustomerReturnReasonIn",
        "CustomerReturnReasonOut": "_content_153_CustomerReturnReasonOut",
        "OrderReportDisbursementIn": "_content_154_OrderReportDisbursementIn",
        "OrderReportDisbursementOut": "_content_155_OrderReportDisbursementOut",
        "OrderTrackingSignalShippingInfoIn": "_content_156_OrderTrackingSignalShippingInfoIn",
        "OrderTrackingSignalShippingInfoOut": "_content_157_OrderTrackingSignalShippingInfoOut",
        "ECommercePlatformLinkInfoIn": "_content_158_ECommercePlatformLinkInfoIn",
        "ECommercePlatformLinkInfoOut": "_content_159_ECommercePlatformLinkInfoOut",
        "RegionGeoTargetAreaIn": "_content_160_RegionGeoTargetAreaIn",
        "RegionGeoTargetAreaOut": "_content_161_RegionGeoTargetAreaOut",
        "DeliveryAreaIn": "_content_162_DeliveryAreaIn",
        "DeliveryAreaOut": "_content_163_DeliveryAreaOut",
        "ProductWeightIn": "_content_164_ProductWeightIn",
        "ProductWeightOut": "_content_165_ProductWeightOut",
        "PosInventoryIn": "_content_166_PosInventoryIn",
        "PosInventoryOut": "_content_167_PosInventoryOut",
        "OrderAddressIn": "_content_168_OrderAddressIn",
        "OrderAddressOut": "_content_169_OrderAddressOut",
        "OrdersRefundItemRequestIn": "_content_170_OrdersRefundItemRequestIn",
        "OrdersRefundItemRequestOut": "_content_171_OrdersRefundItemRequestOut",
        "ReturnpolicyCustomBatchResponseEntryIn": "_content_172_ReturnpolicyCustomBatchResponseEntryIn",
        "ReturnpolicyCustomBatchResponseEntryOut": "_content_173_ReturnpolicyCustomBatchResponseEntryOut",
        "TestOrderDeliveryDetailsIn": "_content_174_TestOrderDeliveryDetailsIn",
        "TestOrderDeliveryDetailsOut": "_content_175_TestOrderDeliveryDetailsOut",
        "AccountBusinessInformationIn": "_content_176_AccountBusinessInformationIn",
        "AccountBusinessInformationOut": "_content_177_AccountBusinessInformationOut",
        "RepricingRuleStatsBasedRuleIn": "_content_178_RepricingRuleStatsBasedRuleIn",
        "RepricingRuleStatsBasedRuleOut": "_content_179_RepricingRuleStatsBasedRuleOut",
        "OrderLineItemProductFeeIn": "_content_180_OrderLineItemProductFeeIn",
        "OrderLineItemProductFeeOut": "_content_181_OrderLineItemProductFeeOut",
        "MinimumOrderValueTableStoreCodeSetWithMovIn": "_content_182_MinimumOrderValueTableStoreCodeSetWithMovIn",
        "MinimumOrderValueTableStoreCodeSetWithMovOut": "_content_183_MinimumOrderValueTableStoreCodeSetWithMovOut",
        "ShipmentTrackingInfoIn": "_content_184_ShipmentTrackingInfoIn",
        "ShipmentTrackingInfoOut": "_content_185_ShipmentTrackingInfoOut",
        "OrdersCreateTestOrderResponseIn": "_content_186_OrdersCreateTestOrderResponseIn",
        "OrdersCreateTestOrderResponseOut": "_content_187_OrdersCreateTestOrderResponseOut",
        "PosInventoryResponseIn": "_content_188_PosInventoryResponseIn",
        "PosInventoryResponseOut": "_content_189_PosInventoryResponseOut",
        "LiasettingsRequestGmbAccessResponseIn": "_content_190_LiasettingsRequestGmbAccessResponseIn",
        "LiasettingsRequestGmbAccessResponseOut": "_content_191_LiasettingsRequestGmbAccessResponseOut",
        "AccountsCustomBatchResponseEntryIn": "_content_192_AccountsCustomBatchResponseEntryIn",
        "AccountsCustomBatchResponseEntryOut": "_content_193_AccountsCustomBatchResponseEntryOut",
        "PromotionIn": "_content_194_PromotionIn",
        "PromotionOut": "_content_195_PromotionOut",
        "OrderPromotionIn": "_content_196_OrderPromotionIn",
        "OrderPromotionOut": "_content_197_OrderPromotionOut",
        "PosCustomBatchResponseEntryIn": "_content_198_PosCustomBatchResponseEntryIn",
        "PosCustomBatchResponseEntryOut": "_content_199_PosCustomBatchResponseEntryOut",
        "AccounttaxCustomBatchResponseEntryIn": "_content_200_AccounttaxCustomBatchResponseEntryIn",
        "AccounttaxCustomBatchResponseEntryOut": "_content_201_AccounttaxCustomBatchResponseEntryOut",
        "ServiceStoreConfigIn": "_content_202_ServiceStoreConfigIn",
        "ServiceStoreConfigOut": "_content_203_ServiceStoreConfigOut",
        "RequestReviewShoppingAdsRequestIn": "_content_204_RequestReviewShoppingAdsRequestIn",
        "RequestReviewShoppingAdsRequestOut": "_content_205_RequestReviewShoppingAdsRequestOut",
        "AccountConversionSettingsIn": "_content_206_AccountConversionSettingsIn",
        "AccountConversionSettingsOut": "_content_207_AccountConversionSettingsOut",
        "AccountAddressIn": "_content_208_AccountAddressIn",
        "AccountAddressOut": "_content_209_AccountAddressOut",
        "RegionPostalCodeAreaIn": "_content_210_RegionPostalCodeAreaIn",
        "RegionPostalCodeAreaOut": "_content_211_RegionPostalCodeAreaOut",
        "RegionalinventoryCustomBatchResponseEntryIn": "_content_212_RegionalinventoryCustomBatchResponseEntryIn",
        "RegionalinventoryCustomBatchResponseEntryOut": "_content_213_RegionalinventoryCustomBatchResponseEntryOut",
        "AccountCustomerServiceIn": "_content_214_AccountCustomerServiceIn",
        "AccountCustomerServiceOut": "_content_215_AccountCustomerServiceOut",
        "GmbAccountsGmbAccountIn": "_content_216_GmbAccountsGmbAccountIn",
        "GmbAccountsGmbAccountOut": "_content_217_GmbAccountsGmbAccountOut",
        "OrdersListResponseIn": "_content_218_OrdersListResponseIn",
        "OrdersListResponseOut": "_content_219_OrdersListResponseOut",
        "ListRepricingRuleReportsResponseIn": "_content_220_ListRepricingRuleReportsResponseIn",
        "ListRepricingRuleReportsResponseOut": "_content_221_ListRepricingRuleReportsResponseOut",
        "HeadersIn": "_content_222_HeadersIn",
        "HeadersOut": "_content_223_HeadersOut",
        "OrdersCancelTestOrderByCustomerRequestIn": "_content_224_OrdersCancelTestOrderByCustomerRequestIn",
        "OrdersCancelTestOrderByCustomerRequestOut": "_content_225_OrdersCancelTestOrderByCustomerRequestOut",
        "AccountTaxTaxRuleIn": "_content_226_AccountTaxTaxRuleIn",
        "AccountTaxTaxRuleOut": "_content_227_AccountTaxTaxRuleOut",
        "OrderOrderAnnotationIn": "_content_228_OrderOrderAnnotationIn",
        "OrderOrderAnnotationOut": "_content_229_OrderOrderAnnotationOut",
        "ValueIn": "_content_230_ValueIn",
        "ValueOut": "_content_231_ValueOut",
        "DatafeedsCustomBatchResponseEntryIn": "_content_232_DatafeedsCustomBatchResponseEntryIn",
        "DatafeedsCustomBatchResponseEntryOut": "_content_233_DatafeedsCustomBatchResponseEntryOut",
        "ShippingsettingsCustomBatchRequestEntryIn": "_content_234_ShippingsettingsCustomBatchRequestEntryIn",
        "ShippingsettingsCustomBatchRequestEntryOut": "_content_235_ShippingsettingsCustomBatchRequestEntryOut",
        "DeliveryAreaPostalCodeRangeIn": "_content_236_DeliveryAreaPostalCodeRangeIn",
        "DeliveryAreaPostalCodeRangeOut": "_content_237_DeliveryAreaPostalCodeRangeOut",
        "ProductUnitPricingBaseMeasureIn": "_content_238_ProductUnitPricingBaseMeasureIn",
        "ProductUnitPricingBaseMeasureOut": "_content_239_ProductUnitPricingBaseMeasureOut",
        "OrderDeliveryDetailsIn": "_content_240_OrderDeliveryDetailsIn",
        "OrderDeliveryDetailsOut": "_content_241_OrderDeliveryDetailsOut",
        "AttributionSettingsConversionTypeIn": "_content_242_AttributionSettingsConversionTypeIn",
        "AttributionSettingsConversionTypeOut": "_content_243_AttributionSettingsConversionTypeOut",
        "ProductsCustomBatchResponseEntryIn": "_content_244_ProductsCustomBatchResponseEntryIn",
        "ProductsCustomBatchResponseEntryOut": "_content_245_ProductsCustomBatchResponseEntryOut",
        "CollectionStatusDestinationStatusIn": "_content_246_CollectionStatusDestinationStatusIn",
        "CollectionStatusDestinationStatusOut": "_content_247_CollectionStatusDestinationStatusOut",
        "OrderShipmentLineItemShipmentIn": "_content_248_OrderShipmentLineItemShipmentIn",
        "OrderShipmentLineItemShipmentOut": "_content_249_OrderShipmentLineItemShipmentOut",
        "OrdersSetLineItemMetadataRequestIn": "_content_250_OrdersSetLineItemMetadataRequestIn",
        "OrdersSetLineItemMetadataRequestOut": "_content_251_OrdersSetLineItemMetadataRequestOut",
        "DatafeedStatusIn": "_content_252_DatafeedStatusIn",
        "DatafeedStatusOut": "_content_253_DatafeedStatusOut",
        "AttributionSettingsIn": "_content_254_AttributionSettingsIn",
        "AttributionSettingsOut": "_content_255_AttributionSettingsOut",
        "AccountStatusStatisticsIn": "_content_256_AccountStatusStatisticsIn",
        "AccountStatusStatisticsOut": "_content_257_AccountStatusStatisticsOut",
        "AccountsCustomBatchRequestEntryLinkRequestIn": "_content_258_AccountsCustomBatchRequestEntryLinkRequestIn",
        "AccountsCustomBatchRequestEntryLinkRequestOut": "_content_259_AccountsCustomBatchRequestEntryLinkRequestOut",
        "ReturnShipmentIn": "_content_260_ReturnShipmentIn",
        "ReturnShipmentOut": "_content_261_ReturnShipmentOut",
        "RegionalinventoryCustomBatchRequestIn": "_content_262_RegionalinventoryCustomBatchRequestIn",
        "RegionalinventoryCustomBatchRequestOut": "_content_263_RegionalinventoryCustomBatchRequestOut",
        "PaymentServiceProviderLinkInfoIn": "_content_264_PaymentServiceProviderLinkInfoIn",
        "PaymentServiceProviderLinkInfoOut": "_content_265_PaymentServiceProviderLinkInfoOut",
        "ShoppingAdsProgramStatusRegionStatusIn": "_content_266_ShoppingAdsProgramStatusRegionStatusIn",
        "ShoppingAdsProgramStatusRegionStatusOut": "_content_267_ShoppingAdsProgramStatusRegionStatusOut",
        "DistanceIn": "_content_268_DistanceIn",
        "DistanceOut": "_content_269_DistanceOut",
        "WarehouseIn": "_content_270_WarehouseIn",
        "WarehouseOut": "_content_271_WarehouseOut",
        "VerifyPhoneNumberRequestIn": "_content_272_VerifyPhoneNumberRequestIn",
        "VerifyPhoneNumberRequestOut": "_content_273_VerifyPhoneNumberRequestOut",
        "DeliveryTimeIn": "_content_274_DeliveryTimeIn",
        "DeliveryTimeOut": "_content_275_DeliveryTimeOut",
        "OrderShipmentScheduledDeliveryDetailsIn": "_content_276_OrderShipmentScheduledDeliveryDetailsIn",
        "OrderShipmentScheduledDeliveryDetailsOut": "_content_277_OrderShipmentScheduledDeliveryDetailsOut",
        "InvoiceSummaryIn": "_content_278_InvoiceSummaryIn",
        "InvoiceSummaryOut": "_content_279_InvoiceSummaryOut",
        "LinkServiceIn": "_content_280_LinkServiceIn",
        "LinkServiceOut": "_content_281_LinkServiceOut",
        "OrderReportTransactionIn": "_content_282_OrderReportTransactionIn",
        "OrderReportTransactionOut": "_content_283_OrderReportTransactionOut",
        "AccountsListResponseIn": "_content_284_AccountsListResponseIn",
        "AccountsListResponseOut": "_content_285_AccountsListResponseOut",
        "PosCustomBatchRequestEntryIn": "_content_286_PosCustomBatchRequestEntryIn",
        "PosCustomBatchRequestEntryOut": "_content_287_PosCustomBatchRequestEntryOut",
        "OrdersRefundItemResponseIn": "_content_288_OrdersRefundItemResponseIn",
        "OrdersRefundItemResponseOut": "_content_289_OrdersRefundItemResponseOut",
        "AccountsLinkRequestIn": "_content_290_AccountsLinkRequestIn",
        "AccountsLinkRequestOut": "_content_291_AccountsLinkRequestOut",
        "OrderCustomerMarketingRightsInfoIn": "_content_292_OrderCustomerMarketingRightsInfoIn",
        "OrderCustomerMarketingRightsInfoOut": "_content_293_OrderCustomerMarketingRightsInfoOut",
        "LinkedAccountIn": "_content_294_LinkedAccountIn",
        "LinkedAccountOut": "_content_295_LinkedAccountOut",
        "OrdersCancelResponseIn": "_content_296_OrdersCancelResponseIn",
        "OrdersCancelResponseOut": "_content_297_OrdersCancelResponseOut",
        "OrderinvoicesCustomBatchRequestEntryCreateRefundInvoiceReturnOptionIn": "_content_298_OrderinvoicesCustomBatchRequestEntryCreateRefundInvoiceReturnOptionIn",
        "OrderinvoicesCustomBatchRequestEntryCreateRefundInvoiceReturnOptionOut": "_content_299_OrderinvoicesCustomBatchRequestEntryCreateRefundInvoiceReturnOptionOut",
        "OrdersRefundOrderRequestIn": "_content_300_OrdersRefundOrderRequestIn",
        "OrdersRefundOrderRequestOut": "_content_301_OrdersRefundOrderRequestOut",
        "ListConversionSourcesResponseIn": "_content_302_ListConversionSourcesResponseIn",
        "ListConversionSourcesResponseOut": "_content_303_ListConversionSourcesResponseOut",
        "LocalinventoryCustomBatchRequestIn": "_content_304_LocalinventoryCustomBatchRequestIn",
        "LocalinventoryCustomBatchRequestOut": "_content_305_LocalinventoryCustomBatchRequestOut",
        "ProductDimensionIn": "_content_306_ProductDimensionIn",
        "ProductDimensionOut": "_content_307_ProductDimensionOut",
        "RegionIn": "_content_308_RegionIn",
        "RegionOut": "_content_309_RegionOut",
        "DatafeedstatusesCustomBatchRequestIn": "_content_310_DatafeedstatusesCustomBatchRequestIn",
        "DatafeedstatusesCustomBatchRequestOut": "_content_311_DatafeedstatusesCustomBatchRequestOut",
        "OrdersGetTestOrderTemplateResponseIn": "_content_312_OrdersGetTestOrderTemplateResponseIn",
        "OrdersGetTestOrderTemplateResponseOut": "_content_313_OrdersGetTestOrderTemplateResponseOut",
        "LocalinventoryCustomBatchRequestEntryIn": "_content_314_LocalinventoryCustomBatchRequestEntryIn",
        "LocalinventoryCustomBatchRequestEntryOut": "_content_315_LocalinventoryCustomBatchRequestEntryOut",
        "AccountstatusesCustomBatchRequestIn": "_content_316_AccountstatusesCustomBatchRequestIn",
        "AccountstatusesCustomBatchRequestOut": "_content_317_AccountstatusesCustomBatchRequestOut",
        "ProductViewItemIssueIn": "_content_318_ProductViewItemIssueIn",
        "ProductViewItemIssueOut": "_content_319_ProductViewItemIssueOut",
        "AccountIdentifierIn": "_content_320_AccountIdentifierIn",
        "AccountIdentifierOut": "_content_321_AccountIdentifierOut",
        "RepricingProductReportBuyboxWinningProductStatsIn": "_content_322_RepricingProductReportBuyboxWinningProductStatsIn",
        "RepricingProductReportBuyboxWinningProductStatsOut": "_content_323_RepricingProductReportBuyboxWinningProductStatsOut",
        "OrderreturnsProcessRequestIn": "_content_324_OrderreturnsProcessRequestIn",
        "OrderreturnsProcessRequestOut": "_content_325_OrderreturnsProcessRequestOut",
        "FreeListingsProgramStatusReviewIneligibilityReasonDetailsIn": "_content_326_FreeListingsProgramStatusReviewIneligibilityReasonDetailsIn",
        "FreeListingsProgramStatusReviewIneligibilityReasonDetailsOut": "_content_327_FreeListingsProgramStatusReviewIneligibilityReasonDetailsOut",
        "AccountItemUpdatesSettingsIn": "_content_328_AccountItemUpdatesSettingsIn",
        "AccountItemUpdatesSettingsOut": "_content_329_AccountItemUpdatesSettingsOut",
        "AccountReturnCarrierIn": "_content_330_AccountReturnCarrierIn",
        "AccountReturnCarrierOut": "_content_331_AccountReturnCarrierOut",
        "OrderLineItemProductIn": "_content_332_OrderLineItemProductIn",
        "OrderLineItemProductOut": "_content_333_OrderLineItemProductOut",
        "OrderreturnsAcknowledgeRequestIn": "_content_334_OrderreturnsAcknowledgeRequestIn",
        "OrderreturnsAcknowledgeRequestOut": "_content_335_OrderreturnsAcknowledgeRequestOut",
        "OrdersCustomBatchRequestEntryRefundItemItemIn": "_content_336_OrdersCustomBatchRequestEntryRefundItemItemIn",
        "OrdersCustomBatchRequestEntryRefundItemItemOut": "_content_337_OrdersCustomBatchRequestEntryRefundItemItemOut",
        "SegmentsIn": "_content_338_SegmentsIn",
        "SegmentsOut": "_content_339_SegmentsOut",
        "AccountStatusItemLevelIssueIn": "_content_340_AccountStatusItemLevelIssueIn",
        "AccountStatusItemLevelIssueOut": "_content_341_AccountStatusItemLevelIssueOut",
        "ConversionSourceIn": "_content_342_ConversionSourceIn",
        "ConversionSourceOut": "_content_343_ConversionSourceOut",
        "ReturnaddressCustomBatchResponseIn": "_content_344_ReturnaddressCustomBatchResponseIn",
        "ReturnaddressCustomBatchResponseOut": "_content_345_ReturnaddressCustomBatchResponseOut",
        "OrderLineItemReturnInfoIn": "_content_346_OrderLineItemReturnInfoIn",
        "OrderLineItemReturnInfoOut": "_content_347_OrderLineItemReturnInfoOut",
        "RepricingRuleReportBuyboxWinningRuleStatsIn": "_content_348_RepricingRuleReportBuyboxWinningRuleStatsIn",
        "RepricingRuleReportBuyboxWinningRuleStatsOut": "_content_349_RepricingRuleReportBuyboxWinningRuleStatsOut",
        "PosCustomBatchResponseIn": "_content_350_PosCustomBatchResponseIn",
        "PosCustomBatchResponseOut": "_content_351_PosCustomBatchResponseOut",
        "OrdersRejectReturnLineItemRequestIn": "_content_352_OrdersRejectReturnLineItemRequestIn",
        "OrdersRejectReturnLineItemRequestOut": "_content_353_OrdersRejectReturnLineItemRequestOut",
        "ProductsCustomBatchRequestIn": "_content_354_ProductsCustomBatchRequestIn",
        "ProductsCustomBatchRequestOut": "_content_355_ProductsCustomBatchRequestOut",
        "ShippingsettingsCustomBatchRequestIn": "_content_356_ShippingsettingsCustomBatchRequestIn",
        "ShippingsettingsCustomBatchRequestOut": "_content_357_ShippingsettingsCustomBatchRequestOut",
        "LiasettingsCustomBatchRequestIn": "_content_358_LiasettingsCustomBatchRequestIn",
        "LiasettingsCustomBatchRequestOut": "_content_359_LiasettingsCustomBatchRequestOut",
        "DatafeedstatusesCustomBatchResponseIn": "_content_360_DatafeedstatusesCustomBatchResponseIn",
        "DatafeedstatusesCustomBatchResponseOut": "_content_361_DatafeedstatusesCustomBatchResponseOut",
        "OrdersRejectReturnLineItemResponseIn": "_content_362_OrdersRejectReturnLineItemResponseIn",
        "OrdersRejectReturnLineItemResponseOut": "_content_363_OrdersRejectReturnLineItemResponseOut",
        "DatafeedsListResponseIn": "_content_364_DatafeedsListResponseIn",
        "DatafeedsListResponseOut": "_content_365_DatafeedsListResponseOut",
        "WeightIn": "_content_366_WeightIn",
        "WeightOut": "_content_367_WeightOut",
        "ShippingsettingsGetSupportedPickupServicesResponseIn": "_content_368_ShippingsettingsGetSupportedPickupServicesResponseIn",
        "ShippingsettingsGetSupportedPickupServicesResponseOut": "_content_369_ShippingsettingsGetSupportedPickupServicesResponseOut",
        "DatafeedFormatIn": "_content_370_DatafeedFormatIn",
        "DatafeedFormatOut": "_content_371_DatafeedFormatOut",
        "ReturnShippingLabelIn": "_content_372_ReturnShippingLabelIn",
        "ReturnShippingLabelOut": "_content_373_ReturnShippingLabelOut",
        "PickupCarrierServiceIn": "_content_374_PickupCarrierServiceIn",
        "PickupCarrierServiceOut": "_content_375_PickupCarrierServiceOut",
        "ReturnPricingInfoIn": "_content_376_ReturnPricingInfoIn",
        "ReturnPricingInfoOut": "_content_377_ReturnPricingInfoOut",
        "OrderreportsListDisbursementsResponseIn": "_content_378_OrderreportsListDisbursementsResponseIn",
        "OrderreportsListDisbursementsResponseOut": "_content_379_OrderreportsListDisbursementsResponseOut",
        "OrdersUpdateShipmentResponseIn": "_content_380_OrdersUpdateShipmentResponseIn",
        "OrdersUpdateShipmentResponseOut": "_content_381_OrdersUpdateShipmentResponseOut",
        "AccountsCustomBatchRequestIn": "_content_382_AccountsCustomBatchRequestIn",
        "AccountsCustomBatchRequestOut": "_content_383_AccountsCustomBatchRequestOut",
        "OrdersAdvanceTestOrderResponseIn": "_content_384_OrdersAdvanceTestOrderResponseIn",
        "OrdersAdvanceTestOrderResponseOut": "_content_385_OrdersAdvanceTestOrderResponseOut",
        "InvoiceSummaryAdditionalChargeSummaryIn": "_content_386_InvoiceSummaryAdditionalChargeSummaryIn",
        "InvoiceSummaryAdditionalChargeSummaryOut": "_content_387_InvoiceSummaryAdditionalChargeSummaryOut",
        "ShippingsettingsGetSupportedHolidaysResponseIn": "_content_388_ShippingsettingsGetSupportedHolidaysResponseIn",
        "ShippingsettingsGetSupportedHolidaysResponseOut": "_content_389_ShippingsettingsGetSupportedHolidaysResponseOut",
        "ReturnAddressIn": "_content_390_ReturnAddressIn",
        "ReturnAddressOut": "_content_391_ReturnAddressOut",
        "ListReturnPolicyOnlineResponseIn": "_content_392_ListReturnPolicyOnlineResponseIn",
        "ListReturnPolicyOnlineResponseOut": "_content_393_ListReturnPolicyOnlineResponseOut",
        "PosListResponseIn": "_content_394_PosListResponseIn",
        "PosListResponseOut": "_content_395_PosListResponseOut",
        "CloudExportAdditionalPropertiesIn": "_content_396_CloudExportAdditionalPropertiesIn",
        "CloudExportAdditionalPropertiesOut": "_content_397_CloudExportAdditionalPropertiesOut",
        "OrderinvoicesCreateRefundInvoiceRequestIn": "_content_398_OrderinvoicesCreateRefundInvoiceRequestIn",
        "OrderinvoicesCreateRefundInvoiceRequestOut": "_content_399_OrderinvoicesCreateRefundInvoiceRequestOut",
        "RecommendationCreativeIn": "_content_400_RecommendationCreativeIn",
        "RecommendationCreativeOut": "_content_401_RecommendationCreativeOut",
        "PriceCompetitivenessIn": "_content_402_PriceCompetitivenessIn",
        "PriceCompetitivenessOut": "_content_403_PriceCompetitivenessOut",
        "ProductAmountIn": "_content_404_ProductAmountIn",
        "ProductAmountOut": "_content_405_ProductAmountOut",
        "InapplicabilityDetailsIn": "_content_406_InapplicabilityDetailsIn",
        "InapplicabilityDetailsOut": "_content_407_InapplicabilityDetailsOut",
        "AccountItemUpdatesIn": "_content_408_AccountItemUpdatesIn",
        "AccountItemUpdatesOut": "_content_409_AccountItemUpdatesOut",
        "OrderTrackingSignalShipmentLineItemMappingIn": "_content_410_OrderTrackingSignalShipmentLineItemMappingIn",
        "OrderTrackingSignalShipmentLineItemMappingOut": "_content_411_OrderTrackingSignalShipmentLineItemMappingOut",
        "OrderPickupDetailsIn": "_content_412_OrderPickupDetailsIn",
        "OrderPickupDetailsOut": "_content_413_OrderPickupDetailsOut",
        "DatafeedFetchScheduleIn": "_content_414_DatafeedFetchScheduleIn",
        "DatafeedFetchScheduleOut": "_content_415_DatafeedFetchScheduleOut",
        "ProductProductDetailIn": "_content_416_ProductProductDetailIn",
        "ProductProductDetailOut": "_content_417_ProductProductDetailOut",
        "OrdersCustomBatchRequestEntryUpdateShipmentScheduledDeliveryDetailsIn": "_content_418_OrdersCustomBatchRequestEntryUpdateShipmentScheduledDeliveryDetailsIn",
        "OrdersCustomBatchRequestEntryUpdateShipmentScheduledDeliveryDetailsOut": "_content_419_OrdersCustomBatchRequestEntryUpdateShipmentScheduledDeliveryDetailsOut",
        "SettlementTransactionTransactionIn": "_content_420_SettlementTransactionTransactionIn",
        "SettlementTransactionTransactionOut": "_content_421_SettlementTransactionTransactionOut",
        "OnboardBuyOnGoogleProgramRequestIn": "_content_422_OnboardBuyOnGoogleProgramRequestIn",
        "OnboardBuyOnGoogleProgramRequestOut": "_content_423_OnboardBuyOnGoogleProgramRequestOut",
        "AccountsCustomBatchRequestEntryIn": "_content_424_AccountsCustomBatchRequestEntryIn",
        "AccountsCustomBatchRequestEntryOut": "_content_425_AccountsCustomBatchRequestEntryOut",
        "LiasettingsGetAccessibleGmbAccountsResponseIn": "_content_426_LiasettingsGetAccessibleGmbAccountsResponseIn",
        "LiasettingsGetAccessibleGmbAccountsResponseOut": "_content_427_LiasettingsGetAccessibleGmbAccountsResponseOut",
        "PosInventoryRequestIn": "_content_428_PosInventoryRequestIn",
        "PosInventoryRequestOut": "_content_429_PosInventoryRequestOut",
        "PromotionPromotionStatusIn": "_content_430_PromotionPromotionStatusIn",
        "PromotionPromotionStatusOut": "_content_431_PromotionPromotionStatusOut",
        "ProductStatusIn": "_content_432_ProductStatusIn",
        "ProductStatusOut": "_content_433_ProductStatusOut",
        "DatafeedstatusesCustomBatchRequestEntryIn": "_content_434_DatafeedstatusesCustomBatchRequestEntryIn",
        "DatafeedstatusesCustomBatchRequestEntryOut": "_content_435_DatafeedstatusesCustomBatchRequestEntryOut",
        "ListPromotionResponseIn": "_content_436_ListPromotionResponseIn",
        "ListPromotionResponseOut": "_content_437_ListPromotionResponseOut",
        "ListMethodQuotasResponseIn": "_content_438_ListMethodQuotasResponseIn",
        "ListMethodQuotasResponseOut": "_content_439_ListMethodQuotasResponseOut",
        "ReturnPolicyPolicyIn": "_content_440_ReturnPolicyPolicyIn",
        "ReturnPolicyPolicyOut": "_content_441_ReturnPolicyPolicyOut",
        "ShippingsettingsGetSupportedCarriersResponseIn": "_content_442_ShippingsettingsGetSupportedCarriersResponseIn",
        "ShippingsettingsGetSupportedCarriersResponseOut": "_content_443_ShippingsettingsGetSupportedCarriersResponseOut",
        "ProductIn": "_content_444_ProductIn",
        "ProductOut": "_content_445_ProductOut",
        "RepricingRuleEligibleOfferMatcherStringMatcherIn": "_content_446_RepricingRuleEligibleOfferMatcherStringMatcherIn",
        "RepricingRuleEligibleOfferMatcherStringMatcherOut": "_content_447_RepricingRuleEligibleOfferMatcherStringMatcherOut",
        "ProductViewIn": "_content_448_ProductViewIn",
        "ProductViewOut": "_content_449_ProductViewOut",
        "OrderCancellationIn": "_content_450_OrderCancellationIn",
        "OrderCancellationOut": "_content_451_OrderCancellationOut",
        "RecommendationDescriptionIn": "_content_452_RecommendationDescriptionIn",
        "RecommendationDescriptionOut": "_content_453_RecommendationDescriptionOut",
        "OrderCustomerIn": "_content_454_OrderCustomerIn",
        "OrderCustomerOut": "_content_455_OrderCustomerOut",
        "OrderreturnsReturnItemIn": "_content_456_OrderreturnsReturnItemIn",
        "OrderreturnsReturnItemOut": "_content_457_OrderreturnsReturnItemOut",
        "ServiceStoreConfigCutoffConfigLocalCutoffTimeIn": "_content_458_ServiceStoreConfigCutoffConfigLocalCutoffTimeIn",
        "ServiceStoreConfigCutoffConfigLocalCutoffTimeOut": "_content_459_ServiceStoreConfigCutoffConfigLocalCutoffTimeOut",
        "OrderTrackingSignalIn": "_content_460_OrderTrackingSignalIn",
        "OrderTrackingSignalOut": "_content_461_OrderTrackingSignalOut",
        "ProductCertificationIn": "_content_462_ProductCertificationIn",
        "ProductCertificationOut": "_content_463_ProductCertificationOut",
        "LiaInventorySettingsIn": "_content_464_LiaInventorySettingsIn",
        "LiaInventorySettingsOut": "_content_465_LiaInventorySettingsOut",
        "OrderreportsListTransactionsResponseIn": "_content_466_OrderreportsListTransactionsResponseIn",
        "OrderreportsListTransactionsResponseOut": "_content_467_OrderreportsListTransactionsResponseOut",
        "TestOrderPickupDetailsIn": "_content_468_TestOrderPickupDetailsIn",
        "TestOrderPickupDetailsOut": "_content_469_TestOrderPickupDetailsOut",
        "PriceIn": "_content_470_PriceIn",
        "PriceOut": "_content_471_PriceOut",
        "OrderLineItemProductVariantAttributeIn": "_content_472_OrderLineItemProductVariantAttributeIn",
        "OrderLineItemProductVariantAttributeOut": "_content_473_OrderLineItemProductVariantAttributeOut",
        "ReturnaddressCustomBatchResponseEntryIn": "_content_474_ReturnaddressCustomBatchResponseEntryIn",
        "ReturnaddressCustomBatchResponseEntryOut": "_content_475_ReturnaddressCustomBatchResponseEntryOut",
        "OrderinvoicesCreateRefundInvoiceResponseIn": "_content_476_OrderinvoicesCreateRefundInvoiceResponseIn",
        "OrderinvoicesCreateRefundInvoiceResponseOut": "_content_477_OrderinvoicesCreateRefundInvoiceResponseOut",
        "AccountImageImprovementsSettingsIn": "_content_478_AccountImageImprovementsSettingsIn",
        "AccountImageImprovementsSettingsOut": "_content_479_AccountImageImprovementsSettingsOut",
        "OrdersAcknowledgeResponseIn": "_content_480_OrdersAcknowledgeResponseIn",
        "OrdersAcknowledgeResponseOut": "_content_481_OrdersAcknowledgeResponseOut",
        "MerchantRejectionReasonIn": "_content_482_MerchantRejectionReasonIn",
        "MerchantRejectionReasonOut": "_content_483_MerchantRejectionReasonOut",
        "AccountImageImprovementsIn": "_content_484_AccountImageImprovementsIn",
        "AccountImageImprovementsOut": "_content_485_AccountImageImprovementsOut",
        "AccounttaxCustomBatchRequestIn": "_content_486_AccounttaxCustomBatchRequestIn",
        "AccounttaxCustomBatchRequestOut": "_content_487_AccounttaxCustomBatchRequestOut",
        "PostalCodeGroupIn": "_content_488_PostalCodeGroupIn",
        "PostalCodeGroupOut": "_content_489_PostalCodeGroupOut",
        "ReturnpolicyCustomBatchRequestEntryIn": "_content_490_ReturnpolicyCustomBatchRequestEntryIn",
        "ReturnpolicyCustomBatchRequestEntryOut": "_content_491_ReturnpolicyCustomBatchRequestEntryOut",
        "ProductViewItemIssueItemIssueSeverityIn": "_content_492_ProductViewItemIssueItemIssueSeverityIn",
        "ProductViewItemIssueItemIssueSeverityOut": "_content_493_ProductViewItemIssueItemIssueSeverityOut",
        "AccountStatusProductsIn": "_content_494_AccountStatusProductsIn",
        "AccountStatusProductsOut": "_content_495_AccountStatusProductsOut",
        "ProductViewItemIssueItemIssueTypeIn": "_content_496_ProductViewItemIssueItemIssueTypeIn",
        "ProductViewItemIssueItemIssueTypeOut": "_content_497_ProductViewItemIssueItemIssueTypeOut",
        "ReturnPolicyOnlineReturnShippingFeeIn": "_content_498_ReturnPolicyOnlineReturnShippingFeeIn",
        "ReturnPolicyOnlineReturnShippingFeeOut": "_content_499_ReturnPolicyOnlineReturnShippingFeeOut",
        "RefundReasonIn": "_content_500_RefundReasonIn",
        "RefundReasonOut": "_content_501_RefundReasonOut",
        "CarriersCarrierIn": "_content_502_CarriersCarrierIn",
        "CarriersCarrierOut": "_content_503_CarriersCarrierOut",
        "BrandIn": "_content_504_BrandIn",
        "BrandOut": "_content_505_BrandOut",
        "OrderinvoicesCreateChargeInvoiceRequestIn": "_content_506_OrderinvoicesCreateChargeInvoiceRequestIn",
        "OrderinvoicesCreateChargeInvoiceRequestOut": "_content_507_OrderinvoicesCreateChargeInvoiceRequestOut",
        "OrdersUpdateLineItemShippingDetailsResponseIn": "_content_508_OrdersUpdateLineItemShippingDetailsResponseIn",
        "OrdersUpdateLineItemShippingDetailsResponseOut": "_content_509_OrdersUpdateLineItemShippingDetailsResponseOut",
        "OrderShipmentIn": "_content_510_OrderShipmentIn",
        "OrderShipmentOut": "_content_511_OrderShipmentOut",
        "ErrorIn": "_content_512_ErrorIn",
        "ErrorOut": "_content_513_ErrorOut",
        "DateTimeIn": "_content_514_DateTimeIn",
        "DateTimeOut": "_content_515_DateTimeOut",
        "AccountStatusAccountLevelIssueIn": "_content_516_AccountStatusAccountLevelIssueIn",
        "AccountStatusAccountLevelIssueOut": "_content_517_AccountStatusAccountLevelIssueOut",
        "OrdersAcknowledgeRequestIn": "_content_518_OrdersAcknowledgeRequestIn",
        "OrdersAcknowledgeRequestOut": "_content_519_OrdersAcknowledgeRequestOut",
        "ErrorsIn": "_content_520_ErrorsIn",
        "ErrorsOut": "_content_521_ErrorsOut",
        "AccounttaxListResponseIn": "_content_522_AccounttaxListResponseIn",
        "AccounttaxListResponseOut": "_content_523_AccounttaxListResponseOut",
        "RecommendationCallToActionIn": "_content_524_RecommendationCallToActionIn",
        "RecommendationCallToActionOut": "_content_525_RecommendationCallToActionOut",
        "AccountsListLinksResponseIn": "_content_526_AccountsListLinksResponseIn",
        "AccountsListLinksResponseOut": "_content_527_AccountsListLinksResponseOut",
        "DatafeedStatusErrorIn": "_content_528_DatafeedStatusErrorIn",
        "DatafeedStatusErrorOut": "_content_529_DatafeedStatusErrorOut",
        "MerchantCenterDestinationIn": "_content_530_MerchantCenterDestinationIn",
        "MerchantCenterDestinationOut": "_content_531_MerchantCenterDestinationOut",
        "RepricingProductReportIn": "_content_532_RepricingProductReportIn",
        "RepricingProductReportOut": "_content_533_RepricingProductReportOut",
        "ReturnPolicySeasonalOverrideIn": "_content_534_ReturnPolicySeasonalOverrideIn",
        "ReturnPolicySeasonalOverrideOut": "_content_535_ReturnPolicySeasonalOverrideOut",
        "OrdersUpdateMerchantOrderIdRequestIn": "_content_536_OrdersUpdateMerchantOrderIdRequestIn",
        "OrdersUpdateMerchantOrderIdRequestOut": "_content_537_OrdersUpdateMerchantOrderIdRequestOut",
        "AccountsUpdateLabelsResponseIn": "_content_538_AccountsUpdateLabelsResponseIn",
        "AccountsUpdateLabelsResponseOut": "_content_539_AccountsUpdateLabelsResponseOut",
        "HolidayCutoffIn": "_content_540_HolidayCutoffIn",
        "HolidayCutoffOut": "_content_541_HolidayCutoffOut",
        "ProductDeliveryTimeAreaDeliveryTimeDeliveryTimeIn": "_content_542_ProductDeliveryTimeAreaDeliveryTimeDeliveryTimeIn",
        "ProductDeliveryTimeAreaDeliveryTimeDeliveryTimeOut": "_content_543_ProductDeliveryTimeAreaDeliveryTimeDeliveryTimeOut",
        "ShipmentInvoiceLineItemInvoiceIn": "_content_544_ShipmentInvoiceLineItemInvoiceIn",
        "ShipmentInvoiceLineItemInvoiceOut": "_content_545_ShipmentInvoiceLineItemInvoiceOut",
        "PriceAmountIn": "_content_546_PriceAmountIn",
        "PriceAmountOut": "_content_547_PriceAmountOut",
        "ProductsCustomBatchRequestEntryIn": "_content_548_ProductsCustomBatchRequestEntryIn",
        "ProductsCustomBatchRequestEntryOut": "_content_549_ProductsCustomBatchRequestEntryOut",
        "UnitInvoiceIn": "_content_550_UnitInvoiceIn",
        "UnitInvoiceOut": "_content_551_UnitInvoiceOut",
        "LocalinventoryCustomBatchResponseEntryIn": "_content_552_LocalinventoryCustomBatchResponseEntryIn",
        "LocalinventoryCustomBatchResponseEntryOut": "_content_553_LocalinventoryCustomBatchResponseEntryOut",
        "ReturnPolicyOnlineRestockingFeeIn": "_content_554_ReturnPolicyOnlineRestockingFeeIn",
        "ReturnPolicyOnlineRestockingFeeOut": "_content_555_ReturnPolicyOnlineRestockingFeeOut",
        "AccountShippingImprovementsIn": "_content_556_AccountShippingImprovementsIn",
        "AccountShippingImprovementsOut": "_content_557_AccountShippingImprovementsOut",
        "PauseBuyOnGoogleProgramRequestIn": "_content_558_PauseBuyOnGoogleProgramRequestIn",
        "PauseBuyOnGoogleProgramRequestOut": "_content_559_PauseBuyOnGoogleProgramRequestOut",
        "ProductShippingWeightIn": "_content_560_ProductShippingWeightIn",
        "ProductShippingWeightOut": "_content_561_ProductShippingWeightOut",
        "OrdersCreateTestReturnResponseIn": "_content_562_OrdersCreateTestReturnResponseIn",
        "OrdersCreateTestReturnResponseOut": "_content_563_OrdersCreateTestReturnResponseOut",
        "TransitTableTransitTimeRowIn": "_content_564_TransitTableTransitTimeRowIn",
        "TransitTableTransitTimeRowOut": "_content_565_TransitTableTransitTimeRowOut",
        "DatafeedstatusesCustomBatchResponseEntryIn": "_content_566_DatafeedstatusesCustomBatchResponseEntryIn",
        "DatafeedstatusesCustomBatchResponseEntryOut": "_content_567_DatafeedstatusesCustomBatchResponseEntryOut",
        "ListCssesResponseIn": "_content_568_ListCssesResponseIn",
        "ListCssesResponseOut": "_content_569_ListCssesResponseOut",
        "ListRepricingRulesResponseIn": "_content_570_ListRepricingRulesResponseIn",
        "ListRepricingRulesResponseOut": "_content_571_ListRepricingRulesResponseOut",
        "ReportRowIn": "_content_572_ReportRowIn",
        "ReportRowOut": "_content_573_ReportRowOut",
        "OrdersInStoreRefundLineItemRequestIn": "_content_574_OrdersInStoreRefundLineItemRequestIn",
        "OrdersInStoreRefundLineItemRequestOut": "_content_575_OrdersInStoreRefundLineItemRequestOut",
        "ListAccountLabelsResponseIn": "_content_576_ListAccountLabelsResponseIn",
        "ListAccountLabelsResponseOut": "_content_577_ListAccountLabelsResponseOut",
        "CutoffTimeIn": "_content_578_CutoffTimeIn",
        "CutoffTimeOut": "_content_579_CutoffTimeOut",
        "RequestReviewBuyOnGoogleProgramRequestIn": "_content_580_RequestReviewBuyOnGoogleProgramRequestIn",
        "RequestReviewBuyOnGoogleProgramRequestOut": "_content_581_RequestReviewBuyOnGoogleProgramRequestOut",
        "ServiceStoreConfigCutoffConfigIn": "_content_582_ServiceStoreConfigCutoffConfigIn",
        "ServiceStoreConfigCutoffConfigOut": "_content_583_ServiceStoreConfigCutoffConfigOut",
        "AccountsLinkResponseIn": "_content_584_AccountsLinkResponseIn",
        "AccountsLinkResponseOut": "_content_585_AccountsLinkResponseOut",
        "AccountGoogleMyBusinessLinkIn": "_content_586_AccountGoogleMyBusinessLinkIn",
        "AccountGoogleMyBusinessLinkOut": "_content_587_AccountGoogleMyBusinessLinkOut",
        "LiasettingsCustomBatchRequestEntryIn": "_content_588_LiasettingsCustomBatchRequestEntryIn",
        "LiasettingsCustomBatchRequestEntryOut": "_content_589_LiasettingsCustomBatchRequestEntryOut",
        "OrderreturnsListResponseIn": "_content_590_OrderreturnsListResponseIn",
        "OrderreturnsListResponseOut": "_content_591_OrderreturnsListResponseOut",
        "LocalinventoryCustomBatchResponseIn": "_content_592_LocalinventoryCustomBatchResponseIn",
        "LocalinventoryCustomBatchResponseOut": "_content_593_LocalinventoryCustomBatchResponseOut",
        "OrdersInStoreRefundLineItemResponseIn": "_content_594_OrdersInStoreRefundLineItemResponseIn",
        "OrdersInStoreRefundLineItemResponseOut": "_content_595_OrdersInStoreRefundLineItemResponseOut",
        "ProductShippingIn": "_content_596_ProductShippingIn",
        "ProductShippingOut": "_content_597_ProductShippingOut",
        "ShippingSettingsIn": "_content_598_ShippingSettingsIn",
        "ShippingSettingsOut": "_content_599_ShippingSettingsOut",
        "RepricingRuleRestrictionBoundaryIn": "_content_600_RepricingRuleRestrictionBoundaryIn",
        "RepricingRuleRestrictionBoundaryOut": "_content_601_RepricingRuleRestrictionBoundaryOut",
        "AccountLabelIn": "_content_602_AccountLabelIn",
        "AccountLabelOut": "_content_603_AccountLabelOut",
        "OrdersGetByMerchantOrderIdResponseIn": "_content_604_OrdersGetByMerchantOrderIdResponseIn",
        "OrdersGetByMerchantOrderIdResponseOut": "_content_605_OrdersGetByMerchantOrderIdResponseOut",
        "ProductstatusesCustomBatchResponseIn": "_content_606_ProductstatusesCustomBatchResponseIn",
        "ProductstatusesCustomBatchResponseOut": "_content_607_ProductstatusesCustomBatchResponseOut",
        "AccountStatusIn": "_content_608_AccountStatusIn",
        "AccountStatusOut": "_content_609_AccountStatusOut",
        "OrderRefundIn": "_content_610_OrderRefundIn",
        "OrderRefundOut": "_content_611_OrderRefundOut",
        "TestOrderLineItemIn": "_content_612_TestOrderLineItemIn",
        "TestOrderLineItemOut": "_content_613_TestOrderLineItemOut",
        "OrderLineItemAdjustmentIn": "_content_614_OrderLineItemAdjustmentIn",
        "OrderLineItemAdjustmentOut": "_content_615_OrderLineItemAdjustmentOut",
        "PosSaleRequestIn": "_content_616_PosSaleRequestIn",
        "PosSaleRequestOut": "_content_617_PosSaleRequestOut",
        "ProductIdIn": "_content_618_ProductIdIn",
        "ProductIdOut": "_content_619_ProductIdOut",
        "ShoppingAdsProgramStatusReviewIneligibilityReasonDetailsIn": "_content_620_ShoppingAdsProgramStatusReviewIneligibilityReasonDetailsIn",
        "ShoppingAdsProgramStatusReviewIneligibilityReasonDetailsOut": "_content_621_ShoppingAdsProgramStatusReviewIneligibilityReasonDetailsOut",
        "LoyaltyPointsIn": "_content_622_LoyaltyPointsIn",
        "LoyaltyPointsOut": "_content_623_LoyaltyPointsOut",
        "ShippingsettingsCustomBatchResponseIn": "_content_624_ShippingsettingsCustomBatchResponseIn",
        "ShippingsettingsCustomBatchResponseOut": "_content_625_ShippingsettingsCustomBatchResponseOut",
        "OrderreturnsAcknowledgeResponseIn": "_content_626_OrderreturnsAcknowledgeResponseIn",
        "OrderreturnsAcknowledgeResponseOut": "_content_627_OrderreturnsAcknowledgeResponseOut",
        "ProductsCustomBatchResponseIn": "_content_628_ProductsCustomBatchResponseIn",
        "ProductsCustomBatchResponseOut": "_content_629_ProductsCustomBatchResponseOut",
        "PosCustomBatchRequestIn": "_content_630_PosCustomBatchRequestIn",
        "PosCustomBatchRequestOut": "_content_631_PosCustomBatchRequestOut",
        "CssIn": "_content_632_CssIn",
        "CssOut": "_content_633_CssOut",
        "ProductsListResponseIn": "_content_634_ProductsListResponseIn",
        "ProductsListResponseOut": "_content_635_ProductsListResponseOut",
        "OrderLineItemIn": "_content_636_OrderLineItemIn",
        "OrderLineItemOut": "_content_637_OrderLineItemOut",
        "DatafeedsFetchNowResponseIn": "_content_638_DatafeedsFetchNowResponseIn",
        "DatafeedsFetchNowResponseOut": "_content_639_DatafeedsFetchNowResponseOut",
        "OrdersReturnRefundLineItemResponseIn": "_content_640_OrdersReturnRefundLineItemResponseIn",
        "OrdersReturnRefundLineItemResponseOut": "_content_641_OrdersReturnRefundLineItemResponseOut",
        "OrdersCancelLineItemResponseIn": "_content_642_OrdersCancelLineItemResponseIn",
        "OrdersCancelLineItemResponseOut": "_content_643_OrdersCancelLineItemResponseOut",
        "ShippingsettingsListResponseIn": "_content_644_ShippingsettingsListResponseIn",
        "ShippingsettingsListResponseOut": "_content_645_ShippingsettingsListResponseOut",
        "RequestReviewFreeListingsRequestIn": "_content_646_RequestReviewFreeListingsRequestIn",
        "RequestReviewFreeListingsRequestOut": "_content_647_RequestReviewFreeListingsRequestOut",
        "LiaOnDisplayToOrderSettingsIn": "_content_648_LiaOnDisplayToOrderSettingsIn",
        "LiaOnDisplayToOrderSettingsOut": "_content_649_LiaOnDisplayToOrderSettingsOut",
        "OrderinvoicesCustomBatchRequestEntryCreateRefundInvoiceRefundOptionIn": "_content_650_OrderinvoicesCustomBatchRequestEntryCreateRefundInvoiceRefundOptionIn",
        "OrderinvoicesCustomBatchRequestEntryCreateRefundInvoiceRefundOptionOut": "_content_651_OrderinvoicesCustomBatchRequestEntryCreateRefundInvoiceRefundOptionOut",
        "ReturnpolicyCustomBatchResponseIn": "_content_652_ReturnpolicyCustomBatchResponseIn",
        "ReturnpolicyCustomBatchResponseOut": "_content_653_ReturnpolicyCustomBatchResponseOut",
        "LiasettingsSetPosDataProviderResponseIn": "_content_654_LiasettingsSetPosDataProviderResponseIn",
        "LiasettingsSetPosDataProviderResponseOut": "_content_655_LiasettingsSetPosDataProviderResponseOut",
        "CarrierRateIn": "_content_656_CarrierRateIn",
        "CarrierRateOut": "_content_657_CarrierRateOut",
        "LiaSettingsIn": "_content_658_LiaSettingsIn",
        "LiaSettingsOut": "_content_659_LiaSettingsOut",
        "RequestPhoneVerificationResponseIn": "_content_660_RequestPhoneVerificationResponseIn",
        "RequestPhoneVerificationResponseOut": "_content_661_RequestPhoneVerificationResponseOut",
        "AccounttaxCustomBatchResponseIn": "_content_662_AccounttaxCustomBatchResponseIn",
        "AccounttaxCustomBatchResponseOut": "_content_663_AccounttaxCustomBatchResponseOut",
        "AccountsAuthInfoResponseIn": "_content_664_AccountsAuthInfoResponseIn",
        "AccountsAuthInfoResponseOut": "_content_665_AccountsAuthInfoResponseOut",
        "RateGroupIn": "_content_666_RateGroupIn",
        "RateGroupOut": "_content_667_RateGroupOut",
        "PosSaleResponseIn": "_content_668_PosSaleResponseIn",
        "PosSaleResponseOut": "_content_669_PosSaleResponseOut",
        "ProductClusterIn": "_content_670_ProductClusterIn",
        "ProductClusterOut": "_content_671_ProductClusterOut",
        "TransitTableIn": "_content_672_TransitTableIn",
        "TransitTableOut": "_content_673_TransitTableOut",
        "OrdersReturnRefundLineItemRequestIn": "_content_674_OrdersReturnRefundLineItemRequestIn",
        "OrdersReturnRefundLineItemRequestOut": "_content_675_OrdersReturnRefundLineItemRequestOut",
        "AddressIn": "_content_676_AddressIn",
        "AddressOut": "_content_677_AddressOut",
        "LabelIdsIn": "_content_678_LabelIdsIn",
        "LabelIdsOut": "_content_679_LabelIdsOut",
        "WarehouseBasedDeliveryTimeIn": "_content_680_WarehouseBasedDeliveryTimeIn",
        "WarehouseBasedDeliveryTimeOut": "_content_681_WarehouseBasedDeliveryTimeOut",
        "ReturnAddressAddressIn": "_content_682_ReturnAddressAddressIn",
        "ReturnAddressAddressOut": "_content_683_ReturnAddressAddressOut",
        "AccountTaxIn": "_content_684_AccountTaxIn",
        "AccountTaxOut": "_content_685_AccountTaxOut",
        "DatafeedIn": "_content_686_DatafeedIn",
        "DatafeedOut": "_content_687_DatafeedOut",
        "RepricingRuleEffectiveTimeFixedTimePeriodIn": "_content_688_RepricingRuleEffectiveTimeFixedTimePeriodIn",
        "RepricingRuleEffectiveTimeFixedTimePeriodOut": "_content_689_RepricingRuleEffectiveTimeFixedTimePeriodOut",
        "OrdersCreateTestReturnRequestIn": "_content_690_OrdersCreateTestReturnRequestIn",
        "OrdersCreateTestReturnRequestOut": "_content_691_OrdersCreateTestReturnRequestOut",
        "AccountIn": "_content_692_AccountIn",
        "AccountOut": "_content_693_AccountOut",
        "AccountCredentialsIn": "_content_694_AccountCredentialsIn",
        "AccountCredentialsOut": "_content_695_AccountCredentialsOut",
        "ReturnPolicyIn": "_content_696_ReturnPolicyIn",
        "ReturnPolicyOut": "_content_697_ReturnPolicyOut",
        "HolidaysHolidayIn": "_content_698_HolidaysHolidayIn",
        "HolidaysHolidayOut": "_content_699_HolidaysHolidayOut",
        "AccountUserIn": "_content_700_AccountUserIn",
        "AccountUserOut": "_content_701_AccountUserOut",
        "MetricsIn": "_content_702_MetricsIn",
        "MetricsOut": "_content_703_MetricsOut",
        "UndeleteConversionSourceRequestIn": "_content_704_UndeleteConversionSourceRequestIn",
        "UndeleteConversionSourceRequestOut": "_content_705_UndeleteConversionSourceRequestOut",
        "TimePeriodIn": "_content_706_TimePeriodIn",
        "TimePeriodOut": "_content_707_TimePeriodOut",
        "LocationIdSetIn": "_content_708_LocationIdSetIn",
        "LocationIdSetOut": "_content_709_LocationIdSetOut",
        "MinimumOrderValueTableIn": "_content_710_MinimumOrderValueTableIn",
        "MinimumOrderValueTableOut": "_content_711_MinimumOrderValueTableOut",
        "GmbAccountsIn": "_content_712_GmbAccountsIn",
        "GmbAccountsOut": "_content_713_GmbAccountsOut",
        "CustomAttributeIn": "_content_714_CustomAttributeIn",
        "CustomAttributeOut": "_content_715_CustomAttributeOut",
        "SettlementTransactionAmountIn": "_content_716_SettlementTransactionAmountIn",
        "SettlementTransactionAmountOut": "_content_717_SettlementTransactionAmountOut",
        "TimeZoneIn": "_content_718_TimeZoneIn",
        "TimeZoneOut": "_content_719_TimeZoneOut",
        "DatafeedsCustomBatchRequestEntryIn": "_content_720_DatafeedsCustomBatchRequestEntryIn",
        "DatafeedsCustomBatchRequestEntryOut": "_content_721_DatafeedsCustomBatchRequestEntryOut",
        "ReturnPolicyOnlinePolicyIn": "_content_722_ReturnPolicyOnlinePolicyIn",
        "ReturnPolicyOnlinePolicyOut": "_content_723_ReturnPolicyOnlinePolicyOut",
        "ReturnpolicyCustomBatchRequestIn": "_content_724_ReturnpolicyCustomBatchRequestIn",
        "ReturnpolicyCustomBatchRequestOut": "_content_725_ReturnpolicyCustomBatchRequestOut",
        "UnitInvoiceTaxLineIn": "_content_726_UnitInvoiceTaxLineIn",
        "UnitInvoiceTaxLineOut": "_content_727_UnitInvoiceTaxLineOut",
        "OrdersUpdateShipmentRequestIn": "_content_728_OrdersUpdateShipmentRequestIn",
        "OrdersUpdateShipmentRequestOut": "_content_729_OrdersUpdateShipmentRequestOut",
        "VerifyPhoneNumberResponseIn": "_content_730_VerifyPhoneNumberResponseIn",
        "VerifyPhoneNumberResponseOut": "_content_731_VerifyPhoneNumberResponseOut",
        "ProductDeliveryTimeAreaDeliveryTimeIn": "_content_732_ProductDeliveryTimeAreaDeliveryTimeIn",
        "ProductDeliveryTimeAreaDeliveryTimeOut": "_content_733_ProductDeliveryTimeAreaDeliveryTimeOut",
        "AccountAutomaticImprovementsIn": "_content_734_AccountAutomaticImprovementsIn",
        "AccountAutomaticImprovementsOut": "_content_735_AccountAutomaticImprovementsOut",
        "PosStoreIn": "_content_736_PosStoreIn",
        "PosStoreOut": "_content_737_PosStoreOut",
        "OrdersUpdateMerchantOrderIdResponseIn": "_content_738_OrdersUpdateMerchantOrderIdResponseIn",
        "OrdersUpdateMerchantOrderIdResponseOut": "_content_739_OrdersUpdateMerchantOrderIdResponseOut",
        "CaptureOrderRequestIn": "_content_740_CaptureOrderRequestIn",
        "CaptureOrderRequestOut": "_content_741_CaptureOrderRequestOut",
        "AccountYouTubeChannelLinkIn": "_content_742_AccountYouTubeChannelLinkIn",
        "AccountYouTubeChannelLinkOut": "_content_743_AccountYouTubeChannelLinkOut",
        "OrderPromotionItemIn": "_content_744_OrderPromotionItemIn",
        "OrderPromotionItemOut": "_content_745_OrderPromotionItemOut",
        "LiaAboutPageSettingsIn": "_content_746_LiaAboutPageSettingsIn",
        "LiaAboutPageSettingsOut": "_content_747_LiaAboutPageSettingsOut",
        "RegionalinventoryCustomBatchRequestEntryIn": "_content_748_RegionalinventoryCustomBatchRequestEntryIn",
        "RegionalinventoryCustomBatchRequestEntryOut": "_content_749_RegionalinventoryCustomBatchRequestEntryOut",
        "DatafeedStatusExampleIn": "_content_750_DatafeedStatusExampleIn",
        "DatafeedStatusExampleOut": "_content_751_DatafeedStatusExampleOut",
        "OrderreturnsLineItemIn": "_content_752_OrderreturnsLineItemIn",
        "OrderreturnsLineItemOut": "_content_753_OrderreturnsLineItemOut",
        "BuyOnGoogleProgramStatusIn": "_content_754_BuyOnGoogleProgramStatusIn",
        "BuyOnGoogleProgramStatusOut": "_content_755_BuyOnGoogleProgramStatusOut",
        "AccountsCustomBatchResponseIn": "_content_756_AccountsCustomBatchResponseIn",
        "AccountsCustomBatchResponseOut": "_content_757_AccountsCustomBatchResponseOut",
        "MonetaryAmountIn": "_content_758_MonetaryAmountIn",
        "MonetaryAmountOut": "_content_759_MonetaryAmountOut",
        "ListCollectionsResponseIn": "_content_760_ListCollectionsResponseIn",
        "ListCollectionsResponseOut": "_content_761_ListCollectionsResponseOut",
        "ListRegionsResponseIn": "_content_762_ListRegionsResponseIn",
        "ListRegionsResponseOut": "_content_763_ListRegionsResponseOut",
        "RepricingRuleEffectiveTimeIn": "_content_764_RepricingRuleEffectiveTimeIn",
        "RepricingRuleEffectiveTimeOut": "_content_765_RepricingRuleEffectiveTimeOut",
        "DatafeedstatusesListResponseIn": "_content_766_DatafeedstatusesListResponseIn",
        "DatafeedstatusesListResponseOut": "_content_767_DatafeedstatusesListResponseOut",
        "LiasettingsCustomBatchResponseIn": "_content_768_LiasettingsCustomBatchResponseIn",
        "LiasettingsCustomBatchResponseOut": "_content_769_LiasettingsCustomBatchResponseOut",
        "SearchRequestIn": "_content_770_SearchRequestIn",
        "SearchRequestOut": "_content_771_SearchRequestOut",
        "ProductStatusItemLevelIssueIn": "_content_772_ProductStatusItemLevelIssueIn",
        "ProductStatusItemLevelIssueOut": "_content_773_ProductStatusItemLevelIssueOut",
        "ProductDeliveryTimeIn": "_content_774_ProductDeliveryTimeIn",
        "ProductDeliveryTimeOut": "_content_775_ProductDeliveryTimeOut",
        "PromotionPromotionStatusDestinationStatusIn": "_content_776_PromotionPromotionStatusDestinationStatusIn",
        "PromotionPromotionStatusDestinationStatusOut": "_content_777_PromotionPromotionStatusDestinationStatusOut",
        "LocalInventoryIn": "_content_778_LocalInventoryIn",
        "LocalInventoryOut": "_content_779_LocalInventoryOut",
        "TestOrderLineItemProductIn": "_content_780_TestOrderLineItemProductIn",
        "TestOrderLineItemProductOut": "_content_781_TestOrderLineItemProductOut",
        "InstallmentIn": "_content_782_InstallmentIn",
        "InstallmentOut": "_content_783_InstallmentOut",
        "LiasettingsRequestInventoryVerificationResponseIn": "_content_784_LiasettingsRequestInventoryVerificationResponseIn",
        "LiasettingsRequestInventoryVerificationResponseOut": "_content_785_LiasettingsRequestInventoryVerificationResponseOut",
        "SettlementReportIn": "_content_786_SettlementReportIn",
        "SettlementReportOut": "_content_787_SettlementReportOut",
        "OrdersCancelRequestIn": "_content_788_OrdersCancelRequestIn",
        "OrdersCancelRequestOut": "_content_789_OrdersCancelRequestOut",
        "TableIn": "_content_790_TableIn",
        "TableOut": "_content_791_TableOut",
        "OrderreturnsCreateOrderReturnResponseIn": "_content_792_OrderreturnsCreateOrderReturnResponseIn",
        "OrderreturnsCreateOrderReturnResponseOut": "_content_793_OrderreturnsCreateOrderReturnResponseOut",
        "OrderCustomerLoyaltyInfoIn": "_content_794_OrderCustomerLoyaltyInfoIn",
        "OrderCustomerLoyaltyInfoOut": "_content_795_OrderCustomerLoyaltyInfoOut",
        "ReportInteractionRequestIn": "_content_796_ReportInteractionRequestIn",
        "ReportInteractionRequestOut": "_content_797_ReportInteractionRequestOut",
        "RegionalInventoryIn": "_content_798_RegionalInventoryIn",
        "RegionalInventoryOut": "_content_799_RegionalInventoryOut",
        "LiasettingsCustomBatchResponseEntryIn": "_content_800_LiasettingsCustomBatchResponseEntryIn",
        "LiasettingsCustomBatchResponseEntryOut": "_content_801_LiasettingsCustomBatchResponseEntryOut",
        "OrderreturnsRejectOperationIn": "_content_802_OrderreturnsRejectOperationIn",
        "OrderreturnsRejectOperationOut": "_content_803_OrderreturnsRejectOperationOut",
        "AccounttaxCustomBatchRequestEntryIn": "_content_804_AccounttaxCustomBatchRequestEntryIn",
        "AccounttaxCustomBatchRequestEntryOut": "_content_805_AccounttaxCustomBatchRequestEntryOut",
        "OrdersCancelTestOrderByCustomerResponseIn": "_content_806_OrdersCancelTestOrderByCustomerResponseIn",
        "OrdersCancelTestOrderByCustomerResponseOut": "_content_807_OrdersCancelTestOrderByCustomerResponseOut",
        "DatafeedTargetIn": "_content_808_DatafeedTargetIn",
        "DatafeedTargetOut": "_content_809_DatafeedTargetOut",
        "AccountstatusesListResponseIn": "_content_810_AccountstatusesListResponseIn",
        "AccountstatusesListResponseOut": "_content_811_AccountstatusesListResponseOut",
        "OrderTrackingSignalLineItemDetailsIn": "_content_812_OrderTrackingSignalLineItemDetailsIn",
        "OrderTrackingSignalLineItemDetailsOut": "_content_813_OrderTrackingSignalLineItemDetailsOut",
        "RepricingRuleRestrictionIn": "_content_814_RepricingRuleRestrictionIn",
        "RepricingRuleRestrictionOut": "_content_815_RepricingRuleRestrictionOut",
        "ReturnaddressListResponseIn": "_content_816_ReturnaddressListResponseIn",
        "ReturnaddressListResponseOut": "_content_817_ReturnaddressListResponseOut",
        "RequestPhoneVerificationRequestIn": "_content_818_RequestPhoneVerificationRequestIn",
        "RequestPhoneVerificationRequestOut": "_content_819_RequestPhoneVerificationRequestOut",
        "ReturnaddressCustomBatchRequestEntryIn": "_content_820_ReturnaddressCustomBatchRequestEntryIn",
        "ReturnaddressCustomBatchRequestEntryOut": "_content_821_ReturnaddressCustomBatchRequestEntryOut",
        "LiaPosDataProviderIn": "_content_822_LiaPosDataProviderIn",
        "LiaPosDataProviderOut": "_content_823_LiaPosDataProviderOut",
        "ProductstatusesListResponseIn": "_content_824_ProductstatusesListResponseIn",
        "ProductstatusesListResponseOut": "_content_825_ProductstatusesListResponseOut",
        "ListAccountReturnCarrierResponseIn": "_content_826_ListAccountReturnCarrierResponseIn",
        "ListAccountReturnCarrierResponseOut": "_content_827_ListAccountReturnCarrierResponseOut",
        "OrderinvoicesCreateChargeInvoiceResponseIn": "_content_828_OrderinvoicesCreateChargeInvoiceResponseIn",
        "OrderinvoicesCreateChargeInvoiceResponseOut": "_content_829_OrderinvoicesCreateChargeInvoiceResponseOut",
        "AmountIn": "_content_830_AmountIn",
        "AmountOut": "_content_831_AmountOut",
        "MerchantOrderReturnItemIn": "_content_832_MerchantOrderReturnItemIn",
        "MerchantOrderReturnItemOut": "_content_833_MerchantOrderReturnItemOut",
        "LiasettingsListPosDataProvidersResponseIn": "_content_834_LiasettingsListPosDataProvidersResponseIn",
        "LiasettingsListPosDataProvidersResponseOut": "_content_835_LiasettingsListPosDataProvidersResponseOut",
        "DateIn": "_content_836_DateIn",
        "DateOut": "_content_837_DateOut",
        "OrderMerchantProvidedAnnotationIn": "_content_838_OrderMerchantProvidedAnnotationIn",
        "OrderMerchantProvidedAnnotationOut": "_content_839_OrderMerchantProvidedAnnotationOut",
        "OrderLineItemShippingDetailsMethodIn": "_content_840_OrderLineItemShippingDetailsMethodIn",
        "OrderLineItemShippingDetailsMethodOut": "_content_841_OrderLineItemShippingDetailsMethodOut",
        "ProductShippingDimensionIn": "_content_842_ProductShippingDimensionIn",
        "ProductShippingDimensionOut": "_content_843_ProductShippingDimensionOut",
        "TransitTableTransitTimeRowTransitTimeValueIn": "_content_844_TransitTableTransitTimeRowTransitTimeValueIn",
        "TransitTableTransitTimeRowTransitTimeValueOut": "_content_845_TransitTableTransitTimeRowTransitTimeValueOut",
        "OrdersCustomBatchRequestEntryRefundItemShippingIn": "_content_846_OrdersCustomBatchRequestEntryRefundItemShippingIn",
        "OrdersCustomBatchRequestEntryRefundItemShippingOut": "_content_847_OrdersCustomBatchRequestEntryRefundItemShippingOut",
        "OrdersShipLineItemsRequestIn": "_content_848_OrdersShipLineItemsRequestIn",
        "OrdersShipLineItemsRequestOut": "_content_849_OrdersShipLineItemsRequestOut",
        "RegionalinventoryCustomBatchResponseIn": "_content_850_RegionalinventoryCustomBatchResponseIn",
        "RegionalinventoryCustomBatchResponseOut": "_content_851_RegionalinventoryCustomBatchResponseOut",
        "TestOrderIn": "_content_852_TestOrderIn",
        "TestOrderOut": "_content_853_TestOrderOut",
        "ProductSubscriptionCostIn": "_content_854_ProductSubscriptionCostIn",
        "ProductSubscriptionCostOut": "_content_855_ProductSubscriptionCostOut",
        "PriceInsightsIn": "_content_856_PriceInsightsIn",
        "PriceInsightsOut": "_content_857_PriceInsightsOut",
        "TestOrderAddressIn": "_content_858_TestOrderAddressIn",
        "TestOrderAddressOut": "_content_859_TestOrderAddressOut",
        "RowIn": "_content_860_RowIn",
        "RowOut": "_content_861_RowOut",
        "GoogleAnalyticsLinkIn": "_content_862_GoogleAnalyticsLinkIn",
        "GoogleAnalyticsLinkOut": "_content_863_GoogleAnalyticsLinkOut",
        "SettlementTransactionIn": "_content_864_SettlementTransactionIn",
        "SettlementTransactionOut": "_content_865_SettlementTransactionOut",
        "ListRepricingProductReportsResponseIn": "_content_866_ListRepricingProductReportsResponseIn",
        "ListRepricingProductReportsResponseOut": "_content_867_ListRepricingProductReportsResponseOut",
        "OrderPickupDetailsCollectorIn": "_content_868_OrderPickupDetailsCollectorIn",
        "OrderPickupDetailsCollectorOut": "_content_869_OrderPickupDetailsCollectorOut",
        "SettlementreportsListResponseIn": "_content_870_SettlementreportsListResponseIn",
        "SettlementreportsListResponseOut": "_content_871_SettlementreportsListResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ProductTaxIn"] = t.struct(
        {
            "postalCode": t.string().optional(),
            "region": t.string().optional(),
            "rate": t.number().optional(),
            "country": t.string().optional(),
            "locationId": t.string().optional(),
            "taxShip": t.boolean().optional(),
        }
    ).named(renames["ProductTaxIn"])
    types["ProductTaxOut"] = t.struct(
        {
            "postalCode": t.string().optional(),
            "region": t.string().optional(),
            "rate": t.number().optional(),
            "country": t.string().optional(),
            "locationId": t.string().optional(),
            "taxShip": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductTaxOut"])
    types["ServiceIn"] = t.struct(
        {
            "rateGroups": t.array(t.proxy(renames["RateGroupIn"])).optional(),
            "eligibility": t.string().optional(),
            "storeConfig": t.proxy(renames["ServiceStoreConfigIn"]).optional(),
            "minimumOrderValue": t.proxy(renames["PriceIn"]).optional(),
            "minimumOrderValueTable": t.proxy(
                renames["MinimumOrderValueTableIn"]
            ).optional(),
            "currency": t.string().optional(),
            "deliveryCountry": t.string().optional(),
            "pickupService": t.proxy(renames["PickupCarrierServiceIn"]).optional(),
            "name": t.string().optional(),
            "active": t.boolean().optional(),
            "deliveryTime": t.proxy(renames["DeliveryTimeIn"]).optional(),
            "shipmentType": t.string().optional(),
        }
    ).named(renames["ServiceIn"])
    types["ServiceOut"] = t.struct(
        {
            "rateGroups": t.array(t.proxy(renames["RateGroupOut"])).optional(),
            "eligibility": t.string().optional(),
            "storeConfig": t.proxy(renames["ServiceStoreConfigOut"]).optional(),
            "minimumOrderValue": t.proxy(renames["PriceOut"]).optional(),
            "minimumOrderValueTable": t.proxy(
                renames["MinimumOrderValueTableOut"]
            ).optional(),
            "currency": t.string().optional(),
            "deliveryCountry": t.string().optional(),
            "pickupService": t.proxy(renames["PickupCarrierServiceOut"]).optional(),
            "name": t.string().optional(),
            "active": t.boolean().optional(),
            "deliveryTime": t.proxy(renames["DeliveryTimeOut"]).optional(),
            "shipmentType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceOut"])
    types["OrdersSetLineItemMetadataResponseIn"] = t.struct(
        {"kind": t.string().optional(), "executionStatus": t.string().optional()}
    ).named(renames["OrdersSetLineItemMetadataResponseIn"])
    types["OrdersSetLineItemMetadataResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "executionStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersSetLineItemMetadataResponseOut"])
    types["OrdersRefundOrderResponseIn"] = t.struct(
        {"kind": t.string().optional(), "executionStatus": t.string().optional()}
    ).named(renames["OrdersRefundOrderResponseIn"])
    types["OrdersRefundOrderResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "executionStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersRefundOrderResponseOut"])
    types["UnitInvoiceAdditionalChargeIn"] = t.struct(
        {
            "additionalChargeAmount": t.proxy(renames["AmountIn"]).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["UnitInvoiceAdditionalChargeIn"])
    types["UnitInvoiceAdditionalChargeOut"] = t.struct(
        {
            "additionalChargeAmount": t.proxy(renames["AmountOut"]).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UnitInvoiceAdditionalChargeOut"])
    types["AccountsUpdateLabelsRequestIn"] = t.struct(
        {"labelIds": t.array(t.string()).optional()}
    ).named(renames["AccountsUpdateLabelsRequestIn"])
    types["AccountsUpdateLabelsRequestOut"] = t.struct(
        {
            "labelIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountsUpdateLabelsRequestOut"])
    types["CollectionIn"] = t.struct(
        {
            "language": t.string().optional(),
            "id": t.string(),
            "productCountry": t.string().optional(),
            "customLabel2": t.string().optional(),
            "mobileLink": t.string().optional(),
            "imageLink": t.array(t.string()).optional(),
            "customLabel3": t.string().optional(),
            "headline": t.array(t.string()).optional(),
            "customLabel0": t.string().optional(),
            "featuredProduct": t.array(
                t.proxy(renames["CollectionFeaturedProductIn"])
            ).optional(),
            "link": t.string().optional(),
            "customLabel1": t.string().optional(),
            "customLabel4": t.string().optional(),
        }
    ).named(renames["CollectionIn"])
    types["CollectionOut"] = t.struct(
        {
            "language": t.string().optional(),
            "id": t.string(),
            "productCountry": t.string().optional(),
            "customLabel2": t.string().optional(),
            "mobileLink": t.string().optional(),
            "imageLink": t.array(t.string()).optional(),
            "customLabel3": t.string().optional(),
            "headline": t.array(t.string()).optional(),
            "customLabel0": t.string().optional(),
            "featuredProduct": t.array(
                t.proxy(renames["CollectionFeaturedProductOut"])
            ).optional(),
            "link": t.string().optional(),
            "customLabel1": t.string().optional(),
            "customLabel4": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CollectionOut"])
    types["RepricingRuleCostOfGoodsSaleRuleIn"] = t.struct(
        {"priceDelta": t.string().optional(), "percentageDelta": t.integer().optional()}
    ).named(renames["RepricingRuleCostOfGoodsSaleRuleIn"])
    types["RepricingRuleCostOfGoodsSaleRuleOut"] = t.struct(
        {
            "priceDelta": t.string().optional(),
            "percentageDelta": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepricingRuleCostOfGoodsSaleRuleOut"])
    types["PosSaleIn"] = t.struct(
        {
            "quantity": t.string(),
            "timestamp": t.string(),
            "storeCode": t.string(),
            "targetCountry": t.string(),
            "kind": t.string().optional(),
            "contentLanguage": t.string(),
            "gtin": t.string().optional(),
            "price": t.proxy(renames["PriceIn"]),
            "itemId": t.string(),
            "saleId": t.string().optional(),
        }
    ).named(renames["PosSaleIn"])
    types["PosSaleOut"] = t.struct(
        {
            "quantity": t.string(),
            "timestamp": t.string(),
            "storeCode": t.string(),
            "targetCountry": t.string(),
            "kind": t.string().optional(),
            "contentLanguage": t.string(),
            "gtin": t.string().optional(),
            "price": t.proxy(renames["PriceOut"]),
            "itemId": t.string(),
            "saleId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PosSaleOut"])
    types["CollectionStatusItemLevelIssueIn"] = t.struct(
        {
            "attributeName": t.string().optional(),
            "destination": t.string().optional(),
            "description": t.string().optional(),
            "resolution": t.string().optional(),
            "servability": t.string().optional(),
            "applicableCountries": t.array(t.string()).optional(),
            "code": t.string().optional(),
            "documentation": t.string().optional(),
            "detail": t.string().optional(),
        }
    ).named(renames["CollectionStatusItemLevelIssueIn"])
    types["CollectionStatusItemLevelIssueOut"] = t.struct(
        {
            "attributeName": t.string().optional(),
            "destination": t.string().optional(),
            "description": t.string().optional(),
            "resolution": t.string().optional(),
            "servability": t.string().optional(),
            "applicableCountries": t.array(t.string()).optional(),
            "code": t.string().optional(),
            "documentation": t.string().optional(),
            "detail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CollectionStatusItemLevelIssueOut"])
    types["RepricingRuleEligibleOfferMatcherIn"] = t.struct(
        {
            "offerIdMatcher": t.proxy(
                renames["RepricingRuleEligibleOfferMatcherStringMatcherIn"]
            ).optional(),
            "itemGroupIdMatcher": t.proxy(
                renames["RepricingRuleEligibleOfferMatcherStringMatcherIn"]
            ).optional(),
            "skipWhenOnPromotion": t.boolean().optional(),
            "brandMatcher": t.proxy(
                renames["RepricingRuleEligibleOfferMatcherStringMatcherIn"]
            ).optional(),
            "matcherOption": t.string().optional(),
        }
    ).named(renames["RepricingRuleEligibleOfferMatcherIn"])
    types["RepricingRuleEligibleOfferMatcherOut"] = t.struct(
        {
            "offerIdMatcher": t.proxy(
                renames["RepricingRuleEligibleOfferMatcherStringMatcherOut"]
            ).optional(),
            "itemGroupIdMatcher": t.proxy(
                renames["RepricingRuleEligibleOfferMatcherStringMatcherOut"]
            ).optional(),
            "skipWhenOnPromotion": t.boolean().optional(),
            "brandMatcher": t.proxy(
                renames["RepricingRuleEligibleOfferMatcherStringMatcherOut"]
            ).optional(),
            "matcherOption": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepricingRuleEligibleOfferMatcherOut"])
    types["OrderreturnsPartialRefundIn"] = t.struct(
        {
            "priceAmount": t.proxy(renames["PriceIn"]).optional(),
            "taxAmount": t.proxy(renames["PriceIn"]).optional(),
        }
    ).named(renames["OrderreturnsPartialRefundIn"])
    types["OrderreturnsPartialRefundOut"] = t.struct(
        {
            "priceAmount": t.proxy(renames["PriceOut"]).optional(),
            "taxAmount": t.proxy(renames["PriceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderreturnsPartialRefundOut"])
    types["FreeListingsProgramStatusRegionStatusIn"] = t.struct(
        {
            "onboardingIssues": t.array(t.string()).optional(),
            "reviewIneligibilityReasonDescription": t.string().optional(),
            "reviewEligibilityStatus": t.string().optional(),
            "disapprovalDate": t.string().optional(),
            "reviewIneligibilityReason": t.string().optional(),
            "eligibilityStatus": t.string().optional(),
            "reviewIssues": t.array(t.string()).optional(),
            "regionCodes": t.array(t.string()).optional(),
            "reviewIneligibilityReasonDetails": t.proxy(
                renames["FreeListingsProgramStatusReviewIneligibilityReasonDetailsIn"]
            ).optional(),
        }
    ).named(renames["FreeListingsProgramStatusRegionStatusIn"])
    types["FreeListingsProgramStatusRegionStatusOut"] = t.struct(
        {
            "onboardingIssues": t.array(t.string()).optional(),
            "reviewIneligibilityReasonDescription": t.string().optional(),
            "reviewEligibilityStatus": t.string().optional(),
            "disapprovalDate": t.string().optional(),
            "reviewIneligibilityReason": t.string().optional(),
            "eligibilityStatus": t.string().optional(),
            "reviewIssues": t.array(t.string()).optional(),
            "regionCodes": t.array(t.string()).optional(),
            "reviewIneligibilityReasonDetails": t.proxy(
                renames["FreeListingsProgramStatusReviewIneligibilityReasonDetailsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FreeListingsProgramStatusRegionStatusOut"])
    types["OrderReturnIn"] = t.struct(
        {
            "reasonText": t.string().optional(),
            "reason": t.string().optional(),
            "actor": t.string().optional(),
            "creationDate": t.string().optional(),
            "quantity": t.integer().optional(),
        }
    ).named(renames["OrderReturnIn"])
    types["OrderReturnOut"] = t.struct(
        {
            "reasonText": t.string().optional(),
            "reason": t.string().optional(),
            "actor": t.string().optional(),
            "creationDate": t.string().optional(),
            "quantity": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderReturnOut"])
    types["ProductStatusDestinationStatusIn"] = t.struct(
        {
            "disapprovedCountries": t.array(t.string()).optional(),
            "status": t.string().optional(),
            "destination": t.string().optional(),
            "approvedCountries": t.array(t.string()).optional(),
            "pendingCountries": t.array(t.string()).optional(),
        }
    ).named(renames["ProductStatusDestinationStatusIn"])
    types["ProductStatusDestinationStatusOut"] = t.struct(
        {
            "disapprovedCountries": t.array(t.string()).optional(),
            "status": t.string().optional(),
            "destination": t.string().optional(),
            "approvedCountries": t.array(t.string()).optional(),
            "pendingCountries": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductStatusDestinationStatusOut"])
    types["ProductViewItemIssueIssueSeverityPerDestinationIn"] = t.struct(
        {
            "demotedCountries": t.array(t.string()).optional(),
            "destination": t.string().optional(),
            "disapprovedCountries": t.array(t.string()).optional(),
        }
    ).named(renames["ProductViewItemIssueIssueSeverityPerDestinationIn"])
    types["ProductViewItemIssueIssueSeverityPerDestinationOut"] = t.struct(
        {
            "demotedCountries": t.array(t.string()).optional(),
            "destination": t.string().optional(),
            "disapprovedCountries": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductViewItemIssueIssueSeverityPerDestinationOut"])
    types["ListCollectionStatusesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "resources": t.array(t.proxy(renames["CollectionStatusIn"])).optional(),
        }
    ).named(renames["ListCollectionStatusesResponseIn"])
    types["ListCollectionStatusesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "resources": t.array(t.proxy(renames["CollectionStatusOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCollectionStatusesResponseOut"])
    types["ReturnPolicyOnlineReturnReasonCategoryInfoIn"] = t.struct(
        {
            "returnLabelSource": t.string().optional(),
            "returnShippingFee": t.proxy(
                renames["ReturnPolicyOnlineReturnShippingFeeIn"]
            ).optional(),
            "returnReasonCategory": t.string().optional(),
        }
    ).named(renames["ReturnPolicyOnlineReturnReasonCategoryInfoIn"])
    types["ReturnPolicyOnlineReturnReasonCategoryInfoOut"] = t.struct(
        {
            "returnLabelSource": t.string().optional(),
            "returnShippingFee": t.proxy(
                renames["ReturnPolicyOnlineReturnShippingFeeOut"]
            ).optional(),
            "returnReasonCategory": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReturnPolicyOnlineReturnReasonCategoryInfoOut"])
    types["OrdersCreateTestOrderRequestIn"] = t.struct(
        {
            "templateName": t.string().optional(),
            "country": t.string().optional(),
            "testOrder": t.proxy(renames["TestOrderIn"]).optional(),
        }
    ).named(renames["OrdersCreateTestOrderRequestIn"])
    types["OrdersCreateTestOrderRequestOut"] = t.struct(
        {
            "templateName": t.string().optional(),
            "country": t.string().optional(),
            "testOrder": t.proxy(renames["TestOrderOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersCreateTestOrderRequestOut"])
    types["OrdersUpdateLineItemShippingDetailsRequestIn"] = t.struct(
        {
            "lineItemId": t.string().optional(),
            "productId": t.string().optional(),
            "shipByDate": t.string().optional(),
            "operationId": t.string().optional(),
            "deliverByDate": t.string().optional(),
        }
    ).named(renames["OrdersUpdateLineItemShippingDetailsRequestIn"])
    types["OrdersUpdateLineItemShippingDetailsRequestOut"] = t.struct(
        {
            "lineItemId": t.string().optional(),
            "productId": t.string().optional(),
            "shipByDate": t.string().optional(),
            "operationId": t.string().optional(),
            "deliverByDate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersUpdateLineItemShippingDetailsRequestOut"])
    types["CaptureOrderResponseIn"] = t.struct(
        {"executionStatus": t.string().optional()}
    ).named(renames["CaptureOrderResponseIn"])
    types["CaptureOrderResponseOut"] = t.struct(
        {
            "executionStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CaptureOrderResponseOut"])
    types["MerchantOrderReturnIn"] = t.struct(
        {
            "creationDate": t.string().optional(),
            "returnShipments": t.array(t.proxy(renames["ReturnShipmentIn"])).optional(),
            "orderId": t.string().optional(),
            "merchantOrderId": t.string().optional(),
            "orderReturnId": t.string().optional(),
            "returnItems": t.array(
                t.proxy(renames["MerchantOrderReturnItemIn"])
            ).optional(),
            "returnPricingInfo": t.proxy(renames["ReturnPricingInfoIn"]).optional(),
        }
    ).named(renames["MerchantOrderReturnIn"])
    types["MerchantOrderReturnOut"] = t.struct(
        {
            "creationDate": t.string().optional(),
            "returnShipments": t.array(
                t.proxy(renames["ReturnShipmentOut"])
            ).optional(),
            "orderId": t.string().optional(),
            "merchantOrderId": t.string().optional(),
            "orderReturnId": t.string().optional(),
            "returnItems": t.array(
                t.proxy(renames["MerchantOrderReturnItemOut"])
            ).optional(),
            "returnPricingInfo": t.proxy(renames["ReturnPricingInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MerchantOrderReturnOut"])
    types["SettlementTransactionAmountCommissionIn"] = t.struct(
        {"category": t.string().optional(), "rate": t.string().optional()}
    ).named(renames["SettlementTransactionAmountCommissionIn"])
    types["SettlementTransactionAmountCommissionOut"] = t.struct(
        {
            "category": t.string().optional(),
            "rate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SettlementTransactionAmountCommissionOut"])
    types["OrdersShipLineItemsResponseIn"] = t.struct(
        {"kind": t.string().optional(), "executionStatus": t.string().optional()}
    ).named(renames["OrdersShipLineItemsResponseIn"])
    types["OrdersShipLineItemsResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "executionStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersShipLineItemsResponseOut"])
    types["ProductstatusesCustomBatchRequestIn"] = t.struct(
        {
            "entries": t.array(
                t.proxy(renames["ProductstatusesCustomBatchRequestEntryIn"])
            ).optional()
        }
    ).named(renames["ProductstatusesCustomBatchRequestIn"])
    types["ProductstatusesCustomBatchRequestOut"] = t.struct(
        {
            "entries": t.array(
                t.proxy(renames["ProductstatusesCustomBatchRequestEntryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductstatusesCustomBatchRequestOut"])
    types["PosDataProvidersPosDataProviderIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "providerId": t.string().optional(),
            "fullName": t.string().optional(),
        }
    ).named(renames["PosDataProvidersPosDataProviderIn"])
    types["PosDataProvidersPosDataProviderOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "providerId": t.string().optional(),
            "fullName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PosDataProvidersPosDataProviderOut"])
    types["OrderreturnsRefundOperationIn"] = t.struct(
        {
            "fullRefund": t.boolean().optional(),
            "returnRefundReason": t.string().optional(),
            "partialRefund": t.proxy(renames["OrderreturnsPartialRefundIn"]).optional(),
            "paymentType": t.string().optional(),
            "reasonText": t.string().optional(),
        }
    ).named(renames["OrderreturnsRefundOperationIn"])
    types["OrderreturnsRefundOperationOut"] = t.struct(
        {
            "fullRefund": t.boolean().optional(),
            "returnRefundReason": t.string().optional(),
            "partialRefund": t.proxy(
                renames["OrderreturnsPartialRefundOut"]
            ).optional(),
            "paymentType": t.string().optional(),
            "reasonText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderreturnsRefundOperationOut"])
    types["OrderreturnsCreateOrderReturnRequestIn"] = t.struct(
        {
            "returnMethodType": t.string().optional(),
            "operationId": t.string().optional(),
            "orderId": t.string().optional(),
            "lineItems": t.array(t.proxy(renames["OrderreturnsLineItemIn"])).optional(),
        }
    ).named(renames["OrderreturnsCreateOrderReturnRequestIn"])
    types["OrderreturnsCreateOrderReturnRequestOut"] = t.struct(
        {
            "returnMethodType": t.string().optional(),
            "operationId": t.string().optional(),
            "orderId": t.string().optional(),
            "lineItems": t.array(
                t.proxy(renames["OrderreturnsLineItemOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderreturnsCreateOrderReturnRequestOut"])
    types["AccountstatusesCustomBatchResponseIn"] = t.struct(
        {
            "entries": t.array(
                t.proxy(renames["AccountstatusesCustomBatchResponseEntryIn"])
            ).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["AccountstatusesCustomBatchResponseIn"])
    types["AccountstatusesCustomBatchResponseOut"] = t.struct(
        {
            "entries": t.array(
                t.proxy(renames["AccountstatusesCustomBatchResponseEntryOut"])
            ).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountstatusesCustomBatchResponseOut"])
    types["OrderIn"] = t.struct(
        {
            "pickupDetails": t.proxy(renames["OrderPickupDetailsIn"]).optional(),
            "placedDate": t.string().optional(),
            "netPriceAmount": t.proxy(renames["PriceIn"]).optional(),
            "paymentStatus": t.string().optional(),
            "annotations": t.array(
                t.proxy(renames["OrderOrderAnnotationIn"])
            ).optional(),
            "taxCollector": t.string().optional(),
            "shippingCost": t.proxy(renames["PriceIn"]).optional(),
            "shipments": t.array(t.proxy(renames["OrderShipmentIn"])).optional(),
            "shippingCostTax": t.proxy(renames["PriceIn"]).optional(),
            "acknowledged": t.boolean().optional(),
            "merchantId": t.string(),
            "netTaxAmount": t.proxy(renames["PriceIn"]).optional(),
            "promotions": t.array(t.proxy(renames["OrderPromotionIn"])).optional(),
            "deliveryDetails": t.proxy(renames["OrderDeliveryDetailsIn"]).optional(),
            "merchantOrderId": t.string().optional(),
            "id": t.string().optional(),
            "status": t.string().optional(),
            "refunds": t.array(t.proxy(renames["OrderRefundIn"])).optional(),
            "customer": t.proxy(renames["OrderCustomerIn"]).optional(),
            "lineItems": t.array(t.proxy(renames["OrderLineItemIn"])).optional(),
            "kind": t.string().optional(),
            "billingAddress": t.proxy(renames["OrderAddressIn"]).optional(),
        }
    ).named(renames["OrderIn"])
    types["OrderOut"] = t.struct(
        {
            "pickupDetails": t.proxy(renames["OrderPickupDetailsOut"]).optional(),
            "placedDate": t.string().optional(),
            "netPriceAmount": t.proxy(renames["PriceOut"]).optional(),
            "paymentStatus": t.string().optional(),
            "annotations": t.array(
                t.proxy(renames["OrderOrderAnnotationOut"])
            ).optional(),
            "taxCollector": t.string().optional(),
            "shippingCost": t.proxy(renames["PriceOut"]).optional(),
            "shipments": t.array(t.proxy(renames["OrderShipmentOut"])).optional(),
            "shippingCostTax": t.proxy(renames["PriceOut"]).optional(),
            "acknowledged": t.boolean().optional(),
            "merchantId": t.string(),
            "netTaxAmount": t.proxy(renames["PriceOut"]).optional(),
            "promotions": t.array(t.proxy(renames["OrderPromotionOut"])).optional(),
            "deliveryDetails": t.proxy(renames["OrderDeliveryDetailsOut"]).optional(),
            "merchantOrderId": t.string().optional(),
            "id": t.string().optional(),
            "status": t.string().optional(),
            "refunds": t.array(t.proxy(renames["OrderRefundOut"])).optional(),
            "customer": t.proxy(renames["OrderCustomerOut"]).optional(),
            "lineItems": t.array(t.proxy(renames["OrderLineItemOut"])).optional(),
            "kind": t.string().optional(),
            "billingAddress": t.proxy(renames["OrderAddressOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderOut"])
    types["ReturnPolicyOnlineIn"] = t.struct(
        {
            "returnMethods": t.array(t.string()).optional(),
            "restockingFee": t.proxy(
                renames["ReturnPolicyOnlineRestockingFeeIn"]
            ).optional(),
            "name": t.string().optional(),
            "returnReasonCategoryInfo": t.array(
                t.proxy(renames["ReturnPolicyOnlineReturnReasonCategoryInfoIn"])
            ).optional(),
            "label": t.string().optional(),
            "countries": t.array(t.string()).optional(),
            "policy": t.proxy(renames["ReturnPolicyOnlinePolicyIn"]).optional(),
            "itemConditions": t.array(t.string()).optional(),
            "returnPolicyUri": t.string().optional(),
        }
    ).named(renames["ReturnPolicyOnlineIn"])
    types["ReturnPolicyOnlineOut"] = t.struct(
        {
            "returnMethods": t.array(t.string()).optional(),
            "restockingFee": t.proxy(
                renames["ReturnPolicyOnlineRestockingFeeOut"]
            ).optional(),
            "name": t.string().optional(),
            "returnReasonCategoryInfo": t.array(
                t.proxy(renames["ReturnPolicyOnlineReturnReasonCategoryInfoOut"])
            ).optional(),
            "label": t.string().optional(),
            "countries": t.array(t.string()).optional(),
            "policy": t.proxy(renames["ReturnPolicyOnlinePolicyOut"]).optional(),
            "itemConditions": t.array(t.string()).optional(),
            "returnPolicyId": t.string().optional(),
            "returnPolicyUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReturnPolicyOnlineOut"])
    types["PromotionPromotionStatusPromotionIssueIn"] = t.struct(
        {"detail": t.string().optional(), "code": t.string().optional()}
    ).named(renames["PromotionPromotionStatusPromotionIssueIn"])
    types["PromotionPromotionStatusPromotionIssueOut"] = t.struct(
        {
            "detail": t.string().optional(),
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PromotionPromotionStatusPromotionIssueOut"])
    types["SettlementtransactionsListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "resources": t.array(t.proxy(renames["SettlementTransactionIn"])),
            "kind": t.string().optional(),
        }
    ).named(renames["SettlementtransactionsListResponseIn"])
    types["SettlementtransactionsListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "resources": t.array(t.proxy(renames["SettlementTransactionOut"])),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SettlementtransactionsListResponseOut"])
    types["AccountstatusesCustomBatchRequestEntryIn"] = t.struct(
        {
            "merchantId": t.string().optional(),
            "method": t.string().optional(),
            "batchId": t.integer().optional(),
            "destinations": t.array(t.string()).optional(),
            "accountId": t.string().optional(),
        }
    ).named(renames["AccountstatusesCustomBatchRequestEntryIn"])
    types["AccountstatusesCustomBatchRequestEntryOut"] = t.struct(
        {
            "merchantId": t.string().optional(),
            "method": t.string().optional(),
            "batchId": t.integer().optional(),
            "destinations": t.array(t.string()).optional(),
            "accountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountstatusesCustomBatchRequestEntryOut"])
    types["ReturnpolicyListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "resources": t.array(t.proxy(renames["ReturnPolicyIn"])),
        }
    ).named(renames["ReturnpolicyListResponseIn"])
    types["ReturnpolicyListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "resources": t.array(t.proxy(renames["ReturnPolicyOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReturnpolicyListResponseOut"])
    types["PosDataProvidersIn"] = t.struct(
        {
            "country": t.string().optional(),
            "posDataProviders": t.array(
                t.proxy(renames["PosDataProvidersPosDataProviderIn"])
            ).optional(),
        }
    ).named(renames["PosDataProvidersIn"])
    types["PosDataProvidersOut"] = t.struct(
        {
            "country": t.string().optional(),
            "posDataProviders": t.array(
                t.proxy(renames["PosDataProvidersPosDataProviderOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PosDataProvidersOut"])
    types["AccountAdsLinkIn"] = t.struct(
        {"adsId": t.string().optional(), "status": t.string().optional()}
    ).named(renames["AccountAdsLinkIn"])
    types["AccountAdsLinkOut"] = t.struct(
        {
            "adsId": t.string().optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountAdsLinkOut"])
    types["GenerateRecommendationsResponseIn"] = t.struct(
        {"recommendations": t.array(t.proxy(renames["RecommendationIn"])).optional()}
    ).named(renames["GenerateRecommendationsResponseIn"])
    types["GenerateRecommendationsResponseOut"] = t.struct(
        {
            "recommendations": t.array(
                t.proxy(renames["RecommendationOut"])
            ).optional(),
            "responseToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateRecommendationsResponseOut"])
    types["ShoppingAdsProgramStatusIn"] = t.struct(
        {
            "regionStatuses": t.array(
                t.proxy(renames["ShoppingAdsProgramStatusRegionStatusIn"])
            ).optional(),
            "globalState": t.string().optional(),
        }
    ).named(renames["ShoppingAdsProgramStatusIn"])
    types["ShoppingAdsProgramStatusOut"] = t.struct(
        {
            "regionStatuses": t.array(
                t.proxy(renames["ShoppingAdsProgramStatusRegionStatusOut"])
            ).optional(),
            "globalState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShoppingAdsProgramStatusOut"])
    types["LiasettingsSetInventoryVerificationContactResponseIn"] = t.struct(
        {"kind": t.string().optional()}
    ).named(renames["LiasettingsSetInventoryVerificationContactResponseIn"])
    types["LiasettingsSetInventoryVerificationContactResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiasettingsSetInventoryVerificationContactResponseOut"])
    types["OrdersCustomBatchRequestEntryShipLineItemsShipmentInfoIn"] = t.struct(
        {
            "carrier": t.string().optional(),
            "trackingId": t.string().optional(),
            "shipmentId": t.string(),
        }
    ).named(renames["OrdersCustomBatchRequestEntryShipLineItemsShipmentInfoIn"])
    types["OrdersCustomBatchRequestEntryShipLineItemsShipmentInfoOut"] = t.struct(
        {
            "carrier": t.string().optional(),
            "trackingId": t.string().optional(),
            "shipmentId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersCustomBatchRequestEntryShipLineItemsShipmentInfoOut"])
    types["RecommendationIn"] = t.struct(
        {
            "paid": t.boolean().optional(),
            "recommendationName": t.string().optional(),
            "numericalImpact": t.integer().optional(),
            "defaultCallToAction": t.proxy(
                renames["RecommendationCallToActionIn"]
            ).optional(),
            "title": t.string().optional(),
            "defaultDescription": t.string().optional(),
            "subType": t.string().optional(),
        }
    ).named(renames["RecommendationIn"])
    types["RecommendationOut"] = t.struct(
        {
            "additionalDescriptions": t.array(
                t.proxy(renames["RecommendationDescriptionOut"])
            ).optional(),
            "creative": t.array(
                t.proxy(renames["RecommendationCreativeOut"])
            ).optional(),
            "paid": t.boolean().optional(),
            "type": t.string().optional(),
            "recommendationName": t.string().optional(),
            "numericalImpact": t.integer().optional(),
            "defaultCallToAction": t.proxy(
                renames["RecommendationCallToActionOut"]
            ).optional(),
            "additionalCallToAction": t.array(
                t.proxy(renames["RecommendationCallToActionOut"])
            ).optional(),
            "title": t.string().optional(),
            "defaultDescription": t.string().optional(),
            "subType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RecommendationOut"])
    types["ProductstatusesCustomBatchRequestEntryIn"] = t.struct(
        {
            "merchantId": t.string().optional(),
            "method": t.string().optional(),
            "includeAttributes": t.boolean().optional(),
            "destinations": t.array(t.string()).optional(),
            "productId": t.string().optional(),
            "batchId": t.integer().optional(),
        }
    ).named(renames["ProductstatusesCustomBatchRequestEntryIn"])
    types["ProductstatusesCustomBatchRequestEntryOut"] = t.struct(
        {
            "merchantId": t.string().optional(),
            "method": t.string().optional(),
            "includeAttributes": t.boolean().optional(),
            "destinations": t.array(t.string()).optional(),
            "productId": t.string().optional(),
            "batchId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductstatusesCustomBatchRequestEntryOut"])
    types["OrdersCustomBatchRequestEntryCreateTestReturnReturnItemIn"] = t.struct(
        {"lineItemId": t.string().optional(), "quantity": t.integer().optional()}
    ).named(renames["OrdersCustomBatchRequestEntryCreateTestReturnReturnItemIn"])
    types["OrdersCustomBatchRequestEntryCreateTestReturnReturnItemOut"] = t.struct(
        {
            "lineItemId": t.string().optional(),
            "quantity": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersCustomBatchRequestEntryCreateTestReturnReturnItemOut"])
    types["RegionPostalCodeAreaPostalCodeRangeIn"] = t.struct(
        {"begin": t.string(), "end": t.string().optional()}
    ).named(renames["RegionPostalCodeAreaPostalCodeRangeIn"])
    types["RegionPostalCodeAreaPostalCodeRangeOut"] = t.struct(
        {
            "begin": t.string(),
            "end": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegionPostalCodeAreaPostalCodeRangeOut"])
    types["MethodQuotaIn"] = t.struct(
        {
            "method": t.string().optional(),
            "quotaUsage": t.string().optional(),
            "quotaLimit": t.string().optional(),
        }
    ).named(renames["MethodQuotaIn"])
    types["MethodQuotaOut"] = t.struct(
        {
            "method": t.string().optional(),
            "quotaUsage": t.string().optional(),
            "quotaLimit": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MethodQuotaOut"])
    types["ProductUnitPricingMeasureIn"] = t.struct(
        {"value": t.number().optional(), "unit": t.string().optional()}
    ).named(renames["ProductUnitPricingMeasureIn"])
    types["ProductUnitPricingMeasureOut"] = t.struct(
        {
            "value": t.number().optional(),
            "unit": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductUnitPricingMeasureOut"])
    types["DatafeedsCustomBatchResponseIn"] = t.struct(
        {
            "entries": t.array(
                t.proxy(renames["DatafeedsCustomBatchResponseEntryIn"])
            ).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["DatafeedsCustomBatchResponseIn"])
    types["DatafeedsCustomBatchResponseOut"] = t.struct(
        {
            "entries": t.array(
                t.proxy(renames["DatafeedsCustomBatchResponseEntryOut"])
            ).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatafeedsCustomBatchResponseOut"])
    types["CollectionFeaturedProductIn"] = t.struct(
        {"y": t.number(), "offerId": t.string().optional(), "x": t.number()}
    ).named(renames["CollectionFeaturedProductIn"])
    types["CollectionFeaturedProductOut"] = t.struct(
        {
            "y": t.number(),
            "offerId": t.string().optional(),
            "x": t.number(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CollectionFeaturedProductOut"])
    types["OrderreturnsProcessResponseIn"] = t.struct(
        {"kind": t.string().optional(), "executionStatus": t.string().optional()}
    ).named(renames["OrderreturnsProcessResponseIn"])
    types["OrderreturnsProcessResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "executionStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderreturnsProcessResponseOut"])
    types["ShippingsettingsCustomBatchResponseEntryIn"] = t.struct(
        {
            "errors": t.proxy(renames["ErrorsIn"]).optional(),
            "shippingSettings": t.proxy(renames["ShippingSettingsIn"]).optional(),
            "kind": t.string().optional(),
            "batchId": t.integer().optional(),
        }
    ).named(renames["ShippingsettingsCustomBatchResponseEntryIn"])
    types["ShippingsettingsCustomBatchResponseEntryOut"] = t.struct(
        {
            "errors": t.proxy(renames["ErrorsOut"]).optional(),
            "shippingSettings": t.proxy(renames["ShippingSettingsOut"]).optional(),
            "kind": t.string().optional(),
            "batchId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShippingsettingsCustomBatchResponseEntryOut"])
    types["DatafeedsCustomBatchRequestIn"] = t.struct(
        {
            "entries": t.array(
                t.proxy(renames["DatafeedsCustomBatchRequestEntryIn"])
            ).optional()
        }
    ).named(renames["DatafeedsCustomBatchRequestIn"])
    types["DatafeedsCustomBatchRequestOut"] = t.struct(
        {
            "entries": t.array(
                t.proxy(renames["DatafeedsCustomBatchRequestEntryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatafeedsCustomBatchRequestOut"])
    types["AccountstatusesCustomBatchResponseEntryIn"] = t.struct(
        {
            "batchId": t.integer().optional(),
            "errors": t.proxy(renames["ErrorsIn"]).optional(),
            "accountStatus": t.proxy(renames["AccountStatusIn"]).optional(),
        }
    ).named(renames["AccountstatusesCustomBatchResponseEntryIn"])
    types["AccountstatusesCustomBatchResponseEntryOut"] = t.struct(
        {
            "batchId": t.integer().optional(),
            "errors": t.proxy(renames["ErrorsOut"]).optional(),
            "accountStatus": t.proxy(renames["AccountStatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountstatusesCustomBatchResponseEntryOut"])
    types["RepricingRuleIn"] = t.struct(
        {
            "title": t.string().optional(),
            "statsBasedRule": t.proxy(
                renames["RepricingRuleStatsBasedRuleIn"]
            ).optional(),
            "effectiveTimePeriod": t.proxy(renames["RepricingRuleEffectiveTimeIn"]),
            "restriction": t.proxy(renames["RepricingRuleRestrictionIn"]),
            "type": t.string(),
            "countryCode": t.string(),
            "eligibleOfferMatcher": t.proxy(
                renames["RepricingRuleEligibleOfferMatcherIn"]
            ),
            "languageCode": t.string(),
            "paused": t.boolean().optional(),
            "cogsBasedRule": t.proxy(
                renames["RepricingRuleCostOfGoodsSaleRuleIn"]
            ).optional(),
        }
    ).named(renames["RepricingRuleIn"])
    types["RepricingRuleOut"] = t.struct(
        {
            "title": t.string().optional(),
            "statsBasedRule": t.proxy(
                renames["RepricingRuleStatsBasedRuleOut"]
            ).optional(),
            "effectiveTimePeriod": t.proxy(renames["RepricingRuleEffectiveTimeOut"]),
            "restriction": t.proxy(renames["RepricingRuleRestrictionOut"]),
            "type": t.string(),
            "countryCode": t.string(),
            "ruleId": t.string().optional(),
            "merchantId": t.string().optional(),
            "eligibleOfferMatcher": t.proxy(
                renames["RepricingRuleEligibleOfferMatcherOut"]
            ),
            "languageCode": t.string(),
            "paused": t.boolean().optional(),
            "cogsBasedRule": t.proxy(
                renames["RepricingRuleCostOfGoodsSaleRuleOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepricingRuleOut"])
    types["ShipmentInvoiceIn"] = t.struct(
        {
            "shipmentGroupId": t.string().optional(),
            "invoiceSummary": t.proxy(renames["InvoiceSummaryIn"]).optional(),
            "lineItemInvoices": t.array(
                t.proxy(renames["ShipmentInvoiceLineItemInvoiceIn"])
            ).optional(),
        }
    ).named(renames["ShipmentInvoiceIn"])
    types["ShipmentInvoiceOut"] = t.struct(
        {
            "shipmentGroupId": t.string().optional(),
            "invoiceSummary": t.proxy(renames["InvoiceSummaryOut"]).optional(),
            "lineItemInvoices": t.array(
                t.proxy(renames["ShipmentInvoiceLineItemInvoiceOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShipmentInvoiceOut"])
    types["FreeListingsProgramStatusIn"] = t.struct(
        {
            "globalState": t.string().optional(),
            "regionStatuses": t.array(
                t.proxy(renames["FreeListingsProgramStatusRegionStatusIn"])
            ).optional(),
        }
    ).named(renames["FreeListingsProgramStatusIn"])
    types["FreeListingsProgramStatusOut"] = t.struct(
        {
            "globalState": t.string().optional(),
            "regionStatuses": t.array(
                t.proxy(renames["FreeListingsProgramStatusRegionStatusOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FreeListingsProgramStatusOut"])
    types["BestSellersIn"] = t.struct(
        {
            "reportGranularity": t.string().optional(),
            "rank": t.string().optional(),
            "categoryId": t.string().optional(),
            "previousRank": t.string().optional(),
            "relativeDemandChange": t.string().optional(),
            "reportDate": t.proxy(renames["DateIn"]).optional(),
            "previousRelativeDemand": t.string().optional(),
            "countryCode": t.string().optional(),
            "relativeDemand": t.string().optional(),
        }
    ).named(renames["BestSellersIn"])
    types["BestSellersOut"] = t.struct(
        {
            "reportGranularity": t.string().optional(),
            "rank": t.string().optional(),
            "categoryId": t.string().optional(),
            "previousRank": t.string().optional(),
            "relativeDemandChange": t.string().optional(),
            "reportDate": t.proxy(renames["DateOut"]).optional(),
            "previousRelativeDemand": t.string().optional(),
            "countryCode": t.string().optional(),
            "relativeDemand": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BestSellersOut"])
    types["PostalCodeRangeIn"] = t.struct(
        {
            "postalCodeRangeEnd": t.string().optional(),
            "postalCodeRangeBegin": t.string().optional(),
        }
    ).named(renames["PostalCodeRangeIn"])
    types["PostalCodeRangeOut"] = t.struct(
        {
            "postalCodeRangeEnd": t.string().optional(),
            "postalCodeRangeBegin": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostalCodeRangeOut"])
    types["OrderLineItemShippingDetailsIn"] = t.struct(
        {
            "type": t.string().optional(),
            "shipByDate": t.string(),
            "deliverByDate": t.string(),
            "pickupPromiseInMinutes": t.integer().optional(),
            "method": t.proxy(renames["OrderLineItemShippingDetailsMethodIn"]),
        }
    ).named(renames["OrderLineItemShippingDetailsIn"])
    types["OrderLineItemShippingDetailsOut"] = t.struct(
        {
            "type": t.string().optional(),
            "shipByDate": t.string(),
            "deliverByDate": t.string(),
            "pickupPromiseInMinutes": t.integer().optional(),
            "method": t.proxy(renames["OrderLineItemShippingDetailsMethodOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderLineItemShippingDetailsOut"])
    types["TestOrderPickupDetailsPickupPersonIn"] = t.struct(
        {"name": t.string(), "phoneNumber": t.string()}
    ).named(renames["TestOrderPickupDetailsPickupPersonIn"])
    types["TestOrderPickupDetailsPickupPersonOut"] = t.struct(
        {
            "name": t.string(),
            "phoneNumber": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestOrderPickupDetailsPickupPersonOut"])
    types["AccountsClaimWebsiteResponseIn"] = t.struct(
        {"kind": t.string().optional()}
    ).named(renames["AccountsClaimWebsiteResponseIn"])
    types["AccountsClaimWebsiteResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountsClaimWebsiteResponseOut"])
    types["SearchResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "results": t.array(t.proxy(renames["ReportRowIn"])).optional(),
        }
    ).named(renames["SearchResponseIn"])
    types["SearchResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "results": t.array(t.proxy(renames["ReportRowOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchResponseOut"])
    types["LiasettingsListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "resources": t.array(t.proxy(renames["LiaSettingsIn"])),
            "kind": t.string().optional(),
        }
    ).named(renames["LiasettingsListResponseIn"])
    types["LiasettingsListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "resources": t.array(t.proxy(renames["LiaSettingsOut"])),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiasettingsListResponseOut"])
    types["SettlementTransactionIdentifiersIn"] = t.struct(
        {
            "transactionId": t.string().optional(),
            "shipmentIds": t.array(t.string()).optional(),
            "merchantOrderId": t.string().optional(),
            "settlementEntryId": t.string().optional(),
            "orderItemId": t.string().optional(),
            "adjustmentId": t.string().optional(),
        }
    ).named(renames["SettlementTransactionIdentifiersIn"])
    types["SettlementTransactionIdentifiersOut"] = t.struct(
        {
            "transactionId": t.string().optional(),
            "shipmentIds": t.array(t.string()).optional(),
            "merchantOrderId": t.string().optional(),
            "settlementEntryId": t.string().optional(),
            "orderItemId": t.string().optional(),
            "adjustmentId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SettlementTransactionIdentifiersOut"])
    types["OrdersCancelLineItemRequestIn"] = t.struct(
        {
            "productId": t.string().optional(),
            "reasonText": t.string().optional(),
            "reason": t.string().optional(),
            "lineItemId": t.string().optional(),
            "quantity": t.integer().optional(),
            "operationId": t.string().optional(),
        }
    ).named(renames["OrdersCancelLineItemRequestIn"])
    types["OrdersCancelLineItemRequestOut"] = t.struct(
        {
            "productId": t.string().optional(),
            "reasonText": t.string().optional(),
            "reason": t.string().optional(),
            "lineItemId": t.string().optional(),
            "quantity": t.integer().optional(),
            "operationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersCancelLineItemRequestOut"])
    types["ProductstatusesCustomBatchResponseEntryIn"] = t.struct(
        {
            "productStatus": t.proxy(renames["ProductStatusIn"]).optional(),
            "kind": t.string().optional(),
            "errors": t.proxy(renames["ErrorsIn"]).optional(),
            "batchId": t.integer().optional(),
        }
    ).named(renames["ProductstatusesCustomBatchResponseEntryIn"])
    types["ProductstatusesCustomBatchResponseEntryOut"] = t.struct(
        {
            "productStatus": t.proxy(renames["ProductStatusOut"]).optional(),
            "kind": t.string().optional(),
            "errors": t.proxy(renames["ErrorsOut"]).optional(),
            "batchId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductstatusesCustomBatchResponseEntryOut"])
    types["PickupServicesPickupServiceIn"] = t.struct(
        {
            "carrierName": t.string().optional(),
            "country": t.string().optional(),
            "serviceName": t.string().optional(),
        }
    ).named(renames["PickupServicesPickupServiceIn"])
    types["PickupServicesPickupServiceOut"] = t.struct(
        {
            "carrierName": t.string().optional(),
            "country": t.string().optional(),
            "serviceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PickupServicesPickupServiceOut"])
    types["ReturnaddressCustomBatchRequestIn"] = t.struct(
        {
            "entries": t.array(
                t.proxy(renames["ReturnaddressCustomBatchRequestEntryIn"])
            ).optional()
        }
    ).named(renames["ReturnaddressCustomBatchRequestIn"])
    types["ReturnaddressCustomBatchRequestOut"] = t.struct(
        {
            "entries": t.array(
                t.proxy(renames["ReturnaddressCustomBatchRequestEntryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReturnaddressCustomBatchRequestOut"])
    types["BusinessDayConfigIn"] = t.struct(
        {"businessDays": t.array(t.string()).optional()}
    ).named(renames["BusinessDayConfigIn"])
    types["BusinessDayConfigOut"] = t.struct(
        {
            "businessDays": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BusinessDayConfigOut"])
    types["WarehouseCutoffTimeIn"] = t.struct(
        {"minute": t.integer(), "hour": t.integer()}
    ).named(renames["WarehouseCutoffTimeIn"])
    types["WarehouseCutoffTimeOut"] = t.struct(
        {
            "minute": t.integer(),
            "hour": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WarehouseCutoffTimeOut"])
    types["ActivateBuyOnGoogleProgramRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ActivateBuyOnGoogleProgramRequestIn"])
    types["ActivateBuyOnGoogleProgramRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ActivateBuyOnGoogleProgramRequestOut"])
    types["PubsubNotificationSettingsIn"] = t.struct(
        {
            "cloudTopicName": t.string().optional(),
            "registeredEvents": t.array(t.string()).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["PubsubNotificationSettingsIn"])
    types["PubsubNotificationSettingsOut"] = t.struct(
        {
            "cloudTopicName": t.string().optional(),
            "registeredEvents": t.array(t.string()).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PubsubNotificationSettingsOut"])
    types["RepricingRuleReportIn"] = t.struct(
        {
            "date": t.proxy(renames["DateIn"]).optional(),
            "type": t.string().optional(),
            "inapplicabilityDetails": t.array(
                t.proxy(renames["InapplicabilityDetailsIn"])
            ).optional(),
            "totalGmv": t.proxy(renames["PriceAmountIn"]).optional(),
            "inapplicableProducts": t.array(t.string()).optional(),
            "orderItemCount": t.integer().optional(),
            "impactedProducts": t.array(t.string()).optional(),
            "ruleId": t.string().optional(),
            "buyboxWinningRuleStats": t.proxy(
                renames["RepricingRuleReportBuyboxWinningRuleStatsIn"]
            ).optional(),
        }
    ).named(renames["RepricingRuleReportIn"])
    types["RepricingRuleReportOut"] = t.struct(
        {
            "date": t.proxy(renames["DateOut"]).optional(),
            "type": t.string().optional(),
            "inapplicabilityDetails": t.array(
                t.proxy(renames["InapplicabilityDetailsOut"])
            ).optional(),
            "totalGmv": t.proxy(renames["PriceAmountOut"]).optional(),
            "inapplicableProducts": t.array(t.string()).optional(),
            "orderItemCount": t.integer().optional(),
            "impactedProducts": t.array(t.string()).optional(),
            "ruleId": t.string().optional(),
            "buyboxWinningRuleStats": t.proxy(
                renames["RepricingRuleReportBuyboxWinningRuleStatsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepricingRuleReportOut"])
    types["LiaCountrySettingsIn"] = t.struct(
        {
            "hostedLocalStorefrontActive": t.boolean().optional(),
            "country": t.string(),
            "inventory": t.proxy(renames["LiaInventorySettingsIn"]).optional(),
            "onDisplayToOrder": t.proxy(
                renames["LiaOnDisplayToOrderSettingsIn"]
            ).optional(),
            "posDataProvider": t.proxy(renames["LiaPosDataProviderIn"]).optional(),
            "about": t.proxy(renames["LiaAboutPageSettingsIn"]).optional(),
            "storePickupActive": t.boolean().optional(),
        }
    ).named(renames["LiaCountrySettingsIn"])
    types["LiaCountrySettingsOut"] = t.struct(
        {
            "hostedLocalStorefrontActive": t.boolean().optional(),
            "country": t.string(),
            "inventory": t.proxy(renames["LiaInventorySettingsOut"]).optional(),
            "onDisplayToOrder": t.proxy(
                renames["LiaOnDisplayToOrderSettingsOut"]
            ).optional(),
            "posDataProvider": t.proxy(renames["LiaPosDataProviderOut"]).optional(),
            "about": t.proxy(renames["LiaAboutPageSettingsOut"]).optional(),
            "storePickupActive": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiaCountrySettingsOut"])
    types["CollectionStatusIn"] = t.struct(
        {
            "destinationStatuses": t.array(
                t.proxy(renames["CollectionStatusDestinationStatusIn"])
            ).optional(),
            "collectionLevelIssuses": t.array(
                t.proxy(renames["CollectionStatusItemLevelIssueIn"])
            ).optional(),
            "id": t.string(),
            "creationDate": t.string().optional(),
            "lastUpdateDate": t.string().optional(),
        }
    ).named(renames["CollectionStatusIn"])
    types["CollectionStatusOut"] = t.struct(
        {
            "destinationStatuses": t.array(
                t.proxy(renames["CollectionStatusDestinationStatusOut"])
            ).optional(),
            "collectionLevelIssuses": t.array(
                t.proxy(renames["CollectionStatusItemLevelIssueOut"])
            ).optional(),
            "id": t.string(),
            "creationDate": t.string().optional(),
            "lastUpdateDate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CollectionStatusOut"])
    types["CustomerReturnReasonIn"] = t.struct(
        {"reasonCode": t.string().optional(), "description": t.string().optional()}
    ).named(renames["CustomerReturnReasonIn"])
    types["CustomerReturnReasonOut"] = t.struct(
        {
            "reasonCode": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomerReturnReasonOut"])
    types["OrderReportDisbursementIn"] = t.struct(
        {
            "disbursementId": t.string().optional(),
            "disbursementDate": t.string().optional(),
            "disbursementCreationDate": t.string().optional(),
            "merchantId": t.string().optional(),
            "disbursementAmount": t.proxy(renames["PriceIn"]).optional(),
        }
    ).named(renames["OrderReportDisbursementIn"])
    types["OrderReportDisbursementOut"] = t.struct(
        {
            "disbursementId": t.string().optional(),
            "disbursementDate": t.string().optional(),
            "disbursementCreationDate": t.string().optional(),
            "merchantId": t.string().optional(),
            "disbursementAmount": t.proxy(renames["PriceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderReportDisbursementOut"])
    types["OrderTrackingSignalShippingInfoIn"] = t.struct(
        {
            "shippingStatus": t.string().optional(),
            "trackingId": t.string().optional(),
            "carrierName": t.string().optional(),
            "shippedTime": t.proxy(renames["DateTimeIn"]).optional(),
            "carrierServiceName": t.string().optional(),
            "originRegionCode": t.string().optional(),
            "actualDeliveryTime": t.proxy(renames["DateTimeIn"]).optional(),
            "originPostalCode": t.string().optional(),
            "latestDeliveryPromiseTime": t.proxy(renames["DateTimeIn"]).optional(),
            "shipmentId": t.string(),
            "earliestDeliveryPromiseTime": t.proxy(renames["DateTimeIn"]).optional(),
        }
    ).named(renames["OrderTrackingSignalShippingInfoIn"])
    types["OrderTrackingSignalShippingInfoOut"] = t.struct(
        {
            "shippingStatus": t.string().optional(),
            "trackingId": t.string().optional(),
            "carrierName": t.string().optional(),
            "shippedTime": t.proxy(renames["DateTimeOut"]).optional(),
            "carrierServiceName": t.string().optional(),
            "originRegionCode": t.string().optional(),
            "actualDeliveryTime": t.proxy(renames["DateTimeOut"]).optional(),
            "originPostalCode": t.string().optional(),
            "latestDeliveryPromiseTime": t.proxy(renames["DateTimeOut"]).optional(),
            "shipmentId": t.string(),
            "earliestDeliveryPromiseTime": t.proxy(renames["DateTimeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderTrackingSignalShippingInfoOut"])
    types["ECommercePlatformLinkInfoIn"] = t.struct(
        {"externalAccountId": t.string().optional()}
    ).named(renames["ECommercePlatformLinkInfoIn"])
    types["ECommercePlatformLinkInfoOut"] = t.struct(
        {
            "externalAccountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ECommercePlatformLinkInfoOut"])
    types["RegionGeoTargetAreaIn"] = t.struct(
        {"geotargetCriteriaIds": t.array(t.string())}
    ).named(renames["RegionGeoTargetAreaIn"])
    types["RegionGeoTargetAreaOut"] = t.struct(
        {
            "geotargetCriteriaIds": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegionGeoTargetAreaOut"])
    types["DeliveryAreaIn"] = t.struct(
        {
            "regionCode": t.string().optional(),
            "postalCodeRange": t.proxy(
                renames["DeliveryAreaPostalCodeRangeIn"]
            ).optional(),
            "countryCode": t.string(),
        }
    ).named(renames["DeliveryAreaIn"])
    types["DeliveryAreaOut"] = t.struct(
        {
            "regionCode": t.string().optional(),
            "postalCodeRange": t.proxy(
                renames["DeliveryAreaPostalCodeRangeOut"]
            ).optional(),
            "countryCode": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeliveryAreaOut"])
    types["ProductWeightIn"] = t.struct(
        {"value": t.number(), "unit": t.string()}
    ).named(renames["ProductWeightIn"])
    types["ProductWeightOut"] = t.struct(
        {
            "value": t.number(),
            "unit": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductWeightOut"])
    types["PosInventoryIn"] = t.struct(
        {
            "contentLanguage": t.string(),
            "storeCode": t.string(),
            "itemId": t.string(),
            "timestamp": t.string(),
            "gtin": t.string().optional(),
            "quantity": t.string(),
            "kind": t.string().optional(),
            "targetCountry": t.string(),
            "price": t.proxy(renames["PriceIn"]),
        }
    ).named(renames["PosInventoryIn"])
    types["PosInventoryOut"] = t.struct(
        {
            "contentLanguage": t.string(),
            "storeCode": t.string(),
            "itemId": t.string(),
            "timestamp": t.string(),
            "gtin": t.string().optional(),
            "quantity": t.string(),
            "kind": t.string().optional(),
            "targetCountry": t.string(),
            "price": t.proxy(renames["PriceOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PosInventoryOut"])
    types["OrderAddressIn"] = t.struct(
        {
            "region": t.string().optional(),
            "postalCode": t.string().optional(),
            "country": t.string().optional(),
            "streetAddress": t.array(t.string()).optional(),
            "recipientName": t.string().optional(),
            "locality": t.string().optional(),
            "isPostOfficeBox": t.boolean().optional(),
            "fullAddress": t.array(t.string()).optional(),
        }
    ).named(renames["OrderAddressIn"])
    types["OrderAddressOut"] = t.struct(
        {
            "region": t.string().optional(),
            "postalCode": t.string().optional(),
            "country": t.string().optional(),
            "streetAddress": t.array(t.string()).optional(),
            "recipientName": t.string().optional(),
            "locality": t.string().optional(),
            "isPostOfficeBox": t.boolean().optional(),
            "fullAddress": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderAddressOut"])
    types["OrdersRefundItemRequestIn"] = t.struct(
        {
            "shipping": t.proxy(
                renames["OrdersCustomBatchRequestEntryRefundItemShippingIn"]
            ).optional(),
            "items": t.array(
                t.proxy(renames["OrdersCustomBatchRequestEntryRefundItemItemIn"])
            ).optional(),
            "reason": t.string().optional(),
            "reasonText": t.string().optional(),
            "operationId": t.string().optional(),
        }
    ).named(renames["OrdersRefundItemRequestIn"])
    types["OrdersRefundItemRequestOut"] = t.struct(
        {
            "shipping": t.proxy(
                renames["OrdersCustomBatchRequestEntryRefundItemShippingOut"]
            ).optional(),
            "items": t.array(
                t.proxy(renames["OrdersCustomBatchRequestEntryRefundItemItemOut"])
            ).optional(),
            "reason": t.string().optional(),
            "reasonText": t.string().optional(),
            "operationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersRefundItemRequestOut"])
    types["ReturnpolicyCustomBatchResponseEntryIn"] = t.struct(
        {
            "returnPolicy": t.proxy(renames["ReturnPolicyIn"]).optional(),
            "kind": t.string().optional(),
            "batchId": t.integer().optional(),
            "errors": t.proxy(renames["ErrorsIn"]).optional(),
        }
    ).named(renames["ReturnpolicyCustomBatchResponseEntryIn"])
    types["ReturnpolicyCustomBatchResponseEntryOut"] = t.struct(
        {
            "returnPolicy": t.proxy(renames["ReturnPolicyOut"]).optional(),
            "kind": t.string().optional(),
            "batchId": t.integer().optional(),
            "errors": t.proxy(renames["ErrorsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReturnpolicyCustomBatchResponseEntryOut"])
    types["TestOrderDeliveryDetailsIn"] = t.struct(
        {
            "phoneNumber": t.string().optional(),
            "isScheduledDelivery": t.boolean().optional(),
            "address": t.proxy(renames["TestOrderAddressIn"]).optional(),
        }
    ).named(renames["TestOrderDeliveryDetailsIn"])
    types["TestOrderDeliveryDetailsOut"] = t.struct(
        {
            "phoneNumber": t.string().optional(),
            "isScheduledDelivery": t.boolean().optional(),
            "address": t.proxy(renames["TestOrderAddressOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestOrderDeliveryDetailsOut"])
    types["AccountBusinessInformationIn"] = t.struct(
        {
            "phoneNumber": t.string().optional(),
            "phoneVerificationStatus": t.string().optional(),
            "koreanBusinessRegistrationNumber": t.string().optional(),
            "customerService": t.proxy(renames["AccountCustomerServiceIn"]).optional(),
            "address": t.proxy(renames["AccountAddressIn"]).optional(),
        }
    ).named(renames["AccountBusinessInformationIn"])
    types["AccountBusinessInformationOut"] = t.struct(
        {
            "phoneNumber": t.string().optional(),
            "phoneVerificationStatus": t.string().optional(),
            "koreanBusinessRegistrationNumber": t.string().optional(),
            "customerService": t.proxy(renames["AccountCustomerServiceOut"]).optional(),
            "address": t.proxy(renames["AccountAddressOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountBusinessInformationOut"])
    types["RepricingRuleStatsBasedRuleIn"] = t.struct(
        {"percentageDelta": t.integer().optional(), "priceDelta": t.string().optional()}
    ).named(renames["RepricingRuleStatsBasedRuleIn"])
    types["RepricingRuleStatsBasedRuleOut"] = t.struct(
        {
            "percentageDelta": t.integer().optional(),
            "priceDelta": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepricingRuleStatsBasedRuleOut"])
    types["OrderLineItemProductFeeIn"] = t.struct(
        {
            "name": t.string().optional(),
            "amount": t.proxy(renames["PriceIn"]).optional(),
        }
    ).named(renames["OrderLineItemProductFeeIn"])
    types["OrderLineItemProductFeeOut"] = t.struct(
        {
            "name": t.string().optional(),
            "amount": t.proxy(renames["PriceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderLineItemProductFeeOut"])
    types["MinimumOrderValueTableStoreCodeSetWithMovIn"] = t.struct(
        {
            "storeCodes": t.array(t.string()).optional(),
            "value": t.proxy(renames["PriceIn"]).optional(),
        }
    ).named(renames["MinimumOrderValueTableStoreCodeSetWithMovIn"])
    types["MinimumOrderValueTableStoreCodeSetWithMovOut"] = t.struct(
        {
            "storeCodes": t.array(t.string()).optional(),
            "value": t.proxy(renames["PriceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MinimumOrderValueTableStoreCodeSetWithMovOut"])
    types["ShipmentTrackingInfoIn"] = t.struct(
        {"trackingNumber": t.string().optional(), "carrier": t.string().optional()}
    ).named(renames["ShipmentTrackingInfoIn"])
    types["ShipmentTrackingInfoOut"] = t.struct(
        {
            "trackingNumber": t.string().optional(),
            "carrier": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShipmentTrackingInfoOut"])
    types["OrdersCreateTestOrderResponseIn"] = t.struct(
        {"kind": t.string().optional(), "orderId": t.string().optional()}
    ).named(renames["OrdersCreateTestOrderResponseIn"])
    types["OrdersCreateTestOrderResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "orderId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersCreateTestOrderResponseOut"])
    types["PosInventoryResponseIn"] = t.struct(
        {
            "quantity": t.string(),
            "storeCode": t.string(),
            "gtin": t.string().optional(),
            "contentLanguage": t.string(),
            "price": t.proxy(renames["PriceIn"]),
            "targetCountry": t.string(),
            "kind": t.string().optional(),
            "timestamp": t.string(),
            "itemId": t.string(),
        }
    ).named(renames["PosInventoryResponseIn"])
    types["PosInventoryResponseOut"] = t.struct(
        {
            "quantity": t.string(),
            "storeCode": t.string(),
            "gtin": t.string().optional(),
            "contentLanguage": t.string(),
            "price": t.proxy(renames["PriceOut"]),
            "targetCountry": t.string(),
            "kind": t.string().optional(),
            "timestamp": t.string(),
            "itemId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PosInventoryResponseOut"])
    types["LiasettingsRequestGmbAccessResponseIn"] = t.struct(
        {"kind": t.string().optional()}
    ).named(renames["LiasettingsRequestGmbAccessResponseIn"])
    types["LiasettingsRequestGmbAccessResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiasettingsRequestGmbAccessResponseOut"])
    types["AccountsCustomBatchResponseEntryIn"] = t.struct(
        {
            "batchId": t.integer().optional(),
            "kind": t.string().optional(),
            "account": t.proxy(renames["AccountIn"]).optional(),
            "errors": t.proxy(renames["ErrorsIn"]).optional(),
        }
    ).named(renames["AccountsCustomBatchResponseEntryIn"])
    types["AccountsCustomBatchResponseEntryOut"] = t.struct(
        {
            "batchId": t.integer().optional(),
            "kind": t.string().optional(),
            "account": t.proxy(renames["AccountOut"]).optional(),
            "errors": t.proxy(renames["ErrorsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountsCustomBatchResponseEntryOut"])
    types["PromotionIn"] = t.struct(
        {
            "redemptionChannel": t.array(t.string()),
            "storeCodeExclusion": t.array(t.string()).optional(),
            "brand": t.array(t.string()).optional(),
            "targetCountry": t.string(),
            "moneyBudget": t.proxy(renames["PriceAmountIn"]).optional(),
            "percentOff": t.integer().optional(),
            "orderLimit": t.integer().optional(),
            "promotionDisplayTimePeriod": t.proxy(renames["TimePeriodIn"]).optional(),
            "getThisQuantityDiscounted": t.integer().optional(),
            "itemIdExclusion": t.array(t.string()).optional(),
            "minimumPurchaseQuantity": t.integer().optional(),
            "promotionEffectiveTimePeriod": t.proxy(renames["TimePeriodIn"]),
            "productType": t.array(t.string()).optional(),
            "minimumPurchaseAmount": t.proxy(renames["PriceAmountIn"]).optional(),
            "promotionId": t.string(),
            "longTitle": t.string(),
            "storeCode": t.array(t.string()).optional(),
            "storeApplicability": t.string().optional(),
            "productApplicability": t.string(),
            "promotionDisplayDates": t.string().optional(),
            "itemGroupId": t.array(t.string()).optional(),
            "moneyOffAmount": t.proxy(renames["PriceAmountIn"]).optional(),
            "offerType": t.string(),
            "itemId": t.array(t.string()).optional(),
            "genericRedemptionCode": t.string().optional(),
            "promotionEffectiveDates": t.string().optional(),
            "freeGiftDescription": t.string().optional(),
            "itemGroupIdExclusion": t.array(t.string()).optional(),
            "freeGiftValue": t.proxy(renames["PriceAmountIn"]).optional(),
            "freeGiftItemId": t.string().optional(),
            "shippingServiceNames": t.array(t.string()).optional(),
            "couponValueType": t.string(),
            "promotionDestinationIds": t.array(t.string()).optional(),
            "brandExclusion": t.array(t.string()).optional(),
            "limitQuantity": t.integer().optional(),
            "promotionUrl": t.string().optional(),
            "contentLanguage": t.string(),
            "productTypeExclusion": t.array(t.string()).optional(),
            "limitValue": t.proxy(renames["PriceAmountIn"]).optional(),
        }
    ).named(renames["PromotionIn"])
    types["PromotionOut"] = t.struct(
        {
            "redemptionChannel": t.array(t.string()),
            "storeCodeExclusion": t.array(t.string()).optional(),
            "brand": t.array(t.string()).optional(),
            "id": t.string(),
            "targetCountry": t.string(),
            "moneyBudget": t.proxy(renames["PriceAmountOut"]).optional(),
            "percentOff": t.integer().optional(),
            "orderLimit": t.integer().optional(),
            "promotionDisplayTimePeriod": t.proxy(renames["TimePeriodOut"]).optional(),
            "getThisQuantityDiscounted": t.integer().optional(),
            "itemIdExclusion": t.array(t.string()).optional(),
            "minimumPurchaseQuantity": t.integer().optional(),
            "promotionEffectiveTimePeriod": t.proxy(renames["TimePeriodOut"]),
            "promotionStatus": t.proxy(
                renames["PromotionPromotionStatusOut"]
            ).optional(),
            "productType": t.array(t.string()).optional(),
            "minimumPurchaseAmount": t.proxy(renames["PriceAmountOut"]).optional(),
            "promotionId": t.string(),
            "longTitle": t.string(),
            "storeCode": t.array(t.string()).optional(),
            "storeApplicability": t.string().optional(),
            "productApplicability": t.string(),
            "promotionDisplayDates": t.string().optional(),
            "itemGroupId": t.array(t.string()).optional(),
            "moneyOffAmount": t.proxy(renames["PriceAmountOut"]).optional(),
            "offerType": t.string(),
            "itemId": t.array(t.string()).optional(),
            "genericRedemptionCode": t.string().optional(),
            "promotionEffectiveDates": t.string().optional(),
            "freeGiftDescription": t.string().optional(),
            "itemGroupIdExclusion": t.array(t.string()).optional(),
            "freeGiftValue": t.proxy(renames["PriceAmountOut"]).optional(),
            "freeGiftItemId": t.string().optional(),
            "shippingServiceNames": t.array(t.string()).optional(),
            "couponValueType": t.string(),
            "promotionDestinationIds": t.array(t.string()).optional(),
            "brandExclusion": t.array(t.string()).optional(),
            "limitQuantity": t.integer().optional(),
            "promotionUrl": t.string().optional(),
            "contentLanguage": t.string(),
            "productTypeExclusion": t.array(t.string()).optional(),
            "limitValue": t.proxy(renames["PriceAmountOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PromotionOut"])
    types["OrderPromotionIn"] = t.struct(
        {
            "subtype": t.string(),
            "funder": t.string(),
            "taxValue": t.proxy(renames["PriceIn"]).optional(),
            "type": t.string(),
            "shortTitle": t.string().optional(),
            "priceValue": t.proxy(renames["PriceIn"]).optional(),
            "startTime": t.string().optional(),
            "applicableItems": t.array(
                t.proxy(renames["OrderPromotionItemIn"])
            ).optional(),
            "merchantPromotionId": t.string(),
            "appliedItems": t.array(
                t.proxy(renames["OrderPromotionItemIn"])
            ).optional(),
            "endTime": t.string().optional(),
            "title": t.string(),
        }
    ).named(renames["OrderPromotionIn"])
    types["OrderPromotionOut"] = t.struct(
        {
            "subtype": t.string(),
            "funder": t.string(),
            "taxValue": t.proxy(renames["PriceOut"]).optional(),
            "type": t.string(),
            "shortTitle": t.string().optional(),
            "priceValue": t.proxy(renames["PriceOut"]).optional(),
            "startTime": t.string().optional(),
            "applicableItems": t.array(
                t.proxy(renames["OrderPromotionItemOut"])
            ).optional(),
            "merchantPromotionId": t.string(),
            "appliedItems": t.array(
                t.proxy(renames["OrderPromotionItemOut"])
            ).optional(),
            "endTime": t.string().optional(),
            "title": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderPromotionOut"])
    types["PosCustomBatchResponseEntryIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "inventory": t.proxy(renames["PosInventoryIn"]).optional(),
            "store": t.proxy(renames["PosStoreIn"]).optional(),
            "sale": t.proxy(renames["PosSaleIn"]).optional(),
            "batchId": t.integer().optional(),
            "errors": t.proxy(renames["ErrorsIn"]).optional(),
        }
    ).named(renames["PosCustomBatchResponseEntryIn"])
    types["PosCustomBatchResponseEntryOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "inventory": t.proxy(renames["PosInventoryOut"]).optional(),
            "store": t.proxy(renames["PosStoreOut"]).optional(),
            "sale": t.proxy(renames["PosSaleOut"]).optional(),
            "batchId": t.integer().optional(),
            "errors": t.proxy(renames["ErrorsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PosCustomBatchResponseEntryOut"])
    types["AccounttaxCustomBatchResponseEntryIn"] = t.struct(
        {
            "accountTax": t.proxy(renames["AccountTaxIn"]).optional(),
            "errors": t.proxy(renames["ErrorsIn"]).optional(),
            "kind": t.string().optional(),
            "batchId": t.integer().optional(),
        }
    ).named(renames["AccounttaxCustomBatchResponseEntryIn"])
    types["AccounttaxCustomBatchResponseEntryOut"] = t.struct(
        {
            "accountTax": t.proxy(renames["AccountTaxOut"]).optional(),
            "errors": t.proxy(renames["ErrorsOut"]).optional(),
            "kind": t.string().optional(),
            "batchId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccounttaxCustomBatchResponseEntryOut"])
    types["ServiceStoreConfigIn"] = t.struct(
        {
            "serviceRadius": t.proxy(renames["DistanceIn"]).optional(),
            "storeServiceType": t.string().optional(),
            "cutoffConfig": t.proxy(
                renames["ServiceStoreConfigCutoffConfigIn"]
            ).optional(),
            "storeCodes": t.array(t.string()).optional(),
        }
    ).named(renames["ServiceStoreConfigIn"])
    types["ServiceStoreConfigOut"] = t.struct(
        {
            "serviceRadius": t.proxy(renames["DistanceOut"]).optional(),
            "storeServiceType": t.string().optional(),
            "cutoffConfig": t.proxy(
                renames["ServiceStoreConfigCutoffConfigOut"]
            ).optional(),
            "storeCodes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceStoreConfigOut"])
    types["RequestReviewShoppingAdsRequestIn"] = t.struct(
        {"regionCode": t.string().optional()}
    ).named(renames["RequestReviewShoppingAdsRequestIn"])
    types["RequestReviewShoppingAdsRequestOut"] = t.struct(
        {
            "regionCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestReviewShoppingAdsRequestOut"])
    types["AccountConversionSettingsIn"] = t.struct(
        {"freeListingsAutoTaggingEnabled": t.boolean().optional()}
    ).named(renames["AccountConversionSettingsIn"])
    types["AccountConversionSettingsOut"] = t.struct(
        {
            "freeListingsAutoTaggingEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountConversionSettingsOut"])
    types["AccountAddressIn"] = t.struct(
        {
            "locality": t.string().optional(),
            "streetAddress": t.string().optional(),
            "region": t.string().optional(),
            "country": t.string().optional(),
            "postalCode": t.string().optional(),
        }
    ).named(renames["AccountAddressIn"])
    types["AccountAddressOut"] = t.struct(
        {
            "locality": t.string().optional(),
            "streetAddress": t.string().optional(),
            "region": t.string().optional(),
            "country": t.string().optional(),
            "postalCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountAddressOut"])
    types["RegionPostalCodeAreaIn"] = t.struct(
        {
            "postalCodes": t.array(
                t.proxy(renames["RegionPostalCodeAreaPostalCodeRangeIn"])
            ),
            "regionCode": t.string(),
        }
    ).named(renames["RegionPostalCodeAreaIn"])
    types["RegionPostalCodeAreaOut"] = t.struct(
        {
            "postalCodes": t.array(
                t.proxy(renames["RegionPostalCodeAreaPostalCodeRangeOut"])
            ),
            "regionCode": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegionPostalCodeAreaOut"])
    types["RegionalinventoryCustomBatchResponseEntryIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "regionalInventory": t.proxy(renames["RegionalInventoryIn"]).optional(),
            "errors": t.proxy(renames["ErrorsIn"]).optional(),
            "batchId": t.integer().optional(),
        }
    ).named(renames["RegionalinventoryCustomBatchResponseEntryIn"])
    types["RegionalinventoryCustomBatchResponseEntryOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "regionalInventory": t.proxy(renames["RegionalInventoryOut"]).optional(),
            "errors": t.proxy(renames["ErrorsOut"]).optional(),
            "batchId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegionalinventoryCustomBatchResponseEntryOut"])
    types["AccountCustomerServiceIn"] = t.struct(
        {
            "url": t.string().optional(),
            "email": t.string().optional(),
            "phoneNumber": t.string().optional(),
        }
    ).named(renames["AccountCustomerServiceIn"])
    types["AccountCustomerServiceOut"] = t.struct(
        {
            "url": t.string().optional(),
            "email": t.string().optional(),
            "phoneNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountCustomerServiceOut"])
    types["GmbAccountsGmbAccountIn"] = t.struct(
        {
            "type": t.string().optional(),
            "name": t.string().optional(),
            "email": t.string().optional(),
            "listingCount": t.string().optional(),
        }
    ).named(renames["GmbAccountsGmbAccountIn"])
    types["GmbAccountsGmbAccountOut"] = t.struct(
        {
            "type": t.string().optional(),
            "name": t.string().optional(),
            "email": t.string().optional(),
            "listingCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GmbAccountsGmbAccountOut"])
    types["OrdersListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "resources": t.array(t.proxy(renames["OrderIn"])),
        }
    ).named(renames["OrdersListResponseIn"])
    types["OrdersListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "resources": t.array(t.proxy(renames["OrderOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersListResponseOut"])
    types["ListRepricingRuleReportsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "repricingRuleReports": t.array(
                t.proxy(renames["RepricingRuleReportIn"])
            ).optional(),
        }
    ).named(renames["ListRepricingRuleReportsResponseIn"])
    types["ListRepricingRuleReportsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "repricingRuleReports": t.array(
                t.proxy(renames["RepricingRuleReportOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListRepricingRuleReportsResponseOut"])
    types["HeadersIn"] = t.struct(
        {
            "prices": t.array(t.proxy(renames["PriceIn"])).optional(),
            "numberOfItems": t.array(t.string()).optional(),
            "locations": t.array(t.proxy(renames["LocationIdSetIn"])).optional(),
            "weights": t.array(t.proxy(renames["WeightIn"])).optional(),
            "postalCodeGroupNames": t.array(t.string()).optional(),
        }
    ).named(renames["HeadersIn"])
    types["HeadersOut"] = t.struct(
        {
            "prices": t.array(t.proxy(renames["PriceOut"])).optional(),
            "numberOfItems": t.array(t.string()).optional(),
            "locations": t.array(t.proxy(renames["LocationIdSetOut"])).optional(),
            "weights": t.array(t.proxy(renames["WeightOut"])).optional(),
            "postalCodeGroupNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HeadersOut"])
    types["OrdersCancelTestOrderByCustomerRequestIn"] = t.struct(
        {"reason": t.string().optional()}
    ).named(renames["OrdersCancelTestOrderByCustomerRequestIn"])
    types["OrdersCancelTestOrderByCustomerRequestOut"] = t.struct(
        {
            "reason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersCancelTestOrderByCustomerRequestOut"])
    types["AccountTaxTaxRuleIn"] = t.struct(
        {
            "shippingTaxed": t.boolean().optional(),
            "useGlobalRate": t.boolean().optional(),
            "country": t.string().optional(),
            "locationId": t.string(),
            "ratePercent": t.string().optional(),
        }
    ).named(renames["AccountTaxTaxRuleIn"])
    types["AccountTaxTaxRuleOut"] = t.struct(
        {
            "shippingTaxed": t.boolean().optional(),
            "useGlobalRate": t.boolean().optional(),
            "country": t.string().optional(),
            "locationId": t.string(),
            "ratePercent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountTaxTaxRuleOut"])
    types["OrderOrderAnnotationIn"] = t.struct(
        {"key": t.string().optional(), "value": t.string().optional()}
    ).named(renames["OrderOrderAnnotationIn"])
    types["OrderOrderAnnotationOut"] = t.struct(
        {
            "key": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderOrderAnnotationOut"])
    types["ValueIn"] = t.struct(
        {
            "flatRate": t.proxy(renames["PriceIn"]).optional(),
            "subtableName": t.string().optional(),
            "noShipping": t.boolean().optional(),
            "carrierRateName": t.string().optional(),
            "pricePercentage": t.string().optional(),
        }
    ).named(renames["ValueIn"])
    types["ValueOut"] = t.struct(
        {
            "flatRate": t.proxy(renames["PriceOut"]).optional(),
            "subtableName": t.string().optional(),
            "noShipping": t.boolean().optional(),
            "carrierRateName": t.string().optional(),
            "pricePercentage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValueOut"])
    types["DatafeedsCustomBatchResponseEntryIn"] = t.struct(
        {
            "datafeed": t.proxy(renames["DatafeedIn"]).optional(),
            "errors": t.proxy(renames["ErrorsIn"]).optional(),
            "batchId": t.integer().optional(),
        }
    ).named(renames["DatafeedsCustomBatchResponseEntryIn"])
    types["DatafeedsCustomBatchResponseEntryOut"] = t.struct(
        {
            "datafeed": t.proxy(renames["DatafeedOut"]).optional(),
            "errors": t.proxy(renames["ErrorsOut"]).optional(),
            "batchId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatafeedsCustomBatchResponseEntryOut"])
    types["ShippingsettingsCustomBatchRequestEntryIn"] = t.struct(
        {
            "merchantId": t.string().optional(),
            "batchId": t.integer().optional(),
            "shippingSettings": t.proxy(renames["ShippingSettingsIn"]).optional(),
            "accountId": t.string().optional(),
            "method": t.string().optional(),
        }
    ).named(renames["ShippingsettingsCustomBatchRequestEntryIn"])
    types["ShippingsettingsCustomBatchRequestEntryOut"] = t.struct(
        {
            "merchantId": t.string().optional(),
            "batchId": t.integer().optional(),
            "shippingSettings": t.proxy(renames["ShippingSettingsOut"]).optional(),
            "accountId": t.string().optional(),
            "method": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShippingsettingsCustomBatchRequestEntryOut"])
    types["DeliveryAreaPostalCodeRangeIn"] = t.struct(
        {"lastPostalCode": t.string().optional(), "firstPostalCode": t.string()}
    ).named(renames["DeliveryAreaPostalCodeRangeIn"])
    types["DeliveryAreaPostalCodeRangeOut"] = t.struct(
        {
            "lastPostalCode": t.string().optional(),
            "firstPostalCode": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeliveryAreaPostalCodeRangeOut"])
    types["ProductUnitPricingBaseMeasureIn"] = t.struct(
        {"value": t.string().optional(), "unit": t.string().optional()}
    ).named(renames["ProductUnitPricingBaseMeasureIn"])
    types["ProductUnitPricingBaseMeasureOut"] = t.struct(
        {
            "value": t.string().optional(),
            "unit": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductUnitPricingBaseMeasureOut"])
    types["OrderDeliveryDetailsIn"] = t.struct(
        {
            "phoneNumber": t.string().optional(),
            "address": t.proxy(renames["OrderAddressIn"]).optional(),
        }
    ).named(renames["OrderDeliveryDetailsIn"])
    types["OrderDeliveryDetailsOut"] = t.struct(
        {
            "phoneNumber": t.string().optional(),
            "address": t.proxy(renames["OrderAddressOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderDeliveryDetailsOut"])
    types["AttributionSettingsConversionTypeIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AttributionSettingsConversionTypeIn"])
    types["AttributionSettingsConversionTypeOut"] = t.struct(
        {
            "name": t.string().optional(),
            "includeInReporting": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttributionSettingsConversionTypeOut"])
    types["ProductsCustomBatchResponseEntryIn"] = t.struct(
        {
            "errors": t.proxy(renames["ErrorsIn"]).optional(),
            "batchId": t.integer().optional(),
            "kind": t.string().optional(),
            "product": t.proxy(renames["ProductIn"]).optional(),
        }
    ).named(renames["ProductsCustomBatchResponseEntryIn"])
    types["ProductsCustomBatchResponseEntryOut"] = t.struct(
        {
            "errors": t.proxy(renames["ErrorsOut"]).optional(),
            "batchId": t.integer().optional(),
            "kind": t.string().optional(),
            "product": t.proxy(renames["ProductOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductsCustomBatchResponseEntryOut"])
    types["CollectionStatusDestinationStatusIn"] = t.struct(
        {
            "disapprovedCountries": t.array(t.string()).optional(),
            "pendingCountries": t.array(t.string()).optional(),
            "status": t.string().optional(),
            "destination": t.string().optional(),
            "approvedCountries": t.array(t.string()).optional(),
        }
    ).named(renames["CollectionStatusDestinationStatusIn"])
    types["CollectionStatusDestinationStatusOut"] = t.struct(
        {
            "disapprovedCountries": t.array(t.string()).optional(),
            "pendingCountries": t.array(t.string()).optional(),
            "status": t.string().optional(),
            "destination": t.string().optional(),
            "approvedCountries": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CollectionStatusDestinationStatusOut"])
    types["OrderShipmentLineItemShipmentIn"] = t.struct(
        {
            "lineItemId": t.string().optional(),
            "quantity": t.integer().optional(),
            "productId": t.string().optional(),
        }
    ).named(renames["OrderShipmentLineItemShipmentIn"])
    types["OrderShipmentLineItemShipmentOut"] = t.struct(
        {
            "lineItemId": t.string().optional(),
            "quantity": t.integer().optional(),
            "productId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderShipmentLineItemShipmentOut"])
    types["OrdersSetLineItemMetadataRequestIn"] = t.struct(
        {
            "annotations": t.array(
                t.proxy(renames["OrderMerchantProvidedAnnotationIn"])
            ),
            "productId": t.string().optional(),
            "operationId": t.string().optional(),
            "lineItemId": t.string().optional(),
        }
    ).named(renames["OrdersSetLineItemMetadataRequestIn"])
    types["OrdersSetLineItemMetadataRequestOut"] = t.struct(
        {
            "annotations": t.array(
                t.proxy(renames["OrderMerchantProvidedAnnotationOut"])
            ),
            "productId": t.string().optional(),
            "operationId": t.string().optional(),
            "lineItemId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersSetLineItemMetadataRequestOut"])
    types["DatafeedStatusIn"] = t.struct(
        {
            "itemsValid": t.string().optional(),
            "lastUploadDate": t.string().optional(),
            "country": t.string().optional(),
            "itemsTotal": t.string().optional(),
            "kind": t.string().optional(),
            "processingStatus": t.string().optional(),
            "errors": t.array(t.proxy(renames["DatafeedStatusErrorIn"])).optional(),
            "datafeedId": t.string().optional(),
            "warnings": t.array(t.proxy(renames["DatafeedStatusErrorIn"])).optional(),
            "feedLabel": t.string().optional(),
            "language": t.string().optional(),
        }
    ).named(renames["DatafeedStatusIn"])
    types["DatafeedStatusOut"] = t.struct(
        {
            "itemsValid": t.string().optional(),
            "lastUploadDate": t.string().optional(),
            "country": t.string().optional(),
            "itemsTotal": t.string().optional(),
            "kind": t.string().optional(),
            "processingStatus": t.string().optional(),
            "errors": t.array(t.proxy(renames["DatafeedStatusErrorOut"])).optional(),
            "datafeedId": t.string().optional(),
            "warnings": t.array(t.proxy(renames["DatafeedStatusErrorOut"])).optional(),
            "feedLabel": t.string().optional(),
            "language": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatafeedStatusOut"])
    types["AttributionSettingsIn"] = t.struct(
        {
            "attributionModel": t.string(),
            "conversionType": t.array(
                t.proxy(renames["AttributionSettingsConversionTypeIn"])
            ).optional(),
            "attributionLookbackWindowInDays": t.integer(),
        }
    ).named(renames["AttributionSettingsIn"])
    types["AttributionSettingsOut"] = t.struct(
        {
            "attributionModel": t.string(),
            "conversionType": t.array(
                t.proxy(renames["AttributionSettingsConversionTypeOut"])
            ).optional(),
            "attributionLookbackWindowInDays": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttributionSettingsOut"])
    types["AccountStatusStatisticsIn"] = t.struct(
        {
            "expiring": t.string().optional(),
            "pending": t.string().optional(),
            "disapproved": t.string().optional(),
            "active": t.string().optional(),
        }
    ).named(renames["AccountStatusStatisticsIn"])
    types["AccountStatusStatisticsOut"] = t.struct(
        {
            "expiring": t.string().optional(),
            "pending": t.string().optional(),
            "disapproved": t.string().optional(),
            "active": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountStatusStatisticsOut"])
    types["AccountsCustomBatchRequestEntryLinkRequestIn"] = t.struct(
        {
            "action": t.string().optional(),
            "services": t.array(t.string()).optional(),
            "linkType": t.string().optional(),
            "linkedAccountId": t.string().optional(),
        }
    ).named(renames["AccountsCustomBatchRequestEntryLinkRequestIn"])
    types["AccountsCustomBatchRequestEntryLinkRequestOut"] = t.struct(
        {
            "action": t.string().optional(),
            "services": t.array(t.string()).optional(),
            "linkType": t.string().optional(),
            "linkedAccountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountsCustomBatchRequestEntryLinkRequestOut"])
    types["ReturnShipmentIn"] = t.struct(
        {
            "shipmentId": t.string().optional(),
            "returnMethodType": t.string().optional(),
            "creationDate": t.string().optional(),
            "deliveryDate": t.string().optional(),
            "state": t.string().optional(),
            "shippingDate": t.string().optional(),
            "shipmentTrackingInfos": t.array(
                t.proxy(renames["ShipmentTrackingInfoIn"])
            ).optional(),
        }
    ).named(renames["ReturnShipmentIn"])
    types["ReturnShipmentOut"] = t.struct(
        {
            "shipmentId": t.string().optional(),
            "returnMethodType": t.string().optional(),
            "creationDate": t.string().optional(),
            "deliveryDate": t.string().optional(),
            "state": t.string().optional(),
            "shippingDate": t.string().optional(),
            "shipmentTrackingInfos": t.array(
                t.proxy(renames["ShipmentTrackingInfoOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReturnShipmentOut"])
    types["RegionalinventoryCustomBatchRequestIn"] = t.struct(
        {
            "entries": t.array(
                t.proxy(renames["RegionalinventoryCustomBatchRequestEntryIn"])
            ).optional()
        }
    ).named(renames["RegionalinventoryCustomBatchRequestIn"])
    types["RegionalinventoryCustomBatchRequestOut"] = t.struct(
        {
            "entries": t.array(
                t.proxy(renames["RegionalinventoryCustomBatchRequestEntryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegionalinventoryCustomBatchRequestOut"])
    types["PaymentServiceProviderLinkInfoIn"] = t.struct(
        {
            "externalAccountId": t.string().optional(),
            "externalAccountBusinessCountry": t.string().optional(),
        }
    ).named(renames["PaymentServiceProviderLinkInfoIn"])
    types["PaymentServiceProviderLinkInfoOut"] = t.struct(
        {
            "externalAccountId": t.string().optional(),
            "externalAccountBusinessCountry": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PaymentServiceProviderLinkInfoOut"])
    types["ShoppingAdsProgramStatusRegionStatusIn"] = t.struct(
        {
            "reviewIneligibilityReasonDetails": t.proxy(
                renames["ShoppingAdsProgramStatusReviewIneligibilityReasonDetailsIn"]
            ).optional(),
            "regionCodes": t.array(t.string()).optional(),
            "reviewIssues": t.array(t.string()).optional(),
            "disapprovalDate": t.string().optional(),
            "reviewEligibilityStatus": t.string().optional(),
            "reviewIneligibilityReasonDescription": t.string().optional(),
            "onboardingIssues": t.array(t.string()).optional(),
            "reviewIneligibilityReason": t.string().optional(),
            "eligibilityStatus": t.string().optional(),
        }
    ).named(renames["ShoppingAdsProgramStatusRegionStatusIn"])
    types["ShoppingAdsProgramStatusRegionStatusOut"] = t.struct(
        {
            "reviewIneligibilityReasonDetails": t.proxy(
                renames["ShoppingAdsProgramStatusReviewIneligibilityReasonDetailsOut"]
            ).optional(),
            "regionCodes": t.array(t.string()).optional(),
            "reviewIssues": t.array(t.string()).optional(),
            "disapprovalDate": t.string().optional(),
            "reviewEligibilityStatus": t.string().optional(),
            "reviewIneligibilityReasonDescription": t.string().optional(),
            "onboardingIssues": t.array(t.string()).optional(),
            "reviewIneligibilityReason": t.string().optional(),
            "eligibilityStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShoppingAdsProgramStatusRegionStatusOut"])
    types["DistanceIn"] = t.struct(
        {"value": t.string().optional(), "unit": t.string().optional()}
    ).named(renames["DistanceIn"])
    types["DistanceOut"] = t.struct(
        {
            "value": t.string().optional(),
            "unit": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DistanceOut"])
    types["WarehouseIn"] = t.struct(
        {
            "cutoffTime": t.proxy(renames["WarehouseCutoffTimeIn"]),
            "shippingAddress": t.proxy(renames["AddressIn"]),
            "name": t.string(),
            "businessDayConfig": t.proxy(renames["BusinessDayConfigIn"]).optional(),
            "handlingDays": t.string(),
        }
    ).named(renames["WarehouseIn"])
    types["WarehouseOut"] = t.struct(
        {
            "cutoffTime": t.proxy(renames["WarehouseCutoffTimeOut"]),
            "shippingAddress": t.proxy(renames["AddressOut"]),
            "name": t.string(),
            "businessDayConfig": t.proxy(renames["BusinessDayConfigOut"]).optional(),
            "handlingDays": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WarehouseOut"])
    types["VerifyPhoneNumberRequestIn"] = t.struct(
        {
            "phoneVerificationMethod": t.string().optional(),
            "verificationCode": t.string().optional(),
            "verificationId": t.string().optional(),
        }
    ).named(renames["VerifyPhoneNumberRequestIn"])
    types["VerifyPhoneNumberRequestOut"] = t.struct(
        {
            "phoneVerificationMethod": t.string().optional(),
            "verificationCode": t.string().optional(),
            "verificationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VerifyPhoneNumberRequestOut"])
    types["DeliveryTimeIn"] = t.struct(
        {
            "handlingBusinessDayConfig": t.proxy(
                renames["BusinessDayConfigIn"]
            ).optional(),
            "minTransitTimeInDays": t.integer().optional(),
            "maxHandlingTimeInDays": t.integer().optional(),
            "transitTimeTable": t.proxy(renames["TransitTableIn"]).optional(),
            "maxTransitTimeInDays": t.integer().optional(),
            "transitBusinessDayConfig": t.proxy(
                renames["BusinessDayConfigIn"]
            ).optional(),
            "cutoffTime": t.proxy(renames["CutoffTimeIn"]).optional(),
            "warehouseBasedDeliveryTimes": t.array(
                t.proxy(renames["WarehouseBasedDeliveryTimeIn"])
            ).optional(),
            "minHandlingTimeInDays": t.integer().optional(),
            "holidayCutoffs": t.array(t.proxy(renames["HolidayCutoffIn"])).optional(),
        }
    ).named(renames["DeliveryTimeIn"])
    types["DeliveryTimeOut"] = t.struct(
        {
            "handlingBusinessDayConfig": t.proxy(
                renames["BusinessDayConfigOut"]
            ).optional(),
            "minTransitTimeInDays": t.integer().optional(),
            "maxHandlingTimeInDays": t.integer().optional(),
            "transitTimeTable": t.proxy(renames["TransitTableOut"]).optional(),
            "maxTransitTimeInDays": t.integer().optional(),
            "transitBusinessDayConfig": t.proxy(
                renames["BusinessDayConfigOut"]
            ).optional(),
            "cutoffTime": t.proxy(renames["CutoffTimeOut"]).optional(),
            "warehouseBasedDeliveryTimes": t.array(
                t.proxy(renames["WarehouseBasedDeliveryTimeOut"])
            ).optional(),
            "minHandlingTimeInDays": t.integer().optional(),
            "holidayCutoffs": t.array(t.proxy(renames["HolidayCutoffOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeliveryTimeOut"])
    types["OrderShipmentScheduledDeliveryDetailsIn"] = t.struct(
        {
            "carrierPhoneNumber": t.string().optional(),
            "scheduledDate": t.string().optional(),
        }
    ).named(renames["OrderShipmentScheduledDeliveryDetailsIn"])
    types["OrderShipmentScheduledDeliveryDetailsOut"] = t.struct(
        {
            "carrierPhoneNumber": t.string().optional(),
            "scheduledDate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderShipmentScheduledDeliveryDetailsOut"])
    types["InvoiceSummaryIn"] = t.struct(
        {
            "additionalChargeSummaries": t.array(
                t.proxy(renames["InvoiceSummaryAdditionalChargeSummaryIn"])
            ).optional(),
            "productTotal": t.proxy(renames["AmountIn"]).optional(),
        }
    ).named(renames["InvoiceSummaryIn"])
    types["InvoiceSummaryOut"] = t.struct(
        {
            "additionalChargeSummaries": t.array(
                t.proxy(renames["InvoiceSummaryAdditionalChargeSummaryOut"])
            ).optional(),
            "productTotal": t.proxy(renames["AmountOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InvoiceSummaryOut"])
    types["LinkServiceIn"] = t.struct(
        {"status": t.string().optional(), "service": t.string().optional()}
    ).named(renames["LinkServiceIn"])
    types["LinkServiceOut"] = t.struct(
        {
            "status": t.string().optional(),
            "service": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinkServiceOut"])
    types["OrderReportTransactionIn"] = t.struct(
        {
            "disbursementDate": t.string().optional(),
            "merchantId": t.string().optional(),
            "disbursementId": t.string().optional(),
            "transactionDate": t.string().optional(),
            "orderId": t.string().optional(),
            "productAmount": t.proxy(renames["ProductAmountIn"]).optional(),
            "disbursementCreationDate": t.string().optional(),
            "disbursementAmount": t.proxy(renames["PriceIn"]).optional(),
            "merchantOrderId": t.string().optional(),
        }
    ).named(renames["OrderReportTransactionIn"])
    types["OrderReportTransactionOut"] = t.struct(
        {
            "disbursementDate": t.string().optional(),
            "merchantId": t.string().optional(),
            "disbursementId": t.string().optional(),
            "transactionDate": t.string().optional(),
            "orderId": t.string().optional(),
            "productAmount": t.proxy(renames["ProductAmountOut"]).optional(),
            "disbursementCreationDate": t.string().optional(),
            "disbursementAmount": t.proxy(renames["PriceOut"]).optional(),
            "merchantOrderId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderReportTransactionOut"])
    types["AccountsListResponseIn"] = t.struct(
        {
            "resources": t.array(t.proxy(renames["AccountIn"])),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["AccountsListResponseIn"])
    types["AccountsListResponseOut"] = t.struct(
        {
            "resources": t.array(t.proxy(renames["AccountOut"])),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountsListResponseOut"])
    types["PosCustomBatchRequestEntryIn"] = t.struct(
        {
            "batchId": t.integer().optional(),
            "storeCode": t.string().optional(),
            "store": t.proxy(renames["PosStoreIn"]).optional(),
            "method": t.string().optional(),
            "merchantId": t.string().optional(),
            "inventory": t.proxy(renames["PosInventoryIn"]).optional(),
            "sale": t.proxy(renames["PosSaleIn"]).optional(),
            "targetMerchantId": t.string().optional(),
        }
    ).named(renames["PosCustomBatchRequestEntryIn"])
    types["PosCustomBatchRequestEntryOut"] = t.struct(
        {
            "batchId": t.integer().optional(),
            "storeCode": t.string().optional(),
            "store": t.proxy(renames["PosStoreOut"]).optional(),
            "method": t.string().optional(),
            "merchantId": t.string().optional(),
            "inventory": t.proxy(renames["PosInventoryOut"]).optional(),
            "sale": t.proxy(renames["PosSaleOut"]).optional(),
            "targetMerchantId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PosCustomBatchRequestEntryOut"])
    types["OrdersRefundItemResponseIn"] = t.struct(
        {"kind": t.string().optional(), "executionStatus": t.string().optional()}
    ).named(renames["OrdersRefundItemResponseIn"])
    types["OrdersRefundItemResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "executionStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersRefundItemResponseOut"])
    types["AccountsLinkRequestIn"] = t.struct(
        {
            "action": t.string().optional(),
            "linkType": t.string().optional(),
            "linkedAccountId": t.string().optional(),
            "eCommercePlatformLinkInfo": t.proxy(
                renames["ECommercePlatformLinkInfoIn"]
            ).optional(),
            "paymentServiceProviderLinkInfo": t.proxy(
                renames["PaymentServiceProviderLinkInfoIn"]
            ).optional(),
            "services": t.array(t.string()).optional(),
        }
    ).named(renames["AccountsLinkRequestIn"])
    types["AccountsLinkRequestOut"] = t.struct(
        {
            "action": t.string().optional(),
            "linkType": t.string().optional(),
            "linkedAccountId": t.string().optional(),
            "eCommercePlatformLinkInfo": t.proxy(
                renames["ECommercePlatformLinkInfoOut"]
            ).optional(),
            "paymentServiceProviderLinkInfo": t.proxy(
                renames["PaymentServiceProviderLinkInfoOut"]
            ).optional(),
            "services": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountsLinkRequestOut"])
    types["OrderCustomerMarketingRightsInfoIn"] = t.struct(
        {
            "explicitMarketingPreference": t.string().optional(),
            "marketingEmailAddress": t.string().optional(),
            "lastUpdatedTimestamp": t.string().optional(),
        }
    ).named(renames["OrderCustomerMarketingRightsInfoIn"])
    types["OrderCustomerMarketingRightsInfoOut"] = t.struct(
        {
            "explicitMarketingPreference": t.string().optional(),
            "marketingEmailAddress": t.string().optional(),
            "lastUpdatedTimestamp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderCustomerMarketingRightsInfoOut"])
    types["LinkedAccountIn"] = t.struct(
        {
            "linkedAccountId": t.string().optional(),
            "services": t.array(t.proxy(renames["LinkServiceIn"])).optional(),
        }
    ).named(renames["LinkedAccountIn"])
    types["LinkedAccountOut"] = t.struct(
        {
            "linkedAccountId": t.string().optional(),
            "services": t.array(t.proxy(renames["LinkServiceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinkedAccountOut"])
    types["OrdersCancelResponseIn"] = t.struct(
        {"executionStatus": t.string().optional(), "kind": t.string().optional()}
    ).named(renames["OrdersCancelResponseIn"])
    types["OrdersCancelResponseOut"] = t.struct(
        {
            "executionStatus": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersCancelResponseOut"])
    types[
        "OrderinvoicesCustomBatchRequestEntryCreateRefundInvoiceReturnOptionIn"
    ] = t.struct(
        {"description": t.string().optional(), "reason": t.string().optional()}
    ).named(
        renames["OrderinvoicesCustomBatchRequestEntryCreateRefundInvoiceReturnOptionIn"]
    )
    types[
        "OrderinvoicesCustomBatchRequestEntryCreateRefundInvoiceReturnOptionOut"
    ] = t.struct(
        {
            "description": t.string().optional(),
            "reason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "OrderinvoicesCustomBatchRequestEntryCreateRefundInvoiceReturnOptionOut"
        ]
    )
    types["OrdersRefundOrderRequestIn"] = t.struct(
        {
            "fullRefund": t.boolean().optional(),
            "reasonText": t.string().optional(),
            "amount": t.proxy(renames["MonetaryAmountIn"]).optional(),
            "operationId": t.string().optional(),
            "reason": t.string().optional(),
        }
    ).named(renames["OrdersRefundOrderRequestIn"])
    types["OrdersRefundOrderRequestOut"] = t.struct(
        {
            "fullRefund": t.boolean().optional(),
            "reasonText": t.string().optional(),
            "amount": t.proxy(renames["MonetaryAmountOut"]).optional(),
            "operationId": t.string().optional(),
            "reason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersRefundOrderRequestOut"])
    types["ListConversionSourcesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "conversionSources": t.array(
                t.proxy(renames["ConversionSourceIn"])
            ).optional(),
        }
    ).named(renames["ListConversionSourcesResponseIn"])
    types["ListConversionSourcesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "conversionSources": t.array(
                t.proxy(renames["ConversionSourceOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListConversionSourcesResponseOut"])
    types["LocalinventoryCustomBatchRequestIn"] = t.struct(
        {
            "entries": t.array(
                t.proxy(renames["LocalinventoryCustomBatchRequestEntryIn"])
            ).optional()
        }
    ).named(renames["LocalinventoryCustomBatchRequestIn"])
    types["LocalinventoryCustomBatchRequestOut"] = t.struct(
        {
            "entries": t.array(
                t.proxy(renames["LocalinventoryCustomBatchRequestEntryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocalinventoryCustomBatchRequestOut"])
    types["ProductDimensionIn"] = t.struct(
        {"unit": t.string(), "value": t.number()}
    ).named(renames["ProductDimensionIn"])
    types["ProductDimensionOut"] = t.struct(
        {
            "unit": t.string(),
            "value": t.number(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductDimensionOut"])
    types["RegionIn"] = t.struct(
        {
            "geotargetArea": t.proxy(renames["RegionGeoTargetAreaIn"]).optional(),
            "postalCodeArea": t.proxy(renames["RegionPostalCodeAreaIn"]).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["RegionIn"])
    types["RegionOut"] = t.struct(
        {
            "shippingEligible": t.boolean().optional(),
            "geotargetArea": t.proxy(renames["RegionGeoTargetAreaOut"]).optional(),
            "postalCodeArea": t.proxy(renames["RegionPostalCodeAreaOut"]).optional(),
            "regionId": t.string().optional(),
            "regionalInventoryEligible": t.boolean().optional(),
            "merchantId": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegionOut"])
    types["DatafeedstatusesCustomBatchRequestIn"] = t.struct(
        {
            "entries": t.array(
                t.proxy(renames["DatafeedstatusesCustomBatchRequestEntryIn"])
            ).optional()
        }
    ).named(renames["DatafeedstatusesCustomBatchRequestIn"])
    types["DatafeedstatusesCustomBatchRequestOut"] = t.struct(
        {
            "entries": t.array(
                t.proxy(renames["DatafeedstatusesCustomBatchRequestEntryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatafeedstatusesCustomBatchRequestOut"])
    types["OrdersGetTestOrderTemplateResponseIn"] = t.struct(
        {
            "template": t.proxy(renames["TestOrderIn"]).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["OrdersGetTestOrderTemplateResponseIn"])
    types["OrdersGetTestOrderTemplateResponseOut"] = t.struct(
        {
            "template": t.proxy(renames["TestOrderOut"]).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersGetTestOrderTemplateResponseOut"])
    types["LocalinventoryCustomBatchRequestEntryIn"] = t.struct(
        {
            "method": t.string().optional(),
            "merchantId": t.string().optional(),
            "batchId": t.integer().optional(),
            "productId": t.string().optional(),
            "localInventory": t.proxy(renames["LocalInventoryIn"]).optional(),
        }
    ).named(renames["LocalinventoryCustomBatchRequestEntryIn"])
    types["LocalinventoryCustomBatchRequestEntryOut"] = t.struct(
        {
            "method": t.string().optional(),
            "merchantId": t.string().optional(),
            "batchId": t.integer().optional(),
            "productId": t.string().optional(),
            "localInventory": t.proxy(renames["LocalInventoryOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocalinventoryCustomBatchRequestEntryOut"])
    types["AccountstatusesCustomBatchRequestIn"] = t.struct(
        {
            "entries": t.array(
                t.proxy(renames["AccountstatusesCustomBatchRequestEntryIn"])
            ).optional()
        }
    ).named(renames["AccountstatusesCustomBatchRequestIn"])
    types["AccountstatusesCustomBatchRequestOut"] = t.struct(
        {
            "entries": t.array(
                t.proxy(renames["AccountstatusesCustomBatchRequestEntryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountstatusesCustomBatchRequestOut"])
    types["ProductViewItemIssueIn"] = t.struct(
        {
            "severity": t.proxy(
                renames["ProductViewItemIssueItemIssueSeverityIn"]
            ).optional(),
            "issueType": t.proxy(
                renames["ProductViewItemIssueItemIssueTypeIn"]
            ).optional(),
            "resolution": t.string().optional(),
        }
    ).named(renames["ProductViewItemIssueIn"])
    types["ProductViewItemIssueOut"] = t.struct(
        {
            "severity": t.proxy(
                renames["ProductViewItemIssueItemIssueSeverityOut"]
            ).optional(),
            "issueType": t.proxy(
                renames["ProductViewItemIssueItemIssueTypeOut"]
            ).optional(),
            "resolution": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductViewItemIssueOut"])
    types["AccountIdentifierIn"] = t.struct(
        {"aggregatorId": t.string().optional(), "merchantId": t.string().optional()}
    ).named(renames["AccountIdentifierIn"])
    types["AccountIdentifierOut"] = t.struct(
        {
            "aggregatorId": t.string().optional(),
            "merchantId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountIdentifierOut"])
    types["RepricingProductReportBuyboxWinningProductStatsIn"] = t.struct(
        {"buyboxWinsCount": t.integer().optional()}
    ).named(renames["RepricingProductReportBuyboxWinningProductStatsIn"])
    types["RepricingProductReportBuyboxWinningProductStatsOut"] = t.struct(
        {
            "buyboxWinsCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepricingProductReportBuyboxWinningProductStatsOut"])
    types["OrderreturnsProcessRequestIn"] = t.struct(
        {
            "refundShippingFee": t.proxy(
                renames["OrderreturnsRefundOperationIn"]
            ).optional(),
            "operationId": t.string().optional(),
            "fullChargeReturnShippingCost": t.boolean().optional(),
            "returnItems": t.array(
                t.proxy(renames["OrderreturnsReturnItemIn"])
            ).optional(),
        }
    ).named(renames["OrderreturnsProcessRequestIn"])
    types["OrderreturnsProcessRequestOut"] = t.struct(
        {
            "refundShippingFee": t.proxy(
                renames["OrderreturnsRefundOperationOut"]
            ).optional(),
            "operationId": t.string().optional(),
            "fullChargeReturnShippingCost": t.boolean().optional(),
            "returnItems": t.array(
                t.proxy(renames["OrderreturnsReturnItemOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderreturnsProcessRequestOut"])
    types["FreeListingsProgramStatusReviewIneligibilityReasonDetailsIn"] = t.struct(
        {"cooldownTime": t.string().optional()}
    ).named(renames["FreeListingsProgramStatusReviewIneligibilityReasonDetailsIn"])
    types["FreeListingsProgramStatusReviewIneligibilityReasonDetailsOut"] = t.struct(
        {
            "cooldownTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FreeListingsProgramStatusReviewIneligibilityReasonDetailsOut"])
    types["AccountItemUpdatesSettingsIn"] = t.struct(
        {
            "allowAvailabilityUpdates": t.boolean().optional(),
            "allowStrictAvailabilityUpdates": t.boolean().optional(),
            "allowConditionUpdates": t.boolean().optional(),
            "allowPriceUpdates": t.boolean().optional(),
        }
    ).named(renames["AccountItemUpdatesSettingsIn"])
    types["AccountItemUpdatesSettingsOut"] = t.struct(
        {
            "allowAvailabilityUpdates": t.boolean().optional(),
            "allowStrictAvailabilityUpdates": t.boolean().optional(),
            "allowConditionUpdates": t.boolean().optional(),
            "allowPriceUpdates": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountItemUpdatesSettingsOut"])
    types["AccountReturnCarrierIn"] = t.struct(
        {
            "carrierAccountNumber": t.string().optional(),
            "carrierCode": t.string().optional(),
            "carrierAccountName": t.string().optional(),
        }
    ).named(renames["AccountReturnCarrierIn"])
    types["AccountReturnCarrierOut"] = t.struct(
        {
            "carrierAccountNumber": t.string().optional(),
            "carrierAccountId": t.string().optional(),
            "carrierCode": t.string().optional(),
            "carrierAccountName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountReturnCarrierOut"])
    types["OrderLineItemProductIn"] = t.struct(
        {
            "fees": t.array(t.proxy(renames["OrderLineItemProductFeeIn"])).optional(),
            "shownImage": t.string().optional(),
            "itemGroupId": t.string().optional(),
            "imageLink": t.string().optional(),
            "condition": t.string().optional(),
            "id": t.string().optional(),
            "price": t.proxy(renames["PriceIn"]).optional(),
            "offerId": t.string().optional(),
            "title": t.string().optional(),
            "gtin": t.string().optional(),
            "mpn": t.string().optional(),
            "targetCountry": t.string().optional(),
            "brand": t.string().optional(),
            "contentLanguage": t.string().optional(),
            "variantAttributes": t.array(
                t.proxy(renames["OrderLineItemProductVariantAttributeIn"])
            ).optional(),
        }
    ).named(renames["OrderLineItemProductIn"])
    types["OrderLineItemProductOut"] = t.struct(
        {
            "fees": t.array(t.proxy(renames["OrderLineItemProductFeeOut"])).optional(),
            "shownImage": t.string().optional(),
            "itemGroupId": t.string().optional(),
            "imageLink": t.string().optional(),
            "condition": t.string().optional(),
            "id": t.string().optional(),
            "price": t.proxy(renames["PriceOut"]).optional(),
            "offerId": t.string().optional(),
            "title": t.string().optional(),
            "gtin": t.string().optional(),
            "mpn": t.string().optional(),
            "targetCountry": t.string().optional(),
            "brand": t.string().optional(),
            "contentLanguage": t.string().optional(),
            "variantAttributes": t.array(
                t.proxy(renames["OrderLineItemProductVariantAttributeOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderLineItemProductOut"])
    types["OrderreturnsAcknowledgeRequestIn"] = t.struct(
        {"operationId": t.string().optional()}
    ).named(renames["OrderreturnsAcknowledgeRequestIn"])
    types["OrderreturnsAcknowledgeRequestOut"] = t.struct(
        {
            "operationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderreturnsAcknowledgeRequestOut"])
    types["OrdersCustomBatchRequestEntryRefundItemItemIn"] = t.struct(
        {
            "productId": t.string().optional(),
            "amount": t.proxy(renames["MonetaryAmountIn"]).optional(),
            "fullRefund": t.boolean().optional(),
            "quantity": t.integer().optional(),
            "lineItemId": t.string().optional(),
        }
    ).named(renames["OrdersCustomBatchRequestEntryRefundItemItemIn"])
    types["OrdersCustomBatchRequestEntryRefundItemItemOut"] = t.struct(
        {
            "productId": t.string().optional(),
            "amount": t.proxy(renames["MonetaryAmountOut"]).optional(),
            "fullRefund": t.boolean().optional(),
            "quantity": t.integer().optional(),
            "lineItemId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersCustomBatchRequestEntryRefundItemItemOut"])
    types["SegmentsIn"] = t.struct(
        {
            "brand": t.string().optional(),
            "productTypeL1": t.string().optional(),
            "customLabel2": t.string().optional(),
            "categoryL3": t.string().optional(),
            "customLabel4": t.string().optional(),
            "customLabel1": t.string().optional(),
            "productTypeL4": t.string().optional(),
            "week": t.proxy(renames["DateIn"]).optional(),
            "currencyCode": t.string().optional(),
            "productTypeL5": t.string().optional(),
            "customLabel0": t.string().optional(),
            "categoryL5": t.string().optional(),
            "categoryL4": t.string().optional(),
            "customerCountryCode": t.string().optional(),
            "offerId": t.string().optional(),
            "categoryL1": t.string().optional(),
            "productTypeL3": t.string().optional(),
            "categoryL2": t.string().optional(),
            "productTypeL2": t.string().optional(),
            "date": t.proxy(renames["DateIn"]).optional(),
            "program": t.string().optional(),
            "title": t.string().optional(),
            "customLabel3": t.string().optional(),
        }
    ).named(renames["SegmentsIn"])
    types["SegmentsOut"] = t.struct(
        {
            "brand": t.string().optional(),
            "productTypeL1": t.string().optional(),
            "customLabel2": t.string().optional(),
            "categoryL3": t.string().optional(),
            "customLabel4": t.string().optional(),
            "customLabel1": t.string().optional(),
            "productTypeL4": t.string().optional(),
            "week": t.proxy(renames["DateOut"]).optional(),
            "currencyCode": t.string().optional(),
            "productTypeL5": t.string().optional(),
            "customLabel0": t.string().optional(),
            "categoryL5": t.string().optional(),
            "categoryL4": t.string().optional(),
            "customerCountryCode": t.string().optional(),
            "offerId": t.string().optional(),
            "categoryL1": t.string().optional(),
            "productTypeL3": t.string().optional(),
            "categoryL2": t.string().optional(),
            "productTypeL2": t.string().optional(),
            "date": t.proxy(renames["DateOut"]).optional(),
            "program": t.string().optional(),
            "title": t.string().optional(),
            "customLabel3": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SegmentsOut"])
    types["AccountStatusItemLevelIssueIn"] = t.struct(
        {
            "servability": t.string().optional(),
            "numItems": t.string().optional(),
            "documentation": t.string().optional(),
            "attributeName": t.string().optional(),
            "code": t.string().optional(),
            "resolution": t.string().optional(),
            "detail": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["AccountStatusItemLevelIssueIn"])
    types["AccountStatusItemLevelIssueOut"] = t.struct(
        {
            "servability": t.string().optional(),
            "numItems": t.string().optional(),
            "documentation": t.string().optional(),
            "attributeName": t.string().optional(),
            "code": t.string().optional(),
            "resolution": t.string().optional(),
            "detail": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountStatusItemLevelIssueOut"])
    types["ConversionSourceIn"] = t.struct(
        {
            "googleAnalyticsLink": t.proxy(renames["GoogleAnalyticsLinkIn"]).optional(),
            "merchantCenterDestination": t.proxy(
                renames["MerchantCenterDestinationIn"]
            ).optional(),
        }
    ).named(renames["ConversionSourceIn"])
    types["ConversionSourceOut"] = t.struct(
        {
            "state": t.string().optional(),
            "googleAnalyticsLink": t.proxy(
                renames["GoogleAnalyticsLinkOut"]
            ).optional(),
            "conversionSourceId": t.string().optional(),
            "merchantCenterDestination": t.proxy(
                renames["MerchantCenterDestinationOut"]
            ).optional(),
            "expireTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConversionSourceOut"])
    types["ReturnaddressCustomBatchResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "entries": t.array(
                t.proxy(renames["ReturnaddressCustomBatchResponseEntryIn"])
            ).optional(),
        }
    ).named(renames["ReturnaddressCustomBatchResponseIn"])
    types["ReturnaddressCustomBatchResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "entries": t.array(
                t.proxy(renames["ReturnaddressCustomBatchResponseEntryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReturnaddressCustomBatchResponseOut"])
    types["OrderLineItemReturnInfoIn"] = t.struct(
        {
            "isReturnable": t.boolean(),
            "daysToReturn": t.integer(),
            "policyUrl": t.string(),
        }
    ).named(renames["OrderLineItemReturnInfoIn"])
    types["OrderLineItemReturnInfoOut"] = t.struct(
        {
            "isReturnable": t.boolean(),
            "daysToReturn": t.integer(),
            "policyUrl": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderLineItemReturnInfoOut"])
    types["RepricingRuleReportBuyboxWinningRuleStatsIn"] = t.struct(
        {"buyboxWonProductCount": t.integer().optional()}
    ).named(renames["RepricingRuleReportBuyboxWinningRuleStatsIn"])
    types["RepricingRuleReportBuyboxWinningRuleStatsOut"] = t.struct(
        {
            "buyboxWonProductCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepricingRuleReportBuyboxWinningRuleStatsOut"])
    types["PosCustomBatchResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "entries": t.array(
                t.proxy(renames["PosCustomBatchResponseEntryIn"])
            ).optional(),
        }
    ).named(renames["PosCustomBatchResponseIn"])
    types["PosCustomBatchResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "entries": t.array(
                t.proxy(renames["PosCustomBatchResponseEntryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PosCustomBatchResponseOut"])
    types["OrdersRejectReturnLineItemRequestIn"] = t.struct(
        {
            "operationId": t.string().optional(),
            "lineItemId": t.string().optional(),
            "reason": t.string().optional(),
            "quantity": t.integer().optional(),
            "reasonText": t.string().optional(),
            "productId": t.string().optional(),
        }
    ).named(renames["OrdersRejectReturnLineItemRequestIn"])
    types["OrdersRejectReturnLineItemRequestOut"] = t.struct(
        {
            "operationId": t.string().optional(),
            "lineItemId": t.string().optional(),
            "reason": t.string().optional(),
            "quantity": t.integer().optional(),
            "reasonText": t.string().optional(),
            "productId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersRejectReturnLineItemRequestOut"])
    types["ProductsCustomBatchRequestIn"] = t.struct(
        {
            "entries": t.array(
                t.proxy(renames["ProductsCustomBatchRequestEntryIn"])
            ).optional()
        }
    ).named(renames["ProductsCustomBatchRequestIn"])
    types["ProductsCustomBatchRequestOut"] = t.struct(
        {
            "entries": t.array(
                t.proxy(renames["ProductsCustomBatchRequestEntryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductsCustomBatchRequestOut"])
    types["ShippingsettingsCustomBatchRequestIn"] = t.struct(
        {
            "entries": t.array(
                t.proxy(renames["ShippingsettingsCustomBatchRequestEntryIn"])
            ).optional()
        }
    ).named(renames["ShippingsettingsCustomBatchRequestIn"])
    types["ShippingsettingsCustomBatchRequestOut"] = t.struct(
        {
            "entries": t.array(
                t.proxy(renames["ShippingsettingsCustomBatchRequestEntryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShippingsettingsCustomBatchRequestOut"])
    types["LiasettingsCustomBatchRequestIn"] = t.struct(
        {
            "entries": t.array(
                t.proxy(renames["LiasettingsCustomBatchRequestEntryIn"])
            ).optional()
        }
    ).named(renames["LiasettingsCustomBatchRequestIn"])
    types["LiasettingsCustomBatchRequestOut"] = t.struct(
        {
            "entries": t.array(
                t.proxy(renames["LiasettingsCustomBatchRequestEntryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiasettingsCustomBatchRequestOut"])
    types["DatafeedstatusesCustomBatchResponseIn"] = t.struct(
        {
            "entries": t.array(
                t.proxy(renames["DatafeedstatusesCustomBatchResponseEntryIn"])
            ).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["DatafeedstatusesCustomBatchResponseIn"])
    types["DatafeedstatusesCustomBatchResponseOut"] = t.struct(
        {
            "entries": t.array(
                t.proxy(renames["DatafeedstatusesCustomBatchResponseEntryOut"])
            ).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatafeedstatusesCustomBatchResponseOut"])
    types["OrdersRejectReturnLineItemResponseIn"] = t.struct(
        {"kind": t.string().optional(), "executionStatus": t.string().optional()}
    ).named(renames["OrdersRejectReturnLineItemResponseIn"])
    types["OrdersRejectReturnLineItemResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "executionStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersRejectReturnLineItemResponseOut"])
    types["DatafeedsListResponseIn"] = t.struct(
        {
            "resources": t.array(t.proxy(renames["DatafeedIn"])),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["DatafeedsListResponseIn"])
    types["DatafeedsListResponseOut"] = t.struct(
        {
            "resources": t.array(t.proxy(renames["DatafeedOut"])),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatafeedsListResponseOut"])
    types["WeightIn"] = t.struct({"value": t.string(), "unit": t.string()}).named(
        renames["WeightIn"]
    )
    types["WeightOut"] = t.struct(
        {
            "value": t.string(),
            "unit": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WeightOut"])
    types["ShippingsettingsGetSupportedPickupServicesResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "pickupServices": t.array(
                t.proxy(renames["PickupServicesPickupServiceIn"])
            ).optional(),
        }
    ).named(renames["ShippingsettingsGetSupportedPickupServicesResponseIn"])
    types["ShippingsettingsGetSupportedPickupServicesResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "pickupServices": t.array(
                t.proxy(renames["PickupServicesPickupServiceOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShippingsettingsGetSupportedPickupServicesResponseOut"])
    types["DatafeedFormatIn"] = t.struct(
        {
            "columnDelimiter": t.string().optional(),
            "quotingMode": t.string().optional(),
            "fileEncoding": t.string().optional(),
        }
    ).named(renames["DatafeedFormatIn"])
    types["DatafeedFormatOut"] = t.struct(
        {
            "columnDelimiter": t.string().optional(),
            "quotingMode": t.string().optional(),
            "fileEncoding": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatafeedFormatOut"])
    types["ReturnShippingLabelIn"] = t.struct(
        {
            "carrier": t.string().optional(),
            "labelUri": t.string().optional(),
            "trackingId": t.string().optional(),
        }
    ).named(renames["ReturnShippingLabelIn"])
    types["ReturnShippingLabelOut"] = t.struct(
        {
            "carrier": t.string().optional(),
            "labelUri": t.string().optional(),
            "trackingId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReturnShippingLabelOut"])
    types["PickupCarrierServiceIn"] = t.struct(
        {"serviceName": t.string().optional(), "carrierName": t.string().optional()}
    ).named(renames["PickupCarrierServiceIn"])
    types["PickupCarrierServiceOut"] = t.struct(
        {
            "serviceName": t.string().optional(),
            "carrierName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PickupCarrierServiceOut"])
    types["ReturnPricingInfoIn"] = t.struct(
        {
            "refundableShippingAmount": t.proxy(renames["MonetaryAmountIn"]).optional(),
            "maxReturnShippingFee": t.proxy(renames["MonetaryAmountIn"]).optional(),
            "refundableItemsTotalAmount": t.proxy(
                renames["MonetaryAmountIn"]
            ).optional(),
            "totalRefundedAmount": t.proxy(renames["MonetaryAmountIn"]).optional(),
            "chargeReturnShippingFee": t.boolean().optional(),
        }
    ).named(renames["ReturnPricingInfoIn"])
    types["ReturnPricingInfoOut"] = t.struct(
        {
            "refundableShippingAmount": t.proxy(
                renames["MonetaryAmountOut"]
            ).optional(),
            "maxReturnShippingFee": t.proxy(renames["MonetaryAmountOut"]).optional(),
            "refundableItemsTotalAmount": t.proxy(
                renames["MonetaryAmountOut"]
            ).optional(),
            "totalRefundedAmount": t.proxy(renames["MonetaryAmountOut"]).optional(),
            "chargeReturnShippingFee": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReturnPricingInfoOut"])
    types["OrderreportsListDisbursementsResponseIn"] = t.struct(
        {
            "disbursements": t.array(
                t.proxy(renames["OrderReportDisbursementIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["OrderreportsListDisbursementsResponseIn"])
    types["OrderreportsListDisbursementsResponseOut"] = t.struct(
        {
            "disbursements": t.array(
                t.proxy(renames["OrderReportDisbursementOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderreportsListDisbursementsResponseOut"])
    types["OrdersUpdateShipmentResponseIn"] = t.struct(
        {"executionStatus": t.string().optional(), "kind": t.string().optional()}
    ).named(renames["OrdersUpdateShipmentResponseIn"])
    types["OrdersUpdateShipmentResponseOut"] = t.struct(
        {
            "executionStatus": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersUpdateShipmentResponseOut"])
    types["AccountsCustomBatchRequestIn"] = t.struct(
        {
            "entries": t.array(
                t.proxy(renames["AccountsCustomBatchRequestEntryIn"])
            ).optional()
        }
    ).named(renames["AccountsCustomBatchRequestIn"])
    types["AccountsCustomBatchRequestOut"] = t.struct(
        {
            "entries": t.array(
                t.proxy(renames["AccountsCustomBatchRequestEntryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountsCustomBatchRequestOut"])
    types["OrdersAdvanceTestOrderResponseIn"] = t.struct(
        {"kind": t.string().optional()}
    ).named(renames["OrdersAdvanceTestOrderResponseIn"])
    types["OrdersAdvanceTestOrderResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersAdvanceTestOrderResponseOut"])
    types["InvoiceSummaryAdditionalChargeSummaryIn"] = t.struct(
        {
            "type": t.string().optional(),
            "totalAmount": t.proxy(renames["AmountIn"]).optional(),
        }
    ).named(renames["InvoiceSummaryAdditionalChargeSummaryIn"])
    types["InvoiceSummaryAdditionalChargeSummaryOut"] = t.struct(
        {
            "type": t.string().optional(),
            "totalAmount": t.proxy(renames["AmountOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InvoiceSummaryAdditionalChargeSummaryOut"])
    types["ShippingsettingsGetSupportedHolidaysResponseIn"] = t.struct(
        {
            "holidays": t.array(t.proxy(renames["HolidaysHolidayIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ShippingsettingsGetSupportedHolidaysResponseIn"])
    types["ShippingsettingsGetSupportedHolidaysResponseOut"] = t.struct(
        {
            "holidays": t.array(t.proxy(renames["HolidaysHolidayOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShippingsettingsGetSupportedHolidaysResponseOut"])
    types["ReturnAddressIn"] = t.struct(
        {
            "address": t.proxy(renames["ReturnAddressAddressIn"]),
            "returnAddressId": t.string().optional(),
            "country": t.string(),
            "phoneNumber": t.string(),
            "label": t.string(),
            "kind": t.string().optional(),
        }
    ).named(renames["ReturnAddressIn"])
    types["ReturnAddressOut"] = t.struct(
        {
            "address": t.proxy(renames["ReturnAddressAddressOut"]),
            "returnAddressId": t.string().optional(),
            "country": t.string(),
            "phoneNumber": t.string(),
            "label": t.string(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReturnAddressOut"])
    types["ListReturnPolicyOnlineResponseIn"] = t.struct(
        {"returnPolicies": t.array(t.proxy(renames["ReturnPolicyOnlineIn"])).optional()}
    ).named(renames["ListReturnPolicyOnlineResponseIn"])
    types["ListReturnPolicyOnlineResponseOut"] = t.struct(
        {
            "returnPolicies": t.array(
                t.proxy(renames["ReturnPolicyOnlineOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListReturnPolicyOnlineResponseOut"])
    types["PosListResponseIn"] = t.struct(
        {
            "resources": t.array(t.proxy(renames["PosStoreIn"])),
            "kind": t.string().optional(),
        }
    ).named(renames["PosListResponseIn"])
    types["PosListResponseOut"] = t.struct(
        {
            "resources": t.array(t.proxy(renames["PosStoreOut"])),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PosListResponseOut"])
    types["CloudExportAdditionalPropertiesIn"] = t.struct(
        {
            "minValue": t.number().optional(),
            "floatValue": t.array(t.number()).optional(),
            "boolValue": t.boolean().optional(),
            "unitCode": t.string().optional(),
            "textValue": t.array(t.string()).optional(),
            "maxValue": t.number().optional(),
            "intValue": t.array(t.string()).optional(),
            "propertyName": t.string().optional(),
        }
    ).named(renames["CloudExportAdditionalPropertiesIn"])
    types["CloudExportAdditionalPropertiesOut"] = t.struct(
        {
            "minValue": t.number().optional(),
            "floatValue": t.array(t.number()).optional(),
            "boolValue": t.boolean().optional(),
            "unitCode": t.string().optional(),
            "textValue": t.array(t.string()).optional(),
            "maxValue": t.number().optional(),
            "intValue": t.array(t.string()).optional(),
            "propertyName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudExportAdditionalPropertiesOut"])
    types["OrderinvoicesCreateRefundInvoiceRequestIn"] = t.struct(
        {
            "shipmentInvoices": t.array(
                t.proxy(renames["ShipmentInvoiceIn"])
            ).optional(),
            "returnOption": t.proxy(
                renames[
                    "OrderinvoicesCustomBatchRequestEntryCreateRefundInvoiceReturnOptionIn"
                ]
            ).optional(),
            "operationId": t.string().optional(),
            "invoiceId": t.string().optional(),
            "refundOnlyOption": t.proxy(
                renames[
                    "OrderinvoicesCustomBatchRequestEntryCreateRefundInvoiceRefundOptionIn"
                ]
            ).optional(),
        }
    ).named(renames["OrderinvoicesCreateRefundInvoiceRequestIn"])
    types["OrderinvoicesCreateRefundInvoiceRequestOut"] = t.struct(
        {
            "shipmentInvoices": t.array(
                t.proxy(renames["ShipmentInvoiceOut"])
            ).optional(),
            "returnOption": t.proxy(
                renames[
                    "OrderinvoicesCustomBatchRequestEntryCreateRefundInvoiceReturnOptionOut"
                ]
            ).optional(),
            "operationId": t.string().optional(),
            "invoiceId": t.string().optional(),
            "refundOnlyOption": t.proxy(
                renames[
                    "OrderinvoicesCustomBatchRequestEntryCreateRefundInvoiceRefundOptionOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderinvoicesCreateRefundInvoiceRequestOut"])
    types["RecommendationCreativeIn"] = t.struct(
        {"uri": t.string().optional(), "type": t.string().optional()}
    ).named(renames["RecommendationCreativeIn"])
    types["RecommendationCreativeOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RecommendationCreativeOut"])
    types["PriceCompetitivenessIn"] = t.struct(
        {
            "benchmarkPriceMicros": t.string().optional(),
            "countryCode": t.string().optional(),
            "benchmarkPriceCurrencyCode": t.string().optional(),
        }
    ).named(renames["PriceCompetitivenessIn"])
    types["PriceCompetitivenessOut"] = t.struct(
        {
            "benchmarkPriceMicros": t.string().optional(),
            "countryCode": t.string().optional(),
            "benchmarkPriceCurrencyCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PriceCompetitivenessOut"])
    types["ProductAmountIn"] = t.struct(
        {
            "priceAmount": t.proxy(renames["PriceIn"]).optional(),
            "taxAmount": t.proxy(renames["PriceIn"]).optional(),
            "remittedTaxAmount": t.proxy(renames["PriceIn"]).optional(),
        }
    ).named(renames["ProductAmountIn"])
    types["ProductAmountOut"] = t.struct(
        {
            "priceAmount": t.proxy(renames["PriceOut"]).optional(),
            "taxAmount": t.proxy(renames["PriceOut"]).optional(),
            "remittedTaxAmount": t.proxy(renames["PriceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductAmountOut"])
    types["InapplicabilityDetailsIn"] = t.struct(
        {
            "inapplicableCount": t.string().optional(),
            "inapplicableReason": t.string().optional(),
        }
    ).named(renames["InapplicabilityDetailsIn"])
    types["InapplicabilityDetailsOut"] = t.struct(
        {
            "inapplicableCount": t.string().optional(),
            "inapplicableReason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InapplicabilityDetailsOut"])
    types["AccountItemUpdatesIn"] = t.struct(
        {
            "accountItemUpdatesSettings": t.proxy(
                renames["AccountItemUpdatesSettingsIn"]
            ).optional()
        }
    ).named(renames["AccountItemUpdatesIn"])
    types["AccountItemUpdatesOut"] = t.struct(
        {
            "effectiveAllowConditionUpdates": t.boolean().optional(),
            "effectiveAllowPriceUpdates": t.boolean().optional(),
            "accountItemUpdatesSettings": t.proxy(
                renames["AccountItemUpdatesSettingsOut"]
            ).optional(),
            "effectiveAllowAvailabilityUpdates": t.boolean().optional(),
            "effectiveAllowStrictAvailabilityUpdates": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountItemUpdatesOut"])
    types["OrderTrackingSignalShipmentLineItemMappingIn"] = t.struct(
        {
            "shipmentId": t.string(),
            "quantity": t.string().optional(),
            "lineItemId": t.string(),
        }
    ).named(renames["OrderTrackingSignalShipmentLineItemMappingIn"])
    types["OrderTrackingSignalShipmentLineItemMappingOut"] = t.struct(
        {
            "shipmentId": t.string(),
            "quantity": t.string().optional(),
            "lineItemId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderTrackingSignalShipmentLineItemMappingOut"])
    types["OrderPickupDetailsIn"] = t.struct(
        {
            "collectors": t.array(
                t.proxy(renames["OrderPickupDetailsCollectorIn"])
            ).optional(),
            "address": t.proxy(renames["OrderAddressIn"]).optional(),
            "locationId": t.string().optional(),
            "pickupType": t.string().optional(),
        }
    ).named(renames["OrderPickupDetailsIn"])
    types["OrderPickupDetailsOut"] = t.struct(
        {
            "collectors": t.array(
                t.proxy(renames["OrderPickupDetailsCollectorOut"])
            ).optional(),
            "address": t.proxy(renames["OrderAddressOut"]).optional(),
            "locationId": t.string().optional(),
            "pickupType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderPickupDetailsOut"])
    types["DatafeedFetchScheduleIn"] = t.struct(
        {
            "paused": t.boolean().optional(),
            "username": t.string().optional(),
            "dayOfMonth": t.integer().optional(),
            "timeZone": t.string().optional(),
            "minuteOfHour": t.integer().optional(),
            "fetchUrl": t.string().optional(),
            "weekday": t.string().optional(),
            "password": t.string().optional(),
            "hour": t.integer().optional(),
        }
    ).named(renames["DatafeedFetchScheduleIn"])
    types["DatafeedFetchScheduleOut"] = t.struct(
        {
            "paused": t.boolean().optional(),
            "username": t.string().optional(),
            "dayOfMonth": t.integer().optional(),
            "timeZone": t.string().optional(),
            "minuteOfHour": t.integer().optional(),
            "fetchUrl": t.string().optional(),
            "weekday": t.string().optional(),
            "password": t.string().optional(),
            "hour": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatafeedFetchScheduleOut"])
    types["ProductProductDetailIn"] = t.struct(
        {
            "sectionName": t.string().optional(),
            "attributeName": t.string().optional(),
            "attributeValue": t.string().optional(),
        }
    ).named(renames["ProductProductDetailIn"])
    types["ProductProductDetailOut"] = t.struct(
        {
            "sectionName": t.string().optional(),
            "attributeName": t.string().optional(),
            "attributeValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductProductDetailOut"])
    types[
        "OrdersCustomBatchRequestEntryUpdateShipmentScheduledDeliveryDetailsIn"
    ] = t.struct(
        {
            "carrierPhoneNumber": t.string().optional(),
            "scheduledDate": t.string().optional(),
        }
    ).named(
        renames["OrdersCustomBatchRequestEntryUpdateShipmentScheduledDeliveryDetailsIn"]
    )
    types[
        "OrdersCustomBatchRequestEntryUpdateShipmentScheduledDeliveryDetailsOut"
    ] = t.struct(
        {
            "carrierPhoneNumber": t.string().optional(),
            "scheduledDate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "OrdersCustomBatchRequestEntryUpdateShipmentScheduledDeliveryDetailsOut"
        ]
    )
    types["SettlementTransactionTransactionIn"] = t.struct(
        {"postDate": t.string().optional(), "type": t.string().optional()}
    ).named(renames["SettlementTransactionTransactionIn"])
    types["SettlementTransactionTransactionOut"] = t.struct(
        {
            "postDate": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SettlementTransactionTransactionOut"])
    types["OnboardBuyOnGoogleProgramRequestIn"] = t.struct(
        {"customerServiceEmail": t.string().optional()}
    ).named(renames["OnboardBuyOnGoogleProgramRequestIn"])
    types["OnboardBuyOnGoogleProgramRequestOut"] = t.struct(
        {
            "customerServiceEmail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OnboardBuyOnGoogleProgramRequestOut"])
    types["AccountsCustomBatchRequestEntryIn"] = t.struct(
        {
            "account": t.proxy(renames["AccountIn"]).optional(),
            "batchId": t.integer().optional(),
            "accountId": t.string().optional(),
            "linkRequest": t.proxy(
                renames["AccountsCustomBatchRequestEntryLinkRequestIn"]
            ).optional(),
            "labelIds": t.array(t.string()).optional(),
            "method": t.string().optional(),
            "view": t.string().optional(),
            "force": t.boolean().optional(),
            "overwrite": t.boolean().optional(),
            "merchantId": t.string().optional(),
        }
    ).named(renames["AccountsCustomBatchRequestEntryIn"])
    types["AccountsCustomBatchRequestEntryOut"] = t.struct(
        {
            "account": t.proxy(renames["AccountOut"]).optional(),
            "batchId": t.integer().optional(),
            "accountId": t.string().optional(),
            "linkRequest": t.proxy(
                renames["AccountsCustomBatchRequestEntryLinkRequestOut"]
            ).optional(),
            "labelIds": t.array(t.string()).optional(),
            "method": t.string().optional(),
            "view": t.string().optional(),
            "force": t.boolean().optional(),
            "overwrite": t.boolean().optional(),
            "merchantId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountsCustomBatchRequestEntryOut"])
    types["LiasettingsGetAccessibleGmbAccountsResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "accountId": t.string().optional(),
            "gmbAccounts": t.array(
                t.proxy(renames["GmbAccountsGmbAccountIn"])
            ).optional(),
        }
    ).named(renames["LiasettingsGetAccessibleGmbAccountsResponseIn"])
    types["LiasettingsGetAccessibleGmbAccountsResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "accountId": t.string().optional(),
            "gmbAccounts": t.array(
                t.proxy(renames["GmbAccountsGmbAccountOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiasettingsGetAccessibleGmbAccountsResponseOut"])
    types["PosInventoryRequestIn"] = t.struct(
        {
            "targetCountry": t.string(),
            "gtin": t.string().optional(),
            "storeCode": t.string(),
            "contentLanguage": t.string(),
            "itemId": t.string(),
            "timestamp": t.string(),
            "price": t.proxy(renames["PriceIn"]),
            "quantity": t.string(),
        }
    ).named(renames["PosInventoryRequestIn"])
    types["PosInventoryRequestOut"] = t.struct(
        {
            "targetCountry": t.string(),
            "gtin": t.string().optional(),
            "storeCode": t.string(),
            "contentLanguage": t.string(),
            "itemId": t.string(),
            "timestamp": t.string(),
            "price": t.proxy(renames["PriceOut"]),
            "quantity": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PosInventoryRequestOut"])
    types["PromotionPromotionStatusIn"] = t.struct(
        {
            "lastUpdateDate": t.string().optional(),
            "creationDate": t.string().optional(),
            "destinationStatuses": t.array(
                t.proxy(renames["PromotionPromotionStatusDestinationStatusIn"])
            ).optional(),
            "promotionIssue": t.array(
                t.proxy(renames["PromotionPromotionStatusPromotionIssueIn"])
            ).optional(),
        }
    ).named(renames["PromotionPromotionStatusIn"])
    types["PromotionPromotionStatusOut"] = t.struct(
        {
            "lastUpdateDate": t.string().optional(),
            "creationDate": t.string().optional(),
            "destinationStatuses": t.array(
                t.proxy(renames["PromotionPromotionStatusDestinationStatusOut"])
            ).optional(),
            "promotionIssue": t.array(
                t.proxy(renames["PromotionPromotionStatusPromotionIssueOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PromotionPromotionStatusOut"])
    types["ProductStatusIn"] = t.struct(
        {
            "link": t.string().optional(),
            "creationDate": t.string().optional(),
            "itemLevelIssues": t.array(
                t.proxy(renames["ProductStatusItemLevelIssueIn"])
            ).optional(),
            "title": t.string().optional(),
            "productId": t.string().optional(),
            "googleExpirationDate": t.string().optional(),
            "destinationStatuses": t.array(
                t.proxy(renames["ProductStatusDestinationStatusIn"])
            ).optional(),
            "lastUpdateDate": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ProductStatusIn"])
    types["ProductStatusOut"] = t.struct(
        {
            "link": t.string().optional(),
            "creationDate": t.string().optional(),
            "itemLevelIssues": t.array(
                t.proxy(renames["ProductStatusItemLevelIssueOut"])
            ).optional(),
            "title": t.string().optional(),
            "productId": t.string().optional(),
            "googleExpirationDate": t.string().optional(),
            "destinationStatuses": t.array(
                t.proxy(renames["ProductStatusDestinationStatusOut"])
            ).optional(),
            "lastUpdateDate": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductStatusOut"])
    types["DatafeedstatusesCustomBatchRequestEntryIn"] = t.struct(
        {
            "batchId": t.integer().optional(),
            "country": t.string().optional(),
            "language": t.string().optional(),
            "feedLabel": t.string().optional(),
            "method": t.string().optional(),
            "merchantId": t.string().optional(),
            "datafeedId": t.string().optional(),
        }
    ).named(renames["DatafeedstatusesCustomBatchRequestEntryIn"])
    types["DatafeedstatusesCustomBatchRequestEntryOut"] = t.struct(
        {
            "batchId": t.integer().optional(),
            "country": t.string().optional(),
            "language": t.string().optional(),
            "feedLabel": t.string().optional(),
            "method": t.string().optional(),
            "merchantId": t.string().optional(),
            "datafeedId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatafeedstatusesCustomBatchRequestEntryOut"])
    types["ListPromotionResponseIn"] = t.struct(
        {
            "promotions": t.array(t.proxy(renames["PromotionIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListPromotionResponseIn"])
    types["ListPromotionResponseOut"] = t.struct(
        {
            "promotions": t.array(t.proxy(renames["PromotionOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPromotionResponseOut"])
    types["ListMethodQuotasResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "methodQuotas": t.array(t.proxy(renames["MethodQuotaIn"])).optional(),
        }
    ).named(renames["ListMethodQuotasResponseIn"])
    types["ListMethodQuotasResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "methodQuotas": t.array(t.proxy(renames["MethodQuotaOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListMethodQuotasResponseOut"])
    types["ReturnPolicyPolicyIn"] = t.struct(
        {
            "lastReturnDate": t.string(),
            "numberOfDays": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["ReturnPolicyPolicyIn"])
    types["ReturnPolicyPolicyOut"] = t.struct(
        {
            "lastReturnDate": t.string(),
            "numberOfDays": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReturnPolicyPolicyOut"])
    types["ShippingsettingsGetSupportedCarriersResponseIn"] = t.struct(
        {
            "carriers": t.array(t.proxy(renames["CarriersCarrierIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ShippingsettingsGetSupportedCarriersResponseIn"])
    types["ShippingsettingsGetSupportedCarriersResponseOut"] = t.struct(
        {
            "carriers": t.array(t.proxy(renames["CarriersCarrierOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShippingsettingsGetSupportedCarriersResponseOut"])
    types["ProductIn"] = t.struct(
        {
            "sellOnGoogleQuantity": t.string().optional(),
            "taxCategory": t.string().optional(),
            "mpn": t.string().optional(),
            "gtin": t.string().optional(),
            "availabilityDate": t.string().optional(),
            "gender": t.string().optional(),
            "itemGroupId": t.string().optional(),
            "excludedDestinations": t.array(t.string()).optional(),
            "shoppingAdsExcludedCountries": t.array(t.string()).optional(),
            "availability": t.string().optional(),
            "shippingLength": t.proxy(renames["ProductShippingDimensionIn"]).optional(),
            "sizeType": t.string().optional(),
            "ageGroup": t.string().optional(),
            "productTypes": t.array(t.string()).optional(),
            "displayAdsSimilarIds": t.array(t.string()).optional(),
            "customLabel1": t.string().optional(),
            "minHandlingTime": t.string().optional(),
            "transitTimeLabel": t.string().optional(),
            "externalSellerId": t.string(),
            "additionalSizeType": t.string().optional(),
            "productWeight": t.proxy(renames["ProductWeightIn"]).optional(),
            "pickupSla": t.string().optional(),
            "shippingWeight": t.proxy(renames["ProductShippingWeightIn"]).optional(),
            "title": t.string().optional(),
            "promotionIds": t.array(t.string()).optional(),
            "energyEfficiencyClass": t.string().optional(),
            "productHighlights": t.array(t.string()).optional(),
            "installment": t.proxy(renames["InstallmentIn"]).optional(),
            "multipack": t.string().optional(),
            "lifestyleImageLinks": t.array(t.string()).optional(),
            "link": t.string().optional(),
            "color": t.string().optional(),
            "brand": t.string().optional(),
            "additionalImageLinks": t.array(t.string()).optional(),
            "unitPricingMeasure": t.proxy(
                renames["ProductUnitPricingMeasureIn"]
            ).optional(),
            "identifierExists": t.boolean().optional(),
            "source": t.string().optional(),
            "productWidth": t.proxy(renames["ProductDimensionIn"]).optional(),
            "loyaltyPoints": t.proxy(renames["LoyaltyPointsIn"]).optional(),
            "productHeight": t.proxy(renames["ProductDimensionIn"]).optional(),
            "linkTemplate": t.string().optional(),
            "certifications": t.array(
                t.proxy(renames["ProductCertificationIn"])
            ).optional(),
            "isBundle": t.boolean().optional(),
            "productDetails": t.array(
                t.proxy(renames["ProductProductDetailIn"])
            ).optional(),
            "mobileLink": t.string().optional(),
            "pickupMethod": t.string().optional(),
            "googleProductCategory": t.string().optional(),
            "displayAdsTitle": t.string().optional(),
            "minEnergyEfficiencyClass": t.string().optional(),
            "price": t.proxy(renames["PriceIn"]).optional(),
            "shipping": t.array(t.proxy(renames["ProductShippingIn"])).optional(),
            "shippingWidth": t.proxy(renames["ProductShippingDimensionIn"]).optional(),
            "customLabel0": t.string().optional(),
            "adsLabels": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "adsRedirect": t.string().optional(),
            "shippingLabel": t.string().optional(),
            "canonicalLink": t.string().optional(),
            "condition": t.string().optional(),
            "productLength": t.proxy(renames["ProductDimensionIn"]).optional(),
            "offerId": t.string(),
            "adult": t.boolean().optional(),
            "material": t.string().optional(),
            "displayAdsId": t.string().optional(),
            "includedDestinations": t.array(t.string()).optional(),
            "contentLanguage": t.string(),
            "adsGrouping": t.string().optional(),
            "cloudExportAdditionalProperties": t.array(
                t.proxy(renames["CloudExportAdditionalPropertiesIn"])
            ).optional(),
            "displayAdsLink": t.string().optional(),
            "maxHandlingTime": t.string().optional(),
            "sizeSystem": t.string().optional(),
            "subscriptionCost": t.proxy(
                renames["ProductSubscriptionCostIn"]
            ).optional(),
            "salePriceEffectiveDate": t.string().optional(),
            "feedLabel": t.string().optional(),
            "disclosureDate": t.string().optional(),
            "taxes": t.array(t.proxy(renames["ProductTaxIn"])).optional(),
            "channel": t.string(),
            "customLabel4": t.string().optional(),
            "sizes": t.array(t.string()).optional(),
            "displayAdsValue": t.number().optional(),
            "costOfGoodsSold": t.proxy(renames["PriceIn"]).optional(),
            "mobileLinkTemplate": t.string().optional(),
            "targetCountry": t.string(),
            "salePrice": t.proxy(renames["PriceIn"]).optional(),
            "imageLink": t.string().optional(),
            "unitPricingBaseMeasure": t.proxy(
                renames["ProductUnitPricingBaseMeasureIn"]
            ).optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "maxEnergyEfficiencyClass": t.string().optional(),
            "pattern": t.string().optional(),
            "customAttributes": t.array(
                t.proxy(renames["CustomAttributeIn"])
            ).optional(),
            "customLabel2": t.string().optional(),
            "shippingHeight": t.proxy(renames["ProductShippingDimensionIn"]).optional(),
            "customLabel3": t.string().optional(),
            "expirationDate": t.string().optional(),
            "pause": t.string().optional(),
        }
    ).named(renames["ProductIn"])
    types["ProductOut"] = t.struct(
        {
            "sellOnGoogleQuantity": t.string().optional(),
            "taxCategory": t.string().optional(),
            "mpn": t.string().optional(),
            "gtin": t.string().optional(),
            "availabilityDate": t.string().optional(),
            "gender": t.string().optional(),
            "itemGroupId": t.string().optional(),
            "excludedDestinations": t.array(t.string()).optional(),
            "shoppingAdsExcludedCountries": t.array(t.string()).optional(),
            "availability": t.string().optional(),
            "shippingLength": t.proxy(
                renames["ProductShippingDimensionOut"]
            ).optional(),
            "sizeType": t.string().optional(),
            "ageGroup": t.string().optional(),
            "productTypes": t.array(t.string()).optional(),
            "displayAdsSimilarIds": t.array(t.string()).optional(),
            "customLabel1": t.string().optional(),
            "minHandlingTime": t.string().optional(),
            "transitTimeLabel": t.string().optional(),
            "externalSellerId": t.string(),
            "additionalSizeType": t.string().optional(),
            "productWeight": t.proxy(renames["ProductWeightOut"]).optional(),
            "pickupSla": t.string().optional(),
            "shippingWeight": t.proxy(renames["ProductShippingWeightOut"]).optional(),
            "title": t.string().optional(),
            "promotionIds": t.array(t.string()).optional(),
            "energyEfficiencyClass": t.string().optional(),
            "productHighlights": t.array(t.string()).optional(),
            "installment": t.proxy(renames["InstallmentOut"]).optional(),
            "multipack": t.string().optional(),
            "lifestyleImageLinks": t.array(t.string()).optional(),
            "link": t.string().optional(),
            "color": t.string().optional(),
            "brand": t.string().optional(),
            "additionalImageLinks": t.array(t.string()).optional(),
            "unitPricingMeasure": t.proxy(
                renames["ProductUnitPricingMeasureOut"]
            ).optional(),
            "identifierExists": t.boolean().optional(),
            "source": t.string().optional(),
            "productWidth": t.proxy(renames["ProductDimensionOut"]).optional(),
            "loyaltyPoints": t.proxy(renames["LoyaltyPointsOut"]).optional(),
            "productHeight": t.proxy(renames["ProductDimensionOut"]).optional(),
            "linkTemplate": t.string().optional(),
            "certifications": t.array(
                t.proxy(renames["ProductCertificationOut"])
            ).optional(),
            "isBundle": t.boolean().optional(),
            "productDetails": t.array(
                t.proxy(renames["ProductProductDetailOut"])
            ).optional(),
            "mobileLink": t.string().optional(),
            "pickupMethod": t.string().optional(),
            "googleProductCategory": t.string().optional(),
            "displayAdsTitle": t.string().optional(),
            "minEnergyEfficiencyClass": t.string().optional(),
            "price": t.proxy(renames["PriceOut"]).optional(),
            "shipping": t.array(t.proxy(renames["ProductShippingOut"])).optional(),
            "shippingWidth": t.proxy(renames["ProductShippingDimensionOut"]).optional(),
            "customLabel0": t.string().optional(),
            "adsLabels": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "adsRedirect": t.string().optional(),
            "shippingLabel": t.string().optional(),
            "canonicalLink": t.string().optional(),
            "condition": t.string().optional(),
            "productLength": t.proxy(renames["ProductDimensionOut"]).optional(),
            "offerId": t.string(),
            "adult": t.boolean().optional(),
            "material": t.string().optional(),
            "displayAdsId": t.string().optional(),
            "includedDestinations": t.array(t.string()).optional(),
            "contentLanguage": t.string(),
            "adsGrouping": t.string().optional(),
            "cloudExportAdditionalProperties": t.array(
                t.proxy(renames["CloudExportAdditionalPropertiesOut"])
            ).optional(),
            "displayAdsLink": t.string().optional(),
            "maxHandlingTime": t.string().optional(),
            "sizeSystem": t.string().optional(),
            "subscriptionCost": t.proxy(
                renames["ProductSubscriptionCostOut"]
            ).optional(),
            "salePriceEffectiveDate": t.string().optional(),
            "feedLabel": t.string().optional(),
            "disclosureDate": t.string().optional(),
            "taxes": t.array(t.proxy(renames["ProductTaxOut"])).optional(),
            "channel": t.string(),
            "customLabel4": t.string().optional(),
            "sizes": t.array(t.string()).optional(),
            "displayAdsValue": t.number().optional(),
            "costOfGoodsSold": t.proxy(renames["PriceOut"]).optional(),
            "mobileLinkTemplate": t.string().optional(),
            "targetCountry": t.string(),
            "salePrice": t.proxy(renames["PriceOut"]).optional(),
            "imageLink": t.string().optional(),
            "unitPricingBaseMeasure": t.proxy(
                renames["ProductUnitPricingBaseMeasureOut"]
            ).optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "maxEnergyEfficiencyClass": t.string().optional(),
            "pattern": t.string().optional(),
            "customAttributes": t.array(
                t.proxy(renames["CustomAttributeOut"])
            ).optional(),
            "customLabel2": t.string().optional(),
            "shippingHeight": t.proxy(
                renames["ProductShippingDimensionOut"]
            ).optional(),
            "customLabel3": t.string().optional(),
            "expirationDate": t.string().optional(),
            "pause": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductOut"])
    types["RepricingRuleEligibleOfferMatcherStringMatcherIn"] = t.struct(
        {"strAttributes": t.array(t.string()).optional()}
    ).named(renames["RepricingRuleEligibleOfferMatcherStringMatcherIn"])
    types["RepricingRuleEligibleOfferMatcherStringMatcherOut"] = t.struct(
        {
            "strAttributes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepricingRuleEligibleOfferMatcherStringMatcherOut"])
    types["ProductViewIn"] = t.struct(
        {
            "productTypeL5": t.string().optional(),
            "itemIssues": t.array(
                t.proxy(renames["ProductViewItemIssueIn"])
            ).optional(),
            "languageCode": t.string().optional(),
            "productTypeL2": t.string().optional(),
            "creationTime": t.string().optional(),
            "id": t.string().optional(),
            "categoryL2": t.string().optional(),
            "categoryL3": t.string().optional(),
            "productTypeL3": t.string().optional(),
            "brand": t.string().optional(),
            "gtin": t.array(t.string()).optional(),
            "priceMicros": t.string().optional(),
            "shippingLabel": t.string().optional(),
            "productTypeL1": t.string().optional(),
            "categoryL4": t.string().optional(),
            "categoryL1": t.string().optional(),
            "categoryL5": t.string().optional(),
            "offerId": t.string().optional(),
            "itemGroupId": t.string().optional(),
            "channel": t.string().optional(),
            "aggregatedDestinationStatus": t.string().optional(),
            "expirationDate": t.proxy(renames["DateIn"]).optional(),
            "title": t.string().optional(),
            "availability": t.string().optional(),
            "currencyCode": t.string().optional(),
            "condition": t.string().optional(),
            "productTypeL4": t.string().optional(),
        }
    ).named(renames["ProductViewIn"])
    types["ProductViewOut"] = t.struct(
        {
            "productTypeL5": t.string().optional(),
            "itemIssues": t.array(
                t.proxy(renames["ProductViewItemIssueOut"])
            ).optional(),
            "languageCode": t.string().optional(),
            "productTypeL2": t.string().optional(),
            "creationTime": t.string().optional(),
            "id": t.string().optional(),
            "categoryL2": t.string().optional(),
            "categoryL3": t.string().optional(),
            "productTypeL3": t.string().optional(),
            "brand": t.string().optional(),
            "gtin": t.array(t.string()).optional(),
            "priceMicros": t.string().optional(),
            "shippingLabel": t.string().optional(),
            "productTypeL1": t.string().optional(),
            "categoryL4": t.string().optional(),
            "categoryL1": t.string().optional(),
            "categoryL5": t.string().optional(),
            "offerId": t.string().optional(),
            "itemGroupId": t.string().optional(),
            "channel": t.string().optional(),
            "aggregatedDestinationStatus": t.string().optional(),
            "expirationDate": t.proxy(renames["DateOut"]).optional(),
            "title": t.string().optional(),
            "availability": t.string().optional(),
            "currencyCode": t.string().optional(),
            "condition": t.string().optional(),
            "productTypeL4": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductViewOut"])
    types["OrderCancellationIn"] = t.struct(
        {
            "quantity": t.integer().optional(),
            "creationDate": t.string().optional(),
            "actor": t.string().optional(),
            "reason": t.string().optional(),
            "reasonText": t.string().optional(),
        }
    ).named(renames["OrderCancellationIn"])
    types["OrderCancellationOut"] = t.struct(
        {
            "quantity": t.integer().optional(),
            "creationDate": t.string().optional(),
            "actor": t.string().optional(),
            "reason": t.string().optional(),
            "reasonText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderCancellationOut"])
    types["RecommendationDescriptionIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RecommendationDescriptionIn"]
    )
    types["RecommendationDescriptionOut"] = t.struct(
        {
            "text": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RecommendationDescriptionOut"])
    types["OrderCustomerIn"] = t.struct(
        {
            "invoiceReceivingEmail": t.string().optional(),
            "loyaltyInfo": t.proxy(renames["OrderCustomerLoyaltyInfoIn"]).optional(),
            "fullName": t.string().optional(),
            "marketingRightsInfo": t.proxy(
                renames["OrderCustomerMarketingRightsInfoIn"]
            ).optional(),
        }
    ).named(renames["OrderCustomerIn"])
    types["OrderCustomerOut"] = t.struct(
        {
            "invoiceReceivingEmail": t.string().optional(),
            "loyaltyInfo": t.proxy(renames["OrderCustomerLoyaltyInfoOut"]).optional(),
            "fullName": t.string().optional(),
            "marketingRightsInfo": t.proxy(
                renames["OrderCustomerMarketingRightsInfoOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderCustomerOut"])
    types["OrderreturnsReturnItemIn"] = t.struct(
        {
            "refund": t.proxy(renames["OrderreturnsRefundOperationIn"]).optional(),
            "reject": t.proxy(renames["OrderreturnsRejectOperationIn"]).optional(),
            "returnItemId": t.string().optional(),
        }
    ).named(renames["OrderreturnsReturnItemIn"])
    types["OrderreturnsReturnItemOut"] = t.struct(
        {
            "refund": t.proxy(renames["OrderreturnsRefundOperationOut"]).optional(),
            "reject": t.proxy(renames["OrderreturnsRejectOperationOut"]).optional(),
            "returnItemId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderreturnsReturnItemOut"])
    types["ServiceStoreConfigCutoffConfigLocalCutoffTimeIn"] = t.struct(
        {"minute": t.string().optional(), "hour": t.string().optional()}
    ).named(renames["ServiceStoreConfigCutoffConfigLocalCutoffTimeIn"])
    types["ServiceStoreConfigCutoffConfigLocalCutoffTimeOut"] = t.struct(
        {
            "minute": t.string().optional(),
            "hour": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceStoreConfigCutoffConfigLocalCutoffTimeOut"])
    types["OrderTrackingSignalIn"] = t.struct(
        {
            "shippingInfo": t.array(
                t.proxy(renames["OrderTrackingSignalShippingInfoIn"])
            ).optional(),
            "lineItems": t.array(
                t.proxy(renames["OrderTrackingSignalLineItemDetailsIn"])
            ).optional(),
            "orderCreatedTime": t.proxy(renames["DateTimeIn"]),
            "merchantId": t.string().optional(),
            "customerShippingFee": t.proxy(renames["PriceAmountIn"]).optional(),
            "deliveryRegionCode": t.string(),
            "shipmentLineItemMapping": t.array(
                t.proxy(renames["OrderTrackingSignalShipmentLineItemMappingIn"])
            ).optional(),
            "orderId": t.string(),
            "deliveryPostalCode": t.string(),
        }
    ).named(renames["OrderTrackingSignalIn"])
    types["OrderTrackingSignalOut"] = t.struct(
        {
            "shippingInfo": t.array(
                t.proxy(renames["OrderTrackingSignalShippingInfoOut"])
            ).optional(),
            "lineItems": t.array(
                t.proxy(renames["OrderTrackingSignalLineItemDetailsOut"])
            ).optional(),
            "orderCreatedTime": t.proxy(renames["DateTimeOut"]),
            "merchantId": t.string().optional(),
            "customerShippingFee": t.proxy(renames["PriceAmountOut"]).optional(),
            "deliveryRegionCode": t.string(),
            "shipmentLineItemMapping": t.array(
                t.proxy(renames["OrderTrackingSignalShipmentLineItemMappingOut"])
            ).optional(),
            "orderId": t.string(),
            "deliveryPostalCode": t.string(),
            "orderTrackingSignalId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderTrackingSignalOut"])
    types["ProductCertificationIn"] = t.struct(
        {
            "certificationName": t.string().optional(),
            "certificationAuthority": t.string().optional(),
            "certificationCode": t.string().optional(),
        }
    ).named(renames["ProductCertificationIn"])
    types["ProductCertificationOut"] = t.struct(
        {
            "certificationName": t.string().optional(),
            "certificationAuthority": t.string().optional(),
            "certificationCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductCertificationOut"])
    types["LiaInventorySettingsIn"] = t.struct(
        {
            "status": t.string().optional(),
            "inventoryVerificationContactEmail": t.string().optional(),
            "inventoryVerificationContactName": t.string().optional(),
            "inventoryVerificationContactStatus": t.string().optional(),
        }
    ).named(renames["LiaInventorySettingsIn"])
    types["LiaInventorySettingsOut"] = t.struct(
        {
            "status": t.string().optional(),
            "inventoryVerificationContactEmail": t.string().optional(),
            "inventoryVerificationContactName": t.string().optional(),
            "inventoryVerificationContactStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiaInventorySettingsOut"])
    types["OrderreportsListTransactionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "transactions": t.array(
                t.proxy(renames["OrderReportTransactionIn"])
            ).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["OrderreportsListTransactionsResponseIn"])
    types["OrderreportsListTransactionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "transactions": t.array(
                t.proxy(renames["OrderReportTransactionOut"])
            ).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderreportsListTransactionsResponseOut"])
    types["TestOrderPickupDetailsIn"] = t.struct(
        {
            "pickupPersons": t.array(
                t.proxy(renames["TestOrderPickupDetailsPickupPersonIn"])
            ),
            "pickupLocationType": t.string().optional(),
            "locationCode": t.string(),
            "pickupLocationAddress": t.proxy(renames["TestOrderAddressIn"]),
        }
    ).named(renames["TestOrderPickupDetailsIn"])
    types["TestOrderPickupDetailsOut"] = t.struct(
        {
            "pickupPersons": t.array(
                t.proxy(renames["TestOrderPickupDetailsPickupPersonOut"])
            ),
            "pickupLocationType": t.string().optional(),
            "locationCode": t.string(),
            "pickupLocationAddress": t.proxy(renames["TestOrderAddressOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestOrderPickupDetailsOut"])
    types["PriceIn"] = t.struct(
        {"currency": t.string().optional(), "value": t.string().optional()}
    ).named(renames["PriceIn"])
    types["PriceOut"] = t.struct(
        {
            "currency": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PriceOut"])
    types["OrderLineItemProductVariantAttributeIn"] = t.struct(
        {"dimension": t.string().optional(), "value": t.string().optional()}
    ).named(renames["OrderLineItemProductVariantAttributeIn"])
    types["OrderLineItemProductVariantAttributeOut"] = t.struct(
        {
            "dimension": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderLineItemProductVariantAttributeOut"])
    types["ReturnaddressCustomBatchResponseEntryIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "returnAddress": t.proxy(renames["ReturnAddressIn"]).optional(),
            "batchId": t.integer().optional(),
            "errors": t.proxy(renames["ErrorsIn"]).optional(),
        }
    ).named(renames["ReturnaddressCustomBatchResponseEntryIn"])
    types["ReturnaddressCustomBatchResponseEntryOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "returnAddress": t.proxy(renames["ReturnAddressOut"]).optional(),
            "batchId": t.integer().optional(),
            "errors": t.proxy(renames["ErrorsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReturnaddressCustomBatchResponseEntryOut"])
    types["OrderinvoicesCreateRefundInvoiceResponseIn"] = t.struct(
        {"kind": t.string().optional(), "executionStatus": t.string().optional()}
    ).named(renames["OrderinvoicesCreateRefundInvoiceResponseIn"])
    types["OrderinvoicesCreateRefundInvoiceResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "executionStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderinvoicesCreateRefundInvoiceResponseOut"])
    types["AccountImageImprovementsSettingsIn"] = t.struct(
        {"allowAutomaticImageImprovements": t.boolean().optional()}
    ).named(renames["AccountImageImprovementsSettingsIn"])
    types["AccountImageImprovementsSettingsOut"] = t.struct(
        {
            "allowAutomaticImageImprovements": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountImageImprovementsSettingsOut"])
    types["OrdersAcknowledgeResponseIn"] = t.struct(
        {"executionStatus": t.string().optional(), "kind": t.string().optional()}
    ).named(renames["OrdersAcknowledgeResponseIn"])
    types["OrdersAcknowledgeResponseOut"] = t.struct(
        {
            "executionStatus": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersAcknowledgeResponseOut"])
    types["MerchantRejectionReasonIn"] = t.struct(
        {"description": t.string().optional(), "reasonCode": t.string().optional()}
    ).named(renames["MerchantRejectionReasonIn"])
    types["MerchantRejectionReasonOut"] = t.struct(
        {
            "description": t.string().optional(),
            "reasonCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MerchantRejectionReasonOut"])
    types["AccountImageImprovementsIn"] = t.struct(
        {
            "accountImageImprovementsSettings": t.proxy(
                renames["AccountImageImprovementsSettingsIn"]
            ).optional()
        }
    ).named(renames["AccountImageImprovementsIn"])
    types["AccountImageImprovementsOut"] = t.struct(
        {
            "effectiveAllowAutomaticImageImprovements": t.boolean().optional(),
            "accountImageImprovementsSettings": t.proxy(
                renames["AccountImageImprovementsSettingsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountImageImprovementsOut"])
    types["AccounttaxCustomBatchRequestIn"] = t.struct(
        {
            "entries": t.array(
                t.proxy(renames["AccounttaxCustomBatchRequestEntryIn"])
            ).optional()
        }
    ).named(renames["AccounttaxCustomBatchRequestIn"])
    types["AccounttaxCustomBatchRequestOut"] = t.struct(
        {
            "entries": t.array(
                t.proxy(renames["AccounttaxCustomBatchRequestEntryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccounttaxCustomBatchRequestOut"])
    types["PostalCodeGroupIn"] = t.struct(
        {
            "country": t.string().optional(),
            "name": t.string().optional(),
            "postalCodeRanges": t.array(
                t.proxy(renames["PostalCodeRangeIn"])
            ).optional(),
        }
    ).named(renames["PostalCodeGroupIn"])
    types["PostalCodeGroupOut"] = t.struct(
        {
            "country": t.string().optional(),
            "name": t.string().optional(),
            "postalCodeRanges": t.array(
                t.proxy(renames["PostalCodeRangeOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostalCodeGroupOut"])
    types["ReturnpolicyCustomBatchRequestEntryIn"] = t.struct(
        {
            "batchId": t.integer().optional(),
            "merchantId": t.string().optional(),
            "method": t.string().optional(),
            "returnPolicy": t.proxy(renames["ReturnPolicyIn"]).optional(),
            "returnPolicyId": t.string().optional(),
        }
    ).named(renames["ReturnpolicyCustomBatchRequestEntryIn"])
    types["ReturnpolicyCustomBatchRequestEntryOut"] = t.struct(
        {
            "batchId": t.integer().optional(),
            "merchantId": t.string().optional(),
            "method": t.string().optional(),
            "returnPolicy": t.proxy(renames["ReturnPolicyOut"]).optional(),
            "returnPolicyId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReturnpolicyCustomBatchRequestEntryOut"])
    types["ProductViewItemIssueItemIssueSeverityIn"] = t.struct(
        {
            "severityPerDestination": t.array(
                t.proxy(renames["ProductViewItemIssueIssueSeverityPerDestinationIn"])
            ).optional(),
            "aggregatedSeverity": t.string().optional(),
        }
    ).named(renames["ProductViewItemIssueItemIssueSeverityIn"])
    types["ProductViewItemIssueItemIssueSeverityOut"] = t.struct(
        {
            "severityPerDestination": t.array(
                t.proxy(renames["ProductViewItemIssueIssueSeverityPerDestinationOut"])
            ).optional(),
            "aggregatedSeverity": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductViewItemIssueItemIssueSeverityOut"])
    types["AccountStatusProductsIn"] = t.struct(
        {
            "destination": t.string().optional(),
            "statistics": t.proxy(renames["AccountStatusStatisticsIn"]).optional(),
            "country": t.string().optional(),
            "channel": t.string().optional(),
            "itemLevelIssues": t.array(
                t.proxy(renames["AccountStatusItemLevelIssueIn"])
            ).optional(),
        }
    ).named(renames["AccountStatusProductsIn"])
    types["AccountStatusProductsOut"] = t.struct(
        {
            "destination": t.string().optional(),
            "statistics": t.proxy(renames["AccountStatusStatisticsOut"]).optional(),
            "country": t.string().optional(),
            "channel": t.string().optional(),
            "itemLevelIssues": t.array(
                t.proxy(renames["AccountStatusItemLevelIssueOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountStatusProductsOut"])
    types["ProductViewItemIssueItemIssueTypeIn"] = t.struct(
        {"code": t.string().optional(), "canonicalAttribute": t.string().optional()}
    ).named(renames["ProductViewItemIssueItemIssueTypeIn"])
    types["ProductViewItemIssueItemIssueTypeOut"] = t.struct(
        {
            "code": t.string().optional(),
            "canonicalAttribute": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductViewItemIssueItemIssueTypeOut"])
    types["ReturnPolicyOnlineReturnShippingFeeIn"] = t.struct(
        {
            "type": t.string().optional(),
            "fixedFee": t.proxy(renames["PriceAmountIn"]).optional(),
        }
    ).named(renames["ReturnPolicyOnlineReturnShippingFeeIn"])
    types["ReturnPolicyOnlineReturnShippingFeeOut"] = t.struct(
        {
            "type": t.string().optional(),
            "fixedFee": t.proxy(renames["PriceAmountOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReturnPolicyOnlineReturnShippingFeeOut"])
    types["RefundReasonIn"] = t.struct(
        {"reasonCode": t.string().optional(), "description": t.string().optional()}
    ).named(renames["RefundReasonIn"])
    types["RefundReasonOut"] = t.struct(
        {
            "reasonCode": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RefundReasonOut"])
    types["CarriersCarrierIn"] = t.struct(
        {
            "name": t.string().optional(),
            "services": t.array(t.string()).optional(),
            "eddServices": t.array(t.string()).optional(),
            "country": t.string().optional(),
        }
    ).named(renames["CarriersCarrierIn"])
    types["CarriersCarrierOut"] = t.struct(
        {
            "name": t.string().optional(),
            "services": t.array(t.string()).optional(),
            "eddServices": t.array(t.string()).optional(),
            "country": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CarriersCarrierOut"])
    types["BrandIn"] = t.struct({"name": t.string().optional()}).named(
        renames["BrandIn"]
    )
    types["BrandOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BrandOut"])
    types["OrderinvoicesCreateChargeInvoiceRequestIn"] = t.struct(
        {
            "operationId": t.string().optional(),
            "invoiceSummary": t.proxy(renames["InvoiceSummaryIn"]).optional(),
            "lineItemInvoices": t.array(
                t.proxy(renames["ShipmentInvoiceLineItemInvoiceIn"])
            ).optional(),
            "shipmentGroupId": t.string().optional(),
            "invoiceId": t.string().optional(),
        }
    ).named(renames["OrderinvoicesCreateChargeInvoiceRequestIn"])
    types["OrderinvoicesCreateChargeInvoiceRequestOut"] = t.struct(
        {
            "operationId": t.string().optional(),
            "invoiceSummary": t.proxy(renames["InvoiceSummaryOut"]).optional(),
            "lineItemInvoices": t.array(
                t.proxy(renames["ShipmentInvoiceLineItemInvoiceOut"])
            ).optional(),
            "shipmentGroupId": t.string().optional(),
            "invoiceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderinvoicesCreateChargeInvoiceRequestOut"])
    types["OrdersUpdateLineItemShippingDetailsResponseIn"] = t.struct(
        {"executionStatus": t.string().optional(), "kind": t.string().optional()}
    ).named(renames["OrdersUpdateLineItemShippingDetailsResponseIn"])
    types["OrdersUpdateLineItemShippingDetailsResponseOut"] = t.struct(
        {
            "executionStatus": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersUpdateLineItemShippingDetailsResponseOut"])
    types["OrderShipmentIn"] = t.struct(
        {
            "status": t.string().optional(),
            "deliveryDate": t.string().optional(),
            "scheduledDeliveryDetails": t.proxy(
                renames["OrderShipmentScheduledDeliveryDetailsIn"]
            ).optional(),
            "carrier": t.string().optional(),
            "lineItems": t.array(
                t.proxy(renames["OrderShipmentLineItemShipmentIn"])
            ).optional(),
            "trackingId": t.string().optional(),
            "shipmentGroupId": t.string().optional(),
            "creationDate": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["OrderShipmentIn"])
    types["OrderShipmentOut"] = t.struct(
        {
            "status": t.string().optional(),
            "deliveryDate": t.string().optional(),
            "scheduledDeliveryDetails": t.proxy(
                renames["OrderShipmentScheduledDeliveryDetailsOut"]
            ).optional(),
            "carrier": t.string().optional(),
            "lineItems": t.array(
                t.proxy(renames["OrderShipmentLineItemShipmentOut"])
            ).optional(),
            "trackingId": t.string().optional(),
            "shipmentGroupId": t.string().optional(),
            "creationDate": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderShipmentOut"])
    types["ErrorIn"] = t.struct(
        {
            "domain": t.string().optional(),
            "message": t.string().optional(),
            "reason": t.string().optional(),
        }
    ).named(renames["ErrorIn"])
    types["ErrorOut"] = t.struct(
        {
            "domain": t.string().optional(),
            "message": t.string().optional(),
            "reason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ErrorOut"])
    types["DateTimeIn"] = t.struct(
        {
            "hours": t.integer().optional(),
            "year": t.integer().optional(),
            "timeZone": t.proxy(renames["TimeZoneIn"]).optional(),
            "nanos": t.integer().optional(),
            "seconds": t.integer().optional(),
            "month": t.integer().optional(),
            "utcOffset": t.string().optional(),
            "minutes": t.integer().optional(),
            "day": t.integer().optional(),
        }
    ).named(renames["DateTimeIn"])
    types["DateTimeOut"] = t.struct(
        {
            "hours": t.integer().optional(),
            "year": t.integer().optional(),
            "timeZone": t.proxy(renames["TimeZoneOut"]).optional(),
            "nanos": t.integer().optional(),
            "seconds": t.integer().optional(),
            "month": t.integer().optional(),
            "utcOffset": t.string().optional(),
            "minutes": t.integer().optional(),
            "day": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateTimeOut"])
    types["AccountStatusAccountLevelIssueIn"] = t.struct(
        {
            "detail": t.string().optional(),
            "severity": t.string().optional(),
            "documentation": t.string().optional(),
            "destination": t.string().optional(),
            "title": t.string().optional(),
            "id": t.string().optional(),
            "country": t.string().optional(),
        }
    ).named(renames["AccountStatusAccountLevelIssueIn"])
    types["AccountStatusAccountLevelIssueOut"] = t.struct(
        {
            "detail": t.string().optional(),
            "severity": t.string().optional(),
            "documentation": t.string().optional(),
            "destination": t.string().optional(),
            "title": t.string().optional(),
            "id": t.string().optional(),
            "country": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountStatusAccountLevelIssueOut"])
    types["OrdersAcknowledgeRequestIn"] = t.struct(
        {"operationId": t.string().optional()}
    ).named(renames["OrdersAcknowledgeRequestIn"])
    types["OrdersAcknowledgeRequestOut"] = t.struct(
        {
            "operationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersAcknowledgeRequestOut"])
    types["ErrorsIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "errors": t.array(t.proxy(renames["ErrorIn"])).optional(),
        }
    ).named(renames["ErrorsIn"])
    types["ErrorsOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "errors": t.array(t.proxy(renames["ErrorOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ErrorsOut"])
    types["AccounttaxListResponseIn"] = t.struct(
        {
            "resources": t.array(t.proxy(renames["AccountTaxIn"])),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["AccounttaxListResponseIn"])
    types["AccounttaxListResponseOut"] = t.struct(
        {
            "resources": t.array(t.proxy(renames["AccountTaxOut"])),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccounttaxListResponseOut"])
    types["RecommendationCallToActionIn"] = t.struct(
        {"uri": t.string().optional()}
    ).named(renames["RecommendationCallToActionIn"])
    types["RecommendationCallToActionOut"] = t.struct(
        {
            "intent": t.string().optional(),
            "localizedText": t.string().optional(),
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RecommendationCallToActionOut"])
    types["AccountsListLinksResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "links": t.array(t.proxy(renames["LinkedAccountIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["AccountsListLinksResponseIn"])
    types["AccountsListLinksResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "links": t.array(t.proxy(renames["LinkedAccountOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountsListLinksResponseOut"])
    types["DatafeedStatusErrorIn"] = t.struct(
        {
            "examples": t.array(t.proxy(renames["DatafeedStatusExampleIn"])).optional(),
            "count": t.string().optional(),
            "code": t.string().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["DatafeedStatusErrorIn"])
    types["DatafeedStatusErrorOut"] = t.struct(
        {
            "examples": t.array(
                t.proxy(renames["DatafeedStatusExampleOut"])
            ).optional(),
            "count": t.string().optional(),
            "code": t.string().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatafeedStatusErrorOut"])
    types["MerchantCenterDestinationIn"] = t.struct(
        {
            "displayName": t.string(),
            "currencyCode": t.string(),
            "attributionSettings": t.proxy(renames["AttributionSettingsIn"]),
        }
    ).named(renames["MerchantCenterDestinationIn"])
    types["MerchantCenterDestinationOut"] = t.struct(
        {
            "displayName": t.string(),
            "destinationId": t.string().optional(),
            "currencyCode": t.string(),
            "attributionSettings": t.proxy(renames["AttributionSettingsOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MerchantCenterDestinationOut"])
    types["RepricingProductReportIn"] = t.struct(
        {
            "ruleIds": t.array(t.string()).optional(),
            "lowWatermark": t.proxy(renames["PriceAmountIn"]).optional(),
            "orderItemCount": t.integer().optional(),
            "inapplicabilityDetails": t.array(
                t.proxy(renames["InapplicabilityDetailsIn"])
            ).optional(),
            "applicationCount": t.string().optional(),
            "totalGmv": t.proxy(renames["PriceAmountIn"]).optional(),
            "buyboxWinningProductStats": t.proxy(
                renames["RepricingProductReportBuyboxWinningProductStatsIn"]
            ).optional(),
            "type": t.string().optional(),
            "highWatermark": t.proxy(renames["PriceAmountIn"]).optional(),
            "date": t.proxy(renames["DateIn"]).optional(),
        }
    ).named(renames["RepricingProductReportIn"])
    types["RepricingProductReportOut"] = t.struct(
        {
            "ruleIds": t.array(t.string()).optional(),
            "lowWatermark": t.proxy(renames["PriceAmountOut"]).optional(),
            "orderItemCount": t.integer().optional(),
            "inapplicabilityDetails": t.array(
                t.proxy(renames["InapplicabilityDetailsOut"])
            ).optional(),
            "applicationCount": t.string().optional(),
            "totalGmv": t.proxy(renames["PriceAmountOut"]).optional(),
            "buyboxWinningProductStats": t.proxy(
                renames["RepricingProductReportBuyboxWinningProductStatsOut"]
            ).optional(),
            "type": t.string().optional(),
            "highWatermark": t.proxy(renames["PriceAmountOut"]).optional(),
            "date": t.proxy(renames["DateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepricingProductReportOut"])
    types["ReturnPolicySeasonalOverrideIn"] = t.struct(
        {
            "endDate": t.string(),
            "policy": t.proxy(renames["ReturnPolicyPolicyIn"]),
            "startDate": t.string(),
            "name": t.string(),
        }
    ).named(renames["ReturnPolicySeasonalOverrideIn"])
    types["ReturnPolicySeasonalOverrideOut"] = t.struct(
        {
            "endDate": t.string(),
            "policy": t.proxy(renames["ReturnPolicyPolicyOut"]),
            "startDate": t.string(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReturnPolicySeasonalOverrideOut"])
    types["OrdersUpdateMerchantOrderIdRequestIn"] = t.struct(
        {"merchantOrderId": t.string().optional(), "operationId": t.string().optional()}
    ).named(renames["OrdersUpdateMerchantOrderIdRequestIn"])
    types["OrdersUpdateMerchantOrderIdRequestOut"] = t.struct(
        {
            "merchantOrderId": t.string().optional(),
            "operationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersUpdateMerchantOrderIdRequestOut"])
    types["AccountsUpdateLabelsResponseIn"] = t.struct(
        {"kind": t.string().optional()}
    ).named(renames["AccountsUpdateLabelsResponseIn"])
    types["AccountsUpdateLabelsResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountsUpdateLabelsResponseOut"])
    types["HolidayCutoffIn"] = t.struct(
        {
            "deadlineTimezone": t.string().optional(),
            "holidayId": t.string().optional(),
            "deadlineHour": t.integer().optional(),
            "deadlineDate": t.string().optional(),
            "visibleFromDate": t.string().optional(),
        }
    ).named(renames["HolidayCutoffIn"])
    types["HolidayCutoffOut"] = t.struct(
        {
            "deadlineTimezone": t.string().optional(),
            "holidayId": t.string().optional(),
            "deadlineHour": t.integer().optional(),
            "deadlineDate": t.string().optional(),
            "visibleFromDate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HolidayCutoffOut"])
    types["ProductDeliveryTimeAreaDeliveryTimeDeliveryTimeIn"] = t.struct(
        {
            "maxTransitTimeDays": t.integer(),
            "maxHandlingTimeDays": t.integer(),
            "minTransitTimeDays": t.integer(),
            "minHandlingTimeDays": t.integer(),
        }
    ).named(renames["ProductDeliveryTimeAreaDeliveryTimeDeliveryTimeIn"])
    types["ProductDeliveryTimeAreaDeliveryTimeDeliveryTimeOut"] = t.struct(
        {
            "maxTransitTimeDays": t.integer(),
            "maxHandlingTimeDays": t.integer(),
            "minTransitTimeDays": t.integer(),
            "minHandlingTimeDays": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductDeliveryTimeAreaDeliveryTimeDeliveryTimeOut"])
    types["ShipmentInvoiceLineItemInvoiceIn"] = t.struct(
        {
            "unitInvoice": t.proxy(renames["UnitInvoiceIn"]).optional(),
            "shipmentUnitIds": t.array(t.string()).optional(),
            "lineItemId": t.string().optional(),
            "productId": t.string().optional(),
        }
    ).named(renames["ShipmentInvoiceLineItemInvoiceIn"])
    types["ShipmentInvoiceLineItemInvoiceOut"] = t.struct(
        {
            "unitInvoice": t.proxy(renames["UnitInvoiceOut"]).optional(),
            "shipmentUnitIds": t.array(t.string()).optional(),
            "lineItemId": t.string().optional(),
            "productId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShipmentInvoiceLineItemInvoiceOut"])
    types["PriceAmountIn"] = t.struct(
        {"currency": t.string().optional(), "value": t.string().optional()}
    ).named(renames["PriceAmountIn"])
    types["PriceAmountOut"] = t.struct(
        {
            "currency": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PriceAmountOut"])
    types["ProductsCustomBatchRequestEntryIn"] = t.struct(
        {
            "feedId": t.string().optional(),
            "method": t.string().optional(),
            "productId": t.string().optional(),
            "updateMask": t.string().optional(),
            "batchId": t.integer().optional(),
            "product": t.proxy(renames["ProductIn"]).optional(),
            "merchantId": t.string().optional(),
        }
    ).named(renames["ProductsCustomBatchRequestEntryIn"])
    types["ProductsCustomBatchRequestEntryOut"] = t.struct(
        {
            "feedId": t.string().optional(),
            "method": t.string().optional(),
            "productId": t.string().optional(),
            "updateMask": t.string().optional(),
            "batchId": t.integer().optional(),
            "product": t.proxy(renames["ProductOut"]).optional(),
            "merchantId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductsCustomBatchRequestEntryOut"])
    types["UnitInvoiceIn"] = t.struct(
        {
            "additionalCharges": t.array(
                t.proxy(renames["UnitInvoiceAdditionalChargeIn"])
            ).optional(),
            "unitPrice": t.proxy(renames["PriceIn"]).optional(),
            "unitPriceTaxes": t.array(
                t.proxy(renames["UnitInvoiceTaxLineIn"])
            ).optional(),
        }
    ).named(renames["UnitInvoiceIn"])
    types["UnitInvoiceOut"] = t.struct(
        {
            "additionalCharges": t.array(
                t.proxy(renames["UnitInvoiceAdditionalChargeOut"])
            ).optional(),
            "unitPrice": t.proxy(renames["PriceOut"]).optional(),
            "unitPriceTaxes": t.array(
                t.proxy(renames["UnitInvoiceTaxLineOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UnitInvoiceOut"])
    types["LocalinventoryCustomBatchResponseEntryIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "errors": t.proxy(renames["ErrorsIn"]).optional(),
            "batchId": t.integer().optional(),
        }
    ).named(renames["LocalinventoryCustomBatchResponseEntryIn"])
    types["LocalinventoryCustomBatchResponseEntryOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "errors": t.proxy(renames["ErrorsOut"]).optional(),
            "batchId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocalinventoryCustomBatchResponseEntryOut"])
    types["ReturnPolicyOnlineRestockingFeeIn"] = t.struct(
        {
            "microPercent": t.integer().optional(),
            "fixedFee": t.proxy(renames["PriceAmountIn"]).optional(),
        }
    ).named(renames["ReturnPolicyOnlineRestockingFeeIn"])
    types["ReturnPolicyOnlineRestockingFeeOut"] = t.struct(
        {
            "microPercent": t.integer().optional(),
            "fixedFee": t.proxy(renames["PriceAmountOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReturnPolicyOnlineRestockingFeeOut"])
    types["AccountShippingImprovementsIn"] = t.struct(
        {"allowShippingImprovements": t.boolean().optional()}
    ).named(renames["AccountShippingImprovementsIn"])
    types["AccountShippingImprovementsOut"] = t.struct(
        {
            "allowShippingImprovements": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountShippingImprovementsOut"])
    types["PauseBuyOnGoogleProgramRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["PauseBuyOnGoogleProgramRequestIn"])
    types["PauseBuyOnGoogleProgramRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PauseBuyOnGoogleProgramRequestOut"])
    types["ProductShippingWeightIn"] = t.struct(
        {"value": t.number().optional(), "unit": t.string().optional()}
    ).named(renames["ProductShippingWeightIn"])
    types["ProductShippingWeightOut"] = t.struct(
        {
            "value": t.number().optional(),
            "unit": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductShippingWeightOut"])
    types["OrdersCreateTestReturnResponseIn"] = t.struct(
        {"kind": t.string().optional(), "returnId": t.string().optional()}
    ).named(renames["OrdersCreateTestReturnResponseIn"])
    types["OrdersCreateTestReturnResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "returnId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersCreateTestReturnResponseOut"])
    types["TransitTableTransitTimeRowIn"] = t.struct(
        {
            "values": t.array(
                t.proxy(renames["TransitTableTransitTimeRowTransitTimeValueIn"])
            )
        }
    ).named(renames["TransitTableTransitTimeRowIn"])
    types["TransitTableTransitTimeRowOut"] = t.struct(
        {
            "values": t.array(
                t.proxy(renames["TransitTableTransitTimeRowTransitTimeValueOut"])
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransitTableTransitTimeRowOut"])
    types["DatafeedstatusesCustomBatchResponseEntryIn"] = t.struct(
        {
            "datafeedStatus": t.proxy(renames["DatafeedStatusIn"]).optional(),
            "batchId": t.integer().optional(),
            "errors": t.proxy(renames["ErrorsIn"]).optional(),
        }
    ).named(renames["DatafeedstatusesCustomBatchResponseEntryIn"])
    types["DatafeedstatusesCustomBatchResponseEntryOut"] = t.struct(
        {
            "datafeedStatus": t.proxy(renames["DatafeedStatusOut"]).optional(),
            "batchId": t.integer().optional(),
            "errors": t.proxy(renames["ErrorsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatafeedstatusesCustomBatchResponseEntryOut"])
    types["ListCssesResponseIn"] = t.struct(
        {
            "csses": t.array(t.proxy(renames["CssIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListCssesResponseIn"])
    types["ListCssesResponseOut"] = t.struct(
        {
            "csses": t.array(t.proxy(renames["CssOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCssesResponseOut"])
    types["ListRepricingRulesResponseIn"] = t.struct(
        {
            "repricingRules": t.array(t.proxy(renames["RepricingRuleIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListRepricingRulesResponseIn"])
    types["ListRepricingRulesResponseOut"] = t.struct(
        {
            "repricingRules": t.array(t.proxy(renames["RepricingRuleOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListRepricingRulesResponseOut"])
    types["ReportRowIn"] = t.struct(
        {
            "priceCompetitiveness": t.proxy(
                renames["PriceCompetitivenessIn"]
            ).optional(),
            "priceInsights": t.proxy(renames["PriceInsightsIn"]).optional(),
            "productCluster": t.proxy(renames["ProductClusterIn"]).optional(),
            "metrics": t.proxy(renames["MetricsIn"]).optional(),
            "productView": t.proxy(renames["ProductViewIn"]).optional(),
            "bestSellers": t.proxy(renames["BestSellersIn"]).optional(),
            "segments": t.proxy(renames["SegmentsIn"]).optional(),
            "brand": t.proxy(renames["BrandIn"]).optional(),
        }
    ).named(renames["ReportRowIn"])
    types["ReportRowOut"] = t.struct(
        {
            "priceCompetitiveness": t.proxy(
                renames["PriceCompetitivenessOut"]
            ).optional(),
            "priceInsights": t.proxy(renames["PriceInsightsOut"]).optional(),
            "productCluster": t.proxy(renames["ProductClusterOut"]).optional(),
            "metrics": t.proxy(renames["MetricsOut"]).optional(),
            "productView": t.proxy(renames["ProductViewOut"]).optional(),
            "bestSellers": t.proxy(renames["BestSellersOut"]).optional(),
            "segments": t.proxy(renames["SegmentsOut"]).optional(),
            "brand": t.proxy(renames["BrandOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportRowOut"])
    types["OrdersInStoreRefundLineItemRequestIn"] = t.struct(
        {
            "taxAmount": t.proxy(renames["PriceIn"]).optional(),
            "productId": t.string().optional(),
            "quantity": t.integer().optional(),
            "reasonText": t.string().optional(),
            "reason": t.string().optional(),
            "priceAmount": t.proxy(renames["PriceIn"]).optional(),
            "operationId": t.string().optional(),
            "lineItemId": t.string().optional(),
        }
    ).named(renames["OrdersInStoreRefundLineItemRequestIn"])
    types["OrdersInStoreRefundLineItemRequestOut"] = t.struct(
        {
            "taxAmount": t.proxy(renames["PriceOut"]).optional(),
            "productId": t.string().optional(),
            "quantity": t.integer().optional(),
            "reasonText": t.string().optional(),
            "reason": t.string().optional(),
            "priceAmount": t.proxy(renames["PriceOut"]).optional(),
            "operationId": t.string().optional(),
            "lineItemId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersInStoreRefundLineItemRequestOut"])
    types["ListAccountLabelsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "accountLabels": t.array(t.proxy(renames["AccountLabelIn"])).optional(),
        }
    ).named(renames["ListAccountLabelsResponseIn"])
    types["ListAccountLabelsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "accountLabels": t.array(t.proxy(renames["AccountLabelOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAccountLabelsResponseOut"])
    types["CutoffTimeIn"] = t.struct(
        {
            "hour": t.integer().optional(),
            "minute": t.integer().optional(),
            "timezone": t.string().optional(),
        }
    ).named(renames["CutoffTimeIn"])
    types["CutoffTimeOut"] = t.struct(
        {
            "hour": t.integer().optional(),
            "minute": t.integer().optional(),
            "timezone": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CutoffTimeOut"])
    types["RequestReviewBuyOnGoogleProgramRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["RequestReviewBuyOnGoogleProgramRequestIn"])
    types["RequestReviewBuyOnGoogleProgramRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RequestReviewBuyOnGoogleProgramRequestOut"])
    types["ServiceStoreConfigCutoffConfigIn"] = t.struct(
        {
            "noDeliveryPostCutoff": t.boolean().optional(),
            "localCutoffTime": t.proxy(
                renames["ServiceStoreConfigCutoffConfigLocalCutoffTimeIn"]
            ).optional(),
            "storeCloseOffsetHours": t.string().optional(),
        }
    ).named(renames["ServiceStoreConfigCutoffConfigIn"])
    types["ServiceStoreConfigCutoffConfigOut"] = t.struct(
        {
            "noDeliveryPostCutoff": t.boolean().optional(),
            "localCutoffTime": t.proxy(
                renames["ServiceStoreConfigCutoffConfigLocalCutoffTimeOut"]
            ).optional(),
            "storeCloseOffsetHours": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceStoreConfigCutoffConfigOut"])
    types["AccountsLinkResponseIn"] = t.struct({"kind": t.string().optional()}).named(
        renames["AccountsLinkResponseIn"]
    )
    types["AccountsLinkResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountsLinkResponseOut"])
    types["AccountGoogleMyBusinessLinkIn"] = t.struct(
        {
            "status": t.string().optional(),
            "gmbEmail": t.string().optional(),
            "gmbAccountId": t.string().optional(),
        }
    ).named(renames["AccountGoogleMyBusinessLinkIn"])
    types["AccountGoogleMyBusinessLinkOut"] = t.struct(
        {
            "status": t.string().optional(),
            "gmbEmail": t.string().optional(),
            "gmbAccountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountGoogleMyBusinessLinkOut"])
    types["LiasettingsCustomBatchRequestEntryIn"] = t.struct(
        {
            "merchantId": t.string().optional(),
            "contactEmail": t.string().optional(),
            "method": t.string().optional(),
            "country": t.string().optional(),
            "posExternalAccountId": t.string().optional(),
            "posDataProviderId": t.string().optional(),
            "contactName": t.string().optional(),
            "liaSettings": t.proxy(renames["LiaSettingsIn"]).optional(),
            "gmbEmail": t.string().optional(),
            "batchId": t.integer().optional(),
            "accountId": t.string().optional(),
        }
    ).named(renames["LiasettingsCustomBatchRequestEntryIn"])
    types["LiasettingsCustomBatchRequestEntryOut"] = t.struct(
        {
            "merchantId": t.string().optional(),
            "contactEmail": t.string().optional(),
            "method": t.string().optional(),
            "country": t.string().optional(),
            "posExternalAccountId": t.string().optional(),
            "posDataProviderId": t.string().optional(),
            "contactName": t.string().optional(),
            "liaSettings": t.proxy(renames["LiaSettingsOut"]).optional(),
            "gmbEmail": t.string().optional(),
            "batchId": t.integer().optional(),
            "accountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiasettingsCustomBatchRequestEntryOut"])
    types["OrderreturnsListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "resources": t.array(t.proxy(renames["MerchantOrderReturnIn"])),
        }
    ).named(renames["OrderreturnsListResponseIn"])
    types["OrderreturnsListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "resources": t.array(t.proxy(renames["MerchantOrderReturnOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderreturnsListResponseOut"])
    types["LocalinventoryCustomBatchResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "entries": t.array(
                t.proxy(renames["LocalinventoryCustomBatchResponseEntryIn"])
            ).optional(),
        }
    ).named(renames["LocalinventoryCustomBatchResponseIn"])
    types["LocalinventoryCustomBatchResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "entries": t.array(
                t.proxy(renames["LocalinventoryCustomBatchResponseEntryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocalinventoryCustomBatchResponseOut"])
    types["OrdersInStoreRefundLineItemResponseIn"] = t.struct(
        {"executionStatus": t.string().optional(), "kind": t.string().optional()}
    ).named(renames["OrdersInStoreRefundLineItemResponseIn"])
    types["OrdersInStoreRefundLineItemResponseOut"] = t.struct(
        {
            "executionStatus": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersInStoreRefundLineItemResponseOut"])
    types["ProductShippingIn"] = t.struct(
        {
            "maxTransitTime": t.string().optional(),
            "region": t.string().optional(),
            "country": t.string().optional(),
            "postalCode": t.string().optional(),
            "service": t.string().optional(),
            "minHandlingTime": t.string().optional(),
            "maxHandlingTime": t.string().optional(),
            "price": t.proxy(renames["PriceIn"]).optional(),
            "minTransitTime": t.string().optional(),
            "locationId": t.string().optional(),
            "locationGroupName": t.string().optional(),
        }
    ).named(renames["ProductShippingIn"])
    types["ProductShippingOut"] = t.struct(
        {
            "maxTransitTime": t.string().optional(),
            "region": t.string().optional(),
            "country": t.string().optional(),
            "postalCode": t.string().optional(),
            "service": t.string().optional(),
            "minHandlingTime": t.string().optional(),
            "maxHandlingTime": t.string().optional(),
            "price": t.proxy(renames["PriceOut"]).optional(),
            "minTransitTime": t.string().optional(),
            "locationId": t.string().optional(),
            "locationGroupName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductShippingOut"])
    types["ShippingSettingsIn"] = t.struct(
        {
            "services": t.array(t.proxy(renames["ServiceIn"])).optional(),
            "warehouses": t.array(t.proxy(renames["WarehouseIn"])).optional(),
            "postalCodeGroups": t.array(
                t.proxy(renames["PostalCodeGroupIn"])
            ).optional(),
            "accountId": t.string().optional(),
        }
    ).named(renames["ShippingSettingsIn"])
    types["ShippingSettingsOut"] = t.struct(
        {
            "services": t.array(t.proxy(renames["ServiceOut"])).optional(),
            "warehouses": t.array(t.proxy(renames["WarehouseOut"])).optional(),
            "postalCodeGroups": t.array(
                t.proxy(renames["PostalCodeGroupOut"])
            ).optional(),
            "accountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShippingSettingsOut"])
    types["RepricingRuleRestrictionBoundaryIn"] = t.struct(
        {"percentageDelta": t.integer().optional(), "priceDelta": t.string().optional()}
    ).named(renames["RepricingRuleRestrictionBoundaryIn"])
    types["RepricingRuleRestrictionBoundaryOut"] = t.struct(
        {
            "percentageDelta": t.integer().optional(),
            "priceDelta": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepricingRuleRestrictionBoundaryOut"])
    types["AccountLabelIn"] = t.struct(
        {
            "name": t.string().optional(),
            "description": t.string().optional(),
            "accountId": t.string().optional(),
        }
    ).named(renames["AccountLabelIn"])
    types["AccountLabelOut"] = t.struct(
        {
            "labelType": t.string().optional(),
            "labelId": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "accountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountLabelOut"])
    types["OrdersGetByMerchantOrderIdResponseIn"] = t.struct(
        {"order": t.proxy(renames["OrderIn"]).optional(), "kind": t.string().optional()}
    ).named(renames["OrdersGetByMerchantOrderIdResponseIn"])
    types["OrdersGetByMerchantOrderIdResponseOut"] = t.struct(
        {
            "order": t.proxy(renames["OrderOut"]).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersGetByMerchantOrderIdResponseOut"])
    types["ProductstatusesCustomBatchResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "entries": t.array(
                t.proxy(renames["ProductstatusesCustomBatchResponseEntryIn"])
            ).optional(),
        }
    ).named(renames["ProductstatusesCustomBatchResponseIn"])
    types["ProductstatusesCustomBatchResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "entries": t.array(
                t.proxy(renames["ProductstatusesCustomBatchResponseEntryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductstatusesCustomBatchResponseOut"])
    types["AccountStatusIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "products": t.array(t.proxy(renames["AccountStatusProductsIn"])).optional(),
            "websiteClaimed": t.boolean().optional(),
            "accountId": t.string().optional(),
            "accountLevelIssues": t.array(
                t.proxy(renames["AccountStatusAccountLevelIssueIn"])
            ).optional(),
            "accountManagement": t.string().optional(),
        }
    ).named(renames["AccountStatusIn"])
    types["AccountStatusOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "products": t.array(
                t.proxy(renames["AccountStatusProductsOut"])
            ).optional(),
            "websiteClaimed": t.boolean().optional(),
            "accountId": t.string().optional(),
            "accountLevelIssues": t.array(
                t.proxy(renames["AccountStatusAccountLevelIssueOut"])
            ).optional(),
            "accountManagement": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountStatusOut"])
    types["OrderRefundIn"] = t.struct(
        {
            "actor": t.string().optional(),
            "creationDate": t.string().optional(),
            "amount": t.proxy(renames["PriceIn"]).optional(),
            "reason": t.string().optional(),
            "reasonText": t.string().optional(),
        }
    ).named(renames["OrderRefundIn"])
    types["OrderRefundOut"] = t.struct(
        {
            "actor": t.string().optional(),
            "creationDate": t.string().optional(),
            "amount": t.proxy(renames["PriceOut"]).optional(),
            "reason": t.string().optional(),
            "reasonText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderRefundOut"])
    types["TestOrderLineItemIn"] = t.struct(
        {
            "product": t.proxy(renames["TestOrderLineItemProductIn"]),
            "returnInfo": t.proxy(renames["OrderLineItemReturnInfoIn"]),
            "shippingDetails": t.proxy(renames["OrderLineItemShippingDetailsIn"]),
            "quantityOrdered": t.integer(),
        }
    ).named(renames["TestOrderLineItemIn"])
    types["TestOrderLineItemOut"] = t.struct(
        {
            "product": t.proxy(renames["TestOrderLineItemProductOut"]),
            "returnInfo": t.proxy(renames["OrderLineItemReturnInfoOut"]),
            "shippingDetails": t.proxy(renames["OrderLineItemShippingDetailsOut"]),
            "quantityOrdered": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestOrderLineItemOut"])
    types["OrderLineItemAdjustmentIn"] = t.struct(
        {
            "type": t.string().optional(),
            "taxAdjustment": t.proxy(renames["PriceIn"]).optional(),
            "priceAdjustment": t.proxy(renames["PriceIn"]).optional(),
        }
    ).named(renames["OrderLineItemAdjustmentIn"])
    types["OrderLineItemAdjustmentOut"] = t.struct(
        {
            "type": t.string().optional(),
            "taxAdjustment": t.proxy(renames["PriceOut"]).optional(),
            "priceAdjustment": t.proxy(renames["PriceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderLineItemAdjustmentOut"])
    types["PosSaleRequestIn"] = t.struct(
        {
            "saleId": t.string().optional(),
            "itemId": t.string(),
            "timestamp": t.string(),
            "targetCountry": t.string(),
            "contentLanguage": t.string(),
            "gtin": t.string().optional(),
            "storeCode": t.string(),
            "price": t.proxy(renames["PriceIn"]),
            "quantity": t.string(),
        }
    ).named(renames["PosSaleRequestIn"])
    types["PosSaleRequestOut"] = t.struct(
        {
            "saleId": t.string().optional(),
            "itemId": t.string(),
            "timestamp": t.string(),
            "targetCountry": t.string(),
            "contentLanguage": t.string(),
            "gtin": t.string().optional(),
            "storeCode": t.string(),
            "price": t.proxy(renames["PriceOut"]),
            "quantity": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PosSaleRequestOut"])
    types["ProductIdIn"] = t.struct({"productId": t.string().optional()}).named(
        renames["ProductIdIn"]
    )
    types["ProductIdOut"] = t.struct(
        {
            "productId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductIdOut"])
    types["ShoppingAdsProgramStatusReviewIneligibilityReasonDetailsIn"] = t.struct(
        {"cooldownTime": t.string().optional()}
    ).named(renames["ShoppingAdsProgramStatusReviewIneligibilityReasonDetailsIn"])
    types["ShoppingAdsProgramStatusReviewIneligibilityReasonDetailsOut"] = t.struct(
        {
            "cooldownTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShoppingAdsProgramStatusReviewIneligibilityReasonDetailsOut"])
    types["LoyaltyPointsIn"] = t.struct(
        {
            "pointsValue": t.string().optional(),
            "ratio": t.number().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["LoyaltyPointsIn"])
    types["LoyaltyPointsOut"] = t.struct(
        {
            "pointsValue": t.string().optional(),
            "ratio": t.number().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LoyaltyPointsOut"])
    types["ShippingsettingsCustomBatchResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "entries": t.array(
                t.proxy(renames["ShippingsettingsCustomBatchResponseEntryIn"])
            ).optional(),
        }
    ).named(renames["ShippingsettingsCustomBatchResponseIn"])
    types["ShippingsettingsCustomBatchResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "entries": t.array(
                t.proxy(renames["ShippingsettingsCustomBatchResponseEntryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShippingsettingsCustomBatchResponseOut"])
    types["OrderreturnsAcknowledgeResponseIn"] = t.struct(
        {"executionStatus": t.string().optional(), "kind": t.string().optional()}
    ).named(renames["OrderreturnsAcknowledgeResponseIn"])
    types["OrderreturnsAcknowledgeResponseOut"] = t.struct(
        {
            "executionStatus": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderreturnsAcknowledgeResponseOut"])
    types["ProductsCustomBatchResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "entries": t.array(
                t.proxy(renames["ProductsCustomBatchResponseEntryIn"])
            ).optional(),
        }
    ).named(renames["ProductsCustomBatchResponseIn"])
    types["ProductsCustomBatchResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "entries": t.array(
                t.proxy(renames["ProductsCustomBatchResponseEntryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductsCustomBatchResponseOut"])
    types["PosCustomBatchRequestIn"] = t.struct(
        {
            "entries": t.array(
                t.proxy(renames["PosCustomBatchRequestEntryIn"])
            ).optional()
        }
    ).named(renames["PosCustomBatchRequestIn"])
    types["PosCustomBatchRequestOut"] = t.struct(
        {
            "entries": t.array(
                t.proxy(renames["PosCustomBatchRequestEntryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PosCustomBatchRequestOut"])
    types["CssIn"] = t.struct({"labelIds": t.array(t.string()).optional()}).named(
        renames["CssIn"]
    )
    types["CssOut"] = t.struct(
        {
            "fullName": t.string().optional(),
            "labelIds": t.array(t.string()).optional(),
            "homepageUri": t.string().optional(),
            "cssDomainId": t.string().optional(),
            "cssGroupId": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CssOut"])
    types["ProductsListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "resources": t.array(t.proxy(renames["ProductIn"])),
        }
    ).named(renames["ProductsListResponseIn"])
    types["ProductsListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "resources": t.array(t.proxy(renames["ProductOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductsListResponseOut"])
    types["OrderLineItemIn"] = t.struct(
        {
            "quantityDelivered": t.integer().optional(),
            "cancellations": t.array(
                t.proxy(renames["OrderCancellationIn"])
            ).optional(),
            "quantityReturned": t.integer().optional(),
            "adjustments": t.array(
                t.proxy(renames["OrderLineItemAdjustmentIn"])
            ).optional(),
            "quantityUndeliverable": t.integer().optional(),
            "returns": t.array(t.proxy(renames["OrderReturnIn"])).optional(),
            "shippingDetails": t.proxy(
                renames["OrderLineItemShippingDetailsIn"]
            ).optional(),
            "quantityShipped": t.integer().optional(),
            "product": t.proxy(renames["OrderLineItemProductIn"]).optional(),
            "quantityCanceled": t.integer().optional(),
            "tax": t.proxy(renames["PriceIn"]).optional(),
            "price": t.proxy(renames["PriceIn"]).optional(),
            "annotations": t.array(
                t.proxy(renames["OrderMerchantProvidedAnnotationIn"])
            ).optional(),
            "quantityOrdered": t.integer().optional(),
            "id": t.string().optional(),
            "returnInfo": t.proxy(renames["OrderLineItemReturnInfoIn"]).optional(),
            "quantityPending": t.integer().optional(),
            "quantityReadyForPickup": t.integer().optional(),
        }
    ).named(renames["OrderLineItemIn"])
    types["OrderLineItemOut"] = t.struct(
        {
            "quantityDelivered": t.integer().optional(),
            "cancellations": t.array(
                t.proxy(renames["OrderCancellationOut"])
            ).optional(),
            "quantityReturned": t.integer().optional(),
            "adjustments": t.array(
                t.proxy(renames["OrderLineItemAdjustmentOut"])
            ).optional(),
            "quantityUndeliverable": t.integer().optional(),
            "returns": t.array(t.proxy(renames["OrderReturnOut"])).optional(),
            "shippingDetails": t.proxy(
                renames["OrderLineItemShippingDetailsOut"]
            ).optional(),
            "quantityShipped": t.integer().optional(),
            "product": t.proxy(renames["OrderLineItemProductOut"]).optional(),
            "quantityCanceled": t.integer().optional(),
            "tax": t.proxy(renames["PriceOut"]).optional(),
            "price": t.proxy(renames["PriceOut"]).optional(),
            "annotations": t.array(
                t.proxy(renames["OrderMerchantProvidedAnnotationOut"])
            ).optional(),
            "quantityOrdered": t.integer().optional(),
            "id": t.string().optional(),
            "returnInfo": t.proxy(renames["OrderLineItemReturnInfoOut"]).optional(),
            "quantityPending": t.integer().optional(),
            "quantityReadyForPickup": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderLineItemOut"])
    types["DatafeedsFetchNowResponseIn"] = t.struct(
        {"kind": t.string().optional()}
    ).named(renames["DatafeedsFetchNowResponseIn"])
    types["DatafeedsFetchNowResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatafeedsFetchNowResponseOut"])
    types["OrdersReturnRefundLineItemResponseIn"] = t.struct(
        {"kind": t.string().optional(), "executionStatus": t.string().optional()}
    ).named(renames["OrdersReturnRefundLineItemResponseIn"])
    types["OrdersReturnRefundLineItemResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "executionStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersReturnRefundLineItemResponseOut"])
    types["OrdersCancelLineItemResponseIn"] = t.struct(
        {"kind": t.string().optional(), "executionStatus": t.string().optional()}
    ).named(renames["OrdersCancelLineItemResponseIn"])
    types["OrdersCancelLineItemResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "executionStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersCancelLineItemResponseOut"])
    types["ShippingsettingsListResponseIn"] = t.struct(
        {
            "resources": t.array(t.proxy(renames["ShippingSettingsIn"])),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ShippingsettingsListResponseIn"])
    types["ShippingsettingsListResponseOut"] = t.struct(
        {
            "resources": t.array(t.proxy(renames["ShippingSettingsOut"])),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShippingsettingsListResponseOut"])
    types["RequestReviewFreeListingsRequestIn"] = t.struct(
        {"regionCode": t.string().optional()}
    ).named(renames["RequestReviewFreeListingsRequestIn"])
    types["RequestReviewFreeListingsRequestOut"] = t.struct(
        {
            "regionCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestReviewFreeListingsRequestOut"])
    types["LiaOnDisplayToOrderSettingsIn"] = t.struct(
        {
            "shippingCostPolicyUrl": t.string().optional(),
            "status": t.string().optional(),
        }
    ).named(renames["LiaOnDisplayToOrderSettingsIn"])
    types["LiaOnDisplayToOrderSettingsOut"] = t.struct(
        {
            "shippingCostPolicyUrl": t.string().optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiaOnDisplayToOrderSettingsOut"])
    types[
        "OrderinvoicesCustomBatchRequestEntryCreateRefundInvoiceRefundOptionIn"
    ] = t.struct(
        {"description": t.string().optional(), "reason": t.string().optional()}
    ).named(
        renames["OrderinvoicesCustomBatchRequestEntryCreateRefundInvoiceRefundOptionIn"]
    )
    types[
        "OrderinvoicesCustomBatchRequestEntryCreateRefundInvoiceRefundOptionOut"
    ] = t.struct(
        {
            "description": t.string().optional(),
            "reason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "OrderinvoicesCustomBatchRequestEntryCreateRefundInvoiceRefundOptionOut"
        ]
    )
    types["ReturnpolicyCustomBatchResponseIn"] = t.struct(
        {
            "entries": t.array(
                t.proxy(renames["ReturnpolicyCustomBatchResponseEntryIn"])
            ).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ReturnpolicyCustomBatchResponseIn"])
    types["ReturnpolicyCustomBatchResponseOut"] = t.struct(
        {
            "entries": t.array(
                t.proxy(renames["ReturnpolicyCustomBatchResponseEntryOut"])
            ).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReturnpolicyCustomBatchResponseOut"])
    types["LiasettingsSetPosDataProviderResponseIn"] = t.struct(
        {"kind": t.string().optional()}
    ).named(renames["LiasettingsSetPosDataProviderResponseIn"])
    types["LiasettingsSetPosDataProviderResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiasettingsSetPosDataProviderResponseOut"])
    types["CarrierRateIn"] = t.struct(
        {
            "originPostalCode": t.string().optional(),
            "carrierService": t.string().optional(),
            "percentageAdjustment": t.string().optional(),
            "carrierName": t.string().optional(),
            "flatAdjustment": t.proxy(renames["PriceIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["CarrierRateIn"])
    types["CarrierRateOut"] = t.struct(
        {
            "originPostalCode": t.string().optional(),
            "carrierService": t.string().optional(),
            "percentageAdjustment": t.string().optional(),
            "carrierName": t.string().optional(),
            "flatAdjustment": t.proxy(renames["PriceOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CarrierRateOut"])
    types["LiaSettingsIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "countrySettings": t.array(
                t.proxy(renames["LiaCountrySettingsIn"])
            ).optional(),
            "accountId": t.string().optional(),
        }
    ).named(renames["LiaSettingsIn"])
    types["LiaSettingsOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "countrySettings": t.array(
                t.proxy(renames["LiaCountrySettingsOut"])
            ).optional(),
            "accountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiaSettingsOut"])
    types["RequestPhoneVerificationResponseIn"] = t.struct(
        {"verificationId": t.string().optional()}
    ).named(renames["RequestPhoneVerificationResponseIn"])
    types["RequestPhoneVerificationResponseOut"] = t.struct(
        {
            "verificationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestPhoneVerificationResponseOut"])
    types["AccounttaxCustomBatchResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "entries": t.array(
                t.proxy(renames["AccounttaxCustomBatchResponseEntryIn"])
            ).optional(),
        }
    ).named(renames["AccounttaxCustomBatchResponseIn"])
    types["AccounttaxCustomBatchResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "entries": t.array(
                t.proxy(renames["AccounttaxCustomBatchResponseEntryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccounttaxCustomBatchResponseOut"])
    types["AccountsAuthInfoResponseIn"] = t.struct(
        {
            "accountIdentifiers": t.array(
                t.proxy(renames["AccountIdentifierIn"])
            ).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["AccountsAuthInfoResponseIn"])
    types["AccountsAuthInfoResponseOut"] = t.struct(
        {
            "accountIdentifiers": t.array(
                t.proxy(renames["AccountIdentifierOut"])
            ).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountsAuthInfoResponseOut"])
    types["RateGroupIn"] = t.struct(
        {
            "mainTable": t.proxy(renames["TableIn"]).optional(),
            "applicableShippingLabels": t.array(t.string()).optional(),
            "subtables": t.array(t.proxy(renames["TableIn"])).optional(),
            "carrierRates": t.array(t.proxy(renames["CarrierRateIn"])).optional(),
            "singleValue": t.proxy(renames["ValueIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["RateGroupIn"])
    types["RateGroupOut"] = t.struct(
        {
            "mainTable": t.proxy(renames["TableOut"]).optional(),
            "applicableShippingLabels": t.array(t.string()).optional(),
            "subtables": t.array(t.proxy(renames["TableOut"])).optional(),
            "carrierRates": t.array(t.proxy(renames["CarrierRateOut"])).optional(),
            "singleValue": t.proxy(renames["ValueOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RateGroupOut"])
    types["PosSaleResponseIn"] = t.struct(
        {
            "gtin": t.string().optional(),
            "contentLanguage": t.string(),
            "targetCountry": t.string(),
            "quantity": t.string(),
            "timestamp": t.string(),
            "kind": t.string().optional(),
            "saleId": t.string().optional(),
            "itemId": t.string(),
            "price": t.proxy(renames["PriceIn"]),
            "storeCode": t.string(),
        }
    ).named(renames["PosSaleResponseIn"])
    types["PosSaleResponseOut"] = t.struct(
        {
            "gtin": t.string().optional(),
            "contentLanguage": t.string(),
            "targetCountry": t.string(),
            "quantity": t.string(),
            "timestamp": t.string(),
            "kind": t.string().optional(),
            "saleId": t.string().optional(),
            "itemId": t.string(),
            "price": t.proxy(renames["PriceOut"]),
            "storeCode": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PosSaleResponseOut"])
    types["ProductClusterIn"] = t.struct(
        {
            "title": t.string().optional(),
            "categoryL3": t.string().optional(),
            "categoryL4": t.string().optional(),
            "inventoryStatus": t.string().optional(),
            "categoryL2": t.string().optional(),
            "brand": t.string().optional(),
            "categoryL1": t.string().optional(),
            "variantGtins": t.array(t.string()).optional(),
            "brandInventoryStatus": t.string().optional(),
            "categoryL5": t.string().optional(),
        }
    ).named(renames["ProductClusterIn"])
    types["ProductClusterOut"] = t.struct(
        {
            "title": t.string().optional(),
            "categoryL3": t.string().optional(),
            "categoryL4": t.string().optional(),
            "inventoryStatus": t.string().optional(),
            "categoryL2": t.string().optional(),
            "brand": t.string().optional(),
            "categoryL1": t.string().optional(),
            "variantGtins": t.array(t.string()).optional(),
            "brandInventoryStatus": t.string().optional(),
            "categoryL5": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductClusterOut"])
    types["TransitTableIn"] = t.struct(
        {
            "transitTimeLabels": t.array(t.string()).optional(),
            "rows": t.array(t.proxy(renames["TransitTableTransitTimeRowIn"])),
            "postalCodeGroupNames": t.array(t.string()).optional(),
        }
    ).named(renames["TransitTableIn"])
    types["TransitTableOut"] = t.struct(
        {
            "transitTimeLabels": t.array(t.string()).optional(),
            "rows": t.array(t.proxy(renames["TransitTableTransitTimeRowOut"])),
            "postalCodeGroupNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransitTableOut"])
    types["OrdersReturnRefundLineItemRequestIn"] = t.struct(
        {
            "productId": t.string().optional(),
            "operationId": t.string().optional(),
            "reason": t.string().optional(),
            "taxAmount": t.proxy(renames["PriceIn"]).optional(),
            "lineItemId": t.string().optional(),
            "priceAmount": t.proxy(renames["PriceIn"]).optional(),
            "quantity": t.integer().optional(),
            "reasonText": t.string().optional(),
        }
    ).named(renames["OrdersReturnRefundLineItemRequestIn"])
    types["OrdersReturnRefundLineItemRequestOut"] = t.struct(
        {
            "productId": t.string().optional(),
            "operationId": t.string().optional(),
            "reason": t.string().optional(),
            "taxAmount": t.proxy(renames["PriceOut"]).optional(),
            "lineItemId": t.string().optional(),
            "priceAmount": t.proxy(renames["PriceOut"]).optional(),
            "quantity": t.integer().optional(),
            "reasonText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersReturnRefundLineItemRequestOut"])
    types["AddressIn"] = t.struct(
        {
            "country": t.string(),
            "postalCode": t.string(),
            "streetAddress": t.string().optional(),
            "administrativeArea": t.string(),
            "city": t.string(),
        }
    ).named(renames["AddressIn"])
    types["AddressOut"] = t.struct(
        {
            "country": t.string(),
            "postalCode": t.string(),
            "streetAddress": t.string().optional(),
            "administrativeArea": t.string(),
            "city": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddressOut"])
    types["LabelIdsIn"] = t.struct({"labelIds": t.array(t.string()).optional()}).named(
        renames["LabelIdsIn"]
    )
    types["LabelIdsOut"] = t.struct(
        {
            "labelIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LabelIdsOut"])
    types["WarehouseBasedDeliveryTimeIn"] = t.struct(
        {
            "warehouseName": t.string().optional(),
            "originAdministrativeArea": t.string().optional(),
            "originCountry": t.string().optional(),
            "carrier": t.string(),
            "originCity": t.string().optional(),
            "carrierService": t.string(),
            "originPostalCode": t.string().optional(),
            "originStreetAddress": t.string().optional(),
        }
    ).named(renames["WarehouseBasedDeliveryTimeIn"])
    types["WarehouseBasedDeliveryTimeOut"] = t.struct(
        {
            "warehouseName": t.string().optional(),
            "originAdministrativeArea": t.string().optional(),
            "originCountry": t.string().optional(),
            "carrier": t.string(),
            "originCity": t.string().optional(),
            "carrierService": t.string(),
            "originPostalCode": t.string().optional(),
            "originStreetAddress": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WarehouseBasedDeliveryTimeOut"])
    types["ReturnAddressAddressIn"] = t.struct(
        {
            "recipientName": t.string().optional(),
            "region": t.string().optional(),
            "country": t.string().optional(),
            "postalCode": t.string().optional(),
            "locality": t.string().optional(),
            "streetAddress": t.array(t.string()).optional(),
        }
    ).named(renames["ReturnAddressAddressIn"])
    types["ReturnAddressAddressOut"] = t.struct(
        {
            "recipientName": t.string().optional(),
            "region": t.string().optional(),
            "country": t.string().optional(),
            "postalCode": t.string().optional(),
            "locality": t.string().optional(),
            "streetAddress": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReturnAddressAddressOut"])
    types["AccountTaxIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "rules": t.array(t.proxy(renames["AccountTaxTaxRuleIn"])).optional(),
            "accountId": t.string(),
        }
    ).named(renames["AccountTaxIn"])
    types["AccountTaxOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "rules": t.array(t.proxy(renames["AccountTaxTaxRuleOut"])).optional(),
            "accountId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountTaxOut"])
    types["DatafeedIn"] = t.struct(
        {
            "attributeLanguage": t.string().optional(),
            "kind": t.string().optional(),
            "contentType": t.string(),
            "format": t.proxy(renames["DatafeedFormatIn"]).optional(),
            "name": t.string(),
            "targets": t.array(t.proxy(renames["DatafeedTargetIn"])).optional(),
            "fetchSchedule": t.proxy(renames["DatafeedFetchScheduleIn"]).optional(),
            "id": t.string(),
            "fileName": t.string(),
        }
    ).named(renames["DatafeedIn"])
    types["DatafeedOut"] = t.struct(
        {
            "attributeLanguage": t.string().optional(),
            "kind": t.string().optional(),
            "contentType": t.string(),
            "format": t.proxy(renames["DatafeedFormatOut"]).optional(),
            "name": t.string(),
            "targets": t.array(t.proxy(renames["DatafeedTargetOut"])).optional(),
            "fetchSchedule": t.proxy(renames["DatafeedFetchScheduleOut"]).optional(),
            "id": t.string(),
            "fileName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatafeedOut"])
    types["RepricingRuleEffectiveTimeFixedTimePeriodIn"] = t.struct(
        {"endTime": t.string().optional(), "startTime": t.string().optional()}
    ).named(renames["RepricingRuleEffectiveTimeFixedTimePeriodIn"])
    types["RepricingRuleEffectiveTimeFixedTimePeriodOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepricingRuleEffectiveTimeFixedTimePeriodOut"])
    types["OrdersCreateTestReturnRequestIn"] = t.struct(
        {
            "items": t.array(
                t.proxy(
                    renames["OrdersCustomBatchRequestEntryCreateTestReturnReturnItemIn"]
                )
            ).optional()
        }
    ).named(renames["OrdersCreateTestReturnRequestIn"])
    types["OrdersCreateTestReturnRequestOut"] = t.struct(
        {
            "items": t.array(
                t.proxy(
                    renames[
                        "OrdersCustomBatchRequestEntryCreateTestReturnReturnItemOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersCreateTestReturnRequestOut"])
    types["AccountIn"] = t.struct(
        {
            "googleMyBusinessLink": t.proxy(
                renames["AccountGoogleMyBusinessLinkIn"]
            ).optional(),
            "adultContent": t.boolean().optional(),
            "adsLinks": t.array(t.proxy(renames["AccountAdsLinkIn"])).optional(),
            "cssId": t.string().optional(),
            "labelIds": t.array(t.string()).optional(),
            "sellerId": t.string().optional(),
            "name": t.string(),
            "id": t.string(),
            "businessInformation": t.proxy(
                renames["AccountBusinessInformationIn"]
            ).optional(),
            "automaticLabelIds": t.array(t.string()).optional(),
            "websiteUrl": t.string().optional(),
            "youtubeChannelLinks": t.array(
                t.proxy(renames["AccountYouTubeChannelLinkIn"])
            ).optional(),
            "automaticImprovements": t.proxy(
                renames["AccountAutomaticImprovementsIn"]
            ).optional(),
            "kind": t.string().optional(),
            "users": t.array(t.proxy(renames["AccountUserIn"])).optional(),
            "conversionSettings": t.proxy(
                renames["AccountConversionSettingsIn"]
            ).optional(),
        }
    ).named(renames["AccountIn"])
    types["AccountOut"] = t.struct(
        {
            "googleMyBusinessLink": t.proxy(
                renames["AccountGoogleMyBusinessLinkOut"]
            ).optional(),
            "adultContent": t.boolean().optional(),
            "adsLinks": t.array(t.proxy(renames["AccountAdsLinkOut"])).optional(),
            "cssId": t.string().optional(),
            "labelIds": t.array(t.string()).optional(),
            "sellerId": t.string().optional(),
            "name": t.string(),
            "id": t.string(),
            "accountManagement": t.string().optional(),
            "businessInformation": t.proxy(
                renames["AccountBusinessInformationOut"]
            ).optional(),
            "automaticLabelIds": t.array(t.string()).optional(),
            "websiteUrl": t.string().optional(),
            "youtubeChannelLinks": t.array(
                t.proxy(renames["AccountYouTubeChannelLinkOut"])
            ).optional(),
            "automaticImprovements": t.proxy(
                renames["AccountAutomaticImprovementsOut"]
            ).optional(),
            "kind": t.string().optional(),
            "users": t.array(t.proxy(renames["AccountUserOut"])).optional(),
            "conversionSettings": t.proxy(
                renames["AccountConversionSettingsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountOut"])
    types["AccountCredentialsIn"] = t.struct(
        {
            "expiresIn": t.string().optional(),
            "accessToken": t.string().optional(),
            "purpose": t.string().optional(),
        }
    ).named(renames["AccountCredentialsIn"])
    types["AccountCredentialsOut"] = t.struct(
        {
            "expiresIn": t.string().optional(),
            "accessToken": t.string().optional(),
            "purpose": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountCredentialsOut"])
    types["ReturnPolicyIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "label": t.string(),
            "nonFreeReturnReasons": t.array(t.string()).optional(),
            "policy": t.proxy(renames["ReturnPolicyPolicyIn"]),
            "name": t.string(),
            "seasonalOverrides": t.array(
                t.proxy(renames["ReturnPolicySeasonalOverrideIn"])
            ).optional(),
            "returnPolicyId": t.string().optional(),
            "country": t.string(),
            "returnShippingFee": t.proxy(renames["PriceIn"]).optional(),
        }
    ).named(renames["ReturnPolicyIn"])
    types["ReturnPolicyOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "label": t.string(),
            "nonFreeReturnReasons": t.array(t.string()).optional(),
            "policy": t.proxy(renames["ReturnPolicyPolicyOut"]),
            "name": t.string(),
            "seasonalOverrides": t.array(
                t.proxy(renames["ReturnPolicySeasonalOverrideOut"])
            ).optional(),
            "returnPolicyId": t.string().optional(),
            "country": t.string(),
            "returnShippingFee": t.proxy(renames["PriceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReturnPolicyOut"])
    types["HolidaysHolidayIn"] = t.struct(
        {
            "id": t.string().optional(),
            "deliveryGuaranteeDate": t.string().optional(),
            "countryCode": t.string().optional(),
            "type": t.string().optional(),
            "date": t.string().optional(),
            "deliveryGuaranteeHour": t.string().optional(),
        }
    ).named(renames["HolidaysHolidayIn"])
    types["HolidaysHolidayOut"] = t.struct(
        {
            "id": t.string().optional(),
            "deliveryGuaranteeDate": t.string().optional(),
            "countryCode": t.string().optional(),
            "type": t.string().optional(),
            "date": t.string().optional(),
            "deliveryGuaranteeHour": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HolidaysHolidayOut"])
    types["AccountUserIn"] = t.struct(
        {
            "paymentsAnalyst": t.boolean().optional(),
            "paymentsManager": t.boolean().optional(),
            "reportingManager": t.boolean().optional(),
            "admin": t.boolean().optional(),
            "emailAddress": t.string().optional(),
            "orderManager": t.boolean().optional(),
        }
    ).named(renames["AccountUserIn"])
    types["AccountUserOut"] = t.struct(
        {
            "paymentsAnalyst": t.boolean().optional(),
            "paymentsManager": t.boolean().optional(),
            "reportingManager": t.boolean().optional(),
            "admin": t.boolean().optional(),
            "emailAddress": t.string().optional(),
            "orderManager": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountUserOut"])
    types["MetricsIn"] = t.struct(
        {
            "returnRate": t.number().optional(),
            "shippedOrders": t.string().optional(),
            "shippedItemSalesMicros": t.string().optional(),
            "orderedItemSalesMicros": t.string().optional(),
            "returnedItems": t.string().optional(),
            "itemFillRate": t.number().optional(),
            "orderedItems": t.string().optional(),
            "conversionValueMicros": t.string().optional(),
            "rejectedItems": t.string().optional(),
            "clicks": t.string().optional(),
            "shippedItems": t.string().optional(),
            "itemDaysToShip": t.number().optional(),
            "aovMicros": t.number().optional(),
            "impressions": t.string().optional(),
            "returnsMicros": t.string().optional(),
            "conversionRate": t.number().optional(),
            "unshippedOrders": t.number().optional(),
            "unshippedItems": t.number().optional(),
            "daysToShip": t.number().optional(),
            "orders": t.string().optional(),
            "aos": t.number().optional(),
            "conversions": t.number().optional(),
            "ctr": t.number().optional(),
        }
    ).named(renames["MetricsIn"])
    types["MetricsOut"] = t.struct(
        {
            "returnRate": t.number().optional(),
            "shippedOrders": t.string().optional(),
            "shippedItemSalesMicros": t.string().optional(),
            "orderedItemSalesMicros": t.string().optional(),
            "returnedItems": t.string().optional(),
            "itemFillRate": t.number().optional(),
            "orderedItems": t.string().optional(),
            "conversionValueMicros": t.string().optional(),
            "rejectedItems": t.string().optional(),
            "clicks": t.string().optional(),
            "shippedItems": t.string().optional(),
            "itemDaysToShip": t.number().optional(),
            "aovMicros": t.number().optional(),
            "impressions": t.string().optional(),
            "returnsMicros": t.string().optional(),
            "conversionRate": t.number().optional(),
            "unshippedOrders": t.number().optional(),
            "unshippedItems": t.number().optional(),
            "daysToShip": t.number().optional(),
            "orders": t.string().optional(),
            "aos": t.number().optional(),
            "conversions": t.number().optional(),
            "ctr": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricsOut"])
    types["UndeleteConversionSourceRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["UndeleteConversionSourceRequestIn"])
    types["UndeleteConversionSourceRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UndeleteConversionSourceRequestOut"])
    types["TimePeriodIn"] = t.struct(
        {"startTime": t.string().optional(), "endTime": t.string().optional()}
    ).named(renames["TimePeriodIn"])
    types["TimePeriodOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimePeriodOut"])
    types["LocationIdSetIn"] = t.struct(
        {"locationIds": t.array(t.string()).optional()}
    ).named(renames["LocationIdSetIn"])
    types["LocationIdSetOut"] = t.struct(
        {
            "locationIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationIdSetOut"])
    types["MinimumOrderValueTableIn"] = t.struct(
        {
            "storeCodeSetWithMovs": t.array(
                t.proxy(renames["MinimumOrderValueTableStoreCodeSetWithMovIn"])
            )
        }
    ).named(renames["MinimumOrderValueTableIn"])
    types["MinimumOrderValueTableOut"] = t.struct(
        {
            "storeCodeSetWithMovs": t.array(
                t.proxy(renames["MinimumOrderValueTableStoreCodeSetWithMovOut"])
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MinimumOrderValueTableOut"])
    types["GmbAccountsIn"] = t.struct(
        {
            "accountId": t.string().optional(),
            "gmbAccounts": t.array(
                t.proxy(renames["GmbAccountsGmbAccountIn"])
            ).optional(),
        }
    ).named(renames["GmbAccountsIn"])
    types["GmbAccountsOut"] = t.struct(
        {
            "accountId": t.string().optional(),
            "gmbAccounts": t.array(
                t.proxy(renames["GmbAccountsGmbAccountOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GmbAccountsOut"])
    types["CustomAttributeIn"] = t.struct(
        {
            "groupValues": t.array(t.proxy(renames["CustomAttributeIn"])).optional(),
            "value": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["CustomAttributeIn"])
    types["CustomAttributeOut"] = t.struct(
        {
            "groupValues": t.array(t.proxy(renames["CustomAttributeOut"])).optional(),
            "value": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomAttributeOut"])
    types["SettlementTransactionAmountIn"] = t.struct(
        {
            "description": t.string().optional(),
            "type": t.string().optional(),
            "transactionAmount": t.proxy(renames["PriceIn"]).optional(),
            "commission": t.proxy(renames["SettlementTransactionAmountCommissionIn"]),
        }
    ).named(renames["SettlementTransactionAmountIn"])
    types["SettlementTransactionAmountOut"] = t.struct(
        {
            "description": t.string().optional(),
            "type": t.string().optional(),
            "transactionAmount": t.proxy(renames["PriceOut"]).optional(),
            "commission": t.proxy(renames["SettlementTransactionAmountCommissionOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SettlementTransactionAmountOut"])
    types["TimeZoneIn"] = t.struct(
        {"version": t.string().optional(), "id": t.string().optional()}
    ).named(renames["TimeZoneIn"])
    types["TimeZoneOut"] = t.struct(
        {
            "version": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeZoneOut"])
    types["DatafeedsCustomBatchRequestEntryIn"] = t.struct(
        {
            "merchantId": t.string().optional(),
            "datafeedId": t.string().optional(),
            "batchId": t.integer().optional(),
            "datafeed": t.proxy(renames["DatafeedIn"]).optional(),
            "method": t.string().optional(),
        }
    ).named(renames["DatafeedsCustomBatchRequestEntryIn"])
    types["DatafeedsCustomBatchRequestEntryOut"] = t.struct(
        {
            "merchantId": t.string().optional(),
            "datafeedId": t.string().optional(),
            "batchId": t.integer().optional(),
            "datafeed": t.proxy(renames["DatafeedOut"]).optional(),
            "method": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatafeedsCustomBatchRequestEntryOut"])
    types["ReturnPolicyOnlinePolicyIn"] = t.struct(
        {"type": t.string().optional(), "days": t.string().optional()}
    ).named(renames["ReturnPolicyOnlinePolicyIn"])
    types["ReturnPolicyOnlinePolicyOut"] = t.struct(
        {
            "type": t.string().optional(),
            "days": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReturnPolicyOnlinePolicyOut"])
    types["ReturnpolicyCustomBatchRequestIn"] = t.struct(
        {
            "entries": t.array(
                t.proxy(renames["ReturnpolicyCustomBatchRequestEntryIn"])
            ).optional()
        }
    ).named(renames["ReturnpolicyCustomBatchRequestIn"])
    types["ReturnpolicyCustomBatchRequestOut"] = t.struct(
        {
            "entries": t.array(
                t.proxy(renames["ReturnpolicyCustomBatchRequestEntryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReturnpolicyCustomBatchRequestOut"])
    types["UnitInvoiceTaxLineIn"] = t.struct(
        {
            "taxType": t.string().optional(),
            "taxAmount": t.proxy(renames["PriceIn"]).optional(),
            "taxName": t.string().optional(),
        }
    ).named(renames["UnitInvoiceTaxLineIn"])
    types["UnitInvoiceTaxLineOut"] = t.struct(
        {
            "taxType": t.string().optional(),
            "taxAmount": t.proxy(renames["PriceOut"]).optional(),
            "taxName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UnitInvoiceTaxLineOut"])
    types["OrdersUpdateShipmentRequestIn"] = t.struct(
        {
            "readyPickupDate": t.string().optional(),
            "trackingId": t.string().optional(),
            "status": t.string().optional(),
            "shipmentId": t.string().optional(),
            "carrier": t.string().optional(),
            "undeliveredDate": t.string().optional(),
            "operationId": t.string().optional(),
            "deliveryDate": t.string().optional(),
            "lastPickupDate": t.string().optional(),
            "scheduledDeliveryDetails": t.proxy(
                renames[
                    "OrdersCustomBatchRequestEntryUpdateShipmentScheduledDeliveryDetailsIn"
                ]
            ).optional(),
        }
    ).named(renames["OrdersUpdateShipmentRequestIn"])
    types["OrdersUpdateShipmentRequestOut"] = t.struct(
        {
            "readyPickupDate": t.string().optional(),
            "trackingId": t.string().optional(),
            "status": t.string().optional(),
            "shipmentId": t.string().optional(),
            "carrier": t.string().optional(),
            "undeliveredDate": t.string().optional(),
            "operationId": t.string().optional(),
            "deliveryDate": t.string().optional(),
            "lastPickupDate": t.string().optional(),
            "scheduledDeliveryDetails": t.proxy(
                renames[
                    "OrdersCustomBatchRequestEntryUpdateShipmentScheduledDeliveryDetailsOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersUpdateShipmentRequestOut"])
    types["VerifyPhoneNumberResponseIn"] = t.struct(
        {"verifiedPhoneNumber": t.string().optional()}
    ).named(renames["VerifyPhoneNumberResponseIn"])
    types["VerifyPhoneNumberResponseOut"] = t.struct(
        {
            "verifiedPhoneNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VerifyPhoneNumberResponseOut"])
    types["ProductDeliveryTimeAreaDeliveryTimeIn"] = t.struct(
        {
            "deliveryArea": t.proxy(renames["DeliveryAreaIn"]),
            "deliveryTime": t.proxy(
                renames["ProductDeliveryTimeAreaDeliveryTimeDeliveryTimeIn"]
            ),
        }
    ).named(renames["ProductDeliveryTimeAreaDeliveryTimeIn"])
    types["ProductDeliveryTimeAreaDeliveryTimeOut"] = t.struct(
        {
            "deliveryArea": t.proxy(renames["DeliveryAreaOut"]),
            "deliveryTime": t.proxy(
                renames["ProductDeliveryTimeAreaDeliveryTimeDeliveryTimeOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductDeliveryTimeAreaDeliveryTimeOut"])
    types["AccountAutomaticImprovementsIn"] = t.struct(
        {
            "shippingImprovements": t.proxy(
                renames["AccountShippingImprovementsIn"]
            ).optional(),
            "itemUpdates": t.proxy(renames["AccountItemUpdatesIn"]).optional(),
            "imageImprovements": t.proxy(
                renames["AccountImageImprovementsIn"]
            ).optional(),
        }
    ).named(renames["AccountAutomaticImprovementsIn"])
    types["AccountAutomaticImprovementsOut"] = t.struct(
        {
            "shippingImprovements": t.proxy(
                renames["AccountShippingImprovementsOut"]
            ).optional(),
            "itemUpdates": t.proxy(renames["AccountItemUpdatesOut"]).optional(),
            "imageImprovements": t.proxy(
                renames["AccountImageImprovementsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountAutomaticImprovementsOut"])
    types["PosStoreIn"] = t.struct(
        {
            "storeAddress": t.string(),
            "kind": t.string().optional(),
            "websiteUrl": t.string().optional(),
            "storeCode": t.string(),
            "phoneNumber": t.string().optional(),
            "gcidCategory": t.array(t.string()).optional(),
            "placeId": t.string().optional(),
            "storeName": t.string().optional(),
        }
    ).named(renames["PosStoreIn"])
    types["PosStoreOut"] = t.struct(
        {
            "storeAddress": t.string(),
            "kind": t.string().optional(),
            "websiteUrl": t.string().optional(),
            "storeCode": t.string(),
            "phoneNumber": t.string().optional(),
            "gcidCategory": t.array(t.string()).optional(),
            "placeId": t.string().optional(),
            "storeName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PosStoreOut"])
    types["OrdersUpdateMerchantOrderIdResponseIn"] = t.struct(
        {"kind": t.string().optional(), "executionStatus": t.string().optional()}
    ).named(renames["OrdersUpdateMerchantOrderIdResponseIn"])
    types["OrdersUpdateMerchantOrderIdResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "executionStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersUpdateMerchantOrderIdResponseOut"])
    types["CaptureOrderRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CaptureOrderRequestIn"]
    )
    types["CaptureOrderRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CaptureOrderRequestOut"])
    types["AccountYouTubeChannelLinkIn"] = t.struct(
        {"channelId": t.string().optional(), "status": t.string().optional()}
    ).named(renames["AccountYouTubeChannelLinkIn"])
    types["AccountYouTubeChannelLinkOut"] = t.struct(
        {
            "channelId": t.string().optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountYouTubeChannelLinkOut"])
    types["OrderPromotionItemIn"] = t.struct(
        {
            "lineItemId": t.string().optional(),
            "quantity": t.integer().optional(),
            "productId": t.string().optional(),
            "offerId": t.string(),
        }
    ).named(renames["OrderPromotionItemIn"])
    types["OrderPromotionItemOut"] = t.struct(
        {
            "lineItemId": t.string().optional(),
            "quantity": t.integer().optional(),
            "productId": t.string().optional(),
            "offerId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderPromotionItemOut"])
    types["LiaAboutPageSettingsIn"] = t.struct(
        {"status": t.string().optional(), "url": t.string().optional()}
    ).named(renames["LiaAboutPageSettingsIn"])
    types["LiaAboutPageSettingsOut"] = t.struct(
        {
            "status": t.string().optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiaAboutPageSettingsOut"])
    types["RegionalinventoryCustomBatchRequestEntryIn"] = t.struct(
        {
            "regionalInventory": t.proxy(renames["RegionalInventoryIn"]).optional(),
            "method": t.string().optional(),
            "merchantId": t.string().optional(),
            "batchId": t.integer().optional(),
            "productId": t.string().optional(),
        }
    ).named(renames["RegionalinventoryCustomBatchRequestEntryIn"])
    types["RegionalinventoryCustomBatchRequestEntryOut"] = t.struct(
        {
            "regionalInventory": t.proxy(renames["RegionalInventoryOut"]).optional(),
            "method": t.string().optional(),
            "merchantId": t.string().optional(),
            "batchId": t.integer().optional(),
            "productId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegionalinventoryCustomBatchRequestEntryOut"])
    types["DatafeedStatusExampleIn"] = t.struct(
        {
            "value": t.string().optional(),
            "lineNumber": t.string().optional(),
            "itemId": t.string().optional(),
        }
    ).named(renames["DatafeedStatusExampleIn"])
    types["DatafeedStatusExampleOut"] = t.struct(
        {
            "value": t.string().optional(),
            "lineNumber": t.string().optional(),
            "itemId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatafeedStatusExampleOut"])
    types["OrderreturnsLineItemIn"] = t.struct(
        {
            "lineItemId": t.string().optional(),
            "quantity": t.integer().optional(),
            "productId": t.string().optional(),
        }
    ).named(renames["OrderreturnsLineItemIn"])
    types["OrderreturnsLineItemOut"] = t.struct(
        {
            "lineItemId": t.string().optional(),
            "quantity": t.integer().optional(),
            "productId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderreturnsLineItemOut"])
    types["BuyOnGoogleProgramStatusIn"] = t.struct(
        {
            "customerServicePendingEmail": t.string().optional(),
            "customerServicePendingPhoneRegionCode": t.string().optional(),
            "businessModel": t.array(t.string()).optional(),
            "customerServicePendingPhoneNumber": t.string().optional(),
            "onlineSalesChannel": t.string().optional(),
        }
    ).named(renames["BuyOnGoogleProgramStatusIn"])
    types["BuyOnGoogleProgramStatusOut"] = t.struct(
        {
            "customerServicePendingEmail": t.string().optional(),
            "customerServicePendingPhoneRegionCode": t.string().optional(),
            "customerServiceVerifiedEmail": t.string().optional(),
            "businessModel": t.array(t.string()).optional(),
            "participationStage": t.string().optional(),
            "customerServiceVerifiedPhoneNumber": t.string().optional(),
            "customerServiceVerifiedPhoneRegionCode": t.string().optional(),
            "customerServicePendingPhoneNumber": t.string().optional(),
            "onlineSalesChannel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuyOnGoogleProgramStatusOut"])
    types["AccountsCustomBatchResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "entries": t.array(
                t.proxy(renames["AccountsCustomBatchResponseEntryIn"])
            ).optional(),
        }
    ).named(renames["AccountsCustomBatchResponseIn"])
    types["AccountsCustomBatchResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "entries": t.array(
                t.proxy(renames["AccountsCustomBatchResponseEntryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountsCustomBatchResponseOut"])
    types["MonetaryAmountIn"] = t.struct(
        {
            "priceAmount": t.proxy(renames["PriceIn"]).optional(),
            "taxAmount": t.proxy(renames["PriceIn"]).optional(),
        }
    ).named(renames["MonetaryAmountIn"])
    types["MonetaryAmountOut"] = t.struct(
        {
            "priceAmount": t.proxy(renames["PriceOut"]).optional(),
            "taxAmount": t.proxy(renames["PriceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MonetaryAmountOut"])
    types["ListCollectionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "resources": t.array(t.proxy(renames["CollectionIn"])).optional(),
        }
    ).named(renames["ListCollectionsResponseIn"])
    types["ListCollectionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "resources": t.array(t.proxy(renames["CollectionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCollectionsResponseOut"])
    types["ListRegionsResponseIn"] = t.struct(
        {
            "regions": t.array(t.proxy(renames["RegionIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListRegionsResponseIn"])
    types["ListRegionsResponseOut"] = t.struct(
        {
            "regions": t.array(t.proxy(renames["RegionOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListRegionsResponseOut"])
    types["RepricingRuleEffectiveTimeIn"] = t.struct(
        {
            "fixedTimePeriods": t.array(
                t.proxy(renames["RepricingRuleEffectiveTimeFixedTimePeriodIn"])
            ).optional()
        }
    ).named(renames["RepricingRuleEffectiveTimeIn"])
    types["RepricingRuleEffectiveTimeOut"] = t.struct(
        {
            "fixedTimePeriods": t.array(
                t.proxy(renames["RepricingRuleEffectiveTimeFixedTimePeriodOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepricingRuleEffectiveTimeOut"])
    types["DatafeedstatusesListResponseIn"] = t.struct(
        {
            "resources": t.array(t.proxy(renames["DatafeedStatusIn"])),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["DatafeedstatusesListResponseIn"])
    types["DatafeedstatusesListResponseOut"] = t.struct(
        {
            "resources": t.array(t.proxy(renames["DatafeedStatusOut"])),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatafeedstatusesListResponseOut"])
    types["LiasettingsCustomBatchResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "entries": t.array(
                t.proxy(renames["LiasettingsCustomBatchResponseEntryIn"])
            ).optional(),
        }
    ).named(renames["LiasettingsCustomBatchResponseIn"])
    types["LiasettingsCustomBatchResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "entries": t.array(
                t.proxy(renames["LiasettingsCustomBatchResponseEntryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiasettingsCustomBatchResponseOut"])
    types["SearchRequestIn"] = t.struct(
        {
            "query": t.string(),
            "pageSize": t.integer().optional(),
            "pageToken": t.string().optional(),
        }
    ).named(renames["SearchRequestIn"])
    types["SearchRequestOut"] = t.struct(
        {
            "query": t.string(),
            "pageSize": t.integer().optional(),
            "pageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchRequestOut"])
    types["ProductStatusItemLevelIssueIn"] = t.struct(
        {
            "servability": t.string().optional(),
            "destination": t.string().optional(),
            "code": t.string().optional(),
            "applicableCountries": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "documentation": t.string().optional(),
            "detail": t.string().optional(),
            "attributeName": t.string().optional(),
            "resolution": t.string().optional(),
        }
    ).named(renames["ProductStatusItemLevelIssueIn"])
    types["ProductStatusItemLevelIssueOut"] = t.struct(
        {
            "servability": t.string().optional(),
            "destination": t.string().optional(),
            "code": t.string().optional(),
            "applicableCountries": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "documentation": t.string().optional(),
            "detail": t.string().optional(),
            "attributeName": t.string().optional(),
            "resolution": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductStatusItemLevelIssueOut"])
    types["ProductDeliveryTimeIn"] = t.struct(
        {
            "areaDeliveryTimes": t.array(
                t.proxy(renames["ProductDeliveryTimeAreaDeliveryTimeIn"])
            ),
            "productId": t.proxy(renames["ProductIdIn"]),
        }
    ).named(renames["ProductDeliveryTimeIn"])
    types["ProductDeliveryTimeOut"] = t.struct(
        {
            "areaDeliveryTimes": t.array(
                t.proxy(renames["ProductDeliveryTimeAreaDeliveryTimeOut"])
            ),
            "productId": t.proxy(renames["ProductIdOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductDeliveryTimeOut"])
    types["PromotionPromotionStatusDestinationStatusIn"] = t.struct(
        {"status": t.string().optional(), "destination": t.string().optional()}
    ).named(renames["PromotionPromotionStatusDestinationStatusIn"])
    types["PromotionPromotionStatusDestinationStatusOut"] = t.struct(
        {
            "status": t.string().optional(),
            "destination": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PromotionPromotionStatusDestinationStatusOut"])
    types["LocalInventoryIn"] = t.struct(
        {
            "availability": t.string().optional(),
            "price": t.proxy(renames["PriceIn"]).optional(),
            "salePriceEffectiveDate": t.string().optional(),
            "kind": t.string().optional(),
            "instoreProductLocation": t.string().optional(),
            "quantity": t.integer().optional(),
            "customAttributes": t.array(
                t.proxy(renames["CustomAttributeIn"])
            ).optional(),
            "storeCode": t.string(),
            "pickupMethod": t.string().optional(),
            "pickupSla": t.string().optional(),
            "salePrice": t.proxy(renames["PriceIn"]).optional(),
        }
    ).named(renames["LocalInventoryIn"])
    types["LocalInventoryOut"] = t.struct(
        {
            "availability": t.string().optional(),
            "price": t.proxy(renames["PriceOut"]).optional(),
            "salePriceEffectiveDate": t.string().optional(),
            "kind": t.string().optional(),
            "instoreProductLocation": t.string().optional(),
            "quantity": t.integer().optional(),
            "customAttributes": t.array(
                t.proxy(renames["CustomAttributeOut"])
            ).optional(),
            "storeCode": t.string(),
            "pickupMethod": t.string().optional(),
            "pickupSla": t.string().optional(),
            "salePrice": t.proxy(renames["PriceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocalInventoryOut"])
    types["TestOrderLineItemProductIn"] = t.struct(
        {
            "offerId": t.string(),
            "gtin": t.string().optional(),
            "variantAttributes": t.array(
                t.proxy(renames["OrderLineItemProductVariantAttributeIn"])
            ).optional(),
            "fees": t.array(t.proxy(renames["OrderLineItemProductFeeIn"])).optional(),
            "title": t.string(),
            "mpn": t.string().optional(),
            "targetCountry": t.string(),
            "itemGroupId": t.string().optional(),
            "brand": t.string(),
            "imageLink": t.string(),
            "contentLanguage": t.string(),
            "price": t.proxy(renames["PriceIn"]),
            "condition": t.string(),
        }
    ).named(renames["TestOrderLineItemProductIn"])
    types["TestOrderLineItemProductOut"] = t.struct(
        {
            "offerId": t.string(),
            "gtin": t.string().optional(),
            "variantAttributes": t.array(
                t.proxy(renames["OrderLineItemProductVariantAttributeOut"])
            ).optional(),
            "fees": t.array(t.proxy(renames["OrderLineItemProductFeeOut"])).optional(),
            "title": t.string(),
            "mpn": t.string().optional(),
            "targetCountry": t.string(),
            "itemGroupId": t.string().optional(),
            "brand": t.string(),
            "imageLink": t.string(),
            "contentLanguage": t.string(),
            "price": t.proxy(renames["PriceOut"]),
            "condition": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestOrderLineItemProductOut"])
    types["InstallmentIn"] = t.struct(
        {
            "amount": t.proxy(renames["PriceIn"]).optional(),
            "months": t.string().optional(),
        }
    ).named(renames["InstallmentIn"])
    types["InstallmentOut"] = t.struct(
        {
            "amount": t.proxy(renames["PriceOut"]).optional(),
            "months": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstallmentOut"])
    types["LiasettingsRequestInventoryVerificationResponseIn"] = t.struct(
        {"kind": t.string().optional()}
    ).named(renames["LiasettingsRequestInventoryVerificationResponseIn"])
    types["LiasettingsRequestInventoryVerificationResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiasettingsRequestInventoryVerificationResponseOut"])
    types["SettlementReportIn"] = t.struct(
        {
            "transferAmount": t.proxy(renames["PriceIn"]).optional(),
            "transferIds": t.array(t.string()).optional(),
            "previousBalance": t.proxy(renames["PriceIn"]).optional(),
            "settlementId": t.string().optional(),
            "kind": t.string().optional(),
            "transferDate": t.string().optional(),
            "startDate": t.string().optional(),
            "endDate": t.string().optional(),
        }
    ).named(renames["SettlementReportIn"])
    types["SettlementReportOut"] = t.struct(
        {
            "transferAmount": t.proxy(renames["PriceOut"]).optional(),
            "transferIds": t.array(t.string()).optional(),
            "previousBalance": t.proxy(renames["PriceOut"]).optional(),
            "settlementId": t.string().optional(),
            "kind": t.string().optional(),
            "transferDate": t.string().optional(),
            "startDate": t.string().optional(),
            "endDate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SettlementReportOut"])
    types["OrdersCancelRequestIn"] = t.struct(
        {
            "operationId": t.string().optional(),
            "reason": t.string().optional(),
            "reasonText": t.string().optional(),
        }
    ).named(renames["OrdersCancelRequestIn"])
    types["OrdersCancelRequestOut"] = t.struct(
        {
            "operationId": t.string().optional(),
            "reason": t.string().optional(),
            "reasonText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersCancelRequestOut"])
    types["TableIn"] = t.struct(
        {
            "name": t.string().optional(),
            "rows": t.array(t.proxy(renames["RowIn"])).optional(),
            "columnHeaders": t.proxy(renames["HeadersIn"]).optional(),
            "rowHeaders": t.proxy(renames["HeadersIn"]).optional(),
        }
    ).named(renames["TableIn"])
    types["TableOut"] = t.struct(
        {
            "name": t.string().optional(),
            "rows": t.array(t.proxy(renames["RowOut"])).optional(),
            "columnHeaders": t.proxy(renames["HeadersOut"]).optional(),
            "rowHeaders": t.proxy(renames["HeadersOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableOut"])
    types["OrderreturnsCreateOrderReturnResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "orderReturn": t.proxy(renames["MerchantOrderReturnIn"]).optional(),
            "executionStatus": t.string().optional(),
        }
    ).named(renames["OrderreturnsCreateOrderReturnResponseIn"])
    types["OrderreturnsCreateOrderReturnResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "orderReturn": t.proxy(renames["MerchantOrderReturnOut"]).optional(),
            "executionStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderreturnsCreateOrderReturnResponseOut"])
    types["OrderCustomerLoyaltyInfoIn"] = t.struct(
        {"loyaltyNumber": t.string().optional(), "name": t.string().optional()}
    ).named(renames["OrderCustomerLoyaltyInfoIn"])
    types["OrderCustomerLoyaltyInfoOut"] = t.struct(
        {
            "loyaltyNumber": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderCustomerLoyaltyInfoOut"])
    types["ReportInteractionRequestIn"] = t.struct(
        {
            "type": t.string(),
            "responseToken": t.string(),
            "subtype": t.string().optional(),
            "interactionType": t.string(),
        }
    ).named(renames["ReportInteractionRequestIn"])
    types["ReportInteractionRequestOut"] = t.struct(
        {
            "type": t.string(),
            "responseToken": t.string(),
            "subtype": t.string().optional(),
            "interactionType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportInteractionRequestOut"])
    types["RegionalInventoryIn"] = t.struct(
        {
            "customAttributes": t.array(
                t.proxy(renames["CustomAttributeIn"])
            ).optional(),
            "availability": t.string().optional(),
            "price": t.proxy(renames["PriceIn"]).optional(),
            "salePrice": t.proxy(renames["PriceIn"]).optional(),
            "kind": t.string().optional(),
            "regionId": t.string().optional(),
            "salePriceEffectiveDate": t.string().optional(),
        }
    ).named(renames["RegionalInventoryIn"])
    types["RegionalInventoryOut"] = t.struct(
        {
            "customAttributes": t.array(
                t.proxy(renames["CustomAttributeOut"])
            ).optional(),
            "availability": t.string().optional(),
            "price": t.proxy(renames["PriceOut"]).optional(),
            "salePrice": t.proxy(renames["PriceOut"]).optional(),
            "kind": t.string().optional(),
            "regionId": t.string().optional(),
            "salePriceEffectiveDate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegionalInventoryOut"])
    types["LiasettingsCustomBatchResponseEntryIn"] = t.struct(
        {
            "liaSettings": t.proxy(renames["LiaSettingsIn"]).optional(),
            "gmbAccounts": t.proxy(renames["GmbAccountsIn"]).optional(),
            "kind": t.string().optional(),
            "posDataProviders": t.array(
                t.proxy(renames["PosDataProvidersIn"])
            ).optional(),
            "batchId": t.integer().optional(),
            "errors": t.proxy(renames["ErrorsIn"]).optional(),
        }
    ).named(renames["LiasettingsCustomBatchResponseEntryIn"])
    types["LiasettingsCustomBatchResponseEntryOut"] = t.struct(
        {
            "liaSettings": t.proxy(renames["LiaSettingsOut"]).optional(),
            "gmbAccounts": t.proxy(renames["GmbAccountsOut"]).optional(),
            "kind": t.string().optional(),
            "posDataProviders": t.array(
                t.proxy(renames["PosDataProvidersOut"])
            ).optional(),
            "batchId": t.integer().optional(),
            "errors": t.proxy(renames["ErrorsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiasettingsCustomBatchResponseEntryOut"])
    types["OrderreturnsRejectOperationIn"] = t.struct(
        {"reason": t.string().optional(), "reasonText": t.string().optional()}
    ).named(renames["OrderreturnsRejectOperationIn"])
    types["OrderreturnsRejectOperationOut"] = t.struct(
        {
            "reason": t.string().optional(),
            "reasonText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderreturnsRejectOperationOut"])
    types["AccounttaxCustomBatchRequestEntryIn"] = t.struct(
        {
            "accountTax": t.proxy(renames["AccountTaxIn"]).optional(),
            "merchantId": t.string().optional(),
            "method": t.string().optional(),
            "accountId": t.string().optional(),
            "batchId": t.integer().optional(),
        }
    ).named(renames["AccounttaxCustomBatchRequestEntryIn"])
    types["AccounttaxCustomBatchRequestEntryOut"] = t.struct(
        {
            "accountTax": t.proxy(renames["AccountTaxOut"]).optional(),
            "merchantId": t.string().optional(),
            "method": t.string().optional(),
            "accountId": t.string().optional(),
            "batchId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccounttaxCustomBatchRequestEntryOut"])
    types["OrdersCancelTestOrderByCustomerResponseIn"] = t.struct(
        {"kind": t.string().optional()}
    ).named(renames["OrdersCancelTestOrderByCustomerResponseIn"])
    types["OrdersCancelTestOrderByCustomerResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersCancelTestOrderByCustomerResponseOut"])
    types["DatafeedTargetIn"] = t.struct(
        {
            "feedLabel": t.string().optional(),
            "excludedDestinations": t.array(t.string()).optional(),
            "includedDestinations": t.array(t.string()).optional(),
            "language": t.string().optional(),
            "targetCountries": t.array(t.string()).optional(),
            "country": t.string().optional(),
        }
    ).named(renames["DatafeedTargetIn"])
    types["DatafeedTargetOut"] = t.struct(
        {
            "feedLabel": t.string().optional(),
            "excludedDestinations": t.array(t.string()).optional(),
            "includedDestinations": t.array(t.string()).optional(),
            "language": t.string().optional(),
            "targetCountries": t.array(t.string()).optional(),
            "country": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatafeedTargetOut"])
    types["AccountstatusesListResponseIn"] = t.struct(
        {
            "resources": t.array(t.proxy(renames["AccountStatusIn"])),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["AccountstatusesListResponseIn"])
    types["AccountstatusesListResponseOut"] = t.struct(
        {
            "resources": t.array(t.proxy(renames["AccountStatusOut"])),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountstatusesListResponseOut"])
    types["OrderTrackingSignalLineItemDetailsIn"] = t.struct(
        {
            "productTitle": t.string().optional(),
            "productDescription": t.string().optional(),
            "productId": t.string(),
            "gtin": t.string().optional(),
            "upc": t.string().optional(),
            "sku": t.string().optional(),
            "mpn": t.string().optional(),
            "brand": t.string().optional(),
            "quantity": t.string().optional(),
            "lineItemId": t.string(),
        }
    ).named(renames["OrderTrackingSignalLineItemDetailsIn"])
    types["OrderTrackingSignalLineItemDetailsOut"] = t.struct(
        {
            "productTitle": t.string().optional(),
            "productDescription": t.string().optional(),
            "productId": t.string(),
            "gtin": t.string().optional(),
            "upc": t.string().optional(),
            "sku": t.string().optional(),
            "mpn": t.string().optional(),
            "brand": t.string().optional(),
            "quantity": t.string().optional(),
            "lineItemId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderTrackingSignalLineItemDetailsOut"])
    types["RepricingRuleRestrictionIn"] = t.struct(
        {
            "useAutoPricingMinPrice": t.boolean().optional(),
            "floor": t.proxy(renames["RepricingRuleRestrictionBoundaryIn"]).optional(),
        }
    ).named(renames["RepricingRuleRestrictionIn"])
    types["RepricingRuleRestrictionOut"] = t.struct(
        {
            "useAutoPricingMinPrice": t.boolean().optional(),
            "floor": t.proxy(renames["RepricingRuleRestrictionBoundaryOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepricingRuleRestrictionOut"])
    types["ReturnaddressListResponseIn"] = t.struct(
        {
            "resources": t.array(t.proxy(renames["ReturnAddressIn"])),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ReturnaddressListResponseIn"])
    types["ReturnaddressListResponseOut"] = t.struct(
        {
            "resources": t.array(t.proxy(renames["ReturnAddressOut"])),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReturnaddressListResponseOut"])
    types["RequestPhoneVerificationRequestIn"] = t.struct(
        {
            "phoneNumber": t.string().optional(),
            "languageCode": t.string().optional(),
            "phoneRegionCode": t.string(),
            "phoneVerificationMethod": t.string().optional(),
        }
    ).named(renames["RequestPhoneVerificationRequestIn"])
    types["RequestPhoneVerificationRequestOut"] = t.struct(
        {
            "phoneNumber": t.string().optional(),
            "languageCode": t.string().optional(),
            "phoneRegionCode": t.string(),
            "phoneVerificationMethod": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestPhoneVerificationRequestOut"])
    types["ReturnaddressCustomBatchRequestEntryIn"] = t.struct(
        {
            "merchantId": t.string().optional(),
            "returnAddressId": t.string().optional(),
            "returnAddress": t.proxy(renames["ReturnAddressIn"]).optional(),
            "batchId": t.integer().optional(),
            "method": t.string().optional(),
        }
    ).named(renames["ReturnaddressCustomBatchRequestEntryIn"])
    types["ReturnaddressCustomBatchRequestEntryOut"] = t.struct(
        {
            "merchantId": t.string().optional(),
            "returnAddressId": t.string().optional(),
            "returnAddress": t.proxy(renames["ReturnAddressOut"]).optional(),
            "batchId": t.integer().optional(),
            "method": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReturnaddressCustomBatchRequestEntryOut"])
    types["LiaPosDataProviderIn"] = t.struct(
        {
            "posDataProviderId": t.string().optional(),
            "posExternalAccountId": t.string().optional(),
        }
    ).named(renames["LiaPosDataProviderIn"])
    types["LiaPosDataProviderOut"] = t.struct(
        {
            "posDataProviderId": t.string().optional(),
            "posExternalAccountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiaPosDataProviderOut"])
    types["ProductstatusesListResponseIn"] = t.struct(
        {
            "resources": t.array(t.proxy(renames["ProductStatusIn"])),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ProductstatusesListResponseIn"])
    types["ProductstatusesListResponseOut"] = t.struct(
        {
            "resources": t.array(t.proxy(renames["ProductStatusOut"])),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductstatusesListResponseOut"])
    types["ListAccountReturnCarrierResponseIn"] = t.struct(
        {
            "accountReturnCarriers": t.array(
                t.proxy(renames["AccountReturnCarrierIn"])
            ).optional()
        }
    ).named(renames["ListAccountReturnCarrierResponseIn"])
    types["ListAccountReturnCarrierResponseOut"] = t.struct(
        {
            "accountReturnCarriers": t.array(
                t.proxy(renames["AccountReturnCarrierOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAccountReturnCarrierResponseOut"])
    types["OrderinvoicesCreateChargeInvoiceResponseIn"] = t.struct(
        {"executionStatus": t.string().optional(), "kind": t.string().optional()}
    ).named(renames["OrderinvoicesCreateChargeInvoiceResponseIn"])
    types["OrderinvoicesCreateChargeInvoiceResponseOut"] = t.struct(
        {
            "executionStatus": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderinvoicesCreateChargeInvoiceResponseOut"])
    types["AmountIn"] = t.struct(
        {
            "taxAmount": t.proxy(renames["PriceIn"]).optional(),
            "priceAmount": t.proxy(renames["PriceIn"]).optional(),
        }
    ).named(renames["AmountIn"])
    types["AmountOut"] = t.struct(
        {
            "taxAmount": t.proxy(renames["PriceOut"]).optional(),
            "priceAmount": t.proxy(renames["PriceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AmountOut"])
    types["MerchantOrderReturnItemIn"] = t.struct(
        {
            "refundableAmount": t.proxy(renames["MonetaryAmountIn"]).optional(),
            "returnShipmentIds": t.array(t.string()).optional(),
            "state": t.string().optional(),
            "itemId": t.string().optional(),
            "merchantReturnReason": t.proxy(renames["RefundReasonIn"]).optional(),
            "returnItemId": t.string().optional(),
            "product": t.proxy(renames["OrderLineItemProductIn"]).optional(),
            "shipmentUnitId": t.string().optional(),
            "customerReturnReason": t.proxy(
                renames["CustomerReturnReasonIn"]
            ).optional(),
            "merchantRejectionReason": t.proxy(
                renames["MerchantRejectionReasonIn"]
            ).optional(),
            "shipmentGroupId": t.string().optional(),
        }
    ).named(renames["MerchantOrderReturnItemIn"])
    types["MerchantOrderReturnItemOut"] = t.struct(
        {
            "refundableAmount": t.proxy(renames["MonetaryAmountOut"]).optional(),
            "returnShipmentIds": t.array(t.string()).optional(),
            "state": t.string().optional(),
            "itemId": t.string().optional(),
            "merchantReturnReason": t.proxy(renames["RefundReasonOut"]).optional(),
            "returnItemId": t.string().optional(),
            "product": t.proxy(renames["OrderLineItemProductOut"]).optional(),
            "shipmentUnitId": t.string().optional(),
            "customerReturnReason": t.proxy(
                renames["CustomerReturnReasonOut"]
            ).optional(),
            "merchantRejectionReason": t.proxy(
                renames["MerchantRejectionReasonOut"]
            ).optional(),
            "shipmentGroupId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MerchantOrderReturnItemOut"])
    types["LiasettingsListPosDataProvidersResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "posDataProviders": t.array(
                t.proxy(renames["PosDataProvidersIn"])
            ).optional(),
        }
    ).named(renames["LiasettingsListPosDataProvidersResponseIn"])
    types["LiasettingsListPosDataProvidersResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "posDataProviders": t.array(
                t.proxy(renames["PosDataProvidersOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiasettingsListPosDataProvidersResponseOut"])
    types["DateIn"] = t.struct(
        {
            "year": t.integer().optional(),
            "day": t.integer().optional(),
            "month": t.integer().optional(),
        }
    ).named(renames["DateIn"])
    types["DateOut"] = t.struct(
        {
            "year": t.integer().optional(),
            "day": t.integer().optional(),
            "month": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
    types["OrderMerchantProvidedAnnotationIn"] = t.struct(
        {"key": t.string().optional(), "value": t.string().optional()}
    ).named(renames["OrderMerchantProvidedAnnotationIn"])
    types["OrderMerchantProvidedAnnotationOut"] = t.struct(
        {
            "key": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderMerchantProvidedAnnotationOut"])
    types["OrderLineItemShippingDetailsMethodIn"] = t.struct(
        {
            "maxDaysInTransit": t.integer(),
            "minDaysInTransit": t.integer(),
            "methodName": t.string(),
            "carrier": t.string().optional(),
        }
    ).named(renames["OrderLineItemShippingDetailsMethodIn"])
    types["OrderLineItemShippingDetailsMethodOut"] = t.struct(
        {
            "maxDaysInTransit": t.integer(),
            "minDaysInTransit": t.integer(),
            "methodName": t.string(),
            "carrier": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderLineItemShippingDetailsMethodOut"])
    types["ProductShippingDimensionIn"] = t.struct(
        {"value": t.number().optional(), "unit": t.string().optional()}
    ).named(renames["ProductShippingDimensionIn"])
    types["ProductShippingDimensionOut"] = t.struct(
        {
            "value": t.number().optional(),
            "unit": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductShippingDimensionOut"])
    types["TransitTableTransitTimeRowTransitTimeValueIn"] = t.struct(
        {
            "maxTransitTimeInDays": t.integer().optional(),
            "minTransitTimeInDays": t.integer().optional(),
        }
    ).named(renames["TransitTableTransitTimeRowTransitTimeValueIn"])
    types["TransitTableTransitTimeRowTransitTimeValueOut"] = t.struct(
        {
            "maxTransitTimeInDays": t.integer().optional(),
            "minTransitTimeInDays": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransitTableTransitTimeRowTransitTimeValueOut"])
    types["OrdersCustomBatchRequestEntryRefundItemShippingIn"] = t.struct(
        {
            "fullRefund": t.boolean().optional(),
            "amount": t.proxy(renames["PriceIn"]).optional(),
        }
    ).named(renames["OrdersCustomBatchRequestEntryRefundItemShippingIn"])
    types["OrdersCustomBatchRequestEntryRefundItemShippingOut"] = t.struct(
        {
            "fullRefund": t.boolean().optional(),
            "amount": t.proxy(renames["PriceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersCustomBatchRequestEntryRefundItemShippingOut"])
    types["OrdersShipLineItemsRequestIn"] = t.struct(
        {
            "shipmentInfos": t.array(
                t.proxy(
                    renames["OrdersCustomBatchRequestEntryShipLineItemsShipmentInfoIn"]
                )
            ).optional(),
            "operationId": t.string().optional(),
            "lineItems": t.array(
                t.proxy(renames["OrderShipmentLineItemShipmentIn"])
            ).optional(),
            "shipmentGroupId": t.string().optional(),
        }
    ).named(renames["OrdersShipLineItemsRequestIn"])
    types["OrdersShipLineItemsRequestOut"] = t.struct(
        {
            "shipmentInfos": t.array(
                t.proxy(
                    renames["OrdersCustomBatchRequestEntryShipLineItemsShipmentInfoOut"]
                )
            ).optional(),
            "operationId": t.string().optional(),
            "lineItems": t.array(
                t.proxy(renames["OrderShipmentLineItemShipmentOut"])
            ).optional(),
            "shipmentGroupId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersShipLineItemsRequestOut"])
    types["RegionalinventoryCustomBatchResponseIn"] = t.struct(
        {
            "entries": t.array(
                t.proxy(renames["RegionalinventoryCustomBatchResponseEntryIn"])
            ).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["RegionalinventoryCustomBatchResponseIn"])
    types["RegionalinventoryCustomBatchResponseOut"] = t.struct(
        {
            "entries": t.array(
                t.proxy(renames["RegionalinventoryCustomBatchResponseEntryOut"])
            ).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegionalinventoryCustomBatchResponseOut"])
    types["TestOrderIn"] = t.struct(
        {
            "notificationMode": t.string().optional(),
            "enableOrderinvoices": t.boolean().optional(),
            "promotions": t.array(t.proxy(renames["OrderPromotionIn"])).optional(),
            "predefinedPickupDetails": t.string().optional(),
            "deliveryDetails": t.proxy(
                renames["TestOrderDeliveryDetailsIn"]
            ).optional(),
            "shippingCost": t.proxy(renames["PriceIn"]),
            "predefinedBillingAddress": t.string(),
            "lineItems": t.array(t.proxy(renames["TestOrderLineItemIn"])),
            "shippingOption": t.string(),
            "kind": t.string().optional(),
            "predefinedEmail": t.string(),
            "pickupDetails": t.proxy(renames["TestOrderPickupDetailsIn"]).optional(),
            "predefinedDeliveryAddress": t.string(),
        }
    ).named(renames["TestOrderIn"])
    types["TestOrderOut"] = t.struct(
        {
            "notificationMode": t.string().optional(),
            "enableOrderinvoices": t.boolean().optional(),
            "promotions": t.array(t.proxy(renames["OrderPromotionOut"])).optional(),
            "predefinedPickupDetails": t.string().optional(),
            "deliveryDetails": t.proxy(
                renames["TestOrderDeliveryDetailsOut"]
            ).optional(),
            "shippingCost": t.proxy(renames["PriceOut"]),
            "predefinedBillingAddress": t.string(),
            "lineItems": t.array(t.proxy(renames["TestOrderLineItemOut"])),
            "shippingOption": t.string(),
            "kind": t.string().optional(),
            "predefinedEmail": t.string(),
            "pickupDetails": t.proxy(renames["TestOrderPickupDetailsOut"]).optional(),
            "predefinedDeliveryAddress": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestOrderOut"])
    types["ProductSubscriptionCostIn"] = t.struct(
        {
            "period": t.string().optional(),
            "periodLength": t.string().optional(),
            "amount": t.proxy(renames["PriceIn"]).optional(),
        }
    ).named(renames["ProductSubscriptionCostIn"])
    types["ProductSubscriptionCostOut"] = t.struct(
        {
            "period": t.string().optional(),
            "periodLength": t.string().optional(),
            "amount": t.proxy(renames["PriceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductSubscriptionCostOut"])
    types["PriceInsightsIn"] = t.struct(
        {
            "predictedClicksChangeFraction": t.number().optional(),
            "predictedConversionsChangeFraction": t.number().optional(),
            "predictedMonthlyGrossProfitChangeMicros": t.string().optional(),
            "predictedGrossProfitChangeFraction": t.number().optional(),
            "suggestedPriceCurrencyCode": t.string().optional(),
            "predictedImpressionsChangeFraction": t.number().optional(),
            "predictedMonthlyGrossProfitChangeCurrencyCode": t.string().optional(),
            "suggestedPriceMicros": t.string().optional(),
        }
    ).named(renames["PriceInsightsIn"])
    types["PriceInsightsOut"] = t.struct(
        {
            "predictedClicksChangeFraction": t.number().optional(),
            "predictedConversionsChangeFraction": t.number().optional(),
            "predictedMonthlyGrossProfitChangeMicros": t.string().optional(),
            "predictedGrossProfitChangeFraction": t.number().optional(),
            "suggestedPriceCurrencyCode": t.string().optional(),
            "predictedImpressionsChangeFraction": t.number().optional(),
            "predictedMonthlyGrossProfitChangeCurrencyCode": t.string().optional(),
            "suggestedPriceMicros": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PriceInsightsOut"])
    types["TestOrderAddressIn"] = t.struct(
        {
            "fullAddress": t.array(t.string()).optional(),
            "country": t.string().optional(),
            "region": t.string().optional(),
            "locality": t.string().optional(),
            "streetAddress": t.array(t.string()).optional(),
            "recipientName": t.string().optional(),
            "postalCode": t.string().optional(),
            "isPostOfficeBox": t.boolean().optional(),
        }
    ).named(renames["TestOrderAddressIn"])
    types["TestOrderAddressOut"] = t.struct(
        {
            "fullAddress": t.array(t.string()).optional(),
            "country": t.string().optional(),
            "region": t.string().optional(),
            "locality": t.string().optional(),
            "streetAddress": t.array(t.string()).optional(),
            "recipientName": t.string().optional(),
            "postalCode": t.string().optional(),
            "isPostOfficeBox": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestOrderAddressOut"])
    types["RowIn"] = t.struct(
        {"cells": t.array(t.proxy(renames["ValueIn"])).optional()}
    ).named(renames["RowIn"])
    types["RowOut"] = t.struct(
        {
            "cells": t.array(t.proxy(renames["ValueOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RowOut"])
    types["GoogleAnalyticsLinkIn"] = t.struct({"propertyId": t.string()}).named(
        renames["GoogleAnalyticsLinkIn"]
    )
    types["GoogleAnalyticsLinkOut"] = t.struct(
        {
            "propertyId": t.string(),
            "attributionSettings": t.proxy(
                renames["AttributionSettingsOut"]
            ).optional(),
            "propertyName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsLinkOut"])
    types["SettlementTransactionIn"] = t.struct(
        {
            "identifiers": t.proxy(
                renames["SettlementTransactionIdentifiersIn"]
            ).optional(),
            "transaction": t.proxy(
                renames["SettlementTransactionTransactionIn"]
            ).optional(),
            "amount": t.proxy(renames["SettlementTransactionAmountIn"]).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["SettlementTransactionIn"])
    types["SettlementTransactionOut"] = t.struct(
        {
            "identifiers": t.proxy(
                renames["SettlementTransactionIdentifiersOut"]
            ).optional(),
            "transaction": t.proxy(
                renames["SettlementTransactionTransactionOut"]
            ).optional(),
            "amount": t.proxy(renames["SettlementTransactionAmountOut"]).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SettlementTransactionOut"])
    types["ListRepricingProductReportsResponseIn"] = t.struct(
        {
            "repricingProductReports": t.array(
                t.proxy(renames["RepricingProductReportIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListRepricingProductReportsResponseIn"])
    types["ListRepricingProductReportsResponseOut"] = t.struct(
        {
            "repricingProductReports": t.array(
                t.proxy(renames["RepricingProductReportOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListRepricingProductReportsResponseOut"])
    types["OrderPickupDetailsCollectorIn"] = t.struct(
        {"phoneNumber": t.string().optional(), "name": t.string().optional()}
    ).named(renames["OrderPickupDetailsCollectorIn"])
    types["OrderPickupDetailsCollectorOut"] = t.struct(
        {
            "phoneNumber": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderPickupDetailsCollectorOut"])
    types["SettlementreportsListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "resources": t.array(t.proxy(renames["SettlementReportIn"])),
        }
    ).named(renames["SettlementreportsListResponseIn"])
    types["SettlementreportsListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "resources": t.array(t.proxy(renames["SettlementReportOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SettlementreportsListResponseOut"])

    functions = {}
    functions["repricingrulesDelete"] = content.get(
        "{merchantId}/repricingrules",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "merchantId": t.string(),
                "countryCode": t.string().optional(),
                "languageCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListRepricingRulesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["repricingrulesPatch"] = content.get(
        "{merchantId}/repricingrules",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "merchantId": t.string(),
                "countryCode": t.string().optional(),
                "languageCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListRepricingRulesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["repricingrulesCreate"] = content.get(
        "{merchantId}/repricingrules",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "merchantId": t.string(),
                "countryCode": t.string().optional(),
                "languageCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListRepricingRulesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["repricingrulesGet"] = content.get(
        "{merchantId}/repricingrules",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "merchantId": t.string(),
                "countryCode": t.string().optional(),
                "languageCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListRepricingRulesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["repricingrulesList"] = content.get(
        "{merchantId}/repricingrules",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "merchantId": t.string(),
                "countryCode": t.string().optional(),
                "languageCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListRepricingRulesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["repricingrulesRepricingreportsList"] = content.get(
        "{merchantId}/repricingrules/{ruleId}/repricingreports",
        t.struct(
            {
                "ruleId": t.string(),
                "endDate": t.string().optional(),
                "pageToken": t.string().optional(),
                "startDate": t.string().optional(),
                "merchantId": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListRepricingRuleReportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["recommendationsGenerate"] = content.post(
        "{merchantId}/recommendations/reportInteraction",
        t.struct(
            {
                "merchantId": t.string(),
                "type": t.string(),
                "responseToken": t.string(),
                "subtype": t.string().optional(),
                "interactionType": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["recommendationsReportInteraction"] = content.post(
        "{merchantId}/recommendations/reportInteraction",
        t.struct(
            {
                "merchantId": t.string(),
                "type": t.string(),
                "responseToken": t.string(),
                "subtype": t.string().optional(),
                "interactionType": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["ordertrackingsignalsCreate"] = content.post(
        "{merchantId}/ordertrackingsignals",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "shippingInfo": t.array(
                    t.proxy(renames["OrderTrackingSignalShippingInfoIn"])
                ).optional(),
                "lineItems": t.array(
                    t.proxy(renames["OrderTrackingSignalLineItemDetailsIn"])
                ).optional(),
                "orderCreatedTime": t.proxy(renames["DateTimeIn"]),
                "customerShippingFee": t.proxy(renames["PriceAmountIn"]).optional(),
                "deliveryRegionCode": t.string(),
                "shipmentLineItemMapping": t.array(
                    t.proxy(renames["OrderTrackingSignalShipmentLineItemMappingIn"])
                ).optional(),
                "orderId": t.string(),
                "deliveryPostalCode": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrderTrackingSignalOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["orderinvoicesCreaterefundinvoice"] = content.post(
        "{merchantId}/orderinvoices/{orderId}/createChargeInvoice",
        t.struct(
            {
                "orderId": t.string().optional(),
                "merchantId": t.string().optional(),
                "operationId": t.string().optional(),
                "invoiceSummary": t.proxy(renames["InvoiceSummaryIn"]).optional(),
                "lineItemInvoices": t.array(
                    t.proxy(renames["ShipmentInvoiceLineItemInvoiceIn"])
                ).optional(),
                "shipmentGroupId": t.string().optional(),
                "invoiceId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrderinvoicesCreateChargeInvoiceResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["orderinvoicesCreatechargeinvoice"] = content.post(
        "{merchantId}/orderinvoices/{orderId}/createChargeInvoice",
        t.struct(
            {
                "orderId": t.string().optional(),
                "merchantId": t.string().optional(),
                "operationId": t.string().optional(),
                "invoiceSummary": t.proxy(renames["InvoiceSummaryIn"]).optional(),
                "lineItemInvoices": t.array(
                    t.proxy(renames["ShipmentInvoiceLineItemInvoiceIn"])
                ).optional(),
                "shipmentGroupId": t.string().optional(),
                "invoiceId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrderinvoicesCreateChargeInvoiceResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settlementtransactionsList"] = content.get(
        "{merchantId}/settlementreports/{settlementId}/transactions",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "settlementId": t.string().optional(),
                "transactionIds": t.string().optional(),
                "pageToken": t.string().optional(),
                "merchantId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SettlementtransactionsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["regionalinventoryCustombatch"] = content.post(
        "{merchantId}/products/{productId}/regionalinventory",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "productId": t.string().optional(),
                "customAttributes": t.array(
                    t.proxy(renames["CustomAttributeIn"])
                ).optional(),
                "availability": t.string().optional(),
                "price": t.proxy(renames["PriceIn"]).optional(),
                "salePrice": t.proxy(renames["PriceIn"]).optional(),
                "kind": t.string().optional(),
                "regionId": t.string().optional(),
                "salePriceEffectiveDate": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RegionalInventoryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["regionalinventoryInsert"] = content.post(
        "{merchantId}/products/{productId}/regionalinventory",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "productId": t.string().optional(),
                "customAttributes": t.array(
                    t.proxy(renames["CustomAttributeIn"])
                ).optional(),
                "availability": t.string().optional(),
                "price": t.proxy(renames["PriceIn"]).optional(),
                "salePrice": t.proxy(renames["PriceIn"]).optional(),
                "kind": t.string().optional(),
                "regionId": t.string().optional(),
                "salePriceEffectiveDate": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RegionalInventoryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["quotasList"] = content.get(
        "{merchantId}/quotas",
        t.struct(
            {
                "merchantId": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMethodQuotasResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsListlinks"] = content.post(
        "{merchantId}/accounts/{accountId}/claimwebsite",
        t.struct(
            {
                "accountId": t.string().optional(),
                "overwrite": t.boolean().optional(),
                "merchantId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountsClaimWebsiteResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsDelete"] = content.post(
        "{merchantId}/accounts/{accountId}/claimwebsite",
        t.struct(
            {
                "accountId": t.string().optional(),
                "overwrite": t.boolean().optional(),
                "merchantId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountsClaimWebsiteResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsUpdate"] = content.post(
        "{merchantId}/accounts/{accountId}/claimwebsite",
        t.struct(
            {
                "accountId": t.string().optional(),
                "overwrite": t.boolean().optional(),
                "merchantId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountsClaimWebsiteResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsRequestphoneverification"] = content.post(
        "{merchantId}/accounts/{accountId}/claimwebsite",
        t.struct(
            {
                "accountId": t.string().optional(),
                "overwrite": t.boolean().optional(),
                "merchantId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountsClaimWebsiteResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAuthinfo"] = content.post(
        "{merchantId}/accounts/{accountId}/claimwebsite",
        t.struct(
            {
                "accountId": t.string().optional(),
                "overwrite": t.boolean().optional(),
                "merchantId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountsClaimWebsiteResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsLink"] = content.post(
        "{merchantId}/accounts/{accountId}/claimwebsite",
        t.struct(
            {
                "accountId": t.string().optional(),
                "overwrite": t.boolean().optional(),
                "merchantId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountsClaimWebsiteResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsInsert"] = content.post(
        "{merchantId}/accounts/{accountId}/claimwebsite",
        t.struct(
            {
                "accountId": t.string().optional(),
                "overwrite": t.boolean().optional(),
                "merchantId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountsClaimWebsiteResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsUpdatelabels"] = content.post(
        "{merchantId}/accounts/{accountId}/claimwebsite",
        t.struct(
            {
                "accountId": t.string().optional(),
                "overwrite": t.boolean().optional(),
                "merchantId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountsClaimWebsiteResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsList"] = content.post(
        "{merchantId}/accounts/{accountId}/claimwebsite",
        t.struct(
            {
                "accountId": t.string().optional(),
                "overwrite": t.boolean().optional(),
                "merchantId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountsClaimWebsiteResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsVerifyphonenumber"] = content.post(
        "{merchantId}/accounts/{accountId}/claimwebsite",
        t.struct(
            {
                "accountId": t.string().optional(),
                "overwrite": t.boolean().optional(),
                "merchantId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountsClaimWebsiteResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsGet"] = content.post(
        "{merchantId}/accounts/{accountId}/claimwebsite",
        t.struct(
            {
                "accountId": t.string().optional(),
                "overwrite": t.boolean().optional(),
                "merchantId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountsClaimWebsiteResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCustombatch"] = content.post(
        "{merchantId}/accounts/{accountId}/claimwebsite",
        t.struct(
            {
                "accountId": t.string().optional(),
                "overwrite": t.boolean().optional(),
                "merchantId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountsClaimWebsiteResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsClaimwebsite"] = content.post(
        "{merchantId}/accounts/{accountId}/claimwebsite",
        t.struct(
            {
                "accountId": t.string().optional(),
                "overwrite": t.boolean().optional(),
                "merchantId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountsClaimWebsiteResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsLabelsDelete"] = content.post(
        "accounts/{accountId}/labels",
        t.struct(
            {
                "accountId": t.string().optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountLabelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsLabelsPatch"] = content.post(
        "accounts/{accountId}/labels",
        t.struct(
            {
                "accountId": t.string().optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountLabelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsLabelsList"] = content.post(
        "accounts/{accountId}/labels",
        t.struct(
            {
                "accountId": t.string().optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountLabelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsLabelsCreate"] = content.post(
        "accounts/{accountId}/labels",
        t.struct(
            {
                "accountId": t.string().optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountLabelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsReturncarrierPatch"] = content.get(
        "accounts/{accountId}/returncarrier",
        t.struct({"accountId": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ListAccountReturnCarrierResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsReturncarrierDelete"] = content.get(
        "accounts/{accountId}/returncarrier",
        t.struct({"accountId": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ListAccountReturnCarrierResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsReturncarrierCreate"] = content.get(
        "accounts/{accountId}/returncarrier",
        t.struct({"accountId": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ListAccountReturnCarrierResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsReturncarrierList"] = content.get(
        "accounts/{accountId}/returncarrier",
        t.struct({"accountId": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ListAccountReturnCarrierResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCredentialsCreate"] = content.post(
        "accounts/{accountId}/credentials",
        t.struct(
            {
                "accountId": t.string(),
                "expiresIn": t.string().optional(),
                "accessToken": t.string().optional(),
                "purpose": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountCredentialsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["returnaddressInsert"] = content.post(
        "returnaddress/batch",
        t.struct(
            {
                "entries": t.array(
                    t.proxy(renames["ReturnaddressCustomBatchRequestEntryIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReturnaddressCustomBatchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["returnaddressDelete"] = content.post(
        "returnaddress/batch",
        t.struct(
            {
                "entries": t.array(
                    t.proxy(renames["ReturnaddressCustomBatchRequestEntryIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReturnaddressCustomBatchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["returnaddressGet"] = content.post(
        "returnaddress/batch",
        t.struct(
            {
                "entries": t.array(
                    t.proxy(renames["ReturnaddressCustomBatchRequestEntryIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReturnaddressCustomBatchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["returnaddressList"] = content.post(
        "returnaddress/batch",
        t.struct(
            {
                "entries": t.array(
                    t.proxy(renames["ReturnaddressCustomBatchRequestEntryIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReturnaddressCustomBatchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["returnaddressCustombatch"] = content.post(
        "returnaddress/batch",
        t.struct(
            {
                "entries": t.array(
                    t.proxy(renames["ReturnaddressCustomBatchRequestEntryIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReturnaddressCustomBatchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accounttaxGet"] = content.put(
        "{merchantId}/accounttax/{accountId}",
        t.struct(
            {
                "accountId": t.string(),
                "merchantId": t.string().optional(),
                "kind": t.string().optional(),
                "rules": t.array(t.proxy(renames["AccountTaxTaxRuleIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountTaxOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accounttaxList"] = content.put(
        "{merchantId}/accounttax/{accountId}",
        t.struct(
            {
                "accountId": t.string(),
                "merchantId": t.string().optional(),
                "kind": t.string().optional(),
                "rules": t.array(t.proxy(renames["AccountTaxTaxRuleIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountTaxOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accounttaxCustombatch"] = content.put(
        "{merchantId}/accounttax/{accountId}",
        t.struct(
            {
                "accountId": t.string(),
                "merchantId": t.string().optional(),
                "kind": t.string().optional(),
                "rules": t.array(t.proxy(renames["AccountTaxTaxRuleIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountTaxOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accounttaxUpdate"] = content.put(
        "{merchantId}/accounttax/{accountId}",
        t.struct(
            {
                "accountId": t.string(),
                "merchantId": t.string().optional(),
                "kind": t.string().optional(),
                "rules": t.array(t.proxy(renames["AccountTaxTaxRuleIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountTaxOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["productsList"] = content.post(
        "{merchantId}/products",
        t.struct(
            {
                "feedId": t.string().optional(),
                "merchantId": t.string().optional(),
                "sellOnGoogleQuantity": t.string().optional(),
                "taxCategory": t.string().optional(),
                "mpn": t.string().optional(),
                "gtin": t.string().optional(),
                "availabilityDate": t.string().optional(),
                "gender": t.string().optional(),
                "itemGroupId": t.string().optional(),
                "excludedDestinations": t.array(t.string()).optional(),
                "shoppingAdsExcludedCountries": t.array(t.string()).optional(),
                "availability": t.string().optional(),
                "shippingLength": t.proxy(
                    renames["ProductShippingDimensionIn"]
                ).optional(),
                "sizeType": t.string().optional(),
                "ageGroup": t.string().optional(),
                "productTypes": t.array(t.string()).optional(),
                "displayAdsSimilarIds": t.array(t.string()).optional(),
                "customLabel1": t.string().optional(),
                "minHandlingTime": t.string().optional(),
                "transitTimeLabel": t.string().optional(),
                "externalSellerId": t.string(),
                "additionalSizeType": t.string().optional(),
                "productWeight": t.proxy(renames["ProductWeightIn"]).optional(),
                "pickupSla": t.string().optional(),
                "shippingWeight": t.proxy(
                    renames["ProductShippingWeightIn"]
                ).optional(),
                "title": t.string().optional(),
                "promotionIds": t.array(t.string()).optional(),
                "energyEfficiencyClass": t.string().optional(),
                "productHighlights": t.array(t.string()).optional(),
                "installment": t.proxy(renames["InstallmentIn"]).optional(),
                "multipack": t.string().optional(),
                "lifestyleImageLinks": t.array(t.string()).optional(),
                "link": t.string().optional(),
                "color": t.string().optional(),
                "brand": t.string().optional(),
                "additionalImageLinks": t.array(t.string()).optional(),
                "unitPricingMeasure": t.proxy(
                    renames["ProductUnitPricingMeasureIn"]
                ).optional(),
                "identifierExists": t.boolean().optional(),
                "source": t.string().optional(),
                "productWidth": t.proxy(renames["ProductDimensionIn"]).optional(),
                "loyaltyPoints": t.proxy(renames["LoyaltyPointsIn"]).optional(),
                "productHeight": t.proxy(renames["ProductDimensionIn"]).optional(),
                "linkTemplate": t.string().optional(),
                "certifications": t.array(
                    t.proxy(renames["ProductCertificationIn"])
                ).optional(),
                "isBundle": t.boolean().optional(),
                "productDetails": t.array(
                    t.proxy(renames["ProductProductDetailIn"])
                ).optional(),
                "mobileLink": t.string().optional(),
                "pickupMethod": t.string().optional(),
                "googleProductCategory": t.string().optional(),
                "displayAdsTitle": t.string().optional(),
                "minEnergyEfficiencyClass": t.string().optional(),
                "price": t.proxy(renames["PriceIn"]).optional(),
                "shipping": t.array(t.proxy(renames["ProductShippingIn"])).optional(),
                "shippingWidth": t.proxy(
                    renames["ProductShippingDimensionIn"]
                ).optional(),
                "customLabel0": t.string().optional(),
                "adsLabels": t.array(t.string()).optional(),
                "description": t.string().optional(),
                "adsRedirect": t.string().optional(),
                "shippingLabel": t.string().optional(),
                "canonicalLink": t.string().optional(),
                "condition": t.string().optional(),
                "productLength": t.proxy(renames["ProductDimensionIn"]).optional(),
                "offerId": t.string(),
                "adult": t.boolean().optional(),
                "material": t.string().optional(),
                "displayAdsId": t.string().optional(),
                "includedDestinations": t.array(t.string()).optional(),
                "contentLanguage": t.string(),
                "adsGrouping": t.string().optional(),
                "cloudExportAdditionalProperties": t.array(
                    t.proxy(renames["CloudExportAdditionalPropertiesIn"])
                ).optional(),
                "displayAdsLink": t.string().optional(),
                "maxHandlingTime": t.string().optional(),
                "sizeSystem": t.string().optional(),
                "subscriptionCost": t.proxy(
                    renames["ProductSubscriptionCostIn"]
                ).optional(),
                "salePriceEffectiveDate": t.string().optional(),
                "feedLabel": t.string().optional(),
                "disclosureDate": t.string().optional(),
                "taxes": t.array(t.proxy(renames["ProductTaxIn"])).optional(),
                "channel": t.string(),
                "customLabel4": t.string().optional(),
                "sizes": t.array(t.string()).optional(),
                "displayAdsValue": t.number().optional(),
                "costOfGoodsSold": t.proxy(renames["PriceIn"]).optional(),
                "mobileLinkTemplate": t.string().optional(),
                "targetCountry": t.string(),
                "salePrice": t.proxy(renames["PriceIn"]).optional(),
                "imageLink": t.string().optional(),
                "unitPricingBaseMeasure": t.proxy(
                    renames["ProductUnitPricingBaseMeasureIn"]
                ).optional(),
                "kind": t.string().optional(),
                "id": t.string().optional(),
                "maxEnergyEfficiencyClass": t.string().optional(),
                "pattern": t.string().optional(),
                "customAttributes": t.array(
                    t.proxy(renames["CustomAttributeIn"])
                ).optional(),
                "customLabel2": t.string().optional(),
                "shippingHeight": t.proxy(
                    renames["ProductShippingDimensionIn"]
                ).optional(),
                "customLabel3": t.string().optional(),
                "expirationDate": t.string().optional(),
                "pause": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["productsUpdate"] = content.post(
        "{merchantId}/products",
        t.struct(
            {
                "feedId": t.string().optional(),
                "merchantId": t.string().optional(),
                "sellOnGoogleQuantity": t.string().optional(),
                "taxCategory": t.string().optional(),
                "mpn": t.string().optional(),
                "gtin": t.string().optional(),
                "availabilityDate": t.string().optional(),
                "gender": t.string().optional(),
                "itemGroupId": t.string().optional(),
                "excludedDestinations": t.array(t.string()).optional(),
                "shoppingAdsExcludedCountries": t.array(t.string()).optional(),
                "availability": t.string().optional(),
                "shippingLength": t.proxy(
                    renames["ProductShippingDimensionIn"]
                ).optional(),
                "sizeType": t.string().optional(),
                "ageGroup": t.string().optional(),
                "productTypes": t.array(t.string()).optional(),
                "displayAdsSimilarIds": t.array(t.string()).optional(),
                "customLabel1": t.string().optional(),
                "minHandlingTime": t.string().optional(),
                "transitTimeLabel": t.string().optional(),
                "externalSellerId": t.string(),
                "additionalSizeType": t.string().optional(),
                "productWeight": t.proxy(renames["ProductWeightIn"]).optional(),
                "pickupSla": t.string().optional(),
                "shippingWeight": t.proxy(
                    renames["ProductShippingWeightIn"]
                ).optional(),
                "title": t.string().optional(),
                "promotionIds": t.array(t.string()).optional(),
                "energyEfficiencyClass": t.string().optional(),
                "productHighlights": t.array(t.string()).optional(),
                "installment": t.proxy(renames["InstallmentIn"]).optional(),
                "multipack": t.string().optional(),
                "lifestyleImageLinks": t.array(t.string()).optional(),
                "link": t.string().optional(),
                "color": t.string().optional(),
                "brand": t.string().optional(),
                "additionalImageLinks": t.array(t.string()).optional(),
                "unitPricingMeasure": t.proxy(
                    renames["ProductUnitPricingMeasureIn"]
                ).optional(),
                "identifierExists": t.boolean().optional(),
                "source": t.string().optional(),
                "productWidth": t.proxy(renames["ProductDimensionIn"]).optional(),
                "loyaltyPoints": t.proxy(renames["LoyaltyPointsIn"]).optional(),
                "productHeight": t.proxy(renames["ProductDimensionIn"]).optional(),
                "linkTemplate": t.string().optional(),
                "certifications": t.array(
                    t.proxy(renames["ProductCertificationIn"])
                ).optional(),
                "isBundle": t.boolean().optional(),
                "productDetails": t.array(
                    t.proxy(renames["ProductProductDetailIn"])
                ).optional(),
                "mobileLink": t.string().optional(),
                "pickupMethod": t.string().optional(),
                "googleProductCategory": t.string().optional(),
                "displayAdsTitle": t.string().optional(),
                "minEnergyEfficiencyClass": t.string().optional(),
                "price": t.proxy(renames["PriceIn"]).optional(),
                "shipping": t.array(t.proxy(renames["ProductShippingIn"])).optional(),
                "shippingWidth": t.proxy(
                    renames["ProductShippingDimensionIn"]
                ).optional(),
                "customLabel0": t.string().optional(),
                "adsLabels": t.array(t.string()).optional(),
                "description": t.string().optional(),
                "adsRedirect": t.string().optional(),
                "shippingLabel": t.string().optional(),
                "canonicalLink": t.string().optional(),
                "condition": t.string().optional(),
                "productLength": t.proxy(renames["ProductDimensionIn"]).optional(),
                "offerId": t.string(),
                "adult": t.boolean().optional(),
                "material": t.string().optional(),
                "displayAdsId": t.string().optional(),
                "includedDestinations": t.array(t.string()).optional(),
                "contentLanguage": t.string(),
                "adsGrouping": t.string().optional(),
                "cloudExportAdditionalProperties": t.array(
                    t.proxy(renames["CloudExportAdditionalPropertiesIn"])
                ).optional(),
                "displayAdsLink": t.string().optional(),
                "maxHandlingTime": t.string().optional(),
                "sizeSystem": t.string().optional(),
                "subscriptionCost": t.proxy(
                    renames["ProductSubscriptionCostIn"]
                ).optional(),
                "salePriceEffectiveDate": t.string().optional(),
                "feedLabel": t.string().optional(),
                "disclosureDate": t.string().optional(),
                "taxes": t.array(t.proxy(renames["ProductTaxIn"])).optional(),
                "channel": t.string(),
                "customLabel4": t.string().optional(),
                "sizes": t.array(t.string()).optional(),
                "displayAdsValue": t.number().optional(),
                "costOfGoodsSold": t.proxy(renames["PriceIn"]).optional(),
                "mobileLinkTemplate": t.string().optional(),
                "targetCountry": t.string(),
                "salePrice": t.proxy(renames["PriceIn"]).optional(),
                "imageLink": t.string().optional(),
                "unitPricingBaseMeasure": t.proxy(
                    renames["ProductUnitPricingBaseMeasureIn"]
                ).optional(),
                "kind": t.string().optional(),
                "id": t.string().optional(),
                "maxEnergyEfficiencyClass": t.string().optional(),
                "pattern": t.string().optional(),
                "customAttributes": t.array(
                    t.proxy(renames["CustomAttributeIn"])
                ).optional(),
                "customLabel2": t.string().optional(),
                "shippingHeight": t.proxy(
                    renames["ProductShippingDimensionIn"]
                ).optional(),
                "customLabel3": t.string().optional(),
                "expirationDate": t.string().optional(),
                "pause": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["productsGet"] = content.post(
        "{merchantId}/products",
        t.struct(
            {
                "feedId": t.string().optional(),
                "merchantId": t.string().optional(),
                "sellOnGoogleQuantity": t.string().optional(),
                "taxCategory": t.string().optional(),
                "mpn": t.string().optional(),
                "gtin": t.string().optional(),
                "availabilityDate": t.string().optional(),
                "gender": t.string().optional(),
                "itemGroupId": t.string().optional(),
                "excludedDestinations": t.array(t.string()).optional(),
                "shoppingAdsExcludedCountries": t.array(t.string()).optional(),
                "availability": t.string().optional(),
                "shippingLength": t.proxy(
                    renames["ProductShippingDimensionIn"]
                ).optional(),
                "sizeType": t.string().optional(),
                "ageGroup": t.string().optional(),
                "productTypes": t.array(t.string()).optional(),
                "displayAdsSimilarIds": t.array(t.string()).optional(),
                "customLabel1": t.string().optional(),
                "minHandlingTime": t.string().optional(),
                "transitTimeLabel": t.string().optional(),
                "externalSellerId": t.string(),
                "additionalSizeType": t.string().optional(),
                "productWeight": t.proxy(renames["ProductWeightIn"]).optional(),
                "pickupSla": t.string().optional(),
                "shippingWeight": t.proxy(
                    renames["ProductShippingWeightIn"]
                ).optional(),
                "title": t.string().optional(),
                "promotionIds": t.array(t.string()).optional(),
                "energyEfficiencyClass": t.string().optional(),
                "productHighlights": t.array(t.string()).optional(),
                "installment": t.proxy(renames["InstallmentIn"]).optional(),
                "multipack": t.string().optional(),
                "lifestyleImageLinks": t.array(t.string()).optional(),
                "link": t.string().optional(),
                "color": t.string().optional(),
                "brand": t.string().optional(),
                "additionalImageLinks": t.array(t.string()).optional(),
                "unitPricingMeasure": t.proxy(
                    renames["ProductUnitPricingMeasureIn"]
                ).optional(),
                "identifierExists": t.boolean().optional(),
                "source": t.string().optional(),
                "productWidth": t.proxy(renames["ProductDimensionIn"]).optional(),
                "loyaltyPoints": t.proxy(renames["LoyaltyPointsIn"]).optional(),
                "productHeight": t.proxy(renames["ProductDimensionIn"]).optional(),
                "linkTemplate": t.string().optional(),
                "certifications": t.array(
                    t.proxy(renames["ProductCertificationIn"])
                ).optional(),
                "isBundle": t.boolean().optional(),
                "productDetails": t.array(
                    t.proxy(renames["ProductProductDetailIn"])
                ).optional(),
                "mobileLink": t.string().optional(),
                "pickupMethod": t.string().optional(),
                "googleProductCategory": t.string().optional(),
                "displayAdsTitle": t.string().optional(),
                "minEnergyEfficiencyClass": t.string().optional(),
                "price": t.proxy(renames["PriceIn"]).optional(),
                "shipping": t.array(t.proxy(renames["ProductShippingIn"])).optional(),
                "shippingWidth": t.proxy(
                    renames["ProductShippingDimensionIn"]
                ).optional(),
                "customLabel0": t.string().optional(),
                "adsLabels": t.array(t.string()).optional(),
                "description": t.string().optional(),
                "adsRedirect": t.string().optional(),
                "shippingLabel": t.string().optional(),
                "canonicalLink": t.string().optional(),
                "condition": t.string().optional(),
                "productLength": t.proxy(renames["ProductDimensionIn"]).optional(),
                "offerId": t.string(),
                "adult": t.boolean().optional(),
                "material": t.string().optional(),
                "displayAdsId": t.string().optional(),
                "includedDestinations": t.array(t.string()).optional(),
                "contentLanguage": t.string(),
                "adsGrouping": t.string().optional(),
                "cloudExportAdditionalProperties": t.array(
                    t.proxy(renames["CloudExportAdditionalPropertiesIn"])
                ).optional(),
                "displayAdsLink": t.string().optional(),
                "maxHandlingTime": t.string().optional(),
                "sizeSystem": t.string().optional(),
                "subscriptionCost": t.proxy(
                    renames["ProductSubscriptionCostIn"]
                ).optional(),
                "salePriceEffectiveDate": t.string().optional(),
                "feedLabel": t.string().optional(),
                "disclosureDate": t.string().optional(),
                "taxes": t.array(t.proxy(renames["ProductTaxIn"])).optional(),
                "channel": t.string(),
                "customLabel4": t.string().optional(),
                "sizes": t.array(t.string()).optional(),
                "displayAdsValue": t.number().optional(),
                "costOfGoodsSold": t.proxy(renames["PriceIn"]).optional(),
                "mobileLinkTemplate": t.string().optional(),
                "targetCountry": t.string(),
                "salePrice": t.proxy(renames["PriceIn"]).optional(),
                "imageLink": t.string().optional(),
                "unitPricingBaseMeasure": t.proxy(
                    renames["ProductUnitPricingBaseMeasureIn"]
                ).optional(),
                "kind": t.string().optional(),
                "id": t.string().optional(),
                "maxEnergyEfficiencyClass": t.string().optional(),
                "pattern": t.string().optional(),
                "customAttributes": t.array(
                    t.proxy(renames["CustomAttributeIn"])
                ).optional(),
                "customLabel2": t.string().optional(),
                "shippingHeight": t.proxy(
                    renames["ProductShippingDimensionIn"]
                ).optional(),
                "customLabel3": t.string().optional(),
                "expirationDate": t.string().optional(),
                "pause": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["productsCustombatch"] = content.post(
        "{merchantId}/products",
        t.struct(
            {
                "feedId": t.string().optional(),
                "merchantId": t.string().optional(),
                "sellOnGoogleQuantity": t.string().optional(),
                "taxCategory": t.string().optional(),
                "mpn": t.string().optional(),
                "gtin": t.string().optional(),
                "availabilityDate": t.string().optional(),
                "gender": t.string().optional(),
                "itemGroupId": t.string().optional(),
                "excludedDestinations": t.array(t.string()).optional(),
                "shoppingAdsExcludedCountries": t.array(t.string()).optional(),
                "availability": t.string().optional(),
                "shippingLength": t.proxy(
                    renames["ProductShippingDimensionIn"]
                ).optional(),
                "sizeType": t.string().optional(),
                "ageGroup": t.string().optional(),
                "productTypes": t.array(t.string()).optional(),
                "displayAdsSimilarIds": t.array(t.string()).optional(),
                "customLabel1": t.string().optional(),
                "minHandlingTime": t.string().optional(),
                "transitTimeLabel": t.string().optional(),
                "externalSellerId": t.string(),
                "additionalSizeType": t.string().optional(),
                "productWeight": t.proxy(renames["ProductWeightIn"]).optional(),
                "pickupSla": t.string().optional(),
                "shippingWeight": t.proxy(
                    renames["ProductShippingWeightIn"]
                ).optional(),
                "title": t.string().optional(),
                "promotionIds": t.array(t.string()).optional(),
                "energyEfficiencyClass": t.string().optional(),
                "productHighlights": t.array(t.string()).optional(),
                "installment": t.proxy(renames["InstallmentIn"]).optional(),
                "multipack": t.string().optional(),
                "lifestyleImageLinks": t.array(t.string()).optional(),
                "link": t.string().optional(),
                "color": t.string().optional(),
                "brand": t.string().optional(),
                "additionalImageLinks": t.array(t.string()).optional(),
                "unitPricingMeasure": t.proxy(
                    renames["ProductUnitPricingMeasureIn"]
                ).optional(),
                "identifierExists": t.boolean().optional(),
                "source": t.string().optional(),
                "productWidth": t.proxy(renames["ProductDimensionIn"]).optional(),
                "loyaltyPoints": t.proxy(renames["LoyaltyPointsIn"]).optional(),
                "productHeight": t.proxy(renames["ProductDimensionIn"]).optional(),
                "linkTemplate": t.string().optional(),
                "certifications": t.array(
                    t.proxy(renames["ProductCertificationIn"])
                ).optional(),
                "isBundle": t.boolean().optional(),
                "productDetails": t.array(
                    t.proxy(renames["ProductProductDetailIn"])
                ).optional(),
                "mobileLink": t.string().optional(),
                "pickupMethod": t.string().optional(),
                "googleProductCategory": t.string().optional(),
                "displayAdsTitle": t.string().optional(),
                "minEnergyEfficiencyClass": t.string().optional(),
                "price": t.proxy(renames["PriceIn"]).optional(),
                "shipping": t.array(t.proxy(renames["ProductShippingIn"])).optional(),
                "shippingWidth": t.proxy(
                    renames["ProductShippingDimensionIn"]
                ).optional(),
                "customLabel0": t.string().optional(),
                "adsLabels": t.array(t.string()).optional(),
                "description": t.string().optional(),
                "adsRedirect": t.string().optional(),
                "shippingLabel": t.string().optional(),
                "canonicalLink": t.string().optional(),
                "condition": t.string().optional(),
                "productLength": t.proxy(renames["ProductDimensionIn"]).optional(),
                "offerId": t.string(),
                "adult": t.boolean().optional(),
                "material": t.string().optional(),
                "displayAdsId": t.string().optional(),
                "includedDestinations": t.array(t.string()).optional(),
                "contentLanguage": t.string(),
                "adsGrouping": t.string().optional(),
                "cloudExportAdditionalProperties": t.array(
                    t.proxy(renames["CloudExportAdditionalPropertiesIn"])
                ).optional(),
                "displayAdsLink": t.string().optional(),
                "maxHandlingTime": t.string().optional(),
                "sizeSystem": t.string().optional(),
                "subscriptionCost": t.proxy(
                    renames["ProductSubscriptionCostIn"]
                ).optional(),
                "salePriceEffectiveDate": t.string().optional(),
                "feedLabel": t.string().optional(),
                "disclosureDate": t.string().optional(),
                "taxes": t.array(t.proxy(renames["ProductTaxIn"])).optional(),
                "channel": t.string(),
                "customLabel4": t.string().optional(),
                "sizes": t.array(t.string()).optional(),
                "displayAdsValue": t.number().optional(),
                "costOfGoodsSold": t.proxy(renames["PriceIn"]).optional(),
                "mobileLinkTemplate": t.string().optional(),
                "targetCountry": t.string(),
                "salePrice": t.proxy(renames["PriceIn"]).optional(),
                "imageLink": t.string().optional(),
                "unitPricingBaseMeasure": t.proxy(
                    renames["ProductUnitPricingBaseMeasureIn"]
                ).optional(),
                "kind": t.string().optional(),
                "id": t.string().optional(),
                "maxEnergyEfficiencyClass": t.string().optional(),
                "pattern": t.string().optional(),
                "customAttributes": t.array(
                    t.proxy(renames["CustomAttributeIn"])
                ).optional(),
                "customLabel2": t.string().optional(),
                "shippingHeight": t.proxy(
                    renames["ProductShippingDimensionIn"]
                ).optional(),
                "customLabel3": t.string().optional(),
                "expirationDate": t.string().optional(),
                "pause": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["productsDelete"] = content.post(
        "{merchantId}/products",
        t.struct(
            {
                "feedId": t.string().optional(),
                "merchantId": t.string().optional(),
                "sellOnGoogleQuantity": t.string().optional(),
                "taxCategory": t.string().optional(),
                "mpn": t.string().optional(),
                "gtin": t.string().optional(),
                "availabilityDate": t.string().optional(),
                "gender": t.string().optional(),
                "itemGroupId": t.string().optional(),
                "excludedDestinations": t.array(t.string()).optional(),
                "shoppingAdsExcludedCountries": t.array(t.string()).optional(),
                "availability": t.string().optional(),
                "shippingLength": t.proxy(
                    renames["ProductShippingDimensionIn"]
                ).optional(),
                "sizeType": t.string().optional(),
                "ageGroup": t.string().optional(),
                "productTypes": t.array(t.string()).optional(),
                "displayAdsSimilarIds": t.array(t.string()).optional(),
                "customLabel1": t.string().optional(),
                "minHandlingTime": t.string().optional(),
                "transitTimeLabel": t.string().optional(),
                "externalSellerId": t.string(),
                "additionalSizeType": t.string().optional(),
                "productWeight": t.proxy(renames["ProductWeightIn"]).optional(),
                "pickupSla": t.string().optional(),
                "shippingWeight": t.proxy(
                    renames["ProductShippingWeightIn"]
                ).optional(),
                "title": t.string().optional(),
                "promotionIds": t.array(t.string()).optional(),
                "energyEfficiencyClass": t.string().optional(),
                "productHighlights": t.array(t.string()).optional(),
                "installment": t.proxy(renames["InstallmentIn"]).optional(),
                "multipack": t.string().optional(),
                "lifestyleImageLinks": t.array(t.string()).optional(),
                "link": t.string().optional(),
                "color": t.string().optional(),
                "brand": t.string().optional(),
                "additionalImageLinks": t.array(t.string()).optional(),
                "unitPricingMeasure": t.proxy(
                    renames["ProductUnitPricingMeasureIn"]
                ).optional(),
                "identifierExists": t.boolean().optional(),
                "source": t.string().optional(),
                "productWidth": t.proxy(renames["ProductDimensionIn"]).optional(),
                "loyaltyPoints": t.proxy(renames["LoyaltyPointsIn"]).optional(),
                "productHeight": t.proxy(renames["ProductDimensionIn"]).optional(),
                "linkTemplate": t.string().optional(),
                "certifications": t.array(
                    t.proxy(renames["ProductCertificationIn"])
                ).optional(),
                "isBundle": t.boolean().optional(),
                "productDetails": t.array(
                    t.proxy(renames["ProductProductDetailIn"])
                ).optional(),
                "mobileLink": t.string().optional(),
                "pickupMethod": t.string().optional(),
                "googleProductCategory": t.string().optional(),
                "displayAdsTitle": t.string().optional(),
                "minEnergyEfficiencyClass": t.string().optional(),
                "price": t.proxy(renames["PriceIn"]).optional(),
                "shipping": t.array(t.proxy(renames["ProductShippingIn"])).optional(),
                "shippingWidth": t.proxy(
                    renames["ProductShippingDimensionIn"]
                ).optional(),
                "customLabel0": t.string().optional(),
                "adsLabels": t.array(t.string()).optional(),
                "description": t.string().optional(),
                "adsRedirect": t.string().optional(),
                "shippingLabel": t.string().optional(),
                "canonicalLink": t.string().optional(),
                "condition": t.string().optional(),
                "productLength": t.proxy(renames["ProductDimensionIn"]).optional(),
                "offerId": t.string(),
                "adult": t.boolean().optional(),
                "material": t.string().optional(),
                "displayAdsId": t.string().optional(),
                "includedDestinations": t.array(t.string()).optional(),
                "contentLanguage": t.string(),
                "adsGrouping": t.string().optional(),
                "cloudExportAdditionalProperties": t.array(
                    t.proxy(renames["CloudExportAdditionalPropertiesIn"])
                ).optional(),
                "displayAdsLink": t.string().optional(),
                "maxHandlingTime": t.string().optional(),
                "sizeSystem": t.string().optional(),
                "subscriptionCost": t.proxy(
                    renames["ProductSubscriptionCostIn"]
                ).optional(),
                "salePriceEffectiveDate": t.string().optional(),
                "feedLabel": t.string().optional(),
                "disclosureDate": t.string().optional(),
                "taxes": t.array(t.proxy(renames["ProductTaxIn"])).optional(),
                "channel": t.string(),
                "customLabel4": t.string().optional(),
                "sizes": t.array(t.string()).optional(),
                "displayAdsValue": t.number().optional(),
                "costOfGoodsSold": t.proxy(renames["PriceIn"]).optional(),
                "mobileLinkTemplate": t.string().optional(),
                "targetCountry": t.string(),
                "salePrice": t.proxy(renames["PriceIn"]).optional(),
                "imageLink": t.string().optional(),
                "unitPricingBaseMeasure": t.proxy(
                    renames["ProductUnitPricingBaseMeasureIn"]
                ).optional(),
                "kind": t.string().optional(),
                "id": t.string().optional(),
                "maxEnergyEfficiencyClass": t.string().optional(),
                "pattern": t.string().optional(),
                "customAttributes": t.array(
                    t.proxy(renames["CustomAttributeIn"])
                ).optional(),
                "customLabel2": t.string().optional(),
                "shippingHeight": t.proxy(
                    renames["ProductShippingDimensionIn"]
                ).optional(),
                "customLabel3": t.string().optional(),
                "expirationDate": t.string().optional(),
                "pause": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["productsInsert"] = content.post(
        "{merchantId}/products",
        t.struct(
            {
                "feedId": t.string().optional(),
                "merchantId": t.string().optional(),
                "sellOnGoogleQuantity": t.string().optional(),
                "taxCategory": t.string().optional(),
                "mpn": t.string().optional(),
                "gtin": t.string().optional(),
                "availabilityDate": t.string().optional(),
                "gender": t.string().optional(),
                "itemGroupId": t.string().optional(),
                "excludedDestinations": t.array(t.string()).optional(),
                "shoppingAdsExcludedCountries": t.array(t.string()).optional(),
                "availability": t.string().optional(),
                "shippingLength": t.proxy(
                    renames["ProductShippingDimensionIn"]
                ).optional(),
                "sizeType": t.string().optional(),
                "ageGroup": t.string().optional(),
                "productTypes": t.array(t.string()).optional(),
                "displayAdsSimilarIds": t.array(t.string()).optional(),
                "customLabel1": t.string().optional(),
                "minHandlingTime": t.string().optional(),
                "transitTimeLabel": t.string().optional(),
                "externalSellerId": t.string(),
                "additionalSizeType": t.string().optional(),
                "productWeight": t.proxy(renames["ProductWeightIn"]).optional(),
                "pickupSla": t.string().optional(),
                "shippingWeight": t.proxy(
                    renames["ProductShippingWeightIn"]
                ).optional(),
                "title": t.string().optional(),
                "promotionIds": t.array(t.string()).optional(),
                "energyEfficiencyClass": t.string().optional(),
                "productHighlights": t.array(t.string()).optional(),
                "installment": t.proxy(renames["InstallmentIn"]).optional(),
                "multipack": t.string().optional(),
                "lifestyleImageLinks": t.array(t.string()).optional(),
                "link": t.string().optional(),
                "color": t.string().optional(),
                "brand": t.string().optional(),
                "additionalImageLinks": t.array(t.string()).optional(),
                "unitPricingMeasure": t.proxy(
                    renames["ProductUnitPricingMeasureIn"]
                ).optional(),
                "identifierExists": t.boolean().optional(),
                "source": t.string().optional(),
                "productWidth": t.proxy(renames["ProductDimensionIn"]).optional(),
                "loyaltyPoints": t.proxy(renames["LoyaltyPointsIn"]).optional(),
                "productHeight": t.proxy(renames["ProductDimensionIn"]).optional(),
                "linkTemplate": t.string().optional(),
                "certifications": t.array(
                    t.proxy(renames["ProductCertificationIn"])
                ).optional(),
                "isBundle": t.boolean().optional(),
                "productDetails": t.array(
                    t.proxy(renames["ProductProductDetailIn"])
                ).optional(),
                "mobileLink": t.string().optional(),
                "pickupMethod": t.string().optional(),
                "googleProductCategory": t.string().optional(),
                "displayAdsTitle": t.string().optional(),
                "minEnergyEfficiencyClass": t.string().optional(),
                "price": t.proxy(renames["PriceIn"]).optional(),
                "shipping": t.array(t.proxy(renames["ProductShippingIn"])).optional(),
                "shippingWidth": t.proxy(
                    renames["ProductShippingDimensionIn"]
                ).optional(),
                "customLabel0": t.string().optional(),
                "adsLabels": t.array(t.string()).optional(),
                "description": t.string().optional(),
                "adsRedirect": t.string().optional(),
                "shippingLabel": t.string().optional(),
                "canonicalLink": t.string().optional(),
                "condition": t.string().optional(),
                "productLength": t.proxy(renames["ProductDimensionIn"]).optional(),
                "offerId": t.string(),
                "adult": t.boolean().optional(),
                "material": t.string().optional(),
                "displayAdsId": t.string().optional(),
                "includedDestinations": t.array(t.string()).optional(),
                "contentLanguage": t.string(),
                "adsGrouping": t.string().optional(),
                "cloudExportAdditionalProperties": t.array(
                    t.proxy(renames["CloudExportAdditionalPropertiesIn"])
                ).optional(),
                "displayAdsLink": t.string().optional(),
                "maxHandlingTime": t.string().optional(),
                "sizeSystem": t.string().optional(),
                "subscriptionCost": t.proxy(
                    renames["ProductSubscriptionCostIn"]
                ).optional(),
                "salePriceEffectiveDate": t.string().optional(),
                "feedLabel": t.string().optional(),
                "disclosureDate": t.string().optional(),
                "taxes": t.array(t.proxy(renames["ProductTaxIn"])).optional(),
                "channel": t.string(),
                "customLabel4": t.string().optional(),
                "sizes": t.array(t.string()).optional(),
                "displayAdsValue": t.number().optional(),
                "costOfGoodsSold": t.proxy(renames["PriceIn"]).optional(),
                "mobileLinkTemplate": t.string().optional(),
                "targetCountry": t.string(),
                "salePrice": t.proxy(renames["PriceIn"]).optional(),
                "imageLink": t.string().optional(),
                "unitPricingBaseMeasure": t.proxy(
                    renames["ProductUnitPricingBaseMeasureIn"]
                ).optional(),
                "kind": t.string().optional(),
                "id": t.string().optional(),
                "maxEnergyEfficiencyClass": t.string().optional(),
                "pattern": t.string().optional(),
                "customAttributes": t.array(
                    t.proxy(renames["CustomAttributeIn"])
                ).optional(),
                "customLabel2": t.string().optional(),
                "shippingHeight": t.proxy(
                    renames["ProductShippingDimensionIn"]
                ).optional(),
                "customLabel3": t.string().optional(),
                "expirationDate": t.string().optional(),
                "pause": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["conversionsourcesPatch"] = content.post(
        "{merchantId}/conversionsources/{conversionSourceId}:undelete",
        t.struct(
            {
                "merchantId": t.string(),
                "conversionSourceId": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["conversionsourcesDelete"] = content.post(
        "{merchantId}/conversionsources/{conversionSourceId}:undelete",
        t.struct(
            {
                "merchantId": t.string(),
                "conversionSourceId": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["conversionsourcesGet"] = content.post(
        "{merchantId}/conversionsources/{conversionSourceId}:undelete",
        t.struct(
            {
                "merchantId": t.string(),
                "conversionSourceId": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["conversionsourcesCreate"] = content.post(
        "{merchantId}/conversionsources/{conversionSourceId}:undelete",
        t.struct(
            {
                "merchantId": t.string(),
                "conversionSourceId": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["conversionsourcesList"] = content.post(
        "{merchantId}/conversionsources/{conversionSourceId}:undelete",
        t.struct(
            {
                "merchantId": t.string(),
                "conversionSourceId": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["conversionsourcesUndelete"] = content.post(
        "{merchantId}/conversionsources/{conversionSourceId}:undelete",
        t.struct(
            {
                "merchantId": t.string(),
                "conversionSourceId": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["shoppingadsprogramGet"] = content.post(
        "{merchantId}/shoppingadsprogram/requestreview",
        t.struct(
            {
                "merchantId": t.string(),
                "regionCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["shoppingadsprogramRequestreview"] = content.post(
        "{merchantId}/shoppingadsprogram/requestreview",
        t.struct(
            {
                "merchantId": t.string(),
                "regionCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["orderreportsListtransactions"] = content.get(
        "{merchantId}/orderreports/disbursements",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "disbursementStartDate": t.string().optional(),
                "merchantId": t.string().optional(),
                "disbursementEndDate": t.string().optional(),
                "maxResults": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrderreportsListDisbursementsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["orderreportsListdisbursements"] = content.get(
        "{merchantId}/orderreports/disbursements",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "disbursementStartDate": t.string().optional(),
                "merchantId": t.string().optional(),
                "disbursementEndDate": t.string().optional(),
                "maxResults": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrderreportsListDisbursementsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["ordersList"] = content.post(
        "{merchantId}/orders/{orderId}/refundorder",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "orderId": t.string().optional(),
                "fullRefund": t.boolean().optional(),
                "reasonText": t.string().optional(),
                "amount": t.proxy(renames["MonetaryAmountIn"]).optional(),
                "operationId": t.string().optional(),
                "reason": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrdersRefundOrderResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["ordersUpdateshipment"] = content.post(
        "{merchantId}/orders/{orderId}/refundorder",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "orderId": t.string().optional(),
                "fullRefund": t.boolean().optional(),
                "reasonText": t.string().optional(),
                "amount": t.proxy(renames["MonetaryAmountIn"]).optional(),
                "operationId": t.string().optional(),
                "reason": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrdersRefundOrderResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["ordersRefunditem"] = content.post(
        "{merchantId}/orders/{orderId}/refundorder",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "orderId": t.string().optional(),
                "fullRefund": t.boolean().optional(),
                "reasonText": t.string().optional(),
                "amount": t.proxy(renames["MonetaryAmountIn"]).optional(),
                "operationId": t.string().optional(),
                "reason": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrdersRefundOrderResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["ordersAcknowledge"] = content.post(
        "{merchantId}/orders/{orderId}/refundorder",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "orderId": t.string().optional(),
                "fullRefund": t.boolean().optional(),
                "reasonText": t.string().optional(),
                "amount": t.proxy(renames["MonetaryAmountIn"]).optional(),
                "operationId": t.string().optional(),
                "reason": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrdersRefundOrderResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["ordersCancel"] = content.post(
        "{merchantId}/orders/{orderId}/refundorder",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "orderId": t.string().optional(),
                "fullRefund": t.boolean().optional(),
                "reasonText": t.string().optional(),
                "amount": t.proxy(renames["MonetaryAmountIn"]).optional(),
                "operationId": t.string().optional(),
                "reason": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrdersRefundOrderResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["ordersGet"] = content.post(
        "{merchantId}/orders/{orderId}/refundorder",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "orderId": t.string().optional(),
                "fullRefund": t.boolean().optional(),
                "reasonText": t.string().optional(),
                "amount": t.proxy(renames["MonetaryAmountIn"]).optional(),
                "operationId": t.string().optional(),
                "reason": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrdersRefundOrderResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["ordersInstorerefundlineitem"] = content.post(
        "{merchantId}/orders/{orderId}/refundorder",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "orderId": t.string().optional(),
                "fullRefund": t.boolean().optional(),
                "reasonText": t.string().optional(),
                "amount": t.proxy(renames["MonetaryAmountIn"]).optional(),
                "operationId": t.string().optional(),
                "reason": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrdersRefundOrderResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["ordersCreatetestreturn"] = content.post(
        "{merchantId}/orders/{orderId}/refundorder",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "orderId": t.string().optional(),
                "fullRefund": t.boolean().optional(),
                "reasonText": t.string().optional(),
                "amount": t.proxy(renames["MonetaryAmountIn"]).optional(),
                "operationId": t.string().optional(),
                "reason": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrdersRefundOrderResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["ordersCanceltestorderbycustomer"] = content.post(
        "{merchantId}/orders/{orderId}/refundorder",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "orderId": t.string().optional(),
                "fullRefund": t.boolean().optional(),
                "reasonText": t.string().optional(),
                "amount": t.proxy(renames["MonetaryAmountIn"]).optional(),
                "operationId": t.string().optional(),
                "reason": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrdersRefundOrderResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["ordersCancellineitem"] = content.post(
        "{merchantId}/orders/{orderId}/refundorder",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "orderId": t.string().optional(),
                "fullRefund": t.boolean().optional(),
                "reasonText": t.string().optional(),
                "amount": t.proxy(renames["MonetaryAmountIn"]).optional(),
                "operationId": t.string().optional(),
                "reason": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrdersRefundOrderResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["ordersShiplineitems"] = content.post(
        "{merchantId}/orders/{orderId}/refundorder",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "orderId": t.string().optional(),
                "fullRefund": t.boolean().optional(),
                "reasonText": t.string().optional(),
                "amount": t.proxy(renames["MonetaryAmountIn"]).optional(),
                "operationId": t.string().optional(),
                "reason": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrdersRefundOrderResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["ordersCreatetestorder"] = content.post(
        "{merchantId}/orders/{orderId}/refundorder",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "orderId": t.string().optional(),
                "fullRefund": t.boolean().optional(),
                "reasonText": t.string().optional(),
                "amount": t.proxy(renames["MonetaryAmountIn"]).optional(),
                "operationId": t.string().optional(),
                "reason": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrdersRefundOrderResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["ordersUpdatelineitemshippingdetails"] = content.post(
        "{merchantId}/orders/{orderId}/refundorder",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "orderId": t.string().optional(),
                "fullRefund": t.boolean().optional(),
                "reasonText": t.string().optional(),
                "amount": t.proxy(renames["MonetaryAmountIn"]).optional(),
                "operationId": t.string().optional(),
                "reason": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrdersRefundOrderResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["ordersReturnrefundlineitem"] = content.post(
        "{merchantId}/orders/{orderId}/refundorder",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "orderId": t.string().optional(),
                "fullRefund": t.boolean().optional(),
                "reasonText": t.string().optional(),
                "amount": t.proxy(renames["MonetaryAmountIn"]).optional(),
                "operationId": t.string().optional(),
                "reason": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrdersRefundOrderResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["ordersUpdatemerchantorderid"] = content.post(
        "{merchantId}/orders/{orderId}/refundorder",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "orderId": t.string().optional(),
                "fullRefund": t.boolean().optional(),
                "reasonText": t.string().optional(),
                "amount": t.proxy(renames["MonetaryAmountIn"]).optional(),
                "operationId": t.string().optional(),
                "reason": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrdersRefundOrderResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["ordersGettestordertemplate"] = content.post(
        "{merchantId}/orders/{orderId}/refundorder",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "orderId": t.string().optional(),
                "fullRefund": t.boolean().optional(),
                "reasonText": t.string().optional(),
                "amount": t.proxy(renames["MonetaryAmountIn"]).optional(),
                "operationId": t.string().optional(),
                "reason": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrdersRefundOrderResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["ordersCaptureOrder"] = content.post(
        "{merchantId}/orders/{orderId}/refundorder",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "orderId": t.string().optional(),
                "fullRefund": t.boolean().optional(),
                "reasonText": t.string().optional(),
                "amount": t.proxy(renames["MonetaryAmountIn"]).optional(),
                "operationId": t.string().optional(),
                "reason": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrdersRefundOrderResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["ordersAdvancetestorder"] = content.post(
        "{merchantId}/orders/{orderId}/refundorder",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "orderId": t.string().optional(),
                "fullRefund": t.boolean().optional(),
                "reasonText": t.string().optional(),
                "amount": t.proxy(renames["MonetaryAmountIn"]).optional(),
                "operationId": t.string().optional(),
                "reason": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrdersRefundOrderResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["ordersGetbymerchantorderid"] = content.post(
        "{merchantId}/orders/{orderId}/refundorder",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "orderId": t.string().optional(),
                "fullRefund": t.boolean().optional(),
                "reasonText": t.string().optional(),
                "amount": t.proxy(renames["MonetaryAmountIn"]).optional(),
                "operationId": t.string().optional(),
                "reason": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrdersRefundOrderResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["ordersRejectreturnlineitem"] = content.post(
        "{merchantId}/orders/{orderId}/refundorder",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "orderId": t.string().optional(),
                "fullRefund": t.boolean().optional(),
                "reasonText": t.string().optional(),
                "amount": t.proxy(renames["MonetaryAmountIn"]).optional(),
                "operationId": t.string().optional(),
                "reason": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrdersRefundOrderResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["ordersSetlineitemmetadata"] = content.post(
        "{merchantId}/orders/{orderId}/refundorder",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "orderId": t.string().optional(),
                "fullRefund": t.boolean().optional(),
                "reasonText": t.string().optional(),
                "amount": t.proxy(renames["MonetaryAmountIn"]).optional(),
                "operationId": t.string().optional(),
                "reason": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrdersRefundOrderResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["ordersRefundorder"] = content.post(
        "{merchantId}/orders/{orderId}/refundorder",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "orderId": t.string().optional(),
                "fullRefund": t.boolean().optional(),
                "reasonText": t.string().optional(),
                "amount": t.proxy(renames["MonetaryAmountIn"]).optional(),
                "operationId": t.string().optional(),
                "reason": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrdersRefundOrderResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyongoogleprogramsGet"] = content.post(
        "{merchantId}/buyongoogleprograms/{regionCode}/activate",
        t.struct(
            {
                "regionCode": t.string(),
                "merchantId": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyongoogleprogramsRequestreview"] = content.post(
        "{merchantId}/buyongoogleprograms/{regionCode}/activate",
        t.struct(
            {
                "regionCode": t.string(),
                "merchantId": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyongoogleprogramsPatch"] = content.post(
        "{merchantId}/buyongoogleprograms/{regionCode}/activate",
        t.struct(
            {
                "regionCode": t.string(),
                "merchantId": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyongoogleprogramsOnboard"] = content.post(
        "{merchantId}/buyongoogleprograms/{regionCode}/activate",
        t.struct(
            {
                "regionCode": t.string(),
                "merchantId": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyongoogleprogramsPause"] = content.post(
        "{merchantId}/buyongoogleprograms/{regionCode}/activate",
        t.struct(
            {
                "regionCode": t.string(),
                "merchantId": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyongoogleprogramsActivate"] = content.post(
        "{merchantId}/buyongoogleprograms/{regionCode}/activate",
        t.struct(
            {
                "regionCode": t.string(),
                "merchantId": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["productdeliverytimeCreate"] = content.get(
        "{merchantId}/productdeliverytime/{productId}",
        t.struct(
            {
                "merchantId": t.string(),
                "productId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductDeliveryTimeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["productdeliverytimeDelete"] = content.get(
        "{merchantId}/productdeliverytime/{productId}",
        t.struct(
            {
                "merchantId": t.string(),
                "productId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductDeliveryTimeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["productdeliverytimeGet"] = content.get(
        "{merchantId}/productdeliverytime/{productId}",
        t.struct(
            {
                "merchantId": t.string(),
                "productId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductDeliveryTimeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["reportsSearch"] = content.post(
        "{merchantId}/reports/search",
        t.struct(
            {
                "merchantId": t.string(),
                "query": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountstatusesList"] = content.post(
        "accountstatuses/batch",
        t.struct(
            {
                "entries": t.array(
                    t.proxy(renames["AccountstatusesCustomBatchRequestEntryIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountstatusesCustomBatchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountstatusesGet"] = content.post(
        "accountstatuses/batch",
        t.struct(
            {
                "entries": t.array(
                    t.proxy(renames["AccountstatusesCustomBatchRequestEntryIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountstatusesCustomBatchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountstatusesCustombatch"] = content.post(
        "accountstatuses/batch",
        t.struct(
            {
                "entries": t.array(
                    t.proxy(renames["AccountstatusesCustomBatchRequestEntryIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountstatusesCustomBatchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liasettingsList"] = content.get(
        "{merchantId}/liasettings/{accountId}/accessiblegmbaccounts",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "accountId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LiasettingsGetAccessibleGmbAccountsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liasettingsGet"] = content.get(
        "{merchantId}/liasettings/{accountId}/accessiblegmbaccounts",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "accountId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LiasettingsGetAccessibleGmbAccountsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liasettingsCustombatch"] = content.get(
        "{merchantId}/liasettings/{accountId}/accessiblegmbaccounts",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "accountId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LiasettingsGetAccessibleGmbAccountsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liasettingsRequestgmbaccess"] = content.get(
        "{merchantId}/liasettings/{accountId}/accessiblegmbaccounts",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "accountId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LiasettingsGetAccessibleGmbAccountsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liasettingsSetinventoryverificationcontact"] = content.get(
        "{merchantId}/liasettings/{accountId}/accessiblegmbaccounts",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "accountId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LiasettingsGetAccessibleGmbAccountsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liasettingsRequestinventoryverification"] = content.get(
        "{merchantId}/liasettings/{accountId}/accessiblegmbaccounts",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "accountId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LiasettingsGetAccessibleGmbAccountsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liasettingsListposdataproviders"] = content.get(
        "{merchantId}/liasettings/{accountId}/accessiblegmbaccounts",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "accountId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LiasettingsGetAccessibleGmbAccountsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liasettingsSetposdataprovider"] = content.get(
        "{merchantId}/liasettings/{accountId}/accessiblegmbaccounts",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "accountId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LiasettingsGetAccessibleGmbAccountsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liasettingsUpdate"] = content.get(
        "{merchantId}/liasettings/{accountId}/accessiblegmbaccounts",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "accountId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LiasettingsGetAccessibleGmbAccountsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liasettingsGetaccessiblegmbaccounts"] = content.get(
        "{merchantId}/liasettings/{accountId}/accessiblegmbaccounts",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "accountId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LiasettingsGetAccessibleGmbAccountsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["productstatusesList"] = content.post(
        "productstatuses/batch",
        t.struct(
            {
                "entries": t.array(
                    t.proxy(renames["ProductstatusesCustomBatchRequestEntryIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductstatusesCustomBatchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["productstatusesGet"] = content.post(
        "productstatuses/batch",
        t.struct(
            {
                "entries": t.array(
                    t.proxy(renames["ProductstatusesCustomBatchRequestEntryIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductstatusesCustomBatchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["productstatusesCustombatch"] = content.post(
        "productstatuses/batch",
        t.struct(
            {
                "entries": t.array(
                    t.proxy(renames["ProductstatusesCustomBatchRequestEntryIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductstatusesCustomBatchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["productstatusesRepricingreportsList"] = content.get(
        "{merchantId}/productstatuses/{productId}/repricingreports",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "endDate": t.string().optional(),
                "pageSize": t.integer().optional(),
                "productId": t.string(),
                "ruleId": t.string().optional(),
                "merchantId": t.string(),
                "startDate": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListRepricingProductReportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["datafeedstatusesList"] = content.post(
        "datafeedstatuses/batch",
        t.struct(
            {
                "entries": t.array(
                    t.proxy(renames["DatafeedstatusesCustomBatchRequestEntryIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DatafeedstatusesCustomBatchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["datafeedstatusesGet"] = content.post(
        "datafeedstatuses/batch",
        t.struct(
            {
                "entries": t.array(
                    t.proxy(renames["DatafeedstatusesCustomBatchRequestEntryIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DatafeedstatusesCustomBatchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["datafeedstatusesCustombatch"] = content.post(
        "datafeedstatuses/batch",
        t.struct(
            {
                "entries": t.array(
                    t.proxy(renames["DatafeedstatusesCustomBatchRequestEntryIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DatafeedstatusesCustomBatchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["localinventoryInsert"] = content.post(
        "localinventory/batch",
        t.struct(
            {
                "entries": t.array(
                    t.proxy(renames["LocalinventoryCustomBatchRequestEntryIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LocalinventoryCustomBatchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["localinventoryCustombatch"] = content.post(
        "localinventory/batch",
        t.struct(
            {
                "entries": t.array(
                    t.proxy(renames["LocalinventoryCustomBatchRequestEntryIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LocalinventoryCustomBatchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["shippingsettingsGet"] = content.get(
        "{merchantId}/supportedPickupServices",
        t.struct({"merchantId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ShippingsettingsGetSupportedPickupServicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["shippingsettingsGetsupportedholidays"] = content.get(
        "{merchantId}/supportedPickupServices",
        t.struct({"merchantId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ShippingsettingsGetSupportedPickupServicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["shippingsettingsCustombatch"] = content.get(
        "{merchantId}/supportedPickupServices",
        t.struct({"merchantId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ShippingsettingsGetSupportedPickupServicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["shippingsettingsGetsupportedcarriers"] = content.get(
        "{merchantId}/supportedPickupServices",
        t.struct({"merchantId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ShippingsettingsGetSupportedPickupServicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["shippingsettingsUpdate"] = content.get(
        "{merchantId}/supportedPickupServices",
        t.struct({"merchantId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ShippingsettingsGetSupportedPickupServicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["shippingsettingsList"] = content.get(
        "{merchantId}/supportedPickupServices",
        t.struct({"merchantId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ShippingsettingsGetSupportedPickupServicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["shippingsettingsGetsupportedpickupservices"] = content.get(
        "{merchantId}/supportedPickupServices",
        t.struct({"merchantId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ShippingsettingsGetSupportedPickupServicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["datafeedsInsert"] = content.post(
        "{merchantId}/datafeeds/{datafeedId}/fetchNow",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "datafeedId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DatafeedsFetchNowResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["datafeedsUpdate"] = content.post(
        "{merchantId}/datafeeds/{datafeedId}/fetchNow",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "datafeedId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DatafeedsFetchNowResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["datafeedsCustombatch"] = content.post(
        "{merchantId}/datafeeds/{datafeedId}/fetchNow",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "datafeedId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DatafeedsFetchNowResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["datafeedsGet"] = content.post(
        "{merchantId}/datafeeds/{datafeedId}/fetchNow",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "datafeedId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DatafeedsFetchNowResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["datafeedsList"] = content.post(
        "{merchantId}/datafeeds/{datafeedId}/fetchNow",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "datafeedId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DatafeedsFetchNowResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["datafeedsDelete"] = content.post(
        "{merchantId}/datafeeds/{datafeedId}/fetchNow",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "datafeedId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DatafeedsFetchNowResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["datafeedsFetchnow"] = content.post(
        "{merchantId}/datafeeds/{datafeedId}/fetchNow",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "datafeedId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DatafeedsFetchNowResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["pubsubnotificationsettingsGet"] = content.put(
        "{merchantId}/pubsubnotificationsettings",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "cloudTopicName": t.string().optional(),
                "registeredEvents": t.array(t.string()).optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PubsubNotificationSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["pubsubnotificationsettingsUpdate"] = content.put(
        "{merchantId}/pubsubnotificationsettings",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "cloudTopicName": t.string().optional(),
                "registeredEvents": t.array(t.string()).optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PubsubNotificationSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settlementreportsGet"] = content.get(
        "{merchantId}/settlementreports",
        t.struct(
            {
                "transferStartDate": t.string().optional(),
                "merchantId": t.string().optional(),
                "pageToken": t.string().optional(),
                "transferEndDate": t.string().optional(),
                "maxResults": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SettlementreportsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settlementreportsList"] = content.get(
        "{merchantId}/settlementreports",
        t.struct(
            {
                "transferStartDate": t.string().optional(),
                "merchantId": t.string().optional(),
                "pageToken": t.string().optional(),
                "transferEndDate": t.string().optional(),
                "maxResults": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SettlementreportsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["regionsList"] = content.post(
        "{merchantId}/regions",
        t.struct(
            {
                "regionId": t.string(),
                "merchantId": t.string(),
                "geotargetArea": t.proxy(renames["RegionGeoTargetAreaIn"]).optional(),
                "postalCodeArea": t.proxy(renames["RegionPostalCodeAreaIn"]).optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RegionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["regionsGet"] = content.post(
        "{merchantId}/regions",
        t.struct(
            {
                "regionId": t.string(),
                "merchantId": t.string(),
                "geotargetArea": t.proxy(renames["RegionGeoTargetAreaIn"]).optional(),
                "postalCodeArea": t.proxy(renames["RegionPostalCodeAreaIn"]).optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RegionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["regionsDelete"] = content.post(
        "{merchantId}/regions",
        t.struct(
            {
                "regionId": t.string(),
                "merchantId": t.string(),
                "geotargetArea": t.proxy(renames["RegionGeoTargetAreaIn"]).optional(),
                "postalCodeArea": t.proxy(renames["RegionPostalCodeAreaIn"]).optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RegionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["regionsPatch"] = content.post(
        "{merchantId}/regions",
        t.struct(
            {
                "regionId": t.string(),
                "merchantId": t.string(),
                "geotargetArea": t.proxy(renames["RegionGeoTargetAreaIn"]).optional(),
                "postalCodeArea": t.proxy(renames["RegionPostalCodeAreaIn"]).optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RegionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["regionsCreate"] = content.post(
        "{merchantId}/regions",
        t.struct(
            {
                "regionId": t.string(),
                "merchantId": t.string(),
                "geotargetArea": t.proxy(renames["RegionGeoTargetAreaIn"]).optional(),
                "postalCodeArea": t.proxy(renames["RegionPostalCodeAreaIn"]).optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RegionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["cssesUpdatelabels"] = content.get(
        "{cssGroupId}/csses",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "cssGroupId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCssesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["cssesGet"] = content.get(
        "{cssGroupId}/csses",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "cssGroupId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCssesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["cssesList"] = content.get(
        "{cssGroupId}/csses",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "cssGroupId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCssesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["posInsert"] = content.delete(
        "{merchantId}/pos/{targetMerchantId}/store/{storeCode}",
        t.struct(
            {
                "targetMerchantId": t.string().optional(),
                "merchantId": t.string().optional(),
                "storeCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["posCustombatch"] = content.delete(
        "{merchantId}/pos/{targetMerchantId}/store/{storeCode}",
        t.struct(
            {
                "targetMerchantId": t.string().optional(),
                "merchantId": t.string().optional(),
                "storeCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["posSale"] = content.delete(
        "{merchantId}/pos/{targetMerchantId}/store/{storeCode}",
        t.struct(
            {
                "targetMerchantId": t.string().optional(),
                "merchantId": t.string().optional(),
                "storeCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["posGet"] = content.delete(
        "{merchantId}/pos/{targetMerchantId}/store/{storeCode}",
        t.struct(
            {
                "targetMerchantId": t.string().optional(),
                "merchantId": t.string().optional(),
                "storeCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["posList"] = content.delete(
        "{merchantId}/pos/{targetMerchantId}/store/{storeCode}",
        t.struct(
            {
                "targetMerchantId": t.string().optional(),
                "merchantId": t.string().optional(),
                "storeCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["posInventory"] = content.delete(
        "{merchantId}/pos/{targetMerchantId}/store/{storeCode}",
        t.struct(
            {
                "targetMerchantId": t.string().optional(),
                "merchantId": t.string().optional(),
                "storeCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["posDelete"] = content.delete(
        "{merchantId}/pos/{targetMerchantId}/store/{storeCode}",
        t.struct(
            {
                "targetMerchantId": t.string().optional(),
                "merchantId": t.string().optional(),
                "storeCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["promotionsGet"] = content.get(
        "{merchantId}/promotions",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "countryCode": t.string().optional(),
                "merchantId": t.string(),
                "pageSize": t.integer().optional(),
                "languageCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPromotionResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["promotionsCreate"] = content.get(
        "{merchantId}/promotions",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "countryCode": t.string().optional(),
                "merchantId": t.string(),
                "pageSize": t.integer().optional(),
                "languageCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPromotionResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["promotionsList"] = content.get(
        "{merchantId}/promotions",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "countryCode": t.string().optional(),
                "merchantId": t.string(),
                "pageSize": t.integer().optional(),
                "languageCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPromotionResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["collectionsList"] = content.post(
        "{merchantId}/collections",
        t.struct(
            {
                "merchantId": t.string(),
                "language": t.string().optional(),
                "id": t.string(),
                "productCountry": t.string().optional(),
                "customLabel2": t.string().optional(),
                "mobileLink": t.string().optional(),
                "imageLink": t.array(t.string()).optional(),
                "customLabel3": t.string().optional(),
                "headline": t.array(t.string()).optional(),
                "customLabel0": t.string().optional(),
                "featuredProduct": t.array(
                    t.proxy(renames["CollectionFeaturedProductIn"])
                ).optional(),
                "link": t.string().optional(),
                "customLabel1": t.string().optional(),
                "customLabel4": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CollectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["collectionsGet"] = content.post(
        "{merchantId}/collections",
        t.struct(
            {
                "merchantId": t.string(),
                "language": t.string().optional(),
                "id": t.string(),
                "productCountry": t.string().optional(),
                "customLabel2": t.string().optional(),
                "mobileLink": t.string().optional(),
                "imageLink": t.array(t.string()).optional(),
                "customLabel3": t.string().optional(),
                "headline": t.array(t.string()).optional(),
                "customLabel0": t.string().optional(),
                "featuredProduct": t.array(
                    t.proxy(renames["CollectionFeaturedProductIn"])
                ).optional(),
                "link": t.string().optional(),
                "customLabel1": t.string().optional(),
                "customLabel4": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CollectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["collectionsDelete"] = content.post(
        "{merchantId}/collections",
        t.struct(
            {
                "merchantId": t.string(),
                "language": t.string().optional(),
                "id": t.string(),
                "productCountry": t.string().optional(),
                "customLabel2": t.string().optional(),
                "mobileLink": t.string().optional(),
                "imageLink": t.array(t.string()).optional(),
                "customLabel3": t.string().optional(),
                "headline": t.array(t.string()).optional(),
                "customLabel0": t.string().optional(),
                "featuredProduct": t.array(
                    t.proxy(renames["CollectionFeaturedProductIn"])
                ).optional(),
                "link": t.string().optional(),
                "customLabel1": t.string().optional(),
                "customLabel4": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CollectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["collectionsCreate"] = content.post(
        "{merchantId}/collections",
        t.struct(
            {
                "merchantId": t.string(),
                "language": t.string().optional(),
                "id": t.string(),
                "productCountry": t.string().optional(),
                "customLabel2": t.string().optional(),
                "mobileLink": t.string().optional(),
                "imageLink": t.array(t.string()).optional(),
                "customLabel3": t.string().optional(),
                "headline": t.array(t.string()).optional(),
                "customLabel0": t.string().optional(),
                "featuredProduct": t.array(
                    t.proxy(renames["CollectionFeaturedProductIn"])
                ).optional(),
                "link": t.string().optional(),
                "customLabel1": t.string().optional(),
                "customLabel4": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CollectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["returnpolicyonlineDelete"] = content.get(
        "{merchantId}/returnpolicyonline",
        t.struct({"merchantId": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ListReturnPolicyOnlineResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["returnpolicyonlineCreate"] = content.get(
        "{merchantId}/returnpolicyonline",
        t.struct({"merchantId": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ListReturnPolicyOnlineResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["returnpolicyonlineGet"] = content.get(
        "{merchantId}/returnpolicyonline",
        t.struct({"merchantId": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ListReturnPolicyOnlineResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["returnpolicyonlinePatch"] = content.get(
        "{merchantId}/returnpolicyonline",
        t.struct({"merchantId": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ListReturnPolicyOnlineResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["returnpolicyonlineList"] = content.get(
        "{merchantId}/returnpolicyonline",
        t.struct({"merchantId": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ListReturnPolicyOnlineResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["orderreturnsAcknowledge"] = content.get(
        "{merchantId}/orderreturns/{returnId}",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "returnId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MerchantOrderReturnOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["orderreturnsList"] = content.get(
        "{merchantId}/orderreturns/{returnId}",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "returnId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MerchantOrderReturnOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["orderreturnsProcess"] = content.get(
        "{merchantId}/orderreturns/{returnId}",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "returnId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MerchantOrderReturnOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["orderreturnsCreateorderreturn"] = content.get(
        "{merchantId}/orderreturns/{returnId}",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "returnId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MerchantOrderReturnOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["orderreturnsGet"] = content.get(
        "{merchantId}/orderreturns/{returnId}",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "returnId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MerchantOrderReturnOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["orderreturnsLabelsCreate"] = content.post(
        "{merchantId}/orderreturns/{returnId}/labels",
        t.struct(
            {
                "returnId": t.string(),
                "merchantId": t.string(),
                "carrier": t.string().optional(),
                "labelUri": t.string().optional(),
                "trackingId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReturnShippingLabelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["freelistingsprogramRequestreview"] = content.get(
        "{merchantId}/freelistingsprogram",
        t.struct({"merchantId": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["FreeListingsProgramStatusOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["freelistingsprogramGet"] = content.get(
        "{merchantId}/freelistingsprogram",
        t.struct({"merchantId": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["FreeListingsProgramStatusOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["returnpolicyDelete"] = content.post(
        "{merchantId}/returnpolicy",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "kind": t.string().optional(),
                "label": t.string(),
                "nonFreeReturnReasons": t.array(t.string()).optional(),
                "policy": t.proxy(renames["ReturnPolicyPolicyIn"]),
                "name": t.string(),
                "seasonalOverrides": t.array(
                    t.proxy(renames["ReturnPolicySeasonalOverrideIn"])
                ).optional(),
                "returnPolicyId": t.string().optional(),
                "country": t.string(),
                "returnShippingFee": t.proxy(renames["PriceIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReturnPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["returnpolicyGet"] = content.post(
        "{merchantId}/returnpolicy",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "kind": t.string().optional(),
                "label": t.string(),
                "nonFreeReturnReasons": t.array(t.string()).optional(),
                "policy": t.proxy(renames["ReturnPolicyPolicyIn"]),
                "name": t.string(),
                "seasonalOverrides": t.array(
                    t.proxy(renames["ReturnPolicySeasonalOverrideIn"])
                ).optional(),
                "returnPolicyId": t.string().optional(),
                "country": t.string(),
                "returnShippingFee": t.proxy(renames["PriceIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReturnPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["returnpolicyList"] = content.post(
        "{merchantId}/returnpolicy",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "kind": t.string().optional(),
                "label": t.string(),
                "nonFreeReturnReasons": t.array(t.string()).optional(),
                "policy": t.proxy(renames["ReturnPolicyPolicyIn"]),
                "name": t.string(),
                "seasonalOverrides": t.array(
                    t.proxy(renames["ReturnPolicySeasonalOverrideIn"])
                ).optional(),
                "returnPolicyId": t.string().optional(),
                "country": t.string(),
                "returnShippingFee": t.proxy(renames["PriceIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReturnPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["returnpolicyCustombatch"] = content.post(
        "{merchantId}/returnpolicy",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "kind": t.string().optional(),
                "label": t.string(),
                "nonFreeReturnReasons": t.array(t.string()).optional(),
                "policy": t.proxy(renames["ReturnPolicyPolicyIn"]),
                "name": t.string(),
                "seasonalOverrides": t.array(
                    t.proxy(renames["ReturnPolicySeasonalOverrideIn"])
                ).optional(),
                "returnPolicyId": t.string().optional(),
                "country": t.string(),
                "returnShippingFee": t.proxy(renames["PriceIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReturnPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["returnpolicyInsert"] = content.post(
        "{merchantId}/returnpolicy",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "kind": t.string().optional(),
                "label": t.string(),
                "nonFreeReturnReasons": t.array(t.string()).optional(),
                "policy": t.proxy(renames["ReturnPolicyPolicyIn"]),
                "name": t.string(),
                "seasonalOverrides": t.array(
                    t.proxy(renames["ReturnPolicySeasonalOverrideIn"])
                ).optional(),
                "returnPolicyId": t.string().optional(),
                "country": t.string(),
                "returnShippingFee": t.proxy(renames["PriceIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReturnPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["collectionstatusesList"] = content.get(
        "{merchantId}/collectionstatuses/{collectionId}",
        t.struct(
            {
                "merchantId": t.string(),
                "collectionId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CollectionStatusOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["collectionstatusesGet"] = content.get(
        "{merchantId}/collectionstatuses/{collectionId}",
        t.struct(
            {
                "merchantId": t.string(),
                "collectionId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CollectionStatusOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="content", renames=renames, types=Box(types), functions=Box(functions)
    )
