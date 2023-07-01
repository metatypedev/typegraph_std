from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_androidpublisher():
    androidpublisher = HTTPRuntime("https://androidpublisher.googleapis.com/")

    renames = {
        "ErrorResponse": "_androidpublisher_1_ErrorResponse",
        "InappproductsListResponseIn": "_androidpublisher_2_InappproductsListResponseIn",
        "InappproductsListResponseOut": "_androidpublisher_3_InappproductsListResponseOut",
        "ModuleMetadataIn": "_androidpublisher_4_ModuleMetadataIn",
        "ModuleMetadataOut": "_androidpublisher_5_ModuleMetadataOut",
        "ListSubscriptionOffersResponseIn": "_androidpublisher_6_ListSubscriptionOffersResponseIn",
        "ListSubscriptionOffersResponseOut": "_androidpublisher_7_ListSubscriptionOffersResponseOut",
        "DeviceTierSetIn": "_androidpublisher_8_DeviceTierSetIn",
        "DeviceTierSetOut": "_androidpublisher_9_DeviceTierSetOut",
        "DeveloperInitiatedCancellationIn": "_androidpublisher_10_DeveloperInitiatedCancellationIn",
        "DeveloperInitiatedCancellationOut": "_androidpublisher_11_DeveloperInitiatedCancellationOut",
        "AcquisitionTargetingRuleIn": "_androidpublisher_12_AcquisitionTargetingRuleIn",
        "AcquisitionTargetingRuleOut": "_androidpublisher_13_AcquisitionTargetingRuleOut",
        "RecurringExternalTransactionIn": "_androidpublisher_14_RecurringExternalTransactionIn",
        "RecurringExternalTransactionOut": "_androidpublisher_15_RecurringExternalTransactionOut",
        "SubscriptionPurchasesDeferRequestIn": "_androidpublisher_16_SubscriptionPurchasesDeferRequestIn",
        "SubscriptionPurchasesDeferRequestOut": "_androidpublisher_17_SubscriptionPurchasesDeferRequestOut",
        "MigrateBasePlanPricesRequestIn": "_androidpublisher_18_MigrateBasePlanPricesRequestIn",
        "MigrateBasePlanPricesRequestOut": "_androidpublisher_19_MigrateBasePlanPricesRequestOut",
        "DeactivateSubscriptionOfferRequestIn": "_androidpublisher_20_DeactivateSubscriptionOfferRequestIn",
        "DeactivateSubscriptionOfferRequestOut": "_androidpublisher_21_DeactivateSubscriptionOfferRequestOut",
        "ListSubscriptionsResponseIn": "_androidpublisher_22_ListSubscriptionsResponseIn",
        "ListSubscriptionsResponseOut": "_androidpublisher_23_ListSubscriptionsResponseOut",
        "VariantIn": "_androidpublisher_24_VariantIn",
        "VariantOut": "_androidpublisher_25_VariantOut",
        "VariantTargetingIn": "_androidpublisher_26_VariantTargetingIn",
        "VariantTargetingOut": "_androidpublisher_27_VariantTargetingOut",
        "GeneratedApksPerSigningKeyIn": "_androidpublisher_28_GeneratedApksPerSigningKeyIn",
        "GeneratedApksPerSigningKeyOut": "_androidpublisher_29_GeneratedApksPerSigningKeyOut",
        "SubscriptionListingIn": "_androidpublisher_30_SubscriptionListingIn",
        "SubscriptionListingOut": "_androidpublisher_31_SubscriptionListingOut",
        "RegionalSubscriptionOfferPhaseConfigIn": "_androidpublisher_32_RegionalSubscriptionOfferPhaseConfigIn",
        "RegionalSubscriptionOfferPhaseConfigOut": "_androidpublisher_33_RegionalSubscriptionOfferPhaseConfigOut",
        "MultiAbiTargetingIn": "_androidpublisher_34_MultiAbiTargetingIn",
        "MultiAbiTargetingOut": "_androidpublisher_35_MultiAbiTargetingOut",
        "VoidedPurchasesListResponseIn": "_androidpublisher_36_VoidedPurchasesListResponseIn",
        "VoidedPurchasesListResponseOut": "_androidpublisher_37_VoidedPurchasesListResponseOut",
        "ImagesDeleteAllResponseIn": "_androidpublisher_38_ImagesDeleteAllResponseIn",
        "ImagesDeleteAllResponseOut": "_androidpublisher_39_ImagesDeleteAllResponseOut",
        "ExternalTransactionAddressIn": "_androidpublisher_40_ExternalTransactionAddressIn",
        "ExternalTransactionAddressOut": "_androidpublisher_41_ExternalTransactionAddressOut",
        "ConvertedRegionPriceIn": "_androidpublisher_42_ConvertedRegionPriceIn",
        "ConvertedRegionPriceOut": "_androidpublisher_43_ConvertedRegionPriceOut",
        "ConvertRegionPricesRequestIn": "_androidpublisher_44_ConvertRegionPricesRequestIn",
        "ConvertRegionPricesRequestOut": "_androidpublisher_45_ConvertRegionPricesRequestOut",
        "MultiAbiIn": "_androidpublisher_46_MultiAbiIn",
        "MultiAbiOut": "_androidpublisher_47_MultiAbiOut",
        "ExternalTransactionIn": "_androidpublisher_48_ExternalTransactionIn",
        "ExternalTransactionOut": "_androidpublisher_49_ExternalTransactionOut",
        "UserIn": "_androidpublisher_50_UserIn",
        "UserOut": "_androidpublisher_51_UserOut",
        "TracksListResponseIn": "_androidpublisher_52_TracksListResponseIn",
        "TracksListResponseOut": "_androidpublisher_53_TracksListResponseOut",
        "RegionalBasePlanConfigIn": "_androidpublisher_54_RegionalBasePlanConfigIn",
        "RegionalBasePlanConfigOut": "_androidpublisher_55_RegionalBasePlanConfigOut",
        "DeviceGroupIn": "_androidpublisher_56_DeviceGroupIn",
        "DeviceGroupOut": "_androidpublisher_57_DeviceGroupOut",
        "SubscribeWithGoogleInfoIn": "_androidpublisher_58_SubscribeWithGoogleInfoIn",
        "SubscribeWithGoogleInfoOut": "_androidpublisher_59_SubscribeWithGoogleInfoOut",
        "TokenPaginationIn": "_androidpublisher_60_TokenPaginationIn",
        "TokenPaginationOut": "_androidpublisher_61_TokenPaginationOut",
        "ManagedProductTaxAndComplianceSettingsIn": "_androidpublisher_62_ManagedProductTaxAndComplianceSettingsIn",
        "ManagedProductTaxAndComplianceSettingsOut": "_androidpublisher_63_ManagedProductTaxAndComplianceSettingsOut",
        "ListingsListResponseIn": "_androidpublisher_64_ListingsListResponseIn",
        "ListingsListResponseOut": "_androidpublisher_65_ListingsListResponseOut",
        "SplitApkMetadataIn": "_androidpublisher_66_SplitApkMetadataIn",
        "SplitApkMetadataOut": "_androidpublisher_67_SplitApkMetadataOut",
        "DeviceSpecIn": "_androidpublisher_68_DeviceSpecIn",
        "DeviceSpecOut": "_androidpublisher_69_DeviceSpecOut",
        "TrackTargetedCountryIn": "_androidpublisher_70_TrackTargetedCountryIn",
        "TrackTargetedCountryOut": "_androidpublisher_71_TrackTargetedCountryOut",
        "ScreenDensityIn": "_androidpublisher_72_ScreenDensityIn",
        "ScreenDensityOut": "_androidpublisher_73_ScreenDensityOut",
        "AssetSliceSetIn": "_androidpublisher_74_AssetSliceSetIn",
        "AssetSliceSetOut": "_androidpublisher_75_AssetSliceSetOut",
        "MoneyIn": "_androidpublisher_76_MoneyIn",
        "MoneyOut": "_androidpublisher_77_MoneyOut",
        "SdkVersionTargetingIn": "_androidpublisher_78_SdkVersionTargetingIn",
        "SdkVersionTargetingOut": "_androidpublisher_79_SdkVersionTargetingOut",
        "ReviewIn": "_androidpublisher_80_ReviewIn",
        "ReviewOut": "_androidpublisher_81_ReviewOut",
        "AbiIn": "_androidpublisher_82_AbiIn",
        "AbiOut": "_androidpublisher_83_AbiOut",
        "ProductPurchaseIn": "_androidpublisher_84_ProductPurchaseIn",
        "ProductPurchaseOut": "_androidpublisher_85_ProductPurchaseOut",
        "RefundExternalTransactionRequestIn": "_androidpublisher_86_RefundExternalTransactionRequestIn",
        "RefundExternalTransactionRequestOut": "_androidpublisher_87_RefundExternalTransactionRequestOut",
        "ApkTargetingIn": "_androidpublisher_88_ApkTargetingIn",
        "ApkTargetingOut": "_androidpublisher_89_ApkTargetingOut",
        "SystemApksListResponseIn": "_androidpublisher_90_SystemApksListResponseIn",
        "SystemApksListResponseOut": "_androidpublisher_91_SystemApksListResponseOut",
        "DeferredItemReplacementIn": "_androidpublisher_92_DeferredItemReplacementIn",
        "DeferredItemReplacementOut": "_androidpublisher_93_DeferredItemReplacementOut",
        "ActivateBasePlanRequestIn": "_androidpublisher_94_ActivateBasePlanRequestIn",
        "ActivateBasePlanRequestOut": "_androidpublisher_95_ActivateBasePlanRequestOut",
        "UpgradeTargetingRuleIn": "_androidpublisher_96_UpgradeTargetingRuleIn",
        "UpgradeTargetingRuleOut": "_androidpublisher_97_UpgradeTargetingRuleOut",
        "CommentIn": "_androidpublisher_98_CommentIn",
        "CommentOut": "_androidpublisher_99_CommentOut",
        "SubscriptionOfferTargetingIn": "_androidpublisher_100_SubscriptionOfferTargetingIn",
        "SubscriptionOfferTargetingOut": "_androidpublisher_101_SubscriptionOfferTargetingOut",
        "PrepaidPlanIn": "_androidpublisher_102_PrepaidPlanIn",
        "PrepaidPlanOut": "_androidpublisher_103_PrepaidPlanOut",
        "ArchiveSubscriptionRequestIn": "_androidpublisher_104_ArchiveSubscriptionRequestIn",
        "ArchiveSubscriptionRequestOut": "_androidpublisher_105_ArchiveSubscriptionRequestOut",
        "GeneratedAssetPackSliceIn": "_androidpublisher_106_GeneratedAssetPackSliceIn",
        "GeneratedAssetPackSliceOut": "_androidpublisher_107_GeneratedAssetPackSliceOut",
        "LanguageTargetingIn": "_androidpublisher_108_LanguageTargetingIn",
        "LanguageTargetingOut": "_androidpublisher_109_LanguageTargetingOut",
        "SubscriptionOfferPhaseIn": "_androidpublisher_110_SubscriptionOfferPhaseIn",
        "SubscriptionOfferPhaseOut": "_androidpublisher_111_SubscriptionOfferPhaseOut",
        "OfferTagIn": "_androidpublisher_112_OfferTagIn",
        "OfferTagOut": "_androidpublisher_113_OfferTagOut",
        "ApksListResponseIn": "_androidpublisher_114_ApksListResponseIn",
        "ApksListResponseOut": "_androidpublisher_115_ApksListResponseOut",
        "SubscriptionPurchaseV2In": "_androidpublisher_116_SubscriptionPurchaseV2In",
        "SubscriptionPurchaseV2Out": "_androidpublisher_117_SubscriptionPurchaseV2Out",
        "PageInfoIn": "_androidpublisher_118_PageInfoIn",
        "PageInfoOut": "_androidpublisher_119_PageInfoOut",
        "DeobfuscationFilesUploadResponseIn": "_androidpublisher_120_DeobfuscationFilesUploadResponseIn",
        "DeobfuscationFilesUploadResponseOut": "_androidpublisher_121_DeobfuscationFilesUploadResponseOut",
        "AutoRenewingPlanIn": "_androidpublisher_122_AutoRenewingPlanIn",
        "AutoRenewingPlanOut": "_androidpublisher_123_AutoRenewingPlanOut",
        "AssetModuleMetadataIn": "_androidpublisher_124_AssetModuleMetadataIn",
        "AssetModuleMetadataOut": "_androidpublisher_125_AssetModuleMetadataOut",
        "PartialRefundIn": "_androidpublisher_126_PartialRefundIn",
        "PartialRefundOut": "_androidpublisher_127_PartialRefundOut",
        "TargetingRuleScopeIn": "_androidpublisher_128_TargetingRuleScopeIn",
        "TargetingRuleScopeOut": "_androidpublisher_129_TargetingRuleScopeOut",
        "UserCountriesTargetingIn": "_androidpublisher_130_UserCountriesTargetingIn",
        "UserCountriesTargetingOut": "_androidpublisher_131_UserCountriesTargetingOut",
        "TargetingInfoIn": "_androidpublisher_132_TargetingInfoIn",
        "TargetingInfoOut": "_androidpublisher_133_TargetingInfoOut",
        "TextureCompressionFormatIn": "_androidpublisher_134_TextureCompressionFormatIn",
        "TextureCompressionFormatOut": "_androidpublisher_135_TextureCompressionFormatOut",
        "DeviceIdIn": "_androidpublisher_136_DeviceIdIn",
        "DeviceIdOut": "_androidpublisher_137_DeviceIdOut",
        "StandaloneApkMetadataIn": "_androidpublisher_138_StandaloneApkMetadataIn",
        "StandaloneApkMetadataOut": "_androidpublisher_139_StandaloneApkMetadataOut",
        "ApkDescriptionIn": "_androidpublisher_140_ApkDescriptionIn",
        "ApkDescriptionOut": "_androidpublisher_141_ApkDescriptionOut",
        "ApksAddExternallyHostedResponseIn": "_androidpublisher_142_ApksAddExternallyHostedResponseIn",
        "ApksAddExternallyHostedResponseOut": "_androidpublisher_143_ApksAddExternallyHostedResponseOut",
        "ReviewReplyResultIn": "_androidpublisher_144_ReviewReplyResultIn",
        "ReviewReplyResultOut": "_androidpublisher_145_ReviewReplyResultOut",
        "DeviceTierConfigIn": "_androidpublisher_146_DeviceTierConfigIn",
        "DeviceTierConfigOut": "_androidpublisher_147_DeviceTierConfigOut",
        "PriceIn": "_androidpublisher_148_PriceIn",
        "PriceOut": "_androidpublisher_149_PriceOut",
        "SplitApkVariantIn": "_androidpublisher_150_SplitApkVariantIn",
        "SplitApkVariantOut": "_androidpublisher_151_SplitApkVariantOut",
        "SubscriptionDeferralInfoIn": "_androidpublisher_152_SubscriptionDeferralInfoIn",
        "SubscriptionDeferralInfoOut": "_androidpublisher_153_SubscriptionDeferralInfoOut",
        "FullRefundIn": "_androidpublisher_154_FullRefundIn",
        "FullRefundOut": "_androidpublisher_155_FullRefundOut",
        "ConvertRegionPricesResponseIn": "_androidpublisher_156_ConvertRegionPricesResponseIn",
        "ConvertRegionPricesResponseOut": "_androidpublisher_157_ConvertRegionPricesResponseOut",
        "ApkIn": "_androidpublisher_158_ApkIn",
        "ApkOut": "_androidpublisher_159_ApkOut",
        "ApksAddExternallyHostedRequestIn": "_androidpublisher_160_ApksAddExternallyHostedRequestIn",
        "ApksAddExternallyHostedRequestOut": "_androidpublisher_161_ApksAddExternallyHostedRequestOut",
        "ProductPurchasesAcknowledgeRequestIn": "_androidpublisher_162_ProductPurchasesAcknowledgeRequestIn",
        "ProductPurchasesAcknowledgeRequestOut": "_androidpublisher_163_ProductPurchasesAcknowledgeRequestOut",
        "DeactivateBasePlanRequestIn": "_androidpublisher_164_DeactivateBasePlanRequestIn",
        "DeactivateBasePlanRequestOut": "_androidpublisher_165_DeactivateBasePlanRequestOut",
        "ExternallyHostedApkIn": "_androidpublisher_166_ExternallyHostedApkIn",
        "ExternallyHostedApkOut": "_androidpublisher_167_ExternallyHostedApkOut",
        "OneTimeExternalTransactionIn": "_androidpublisher_168_OneTimeExternalTransactionIn",
        "OneTimeExternalTransactionOut": "_androidpublisher_169_OneTimeExternalTransactionOut",
        "ApkSetIn": "_androidpublisher_170_ApkSetIn",
        "ApkSetOut": "_androidpublisher_171_ApkSetOut",
        "UsesPermissionIn": "_androidpublisher_172_UsesPermissionIn",
        "UsesPermissionOut": "_androidpublisher_173_UsesPermissionOut",
        "TestersIn": "_androidpublisher_174_TestersIn",
        "TestersOut": "_androidpublisher_175_TestersOut",
        "IntroductoryPriceInfoIn": "_androidpublisher_176_IntroductoryPriceInfoIn",
        "IntroductoryPriceInfoOut": "_androidpublisher_177_IntroductoryPriceInfoOut",
        "DeviceFeatureIn": "_androidpublisher_178_DeviceFeatureIn",
        "DeviceFeatureOut": "_androidpublisher_179_DeviceFeatureOut",
        "GeneratedSplitApkIn": "_androidpublisher_180_GeneratedSplitApkIn",
        "GeneratedSplitApkOut": "_androidpublisher_181_GeneratedSplitApkOut",
        "ExternalAccountIdentifiersIn": "_androidpublisher_182_ExternalAccountIdentifiersIn",
        "ExternalAccountIdentifiersOut": "_androidpublisher_183_ExternalAccountIdentifiersOut",
        "DeviceSelectorIn": "_androidpublisher_184_DeviceSelectorIn",
        "DeviceSelectorOut": "_androidpublisher_185_DeviceSelectorOut",
        "ListingIn": "_androidpublisher_186_ListingIn",
        "ListingOut": "_androidpublisher_187_ListingOut",
        "BundlesListResponseIn": "_androidpublisher_188_BundlesListResponseIn",
        "BundlesListResponseOut": "_androidpublisher_189_BundlesListResponseOut",
        "InternalAppSharingArtifactIn": "_androidpublisher_190_InternalAppSharingArtifactIn",
        "InternalAppSharingArtifactOut": "_androidpublisher_191_InternalAppSharingArtifactOut",
        "OtherRegionsSubscriptionOfferPhasePricesIn": "_androidpublisher_192_OtherRegionsSubscriptionOfferPhasePricesIn",
        "OtherRegionsSubscriptionOfferPhasePricesOut": "_androidpublisher_193_OtherRegionsSubscriptionOfferPhasePricesOut",
        "GeneratedApksListResponseIn": "_androidpublisher_194_GeneratedApksListResponseIn",
        "GeneratedApksListResponseOut": "_androidpublisher_195_GeneratedApksListResponseOut",
        "ReviewsReplyResponseIn": "_androidpublisher_196_ReviewsReplyResponseIn",
        "ReviewsReplyResponseOut": "_androidpublisher_197_ReviewsReplyResponseOut",
        "DeviceRamIn": "_androidpublisher_198_DeviceRamIn",
        "DeviceRamOut": "_androidpublisher_199_DeviceRamOut",
        "AppEditIn": "_androidpublisher_200_AppEditIn",
        "AppEditOut": "_androidpublisher_201_AppEditOut",
        "CanceledStateContextIn": "_androidpublisher_202_CanceledStateContextIn",
        "CanceledStateContextOut": "_androidpublisher_203_CanceledStateContextOut",
        "AppDetailsIn": "_androidpublisher_204_AppDetailsIn",
        "AppDetailsOut": "_androidpublisher_205_AppDetailsOut",
        "SubscriptionPriceChangeIn": "_androidpublisher_206_SubscriptionPriceChangeIn",
        "SubscriptionPriceChangeOut": "_androidpublisher_207_SubscriptionPriceChangeOut",
        "ImagesUploadResponseIn": "_androidpublisher_208_ImagesUploadResponseIn",
        "ImagesUploadResponseOut": "_androidpublisher_209_ImagesUploadResponseOut",
        "ListUsersResponseIn": "_androidpublisher_210_ListUsersResponseIn",
        "ListUsersResponseOut": "_androidpublisher_211_ListUsersResponseOut",
        "SubscriptionTaxAndComplianceSettingsIn": "_androidpublisher_212_SubscriptionTaxAndComplianceSettingsIn",
        "SubscriptionTaxAndComplianceSettingsOut": "_androidpublisher_213_SubscriptionTaxAndComplianceSettingsOut",
        "SubscriptionItemPriceChangeDetailsIn": "_androidpublisher_214_SubscriptionItemPriceChangeDetailsIn",
        "SubscriptionItemPriceChangeDetailsOut": "_androidpublisher_215_SubscriptionItemPriceChangeDetailsOut",
        "ScreenDensityTargetingIn": "_androidpublisher_216_ScreenDensityTargetingIn",
        "ScreenDensityTargetingOut": "_androidpublisher_217_ScreenDensityTargetingOut",
        "TextureCompressionFormatTargetingIn": "_androidpublisher_218_TextureCompressionFormatTargetingIn",
        "TextureCompressionFormatTargetingOut": "_androidpublisher_219_TextureCompressionFormatTargetingOut",
        "AbiTargetingIn": "_androidpublisher_220_AbiTargetingIn",
        "AbiTargetingOut": "_androidpublisher_221_AbiTargetingOut",
        "TrackReleaseIn": "_androidpublisher_222_TrackReleaseIn",
        "TrackReleaseOut": "_androidpublisher_223_TrackReleaseOut",
        "RegionsVersionIn": "_androidpublisher_224_RegionsVersionIn",
        "RegionsVersionOut": "_androidpublisher_225_RegionsVersionOut",
        "ListDeviceTierConfigsResponseIn": "_androidpublisher_226_ListDeviceTierConfigsResponseIn",
        "ListDeviceTierConfigsResponseOut": "_androidpublisher_227_ListDeviceTierConfigsResponseOut",
        "InAppProductIn": "_androidpublisher_228_InAppProductIn",
        "InAppProductOut": "_androidpublisher_229_InAppProductOut",
        "ExternalSubscriptionIn": "_androidpublisher_230_ExternalSubscriptionIn",
        "ExternalSubscriptionOut": "_androidpublisher_231_ExternalSubscriptionOut",
        "PausedStateContextIn": "_androidpublisher_232_PausedStateContextIn",
        "PausedStateContextOut": "_androidpublisher_233_PausedStateContextOut",
        "TimestampIn": "_androidpublisher_234_TimestampIn",
        "TimestampOut": "_androidpublisher_235_TimestampOut",
        "RegionalSubscriptionOfferConfigIn": "_androidpublisher_236_RegionalSubscriptionOfferConfigIn",
        "RegionalSubscriptionOfferConfigOut": "_androidpublisher_237_RegionalSubscriptionOfferConfigOut",
        "CancelSurveyResultIn": "_androidpublisher_238_CancelSurveyResultIn",
        "CancelSurveyResultOut": "_androidpublisher_239_CancelSurveyResultOut",
        "SubscriptionPurchaseIn": "_androidpublisher_240_SubscriptionPurchaseIn",
        "SubscriptionPurchaseOut": "_androidpublisher_241_SubscriptionPurchaseOut",
        "UserCountrySetIn": "_androidpublisher_242_UserCountrySetIn",
        "UserCountrySetOut": "_androidpublisher_243_UserCountrySetOut",
        "ExpansionFileIn": "_androidpublisher_244_ExpansionFileIn",
        "ExpansionFileOut": "_androidpublisher_245_ExpansionFileOut",
        "GeneratedUniversalApkIn": "_androidpublisher_246_GeneratedUniversalApkIn",
        "GeneratedUniversalApkOut": "_androidpublisher_247_GeneratedUniversalApkOut",
        "ConvertedOtherRegionsPriceIn": "_androidpublisher_248_ConvertedOtherRegionsPriceIn",
        "ConvertedOtherRegionsPriceOut": "_androidpublisher_249_ConvertedOtherRegionsPriceOut",
        "RegionalPriceMigrationConfigIn": "_androidpublisher_250_RegionalPriceMigrationConfigIn",
        "RegionalPriceMigrationConfigOut": "_androidpublisher_251_RegionalPriceMigrationConfigOut",
        "DeobfuscationFileIn": "_androidpublisher_252_DeobfuscationFileIn",
        "DeobfuscationFileOut": "_androidpublisher_253_DeobfuscationFileOut",
        "OtherRegionsSubscriptionOfferConfigIn": "_androidpublisher_254_OtherRegionsSubscriptionOfferConfigIn",
        "OtherRegionsSubscriptionOfferConfigOut": "_androidpublisher_255_OtherRegionsSubscriptionOfferConfigOut",
        "BundleIn": "_androidpublisher_256_BundleIn",
        "BundleOut": "_androidpublisher_257_BundleOut",
        "VoidedPurchaseIn": "_androidpublisher_258_VoidedPurchaseIn",
        "VoidedPurchaseOut": "_androidpublisher_259_VoidedPurchaseOut",
        "DeviceMetadataIn": "_androidpublisher_260_DeviceMetadataIn",
        "DeviceMetadataOut": "_androidpublisher_261_DeviceMetadataOut",
        "ExpansionFilesUploadResponseIn": "_androidpublisher_262_ExpansionFilesUploadResponseIn",
        "ExpansionFilesUploadResponseOut": "_androidpublisher_263_ExpansionFilesUploadResponseOut",
        "PrepaidBasePlanTypeIn": "_androidpublisher_264_PrepaidBasePlanTypeIn",
        "PrepaidBasePlanTypeOut": "_androidpublisher_265_PrepaidBasePlanTypeOut",
        "SubscriptionOfferIn": "_androidpublisher_266_SubscriptionOfferIn",
        "SubscriptionOfferOut": "_androidpublisher_267_SubscriptionOfferOut",
        "AutoRenewingBasePlanTypeIn": "_androidpublisher_268_AutoRenewingBasePlanTypeIn",
        "AutoRenewingBasePlanTypeOut": "_androidpublisher_269_AutoRenewingBasePlanTypeOut",
        "TestPurchaseIn": "_androidpublisher_270_TestPurchaseIn",
        "TestPurchaseOut": "_androidpublisher_271_TestPurchaseOut",
        "SdkVersionIn": "_androidpublisher_272_SdkVersionIn",
        "SdkVersionOut": "_androidpublisher_273_SdkVersionOut",
        "DeveloperCommentIn": "_androidpublisher_274_DeveloperCommentIn",
        "DeveloperCommentOut": "_androidpublisher_275_DeveloperCommentOut",
        "MigrateBasePlanPricesResponseIn": "_androidpublisher_276_MigrateBasePlanPricesResponseIn",
        "MigrateBasePlanPricesResponseOut": "_androidpublisher_277_MigrateBasePlanPricesResponseOut",
        "ImageIn": "_androidpublisher_278_ImageIn",
        "ImageOut": "_androidpublisher_279_ImageOut",
        "SubscriptionIn": "_androidpublisher_280_SubscriptionIn",
        "SubscriptionOut": "_androidpublisher_281_SubscriptionOut",
        "ModuleTargetingIn": "_androidpublisher_282_ModuleTargetingIn",
        "ModuleTargetingOut": "_androidpublisher_283_ModuleTargetingOut",
        "RegionalTaxRateInfoIn": "_androidpublisher_284_RegionalTaxRateInfoIn",
        "RegionalTaxRateInfoOut": "_androidpublisher_285_RegionalTaxRateInfoOut",
        "SystemFeatureIn": "_androidpublisher_286_SystemFeatureIn",
        "SystemFeatureOut": "_androidpublisher_287_SystemFeatureOut",
        "CountryTargetingIn": "_androidpublisher_288_CountryTargetingIn",
        "CountryTargetingOut": "_androidpublisher_289_CountryTargetingOut",
        "SubscriptionCancelSurveyResultIn": "_androidpublisher_290_SubscriptionCancelSurveyResultIn",
        "SubscriptionCancelSurveyResultOut": "_androidpublisher_291_SubscriptionCancelSurveyResultOut",
        "UserCommentIn": "_androidpublisher_292_UserCommentIn",
        "UserCommentOut": "_androidpublisher_293_UserCommentOut",
        "ReplacementCancellationIn": "_androidpublisher_294_ReplacementCancellationIn",
        "ReplacementCancellationOut": "_androidpublisher_295_ReplacementCancellationOut",
        "InAppProductListingIn": "_androidpublisher_296_InAppProductListingIn",
        "InAppProductListingOut": "_androidpublisher_297_InAppProductListingOut",
        "ActivateSubscriptionOfferRequestIn": "_androidpublisher_298_ActivateSubscriptionOfferRequestIn",
        "ActivateSubscriptionOfferRequestOut": "_androidpublisher_299_ActivateSubscriptionOfferRequestOut",
        "ApkBinaryIn": "_androidpublisher_300_ApkBinaryIn",
        "ApkBinaryOut": "_androidpublisher_301_ApkBinaryOut",
        "LocalizedTextIn": "_androidpublisher_302_LocalizedTextIn",
        "LocalizedTextOut": "_androidpublisher_303_LocalizedTextOut",
        "TrackCountryAvailabilityIn": "_androidpublisher_304_TrackCountryAvailabilityIn",
        "TrackCountryAvailabilityOut": "_androidpublisher_305_TrackCountryAvailabilityOut",
        "GrantIn": "_androidpublisher_306_GrantIn",
        "GrantOut": "_androidpublisher_307_GrantOut",
        "SubscriptionPurchasesAcknowledgeRequestIn": "_androidpublisher_308_SubscriptionPurchasesAcknowledgeRequestIn",
        "SubscriptionPurchasesAcknowledgeRequestOut": "_androidpublisher_309_SubscriptionPurchasesAcknowledgeRequestOut",
        "UserInitiatedCancellationIn": "_androidpublisher_310_UserInitiatedCancellationIn",
        "UserInitiatedCancellationOut": "_androidpublisher_311_UserInitiatedCancellationOut",
        "ReviewsListResponseIn": "_androidpublisher_312_ReviewsListResponseIn",
        "ReviewsListResponseOut": "_androidpublisher_313_ReviewsListResponseOut",
        "BasePlanIn": "_androidpublisher_314_BasePlanIn",
        "BasePlanOut": "_androidpublisher_315_BasePlanOut",
        "OtherRegionsBasePlanConfigIn": "_androidpublisher_316_OtherRegionsBasePlanConfigIn",
        "OtherRegionsBasePlanConfigOut": "_androidpublisher_317_OtherRegionsBasePlanConfigOut",
        "ReviewsReplyRequestIn": "_androidpublisher_318_ReviewsReplyRequestIn",
        "ReviewsReplyRequestOut": "_androidpublisher_319_ReviewsReplyRequestOut",
        "OtherRegionsSubscriptionOfferPhaseConfigIn": "_androidpublisher_320_OtherRegionsSubscriptionOfferPhaseConfigIn",
        "OtherRegionsSubscriptionOfferPhaseConfigOut": "_androidpublisher_321_OtherRegionsSubscriptionOfferPhaseConfigOut",
        "OfferDetailsIn": "_androidpublisher_322_OfferDetailsIn",
        "OfferDetailsOut": "_androidpublisher_323_OfferDetailsOut",
        "DeviceFeatureTargetingIn": "_androidpublisher_324_DeviceFeatureTargetingIn",
        "DeviceFeatureTargetingOut": "_androidpublisher_325_DeviceFeatureTargetingOut",
        "ImagesListResponseIn": "_androidpublisher_326_ImagesListResponseIn",
        "ImagesListResponseOut": "_androidpublisher_327_ImagesListResponseOut",
        "SubscriptionPurchasesDeferResponseIn": "_androidpublisher_328_SubscriptionPurchasesDeferResponseIn",
        "SubscriptionPurchasesDeferResponseOut": "_androidpublisher_329_SubscriptionPurchasesDeferResponseOut",
        "DeviceTierIn": "_androidpublisher_330_DeviceTierIn",
        "DeviceTierOut": "_androidpublisher_331_DeviceTierOut",
        "SubscriptionPurchaseLineItemIn": "_androidpublisher_332_SubscriptionPurchaseLineItemIn",
        "SubscriptionPurchaseLineItemOut": "_androidpublisher_333_SubscriptionPurchaseLineItemOut",
        "ExternalTransactionTestPurchaseIn": "_androidpublisher_334_ExternalTransactionTestPurchaseIn",
        "ExternalTransactionTestPurchaseOut": "_androidpublisher_335_ExternalTransactionTestPurchaseOut",
        "GeneratedStandaloneApkIn": "_androidpublisher_336_GeneratedStandaloneApkIn",
        "GeneratedStandaloneApkOut": "_androidpublisher_337_GeneratedStandaloneApkOut",
        "SystemInitiatedCancellationIn": "_androidpublisher_338_SystemInitiatedCancellationIn",
        "SystemInitiatedCancellationOut": "_androidpublisher_339_SystemInitiatedCancellationOut",
        "TrackIn": "_androidpublisher_340_TrackIn",
        "TrackOut": "_androidpublisher_341_TrackOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["InappproductsListResponseIn"] = t.struct(
        {
            "tokenPagination": t.proxy(renames["TokenPaginationIn"]).optional(),
            "pageInfo": t.proxy(renames["PageInfoIn"]).optional(),
            "inappproduct": t.array(t.proxy(renames["InAppProductIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["InappproductsListResponseIn"])
    types["InappproductsListResponseOut"] = t.struct(
        {
            "tokenPagination": t.proxy(renames["TokenPaginationOut"]).optional(),
            "pageInfo": t.proxy(renames["PageInfoOut"]).optional(),
            "inappproduct": t.array(t.proxy(renames["InAppProductOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InappproductsListResponseOut"])
    types["ModuleMetadataIn"] = t.struct(
        {
            "dependencies": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "targeting": t.proxy(renames["ModuleTargetingIn"]).optional(),
            "deliveryType": t.string().optional(),
            "moduleType": t.string().optional(),
        }
    ).named(renames["ModuleMetadataIn"])
    types["ModuleMetadataOut"] = t.struct(
        {
            "dependencies": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "targeting": t.proxy(renames["ModuleTargetingOut"]).optional(),
            "deliveryType": t.string().optional(),
            "moduleType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ModuleMetadataOut"])
    types["ListSubscriptionOffersResponseIn"] = t.struct(
        {
            "subscriptionOffers": t.array(
                t.proxy(renames["SubscriptionOfferIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListSubscriptionOffersResponseIn"])
    types["ListSubscriptionOffersResponseOut"] = t.struct(
        {
            "subscriptionOffers": t.array(
                t.proxy(renames["SubscriptionOfferOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSubscriptionOffersResponseOut"])
    types["DeviceTierSetIn"] = t.struct(
        {"deviceTiers": t.array(t.proxy(renames["DeviceTierIn"])).optional()}
    ).named(renames["DeviceTierSetIn"])
    types["DeviceTierSetOut"] = t.struct(
        {
            "deviceTiers": t.array(t.proxy(renames["DeviceTierOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceTierSetOut"])
    types["DeveloperInitiatedCancellationIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DeveloperInitiatedCancellationIn"])
    types["DeveloperInitiatedCancellationOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeveloperInitiatedCancellationOut"])
    types["AcquisitionTargetingRuleIn"] = t.struct(
        {"scope": t.proxy(renames["TargetingRuleScopeIn"])}
    ).named(renames["AcquisitionTargetingRuleIn"])
    types["AcquisitionTargetingRuleOut"] = t.struct(
        {
            "scope": t.proxy(renames["TargetingRuleScopeOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AcquisitionTargetingRuleOut"])
    types["RecurringExternalTransactionIn"] = t.struct(
        {
            "initialExternalTransactionId": t.string().optional(),
            "externalTransactionToken": t.string().optional(),
            "externalSubscription": t.proxy(
                renames["ExternalSubscriptionIn"]
            ).optional(),
        }
    ).named(renames["RecurringExternalTransactionIn"])
    types["RecurringExternalTransactionOut"] = t.struct(
        {
            "initialExternalTransactionId": t.string().optional(),
            "externalTransactionToken": t.string().optional(),
            "externalSubscription": t.proxy(
                renames["ExternalSubscriptionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RecurringExternalTransactionOut"])
    types["SubscriptionPurchasesDeferRequestIn"] = t.struct(
        {"deferralInfo": t.proxy(renames["SubscriptionDeferralInfoIn"]).optional()}
    ).named(renames["SubscriptionPurchasesDeferRequestIn"])
    types["SubscriptionPurchasesDeferRequestOut"] = t.struct(
        {
            "deferralInfo": t.proxy(renames["SubscriptionDeferralInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscriptionPurchasesDeferRequestOut"])
    types["MigrateBasePlanPricesRequestIn"] = t.struct(
        {
            "regionsVersion": t.proxy(renames["RegionsVersionIn"]),
            "regionalPriceMigrations": t.array(
                t.proxy(renames["RegionalPriceMigrationConfigIn"])
            ),
        }
    ).named(renames["MigrateBasePlanPricesRequestIn"])
    types["MigrateBasePlanPricesRequestOut"] = t.struct(
        {
            "regionsVersion": t.proxy(renames["RegionsVersionOut"]),
            "regionalPriceMigrations": t.array(
                t.proxy(renames["RegionalPriceMigrationConfigOut"])
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MigrateBasePlanPricesRequestOut"])
    types["DeactivateSubscriptionOfferRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DeactivateSubscriptionOfferRequestIn"])
    types["DeactivateSubscriptionOfferRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeactivateSubscriptionOfferRequestOut"])
    types["ListSubscriptionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "subscriptions": t.array(t.proxy(renames["SubscriptionIn"])).optional(),
        }
    ).named(renames["ListSubscriptionsResponseIn"])
    types["ListSubscriptionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "subscriptions": t.array(t.proxy(renames["SubscriptionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSubscriptionsResponseOut"])
    types["VariantIn"] = t.struct(
        {"deviceSpec": t.proxy(renames["DeviceSpecIn"]).optional()}
    ).named(renames["VariantIn"])
    types["VariantOut"] = t.struct(
        {
            "deviceSpec": t.proxy(renames["DeviceSpecOut"]).optional(),
            "variantId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VariantOut"])
    types["VariantTargetingIn"] = t.struct(
        {
            "textureCompressionFormatTargeting": t.proxy(
                renames["TextureCompressionFormatTargetingIn"]
            ).optional(),
            "abiTargeting": t.proxy(renames["AbiTargetingIn"]).optional(),
            "sdkVersionTargeting": t.proxy(renames["SdkVersionTargetingIn"]).optional(),
            "multiAbiTargeting": t.proxy(renames["MultiAbiTargetingIn"]).optional(),
            "screenDensityTargeting": t.proxy(
                renames["ScreenDensityTargetingIn"]
            ).optional(),
        }
    ).named(renames["VariantTargetingIn"])
    types["VariantTargetingOut"] = t.struct(
        {
            "textureCompressionFormatTargeting": t.proxy(
                renames["TextureCompressionFormatTargetingOut"]
            ).optional(),
            "abiTargeting": t.proxy(renames["AbiTargetingOut"]).optional(),
            "sdkVersionTargeting": t.proxy(
                renames["SdkVersionTargetingOut"]
            ).optional(),
            "multiAbiTargeting": t.proxy(renames["MultiAbiTargetingOut"]).optional(),
            "screenDensityTargeting": t.proxy(
                renames["ScreenDensityTargetingOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VariantTargetingOut"])
    types["GeneratedApksPerSigningKeyIn"] = t.struct(
        {
            "generatedAssetPackSlices": t.array(
                t.proxy(renames["GeneratedAssetPackSliceIn"])
            ).optional(),
            "generatedSplitApks": t.array(
                t.proxy(renames["GeneratedSplitApkIn"])
            ).optional(),
            "certificateSha256Hash": t.string().optional(),
            "generatedUniversalApk": t.proxy(
                renames["GeneratedUniversalApkIn"]
            ).optional(),
            "targetingInfo": t.proxy(renames["TargetingInfoIn"]).optional(),
            "generatedStandaloneApks": t.array(
                t.proxy(renames["GeneratedStandaloneApkIn"])
            ).optional(),
        }
    ).named(renames["GeneratedApksPerSigningKeyIn"])
    types["GeneratedApksPerSigningKeyOut"] = t.struct(
        {
            "generatedAssetPackSlices": t.array(
                t.proxy(renames["GeneratedAssetPackSliceOut"])
            ).optional(),
            "generatedSplitApks": t.array(
                t.proxy(renames["GeneratedSplitApkOut"])
            ).optional(),
            "certificateSha256Hash": t.string().optional(),
            "generatedUniversalApk": t.proxy(
                renames["GeneratedUniversalApkOut"]
            ).optional(),
            "targetingInfo": t.proxy(renames["TargetingInfoOut"]).optional(),
            "generatedStandaloneApks": t.array(
                t.proxy(renames["GeneratedStandaloneApkOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GeneratedApksPerSigningKeyOut"])
    types["SubscriptionListingIn"] = t.struct(
        {
            "description": t.string().optional(),
            "benefits": t.array(t.string()).optional(),
            "title": t.string(),
            "languageCode": t.string(),
        }
    ).named(renames["SubscriptionListingIn"])
    types["SubscriptionListingOut"] = t.struct(
        {
            "description": t.string().optional(),
            "benefits": t.array(t.string()).optional(),
            "title": t.string(),
            "languageCode": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscriptionListingOut"])
    types["RegionalSubscriptionOfferPhaseConfigIn"] = t.struct(
        {
            "absoluteDiscount": t.proxy(renames["MoneyIn"]).optional(),
            "price": t.proxy(renames["MoneyIn"]).optional(),
            "regionCode": t.string(),
            "relativeDiscount": t.number().optional(),
        }
    ).named(renames["RegionalSubscriptionOfferPhaseConfigIn"])
    types["RegionalSubscriptionOfferPhaseConfigOut"] = t.struct(
        {
            "absoluteDiscount": t.proxy(renames["MoneyOut"]).optional(),
            "price": t.proxy(renames["MoneyOut"]).optional(),
            "regionCode": t.string(),
            "relativeDiscount": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegionalSubscriptionOfferPhaseConfigOut"])
    types["MultiAbiTargetingIn"] = t.struct(
        {
            "alternatives": t.array(t.proxy(renames["MultiAbiIn"])).optional(),
            "value": t.array(t.proxy(renames["MultiAbiIn"])).optional(),
        }
    ).named(renames["MultiAbiTargetingIn"])
    types["MultiAbiTargetingOut"] = t.struct(
        {
            "alternatives": t.array(t.proxy(renames["MultiAbiOut"])).optional(),
            "value": t.array(t.proxy(renames["MultiAbiOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MultiAbiTargetingOut"])
    types["VoidedPurchasesListResponseIn"] = t.struct(
        {
            "voidedPurchases": t.array(t.proxy(renames["VoidedPurchaseIn"])),
            "pageInfo": t.proxy(renames["PageInfoIn"]).optional(),
            "tokenPagination": t.proxy(renames["TokenPaginationIn"]).optional(),
        }
    ).named(renames["VoidedPurchasesListResponseIn"])
    types["VoidedPurchasesListResponseOut"] = t.struct(
        {
            "voidedPurchases": t.array(t.proxy(renames["VoidedPurchaseOut"])),
            "pageInfo": t.proxy(renames["PageInfoOut"]).optional(),
            "tokenPagination": t.proxy(renames["TokenPaginationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VoidedPurchasesListResponseOut"])
    types["ImagesDeleteAllResponseIn"] = t.struct(
        {"deleted": t.array(t.proxy(renames["ImageIn"])).optional()}
    ).named(renames["ImagesDeleteAllResponseIn"])
    types["ImagesDeleteAllResponseOut"] = t.struct(
        {
            "deleted": t.array(t.proxy(renames["ImageOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImagesDeleteAllResponseOut"])
    types["ExternalTransactionAddressIn"] = t.struct({"regionCode": t.string()}).named(
        renames["ExternalTransactionAddressIn"]
    )
    types["ExternalTransactionAddressOut"] = t.struct(
        {
            "regionCode": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExternalTransactionAddressOut"])
    types["ConvertedRegionPriceIn"] = t.struct(
        {
            "regionCode": t.string().optional(),
            "taxAmount": t.proxy(renames["MoneyIn"]).optional(),
            "price": t.proxy(renames["MoneyIn"]).optional(),
        }
    ).named(renames["ConvertedRegionPriceIn"])
    types["ConvertedRegionPriceOut"] = t.struct(
        {
            "regionCode": t.string().optional(),
            "taxAmount": t.proxy(renames["MoneyOut"]).optional(),
            "price": t.proxy(renames["MoneyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConvertedRegionPriceOut"])
    types["ConvertRegionPricesRequestIn"] = t.struct(
        {"price": t.proxy(renames["MoneyIn"]).optional()}
    ).named(renames["ConvertRegionPricesRequestIn"])
    types["ConvertRegionPricesRequestOut"] = t.struct(
        {
            "price": t.proxy(renames["MoneyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConvertRegionPricesRequestOut"])
    types["MultiAbiIn"] = t.struct(
        {"abi": t.array(t.proxy(renames["AbiIn"])).optional()}
    ).named(renames["MultiAbiIn"])
    types["MultiAbiOut"] = t.struct(
        {
            "abi": t.array(t.proxy(renames["AbiOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MultiAbiOut"])
    types["ExternalTransactionIn"] = t.struct(
        {
            "oneTimeTransaction": t.proxy(
                renames["OneTimeExternalTransactionIn"]
            ).optional(),
            "transactionTime": t.string(),
            "recurringTransaction": t.proxy(
                renames["RecurringExternalTransactionIn"]
            ).optional(),
            "originalPreTaxAmount": t.proxy(renames["PriceIn"]),
            "userTaxAddress": t.proxy(renames["ExternalTransactionAddressIn"]),
            "originalTaxAmount": t.proxy(renames["PriceIn"]),
        }
    ).named(renames["ExternalTransactionIn"])
    types["ExternalTransactionOut"] = t.struct(
        {
            "currentPreTaxAmount": t.proxy(renames["PriceOut"]).optional(),
            "oneTimeTransaction": t.proxy(
                renames["OneTimeExternalTransactionOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "packageName": t.string().optional(),
            "currentTaxAmount": t.proxy(renames["PriceOut"]).optional(),
            "externalTransactionId": t.string().optional(),
            "transactionTime": t.string(),
            "recurringTransaction": t.proxy(
                renames["RecurringExternalTransactionOut"]
            ).optional(),
            "originalPreTaxAmount": t.proxy(renames["PriceOut"]),
            "transactionState": t.string().optional(),
            "testPurchase": t.proxy(
                renames["ExternalTransactionTestPurchaseOut"]
            ).optional(),
            "userTaxAddress": t.proxy(renames["ExternalTransactionAddressOut"]),
            "originalTaxAmount": t.proxy(renames["PriceOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExternalTransactionOut"])
    types["UserIn"] = t.struct(
        {
            "developerAccountPermissions": t.array(t.string()).optional(),
            "name": t.string(),
            "email": t.string().optional(),
            "expirationTime": t.string().optional(),
        }
    ).named(renames["UserIn"])
    types["UserOut"] = t.struct(
        {
            "developerAccountPermissions": t.array(t.string()).optional(),
            "accessState": t.string().optional(),
            "partial": t.boolean().optional(),
            "grants": t.array(t.proxy(renames["GrantOut"])).optional(),
            "name": t.string(),
            "email": t.string().optional(),
            "expirationTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserOut"])
    types["TracksListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "tracks": t.array(t.proxy(renames["TrackIn"])).optional(),
        }
    ).named(renames["TracksListResponseIn"])
    types["TracksListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "tracks": t.array(t.proxy(renames["TrackOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TracksListResponseOut"])
    types["RegionalBasePlanConfigIn"] = t.struct(
        {
            "price": t.proxy(renames["MoneyIn"]).optional(),
            "regionCode": t.string(),
            "newSubscriberAvailability": t.boolean().optional(),
        }
    ).named(renames["RegionalBasePlanConfigIn"])
    types["RegionalBasePlanConfigOut"] = t.struct(
        {
            "price": t.proxy(renames["MoneyOut"]).optional(),
            "regionCode": t.string(),
            "newSubscriberAvailability": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegionalBasePlanConfigOut"])
    types["DeviceGroupIn"] = t.struct(
        {
            "name": t.string().optional(),
            "deviceSelectors": t.array(t.proxy(renames["DeviceSelectorIn"])).optional(),
        }
    ).named(renames["DeviceGroupIn"])
    types["DeviceGroupOut"] = t.struct(
        {
            "name": t.string().optional(),
            "deviceSelectors": t.array(
                t.proxy(renames["DeviceSelectorOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceGroupOut"])
    types["SubscribeWithGoogleInfoIn"] = t.struct(
        {
            "emailAddress": t.string().optional(),
            "profileId": t.string().optional(),
            "profileName": t.string().optional(),
            "givenName": t.string().optional(),
            "familyName": t.string().optional(),
        }
    ).named(renames["SubscribeWithGoogleInfoIn"])
    types["SubscribeWithGoogleInfoOut"] = t.struct(
        {
            "emailAddress": t.string().optional(),
            "profileId": t.string().optional(),
            "profileName": t.string().optional(),
            "givenName": t.string().optional(),
            "familyName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscribeWithGoogleInfoOut"])
    types["TokenPaginationIn"] = t.struct(
        {"previousPageToken": t.string(), "nextPageToken": t.string().optional()}
    ).named(renames["TokenPaginationIn"])
    types["TokenPaginationOut"] = t.struct(
        {
            "previousPageToken": t.string(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TokenPaginationOut"])
    types["ManagedProductTaxAndComplianceSettingsIn"] = t.struct(
        {
            "eeaWithdrawalRightType": t.string().optional(),
            "taxRateInfoByRegionCode": t.struct(
                {"_": t.string().optional()}
            ).optional(),
        }
    ).named(renames["ManagedProductTaxAndComplianceSettingsIn"])
    types["ManagedProductTaxAndComplianceSettingsOut"] = t.struct(
        {
            "eeaWithdrawalRightType": t.string().optional(),
            "taxRateInfoByRegionCode": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedProductTaxAndComplianceSettingsOut"])
    types["ListingsListResponseIn"] = t.struct(
        {
            "listings": t.array(t.proxy(renames["ListingIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ListingsListResponseIn"])
    types["ListingsListResponseOut"] = t.struct(
        {
            "listings": t.array(t.proxy(renames["ListingOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListingsListResponseOut"])
    types["SplitApkMetadataIn"] = t.struct(
        {"isMasterSplit": t.boolean().optional(), "splitId": t.string().optional()}
    ).named(renames["SplitApkMetadataIn"])
    types["SplitApkMetadataOut"] = t.struct(
        {
            "isMasterSplit": t.boolean().optional(),
            "splitId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SplitApkMetadataOut"])
    types["DeviceSpecIn"] = t.struct(
        {
            "supportedAbis": t.array(t.string()).optional(),
            "screenDensity": t.integer().optional(),
            "supportedLocales": t.array(t.string()).optional(),
        }
    ).named(renames["DeviceSpecIn"])
    types["DeviceSpecOut"] = t.struct(
        {
            "supportedAbis": t.array(t.string()).optional(),
            "screenDensity": t.integer().optional(),
            "supportedLocales": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceSpecOut"])
    types["TrackTargetedCountryIn"] = t.struct(
        {"countryCode": t.string().optional()}
    ).named(renames["TrackTargetedCountryIn"])
    types["TrackTargetedCountryOut"] = t.struct(
        {
            "countryCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrackTargetedCountryOut"])
    types["ScreenDensityIn"] = t.struct(
        {"densityAlias": t.string().optional(), "densityDpi": t.integer().optional()}
    ).named(renames["ScreenDensityIn"])
    types["ScreenDensityOut"] = t.struct(
        {
            "densityAlias": t.string().optional(),
            "densityDpi": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScreenDensityOut"])
    types["AssetSliceSetIn"] = t.struct(
        {
            "apkDescription": t.array(t.proxy(renames["ApkDescriptionIn"])).optional(),
            "assetModuleMetadata": t.proxy(renames["AssetModuleMetadataIn"]).optional(),
        }
    ).named(renames["AssetSliceSetIn"])
    types["AssetSliceSetOut"] = t.struct(
        {
            "apkDescription": t.array(t.proxy(renames["ApkDescriptionOut"])).optional(),
            "assetModuleMetadata": t.proxy(
                renames["AssetModuleMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssetSliceSetOut"])
    types["MoneyIn"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "currencyCode": t.string().optional(),
            "units": t.string().optional(),
        }
    ).named(renames["MoneyIn"])
    types["MoneyOut"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "currencyCode": t.string().optional(),
            "units": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoneyOut"])
    types["SdkVersionTargetingIn"] = t.struct(
        {
            "alternatives": t.array(t.proxy(renames["SdkVersionIn"])).optional(),
            "value": t.array(t.proxy(renames["SdkVersionIn"])).optional(),
        }
    ).named(renames["SdkVersionTargetingIn"])
    types["SdkVersionTargetingOut"] = t.struct(
        {
            "alternatives": t.array(t.proxy(renames["SdkVersionOut"])).optional(),
            "value": t.array(t.proxy(renames["SdkVersionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SdkVersionTargetingOut"])
    types["ReviewIn"] = t.struct(
        {
            "authorName": t.string().optional(),
            "comments": t.array(t.proxy(renames["CommentIn"])).optional(),
            "reviewId": t.string().optional(),
        }
    ).named(renames["ReviewIn"])
    types["ReviewOut"] = t.struct(
        {
            "authorName": t.string().optional(),
            "comments": t.array(t.proxy(renames["CommentOut"])).optional(),
            "reviewId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReviewOut"])
    types["AbiIn"] = t.struct({"alias": t.string().optional()}).named(renames["AbiIn"])
    types["AbiOut"] = t.struct(
        {
            "alias": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AbiOut"])
    types["ProductPurchaseIn"] = t.struct(
        {
            "regionCode": t.string().optional(),
            "purchaseToken": t.string().optional(),
            "obfuscatedExternalProfileId": t.string().optional(),
            "obfuscatedExternalAccountId": t.string().optional(),
            "purchaseTimeMillis": t.string().optional(),
            "productId": t.string().optional(),
            "kind": t.string().optional(),
            "quantity": t.integer().optional(),
            "orderId": t.string().optional(),
            "purchaseState": t.integer().optional(),
            "consumptionState": t.integer().optional(),
            "developerPayload": t.string().optional(),
            "acknowledgementState": t.integer().optional(),
            "purchaseType": t.integer().optional(),
        }
    ).named(renames["ProductPurchaseIn"])
    types["ProductPurchaseOut"] = t.struct(
        {
            "regionCode": t.string().optional(),
            "purchaseToken": t.string().optional(),
            "obfuscatedExternalProfileId": t.string().optional(),
            "obfuscatedExternalAccountId": t.string().optional(),
            "purchaseTimeMillis": t.string().optional(),
            "productId": t.string().optional(),
            "kind": t.string().optional(),
            "quantity": t.integer().optional(),
            "orderId": t.string().optional(),
            "purchaseState": t.integer().optional(),
            "consumptionState": t.integer().optional(),
            "developerPayload": t.string().optional(),
            "acknowledgementState": t.integer().optional(),
            "purchaseType": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductPurchaseOut"])
    types["RefundExternalTransactionRequestIn"] = t.struct(
        {
            "partialRefund": t.proxy(renames["PartialRefundIn"]).optional(),
            "fullRefund": t.proxy(renames["FullRefundIn"]).optional(),
            "refundTime": t.string(),
        }
    ).named(renames["RefundExternalTransactionRequestIn"])
    types["RefundExternalTransactionRequestOut"] = t.struct(
        {
            "partialRefund": t.proxy(renames["PartialRefundOut"]).optional(),
            "fullRefund": t.proxy(renames["FullRefundOut"]).optional(),
            "refundTime": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RefundExternalTransactionRequestOut"])
    types["ApkTargetingIn"] = t.struct(
        {
            "screenDensityTargeting": t.proxy(
                renames["ScreenDensityTargetingIn"]
            ).optional(),
            "textureCompressionFormatTargeting": t.proxy(
                renames["TextureCompressionFormatTargetingIn"]
            ).optional(),
            "abiTargeting": t.proxy(renames["AbiTargetingIn"]).optional(),
            "languageTargeting": t.proxy(renames["LanguageTargetingIn"]).optional(),
            "multiAbiTargeting": t.proxy(renames["MultiAbiTargetingIn"]).optional(),
            "sdkVersionTargeting": t.proxy(renames["SdkVersionTargetingIn"]).optional(),
        }
    ).named(renames["ApkTargetingIn"])
    types["ApkTargetingOut"] = t.struct(
        {
            "screenDensityTargeting": t.proxy(
                renames["ScreenDensityTargetingOut"]
            ).optional(),
            "textureCompressionFormatTargeting": t.proxy(
                renames["TextureCompressionFormatTargetingOut"]
            ).optional(),
            "abiTargeting": t.proxy(renames["AbiTargetingOut"]).optional(),
            "languageTargeting": t.proxy(renames["LanguageTargetingOut"]).optional(),
            "multiAbiTargeting": t.proxy(renames["MultiAbiTargetingOut"]).optional(),
            "sdkVersionTargeting": t.proxy(
                renames["SdkVersionTargetingOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApkTargetingOut"])
    types["SystemApksListResponseIn"] = t.struct(
        {"variants": t.array(t.proxy(renames["VariantIn"])).optional()}
    ).named(renames["SystemApksListResponseIn"])
    types["SystemApksListResponseOut"] = t.struct(
        {
            "variants": t.array(t.proxy(renames["VariantOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SystemApksListResponseOut"])
    types["DeferredItemReplacementIn"] = t.struct(
        {"productId": t.string().optional()}
    ).named(renames["DeferredItemReplacementIn"])
    types["DeferredItemReplacementOut"] = t.struct(
        {
            "productId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeferredItemReplacementOut"])
    types["ActivateBasePlanRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ActivateBasePlanRequestIn"]
    )
    types["ActivateBasePlanRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ActivateBasePlanRequestOut"])
    types["UpgradeTargetingRuleIn"] = t.struct(
        {
            "oncePerUser": t.boolean().optional(),
            "scope": t.proxy(renames["TargetingRuleScopeIn"]),
            "billingPeriodDuration": t.string().optional(),
        }
    ).named(renames["UpgradeTargetingRuleIn"])
    types["UpgradeTargetingRuleOut"] = t.struct(
        {
            "oncePerUser": t.boolean().optional(),
            "scope": t.proxy(renames["TargetingRuleScopeOut"]),
            "billingPeriodDuration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpgradeTargetingRuleOut"])
    types["CommentIn"] = t.struct(
        {
            "userComment": t.proxy(renames["UserCommentIn"]).optional(),
            "developerComment": t.proxy(renames["DeveloperCommentIn"]).optional(),
        }
    ).named(renames["CommentIn"])
    types["CommentOut"] = t.struct(
        {
            "userComment": t.proxy(renames["UserCommentOut"]).optional(),
            "developerComment": t.proxy(renames["DeveloperCommentOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommentOut"])
    types["SubscriptionOfferTargetingIn"] = t.struct(
        {
            "upgradeRule": t.proxy(renames["UpgradeTargetingRuleIn"]).optional(),
            "acquisitionRule": t.proxy(
                renames["AcquisitionTargetingRuleIn"]
            ).optional(),
        }
    ).named(renames["SubscriptionOfferTargetingIn"])
    types["SubscriptionOfferTargetingOut"] = t.struct(
        {
            "upgradeRule": t.proxy(renames["UpgradeTargetingRuleOut"]).optional(),
            "acquisitionRule": t.proxy(
                renames["AcquisitionTargetingRuleOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscriptionOfferTargetingOut"])
    types["PrepaidPlanIn"] = t.struct(
        {"allowExtendAfterTime": t.string().optional()}
    ).named(renames["PrepaidPlanIn"])
    types["PrepaidPlanOut"] = t.struct(
        {
            "allowExtendAfterTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrepaidPlanOut"])
    types["ArchiveSubscriptionRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ArchiveSubscriptionRequestIn"])
    types["ArchiveSubscriptionRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ArchiveSubscriptionRequestOut"])
    types["GeneratedAssetPackSliceIn"] = t.struct(
        {
            "version": t.string().optional(),
            "sliceId": t.string().optional(),
            "moduleName": t.string().optional(),
            "downloadId": t.string().optional(),
        }
    ).named(renames["GeneratedAssetPackSliceIn"])
    types["GeneratedAssetPackSliceOut"] = t.struct(
        {
            "version": t.string().optional(),
            "sliceId": t.string().optional(),
            "moduleName": t.string().optional(),
            "downloadId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GeneratedAssetPackSliceOut"])
    types["LanguageTargetingIn"] = t.struct(
        {
            "alternatives": t.array(t.string()).optional(),
            "value": t.array(t.string()).optional(),
        }
    ).named(renames["LanguageTargetingIn"])
    types["LanguageTargetingOut"] = t.struct(
        {
            "alternatives": t.array(t.string()).optional(),
            "value": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LanguageTargetingOut"])
    types["SubscriptionOfferPhaseIn"] = t.struct(
        {
            "regionalConfigs": t.array(
                t.proxy(renames["RegionalSubscriptionOfferPhaseConfigIn"])
            ),
            "recurrenceCount": t.integer(),
            "otherRegionsConfig": t.proxy(
                renames["OtherRegionsSubscriptionOfferPhaseConfigIn"]
            ).optional(),
            "duration": t.string(),
        }
    ).named(renames["SubscriptionOfferPhaseIn"])
    types["SubscriptionOfferPhaseOut"] = t.struct(
        {
            "regionalConfigs": t.array(
                t.proxy(renames["RegionalSubscriptionOfferPhaseConfigOut"])
            ),
            "recurrenceCount": t.integer(),
            "otherRegionsConfig": t.proxy(
                renames["OtherRegionsSubscriptionOfferPhaseConfigOut"]
            ).optional(),
            "duration": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscriptionOfferPhaseOut"])
    types["OfferTagIn"] = t.struct({"tag": t.string().optional()}).named(
        renames["OfferTagIn"]
    )
    types["OfferTagOut"] = t.struct(
        {
            "tag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OfferTagOut"])
    types["ApksListResponseIn"] = t.struct(
        {
            "apks": t.array(t.proxy(renames["ApkIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ApksListResponseIn"])
    types["ApksListResponseOut"] = t.struct(
        {
            "apks": t.array(t.proxy(renames["ApkOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApksListResponseOut"])
    types["SubscriptionPurchaseV2In"] = t.struct(
        {
            "externalAccountIdentifiers": t.proxy(
                renames["ExternalAccountIdentifiersIn"]
            ).optional(),
            "canceledStateContext": t.proxy(
                renames["CanceledStateContextIn"]
            ).optional(),
            "acknowledgementState": t.string().optional(),
            "startTime": t.string().optional(),
            "linkedPurchaseToken": t.string().optional(),
            "pausedStateContext": t.proxy(renames["PausedStateContextIn"]).optional(),
            "kind": t.string().optional(),
            "regionCode": t.string().optional(),
            "subscribeWithGoogleInfo": t.proxy(
                renames["SubscribeWithGoogleInfoIn"]
            ).optional(),
            "lineItems": t.array(
                t.proxy(renames["SubscriptionPurchaseLineItemIn"])
            ).optional(),
            "subscriptionState": t.string().optional(),
            "testPurchase": t.proxy(renames["TestPurchaseIn"]).optional(),
            "latestOrderId": t.string().optional(),
        }
    ).named(renames["SubscriptionPurchaseV2In"])
    types["SubscriptionPurchaseV2Out"] = t.struct(
        {
            "externalAccountIdentifiers": t.proxy(
                renames["ExternalAccountIdentifiersOut"]
            ).optional(),
            "canceledStateContext": t.proxy(
                renames["CanceledStateContextOut"]
            ).optional(),
            "acknowledgementState": t.string().optional(),
            "startTime": t.string().optional(),
            "linkedPurchaseToken": t.string().optional(),
            "pausedStateContext": t.proxy(renames["PausedStateContextOut"]).optional(),
            "kind": t.string().optional(),
            "regionCode": t.string().optional(),
            "subscribeWithGoogleInfo": t.proxy(
                renames["SubscribeWithGoogleInfoOut"]
            ).optional(),
            "lineItems": t.array(
                t.proxy(renames["SubscriptionPurchaseLineItemOut"])
            ).optional(),
            "subscriptionState": t.string().optional(),
            "testPurchase": t.proxy(renames["TestPurchaseOut"]).optional(),
            "latestOrderId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscriptionPurchaseV2Out"])
    types["PageInfoIn"] = t.struct(
        {
            "startIndex": t.integer().optional(),
            "resultPerPage": t.integer().optional(),
            "totalResults": t.integer().optional(),
        }
    ).named(renames["PageInfoIn"])
    types["PageInfoOut"] = t.struct(
        {
            "startIndex": t.integer().optional(),
            "resultPerPage": t.integer().optional(),
            "totalResults": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PageInfoOut"])
    types["DeobfuscationFilesUploadResponseIn"] = t.struct(
        {"deobfuscationFile": t.proxy(renames["DeobfuscationFileIn"]).optional()}
    ).named(renames["DeobfuscationFilesUploadResponseIn"])
    types["DeobfuscationFilesUploadResponseOut"] = t.struct(
        {
            "deobfuscationFile": t.proxy(renames["DeobfuscationFileOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeobfuscationFilesUploadResponseOut"])
    types["AutoRenewingPlanIn"] = t.struct(
        {
            "autoRenewEnabled": t.boolean().optional(),
            "priceChangeDetails": t.proxy(
                renames["SubscriptionItemPriceChangeDetailsIn"]
            ).optional(),
        }
    ).named(renames["AutoRenewingPlanIn"])
    types["AutoRenewingPlanOut"] = t.struct(
        {
            "autoRenewEnabled": t.boolean().optional(),
            "priceChangeDetails": t.proxy(
                renames["SubscriptionItemPriceChangeDetailsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutoRenewingPlanOut"])
    types["AssetModuleMetadataIn"] = t.struct(
        {"name": t.string().optional(), "deliveryType": t.string().optional()}
    ).named(renames["AssetModuleMetadataIn"])
    types["AssetModuleMetadataOut"] = t.struct(
        {
            "name": t.string().optional(),
            "deliveryType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssetModuleMetadataOut"])
    types["PartialRefundIn"] = t.struct(
        {"refundId": t.string(), "refundPreTaxAmount": t.proxy(renames["PriceIn"])}
    ).named(renames["PartialRefundIn"])
    types["PartialRefundOut"] = t.struct(
        {
            "refundId": t.string(),
            "refundPreTaxAmount": t.proxy(renames["PriceOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartialRefundOut"])
    types["TargetingRuleScopeIn"] = t.struct(
        {"specificSubscriptionInApp": t.string().optional()}
    ).named(renames["TargetingRuleScopeIn"])
    types["TargetingRuleScopeOut"] = t.struct(
        {
            "specificSubscriptionInApp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetingRuleScopeOut"])
    types["UserCountriesTargetingIn"] = t.struct(
        {
            "countryCodes": t.array(t.string()).optional(),
            "exclude": t.boolean().optional(),
        }
    ).named(renames["UserCountriesTargetingIn"])
    types["UserCountriesTargetingOut"] = t.struct(
        {
            "countryCodes": t.array(t.string()).optional(),
            "exclude": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserCountriesTargetingOut"])
    types["TargetingInfoIn"] = t.struct(
        {
            "variant": t.array(t.proxy(renames["SplitApkVariantIn"])).optional(),
            "packageName": t.string().optional(),
            "assetSliceSet": t.array(t.proxy(renames["AssetSliceSetIn"])).optional(),
        }
    ).named(renames["TargetingInfoIn"])
    types["TargetingInfoOut"] = t.struct(
        {
            "variant": t.array(t.proxy(renames["SplitApkVariantOut"])).optional(),
            "packageName": t.string().optional(),
            "assetSliceSet": t.array(t.proxy(renames["AssetSliceSetOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetingInfoOut"])
    types["TextureCompressionFormatIn"] = t.struct(
        {"alias": t.string().optional()}
    ).named(renames["TextureCompressionFormatIn"])
    types["TextureCompressionFormatOut"] = t.struct(
        {
            "alias": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextureCompressionFormatOut"])
    types["DeviceIdIn"] = t.struct(
        {"buildDevice": t.string().optional(), "buildBrand": t.string().optional()}
    ).named(renames["DeviceIdIn"])
    types["DeviceIdOut"] = t.struct(
        {
            "buildDevice": t.string().optional(),
            "buildBrand": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceIdOut"])
    types["StandaloneApkMetadataIn"] = t.struct(
        {"fusedModuleName": t.array(t.string()).optional()}
    ).named(renames["StandaloneApkMetadataIn"])
    types["StandaloneApkMetadataOut"] = t.struct(
        {
            "fusedModuleName": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StandaloneApkMetadataOut"])
    types["ApkDescriptionIn"] = t.struct(
        {
            "instantApkMetadata": t.proxy(renames["SplitApkMetadataIn"]).optional(),
            "assetSliceMetadata": t.proxy(renames["SplitApkMetadataIn"]).optional(),
            "standaloneApkMetadata": t.proxy(
                renames["StandaloneApkMetadataIn"]
            ).optional(),
            "targeting": t.proxy(renames["ApkTargetingIn"]).optional(),
            "splitApkMetadata": t.proxy(renames["SplitApkMetadataIn"]).optional(),
            "path": t.string().optional(),
        }
    ).named(renames["ApkDescriptionIn"])
    types["ApkDescriptionOut"] = t.struct(
        {
            "instantApkMetadata": t.proxy(renames["SplitApkMetadataOut"]).optional(),
            "assetSliceMetadata": t.proxy(renames["SplitApkMetadataOut"]).optional(),
            "standaloneApkMetadata": t.proxy(
                renames["StandaloneApkMetadataOut"]
            ).optional(),
            "targeting": t.proxy(renames["ApkTargetingOut"]).optional(),
            "splitApkMetadata": t.proxy(renames["SplitApkMetadataOut"]).optional(),
            "path": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApkDescriptionOut"])
    types["ApksAddExternallyHostedResponseIn"] = t.struct(
        {"externallyHostedApk": t.proxy(renames["ExternallyHostedApkIn"]).optional()}
    ).named(renames["ApksAddExternallyHostedResponseIn"])
    types["ApksAddExternallyHostedResponseOut"] = t.struct(
        {
            "externallyHostedApk": t.proxy(
                renames["ExternallyHostedApkOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApksAddExternallyHostedResponseOut"])
    types["ReviewReplyResultIn"] = t.struct(
        {
            "replyText": t.string().optional(),
            "lastEdited": t.proxy(renames["TimestampIn"]).optional(),
        }
    ).named(renames["ReviewReplyResultIn"])
    types["ReviewReplyResultOut"] = t.struct(
        {
            "replyText": t.string().optional(),
            "lastEdited": t.proxy(renames["TimestampOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReviewReplyResultOut"])
    types["DeviceTierConfigIn"] = t.struct(
        {
            "userCountrySets": t.array(t.proxy(renames["UserCountrySetIn"])).optional(),
            "deviceGroups": t.array(t.proxy(renames["DeviceGroupIn"])).optional(),
            "deviceTierSet": t.proxy(renames["DeviceTierSetIn"]).optional(),
        }
    ).named(renames["DeviceTierConfigIn"])
    types["DeviceTierConfigOut"] = t.struct(
        {
            "userCountrySets": t.array(
                t.proxy(renames["UserCountrySetOut"])
            ).optional(),
            "deviceGroups": t.array(t.proxy(renames["DeviceGroupOut"])).optional(),
            "deviceTierSet": t.proxy(renames["DeviceTierSetOut"]).optional(),
            "deviceTierConfigId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceTierConfigOut"])
    types["PriceIn"] = t.struct(
        {"priceMicros": t.string().optional(), "currency": t.string().optional()}
    ).named(renames["PriceIn"])
    types["PriceOut"] = t.struct(
        {
            "priceMicros": t.string().optional(),
            "currency": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PriceOut"])
    types["SplitApkVariantIn"] = t.struct(
        {
            "variantNumber": t.integer().optional(),
            "apkSet": t.array(t.proxy(renames["ApkSetIn"])).optional(),
            "targeting": t.proxy(renames["VariantTargetingIn"]).optional(),
        }
    ).named(renames["SplitApkVariantIn"])
    types["SplitApkVariantOut"] = t.struct(
        {
            "variantNumber": t.integer().optional(),
            "apkSet": t.array(t.proxy(renames["ApkSetOut"])).optional(),
            "targeting": t.proxy(renames["VariantTargetingOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SplitApkVariantOut"])
    types["SubscriptionDeferralInfoIn"] = t.struct(
        {
            "desiredExpiryTimeMillis": t.string().optional(),
            "expectedExpiryTimeMillis": t.string().optional(),
        }
    ).named(renames["SubscriptionDeferralInfoIn"])
    types["SubscriptionDeferralInfoOut"] = t.struct(
        {
            "desiredExpiryTimeMillis": t.string().optional(),
            "expectedExpiryTimeMillis": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscriptionDeferralInfoOut"])
    types["FullRefundIn"] = t.struct({"_": t.string().optional()}).named(
        renames["FullRefundIn"]
    )
    types["FullRefundOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["FullRefundOut"])
    types["ConvertRegionPricesResponseIn"] = t.struct(
        {
            "convertedRegionPrices": t.struct({"_": t.string().optional()}).optional(),
            "convertedOtherRegionsPrice": t.proxy(
                renames["ConvertedOtherRegionsPriceIn"]
            ).optional(),
        }
    ).named(renames["ConvertRegionPricesResponseIn"])
    types["ConvertRegionPricesResponseOut"] = t.struct(
        {
            "convertedRegionPrices": t.struct({"_": t.string().optional()}).optional(),
            "convertedOtherRegionsPrice": t.proxy(
                renames["ConvertedOtherRegionsPriceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConvertRegionPricesResponseOut"])
    types["ApkIn"] = t.struct(
        {
            "binary": t.proxy(renames["ApkBinaryIn"]).optional(),
            "versionCode": t.integer().optional(),
        }
    ).named(renames["ApkIn"])
    types["ApkOut"] = t.struct(
        {
            "binary": t.proxy(renames["ApkBinaryOut"]).optional(),
            "versionCode": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApkOut"])
    types["ApksAddExternallyHostedRequestIn"] = t.struct(
        {"externallyHostedApk": t.proxy(renames["ExternallyHostedApkIn"]).optional()}
    ).named(renames["ApksAddExternallyHostedRequestIn"])
    types["ApksAddExternallyHostedRequestOut"] = t.struct(
        {
            "externallyHostedApk": t.proxy(
                renames["ExternallyHostedApkOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApksAddExternallyHostedRequestOut"])
    types["ProductPurchasesAcknowledgeRequestIn"] = t.struct(
        {"developerPayload": t.string().optional()}
    ).named(renames["ProductPurchasesAcknowledgeRequestIn"])
    types["ProductPurchasesAcknowledgeRequestOut"] = t.struct(
        {
            "developerPayload": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductPurchasesAcknowledgeRequestOut"])
    types["DeactivateBasePlanRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeactivateBasePlanRequestIn"]
    )
    types["DeactivateBasePlanRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeactivateBasePlanRequestOut"])
    types["ExternallyHostedApkIn"] = t.struct(
        {
            "applicationLabel": t.string().optional(),
            "versionCode": t.integer().optional(),
            "maximumSdk": t.integer().optional(),
            "iconBase64": t.string().optional(),
            "packageName": t.string().optional(),
            "nativeCodes": t.array(t.string()).optional(),
            "usesPermissions": t.array(t.proxy(renames["UsesPermissionIn"])).optional(),
            "versionName": t.string().optional(),
            "certificateBase64s": t.array(t.string()).optional(),
            "fileSha256Base64": t.string().optional(),
            "fileSize": t.string().optional(),
            "externallyHostedUrl": t.string().optional(),
            "usesFeatures": t.array(t.string()).optional(),
            "fileSha1Base64": t.string().optional(),
            "minimumSdk": t.integer().optional(),
        }
    ).named(renames["ExternallyHostedApkIn"])
    types["ExternallyHostedApkOut"] = t.struct(
        {
            "applicationLabel": t.string().optional(),
            "versionCode": t.integer().optional(),
            "maximumSdk": t.integer().optional(),
            "iconBase64": t.string().optional(),
            "packageName": t.string().optional(),
            "nativeCodes": t.array(t.string()).optional(),
            "usesPermissions": t.array(
                t.proxy(renames["UsesPermissionOut"])
            ).optional(),
            "versionName": t.string().optional(),
            "certificateBase64s": t.array(t.string()).optional(),
            "fileSha256Base64": t.string().optional(),
            "fileSize": t.string().optional(),
            "externallyHostedUrl": t.string().optional(),
            "usesFeatures": t.array(t.string()).optional(),
            "fileSha1Base64": t.string().optional(),
            "minimumSdk": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExternallyHostedApkOut"])
    types["OneTimeExternalTransactionIn"] = t.struct(
        {"externalTransactionToken": t.string().optional()}
    ).named(renames["OneTimeExternalTransactionIn"])
    types["OneTimeExternalTransactionOut"] = t.struct(
        {
            "externalTransactionToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OneTimeExternalTransactionOut"])
    types["ApkSetIn"] = t.struct(
        {
            "apkDescription": t.array(t.proxy(renames["ApkDescriptionIn"])).optional(),
            "moduleMetadata": t.proxy(renames["ModuleMetadataIn"]).optional(),
        }
    ).named(renames["ApkSetIn"])
    types["ApkSetOut"] = t.struct(
        {
            "apkDescription": t.array(t.proxy(renames["ApkDescriptionOut"])).optional(),
            "moduleMetadata": t.proxy(renames["ModuleMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApkSetOut"])
    types["UsesPermissionIn"] = t.struct(
        {"maxSdkVersion": t.integer().optional(), "name": t.string().optional()}
    ).named(renames["UsesPermissionIn"])
    types["UsesPermissionOut"] = t.struct(
        {
            "maxSdkVersion": t.integer().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UsesPermissionOut"])
    types["TestersIn"] = t.struct(
        {"googleGroups": t.array(t.string()).optional()}
    ).named(renames["TestersIn"])
    types["TestersOut"] = t.struct(
        {
            "googleGroups": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestersOut"])
    types["IntroductoryPriceInfoIn"] = t.struct(
        {
            "introductoryPriceCurrencyCode": t.string().optional(),
            "introductoryPriceAmountMicros": t.string().optional(),
            "introductoryPricePeriod": t.string().optional(),
            "introductoryPriceCycles": t.integer().optional(),
        }
    ).named(renames["IntroductoryPriceInfoIn"])
    types["IntroductoryPriceInfoOut"] = t.struct(
        {
            "introductoryPriceCurrencyCode": t.string().optional(),
            "introductoryPriceAmountMicros": t.string().optional(),
            "introductoryPricePeriod": t.string().optional(),
            "introductoryPriceCycles": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntroductoryPriceInfoOut"])
    types["DeviceFeatureIn"] = t.struct(
        {"featureVersion": t.integer().optional(), "featureName": t.string().optional()}
    ).named(renames["DeviceFeatureIn"])
    types["DeviceFeatureOut"] = t.struct(
        {
            "featureVersion": t.integer().optional(),
            "featureName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceFeatureOut"])
    types["GeneratedSplitApkIn"] = t.struct(
        {
            "variantId": t.integer().optional(),
            "downloadId": t.string().optional(),
            "moduleName": t.string().optional(),
            "splitId": t.string().optional(),
        }
    ).named(renames["GeneratedSplitApkIn"])
    types["GeneratedSplitApkOut"] = t.struct(
        {
            "variantId": t.integer().optional(),
            "downloadId": t.string().optional(),
            "moduleName": t.string().optional(),
            "splitId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GeneratedSplitApkOut"])
    types["ExternalAccountIdentifiersIn"] = t.struct(
        {
            "obfuscatedExternalAccountId": t.string().optional(),
            "externalAccountId": t.string().optional(),
            "obfuscatedExternalProfileId": t.string().optional(),
        }
    ).named(renames["ExternalAccountIdentifiersIn"])
    types["ExternalAccountIdentifiersOut"] = t.struct(
        {
            "obfuscatedExternalAccountId": t.string().optional(),
            "externalAccountId": t.string().optional(),
            "obfuscatedExternalProfileId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExternalAccountIdentifiersOut"])
    types["DeviceSelectorIn"] = t.struct(
        {
            "includedDeviceIds": t.array(t.proxy(renames["DeviceIdIn"])).optional(),
            "requiredSystemFeatures": t.array(
                t.proxy(renames["SystemFeatureIn"])
            ).optional(),
            "excludedDeviceIds": t.array(t.proxy(renames["DeviceIdIn"])).optional(),
            "deviceRam": t.proxy(renames["DeviceRamIn"]).optional(),
            "forbiddenSystemFeatures": t.array(
                t.proxy(renames["SystemFeatureIn"])
            ).optional(),
        }
    ).named(renames["DeviceSelectorIn"])
    types["DeviceSelectorOut"] = t.struct(
        {
            "includedDeviceIds": t.array(t.proxy(renames["DeviceIdOut"])).optional(),
            "requiredSystemFeatures": t.array(
                t.proxy(renames["SystemFeatureOut"])
            ).optional(),
            "excludedDeviceIds": t.array(t.proxy(renames["DeviceIdOut"])).optional(),
            "deviceRam": t.proxy(renames["DeviceRamOut"]).optional(),
            "forbiddenSystemFeatures": t.array(
                t.proxy(renames["SystemFeatureOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceSelectorOut"])
    types["ListingIn"] = t.struct(
        {
            "fullDescription": t.string().optional(),
            "title": t.string().optional(),
            "shortDescription": t.string().optional(),
            "language": t.string().optional(),
            "video": t.string().optional(),
        }
    ).named(renames["ListingIn"])
    types["ListingOut"] = t.struct(
        {
            "fullDescription": t.string().optional(),
            "title": t.string().optional(),
            "shortDescription": t.string().optional(),
            "language": t.string().optional(),
            "video": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListingOut"])
    types["BundlesListResponseIn"] = t.struct(
        {
            "bundles": t.array(t.proxy(renames["BundleIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["BundlesListResponseIn"])
    types["BundlesListResponseOut"] = t.struct(
        {
            "bundles": t.array(t.proxy(renames["BundleOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BundlesListResponseOut"])
    types["InternalAppSharingArtifactIn"] = t.struct(
        {
            "sha256": t.string().optional(),
            "certificateFingerprint": t.string().optional(),
            "downloadUrl": t.string().optional(),
        }
    ).named(renames["InternalAppSharingArtifactIn"])
    types["InternalAppSharingArtifactOut"] = t.struct(
        {
            "sha256": t.string().optional(),
            "certificateFingerprint": t.string().optional(),
            "downloadUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InternalAppSharingArtifactOut"])
    types["OtherRegionsSubscriptionOfferPhasePricesIn"] = t.struct(
        {
            "eurPrice": t.proxy(renames["MoneyIn"]),
            "usdPrice": t.proxy(renames["MoneyIn"]),
        }
    ).named(renames["OtherRegionsSubscriptionOfferPhasePricesIn"])
    types["OtherRegionsSubscriptionOfferPhasePricesOut"] = t.struct(
        {
            "eurPrice": t.proxy(renames["MoneyOut"]),
            "usdPrice": t.proxy(renames["MoneyOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OtherRegionsSubscriptionOfferPhasePricesOut"])
    types["GeneratedApksListResponseIn"] = t.struct(
        {
            "generatedApks": t.array(
                t.proxy(renames["GeneratedApksPerSigningKeyIn"])
            ).optional()
        }
    ).named(renames["GeneratedApksListResponseIn"])
    types["GeneratedApksListResponseOut"] = t.struct(
        {
            "generatedApks": t.array(
                t.proxy(renames["GeneratedApksPerSigningKeyOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GeneratedApksListResponseOut"])
    types["ReviewsReplyResponseIn"] = t.struct(
        {"result": t.proxy(renames["ReviewReplyResultIn"]).optional()}
    ).named(renames["ReviewsReplyResponseIn"])
    types["ReviewsReplyResponseOut"] = t.struct(
        {
            "result": t.proxy(renames["ReviewReplyResultOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReviewsReplyResponseOut"])
    types["DeviceRamIn"] = t.struct(
        {"maxBytes": t.string().optional(), "minBytes": t.string().optional()}
    ).named(renames["DeviceRamIn"])
    types["DeviceRamOut"] = t.struct(
        {
            "maxBytes": t.string().optional(),
            "minBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceRamOut"])
    types["AppEditIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AppEditIn"]
    )
    types["AppEditOut"] = t.struct(
        {
            "expiryTimeSeconds": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppEditOut"])
    types["CanceledStateContextIn"] = t.struct(
        {
            "systemInitiatedCancellation": t.proxy(
                renames["SystemInitiatedCancellationIn"]
            ).optional(),
            "userInitiatedCancellation": t.proxy(
                renames["UserInitiatedCancellationIn"]
            ).optional(),
            "developerInitiatedCancellation": t.proxy(
                renames["DeveloperInitiatedCancellationIn"]
            ).optional(),
            "replacementCancellation": t.proxy(
                renames["ReplacementCancellationIn"]
            ).optional(),
        }
    ).named(renames["CanceledStateContextIn"])
    types["CanceledStateContextOut"] = t.struct(
        {
            "systemInitiatedCancellation": t.proxy(
                renames["SystemInitiatedCancellationOut"]
            ).optional(),
            "userInitiatedCancellation": t.proxy(
                renames["UserInitiatedCancellationOut"]
            ).optional(),
            "developerInitiatedCancellation": t.proxy(
                renames["DeveloperInitiatedCancellationOut"]
            ).optional(),
            "replacementCancellation": t.proxy(
                renames["ReplacementCancellationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CanceledStateContextOut"])
    types["AppDetailsIn"] = t.struct(
        {
            "contactPhone": t.string().optional(),
            "contactWebsite": t.string().optional(),
            "contactEmail": t.string().optional(),
            "defaultLanguage": t.string().optional(),
        }
    ).named(renames["AppDetailsIn"])
    types["AppDetailsOut"] = t.struct(
        {
            "contactPhone": t.string().optional(),
            "contactWebsite": t.string().optional(),
            "contactEmail": t.string().optional(),
            "defaultLanguage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppDetailsOut"])
    types["SubscriptionPriceChangeIn"] = t.struct(
        {
            "state": t.integer().optional(),
            "newPrice": t.proxy(renames["PriceIn"]).optional(),
        }
    ).named(renames["SubscriptionPriceChangeIn"])
    types["SubscriptionPriceChangeOut"] = t.struct(
        {
            "state": t.integer().optional(),
            "newPrice": t.proxy(renames["PriceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscriptionPriceChangeOut"])
    types["ImagesUploadResponseIn"] = t.struct(
        {"image": t.proxy(renames["ImageIn"]).optional()}
    ).named(renames["ImagesUploadResponseIn"])
    types["ImagesUploadResponseOut"] = t.struct(
        {
            "image": t.proxy(renames["ImageOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImagesUploadResponseOut"])
    types["ListUsersResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "users": t.array(t.proxy(renames["UserIn"])).optional(),
        }
    ).named(renames["ListUsersResponseIn"])
    types["ListUsersResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "users": t.array(t.proxy(renames["UserOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListUsersResponseOut"])
    types["SubscriptionTaxAndComplianceSettingsIn"] = t.struct(
        {
            "eeaWithdrawalRightType": t.string().optional(),
            "taxRateInfoByRegionCode": t.struct(
                {"_": t.string().optional()}
            ).optional(),
        }
    ).named(renames["SubscriptionTaxAndComplianceSettingsIn"])
    types["SubscriptionTaxAndComplianceSettingsOut"] = t.struct(
        {
            "eeaWithdrawalRightType": t.string().optional(),
            "taxRateInfoByRegionCode": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscriptionTaxAndComplianceSettingsOut"])
    types["SubscriptionItemPriceChangeDetailsIn"] = t.struct(
        {
            "priceChangeMode": t.string().optional(),
            "priceChangeState": t.string().optional(),
            "expectedNewPriceChargeTime": t.string().optional(),
            "newPrice": t.proxy(renames["MoneyIn"]).optional(),
        }
    ).named(renames["SubscriptionItemPriceChangeDetailsIn"])
    types["SubscriptionItemPriceChangeDetailsOut"] = t.struct(
        {
            "priceChangeMode": t.string().optional(),
            "priceChangeState": t.string().optional(),
            "expectedNewPriceChargeTime": t.string().optional(),
            "newPrice": t.proxy(renames["MoneyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscriptionItemPriceChangeDetailsOut"])
    types["ScreenDensityTargetingIn"] = t.struct(
        {
            "value": t.array(t.proxy(renames["ScreenDensityIn"])).optional(),
            "alternatives": t.array(t.proxy(renames["ScreenDensityIn"])).optional(),
        }
    ).named(renames["ScreenDensityTargetingIn"])
    types["ScreenDensityTargetingOut"] = t.struct(
        {
            "value": t.array(t.proxy(renames["ScreenDensityOut"])).optional(),
            "alternatives": t.array(t.proxy(renames["ScreenDensityOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScreenDensityTargetingOut"])
    types["TextureCompressionFormatTargetingIn"] = t.struct(
        {
            "alternatives": t.array(
                t.proxy(renames["TextureCompressionFormatIn"])
            ).optional(),
            "value": t.array(t.proxy(renames["TextureCompressionFormatIn"])).optional(),
        }
    ).named(renames["TextureCompressionFormatTargetingIn"])
    types["TextureCompressionFormatTargetingOut"] = t.struct(
        {
            "alternatives": t.array(
                t.proxy(renames["TextureCompressionFormatOut"])
            ).optional(),
            "value": t.array(
                t.proxy(renames["TextureCompressionFormatOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextureCompressionFormatTargetingOut"])
    types["AbiTargetingIn"] = t.struct(
        {
            "alternatives": t.array(t.proxy(renames["AbiIn"])).optional(),
            "value": t.array(t.proxy(renames["AbiIn"])).optional(),
        }
    ).named(renames["AbiTargetingIn"])
    types["AbiTargetingOut"] = t.struct(
        {
            "alternatives": t.array(t.proxy(renames["AbiOut"])).optional(),
            "value": t.array(t.proxy(renames["AbiOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AbiTargetingOut"])
    types["TrackReleaseIn"] = t.struct(
        {
            "status": t.string().optional(),
            "userFraction": t.number().optional(),
            "releaseNotes": t.array(t.proxy(renames["LocalizedTextIn"])).optional(),
            "countryTargeting": t.proxy(renames["CountryTargetingIn"]).optional(),
            "inAppUpdatePriority": t.integer().optional(),
            "name": t.string().optional(),
            "versionCodes": t.array(t.string()).optional(),
        }
    ).named(renames["TrackReleaseIn"])
    types["TrackReleaseOut"] = t.struct(
        {
            "status": t.string().optional(),
            "userFraction": t.number().optional(),
            "releaseNotes": t.array(t.proxy(renames["LocalizedTextOut"])).optional(),
            "countryTargeting": t.proxy(renames["CountryTargetingOut"]).optional(),
            "inAppUpdatePriority": t.integer().optional(),
            "name": t.string().optional(),
            "versionCodes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrackReleaseOut"])
    types["RegionsVersionIn"] = t.struct({"version": t.string()}).named(
        renames["RegionsVersionIn"]
    )
    types["RegionsVersionOut"] = t.struct(
        {"version": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RegionsVersionOut"])
    types["ListDeviceTierConfigsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "deviceTierConfigs": t.array(
                t.proxy(renames["DeviceTierConfigIn"])
            ).optional(),
        }
    ).named(renames["ListDeviceTierConfigsResponseIn"])
    types["ListDeviceTierConfigsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "deviceTierConfigs": t.array(
                t.proxy(renames["DeviceTierConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDeviceTierConfigsResponseOut"])
    types["InAppProductIn"] = t.struct(
        {
            "sku": t.string().optional(),
            "managedProductTaxesAndComplianceSettings": t.proxy(
                renames["ManagedProductTaxAndComplianceSettingsIn"]
            ).optional(),
            "defaultLanguage": t.string().optional(),
            "status": t.string().optional(),
            "packageName": t.string().optional(),
            "subscriptionTaxesAndComplianceSettings": t.proxy(
                renames["SubscriptionTaxAndComplianceSettingsIn"]
            ).optional(),
            "subscriptionPeriod": t.string().optional(),
            "defaultPrice": t.proxy(renames["PriceIn"]).optional(),
            "purchaseType": t.string().optional(),
            "trialPeriod": t.string().optional(),
            "gracePeriod": t.string().optional(),
            "prices": t.struct({"_": t.string().optional()}).optional(),
            "listings": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["InAppProductIn"])
    types["InAppProductOut"] = t.struct(
        {
            "sku": t.string().optional(),
            "managedProductTaxesAndComplianceSettings": t.proxy(
                renames["ManagedProductTaxAndComplianceSettingsOut"]
            ).optional(),
            "defaultLanguage": t.string().optional(),
            "status": t.string().optional(),
            "packageName": t.string().optional(),
            "subscriptionTaxesAndComplianceSettings": t.proxy(
                renames["SubscriptionTaxAndComplianceSettingsOut"]
            ).optional(),
            "subscriptionPeriod": t.string().optional(),
            "defaultPrice": t.proxy(renames["PriceOut"]).optional(),
            "purchaseType": t.string().optional(),
            "trialPeriod": t.string().optional(),
            "gracePeriod": t.string().optional(),
            "prices": t.struct({"_": t.string().optional()}).optional(),
            "listings": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InAppProductOut"])
    types["ExternalSubscriptionIn"] = t.struct({"subscriptionType": t.string()}).named(
        renames["ExternalSubscriptionIn"]
    )
    types["ExternalSubscriptionOut"] = t.struct(
        {
            "subscriptionType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExternalSubscriptionOut"])
    types["PausedStateContextIn"] = t.struct(
        {"autoResumeTime": t.string().optional()}
    ).named(renames["PausedStateContextIn"])
    types["PausedStateContextOut"] = t.struct(
        {
            "autoResumeTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PausedStateContextOut"])
    types["TimestampIn"] = t.struct(
        {"seconds": t.string().optional(), "nanos": t.integer().optional()}
    ).named(renames["TimestampIn"])
    types["TimestampOut"] = t.struct(
        {
            "seconds": t.string().optional(),
            "nanos": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimestampOut"])
    types["RegionalSubscriptionOfferConfigIn"] = t.struct(
        {"newSubscriberAvailability": t.boolean().optional(), "regionCode": t.string()}
    ).named(renames["RegionalSubscriptionOfferConfigIn"])
    types["RegionalSubscriptionOfferConfigOut"] = t.struct(
        {
            "newSubscriberAvailability": t.boolean().optional(),
            "regionCode": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegionalSubscriptionOfferConfigOut"])
    types["CancelSurveyResultIn"] = t.struct(
        {"reasonUserInput": t.string().optional(), "reason": t.string().optional()}
    ).named(renames["CancelSurveyResultIn"])
    types["CancelSurveyResultOut"] = t.struct(
        {
            "reasonUserInput": t.string().optional(),
            "reason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CancelSurveyResultOut"])
    types["SubscriptionPurchaseIn"] = t.struct(
        {
            "startTimeMillis": t.string().optional(),
            "paymentState": t.integer().optional(),
            "obfuscatedExternalAccountId": t.string().optional(),
            "cancelReason": t.integer().optional(),
            "kind": t.string().optional(),
            "developerPayload": t.string().optional(),
            "linkedPurchaseToken": t.string().optional(),
            "countryCode": t.string().optional(),
            "acknowledgementState": t.integer().optional(),
            "priceCurrencyCode": t.string().optional(),
            "profileId": t.string().optional(),
            "purchaseType": t.integer().optional(),
            "priceChange": t.proxy(renames["SubscriptionPriceChangeIn"]).optional(),
            "obfuscatedExternalProfileId": t.string().optional(),
            "promotionCode": t.string().optional(),
            "expiryTimeMillis": t.string().optional(),
            "givenName": t.string().optional(),
            "userCancellationTimeMillis": t.string().optional(),
            "externalAccountId": t.string().optional(),
            "autoRenewing": t.boolean().optional(),
            "orderId": t.string().optional(),
            "cancelSurveyResult": t.proxy(
                renames["SubscriptionCancelSurveyResultIn"]
            ).optional(),
            "priceAmountMicros": t.string().optional(),
            "introductoryPriceInfo": t.proxy(
                renames["IntroductoryPriceInfoIn"]
            ).optional(),
            "profileName": t.string().optional(),
            "emailAddress": t.string().optional(),
            "familyName": t.string().optional(),
            "promotionType": t.integer().optional(),
            "autoResumeTimeMillis": t.string().optional(),
        }
    ).named(renames["SubscriptionPurchaseIn"])
    types["SubscriptionPurchaseOut"] = t.struct(
        {
            "startTimeMillis": t.string().optional(),
            "paymentState": t.integer().optional(),
            "obfuscatedExternalAccountId": t.string().optional(),
            "cancelReason": t.integer().optional(),
            "kind": t.string().optional(),
            "developerPayload": t.string().optional(),
            "linkedPurchaseToken": t.string().optional(),
            "countryCode": t.string().optional(),
            "acknowledgementState": t.integer().optional(),
            "priceCurrencyCode": t.string().optional(),
            "profileId": t.string().optional(),
            "purchaseType": t.integer().optional(),
            "priceChange": t.proxy(renames["SubscriptionPriceChangeOut"]).optional(),
            "obfuscatedExternalProfileId": t.string().optional(),
            "promotionCode": t.string().optional(),
            "expiryTimeMillis": t.string().optional(),
            "givenName": t.string().optional(),
            "userCancellationTimeMillis": t.string().optional(),
            "externalAccountId": t.string().optional(),
            "autoRenewing": t.boolean().optional(),
            "orderId": t.string().optional(),
            "cancelSurveyResult": t.proxy(
                renames["SubscriptionCancelSurveyResultOut"]
            ).optional(),
            "priceAmountMicros": t.string().optional(),
            "introductoryPriceInfo": t.proxy(
                renames["IntroductoryPriceInfoOut"]
            ).optional(),
            "profileName": t.string().optional(),
            "emailAddress": t.string().optional(),
            "familyName": t.string().optional(),
            "promotionType": t.integer().optional(),
            "autoResumeTimeMillis": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscriptionPurchaseOut"])
    types["UserCountrySetIn"] = t.struct(
        {"name": t.string().optional(), "countryCodes": t.array(t.string()).optional()}
    ).named(renames["UserCountrySetIn"])
    types["UserCountrySetOut"] = t.struct(
        {
            "name": t.string().optional(),
            "countryCodes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserCountrySetOut"])
    types["ExpansionFileIn"] = t.struct(
        {"referencesVersion": t.integer().optional(), "fileSize": t.string().optional()}
    ).named(renames["ExpansionFileIn"])
    types["ExpansionFileOut"] = t.struct(
        {
            "referencesVersion": t.integer().optional(),
            "fileSize": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExpansionFileOut"])
    types["GeneratedUniversalApkIn"] = t.struct(
        {"downloadId": t.string().optional()}
    ).named(renames["GeneratedUniversalApkIn"])
    types["GeneratedUniversalApkOut"] = t.struct(
        {
            "downloadId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GeneratedUniversalApkOut"])
    types["ConvertedOtherRegionsPriceIn"] = t.struct(
        {
            "usdPrice": t.proxy(renames["MoneyIn"]).optional(),
            "eurPrice": t.proxy(renames["MoneyIn"]).optional(),
        }
    ).named(renames["ConvertedOtherRegionsPriceIn"])
    types["ConvertedOtherRegionsPriceOut"] = t.struct(
        {
            "usdPrice": t.proxy(renames["MoneyOut"]).optional(),
            "eurPrice": t.proxy(renames["MoneyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConvertedOtherRegionsPriceOut"])
    types["RegionalPriceMigrationConfigIn"] = t.struct(
        {"regionCode": t.string(), "oldestAllowedPriceVersionTime": t.string()}
    ).named(renames["RegionalPriceMigrationConfigIn"])
    types["RegionalPriceMigrationConfigOut"] = t.struct(
        {
            "regionCode": t.string(),
            "oldestAllowedPriceVersionTime": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegionalPriceMigrationConfigOut"])
    types["DeobfuscationFileIn"] = t.struct(
        {"symbolType": t.string().optional()}
    ).named(renames["DeobfuscationFileIn"])
    types["DeobfuscationFileOut"] = t.struct(
        {
            "symbolType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeobfuscationFileOut"])
    types["OtherRegionsSubscriptionOfferConfigIn"] = t.struct(
        {"otherRegionsNewSubscriberAvailability": t.boolean().optional()}
    ).named(renames["OtherRegionsSubscriptionOfferConfigIn"])
    types["OtherRegionsSubscriptionOfferConfigOut"] = t.struct(
        {
            "otherRegionsNewSubscriberAvailability": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OtherRegionsSubscriptionOfferConfigOut"])
    types["BundleIn"] = t.struct(
        {
            "sha1": t.string().optional(),
            "versionCode": t.integer().optional(),
            "sha256": t.string().optional(),
        }
    ).named(renames["BundleIn"])
    types["BundleOut"] = t.struct(
        {
            "sha1": t.string().optional(),
            "versionCode": t.integer().optional(),
            "sha256": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BundleOut"])
    types["VoidedPurchaseIn"] = t.struct(
        {
            "voidedSource": t.integer().optional(),
            "purchaseToken": t.string().optional(),
            "purchaseTimeMillis": t.string().optional(),
            "voidedTimeMillis": t.string().optional(),
            "orderId": t.string().optional(),
            "voidedReason": t.integer().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["VoidedPurchaseIn"])
    types["VoidedPurchaseOut"] = t.struct(
        {
            "voidedSource": t.integer().optional(),
            "purchaseToken": t.string().optional(),
            "purchaseTimeMillis": t.string().optional(),
            "voidedTimeMillis": t.string().optional(),
            "orderId": t.string().optional(),
            "voidedReason": t.integer().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VoidedPurchaseOut"])
    types["DeviceMetadataIn"] = t.struct(
        {
            "ramMb": t.integer().optional(),
            "nativePlatform": t.string().optional(),
            "cpuMake": t.string().optional(),
            "cpuModel": t.string().optional(),
            "screenWidthPx": t.integer().optional(),
            "screenDensityDpi": t.integer().optional(),
            "deviceClass": t.string().optional(),
            "screenHeightPx": t.integer().optional(),
            "glEsVersion": t.integer().optional(),
            "productName": t.string().optional(),
            "manufacturer": t.string().optional(),
        }
    ).named(renames["DeviceMetadataIn"])
    types["DeviceMetadataOut"] = t.struct(
        {
            "ramMb": t.integer().optional(),
            "nativePlatform": t.string().optional(),
            "cpuMake": t.string().optional(),
            "cpuModel": t.string().optional(),
            "screenWidthPx": t.integer().optional(),
            "screenDensityDpi": t.integer().optional(),
            "deviceClass": t.string().optional(),
            "screenHeightPx": t.integer().optional(),
            "glEsVersion": t.integer().optional(),
            "productName": t.string().optional(),
            "manufacturer": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceMetadataOut"])
    types["ExpansionFilesUploadResponseIn"] = t.struct(
        {"expansionFile": t.proxy(renames["ExpansionFileIn"]).optional()}
    ).named(renames["ExpansionFilesUploadResponseIn"])
    types["ExpansionFilesUploadResponseOut"] = t.struct(
        {
            "expansionFile": t.proxy(renames["ExpansionFileOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExpansionFilesUploadResponseOut"])
    types["PrepaidBasePlanTypeIn"] = t.struct(
        {"timeExtension": t.string().optional(), "billingPeriodDuration": t.string()}
    ).named(renames["PrepaidBasePlanTypeIn"])
    types["PrepaidBasePlanTypeOut"] = t.struct(
        {
            "timeExtension": t.string().optional(),
            "billingPeriodDuration": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrepaidBasePlanTypeOut"])
    types["SubscriptionOfferIn"] = t.struct(
        {
            "phases": t.array(t.proxy(renames["SubscriptionOfferPhaseIn"])),
            "productId": t.string(),
            "packageName": t.string(),
            "targeting": t.proxy(renames["SubscriptionOfferTargetingIn"]).optional(),
            "offerTags": t.array(t.proxy(renames["OfferTagIn"])).optional(),
            "offerId": t.string(),
            "basePlanId": t.string(),
            "otherRegionsConfig": t.proxy(
                renames["OtherRegionsSubscriptionOfferConfigIn"]
            ).optional(),
            "regionalConfigs": t.array(
                t.proxy(renames["RegionalSubscriptionOfferConfigIn"])
            ),
        }
    ).named(renames["SubscriptionOfferIn"])
    types["SubscriptionOfferOut"] = t.struct(
        {
            "phases": t.array(t.proxy(renames["SubscriptionOfferPhaseOut"])),
            "state": t.string().optional(),
            "productId": t.string(),
            "packageName": t.string(),
            "targeting": t.proxy(renames["SubscriptionOfferTargetingOut"]).optional(),
            "offerTags": t.array(t.proxy(renames["OfferTagOut"])).optional(),
            "offerId": t.string(),
            "basePlanId": t.string(),
            "otherRegionsConfig": t.proxy(
                renames["OtherRegionsSubscriptionOfferConfigOut"]
            ).optional(),
            "regionalConfigs": t.array(
                t.proxy(renames["RegionalSubscriptionOfferConfigOut"])
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscriptionOfferOut"])
    types["AutoRenewingBasePlanTypeIn"] = t.struct(
        {
            "billingPeriodDuration": t.string(),
            "resubscribeState": t.string().optional(),
            "legacyCompatible": t.boolean().optional(),
            "legacyCompatibleSubscriptionOfferId": t.string().optional(),
            "gracePeriodDuration": t.string().optional(),
            "prorationMode": t.string().optional(),
        }
    ).named(renames["AutoRenewingBasePlanTypeIn"])
    types["AutoRenewingBasePlanTypeOut"] = t.struct(
        {
            "billingPeriodDuration": t.string(),
            "resubscribeState": t.string().optional(),
            "legacyCompatible": t.boolean().optional(),
            "legacyCompatibleSubscriptionOfferId": t.string().optional(),
            "gracePeriodDuration": t.string().optional(),
            "prorationMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutoRenewingBasePlanTypeOut"])
    types["TestPurchaseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["TestPurchaseIn"]
    )
    types["TestPurchaseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["TestPurchaseOut"])
    types["SdkVersionIn"] = t.struct({"min": t.integer().optional()}).named(
        renames["SdkVersionIn"]
    )
    types["SdkVersionOut"] = t.struct(
        {
            "min": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SdkVersionOut"])
    types["DeveloperCommentIn"] = t.struct(
        {
            "text": t.string().optional(),
            "lastModified": t.proxy(renames["TimestampIn"]).optional(),
        }
    ).named(renames["DeveloperCommentIn"])
    types["DeveloperCommentOut"] = t.struct(
        {
            "text": t.string().optional(),
            "lastModified": t.proxy(renames["TimestampOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeveloperCommentOut"])
    types["MigrateBasePlanPricesResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["MigrateBasePlanPricesResponseIn"])
    types["MigrateBasePlanPricesResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["MigrateBasePlanPricesResponseOut"])
    types["ImageIn"] = t.struct(
        {
            "sha1": t.string().optional(),
            "sha256": t.string().optional(),
            "id": t.string().optional(),
            "url": t.string().optional(),
        }
    ).named(renames["ImageIn"])
    types["ImageOut"] = t.struct(
        {
            "sha1": t.string().optional(),
            "sha256": t.string().optional(),
            "id": t.string().optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageOut"])
    types["SubscriptionIn"] = t.struct(
        {
            "productId": t.string().optional(),
            "listings": t.array(t.proxy(renames["SubscriptionListingIn"])),
            "packageName": t.string().optional(),
            "basePlans": t.array(t.proxy(renames["BasePlanIn"])).optional(),
            "taxAndComplianceSettings": t.proxy(
                renames["SubscriptionTaxAndComplianceSettingsIn"]
            ).optional(),
        }
    ).named(renames["SubscriptionIn"])
    types["SubscriptionOut"] = t.struct(
        {
            "productId": t.string().optional(),
            "listings": t.array(t.proxy(renames["SubscriptionListingOut"])),
            "archived": t.boolean().optional(),
            "packageName": t.string().optional(),
            "basePlans": t.array(t.proxy(renames["BasePlanOut"])).optional(),
            "taxAndComplianceSettings": t.proxy(
                renames["SubscriptionTaxAndComplianceSettingsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscriptionOut"])
    types["ModuleTargetingIn"] = t.struct(
        {
            "deviceFeatureTargeting": t.array(
                t.proxy(renames["DeviceFeatureTargetingIn"])
            ).optional(),
            "sdkVersionTargeting": t.proxy(renames["SdkVersionTargetingIn"]).optional(),
            "userCountriesTargeting": t.proxy(
                renames["UserCountriesTargetingIn"]
            ).optional(),
        }
    ).named(renames["ModuleTargetingIn"])
    types["ModuleTargetingOut"] = t.struct(
        {
            "deviceFeatureTargeting": t.array(
                t.proxy(renames["DeviceFeatureTargetingOut"])
            ).optional(),
            "sdkVersionTargeting": t.proxy(
                renames["SdkVersionTargetingOut"]
            ).optional(),
            "userCountriesTargeting": t.proxy(
                renames["UserCountriesTargetingOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ModuleTargetingOut"])
    types["RegionalTaxRateInfoIn"] = t.struct(
        {
            "eligibleForStreamingServiceTaxRate": t.boolean().optional(),
            "streamingTaxType": t.string().optional(),
            "taxTier": t.string().optional(),
        }
    ).named(renames["RegionalTaxRateInfoIn"])
    types["RegionalTaxRateInfoOut"] = t.struct(
        {
            "eligibleForStreamingServiceTaxRate": t.boolean().optional(),
            "streamingTaxType": t.string().optional(),
            "taxTier": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegionalTaxRateInfoOut"])
    types["SystemFeatureIn"] = t.struct({"name": t.string().optional()}).named(
        renames["SystemFeatureIn"]
    )
    types["SystemFeatureOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SystemFeatureOut"])
    types["CountryTargetingIn"] = t.struct(
        {
            "countries": t.array(t.string()).optional(),
            "includeRestOfWorld": t.boolean().optional(),
        }
    ).named(renames["CountryTargetingIn"])
    types["CountryTargetingOut"] = t.struct(
        {
            "countries": t.array(t.string()).optional(),
            "includeRestOfWorld": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CountryTargetingOut"])
    types["SubscriptionCancelSurveyResultIn"] = t.struct(
        {
            "cancelSurveyReason": t.integer().optional(),
            "userInputCancelReason": t.string().optional(),
        }
    ).named(renames["SubscriptionCancelSurveyResultIn"])
    types["SubscriptionCancelSurveyResultOut"] = t.struct(
        {
            "cancelSurveyReason": t.integer().optional(),
            "userInputCancelReason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscriptionCancelSurveyResultOut"])
    types["UserCommentIn"] = t.struct(
        {
            "reviewerLanguage": t.string().optional(),
            "starRating": t.integer().optional(),
            "lastModified": t.proxy(renames["TimestampIn"]).optional(),
            "deviceMetadata": t.proxy(renames["DeviceMetadataIn"]).optional(),
            "appVersionName": t.string().optional(),
            "thumbsDownCount": t.integer().optional(),
            "text": t.string().optional(),
            "originalText": t.string().optional(),
            "thumbsUpCount": t.integer().optional(),
            "device": t.string().optional(),
            "androidOsVersion": t.integer().optional(),
            "appVersionCode": t.integer().optional(),
        }
    ).named(renames["UserCommentIn"])
    types["UserCommentOut"] = t.struct(
        {
            "reviewerLanguage": t.string().optional(),
            "starRating": t.integer().optional(),
            "lastModified": t.proxy(renames["TimestampOut"]).optional(),
            "deviceMetadata": t.proxy(renames["DeviceMetadataOut"]).optional(),
            "appVersionName": t.string().optional(),
            "thumbsDownCount": t.integer().optional(),
            "text": t.string().optional(),
            "originalText": t.string().optional(),
            "thumbsUpCount": t.integer().optional(),
            "device": t.string().optional(),
            "androidOsVersion": t.integer().optional(),
            "appVersionCode": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserCommentOut"])
    types["ReplacementCancellationIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ReplacementCancellationIn"]
    )
    types["ReplacementCancellationOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ReplacementCancellationOut"])
    types["InAppProductListingIn"] = t.struct(
        {
            "benefits": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["InAppProductListingIn"])
    types["InAppProductListingOut"] = t.struct(
        {
            "benefits": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InAppProductListingOut"])
    types["ActivateSubscriptionOfferRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ActivateSubscriptionOfferRequestIn"])
    types["ActivateSubscriptionOfferRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ActivateSubscriptionOfferRequestOut"])
    types["ApkBinaryIn"] = t.struct(
        {"sha256": t.string().optional(), "sha1": t.string().optional()}
    ).named(renames["ApkBinaryIn"])
    types["ApkBinaryOut"] = t.struct(
        {
            "sha256": t.string().optional(),
            "sha1": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApkBinaryOut"])
    types["LocalizedTextIn"] = t.struct(
        {"text": t.string().optional(), "language": t.string().optional()}
    ).named(renames["LocalizedTextIn"])
    types["LocalizedTextOut"] = t.struct(
        {
            "text": t.string().optional(),
            "language": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocalizedTextOut"])
    types["TrackCountryAvailabilityIn"] = t.struct(
        {
            "restOfWorld": t.boolean().optional(),
            "countries": t.array(t.proxy(renames["TrackTargetedCountryIn"])).optional(),
            "syncWithProduction": t.boolean().optional(),
        }
    ).named(renames["TrackCountryAvailabilityIn"])
    types["TrackCountryAvailabilityOut"] = t.struct(
        {
            "restOfWorld": t.boolean().optional(),
            "countries": t.array(
                t.proxy(renames["TrackTargetedCountryOut"])
            ).optional(),
            "syncWithProduction": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrackCountryAvailabilityOut"])
    types["GrantIn"] = t.struct(
        {
            "name": t.string(),
            "packageName": t.string().optional(),
            "appLevelPermissions": t.array(t.string()).optional(),
        }
    ).named(renames["GrantIn"])
    types["GrantOut"] = t.struct(
        {
            "name": t.string(),
            "packageName": t.string().optional(),
            "appLevelPermissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrantOut"])
    types["SubscriptionPurchasesAcknowledgeRequestIn"] = t.struct(
        {"developerPayload": t.string().optional()}
    ).named(renames["SubscriptionPurchasesAcknowledgeRequestIn"])
    types["SubscriptionPurchasesAcknowledgeRequestOut"] = t.struct(
        {
            "developerPayload": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscriptionPurchasesAcknowledgeRequestOut"])
    types["UserInitiatedCancellationIn"] = t.struct(
        {
            "cancelSurveyResult": t.proxy(renames["CancelSurveyResultIn"]).optional(),
            "cancelTime": t.string().optional(),
        }
    ).named(renames["UserInitiatedCancellationIn"])
    types["UserInitiatedCancellationOut"] = t.struct(
        {
            "cancelSurveyResult": t.proxy(renames["CancelSurveyResultOut"]).optional(),
            "cancelTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserInitiatedCancellationOut"])
    types["ReviewsListResponseIn"] = t.struct(
        {
            "pageInfo": t.proxy(renames["PageInfoIn"]).optional(),
            "reviews": t.array(t.proxy(renames["ReviewIn"])).optional(),
            "tokenPagination": t.proxy(renames["TokenPaginationIn"]).optional(),
        }
    ).named(renames["ReviewsListResponseIn"])
    types["ReviewsListResponseOut"] = t.struct(
        {
            "pageInfo": t.proxy(renames["PageInfoOut"]).optional(),
            "reviews": t.array(t.proxy(renames["ReviewOut"])).optional(),
            "tokenPagination": t.proxy(renames["TokenPaginationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReviewsListResponseOut"])
    types["BasePlanIn"] = t.struct(
        {
            "prepaidBasePlanType": t.proxy(renames["PrepaidBasePlanTypeIn"]).optional(),
            "regionalConfigs": t.array(
                t.proxy(renames["RegionalBasePlanConfigIn"])
            ).optional(),
            "otherRegionsConfig": t.proxy(
                renames["OtherRegionsBasePlanConfigIn"]
            ).optional(),
            "autoRenewingBasePlanType": t.proxy(
                renames["AutoRenewingBasePlanTypeIn"]
            ).optional(),
            "basePlanId": t.string(),
            "offerTags": t.array(t.proxy(renames["OfferTagIn"])).optional(),
        }
    ).named(renames["BasePlanIn"])
    types["BasePlanOut"] = t.struct(
        {
            "prepaidBasePlanType": t.proxy(
                renames["PrepaidBasePlanTypeOut"]
            ).optional(),
            "regionalConfigs": t.array(
                t.proxy(renames["RegionalBasePlanConfigOut"])
            ).optional(),
            "otherRegionsConfig": t.proxy(
                renames["OtherRegionsBasePlanConfigOut"]
            ).optional(),
            "autoRenewingBasePlanType": t.proxy(
                renames["AutoRenewingBasePlanTypeOut"]
            ).optional(),
            "state": t.string().optional(),
            "basePlanId": t.string(),
            "offerTags": t.array(t.proxy(renames["OfferTagOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BasePlanOut"])
    types["OtherRegionsBasePlanConfigIn"] = t.struct(
        {
            "newSubscriberAvailability": t.boolean().optional(),
            "usdPrice": t.proxy(renames["MoneyIn"]),
            "eurPrice": t.proxy(renames["MoneyIn"]),
        }
    ).named(renames["OtherRegionsBasePlanConfigIn"])
    types["OtherRegionsBasePlanConfigOut"] = t.struct(
        {
            "newSubscriberAvailability": t.boolean().optional(),
            "usdPrice": t.proxy(renames["MoneyOut"]),
            "eurPrice": t.proxy(renames["MoneyOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OtherRegionsBasePlanConfigOut"])
    types["ReviewsReplyRequestIn"] = t.struct(
        {"replyText": t.string().optional()}
    ).named(renames["ReviewsReplyRequestIn"])
    types["ReviewsReplyRequestOut"] = t.struct(
        {
            "replyText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReviewsReplyRequestOut"])
    types["OtherRegionsSubscriptionOfferPhaseConfigIn"] = t.struct(
        {
            "otherRegionsPrices": t.proxy(
                renames["OtherRegionsSubscriptionOfferPhasePricesIn"]
            ).optional(),
            "absoluteDiscounts": t.proxy(
                renames["OtherRegionsSubscriptionOfferPhasePricesIn"]
            ).optional(),
            "relativeDiscount": t.number().optional(),
        }
    ).named(renames["OtherRegionsSubscriptionOfferPhaseConfigIn"])
    types["OtherRegionsSubscriptionOfferPhaseConfigOut"] = t.struct(
        {
            "otherRegionsPrices": t.proxy(
                renames["OtherRegionsSubscriptionOfferPhasePricesOut"]
            ).optional(),
            "absoluteDiscounts": t.proxy(
                renames["OtherRegionsSubscriptionOfferPhasePricesOut"]
            ).optional(),
            "relativeDiscount": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OtherRegionsSubscriptionOfferPhaseConfigOut"])
    types["OfferDetailsIn"] = t.struct(
        {
            "basePlanId": t.string().optional(),
            "offerTags": t.array(t.string()).optional(),
            "offerId": t.string().optional(),
        }
    ).named(renames["OfferDetailsIn"])
    types["OfferDetailsOut"] = t.struct(
        {
            "basePlanId": t.string().optional(),
            "offerTags": t.array(t.string()).optional(),
            "offerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OfferDetailsOut"])
    types["DeviceFeatureTargetingIn"] = t.struct(
        {"requiredFeature": t.proxy(renames["DeviceFeatureIn"]).optional()}
    ).named(renames["DeviceFeatureTargetingIn"])
    types["DeviceFeatureTargetingOut"] = t.struct(
        {
            "requiredFeature": t.proxy(renames["DeviceFeatureOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceFeatureTargetingOut"])
    types["ImagesListResponseIn"] = t.struct(
        {"images": t.array(t.proxy(renames["ImageIn"])).optional()}
    ).named(renames["ImagesListResponseIn"])
    types["ImagesListResponseOut"] = t.struct(
        {
            "images": t.array(t.proxy(renames["ImageOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImagesListResponseOut"])
    types["SubscriptionPurchasesDeferResponseIn"] = t.struct(
        {"newExpiryTimeMillis": t.string().optional()}
    ).named(renames["SubscriptionPurchasesDeferResponseIn"])
    types["SubscriptionPurchasesDeferResponseOut"] = t.struct(
        {
            "newExpiryTimeMillis": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscriptionPurchasesDeferResponseOut"])
    types["DeviceTierIn"] = t.struct(
        {
            "level": t.integer().optional(),
            "deviceGroupNames": t.array(t.string()).optional(),
        }
    ).named(renames["DeviceTierIn"])
    types["DeviceTierOut"] = t.struct(
        {
            "level": t.integer().optional(),
            "deviceGroupNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceTierOut"])
    types["SubscriptionPurchaseLineItemIn"] = t.struct(
        {
            "prepaidPlan": t.proxy(renames["PrepaidPlanIn"]).optional(),
            "deferredItemReplacement": t.proxy(
                renames["DeferredItemReplacementIn"]
            ).optional(),
            "autoRenewingPlan": t.proxy(renames["AutoRenewingPlanIn"]).optional(),
            "expiryTime": t.string().optional(),
            "productId": t.string().optional(),
            "offerDetails": t.proxy(renames["OfferDetailsIn"]).optional(),
        }
    ).named(renames["SubscriptionPurchaseLineItemIn"])
    types["SubscriptionPurchaseLineItemOut"] = t.struct(
        {
            "prepaidPlan": t.proxy(renames["PrepaidPlanOut"]).optional(),
            "deferredItemReplacement": t.proxy(
                renames["DeferredItemReplacementOut"]
            ).optional(),
            "autoRenewingPlan": t.proxy(renames["AutoRenewingPlanOut"]).optional(),
            "expiryTime": t.string().optional(),
            "productId": t.string().optional(),
            "offerDetails": t.proxy(renames["OfferDetailsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscriptionPurchaseLineItemOut"])
    types["ExternalTransactionTestPurchaseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ExternalTransactionTestPurchaseIn"])
    types["ExternalTransactionTestPurchaseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ExternalTransactionTestPurchaseOut"])
    types["GeneratedStandaloneApkIn"] = t.struct(
        {"downloadId": t.string().optional(), "variantId": t.integer().optional()}
    ).named(renames["GeneratedStandaloneApkIn"])
    types["GeneratedStandaloneApkOut"] = t.struct(
        {
            "downloadId": t.string().optional(),
            "variantId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GeneratedStandaloneApkOut"])
    types["SystemInitiatedCancellationIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["SystemInitiatedCancellationIn"])
    types["SystemInitiatedCancellationOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SystemInitiatedCancellationOut"])
    types["TrackIn"] = t.struct(
        {
            "releases": t.array(t.proxy(renames["TrackReleaseIn"])).optional(),
            "track": t.string().optional(),
        }
    ).named(renames["TrackIn"])
    types["TrackOut"] = t.struct(
        {
            "releases": t.array(t.proxy(renames["TrackReleaseOut"])).optional(),
            "track": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrackOut"])

    functions = {}
    functions["generatedapksList"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/generatedApks/{versionCode}/downloads/{downloadId}:download",
        t.struct(
            {
                "versionCode": t.integer().optional(),
                "downloadId": t.string().optional(),
                "packageName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["generatedapksDownload"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/generatedApks/{versionCode}/downloads/{downloadId}:download",
        t.struct(
            {
                "versionCode": t.integer().optional(),
                "downloadId": t.string().optional(),
                "packageName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["ordersRefund"] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/orders/{orderId}:refund",
        t.struct(
            {
                "packageName": t.string().optional(),
                "revoke": t.boolean().optional(),
                "orderId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["externaltransactionsRefundexternaltransaction"] = androidpublisher.post(
        "androidpublisher/v3/{parent}/externalTransactions",
        t.struct(
            {
                "parent": t.string(),
                "externalTransactionId": t.string(),
                "oneTimeTransaction": t.proxy(
                    renames["OneTimeExternalTransactionIn"]
                ).optional(),
                "transactionTime": t.string(),
                "recurringTransaction": t.proxy(
                    renames["RecurringExternalTransactionIn"]
                ).optional(),
                "originalPreTaxAmount": t.proxy(renames["PriceIn"]),
                "userTaxAddress": t.proxy(renames["ExternalTransactionAddressIn"]),
                "originalTaxAmount": t.proxy(renames["PriceIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExternalTransactionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["externaltransactionsGetexternaltransaction"] = androidpublisher.post(
        "androidpublisher/v3/{parent}/externalTransactions",
        t.struct(
            {
                "parent": t.string(),
                "externalTransactionId": t.string(),
                "oneTimeTransaction": t.proxy(
                    renames["OneTimeExternalTransactionIn"]
                ).optional(),
                "transactionTime": t.string(),
                "recurringTransaction": t.proxy(
                    renames["RecurringExternalTransactionIn"]
                ).optional(),
                "originalPreTaxAmount": t.proxy(renames["PriceIn"]),
                "userTaxAddress": t.proxy(renames["ExternalTransactionAddressIn"]),
                "originalTaxAmount": t.proxy(renames["PriceIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExternalTransactionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["externaltransactionsCreateexternaltransaction"] = androidpublisher.post(
        "androidpublisher/v3/{parent}/externalTransactions",
        t.struct(
            {
                "parent": t.string(),
                "externalTransactionId": t.string(),
                "oneTimeTransaction": t.proxy(
                    renames["OneTimeExternalTransactionIn"]
                ).optional(),
                "transactionTime": t.string(),
                "recurringTransaction": t.proxy(
                    renames["RecurringExternalTransactionIn"]
                ).optional(),
                "originalPreTaxAmount": t.proxy(renames["PriceIn"]),
                "userTaxAddress": t.proxy(renames["ExternalTransactionAddressIn"]),
                "originalTaxAmount": t.proxy(renames["PriceIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExternalTransactionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["monetizationConvertRegionPrices"] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/pricing:convertRegionPrices",
        t.struct(
            {
                "packageName": t.string(),
                "price": t.proxy(renames["MoneyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConvertRegionPricesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["monetizationSubscriptionsCreate"] = androidpublisher.delete(
        "androidpublisher/v3/applications/{packageName}/subscriptions/{productId}",
        t.struct(
            {
                "productId": t.string(),
                "packageName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["monetizationSubscriptionsPatch"] = androidpublisher.delete(
        "androidpublisher/v3/applications/{packageName}/subscriptions/{productId}",
        t.struct(
            {
                "productId": t.string(),
                "packageName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["monetizationSubscriptionsGet"] = androidpublisher.delete(
        "androidpublisher/v3/applications/{packageName}/subscriptions/{productId}",
        t.struct(
            {
                "productId": t.string(),
                "packageName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["monetizationSubscriptionsArchive"] = androidpublisher.delete(
        "androidpublisher/v3/applications/{packageName}/subscriptions/{productId}",
        t.struct(
            {
                "productId": t.string(),
                "packageName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["monetizationSubscriptionsList"] = androidpublisher.delete(
        "androidpublisher/v3/applications/{packageName}/subscriptions/{productId}",
        t.struct(
            {
                "productId": t.string(),
                "packageName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["monetizationSubscriptionsDelete"] = androidpublisher.delete(
        "androidpublisher/v3/applications/{packageName}/subscriptions/{productId}",
        t.struct(
            {
                "productId": t.string(),
                "packageName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["monetizationSubscriptionsBasePlansDeactivate"] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/subscriptions/{productId}/basePlans/{basePlanId}:migratePrices",
        t.struct(
            {
                "basePlanId": t.string(),
                "packageName": t.string(),
                "productId": t.string(),
                "regionsVersion": t.proxy(renames["RegionsVersionIn"]),
                "regionalPriceMigrations": t.array(
                    t.proxy(renames["RegionalPriceMigrationConfigIn"])
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MigrateBasePlanPricesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["monetizationSubscriptionsBasePlansActivate"] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/subscriptions/{productId}/basePlans/{basePlanId}:migratePrices",
        t.struct(
            {
                "basePlanId": t.string(),
                "packageName": t.string(),
                "productId": t.string(),
                "regionsVersion": t.proxy(renames["RegionsVersionIn"]),
                "regionalPriceMigrations": t.array(
                    t.proxy(renames["RegionalPriceMigrationConfigIn"])
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MigrateBasePlanPricesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["monetizationSubscriptionsBasePlansDelete"] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/subscriptions/{productId}/basePlans/{basePlanId}:migratePrices",
        t.struct(
            {
                "basePlanId": t.string(),
                "packageName": t.string(),
                "productId": t.string(),
                "regionsVersion": t.proxy(renames["RegionsVersionIn"]),
                "regionalPriceMigrations": t.array(
                    t.proxy(renames["RegionalPriceMigrationConfigIn"])
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MigrateBasePlanPricesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "monetizationSubscriptionsBasePlansMigratePrices"
    ] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/subscriptions/{productId}/basePlans/{basePlanId}:migratePrices",
        t.struct(
            {
                "basePlanId": t.string(),
                "packageName": t.string(),
                "productId": t.string(),
                "regionsVersion": t.proxy(renames["RegionsVersionIn"]),
                "regionalPriceMigrations": t.array(
                    t.proxy(renames["RegionalPriceMigrationConfigIn"])
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MigrateBasePlanPricesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "monetizationSubscriptionsBasePlansOffersDeactivate"
    ] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/subscriptions/{productId}/basePlans/{basePlanId}/offers",
        t.struct(
            {
                "productId": t.string(),
                "basePlanId": t.string(),
                "packageName": t.string(),
                "offerId": t.string(),
                "regionsVersion.version": t.string(),
                "phases": t.array(t.proxy(renames["SubscriptionOfferPhaseIn"])),
                "targeting": t.proxy(
                    renames["SubscriptionOfferTargetingIn"]
                ).optional(),
                "offerTags": t.array(t.proxy(renames["OfferTagIn"])).optional(),
                "otherRegionsConfig": t.proxy(
                    renames["OtherRegionsSubscriptionOfferConfigIn"]
                ).optional(),
                "regionalConfigs": t.array(
                    t.proxy(renames["RegionalSubscriptionOfferConfigIn"])
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionOfferOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "monetizationSubscriptionsBasePlansOffersActivate"
    ] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/subscriptions/{productId}/basePlans/{basePlanId}/offers",
        t.struct(
            {
                "productId": t.string(),
                "basePlanId": t.string(),
                "packageName": t.string(),
                "offerId": t.string(),
                "regionsVersion.version": t.string(),
                "phases": t.array(t.proxy(renames["SubscriptionOfferPhaseIn"])),
                "targeting": t.proxy(
                    renames["SubscriptionOfferTargetingIn"]
                ).optional(),
                "offerTags": t.array(t.proxy(renames["OfferTagIn"])).optional(),
                "otherRegionsConfig": t.proxy(
                    renames["OtherRegionsSubscriptionOfferConfigIn"]
                ).optional(),
                "regionalConfigs": t.array(
                    t.proxy(renames["RegionalSubscriptionOfferConfigIn"])
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionOfferOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["monetizationSubscriptionsBasePlansOffersList"] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/subscriptions/{productId}/basePlans/{basePlanId}/offers",
        t.struct(
            {
                "productId": t.string(),
                "basePlanId": t.string(),
                "packageName": t.string(),
                "offerId": t.string(),
                "regionsVersion.version": t.string(),
                "phases": t.array(t.proxy(renames["SubscriptionOfferPhaseIn"])),
                "targeting": t.proxy(
                    renames["SubscriptionOfferTargetingIn"]
                ).optional(),
                "offerTags": t.array(t.proxy(renames["OfferTagIn"])).optional(),
                "otherRegionsConfig": t.proxy(
                    renames["OtherRegionsSubscriptionOfferConfigIn"]
                ).optional(),
                "regionalConfigs": t.array(
                    t.proxy(renames["RegionalSubscriptionOfferConfigIn"])
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionOfferOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["monetizationSubscriptionsBasePlansOffersGet"] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/subscriptions/{productId}/basePlans/{basePlanId}/offers",
        t.struct(
            {
                "productId": t.string(),
                "basePlanId": t.string(),
                "packageName": t.string(),
                "offerId": t.string(),
                "regionsVersion.version": t.string(),
                "phases": t.array(t.proxy(renames["SubscriptionOfferPhaseIn"])),
                "targeting": t.proxy(
                    renames["SubscriptionOfferTargetingIn"]
                ).optional(),
                "offerTags": t.array(t.proxy(renames["OfferTagIn"])).optional(),
                "otherRegionsConfig": t.proxy(
                    renames["OtherRegionsSubscriptionOfferConfigIn"]
                ).optional(),
                "regionalConfigs": t.array(
                    t.proxy(renames["RegionalSubscriptionOfferConfigIn"])
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionOfferOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["monetizationSubscriptionsBasePlansOffersPatch"] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/subscriptions/{productId}/basePlans/{basePlanId}/offers",
        t.struct(
            {
                "productId": t.string(),
                "basePlanId": t.string(),
                "packageName": t.string(),
                "offerId": t.string(),
                "regionsVersion.version": t.string(),
                "phases": t.array(t.proxy(renames["SubscriptionOfferPhaseIn"])),
                "targeting": t.proxy(
                    renames["SubscriptionOfferTargetingIn"]
                ).optional(),
                "offerTags": t.array(t.proxy(renames["OfferTagIn"])).optional(),
                "otherRegionsConfig": t.proxy(
                    renames["OtherRegionsSubscriptionOfferConfigIn"]
                ).optional(),
                "regionalConfigs": t.array(
                    t.proxy(renames["RegionalSubscriptionOfferConfigIn"])
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionOfferOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["monetizationSubscriptionsBasePlansOffersDelete"] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/subscriptions/{productId}/basePlans/{basePlanId}/offers",
        t.struct(
            {
                "productId": t.string(),
                "basePlanId": t.string(),
                "packageName": t.string(),
                "offerId": t.string(),
                "regionsVersion.version": t.string(),
                "phases": t.array(t.proxy(renames["SubscriptionOfferPhaseIn"])),
                "targeting": t.proxy(
                    renames["SubscriptionOfferTargetingIn"]
                ).optional(),
                "offerTags": t.array(t.proxy(renames["OfferTagIn"])).optional(),
                "otherRegionsConfig": t.proxy(
                    renames["OtherRegionsSubscriptionOfferConfigIn"]
                ).optional(),
                "regionalConfigs": t.array(
                    t.proxy(renames["RegionalSubscriptionOfferConfigIn"])
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionOfferOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["monetizationSubscriptionsBasePlansOffersCreate"] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/subscriptions/{productId}/basePlans/{basePlanId}/offers",
        t.struct(
            {
                "productId": t.string(),
                "basePlanId": t.string(),
                "packageName": t.string(),
                "offerId": t.string(),
                "regionsVersion.version": t.string(),
                "phases": t.array(t.proxy(renames["SubscriptionOfferPhaseIn"])),
                "targeting": t.proxy(
                    renames["SubscriptionOfferTargetingIn"]
                ).optional(),
                "offerTags": t.array(t.proxy(renames["OfferTagIn"])).optional(),
                "otherRegionsConfig": t.proxy(
                    renames["OtherRegionsSubscriptionOfferConfigIn"]
                ).optional(),
                "regionalConfigs": t.array(
                    t.proxy(renames["RegionalSubscriptionOfferConfigIn"])
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionOfferOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["purchasesSubscriptionsv2Get"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/purchases/subscriptionsv2/tokens/{token}",
        t.struct(
            {
                "token": t.string(),
                "packageName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionPurchaseV2Out"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["purchasesVoidedpurchasesList"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/purchases/voidedpurchases",
        t.struct(
            {
                "packageName": t.string().optional(),
                "token": t.string().optional(),
                "type": t.integer().optional(),
                "endTime": t.string().optional(),
                "startIndex": t.integer().optional(),
                "maxResults": t.integer().optional(),
                "startTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VoidedPurchasesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["purchasesProductsAcknowledge"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/purchases/products/{productId}/tokens/{token}",
        t.struct(
            {
                "packageName": t.string().optional(),
                "productId": t.string().optional(),
                "token": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductPurchaseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["purchasesProductsConsume"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/purchases/products/{productId}/tokens/{token}",
        t.struct(
            {
                "packageName": t.string().optional(),
                "productId": t.string().optional(),
                "token": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductPurchaseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["purchasesProductsGet"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/purchases/products/{productId}/tokens/{token}",
        t.struct(
            {
                "packageName": t.string().optional(),
                "productId": t.string().optional(),
                "token": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductPurchaseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["purchasesSubscriptionsCancel"] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/purchases/subscriptions/{subscriptionId}/tokens/{token}:refund",
        t.struct(
            {
                "packageName": t.string().optional(),
                "subscriptionId": t.string().optional(),
                "token": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["purchasesSubscriptionsAcknowledge"] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/purchases/subscriptions/{subscriptionId}/tokens/{token}:refund",
        t.struct(
            {
                "packageName": t.string().optional(),
                "subscriptionId": t.string().optional(),
                "token": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["purchasesSubscriptionsDefer"] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/purchases/subscriptions/{subscriptionId}/tokens/{token}:refund",
        t.struct(
            {
                "packageName": t.string().optional(),
                "subscriptionId": t.string().optional(),
                "token": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["purchasesSubscriptionsGet"] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/purchases/subscriptions/{subscriptionId}/tokens/{token}:refund",
        t.struct(
            {
                "packageName": t.string().optional(),
                "subscriptionId": t.string().optional(),
                "token": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["purchasesSubscriptionsRevoke"] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/purchases/subscriptions/{subscriptionId}/tokens/{token}:refund",
        t.struct(
            {
                "packageName": t.string().optional(),
                "subscriptionId": t.string().optional(),
                "token": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["purchasesSubscriptionsRefund"] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/purchases/subscriptions/{subscriptionId}/tokens/{token}:refund",
        t.struct(
            {
                "packageName": t.string().optional(),
                "subscriptionId": t.string().optional(),
                "token": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsValidate"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}",
        t.struct(
            {
                "editId": t.string().optional(),
                "packageName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AppEditOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsInsert"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}",
        t.struct(
            {
                "editId": t.string().optional(),
                "packageName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AppEditOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsDelete"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}",
        t.struct(
            {
                "editId": t.string().optional(),
                "packageName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AppEditOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsCommit"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}",
        t.struct(
            {
                "editId": t.string().optional(),
                "packageName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AppEditOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsGet"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}",
        t.struct(
            {
                "editId": t.string().optional(),
                "packageName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AppEditOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsTracksGet"] = androidpublisher.patch(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/tracks/{track}",
        t.struct(
            {
                "track": t.string().optional(),
                "editId": t.string().optional(),
                "packageName": t.string().optional(),
                "releases": t.array(t.proxy(renames["TrackReleaseIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TrackOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsTracksList"] = androidpublisher.patch(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/tracks/{track}",
        t.struct(
            {
                "track": t.string().optional(),
                "editId": t.string().optional(),
                "packageName": t.string().optional(),
                "releases": t.array(t.proxy(renames["TrackReleaseIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TrackOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsTracksUpdate"] = androidpublisher.patch(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/tracks/{track}",
        t.struct(
            {
                "track": t.string().optional(),
                "editId": t.string().optional(),
                "packageName": t.string().optional(),
                "releases": t.array(t.proxy(renames["TrackReleaseIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TrackOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsTracksPatch"] = androidpublisher.patch(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/tracks/{track}",
        t.struct(
            {
                "track": t.string().optional(),
                "editId": t.string().optional(),
                "packageName": t.string().optional(),
                "releases": t.array(t.proxy(renames["TrackReleaseIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TrackOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsDetailsPatch"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/details",
        t.struct(
            {
                "editId": t.string().optional(),
                "packageName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AppDetailsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsDetailsUpdate"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/details",
        t.struct(
            {
                "editId": t.string().optional(),
                "packageName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AppDetailsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsDetailsGet"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/details",
        t.struct(
            {
                "editId": t.string().optional(),
                "packageName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AppDetailsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsImagesDelete"] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/listings/{language}/{imageType}",
        t.struct(
            {
                "imageType": t.string().optional(),
                "editId": t.string().optional(),
                "packageName": t.string().optional(),
                "language": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ImagesUploadResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsImagesList"] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/listings/{language}/{imageType}",
        t.struct(
            {
                "imageType": t.string().optional(),
                "editId": t.string().optional(),
                "packageName": t.string().optional(),
                "language": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ImagesUploadResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsImagesDeleteall"] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/listings/{language}/{imageType}",
        t.struct(
            {
                "imageType": t.string().optional(),
                "editId": t.string().optional(),
                "packageName": t.string().optional(),
                "language": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ImagesUploadResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsImagesUpload"] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/listings/{language}/{imageType}",
        t.struct(
            {
                "imageType": t.string().optional(),
                "editId": t.string().optional(),
                "packageName": t.string().optional(),
                "language": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ImagesUploadResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsCountryavailabilityGet"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/countryAvailability/{track}",
        t.struct(
            {
                "editId": t.string().optional(),
                "packageName": t.string().optional(),
                "track": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TrackCountryAvailabilityOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsListingsUpdate"] = androidpublisher.patch(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/listings/{language}",
        t.struct(
            {
                "editId": t.string().optional(),
                "language": t.string().optional(),
                "packageName": t.string().optional(),
                "fullDescription": t.string().optional(),
                "title": t.string().optional(),
                "shortDescription": t.string().optional(),
                "video": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsListingsDelete"] = androidpublisher.patch(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/listings/{language}",
        t.struct(
            {
                "editId": t.string().optional(),
                "language": t.string().optional(),
                "packageName": t.string().optional(),
                "fullDescription": t.string().optional(),
                "title": t.string().optional(),
                "shortDescription": t.string().optional(),
                "video": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsListingsDeleteall"] = androidpublisher.patch(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/listings/{language}",
        t.struct(
            {
                "editId": t.string().optional(),
                "language": t.string().optional(),
                "packageName": t.string().optional(),
                "fullDescription": t.string().optional(),
                "title": t.string().optional(),
                "shortDescription": t.string().optional(),
                "video": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsListingsGet"] = androidpublisher.patch(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/listings/{language}",
        t.struct(
            {
                "editId": t.string().optional(),
                "language": t.string().optional(),
                "packageName": t.string().optional(),
                "fullDescription": t.string().optional(),
                "title": t.string().optional(),
                "shortDescription": t.string().optional(),
                "video": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsListingsList"] = androidpublisher.patch(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/listings/{language}",
        t.struct(
            {
                "editId": t.string().optional(),
                "language": t.string().optional(),
                "packageName": t.string().optional(),
                "fullDescription": t.string().optional(),
                "title": t.string().optional(),
                "shortDescription": t.string().optional(),
                "video": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsListingsPatch"] = androidpublisher.patch(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/listings/{language}",
        t.struct(
            {
                "editId": t.string().optional(),
                "language": t.string().optional(),
                "packageName": t.string().optional(),
                "fullDescription": t.string().optional(),
                "title": t.string().optional(),
                "shortDescription": t.string().optional(),
                "video": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsDeobfuscationfilesUpload"] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/apks/{apkVersionCode}/deobfuscationFiles/{deobfuscationFileType}",
        t.struct(
            {
                "deobfuscationFileType": t.string().optional(),
                "packageName": t.string().optional(),
                "apkVersionCode": t.integer().optional(),
                "editId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeobfuscationFilesUploadResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsExpansionfilesUpdate"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/apks/{apkVersionCode}/expansionFiles/{expansionFileType}",
        t.struct(
            {
                "editId": t.string().optional(),
                "apkVersionCode": t.integer().optional(),
                "packageName": t.string().optional(),
                "expansionFileType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExpansionFileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsExpansionfilesPatch"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/apks/{apkVersionCode}/expansionFiles/{expansionFileType}",
        t.struct(
            {
                "editId": t.string().optional(),
                "apkVersionCode": t.integer().optional(),
                "packageName": t.string().optional(),
                "expansionFileType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExpansionFileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsExpansionfilesUpload"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/apks/{apkVersionCode}/expansionFiles/{expansionFileType}",
        t.struct(
            {
                "editId": t.string().optional(),
                "apkVersionCode": t.integer().optional(),
                "packageName": t.string().optional(),
                "expansionFileType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExpansionFileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsExpansionfilesGet"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/apks/{apkVersionCode}/expansionFiles/{expansionFileType}",
        t.struct(
            {
                "editId": t.string().optional(),
                "apkVersionCode": t.integer().optional(),
                "packageName": t.string().optional(),
                "expansionFileType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExpansionFileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsTestersUpdate"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/testers/{track}",
        t.struct(
            {
                "track": t.string().optional(),
                "packageName": t.string().optional(),
                "editId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestersOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsTestersPatch"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/testers/{track}",
        t.struct(
            {
                "track": t.string().optional(),
                "packageName": t.string().optional(),
                "editId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestersOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsTestersGet"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/testers/{track}",
        t.struct(
            {
                "track": t.string().optional(),
                "packageName": t.string().optional(),
                "editId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestersOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsBundlesList"] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/bundles",
        t.struct(
            {
                "ackBundleInstallationWarning": t.boolean().optional(),
                "editId": t.string().optional(),
                "packageName": t.string().optional(),
                "deviceTierConfigId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BundleOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsBundlesUpload"] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/bundles",
        t.struct(
            {
                "ackBundleInstallationWarning": t.boolean().optional(),
                "editId": t.string().optional(),
                "packageName": t.string().optional(),
                "deviceTierConfigId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BundleOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsApksUpload"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/apks",
        t.struct(
            {
                "editId": t.string().optional(),
                "packageName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApksListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsApksAddexternallyhosted"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/apks",
        t.struct(
            {
                "editId": t.string().optional(),
                "packageName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApksListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsApksList"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/apks",
        t.struct(
            {
                "editId": t.string().optional(),
                "packageName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApksListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["grantsDelete"] = androidpublisher.post(
        "androidpublisher/v3/{parent}/grants",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string(),
                "packageName": t.string().optional(),
                "appLevelPermissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GrantOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["grantsPatch"] = androidpublisher.post(
        "androidpublisher/v3/{parent}/grants",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string(),
                "packageName": t.string().optional(),
                "appLevelPermissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GrantOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["grantsCreate"] = androidpublisher.post(
        "androidpublisher/v3/{parent}/grants",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string(),
                "packageName": t.string().optional(),
                "appLevelPermissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GrantOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersDelete"] = androidpublisher.get(
        "androidpublisher/v3/{parent}/users",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListUsersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersCreate"] = androidpublisher.get(
        "androidpublisher/v3/{parent}/users",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListUsersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersPatch"] = androidpublisher.get(
        "androidpublisher/v3/{parent}/users",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListUsersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersList"] = androidpublisher.get(
        "androidpublisher/v3/{parent}/users",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListUsersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["applicationsDeviceTierConfigsGet"] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/deviceTierConfigs",
        t.struct(
            {
                "allowUnknownDevices": t.boolean().optional(),
                "packageName": t.string().optional(),
                "userCountrySets": t.array(
                    t.proxy(renames["UserCountrySetIn"])
                ).optional(),
                "deviceGroups": t.array(t.proxy(renames["DeviceGroupIn"])).optional(),
                "deviceTierSet": t.proxy(renames["DeviceTierSetIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeviceTierConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["applicationsDeviceTierConfigsList"] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/deviceTierConfigs",
        t.struct(
            {
                "allowUnknownDevices": t.boolean().optional(),
                "packageName": t.string().optional(),
                "userCountrySets": t.array(
                    t.proxy(renames["UserCountrySetIn"])
                ).optional(),
                "deviceGroups": t.array(t.proxy(renames["DeviceGroupIn"])).optional(),
                "deviceTierSet": t.proxy(renames["DeviceTierSetIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeviceTierConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["applicationsDeviceTierConfigsCreate"] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/deviceTierConfigs",
        t.struct(
            {
                "allowUnknownDevices": t.boolean().optional(),
                "packageName": t.string().optional(),
                "userCountrySets": t.array(
                    t.proxy(renames["UserCountrySetIn"])
                ).optional(),
                "deviceGroups": t.array(t.proxy(renames["DeviceGroupIn"])).optional(),
                "deviceTierSet": t.proxy(renames["DeviceTierSetIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeviceTierConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inappproductsPatch"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/inappproducts",
        t.struct(
            {
                "packageName": t.string().optional(),
                "token": t.string().optional(),
                "maxResults": t.integer().optional(),
                "startIndex": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InappproductsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inappproductsInsert"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/inappproducts",
        t.struct(
            {
                "packageName": t.string().optional(),
                "token": t.string().optional(),
                "maxResults": t.integer().optional(),
                "startIndex": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InappproductsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inappproductsGet"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/inappproducts",
        t.struct(
            {
                "packageName": t.string().optional(),
                "token": t.string().optional(),
                "maxResults": t.integer().optional(),
                "startIndex": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InappproductsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inappproductsUpdate"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/inappproducts",
        t.struct(
            {
                "packageName": t.string().optional(),
                "token": t.string().optional(),
                "maxResults": t.integer().optional(),
                "startIndex": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InappproductsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inappproductsDelete"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/inappproducts",
        t.struct(
            {
                "packageName": t.string().optional(),
                "token": t.string().optional(),
                "maxResults": t.integer().optional(),
                "startIndex": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InappproductsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inappproductsList"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/inappproducts",
        t.struct(
            {
                "packageName": t.string().optional(),
                "token": t.string().optional(),
                "maxResults": t.integer().optional(),
                "startIndex": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InappproductsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["internalappsharingartifactsUploadbundle"] = androidpublisher.post(
        "androidpublisher/v3/applications/internalappsharing/{packageName}/artifacts/apk",
        t.struct({"packageName": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["InternalAppSharingArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["internalappsharingartifactsUploadapk"] = androidpublisher.post(
        "androidpublisher/v3/applications/internalappsharing/{packageName}/artifacts/apk",
        t.struct({"packageName": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["InternalAppSharingArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["systemapksVariantsList"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/systemApks/{versionCode}/variants/{variantId}",
        t.struct(
            {
                "packageName": t.string().optional(),
                "versionCode": t.string().optional(),
                "variantId": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VariantOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["systemapksVariantsCreate"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/systemApks/{versionCode}/variants/{variantId}",
        t.struct(
            {
                "packageName": t.string().optional(),
                "versionCode": t.string().optional(),
                "variantId": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VariantOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["systemapksVariantsDownload"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/systemApks/{versionCode}/variants/{variantId}",
        t.struct(
            {
                "packageName": t.string().optional(),
                "versionCode": t.string().optional(),
                "variantId": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VariantOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["systemapksVariantsGet"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/systemApks/{versionCode}/variants/{variantId}",
        t.struct(
            {
                "packageName": t.string().optional(),
                "versionCode": t.string().optional(),
                "variantId": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VariantOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["reviewsReply"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/reviews/{reviewId}",
        t.struct(
            {
                "packageName": t.string().optional(),
                "reviewId": t.string().optional(),
                "translationLanguage": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReviewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["reviewsList"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/reviews/{reviewId}",
        t.struct(
            {
                "packageName": t.string().optional(),
                "reviewId": t.string().optional(),
                "translationLanguage": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReviewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["reviewsGet"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/reviews/{reviewId}",
        t.struct(
            {
                "packageName": t.string().optional(),
                "reviewId": t.string().optional(),
                "translationLanguage": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReviewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="androidpublisher",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
