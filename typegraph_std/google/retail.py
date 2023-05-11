from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_retail() -> Import:
    retail = HTTPRuntime("https://retail.googleapis.com/")

    renames = {
        "ErrorResponse": "_retail_1_ErrorResponse",
        "GoogleCloudRetailV2UserEventInputConfigIn": "_retail_2_GoogleCloudRetailV2UserEventInputConfigIn",
        "GoogleCloudRetailV2UserEventInputConfigOut": "_retail_3_GoogleCloudRetailV2UserEventInputConfigOut",
        "GoogleCloudRetailV2ControlIn": "_retail_4_GoogleCloudRetailV2ControlIn",
        "GoogleCloudRetailV2ControlOut": "_retail_5_GoogleCloudRetailV2ControlOut",
        "GoogleCloudRetailV2ImportMetadataIn": "_retail_6_GoogleCloudRetailV2ImportMetadataIn",
        "GoogleCloudRetailV2ImportMetadataOut": "_retail_7_GoogleCloudRetailV2ImportMetadataOut",
        "GoogleCloudRetailV2RemoveCatalogAttributeRequestIn": "_retail_8_GoogleCloudRetailV2RemoveCatalogAttributeRequestIn",
        "GoogleCloudRetailV2RemoveCatalogAttributeRequestOut": "_retail_9_GoogleCloudRetailV2RemoveCatalogAttributeRequestOut",
        "GoogleCloudRetailV2ResumeModelRequestIn": "_retail_10_GoogleCloudRetailV2ResumeModelRequestIn",
        "GoogleCloudRetailV2ResumeModelRequestOut": "_retail_11_GoogleCloudRetailV2ResumeModelRequestOut",
        "GoogleCloudRetailV2betaTuneModelMetadataIn": "_retail_12_GoogleCloudRetailV2betaTuneModelMetadataIn",
        "GoogleCloudRetailV2betaTuneModelMetadataOut": "_retail_13_GoogleCloudRetailV2betaTuneModelMetadataOut",
        "GoogleCloudRetailV2betaMerchantCenterAccountLinkMerchantCenterFeedFilterIn": "_retail_14_GoogleCloudRetailV2betaMerchantCenterAccountLinkMerchantCenterFeedFilterIn",
        "GoogleCloudRetailV2betaMerchantCenterAccountLinkMerchantCenterFeedFilterOut": "_retail_15_GoogleCloudRetailV2betaMerchantCenterAccountLinkMerchantCenterFeedFilterOut",
        "GoogleCloudRetailV2betaAddLocalInventoriesResponseIn": "_retail_16_GoogleCloudRetailV2betaAddLocalInventoriesResponseIn",
        "GoogleCloudRetailV2betaAddLocalInventoriesResponseOut": "_retail_17_GoogleCloudRetailV2betaAddLocalInventoriesResponseOut",
        "GoogleCloudRetailV2betaAddFulfillmentPlacesResponseIn": "_retail_18_GoogleCloudRetailV2betaAddFulfillmentPlacesResponseIn",
        "GoogleCloudRetailV2betaAddFulfillmentPlacesResponseOut": "_retail_19_GoogleCloudRetailV2betaAddFulfillmentPlacesResponseOut",
        "GoogleCloudRetailV2SetInventoryRequestIn": "_retail_20_GoogleCloudRetailV2SetInventoryRequestIn",
        "GoogleCloudRetailV2SetInventoryRequestOut": "_retail_21_GoogleCloudRetailV2SetInventoryRequestOut",
        "GoogleCloudRetailV2RemoveLocalInventoriesResponseIn": "_retail_22_GoogleCloudRetailV2RemoveLocalInventoriesResponseIn",
        "GoogleCloudRetailV2RemoveLocalInventoriesResponseOut": "_retail_23_GoogleCloudRetailV2RemoveLocalInventoriesResponseOut",
        "GoogleCloudRetailV2TuneModelMetadataIn": "_retail_24_GoogleCloudRetailV2TuneModelMetadataIn",
        "GoogleCloudRetailV2TuneModelMetadataOut": "_retail_25_GoogleCloudRetailV2TuneModelMetadataOut",
        "GoogleCloudRetailV2betaSetInventoryMetadataIn": "_retail_26_GoogleCloudRetailV2betaSetInventoryMetadataIn",
        "GoogleCloudRetailV2betaSetInventoryMetadataOut": "_retail_27_GoogleCloudRetailV2betaSetInventoryMetadataOut",
        "GoogleCloudRetailV2alphaMerchantCenterAccountLinkIn": "_retail_28_GoogleCloudRetailV2alphaMerchantCenterAccountLinkIn",
        "GoogleCloudRetailV2alphaMerchantCenterAccountLinkOut": "_retail_29_GoogleCloudRetailV2alphaMerchantCenterAccountLinkOut",
        "GoogleCloudRetailV2RuleReplacementActionIn": "_retail_30_GoogleCloudRetailV2RuleReplacementActionIn",
        "GoogleCloudRetailV2RuleReplacementActionOut": "_retail_31_GoogleCloudRetailV2RuleReplacementActionOut",
        "GoogleCloudRetailV2CompletionConfigIn": "_retail_32_GoogleCloudRetailV2CompletionConfigIn",
        "GoogleCloudRetailV2CompletionConfigOut": "_retail_33_GoogleCloudRetailV2CompletionConfigOut",
        "GoogleCloudRetailV2betaModelServingConfigListIn": "_retail_34_GoogleCloudRetailV2betaModelServingConfigListIn",
        "GoogleCloudRetailV2betaModelServingConfigListOut": "_retail_35_GoogleCloudRetailV2betaModelServingConfigListOut",
        "GoogleCloudRetailV2ListModelsResponseIn": "_retail_36_GoogleCloudRetailV2ListModelsResponseIn",
        "GoogleCloudRetailV2ListModelsResponseOut": "_retail_37_GoogleCloudRetailV2ListModelsResponseOut",
        "GoogleCloudRetailV2alphaRemoveFulfillmentPlacesResponseIn": "_retail_38_GoogleCloudRetailV2alphaRemoveFulfillmentPlacesResponseIn",
        "GoogleCloudRetailV2alphaRemoveFulfillmentPlacesResponseOut": "_retail_39_GoogleCloudRetailV2alphaRemoveFulfillmentPlacesResponseOut",
        "GoogleCloudRetailV2CatalogIn": "_retail_40_GoogleCloudRetailV2CatalogIn",
        "GoogleCloudRetailV2CatalogOut": "_retail_41_GoogleCloudRetailV2CatalogOut",
        "GoogleCloudRetailV2SearchResponseFacetIn": "_retail_42_GoogleCloudRetailV2SearchResponseFacetIn",
        "GoogleCloudRetailV2SearchResponseFacetOut": "_retail_43_GoogleCloudRetailV2SearchResponseFacetOut",
        "GoogleCloudRetailV2ReplaceCatalogAttributeRequestIn": "_retail_44_GoogleCloudRetailV2ReplaceCatalogAttributeRequestIn",
        "GoogleCloudRetailV2ReplaceCatalogAttributeRequestOut": "_retail_45_GoogleCloudRetailV2ReplaceCatalogAttributeRequestOut",
        "GoogleCloudRetailV2RemoveLocalInventoriesMetadataIn": "_retail_46_GoogleCloudRetailV2RemoveLocalInventoriesMetadataIn",
        "GoogleCloudRetailV2RemoveLocalInventoriesMetadataOut": "_retail_47_GoogleCloudRetailV2RemoveLocalInventoriesMetadataOut",
        "GoogleCloudRetailV2betaExportErrorsConfigIn": "_retail_48_GoogleCloudRetailV2betaExportErrorsConfigIn",
        "GoogleCloudRetailV2betaExportErrorsConfigOut": "_retail_49_GoogleCloudRetailV2betaExportErrorsConfigOut",
        "GoogleCloudRetailV2alphaAddFulfillmentPlacesMetadataIn": "_retail_50_GoogleCloudRetailV2alphaAddFulfillmentPlacesMetadataIn",
        "GoogleCloudRetailV2alphaAddFulfillmentPlacesMetadataOut": "_retail_51_GoogleCloudRetailV2alphaAddFulfillmentPlacesMetadataOut",
        "GoogleCloudRetailV2AudienceIn": "_retail_52_GoogleCloudRetailV2AudienceIn",
        "GoogleCloudRetailV2AudienceOut": "_retail_53_GoogleCloudRetailV2AudienceOut",
        "GoogleCloudRetailV2betaSetInventoryResponseIn": "_retail_54_GoogleCloudRetailV2betaSetInventoryResponseIn",
        "GoogleCloudRetailV2betaSetInventoryResponseOut": "_retail_55_GoogleCloudRetailV2betaSetInventoryResponseOut",
        "GoogleCloudRetailV2alphaSetInventoryResponseIn": "_retail_56_GoogleCloudRetailV2alphaSetInventoryResponseIn",
        "GoogleCloudRetailV2alphaSetInventoryResponseOut": "_retail_57_GoogleCloudRetailV2alphaSetInventoryResponseOut",
        "GoogleCloudRetailV2CatalogAttributeIn": "_retail_58_GoogleCloudRetailV2CatalogAttributeIn",
        "GoogleCloudRetailV2CatalogAttributeOut": "_retail_59_GoogleCloudRetailV2CatalogAttributeOut",
        "GoogleCloudRetailV2RemoveLocalInventoriesRequestIn": "_retail_60_GoogleCloudRetailV2RemoveLocalInventoriesRequestIn",
        "GoogleCloudRetailV2RemoveLocalInventoriesRequestOut": "_retail_61_GoogleCloudRetailV2RemoveLocalInventoriesRequestOut",
        "GoogleCloudRetailV2TuneModelRequestIn": "_retail_62_GoogleCloudRetailV2TuneModelRequestIn",
        "GoogleCloudRetailV2TuneModelRequestOut": "_retail_63_GoogleCloudRetailV2TuneModelRequestOut",
        "GoogleCloudRetailV2ServingConfigIn": "_retail_64_GoogleCloudRetailV2ServingConfigIn",
        "GoogleCloudRetailV2ServingConfigOut": "_retail_65_GoogleCloudRetailV2ServingConfigOut",
        "GoogleCloudRetailV2alphaImportCompletionDataResponseIn": "_retail_66_GoogleCloudRetailV2alphaImportCompletionDataResponseIn",
        "GoogleCloudRetailV2alphaImportCompletionDataResponseOut": "_retail_67_GoogleCloudRetailV2alphaImportCompletionDataResponseOut",
        "GoogleCloudRetailV2PredictResponseIn": "_retail_68_GoogleCloudRetailV2PredictResponseIn",
        "GoogleCloudRetailV2PredictResponseOut": "_retail_69_GoogleCloudRetailV2PredictResponseOut",
        "GoogleCloudRetailV2SetDefaultBranchRequestIn": "_retail_70_GoogleCloudRetailV2SetDefaultBranchRequestIn",
        "GoogleCloudRetailV2SetDefaultBranchRequestOut": "_retail_71_GoogleCloudRetailV2SetDefaultBranchRequestOut",
        "GoogleCloudRetailV2ImportErrorsConfigIn": "_retail_72_GoogleCloudRetailV2ImportErrorsConfigIn",
        "GoogleCloudRetailV2ImportErrorsConfigOut": "_retail_73_GoogleCloudRetailV2ImportErrorsConfigOut",
        "GoogleCloudRetailV2ProductInlineSourceIn": "_retail_74_GoogleCloudRetailV2ProductInlineSourceIn",
        "GoogleCloudRetailV2ProductInlineSourceOut": "_retail_75_GoogleCloudRetailV2ProductInlineSourceOut",
        "GoogleCloudRetailV2alphaAddLocalInventoriesResponseIn": "_retail_76_GoogleCloudRetailV2alphaAddLocalInventoriesResponseIn",
        "GoogleCloudRetailV2alphaAddLocalInventoriesResponseOut": "_retail_77_GoogleCloudRetailV2alphaAddLocalInventoriesResponseOut",
        "GoogleCloudRetailV2ExperimentInfoServingConfigExperimentIn": "_retail_78_GoogleCloudRetailV2ExperimentInfoServingConfigExperimentIn",
        "GoogleCloudRetailV2ExperimentInfoServingConfigExperimentOut": "_retail_79_GoogleCloudRetailV2ExperimentInfoServingConfigExperimentOut",
        "GoogleCloudRetailV2betaModelModelFeaturesConfigIn": "_retail_80_GoogleCloudRetailV2betaModelModelFeaturesConfigIn",
        "GoogleCloudRetailV2betaModelModelFeaturesConfigOut": "_retail_81_GoogleCloudRetailV2betaModelModelFeaturesConfigOut",
        "GoogleCloudRetailV2PredictResponsePredictionResultIn": "_retail_82_GoogleCloudRetailV2PredictResponsePredictionResultIn",
        "GoogleCloudRetailV2PredictResponsePredictionResultOut": "_retail_83_GoogleCloudRetailV2PredictResponsePredictionResultOut",
        "GoogleCloudRetailV2betaPurgeUserEventsResponseIn": "_retail_84_GoogleCloudRetailV2betaPurgeUserEventsResponseIn",
        "GoogleCloudRetailV2betaPurgeUserEventsResponseOut": "_retail_85_GoogleCloudRetailV2betaPurgeUserEventsResponseOut",
        "GoogleCloudRetailV2SetInventoryResponseIn": "_retail_86_GoogleCloudRetailV2SetInventoryResponseIn",
        "GoogleCloudRetailV2SetInventoryResponseOut": "_retail_87_GoogleCloudRetailV2SetInventoryResponseOut",
        "GoogleCloudRetailV2alphaAddFulfillmentPlacesResponseIn": "_retail_88_GoogleCloudRetailV2alphaAddFulfillmentPlacesResponseIn",
        "GoogleCloudRetailV2alphaAddFulfillmentPlacesResponseOut": "_retail_89_GoogleCloudRetailV2alphaAddFulfillmentPlacesResponseOut",
        "GoogleCloudRetailV2betaImportErrorsConfigIn": "_retail_90_GoogleCloudRetailV2betaImportErrorsConfigIn",
        "GoogleCloudRetailV2betaImportErrorsConfigOut": "_retail_91_GoogleCloudRetailV2betaImportErrorsConfigOut",
        "GoogleCloudRetailV2alphaImportErrorsConfigIn": "_retail_92_GoogleCloudRetailV2alphaImportErrorsConfigIn",
        "GoogleCloudRetailV2alphaImportErrorsConfigOut": "_retail_93_GoogleCloudRetailV2alphaImportErrorsConfigOut",
        "GoogleCloudRetailV2CompleteQueryResponseIn": "_retail_94_GoogleCloudRetailV2CompleteQueryResponseIn",
        "GoogleCloudRetailV2CompleteQueryResponseOut": "_retail_95_GoogleCloudRetailV2CompleteQueryResponseOut",
        "GoogleCloudRetailV2AddCatalogAttributeRequestIn": "_retail_96_GoogleCloudRetailV2AddCatalogAttributeRequestIn",
        "GoogleCloudRetailV2AddCatalogAttributeRequestOut": "_retail_97_GoogleCloudRetailV2AddCatalogAttributeRequestOut",
        "GoogleCloudRetailV2ModelModelFeaturesConfigIn": "_retail_98_GoogleCloudRetailV2ModelModelFeaturesConfigIn",
        "GoogleCloudRetailV2ModelModelFeaturesConfigOut": "_retail_99_GoogleCloudRetailV2ModelModelFeaturesConfigOut",
        "GoogleCloudRetailV2PauseModelRequestIn": "_retail_100_GoogleCloudRetailV2PauseModelRequestIn",
        "GoogleCloudRetailV2PauseModelRequestOut": "_retail_101_GoogleCloudRetailV2PauseModelRequestOut",
        "GoogleCloudRetailV2RuleOnewaySynonymsActionIn": "_retail_102_GoogleCloudRetailV2RuleOnewaySynonymsActionIn",
        "GoogleCloudRetailV2RuleOnewaySynonymsActionOut": "_retail_103_GoogleCloudRetailV2RuleOnewaySynonymsActionOut",
        "GoogleCloudRetailV2PurgeUserEventsResponseIn": "_retail_104_GoogleCloudRetailV2PurgeUserEventsResponseIn",
        "GoogleCloudRetailV2PurgeUserEventsResponseOut": "_retail_105_GoogleCloudRetailV2PurgeUserEventsResponseOut",
        "GoogleCloudRetailV2alphaUserEventImportSummaryIn": "_retail_106_GoogleCloudRetailV2alphaUserEventImportSummaryIn",
        "GoogleCloudRetailV2alphaUserEventImportSummaryOut": "_retail_107_GoogleCloudRetailV2alphaUserEventImportSummaryOut",
        "GoogleCloudRetailV2alphaPurgeMetadataIn": "_retail_108_GoogleCloudRetailV2alphaPurgeMetadataIn",
        "GoogleCloudRetailV2alphaPurgeMetadataOut": "_retail_109_GoogleCloudRetailV2alphaPurgeMetadataOut",
        "GoogleCloudRetailV2RemoveControlRequestIn": "_retail_110_GoogleCloudRetailV2RemoveControlRequestIn",
        "GoogleCloudRetailV2RemoveControlRequestOut": "_retail_111_GoogleCloudRetailV2RemoveControlRequestOut",
        "GoogleCloudRetailV2betaAddFulfillmentPlacesMetadataIn": "_retail_112_GoogleCloudRetailV2betaAddFulfillmentPlacesMetadataIn",
        "GoogleCloudRetailV2betaAddFulfillmentPlacesMetadataOut": "_retail_113_GoogleCloudRetailV2betaAddFulfillmentPlacesMetadataOut",
        "GoogleCloudRetailV2GetDefaultBranchResponseIn": "_retail_114_GoogleCloudRetailV2GetDefaultBranchResponseIn",
        "GoogleCloudRetailV2GetDefaultBranchResponseOut": "_retail_115_GoogleCloudRetailV2GetDefaultBranchResponseOut",
        "GoogleCloudRetailV2ImportProductsResponseIn": "_retail_116_GoogleCloudRetailV2ImportProductsResponseIn",
        "GoogleCloudRetailV2ImportProductsResponseOut": "_retail_117_GoogleCloudRetailV2ImportProductsResponseOut",
        "GoogleCloudRetailLoggingSourceLocationIn": "_retail_118_GoogleCloudRetailLoggingSourceLocationIn",
        "GoogleCloudRetailLoggingSourceLocationOut": "_retail_119_GoogleCloudRetailLoggingSourceLocationOut",
        "GoogleCloudRetailV2alphaModelPageOptimizationConfigPanelIn": "_retail_120_GoogleCloudRetailV2alphaModelPageOptimizationConfigPanelIn",
        "GoogleCloudRetailV2alphaModelPageOptimizationConfigPanelOut": "_retail_121_GoogleCloudRetailV2alphaModelPageOptimizationConfigPanelOut",
        "GoogleCloudRetailV2RejoinUserEventsResponseIn": "_retail_122_GoogleCloudRetailV2RejoinUserEventsResponseIn",
        "GoogleCloudRetailV2RejoinUserEventsResponseOut": "_retail_123_GoogleCloudRetailV2RejoinUserEventsResponseOut",
        "GoogleCloudRetailV2ListControlsResponseIn": "_retail_124_GoogleCloudRetailV2ListControlsResponseIn",
        "GoogleCloudRetailV2ListControlsResponseOut": "_retail_125_GoogleCloudRetailV2ListControlsResponseOut",
        "GoogleCloudRetailV2ConditionQueryTermIn": "_retail_126_GoogleCloudRetailV2ConditionQueryTermIn",
        "GoogleCloudRetailV2ConditionQueryTermOut": "_retail_127_GoogleCloudRetailV2ConditionQueryTermOut",
        "GoogleCloudRetailV2ImportCompletionDataRequestIn": "_retail_128_GoogleCloudRetailV2ImportCompletionDataRequestIn",
        "GoogleCloudRetailV2ImportCompletionDataRequestOut": "_retail_129_GoogleCloudRetailV2ImportCompletionDataRequestOut",
        "GoogleCloudRetailV2ModelFrequentlyBoughtTogetherFeaturesConfigIn": "_retail_130_GoogleCloudRetailV2ModelFrequentlyBoughtTogetherFeaturesConfigIn",
        "GoogleCloudRetailV2ModelFrequentlyBoughtTogetherFeaturesConfigOut": "_retail_131_GoogleCloudRetailV2ModelFrequentlyBoughtTogetherFeaturesConfigOut",
        "GoogleCloudRetailV2SearchRequestBoostSpecIn": "_retail_132_GoogleCloudRetailV2SearchRequestBoostSpecIn",
        "GoogleCloudRetailV2SearchRequestBoostSpecOut": "_retail_133_GoogleCloudRetailV2SearchRequestBoostSpecOut",
        "GoogleCloudRetailV2ConditionIn": "_retail_134_GoogleCloudRetailV2ConditionIn",
        "GoogleCloudRetailV2ConditionOut": "_retail_135_GoogleCloudRetailV2ConditionOut",
        "GoogleCloudRetailV2SearchRequestQueryExpansionSpecIn": "_retail_136_GoogleCloudRetailV2SearchRequestQueryExpansionSpecIn",
        "GoogleCloudRetailV2SearchRequestQueryExpansionSpecOut": "_retail_137_GoogleCloudRetailV2SearchRequestQueryExpansionSpecOut",
        "GoogleCloudRetailV2alphaTuneModelMetadataIn": "_retail_138_GoogleCloudRetailV2alphaTuneModelMetadataIn",
        "GoogleCloudRetailV2alphaTuneModelMetadataOut": "_retail_139_GoogleCloudRetailV2alphaTuneModelMetadataOut",
        "GoogleCloudRetailV2alphaExportUserEventsResponseIn": "_retail_140_GoogleCloudRetailV2alphaExportUserEventsResponseIn",
        "GoogleCloudRetailV2alphaExportUserEventsResponseOut": "_retail_141_GoogleCloudRetailV2alphaExportUserEventsResponseOut",
        "GoogleCloudRetailV2betaGcsOutputResultIn": "_retail_142_GoogleCloudRetailV2betaGcsOutputResultIn",
        "GoogleCloudRetailV2betaGcsOutputResultOut": "_retail_143_GoogleCloudRetailV2betaGcsOutputResultOut",
        "GoogleCloudRetailV2SetInventoryMetadataIn": "_retail_144_GoogleCloudRetailV2SetInventoryMetadataIn",
        "GoogleCloudRetailV2SetInventoryMetadataOut": "_retail_145_GoogleCloudRetailV2SetInventoryMetadataOut",
        "GoogleCloudRetailV2betaBigQueryOutputResultIn": "_retail_146_GoogleCloudRetailV2betaBigQueryOutputResultIn",
        "GoogleCloudRetailV2betaBigQueryOutputResultOut": "_retail_147_GoogleCloudRetailV2betaBigQueryOutputResultOut",
        "GoogleCloudRetailV2AddLocalInventoriesResponseIn": "_retail_148_GoogleCloudRetailV2AddLocalInventoriesResponseIn",
        "GoogleCloudRetailV2AddLocalInventoriesResponseOut": "_retail_149_GoogleCloudRetailV2AddLocalInventoriesResponseOut",
        "GoogleCloudRetailV2betaRemoveFulfillmentPlacesResponseIn": "_retail_150_GoogleCloudRetailV2betaRemoveFulfillmentPlacesResponseIn",
        "GoogleCloudRetailV2betaRemoveFulfillmentPlacesResponseOut": "_retail_151_GoogleCloudRetailV2betaRemoveFulfillmentPlacesResponseOut",
        "GoogleCloudRetailV2alphaImportUserEventsResponseIn": "_retail_152_GoogleCloudRetailV2alphaImportUserEventsResponseIn",
        "GoogleCloudRetailV2alphaImportUserEventsResponseOut": "_retail_153_GoogleCloudRetailV2alphaImportUserEventsResponseOut",
        "GoogleCloudRetailV2ModelServingConfigListIn": "_retail_154_GoogleCloudRetailV2ModelServingConfigListIn",
        "GoogleCloudRetailV2ModelServingConfigListOut": "_retail_155_GoogleCloudRetailV2ModelServingConfigListOut",
        "GoogleCloudRetailV2SearchRequestFacetSpecFacetKeyIn": "_retail_156_GoogleCloudRetailV2SearchRequestFacetSpecFacetKeyIn",
        "GoogleCloudRetailV2SearchRequestFacetSpecFacetKeyOut": "_retail_157_GoogleCloudRetailV2SearchRequestFacetSpecFacetKeyOut",
        "GoogleCloudRetailV2CompletionDetailIn": "_retail_158_GoogleCloudRetailV2CompletionDetailIn",
        "GoogleCloudRetailV2CompletionDetailOut": "_retail_159_GoogleCloudRetailV2CompletionDetailOut",
        "GoogleCloudRetailV2AddFulfillmentPlacesMetadataIn": "_retail_160_GoogleCloudRetailV2AddFulfillmentPlacesMetadataIn",
        "GoogleCloudRetailV2AddFulfillmentPlacesMetadataOut": "_retail_161_GoogleCloudRetailV2AddFulfillmentPlacesMetadataOut",
        "GoogleCloudRetailLoggingImportErrorContextIn": "_retail_162_GoogleCloudRetailLoggingImportErrorContextIn",
        "GoogleCloudRetailLoggingImportErrorContextOut": "_retail_163_GoogleCloudRetailLoggingImportErrorContextOut",
        "GoogleCloudRetailV2alphaRejoinUserEventsMetadataIn": "_retail_164_GoogleCloudRetailV2alphaRejoinUserEventsMetadataIn",
        "GoogleCloudRetailV2alphaRejoinUserEventsMetadataOut": "_retail_165_GoogleCloudRetailV2alphaRejoinUserEventsMetadataOut",
        "GoogleCloudRetailV2CompletionDataInputConfigIn": "_retail_166_GoogleCloudRetailV2CompletionDataInputConfigIn",
        "GoogleCloudRetailV2CompletionDataInputConfigOut": "_retail_167_GoogleCloudRetailV2CompletionDataInputConfigOut",
        "GoogleCloudRetailV2alphaPurgeProductsResponseIn": "_retail_168_GoogleCloudRetailV2alphaPurgeProductsResponseIn",
        "GoogleCloudRetailV2alphaPurgeProductsResponseOut": "_retail_169_GoogleCloudRetailV2alphaPurgeProductsResponseOut",
        "GoogleCloudRetailV2alphaPurgeUserEventsResponseIn": "_retail_170_GoogleCloudRetailV2alphaPurgeUserEventsResponseIn",
        "GoogleCloudRetailV2alphaPurgeUserEventsResponseOut": "_retail_171_GoogleCloudRetailV2alphaPurgeUserEventsResponseOut",
        "GoogleCloudRetailV2LocalInventoryIn": "_retail_172_GoogleCloudRetailV2LocalInventoryIn",
        "GoogleCloudRetailV2LocalInventoryOut": "_retail_173_GoogleCloudRetailV2LocalInventoryOut",
        "GoogleCloudRetailV2alphaTransformedUserEventsMetadataIn": "_retail_174_GoogleCloudRetailV2alphaTransformedUserEventsMetadataIn",
        "GoogleCloudRetailV2alphaTransformedUserEventsMetadataOut": "_retail_175_GoogleCloudRetailV2alphaTransformedUserEventsMetadataOut",
        "GoogleCloudRetailV2betaTuneModelResponseIn": "_retail_176_GoogleCloudRetailV2betaTuneModelResponseIn",
        "GoogleCloudRetailV2betaTuneModelResponseOut": "_retail_177_GoogleCloudRetailV2betaTuneModelResponseOut",
        "GoogleCloudRetailV2ColorInfoIn": "_retail_178_GoogleCloudRetailV2ColorInfoIn",
        "GoogleCloudRetailV2ColorInfoOut": "_retail_179_GoogleCloudRetailV2ColorInfoOut",
        "GoogleCloudRetailV2RemoveFulfillmentPlacesResponseIn": "_retail_180_GoogleCloudRetailV2RemoveFulfillmentPlacesResponseIn",
        "GoogleCloudRetailV2RemoveFulfillmentPlacesResponseOut": "_retail_181_GoogleCloudRetailV2RemoveFulfillmentPlacesResponseOut",
        "GoogleCloudRetailV2RemoveFulfillmentPlacesRequestIn": "_retail_182_GoogleCloudRetailV2RemoveFulfillmentPlacesRequestIn",
        "GoogleCloudRetailV2RemoveFulfillmentPlacesRequestOut": "_retail_183_GoogleCloudRetailV2RemoveFulfillmentPlacesRequestOut",
        "GoogleCloudRetailV2RejoinUserEventsMetadataIn": "_retail_184_GoogleCloudRetailV2RejoinUserEventsMetadataIn",
        "GoogleCloudRetailV2RejoinUserEventsMetadataOut": "_retail_185_GoogleCloudRetailV2RejoinUserEventsMetadataOut",
        "GoogleCloudRetailV2UserInfoIn": "_retail_186_GoogleCloudRetailV2UserInfoIn",
        "GoogleCloudRetailV2UserInfoOut": "_retail_187_GoogleCloudRetailV2UserInfoOut",
        "GoogleCloudRetailV2ImageIn": "_retail_188_GoogleCloudRetailV2ImageIn",
        "GoogleCloudRetailV2ImageOut": "_retail_189_GoogleCloudRetailV2ImageOut",
        "GoogleCloudRetailV2betaRemoveLocalInventoriesMetadataIn": "_retail_190_GoogleCloudRetailV2betaRemoveLocalInventoriesMetadataIn",
        "GoogleCloudRetailV2betaRemoveLocalInventoriesMetadataOut": "_retail_191_GoogleCloudRetailV2betaRemoveLocalInventoriesMetadataOut",
        "GoogleCloudRetailV2RuleBoostActionIn": "_retail_192_GoogleCloudRetailV2RuleBoostActionIn",
        "GoogleCloudRetailV2RuleBoostActionOut": "_retail_193_GoogleCloudRetailV2RuleBoostActionOut",
        "GoogleCloudRetailV2SearchResponseIn": "_retail_194_GoogleCloudRetailV2SearchResponseIn",
        "GoogleCloudRetailV2SearchResponseOut": "_retail_195_GoogleCloudRetailV2SearchResponseOut",
        "GoogleCloudRetailV2RejoinUserEventsRequestIn": "_retail_196_GoogleCloudRetailV2RejoinUserEventsRequestIn",
        "GoogleCloudRetailV2RejoinUserEventsRequestOut": "_retail_197_GoogleCloudRetailV2RejoinUserEventsRequestOut",
        "GoogleCloudRetailV2alphaMerchantCenterAccountLinkMerchantCenterFeedFilterIn": "_retail_198_GoogleCloudRetailV2alphaMerchantCenterAccountLinkMerchantCenterFeedFilterIn",
        "GoogleCloudRetailV2alphaMerchantCenterAccountLinkMerchantCenterFeedFilterOut": "_retail_199_GoogleCloudRetailV2alphaMerchantCenterAccountLinkMerchantCenterFeedFilterOut",
        "GoogleCloudRetailV2betaModelFrequentlyBoughtTogetherFeaturesConfigIn": "_retail_200_GoogleCloudRetailV2betaModelFrequentlyBoughtTogetherFeaturesConfigIn",
        "GoogleCloudRetailV2betaModelFrequentlyBoughtTogetherFeaturesConfigOut": "_retail_201_GoogleCloudRetailV2betaModelFrequentlyBoughtTogetherFeaturesConfigOut",
        "GoogleCloudRetailV2SearchResponseSearchResultIn": "_retail_202_GoogleCloudRetailV2SearchResponseSearchResultIn",
        "GoogleCloudRetailV2SearchResponseSearchResultOut": "_retail_203_GoogleCloudRetailV2SearchResponseSearchResultOut",
        "GoogleCloudRetailV2ProductIn": "_retail_204_GoogleCloudRetailV2ProductIn",
        "GoogleCloudRetailV2ProductOut": "_retail_205_GoogleCloudRetailV2ProductOut",
        "GoogleCloudRetailLoggingErrorContextIn": "_retail_206_GoogleCloudRetailLoggingErrorContextIn",
        "GoogleCloudRetailLoggingErrorContextOut": "_retail_207_GoogleCloudRetailLoggingErrorContextOut",
        "GoogleCloudRetailV2SearchRequestIn": "_retail_208_GoogleCloudRetailV2SearchRequestIn",
        "GoogleCloudRetailV2SearchRequestOut": "_retail_209_GoogleCloudRetailV2SearchRequestOut",
        "GoogleCloudRetailV2UserEventInlineSourceIn": "_retail_210_GoogleCloudRetailV2UserEventInlineSourceIn",
        "GoogleCloudRetailV2UserEventInlineSourceOut": "_retail_211_GoogleCloudRetailV2UserEventInlineSourceOut",
        "GoogleCloudRetailV2AttributesConfigIn": "_retail_212_GoogleCloudRetailV2AttributesConfigIn",
        "GoogleCloudRetailV2AttributesConfigOut": "_retail_213_GoogleCloudRetailV2AttributesConfigOut",
        "GoogleCloudRetailV2CompleteQueryResponseRecentSearchResultIn": "_retail_214_GoogleCloudRetailV2CompleteQueryResponseRecentSearchResultIn",
        "GoogleCloudRetailV2CompleteQueryResponseRecentSearchResultOut": "_retail_215_GoogleCloudRetailV2CompleteQueryResponseRecentSearchResultOut",
        "GoogleCloudRetailV2alphaExportProductsResponseIn": "_retail_216_GoogleCloudRetailV2alphaExportProductsResponseIn",
        "GoogleCloudRetailV2alphaExportProductsResponseOut": "_retail_217_GoogleCloudRetailV2alphaExportProductsResponseOut",
        "GoogleCloudRetailV2AddFulfillmentPlacesResponseIn": "_retail_218_GoogleCloudRetailV2AddFulfillmentPlacesResponseIn",
        "GoogleCloudRetailV2AddFulfillmentPlacesResponseOut": "_retail_219_GoogleCloudRetailV2AddFulfillmentPlacesResponseOut",
        "GoogleCloudRetailV2AddLocalInventoriesRequestIn": "_retail_220_GoogleCloudRetailV2AddLocalInventoriesRequestIn",
        "GoogleCloudRetailV2AddLocalInventoriesRequestOut": "_retail_221_GoogleCloudRetailV2AddLocalInventoriesRequestOut",
        "GoogleLongrunningListOperationsResponseIn": "_retail_222_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_retail_223_GoogleLongrunningListOperationsResponseOut",
        "GoogleCloudRetailV2TuneModelResponseIn": "_retail_224_GoogleCloudRetailV2TuneModelResponseIn",
        "GoogleCloudRetailV2TuneModelResponseOut": "_retail_225_GoogleCloudRetailV2TuneModelResponseOut",
        "GoogleCloudRetailV2PredictRequestIn": "_retail_226_GoogleCloudRetailV2PredictRequestIn",
        "GoogleCloudRetailV2PredictRequestOut": "_retail_227_GoogleCloudRetailV2PredictRequestOut",
        "GoogleCloudRetailV2alphaPurgeProductsMetadataIn": "_retail_228_GoogleCloudRetailV2alphaPurgeProductsMetadataIn",
        "GoogleCloudRetailV2alphaPurgeProductsMetadataOut": "_retail_229_GoogleCloudRetailV2alphaPurgeProductsMetadataOut",
        "GoogleCloudRetailV2betaModelIn": "_retail_230_GoogleCloudRetailV2betaModelIn",
        "GoogleCloudRetailV2betaModelOut": "_retail_231_GoogleCloudRetailV2betaModelOut",
        "GoogleCloudRetailV2CreateModelMetadataIn": "_retail_232_GoogleCloudRetailV2CreateModelMetadataIn",
        "GoogleCloudRetailV2CreateModelMetadataOut": "_retail_233_GoogleCloudRetailV2CreateModelMetadataOut",
        "GoogleCloudRetailV2alphaRemoveLocalInventoriesResponseIn": "_retail_234_GoogleCloudRetailV2alphaRemoveLocalInventoriesResponseIn",
        "GoogleCloudRetailV2alphaRemoveLocalInventoriesResponseOut": "_retail_235_GoogleCloudRetailV2alphaRemoveLocalInventoriesResponseOut",
        "GoogleCloudRetailV2alphaRejoinUserEventsResponseIn": "_retail_236_GoogleCloudRetailV2alphaRejoinUserEventsResponseIn",
        "GoogleCloudRetailV2alphaRejoinUserEventsResponseOut": "_retail_237_GoogleCloudRetailV2alphaRejoinUserEventsResponseOut",
        "GoogleCloudRetailV2ConditionTimeRangeIn": "_retail_238_GoogleCloudRetailV2ConditionTimeRangeIn",
        "GoogleCloudRetailV2ConditionTimeRangeOut": "_retail_239_GoogleCloudRetailV2ConditionTimeRangeOut",
        "GoogleCloudRetailV2ImportUserEventsRequestIn": "_retail_240_GoogleCloudRetailV2ImportUserEventsRequestIn",
        "GoogleCloudRetailV2ImportUserEventsRequestOut": "_retail_241_GoogleCloudRetailV2ImportUserEventsRequestOut",
        "GoogleCloudRetailV2ListCatalogsResponseIn": "_retail_242_GoogleCloudRetailV2ListCatalogsResponseIn",
        "GoogleCloudRetailV2ListCatalogsResponseOut": "_retail_243_GoogleCloudRetailV2ListCatalogsResponseOut",
        "GoogleCloudRetailV2alphaGcsOutputResultIn": "_retail_244_GoogleCloudRetailV2alphaGcsOutputResultIn",
        "GoogleCloudRetailV2alphaGcsOutputResultOut": "_retail_245_GoogleCloudRetailV2alphaGcsOutputResultOut",
        "GoogleLongrunningOperationIn": "_retail_246_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_retail_247_GoogleLongrunningOperationOut",
        "GoogleCloudRetailV2betaCreateMerchantCenterAccountLinkMetadataIn": "_retail_248_GoogleCloudRetailV2betaCreateMerchantCenterAccountLinkMetadataIn",
        "GoogleCloudRetailV2betaCreateMerchantCenterAccountLinkMetadataOut": "_retail_249_GoogleCloudRetailV2betaCreateMerchantCenterAccountLinkMetadataOut",
        "GoogleCloudRetailV2ModelIn": "_retail_250_GoogleCloudRetailV2ModelIn",
        "GoogleCloudRetailV2ModelOut": "_retail_251_GoogleCloudRetailV2ModelOut",
        "GoogleCloudRetailV2ListProductsResponseIn": "_retail_252_GoogleCloudRetailV2ListProductsResponseIn",
        "GoogleCloudRetailV2ListProductsResponseOut": "_retail_253_GoogleCloudRetailV2ListProductsResponseOut",
        "GoogleCloudRetailV2alphaImportProductsResponseIn": "_retail_254_GoogleCloudRetailV2alphaImportProductsResponseIn",
        "GoogleCloudRetailV2alphaImportProductsResponseOut": "_retail_255_GoogleCloudRetailV2alphaImportProductsResponseOut",
        "GoogleCloudRetailV2betaImportMetadataIn": "_retail_256_GoogleCloudRetailV2betaImportMetadataIn",
        "GoogleCloudRetailV2betaImportMetadataOut": "_retail_257_GoogleCloudRetailV2betaImportMetadataOut",
        "GoogleCloudRetailV2AddControlRequestIn": "_retail_258_GoogleCloudRetailV2AddControlRequestIn",
        "GoogleCloudRetailV2AddControlRequestOut": "_retail_259_GoogleCloudRetailV2AddControlRequestOut",
        "GoogleCloudRetailV2AddLocalInventoriesMetadataIn": "_retail_260_GoogleCloudRetailV2AddLocalInventoriesMetadataIn",
        "GoogleCloudRetailV2AddLocalInventoriesMetadataOut": "_retail_261_GoogleCloudRetailV2AddLocalInventoriesMetadataOut",
        "GoogleCloudRetailV2ProductInputConfigIn": "_retail_262_GoogleCloudRetailV2ProductInputConfigIn",
        "GoogleCloudRetailV2ProductInputConfigOut": "_retail_263_GoogleCloudRetailV2ProductInputConfigOut",
        "GoogleCloudRetailV2ImportCompletionDataResponseIn": "_retail_264_GoogleCloudRetailV2ImportCompletionDataResponseIn",
        "GoogleCloudRetailV2ImportCompletionDataResponseOut": "_retail_265_GoogleCloudRetailV2ImportCompletionDataResponseOut",
        "GoogleCloudRetailV2SearchResponseFacetFacetValueIn": "_retail_266_GoogleCloudRetailV2SearchResponseFacetFacetValueIn",
        "GoogleCloudRetailV2SearchResponseFacetFacetValueOut": "_retail_267_GoogleCloudRetailV2SearchResponseFacetFacetValueOut",
        "GoogleCloudRetailV2alphaModelPageOptimizationConfigCandidateIn": "_retail_268_GoogleCloudRetailV2alphaModelPageOptimizationConfigCandidateIn",
        "GoogleCloudRetailV2alphaModelPageOptimizationConfigCandidateOut": "_retail_269_GoogleCloudRetailV2alphaModelPageOptimizationConfigCandidateOut",
        "GoogleCloudRetailV2alphaOutputResultIn": "_retail_270_GoogleCloudRetailV2alphaOutputResultIn",
        "GoogleCloudRetailV2alphaOutputResultOut": "_retail_271_GoogleCloudRetailV2alphaOutputResultOut",
        "GoogleCloudRetailV2PriceInfoIn": "_retail_272_GoogleCloudRetailV2PriceInfoIn",
        "GoogleCloudRetailV2PriceInfoOut": "_retail_273_GoogleCloudRetailV2PriceInfoOut",
        "GoogleCloudRetailV2betaAddLocalInventoriesMetadataIn": "_retail_274_GoogleCloudRetailV2betaAddLocalInventoriesMetadataIn",
        "GoogleCloudRetailV2betaAddLocalInventoriesMetadataOut": "_retail_275_GoogleCloudRetailV2betaAddLocalInventoriesMetadataOut",
        "GoogleCloudRetailV2alphaModelIn": "_retail_276_GoogleCloudRetailV2alphaModelIn",
        "GoogleCloudRetailV2alphaModelOut": "_retail_277_GoogleCloudRetailV2alphaModelOut",
        "GoogleCloudRetailV2alphaRemoveLocalInventoriesMetadataIn": "_retail_278_GoogleCloudRetailV2alphaRemoveLocalInventoriesMetadataIn",
        "GoogleCloudRetailV2alphaRemoveLocalInventoriesMetadataOut": "_retail_279_GoogleCloudRetailV2alphaRemoveLocalInventoriesMetadataOut",
        "GoogleCloudRetailV2betaRejoinUserEventsMetadataIn": "_retail_280_GoogleCloudRetailV2betaRejoinUserEventsMetadataIn",
        "GoogleCloudRetailV2betaRejoinUserEventsMetadataOut": "_retail_281_GoogleCloudRetailV2betaRejoinUserEventsMetadataOut",
        "GoogleCloudRetailV2AddFulfillmentPlacesRequestIn": "_retail_282_GoogleCloudRetailV2AddFulfillmentPlacesRequestIn",
        "GoogleCloudRetailV2AddFulfillmentPlacesRequestOut": "_retail_283_GoogleCloudRetailV2AddFulfillmentPlacesRequestOut",
        "GoogleCloudRetailV2betaExportProductsResponseIn": "_retail_284_GoogleCloudRetailV2betaExportProductsResponseIn",
        "GoogleCloudRetailV2betaExportProductsResponseOut": "_retail_285_GoogleCloudRetailV2betaExportProductsResponseOut",
        "GoogleCloudRetailV2alphaSetInventoryMetadataIn": "_retail_286_GoogleCloudRetailV2alphaSetInventoryMetadataIn",
        "GoogleCloudRetailV2alphaSetInventoryMetadataOut": "_retail_287_GoogleCloudRetailV2alphaSetInventoryMetadataOut",
        "GoogleCloudRetailV2alphaCreateModelMetadataIn": "_retail_288_GoogleCloudRetailV2alphaCreateModelMetadataIn",
        "GoogleCloudRetailV2alphaCreateModelMetadataOut": "_retail_289_GoogleCloudRetailV2alphaCreateModelMetadataOut",
        "GoogleCloudRetailLoggingErrorLogIn": "_retail_290_GoogleCloudRetailLoggingErrorLogIn",
        "GoogleCloudRetailLoggingErrorLogOut": "_retail_291_GoogleCloudRetailLoggingErrorLogOut",
        "GoogleCloudRetailV2IntervalIn": "_retail_292_GoogleCloudRetailV2IntervalIn",
        "GoogleCloudRetailV2IntervalOut": "_retail_293_GoogleCloudRetailV2IntervalOut",
        "GoogleCloudRetailV2ProductDetailIn": "_retail_294_GoogleCloudRetailV2ProductDetailIn",
        "GoogleCloudRetailV2ProductDetailOut": "_retail_295_GoogleCloudRetailV2ProductDetailOut",
        "GoogleCloudRetailV2alphaAddLocalInventoriesMetadataIn": "_retail_296_GoogleCloudRetailV2alphaAddLocalInventoriesMetadataIn",
        "GoogleCloudRetailV2alphaAddLocalInventoriesMetadataOut": "_retail_297_GoogleCloudRetailV2alphaAddLocalInventoriesMetadataOut",
        "GoogleCloudRetailV2betaUserEventImportSummaryIn": "_retail_298_GoogleCloudRetailV2betaUserEventImportSummaryIn",
        "GoogleCloudRetailV2betaUserEventImportSummaryOut": "_retail_299_GoogleCloudRetailV2betaUserEventImportSummaryOut",
        "GoogleRpcStatusIn": "_retail_300_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_retail_301_GoogleRpcStatusOut",
        "GoogleCloudRetailV2betaImportProductsResponseIn": "_retail_302_GoogleCloudRetailV2betaImportProductsResponseIn",
        "GoogleCloudRetailV2betaImportProductsResponseOut": "_retail_303_GoogleCloudRetailV2betaImportProductsResponseOut",
        "GoogleCloudRetailV2betaExportMetadataIn": "_retail_304_GoogleCloudRetailV2betaExportMetadataIn",
        "GoogleCloudRetailV2betaExportMetadataOut": "_retail_305_GoogleCloudRetailV2betaExportMetadataOut",
        "GoogleCloudRetailV2RemoveFulfillmentPlacesMetadataIn": "_retail_306_GoogleCloudRetailV2RemoveFulfillmentPlacesMetadataIn",
        "GoogleCloudRetailV2RemoveFulfillmentPlacesMetadataOut": "_retail_307_GoogleCloudRetailV2RemoveFulfillmentPlacesMetadataOut",
        "GoogleCloudRetailV2RuleRedirectActionIn": "_retail_308_GoogleCloudRetailV2RuleRedirectActionIn",
        "GoogleCloudRetailV2RuleRedirectActionOut": "_retail_309_GoogleCloudRetailV2RuleRedirectActionOut",
        "GoogleCloudRetailV2RuleIgnoreActionIn": "_retail_310_GoogleCloudRetailV2RuleIgnoreActionIn",
        "GoogleCloudRetailV2RuleIgnoreActionOut": "_retail_311_GoogleCloudRetailV2RuleIgnoreActionOut",
        "GoogleCloudRetailV2CustomAttributeIn": "_retail_312_GoogleCloudRetailV2CustomAttributeIn",
        "GoogleCloudRetailV2CustomAttributeOut": "_retail_313_GoogleCloudRetailV2CustomAttributeOut",
        "GoogleCloudRetailV2alphaTuneModelResponseIn": "_retail_314_GoogleCloudRetailV2alphaTuneModelResponseIn",
        "GoogleCloudRetailV2alphaTuneModelResponseOut": "_retail_315_GoogleCloudRetailV2alphaTuneModelResponseOut",
        "GoogleCloudRetailV2PriceInfoPriceRangeIn": "_retail_316_GoogleCloudRetailV2PriceInfoPriceRangeIn",
        "GoogleCloudRetailV2PriceInfoPriceRangeOut": "_retail_317_GoogleCloudRetailV2PriceInfoPriceRangeOut",
        "GoogleCloudRetailV2UserEventIn": "_retail_318_GoogleCloudRetailV2UserEventIn",
        "GoogleCloudRetailV2UserEventOut": "_retail_319_GoogleCloudRetailV2UserEventOut",
        "GoogleCloudRetailLoggingServiceContextIn": "_retail_320_GoogleCloudRetailLoggingServiceContextIn",
        "GoogleCloudRetailLoggingServiceContextOut": "_retail_321_GoogleCloudRetailLoggingServiceContextOut",
        "GoogleCloudRetailV2GcsSourceIn": "_retail_322_GoogleCloudRetailV2GcsSourceIn",
        "GoogleCloudRetailV2GcsSourceOut": "_retail_323_GoogleCloudRetailV2GcsSourceOut",
        "GoogleCloudRetailV2RuleDoNotAssociateActionIn": "_retail_324_GoogleCloudRetailV2RuleDoNotAssociateActionIn",
        "GoogleCloudRetailV2RuleDoNotAssociateActionOut": "_retail_325_GoogleCloudRetailV2RuleDoNotAssociateActionOut",
        "GoogleCloudRetailV2betaImportCompletionDataResponseIn": "_retail_326_GoogleCloudRetailV2betaImportCompletionDataResponseIn",
        "GoogleCloudRetailV2betaImportCompletionDataResponseOut": "_retail_327_GoogleCloudRetailV2betaImportCompletionDataResponseOut",
        "GoogleCloudRetailV2betaOutputResultIn": "_retail_328_GoogleCloudRetailV2betaOutputResultIn",
        "GoogleCloudRetailV2betaOutputResultOut": "_retail_329_GoogleCloudRetailV2betaOutputResultOut",
        "GoogleCloudRetailV2PurchaseTransactionIn": "_retail_330_GoogleCloudRetailV2PurchaseTransactionIn",
        "GoogleCloudRetailV2PurchaseTransactionOut": "_retail_331_GoogleCloudRetailV2PurchaseTransactionOut",
        "GoogleCloudRetailV2RatingIn": "_retail_332_GoogleCloudRetailV2RatingIn",
        "GoogleCloudRetailV2RatingOut": "_retail_333_GoogleCloudRetailV2RatingOut",
        "GoogleCloudRetailV2UserEventImportSummaryIn": "_retail_334_GoogleCloudRetailV2UserEventImportSummaryIn",
        "GoogleCloudRetailV2UserEventImportSummaryOut": "_retail_335_GoogleCloudRetailV2UserEventImportSummaryOut",
        "GoogleCloudRetailV2ImportUserEventsResponseIn": "_retail_336_GoogleCloudRetailV2ImportUserEventsResponseIn",
        "GoogleCloudRetailV2ImportUserEventsResponseOut": "_retail_337_GoogleCloudRetailV2ImportUserEventsResponseOut",
        "GoogleCloudRetailV2CompleteQueryResponseCompletionResultIn": "_retail_338_GoogleCloudRetailV2CompleteQueryResponseCompletionResultIn",
        "GoogleCloudRetailV2CompleteQueryResponseCompletionResultOut": "_retail_339_GoogleCloudRetailV2CompleteQueryResponseCompletionResultOut",
        "GoogleCloudRetailV2ProductLevelConfigIn": "_retail_340_GoogleCloudRetailV2ProductLevelConfigIn",
        "GoogleCloudRetailV2ProductLevelConfigOut": "_retail_341_GoogleCloudRetailV2ProductLevelConfigOut",
        "GoogleCloudRetailV2SearchResponseQueryExpansionInfoIn": "_retail_342_GoogleCloudRetailV2SearchResponseQueryExpansionInfoIn",
        "GoogleCloudRetailV2SearchResponseQueryExpansionInfoOut": "_retail_343_GoogleCloudRetailV2SearchResponseQueryExpansionInfoOut",
        "GoogleCloudRetailV2alphaBigQueryOutputResultIn": "_retail_344_GoogleCloudRetailV2alphaBigQueryOutputResultIn",
        "GoogleCloudRetailV2alphaBigQueryOutputResultOut": "_retail_345_GoogleCloudRetailV2alphaBigQueryOutputResultOut",
        "GoogleCloudRetailV2alphaModelFrequentlyBoughtTogetherFeaturesConfigIn": "_retail_346_GoogleCloudRetailV2alphaModelFrequentlyBoughtTogetherFeaturesConfigIn",
        "GoogleCloudRetailV2alphaModelFrequentlyBoughtTogetherFeaturesConfigOut": "_retail_347_GoogleCloudRetailV2alphaModelFrequentlyBoughtTogetherFeaturesConfigOut",
        "GoogleCloudRetailV2PurgeMetadataIn": "_retail_348_GoogleCloudRetailV2PurgeMetadataIn",
        "GoogleCloudRetailV2PurgeMetadataOut": "_retail_349_GoogleCloudRetailV2PurgeMetadataOut",
        "GoogleProtobufEmptyIn": "_retail_350_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_retail_351_GoogleProtobufEmptyOut",
        "GoogleCloudRetailV2betaImportUserEventsResponseIn": "_retail_352_GoogleCloudRetailV2betaImportUserEventsResponseIn",
        "GoogleCloudRetailV2betaImportUserEventsResponseOut": "_retail_353_GoogleCloudRetailV2betaImportUserEventsResponseOut",
        "GoogleCloudRetailV2betaRejoinUserEventsResponseIn": "_retail_354_GoogleCloudRetailV2betaRejoinUserEventsResponseIn",
        "GoogleCloudRetailV2betaRejoinUserEventsResponseOut": "_retail_355_GoogleCloudRetailV2betaRejoinUserEventsResponseOut",
        "GoogleCloudRetailV2RuleTwowaySynonymsActionIn": "_retail_356_GoogleCloudRetailV2RuleTwowaySynonymsActionIn",
        "GoogleCloudRetailV2RuleTwowaySynonymsActionOut": "_retail_357_GoogleCloudRetailV2RuleTwowaySynonymsActionOut",
        "GoogleCloudRetailV2alphaModelModelFeaturesConfigIn": "_retail_358_GoogleCloudRetailV2alphaModelModelFeaturesConfigIn",
        "GoogleCloudRetailV2alphaModelModelFeaturesConfigOut": "_retail_359_GoogleCloudRetailV2alphaModelModelFeaturesConfigOut",
        "GoogleCloudRetailV2BigQuerySourceIn": "_retail_360_GoogleCloudRetailV2BigQuerySourceIn",
        "GoogleCloudRetailV2BigQuerySourceOut": "_retail_361_GoogleCloudRetailV2BigQuerySourceOut",
        "GoogleCloudRetailV2ExperimentInfoIn": "_retail_362_GoogleCloudRetailV2ExperimentInfoIn",
        "GoogleCloudRetailV2ExperimentInfoOut": "_retail_363_GoogleCloudRetailV2ExperimentInfoOut",
        "GoogleCloudRetailV2ImportProductsRequestIn": "_retail_364_GoogleCloudRetailV2ImportProductsRequestIn",
        "GoogleCloudRetailV2ImportProductsRequestOut": "_retail_365_GoogleCloudRetailV2ImportProductsRequestOut",
        "GoogleCloudRetailV2betaCreateModelMetadataIn": "_retail_366_GoogleCloudRetailV2betaCreateModelMetadataIn",
        "GoogleCloudRetailV2betaCreateModelMetadataOut": "_retail_367_GoogleCloudRetailV2betaCreateModelMetadataOut",
        "GoogleCloudRetailV2betaPurgeMetadataIn": "_retail_368_GoogleCloudRetailV2betaPurgeMetadataIn",
        "GoogleCloudRetailV2betaPurgeMetadataOut": "_retail_369_GoogleCloudRetailV2betaPurgeMetadataOut",
        "GoogleCloudRetailLoggingHttpRequestContextIn": "_retail_370_GoogleCloudRetailLoggingHttpRequestContextIn",
        "GoogleCloudRetailLoggingHttpRequestContextOut": "_retail_371_GoogleCloudRetailLoggingHttpRequestContextOut",
        "GoogleCloudRetailV2betaRemoveLocalInventoriesResponseIn": "_retail_372_GoogleCloudRetailV2betaRemoveLocalInventoriesResponseIn",
        "GoogleCloudRetailV2betaRemoveLocalInventoriesResponseOut": "_retail_373_GoogleCloudRetailV2betaRemoveLocalInventoriesResponseOut",
        "GoogleCloudRetailV2alphaExportMetadataIn": "_retail_374_GoogleCloudRetailV2alphaExportMetadataIn",
        "GoogleCloudRetailV2alphaExportMetadataOut": "_retail_375_GoogleCloudRetailV2alphaExportMetadataOut",
        "GoogleCloudRetailV2alphaModelServingConfigListIn": "_retail_376_GoogleCloudRetailV2alphaModelServingConfigListIn",
        "GoogleCloudRetailV2alphaModelServingConfigListOut": "_retail_377_GoogleCloudRetailV2alphaModelServingConfigListOut",
        "GoogleCloudRetailV2alphaModelPageOptimizationConfigIn": "_retail_378_GoogleCloudRetailV2alphaModelPageOptimizationConfigIn",
        "GoogleCloudRetailV2alphaModelPageOptimizationConfigOut": "_retail_379_GoogleCloudRetailV2alphaModelPageOptimizationConfigOut",
        "GoogleCloudRetailV2alphaImportMetadataIn": "_retail_380_GoogleCloudRetailV2alphaImportMetadataIn",
        "GoogleCloudRetailV2alphaImportMetadataOut": "_retail_381_GoogleCloudRetailV2alphaImportMetadataOut",
        "GoogleCloudRetailV2alphaExportErrorsConfigIn": "_retail_382_GoogleCloudRetailV2alphaExportErrorsConfigIn",
        "GoogleCloudRetailV2alphaExportErrorsConfigOut": "_retail_383_GoogleCloudRetailV2alphaExportErrorsConfigOut",
        "GoogleCloudRetailV2RuleIn": "_retail_384_GoogleCloudRetailV2RuleIn",
        "GoogleCloudRetailV2RuleOut": "_retail_385_GoogleCloudRetailV2RuleOut",
        "GoogleCloudRetailV2SearchRequestFacetSpecIn": "_retail_386_GoogleCloudRetailV2SearchRequestFacetSpecIn",
        "GoogleCloudRetailV2SearchRequestFacetSpecOut": "_retail_387_GoogleCloudRetailV2SearchRequestFacetSpecOut",
        "GoogleCloudRetailV2RuleFilterActionIn": "_retail_388_GoogleCloudRetailV2RuleFilterActionIn",
        "GoogleCloudRetailV2RuleFilterActionOut": "_retail_389_GoogleCloudRetailV2RuleFilterActionOut",
        "GoogleCloudRetailV2PurgeUserEventsRequestIn": "_retail_390_GoogleCloudRetailV2PurgeUserEventsRequestIn",
        "GoogleCloudRetailV2PurgeUserEventsRequestOut": "_retail_391_GoogleCloudRetailV2PurgeUserEventsRequestOut",
        "GoogleCloudRetailV2SearchRequestSpellCorrectionSpecIn": "_retail_392_GoogleCloudRetailV2SearchRequestSpellCorrectionSpecIn",
        "GoogleCloudRetailV2SearchRequestSpellCorrectionSpecOut": "_retail_393_GoogleCloudRetailV2SearchRequestSpellCorrectionSpecOut",
        "GoogleTypeDateIn": "_retail_394_GoogleTypeDateIn",
        "GoogleTypeDateOut": "_retail_395_GoogleTypeDateOut",
        "GoogleCloudRetailV2ListServingConfigsResponseIn": "_retail_396_GoogleCloudRetailV2ListServingConfigsResponseIn",
        "GoogleCloudRetailV2ListServingConfigsResponseOut": "_retail_397_GoogleCloudRetailV2ListServingConfigsResponseOut",
        "GoogleCloudRetailV2SearchRequestBoostSpecConditionBoostSpecIn": "_retail_398_GoogleCloudRetailV2SearchRequestBoostSpecConditionBoostSpecIn",
        "GoogleCloudRetailV2SearchRequestBoostSpecConditionBoostSpecOut": "_retail_399_GoogleCloudRetailV2SearchRequestBoostSpecConditionBoostSpecOut",
        "GoogleCloudRetailV2SearchRequestDynamicFacetSpecIn": "_retail_400_GoogleCloudRetailV2SearchRequestDynamicFacetSpecIn",
        "GoogleCloudRetailV2SearchRequestDynamicFacetSpecOut": "_retail_401_GoogleCloudRetailV2SearchRequestDynamicFacetSpecOut",
        "GoogleCloudRetailV2alphaRemoveFulfillmentPlacesMetadataIn": "_retail_402_GoogleCloudRetailV2alphaRemoveFulfillmentPlacesMetadataIn",
        "GoogleCloudRetailV2alphaRemoveFulfillmentPlacesMetadataOut": "_retail_403_GoogleCloudRetailV2alphaRemoveFulfillmentPlacesMetadataOut",
        "GoogleCloudRetailV2SearchRequestPersonalizationSpecIn": "_retail_404_GoogleCloudRetailV2SearchRequestPersonalizationSpecIn",
        "GoogleCloudRetailV2SearchRequestPersonalizationSpecOut": "_retail_405_GoogleCloudRetailV2SearchRequestPersonalizationSpecOut",
        "GoogleCloudRetailV2betaRemoveFulfillmentPlacesMetadataIn": "_retail_406_GoogleCloudRetailV2betaRemoveFulfillmentPlacesMetadataIn",
        "GoogleCloudRetailV2betaRemoveFulfillmentPlacesMetadataOut": "_retail_407_GoogleCloudRetailV2betaRemoveFulfillmentPlacesMetadataOut",
        "GoogleCloudRetailV2PromotionIn": "_retail_408_GoogleCloudRetailV2PromotionIn",
        "GoogleCloudRetailV2PromotionOut": "_retail_409_GoogleCloudRetailV2PromotionOut",
        "GoogleCloudRetailV2FulfillmentInfoIn": "_retail_410_GoogleCloudRetailV2FulfillmentInfoIn",
        "GoogleCloudRetailV2FulfillmentInfoOut": "_retail_411_GoogleCloudRetailV2FulfillmentInfoOut",
        "GoogleCloudRetailV2betaMerchantCenterAccountLinkIn": "_retail_412_GoogleCloudRetailV2betaMerchantCenterAccountLinkIn",
        "GoogleCloudRetailV2betaMerchantCenterAccountLinkOut": "_retail_413_GoogleCloudRetailV2betaMerchantCenterAccountLinkOut",
        "GoogleApiHttpBodyIn": "_retail_414_GoogleApiHttpBodyIn",
        "GoogleApiHttpBodyOut": "_retail_415_GoogleApiHttpBodyOut",
        "GoogleCloudRetailV2betaExportUserEventsResponseIn": "_retail_416_GoogleCloudRetailV2betaExportUserEventsResponseIn",
        "GoogleCloudRetailV2betaExportUserEventsResponseOut": "_retail_417_GoogleCloudRetailV2betaExportUserEventsResponseOut",
        "GoogleCloudRetailV2alphaCreateMerchantCenterAccountLinkMetadataIn": "_retail_418_GoogleCloudRetailV2alphaCreateMerchantCenterAccountLinkMetadataIn",
        "GoogleCloudRetailV2alphaCreateMerchantCenterAccountLinkMetadataOut": "_retail_419_GoogleCloudRetailV2alphaCreateMerchantCenterAccountLinkMetadataOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudRetailV2UserEventInputConfigIn"] = t.struct(
        {
            "bigQuerySource": t.proxy(renames["GoogleCloudRetailV2BigQuerySourceIn"]),
            "gcsSource": t.proxy(renames["GoogleCloudRetailV2GcsSourceIn"]),
            "userEventInlineSource": t.proxy(
                renames["GoogleCloudRetailV2UserEventInlineSourceIn"]
            ),
        }
    ).named(renames["GoogleCloudRetailV2UserEventInputConfigIn"])
    types["GoogleCloudRetailV2UserEventInputConfigOut"] = t.struct(
        {
            "bigQuerySource": t.proxy(renames["GoogleCloudRetailV2BigQuerySourceOut"]),
            "gcsSource": t.proxy(renames["GoogleCloudRetailV2GcsSourceOut"]),
            "userEventInlineSource": t.proxy(
                renames["GoogleCloudRetailV2UserEventInlineSourceOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2UserEventInputConfigOut"])
    types["GoogleCloudRetailV2ControlIn"] = t.struct(
        {
            "rule": t.proxy(renames["GoogleCloudRetailV2RuleIn"]).optional(),
            "searchSolutionUseCase": t.array(t.string()).optional(),
            "displayName": t.string(),
            "solutionTypes": t.array(t.string()),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2ControlIn"])
    types["GoogleCloudRetailV2ControlOut"] = t.struct(
        {
            "rule": t.proxy(renames["GoogleCloudRetailV2RuleOut"]).optional(),
            "searchSolutionUseCase": t.array(t.string()).optional(),
            "displayName": t.string(),
            "associatedServingConfigIds": t.array(t.string()).optional(),
            "solutionTypes": t.array(t.string()),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ControlOut"])
    types["GoogleCloudRetailV2ImportMetadataIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "successCount": t.string().optional(),
            "requestId": t.string().optional(),
            "notificationPubsubTopic": t.string().optional(),
            "createTime": t.string().optional(),
            "failureCount": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2ImportMetadataIn"])
    types["GoogleCloudRetailV2ImportMetadataOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "successCount": t.string().optional(),
            "requestId": t.string().optional(),
            "notificationPubsubTopic": t.string().optional(),
            "createTime": t.string().optional(),
            "failureCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ImportMetadataOut"])
    types["GoogleCloudRetailV2RemoveCatalogAttributeRequestIn"] = t.struct(
        {"key": t.string()}
    ).named(renames["GoogleCloudRetailV2RemoveCatalogAttributeRequestIn"])
    types["GoogleCloudRetailV2RemoveCatalogAttributeRequestOut"] = t.struct(
        {"key": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2RemoveCatalogAttributeRequestOut"])
    types["GoogleCloudRetailV2ResumeModelRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2ResumeModelRequestIn"])
    types["GoogleCloudRetailV2ResumeModelRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2ResumeModelRequestOut"])
    types["GoogleCloudRetailV2betaTuneModelMetadataIn"] = t.struct(
        {"model": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2betaTuneModelMetadataIn"])
    types["GoogleCloudRetailV2betaTuneModelMetadataOut"] = t.struct(
        {
            "model": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2betaTuneModelMetadataOut"])
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
    types["GoogleCloudRetailV2betaAddLocalInventoriesResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2betaAddLocalInventoriesResponseIn"])
    types["GoogleCloudRetailV2betaAddLocalInventoriesResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2betaAddLocalInventoriesResponseOut"])
    types["GoogleCloudRetailV2betaAddFulfillmentPlacesResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2betaAddFulfillmentPlacesResponseIn"])
    types["GoogleCloudRetailV2betaAddFulfillmentPlacesResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2betaAddFulfillmentPlacesResponseOut"])
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
    types["GoogleCloudRetailV2RemoveLocalInventoriesResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2RemoveLocalInventoriesResponseIn"])
    types["GoogleCloudRetailV2RemoveLocalInventoriesResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2RemoveLocalInventoriesResponseOut"])
    types["GoogleCloudRetailV2TuneModelMetadataIn"] = t.struct(
        {"model": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2TuneModelMetadataIn"])
    types["GoogleCloudRetailV2TuneModelMetadataOut"] = t.struct(
        {
            "model": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2TuneModelMetadataOut"])
    types["GoogleCloudRetailV2betaSetInventoryMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2betaSetInventoryMetadataIn"])
    types["GoogleCloudRetailV2betaSetInventoryMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2betaSetInventoryMetadataOut"])
    types["GoogleCloudRetailV2alphaMerchantCenterAccountLinkIn"] = t.struct(
        {
            "branchId": t.string(),
            "languageCode": t.string().optional(),
            "feedFilters": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudRetailV2alphaMerchantCenterAccountLinkMerchantCenterFeedFilterIn"
                    ]
                )
            ).optional(),
            "merchantCenterAccountId": t.string(),
            "feedLabel": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaMerchantCenterAccountLinkIn"])
    types["GoogleCloudRetailV2alphaMerchantCenterAccountLinkOut"] = t.struct(
        {
            "branchId": t.string(),
            "projectId": t.string().optional(),
            "languageCode": t.string().optional(),
            "state": t.string().optional(),
            "feedFilters": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudRetailV2alphaMerchantCenterAccountLinkMerchantCenterFeedFilterOut"
                    ]
                )
            ).optional(),
            "merchantCenterAccountId": t.string(),
            "feedLabel": t.string().optional(),
            "name": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaMerchantCenterAccountLinkOut"])
    types["GoogleCloudRetailV2RuleReplacementActionIn"] = t.struct(
        {
            "queryTerms": t.array(t.string()).optional(),
            "term": t.string().optional(),
            "replacementTerm": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2RuleReplacementActionIn"])
    types["GoogleCloudRetailV2RuleReplacementActionOut"] = t.struct(
        {
            "queryTerms": t.array(t.string()).optional(),
            "term": t.string().optional(),
            "replacementTerm": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2RuleReplacementActionOut"])
    types["GoogleCloudRetailV2CompletionConfigIn"] = t.struct(
        {
            "name": t.string(),
            "autoLearning": t.boolean().optional(),
            "matchingOrder": t.string().optional(),
            "minPrefixLength": t.integer().optional(),
            "maxSuggestions": t.integer().optional(),
        }
    ).named(renames["GoogleCloudRetailV2CompletionConfigIn"])
    types["GoogleCloudRetailV2CompletionConfigOut"] = t.struct(
        {
            "lastSuggestionsImportOperation": t.string().optional(),
            "name": t.string(),
            "suggestionsInputConfig": t.proxy(
                renames["GoogleCloudRetailV2CompletionDataInputConfigOut"]
            ).optional(),
            "lastAllowlistImportOperation": t.string().optional(),
            "allowlistInputConfig": t.proxy(
                renames["GoogleCloudRetailV2CompletionDataInputConfigOut"]
            ).optional(),
            "autoLearning": t.boolean().optional(),
            "matchingOrder": t.string().optional(),
            "denylistInputConfig": t.proxy(
                renames["GoogleCloudRetailV2CompletionDataInputConfigOut"]
            ).optional(),
            "minPrefixLength": t.integer().optional(),
            "maxSuggestions": t.integer().optional(),
            "lastDenylistImportOperation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2CompletionConfigOut"])
    types["GoogleCloudRetailV2betaModelServingConfigListIn"] = t.struct(
        {"servingConfigIds": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudRetailV2betaModelServingConfigListIn"])
    types["GoogleCloudRetailV2betaModelServingConfigListOut"] = t.struct(
        {
            "servingConfigIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2betaModelServingConfigListOut"])
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
    types["GoogleCloudRetailV2alphaRemoveFulfillmentPlacesResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2alphaRemoveFulfillmentPlacesResponseIn"])
    types["GoogleCloudRetailV2alphaRemoveFulfillmentPlacesResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2alphaRemoveFulfillmentPlacesResponseOut"])
    types["GoogleCloudRetailV2CatalogIn"] = t.struct(
        {
            "productLevelConfig": t.proxy(
                renames["GoogleCloudRetailV2ProductLevelConfigIn"]
            ),
            "name": t.string(),
            "displayName": t.string(),
        }
    ).named(renames["GoogleCloudRetailV2CatalogIn"])
    types["GoogleCloudRetailV2CatalogOut"] = t.struct(
        {
            "productLevelConfig": t.proxy(
                renames["GoogleCloudRetailV2ProductLevelConfigOut"]
            ),
            "name": t.string(),
            "displayName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2CatalogOut"])
    types["GoogleCloudRetailV2SearchResponseFacetIn"] = t.struct(
        {
            "key": t.string().optional(),
            "dynamicFacet": t.boolean().optional(),
            "values": t.array(
                t.proxy(renames["GoogleCloudRetailV2SearchResponseFacetFacetValueIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudRetailV2SearchResponseFacetIn"])
    types["GoogleCloudRetailV2SearchResponseFacetOut"] = t.struct(
        {
            "key": t.string().optional(),
            "dynamicFacet": t.boolean().optional(),
            "values": t.array(
                t.proxy(renames["GoogleCloudRetailV2SearchResponseFacetFacetValueOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2SearchResponseFacetOut"])
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
    types["GoogleCloudRetailV2RemoveLocalInventoriesMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2RemoveLocalInventoriesMetadataIn"])
    types["GoogleCloudRetailV2RemoveLocalInventoriesMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2RemoveLocalInventoriesMetadataOut"])
    types["GoogleCloudRetailV2betaExportErrorsConfigIn"] = t.struct(
        {"gcsPrefix": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2betaExportErrorsConfigIn"])
    types["GoogleCloudRetailV2betaExportErrorsConfigOut"] = t.struct(
        {
            "gcsPrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2betaExportErrorsConfigOut"])
    types["GoogleCloudRetailV2alphaAddFulfillmentPlacesMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2alphaAddFulfillmentPlacesMetadataIn"])
    types["GoogleCloudRetailV2alphaAddFulfillmentPlacesMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2alphaAddFulfillmentPlacesMetadataOut"])
    types["GoogleCloudRetailV2AudienceIn"] = t.struct(
        {
            "genders": t.array(t.string()).optional(),
            "ageGroups": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudRetailV2AudienceIn"])
    types["GoogleCloudRetailV2AudienceOut"] = t.struct(
        {
            "genders": t.array(t.string()).optional(),
            "ageGroups": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2AudienceOut"])
    types["GoogleCloudRetailV2betaSetInventoryResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2betaSetInventoryResponseIn"])
    types["GoogleCloudRetailV2betaSetInventoryResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2betaSetInventoryResponseOut"])
    types["GoogleCloudRetailV2alphaSetInventoryResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2alphaSetInventoryResponseIn"])
    types["GoogleCloudRetailV2alphaSetInventoryResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2alphaSetInventoryResponseOut"])
    types["GoogleCloudRetailV2CatalogAttributeIn"] = t.struct(
        {
            "indexableOption": t.string().optional(),
            "dynamicFacetableOption": t.string().optional(),
            "searchableOption": t.string().optional(),
            "retrievableOption": t.string().optional(),
            "key": t.string(),
            "exactSearchableOption": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2CatalogAttributeIn"])
    types["GoogleCloudRetailV2CatalogAttributeOut"] = t.struct(
        {
            "indexableOption": t.string().optional(),
            "dynamicFacetableOption": t.string().optional(),
            "inUse": t.boolean().optional(),
            "searchableOption": t.string().optional(),
            "retrievableOption": t.string().optional(),
            "key": t.string(),
            "type": t.string().optional(),
            "exactSearchableOption": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2CatalogAttributeOut"])
    types["GoogleCloudRetailV2RemoveLocalInventoriesRequestIn"] = t.struct(
        {
            "placeIds": t.array(t.string()),
            "allowMissing": t.boolean().optional(),
            "removeTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2RemoveLocalInventoriesRequestIn"])
    types["GoogleCloudRetailV2RemoveLocalInventoriesRequestOut"] = t.struct(
        {
            "placeIds": t.array(t.string()),
            "allowMissing": t.boolean().optional(),
            "removeTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2RemoveLocalInventoriesRequestOut"])
    types["GoogleCloudRetailV2TuneModelRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2TuneModelRequestIn"])
    types["GoogleCloudRetailV2TuneModelRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2TuneModelRequestOut"])
    types["GoogleCloudRetailV2ServingConfigIn"] = t.struct(
        {
            "ignoreControlIds": t.array(t.string()).optional(),
            "dynamicFacetSpec": t.proxy(
                renames["GoogleCloudRetailV2SearchRequestDynamicFacetSpecIn"]
            ).optional(),
            "diversityLevel": t.string().optional(),
            "onewaySynonymsControlIds": t.array(t.string()).optional(),
            "modelId": t.string().optional(),
            "boostControlIds": t.array(t.string()).optional(),
            "diversityType": t.string().optional(),
            "filterControlIds": t.array(t.string()).optional(),
            "enableCategoryFilterLevel": t.string().optional(),
            "doNotAssociateControlIds": t.array(t.string()).optional(),
            "twowaySynonymsControlIds": t.array(t.string()).optional(),
            "displayName": t.string(),
            "name": t.string().optional(),
            "redirectControlIds": t.array(t.string()).optional(),
            "replacementControlIds": t.array(t.string()).optional(),
            "priceRerankingLevel": t.string().optional(),
            "facetControlIds": t.array(t.string()).optional(),
            "solutionTypes": t.array(t.string()),
            "personalizationSpec": t.proxy(
                renames["GoogleCloudRetailV2SearchRequestPersonalizationSpecIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ServingConfigIn"])
    types["GoogleCloudRetailV2ServingConfigOut"] = t.struct(
        {
            "ignoreControlIds": t.array(t.string()).optional(),
            "dynamicFacetSpec": t.proxy(
                renames["GoogleCloudRetailV2SearchRequestDynamicFacetSpecOut"]
            ).optional(),
            "diversityLevel": t.string().optional(),
            "onewaySynonymsControlIds": t.array(t.string()).optional(),
            "modelId": t.string().optional(),
            "boostControlIds": t.array(t.string()).optional(),
            "diversityType": t.string().optional(),
            "filterControlIds": t.array(t.string()).optional(),
            "enableCategoryFilterLevel": t.string().optional(),
            "doNotAssociateControlIds": t.array(t.string()).optional(),
            "twowaySynonymsControlIds": t.array(t.string()).optional(),
            "displayName": t.string(),
            "name": t.string().optional(),
            "redirectControlIds": t.array(t.string()).optional(),
            "replacementControlIds": t.array(t.string()).optional(),
            "priceRerankingLevel": t.string().optional(),
            "facetControlIds": t.array(t.string()).optional(),
            "solutionTypes": t.array(t.string()),
            "personalizationSpec": t.proxy(
                renames["GoogleCloudRetailV2SearchRequestPersonalizationSpecOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ServingConfigOut"])
    types["GoogleCloudRetailV2alphaImportCompletionDataResponseIn"] = t.struct(
        {"errorSamples": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional()}
    ).named(renames["GoogleCloudRetailV2alphaImportCompletionDataResponseIn"])
    types["GoogleCloudRetailV2alphaImportCompletionDataResponseOut"] = t.struct(
        {
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaImportCompletionDataResponseOut"])
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
    types["GoogleCloudRetailV2SetDefaultBranchRequestIn"] = t.struct(
        {
            "note": t.string().optional(),
            "force": t.boolean().optional(),
            "branchId": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2SetDefaultBranchRequestIn"])
    types["GoogleCloudRetailV2SetDefaultBranchRequestOut"] = t.struct(
        {
            "note": t.string().optional(),
            "force": t.boolean().optional(),
            "branchId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2SetDefaultBranchRequestOut"])
    types["GoogleCloudRetailV2ImportErrorsConfigIn"] = t.struct(
        {"gcsPrefix": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2ImportErrorsConfigIn"])
    types["GoogleCloudRetailV2ImportErrorsConfigOut"] = t.struct(
        {
            "gcsPrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ImportErrorsConfigOut"])
    types["GoogleCloudRetailV2ProductInlineSourceIn"] = t.struct(
        {"products": t.array(t.proxy(renames["GoogleCloudRetailV2ProductIn"]))}
    ).named(renames["GoogleCloudRetailV2ProductInlineSourceIn"])
    types["GoogleCloudRetailV2ProductInlineSourceOut"] = t.struct(
        {
            "products": t.array(t.proxy(renames["GoogleCloudRetailV2ProductOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ProductInlineSourceOut"])
    types["GoogleCloudRetailV2alphaAddLocalInventoriesResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2alphaAddLocalInventoriesResponseIn"])
    types["GoogleCloudRetailV2alphaAddLocalInventoriesResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2alphaAddLocalInventoriesResponseOut"])
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
    types["GoogleCloudRetailV2PredictResponsePredictionResultIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2PredictResponsePredictionResultIn"])
    types["GoogleCloudRetailV2PredictResponsePredictionResultOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2PredictResponsePredictionResultOut"])
    types["GoogleCloudRetailV2betaPurgeUserEventsResponseIn"] = t.struct(
        {"purgedEventsCount": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2betaPurgeUserEventsResponseIn"])
    types["GoogleCloudRetailV2betaPurgeUserEventsResponseOut"] = t.struct(
        {
            "purgedEventsCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2betaPurgeUserEventsResponseOut"])
    types["GoogleCloudRetailV2SetInventoryResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2SetInventoryResponseIn"])
    types["GoogleCloudRetailV2SetInventoryResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2SetInventoryResponseOut"])
    types["GoogleCloudRetailV2alphaAddFulfillmentPlacesResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2alphaAddFulfillmentPlacesResponseIn"])
    types["GoogleCloudRetailV2alphaAddFulfillmentPlacesResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2alphaAddFulfillmentPlacesResponseOut"])
    types["GoogleCloudRetailV2betaImportErrorsConfigIn"] = t.struct(
        {"gcsPrefix": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2betaImportErrorsConfigIn"])
    types["GoogleCloudRetailV2betaImportErrorsConfigOut"] = t.struct(
        {
            "gcsPrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2betaImportErrorsConfigOut"])
    types["GoogleCloudRetailV2alphaImportErrorsConfigIn"] = t.struct(
        {"gcsPrefix": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2alphaImportErrorsConfigIn"])
    types["GoogleCloudRetailV2alphaImportErrorsConfigOut"] = t.struct(
        {
            "gcsPrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaImportErrorsConfigOut"])
    types["GoogleCloudRetailV2CompleteQueryResponseIn"] = t.struct(
        {
            "attributionToken": t.string().optional(),
            "completionResults": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudRetailV2CompleteQueryResponseCompletionResultIn"
                    ]
                )
            ).optional(),
            "recentSearchResults": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudRetailV2CompleteQueryResponseRecentSearchResultIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudRetailV2CompleteQueryResponseIn"])
    types["GoogleCloudRetailV2CompleteQueryResponseOut"] = t.struct(
        {
            "attributionToken": t.string().optional(),
            "completionResults": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudRetailV2CompleteQueryResponseCompletionResultOut"
                    ]
                )
            ).optional(),
            "recentSearchResults": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudRetailV2CompleteQueryResponseRecentSearchResultOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2CompleteQueryResponseOut"])
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
    types["GoogleCloudRetailV2PauseModelRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2PauseModelRequestIn"])
    types["GoogleCloudRetailV2PauseModelRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2PauseModelRequestOut"])
    types["GoogleCloudRetailV2RuleOnewaySynonymsActionIn"] = t.struct(
        {
            "queryTerms": t.array(t.string()).optional(),
            "synonyms": t.array(t.string()).optional(),
            "onewayTerms": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudRetailV2RuleOnewaySynonymsActionIn"])
    types["GoogleCloudRetailV2RuleOnewaySynonymsActionOut"] = t.struct(
        {
            "queryTerms": t.array(t.string()).optional(),
            "synonyms": t.array(t.string()).optional(),
            "onewayTerms": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2RuleOnewaySynonymsActionOut"])
    types["GoogleCloudRetailV2PurgeUserEventsResponseIn"] = t.struct(
        {"purgedEventsCount": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2PurgeUserEventsResponseIn"])
    types["GoogleCloudRetailV2PurgeUserEventsResponseOut"] = t.struct(
        {
            "purgedEventsCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2PurgeUserEventsResponseOut"])
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
    types["GoogleCloudRetailV2alphaPurgeMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2alphaPurgeMetadataIn"])
    types["GoogleCloudRetailV2alphaPurgeMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2alphaPurgeMetadataOut"])
    types["GoogleCloudRetailV2RemoveControlRequestIn"] = t.struct(
        {"controlId": t.string()}
    ).named(renames["GoogleCloudRetailV2RemoveControlRequestIn"])
    types["GoogleCloudRetailV2RemoveControlRequestOut"] = t.struct(
        {"controlId": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2RemoveControlRequestOut"])
    types["GoogleCloudRetailV2betaAddFulfillmentPlacesMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2betaAddFulfillmentPlacesMetadataIn"])
    types["GoogleCloudRetailV2betaAddFulfillmentPlacesMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2betaAddFulfillmentPlacesMetadataOut"])
    types["GoogleCloudRetailV2GetDefaultBranchResponseIn"] = t.struct(
        {
            "setTime": t.string().optional(),
            "note": t.string().optional(),
            "branch": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2GetDefaultBranchResponseIn"])
    types["GoogleCloudRetailV2GetDefaultBranchResponseOut"] = t.struct(
        {
            "setTime": t.string().optional(),
            "note": t.string().optional(),
            "branch": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2GetDefaultBranchResponseOut"])
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
    types["GoogleCloudRetailLoggingSourceLocationIn"] = t.struct(
        {"functionName": t.string().optional()}
    ).named(renames["GoogleCloudRetailLoggingSourceLocationIn"])
    types["GoogleCloudRetailLoggingSourceLocationOut"] = t.struct(
        {
            "functionName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailLoggingSourceLocationOut"])
    types["GoogleCloudRetailV2alphaModelPageOptimizationConfigPanelIn"] = t.struct(
        {
            "candidates": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudRetailV2alphaModelPageOptimizationConfigCandidateIn"
                    ]
                )
            ),
            "defaultCandidate": t.proxy(
                renames[
                    "GoogleCloudRetailV2alphaModelPageOptimizationConfigCandidateIn"
                ]
            ),
            "displayName": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaModelPageOptimizationConfigPanelIn"])
    types["GoogleCloudRetailV2alphaModelPageOptimizationConfigPanelOut"] = t.struct(
        {
            "candidates": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudRetailV2alphaModelPageOptimizationConfigCandidateOut"
                    ]
                )
            ),
            "defaultCandidate": t.proxy(
                renames[
                    "GoogleCloudRetailV2alphaModelPageOptimizationConfigCandidateOut"
                ]
            ),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaModelPageOptimizationConfigPanelOut"])
    types["GoogleCloudRetailV2RejoinUserEventsResponseIn"] = t.struct(
        {"rejoinedUserEventsCount": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2RejoinUserEventsResponseIn"])
    types["GoogleCloudRetailV2RejoinUserEventsResponseOut"] = t.struct(
        {
            "rejoinedUserEventsCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2RejoinUserEventsResponseOut"])
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
    types["GoogleCloudRetailV2ConditionQueryTermIn"] = t.struct(
        {"fullMatch": t.boolean().optional(), "value": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2ConditionQueryTermIn"])
    types["GoogleCloudRetailV2ConditionQueryTermOut"] = t.struct(
        {
            "fullMatch": t.boolean().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ConditionQueryTermOut"])
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
    types["GoogleCloudRetailV2SearchRequestQueryExpansionSpecIn"] = t.struct(
        {
            "pinUnexpandedResults": t.boolean().optional(),
            "condition": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2SearchRequestQueryExpansionSpecIn"])
    types["GoogleCloudRetailV2SearchRequestQueryExpansionSpecOut"] = t.struct(
        {
            "pinUnexpandedResults": t.boolean().optional(),
            "condition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2SearchRequestQueryExpansionSpecOut"])
    types["GoogleCloudRetailV2alphaTuneModelMetadataIn"] = t.struct(
        {"model": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2alphaTuneModelMetadataIn"])
    types["GoogleCloudRetailV2alphaTuneModelMetadataOut"] = t.struct(
        {
            "model": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaTuneModelMetadataOut"])
    types["GoogleCloudRetailV2alphaExportUserEventsResponseIn"] = t.struct(
        {
            "outputResult": t.proxy(
                renames["GoogleCloudRetailV2alphaOutputResultIn"]
            ).optional(),
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional(),
            "errorsConfig": t.proxy(
                renames["GoogleCloudRetailV2alphaExportErrorsConfigIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaExportUserEventsResponseIn"])
    types["GoogleCloudRetailV2alphaExportUserEventsResponseOut"] = t.struct(
        {
            "outputResult": t.proxy(
                renames["GoogleCloudRetailV2alphaOutputResultOut"]
            ).optional(),
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "errorsConfig": t.proxy(
                renames["GoogleCloudRetailV2alphaExportErrorsConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaExportUserEventsResponseOut"])
    types["GoogleCloudRetailV2betaGcsOutputResultIn"] = t.struct(
        {"outputUri": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2betaGcsOutputResultIn"])
    types["GoogleCloudRetailV2betaGcsOutputResultOut"] = t.struct(
        {
            "outputUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2betaGcsOutputResultOut"])
    types["GoogleCloudRetailV2SetInventoryMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2SetInventoryMetadataIn"])
    types["GoogleCloudRetailV2SetInventoryMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2SetInventoryMetadataOut"])
    types["GoogleCloudRetailV2betaBigQueryOutputResultIn"] = t.struct(
        {"datasetId": t.string().optional(), "tableId": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2betaBigQueryOutputResultIn"])
    types["GoogleCloudRetailV2betaBigQueryOutputResultOut"] = t.struct(
        {
            "datasetId": t.string().optional(),
            "tableId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2betaBigQueryOutputResultOut"])
    types["GoogleCloudRetailV2AddLocalInventoriesResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2AddLocalInventoriesResponseIn"])
    types["GoogleCloudRetailV2AddLocalInventoriesResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2AddLocalInventoriesResponseOut"])
    types["GoogleCloudRetailV2betaRemoveFulfillmentPlacesResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2betaRemoveFulfillmentPlacesResponseIn"])
    types["GoogleCloudRetailV2betaRemoveFulfillmentPlacesResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2betaRemoveFulfillmentPlacesResponseOut"])
    types["GoogleCloudRetailV2alphaImportUserEventsResponseIn"] = t.struct(
        {
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional(),
            "errorsConfig": t.proxy(
                renames["GoogleCloudRetailV2alphaImportErrorsConfigIn"]
            ).optional(),
            "importSummary": t.proxy(
                renames["GoogleCloudRetailV2alphaUserEventImportSummaryIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaImportUserEventsResponseIn"])
    types["GoogleCloudRetailV2alphaImportUserEventsResponseOut"] = t.struct(
        {
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "errorsConfig": t.proxy(
                renames["GoogleCloudRetailV2alphaImportErrorsConfigOut"]
            ).optional(),
            "importSummary": t.proxy(
                renames["GoogleCloudRetailV2alphaUserEventImportSummaryOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaImportUserEventsResponseOut"])
    types["GoogleCloudRetailV2ModelServingConfigListIn"] = t.struct(
        {"servingConfigIds": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudRetailV2ModelServingConfigListIn"])
    types["GoogleCloudRetailV2ModelServingConfigListOut"] = t.struct(
        {
            "servingConfigIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ModelServingConfigListOut"])
    types["GoogleCloudRetailV2SearchRequestFacetSpecFacetKeyIn"] = t.struct(
        {
            "query": t.string().optional(),
            "intervals": t.array(
                t.proxy(renames["GoogleCloudRetailV2IntervalIn"])
            ).optional(),
            "restrictedValues": t.array(t.string()).optional(),
            "caseInsensitive": t.boolean().optional(),
            "contains": t.array(t.string()).optional(),
            "orderBy": t.string().optional(),
            "prefixes": t.array(t.string()).optional(),
            "returnMinMax": t.boolean().optional(),
            "key": t.string(),
        }
    ).named(renames["GoogleCloudRetailV2SearchRequestFacetSpecFacetKeyIn"])
    types["GoogleCloudRetailV2SearchRequestFacetSpecFacetKeyOut"] = t.struct(
        {
            "query": t.string().optional(),
            "intervals": t.array(
                t.proxy(renames["GoogleCloudRetailV2IntervalOut"])
            ).optional(),
            "restrictedValues": t.array(t.string()).optional(),
            "caseInsensitive": t.boolean().optional(),
            "contains": t.array(t.string()).optional(),
            "orderBy": t.string().optional(),
            "prefixes": t.array(t.string()).optional(),
            "returnMinMax": t.boolean().optional(),
            "key": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2SearchRequestFacetSpecFacetKeyOut"])
    types["GoogleCloudRetailV2CompletionDetailIn"] = t.struct(
        {
            "completionAttributionToken": t.string().optional(),
            "selectedPosition": t.integer().optional(),
            "selectedSuggestion": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2CompletionDetailIn"])
    types["GoogleCloudRetailV2CompletionDetailOut"] = t.struct(
        {
            "completionAttributionToken": t.string().optional(),
            "selectedPosition": t.integer().optional(),
            "selectedSuggestion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2CompletionDetailOut"])
    types["GoogleCloudRetailV2AddFulfillmentPlacesMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2AddFulfillmentPlacesMetadataIn"])
    types["GoogleCloudRetailV2AddFulfillmentPlacesMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2AddFulfillmentPlacesMetadataOut"])
    types["GoogleCloudRetailLoggingImportErrorContextIn"] = t.struct(
        {
            "operationName": t.string().optional(),
            "catalogItem": t.string().optional(),
            "gcsPath": t.string().optional(),
            "lineNumber": t.string().optional(),
            "userEvent": t.string().optional(),
            "product": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailLoggingImportErrorContextIn"])
    types["GoogleCloudRetailLoggingImportErrorContextOut"] = t.struct(
        {
            "operationName": t.string().optional(),
            "catalogItem": t.string().optional(),
            "gcsPath": t.string().optional(),
            "lineNumber": t.string().optional(),
            "userEvent": t.string().optional(),
            "product": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailLoggingImportErrorContextOut"])
    types["GoogleCloudRetailV2alphaRejoinUserEventsMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2alphaRejoinUserEventsMetadataIn"])
    types["GoogleCloudRetailV2alphaRejoinUserEventsMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2alphaRejoinUserEventsMetadataOut"])
    types["GoogleCloudRetailV2CompletionDataInputConfigIn"] = t.struct(
        {"bigQuerySource": t.proxy(renames["GoogleCloudRetailV2BigQuerySourceIn"])}
    ).named(renames["GoogleCloudRetailV2CompletionDataInputConfigIn"])
    types["GoogleCloudRetailV2CompletionDataInputConfigOut"] = t.struct(
        {
            "bigQuerySource": t.proxy(renames["GoogleCloudRetailV2BigQuerySourceOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2CompletionDataInputConfigOut"])
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
    types["GoogleCloudRetailV2alphaPurgeUserEventsResponseIn"] = t.struct(
        {"purgedEventsCount": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2alphaPurgeUserEventsResponseIn"])
    types["GoogleCloudRetailV2alphaPurgeUserEventsResponseOut"] = t.struct(
        {
            "purgedEventsCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaPurgeUserEventsResponseOut"])
    types["GoogleCloudRetailV2LocalInventoryIn"] = t.struct(
        {
            "fulfillmentTypes": t.array(t.string()).optional(),
            "placeId": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "priceInfo": t.proxy(renames["GoogleCloudRetailV2PriceInfoIn"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2LocalInventoryIn"])
    types["GoogleCloudRetailV2LocalInventoryOut"] = t.struct(
        {
            "fulfillmentTypes": t.array(t.string()).optional(),
            "placeId": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "priceInfo": t.proxy(renames["GoogleCloudRetailV2PriceInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2LocalInventoryOut"])
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
    types["GoogleCloudRetailV2betaTuneModelResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2betaTuneModelResponseIn"])
    types["GoogleCloudRetailV2betaTuneModelResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2betaTuneModelResponseOut"])
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
    types["GoogleCloudRetailV2RemoveFulfillmentPlacesResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2RemoveFulfillmentPlacesResponseIn"])
    types["GoogleCloudRetailV2RemoveFulfillmentPlacesResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2RemoveFulfillmentPlacesResponseOut"])
    types["GoogleCloudRetailV2RemoveFulfillmentPlacesRequestIn"] = t.struct(
        {
            "type": t.string(),
            "allowMissing": t.boolean().optional(),
            "placeIds": t.array(t.string()),
            "removeTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2RemoveFulfillmentPlacesRequestIn"])
    types["GoogleCloudRetailV2RemoveFulfillmentPlacesRequestOut"] = t.struct(
        {
            "type": t.string(),
            "allowMissing": t.boolean().optional(),
            "placeIds": t.array(t.string()),
            "removeTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2RemoveFulfillmentPlacesRequestOut"])
    types["GoogleCloudRetailV2RejoinUserEventsMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2RejoinUserEventsMetadataIn"])
    types["GoogleCloudRetailV2RejoinUserEventsMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2RejoinUserEventsMetadataOut"])
    types["GoogleCloudRetailV2UserInfoIn"] = t.struct(
        {
            "ipAddress": t.string().optional(),
            "userAgent": t.string().optional(),
            "directUserRequest": t.boolean().optional(),
            "userId": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2UserInfoIn"])
    types["GoogleCloudRetailV2UserInfoOut"] = t.struct(
        {
            "ipAddress": t.string().optional(),
            "userAgent": t.string().optional(),
            "directUserRequest": t.boolean().optional(),
            "userId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2UserInfoOut"])
    types["GoogleCloudRetailV2ImageIn"] = t.struct(
        {
            "height": t.integer().optional(),
            "uri": t.string(),
            "width": t.integer().optional(),
        }
    ).named(renames["GoogleCloudRetailV2ImageIn"])
    types["GoogleCloudRetailV2ImageOut"] = t.struct(
        {
            "height": t.integer().optional(),
            "uri": t.string(),
            "width": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ImageOut"])
    types["GoogleCloudRetailV2betaRemoveLocalInventoriesMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2betaRemoveLocalInventoriesMetadataIn"])
    types["GoogleCloudRetailV2betaRemoveLocalInventoriesMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2betaRemoveLocalInventoriesMetadataOut"])
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
    types["GoogleCloudRetailV2SearchResponseIn"] = t.struct(
        {
            "queryExpansionInfo": t.proxy(
                renames["GoogleCloudRetailV2SearchResponseQueryExpansionInfoIn"]
            ).optional(),
            "totalSize": t.integer().optional(),
            "redirectUri": t.string().optional(),
            "results": t.array(
                t.proxy(renames["GoogleCloudRetailV2SearchResponseSearchResultIn"])
            ).optional(),
            "invalidConditionBoostSpecs": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudRetailV2SearchRequestBoostSpecConditionBoostSpecIn"
                    ]
                )
            ).optional(),
            "facets": t.array(
                t.proxy(renames["GoogleCloudRetailV2SearchResponseFacetIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "experimentInfo": t.array(
                t.proxy(renames["GoogleCloudRetailV2ExperimentInfoIn"])
            ).optional(),
            "correctedQuery": t.string().optional(),
            "appliedControls": t.array(t.string()).optional(),
            "attributionToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2SearchResponseIn"])
    types["GoogleCloudRetailV2SearchResponseOut"] = t.struct(
        {
            "queryExpansionInfo": t.proxy(
                renames["GoogleCloudRetailV2SearchResponseQueryExpansionInfoOut"]
            ).optional(),
            "totalSize": t.integer().optional(),
            "redirectUri": t.string().optional(),
            "results": t.array(
                t.proxy(renames["GoogleCloudRetailV2SearchResponseSearchResultOut"])
            ).optional(),
            "invalidConditionBoostSpecs": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudRetailV2SearchRequestBoostSpecConditionBoostSpecOut"
                    ]
                )
            ).optional(),
            "facets": t.array(
                t.proxy(renames["GoogleCloudRetailV2SearchResponseFacetOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "experimentInfo": t.array(
                t.proxy(renames["GoogleCloudRetailV2ExperimentInfoOut"])
            ).optional(),
            "correctedQuery": t.string().optional(),
            "appliedControls": t.array(t.string()).optional(),
            "attributionToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2SearchResponseOut"])
    types["GoogleCloudRetailV2RejoinUserEventsRequestIn"] = t.struct(
        {"userEventRejoinScope": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2RejoinUserEventsRequestIn"])
    types["GoogleCloudRetailV2RejoinUserEventsRequestOut"] = t.struct(
        {
            "userEventRejoinScope": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2RejoinUserEventsRequestOut"])
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
    types["GoogleCloudRetailV2SearchResponseSearchResultIn"] = t.struct(
        {
            "id": t.string().optional(),
            "matchingVariantFields": t.struct({"_": t.string().optional()}).optional(),
            "variantRollupValues": t.struct({"_": t.string().optional()}).optional(),
            "personalLabels": t.array(t.string()).optional(),
            "matchingVariantCount": t.integer().optional(),
            "product": t.proxy(renames["GoogleCloudRetailV2ProductIn"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2SearchResponseSearchResultIn"])
    types["GoogleCloudRetailV2SearchResponseSearchResultOut"] = t.struct(
        {
            "id": t.string().optional(),
            "matchingVariantFields": t.struct({"_": t.string().optional()}).optional(),
            "variantRollupValues": t.struct({"_": t.string().optional()}).optional(),
            "personalLabels": t.array(t.string()).optional(),
            "matchingVariantCount": t.integer().optional(),
            "product": t.proxy(renames["GoogleCloudRetailV2ProductOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2SearchResponseSearchResultOut"])
    types["GoogleCloudRetailV2ProductIn"] = t.struct(
        {
            "sizes": t.array(t.string()).optional(),
            "colorInfo": t.proxy(renames["GoogleCloudRetailV2ColorInfoIn"]).optional(),
            "patterns": t.array(t.string()).optional(),
            "images": t.array(
                t.proxy(renames["GoogleCloudRetailV2ImageIn"])
            ).optional(),
            "expireTime": t.string().optional(),
            "categories": t.array(t.string()).optional(),
            "brands": t.array(t.string()).optional(),
            "type": t.string().optional(),
            "uri": t.string().optional(),
            "retrievableFields": t.string().optional(),
            "primaryProductId": t.string().optional(),
            "collectionMemberIds": t.array(t.string()).optional(),
            "promotions": t.array(
                t.proxy(renames["GoogleCloudRetailV2PromotionIn"])
            ).optional(),
            "rating": t.proxy(renames["GoogleCloudRetailV2RatingIn"]).optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "availability": t.string().optional(),
            "fulfillmentInfo": t.array(
                t.proxy(renames["GoogleCloudRetailV2FulfillmentInfoIn"])
            ).optional(),
            "priceInfo": t.proxy(renames["GoogleCloudRetailV2PriceInfoIn"]).optional(),
            "description": t.string().optional(),
            "publishTime": t.string().optional(),
            "conditions": t.array(t.string()).optional(),
            "materials": t.array(t.string()).optional(),
            "gtin": t.string().optional(),
            "languageCode": t.string().optional(),
            "audience": t.proxy(renames["GoogleCloudRetailV2AudienceIn"]).optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "availableQuantity": t.integer().optional(),
            "title": t.string(),
            "ttl": t.string().optional(),
            "availableTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2ProductIn"])
    types["GoogleCloudRetailV2ProductOut"] = t.struct(
        {
            "sizes": t.array(t.string()).optional(),
            "colorInfo": t.proxy(renames["GoogleCloudRetailV2ColorInfoOut"]).optional(),
            "patterns": t.array(t.string()).optional(),
            "images": t.array(
                t.proxy(renames["GoogleCloudRetailV2ImageOut"])
            ).optional(),
            "expireTime": t.string().optional(),
            "categories": t.array(t.string()).optional(),
            "brands": t.array(t.string()).optional(),
            "type": t.string().optional(),
            "uri": t.string().optional(),
            "retrievableFields": t.string().optional(),
            "primaryProductId": t.string().optional(),
            "collectionMemberIds": t.array(t.string()).optional(),
            "promotions": t.array(
                t.proxy(renames["GoogleCloudRetailV2PromotionOut"])
            ).optional(),
            "rating": t.proxy(renames["GoogleCloudRetailV2RatingOut"]).optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "availability": t.string().optional(),
            "fulfillmentInfo": t.array(
                t.proxy(renames["GoogleCloudRetailV2FulfillmentInfoOut"])
            ).optional(),
            "priceInfo": t.proxy(renames["GoogleCloudRetailV2PriceInfoOut"]).optional(),
            "variants": t.array(
                t.proxy(renames["GoogleCloudRetailV2ProductOut"])
            ).optional(),
            "description": t.string().optional(),
            "publishTime": t.string().optional(),
            "conditions": t.array(t.string()).optional(),
            "materials": t.array(t.string()).optional(),
            "gtin": t.string().optional(),
            "localInventories": t.array(
                t.proxy(renames["GoogleCloudRetailV2LocalInventoryOut"])
            ).optional(),
            "languageCode": t.string().optional(),
            "audience": t.proxy(renames["GoogleCloudRetailV2AudienceOut"]).optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "availableQuantity": t.integer().optional(),
            "title": t.string(),
            "ttl": t.string().optional(),
            "availableTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ProductOut"])
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
    types["GoogleCloudRetailV2SearchRequestIn"] = t.struct(
        {
            "pageToken": t.string().optional(),
            "variantRollupKeys": t.array(t.string()).optional(),
            "canonicalFilter": t.string().optional(),
            "offset": t.integer().optional(),
            "pageSize": t.integer().optional(),
            "spellCorrectionSpec": t.proxy(
                renames["GoogleCloudRetailV2SearchRequestSpellCorrectionSpecIn"]
            ).optional(),
            "visitorId": t.string(),
            "dynamicFacetSpec": t.proxy(
                renames["GoogleCloudRetailV2SearchRequestDynamicFacetSpecIn"]
            ).optional(),
            "orderBy": t.string().optional(),
            "userInfo": t.proxy(renames["GoogleCloudRetailV2UserInfoIn"]).optional(),
            "entity": t.string().optional(),
            "branch": t.string().optional(),
            "personalizationSpec": t.proxy(
                renames["GoogleCloudRetailV2SearchRequestPersonalizationSpecIn"]
            ).optional(),
            "pageCategories": t.array(t.string()).optional(),
            "facetSpecs": t.array(
                t.proxy(renames["GoogleCloudRetailV2SearchRequestFacetSpecIn"])
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "boostSpec": t.proxy(
                renames["GoogleCloudRetailV2SearchRequestBoostSpecIn"]
            ).optional(),
            "filter": t.string().optional(),
            "searchMode": t.string().optional(),
            "query": t.string().optional(),
            "queryExpansionSpec": t.proxy(
                renames["GoogleCloudRetailV2SearchRequestQueryExpansionSpecIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudRetailV2SearchRequestIn"])
    types["GoogleCloudRetailV2SearchRequestOut"] = t.struct(
        {
            "pageToken": t.string().optional(),
            "variantRollupKeys": t.array(t.string()).optional(),
            "canonicalFilter": t.string().optional(),
            "offset": t.integer().optional(),
            "pageSize": t.integer().optional(),
            "spellCorrectionSpec": t.proxy(
                renames["GoogleCloudRetailV2SearchRequestSpellCorrectionSpecOut"]
            ).optional(),
            "visitorId": t.string(),
            "dynamicFacetSpec": t.proxy(
                renames["GoogleCloudRetailV2SearchRequestDynamicFacetSpecOut"]
            ).optional(),
            "orderBy": t.string().optional(),
            "userInfo": t.proxy(renames["GoogleCloudRetailV2UserInfoOut"]).optional(),
            "entity": t.string().optional(),
            "branch": t.string().optional(),
            "personalizationSpec": t.proxy(
                renames["GoogleCloudRetailV2SearchRequestPersonalizationSpecOut"]
            ).optional(),
            "pageCategories": t.array(t.string()).optional(),
            "facetSpecs": t.array(
                t.proxy(renames["GoogleCloudRetailV2SearchRequestFacetSpecOut"])
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "boostSpec": t.proxy(
                renames["GoogleCloudRetailV2SearchRequestBoostSpecOut"]
            ).optional(),
            "filter": t.string().optional(),
            "searchMode": t.string().optional(),
            "query": t.string().optional(),
            "queryExpansionSpec": t.proxy(
                renames["GoogleCloudRetailV2SearchRequestQueryExpansionSpecOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2SearchRequestOut"])
    types["GoogleCloudRetailV2UserEventInlineSourceIn"] = t.struct(
        {"userEvents": t.array(t.proxy(renames["GoogleCloudRetailV2UserEventIn"]))}
    ).named(renames["GoogleCloudRetailV2UserEventInlineSourceIn"])
    types["GoogleCloudRetailV2UserEventInlineSourceOut"] = t.struct(
        {
            "userEvents": t.array(t.proxy(renames["GoogleCloudRetailV2UserEventOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2UserEventInlineSourceOut"])
    types["GoogleCloudRetailV2AttributesConfigIn"] = t.struct(
        {
            "catalogAttributes": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string(),
        }
    ).named(renames["GoogleCloudRetailV2AttributesConfigIn"])
    types["GoogleCloudRetailV2AttributesConfigOut"] = t.struct(
        {
            "attributeConfigLevel": t.string().optional(),
            "catalogAttributes": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2AttributesConfigOut"])
    types["GoogleCloudRetailV2CompleteQueryResponseRecentSearchResultIn"] = t.struct(
        {"recentSearch": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2CompleteQueryResponseRecentSearchResultIn"])
    types["GoogleCloudRetailV2CompleteQueryResponseRecentSearchResultOut"] = t.struct(
        {
            "recentSearch": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2CompleteQueryResponseRecentSearchResultOut"])
    types["GoogleCloudRetailV2alphaExportProductsResponseIn"] = t.struct(
        {
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional(),
            "errorsConfig": t.proxy(
                renames["GoogleCloudRetailV2alphaExportErrorsConfigIn"]
            ).optional(),
            "outputResult": t.proxy(
                renames["GoogleCloudRetailV2alphaOutputResultIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaExportProductsResponseIn"])
    types["GoogleCloudRetailV2alphaExportProductsResponseOut"] = t.struct(
        {
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "errorsConfig": t.proxy(
                renames["GoogleCloudRetailV2alphaExportErrorsConfigOut"]
            ).optional(),
            "outputResult": t.proxy(
                renames["GoogleCloudRetailV2alphaOutputResultOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaExportProductsResponseOut"])
    types["GoogleCloudRetailV2AddFulfillmentPlacesResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2AddFulfillmentPlacesResponseIn"])
    types["GoogleCloudRetailV2AddFulfillmentPlacesResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2AddFulfillmentPlacesResponseOut"])
    types["GoogleCloudRetailV2AddLocalInventoriesRequestIn"] = t.struct(
        {
            "addTime": t.string().optional(),
            "allowMissing": t.boolean().optional(),
            "localInventories": t.array(
                t.proxy(renames["GoogleCloudRetailV2LocalInventoryIn"])
            ),
            "addMask": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2AddLocalInventoriesRequestIn"])
    types["GoogleCloudRetailV2AddLocalInventoriesRequestOut"] = t.struct(
        {
            "addTime": t.string().optional(),
            "allowMissing": t.boolean().optional(),
            "localInventories": t.array(
                t.proxy(renames["GoogleCloudRetailV2LocalInventoryOut"])
            ),
            "addMask": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2AddLocalInventoriesRequestOut"])
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
    types["GoogleCloudRetailV2TuneModelResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2TuneModelResponseIn"])
    types["GoogleCloudRetailV2TuneModelResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2TuneModelResponseOut"])
    types["GoogleCloudRetailV2PredictRequestIn"] = t.struct(
        {
            "validateOnly": t.boolean().optional(),
            "filter": t.string().optional(),
            "pageSize": t.integer().optional(),
            "userEvent": t.proxy(renames["GoogleCloudRetailV2UserEventIn"]),
            "params": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "pageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2PredictRequestIn"])
    types["GoogleCloudRetailV2PredictRequestOut"] = t.struct(
        {
            "validateOnly": t.boolean().optional(),
            "filter": t.string().optional(),
            "pageSize": t.integer().optional(),
            "userEvent": t.proxy(renames["GoogleCloudRetailV2UserEventOut"]),
            "params": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "pageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2PredictRequestOut"])
    types["GoogleCloudRetailV2alphaPurgeProductsMetadataIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "failureCount": t.string().optional(),
            "successCount": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaPurgeProductsMetadataIn"])
    types["GoogleCloudRetailV2alphaPurgeProductsMetadataOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "failureCount": t.string().optional(),
            "successCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaPurgeProductsMetadataOut"])
    types["GoogleCloudRetailV2betaModelIn"] = t.struct(
        {
            "periodicTuningState": t.string().optional(),
            "modelFeaturesConfig": t.proxy(
                renames["GoogleCloudRetailV2betaModelModelFeaturesConfigIn"]
            ).optional(),
            "trainingState": t.string().optional(),
            "name": t.string(),
            "filteringOption": t.string().optional(),
            "type": t.string(),
            "optimizationObjective": t.string().optional(),
            "displayName": t.string(),
        }
    ).named(renames["GoogleCloudRetailV2betaModelIn"])
    types["GoogleCloudRetailV2betaModelOut"] = t.struct(
        {
            "periodicTuningState": t.string().optional(),
            "modelFeaturesConfig": t.proxy(
                renames["GoogleCloudRetailV2betaModelModelFeaturesConfigOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "trainingState": t.string().optional(),
            "name": t.string(),
            "filteringOption": t.string().optional(),
            "type": t.string(),
            "servingConfigLists": t.array(
                t.proxy(renames["GoogleCloudRetailV2betaModelServingConfigListOut"])
            ).optional(),
            "servingState": t.string().optional(),
            "tuningOperation": t.string().optional(),
            "optimizationObjective": t.string().optional(),
            "displayName": t.string(),
            "dataState": t.string().optional(),
            "lastTuneTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2betaModelOut"])
    types["GoogleCloudRetailV2CreateModelMetadataIn"] = t.struct(
        {"model": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2CreateModelMetadataIn"])
    types["GoogleCloudRetailV2CreateModelMetadataOut"] = t.struct(
        {
            "model": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2CreateModelMetadataOut"])
    types["GoogleCloudRetailV2alphaRemoveLocalInventoriesResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2alphaRemoveLocalInventoriesResponseIn"])
    types["GoogleCloudRetailV2alphaRemoveLocalInventoriesResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2alphaRemoveLocalInventoriesResponseOut"])
    types["GoogleCloudRetailV2alphaRejoinUserEventsResponseIn"] = t.struct(
        {"rejoinedUserEventsCount": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2alphaRejoinUserEventsResponseIn"])
    types["GoogleCloudRetailV2alphaRejoinUserEventsResponseOut"] = t.struct(
        {
            "rejoinedUserEventsCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaRejoinUserEventsResponseOut"])
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
    types["GoogleCloudRetailV2ImportUserEventsRequestIn"] = t.struct(
        {
            "errorsConfig": t.proxy(
                renames["GoogleCloudRetailV2ImportErrorsConfigIn"]
            ).optional(),
            "inputConfig": t.proxy(
                renames["GoogleCloudRetailV2UserEventInputConfigIn"]
            ),
        }
    ).named(renames["GoogleCloudRetailV2ImportUserEventsRequestIn"])
    types["GoogleCloudRetailV2ImportUserEventsRequestOut"] = t.struct(
        {
            "errorsConfig": t.proxy(
                renames["GoogleCloudRetailV2ImportErrorsConfigOut"]
            ).optional(),
            "inputConfig": t.proxy(
                renames["GoogleCloudRetailV2UserEventInputConfigOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ImportUserEventsRequestOut"])
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
    types["GoogleCloudRetailV2alphaGcsOutputResultIn"] = t.struct(
        {"outputUri": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2alphaGcsOutputResultIn"])
    types["GoogleCloudRetailV2alphaGcsOutputResultOut"] = t.struct(
        {
            "outputUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaGcsOutputResultOut"])
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
    types[
        "GoogleCloudRetailV2betaCreateMerchantCenterAccountLinkMetadataIn"
    ] = t.struct(
        {"updateTime": t.string().optional(), "createTime": t.string().optional()}
    ).named(
        renames["GoogleCloudRetailV2betaCreateMerchantCenterAccountLinkMetadataIn"]
    )
    types[
        "GoogleCloudRetailV2betaCreateMerchantCenterAccountLinkMetadataOut"
    ] = t.struct(
        {
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudRetailV2betaCreateMerchantCenterAccountLinkMetadataOut"]
    )
    types["GoogleCloudRetailV2ModelIn"] = t.struct(
        {
            "name": t.string(),
            "trainingState": t.string().optional(),
            "displayName": t.string(),
            "filteringOption": t.string().optional(),
            "periodicTuningState": t.string().optional(),
            "type": t.string(),
            "modelFeaturesConfig": t.proxy(
                renames["GoogleCloudRetailV2ModelModelFeaturesConfigIn"]
            ).optional(),
            "optimizationObjective": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2ModelIn"])
    types["GoogleCloudRetailV2ModelOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "name": t.string(),
            "servingState": t.string().optional(),
            "trainingState": t.string().optional(),
            "displayName": t.string(),
            "filteringOption": t.string().optional(),
            "periodicTuningState": t.string().optional(),
            "tuningOperation": t.string().optional(),
            "dataState": t.string().optional(),
            "servingConfigLists": t.array(
                t.proxy(renames["GoogleCloudRetailV2ModelServingConfigListOut"])
            ).optional(),
            "type": t.string(),
            "modelFeaturesConfig": t.proxy(
                renames["GoogleCloudRetailV2ModelModelFeaturesConfigOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "optimizationObjective": t.string().optional(),
            "lastTuneTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ModelOut"])
    types["GoogleCloudRetailV2ListProductsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "products": t.array(
                t.proxy(renames["GoogleCloudRetailV2ProductIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ListProductsResponseIn"])
    types["GoogleCloudRetailV2ListProductsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "products": t.array(
                t.proxy(renames["GoogleCloudRetailV2ProductOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ListProductsResponseOut"])
    types["GoogleCloudRetailV2alphaImportProductsResponseIn"] = t.struct(
        {
            "errorsConfig": t.proxy(
                renames["GoogleCloudRetailV2alphaImportErrorsConfigIn"]
            ).optional(),
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaImportProductsResponseIn"])
    types["GoogleCloudRetailV2alphaImportProductsResponseOut"] = t.struct(
        {
            "errorsConfig": t.proxy(
                renames["GoogleCloudRetailV2alphaImportErrorsConfigOut"]
            ).optional(),
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaImportProductsResponseOut"])
    types["GoogleCloudRetailV2betaImportMetadataIn"] = t.struct(
        {
            "successCount": t.string().optional(),
            "failureCount": t.string().optional(),
            "notificationPubsubTopic": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "requestId": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2betaImportMetadataIn"])
    types["GoogleCloudRetailV2betaImportMetadataOut"] = t.struct(
        {
            "successCount": t.string().optional(),
            "failureCount": t.string().optional(),
            "notificationPubsubTopic": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2betaImportMetadataOut"])
    types["GoogleCloudRetailV2AddControlRequestIn"] = t.struct(
        {"controlId": t.string()}
    ).named(renames["GoogleCloudRetailV2AddControlRequestIn"])
    types["GoogleCloudRetailV2AddControlRequestOut"] = t.struct(
        {"controlId": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2AddControlRequestOut"])
    types["GoogleCloudRetailV2AddLocalInventoriesMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2AddLocalInventoriesMetadataIn"])
    types["GoogleCloudRetailV2AddLocalInventoriesMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2AddLocalInventoriesMetadataOut"])
    types["GoogleCloudRetailV2ProductInputConfigIn"] = t.struct(
        {
            "gcsSource": t.proxy(renames["GoogleCloudRetailV2GcsSourceIn"]).optional(),
            "productInlineSource": t.proxy(
                renames["GoogleCloudRetailV2ProductInlineSourceIn"]
            ).optional(),
            "bigQuerySource": t.proxy(
                renames["GoogleCloudRetailV2BigQuerySourceIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ProductInputConfigIn"])
    types["GoogleCloudRetailV2ProductInputConfigOut"] = t.struct(
        {
            "gcsSource": t.proxy(renames["GoogleCloudRetailV2GcsSourceOut"]).optional(),
            "productInlineSource": t.proxy(
                renames["GoogleCloudRetailV2ProductInlineSourceOut"]
            ).optional(),
            "bigQuerySource": t.proxy(
                renames["GoogleCloudRetailV2BigQuerySourceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ProductInputConfigOut"])
    types["GoogleCloudRetailV2ImportCompletionDataResponseIn"] = t.struct(
        {"errorSamples": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional()}
    ).named(renames["GoogleCloudRetailV2ImportCompletionDataResponseIn"])
    types["GoogleCloudRetailV2ImportCompletionDataResponseOut"] = t.struct(
        {
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ImportCompletionDataResponseOut"])
    types["GoogleCloudRetailV2SearchResponseFacetFacetValueIn"] = t.struct(
        {
            "interval": t.proxy(renames["GoogleCloudRetailV2IntervalIn"]).optional(),
            "minValue": t.number().optional(),
            "count": t.string().optional(),
            "value": t.string().optional(),
            "maxValue": t.number().optional(),
        }
    ).named(renames["GoogleCloudRetailV2SearchResponseFacetFacetValueIn"])
    types["GoogleCloudRetailV2SearchResponseFacetFacetValueOut"] = t.struct(
        {
            "interval": t.proxy(renames["GoogleCloudRetailV2IntervalOut"]).optional(),
            "minValue": t.number().optional(),
            "count": t.string().optional(),
            "value": t.string().optional(),
            "maxValue": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2SearchResponseFacetFacetValueOut"])
    types["GoogleCloudRetailV2alphaModelPageOptimizationConfigCandidateIn"] = t.struct(
        {"servingConfigId": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2alphaModelPageOptimizationConfigCandidateIn"])
    types["GoogleCloudRetailV2alphaModelPageOptimizationConfigCandidateOut"] = t.struct(
        {
            "servingConfigId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaModelPageOptimizationConfigCandidateOut"])
    types["GoogleCloudRetailV2alphaOutputResultIn"] = t.struct(
        {
            "gcsResult": t.array(
                t.proxy(renames["GoogleCloudRetailV2alphaGcsOutputResultIn"])
            ).optional(),
            "bigqueryResult": t.array(
                t.proxy(renames["GoogleCloudRetailV2alphaBigQueryOutputResultIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaOutputResultIn"])
    types["GoogleCloudRetailV2alphaOutputResultOut"] = t.struct(
        {
            "gcsResult": t.array(
                t.proxy(renames["GoogleCloudRetailV2alphaGcsOutputResultOut"])
            ).optional(),
            "bigqueryResult": t.array(
                t.proxy(renames["GoogleCloudRetailV2alphaBigQueryOutputResultOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaOutputResultOut"])
    types["GoogleCloudRetailV2PriceInfoIn"] = t.struct(
        {
            "currencyCode": t.string().optional(),
            "price": t.number().optional(),
            "priceExpireTime": t.string().optional(),
            "cost": t.number().optional(),
            "originalPrice": t.number().optional(),
            "priceEffectiveTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2PriceInfoIn"])
    types["GoogleCloudRetailV2PriceInfoOut"] = t.struct(
        {
            "currencyCode": t.string().optional(),
            "price": t.number().optional(),
            "priceExpireTime": t.string().optional(),
            "cost": t.number().optional(),
            "originalPrice": t.number().optional(),
            "priceEffectiveTime": t.string().optional(),
            "priceRange": t.proxy(
                renames["GoogleCloudRetailV2PriceInfoPriceRangeOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2PriceInfoOut"])
    types["GoogleCloudRetailV2betaAddLocalInventoriesMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2betaAddLocalInventoriesMetadataIn"])
    types["GoogleCloudRetailV2betaAddLocalInventoriesMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2betaAddLocalInventoriesMetadataOut"])
    types["GoogleCloudRetailV2alphaModelIn"] = t.struct(
        {
            "optimizationObjective": t.string().optional(),
            "name": t.string(),
            "displayName": t.string(),
            "modelFeaturesConfig": t.proxy(
                renames["GoogleCloudRetailV2alphaModelModelFeaturesConfigIn"]
            ).optional(),
            "trainingState": t.string().optional(),
            "pageOptimizationConfig": t.proxy(
                renames["GoogleCloudRetailV2alphaModelPageOptimizationConfigIn"]
            ).optional(),
            "filteringOption": t.string().optional(),
            "type": t.string(),
            "periodicTuningState": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaModelIn"])
    types["GoogleCloudRetailV2alphaModelOut"] = t.struct(
        {
            "lastTuneTime": t.string().optional(),
            "optimizationObjective": t.string().optional(),
            "tuningOperation": t.string().optional(),
            "name": t.string(),
            "servingState": t.string().optional(),
            "displayName": t.string(),
            "servingConfigLists": t.array(
                t.proxy(renames["GoogleCloudRetailV2alphaModelServingConfigListOut"])
            ).optional(),
            "modelFeaturesConfig": t.proxy(
                renames["GoogleCloudRetailV2alphaModelModelFeaturesConfigOut"]
            ).optional(),
            "trainingState": t.string().optional(),
            "pageOptimizationConfig": t.proxy(
                renames["GoogleCloudRetailV2alphaModelPageOptimizationConfigOut"]
            ).optional(),
            "updateTime": t.string().optional(),
            "filteringOption": t.string().optional(),
            "createTime": t.string().optional(),
            "type": t.string(),
            "dataState": t.string().optional(),
            "periodicTuningState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaModelOut"])
    types["GoogleCloudRetailV2alphaRemoveLocalInventoriesMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2alphaRemoveLocalInventoriesMetadataIn"])
    types["GoogleCloudRetailV2alphaRemoveLocalInventoriesMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2alphaRemoveLocalInventoriesMetadataOut"])
    types["GoogleCloudRetailV2betaRejoinUserEventsMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2betaRejoinUserEventsMetadataIn"])
    types["GoogleCloudRetailV2betaRejoinUserEventsMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2betaRejoinUserEventsMetadataOut"])
    types["GoogleCloudRetailV2AddFulfillmentPlacesRequestIn"] = t.struct(
        {
            "placeIds": t.array(t.string()),
            "allowMissing": t.boolean().optional(),
            "type": t.string(),
            "addTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2AddFulfillmentPlacesRequestIn"])
    types["GoogleCloudRetailV2AddFulfillmentPlacesRequestOut"] = t.struct(
        {
            "placeIds": t.array(t.string()),
            "allowMissing": t.boolean().optional(),
            "type": t.string(),
            "addTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2AddFulfillmentPlacesRequestOut"])
    types["GoogleCloudRetailV2betaExportProductsResponseIn"] = t.struct(
        {
            "errorsConfig": t.proxy(
                renames["GoogleCloudRetailV2betaExportErrorsConfigIn"]
            ).optional(),
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional(),
            "outputResult": t.proxy(
                renames["GoogleCloudRetailV2betaOutputResultIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudRetailV2betaExportProductsResponseIn"])
    types["GoogleCloudRetailV2betaExportProductsResponseOut"] = t.struct(
        {
            "errorsConfig": t.proxy(
                renames["GoogleCloudRetailV2betaExportErrorsConfigOut"]
            ).optional(),
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "outputResult": t.proxy(
                renames["GoogleCloudRetailV2betaOutputResultOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2betaExportProductsResponseOut"])
    types["GoogleCloudRetailV2alphaSetInventoryMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2alphaSetInventoryMetadataIn"])
    types["GoogleCloudRetailV2alphaSetInventoryMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2alphaSetInventoryMetadataOut"])
    types["GoogleCloudRetailV2alphaCreateModelMetadataIn"] = t.struct(
        {"model": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2alphaCreateModelMetadataIn"])
    types["GoogleCloudRetailV2alphaCreateModelMetadataOut"] = t.struct(
        {
            "model": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaCreateModelMetadataOut"])
    types["GoogleCloudRetailLoggingErrorLogIn"] = t.struct(
        {
            "context": t.proxy(
                renames["GoogleCloudRetailLoggingErrorContextIn"]
            ).optional(),
            "serviceContext": t.proxy(
                renames["GoogleCloudRetailLoggingServiceContextIn"]
            ).optional(),
            "message": t.string().optional(),
            "responsePayload": t.struct({"_": t.string().optional()}).optional(),
            "status": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "requestPayload": t.struct({"_": t.string().optional()}).optional(),
            "importPayload": t.proxy(
                renames["GoogleCloudRetailLoggingImportErrorContextIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudRetailLoggingErrorLogIn"])
    types["GoogleCloudRetailLoggingErrorLogOut"] = t.struct(
        {
            "context": t.proxy(
                renames["GoogleCloudRetailLoggingErrorContextOut"]
            ).optional(),
            "serviceContext": t.proxy(
                renames["GoogleCloudRetailLoggingServiceContextOut"]
            ).optional(),
            "message": t.string().optional(),
            "responsePayload": t.struct({"_": t.string().optional()}).optional(),
            "status": t.proxy(renames["GoogleRpcStatusOut"]).optional(),
            "requestPayload": t.struct({"_": t.string().optional()}).optional(),
            "importPayload": t.proxy(
                renames["GoogleCloudRetailLoggingImportErrorContextOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailLoggingErrorLogOut"])
    types["GoogleCloudRetailV2IntervalIn"] = t.struct(
        {
            "minimum": t.number().optional(),
            "maximum": t.number().optional(),
            "exclusiveMinimum": t.number().optional(),
            "exclusiveMaximum": t.number().optional(),
        }
    ).named(renames["GoogleCloudRetailV2IntervalIn"])
    types["GoogleCloudRetailV2IntervalOut"] = t.struct(
        {
            "minimum": t.number().optional(),
            "maximum": t.number().optional(),
            "exclusiveMinimum": t.number().optional(),
            "exclusiveMaximum": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2IntervalOut"])
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
    types["GoogleCloudRetailV2alphaAddLocalInventoriesMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2alphaAddLocalInventoriesMetadataIn"])
    types["GoogleCloudRetailV2alphaAddLocalInventoriesMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2alphaAddLocalInventoriesMetadataOut"])
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
    types["GoogleRpcStatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["GoogleRpcStatusIn"])
    types["GoogleRpcStatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleRpcStatusOut"])
    types["GoogleCloudRetailV2betaImportProductsResponseIn"] = t.struct(
        {
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional(),
            "errorsConfig": t.proxy(
                renames["GoogleCloudRetailV2betaImportErrorsConfigIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudRetailV2betaImportProductsResponseIn"])
    types["GoogleCloudRetailV2betaImportProductsResponseOut"] = t.struct(
        {
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "errorsConfig": t.proxy(
                renames["GoogleCloudRetailV2betaImportErrorsConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2betaImportProductsResponseOut"])
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
    types["GoogleCloudRetailV2RemoveFulfillmentPlacesMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2RemoveFulfillmentPlacesMetadataIn"])
    types["GoogleCloudRetailV2RemoveFulfillmentPlacesMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2RemoveFulfillmentPlacesMetadataOut"])
    types["GoogleCloudRetailV2RuleRedirectActionIn"] = t.struct(
        {"redirectUri": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2RuleRedirectActionIn"])
    types["GoogleCloudRetailV2RuleRedirectActionOut"] = t.struct(
        {
            "redirectUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2RuleRedirectActionOut"])
    types["GoogleCloudRetailV2RuleIgnoreActionIn"] = t.struct(
        {"ignoreTerms": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudRetailV2RuleIgnoreActionIn"])
    types["GoogleCloudRetailV2RuleIgnoreActionOut"] = t.struct(
        {
            "ignoreTerms": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2RuleIgnoreActionOut"])
    types["GoogleCloudRetailV2CustomAttributeIn"] = t.struct(
        {
            "indexable": t.boolean().optional(),
            "text": t.array(t.string()).optional(),
            "searchable": t.boolean().optional(),
            "numbers": t.array(t.number()).optional(),
        }
    ).named(renames["GoogleCloudRetailV2CustomAttributeIn"])
    types["GoogleCloudRetailV2CustomAttributeOut"] = t.struct(
        {
            "indexable": t.boolean().optional(),
            "text": t.array(t.string()).optional(),
            "searchable": t.boolean().optional(),
            "numbers": t.array(t.number()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2CustomAttributeOut"])
    types["GoogleCloudRetailV2alphaTuneModelResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2alphaTuneModelResponseIn"])
    types["GoogleCloudRetailV2alphaTuneModelResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2alphaTuneModelResponseOut"])
    types["GoogleCloudRetailV2PriceInfoPriceRangeIn"] = t.struct(
        {
            "originalPrice": t.proxy(
                renames["GoogleCloudRetailV2IntervalIn"]
            ).optional(),
            "price": t.proxy(renames["GoogleCloudRetailV2IntervalIn"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2PriceInfoPriceRangeIn"])
    types["GoogleCloudRetailV2PriceInfoPriceRangeOut"] = t.struct(
        {
            "originalPrice": t.proxy(
                renames["GoogleCloudRetailV2IntervalOut"]
            ).optional(),
            "price": t.proxy(renames["GoogleCloudRetailV2IntervalOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2PriceInfoPriceRangeOut"])
    types["GoogleCloudRetailV2UserEventIn"] = t.struct(
        {
            "purchaseTransaction": t.proxy(
                renames["GoogleCloudRetailV2PurchaseTransactionIn"]
            ).optional(),
            "uri": t.string().optional(),
            "sessionId": t.string().optional(),
            "experimentIds": t.array(t.string()).optional(),
            "productDetails": t.array(
                t.proxy(renames["GoogleCloudRetailV2ProductDetailIn"])
            ).optional(),
            "pageCategories": t.array(t.string()).optional(),
            "cartId": t.string().optional(),
            "entity": t.string().optional(),
            "eventTime": t.string().optional(),
            "filter": t.string().optional(),
            "pageViewId": t.string().optional(),
            "eventType": t.string(),
            "visitorId": t.string(),
            "referrerUri": t.string().optional(),
            "completionDetail": t.proxy(
                renames["GoogleCloudRetailV2CompletionDetailIn"]
            ).optional(),
            "attributionToken": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "searchQuery": t.string().optional(),
            "orderBy": t.string().optional(),
            "userInfo": t.proxy(renames["GoogleCloudRetailV2UserInfoIn"]).optional(),
            "offset": t.integer().optional(),
        }
    ).named(renames["GoogleCloudRetailV2UserEventIn"])
    types["GoogleCloudRetailV2UserEventOut"] = t.struct(
        {
            "purchaseTransaction": t.proxy(
                renames["GoogleCloudRetailV2PurchaseTransactionOut"]
            ).optional(),
            "uri": t.string().optional(),
            "sessionId": t.string().optional(),
            "experimentIds": t.array(t.string()).optional(),
            "productDetails": t.array(
                t.proxy(renames["GoogleCloudRetailV2ProductDetailOut"])
            ).optional(),
            "pageCategories": t.array(t.string()).optional(),
            "cartId": t.string().optional(),
            "entity": t.string().optional(),
            "eventTime": t.string().optional(),
            "filter": t.string().optional(),
            "pageViewId": t.string().optional(),
            "eventType": t.string(),
            "visitorId": t.string(),
            "referrerUri": t.string().optional(),
            "completionDetail": t.proxy(
                renames["GoogleCloudRetailV2CompletionDetailOut"]
            ).optional(),
            "attributionToken": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "searchQuery": t.string().optional(),
            "orderBy": t.string().optional(),
            "userInfo": t.proxy(renames["GoogleCloudRetailV2UserInfoOut"]).optional(),
            "offset": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2UserEventOut"])
    types["GoogleCloudRetailLoggingServiceContextIn"] = t.struct(
        {"service": t.string().optional()}
    ).named(renames["GoogleCloudRetailLoggingServiceContextIn"])
    types["GoogleCloudRetailLoggingServiceContextOut"] = t.struct(
        {
            "service": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailLoggingServiceContextOut"])
    types["GoogleCloudRetailV2GcsSourceIn"] = t.struct(
        {"inputUris": t.array(t.string()), "dataSchema": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2GcsSourceIn"])
    types["GoogleCloudRetailV2GcsSourceOut"] = t.struct(
        {
            "inputUris": t.array(t.string()),
            "dataSchema": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2GcsSourceOut"])
    types["GoogleCloudRetailV2RuleDoNotAssociateActionIn"] = t.struct(
        {
            "terms": t.array(t.string()).optional(),
            "doNotAssociateTerms": t.array(t.string()).optional(),
            "queryTerms": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudRetailV2RuleDoNotAssociateActionIn"])
    types["GoogleCloudRetailV2RuleDoNotAssociateActionOut"] = t.struct(
        {
            "terms": t.array(t.string()).optional(),
            "doNotAssociateTerms": t.array(t.string()).optional(),
            "queryTerms": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2RuleDoNotAssociateActionOut"])
    types["GoogleCloudRetailV2betaImportCompletionDataResponseIn"] = t.struct(
        {"errorSamples": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional()}
    ).named(renames["GoogleCloudRetailV2betaImportCompletionDataResponseIn"])
    types["GoogleCloudRetailV2betaImportCompletionDataResponseOut"] = t.struct(
        {
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2betaImportCompletionDataResponseOut"])
    types["GoogleCloudRetailV2betaOutputResultIn"] = t.struct(
        {
            "gcsResult": t.array(
                t.proxy(renames["GoogleCloudRetailV2betaGcsOutputResultIn"])
            ).optional(),
            "bigqueryResult": t.array(
                t.proxy(renames["GoogleCloudRetailV2betaBigQueryOutputResultIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudRetailV2betaOutputResultIn"])
    types["GoogleCloudRetailV2betaOutputResultOut"] = t.struct(
        {
            "gcsResult": t.array(
                t.proxy(renames["GoogleCloudRetailV2betaGcsOutputResultOut"])
            ).optional(),
            "bigqueryResult": t.array(
                t.proxy(renames["GoogleCloudRetailV2betaBigQueryOutputResultOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2betaOutputResultOut"])
    types["GoogleCloudRetailV2PurchaseTransactionIn"] = t.struct(
        {
            "tax": t.number().optional(),
            "cost": t.number().optional(),
            "revenue": t.number(),
            "currencyCode": t.string(),
            "id": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2PurchaseTransactionIn"])
    types["GoogleCloudRetailV2PurchaseTransactionOut"] = t.struct(
        {
            "tax": t.number().optional(),
            "cost": t.number().optional(),
            "revenue": t.number(),
            "currencyCode": t.string(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2PurchaseTransactionOut"])
    types["GoogleCloudRetailV2RatingIn"] = t.struct(
        {
            "ratingCount": t.integer().optional(),
            "averageRating": t.number().optional(),
            "ratingHistogram": t.array(t.integer()).optional(),
        }
    ).named(renames["GoogleCloudRetailV2RatingIn"])
    types["GoogleCloudRetailV2RatingOut"] = t.struct(
        {
            "ratingCount": t.integer().optional(),
            "averageRating": t.number().optional(),
            "ratingHistogram": t.array(t.integer()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2RatingOut"])
    types["GoogleCloudRetailV2UserEventImportSummaryIn"] = t.struct(
        {
            "unjoinedEventsCount": t.string().optional(),
            "joinedEventsCount": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2UserEventImportSummaryIn"])
    types["GoogleCloudRetailV2UserEventImportSummaryOut"] = t.struct(
        {
            "unjoinedEventsCount": t.string().optional(),
            "joinedEventsCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2UserEventImportSummaryOut"])
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
    types["GoogleCloudRetailV2CompleteQueryResponseCompletionResultIn"] = t.struct(
        {
            "suggestion": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudRetailV2CompleteQueryResponseCompletionResultIn"])
    types["GoogleCloudRetailV2CompleteQueryResponseCompletionResultOut"] = t.struct(
        {
            "suggestion": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2CompleteQueryResponseCompletionResultOut"])
    types["GoogleCloudRetailV2ProductLevelConfigIn"] = t.struct(
        {
            "ingestionProductType": t.string().optional(),
            "merchantCenterProductIdField": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2ProductLevelConfigIn"])
    types["GoogleCloudRetailV2ProductLevelConfigOut"] = t.struct(
        {
            "ingestionProductType": t.string().optional(),
            "merchantCenterProductIdField": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ProductLevelConfigOut"])
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
    types["GoogleCloudRetailV2alphaBigQueryOutputResultIn"] = t.struct(
        {"datasetId": t.string().optional(), "tableId": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2alphaBigQueryOutputResultIn"])
    types["GoogleCloudRetailV2alphaBigQueryOutputResultOut"] = t.struct(
        {
            "datasetId": t.string().optional(),
            "tableId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaBigQueryOutputResultOut"])
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
    types["GoogleCloudRetailV2PurgeMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2PurgeMetadataIn"])
    types["GoogleCloudRetailV2PurgeMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2PurgeMetadataOut"])
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
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
    types["GoogleCloudRetailV2betaRejoinUserEventsResponseIn"] = t.struct(
        {"rejoinedUserEventsCount": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2betaRejoinUserEventsResponseIn"])
    types["GoogleCloudRetailV2betaRejoinUserEventsResponseOut"] = t.struct(
        {
            "rejoinedUserEventsCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2betaRejoinUserEventsResponseOut"])
    types["GoogleCloudRetailV2RuleTwowaySynonymsActionIn"] = t.struct(
        {"synonyms": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudRetailV2RuleTwowaySynonymsActionIn"])
    types["GoogleCloudRetailV2RuleTwowaySynonymsActionOut"] = t.struct(
        {
            "synonyms": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2RuleTwowaySynonymsActionOut"])
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
    types["GoogleCloudRetailV2BigQuerySourceIn"] = t.struct(
        {
            "dataSchema": t.string().optional(),
            "gcsStagingDir": t.string().optional(),
            "partitionDate": t.proxy(renames["GoogleTypeDateIn"]).optional(),
            "tableId": t.string(),
            "datasetId": t.string(),
            "projectId": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2BigQuerySourceIn"])
    types["GoogleCloudRetailV2BigQuerySourceOut"] = t.struct(
        {
            "dataSchema": t.string().optional(),
            "gcsStagingDir": t.string().optional(),
            "partitionDate": t.proxy(renames["GoogleTypeDateOut"]).optional(),
            "tableId": t.string(),
            "datasetId": t.string(),
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2BigQuerySourceOut"])
    types["GoogleCloudRetailV2ExperimentInfoIn"] = t.struct(
        {
            "experiment": t.string().optional(),
            "servingConfigExperiment": t.proxy(
                renames["GoogleCloudRetailV2ExperimentInfoServingConfigExperimentIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ExperimentInfoIn"])
    types["GoogleCloudRetailV2ExperimentInfoOut"] = t.struct(
        {
            "experiment": t.string().optional(),
            "servingConfigExperiment": t.proxy(
                renames["GoogleCloudRetailV2ExperimentInfoServingConfigExperimentOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ExperimentInfoOut"])
    types["GoogleCloudRetailV2ImportProductsRequestIn"] = t.struct(
        {
            "errorsConfig": t.proxy(
                renames["GoogleCloudRetailV2ImportErrorsConfigIn"]
            ).optional(),
            "reconciliationMode": t.string().optional(),
            "notificationPubsubTopic": t.string().optional(),
            "requestId": t.string().optional(),
            "inputConfig": t.proxy(renames["GoogleCloudRetailV2ProductInputConfigIn"]),
            "updateMask": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2ImportProductsRequestIn"])
    types["GoogleCloudRetailV2ImportProductsRequestOut"] = t.struct(
        {
            "errorsConfig": t.proxy(
                renames["GoogleCloudRetailV2ImportErrorsConfigOut"]
            ).optional(),
            "reconciliationMode": t.string().optional(),
            "notificationPubsubTopic": t.string().optional(),
            "requestId": t.string().optional(),
            "inputConfig": t.proxy(renames["GoogleCloudRetailV2ProductInputConfigOut"]),
            "updateMask": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2ImportProductsRequestOut"])
    types["GoogleCloudRetailV2betaCreateModelMetadataIn"] = t.struct(
        {"model": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2betaCreateModelMetadataIn"])
    types["GoogleCloudRetailV2betaCreateModelMetadataOut"] = t.struct(
        {
            "model": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2betaCreateModelMetadataOut"])
    types["GoogleCloudRetailV2betaPurgeMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2betaPurgeMetadataIn"])
    types["GoogleCloudRetailV2betaPurgeMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2betaPurgeMetadataOut"])
    types["GoogleCloudRetailLoggingHttpRequestContextIn"] = t.struct(
        {"responseStatusCode": t.integer().optional()}
    ).named(renames["GoogleCloudRetailLoggingHttpRequestContextIn"])
    types["GoogleCloudRetailLoggingHttpRequestContextOut"] = t.struct(
        {
            "responseStatusCode": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailLoggingHttpRequestContextOut"])
    types["GoogleCloudRetailV2betaRemoveLocalInventoriesResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2betaRemoveLocalInventoriesResponseIn"])
    types["GoogleCloudRetailV2betaRemoveLocalInventoriesResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2betaRemoveLocalInventoriesResponseOut"])
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
    types["GoogleCloudRetailV2alphaModelServingConfigListIn"] = t.struct(
        {"servingConfigIds": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudRetailV2alphaModelServingConfigListIn"])
    types["GoogleCloudRetailV2alphaModelServingConfigListOut"] = t.struct(
        {
            "servingConfigIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaModelServingConfigListOut"])
    types["GoogleCloudRetailV2alphaModelPageOptimizationConfigIn"] = t.struct(
        {
            "pageOptimizationEventType": t.string(),
            "restriction": t.string().optional(),
            "panels": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudRetailV2alphaModelPageOptimizationConfigPanelIn"
                    ]
                )
            ),
        }
    ).named(renames["GoogleCloudRetailV2alphaModelPageOptimizationConfigIn"])
    types["GoogleCloudRetailV2alphaModelPageOptimizationConfigOut"] = t.struct(
        {
            "pageOptimizationEventType": t.string(),
            "restriction": t.string().optional(),
            "panels": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudRetailV2alphaModelPageOptimizationConfigPanelOut"
                    ]
                )
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaModelPageOptimizationConfigOut"])
    types["GoogleCloudRetailV2alphaImportMetadataIn"] = t.struct(
        {
            "successCount": t.string().optional(),
            "transformedUserEventsMetadata": t.proxy(
                renames["GoogleCloudRetailV2alphaTransformedUserEventsMetadataIn"]
            ).optional(),
            "createTime": t.string().optional(),
            "failureCount": t.string().optional(),
            "notificationPubsubTopic": t.string().optional(),
            "requestId": t.string().optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaImportMetadataIn"])
    types["GoogleCloudRetailV2alphaImportMetadataOut"] = t.struct(
        {
            "successCount": t.string().optional(),
            "transformedUserEventsMetadata": t.proxy(
                renames["GoogleCloudRetailV2alphaTransformedUserEventsMetadataOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "failureCount": t.string().optional(),
            "notificationPubsubTopic": t.string().optional(),
            "requestId": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaImportMetadataOut"])
    types["GoogleCloudRetailV2alphaExportErrorsConfigIn"] = t.struct(
        {"gcsPrefix": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2alphaExportErrorsConfigIn"])
    types["GoogleCloudRetailV2alphaExportErrorsConfigOut"] = t.struct(
        {
            "gcsPrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2alphaExportErrorsConfigOut"])
    types["GoogleCloudRetailV2RuleIn"] = t.struct(
        {
            "replacementAction": t.proxy(
                renames["GoogleCloudRetailV2RuleReplacementActionIn"]
            ).optional(),
            "onewaySynonymsAction": t.proxy(
                renames["GoogleCloudRetailV2RuleOnewaySynonymsActionIn"]
            ).optional(),
            "boostAction": t.proxy(
                renames["GoogleCloudRetailV2RuleBoostActionIn"]
            ).optional(),
            "ignoreAction": t.proxy(
                renames["GoogleCloudRetailV2RuleIgnoreActionIn"]
            ).optional(),
            "redirectAction": t.proxy(
                renames["GoogleCloudRetailV2RuleRedirectActionIn"]
            ).optional(),
            "doNotAssociateAction": t.proxy(
                renames["GoogleCloudRetailV2RuleDoNotAssociateActionIn"]
            ).optional(),
            "condition": t.proxy(renames["GoogleCloudRetailV2ConditionIn"]),
            "filterAction": t.proxy(
                renames["GoogleCloudRetailV2RuleFilterActionIn"]
            ).optional(),
            "twowaySynonymsAction": t.proxy(
                renames["GoogleCloudRetailV2RuleTwowaySynonymsActionIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudRetailV2RuleIn"])
    types["GoogleCloudRetailV2RuleOut"] = t.struct(
        {
            "replacementAction": t.proxy(
                renames["GoogleCloudRetailV2RuleReplacementActionOut"]
            ).optional(),
            "onewaySynonymsAction": t.proxy(
                renames["GoogleCloudRetailV2RuleOnewaySynonymsActionOut"]
            ).optional(),
            "boostAction": t.proxy(
                renames["GoogleCloudRetailV2RuleBoostActionOut"]
            ).optional(),
            "ignoreAction": t.proxy(
                renames["GoogleCloudRetailV2RuleIgnoreActionOut"]
            ).optional(),
            "redirectAction": t.proxy(
                renames["GoogleCloudRetailV2RuleRedirectActionOut"]
            ).optional(),
            "doNotAssociateAction": t.proxy(
                renames["GoogleCloudRetailV2RuleDoNotAssociateActionOut"]
            ).optional(),
            "condition": t.proxy(renames["GoogleCloudRetailV2ConditionOut"]),
            "filterAction": t.proxy(
                renames["GoogleCloudRetailV2RuleFilterActionOut"]
            ).optional(),
            "twowaySynonymsAction": t.proxy(
                renames["GoogleCloudRetailV2RuleTwowaySynonymsActionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2RuleOut"])
    types["GoogleCloudRetailV2SearchRequestFacetSpecIn"] = t.struct(
        {
            "excludedFilterKeys": t.array(t.string()).optional(),
            "enableDynamicPosition": t.boolean().optional(),
            "limit": t.integer().optional(),
            "facetKey": t.proxy(
                renames["GoogleCloudRetailV2SearchRequestFacetSpecFacetKeyIn"]
            ),
        }
    ).named(renames["GoogleCloudRetailV2SearchRequestFacetSpecIn"])
    types["GoogleCloudRetailV2SearchRequestFacetSpecOut"] = t.struct(
        {
            "excludedFilterKeys": t.array(t.string()).optional(),
            "enableDynamicPosition": t.boolean().optional(),
            "limit": t.integer().optional(),
            "facetKey": t.proxy(
                renames["GoogleCloudRetailV2SearchRequestFacetSpecFacetKeyOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2SearchRequestFacetSpecOut"])
    types["GoogleCloudRetailV2RuleFilterActionIn"] = t.struct(
        {"filter": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2RuleFilterActionIn"])
    types["GoogleCloudRetailV2RuleFilterActionOut"] = t.struct(
        {
            "filter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2RuleFilterActionOut"])
    types["GoogleCloudRetailV2PurgeUserEventsRequestIn"] = t.struct(
        {"force": t.boolean().optional(), "filter": t.string()}
    ).named(renames["GoogleCloudRetailV2PurgeUserEventsRequestIn"])
    types["GoogleCloudRetailV2PurgeUserEventsRequestOut"] = t.struct(
        {
            "force": t.boolean().optional(),
            "filter": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2PurgeUserEventsRequestOut"])
    types["GoogleCloudRetailV2SearchRequestSpellCorrectionSpecIn"] = t.struct(
        {"mode": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2SearchRequestSpellCorrectionSpecIn"])
    types["GoogleCloudRetailV2SearchRequestSpellCorrectionSpecOut"] = t.struct(
        {
            "mode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2SearchRequestSpellCorrectionSpecOut"])
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
    types["GoogleCloudRetailV2SearchRequestBoostSpecConditionBoostSpecIn"] = t.struct(
        {"condition": t.string().optional(), "boost": t.number().optional()}
    ).named(renames["GoogleCloudRetailV2SearchRequestBoostSpecConditionBoostSpecIn"])
    types["GoogleCloudRetailV2SearchRequestBoostSpecConditionBoostSpecOut"] = t.struct(
        {
            "condition": t.string().optional(),
            "boost": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2SearchRequestBoostSpecConditionBoostSpecOut"])
    types["GoogleCloudRetailV2SearchRequestDynamicFacetSpecIn"] = t.struct(
        {"mode": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2SearchRequestDynamicFacetSpecIn"])
    types["GoogleCloudRetailV2SearchRequestDynamicFacetSpecOut"] = t.struct(
        {
            "mode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2SearchRequestDynamicFacetSpecOut"])
    types["GoogleCloudRetailV2alphaRemoveFulfillmentPlacesMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2alphaRemoveFulfillmentPlacesMetadataIn"])
    types["GoogleCloudRetailV2alphaRemoveFulfillmentPlacesMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2alphaRemoveFulfillmentPlacesMetadataOut"])
    types["GoogleCloudRetailV2SearchRequestPersonalizationSpecIn"] = t.struct(
        {"mode": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2SearchRequestPersonalizationSpecIn"])
    types["GoogleCloudRetailV2SearchRequestPersonalizationSpecOut"] = t.struct(
        {
            "mode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2SearchRequestPersonalizationSpecOut"])
    types["GoogleCloudRetailV2betaRemoveFulfillmentPlacesMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2betaRemoveFulfillmentPlacesMetadataIn"])
    types["GoogleCloudRetailV2betaRemoveFulfillmentPlacesMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRetailV2betaRemoveFulfillmentPlacesMetadataOut"])
    types["GoogleCloudRetailV2PromotionIn"] = t.struct(
        {"promotionId": t.string().optional()}
    ).named(renames["GoogleCloudRetailV2PromotionIn"])
    types["GoogleCloudRetailV2PromotionOut"] = t.struct(
        {
            "promotionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2PromotionOut"])
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
    types["GoogleCloudRetailV2betaMerchantCenterAccountLinkIn"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "feedLabel": t.string().optional(),
            "branchId": t.string(),
            "merchantCenterAccountId": t.string(),
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
            "projectId": t.string().optional(),
            "name": t.string().optional(),
            "languageCode": t.string().optional(),
            "feedLabel": t.string().optional(),
            "branchId": t.string(),
            "merchantCenterAccountId": t.string(),
            "feedFilters": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudRetailV2betaMerchantCenterAccountLinkMerchantCenterFeedFilterOut"
                    ]
                )
            ).optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRetailV2betaMerchantCenterAccountLinkOut"])
    types["GoogleApiHttpBodyIn"] = t.struct(
        {
            "contentType": t.string().optional(),
            "data": t.string().optional(),
            "extensions": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["GoogleApiHttpBodyIn"])
    types["GoogleApiHttpBodyOut"] = t.struct(
        {
            "contentType": t.string().optional(),
            "data": t.string().optional(),
            "extensions": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleApiHttpBodyOut"])
    types["GoogleCloudRetailV2betaExportUserEventsResponseIn"] = t.struct(
        {
            "outputResult": t.proxy(
                renames["GoogleCloudRetailV2betaOutputResultIn"]
            ).optional(),
            "errorSamples": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional(),
            "errorsConfig": t.proxy(
                renames["GoogleCloudRetailV2betaExportErrorsConfigIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudRetailV2betaExportUserEventsResponseIn"])
    types["GoogleCloudRetailV2betaExportUserEventsResponseOut"] = t.struct(
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
    ).named(renames["GoogleCloudRetailV2betaExportUserEventsResponseOut"])
    types[
        "GoogleCloudRetailV2alphaCreateMerchantCenterAccountLinkMetadataIn"
    ] = t.struct(
        {"createTime": t.string().optional(), "updateTime": t.string().optional()}
    ).named(
        renames["GoogleCloudRetailV2alphaCreateMerchantCenterAccountLinkMetadataIn"]
    )
    types[
        "GoogleCloudRetailV2alphaCreateMerchantCenterAccountLinkMetadataOut"
    ] = t.struct(
        {
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudRetailV2alphaCreateMerchantCenterAccountLinkMetadataOut"]
    )

    functions = {}
    functions["projectsOperationsGet"] = retail.get(
        "v2/{name}/operations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOperationsList"] = retail.get(
        "v2/{name}/operations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
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
    functions["projectsLocationsCatalogsGetCompletionConfig"] = retail.get(
        "v2/{catalog}:getDefaultBranch",
        t.struct({"catalog": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRetailV2GetDefaultBranchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsUpdateCompletionConfig"] = retail.get(
        "v2/{catalog}:getDefaultBranch",
        t.struct({"catalog": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRetailV2GetDefaultBranchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsPatch"] = retail.get(
        "v2/{catalog}:getDefaultBranch",
        t.struct({"catalog": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRetailV2GetDefaultBranchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsUpdateAttributesConfig"] = retail.get(
        "v2/{catalog}:getDefaultBranch",
        t.struct({"catalog": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRetailV2GetDefaultBranchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsSetDefaultBranch"] = retail.get(
        "v2/{catalog}:getDefaultBranch",
        t.struct({"catalog": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRetailV2GetDefaultBranchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsList"] = retail.get(
        "v2/{catalog}:getDefaultBranch",
        t.struct({"catalog": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRetailV2GetDefaultBranchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsGetAttributesConfig"] = retail.get(
        "v2/{catalog}:getDefaultBranch",
        t.struct({"catalog": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRetailV2GetDefaultBranchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsCompleteQuery"] = retail.get(
        "v2/{catalog}:getDefaultBranch",
        t.struct({"catalog": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRetailV2GetDefaultBranchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsGetDefaultBranch"] = retail.get(
        "v2/{catalog}:getDefaultBranch",
        t.struct({"catalog": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRetailV2GetDefaultBranchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsServingConfigsDelete"] = retail.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "ignoreControlIds": t.array(t.string()).optional(),
                "dynamicFacetSpec": t.proxy(
                    renames["GoogleCloudRetailV2SearchRequestDynamicFacetSpecIn"]
                ).optional(),
                "diversityLevel": t.string().optional(),
                "onewaySynonymsControlIds": t.array(t.string()).optional(),
                "modelId": t.string().optional(),
                "boostControlIds": t.array(t.string()).optional(),
                "diversityType": t.string().optional(),
                "filterControlIds": t.array(t.string()).optional(),
                "enableCategoryFilterLevel": t.string().optional(),
                "doNotAssociateControlIds": t.array(t.string()).optional(),
                "twowaySynonymsControlIds": t.array(t.string()).optional(),
                "displayName": t.string(),
                "redirectControlIds": t.array(t.string()).optional(),
                "replacementControlIds": t.array(t.string()).optional(),
                "priceRerankingLevel": t.string().optional(),
                "facetControlIds": t.array(t.string()).optional(),
                "solutionTypes": t.array(t.string()),
                "personalizationSpec": t.proxy(
                    renames["GoogleCloudRetailV2SearchRequestPersonalizationSpecIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRetailV2ServingConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsServingConfigsRemoveControl"] = retail.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "ignoreControlIds": t.array(t.string()).optional(),
                "dynamicFacetSpec": t.proxy(
                    renames["GoogleCloudRetailV2SearchRequestDynamicFacetSpecIn"]
                ).optional(),
                "diversityLevel": t.string().optional(),
                "onewaySynonymsControlIds": t.array(t.string()).optional(),
                "modelId": t.string().optional(),
                "boostControlIds": t.array(t.string()).optional(),
                "diversityType": t.string().optional(),
                "filterControlIds": t.array(t.string()).optional(),
                "enableCategoryFilterLevel": t.string().optional(),
                "doNotAssociateControlIds": t.array(t.string()).optional(),
                "twowaySynonymsControlIds": t.array(t.string()).optional(),
                "displayName": t.string(),
                "redirectControlIds": t.array(t.string()).optional(),
                "replacementControlIds": t.array(t.string()).optional(),
                "priceRerankingLevel": t.string().optional(),
                "facetControlIds": t.array(t.string()).optional(),
                "solutionTypes": t.array(t.string()),
                "personalizationSpec": t.proxy(
                    renames["GoogleCloudRetailV2SearchRequestPersonalizationSpecIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRetailV2ServingConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsServingConfigsAddControl"] = retail.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "ignoreControlIds": t.array(t.string()).optional(),
                "dynamicFacetSpec": t.proxy(
                    renames["GoogleCloudRetailV2SearchRequestDynamicFacetSpecIn"]
                ).optional(),
                "diversityLevel": t.string().optional(),
                "onewaySynonymsControlIds": t.array(t.string()).optional(),
                "modelId": t.string().optional(),
                "boostControlIds": t.array(t.string()).optional(),
                "diversityType": t.string().optional(),
                "filterControlIds": t.array(t.string()).optional(),
                "enableCategoryFilterLevel": t.string().optional(),
                "doNotAssociateControlIds": t.array(t.string()).optional(),
                "twowaySynonymsControlIds": t.array(t.string()).optional(),
                "displayName": t.string(),
                "redirectControlIds": t.array(t.string()).optional(),
                "replacementControlIds": t.array(t.string()).optional(),
                "priceRerankingLevel": t.string().optional(),
                "facetControlIds": t.array(t.string()).optional(),
                "solutionTypes": t.array(t.string()),
                "personalizationSpec": t.proxy(
                    renames["GoogleCloudRetailV2SearchRequestPersonalizationSpecIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRetailV2ServingConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsServingConfigsPredict"] = retail.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "ignoreControlIds": t.array(t.string()).optional(),
                "dynamicFacetSpec": t.proxy(
                    renames["GoogleCloudRetailV2SearchRequestDynamicFacetSpecIn"]
                ).optional(),
                "diversityLevel": t.string().optional(),
                "onewaySynonymsControlIds": t.array(t.string()).optional(),
                "modelId": t.string().optional(),
                "boostControlIds": t.array(t.string()).optional(),
                "diversityType": t.string().optional(),
                "filterControlIds": t.array(t.string()).optional(),
                "enableCategoryFilterLevel": t.string().optional(),
                "doNotAssociateControlIds": t.array(t.string()).optional(),
                "twowaySynonymsControlIds": t.array(t.string()).optional(),
                "displayName": t.string(),
                "redirectControlIds": t.array(t.string()).optional(),
                "replacementControlIds": t.array(t.string()).optional(),
                "priceRerankingLevel": t.string().optional(),
                "facetControlIds": t.array(t.string()).optional(),
                "solutionTypes": t.array(t.string()),
                "personalizationSpec": t.proxy(
                    renames["GoogleCloudRetailV2SearchRequestPersonalizationSpecIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRetailV2ServingConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsServingConfigsGet"] = retail.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "ignoreControlIds": t.array(t.string()).optional(),
                "dynamicFacetSpec": t.proxy(
                    renames["GoogleCloudRetailV2SearchRequestDynamicFacetSpecIn"]
                ).optional(),
                "diversityLevel": t.string().optional(),
                "onewaySynonymsControlIds": t.array(t.string()).optional(),
                "modelId": t.string().optional(),
                "boostControlIds": t.array(t.string()).optional(),
                "diversityType": t.string().optional(),
                "filterControlIds": t.array(t.string()).optional(),
                "enableCategoryFilterLevel": t.string().optional(),
                "doNotAssociateControlIds": t.array(t.string()).optional(),
                "twowaySynonymsControlIds": t.array(t.string()).optional(),
                "displayName": t.string(),
                "redirectControlIds": t.array(t.string()).optional(),
                "replacementControlIds": t.array(t.string()).optional(),
                "priceRerankingLevel": t.string().optional(),
                "facetControlIds": t.array(t.string()).optional(),
                "solutionTypes": t.array(t.string()),
                "personalizationSpec": t.proxy(
                    renames["GoogleCloudRetailV2SearchRequestPersonalizationSpecIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRetailV2ServingConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsServingConfigsCreate"] = retail.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "ignoreControlIds": t.array(t.string()).optional(),
                "dynamicFacetSpec": t.proxy(
                    renames["GoogleCloudRetailV2SearchRequestDynamicFacetSpecIn"]
                ).optional(),
                "diversityLevel": t.string().optional(),
                "onewaySynonymsControlIds": t.array(t.string()).optional(),
                "modelId": t.string().optional(),
                "boostControlIds": t.array(t.string()).optional(),
                "diversityType": t.string().optional(),
                "filterControlIds": t.array(t.string()).optional(),
                "enableCategoryFilterLevel": t.string().optional(),
                "doNotAssociateControlIds": t.array(t.string()).optional(),
                "twowaySynonymsControlIds": t.array(t.string()).optional(),
                "displayName": t.string(),
                "redirectControlIds": t.array(t.string()).optional(),
                "replacementControlIds": t.array(t.string()).optional(),
                "priceRerankingLevel": t.string().optional(),
                "facetControlIds": t.array(t.string()).optional(),
                "solutionTypes": t.array(t.string()),
                "personalizationSpec": t.proxy(
                    renames["GoogleCloudRetailV2SearchRequestPersonalizationSpecIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRetailV2ServingConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsServingConfigsSearch"] = retail.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "ignoreControlIds": t.array(t.string()).optional(),
                "dynamicFacetSpec": t.proxy(
                    renames["GoogleCloudRetailV2SearchRequestDynamicFacetSpecIn"]
                ).optional(),
                "diversityLevel": t.string().optional(),
                "onewaySynonymsControlIds": t.array(t.string()).optional(),
                "modelId": t.string().optional(),
                "boostControlIds": t.array(t.string()).optional(),
                "diversityType": t.string().optional(),
                "filterControlIds": t.array(t.string()).optional(),
                "enableCategoryFilterLevel": t.string().optional(),
                "doNotAssociateControlIds": t.array(t.string()).optional(),
                "twowaySynonymsControlIds": t.array(t.string()).optional(),
                "displayName": t.string(),
                "redirectControlIds": t.array(t.string()).optional(),
                "replacementControlIds": t.array(t.string()).optional(),
                "priceRerankingLevel": t.string().optional(),
                "facetControlIds": t.array(t.string()).optional(),
                "solutionTypes": t.array(t.string()),
                "personalizationSpec": t.proxy(
                    renames["GoogleCloudRetailV2SearchRequestPersonalizationSpecIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRetailV2ServingConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsServingConfigsList"] = retail.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "ignoreControlIds": t.array(t.string()).optional(),
                "dynamicFacetSpec": t.proxy(
                    renames["GoogleCloudRetailV2SearchRequestDynamicFacetSpecIn"]
                ).optional(),
                "diversityLevel": t.string().optional(),
                "onewaySynonymsControlIds": t.array(t.string()).optional(),
                "modelId": t.string().optional(),
                "boostControlIds": t.array(t.string()).optional(),
                "diversityType": t.string().optional(),
                "filterControlIds": t.array(t.string()).optional(),
                "enableCategoryFilterLevel": t.string().optional(),
                "doNotAssociateControlIds": t.array(t.string()).optional(),
                "twowaySynonymsControlIds": t.array(t.string()).optional(),
                "displayName": t.string(),
                "redirectControlIds": t.array(t.string()).optional(),
                "replacementControlIds": t.array(t.string()).optional(),
                "priceRerankingLevel": t.string().optional(),
                "facetControlIds": t.array(t.string()).optional(),
                "solutionTypes": t.array(t.string()),
                "personalizationSpec": t.proxy(
                    renames["GoogleCloudRetailV2SearchRequestPersonalizationSpecIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRetailV2ServingConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsServingConfigsPatch"] = retail.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "ignoreControlIds": t.array(t.string()).optional(),
                "dynamicFacetSpec": t.proxy(
                    renames["GoogleCloudRetailV2SearchRequestDynamicFacetSpecIn"]
                ).optional(),
                "diversityLevel": t.string().optional(),
                "onewaySynonymsControlIds": t.array(t.string()).optional(),
                "modelId": t.string().optional(),
                "boostControlIds": t.array(t.string()).optional(),
                "diversityType": t.string().optional(),
                "filterControlIds": t.array(t.string()).optional(),
                "enableCategoryFilterLevel": t.string().optional(),
                "doNotAssociateControlIds": t.array(t.string()).optional(),
                "twowaySynonymsControlIds": t.array(t.string()).optional(),
                "displayName": t.string(),
                "redirectControlIds": t.array(t.string()).optional(),
                "replacementControlIds": t.array(t.string()).optional(),
                "priceRerankingLevel": t.string().optional(),
                "facetControlIds": t.array(t.string()).optional(),
                "solutionTypes": t.array(t.string()),
                "personalizationSpec": t.proxy(
                    renames["GoogleCloudRetailV2SearchRequestPersonalizationSpecIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRetailV2ServingConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsUserEventsRejoin"] = retail.post(
        "v2/{parent}/userEvents:import",
        t.struct(
            {
                "parent": t.string(),
                "errorsConfig": t.proxy(
                    renames["GoogleCloudRetailV2ImportErrorsConfigIn"]
                ).optional(),
                "inputConfig": t.proxy(
                    renames["GoogleCloudRetailV2UserEventInputConfigIn"]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsUserEventsWrite"] = retail.post(
        "v2/{parent}/userEvents:import",
        t.struct(
            {
                "parent": t.string(),
                "errorsConfig": t.proxy(
                    renames["GoogleCloudRetailV2ImportErrorsConfigIn"]
                ).optional(),
                "inputConfig": t.proxy(
                    renames["GoogleCloudRetailV2UserEventInputConfigIn"]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsUserEventsCollect"] = retail.post(
        "v2/{parent}/userEvents:import",
        t.struct(
            {
                "parent": t.string(),
                "errorsConfig": t.proxy(
                    renames["GoogleCloudRetailV2ImportErrorsConfigIn"]
                ).optional(),
                "inputConfig": t.proxy(
                    renames["GoogleCloudRetailV2UserEventInputConfigIn"]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsUserEventsPurge"] = retail.post(
        "v2/{parent}/userEvents:import",
        t.struct(
            {
                "parent": t.string(),
                "errorsConfig": t.proxy(
                    renames["GoogleCloudRetailV2ImportErrorsConfigIn"]
                ).optional(),
                "inputConfig": t.proxy(
                    renames["GoogleCloudRetailV2UserEventInputConfigIn"]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsUserEventsImport"] = retail.post(
        "v2/{parent}/userEvents:import",
        t.struct(
            {
                "parent": t.string(),
                "errorsConfig": t.proxy(
                    renames["GoogleCloudRetailV2ImportErrorsConfigIn"]
                ).optional(),
                "inputConfig": t.proxy(
                    renames["GoogleCloudRetailV2UserEventInputConfigIn"]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsModelsGet"] = retail.get(
        "v2/{parent}/models",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRetailV2ListModelsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsModelsPause"] = retail.get(
        "v2/{parent}/models",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRetailV2ListModelsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsModelsDelete"] = retail.get(
        "v2/{parent}/models",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRetailV2ListModelsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsModelsCreate"] = retail.get(
        "v2/{parent}/models",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRetailV2ListModelsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsModelsPatch"] = retail.get(
        "v2/{parent}/models",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRetailV2ListModelsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsModelsTune"] = retail.get(
        "v2/{parent}/models",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRetailV2ListModelsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsModelsResume"] = retail.get(
        "v2/{parent}/models",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRetailV2ListModelsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsModelsList"] = retail.get(
        "v2/{parent}/models",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRetailV2ListModelsResponseOut"]),
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
    functions["projectsLocationsCatalogsControlsList"] = retail.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsControlsPatch"] = retail.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsControlsCreate"] = retail.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsControlsGet"] = retail.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsControlsDelete"] = retail.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsPlacementsPredict"] = retail.post(
        "v2/{placement}:search",
        t.struct(
            {
                "placement": t.string(),
                "pageToken": t.string().optional(),
                "variantRollupKeys": t.array(t.string()).optional(),
                "canonicalFilter": t.string().optional(),
                "offset": t.integer().optional(),
                "pageSize": t.integer().optional(),
                "spellCorrectionSpec": t.proxy(
                    renames["GoogleCloudRetailV2SearchRequestSpellCorrectionSpecIn"]
                ).optional(),
                "visitorId": t.string(),
                "dynamicFacetSpec": t.proxy(
                    renames["GoogleCloudRetailV2SearchRequestDynamicFacetSpecIn"]
                ).optional(),
                "orderBy": t.string().optional(),
                "userInfo": t.proxy(
                    renames["GoogleCloudRetailV2UserInfoIn"]
                ).optional(),
                "entity": t.string().optional(),
                "branch": t.string().optional(),
                "personalizationSpec": t.proxy(
                    renames["GoogleCloudRetailV2SearchRequestPersonalizationSpecIn"]
                ).optional(),
                "pageCategories": t.array(t.string()).optional(),
                "facetSpecs": t.array(
                    t.proxy(renames["GoogleCloudRetailV2SearchRequestFacetSpecIn"])
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "boostSpec": t.proxy(
                    renames["GoogleCloudRetailV2SearchRequestBoostSpecIn"]
                ).optional(),
                "filter": t.string().optional(),
                "searchMode": t.string().optional(),
                "query": t.string().optional(),
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
                "variantRollupKeys": t.array(t.string()).optional(),
                "canonicalFilter": t.string().optional(),
                "offset": t.integer().optional(),
                "pageSize": t.integer().optional(),
                "spellCorrectionSpec": t.proxy(
                    renames["GoogleCloudRetailV2SearchRequestSpellCorrectionSpecIn"]
                ).optional(),
                "visitorId": t.string(),
                "dynamicFacetSpec": t.proxy(
                    renames["GoogleCloudRetailV2SearchRequestDynamicFacetSpecIn"]
                ).optional(),
                "orderBy": t.string().optional(),
                "userInfo": t.proxy(
                    renames["GoogleCloudRetailV2UserInfoIn"]
                ).optional(),
                "entity": t.string().optional(),
                "branch": t.string().optional(),
                "personalizationSpec": t.proxy(
                    renames["GoogleCloudRetailV2SearchRequestPersonalizationSpecIn"]
                ).optional(),
                "pageCategories": t.array(t.string()).optional(),
                "facetSpecs": t.array(
                    t.proxy(renames["GoogleCloudRetailV2SearchRequestFacetSpecIn"])
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "boostSpec": t.proxy(
                    renames["GoogleCloudRetailV2SearchRequestBoostSpecIn"]
                ).optional(),
                "filter": t.string().optional(),
                "searchMode": t.string().optional(),
                "query": t.string().optional(),
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
    functions[
        "projectsLocationsCatalogsAttributesConfigReplaceCatalogAttribute"
    ] = retail.post(
        "v2/{attributesConfig}:addCatalogAttribute",
        t.struct(
            {
                "attributesConfig": t.string(),
                "catalogAttribute": t.proxy(
                    renames["GoogleCloudRetailV2CatalogAttributeIn"]
                ),
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
        "v2/{attributesConfig}:addCatalogAttribute",
        t.struct(
            {
                "attributesConfig": t.string(),
                "catalogAttribute": t.proxy(
                    renames["GoogleCloudRetailV2CatalogAttributeIn"]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRetailV2AttributesConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsCatalogsAttributesConfigAddCatalogAttribute"
    ] = retail.post(
        "v2/{attributesConfig}:addCatalogAttribute",
        t.struct(
            {
                "attributesConfig": t.string(),
                "catalogAttribute": t.proxy(
                    renames["GoogleCloudRetailV2CatalogAttributeIn"]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRetailV2AttributesConfigOut"]),
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
    functions["projectsLocationsCatalogsBranchesProductsPatch"] = retail.post(
        "v2/{product}:addFulfillmentPlaces",
        t.struct(
            {
                "product": t.string(),
                "placeIds": t.array(t.string()),
                "allowMissing": t.boolean().optional(),
                "type": t.string(),
                "addTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsBranchesProductsList"] = retail.post(
        "v2/{product}:addFulfillmentPlaces",
        t.struct(
            {
                "product": t.string(),
                "placeIds": t.array(t.string()),
                "allowMissing": t.boolean().optional(),
                "type": t.string(),
                "addTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsBranchesProductsDelete"] = retail.post(
        "v2/{product}:addFulfillmentPlaces",
        t.struct(
            {
                "product": t.string(),
                "placeIds": t.array(t.string()),
                "allowMissing": t.boolean().optional(),
                "type": t.string(),
                "addTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsBranchesProductsSetInventory"] = retail.post(
        "v2/{product}:addFulfillmentPlaces",
        t.struct(
            {
                "product": t.string(),
                "placeIds": t.array(t.string()),
                "allowMissing": t.boolean().optional(),
                "type": t.string(),
                "addTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsBranchesProductsImport"] = retail.post(
        "v2/{product}:addFulfillmentPlaces",
        t.struct(
            {
                "product": t.string(),
                "placeIds": t.array(t.string()),
                "allowMissing": t.boolean().optional(),
                "type": t.string(),
                "addTime": t.string().optional(),
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
        "v2/{product}:addFulfillmentPlaces",
        t.struct(
            {
                "product": t.string(),
                "placeIds": t.array(t.string()),
                "allowMissing": t.boolean().optional(),
                "type": t.string(),
                "addTime": t.string().optional(),
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
        "v2/{product}:addFulfillmentPlaces",
        t.struct(
            {
                "product": t.string(),
                "placeIds": t.array(t.string()),
                "allowMissing": t.boolean().optional(),
                "type": t.string(),
                "addTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsBranchesProductsGet"] = retail.post(
        "v2/{product}:addFulfillmentPlaces",
        t.struct(
            {
                "product": t.string(),
                "placeIds": t.array(t.string()),
                "allowMissing": t.boolean().optional(),
                "type": t.string(),
                "addTime": t.string().optional(),
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
        "v2/{product}:addFulfillmentPlaces",
        t.struct(
            {
                "product": t.string(),
                "placeIds": t.array(t.string()),
                "allowMissing": t.boolean().optional(),
                "type": t.string(),
                "addTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCatalogsBranchesProductsCreate"] = retail.post(
        "v2/{product}:addFulfillmentPlaces",
        t.struct(
            {
                "product": t.string(),
                "placeIds": t.array(t.string()),
                "allowMissing": t.boolean().optional(),
                "type": t.string(),
                "addTime": t.string().optional(),
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
        "v2/{product}:addFulfillmentPlaces",
        t.struct(
            {
                "product": t.string(),
                "placeIds": t.array(t.string()),
                "allowMissing": t.boolean().optional(),
                "type": t.string(),
                "addTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(importer="retail", renames=renames, types=types, functions=functions)
