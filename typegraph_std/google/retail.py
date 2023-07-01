from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_retail():
    retail = HTTPRuntime("https://retail.googleapis.com/")

    renames = {
        "ErrorResponse": "_retail_1_ErrorResponse",
        "GoogleCloudRetailV2alphaSetInventoryMetadataIn": "_retail_2_GoogleCloudRetailV2alphaSetInventoryMetadataIn",
        "GoogleCloudRetailV2alphaSetInventoryMetadataOut": "_retail_3_GoogleCloudRetailV2alphaSetInventoryMetadataOut",
        "GoogleCloudRetailV2ConditionQueryTermIn": "_retail_4_GoogleCloudRetailV2ConditionQueryTermIn",
        "GoogleCloudRetailV2ConditionQueryTermOut": "_retail_5_GoogleCloudRetailV2ConditionQueryTermOut",
        "GoogleCloudRetailV2GcsSourceIn": "_retail_6_GoogleCloudRetailV2GcsSourceIn",
        "GoogleCloudRetailV2GcsSourceOut": "_retail_7_GoogleCloudRetailV2GcsSourceOut",
        "GoogleCloudRetailLoggingServiceContextIn": "_retail_8_GoogleCloudRetailLoggingServiceContextIn",
        "GoogleCloudRetailLoggingServiceContextOut": "_retail_9_GoogleCloudRetailLoggingServiceContextOut",
        "GoogleCloudRetailV2alphaTuneModelMetadataIn": "_retail_10_GoogleCloudRetailV2alphaTuneModelMetadataIn",
        "GoogleCloudRetailV2alphaTuneModelMetadataOut": "_retail_11_GoogleCloudRetailV2alphaTuneModelMetadataOut",
        "GoogleCloudRetailV2TuneModelRequestIn": "_retail_12_GoogleCloudRetailV2TuneModelRequestIn",
        "GoogleCloudRetailV2TuneModelRequestOut": "_retail_13_GoogleCloudRetailV2TuneModelRequestOut",
        "GoogleCloudRetailV2PredictRequestIn": "_retail_14_GoogleCloudRetailV2PredictRequestIn",
        "GoogleCloudRetailV2PredictRequestOut": "_retail_15_GoogleCloudRetailV2PredictRequestOut",
        "GoogleCloudRetailV2alphaExportErrorsConfigIn": "_retail_16_GoogleCloudRetailV2alphaExportErrorsConfigIn",
        "GoogleCloudRetailV2alphaExportErrorsConfigOut": "_retail_17_GoogleCloudRetailV2alphaExportErrorsConfigOut",
        "GoogleCloudRetailV2UserEventImportSummaryIn": "_retail_18_GoogleCloudRetailV2UserEventImportSummaryIn",
        "GoogleCloudRetailV2UserEventImportSummaryOut": "_retail_19_GoogleCloudRetailV2UserEventImportSummaryOut",
        "GoogleCloudRetailV2alphaTuneModelResponseIn": "_retail_20_GoogleCloudRetailV2alphaTuneModelResponseIn",
        "GoogleCloudRetailV2alphaTuneModelResponseOut": "_retail_21_GoogleCloudRetailV2alphaTuneModelResponseOut",
        "GoogleCloudRetailV2AddFulfillmentPlacesMetadataIn": "_retail_22_GoogleCloudRetailV2AddFulfillmentPlacesMetadataIn",
        "GoogleCloudRetailV2AddFulfillmentPlacesMetadataOut": "_retail_23_GoogleCloudRetailV2AddFulfillmentPlacesMetadataOut",
        "GoogleCloudRetailV2RemoveFulfillmentPlacesMetadataIn": "_retail_24_GoogleCloudRetailV2RemoveFulfillmentPlacesMetadataIn",
        "GoogleCloudRetailV2RemoveFulfillmentPlacesMetadataOut": "_retail_25_GoogleCloudRetailV2RemoveFulfillmentPlacesMetadataOut",
        "GoogleCloudRetailV2alphaModelModelFeaturesConfigIn": "_retail_26_GoogleCloudRetailV2alphaModelModelFeaturesConfigIn",
        "GoogleCloudRetailV2alphaModelModelFeaturesConfigOut": "_retail_27_GoogleCloudRetailV2alphaModelModelFeaturesConfigOut",
        "GoogleCloudRetailV2SearchRequestFacetSpecIn": "_retail_28_GoogleCloudRetailV2SearchRequestFacetSpecIn",
        "GoogleCloudRetailV2SearchRequestFacetSpecOut": "_retail_29_GoogleCloudRetailV2SearchRequestFacetSpecOut",
        "GoogleCloudRetailV2alphaAddLocalInventoriesMetadataIn": "_retail_30_GoogleCloudRetailV2alphaAddLocalInventoriesMetadataIn",
        "GoogleCloudRetailV2alphaAddLocalInventoriesMetadataOut": "_retail_31_GoogleCloudRetailV2alphaAddLocalInventoriesMetadataOut",
        "GoogleCloudRetailV2FulfillmentInfoIn": "_retail_32_GoogleCloudRetailV2FulfillmentInfoIn",
        "GoogleCloudRetailV2FulfillmentInfoOut": "_retail_33_GoogleCloudRetailV2FulfillmentInfoOut",
        "GoogleCloudRetailV2RejoinUserEventsMetadataIn": "_retail_34_GoogleCloudRetailV2RejoinUserEventsMetadataIn",
        "GoogleCloudRetailV2RejoinUserEventsMetadataOut": "_retail_35_GoogleCloudRetailV2RejoinUserEventsMetadataOut",
        "GoogleCloudRetailV2ModelServingConfigListIn": "_retail_36_GoogleCloudRetailV2ModelServingConfigListIn",
        "GoogleCloudRetailV2ModelServingConfigListOut": "_retail_37_GoogleCloudRetailV2ModelServingConfigListOut",
        "GoogleCloudRetailV2betaRemoveFulfillmentPlacesResponseIn": "_retail_38_GoogleCloudRetailV2betaRemoveFulfillmentPlacesResponseIn",
        "GoogleCloudRetailV2betaRemoveFulfillmentPlacesResponseOut": "_retail_39_GoogleCloudRetailV2betaRemoveFulfillmentPlacesResponseOut",
        "GoogleCloudRetailV2RuleReplacementActionIn": "_retail_40_GoogleCloudRetailV2RuleReplacementActionIn",
        "GoogleCloudRetailV2RuleReplacementActionOut": "_retail_41_GoogleCloudRetailV2RuleReplacementActionOut",
        "GoogleCloudRetailV2ImportMetadataIn": "_retail_42_GoogleCloudRetailV2ImportMetadataIn",
        "GoogleCloudRetailV2ImportMetadataOut": "_retail_43_GoogleCloudRetailV2ImportMetadataOut",
        "GoogleCloudRetailV2PromotionIn": "_retail_44_GoogleCloudRetailV2PromotionIn",
        "GoogleCloudRetailV2PromotionOut": "_retail_45_GoogleCloudRetailV2PromotionOut",
        "GoogleCloudRetailV2betaModelModelFeaturesConfigIn": "_retail_46_GoogleCloudRetailV2betaModelModelFeaturesConfigIn",
        "GoogleCloudRetailV2betaModelModelFeaturesConfigOut": "_retail_47_GoogleCloudRetailV2betaModelModelFeaturesConfigOut",
        "GoogleCloudRetailV2alphaPurgeProductsMetadataIn": "_retail_48_GoogleCloudRetailV2alphaPurgeProductsMetadataIn",
        "GoogleCloudRetailV2alphaPurgeProductsMetadataOut": "_retail_49_GoogleCloudRetailV2alphaPurgeProductsMetadataOut",
        "GoogleCloudRetailV2alphaModelFrequentlyBoughtTogetherFeaturesConfigIn": "_retail_50_GoogleCloudRetailV2alphaModelFrequentlyBoughtTogetherFeaturesConfigIn",
        "GoogleCloudRetailV2alphaModelFrequentlyBoughtTogetherFeaturesConfigOut": "_retail_51_GoogleCloudRetailV2alphaModelFrequentlyBoughtTogetherFeaturesConfigOut",
        "GoogleCloudRetailV2ListCatalogsResponseIn": "_retail_52_GoogleCloudRetailV2ListCatalogsResponseIn",
        "GoogleCloudRetailV2ListCatalogsResponseOut": "_retail_53_GoogleCloudRetailV2ListCatalogsResponseOut",
        "GoogleCloudRetailV2betaModelIn": "_retail_54_GoogleCloudRetailV2betaModelIn",
        "GoogleCloudRetailV2betaModelOut": "_retail_55_GoogleCloudRetailV2betaModelOut",
        "GoogleCloudRetailV2AddCatalogAttributeRequestIn": "_retail_56_GoogleCloudRetailV2AddCatalogAttributeRequestIn",
        "GoogleCloudRetailV2AddCatalogAttributeRequestOut": "_retail_57_GoogleCloudRetailV2AddCatalogAttributeRequestOut",
        "GoogleCloudRetailV2ServingConfigIn": "_retail_58_GoogleCloudRetailV2ServingConfigIn",
        "GoogleCloudRetailV2ServingConfigOut": "_retail_59_GoogleCloudRetailV2ServingConfigOut",
        "GoogleCloudRetailV2AddLocalInventoriesMetadataIn": "_retail_60_GoogleCloudRetailV2AddLocalInventoriesMetadataIn",
        "GoogleCloudRetailV2AddLocalInventoriesMetadataOut": "_retail_61_GoogleCloudRetailV2AddLocalInventoriesMetadataOut",
        "GoogleCloudRetailV2SearchRequestBoostSpecConditionBoostSpecIn": "_retail_62_GoogleCloudRetailV2SearchRequestBoostSpecConditionBoostSpecIn",
        "GoogleCloudRetailV2SearchRequestBoostSpecConditionBoostSpecOut": "_retail_63_GoogleCloudRetailV2SearchRequestBoostSpecConditionBoostSpecOut",
        "GoogleCloudRetailV2ProductLevelConfigIn": "_retail_64_GoogleCloudRetailV2ProductLevelConfigIn",
        "GoogleCloudRetailV2ProductLevelConfigOut": "_retail_65_GoogleCloudRetailV2ProductLevelConfigOut",
        "GoogleCloudRetailV2ListProductsResponseIn": "_retail_66_GoogleCloudRetailV2ListProductsResponseIn",
        "GoogleCloudRetailV2ListProductsResponseOut": "_retail_67_GoogleCloudRetailV2ListProductsResponseOut",
        "GoogleCloudRetailV2alphaRemoveFulfillmentPlacesResponseIn": "_retail_68_GoogleCloudRetailV2alphaRemoveFulfillmentPlacesResponseIn",
        "GoogleCloudRetailV2alphaRemoveFulfillmentPlacesResponseOut": "_retail_69_GoogleCloudRetailV2alphaRemoveFulfillmentPlacesResponseOut",
        "GoogleCloudRetailV2RuleDoNotAssociateActionIn": "_retail_70_GoogleCloudRetailV2RuleDoNotAssociateActionIn",
        "GoogleCloudRetailV2RuleDoNotAssociateActionOut": "_retail_71_GoogleCloudRetailV2RuleDoNotAssociateActionOut",
        "GoogleCloudRetailV2betaModelServingConfigListIn": "_retail_72_GoogleCloudRetailV2betaModelServingConfigListIn",
        "GoogleCloudRetailV2betaModelServingConfigListOut": "_retail_73_GoogleCloudRetailV2betaModelServingConfigListOut",
        "GoogleCloudRetailLoggingHttpRequestContextIn": "_retail_74_GoogleCloudRetailLoggingHttpRequestContextIn",
        "GoogleCloudRetailLoggingHttpRequestContextOut": "_retail_75_GoogleCloudRetailLoggingHttpRequestContextOut",
        "GoogleCloudRetailV2CompleteQueryResponseCompletionResultIn": "_retail_76_GoogleCloudRetailV2CompleteQueryResponseCompletionResultIn",
        "GoogleCloudRetailV2CompleteQueryResponseCompletionResultOut": "_retail_77_GoogleCloudRetailV2CompleteQueryResponseCompletionResultOut",
        "GoogleCloudRetailV2betaImportProductsResponseIn": "_retail_78_GoogleCloudRetailV2betaImportProductsResponseIn",
        "GoogleCloudRetailV2betaImportProductsResponseOut": "_retail_79_GoogleCloudRetailV2betaImportProductsResponseOut",
        "GoogleCloudRetailV2UserEventInputConfigIn": "_retail_80_GoogleCloudRetailV2UserEventInputConfigIn",
        "GoogleCloudRetailV2UserEventInputConfigOut": "_retail_81_GoogleCloudRetailV2UserEventInputConfigOut",
        "GoogleCloudRetailV2SearchResponseIn": "_retail_82_GoogleCloudRetailV2SearchResponseIn",
        "GoogleCloudRetailV2SearchResponseOut": "_retail_83_GoogleCloudRetailV2SearchResponseOut",
        "GoogleCloudRetailV2PredictResponseIn": "_retail_84_GoogleCloudRetailV2PredictResponseIn",
        "GoogleCloudRetailV2PredictResponseOut": "_retail_85_GoogleCloudRetailV2PredictResponseOut",
        "GoogleCloudRetailV2betaRejoinUserEventsMetadataIn": "_retail_86_GoogleCloudRetailV2betaRejoinUserEventsMetadataIn",
        "GoogleCloudRetailV2betaRejoinUserEventsMetadataOut": "_retail_87_GoogleCloudRetailV2betaRejoinUserEventsMetadataOut",
        "GoogleCloudRetailV2alphaTransformedUserEventsMetadataIn": "_retail_88_GoogleCloudRetailV2alphaTransformedUserEventsMetadataIn",
        "GoogleCloudRetailV2alphaTransformedUserEventsMetadataOut": "_retail_89_GoogleCloudRetailV2alphaTransformedUserEventsMetadataOut",
        "GoogleCloudRetailV2alphaModelPageOptimizationConfigPanelIn": "_retail_90_GoogleCloudRetailV2alphaModelPageOptimizationConfigPanelIn",
        "GoogleCloudRetailV2alphaModelPageOptimizationConfigPanelOut": "_retail_91_GoogleCloudRetailV2alphaModelPageOptimizationConfigPanelOut",
        "GoogleCloudRetailV2betaSetInventoryMetadataIn": "_retail_92_GoogleCloudRetailV2betaSetInventoryMetadataIn",
        "GoogleCloudRetailV2betaSetInventoryMetadataOut": "_retail_93_GoogleCloudRetailV2betaSetInventoryMetadataOut",
        "GoogleCloudRetailV2CatalogAttributeIn": "_retail_94_GoogleCloudRetailV2CatalogAttributeIn",
        "GoogleCloudRetailV2CatalogAttributeOut": "_retail_95_GoogleCloudRetailV2CatalogAttributeOut",
        "GoogleCloudRetailV2alphaAddFulfillmentPlacesMetadataIn": "_retail_96_GoogleCloudRetailV2alphaAddFulfillmentPlacesMetadataIn",
        "GoogleCloudRetailV2alphaAddFulfillmentPlacesMetadataOut": "_retail_97_GoogleCloudRetailV2alphaAddFulfillmentPlacesMetadataOut",
        "GoogleCloudRetailV2AddFulfillmentPlacesRequestIn": "_retail_98_GoogleCloudRetailV2AddFulfillmentPlacesRequestIn",
        "GoogleCloudRetailV2AddFulfillmentPlacesRequestOut": "_retail_99_GoogleCloudRetailV2AddFulfillmentPlacesRequestOut",
        "GoogleCloudRetailV2CompletionDataInputConfigIn": "_retail_100_GoogleCloudRetailV2CompletionDataInputConfigIn",
        "GoogleCloudRetailV2CompletionDataInputConfigOut": "_retail_101_GoogleCloudRetailV2CompletionDataInputConfigOut",
        "GoogleCloudRetailV2ImportProductsRequestIn": "_retail_102_GoogleCloudRetailV2ImportProductsRequestIn",
        "GoogleCloudRetailV2ImportProductsRequestOut": "_retail_103_GoogleCloudRetailV2ImportProductsRequestOut",
        "GoogleCloudRetailV2betaCreateMerchantCenterAccountLinkMetadataIn": "_retail_104_GoogleCloudRetailV2betaCreateMerchantCenterAccountLinkMetadataIn",
        "GoogleCloudRetailV2betaCreateMerchantCenterAccountLinkMetadataOut": "_retail_105_GoogleCloudRetailV2betaCreateMerchantCenterAccountLinkMetadataOut",
        "GoogleCloudRetailV2PriceInfoIn": "_retail_106_GoogleCloudRetailV2PriceInfoIn",
        "GoogleCloudRetailV2PriceInfoOut": "_retail_107_GoogleCloudRetailV2PriceInfoOut",
        "GoogleCloudRetailV2betaExportProductsResponseIn": "_retail_108_GoogleCloudRetailV2betaExportProductsResponseIn",
        "GoogleCloudRetailV2betaExportProductsResponseOut": "_retail_109_GoogleCloudRetailV2betaExportProductsResponseOut",
        "GoogleCloudRetailV2alphaMerchantCenterAccountLinkMerchantCenterFeedFilterIn": "_retail_110_GoogleCloudRetailV2alphaMerchantCenterAccountLinkMerchantCenterFeedFilterIn",
        "GoogleCloudRetailV2alphaMerchantCenterAccountLinkMerchantCenterFeedFilterOut": "_retail_111_GoogleCloudRetailV2alphaMerchantCenterAccountLinkMerchantCenterFeedFilterOut",
        "GoogleCloudRetailV2alphaAddFulfillmentPlacesResponseIn": "_retail_112_GoogleCloudRetailV2alphaAddFulfillmentPlacesResponseIn",
        "GoogleCloudRetailV2alphaAddFulfillmentPlacesResponseOut": "_retail_113_GoogleCloudRetailV2alphaAddFulfillmentPlacesResponseOut",
        "GoogleCloudRetailV2ImportErrorsConfigIn": "_retail_114_GoogleCloudRetailV2ImportErrorsConfigIn",
        "GoogleCloudRetailV2ImportErrorsConfigOut": "_retail_115_GoogleCloudRetailV2ImportErrorsConfigOut",
        "GoogleCloudRetailV2LocalInventoryIn": "_retail_116_GoogleCloudRetailV2LocalInventoryIn",
        "GoogleCloudRetailV2LocalInventoryOut": "_retail_117_GoogleCloudRetailV2LocalInventoryOut",
        "GoogleCloudRetailV2SearchResponseFacetFacetValueIn": "_retail_118_GoogleCloudRetailV2SearchResponseFacetFacetValueIn",
        "GoogleCloudRetailV2SearchResponseFacetFacetValueOut": "_retail_119_GoogleCloudRetailV2SearchResponseFacetFacetValueOut",
        "GoogleCloudRetailV2ReplaceCatalogAttributeRequestIn": "_retail_120_GoogleCloudRetailV2ReplaceCatalogAttributeRequestIn",
        "GoogleCloudRetailV2ReplaceCatalogAttributeRequestOut": "_retail_121_GoogleCloudRetailV2ReplaceCatalogAttributeRequestOut",
        "GoogleProtobufEmptyIn": "_retail_122_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_retail_123_GoogleProtobufEmptyOut",
        "GoogleCloudRetailV2SearchRequestFacetSpecFacetKeyIn": "_retail_124_GoogleCloudRetailV2SearchRequestFacetSpecFacetKeyIn",
        "GoogleCloudRetailV2SearchRequestFacetSpecFacetKeyOut": "_retail_125_GoogleCloudRetailV2SearchRequestFacetSpecFacetKeyOut",
        "GoogleCloudRetailV2alphaRemoveLocalInventoriesResponseIn": "_retail_126_GoogleCloudRetailV2alphaRemoveLocalInventoriesResponseIn",
        "GoogleCloudRetailV2alphaRemoveLocalInventoriesResponseOut": "_retail_127_GoogleCloudRetailV2alphaRemoveLocalInventoriesResponseOut",
        "GoogleCloudRetailV2ProductIn": "_retail_128_GoogleCloudRetailV2ProductIn",
        "GoogleCloudRetailV2ProductOut": "_retail_129_GoogleCloudRetailV2ProductOut",
        "GoogleCloudRetailV2IntervalIn": "_retail_130_GoogleCloudRetailV2IntervalIn",
        "GoogleCloudRetailV2IntervalOut": "_retail_131_GoogleCloudRetailV2IntervalOut",
        "GoogleCloudRetailV2RemoveFulfillmentPlacesRequestIn": "_retail_132_GoogleCloudRetailV2RemoveFulfillmentPlacesRequestIn",
        "GoogleCloudRetailV2RemoveFulfillmentPlacesRequestOut": "_retail_133_GoogleCloudRetailV2RemoveFulfillmentPlacesRequestOut",
        "GoogleCloudRetailV2alphaRejoinUserEventsResponseIn": "_retail_134_GoogleCloudRetailV2alphaRejoinUserEventsResponseIn",
        "GoogleCloudRetailV2alphaRejoinUserEventsResponseOut": "_retail_135_GoogleCloudRetailV2alphaRejoinUserEventsResponseOut",
        "GoogleCloudRetailV2RatingIn": "_retail_136_GoogleCloudRetailV2RatingIn",
        "GoogleCloudRetailV2RatingOut": "_retail_137_GoogleCloudRetailV2RatingOut",
        "GoogleCloudRetailV2CompletionConfigIn": "_retail_138_GoogleCloudRetailV2CompletionConfigIn",
        "GoogleCloudRetailV2CompletionConfigOut": "_retail_139_GoogleCloudRetailV2CompletionConfigOut",
        "GoogleCloudRetailV2alphaImportUserEventsResponseIn": "_retail_140_GoogleCloudRetailV2alphaImportUserEventsResponseIn",
        "GoogleCloudRetailV2alphaImportUserEventsResponseOut": "_retail_141_GoogleCloudRetailV2alphaImportUserEventsResponseOut",
        "GoogleCloudRetailV2TuneModelMetadataIn": "_retail_142_GoogleCloudRetailV2TuneModelMetadataIn",
        "GoogleCloudRetailV2TuneModelMetadataOut": "_retail_143_GoogleCloudRetailV2TuneModelMetadataOut",
        "GoogleCloudRetailV2CatalogIn": "_retail_144_GoogleCloudRetailV2CatalogIn",
        "GoogleCloudRetailV2CatalogOut": "_retail_145_GoogleCloudRetailV2CatalogOut",
        "GoogleCloudRetailV2UserEventIn": "_retail_146_GoogleCloudRetailV2UserEventIn",
        "GoogleCloudRetailV2UserEventOut": "_retail_147_GoogleCloudRetailV2UserEventOut",
        "GoogleCloudRetailV2SetDefaultBranchRequestIn": "_retail_148_GoogleCloudRetailV2SetDefaultBranchRequestIn",
        "GoogleCloudRetailV2SetDefaultBranchRequestOut": "_retail_149_GoogleCloudRetailV2SetDefaultBranchRequestOut",
        "GoogleCloudRetailV2betaPurgeUserEventsResponseIn": "_retail_150_GoogleCloudRetailV2betaPurgeUserEventsResponseIn",
        "GoogleCloudRetailV2betaPurgeUserEventsResponseOut": "_retail_151_GoogleCloudRetailV2betaPurgeUserEventsResponseOut",
        "GoogleCloudRetailV2alphaPurgeProductsResponseIn": "_retail_152_GoogleCloudRetailV2alphaPurgeProductsResponseIn",
        "GoogleCloudRetailV2alphaPurgeProductsResponseOut": "_retail_153_GoogleCloudRetailV2alphaPurgeProductsResponseOut",
        "GoogleCloudRetailV2alphaGcsOutputResultIn": "_retail_154_GoogleCloudRetailV2alphaGcsOutputResultIn",
        "GoogleCloudRetailV2alphaGcsOutputResultOut": "_retail_155_GoogleCloudRetailV2alphaGcsOutputResultOut",
        "GoogleCloudRetailV2RuleIn": "_retail_156_GoogleCloudRetailV2RuleIn",
        "GoogleCloudRetailV2RuleOut": "_retail_157_GoogleCloudRetailV2RuleOut",
        "GoogleCloudRetailV2alphaExportUserEventsResponseIn": "_retail_158_GoogleCloudRetailV2alphaExportUserEventsResponseIn",
        "GoogleCloudRetailV2alphaExportUserEventsResponseOut": "_retail_159_GoogleCloudRetailV2alphaExportUserEventsResponseOut",
        "GoogleCloudRetailV2betaImportCompletionDataResponseIn": "_retail_160_GoogleCloudRetailV2betaImportCompletionDataResponseIn",
        "GoogleCloudRetailV2betaImportCompletionDataResponseOut": "_retail_161_GoogleCloudRetailV2betaImportCompletionDataResponseOut",
        "GoogleCloudRetailV2RuleTwowaySynonymsActionIn": "_retail_162_GoogleCloudRetailV2RuleTwowaySynonymsActionIn",
        "GoogleCloudRetailV2RuleTwowaySynonymsActionOut": "_retail_163_GoogleCloudRetailV2RuleTwowaySynonymsActionOut",
        "GoogleCloudRetailLoggingErrorContextIn": "_retail_164_GoogleCloudRetailLoggingErrorContextIn",
        "GoogleCloudRetailLoggingErrorContextOut": "_retail_165_GoogleCloudRetailLoggingErrorContextOut",
        "GoogleCloudRetailV2RemoveLocalInventoriesResponseIn": "_retail_166_GoogleCloudRetailV2RemoveLocalInventoriesResponseIn",
        "GoogleCloudRetailV2RemoveLocalInventoriesResponseOut": "_retail_167_GoogleCloudRetailV2RemoveLocalInventoriesResponseOut",
        "GoogleCloudRetailV2ImportUserEventsRequestIn": "_retail_168_GoogleCloudRetailV2ImportUserEventsRequestIn",
        "GoogleCloudRetailV2ImportUserEventsRequestOut": "_retail_169_GoogleCloudRetailV2ImportUserEventsRequestOut",
        "GoogleCloudRetailV2RuleRedirectActionIn": "_retail_170_GoogleCloudRetailV2RuleRedirectActionIn",
        "GoogleCloudRetailV2RuleRedirectActionOut": "_retail_171_GoogleCloudRetailV2RuleRedirectActionOut",
        "GoogleCloudRetailV2ProductDetailIn": "_retail_172_GoogleCloudRetailV2ProductDetailIn",
        "GoogleCloudRetailV2ProductDetailOut": "_retail_173_GoogleCloudRetailV2ProductDetailOut",
        "GoogleCloudRetailV2ListModelsResponseIn": "_retail_174_GoogleCloudRetailV2ListModelsResponseIn",
        "GoogleCloudRetailV2ListModelsResponseOut": "_retail_175_GoogleCloudRetailV2ListModelsResponseOut",
        "GoogleCloudRetailV2alphaImportErrorsConfigIn": "_retail_176_GoogleCloudRetailV2alphaImportErrorsConfigIn",
        "GoogleCloudRetailV2alphaImportErrorsConfigOut": "_retail_177_GoogleCloudRetailV2alphaImportErrorsConfigOut",
        "GoogleCloudRetailV2PurgeUserEventsResponseIn": "_retail_178_GoogleCloudRetailV2PurgeUserEventsResponseIn",
        "GoogleCloudRetailV2PurgeUserEventsResponseOut": "_retail_179_GoogleCloudRetailV2PurgeUserEventsResponseOut",
        "GoogleCloudRetailV2PauseModelRequestIn": "_retail_180_GoogleCloudRetailV2PauseModelRequestIn",
        "GoogleCloudRetailV2PauseModelRequestOut": "_retail_181_GoogleCloudRetailV2PauseModelRequestOut",
        "GoogleCloudRetailV2alphaRejoinUserEventsMetadataIn": "_retail_182_GoogleCloudRetailV2alphaRejoinUserEventsMetadataIn",
        "GoogleCloudRetailV2alphaRejoinUserEventsMetadataOut": "_retail_183_GoogleCloudRetailV2alphaRejoinUserEventsMetadataOut",
        "GoogleCloudRetailLoggingImportErrorContextIn": "_retail_184_GoogleCloudRetailLoggingImportErrorContextIn",
        "GoogleCloudRetailLoggingImportErrorContextOut": "_retail_185_GoogleCloudRetailLoggingImportErrorContextOut",
        "GoogleCloudRetailV2SetInventoryMetadataIn": "_retail_186_GoogleCloudRetailV2SetInventoryMetadataIn",
        "GoogleCloudRetailV2SetInventoryMetadataOut": "_retail_187_GoogleCloudRetailV2SetInventoryMetadataOut",
        "GoogleCloudRetailLoggingErrorLogIn": "_retail_188_GoogleCloudRetailLoggingErrorLogIn",
        "GoogleCloudRetailLoggingErrorLogOut": "_retail_189_GoogleCloudRetailLoggingErrorLogOut",
        "GoogleCloudRetailV2SetInventoryResponseIn": "_retail_190_GoogleCloudRetailV2SetInventoryResponseIn",
        "GoogleCloudRetailV2SetInventoryResponseOut": "_retail_191_GoogleCloudRetailV2SetInventoryResponseOut",
        "GoogleCloudRetailV2ConditionIn": "_retail_192_GoogleCloudRetailV2ConditionIn",
        "GoogleCloudRetailV2ConditionOut": "_retail_193_GoogleCloudRetailV2ConditionOut",
        "GoogleLongrunningListOperationsResponseIn": "_retail_194_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_retail_195_GoogleLongrunningListOperationsResponseOut",
        "GoogleCloudRetailV2betaExportMetadataIn": "_retail_196_GoogleCloudRetailV2betaExportMetadataIn",
        "GoogleCloudRetailV2betaExportMetadataOut": "_retail_197_GoogleCloudRetailV2betaExportMetadataOut",
        "GoogleCloudRetailV2RemoveCatalogAttributeRequestIn": "_retail_198_GoogleCloudRetailV2RemoveCatalogAttributeRequestIn",
        "GoogleCloudRetailV2RemoveCatalogAttributeRequestOut": "_retail_199_GoogleCloudRetailV2RemoveCatalogAttributeRequestOut",
        "GoogleCloudRetailV2ImageIn": "_retail_200_GoogleCloudRetailV2ImageIn",
        "GoogleCloudRetailV2ImageOut": "_retail_201_GoogleCloudRetailV2ImageOut",
        "GoogleCloudRetailV2RuleBoostActionIn": "_retail_202_GoogleCloudRetailV2RuleBoostActionIn",
        "GoogleCloudRetailV2RuleBoostActionOut": "_retail_203_GoogleCloudRetailV2RuleBoostActionOut",
        "GoogleCloudRetailV2SearchRequestQueryExpansionSpecIn": "_retail_204_GoogleCloudRetailV2SearchRequestQueryExpansionSpecIn",
        "GoogleCloudRetailV2SearchRequestQueryExpansionSpecOut": "_retail_205_GoogleCloudRetailV2SearchRequestQueryExpansionSpecOut",
        "GoogleCloudRetailV2betaOutputResultIn": "_retail_206_GoogleCloudRetailV2betaOutputResultIn",
        "GoogleCloudRetailV2betaOutputResultOut": "_retail_207_GoogleCloudRetailV2betaOutputResultOut",
        "GoogleCloudRetailV2alphaModelIn": "_retail_208_GoogleCloudRetailV2alphaModelIn",
        "GoogleCloudRetailV2alphaModelOut": "_retail_209_GoogleCloudRetailV2alphaModelOut",
        "GoogleRpcStatusIn": "_retail_210_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_retail_211_GoogleRpcStatusOut",
        "GoogleCloudRetailV2alphaImportCompletionDataResponseIn": "_retail_212_GoogleCloudRetailV2alphaImportCompletionDataResponseIn",
        "GoogleCloudRetailV2alphaImportCompletionDataResponseOut": "_retail_213_GoogleCloudRetailV2alphaImportCompletionDataResponseOut",
        "GoogleCloudRetailV2AudienceIn": "_retail_214_GoogleCloudRetailV2AudienceIn",
        "GoogleCloudRetailV2AudienceOut": "_retail_215_GoogleCloudRetailV2AudienceOut",
        "GoogleCloudRetailV2betaImportUserEventsResponseIn": "_retail_216_GoogleCloudRetailV2betaImportUserEventsResponseIn",
        "GoogleCloudRetailV2betaImportUserEventsResponseOut": "_retail_217_GoogleCloudRetailV2betaImportUserEventsResponseOut",
        "GoogleApiHttpBodyIn": "_retail_218_GoogleApiHttpBodyIn",
        "GoogleApiHttpBodyOut": "_retail_219_GoogleApiHttpBodyOut",
        "GoogleCloudRetailV2AddControlRequestIn": "_retail_220_GoogleCloudRetailV2AddControlRequestIn",
        "GoogleCloudRetailV2AddControlRequestOut": "_retail_221_GoogleCloudRetailV2AddControlRequestOut",
        "GoogleCloudRetailV2UserEventInlineSourceIn": "_retail_222_GoogleCloudRetailV2UserEventInlineSourceIn",
        "GoogleCloudRetailV2UserEventInlineSourceOut": "_retail_223_GoogleCloudRetailV2UserEventInlineSourceOut",
        "GoogleCloudRetailV2CreateModelMetadataIn": "_retail_224_GoogleCloudRetailV2CreateModelMetadataIn",
        "GoogleCloudRetailV2CreateModelMetadataOut": "_retail_225_GoogleCloudRetailV2CreateModelMetadataOut",
        "GoogleCloudRetailV2ModelFrequentlyBoughtTogetherFeaturesConfigIn": "_retail_226_GoogleCloudRetailV2ModelFrequentlyBoughtTogetherFeaturesConfigIn",
        "GoogleCloudRetailV2ModelFrequentlyBoughtTogetherFeaturesConfigOut": "_retail_227_GoogleCloudRetailV2ModelFrequentlyBoughtTogetherFeaturesConfigOut",
        "GoogleCloudRetailV2alphaRemoveLocalInventoriesMetadataIn": "_retail_228_GoogleCloudRetailV2alphaRemoveLocalInventoriesMetadataIn",
        "GoogleCloudRetailV2alphaRemoveLocalInventoriesMetadataOut": "_retail_229_GoogleCloudRetailV2alphaRemoveLocalInventoriesMetadataOut",
        "GoogleCloudRetailV2betaRemoveLocalInventoriesMetadataIn": "_retail_230_GoogleCloudRetailV2betaRemoveLocalInventoriesMetadataIn",
        "GoogleCloudRetailV2betaRemoveLocalInventoriesMetadataOut": "_retail_231_GoogleCloudRetailV2betaRemoveLocalInventoriesMetadataOut",
        "GoogleCloudRetailV2betaAddFulfillmentPlacesMetadataIn": "_retail_232_GoogleCloudRetailV2betaAddFulfillmentPlacesMetadataIn",
        "GoogleCloudRetailV2betaAddFulfillmentPlacesMetadataOut": "_retail_233_GoogleCloudRetailV2betaAddFulfillmentPlacesMetadataOut",
        "GoogleCloudRetailV2ListControlsResponseIn": "_retail_234_GoogleCloudRetailV2ListControlsResponseIn",
        "GoogleCloudRetailV2ListControlsResponseOut": "_retail_235_GoogleCloudRetailV2ListControlsResponseOut",
        "GoogleCloudRetailV2betaImportMetadataIn": "_retail_236_GoogleCloudRetailV2betaImportMetadataIn",
        "GoogleCloudRetailV2betaImportMetadataOut": "_retail_237_GoogleCloudRetailV2betaImportMetadataOut",
        "GoogleCloudRetailV2betaTuneModelMetadataIn": "_retail_238_GoogleCloudRetailV2betaTuneModelMetadataIn",
        "GoogleCloudRetailV2betaTuneModelMetadataOut": "_retail_239_GoogleCloudRetailV2betaTuneModelMetadataOut",
        "GoogleCloudRetailV2RemoveLocalInventoriesMetadataIn": "_retail_240_GoogleCloudRetailV2RemoveLocalInventoriesMetadataIn",
        "GoogleCloudRetailV2RemoveLocalInventoriesMetadataOut": "_retail_241_GoogleCloudRetailV2RemoveLocalInventoriesMetadataOut",
        "GoogleCloudRetailV2RemoveControlRequestIn": "_retail_242_GoogleCloudRetailV2RemoveControlRequestIn",
        "GoogleCloudRetailV2RemoveControlRequestOut": "_retail_243_GoogleCloudRetailV2RemoveControlRequestOut",
        "GoogleCloudRetailV2betaExportUserEventsResponseIn": "_retail_244_GoogleCloudRetailV2betaExportUserEventsResponseIn",
        "GoogleCloudRetailV2betaExportUserEventsResponseOut": "_retail_245_GoogleCloudRetailV2betaExportUserEventsResponseOut",
        "GoogleCloudRetailV2AddLocalInventoriesRequestIn": "_retail_246_GoogleCloudRetailV2AddLocalInventoriesRequestIn",
        "GoogleCloudRetailV2AddLocalInventoriesRequestOut": "_retail_247_GoogleCloudRetailV2AddLocalInventoriesRequestOut",
        "GoogleCloudRetailV2betaMerchantCenterAccountLinkMerchantCenterFeedFilterIn": "_retail_248_GoogleCloudRetailV2betaMerchantCenterAccountLinkMerchantCenterFeedFilterIn",
        "GoogleCloudRetailV2betaMerchantCenterAccountLinkMerchantCenterFeedFilterOut": "_retail_249_GoogleCloudRetailV2betaMerchantCenterAccountLinkMerchantCenterFeedFilterOut",
        "GoogleCloudRetailV2RuleIgnoreActionIn": "_retail_250_GoogleCloudRetailV2RuleIgnoreActionIn",
        "GoogleCloudRetailV2RuleIgnoreActionOut": "_retail_251_GoogleCloudRetailV2RuleIgnoreActionOut",
        "GoogleCloudRetailV2SearchRequestPersonalizationSpecIn": "_retail_252_GoogleCloudRetailV2SearchRequestPersonalizationSpecIn",
        "GoogleCloudRetailV2SearchRequestPersonalizationSpecOut": "_retail_253_GoogleCloudRetailV2SearchRequestPersonalizationSpecOut",
        "GoogleCloudRetailV2AddLocalInventoriesResponseIn": "_retail_254_GoogleCloudRetailV2AddLocalInventoriesResponseIn",
        "GoogleCloudRetailV2AddLocalInventoriesResponseOut": "_retail_255_GoogleCloudRetailV2AddLocalInventoriesResponseOut",
        "GoogleCloudRetailV2alphaPurgeMetadataIn": "_retail_256_GoogleCloudRetailV2alphaPurgeMetadataIn",
        "GoogleCloudRetailV2alphaPurgeMetadataOut": "_retail_257_GoogleCloudRetailV2alphaPurgeMetadataOut",
        "GoogleCloudRetailV2betaRemoveLocalInventoriesResponseIn": "_retail_258_GoogleCloudRetailV2betaRemoveLocalInventoriesResponseIn",
        "GoogleCloudRetailV2betaRemoveLocalInventoriesResponseOut": "_retail_259_GoogleCloudRetailV2betaRemoveLocalInventoriesResponseOut",
        "GoogleCloudRetailV2betaAddFulfillmentPlacesResponseIn": "_retail_260_GoogleCloudRetailV2betaAddFulfillmentPlacesResponseIn",
        "GoogleCloudRetailV2betaAddFulfillmentPlacesResponseOut": "_retail_261_GoogleCloudRetailV2betaAddFulfillmentPlacesResponseOut",
        "GoogleCloudRetailV2betaPurgeMetadataIn": "_retail_262_GoogleCloudRetailV2betaPurgeMetadataIn",
        "GoogleCloudRetailV2betaPurgeMetadataOut": "_retail_263_GoogleCloudRetailV2betaPurgeMetadataOut",
        "GoogleCloudRetailV2CompleteQueryResponseIn": "_retail_264_GoogleCloudRetailV2CompleteQueryResponseIn",
        "GoogleCloudRetailV2CompleteQueryResponseOut": "_retail_265_GoogleCloudRetailV2CompleteQueryResponseOut",
        "GoogleCloudRetailV2AddFulfillmentPlacesResponseIn": "_retail_266_GoogleCloudRetailV2AddFulfillmentPlacesResponseIn",
        "GoogleCloudRetailV2AddFulfillmentPlacesResponseOut": "_retail_267_GoogleCloudRetailV2AddFulfillmentPlacesResponseOut",
        "GoogleCloudRetailV2betaPurgeProductsMetadataIn": "_retail_268_GoogleCloudRetailV2betaPurgeProductsMetadataIn",
        "GoogleCloudRetailV2betaPurgeProductsMetadataOut": "_retail_269_GoogleCloudRetailV2betaPurgeProductsMetadataOut",
        "GoogleCloudRetailV2betaImportErrorsConfigIn": "_retail_270_GoogleCloudRetailV2betaImportErrorsConfigIn",
        "GoogleCloudRetailV2betaImportErrorsConfigOut": "_retail_271_GoogleCloudRetailV2betaImportErrorsConfigOut",
        "GoogleCloudRetailV2betaAddLocalInventoriesResponseIn": "_retail_272_GoogleCloudRetailV2betaAddLocalInventoriesResponseIn",
        "GoogleCloudRetailV2betaAddLocalInventoriesResponseOut": "_retail_273_GoogleCloudRetailV2betaAddLocalInventoriesResponseOut",
        "GoogleCloudRetailLoggingSourceLocationIn": "_retail_274_GoogleCloudRetailLoggingSourceLocationIn",
        "GoogleCloudRetailLoggingSourceLocationOut": "_retail_275_GoogleCloudRetailLoggingSourceLocationOut",
        "GoogleCloudRetailV2alphaUserEventImportSummaryIn": "_retail_276_GoogleCloudRetailV2alphaUserEventImportSummaryIn",
        "GoogleCloudRetailV2alphaUserEventImportSummaryOut": "_retail_277_GoogleCloudRetailV2alphaUserEventImportSummaryOut",
        "GoogleCloudRetailV2ExperimentInfoIn": "_retail_278_GoogleCloudRetailV2ExperimentInfoIn",
        "GoogleCloudRetailV2ExperimentInfoOut": "_retail_279_GoogleCloudRetailV2ExperimentInfoOut",
        "GoogleCloudRetailV2RuleFilterActionIn": "_retail_280_GoogleCloudRetailV2RuleFilterActionIn",
        "GoogleCloudRetailV2RuleFilterActionOut": "_retail_281_GoogleCloudRetailV2RuleFilterActionOut",
        "GoogleCloudRetailV2PriceInfoPriceRangeIn": "_retail_282_GoogleCloudRetailV2PriceInfoPriceRangeIn",
        "GoogleCloudRetailV2PriceInfoPriceRangeOut": "_retail_283_GoogleCloudRetailV2PriceInfoPriceRangeOut",
        "GoogleCloudRetailV2betaGcsOutputResultIn": "_retail_284_GoogleCloudRetailV2betaGcsOutputResultIn",
        "GoogleCloudRetailV2betaGcsOutputResultOut": "_retail_285_GoogleCloudRetailV2betaGcsOutputResultOut",
        "GoogleCloudRetailV2PurgeMetadataIn": "_retail_286_GoogleCloudRetailV2PurgeMetadataIn",
        "GoogleCloudRetailV2PurgeMetadataOut": "_retail_287_GoogleCloudRetailV2PurgeMetadataOut",
        "GoogleCloudRetailV2TuneModelResponseIn": "_retail_288_GoogleCloudRetailV2TuneModelResponseIn",
        "GoogleCloudRetailV2TuneModelResponseOut": "_retail_289_GoogleCloudRetailV2TuneModelResponseOut",
        "GoogleCloudRetailV2CustomAttributeIn": "_retail_290_GoogleCloudRetailV2CustomAttributeIn",
        "GoogleCloudRetailV2CustomAttributeOut": "_retail_291_GoogleCloudRetailV2CustomAttributeOut",
        "GoogleCloudRetailV2betaAddLocalInventoriesMetadataIn": "_retail_292_GoogleCloudRetailV2betaAddLocalInventoriesMetadataIn",
        "GoogleCloudRetailV2betaAddLocalInventoriesMetadataOut": "_retail_293_GoogleCloudRetailV2betaAddLocalInventoriesMetadataOut",
        "GoogleCloudRetailV2ImportCompletionDataResponseIn": "_retail_294_GoogleCloudRetailV2ImportCompletionDataResponseIn",
        "GoogleCloudRetailV2ImportCompletionDataResponseOut": "_retail_295_GoogleCloudRetailV2ImportCompletionDataResponseOut",
        "GoogleCloudRetailV2ProductInputConfigIn": "_retail_296_GoogleCloudRetailV2ProductInputConfigIn",
        "GoogleCloudRetailV2ProductInputConfigOut": "_retail_297_GoogleCloudRetailV2ProductInputConfigOut",
        "GoogleCloudRetailV2SearchRequestIn": "_retail_298_GoogleCloudRetailV2SearchRequestIn",
        "GoogleCloudRetailV2SearchRequestOut": "_retail_299_GoogleCloudRetailV2SearchRequestOut",
        "GoogleCloudRetailV2SearchResponseFacetIn": "_retail_300_GoogleCloudRetailV2SearchResponseFacetIn",
        "GoogleCloudRetailV2SearchResponseFacetOut": "_retail_301_GoogleCloudRetailV2SearchResponseFacetOut",
        "GoogleCloudRetailV2ListServingConfigsResponseIn": "_retail_302_GoogleCloudRetailV2ListServingConfigsResponseIn",
        "GoogleCloudRetailV2ListServingConfigsResponseOut": "_retail_303_GoogleCloudRetailV2ListServingConfigsResponseOut",
        "GoogleCloudRetailV2ResumeModelRequestIn": "_retail_304_GoogleCloudRetailV2ResumeModelRequestIn",
        "GoogleCloudRetailV2ResumeModelRequestOut": "_retail_305_GoogleCloudRetailV2ResumeModelRequestOut",
        "GoogleCloudRetailV2betaSetInventoryResponseIn": "_retail_306_GoogleCloudRetailV2betaSetInventoryResponseIn",
        "GoogleCloudRetailV2betaSetInventoryResponseOut": "_retail_307_GoogleCloudRetailV2betaSetInventoryResponseOut",
        "GoogleCloudRetailV2alphaCreateMerchantCenterAccountLinkMetadataIn": "_retail_308_GoogleCloudRetailV2alphaCreateMerchantCenterAccountLinkMetadataIn",
        "GoogleCloudRetailV2alphaCreateMerchantCenterAccountLinkMetadataOut": "_retail_309_GoogleCloudRetailV2alphaCreateMerchantCenterAccountLinkMetadataOut",
        "GoogleCloudRetailV2SetInventoryRequestIn": "_retail_310_GoogleCloudRetailV2SetInventoryRequestIn",
        "GoogleCloudRetailV2SetInventoryRequestOut": "_retail_311_GoogleCloudRetailV2SetInventoryRequestOut",
        "GoogleCloudRetailV2CompletionDetailIn": "_retail_312_GoogleCloudRetailV2CompletionDetailIn",
        "GoogleCloudRetailV2CompletionDetailOut": "_retail_313_GoogleCloudRetailV2CompletionDetailOut",
        "GoogleCloudRetailV2CompleteQueryResponseRecentSearchResultIn": "_retail_314_GoogleCloudRetailV2CompleteQueryResponseRecentSearchResultIn",
        "GoogleCloudRetailV2CompleteQueryResponseRecentSearchResultOut": "_retail_315_GoogleCloudRetailV2CompleteQueryResponseRecentSearchResultOut",
        "GoogleTypeDateIn": "_retail_316_GoogleTypeDateIn",
        "GoogleTypeDateOut": "_retail_317_GoogleTypeDateOut",
        "GoogleCloudRetailV2alphaAddLocalInventoriesResponseIn": "_retail_318_GoogleCloudRetailV2alphaAddLocalInventoriesResponseIn",
        "GoogleCloudRetailV2alphaAddLocalInventoriesResponseOut": "_retail_319_GoogleCloudRetailV2alphaAddLocalInventoriesResponseOut",
        "GoogleCloudRetailV2PurgeProductsRequestIn": "_retail_320_GoogleCloudRetailV2PurgeProductsRequestIn",
        "GoogleCloudRetailV2PurgeProductsRequestOut": "_retail_321_GoogleCloudRetailV2PurgeProductsRequestOut",
        "GoogleCloudRetailV2alphaCreateModelMetadataIn": "_retail_322_GoogleCloudRetailV2alphaCreateModelMetadataIn",
        "GoogleCloudRetailV2alphaCreateModelMetadataOut": "_retail_323_GoogleCloudRetailV2alphaCreateModelMetadataOut",
        "GoogleCloudRetailV2alphaPurgeUserEventsResponseIn": "_retail_324_GoogleCloudRetailV2alphaPurgeUserEventsResponseIn",
        "GoogleCloudRetailV2alphaPurgeUserEventsResponseOut": "_retail_325_GoogleCloudRetailV2alphaPurgeUserEventsResponseOut",
        "GoogleCloudRetailV2ImportCompletionDataRequestIn": "_retail_326_GoogleCloudRetailV2ImportCompletionDataRequestIn",
        "GoogleCloudRetailV2ImportCompletionDataRequestOut": "_retail_327_GoogleCloudRetailV2ImportCompletionDataRequestOut",
        "GoogleCloudRetailV2betaMerchantCenterAccountLinkIn": "_retail_328_GoogleCloudRetailV2betaMerchantCenterAccountLinkIn",
        "GoogleCloudRetailV2betaMerchantCenterAccountLinkOut": "_retail_329_GoogleCloudRetailV2betaMerchantCenterAccountLinkOut",
        "GoogleCloudRetailV2GetDefaultBranchResponseIn": "_retail_330_GoogleCloudRetailV2GetDefaultBranchResponseIn",
        "GoogleCloudRetailV2GetDefaultBranchResponseOut": "_retail_331_GoogleCloudRetailV2GetDefaultBranchResponseOut",
        "GoogleCloudRetailV2betaTuneModelResponseIn": "_retail_332_GoogleCloudRetailV2betaTuneModelResponseIn",
        "GoogleCloudRetailV2betaTuneModelResponseOut": "_retail_333_GoogleCloudRetailV2betaTuneModelResponseOut",
        "GoogleCloudRetailV2ControlIn": "_retail_334_GoogleCloudRetailV2ControlIn",
        "GoogleCloudRetailV2ControlOut": "_retail_335_GoogleCloudRetailV2ControlOut",
        "GoogleCloudRetailV2PurgeProductsResponseIn": "_retail_336_GoogleCloudRetailV2PurgeProductsResponseIn",
        "GoogleCloudRetailV2PurgeProductsResponseOut": "_retail_337_GoogleCloudRetailV2PurgeProductsResponseOut",
        "GoogleCloudRetailV2PurgeProductsMetadataIn": "_retail_338_GoogleCloudRetailV2PurgeProductsMetadataIn",
        "GoogleCloudRetailV2PurgeProductsMetadataOut": "_retail_339_GoogleCloudRetailV2PurgeProductsMetadataOut",
        "GoogleCloudRetailV2SearchResponseSearchResultIn": "_retail_340_GoogleCloudRetailV2SearchResponseSearchResultIn",
        "GoogleCloudRetailV2SearchResponseSearchResultOut": "_retail_341_GoogleCloudRetailV2SearchResponseSearchResultOut",
        "GoogleCloudRetailV2ExperimentInfoServingConfigExperimentIn": "_retail_342_GoogleCloudRetailV2ExperimentInfoServingConfigExperimentIn",
        "GoogleCloudRetailV2ExperimentInfoServingConfigExperimentOut": "_retail_343_GoogleCloudRetailV2ExperimentInfoServingConfigExperimentOut",
        "GoogleCloudRetailV2ImportProductsResponseIn": "_retail_344_GoogleCloudRetailV2ImportProductsResponseIn",
        "GoogleCloudRetailV2ImportProductsResponseOut": "_retail_345_GoogleCloudRetailV2ImportProductsResponseOut",
        "GoogleCloudRetailV2RemoveFulfillmentPlacesResponseIn": "_retail_346_GoogleCloudRetailV2RemoveFulfillmentPlacesResponseIn",
        "GoogleCloudRetailV2RemoveFulfillmentPlacesResponseOut": "_retail_347_GoogleCloudRetailV2RemoveFulfillmentPlacesResponseOut",
        "GoogleCloudRetailV2SearchRequestDynamicFacetSpecIn": "_retail_348_GoogleCloudRetailV2SearchRequestDynamicFacetSpecIn",
        "GoogleCloudRetailV2SearchRequestDynamicFacetSpecOut": "_retail_349_GoogleCloudRetailV2SearchRequestDynamicFacetSpecOut",
        "GoogleCloudRetailV2ProductInlineSourceIn": "_retail_350_GoogleCloudRetailV2ProductInlineSourceIn",
        "GoogleCloudRetailV2ProductInlineSourceOut": "_retail_351_GoogleCloudRetailV2ProductInlineSourceOut",
        "GoogleCloudRetailV2ModelIn": "_retail_352_GoogleCloudRetailV2ModelIn",
        "GoogleCloudRetailV2ModelOut": "_retail_353_GoogleCloudRetailV2ModelOut",
        "GoogleCloudRetailV2PredictResponsePredictionResultIn": "_retail_354_GoogleCloudRetailV2PredictResponsePredictionResultIn",
        "GoogleCloudRetailV2PredictResponsePredictionResultOut": "_retail_355_GoogleCloudRetailV2PredictResponsePredictionResultOut",
        "GoogleCloudRetailV2betaUserEventImportSummaryIn": "_retail_356_GoogleCloudRetailV2betaUserEventImportSummaryIn",
        "GoogleCloudRetailV2betaUserEventImportSummaryOut": "_retail_357_GoogleCloudRetailV2betaUserEventImportSummaryOut",
        "GoogleCloudRetailV2betaRemoveFulfillmentPlacesMetadataIn": "_retail_358_GoogleCloudRetailV2betaRemoveFulfillmentPlacesMetadataIn",
        "GoogleCloudRetailV2betaRemoveFulfillmentPlacesMetadataOut": "_retail_359_GoogleCloudRetailV2betaRemoveFulfillmentPlacesMetadataOut",
        "GoogleCloudRetailV2ConditionTimeRangeIn": "_retail_360_GoogleCloudRetailV2ConditionTimeRangeIn",
        "GoogleCloudRetailV2ConditionTimeRangeOut": "_retail_361_GoogleCloudRetailV2ConditionTimeRangeOut",
        "GoogleCloudRetailV2alphaSetInventoryResponseIn": "_retail_362_GoogleCloudRetailV2alphaSetInventoryResponseIn",
        "GoogleCloudRetailV2alphaSetInventoryResponseOut": "_retail_363_GoogleCloudRetailV2alphaSetInventoryResponseOut",
        "GoogleCloudRetailV2SearchRequestSpellCorrectionSpecIn": "_retail_364_GoogleCloudRetailV2SearchRequestSpellCorrectionSpecIn",
        "GoogleCloudRetailV2SearchRequestSpellCorrectionSpecOut": "_retail_365_GoogleCloudRetailV2SearchRequestSpellCorrectionSpecOut",
        "GoogleCloudRetailV2alphaBigQueryOutputResultIn": "_retail_366_GoogleCloudRetailV2alphaBigQueryOutputResultIn",
        "GoogleCloudRetailV2alphaBigQueryOutputResultOut": "_retail_367_GoogleCloudRetailV2alphaBigQueryOutputResultOut",
        "GoogleCloudRetailV2alphaModelServingConfigListIn": "_retail_368_GoogleCloudRetailV2alphaModelServingConfigListIn",
        "GoogleCloudRetailV2alphaModelServingConfigListOut": "_retail_369_GoogleCloudRetailV2alphaModelServingConfigListOut",
        "GoogleCloudRetailV2alphaExportProductsResponseIn": "_retail_370_GoogleCloudRetailV2alphaExportProductsResponseIn",
        "GoogleCloudRetailV2alphaExportProductsResponseOut": "_retail_371_GoogleCloudRetailV2alphaExportProductsResponseOut",
        "GoogleCloudRetailV2betaExportErrorsConfigIn": "_retail_372_GoogleCloudRetailV2betaExportErrorsConfigIn",
        "GoogleCloudRetailV2betaExportErrorsConfigOut": "_retail_373_GoogleCloudRetailV2betaExportErrorsConfigOut",
        "GoogleCloudRetailV2PurchaseTransactionIn": "_retail_374_GoogleCloudRetailV2PurchaseTransactionIn",
        "GoogleCloudRetailV2PurchaseTransactionOut": "_retail_375_GoogleCloudRetailV2PurchaseTransactionOut",
        "GoogleCloudRetailV2alphaRemoveFulfillmentPlacesMetadataIn": "_retail_376_GoogleCloudRetailV2alphaRemoveFulfillmentPlacesMetadataIn",
        "GoogleCloudRetailV2alphaRemoveFulfillmentPlacesMetadataOut": "_retail_377_GoogleCloudRetailV2alphaRemoveFulfillmentPlacesMetadataOut",
        "GoogleCloudRetailV2alphaImportMetadataIn": "_retail_378_GoogleCloudRetailV2alphaImportMetadataIn",
        "GoogleCloudRetailV2alphaImportMetadataOut": "_retail_379_GoogleCloudRetailV2alphaImportMetadataOut",
        "GoogleCloudRetailV2alphaModelPageOptimizationConfigIn": "_retail_380_GoogleCloudRetailV2alphaModelPageOptimizationConfigIn",
        "GoogleCloudRetailV2alphaModelPageOptimizationConfigOut": "_retail_381_GoogleCloudRetailV2alphaModelPageOptimizationConfigOut",
        "GoogleCloudRetailV2betaPurgeProductsResponseIn": "_retail_382_GoogleCloudRetailV2betaPurgeProductsResponseIn",
        "GoogleCloudRetailV2betaPurgeProductsResponseOut": "_retail_383_GoogleCloudRetailV2betaPurgeProductsResponseOut",
        "GoogleCloudRetailV2alphaModelPageOptimizationConfigCandidateIn": "_retail_384_GoogleCloudRetailV2alphaModelPageOptimizationConfigCandidateIn",
        "GoogleCloudRetailV2alphaModelPageOptimizationConfigCandidateOut": "_retail_385_GoogleCloudRetailV2alphaModelPageOptimizationConfigCandidateOut",
        "GoogleCloudRetailV2BigQuerySourceIn": "_retail_386_GoogleCloudRetailV2BigQuerySourceIn",
        "GoogleCloudRetailV2BigQuerySourceOut": "_retail_387_GoogleCloudRetailV2BigQuerySourceOut",
        "GoogleCloudRetailV2alphaExportMetadataIn": "_retail_388_GoogleCloudRetailV2alphaExportMetadataIn",
        "GoogleCloudRetailV2alphaExportMetadataOut": "_retail_389_GoogleCloudRetailV2alphaExportMetadataOut",
        "GoogleCloudRetailV2RemoveLocalInventoriesRequestIn": "_retail_390_GoogleCloudRetailV2RemoveLocalInventoriesRequestIn",
        "GoogleCloudRetailV2RemoveLocalInventoriesRequestOut": "_retail_391_GoogleCloudRetailV2RemoveLocalInventoriesRequestOut",
        "GoogleCloudRetailV2betaRejoinUserEventsResponseIn": "_retail_392_GoogleCloudRetailV2betaRejoinUserEventsResponseIn",
        "GoogleCloudRetailV2betaRejoinUserEventsResponseOut": "_retail_393_GoogleCloudRetailV2betaRejoinUserEventsResponseOut",
        "GoogleCloudRetailV2RejoinUserEventsResponseIn": "_retail_394_GoogleCloudRetailV2RejoinUserEventsResponseIn",
        "GoogleCloudRetailV2RejoinUserEventsResponseOut": "_retail_395_GoogleCloudRetailV2RejoinUserEventsResponseOut",
        "GoogleCloudRetailV2alphaImportProductsResponseIn": "_retail_396_GoogleCloudRetailV2alphaImportProductsResponseIn",
        "GoogleCloudRetailV2alphaImportProductsResponseOut": "_retail_397_GoogleCloudRetailV2alphaImportProductsResponseOut",
        "GoogleCloudRetailV2PurgeUserEventsRequestIn": "_retail_398_GoogleCloudRetailV2PurgeUserEventsRequestIn",
        "GoogleCloudRetailV2PurgeUserEventsRequestOut": "_retail_399_GoogleCloudRetailV2PurgeUserEventsRequestOut",
        "GoogleCloudRetailV2ColorInfoIn": "_retail_400_GoogleCloudRetailV2ColorInfoIn",
        "GoogleCloudRetailV2ColorInfoOut": "_retail_401_GoogleCloudRetailV2ColorInfoOut",
        "GoogleLongrunningOperationIn": "_retail_402_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_retail_403_GoogleLongrunningOperationOut",
        "GoogleCloudRetailV2alphaOutputResultIn": "_retail_404_GoogleCloudRetailV2alphaOutputResultIn",
        "GoogleCloudRetailV2alphaOutputResultOut": "_retail_405_GoogleCloudRetailV2alphaOutputResultOut",
        "GoogleCloudRetailV2betaBigQueryOutputResultIn": "_retail_406_GoogleCloudRetailV2betaBigQueryOutputResultIn",
        "GoogleCloudRetailV2betaBigQueryOutputResultOut": "_retail_407_GoogleCloudRetailV2betaBigQueryOutputResultOut",
        "GoogleCloudRetailV2SearchResponseQueryExpansionInfoIn": "_retail_408_GoogleCloudRetailV2SearchResponseQueryExpansionInfoIn",
        "GoogleCloudRetailV2SearchResponseQueryExpansionInfoOut": "_retail_409_GoogleCloudRetailV2SearchResponseQueryExpansionInfoOut",
        "GoogleCloudRetailV2RejoinUserEventsRequestIn": "_retail_410_GoogleCloudRetailV2RejoinUserEventsRequestIn",
        "GoogleCloudRetailV2RejoinUserEventsRequestOut": "_retail_411_GoogleCloudRetailV2RejoinUserEventsRequestOut",
        "GoogleCloudRetailV2RuleOnewaySynonymsActionIn": "_retail_412_GoogleCloudRetailV2RuleOnewaySynonymsActionIn",
        "GoogleCloudRetailV2RuleOnewaySynonymsActionOut": "_retail_413_GoogleCloudRetailV2RuleOnewaySynonymsActionOut",
        "GoogleCloudRetailV2alphaMerchantCenterAccountLinkIn": "_retail_414_GoogleCloudRetailV2alphaMerchantCenterAccountLinkIn",
        "GoogleCloudRetailV2alphaMerchantCenterAccountLinkOut": "_retail_415_GoogleCloudRetailV2alphaMerchantCenterAccountLinkOut",
        "GoogleCloudRetailV2betaModelFrequentlyBoughtTogetherFeaturesConfigIn": "_retail_416_GoogleCloudRetailV2betaModelFrequentlyBoughtTogetherFeaturesConfigIn",
        "GoogleCloudRetailV2betaModelFrequentlyBoughtTogetherFeaturesConfigOut": "_retail_417_GoogleCloudRetailV2betaModelFrequentlyBoughtTogetherFeaturesConfigOut",
        "GoogleCloudRetailV2ImportUserEventsResponseIn": "_retail_418_GoogleCloudRetailV2ImportUserEventsResponseIn",
        "GoogleCloudRetailV2ImportUserEventsResponseOut": "_retail_419_GoogleCloudRetailV2ImportUserEventsResponseOut",
        "GoogleCloudRetailV2betaCreateModelMetadataIn": "_retail_420_GoogleCloudRetailV2betaCreateModelMetadataIn",
        "GoogleCloudRetailV2betaCreateModelMetadataOut": "_retail_421_GoogleCloudRetailV2betaCreateModelMetadataOut",
        "GoogleCloudRetailV2UserInfoIn": "_retail_422_GoogleCloudRetailV2UserInfoIn",
        "GoogleCloudRetailV2UserInfoOut": "_retail_423_GoogleCloudRetailV2UserInfoOut",
        "GoogleCloudRetailV2AttributesConfigIn": "_retail_424_GoogleCloudRetailV2AttributesConfigIn",
        "GoogleCloudRetailV2AttributesConfigOut": "_retail_425_GoogleCloudRetailV2AttributesConfigOut",
        "GoogleCloudRetailV2ModelModelFeaturesConfigIn": "_retail_426_GoogleCloudRetailV2ModelModelFeaturesConfigIn",
        "GoogleCloudRetailV2ModelModelFeaturesConfigOut": "_retail_427_GoogleCloudRetailV2ModelModelFeaturesConfigOut",
        "GoogleCloudRetailV2SearchRequestBoostSpecIn": "_retail_428_GoogleCloudRetailV2SearchRequestBoostSpecIn",
        "GoogleCloudRetailV2SearchRequestBoostSpecOut": "_retail_429_GoogleCloudRetailV2SearchRequestBoostSpecOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudRetailV2alphaSetInventoryMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2alphaSetInventoryMetadataIn"])
    types["GoogleCloudRetailV2alphaSetInventoryMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2alphaSetInventoryMetadataOut"])
    types["GoogleCloudRetailV2ConditionQueryTermIn"] = t.struct(
        {"value": t.string().optional(), "fullMatch": t.boolean().optional()}
    ).named(renames["GoogleCloudRetailV2ConditionQueryTermIn"])
    types["GoogleCloudRetailV2ConditionQueryTermOut"] = t.struct(
        {
            "value": t.string().optional(),
            "fullMatch": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ConditionQueryTermOut"])
    types["GoogleCloudRetailV2GcsSourceIn"] = t.struct(
        {"dataSchema": t.string().optional(), "inputUris": t.array(t.string())}
    ).named(renames["GoogleCloudRetailV2GcsSourceIn"])
    types["GoogleCloudRetailV2GcsSourceOut"] = t.struct(
        {
            "dataSchema": t.string().optional(),
            "inputUris": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2GcsSourceOut"])
    types["GoogleCloudRetailLoggingServiceContextIn"] = t.struct(
        {"service": t.string().optional()}
    ).named(renames["GoogleCloudRetailLoggingServiceContextIn"])
    types["GoogleCloudRetailLoggingServiceContextOut"] = t.struct(
        {
            "service": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailLoggingServiceContextOut"])
    types["GoogleCloudRetailV2alphaTuneModelMetadataIn"] = t.struct(
        {"model": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2alphaTuneModelMetadataIn"])
    types["GoogleCloudRetailV2alphaTuneModelMetadataOut"] = t.struct(
        {
            "model": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaTuneModelMetadataOut"])
    types["GoogleCloudRetailV2TuneModelRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2TuneModelRequestIn"])
    types["GoogleCloudRetailV2TuneModelRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2TuneModelRequestOut"])
    types["GoogleCloudRetailV2PredictRequestIn"] = t.struct(
        {
            "validateOnly": t.boolean().optional(),
            "filter": t.string().optional(),
            "userEvent": t.proxy(renames["GoogleCloudRetailV2UserEventIn"]),
            "params": t.struct({"_": t.string().optional()}).optional(),
            "pageToken": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "pageSize": t.integer().optional(),
        }
    ).named(renames["GoogleCloudRetailV2PredictRequestIn"])
    types["GoogleCloudRetailV2PredictRequestOut"] = t.struct(
        {
            "validateOnly": t.boolean().optional(),
            "filter": t.string().optional(),
            "userEvent": t.proxy(renames["GoogleCloudRetailV2UserEventOut"]),
            "params": t.struct({"_": t.string().optional()}).optional(),
            "pageToken": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "pageSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2PredictRequestOut"])
    types["GoogleCloudRetailV2alphaExportErrorsConfigIn"] = t.struct(
        {"gcsPrefix": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2alphaExportErrorsConfigIn"])
    types["GoogleCloudRetailV2alphaExportErrorsConfigOut"] = t.struct(
        {
            "gcsPrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaExportErrorsConfigOut"])
    types["GoogleCloudRetailV2UserEventImportSummaryIn"] = t.struct(
        {
            "joinedEventsCount": t.string().optional(),
            "unjoinedEventsCount": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2UserEventImportSummaryIn"])
    types["GoogleCloudRetailV2UserEventImportSummaryOut"] = t.struct(
        {
            "joinedEventsCount": t.string().optional(),
            "unjoinedEventsCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2UserEventImportSummaryOut"])
    types["GoogleCloudRetailV2alphaTuneModelResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2alphaTuneModelResponseIn"])
    types["GoogleCloudRetailV2alphaTuneModelResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2alphaTuneModelResponseOut"])
    types["GoogleCloudRetailV2AddFulfillmentPlacesMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2AddFulfillmentPlacesMetadataIn"])
    types["GoogleCloudRetailV2AddFulfillmentPlacesMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2AddFulfillmentPlacesMetadataOut"])
    types["GoogleCloudRetailV2RemoveFulfillmentPlacesMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2RemoveFulfillmentPlacesMetadataIn"])
    types["GoogleCloudRetailV2RemoveFulfillmentPlacesMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2RemoveFulfillmentPlacesMetadataOut"])
    types["GoogleCloudRetailV2alphaModelModelFeaturesConfigIn"] = t.struct(
        {
            "frequentlyBoughtTogetherConfig": t.proxy(
                renames[
                    "GoogleCloudRetailV2alphaModelFrequentlyBoughtTogetherFeaturesConfigIn"
                ]
            ).optional()
        }
    ).named(renames["GoogleCloudRetailV2alphaModelModelFeaturesConfigIn"])
    types["GoogleCloudRetailV2alphaModelModelFeaturesConfigOut"] = t.struct(
        {
            "frequentlyBoughtTogetherConfig": t.proxy(
                renames[
                    "GoogleCloudRetailV2alphaModelFrequentlyBoughtTogetherFeaturesConfigOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaModelModelFeaturesConfigOut"])
    types["GoogleCloudRetailV2SearchRequestFacetSpecIn"] = t.struct(
        {
            "enableDynamicPosition": t.boolean().optional(),
            "limit": t.integer().optional(),
            "facetKey": t.proxy(
                renames["GoogleCloudRetailV2SearchRequestFacetSpecFacetKeyIn"]
            ),
            "excludedFilterKeys": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudRetailV2SearchRequestFacetSpecIn"])
    types["GoogleCloudRetailV2SearchRequestFacetSpecOut"] = t.struct(
        {
            "enableDynamicPosition": t.boolean().optional(),
            "limit": t.integer().optional(),
            "facetKey": t.proxy(
                renames["GoogleCloudRetailV2SearchRequestFacetSpecFacetKeyOut"]
            ),
            "excludedFilterKeys": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2SearchRequestFacetSpecOut"])
    types["GoogleCloudRetailV2alphaAddLocalInventoriesMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2alphaAddLocalInventoriesMetadataIn"])
    types["GoogleCloudRetailV2alphaAddLocalInventoriesMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2alphaAddLocalInventoriesMetadataOut"])
    types["GoogleCloudRetailV2FulfillmentInfoIn"] = t.struct(
        {"type": t.string().optional(), "placeIds": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudRetailV2FulfillmentInfoIn"])
    types["GoogleCloudRetailV2FulfillmentInfoOut"] = t.struct(
        {
            "type": t.string().optional(),
            "placeIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2FulfillmentInfoOut"])
    types["GoogleCloudRetailV2RejoinUserEventsMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2RejoinUserEventsMetadataIn"])
    types["GoogleCloudRetailV2RejoinUserEventsMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2RejoinUserEventsMetadataOut"])
    types["GoogleCloudRetailV2ModelServingConfigListIn"] = t.struct(
        {"servingConfigIds": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudRetailV2ModelServingConfigListIn"])
    types["GoogleCloudRetailV2ModelServingConfigListOut"] = t.struct(
        {
            "servingConfigIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ModelServingConfigListOut"])
    types["GoogleCloudRetailV2betaRemoveFulfillmentPlacesResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2betaRemoveFulfillmentPlacesResponseIn"])
    types["GoogleCloudRetailV2betaRemoveFulfillmentPlacesResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2betaRemoveFulfillmentPlacesResponseOut"])
    types["GoogleCloudRetailV2RuleReplacementActionIn"] = t.struct(
        {
            "term": t.string().optional(),
            "queryTerms": t.array(t.string()).optional(),
            "replacementTerm": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2RuleReplacementActionIn"])
    types["GoogleCloudRetailV2RuleReplacementActionOut"] = t.struct(
        {
            "term": t.string().optional(),
            "queryTerms": t.array(t.string()).optional(),
            "replacementTerm": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2RuleReplacementActionOut"])
    types["GoogleCloudRetailV2ImportMetadataIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "successCount": t.string().optional(),
            "notificationPubsubTopic": t.string().optional(),
            "failureCount": t.string().optional(),
            "createTime": t.string().optional(),
            "requestId": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2ImportMetadataIn"])
    types["GoogleCloudRetailV2ImportMetadataOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "successCount": t.string().optional(),
            "notificationPubsubTopic": t.string().optional(),
            "failureCount": t.string().optional(),
            "createTime": t.string().optional(),
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ImportMetadataOut"])
    types["GoogleCloudRetailV2PromotionIn"] = t.struct(
        {"promotionId": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2PromotionIn"])
    types["GoogleCloudRetailV2PromotionOut"] = t.struct(
        {
            "promotionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2PromotionOut"])
    types["GoogleCloudRetailV2betaModelModelFeaturesConfigIn"] = t.struct(
        {
            "frequentlyBoughtTogetherConfig": t.proxy(
                renames[
                    "GoogleCloudRetailV2betaModelFrequentlyBoughtTogetherFeaturesConfigIn"
                ]
            ).optional()
        }
    ).named(renames["GoogleCloudRetailV2betaModelModelFeaturesConfigIn"])
    types["GoogleCloudRetailV2betaModelModelFeaturesConfigOut"] = t.struct(
        {
            "frequentlyBoughtTogetherConfig": t.proxy(
                renames[
                    "GoogleCloudRetailV2betaModelFrequentlyBoughtTogetherFeaturesConfigOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2betaModelModelFeaturesConfigOut"])
    types["GoogleCloudRetailV2alphaPurgeProductsMetadataIn"] = t.struct(
        {
            "successCount": t.string().optional(),
            "createTime": t.string().optional(),
            "failureCount": t.string().optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaPurgeProductsMetadataIn"])
    types["GoogleCloudRetailV2alphaPurgeProductsMetadataOut"] = t.struct(
        {
            "successCount": t.string().optional(),
            "createTime": t.string().optional(),
            "failureCount": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaPurgeProductsMetadataOut"])
    types[
        "GoogleCloudRetailV2alphaModelFrequentlyBoughtTogetherFeaturesConfigIn"
    ] = t.struct({"contextProductsType": t.string().optional()}).named(
        renames["GoogleCloudRetailV2alphaModelFrequentlyBoughtTogetherFeaturesConfigIn"]
    )
    types[
        "GoogleCloudRetailV2alphaModelFrequentlyBoughtTogetherFeaturesConfigOut"
    ] = t.struct(
        {
            "contextProductsType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudRetailV2alphaModelFrequentlyBoughtTogetherFeaturesConfigOut"
        ]
    )
    types["GoogleCloudRetailV2ListCatalogsResponseIn"] = t.struct(
        {
            "catalogs": t.array(
                t.proxy(renames["GoogleCloudRetailV2CatalogIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2ListCatalogsResponseIn"])
    types["GoogleCloudRetailV2ListCatalogsResponseOut"] = t.struct(
        {
            "catalogs": t.array(
                t.proxy(renames["GoogleCloudRetailV2CatalogOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ListCatalogsResponseOut"])
    types["GoogleCloudRetailV2betaModelIn"] = t.struct(
        {
            "type": t.string(),
            "displayName": t.string(),
            "periodicTuningState": t.string().optional(),
            "name": t.string(),
            "modelFeaturesConfig": t.proxy(
                renames["GoogleCloudRetailV2betaModelModelFeaturesConfigIn"]
            ).optional(),
            "trainingState": t.string().optional(),
            "filteringOption": t.string().optional(),
            "optimizationObjective": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2betaModelIn"])
    types["GoogleCloudRetailV2betaModelOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "type": t.string(),
            "displayName": t.string(),
            "periodicTuningState": t.string().optional(),
            "servingState": t.string().optional(),
            "servingConfigLists": t.array(
                t.proxy(renames["GoogleCloudRetailV2betaModelServingConfigListOut"])
            ).optional(),
            "createTime": t.string().optional(),
            "tuningOperation": t.string().optional(),
            "name": t.string(),
            "modelFeaturesConfig": t.proxy(
                renames["GoogleCloudRetailV2betaModelModelFeaturesConfigOut"]
            ).optional(),
            "lastTuneTime": t.string().optional(),
            "trainingState": t.string().optional(),
            "filteringOption": t.string().optional(),
            "dataState": t.string().optional(),
            "optimizationObjective": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2betaModelOut"])
    types["GoogleCloudRetailV2AddCatalogAttributeRequestIn"] = t.struct(
        {"catalogAttribute": t.proxy(renames["GoogleCloudRetailV2CatalogAttributeIn"])}
    ).named(renames["GoogleCloudRetailV2AddCatalogAttributeRequestIn"])
    types["GoogleCloudRetailV2AddCatalogAttributeRequestOut"] = t.struct(
        {
            "catalogAttribute": t.proxy(
                renames["GoogleCloudRetailV2CatalogAttributeOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2AddCatalogAttributeRequestOut"])
    types["GoogleCloudRetailV2ServingConfigIn"] = t.struct(
        {
            "diversityLevel": t.string().optional(),
            "solutionTypes": t.array(t.string()),
            "diversityType": t.string().optional(),
            "redirectControlIds": t.array(t.string()).optional(),
            "displayName": t.string(),
            "boostControlIds": t.array(t.string()).optional(),
            "dynamicFacetSpec": t.proxy(
                renames["GoogleCloudRetailV2SearchRequestDynamicFacetSpecIn"]
            ).optional(),
            "enableCategoryFilterLevel": t.string().optional(),
            "twowaySynonymsControlIds": t.array(t.string()).optional(),
            "doNotAssociateControlIds": t.array(t.string()).optional(),
            "onewaySynonymsControlIds": t.array(t.string()).optional(),
            "ignoreControlIds": t.array(t.string()).optional(),
            "facetControlIds": t.array(t.string()).optional(),
            "priceRerankingLevel": t.string().optional(),
            "personalizationSpec": t.proxy(
                renames["GoogleCloudRetailV2SearchRequestPersonalizationSpecIn"]
            ).optional(),
            "replacementControlIds": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "modelId": t.string().optional(),
            "filterControlIds": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ServingConfigIn"])
    types["GoogleCloudRetailV2ServingConfigOut"] = t.struct(
        {
            "diversityLevel": t.string().optional(),
            "solutionTypes": t.array(t.string()),
            "diversityType": t.string().optional(),
            "redirectControlIds": t.array(t.string()).optional(),
            "displayName": t.string(),
            "boostControlIds": t.array(t.string()).optional(),
            "dynamicFacetSpec": t.proxy(
                renames["GoogleCloudRetailV2SearchRequestDynamicFacetSpecOut"]
            ).optional(),
            "enableCategoryFilterLevel": t.string().optional(),
            "twowaySynonymsControlIds": t.array(t.string()).optional(),
            "doNotAssociateControlIds": t.array(t.string()).optional(),
            "onewaySynonymsControlIds": t.array(t.string()).optional(),
            "ignoreControlIds": t.array(t.string()).optional(),
            "facetControlIds": t.array(t.string()).optional(),
            "priceRerankingLevel": t.string().optional(),
            "personalizationSpec": t.proxy(
                renames["GoogleCloudRetailV2SearchRequestPersonalizationSpecOut"]
            ).optional(),
            "replacementControlIds": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "modelId": t.string().optional(),
            "filterControlIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ServingConfigOut"])
    types["GoogleCloudRetailV2AddLocalInventoriesMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2AddLocalInventoriesMetadataIn"])
    types["GoogleCloudRetailV2AddLocalInventoriesMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2AddLocalInventoriesMetadataOut"])
    types["GoogleCloudRetailV2SearchRequestBoostSpecConditionBoostSpecIn"] = t.struct(
        {"boost": t.number().optional(), "condition": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2SearchRequestBoostSpecConditionBoostSpecIn"])
    types["GoogleCloudRetailV2SearchRequestBoostSpecConditionBoostSpecOut"] = t.struct(
        {
            "boost": t.number().optional(),
            "condition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2SearchRequestBoostSpecConditionBoostSpecOut"])
    types["GoogleCloudRetailV2ProductLevelConfigIn"] = t.struct(
        {
            "merchantCenterProductIdField": t.string().optional(),
            "ingestionProductType": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2ProductLevelConfigIn"])
    types["GoogleCloudRetailV2ProductLevelConfigOut"] = t.struct(
        {
            "merchantCenterProductIdField": t.string().optional(),
            "ingestionProductType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ProductLevelConfigOut"])
    types["GoogleCloudRetailV2ListProductsResponseIn"] = t.struct(
        {
            "products": t.array(
                t.proxy(renames["GoogleCloudRetailV2ProductIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2ListProductsResponseIn"])
    types["GoogleCloudRetailV2ListProductsResponseOut"] = t.struct(
        {
            "products": t.array(
                t.proxy(renames["GoogleCloudRetailV2ProductOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ListProductsResponseOut"])
    types["GoogleCloudRetailV2alphaRemoveFulfillmentPlacesResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2alphaRemoveFulfillmentPlacesResponseIn"])
    types["GoogleCloudRetailV2alphaRemoveFulfillmentPlacesResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2alphaRemoveFulfillmentPlacesResponseOut"])
    types["GoogleCloudRetailV2RuleDoNotAssociateActionIn"] = t.struct(
        {
            "doNotAssociateTerms": t.array(t.string()).optional(),
            "terms": t.array(t.string()).optional(),
            "queryTerms": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudRetailV2RuleDoNotAssociateActionIn"])
    types["GoogleCloudRetailV2RuleDoNotAssociateActionOut"] = t.struct(
        {
            "doNotAssociateTerms": t.array(t.string()).optional(),
            "terms": t.array(t.string()).optional(),
            "queryTerms": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2RuleDoNotAssociateActionOut"])
    types["GoogleCloudRetailV2betaModelServingConfigListIn"] = t.struct(
        {"servingConfigIds": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudRetailV2betaModelServingConfigListIn"])
    types["GoogleCloudRetailV2betaModelServingConfigListOut"] = t.struct(
        {
            "servingConfigIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2betaModelServingConfigListOut"])
    types["GoogleCloudRetailLoggingHttpRequestContextIn"] = t.struct(
        {"responseStatusCode": t.integer().optional()}
    ).named(renames["GoogleCloudRetailLoggingHttpRequestContextIn"])
    types["GoogleCloudRetailLoggingHttpRequestContextOut"] = t.struct(
        {
            "responseStatusCode": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailLoggingHttpRequestContextOut"])
    types["GoogleCloudRetailV2CompleteQueryResponseCompletionResultIn"] = t.struct(
        {
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "suggestion": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2CompleteQueryResponseCompletionResultIn"])
    types["GoogleCloudRetailV2CompleteQueryResponseCompletionResultOut"] = t.struct(
        {
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "suggestion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2CompleteQueryResponseCompletionResultOut"])
    types["GoogleCloudRetailV2betaImportProductsResponseIn"] = t.struct(
        {
            "errorsConfig": t.proxy(
                renames["GoogleCloudRetailV2betaImportErrorsConfigIn"]
            ).optional(),
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional(),
        }
    ).named(renames["GoogleCloudRetailV2betaImportProductsResponseIn"])
    types["GoogleCloudRetailV2betaImportProductsResponseOut"] = t.struct(
        {
            "errorsConfig": t.proxy(
                renames["GoogleCloudRetailV2betaImportErrorsConfigOut"]
            ).optional(),
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2betaImportProductsResponseOut"])
    types["GoogleCloudRetailV2UserEventInputConfigIn"] = t.struct(
        {
            "gcsSource": t.proxy(renames["GoogleCloudRetailV2GcsSourceIn"]),
            "userEventInlineSource": t.proxy(
                renames["GoogleCloudRetailV2UserEventInlineSourceIn"]
            ),
            "bigQuerySource": t.proxy(renames["GoogleCloudRetailV2BigQuerySourceIn"]),
        }
    ).named(renames["GoogleCloudRetailV2UserEventInputConfigIn"])
    types["GoogleCloudRetailV2UserEventInputConfigOut"] = t.struct(
        {
            "gcsSource": t.proxy(renames["GoogleCloudRetailV2GcsSourceOut"]),
            "userEventInlineSource": t.proxy(
                renames["GoogleCloudRetailV2UserEventInlineSourceOut"]
            ),
            "bigQuerySource": t.proxy(renames["GoogleCloudRetailV2BigQuerySourceOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2UserEventInputConfigOut"])
    types["GoogleCloudRetailV2SearchResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "facets": t.array(
                t.proxy(renames["GoogleCloudRetailV2SearchResponseFacetIn"])
            ).optional(),
            "experimentInfo": t.array(
                t.proxy(renames["GoogleCloudRetailV2ExperimentInfoIn"])
            ).optional(),
            "queryExpansionInfo": t.proxy(
                renames["GoogleCloudRetailV2SearchResponseQueryExpansionInfoIn"]
            ).optional(),
            "correctedQuery": t.string().optional(),
            "appliedControls": t.array(t.string()).optional(),
            "results": t.array(
                t.proxy(renames["GoogleCloudRetailV2SearchResponseSearchResultIn"])
            ).optional(),
            "totalSize": t.integer().optional(),
            "redirectUri": t.string().optional(),
            "invalidConditionBoostSpecs": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudRetailV2SearchRequestBoostSpecConditionBoostSpecIn"
                    ]
                )
            ).optional(),
            "attributionToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2SearchResponseIn"])
    types["GoogleCloudRetailV2SearchResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "facets": t.array(
                t.proxy(renames["GoogleCloudRetailV2SearchResponseFacetOut"])
            ).optional(),
            "experimentInfo": t.array(
                t.proxy(renames["GoogleCloudRetailV2ExperimentInfoOut"])
            ).optional(),
            "queryExpansionInfo": t.proxy(
                renames["GoogleCloudRetailV2SearchResponseQueryExpansionInfoOut"]
            ).optional(),
            "correctedQuery": t.string().optional(),
            "appliedControls": t.array(t.string()).optional(),
            "results": t.array(
                t.proxy(renames["GoogleCloudRetailV2SearchResponseSearchResultOut"])
            ).optional(),
            "totalSize": t.integer().optional(),
            "redirectUri": t.string().optional(),
            "invalidConditionBoostSpecs": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudRetailV2SearchRequestBoostSpecConditionBoostSpecOut"
                    ]
                )
            ).optional(),
            "attributionToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2SearchResponseOut"])
    types["GoogleCloudRetailV2PredictResponseIn"] = t.struct(
        {
            "attributionToken": t.string().optional(),
            "results": t.array(
                t.proxy(renames["GoogleCloudRetailV2PredictResponsePredictionResultIn"])
            ).optional(),
            "validateOnly": t.boolean().optional(),
            "missingIds": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudRetailV2PredictResponseIn"])
    types["GoogleCloudRetailV2PredictResponseOut"] = t.struct(
        {
            "attributionToken": t.string().optional(),
            "results": t.array(
                t.proxy(
                    renames["GoogleCloudRetailV2PredictResponsePredictionResultOut"]
                )
            ).optional(),
            "validateOnly": t.boolean().optional(),
            "missingIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2PredictResponseOut"])
    types["GoogleCloudRetailV2betaRejoinUserEventsMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2betaRejoinUserEventsMetadataIn"])
    types["GoogleCloudRetailV2betaRejoinUserEventsMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2betaRejoinUserEventsMetadataOut"])
    types["GoogleCloudRetailV2alphaTransformedUserEventsMetadataIn"] = t.struct(
        {
            "sourceEventsCount": t.string().optional(),
            "transformedEventsCount": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaTransformedUserEventsMetadataIn"])
    types["GoogleCloudRetailV2alphaTransformedUserEventsMetadataOut"] = t.struct(
        {
            "sourceEventsCount": t.string().optional(),
            "transformedEventsCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaTransformedUserEventsMetadataOut"])
    types["GoogleCloudRetailV2alphaModelPageOptimizationConfigPanelIn"] = t.struct(
        {
            "defaultCandidate": t.proxy(
                renames[
                    "GoogleCloudRetailV2alphaModelPageOptimizationConfigCandidateIn"
                ]
            ),
            "displayName": t.string().optional(),
            "candidates": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudRetailV2alphaModelPageOptimizationConfigCandidateIn"
                    ]
                )
            ),
        }
    ).named(renames["GoogleCloudRetailV2alphaModelPageOptimizationConfigPanelIn"])
    types["GoogleCloudRetailV2alphaModelPageOptimizationConfigPanelOut"] = t.struct(
        {
            "defaultCandidate": t.proxy(
                renames[
                    "GoogleCloudRetailV2alphaModelPageOptimizationConfigCandidateOut"
                ]
            ),
            "displayName": t.string().optional(),
            "candidates": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudRetailV2alphaModelPageOptimizationConfigCandidateOut"
                    ]
                )
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaModelPageOptimizationConfigPanelOut"])
    types["GoogleCloudRetailV2betaSetInventoryMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2betaSetInventoryMetadataIn"])
    types["GoogleCloudRetailV2betaSetInventoryMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2betaSetInventoryMetadataOut"])
    types["GoogleCloudRetailV2CatalogAttributeIn"] = t.struct(
        {
            "exactSearchableOption": t.string().optional(),
            "dynamicFacetableOption": t.string().optional(),
            "indexableOption": t.string().optional(),
            "searchableOption": t.string().optional(),
            "retrievableOption": t.string().optional(),
            "key": t.string(),
        }
    ).named(renames["GoogleCloudRetailV2CatalogAttributeIn"])
    types["GoogleCloudRetailV2CatalogAttributeOut"] = t.struct(
        {
            "exactSearchableOption": t.string().optional(),
            "type": t.string().optional(),
            "dynamicFacetableOption": t.string().optional(),
            "indexableOption": t.string().optional(),
            "inUse": t.boolean().optional(),
            "searchableOption": t.string().optional(),
            "retrievableOption": t.string().optional(),
            "key": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2CatalogAttributeOut"])
    types["GoogleCloudRetailV2alphaAddFulfillmentPlacesMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2alphaAddFulfillmentPlacesMetadataIn"])
    types["GoogleCloudRetailV2alphaAddFulfillmentPlacesMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2alphaAddFulfillmentPlacesMetadataOut"])
    types["GoogleCloudRetailV2AddFulfillmentPlacesRequestIn"] = t.struct(
        {
            "type": t.string(),
            "allowMissing": t.boolean().optional(),
            "addTime": t.string().optional(),
            "placeIds": t.array(t.string()),
        }
    ).named(renames["GoogleCloudRetailV2AddFulfillmentPlacesRequestIn"])
    types["GoogleCloudRetailV2AddFulfillmentPlacesRequestOut"] = t.struct(
        {
            "type": t.string(),
            "allowMissing": t.boolean().optional(),
            "addTime": t.string().optional(),
            "placeIds": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2AddFulfillmentPlacesRequestOut"])
    types["GoogleCloudRetailV2CompletionDataInputConfigIn"] = t.struct(
        {"bigQuerySource": t.proxy(renames["GoogleCloudRetailV2BigQuerySourceIn"])}
    ).named(renames["GoogleCloudRetailV2CompletionDataInputConfigIn"])
    types["GoogleCloudRetailV2CompletionDataInputConfigOut"] = t.struct(
        {
            "bigQuerySource": t.proxy(renames["GoogleCloudRetailV2BigQuerySourceOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2CompletionDataInputConfigOut"])
    types["GoogleCloudRetailV2ImportProductsRequestIn"] = t.struct(
        {
            "reconciliationMode": t.string().optional(),
            "errorsConfig": t.proxy(
                renames["GoogleCloudRetailV2ImportErrorsConfigIn"]
            ).optional(),
            "requestId": t.string().optional(),
            "updateMask": t.string().optional(),
            "inputConfig": t.proxy(renames["GoogleCloudRetailV2ProductInputConfigIn"]),
            "notificationPubsubTopic": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2ImportProductsRequestIn"])
    types["GoogleCloudRetailV2ImportProductsRequestOut"] = t.struct(
        {
            "reconciliationMode": t.string().optional(),
            "errorsConfig": t.proxy(
                renames["GoogleCloudRetailV2ImportErrorsConfigOut"]
            ).optional(),
            "requestId": t.string().optional(),
            "updateMask": t.string().optional(),
            "inputConfig": t.proxy(renames["GoogleCloudRetailV2ProductInputConfigOut"]),
            "notificationPubsubTopic": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ImportProductsRequestOut"])
    types[
        "GoogleCloudRetailV2betaCreateMerchantCenterAccountLinkMetadataIn"
    ] = t.struct(
        {"createTime": t.string().optional(), "updateTime": t.string().optional()}
    ).named(
        renames["GoogleCloudRetailV2betaCreateMerchantCenterAccountLinkMetadataIn"]
    )
    types[
        "GoogleCloudRetailV2betaCreateMerchantCenterAccountLinkMetadataOut"
    ] = t.struct(
        {
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudRetailV2betaCreateMerchantCenterAccountLinkMetadataOut"]
    )
    types["GoogleCloudRetailV2PriceInfoIn"] = t.struct(
        {
            "priceEffectiveTime": t.string().optional(),
            "priceExpireTime": t.string().optional(),
            "cost": t.number().optional(),
            "originalPrice": t.number().optional(),
            "price": t.number().optional(),
            "currencyCode": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2PriceInfoIn"])
    types["GoogleCloudRetailV2PriceInfoOut"] = t.struct(
        {
            "priceEffectiveTime": t.string().optional(),
            "priceExpireTime": t.string().optional(),
            "cost": t.number().optional(),
            "priceRange": t.proxy(
                renames["GoogleCloudRetailV2PriceInfoPriceRangeOut"]
            ).optional(),
            "originalPrice": t.number().optional(),
            "price": t.number().optional(),
            "currencyCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2PriceInfoOut"])
    types["GoogleCloudRetailV2betaExportProductsResponseIn"] = t.struct(
        {
            "outputResult": t.proxy(
                renames["GoogleCloudRetailV2betaOutputResultIn"]
            ).optional(),
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional(),
            "errorsConfig": t.proxy(
                renames["GoogleCloudRetailV2betaExportErrorsConfigIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudRetailV2betaExportProductsResponseIn"])
    types["GoogleCloudRetailV2betaExportProductsResponseOut"] = t.struct(
        {
            "outputResult": t.proxy(
                renames["GoogleCloudRetailV2betaOutputResultOut"]
            ).optional(),
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "errorsConfig": t.proxy(
                renames["GoogleCloudRetailV2betaExportErrorsConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2betaExportProductsResponseOut"])
    types[
        "GoogleCloudRetailV2alphaMerchantCenterAccountLinkMerchantCenterFeedFilterIn"
    ] = t.struct(
        {
            "primaryFeedName": t.string().optional(),
            "primaryFeedId": t.string().optional(),
        }
    ).named(
        renames[
            "GoogleCloudRetailV2alphaMerchantCenterAccountLinkMerchantCenterFeedFilterIn"
        ]
    )
    types[
        "GoogleCloudRetailV2alphaMerchantCenterAccountLinkMerchantCenterFeedFilterOut"
    ] = t.struct(
        {
            "primaryFeedName": t.string().optional(),
            "primaryFeedId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudRetailV2alphaMerchantCenterAccountLinkMerchantCenterFeedFilterOut"
        ]
    )
    types["GoogleCloudRetailV2alphaAddFulfillmentPlacesResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2alphaAddFulfillmentPlacesResponseIn"])
    types["GoogleCloudRetailV2alphaAddFulfillmentPlacesResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2alphaAddFulfillmentPlacesResponseOut"])
    types["GoogleCloudRetailV2ImportErrorsConfigIn"] = t.struct(
        {"gcsPrefix": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2ImportErrorsConfigIn"])
    types["GoogleCloudRetailV2ImportErrorsConfigOut"] = t.struct(
        {
            "gcsPrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ImportErrorsConfigOut"])
    types["GoogleCloudRetailV2LocalInventoryIn"] = t.struct(
        {
            "placeId": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "priceInfo": t.proxy(renames["GoogleCloudRetailV2PriceInfoIn"]).optional(),
            "fulfillmentTypes": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudRetailV2LocalInventoryIn"])
    types["GoogleCloudRetailV2LocalInventoryOut"] = t.struct(
        {
            "placeId": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "priceInfo": t.proxy(renames["GoogleCloudRetailV2PriceInfoOut"]).optional(),
            "fulfillmentTypes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2LocalInventoryOut"])
    types["GoogleCloudRetailV2SearchResponseFacetFacetValueIn"] = t.struct(
        {
            "maxValue": t.number().optional(),
            "count": t.string().optional(),
            "value": t.string().optional(),
            "interval": t.proxy(renames["GoogleCloudRetailV2IntervalIn"]).optional(),
            "minValue": t.number().optional(),
        }
    ).named(renames["GoogleCloudRetailV2SearchResponseFacetFacetValueIn"])
    types["GoogleCloudRetailV2SearchResponseFacetFacetValueOut"] = t.struct(
        {
            "maxValue": t.number().optional(),
            "count": t.string().optional(),
            "value": t.string().optional(),
            "interval": t.proxy(renames["GoogleCloudRetailV2IntervalOut"]).optional(),
            "minValue": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2SearchResponseFacetFacetValueOut"])
    types["GoogleCloudRetailV2ReplaceCatalogAttributeRequestIn"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "catalogAttribute": t.proxy(
                renames["GoogleCloudRetailV2CatalogAttributeIn"]
            ),
        }
    ).named(renames["GoogleCloudRetailV2ReplaceCatalogAttributeRequestIn"])
    types["GoogleCloudRetailV2ReplaceCatalogAttributeRequestOut"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "catalogAttribute": t.proxy(
                renames["GoogleCloudRetailV2CatalogAttributeOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ReplaceCatalogAttributeRequestOut"])
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
    types["GoogleCloudRetailV2SearchRequestFacetSpecFacetKeyIn"] = t.struct(
        {
            "prefixes": t.array(t.string()).optional(),
            "intervals": t.array(
                t.proxy(renames["GoogleCloudRetailV2IntervalIn"])
            ).optional(),
            "returnMinMax": t.boolean().optional(),
            "restrictedValues": t.array(t.string()).optional(),
            "orderBy": t.string().optional(),
            "caseInsensitive": t.boolean().optional(),
            "key": t.string(),
            "query": t.string().optional(),
            "contains": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudRetailV2SearchRequestFacetSpecFacetKeyIn"])
    types["GoogleCloudRetailV2SearchRequestFacetSpecFacetKeyOut"] = t.struct(
        {
            "prefixes": t.array(t.string()).optional(),
            "intervals": t.array(
                t.proxy(renames["GoogleCloudRetailV2IntervalOut"])
            ).optional(),
            "returnMinMax": t.boolean().optional(),
            "restrictedValues": t.array(t.string()).optional(),
            "orderBy": t.string().optional(),
            "caseInsensitive": t.boolean().optional(),
            "key": t.string(),
            "query": t.string().optional(),
            "contains": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2SearchRequestFacetSpecFacetKeyOut"])
    types["GoogleCloudRetailV2alphaRemoveLocalInventoriesResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2alphaRemoveLocalInventoriesResponseIn"])
    types["GoogleCloudRetailV2alphaRemoveLocalInventoriesResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2alphaRemoveLocalInventoriesResponseOut"])
    types["GoogleCloudRetailV2ProductIn"] = t.struct(
        {
            "conditions": t.array(t.string()).optional(),
            "availableTime": t.string().optional(),
            "categories": t.array(t.string()).optional(),
            "colorInfo": t.proxy(renames["GoogleCloudRetailV2ColorInfoIn"]).optional(),
            "audience": t.proxy(renames["GoogleCloudRetailV2AudienceIn"]).optional(),
            "sizes": t.array(t.string()).optional(),
            "fulfillmentInfo": t.array(
                t.proxy(renames["GoogleCloudRetailV2FulfillmentInfoIn"])
            ).optional(),
            "patterns": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
            "materials": t.array(t.string()).optional(),
            "availability": t.string().optional(),
            "uri": t.string().optional(),
            "images": t.array(
                t.proxy(renames["GoogleCloudRetailV2ImageIn"])
            ).optional(),
            "tags": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "publishTime": t.string().optional(),
            "collectionMemberIds": t.array(t.string()).optional(),
            "brands": t.array(t.string()).optional(),
            "expireTime": t.string().optional(),
            "priceInfo": t.proxy(renames["GoogleCloudRetailV2PriceInfoIn"]).optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "gtin": t.string().optional(),
            "primaryProductId": t.string().optional(),
            "id": t.string().optional(),
            "promotions": t.array(
                t.proxy(renames["GoogleCloudRetailV2PromotionIn"])
            ).optional(),
            "availableQuantity": t.integer().optional(),
            "rating": t.proxy(renames["GoogleCloudRetailV2RatingIn"]).optional(),
            "languageCode": t.string().optional(),
            "ttl": t.string().optional(),
            "retrievableFields": t.string().optional(),
            "title": t.string(),
        }
    ).named(renames["GoogleCloudRetailV2ProductIn"])
    types["GoogleCloudRetailV2ProductOut"] = t.struct(
        {
            "conditions": t.array(t.string()).optional(),
            "variants": t.array(
                t.proxy(renames["GoogleCloudRetailV2ProductOut"])
            ).optional(),
            "availableTime": t.string().optional(),
            "categories": t.array(t.string()).optional(),
            "colorInfo": t.proxy(renames["GoogleCloudRetailV2ColorInfoOut"]).optional(),
            "audience": t.proxy(renames["GoogleCloudRetailV2AudienceOut"]).optional(),
            "sizes": t.array(t.string()).optional(),
            "fulfillmentInfo": t.array(
                t.proxy(renames["GoogleCloudRetailV2FulfillmentInfoOut"])
            ).optional(),
            "patterns": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
            "materials": t.array(t.string()).optional(),
            "availability": t.string().optional(),
            "uri": t.string().optional(),
            "images": t.array(
                t.proxy(renames["GoogleCloudRetailV2ImageOut"])
            ).optional(),
            "localInventories": t.array(
                t.proxy(renames["GoogleCloudRetailV2LocalInventoryOut"])
            ).optional(),
            "tags": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "publishTime": t.string().optional(),
            "collectionMemberIds": t.array(t.string()).optional(),
            "brands": t.array(t.string()).optional(),
            "expireTime": t.string().optional(),
            "priceInfo": t.proxy(renames["GoogleCloudRetailV2PriceInfoOut"]).optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "gtin": t.string().optional(),
            "primaryProductId": t.string().optional(),
            "id": t.string().optional(),
            "promotions": t.array(
                t.proxy(renames["GoogleCloudRetailV2PromotionOut"])
            ).optional(),
            "availableQuantity": t.integer().optional(),
            "rating": t.proxy(renames["GoogleCloudRetailV2RatingOut"]).optional(),
            "languageCode": t.string().optional(),
            "ttl": t.string().optional(),
            "retrievableFields": t.string().optional(),
            "title": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ProductOut"])
    types["GoogleCloudRetailV2IntervalIn"] = t.struct(
        {
            "maximum": t.number().optional(),
            "exclusiveMaximum": t.number().optional(),
            "minimum": t.number().optional(),
            "exclusiveMinimum": t.number().optional(),
        }
    ).named(renames["GoogleCloudRetailV2IntervalIn"])
    types["GoogleCloudRetailV2IntervalOut"] = t.struct(
        {
            "maximum": t.number().optional(),
            "exclusiveMaximum": t.number().optional(),
            "minimum": t.number().optional(),
            "exclusiveMinimum": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2IntervalOut"])
    types["GoogleCloudRetailV2RemoveFulfillmentPlacesRequestIn"] = t.struct(
        {
            "type": t.string(),
            "placeIds": t.array(t.string()),
            "removeTime": t.string().optional(),
            "allowMissing": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudRetailV2RemoveFulfillmentPlacesRequestIn"])
    types["GoogleCloudRetailV2RemoveFulfillmentPlacesRequestOut"] = t.struct(
        {
            "type": t.string(),
            "placeIds": t.array(t.string()),
            "removeTime": t.string().optional(),
            "allowMissing": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2RemoveFulfillmentPlacesRequestOut"])
    types["GoogleCloudRetailV2alphaRejoinUserEventsResponseIn"] = t.struct(
        {"rejoinedUserEventsCount": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2alphaRejoinUserEventsResponseIn"])
    types["GoogleCloudRetailV2alphaRejoinUserEventsResponseOut"] = t.struct(
        {
            "rejoinedUserEventsCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaRejoinUserEventsResponseOut"])
    types["GoogleCloudRetailV2RatingIn"] = t.struct(
        {
            "ratingHistogram": t.array(t.integer()).optional(),
            "ratingCount": t.integer().optional(),
            "averageRating": t.number().optional(),
        }
    ).named(renames["GoogleCloudRetailV2RatingIn"])
    types["GoogleCloudRetailV2RatingOut"] = t.struct(
        {
            "ratingHistogram": t.array(t.integer()).optional(),
            "ratingCount": t.integer().optional(),
            "averageRating": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2RatingOut"])
    types["GoogleCloudRetailV2CompletionConfigIn"] = t.struct(
        {
            "name": t.string(),
            "autoLearning": t.boolean().optional(),
            "minPrefixLength": t.integer().optional(),
            "matchingOrder": t.string().optional(),
            "maxSuggestions": t.integer().optional(),
        }
    ).named(renames["GoogleCloudRetailV2CompletionConfigIn"])
    types["GoogleCloudRetailV2CompletionConfigOut"] = t.struct(
        {
            "lastSuggestionsImportOperation": t.string().optional(),
            "name": t.string(),
            "autoLearning": t.boolean().optional(),
            "allowlistInputConfig": t.proxy(
                renames["GoogleCloudRetailV2CompletionDataInputConfigOut"]
            ).optional(),
            "lastDenylistImportOperation": t.string().optional(),
            "lastAllowlistImportOperation": t.string().optional(),
            "minPrefixLength": t.integer().optional(),
            "matchingOrder": t.string().optional(),
            "denylistInputConfig": t.proxy(
                renames["GoogleCloudRetailV2CompletionDataInputConfigOut"]
            ).optional(),
            "maxSuggestions": t.integer().optional(),
            "suggestionsInputConfig": t.proxy(
                renames["GoogleCloudRetailV2CompletionDataInputConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2CompletionConfigOut"])
    types["GoogleCloudRetailV2alphaImportUserEventsResponseIn"] = t.struct(
        {
            "importSummary": t.proxy(
                renames["GoogleCloudRetailV2alphaUserEventImportSummaryIn"]
            ).optional(),
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional(),
            "errorsConfig": t.proxy(
                renames["GoogleCloudRetailV2alphaImportErrorsConfigIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaImportUserEventsResponseIn"])
    types["GoogleCloudRetailV2alphaImportUserEventsResponseOut"] = t.struct(
        {
            "importSummary": t.proxy(
                renames["GoogleCloudRetailV2alphaUserEventImportSummaryOut"]
            ).optional(),
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "errorsConfig": t.proxy(
                renames["GoogleCloudRetailV2alphaImportErrorsConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaImportUserEventsResponseOut"])
    types["GoogleCloudRetailV2TuneModelMetadataIn"] = t.struct(
        {"model": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2TuneModelMetadataIn"])
    types["GoogleCloudRetailV2TuneModelMetadataOut"] = t.struct(
        {
            "model": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2TuneModelMetadataOut"])
    types["GoogleCloudRetailV2CatalogIn"] = t.struct(
        {
            "displayName": t.string(),
            "name": t.string(),
            "productLevelConfig": t.proxy(
                renames["GoogleCloudRetailV2ProductLevelConfigIn"]
            ),
        }
    ).named(renames["GoogleCloudRetailV2CatalogIn"])
    types["GoogleCloudRetailV2CatalogOut"] = t.struct(
        {
            "displayName": t.string(),
            "name": t.string(),
            "productLevelConfig": t.proxy(
                renames["GoogleCloudRetailV2ProductLevelConfigOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2CatalogOut"])
    types["GoogleCloudRetailV2UserEventIn"] = t.struct(
        {
            "pageCategories": t.array(t.string()).optional(),
            "cartId": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "orderBy": t.string().optional(),
            "searchQuery": t.string().optional(),
            "completionDetail": t.proxy(
                renames["GoogleCloudRetailV2CompletionDetailIn"]
            ).optional(),
            "filter": t.string().optional(),
            "eventTime": t.string().optional(),
            "sessionId": t.string().optional(),
            "visitorId": t.string(),
            "eventType": t.string(),
            "pageViewId": t.string().optional(),
            "attributionToken": t.string().optional(),
            "purchaseTransaction": t.proxy(
                renames["GoogleCloudRetailV2PurchaseTransactionIn"]
            ).optional(),
            "userInfo": t.proxy(renames["GoogleCloudRetailV2UserInfoIn"]).optional(),
            "uri": t.string().optional(),
            "referrerUri": t.string().optional(),
            "experimentIds": t.array(t.string()).optional(),
            "offset": t.integer().optional(),
            "productDetails": t.array(
                t.proxy(renames["GoogleCloudRetailV2ProductDetailIn"])
            ).optional(),
            "entity": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2UserEventIn"])
    types["GoogleCloudRetailV2UserEventOut"] = t.struct(
        {
            "pageCategories": t.array(t.string()).optional(),
            "cartId": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "orderBy": t.string().optional(),
            "searchQuery": t.string().optional(),
            "completionDetail": t.proxy(
                renames["GoogleCloudRetailV2CompletionDetailOut"]
            ).optional(),
            "filter": t.string().optional(),
            "eventTime": t.string().optional(),
            "sessionId": t.string().optional(),
            "visitorId": t.string(),
            "eventType": t.string(),
            "pageViewId": t.string().optional(),
            "attributionToken": t.string().optional(),
            "purchaseTransaction": t.proxy(
                renames["GoogleCloudRetailV2PurchaseTransactionOut"]
            ).optional(),
            "userInfo": t.proxy(renames["GoogleCloudRetailV2UserInfoOut"]).optional(),
            "uri": t.string().optional(),
            "referrerUri": t.string().optional(),
            "experimentIds": t.array(t.string()).optional(),
            "offset": t.integer().optional(),
            "productDetails": t.array(
                t.proxy(renames["GoogleCloudRetailV2ProductDetailOut"])
            ).optional(),
            "entity": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2UserEventOut"])
    types["GoogleCloudRetailV2SetDefaultBranchRequestIn"] = t.struct(
        {
            "force": t.boolean().optional(),
            "branchId": t.string().optional(),
            "note": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2SetDefaultBranchRequestIn"])
    types["GoogleCloudRetailV2SetDefaultBranchRequestOut"] = t.struct(
        {
            "force": t.boolean().optional(),
            "branchId": t.string().optional(),
            "note": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2SetDefaultBranchRequestOut"])
    types["GoogleCloudRetailV2betaPurgeUserEventsResponseIn"] = t.struct(
        {"purgedEventsCount": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2betaPurgeUserEventsResponseIn"])
    types["GoogleCloudRetailV2betaPurgeUserEventsResponseOut"] = t.struct(
        {
            "purgedEventsCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2betaPurgeUserEventsResponseOut"])
    types["GoogleCloudRetailV2alphaPurgeProductsResponseIn"] = t.struct(
        {
            "purgeSample": t.array(t.string()).optional(),
            "purgeCount": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaPurgeProductsResponseIn"])
    types["GoogleCloudRetailV2alphaPurgeProductsResponseOut"] = t.struct(
        {
            "purgeSample": t.array(t.string()).optional(),
            "purgeCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaPurgeProductsResponseOut"])
    types["GoogleCloudRetailV2alphaGcsOutputResultIn"] = t.struct(
        {"outputUri": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2alphaGcsOutputResultIn"])
    types["GoogleCloudRetailV2alphaGcsOutputResultOut"] = t.struct(
        {
            "outputUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaGcsOutputResultOut"])
    types["GoogleCloudRetailV2RuleIn"] = t.struct(
        {
            "doNotAssociateAction": t.proxy(
                renames["GoogleCloudRetailV2RuleDoNotAssociateActionIn"]
            ).optional(),
            "filterAction": t.proxy(
                renames["GoogleCloudRetailV2RuleFilterActionIn"]
            ).optional(),
            "onewaySynonymsAction": t.proxy(
                renames["GoogleCloudRetailV2RuleOnewaySynonymsActionIn"]
            ).optional(),
            "ignoreAction": t.proxy(
                renames["GoogleCloudRetailV2RuleIgnoreActionIn"]
            ).optional(),
            "boostAction": t.proxy(
                renames["GoogleCloudRetailV2RuleBoostActionIn"]
            ).optional(),
            "condition": t.proxy(renames["GoogleCloudRetailV2ConditionIn"]),
            "redirectAction": t.proxy(
                renames["GoogleCloudRetailV2RuleRedirectActionIn"]
            ).optional(),
            "replacementAction": t.proxy(
                renames["GoogleCloudRetailV2RuleReplacementActionIn"]
            ).optional(),
            "twowaySynonymsAction": t.proxy(
                renames["GoogleCloudRetailV2RuleTwowaySynonymsActionIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudRetailV2RuleIn"])
    types["GoogleCloudRetailV2RuleOut"] = t.struct(
        {
            "doNotAssociateAction": t.proxy(
                renames["GoogleCloudRetailV2RuleDoNotAssociateActionOut"]
            ).optional(),
            "filterAction": t.proxy(
                renames["GoogleCloudRetailV2RuleFilterActionOut"]
            ).optional(),
            "onewaySynonymsAction": t.proxy(
                renames["GoogleCloudRetailV2RuleOnewaySynonymsActionOut"]
            ).optional(),
            "ignoreAction": t.proxy(
                renames["GoogleCloudRetailV2RuleIgnoreActionOut"]
            ).optional(),
            "boostAction": t.proxy(
                renames["GoogleCloudRetailV2RuleBoostActionOut"]
            ).optional(),
            "condition": t.proxy(renames["GoogleCloudRetailV2ConditionOut"]),
            "redirectAction": t.proxy(
                renames["GoogleCloudRetailV2RuleRedirectActionOut"]
            ).optional(),
            "replacementAction": t.proxy(
                renames["GoogleCloudRetailV2RuleReplacementActionOut"]
            ).optional(),
            "twowaySynonymsAction": t.proxy(
                renames["GoogleCloudRetailV2RuleTwowaySynonymsActionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2RuleOut"])
    types["GoogleCloudRetailV2alphaExportUserEventsResponseIn"] = t.struct(
        {
            "outputResult": t.proxy(
                renames["GoogleCloudRetailV2alphaOutputResultIn"]
            ).optional(),
            "errorsConfig": t.proxy(
                renames["GoogleCloudRetailV2alphaExportErrorsConfigIn"]
            ).optional(),
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaExportUserEventsResponseIn"])
    types["GoogleCloudRetailV2alphaExportUserEventsResponseOut"] = t.struct(
        {
            "outputResult": t.proxy(
                renames["GoogleCloudRetailV2alphaOutputResultOut"]
            ).optional(),
            "errorsConfig": t.proxy(
                renames["GoogleCloudRetailV2alphaExportErrorsConfigOut"]
            ).optional(),
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaExportUserEventsResponseOut"])
    types["GoogleCloudRetailV2betaImportCompletionDataResponseIn"] = t.struct(
        {"errorSamples": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional()}
    ).named(renames["GoogleCloudRetailV2betaImportCompletionDataResponseIn"])
    types["GoogleCloudRetailV2betaImportCompletionDataResponseOut"] = t.struct(
        {
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2betaImportCompletionDataResponseOut"])
    types["GoogleCloudRetailV2RuleTwowaySynonymsActionIn"] = t.struct(
        {"synonyms": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudRetailV2RuleTwowaySynonymsActionIn"])
    types["GoogleCloudRetailV2RuleTwowaySynonymsActionOut"] = t.struct(
        {
            "synonyms": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2RuleTwowaySynonymsActionOut"])
    types["GoogleCloudRetailLoggingErrorContextIn"] = t.struct(
        {
            "httpRequest": t.proxy(
                renames["GoogleCloudRetailLoggingHttpRequestContextIn"]
            ).optional(),
            "reportLocation": t.proxy(
                renames["GoogleCloudRetailLoggingSourceLocationIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudRetailLoggingErrorContextIn"])
    types["GoogleCloudRetailLoggingErrorContextOut"] = t.struct(
        {
            "httpRequest": t.proxy(
                renames["GoogleCloudRetailLoggingHttpRequestContextOut"]
            ).optional(),
            "reportLocation": t.proxy(
                renames["GoogleCloudRetailLoggingSourceLocationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailLoggingErrorContextOut"])
    types["GoogleCloudRetailV2RemoveLocalInventoriesResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2RemoveLocalInventoriesResponseIn"])
    types["GoogleCloudRetailV2RemoveLocalInventoriesResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2RemoveLocalInventoriesResponseOut"])
    types["GoogleCloudRetailV2ImportUserEventsRequestIn"] = t.struct(
        {
            "inputConfig": t.proxy(
                renames["GoogleCloudRetailV2UserEventInputConfigIn"]
            ),
            "errorsConfig": t.proxy(
                renames["GoogleCloudRetailV2ImportErrorsConfigIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ImportUserEventsRequestIn"])
    types["GoogleCloudRetailV2ImportUserEventsRequestOut"] = t.struct(
        {
            "inputConfig": t.proxy(
                renames["GoogleCloudRetailV2UserEventInputConfigOut"]
            ),
            "errorsConfig": t.proxy(
                renames["GoogleCloudRetailV2ImportErrorsConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ImportUserEventsRequestOut"])
    types["GoogleCloudRetailV2RuleRedirectActionIn"] = t.struct(
        {"redirectUri": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2RuleRedirectActionIn"])
    types["GoogleCloudRetailV2RuleRedirectActionOut"] = t.struct(
        {
            "redirectUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2RuleRedirectActionOut"])
    types["GoogleCloudRetailV2ProductDetailIn"] = t.struct(
        {
            "product": t.proxy(renames["GoogleCloudRetailV2ProductIn"]),
            "quantity": t.integer().optional(),
        }
    ).named(renames["GoogleCloudRetailV2ProductDetailIn"])
    types["GoogleCloudRetailV2ProductDetailOut"] = t.struct(
        {
            "product": t.proxy(renames["GoogleCloudRetailV2ProductOut"]),
            "quantity": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ProductDetailOut"])
    types["GoogleCloudRetailV2ListModelsResponseIn"] = t.struct(
        {
            "models": t.array(
                t.proxy(renames["GoogleCloudRetailV2ModelIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2ListModelsResponseIn"])
    types["GoogleCloudRetailV2ListModelsResponseOut"] = t.struct(
        {
            "models": t.array(
                t.proxy(renames["GoogleCloudRetailV2ModelOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ListModelsResponseOut"])
    types["GoogleCloudRetailV2alphaImportErrorsConfigIn"] = t.struct(
        {"gcsPrefix": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2alphaImportErrorsConfigIn"])
    types["GoogleCloudRetailV2alphaImportErrorsConfigOut"] = t.struct(
        {
            "gcsPrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaImportErrorsConfigOut"])
    types["GoogleCloudRetailV2PurgeUserEventsResponseIn"] = t.struct(
        {"purgedEventsCount": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2PurgeUserEventsResponseIn"])
    types["GoogleCloudRetailV2PurgeUserEventsResponseOut"] = t.struct(
        {
            "purgedEventsCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2PurgeUserEventsResponseOut"])
    types["GoogleCloudRetailV2PauseModelRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2PauseModelRequestIn"])
    types["GoogleCloudRetailV2PauseModelRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2PauseModelRequestOut"])
    types["GoogleCloudRetailV2alphaRejoinUserEventsMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2alphaRejoinUserEventsMetadataIn"])
    types["GoogleCloudRetailV2alphaRejoinUserEventsMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2alphaRejoinUserEventsMetadataOut"])
    types["GoogleCloudRetailLoggingImportErrorContextIn"] = t.struct(
        {
            "lineNumber": t.string().optional(),
            "userEvent": t.string().optional(),
            "gcsPath": t.string().optional(),
            "operationName": t.string().optional(),
            "product": t.string().optional(),
            "catalogItem": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailLoggingImportErrorContextIn"])
    types["GoogleCloudRetailLoggingImportErrorContextOut"] = t.struct(
        {
            "lineNumber": t.string().optional(),
            "userEvent": t.string().optional(),
            "gcsPath": t.string().optional(),
            "operationName": t.string().optional(),
            "product": t.string().optional(),
            "catalogItem": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailLoggingImportErrorContextOut"])
    types["GoogleCloudRetailV2SetInventoryMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2SetInventoryMetadataIn"])
    types["GoogleCloudRetailV2SetInventoryMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2SetInventoryMetadataOut"])
    types["GoogleCloudRetailLoggingErrorLogIn"] = t.struct(
        {
            "message": t.string().optional(),
            "serviceContext": t.proxy(
                renames["GoogleCloudRetailLoggingServiceContextIn"]
            ).optional(),
            "responsePayload": t.struct({"_": t.string().optional()}).optional(),
            "importPayload": t.proxy(
                renames["GoogleCloudRetailLoggingImportErrorContextIn"]
            ).optional(),
            "requestPayload": t.struct({"_": t.string().optional()}).optional(),
            "context": t.proxy(
                renames["GoogleCloudRetailLoggingErrorContextIn"]
            ).optional(),
            "status": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
        }
    ).named(renames["GoogleCloudRetailLoggingErrorLogIn"])
    types["GoogleCloudRetailLoggingErrorLogOut"] = t.struct(
        {
            "message": t.string().optional(),
            "serviceContext": t.proxy(
                renames["GoogleCloudRetailLoggingServiceContextOut"]
            ).optional(),
            "responsePayload": t.struct({"_": t.string().optional()}).optional(),
            "importPayload": t.proxy(
                renames["GoogleCloudRetailLoggingImportErrorContextOut"]
            ).optional(),
            "requestPayload": t.struct({"_": t.string().optional()}).optional(),
            "context": t.proxy(
                renames["GoogleCloudRetailLoggingErrorContextOut"]
            ).optional(),
            "status": t.proxy(renames["GoogleRpcStatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailLoggingErrorLogOut"])
    types["GoogleCloudRetailV2SetInventoryResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2SetInventoryResponseIn"])
    types["GoogleCloudRetailV2SetInventoryResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2SetInventoryResponseOut"])
    types["GoogleCloudRetailV2ConditionIn"] = t.struct(
        {
            "activeTimeRange": t.array(
                t.proxy(renames["GoogleCloudRetailV2ConditionTimeRangeIn"])
            ).optional(),
            "queryTerms": t.array(
                t.proxy(renames["GoogleCloudRetailV2ConditionQueryTermIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ConditionIn"])
    types["GoogleCloudRetailV2ConditionOut"] = t.struct(
        {
            "activeTimeRange": t.array(
                t.proxy(renames["GoogleCloudRetailV2ConditionTimeRangeOut"])
            ).optional(),
            "queryTerms": t.array(
                t.proxy(renames["GoogleCloudRetailV2ConditionQueryTermOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ConditionOut"])
    types["GoogleLongrunningListOperationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(
                t.proxy(renames["GoogleLongrunningOperationIn"])
            ).optional(),
        }
    ).named(renames["GoogleLongrunningListOperationsResponseIn"])
    types["GoogleLongrunningListOperationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(
                t.proxy(renames["GoogleLongrunningOperationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleLongrunningListOperationsResponseOut"])
    types["GoogleCloudRetailV2betaExportMetadataIn"] = t.struct(
        {"updateTime": t.string().optional(), "createTime": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2betaExportMetadataIn"])
    types["GoogleCloudRetailV2betaExportMetadataOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2betaExportMetadataOut"])
    types["GoogleCloudRetailV2RemoveCatalogAttributeRequestIn"] = t.struct(
        {"key": t.string()}
    ).named(renames["GoogleCloudRetailV2RemoveCatalogAttributeRequestIn"])
    types["GoogleCloudRetailV2RemoveCatalogAttributeRequestOut"] = t.struct(
        {"key": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2RemoveCatalogAttributeRequestOut"])
    types["GoogleCloudRetailV2ImageIn"] = t.struct(
        {
            "width": t.integer().optional(),
            "height": t.integer().optional(),
            "uri": t.string(),
        }
    ).named(renames["GoogleCloudRetailV2ImageIn"])
    types["GoogleCloudRetailV2ImageOut"] = t.struct(
        {
            "width": t.integer().optional(),
            "height": t.integer().optional(),
            "uri": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ImageOut"])
    types["GoogleCloudRetailV2RuleBoostActionIn"] = t.struct(
        {"productsFilter": t.string().optional(), "boost": t.number().optional()}
    ).named(renames["GoogleCloudRetailV2RuleBoostActionIn"])
    types["GoogleCloudRetailV2RuleBoostActionOut"] = t.struct(
        {
            "productsFilter": t.string().optional(),
            "boost": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2RuleBoostActionOut"])
    types["GoogleCloudRetailV2SearchRequestQueryExpansionSpecIn"] = t.struct(
        {
            "condition": t.string().optional(),
            "pinUnexpandedResults": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudRetailV2SearchRequestQueryExpansionSpecIn"])
    types["GoogleCloudRetailV2SearchRequestQueryExpansionSpecOut"] = t.struct(
        {
            "condition": t.string().optional(),
            "pinUnexpandedResults": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2SearchRequestQueryExpansionSpecOut"])
    types["GoogleCloudRetailV2betaOutputResultIn"] = t.struct(
        {
            "bigqueryResult": t.array(
                t.proxy(renames["GoogleCloudRetailV2betaBigQueryOutputResultIn"])
            ).optional(),
            "gcsResult": t.array(
                t.proxy(renames["GoogleCloudRetailV2betaGcsOutputResultIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudRetailV2betaOutputResultIn"])
    types["GoogleCloudRetailV2betaOutputResultOut"] = t.struct(
        {
            "bigqueryResult": t.array(
                t.proxy(renames["GoogleCloudRetailV2betaBigQueryOutputResultOut"])
            ).optional(),
            "gcsResult": t.array(
                t.proxy(renames["GoogleCloudRetailV2betaGcsOutputResultOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2betaOutputResultOut"])
    types["GoogleCloudRetailV2alphaModelIn"] = t.struct(
        {
            "trainingState": t.string().optional(),
            "name": t.string(),
            "filteringOption": t.string().optional(),
            "type": t.string(),
            "pageOptimizationConfig": t.proxy(
                renames["GoogleCloudRetailV2alphaModelPageOptimizationConfigIn"]
            ).optional(),
            "modelFeaturesConfig": t.proxy(
                renames["GoogleCloudRetailV2alphaModelModelFeaturesConfigIn"]
            ).optional(),
            "optimizationObjective": t.string().optional(),
            "periodicTuningState": t.string().optional(),
            "displayName": t.string(),
        }
    ).named(renames["GoogleCloudRetailV2alphaModelIn"])
    types["GoogleCloudRetailV2alphaModelOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "trainingState": t.string().optional(),
            "dataState": t.string().optional(),
            "name": t.string(),
            "servingState": t.string().optional(),
            "filteringOption": t.string().optional(),
            "lastTuneTime": t.string().optional(),
            "type": t.string(),
            "pageOptimizationConfig": t.proxy(
                renames["GoogleCloudRetailV2alphaModelPageOptimizationConfigOut"]
            ).optional(),
            "modelFeaturesConfig": t.proxy(
                renames["GoogleCloudRetailV2alphaModelModelFeaturesConfigOut"]
            ).optional(),
            "servingConfigLists": t.array(
                t.proxy(renames["GoogleCloudRetailV2alphaModelServingConfigListOut"])
            ).optional(),
            "optimizationObjective": t.string().optional(),
            "periodicTuningState": t.string().optional(),
            "displayName": t.string(),
            "createTime": t.string().optional(),
            "tuningOperation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaModelOut"])
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
    types["GoogleCloudRetailV2alphaImportCompletionDataResponseIn"] = t.struct(
        {"errorSamples": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional()}
    ).named(renames["GoogleCloudRetailV2alphaImportCompletionDataResponseIn"])
    types["GoogleCloudRetailV2alphaImportCompletionDataResponseOut"] = t.struct(
        {
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaImportCompletionDataResponseOut"])
    types["GoogleCloudRetailV2AudienceIn"] = t.struct(
        {
            "ageGroups": t.array(t.string()).optional(),
            "genders": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudRetailV2AudienceIn"])
    types["GoogleCloudRetailV2AudienceOut"] = t.struct(
        {
            "ageGroups": t.array(t.string()).optional(),
            "genders": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2AudienceOut"])
    types["GoogleCloudRetailV2betaImportUserEventsResponseIn"] = t.struct(
        {
            "importSummary": t.proxy(
                renames["GoogleCloudRetailV2betaUserEventImportSummaryIn"]
            ).optional(),
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional(),
            "errorsConfig": t.proxy(
                renames["GoogleCloudRetailV2betaImportErrorsConfigIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudRetailV2betaImportUserEventsResponseIn"])
    types["GoogleCloudRetailV2betaImportUserEventsResponseOut"] = t.struct(
        {
            "importSummary": t.proxy(
                renames["GoogleCloudRetailV2betaUserEventImportSummaryOut"]
            ).optional(),
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "errorsConfig": t.proxy(
                renames["GoogleCloudRetailV2betaImportErrorsConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2betaImportUserEventsResponseOut"])
    types["GoogleApiHttpBodyIn"] = t.struct(
        {
            "contentType": t.string().optional(),
            "extensions": t.array(t.struct({"_": t.string().optional()})).optional(),
            "data": t.string().optional(),
        }
    ).named(renames["GoogleApiHttpBodyIn"])
    types["GoogleApiHttpBodyOut"] = t.struct(
        {
            "contentType": t.string().optional(),
            "extensions": t.array(t.struct({"_": t.string().optional()})).optional(),
            "data": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleApiHttpBodyOut"])
    types["GoogleCloudRetailV2AddControlRequestIn"] = t.struct(
        {"controlId": t.string()}
    ).named(renames["GoogleCloudRetailV2AddControlRequestIn"])
    types["GoogleCloudRetailV2AddControlRequestOut"] = t.struct(
        {"controlId": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2AddControlRequestOut"])
    types["GoogleCloudRetailV2UserEventInlineSourceIn"] = t.struct(
        {"userEvents": t.array(t.proxy(renames["GoogleCloudRetailV2UserEventIn"]))}
    ).named(renames["GoogleCloudRetailV2UserEventInlineSourceIn"])
    types["GoogleCloudRetailV2UserEventInlineSourceOut"] = t.struct(
        {
            "userEvents": t.array(t.proxy(renames["GoogleCloudRetailV2UserEventOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2UserEventInlineSourceOut"])
    types["GoogleCloudRetailV2CreateModelMetadataIn"] = t.struct(
        {"model": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2CreateModelMetadataIn"])
    types["GoogleCloudRetailV2CreateModelMetadataOut"] = t.struct(
        {
            "model": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2CreateModelMetadataOut"])
    types[
        "GoogleCloudRetailV2ModelFrequentlyBoughtTogetherFeaturesConfigIn"
    ] = t.struct({"contextProductsType": t.string().optional()}).named(
        renames["GoogleCloudRetailV2ModelFrequentlyBoughtTogetherFeaturesConfigIn"]
    )
    types[
        "GoogleCloudRetailV2ModelFrequentlyBoughtTogetherFeaturesConfigOut"
    ] = t.struct(
        {
            "contextProductsType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudRetailV2ModelFrequentlyBoughtTogetherFeaturesConfigOut"]
    )
    types["GoogleCloudRetailV2alphaRemoveLocalInventoriesMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2alphaRemoveLocalInventoriesMetadataIn"])
    types["GoogleCloudRetailV2alphaRemoveLocalInventoriesMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2alphaRemoveLocalInventoriesMetadataOut"])
    types["GoogleCloudRetailV2betaRemoveLocalInventoriesMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2betaRemoveLocalInventoriesMetadataIn"])
    types["GoogleCloudRetailV2betaRemoveLocalInventoriesMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2betaRemoveLocalInventoriesMetadataOut"])
    types["GoogleCloudRetailV2betaAddFulfillmentPlacesMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2betaAddFulfillmentPlacesMetadataIn"])
    types["GoogleCloudRetailV2betaAddFulfillmentPlacesMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2betaAddFulfillmentPlacesMetadataOut"])
    types["GoogleCloudRetailV2ListControlsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "controls": t.array(
                t.proxy(renames["GoogleCloudRetailV2ControlIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ListControlsResponseIn"])
    types["GoogleCloudRetailV2ListControlsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "controls": t.array(
                t.proxy(renames["GoogleCloudRetailV2ControlOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ListControlsResponseOut"])
    types["GoogleCloudRetailV2betaImportMetadataIn"] = t.struct(
        {
            "failureCount": t.string().optional(),
            "updateTime": t.string().optional(),
            "requestId": t.string().optional(),
            "notificationPubsubTopic": t.string().optional(),
            "createTime": t.string().optional(),
            "successCount": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2betaImportMetadataIn"])
    types["GoogleCloudRetailV2betaImportMetadataOut"] = t.struct(
        {
            "failureCount": t.string().optional(),
            "updateTime": t.string().optional(),
            "requestId": t.string().optional(),
            "notificationPubsubTopic": t.string().optional(),
            "createTime": t.string().optional(),
            "successCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2betaImportMetadataOut"])
    types["GoogleCloudRetailV2betaTuneModelMetadataIn"] = t.struct(
        {"model": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2betaTuneModelMetadataIn"])
    types["GoogleCloudRetailV2betaTuneModelMetadataOut"] = t.struct(
        {
            "model": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2betaTuneModelMetadataOut"])
    types["GoogleCloudRetailV2RemoveLocalInventoriesMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2RemoveLocalInventoriesMetadataIn"])
    types["GoogleCloudRetailV2RemoveLocalInventoriesMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2RemoveLocalInventoriesMetadataOut"])
    types["GoogleCloudRetailV2RemoveControlRequestIn"] = t.struct(
        {"controlId": t.string()}
    ).named(renames["GoogleCloudRetailV2RemoveControlRequestIn"])
    types["GoogleCloudRetailV2RemoveControlRequestOut"] = t.struct(
        {"controlId": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2RemoveControlRequestOut"])
    types["GoogleCloudRetailV2betaExportUserEventsResponseIn"] = t.struct(
        {
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional(),
            "outputResult": t.proxy(
                renames["GoogleCloudRetailV2betaOutputResultIn"]
            ).optional(),
            "errorsConfig": t.proxy(
                renames["GoogleCloudRetailV2betaExportErrorsConfigIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudRetailV2betaExportUserEventsResponseIn"])
    types["GoogleCloudRetailV2betaExportUserEventsResponseOut"] = t.struct(
        {
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "outputResult": t.proxy(
                renames["GoogleCloudRetailV2betaOutputResultOut"]
            ).optional(),
            "errorsConfig": t.proxy(
                renames["GoogleCloudRetailV2betaExportErrorsConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2betaExportUserEventsResponseOut"])
    types["GoogleCloudRetailV2AddLocalInventoriesRequestIn"] = t.struct(
        {
            "allowMissing": t.boolean().optional(),
            "localInventories": t.array(
                t.proxy(renames["GoogleCloudRetailV2LocalInventoryIn"])
            ),
            "addMask": t.string().optional(),
            "addTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2AddLocalInventoriesRequestIn"])
    types["GoogleCloudRetailV2AddLocalInventoriesRequestOut"] = t.struct(
        {
            "allowMissing": t.boolean().optional(),
            "localInventories": t.array(
                t.proxy(renames["GoogleCloudRetailV2LocalInventoryOut"])
            ),
            "addMask": t.string().optional(),
            "addTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2AddLocalInventoriesRequestOut"])
    types[
        "GoogleCloudRetailV2betaMerchantCenterAccountLinkMerchantCenterFeedFilterIn"
    ] = t.struct(
        {
            "primaryFeedName": t.string().optional(),
            "primaryFeedId": t.string().optional(),
        }
    ).named(
        renames[
            "GoogleCloudRetailV2betaMerchantCenterAccountLinkMerchantCenterFeedFilterIn"
        ]
    )
    types[
        "GoogleCloudRetailV2betaMerchantCenterAccountLinkMerchantCenterFeedFilterOut"
    ] = t.struct(
        {
            "primaryFeedName": t.string().optional(),
            "primaryFeedId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudRetailV2betaMerchantCenterAccountLinkMerchantCenterFeedFilterOut"
        ]
    )
    types["GoogleCloudRetailV2RuleIgnoreActionIn"] = t.struct(
        {"ignoreTerms": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudRetailV2RuleIgnoreActionIn"])
    types["GoogleCloudRetailV2RuleIgnoreActionOut"] = t.struct(
        {
            "ignoreTerms": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2RuleIgnoreActionOut"])
    types["GoogleCloudRetailV2SearchRequestPersonalizationSpecIn"] = t.struct(
        {"mode": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2SearchRequestPersonalizationSpecIn"])
    types["GoogleCloudRetailV2SearchRequestPersonalizationSpecOut"] = t.struct(
        {
            "mode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2SearchRequestPersonalizationSpecOut"])
    types["GoogleCloudRetailV2AddLocalInventoriesResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2AddLocalInventoriesResponseIn"])
    types["GoogleCloudRetailV2AddLocalInventoriesResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2AddLocalInventoriesResponseOut"])
    types["GoogleCloudRetailV2alphaPurgeMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2alphaPurgeMetadataIn"])
    types["GoogleCloudRetailV2alphaPurgeMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2alphaPurgeMetadataOut"])
    types["GoogleCloudRetailV2betaRemoveLocalInventoriesResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2betaRemoveLocalInventoriesResponseIn"])
    types["GoogleCloudRetailV2betaRemoveLocalInventoriesResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2betaRemoveLocalInventoriesResponseOut"])
    types["GoogleCloudRetailV2betaAddFulfillmentPlacesResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2betaAddFulfillmentPlacesResponseIn"])
    types["GoogleCloudRetailV2betaAddFulfillmentPlacesResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2betaAddFulfillmentPlacesResponseOut"])
    types["GoogleCloudRetailV2betaPurgeMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2betaPurgeMetadataIn"])
    types["GoogleCloudRetailV2betaPurgeMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2betaPurgeMetadataOut"])
    types["GoogleCloudRetailV2CompleteQueryResponseIn"] = t.struct(
        {
            "recentSearchResults": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudRetailV2CompleteQueryResponseRecentSearchResultIn"
                    ]
                )
            ).optional(),
            "completionResults": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudRetailV2CompleteQueryResponseCompletionResultIn"
                    ]
                )
            ).optional(),
            "attributionToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2CompleteQueryResponseIn"])
    types["GoogleCloudRetailV2CompleteQueryResponseOut"] = t.struct(
        {
            "recentSearchResults": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudRetailV2CompleteQueryResponseRecentSearchResultOut"
                    ]
                )
            ).optional(),
            "completionResults": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudRetailV2CompleteQueryResponseCompletionResultOut"
                    ]
                )
            ).optional(),
            "attributionToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2CompleteQueryResponseOut"])
    types["GoogleCloudRetailV2AddFulfillmentPlacesResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2AddFulfillmentPlacesResponseIn"])
    types["GoogleCloudRetailV2AddFulfillmentPlacesResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2AddFulfillmentPlacesResponseOut"])
    types["GoogleCloudRetailV2betaPurgeProductsMetadataIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "failureCount": t.string().optional(),
            "successCount": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2betaPurgeProductsMetadataIn"])
    types["GoogleCloudRetailV2betaPurgeProductsMetadataOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "failureCount": t.string().optional(),
            "successCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2betaPurgeProductsMetadataOut"])
    types["GoogleCloudRetailV2betaImportErrorsConfigIn"] = t.struct(
        {"gcsPrefix": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2betaImportErrorsConfigIn"])
    types["GoogleCloudRetailV2betaImportErrorsConfigOut"] = t.struct(
        {
            "gcsPrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2betaImportErrorsConfigOut"])
    types["GoogleCloudRetailV2betaAddLocalInventoriesResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2betaAddLocalInventoriesResponseIn"])
    types["GoogleCloudRetailV2betaAddLocalInventoriesResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2betaAddLocalInventoriesResponseOut"])
    types["GoogleCloudRetailLoggingSourceLocationIn"] = t.struct(
        {"functionName": t.string().optional()}
    ).named(renames["GoogleCloudRetailLoggingSourceLocationIn"])
    types["GoogleCloudRetailLoggingSourceLocationOut"] = t.struct(
        {
            "functionName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailLoggingSourceLocationOut"])
    types["GoogleCloudRetailV2alphaUserEventImportSummaryIn"] = t.struct(
        {
            "unjoinedEventsCount": t.string().optional(),
            "joinedEventsCount": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaUserEventImportSummaryIn"])
    types["GoogleCloudRetailV2alphaUserEventImportSummaryOut"] = t.struct(
        {
            "unjoinedEventsCount": t.string().optional(),
            "joinedEventsCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaUserEventImportSummaryOut"])
    types["GoogleCloudRetailV2ExperimentInfoIn"] = t.struct(
        {
            "servingConfigExperiment": t.proxy(
                renames["GoogleCloudRetailV2ExperimentInfoServingConfigExperimentIn"]
            ).optional(),
            "experiment": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2ExperimentInfoIn"])
    types["GoogleCloudRetailV2ExperimentInfoOut"] = t.struct(
        {
            "servingConfigExperiment": t.proxy(
                renames["GoogleCloudRetailV2ExperimentInfoServingConfigExperimentOut"]
            ).optional(),
            "experiment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ExperimentInfoOut"])
    types["GoogleCloudRetailV2RuleFilterActionIn"] = t.struct(
        {"filter": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2RuleFilterActionIn"])
    types["GoogleCloudRetailV2RuleFilterActionOut"] = t.struct(
        {
            "filter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2RuleFilterActionOut"])
    types["GoogleCloudRetailV2PriceInfoPriceRangeIn"] = t.struct(
        {
            "price": t.proxy(renames["GoogleCloudRetailV2IntervalIn"]).optional(),
            "originalPrice": t.proxy(
                renames["GoogleCloudRetailV2IntervalIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudRetailV2PriceInfoPriceRangeIn"])
    types["GoogleCloudRetailV2PriceInfoPriceRangeOut"] = t.struct(
        {
            "price": t.proxy(renames["GoogleCloudRetailV2IntervalOut"]).optional(),
            "originalPrice": t.proxy(
                renames["GoogleCloudRetailV2IntervalOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2PriceInfoPriceRangeOut"])
    types["GoogleCloudRetailV2betaGcsOutputResultIn"] = t.struct(
        {"outputUri": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2betaGcsOutputResultIn"])
    types["GoogleCloudRetailV2betaGcsOutputResultOut"] = t.struct(
        {
            "outputUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2betaGcsOutputResultOut"])
    types["GoogleCloudRetailV2PurgeMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2PurgeMetadataIn"])
    types["GoogleCloudRetailV2PurgeMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2PurgeMetadataOut"])
    types["GoogleCloudRetailV2TuneModelResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2TuneModelResponseIn"])
    types["GoogleCloudRetailV2TuneModelResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2TuneModelResponseOut"])
    types["GoogleCloudRetailV2CustomAttributeIn"] = t.struct(
        {
            "indexable": t.boolean().optional(),
            "numbers": t.array(t.number()).optional(),
            "text": t.array(t.string()).optional(),
            "searchable": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudRetailV2CustomAttributeIn"])
    types["GoogleCloudRetailV2CustomAttributeOut"] = t.struct(
        {
            "indexable": t.boolean().optional(),
            "numbers": t.array(t.number()).optional(),
            "text": t.array(t.string()).optional(),
            "searchable": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2CustomAttributeOut"])
    types["GoogleCloudRetailV2betaAddLocalInventoriesMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2betaAddLocalInventoriesMetadataIn"])
    types["GoogleCloudRetailV2betaAddLocalInventoriesMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2betaAddLocalInventoriesMetadataOut"])
    types["GoogleCloudRetailV2ImportCompletionDataResponseIn"] = t.struct(
        {"errorSamples": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional()}
    ).named(renames["GoogleCloudRetailV2ImportCompletionDataResponseIn"])
    types["GoogleCloudRetailV2ImportCompletionDataResponseOut"] = t.struct(
        {
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ImportCompletionDataResponseOut"])
    types["GoogleCloudRetailV2ProductInputConfigIn"] = t.struct(
        {
            "productInlineSource": t.proxy(
                renames["GoogleCloudRetailV2ProductInlineSourceIn"]
            ).optional(),
            "gcsSource": t.proxy(renames["GoogleCloudRetailV2GcsSourceIn"]).optional(),
            "bigQuerySource": t.proxy(
                renames["GoogleCloudRetailV2BigQuerySourceIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ProductInputConfigIn"])
    types["GoogleCloudRetailV2ProductInputConfigOut"] = t.struct(
        {
            "productInlineSource": t.proxy(
                renames["GoogleCloudRetailV2ProductInlineSourceOut"]
            ).optional(),
            "gcsSource": t.proxy(renames["GoogleCloudRetailV2GcsSourceOut"]).optional(),
            "bigQuerySource": t.proxy(
                renames["GoogleCloudRetailV2BigQuerySourceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ProductInputConfigOut"])
    types["GoogleCloudRetailV2SearchRequestIn"] = t.struct(
        {
            "pageToken": t.string().optional(),
            "offset": t.integer().optional(),
            "spellCorrectionSpec": t.proxy(
                renames["GoogleCloudRetailV2SearchRequestSpellCorrectionSpecIn"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "pageSize": t.integer().optional(),
            "query": t.string().optional(),
            "searchMode": t.string().optional(),
            "dynamicFacetSpec": t.proxy(
                renames["GoogleCloudRetailV2SearchRequestDynamicFacetSpecIn"]
            ).optional(),
            "personalizationSpec": t.proxy(
                renames["GoogleCloudRetailV2SearchRequestPersonalizationSpecIn"]
            ).optional(),
            "visitorId": t.string(),
            "userInfo": t.proxy(renames["GoogleCloudRetailV2UserInfoIn"]).optional(),
            "branch": t.string().optional(),
            "boostSpec": t.proxy(
                renames["GoogleCloudRetailV2SearchRequestBoostSpecIn"]
            ).optional(),
            "orderBy": t.string().optional(),
            "filter": t.string().optional(),
            "variantRollupKeys": t.array(t.string()).optional(),
            "pageCategories": t.array(t.string()).optional(),
            "facetSpecs": t.array(
                t.proxy(renames["GoogleCloudRetailV2SearchRequestFacetSpecIn"])
            ).optional(),
            "canonicalFilter": t.string().optional(),
            "entity": t.string().optional(),
            "queryExpansionSpec": t.proxy(
                renames["GoogleCloudRetailV2SearchRequestQueryExpansionSpecIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudRetailV2SearchRequestIn"])
    types["GoogleCloudRetailV2SearchRequestOut"] = t.struct(
        {
            "pageToken": t.string().optional(),
            "offset": t.integer().optional(),
            "spellCorrectionSpec": t.proxy(
                renames["GoogleCloudRetailV2SearchRequestSpellCorrectionSpecOut"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "pageSize": t.integer().optional(),
            "query": t.string().optional(),
            "searchMode": t.string().optional(),
            "dynamicFacetSpec": t.proxy(
                renames["GoogleCloudRetailV2SearchRequestDynamicFacetSpecOut"]
            ).optional(),
            "personalizationSpec": t.proxy(
                renames["GoogleCloudRetailV2SearchRequestPersonalizationSpecOut"]
            ).optional(),
            "visitorId": t.string(),
            "userInfo": t.proxy(renames["GoogleCloudRetailV2UserInfoOut"]).optional(),
            "branch": t.string().optional(),
            "boostSpec": t.proxy(
                renames["GoogleCloudRetailV2SearchRequestBoostSpecOut"]
            ).optional(),
            "orderBy": t.string().optional(),
            "filter": t.string().optional(),
            "variantRollupKeys": t.array(t.string()).optional(),
            "pageCategories": t.array(t.string()).optional(),
            "facetSpecs": t.array(
                t.proxy(renames["GoogleCloudRetailV2SearchRequestFacetSpecOut"])
            ).optional(),
            "canonicalFilter": t.string().optional(),
            "entity": t.string().optional(),
            "queryExpansionSpec": t.proxy(
                renames["GoogleCloudRetailV2SearchRequestQueryExpansionSpecOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2SearchRequestOut"])
    types["GoogleCloudRetailV2SearchResponseFacetIn"] = t.struct(
        {
            "dynamicFacet": t.boolean().optional(),
            "values": t.array(
                t.proxy(renames["GoogleCloudRetailV2SearchResponseFacetFacetValueIn"])
            ).optional(),
            "key": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2SearchResponseFacetIn"])
    types["GoogleCloudRetailV2SearchResponseFacetOut"] = t.struct(
        {
            "dynamicFacet": t.boolean().optional(),
            "values": t.array(
                t.proxy(renames["GoogleCloudRetailV2SearchResponseFacetFacetValueOut"])
            ).optional(),
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2SearchResponseFacetOut"])
    types["GoogleCloudRetailV2ListServingConfigsResponseIn"] = t.struct(
        {
            "servingConfigs": t.array(
                t.proxy(renames["GoogleCloudRetailV2ServingConfigIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2ListServingConfigsResponseIn"])
    types["GoogleCloudRetailV2ListServingConfigsResponseOut"] = t.struct(
        {
            "servingConfigs": t.array(
                t.proxy(renames["GoogleCloudRetailV2ServingConfigOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ListServingConfigsResponseOut"])
    types["GoogleCloudRetailV2ResumeModelRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2ResumeModelRequestIn"])
    types["GoogleCloudRetailV2ResumeModelRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2ResumeModelRequestOut"])
    types["GoogleCloudRetailV2betaSetInventoryResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2betaSetInventoryResponseIn"])
    types["GoogleCloudRetailV2betaSetInventoryResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2betaSetInventoryResponseOut"])
    types[
        "GoogleCloudRetailV2alphaCreateMerchantCenterAccountLinkMetadataIn"
    ] = t.struct(
        {"updateTime": t.string().optional(), "createTime": t.string().optional()}
    ).named(
        renames["GoogleCloudRetailV2alphaCreateMerchantCenterAccountLinkMetadataIn"]
    )
    types[
        "GoogleCloudRetailV2alphaCreateMerchantCenterAccountLinkMetadataOut"
    ] = t.struct(
        {
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudRetailV2alphaCreateMerchantCenterAccountLinkMetadataOut"]
    )
    types["GoogleCloudRetailV2SetInventoryRequestIn"] = t.struct(
        {
            "inventory": t.proxy(renames["GoogleCloudRetailV2ProductIn"]),
            "setMask": t.string().optional(),
            "allowMissing": t.boolean().optional(),
            "setTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2SetInventoryRequestIn"])
    types["GoogleCloudRetailV2SetInventoryRequestOut"] = t.struct(
        {
            "inventory": t.proxy(renames["GoogleCloudRetailV2ProductOut"]),
            "setMask": t.string().optional(),
            "allowMissing": t.boolean().optional(),
            "setTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2SetInventoryRequestOut"])
    types["GoogleCloudRetailV2CompletionDetailIn"] = t.struct(
        {
            "selectedPosition": t.integer().optional(),
            "selectedSuggestion": t.string().optional(),
            "completionAttributionToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2CompletionDetailIn"])
    types["GoogleCloudRetailV2CompletionDetailOut"] = t.struct(
        {
            "selectedPosition": t.integer().optional(),
            "selectedSuggestion": t.string().optional(),
            "completionAttributionToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2CompletionDetailOut"])
    types["GoogleCloudRetailV2CompleteQueryResponseRecentSearchResultIn"] = t.struct(
        {"recentSearch": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2CompleteQueryResponseRecentSearchResultIn"])
    types["GoogleCloudRetailV2CompleteQueryResponseRecentSearchResultOut"] = t.struct(
        {
            "recentSearch": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2CompleteQueryResponseRecentSearchResultOut"])
    types["GoogleTypeDateIn"] = t.struct(
        {
            "month": t.integer().optional(),
            "day": t.integer().optional(),
            "year": t.integer().optional(),
        }
    ).named(renames["GoogleTypeDateIn"])
    types["GoogleTypeDateOut"] = t.struct(
        {
            "month": t.integer().optional(),
            "day": t.integer().optional(),
            "year": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeDateOut"])
    types["GoogleCloudRetailV2alphaAddLocalInventoriesResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2alphaAddLocalInventoriesResponseIn"])
    types["GoogleCloudRetailV2alphaAddLocalInventoriesResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2alphaAddLocalInventoriesResponseOut"])
    types["GoogleCloudRetailV2PurgeProductsRequestIn"] = t.struct(
        {"filter": t.string(), "force": t.boolean().optional()}
    ).named(renames["GoogleCloudRetailV2PurgeProductsRequestIn"])
    types["GoogleCloudRetailV2PurgeProductsRequestOut"] = t.struct(
        {
            "filter": t.string(),
            "force": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2PurgeProductsRequestOut"])
    types["GoogleCloudRetailV2alphaCreateModelMetadataIn"] = t.struct(
        {"model": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2alphaCreateModelMetadataIn"])
    types["GoogleCloudRetailV2alphaCreateModelMetadataOut"] = t.struct(
        {
            "model": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaCreateModelMetadataOut"])
    types["GoogleCloudRetailV2alphaPurgeUserEventsResponseIn"] = t.struct(
        {"purgedEventsCount": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2alphaPurgeUserEventsResponseIn"])
    types["GoogleCloudRetailV2alphaPurgeUserEventsResponseOut"] = t.struct(
        {
            "purgedEventsCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaPurgeUserEventsResponseOut"])
    types["GoogleCloudRetailV2ImportCompletionDataRequestIn"] = t.struct(
        {
            "notificationPubsubTopic": t.string().optional(),
            "inputConfig": t.proxy(
                renames["GoogleCloudRetailV2CompletionDataInputConfigIn"]
            ),
        }
    ).named(renames["GoogleCloudRetailV2ImportCompletionDataRequestIn"])
    types["GoogleCloudRetailV2ImportCompletionDataRequestOut"] = t.struct(
        {
            "notificationPubsubTopic": t.string().optional(),
            "inputConfig": t.proxy(
                renames["GoogleCloudRetailV2CompletionDataInputConfigOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ImportCompletionDataRequestOut"])
    types["GoogleCloudRetailV2betaMerchantCenterAccountLinkIn"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "merchantCenterAccountId": t.string(),
            "source": t.string().optional(),
            "feedLabel": t.string().optional(),
            "branchId": t.string(),
            "feedFilters": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudRetailV2betaMerchantCenterAccountLinkMerchantCenterFeedFilterIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudRetailV2betaMerchantCenterAccountLinkIn"])
    types["GoogleCloudRetailV2betaMerchantCenterAccountLinkOut"] = t.struct(
        {
            "state": t.string().optional(),
            "languageCode": t.string().optional(),
            "name": t.string().optional(),
            "id": t.string().optional(),
            "merchantCenterAccountId": t.string(),
            "source": t.string().optional(),
            "feedLabel": t.string().optional(),
            "projectId": t.string().optional(),
            "branchId": t.string(),
            "feedFilters": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudRetailV2betaMerchantCenterAccountLinkMerchantCenterFeedFilterOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2betaMerchantCenterAccountLinkOut"])
    types["GoogleCloudRetailV2GetDefaultBranchResponseIn"] = t.struct(
        {
            "branch": t.string().optional(),
            "note": t.string().optional(),
            "setTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2GetDefaultBranchResponseIn"])
    types["GoogleCloudRetailV2GetDefaultBranchResponseOut"] = t.struct(
        {
            "branch": t.string().optional(),
            "note": t.string().optional(),
            "setTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2GetDefaultBranchResponseOut"])
    types["GoogleCloudRetailV2betaTuneModelResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2betaTuneModelResponseIn"])
    types["GoogleCloudRetailV2betaTuneModelResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2betaTuneModelResponseOut"])
    types["GoogleCloudRetailV2ControlIn"] = t.struct(
        {
            "searchSolutionUseCase": t.array(t.string()).optional(),
            "displayName": t.string(),
            "rule": t.proxy(renames["GoogleCloudRetailV2RuleIn"]).optional(),
            "solutionTypes": t.array(t.string()),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2ControlIn"])
    types["GoogleCloudRetailV2ControlOut"] = t.struct(
        {
            "associatedServingConfigIds": t.array(t.string()).optional(),
            "searchSolutionUseCase": t.array(t.string()).optional(),
            "displayName": t.string(),
            "rule": t.proxy(renames["GoogleCloudRetailV2RuleOut"]).optional(),
            "solutionTypes": t.array(t.string()),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ControlOut"])
    types["GoogleCloudRetailV2PurgeProductsResponseIn"] = t.struct(
        {
            "purgeCount": t.string().optional(),
            "purgeSample": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudRetailV2PurgeProductsResponseIn"])
    types["GoogleCloudRetailV2PurgeProductsResponseOut"] = t.struct(
        {
            "purgeCount": t.string().optional(),
            "purgeSample": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2PurgeProductsResponseOut"])
    types["GoogleCloudRetailV2PurgeProductsMetadataIn"] = t.struct(
        {
            "successCount": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "failureCount": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2PurgeProductsMetadataIn"])
    types["GoogleCloudRetailV2PurgeProductsMetadataOut"] = t.struct(
        {
            "successCount": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "failureCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2PurgeProductsMetadataOut"])
    types["GoogleCloudRetailV2SearchResponseSearchResultIn"] = t.struct(
        {
            "variantRollupValues": t.struct({"_": t.string().optional()}).optional(),
            "personalLabels": t.array(t.string()).optional(),
            "matchingVariantCount": t.integer().optional(),
            "id": t.string().optional(),
            "product": t.proxy(renames["GoogleCloudRetailV2ProductIn"]).optional(),
            "matchingVariantFields": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudRetailV2SearchResponseSearchResultIn"])
    types["GoogleCloudRetailV2SearchResponseSearchResultOut"] = t.struct(
        {
            "variantRollupValues": t.struct({"_": t.string().optional()}).optional(),
            "personalLabels": t.array(t.string()).optional(),
            "matchingVariantCount": t.integer().optional(),
            "id": t.string().optional(),
            "product": t.proxy(renames["GoogleCloudRetailV2ProductOut"]).optional(),
            "matchingVariantFields": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2SearchResponseSearchResultOut"])
    types["GoogleCloudRetailV2ExperimentInfoServingConfigExperimentIn"] = t.struct(
        {
            "originalServingConfig": t.string().optional(),
            "experimentServingConfig": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2ExperimentInfoServingConfigExperimentIn"])
    types["GoogleCloudRetailV2ExperimentInfoServingConfigExperimentOut"] = t.struct(
        {
            "originalServingConfig": t.string().optional(),
            "experimentServingConfig": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ExperimentInfoServingConfigExperimentOut"])
    types["GoogleCloudRetailV2ImportProductsResponseIn"] = t.struct(
        {
            "errorsConfig": t.proxy(
                renames["GoogleCloudRetailV2ImportErrorsConfigIn"]
            ).optional(),
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ImportProductsResponseIn"])
    types["GoogleCloudRetailV2ImportProductsResponseOut"] = t.struct(
        {
            "errorsConfig": t.proxy(
                renames["GoogleCloudRetailV2ImportErrorsConfigOut"]
            ).optional(),
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ImportProductsResponseOut"])
    types["GoogleCloudRetailV2RemoveFulfillmentPlacesResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2RemoveFulfillmentPlacesResponseIn"])
    types["GoogleCloudRetailV2RemoveFulfillmentPlacesResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2RemoveFulfillmentPlacesResponseOut"])
    types["GoogleCloudRetailV2SearchRequestDynamicFacetSpecIn"] = t.struct(
        {"mode": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2SearchRequestDynamicFacetSpecIn"])
    types["GoogleCloudRetailV2SearchRequestDynamicFacetSpecOut"] = t.struct(
        {
            "mode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2SearchRequestDynamicFacetSpecOut"])
    types["GoogleCloudRetailV2ProductInlineSourceIn"] = t.struct(
        {"products": t.array(t.proxy(renames["GoogleCloudRetailV2ProductIn"]))}
    ).named(renames["GoogleCloudRetailV2ProductInlineSourceIn"])
    types["GoogleCloudRetailV2ProductInlineSourceOut"] = t.struct(
        {
            "products": t.array(t.proxy(renames["GoogleCloudRetailV2ProductOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ProductInlineSourceOut"])
    types["GoogleCloudRetailV2ModelIn"] = t.struct(
        {
            "periodicTuningState": t.string().optional(),
            "trainingState": t.string().optional(),
            "type": t.string(),
            "modelFeaturesConfig": t.proxy(
                renames["GoogleCloudRetailV2ModelModelFeaturesConfigIn"]
            ).optional(),
            "displayName": t.string(),
            "optimizationObjective": t.string().optional(),
            "filteringOption": t.string().optional(),
            "name": t.string(),
        }
    ).named(renames["GoogleCloudRetailV2ModelIn"])
    types["GoogleCloudRetailV2ModelOut"] = t.struct(
        {
            "periodicTuningState": t.string().optional(),
            "trainingState": t.string().optional(),
            "type": t.string(),
            "lastTuneTime": t.string().optional(),
            "modelFeaturesConfig": t.proxy(
                renames["GoogleCloudRetailV2ModelModelFeaturesConfigOut"]
            ).optional(),
            "servingState": t.string().optional(),
            "updateTime": t.string().optional(),
            "displayName": t.string(),
            "optimizationObjective": t.string().optional(),
            "createTime": t.string().optional(),
            "filteringOption": t.string().optional(),
            "dataState": t.string().optional(),
            "name": t.string(),
            "servingConfigLists": t.array(
                t.proxy(renames["GoogleCloudRetailV2ModelServingConfigListOut"])
            ).optional(),
            "tuningOperation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ModelOut"])
    types["GoogleCloudRetailV2PredictResponsePredictionResultIn"] = t.struct(
        {
            "id": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudRetailV2PredictResponsePredictionResultIn"])
    types["GoogleCloudRetailV2PredictResponsePredictionResultOut"] = t.struct(
        {
            "id": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2PredictResponsePredictionResultOut"])
    types["GoogleCloudRetailV2betaUserEventImportSummaryIn"] = t.struct(
        {
            "unjoinedEventsCount": t.string().optional(),
            "joinedEventsCount": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2betaUserEventImportSummaryIn"])
    types["GoogleCloudRetailV2betaUserEventImportSummaryOut"] = t.struct(
        {
            "unjoinedEventsCount": t.string().optional(),
            "joinedEventsCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2betaUserEventImportSummaryOut"])
    types["GoogleCloudRetailV2betaRemoveFulfillmentPlacesMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2betaRemoveFulfillmentPlacesMetadataIn"])
    types["GoogleCloudRetailV2betaRemoveFulfillmentPlacesMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2betaRemoveFulfillmentPlacesMetadataOut"])
    types["GoogleCloudRetailV2ConditionTimeRangeIn"] = t.struct(
        {"startTime": t.string().optional(), "endTime": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2ConditionTimeRangeIn"])
    types["GoogleCloudRetailV2ConditionTimeRangeOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ConditionTimeRangeOut"])
    types["GoogleCloudRetailV2alphaSetInventoryResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2alphaSetInventoryResponseIn"])
    types["GoogleCloudRetailV2alphaSetInventoryResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2alphaSetInventoryResponseOut"])
    types["GoogleCloudRetailV2SearchRequestSpellCorrectionSpecIn"] = t.struct(
        {"mode": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2SearchRequestSpellCorrectionSpecIn"])
    types["GoogleCloudRetailV2SearchRequestSpellCorrectionSpecOut"] = t.struct(
        {
            "mode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2SearchRequestSpellCorrectionSpecOut"])
    types["GoogleCloudRetailV2alphaBigQueryOutputResultIn"] = t.struct(
        {"tableId": t.string().optional(), "datasetId": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2alphaBigQueryOutputResultIn"])
    types["GoogleCloudRetailV2alphaBigQueryOutputResultOut"] = t.struct(
        {
            "tableId": t.string().optional(),
            "datasetId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaBigQueryOutputResultOut"])
    types["GoogleCloudRetailV2alphaModelServingConfigListIn"] = t.struct(
        {"servingConfigIds": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudRetailV2alphaModelServingConfigListIn"])
    types["GoogleCloudRetailV2alphaModelServingConfigListOut"] = t.struct(
        {
            "servingConfigIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaModelServingConfigListOut"])
    types["GoogleCloudRetailV2alphaExportProductsResponseIn"] = t.struct(
        {
            "errorsConfig": t.proxy(
                renames["GoogleCloudRetailV2alphaExportErrorsConfigIn"]
            ).optional(),
            "outputResult": t.proxy(
                renames["GoogleCloudRetailV2alphaOutputResultIn"]
            ).optional(),
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaExportProductsResponseIn"])
    types["GoogleCloudRetailV2alphaExportProductsResponseOut"] = t.struct(
        {
            "errorsConfig": t.proxy(
                renames["GoogleCloudRetailV2alphaExportErrorsConfigOut"]
            ).optional(),
            "outputResult": t.proxy(
                renames["GoogleCloudRetailV2alphaOutputResultOut"]
            ).optional(),
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaExportProductsResponseOut"])
    types["GoogleCloudRetailV2betaExportErrorsConfigIn"] = t.struct(
        {"gcsPrefix": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2betaExportErrorsConfigIn"])
    types["GoogleCloudRetailV2betaExportErrorsConfigOut"] = t.struct(
        {
            "gcsPrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2betaExportErrorsConfigOut"])
    types["GoogleCloudRetailV2PurchaseTransactionIn"] = t.struct(
        {
            "id": t.string().optional(),
            "revenue": t.number(),
            "cost": t.number().optional(),
            "currencyCode": t.string(),
            "tax": t.number().optional(),
        }
    ).named(renames["GoogleCloudRetailV2PurchaseTransactionIn"])
    types["GoogleCloudRetailV2PurchaseTransactionOut"] = t.struct(
        {
            "id": t.string().optional(),
            "revenue": t.number(),
            "cost": t.number().optional(),
            "currencyCode": t.string(),
            "tax": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2PurchaseTransactionOut"])
    types["GoogleCloudRetailV2alphaRemoveFulfillmentPlacesMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2alphaRemoveFulfillmentPlacesMetadataIn"])
    types["GoogleCloudRetailV2alphaRemoveFulfillmentPlacesMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2alphaRemoveFulfillmentPlacesMetadataOut"])
    types["GoogleCloudRetailV2alphaImportMetadataIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "transformedUserEventsMetadata": t.proxy(
                renames["GoogleCloudRetailV2alphaTransformedUserEventsMetadataIn"]
            ).optional(),
            "createTime": t.string().optional(),
            "notificationPubsubTopic": t.string().optional(),
            "failureCount": t.string().optional(),
            "successCount": t.string().optional(),
            "requestId": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaImportMetadataIn"])
    types["GoogleCloudRetailV2alphaImportMetadataOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "transformedUserEventsMetadata": t.proxy(
                renames["GoogleCloudRetailV2alphaTransformedUserEventsMetadataOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "notificationPubsubTopic": t.string().optional(),
            "failureCount": t.string().optional(),
            "successCount": t.string().optional(),
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaImportMetadataOut"])
    types["GoogleCloudRetailV2alphaModelPageOptimizationConfigIn"] = t.struct(
        {
            "panels": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudRetailV2alphaModelPageOptimizationConfigPanelIn"
                    ]
                )
            ),
            "restriction": t.string().optional(),
            "pageOptimizationEventType": t.string(),
        }
    ).named(renames["GoogleCloudRetailV2alphaModelPageOptimizationConfigIn"])
    types["GoogleCloudRetailV2alphaModelPageOptimizationConfigOut"] = t.struct(
        {
            "panels": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudRetailV2alphaModelPageOptimizationConfigPanelOut"
                    ]
                )
            ),
            "restriction": t.string().optional(),
            "pageOptimizationEventType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaModelPageOptimizationConfigOut"])
    types["GoogleCloudRetailV2betaPurgeProductsResponseIn"] = t.struct(
        {
            "purgeCount": t.string().optional(),
            "purgeSample": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudRetailV2betaPurgeProductsResponseIn"])
    types["GoogleCloudRetailV2betaPurgeProductsResponseOut"] = t.struct(
        {
            "purgeCount": t.string().optional(),
            "purgeSample": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2betaPurgeProductsResponseOut"])
    types["GoogleCloudRetailV2alphaModelPageOptimizationConfigCandidateIn"] = t.struct(
        {"servingConfigId": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2alphaModelPageOptimizationConfigCandidateIn"])
    types["GoogleCloudRetailV2alphaModelPageOptimizationConfigCandidateOut"] = t.struct(
        {
            "servingConfigId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaModelPageOptimizationConfigCandidateOut"])
    types["GoogleCloudRetailV2BigQuerySourceIn"] = t.struct(
        {
            "projectId": t.string().optional(),
            "datasetId": t.string(),
            "partitionDate": t.proxy(renames["GoogleTypeDateIn"]).optional(),
            "tableId": t.string(),
            "gcsStagingDir": t.string().optional(),
            "dataSchema": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2BigQuerySourceIn"])
    types["GoogleCloudRetailV2BigQuerySourceOut"] = t.struct(
        {
            "projectId": t.string().optional(),
            "datasetId": t.string(),
            "partitionDate": t.proxy(renames["GoogleTypeDateOut"]).optional(),
            "tableId": t.string(),
            "gcsStagingDir": t.string().optional(),
            "dataSchema": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2BigQuerySourceOut"])
    types["GoogleCloudRetailV2alphaExportMetadataIn"] = t.struct(
        {"updateTime": t.string().optional(), "createTime": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2alphaExportMetadataIn"])
    types["GoogleCloudRetailV2alphaExportMetadataOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaExportMetadataOut"])
    types["GoogleCloudRetailV2RemoveLocalInventoriesRequestIn"] = t.struct(
        {
            "allowMissing": t.boolean().optional(),
            "placeIds": t.array(t.string()),
            "removeTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2RemoveLocalInventoriesRequestIn"])
    types["GoogleCloudRetailV2RemoveLocalInventoriesRequestOut"] = t.struct(
        {
            "allowMissing": t.boolean().optional(),
            "placeIds": t.array(t.string()),
            "removeTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2RemoveLocalInventoriesRequestOut"])
    types["GoogleCloudRetailV2betaRejoinUserEventsResponseIn"] = t.struct(
        {"rejoinedUserEventsCount": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2betaRejoinUserEventsResponseIn"])
    types["GoogleCloudRetailV2betaRejoinUserEventsResponseOut"] = t.struct(
        {
            "rejoinedUserEventsCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2betaRejoinUserEventsResponseOut"])
    types["GoogleCloudRetailV2RejoinUserEventsResponseIn"] = t.struct(
        {"rejoinedUserEventsCount": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2RejoinUserEventsResponseIn"])
    types["GoogleCloudRetailV2RejoinUserEventsResponseOut"] = t.struct(
        {
            "rejoinedUserEventsCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2RejoinUserEventsResponseOut"])
    types["GoogleCloudRetailV2alphaImportProductsResponseIn"] = t.struct(
        {
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional(),
            "errorsConfig": t.proxy(
                renames["GoogleCloudRetailV2alphaImportErrorsConfigIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaImportProductsResponseIn"])
    types["GoogleCloudRetailV2alphaImportProductsResponseOut"] = t.struct(
        {
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "errorsConfig": t.proxy(
                renames["GoogleCloudRetailV2alphaImportErrorsConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaImportProductsResponseOut"])
    types["GoogleCloudRetailV2PurgeUserEventsRequestIn"] = t.struct(
        {"filter": t.string(), "force": t.boolean().optional()}
    ).named(renames["GoogleCloudRetailV2PurgeUserEventsRequestIn"])
    types["GoogleCloudRetailV2PurgeUserEventsRequestOut"] = t.struct(
        {
            "filter": t.string(),
            "force": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2PurgeUserEventsRequestOut"])
    types["GoogleCloudRetailV2ColorInfoIn"] = t.struct(
        {
            "colors": t.array(t.string()).optional(),
            "colorFamilies": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ColorInfoIn"])
    types["GoogleCloudRetailV2ColorInfoOut"] = t.struct(
        {
            "colors": t.array(t.string()).optional(),
            "colorFamilies": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ColorInfoOut"])
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
    types["GoogleCloudRetailV2alphaOutputResultIn"] = t.struct(
        {
            "bigqueryResult": t.array(
                t.proxy(renames["GoogleCloudRetailV2alphaBigQueryOutputResultIn"])
            ).optional(),
            "gcsResult": t.array(
                t.proxy(renames["GoogleCloudRetailV2alphaGcsOutputResultIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaOutputResultIn"])
    types["GoogleCloudRetailV2alphaOutputResultOut"] = t.struct(
        {
            "bigqueryResult": t.array(
                t.proxy(renames["GoogleCloudRetailV2alphaBigQueryOutputResultOut"])
            ).optional(),
            "gcsResult": t.array(
                t.proxy(renames["GoogleCloudRetailV2alphaGcsOutputResultOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaOutputResultOut"])
    types["GoogleCloudRetailV2betaBigQueryOutputResultIn"] = t.struct(
        {"tableId": t.string().optional(), "datasetId": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2betaBigQueryOutputResultIn"])
    types["GoogleCloudRetailV2betaBigQueryOutputResultOut"] = t.struct(
        {
            "tableId": t.string().optional(),
            "datasetId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2betaBigQueryOutputResultOut"])
    types["GoogleCloudRetailV2SearchResponseQueryExpansionInfoIn"] = t.struct(
        {
            "pinnedResultCount": t.string().optional(),
            "expandedQuery": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudRetailV2SearchResponseQueryExpansionInfoIn"])
    types["GoogleCloudRetailV2SearchResponseQueryExpansionInfoOut"] = t.struct(
        {
            "pinnedResultCount": t.string().optional(),
            "expandedQuery": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2SearchResponseQueryExpansionInfoOut"])
    types["GoogleCloudRetailV2RejoinUserEventsRequestIn"] = t.struct(
        {"userEventRejoinScope": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2RejoinUserEventsRequestIn"])
    types["GoogleCloudRetailV2RejoinUserEventsRequestOut"] = t.struct(
        {
            "userEventRejoinScope": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2RejoinUserEventsRequestOut"])
    types["GoogleCloudRetailV2RuleOnewaySynonymsActionIn"] = t.struct(
        {
            "onewayTerms": t.array(t.string()).optional(),
            "synonyms": t.array(t.string()).optional(),
            "queryTerms": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudRetailV2RuleOnewaySynonymsActionIn"])
    types["GoogleCloudRetailV2RuleOnewaySynonymsActionOut"] = t.struct(
        {
            "onewayTerms": t.array(t.string()).optional(),
            "synonyms": t.array(t.string()).optional(),
            "queryTerms": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2RuleOnewaySynonymsActionOut"])
    types["GoogleCloudRetailV2alphaMerchantCenterAccountLinkIn"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "feedFilters": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudRetailV2alphaMerchantCenterAccountLinkMerchantCenterFeedFilterIn"
                    ]
                )
            ).optional(),
            "feedLabel": t.string().optional(),
            "merchantCenterAccountId": t.string(),
            "branchId": t.string(),
            "source": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaMerchantCenterAccountLinkIn"])
    types["GoogleCloudRetailV2alphaMerchantCenterAccountLinkOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "feedFilters": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudRetailV2alphaMerchantCenterAccountLinkMerchantCenterFeedFilterOut"
                    ]
                )
            ).optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "id": t.string().optional(),
            "feedLabel": t.string().optional(),
            "merchantCenterAccountId": t.string(),
            "projectId": t.string().optional(),
            "branchId": t.string(),
            "source": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaMerchantCenterAccountLinkOut"])
    types[
        "GoogleCloudRetailV2betaModelFrequentlyBoughtTogetherFeaturesConfigIn"
    ] = t.struct({"contextProductsType": t.string().optional()}).named(
        renames["GoogleCloudRetailV2betaModelFrequentlyBoughtTogetherFeaturesConfigIn"]
    )
    types[
        "GoogleCloudRetailV2betaModelFrequentlyBoughtTogetherFeaturesConfigOut"
    ] = t.struct(
        {
            "contextProductsType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudRetailV2betaModelFrequentlyBoughtTogetherFeaturesConfigOut"]
    )
    types["GoogleCloudRetailV2ImportUserEventsResponseIn"] = t.struct(
        {
            "importSummary": t.proxy(
                renames["GoogleCloudRetailV2UserEventImportSummaryIn"]
            ).optional(),
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional(),
            "errorsConfig": t.proxy(
                renames["GoogleCloudRetailV2ImportErrorsConfigIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ImportUserEventsResponseIn"])
    types["GoogleCloudRetailV2ImportUserEventsResponseOut"] = t.struct(
        {
            "importSummary": t.proxy(
                renames["GoogleCloudRetailV2UserEventImportSummaryOut"]
            ).optional(),
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "errorsConfig": t.proxy(
                renames["GoogleCloudRetailV2ImportErrorsConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ImportUserEventsResponseOut"])
    types["GoogleCloudRetailV2betaCreateModelMetadataIn"] = t.struct(
        {"model": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2betaCreateModelMetadataIn"])
    types["GoogleCloudRetailV2betaCreateModelMetadataOut"] = t.struct(
        {
            "model": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2betaCreateModelMetadataOut"])
    types["GoogleCloudRetailV2UserInfoIn"] = t.struct(
        {
            "directUserRequest": t.boolean().optional(),
            "userId": t.string().optional(),
            "ipAddress": t.string().optional(),
            "userAgent": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2UserInfoIn"])
    types["GoogleCloudRetailV2UserInfoOut"] = t.struct(
        {
            "directUserRequest": t.boolean().optional(),
            "userId": t.string().optional(),
            "ipAddress": t.string().optional(),
            "userAgent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2UserInfoOut"])
    types["GoogleCloudRetailV2AttributesConfigIn"] = t.struct(
        {
            "catalogAttributes": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string(),
        }
    ).named(renames["GoogleCloudRetailV2AttributesConfigIn"])
    types["GoogleCloudRetailV2AttributesConfigOut"] = t.struct(
        {
            "catalogAttributes": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string(),
            "attributeConfigLevel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2AttributesConfigOut"])
    types["GoogleCloudRetailV2ModelModelFeaturesConfigIn"] = t.struct(
        {
            "frequentlyBoughtTogetherConfig": t.proxy(
                renames[
                    "GoogleCloudRetailV2ModelFrequentlyBoughtTogetherFeaturesConfigIn"
                ]
            ).optional()
        }
    ).named(renames["GoogleCloudRetailV2ModelModelFeaturesConfigIn"])
    types["GoogleCloudRetailV2ModelModelFeaturesConfigOut"] = t.struct(
        {
            "frequentlyBoughtTogetherConfig": t.proxy(
                renames[
                    "GoogleCloudRetailV2ModelFrequentlyBoughtTogetherFeaturesConfigOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ModelModelFeaturesConfigOut"])
    types["GoogleCloudRetailV2SearchRequestBoostSpecIn"] = t.struct(
        {
            "skipBoostSpecValidation": t.boolean().optional(),
            "conditionBoostSpecs": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudRetailV2SearchRequestBoostSpecConditionBoostSpecIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudRetailV2SearchRequestBoostSpecIn"])
    types["GoogleCloudRetailV2SearchRequestBoostSpecOut"] = t.struct(
        {
            "skipBoostSpecValidation": t.boolean().optional(),
            "conditionBoostSpecs": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudRetailV2SearchRequestBoostSpecConditionBoostSpecOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2SearchRequestBoostSpecOut"])

    functions = {}
    functions["projectsOperationsList"] = retail.get(
        "v2/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOperationsGet"] = retail.get(
        "v2/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = retail.get(
        "v2/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = retail.get(
        "v2/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsGetDefaultBranch"] = retail.get(
        "v2/{parent}/catalogs",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRetailV2ListCatalogsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsUpdateAttributesConfig"] = retail.get(
        "v2/{parent}/catalogs",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRetailV2ListCatalogsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsPatch"] = retail.get(
        "v2/{parent}/catalogs",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRetailV2ListCatalogsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsGetCompletionConfig"] = retail.get(
        "v2/{parent}/catalogs",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRetailV2ListCatalogsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsSetDefaultBranch"] = retail.get(
        "v2/{parent}/catalogs",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRetailV2ListCatalogsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsGetAttributesConfig"] = retail.get(
        "v2/{parent}/catalogs",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRetailV2ListCatalogsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsCompleteQuery"] = retail.get(
        "v2/{parent}/catalogs",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRetailV2ListCatalogsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsUpdateCompletionConfig"] = retail.get(
        "v2/{parent}/catalogs",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRetailV2ListCatalogsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsList"] = retail.get(
        "v2/{parent}/catalogs",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRetailV2ListCatalogsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsBranchesOperationsGet"] = retail.get(
        "v2/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsBranchesProductsList"] = retail.post(
        "v2/{parent}/products:import",
        t.struct(
            {
                "parent": t.string(),
                "reconciliationMode": t.string().optional(),
                "errorsConfig": t.proxy(
                    renames["GoogleCloudRetailV2ImportErrorsConfigIn"]
                ).optional(),
                "requestId": t.string().optional(),
                "updateMask": t.string().optional(),
                "inputConfig": t.proxy(
                    renames["GoogleCloudRetailV2ProductInputConfigIn"]
                ),
                "notificationPubsubTopic": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsBranchesProductsPurge"] = retail.post(
        "v2/{parent}/products:import",
        t.struct(
            {
                "parent": t.string(),
                "reconciliationMode": t.string().optional(),
                "errorsConfig": t.proxy(
                    renames["GoogleCloudRetailV2ImportErrorsConfigIn"]
                ).optional(),
                "requestId": t.string().optional(),
                "updateMask": t.string().optional(),
                "inputConfig": t.proxy(
                    renames["GoogleCloudRetailV2ProductInputConfigIn"]
                ),
                "notificationPubsubTopic": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsBranchesProductsCreate"] = retail.post(
        "v2/{parent}/products:import",
        t.struct(
            {
                "parent": t.string(),
                "reconciliationMode": t.string().optional(),
                "errorsConfig": t.proxy(
                    renames["GoogleCloudRetailV2ImportErrorsConfigIn"]
                ).optional(),
                "requestId": t.string().optional(),
                "updateMask": t.string().optional(),
                "inputConfig": t.proxy(
                    renames["GoogleCloudRetailV2ProductInputConfigIn"]
                ),
                "notificationPubsubTopic": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCatalogsBranchesProductsAddFulfillmentPlaces"
    ] = retail.post(
        "v2/{parent}/products:import",
        t.struct(
            {
                "parent": t.string(),
                "reconciliationMode": t.string().optional(),
                "errorsConfig": t.proxy(
                    renames["GoogleCloudRetailV2ImportErrorsConfigIn"]
                ).optional(),
                "requestId": t.string().optional(),
                "updateMask": t.string().optional(),
                "inputConfig": t.proxy(
                    renames["GoogleCloudRetailV2ProductInputConfigIn"]
                ),
                "notificationPubsubTopic": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsBranchesProductsPatch"] = retail.post(
        "v2/{parent}/products:import",
        t.struct(
            {
                "parent": t.string(),
                "reconciliationMode": t.string().optional(),
                "errorsConfig": t.proxy(
                    renames["GoogleCloudRetailV2ImportErrorsConfigIn"]
                ).optional(),
                "requestId": t.string().optional(),
                "updateMask": t.string().optional(),
                "inputConfig": t.proxy(
                    renames["GoogleCloudRetailV2ProductInputConfigIn"]
                ),
                "notificationPubsubTopic": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsBranchesProductsDelete"] = retail.post(
        "v2/{parent}/products:import",
        t.struct(
            {
                "parent": t.string(),
                "reconciliationMode": t.string().optional(),
                "errorsConfig": t.proxy(
                    renames["GoogleCloudRetailV2ImportErrorsConfigIn"]
                ).optional(),
                "requestId": t.string().optional(),
                "updateMask": t.string().optional(),
                "inputConfig": t.proxy(
                    renames["GoogleCloudRetailV2ProductInputConfigIn"]
                ),
                "notificationPubsubTopic": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsBranchesProductsSetInventory"] = retail.post(
        "v2/{parent}/products:import",
        t.struct(
            {
                "parent": t.string(),
                "reconciliationMode": t.string().optional(),
                "errorsConfig": t.proxy(
                    renames["GoogleCloudRetailV2ImportErrorsConfigIn"]
                ).optional(),
                "requestId": t.string().optional(),
                "updateMask": t.string().optional(),
                "inputConfig": t.proxy(
                    renames["GoogleCloudRetailV2ProductInputConfigIn"]
                ),
                "notificationPubsubTopic": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsBranchesProductsGet"] = retail.post(
        "v2/{parent}/products:import",
        t.struct(
            {
                "parent": t.string(),
                "reconciliationMode": t.string().optional(),
                "errorsConfig": t.proxy(
                    renames["GoogleCloudRetailV2ImportErrorsConfigIn"]
                ).optional(),
                "requestId": t.string().optional(),
                "updateMask": t.string().optional(),
                "inputConfig": t.proxy(
                    renames["GoogleCloudRetailV2ProductInputConfigIn"]
                ),
                "notificationPubsubTopic": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCatalogsBranchesProductsAddLocalInventories"
    ] = retail.post(
        "v2/{parent}/products:import",
        t.struct(
            {
                "parent": t.string(),
                "reconciliationMode": t.string().optional(),
                "errorsConfig": t.proxy(
                    renames["GoogleCloudRetailV2ImportErrorsConfigIn"]
                ).optional(),
                "requestId": t.string().optional(),
                "updateMask": t.string().optional(),
                "inputConfig": t.proxy(
                    renames["GoogleCloudRetailV2ProductInputConfigIn"]
                ),
                "notificationPubsubTopic": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCatalogsBranchesProductsRemoveLocalInventories"
    ] = retail.post(
        "v2/{parent}/products:import",
        t.struct(
            {
                "parent": t.string(),
                "reconciliationMode": t.string().optional(),
                "errorsConfig": t.proxy(
                    renames["GoogleCloudRetailV2ImportErrorsConfigIn"]
                ).optional(),
                "requestId": t.string().optional(),
                "updateMask": t.string().optional(),
                "inputConfig": t.proxy(
                    renames["GoogleCloudRetailV2ProductInputConfigIn"]
                ),
                "notificationPubsubTopic": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCatalogsBranchesProductsRemoveFulfillmentPlaces"
    ] = retail.post(
        "v2/{parent}/products:import",
        t.struct(
            {
                "parent": t.string(),
                "reconciliationMode": t.string().optional(),
                "errorsConfig": t.proxy(
                    renames["GoogleCloudRetailV2ImportErrorsConfigIn"]
                ).optional(),
                "requestId": t.string().optional(),
                "updateMask": t.string().optional(),
                "inputConfig": t.proxy(
                    renames["GoogleCloudRetailV2ProductInputConfigIn"]
                ),
                "notificationPubsubTopic": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsBranchesProductsImport"] = retail.post(
        "v2/{parent}/products:import",
        t.struct(
            {
                "parent": t.string(),
                "reconciliationMode": t.string().optional(),
                "errorsConfig": t.proxy(
                    renames["GoogleCloudRetailV2ImportErrorsConfigIn"]
                ).optional(),
                "requestId": t.string().optional(),
                "updateMask": t.string().optional(),
                "inputConfig": t.proxy(
                    renames["GoogleCloudRetailV2ProductInputConfigIn"]
                ),
                "notificationPubsubTopic": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsPlacementsPredict"] = retail.post(
        "v2/{placement}:search",
        t.struct(
            {
                "placement": t.string(),
                "pageToken": t.string().optional(),
                "offset": t.integer().optional(),
                "spellCorrectionSpec": t.proxy(
                    renames["GoogleCloudRetailV2SearchRequestSpellCorrectionSpecIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "pageSize": t.integer().optional(),
                "query": t.string().optional(),
                "searchMode": t.string().optional(),
                "dynamicFacetSpec": t.proxy(
                    renames["GoogleCloudRetailV2SearchRequestDynamicFacetSpecIn"]
                ).optional(),
                "personalizationSpec": t.proxy(
                    renames["GoogleCloudRetailV2SearchRequestPersonalizationSpecIn"]
                ).optional(),
                "visitorId": t.string(),
                "userInfo": t.proxy(
                    renames["GoogleCloudRetailV2UserInfoIn"]
                ).optional(),
                "branch": t.string().optional(),
                "boostSpec": t.proxy(
                    renames["GoogleCloudRetailV2SearchRequestBoostSpecIn"]
                ).optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "variantRollupKeys": t.array(t.string()).optional(),
                "pageCategories": t.array(t.string()).optional(),
                "facetSpecs": t.array(
                    t.proxy(renames["GoogleCloudRetailV2SearchRequestFacetSpecIn"])
                ).optional(),
                "canonicalFilter": t.string().optional(),
                "entity": t.string().optional(),
                "queryExpansionSpec": t.proxy(
                    renames["GoogleCloudRetailV2SearchRequestQueryExpansionSpecIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRetailV2SearchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsPlacementsSearch"] = retail.post(
        "v2/{placement}:search",
        t.struct(
            {
                "placement": t.string(),
                "pageToken": t.string().optional(),
                "offset": t.integer().optional(),
                "spellCorrectionSpec": t.proxy(
                    renames["GoogleCloudRetailV2SearchRequestSpellCorrectionSpecIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "pageSize": t.integer().optional(),
                "query": t.string().optional(),
                "searchMode": t.string().optional(),
                "dynamicFacetSpec": t.proxy(
                    renames["GoogleCloudRetailV2SearchRequestDynamicFacetSpecIn"]
                ).optional(),
                "personalizationSpec": t.proxy(
                    renames["GoogleCloudRetailV2SearchRequestPersonalizationSpecIn"]
                ).optional(),
                "visitorId": t.string(),
                "userInfo": t.proxy(
                    renames["GoogleCloudRetailV2UserInfoIn"]
                ).optional(),
                "branch": t.string().optional(),
                "boostSpec": t.proxy(
                    renames["GoogleCloudRetailV2SearchRequestBoostSpecIn"]
                ).optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "variantRollupKeys": t.array(t.string()).optional(),
                "pageCategories": t.array(t.string()).optional(),
                "facetSpecs": t.array(
                    t.proxy(renames["GoogleCloudRetailV2SearchRequestFacetSpecIn"])
                ).optional(),
                "canonicalFilter": t.string().optional(),
                "entity": t.string().optional(),
                "queryExpansionSpec": t.proxy(
                    renames["GoogleCloudRetailV2SearchRequestQueryExpansionSpecIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRetailV2SearchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsControlsList"] = retail.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRetailV2ControlOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsControlsDelete"] = retail.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRetailV2ControlOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsControlsCreate"] = retail.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRetailV2ControlOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsControlsPatch"] = retail.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRetailV2ControlOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsControlsGet"] = retail.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRetailV2ControlOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsModelsList"] = retail.post(
        "v2/{name}:resume",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRetailV2ModelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsModelsCreate"] = retail.post(
        "v2/{name}:resume",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRetailV2ModelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsModelsPause"] = retail.post(
        "v2/{name}:resume",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRetailV2ModelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsModelsPatch"] = retail.post(
        "v2/{name}:resume",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRetailV2ModelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsModelsTune"] = retail.post(
        "v2/{name}:resume",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRetailV2ModelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsModelsGet"] = retail.post(
        "v2/{name}:resume",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRetailV2ModelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsModelsDelete"] = retail.post(
        "v2/{name}:resume",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRetailV2ModelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsModelsResume"] = retail.post(
        "v2/{name}:resume",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRetailV2ModelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsOperationsList"] = retail.get(
        "v2/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsOperationsGet"] = retail.get(
        "v2/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsCompletionDataImport"] = retail.post(
        "v2/{parent}/completionData:import",
        t.struct(
            {
                "parent": t.string(),
                "notificationPubsubTopic": t.string().optional(),
                "inputConfig": t.proxy(
                    renames["GoogleCloudRetailV2CompletionDataInputConfigIn"]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsUserEventsPurge"] = retail.post(
        "v2/{parent}/userEvents:write",
        t.struct(
            {
                "parent": t.string(),
                "writeAsync": t.boolean().optional(),
                "pageCategories": t.array(t.string()).optional(),
                "cartId": t.string().optional(),
                "attributes": t.struct({"_": t.string().optional()}).optional(),
                "orderBy": t.string().optional(),
                "searchQuery": t.string().optional(),
                "completionDetail": t.proxy(
                    renames["GoogleCloudRetailV2CompletionDetailIn"]
                ).optional(),
                "filter": t.string().optional(),
                "eventTime": t.string().optional(),
                "sessionId": t.string().optional(),
                "visitorId": t.string(),
                "eventType": t.string(),
                "pageViewId": t.string().optional(),
                "attributionToken": t.string().optional(),
                "purchaseTransaction": t.proxy(
                    renames["GoogleCloudRetailV2PurchaseTransactionIn"]
                ).optional(),
                "userInfo": t.proxy(
                    renames["GoogleCloudRetailV2UserInfoIn"]
                ).optional(),
                "uri": t.string().optional(),
                "referrerUri": t.string().optional(),
                "experimentIds": t.array(t.string()).optional(),
                "offset": t.integer().optional(),
                "productDetails": t.array(
                    t.proxy(renames["GoogleCloudRetailV2ProductDetailIn"])
                ).optional(),
                "entity": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRetailV2UserEventOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsUserEventsCollect"] = retail.post(
        "v2/{parent}/userEvents:write",
        t.struct(
            {
                "parent": t.string(),
                "writeAsync": t.boolean().optional(),
                "pageCategories": t.array(t.string()).optional(),
                "cartId": t.string().optional(),
                "attributes": t.struct({"_": t.string().optional()}).optional(),
                "orderBy": t.string().optional(),
                "searchQuery": t.string().optional(),
                "completionDetail": t.proxy(
                    renames["GoogleCloudRetailV2CompletionDetailIn"]
                ).optional(),
                "filter": t.string().optional(),
                "eventTime": t.string().optional(),
                "sessionId": t.string().optional(),
                "visitorId": t.string(),
                "eventType": t.string(),
                "pageViewId": t.string().optional(),
                "attributionToken": t.string().optional(),
                "purchaseTransaction": t.proxy(
                    renames["GoogleCloudRetailV2PurchaseTransactionIn"]
                ).optional(),
                "userInfo": t.proxy(
                    renames["GoogleCloudRetailV2UserInfoIn"]
                ).optional(),
                "uri": t.string().optional(),
                "referrerUri": t.string().optional(),
                "experimentIds": t.array(t.string()).optional(),
                "offset": t.integer().optional(),
                "productDetails": t.array(
                    t.proxy(renames["GoogleCloudRetailV2ProductDetailIn"])
                ).optional(),
                "entity": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRetailV2UserEventOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsUserEventsRejoin"] = retail.post(
        "v2/{parent}/userEvents:write",
        t.struct(
            {
                "parent": t.string(),
                "writeAsync": t.boolean().optional(),
                "pageCategories": t.array(t.string()).optional(),
                "cartId": t.string().optional(),
                "attributes": t.struct({"_": t.string().optional()}).optional(),
                "orderBy": t.string().optional(),
                "searchQuery": t.string().optional(),
                "completionDetail": t.proxy(
                    renames["GoogleCloudRetailV2CompletionDetailIn"]
                ).optional(),
                "filter": t.string().optional(),
                "eventTime": t.string().optional(),
                "sessionId": t.string().optional(),
                "visitorId": t.string(),
                "eventType": t.string(),
                "pageViewId": t.string().optional(),
                "attributionToken": t.string().optional(),
                "purchaseTransaction": t.proxy(
                    renames["GoogleCloudRetailV2PurchaseTransactionIn"]
                ).optional(),
                "userInfo": t.proxy(
                    renames["GoogleCloudRetailV2UserInfoIn"]
                ).optional(),
                "uri": t.string().optional(),
                "referrerUri": t.string().optional(),
                "experimentIds": t.array(t.string()).optional(),
                "offset": t.integer().optional(),
                "productDetails": t.array(
                    t.proxy(renames["GoogleCloudRetailV2ProductDetailIn"])
                ).optional(),
                "entity": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRetailV2UserEventOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsUserEventsImport"] = retail.post(
        "v2/{parent}/userEvents:write",
        t.struct(
            {
                "parent": t.string(),
                "writeAsync": t.boolean().optional(),
                "pageCategories": t.array(t.string()).optional(),
                "cartId": t.string().optional(),
                "attributes": t.struct({"_": t.string().optional()}).optional(),
                "orderBy": t.string().optional(),
                "searchQuery": t.string().optional(),
                "completionDetail": t.proxy(
                    renames["GoogleCloudRetailV2CompletionDetailIn"]
                ).optional(),
                "filter": t.string().optional(),
                "eventTime": t.string().optional(),
                "sessionId": t.string().optional(),
                "visitorId": t.string(),
                "eventType": t.string(),
                "pageViewId": t.string().optional(),
                "attributionToken": t.string().optional(),
                "purchaseTransaction": t.proxy(
                    renames["GoogleCloudRetailV2PurchaseTransactionIn"]
                ).optional(),
                "userInfo": t.proxy(
                    renames["GoogleCloudRetailV2UserInfoIn"]
                ).optional(),
                "uri": t.string().optional(),
                "referrerUri": t.string().optional(),
                "experimentIds": t.array(t.string()).optional(),
                "offset": t.integer().optional(),
                "productDetails": t.array(
                    t.proxy(renames["GoogleCloudRetailV2ProductDetailIn"])
                ).optional(),
                "entity": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRetailV2UserEventOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsUserEventsWrite"] = retail.post(
        "v2/{parent}/userEvents:write",
        t.struct(
            {
                "parent": t.string(),
                "writeAsync": t.boolean().optional(),
                "pageCategories": t.array(t.string()).optional(),
                "cartId": t.string().optional(),
                "attributes": t.struct({"_": t.string().optional()}).optional(),
                "orderBy": t.string().optional(),
                "searchQuery": t.string().optional(),
                "completionDetail": t.proxy(
                    renames["GoogleCloudRetailV2CompletionDetailIn"]
                ).optional(),
                "filter": t.string().optional(),
                "eventTime": t.string().optional(),
                "sessionId": t.string().optional(),
                "visitorId": t.string(),
                "eventType": t.string(),
                "pageViewId": t.string().optional(),
                "attributionToken": t.string().optional(),
                "purchaseTransaction": t.proxy(
                    renames["GoogleCloudRetailV2PurchaseTransactionIn"]
                ).optional(),
                "userInfo": t.proxy(
                    renames["GoogleCloudRetailV2UserInfoIn"]
                ).optional(),
                "uri": t.string().optional(),
                "referrerUri": t.string().optional(),
                "experimentIds": t.array(t.string()).optional(),
                "offset": t.integer().optional(),
                "productDetails": t.array(
                    t.proxy(renames["GoogleCloudRetailV2ProductDetailIn"])
                ).optional(),
                "entity": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRetailV2UserEventOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCatalogsAttributesConfigAddCatalogAttribute"
    ] = retail.post(
        "v2/{attributesConfig}:removeCatalogAttribute",
        t.struct(
            {
                "attributesConfig": t.string(),
                "key": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRetailV2AttributesConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCatalogsAttributesConfigReplaceCatalogAttribute"
    ] = retail.post(
        "v2/{attributesConfig}:removeCatalogAttribute",
        t.struct(
            {
                "attributesConfig": t.string(),
                "key": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRetailV2AttributesConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCatalogsAttributesConfigRemoveCatalogAttribute"
    ] = retail.post(
        "v2/{attributesConfig}:removeCatalogAttribute",
        t.struct(
            {
                "attributesConfig": t.string(),
                "key": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRetailV2AttributesConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsServingConfigsSearch"] = retail.post(
        "v2/{placement}:predict",
        t.struct(
            {
                "placement": t.string(),
                "validateOnly": t.boolean().optional(),
                "filter": t.string().optional(),
                "userEvent": t.proxy(renames["GoogleCloudRetailV2UserEventIn"]),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "pageToken": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRetailV2PredictResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsServingConfigsDelete"] = retail.post(
        "v2/{placement}:predict",
        t.struct(
            {
                "placement": t.string(),
                "validateOnly": t.boolean().optional(),
                "filter": t.string().optional(),
                "userEvent": t.proxy(renames["GoogleCloudRetailV2UserEventIn"]),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "pageToken": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRetailV2PredictResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsServingConfigsRemoveControl"] = retail.post(
        "v2/{placement}:predict",
        t.struct(
            {
                "placement": t.string(),
                "validateOnly": t.boolean().optional(),
                "filter": t.string().optional(),
                "userEvent": t.proxy(renames["GoogleCloudRetailV2UserEventIn"]),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "pageToken": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRetailV2PredictResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsServingConfigsPatch"] = retail.post(
        "v2/{placement}:predict",
        t.struct(
            {
                "placement": t.string(),
                "validateOnly": t.boolean().optional(),
                "filter": t.string().optional(),
                "userEvent": t.proxy(renames["GoogleCloudRetailV2UserEventIn"]),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "pageToken": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRetailV2PredictResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsServingConfigsList"] = retail.post(
        "v2/{placement}:predict",
        t.struct(
            {
                "placement": t.string(),
                "validateOnly": t.boolean().optional(),
                "filter": t.string().optional(),
                "userEvent": t.proxy(renames["GoogleCloudRetailV2UserEventIn"]),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "pageToken": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRetailV2PredictResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsServingConfigsCreate"] = retail.post(
        "v2/{placement}:predict",
        t.struct(
            {
                "placement": t.string(),
                "validateOnly": t.boolean().optional(),
                "filter": t.string().optional(),
                "userEvent": t.proxy(renames["GoogleCloudRetailV2UserEventIn"]),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "pageToken": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRetailV2PredictResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsServingConfigsGet"] = retail.post(
        "v2/{placement}:predict",
        t.struct(
            {
                "placement": t.string(),
                "validateOnly": t.boolean().optional(),
                "filter": t.string().optional(),
                "userEvent": t.proxy(renames["GoogleCloudRetailV2UserEventIn"]),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "pageToken": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRetailV2PredictResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsServingConfigsAddControl"] = retail.post(
        "v2/{placement}:predict",
        t.struct(
            {
                "placement": t.string(),
                "validateOnly": t.boolean().optional(),
                "filter": t.string().optional(),
                "userEvent": t.proxy(renames["GoogleCloudRetailV2UserEventIn"]),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "pageToken": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRetailV2PredictResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsServingConfigsPredict"] = retail.post(
        "v2/{placement}:predict",
        t.struct(
            {
                "placement": t.string(),
                "validateOnly": t.boolean().optional(),
                "filter": t.string().optional(),
                "userEvent": t.proxy(renames["GoogleCloudRetailV2UserEventIn"]),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "pageToken": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRetailV2PredictResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="retail", renames=renames, types=Box(types), functions=Box(functions)
    )
