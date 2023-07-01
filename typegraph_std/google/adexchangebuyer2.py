from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_adexchangebuyer2():
    adexchangebuyer2 = HTTPRuntime("https://adexchangebuyer.googleapis.com/")

    renames = {
        "ErrorResponse": "_adexchangebuyer2_1_ErrorResponse",
        "RealtimeTimeRangeIn": "_adexchangebuyer2_2_RealtimeTimeRangeIn",
        "RealtimeTimeRangeOut": "_adexchangebuyer2_3_RealtimeTimeRangeOut",
        "HtmlContentIn": "_adexchangebuyer2_4_HtmlContentIn",
        "HtmlContentOut": "_adexchangebuyer2_5_HtmlContentOut",
        "ListProposalsResponseIn": "_adexchangebuyer2_6_ListProposalsResponseIn",
        "ListProposalsResponseOut": "_adexchangebuyer2_7_ListProposalsResponseOut",
        "TargetingValueIn": "_adexchangebuyer2_8_TargetingValueIn",
        "TargetingValueOut": "_adexchangebuyer2_9_TargetingValueOut",
        "OperatingSystemTargetingIn": "_adexchangebuyer2_10_OperatingSystemTargetingIn",
        "OperatingSystemTargetingOut": "_adexchangebuyer2_11_OperatingSystemTargetingOut",
        "DeliveryControlIn": "_adexchangebuyer2_12_DeliveryControlIn",
        "DeliveryControlOut": "_adexchangebuyer2_13_DeliveryControlOut",
        "NativeContentIn": "_adexchangebuyer2_14_NativeContentIn",
        "NativeContentOut": "_adexchangebuyer2_15_NativeContentOut",
        "VideoTargetingIn": "_adexchangebuyer2_16_VideoTargetingIn",
        "VideoTargetingOut": "_adexchangebuyer2_17_VideoTargetingOut",
        "ContactInformationIn": "_adexchangebuyer2_18_ContactInformationIn",
        "ContactInformationOut": "_adexchangebuyer2_19_ContactInformationOut",
        "DealTermsIn": "_adexchangebuyer2_20_DealTermsIn",
        "DealTermsOut": "_adexchangebuyer2_21_DealTermsOut",
        "CancelNegotiationRequestIn": "_adexchangebuyer2_22_CancelNegotiationRequestIn",
        "CancelNegotiationRequestOut": "_adexchangebuyer2_23_CancelNegotiationRequestOut",
        "ResumeProposalDealsRequestIn": "_adexchangebuyer2_24_ResumeProposalDealsRequestIn",
        "ResumeProposalDealsRequestOut": "_adexchangebuyer2_25_ResumeProposalDealsRequestOut",
        "ListDealAssociationsResponseIn": "_adexchangebuyer2_26_ListDealAssociationsResponseIn",
        "ListDealAssociationsResponseOut": "_adexchangebuyer2_27_ListDealAssociationsResponseOut",
        "UrlTargetingIn": "_adexchangebuyer2_28_UrlTargetingIn",
        "UrlTargetingOut": "_adexchangebuyer2_29_UrlTargetingOut",
        "ListFilteredBidsResponseIn": "_adexchangebuyer2_30_ListFilteredBidsResponseIn",
        "ListFilteredBidsResponseOut": "_adexchangebuyer2_31_ListFilteredBidsResponseOut",
        "NonGuaranteedAuctionTermsIn": "_adexchangebuyer2_32_NonGuaranteedAuctionTermsIn",
        "NonGuaranteedAuctionTermsOut": "_adexchangebuyer2_33_NonGuaranteedAuctionTermsOut",
        "EmptyIn": "_adexchangebuyer2_34_EmptyIn",
        "EmptyOut": "_adexchangebuyer2_35_EmptyOut",
        "CreativeIn": "_adexchangebuyer2_36_CreativeIn",
        "CreativeOut": "_adexchangebuyer2_37_CreativeOut",
        "TechnologyTargetingIn": "_adexchangebuyer2_38_TechnologyTargetingIn",
        "TechnologyTargetingOut": "_adexchangebuyer2_39_TechnologyTargetingOut",
        "ListFilterSetsResponseIn": "_adexchangebuyer2_40_ListFilterSetsResponseIn",
        "ListFilterSetsResponseOut": "_adexchangebuyer2_41_ListFilterSetsResponseOut",
        "ListFilteredBidRequestsResponseIn": "_adexchangebuyer2_42_ListFilteredBidRequestsResponseIn",
        "ListFilteredBidRequestsResponseOut": "_adexchangebuyer2_43_ListFilteredBidRequestsResponseOut",
        "PauseProposalRequestIn": "_adexchangebuyer2_44_PauseProposalRequestIn",
        "PauseProposalRequestOut": "_adexchangebuyer2_45_PauseProposalRequestOut",
        "ListBidMetricsResponseIn": "_adexchangebuyer2_46_ListBidMetricsResponseIn",
        "ListBidMetricsResponseOut": "_adexchangebuyer2_47_ListBidMetricsResponseOut",
        "FrequencyCapIn": "_adexchangebuyer2_48_FrequencyCapIn",
        "FrequencyCapOut": "_adexchangebuyer2_49_FrequencyCapOut",
        "PublisherProfileIn": "_adexchangebuyer2_50_PublisherProfileIn",
        "PublisherProfileOut": "_adexchangebuyer2_51_PublisherProfileOut",
        "MobileApplicationTargetingIn": "_adexchangebuyer2_52_MobileApplicationTargetingIn",
        "MobileApplicationTargetingOut": "_adexchangebuyer2_53_MobileApplicationTargetingOut",
        "FilteredBidDetailRowIn": "_adexchangebuyer2_54_FilteredBidDetailRowIn",
        "FilteredBidDetailRowOut": "_adexchangebuyer2_55_FilteredBidDetailRowOut",
        "AddNoteRequestIn": "_adexchangebuyer2_56_AddNoteRequestIn",
        "AddNoteRequestOut": "_adexchangebuyer2_57_AddNoteRequestOut",
        "FilterSetIn": "_adexchangebuyer2_58_FilterSetIn",
        "FilterSetOut": "_adexchangebuyer2_59_FilterSetOut",
        "CalloutStatusRowIn": "_adexchangebuyer2_60_CalloutStatusRowIn",
        "CalloutStatusRowOut": "_adexchangebuyer2_61_CalloutStatusRowOut",
        "ListClientsResponseIn": "_adexchangebuyer2_62_ListClientsResponseIn",
        "ListClientsResponseOut": "_adexchangebuyer2_63_ListClientsResponseOut",
        "AuctionContextIn": "_adexchangebuyer2_64_AuctionContextIn",
        "AuctionContextOut": "_adexchangebuyer2_65_AuctionContextOut",
        "PriceIn": "_adexchangebuyer2_66_PriceIn",
        "PriceOut": "_adexchangebuyer2_67_PriceOut",
        "PublisherProfileMobileApplicationIn": "_adexchangebuyer2_68_PublisherProfileMobileApplicationIn",
        "PublisherProfileMobileApplicationOut": "_adexchangebuyer2_69_PublisherProfileMobileApplicationOut",
        "NoteIn": "_adexchangebuyer2_70_NoteIn",
        "NoteOut": "_adexchangebuyer2_71_NoteOut",
        "ListClientUserInvitationsResponseIn": "_adexchangebuyer2_72_ListClientUserInvitationsResponseIn",
        "ListClientUserInvitationsResponseOut": "_adexchangebuyer2_73_ListClientUserInvitationsResponseOut",
        "ResumeProposalRequestIn": "_adexchangebuyer2_74_ResumeProposalRequestIn",
        "ResumeProposalRequestOut": "_adexchangebuyer2_75_ResumeProposalRequestOut",
        "ListLosingBidsResponseIn": "_adexchangebuyer2_76_ListLosingBidsResponseIn",
        "ListLosingBidsResponseOut": "_adexchangebuyer2_77_ListLosingBidsResponseOut",
        "MoneyIn": "_adexchangebuyer2_78_MoneyIn",
        "MoneyOut": "_adexchangebuyer2_79_MoneyOut",
        "AppContextIn": "_adexchangebuyer2_80_AppContextIn",
        "AppContextOut": "_adexchangebuyer2_81_AppContextOut",
        "TimeOfDayIn": "_adexchangebuyer2_82_TimeOfDayIn",
        "TimeOfDayOut": "_adexchangebuyer2_83_TimeOfDayOut",
        "ClientIn": "_adexchangebuyer2_84_ClientIn",
        "ClientOut": "_adexchangebuyer2_85_ClientOut",
        "ListPublisherProfilesResponseIn": "_adexchangebuyer2_86_ListPublisherProfilesResponseIn",
        "ListPublisherProfilesResponseOut": "_adexchangebuyer2_87_ListPublisherProfilesResponseOut",
        "RelativeDateRangeIn": "_adexchangebuyer2_88_RelativeDateRangeIn",
        "RelativeDateRangeOut": "_adexchangebuyer2_89_RelativeDateRangeOut",
        "CompleteSetupRequestIn": "_adexchangebuyer2_90_CompleteSetupRequestIn",
        "CompleteSetupRequestOut": "_adexchangebuyer2_91_CompleteSetupRequestOut",
        "TimeIntervalIn": "_adexchangebuyer2_92_TimeIntervalIn",
        "TimeIntervalOut": "_adexchangebuyer2_93_TimeIntervalOut",
        "InventorySizeTargetingIn": "_adexchangebuyer2_94_InventorySizeTargetingIn",
        "InventorySizeTargetingOut": "_adexchangebuyer2_95_InventorySizeTargetingOut",
        "CreativeDealAssociationIn": "_adexchangebuyer2_96_CreativeDealAssociationIn",
        "CreativeDealAssociationOut": "_adexchangebuyer2_97_CreativeDealAssociationOut",
        "BidMetricsRowIn": "_adexchangebuyer2_98_BidMetricsRowIn",
        "BidMetricsRowOut": "_adexchangebuyer2_99_BidMetricsRowOut",
        "CriteriaTargetingIn": "_adexchangebuyer2_100_CriteriaTargetingIn",
        "CriteriaTargetingOut": "_adexchangebuyer2_101_CriteriaTargetingOut",
        "ListBidResponsesWithoutBidsResponseIn": "_adexchangebuyer2_102_ListBidResponsesWithoutBidsResponseIn",
        "ListBidResponsesWithoutBidsResponseOut": "_adexchangebuyer2_103_ListBidResponsesWithoutBidsResponseOut",
        "DayPartIn": "_adexchangebuyer2_104_DayPartIn",
        "DayPartOut": "_adexchangebuyer2_105_DayPartOut",
        "DealServingMetadataIn": "_adexchangebuyer2_106_DealServingMetadataIn",
        "DealServingMetadataOut": "_adexchangebuyer2_107_DealServingMetadataOut",
        "DayPartTargetingIn": "_adexchangebuyer2_108_DayPartTargetingIn",
        "DayPartTargetingOut": "_adexchangebuyer2_109_DayPartTargetingOut",
        "PlacementTargetingIn": "_adexchangebuyer2_110_PlacementTargetingIn",
        "PlacementTargetingOut": "_adexchangebuyer2_111_PlacementTargetingOut",
        "CorrectionIn": "_adexchangebuyer2_112_CorrectionIn",
        "CorrectionOut": "_adexchangebuyer2_113_CorrectionOut",
        "DealIn": "_adexchangebuyer2_114_DealIn",
        "DealOut": "_adexchangebuyer2_115_DealOut",
        "ListCreativeStatusBreakdownByCreativeResponseIn": "_adexchangebuyer2_116_ListCreativeStatusBreakdownByCreativeResponseIn",
        "ListCreativeStatusBreakdownByCreativeResponseOut": "_adexchangebuyer2_117_ListCreativeStatusBreakdownByCreativeResponseOut",
        "DisapprovalIn": "_adexchangebuyer2_118_DisapprovalIn",
        "DisapprovalOut": "_adexchangebuyer2_119_DisapprovalOut",
        "AbsoluteDateRangeIn": "_adexchangebuyer2_120_AbsoluteDateRangeIn",
        "AbsoluteDateRangeOut": "_adexchangebuyer2_121_AbsoluteDateRangeOut",
        "StopWatchingCreativeRequestIn": "_adexchangebuyer2_122_StopWatchingCreativeRequestIn",
        "StopWatchingCreativeRequestOut": "_adexchangebuyer2_123_StopWatchingCreativeRequestOut",
        "WatchCreativeRequestIn": "_adexchangebuyer2_124_WatchCreativeRequestIn",
        "WatchCreativeRequestOut": "_adexchangebuyer2_125_WatchCreativeRequestOut",
        "ListClientUsersResponseIn": "_adexchangebuyer2_126_ListClientUsersResponseIn",
        "ListClientUsersResponseOut": "_adexchangebuyer2_127_ListClientUsersResponseOut",
        "VideoContentIn": "_adexchangebuyer2_128_VideoContentIn",
        "VideoContentOut": "_adexchangebuyer2_129_VideoContentOut",
        "PrivateDataIn": "_adexchangebuyer2_130_PrivateDataIn",
        "PrivateDataOut": "_adexchangebuyer2_131_PrivateDataOut",
        "ListImpressionMetricsResponseIn": "_adexchangebuyer2_132_ListImpressionMetricsResponseIn",
        "ListImpressionMetricsResponseOut": "_adexchangebuyer2_133_ListImpressionMetricsResponseOut",
        "SizeIn": "_adexchangebuyer2_134_SizeIn",
        "SizeOut": "_adexchangebuyer2_135_SizeOut",
        "NonBillableWinningBidStatusRowIn": "_adexchangebuyer2_136_NonBillableWinningBidStatusRowIn",
        "NonBillableWinningBidStatusRowOut": "_adexchangebuyer2_137_NonBillableWinningBidStatusRowOut",
        "NonGuaranteedFixedPriceTermsIn": "_adexchangebuyer2_138_NonGuaranteedFixedPriceTermsIn",
        "NonGuaranteedFixedPriceTermsOut": "_adexchangebuyer2_139_NonGuaranteedFixedPriceTermsOut",
        "FilteredBidCreativeRowIn": "_adexchangebuyer2_140_FilteredBidCreativeRowIn",
        "FilteredBidCreativeRowOut": "_adexchangebuyer2_141_FilteredBidCreativeRowOut",
        "LocationContextIn": "_adexchangebuyer2_142_LocationContextIn",
        "LocationContextOut": "_adexchangebuyer2_143_LocationContextOut",
        "BuyerIn": "_adexchangebuyer2_144_BuyerIn",
        "BuyerOut": "_adexchangebuyer2_145_BuyerOut",
        "AdTechnologyProvidersIn": "_adexchangebuyer2_146_AdTechnologyProvidersIn",
        "AdTechnologyProvidersOut": "_adexchangebuyer2_147_AdTechnologyProvidersOut",
        "ServingRestrictionIn": "_adexchangebuyer2_148_ServingRestrictionIn",
        "ServingRestrictionOut": "_adexchangebuyer2_149_ServingRestrictionOut",
        "PricePerBuyerIn": "_adexchangebuyer2_150_PricePerBuyerIn",
        "PricePerBuyerOut": "_adexchangebuyer2_151_PricePerBuyerOut",
        "CreativeSpecificationIn": "_adexchangebuyer2_152_CreativeSpecificationIn",
        "CreativeSpecificationOut": "_adexchangebuyer2_153_CreativeSpecificationOut",
        "SecurityContextIn": "_adexchangebuyer2_154_SecurityContextIn",
        "SecurityContextOut": "_adexchangebuyer2_155_SecurityContextOut",
        "PlatformContextIn": "_adexchangebuyer2_156_PlatformContextIn",
        "PlatformContextOut": "_adexchangebuyer2_157_PlatformContextOut",
        "ImpressionMetricsRowIn": "_adexchangebuyer2_158_ImpressionMetricsRowIn",
        "ImpressionMetricsRowOut": "_adexchangebuyer2_159_ImpressionMetricsRowOut",
        "AddDealAssociationRequestIn": "_adexchangebuyer2_160_AddDealAssociationRequestIn",
        "AddDealAssociationRequestOut": "_adexchangebuyer2_161_AddDealAssociationRequestOut",
        "ListCreativeStatusBreakdownByDetailResponseIn": "_adexchangebuyer2_162_ListCreativeStatusBreakdownByDetailResponseIn",
        "ListCreativeStatusBreakdownByDetailResponseOut": "_adexchangebuyer2_163_ListCreativeStatusBreakdownByDetailResponseOut",
        "AcceptProposalRequestIn": "_adexchangebuyer2_164_AcceptProposalRequestIn",
        "AcceptProposalRequestOut": "_adexchangebuyer2_165_AcceptProposalRequestOut",
        "AdSizeIn": "_adexchangebuyer2_166_AdSizeIn",
        "AdSizeOut": "_adexchangebuyer2_167_AdSizeOut",
        "ListProductsResponseIn": "_adexchangebuyer2_168_ListProductsResponseIn",
        "ListProductsResponseOut": "_adexchangebuyer2_169_ListProductsResponseOut",
        "TargetingCriteriaIn": "_adexchangebuyer2_170_TargetingCriteriaIn",
        "TargetingCriteriaOut": "_adexchangebuyer2_171_TargetingCriteriaOut",
        "ProductIn": "_adexchangebuyer2_172_ProductIn",
        "ProductOut": "_adexchangebuyer2_173_ProductOut",
        "ListBidResponseErrorsResponseIn": "_adexchangebuyer2_174_ListBidResponseErrorsResponseIn",
        "ListBidResponseErrorsResponseOut": "_adexchangebuyer2_175_ListBidResponseErrorsResponseOut",
        "FirstPartyMobileApplicationTargetingIn": "_adexchangebuyer2_176_FirstPartyMobileApplicationTargetingIn",
        "FirstPartyMobileApplicationTargetingOut": "_adexchangebuyer2_177_FirstPartyMobileApplicationTargetingOut",
        "DateIn": "_adexchangebuyer2_178_DateIn",
        "DateOut": "_adexchangebuyer2_179_DateOut",
        "CreativeSizeIn": "_adexchangebuyer2_180_CreativeSizeIn",
        "CreativeSizeOut": "_adexchangebuyer2_181_CreativeSizeOut",
        "ListCreativesResponseIn": "_adexchangebuyer2_182_ListCreativesResponseIn",
        "ListCreativesResponseOut": "_adexchangebuyer2_183_ListCreativesResponseOut",
        "BidResponseWithoutBidsStatusRowIn": "_adexchangebuyer2_184_BidResponseWithoutBidsStatusRowIn",
        "BidResponseWithoutBidsStatusRowOut": "_adexchangebuyer2_185_BidResponseWithoutBidsStatusRowOut",
        "ClientUserInvitationIn": "_adexchangebuyer2_186_ClientUserInvitationIn",
        "ClientUserInvitationOut": "_adexchangebuyer2_187_ClientUserInvitationOut",
        "MarketplaceTargetingIn": "_adexchangebuyer2_188_MarketplaceTargetingIn",
        "MarketplaceTargetingOut": "_adexchangebuyer2_189_MarketplaceTargetingOut",
        "MetricValueIn": "_adexchangebuyer2_190_MetricValueIn",
        "MetricValueOut": "_adexchangebuyer2_191_MetricValueOut",
        "CreativeRestrictionsIn": "_adexchangebuyer2_192_CreativeRestrictionsIn",
        "CreativeRestrictionsOut": "_adexchangebuyer2_193_CreativeRestrictionsOut",
        "GuaranteedFixedPriceTermsIn": "_adexchangebuyer2_194_GuaranteedFixedPriceTermsIn",
        "GuaranteedFixedPriceTermsOut": "_adexchangebuyer2_195_GuaranteedFixedPriceTermsOut",
        "ListNonBillableWinningBidsResponseIn": "_adexchangebuyer2_196_ListNonBillableWinningBidsResponseIn",
        "ListNonBillableWinningBidsResponseOut": "_adexchangebuyer2_197_ListNonBillableWinningBidsResponseOut",
        "SellerIn": "_adexchangebuyer2_198_SellerIn",
        "SellerOut": "_adexchangebuyer2_199_SellerOut",
        "CreativeStatusRowIn": "_adexchangebuyer2_200_CreativeStatusRowIn",
        "CreativeStatusRowOut": "_adexchangebuyer2_201_CreativeStatusRowOut",
        "RowDimensionsIn": "_adexchangebuyer2_202_RowDimensionsIn",
        "RowDimensionsOut": "_adexchangebuyer2_203_RowDimensionsOut",
        "ServingContextIn": "_adexchangebuyer2_204_ServingContextIn",
        "ServingContextOut": "_adexchangebuyer2_205_ServingContextOut",
        "ClientUserIn": "_adexchangebuyer2_206_ClientUserIn",
        "ClientUserOut": "_adexchangebuyer2_207_ClientUserOut",
        "ImageIn": "_adexchangebuyer2_208_ImageIn",
        "ImageOut": "_adexchangebuyer2_209_ImageOut",
        "RemoveDealAssociationRequestIn": "_adexchangebuyer2_210_RemoveDealAssociationRequestIn",
        "RemoveDealAssociationRequestOut": "_adexchangebuyer2_211_RemoveDealAssociationRequestOut",
        "DealPauseStatusIn": "_adexchangebuyer2_212_DealPauseStatusIn",
        "DealPauseStatusOut": "_adexchangebuyer2_213_DealPauseStatusOut",
        "PauseProposalDealsRequestIn": "_adexchangebuyer2_214_PauseProposalDealsRequestIn",
        "PauseProposalDealsRequestOut": "_adexchangebuyer2_215_PauseProposalDealsRequestOut",
        "ProposalIn": "_adexchangebuyer2_216_ProposalIn",
        "ProposalOut": "_adexchangebuyer2_217_ProposalOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["RealtimeTimeRangeIn"] = t.struct(
        {"startTimestamp": t.string().optional()}
    ).named(renames["RealtimeTimeRangeIn"])
    types["RealtimeTimeRangeOut"] = t.struct(
        {
            "startTimestamp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RealtimeTimeRangeOut"])
    types["HtmlContentIn"] = t.struct(
        {
            "snippet": t.string().optional(),
            "height": t.integer().optional(),
            "width": t.integer().optional(),
        }
    ).named(renames["HtmlContentIn"])
    types["HtmlContentOut"] = t.struct(
        {
            "snippet": t.string().optional(),
            "height": t.integer().optional(),
            "width": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HtmlContentOut"])
    types["ListProposalsResponseIn"] = t.struct(
        {
            "proposals": t.array(t.proxy(renames["ProposalIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListProposalsResponseIn"])
    types["ListProposalsResponseOut"] = t.struct(
        {
            "proposals": t.array(t.proxy(renames["ProposalOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListProposalsResponseOut"])
    types["TargetingValueIn"] = t.struct(
        {
            "longValue": t.string().optional(),
            "dayPartTargetingValue": t.proxy(renames["DayPartTargetingIn"]).optional(),
            "creativeSizeValue": t.proxy(renames["CreativeSizeIn"]).optional(),
            "stringValue": t.string().optional(),
        }
    ).named(renames["TargetingValueIn"])
    types["TargetingValueOut"] = t.struct(
        {
            "longValue": t.string().optional(),
            "dayPartTargetingValue": t.proxy(renames["DayPartTargetingOut"]).optional(),
            "creativeSizeValue": t.proxy(renames["CreativeSizeOut"]).optional(),
            "stringValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetingValueOut"])
    types["OperatingSystemTargetingIn"] = t.struct(
        {
            "operatingSystemVersionCriteria": t.proxy(
                renames["CriteriaTargetingIn"]
            ).optional(),
            "operatingSystemCriteria": t.proxy(
                renames["CriteriaTargetingIn"]
            ).optional(),
        }
    ).named(renames["OperatingSystemTargetingIn"])
    types["OperatingSystemTargetingOut"] = t.struct(
        {
            "operatingSystemVersionCriteria": t.proxy(
                renames["CriteriaTargetingOut"]
            ).optional(),
            "operatingSystemCriteria": t.proxy(
                renames["CriteriaTargetingOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperatingSystemTargetingOut"])
    types["DeliveryControlIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeliveryControlIn"]
    )
    types["DeliveryControlOut"] = t.struct(
        {
            "frequencyCaps": t.array(t.proxy(renames["FrequencyCapOut"])).optional(),
            "creativeBlockingLevel": t.string().optional(),
            "deliveryRateType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeliveryControlOut"])
    types["NativeContentIn"] = t.struct(
        {
            "callToAction": t.string().optional(),
            "starRating": t.number().optional(),
            "headline": t.string().optional(),
            "clickTrackingUrl": t.string().optional(),
            "videoUrl": t.string().optional(),
            "body": t.string().optional(),
            "priceDisplayText": t.string().optional(),
            "storeUrl": t.string().optional(),
            "advertiserName": t.string().optional(),
            "image": t.proxy(renames["ImageIn"]).optional(),
            "appIcon": t.proxy(renames["ImageIn"]).optional(),
            "clickLinkUrl": t.string().optional(),
            "logo": t.proxy(renames["ImageIn"]).optional(),
        }
    ).named(renames["NativeContentIn"])
    types["NativeContentOut"] = t.struct(
        {
            "callToAction": t.string().optional(),
            "starRating": t.number().optional(),
            "headline": t.string().optional(),
            "clickTrackingUrl": t.string().optional(),
            "videoUrl": t.string().optional(),
            "body": t.string().optional(),
            "priceDisplayText": t.string().optional(),
            "storeUrl": t.string().optional(),
            "advertiserName": t.string().optional(),
            "image": t.proxy(renames["ImageOut"]).optional(),
            "appIcon": t.proxy(renames["ImageOut"]).optional(),
            "clickLinkUrl": t.string().optional(),
            "logo": t.proxy(renames["ImageOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NativeContentOut"])
    types["VideoTargetingIn"] = t.struct(
        {
            "excludedPositionTypes": t.array(t.string()).optional(),
            "targetedPositionTypes": t.array(t.string()).optional(),
        }
    ).named(renames["VideoTargetingIn"])
    types["VideoTargetingOut"] = t.struct(
        {
            "excludedPositionTypes": t.array(t.string()).optional(),
            "targetedPositionTypes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoTargetingOut"])
    types["ContactInformationIn"] = t.struct(
        {"email": t.string().optional(), "name": t.string().optional()}
    ).named(renames["ContactInformationIn"])
    types["ContactInformationOut"] = t.struct(
        {
            "email": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContactInformationOut"])
    types["DealTermsIn"] = t.struct(
        {
            "nonGuaranteedAuctionTerms": t.proxy(
                renames["NonGuaranteedAuctionTermsIn"]
            ).optional(),
            "description": t.string().optional(),
            "estimatedGrossSpend": t.proxy(renames["PriceIn"]).optional(),
            "estimatedImpressionsPerDay": t.string().optional(),
            "guaranteedFixedPriceTerms": t.proxy(
                renames["GuaranteedFixedPriceTermsIn"]
            ).optional(),
            "sellerTimeZone": t.string().optional(),
            "brandingType": t.string().optional(),
            "nonGuaranteedFixedPriceTerms": t.proxy(
                renames["NonGuaranteedFixedPriceTermsIn"]
            ).optional(),
        }
    ).named(renames["DealTermsIn"])
    types["DealTermsOut"] = t.struct(
        {
            "nonGuaranteedAuctionTerms": t.proxy(
                renames["NonGuaranteedAuctionTermsOut"]
            ).optional(),
            "description": t.string().optional(),
            "estimatedGrossSpend": t.proxy(renames["PriceOut"]).optional(),
            "estimatedImpressionsPerDay": t.string().optional(),
            "guaranteedFixedPriceTerms": t.proxy(
                renames["GuaranteedFixedPriceTermsOut"]
            ).optional(),
            "sellerTimeZone": t.string().optional(),
            "brandingType": t.string().optional(),
            "nonGuaranteedFixedPriceTerms": t.proxy(
                renames["NonGuaranteedFixedPriceTermsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DealTermsOut"])
    types["CancelNegotiationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelNegotiationRequestIn"]
    )
    types["CancelNegotiationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelNegotiationRequestOut"])
    types["ResumeProposalDealsRequestIn"] = t.struct(
        {"externalDealIds": t.array(t.string()).optional()}
    ).named(renames["ResumeProposalDealsRequestIn"])
    types["ResumeProposalDealsRequestOut"] = t.struct(
        {
            "externalDealIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResumeProposalDealsRequestOut"])
    types["ListDealAssociationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "associations": t.array(
                t.proxy(renames["CreativeDealAssociationIn"])
            ).optional(),
        }
    ).named(renames["ListDealAssociationsResponseIn"])
    types["ListDealAssociationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "associations": t.array(
                t.proxy(renames["CreativeDealAssociationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDealAssociationsResponseOut"])
    types["UrlTargetingIn"] = t.struct(
        {
            "excludedUrls": t.array(t.string()).optional(),
            "targetedUrls": t.array(t.string()).optional(),
        }
    ).named(renames["UrlTargetingIn"])
    types["UrlTargetingOut"] = t.struct(
        {
            "excludedUrls": t.array(t.string()).optional(),
            "targetedUrls": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UrlTargetingOut"])
    types["ListFilteredBidsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "creativeStatusRows": t.array(
                t.proxy(renames["CreativeStatusRowIn"])
            ).optional(),
        }
    ).named(renames["ListFilteredBidsResponseIn"])
    types["ListFilteredBidsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "creativeStatusRows": t.array(
                t.proxy(renames["CreativeStatusRowOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListFilteredBidsResponseOut"])
    types["NonGuaranteedAuctionTermsIn"] = t.struct(
        {
            "autoOptimizePrivateAuction": t.boolean().optional(),
            "reservePricesPerBuyer": t.array(
                t.proxy(renames["PricePerBuyerIn"])
            ).optional(),
        }
    ).named(renames["NonGuaranteedAuctionTermsIn"])
    types["NonGuaranteedAuctionTermsOut"] = t.struct(
        {
            "autoOptimizePrivateAuction": t.boolean().optional(),
            "reservePricesPerBuyer": t.array(
                t.proxy(renames["PricePerBuyerOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NonGuaranteedAuctionTermsOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["CreativeIn"] = t.struct(
        {
            "corrections": t.array(t.proxy(renames["CorrectionIn"])).optional(),
            "detectedDomains": t.array(t.string()).optional(),
            "servingRestrictions": t.array(
                t.proxy(renames["ServingRestrictionIn"])
            ).optional(),
            "native": t.proxy(renames["NativeContentIn"]).optional(),
            "version": t.integer().optional(),
            "video": t.proxy(renames["VideoContentIn"]).optional(),
            "detectedSensitiveCategories": t.array(t.integer()).optional(),
            "agencyId": t.string().optional(),
            "clickThroughUrls": t.array(t.string()).optional(),
            "adChoicesDestinationUrl": t.string().optional(),
            "detectedProductCategories": t.array(t.integer()).optional(),
            "adTechnologyProviders": t.proxy(
                renames["AdTechnologyProvidersIn"]
            ).optional(),
            "dealsStatus": t.string().optional(),
            "detectedLanguages": t.array(t.string()).optional(),
            "attributes": t.array(t.string()).optional(),
            "vendorIds": t.array(t.integer()).optional(),
            "advertiserName": t.string().optional(),
            "restrictedCategories": t.array(t.string()).optional(),
            "declaredClickThroughUrls": t.array(t.string()).optional(),
            "detectedAdvertiserIds": t.array(t.string()).optional(),
            "impressionTrackingUrls": t.array(t.string()).optional(),
            "html": t.proxy(renames["HtmlContentIn"]).optional(),
            "accountId": t.string().optional(),
            "openAuctionStatus": t.string().optional(),
            "creativeId": t.string().optional(),
            "apiUpdateTime": t.string().optional(),
        }
    ).named(renames["CreativeIn"])
    types["CreativeOut"] = t.struct(
        {
            "corrections": t.array(t.proxy(renames["CorrectionOut"])).optional(),
            "detectedDomains": t.array(t.string()).optional(),
            "servingRestrictions": t.array(
                t.proxy(renames["ServingRestrictionOut"])
            ).optional(),
            "native": t.proxy(renames["NativeContentOut"]).optional(),
            "version": t.integer().optional(),
            "video": t.proxy(renames["VideoContentOut"]).optional(),
            "detectedSensitiveCategories": t.array(t.integer()).optional(),
            "agencyId": t.string().optional(),
            "clickThroughUrls": t.array(t.string()).optional(),
            "adChoicesDestinationUrl": t.string().optional(),
            "detectedProductCategories": t.array(t.integer()).optional(),
            "adTechnologyProviders": t.proxy(
                renames["AdTechnologyProvidersOut"]
            ).optional(),
            "dealsStatus": t.string().optional(),
            "detectedLanguages": t.array(t.string()).optional(),
            "attributes": t.array(t.string()).optional(),
            "vendorIds": t.array(t.integer()).optional(),
            "advertiserName": t.string().optional(),
            "restrictedCategories": t.array(t.string()).optional(),
            "declaredClickThroughUrls": t.array(t.string()).optional(),
            "detectedAdvertiserIds": t.array(t.string()).optional(),
            "impressionTrackingUrls": t.array(t.string()).optional(),
            "html": t.proxy(renames["HtmlContentOut"]).optional(),
            "accountId": t.string().optional(),
            "openAuctionStatus": t.string().optional(),
            "creativeId": t.string().optional(),
            "apiUpdateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeOut"])
    types["TechnologyTargetingIn"] = t.struct(
        {
            "deviceCategoryTargeting": t.proxy(
                renames["CriteriaTargetingIn"]
            ).optional(),
            "deviceCapabilityTargeting": t.proxy(
                renames["CriteriaTargetingIn"]
            ).optional(),
            "operatingSystemTargeting": t.proxy(
                renames["OperatingSystemTargetingIn"]
            ).optional(),
        }
    ).named(renames["TechnologyTargetingIn"])
    types["TechnologyTargetingOut"] = t.struct(
        {
            "deviceCategoryTargeting": t.proxy(
                renames["CriteriaTargetingOut"]
            ).optional(),
            "deviceCapabilityTargeting": t.proxy(
                renames["CriteriaTargetingOut"]
            ).optional(),
            "operatingSystemTargeting": t.proxy(
                renames["OperatingSystemTargetingOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TechnologyTargetingOut"])
    types["ListFilterSetsResponseIn"] = t.struct(
        {
            "filterSets": t.array(t.proxy(renames["FilterSetIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListFilterSetsResponseIn"])
    types["ListFilterSetsResponseOut"] = t.struct(
        {
            "filterSets": t.array(t.proxy(renames["FilterSetOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListFilterSetsResponseOut"])
    types["ListFilteredBidRequestsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "calloutStatusRows": t.array(
                t.proxy(renames["CalloutStatusRowIn"])
            ).optional(),
        }
    ).named(renames["ListFilteredBidRequestsResponseIn"])
    types["ListFilteredBidRequestsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "calloutStatusRows": t.array(
                t.proxy(renames["CalloutStatusRowOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListFilteredBidRequestsResponseOut"])
    types["PauseProposalRequestIn"] = t.struct({"reason": t.string().optional()}).named(
        renames["PauseProposalRequestIn"]
    )
    types["PauseProposalRequestOut"] = t.struct(
        {
            "reason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PauseProposalRequestOut"])
    types["ListBidMetricsResponseIn"] = t.struct(
        {
            "bidMetricsRows": t.array(t.proxy(renames["BidMetricsRowIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListBidMetricsResponseIn"])
    types["ListBidMetricsResponseOut"] = t.struct(
        {
            "bidMetricsRows": t.array(t.proxy(renames["BidMetricsRowOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBidMetricsResponseOut"])
    types["FrequencyCapIn"] = t.struct(
        {
            "timeUnitType": t.string().optional(),
            "numTimeUnits": t.integer().optional(),
            "maxImpressions": t.integer().optional(),
        }
    ).named(renames["FrequencyCapIn"])
    types["FrequencyCapOut"] = t.struct(
        {
            "timeUnitType": t.string().optional(),
            "numTimeUnits": t.integer().optional(),
            "maxImpressions": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FrequencyCapOut"])
    types["PublisherProfileIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "logoUrl": t.string().optional(),
            "mediaKitUrl": t.string().optional(),
            "samplePageUrl": t.string().optional(),
            "mobileApps": t.array(
                t.proxy(renames["PublisherProfileMobileApplicationIn"])
            ).optional(),
            "googlePlusUrl": t.string().optional(),
            "directDealsContact": t.string().optional(),
            "publisherProfileId": t.string().optional(),
            "programmaticDealsContact": t.string().optional(),
            "rateCardInfoUrl": t.string().optional(),
            "buyerPitchStatement": t.string().optional(),
            "domains": t.array(t.string()).optional(),
            "isParent": t.boolean().optional(),
            "audienceDescription": t.string().optional(),
            "seller": t.proxy(renames["SellerIn"]).optional(),
            "topHeadlines": t.array(t.string()).optional(),
            "overview": t.string().optional(),
        }
    ).named(renames["PublisherProfileIn"])
    types["PublisherProfileOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "logoUrl": t.string().optional(),
            "mediaKitUrl": t.string().optional(),
            "samplePageUrl": t.string().optional(),
            "mobileApps": t.array(
                t.proxy(renames["PublisherProfileMobileApplicationOut"])
            ).optional(),
            "googlePlusUrl": t.string().optional(),
            "directDealsContact": t.string().optional(),
            "publisherProfileId": t.string().optional(),
            "programmaticDealsContact": t.string().optional(),
            "rateCardInfoUrl": t.string().optional(),
            "buyerPitchStatement": t.string().optional(),
            "domains": t.array(t.string()).optional(),
            "isParent": t.boolean().optional(),
            "audienceDescription": t.string().optional(),
            "seller": t.proxy(renames["SellerOut"]).optional(),
            "topHeadlines": t.array(t.string()).optional(),
            "overview": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublisherProfileOut"])
    types["MobileApplicationTargetingIn"] = t.struct(
        {
            "firstPartyTargeting": t.proxy(
                renames["FirstPartyMobileApplicationTargetingIn"]
            ).optional()
        }
    ).named(renames["MobileApplicationTargetingIn"])
    types["MobileApplicationTargetingOut"] = t.struct(
        {
            "firstPartyTargeting": t.proxy(
                renames["FirstPartyMobileApplicationTargetingOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MobileApplicationTargetingOut"])
    types["FilteredBidDetailRowIn"] = t.struct(
        {
            "detailId": t.integer().optional(),
            "rowDimensions": t.proxy(renames["RowDimensionsIn"]).optional(),
            "detail": t.string().optional(),
            "bidCount": t.proxy(renames["MetricValueIn"]).optional(),
        }
    ).named(renames["FilteredBidDetailRowIn"])
    types["FilteredBidDetailRowOut"] = t.struct(
        {
            "detailId": t.integer().optional(),
            "rowDimensions": t.proxy(renames["RowDimensionsOut"]).optional(),
            "detail": t.string().optional(),
            "bidCount": t.proxy(renames["MetricValueOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilteredBidDetailRowOut"])
    types["AddNoteRequestIn"] = t.struct(
        {"note": t.proxy(renames["NoteIn"]).optional()}
    ).named(renames["AddNoteRequestIn"])
    types["AddNoteRequestOut"] = t.struct(
        {
            "note": t.proxy(renames["NoteOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddNoteRequestOut"])
    types["FilterSetIn"] = t.struct(
        {
            "creativeId": t.string().optional(),
            "realtimeTimeRange": t.proxy(renames["RealtimeTimeRangeIn"]).optional(),
            "dealId": t.string().optional(),
            "name": t.string().optional(),
            "platforms": t.array(t.string()).optional(),
            "sellerNetworkIds": t.array(t.integer()).optional(),
            "timeSeriesGranularity": t.string().optional(),
            "relativeDateRange": t.proxy(renames["RelativeDateRangeIn"]).optional(),
            "publisherIdentifiers": t.array(t.string()).optional(),
            "environment": t.string().optional(),
            "formats": t.array(t.string()).optional(),
            "format": t.string().optional(),
            "breakdownDimensions": t.array(t.string()).optional(),
            "absoluteDateRange": t.proxy(renames["AbsoluteDateRangeIn"]).optional(),
        }
    ).named(renames["FilterSetIn"])
    types["FilterSetOut"] = t.struct(
        {
            "creativeId": t.string().optional(),
            "realtimeTimeRange": t.proxy(renames["RealtimeTimeRangeOut"]).optional(),
            "dealId": t.string().optional(),
            "name": t.string().optional(),
            "platforms": t.array(t.string()).optional(),
            "sellerNetworkIds": t.array(t.integer()).optional(),
            "timeSeriesGranularity": t.string().optional(),
            "relativeDateRange": t.proxy(renames["RelativeDateRangeOut"]).optional(),
            "publisherIdentifiers": t.array(t.string()).optional(),
            "environment": t.string().optional(),
            "formats": t.array(t.string()).optional(),
            "format": t.string().optional(),
            "breakdownDimensions": t.array(t.string()).optional(),
            "absoluteDateRange": t.proxy(renames["AbsoluteDateRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterSetOut"])
    types["CalloutStatusRowIn"] = t.struct(
        {
            "impressionCount": t.proxy(renames["MetricValueIn"]).optional(),
            "rowDimensions": t.proxy(renames["RowDimensionsIn"]).optional(),
            "calloutStatusId": t.integer().optional(),
        }
    ).named(renames["CalloutStatusRowIn"])
    types["CalloutStatusRowOut"] = t.struct(
        {
            "impressionCount": t.proxy(renames["MetricValueOut"]).optional(),
            "rowDimensions": t.proxy(renames["RowDimensionsOut"]).optional(),
            "calloutStatusId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CalloutStatusRowOut"])
    types["ListClientsResponseIn"] = t.struct(
        {
            "clients": t.array(t.proxy(renames["ClientIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListClientsResponseIn"])
    types["ListClientsResponseOut"] = t.struct(
        {
            "clients": t.array(t.proxy(renames["ClientOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListClientsResponseOut"])
    types["AuctionContextIn"] = t.struct(
        {"auctionTypes": t.array(t.string()).optional()}
    ).named(renames["AuctionContextIn"])
    types["AuctionContextOut"] = t.struct(
        {
            "auctionTypes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuctionContextOut"])
    types["PriceIn"] = t.struct(
        {
            "amount": t.proxy(renames["MoneyIn"]).optional(),
            "pricingType": t.string().optional(),
        }
    ).named(renames["PriceIn"])
    types["PriceOut"] = t.struct(
        {
            "amount": t.proxy(renames["MoneyOut"]).optional(),
            "pricingType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PriceOut"])
    types["PublisherProfileMobileApplicationIn"] = t.struct(
        {
            "externalAppId": t.string().optional(),
            "appStore": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["PublisherProfileMobileApplicationIn"])
    types["PublisherProfileMobileApplicationOut"] = t.struct(
        {
            "externalAppId": t.string().optional(),
            "appStore": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublisherProfileMobileApplicationOut"])
    types["NoteIn"] = t.struct({"note": t.string().optional()}).named(renames["NoteIn"])
    types["NoteOut"] = t.struct(
        {
            "noteId": t.string().optional(),
            "createTime": t.string().optional(),
            "creatorRole": t.string().optional(),
            "note": t.string().optional(),
            "proposalRevision": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NoteOut"])
    types["ListClientUserInvitationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "invitations": t.array(
                t.proxy(renames["ClientUserInvitationIn"])
            ).optional(),
        }
    ).named(renames["ListClientUserInvitationsResponseIn"])
    types["ListClientUserInvitationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "invitations": t.array(
                t.proxy(renames["ClientUserInvitationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListClientUserInvitationsResponseOut"])
    types["ResumeProposalRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ResumeProposalRequestIn"]
    )
    types["ResumeProposalRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ResumeProposalRequestOut"])
    types["ListLosingBidsResponseIn"] = t.struct(
        {
            "creativeStatusRows": t.array(
                t.proxy(renames["CreativeStatusRowIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListLosingBidsResponseIn"])
    types["ListLosingBidsResponseOut"] = t.struct(
        {
            "creativeStatusRows": t.array(
                t.proxy(renames["CreativeStatusRowOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLosingBidsResponseOut"])
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
    types["AppContextIn"] = t.struct(
        {"appTypes": t.array(t.string()).optional()}
    ).named(renames["AppContextIn"])
    types["AppContextOut"] = t.struct(
        {
            "appTypes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppContextOut"])
    types["TimeOfDayIn"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "hours": t.integer().optional(),
            "seconds": t.integer().optional(),
            "minutes": t.integer().optional(),
        }
    ).named(renames["TimeOfDayIn"])
    types["TimeOfDayOut"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "hours": t.integer().optional(),
            "seconds": t.integer().optional(),
            "minutes": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeOfDayOut"])
    types["ClientIn"] = t.struct(
        {
            "status": t.string().optional(),
            "entityType": t.string().optional(),
            "clientName": t.string().optional(),
            "role": t.string().optional(),
            "partnerClientId": t.string().optional(),
            "visibleToSeller": t.boolean().optional(),
            "entityName": t.string().optional(),
            "entityId": t.string().optional(),
            "clientAccountId": t.string().optional(),
        }
    ).named(renames["ClientIn"])
    types["ClientOut"] = t.struct(
        {
            "status": t.string().optional(),
            "entityType": t.string().optional(),
            "clientName": t.string().optional(),
            "role": t.string().optional(),
            "partnerClientId": t.string().optional(),
            "visibleToSeller": t.boolean().optional(),
            "entityName": t.string().optional(),
            "entityId": t.string().optional(),
            "clientAccountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientOut"])
    types["ListPublisherProfilesResponseIn"] = t.struct(
        {
            "publisherProfiles": t.array(
                t.proxy(renames["PublisherProfileIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListPublisherProfilesResponseIn"])
    types["ListPublisherProfilesResponseOut"] = t.struct(
        {
            "publisherProfiles": t.array(
                t.proxy(renames["PublisherProfileOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPublisherProfilesResponseOut"])
    types["RelativeDateRangeIn"] = t.struct(
        {"durationDays": t.integer().optional(), "offsetDays": t.integer().optional()}
    ).named(renames["RelativeDateRangeIn"])
    types["RelativeDateRangeOut"] = t.struct(
        {
            "durationDays": t.integer().optional(),
            "offsetDays": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RelativeDateRangeOut"])
    types["CompleteSetupRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CompleteSetupRequestIn"]
    )
    types["CompleteSetupRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CompleteSetupRequestOut"])
    types["TimeIntervalIn"] = t.struct(
        {"startTime": t.string().optional(), "endTime": t.string().optional()}
    ).named(renames["TimeIntervalIn"])
    types["TimeIntervalOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeIntervalOut"])
    types["InventorySizeTargetingIn"] = t.struct(
        {
            "targetedInventorySizes": t.array(t.proxy(renames["AdSizeIn"])).optional(),
            "excludedInventorySizes": t.array(t.proxy(renames["AdSizeIn"])).optional(),
        }
    ).named(renames["InventorySizeTargetingIn"])
    types["InventorySizeTargetingOut"] = t.struct(
        {
            "targetedInventorySizes": t.array(t.proxy(renames["AdSizeOut"])).optional(),
            "excludedInventorySizes": t.array(t.proxy(renames["AdSizeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventorySizeTargetingOut"])
    types["CreativeDealAssociationIn"] = t.struct(
        {
            "accountId": t.string().optional(),
            "dealsId": t.string().optional(),
            "creativeId": t.string().optional(),
        }
    ).named(renames["CreativeDealAssociationIn"])
    types["CreativeDealAssociationOut"] = t.struct(
        {
            "accountId": t.string().optional(),
            "dealsId": t.string().optional(),
            "creativeId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeDealAssociationOut"])
    types["BidMetricsRowIn"] = t.struct(
        {
            "impressionsWon": t.proxy(renames["MetricValueIn"]).optional(),
            "bidsInAuction": t.proxy(renames["MetricValueIn"]).optional(),
            "viewableImpressions": t.proxy(renames["MetricValueIn"]).optional(),
            "measurableImpressions": t.proxy(renames["MetricValueIn"]).optional(),
            "rowDimensions": t.proxy(renames["RowDimensionsIn"]).optional(),
            "reachedQueries": t.proxy(renames["MetricValueIn"]).optional(),
            "bids": t.proxy(renames["MetricValueIn"]).optional(),
            "billedImpressions": t.proxy(renames["MetricValueIn"]).optional(),
        }
    ).named(renames["BidMetricsRowIn"])
    types["BidMetricsRowOut"] = t.struct(
        {
            "impressionsWon": t.proxy(renames["MetricValueOut"]).optional(),
            "bidsInAuction": t.proxy(renames["MetricValueOut"]).optional(),
            "viewableImpressions": t.proxy(renames["MetricValueOut"]).optional(),
            "measurableImpressions": t.proxy(renames["MetricValueOut"]).optional(),
            "rowDimensions": t.proxy(renames["RowDimensionsOut"]).optional(),
            "reachedQueries": t.proxy(renames["MetricValueOut"]).optional(),
            "bids": t.proxy(renames["MetricValueOut"]).optional(),
            "billedImpressions": t.proxy(renames["MetricValueOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BidMetricsRowOut"])
    types["CriteriaTargetingIn"] = t.struct(
        {
            "targetedCriteriaIds": t.array(t.string()).optional(),
            "excludedCriteriaIds": t.array(t.string()).optional(),
        }
    ).named(renames["CriteriaTargetingIn"])
    types["CriteriaTargetingOut"] = t.struct(
        {
            "targetedCriteriaIds": t.array(t.string()).optional(),
            "excludedCriteriaIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CriteriaTargetingOut"])
    types["ListBidResponsesWithoutBidsResponseIn"] = t.struct(
        {
            "bidResponseWithoutBidsStatusRows": t.array(
                t.proxy(renames["BidResponseWithoutBidsStatusRowIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListBidResponsesWithoutBidsResponseIn"])
    types["ListBidResponsesWithoutBidsResponseOut"] = t.struct(
        {
            "bidResponseWithoutBidsStatusRows": t.array(
                t.proxy(renames["BidResponseWithoutBidsStatusRowOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBidResponsesWithoutBidsResponseOut"])
    types["DayPartIn"] = t.struct(
        {
            "dayOfWeek": t.string().optional(),
            "endTime": t.proxy(renames["TimeOfDayIn"]).optional(),
            "startTime": t.proxy(renames["TimeOfDayIn"]).optional(),
        }
    ).named(renames["DayPartIn"])
    types["DayPartOut"] = t.struct(
        {
            "dayOfWeek": t.string().optional(),
            "endTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "startTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DayPartOut"])
    types["DealServingMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DealServingMetadataIn"]
    )
    types["DealServingMetadataOut"] = t.struct(
        {
            "dealPauseStatus": t.proxy(renames["DealPauseStatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DealServingMetadataOut"])
    types["DayPartTargetingIn"] = t.struct(
        {
            "dayParts": t.array(t.proxy(renames["DayPartIn"])).optional(),
            "timeZoneType": t.string().optional(),
        }
    ).named(renames["DayPartTargetingIn"])
    types["DayPartTargetingOut"] = t.struct(
        {
            "dayParts": t.array(t.proxy(renames["DayPartOut"])).optional(),
            "timeZoneType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DayPartTargetingOut"])
    types["PlacementTargetingIn"] = t.struct(
        {
            "urlTargeting": t.proxy(renames["UrlTargetingIn"]).optional(),
            "mobileApplicationTargeting": t.proxy(
                renames["MobileApplicationTargetingIn"]
            ).optional(),
        }
    ).named(renames["PlacementTargetingIn"])
    types["PlacementTargetingOut"] = t.struct(
        {
            "urlTargeting": t.proxy(renames["UrlTargetingOut"]).optional(),
            "mobileApplicationTargeting": t.proxy(
                renames["MobileApplicationTargetingOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlacementTargetingOut"])
    types["CorrectionIn"] = t.struct(
        {
            "type": t.string().optional(),
            "contexts": t.array(t.proxy(renames["ServingContextIn"])).optional(),
            "details": t.array(t.string()).optional(),
        }
    ).named(renames["CorrectionIn"])
    types["CorrectionOut"] = t.struct(
        {
            "type": t.string().optional(),
            "contexts": t.array(t.proxy(renames["ServingContextOut"])).optional(),
            "details": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CorrectionOut"])
    types["DealIn"] = t.struct(
        {
            "syndicationProduct": t.string().optional(),
            "availableEndTime": t.string().optional(),
            "targetingCriterion": t.array(
                t.proxy(renames["TargetingCriteriaIn"])
            ).optional(),
            "deliveryControl": t.proxy(renames["DeliveryControlIn"]).optional(),
            "description": t.string().optional(),
            "createProductId": t.string().optional(),
            "availableStartTime": t.string().optional(),
            "webPropertyCode": t.string().optional(),
            "dealTerms": t.proxy(renames["DealTermsIn"]).optional(),
            "buyerPrivateData": t.proxy(renames["PrivateDataIn"]).optional(),
            "displayName": t.string().optional(),
            "createProductRevision": t.string().optional(),
        }
    ).named(renames["DealIn"])
    types["DealOut"] = t.struct(
        {
            "syndicationProduct": t.string().optional(),
            "createTime": t.string().optional(),
            "targeting": t.proxy(renames["MarketplaceTargetingOut"]).optional(),
            "availableEndTime": t.string().optional(),
            "sellerContacts": t.array(
                t.proxy(renames["ContactInformationOut"])
            ).optional(),
            "targetingCriterion": t.array(
                t.proxy(renames["TargetingCriteriaOut"])
            ).optional(),
            "deliveryControl": t.proxy(renames["DeliveryControlOut"]).optional(),
            "description": t.string().optional(),
            "programmaticCreativeSource": t.string().optional(),
            "createProductId": t.string().optional(),
            "availableStartTime": t.string().optional(),
            "webPropertyCode": t.string().optional(),
            "dealTerms": t.proxy(renames["DealTermsOut"]).optional(),
            "buyerPrivateData": t.proxy(renames["PrivateDataOut"]).optional(),
            "dealId": t.string().optional(),
            "dealServingMetadata": t.proxy(
                renames["DealServingMetadataOut"]
            ).optional(),
            "displayName": t.string().optional(),
            "creativeSafeFrameCompatibility": t.string().optional(),
            "createProductRevision": t.string().optional(),
            "creativePreApprovalPolicy": t.string().optional(),
            "externalDealId": t.string().optional(),
            "updateTime": t.string().optional(),
            "isSetupComplete": t.boolean().optional(),
            "creativeRestrictions": t.proxy(
                renames["CreativeRestrictionsOut"]
            ).optional(),
            "proposalId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DealOut"])
    types["ListCreativeStatusBreakdownByCreativeResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "filteredBidCreativeRows": t.array(
                t.proxy(renames["FilteredBidCreativeRowIn"])
            ).optional(),
        }
    ).named(renames["ListCreativeStatusBreakdownByCreativeResponseIn"])
    types["ListCreativeStatusBreakdownByCreativeResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "filteredBidCreativeRows": t.array(
                t.proxy(renames["FilteredBidCreativeRowOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCreativeStatusBreakdownByCreativeResponseOut"])
    types["DisapprovalIn"] = t.struct(
        {"details": t.array(t.string()).optional(), "reason": t.string().optional()}
    ).named(renames["DisapprovalIn"])
    types["DisapprovalOut"] = t.struct(
        {
            "details": t.array(t.string()).optional(),
            "reason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DisapprovalOut"])
    types["AbsoluteDateRangeIn"] = t.struct(
        {
            "endDate": t.proxy(renames["DateIn"]).optional(),
            "startDate": t.proxy(renames["DateIn"]).optional(),
        }
    ).named(renames["AbsoluteDateRangeIn"])
    types["AbsoluteDateRangeOut"] = t.struct(
        {
            "endDate": t.proxy(renames["DateOut"]).optional(),
            "startDate": t.proxy(renames["DateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AbsoluteDateRangeOut"])
    types["StopWatchingCreativeRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["StopWatchingCreativeRequestIn"])
    types["StopWatchingCreativeRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StopWatchingCreativeRequestOut"])
    types["WatchCreativeRequestIn"] = t.struct({"topic": t.string().optional()}).named(
        renames["WatchCreativeRequestIn"]
    )
    types["WatchCreativeRequestOut"] = t.struct(
        {
            "topic": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WatchCreativeRequestOut"])
    types["ListClientUsersResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "users": t.array(t.proxy(renames["ClientUserIn"])).optional(),
        }
    ).named(renames["ListClientUsersResponseIn"])
    types["ListClientUsersResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "users": t.array(t.proxy(renames["ClientUserOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListClientUsersResponseOut"])
    types["VideoContentIn"] = t.struct(
        {"videoUrl": t.string().optional(), "videoVastXml": t.string().optional()}
    ).named(renames["VideoContentIn"])
    types["VideoContentOut"] = t.struct(
        {
            "videoUrl": t.string().optional(),
            "videoVastXml": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoContentOut"])
    types["PrivateDataIn"] = t.struct({"referenceId": t.string().optional()}).named(
        renames["PrivateDataIn"]
    )
    types["PrivateDataOut"] = t.struct(
        {
            "referenceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrivateDataOut"])
    types["ListImpressionMetricsResponseIn"] = t.struct(
        {
            "impressionMetricsRows": t.array(
                t.proxy(renames["ImpressionMetricsRowIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListImpressionMetricsResponseIn"])
    types["ListImpressionMetricsResponseOut"] = t.struct(
        {
            "impressionMetricsRows": t.array(
                t.proxy(renames["ImpressionMetricsRowOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListImpressionMetricsResponseOut"])
    types["SizeIn"] = t.struct(
        {"width": t.integer().optional(), "height": t.integer().optional()}
    ).named(renames["SizeIn"])
    types["SizeOut"] = t.struct(
        {
            "width": t.integer().optional(),
            "height": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SizeOut"])
    types["NonBillableWinningBidStatusRowIn"] = t.struct(
        {
            "status": t.string().optional(),
            "bidCount": t.proxy(renames["MetricValueIn"]).optional(),
            "rowDimensions": t.proxy(renames["RowDimensionsIn"]).optional(),
        }
    ).named(renames["NonBillableWinningBidStatusRowIn"])
    types["NonBillableWinningBidStatusRowOut"] = t.struct(
        {
            "status": t.string().optional(),
            "bidCount": t.proxy(renames["MetricValueOut"]).optional(),
            "rowDimensions": t.proxy(renames["RowDimensionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NonBillableWinningBidStatusRowOut"])
    types["NonGuaranteedFixedPriceTermsIn"] = t.struct(
        {"fixedPrices": t.array(t.proxy(renames["PricePerBuyerIn"])).optional()}
    ).named(renames["NonGuaranteedFixedPriceTermsIn"])
    types["NonGuaranteedFixedPriceTermsOut"] = t.struct(
        {
            "fixedPrices": t.array(t.proxy(renames["PricePerBuyerOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NonGuaranteedFixedPriceTermsOut"])
    types["FilteredBidCreativeRowIn"] = t.struct(
        {
            "rowDimensions": t.proxy(renames["RowDimensionsIn"]).optional(),
            "bidCount": t.proxy(renames["MetricValueIn"]).optional(),
            "creativeId": t.string().optional(),
        }
    ).named(renames["FilteredBidCreativeRowIn"])
    types["FilteredBidCreativeRowOut"] = t.struct(
        {
            "rowDimensions": t.proxy(renames["RowDimensionsOut"]).optional(),
            "bidCount": t.proxy(renames["MetricValueOut"]).optional(),
            "creativeId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilteredBidCreativeRowOut"])
    types["LocationContextIn"] = t.struct(
        {"geoCriteriaIds": t.array(t.integer()).optional()}
    ).named(renames["LocationContextIn"])
    types["LocationContextOut"] = t.struct(
        {
            "geoCriteriaIds": t.array(t.integer()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationContextOut"])
    types["BuyerIn"] = t.struct({"accountId": t.string().optional()}).named(
        renames["BuyerIn"]
    )
    types["BuyerOut"] = t.struct(
        {
            "accountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuyerOut"])
    types["AdTechnologyProvidersIn"] = t.struct(
        {
            "hasUnidentifiedProvider": t.boolean().optional(),
            "detectedProviderIds": t.array(t.string()).optional(),
        }
    ).named(renames["AdTechnologyProvidersIn"])
    types["AdTechnologyProvidersOut"] = t.struct(
        {
            "hasUnidentifiedProvider": t.boolean().optional(),
            "detectedProviderIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdTechnologyProvidersOut"])
    types["ServingRestrictionIn"] = t.struct(
        {
            "disapproval": t.proxy(renames["DisapprovalIn"]).optional(),
            "disapprovalReasons": t.array(t.proxy(renames["DisapprovalIn"])).optional(),
            "status": t.string().optional(),
            "contexts": t.array(t.proxy(renames["ServingContextIn"])).optional(),
        }
    ).named(renames["ServingRestrictionIn"])
    types["ServingRestrictionOut"] = t.struct(
        {
            "disapproval": t.proxy(renames["DisapprovalOut"]).optional(),
            "disapprovalReasons": t.array(
                t.proxy(renames["DisapprovalOut"])
            ).optional(),
            "status": t.string().optional(),
            "contexts": t.array(t.proxy(renames["ServingContextOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServingRestrictionOut"])
    types["PricePerBuyerIn"] = t.struct(
        {
            "buyer": t.proxy(renames["BuyerIn"]).optional(),
            "price": t.proxy(renames["PriceIn"]).optional(),
            "advertiserIds": t.array(t.string()).optional(),
        }
    ).named(renames["PricePerBuyerIn"])
    types["PricePerBuyerOut"] = t.struct(
        {
            "buyer": t.proxy(renames["BuyerOut"]).optional(),
            "price": t.proxy(renames["PriceOut"]).optional(),
            "advertiserIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PricePerBuyerOut"])
    types["CreativeSpecificationIn"] = t.struct(
        {
            "creativeCompanionSizes": t.array(t.proxy(renames["AdSizeIn"])).optional(),
            "creativeSize": t.proxy(renames["AdSizeIn"]).optional(),
        }
    ).named(renames["CreativeSpecificationIn"])
    types["CreativeSpecificationOut"] = t.struct(
        {
            "creativeCompanionSizes": t.array(t.proxy(renames["AdSizeOut"])).optional(),
            "creativeSize": t.proxy(renames["AdSizeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeSpecificationOut"])
    types["SecurityContextIn"] = t.struct(
        {"securities": t.array(t.string()).optional()}
    ).named(renames["SecurityContextIn"])
    types["SecurityContextOut"] = t.struct(
        {
            "securities": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecurityContextOut"])
    types["PlatformContextIn"] = t.struct(
        {"platforms": t.array(t.string()).optional()}
    ).named(renames["PlatformContextIn"])
    types["PlatformContextOut"] = t.struct(
        {
            "platforms": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlatformContextOut"])
    types["ImpressionMetricsRowIn"] = t.struct(
        {
            "inventoryMatches": t.proxy(renames["MetricValueIn"]).optional(),
            "successfulResponses": t.proxy(renames["MetricValueIn"]).optional(),
            "responsesWithBids": t.proxy(renames["MetricValueIn"]).optional(),
            "rowDimensions": t.proxy(renames["RowDimensionsIn"]).optional(),
            "availableImpressions": t.proxy(renames["MetricValueIn"]).optional(),
            "bidRequests": t.proxy(renames["MetricValueIn"]).optional(),
        }
    ).named(renames["ImpressionMetricsRowIn"])
    types["ImpressionMetricsRowOut"] = t.struct(
        {
            "inventoryMatches": t.proxy(renames["MetricValueOut"]).optional(),
            "successfulResponses": t.proxy(renames["MetricValueOut"]).optional(),
            "responsesWithBids": t.proxy(renames["MetricValueOut"]).optional(),
            "rowDimensions": t.proxy(renames["RowDimensionsOut"]).optional(),
            "availableImpressions": t.proxy(renames["MetricValueOut"]).optional(),
            "bidRequests": t.proxy(renames["MetricValueOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImpressionMetricsRowOut"])
    types["AddDealAssociationRequestIn"] = t.struct(
        {"association": t.proxy(renames["CreativeDealAssociationIn"]).optional()}
    ).named(renames["AddDealAssociationRequestIn"])
    types["AddDealAssociationRequestOut"] = t.struct(
        {
            "association": t.proxy(renames["CreativeDealAssociationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddDealAssociationRequestOut"])
    types["ListCreativeStatusBreakdownByDetailResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "detailType": t.string().optional(),
            "filteredBidDetailRows": t.array(
                t.proxy(renames["FilteredBidDetailRowIn"])
            ).optional(),
        }
    ).named(renames["ListCreativeStatusBreakdownByDetailResponseIn"])
    types["ListCreativeStatusBreakdownByDetailResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "detailType": t.string().optional(),
            "filteredBidDetailRows": t.array(
                t.proxy(renames["FilteredBidDetailRowOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCreativeStatusBreakdownByDetailResponseOut"])
    types["AcceptProposalRequestIn"] = t.struct(
        {"proposalRevision": t.string().optional()}
    ).named(renames["AcceptProposalRequestIn"])
    types["AcceptProposalRequestOut"] = t.struct(
        {
            "proposalRevision": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AcceptProposalRequestOut"])
    types["AdSizeIn"] = t.struct(
        {
            "sizeType": t.string().optional(),
            "width": t.string().optional(),
            "height": t.string().optional(),
        }
    ).named(renames["AdSizeIn"])
    types["AdSizeOut"] = t.struct(
        {
            "sizeType": t.string().optional(),
            "width": t.string().optional(),
            "height": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdSizeOut"])
    types["ListProductsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "products": t.array(t.proxy(renames["ProductIn"])).optional(),
        }
    ).named(renames["ListProductsResponseIn"])
    types["ListProductsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "products": t.array(t.proxy(renames["ProductOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListProductsResponseOut"])
    types["TargetingCriteriaIn"] = t.struct(
        {
            "key": t.string().optional(),
            "exclusions": t.array(t.proxy(renames["TargetingValueIn"])).optional(),
            "inclusions": t.array(t.proxy(renames["TargetingValueIn"])).optional(),
        }
    ).named(renames["TargetingCriteriaIn"])
    types["TargetingCriteriaOut"] = t.struct(
        {
            "key": t.string().optional(),
            "exclusions": t.array(t.proxy(renames["TargetingValueOut"])).optional(),
            "inclusions": t.array(t.proxy(renames["TargetingValueOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetingCriteriaOut"])
    types["ProductIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "targetingCriterion": t.array(
                t.proxy(renames["TargetingCriteriaIn"])
            ).optional(),
            "webPropertyCode": t.string().optional(),
            "availableStartTime": t.string().optional(),
            "productRevision": t.string().optional(),
            "hasCreatorSignedOff": t.boolean().optional(),
            "createTime": t.string().optional(),
            "productId": t.string().optional(),
            "terms": t.proxy(renames["DealTermsIn"]).optional(),
            "creatorContacts": t.array(
                t.proxy(renames["ContactInformationIn"])
            ).optional(),
            "updateTime": t.string().optional(),
            "syndicationProduct": t.string().optional(),
            "seller": t.proxy(renames["SellerIn"]).optional(),
            "availableEndTime": t.string().optional(),
            "publisherProfileId": t.string().optional(),
        }
    ).named(renames["ProductIn"])
    types["ProductOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "targetingCriterion": t.array(
                t.proxy(renames["TargetingCriteriaOut"])
            ).optional(),
            "webPropertyCode": t.string().optional(),
            "availableStartTime": t.string().optional(),
            "productRevision": t.string().optional(),
            "hasCreatorSignedOff": t.boolean().optional(),
            "createTime": t.string().optional(),
            "productId": t.string().optional(),
            "terms": t.proxy(renames["DealTermsOut"]).optional(),
            "creatorContacts": t.array(
                t.proxy(renames["ContactInformationOut"])
            ).optional(),
            "updateTime": t.string().optional(),
            "syndicationProduct": t.string().optional(),
            "seller": t.proxy(renames["SellerOut"]).optional(),
            "availableEndTime": t.string().optional(),
            "publisherProfileId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductOut"])
    types["ListBidResponseErrorsResponseIn"] = t.struct(
        {
            "calloutStatusRows": t.array(
                t.proxy(renames["CalloutStatusRowIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListBidResponseErrorsResponseIn"])
    types["ListBidResponseErrorsResponseOut"] = t.struct(
        {
            "calloutStatusRows": t.array(
                t.proxy(renames["CalloutStatusRowOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBidResponseErrorsResponseOut"])
    types["FirstPartyMobileApplicationTargetingIn"] = t.struct(
        {
            "excludedAppIds": t.array(t.string()).optional(),
            "targetedAppIds": t.array(t.string()).optional(),
        }
    ).named(renames["FirstPartyMobileApplicationTargetingIn"])
    types["FirstPartyMobileApplicationTargetingOut"] = t.struct(
        {
            "excludedAppIds": t.array(t.string()).optional(),
            "targetedAppIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FirstPartyMobileApplicationTargetingOut"])
    types["DateIn"] = t.struct(
        {
            "month": t.integer().optional(),
            "year": t.integer().optional(),
            "day": t.integer().optional(),
        }
    ).named(renames["DateIn"])
    types["DateOut"] = t.struct(
        {
            "month": t.integer().optional(),
            "year": t.integer().optional(),
            "day": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
    types["CreativeSizeIn"] = t.struct(
        {
            "nativeTemplate": t.string().optional(),
            "companionSizes": t.array(t.proxy(renames["SizeIn"])).optional(),
            "creativeSizeType": t.string().optional(),
            "allowedFormats": t.array(t.string()).optional(),
            "skippableAdType": t.string().optional(),
            "size": t.proxy(renames["SizeIn"]).optional(),
        }
    ).named(renames["CreativeSizeIn"])
    types["CreativeSizeOut"] = t.struct(
        {
            "nativeTemplate": t.string().optional(),
            "companionSizes": t.array(t.proxy(renames["SizeOut"])).optional(),
            "creativeSizeType": t.string().optional(),
            "allowedFormats": t.array(t.string()).optional(),
            "skippableAdType": t.string().optional(),
            "size": t.proxy(renames["SizeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeSizeOut"])
    types["ListCreativesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "creatives": t.array(t.proxy(renames["CreativeIn"])).optional(),
        }
    ).named(renames["ListCreativesResponseIn"])
    types["ListCreativesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "creatives": t.array(t.proxy(renames["CreativeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCreativesResponseOut"])
    types["BidResponseWithoutBidsStatusRowIn"] = t.struct(
        {
            "rowDimensions": t.proxy(renames["RowDimensionsIn"]).optional(),
            "impressionCount": t.proxy(renames["MetricValueIn"]).optional(),
            "status": t.string().optional(),
        }
    ).named(renames["BidResponseWithoutBidsStatusRowIn"])
    types["BidResponseWithoutBidsStatusRowOut"] = t.struct(
        {
            "rowDimensions": t.proxy(renames["RowDimensionsOut"]).optional(),
            "impressionCount": t.proxy(renames["MetricValueOut"]).optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BidResponseWithoutBidsStatusRowOut"])
    types["ClientUserInvitationIn"] = t.struct(
        {
            "invitationId": t.string().optional(),
            "email": t.string().optional(),
            "clientAccountId": t.string().optional(),
        }
    ).named(renames["ClientUserInvitationIn"])
    types["ClientUserInvitationOut"] = t.struct(
        {
            "invitationId": t.string().optional(),
            "email": t.string().optional(),
            "clientAccountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientUserInvitationOut"])
    types["MarketplaceTargetingIn"] = t.struct(
        {
            "placementTargeting": t.proxy(renames["PlacementTargetingIn"]).optional(),
            "geoTargeting": t.proxy(renames["CriteriaTargetingIn"]).optional(),
            "videoTargeting": t.proxy(renames["VideoTargetingIn"]).optional(),
            "technologyTargeting": t.proxy(renames["TechnologyTargetingIn"]).optional(),
            "inventorySizeTargeting": t.proxy(
                renames["InventorySizeTargetingIn"]
            ).optional(),
        }
    ).named(renames["MarketplaceTargetingIn"])
    types["MarketplaceTargetingOut"] = t.struct(
        {
            "placementTargeting": t.proxy(renames["PlacementTargetingOut"]).optional(),
            "geoTargeting": t.proxy(renames["CriteriaTargetingOut"]).optional(),
            "videoTargeting": t.proxy(renames["VideoTargetingOut"]).optional(),
            "technologyTargeting": t.proxy(
                renames["TechnologyTargetingOut"]
            ).optional(),
            "inventorySizeTargeting": t.proxy(
                renames["InventorySizeTargetingOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MarketplaceTargetingOut"])
    types["MetricValueIn"] = t.struct(
        {"variance": t.string().optional(), "value": t.string().optional()}
    ).named(renames["MetricValueIn"])
    types["MetricValueOut"] = t.struct(
        {
            "variance": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricValueOut"])
    types["CreativeRestrictionsIn"] = t.struct(
        {
            "creativeFormat": t.string().optional(),
            "skippableAdType": t.string().optional(),
            "creativeSpecifications": t.array(
                t.proxy(renames["CreativeSpecificationIn"])
            ),
        }
    ).named(renames["CreativeRestrictionsIn"])
    types["CreativeRestrictionsOut"] = t.struct(
        {
            "creativeFormat": t.string().optional(),
            "skippableAdType": t.string().optional(),
            "creativeSpecifications": t.array(
                t.proxy(renames["CreativeSpecificationOut"])
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeRestrictionsOut"])
    types["GuaranteedFixedPriceTermsIn"] = t.struct(
        {
            "fixedPrices": t.array(t.proxy(renames["PricePerBuyerIn"])).optional(),
            "reservationType": t.string().optional(),
            "guaranteedImpressions": t.string().optional(),
            "guaranteedLooks": t.string().optional(),
            "impressionCap": t.string().optional(),
            "percentShareOfVoice": t.string().optional(),
            "minimumDailyLooks": t.string().optional(),
        }
    ).named(renames["GuaranteedFixedPriceTermsIn"])
    types["GuaranteedFixedPriceTermsOut"] = t.struct(
        {
            "fixedPrices": t.array(t.proxy(renames["PricePerBuyerOut"])).optional(),
            "reservationType": t.string().optional(),
            "guaranteedImpressions": t.string().optional(),
            "guaranteedLooks": t.string().optional(),
            "impressionCap": t.string().optional(),
            "percentShareOfVoice": t.string().optional(),
            "minimumDailyLooks": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GuaranteedFixedPriceTermsOut"])
    types["ListNonBillableWinningBidsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "nonBillableWinningBidStatusRows": t.array(
                t.proxy(renames["NonBillableWinningBidStatusRowIn"])
            ).optional(),
        }
    ).named(renames["ListNonBillableWinningBidsResponseIn"])
    types["ListNonBillableWinningBidsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "nonBillableWinningBidStatusRows": t.array(
                t.proxy(renames["NonBillableWinningBidStatusRowOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListNonBillableWinningBidsResponseOut"])
    types["SellerIn"] = t.struct({"accountId": t.string().optional()}).named(
        renames["SellerIn"]
    )
    types["SellerOut"] = t.struct(
        {
            "subAccountId": t.string().optional(),
            "accountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SellerOut"])
    types["CreativeStatusRowIn"] = t.struct(
        {
            "rowDimensions": t.proxy(renames["RowDimensionsIn"]).optional(),
            "bidCount": t.proxy(renames["MetricValueIn"]).optional(),
            "creativeStatusId": t.integer().optional(),
        }
    ).named(renames["CreativeStatusRowIn"])
    types["CreativeStatusRowOut"] = t.struct(
        {
            "rowDimensions": t.proxy(renames["RowDimensionsOut"]).optional(),
            "bidCount": t.proxy(renames["MetricValueOut"]).optional(),
            "creativeStatusId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeStatusRowOut"])
    types["RowDimensionsIn"] = t.struct(
        {
            "timeInterval": t.proxy(renames["TimeIntervalIn"]).optional(),
            "publisherIdentifier": t.string().optional(),
        }
    ).named(renames["RowDimensionsIn"])
    types["RowDimensionsOut"] = t.struct(
        {
            "timeInterval": t.proxy(renames["TimeIntervalOut"]).optional(),
            "publisherIdentifier": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RowDimensionsOut"])
    types["ServingContextIn"] = t.struct(
        {
            "all": t.string().optional(),
            "auctionType": t.proxy(renames["AuctionContextIn"]).optional(),
            "platform": t.proxy(renames["PlatformContextIn"]).optional(),
            "location": t.proxy(renames["LocationContextIn"]).optional(),
            "securityType": t.proxy(renames["SecurityContextIn"]).optional(),
            "appType": t.proxy(renames["AppContextIn"]).optional(),
        }
    ).named(renames["ServingContextIn"])
    types["ServingContextOut"] = t.struct(
        {
            "all": t.string().optional(),
            "auctionType": t.proxy(renames["AuctionContextOut"]).optional(),
            "platform": t.proxy(renames["PlatformContextOut"]).optional(),
            "location": t.proxy(renames["LocationContextOut"]).optional(),
            "securityType": t.proxy(renames["SecurityContextOut"]).optional(),
            "appType": t.proxy(renames["AppContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServingContextOut"])
    types["ClientUserIn"] = t.struct(
        {
            "email": t.string().optional(),
            "status": t.string().optional(),
            "clientAccountId": t.string().optional(),
            "userId": t.string().optional(),
        }
    ).named(renames["ClientUserIn"])
    types["ClientUserOut"] = t.struct(
        {
            "email": t.string().optional(),
            "status": t.string().optional(),
            "clientAccountId": t.string().optional(),
            "userId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientUserOut"])
    types["ImageIn"] = t.struct(
        {
            "url": t.string().optional(),
            "width": t.integer().optional(),
            "height": t.integer().optional(),
        }
    ).named(renames["ImageIn"])
    types["ImageOut"] = t.struct(
        {
            "url": t.string().optional(),
            "width": t.integer().optional(),
            "height": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageOut"])
    types["RemoveDealAssociationRequestIn"] = t.struct(
        {"association": t.proxy(renames["CreativeDealAssociationIn"]).optional()}
    ).named(renames["RemoveDealAssociationRequestIn"])
    types["RemoveDealAssociationRequestOut"] = t.struct(
        {
            "association": t.proxy(renames["CreativeDealAssociationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveDealAssociationRequestOut"])
    types["DealPauseStatusIn"] = t.struct(
        {
            "sellerPauseReason": t.string().optional(),
            "firstPausedBy": t.string().optional(),
            "hasBuyerPaused": t.boolean().optional(),
            "buyerPauseReason": t.string().optional(),
            "hasSellerPaused": t.boolean().optional(),
        }
    ).named(renames["DealPauseStatusIn"])
    types["DealPauseStatusOut"] = t.struct(
        {
            "sellerPauseReason": t.string().optional(),
            "firstPausedBy": t.string().optional(),
            "hasBuyerPaused": t.boolean().optional(),
            "buyerPauseReason": t.string().optional(),
            "hasSellerPaused": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DealPauseStatusOut"])
    types["PauseProposalDealsRequestIn"] = t.struct(
        {
            "externalDealIds": t.array(t.string()).optional(),
            "reason": t.string().optional(),
        }
    ).named(renames["PauseProposalDealsRequestIn"])
    types["PauseProposalDealsRequestOut"] = t.struct(
        {
            "externalDealIds": t.array(t.string()).optional(),
            "reason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PauseProposalDealsRequestOut"])
    types["ProposalIn"] = t.struct(
        {
            "buyerPrivateData": t.proxy(renames["PrivateDataIn"]).optional(),
            "seller": t.proxy(renames["SellerIn"]).optional(),
            "deals": t.array(t.proxy(renames["DealIn"])).optional(),
            "displayName": t.string().optional(),
            "buyerContacts": t.array(
                t.proxy(renames["ContactInformationIn"])
            ).optional(),
            "buyer": t.proxy(renames["BuyerIn"]).optional(),
        }
    ).named(renames["ProposalIn"])
    types["ProposalOut"] = t.struct(
        {
            "sellerContacts": t.array(
                t.proxy(renames["ContactInformationOut"])
            ).optional(),
            "updateTime": t.string().optional(),
            "lastUpdaterOrCommentorRole": t.string().optional(),
            "buyerPrivateData": t.proxy(renames["PrivateDataOut"]).optional(),
            "isSetupComplete": t.boolean().optional(),
            "termsAndConditions": t.string().optional(),
            "proposalId": t.string().optional(),
            "isRenegotiating": t.boolean().optional(),
            "seller": t.proxy(renames["SellerOut"]).optional(),
            "billedBuyer": t.proxy(renames["BuyerOut"]).optional(),
            "deals": t.array(t.proxy(renames["DealOut"])).optional(),
            "proposalRevision": t.string().optional(),
            "privateAuctionId": t.string().optional(),
            "notes": t.array(t.proxy(renames["NoteOut"])).optional(),
            "originatorRole": t.string().optional(),
            "displayName": t.string().optional(),
            "buyerContacts": t.array(
                t.proxy(renames["ContactInformationOut"])
            ).optional(),
            "buyer": t.proxy(renames["BuyerOut"]).optional(),
            "proposalState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProposalOut"])

    functions = {}
    functions["biddersAccountsFilterSetsDelete"] = adexchangebuyer2.get(
        "v2beta1/{ownerName}/filterSets",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "ownerName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFilterSetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersAccountsFilterSetsGet"] = adexchangebuyer2.get(
        "v2beta1/{ownerName}/filterSets",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "ownerName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFilterSetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersAccountsFilterSetsCreate"] = adexchangebuyer2.get(
        "v2beta1/{ownerName}/filterSets",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "ownerName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFilterSetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersAccountsFilterSetsList"] = adexchangebuyer2.get(
        "v2beta1/{ownerName}/filterSets",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "ownerName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFilterSetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersAccountsFilterSetsBidResponseErrorsList"] = adexchangebuyer2.get(
        "v2beta1/{filterSetName}/bidResponseErrors",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filterSetName": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBidResponseErrorsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "biddersAccountsFilterSetsNonBillableWinningBidsList"
    ] = adexchangebuyer2.get(
        "v2beta1/{filterSetName}/nonBillableWinningBids",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filterSetName": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListNonBillableWinningBidsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersAccountsFilterSetsLosingBidsList"] = adexchangebuyer2.get(
        "v2beta1/{filterSetName}/losingBids",
        t.struct(
            {
                "filterSetName": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLosingBidsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "biddersAccountsFilterSetsBidResponsesWithoutBidsList"
    ] = adexchangebuyer2.get(
        "v2beta1/{filterSetName}/bidResponsesWithoutBids",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filterSetName": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBidResponsesWithoutBidsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersAccountsFilterSetsFilteredBidsList"] = adexchangebuyer2.get(
        "v2beta1/{filterSetName}/filteredBids",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filterSetName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFilteredBidsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "biddersAccountsFilterSetsFilteredBidsDetailsList"
    ] = adexchangebuyer2.get(
        "v2beta1/{filterSetName}/filteredBids/{creativeStatusId}/details",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "creativeStatusId": t.integer().optional(),
                "filterSetName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCreativeStatusBreakdownByDetailResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "biddersAccountsFilterSetsFilteredBidsCreativesList"
    ] = adexchangebuyer2.get(
        "v2beta1/{filterSetName}/filteredBids/{creativeStatusId}/creatives",
        t.struct(
            {
                "creativeStatusId": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filterSetName": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCreativeStatusBreakdownByCreativeResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersAccountsFilterSetsBidMetricsList"] = adexchangebuyer2.get(
        "v2beta1/{filterSetName}/bidMetrics",
        t.struct(
            {
                "filterSetName": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBidMetricsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersAccountsFilterSetsImpressionMetricsList"] = adexchangebuyer2.get(
        "v2beta1/{filterSetName}/impressionMetrics",
        t.struct(
            {
                "filterSetName": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListImpressionMetricsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "biddersAccountsFilterSetsFilteredBidRequestsList"
    ] = adexchangebuyer2.get(
        "v2beta1/{filterSetName}/filteredBidRequests",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filterSetName": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFilteredBidRequestsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersFilterSetsCreate"] = adexchangebuyer2.get(
        "v2beta1/{ownerName}/filterSets",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "ownerName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFilterSetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersFilterSetsDelete"] = adexchangebuyer2.get(
        "v2beta1/{ownerName}/filterSets",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "ownerName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFilterSetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersFilterSetsGet"] = adexchangebuyer2.get(
        "v2beta1/{ownerName}/filterSets",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "ownerName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFilterSetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersFilterSetsList"] = adexchangebuyer2.get(
        "v2beta1/{ownerName}/filterSets",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "ownerName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFilterSetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersFilterSetsLosingBidsList"] = adexchangebuyer2.get(
        "v2beta1/{filterSetName}/losingBids",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filterSetName": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLosingBidsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersFilterSetsImpressionMetricsList"] = adexchangebuyer2.get(
        "v2beta1/{filterSetName}/impressionMetrics",
        t.struct(
            {
                "filterSetName": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListImpressionMetricsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersFilterSetsFilteredBidRequestsList"] = adexchangebuyer2.get(
        "v2beta1/{filterSetName}/filteredBidRequests",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filterSetName": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFilteredBidRequestsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersFilterSetsBidResponseErrorsList"] = adexchangebuyer2.get(
        "v2beta1/{filterSetName}/bidResponseErrors",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filterSetName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBidResponseErrorsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersFilterSetsBidResponsesWithoutBidsList"] = adexchangebuyer2.get(
        "v2beta1/{filterSetName}/bidResponsesWithoutBids",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filterSetName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBidResponsesWithoutBidsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersFilterSetsNonBillableWinningBidsList"] = adexchangebuyer2.get(
        "v2beta1/{filterSetName}/nonBillableWinningBids",
        t.struct(
            {
                "filterSetName": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListNonBillableWinningBidsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersFilterSetsBidMetricsList"] = adexchangebuyer2.get(
        "v2beta1/{filterSetName}/bidMetrics",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filterSetName": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBidMetricsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersFilterSetsFilteredBidsList"] = adexchangebuyer2.get(
        "v2beta1/{filterSetName}/filteredBids",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filterSetName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFilteredBidsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersFilterSetsFilteredBidsCreativesList"] = adexchangebuyer2.get(
        "v2beta1/{filterSetName}/filteredBids/{creativeStatusId}/creatives",
        t.struct(
            {
                "creativeStatusId": t.integer().optional(),
                "pageSize": t.integer().optional(),
                "filterSetName": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCreativeStatusBreakdownByCreativeResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersFilterSetsFilteredBidsDetailsList"] = adexchangebuyer2.get(
        "v2beta1/{filterSetName}/filteredBids/{creativeStatusId}/details",
        t.struct(
            {
                "filterSetName": t.string().optional(),
                "creativeStatusId": t.integer().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCreativeStatusBreakdownByDetailResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsFinalizedProposalsPause"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/finalizedProposals",
        t.struct(
            {
                "filterSyntax": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "accountId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListProposalsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsFinalizedProposalsResume"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/finalizedProposals",
        t.struct(
            {
                "filterSyntax": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "accountId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListProposalsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsFinalizedProposalsList"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/finalizedProposals",
        t.struct(
            {
                "filterSyntax": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "accountId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListProposalsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCreativesList"] = adexchangebuyer2.post(
        "v2beta1/accounts/{accountId}/creatives/{creativeId}:stopWatching",
        t.struct(
            {
                "creativeId": t.string().optional(),
                "accountId": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCreativesUpdate"] = adexchangebuyer2.post(
        "v2beta1/accounts/{accountId}/creatives/{creativeId}:stopWatching",
        t.struct(
            {
                "creativeId": t.string().optional(),
                "accountId": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCreativesWatch"] = adexchangebuyer2.post(
        "v2beta1/accounts/{accountId}/creatives/{creativeId}:stopWatching",
        t.struct(
            {
                "creativeId": t.string().optional(),
                "accountId": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCreativesCreate"] = adexchangebuyer2.post(
        "v2beta1/accounts/{accountId}/creatives/{creativeId}:stopWatching",
        t.struct(
            {
                "creativeId": t.string().optional(),
                "accountId": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCreativesGet"] = adexchangebuyer2.post(
        "v2beta1/accounts/{accountId}/creatives/{creativeId}:stopWatching",
        t.struct(
            {
                "creativeId": t.string().optional(),
                "accountId": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCreativesStopWatching"] = adexchangebuyer2.post(
        "v2beta1/accounts/{accountId}/creatives/{creativeId}:stopWatching",
        t.struct(
            {
                "creativeId": t.string().optional(),
                "accountId": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCreativesDealAssociationsAdd"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/creatives/{creativeId}/dealAssociations",
        t.struct(
            {
                "creativeId": t.string().optional(),
                "query": t.string().optional(),
                "accountId": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDealAssociationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCreativesDealAssociationsRemove"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/creatives/{creativeId}/dealAssociations",
        t.struct(
            {
                "creativeId": t.string().optional(),
                "query": t.string().optional(),
                "accountId": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDealAssociationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCreativesDealAssociationsList"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/creatives/{creativeId}/dealAssociations",
        t.struct(
            {
                "creativeId": t.string().optional(),
                "query": t.string().optional(),
                "accountId": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDealAssociationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsClientsUpdate"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/clients",
        t.struct(
            {
                "accountId": t.string().optional(),
                "partnerClientId": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListClientsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsClientsGet"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/clients",
        t.struct(
            {
                "accountId": t.string().optional(),
                "partnerClientId": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListClientsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsClientsCreate"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/clients",
        t.struct(
            {
                "accountId": t.string().optional(),
                "partnerClientId": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListClientsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsClientsList"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/clients",
        t.struct(
            {
                "accountId": t.string().optional(),
                "partnerClientId": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListClientsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsClientsUsersUpdate"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/clients/{clientAccountId}/users/{userId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "clientAccountId": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClientUserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsClientsUsersList"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/clients/{clientAccountId}/users/{userId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "clientAccountId": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClientUserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsClientsUsersGet"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/clients/{clientAccountId}/users/{userId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "clientAccountId": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClientUserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsClientsInvitationsList"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/clients/{clientAccountId}/invitations/{invitationId}",
        t.struct(
            {
                "clientAccountId": t.string().optional(),
                "accountId": t.string().optional(),
                "invitationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClientUserInvitationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsClientsInvitationsCreate"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/clients/{clientAccountId}/invitations/{invitationId}",
        t.struct(
            {
                "clientAccountId": t.string().optional(),
                "accountId": t.string().optional(),
                "invitationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClientUserInvitationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsClientsInvitationsGet"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/clients/{clientAccountId}/invitations/{invitationId}",
        t.struct(
            {
                "clientAccountId": t.string().optional(),
                "accountId": t.string().optional(),
                "invitationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClientUserInvitationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsPublisherProfilesList"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/publisherProfiles/{publisherProfileId}",
        t.struct(
            {
                "publisherProfileId": t.string().optional(),
                "accountId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PublisherProfileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsPublisherProfilesGet"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/publisherProfiles/{publisherProfileId}",
        t.struct(
            {
                "publisherProfileId": t.string().optional(),
                "accountId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PublisherProfileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsProductsList"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/products/{productId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "productId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsProductsGet"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/products/{productId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "productId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsProposalsList"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/proposals/{proposalId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "proposalId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProposalOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsProposalsAccept"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/proposals/{proposalId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "proposalId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProposalOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsProposalsCompleteSetup"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/proposals/{proposalId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "proposalId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProposalOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsProposalsUpdate"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/proposals/{proposalId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "proposalId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProposalOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsProposalsCreate"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/proposals/{proposalId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "proposalId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProposalOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsProposalsPause"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/proposals/{proposalId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "proposalId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProposalOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsProposalsResume"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/proposals/{proposalId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "proposalId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProposalOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsProposalsCancelNegotiation"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/proposals/{proposalId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "proposalId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProposalOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsProposalsAddNote"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/proposals/{proposalId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "proposalId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProposalOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsProposalsGet"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/proposals/{proposalId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "proposalId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProposalOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="adexchangebuyer2",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
