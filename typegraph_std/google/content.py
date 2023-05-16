from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_content() -> Import:
    content = HTTPRuntime("https://shoppingcontent.googleapis.com/")

    renames = {
        "ErrorResponse": "_content_1_ErrorResponse",
        "OrdersRefundItemResponseIn": "_content_2_OrdersRefundItemResponseIn",
        "OrdersRefundItemResponseOut": "_content_3_OrdersRefundItemResponseOut",
        "RequestPhoneVerificationRequestIn": "_content_4_RequestPhoneVerificationRequestIn",
        "RequestPhoneVerificationRequestOut": "_content_5_RequestPhoneVerificationRequestOut",
        "PosSaleIn": "_content_6_PosSaleIn",
        "PosSaleOut": "_content_7_PosSaleOut",
        "MerchantOrderReturnItemIn": "_content_8_MerchantOrderReturnItemIn",
        "MerchantOrderReturnItemOut": "_content_9_MerchantOrderReturnItemOut",
        "CollectionStatusIn": "_content_10_CollectionStatusIn",
        "CollectionStatusOut": "_content_11_CollectionStatusOut",
        "OrderreturnsPartialRefundIn": "_content_12_OrderreturnsPartialRefundIn",
        "OrderreturnsPartialRefundOut": "_content_13_OrderreturnsPartialRefundOut",
        "AccountAdsLinkIn": "_content_14_AccountAdsLinkIn",
        "AccountAdsLinkOut": "_content_15_AccountAdsLinkOut",
        "OrderLineItemIn": "_content_16_OrderLineItemIn",
        "OrderLineItemOut": "_content_17_OrderLineItemOut",
        "CarriersCarrierIn": "_content_18_CarriersCarrierIn",
        "CarriersCarrierOut": "_content_19_CarriersCarrierOut",
        "ShipmentInvoiceLineItemInvoiceIn": "_content_20_ShipmentInvoiceLineItemInvoiceIn",
        "ShipmentInvoiceLineItemInvoiceOut": "_content_21_ShipmentInvoiceLineItemInvoiceOut",
        "ReturnaddressCustomBatchResponseIn": "_content_22_ReturnaddressCustomBatchResponseIn",
        "ReturnaddressCustomBatchResponseOut": "_content_23_ReturnaddressCustomBatchResponseOut",
        "AccountIdentifierIn": "_content_24_AccountIdentifierIn",
        "AccountIdentifierOut": "_content_25_AccountIdentifierOut",
        "CaptureOrderResponseIn": "_content_26_CaptureOrderResponseIn",
        "CaptureOrderResponseOut": "_content_27_CaptureOrderResponseOut",
        "TestOrderPickupDetailsPickupPersonIn": "_content_28_TestOrderPickupDetailsPickupPersonIn",
        "TestOrderPickupDetailsPickupPersonOut": "_content_29_TestOrderPickupDetailsPickupPersonOut",
        "RefundReasonIn": "_content_30_RefundReasonIn",
        "RefundReasonOut": "_content_31_RefundReasonOut",
        "OrderreportsListTransactionsResponseIn": "_content_32_OrderreportsListTransactionsResponseIn",
        "OrderreportsListTransactionsResponseOut": "_content_33_OrderreportsListTransactionsResponseOut",
        "ReturnaddressCustomBatchRequestEntryIn": "_content_34_ReturnaddressCustomBatchRequestEntryIn",
        "ReturnaddressCustomBatchRequestEntryOut": "_content_35_ReturnaddressCustomBatchRequestEntryOut",
        "ListCollectionsResponseIn": "_content_36_ListCollectionsResponseIn",
        "ListCollectionsResponseOut": "_content_37_ListCollectionsResponseOut",
        "ProductViewItemIssueIn": "_content_38_ProductViewItemIssueIn",
        "ProductViewItemIssueOut": "_content_39_ProductViewItemIssueOut",
        "RecommendationIn": "_content_40_RecommendationIn",
        "RecommendationOut": "_content_41_RecommendationOut",
        "ReturnpolicyListResponseIn": "_content_42_ReturnpolicyListResponseIn",
        "ReturnpolicyListResponseOut": "_content_43_ReturnpolicyListResponseOut",
        "PostalCodeRangeIn": "_content_44_PostalCodeRangeIn",
        "PostalCodeRangeOut": "_content_45_PostalCodeRangeOut",
        "SettlementTransactionAmountIn": "_content_46_SettlementTransactionAmountIn",
        "SettlementTransactionAmountOut": "_content_47_SettlementTransactionAmountOut",
        "AccountStatusStatisticsIn": "_content_48_AccountStatusStatisticsIn",
        "AccountStatusStatisticsOut": "_content_49_AccountStatusStatisticsOut",
        "DatafeedstatusesListResponseIn": "_content_50_DatafeedstatusesListResponseIn",
        "DatafeedstatusesListResponseOut": "_content_51_DatafeedstatusesListResponseOut",
        "SettlementTransactionTransactionIn": "_content_52_SettlementTransactionTransactionIn",
        "SettlementTransactionTransactionOut": "_content_53_SettlementTransactionTransactionOut",
        "OrdersSetLineItemMetadataResponseIn": "_content_54_OrdersSetLineItemMetadataResponseIn",
        "OrdersSetLineItemMetadataResponseOut": "_content_55_OrdersSetLineItemMetadataResponseOut",
        "LiasettingsCustomBatchResponseIn": "_content_56_LiasettingsCustomBatchResponseIn",
        "LiasettingsCustomBatchResponseOut": "_content_57_LiasettingsCustomBatchResponseOut",
        "ShoppingAdsProgramStatusReviewIneligibilityReasonDetailsIn": "_content_58_ShoppingAdsProgramStatusReviewIneligibilityReasonDetailsIn",
        "ShoppingAdsProgramStatusReviewIneligibilityReasonDetailsOut": "_content_59_ShoppingAdsProgramStatusReviewIneligibilityReasonDetailsOut",
        "AccountTaxIn": "_content_60_AccountTaxIn",
        "AccountTaxOut": "_content_61_AccountTaxOut",
        "LocationIdSetIn": "_content_62_LocationIdSetIn",
        "LocationIdSetOut": "_content_63_LocationIdSetOut",
        "OrderLineItemReturnInfoIn": "_content_64_OrderLineItemReturnInfoIn",
        "OrderLineItemReturnInfoOut": "_content_65_OrderLineItemReturnInfoOut",
        "AccountAddressIn": "_content_66_AccountAddressIn",
        "AccountAddressOut": "_content_67_AccountAddressOut",
        "OrderinvoicesCustomBatchRequestEntryCreateRefundInvoiceRefundOptionIn": "_content_68_OrderinvoicesCustomBatchRequestEntryCreateRefundInvoiceRefundOptionIn",
        "OrderinvoicesCustomBatchRequestEntryCreateRefundInvoiceRefundOptionOut": "_content_69_OrderinvoicesCustomBatchRequestEntryCreateRefundInvoiceRefundOptionOut",
        "OrderPickupDetailsIn": "_content_70_OrderPickupDetailsIn",
        "OrderPickupDetailsOut": "_content_71_OrderPickupDetailsOut",
        "PosSaleRequestIn": "_content_72_PosSaleRequestIn",
        "PosSaleRequestOut": "_content_73_PosSaleRequestOut",
        "LocalinventoryCustomBatchResponseEntryIn": "_content_74_LocalinventoryCustomBatchResponseEntryIn",
        "LocalinventoryCustomBatchResponseEntryOut": "_content_75_LocalinventoryCustomBatchResponseEntryOut",
        "OrdersShipLineItemsRequestIn": "_content_76_OrdersShipLineItemsRequestIn",
        "OrdersShipLineItemsRequestOut": "_content_77_OrdersShipLineItemsRequestOut",
        "RepricingProductReportIn": "_content_78_RepricingProductReportIn",
        "RepricingProductReportOut": "_content_79_RepricingProductReportOut",
        "OrdersGetByMerchantOrderIdResponseIn": "_content_80_OrdersGetByMerchantOrderIdResponseIn",
        "OrdersGetByMerchantOrderIdResponseOut": "_content_81_OrdersGetByMerchantOrderIdResponseOut",
        "ReturnAddressAddressIn": "_content_82_ReturnAddressAddressIn",
        "ReturnAddressAddressOut": "_content_83_ReturnAddressAddressOut",
        "ProductProductDetailIn": "_content_84_ProductProductDetailIn",
        "ProductProductDetailOut": "_content_85_ProductProductDetailOut",
        "DeliveryAreaIn": "_content_86_DeliveryAreaIn",
        "DeliveryAreaOut": "_content_87_DeliveryAreaOut",
        "ServiceStoreConfigCutoffConfigLocalCutoffTimeIn": "_content_88_ServiceStoreConfigCutoffConfigLocalCutoffTimeIn",
        "ServiceStoreConfigCutoffConfigLocalCutoffTimeOut": "_content_89_ServiceStoreConfigCutoffConfigLocalCutoffTimeOut",
        "ProductShippingWeightIn": "_content_90_ProductShippingWeightIn",
        "ProductShippingWeightOut": "_content_91_ProductShippingWeightOut",
        "AccountsCustomBatchRequestIn": "_content_92_AccountsCustomBatchRequestIn",
        "AccountsCustomBatchRequestOut": "_content_93_AccountsCustomBatchRequestOut",
        "PosStoreIn": "_content_94_PosStoreIn",
        "PosStoreOut": "_content_95_PosStoreOut",
        "ShoppingAdsProgramStatusRegionStatusIn": "_content_96_ShoppingAdsProgramStatusRegionStatusIn",
        "ShoppingAdsProgramStatusRegionStatusOut": "_content_97_ShoppingAdsProgramStatusRegionStatusOut",
        "DatafeedstatusesCustomBatchRequestIn": "_content_98_DatafeedstatusesCustomBatchRequestIn",
        "DatafeedstatusesCustomBatchRequestOut": "_content_99_DatafeedstatusesCustomBatchRequestOut",
        "RecommendationCallToActionIn": "_content_100_RecommendationCallToActionIn",
        "RecommendationCallToActionOut": "_content_101_RecommendationCallToActionOut",
        "OrderinvoicesCreateChargeInvoiceResponseIn": "_content_102_OrderinvoicesCreateChargeInvoiceResponseIn",
        "OrderinvoicesCreateChargeInvoiceResponseOut": "_content_103_OrderinvoicesCreateChargeInvoiceResponseOut",
        "DateIn": "_content_104_DateIn",
        "DateOut": "_content_105_DateOut",
        "AccountStatusProductsIn": "_content_106_AccountStatusProductsIn",
        "AccountStatusProductsOut": "_content_107_AccountStatusProductsOut",
        "DatafeedsCustomBatchResponseEntryIn": "_content_108_DatafeedsCustomBatchResponseEntryIn",
        "DatafeedsCustomBatchResponseEntryOut": "_content_109_DatafeedsCustomBatchResponseEntryOut",
        "RequestReviewFreeListingsRequestIn": "_content_110_RequestReviewFreeListingsRequestIn",
        "RequestReviewFreeListingsRequestOut": "_content_111_RequestReviewFreeListingsRequestOut",
        "RecommendationCreativeIn": "_content_112_RecommendationCreativeIn",
        "RecommendationCreativeOut": "_content_113_RecommendationCreativeOut",
        "AccountStatusIn": "_content_114_AccountStatusIn",
        "AccountStatusOut": "_content_115_AccountStatusOut",
        "ECommercePlatformLinkInfoIn": "_content_116_ECommercePlatformLinkInfoIn",
        "ECommercePlatformLinkInfoOut": "_content_117_ECommercePlatformLinkInfoOut",
        "CutoffTimeIn": "_content_118_CutoffTimeIn",
        "CutoffTimeOut": "_content_119_CutoffTimeOut",
        "OrdersCustomBatchRequestEntryUpdateShipmentScheduledDeliveryDetailsIn": "_content_120_OrdersCustomBatchRequestEntryUpdateShipmentScheduledDeliveryDetailsIn",
        "OrdersCustomBatchRequestEntryUpdateShipmentScheduledDeliveryDetailsOut": "_content_121_OrdersCustomBatchRequestEntryUpdateShipmentScheduledDeliveryDetailsOut",
        "LabelIdsIn": "_content_122_LabelIdsIn",
        "LabelIdsOut": "_content_123_LabelIdsOut",
        "RegionalinventoryCustomBatchResponseEntryIn": "_content_124_RegionalinventoryCustomBatchResponseEntryIn",
        "RegionalinventoryCustomBatchResponseEntryOut": "_content_125_RegionalinventoryCustomBatchResponseEntryOut",
        "GmbAccountsIn": "_content_126_GmbAccountsIn",
        "GmbAccountsOut": "_content_127_GmbAccountsOut",
        "PriceCompetitivenessIn": "_content_128_PriceCompetitivenessIn",
        "PriceCompetitivenessOut": "_content_129_PriceCompetitivenessOut",
        "OrdersCreateTestOrderRequestIn": "_content_130_OrdersCreateTestOrderRequestIn",
        "OrdersCreateTestOrderRequestOut": "_content_131_OrdersCreateTestOrderRequestOut",
        "PromotionPromotionStatusDestinationStatusIn": "_content_132_PromotionPromotionStatusDestinationStatusIn",
        "PromotionPromotionStatusDestinationStatusOut": "_content_133_PromotionPromotionStatusDestinationStatusOut",
        "SegmentsIn": "_content_134_SegmentsIn",
        "SegmentsOut": "_content_135_SegmentsOut",
        "OrderShipmentScheduledDeliveryDetailsIn": "_content_136_OrderShipmentScheduledDeliveryDetailsIn",
        "OrderShipmentScheduledDeliveryDetailsOut": "_content_137_OrderShipmentScheduledDeliveryDetailsOut",
        "OrderCustomerLoyaltyInfoIn": "_content_138_OrderCustomerLoyaltyInfoIn",
        "OrderCustomerLoyaltyInfoOut": "_content_139_OrderCustomerLoyaltyInfoOut",
        "OrderinvoicesCreateRefundInvoiceRequestIn": "_content_140_OrderinvoicesCreateRefundInvoiceRequestIn",
        "OrderinvoicesCreateRefundInvoiceRequestOut": "_content_141_OrderinvoicesCreateRefundInvoiceRequestOut",
        "ProductstatusesCustomBatchResponseIn": "_content_142_ProductstatusesCustomBatchResponseIn",
        "ProductstatusesCustomBatchResponseOut": "_content_143_ProductstatusesCustomBatchResponseOut",
        "DeliveryTimeIn": "_content_144_DeliveryTimeIn",
        "DeliveryTimeOut": "_content_145_DeliveryTimeOut",
        "ProductViewItemIssueIssueSeverityPerDestinationIn": "_content_146_ProductViewItemIssueIssueSeverityPerDestinationIn",
        "ProductViewItemIssueIssueSeverityPerDestinationOut": "_content_147_ProductViewItemIssueIssueSeverityPerDestinationOut",
        "PosListResponseIn": "_content_148_PosListResponseIn",
        "PosListResponseOut": "_content_149_PosListResponseOut",
        "DeliveryAreaPostalCodeRangeIn": "_content_150_DeliveryAreaPostalCodeRangeIn",
        "DeliveryAreaPostalCodeRangeOut": "_content_151_DeliveryAreaPostalCodeRangeOut",
        "CollectionStatusDestinationStatusIn": "_content_152_CollectionStatusDestinationStatusIn",
        "CollectionStatusDestinationStatusOut": "_content_153_CollectionStatusDestinationStatusOut",
        "TestOrderLineItemProductIn": "_content_154_TestOrderLineItemProductIn",
        "TestOrderLineItemProductOut": "_content_155_TestOrderLineItemProductOut",
        "AccountConversionSettingsIn": "_content_156_AccountConversionSettingsIn",
        "AccountConversionSettingsOut": "_content_157_AccountConversionSettingsOut",
        "OrdersCustomBatchRequestEntryRefundItemItemIn": "_content_158_OrdersCustomBatchRequestEntryRefundItemItemIn",
        "OrdersCustomBatchRequestEntryRefundItemItemOut": "_content_159_OrdersCustomBatchRequestEntryRefundItemItemOut",
        "RepricingRuleEligibleOfferMatcherStringMatcherIn": "_content_160_RepricingRuleEligibleOfferMatcherStringMatcherIn",
        "RepricingRuleEligibleOfferMatcherStringMatcherOut": "_content_161_RepricingRuleEligibleOfferMatcherStringMatcherOut",
        "WarehouseCutoffTimeIn": "_content_162_WarehouseCutoffTimeIn",
        "WarehouseCutoffTimeOut": "_content_163_WarehouseCutoffTimeOut",
        "CssIn": "_content_164_CssIn",
        "CssOut": "_content_165_CssOut",
        "BuyOnGoogleProgramStatusIn": "_content_166_BuyOnGoogleProgramStatusIn",
        "BuyOnGoogleProgramStatusOut": "_content_167_BuyOnGoogleProgramStatusOut",
        "OrderTrackingSignalLineItemDetailsIn": "_content_168_OrderTrackingSignalLineItemDetailsIn",
        "OrderTrackingSignalLineItemDetailsOut": "_content_169_OrderTrackingSignalLineItemDetailsOut",
        "AccounttaxCustomBatchRequestIn": "_content_170_AccounttaxCustomBatchRequestIn",
        "AccounttaxCustomBatchRequestOut": "_content_171_AccounttaxCustomBatchRequestOut",
        "OrderLineItemProductFeeIn": "_content_172_OrderLineItemProductFeeIn",
        "OrderLineItemProductFeeOut": "_content_173_OrderLineItemProductFeeOut",
        "ServiceStoreConfigCutoffConfigIn": "_content_174_ServiceStoreConfigCutoffConfigIn",
        "ServiceStoreConfigCutoffConfigOut": "_content_175_ServiceStoreConfigCutoffConfigOut",
        "ShipmentTrackingInfoIn": "_content_176_ShipmentTrackingInfoIn",
        "ShipmentTrackingInfoOut": "_content_177_ShipmentTrackingInfoOut",
        "ServiceIn": "_content_178_ServiceIn",
        "ServiceOut": "_content_179_ServiceOut",
        "OrderLineItemProductVariantAttributeIn": "_content_180_OrderLineItemProductVariantAttributeIn",
        "OrderLineItemProductVariantAttributeOut": "_content_181_OrderLineItemProductVariantAttributeOut",
        "OrderTrackingSignalShippingInfoIn": "_content_182_OrderTrackingSignalShippingInfoIn",
        "OrderTrackingSignalShippingInfoOut": "_content_183_OrderTrackingSignalShippingInfoOut",
        "SettlementTransactionIdentifiersIn": "_content_184_SettlementTransactionIdentifiersIn",
        "SettlementTransactionIdentifiersOut": "_content_185_SettlementTransactionIdentifiersOut",
        "OrdersRefundItemRequestIn": "_content_186_OrdersRefundItemRequestIn",
        "OrdersRefundItemRequestOut": "_content_187_OrdersRefundItemRequestOut",
        "ReturnAddressIn": "_content_188_ReturnAddressIn",
        "ReturnAddressOut": "_content_189_ReturnAddressOut",
        "ListConversionSourcesResponseIn": "_content_190_ListConversionSourcesResponseIn",
        "ListConversionSourcesResponseOut": "_content_191_ListConversionSourcesResponseOut",
        "ProductUnitPricingMeasureIn": "_content_192_ProductUnitPricingMeasureIn",
        "ProductUnitPricingMeasureOut": "_content_193_ProductUnitPricingMeasureOut",
        "AddressIn": "_content_194_AddressIn",
        "AddressOut": "_content_195_AddressOut",
        "OrdersCancelLineItemRequestIn": "_content_196_OrdersCancelLineItemRequestIn",
        "OrdersCancelLineItemRequestOut": "_content_197_OrdersCancelLineItemRequestOut",
        "ProductClusterIn": "_content_198_ProductClusterIn",
        "ProductClusterOut": "_content_199_ProductClusterOut",
        "OrderCustomerMarketingRightsInfoIn": "_content_200_OrderCustomerMarketingRightsInfoIn",
        "OrderCustomerMarketingRightsInfoOut": "_content_201_OrderCustomerMarketingRightsInfoOut",
        "PosCustomBatchRequestIn": "_content_202_PosCustomBatchRequestIn",
        "PosCustomBatchRequestOut": "_content_203_PosCustomBatchRequestOut",
        "AccountStatusAccountLevelIssueIn": "_content_204_AccountStatusAccountLevelIssueIn",
        "AccountStatusAccountLevelIssueOut": "_content_205_AccountStatusAccountLevelIssueOut",
        "ProductstatusesListResponseIn": "_content_206_ProductstatusesListResponseIn",
        "ProductstatusesListResponseOut": "_content_207_ProductstatusesListResponseOut",
        "ReturnaddressCustomBatchRequestIn": "_content_208_ReturnaddressCustomBatchRequestIn",
        "ReturnaddressCustomBatchRequestOut": "_content_209_ReturnaddressCustomBatchRequestOut",
        "AccountstatusesCustomBatchRequestEntryIn": "_content_210_AccountstatusesCustomBatchRequestEntryIn",
        "AccountstatusesCustomBatchRequestEntryOut": "_content_211_AccountstatusesCustomBatchRequestEntryOut",
        "PosInventoryIn": "_content_212_PosInventoryIn",
        "PosInventoryOut": "_content_213_PosInventoryOut",
        "OrderShipmentLineItemShipmentIn": "_content_214_OrderShipmentLineItemShipmentIn",
        "OrderShipmentLineItemShipmentOut": "_content_215_OrderShipmentLineItemShipmentOut",
        "OrderinvoicesCreateChargeInvoiceRequestIn": "_content_216_OrderinvoicesCreateChargeInvoiceRequestIn",
        "OrderinvoicesCreateChargeInvoiceRequestOut": "_content_217_OrderinvoicesCreateChargeInvoiceRequestOut",
        "RowIn": "_content_218_RowIn",
        "RowOut": "_content_219_RowOut",
        "AccountItemUpdatesIn": "_content_220_AccountItemUpdatesIn",
        "AccountItemUpdatesOut": "_content_221_AccountItemUpdatesOut",
        "ListReturnPolicyOnlineResponseIn": "_content_222_ListReturnPolicyOnlineResponseIn",
        "ListReturnPolicyOnlineResponseOut": "_content_223_ListReturnPolicyOnlineResponseOut",
        "OrderPickupDetailsCollectorIn": "_content_224_OrderPickupDetailsCollectorIn",
        "OrderPickupDetailsCollectorOut": "_content_225_OrderPickupDetailsCollectorOut",
        "ListMethodQuotasResponseIn": "_content_226_ListMethodQuotasResponseIn",
        "ListMethodQuotasResponseOut": "_content_227_ListMethodQuotasResponseOut",
        "OrdersAcknowledgeResponseIn": "_content_228_OrdersAcknowledgeResponseIn",
        "OrdersAcknowledgeResponseOut": "_content_229_OrdersAcknowledgeResponseOut",
        "OrdersCreateTestOrderResponseIn": "_content_230_OrdersCreateTestOrderResponseIn",
        "OrdersCreateTestOrderResponseOut": "_content_231_OrdersCreateTestOrderResponseOut",
        "RequestPhoneVerificationResponseIn": "_content_232_RequestPhoneVerificationResponseIn",
        "RequestPhoneVerificationResponseOut": "_content_233_RequestPhoneVerificationResponseOut",
        "OrderPromotionIn": "_content_234_OrderPromotionIn",
        "OrderPromotionOut": "_content_235_OrderPromotionOut",
        "RegionPostalCodeAreaPostalCodeRangeIn": "_content_236_RegionPostalCodeAreaPostalCodeRangeIn",
        "RegionPostalCodeAreaPostalCodeRangeOut": "_content_237_RegionPostalCodeAreaPostalCodeRangeOut",
        "OrderRefundIn": "_content_238_OrderRefundIn",
        "OrderRefundOut": "_content_239_OrderRefundOut",
        "ShippingSettingsIn": "_content_240_ShippingSettingsIn",
        "ShippingSettingsOut": "_content_241_ShippingSettingsOut",
        "ReturnpolicyCustomBatchRequestIn": "_content_242_ReturnpolicyCustomBatchRequestIn",
        "ReturnpolicyCustomBatchRequestOut": "_content_243_ReturnpolicyCustomBatchRequestOut",
        "TimePeriodIn": "_content_244_TimePeriodIn",
        "TimePeriodOut": "_content_245_TimePeriodOut",
        "LiaCountrySettingsIn": "_content_246_LiaCountrySettingsIn",
        "LiaCountrySettingsOut": "_content_247_LiaCountrySettingsOut",
        "OrderreturnsCreateOrderReturnRequestIn": "_content_248_OrderreturnsCreateOrderReturnRequestIn",
        "OrderreturnsCreateOrderReturnRequestOut": "_content_249_OrderreturnsCreateOrderReturnRequestOut",
        "ProductsListResponseIn": "_content_250_ProductsListResponseIn",
        "ProductsListResponseOut": "_content_251_ProductsListResponseOut",
        "AccountsCustomBatchRequestEntryIn": "_content_252_AccountsCustomBatchRequestEntryIn",
        "AccountsCustomBatchRequestEntryOut": "_content_253_AccountsCustomBatchRequestEntryOut",
        "TestOrderAddressIn": "_content_254_TestOrderAddressIn",
        "TestOrderAddressOut": "_content_255_TestOrderAddressOut",
        "OrderreturnsAcknowledgeResponseIn": "_content_256_OrderreturnsAcknowledgeResponseIn",
        "OrderreturnsAcknowledgeResponseOut": "_content_257_OrderreturnsAcknowledgeResponseOut",
        "AccounttaxListResponseIn": "_content_258_AccounttaxListResponseIn",
        "AccounttaxListResponseOut": "_content_259_AccounttaxListResponseOut",
        "RegionalInventoryIn": "_content_260_RegionalInventoryIn",
        "RegionalInventoryOut": "_content_261_RegionalInventoryOut",
        "OrderreturnsProcessRequestIn": "_content_262_OrderreturnsProcessRequestIn",
        "OrderreturnsProcessRequestOut": "_content_263_OrderreturnsProcessRequestOut",
        "ProductstatusesCustomBatchResponseEntryIn": "_content_264_ProductstatusesCustomBatchResponseEntryIn",
        "ProductstatusesCustomBatchResponseEntryOut": "_content_265_ProductstatusesCustomBatchResponseEntryOut",
        "ProductsCustomBatchResponseIn": "_content_266_ProductsCustomBatchResponseIn",
        "ProductsCustomBatchResponseOut": "_content_267_ProductsCustomBatchResponseOut",
        "LocalinventoryCustomBatchResponseIn": "_content_268_LocalinventoryCustomBatchResponseIn",
        "LocalinventoryCustomBatchResponseOut": "_content_269_LocalinventoryCustomBatchResponseOut",
        "VerifyPhoneNumberRequestIn": "_content_270_VerifyPhoneNumberRequestIn",
        "VerifyPhoneNumberRequestOut": "_content_271_VerifyPhoneNumberRequestOut",
        "ReturnPolicyOnlineRestockingFeeIn": "_content_272_ReturnPolicyOnlineRestockingFeeIn",
        "ReturnPolicyOnlineRestockingFeeOut": "_content_273_ReturnPolicyOnlineRestockingFeeOut",
        "OrdersUpdateShipmentRequestIn": "_content_274_OrdersUpdateShipmentRequestIn",
        "OrdersUpdateShipmentRequestOut": "_content_275_OrdersUpdateShipmentRequestOut",
        "OrderPromotionItemIn": "_content_276_OrderPromotionItemIn",
        "OrderPromotionItemOut": "_content_277_OrderPromotionItemOut",
        "ReturnPolicyOnlinePolicyIn": "_content_278_ReturnPolicyOnlinePolicyIn",
        "ReturnPolicyOnlinePolicyOut": "_content_279_ReturnPolicyOnlinePolicyOut",
        "ActivateBuyOnGoogleProgramRequestIn": "_content_280_ActivateBuyOnGoogleProgramRequestIn",
        "ActivateBuyOnGoogleProgramRequestOut": "_content_281_ActivateBuyOnGoogleProgramRequestOut",
        "ListAccountLabelsResponseIn": "_content_282_ListAccountLabelsResponseIn",
        "ListAccountLabelsResponseOut": "_content_283_ListAccountLabelsResponseOut",
        "WeightIn": "_content_284_WeightIn",
        "WeightOut": "_content_285_WeightOut",
        "ListAccountReturnCarrierResponseIn": "_content_286_ListAccountReturnCarrierResponseIn",
        "ListAccountReturnCarrierResponseOut": "_content_287_ListAccountReturnCarrierResponseOut",
        "GenerateRecommendationsResponseIn": "_content_288_GenerateRecommendationsResponseIn",
        "GenerateRecommendationsResponseOut": "_content_289_GenerateRecommendationsResponseOut",
        "OrderreturnsRejectOperationIn": "_content_290_OrderreturnsRejectOperationIn",
        "OrderreturnsRejectOperationOut": "_content_291_OrderreturnsRejectOperationOut",
        "OrdersUpdateLineItemShippingDetailsResponseIn": "_content_292_OrdersUpdateLineItemShippingDetailsResponseIn",
        "OrdersUpdateLineItemShippingDetailsResponseOut": "_content_293_OrdersUpdateLineItemShippingDetailsResponseOut",
        "OrderLineItemShippingDetailsMethodIn": "_content_294_OrderLineItemShippingDetailsMethodIn",
        "OrderLineItemShippingDetailsMethodOut": "_content_295_OrderLineItemShippingDetailsMethodOut",
        "ListRepricingRuleReportsResponseIn": "_content_296_ListRepricingRuleReportsResponseIn",
        "ListRepricingRuleReportsResponseOut": "_content_297_ListRepricingRuleReportsResponseOut",
        "OrdersListResponseIn": "_content_298_OrdersListResponseIn",
        "OrdersListResponseOut": "_content_299_OrdersListResponseOut",
        "AccountBusinessInformationIn": "_content_300_AccountBusinessInformationIn",
        "AccountBusinessInformationOut": "_content_301_AccountBusinessInformationOut",
        "RequestReviewShoppingAdsRequestIn": "_content_302_RequestReviewShoppingAdsRequestIn",
        "RequestReviewShoppingAdsRequestOut": "_content_303_RequestReviewShoppingAdsRequestOut",
        "CaptureOrderRequestIn": "_content_304_CaptureOrderRequestIn",
        "CaptureOrderRequestOut": "_content_305_CaptureOrderRequestOut",
        "PaymentServiceProviderLinkInfoIn": "_content_306_PaymentServiceProviderLinkInfoIn",
        "PaymentServiceProviderLinkInfoOut": "_content_307_PaymentServiceProviderLinkInfoOut",
        "TransitTableTransitTimeRowIn": "_content_308_TransitTableTransitTimeRowIn",
        "TransitTableTransitTimeRowOut": "_content_309_TransitTableTransitTimeRowOut",
        "PubsubNotificationSettingsIn": "_content_310_PubsubNotificationSettingsIn",
        "PubsubNotificationSettingsOut": "_content_311_PubsubNotificationSettingsOut",
        "AttributionSettingsConversionTypeIn": "_content_312_AttributionSettingsConversionTypeIn",
        "AttributionSettingsConversionTypeOut": "_content_313_AttributionSettingsConversionTypeOut",
        "ProductsCustomBatchRequestIn": "_content_314_ProductsCustomBatchRequestIn",
        "ProductsCustomBatchRequestOut": "_content_315_ProductsCustomBatchRequestOut",
        "DatafeedStatusExampleIn": "_content_316_DatafeedStatusExampleIn",
        "DatafeedStatusExampleOut": "_content_317_DatafeedStatusExampleOut",
        "AccountCustomerServiceIn": "_content_318_AccountCustomerServiceIn",
        "AccountCustomerServiceOut": "_content_319_AccountCustomerServiceOut",
        "FreeListingsProgramStatusRegionStatusIn": "_content_320_FreeListingsProgramStatusRegionStatusIn",
        "FreeListingsProgramStatusRegionStatusOut": "_content_321_FreeListingsProgramStatusRegionStatusOut",
        "OrdersCancelTestOrderByCustomerResponseIn": "_content_322_OrdersCancelTestOrderByCustomerResponseIn",
        "OrdersCancelTestOrderByCustomerResponseOut": "_content_323_OrdersCancelTestOrderByCustomerResponseOut",
        "OrderinvoicesCreateRefundInvoiceResponseIn": "_content_324_OrderinvoicesCreateRefundInvoiceResponseIn",
        "OrderinvoicesCreateRefundInvoiceResponseOut": "_content_325_OrderinvoicesCreateRefundInvoiceResponseOut",
        "OrdersCancelResponseIn": "_content_326_OrdersCancelResponseIn",
        "OrdersCancelResponseOut": "_content_327_OrdersCancelResponseOut",
        "GmbAccountsGmbAccountIn": "_content_328_GmbAccountsGmbAccountIn",
        "GmbAccountsGmbAccountOut": "_content_329_GmbAccountsGmbAccountOut",
        "OrdersCustomBatchRequestEntryRefundItemShippingIn": "_content_330_OrdersCustomBatchRequestEntryRefundItemShippingIn",
        "OrdersCustomBatchRequestEntryRefundItemShippingOut": "_content_331_OrdersCustomBatchRequestEntryRefundItemShippingOut",
        "OrdersInStoreRefundLineItemRequestIn": "_content_332_OrdersInStoreRefundLineItemRequestIn",
        "OrdersInStoreRefundLineItemRequestOut": "_content_333_OrdersInStoreRefundLineItemRequestOut",
        "AccountCredentialsIn": "_content_334_AccountCredentialsIn",
        "AccountCredentialsOut": "_content_335_AccountCredentialsOut",
        "PostalCodeGroupIn": "_content_336_PostalCodeGroupIn",
        "PostalCodeGroupOut": "_content_337_PostalCodeGroupOut",
        "ValueIn": "_content_338_ValueIn",
        "ValueOut": "_content_339_ValueOut",
        "LiasettingsSetInventoryVerificationContactResponseIn": "_content_340_LiasettingsSetInventoryVerificationContactResponseIn",
        "LiasettingsSetInventoryVerificationContactResponseOut": "_content_341_LiasettingsSetInventoryVerificationContactResponseOut",
        "OrdersAcknowledgeRequestIn": "_content_342_OrdersAcknowledgeRequestIn",
        "OrdersAcknowledgeRequestOut": "_content_343_OrdersAcknowledgeRequestOut",
        "PosDataProvidersIn": "_content_344_PosDataProvidersIn",
        "PosDataProvidersOut": "_content_345_PosDataProvidersOut",
        "AccountsLinkResponseIn": "_content_346_AccountsLinkResponseIn",
        "AccountsLinkResponseOut": "_content_347_AccountsLinkResponseOut",
        "LiasettingsGetAccessibleGmbAccountsResponseIn": "_content_348_LiasettingsGetAccessibleGmbAccountsResponseIn",
        "LiasettingsGetAccessibleGmbAccountsResponseOut": "_content_349_LiasettingsGetAccessibleGmbAccountsResponseOut",
        "LinkedAccountIn": "_content_350_LinkedAccountIn",
        "LinkedAccountOut": "_content_351_LinkedAccountOut",
        "AccountImageImprovementsSettingsIn": "_content_352_AccountImageImprovementsSettingsIn",
        "AccountImageImprovementsSettingsOut": "_content_353_AccountImageImprovementsSettingsOut",
        "ShippingsettingsListResponseIn": "_content_354_ShippingsettingsListResponseIn",
        "ShippingsettingsListResponseOut": "_content_355_ShippingsettingsListResponseOut",
        "LiasettingsRequestGmbAccessResponseIn": "_content_356_LiasettingsRequestGmbAccessResponseIn",
        "LiasettingsRequestGmbAccessResponseOut": "_content_357_LiasettingsRequestGmbAccessResponseOut",
        "InvoiceSummaryAdditionalChargeSummaryIn": "_content_358_InvoiceSummaryAdditionalChargeSummaryIn",
        "InvoiceSummaryAdditionalChargeSummaryOut": "_content_359_InvoiceSummaryAdditionalChargeSummaryOut",
        "OrderreturnsReturnItemIn": "_content_360_OrderreturnsReturnItemIn",
        "OrderreturnsReturnItemOut": "_content_361_OrderreturnsReturnItemOut",
        "PosSaleResponseIn": "_content_362_PosSaleResponseIn",
        "PosSaleResponseOut": "_content_363_PosSaleResponseOut",
        "SettlementtransactionsListResponseIn": "_content_364_SettlementtransactionsListResponseIn",
        "SettlementtransactionsListResponseOut": "_content_365_SettlementtransactionsListResponseOut",
        "ProductUnitPricingBaseMeasureIn": "_content_366_ProductUnitPricingBaseMeasureIn",
        "ProductUnitPricingBaseMeasureOut": "_content_367_ProductUnitPricingBaseMeasureOut",
        "ProductStatusItemLevelIssueIn": "_content_368_ProductStatusItemLevelIssueIn",
        "ProductStatusItemLevelIssueOut": "_content_369_ProductStatusItemLevelIssueOut",
        "OrdersReturnRefundLineItemResponseIn": "_content_370_OrdersReturnRefundLineItemResponseIn",
        "OrdersReturnRefundLineItemResponseOut": "_content_371_OrdersReturnRefundLineItemResponseOut",
        "ProductDimensionIn": "_content_372_ProductDimensionIn",
        "ProductDimensionOut": "_content_373_ProductDimensionOut",
        "MetricsIn": "_content_374_MetricsIn",
        "MetricsOut": "_content_375_MetricsOut",
        "RepricingRuleEffectiveTimeFixedTimePeriodIn": "_content_376_RepricingRuleEffectiveTimeFixedTimePeriodIn",
        "RepricingRuleEffectiveTimeFixedTimePeriodOut": "_content_377_RepricingRuleEffectiveTimeFixedTimePeriodOut",
        "ReturnPolicyOnlineReturnReasonCategoryInfoIn": "_content_378_ReturnPolicyOnlineReturnReasonCategoryInfoIn",
        "ReturnPolicyOnlineReturnReasonCategoryInfoOut": "_content_379_ReturnPolicyOnlineReturnReasonCategoryInfoOut",
        "AccountsListResponseIn": "_content_380_AccountsListResponseIn",
        "AccountsListResponseOut": "_content_381_AccountsListResponseOut",
        "ShippingsettingsGetSupportedHolidaysResponseIn": "_content_382_ShippingsettingsGetSupportedHolidaysResponseIn",
        "ShippingsettingsGetSupportedHolidaysResponseOut": "_content_383_ShippingsettingsGetSupportedHolidaysResponseOut",
        "LocalinventoryCustomBatchRequestIn": "_content_384_LocalinventoryCustomBatchRequestIn",
        "LocalinventoryCustomBatchRequestOut": "_content_385_LocalinventoryCustomBatchRequestOut",
        "UnitInvoiceTaxLineIn": "_content_386_UnitInvoiceTaxLineIn",
        "UnitInvoiceTaxLineOut": "_content_387_UnitInvoiceTaxLineOut",
        "FreeListingsProgramStatusIn": "_content_388_FreeListingsProgramStatusIn",
        "FreeListingsProgramStatusOut": "_content_389_FreeListingsProgramStatusOut",
        "TestOrderLineItemIn": "_content_390_TestOrderLineItemIn",
        "TestOrderLineItemOut": "_content_391_TestOrderLineItemOut",
        "RepricingRuleRestrictionBoundaryIn": "_content_392_RepricingRuleRestrictionBoundaryIn",
        "RepricingRuleRestrictionBoundaryOut": "_content_393_RepricingRuleRestrictionBoundaryOut",
        "OrdersShipLineItemsResponseIn": "_content_394_OrdersShipLineItemsResponseIn",
        "OrdersShipLineItemsResponseOut": "_content_395_OrdersShipLineItemsResponseOut",
        "OrdersRefundOrderResponseIn": "_content_396_OrdersRefundOrderResponseIn",
        "OrdersRefundOrderResponseOut": "_content_397_OrdersRefundOrderResponseOut",
        "OrdersUpdateMerchantOrderIdRequestIn": "_content_398_OrdersUpdateMerchantOrderIdRequestIn",
        "OrdersUpdateMerchantOrderIdRequestOut": "_content_399_OrdersUpdateMerchantOrderIdRequestOut",
        "ReturnPolicyPolicyIn": "_content_400_ReturnPolicyPolicyIn",
        "ReturnPolicyPolicyOut": "_content_401_ReturnPolicyPolicyOut",
        "RegionalinventoryCustomBatchResponseIn": "_content_402_RegionalinventoryCustomBatchResponseIn",
        "RegionalinventoryCustomBatchResponseOut": "_content_403_RegionalinventoryCustomBatchResponseOut",
        "OrdersCustomBatchRequestEntryCreateTestReturnReturnItemIn": "_content_404_OrdersCustomBatchRequestEntryCreateTestReturnReturnItemIn",
        "OrdersCustomBatchRequestEntryCreateTestReturnReturnItemOut": "_content_405_OrdersCustomBatchRequestEntryCreateTestReturnReturnItemOut",
        "OrderShipmentIn": "_content_406_OrderShipmentIn",
        "OrderShipmentOut": "_content_407_OrderShipmentOut",
        "CollectionStatusItemLevelIssueIn": "_content_408_CollectionStatusItemLevelIssueIn",
        "CollectionStatusItemLevelIssueOut": "_content_409_CollectionStatusItemLevelIssueOut",
        "OrdersAdvanceTestOrderResponseIn": "_content_410_OrdersAdvanceTestOrderResponseIn",
        "OrdersAdvanceTestOrderResponseOut": "_content_411_OrdersAdvanceTestOrderResponseOut",
        "RepricingRuleRestrictionIn": "_content_412_RepricingRuleRestrictionIn",
        "RepricingRuleRestrictionOut": "_content_413_RepricingRuleRestrictionOut",
        "ProductstatusesCustomBatchRequestIn": "_content_414_ProductstatusesCustomBatchRequestIn",
        "ProductstatusesCustomBatchRequestOut": "_content_415_ProductstatusesCustomBatchRequestOut",
        "OrdersRejectReturnLineItemResponseIn": "_content_416_OrdersRejectReturnLineItemResponseIn",
        "OrdersRejectReturnLineItemResponseOut": "_content_417_OrdersRejectReturnLineItemResponseOut",
        "RepricingRuleIn": "_content_418_RepricingRuleIn",
        "RepricingRuleOut": "_content_419_RepricingRuleOut",
        "OrderreportsListDisbursementsResponseIn": "_content_420_OrderreportsListDisbursementsResponseIn",
        "OrderreportsListDisbursementsResponseOut": "_content_421_OrderreportsListDisbursementsResponseOut",
        "HolidaysHolidayIn": "_content_422_HolidaysHolidayIn",
        "HolidaysHolidayOut": "_content_423_HolidaysHolidayOut",
        "PauseBuyOnGoogleProgramRequestIn": "_content_424_PauseBuyOnGoogleProgramRequestIn",
        "PauseBuyOnGoogleProgramRequestOut": "_content_425_PauseBuyOnGoogleProgramRequestOut",
        "DateTimeIn": "_content_426_DateTimeIn",
        "DateTimeOut": "_content_427_DateTimeOut",
        "ShippingsettingsGetSupportedPickupServicesResponseIn": "_content_428_ShippingsettingsGetSupportedPickupServicesResponseIn",
        "ShippingsettingsGetSupportedPickupServicesResponseOut": "_content_429_ShippingsettingsGetSupportedPickupServicesResponseOut",
        "ReturnpolicyCustomBatchResponseIn": "_content_430_ReturnpolicyCustomBatchResponseIn",
        "ReturnpolicyCustomBatchResponseOut": "_content_431_ReturnpolicyCustomBatchResponseOut",
        "InapplicabilityDetailsIn": "_content_432_InapplicabilityDetailsIn",
        "InapplicabilityDetailsOut": "_content_433_InapplicabilityDetailsOut",
        "LiaOnDisplayToOrderSettingsIn": "_content_434_LiaOnDisplayToOrderSettingsIn",
        "LiaOnDisplayToOrderSettingsOut": "_content_435_LiaOnDisplayToOrderSettingsOut",
        "ProductDeliveryTimeIn": "_content_436_ProductDeliveryTimeIn",
        "ProductDeliveryTimeOut": "_content_437_ProductDeliveryTimeOut",
        "ShippingsettingsCustomBatchRequestIn": "_content_438_ShippingsettingsCustomBatchRequestIn",
        "ShippingsettingsCustomBatchRequestOut": "_content_439_ShippingsettingsCustomBatchRequestOut",
        "AccountsLinkRequestIn": "_content_440_AccountsLinkRequestIn",
        "AccountsLinkRequestOut": "_content_441_AccountsLinkRequestOut",
        "PickupCarrierServiceIn": "_content_442_PickupCarrierServiceIn",
        "PickupCarrierServiceOut": "_content_443_PickupCarrierServiceOut",
        "AccountImageImprovementsIn": "_content_444_AccountImageImprovementsIn",
        "AccountImageImprovementsOut": "_content_445_AccountImageImprovementsOut",
        "AttributionSettingsIn": "_content_446_AttributionSettingsIn",
        "AttributionSettingsOut": "_content_447_AttributionSettingsOut",
        "OrdersInStoreRefundLineItemResponseIn": "_content_448_OrdersInStoreRefundLineItemResponseIn",
        "OrdersInStoreRefundLineItemResponseOut": "_content_449_OrdersInStoreRefundLineItemResponseOut",
        "MethodQuotaIn": "_content_450_MethodQuotaIn",
        "MethodQuotaOut": "_content_451_MethodQuotaOut",
        "ProductAmountIn": "_content_452_ProductAmountIn",
        "ProductAmountOut": "_content_453_ProductAmountOut",
        "ProductIn": "_content_454_ProductIn",
        "ProductOut": "_content_455_ProductOut",
        "OrderCustomerIn": "_content_456_OrderCustomerIn",
        "OrderCustomerOut": "_content_457_OrderCustomerOut",
        "ServiceStoreConfigIn": "_content_458_ServiceStoreConfigIn",
        "ServiceStoreConfigOut": "_content_459_ServiceStoreConfigOut",
        "SearchRequestIn": "_content_460_SearchRequestIn",
        "SearchRequestOut": "_content_461_SearchRequestOut",
        "TransitTableIn": "_content_462_TransitTableIn",
        "TransitTableOut": "_content_463_TransitTableOut",
        "LiaPosDataProviderIn": "_content_464_LiaPosDataProviderIn",
        "LiaPosDataProviderOut": "_content_465_LiaPosDataProviderOut",
        "RegionPostalCodeAreaIn": "_content_466_RegionPostalCodeAreaIn",
        "RegionPostalCodeAreaOut": "_content_467_RegionPostalCodeAreaOut",
        "ReturnPolicySeasonalOverrideIn": "_content_468_ReturnPolicySeasonalOverrideIn",
        "ReturnPolicySeasonalOverrideOut": "_content_469_ReturnPolicySeasonalOverrideOut",
        "TestOrderDeliveryDetailsIn": "_content_470_TestOrderDeliveryDetailsIn",
        "TestOrderDeliveryDetailsOut": "_content_471_TestOrderDeliveryDetailsOut",
        "DistanceIn": "_content_472_DistanceIn",
        "DistanceOut": "_content_473_DistanceOut",
        "OrderreturnsCreateOrderReturnResponseIn": "_content_474_OrderreturnsCreateOrderReturnResponseIn",
        "OrderreturnsCreateOrderReturnResponseOut": "_content_475_OrderreturnsCreateOrderReturnResponseOut",
        "DatafeedFetchScheduleIn": "_content_476_DatafeedFetchScheduleIn",
        "DatafeedFetchScheduleOut": "_content_477_DatafeedFetchScheduleOut",
        "OrderTrackingSignalShipmentLineItemMappingIn": "_content_478_OrderTrackingSignalShipmentLineItemMappingIn",
        "OrderTrackingSignalShipmentLineItemMappingOut": "_content_479_OrderTrackingSignalShipmentLineItemMappingOut",
        "RegionGeoTargetAreaIn": "_content_480_RegionGeoTargetAreaIn",
        "RegionGeoTargetAreaOut": "_content_481_RegionGeoTargetAreaOut",
        "PromotionIn": "_content_482_PromotionIn",
        "PromotionOut": "_content_483_PromotionOut",
        "AccounttaxCustomBatchRequestEntryIn": "_content_484_AccounttaxCustomBatchRequestEntryIn",
        "AccounttaxCustomBatchRequestEntryOut": "_content_485_AccounttaxCustomBatchRequestEntryOut",
        "PriceInsightsIn": "_content_486_PriceInsightsIn",
        "PriceInsightsOut": "_content_487_PriceInsightsOut",
        "LoyaltyPointsIn": "_content_488_LoyaltyPointsIn",
        "LoyaltyPointsOut": "_content_489_LoyaltyPointsOut",
        "UnitInvoiceAdditionalChargeIn": "_content_490_UnitInvoiceAdditionalChargeIn",
        "UnitInvoiceAdditionalChargeOut": "_content_491_UnitInvoiceAdditionalChargeOut",
        "ReturnShippingLabelIn": "_content_492_ReturnShippingLabelIn",
        "ReturnShippingLabelOut": "_content_493_ReturnShippingLabelOut",
        "ProductWeightIn": "_content_494_ProductWeightIn",
        "ProductWeightOut": "_content_495_ProductWeightOut",
        "OrdersUpdateShipmentResponseIn": "_content_496_OrdersUpdateShipmentResponseIn",
        "OrdersUpdateShipmentResponseOut": "_content_497_OrdersUpdateShipmentResponseOut",
        "AccountstatusesCustomBatchRequestIn": "_content_498_AccountstatusesCustomBatchRequestIn",
        "AccountstatusesCustomBatchRequestOut": "_content_499_AccountstatusesCustomBatchRequestOut",
        "RegionalinventoryCustomBatchRequestEntryIn": "_content_500_RegionalinventoryCustomBatchRequestEntryIn",
        "RegionalinventoryCustomBatchRequestEntryOut": "_content_501_RegionalinventoryCustomBatchRequestEntryOut",
        "ProductsCustomBatchRequestEntryIn": "_content_502_ProductsCustomBatchRequestEntryIn",
        "ProductsCustomBatchRequestEntryOut": "_content_503_ProductsCustomBatchRequestEntryOut",
        "WarehouseBasedDeliveryTimeIn": "_content_504_WarehouseBasedDeliveryTimeIn",
        "WarehouseBasedDeliveryTimeOut": "_content_505_WarehouseBasedDeliveryTimeOut",
        "AccountsAuthInfoResponseIn": "_content_506_AccountsAuthInfoResponseIn",
        "AccountsAuthInfoResponseOut": "_content_507_AccountsAuthInfoResponseOut",
        "AccountAutomaticImprovementsIn": "_content_508_AccountAutomaticImprovementsIn",
        "AccountAutomaticImprovementsOut": "_content_509_AccountAutomaticImprovementsOut",
        "ShippingsettingsCustomBatchResponseEntryIn": "_content_510_ShippingsettingsCustomBatchResponseEntryIn",
        "ShippingsettingsCustomBatchResponseEntryOut": "_content_511_ShippingsettingsCustomBatchResponseEntryOut",
        "HeadersIn": "_content_512_HeadersIn",
        "HeadersOut": "_content_513_HeadersOut",
        "RequestReviewBuyOnGoogleProgramRequestIn": "_content_514_RequestReviewBuyOnGoogleProgramRequestIn",
        "RequestReviewBuyOnGoogleProgramRequestOut": "_content_515_RequestReviewBuyOnGoogleProgramRequestOut",
        "AccountIn": "_content_516_AccountIn",
        "AccountOut": "_content_517_AccountOut",
        "ProductViewItemIssueItemIssueTypeIn": "_content_518_ProductViewItemIssueItemIssueTypeIn",
        "ProductViewItemIssueItemIssueTypeOut": "_content_519_ProductViewItemIssueItemIssueTypeOut",
        "OrdersUpdateLineItemShippingDetailsRequestIn": "_content_520_OrdersUpdateLineItemShippingDetailsRequestIn",
        "OrdersUpdateLineItemShippingDetailsRequestOut": "_content_521_OrdersUpdateLineItemShippingDetailsRequestOut",
        "MinimumOrderValueTableIn": "_content_522_MinimumOrderValueTableIn",
        "MinimumOrderValueTableOut": "_content_523_MinimumOrderValueTableOut",
        "RegionIn": "_content_524_RegionIn",
        "RegionOut": "_content_525_RegionOut",
        "BrandIn": "_content_526_BrandIn",
        "BrandOut": "_content_527_BrandOut",
        "AccountsUpdateLabelsResponseIn": "_content_528_AccountsUpdateLabelsResponseIn",
        "AccountsUpdateLabelsResponseOut": "_content_529_AccountsUpdateLabelsResponseOut",
        "ErrorsIn": "_content_530_ErrorsIn",
        "ErrorsOut": "_content_531_ErrorsOut",
        "AccountReturnCarrierIn": "_content_532_AccountReturnCarrierIn",
        "AccountReturnCarrierOut": "_content_533_AccountReturnCarrierOut",
        "ListCssesResponseIn": "_content_534_ListCssesResponseIn",
        "ListCssesResponseOut": "_content_535_ListCssesResponseOut",
        "AccountUserIn": "_content_536_AccountUserIn",
        "AccountUserOut": "_content_537_AccountUserOut",
        "ProductShippingDimensionIn": "_content_538_ProductShippingDimensionIn",
        "ProductShippingDimensionOut": "_content_539_ProductShippingDimensionOut",
        "PriceAmountIn": "_content_540_PriceAmountIn",
        "PriceAmountOut": "_content_541_PriceAmountOut",
        "ShippingsettingsCustomBatchRequestEntryIn": "_content_542_ShippingsettingsCustomBatchRequestEntryIn",
        "ShippingsettingsCustomBatchRequestEntryOut": "_content_543_ShippingsettingsCustomBatchRequestEntryOut",
        "OrdersReturnRefundLineItemRequestIn": "_content_544_OrdersReturnRefundLineItemRequestIn",
        "OrdersReturnRefundLineItemRequestOut": "_content_545_OrdersReturnRefundLineItemRequestOut",
        "DatafeedstatusesCustomBatchResponseIn": "_content_546_DatafeedstatusesCustomBatchResponseIn",
        "DatafeedstatusesCustomBatchResponseOut": "_content_547_DatafeedstatusesCustomBatchResponseOut",
        "PickupServicesPickupServiceIn": "_content_548_PickupServicesPickupServiceIn",
        "PickupServicesPickupServiceOut": "_content_549_PickupServicesPickupServiceOut",
        "ProductViewItemIssueItemIssueSeverityIn": "_content_550_ProductViewItemIssueItemIssueSeverityIn",
        "ProductViewItemIssueItemIssueSeverityOut": "_content_551_ProductViewItemIssueItemIssueSeverityOut",
        "PosCustomBatchResponseEntryIn": "_content_552_PosCustomBatchResponseEntryIn",
        "PosCustomBatchResponseEntryOut": "_content_553_PosCustomBatchResponseEntryOut",
        "PosInventoryResponseIn": "_content_554_PosInventoryResponseIn",
        "PosInventoryResponseOut": "_content_555_PosInventoryResponseOut",
        "RepricingRuleCostOfGoodsSaleRuleIn": "_content_556_RepricingRuleCostOfGoodsSaleRuleIn",
        "RepricingRuleCostOfGoodsSaleRuleOut": "_content_557_RepricingRuleCostOfGoodsSaleRuleOut",
        "OrderOrderAnnotationIn": "_content_558_OrderOrderAnnotationIn",
        "OrderOrderAnnotationOut": "_content_559_OrderOrderAnnotationOut",
        "PriceIn": "_content_560_PriceIn",
        "PriceOut": "_content_561_PriceOut",
        "LocalinventoryCustomBatchRequestEntryIn": "_content_562_LocalinventoryCustomBatchRequestEntryIn",
        "LocalinventoryCustomBatchRequestEntryOut": "_content_563_LocalinventoryCustomBatchRequestEntryOut",
        "CustomerIn": "_content_564_CustomerIn",
        "CustomerOut": "_content_565_CustomerOut",
        "OrderLineItemProductIn": "_content_566_OrderLineItemProductIn",
        "OrderLineItemProductOut": "_content_567_OrderLineItemProductOut",
        "DatafeedFormatIn": "_content_568_DatafeedFormatIn",
        "DatafeedFormatOut": "_content_569_DatafeedFormatOut",
        "OrdersCancelRequestIn": "_content_570_OrdersCancelRequestIn",
        "OrdersCancelRequestOut": "_content_571_OrdersCancelRequestOut",
        "DatafeedTargetIn": "_content_572_DatafeedTargetIn",
        "DatafeedTargetOut": "_content_573_DatafeedTargetOut",
        "ListRegionsResponseIn": "_content_574_ListRegionsResponseIn",
        "ListRegionsResponseOut": "_content_575_ListRegionsResponseOut",
        "ProductShippingIn": "_content_576_ProductShippingIn",
        "ProductShippingOut": "_content_577_ProductShippingOut",
        "OrderLineItemAdjustmentIn": "_content_578_OrderLineItemAdjustmentIn",
        "OrderLineItemAdjustmentOut": "_content_579_OrderLineItemAdjustmentOut",
        "ShoppingAdsProgramStatusIn": "_content_580_ShoppingAdsProgramStatusIn",
        "ShoppingAdsProgramStatusOut": "_content_581_ShoppingAdsProgramStatusOut",
        "BusinessDayConfigIn": "_content_582_BusinessDayConfigIn",
        "BusinessDayConfigOut": "_content_583_BusinessDayConfigOut",
        "DatafeedsCustomBatchResponseIn": "_content_584_DatafeedsCustomBatchResponseIn",
        "DatafeedsCustomBatchResponseOut": "_content_585_DatafeedsCustomBatchResponseOut",
        "OrderLineItemShippingDetailsIn": "_content_586_OrderLineItemShippingDetailsIn",
        "OrderLineItemShippingDetailsOut": "_content_587_OrderLineItemShippingDetailsOut",
        "ProductDeliveryTimeAreaDeliveryTimeIn": "_content_588_ProductDeliveryTimeAreaDeliveryTimeIn",
        "ProductDeliveryTimeAreaDeliveryTimeOut": "_content_589_ProductDeliveryTimeAreaDeliveryTimeOut",
        "CustomerReturnReasonIn": "_content_590_CustomerReturnReasonIn",
        "CustomerReturnReasonOut": "_content_591_CustomerReturnReasonOut",
        "DatafeedstatusesCustomBatchRequestEntryIn": "_content_592_DatafeedstatusesCustomBatchRequestEntryIn",
        "DatafeedstatusesCustomBatchRequestEntryOut": "_content_593_DatafeedstatusesCustomBatchRequestEntryOut",
        "OrderreturnsLineItemIn": "_content_594_OrderreturnsLineItemIn",
        "OrderreturnsLineItemOut": "_content_595_OrderreturnsLineItemOut",
        "MerchantCenterDestinationIn": "_content_596_MerchantCenterDestinationIn",
        "MerchantCenterDestinationOut": "_content_597_MerchantCenterDestinationOut",
        "PromotionPromotionStatusIn": "_content_598_PromotionPromotionStatusIn",
        "PromotionPromotionStatusOut": "_content_599_PromotionPromotionStatusOut",
        "RepricingRuleReportIn": "_content_600_RepricingRuleReportIn",
        "RepricingRuleReportOut": "_content_601_RepricingRuleReportOut",
        "CarrierRateIn": "_content_602_CarrierRateIn",
        "CarrierRateOut": "_content_603_CarrierRateOut",
        "AmountIn": "_content_604_AmountIn",
        "AmountOut": "_content_605_AmountOut",
        "ShippingsettingsCustomBatchResponseIn": "_content_606_ShippingsettingsCustomBatchResponseIn",
        "ShippingsettingsCustomBatchResponseOut": "_content_607_ShippingsettingsCustomBatchResponseOut",
        "LiaInventorySettingsIn": "_content_608_LiaInventorySettingsIn",
        "LiaInventorySettingsOut": "_content_609_LiaInventorySettingsOut",
        "AccountsListLinksResponseIn": "_content_610_AccountsListLinksResponseIn",
        "AccountsListLinksResponseOut": "_content_611_AccountsListLinksResponseOut",
        "ListRepricingRulesResponseIn": "_content_612_ListRepricingRulesResponseIn",
        "ListRepricingRulesResponseOut": "_content_613_ListRepricingRulesResponseOut",
        "ProductStatusDestinationStatusIn": "_content_614_ProductStatusDestinationStatusIn",
        "ProductStatusDestinationStatusOut": "_content_615_ProductStatusDestinationStatusOut",
        "TestOrderPickupDetailsIn": "_content_616_TestOrderPickupDetailsIn",
        "TestOrderPickupDetailsOut": "_content_617_TestOrderPickupDetailsOut",
        "OrdersRefundOrderRequestIn": "_content_618_OrdersRefundOrderRequestIn",
        "OrdersRefundOrderRequestOut": "_content_619_OrdersRefundOrderRequestOut",
        "OrdersCancelTestOrderByCustomerRequestIn": "_content_620_OrdersCancelTestOrderByCustomerRequestIn",
        "OrdersCancelTestOrderByCustomerRequestOut": "_content_621_OrdersCancelTestOrderByCustomerRequestOut",
        "SettlementTransactionIn": "_content_622_SettlementTransactionIn",
        "SettlementTransactionOut": "_content_623_SettlementTransactionOut",
        "RepricingRuleReportBuyboxWinningRuleStatsIn": "_content_624_RepricingRuleReportBuyboxWinningRuleStatsIn",
        "RepricingRuleReportBuyboxWinningRuleStatsOut": "_content_625_RepricingRuleReportBuyboxWinningRuleStatsOut",
        "LiasettingsCustomBatchRequestEntryIn": "_content_626_LiasettingsCustomBatchRequestEntryIn",
        "LiasettingsCustomBatchRequestEntryOut": "_content_627_LiasettingsCustomBatchRequestEntryOut",
        "HolidayCutoffIn": "_content_628_HolidayCutoffIn",
        "HolidayCutoffOut": "_content_629_HolidayCutoffOut",
        "AccountsCustomBatchResponseEntryIn": "_content_630_AccountsCustomBatchResponseEntryIn",
        "AccountsCustomBatchResponseEntryOut": "_content_631_AccountsCustomBatchResponseEntryOut",
        "PosCustomBatchResponseIn": "_content_632_PosCustomBatchResponseIn",
        "PosCustomBatchResponseOut": "_content_633_PosCustomBatchResponseOut",
        "SettlementReportIn": "_content_634_SettlementReportIn",
        "SettlementReportOut": "_content_635_SettlementReportOut",
        "DatafeedsListResponseIn": "_content_636_DatafeedsListResponseIn",
        "DatafeedsListResponseOut": "_content_637_DatafeedsListResponseOut",
        "VerifyPhoneNumberResponseIn": "_content_638_VerifyPhoneNumberResponseIn",
        "VerifyPhoneNumberResponseOut": "_content_639_VerifyPhoneNumberResponseOut",
        "ProductIdIn": "_content_640_ProductIdIn",
        "ProductIdOut": "_content_641_ProductIdOut",
        "RecommendationDescriptionIn": "_content_642_RecommendationDescriptionIn",
        "RecommendationDescriptionOut": "_content_643_RecommendationDescriptionOut",
        "OrdersCreateTestReturnResponseIn": "_content_644_OrdersCreateTestReturnResponseIn",
        "OrdersCreateTestReturnResponseOut": "_content_645_OrdersCreateTestReturnResponseOut",
        "PosCustomBatchRequestEntryIn": "_content_646_PosCustomBatchRequestEntryIn",
        "PosCustomBatchRequestEntryOut": "_content_647_PosCustomBatchRequestEntryOut",
        "UndeleteConversionSourceRequestIn": "_content_648_UndeleteConversionSourceRequestIn",
        "UndeleteConversionSourceRequestOut": "_content_649_UndeleteConversionSourceRequestOut",
        "ConversionSourceIn": "_content_650_ConversionSourceIn",
        "ConversionSourceOut": "_content_651_ConversionSourceOut",
        "OrdersSetLineItemMetadataRequestIn": "_content_652_OrdersSetLineItemMetadataRequestIn",
        "OrdersSetLineItemMetadataRequestOut": "_content_653_OrdersSetLineItemMetadataRequestOut",
        "ProductstatusesCustomBatchRequestEntryIn": "_content_654_ProductstatusesCustomBatchRequestEntryIn",
        "ProductstatusesCustomBatchRequestEntryOut": "_content_655_ProductstatusesCustomBatchRequestEntryOut",
        "DatafeedStatusErrorIn": "_content_656_DatafeedStatusErrorIn",
        "DatafeedStatusErrorOut": "_content_657_DatafeedStatusErrorOut",
        "ReportInteractionRequestIn": "_content_658_ReportInteractionRequestIn",
        "ReportInteractionRequestOut": "_content_659_ReportInteractionRequestOut",
        "AccountsCustomBatchResponseIn": "_content_660_AccountsCustomBatchResponseIn",
        "AccountsCustomBatchResponseOut": "_content_661_AccountsCustomBatchResponseOut",
        "DatafeedstatusesCustomBatchResponseEntryIn": "_content_662_DatafeedstatusesCustomBatchResponseEntryIn",
        "DatafeedstatusesCustomBatchResponseEntryOut": "_content_663_DatafeedstatusesCustomBatchResponseEntryOut",
        "ReturnaddressListResponseIn": "_content_664_ReturnaddressListResponseIn",
        "ReturnaddressListResponseOut": "_content_665_ReturnaddressListResponseOut",
        "PosInventoryRequestIn": "_content_666_PosInventoryRequestIn",
        "PosInventoryRequestOut": "_content_667_PosInventoryRequestOut",
        "OrdersRejectReturnLineItemRequestIn": "_content_668_OrdersRejectReturnLineItemRequestIn",
        "OrdersRejectReturnLineItemRequestOut": "_content_669_OrdersRejectReturnLineItemRequestOut",
        "ProductDeliveryTimeAreaDeliveryTimeDeliveryTimeIn": "_content_670_ProductDeliveryTimeAreaDeliveryTimeDeliveryTimeIn",
        "ProductDeliveryTimeAreaDeliveryTimeDeliveryTimeOut": "_content_671_ProductDeliveryTimeAreaDeliveryTimeDeliveryTimeOut",
        "DatafeedsCustomBatchRequestIn": "_content_672_DatafeedsCustomBatchRequestIn",
        "DatafeedsCustomBatchRequestOut": "_content_673_DatafeedsCustomBatchRequestOut",
        "MonetaryAmountIn": "_content_674_MonetaryAmountIn",
        "MonetaryAmountOut": "_content_675_MonetaryAmountOut",
        "AccountTaxTaxRuleIn": "_content_676_AccountTaxTaxRuleIn",
        "AccountTaxTaxRuleOut": "_content_677_AccountTaxTaxRuleOut",
        "InstallmentIn": "_content_678_InstallmentIn",
        "InstallmentOut": "_content_679_InstallmentOut",
        "CustomerLoyaltyDataIn": "_content_680_CustomerLoyaltyDataIn",
        "CustomerLoyaltyDataOut": "_content_681_CustomerLoyaltyDataOut",
        "AccountstatusesCustomBatchResponseIn": "_content_682_AccountstatusesCustomBatchResponseIn",
        "AccountstatusesCustomBatchResponseOut": "_content_683_AccountstatusesCustomBatchResponseOut",
        "OrderCancellationIn": "_content_684_OrderCancellationIn",
        "OrderCancellationOut": "_content_685_OrderCancellationOut",
        "BestSellersIn": "_content_686_BestSellersIn",
        "BestSellersOut": "_content_687_BestSellersOut",
        "RateGroupIn": "_content_688_RateGroupIn",
        "RateGroupOut": "_content_689_RateGroupOut",
        "OrderReportDisbursementIn": "_content_690_OrderReportDisbursementIn",
        "OrderReportDisbursementOut": "_content_691_OrderReportDisbursementOut",
        "AccountsCustomBatchRequestEntryLinkRequestIn": "_content_692_AccountsCustomBatchRequestEntryLinkRequestIn",
        "AccountsCustomBatchRequestEntryLinkRequestOut": "_content_693_AccountsCustomBatchRequestEntryLinkRequestOut",
        "SettlementTransactionAmountCommissionIn": "_content_694_SettlementTransactionAmountCommissionIn",
        "SettlementTransactionAmountCommissionOut": "_content_695_SettlementTransactionAmountCommissionOut",
        "OrdersUpdateMerchantOrderIdResponseIn": "_content_696_OrdersUpdateMerchantOrderIdResponseIn",
        "OrdersUpdateMerchantOrderIdResponseOut": "_content_697_OrdersUpdateMerchantOrderIdResponseOut",
        "AccountItemUpdatesSettingsIn": "_content_698_AccountItemUpdatesSettingsIn",
        "AccountItemUpdatesSettingsOut": "_content_699_AccountItemUpdatesSettingsOut",
        "TransitTableTransitTimeRowTransitTimeValueIn": "_content_700_TransitTableTransitTimeRowTransitTimeValueIn",
        "TransitTableTransitTimeRowTransitTimeValueOut": "_content_701_TransitTableTransitTimeRowTransitTimeValueOut",
        "OnboardBuyOnGoogleProgramRequestIn": "_content_702_OnboardBuyOnGoogleProgramRequestIn",
        "OnboardBuyOnGoogleProgramRequestOut": "_content_703_OnboardBuyOnGoogleProgramRequestOut",
        "ShipmentInvoiceIn": "_content_704_ShipmentInvoiceIn",
        "ShipmentInvoiceOut": "_content_705_ShipmentInvoiceOut",
        "SettlementreportsListResponseIn": "_content_706_SettlementreportsListResponseIn",
        "SettlementreportsListResponseOut": "_content_707_SettlementreportsListResponseOut",
        "OrdersCancelLineItemResponseIn": "_content_708_OrdersCancelLineItemResponseIn",
        "OrdersCancelLineItemResponseOut": "_content_709_OrdersCancelLineItemResponseOut",
        "TestOrderIn": "_content_710_TestOrderIn",
        "TestOrderOut": "_content_711_TestOrderOut",
        "LiaSettingsIn": "_content_712_LiaSettingsIn",
        "LiaSettingsOut": "_content_713_LiaSettingsOut",
        "MerchantOrderReturnIn": "_content_714_MerchantOrderReturnIn",
        "MerchantOrderReturnOut": "_content_715_MerchantOrderReturnOut",
        "DatafeedIn": "_content_716_DatafeedIn",
        "DatafeedOut": "_content_717_DatafeedOut",
        "PromotionPromotionStatusPromotionIssueIn": "_content_718_PromotionPromotionStatusPromotionIssueIn",
        "PromotionPromotionStatusPromotionIssueOut": "_content_719_PromotionPromotionStatusPromotionIssueOut",
        "AccountStatusItemLevelIssueIn": "_content_720_AccountStatusItemLevelIssueIn",
        "AccountStatusItemLevelIssueOut": "_content_721_AccountStatusItemLevelIssueOut",
        "ReturnpolicyCustomBatchResponseEntryIn": "_content_722_ReturnpolicyCustomBatchResponseEntryIn",
        "ReturnpolicyCustomBatchResponseEntryOut": "_content_723_ReturnpolicyCustomBatchResponseEntryOut",
        "OrderreturnsProcessResponseIn": "_content_724_OrderreturnsProcessResponseIn",
        "OrderreturnsProcessResponseOut": "_content_725_OrderreturnsProcessResponseOut",
        "AccounttaxCustomBatchResponseEntryIn": "_content_726_AccounttaxCustomBatchResponseEntryIn",
        "AccounttaxCustomBatchResponseEntryOut": "_content_727_AccounttaxCustomBatchResponseEntryOut",
        "TableIn": "_content_728_TableIn",
        "TableOut": "_content_729_TableOut",
        "ProductTaxIn": "_content_730_ProductTaxIn",
        "ProductTaxOut": "_content_731_ProductTaxOut",
        "SearchResponseIn": "_content_732_SearchResponseIn",
        "SearchResponseOut": "_content_733_SearchResponseOut",
        "LocalInventoryIn": "_content_734_LocalInventoryIn",
        "LocalInventoryOut": "_content_735_LocalInventoryOut",
        "LinkServiceIn": "_content_736_LinkServiceIn",
        "LinkServiceOut": "_content_737_LinkServiceOut",
        "OrderreturnsAcknowledgeRequestIn": "_content_738_OrderreturnsAcknowledgeRequestIn",
        "OrderreturnsAcknowledgeRequestOut": "_content_739_OrderreturnsAcknowledgeRequestOut",
        "ListRepricingProductReportsResponseIn": "_content_740_ListRepricingProductReportsResponseIn",
        "ListRepricingProductReportsResponseOut": "_content_741_ListRepricingProductReportsResponseOut",
        "ReturnPolicyIn": "_content_742_ReturnPolicyIn",
        "ReturnPolicyOut": "_content_743_ReturnPolicyOut",
        "DatafeedsFetchNowResponseIn": "_content_744_DatafeedsFetchNowResponseIn",
        "DatafeedsFetchNowResponseOut": "_content_745_DatafeedsFetchNowResponseOut",
        "OrderAddressIn": "_content_746_OrderAddressIn",
        "OrderAddressOut": "_content_747_OrderAddressOut",
        "FreeListingsProgramStatusReviewIneligibilityReasonDetailsIn": "_content_748_FreeListingsProgramStatusReviewIneligibilityReasonDetailsIn",
        "FreeListingsProgramStatusReviewIneligibilityReasonDetailsOut": "_content_749_FreeListingsProgramStatusReviewIneligibilityReasonDetailsOut",
        "ReturnShipmentIn": "_content_750_ReturnShipmentIn",
        "ReturnShipmentOut": "_content_751_ReturnShipmentOut",
        "DatafeedsCustomBatchRequestEntryIn": "_content_752_DatafeedsCustomBatchRequestEntryIn",
        "DatafeedsCustomBatchRequestEntryOut": "_content_753_DatafeedsCustomBatchRequestEntryOut",
        "ReturnpolicyCustomBatchRequestEntryIn": "_content_754_ReturnpolicyCustomBatchRequestEntryIn",
        "ReturnpolicyCustomBatchRequestEntryOut": "_content_755_ReturnpolicyCustomBatchRequestEntryOut",
        "LiasettingsSetPosDataProviderResponseIn": "_content_756_LiasettingsSetPosDataProviderResponseIn",
        "LiasettingsSetPosDataProviderResponseOut": "_content_757_LiasettingsSetPosDataProviderResponseOut",
        "ProductStatusIn": "_content_758_ProductStatusIn",
        "ProductStatusOut": "_content_759_ProductStatusOut",
        "LiaAboutPageSettingsIn": "_content_760_LiaAboutPageSettingsIn",
        "LiaAboutPageSettingsOut": "_content_761_LiaAboutPageSettingsOut",
        "OrdersGetTestOrderTemplateResponseIn": "_content_762_OrdersGetTestOrderTemplateResponseIn",
        "OrdersGetTestOrderTemplateResponseOut": "_content_763_OrdersGetTestOrderTemplateResponseOut",
        "AccountYouTubeChannelLinkIn": "_content_764_AccountYouTubeChannelLinkIn",
        "AccountYouTubeChannelLinkOut": "_content_765_AccountYouTubeChannelLinkOut",
        "LiasettingsListResponseIn": "_content_766_LiasettingsListResponseIn",
        "LiasettingsListResponseOut": "_content_767_LiasettingsListResponseOut",
        "RegionalinventoryCustomBatchRequestIn": "_content_768_RegionalinventoryCustomBatchRequestIn",
        "RegionalinventoryCustomBatchRequestOut": "_content_769_RegionalinventoryCustomBatchRequestOut",
        "AccountShippingImprovementsIn": "_content_770_AccountShippingImprovementsIn",
        "AccountShippingImprovementsOut": "_content_771_AccountShippingImprovementsOut",
        "LiasettingsCustomBatchResponseEntryIn": "_content_772_LiasettingsCustomBatchResponseEntryIn",
        "LiasettingsCustomBatchResponseEntryOut": "_content_773_LiasettingsCustomBatchResponseEntryOut",
        "ReturnPricingInfoIn": "_content_774_ReturnPricingInfoIn",
        "ReturnPricingInfoOut": "_content_775_ReturnPricingInfoOut",
        "OrderMerchantProvidedAnnotationIn": "_content_776_OrderMerchantProvidedAnnotationIn",
        "OrderMerchantProvidedAnnotationOut": "_content_777_OrderMerchantProvidedAnnotationOut",
        "RepricingProductReportBuyboxWinningProductStatsIn": "_content_778_RepricingProductReportBuyboxWinningProductStatsIn",
        "RepricingProductReportBuyboxWinningProductStatsOut": "_content_779_RepricingProductReportBuyboxWinningProductStatsOut",
        "ProductSubscriptionCostIn": "_content_780_ProductSubscriptionCostIn",
        "ProductSubscriptionCostOut": "_content_781_ProductSubscriptionCostOut",
        "ReportRowIn": "_content_782_ReportRowIn",
        "ReportRowOut": "_content_783_ReportRowOut",
        "OrderinvoicesCustomBatchRequestEntryCreateRefundInvoiceReturnOptionIn": "_content_784_OrderinvoicesCustomBatchRequestEntryCreateRefundInvoiceReturnOptionIn",
        "OrderinvoicesCustomBatchRequestEntryCreateRefundInvoiceReturnOptionOut": "_content_785_OrderinvoicesCustomBatchRequestEntryCreateRefundInvoiceReturnOptionOut",
        "MinimumOrderValueTableStoreCodeSetWithMovIn": "_content_786_MinimumOrderValueTableStoreCodeSetWithMovIn",
        "MinimumOrderValueTableStoreCodeSetWithMovOut": "_content_787_MinimumOrderValueTableStoreCodeSetWithMovOut",
        "OrderDeliveryDetailsIn": "_content_788_OrderDeliveryDetailsIn",
        "OrderDeliveryDetailsOut": "_content_789_OrderDeliveryDetailsOut",
        "AccountstatusesCustomBatchResponseEntryIn": "_content_790_AccountstatusesCustomBatchResponseEntryIn",
        "AccountstatusesCustomBatchResponseEntryOut": "_content_791_AccountstatusesCustomBatchResponseEntryOut",
        "AccountsUpdateLabelsRequestIn": "_content_792_AccountsUpdateLabelsRequestIn",
        "AccountsUpdateLabelsRequestOut": "_content_793_AccountsUpdateLabelsRequestOut",
        "LiasettingsCustomBatchRequestIn": "_content_794_LiasettingsCustomBatchRequestIn",
        "LiasettingsCustomBatchRequestOut": "_content_795_LiasettingsCustomBatchRequestOut",
        "ReturnPolicyOnlineIn": "_content_796_ReturnPolicyOnlineIn",
        "ReturnPolicyOnlineOut": "_content_797_ReturnPolicyOnlineOut",
        "OrderreturnsRefundOperationIn": "_content_798_OrderreturnsRefundOperationIn",
        "OrderreturnsRefundOperationOut": "_content_799_OrderreturnsRefundOperationOut",
        "ProductViewIn": "_content_800_ProductViewIn",
        "ProductViewOut": "_content_801_ProductViewOut",
        "RepricingRuleEligibleOfferMatcherIn": "_content_802_RepricingRuleEligibleOfferMatcherIn",
        "RepricingRuleEligibleOfferMatcherOut": "_content_803_RepricingRuleEligibleOfferMatcherOut",
        "CollectionFeaturedProductIn": "_content_804_CollectionFeaturedProductIn",
        "CollectionFeaturedProductOut": "_content_805_CollectionFeaturedProductOut",
        "AccountLabelIn": "_content_806_AccountLabelIn",
        "AccountLabelOut": "_content_807_AccountLabelOut",
        "ShippingsettingsGetSupportedCarriersResponseIn": "_content_808_ShippingsettingsGetSupportedCarriersResponseIn",
        "ShippingsettingsGetSupportedCarriersResponseOut": "_content_809_ShippingsettingsGetSupportedCarriersResponseOut",
        "AccountsClaimWebsiteResponseIn": "_content_810_AccountsClaimWebsiteResponseIn",
        "AccountsClaimWebsiteResponseOut": "_content_811_AccountsClaimWebsiteResponseOut",
        "ReturnaddressCustomBatchResponseEntryIn": "_content_812_ReturnaddressCustomBatchResponseEntryIn",
        "ReturnaddressCustomBatchResponseEntryOut": "_content_813_ReturnaddressCustomBatchResponseEntryOut",
        "OrdersCustomBatchRequestEntryShipLineItemsShipmentInfoIn": "_content_814_OrdersCustomBatchRequestEntryShipLineItemsShipmentInfoIn",
        "OrdersCustomBatchRequestEntryShipLineItemsShipmentInfoOut": "_content_815_OrdersCustomBatchRequestEntryShipLineItemsShipmentInfoOut",
        "UnitInvoiceIn": "_content_816_UnitInvoiceIn",
        "UnitInvoiceOut": "_content_817_UnitInvoiceOut",
        "RepricingRuleStatsBasedRuleIn": "_content_818_RepricingRuleStatsBasedRuleIn",
        "RepricingRuleStatsBasedRuleOut": "_content_819_RepricingRuleStatsBasedRuleOut",
        "CustomAttributeIn": "_content_820_CustomAttributeIn",
        "CustomAttributeOut": "_content_821_CustomAttributeOut",
        "ReturnPolicyOnlineReturnShippingFeeIn": "_content_822_ReturnPolicyOnlineReturnShippingFeeIn",
        "ReturnPolicyOnlineReturnShippingFeeOut": "_content_823_ReturnPolicyOnlineReturnShippingFeeOut",
        "OrderreturnsListResponseIn": "_content_824_OrderreturnsListResponseIn",
        "OrderreturnsListResponseOut": "_content_825_OrderreturnsListResponseOut",
        "ListCollectionStatusesResponseIn": "_content_826_ListCollectionStatusesResponseIn",
        "ListCollectionStatusesResponseOut": "_content_827_ListCollectionStatusesResponseOut",
        "OrderTrackingSignalIn": "_content_828_OrderTrackingSignalIn",
        "OrderTrackingSignalOut": "_content_829_OrderTrackingSignalOut",
        "AccountstatusesListResponseIn": "_content_830_AccountstatusesListResponseIn",
        "AccountstatusesListResponseOut": "_content_831_AccountstatusesListResponseOut",
        "AccounttaxCustomBatchResponseIn": "_content_832_AccounttaxCustomBatchResponseIn",
        "AccounttaxCustomBatchResponseOut": "_content_833_AccounttaxCustomBatchResponseOut",
        "RepricingRuleEffectiveTimeIn": "_content_834_RepricingRuleEffectiveTimeIn",
        "RepricingRuleEffectiveTimeOut": "_content_835_RepricingRuleEffectiveTimeOut",
        "CloudExportAdditionalPropertiesIn": "_content_836_CloudExportAdditionalPropertiesIn",
        "CloudExportAdditionalPropertiesOut": "_content_837_CloudExportAdditionalPropertiesOut",
        "OrderIn": "_content_838_OrderIn",
        "OrderOut": "_content_839_OrderOut",
        "ErrorIn": "_content_840_ErrorIn",
        "ErrorOut": "_content_841_ErrorOut",
        "InvoiceSummaryIn": "_content_842_InvoiceSummaryIn",
        "InvoiceSummaryOut": "_content_843_InvoiceSummaryOut",
        "LiasettingsListPosDataProvidersResponseIn": "_content_844_LiasettingsListPosDataProvidersResponseIn",
        "LiasettingsListPosDataProvidersResponseOut": "_content_845_LiasettingsListPosDataProvidersResponseOut",
        "CollectionIn": "_content_846_CollectionIn",
        "CollectionOut": "_content_847_CollectionOut",
        "WarehouseIn": "_content_848_WarehouseIn",
        "WarehouseOut": "_content_849_WarehouseOut",
        "PosDataProvidersPosDataProviderIn": "_content_850_PosDataProvidersPosDataProviderIn",
        "PosDataProvidersPosDataProviderOut": "_content_851_PosDataProvidersPosDataProviderOut",
        "OrdersCreateTestReturnRequestIn": "_content_852_OrdersCreateTestReturnRequestIn",
        "OrdersCreateTestReturnRequestOut": "_content_853_OrdersCreateTestReturnRequestOut",
        "MerchantRejectionReasonIn": "_content_854_MerchantRejectionReasonIn",
        "MerchantRejectionReasonOut": "_content_855_MerchantRejectionReasonOut",
        "AccountGoogleMyBusinessLinkIn": "_content_856_AccountGoogleMyBusinessLinkIn",
        "AccountGoogleMyBusinessLinkOut": "_content_857_AccountGoogleMyBusinessLinkOut",
        "GoogleAnalyticsLinkIn": "_content_858_GoogleAnalyticsLinkIn",
        "GoogleAnalyticsLinkOut": "_content_859_GoogleAnalyticsLinkOut",
        "ProductsCustomBatchResponseEntryIn": "_content_860_ProductsCustomBatchResponseEntryIn",
        "ProductsCustomBatchResponseEntryOut": "_content_861_ProductsCustomBatchResponseEntryOut",
        "LiasettingsRequestInventoryVerificationResponseIn": "_content_862_LiasettingsRequestInventoryVerificationResponseIn",
        "LiasettingsRequestInventoryVerificationResponseOut": "_content_863_LiasettingsRequestInventoryVerificationResponseOut",
        "OrderReportTransactionIn": "_content_864_OrderReportTransactionIn",
        "OrderReportTransactionOut": "_content_865_OrderReportTransactionOut",
        "DatafeedStatusIn": "_content_866_DatafeedStatusIn",
        "DatafeedStatusOut": "_content_867_DatafeedStatusOut",
        "TimeZoneIn": "_content_868_TimeZoneIn",
        "TimeZoneOut": "_content_869_TimeZoneOut",
        "OrderReturnIn": "_content_870_OrderReturnIn",
        "OrderReturnOut": "_content_871_OrderReturnOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["RequestPhoneVerificationRequestIn"] = t.struct(
        {
            "phoneRegionCode": t.string(),
            "phoneNumber": t.string().optional(),
            "phoneVerificationMethod": t.string().optional(),
            "languageCode": t.string().optional(),
        }
    ).named(renames["RequestPhoneVerificationRequestIn"])
    types["RequestPhoneVerificationRequestOut"] = t.struct(
        {
            "phoneRegionCode": t.string(),
            "phoneNumber": t.string().optional(),
            "phoneVerificationMethod": t.string().optional(),
            "languageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestPhoneVerificationRequestOut"])
    types["PosSaleIn"] = t.struct(
        {
            "timestamp": t.string(),
            "contentLanguage": t.string(),
            "targetCountry": t.string(),
            "price": t.proxy(renames["PriceIn"]),
            "saleId": t.string().optional(),
            "quantity": t.string(),
            "gtin": t.string().optional(),
            "itemId": t.string(),
            "storeCode": t.string(),
            "kind": t.string().optional(),
        }
    ).named(renames["PosSaleIn"])
    types["PosSaleOut"] = t.struct(
        {
            "timestamp": t.string(),
            "contentLanguage": t.string(),
            "targetCountry": t.string(),
            "price": t.proxy(renames["PriceOut"]),
            "saleId": t.string().optional(),
            "quantity": t.string(),
            "gtin": t.string().optional(),
            "itemId": t.string(),
            "storeCode": t.string(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PosSaleOut"])
    types["MerchantOrderReturnItemIn"] = t.struct(
        {
            "product": t.proxy(renames["OrderLineItemProductIn"]).optional(),
            "merchantReturnReason": t.proxy(renames["RefundReasonIn"]).optional(),
            "merchantRejectionReason": t.proxy(
                renames["MerchantRejectionReasonIn"]
            ).optional(),
            "state": t.string().optional(),
            "customerReturnReason": t.proxy(
                renames["CustomerReturnReasonIn"]
            ).optional(),
            "shipmentUnitId": t.string().optional(),
            "returnShipmentIds": t.array(t.string()).optional(),
            "returnItemId": t.string().optional(),
            "refundableAmount": t.proxy(renames["MonetaryAmountIn"]).optional(),
            "shipmentGroupId": t.string().optional(),
            "itemId": t.string().optional(),
        }
    ).named(renames["MerchantOrderReturnItemIn"])
    types["MerchantOrderReturnItemOut"] = t.struct(
        {
            "product": t.proxy(renames["OrderLineItemProductOut"]).optional(),
            "merchantReturnReason": t.proxy(renames["RefundReasonOut"]).optional(),
            "merchantRejectionReason": t.proxy(
                renames["MerchantRejectionReasonOut"]
            ).optional(),
            "state": t.string().optional(),
            "customerReturnReason": t.proxy(
                renames["CustomerReturnReasonOut"]
            ).optional(),
            "shipmentUnitId": t.string().optional(),
            "returnShipmentIds": t.array(t.string()).optional(),
            "returnItemId": t.string().optional(),
            "refundableAmount": t.proxy(renames["MonetaryAmountOut"]).optional(),
            "shipmentGroupId": t.string().optional(),
            "itemId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MerchantOrderReturnItemOut"])
    types["CollectionStatusIn"] = t.struct(
        {
            "creationDate": t.string().optional(),
            "lastUpdateDate": t.string().optional(),
            "destinationStatuses": t.array(
                t.proxy(renames["CollectionStatusDestinationStatusIn"])
            ).optional(),
            "id": t.string(),
            "collectionLevelIssuses": t.array(
                t.proxy(renames["CollectionStatusItemLevelIssueIn"])
            ).optional(),
        }
    ).named(renames["CollectionStatusIn"])
    types["CollectionStatusOut"] = t.struct(
        {
            "creationDate": t.string().optional(),
            "lastUpdateDate": t.string().optional(),
            "destinationStatuses": t.array(
                t.proxy(renames["CollectionStatusDestinationStatusOut"])
            ).optional(),
            "id": t.string(),
            "collectionLevelIssuses": t.array(
                t.proxy(renames["CollectionStatusItemLevelIssueOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CollectionStatusOut"])
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
    types["AccountAdsLinkIn"] = t.struct(
        {"status": t.string().optional(), "adsId": t.string().optional()}
    ).named(renames["AccountAdsLinkIn"])
    types["AccountAdsLinkOut"] = t.struct(
        {
            "status": t.string().optional(),
            "adsId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountAdsLinkOut"])
    types["OrderLineItemIn"] = t.struct(
        {
            "quantityPending": t.integer().optional(),
            "shippingDetails": t.proxy(
                renames["OrderLineItemShippingDetailsIn"]
            ).optional(),
            "quantityShipped": t.integer().optional(),
            "quantityDelivered": t.integer().optional(),
            "returns": t.array(t.proxy(renames["OrderReturnIn"])).optional(),
            "annotations": t.array(
                t.proxy(renames["OrderMerchantProvidedAnnotationIn"])
            ).optional(),
            "returnInfo": t.proxy(renames["OrderLineItemReturnInfoIn"]).optional(),
            "adjustments": t.array(
                t.proxy(renames["OrderLineItemAdjustmentIn"])
            ).optional(),
            "id": t.string().optional(),
            "quantityReadyForPickup": t.integer().optional(),
            "quantityOrdered": t.integer().optional(),
            "quantityUndeliverable": t.integer().optional(),
            "quantityCanceled": t.integer().optional(),
            "cancellations": t.array(
                t.proxy(renames["OrderCancellationIn"])
            ).optional(),
            "quantityReturned": t.integer().optional(),
            "product": t.proxy(renames["OrderLineItemProductIn"]).optional(),
            "tax": t.proxy(renames["PriceIn"]).optional(),
            "price": t.proxy(renames["PriceIn"]).optional(),
        }
    ).named(renames["OrderLineItemIn"])
    types["OrderLineItemOut"] = t.struct(
        {
            "quantityPending": t.integer().optional(),
            "shippingDetails": t.proxy(
                renames["OrderLineItemShippingDetailsOut"]
            ).optional(),
            "quantityShipped": t.integer().optional(),
            "quantityDelivered": t.integer().optional(),
            "returns": t.array(t.proxy(renames["OrderReturnOut"])).optional(),
            "annotations": t.array(
                t.proxy(renames["OrderMerchantProvidedAnnotationOut"])
            ).optional(),
            "returnInfo": t.proxy(renames["OrderLineItemReturnInfoOut"]).optional(),
            "adjustments": t.array(
                t.proxy(renames["OrderLineItemAdjustmentOut"])
            ).optional(),
            "id": t.string().optional(),
            "quantityReadyForPickup": t.integer().optional(),
            "quantityOrdered": t.integer().optional(),
            "quantityUndeliverable": t.integer().optional(),
            "quantityCanceled": t.integer().optional(),
            "cancellations": t.array(
                t.proxy(renames["OrderCancellationOut"])
            ).optional(),
            "quantityReturned": t.integer().optional(),
            "product": t.proxy(renames["OrderLineItemProductOut"]).optional(),
            "tax": t.proxy(renames["PriceOut"]).optional(),
            "price": t.proxy(renames["PriceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderLineItemOut"])
    types["CarriersCarrierIn"] = t.struct(
        {
            "country": t.string().optional(),
            "eddServices": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "services": t.array(t.string()).optional(),
        }
    ).named(renames["CarriersCarrierIn"])
    types["CarriersCarrierOut"] = t.struct(
        {
            "country": t.string().optional(),
            "eddServices": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "services": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CarriersCarrierOut"])
    types["ShipmentInvoiceLineItemInvoiceIn"] = t.struct(
        {
            "lineItemId": t.string().optional(),
            "unitInvoice": t.proxy(renames["UnitInvoiceIn"]).optional(),
            "shipmentUnitIds": t.array(t.string()).optional(),
            "productId": t.string().optional(),
        }
    ).named(renames["ShipmentInvoiceLineItemInvoiceIn"])
    types["ShipmentInvoiceLineItemInvoiceOut"] = t.struct(
        {
            "lineItemId": t.string().optional(),
            "unitInvoice": t.proxy(renames["UnitInvoiceOut"]).optional(),
            "shipmentUnitIds": t.array(t.string()).optional(),
            "productId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShipmentInvoiceLineItemInvoiceOut"])
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
    types["AccountIdentifierIn"] = t.struct(
        {"merchantId": t.string().optional(), "aggregatorId": t.string().optional()}
    ).named(renames["AccountIdentifierIn"])
    types["AccountIdentifierOut"] = t.struct(
        {
            "merchantId": t.string().optional(),
            "aggregatorId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountIdentifierOut"])
    types["CaptureOrderResponseIn"] = t.struct(
        {"executionStatus": t.string().optional()}
    ).named(renames["CaptureOrderResponseIn"])
    types["CaptureOrderResponseOut"] = t.struct(
        {
            "executionStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CaptureOrderResponseOut"])
    types["TestOrderPickupDetailsPickupPersonIn"] = t.struct(
        {"phoneNumber": t.string(), "name": t.string()}
    ).named(renames["TestOrderPickupDetailsPickupPersonIn"])
    types["TestOrderPickupDetailsPickupPersonOut"] = t.struct(
        {
            "phoneNumber": t.string(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestOrderPickupDetailsPickupPersonOut"])
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
    types["OrderreportsListTransactionsResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "transactions": t.array(
                t.proxy(renames["OrderReportTransactionIn"])
            ).optional(),
        }
    ).named(renames["OrderreportsListTransactionsResponseIn"])
    types["OrderreportsListTransactionsResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "transactions": t.array(
                t.proxy(renames["OrderReportTransactionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderreportsListTransactionsResponseOut"])
    types["ReturnaddressCustomBatchRequestEntryIn"] = t.struct(
        {
            "method": t.string().optional(),
            "returnAddress": t.proxy(renames["ReturnAddressIn"]).optional(),
            "batchId": t.integer().optional(),
            "merchantId": t.string().optional(),
            "returnAddressId": t.string().optional(),
        }
    ).named(renames["ReturnaddressCustomBatchRequestEntryIn"])
    types["ReturnaddressCustomBatchRequestEntryOut"] = t.struct(
        {
            "method": t.string().optional(),
            "returnAddress": t.proxy(renames["ReturnAddressOut"]).optional(),
            "batchId": t.integer().optional(),
            "merchantId": t.string().optional(),
            "returnAddressId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReturnaddressCustomBatchRequestEntryOut"])
    types["ListCollectionsResponseIn"] = t.struct(
        {
            "resources": t.array(t.proxy(renames["CollectionIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListCollectionsResponseIn"])
    types["ListCollectionsResponseOut"] = t.struct(
        {
            "resources": t.array(t.proxy(renames["CollectionOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCollectionsResponseOut"])
    types["ProductViewItemIssueIn"] = t.struct(
        {
            "severity": t.proxy(
                renames["ProductViewItemIssueItemIssueSeverityIn"]
            ).optional(),
            "resolution": t.string().optional(),
            "issueType": t.proxy(
                renames["ProductViewItemIssueItemIssueTypeIn"]
            ).optional(),
        }
    ).named(renames["ProductViewItemIssueIn"])
    types["ProductViewItemIssueOut"] = t.struct(
        {
            "severity": t.proxy(
                renames["ProductViewItemIssueItemIssueSeverityOut"]
            ).optional(),
            "resolution": t.string().optional(),
            "issueType": t.proxy(
                renames["ProductViewItemIssueItemIssueTypeOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductViewItemIssueOut"])
    types["RecommendationIn"] = t.struct(
        {
            "title": t.string().optional(),
            "recommendationName": t.string().optional(),
            "defaultDescription": t.string().optional(),
            "numericalImpact": t.integer().optional(),
            "defaultCallToAction": t.proxy(
                renames["RecommendationCallToActionIn"]
            ).optional(),
            "paid": t.boolean().optional(),
            "subType": t.string().optional(),
        }
    ).named(renames["RecommendationIn"])
    types["RecommendationOut"] = t.struct(
        {
            "additionalDescriptions": t.array(
                t.proxy(renames["RecommendationDescriptionOut"])
            ).optional(),
            "title": t.string().optional(),
            "recommendationName": t.string().optional(),
            "defaultDescription": t.string().optional(),
            "numericalImpact": t.integer().optional(),
            "defaultCallToAction": t.proxy(
                renames["RecommendationCallToActionOut"]
            ).optional(),
            "paid": t.boolean().optional(),
            "additionalCallToAction": t.array(
                t.proxy(renames["RecommendationCallToActionOut"])
            ).optional(),
            "creative": t.array(
                t.proxy(renames["RecommendationCreativeOut"])
            ).optional(),
            "subType": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RecommendationOut"])
    types["ReturnpolicyListResponseIn"] = t.struct(
        {
            "resources": t.array(t.proxy(renames["ReturnPolicyIn"])),
            "kind": t.string().optional(),
        }
    ).named(renames["ReturnpolicyListResponseIn"])
    types["ReturnpolicyListResponseOut"] = t.struct(
        {
            "resources": t.array(t.proxy(renames["ReturnPolicyOut"])),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReturnpolicyListResponseOut"])
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
    types["SettlementTransactionAmountIn"] = t.struct(
        {
            "description": t.string().optional(),
            "transactionAmount": t.proxy(renames["PriceIn"]).optional(),
            "type": t.string().optional(),
            "commission": t.proxy(renames["SettlementTransactionAmountCommissionIn"]),
        }
    ).named(renames["SettlementTransactionAmountIn"])
    types["SettlementTransactionAmountOut"] = t.struct(
        {
            "description": t.string().optional(),
            "transactionAmount": t.proxy(renames["PriceOut"]).optional(),
            "type": t.string().optional(),
            "commission": t.proxy(renames["SettlementTransactionAmountCommissionOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SettlementTransactionAmountOut"])
    types["AccountStatusStatisticsIn"] = t.struct(
        {
            "expiring": t.string().optional(),
            "disapproved": t.string().optional(),
            "pending": t.string().optional(),
            "active": t.string().optional(),
        }
    ).named(renames["AccountStatusStatisticsIn"])
    types["AccountStatusStatisticsOut"] = t.struct(
        {
            "expiring": t.string().optional(),
            "disapproved": t.string().optional(),
            "pending": t.string().optional(),
            "active": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountStatusStatisticsOut"])
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
    types["SettlementTransactionTransactionIn"] = t.struct(
        {"type": t.string().optional(), "postDate": t.string().optional()}
    ).named(renames["SettlementTransactionTransactionIn"])
    types["SettlementTransactionTransactionOut"] = t.struct(
        {
            "type": t.string().optional(),
            "postDate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SettlementTransactionTransactionOut"])
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
    types["LiasettingsCustomBatchResponseIn"] = t.struct(
        {
            "entries": t.array(
                t.proxy(renames["LiasettingsCustomBatchResponseEntryIn"])
            ).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["LiasettingsCustomBatchResponseIn"])
    types["LiasettingsCustomBatchResponseOut"] = t.struct(
        {
            "entries": t.array(
                t.proxy(renames["LiasettingsCustomBatchResponseEntryOut"])
            ).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiasettingsCustomBatchResponseOut"])
    types["ShoppingAdsProgramStatusReviewIneligibilityReasonDetailsIn"] = t.struct(
        {"cooldownTime": t.string().optional()}
    ).named(renames["ShoppingAdsProgramStatusReviewIneligibilityReasonDetailsIn"])
    types["ShoppingAdsProgramStatusReviewIneligibilityReasonDetailsOut"] = t.struct(
        {
            "cooldownTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShoppingAdsProgramStatusReviewIneligibilityReasonDetailsOut"])
    types["AccountTaxIn"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["AccountTaxTaxRuleIn"])).optional(),
            "accountId": t.string(),
            "kind": t.string().optional(),
        }
    ).named(renames["AccountTaxIn"])
    types["AccountTaxOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["AccountTaxTaxRuleOut"])).optional(),
            "accountId": t.string(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountTaxOut"])
    types["LocationIdSetIn"] = t.struct(
        {"locationIds": t.array(t.string()).optional()}
    ).named(renames["LocationIdSetIn"])
    types["LocationIdSetOut"] = t.struct(
        {
            "locationIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationIdSetOut"])
    types["OrderLineItemReturnInfoIn"] = t.struct(
        {
            "daysToReturn": t.integer(),
            "policyUrl": t.string(),
            "isReturnable": t.boolean(),
        }
    ).named(renames["OrderLineItemReturnInfoIn"])
    types["OrderLineItemReturnInfoOut"] = t.struct(
        {
            "daysToReturn": t.integer(),
            "policyUrl": t.string(),
            "isReturnable": t.boolean(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderLineItemReturnInfoOut"])
    types["AccountAddressIn"] = t.struct(
        {
            "postalCode": t.string().optional(),
            "locality": t.string().optional(),
            "region": t.string().optional(),
            "streetAddress": t.string().optional(),
            "country": t.string().optional(),
        }
    ).named(renames["AccountAddressIn"])
    types["AccountAddressOut"] = t.struct(
        {
            "postalCode": t.string().optional(),
            "locality": t.string().optional(),
            "region": t.string().optional(),
            "streetAddress": t.string().optional(),
            "country": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountAddressOut"])
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
    types["OrderPickupDetailsIn"] = t.struct(
        {
            "collectors": t.array(
                t.proxy(renames["OrderPickupDetailsCollectorIn"])
            ).optional(),
            "pickupType": t.string().optional(),
            "address": t.proxy(renames["OrderAddressIn"]).optional(),
            "locationId": t.string().optional(),
        }
    ).named(renames["OrderPickupDetailsIn"])
    types["OrderPickupDetailsOut"] = t.struct(
        {
            "collectors": t.array(
                t.proxy(renames["OrderPickupDetailsCollectorOut"])
            ).optional(),
            "pickupType": t.string().optional(),
            "address": t.proxy(renames["OrderAddressOut"]).optional(),
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderPickupDetailsOut"])
    types["PosSaleRequestIn"] = t.struct(
        {
            "gtin": t.string().optional(),
            "contentLanguage": t.string(),
            "storeCode": t.string(),
            "quantity": t.string(),
            "saleId": t.string().optional(),
            "timestamp": t.string(),
            "targetCountry": t.string(),
            "itemId": t.string(),
            "price": t.proxy(renames["PriceIn"]),
        }
    ).named(renames["PosSaleRequestIn"])
    types["PosSaleRequestOut"] = t.struct(
        {
            "gtin": t.string().optional(),
            "contentLanguage": t.string(),
            "storeCode": t.string(),
            "quantity": t.string(),
            "saleId": t.string().optional(),
            "timestamp": t.string(),
            "targetCountry": t.string(),
            "itemId": t.string(),
            "price": t.proxy(renames["PriceOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PosSaleRequestOut"])
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
    types["OrdersShipLineItemsRequestIn"] = t.struct(
        {
            "shipmentInfos": t.array(
                t.proxy(
                    renames["OrdersCustomBatchRequestEntryShipLineItemsShipmentInfoIn"]
                )
            ).optional(),
            "shipmentGroupId": t.string().optional(),
            "lineItems": t.array(
                t.proxy(renames["OrderShipmentLineItemShipmentIn"])
            ).optional(),
            "operationId": t.string().optional(),
        }
    ).named(renames["OrdersShipLineItemsRequestIn"])
    types["OrdersShipLineItemsRequestOut"] = t.struct(
        {
            "shipmentInfos": t.array(
                t.proxy(
                    renames["OrdersCustomBatchRequestEntryShipLineItemsShipmentInfoOut"]
                )
            ).optional(),
            "shipmentGroupId": t.string().optional(),
            "lineItems": t.array(
                t.proxy(renames["OrderShipmentLineItemShipmentOut"])
            ).optional(),
            "operationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersShipLineItemsRequestOut"])
    types["RepricingProductReportIn"] = t.struct(
        {
            "totalGmv": t.proxy(renames["PriceAmountIn"]).optional(),
            "lowWatermark": t.proxy(renames["PriceAmountIn"]).optional(),
            "inapplicabilityDetails": t.array(
                t.proxy(renames["InapplicabilityDetailsIn"])
            ).optional(),
            "applicationCount": t.string().optional(),
            "highWatermark": t.proxy(renames["PriceAmountIn"]).optional(),
            "orderItemCount": t.integer().optional(),
            "buyboxWinningProductStats": t.proxy(
                renames["RepricingProductReportBuyboxWinningProductStatsIn"]
            ).optional(),
            "date": t.proxy(renames["DateIn"]).optional(),
            "type": t.string().optional(),
            "ruleIds": t.array(t.string()).optional(),
        }
    ).named(renames["RepricingProductReportIn"])
    types["RepricingProductReportOut"] = t.struct(
        {
            "totalGmv": t.proxy(renames["PriceAmountOut"]).optional(),
            "lowWatermark": t.proxy(renames["PriceAmountOut"]).optional(),
            "inapplicabilityDetails": t.array(
                t.proxy(renames["InapplicabilityDetailsOut"])
            ).optional(),
            "applicationCount": t.string().optional(),
            "highWatermark": t.proxy(renames["PriceAmountOut"]).optional(),
            "orderItemCount": t.integer().optional(),
            "buyboxWinningProductStats": t.proxy(
                renames["RepricingProductReportBuyboxWinningProductStatsOut"]
            ).optional(),
            "date": t.proxy(renames["DateOut"]).optional(),
            "type": t.string().optional(),
            "ruleIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepricingProductReportOut"])
    types["OrdersGetByMerchantOrderIdResponseIn"] = t.struct(
        {"kind": t.string().optional(), "order": t.proxy(renames["OrderIn"]).optional()}
    ).named(renames["OrdersGetByMerchantOrderIdResponseIn"])
    types["OrdersGetByMerchantOrderIdResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "order": t.proxy(renames["OrderOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersGetByMerchantOrderIdResponseOut"])
    types["ReturnAddressAddressIn"] = t.struct(
        {
            "locality": t.string().optional(),
            "country": t.string().optional(),
            "region": t.string().optional(),
            "recipientName": t.string().optional(),
            "streetAddress": t.array(t.string()).optional(),
            "postalCode": t.string().optional(),
        }
    ).named(renames["ReturnAddressAddressIn"])
    types["ReturnAddressAddressOut"] = t.struct(
        {
            "locality": t.string().optional(),
            "country": t.string().optional(),
            "region": t.string().optional(),
            "recipientName": t.string().optional(),
            "streetAddress": t.array(t.string()).optional(),
            "postalCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReturnAddressAddressOut"])
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
    types["DeliveryAreaIn"] = t.struct(
        {
            "countryCode": t.string(),
            "postalCodeRange": t.proxy(
                renames["DeliveryAreaPostalCodeRangeIn"]
            ).optional(),
            "regionCode": t.string().optional(),
        }
    ).named(renames["DeliveryAreaIn"])
    types["DeliveryAreaOut"] = t.struct(
        {
            "countryCode": t.string(),
            "postalCodeRange": t.proxy(
                renames["DeliveryAreaPostalCodeRangeOut"]
            ).optional(),
            "regionCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeliveryAreaOut"])
    types["ServiceStoreConfigCutoffConfigLocalCutoffTimeIn"] = t.struct(
        {"hour": t.string().optional(), "minute": t.string().optional()}
    ).named(renames["ServiceStoreConfigCutoffConfigLocalCutoffTimeIn"])
    types["ServiceStoreConfigCutoffConfigLocalCutoffTimeOut"] = t.struct(
        {
            "hour": t.string().optional(),
            "minute": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceStoreConfigCutoffConfigLocalCutoffTimeOut"])
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
    types["PosStoreIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "storeAddress": t.string(),
            "phoneNumber": t.string().optional(),
            "websiteUrl": t.string().optional(),
            "placeId": t.string().optional(),
            "gcidCategory": t.array(t.string()).optional(),
            "storeCode": t.string(),
            "storeName": t.string().optional(),
        }
    ).named(renames["PosStoreIn"])
    types["PosStoreOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "storeAddress": t.string(),
            "phoneNumber": t.string().optional(),
            "websiteUrl": t.string().optional(),
            "placeId": t.string().optional(),
            "gcidCategory": t.array(t.string()).optional(),
            "storeCode": t.string(),
            "storeName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PosStoreOut"])
    types["ShoppingAdsProgramStatusRegionStatusIn"] = t.struct(
        {
            "reviewIssues": t.array(t.string()).optional(),
            "onboardingIssues": t.array(t.string()).optional(),
            "reviewIneligibilityReasonDetails": t.proxy(
                renames["ShoppingAdsProgramStatusReviewIneligibilityReasonDetailsIn"]
            ).optional(),
            "reviewIneligibilityReasonDescription": t.string().optional(),
            "reviewEligibilityStatus": t.string().optional(),
            "disapprovalDate": t.string().optional(),
            "eligibilityStatus": t.string().optional(),
            "regionCodes": t.array(t.string()).optional(),
            "reviewIneligibilityReason": t.string().optional(),
        }
    ).named(renames["ShoppingAdsProgramStatusRegionStatusIn"])
    types["ShoppingAdsProgramStatusRegionStatusOut"] = t.struct(
        {
            "reviewIssues": t.array(t.string()).optional(),
            "onboardingIssues": t.array(t.string()).optional(),
            "reviewIneligibilityReasonDetails": t.proxy(
                renames["ShoppingAdsProgramStatusReviewIneligibilityReasonDetailsOut"]
            ).optional(),
            "reviewIneligibilityReasonDescription": t.string().optional(),
            "reviewEligibilityStatus": t.string().optional(),
            "disapprovalDate": t.string().optional(),
            "eligibilityStatus": t.string().optional(),
            "regionCodes": t.array(t.string()).optional(),
            "reviewIneligibilityReason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShoppingAdsProgramStatusRegionStatusOut"])
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
    types["RecommendationCallToActionIn"] = t.struct(
        {"uri": t.string().optional()}
    ).named(renames["RecommendationCallToActionIn"])
    types["RecommendationCallToActionOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "intent": t.string().optional(),
            "localizedText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RecommendationCallToActionOut"])
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
    types["DateIn"] = t.struct(
        {
            "day": t.integer().optional(),
            "year": t.integer().optional(),
            "month": t.integer().optional(),
        }
    ).named(renames["DateIn"])
    types["DateOut"] = t.struct(
        {
            "day": t.integer().optional(),
            "year": t.integer().optional(),
            "month": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
    types["AccountStatusProductsIn"] = t.struct(
        {
            "channel": t.string().optional(),
            "country": t.string().optional(),
            "destination": t.string().optional(),
            "statistics": t.proxy(renames["AccountStatusStatisticsIn"]).optional(),
            "itemLevelIssues": t.array(
                t.proxy(renames["AccountStatusItemLevelIssueIn"])
            ).optional(),
        }
    ).named(renames["AccountStatusProductsIn"])
    types["AccountStatusProductsOut"] = t.struct(
        {
            "channel": t.string().optional(),
            "country": t.string().optional(),
            "destination": t.string().optional(),
            "statistics": t.proxy(renames["AccountStatusStatisticsOut"]).optional(),
            "itemLevelIssues": t.array(
                t.proxy(renames["AccountStatusItemLevelIssueOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountStatusProductsOut"])
    types["DatafeedsCustomBatchResponseEntryIn"] = t.struct(
        {
            "errors": t.proxy(renames["ErrorsIn"]).optional(),
            "batchId": t.integer().optional(),
            "datafeed": t.proxy(renames["DatafeedIn"]).optional(),
        }
    ).named(renames["DatafeedsCustomBatchResponseEntryIn"])
    types["DatafeedsCustomBatchResponseEntryOut"] = t.struct(
        {
            "errors": t.proxy(renames["ErrorsOut"]).optional(),
            "batchId": t.integer().optional(),
            "datafeed": t.proxy(renames["DatafeedOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatafeedsCustomBatchResponseEntryOut"])
    types["RequestReviewFreeListingsRequestIn"] = t.struct(
        {"regionCode": t.string().optional()}
    ).named(renames["RequestReviewFreeListingsRequestIn"])
    types["RequestReviewFreeListingsRequestOut"] = t.struct(
        {
            "regionCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestReviewFreeListingsRequestOut"])
    types["RecommendationCreativeIn"] = t.struct(
        {"type": t.string().optional(), "uri": t.string().optional()}
    ).named(renames["RecommendationCreativeIn"])
    types["RecommendationCreativeOut"] = t.struct(
        {
            "type": t.string().optional(),
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RecommendationCreativeOut"])
    types["AccountStatusIn"] = t.struct(
        {
            "accountLevelIssues": t.array(
                t.proxy(renames["AccountStatusAccountLevelIssueIn"])
            ).optional(),
            "accountManagement": t.string().optional(),
            "websiteClaimed": t.boolean().optional(),
            "accountId": t.string().optional(),
            "kind": t.string().optional(),
            "products": t.array(t.proxy(renames["AccountStatusProductsIn"])).optional(),
        }
    ).named(renames["AccountStatusIn"])
    types["AccountStatusOut"] = t.struct(
        {
            "accountLevelIssues": t.array(
                t.proxy(renames["AccountStatusAccountLevelIssueOut"])
            ).optional(),
            "accountManagement": t.string().optional(),
            "websiteClaimed": t.boolean().optional(),
            "accountId": t.string().optional(),
            "kind": t.string().optional(),
            "products": t.array(
                t.proxy(renames["AccountStatusProductsOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountStatusOut"])
    types["ECommercePlatformLinkInfoIn"] = t.struct(
        {"externalAccountId": t.string().optional()}
    ).named(renames["ECommercePlatformLinkInfoIn"])
    types["ECommercePlatformLinkInfoOut"] = t.struct(
        {
            "externalAccountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ECommercePlatformLinkInfoOut"])
    types["CutoffTimeIn"] = t.struct(
        {
            "timezone": t.string().optional(),
            "hour": t.integer().optional(),
            "minute": t.integer().optional(),
        }
    ).named(renames["CutoffTimeIn"])
    types["CutoffTimeOut"] = t.struct(
        {
            "timezone": t.string().optional(),
            "hour": t.integer().optional(),
            "minute": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CutoffTimeOut"])
    types[
        "OrdersCustomBatchRequestEntryUpdateShipmentScheduledDeliveryDetailsIn"
    ] = t.struct(
        {
            "scheduledDate": t.string().optional(),
            "carrierPhoneNumber": t.string().optional(),
        }
    ).named(
        renames["OrdersCustomBatchRequestEntryUpdateShipmentScheduledDeliveryDetailsIn"]
    )
    types[
        "OrdersCustomBatchRequestEntryUpdateShipmentScheduledDeliveryDetailsOut"
    ] = t.struct(
        {
            "scheduledDate": t.string().optional(),
            "carrierPhoneNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "OrdersCustomBatchRequestEntryUpdateShipmentScheduledDeliveryDetailsOut"
        ]
    )
    types["LabelIdsIn"] = t.struct({"labelIds": t.array(t.string()).optional()}).named(
        renames["LabelIdsIn"]
    )
    types["LabelIdsOut"] = t.struct(
        {
            "labelIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LabelIdsOut"])
    types["RegionalinventoryCustomBatchResponseEntryIn"] = t.struct(
        {
            "errors": t.proxy(renames["ErrorsIn"]).optional(),
            "batchId": t.integer().optional(),
            "regionalInventory": t.proxy(renames["RegionalInventoryIn"]).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["RegionalinventoryCustomBatchResponseEntryIn"])
    types["RegionalinventoryCustomBatchResponseEntryOut"] = t.struct(
        {
            "errors": t.proxy(renames["ErrorsOut"]).optional(),
            "batchId": t.integer().optional(),
            "regionalInventory": t.proxy(renames["RegionalInventoryOut"]).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegionalinventoryCustomBatchResponseEntryOut"])
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
    types["PriceCompetitivenessIn"] = t.struct(
        {
            "benchmarkPriceMicros": t.string().optional(),
            "benchmarkPriceCurrencyCode": t.string().optional(),
            "countryCode": t.string().optional(),
        }
    ).named(renames["PriceCompetitivenessIn"])
    types["PriceCompetitivenessOut"] = t.struct(
        {
            "benchmarkPriceMicros": t.string().optional(),
            "benchmarkPriceCurrencyCode": t.string().optional(),
            "countryCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PriceCompetitivenessOut"])
    types["OrdersCreateTestOrderRequestIn"] = t.struct(
        {
            "testOrder": t.proxy(renames["TestOrderIn"]).optional(),
            "templateName": t.string().optional(),
            "country": t.string().optional(),
        }
    ).named(renames["OrdersCreateTestOrderRequestIn"])
    types["OrdersCreateTestOrderRequestOut"] = t.struct(
        {
            "testOrder": t.proxy(renames["TestOrderOut"]).optional(),
            "templateName": t.string().optional(),
            "country": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersCreateTestOrderRequestOut"])
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
    types["SegmentsIn"] = t.struct(
        {
            "customLabel3": t.string().optional(),
            "customLabel4": t.string().optional(),
            "date": t.proxy(renames["DateIn"]).optional(),
            "categoryL2": t.string().optional(),
            "customerCountryCode": t.string().optional(),
            "productTypeL4": t.string().optional(),
            "program": t.string().optional(),
            "week": t.proxy(renames["DateIn"]).optional(),
            "categoryL5": t.string().optional(),
            "categoryL4": t.string().optional(),
            "productTypeL2": t.string().optional(),
            "customLabel2": t.string().optional(),
            "currencyCode": t.string().optional(),
            "productTypeL3": t.string().optional(),
            "categoryL3": t.string().optional(),
            "customLabel1": t.string().optional(),
            "brand": t.string().optional(),
            "customLabel0": t.string().optional(),
            "categoryL1": t.string().optional(),
            "productTypeL5": t.string().optional(),
            "title": t.string().optional(),
            "productTypeL1": t.string().optional(),
            "offerId": t.string().optional(),
        }
    ).named(renames["SegmentsIn"])
    types["SegmentsOut"] = t.struct(
        {
            "customLabel3": t.string().optional(),
            "customLabel4": t.string().optional(),
            "date": t.proxy(renames["DateOut"]).optional(),
            "categoryL2": t.string().optional(),
            "customerCountryCode": t.string().optional(),
            "productTypeL4": t.string().optional(),
            "program": t.string().optional(),
            "week": t.proxy(renames["DateOut"]).optional(),
            "categoryL5": t.string().optional(),
            "categoryL4": t.string().optional(),
            "productTypeL2": t.string().optional(),
            "customLabel2": t.string().optional(),
            "currencyCode": t.string().optional(),
            "productTypeL3": t.string().optional(),
            "categoryL3": t.string().optional(),
            "customLabel1": t.string().optional(),
            "brand": t.string().optional(),
            "customLabel0": t.string().optional(),
            "categoryL1": t.string().optional(),
            "productTypeL5": t.string().optional(),
            "title": t.string().optional(),
            "productTypeL1": t.string().optional(),
            "offerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SegmentsOut"])
    types["OrderShipmentScheduledDeliveryDetailsIn"] = t.struct(
        {
            "scheduledDate": t.string().optional(),
            "carrierPhoneNumber": t.string().optional(),
        }
    ).named(renames["OrderShipmentScheduledDeliveryDetailsIn"])
    types["OrderShipmentScheduledDeliveryDetailsOut"] = t.struct(
        {
            "scheduledDate": t.string().optional(),
            "carrierPhoneNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderShipmentScheduledDeliveryDetailsOut"])
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
    types["OrderinvoicesCreateRefundInvoiceRequestIn"] = t.struct(
        {
            "invoiceId": t.string().optional(),
            "refundOnlyOption": t.proxy(
                renames[
                    "OrderinvoicesCustomBatchRequestEntryCreateRefundInvoiceRefundOptionIn"
                ]
            ).optional(),
            "shipmentInvoices": t.array(
                t.proxy(renames["ShipmentInvoiceIn"])
            ).optional(),
            "returnOption": t.proxy(
                renames[
                    "OrderinvoicesCustomBatchRequestEntryCreateRefundInvoiceReturnOptionIn"
                ]
            ).optional(),
            "operationId": t.string().optional(),
        }
    ).named(renames["OrderinvoicesCreateRefundInvoiceRequestIn"])
    types["OrderinvoicesCreateRefundInvoiceRequestOut"] = t.struct(
        {
            "invoiceId": t.string().optional(),
            "refundOnlyOption": t.proxy(
                renames[
                    "OrderinvoicesCustomBatchRequestEntryCreateRefundInvoiceRefundOptionOut"
                ]
            ).optional(),
            "shipmentInvoices": t.array(
                t.proxy(renames["ShipmentInvoiceOut"])
            ).optional(),
            "returnOption": t.proxy(
                renames[
                    "OrderinvoicesCustomBatchRequestEntryCreateRefundInvoiceReturnOptionOut"
                ]
            ).optional(),
            "operationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderinvoicesCreateRefundInvoiceRequestOut"])
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
    types["DeliveryTimeIn"] = t.struct(
        {
            "transitBusinessDayConfig": t.proxy(
                renames["BusinessDayConfigIn"]
            ).optional(),
            "handlingBusinessDayConfig": t.proxy(
                renames["BusinessDayConfigIn"]
            ).optional(),
            "transitTimeTable": t.proxy(renames["TransitTableIn"]).optional(),
            "maxTransitTimeInDays": t.integer().optional(),
            "minTransitTimeInDays": t.integer().optional(),
            "warehouseBasedDeliveryTimes": t.array(
                t.proxy(renames["WarehouseBasedDeliveryTimeIn"])
            ).optional(),
            "maxHandlingTimeInDays": t.integer().optional(),
            "minHandlingTimeInDays": t.integer().optional(),
            "cutoffTime": t.proxy(renames["CutoffTimeIn"]).optional(),
            "holidayCutoffs": t.array(t.proxy(renames["HolidayCutoffIn"])).optional(),
        }
    ).named(renames["DeliveryTimeIn"])
    types["DeliveryTimeOut"] = t.struct(
        {
            "transitBusinessDayConfig": t.proxy(
                renames["BusinessDayConfigOut"]
            ).optional(),
            "handlingBusinessDayConfig": t.proxy(
                renames["BusinessDayConfigOut"]
            ).optional(),
            "transitTimeTable": t.proxy(renames["TransitTableOut"]).optional(),
            "maxTransitTimeInDays": t.integer().optional(),
            "minTransitTimeInDays": t.integer().optional(),
            "warehouseBasedDeliveryTimes": t.array(
                t.proxy(renames["WarehouseBasedDeliveryTimeOut"])
            ).optional(),
            "maxHandlingTimeInDays": t.integer().optional(),
            "minHandlingTimeInDays": t.integer().optional(),
            "cutoffTime": t.proxy(renames["CutoffTimeOut"]).optional(),
            "holidayCutoffs": t.array(t.proxy(renames["HolidayCutoffOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeliveryTimeOut"])
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
    types["PosListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "resources": t.array(t.proxy(renames["PosStoreIn"])),
        }
    ).named(renames["PosListResponseIn"])
    types["PosListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "resources": t.array(t.proxy(renames["PosStoreOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PosListResponseOut"])
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
    types["CollectionStatusDestinationStatusIn"] = t.struct(
        {
            "pendingCountries": t.array(t.string()).optional(),
            "disapprovedCountries": t.array(t.string()).optional(),
            "destination": t.string().optional(),
            "approvedCountries": t.array(t.string()).optional(),
            "status": t.string().optional(),
        }
    ).named(renames["CollectionStatusDestinationStatusIn"])
    types["CollectionStatusDestinationStatusOut"] = t.struct(
        {
            "pendingCountries": t.array(t.string()).optional(),
            "disapprovedCountries": t.array(t.string()).optional(),
            "destination": t.string().optional(),
            "approvedCountries": t.array(t.string()).optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CollectionStatusDestinationStatusOut"])
    types["TestOrderLineItemProductIn"] = t.struct(
        {
            "itemGroupId": t.string().optional(),
            "gtin": t.string().optional(),
            "condition": t.string(),
            "targetCountry": t.string(),
            "brand": t.string(),
            "offerId": t.string(),
            "fees": t.array(t.proxy(renames["OrderLineItemProductFeeIn"])).optional(),
            "imageLink": t.string(),
            "variantAttributes": t.array(
                t.proxy(renames["OrderLineItemProductVariantAttributeIn"])
            ).optional(),
            "title": t.string(),
            "contentLanguage": t.string(),
            "mpn": t.string().optional(),
            "price": t.proxy(renames["PriceIn"]),
        }
    ).named(renames["TestOrderLineItemProductIn"])
    types["TestOrderLineItemProductOut"] = t.struct(
        {
            "itemGroupId": t.string().optional(),
            "gtin": t.string().optional(),
            "condition": t.string(),
            "targetCountry": t.string(),
            "brand": t.string(),
            "offerId": t.string(),
            "fees": t.array(t.proxy(renames["OrderLineItemProductFeeOut"])).optional(),
            "imageLink": t.string(),
            "variantAttributes": t.array(
                t.proxy(renames["OrderLineItemProductVariantAttributeOut"])
            ).optional(),
            "title": t.string(),
            "contentLanguage": t.string(),
            "mpn": t.string().optional(),
            "price": t.proxy(renames["PriceOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestOrderLineItemProductOut"])
    types["AccountConversionSettingsIn"] = t.struct(
        {"freeListingsAutoTaggingEnabled": t.boolean().optional()}
    ).named(renames["AccountConversionSettingsIn"])
    types["AccountConversionSettingsOut"] = t.struct(
        {
            "freeListingsAutoTaggingEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountConversionSettingsOut"])
    types["OrdersCustomBatchRequestEntryRefundItemItemIn"] = t.struct(
        {
            "lineItemId": t.string().optional(),
            "amount": t.proxy(renames["MonetaryAmountIn"]).optional(),
            "quantity": t.integer().optional(),
            "fullRefund": t.boolean().optional(),
            "productId": t.string().optional(),
        }
    ).named(renames["OrdersCustomBatchRequestEntryRefundItemItemIn"])
    types["OrdersCustomBatchRequestEntryRefundItemItemOut"] = t.struct(
        {
            "lineItemId": t.string().optional(),
            "amount": t.proxy(renames["MonetaryAmountOut"]).optional(),
            "quantity": t.integer().optional(),
            "fullRefund": t.boolean().optional(),
            "productId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersCustomBatchRequestEntryRefundItemItemOut"])
    types["RepricingRuleEligibleOfferMatcherStringMatcherIn"] = t.struct(
        {"strAttributes": t.array(t.string()).optional()}
    ).named(renames["RepricingRuleEligibleOfferMatcherStringMatcherIn"])
    types["RepricingRuleEligibleOfferMatcherStringMatcherOut"] = t.struct(
        {
            "strAttributes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepricingRuleEligibleOfferMatcherStringMatcherOut"])
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
    types["CssIn"] = t.struct({"labelIds": t.array(t.string()).optional()}).named(
        renames["CssIn"]
    )
    types["CssOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "fullName": t.string().optional(),
            "cssDomainId": t.string().optional(),
            "cssGroupId": t.string().optional(),
            "homepageUri": t.string().optional(),
            "labelIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CssOut"])
    types["BuyOnGoogleProgramStatusIn"] = t.struct(
        {
            "businessModel": t.array(t.string()).optional(),
            "customerServicePendingEmail": t.string().optional(),
            "customerServicePendingPhoneRegionCode": t.string().optional(),
            "customerServicePendingPhoneNumber": t.string().optional(),
            "onlineSalesChannel": t.string().optional(),
        }
    ).named(renames["BuyOnGoogleProgramStatusIn"])
    types["BuyOnGoogleProgramStatusOut"] = t.struct(
        {
            "customerServiceVerifiedEmail": t.string().optional(),
            "businessModel": t.array(t.string()).optional(),
            "customerServicePendingEmail": t.string().optional(),
            "participationStage": t.string().optional(),
            "customerServicePendingPhoneRegionCode": t.string().optional(),
            "customerServiceVerifiedPhoneRegionCode": t.string().optional(),
            "customerServiceVerifiedPhoneNumber": t.string().optional(),
            "customerServicePendingPhoneNumber": t.string().optional(),
            "onlineSalesChannel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuyOnGoogleProgramStatusOut"])
    types["OrderTrackingSignalLineItemDetailsIn"] = t.struct(
        {
            "quantity": t.string().optional(),
            "sku": t.string().optional(),
            "brand": t.string().optional(),
            "lineItemId": t.string(),
            "productId": t.string(),
            "gtin": t.string().optional(),
            "upc": t.string().optional(),
            "productTitle": t.string().optional(),
            "mpn": t.string().optional(),
            "productDescription": t.string().optional(),
        }
    ).named(renames["OrderTrackingSignalLineItemDetailsIn"])
    types["OrderTrackingSignalLineItemDetailsOut"] = t.struct(
        {
            "quantity": t.string().optional(),
            "sku": t.string().optional(),
            "brand": t.string().optional(),
            "lineItemId": t.string(),
            "productId": t.string(),
            "gtin": t.string().optional(),
            "upc": t.string().optional(),
            "productTitle": t.string().optional(),
            "mpn": t.string().optional(),
            "productDescription": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderTrackingSignalLineItemDetailsOut"])
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
    types["OrderLineItemProductFeeIn"] = t.struct(
        {
            "amount": t.proxy(renames["PriceIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OrderLineItemProductFeeIn"])
    types["OrderLineItemProductFeeOut"] = t.struct(
        {
            "amount": t.proxy(renames["PriceOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderLineItemProductFeeOut"])
    types["ServiceStoreConfigCutoffConfigIn"] = t.struct(
        {
            "localCutoffTime": t.proxy(
                renames["ServiceStoreConfigCutoffConfigLocalCutoffTimeIn"]
            ).optional(),
            "storeCloseOffsetHours": t.string().optional(),
        }
    ).named(renames["ServiceStoreConfigCutoffConfigIn"])
    types["ServiceStoreConfigCutoffConfigOut"] = t.struct(
        {
            "localCutoffTime": t.proxy(
                renames["ServiceStoreConfigCutoffConfigLocalCutoffTimeOut"]
            ).optional(),
            "storeCloseOffsetHours": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceStoreConfigCutoffConfigOut"])
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
    types["ServiceIn"] = t.struct(
        {
            "pickupService": t.proxy(renames["PickupCarrierServiceIn"]).optional(),
            "name": t.string().optional(),
            "eligibility": t.string().optional(),
            "rateGroups": t.array(t.proxy(renames["RateGroupIn"])).optional(),
            "active": t.boolean().optional(),
            "storeConfig": t.proxy(renames["ServiceStoreConfigIn"]).optional(),
            "deliveryCountry": t.string().optional(),
            "deliveryTime": t.proxy(renames["DeliveryTimeIn"]).optional(),
            "minimumOrderValueTable": t.proxy(
                renames["MinimumOrderValueTableIn"]
            ).optional(),
            "currency": t.string().optional(),
            "shipmentType": t.string().optional(),
            "minimumOrderValue": t.proxy(renames["PriceIn"]).optional(),
        }
    ).named(renames["ServiceIn"])
    types["ServiceOut"] = t.struct(
        {
            "pickupService": t.proxy(renames["PickupCarrierServiceOut"]).optional(),
            "name": t.string().optional(),
            "eligibility": t.string().optional(),
            "rateGroups": t.array(t.proxy(renames["RateGroupOut"])).optional(),
            "active": t.boolean().optional(),
            "storeConfig": t.proxy(renames["ServiceStoreConfigOut"]).optional(),
            "deliveryCountry": t.string().optional(),
            "deliveryTime": t.proxy(renames["DeliveryTimeOut"]).optional(),
            "minimumOrderValueTable": t.proxy(
                renames["MinimumOrderValueTableOut"]
            ).optional(),
            "currency": t.string().optional(),
            "shipmentType": t.string().optional(),
            "minimumOrderValue": t.proxy(renames["PriceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceOut"])
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
    types["OrderTrackingSignalShippingInfoIn"] = t.struct(
        {
            "shippingStatus": t.string().optional(),
            "shippedTime": t.proxy(renames["DateTimeIn"]).optional(),
            "latestDeliveryPromiseTime": t.proxy(renames["DateTimeIn"]).optional(),
            "actualDeliveryTime": t.proxy(renames["DateTimeIn"]).optional(),
            "shipmentId": t.string(),
            "trackingId": t.string().optional(),
            "originRegionCode": t.string().optional(),
            "originPostalCode": t.string().optional(),
            "carrierServiceName": t.string().optional(),
            "earliestDeliveryPromiseTime": t.proxy(renames["DateTimeIn"]).optional(),
            "carrierName": t.string().optional(),
        }
    ).named(renames["OrderTrackingSignalShippingInfoIn"])
    types["OrderTrackingSignalShippingInfoOut"] = t.struct(
        {
            "shippingStatus": t.string().optional(),
            "shippedTime": t.proxy(renames["DateTimeOut"]).optional(),
            "latestDeliveryPromiseTime": t.proxy(renames["DateTimeOut"]).optional(),
            "actualDeliveryTime": t.proxy(renames["DateTimeOut"]).optional(),
            "shipmentId": t.string(),
            "trackingId": t.string().optional(),
            "originRegionCode": t.string().optional(),
            "originPostalCode": t.string().optional(),
            "carrierServiceName": t.string().optional(),
            "earliestDeliveryPromiseTime": t.proxy(renames["DateTimeOut"]).optional(),
            "carrierName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderTrackingSignalShippingInfoOut"])
    types["SettlementTransactionIdentifiersIn"] = t.struct(
        {
            "transactionId": t.string().optional(),
            "settlementEntryId": t.string().optional(),
            "merchantOrderId": t.string().optional(),
            "adjustmentId": t.string().optional(),
            "orderItemId": t.string().optional(),
            "shipmentIds": t.array(t.string()).optional(),
        }
    ).named(renames["SettlementTransactionIdentifiersIn"])
    types["SettlementTransactionIdentifiersOut"] = t.struct(
        {
            "transactionId": t.string().optional(),
            "settlementEntryId": t.string().optional(),
            "merchantOrderId": t.string().optional(),
            "adjustmentId": t.string().optional(),
            "orderItemId": t.string().optional(),
            "shipmentIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SettlementTransactionIdentifiersOut"])
    types["OrdersRefundItemRequestIn"] = t.struct(
        {
            "reason": t.string().optional(),
            "reasonText": t.string().optional(),
            "operationId": t.string().optional(),
            "items": t.array(
                t.proxy(renames["OrdersCustomBatchRequestEntryRefundItemItemIn"])
            ).optional(),
            "shipping": t.proxy(
                renames["OrdersCustomBatchRequestEntryRefundItemShippingIn"]
            ).optional(),
        }
    ).named(renames["OrdersRefundItemRequestIn"])
    types["OrdersRefundItemRequestOut"] = t.struct(
        {
            "reason": t.string().optional(),
            "reasonText": t.string().optional(),
            "operationId": t.string().optional(),
            "items": t.array(
                t.proxy(renames["OrdersCustomBatchRequestEntryRefundItemItemOut"])
            ).optional(),
            "shipping": t.proxy(
                renames["OrdersCustomBatchRequestEntryRefundItemShippingOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersRefundItemRequestOut"])
    types["ReturnAddressIn"] = t.struct(
        {
            "address": t.proxy(renames["ReturnAddressAddressIn"]),
            "country": t.string(),
            "phoneNumber": t.string(),
            "kind": t.string().optional(),
            "label": t.string(),
            "returnAddressId": t.string().optional(),
        }
    ).named(renames["ReturnAddressIn"])
    types["ReturnAddressOut"] = t.struct(
        {
            "address": t.proxy(renames["ReturnAddressAddressOut"]),
            "country": t.string(),
            "phoneNumber": t.string(),
            "kind": t.string().optional(),
            "label": t.string(),
            "returnAddressId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReturnAddressOut"])
    types["ListConversionSourcesResponseIn"] = t.struct(
        {
            "conversionSources": t.array(
                t.proxy(renames["ConversionSourceIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListConversionSourcesResponseIn"])
    types["ListConversionSourcesResponseOut"] = t.struct(
        {
            "conversionSources": t.array(
                t.proxy(renames["ConversionSourceOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListConversionSourcesResponseOut"])
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
    types["AddressIn"] = t.struct(
        {
            "country": t.string(),
            "administrativeArea": t.string(),
            "streetAddress": t.string().optional(),
            "postalCode": t.string(),
            "city": t.string(),
        }
    ).named(renames["AddressIn"])
    types["AddressOut"] = t.struct(
        {
            "country": t.string(),
            "administrativeArea": t.string(),
            "streetAddress": t.string().optional(),
            "postalCode": t.string(),
            "city": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddressOut"])
    types["OrdersCancelLineItemRequestIn"] = t.struct(
        {
            "operationId": t.string().optional(),
            "reasonText": t.string().optional(),
            "productId": t.string().optional(),
            "quantity": t.integer().optional(),
            "lineItemId": t.string().optional(),
            "reason": t.string().optional(),
        }
    ).named(renames["OrdersCancelLineItemRequestIn"])
    types["OrdersCancelLineItemRequestOut"] = t.struct(
        {
            "operationId": t.string().optional(),
            "reasonText": t.string().optional(),
            "productId": t.string().optional(),
            "quantity": t.integer().optional(),
            "lineItemId": t.string().optional(),
            "reason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersCancelLineItemRequestOut"])
    types["ProductClusterIn"] = t.struct(
        {
            "variantGtins": t.array(t.string()).optional(),
            "categoryL1": t.string().optional(),
            "categoryL4": t.string().optional(),
            "inventoryStatus": t.string().optional(),
            "brand": t.string().optional(),
            "brandInventoryStatus": t.string().optional(),
            "categoryL5": t.string().optional(),
            "categoryL3": t.string().optional(),
            "categoryL2": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["ProductClusterIn"])
    types["ProductClusterOut"] = t.struct(
        {
            "variantGtins": t.array(t.string()).optional(),
            "categoryL1": t.string().optional(),
            "categoryL4": t.string().optional(),
            "inventoryStatus": t.string().optional(),
            "brand": t.string().optional(),
            "brandInventoryStatus": t.string().optional(),
            "categoryL5": t.string().optional(),
            "categoryL3": t.string().optional(),
            "categoryL2": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductClusterOut"])
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
    types["AccountStatusAccountLevelIssueIn"] = t.struct(
        {
            "title": t.string().optional(),
            "destination": t.string().optional(),
            "documentation": t.string().optional(),
            "country": t.string().optional(),
            "id": t.string().optional(),
            "severity": t.string().optional(),
            "detail": t.string().optional(),
        }
    ).named(renames["AccountStatusAccountLevelIssueIn"])
    types["AccountStatusAccountLevelIssueOut"] = t.struct(
        {
            "title": t.string().optional(),
            "destination": t.string().optional(),
            "documentation": t.string().optional(),
            "country": t.string().optional(),
            "id": t.string().optional(),
            "severity": t.string().optional(),
            "detail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountStatusAccountLevelIssueOut"])
    types["ProductstatusesListResponseIn"] = t.struct(
        {
            "resources": t.array(t.proxy(renames["ProductStatusIn"])),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ProductstatusesListResponseIn"])
    types["ProductstatusesListResponseOut"] = t.struct(
        {
            "resources": t.array(t.proxy(renames["ProductStatusOut"])),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductstatusesListResponseOut"])
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
    types["AccountstatusesCustomBatchRequestEntryIn"] = t.struct(
        {
            "accountId": t.string().optional(),
            "batchId": t.integer().optional(),
            "destinations": t.array(t.string()).optional(),
            "merchantId": t.string().optional(),
            "method": t.string().optional(),
        }
    ).named(renames["AccountstatusesCustomBatchRequestEntryIn"])
    types["AccountstatusesCustomBatchRequestEntryOut"] = t.struct(
        {
            "accountId": t.string().optional(),
            "batchId": t.integer().optional(),
            "destinations": t.array(t.string()).optional(),
            "merchantId": t.string().optional(),
            "method": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountstatusesCustomBatchRequestEntryOut"])
    types["PosInventoryIn"] = t.struct(
        {
            "contentLanguage": t.string(),
            "kind": t.string().optional(),
            "storeCode": t.string(),
            "gtin": t.string().optional(),
            "quantity": t.string(),
            "targetCountry": t.string(),
            "itemId": t.string(),
            "timestamp": t.string(),
            "price": t.proxy(renames["PriceIn"]),
        }
    ).named(renames["PosInventoryIn"])
    types["PosInventoryOut"] = t.struct(
        {
            "contentLanguage": t.string(),
            "kind": t.string().optional(),
            "storeCode": t.string(),
            "gtin": t.string().optional(),
            "quantity": t.string(),
            "targetCountry": t.string(),
            "itemId": t.string(),
            "timestamp": t.string(),
            "price": t.proxy(renames["PriceOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PosInventoryOut"])
    types["OrderShipmentLineItemShipmentIn"] = t.struct(
        {
            "productId": t.string().optional(),
            "quantity": t.integer().optional(),
            "lineItemId": t.string().optional(),
        }
    ).named(renames["OrderShipmentLineItemShipmentIn"])
    types["OrderShipmentLineItemShipmentOut"] = t.struct(
        {
            "productId": t.string().optional(),
            "quantity": t.integer().optional(),
            "lineItemId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderShipmentLineItemShipmentOut"])
    types["OrderinvoicesCreateChargeInvoiceRequestIn"] = t.struct(
        {
            "invoiceSummary": t.proxy(renames["InvoiceSummaryIn"]).optional(),
            "lineItemInvoices": t.array(
                t.proxy(renames["ShipmentInvoiceLineItemInvoiceIn"])
            ).optional(),
            "shipmentGroupId": t.string().optional(),
            "invoiceId": t.string().optional(),
            "operationId": t.string().optional(),
        }
    ).named(renames["OrderinvoicesCreateChargeInvoiceRequestIn"])
    types["OrderinvoicesCreateChargeInvoiceRequestOut"] = t.struct(
        {
            "invoiceSummary": t.proxy(renames["InvoiceSummaryOut"]).optional(),
            "lineItemInvoices": t.array(
                t.proxy(renames["ShipmentInvoiceLineItemInvoiceOut"])
            ).optional(),
            "shipmentGroupId": t.string().optional(),
            "invoiceId": t.string().optional(),
            "operationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderinvoicesCreateChargeInvoiceRequestOut"])
    types["RowIn"] = t.struct(
        {"cells": t.array(t.proxy(renames["ValueIn"])).optional()}
    ).named(renames["RowIn"])
    types["RowOut"] = t.struct(
        {
            "cells": t.array(t.proxy(renames["ValueOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RowOut"])
    types["AccountItemUpdatesIn"] = t.struct(
        {
            "accountItemUpdatesSettings": t.proxy(
                renames["AccountItemUpdatesSettingsIn"]
            ).optional()
        }
    ).named(renames["AccountItemUpdatesIn"])
    types["AccountItemUpdatesOut"] = t.struct(
        {
            "effectiveAllowStrictAvailabilityUpdates": t.boolean().optional(),
            "effectiveAllowAvailabilityUpdates": t.boolean().optional(),
            "effectiveAllowConditionUpdates": t.boolean().optional(),
            "effectiveAllowPriceUpdates": t.boolean().optional(),
            "accountItemUpdatesSettings": t.proxy(
                renames["AccountItemUpdatesSettingsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountItemUpdatesOut"])
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
    types["ListMethodQuotasResponseIn"] = t.struct(
        {
            "methodQuotas": t.array(t.proxy(renames["MethodQuotaIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListMethodQuotasResponseIn"])
    types["ListMethodQuotasResponseOut"] = t.struct(
        {
            "methodQuotas": t.array(t.proxy(renames["MethodQuotaOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListMethodQuotasResponseOut"])
    types["OrdersAcknowledgeResponseIn"] = t.struct(
        {"kind": t.string().optional(), "executionStatus": t.string().optional()}
    ).named(renames["OrdersAcknowledgeResponseIn"])
    types["OrdersAcknowledgeResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "executionStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersAcknowledgeResponseOut"])
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
    types["RequestPhoneVerificationResponseIn"] = t.struct(
        {"verificationId": t.string().optional()}
    ).named(renames["RequestPhoneVerificationResponseIn"])
    types["RequestPhoneVerificationResponseOut"] = t.struct(
        {
            "verificationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestPhoneVerificationResponseOut"])
    types["OrderPromotionIn"] = t.struct(
        {
            "shortTitle": t.string().optional(),
            "taxValue": t.proxy(renames["PriceIn"]).optional(),
            "funder": t.string(),
            "startTime": t.string().optional(),
            "subtype": t.string(),
            "applicableItems": t.array(
                t.proxy(renames["OrderPromotionItemIn"])
            ).optional(),
            "priceValue": t.proxy(renames["PriceIn"]).optional(),
            "type": t.string(),
            "merchantPromotionId": t.string(),
            "endTime": t.string().optional(),
            "appliedItems": t.array(
                t.proxy(renames["OrderPromotionItemIn"])
            ).optional(),
            "title": t.string(),
        }
    ).named(renames["OrderPromotionIn"])
    types["OrderPromotionOut"] = t.struct(
        {
            "shortTitle": t.string().optional(),
            "taxValue": t.proxy(renames["PriceOut"]).optional(),
            "funder": t.string(),
            "startTime": t.string().optional(),
            "subtype": t.string(),
            "applicableItems": t.array(
                t.proxy(renames["OrderPromotionItemOut"])
            ).optional(),
            "priceValue": t.proxy(renames["PriceOut"]).optional(),
            "type": t.string(),
            "merchantPromotionId": t.string(),
            "endTime": t.string().optional(),
            "appliedItems": t.array(
                t.proxy(renames["OrderPromotionItemOut"])
            ).optional(),
            "title": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderPromotionOut"])
    types["RegionPostalCodeAreaPostalCodeRangeIn"] = t.struct(
        {"end": t.string().optional(), "begin": t.string()}
    ).named(renames["RegionPostalCodeAreaPostalCodeRangeIn"])
    types["RegionPostalCodeAreaPostalCodeRangeOut"] = t.struct(
        {
            "end": t.string().optional(),
            "begin": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegionPostalCodeAreaPostalCodeRangeOut"])
    types["OrderRefundIn"] = t.struct(
        {
            "amount": t.proxy(renames["PriceIn"]).optional(),
            "creationDate": t.string().optional(),
            "reasonText": t.string().optional(),
            "reason": t.string().optional(),
            "actor": t.string().optional(),
        }
    ).named(renames["OrderRefundIn"])
    types["OrderRefundOut"] = t.struct(
        {
            "amount": t.proxy(renames["PriceOut"]).optional(),
            "creationDate": t.string().optional(),
            "reasonText": t.string().optional(),
            "reason": t.string().optional(),
            "actor": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderRefundOut"])
    types["ShippingSettingsIn"] = t.struct(
        {
            "postalCodeGroups": t.array(
                t.proxy(renames["PostalCodeGroupIn"])
            ).optional(),
            "services": t.array(t.proxy(renames["ServiceIn"])).optional(),
            "warehouses": t.array(t.proxy(renames["WarehouseIn"])).optional(),
            "accountId": t.string().optional(),
        }
    ).named(renames["ShippingSettingsIn"])
    types["ShippingSettingsOut"] = t.struct(
        {
            "postalCodeGroups": t.array(
                t.proxy(renames["PostalCodeGroupOut"])
            ).optional(),
            "services": t.array(t.proxy(renames["ServiceOut"])).optional(),
            "warehouses": t.array(t.proxy(renames["WarehouseOut"])).optional(),
            "accountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShippingSettingsOut"])
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
    types["TimePeriodIn"] = t.struct(
        {"endTime": t.string().optional(), "startTime": t.string().optional()}
    ).named(renames["TimePeriodIn"])
    types["TimePeriodOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimePeriodOut"])
    types["LiaCountrySettingsIn"] = t.struct(
        {
            "storePickupActive": t.boolean().optional(),
            "onDisplayToOrder": t.proxy(
                renames["LiaOnDisplayToOrderSettingsIn"]
            ).optional(),
            "posDataProvider": t.proxy(renames["LiaPosDataProviderIn"]).optional(),
            "inventory": t.proxy(renames["LiaInventorySettingsIn"]).optional(),
            "hostedLocalStorefrontActive": t.boolean().optional(),
            "country": t.string(),
            "about": t.proxy(renames["LiaAboutPageSettingsIn"]).optional(),
        }
    ).named(renames["LiaCountrySettingsIn"])
    types["LiaCountrySettingsOut"] = t.struct(
        {
            "storePickupActive": t.boolean().optional(),
            "onDisplayToOrder": t.proxy(
                renames["LiaOnDisplayToOrderSettingsOut"]
            ).optional(),
            "posDataProvider": t.proxy(renames["LiaPosDataProviderOut"]).optional(),
            "inventory": t.proxy(renames["LiaInventorySettingsOut"]).optional(),
            "hostedLocalStorefrontActive": t.boolean().optional(),
            "country": t.string(),
            "about": t.proxy(renames["LiaAboutPageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiaCountrySettingsOut"])
    types["OrderreturnsCreateOrderReturnRequestIn"] = t.struct(
        {
            "lineItems": t.array(t.proxy(renames["OrderreturnsLineItemIn"])).optional(),
            "returnMethodType": t.string().optional(),
            "orderId": t.string().optional(),
            "operationId": t.string().optional(),
        }
    ).named(renames["OrderreturnsCreateOrderReturnRequestIn"])
    types["OrderreturnsCreateOrderReturnRequestOut"] = t.struct(
        {
            "lineItems": t.array(
                t.proxy(renames["OrderreturnsLineItemOut"])
            ).optional(),
            "returnMethodType": t.string().optional(),
            "orderId": t.string().optional(),
            "operationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderreturnsCreateOrderReturnRequestOut"])
    types["ProductsListResponseIn"] = t.struct(
        {
            "resources": t.array(t.proxy(renames["ProductIn"])),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ProductsListResponseIn"])
    types["ProductsListResponseOut"] = t.struct(
        {
            "resources": t.array(t.proxy(renames["ProductOut"])),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductsListResponseOut"])
    types["AccountsCustomBatchRequestEntryIn"] = t.struct(
        {
            "force": t.boolean().optional(),
            "method": t.string().optional(),
            "linkRequest": t.proxy(
                renames["AccountsCustomBatchRequestEntryLinkRequestIn"]
            ).optional(),
            "accountId": t.string().optional(),
            "batchId": t.integer().optional(),
            "labelIds": t.array(t.string()).optional(),
            "view": t.string().optional(),
            "overwrite": t.boolean().optional(),
            "merchantId": t.string().optional(),
            "account": t.proxy(renames["AccountIn"]).optional(),
        }
    ).named(renames["AccountsCustomBatchRequestEntryIn"])
    types["AccountsCustomBatchRequestEntryOut"] = t.struct(
        {
            "force": t.boolean().optional(),
            "method": t.string().optional(),
            "linkRequest": t.proxy(
                renames["AccountsCustomBatchRequestEntryLinkRequestOut"]
            ).optional(),
            "accountId": t.string().optional(),
            "batchId": t.integer().optional(),
            "labelIds": t.array(t.string()).optional(),
            "view": t.string().optional(),
            "overwrite": t.boolean().optional(),
            "merchantId": t.string().optional(),
            "account": t.proxy(renames["AccountOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountsCustomBatchRequestEntryOut"])
    types["TestOrderAddressIn"] = t.struct(
        {
            "country": t.string().optional(),
            "region": t.string().optional(),
            "postalCode": t.string().optional(),
            "recipientName": t.string().optional(),
            "streetAddress": t.array(t.string()).optional(),
            "fullAddress": t.array(t.string()).optional(),
            "locality": t.string().optional(),
            "isPostOfficeBox": t.boolean().optional(),
        }
    ).named(renames["TestOrderAddressIn"])
    types["TestOrderAddressOut"] = t.struct(
        {
            "country": t.string().optional(),
            "region": t.string().optional(),
            "postalCode": t.string().optional(),
            "recipientName": t.string().optional(),
            "streetAddress": t.array(t.string()).optional(),
            "fullAddress": t.array(t.string()).optional(),
            "locality": t.string().optional(),
            "isPostOfficeBox": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestOrderAddressOut"])
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
    types["AccounttaxListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "resources": t.array(t.proxy(renames["AccountTaxIn"])),
        }
    ).named(renames["AccounttaxListResponseIn"])
    types["AccounttaxListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "resources": t.array(t.proxy(renames["AccountTaxOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccounttaxListResponseOut"])
    types["RegionalInventoryIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "customAttributes": t.array(
                t.proxy(renames["CustomAttributeIn"])
            ).optional(),
            "availability": t.string().optional(),
            "salePrice": t.proxy(renames["PriceIn"]).optional(),
            "salePriceEffectiveDate": t.string().optional(),
            "regionId": t.string().optional(),
            "price": t.proxy(renames["PriceIn"]).optional(),
        }
    ).named(renames["RegionalInventoryIn"])
    types["RegionalInventoryOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "customAttributes": t.array(
                t.proxy(renames["CustomAttributeOut"])
            ).optional(),
            "availability": t.string().optional(),
            "salePrice": t.proxy(renames["PriceOut"]).optional(),
            "salePriceEffectiveDate": t.string().optional(),
            "regionId": t.string().optional(),
            "price": t.proxy(renames["PriceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegionalInventoryOut"])
    types["OrderreturnsProcessRequestIn"] = t.struct(
        {
            "refundShippingFee": t.proxy(
                renames["OrderreturnsRefundOperationIn"]
            ).optional(),
            "fullChargeReturnShippingCost": t.boolean().optional(),
            "returnItems": t.array(
                t.proxy(renames["OrderreturnsReturnItemIn"])
            ).optional(),
            "operationId": t.string().optional(),
        }
    ).named(renames["OrderreturnsProcessRequestIn"])
    types["OrderreturnsProcessRequestOut"] = t.struct(
        {
            "refundShippingFee": t.proxy(
                renames["OrderreturnsRefundOperationOut"]
            ).optional(),
            "fullChargeReturnShippingCost": t.boolean().optional(),
            "returnItems": t.array(
                t.proxy(renames["OrderreturnsReturnItemOut"])
            ).optional(),
            "operationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderreturnsProcessRequestOut"])
    types["ProductstatusesCustomBatchResponseEntryIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "batchId": t.integer().optional(),
            "errors": t.proxy(renames["ErrorsIn"]).optional(),
            "productStatus": t.proxy(renames["ProductStatusIn"]).optional(),
        }
    ).named(renames["ProductstatusesCustomBatchResponseEntryIn"])
    types["ProductstatusesCustomBatchResponseEntryOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "batchId": t.integer().optional(),
            "errors": t.proxy(renames["ErrorsOut"]).optional(),
            "productStatus": t.proxy(renames["ProductStatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductstatusesCustomBatchResponseEntryOut"])
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
    types["LocalinventoryCustomBatchResponseIn"] = t.struct(
        {
            "entries": t.array(
                t.proxy(renames["LocalinventoryCustomBatchResponseEntryIn"])
            ).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["LocalinventoryCustomBatchResponseIn"])
    types["LocalinventoryCustomBatchResponseOut"] = t.struct(
        {
            "entries": t.array(
                t.proxy(renames["LocalinventoryCustomBatchResponseEntryOut"])
            ).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocalinventoryCustomBatchResponseOut"])
    types["VerifyPhoneNumberRequestIn"] = t.struct(
        {
            "verificationCode": t.string().optional(),
            "phoneVerificationMethod": t.string().optional(),
            "verificationId": t.string().optional(),
        }
    ).named(renames["VerifyPhoneNumberRequestIn"])
    types["VerifyPhoneNumberRequestOut"] = t.struct(
        {
            "verificationCode": t.string().optional(),
            "phoneVerificationMethod": t.string().optional(),
            "verificationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VerifyPhoneNumberRequestOut"])
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
    types["OrdersUpdateShipmentRequestIn"] = t.struct(
        {
            "operationId": t.string().optional(),
            "status": t.string().optional(),
            "scheduledDeliveryDetails": t.proxy(
                renames[
                    "OrdersCustomBatchRequestEntryUpdateShipmentScheduledDeliveryDetailsIn"
                ]
            ).optional(),
            "lastPickupDate": t.string().optional(),
            "carrier": t.string().optional(),
            "deliveryDate": t.string().optional(),
            "shipmentId": t.string().optional(),
            "trackingId": t.string().optional(),
            "undeliveredDate": t.string().optional(),
            "readyPickupDate": t.string().optional(),
        }
    ).named(renames["OrdersUpdateShipmentRequestIn"])
    types["OrdersUpdateShipmentRequestOut"] = t.struct(
        {
            "operationId": t.string().optional(),
            "status": t.string().optional(),
            "scheduledDeliveryDetails": t.proxy(
                renames[
                    "OrdersCustomBatchRequestEntryUpdateShipmentScheduledDeliveryDetailsOut"
                ]
            ).optional(),
            "lastPickupDate": t.string().optional(),
            "carrier": t.string().optional(),
            "deliveryDate": t.string().optional(),
            "shipmentId": t.string().optional(),
            "trackingId": t.string().optional(),
            "undeliveredDate": t.string().optional(),
            "readyPickupDate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersUpdateShipmentRequestOut"])
    types["OrderPromotionItemIn"] = t.struct(
        {
            "productId": t.string().optional(),
            "quantity": t.integer().optional(),
            "offerId": t.string(),
            "lineItemId": t.string().optional(),
        }
    ).named(renames["OrderPromotionItemIn"])
    types["OrderPromotionItemOut"] = t.struct(
        {
            "productId": t.string().optional(),
            "quantity": t.integer().optional(),
            "offerId": t.string(),
            "lineItemId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderPromotionItemOut"])
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
    types["ActivateBuyOnGoogleProgramRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ActivateBuyOnGoogleProgramRequestIn"])
    types["ActivateBuyOnGoogleProgramRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ActivateBuyOnGoogleProgramRequestOut"])
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
    types["OrderreturnsRejectOperationIn"] = t.struct(
        {"reasonText": t.string().optional(), "reason": t.string().optional()}
    ).named(renames["OrderreturnsRejectOperationIn"])
    types["OrderreturnsRejectOperationOut"] = t.struct(
        {
            "reasonText": t.string().optional(),
            "reason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderreturnsRejectOperationOut"])
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
    types["OrderLineItemShippingDetailsMethodIn"] = t.struct(
        {
            "carrier": t.string().optional(),
            "methodName": t.string(),
            "maxDaysInTransit": t.integer(),
            "minDaysInTransit": t.integer(),
        }
    ).named(renames["OrderLineItemShippingDetailsMethodIn"])
    types["OrderLineItemShippingDetailsMethodOut"] = t.struct(
        {
            "carrier": t.string().optional(),
            "methodName": t.string(),
            "maxDaysInTransit": t.integer(),
            "minDaysInTransit": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderLineItemShippingDetailsMethodOut"])
    types["ListRepricingRuleReportsResponseIn"] = t.struct(
        {
            "repricingRuleReports": t.array(
                t.proxy(renames["RepricingRuleReportIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListRepricingRuleReportsResponseIn"])
    types["ListRepricingRuleReportsResponseOut"] = t.struct(
        {
            "repricingRuleReports": t.array(
                t.proxy(renames["RepricingRuleReportOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListRepricingRuleReportsResponseOut"])
    types["OrdersListResponseIn"] = t.struct(
        {
            "resources": t.array(t.proxy(renames["OrderIn"])),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["OrdersListResponseIn"])
    types["OrdersListResponseOut"] = t.struct(
        {
            "resources": t.array(t.proxy(renames["OrderOut"])),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersListResponseOut"])
    types["AccountBusinessInformationIn"] = t.struct(
        {
            "address": t.proxy(renames["AccountAddressIn"]).optional(),
            "phoneVerificationStatus": t.string().optional(),
            "customerService": t.proxy(renames["AccountCustomerServiceIn"]).optional(),
            "phoneNumber": t.string().optional(),
            "koreanBusinessRegistrationNumber": t.string().optional(),
        }
    ).named(renames["AccountBusinessInformationIn"])
    types["AccountBusinessInformationOut"] = t.struct(
        {
            "address": t.proxy(renames["AccountAddressOut"]).optional(),
            "phoneVerificationStatus": t.string().optional(),
            "customerService": t.proxy(renames["AccountCustomerServiceOut"]).optional(),
            "phoneNumber": t.string().optional(),
            "koreanBusinessRegistrationNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountBusinessInformationOut"])
    types["RequestReviewShoppingAdsRequestIn"] = t.struct(
        {"regionCode": t.string().optional()}
    ).named(renames["RequestReviewShoppingAdsRequestIn"])
    types["RequestReviewShoppingAdsRequestOut"] = t.struct(
        {
            "regionCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestReviewShoppingAdsRequestOut"])
    types["CaptureOrderRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CaptureOrderRequestIn"]
    )
    types["CaptureOrderRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CaptureOrderRequestOut"])
    types["PaymentServiceProviderLinkInfoIn"] = t.struct(
        {
            "externalAccountBusinessCountry": t.string().optional(),
            "externalAccountId": t.string().optional(),
        }
    ).named(renames["PaymentServiceProviderLinkInfoIn"])
    types["PaymentServiceProviderLinkInfoOut"] = t.struct(
        {
            "externalAccountBusinessCountry": t.string().optional(),
            "externalAccountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PaymentServiceProviderLinkInfoOut"])
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
    types["DatafeedStatusExampleIn"] = t.struct(
        {
            "lineNumber": t.string().optional(),
            "value": t.string().optional(),
            "itemId": t.string().optional(),
        }
    ).named(renames["DatafeedStatusExampleIn"])
    types["DatafeedStatusExampleOut"] = t.struct(
        {
            "lineNumber": t.string().optional(),
            "value": t.string().optional(),
            "itemId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatafeedStatusExampleOut"])
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
    types["FreeListingsProgramStatusRegionStatusIn"] = t.struct(
        {
            "onboardingIssues": t.array(t.string()).optional(),
            "reviewIneligibilityReasonDetails": t.proxy(
                renames["FreeListingsProgramStatusReviewIneligibilityReasonDetailsIn"]
            ).optional(),
            "regionCodes": t.array(t.string()).optional(),
            "reviewEligibilityStatus": t.string().optional(),
            "reviewIssues": t.array(t.string()).optional(),
            "disapprovalDate": t.string().optional(),
            "eligibilityStatus": t.string().optional(),
            "reviewIneligibilityReasonDescription": t.string().optional(),
            "reviewIneligibilityReason": t.string().optional(),
        }
    ).named(renames["FreeListingsProgramStatusRegionStatusIn"])
    types["FreeListingsProgramStatusRegionStatusOut"] = t.struct(
        {
            "onboardingIssues": t.array(t.string()).optional(),
            "reviewIneligibilityReasonDetails": t.proxy(
                renames["FreeListingsProgramStatusReviewIneligibilityReasonDetailsOut"]
            ).optional(),
            "regionCodes": t.array(t.string()).optional(),
            "reviewEligibilityStatus": t.string().optional(),
            "reviewIssues": t.array(t.string()).optional(),
            "disapprovalDate": t.string().optional(),
            "eligibilityStatus": t.string().optional(),
            "reviewIneligibilityReasonDescription": t.string().optional(),
            "reviewIneligibilityReason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FreeListingsProgramStatusRegionStatusOut"])
    types["OrdersCancelTestOrderByCustomerResponseIn"] = t.struct(
        {"kind": t.string().optional()}
    ).named(renames["OrdersCancelTestOrderByCustomerResponseIn"])
    types["OrdersCancelTestOrderByCustomerResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersCancelTestOrderByCustomerResponseOut"])
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
    types["OrdersCancelResponseIn"] = t.struct(
        {"kind": t.string().optional(), "executionStatus": t.string().optional()}
    ).named(renames["OrdersCancelResponseIn"])
    types["OrdersCancelResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "executionStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersCancelResponseOut"])
    types["GmbAccountsGmbAccountIn"] = t.struct(
        {
            "name": t.string().optional(),
            "type": t.string().optional(),
            "listingCount": t.string().optional(),
            "email": t.string().optional(),
        }
    ).named(renames["GmbAccountsGmbAccountIn"])
    types["GmbAccountsGmbAccountOut"] = t.struct(
        {
            "name": t.string().optional(),
            "type": t.string().optional(),
            "listingCount": t.string().optional(),
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GmbAccountsGmbAccountOut"])
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
    types["OrdersInStoreRefundLineItemRequestIn"] = t.struct(
        {
            "lineItemId": t.string().optional(),
            "operationId": t.string().optional(),
            "productId": t.string().optional(),
            "reason": t.string().optional(),
            "taxAmount": t.proxy(renames["PriceIn"]).optional(),
            "reasonText": t.string().optional(),
            "quantity": t.integer().optional(),
            "priceAmount": t.proxy(renames["PriceIn"]).optional(),
        }
    ).named(renames["OrdersInStoreRefundLineItemRequestIn"])
    types["OrdersInStoreRefundLineItemRequestOut"] = t.struct(
        {
            "lineItemId": t.string().optional(),
            "operationId": t.string().optional(),
            "productId": t.string().optional(),
            "reason": t.string().optional(),
            "taxAmount": t.proxy(renames["PriceOut"]).optional(),
            "reasonText": t.string().optional(),
            "quantity": t.integer().optional(),
            "priceAmount": t.proxy(renames["PriceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersInStoreRefundLineItemRequestOut"])
    types["AccountCredentialsIn"] = t.struct(
        {
            "accessToken": t.string().optional(),
            "purpose": t.string().optional(),
            "expiresIn": t.string().optional(),
        }
    ).named(renames["AccountCredentialsIn"])
    types["AccountCredentialsOut"] = t.struct(
        {
            "accessToken": t.string().optional(),
            "purpose": t.string().optional(),
            "expiresIn": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountCredentialsOut"])
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
    types["ValueIn"] = t.struct(
        {
            "noShipping": t.boolean().optional(),
            "pricePercentage": t.string().optional(),
            "carrierRateName": t.string().optional(),
            "subtableName": t.string().optional(),
            "flatRate": t.proxy(renames["PriceIn"]).optional(),
        }
    ).named(renames["ValueIn"])
    types["ValueOut"] = t.struct(
        {
            "noShipping": t.boolean().optional(),
            "pricePercentage": t.string().optional(),
            "carrierRateName": t.string().optional(),
            "subtableName": t.string().optional(),
            "flatRate": t.proxy(renames["PriceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValueOut"])
    types["LiasettingsSetInventoryVerificationContactResponseIn"] = t.struct(
        {"kind": t.string().optional()}
    ).named(renames["LiasettingsSetInventoryVerificationContactResponseIn"])
    types["LiasettingsSetInventoryVerificationContactResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiasettingsSetInventoryVerificationContactResponseOut"])
    types["OrdersAcknowledgeRequestIn"] = t.struct(
        {"operationId": t.string().optional()}
    ).named(renames["OrdersAcknowledgeRequestIn"])
    types["OrdersAcknowledgeRequestOut"] = t.struct(
        {
            "operationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersAcknowledgeRequestOut"])
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
    types["AccountsLinkResponseIn"] = t.struct({"kind": t.string().optional()}).named(
        renames["AccountsLinkResponseIn"]
    )
    types["AccountsLinkResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountsLinkResponseOut"])
    types["LiasettingsGetAccessibleGmbAccountsResponseIn"] = t.struct(
        {
            "gmbAccounts": t.array(
                t.proxy(renames["GmbAccountsGmbAccountIn"])
            ).optional(),
            "accountId": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["LiasettingsGetAccessibleGmbAccountsResponseIn"])
    types["LiasettingsGetAccessibleGmbAccountsResponseOut"] = t.struct(
        {
            "gmbAccounts": t.array(
                t.proxy(renames["GmbAccountsGmbAccountOut"])
            ).optional(),
            "accountId": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiasettingsGetAccessibleGmbAccountsResponseOut"])
    types["LinkedAccountIn"] = t.struct(
        {
            "services": t.array(t.proxy(renames["LinkServiceIn"])).optional(),
            "linkedAccountId": t.string().optional(),
        }
    ).named(renames["LinkedAccountIn"])
    types["LinkedAccountOut"] = t.struct(
        {
            "services": t.array(t.proxy(renames["LinkServiceOut"])).optional(),
            "linkedAccountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinkedAccountOut"])
    types["AccountImageImprovementsSettingsIn"] = t.struct(
        {"allowAutomaticImageImprovements": t.boolean().optional()}
    ).named(renames["AccountImageImprovementsSettingsIn"])
    types["AccountImageImprovementsSettingsOut"] = t.struct(
        {
            "allowAutomaticImageImprovements": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountImageImprovementsSettingsOut"])
    types["ShippingsettingsListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "resources": t.array(t.proxy(renames["ShippingSettingsIn"])),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ShippingsettingsListResponseIn"])
    types["ShippingsettingsListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "resources": t.array(t.proxy(renames["ShippingSettingsOut"])),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShippingsettingsListResponseOut"])
    types["LiasettingsRequestGmbAccessResponseIn"] = t.struct(
        {"kind": t.string().optional()}
    ).named(renames["LiasettingsRequestGmbAccessResponseIn"])
    types["LiasettingsRequestGmbAccessResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiasettingsRequestGmbAccessResponseOut"])
    types["InvoiceSummaryAdditionalChargeSummaryIn"] = t.struct(
        {
            "totalAmount": t.proxy(renames["AmountIn"]).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["InvoiceSummaryAdditionalChargeSummaryIn"])
    types["InvoiceSummaryAdditionalChargeSummaryOut"] = t.struct(
        {
            "totalAmount": t.proxy(renames["AmountOut"]).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InvoiceSummaryAdditionalChargeSummaryOut"])
    types["OrderreturnsReturnItemIn"] = t.struct(
        {
            "refund": t.proxy(renames["OrderreturnsRefundOperationIn"]).optional(),
            "returnItemId": t.string().optional(),
            "reject": t.proxy(renames["OrderreturnsRejectOperationIn"]).optional(),
        }
    ).named(renames["OrderreturnsReturnItemIn"])
    types["OrderreturnsReturnItemOut"] = t.struct(
        {
            "refund": t.proxy(renames["OrderreturnsRefundOperationOut"]).optional(),
            "returnItemId": t.string().optional(),
            "reject": t.proxy(renames["OrderreturnsRejectOperationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderreturnsReturnItemOut"])
    types["PosSaleResponseIn"] = t.struct(
        {
            "contentLanguage": t.string(),
            "quantity": t.string(),
            "itemId": t.string(),
            "price": t.proxy(renames["PriceIn"]),
            "timestamp": t.string(),
            "saleId": t.string().optional(),
            "storeCode": t.string(),
            "kind": t.string().optional(),
            "targetCountry": t.string(),
            "gtin": t.string().optional(),
        }
    ).named(renames["PosSaleResponseIn"])
    types["PosSaleResponseOut"] = t.struct(
        {
            "contentLanguage": t.string(),
            "quantity": t.string(),
            "itemId": t.string(),
            "price": t.proxy(renames["PriceOut"]),
            "timestamp": t.string(),
            "saleId": t.string().optional(),
            "storeCode": t.string(),
            "kind": t.string().optional(),
            "targetCountry": t.string(),
            "gtin": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PosSaleResponseOut"])
    types["SettlementtransactionsListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "resources": t.array(t.proxy(renames["SettlementTransactionIn"])),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["SettlementtransactionsListResponseIn"])
    types["SettlementtransactionsListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "resources": t.array(t.proxy(renames["SettlementTransactionOut"])),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SettlementtransactionsListResponseOut"])
    types["ProductUnitPricingBaseMeasureIn"] = t.struct(
        {"unit": t.string().optional(), "value": t.string().optional()}
    ).named(renames["ProductUnitPricingBaseMeasureIn"])
    types["ProductUnitPricingBaseMeasureOut"] = t.struct(
        {
            "unit": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductUnitPricingBaseMeasureOut"])
    types["ProductStatusItemLevelIssueIn"] = t.struct(
        {
            "resolution": t.string().optional(),
            "servability": t.string().optional(),
            "applicableCountries": t.array(t.string()).optional(),
            "destination": t.string().optional(),
            "attributeName": t.string().optional(),
            "description": t.string().optional(),
            "documentation": t.string().optional(),
            "code": t.string().optional(),
            "detail": t.string().optional(),
        }
    ).named(renames["ProductStatusItemLevelIssueIn"])
    types["ProductStatusItemLevelIssueOut"] = t.struct(
        {
            "resolution": t.string().optional(),
            "servability": t.string().optional(),
            "applicableCountries": t.array(t.string()).optional(),
            "destination": t.string().optional(),
            "attributeName": t.string().optional(),
            "description": t.string().optional(),
            "documentation": t.string().optional(),
            "code": t.string().optional(),
            "detail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductStatusItemLevelIssueOut"])
    types["OrdersReturnRefundLineItemResponseIn"] = t.struct(
        {"executionStatus": t.string().optional(), "kind": t.string().optional()}
    ).named(renames["OrdersReturnRefundLineItemResponseIn"])
    types["OrdersReturnRefundLineItemResponseOut"] = t.struct(
        {
            "executionStatus": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersReturnRefundLineItemResponseOut"])
    types["ProductDimensionIn"] = t.struct(
        {"value": t.number(), "unit": t.string()}
    ).named(renames["ProductDimensionIn"])
    types["ProductDimensionOut"] = t.struct(
        {
            "value": t.number(),
            "unit": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductDimensionOut"])
    types["MetricsIn"] = t.struct(
        {
            "returnsMicros": t.string().optional(),
            "shippedItems": t.string().optional(),
            "clicks": t.string().optional(),
            "aos": t.number().optional(),
            "daysToShip": t.number().optional(),
            "orders": t.string().optional(),
            "conversions": t.number().optional(),
            "returnedItems": t.string().optional(),
            "aovMicros": t.number().optional(),
            "returnRate": t.number().optional(),
            "itemDaysToShip": t.number().optional(),
            "shippedItemSalesMicros": t.string().optional(),
            "impressions": t.string().optional(),
            "conversionValueMicros": t.string().optional(),
            "orderedItems": t.string().optional(),
            "rejectedItems": t.string().optional(),
            "orderedItemSalesMicros": t.string().optional(),
            "conversionRate": t.number().optional(),
            "itemFillRate": t.number().optional(),
            "unshippedOrders": t.number().optional(),
            "shippedOrders": t.string().optional(),
            "ctr": t.number().optional(),
            "unshippedItems": t.number().optional(),
        }
    ).named(renames["MetricsIn"])
    types["MetricsOut"] = t.struct(
        {
            "returnsMicros": t.string().optional(),
            "shippedItems": t.string().optional(),
            "clicks": t.string().optional(),
            "aos": t.number().optional(),
            "daysToShip": t.number().optional(),
            "orders": t.string().optional(),
            "conversions": t.number().optional(),
            "returnedItems": t.string().optional(),
            "aovMicros": t.number().optional(),
            "returnRate": t.number().optional(),
            "itemDaysToShip": t.number().optional(),
            "shippedItemSalesMicros": t.string().optional(),
            "impressions": t.string().optional(),
            "conversionValueMicros": t.string().optional(),
            "orderedItems": t.string().optional(),
            "rejectedItems": t.string().optional(),
            "orderedItemSalesMicros": t.string().optional(),
            "conversionRate": t.number().optional(),
            "itemFillRate": t.number().optional(),
            "unshippedOrders": t.number().optional(),
            "shippedOrders": t.string().optional(),
            "ctr": t.number().optional(),
            "unshippedItems": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricsOut"])
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
    types["ReturnPolicyOnlineReturnReasonCategoryInfoIn"] = t.struct(
        {
            "returnShippingFee": t.proxy(
                renames["ReturnPolicyOnlineReturnShippingFeeIn"]
            ).optional(),
            "returnLabelSource": t.string().optional(),
            "returnReasonCategory": t.string().optional(),
        }
    ).named(renames["ReturnPolicyOnlineReturnReasonCategoryInfoIn"])
    types["ReturnPolicyOnlineReturnReasonCategoryInfoOut"] = t.struct(
        {
            "returnShippingFee": t.proxy(
                renames["ReturnPolicyOnlineReturnShippingFeeOut"]
            ).optional(),
            "returnLabelSource": t.string().optional(),
            "returnReasonCategory": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReturnPolicyOnlineReturnReasonCategoryInfoOut"])
    types["AccountsListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "resources": t.array(t.proxy(renames["AccountIn"])),
        }
    ).named(renames["AccountsListResponseIn"])
    types["AccountsListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "resources": t.array(t.proxy(renames["AccountOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountsListResponseOut"])
    types["ShippingsettingsGetSupportedHolidaysResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "holidays": t.array(t.proxy(renames["HolidaysHolidayIn"])).optional(),
        }
    ).named(renames["ShippingsettingsGetSupportedHolidaysResponseIn"])
    types["ShippingsettingsGetSupportedHolidaysResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "holidays": t.array(t.proxy(renames["HolidaysHolidayOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShippingsettingsGetSupportedHolidaysResponseOut"])
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
    types["UnitInvoiceTaxLineIn"] = t.struct(
        {
            "taxAmount": t.proxy(renames["PriceIn"]).optional(),
            "taxType": t.string().optional(),
            "taxName": t.string().optional(),
        }
    ).named(renames["UnitInvoiceTaxLineIn"])
    types["UnitInvoiceTaxLineOut"] = t.struct(
        {
            "taxAmount": t.proxy(renames["PriceOut"]).optional(),
            "taxType": t.string().optional(),
            "taxName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UnitInvoiceTaxLineOut"])
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
    types["TestOrderLineItemIn"] = t.struct(
        {
            "returnInfo": t.proxy(renames["OrderLineItemReturnInfoIn"]),
            "shippingDetails": t.proxy(renames["OrderLineItemShippingDetailsIn"]),
            "product": t.proxy(renames["TestOrderLineItemProductIn"]),
            "quantityOrdered": t.integer(),
        }
    ).named(renames["TestOrderLineItemIn"])
    types["TestOrderLineItemOut"] = t.struct(
        {
            "returnInfo": t.proxy(renames["OrderLineItemReturnInfoOut"]),
            "shippingDetails": t.proxy(renames["OrderLineItemShippingDetailsOut"]),
            "product": t.proxy(renames["TestOrderLineItemProductOut"]),
            "quantityOrdered": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestOrderLineItemOut"])
    types["RepricingRuleRestrictionBoundaryIn"] = t.struct(
        {"priceDelta": t.string().optional(), "percentageDelta": t.integer().optional()}
    ).named(renames["RepricingRuleRestrictionBoundaryIn"])
    types["RepricingRuleRestrictionBoundaryOut"] = t.struct(
        {
            "priceDelta": t.string().optional(),
            "percentageDelta": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepricingRuleRestrictionBoundaryOut"])
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
    types["ReturnPolicyPolicyIn"] = t.struct(
        {
            "numberOfDays": t.string().optional(),
            "type": t.string().optional(),
            "lastReturnDate": t.string(),
        }
    ).named(renames["ReturnPolicyPolicyIn"])
    types["ReturnPolicyPolicyOut"] = t.struct(
        {
            "numberOfDays": t.string().optional(),
            "type": t.string().optional(),
            "lastReturnDate": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReturnPolicyPolicyOut"])
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
    types["OrdersCustomBatchRequestEntryCreateTestReturnReturnItemIn"] = t.struct(
        {"quantity": t.integer().optional(), "lineItemId": t.string().optional()}
    ).named(renames["OrdersCustomBatchRequestEntryCreateTestReturnReturnItemIn"])
    types["OrdersCustomBatchRequestEntryCreateTestReturnReturnItemOut"] = t.struct(
        {
            "quantity": t.integer().optional(),
            "lineItemId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersCustomBatchRequestEntryCreateTestReturnReturnItemOut"])
    types["OrderShipmentIn"] = t.struct(
        {
            "trackingId": t.string().optional(),
            "deliveryDate": t.string().optional(),
            "shipmentGroupId": t.string().optional(),
            "lineItems": t.array(
                t.proxy(renames["OrderShipmentLineItemShipmentIn"])
            ).optional(),
            "id": t.string().optional(),
            "scheduledDeliveryDetails": t.proxy(
                renames["OrderShipmentScheduledDeliveryDetailsIn"]
            ).optional(),
            "carrier": t.string().optional(),
            "creationDate": t.string().optional(),
            "status": t.string().optional(),
        }
    ).named(renames["OrderShipmentIn"])
    types["OrderShipmentOut"] = t.struct(
        {
            "trackingId": t.string().optional(),
            "deliveryDate": t.string().optional(),
            "shipmentGroupId": t.string().optional(),
            "lineItems": t.array(
                t.proxy(renames["OrderShipmentLineItemShipmentOut"])
            ).optional(),
            "id": t.string().optional(),
            "scheduledDeliveryDetails": t.proxy(
                renames["OrderShipmentScheduledDeliveryDetailsOut"]
            ).optional(),
            "carrier": t.string().optional(),
            "creationDate": t.string().optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderShipmentOut"])
    types["CollectionStatusItemLevelIssueIn"] = t.struct(
        {
            "applicableCountries": t.array(t.string()).optional(),
            "detail": t.string().optional(),
            "servability": t.string().optional(),
            "resolution": t.string().optional(),
            "attributeName": t.string().optional(),
            "destination": t.string().optional(),
            "documentation": t.string().optional(),
            "code": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["CollectionStatusItemLevelIssueIn"])
    types["CollectionStatusItemLevelIssueOut"] = t.struct(
        {
            "applicableCountries": t.array(t.string()).optional(),
            "detail": t.string().optional(),
            "servability": t.string().optional(),
            "resolution": t.string().optional(),
            "attributeName": t.string().optional(),
            "destination": t.string().optional(),
            "documentation": t.string().optional(),
            "code": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CollectionStatusItemLevelIssueOut"])
    types["OrdersAdvanceTestOrderResponseIn"] = t.struct(
        {"kind": t.string().optional()}
    ).named(renames["OrdersAdvanceTestOrderResponseIn"])
    types["OrdersAdvanceTestOrderResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersAdvanceTestOrderResponseOut"])
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
    types["OrdersRejectReturnLineItemResponseIn"] = t.struct(
        {"executionStatus": t.string().optional(), "kind": t.string().optional()}
    ).named(renames["OrdersRejectReturnLineItemResponseIn"])
    types["OrdersRejectReturnLineItemResponseOut"] = t.struct(
        {
            "executionStatus": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersRejectReturnLineItemResponseOut"])
    types["RepricingRuleIn"] = t.struct(
        {
            "cogsBasedRule": t.proxy(
                renames["RepricingRuleCostOfGoodsSaleRuleIn"]
            ).optional(),
            "restriction": t.proxy(renames["RepricingRuleRestrictionIn"]),
            "title": t.string().optional(),
            "paused": t.boolean().optional(),
            "countryCode": t.string(),
            "languageCode": t.string(),
            "type": t.string(),
            "effectiveTimePeriod": t.proxy(renames["RepricingRuleEffectiveTimeIn"]),
            "statsBasedRule": t.proxy(
                renames["RepricingRuleStatsBasedRuleIn"]
            ).optional(),
            "eligibleOfferMatcher": t.proxy(
                renames["RepricingRuleEligibleOfferMatcherIn"]
            ),
        }
    ).named(renames["RepricingRuleIn"])
    types["RepricingRuleOut"] = t.struct(
        {
            "cogsBasedRule": t.proxy(
                renames["RepricingRuleCostOfGoodsSaleRuleOut"]
            ).optional(),
            "restriction": t.proxy(renames["RepricingRuleRestrictionOut"]),
            "title": t.string().optional(),
            "ruleId": t.string().optional(),
            "paused": t.boolean().optional(),
            "countryCode": t.string(),
            "languageCode": t.string(),
            "type": t.string(),
            "merchantId": t.string().optional(),
            "effectiveTimePeriod": t.proxy(renames["RepricingRuleEffectiveTimeOut"]),
            "statsBasedRule": t.proxy(
                renames["RepricingRuleStatsBasedRuleOut"]
            ).optional(),
            "eligibleOfferMatcher": t.proxy(
                renames["RepricingRuleEligibleOfferMatcherOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepricingRuleOut"])
    types["OrderreportsListDisbursementsResponseIn"] = t.struct(
        {
            "disbursements": t.array(
                t.proxy(renames["OrderReportDisbursementIn"])
            ).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["OrderreportsListDisbursementsResponseIn"])
    types["OrderreportsListDisbursementsResponseOut"] = t.struct(
        {
            "disbursements": t.array(
                t.proxy(renames["OrderReportDisbursementOut"])
            ).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderreportsListDisbursementsResponseOut"])
    types["HolidaysHolidayIn"] = t.struct(
        {
            "id": t.string().optional(),
            "deliveryGuaranteeHour": t.string().optional(),
            "type": t.string().optional(),
            "countryCode": t.string().optional(),
            "deliveryGuaranteeDate": t.string().optional(),
            "date": t.string().optional(),
        }
    ).named(renames["HolidaysHolidayIn"])
    types["HolidaysHolidayOut"] = t.struct(
        {
            "id": t.string().optional(),
            "deliveryGuaranteeHour": t.string().optional(),
            "type": t.string().optional(),
            "countryCode": t.string().optional(),
            "deliveryGuaranteeDate": t.string().optional(),
            "date": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HolidaysHolidayOut"])
    types["PauseBuyOnGoogleProgramRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["PauseBuyOnGoogleProgramRequestIn"])
    types["PauseBuyOnGoogleProgramRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PauseBuyOnGoogleProgramRequestOut"])
    types["DateTimeIn"] = t.struct(
        {
            "seconds": t.integer().optional(),
            "nanos": t.integer().optional(),
            "month": t.integer().optional(),
            "year": t.integer().optional(),
            "hours": t.integer().optional(),
            "minutes": t.integer().optional(),
            "utcOffset": t.string().optional(),
            "timeZone": t.proxy(renames["TimeZoneIn"]).optional(),
            "day": t.integer().optional(),
        }
    ).named(renames["DateTimeIn"])
    types["DateTimeOut"] = t.struct(
        {
            "seconds": t.integer().optional(),
            "nanos": t.integer().optional(),
            "month": t.integer().optional(),
            "year": t.integer().optional(),
            "hours": t.integer().optional(),
            "minutes": t.integer().optional(),
            "utcOffset": t.string().optional(),
            "timeZone": t.proxy(renames["TimeZoneOut"]).optional(),
            "day": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateTimeOut"])
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
    types["ReturnpolicyCustomBatchResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "entries": t.array(
                t.proxy(renames["ReturnpolicyCustomBatchResponseEntryIn"])
            ).optional(),
        }
    ).named(renames["ReturnpolicyCustomBatchResponseIn"])
    types["ReturnpolicyCustomBatchResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "entries": t.array(
                t.proxy(renames["ReturnpolicyCustomBatchResponseEntryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReturnpolicyCustomBatchResponseOut"])
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
    types["AccountsLinkRequestIn"] = t.struct(
        {
            "paymentServiceProviderLinkInfo": t.proxy(
                renames["PaymentServiceProviderLinkInfoIn"]
            ).optional(),
            "services": t.array(t.string()).optional(),
            "eCommercePlatformLinkInfo": t.proxy(
                renames["ECommercePlatformLinkInfoIn"]
            ).optional(),
            "action": t.string().optional(),
            "linkType": t.string().optional(),
            "linkedAccountId": t.string().optional(),
        }
    ).named(renames["AccountsLinkRequestIn"])
    types["AccountsLinkRequestOut"] = t.struct(
        {
            "paymentServiceProviderLinkInfo": t.proxy(
                renames["PaymentServiceProviderLinkInfoOut"]
            ).optional(),
            "services": t.array(t.string()).optional(),
            "eCommercePlatformLinkInfo": t.proxy(
                renames["ECommercePlatformLinkInfoOut"]
            ).optional(),
            "action": t.string().optional(),
            "linkType": t.string().optional(),
            "linkedAccountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountsLinkRequestOut"])
    types["PickupCarrierServiceIn"] = t.struct(
        {"carrierName": t.string().optional(), "serviceName": t.string().optional()}
    ).named(renames["PickupCarrierServiceIn"])
    types["PickupCarrierServiceOut"] = t.struct(
        {
            "carrierName": t.string().optional(),
            "serviceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PickupCarrierServiceOut"])
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
    types["AttributionSettingsIn"] = t.struct(
        {
            "conversionType": t.array(
                t.proxy(renames["AttributionSettingsConversionTypeIn"])
            ).optional(),
            "attributionLookbackWindowInDays": t.integer(),
            "attributionModel": t.string(),
        }
    ).named(renames["AttributionSettingsIn"])
    types["AttributionSettingsOut"] = t.struct(
        {
            "conversionType": t.array(
                t.proxy(renames["AttributionSettingsConversionTypeOut"])
            ).optional(),
            "attributionLookbackWindowInDays": t.integer(),
            "attributionModel": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttributionSettingsOut"])
    types["OrdersInStoreRefundLineItemResponseIn"] = t.struct(
        {"kind": t.string().optional(), "executionStatus": t.string().optional()}
    ).named(renames["OrdersInStoreRefundLineItemResponseIn"])
    types["OrdersInStoreRefundLineItemResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "executionStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersInStoreRefundLineItemResponseOut"])
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
    types["ProductAmountIn"] = t.struct(
        {
            "priceAmount": t.proxy(renames["PriceIn"]).optional(),
            "remittedTaxAmount": t.proxy(renames["PriceIn"]).optional(),
            "taxAmount": t.proxy(renames["PriceIn"]).optional(),
        }
    ).named(renames["ProductAmountIn"])
    types["ProductAmountOut"] = t.struct(
        {
            "priceAmount": t.proxy(renames["PriceOut"]).optional(),
            "remittedTaxAmount": t.proxy(renames["PriceOut"]).optional(),
            "taxAmount": t.proxy(renames["PriceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductAmountOut"])
    types["ProductIn"] = t.struct(
        {
            "material": t.string().optional(),
            "productHeight": t.proxy(renames["ProductDimensionIn"]).optional(),
            "customLabel3": t.string().optional(),
            "mobileLinkTemplate": t.string().optional(),
            "productWeight": t.proxy(renames["ProductWeightIn"]).optional(),
            "adsGrouping": t.string().optional(),
            "includedDestinations": t.array(t.string()).optional(),
            "salePriceEffectiveDate": t.string().optional(),
            "unitPricingBaseMeasure": t.proxy(
                renames["ProductUnitPricingBaseMeasureIn"]
            ).optional(),
            "productDetails": t.array(
                t.proxy(renames["ProductProductDetailIn"])
            ).optional(),
            "mpn": t.string().optional(),
            "channel": t.string(),
            "excludedDestinations": t.array(t.string()).optional(),
            "additionalSizeType": t.string().optional(),
            "taxCategory": t.string().optional(),
            "displayAdsTitle": t.string().optional(),
            "customLabel1": t.string().optional(),
            "customLabel0": t.string().optional(),
            "id": t.string().optional(),
            "minHandlingTime": t.string().optional(),
            "itemGroupId": t.string().optional(),
            "customLabel4": t.string().optional(),
            "linkTemplate": t.string().optional(),
            "costOfGoodsSold": t.proxy(renames["PriceIn"]).optional(),
            "contentLanguage": t.string(),
            "productLength": t.proxy(renames["ProductDimensionIn"]).optional(),
            "shippingWeight": t.proxy(renames["ProductShippingWeightIn"]).optional(),
            "title": t.string().optional(),
            "productHighlights": t.array(t.string()).optional(),
            "expirationDate": t.string().optional(),
            "multipack": t.string().optional(),
            "cloudExportAdditionalProperties": t.array(
                t.proxy(renames["CloudExportAdditionalPropertiesIn"])
            ).optional(),
            "displayAdsId": t.string().optional(),
            "externalSellerId": t.string(),
            "productWidth": t.proxy(renames["ProductDimensionIn"]).optional(),
            "imageLink": t.string().optional(),
            "identifierExists": t.boolean().optional(),
            "ageGroup": t.string().optional(),
            "brand": t.string().optional(),
            "customLabel2": t.string().optional(),
            "shipping": t.array(t.proxy(renames["ProductShippingIn"])).optional(),
            "gtin": t.string().optional(),
            "mobileLink": t.string().optional(),
            "kind": t.string().optional(),
            "description": t.string().optional(),
            "additionalImageLinks": t.array(t.string()).optional(),
            "pickupMethod": t.string().optional(),
            "sellOnGoogleQuantity": t.string().optional(),
            "targetCountry": t.string(),
            "canonicalLink": t.string().optional(),
            "adult": t.boolean().optional(),
            "color": t.string().optional(),
            "displayAdsLink": t.string().optional(),
            "productTypes": t.array(t.string()).optional(),
            "condition": t.string().optional(),
            "transitTimeLabel": t.string().optional(),
            "promotionIds": t.array(t.string()).optional(),
            "availabilityDate": t.string().optional(),
            "shoppingAdsExcludedCountries": t.array(t.string()).optional(),
            "sizes": t.array(t.string()).optional(),
            "price": t.proxy(renames["PriceIn"]).optional(),
            "pause": t.string().optional(),
            "shippingHeight": t.proxy(renames["ProductShippingDimensionIn"]).optional(),
            "shippingLength": t.proxy(renames["ProductShippingDimensionIn"]).optional(),
            "unitPricingMeasure": t.proxy(
                renames["ProductUnitPricingMeasureIn"]
            ).optional(),
            "pickupSla": t.string().optional(),
            "taxes": t.array(t.proxy(renames["ProductTaxIn"])).optional(),
            "googleProductCategory": t.string().optional(),
            "maxEnergyEfficiencyClass": t.string().optional(),
            "energyEfficiencyClass": t.string().optional(),
            "gender": t.string().optional(),
            "source": t.string().optional(),
            "subscriptionCost": t.proxy(
                renames["ProductSubscriptionCostIn"]
            ).optional(),
            "pattern": t.string().optional(),
            "sizeType": t.string().optional(),
            "adsRedirect": t.string().optional(),
            "adsLabels": t.array(t.string()).optional(),
            "sizeSystem": t.string().optional(),
            "availability": t.string().optional(),
            "loyaltyPoints": t.proxy(renames["LoyaltyPointsIn"]).optional(),
            "installment": t.proxy(renames["InstallmentIn"]).optional(),
            "shippingLabel": t.string().optional(),
            "displayAdsSimilarIds": t.array(t.string()).optional(),
            "shippingWidth": t.proxy(renames["ProductShippingDimensionIn"]).optional(),
            "offerId": t.string(),
            "lifestyleImageLinks": t.array(t.string()).optional(),
            "minEnergyEfficiencyClass": t.string().optional(),
            "salePrice": t.proxy(renames["PriceIn"]).optional(),
            "isBundle": t.boolean().optional(),
            "link": t.string().optional(),
            "displayAdsValue": t.number().optional(),
            "feedLabel": t.string().optional(),
            "maxHandlingTime": t.string().optional(),
            "disclosureDate": t.string().optional(),
            "customAttributes": t.array(
                t.proxy(renames["CustomAttributeIn"])
            ).optional(),
        }
    ).named(renames["ProductIn"])
    types["ProductOut"] = t.struct(
        {
            "material": t.string().optional(),
            "productHeight": t.proxy(renames["ProductDimensionOut"]).optional(),
            "customLabel3": t.string().optional(),
            "mobileLinkTemplate": t.string().optional(),
            "productWeight": t.proxy(renames["ProductWeightOut"]).optional(),
            "adsGrouping": t.string().optional(),
            "includedDestinations": t.array(t.string()).optional(),
            "salePriceEffectiveDate": t.string().optional(),
            "unitPricingBaseMeasure": t.proxy(
                renames["ProductUnitPricingBaseMeasureOut"]
            ).optional(),
            "productDetails": t.array(
                t.proxy(renames["ProductProductDetailOut"])
            ).optional(),
            "mpn": t.string().optional(),
            "channel": t.string(),
            "excludedDestinations": t.array(t.string()).optional(),
            "additionalSizeType": t.string().optional(),
            "taxCategory": t.string().optional(),
            "displayAdsTitle": t.string().optional(),
            "customLabel1": t.string().optional(),
            "customLabel0": t.string().optional(),
            "id": t.string().optional(),
            "minHandlingTime": t.string().optional(),
            "itemGroupId": t.string().optional(),
            "customLabel4": t.string().optional(),
            "linkTemplate": t.string().optional(),
            "costOfGoodsSold": t.proxy(renames["PriceOut"]).optional(),
            "contentLanguage": t.string(),
            "productLength": t.proxy(renames["ProductDimensionOut"]).optional(),
            "shippingWeight": t.proxy(renames["ProductShippingWeightOut"]).optional(),
            "title": t.string().optional(),
            "productHighlights": t.array(t.string()).optional(),
            "expirationDate": t.string().optional(),
            "multipack": t.string().optional(),
            "cloudExportAdditionalProperties": t.array(
                t.proxy(renames["CloudExportAdditionalPropertiesOut"])
            ).optional(),
            "displayAdsId": t.string().optional(),
            "externalSellerId": t.string(),
            "productWidth": t.proxy(renames["ProductDimensionOut"]).optional(),
            "imageLink": t.string().optional(),
            "identifierExists": t.boolean().optional(),
            "ageGroup": t.string().optional(),
            "brand": t.string().optional(),
            "customLabel2": t.string().optional(),
            "shipping": t.array(t.proxy(renames["ProductShippingOut"])).optional(),
            "gtin": t.string().optional(),
            "mobileLink": t.string().optional(),
            "kind": t.string().optional(),
            "description": t.string().optional(),
            "additionalImageLinks": t.array(t.string()).optional(),
            "pickupMethod": t.string().optional(),
            "sellOnGoogleQuantity": t.string().optional(),
            "targetCountry": t.string(),
            "canonicalLink": t.string().optional(),
            "adult": t.boolean().optional(),
            "color": t.string().optional(),
            "displayAdsLink": t.string().optional(),
            "productTypes": t.array(t.string()).optional(),
            "condition": t.string().optional(),
            "transitTimeLabel": t.string().optional(),
            "promotionIds": t.array(t.string()).optional(),
            "availabilityDate": t.string().optional(),
            "shoppingAdsExcludedCountries": t.array(t.string()).optional(),
            "sizes": t.array(t.string()).optional(),
            "price": t.proxy(renames["PriceOut"]).optional(),
            "pause": t.string().optional(),
            "shippingHeight": t.proxy(
                renames["ProductShippingDimensionOut"]
            ).optional(),
            "shippingLength": t.proxy(
                renames["ProductShippingDimensionOut"]
            ).optional(),
            "unitPricingMeasure": t.proxy(
                renames["ProductUnitPricingMeasureOut"]
            ).optional(),
            "pickupSla": t.string().optional(),
            "taxes": t.array(t.proxy(renames["ProductTaxOut"])).optional(),
            "googleProductCategory": t.string().optional(),
            "maxEnergyEfficiencyClass": t.string().optional(),
            "energyEfficiencyClass": t.string().optional(),
            "gender": t.string().optional(),
            "source": t.string().optional(),
            "subscriptionCost": t.proxy(
                renames["ProductSubscriptionCostOut"]
            ).optional(),
            "pattern": t.string().optional(),
            "sizeType": t.string().optional(),
            "adsRedirect": t.string().optional(),
            "adsLabels": t.array(t.string()).optional(),
            "sizeSystem": t.string().optional(),
            "availability": t.string().optional(),
            "loyaltyPoints": t.proxy(renames["LoyaltyPointsOut"]).optional(),
            "installment": t.proxy(renames["InstallmentOut"]).optional(),
            "shippingLabel": t.string().optional(),
            "displayAdsSimilarIds": t.array(t.string()).optional(),
            "shippingWidth": t.proxy(renames["ProductShippingDimensionOut"]).optional(),
            "offerId": t.string(),
            "lifestyleImageLinks": t.array(t.string()).optional(),
            "minEnergyEfficiencyClass": t.string().optional(),
            "salePrice": t.proxy(renames["PriceOut"]).optional(),
            "isBundle": t.boolean().optional(),
            "link": t.string().optional(),
            "displayAdsValue": t.number().optional(),
            "feedLabel": t.string().optional(),
            "maxHandlingTime": t.string().optional(),
            "disclosureDate": t.string().optional(),
            "customAttributes": t.array(
                t.proxy(renames["CustomAttributeOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductOut"])
    types["OrderCustomerIn"] = t.struct(
        {
            "marketingRightsInfo": t.proxy(
                renames["OrderCustomerMarketingRightsInfoIn"]
            ).optional(),
            "invoiceReceivingEmail": t.string().optional(),
            "loyaltyInfo": t.proxy(renames["OrderCustomerLoyaltyInfoIn"]).optional(),
            "fullName": t.string().optional(),
        }
    ).named(renames["OrderCustomerIn"])
    types["OrderCustomerOut"] = t.struct(
        {
            "marketingRightsInfo": t.proxy(
                renames["OrderCustomerMarketingRightsInfoOut"]
            ).optional(),
            "invoiceReceivingEmail": t.string().optional(),
            "loyaltyInfo": t.proxy(renames["OrderCustomerLoyaltyInfoOut"]).optional(),
            "fullName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderCustomerOut"])
    types["ServiceStoreConfigIn"] = t.struct(
        {
            "serviceRadius": t.proxy(renames["DistanceIn"]).optional(),
            "storeCodes": t.array(t.string()).optional(),
            "cutoffConfig": t.proxy(
                renames["ServiceStoreConfigCutoffConfigIn"]
            ).optional(),
            "storeServiceType": t.string().optional(),
        }
    ).named(renames["ServiceStoreConfigIn"])
    types["ServiceStoreConfigOut"] = t.struct(
        {
            "serviceRadius": t.proxy(renames["DistanceOut"]).optional(),
            "storeCodes": t.array(t.string()).optional(),
            "cutoffConfig": t.proxy(
                renames["ServiceStoreConfigCutoffConfigOut"]
            ).optional(),
            "storeServiceType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceStoreConfigOut"])
    types["SearchRequestIn"] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "pageToken": t.string().optional(),
            "query": t.string(),
        }
    ).named(renames["SearchRequestIn"])
    types["SearchRequestOut"] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "pageToken": t.string().optional(),
            "query": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchRequestOut"])
    types["TransitTableIn"] = t.struct(
        {
            "postalCodeGroupNames": t.array(t.string()).optional(),
            "transitTimeLabels": t.array(t.string()).optional(),
            "rows": t.array(t.proxy(renames["TransitTableTransitTimeRowIn"])),
        }
    ).named(renames["TransitTableIn"])
    types["TransitTableOut"] = t.struct(
        {
            "postalCodeGroupNames": t.array(t.string()).optional(),
            "transitTimeLabels": t.array(t.string()).optional(),
            "rows": t.array(t.proxy(renames["TransitTableTransitTimeRowOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransitTableOut"])
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
    types["RegionPostalCodeAreaIn"] = t.struct(
        {
            "regionCode": t.string(),
            "postalCodes": t.array(
                t.proxy(renames["RegionPostalCodeAreaPostalCodeRangeIn"])
            ),
        }
    ).named(renames["RegionPostalCodeAreaIn"])
    types["RegionPostalCodeAreaOut"] = t.struct(
        {
            "regionCode": t.string(),
            "postalCodes": t.array(
                t.proxy(renames["RegionPostalCodeAreaPostalCodeRangeOut"])
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegionPostalCodeAreaOut"])
    types["ReturnPolicySeasonalOverrideIn"] = t.struct(
        {
            "policy": t.proxy(renames["ReturnPolicyPolicyIn"]),
            "startDate": t.string(),
            "endDate": t.string(),
            "name": t.string(),
        }
    ).named(renames["ReturnPolicySeasonalOverrideIn"])
    types["ReturnPolicySeasonalOverrideOut"] = t.struct(
        {
            "policy": t.proxy(renames["ReturnPolicyPolicyOut"]),
            "startDate": t.string(),
            "endDate": t.string(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReturnPolicySeasonalOverrideOut"])
    types["TestOrderDeliveryDetailsIn"] = t.struct(
        {
            "isScheduledDelivery": t.boolean().optional(),
            "address": t.proxy(renames["TestOrderAddressIn"]).optional(),
            "phoneNumber": t.string().optional(),
        }
    ).named(renames["TestOrderDeliveryDetailsIn"])
    types["TestOrderDeliveryDetailsOut"] = t.struct(
        {
            "isScheduledDelivery": t.boolean().optional(),
            "address": t.proxy(renames["TestOrderAddressOut"]).optional(),
            "phoneNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestOrderDeliveryDetailsOut"])
    types["DistanceIn"] = t.struct(
        {"unit": t.string().optional(), "value": t.string().optional()}
    ).named(renames["DistanceIn"])
    types["DistanceOut"] = t.struct(
        {
            "unit": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DistanceOut"])
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
    types["DatafeedFetchScheduleIn"] = t.struct(
        {
            "weekday": t.string().optional(),
            "hour": t.integer().optional(),
            "password": t.string().optional(),
            "username": t.string().optional(),
            "timeZone": t.string().optional(),
            "minuteOfHour": t.integer().optional(),
            "fetchUrl": t.string().optional(),
            "dayOfMonth": t.integer().optional(),
            "paused": t.boolean().optional(),
        }
    ).named(renames["DatafeedFetchScheduleIn"])
    types["DatafeedFetchScheduleOut"] = t.struct(
        {
            "weekday": t.string().optional(),
            "hour": t.integer().optional(),
            "password": t.string().optional(),
            "username": t.string().optional(),
            "timeZone": t.string().optional(),
            "minuteOfHour": t.integer().optional(),
            "fetchUrl": t.string().optional(),
            "dayOfMonth": t.integer().optional(),
            "paused": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatafeedFetchScheduleOut"])
    types["OrderTrackingSignalShipmentLineItemMappingIn"] = t.struct(
        {
            "lineItemId": t.string(),
            "quantity": t.string().optional(),
            "shipmentId": t.string(),
        }
    ).named(renames["OrderTrackingSignalShipmentLineItemMappingIn"])
    types["OrderTrackingSignalShipmentLineItemMappingOut"] = t.struct(
        {
            "lineItemId": t.string(),
            "quantity": t.string().optional(),
            "shipmentId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderTrackingSignalShipmentLineItemMappingOut"])
    types["RegionGeoTargetAreaIn"] = t.struct(
        {"geotargetCriteriaIds": t.array(t.string())}
    ).named(renames["RegionGeoTargetAreaIn"])
    types["RegionGeoTargetAreaOut"] = t.struct(
        {
            "geotargetCriteriaIds": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegionGeoTargetAreaOut"])
    types["PromotionIn"] = t.struct(
        {
            "couponValueType": t.string(),
            "limitValue": t.proxy(renames["PriceAmountIn"]).optional(),
            "promotionDisplayDates": t.string().optional(),
            "moneyOffAmount": t.proxy(renames["PriceAmountIn"]).optional(),
            "freeGiftItemId": t.string().optional(),
            "freeGiftValue": t.proxy(renames["PriceAmountIn"]).optional(),
            "productType": t.array(t.string()).optional(),
            "promotionEffectiveTimePeriod": t.proxy(renames["TimePeriodIn"]),
            "productApplicability": t.string(),
            "redemptionChannel": t.array(t.string()),
            "itemGroupId": t.array(t.string()).optional(),
            "percentOff": t.integer().optional(),
            "itemGroupIdExclusion": t.array(t.string()).optional(),
            "limitQuantity": t.integer().optional(),
            "storeApplicability": t.string().optional(),
            "promotionEffectiveDates": t.string().optional(),
            "minimumPurchaseQuantity": t.integer().optional(),
            "contentLanguage": t.string(),
            "productTypeExclusion": t.array(t.string()).optional(),
            "shippingServiceNames": t.array(t.string()).optional(),
            "genericRedemptionCode": t.string().optional(),
            "brand": t.array(t.string()).optional(),
            "brandExclusion": t.array(t.string()).optional(),
            "freeGiftDescription": t.string().optional(),
            "itemId": t.array(t.string()).optional(),
            "longTitle": t.string(),
            "promotionId": t.string(),
            "minimumPurchaseAmount": t.proxy(renames["PriceAmountIn"]).optional(),
            "itemIdExclusion": t.array(t.string()).optional(),
            "getThisQuantityDiscounted": t.integer().optional(),
            "promotionUrl": t.string().optional(),
            "offerType": t.string(),
            "promotionDestinationIds": t.array(t.string()).optional(),
            "targetCountry": t.string(),
            "moneyBudget": t.proxy(renames["PriceAmountIn"]).optional(),
            "storeCodeExclusion": t.array(t.string()).optional(),
            "orderLimit": t.integer().optional(),
            "promotionDisplayTimePeriod": t.proxy(renames["TimePeriodIn"]).optional(),
            "storeCode": t.array(t.string()).optional(),
        }
    ).named(renames["PromotionIn"])
    types["PromotionOut"] = t.struct(
        {
            "couponValueType": t.string(),
            "limitValue": t.proxy(renames["PriceAmountOut"]).optional(),
            "promotionDisplayDates": t.string().optional(),
            "moneyOffAmount": t.proxy(renames["PriceAmountOut"]).optional(),
            "freeGiftItemId": t.string().optional(),
            "freeGiftValue": t.proxy(renames["PriceAmountOut"]).optional(),
            "productType": t.array(t.string()).optional(),
            "id": t.string(),
            "promotionEffectiveTimePeriod": t.proxy(renames["TimePeriodOut"]),
            "productApplicability": t.string(),
            "redemptionChannel": t.array(t.string()),
            "itemGroupId": t.array(t.string()).optional(),
            "promotionStatus": t.proxy(
                renames["PromotionPromotionStatusOut"]
            ).optional(),
            "percentOff": t.integer().optional(),
            "itemGroupIdExclusion": t.array(t.string()).optional(),
            "limitQuantity": t.integer().optional(),
            "storeApplicability": t.string().optional(),
            "promotionEffectiveDates": t.string().optional(),
            "minimumPurchaseQuantity": t.integer().optional(),
            "contentLanguage": t.string(),
            "productTypeExclusion": t.array(t.string()).optional(),
            "shippingServiceNames": t.array(t.string()).optional(),
            "genericRedemptionCode": t.string().optional(),
            "brand": t.array(t.string()).optional(),
            "brandExclusion": t.array(t.string()).optional(),
            "freeGiftDescription": t.string().optional(),
            "itemId": t.array(t.string()).optional(),
            "longTitle": t.string(),
            "promotionId": t.string(),
            "minimumPurchaseAmount": t.proxy(renames["PriceAmountOut"]).optional(),
            "itemIdExclusion": t.array(t.string()).optional(),
            "getThisQuantityDiscounted": t.integer().optional(),
            "promotionUrl": t.string().optional(),
            "offerType": t.string(),
            "promotionDestinationIds": t.array(t.string()).optional(),
            "targetCountry": t.string(),
            "moneyBudget": t.proxy(renames["PriceAmountOut"]).optional(),
            "storeCodeExclusion": t.array(t.string()).optional(),
            "orderLimit": t.integer().optional(),
            "promotionDisplayTimePeriod": t.proxy(renames["TimePeriodOut"]).optional(),
            "storeCode": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PromotionOut"])
    types["AccounttaxCustomBatchRequestEntryIn"] = t.struct(
        {
            "batchId": t.integer().optional(),
            "method": t.string().optional(),
            "accountId": t.string().optional(),
            "accountTax": t.proxy(renames["AccountTaxIn"]).optional(),
            "merchantId": t.string().optional(),
        }
    ).named(renames["AccounttaxCustomBatchRequestEntryIn"])
    types["AccounttaxCustomBatchRequestEntryOut"] = t.struct(
        {
            "batchId": t.integer().optional(),
            "method": t.string().optional(),
            "accountId": t.string().optional(),
            "accountTax": t.proxy(renames["AccountTaxOut"]).optional(),
            "merchantId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccounttaxCustomBatchRequestEntryOut"])
    types["PriceInsightsIn"] = t.struct(
        {
            "predictedGrossProfitChangeFraction": t.number().optional(),
            "predictedImpressionsChangeFraction": t.number().optional(),
            "suggestedPriceMicros": t.string().optional(),
            "predictedClicksChangeFraction": t.number().optional(),
            "predictedMonthlyGrossProfitChangeCurrencyCode": t.string().optional(),
            "predictedConversionsChangeFraction": t.number().optional(),
            "suggestedPriceCurrencyCode": t.string().optional(),
            "predictedMonthlyGrossProfitChangeMicros": t.string().optional(),
        }
    ).named(renames["PriceInsightsIn"])
    types["PriceInsightsOut"] = t.struct(
        {
            "predictedGrossProfitChangeFraction": t.number().optional(),
            "predictedImpressionsChangeFraction": t.number().optional(),
            "suggestedPriceMicros": t.string().optional(),
            "predictedClicksChangeFraction": t.number().optional(),
            "predictedMonthlyGrossProfitChangeCurrencyCode": t.string().optional(),
            "predictedConversionsChangeFraction": t.number().optional(),
            "suggestedPriceCurrencyCode": t.string().optional(),
            "predictedMonthlyGrossProfitChangeMicros": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PriceInsightsOut"])
    types["LoyaltyPointsIn"] = t.struct(
        {
            "ratio": t.number().optional(),
            "pointsValue": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["LoyaltyPointsIn"])
    types["LoyaltyPointsOut"] = t.struct(
        {
            "ratio": t.number().optional(),
            "pointsValue": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LoyaltyPointsOut"])
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
    types["ReturnShippingLabelIn"] = t.struct(
        {
            "trackingId": t.string().optional(),
            "carrier": t.string().optional(),
            "labelUri": t.string().optional(),
        }
    ).named(renames["ReturnShippingLabelIn"])
    types["ReturnShippingLabelOut"] = t.struct(
        {
            "trackingId": t.string().optional(),
            "carrier": t.string().optional(),
            "labelUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReturnShippingLabelOut"])
    types["ProductWeightIn"] = t.struct(
        {"unit": t.string(), "value": t.number()}
    ).named(renames["ProductWeightIn"])
    types["ProductWeightOut"] = t.struct(
        {
            "unit": t.string(),
            "value": t.number(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductWeightOut"])
    types["OrdersUpdateShipmentResponseIn"] = t.struct(
        {"kind": t.string().optional(), "executionStatus": t.string().optional()}
    ).named(renames["OrdersUpdateShipmentResponseIn"])
    types["OrdersUpdateShipmentResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "executionStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersUpdateShipmentResponseOut"])
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
    types["RegionalinventoryCustomBatchRequestEntryIn"] = t.struct(
        {
            "batchId": t.integer().optional(),
            "method": t.string().optional(),
            "regionalInventory": t.proxy(renames["RegionalInventoryIn"]).optional(),
            "merchantId": t.string().optional(),
            "productId": t.string().optional(),
        }
    ).named(renames["RegionalinventoryCustomBatchRequestEntryIn"])
    types["RegionalinventoryCustomBatchRequestEntryOut"] = t.struct(
        {
            "batchId": t.integer().optional(),
            "method": t.string().optional(),
            "regionalInventory": t.proxy(renames["RegionalInventoryOut"]).optional(),
            "merchantId": t.string().optional(),
            "productId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegionalinventoryCustomBatchRequestEntryOut"])
    types["ProductsCustomBatchRequestEntryIn"] = t.struct(
        {
            "batchId": t.integer().optional(),
            "productId": t.string().optional(),
            "method": t.string().optional(),
            "product": t.proxy(renames["ProductIn"]).optional(),
            "merchantId": t.string().optional(),
            "feedId": t.string().optional(),
            "updateMask": t.string().optional(),
        }
    ).named(renames["ProductsCustomBatchRequestEntryIn"])
    types["ProductsCustomBatchRequestEntryOut"] = t.struct(
        {
            "batchId": t.integer().optional(),
            "productId": t.string().optional(),
            "method": t.string().optional(),
            "product": t.proxy(renames["ProductOut"]).optional(),
            "merchantId": t.string().optional(),
            "feedId": t.string().optional(),
            "updateMask": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductsCustomBatchRequestEntryOut"])
    types["WarehouseBasedDeliveryTimeIn"] = t.struct(
        {
            "originStreetAddress": t.string().optional(),
            "originCity": t.string().optional(),
            "originAdministrativeArea": t.string().optional(),
            "originCountry": t.string().optional(),
            "carrier": t.string(),
            "originPostalCode": t.string().optional(),
            "carrierService": t.string(),
            "warehouseName": t.string().optional(),
        }
    ).named(renames["WarehouseBasedDeliveryTimeIn"])
    types["WarehouseBasedDeliveryTimeOut"] = t.struct(
        {
            "originStreetAddress": t.string().optional(),
            "originCity": t.string().optional(),
            "originAdministrativeArea": t.string().optional(),
            "originCountry": t.string().optional(),
            "carrier": t.string(),
            "originPostalCode": t.string().optional(),
            "carrierService": t.string(),
            "warehouseName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WarehouseBasedDeliveryTimeOut"])
    types["AccountsAuthInfoResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "accountIdentifiers": t.array(
                t.proxy(renames["AccountIdentifierIn"])
            ).optional(),
        }
    ).named(renames["AccountsAuthInfoResponseIn"])
    types["AccountsAuthInfoResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "accountIdentifiers": t.array(
                t.proxy(renames["AccountIdentifierOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountsAuthInfoResponseOut"])
    types["AccountAutomaticImprovementsIn"] = t.struct(
        {
            "itemUpdates": t.proxy(renames["AccountItemUpdatesIn"]).optional(),
            "imageImprovements": t.proxy(
                renames["AccountImageImprovementsIn"]
            ).optional(),
            "shippingImprovements": t.proxy(
                renames["AccountShippingImprovementsIn"]
            ).optional(),
        }
    ).named(renames["AccountAutomaticImprovementsIn"])
    types["AccountAutomaticImprovementsOut"] = t.struct(
        {
            "itemUpdates": t.proxy(renames["AccountItemUpdatesOut"]).optional(),
            "imageImprovements": t.proxy(
                renames["AccountImageImprovementsOut"]
            ).optional(),
            "shippingImprovements": t.proxy(
                renames["AccountShippingImprovementsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountAutomaticImprovementsOut"])
    types["ShippingsettingsCustomBatchResponseEntryIn"] = t.struct(
        {
            "shippingSettings": t.proxy(renames["ShippingSettingsIn"]).optional(),
            "kind": t.string().optional(),
            "batchId": t.integer().optional(),
            "errors": t.proxy(renames["ErrorsIn"]).optional(),
        }
    ).named(renames["ShippingsettingsCustomBatchResponseEntryIn"])
    types["ShippingsettingsCustomBatchResponseEntryOut"] = t.struct(
        {
            "shippingSettings": t.proxy(renames["ShippingSettingsOut"]).optional(),
            "kind": t.string().optional(),
            "batchId": t.integer().optional(),
            "errors": t.proxy(renames["ErrorsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShippingsettingsCustomBatchResponseEntryOut"])
    types["HeadersIn"] = t.struct(
        {
            "prices": t.array(t.proxy(renames["PriceIn"])).optional(),
            "postalCodeGroupNames": t.array(t.string()).optional(),
            "locations": t.array(t.proxy(renames["LocationIdSetIn"])).optional(),
            "numberOfItems": t.array(t.string()).optional(),
            "weights": t.array(t.proxy(renames["WeightIn"])).optional(),
        }
    ).named(renames["HeadersIn"])
    types["HeadersOut"] = t.struct(
        {
            "prices": t.array(t.proxy(renames["PriceOut"])).optional(),
            "postalCodeGroupNames": t.array(t.string()).optional(),
            "locations": t.array(t.proxy(renames["LocationIdSetOut"])).optional(),
            "numberOfItems": t.array(t.string()).optional(),
            "weights": t.array(t.proxy(renames["WeightOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HeadersOut"])
    types["RequestReviewBuyOnGoogleProgramRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["RequestReviewBuyOnGoogleProgramRequestIn"])
    types["RequestReviewBuyOnGoogleProgramRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RequestReviewBuyOnGoogleProgramRequestOut"])
    types["AccountIn"] = t.struct(
        {
            "conversionSettings": t.proxy(
                renames["AccountConversionSettingsIn"]
            ).optional(),
            "labelIds": t.array(t.string()).optional(),
            "id": t.string(),
            "kind": t.string().optional(),
            "cssId": t.string().optional(),
            "youtubeChannelLinks": t.array(
                t.proxy(renames["AccountYouTubeChannelLinkIn"])
            ).optional(),
            "googleMyBusinessLink": t.proxy(
                renames["AccountGoogleMyBusinessLinkIn"]
            ).optional(),
            "sellerId": t.string().optional(),
            "adultContent": t.boolean().optional(),
            "adsLinks": t.array(t.proxy(renames["AccountAdsLinkIn"])).optional(),
            "users": t.array(t.proxy(renames["AccountUserIn"])).optional(),
            "name": t.string(),
            "businessInformation": t.proxy(
                renames["AccountBusinessInformationIn"]
            ).optional(),
            "automaticImprovements": t.proxy(
                renames["AccountAutomaticImprovementsIn"]
            ).optional(),
            "websiteUrl": t.string().optional(),
            "automaticLabelIds": t.array(t.string()).optional(),
        }
    ).named(renames["AccountIn"])
    types["AccountOut"] = t.struct(
        {
            "conversionSettings": t.proxy(
                renames["AccountConversionSettingsOut"]
            ).optional(),
            "labelIds": t.array(t.string()).optional(),
            "id": t.string(),
            "kind": t.string().optional(),
            "cssId": t.string().optional(),
            "youtubeChannelLinks": t.array(
                t.proxy(renames["AccountYouTubeChannelLinkOut"])
            ).optional(),
            "googleMyBusinessLink": t.proxy(
                renames["AccountGoogleMyBusinessLinkOut"]
            ).optional(),
            "accountManagement": t.string().optional(),
            "sellerId": t.string().optional(),
            "adultContent": t.boolean().optional(),
            "adsLinks": t.array(t.proxy(renames["AccountAdsLinkOut"])).optional(),
            "users": t.array(t.proxy(renames["AccountUserOut"])).optional(),
            "name": t.string(),
            "businessInformation": t.proxy(
                renames["AccountBusinessInformationOut"]
            ).optional(),
            "automaticImprovements": t.proxy(
                renames["AccountAutomaticImprovementsOut"]
            ).optional(),
            "websiteUrl": t.string().optional(),
            "automaticLabelIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountOut"])
    types["ProductViewItemIssueItemIssueTypeIn"] = t.struct(
        {"canonicalAttribute": t.string().optional(), "code": t.string().optional()}
    ).named(renames["ProductViewItemIssueItemIssueTypeIn"])
    types["ProductViewItemIssueItemIssueTypeOut"] = t.struct(
        {
            "canonicalAttribute": t.string().optional(),
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductViewItemIssueItemIssueTypeOut"])
    types["OrdersUpdateLineItemShippingDetailsRequestIn"] = t.struct(
        {
            "lineItemId": t.string().optional(),
            "shipByDate": t.string().optional(),
            "operationId": t.string().optional(),
            "deliverByDate": t.string().optional(),
            "productId": t.string().optional(),
        }
    ).named(renames["OrdersUpdateLineItemShippingDetailsRequestIn"])
    types["OrdersUpdateLineItemShippingDetailsRequestOut"] = t.struct(
        {
            "lineItemId": t.string().optional(),
            "shipByDate": t.string().optional(),
            "operationId": t.string().optional(),
            "deliverByDate": t.string().optional(),
            "productId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersUpdateLineItemShippingDetailsRequestOut"])
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
    types["RegionIn"] = t.struct(
        {
            "geotargetArea": t.proxy(renames["RegionGeoTargetAreaIn"]).optional(),
            "displayName": t.string().optional(),
            "postalCodeArea": t.proxy(renames["RegionPostalCodeAreaIn"]).optional(),
        }
    ).named(renames["RegionIn"])
    types["RegionOut"] = t.struct(
        {
            "shippingEligible": t.boolean().optional(),
            "geotargetArea": t.proxy(renames["RegionGeoTargetAreaOut"]).optional(),
            "merchantId": t.string().optional(),
            "displayName": t.string().optional(),
            "postalCodeArea": t.proxy(renames["RegionPostalCodeAreaOut"]).optional(),
            "regionalInventoryEligible": t.boolean().optional(),
            "regionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegionOut"])
    types["BrandIn"] = t.struct({"name": t.string().optional()}).named(
        renames["BrandIn"]
    )
    types["BrandOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BrandOut"])
    types["AccountsUpdateLabelsResponseIn"] = t.struct(
        {"kind": t.string().optional()}
    ).named(renames["AccountsUpdateLabelsResponseIn"])
    types["AccountsUpdateLabelsResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountsUpdateLabelsResponseOut"])
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
    types["AccountReturnCarrierIn"] = t.struct(
        {
            "carrierCode": t.string().optional(),
            "carrierAccountNumber": t.string().optional(),
            "carrierAccountName": t.string().optional(),
        }
    ).named(renames["AccountReturnCarrierIn"])
    types["AccountReturnCarrierOut"] = t.struct(
        {
            "carrierCode": t.string().optional(),
            "carrierAccountId": t.string().optional(),
            "carrierAccountNumber": t.string().optional(),
            "carrierAccountName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountReturnCarrierOut"])
    types["ListCssesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "csses": t.array(t.proxy(renames["CssIn"])).optional(),
        }
    ).named(renames["ListCssesResponseIn"])
    types["ListCssesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "csses": t.array(t.proxy(renames["CssOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCssesResponseOut"])
    types["AccountUserIn"] = t.struct(
        {
            "reportingManager": t.boolean().optional(),
            "emailAddress": t.string().optional(),
            "admin": t.boolean().optional(),
            "paymentsManager": t.boolean().optional(),
            "paymentsAnalyst": t.boolean().optional(),
            "orderManager": t.boolean().optional(),
        }
    ).named(renames["AccountUserIn"])
    types["AccountUserOut"] = t.struct(
        {
            "reportingManager": t.boolean().optional(),
            "emailAddress": t.string().optional(),
            "admin": t.boolean().optional(),
            "paymentsManager": t.boolean().optional(),
            "paymentsAnalyst": t.boolean().optional(),
            "orderManager": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountUserOut"])
    types["ProductShippingDimensionIn"] = t.struct(
        {"unit": t.string().optional(), "value": t.number().optional()}
    ).named(renames["ProductShippingDimensionIn"])
    types["ProductShippingDimensionOut"] = t.struct(
        {
            "unit": t.string().optional(),
            "value": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductShippingDimensionOut"])
    types["PriceAmountIn"] = t.struct(
        {"value": t.string().optional(), "currency": t.string().optional()}
    ).named(renames["PriceAmountIn"])
    types["PriceAmountOut"] = t.struct(
        {
            "value": t.string().optional(),
            "currency": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PriceAmountOut"])
    types["ShippingsettingsCustomBatchRequestEntryIn"] = t.struct(
        {
            "shippingSettings": t.proxy(renames["ShippingSettingsIn"]).optional(),
            "accountId": t.string().optional(),
            "merchantId": t.string().optional(),
            "method": t.string().optional(),
            "batchId": t.integer().optional(),
        }
    ).named(renames["ShippingsettingsCustomBatchRequestEntryIn"])
    types["ShippingsettingsCustomBatchRequestEntryOut"] = t.struct(
        {
            "shippingSettings": t.proxy(renames["ShippingSettingsOut"]).optional(),
            "accountId": t.string().optional(),
            "merchantId": t.string().optional(),
            "method": t.string().optional(),
            "batchId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShippingsettingsCustomBatchRequestEntryOut"])
    types["OrdersReturnRefundLineItemRequestIn"] = t.struct(
        {
            "taxAmount": t.proxy(renames["PriceIn"]).optional(),
            "quantity": t.integer().optional(),
            "operationId": t.string().optional(),
            "lineItemId": t.string().optional(),
            "reason": t.string().optional(),
            "productId": t.string().optional(),
            "priceAmount": t.proxy(renames["PriceIn"]).optional(),
            "reasonText": t.string().optional(),
        }
    ).named(renames["OrdersReturnRefundLineItemRequestIn"])
    types["OrdersReturnRefundLineItemRequestOut"] = t.struct(
        {
            "taxAmount": t.proxy(renames["PriceOut"]).optional(),
            "quantity": t.integer().optional(),
            "operationId": t.string().optional(),
            "lineItemId": t.string().optional(),
            "reason": t.string().optional(),
            "productId": t.string().optional(),
            "priceAmount": t.proxy(renames["PriceOut"]).optional(),
            "reasonText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersReturnRefundLineItemRequestOut"])
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
    types["PickupServicesPickupServiceIn"] = t.struct(
        {
            "serviceName": t.string().optional(),
            "country": t.string().optional(),
            "carrierName": t.string().optional(),
        }
    ).named(renames["PickupServicesPickupServiceIn"])
    types["PickupServicesPickupServiceOut"] = t.struct(
        {
            "serviceName": t.string().optional(),
            "country": t.string().optional(),
            "carrierName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PickupServicesPickupServiceOut"])
    types["ProductViewItemIssueItemIssueSeverityIn"] = t.struct(
        {
            "aggregatedSeverity": t.string().optional(),
            "severityPerDestination": t.array(
                t.proxy(renames["ProductViewItemIssueIssueSeverityPerDestinationIn"])
            ).optional(),
        }
    ).named(renames["ProductViewItemIssueItemIssueSeverityIn"])
    types["ProductViewItemIssueItemIssueSeverityOut"] = t.struct(
        {
            "aggregatedSeverity": t.string().optional(),
            "severityPerDestination": t.array(
                t.proxy(renames["ProductViewItemIssueIssueSeverityPerDestinationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductViewItemIssueItemIssueSeverityOut"])
    types["PosCustomBatchResponseEntryIn"] = t.struct(
        {
            "batchId": t.integer().optional(),
            "kind": t.string().optional(),
            "store": t.proxy(renames["PosStoreIn"]).optional(),
            "inventory": t.proxy(renames["PosInventoryIn"]).optional(),
            "sale": t.proxy(renames["PosSaleIn"]).optional(),
            "errors": t.proxy(renames["ErrorsIn"]).optional(),
        }
    ).named(renames["PosCustomBatchResponseEntryIn"])
    types["PosCustomBatchResponseEntryOut"] = t.struct(
        {
            "batchId": t.integer().optional(),
            "kind": t.string().optional(),
            "store": t.proxy(renames["PosStoreOut"]).optional(),
            "inventory": t.proxy(renames["PosInventoryOut"]).optional(),
            "sale": t.proxy(renames["PosSaleOut"]).optional(),
            "errors": t.proxy(renames["ErrorsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PosCustomBatchResponseEntryOut"])
    types["PosInventoryResponseIn"] = t.struct(
        {
            "contentLanguage": t.string(),
            "timestamp": t.string(),
            "gtin": t.string().optional(),
            "kind": t.string().optional(),
            "price": t.proxy(renames["PriceIn"]),
            "quantity": t.string(),
            "itemId": t.string(),
            "targetCountry": t.string(),
            "storeCode": t.string(),
        }
    ).named(renames["PosInventoryResponseIn"])
    types["PosInventoryResponseOut"] = t.struct(
        {
            "contentLanguage": t.string(),
            "timestamp": t.string(),
            "gtin": t.string().optional(),
            "kind": t.string().optional(),
            "price": t.proxy(renames["PriceOut"]),
            "quantity": t.string(),
            "itemId": t.string(),
            "targetCountry": t.string(),
            "storeCode": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PosInventoryResponseOut"])
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
    types["PriceIn"] = t.struct(
        {"value": t.string().optional(), "currency": t.string().optional()}
    ).named(renames["PriceIn"])
    types["PriceOut"] = t.struct(
        {
            "value": t.string().optional(),
            "currency": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PriceOut"])
    types["LocalinventoryCustomBatchRequestEntryIn"] = t.struct(
        {
            "productId": t.string().optional(),
            "batchId": t.integer().optional(),
            "merchantId": t.string().optional(),
            "localInventory": t.proxy(renames["LocalInventoryIn"]).optional(),
            "method": t.string().optional(),
        }
    ).named(renames["LocalinventoryCustomBatchRequestEntryIn"])
    types["LocalinventoryCustomBatchRequestEntryOut"] = t.struct(
        {
            "productId": t.string().optional(),
            "batchId": t.integer().optional(),
            "merchantId": t.string().optional(),
            "localInventory": t.proxy(renames["LocalInventoryOut"]).optional(),
            "method": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocalinventoryCustomBatchRequestEntryOut"])
    types["CustomerIn"] = t.struct(
        {
            "emailAddress": t.string().optional(),
            "loyaltyData": t.proxy(renames["CustomerLoyaltyDataIn"]).optional(),
        }
    ).named(renames["CustomerIn"])
    types["CustomerOut"] = t.struct(
        {
            "emailAddress": t.string().optional(),
            "loyaltyData": t.proxy(renames["CustomerLoyaltyDataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomerOut"])
    types["OrderLineItemProductIn"] = t.struct(
        {
            "gtin": t.string().optional(),
            "brand": t.string().optional(),
            "contentLanguage": t.string().optional(),
            "id": t.string().optional(),
            "offerId": t.string().optional(),
            "variantAttributes": t.array(
                t.proxy(renames["OrderLineItemProductVariantAttributeIn"])
            ).optional(),
            "itemGroupId": t.string().optional(),
            "price": t.proxy(renames["PriceIn"]).optional(),
            "mpn": t.string().optional(),
            "condition": t.string().optional(),
            "title": t.string().optional(),
            "targetCountry": t.string().optional(),
            "shownImage": t.string().optional(),
            "imageLink": t.string().optional(),
            "fees": t.array(t.proxy(renames["OrderLineItemProductFeeIn"])).optional(),
        }
    ).named(renames["OrderLineItemProductIn"])
    types["OrderLineItemProductOut"] = t.struct(
        {
            "gtin": t.string().optional(),
            "brand": t.string().optional(),
            "contentLanguage": t.string().optional(),
            "id": t.string().optional(),
            "offerId": t.string().optional(),
            "variantAttributes": t.array(
                t.proxy(renames["OrderLineItemProductVariantAttributeOut"])
            ).optional(),
            "itemGroupId": t.string().optional(),
            "price": t.proxy(renames["PriceOut"]).optional(),
            "mpn": t.string().optional(),
            "condition": t.string().optional(),
            "title": t.string().optional(),
            "targetCountry": t.string().optional(),
            "shownImage": t.string().optional(),
            "imageLink": t.string().optional(),
            "fees": t.array(t.proxy(renames["OrderLineItemProductFeeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderLineItemProductOut"])
    types["DatafeedFormatIn"] = t.struct(
        {
            "quotingMode": t.string().optional(),
            "columnDelimiter": t.string().optional(),
            "fileEncoding": t.string().optional(),
        }
    ).named(renames["DatafeedFormatIn"])
    types["DatafeedFormatOut"] = t.struct(
        {
            "quotingMode": t.string().optional(),
            "columnDelimiter": t.string().optional(),
            "fileEncoding": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatafeedFormatOut"])
    types["OrdersCancelRequestIn"] = t.struct(
        {
            "reason": t.string().optional(),
            "operationId": t.string().optional(),
            "reasonText": t.string().optional(),
        }
    ).named(renames["OrdersCancelRequestIn"])
    types["OrdersCancelRequestOut"] = t.struct(
        {
            "reason": t.string().optional(),
            "operationId": t.string().optional(),
            "reasonText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersCancelRequestOut"])
    types["DatafeedTargetIn"] = t.struct(
        {
            "country": t.string().optional(),
            "targetCountries": t.array(t.string()).optional(),
            "includedDestinations": t.array(t.string()).optional(),
            "feedLabel": t.string().optional(),
            "excludedDestinations": t.array(t.string()).optional(),
            "language": t.string().optional(),
        }
    ).named(renames["DatafeedTargetIn"])
    types["DatafeedTargetOut"] = t.struct(
        {
            "country": t.string().optional(),
            "targetCountries": t.array(t.string()).optional(),
            "includedDestinations": t.array(t.string()).optional(),
            "feedLabel": t.string().optional(),
            "excludedDestinations": t.array(t.string()).optional(),
            "language": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatafeedTargetOut"])
    types["ListRegionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "regions": t.array(t.proxy(renames["RegionIn"])).optional(),
        }
    ).named(renames["ListRegionsResponseIn"])
    types["ListRegionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "regions": t.array(t.proxy(renames["RegionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListRegionsResponseOut"])
    types["ProductShippingIn"] = t.struct(
        {
            "maxTransitTime": t.string().optional(),
            "maxHandlingTime": t.string().optional(),
            "region": t.string().optional(),
            "service": t.string().optional(),
            "country": t.string().optional(),
            "minTransitTime": t.string().optional(),
            "locationGroupName": t.string().optional(),
            "locationId": t.string().optional(),
            "postalCode": t.string().optional(),
            "price": t.proxy(renames["PriceIn"]).optional(),
            "minHandlingTime": t.string().optional(),
        }
    ).named(renames["ProductShippingIn"])
    types["ProductShippingOut"] = t.struct(
        {
            "maxTransitTime": t.string().optional(),
            "maxHandlingTime": t.string().optional(),
            "region": t.string().optional(),
            "service": t.string().optional(),
            "country": t.string().optional(),
            "minTransitTime": t.string().optional(),
            "locationGroupName": t.string().optional(),
            "locationId": t.string().optional(),
            "postalCode": t.string().optional(),
            "price": t.proxy(renames["PriceOut"]).optional(),
            "minHandlingTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductShippingOut"])
    types["OrderLineItemAdjustmentIn"] = t.struct(
        {
            "taxAdjustment": t.proxy(renames["PriceIn"]).optional(),
            "type": t.string().optional(),
            "priceAdjustment": t.proxy(renames["PriceIn"]).optional(),
        }
    ).named(renames["OrderLineItemAdjustmentIn"])
    types["OrderLineItemAdjustmentOut"] = t.struct(
        {
            "taxAdjustment": t.proxy(renames["PriceOut"]).optional(),
            "type": t.string().optional(),
            "priceAdjustment": t.proxy(renames["PriceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderLineItemAdjustmentOut"])
    types["ShoppingAdsProgramStatusIn"] = t.struct(
        {
            "globalState": t.string().optional(),
            "regionStatuses": t.array(
                t.proxy(renames["ShoppingAdsProgramStatusRegionStatusIn"])
            ).optional(),
        }
    ).named(renames["ShoppingAdsProgramStatusIn"])
    types["ShoppingAdsProgramStatusOut"] = t.struct(
        {
            "globalState": t.string().optional(),
            "regionStatuses": t.array(
                t.proxy(renames["ShoppingAdsProgramStatusRegionStatusOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShoppingAdsProgramStatusOut"])
    types["BusinessDayConfigIn"] = t.struct(
        {"businessDays": t.array(t.string()).optional()}
    ).named(renames["BusinessDayConfigIn"])
    types["BusinessDayConfigOut"] = t.struct(
        {
            "businessDays": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BusinessDayConfigOut"])
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
    types["OrderLineItemShippingDetailsIn"] = t.struct(
        {
            "pickupPromiseInMinutes": t.integer().optional(),
            "deliverByDate": t.string(),
            "method": t.proxy(renames["OrderLineItemShippingDetailsMethodIn"]),
            "type": t.string().optional(),
            "shipByDate": t.string(),
        }
    ).named(renames["OrderLineItemShippingDetailsIn"])
    types["OrderLineItemShippingDetailsOut"] = t.struct(
        {
            "pickupPromiseInMinutes": t.integer().optional(),
            "deliverByDate": t.string(),
            "method": t.proxy(renames["OrderLineItemShippingDetailsMethodOut"]),
            "type": t.string().optional(),
            "shipByDate": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderLineItemShippingDetailsOut"])
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
    types["CustomerReturnReasonIn"] = t.struct(
        {"description": t.string().optional(), "reasonCode": t.string().optional()}
    ).named(renames["CustomerReturnReasonIn"])
    types["CustomerReturnReasonOut"] = t.struct(
        {
            "description": t.string().optional(),
            "reasonCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomerReturnReasonOut"])
    types["DatafeedstatusesCustomBatchRequestEntryIn"] = t.struct(
        {
            "feedLabel": t.string().optional(),
            "batchId": t.integer().optional(),
            "country": t.string().optional(),
            "datafeedId": t.string().optional(),
            "language": t.string().optional(),
            "method": t.string().optional(),
            "merchantId": t.string().optional(),
        }
    ).named(renames["DatafeedstatusesCustomBatchRequestEntryIn"])
    types["DatafeedstatusesCustomBatchRequestEntryOut"] = t.struct(
        {
            "feedLabel": t.string().optional(),
            "batchId": t.integer().optional(),
            "country": t.string().optional(),
            "datafeedId": t.string().optional(),
            "language": t.string().optional(),
            "method": t.string().optional(),
            "merchantId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatafeedstatusesCustomBatchRequestEntryOut"])
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
    types["MerchantCenterDestinationIn"] = t.struct(
        {
            "displayName": t.string(),
            "attributionSettings": t.proxy(renames["AttributionSettingsIn"]),
            "currencyCode": t.string(),
        }
    ).named(renames["MerchantCenterDestinationIn"])
    types["MerchantCenterDestinationOut"] = t.struct(
        {
            "displayName": t.string(),
            "attributionSettings": t.proxy(renames["AttributionSettingsOut"]),
            "currencyCode": t.string(),
            "destinationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MerchantCenterDestinationOut"])
    types["PromotionPromotionStatusIn"] = t.struct(
        {
            "destinationStatuses": t.array(
                t.proxy(renames["PromotionPromotionStatusDestinationStatusIn"])
            ).optional(),
            "lastUpdateDate": t.string().optional(),
            "promotionIssue": t.array(
                t.proxy(renames["PromotionPromotionStatusPromotionIssueIn"])
            ).optional(),
            "creationDate": t.string().optional(),
        }
    ).named(renames["PromotionPromotionStatusIn"])
    types["PromotionPromotionStatusOut"] = t.struct(
        {
            "destinationStatuses": t.array(
                t.proxy(renames["PromotionPromotionStatusDestinationStatusOut"])
            ).optional(),
            "lastUpdateDate": t.string().optional(),
            "promotionIssue": t.array(
                t.proxy(renames["PromotionPromotionStatusPromotionIssueOut"])
            ).optional(),
            "creationDate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PromotionPromotionStatusOut"])
    types["RepricingRuleReportIn"] = t.struct(
        {
            "buyboxWinningRuleStats": t.proxy(
                renames["RepricingRuleReportBuyboxWinningRuleStatsIn"]
            ).optional(),
            "ruleId": t.string().optional(),
            "inapplicabilityDetails": t.array(
                t.proxy(renames["InapplicabilityDetailsIn"])
            ).optional(),
            "impactedProducts": t.array(t.string()).optional(),
            "totalGmv": t.proxy(renames["PriceAmountIn"]).optional(),
            "type": t.string().optional(),
            "orderItemCount": t.integer().optional(),
            "date": t.proxy(renames["DateIn"]).optional(),
            "inapplicableProducts": t.array(t.string()).optional(),
        }
    ).named(renames["RepricingRuleReportIn"])
    types["RepricingRuleReportOut"] = t.struct(
        {
            "buyboxWinningRuleStats": t.proxy(
                renames["RepricingRuleReportBuyboxWinningRuleStatsOut"]
            ).optional(),
            "ruleId": t.string().optional(),
            "inapplicabilityDetails": t.array(
                t.proxy(renames["InapplicabilityDetailsOut"])
            ).optional(),
            "impactedProducts": t.array(t.string()).optional(),
            "totalGmv": t.proxy(renames["PriceAmountOut"]).optional(),
            "type": t.string().optional(),
            "orderItemCount": t.integer().optional(),
            "date": t.proxy(renames["DateOut"]).optional(),
            "inapplicableProducts": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepricingRuleReportOut"])
    types["CarrierRateIn"] = t.struct(
        {
            "carrierName": t.string().optional(),
            "percentageAdjustment": t.string().optional(),
            "originPostalCode": t.string().optional(),
            "name": t.string().optional(),
            "carrierService": t.string().optional(),
            "flatAdjustment": t.proxy(renames["PriceIn"]).optional(),
        }
    ).named(renames["CarrierRateIn"])
    types["CarrierRateOut"] = t.struct(
        {
            "carrierName": t.string().optional(),
            "percentageAdjustment": t.string().optional(),
            "originPostalCode": t.string().optional(),
            "name": t.string().optional(),
            "carrierService": t.string().optional(),
            "flatAdjustment": t.proxy(renames["PriceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CarrierRateOut"])
    types["AmountIn"] = t.struct(
        {
            "priceAmount": t.proxy(renames["PriceIn"]).optional(),
            "taxAmount": t.proxy(renames["PriceIn"]).optional(),
        }
    ).named(renames["AmountIn"])
    types["AmountOut"] = t.struct(
        {
            "priceAmount": t.proxy(renames["PriceOut"]).optional(),
            "taxAmount": t.proxy(renames["PriceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AmountOut"])
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
    types["LiaInventorySettingsIn"] = t.struct(
        {
            "inventoryVerificationContactStatus": t.string().optional(),
            "inventoryVerificationContactName": t.string().optional(),
            "status": t.string().optional(),
            "inventoryVerificationContactEmail": t.string().optional(),
        }
    ).named(renames["LiaInventorySettingsIn"])
    types["LiaInventorySettingsOut"] = t.struct(
        {
            "inventoryVerificationContactStatus": t.string().optional(),
            "inventoryVerificationContactName": t.string().optional(),
            "status": t.string().optional(),
            "inventoryVerificationContactEmail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiaInventorySettingsOut"])
    types["AccountsListLinksResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "links": t.array(t.proxy(renames["LinkedAccountIn"])).optional(),
        }
    ).named(renames["AccountsListLinksResponseIn"])
    types["AccountsListLinksResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "links": t.array(t.proxy(renames["LinkedAccountOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountsListLinksResponseOut"])
    types["ListRepricingRulesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "repricingRules": t.array(t.proxy(renames["RepricingRuleIn"])).optional(),
        }
    ).named(renames["ListRepricingRulesResponseIn"])
    types["ListRepricingRulesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "repricingRules": t.array(t.proxy(renames["RepricingRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListRepricingRulesResponseOut"])
    types["ProductStatusDestinationStatusIn"] = t.struct(
        {
            "disapprovedCountries": t.array(t.string()).optional(),
            "approvedCountries": t.array(t.string()).optional(),
            "destination": t.string().optional(),
            "pendingCountries": t.array(t.string()).optional(),
            "status": t.string().optional(),
        }
    ).named(renames["ProductStatusDestinationStatusIn"])
    types["ProductStatusDestinationStatusOut"] = t.struct(
        {
            "disapprovedCountries": t.array(t.string()).optional(),
            "approvedCountries": t.array(t.string()).optional(),
            "destination": t.string().optional(),
            "pendingCountries": t.array(t.string()).optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductStatusDestinationStatusOut"])
    types["TestOrderPickupDetailsIn"] = t.struct(
        {
            "pickupLocationAddress": t.proxy(renames["TestOrderAddressIn"]),
            "locationCode": t.string(),
            "pickupLocationType": t.string().optional(),
            "pickupPersons": t.array(
                t.proxy(renames["TestOrderPickupDetailsPickupPersonIn"])
            ),
        }
    ).named(renames["TestOrderPickupDetailsIn"])
    types["TestOrderPickupDetailsOut"] = t.struct(
        {
            "pickupLocationAddress": t.proxy(renames["TestOrderAddressOut"]),
            "locationCode": t.string(),
            "pickupLocationType": t.string().optional(),
            "pickupPersons": t.array(
                t.proxy(renames["TestOrderPickupDetailsPickupPersonOut"])
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestOrderPickupDetailsOut"])
    types["OrdersRefundOrderRequestIn"] = t.struct(
        {
            "amount": t.proxy(renames["MonetaryAmountIn"]).optional(),
            "fullRefund": t.boolean().optional(),
            "reason": t.string().optional(),
            "operationId": t.string().optional(),
            "reasonText": t.string().optional(),
        }
    ).named(renames["OrdersRefundOrderRequestIn"])
    types["OrdersRefundOrderRequestOut"] = t.struct(
        {
            "amount": t.proxy(renames["MonetaryAmountOut"]).optional(),
            "fullRefund": t.boolean().optional(),
            "reason": t.string().optional(),
            "operationId": t.string().optional(),
            "reasonText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersRefundOrderRequestOut"])
    types["OrdersCancelTestOrderByCustomerRequestIn"] = t.struct(
        {"reason": t.string().optional()}
    ).named(renames["OrdersCancelTestOrderByCustomerRequestIn"])
    types["OrdersCancelTestOrderByCustomerRequestOut"] = t.struct(
        {
            "reason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersCancelTestOrderByCustomerRequestOut"])
    types["SettlementTransactionIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "identifiers": t.proxy(
                renames["SettlementTransactionIdentifiersIn"]
            ).optional(),
            "transaction": t.proxy(
                renames["SettlementTransactionTransactionIn"]
            ).optional(),
            "amount": t.proxy(renames["SettlementTransactionAmountIn"]).optional(),
        }
    ).named(renames["SettlementTransactionIn"])
    types["SettlementTransactionOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "identifiers": t.proxy(
                renames["SettlementTransactionIdentifiersOut"]
            ).optional(),
            "transaction": t.proxy(
                renames["SettlementTransactionTransactionOut"]
            ).optional(),
            "amount": t.proxy(renames["SettlementTransactionAmountOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SettlementTransactionOut"])
    types["RepricingRuleReportBuyboxWinningRuleStatsIn"] = t.struct(
        {"buyboxWonProductCount": t.integer().optional()}
    ).named(renames["RepricingRuleReportBuyboxWinningRuleStatsIn"])
    types["RepricingRuleReportBuyboxWinningRuleStatsOut"] = t.struct(
        {
            "buyboxWonProductCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepricingRuleReportBuyboxWinningRuleStatsOut"])
    types["LiasettingsCustomBatchRequestEntryIn"] = t.struct(
        {
            "contactEmail": t.string().optional(),
            "gmbEmail": t.string().optional(),
            "accountId": t.string().optional(),
            "batchId": t.integer().optional(),
            "liaSettings": t.proxy(renames["LiaSettingsIn"]).optional(),
            "method": t.string().optional(),
            "posDataProviderId": t.string().optional(),
            "contactName": t.string().optional(),
            "merchantId": t.string().optional(),
            "posExternalAccountId": t.string().optional(),
            "country": t.string().optional(),
        }
    ).named(renames["LiasettingsCustomBatchRequestEntryIn"])
    types["LiasettingsCustomBatchRequestEntryOut"] = t.struct(
        {
            "contactEmail": t.string().optional(),
            "gmbEmail": t.string().optional(),
            "accountId": t.string().optional(),
            "batchId": t.integer().optional(),
            "liaSettings": t.proxy(renames["LiaSettingsOut"]).optional(),
            "method": t.string().optional(),
            "posDataProviderId": t.string().optional(),
            "contactName": t.string().optional(),
            "merchantId": t.string().optional(),
            "posExternalAccountId": t.string().optional(),
            "country": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiasettingsCustomBatchRequestEntryOut"])
    types["HolidayCutoffIn"] = t.struct(
        {
            "holidayId": t.string().optional(),
            "deadlineTimezone": t.string().optional(),
            "deadlineDate": t.string().optional(),
            "visibleFromDate": t.string().optional(),
            "deadlineHour": t.integer().optional(),
        }
    ).named(renames["HolidayCutoffIn"])
    types["HolidayCutoffOut"] = t.struct(
        {
            "holidayId": t.string().optional(),
            "deadlineTimezone": t.string().optional(),
            "deadlineDate": t.string().optional(),
            "visibleFromDate": t.string().optional(),
            "deadlineHour": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HolidayCutoffOut"])
    types["AccountsCustomBatchResponseEntryIn"] = t.struct(
        {
            "account": t.proxy(renames["AccountIn"]).optional(),
            "batchId": t.integer().optional(),
            "kind": t.string().optional(),
            "errors": t.proxy(renames["ErrorsIn"]).optional(),
        }
    ).named(renames["AccountsCustomBatchResponseEntryIn"])
    types["AccountsCustomBatchResponseEntryOut"] = t.struct(
        {
            "account": t.proxy(renames["AccountOut"]).optional(),
            "batchId": t.integer().optional(),
            "kind": t.string().optional(),
            "errors": t.proxy(renames["ErrorsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountsCustomBatchResponseEntryOut"])
    types["PosCustomBatchResponseIn"] = t.struct(
        {
            "entries": t.array(
                t.proxy(renames["PosCustomBatchResponseEntryIn"])
            ).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["PosCustomBatchResponseIn"])
    types["PosCustomBatchResponseOut"] = t.struct(
        {
            "entries": t.array(
                t.proxy(renames["PosCustomBatchResponseEntryOut"])
            ).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PosCustomBatchResponseOut"])
    types["SettlementReportIn"] = t.struct(
        {
            "startDate": t.string().optional(),
            "endDate": t.string().optional(),
            "settlementId": t.string().optional(),
            "transferAmount": t.proxy(renames["PriceIn"]).optional(),
            "kind": t.string().optional(),
            "previousBalance": t.proxy(renames["PriceIn"]).optional(),
            "transferIds": t.array(t.string()).optional(),
            "transferDate": t.string().optional(),
        }
    ).named(renames["SettlementReportIn"])
    types["SettlementReportOut"] = t.struct(
        {
            "startDate": t.string().optional(),
            "endDate": t.string().optional(),
            "settlementId": t.string().optional(),
            "transferAmount": t.proxy(renames["PriceOut"]).optional(),
            "kind": t.string().optional(),
            "previousBalance": t.proxy(renames["PriceOut"]).optional(),
            "transferIds": t.array(t.string()).optional(),
            "transferDate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SettlementReportOut"])
    types["DatafeedsListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "resources": t.array(t.proxy(renames["DatafeedIn"])),
            "kind": t.string().optional(),
        }
    ).named(renames["DatafeedsListResponseIn"])
    types["DatafeedsListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "resources": t.array(t.proxy(renames["DatafeedOut"])),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatafeedsListResponseOut"])
    types["VerifyPhoneNumberResponseIn"] = t.struct(
        {"verifiedPhoneNumber": t.string().optional()}
    ).named(renames["VerifyPhoneNumberResponseIn"])
    types["VerifyPhoneNumberResponseOut"] = t.struct(
        {
            "verifiedPhoneNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VerifyPhoneNumberResponseOut"])
    types["ProductIdIn"] = t.struct({"productId": t.string().optional()}).named(
        renames["ProductIdIn"]
    )
    types["ProductIdOut"] = t.struct(
        {
            "productId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductIdOut"])
    types["RecommendationDescriptionIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RecommendationDescriptionIn"]
    )
    types["RecommendationDescriptionOut"] = t.struct(
        {
            "type": t.string().optional(),
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RecommendationDescriptionOut"])
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
    types["PosCustomBatchRequestEntryIn"] = t.struct(
        {
            "batchId": t.integer().optional(),
            "sale": t.proxy(renames["PosSaleIn"]).optional(),
            "storeCode": t.string().optional(),
            "merchantId": t.string().optional(),
            "targetMerchantId": t.string().optional(),
            "method": t.string().optional(),
            "inventory": t.proxy(renames["PosInventoryIn"]).optional(),
            "store": t.proxy(renames["PosStoreIn"]).optional(),
        }
    ).named(renames["PosCustomBatchRequestEntryIn"])
    types["PosCustomBatchRequestEntryOut"] = t.struct(
        {
            "batchId": t.integer().optional(),
            "sale": t.proxy(renames["PosSaleOut"]).optional(),
            "storeCode": t.string().optional(),
            "merchantId": t.string().optional(),
            "targetMerchantId": t.string().optional(),
            "method": t.string().optional(),
            "inventory": t.proxy(renames["PosInventoryOut"]).optional(),
            "store": t.proxy(renames["PosStoreOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PosCustomBatchRequestEntryOut"])
    types["UndeleteConversionSourceRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["UndeleteConversionSourceRequestIn"])
    types["UndeleteConversionSourceRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UndeleteConversionSourceRequestOut"])
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
            "googleAnalyticsLink": t.proxy(
                renames["GoogleAnalyticsLinkOut"]
            ).optional(),
            "conversionSourceId": t.string().optional(),
            "state": t.string().optional(),
            "expireTime": t.string().optional(),
            "merchantCenterDestination": t.proxy(
                renames["MerchantCenterDestinationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConversionSourceOut"])
    types["OrdersSetLineItemMetadataRequestIn"] = t.struct(
        {
            "productId": t.string().optional(),
            "operationId": t.string().optional(),
            "annotations": t.array(
                t.proxy(renames["OrderMerchantProvidedAnnotationIn"])
            ),
            "lineItemId": t.string().optional(),
        }
    ).named(renames["OrdersSetLineItemMetadataRequestIn"])
    types["OrdersSetLineItemMetadataRequestOut"] = t.struct(
        {
            "productId": t.string().optional(),
            "operationId": t.string().optional(),
            "annotations": t.array(
                t.proxy(renames["OrderMerchantProvidedAnnotationOut"])
            ),
            "lineItemId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersSetLineItemMetadataRequestOut"])
    types["ProductstatusesCustomBatchRequestEntryIn"] = t.struct(
        {
            "destinations": t.array(t.string()).optional(),
            "method": t.string().optional(),
            "includeAttributes": t.boolean().optional(),
            "merchantId": t.string().optional(),
            "productId": t.string().optional(),
            "batchId": t.integer().optional(),
        }
    ).named(renames["ProductstatusesCustomBatchRequestEntryIn"])
    types["ProductstatusesCustomBatchRequestEntryOut"] = t.struct(
        {
            "destinations": t.array(t.string()).optional(),
            "method": t.string().optional(),
            "includeAttributes": t.boolean().optional(),
            "merchantId": t.string().optional(),
            "productId": t.string().optional(),
            "batchId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductstatusesCustomBatchRequestEntryOut"])
    types["DatafeedStatusErrorIn"] = t.struct(
        {
            "examples": t.array(t.proxy(renames["DatafeedStatusExampleIn"])).optional(),
            "message": t.string().optional(),
            "count": t.string().optional(),
            "code": t.string().optional(),
        }
    ).named(renames["DatafeedStatusErrorIn"])
    types["DatafeedStatusErrorOut"] = t.struct(
        {
            "examples": t.array(
                t.proxy(renames["DatafeedStatusExampleOut"])
            ).optional(),
            "message": t.string().optional(),
            "count": t.string().optional(),
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatafeedStatusErrorOut"])
    types["ReportInteractionRequestIn"] = t.struct(
        {
            "interactionType": t.string(),
            "type": t.string(),
            "subtype": t.string().optional(),
            "responseToken": t.string(),
        }
    ).named(renames["ReportInteractionRequestIn"])
    types["ReportInteractionRequestOut"] = t.struct(
        {
            "interactionType": t.string(),
            "type": t.string(),
            "subtype": t.string().optional(),
            "responseToken": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportInteractionRequestOut"])
    types["AccountsCustomBatchResponseIn"] = t.struct(
        {
            "entries": t.array(
                t.proxy(renames["AccountsCustomBatchResponseEntryIn"])
            ).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["AccountsCustomBatchResponseIn"])
    types["AccountsCustomBatchResponseOut"] = t.struct(
        {
            "entries": t.array(
                t.proxy(renames["AccountsCustomBatchResponseEntryOut"])
            ).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountsCustomBatchResponseOut"])
    types["DatafeedstatusesCustomBatchResponseEntryIn"] = t.struct(
        {
            "datafeedStatus": t.proxy(renames["DatafeedStatusIn"]).optional(),
            "errors": t.proxy(renames["ErrorsIn"]).optional(),
            "batchId": t.integer().optional(),
        }
    ).named(renames["DatafeedstatusesCustomBatchResponseEntryIn"])
    types["DatafeedstatusesCustomBatchResponseEntryOut"] = t.struct(
        {
            "datafeedStatus": t.proxy(renames["DatafeedStatusOut"]).optional(),
            "errors": t.proxy(renames["ErrorsOut"]).optional(),
            "batchId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatafeedstatusesCustomBatchResponseEntryOut"])
    types["ReturnaddressListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "resources": t.array(t.proxy(renames["ReturnAddressIn"])),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ReturnaddressListResponseIn"])
    types["ReturnaddressListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "resources": t.array(t.proxy(renames["ReturnAddressOut"])),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReturnaddressListResponseOut"])
    types["PosInventoryRequestIn"] = t.struct(
        {
            "targetCountry": t.string(),
            "quantity": t.string(),
            "timestamp": t.string(),
            "storeCode": t.string(),
            "price": t.proxy(renames["PriceIn"]),
            "gtin": t.string().optional(),
            "contentLanguage": t.string(),
            "itemId": t.string(),
        }
    ).named(renames["PosInventoryRequestIn"])
    types["PosInventoryRequestOut"] = t.struct(
        {
            "targetCountry": t.string(),
            "quantity": t.string(),
            "timestamp": t.string(),
            "storeCode": t.string(),
            "price": t.proxy(renames["PriceOut"]),
            "gtin": t.string().optional(),
            "contentLanguage": t.string(),
            "itemId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PosInventoryRequestOut"])
    types["OrdersRejectReturnLineItemRequestIn"] = t.struct(
        {
            "reasonText": t.string().optional(),
            "operationId": t.string().optional(),
            "quantity": t.integer().optional(),
            "reason": t.string().optional(),
            "lineItemId": t.string().optional(),
            "productId": t.string().optional(),
        }
    ).named(renames["OrdersRejectReturnLineItemRequestIn"])
    types["OrdersRejectReturnLineItemRequestOut"] = t.struct(
        {
            "reasonText": t.string().optional(),
            "operationId": t.string().optional(),
            "quantity": t.integer().optional(),
            "reason": t.string().optional(),
            "lineItemId": t.string().optional(),
            "productId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersRejectReturnLineItemRequestOut"])
    types["ProductDeliveryTimeAreaDeliveryTimeDeliveryTimeIn"] = t.struct(
        {
            "maxTransitTimeDays": t.integer(),
            "maxHandlingTimeDays": t.integer(),
            "minHandlingTimeDays": t.integer(),
            "minTransitTimeDays": t.integer(),
        }
    ).named(renames["ProductDeliveryTimeAreaDeliveryTimeDeliveryTimeIn"])
    types["ProductDeliveryTimeAreaDeliveryTimeDeliveryTimeOut"] = t.struct(
        {
            "maxTransitTimeDays": t.integer(),
            "maxHandlingTimeDays": t.integer(),
            "minHandlingTimeDays": t.integer(),
            "minTransitTimeDays": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductDeliveryTimeAreaDeliveryTimeDeliveryTimeOut"])
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
    types["AccountTaxTaxRuleIn"] = t.struct(
        {
            "useGlobalRate": t.boolean().optional(),
            "country": t.string().optional(),
            "shippingTaxed": t.boolean().optional(),
            "locationId": t.string(),
            "ratePercent": t.string().optional(),
        }
    ).named(renames["AccountTaxTaxRuleIn"])
    types["AccountTaxTaxRuleOut"] = t.struct(
        {
            "useGlobalRate": t.boolean().optional(),
            "country": t.string().optional(),
            "shippingTaxed": t.boolean().optional(),
            "locationId": t.string(),
            "ratePercent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountTaxTaxRuleOut"])
    types["InstallmentIn"] = t.struct(
        {
            "months": t.string().optional(),
            "amount": t.proxy(renames["PriceIn"]).optional(),
        }
    ).named(renames["InstallmentIn"])
    types["InstallmentOut"] = t.struct(
        {
            "months": t.string().optional(),
            "amount": t.proxy(renames["PriceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstallmentOut"])
    types["CustomerLoyaltyDataIn"] = t.struct(
        {"loyaltyTier": t.string().optional()}
    ).named(renames["CustomerLoyaltyDataIn"])
    types["CustomerLoyaltyDataOut"] = t.struct(
        {
            "loyaltyTier": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomerLoyaltyDataOut"])
    types["AccountstatusesCustomBatchResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "entries": t.array(
                t.proxy(renames["AccountstatusesCustomBatchResponseEntryIn"])
            ).optional(),
        }
    ).named(renames["AccountstatusesCustomBatchResponseIn"])
    types["AccountstatusesCustomBatchResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "entries": t.array(
                t.proxy(renames["AccountstatusesCustomBatchResponseEntryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountstatusesCustomBatchResponseOut"])
    types["OrderCancellationIn"] = t.struct(
        {
            "reason": t.string().optional(),
            "creationDate": t.string().optional(),
            "actor": t.string().optional(),
            "reasonText": t.string().optional(),
            "quantity": t.integer().optional(),
        }
    ).named(renames["OrderCancellationIn"])
    types["OrderCancellationOut"] = t.struct(
        {
            "reason": t.string().optional(),
            "creationDate": t.string().optional(),
            "actor": t.string().optional(),
            "reasonText": t.string().optional(),
            "quantity": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderCancellationOut"])
    types["BestSellersIn"] = t.struct(
        {
            "reportGranularity": t.string().optional(),
            "relativeDemandChange": t.string().optional(),
            "relativeDemand": t.string().optional(),
            "rank": t.string().optional(),
            "categoryId": t.string().optional(),
            "previousRelativeDemand": t.string().optional(),
            "countryCode": t.string().optional(),
            "reportDate": t.proxy(renames["DateIn"]).optional(),
            "previousRank": t.string().optional(),
        }
    ).named(renames["BestSellersIn"])
    types["BestSellersOut"] = t.struct(
        {
            "reportGranularity": t.string().optional(),
            "relativeDemandChange": t.string().optional(),
            "relativeDemand": t.string().optional(),
            "rank": t.string().optional(),
            "categoryId": t.string().optional(),
            "previousRelativeDemand": t.string().optional(),
            "countryCode": t.string().optional(),
            "reportDate": t.proxy(renames["DateOut"]).optional(),
            "previousRank": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BestSellersOut"])
    types["RateGroupIn"] = t.struct(
        {
            "applicableShippingLabels": t.array(t.string()).optional(),
            "mainTable": t.proxy(renames["TableIn"]).optional(),
            "singleValue": t.proxy(renames["ValueIn"]).optional(),
            "subtables": t.array(t.proxy(renames["TableIn"])).optional(),
            "carrierRates": t.array(t.proxy(renames["CarrierRateIn"])).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["RateGroupIn"])
    types["RateGroupOut"] = t.struct(
        {
            "applicableShippingLabels": t.array(t.string()).optional(),
            "mainTable": t.proxy(renames["TableOut"]).optional(),
            "singleValue": t.proxy(renames["ValueOut"]).optional(),
            "subtables": t.array(t.proxy(renames["TableOut"])).optional(),
            "carrierRates": t.array(t.proxy(renames["CarrierRateOut"])).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RateGroupOut"])
    types["OrderReportDisbursementIn"] = t.struct(
        {
            "disbursementId": t.string().optional(),
            "merchantId": t.string().optional(),
            "disbursementAmount": t.proxy(renames["PriceIn"]).optional(),
            "disbursementDate": t.string().optional(),
            "disbursementCreationDate": t.string().optional(),
        }
    ).named(renames["OrderReportDisbursementIn"])
    types["OrderReportDisbursementOut"] = t.struct(
        {
            "disbursementId": t.string().optional(),
            "merchantId": t.string().optional(),
            "disbursementAmount": t.proxy(renames["PriceOut"]).optional(),
            "disbursementDate": t.string().optional(),
            "disbursementCreationDate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderReportDisbursementOut"])
    types["AccountsCustomBatchRequestEntryLinkRequestIn"] = t.struct(
        {
            "action": t.string().optional(),
            "linkedAccountId": t.string().optional(),
            "services": t.array(t.string()).optional(),
            "linkType": t.string().optional(),
        }
    ).named(renames["AccountsCustomBatchRequestEntryLinkRequestIn"])
    types["AccountsCustomBatchRequestEntryLinkRequestOut"] = t.struct(
        {
            "action": t.string().optional(),
            "linkedAccountId": t.string().optional(),
            "services": t.array(t.string()).optional(),
            "linkType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountsCustomBatchRequestEntryLinkRequestOut"])
    types["SettlementTransactionAmountCommissionIn"] = t.struct(
        {"rate": t.string().optional(), "category": t.string().optional()}
    ).named(renames["SettlementTransactionAmountCommissionIn"])
    types["SettlementTransactionAmountCommissionOut"] = t.struct(
        {
            "rate": t.string().optional(),
            "category": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SettlementTransactionAmountCommissionOut"])
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
    types["AccountItemUpdatesSettingsIn"] = t.struct(
        {
            "allowAvailabilityUpdates": t.boolean().optional(),
            "allowStrictAvailabilityUpdates": t.boolean().optional(),
            "allowPriceUpdates": t.boolean().optional(),
            "allowConditionUpdates": t.boolean().optional(),
        }
    ).named(renames["AccountItemUpdatesSettingsIn"])
    types["AccountItemUpdatesSettingsOut"] = t.struct(
        {
            "allowAvailabilityUpdates": t.boolean().optional(),
            "allowStrictAvailabilityUpdates": t.boolean().optional(),
            "allowPriceUpdates": t.boolean().optional(),
            "allowConditionUpdates": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountItemUpdatesSettingsOut"])
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
    types["OnboardBuyOnGoogleProgramRequestIn"] = t.struct(
        {"customerServiceEmail": t.string().optional()}
    ).named(renames["OnboardBuyOnGoogleProgramRequestIn"])
    types["OnboardBuyOnGoogleProgramRequestOut"] = t.struct(
        {
            "customerServiceEmail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OnboardBuyOnGoogleProgramRequestOut"])
    types["ShipmentInvoiceIn"] = t.struct(
        {
            "shipmentGroupId": t.string().optional(),
            "lineItemInvoices": t.array(
                t.proxy(renames["ShipmentInvoiceLineItemInvoiceIn"])
            ).optional(),
            "invoiceSummary": t.proxy(renames["InvoiceSummaryIn"]).optional(),
        }
    ).named(renames["ShipmentInvoiceIn"])
    types["ShipmentInvoiceOut"] = t.struct(
        {
            "shipmentGroupId": t.string().optional(),
            "lineItemInvoices": t.array(
                t.proxy(renames["ShipmentInvoiceLineItemInvoiceOut"])
            ).optional(),
            "invoiceSummary": t.proxy(renames["InvoiceSummaryOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShipmentInvoiceOut"])
    types["SettlementreportsListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "resources": t.array(t.proxy(renames["SettlementReportIn"])),
            "kind": t.string().optional(),
        }
    ).named(renames["SettlementreportsListResponseIn"])
    types["SettlementreportsListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "resources": t.array(t.proxy(renames["SettlementReportOut"])),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SettlementreportsListResponseOut"])
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
    types["TestOrderIn"] = t.struct(
        {
            "promotions": t.array(t.proxy(renames["OrderPromotionIn"])).optional(),
            "shippingCost": t.proxy(renames["PriceIn"]),
            "predefinedEmail": t.string(),
            "kind": t.string().optional(),
            "predefinedPickupDetails": t.string().optional(),
            "enableOrderinvoices": t.boolean().optional(),
            "shippingOption": t.string(),
            "pickupDetails": t.proxy(renames["TestOrderPickupDetailsIn"]).optional(),
            "predefinedBillingAddress": t.string(),
            "predefinedDeliveryAddress": t.string(),
            "lineItems": t.array(t.proxy(renames["TestOrderLineItemIn"])),
            "deliveryDetails": t.proxy(
                renames["TestOrderDeliveryDetailsIn"]
            ).optional(),
            "notificationMode": t.string().optional(),
        }
    ).named(renames["TestOrderIn"])
    types["TestOrderOut"] = t.struct(
        {
            "promotions": t.array(t.proxy(renames["OrderPromotionOut"])).optional(),
            "shippingCost": t.proxy(renames["PriceOut"]),
            "predefinedEmail": t.string(),
            "kind": t.string().optional(),
            "predefinedPickupDetails": t.string().optional(),
            "enableOrderinvoices": t.boolean().optional(),
            "shippingOption": t.string(),
            "pickupDetails": t.proxy(renames["TestOrderPickupDetailsOut"]).optional(),
            "predefinedBillingAddress": t.string(),
            "predefinedDeliveryAddress": t.string(),
            "lineItems": t.array(t.proxy(renames["TestOrderLineItemOut"])),
            "deliveryDetails": t.proxy(
                renames["TestOrderDeliveryDetailsOut"]
            ).optional(),
            "notificationMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestOrderOut"])
    types["LiaSettingsIn"] = t.struct(
        {
            "accountId": t.string().optional(),
            "countrySettings": t.array(
                t.proxy(renames["LiaCountrySettingsIn"])
            ).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["LiaSettingsIn"])
    types["LiaSettingsOut"] = t.struct(
        {
            "accountId": t.string().optional(),
            "countrySettings": t.array(
                t.proxy(renames["LiaCountrySettingsOut"])
            ).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiaSettingsOut"])
    types["MerchantOrderReturnIn"] = t.struct(
        {
            "returnShipments": t.array(t.proxy(renames["ReturnShipmentIn"])).optional(),
            "returnPricingInfo": t.proxy(renames["ReturnPricingInfoIn"]).optional(),
            "creationDate": t.string().optional(),
            "merchantOrderId": t.string().optional(),
            "orderReturnId": t.string().optional(),
            "returnItems": t.array(
                t.proxy(renames["MerchantOrderReturnItemIn"])
            ).optional(),
            "orderId": t.string().optional(),
        }
    ).named(renames["MerchantOrderReturnIn"])
    types["MerchantOrderReturnOut"] = t.struct(
        {
            "returnShipments": t.array(
                t.proxy(renames["ReturnShipmentOut"])
            ).optional(),
            "returnPricingInfo": t.proxy(renames["ReturnPricingInfoOut"]).optional(),
            "creationDate": t.string().optional(),
            "merchantOrderId": t.string().optional(),
            "orderReturnId": t.string().optional(),
            "returnItems": t.array(
                t.proxy(renames["MerchantOrderReturnItemOut"])
            ).optional(),
            "orderId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MerchantOrderReturnOut"])
    types["DatafeedIn"] = t.struct(
        {
            "name": t.string(),
            "fileName": t.string(),
            "contentType": t.string(),
            "fetchSchedule": t.proxy(renames["DatafeedFetchScheduleIn"]).optional(),
            "kind": t.string().optional(),
            "id": t.string(),
            "attributeLanguage": t.string().optional(),
            "format": t.proxy(renames["DatafeedFormatIn"]).optional(),
            "targets": t.array(t.proxy(renames["DatafeedTargetIn"])).optional(),
        }
    ).named(renames["DatafeedIn"])
    types["DatafeedOut"] = t.struct(
        {
            "name": t.string(),
            "fileName": t.string(),
            "contentType": t.string(),
            "fetchSchedule": t.proxy(renames["DatafeedFetchScheduleOut"]).optional(),
            "kind": t.string().optional(),
            "id": t.string(),
            "attributeLanguage": t.string().optional(),
            "format": t.proxy(renames["DatafeedFormatOut"]).optional(),
            "targets": t.array(t.proxy(renames["DatafeedTargetOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatafeedOut"])
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
    types["AccountStatusItemLevelIssueIn"] = t.struct(
        {
            "attributeName": t.string().optional(),
            "detail": t.string().optional(),
            "documentation": t.string().optional(),
            "numItems": t.string().optional(),
            "code": t.string().optional(),
            "resolution": t.string().optional(),
            "description": t.string().optional(),
            "servability": t.string().optional(),
        }
    ).named(renames["AccountStatusItemLevelIssueIn"])
    types["AccountStatusItemLevelIssueOut"] = t.struct(
        {
            "attributeName": t.string().optional(),
            "detail": t.string().optional(),
            "documentation": t.string().optional(),
            "numItems": t.string().optional(),
            "code": t.string().optional(),
            "resolution": t.string().optional(),
            "description": t.string().optional(),
            "servability": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountStatusItemLevelIssueOut"])
    types["ReturnpolicyCustomBatchResponseEntryIn"] = t.struct(
        {
            "errors": t.proxy(renames["ErrorsIn"]).optional(),
            "kind": t.string().optional(),
            "returnPolicy": t.proxy(renames["ReturnPolicyIn"]).optional(),
            "batchId": t.integer().optional(),
        }
    ).named(renames["ReturnpolicyCustomBatchResponseEntryIn"])
    types["ReturnpolicyCustomBatchResponseEntryOut"] = t.struct(
        {
            "errors": t.proxy(renames["ErrorsOut"]).optional(),
            "kind": t.string().optional(),
            "returnPolicy": t.proxy(renames["ReturnPolicyOut"]).optional(),
            "batchId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReturnpolicyCustomBatchResponseEntryOut"])
    types["OrderreturnsProcessResponseIn"] = t.struct(
        {"executionStatus": t.string().optional(), "kind": t.string().optional()}
    ).named(renames["OrderreturnsProcessResponseIn"])
    types["OrderreturnsProcessResponseOut"] = t.struct(
        {
            "executionStatus": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderreturnsProcessResponseOut"])
    types["AccounttaxCustomBatchResponseEntryIn"] = t.struct(
        {
            "batchId": t.integer().optional(),
            "errors": t.proxy(renames["ErrorsIn"]).optional(),
            "kind": t.string().optional(),
            "accountTax": t.proxy(renames["AccountTaxIn"]).optional(),
        }
    ).named(renames["AccounttaxCustomBatchResponseEntryIn"])
    types["AccounttaxCustomBatchResponseEntryOut"] = t.struct(
        {
            "batchId": t.integer().optional(),
            "errors": t.proxy(renames["ErrorsOut"]).optional(),
            "kind": t.string().optional(),
            "accountTax": t.proxy(renames["AccountTaxOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccounttaxCustomBatchResponseEntryOut"])
    types["TableIn"] = t.struct(
        {
            "name": t.string().optional(),
            "columnHeaders": t.proxy(renames["HeadersIn"]).optional(),
            "rows": t.array(t.proxy(renames["RowIn"])).optional(),
            "rowHeaders": t.proxy(renames["HeadersIn"]).optional(),
        }
    ).named(renames["TableIn"])
    types["TableOut"] = t.struct(
        {
            "name": t.string().optional(),
            "columnHeaders": t.proxy(renames["HeadersOut"]).optional(),
            "rows": t.array(t.proxy(renames["RowOut"])).optional(),
            "rowHeaders": t.proxy(renames["HeadersOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableOut"])
    types["ProductTaxIn"] = t.struct(
        {
            "locationId": t.string().optional(),
            "rate": t.number().optional(),
            "postalCode": t.string().optional(),
            "region": t.string().optional(),
            "country": t.string().optional(),
            "taxShip": t.boolean().optional(),
        }
    ).named(renames["ProductTaxIn"])
    types["ProductTaxOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "rate": t.number().optional(),
            "postalCode": t.string().optional(),
            "region": t.string().optional(),
            "country": t.string().optional(),
            "taxShip": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductTaxOut"])
    types["SearchResponseIn"] = t.struct(
        {
            "results": t.array(t.proxy(renames["ReportRowIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["SearchResponseIn"])
    types["SearchResponseOut"] = t.struct(
        {
            "results": t.array(t.proxy(renames["ReportRowOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchResponseOut"])
    types["LocalInventoryIn"] = t.struct(
        {
            "salePriceEffectiveDate": t.string().optional(),
            "instoreProductLocation": t.string().optional(),
            "availability": t.string().optional(),
            "kind": t.string().optional(),
            "pickupSla": t.string().optional(),
            "pickupMethod": t.string().optional(),
            "quantity": t.integer().optional(),
            "price": t.proxy(renames["PriceIn"]).optional(),
            "salePrice": t.proxy(renames["PriceIn"]).optional(),
            "storeCode": t.string(),
            "customAttributes": t.array(
                t.proxy(renames["CustomAttributeIn"])
            ).optional(),
        }
    ).named(renames["LocalInventoryIn"])
    types["LocalInventoryOut"] = t.struct(
        {
            "salePriceEffectiveDate": t.string().optional(),
            "instoreProductLocation": t.string().optional(),
            "availability": t.string().optional(),
            "kind": t.string().optional(),
            "pickupSla": t.string().optional(),
            "pickupMethod": t.string().optional(),
            "quantity": t.integer().optional(),
            "price": t.proxy(renames["PriceOut"]).optional(),
            "salePrice": t.proxy(renames["PriceOut"]).optional(),
            "storeCode": t.string(),
            "customAttributes": t.array(
                t.proxy(renames["CustomAttributeOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocalInventoryOut"])
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
    types["OrderreturnsAcknowledgeRequestIn"] = t.struct(
        {"operationId": t.string().optional()}
    ).named(renames["OrderreturnsAcknowledgeRequestIn"])
    types["OrderreturnsAcknowledgeRequestOut"] = t.struct(
        {
            "operationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderreturnsAcknowledgeRequestOut"])
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
    types["ReturnPolicyIn"] = t.struct(
        {
            "label": t.string(),
            "seasonalOverrides": t.array(
                t.proxy(renames["ReturnPolicySeasonalOverrideIn"])
            ).optional(),
            "kind": t.string().optional(),
            "policy": t.proxy(renames["ReturnPolicyPolicyIn"]),
            "nonFreeReturnReasons": t.array(t.string()).optional(),
            "country": t.string(),
            "returnShippingFee": t.proxy(renames["PriceIn"]).optional(),
            "name": t.string(),
            "returnPolicyId": t.string().optional(),
        }
    ).named(renames["ReturnPolicyIn"])
    types["ReturnPolicyOut"] = t.struct(
        {
            "label": t.string(),
            "seasonalOverrides": t.array(
                t.proxy(renames["ReturnPolicySeasonalOverrideOut"])
            ).optional(),
            "kind": t.string().optional(),
            "policy": t.proxy(renames["ReturnPolicyPolicyOut"]),
            "nonFreeReturnReasons": t.array(t.string()).optional(),
            "country": t.string(),
            "returnShippingFee": t.proxy(renames["PriceOut"]).optional(),
            "name": t.string(),
            "returnPolicyId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReturnPolicyOut"])
    types["DatafeedsFetchNowResponseIn"] = t.struct(
        {"kind": t.string().optional()}
    ).named(renames["DatafeedsFetchNowResponseIn"])
    types["DatafeedsFetchNowResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatafeedsFetchNowResponseOut"])
    types["OrderAddressIn"] = t.struct(
        {
            "postalCode": t.string().optional(),
            "isPostOfficeBox": t.boolean().optional(),
            "streetAddress": t.array(t.string()).optional(),
            "country": t.string().optional(),
            "region": t.string().optional(),
            "locality": t.string().optional(),
            "fullAddress": t.array(t.string()).optional(),
            "recipientName": t.string().optional(),
        }
    ).named(renames["OrderAddressIn"])
    types["OrderAddressOut"] = t.struct(
        {
            "postalCode": t.string().optional(),
            "isPostOfficeBox": t.boolean().optional(),
            "streetAddress": t.array(t.string()).optional(),
            "country": t.string().optional(),
            "region": t.string().optional(),
            "locality": t.string().optional(),
            "fullAddress": t.array(t.string()).optional(),
            "recipientName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderAddressOut"])
    types["FreeListingsProgramStatusReviewIneligibilityReasonDetailsIn"] = t.struct(
        {"cooldownTime": t.string().optional()}
    ).named(renames["FreeListingsProgramStatusReviewIneligibilityReasonDetailsIn"])
    types["FreeListingsProgramStatusReviewIneligibilityReasonDetailsOut"] = t.struct(
        {
            "cooldownTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FreeListingsProgramStatusReviewIneligibilityReasonDetailsOut"])
    types["ReturnShipmentIn"] = t.struct(
        {
            "shipmentId": t.string().optional(),
            "creationDate": t.string().optional(),
            "shippingDate": t.string().optional(),
            "state": t.string().optional(),
            "returnMethodType": t.string().optional(),
            "deliveryDate": t.string().optional(),
            "shipmentTrackingInfos": t.array(
                t.proxy(renames["ShipmentTrackingInfoIn"])
            ).optional(),
        }
    ).named(renames["ReturnShipmentIn"])
    types["ReturnShipmentOut"] = t.struct(
        {
            "shipmentId": t.string().optional(),
            "creationDate": t.string().optional(),
            "shippingDate": t.string().optional(),
            "state": t.string().optional(),
            "returnMethodType": t.string().optional(),
            "deliveryDate": t.string().optional(),
            "shipmentTrackingInfos": t.array(
                t.proxy(renames["ShipmentTrackingInfoOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReturnShipmentOut"])
    types["DatafeedsCustomBatchRequestEntryIn"] = t.struct(
        {
            "merchantId": t.string().optional(),
            "datafeed": t.proxy(renames["DatafeedIn"]).optional(),
            "method": t.string().optional(),
            "batchId": t.integer().optional(),
            "datafeedId": t.string().optional(),
        }
    ).named(renames["DatafeedsCustomBatchRequestEntryIn"])
    types["DatafeedsCustomBatchRequestEntryOut"] = t.struct(
        {
            "merchantId": t.string().optional(),
            "datafeed": t.proxy(renames["DatafeedOut"]).optional(),
            "method": t.string().optional(),
            "batchId": t.integer().optional(),
            "datafeedId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatafeedsCustomBatchRequestEntryOut"])
    types["ReturnpolicyCustomBatchRequestEntryIn"] = t.struct(
        {
            "returnPolicyId": t.string().optional(),
            "method": t.string().optional(),
            "batchId": t.integer().optional(),
            "returnPolicy": t.proxy(renames["ReturnPolicyIn"]).optional(),
            "merchantId": t.string().optional(),
        }
    ).named(renames["ReturnpolicyCustomBatchRequestEntryIn"])
    types["ReturnpolicyCustomBatchRequestEntryOut"] = t.struct(
        {
            "returnPolicyId": t.string().optional(),
            "method": t.string().optional(),
            "batchId": t.integer().optional(),
            "returnPolicy": t.proxy(renames["ReturnPolicyOut"]).optional(),
            "merchantId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReturnpolicyCustomBatchRequestEntryOut"])
    types["LiasettingsSetPosDataProviderResponseIn"] = t.struct(
        {"kind": t.string().optional()}
    ).named(renames["LiasettingsSetPosDataProviderResponseIn"])
    types["LiasettingsSetPosDataProviderResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiasettingsSetPosDataProviderResponseOut"])
    types["ProductStatusIn"] = t.struct(
        {
            "title": t.string().optional(),
            "productId": t.string().optional(),
            "lastUpdateDate": t.string().optional(),
            "itemLevelIssues": t.array(
                t.proxy(renames["ProductStatusItemLevelIssueIn"])
            ).optional(),
            "creationDate": t.string().optional(),
            "link": t.string().optional(),
            "destinationStatuses": t.array(
                t.proxy(renames["ProductStatusDestinationStatusIn"])
            ).optional(),
            "kind": t.string().optional(),
            "googleExpirationDate": t.string().optional(),
        }
    ).named(renames["ProductStatusIn"])
    types["ProductStatusOut"] = t.struct(
        {
            "title": t.string().optional(),
            "productId": t.string().optional(),
            "lastUpdateDate": t.string().optional(),
            "itemLevelIssues": t.array(
                t.proxy(renames["ProductStatusItemLevelIssueOut"])
            ).optional(),
            "creationDate": t.string().optional(),
            "link": t.string().optional(),
            "destinationStatuses": t.array(
                t.proxy(renames["ProductStatusDestinationStatusOut"])
            ).optional(),
            "kind": t.string().optional(),
            "googleExpirationDate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductStatusOut"])
    types["LiaAboutPageSettingsIn"] = t.struct(
        {"url": t.string().optional(), "status": t.string().optional()}
    ).named(renames["LiaAboutPageSettingsIn"])
    types["LiaAboutPageSettingsOut"] = t.struct(
        {
            "url": t.string().optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiaAboutPageSettingsOut"])
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
    types["LiasettingsListResponseIn"] = t.struct(
        {
            "resources": t.array(t.proxy(renames["LiaSettingsIn"])),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["LiasettingsListResponseIn"])
    types["LiasettingsListResponseOut"] = t.struct(
        {
            "resources": t.array(t.proxy(renames["LiaSettingsOut"])),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiasettingsListResponseOut"])
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
    types["AccountShippingImprovementsIn"] = t.struct(
        {"allowShippingImprovements": t.boolean().optional()}
    ).named(renames["AccountShippingImprovementsIn"])
    types["AccountShippingImprovementsOut"] = t.struct(
        {
            "allowShippingImprovements": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountShippingImprovementsOut"])
    types["LiasettingsCustomBatchResponseEntryIn"] = t.struct(
        {
            "errors": t.proxy(renames["ErrorsIn"]).optional(),
            "gmbAccounts": t.proxy(renames["GmbAccountsIn"]).optional(),
            "posDataProviders": t.array(
                t.proxy(renames["PosDataProvidersIn"])
            ).optional(),
            "liaSettings": t.proxy(renames["LiaSettingsIn"]).optional(),
            "batchId": t.integer().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["LiasettingsCustomBatchResponseEntryIn"])
    types["LiasettingsCustomBatchResponseEntryOut"] = t.struct(
        {
            "errors": t.proxy(renames["ErrorsOut"]).optional(),
            "gmbAccounts": t.proxy(renames["GmbAccountsOut"]).optional(),
            "posDataProviders": t.array(
                t.proxy(renames["PosDataProvidersOut"])
            ).optional(),
            "liaSettings": t.proxy(renames["LiaSettingsOut"]).optional(),
            "batchId": t.integer().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiasettingsCustomBatchResponseEntryOut"])
    types["ReturnPricingInfoIn"] = t.struct(
        {
            "totalRefundedAmount": t.proxy(renames["MonetaryAmountIn"]).optional(),
            "refundableItemsTotalAmount": t.proxy(
                renames["MonetaryAmountIn"]
            ).optional(),
            "refundableShippingAmount": t.proxy(renames["MonetaryAmountIn"]).optional(),
            "chargeReturnShippingFee": t.boolean().optional(),
            "maxReturnShippingFee": t.proxy(renames["MonetaryAmountIn"]).optional(),
        }
    ).named(renames["ReturnPricingInfoIn"])
    types["ReturnPricingInfoOut"] = t.struct(
        {
            "totalRefundedAmount": t.proxy(renames["MonetaryAmountOut"]).optional(),
            "refundableItemsTotalAmount": t.proxy(
                renames["MonetaryAmountOut"]
            ).optional(),
            "refundableShippingAmount": t.proxy(
                renames["MonetaryAmountOut"]
            ).optional(),
            "chargeReturnShippingFee": t.boolean().optional(),
            "maxReturnShippingFee": t.proxy(renames["MonetaryAmountOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReturnPricingInfoOut"])
    types["OrderMerchantProvidedAnnotationIn"] = t.struct(
        {"value": t.string().optional(), "key": t.string().optional()}
    ).named(renames["OrderMerchantProvidedAnnotationIn"])
    types["OrderMerchantProvidedAnnotationOut"] = t.struct(
        {
            "value": t.string().optional(),
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderMerchantProvidedAnnotationOut"])
    types["RepricingProductReportBuyboxWinningProductStatsIn"] = t.struct(
        {"buyboxWinsCount": t.integer().optional()}
    ).named(renames["RepricingProductReportBuyboxWinningProductStatsIn"])
    types["RepricingProductReportBuyboxWinningProductStatsOut"] = t.struct(
        {
            "buyboxWinsCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepricingProductReportBuyboxWinningProductStatsOut"])
    types["ProductSubscriptionCostIn"] = t.struct(
        {
            "amount": t.proxy(renames["PriceIn"]).optional(),
            "periodLength": t.string().optional(),
            "period": t.string().optional(),
        }
    ).named(renames["ProductSubscriptionCostIn"])
    types["ProductSubscriptionCostOut"] = t.struct(
        {
            "amount": t.proxy(renames["PriceOut"]).optional(),
            "periodLength": t.string().optional(),
            "period": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductSubscriptionCostOut"])
    types["ReportRowIn"] = t.struct(
        {
            "metrics": t.proxy(renames["MetricsIn"]).optional(),
            "bestSellers": t.proxy(renames["BestSellersIn"]).optional(),
            "priceInsights": t.proxy(renames["PriceInsightsIn"]).optional(),
            "productView": t.proxy(renames["ProductViewIn"]).optional(),
            "brand": t.proxy(renames["BrandIn"]).optional(),
            "segments": t.proxy(renames["SegmentsIn"]).optional(),
            "priceCompetitiveness": t.proxy(
                renames["PriceCompetitivenessIn"]
            ).optional(),
            "productCluster": t.proxy(renames["ProductClusterIn"]).optional(),
        }
    ).named(renames["ReportRowIn"])
    types["ReportRowOut"] = t.struct(
        {
            "metrics": t.proxy(renames["MetricsOut"]).optional(),
            "bestSellers": t.proxy(renames["BestSellersOut"]).optional(),
            "priceInsights": t.proxy(renames["PriceInsightsOut"]).optional(),
            "productView": t.proxy(renames["ProductViewOut"]).optional(),
            "brand": t.proxy(renames["BrandOut"]).optional(),
            "segments": t.proxy(renames["SegmentsOut"]).optional(),
            "priceCompetitiveness": t.proxy(
                renames["PriceCompetitivenessOut"]
            ).optional(),
            "productCluster": t.proxy(renames["ProductClusterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportRowOut"])
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
    types["MinimumOrderValueTableStoreCodeSetWithMovIn"] = t.struct(
        {
            "value": t.proxy(renames["PriceIn"]).optional(),
            "storeCodes": t.array(t.string()).optional(),
        }
    ).named(renames["MinimumOrderValueTableStoreCodeSetWithMovIn"])
    types["MinimumOrderValueTableStoreCodeSetWithMovOut"] = t.struct(
        {
            "value": t.proxy(renames["PriceOut"]).optional(),
            "storeCodes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MinimumOrderValueTableStoreCodeSetWithMovOut"])
    types["OrderDeliveryDetailsIn"] = t.struct(
        {
            "address": t.proxy(renames["OrderAddressIn"]).optional(),
            "phoneNumber": t.string().optional(),
        }
    ).named(renames["OrderDeliveryDetailsIn"])
    types["OrderDeliveryDetailsOut"] = t.struct(
        {
            "address": t.proxy(renames["OrderAddressOut"]).optional(),
            "phoneNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderDeliveryDetailsOut"])
    types["AccountstatusesCustomBatchResponseEntryIn"] = t.struct(
        {
            "accountStatus": t.proxy(renames["AccountStatusIn"]).optional(),
            "batchId": t.integer().optional(),
            "errors": t.proxy(renames["ErrorsIn"]).optional(),
        }
    ).named(renames["AccountstatusesCustomBatchResponseEntryIn"])
    types["AccountstatusesCustomBatchResponseEntryOut"] = t.struct(
        {
            "accountStatus": t.proxy(renames["AccountStatusOut"]).optional(),
            "batchId": t.integer().optional(),
            "errors": t.proxy(renames["ErrorsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountstatusesCustomBatchResponseEntryOut"])
    types["AccountsUpdateLabelsRequestIn"] = t.struct(
        {"labelIds": t.array(t.string()).optional()}
    ).named(renames["AccountsUpdateLabelsRequestIn"])
    types["AccountsUpdateLabelsRequestOut"] = t.struct(
        {
            "labelIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountsUpdateLabelsRequestOut"])
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
    types["ReturnPolicyOnlineIn"] = t.struct(
        {
            "returnPolicyUri": t.string().optional(),
            "label": t.string().optional(),
            "policy": t.proxy(renames["ReturnPolicyOnlinePolicyIn"]).optional(),
            "name": t.string().optional(),
            "itemConditions": t.array(t.string()).optional(),
            "countries": t.array(t.string()).optional(),
            "returnReasonCategoryInfo": t.array(
                t.proxy(renames["ReturnPolicyOnlineReturnReasonCategoryInfoIn"])
            ).optional(),
            "restockingFee": t.proxy(
                renames["ReturnPolicyOnlineRestockingFeeIn"]
            ).optional(),
            "returnMethods": t.array(t.string()).optional(),
        }
    ).named(renames["ReturnPolicyOnlineIn"])
    types["ReturnPolicyOnlineOut"] = t.struct(
        {
            "returnPolicyUri": t.string().optional(),
            "returnPolicyId": t.string().optional(),
            "label": t.string().optional(),
            "policy": t.proxy(renames["ReturnPolicyOnlinePolicyOut"]).optional(),
            "name": t.string().optional(),
            "itemConditions": t.array(t.string()).optional(),
            "countries": t.array(t.string()).optional(),
            "returnReasonCategoryInfo": t.array(
                t.proxy(renames["ReturnPolicyOnlineReturnReasonCategoryInfoOut"])
            ).optional(),
            "restockingFee": t.proxy(
                renames["ReturnPolicyOnlineRestockingFeeOut"]
            ).optional(),
            "returnMethods": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReturnPolicyOnlineOut"])
    types["OrderreturnsRefundOperationIn"] = t.struct(
        {
            "fullRefund": t.boolean().optional(),
            "partialRefund": t.proxy(renames["OrderreturnsPartialRefundIn"]).optional(),
            "paymentType": t.string().optional(),
            "returnRefundReason": t.string().optional(),
            "reasonText": t.string().optional(),
        }
    ).named(renames["OrderreturnsRefundOperationIn"])
    types["OrderreturnsRefundOperationOut"] = t.struct(
        {
            "fullRefund": t.boolean().optional(),
            "partialRefund": t.proxy(
                renames["OrderreturnsPartialRefundOut"]
            ).optional(),
            "paymentType": t.string().optional(),
            "returnRefundReason": t.string().optional(),
            "reasonText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderreturnsRefundOperationOut"])
    types["ProductViewIn"] = t.struct(
        {
            "expirationDate": t.proxy(renames["DateIn"]).optional(),
            "offerId": t.string().optional(),
            "aggregatedDestinationStatus": t.string().optional(),
            "categoryL3": t.string().optional(),
            "brand": t.string().optional(),
            "condition": t.string().optional(),
            "productTypeL2": t.string().optional(),
            "priceMicros": t.string().optional(),
            "title": t.string().optional(),
            "itemGroupId": t.string().optional(),
            "id": t.string().optional(),
            "productTypeL5": t.string().optional(),
            "categoryL2": t.string().optional(),
            "productTypeL4": t.string().optional(),
            "languageCode": t.string().optional(),
            "productTypeL3": t.string().optional(),
            "categoryL5": t.string().optional(),
            "currencyCode": t.string().optional(),
            "itemIssues": t.array(
                t.proxy(renames["ProductViewItemIssueIn"])
            ).optional(),
            "shippingLabel": t.string().optional(),
            "channel": t.string().optional(),
            "availability": t.string().optional(),
            "gtin": t.array(t.string()).optional(),
            "creationTime": t.string().optional(),
            "productTypeL1": t.string().optional(),
            "categoryL1": t.string().optional(),
            "categoryL4": t.string().optional(),
        }
    ).named(renames["ProductViewIn"])
    types["ProductViewOut"] = t.struct(
        {
            "expirationDate": t.proxy(renames["DateOut"]).optional(),
            "offerId": t.string().optional(),
            "aggregatedDestinationStatus": t.string().optional(),
            "categoryL3": t.string().optional(),
            "brand": t.string().optional(),
            "condition": t.string().optional(),
            "productTypeL2": t.string().optional(),
            "priceMicros": t.string().optional(),
            "title": t.string().optional(),
            "itemGroupId": t.string().optional(),
            "id": t.string().optional(),
            "productTypeL5": t.string().optional(),
            "categoryL2": t.string().optional(),
            "productTypeL4": t.string().optional(),
            "languageCode": t.string().optional(),
            "productTypeL3": t.string().optional(),
            "categoryL5": t.string().optional(),
            "currencyCode": t.string().optional(),
            "itemIssues": t.array(
                t.proxy(renames["ProductViewItemIssueOut"])
            ).optional(),
            "shippingLabel": t.string().optional(),
            "channel": t.string().optional(),
            "availability": t.string().optional(),
            "gtin": t.array(t.string()).optional(),
            "creationTime": t.string().optional(),
            "productTypeL1": t.string().optional(),
            "categoryL1": t.string().optional(),
            "categoryL4": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductViewOut"])
    types["RepricingRuleEligibleOfferMatcherIn"] = t.struct(
        {
            "brandMatcher": t.proxy(
                renames["RepricingRuleEligibleOfferMatcherStringMatcherIn"]
            ).optional(),
            "offerIdMatcher": t.proxy(
                renames["RepricingRuleEligibleOfferMatcherStringMatcherIn"]
            ).optional(),
            "itemGroupIdMatcher": t.proxy(
                renames["RepricingRuleEligibleOfferMatcherStringMatcherIn"]
            ).optional(),
            "matcherOption": t.string().optional(),
            "skipWhenOnPromotion": t.boolean().optional(),
        }
    ).named(renames["RepricingRuleEligibleOfferMatcherIn"])
    types["RepricingRuleEligibleOfferMatcherOut"] = t.struct(
        {
            "brandMatcher": t.proxy(
                renames["RepricingRuleEligibleOfferMatcherStringMatcherOut"]
            ).optional(),
            "offerIdMatcher": t.proxy(
                renames["RepricingRuleEligibleOfferMatcherStringMatcherOut"]
            ).optional(),
            "itemGroupIdMatcher": t.proxy(
                renames["RepricingRuleEligibleOfferMatcherStringMatcherOut"]
            ).optional(),
            "matcherOption": t.string().optional(),
            "skipWhenOnPromotion": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepricingRuleEligibleOfferMatcherOut"])
    types["CollectionFeaturedProductIn"] = t.struct(
        {"x": t.number(), "offerId": t.string().optional(), "y": t.number()}
    ).named(renames["CollectionFeaturedProductIn"])
    types["CollectionFeaturedProductOut"] = t.struct(
        {
            "x": t.number(),
            "offerId": t.string().optional(),
            "y": t.number(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CollectionFeaturedProductOut"])
    types["AccountLabelIn"] = t.struct(
        {
            "name": t.string().optional(),
            "accountId": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["AccountLabelIn"])
    types["AccountLabelOut"] = t.struct(
        {
            "labelId": t.string().optional(),
            "name": t.string().optional(),
            "accountId": t.string().optional(),
            "labelType": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountLabelOut"])
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
    types["AccountsClaimWebsiteResponseIn"] = t.struct(
        {"kind": t.string().optional()}
    ).named(renames["AccountsClaimWebsiteResponseIn"])
    types["AccountsClaimWebsiteResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountsClaimWebsiteResponseOut"])
    types["ReturnaddressCustomBatchResponseEntryIn"] = t.struct(
        {
            "batchId": t.integer().optional(),
            "returnAddress": t.proxy(renames["ReturnAddressIn"]).optional(),
            "errors": t.proxy(renames["ErrorsIn"]).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ReturnaddressCustomBatchResponseEntryIn"])
    types["ReturnaddressCustomBatchResponseEntryOut"] = t.struct(
        {
            "batchId": t.integer().optional(),
            "returnAddress": t.proxy(renames["ReturnAddressOut"]).optional(),
            "errors": t.proxy(renames["ErrorsOut"]).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReturnaddressCustomBatchResponseEntryOut"])
    types["OrdersCustomBatchRequestEntryShipLineItemsShipmentInfoIn"] = t.struct(
        {
            "shipmentId": t.string(),
            "carrier": t.string().optional(),
            "trackingId": t.string().optional(),
        }
    ).named(renames["OrdersCustomBatchRequestEntryShipLineItemsShipmentInfoIn"])
    types["OrdersCustomBatchRequestEntryShipLineItemsShipmentInfoOut"] = t.struct(
        {
            "shipmentId": t.string(),
            "carrier": t.string().optional(),
            "trackingId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrdersCustomBatchRequestEntryShipLineItemsShipmentInfoOut"])
    types["UnitInvoiceIn"] = t.struct(
        {
            "additionalCharges": t.array(
                t.proxy(renames["UnitInvoiceAdditionalChargeIn"])
            ).optional(),
            "unitPriceTaxes": t.array(
                t.proxy(renames["UnitInvoiceTaxLineIn"])
            ).optional(),
            "unitPrice": t.proxy(renames["PriceIn"]).optional(),
        }
    ).named(renames["UnitInvoiceIn"])
    types["UnitInvoiceOut"] = t.struct(
        {
            "additionalCharges": t.array(
                t.proxy(renames["UnitInvoiceAdditionalChargeOut"])
            ).optional(),
            "unitPriceTaxes": t.array(
                t.proxy(renames["UnitInvoiceTaxLineOut"])
            ).optional(),
            "unitPrice": t.proxy(renames["PriceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UnitInvoiceOut"])
    types["RepricingRuleStatsBasedRuleIn"] = t.struct(
        {"priceDelta": t.string().optional(), "percentageDelta": t.integer().optional()}
    ).named(renames["RepricingRuleStatsBasedRuleIn"])
    types["RepricingRuleStatsBasedRuleOut"] = t.struct(
        {
            "priceDelta": t.string().optional(),
            "percentageDelta": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepricingRuleStatsBasedRuleOut"])
    types["CustomAttributeIn"] = t.struct(
        {
            "value": t.string().optional(),
            "groupValues": t.array(t.proxy(renames["CustomAttributeIn"])).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["CustomAttributeIn"])
    types["CustomAttributeOut"] = t.struct(
        {
            "value": t.string().optional(),
            "groupValues": t.array(t.proxy(renames["CustomAttributeOut"])).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomAttributeOut"])
    types["ReturnPolicyOnlineReturnShippingFeeIn"] = t.struct(
        {
            "fixedFee": t.proxy(renames["PriceAmountIn"]).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["ReturnPolicyOnlineReturnShippingFeeIn"])
    types["ReturnPolicyOnlineReturnShippingFeeOut"] = t.struct(
        {
            "fixedFee": t.proxy(renames["PriceAmountOut"]).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReturnPolicyOnlineReturnShippingFeeOut"])
    types["OrderreturnsListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "resources": t.array(t.proxy(renames["MerchantOrderReturnIn"])),
        }
    ).named(renames["OrderreturnsListResponseIn"])
    types["OrderreturnsListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "resources": t.array(t.proxy(renames["MerchantOrderReturnOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderreturnsListResponseOut"])
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
    types["OrderTrackingSignalIn"] = t.struct(
        {
            "deliveryPostalCode": t.string(),
            "shippingInfo": t.array(
                t.proxy(renames["OrderTrackingSignalShippingInfoIn"])
            ).optional(),
            "customerShippingFee": t.proxy(renames["PriceAmountIn"]).optional(),
            "shipmentLineItemMapping": t.array(
                t.proxy(renames["OrderTrackingSignalShipmentLineItemMappingIn"])
            ).optional(),
            "orderCreatedTime": t.proxy(renames["DateTimeIn"]),
            "lineItems": t.array(
                t.proxy(renames["OrderTrackingSignalLineItemDetailsIn"])
            ).optional(),
            "merchantId": t.string().optional(),
            "deliveryRegionCode": t.string(),
            "orderId": t.string(),
        }
    ).named(renames["OrderTrackingSignalIn"])
    types["OrderTrackingSignalOut"] = t.struct(
        {
            "deliveryPostalCode": t.string(),
            "shippingInfo": t.array(
                t.proxy(renames["OrderTrackingSignalShippingInfoOut"])
            ).optional(),
            "customerShippingFee": t.proxy(renames["PriceAmountOut"]).optional(),
            "shipmentLineItemMapping": t.array(
                t.proxy(renames["OrderTrackingSignalShipmentLineItemMappingOut"])
            ).optional(),
            "orderCreatedTime": t.proxy(renames["DateTimeOut"]),
            "lineItems": t.array(
                t.proxy(renames["OrderTrackingSignalLineItemDetailsOut"])
            ).optional(),
            "merchantId": t.string().optional(),
            "deliveryRegionCode": t.string(),
            "orderTrackingSignalId": t.string().optional(),
            "orderId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderTrackingSignalOut"])
    types["AccountstatusesListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "resources": t.array(t.proxy(renames["AccountStatusIn"])),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["AccountstatusesListResponseIn"])
    types["AccountstatusesListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "resources": t.array(t.proxy(renames["AccountStatusOut"])),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountstatusesListResponseOut"])
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
    types["CloudExportAdditionalPropertiesIn"] = t.struct(
        {
            "maxValue": t.number().optional(),
            "floatValue": t.array(t.number()).optional(),
            "boolValue": t.boolean().optional(),
            "propertyName": t.string().optional(),
            "intValue": t.array(t.string()).optional(),
            "textValue": t.array(t.string()).optional(),
            "unitCode": t.string().optional(),
            "minValue": t.number().optional(),
        }
    ).named(renames["CloudExportAdditionalPropertiesIn"])
    types["CloudExportAdditionalPropertiesOut"] = t.struct(
        {
            "maxValue": t.number().optional(),
            "floatValue": t.array(t.number()).optional(),
            "boolValue": t.boolean().optional(),
            "propertyName": t.string().optional(),
            "intValue": t.array(t.string()).optional(),
            "textValue": t.array(t.string()).optional(),
            "unitCode": t.string().optional(),
            "minValue": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudExportAdditionalPropertiesOut"])
    types["OrderIn"] = t.struct(
        {
            "acknowledged": t.boolean().optional(),
            "customer": t.proxy(renames["OrderCustomerIn"]).optional(),
            "netPriceAmount": t.proxy(renames["PriceIn"]).optional(),
            "deliveryDetails": t.proxy(renames["OrderDeliveryDetailsIn"]).optional(),
            "kind": t.string().optional(),
            "pickupDetails": t.proxy(renames["OrderPickupDetailsIn"]).optional(),
            "merchantOrderId": t.string().optional(),
            "id": t.string().optional(),
            "promotions": t.array(t.proxy(renames["OrderPromotionIn"])).optional(),
            "placedDate": t.string().optional(),
            "annotations": t.array(
                t.proxy(renames["OrderOrderAnnotationIn"])
            ).optional(),
            "paymentStatus": t.string().optional(),
            "taxCollector": t.string().optional(),
            "billingAddress": t.proxy(renames["OrderAddressIn"]).optional(),
            "netTaxAmount": t.proxy(renames["PriceIn"]).optional(),
            "refunds": t.array(t.proxy(renames["OrderRefundIn"])).optional(),
            "status": t.string().optional(),
            "lineItems": t.array(t.proxy(renames["OrderLineItemIn"])).optional(),
            "merchantId": t.string(),
            "shipments": t.array(t.proxy(renames["OrderShipmentIn"])).optional(),
            "shippingCost": t.proxy(renames["PriceIn"]).optional(),
            "shippingCostTax": t.proxy(renames["PriceIn"]).optional(),
        }
    ).named(renames["OrderIn"])
    types["OrderOut"] = t.struct(
        {
            "acknowledged": t.boolean().optional(),
            "customer": t.proxy(renames["OrderCustomerOut"]).optional(),
            "netPriceAmount": t.proxy(renames["PriceOut"]).optional(),
            "deliveryDetails": t.proxy(renames["OrderDeliveryDetailsOut"]).optional(),
            "kind": t.string().optional(),
            "pickupDetails": t.proxy(renames["OrderPickupDetailsOut"]).optional(),
            "merchantOrderId": t.string().optional(),
            "id": t.string().optional(),
            "promotions": t.array(t.proxy(renames["OrderPromotionOut"])).optional(),
            "placedDate": t.string().optional(),
            "annotations": t.array(
                t.proxy(renames["OrderOrderAnnotationOut"])
            ).optional(),
            "paymentStatus": t.string().optional(),
            "taxCollector": t.string().optional(),
            "billingAddress": t.proxy(renames["OrderAddressOut"]).optional(),
            "netTaxAmount": t.proxy(renames["PriceOut"]).optional(),
            "refunds": t.array(t.proxy(renames["OrderRefundOut"])).optional(),
            "status": t.string().optional(),
            "lineItems": t.array(t.proxy(renames["OrderLineItemOut"])).optional(),
            "merchantId": t.string(),
            "shipments": t.array(t.proxy(renames["OrderShipmentOut"])).optional(),
            "shippingCost": t.proxy(renames["PriceOut"]).optional(),
            "shippingCostTax": t.proxy(renames["PriceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderOut"])
    types["ErrorIn"] = t.struct(
        {
            "message": t.string().optional(),
            "reason": t.string().optional(),
            "domain": t.string().optional(),
        }
    ).named(renames["ErrorIn"])
    types["ErrorOut"] = t.struct(
        {
            "message": t.string().optional(),
            "reason": t.string().optional(),
            "domain": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ErrorOut"])
    types["InvoiceSummaryIn"] = t.struct(
        {
            "productTotal": t.proxy(renames["AmountIn"]).optional(),
            "additionalChargeSummaries": t.array(
                t.proxy(renames["InvoiceSummaryAdditionalChargeSummaryIn"])
            ).optional(),
        }
    ).named(renames["InvoiceSummaryIn"])
    types["InvoiceSummaryOut"] = t.struct(
        {
            "productTotal": t.proxy(renames["AmountOut"]).optional(),
            "additionalChargeSummaries": t.array(
                t.proxy(renames["InvoiceSummaryAdditionalChargeSummaryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InvoiceSummaryOut"])
    types["LiasettingsListPosDataProvidersResponseIn"] = t.struct(
        {
            "posDataProviders": t.array(
                t.proxy(renames["PosDataProvidersIn"])
            ).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["LiasettingsListPosDataProvidersResponseIn"])
    types["LiasettingsListPosDataProvidersResponseOut"] = t.struct(
        {
            "posDataProviders": t.array(
                t.proxy(renames["PosDataProvidersOut"])
            ).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiasettingsListPosDataProvidersResponseOut"])
    types["CollectionIn"] = t.struct(
        {
            "language": t.string().optional(),
            "customLabel4": t.string().optional(),
            "customLabel2": t.string().optional(),
            "customLabel0": t.string().optional(),
            "customLabel3": t.string().optional(),
            "featuredProduct": t.array(
                t.proxy(renames["CollectionFeaturedProductIn"])
            ).optional(),
            "link": t.string().optional(),
            "headline": t.array(t.string()).optional(),
            "productCountry": t.string().optional(),
            "customLabel1": t.string().optional(),
            "id": t.string(),
            "imageLink": t.array(t.string()).optional(),
            "mobileLink": t.string().optional(),
        }
    ).named(renames["CollectionIn"])
    types["CollectionOut"] = t.struct(
        {
            "language": t.string().optional(),
            "customLabel4": t.string().optional(),
            "customLabel2": t.string().optional(),
            "customLabel0": t.string().optional(),
            "customLabel3": t.string().optional(),
            "featuredProduct": t.array(
                t.proxy(renames["CollectionFeaturedProductOut"])
            ).optional(),
            "link": t.string().optional(),
            "headline": t.array(t.string()).optional(),
            "productCountry": t.string().optional(),
            "customLabel1": t.string().optional(),
            "id": t.string(),
            "imageLink": t.array(t.string()).optional(),
            "mobileLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CollectionOut"])
    types["WarehouseIn"] = t.struct(
        {
            "name": t.string(),
            "handlingDays": t.string(),
            "businessDayConfig": t.proxy(renames["BusinessDayConfigIn"]).optional(),
            "shippingAddress": t.proxy(renames["AddressIn"]),
            "cutoffTime": t.proxy(renames["WarehouseCutoffTimeIn"]),
        }
    ).named(renames["WarehouseIn"])
    types["WarehouseOut"] = t.struct(
        {
            "name": t.string(),
            "handlingDays": t.string(),
            "businessDayConfig": t.proxy(renames["BusinessDayConfigOut"]).optional(),
            "shippingAddress": t.proxy(renames["AddressOut"]),
            "cutoffTime": t.proxy(renames["WarehouseCutoffTimeOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WarehouseOut"])
    types["PosDataProvidersPosDataProviderIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "fullName": t.string().optional(),
            "providerId": t.string().optional(),
        }
    ).named(renames["PosDataProvidersPosDataProviderIn"])
    types["PosDataProvidersPosDataProviderOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "fullName": t.string().optional(),
            "providerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PosDataProvidersPosDataProviderOut"])
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
    types["AccountGoogleMyBusinessLinkIn"] = t.struct(
        {
            "gmbEmail": t.string().optional(),
            "gmbAccountId": t.string().optional(),
            "status": t.string().optional(),
        }
    ).named(renames["AccountGoogleMyBusinessLinkIn"])
    types["AccountGoogleMyBusinessLinkOut"] = t.struct(
        {
            "gmbEmail": t.string().optional(),
            "gmbAccountId": t.string().optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountGoogleMyBusinessLinkOut"])
    types["GoogleAnalyticsLinkIn"] = t.struct({"propertyId": t.string()}).named(
        renames["GoogleAnalyticsLinkIn"]
    )
    types["GoogleAnalyticsLinkOut"] = t.struct(
        {
            "propertyId": t.string(),
            "propertyName": t.string().optional(),
            "attributionSettings": t.proxy(
                renames["AttributionSettingsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAnalyticsLinkOut"])
    types["ProductsCustomBatchResponseEntryIn"] = t.struct(
        {
            "errors": t.proxy(renames["ErrorsIn"]).optional(),
            "kind": t.string().optional(),
            "product": t.proxy(renames["ProductIn"]).optional(),
            "batchId": t.integer().optional(),
        }
    ).named(renames["ProductsCustomBatchResponseEntryIn"])
    types["ProductsCustomBatchResponseEntryOut"] = t.struct(
        {
            "errors": t.proxy(renames["ErrorsOut"]).optional(),
            "kind": t.string().optional(),
            "product": t.proxy(renames["ProductOut"]).optional(),
            "batchId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductsCustomBatchResponseEntryOut"])
    types["LiasettingsRequestInventoryVerificationResponseIn"] = t.struct(
        {"kind": t.string().optional()}
    ).named(renames["LiasettingsRequestInventoryVerificationResponseIn"])
    types["LiasettingsRequestInventoryVerificationResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LiasettingsRequestInventoryVerificationResponseOut"])
    types["OrderReportTransactionIn"] = t.struct(
        {
            "disbursementCreationDate": t.string().optional(),
            "productAmount": t.proxy(renames["ProductAmountIn"]).optional(),
            "disbursementAmount": t.proxy(renames["PriceIn"]).optional(),
            "disbursementDate": t.string().optional(),
            "transactionDate": t.string().optional(),
            "orderId": t.string().optional(),
            "merchantOrderId": t.string().optional(),
            "merchantId": t.string().optional(),
            "disbursementId": t.string().optional(),
        }
    ).named(renames["OrderReportTransactionIn"])
    types["OrderReportTransactionOut"] = t.struct(
        {
            "disbursementCreationDate": t.string().optional(),
            "productAmount": t.proxy(renames["ProductAmountOut"]).optional(),
            "disbursementAmount": t.proxy(renames["PriceOut"]).optional(),
            "disbursementDate": t.string().optional(),
            "transactionDate": t.string().optional(),
            "orderId": t.string().optional(),
            "merchantOrderId": t.string().optional(),
            "merchantId": t.string().optional(),
            "disbursementId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderReportTransactionOut"])
    types["DatafeedStatusIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "lastUploadDate": t.string().optional(),
            "language": t.string().optional(),
            "itemsTotal": t.string().optional(),
            "warnings": t.array(t.proxy(renames["DatafeedStatusErrorIn"])).optional(),
            "errors": t.array(t.proxy(renames["DatafeedStatusErrorIn"])).optional(),
            "country": t.string().optional(),
            "feedLabel": t.string().optional(),
            "processingStatus": t.string().optional(),
            "datafeedId": t.string().optional(),
            "itemsValid": t.string().optional(),
        }
    ).named(renames["DatafeedStatusIn"])
    types["DatafeedStatusOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "lastUploadDate": t.string().optional(),
            "language": t.string().optional(),
            "itemsTotal": t.string().optional(),
            "warnings": t.array(t.proxy(renames["DatafeedStatusErrorOut"])).optional(),
            "errors": t.array(t.proxy(renames["DatafeedStatusErrorOut"])).optional(),
            "country": t.string().optional(),
            "feedLabel": t.string().optional(),
            "processingStatus": t.string().optional(),
            "datafeedId": t.string().optional(),
            "itemsValid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatafeedStatusOut"])
    types["TimeZoneIn"] = t.struct(
        {"id": t.string().optional(), "version": t.string().optional()}
    ).named(renames["TimeZoneIn"])
    types["TimeZoneOut"] = t.struct(
        {
            "id": t.string().optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeZoneOut"])
    types["OrderReturnIn"] = t.struct(
        {
            "quantity": t.integer().optional(),
            "reasonText": t.string().optional(),
            "reason": t.string().optional(),
            "creationDate": t.string().optional(),
            "actor": t.string().optional(),
        }
    ).named(renames["OrderReturnIn"])
    types["OrderReturnOut"] = t.struct(
        {
            "quantity": t.integer().optional(),
            "reasonText": t.string().optional(),
            "reason": t.string().optional(),
            "creationDate": t.string().optional(),
            "actor": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderReturnOut"])

    functions = {}
    functions["freelistingsprogramGet"] = content.post(
        "{merchantId}/freelistingsprogram/requestreview",
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
    functions["freelistingsprogramRequestreview"] = content.post(
        "{merchantId}/freelistingsprogram/requestreview",
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
    functions["returnpolicyDelete"] = content.post(
        "{merchantId}/returnpolicy",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "label": t.string(),
                "seasonalOverrides": t.array(
                    t.proxy(renames["ReturnPolicySeasonalOverrideIn"])
                ).optional(),
                "kind": t.string().optional(),
                "policy": t.proxy(renames["ReturnPolicyPolicyIn"]),
                "nonFreeReturnReasons": t.array(t.string()).optional(),
                "country": t.string(),
                "returnShippingFee": t.proxy(renames["PriceIn"]).optional(),
                "name": t.string(),
                "returnPolicyId": t.string().optional(),
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
                "label": t.string(),
                "seasonalOverrides": t.array(
                    t.proxy(renames["ReturnPolicySeasonalOverrideIn"])
                ).optional(),
                "kind": t.string().optional(),
                "policy": t.proxy(renames["ReturnPolicyPolicyIn"]),
                "nonFreeReturnReasons": t.array(t.string()).optional(),
                "country": t.string(),
                "returnShippingFee": t.proxy(renames["PriceIn"]).optional(),
                "name": t.string(),
                "returnPolicyId": t.string().optional(),
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
                "label": t.string(),
                "seasonalOverrides": t.array(
                    t.proxy(renames["ReturnPolicySeasonalOverrideIn"])
                ).optional(),
                "kind": t.string().optional(),
                "policy": t.proxy(renames["ReturnPolicyPolicyIn"]),
                "nonFreeReturnReasons": t.array(t.string()).optional(),
                "country": t.string(),
                "returnShippingFee": t.proxy(renames["PriceIn"]).optional(),
                "name": t.string(),
                "returnPolicyId": t.string().optional(),
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
                "label": t.string(),
                "seasonalOverrides": t.array(
                    t.proxy(renames["ReturnPolicySeasonalOverrideIn"])
                ).optional(),
                "kind": t.string().optional(),
                "policy": t.proxy(renames["ReturnPolicyPolicyIn"]),
                "nonFreeReturnReasons": t.array(t.string()).optional(),
                "country": t.string(),
                "returnShippingFee": t.proxy(renames["PriceIn"]).optional(),
                "name": t.string(),
                "returnPolicyId": t.string().optional(),
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
                "label": t.string(),
                "seasonalOverrides": t.array(
                    t.proxy(renames["ReturnPolicySeasonalOverrideIn"])
                ).optional(),
                "kind": t.string().optional(),
                "policy": t.proxy(renames["ReturnPolicyPolicyIn"]),
                "nonFreeReturnReasons": t.array(t.string()).optional(),
                "country": t.string(),
                "returnShippingFee": t.proxy(renames["PriceIn"]).optional(),
                "name": t.string(),
                "returnPolicyId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReturnPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["ordersInstorerefundlineitem"] = content.post(
        "{merchantId}/orders/{orderId}/refunditem",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "orderId": t.string().optional(),
                "reason": t.string().optional(),
                "reasonText": t.string().optional(),
                "operationId": t.string().optional(),
                "items": t.array(
                    t.proxy(renames["OrdersCustomBatchRequestEntryRefundItemItemIn"])
                ).optional(),
                "shipping": t.proxy(
                    renames["OrdersCustomBatchRequestEntryRefundItemShippingIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrdersRefundItemResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["ordersShiplineitems"] = content.post(
        "{merchantId}/orders/{orderId}/refunditem",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "orderId": t.string().optional(),
                "reason": t.string().optional(),
                "reasonText": t.string().optional(),
                "operationId": t.string().optional(),
                "items": t.array(
                    t.proxy(renames["OrdersCustomBatchRequestEntryRefundItemItemIn"])
                ).optional(),
                "shipping": t.proxy(
                    renames["OrdersCustomBatchRequestEntryRefundItemShippingIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrdersRefundItemResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["ordersUpdateshipment"] = content.post(
        "{merchantId}/orders/{orderId}/refunditem",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "orderId": t.string().optional(),
                "reason": t.string().optional(),
                "reasonText": t.string().optional(),
                "operationId": t.string().optional(),
                "items": t.array(
                    t.proxy(renames["OrdersCustomBatchRequestEntryRefundItemItemIn"])
                ).optional(),
                "shipping": t.proxy(
                    renames["OrdersCustomBatchRequestEntryRefundItemShippingIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrdersRefundItemResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["ordersUpdatelineitemshippingdetails"] = content.post(
        "{merchantId}/orders/{orderId}/refunditem",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "orderId": t.string().optional(),
                "reason": t.string().optional(),
                "reasonText": t.string().optional(),
                "operationId": t.string().optional(),
                "items": t.array(
                    t.proxy(renames["OrdersCustomBatchRequestEntryRefundItemItemIn"])
                ).optional(),
                "shipping": t.proxy(
                    renames["OrdersCustomBatchRequestEntryRefundItemShippingIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrdersRefundItemResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["ordersGettestordertemplate"] = content.post(
        "{merchantId}/orders/{orderId}/refunditem",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "orderId": t.string().optional(),
                "reason": t.string().optional(),
                "reasonText": t.string().optional(),
                "operationId": t.string().optional(),
                "items": t.array(
                    t.proxy(renames["OrdersCustomBatchRequestEntryRefundItemItemIn"])
                ).optional(),
                "shipping": t.proxy(
                    renames["OrdersCustomBatchRequestEntryRefundItemShippingIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrdersRefundItemResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["ordersCanceltestorderbycustomer"] = content.post(
        "{merchantId}/orders/{orderId}/refunditem",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "orderId": t.string().optional(),
                "reason": t.string().optional(),
                "reasonText": t.string().optional(),
                "operationId": t.string().optional(),
                "items": t.array(
                    t.proxy(renames["OrdersCustomBatchRequestEntryRefundItemItemIn"])
                ).optional(),
                "shipping": t.proxy(
                    renames["OrdersCustomBatchRequestEntryRefundItemShippingIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrdersRefundItemResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["ordersCreatetestorder"] = content.post(
        "{merchantId}/orders/{orderId}/refunditem",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "orderId": t.string().optional(),
                "reason": t.string().optional(),
                "reasonText": t.string().optional(),
                "operationId": t.string().optional(),
                "items": t.array(
                    t.proxy(renames["OrdersCustomBatchRequestEntryRefundItemItemIn"])
                ).optional(),
                "shipping": t.proxy(
                    renames["OrdersCustomBatchRequestEntryRefundItemShippingIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrdersRefundItemResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["ordersReturnrefundlineitem"] = content.post(
        "{merchantId}/orders/{orderId}/refunditem",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "orderId": t.string().optional(),
                "reason": t.string().optional(),
                "reasonText": t.string().optional(),
                "operationId": t.string().optional(),
                "items": t.array(
                    t.proxy(renames["OrdersCustomBatchRequestEntryRefundItemItemIn"])
                ).optional(),
                "shipping": t.proxy(
                    renames["OrdersCustomBatchRequestEntryRefundItemShippingIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrdersRefundItemResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["ordersSetlineitemmetadata"] = content.post(
        "{merchantId}/orders/{orderId}/refunditem",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "orderId": t.string().optional(),
                "reason": t.string().optional(),
                "reasonText": t.string().optional(),
                "operationId": t.string().optional(),
                "items": t.array(
                    t.proxy(renames["OrdersCustomBatchRequestEntryRefundItemItemIn"])
                ).optional(),
                "shipping": t.proxy(
                    renames["OrdersCustomBatchRequestEntryRefundItemShippingIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrdersRefundItemResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["ordersRejectreturnlineitem"] = content.post(
        "{merchantId}/orders/{orderId}/refunditem",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "orderId": t.string().optional(),
                "reason": t.string().optional(),
                "reasonText": t.string().optional(),
                "operationId": t.string().optional(),
                "items": t.array(
                    t.proxy(renames["OrdersCustomBatchRequestEntryRefundItemItemIn"])
                ).optional(),
                "shipping": t.proxy(
                    renames["OrdersCustomBatchRequestEntryRefundItemShippingIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrdersRefundItemResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["ordersAcknowledge"] = content.post(
        "{merchantId}/orders/{orderId}/refunditem",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "orderId": t.string().optional(),
                "reason": t.string().optional(),
                "reasonText": t.string().optional(),
                "operationId": t.string().optional(),
                "items": t.array(
                    t.proxy(renames["OrdersCustomBatchRequestEntryRefundItemItemIn"])
                ).optional(),
                "shipping": t.proxy(
                    renames["OrdersCustomBatchRequestEntryRefundItemShippingIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrdersRefundItemResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["ordersGet"] = content.post(
        "{merchantId}/orders/{orderId}/refunditem",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "orderId": t.string().optional(),
                "reason": t.string().optional(),
                "reasonText": t.string().optional(),
                "operationId": t.string().optional(),
                "items": t.array(
                    t.proxy(renames["OrdersCustomBatchRequestEntryRefundItemItemIn"])
                ).optional(),
                "shipping": t.proxy(
                    renames["OrdersCustomBatchRequestEntryRefundItemShippingIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrdersRefundItemResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["ordersCancellineitem"] = content.post(
        "{merchantId}/orders/{orderId}/refunditem",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "orderId": t.string().optional(),
                "reason": t.string().optional(),
                "reasonText": t.string().optional(),
                "operationId": t.string().optional(),
                "items": t.array(
                    t.proxy(renames["OrdersCustomBatchRequestEntryRefundItemItemIn"])
                ).optional(),
                "shipping": t.proxy(
                    renames["OrdersCustomBatchRequestEntryRefundItemShippingIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrdersRefundItemResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["ordersCaptureOrder"] = content.post(
        "{merchantId}/orders/{orderId}/refunditem",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "orderId": t.string().optional(),
                "reason": t.string().optional(),
                "reasonText": t.string().optional(),
                "operationId": t.string().optional(),
                "items": t.array(
                    t.proxy(renames["OrdersCustomBatchRequestEntryRefundItemItemIn"])
                ).optional(),
                "shipping": t.proxy(
                    renames["OrdersCustomBatchRequestEntryRefundItemShippingIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrdersRefundItemResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["ordersUpdatemerchantorderid"] = content.post(
        "{merchantId}/orders/{orderId}/refunditem",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "orderId": t.string().optional(),
                "reason": t.string().optional(),
                "reasonText": t.string().optional(),
                "operationId": t.string().optional(),
                "items": t.array(
                    t.proxy(renames["OrdersCustomBatchRequestEntryRefundItemItemIn"])
                ).optional(),
                "shipping": t.proxy(
                    renames["OrdersCustomBatchRequestEntryRefundItemShippingIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrdersRefundItemResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["ordersGetbymerchantorderid"] = content.post(
        "{merchantId}/orders/{orderId}/refunditem",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "orderId": t.string().optional(),
                "reason": t.string().optional(),
                "reasonText": t.string().optional(),
                "operationId": t.string().optional(),
                "items": t.array(
                    t.proxy(renames["OrdersCustomBatchRequestEntryRefundItemItemIn"])
                ).optional(),
                "shipping": t.proxy(
                    renames["OrdersCustomBatchRequestEntryRefundItemShippingIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrdersRefundItemResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["ordersRefundorder"] = content.post(
        "{merchantId}/orders/{orderId}/refunditem",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "orderId": t.string().optional(),
                "reason": t.string().optional(),
                "reasonText": t.string().optional(),
                "operationId": t.string().optional(),
                "items": t.array(
                    t.proxy(renames["OrdersCustomBatchRequestEntryRefundItemItemIn"])
                ).optional(),
                "shipping": t.proxy(
                    renames["OrdersCustomBatchRequestEntryRefundItemShippingIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrdersRefundItemResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["ordersCancel"] = content.post(
        "{merchantId}/orders/{orderId}/refunditem",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "orderId": t.string().optional(),
                "reason": t.string().optional(),
                "reasonText": t.string().optional(),
                "operationId": t.string().optional(),
                "items": t.array(
                    t.proxy(renames["OrdersCustomBatchRequestEntryRefundItemItemIn"])
                ).optional(),
                "shipping": t.proxy(
                    renames["OrdersCustomBatchRequestEntryRefundItemShippingIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrdersRefundItemResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["ordersAdvancetestorder"] = content.post(
        "{merchantId}/orders/{orderId}/refunditem",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "orderId": t.string().optional(),
                "reason": t.string().optional(),
                "reasonText": t.string().optional(),
                "operationId": t.string().optional(),
                "items": t.array(
                    t.proxy(renames["OrdersCustomBatchRequestEntryRefundItemItemIn"])
                ).optional(),
                "shipping": t.proxy(
                    renames["OrdersCustomBatchRequestEntryRefundItemShippingIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrdersRefundItemResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["ordersList"] = content.post(
        "{merchantId}/orders/{orderId}/refunditem",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "orderId": t.string().optional(),
                "reason": t.string().optional(),
                "reasonText": t.string().optional(),
                "operationId": t.string().optional(),
                "items": t.array(
                    t.proxy(renames["OrdersCustomBatchRequestEntryRefundItemItemIn"])
                ).optional(),
                "shipping": t.proxy(
                    renames["OrdersCustomBatchRequestEntryRefundItemShippingIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrdersRefundItemResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["ordersCreatetestreturn"] = content.post(
        "{merchantId}/orders/{orderId}/refunditem",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "orderId": t.string().optional(),
                "reason": t.string().optional(),
                "reasonText": t.string().optional(),
                "operationId": t.string().optional(),
                "items": t.array(
                    t.proxy(renames["OrdersCustomBatchRequestEntryRefundItemItemIn"])
                ).optional(),
                "shipping": t.proxy(
                    renames["OrdersCustomBatchRequestEntryRefundItemShippingIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrdersRefundItemResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["ordersRefunditem"] = content.post(
        "{merchantId}/orders/{orderId}/refunditem",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "orderId": t.string().optional(),
                "reason": t.string().optional(),
                "reasonText": t.string().optional(),
                "operationId": t.string().optional(),
                "items": t.array(
                    t.proxy(renames["OrdersCustomBatchRequestEntryRefundItemItemIn"])
                ).optional(),
                "shipping": t.proxy(
                    renames["OrdersCustomBatchRequestEntryRefundItemShippingIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrdersRefundItemResponseOut"]),
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
    functions["returnpolicyonlinePatch"] = content.post(
        "{merchantId}/returnpolicyonline",
        t.struct(
            {
                "merchantId": t.string(),
                "returnPolicyUri": t.string().optional(),
                "label": t.string().optional(),
                "policy": t.proxy(renames["ReturnPolicyOnlinePolicyIn"]).optional(),
                "name": t.string().optional(),
                "itemConditions": t.array(t.string()).optional(),
                "countries": t.array(t.string()).optional(),
                "returnReasonCategoryInfo": t.array(
                    t.proxy(renames["ReturnPolicyOnlineReturnReasonCategoryInfoIn"])
                ).optional(),
                "restockingFee": t.proxy(
                    renames["ReturnPolicyOnlineRestockingFeeIn"]
                ).optional(),
                "returnMethods": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReturnPolicyOnlineOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["returnpolicyonlineGet"] = content.post(
        "{merchantId}/returnpolicyonline",
        t.struct(
            {
                "merchantId": t.string(),
                "returnPolicyUri": t.string().optional(),
                "label": t.string().optional(),
                "policy": t.proxy(renames["ReturnPolicyOnlinePolicyIn"]).optional(),
                "name": t.string().optional(),
                "itemConditions": t.array(t.string()).optional(),
                "countries": t.array(t.string()).optional(),
                "returnReasonCategoryInfo": t.array(
                    t.proxy(renames["ReturnPolicyOnlineReturnReasonCategoryInfoIn"])
                ).optional(),
                "restockingFee": t.proxy(
                    renames["ReturnPolicyOnlineRestockingFeeIn"]
                ).optional(),
                "returnMethods": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReturnPolicyOnlineOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["returnpolicyonlineDelete"] = content.post(
        "{merchantId}/returnpolicyonline",
        t.struct(
            {
                "merchantId": t.string(),
                "returnPolicyUri": t.string().optional(),
                "label": t.string().optional(),
                "policy": t.proxy(renames["ReturnPolicyOnlinePolicyIn"]).optional(),
                "name": t.string().optional(),
                "itemConditions": t.array(t.string()).optional(),
                "countries": t.array(t.string()).optional(),
                "returnReasonCategoryInfo": t.array(
                    t.proxy(renames["ReturnPolicyOnlineReturnReasonCategoryInfoIn"])
                ).optional(),
                "restockingFee": t.proxy(
                    renames["ReturnPolicyOnlineRestockingFeeIn"]
                ).optional(),
                "returnMethods": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReturnPolicyOnlineOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["returnpolicyonlineList"] = content.post(
        "{merchantId}/returnpolicyonline",
        t.struct(
            {
                "merchantId": t.string(),
                "returnPolicyUri": t.string().optional(),
                "label": t.string().optional(),
                "policy": t.proxy(renames["ReturnPolicyOnlinePolicyIn"]).optional(),
                "name": t.string().optional(),
                "itemConditions": t.array(t.string()).optional(),
                "countries": t.array(t.string()).optional(),
                "returnReasonCategoryInfo": t.array(
                    t.proxy(renames["ReturnPolicyOnlineReturnReasonCategoryInfoIn"])
                ).optional(),
                "restockingFee": t.proxy(
                    renames["ReturnPolicyOnlineRestockingFeeIn"]
                ).optional(),
                "returnMethods": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReturnPolicyOnlineOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["returnpolicyonlineCreate"] = content.post(
        "{merchantId}/returnpolicyonline",
        t.struct(
            {
                "merchantId": t.string(),
                "returnPolicyUri": t.string().optional(),
                "label": t.string().optional(),
                "policy": t.proxy(renames["ReturnPolicyOnlinePolicyIn"]).optional(),
                "name": t.string().optional(),
                "itemConditions": t.array(t.string()).optional(),
                "countries": t.array(t.string()).optional(),
                "returnReasonCategoryInfo": t.array(
                    t.proxy(renames["ReturnPolicyOnlineReturnReasonCategoryInfoIn"])
                ).optional(),
                "restockingFee": t.proxy(
                    renames["ReturnPolicyOnlineRestockingFeeIn"]
                ).optional(),
                "returnMethods": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReturnPolicyOnlineOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accounttaxCustombatch"] = content.get(
        "{merchantId}/accounttax",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "merchantId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccounttaxListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accounttaxUpdate"] = content.get(
        "{merchantId}/accounttax",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "merchantId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccounttaxListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accounttaxGet"] = content.get(
        "{merchantId}/accounttax",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "merchantId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccounttaxListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accounttaxList"] = content.get(
        "{merchantId}/accounttax",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "merchantId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccounttaxListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["localinventoryCustombatch"] = content.post(
        "{merchantId}/products/{productId}/localinventory",
        t.struct(
            {
                "productId": t.string().optional(),
                "merchantId": t.string().optional(),
                "salePriceEffectiveDate": t.string().optional(),
                "instoreProductLocation": t.string().optional(),
                "availability": t.string().optional(),
                "kind": t.string().optional(),
                "pickupSla": t.string().optional(),
                "pickupMethod": t.string().optional(),
                "quantity": t.integer().optional(),
                "price": t.proxy(renames["PriceIn"]).optional(),
                "salePrice": t.proxy(renames["PriceIn"]).optional(),
                "storeCode": t.string(),
                "customAttributes": t.array(
                    t.proxy(renames["CustomAttributeIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LocalInventoryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["localinventoryInsert"] = content.post(
        "{merchantId}/products/{productId}/localinventory",
        t.struct(
            {
                "productId": t.string().optional(),
                "merchantId": t.string().optional(),
                "salePriceEffectiveDate": t.string().optional(),
                "instoreProductLocation": t.string().optional(),
                "availability": t.string().optional(),
                "kind": t.string().optional(),
                "pickupSla": t.string().optional(),
                "pickupMethod": t.string().optional(),
                "quantity": t.integer().optional(),
                "price": t.proxy(renames["PriceIn"]).optional(),
                "salePrice": t.proxy(renames["PriceIn"]).optional(),
                "storeCode": t.string(),
                "customAttributes": t.array(
                    t.proxy(renames["CustomAttributeIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LocalInventoryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersCreate"] = content.post(
        "{merchantId}/customers",
        t.struct(
            {
                "merchantId": t.string(),
                "emailAddress": t.string().optional(),
                "loyaltyData": t.proxy(renames["CustomerLoyaltyDataIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["ordertrackingsignalsCreate"] = content.post(
        "{merchantId}/ordertrackingsignals",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "deliveryPostalCode": t.string(),
                "shippingInfo": t.array(
                    t.proxy(renames["OrderTrackingSignalShippingInfoIn"])
                ).optional(),
                "customerShippingFee": t.proxy(renames["PriceAmountIn"]).optional(),
                "shipmentLineItemMapping": t.array(
                    t.proxy(renames["OrderTrackingSignalShipmentLineItemMappingIn"])
                ).optional(),
                "orderCreatedTime": t.proxy(renames["DateTimeIn"]),
                "lineItems": t.array(
                    t.proxy(renames["OrderTrackingSignalLineItemDetailsIn"])
                ).optional(),
                "deliveryRegionCode": t.string(),
                "orderId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrderTrackingSignalOut"]),
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
    functions["accountsVerifyphonenumber"] = content.post(
        "{merchantId}/accounts",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "conversionSettings": t.proxy(
                    renames["AccountConversionSettingsIn"]
                ).optional(),
                "labelIds": t.array(t.string()).optional(),
                "id": t.string(),
                "kind": t.string().optional(),
                "cssId": t.string().optional(),
                "youtubeChannelLinks": t.array(
                    t.proxy(renames["AccountYouTubeChannelLinkIn"])
                ).optional(),
                "googleMyBusinessLink": t.proxy(
                    renames["AccountGoogleMyBusinessLinkIn"]
                ).optional(),
                "sellerId": t.string().optional(),
                "adultContent": t.boolean().optional(),
                "adsLinks": t.array(t.proxy(renames["AccountAdsLinkIn"])).optional(),
                "users": t.array(t.proxy(renames["AccountUserIn"])).optional(),
                "name": t.string(),
                "businessInformation": t.proxy(
                    renames["AccountBusinessInformationIn"]
                ).optional(),
                "automaticImprovements": t.proxy(
                    renames["AccountAutomaticImprovementsIn"]
                ).optional(),
                "websiteUrl": t.string().optional(),
                "automaticLabelIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsList"] = content.post(
        "{merchantId}/accounts",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "conversionSettings": t.proxy(
                    renames["AccountConversionSettingsIn"]
                ).optional(),
                "labelIds": t.array(t.string()).optional(),
                "id": t.string(),
                "kind": t.string().optional(),
                "cssId": t.string().optional(),
                "youtubeChannelLinks": t.array(
                    t.proxy(renames["AccountYouTubeChannelLinkIn"])
                ).optional(),
                "googleMyBusinessLink": t.proxy(
                    renames["AccountGoogleMyBusinessLinkIn"]
                ).optional(),
                "sellerId": t.string().optional(),
                "adultContent": t.boolean().optional(),
                "adsLinks": t.array(t.proxy(renames["AccountAdsLinkIn"])).optional(),
                "users": t.array(t.proxy(renames["AccountUserIn"])).optional(),
                "name": t.string(),
                "businessInformation": t.proxy(
                    renames["AccountBusinessInformationIn"]
                ).optional(),
                "automaticImprovements": t.proxy(
                    renames["AccountAutomaticImprovementsIn"]
                ).optional(),
                "websiteUrl": t.string().optional(),
                "automaticLabelIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsUpdate"] = content.post(
        "{merchantId}/accounts",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "conversionSettings": t.proxy(
                    renames["AccountConversionSettingsIn"]
                ).optional(),
                "labelIds": t.array(t.string()).optional(),
                "id": t.string(),
                "kind": t.string().optional(),
                "cssId": t.string().optional(),
                "youtubeChannelLinks": t.array(
                    t.proxy(renames["AccountYouTubeChannelLinkIn"])
                ).optional(),
                "googleMyBusinessLink": t.proxy(
                    renames["AccountGoogleMyBusinessLinkIn"]
                ).optional(),
                "sellerId": t.string().optional(),
                "adultContent": t.boolean().optional(),
                "adsLinks": t.array(t.proxy(renames["AccountAdsLinkIn"])).optional(),
                "users": t.array(t.proxy(renames["AccountUserIn"])).optional(),
                "name": t.string(),
                "businessInformation": t.proxy(
                    renames["AccountBusinessInformationIn"]
                ).optional(),
                "automaticImprovements": t.proxy(
                    renames["AccountAutomaticImprovementsIn"]
                ).optional(),
                "websiteUrl": t.string().optional(),
                "automaticLabelIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsListlinks"] = content.post(
        "{merchantId}/accounts",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "conversionSettings": t.proxy(
                    renames["AccountConversionSettingsIn"]
                ).optional(),
                "labelIds": t.array(t.string()).optional(),
                "id": t.string(),
                "kind": t.string().optional(),
                "cssId": t.string().optional(),
                "youtubeChannelLinks": t.array(
                    t.proxy(renames["AccountYouTubeChannelLinkIn"])
                ).optional(),
                "googleMyBusinessLink": t.proxy(
                    renames["AccountGoogleMyBusinessLinkIn"]
                ).optional(),
                "sellerId": t.string().optional(),
                "adultContent": t.boolean().optional(),
                "adsLinks": t.array(t.proxy(renames["AccountAdsLinkIn"])).optional(),
                "users": t.array(t.proxy(renames["AccountUserIn"])).optional(),
                "name": t.string(),
                "businessInformation": t.proxy(
                    renames["AccountBusinessInformationIn"]
                ).optional(),
                "automaticImprovements": t.proxy(
                    renames["AccountAutomaticImprovementsIn"]
                ).optional(),
                "websiteUrl": t.string().optional(),
                "automaticLabelIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsGet"] = content.post(
        "{merchantId}/accounts",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "conversionSettings": t.proxy(
                    renames["AccountConversionSettingsIn"]
                ).optional(),
                "labelIds": t.array(t.string()).optional(),
                "id": t.string(),
                "kind": t.string().optional(),
                "cssId": t.string().optional(),
                "youtubeChannelLinks": t.array(
                    t.proxy(renames["AccountYouTubeChannelLinkIn"])
                ).optional(),
                "googleMyBusinessLink": t.proxy(
                    renames["AccountGoogleMyBusinessLinkIn"]
                ).optional(),
                "sellerId": t.string().optional(),
                "adultContent": t.boolean().optional(),
                "adsLinks": t.array(t.proxy(renames["AccountAdsLinkIn"])).optional(),
                "users": t.array(t.proxy(renames["AccountUserIn"])).optional(),
                "name": t.string(),
                "businessInformation": t.proxy(
                    renames["AccountBusinessInformationIn"]
                ).optional(),
                "automaticImprovements": t.proxy(
                    renames["AccountAutomaticImprovementsIn"]
                ).optional(),
                "websiteUrl": t.string().optional(),
                "automaticLabelIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAuthinfo"] = content.post(
        "{merchantId}/accounts",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "conversionSettings": t.proxy(
                    renames["AccountConversionSettingsIn"]
                ).optional(),
                "labelIds": t.array(t.string()).optional(),
                "id": t.string(),
                "kind": t.string().optional(),
                "cssId": t.string().optional(),
                "youtubeChannelLinks": t.array(
                    t.proxy(renames["AccountYouTubeChannelLinkIn"])
                ).optional(),
                "googleMyBusinessLink": t.proxy(
                    renames["AccountGoogleMyBusinessLinkIn"]
                ).optional(),
                "sellerId": t.string().optional(),
                "adultContent": t.boolean().optional(),
                "adsLinks": t.array(t.proxy(renames["AccountAdsLinkIn"])).optional(),
                "users": t.array(t.proxy(renames["AccountUserIn"])).optional(),
                "name": t.string(),
                "businessInformation": t.proxy(
                    renames["AccountBusinessInformationIn"]
                ).optional(),
                "automaticImprovements": t.proxy(
                    renames["AccountAutomaticImprovementsIn"]
                ).optional(),
                "websiteUrl": t.string().optional(),
                "automaticLabelIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsDelete"] = content.post(
        "{merchantId}/accounts",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "conversionSettings": t.proxy(
                    renames["AccountConversionSettingsIn"]
                ).optional(),
                "labelIds": t.array(t.string()).optional(),
                "id": t.string(),
                "kind": t.string().optional(),
                "cssId": t.string().optional(),
                "youtubeChannelLinks": t.array(
                    t.proxy(renames["AccountYouTubeChannelLinkIn"])
                ).optional(),
                "googleMyBusinessLink": t.proxy(
                    renames["AccountGoogleMyBusinessLinkIn"]
                ).optional(),
                "sellerId": t.string().optional(),
                "adultContent": t.boolean().optional(),
                "adsLinks": t.array(t.proxy(renames["AccountAdsLinkIn"])).optional(),
                "users": t.array(t.proxy(renames["AccountUserIn"])).optional(),
                "name": t.string(),
                "businessInformation": t.proxy(
                    renames["AccountBusinessInformationIn"]
                ).optional(),
                "automaticImprovements": t.proxy(
                    renames["AccountAutomaticImprovementsIn"]
                ).optional(),
                "websiteUrl": t.string().optional(),
                "automaticLabelIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsLink"] = content.post(
        "{merchantId}/accounts",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "conversionSettings": t.proxy(
                    renames["AccountConversionSettingsIn"]
                ).optional(),
                "labelIds": t.array(t.string()).optional(),
                "id": t.string(),
                "kind": t.string().optional(),
                "cssId": t.string().optional(),
                "youtubeChannelLinks": t.array(
                    t.proxy(renames["AccountYouTubeChannelLinkIn"])
                ).optional(),
                "googleMyBusinessLink": t.proxy(
                    renames["AccountGoogleMyBusinessLinkIn"]
                ).optional(),
                "sellerId": t.string().optional(),
                "adultContent": t.boolean().optional(),
                "adsLinks": t.array(t.proxy(renames["AccountAdsLinkIn"])).optional(),
                "users": t.array(t.proxy(renames["AccountUserIn"])).optional(),
                "name": t.string(),
                "businessInformation": t.proxy(
                    renames["AccountBusinessInformationIn"]
                ).optional(),
                "automaticImprovements": t.proxy(
                    renames["AccountAutomaticImprovementsIn"]
                ).optional(),
                "websiteUrl": t.string().optional(),
                "automaticLabelIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsClaimwebsite"] = content.post(
        "{merchantId}/accounts",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "conversionSettings": t.proxy(
                    renames["AccountConversionSettingsIn"]
                ).optional(),
                "labelIds": t.array(t.string()).optional(),
                "id": t.string(),
                "kind": t.string().optional(),
                "cssId": t.string().optional(),
                "youtubeChannelLinks": t.array(
                    t.proxy(renames["AccountYouTubeChannelLinkIn"])
                ).optional(),
                "googleMyBusinessLink": t.proxy(
                    renames["AccountGoogleMyBusinessLinkIn"]
                ).optional(),
                "sellerId": t.string().optional(),
                "adultContent": t.boolean().optional(),
                "adsLinks": t.array(t.proxy(renames["AccountAdsLinkIn"])).optional(),
                "users": t.array(t.proxy(renames["AccountUserIn"])).optional(),
                "name": t.string(),
                "businessInformation": t.proxy(
                    renames["AccountBusinessInformationIn"]
                ).optional(),
                "automaticImprovements": t.proxy(
                    renames["AccountAutomaticImprovementsIn"]
                ).optional(),
                "websiteUrl": t.string().optional(),
                "automaticLabelIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsRequestphoneverification"] = content.post(
        "{merchantId}/accounts",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "conversionSettings": t.proxy(
                    renames["AccountConversionSettingsIn"]
                ).optional(),
                "labelIds": t.array(t.string()).optional(),
                "id": t.string(),
                "kind": t.string().optional(),
                "cssId": t.string().optional(),
                "youtubeChannelLinks": t.array(
                    t.proxy(renames["AccountYouTubeChannelLinkIn"])
                ).optional(),
                "googleMyBusinessLink": t.proxy(
                    renames["AccountGoogleMyBusinessLinkIn"]
                ).optional(),
                "sellerId": t.string().optional(),
                "adultContent": t.boolean().optional(),
                "adsLinks": t.array(t.proxy(renames["AccountAdsLinkIn"])).optional(),
                "users": t.array(t.proxy(renames["AccountUserIn"])).optional(),
                "name": t.string(),
                "businessInformation": t.proxy(
                    renames["AccountBusinessInformationIn"]
                ).optional(),
                "automaticImprovements": t.proxy(
                    renames["AccountAutomaticImprovementsIn"]
                ).optional(),
                "websiteUrl": t.string().optional(),
                "automaticLabelIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCustombatch"] = content.post(
        "{merchantId}/accounts",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "conversionSettings": t.proxy(
                    renames["AccountConversionSettingsIn"]
                ).optional(),
                "labelIds": t.array(t.string()).optional(),
                "id": t.string(),
                "kind": t.string().optional(),
                "cssId": t.string().optional(),
                "youtubeChannelLinks": t.array(
                    t.proxy(renames["AccountYouTubeChannelLinkIn"])
                ).optional(),
                "googleMyBusinessLink": t.proxy(
                    renames["AccountGoogleMyBusinessLinkIn"]
                ).optional(),
                "sellerId": t.string().optional(),
                "adultContent": t.boolean().optional(),
                "adsLinks": t.array(t.proxy(renames["AccountAdsLinkIn"])).optional(),
                "users": t.array(t.proxy(renames["AccountUserIn"])).optional(),
                "name": t.string(),
                "businessInformation": t.proxy(
                    renames["AccountBusinessInformationIn"]
                ).optional(),
                "automaticImprovements": t.proxy(
                    renames["AccountAutomaticImprovementsIn"]
                ).optional(),
                "websiteUrl": t.string().optional(),
                "automaticLabelIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsUpdatelabels"] = content.post(
        "{merchantId}/accounts",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "conversionSettings": t.proxy(
                    renames["AccountConversionSettingsIn"]
                ).optional(),
                "labelIds": t.array(t.string()).optional(),
                "id": t.string(),
                "kind": t.string().optional(),
                "cssId": t.string().optional(),
                "youtubeChannelLinks": t.array(
                    t.proxy(renames["AccountYouTubeChannelLinkIn"])
                ).optional(),
                "googleMyBusinessLink": t.proxy(
                    renames["AccountGoogleMyBusinessLinkIn"]
                ).optional(),
                "sellerId": t.string().optional(),
                "adultContent": t.boolean().optional(),
                "adsLinks": t.array(t.proxy(renames["AccountAdsLinkIn"])).optional(),
                "users": t.array(t.proxy(renames["AccountUserIn"])).optional(),
                "name": t.string(),
                "businessInformation": t.proxy(
                    renames["AccountBusinessInformationIn"]
                ).optional(),
                "automaticImprovements": t.proxy(
                    renames["AccountAutomaticImprovementsIn"]
                ).optional(),
                "websiteUrl": t.string().optional(),
                "automaticLabelIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsInsert"] = content.post(
        "{merchantId}/accounts",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "conversionSettings": t.proxy(
                    renames["AccountConversionSettingsIn"]
                ).optional(),
                "labelIds": t.array(t.string()).optional(),
                "id": t.string(),
                "kind": t.string().optional(),
                "cssId": t.string().optional(),
                "youtubeChannelLinks": t.array(
                    t.proxy(renames["AccountYouTubeChannelLinkIn"])
                ).optional(),
                "googleMyBusinessLink": t.proxy(
                    renames["AccountGoogleMyBusinessLinkIn"]
                ).optional(),
                "sellerId": t.string().optional(),
                "adultContent": t.boolean().optional(),
                "adsLinks": t.array(t.proxy(renames["AccountAdsLinkIn"])).optional(),
                "users": t.array(t.proxy(renames["AccountUserIn"])).optional(),
                "name": t.string(),
                "businessInformation": t.proxy(
                    renames["AccountBusinessInformationIn"]
                ).optional(),
                "automaticImprovements": t.proxy(
                    renames["AccountAutomaticImprovementsIn"]
                ).optional(),
                "websiteUrl": t.string().optional(),
                "automaticLabelIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsReturncarrierCreate"] = content.patch(
        "accounts/{accountId}/returncarrier/{carrierAccountId}",
        t.struct(
            {
                "carrierAccountId": t.string(),
                "accountId": t.string(),
                "carrierCode": t.string().optional(),
                "carrierAccountNumber": t.string().optional(),
                "carrierAccountName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountReturnCarrierOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsReturncarrierList"] = content.patch(
        "accounts/{accountId}/returncarrier/{carrierAccountId}",
        t.struct(
            {
                "carrierAccountId": t.string(),
                "accountId": t.string(),
                "carrierCode": t.string().optional(),
                "carrierAccountNumber": t.string().optional(),
                "carrierAccountName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountReturnCarrierOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsReturncarrierDelete"] = content.patch(
        "accounts/{accountId}/returncarrier/{carrierAccountId}",
        t.struct(
            {
                "carrierAccountId": t.string(),
                "accountId": t.string(),
                "carrierCode": t.string().optional(),
                "carrierAccountNumber": t.string().optional(),
                "carrierAccountName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountReturnCarrierOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsReturncarrierPatch"] = content.patch(
        "accounts/{accountId}/returncarrier/{carrierAccountId}",
        t.struct(
            {
                "carrierAccountId": t.string(),
                "accountId": t.string(),
                "carrierCode": t.string().optional(),
                "carrierAccountNumber": t.string().optional(),
                "carrierAccountName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountReturnCarrierOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCredentialsCreate"] = content.post(
        "accounts/{accountId}/credentials",
        t.struct(
            {
                "accountId": t.string(),
                "accessToken": t.string().optional(),
                "purpose": t.string().optional(),
                "expiresIn": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountCredentialsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsLabelsPatch"] = content.get(
        "accounts/{accountId}/labels",
        t.struct(
            {
                "accountId": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAccountLabelsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsLabelsDelete"] = content.get(
        "accounts/{accountId}/labels",
        t.struct(
            {
                "accountId": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAccountLabelsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsLabelsCreate"] = content.get(
        "accounts/{accountId}/labels",
        t.struct(
            {
                "accountId": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAccountLabelsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsLabelsList"] = content.get(
        "accounts/{accountId}/labels",
        t.struct(
            {
                "accountId": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAccountLabelsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["collectionsDelete"] = content.get(
        "{merchantId}/collections/{collectionId}",
        t.struct(
            {
                "merchantId": t.string(),
                "collectionId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CollectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["collectionsCreate"] = content.get(
        "{merchantId}/collections/{collectionId}",
        t.struct(
            {
                "merchantId": t.string(),
                "collectionId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CollectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["collectionsList"] = content.get(
        "{merchantId}/collections/{collectionId}",
        t.struct(
            {
                "merchantId": t.string(),
                "collectionId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CollectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["collectionsGet"] = content.get(
        "{merchantId}/collections/{collectionId}",
        t.struct(
            {
                "merchantId": t.string(),
                "collectionId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CollectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["orderinvoicesCreatechargeinvoice"] = content.post(
        "{merchantId}/orderinvoices/{orderId}/createRefundInvoice",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "orderId": t.string().optional(),
                "invoiceId": t.string().optional(),
                "refundOnlyOption": t.proxy(
                    renames[
                        "OrderinvoicesCustomBatchRequestEntryCreateRefundInvoiceRefundOptionIn"
                    ]
                ).optional(),
                "shipmentInvoices": t.array(
                    t.proxy(renames["ShipmentInvoiceIn"])
                ).optional(),
                "returnOption": t.proxy(
                    renames[
                        "OrderinvoicesCustomBatchRequestEntryCreateRefundInvoiceReturnOptionIn"
                    ]
                ).optional(),
                "operationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrderinvoicesCreateRefundInvoiceResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["orderinvoicesCreaterefundinvoice"] = content.post(
        "{merchantId}/orderinvoices/{orderId}/createRefundInvoice",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "orderId": t.string().optional(),
                "invoiceId": t.string().optional(),
                "refundOnlyOption": t.proxy(
                    renames[
                        "OrderinvoicesCustomBatchRequestEntryCreateRefundInvoiceRefundOptionIn"
                    ]
                ).optional(),
                "shipmentInvoices": t.array(
                    t.proxy(renames["ShipmentInvoiceIn"])
                ).optional(),
                "returnOption": t.proxy(
                    renames[
                        "OrderinvoicesCustomBatchRequestEntryCreateRefundInvoiceReturnOptionIn"
                    ]
                ).optional(),
                "operationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrderinvoicesCreateRefundInvoiceResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["cssesUpdatelabels"] = content.get(
        "{cssGroupId}/csses",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "cssGroupId": t.string(),
                "pageToken": t.string().optional(),
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
                "cssGroupId": t.string(),
                "pageToken": t.string().optional(),
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
                "cssGroupId": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCssesResponseOut"]),
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
                "maxResults": t.integer().optional(),
                "merchantId": t.string().optional(),
                "pageToken": t.string().optional(),
                "transferStartDate": t.string().optional(),
                "transferEndDate": t.string().optional(),
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
                "maxResults": t.integer().optional(),
                "merchantId": t.string().optional(),
                "pageToken": t.string().optional(),
                "transferStartDate": t.string().optional(),
                "transferEndDate": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SettlementreportsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liasettingsRequestgmbaccess"] = content.get(
        "liasettings/posdataproviders",
        t.struct({"auth": t.string().optional()}),
        t.proxy(renames["LiasettingsListPosDataProvidersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liasettingsList"] = content.get(
        "liasettings/posdataproviders",
        t.struct({"auth": t.string().optional()}),
        t.proxy(renames["LiasettingsListPosDataProvidersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liasettingsCustombatch"] = content.get(
        "liasettings/posdataproviders",
        t.struct({"auth": t.string().optional()}),
        t.proxy(renames["LiasettingsListPosDataProvidersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liasettingsGet"] = content.get(
        "liasettings/posdataproviders",
        t.struct({"auth": t.string().optional()}),
        t.proxy(renames["LiasettingsListPosDataProvidersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liasettingsUpdate"] = content.get(
        "liasettings/posdataproviders",
        t.struct({"auth": t.string().optional()}),
        t.proxy(renames["LiasettingsListPosDataProvidersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liasettingsRequestinventoryverification"] = content.get(
        "liasettings/posdataproviders",
        t.struct({"auth": t.string().optional()}),
        t.proxy(renames["LiasettingsListPosDataProvidersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liasettingsSetinventoryverificationcontact"] = content.get(
        "liasettings/posdataproviders",
        t.struct({"auth": t.string().optional()}),
        t.proxy(renames["LiasettingsListPosDataProvidersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liasettingsGetaccessiblegmbaccounts"] = content.get(
        "liasettings/posdataproviders",
        t.struct({"auth": t.string().optional()}),
        t.proxy(renames["LiasettingsListPosDataProvidersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liasettingsSetposdataprovider"] = content.get(
        "liasettings/posdataproviders",
        t.struct({"auth": t.string().optional()}),
        t.proxy(renames["LiasettingsListPosDataProvidersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liasettingsListposdataproviders"] = content.get(
        "liasettings/posdataproviders",
        t.struct({"auth": t.string().optional()}),
        t.proxy(renames["LiasettingsListPosDataProvidersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["conversionsourcesUndelete"] = content.post(
        "{merchantId}/conversionsources",
        t.struct(
            {
                "merchantId": t.string(),
                "googleAnalyticsLink": t.proxy(
                    renames["GoogleAnalyticsLinkIn"]
                ).optional(),
                "merchantCenterDestination": t.proxy(
                    renames["MerchantCenterDestinationIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConversionSourceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["conversionsourcesList"] = content.post(
        "{merchantId}/conversionsources",
        t.struct(
            {
                "merchantId": t.string(),
                "googleAnalyticsLink": t.proxy(
                    renames["GoogleAnalyticsLinkIn"]
                ).optional(),
                "merchantCenterDestination": t.proxy(
                    renames["MerchantCenterDestinationIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConversionSourceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["conversionsourcesDelete"] = content.post(
        "{merchantId}/conversionsources",
        t.struct(
            {
                "merchantId": t.string(),
                "googleAnalyticsLink": t.proxy(
                    renames["GoogleAnalyticsLinkIn"]
                ).optional(),
                "merchantCenterDestination": t.proxy(
                    renames["MerchantCenterDestinationIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConversionSourceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["conversionsourcesGet"] = content.post(
        "{merchantId}/conversionsources",
        t.struct(
            {
                "merchantId": t.string(),
                "googleAnalyticsLink": t.proxy(
                    renames["GoogleAnalyticsLinkIn"]
                ).optional(),
                "merchantCenterDestination": t.proxy(
                    renames["MerchantCenterDestinationIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConversionSourceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["conversionsourcesPatch"] = content.post(
        "{merchantId}/conversionsources",
        t.struct(
            {
                "merchantId": t.string(),
                "googleAnalyticsLink": t.proxy(
                    renames["GoogleAnalyticsLinkIn"]
                ).optional(),
                "merchantCenterDestination": t.proxy(
                    renames["MerchantCenterDestinationIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConversionSourceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["conversionsourcesCreate"] = content.post(
        "{merchantId}/conversionsources",
        t.struct(
            {
                "merchantId": t.string(),
                "googleAnalyticsLink": t.proxy(
                    renames["GoogleAnalyticsLinkIn"]
                ).optional(),
                "merchantCenterDestination": t.proxy(
                    renames["MerchantCenterDestinationIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConversionSourceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settlementtransactionsList"] = content.get(
        "{merchantId}/settlementreports/{settlementId}/transactions",
        t.struct(
            {
                "settlementId": t.string().optional(),
                "merchantId": t.string().optional(),
                "transactionIds": t.string().optional(),
                "pageToken": t.string().optional(),
                "maxResults": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SettlementtransactionsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["recommendationsGenerate"] = content.post(
        "{merchantId}/recommendations/reportInteraction",
        t.struct(
            {
                "merchantId": t.string(),
                "interactionType": t.string(),
                "type": t.string(),
                "subtype": t.string().optional(),
                "responseToken": t.string(),
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
                "interactionType": t.string(),
                "type": t.string(),
                "subtype": t.string().optional(),
                "responseToken": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["promotionsGet"] = content.post(
        "{merchantId}/promotions",
        t.struct(
            {
                "merchantId": t.string(),
                "couponValueType": t.string(),
                "limitValue": t.proxy(renames["PriceAmountIn"]).optional(),
                "promotionDisplayDates": t.string().optional(),
                "moneyOffAmount": t.proxy(renames["PriceAmountIn"]).optional(),
                "freeGiftItemId": t.string().optional(),
                "freeGiftValue": t.proxy(renames["PriceAmountIn"]).optional(),
                "productType": t.array(t.string()).optional(),
                "promotionEffectiveTimePeriod": t.proxy(renames["TimePeriodIn"]),
                "productApplicability": t.string(),
                "redemptionChannel": t.array(t.string()),
                "itemGroupId": t.array(t.string()).optional(),
                "percentOff": t.integer().optional(),
                "itemGroupIdExclusion": t.array(t.string()).optional(),
                "limitQuantity": t.integer().optional(),
                "storeApplicability": t.string().optional(),
                "promotionEffectiveDates": t.string().optional(),
                "minimumPurchaseQuantity": t.integer().optional(),
                "contentLanguage": t.string(),
                "productTypeExclusion": t.array(t.string()).optional(),
                "shippingServiceNames": t.array(t.string()).optional(),
                "genericRedemptionCode": t.string().optional(),
                "brand": t.array(t.string()).optional(),
                "brandExclusion": t.array(t.string()).optional(),
                "freeGiftDescription": t.string().optional(),
                "itemId": t.array(t.string()).optional(),
                "longTitle": t.string(),
                "promotionId": t.string(),
                "minimumPurchaseAmount": t.proxy(renames["PriceAmountIn"]).optional(),
                "itemIdExclusion": t.array(t.string()).optional(),
                "getThisQuantityDiscounted": t.integer().optional(),
                "promotionUrl": t.string().optional(),
                "offerType": t.string(),
                "promotionDestinationIds": t.array(t.string()).optional(),
                "targetCountry": t.string(),
                "moneyBudget": t.proxy(renames["PriceAmountIn"]).optional(),
                "storeCodeExclusion": t.array(t.string()).optional(),
                "orderLimit": t.integer().optional(),
                "promotionDisplayTimePeriod": t.proxy(
                    renames["TimePeriodIn"]
                ).optional(),
                "storeCode": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PromotionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["promotionsCreate"] = content.post(
        "{merchantId}/promotions",
        t.struct(
            {
                "merchantId": t.string(),
                "couponValueType": t.string(),
                "limitValue": t.proxy(renames["PriceAmountIn"]).optional(),
                "promotionDisplayDates": t.string().optional(),
                "moneyOffAmount": t.proxy(renames["PriceAmountIn"]).optional(),
                "freeGiftItemId": t.string().optional(),
                "freeGiftValue": t.proxy(renames["PriceAmountIn"]).optional(),
                "productType": t.array(t.string()).optional(),
                "promotionEffectiveTimePeriod": t.proxy(renames["TimePeriodIn"]),
                "productApplicability": t.string(),
                "redemptionChannel": t.array(t.string()),
                "itemGroupId": t.array(t.string()).optional(),
                "percentOff": t.integer().optional(),
                "itemGroupIdExclusion": t.array(t.string()).optional(),
                "limitQuantity": t.integer().optional(),
                "storeApplicability": t.string().optional(),
                "promotionEffectiveDates": t.string().optional(),
                "minimumPurchaseQuantity": t.integer().optional(),
                "contentLanguage": t.string(),
                "productTypeExclusion": t.array(t.string()).optional(),
                "shippingServiceNames": t.array(t.string()).optional(),
                "genericRedemptionCode": t.string().optional(),
                "brand": t.array(t.string()).optional(),
                "brandExclusion": t.array(t.string()).optional(),
                "freeGiftDescription": t.string().optional(),
                "itemId": t.array(t.string()).optional(),
                "longTitle": t.string(),
                "promotionId": t.string(),
                "minimumPurchaseAmount": t.proxy(renames["PriceAmountIn"]).optional(),
                "itemIdExclusion": t.array(t.string()).optional(),
                "getThisQuantityDiscounted": t.integer().optional(),
                "promotionUrl": t.string().optional(),
                "offerType": t.string(),
                "promotionDestinationIds": t.array(t.string()).optional(),
                "targetCountry": t.string(),
                "moneyBudget": t.proxy(renames["PriceAmountIn"]).optional(),
                "storeCodeExclusion": t.array(t.string()).optional(),
                "orderLimit": t.integer().optional(),
                "promotionDisplayTimePeriod": t.proxy(
                    renames["TimePeriodIn"]
                ).optional(),
                "storeCode": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PromotionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["productdeliverytimeGet"] = content.post(
        "{merchantId}/productdeliverytime",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "areaDeliveryTimes": t.array(
                    t.proxy(renames["ProductDeliveryTimeAreaDeliveryTimeIn"])
                ),
                "productId": t.proxy(renames["ProductIdIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductDeliveryTimeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["productdeliverytimeDelete"] = content.post(
        "{merchantId}/productdeliverytime",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "areaDeliveryTimes": t.array(
                    t.proxy(renames["ProductDeliveryTimeAreaDeliveryTimeIn"])
                ),
                "productId": t.proxy(renames["ProductIdIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductDeliveryTimeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["productdeliverytimeCreate"] = content.post(
        "{merchantId}/productdeliverytime",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "areaDeliveryTimes": t.array(
                    t.proxy(renames["ProductDeliveryTimeAreaDeliveryTimeIn"])
                ),
                "productId": t.proxy(renames["ProductIdIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductDeliveryTimeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["productsList"] = content.delete(
        "{merchantId}/products/{productId}",
        t.struct(
            {
                "productId": t.string().optional(),
                "feedId": t.string().optional(),
                "merchantId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["productsGet"] = content.delete(
        "{merchantId}/products/{productId}",
        t.struct(
            {
                "productId": t.string().optional(),
                "feedId": t.string().optional(),
                "merchantId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["productsInsert"] = content.delete(
        "{merchantId}/products/{productId}",
        t.struct(
            {
                "productId": t.string().optional(),
                "feedId": t.string().optional(),
                "merchantId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["productsUpdate"] = content.delete(
        "{merchantId}/products/{productId}",
        t.struct(
            {
                "productId": t.string().optional(),
                "feedId": t.string().optional(),
                "merchantId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["productsCustombatch"] = content.delete(
        "{merchantId}/products/{productId}",
        t.struct(
            {
                "productId": t.string().optional(),
                "feedId": t.string().optional(),
                "merchantId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["productsDelete"] = content.delete(
        "{merchantId}/products/{productId}",
        t.struct(
            {
                "productId": t.string().optional(),
                "feedId": t.string().optional(),
                "merchantId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["posCustombatch"] = content.get(
        "{merchantId}/pos/{targetMerchantId}/store/{storeCode}",
        t.struct(
            {
                "targetMerchantId": t.string().optional(),
                "storeCode": t.string().optional(),
                "merchantId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PosStoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["posSale"] = content.get(
        "{merchantId}/pos/{targetMerchantId}/store/{storeCode}",
        t.struct(
            {
                "targetMerchantId": t.string().optional(),
                "storeCode": t.string().optional(),
                "merchantId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PosStoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["posList"] = content.get(
        "{merchantId}/pos/{targetMerchantId}/store/{storeCode}",
        t.struct(
            {
                "targetMerchantId": t.string().optional(),
                "storeCode": t.string().optional(),
                "merchantId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PosStoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["posInventory"] = content.get(
        "{merchantId}/pos/{targetMerchantId}/store/{storeCode}",
        t.struct(
            {
                "targetMerchantId": t.string().optional(),
                "storeCode": t.string().optional(),
                "merchantId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PosStoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["posDelete"] = content.get(
        "{merchantId}/pos/{targetMerchantId}/store/{storeCode}",
        t.struct(
            {
                "targetMerchantId": t.string().optional(),
                "storeCode": t.string().optional(),
                "merchantId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PosStoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["posInsert"] = content.get(
        "{merchantId}/pos/{targetMerchantId}/store/{storeCode}",
        t.struct(
            {
                "targetMerchantId": t.string().optional(),
                "storeCode": t.string().optional(),
                "merchantId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PosStoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["posGet"] = content.get(
        "{merchantId}/pos/{targetMerchantId}/store/{storeCode}",
        t.struct(
            {
                "targetMerchantId": t.string().optional(),
                "storeCode": t.string().optional(),
                "merchantId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PosStoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyongoogleprogramsPause"] = content.get(
        "{merchantId}/buyongoogleprograms/{regionCode}",
        t.struct(
            {
                "merchantId": t.string(),
                "regionCode": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BuyOnGoogleProgramStatusOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyongoogleprogramsActivate"] = content.get(
        "{merchantId}/buyongoogleprograms/{regionCode}",
        t.struct(
            {
                "merchantId": t.string(),
                "regionCode": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BuyOnGoogleProgramStatusOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyongoogleprogramsOnboard"] = content.get(
        "{merchantId}/buyongoogleprograms/{regionCode}",
        t.struct(
            {
                "merchantId": t.string(),
                "regionCode": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BuyOnGoogleProgramStatusOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyongoogleprogramsRequestreview"] = content.get(
        "{merchantId}/buyongoogleprograms/{regionCode}",
        t.struct(
            {
                "merchantId": t.string(),
                "regionCode": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BuyOnGoogleProgramStatusOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyongoogleprogramsPatch"] = content.get(
        "{merchantId}/buyongoogleprograms/{regionCode}",
        t.struct(
            {
                "merchantId": t.string(),
                "regionCode": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BuyOnGoogleProgramStatusOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyongoogleprogramsGet"] = content.get(
        "{merchantId}/buyongoogleprograms/{regionCode}",
        t.struct(
            {
                "merchantId": t.string(),
                "regionCode": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BuyOnGoogleProgramStatusOut"]),
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
    functions["repricingrulesDelete"] = content.patch(
        "{merchantId}/repricingrules/{ruleId}",
        t.struct(
            {
                "ruleId": t.string(),
                "merchantId": t.string(),
                "cogsBasedRule": t.proxy(
                    renames["RepricingRuleCostOfGoodsSaleRuleIn"]
                ).optional(),
                "restriction": t.proxy(renames["RepricingRuleRestrictionIn"]),
                "title": t.string().optional(),
                "paused": t.boolean().optional(),
                "countryCode": t.string(),
                "languageCode": t.string(),
                "type": t.string(),
                "effectiveTimePeriod": t.proxy(renames["RepricingRuleEffectiveTimeIn"]),
                "statsBasedRule": t.proxy(
                    renames["RepricingRuleStatsBasedRuleIn"]
                ).optional(),
                "eligibleOfferMatcher": t.proxy(
                    renames["RepricingRuleEligibleOfferMatcherIn"]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RepricingRuleOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["repricingrulesCreate"] = content.patch(
        "{merchantId}/repricingrules/{ruleId}",
        t.struct(
            {
                "ruleId": t.string(),
                "merchantId": t.string(),
                "cogsBasedRule": t.proxy(
                    renames["RepricingRuleCostOfGoodsSaleRuleIn"]
                ).optional(),
                "restriction": t.proxy(renames["RepricingRuleRestrictionIn"]),
                "title": t.string().optional(),
                "paused": t.boolean().optional(),
                "countryCode": t.string(),
                "languageCode": t.string(),
                "type": t.string(),
                "effectiveTimePeriod": t.proxy(renames["RepricingRuleEffectiveTimeIn"]),
                "statsBasedRule": t.proxy(
                    renames["RepricingRuleStatsBasedRuleIn"]
                ).optional(),
                "eligibleOfferMatcher": t.proxy(
                    renames["RepricingRuleEligibleOfferMatcherIn"]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RepricingRuleOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["repricingrulesList"] = content.patch(
        "{merchantId}/repricingrules/{ruleId}",
        t.struct(
            {
                "ruleId": t.string(),
                "merchantId": t.string(),
                "cogsBasedRule": t.proxy(
                    renames["RepricingRuleCostOfGoodsSaleRuleIn"]
                ).optional(),
                "restriction": t.proxy(renames["RepricingRuleRestrictionIn"]),
                "title": t.string().optional(),
                "paused": t.boolean().optional(),
                "countryCode": t.string(),
                "languageCode": t.string(),
                "type": t.string(),
                "effectiveTimePeriod": t.proxy(renames["RepricingRuleEffectiveTimeIn"]),
                "statsBasedRule": t.proxy(
                    renames["RepricingRuleStatsBasedRuleIn"]
                ).optional(),
                "eligibleOfferMatcher": t.proxy(
                    renames["RepricingRuleEligibleOfferMatcherIn"]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RepricingRuleOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["repricingrulesGet"] = content.patch(
        "{merchantId}/repricingrules/{ruleId}",
        t.struct(
            {
                "ruleId": t.string(),
                "merchantId": t.string(),
                "cogsBasedRule": t.proxy(
                    renames["RepricingRuleCostOfGoodsSaleRuleIn"]
                ).optional(),
                "restriction": t.proxy(renames["RepricingRuleRestrictionIn"]),
                "title": t.string().optional(),
                "paused": t.boolean().optional(),
                "countryCode": t.string(),
                "languageCode": t.string(),
                "type": t.string(),
                "effectiveTimePeriod": t.proxy(renames["RepricingRuleEffectiveTimeIn"]),
                "statsBasedRule": t.proxy(
                    renames["RepricingRuleStatsBasedRuleIn"]
                ).optional(),
                "eligibleOfferMatcher": t.proxy(
                    renames["RepricingRuleEligibleOfferMatcherIn"]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RepricingRuleOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["repricingrulesPatch"] = content.patch(
        "{merchantId}/repricingrules/{ruleId}",
        t.struct(
            {
                "ruleId": t.string(),
                "merchantId": t.string(),
                "cogsBasedRule": t.proxy(
                    renames["RepricingRuleCostOfGoodsSaleRuleIn"]
                ).optional(),
                "restriction": t.proxy(renames["RepricingRuleRestrictionIn"]),
                "title": t.string().optional(),
                "paused": t.boolean().optional(),
                "countryCode": t.string(),
                "languageCode": t.string(),
                "type": t.string(),
                "effectiveTimePeriod": t.proxy(renames["RepricingRuleEffectiveTimeIn"]),
                "statsBasedRule": t.proxy(
                    renames["RepricingRuleStatsBasedRuleIn"]
                ).optional(),
                "eligibleOfferMatcher": t.proxy(
                    renames["RepricingRuleEligibleOfferMatcherIn"]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RepricingRuleOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["repricingrulesRepricingreportsList"] = content.get(
        "{merchantId}/repricingrules/{ruleId}/repricingreports",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "ruleId": t.string(),
                "endDate": t.string().optional(),
                "merchantId": t.string(),
                "startDate": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListRepricingRuleReportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["reportsSearch"] = content.post(
        "{merchantId}/reports/search",
        t.struct(
            {
                "merchantId": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "query": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["shippingsettingsGet"] = content.post(
        "shippingsettings/batch",
        t.struct(
            {
                "entries": t.array(
                    t.proxy(renames["ShippingsettingsCustomBatchRequestEntryIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ShippingsettingsCustomBatchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["shippingsettingsGetsupportedpickupservices"] = content.post(
        "shippingsettings/batch",
        t.struct(
            {
                "entries": t.array(
                    t.proxy(renames["ShippingsettingsCustomBatchRequestEntryIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ShippingsettingsCustomBatchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["shippingsettingsUpdate"] = content.post(
        "shippingsettings/batch",
        t.struct(
            {
                "entries": t.array(
                    t.proxy(renames["ShippingsettingsCustomBatchRequestEntryIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ShippingsettingsCustomBatchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["shippingsettingsList"] = content.post(
        "shippingsettings/batch",
        t.struct(
            {
                "entries": t.array(
                    t.proxy(renames["ShippingsettingsCustomBatchRequestEntryIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ShippingsettingsCustomBatchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["shippingsettingsGetsupportedcarriers"] = content.post(
        "shippingsettings/batch",
        t.struct(
            {
                "entries": t.array(
                    t.proxy(renames["ShippingsettingsCustomBatchRequestEntryIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ShippingsettingsCustomBatchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["shippingsettingsGetsupportedholidays"] = content.post(
        "shippingsettings/batch",
        t.struct(
            {
                "entries": t.array(
                    t.proxy(renames["ShippingsettingsCustomBatchRequestEntryIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ShippingsettingsCustomBatchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["shippingsettingsCustombatch"] = content.post(
        "shippingsettings/batch",
        t.struct(
            {
                "entries": t.array(
                    t.proxy(renames["ShippingsettingsCustomBatchRequestEntryIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ShippingsettingsCustomBatchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["regionalinventoryCustombatch"] = content.post(
        "{merchantId}/products/{productId}/regionalinventory",
        t.struct(
            {
                "productId": t.string().optional(),
                "merchantId": t.string().optional(),
                "kind": t.string().optional(),
                "customAttributes": t.array(
                    t.proxy(renames["CustomAttributeIn"])
                ).optional(),
                "availability": t.string().optional(),
                "salePrice": t.proxy(renames["PriceIn"]).optional(),
                "salePriceEffectiveDate": t.string().optional(),
                "regionId": t.string().optional(),
                "price": t.proxy(renames["PriceIn"]).optional(),
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
                "productId": t.string().optional(),
                "merchantId": t.string().optional(),
                "kind": t.string().optional(),
                "customAttributes": t.array(
                    t.proxy(renames["CustomAttributeIn"])
                ).optional(),
                "availability": t.string().optional(),
                "salePrice": t.proxy(renames["PriceIn"]).optional(),
                "salePriceEffectiveDate": t.string().optional(),
                "regionId": t.string().optional(),
                "price": t.proxy(renames["PriceIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RegionalInventoryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["orderreturnsCreateorderreturn"] = content.post(
        "{merchantId}/orderreturns/{returnId}/acknowledge",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "returnId": t.string().optional(),
                "operationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrderreturnsAcknowledgeResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["orderreturnsGet"] = content.post(
        "{merchantId}/orderreturns/{returnId}/acknowledge",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "returnId": t.string().optional(),
                "operationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrderreturnsAcknowledgeResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["orderreturnsProcess"] = content.post(
        "{merchantId}/orderreturns/{returnId}/acknowledge",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "returnId": t.string().optional(),
                "operationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrderreturnsAcknowledgeResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["orderreturnsList"] = content.post(
        "{merchantId}/orderreturns/{returnId}/acknowledge",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "returnId": t.string().optional(),
                "operationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrderreturnsAcknowledgeResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["orderreturnsAcknowledge"] = content.post(
        "{merchantId}/orderreturns/{returnId}/acknowledge",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "returnId": t.string().optional(),
                "operationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrderreturnsAcknowledgeResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["orderreturnsLabelsCreate"] = content.post(
        "{merchantId}/orderreturns/{returnId}/labels",
        t.struct(
            {
                "merchantId": t.string(),
                "returnId": t.string(),
                "trackingId": t.string().optional(),
                "carrier": t.string().optional(),
                "labelUri": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReturnShippingLabelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["datafeedsCustombatch"] = content.delete(
        "{merchantId}/datafeeds/{datafeedId}",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "datafeedId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["datafeedsGet"] = content.delete(
        "{merchantId}/datafeeds/{datafeedId}",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "datafeedId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["datafeedsUpdate"] = content.delete(
        "{merchantId}/datafeeds/{datafeedId}",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "datafeedId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["datafeedsFetchnow"] = content.delete(
        "{merchantId}/datafeeds/{datafeedId}",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "datafeedId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["datafeedsInsert"] = content.delete(
        "{merchantId}/datafeeds/{datafeedId}",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "datafeedId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["datafeedsList"] = content.delete(
        "{merchantId}/datafeeds/{datafeedId}",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "datafeedId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["datafeedsDelete"] = content.delete(
        "{merchantId}/datafeeds/{datafeedId}",
        t.struct(
            {
                "merchantId": t.string().optional(),
                "datafeedId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["regionsCreate"] = content.get(
        "{merchantId}/regions/{regionId}",
        t.struct(
            {
                "merchantId": t.string(),
                "regionId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RegionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["regionsPatch"] = content.get(
        "{merchantId}/regions/{regionId}",
        t.struct(
            {
                "merchantId": t.string(),
                "regionId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RegionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["regionsDelete"] = content.get(
        "{merchantId}/regions/{regionId}",
        t.struct(
            {
                "merchantId": t.string(),
                "regionId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RegionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["regionsList"] = content.get(
        "{merchantId}/regions/{regionId}",
        t.struct(
            {
                "merchantId": t.string(),
                "regionId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RegionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["regionsGet"] = content.get(
        "{merchantId}/regions/{regionId}",
        t.struct(
            {
                "merchantId": t.string(),
                "regionId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RegionOut"]),
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
    functions["returnaddressDelete"] = content.get(
        "{merchantId}/returnaddress",
        t.struct(
            {
                "country": t.string().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "merchantId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReturnaddressListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["returnaddressCustombatch"] = content.get(
        "{merchantId}/returnaddress",
        t.struct(
            {
                "country": t.string().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "merchantId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReturnaddressListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["returnaddressGet"] = content.get(
        "{merchantId}/returnaddress",
        t.struct(
            {
                "country": t.string().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "merchantId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReturnaddressListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["returnaddressInsert"] = content.get(
        "{merchantId}/returnaddress",
        t.struct(
            {
                "country": t.string().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "merchantId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReturnaddressListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["returnaddressList"] = content.get(
        "{merchantId}/returnaddress",
        t.struct(
            {
                "country": t.string().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "merchantId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReturnaddressListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["productstatusesGet"] = content.get(
        "{merchantId}/productstatuses",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "maxResults": t.integer().optional(),
                "destinations": t.string().optional(),
                "merchantId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductstatusesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["productstatusesCustombatch"] = content.get(
        "{merchantId}/productstatuses",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "maxResults": t.integer().optional(),
                "destinations": t.string().optional(),
                "merchantId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductstatusesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["productstatusesList"] = content.get(
        "{merchantId}/productstatuses",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "maxResults": t.integer().optional(),
                "destinations": t.string().optional(),
                "merchantId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductstatusesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["productstatusesRepricingreportsList"] = content.get(
        "{merchantId}/productstatuses/{productId}/repricingreports",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "ruleId": t.string().optional(),
                "endDate": t.string().optional(),
                "merchantId": t.string(),
                "productId": t.string(),
                "startDate": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListRepricingProductReportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["orderreportsListtransactions"] = content.get(
        "{merchantId}/orderreports/disbursements",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "disbursementEndDate": t.string().optional(),
                "disbursementStartDate": t.string().optional(),
                "merchantId": t.string().optional(),
                "pageToken": t.string().optional(),
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
                "maxResults": t.integer().optional(),
                "disbursementEndDate": t.string().optional(),
                "disbursementStartDate": t.string().optional(),
                "merchantId": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OrderreportsListDisbursementsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="content", renames=renames, types=Box(types), functions=Box(functions)
    )
