from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_androidpublisher() -> Import:
    androidpublisher = HTTPRuntime("https://androidpublisher.googleapis.com/")

    renames = {
        "ErrorResponse": "_androidpublisher_1_ErrorResponse",
        "ExternallyHostedApkIn": "_androidpublisher_2_ExternallyHostedApkIn",
        "ExternallyHostedApkOut": "_androidpublisher_3_ExternallyHostedApkOut",
        "TestersIn": "_androidpublisher_4_TestersIn",
        "TestersOut": "_androidpublisher_5_TestersOut",
        "SystemFeatureIn": "_androidpublisher_6_SystemFeatureIn",
        "SystemFeatureOut": "_androidpublisher_7_SystemFeatureOut",
        "IntroductoryPriceInfoIn": "_androidpublisher_8_IntroductoryPriceInfoIn",
        "IntroductoryPriceInfoOut": "_androidpublisher_9_IntroductoryPriceInfoOut",
        "ActivateSubscriptionOfferRequestIn": "_androidpublisher_10_ActivateSubscriptionOfferRequestIn",
        "ActivateSubscriptionOfferRequestOut": "_androidpublisher_11_ActivateSubscriptionOfferRequestOut",
        "ListingsListResponseIn": "_androidpublisher_12_ListingsListResponseIn",
        "ListingsListResponseOut": "_androidpublisher_13_ListingsListResponseOut",
        "ConvertRegionPricesResponseIn": "_androidpublisher_14_ConvertRegionPricesResponseIn",
        "ConvertRegionPricesResponseOut": "_androidpublisher_15_ConvertRegionPricesResponseOut",
        "TracksListResponseIn": "_androidpublisher_16_TracksListResponseIn",
        "TracksListResponseOut": "_androidpublisher_17_TracksListResponseOut",
        "SubscriptionPurchasesAcknowledgeRequestIn": "_androidpublisher_18_SubscriptionPurchasesAcknowledgeRequestIn",
        "SubscriptionPurchasesAcknowledgeRequestOut": "_androidpublisher_19_SubscriptionPurchasesAcknowledgeRequestOut",
        "ConvertedOtherRegionsPriceIn": "_androidpublisher_20_ConvertedOtherRegionsPriceIn",
        "ConvertedOtherRegionsPriceOut": "_androidpublisher_21_ConvertedOtherRegionsPriceOut",
        "GeneratedSplitApkIn": "_androidpublisher_22_GeneratedSplitApkIn",
        "GeneratedSplitApkOut": "_androidpublisher_23_GeneratedSplitApkOut",
        "ExternalTransactionAddressIn": "_androidpublisher_24_ExternalTransactionAddressIn",
        "ExternalTransactionAddressOut": "_androidpublisher_25_ExternalTransactionAddressOut",
        "DeactivateSubscriptionOfferRequestIn": "_androidpublisher_26_DeactivateSubscriptionOfferRequestIn",
        "DeactivateSubscriptionOfferRequestOut": "_androidpublisher_27_DeactivateSubscriptionOfferRequestOut",
        "SubscriptionOfferTargetingIn": "_androidpublisher_28_SubscriptionOfferTargetingIn",
        "SubscriptionOfferTargetingOut": "_androidpublisher_29_SubscriptionOfferTargetingOut",
        "SubscriptionPriceChangeIn": "_androidpublisher_30_SubscriptionPriceChangeIn",
        "SubscriptionPriceChangeOut": "_androidpublisher_31_SubscriptionPriceChangeOut",
        "OfferTagIn": "_androidpublisher_32_OfferTagIn",
        "OfferTagOut": "_androidpublisher_33_OfferTagOut",
        "RegionsVersionIn": "_androidpublisher_34_RegionsVersionIn",
        "RegionsVersionOut": "_androidpublisher_35_RegionsVersionOut",
        "VoidedPurchaseIn": "_androidpublisher_36_VoidedPurchaseIn",
        "VoidedPurchaseOut": "_androidpublisher_37_VoidedPurchaseOut",
        "RegionalTaxRateInfoIn": "_androidpublisher_38_RegionalTaxRateInfoIn",
        "RegionalTaxRateInfoOut": "_androidpublisher_39_RegionalTaxRateInfoOut",
        "MigrateBasePlanPricesRequestIn": "_androidpublisher_40_MigrateBasePlanPricesRequestIn",
        "MigrateBasePlanPricesRequestOut": "_androidpublisher_41_MigrateBasePlanPricesRequestOut",
        "GeneratedStandaloneApkIn": "_androidpublisher_42_GeneratedStandaloneApkIn",
        "GeneratedStandaloneApkOut": "_androidpublisher_43_GeneratedStandaloneApkOut",
        "ReviewReplyResultIn": "_androidpublisher_44_ReviewReplyResultIn",
        "ReviewReplyResultOut": "_androidpublisher_45_ReviewReplyResultOut",
        "ActivateBasePlanRequestIn": "_androidpublisher_46_ActivateBasePlanRequestIn",
        "ActivateBasePlanRequestOut": "_androidpublisher_47_ActivateBasePlanRequestOut",
        "UsesPermissionIn": "_androidpublisher_48_UsesPermissionIn",
        "UsesPermissionOut": "_androidpublisher_49_UsesPermissionOut",
        "VoidedPurchasesListResponseIn": "_androidpublisher_50_VoidedPurchasesListResponseIn",
        "VoidedPurchasesListResponseOut": "_androidpublisher_51_VoidedPurchasesListResponseOut",
        "InAppProductIn": "_androidpublisher_52_InAppProductIn",
        "InAppProductOut": "_androidpublisher_53_InAppProductOut",
        "UserCommentIn": "_androidpublisher_54_UserCommentIn",
        "UserCommentOut": "_androidpublisher_55_UserCommentOut",
        "TestPurchaseIn": "_androidpublisher_56_TestPurchaseIn",
        "TestPurchaseOut": "_androidpublisher_57_TestPurchaseOut",
        "SubscriptionCancelSurveyResultIn": "_androidpublisher_58_SubscriptionCancelSurveyResultIn",
        "SubscriptionCancelSurveyResultOut": "_androidpublisher_59_SubscriptionCancelSurveyResultOut",
        "DeviceGroupIn": "_androidpublisher_60_DeviceGroupIn",
        "DeviceGroupOut": "_androidpublisher_61_DeviceGroupOut",
        "DeviceTierIn": "_androidpublisher_62_DeviceTierIn",
        "DeviceTierOut": "_androidpublisher_63_DeviceTierOut",
        "PriceIn": "_androidpublisher_64_PriceIn",
        "PriceOut": "_androidpublisher_65_PriceOut",
        "DeviceMetadataIn": "_androidpublisher_66_DeviceMetadataIn",
        "DeviceMetadataOut": "_androidpublisher_67_DeviceMetadataOut",
        "ConvertedRegionPriceIn": "_androidpublisher_68_ConvertedRegionPriceIn",
        "ConvertedRegionPriceOut": "_androidpublisher_69_ConvertedRegionPriceOut",
        "PageInfoIn": "_androidpublisher_70_PageInfoIn",
        "PageInfoOut": "_androidpublisher_71_PageInfoOut",
        "GeneratedUniversalApkIn": "_androidpublisher_72_GeneratedUniversalApkIn",
        "GeneratedUniversalApkOut": "_androidpublisher_73_GeneratedUniversalApkOut",
        "PrepaidPlanIn": "_androidpublisher_74_PrepaidPlanIn",
        "PrepaidPlanOut": "_androidpublisher_75_PrepaidPlanOut",
        "InAppProductListingIn": "_androidpublisher_76_InAppProductListingIn",
        "InAppProductListingOut": "_androidpublisher_77_InAppProductListingOut",
        "SubscriptionListingIn": "_androidpublisher_78_SubscriptionListingIn",
        "SubscriptionListingOut": "_androidpublisher_79_SubscriptionListingOut",
        "ReviewsListResponseIn": "_androidpublisher_80_ReviewsListResponseIn",
        "ReviewsListResponseOut": "_androidpublisher_81_ReviewsListResponseOut",
        "ImageIn": "_androidpublisher_82_ImageIn",
        "ImageOut": "_androidpublisher_83_ImageOut",
        "SubscriptionOfferIn": "_androidpublisher_84_SubscriptionOfferIn",
        "SubscriptionOfferOut": "_androidpublisher_85_SubscriptionOfferOut",
        "DeviceRamIn": "_androidpublisher_86_DeviceRamIn",
        "DeviceRamOut": "_androidpublisher_87_DeviceRamOut",
        "InternalAppSharingArtifactIn": "_androidpublisher_88_InternalAppSharingArtifactIn",
        "InternalAppSharingArtifactOut": "_androidpublisher_89_InternalAppSharingArtifactOut",
        "ListDeviceTierConfigsResponseIn": "_androidpublisher_90_ListDeviceTierConfigsResponseIn",
        "ListDeviceTierConfigsResponseOut": "_androidpublisher_91_ListDeviceTierConfigsResponseOut",
        "DeviceTierConfigIn": "_androidpublisher_92_DeviceTierConfigIn",
        "DeviceTierConfigOut": "_androidpublisher_93_DeviceTierConfigOut",
        "ReplacementCancellationIn": "_androidpublisher_94_ReplacementCancellationIn",
        "ReplacementCancellationOut": "_androidpublisher_95_ReplacementCancellationOut",
        "FullRefundIn": "_androidpublisher_96_FullRefundIn",
        "FullRefundOut": "_androidpublisher_97_FullRefundOut",
        "DeviceIdIn": "_androidpublisher_98_DeviceIdIn",
        "DeviceIdOut": "_androidpublisher_99_DeviceIdOut",
        "GeneratedApksListResponseIn": "_androidpublisher_100_GeneratedApksListResponseIn",
        "GeneratedApksListResponseOut": "_androidpublisher_101_GeneratedApksListResponseOut",
        "ImagesDeleteAllResponseIn": "_androidpublisher_102_ImagesDeleteAllResponseIn",
        "ImagesDeleteAllResponseOut": "_androidpublisher_103_ImagesDeleteAllResponseOut",
        "OtherRegionsSubscriptionOfferPhasePricesIn": "_androidpublisher_104_OtherRegionsSubscriptionOfferPhasePricesIn",
        "OtherRegionsSubscriptionOfferPhasePricesOut": "_androidpublisher_105_OtherRegionsSubscriptionOfferPhasePricesOut",
        "PartialRefundIn": "_androidpublisher_106_PartialRefundIn",
        "PartialRefundOut": "_androidpublisher_107_PartialRefundOut",
        "DeviceSpecIn": "_androidpublisher_108_DeviceSpecIn",
        "DeviceSpecOut": "_androidpublisher_109_DeviceSpecOut",
        "SubscriptionItemPriceChangeDetailsIn": "_androidpublisher_110_SubscriptionItemPriceChangeDetailsIn",
        "SubscriptionItemPriceChangeDetailsOut": "_androidpublisher_111_SubscriptionItemPriceChangeDetailsOut",
        "DeactivateBasePlanRequestIn": "_androidpublisher_112_DeactivateBasePlanRequestIn",
        "DeactivateBasePlanRequestOut": "_androidpublisher_113_DeactivateBasePlanRequestOut",
        "MoneyIn": "_androidpublisher_114_MoneyIn",
        "MoneyOut": "_androidpublisher_115_MoneyOut",
        "GeneratedApksPerSigningKeyIn": "_androidpublisher_116_GeneratedApksPerSigningKeyIn",
        "GeneratedApksPerSigningKeyOut": "_androidpublisher_117_GeneratedApksPerSigningKeyOut",
        "InappproductsListResponseIn": "_androidpublisher_118_InappproductsListResponseIn",
        "InappproductsListResponseOut": "_androidpublisher_119_InappproductsListResponseOut",
        "CommentIn": "_androidpublisher_120_CommentIn",
        "CommentOut": "_androidpublisher_121_CommentOut",
        "DeobfuscationFileIn": "_androidpublisher_122_DeobfuscationFileIn",
        "DeobfuscationFileOut": "_androidpublisher_123_DeobfuscationFileOut",
        "ApkBinaryIn": "_androidpublisher_124_ApkBinaryIn",
        "ApkBinaryOut": "_androidpublisher_125_ApkBinaryOut",
        "ImagesListResponseIn": "_androidpublisher_126_ImagesListResponseIn",
        "ImagesListResponseOut": "_androidpublisher_127_ImagesListResponseOut",
        "RegionalPriceMigrationConfigIn": "_androidpublisher_128_RegionalPriceMigrationConfigIn",
        "RegionalPriceMigrationConfigOut": "_androidpublisher_129_RegionalPriceMigrationConfigOut",
        "DeviceTierSetIn": "_androidpublisher_130_DeviceTierSetIn",
        "DeviceTierSetOut": "_androidpublisher_131_DeviceTierSetOut",
        "UserIn": "_androidpublisher_132_UserIn",
        "UserOut": "_androidpublisher_133_UserOut",
        "RegionalSubscriptionOfferConfigIn": "_androidpublisher_134_RegionalSubscriptionOfferConfigIn",
        "RegionalSubscriptionOfferConfigOut": "_androidpublisher_135_RegionalSubscriptionOfferConfigOut",
        "ProductPurchasesAcknowledgeRequestIn": "_androidpublisher_136_ProductPurchasesAcknowledgeRequestIn",
        "ProductPurchasesAcknowledgeRequestOut": "_androidpublisher_137_ProductPurchasesAcknowledgeRequestOut",
        "TrackCountryAvailabilityIn": "_androidpublisher_138_TrackCountryAvailabilityIn",
        "TrackCountryAvailabilityOut": "_androidpublisher_139_TrackCountryAvailabilityOut",
        "PrepaidBasePlanTypeIn": "_androidpublisher_140_PrepaidBasePlanTypeIn",
        "PrepaidBasePlanTypeOut": "_androidpublisher_141_PrepaidBasePlanTypeOut",
        "SubscriptionOfferPhaseIn": "_androidpublisher_142_SubscriptionOfferPhaseIn",
        "SubscriptionOfferPhaseOut": "_androidpublisher_143_SubscriptionOfferPhaseOut",
        "BasePlanIn": "_androidpublisher_144_BasePlanIn",
        "BasePlanOut": "_androidpublisher_145_BasePlanOut",
        "SubscriptionPurchaseIn": "_androidpublisher_146_SubscriptionPurchaseIn",
        "SubscriptionPurchaseOut": "_androidpublisher_147_SubscriptionPurchaseOut",
        "OtherRegionsSubscriptionOfferPhaseConfigIn": "_androidpublisher_148_OtherRegionsSubscriptionOfferPhaseConfigIn",
        "OtherRegionsSubscriptionOfferPhaseConfigOut": "_androidpublisher_149_OtherRegionsSubscriptionOfferPhaseConfigOut",
        "CancelSurveyResultIn": "_androidpublisher_150_CancelSurveyResultIn",
        "CancelSurveyResultOut": "_androidpublisher_151_CancelSurveyResultOut",
        "RegionalBasePlanConfigIn": "_androidpublisher_152_RegionalBasePlanConfigIn",
        "RegionalBasePlanConfigOut": "_androidpublisher_153_RegionalBasePlanConfigOut",
        "AcquisitionTargetingRuleIn": "_androidpublisher_154_AcquisitionTargetingRuleIn",
        "AcquisitionTargetingRuleOut": "_androidpublisher_155_AcquisitionTargetingRuleOut",
        "ListSubscriptionOffersResponseIn": "_androidpublisher_156_ListSubscriptionOffersResponseIn",
        "ListSubscriptionOffersResponseOut": "_androidpublisher_157_ListSubscriptionOffersResponseOut",
        "CountryTargetingIn": "_androidpublisher_158_CountryTargetingIn",
        "CountryTargetingOut": "_androidpublisher_159_CountryTargetingOut",
        "AutoRenewingBasePlanTypeIn": "_androidpublisher_160_AutoRenewingBasePlanTypeIn",
        "AutoRenewingBasePlanTypeOut": "_androidpublisher_161_AutoRenewingBasePlanTypeOut",
        "BundleIn": "_androidpublisher_162_BundleIn",
        "BundleOut": "_androidpublisher_163_BundleOut",
        "MigrateBasePlanPricesResponseIn": "_androidpublisher_164_MigrateBasePlanPricesResponseIn",
        "MigrateBasePlanPricesResponseOut": "_androidpublisher_165_MigrateBasePlanPricesResponseOut",
        "AppDetailsIn": "_androidpublisher_166_AppDetailsIn",
        "AppDetailsOut": "_androidpublisher_167_AppDetailsOut",
        "TargetingRuleScopeIn": "_androidpublisher_168_TargetingRuleScopeIn",
        "TargetingRuleScopeOut": "_androidpublisher_169_TargetingRuleScopeOut",
        "ExpansionFileIn": "_androidpublisher_170_ExpansionFileIn",
        "ExpansionFileOut": "_androidpublisher_171_ExpansionFileOut",
        "OtherRegionsBasePlanConfigIn": "_androidpublisher_172_OtherRegionsBasePlanConfigIn",
        "OtherRegionsBasePlanConfigOut": "_androidpublisher_173_OtherRegionsBasePlanConfigOut",
        "ExternalTransactionTestPurchaseIn": "_androidpublisher_174_ExternalTransactionTestPurchaseIn",
        "ExternalTransactionTestPurchaseOut": "_androidpublisher_175_ExternalTransactionTestPurchaseOut",
        "ReviewIn": "_androidpublisher_176_ReviewIn",
        "ReviewOut": "_androidpublisher_177_ReviewOut",
        "SubscriptionPurchasesDeferRequestIn": "_androidpublisher_178_SubscriptionPurchasesDeferRequestIn",
        "SubscriptionPurchasesDeferRequestOut": "_androidpublisher_179_SubscriptionPurchasesDeferRequestOut",
        "OfferDetailsIn": "_androidpublisher_180_OfferDetailsIn",
        "OfferDetailsOut": "_androidpublisher_181_OfferDetailsOut",
        "ExpansionFilesUploadResponseIn": "_androidpublisher_182_ExpansionFilesUploadResponseIn",
        "ExpansionFilesUploadResponseOut": "_androidpublisher_183_ExpansionFilesUploadResponseOut",
        "RecurringExternalTransactionIn": "_androidpublisher_184_RecurringExternalTransactionIn",
        "RecurringExternalTransactionOut": "_androidpublisher_185_RecurringExternalTransactionOut",
        "SystemApksListResponseIn": "_androidpublisher_186_SystemApksListResponseIn",
        "SystemApksListResponseOut": "_androidpublisher_187_SystemApksListResponseOut",
        "BundlesListResponseIn": "_androidpublisher_188_BundlesListResponseIn",
        "BundlesListResponseOut": "_androidpublisher_189_BundlesListResponseOut",
        "ManagedProductTaxAndComplianceSettingsIn": "_androidpublisher_190_ManagedProductTaxAndComplianceSettingsIn",
        "ManagedProductTaxAndComplianceSettingsOut": "_androidpublisher_191_ManagedProductTaxAndComplianceSettingsOut",
        "ListSubscriptionsResponseIn": "_androidpublisher_192_ListSubscriptionsResponseIn",
        "ListSubscriptionsResponseOut": "_androidpublisher_193_ListSubscriptionsResponseOut",
        "ProductPurchaseIn": "_androidpublisher_194_ProductPurchaseIn",
        "ProductPurchaseOut": "_androidpublisher_195_ProductPurchaseOut",
        "DeviceSelectorIn": "_androidpublisher_196_DeviceSelectorIn",
        "DeviceSelectorOut": "_androidpublisher_197_DeviceSelectorOut",
        "ArchiveSubscriptionRequestIn": "_androidpublisher_198_ArchiveSubscriptionRequestIn",
        "ArchiveSubscriptionRequestOut": "_androidpublisher_199_ArchiveSubscriptionRequestOut",
        "AppEditIn": "_androidpublisher_200_AppEditIn",
        "AppEditOut": "_androidpublisher_201_AppEditOut",
        "GrantIn": "_androidpublisher_202_GrantIn",
        "GrantOut": "_androidpublisher_203_GrantOut",
        "DeobfuscationFilesUploadResponseIn": "_androidpublisher_204_DeobfuscationFilesUploadResponseIn",
        "DeobfuscationFilesUploadResponseOut": "_androidpublisher_205_DeobfuscationFilesUploadResponseOut",
        "ExternalSubscriptionIn": "_androidpublisher_206_ExternalSubscriptionIn",
        "ExternalSubscriptionOut": "_androidpublisher_207_ExternalSubscriptionOut",
        "ImagesUploadResponseIn": "_androidpublisher_208_ImagesUploadResponseIn",
        "ImagesUploadResponseOut": "_androidpublisher_209_ImagesUploadResponseOut",
        "ReviewsReplyResponseIn": "_androidpublisher_210_ReviewsReplyResponseIn",
        "ReviewsReplyResponseOut": "_androidpublisher_211_ReviewsReplyResponseOut",
        "TrackIn": "_androidpublisher_212_TrackIn",
        "TrackOut": "_androidpublisher_213_TrackOut",
        "TimestampIn": "_androidpublisher_214_TimestampIn",
        "TimestampOut": "_androidpublisher_215_TimestampOut",
        "RegionalSubscriptionOfferPhaseConfigIn": "_androidpublisher_216_RegionalSubscriptionOfferPhaseConfigIn",
        "RegionalSubscriptionOfferPhaseConfigOut": "_androidpublisher_217_RegionalSubscriptionOfferPhaseConfigOut",
        "SubscriptionPurchaseLineItemIn": "_androidpublisher_218_SubscriptionPurchaseLineItemIn",
        "SubscriptionPurchaseLineItemOut": "_androidpublisher_219_SubscriptionPurchaseLineItemOut",
        "TokenPaginationIn": "_androidpublisher_220_TokenPaginationIn",
        "TokenPaginationOut": "_androidpublisher_221_TokenPaginationOut",
        "ApksAddExternallyHostedRequestIn": "_androidpublisher_222_ApksAddExternallyHostedRequestIn",
        "ApksAddExternallyHostedRequestOut": "_androidpublisher_223_ApksAddExternallyHostedRequestOut",
        "SubscriptionTaxAndComplianceSettingsIn": "_androidpublisher_224_SubscriptionTaxAndComplianceSettingsIn",
        "SubscriptionTaxAndComplianceSettingsOut": "_androidpublisher_225_SubscriptionTaxAndComplianceSettingsOut",
        "GeneratedAssetPackSliceIn": "_androidpublisher_226_GeneratedAssetPackSliceIn",
        "GeneratedAssetPackSliceOut": "_androidpublisher_227_GeneratedAssetPackSliceOut",
        "DeveloperInitiatedCancellationIn": "_androidpublisher_228_DeveloperInitiatedCancellationIn",
        "DeveloperInitiatedCancellationOut": "_androidpublisher_229_DeveloperInitiatedCancellationOut",
        "DeveloperCommentIn": "_androidpublisher_230_DeveloperCommentIn",
        "DeveloperCommentOut": "_androidpublisher_231_DeveloperCommentOut",
        "UserCountrySetIn": "_androidpublisher_232_UserCountrySetIn",
        "UserCountrySetOut": "_androidpublisher_233_UserCountrySetOut",
        "SubscriptionDeferralInfoIn": "_androidpublisher_234_SubscriptionDeferralInfoIn",
        "SubscriptionDeferralInfoOut": "_androidpublisher_235_SubscriptionDeferralInfoOut",
        "CanceledStateContextIn": "_androidpublisher_236_CanceledStateContextIn",
        "CanceledStateContextOut": "_androidpublisher_237_CanceledStateContextOut",
        "ApksListResponseIn": "_androidpublisher_238_ApksListResponseIn",
        "ApksListResponseOut": "_androidpublisher_239_ApksListResponseOut",
        "ExternalAccountIdentifiersIn": "_androidpublisher_240_ExternalAccountIdentifiersIn",
        "ExternalAccountIdentifiersOut": "_androidpublisher_241_ExternalAccountIdentifiersOut",
        "ListingIn": "_androidpublisher_242_ListingIn",
        "ListingOut": "_androidpublisher_243_ListingOut",
        "TrackReleaseIn": "_androidpublisher_244_TrackReleaseIn",
        "TrackReleaseOut": "_androidpublisher_245_TrackReleaseOut",
        "OtherRegionsSubscriptionOfferConfigIn": "_androidpublisher_246_OtherRegionsSubscriptionOfferConfigIn",
        "OtherRegionsSubscriptionOfferConfigOut": "_androidpublisher_247_OtherRegionsSubscriptionOfferConfigOut",
        "LocalizedTextIn": "_androidpublisher_248_LocalizedTextIn",
        "LocalizedTextOut": "_androidpublisher_249_LocalizedTextOut",
        "ApksAddExternallyHostedResponseIn": "_androidpublisher_250_ApksAddExternallyHostedResponseIn",
        "ApksAddExternallyHostedResponseOut": "_androidpublisher_251_ApksAddExternallyHostedResponseOut",
        "TrackTargetedCountryIn": "_androidpublisher_252_TrackTargetedCountryIn",
        "TrackTargetedCountryOut": "_androidpublisher_253_TrackTargetedCountryOut",
        "SubscriptionIn": "_androidpublisher_254_SubscriptionIn",
        "SubscriptionOut": "_androidpublisher_255_SubscriptionOut",
        "ListUsersResponseIn": "_androidpublisher_256_ListUsersResponseIn",
        "ListUsersResponseOut": "_androidpublisher_257_ListUsersResponseOut",
        "SystemInitiatedCancellationIn": "_androidpublisher_258_SystemInitiatedCancellationIn",
        "SystemInitiatedCancellationOut": "_androidpublisher_259_SystemInitiatedCancellationOut",
        "AutoRenewingPlanIn": "_androidpublisher_260_AutoRenewingPlanIn",
        "AutoRenewingPlanOut": "_androidpublisher_261_AutoRenewingPlanOut",
        "ReviewsReplyRequestIn": "_androidpublisher_262_ReviewsReplyRequestIn",
        "ReviewsReplyRequestOut": "_androidpublisher_263_ReviewsReplyRequestOut",
        "UserInitiatedCancellationIn": "_androidpublisher_264_UserInitiatedCancellationIn",
        "UserInitiatedCancellationOut": "_androidpublisher_265_UserInitiatedCancellationOut",
        "OneTimeExternalTransactionIn": "_androidpublisher_266_OneTimeExternalTransactionIn",
        "OneTimeExternalTransactionOut": "_androidpublisher_267_OneTimeExternalTransactionOut",
        "RefundExternalTransactionRequestIn": "_androidpublisher_268_RefundExternalTransactionRequestIn",
        "RefundExternalTransactionRequestOut": "_androidpublisher_269_RefundExternalTransactionRequestOut",
        "SubscriptionPurchasesDeferResponseIn": "_androidpublisher_270_SubscriptionPurchasesDeferResponseIn",
        "SubscriptionPurchasesDeferResponseOut": "_androidpublisher_271_SubscriptionPurchasesDeferResponseOut",
        "SubscribeWithGoogleInfoIn": "_androidpublisher_272_SubscribeWithGoogleInfoIn",
        "SubscribeWithGoogleInfoOut": "_androidpublisher_273_SubscribeWithGoogleInfoOut",
        "ExternalTransactionIn": "_androidpublisher_274_ExternalTransactionIn",
        "ExternalTransactionOut": "_androidpublisher_275_ExternalTransactionOut",
        "SubscriptionPurchaseV2In": "_androidpublisher_276_SubscriptionPurchaseV2In",
        "SubscriptionPurchaseV2Out": "_androidpublisher_277_SubscriptionPurchaseV2Out",
        "ApkIn": "_androidpublisher_278_ApkIn",
        "ApkOut": "_androidpublisher_279_ApkOut",
        "UpgradeTargetingRuleIn": "_androidpublisher_280_UpgradeTargetingRuleIn",
        "UpgradeTargetingRuleOut": "_androidpublisher_281_UpgradeTargetingRuleOut",
        "PausedStateContextIn": "_androidpublisher_282_PausedStateContextIn",
        "PausedStateContextOut": "_androidpublisher_283_PausedStateContextOut",
        "VariantIn": "_androidpublisher_284_VariantIn",
        "VariantOut": "_androidpublisher_285_VariantOut",
        "ConvertRegionPricesRequestIn": "_androidpublisher_286_ConvertRegionPricesRequestIn",
        "ConvertRegionPricesRequestOut": "_androidpublisher_287_ConvertRegionPricesRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ExternallyHostedApkIn"] = t.struct(
        {
            "versionCode": t.integer().optional(),
            "fileSize": t.string().optional(),
            "usesPermissions": t.array(t.proxy(renames["UsesPermissionIn"])).optional(),
            "iconBase64": t.string().optional(),
            "nativeCodes": t.array(t.string()).optional(),
            "packageName": t.string().optional(),
            "fileSha256Base64": t.string().optional(),
            "applicationLabel": t.string().optional(),
            "certificateBase64s": t.array(t.string()).optional(),
            "maximumSdk": t.integer().optional(),
            "usesFeatures": t.array(t.string()).optional(),
            "minimumSdk": t.integer().optional(),
            "fileSha1Base64": t.string().optional(),
            "externallyHostedUrl": t.string().optional(),
            "versionName": t.string().optional(),
        }
    ).named(renames["ExternallyHostedApkIn"])
    types["ExternallyHostedApkOut"] = t.struct(
        {
            "versionCode": t.integer().optional(),
            "fileSize": t.string().optional(),
            "usesPermissions": t.array(
                t.proxy(renames["UsesPermissionOut"])
            ).optional(),
            "iconBase64": t.string().optional(),
            "nativeCodes": t.array(t.string()).optional(),
            "packageName": t.string().optional(),
            "fileSha256Base64": t.string().optional(),
            "applicationLabel": t.string().optional(),
            "certificateBase64s": t.array(t.string()).optional(),
            "maximumSdk": t.integer().optional(),
            "usesFeatures": t.array(t.string()).optional(),
            "minimumSdk": t.integer().optional(),
            "fileSha1Base64": t.string().optional(),
            "externallyHostedUrl": t.string().optional(),
            "versionName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExternallyHostedApkOut"])
    types["TestersIn"] = t.struct(
        {"googleGroups": t.array(t.string()).optional()}
    ).named(renames["TestersIn"])
    types["TestersOut"] = t.struct(
        {
            "googleGroups": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestersOut"])
    types["SystemFeatureIn"] = t.struct({"name": t.string().optional()}).named(
        renames["SystemFeatureIn"]
    )
    types["SystemFeatureOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SystemFeatureOut"])
    types["IntroductoryPriceInfoIn"] = t.struct(
        {
            "introductoryPriceCurrencyCode": t.string().optional(),
            "introductoryPriceCycles": t.integer().optional(),
            "introductoryPricePeriod": t.string().optional(),
            "introductoryPriceAmountMicros": t.string().optional(),
        }
    ).named(renames["IntroductoryPriceInfoIn"])
    types["IntroductoryPriceInfoOut"] = t.struct(
        {
            "introductoryPriceCurrencyCode": t.string().optional(),
            "introductoryPriceCycles": t.integer().optional(),
            "introductoryPricePeriod": t.string().optional(),
            "introductoryPriceAmountMicros": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntroductoryPriceInfoOut"])
    types["ActivateSubscriptionOfferRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ActivateSubscriptionOfferRequestIn"])
    types["ActivateSubscriptionOfferRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ActivateSubscriptionOfferRequestOut"])
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
    types["ConvertRegionPricesResponseIn"] = t.struct(
        {
            "convertedOtherRegionsPrice": t.proxy(
                renames["ConvertedOtherRegionsPriceIn"]
            ).optional(),
            "convertedRegionPrices": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ConvertRegionPricesResponseIn"])
    types["ConvertRegionPricesResponseOut"] = t.struct(
        {
            "convertedOtherRegionsPrice": t.proxy(
                renames["ConvertedOtherRegionsPriceOut"]
            ).optional(),
            "convertedRegionPrices": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConvertRegionPricesResponseOut"])
    types["TracksListResponseIn"] = t.struct(
        {
            "tracks": t.array(t.proxy(renames["TrackIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["TracksListResponseIn"])
    types["TracksListResponseOut"] = t.struct(
        {
            "tracks": t.array(t.proxy(renames["TrackOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TracksListResponseOut"])
    types["SubscriptionPurchasesAcknowledgeRequestIn"] = t.struct(
        {"developerPayload": t.string().optional()}
    ).named(renames["SubscriptionPurchasesAcknowledgeRequestIn"])
    types["SubscriptionPurchasesAcknowledgeRequestOut"] = t.struct(
        {
            "developerPayload": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscriptionPurchasesAcknowledgeRequestOut"])
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
    types["GeneratedSplitApkIn"] = t.struct(
        {
            "downloadId": t.string().optional(),
            "splitId": t.string().optional(),
            "variantId": t.integer().optional(),
            "moduleName": t.string().optional(),
        }
    ).named(renames["GeneratedSplitApkIn"])
    types["GeneratedSplitApkOut"] = t.struct(
        {
            "downloadId": t.string().optional(),
            "splitId": t.string().optional(),
            "variantId": t.integer().optional(),
            "moduleName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GeneratedSplitApkOut"])
    types["ExternalTransactionAddressIn"] = t.struct({"regionCode": t.string()}).named(
        renames["ExternalTransactionAddressIn"]
    )
    types["ExternalTransactionAddressOut"] = t.struct(
        {
            "regionCode": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExternalTransactionAddressOut"])
    types["DeactivateSubscriptionOfferRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DeactivateSubscriptionOfferRequestIn"])
    types["DeactivateSubscriptionOfferRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeactivateSubscriptionOfferRequestOut"])
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
    types["OfferTagIn"] = t.struct({"tag": t.string().optional()}).named(
        renames["OfferTagIn"]
    )
    types["OfferTagOut"] = t.struct(
        {
            "tag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OfferTagOut"])
    types["RegionsVersionIn"] = t.struct({"version": t.string()}).named(
        renames["RegionsVersionIn"]
    )
    types["RegionsVersionOut"] = t.struct(
        {"version": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RegionsVersionOut"])
    types["VoidedPurchaseIn"] = t.struct(
        {
            "purchaseToken": t.string().optional(),
            "voidedReason": t.integer().optional(),
            "purchaseTimeMillis": t.string().optional(),
            "voidedSource": t.integer().optional(),
            "voidedTimeMillis": t.string().optional(),
            "kind": t.string().optional(),
            "orderId": t.string().optional(),
        }
    ).named(renames["VoidedPurchaseIn"])
    types["VoidedPurchaseOut"] = t.struct(
        {
            "purchaseToken": t.string().optional(),
            "voidedReason": t.integer().optional(),
            "purchaseTimeMillis": t.string().optional(),
            "voidedSource": t.integer().optional(),
            "voidedTimeMillis": t.string().optional(),
            "kind": t.string().optional(),
            "orderId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VoidedPurchaseOut"])
    types["RegionalTaxRateInfoIn"] = t.struct(
        {
            "taxTier": t.string().optional(),
            "streamingTaxType": t.string().optional(),
            "eligibleForStreamingServiceTaxRate": t.boolean().optional(),
        }
    ).named(renames["RegionalTaxRateInfoIn"])
    types["RegionalTaxRateInfoOut"] = t.struct(
        {
            "taxTier": t.string().optional(),
            "streamingTaxType": t.string().optional(),
            "eligibleForStreamingServiceTaxRate": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegionalTaxRateInfoOut"])
    types["MigrateBasePlanPricesRequestIn"] = t.struct(
        {
            "regionalPriceMigrations": t.array(
                t.proxy(renames["RegionalPriceMigrationConfigIn"])
            ),
            "regionsVersion": t.proxy(renames["RegionsVersionIn"]),
        }
    ).named(renames["MigrateBasePlanPricesRequestIn"])
    types["MigrateBasePlanPricesRequestOut"] = t.struct(
        {
            "regionalPriceMigrations": t.array(
                t.proxy(renames["RegionalPriceMigrationConfigOut"])
            ),
            "regionsVersion": t.proxy(renames["RegionsVersionOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MigrateBasePlanPricesRequestOut"])
    types["GeneratedStandaloneApkIn"] = t.struct(
        {"variantId": t.integer().optional(), "downloadId": t.string().optional()}
    ).named(renames["GeneratedStandaloneApkIn"])
    types["GeneratedStandaloneApkOut"] = t.struct(
        {
            "variantId": t.integer().optional(),
            "downloadId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GeneratedStandaloneApkOut"])
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
    types["ActivateBasePlanRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ActivateBasePlanRequestIn"]
    )
    types["ActivateBasePlanRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ActivateBasePlanRequestOut"])
    types["UsesPermissionIn"] = t.struct(
        {"name": t.string().optional(), "maxSdkVersion": t.integer().optional()}
    ).named(renames["UsesPermissionIn"])
    types["UsesPermissionOut"] = t.struct(
        {
            "name": t.string().optional(),
            "maxSdkVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UsesPermissionOut"])
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
    types["InAppProductIn"] = t.struct(
        {
            "gracePeriod": t.string().optional(),
            "defaultPrice": t.proxy(renames["PriceIn"]).optional(),
            "subscriptionTaxesAndComplianceSettings": t.proxy(
                renames["SubscriptionTaxAndComplianceSettingsIn"]
            ).optional(),
            "purchaseType": t.string().optional(),
            "prices": t.struct({"_": t.string().optional()}).optional(),
            "defaultLanguage": t.string().optional(),
            "packageName": t.string().optional(),
            "sku": t.string().optional(),
            "managedProductTaxesAndComplianceSettings": t.proxy(
                renames["ManagedProductTaxAndComplianceSettingsIn"]
            ).optional(),
            "trialPeriod": t.string().optional(),
            "listings": t.struct({"_": t.string().optional()}).optional(),
            "subscriptionPeriod": t.string().optional(),
            "status": t.string().optional(),
        }
    ).named(renames["InAppProductIn"])
    types["InAppProductOut"] = t.struct(
        {
            "gracePeriod": t.string().optional(),
            "defaultPrice": t.proxy(renames["PriceOut"]).optional(),
            "subscriptionTaxesAndComplianceSettings": t.proxy(
                renames["SubscriptionTaxAndComplianceSettingsOut"]
            ).optional(),
            "purchaseType": t.string().optional(),
            "prices": t.struct({"_": t.string().optional()}).optional(),
            "defaultLanguage": t.string().optional(),
            "packageName": t.string().optional(),
            "sku": t.string().optional(),
            "managedProductTaxesAndComplianceSettings": t.proxy(
                renames["ManagedProductTaxAndComplianceSettingsOut"]
            ).optional(),
            "trialPeriod": t.string().optional(),
            "listings": t.struct({"_": t.string().optional()}).optional(),
            "subscriptionPeriod": t.string().optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InAppProductOut"])
    types["UserCommentIn"] = t.struct(
        {
            "thumbsDownCount": t.integer().optional(),
            "androidOsVersion": t.integer().optional(),
            "device": t.string().optional(),
            "appVersionCode": t.integer().optional(),
            "lastModified": t.proxy(renames["TimestampIn"]).optional(),
            "text": t.string().optional(),
            "thumbsUpCount": t.integer().optional(),
            "reviewerLanguage": t.string().optional(),
            "originalText": t.string().optional(),
            "appVersionName": t.string().optional(),
            "deviceMetadata": t.proxy(renames["DeviceMetadataIn"]).optional(),
            "starRating": t.integer().optional(),
        }
    ).named(renames["UserCommentIn"])
    types["UserCommentOut"] = t.struct(
        {
            "thumbsDownCount": t.integer().optional(),
            "androidOsVersion": t.integer().optional(),
            "device": t.string().optional(),
            "appVersionCode": t.integer().optional(),
            "lastModified": t.proxy(renames["TimestampOut"]).optional(),
            "text": t.string().optional(),
            "thumbsUpCount": t.integer().optional(),
            "reviewerLanguage": t.string().optional(),
            "originalText": t.string().optional(),
            "appVersionName": t.string().optional(),
            "deviceMetadata": t.proxy(renames["DeviceMetadataOut"]).optional(),
            "starRating": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserCommentOut"])
    types["TestPurchaseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["TestPurchaseIn"]
    )
    types["TestPurchaseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["TestPurchaseOut"])
    types["SubscriptionCancelSurveyResultIn"] = t.struct(
        {
            "userInputCancelReason": t.string().optional(),
            "cancelSurveyReason": t.integer().optional(),
        }
    ).named(renames["SubscriptionCancelSurveyResultIn"])
    types["SubscriptionCancelSurveyResultOut"] = t.struct(
        {
            "userInputCancelReason": t.string().optional(),
            "cancelSurveyReason": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscriptionCancelSurveyResultOut"])
    types["DeviceGroupIn"] = t.struct(
        {
            "deviceSelectors": t.array(t.proxy(renames["DeviceSelectorIn"])).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["DeviceGroupIn"])
    types["DeviceGroupOut"] = t.struct(
        {
            "deviceSelectors": t.array(
                t.proxy(renames["DeviceSelectorOut"])
            ).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceGroupOut"])
    types["DeviceTierIn"] = t.struct(
        {
            "deviceGroupNames": t.array(t.string()).optional(),
            "level": t.integer().optional(),
        }
    ).named(renames["DeviceTierIn"])
    types["DeviceTierOut"] = t.struct(
        {
            "deviceGroupNames": t.array(t.string()).optional(),
            "level": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceTierOut"])
    types["PriceIn"] = t.struct(
        {"currency": t.string().optional(), "priceMicros": t.string().optional()}
    ).named(renames["PriceIn"])
    types["PriceOut"] = t.struct(
        {
            "currency": t.string().optional(),
            "priceMicros": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PriceOut"])
    types["DeviceMetadataIn"] = t.struct(
        {
            "productName": t.string().optional(),
            "glEsVersion": t.integer().optional(),
            "deviceClass": t.string().optional(),
            "ramMb": t.integer().optional(),
            "screenHeightPx": t.integer().optional(),
            "screenDensityDpi": t.integer().optional(),
            "manufacturer": t.string().optional(),
            "cpuMake": t.string().optional(),
            "cpuModel": t.string().optional(),
            "screenWidthPx": t.integer().optional(),
            "nativePlatform": t.string().optional(),
        }
    ).named(renames["DeviceMetadataIn"])
    types["DeviceMetadataOut"] = t.struct(
        {
            "productName": t.string().optional(),
            "glEsVersion": t.integer().optional(),
            "deviceClass": t.string().optional(),
            "ramMb": t.integer().optional(),
            "screenHeightPx": t.integer().optional(),
            "screenDensityDpi": t.integer().optional(),
            "manufacturer": t.string().optional(),
            "cpuMake": t.string().optional(),
            "cpuModel": t.string().optional(),
            "screenWidthPx": t.integer().optional(),
            "nativePlatform": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceMetadataOut"])
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
    types["PageInfoIn"] = t.struct(
        {
            "startIndex": t.integer().optional(),
            "totalResults": t.integer().optional(),
            "resultPerPage": t.integer().optional(),
        }
    ).named(renames["PageInfoIn"])
    types["PageInfoOut"] = t.struct(
        {
            "startIndex": t.integer().optional(),
            "totalResults": t.integer().optional(),
            "resultPerPage": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PageInfoOut"])
    types["GeneratedUniversalApkIn"] = t.struct(
        {"downloadId": t.string().optional()}
    ).named(renames["GeneratedUniversalApkIn"])
    types["GeneratedUniversalApkOut"] = t.struct(
        {
            "downloadId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GeneratedUniversalApkOut"])
    types["PrepaidPlanIn"] = t.struct(
        {"allowExtendAfterTime": t.string().optional()}
    ).named(renames["PrepaidPlanIn"])
    types["PrepaidPlanOut"] = t.struct(
        {
            "allowExtendAfterTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrepaidPlanOut"])
    types["InAppProductListingIn"] = t.struct(
        {
            "description": t.string().optional(),
            "benefits": t.array(t.string()).optional(),
            "title": t.string().optional(),
        }
    ).named(renames["InAppProductListingIn"])
    types["InAppProductListingOut"] = t.struct(
        {
            "description": t.string().optional(),
            "benefits": t.array(t.string()).optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InAppProductListingOut"])
    types["SubscriptionListingIn"] = t.struct(
        {
            "description": t.string().optional(),
            "languageCode": t.string(),
            "benefits": t.array(t.string()).optional(),
            "title": t.string(),
        }
    ).named(renames["SubscriptionListingIn"])
    types["SubscriptionListingOut"] = t.struct(
        {
            "description": t.string().optional(),
            "languageCode": t.string(),
            "benefits": t.array(t.string()).optional(),
            "title": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscriptionListingOut"])
    types["ReviewsListResponseIn"] = t.struct(
        {
            "tokenPagination": t.proxy(renames["TokenPaginationIn"]).optional(),
            "pageInfo": t.proxy(renames["PageInfoIn"]).optional(),
            "reviews": t.array(t.proxy(renames["ReviewIn"])).optional(),
        }
    ).named(renames["ReviewsListResponseIn"])
    types["ReviewsListResponseOut"] = t.struct(
        {
            "tokenPagination": t.proxy(renames["TokenPaginationOut"]).optional(),
            "pageInfo": t.proxy(renames["PageInfoOut"]).optional(),
            "reviews": t.array(t.proxy(renames["ReviewOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReviewsListResponseOut"])
    types["ImageIn"] = t.struct(
        {
            "sha1": t.string().optional(),
            "url": t.string().optional(),
            "id": t.string().optional(),
            "sha256": t.string().optional(),
        }
    ).named(renames["ImageIn"])
    types["ImageOut"] = t.struct(
        {
            "sha1": t.string().optional(),
            "url": t.string().optional(),
            "id": t.string().optional(),
            "sha256": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageOut"])
    types["SubscriptionOfferIn"] = t.struct(
        {
            "productId": t.string(),
            "regionalConfigs": t.array(
                t.proxy(renames["RegionalSubscriptionOfferConfigIn"])
            ),
            "phases": t.array(t.proxy(renames["SubscriptionOfferPhaseIn"])),
            "targeting": t.proxy(renames["SubscriptionOfferTargetingIn"]).optional(),
            "packageName": t.string(),
            "basePlanId": t.string(),
            "offerTags": t.array(t.proxy(renames["OfferTagIn"])).optional(),
            "offerId": t.string(),
            "otherRegionsConfig": t.proxy(
                renames["OtherRegionsSubscriptionOfferConfigIn"]
            ).optional(),
        }
    ).named(renames["SubscriptionOfferIn"])
    types["SubscriptionOfferOut"] = t.struct(
        {
            "productId": t.string(),
            "regionalConfigs": t.array(
                t.proxy(renames["RegionalSubscriptionOfferConfigOut"])
            ),
            "phases": t.array(t.proxy(renames["SubscriptionOfferPhaseOut"])),
            "targeting": t.proxy(renames["SubscriptionOfferTargetingOut"]).optional(),
            "packageName": t.string(),
            "basePlanId": t.string(),
            "offerTags": t.array(t.proxy(renames["OfferTagOut"])).optional(),
            "state": t.string().optional(),
            "offerId": t.string(),
            "otherRegionsConfig": t.proxy(
                renames["OtherRegionsSubscriptionOfferConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscriptionOfferOut"])
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
    types["InternalAppSharingArtifactIn"] = t.struct(
        {
            "certificateFingerprint": t.string().optional(),
            "downloadUrl": t.string().optional(),
            "sha256": t.string().optional(),
        }
    ).named(renames["InternalAppSharingArtifactIn"])
    types["InternalAppSharingArtifactOut"] = t.struct(
        {
            "certificateFingerprint": t.string().optional(),
            "downloadUrl": t.string().optional(),
            "sha256": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InternalAppSharingArtifactOut"])
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
    types["DeviceTierConfigIn"] = t.struct(
        {
            "deviceGroups": t.array(t.proxy(renames["DeviceGroupIn"])).optional(),
            "deviceTierSet": t.proxy(renames["DeviceTierSetIn"]).optional(),
            "userCountrySets": t.array(t.proxy(renames["UserCountrySetIn"])).optional(),
        }
    ).named(renames["DeviceTierConfigIn"])
    types["DeviceTierConfigOut"] = t.struct(
        {
            "deviceTierConfigId": t.string().optional(),
            "deviceGroups": t.array(t.proxy(renames["DeviceGroupOut"])).optional(),
            "deviceTierSet": t.proxy(renames["DeviceTierSetOut"]).optional(),
            "userCountrySets": t.array(
                t.proxy(renames["UserCountrySetOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceTierConfigOut"])
    types["ReplacementCancellationIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ReplacementCancellationIn"]
    )
    types["ReplacementCancellationOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ReplacementCancellationOut"])
    types["FullRefundIn"] = t.struct({"_": t.string().optional()}).named(
        renames["FullRefundIn"]
    )
    types["FullRefundOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["FullRefundOut"])
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
    types["ImagesDeleteAllResponseIn"] = t.struct(
        {"deleted": t.array(t.proxy(renames["ImageIn"])).optional()}
    ).named(renames["ImagesDeleteAllResponseIn"])
    types["ImagesDeleteAllResponseOut"] = t.struct(
        {
            "deleted": t.array(t.proxy(renames["ImageOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImagesDeleteAllResponseOut"])
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
    types["DeviceSpecIn"] = t.struct(
        {
            "screenDensity": t.integer().optional(),
            "supportedLocales": t.array(t.string()).optional(),
            "supportedAbis": t.array(t.string()).optional(),
        }
    ).named(renames["DeviceSpecIn"])
    types["DeviceSpecOut"] = t.struct(
        {
            "screenDensity": t.integer().optional(),
            "supportedLocales": t.array(t.string()).optional(),
            "supportedAbis": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceSpecOut"])
    types["SubscriptionItemPriceChangeDetailsIn"] = t.struct(
        {
            "newPrice": t.proxy(renames["MoneyIn"]).optional(),
            "priceChangeState": t.string().optional(),
            "expectedNewPriceChargeTime": t.string().optional(),
            "priceChangeMode": t.string().optional(),
        }
    ).named(renames["SubscriptionItemPriceChangeDetailsIn"])
    types["SubscriptionItemPriceChangeDetailsOut"] = t.struct(
        {
            "newPrice": t.proxy(renames["MoneyOut"]).optional(),
            "priceChangeState": t.string().optional(),
            "expectedNewPriceChargeTime": t.string().optional(),
            "priceChangeMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscriptionItemPriceChangeDetailsOut"])
    types["DeactivateBasePlanRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeactivateBasePlanRequestIn"]
    )
    types["DeactivateBasePlanRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeactivateBasePlanRequestOut"])
    types["MoneyIn"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "units": t.string().optional(),
            "currencyCode": t.string().optional(),
        }
    ).named(renames["MoneyIn"])
    types["MoneyOut"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "units": t.string().optional(),
            "currencyCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoneyOut"])
    types["GeneratedApksPerSigningKeyIn"] = t.struct(
        {
            "generatedSplitApks": t.array(
                t.proxy(renames["GeneratedSplitApkIn"])
            ).optional(),
            "certificateSha256Hash": t.string().optional(),
            "generatedStandaloneApks": t.array(
                t.proxy(renames["GeneratedStandaloneApkIn"])
            ).optional(),
            "generatedAssetPackSlices": t.array(
                t.proxy(renames["GeneratedAssetPackSliceIn"])
            ).optional(),
            "generatedUniversalApk": t.proxy(
                renames["GeneratedUniversalApkIn"]
            ).optional(),
        }
    ).named(renames["GeneratedApksPerSigningKeyIn"])
    types["GeneratedApksPerSigningKeyOut"] = t.struct(
        {
            "generatedSplitApks": t.array(
                t.proxy(renames["GeneratedSplitApkOut"])
            ).optional(),
            "certificateSha256Hash": t.string().optional(),
            "generatedStandaloneApks": t.array(
                t.proxy(renames["GeneratedStandaloneApkOut"])
            ).optional(),
            "generatedAssetPackSlices": t.array(
                t.proxy(renames["GeneratedAssetPackSliceOut"])
            ).optional(),
            "generatedUniversalApk": t.proxy(
                renames["GeneratedUniversalApkOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GeneratedApksPerSigningKeyOut"])
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
    types["DeobfuscationFileIn"] = t.struct(
        {"symbolType": t.string().optional()}
    ).named(renames["DeobfuscationFileIn"])
    types["DeobfuscationFileOut"] = t.struct(
        {
            "symbolType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeobfuscationFileOut"])
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
    types["ImagesListResponseIn"] = t.struct(
        {"images": t.array(t.proxy(renames["ImageIn"])).optional()}
    ).named(renames["ImagesListResponseIn"])
    types["ImagesListResponseOut"] = t.struct(
        {
            "images": t.array(t.proxy(renames["ImageOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImagesListResponseOut"])
    types["RegionalPriceMigrationConfigIn"] = t.struct(
        {"oldestAllowedPriceVersionTime": t.string(), "regionCode": t.string()}
    ).named(renames["RegionalPriceMigrationConfigIn"])
    types["RegionalPriceMigrationConfigOut"] = t.struct(
        {
            "oldestAllowedPriceVersionTime": t.string(),
            "regionCode": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegionalPriceMigrationConfigOut"])
    types["DeviceTierSetIn"] = t.struct(
        {"deviceTiers": t.array(t.proxy(renames["DeviceTierIn"])).optional()}
    ).named(renames["DeviceTierSetIn"])
    types["DeviceTierSetOut"] = t.struct(
        {
            "deviceTiers": t.array(t.proxy(renames["DeviceTierOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceTierSetOut"])
    types["UserIn"] = t.struct(
        {
            "expirationTime": t.string().optional(),
            "developerAccountPermissions": t.array(t.string()).optional(),
            "email": t.string().optional(),
            "name": t.string(),
        }
    ).named(renames["UserIn"])
    types["UserOut"] = t.struct(
        {
            "accessState": t.string().optional(),
            "grants": t.array(t.proxy(renames["GrantOut"])).optional(),
            "expirationTime": t.string().optional(),
            "developerAccountPermissions": t.array(t.string()).optional(),
            "email": t.string().optional(),
            "partial": t.boolean().optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserOut"])
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
    types["ProductPurchasesAcknowledgeRequestIn"] = t.struct(
        {"developerPayload": t.string().optional()}
    ).named(renames["ProductPurchasesAcknowledgeRequestIn"])
    types["ProductPurchasesAcknowledgeRequestOut"] = t.struct(
        {
            "developerPayload": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductPurchasesAcknowledgeRequestOut"])
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
    types["SubscriptionOfferPhaseIn"] = t.struct(
        {
            "recurrenceCount": t.integer(),
            "regionalConfigs": t.array(
                t.proxy(renames["RegionalSubscriptionOfferPhaseConfigIn"])
            ),
            "otherRegionsConfig": t.proxy(
                renames["OtherRegionsSubscriptionOfferPhaseConfigIn"]
            ).optional(),
            "duration": t.string(),
        }
    ).named(renames["SubscriptionOfferPhaseIn"])
    types["SubscriptionOfferPhaseOut"] = t.struct(
        {
            "recurrenceCount": t.integer(),
            "regionalConfigs": t.array(
                t.proxy(renames["RegionalSubscriptionOfferPhaseConfigOut"])
            ),
            "otherRegionsConfig": t.proxy(
                renames["OtherRegionsSubscriptionOfferPhaseConfigOut"]
            ).optional(),
            "duration": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscriptionOfferPhaseOut"])
    types["BasePlanIn"] = t.struct(
        {
            "regionalConfigs": t.array(
                t.proxy(renames["RegionalBasePlanConfigIn"])
            ).optional(),
            "basePlanId": t.string(),
            "autoRenewingBasePlanType": t.proxy(
                renames["AutoRenewingBasePlanTypeIn"]
            ).optional(),
            "otherRegionsConfig": t.proxy(
                renames["OtherRegionsBasePlanConfigIn"]
            ).optional(),
            "prepaidBasePlanType": t.proxy(renames["PrepaidBasePlanTypeIn"]).optional(),
            "offerTags": t.array(t.proxy(renames["OfferTagIn"])).optional(),
        }
    ).named(renames["BasePlanIn"])
    types["BasePlanOut"] = t.struct(
        {
            "regionalConfigs": t.array(
                t.proxy(renames["RegionalBasePlanConfigOut"])
            ).optional(),
            "basePlanId": t.string(),
            "state": t.string().optional(),
            "autoRenewingBasePlanType": t.proxy(
                renames["AutoRenewingBasePlanTypeOut"]
            ).optional(),
            "otherRegionsConfig": t.proxy(
                renames["OtherRegionsBasePlanConfigOut"]
            ).optional(),
            "prepaidBasePlanType": t.proxy(
                renames["PrepaidBasePlanTypeOut"]
            ).optional(),
            "offerTags": t.array(t.proxy(renames["OfferTagOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BasePlanOut"])
    types["SubscriptionPurchaseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "profileId": t.string().optional(),
            "profileName": t.string().optional(),
            "purchaseType": t.integer().optional(),
            "priceAmountMicros": t.string().optional(),
            "obfuscatedExternalProfileId": t.string().optional(),
            "familyName": t.string().optional(),
            "linkedPurchaseToken": t.string().optional(),
            "orderId": t.string().optional(),
            "externalAccountId": t.string().optional(),
            "autoRenewing": t.boolean().optional(),
            "priceChange": t.proxy(renames["SubscriptionPriceChangeIn"]).optional(),
            "givenName": t.string().optional(),
            "priceCurrencyCode": t.string().optional(),
            "emailAddress": t.string().optional(),
            "countryCode": t.string().optional(),
            "acknowledgementState": t.integer().optional(),
            "startTimeMillis": t.string().optional(),
            "paymentState": t.integer().optional(),
            "cancelSurveyResult": t.proxy(
                renames["SubscriptionCancelSurveyResultIn"]
            ).optional(),
            "cancelReason": t.integer().optional(),
            "developerPayload": t.string().optional(),
            "introductoryPriceInfo": t.proxy(
                renames["IntroductoryPriceInfoIn"]
            ).optional(),
            "promotionCode": t.string().optional(),
            "userCancellationTimeMillis": t.string().optional(),
            "expiryTimeMillis": t.string().optional(),
            "autoResumeTimeMillis": t.string().optional(),
            "promotionType": t.integer().optional(),
            "obfuscatedExternalAccountId": t.string().optional(),
        }
    ).named(renames["SubscriptionPurchaseIn"])
    types["SubscriptionPurchaseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "profileId": t.string().optional(),
            "profileName": t.string().optional(),
            "purchaseType": t.integer().optional(),
            "priceAmountMicros": t.string().optional(),
            "obfuscatedExternalProfileId": t.string().optional(),
            "familyName": t.string().optional(),
            "linkedPurchaseToken": t.string().optional(),
            "orderId": t.string().optional(),
            "externalAccountId": t.string().optional(),
            "autoRenewing": t.boolean().optional(),
            "priceChange": t.proxy(renames["SubscriptionPriceChangeOut"]).optional(),
            "givenName": t.string().optional(),
            "priceCurrencyCode": t.string().optional(),
            "emailAddress": t.string().optional(),
            "countryCode": t.string().optional(),
            "acknowledgementState": t.integer().optional(),
            "startTimeMillis": t.string().optional(),
            "paymentState": t.integer().optional(),
            "cancelSurveyResult": t.proxy(
                renames["SubscriptionCancelSurveyResultOut"]
            ).optional(),
            "cancelReason": t.integer().optional(),
            "developerPayload": t.string().optional(),
            "introductoryPriceInfo": t.proxy(
                renames["IntroductoryPriceInfoOut"]
            ).optional(),
            "promotionCode": t.string().optional(),
            "userCancellationTimeMillis": t.string().optional(),
            "expiryTimeMillis": t.string().optional(),
            "autoResumeTimeMillis": t.string().optional(),
            "promotionType": t.integer().optional(),
            "obfuscatedExternalAccountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscriptionPurchaseOut"])
    types["OtherRegionsSubscriptionOfferPhaseConfigIn"] = t.struct(
        {
            "relativeDiscount": t.number().optional(),
            "otherRegionsPrices": t.proxy(
                renames["OtherRegionsSubscriptionOfferPhasePricesIn"]
            ).optional(),
            "absoluteDiscounts": t.proxy(
                renames["OtherRegionsSubscriptionOfferPhasePricesIn"]
            ).optional(),
        }
    ).named(renames["OtherRegionsSubscriptionOfferPhaseConfigIn"])
    types["OtherRegionsSubscriptionOfferPhaseConfigOut"] = t.struct(
        {
            "relativeDiscount": t.number().optional(),
            "otherRegionsPrices": t.proxy(
                renames["OtherRegionsSubscriptionOfferPhasePricesOut"]
            ).optional(),
            "absoluteDiscounts": t.proxy(
                renames["OtherRegionsSubscriptionOfferPhasePricesOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OtherRegionsSubscriptionOfferPhaseConfigOut"])
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
    types["RegionalBasePlanConfigIn"] = t.struct(
        {
            "newSubscriberAvailability": t.boolean().optional(),
            "price": t.proxy(renames["MoneyIn"]).optional(),
            "regionCode": t.string(),
        }
    ).named(renames["RegionalBasePlanConfigIn"])
    types["RegionalBasePlanConfigOut"] = t.struct(
        {
            "newSubscriberAvailability": t.boolean().optional(),
            "price": t.proxy(renames["MoneyOut"]).optional(),
            "regionCode": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegionalBasePlanConfigOut"])
    types["AcquisitionTargetingRuleIn"] = t.struct(
        {"scope": t.proxy(renames["TargetingRuleScopeIn"])}
    ).named(renames["AcquisitionTargetingRuleIn"])
    types["AcquisitionTargetingRuleOut"] = t.struct(
        {
            "scope": t.proxy(renames["TargetingRuleScopeOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AcquisitionTargetingRuleOut"])
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
    types["CountryTargetingIn"] = t.struct(
        {
            "includeRestOfWorld": t.boolean().optional(),
            "countries": t.array(t.string()).optional(),
        }
    ).named(renames["CountryTargetingIn"])
    types["CountryTargetingOut"] = t.struct(
        {
            "includeRestOfWorld": t.boolean().optional(),
            "countries": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CountryTargetingOut"])
    types["AutoRenewingBasePlanTypeIn"] = t.struct(
        {
            "legacyCompatible": t.boolean().optional(),
            "prorationMode": t.string().optional(),
            "billingPeriodDuration": t.string(),
            "gracePeriodDuration": t.string().optional(),
            "resubscribeState": t.string().optional(),
            "legacyCompatibleSubscriptionOfferId": t.string().optional(),
        }
    ).named(renames["AutoRenewingBasePlanTypeIn"])
    types["AutoRenewingBasePlanTypeOut"] = t.struct(
        {
            "legacyCompatible": t.boolean().optional(),
            "prorationMode": t.string().optional(),
            "billingPeriodDuration": t.string(),
            "gracePeriodDuration": t.string().optional(),
            "resubscribeState": t.string().optional(),
            "legacyCompatibleSubscriptionOfferId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutoRenewingBasePlanTypeOut"])
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
    types["MigrateBasePlanPricesResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["MigrateBasePlanPricesResponseIn"])
    types["MigrateBasePlanPricesResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["MigrateBasePlanPricesResponseOut"])
    types["AppDetailsIn"] = t.struct(
        {
            "contactPhone": t.string().optional(),
            "defaultLanguage": t.string().optional(),
            "contactWebsite": t.string().optional(),
            "contactEmail": t.string().optional(),
        }
    ).named(renames["AppDetailsIn"])
    types["AppDetailsOut"] = t.struct(
        {
            "contactPhone": t.string().optional(),
            "defaultLanguage": t.string().optional(),
            "contactWebsite": t.string().optional(),
            "contactEmail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppDetailsOut"])
    types["TargetingRuleScopeIn"] = t.struct(
        {"specificSubscriptionInApp": t.string().optional()}
    ).named(renames["TargetingRuleScopeIn"])
    types["TargetingRuleScopeOut"] = t.struct(
        {
            "specificSubscriptionInApp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetingRuleScopeOut"])
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
    types["ExternalTransactionTestPurchaseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ExternalTransactionTestPurchaseIn"])
    types["ExternalTransactionTestPurchaseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ExternalTransactionTestPurchaseOut"])
    types["ReviewIn"] = t.struct(
        {
            "comments": t.array(t.proxy(renames["CommentIn"])).optional(),
            "reviewId": t.string().optional(),
            "authorName": t.string().optional(),
        }
    ).named(renames["ReviewIn"])
    types["ReviewOut"] = t.struct(
        {
            "comments": t.array(t.proxy(renames["CommentOut"])).optional(),
            "reviewId": t.string().optional(),
            "authorName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReviewOut"])
    types["SubscriptionPurchasesDeferRequestIn"] = t.struct(
        {"deferralInfo": t.proxy(renames["SubscriptionDeferralInfoIn"]).optional()}
    ).named(renames["SubscriptionPurchasesDeferRequestIn"])
    types["SubscriptionPurchasesDeferRequestOut"] = t.struct(
        {
            "deferralInfo": t.proxy(renames["SubscriptionDeferralInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscriptionPurchasesDeferRequestOut"])
    types["OfferDetailsIn"] = t.struct(
        {
            "basePlanId": t.string().optional(),
            "offerId": t.string().optional(),
            "offerTags": t.array(t.string()).optional(),
        }
    ).named(renames["OfferDetailsIn"])
    types["OfferDetailsOut"] = t.struct(
        {
            "basePlanId": t.string().optional(),
            "offerId": t.string().optional(),
            "offerTags": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OfferDetailsOut"])
    types["ExpansionFilesUploadResponseIn"] = t.struct(
        {"expansionFile": t.proxy(renames["ExpansionFileIn"]).optional()}
    ).named(renames["ExpansionFilesUploadResponseIn"])
    types["ExpansionFilesUploadResponseOut"] = t.struct(
        {
            "expansionFile": t.proxy(renames["ExpansionFileOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExpansionFilesUploadResponseOut"])
    types["RecurringExternalTransactionIn"] = t.struct(
        {
            "externalTransactionToken": t.string().optional(),
            "externalSubscription": t.proxy(
                renames["ExternalSubscriptionIn"]
            ).optional(),
            "initialExternalTransactionId": t.string().optional(),
        }
    ).named(renames["RecurringExternalTransactionIn"])
    types["RecurringExternalTransactionOut"] = t.struct(
        {
            "externalTransactionToken": t.string().optional(),
            "externalSubscription": t.proxy(
                renames["ExternalSubscriptionOut"]
            ).optional(),
            "initialExternalTransactionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RecurringExternalTransactionOut"])
    types["SystemApksListResponseIn"] = t.struct(
        {"variants": t.array(t.proxy(renames["VariantIn"])).optional()}
    ).named(renames["SystemApksListResponseIn"])
    types["SystemApksListResponseOut"] = t.struct(
        {
            "variants": t.array(t.proxy(renames["VariantOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SystemApksListResponseOut"])
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
    types["ManagedProductTaxAndComplianceSettingsIn"] = t.struct(
        {
            "taxRateInfoByRegionCode": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "eeaWithdrawalRightType": t.string().optional(),
        }
    ).named(renames["ManagedProductTaxAndComplianceSettingsIn"])
    types["ManagedProductTaxAndComplianceSettingsOut"] = t.struct(
        {
            "taxRateInfoByRegionCode": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "eeaWithdrawalRightType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedProductTaxAndComplianceSettingsOut"])
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
    types["ProductPurchaseIn"] = t.struct(
        {
            "purchaseToken": t.string().optional(),
            "orderId": t.string().optional(),
            "consumptionState": t.integer().optional(),
            "kind": t.string().optional(),
            "purchaseTimeMillis": t.string().optional(),
            "purchaseType": t.integer().optional(),
            "quantity": t.integer().optional(),
            "purchaseState": t.integer().optional(),
            "productId": t.string().optional(),
            "developerPayload": t.string().optional(),
            "acknowledgementState": t.integer().optional(),
            "obfuscatedExternalProfileId": t.string().optional(),
            "obfuscatedExternalAccountId": t.string().optional(),
            "regionCode": t.string().optional(),
        }
    ).named(renames["ProductPurchaseIn"])
    types["ProductPurchaseOut"] = t.struct(
        {
            "purchaseToken": t.string().optional(),
            "orderId": t.string().optional(),
            "consumptionState": t.integer().optional(),
            "kind": t.string().optional(),
            "purchaseTimeMillis": t.string().optional(),
            "purchaseType": t.integer().optional(),
            "quantity": t.integer().optional(),
            "purchaseState": t.integer().optional(),
            "productId": t.string().optional(),
            "developerPayload": t.string().optional(),
            "acknowledgementState": t.integer().optional(),
            "obfuscatedExternalProfileId": t.string().optional(),
            "obfuscatedExternalAccountId": t.string().optional(),
            "regionCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductPurchaseOut"])
    types["DeviceSelectorIn"] = t.struct(
        {
            "requiredSystemFeatures": t.array(
                t.proxy(renames["SystemFeatureIn"])
            ).optional(),
            "deviceRam": t.proxy(renames["DeviceRamIn"]).optional(),
            "excludedDeviceIds": t.array(t.proxy(renames["DeviceIdIn"])).optional(),
            "forbiddenSystemFeatures": t.array(
                t.proxy(renames["SystemFeatureIn"])
            ).optional(),
            "includedDeviceIds": t.array(t.proxy(renames["DeviceIdIn"])).optional(),
        }
    ).named(renames["DeviceSelectorIn"])
    types["DeviceSelectorOut"] = t.struct(
        {
            "requiredSystemFeatures": t.array(
                t.proxy(renames["SystemFeatureOut"])
            ).optional(),
            "deviceRam": t.proxy(renames["DeviceRamOut"]).optional(),
            "excludedDeviceIds": t.array(t.proxy(renames["DeviceIdOut"])).optional(),
            "forbiddenSystemFeatures": t.array(
                t.proxy(renames["SystemFeatureOut"])
            ).optional(),
            "includedDeviceIds": t.array(t.proxy(renames["DeviceIdOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceSelectorOut"])
    types["ArchiveSubscriptionRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ArchiveSubscriptionRequestIn"])
    types["ArchiveSubscriptionRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ArchiveSubscriptionRequestOut"])
    types["AppEditIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AppEditIn"]
    )
    types["AppEditOut"] = t.struct(
        {
            "id": t.string().optional(),
            "expiryTimeSeconds": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppEditOut"])
    types["GrantIn"] = t.struct(
        {
            "appLevelPermissions": t.array(t.string()).optional(),
            "name": t.string(),
            "packageName": t.string().optional(),
        }
    ).named(renames["GrantIn"])
    types["GrantOut"] = t.struct(
        {
            "appLevelPermissions": t.array(t.string()).optional(),
            "name": t.string(),
            "packageName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrantOut"])
    types["DeobfuscationFilesUploadResponseIn"] = t.struct(
        {"deobfuscationFile": t.proxy(renames["DeobfuscationFileIn"]).optional()}
    ).named(renames["DeobfuscationFilesUploadResponseIn"])
    types["DeobfuscationFilesUploadResponseOut"] = t.struct(
        {
            "deobfuscationFile": t.proxy(renames["DeobfuscationFileOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeobfuscationFilesUploadResponseOut"])
    types["ExternalSubscriptionIn"] = t.struct({"subscriptionType": t.string()}).named(
        renames["ExternalSubscriptionIn"]
    )
    types["ExternalSubscriptionOut"] = t.struct(
        {
            "subscriptionType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExternalSubscriptionOut"])
    types["ImagesUploadResponseIn"] = t.struct(
        {"image": t.proxy(renames["ImageIn"]).optional()}
    ).named(renames["ImagesUploadResponseIn"])
    types["ImagesUploadResponseOut"] = t.struct(
        {
            "image": t.proxy(renames["ImageOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImagesUploadResponseOut"])
    types["ReviewsReplyResponseIn"] = t.struct(
        {"result": t.proxy(renames["ReviewReplyResultIn"]).optional()}
    ).named(renames["ReviewsReplyResponseIn"])
    types["ReviewsReplyResponseOut"] = t.struct(
        {
            "result": t.proxy(renames["ReviewReplyResultOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReviewsReplyResponseOut"])
    types["TrackIn"] = t.struct(
        {
            "track": t.string().optional(),
            "releases": t.array(t.proxy(renames["TrackReleaseIn"])).optional(),
        }
    ).named(renames["TrackIn"])
    types["TrackOut"] = t.struct(
        {
            "track": t.string().optional(),
            "releases": t.array(t.proxy(renames["TrackReleaseOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrackOut"])
    types["TimestampIn"] = t.struct(
        {"nanos": t.integer().optional(), "seconds": t.string().optional()}
    ).named(renames["TimestampIn"])
    types["TimestampOut"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "seconds": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimestampOut"])
    types["RegionalSubscriptionOfferPhaseConfigIn"] = t.struct(
        {
            "regionCode": t.string(),
            "absoluteDiscount": t.proxy(renames["MoneyIn"]).optional(),
            "relativeDiscount": t.number().optional(),
            "price": t.proxy(renames["MoneyIn"]).optional(),
        }
    ).named(renames["RegionalSubscriptionOfferPhaseConfigIn"])
    types["RegionalSubscriptionOfferPhaseConfigOut"] = t.struct(
        {
            "regionCode": t.string(),
            "absoluteDiscount": t.proxy(renames["MoneyOut"]).optional(),
            "relativeDiscount": t.number().optional(),
            "price": t.proxy(renames["MoneyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegionalSubscriptionOfferPhaseConfigOut"])
    types["SubscriptionPurchaseLineItemIn"] = t.struct(
        {
            "offerDetails": t.proxy(renames["OfferDetailsIn"]).optional(),
            "prepaidPlan": t.proxy(renames["PrepaidPlanIn"]).optional(),
            "expiryTime": t.string().optional(),
            "autoRenewingPlan": t.proxy(renames["AutoRenewingPlanIn"]).optional(),
            "productId": t.string().optional(),
        }
    ).named(renames["SubscriptionPurchaseLineItemIn"])
    types["SubscriptionPurchaseLineItemOut"] = t.struct(
        {
            "offerDetails": t.proxy(renames["OfferDetailsOut"]).optional(),
            "prepaidPlan": t.proxy(renames["PrepaidPlanOut"]).optional(),
            "expiryTime": t.string().optional(),
            "autoRenewingPlan": t.proxy(renames["AutoRenewingPlanOut"]).optional(),
            "productId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscriptionPurchaseLineItemOut"])
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
    types["SubscriptionTaxAndComplianceSettingsIn"] = t.struct(
        {
            "taxRateInfoByRegionCode": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "eeaWithdrawalRightType": t.string().optional(),
        }
    ).named(renames["SubscriptionTaxAndComplianceSettingsIn"])
    types["SubscriptionTaxAndComplianceSettingsOut"] = t.struct(
        {
            "taxRateInfoByRegionCode": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "eeaWithdrawalRightType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscriptionTaxAndComplianceSettingsOut"])
    types["GeneratedAssetPackSliceIn"] = t.struct(
        {
            "downloadId": t.string().optional(),
            "moduleName": t.string().optional(),
            "sliceId": t.string().optional(),
            "version": t.string().optional(),
        }
    ).named(renames["GeneratedAssetPackSliceIn"])
    types["GeneratedAssetPackSliceOut"] = t.struct(
        {
            "downloadId": t.string().optional(),
            "moduleName": t.string().optional(),
            "sliceId": t.string().optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GeneratedAssetPackSliceOut"])
    types["DeveloperInitiatedCancellationIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DeveloperInitiatedCancellationIn"])
    types["DeveloperInitiatedCancellationOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeveloperInitiatedCancellationOut"])
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
    types["SubscriptionDeferralInfoIn"] = t.struct(
        {
            "expectedExpiryTimeMillis": t.string().optional(),
            "desiredExpiryTimeMillis": t.string().optional(),
        }
    ).named(renames["SubscriptionDeferralInfoIn"])
    types["SubscriptionDeferralInfoOut"] = t.struct(
        {
            "expectedExpiryTimeMillis": t.string().optional(),
            "desiredExpiryTimeMillis": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscriptionDeferralInfoOut"])
    types["CanceledStateContextIn"] = t.struct(
        {
            "userInitiatedCancellation": t.proxy(
                renames["UserInitiatedCancellationIn"]
            ).optional(),
            "replacementCancellation": t.proxy(
                renames["ReplacementCancellationIn"]
            ).optional(),
            "systemInitiatedCancellation": t.proxy(
                renames["SystemInitiatedCancellationIn"]
            ).optional(),
            "developerInitiatedCancellation": t.proxy(
                renames["DeveloperInitiatedCancellationIn"]
            ).optional(),
        }
    ).named(renames["CanceledStateContextIn"])
    types["CanceledStateContextOut"] = t.struct(
        {
            "userInitiatedCancellation": t.proxy(
                renames["UserInitiatedCancellationOut"]
            ).optional(),
            "replacementCancellation": t.proxy(
                renames["ReplacementCancellationOut"]
            ).optional(),
            "systemInitiatedCancellation": t.proxy(
                renames["SystemInitiatedCancellationOut"]
            ).optional(),
            "developerInitiatedCancellation": t.proxy(
                renames["DeveloperInitiatedCancellationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CanceledStateContextOut"])
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
    types["ExternalAccountIdentifiersIn"] = t.struct(
        {
            "obfuscatedExternalProfileId": t.string().optional(),
            "externalAccountId": t.string().optional(),
            "obfuscatedExternalAccountId": t.string().optional(),
        }
    ).named(renames["ExternalAccountIdentifiersIn"])
    types["ExternalAccountIdentifiersOut"] = t.struct(
        {
            "obfuscatedExternalProfileId": t.string().optional(),
            "externalAccountId": t.string().optional(),
            "obfuscatedExternalAccountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExternalAccountIdentifiersOut"])
    types["ListingIn"] = t.struct(
        {
            "language": t.string().optional(),
            "title": t.string().optional(),
            "video": t.string().optional(),
            "fullDescription": t.string().optional(),
            "shortDescription": t.string().optional(),
        }
    ).named(renames["ListingIn"])
    types["ListingOut"] = t.struct(
        {
            "language": t.string().optional(),
            "title": t.string().optional(),
            "video": t.string().optional(),
            "fullDescription": t.string().optional(),
            "shortDescription": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListingOut"])
    types["TrackReleaseIn"] = t.struct(
        {
            "versionCodes": t.array(t.string()).optional(),
            "countryTargeting": t.proxy(renames["CountryTargetingIn"]).optional(),
            "name": t.string().optional(),
            "status": t.string().optional(),
            "inAppUpdatePriority": t.integer().optional(),
            "releaseNotes": t.array(t.proxy(renames["LocalizedTextIn"])).optional(),
            "userFraction": t.number().optional(),
        }
    ).named(renames["TrackReleaseIn"])
    types["TrackReleaseOut"] = t.struct(
        {
            "versionCodes": t.array(t.string()).optional(),
            "countryTargeting": t.proxy(renames["CountryTargetingOut"]).optional(),
            "name": t.string().optional(),
            "status": t.string().optional(),
            "inAppUpdatePriority": t.integer().optional(),
            "releaseNotes": t.array(t.proxy(renames["LocalizedTextOut"])).optional(),
            "userFraction": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrackReleaseOut"])
    types["OtherRegionsSubscriptionOfferConfigIn"] = t.struct(
        {"otherRegionsNewSubscriberAvailability": t.boolean().optional()}
    ).named(renames["OtherRegionsSubscriptionOfferConfigIn"])
    types["OtherRegionsSubscriptionOfferConfigOut"] = t.struct(
        {
            "otherRegionsNewSubscriberAvailability": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OtherRegionsSubscriptionOfferConfigOut"])
    types["LocalizedTextIn"] = t.struct(
        {"language": t.string().optional(), "text": t.string().optional()}
    ).named(renames["LocalizedTextIn"])
    types["LocalizedTextOut"] = t.struct(
        {
            "language": t.string().optional(),
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocalizedTextOut"])
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
    types["TrackTargetedCountryIn"] = t.struct(
        {"countryCode": t.string().optional()}
    ).named(renames["TrackTargetedCountryIn"])
    types["TrackTargetedCountryOut"] = t.struct(
        {
            "countryCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrackTargetedCountryOut"])
    types["SubscriptionIn"] = t.struct(
        {
            "productId": t.string().optional(),
            "listings": t.array(t.proxy(renames["SubscriptionListingIn"])),
            "basePlans": t.array(t.proxy(renames["BasePlanIn"])).optional(),
            "taxAndComplianceSettings": t.proxy(
                renames["SubscriptionTaxAndComplianceSettingsIn"]
            ).optional(),
            "packageName": t.string().optional(),
        }
    ).named(renames["SubscriptionIn"])
    types["SubscriptionOut"] = t.struct(
        {
            "productId": t.string().optional(),
            "listings": t.array(t.proxy(renames["SubscriptionListingOut"])),
            "archived": t.boolean().optional(),
            "basePlans": t.array(t.proxy(renames["BasePlanOut"])).optional(),
            "taxAndComplianceSettings": t.proxy(
                renames["SubscriptionTaxAndComplianceSettingsOut"]
            ).optional(),
            "packageName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscriptionOut"])
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
    types["SystemInitiatedCancellationIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["SystemInitiatedCancellationIn"])
    types["SystemInitiatedCancellationOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SystemInitiatedCancellationOut"])
    types["AutoRenewingPlanIn"] = t.struct(
        {
            "priceChangeDetails": t.proxy(
                renames["SubscriptionItemPriceChangeDetailsIn"]
            ).optional(),
            "autoRenewEnabled": t.boolean().optional(),
        }
    ).named(renames["AutoRenewingPlanIn"])
    types["AutoRenewingPlanOut"] = t.struct(
        {
            "priceChangeDetails": t.proxy(
                renames["SubscriptionItemPriceChangeDetailsOut"]
            ).optional(),
            "autoRenewEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutoRenewingPlanOut"])
    types["ReviewsReplyRequestIn"] = t.struct(
        {"replyText": t.string().optional()}
    ).named(renames["ReviewsReplyRequestIn"])
    types["ReviewsReplyRequestOut"] = t.struct(
        {
            "replyText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReviewsReplyRequestOut"])
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
    types["OneTimeExternalTransactionIn"] = t.struct(
        {"externalTransactionToken": t.string().optional()}
    ).named(renames["OneTimeExternalTransactionIn"])
    types["OneTimeExternalTransactionOut"] = t.struct(
        {
            "externalTransactionToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OneTimeExternalTransactionOut"])
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
    types["SubscriptionPurchasesDeferResponseIn"] = t.struct(
        {"newExpiryTimeMillis": t.string().optional()}
    ).named(renames["SubscriptionPurchasesDeferResponseIn"])
    types["SubscriptionPurchasesDeferResponseOut"] = t.struct(
        {
            "newExpiryTimeMillis": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscriptionPurchasesDeferResponseOut"])
    types["SubscribeWithGoogleInfoIn"] = t.struct(
        {
            "profileId": t.string().optional(),
            "profileName": t.string().optional(),
            "familyName": t.string().optional(),
            "emailAddress": t.string().optional(),
            "givenName": t.string().optional(),
        }
    ).named(renames["SubscribeWithGoogleInfoIn"])
    types["SubscribeWithGoogleInfoOut"] = t.struct(
        {
            "profileId": t.string().optional(),
            "profileName": t.string().optional(),
            "familyName": t.string().optional(),
            "emailAddress": t.string().optional(),
            "givenName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscribeWithGoogleInfoOut"])
    types["ExternalTransactionIn"] = t.struct(
        {
            "originalTaxAmount": t.proxy(renames["PriceIn"]),
            "userTaxAddress": t.proxy(renames["ExternalTransactionAddressIn"]),
            "transactionTime": t.string(),
            "recurringTransaction": t.proxy(
                renames["RecurringExternalTransactionIn"]
            ).optional(),
            "oneTimeTransaction": t.proxy(
                renames["OneTimeExternalTransactionIn"]
            ).optional(),
            "originalPreTaxAmount": t.proxy(renames["PriceIn"]),
        }
    ).named(renames["ExternalTransactionIn"])
    types["ExternalTransactionOut"] = t.struct(
        {
            "transactionState": t.string().optional(),
            "originalTaxAmount": t.proxy(renames["PriceOut"]),
            "testPurchase": t.proxy(
                renames["ExternalTransactionTestPurchaseOut"]
            ).optional(),
            "userTaxAddress": t.proxy(renames["ExternalTransactionAddressOut"]),
            "transactionTime": t.string(),
            "recurringTransaction": t.proxy(
                renames["RecurringExternalTransactionOut"]
            ).optional(),
            "oneTimeTransaction": t.proxy(
                renames["OneTimeExternalTransactionOut"]
            ).optional(),
            "externalTransactionId": t.string().optional(),
            "currentTaxAmount": t.proxy(renames["PriceOut"]).optional(),
            "createTime": t.string().optional(),
            "packageName": t.string().optional(),
            "originalPreTaxAmount": t.proxy(renames["PriceOut"]),
            "currentPreTaxAmount": t.proxy(renames["PriceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExternalTransactionOut"])
    types["SubscriptionPurchaseV2In"] = t.struct(
        {
            "lineItems": t.array(
                t.proxy(renames["SubscriptionPurchaseLineItemIn"])
            ).optional(),
            "pausedStateContext": t.proxy(renames["PausedStateContextIn"]).optional(),
            "acknowledgementState": t.string().optional(),
            "testPurchase": t.proxy(renames["TestPurchaseIn"]).optional(),
            "kind": t.string().optional(),
            "subscribeWithGoogleInfo": t.proxy(
                renames["SubscribeWithGoogleInfoIn"]
            ).optional(),
            "subscriptionState": t.string().optional(),
            "startTime": t.string().optional(),
            "regionCode": t.string().optional(),
            "linkedPurchaseToken": t.string().optional(),
            "externalAccountIdentifiers": t.proxy(
                renames["ExternalAccountIdentifiersIn"]
            ).optional(),
            "latestOrderId": t.string().optional(),
            "canceledStateContext": t.proxy(
                renames["CanceledStateContextIn"]
            ).optional(),
        }
    ).named(renames["SubscriptionPurchaseV2In"])
    types["SubscriptionPurchaseV2Out"] = t.struct(
        {
            "lineItems": t.array(
                t.proxy(renames["SubscriptionPurchaseLineItemOut"])
            ).optional(),
            "pausedStateContext": t.proxy(renames["PausedStateContextOut"]).optional(),
            "acknowledgementState": t.string().optional(),
            "testPurchase": t.proxy(renames["TestPurchaseOut"]).optional(),
            "kind": t.string().optional(),
            "subscribeWithGoogleInfo": t.proxy(
                renames["SubscribeWithGoogleInfoOut"]
            ).optional(),
            "subscriptionState": t.string().optional(),
            "startTime": t.string().optional(),
            "regionCode": t.string().optional(),
            "linkedPurchaseToken": t.string().optional(),
            "externalAccountIdentifiers": t.proxy(
                renames["ExternalAccountIdentifiersOut"]
            ).optional(),
            "latestOrderId": t.string().optional(),
            "canceledStateContext": t.proxy(
                renames["CanceledStateContextOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscriptionPurchaseV2Out"])
    types["ApkIn"] = t.struct(
        {
            "versionCode": t.integer().optional(),
            "binary": t.proxy(renames["ApkBinaryIn"]).optional(),
        }
    ).named(renames["ApkIn"])
    types["ApkOut"] = t.struct(
        {
            "versionCode": t.integer().optional(),
            "binary": t.proxy(renames["ApkBinaryOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApkOut"])
    types["UpgradeTargetingRuleIn"] = t.struct(
        {
            "scope": t.proxy(renames["TargetingRuleScopeIn"]),
            "billingPeriodDuration": t.string().optional(),
            "oncePerUser": t.boolean().optional(),
        }
    ).named(renames["UpgradeTargetingRuleIn"])
    types["UpgradeTargetingRuleOut"] = t.struct(
        {
            "scope": t.proxy(renames["TargetingRuleScopeOut"]),
            "billingPeriodDuration": t.string().optional(),
            "oncePerUser": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpgradeTargetingRuleOut"])
    types["PausedStateContextIn"] = t.struct(
        {"autoResumeTime": t.string().optional()}
    ).named(renames["PausedStateContextIn"])
    types["PausedStateContextOut"] = t.struct(
        {
            "autoResumeTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PausedStateContextOut"])
    types["VariantIn"] = t.struct(
        {"deviceSpec": t.proxy(renames["DeviceSpecIn"]).optional()}
    ).named(renames["VariantIn"])
    types["VariantOut"] = t.struct(
        {
            "variantId": t.integer().optional(),
            "deviceSpec": t.proxy(renames["DeviceSpecOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VariantOut"])
    types["ConvertRegionPricesRequestIn"] = t.struct(
        {"price": t.proxy(renames["MoneyIn"]).optional()}
    ).named(renames["ConvertRegionPricesRequestIn"])
    types["ConvertRegionPricesRequestOut"] = t.struct(
        {
            "price": t.proxy(renames["MoneyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConvertRegionPricesRequestOut"])

    functions = {}
    functions["externaltransactionsRefundexternaltransaction"] = androidpublisher.get(
        "androidpublisher/v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ExternalTransactionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["externaltransactionsCreateexternaltransaction"] = androidpublisher.get(
        "androidpublisher/v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ExternalTransactionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["externaltransactionsGetexternaltransaction"] = androidpublisher.get(
        "androidpublisher/v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ExternalTransactionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["ordersRefund"] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/orders/{orderId}:refund",
        t.struct(
            {
                "revoke": t.boolean().optional(),
                "packageName": t.string().optional(),
                "orderId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["grantsDelete"] = androidpublisher.patch(
        "androidpublisher/v3/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "appLevelPermissions": t.array(t.string()).optional(),
                "packageName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GrantOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["grantsCreate"] = androidpublisher.patch(
        "androidpublisher/v3/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "appLevelPermissions": t.array(t.string()).optional(),
                "packageName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GrantOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["grantsPatch"] = androidpublisher.patch(
        "androidpublisher/v3/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "appLevelPermissions": t.array(t.string()).optional(),
                "packageName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GrantOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsDelete"] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}:validate",
        t.struct(
            {
                "packageName": t.string().optional(),
                "editId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AppEditOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsInsert"] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}:validate",
        t.struct(
            {
                "packageName": t.string().optional(),
                "editId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AppEditOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsGet"] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}:validate",
        t.struct(
            {
                "packageName": t.string().optional(),
                "editId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AppEditOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsCommit"] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}:validate",
        t.struct(
            {
                "packageName": t.string().optional(),
                "editId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AppEditOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsValidate"] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}:validate",
        t.struct(
            {
                "packageName": t.string().optional(),
                "editId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AppEditOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsTestersUpdate"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/testers/{track}",
        t.struct(
            {
                "editId": t.string().optional(),
                "track": t.string().optional(),
                "packageName": t.string().optional(),
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
                "editId": t.string().optional(),
                "track": t.string().optional(),
                "packageName": t.string().optional(),
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
                "editId": t.string().optional(),
                "track": t.string().optional(),
                "packageName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestersOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsExpansionfilesUpdate"] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/apks/{apkVersionCode}/expansionFiles/{expansionFileType}",
        t.struct(
            {
                "packageName": t.string().optional(),
                "expansionFileType": t.string().optional(),
                "editId": t.string().optional(),
                "apkVersionCode": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExpansionFilesUploadResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsExpansionfilesGet"] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/apks/{apkVersionCode}/expansionFiles/{expansionFileType}",
        t.struct(
            {
                "packageName": t.string().optional(),
                "expansionFileType": t.string().optional(),
                "editId": t.string().optional(),
                "apkVersionCode": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExpansionFilesUploadResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsExpansionfilesPatch"] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/apks/{apkVersionCode}/expansionFiles/{expansionFileType}",
        t.struct(
            {
                "packageName": t.string().optional(),
                "expansionFileType": t.string().optional(),
                "editId": t.string().optional(),
                "apkVersionCode": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExpansionFilesUploadResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsExpansionfilesUpload"] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/apks/{apkVersionCode}/expansionFiles/{expansionFileType}",
        t.struct(
            {
                "packageName": t.string().optional(),
                "expansionFileType": t.string().optional(),
                "editId": t.string().optional(),
                "apkVersionCode": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExpansionFilesUploadResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsImagesDeleteall"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/listings/{language}/{imageType}",
        t.struct(
            {
                "packageName": t.string().optional(),
                "language": t.string().optional(),
                "editId": t.string().optional(),
                "imageType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ImagesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsImagesDelete"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/listings/{language}/{imageType}",
        t.struct(
            {
                "packageName": t.string().optional(),
                "language": t.string().optional(),
                "editId": t.string().optional(),
                "imageType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ImagesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsImagesUpload"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/listings/{language}/{imageType}",
        t.struct(
            {
                "packageName": t.string().optional(),
                "language": t.string().optional(),
                "editId": t.string().optional(),
                "imageType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ImagesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsImagesList"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/listings/{language}/{imageType}",
        t.struct(
            {
                "packageName": t.string().optional(),
                "language": t.string().optional(),
                "editId": t.string().optional(),
                "imageType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ImagesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsDetailsGet"] = androidpublisher.put(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/details",
        t.struct(
            {
                "packageName": t.string().optional(),
                "editId": t.string().optional(),
                "contactPhone": t.string().optional(),
                "defaultLanguage": t.string().optional(),
                "contactWebsite": t.string().optional(),
                "contactEmail": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AppDetailsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsDetailsPatch"] = androidpublisher.put(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/details",
        t.struct(
            {
                "packageName": t.string().optional(),
                "editId": t.string().optional(),
                "contactPhone": t.string().optional(),
                "defaultLanguage": t.string().optional(),
                "contactWebsite": t.string().optional(),
                "contactEmail": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AppDetailsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsDetailsUpdate"] = androidpublisher.put(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/details",
        t.struct(
            {
                "packageName": t.string().optional(),
                "editId": t.string().optional(),
                "contactPhone": t.string().optional(),
                "defaultLanguage": t.string().optional(),
                "contactWebsite": t.string().optional(),
                "contactEmail": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AppDetailsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsListingsGet"] = androidpublisher.delete(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/listings",
        t.struct(
            {
                "editId": t.string().optional(),
                "packageName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsListingsDelete"] = androidpublisher.delete(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/listings",
        t.struct(
            {
                "editId": t.string().optional(),
                "packageName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsListingsList"] = androidpublisher.delete(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/listings",
        t.struct(
            {
                "editId": t.string().optional(),
                "packageName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsListingsPatch"] = androidpublisher.delete(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/listings",
        t.struct(
            {
                "editId": t.string().optional(),
                "packageName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsListingsUpdate"] = androidpublisher.delete(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/listings",
        t.struct(
            {
                "editId": t.string().optional(),
                "packageName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsListingsDeleteall"] = androidpublisher.delete(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/listings",
        t.struct(
            {
                "editId": t.string().optional(),
                "packageName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsTracksUpdate"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/tracks/{track}",
        t.struct(
            {
                "track": t.string().optional(),
                "packageName": t.string().optional(),
                "editId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TrackOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsTracksList"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/tracks/{track}",
        t.struct(
            {
                "track": t.string().optional(),
                "packageName": t.string().optional(),
                "editId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TrackOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsTracksPatch"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/tracks/{track}",
        t.struct(
            {
                "track": t.string().optional(),
                "packageName": t.string().optional(),
                "editId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TrackOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsTracksGet"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/tracks/{track}",
        t.struct(
            {
                "track": t.string().optional(),
                "packageName": t.string().optional(),
                "editId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TrackOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsBundlesUpload"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/bundles",
        t.struct(
            {
                "packageName": t.string().optional(),
                "editId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BundlesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsBundlesList"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/bundles",
        t.struct(
            {
                "packageName": t.string().optional(),
                "editId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BundlesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["editsCountryavailabilityGet"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/countryAvailability/{track}",
        t.struct(
            {
                "packageName": t.string().optional(),
                "track": t.string().optional(),
                "editId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TrackCountryAvailabilityOut"]),
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
    functions["editsDeobfuscationfilesUpload"] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/edits/{editId}/apks/{apkVersionCode}/deobfuscationFiles/{deobfuscationFileType}",
        t.struct(
            {
                "packageName": t.string().optional(),
                "deobfuscationFileType": t.string().optional(),
                "apkVersionCode": t.integer().optional(),
                "editId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeobfuscationFilesUploadResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["systemapksVariantsGet"] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/systemApks/{versionCode}/variants",
        t.struct(
            {
                "packageName": t.string().optional(),
                "versionCode": t.string().optional(),
                "deviceSpec": t.proxy(renames["DeviceSpecIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VariantOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["systemapksVariantsDownload"] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/systemApks/{versionCode}/variants",
        t.struct(
            {
                "packageName": t.string().optional(),
                "versionCode": t.string().optional(),
                "deviceSpec": t.proxy(renames["DeviceSpecIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VariantOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["systemapksVariantsList"] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/systemApks/{versionCode}/variants",
        t.struct(
            {
                "packageName": t.string().optional(),
                "versionCode": t.string().optional(),
                "deviceSpec": t.proxy(renames["DeviceSpecIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VariantOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["systemapksVariantsCreate"] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/systemApks/{versionCode}/variants",
        t.struct(
            {
                "packageName": t.string().optional(),
                "versionCode": t.string().optional(),
                "deviceSpec": t.proxy(renames["DeviceSpecIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VariantOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["reviewsGet"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/reviews",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "token": t.string().optional(),
                "packageName": t.string().optional(),
                "translationLanguage": t.string().optional(),
                "startIndex": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReviewsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["reviewsReply"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/reviews",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "token": t.string().optional(),
                "packageName": t.string().optional(),
                "translationLanguage": t.string().optional(),
                "startIndex": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReviewsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["reviewsList"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/reviews",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "token": t.string().optional(),
                "packageName": t.string().optional(),
                "translationLanguage": t.string().optional(),
                "startIndex": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReviewsListResponseOut"]),
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
    functions["purchasesSubscriptionsDefer"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/purchases/subscriptions/{subscriptionId}/tokens/{token}",
        t.struct(
            {
                "subscriptionId": t.string().optional(),
                "packageName": t.string().optional(),
                "token": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionPurchaseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["purchasesSubscriptionsRefund"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/purchases/subscriptions/{subscriptionId}/tokens/{token}",
        t.struct(
            {
                "subscriptionId": t.string().optional(),
                "packageName": t.string().optional(),
                "token": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionPurchaseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["purchasesSubscriptionsAcknowledge"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/purchases/subscriptions/{subscriptionId}/tokens/{token}",
        t.struct(
            {
                "subscriptionId": t.string().optional(),
                "packageName": t.string().optional(),
                "token": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionPurchaseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["purchasesSubscriptionsRevoke"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/purchases/subscriptions/{subscriptionId}/tokens/{token}",
        t.struct(
            {
                "subscriptionId": t.string().optional(),
                "packageName": t.string().optional(),
                "token": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionPurchaseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["purchasesSubscriptionsCancel"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/purchases/subscriptions/{subscriptionId}/tokens/{token}",
        t.struct(
            {
                "subscriptionId": t.string().optional(),
                "packageName": t.string().optional(),
                "token": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionPurchaseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["purchasesSubscriptionsGet"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/purchases/subscriptions/{subscriptionId}/tokens/{token}",
        t.struct(
            {
                "subscriptionId": t.string().optional(),
                "packageName": t.string().optional(),
                "token": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionPurchaseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["purchasesVoidedpurchasesList"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/purchases/voidedpurchases",
        t.struct(
            {
                "startIndex": t.integer().optional(),
                "startTime": t.string().optional(),
                "maxResults": t.integer().optional(),
                "token": t.string().optional(),
                "endTime": t.string().optional(),
                "packageName": t.string().optional(),
                "type": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VoidedPurchasesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["purchasesProductsGet"] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/purchases/products/{productId}/tokens/{token}:consume",
        t.struct(
            {
                "productId": t.string().optional(),
                "token": t.string().optional(),
                "packageName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["purchasesProductsAcknowledge"] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/purchases/products/{productId}/tokens/{token}:consume",
        t.struct(
            {
                "productId": t.string().optional(),
                "token": t.string().optional(),
                "packageName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["purchasesProductsConsume"] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/purchases/products/{productId}/tokens/{token}:consume",
        t.struct(
            {
                "productId": t.string().optional(),
                "token": t.string().optional(),
                "packageName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
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
    functions["monetizationSubscriptionsBasePlansActivate"] = androidpublisher.delete(
        "androidpublisher/v3/applications/{packageName}/subscriptions/{productId}/basePlans/{basePlanId}",
        t.struct(
            {
                "packageName": t.string(),
                "basePlanId": t.string(),
                "productId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["monetizationSubscriptionsBasePlansDeactivate"] = androidpublisher.delete(
        "androidpublisher/v3/applications/{packageName}/subscriptions/{productId}/basePlans/{basePlanId}",
        t.struct(
            {
                "packageName": t.string(),
                "basePlanId": t.string(),
                "productId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "monetizationSubscriptionsBasePlansMigratePrices"
    ] = androidpublisher.delete(
        "androidpublisher/v3/applications/{packageName}/subscriptions/{productId}/basePlans/{basePlanId}",
        t.struct(
            {
                "packageName": t.string(),
                "basePlanId": t.string(),
                "productId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["monetizationSubscriptionsBasePlansDelete"] = androidpublisher.delete(
        "androidpublisher/v3/applications/{packageName}/subscriptions/{productId}/basePlans/{basePlanId}",
        t.struct(
            {
                "packageName": t.string(),
                "basePlanId": t.string(),
                "productId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["monetizationSubscriptionsBasePlansOffersCreate"] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/subscriptions/{productId}/basePlans/{basePlanId}/offers/{offerId}:activate",
        t.struct(
            {
                "productId": t.string(),
                "basePlanId": t.string(),
                "packageName": t.string(),
                "offerId": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionOfferOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["monetizationSubscriptionsBasePlansOffersGet"] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/subscriptions/{productId}/basePlans/{basePlanId}/offers/{offerId}:activate",
        t.struct(
            {
                "productId": t.string(),
                "basePlanId": t.string(),
                "packageName": t.string(),
                "offerId": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionOfferOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "monetizationSubscriptionsBasePlansOffersDeactivate"
    ] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/subscriptions/{productId}/basePlans/{basePlanId}/offers/{offerId}:activate",
        t.struct(
            {
                "productId": t.string(),
                "basePlanId": t.string(),
                "packageName": t.string(),
                "offerId": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionOfferOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["monetizationSubscriptionsBasePlansOffersPatch"] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/subscriptions/{productId}/basePlans/{basePlanId}/offers/{offerId}:activate",
        t.struct(
            {
                "productId": t.string(),
                "basePlanId": t.string(),
                "packageName": t.string(),
                "offerId": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionOfferOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["monetizationSubscriptionsBasePlansOffersDelete"] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/subscriptions/{productId}/basePlans/{basePlanId}/offers/{offerId}:activate",
        t.struct(
            {
                "productId": t.string(),
                "basePlanId": t.string(),
                "packageName": t.string(),
                "offerId": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionOfferOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["monetizationSubscriptionsBasePlansOffersList"] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/subscriptions/{productId}/basePlans/{basePlanId}/offers/{offerId}:activate",
        t.struct(
            {
                "productId": t.string(),
                "basePlanId": t.string(),
                "packageName": t.string(),
                "offerId": t.string(),
                "_": t.string().optional(),
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
        "androidpublisher/v3/applications/{packageName}/subscriptions/{productId}/basePlans/{basePlanId}/offers/{offerId}:activate",
        t.struct(
            {
                "productId": t.string(),
                "basePlanId": t.string(),
                "packageName": t.string(),
                "offerId": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionOfferOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["applicationsDeviceTierConfigsList"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/deviceTierConfigs/{deviceTierConfigId}",
        t.struct(
            {
                "deviceTierConfigId": t.string(),
                "packageName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeviceTierConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["applicationsDeviceTierConfigsCreate"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/deviceTierConfigs/{deviceTierConfigId}",
        t.struct(
            {
                "deviceTierConfigId": t.string(),
                "packageName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeviceTierConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["applicationsDeviceTierConfigsGet"] = androidpublisher.get(
        "androidpublisher/v3/applications/{packageName}/deviceTierConfigs/{deviceTierConfigId}",
        t.struct(
            {
                "deviceTierConfigId": t.string(),
                "packageName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeviceTierConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inappproductsUpdate"] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/inappproducts",
        t.struct(
            {
                "autoConvertMissingPrices": t.boolean().optional(),
                "packageName": t.string().optional(),
                "gracePeriod": t.string().optional(),
                "defaultPrice": t.proxy(renames["PriceIn"]).optional(),
                "subscriptionTaxesAndComplianceSettings": t.proxy(
                    renames["SubscriptionTaxAndComplianceSettingsIn"]
                ).optional(),
                "purchaseType": t.string().optional(),
                "prices": t.struct({"_": t.string().optional()}).optional(),
                "defaultLanguage": t.string().optional(),
                "sku": t.string().optional(),
                "managedProductTaxesAndComplianceSettings": t.proxy(
                    renames["ManagedProductTaxAndComplianceSettingsIn"]
                ).optional(),
                "trialPeriod": t.string().optional(),
                "listings": t.struct({"_": t.string().optional()}).optional(),
                "subscriptionPeriod": t.string().optional(),
                "status": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InAppProductOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inappproductsGet"] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/inappproducts",
        t.struct(
            {
                "autoConvertMissingPrices": t.boolean().optional(),
                "packageName": t.string().optional(),
                "gracePeriod": t.string().optional(),
                "defaultPrice": t.proxy(renames["PriceIn"]).optional(),
                "subscriptionTaxesAndComplianceSettings": t.proxy(
                    renames["SubscriptionTaxAndComplianceSettingsIn"]
                ).optional(),
                "purchaseType": t.string().optional(),
                "prices": t.struct({"_": t.string().optional()}).optional(),
                "defaultLanguage": t.string().optional(),
                "sku": t.string().optional(),
                "managedProductTaxesAndComplianceSettings": t.proxy(
                    renames["ManagedProductTaxAndComplianceSettingsIn"]
                ).optional(),
                "trialPeriod": t.string().optional(),
                "listings": t.struct({"_": t.string().optional()}).optional(),
                "subscriptionPeriod": t.string().optional(),
                "status": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InAppProductOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inappproductsPatch"] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/inappproducts",
        t.struct(
            {
                "autoConvertMissingPrices": t.boolean().optional(),
                "packageName": t.string().optional(),
                "gracePeriod": t.string().optional(),
                "defaultPrice": t.proxy(renames["PriceIn"]).optional(),
                "subscriptionTaxesAndComplianceSettings": t.proxy(
                    renames["SubscriptionTaxAndComplianceSettingsIn"]
                ).optional(),
                "purchaseType": t.string().optional(),
                "prices": t.struct({"_": t.string().optional()}).optional(),
                "defaultLanguage": t.string().optional(),
                "sku": t.string().optional(),
                "managedProductTaxesAndComplianceSettings": t.proxy(
                    renames["ManagedProductTaxAndComplianceSettingsIn"]
                ).optional(),
                "trialPeriod": t.string().optional(),
                "listings": t.struct({"_": t.string().optional()}).optional(),
                "subscriptionPeriod": t.string().optional(),
                "status": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InAppProductOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inappproductsList"] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/inappproducts",
        t.struct(
            {
                "autoConvertMissingPrices": t.boolean().optional(),
                "packageName": t.string().optional(),
                "gracePeriod": t.string().optional(),
                "defaultPrice": t.proxy(renames["PriceIn"]).optional(),
                "subscriptionTaxesAndComplianceSettings": t.proxy(
                    renames["SubscriptionTaxAndComplianceSettingsIn"]
                ).optional(),
                "purchaseType": t.string().optional(),
                "prices": t.struct({"_": t.string().optional()}).optional(),
                "defaultLanguage": t.string().optional(),
                "sku": t.string().optional(),
                "managedProductTaxesAndComplianceSettings": t.proxy(
                    renames["ManagedProductTaxAndComplianceSettingsIn"]
                ).optional(),
                "trialPeriod": t.string().optional(),
                "listings": t.struct({"_": t.string().optional()}).optional(),
                "subscriptionPeriod": t.string().optional(),
                "status": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InAppProductOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inappproductsDelete"] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/inappproducts",
        t.struct(
            {
                "autoConvertMissingPrices": t.boolean().optional(),
                "packageName": t.string().optional(),
                "gracePeriod": t.string().optional(),
                "defaultPrice": t.proxy(renames["PriceIn"]).optional(),
                "subscriptionTaxesAndComplianceSettings": t.proxy(
                    renames["SubscriptionTaxAndComplianceSettingsIn"]
                ).optional(),
                "purchaseType": t.string().optional(),
                "prices": t.struct({"_": t.string().optional()}).optional(),
                "defaultLanguage": t.string().optional(),
                "sku": t.string().optional(),
                "managedProductTaxesAndComplianceSettings": t.proxy(
                    renames["ManagedProductTaxAndComplianceSettingsIn"]
                ).optional(),
                "trialPeriod": t.string().optional(),
                "listings": t.struct({"_": t.string().optional()}).optional(),
                "subscriptionPeriod": t.string().optional(),
                "status": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InAppProductOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inappproductsInsert"] = androidpublisher.post(
        "androidpublisher/v3/applications/{packageName}/inappproducts",
        t.struct(
            {
                "autoConvertMissingPrices": t.boolean().optional(),
                "packageName": t.string().optional(),
                "gracePeriod": t.string().optional(),
                "defaultPrice": t.proxy(renames["PriceIn"]).optional(),
                "subscriptionTaxesAndComplianceSettings": t.proxy(
                    renames["SubscriptionTaxAndComplianceSettingsIn"]
                ).optional(),
                "purchaseType": t.string().optional(),
                "prices": t.struct({"_": t.string().optional()}).optional(),
                "defaultLanguage": t.string().optional(),
                "sku": t.string().optional(),
                "managedProductTaxesAndComplianceSettings": t.proxy(
                    renames["ManagedProductTaxAndComplianceSettingsIn"]
                ).optional(),
                "trialPeriod": t.string().optional(),
                "listings": t.struct({"_": t.string().optional()}).optional(),
                "subscriptionPeriod": t.string().optional(),
                "status": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InAppProductOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersPatch"] = androidpublisher.post(
        "androidpublisher/v3/{parent}/users",
        t.struct(
            {
                "parent": t.string(),
                "expirationTime": t.string().optional(),
                "developerAccountPermissions": t.array(t.string()).optional(),
                "email": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersList"] = androidpublisher.post(
        "androidpublisher/v3/{parent}/users",
        t.struct(
            {
                "parent": t.string(),
                "expirationTime": t.string().optional(),
                "developerAccountPermissions": t.array(t.string()).optional(),
                "email": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersDelete"] = androidpublisher.post(
        "androidpublisher/v3/{parent}/users",
        t.struct(
            {
                "parent": t.string(),
                "expirationTime": t.string().optional(),
                "developerAccountPermissions": t.array(t.string()).optional(),
                "email": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersCreate"] = androidpublisher.post(
        "androidpublisher/v3/{parent}/users",
        t.struct(
            {
                "parent": t.string(),
                "expirationTime": t.string().optional(),
                "developerAccountPermissions": t.array(t.string()).optional(),
                "email": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
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

    return Import(
        importer="androidpublisher",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
