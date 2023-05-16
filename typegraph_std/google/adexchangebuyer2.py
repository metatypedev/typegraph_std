from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_adexchangebuyer2() -> Import:
    adexchangebuyer2 = HTTPRuntime("https://adexchangebuyer.googleapis.com/")

    renames = {
        "ErrorResponse": "_adexchangebuyer2_1_ErrorResponse",
        "ListProductsResponseIn": "_adexchangebuyer2_2_ListProductsResponseIn",
        "ListProductsResponseOut": "_adexchangebuyer2_3_ListProductsResponseOut",
        "ListPublisherProfilesResponseIn": "_adexchangebuyer2_4_ListPublisherProfilesResponseIn",
        "ListPublisherProfilesResponseOut": "_adexchangebuyer2_5_ListPublisherProfilesResponseOut",
        "ListFilteredBidRequestsResponseIn": "_adexchangebuyer2_6_ListFilteredBidRequestsResponseIn",
        "ListFilteredBidRequestsResponseOut": "_adexchangebuyer2_7_ListFilteredBidRequestsResponseOut",
        "CalloutStatusRowIn": "_adexchangebuyer2_8_CalloutStatusRowIn",
        "CalloutStatusRowOut": "_adexchangebuyer2_9_CalloutStatusRowOut",
        "BuyerIn": "_adexchangebuyer2_10_BuyerIn",
        "BuyerOut": "_adexchangebuyer2_11_BuyerOut",
        "TargetingCriteriaIn": "_adexchangebuyer2_12_TargetingCriteriaIn",
        "TargetingCriteriaOut": "_adexchangebuyer2_13_TargetingCriteriaOut",
        "UrlTargetingIn": "_adexchangebuyer2_14_UrlTargetingIn",
        "UrlTargetingOut": "_adexchangebuyer2_15_UrlTargetingOut",
        "ListFilterSetsResponseIn": "_adexchangebuyer2_16_ListFilterSetsResponseIn",
        "ListFilterSetsResponseOut": "_adexchangebuyer2_17_ListFilterSetsResponseOut",
        "TimeOfDayIn": "_adexchangebuyer2_18_TimeOfDayIn",
        "TimeOfDayOut": "_adexchangebuyer2_19_TimeOfDayOut",
        "FilteredBidDetailRowIn": "_adexchangebuyer2_20_FilteredBidDetailRowIn",
        "FilteredBidDetailRowOut": "_adexchangebuyer2_21_FilteredBidDetailRowOut",
        "CompleteSetupRequestIn": "_adexchangebuyer2_22_CompleteSetupRequestIn",
        "CompleteSetupRequestOut": "_adexchangebuyer2_23_CompleteSetupRequestOut",
        "ListProposalsResponseIn": "_adexchangebuyer2_24_ListProposalsResponseIn",
        "ListProposalsResponseOut": "_adexchangebuyer2_25_ListProposalsResponseOut",
        "TargetingValueIn": "_adexchangebuyer2_26_TargetingValueIn",
        "TargetingValueOut": "_adexchangebuyer2_27_TargetingValueOut",
        "DisapprovalIn": "_adexchangebuyer2_28_DisapprovalIn",
        "DisapprovalOut": "_adexchangebuyer2_29_DisapprovalOut",
        "SecurityContextIn": "_adexchangebuyer2_30_SecurityContextIn",
        "SecurityContextOut": "_adexchangebuyer2_31_SecurityContextOut",
        "MobileApplicationTargetingIn": "_adexchangebuyer2_32_MobileApplicationTargetingIn",
        "MobileApplicationTargetingOut": "_adexchangebuyer2_33_MobileApplicationTargetingOut",
        "CreativeSpecificationIn": "_adexchangebuyer2_34_CreativeSpecificationIn",
        "CreativeSpecificationOut": "_adexchangebuyer2_35_CreativeSpecificationOut",
        "RowDimensionsIn": "_adexchangebuyer2_36_RowDimensionsIn",
        "RowDimensionsOut": "_adexchangebuyer2_37_RowDimensionsOut",
        "ListCreativeStatusBreakdownByDetailResponseIn": "_adexchangebuyer2_38_ListCreativeStatusBreakdownByDetailResponseIn",
        "ListCreativeStatusBreakdownByDetailResponseOut": "_adexchangebuyer2_39_ListCreativeStatusBreakdownByDetailResponseOut",
        "PricePerBuyerIn": "_adexchangebuyer2_40_PricePerBuyerIn",
        "PricePerBuyerOut": "_adexchangebuyer2_41_PricePerBuyerOut",
        "DayPartIn": "_adexchangebuyer2_42_DayPartIn",
        "DayPartOut": "_adexchangebuyer2_43_DayPartOut",
        "VideoContentIn": "_adexchangebuyer2_44_VideoContentIn",
        "VideoContentOut": "_adexchangebuyer2_45_VideoContentOut",
        "ImpressionMetricsRowIn": "_adexchangebuyer2_46_ImpressionMetricsRowIn",
        "ImpressionMetricsRowOut": "_adexchangebuyer2_47_ImpressionMetricsRowOut",
        "DayPartTargetingIn": "_adexchangebuyer2_48_DayPartTargetingIn",
        "DayPartTargetingOut": "_adexchangebuyer2_49_DayPartTargetingOut",
        "FilterSetIn": "_adexchangebuyer2_50_FilterSetIn",
        "FilterSetOut": "_adexchangebuyer2_51_FilterSetOut",
        "ResumeProposalRequestIn": "_adexchangebuyer2_52_ResumeProposalRequestIn",
        "ResumeProposalRequestOut": "_adexchangebuyer2_53_ResumeProposalRequestOut",
        "NativeContentIn": "_adexchangebuyer2_54_NativeContentIn",
        "NativeContentOut": "_adexchangebuyer2_55_NativeContentOut",
        "PauseProposalDealsRequestIn": "_adexchangebuyer2_56_PauseProposalDealsRequestIn",
        "PauseProposalDealsRequestOut": "_adexchangebuyer2_57_PauseProposalDealsRequestOut",
        "CorrectionIn": "_adexchangebuyer2_58_CorrectionIn",
        "CorrectionOut": "_adexchangebuyer2_59_CorrectionOut",
        "MarketplaceTargetingIn": "_adexchangebuyer2_60_MarketplaceTargetingIn",
        "MarketplaceTargetingOut": "_adexchangebuyer2_61_MarketplaceTargetingOut",
        "CreativeStatusRowIn": "_adexchangebuyer2_62_CreativeStatusRowIn",
        "CreativeStatusRowOut": "_adexchangebuyer2_63_CreativeStatusRowOut",
        "RelativeDateRangeIn": "_adexchangebuyer2_64_RelativeDateRangeIn",
        "RelativeDateRangeOut": "_adexchangebuyer2_65_RelativeDateRangeOut",
        "ResumeProposalDealsRequestIn": "_adexchangebuyer2_66_ResumeProposalDealsRequestIn",
        "ResumeProposalDealsRequestOut": "_adexchangebuyer2_67_ResumeProposalDealsRequestOut",
        "PrivateDataIn": "_adexchangebuyer2_68_PrivateDataIn",
        "PrivateDataOut": "_adexchangebuyer2_69_PrivateDataOut",
        "FirstPartyMobileApplicationTargetingIn": "_adexchangebuyer2_70_FirstPartyMobileApplicationTargetingIn",
        "FirstPartyMobileApplicationTargetingOut": "_adexchangebuyer2_71_FirstPartyMobileApplicationTargetingOut",
        "ServingRestrictionIn": "_adexchangebuyer2_72_ServingRestrictionIn",
        "ServingRestrictionOut": "_adexchangebuyer2_73_ServingRestrictionOut",
        "NoteIn": "_adexchangebuyer2_74_NoteIn",
        "NoteOut": "_adexchangebuyer2_75_NoteOut",
        "ClientUserInvitationIn": "_adexchangebuyer2_76_ClientUserInvitationIn",
        "ClientUserInvitationOut": "_adexchangebuyer2_77_ClientUserInvitationOut",
        "PriceIn": "_adexchangebuyer2_78_PriceIn",
        "PriceOut": "_adexchangebuyer2_79_PriceOut",
        "ListBidMetricsResponseIn": "_adexchangebuyer2_80_ListBidMetricsResponseIn",
        "ListBidMetricsResponseOut": "_adexchangebuyer2_81_ListBidMetricsResponseOut",
        "FilteredBidCreativeRowIn": "_adexchangebuyer2_82_FilteredBidCreativeRowIn",
        "FilteredBidCreativeRowOut": "_adexchangebuyer2_83_FilteredBidCreativeRowOut",
        "PauseProposalRequestIn": "_adexchangebuyer2_84_PauseProposalRequestIn",
        "PauseProposalRequestOut": "_adexchangebuyer2_85_PauseProposalRequestOut",
        "CreativeIn": "_adexchangebuyer2_86_CreativeIn",
        "CreativeOut": "_adexchangebuyer2_87_CreativeOut",
        "CancelNegotiationRequestIn": "_adexchangebuyer2_88_CancelNegotiationRequestIn",
        "CancelNegotiationRequestOut": "_adexchangebuyer2_89_CancelNegotiationRequestOut",
        "CreativeSizeIn": "_adexchangebuyer2_90_CreativeSizeIn",
        "CreativeSizeOut": "_adexchangebuyer2_91_CreativeSizeOut",
        "ImageIn": "_adexchangebuyer2_92_ImageIn",
        "ImageOut": "_adexchangebuyer2_93_ImageOut",
        "TimeIntervalIn": "_adexchangebuyer2_94_TimeIntervalIn",
        "TimeIntervalOut": "_adexchangebuyer2_95_TimeIntervalOut",
        "DealIn": "_adexchangebuyer2_96_DealIn",
        "DealOut": "_adexchangebuyer2_97_DealOut",
        "ListDealAssociationsResponseIn": "_adexchangebuyer2_98_ListDealAssociationsResponseIn",
        "ListDealAssociationsResponseOut": "_adexchangebuyer2_99_ListDealAssociationsResponseOut",
        "PlacementTargetingIn": "_adexchangebuyer2_100_PlacementTargetingIn",
        "PlacementTargetingOut": "_adexchangebuyer2_101_PlacementTargetingOut",
        "ListBidResponseErrorsResponseIn": "_adexchangebuyer2_102_ListBidResponseErrorsResponseIn",
        "ListBidResponseErrorsResponseOut": "_adexchangebuyer2_103_ListBidResponseErrorsResponseOut",
        "AddDealAssociationRequestIn": "_adexchangebuyer2_104_AddDealAssociationRequestIn",
        "AddDealAssociationRequestOut": "_adexchangebuyer2_105_AddDealAssociationRequestOut",
        "PublisherProfileIn": "_adexchangebuyer2_106_PublisherProfileIn",
        "PublisherProfileOut": "_adexchangebuyer2_107_PublisherProfileOut",
        "BidMetricsRowIn": "_adexchangebuyer2_108_BidMetricsRowIn",
        "BidMetricsRowOut": "_adexchangebuyer2_109_BidMetricsRowOut",
        "ClientIn": "_adexchangebuyer2_110_ClientIn",
        "ClientOut": "_adexchangebuyer2_111_ClientOut",
        "VideoTargetingIn": "_adexchangebuyer2_112_VideoTargetingIn",
        "VideoTargetingOut": "_adexchangebuyer2_113_VideoTargetingOut",
        "ListNonBillableWinningBidsResponseIn": "_adexchangebuyer2_114_ListNonBillableWinningBidsResponseIn",
        "ListNonBillableWinningBidsResponseOut": "_adexchangebuyer2_115_ListNonBillableWinningBidsResponseOut",
        "PlatformContextIn": "_adexchangebuyer2_116_PlatformContextIn",
        "PlatformContextOut": "_adexchangebuyer2_117_PlatformContextOut",
        "AdTechnologyProvidersIn": "_adexchangebuyer2_118_AdTechnologyProvidersIn",
        "AdTechnologyProvidersOut": "_adexchangebuyer2_119_AdTechnologyProvidersOut",
        "NonBillableWinningBidStatusRowIn": "_adexchangebuyer2_120_NonBillableWinningBidStatusRowIn",
        "NonBillableWinningBidStatusRowOut": "_adexchangebuyer2_121_NonBillableWinningBidStatusRowOut",
        "ServingContextIn": "_adexchangebuyer2_122_ServingContextIn",
        "ServingContextOut": "_adexchangebuyer2_123_ServingContextOut",
        "ListFilteredBidsResponseIn": "_adexchangebuyer2_124_ListFilteredBidsResponseIn",
        "ListFilteredBidsResponseOut": "_adexchangebuyer2_125_ListFilteredBidsResponseOut",
        "ListClientUserInvitationsResponseIn": "_adexchangebuyer2_126_ListClientUserInvitationsResponseIn",
        "ListClientUserInvitationsResponseOut": "_adexchangebuyer2_127_ListClientUserInvitationsResponseOut",
        "HtmlContentIn": "_adexchangebuyer2_128_HtmlContentIn",
        "HtmlContentOut": "_adexchangebuyer2_129_HtmlContentOut",
        "RealtimeTimeRangeIn": "_adexchangebuyer2_130_RealtimeTimeRangeIn",
        "RealtimeTimeRangeOut": "_adexchangebuyer2_131_RealtimeTimeRangeOut",
        "ListClientsResponseIn": "_adexchangebuyer2_132_ListClientsResponseIn",
        "ListClientsResponseOut": "_adexchangebuyer2_133_ListClientsResponseOut",
        "AppContextIn": "_adexchangebuyer2_134_AppContextIn",
        "AppContextOut": "_adexchangebuyer2_135_AppContextOut",
        "DealPauseStatusIn": "_adexchangebuyer2_136_DealPauseStatusIn",
        "DealPauseStatusOut": "_adexchangebuyer2_137_DealPauseStatusOut",
        "ProposalIn": "_adexchangebuyer2_138_ProposalIn",
        "ProposalOut": "_adexchangebuyer2_139_ProposalOut",
        "TechnologyTargetingIn": "_adexchangebuyer2_140_TechnologyTargetingIn",
        "TechnologyTargetingOut": "_adexchangebuyer2_141_TechnologyTargetingOut",
        "SizeIn": "_adexchangebuyer2_142_SizeIn",
        "SizeOut": "_adexchangebuyer2_143_SizeOut",
        "CriteriaTargetingIn": "_adexchangebuyer2_144_CriteriaTargetingIn",
        "CriteriaTargetingOut": "_adexchangebuyer2_145_CriteriaTargetingOut",
        "MetricValueIn": "_adexchangebuyer2_146_MetricValueIn",
        "MetricValueOut": "_adexchangebuyer2_147_MetricValueOut",
        "ListBidResponsesWithoutBidsResponseIn": "_adexchangebuyer2_148_ListBidResponsesWithoutBidsResponseIn",
        "ListBidResponsesWithoutBidsResponseOut": "_adexchangebuyer2_149_ListBidResponsesWithoutBidsResponseOut",
        "ListCreativeStatusBreakdownByCreativeResponseIn": "_adexchangebuyer2_150_ListCreativeStatusBreakdownByCreativeResponseIn",
        "ListCreativeStatusBreakdownByCreativeResponseOut": "_adexchangebuyer2_151_ListCreativeStatusBreakdownByCreativeResponseOut",
        "AbsoluteDateRangeIn": "_adexchangebuyer2_152_AbsoluteDateRangeIn",
        "AbsoluteDateRangeOut": "_adexchangebuyer2_153_AbsoluteDateRangeOut",
        "PublisherProfileMobileApplicationIn": "_adexchangebuyer2_154_PublisherProfileMobileApplicationIn",
        "PublisherProfileMobileApplicationOut": "_adexchangebuyer2_155_PublisherProfileMobileApplicationOut",
        "DateIn": "_adexchangebuyer2_156_DateIn",
        "DateOut": "_adexchangebuyer2_157_DateOut",
        "BidResponseWithoutBidsStatusRowIn": "_adexchangebuyer2_158_BidResponseWithoutBidsStatusRowIn",
        "BidResponseWithoutBidsStatusRowOut": "_adexchangebuyer2_159_BidResponseWithoutBidsStatusRowOut",
        "AddNoteRequestIn": "_adexchangebuyer2_160_AddNoteRequestIn",
        "AddNoteRequestOut": "_adexchangebuyer2_161_AddNoteRequestOut",
        "SellerIn": "_adexchangebuyer2_162_SellerIn",
        "SellerOut": "_adexchangebuyer2_163_SellerOut",
        "ProductIn": "_adexchangebuyer2_164_ProductIn",
        "ProductOut": "_adexchangebuyer2_165_ProductOut",
        "EmptyIn": "_adexchangebuyer2_166_EmptyIn",
        "EmptyOut": "_adexchangebuyer2_167_EmptyOut",
        "CreativeDealAssociationIn": "_adexchangebuyer2_168_CreativeDealAssociationIn",
        "CreativeDealAssociationOut": "_adexchangebuyer2_169_CreativeDealAssociationOut",
        "ListCreativesResponseIn": "_adexchangebuyer2_170_ListCreativesResponseIn",
        "ListCreativesResponseOut": "_adexchangebuyer2_171_ListCreativesResponseOut",
        "InventorySizeTargetingIn": "_adexchangebuyer2_172_InventorySizeTargetingIn",
        "InventorySizeTargetingOut": "_adexchangebuyer2_173_InventorySizeTargetingOut",
        "StopWatchingCreativeRequestIn": "_adexchangebuyer2_174_StopWatchingCreativeRequestIn",
        "StopWatchingCreativeRequestOut": "_adexchangebuyer2_175_StopWatchingCreativeRequestOut",
        "ListImpressionMetricsResponseIn": "_adexchangebuyer2_176_ListImpressionMetricsResponseIn",
        "ListImpressionMetricsResponseOut": "_adexchangebuyer2_177_ListImpressionMetricsResponseOut",
        "NonGuaranteedAuctionTermsIn": "_adexchangebuyer2_178_NonGuaranteedAuctionTermsIn",
        "NonGuaranteedAuctionTermsOut": "_adexchangebuyer2_179_NonGuaranteedAuctionTermsOut",
        "GuaranteedFixedPriceTermsIn": "_adexchangebuyer2_180_GuaranteedFixedPriceTermsIn",
        "GuaranteedFixedPriceTermsOut": "_adexchangebuyer2_181_GuaranteedFixedPriceTermsOut",
        "NonGuaranteedFixedPriceTermsIn": "_adexchangebuyer2_182_NonGuaranteedFixedPriceTermsIn",
        "NonGuaranteedFixedPriceTermsOut": "_adexchangebuyer2_183_NonGuaranteedFixedPriceTermsOut",
        "CreativeRestrictionsIn": "_adexchangebuyer2_184_CreativeRestrictionsIn",
        "CreativeRestrictionsOut": "_adexchangebuyer2_185_CreativeRestrictionsOut",
        "OperatingSystemTargetingIn": "_adexchangebuyer2_186_OperatingSystemTargetingIn",
        "OperatingSystemTargetingOut": "_adexchangebuyer2_187_OperatingSystemTargetingOut",
        "ListClientUsersResponseIn": "_adexchangebuyer2_188_ListClientUsersResponseIn",
        "ListClientUsersResponseOut": "_adexchangebuyer2_189_ListClientUsersResponseOut",
        "RemoveDealAssociationRequestIn": "_adexchangebuyer2_190_RemoveDealAssociationRequestIn",
        "RemoveDealAssociationRequestOut": "_adexchangebuyer2_191_RemoveDealAssociationRequestOut",
        "ClientUserIn": "_adexchangebuyer2_192_ClientUserIn",
        "ClientUserOut": "_adexchangebuyer2_193_ClientUserOut",
        "DeliveryControlIn": "_adexchangebuyer2_194_DeliveryControlIn",
        "DeliveryControlOut": "_adexchangebuyer2_195_DeliveryControlOut",
        "WatchCreativeRequestIn": "_adexchangebuyer2_196_WatchCreativeRequestIn",
        "WatchCreativeRequestOut": "_adexchangebuyer2_197_WatchCreativeRequestOut",
        "AuctionContextIn": "_adexchangebuyer2_198_AuctionContextIn",
        "AuctionContextOut": "_adexchangebuyer2_199_AuctionContextOut",
        "ContactInformationIn": "_adexchangebuyer2_200_ContactInformationIn",
        "ContactInformationOut": "_adexchangebuyer2_201_ContactInformationOut",
        "MoneyIn": "_adexchangebuyer2_202_MoneyIn",
        "MoneyOut": "_adexchangebuyer2_203_MoneyOut",
        "DealTermsIn": "_adexchangebuyer2_204_DealTermsIn",
        "DealTermsOut": "_adexchangebuyer2_205_DealTermsOut",
        "ListLosingBidsResponseIn": "_adexchangebuyer2_206_ListLosingBidsResponseIn",
        "ListLosingBidsResponseOut": "_adexchangebuyer2_207_ListLosingBidsResponseOut",
        "AdSizeIn": "_adexchangebuyer2_208_AdSizeIn",
        "AdSizeOut": "_adexchangebuyer2_209_AdSizeOut",
        "DealServingMetadataIn": "_adexchangebuyer2_210_DealServingMetadataIn",
        "DealServingMetadataOut": "_adexchangebuyer2_211_DealServingMetadataOut",
        "LocationContextIn": "_adexchangebuyer2_212_LocationContextIn",
        "LocationContextOut": "_adexchangebuyer2_213_LocationContextOut",
        "AcceptProposalRequestIn": "_adexchangebuyer2_214_AcceptProposalRequestIn",
        "AcceptProposalRequestOut": "_adexchangebuyer2_215_AcceptProposalRequestOut",
        "FrequencyCapIn": "_adexchangebuyer2_216_FrequencyCapIn",
        "FrequencyCapOut": "_adexchangebuyer2_217_FrequencyCapOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ListProductsResponseIn"] = t.struct(
        {
            "products": t.array(t.proxy(renames["ProductIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListProductsResponseIn"])
    types["ListProductsResponseOut"] = t.struct(
        {
            "products": t.array(t.proxy(renames["ProductOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListProductsResponseOut"])
    types["ListPublisherProfilesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "publisherProfiles": t.array(
                t.proxy(renames["PublisherProfileIn"])
            ).optional(),
        }
    ).named(renames["ListPublisherProfilesResponseIn"])
    types["ListPublisherProfilesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "publisherProfiles": t.array(
                t.proxy(renames["PublisherProfileOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPublisherProfilesResponseOut"])
    types["ListFilteredBidRequestsResponseIn"] = t.struct(
        {
            "calloutStatusRows": t.array(
                t.proxy(renames["CalloutStatusRowIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListFilteredBidRequestsResponseIn"])
    types["ListFilteredBidRequestsResponseOut"] = t.struct(
        {
            "calloutStatusRows": t.array(
                t.proxy(renames["CalloutStatusRowOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListFilteredBidRequestsResponseOut"])
    types["CalloutStatusRowIn"] = t.struct(
        {
            "calloutStatusId": t.integer().optional(),
            "impressionCount": t.proxy(renames["MetricValueIn"]).optional(),
            "rowDimensions": t.proxy(renames["RowDimensionsIn"]).optional(),
        }
    ).named(renames["CalloutStatusRowIn"])
    types["CalloutStatusRowOut"] = t.struct(
        {
            "calloutStatusId": t.integer().optional(),
            "impressionCount": t.proxy(renames["MetricValueOut"]).optional(),
            "rowDimensions": t.proxy(renames["RowDimensionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CalloutStatusRowOut"])
    types["BuyerIn"] = t.struct({"accountId": t.string().optional()}).named(
        renames["BuyerIn"]
    )
    types["BuyerOut"] = t.struct(
        {
            "accountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuyerOut"])
    types["TargetingCriteriaIn"] = t.struct(
        {
            "key": t.string().optional(),
            "inclusions": t.array(t.proxy(renames["TargetingValueIn"])).optional(),
            "exclusions": t.array(t.proxy(renames["TargetingValueIn"])).optional(),
        }
    ).named(renames["TargetingCriteriaIn"])
    types["TargetingCriteriaOut"] = t.struct(
        {
            "key": t.string().optional(),
            "inclusions": t.array(t.proxy(renames["TargetingValueOut"])).optional(),
            "exclusions": t.array(t.proxy(renames["TargetingValueOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetingCriteriaOut"])
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
    types["ListFilterSetsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "filterSets": t.array(t.proxy(renames["FilterSetIn"])).optional(),
        }
    ).named(renames["ListFilterSetsResponseIn"])
    types["ListFilterSetsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "filterSets": t.array(t.proxy(renames["FilterSetOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListFilterSetsResponseOut"])
    types["TimeOfDayIn"] = t.struct(
        {
            "hours": t.integer().optional(),
            "minutes": t.integer().optional(),
            "nanos": t.integer().optional(),
            "seconds": t.integer().optional(),
        }
    ).named(renames["TimeOfDayIn"])
    types["TimeOfDayOut"] = t.struct(
        {
            "hours": t.integer().optional(),
            "minutes": t.integer().optional(),
            "nanos": t.integer().optional(),
            "seconds": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeOfDayOut"])
    types["FilteredBidDetailRowIn"] = t.struct(
        {
            "detailId": t.integer().optional(),
            "bidCount": t.proxy(renames["MetricValueIn"]).optional(),
            "rowDimensions": t.proxy(renames["RowDimensionsIn"]).optional(),
            "detail": t.string().optional(),
        }
    ).named(renames["FilteredBidDetailRowIn"])
    types["FilteredBidDetailRowOut"] = t.struct(
        {
            "detailId": t.integer().optional(),
            "bidCount": t.proxy(renames["MetricValueOut"]).optional(),
            "rowDimensions": t.proxy(renames["RowDimensionsOut"]).optional(),
            "detail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilteredBidDetailRowOut"])
    types["CompleteSetupRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CompleteSetupRequestIn"]
    )
    types["CompleteSetupRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CompleteSetupRequestOut"])
    types["ListProposalsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "proposals": t.array(t.proxy(renames["ProposalIn"])).optional(),
        }
    ).named(renames["ListProposalsResponseIn"])
    types["ListProposalsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "proposals": t.array(t.proxy(renames["ProposalOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListProposalsResponseOut"])
    types["TargetingValueIn"] = t.struct(
        {
            "stringValue": t.string().optional(),
            "longValue": t.string().optional(),
            "creativeSizeValue": t.proxy(renames["CreativeSizeIn"]).optional(),
            "dayPartTargetingValue": t.proxy(renames["DayPartTargetingIn"]).optional(),
        }
    ).named(renames["TargetingValueIn"])
    types["TargetingValueOut"] = t.struct(
        {
            "stringValue": t.string().optional(),
            "longValue": t.string().optional(),
            "creativeSizeValue": t.proxy(renames["CreativeSizeOut"]).optional(),
            "dayPartTargetingValue": t.proxy(renames["DayPartTargetingOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetingValueOut"])
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
    types["SecurityContextIn"] = t.struct(
        {"securities": t.array(t.string()).optional()}
    ).named(renames["SecurityContextIn"])
    types["SecurityContextOut"] = t.struct(
        {
            "securities": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecurityContextOut"])
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
    types["RowDimensionsIn"] = t.struct(
        {
            "publisherIdentifier": t.string().optional(),
            "timeInterval": t.proxy(renames["TimeIntervalIn"]).optional(),
        }
    ).named(renames["RowDimensionsIn"])
    types["RowDimensionsOut"] = t.struct(
        {
            "publisherIdentifier": t.string().optional(),
            "timeInterval": t.proxy(renames["TimeIntervalOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RowDimensionsOut"])
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
    types["PricePerBuyerIn"] = t.struct(
        {
            "price": t.proxy(renames["PriceIn"]).optional(),
            "advertiserIds": t.array(t.string()).optional(),
            "buyer": t.proxy(renames["BuyerIn"]).optional(),
        }
    ).named(renames["PricePerBuyerIn"])
    types["PricePerBuyerOut"] = t.struct(
        {
            "price": t.proxy(renames["PriceOut"]).optional(),
            "advertiserIds": t.array(t.string()).optional(),
            "buyer": t.proxy(renames["BuyerOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PricePerBuyerOut"])
    types["DayPartIn"] = t.struct(
        {
            "dayOfWeek": t.string().optional(),
            "startTime": t.proxy(renames["TimeOfDayIn"]).optional(),
            "endTime": t.proxy(renames["TimeOfDayIn"]).optional(),
        }
    ).named(renames["DayPartIn"])
    types["DayPartOut"] = t.struct(
        {
            "dayOfWeek": t.string().optional(),
            "startTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "endTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DayPartOut"])
    types["VideoContentIn"] = t.struct(
        {"videoVastXml": t.string().optional(), "videoUrl": t.string().optional()}
    ).named(renames["VideoContentIn"])
    types["VideoContentOut"] = t.struct(
        {
            "videoVastXml": t.string().optional(),
            "videoUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoContentOut"])
    types["ImpressionMetricsRowIn"] = t.struct(
        {
            "responsesWithBids": t.proxy(renames["MetricValueIn"]).optional(),
            "inventoryMatches": t.proxy(renames["MetricValueIn"]).optional(),
            "successfulResponses": t.proxy(renames["MetricValueIn"]).optional(),
            "bidRequests": t.proxy(renames["MetricValueIn"]).optional(),
            "rowDimensions": t.proxy(renames["RowDimensionsIn"]).optional(),
            "availableImpressions": t.proxy(renames["MetricValueIn"]).optional(),
        }
    ).named(renames["ImpressionMetricsRowIn"])
    types["ImpressionMetricsRowOut"] = t.struct(
        {
            "responsesWithBids": t.proxy(renames["MetricValueOut"]).optional(),
            "inventoryMatches": t.proxy(renames["MetricValueOut"]).optional(),
            "successfulResponses": t.proxy(renames["MetricValueOut"]).optional(),
            "bidRequests": t.proxy(renames["MetricValueOut"]).optional(),
            "rowDimensions": t.proxy(renames["RowDimensionsOut"]).optional(),
            "availableImpressions": t.proxy(renames["MetricValueOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImpressionMetricsRowOut"])
    types["DayPartTargetingIn"] = t.struct(
        {
            "timeZoneType": t.string().optional(),
            "dayParts": t.array(t.proxy(renames["DayPartIn"])).optional(),
        }
    ).named(renames["DayPartTargetingIn"])
    types["DayPartTargetingOut"] = t.struct(
        {
            "timeZoneType": t.string().optional(),
            "dayParts": t.array(t.proxy(renames["DayPartOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DayPartTargetingOut"])
    types["FilterSetIn"] = t.struct(
        {
            "absoluteDateRange": t.proxy(renames["AbsoluteDateRangeIn"]).optional(),
            "publisherIdentifiers": t.array(t.string()).optional(),
            "format": t.string().optional(),
            "dealId": t.string().optional(),
            "creativeId": t.string().optional(),
            "platforms": t.array(t.string()).optional(),
            "sellerNetworkIds": t.array(t.integer()).optional(),
            "realtimeTimeRange": t.proxy(renames["RealtimeTimeRangeIn"]).optional(),
            "timeSeriesGranularity": t.string().optional(),
            "name": t.string().optional(),
            "formats": t.array(t.string()).optional(),
            "environment": t.string().optional(),
            "relativeDateRange": t.proxy(renames["RelativeDateRangeIn"]).optional(),
            "breakdownDimensions": t.array(t.string()).optional(),
        }
    ).named(renames["FilterSetIn"])
    types["FilterSetOut"] = t.struct(
        {
            "absoluteDateRange": t.proxy(renames["AbsoluteDateRangeOut"]).optional(),
            "publisherIdentifiers": t.array(t.string()).optional(),
            "format": t.string().optional(),
            "dealId": t.string().optional(),
            "creativeId": t.string().optional(),
            "platforms": t.array(t.string()).optional(),
            "sellerNetworkIds": t.array(t.integer()).optional(),
            "realtimeTimeRange": t.proxy(renames["RealtimeTimeRangeOut"]).optional(),
            "timeSeriesGranularity": t.string().optional(),
            "name": t.string().optional(),
            "formats": t.array(t.string()).optional(),
            "environment": t.string().optional(),
            "relativeDateRange": t.proxy(renames["RelativeDateRangeOut"]).optional(),
            "breakdownDimensions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterSetOut"])
    types["ResumeProposalRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ResumeProposalRequestIn"]
    )
    types["ResumeProposalRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ResumeProposalRequestOut"])
    types["NativeContentIn"] = t.struct(
        {
            "body": t.string().optional(),
            "clickTrackingUrl": t.string().optional(),
            "advertiserName": t.string().optional(),
            "videoUrl": t.string().optional(),
            "storeUrl": t.string().optional(),
            "priceDisplayText": t.string().optional(),
            "logo": t.proxy(renames["ImageIn"]).optional(),
            "callToAction": t.string().optional(),
            "starRating": t.number().optional(),
            "headline": t.string().optional(),
            "image": t.proxy(renames["ImageIn"]).optional(),
            "appIcon": t.proxy(renames["ImageIn"]).optional(),
            "clickLinkUrl": t.string().optional(),
        }
    ).named(renames["NativeContentIn"])
    types["NativeContentOut"] = t.struct(
        {
            "body": t.string().optional(),
            "clickTrackingUrl": t.string().optional(),
            "advertiserName": t.string().optional(),
            "videoUrl": t.string().optional(),
            "storeUrl": t.string().optional(),
            "priceDisplayText": t.string().optional(),
            "logo": t.proxy(renames["ImageOut"]).optional(),
            "callToAction": t.string().optional(),
            "starRating": t.number().optional(),
            "headline": t.string().optional(),
            "image": t.proxy(renames["ImageOut"]).optional(),
            "appIcon": t.proxy(renames["ImageOut"]).optional(),
            "clickLinkUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NativeContentOut"])
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
    types["CorrectionIn"] = t.struct(
        {
            "details": t.array(t.string()).optional(),
            "type": t.string().optional(),
            "contexts": t.array(t.proxy(renames["ServingContextIn"])).optional(),
        }
    ).named(renames["CorrectionIn"])
    types["CorrectionOut"] = t.struct(
        {
            "details": t.array(t.string()).optional(),
            "type": t.string().optional(),
            "contexts": t.array(t.proxy(renames["ServingContextOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CorrectionOut"])
    types["MarketplaceTargetingIn"] = t.struct(
        {
            "videoTargeting": t.proxy(renames["VideoTargetingIn"]).optional(),
            "geoTargeting": t.proxy(renames["CriteriaTargetingIn"]).optional(),
            "inventorySizeTargeting": t.proxy(
                renames["InventorySizeTargetingIn"]
            ).optional(),
            "technologyTargeting": t.proxy(renames["TechnologyTargetingIn"]).optional(),
            "placementTargeting": t.proxy(renames["PlacementTargetingIn"]).optional(),
        }
    ).named(renames["MarketplaceTargetingIn"])
    types["MarketplaceTargetingOut"] = t.struct(
        {
            "videoTargeting": t.proxy(renames["VideoTargetingOut"]).optional(),
            "geoTargeting": t.proxy(renames["CriteriaTargetingOut"]).optional(),
            "inventorySizeTargeting": t.proxy(
                renames["InventorySizeTargetingOut"]
            ).optional(),
            "technologyTargeting": t.proxy(
                renames["TechnologyTargetingOut"]
            ).optional(),
            "placementTargeting": t.proxy(renames["PlacementTargetingOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MarketplaceTargetingOut"])
    types["CreativeStatusRowIn"] = t.struct(
        {
            "bidCount": t.proxy(renames["MetricValueIn"]).optional(),
            "rowDimensions": t.proxy(renames["RowDimensionsIn"]).optional(),
            "creativeStatusId": t.integer().optional(),
        }
    ).named(renames["CreativeStatusRowIn"])
    types["CreativeStatusRowOut"] = t.struct(
        {
            "bidCount": t.proxy(renames["MetricValueOut"]).optional(),
            "rowDimensions": t.proxy(renames["RowDimensionsOut"]).optional(),
            "creativeStatusId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeStatusRowOut"])
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
    types["ResumeProposalDealsRequestIn"] = t.struct(
        {"externalDealIds": t.array(t.string()).optional()}
    ).named(renames["ResumeProposalDealsRequestIn"])
    types["ResumeProposalDealsRequestOut"] = t.struct(
        {
            "externalDealIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResumeProposalDealsRequestOut"])
    types["PrivateDataIn"] = t.struct({"referenceId": t.string().optional()}).named(
        renames["PrivateDataIn"]
    )
    types["PrivateDataOut"] = t.struct(
        {
            "referenceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrivateDataOut"])
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
    types["ServingRestrictionIn"] = t.struct(
        {
            "disapproval": t.proxy(renames["DisapprovalIn"]).optional(),
            "status": t.string().optional(),
            "disapprovalReasons": t.array(t.proxy(renames["DisapprovalIn"])).optional(),
            "contexts": t.array(t.proxy(renames["ServingContextIn"])).optional(),
        }
    ).named(renames["ServingRestrictionIn"])
    types["ServingRestrictionOut"] = t.struct(
        {
            "disapproval": t.proxy(renames["DisapprovalOut"]).optional(),
            "status": t.string().optional(),
            "disapprovalReasons": t.array(
                t.proxy(renames["DisapprovalOut"])
            ).optional(),
            "contexts": t.array(t.proxy(renames["ServingContextOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServingRestrictionOut"])
    types["NoteIn"] = t.struct({"note": t.string().optional()}).named(renames["NoteIn"])
    types["NoteOut"] = t.struct(
        {
            "note": t.string().optional(),
            "creatorRole": t.string().optional(),
            "proposalRevision": t.string().optional(),
            "createTime": t.string().optional(),
            "noteId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NoteOut"])
    types["ClientUserInvitationIn"] = t.struct(
        {
            "email": t.string().optional(),
            "clientAccountId": t.string().optional(),
            "invitationId": t.string().optional(),
        }
    ).named(renames["ClientUserInvitationIn"])
    types["ClientUserInvitationOut"] = t.struct(
        {
            "email": t.string().optional(),
            "clientAccountId": t.string().optional(),
            "invitationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientUserInvitationOut"])
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
    types["FilteredBidCreativeRowIn"] = t.struct(
        {
            "bidCount": t.proxy(renames["MetricValueIn"]).optional(),
            "rowDimensions": t.proxy(renames["RowDimensionsIn"]).optional(),
            "creativeId": t.string().optional(),
        }
    ).named(renames["FilteredBidCreativeRowIn"])
    types["FilteredBidCreativeRowOut"] = t.struct(
        {
            "bidCount": t.proxy(renames["MetricValueOut"]).optional(),
            "rowDimensions": t.proxy(renames["RowDimensionsOut"]).optional(),
            "creativeId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilteredBidCreativeRowOut"])
    types["PauseProposalRequestIn"] = t.struct({"reason": t.string().optional()}).named(
        renames["PauseProposalRequestIn"]
    )
    types["PauseProposalRequestOut"] = t.struct(
        {
            "reason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PauseProposalRequestOut"])
    types["CreativeIn"] = t.struct(
        {
            "creativeId": t.string().optional(),
            "dealsStatus": t.string().optional(),
            "corrections": t.array(t.proxy(renames["CorrectionIn"])).optional(),
            "version": t.integer().optional(),
            "declaredClickThroughUrls": t.array(t.string()).optional(),
            "accountId": t.string().optional(),
            "clickThroughUrls": t.array(t.string()).optional(),
            "detectedDomains": t.array(t.string()).optional(),
            "adChoicesDestinationUrl": t.string().optional(),
            "detectedSensitiveCategories": t.array(t.integer()).optional(),
            "adTechnologyProviders": t.proxy(
                renames["AdTechnologyProvidersIn"]
            ).optional(),
            "apiUpdateTime": t.string().optional(),
            "advertiserName": t.string().optional(),
            "openAuctionStatus": t.string().optional(),
            "attributes": t.array(t.string()).optional(),
            "agencyId": t.string().optional(),
            "servingRestrictions": t.array(
                t.proxy(renames["ServingRestrictionIn"])
            ).optional(),
            "detectedProductCategories": t.array(t.integer()).optional(),
            "impressionTrackingUrls": t.array(t.string()).optional(),
            "video": t.proxy(renames["VideoContentIn"]).optional(),
            "detectedAdvertiserIds": t.array(t.string()).optional(),
            "native": t.proxy(renames["NativeContentIn"]).optional(),
            "restrictedCategories": t.array(t.string()).optional(),
            "vendorIds": t.array(t.integer()).optional(),
            "html": t.proxy(renames["HtmlContentIn"]).optional(),
            "detectedLanguages": t.array(t.string()).optional(),
        }
    ).named(renames["CreativeIn"])
    types["CreativeOut"] = t.struct(
        {
            "creativeId": t.string().optional(),
            "dealsStatus": t.string().optional(),
            "corrections": t.array(t.proxy(renames["CorrectionOut"])).optional(),
            "version": t.integer().optional(),
            "declaredClickThroughUrls": t.array(t.string()).optional(),
            "accountId": t.string().optional(),
            "clickThroughUrls": t.array(t.string()).optional(),
            "detectedDomains": t.array(t.string()).optional(),
            "adChoicesDestinationUrl": t.string().optional(),
            "detectedSensitiveCategories": t.array(t.integer()).optional(),
            "adTechnologyProviders": t.proxy(
                renames["AdTechnologyProvidersOut"]
            ).optional(),
            "apiUpdateTime": t.string().optional(),
            "advertiserName": t.string().optional(),
            "openAuctionStatus": t.string().optional(),
            "attributes": t.array(t.string()).optional(),
            "agencyId": t.string().optional(),
            "servingRestrictions": t.array(
                t.proxy(renames["ServingRestrictionOut"])
            ).optional(),
            "detectedProductCategories": t.array(t.integer()).optional(),
            "impressionTrackingUrls": t.array(t.string()).optional(),
            "video": t.proxy(renames["VideoContentOut"]).optional(),
            "detectedAdvertiserIds": t.array(t.string()).optional(),
            "native": t.proxy(renames["NativeContentOut"]).optional(),
            "restrictedCategories": t.array(t.string()).optional(),
            "vendorIds": t.array(t.integer()).optional(),
            "html": t.proxy(renames["HtmlContentOut"]).optional(),
            "detectedLanguages": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeOut"])
    types["CancelNegotiationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelNegotiationRequestIn"]
    )
    types["CancelNegotiationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelNegotiationRequestOut"])
    types["CreativeSizeIn"] = t.struct(
        {
            "allowedFormats": t.array(t.string()).optional(),
            "companionSizes": t.array(t.proxy(renames["SizeIn"])).optional(),
            "nativeTemplate": t.string().optional(),
            "creativeSizeType": t.string().optional(),
            "skippableAdType": t.string().optional(),
            "size": t.proxy(renames["SizeIn"]).optional(),
        }
    ).named(renames["CreativeSizeIn"])
    types["CreativeSizeOut"] = t.struct(
        {
            "allowedFormats": t.array(t.string()).optional(),
            "companionSizes": t.array(t.proxy(renames["SizeOut"])).optional(),
            "nativeTemplate": t.string().optional(),
            "creativeSizeType": t.string().optional(),
            "skippableAdType": t.string().optional(),
            "size": t.proxy(renames["SizeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeSizeOut"])
    types["ImageIn"] = t.struct(
        {
            "url": t.string().optional(),
            "height": t.integer().optional(),
            "width": t.integer().optional(),
        }
    ).named(renames["ImageIn"])
    types["ImageOut"] = t.struct(
        {
            "url": t.string().optional(),
            "height": t.integer().optional(),
            "width": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageOut"])
    types["TimeIntervalIn"] = t.struct(
        {"endTime": t.string().optional(), "startTime": t.string().optional()}
    ).named(renames["TimeIntervalIn"])
    types["TimeIntervalOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeIntervalOut"])
    types["DealIn"] = t.struct(
        {
            "webPropertyCode": t.string().optional(),
            "dealTerms": t.proxy(renames["DealTermsIn"]).optional(),
            "createProductRevision": t.string().optional(),
            "availableStartTime": t.string().optional(),
            "availableEndTime": t.string().optional(),
            "createProductId": t.string().optional(),
            "syndicationProduct": t.string().optional(),
            "deliveryControl": t.proxy(renames["DeliveryControlIn"]).optional(),
            "displayName": t.string().optional(),
            "buyerPrivateData": t.proxy(renames["PrivateDataIn"]).optional(),
            "targetingCriterion": t.array(
                t.proxy(renames["TargetingCriteriaIn"])
            ).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["DealIn"])
    types["DealOut"] = t.struct(
        {
            "webPropertyCode": t.string().optional(),
            "targeting": t.proxy(renames["MarketplaceTargetingOut"]).optional(),
            "dealTerms": t.proxy(renames["DealTermsOut"]).optional(),
            "dealServingMetadata": t.proxy(
                renames["DealServingMetadataOut"]
            ).optional(),
            "programmaticCreativeSource": t.string().optional(),
            "createProductRevision": t.string().optional(),
            "availableStartTime": t.string().optional(),
            "creativePreApprovalPolicy": t.string().optional(),
            "availableEndTime": t.string().optional(),
            "creativeSafeFrameCompatibility": t.string().optional(),
            "creativeRestrictions": t.proxy(
                renames["CreativeRestrictionsOut"]
            ).optional(),
            "sellerContacts": t.array(
                t.proxy(renames["ContactInformationOut"])
            ).optional(),
            "isSetupComplete": t.boolean().optional(),
            "createProductId": t.string().optional(),
            "syndicationProduct": t.string().optional(),
            "deliveryControl": t.proxy(renames["DeliveryControlOut"]).optional(),
            "externalDealId": t.string().optional(),
            "proposalId": t.string().optional(),
            "updateTime": t.string().optional(),
            "dealId": t.string().optional(),
            "displayName": t.string().optional(),
            "buyerPrivateData": t.proxy(renames["PrivateDataOut"]).optional(),
            "targetingCriterion": t.array(
                t.proxy(renames["TargetingCriteriaOut"])
            ).optional(),
            "createTime": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DealOut"])
    types["ListDealAssociationsResponseIn"] = t.struct(
        {
            "associations": t.array(
                t.proxy(renames["CreativeDealAssociationIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListDealAssociationsResponseIn"])
    types["ListDealAssociationsResponseOut"] = t.struct(
        {
            "associations": t.array(
                t.proxy(renames["CreativeDealAssociationOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDealAssociationsResponseOut"])
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
    types["AddDealAssociationRequestIn"] = t.struct(
        {"association": t.proxy(renames["CreativeDealAssociationIn"]).optional()}
    ).named(renames["AddDealAssociationRequestIn"])
    types["AddDealAssociationRequestOut"] = t.struct(
        {
            "association": t.proxy(renames["CreativeDealAssociationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddDealAssociationRequestOut"])
    types["PublisherProfileIn"] = t.struct(
        {
            "samplePageUrl": t.string().optional(),
            "domains": t.array(t.string()).optional(),
            "directDealsContact": t.string().optional(),
            "displayName": t.string().optional(),
            "topHeadlines": t.array(t.string()).optional(),
            "overview": t.string().optional(),
            "publisherProfileId": t.string().optional(),
            "buyerPitchStatement": t.string().optional(),
            "mobileApps": t.array(
                t.proxy(renames["PublisherProfileMobileApplicationIn"])
            ).optional(),
            "seller": t.proxy(renames["SellerIn"]).optional(),
            "rateCardInfoUrl": t.string().optional(),
            "mediaKitUrl": t.string().optional(),
            "programmaticDealsContact": t.string().optional(),
            "audienceDescription": t.string().optional(),
            "logoUrl": t.string().optional(),
            "isParent": t.boolean().optional(),
            "googlePlusUrl": t.string().optional(),
        }
    ).named(renames["PublisherProfileIn"])
    types["PublisherProfileOut"] = t.struct(
        {
            "samplePageUrl": t.string().optional(),
            "domains": t.array(t.string()).optional(),
            "directDealsContact": t.string().optional(),
            "displayName": t.string().optional(),
            "topHeadlines": t.array(t.string()).optional(),
            "overview": t.string().optional(),
            "publisherProfileId": t.string().optional(),
            "buyerPitchStatement": t.string().optional(),
            "mobileApps": t.array(
                t.proxy(renames["PublisherProfileMobileApplicationOut"])
            ).optional(),
            "seller": t.proxy(renames["SellerOut"]).optional(),
            "rateCardInfoUrl": t.string().optional(),
            "mediaKitUrl": t.string().optional(),
            "programmaticDealsContact": t.string().optional(),
            "audienceDescription": t.string().optional(),
            "logoUrl": t.string().optional(),
            "isParent": t.boolean().optional(),
            "googlePlusUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublisherProfileOut"])
    types["BidMetricsRowIn"] = t.struct(
        {
            "rowDimensions": t.proxy(renames["RowDimensionsIn"]).optional(),
            "measurableImpressions": t.proxy(renames["MetricValueIn"]).optional(),
            "billedImpressions": t.proxy(renames["MetricValueIn"]).optional(),
            "bids": t.proxy(renames["MetricValueIn"]).optional(),
            "viewableImpressions": t.proxy(renames["MetricValueIn"]).optional(),
            "impressionsWon": t.proxy(renames["MetricValueIn"]).optional(),
            "bidsInAuction": t.proxy(renames["MetricValueIn"]).optional(),
            "reachedQueries": t.proxy(renames["MetricValueIn"]).optional(),
        }
    ).named(renames["BidMetricsRowIn"])
    types["BidMetricsRowOut"] = t.struct(
        {
            "rowDimensions": t.proxy(renames["RowDimensionsOut"]).optional(),
            "measurableImpressions": t.proxy(renames["MetricValueOut"]).optional(),
            "billedImpressions": t.proxy(renames["MetricValueOut"]).optional(),
            "bids": t.proxy(renames["MetricValueOut"]).optional(),
            "viewableImpressions": t.proxy(renames["MetricValueOut"]).optional(),
            "impressionsWon": t.proxy(renames["MetricValueOut"]).optional(),
            "bidsInAuction": t.proxy(renames["MetricValueOut"]).optional(),
            "reachedQueries": t.proxy(renames["MetricValueOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BidMetricsRowOut"])
    types["ClientIn"] = t.struct(
        {
            "entityId": t.string().optional(),
            "clientAccountId": t.string().optional(),
            "clientName": t.string().optional(),
            "visibleToSeller": t.boolean().optional(),
            "partnerClientId": t.string().optional(),
            "role": t.string().optional(),
            "status": t.string().optional(),
            "entityName": t.string().optional(),
            "entityType": t.string().optional(),
        }
    ).named(renames["ClientIn"])
    types["ClientOut"] = t.struct(
        {
            "entityId": t.string().optional(),
            "clientAccountId": t.string().optional(),
            "clientName": t.string().optional(),
            "visibleToSeller": t.boolean().optional(),
            "partnerClientId": t.string().optional(),
            "role": t.string().optional(),
            "status": t.string().optional(),
            "entityName": t.string().optional(),
            "entityType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientOut"])
    types["VideoTargetingIn"] = t.struct(
        {
            "targetedPositionTypes": t.array(t.string()).optional(),
            "excludedPositionTypes": t.array(t.string()).optional(),
        }
    ).named(renames["VideoTargetingIn"])
    types["VideoTargetingOut"] = t.struct(
        {
            "targetedPositionTypes": t.array(t.string()).optional(),
            "excludedPositionTypes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoTargetingOut"])
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
    types["PlatformContextIn"] = t.struct(
        {"platforms": t.array(t.string()).optional()}
    ).named(renames["PlatformContextIn"])
    types["PlatformContextOut"] = t.struct(
        {
            "platforms": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlatformContextOut"])
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
    types["NonBillableWinningBidStatusRowIn"] = t.struct(
        {
            "status": t.string().optional(),
            "rowDimensions": t.proxy(renames["RowDimensionsIn"]).optional(),
            "bidCount": t.proxy(renames["MetricValueIn"]).optional(),
        }
    ).named(renames["NonBillableWinningBidStatusRowIn"])
    types["NonBillableWinningBidStatusRowOut"] = t.struct(
        {
            "status": t.string().optional(),
            "rowDimensions": t.proxy(renames["RowDimensionsOut"]).optional(),
            "bidCount": t.proxy(renames["MetricValueOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NonBillableWinningBidStatusRowOut"])
    types["ServingContextIn"] = t.struct(
        {
            "location": t.proxy(renames["LocationContextIn"]).optional(),
            "securityType": t.proxy(renames["SecurityContextIn"]).optional(),
            "all": t.string().optional(),
            "platform": t.proxy(renames["PlatformContextIn"]).optional(),
            "appType": t.proxy(renames["AppContextIn"]).optional(),
            "auctionType": t.proxy(renames["AuctionContextIn"]).optional(),
        }
    ).named(renames["ServingContextIn"])
    types["ServingContextOut"] = t.struct(
        {
            "location": t.proxy(renames["LocationContextOut"]).optional(),
            "securityType": t.proxy(renames["SecurityContextOut"]).optional(),
            "all": t.string().optional(),
            "platform": t.proxy(renames["PlatformContextOut"]).optional(),
            "appType": t.proxy(renames["AppContextOut"]).optional(),
            "auctionType": t.proxy(renames["AuctionContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServingContextOut"])
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
    types["RealtimeTimeRangeIn"] = t.struct(
        {"startTimestamp": t.string().optional()}
    ).named(renames["RealtimeTimeRangeIn"])
    types["RealtimeTimeRangeOut"] = t.struct(
        {
            "startTimestamp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RealtimeTimeRangeOut"])
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
    types["AppContextIn"] = t.struct(
        {"appTypes": t.array(t.string()).optional()}
    ).named(renames["AppContextIn"])
    types["AppContextOut"] = t.struct(
        {
            "appTypes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppContextOut"])
    types["DealPauseStatusIn"] = t.struct(
        {
            "buyerPauseReason": t.string().optional(),
            "firstPausedBy": t.string().optional(),
            "sellerPauseReason": t.string().optional(),
            "hasSellerPaused": t.boolean().optional(),
            "hasBuyerPaused": t.boolean().optional(),
        }
    ).named(renames["DealPauseStatusIn"])
    types["DealPauseStatusOut"] = t.struct(
        {
            "buyerPauseReason": t.string().optional(),
            "firstPausedBy": t.string().optional(),
            "sellerPauseReason": t.string().optional(),
            "hasSellerPaused": t.boolean().optional(),
            "hasBuyerPaused": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DealPauseStatusOut"])
    types["ProposalIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "buyerPrivateData": t.proxy(renames["PrivateDataIn"]).optional(),
            "buyer": t.proxy(renames["BuyerIn"]).optional(),
            "seller": t.proxy(renames["SellerIn"]).optional(),
            "deals": t.array(t.proxy(renames["DealIn"])).optional(),
            "buyerContacts": t.array(
                t.proxy(renames["ContactInformationIn"])
            ).optional(),
        }
    ).named(renames["ProposalIn"])
    types["ProposalOut"] = t.struct(
        {
            "termsAndConditions": t.string().optional(),
            "billedBuyer": t.proxy(renames["BuyerOut"]).optional(),
            "displayName": t.string().optional(),
            "proposalId": t.string().optional(),
            "lastUpdaterOrCommentorRole": t.string().optional(),
            "updateTime": t.string().optional(),
            "isRenegotiating": t.boolean().optional(),
            "buyerPrivateData": t.proxy(renames["PrivateDataOut"]).optional(),
            "buyer": t.proxy(renames["BuyerOut"]).optional(),
            "originatorRole": t.string().optional(),
            "proposalState": t.string().optional(),
            "sellerContacts": t.array(
                t.proxy(renames["ContactInformationOut"])
            ).optional(),
            "seller": t.proxy(renames["SellerOut"]).optional(),
            "proposalRevision": t.string().optional(),
            "deals": t.array(t.proxy(renames["DealOut"])).optional(),
            "privateAuctionId": t.string().optional(),
            "buyerContacts": t.array(
                t.proxy(renames["ContactInformationOut"])
            ).optional(),
            "isSetupComplete": t.boolean().optional(),
            "notes": t.array(t.proxy(renames["NoteOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProposalOut"])
    types["TechnologyTargetingIn"] = t.struct(
        {
            "deviceCapabilityTargeting": t.proxy(
                renames["CriteriaTargetingIn"]
            ).optional(),
            "operatingSystemTargeting": t.proxy(
                renames["OperatingSystemTargetingIn"]
            ).optional(),
            "deviceCategoryTargeting": t.proxy(
                renames["CriteriaTargetingIn"]
            ).optional(),
        }
    ).named(renames["TechnologyTargetingIn"])
    types["TechnologyTargetingOut"] = t.struct(
        {
            "deviceCapabilityTargeting": t.proxy(
                renames["CriteriaTargetingOut"]
            ).optional(),
            "operatingSystemTargeting": t.proxy(
                renames["OperatingSystemTargetingOut"]
            ).optional(),
            "deviceCategoryTargeting": t.proxy(
                renames["CriteriaTargetingOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TechnologyTargetingOut"])
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
    types["CriteriaTargetingIn"] = t.struct(
        {
            "excludedCriteriaIds": t.array(t.string()).optional(),
            "targetedCriteriaIds": t.array(t.string()).optional(),
        }
    ).named(renames["CriteriaTargetingIn"])
    types["CriteriaTargetingOut"] = t.struct(
        {
            "excludedCriteriaIds": t.array(t.string()).optional(),
            "targetedCriteriaIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CriteriaTargetingOut"])
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
    types["ListCreativeStatusBreakdownByCreativeResponseIn"] = t.struct(
        {
            "filteredBidCreativeRows": t.array(
                t.proxy(renames["FilteredBidCreativeRowIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListCreativeStatusBreakdownByCreativeResponseIn"])
    types["ListCreativeStatusBreakdownByCreativeResponseOut"] = t.struct(
        {
            "filteredBidCreativeRows": t.array(
                t.proxy(renames["FilteredBidCreativeRowOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCreativeStatusBreakdownByCreativeResponseOut"])
    types["AbsoluteDateRangeIn"] = t.struct(
        {
            "startDate": t.proxy(renames["DateIn"]).optional(),
            "endDate": t.proxy(renames["DateIn"]).optional(),
        }
    ).named(renames["AbsoluteDateRangeIn"])
    types["AbsoluteDateRangeOut"] = t.struct(
        {
            "startDate": t.proxy(renames["DateOut"]).optional(),
            "endDate": t.proxy(renames["DateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AbsoluteDateRangeOut"])
    types["PublisherProfileMobileApplicationIn"] = t.struct(
        {
            "appStore": t.string().optional(),
            "name": t.string().optional(),
            "externalAppId": t.string().optional(),
        }
    ).named(renames["PublisherProfileMobileApplicationIn"])
    types["PublisherProfileMobileApplicationOut"] = t.struct(
        {
            "appStore": t.string().optional(),
            "name": t.string().optional(),
            "externalAppId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublisherProfileMobileApplicationOut"])
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
    types["BidResponseWithoutBidsStatusRowIn"] = t.struct(
        {
            "status": t.string().optional(),
            "impressionCount": t.proxy(renames["MetricValueIn"]).optional(),
            "rowDimensions": t.proxy(renames["RowDimensionsIn"]).optional(),
        }
    ).named(renames["BidResponseWithoutBidsStatusRowIn"])
    types["BidResponseWithoutBidsStatusRowOut"] = t.struct(
        {
            "status": t.string().optional(),
            "impressionCount": t.proxy(renames["MetricValueOut"]).optional(),
            "rowDimensions": t.proxy(renames["RowDimensionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BidResponseWithoutBidsStatusRowOut"])
    types["AddNoteRequestIn"] = t.struct(
        {"note": t.proxy(renames["NoteIn"]).optional()}
    ).named(renames["AddNoteRequestIn"])
    types["AddNoteRequestOut"] = t.struct(
        {
            "note": t.proxy(renames["NoteOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddNoteRequestOut"])
    types["SellerIn"] = t.struct({"accountId": t.string().optional()}).named(
        renames["SellerIn"]
    )
    types["SellerOut"] = t.struct(
        {
            "accountId": t.string().optional(),
            "subAccountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SellerOut"])
    types["ProductIn"] = t.struct(
        {
            "availableStartTime": t.string().optional(),
            "terms": t.proxy(renames["DealTermsIn"]).optional(),
            "seller": t.proxy(renames["SellerIn"]).optional(),
            "targetingCriterion": t.array(
                t.proxy(renames["TargetingCriteriaIn"])
            ).optional(),
            "productRevision": t.string().optional(),
            "publisherProfileId": t.string().optional(),
            "updateTime": t.string().optional(),
            "displayName": t.string().optional(),
            "creatorContacts": t.array(
                t.proxy(renames["ContactInformationIn"])
            ).optional(),
            "availableEndTime": t.string().optional(),
            "createTime": t.string().optional(),
            "hasCreatorSignedOff": t.boolean().optional(),
            "webPropertyCode": t.string().optional(),
            "productId": t.string().optional(),
            "syndicationProduct": t.string().optional(),
        }
    ).named(renames["ProductIn"])
    types["ProductOut"] = t.struct(
        {
            "availableStartTime": t.string().optional(),
            "terms": t.proxy(renames["DealTermsOut"]).optional(),
            "seller": t.proxy(renames["SellerOut"]).optional(),
            "targetingCriterion": t.array(
                t.proxy(renames["TargetingCriteriaOut"])
            ).optional(),
            "productRevision": t.string().optional(),
            "publisherProfileId": t.string().optional(),
            "updateTime": t.string().optional(),
            "displayName": t.string().optional(),
            "creatorContacts": t.array(
                t.proxy(renames["ContactInformationOut"])
            ).optional(),
            "availableEndTime": t.string().optional(),
            "createTime": t.string().optional(),
            "hasCreatorSignedOff": t.boolean().optional(),
            "webPropertyCode": t.string().optional(),
            "productId": t.string().optional(),
            "syndicationProduct": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["CreativeDealAssociationIn"] = t.struct(
        {
            "creativeId": t.string().optional(),
            "dealsId": t.string().optional(),
            "accountId": t.string().optional(),
        }
    ).named(renames["CreativeDealAssociationIn"])
    types["CreativeDealAssociationOut"] = t.struct(
        {
            "creativeId": t.string().optional(),
            "dealsId": t.string().optional(),
            "accountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeDealAssociationOut"])
    types["ListCreativesResponseIn"] = t.struct(
        {
            "creatives": t.array(t.proxy(renames["CreativeIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListCreativesResponseIn"])
    types["ListCreativesResponseOut"] = t.struct(
        {
            "creatives": t.array(t.proxy(renames["CreativeOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCreativesResponseOut"])
    types["InventorySizeTargetingIn"] = t.struct(
        {
            "excludedInventorySizes": t.array(t.proxy(renames["AdSizeIn"])).optional(),
            "targetedInventorySizes": t.array(t.proxy(renames["AdSizeIn"])).optional(),
        }
    ).named(renames["InventorySizeTargetingIn"])
    types["InventorySizeTargetingOut"] = t.struct(
        {
            "excludedInventorySizes": t.array(t.proxy(renames["AdSizeOut"])).optional(),
            "targetedInventorySizes": t.array(t.proxy(renames["AdSizeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventorySizeTargetingOut"])
    types["StopWatchingCreativeRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["StopWatchingCreativeRequestIn"])
    types["StopWatchingCreativeRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StopWatchingCreativeRequestOut"])
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
    types["NonGuaranteedAuctionTermsIn"] = t.struct(
        {
            "reservePricesPerBuyer": t.array(
                t.proxy(renames["PricePerBuyerIn"])
            ).optional(),
            "autoOptimizePrivateAuction": t.boolean().optional(),
        }
    ).named(renames["NonGuaranteedAuctionTermsIn"])
    types["NonGuaranteedAuctionTermsOut"] = t.struct(
        {
            "reservePricesPerBuyer": t.array(
                t.proxy(renames["PricePerBuyerOut"])
            ).optional(),
            "autoOptimizePrivateAuction": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NonGuaranteedAuctionTermsOut"])
    types["GuaranteedFixedPriceTermsIn"] = t.struct(
        {
            "guaranteedImpressions": t.string().optional(),
            "minimumDailyLooks": t.string().optional(),
            "reservationType": t.string().optional(),
            "fixedPrices": t.array(t.proxy(renames["PricePerBuyerIn"])).optional(),
            "guaranteedLooks": t.string().optional(),
            "impressionCap": t.string().optional(),
            "percentShareOfVoice": t.string().optional(),
        }
    ).named(renames["GuaranteedFixedPriceTermsIn"])
    types["GuaranteedFixedPriceTermsOut"] = t.struct(
        {
            "guaranteedImpressions": t.string().optional(),
            "minimumDailyLooks": t.string().optional(),
            "reservationType": t.string().optional(),
            "fixedPrices": t.array(t.proxy(renames["PricePerBuyerOut"])).optional(),
            "guaranteedLooks": t.string().optional(),
            "impressionCap": t.string().optional(),
            "percentShareOfVoice": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GuaranteedFixedPriceTermsOut"])
    types["NonGuaranteedFixedPriceTermsIn"] = t.struct(
        {"fixedPrices": t.array(t.proxy(renames["PricePerBuyerIn"])).optional()}
    ).named(renames["NonGuaranteedFixedPriceTermsIn"])
    types["NonGuaranteedFixedPriceTermsOut"] = t.struct(
        {
            "fixedPrices": t.array(t.proxy(renames["PricePerBuyerOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NonGuaranteedFixedPriceTermsOut"])
    types["CreativeRestrictionsIn"] = t.struct(
        {
            "skippableAdType": t.string().optional(),
            "creativeSpecifications": t.array(
                t.proxy(renames["CreativeSpecificationIn"])
            ),
            "creativeFormat": t.string().optional(),
        }
    ).named(renames["CreativeRestrictionsIn"])
    types["CreativeRestrictionsOut"] = t.struct(
        {
            "skippableAdType": t.string().optional(),
            "creativeSpecifications": t.array(
                t.proxy(renames["CreativeSpecificationOut"])
            ),
            "creativeFormat": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeRestrictionsOut"])
    types["OperatingSystemTargetingIn"] = t.struct(
        {
            "operatingSystemCriteria": t.proxy(
                renames["CriteriaTargetingIn"]
            ).optional(),
            "operatingSystemVersionCriteria": t.proxy(
                renames["CriteriaTargetingIn"]
            ).optional(),
        }
    ).named(renames["OperatingSystemTargetingIn"])
    types["OperatingSystemTargetingOut"] = t.struct(
        {
            "operatingSystemCriteria": t.proxy(
                renames["CriteriaTargetingOut"]
            ).optional(),
            "operatingSystemVersionCriteria": t.proxy(
                renames["CriteriaTargetingOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperatingSystemTargetingOut"])
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
    types["RemoveDealAssociationRequestIn"] = t.struct(
        {"association": t.proxy(renames["CreativeDealAssociationIn"]).optional()}
    ).named(renames["RemoveDealAssociationRequestIn"])
    types["RemoveDealAssociationRequestOut"] = t.struct(
        {
            "association": t.proxy(renames["CreativeDealAssociationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveDealAssociationRequestOut"])
    types["ClientUserIn"] = t.struct(
        {
            "clientAccountId": t.string().optional(),
            "userId": t.string().optional(),
            "email": t.string().optional(),
            "status": t.string().optional(),
        }
    ).named(renames["ClientUserIn"])
    types["ClientUserOut"] = t.struct(
        {
            "clientAccountId": t.string().optional(),
            "userId": t.string().optional(),
            "email": t.string().optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientUserOut"])
    types["DeliveryControlIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeliveryControlIn"]
    )
    types["DeliveryControlOut"] = t.struct(
        {
            "creativeBlockingLevel": t.string().optional(),
            "frequencyCaps": t.array(t.proxy(renames["FrequencyCapOut"])).optional(),
            "deliveryRateType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeliveryControlOut"])
    types["WatchCreativeRequestIn"] = t.struct({"topic": t.string().optional()}).named(
        renames["WatchCreativeRequestIn"]
    )
    types["WatchCreativeRequestOut"] = t.struct(
        {
            "topic": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WatchCreativeRequestOut"])
    types["AuctionContextIn"] = t.struct(
        {"auctionTypes": t.array(t.string()).optional()}
    ).named(renames["AuctionContextIn"])
    types["AuctionContextOut"] = t.struct(
        {
            "auctionTypes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuctionContextOut"])
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
    types["MoneyIn"] = t.struct(
        {
            "units": t.string().optional(),
            "currencyCode": t.string().optional(),
            "nanos": t.integer().optional(),
        }
    ).named(renames["MoneyIn"])
    types["MoneyOut"] = t.struct(
        {
            "units": t.string().optional(),
            "currencyCode": t.string().optional(),
            "nanos": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoneyOut"])
    types["DealTermsIn"] = t.struct(
        {
            "estimatedGrossSpend": t.proxy(renames["PriceIn"]).optional(),
            "description": t.string().optional(),
            "estimatedImpressionsPerDay": t.string().optional(),
            "nonGuaranteedAuctionTerms": t.proxy(
                renames["NonGuaranteedAuctionTermsIn"]
            ).optional(),
            "guaranteedFixedPriceTerms": t.proxy(
                renames["GuaranteedFixedPriceTermsIn"]
            ).optional(),
            "nonGuaranteedFixedPriceTerms": t.proxy(
                renames["NonGuaranteedFixedPriceTermsIn"]
            ).optional(),
            "sellerTimeZone": t.string().optional(),
            "brandingType": t.string().optional(),
        }
    ).named(renames["DealTermsIn"])
    types["DealTermsOut"] = t.struct(
        {
            "estimatedGrossSpend": t.proxy(renames["PriceOut"]).optional(),
            "description": t.string().optional(),
            "estimatedImpressionsPerDay": t.string().optional(),
            "nonGuaranteedAuctionTerms": t.proxy(
                renames["NonGuaranteedAuctionTermsOut"]
            ).optional(),
            "guaranteedFixedPriceTerms": t.proxy(
                renames["GuaranteedFixedPriceTermsOut"]
            ).optional(),
            "nonGuaranteedFixedPriceTerms": t.proxy(
                renames["NonGuaranteedFixedPriceTermsOut"]
            ).optional(),
            "sellerTimeZone": t.string().optional(),
            "brandingType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DealTermsOut"])
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
    types["AdSizeIn"] = t.struct(
        {
            "sizeType": t.string().optional(),
            "height": t.string().optional(),
            "width": t.string().optional(),
        }
    ).named(renames["AdSizeIn"])
    types["AdSizeOut"] = t.struct(
        {
            "sizeType": t.string().optional(),
            "height": t.string().optional(),
            "width": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdSizeOut"])
    types["DealServingMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DealServingMetadataIn"]
    )
    types["DealServingMetadataOut"] = t.struct(
        {
            "dealPauseStatus": t.proxy(renames["DealPauseStatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DealServingMetadataOut"])
    types["LocationContextIn"] = t.struct(
        {"geoCriteriaIds": t.array(t.integer()).optional()}
    ).named(renames["LocationContextIn"])
    types["LocationContextOut"] = t.struct(
        {
            "geoCriteriaIds": t.array(t.integer()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationContextOut"])
    types["AcceptProposalRequestIn"] = t.struct(
        {"proposalRevision": t.string().optional()}
    ).named(renames["AcceptProposalRequestIn"])
    types["AcceptProposalRequestOut"] = t.struct(
        {
            "proposalRevision": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AcceptProposalRequestOut"])
    types["FrequencyCapIn"] = t.struct(
        {
            "timeUnitType": t.string().optional(),
            "maxImpressions": t.integer().optional(),
            "numTimeUnits": t.integer().optional(),
        }
    ).named(renames["FrequencyCapIn"])
    types["FrequencyCapOut"] = t.struct(
        {
            "timeUnitType": t.string().optional(),
            "maxImpressions": t.integer().optional(),
            "numTimeUnits": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FrequencyCapOut"])

    functions = {}
    functions["biddersFilterSetsGet"] = adexchangebuyer2.get(
        "v2beta1/{ownerName}/filterSets",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "ownerName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFilterSetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersFilterSetsCreate"] = adexchangebuyer2.get(
        "v2beta1/{ownerName}/filterSets",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "ownerName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFilterSetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersFilterSetsBidMetricsList"] = adexchangebuyer2.get(
        "v2beta1/{filterSetName}/bidMetrics",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filterSetName": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBidMetricsResponseOut"]),
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
    functions["biddersFilterSetsBidResponsesWithoutBidsList"] = adexchangebuyer2.get(
        "v2beta1/{filterSetName}/bidResponsesWithoutBids",
        t.struct(
            {
                "filterSetName": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBidResponsesWithoutBidsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersFilterSetsLosingBidsList"] = adexchangebuyer2.get(
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
    functions["biddersFilterSetsNonBillableWinningBidsList"] = adexchangebuyer2.get(
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filterSetName": t.string().optional(),
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
                "creativeStatusId": t.integer().optional(),
                "filterSetName": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCreativeStatusBreakdownByDetailResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersFilterSetsBidResponseErrorsList"] = adexchangebuyer2.get(
        "v2beta1/{filterSetName}/bidResponseErrors",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filterSetName": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBidResponseErrorsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersAccountsFilterSetsDelete"] = adexchangebuyer2.get(
        "v2beta1/{ownerName}/filterSets",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "ownerName": t.string().optional(),
                "pageToken": t.string().optional(),
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
                "ownerName": t.string().optional(),
                "pageToken": t.string().optional(),
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
                "ownerName": t.string().optional(),
                "pageToken": t.string().optional(),
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
                "ownerName": t.string().optional(),
                "pageToken": t.string().optional(),
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
                "filterSetName": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBidResponseErrorsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "biddersAccountsFilterSetsBidResponsesWithoutBidsList"
    ] = adexchangebuyer2.get(
        "v2beta1/{filterSetName}/bidResponsesWithoutBids",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filterSetName": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBidResponsesWithoutBidsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "biddersAccountsFilterSetsFilteredBidRequestsList"
    ] = adexchangebuyer2.get(
        "v2beta1/{filterSetName}/filteredBidRequests",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filterSetName": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFilteredBidRequestsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "biddersAccountsFilterSetsNonBillableWinningBidsList"
    ] = adexchangebuyer2.get(
        "v2beta1/{filterSetName}/nonBillableWinningBids",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filterSetName": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListNonBillableWinningBidsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersAccountsFilterSetsFilteredBidsList"] = adexchangebuyer2.get(
        "v2beta1/{filterSetName}/filteredBids",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageSize": t.integer().optional(),
                "filterSetName": t.string().optional(),
                "pageToken": t.string().optional(),
                "creativeStatusId": t.integer().optional(),
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
                "filterSetName": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "creativeStatusId": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCreativeStatusBreakdownByCreativeResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersAccountsFilterSetsLosingBidsList"] = adexchangebuyer2.get(
        "v2beta1/{filterSetName}/losingBids",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filterSetName": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLosingBidsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersAccountsFilterSetsImpressionMetricsList"] = adexchangebuyer2.get(
        "v2beta1/{filterSetName}/impressionMetrics",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filterSetName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListImpressionMetricsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersAccountsFilterSetsBidMetricsList"] = adexchangebuyer2.get(
        "v2beta1/{filterSetName}/bidMetrics",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filterSetName": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBidMetricsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsProductsList"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/products/{productId}",
        t.struct(
            {
                "productId": t.string().optional(),
                "accountId": t.string().optional(),
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
                "productId": t.string().optional(),
                "accountId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsProposalsCancelNegotiation"] = adexchangebuyer2.post(
        "v2beta1/accounts/{accountId}/proposals/{proposalId}:addNote",
        t.struct(
            {
                "accountId": t.string().optional(),
                "proposalId": t.string().optional(),
                "note": t.proxy(renames["NoteIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NoteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsProposalsResume"] = adexchangebuyer2.post(
        "v2beta1/accounts/{accountId}/proposals/{proposalId}:addNote",
        t.struct(
            {
                "accountId": t.string().optional(),
                "proposalId": t.string().optional(),
                "note": t.proxy(renames["NoteIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NoteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsProposalsUpdate"] = adexchangebuyer2.post(
        "v2beta1/accounts/{accountId}/proposals/{proposalId}:addNote",
        t.struct(
            {
                "accountId": t.string().optional(),
                "proposalId": t.string().optional(),
                "note": t.proxy(renames["NoteIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NoteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsProposalsList"] = adexchangebuyer2.post(
        "v2beta1/accounts/{accountId}/proposals/{proposalId}:addNote",
        t.struct(
            {
                "accountId": t.string().optional(),
                "proposalId": t.string().optional(),
                "note": t.proxy(renames["NoteIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NoteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsProposalsPause"] = adexchangebuyer2.post(
        "v2beta1/accounts/{accountId}/proposals/{proposalId}:addNote",
        t.struct(
            {
                "accountId": t.string().optional(),
                "proposalId": t.string().optional(),
                "note": t.proxy(renames["NoteIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NoteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsProposalsCreate"] = adexchangebuyer2.post(
        "v2beta1/accounts/{accountId}/proposals/{proposalId}:addNote",
        t.struct(
            {
                "accountId": t.string().optional(),
                "proposalId": t.string().optional(),
                "note": t.proxy(renames["NoteIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NoteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsProposalsAccept"] = adexchangebuyer2.post(
        "v2beta1/accounts/{accountId}/proposals/{proposalId}:addNote",
        t.struct(
            {
                "accountId": t.string().optional(),
                "proposalId": t.string().optional(),
                "note": t.proxy(renames["NoteIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NoteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsProposalsGet"] = adexchangebuyer2.post(
        "v2beta1/accounts/{accountId}/proposals/{proposalId}:addNote",
        t.struct(
            {
                "accountId": t.string().optional(),
                "proposalId": t.string().optional(),
                "note": t.proxy(renames["NoteIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NoteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsProposalsCompleteSetup"] = adexchangebuyer2.post(
        "v2beta1/accounts/{accountId}/proposals/{proposalId}:addNote",
        t.struct(
            {
                "accountId": t.string().optional(),
                "proposalId": t.string().optional(),
                "note": t.proxy(renames["NoteIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NoteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsProposalsAddNote"] = adexchangebuyer2.post(
        "v2beta1/accounts/{accountId}/proposals/{proposalId}:addNote",
        t.struct(
            {
                "accountId": t.string().optional(),
                "proposalId": t.string().optional(),
                "note": t.proxy(renames["NoteIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NoteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsPublisherProfilesGet"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/publisherProfiles",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "accountId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPublisherProfilesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsPublisherProfilesList"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/publisherProfiles",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "accountId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPublisherProfilesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsClientsGet"] = adexchangebuyer2.put(
        "v2beta1/accounts/{accountId}/clients/{clientAccountId}",
        t.struct(
            {
                "clientAccountId": t.string().optional(),
                "accountId": t.string().optional(),
                "entityId": t.string().optional(),
                "clientName": t.string().optional(),
                "visibleToSeller": t.boolean().optional(),
                "partnerClientId": t.string().optional(),
                "role": t.string().optional(),
                "status": t.string().optional(),
                "entityName": t.string().optional(),
                "entityType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClientOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsClientsCreate"] = adexchangebuyer2.put(
        "v2beta1/accounts/{accountId}/clients/{clientAccountId}",
        t.struct(
            {
                "clientAccountId": t.string().optional(),
                "accountId": t.string().optional(),
                "entityId": t.string().optional(),
                "clientName": t.string().optional(),
                "visibleToSeller": t.boolean().optional(),
                "partnerClientId": t.string().optional(),
                "role": t.string().optional(),
                "status": t.string().optional(),
                "entityName": t.string().optional(),
                "entityType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClientOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsClientsList"] = adexchangebuyer2.put(
        "v2beta1/accounts/{accountId}/clients/{clientAccountId}",
        t.struct(
            {
                "clientAccountId": t.string().optional(),
                "accountId": t.string().optional(),
                "entityId": t.string().optional(),
                "clientName": t.string().optional(),
                "visibleToSeller": t.boolean().optional(),
                "partnerClientId": t.string().optional(),
                "role": t.string().optional(),
                "status": t.string().optional(),
                "entityName": t.string().optional(),
                "entityType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClientOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsClientsUpdate"] = adexchangebuyer2.put(
        "v2beta1/accounts/{accountId}/clients/{clientAccountId}",
        t.struct(
            {
                "clientAccountId": t.string().optional(),
                "accountId": t.string().optional(),
                "entityId": t.string().optional(),
                "clientName": t.string().optional(),
                "visibleToSeller": t.boolean().optional(),
                "partnerClientId": t.string().optional(),
                "role": t.string().optional(),
                "status": t.string().optional(),
                "entityName": t.string().optional(),
                "entityType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClientOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsClientsUsersList"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/clients/{clientAccountId}/users/{userId}",
        t.struct(
            {
                "clientAccountId": t.string().optional(),
                "accountId": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClientUserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsClientsUsersUpdate"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/clients/{clientAccountId}/users/{userId}",
        t.struct(
            {
                "clientAccountId": t.string().optional(),
                "accountId": t.string().optional(),
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
                "clientAccountId": t.string().optional(),
                "accountId": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClientUserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsClientsInvitationsList"] = adexchangebuyer2.post(
        "v2beta1/accounts/{accountId}/clients/{clientAccountId}/invitations",
        t.struct(
            {
                "accountId": t.string().optional(),
                "clientAccountId": t.string().optional(),
                "email": t.string().optional(),
                "invitationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClientUserInvitationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsClientsInvitationsGet"] = adexchangebuyer2.post(
        "v2beta1/accounts/{accountId}/clients/{clientAccountId}/invitations",
        t.struct(
            {
                "accountId": t.string().optional(),
                "clientAccountId": t.string().optional(),
                "email": t.string().optional(),
                "invitationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClientUserInvitationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsClientsInvitationsCreate"] = adexchangebuyer2.post(
        "v2beta1/accounts/{accountId}/clients/{clientAccountId}/invitations",
        t.struct(
            {
                "accountId": t.string().optional(),
                "clientAccountId": t.string().optional(),
                "email": t.string().optional(),
                "invitationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClientUserInvitationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCreativesUpdate"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/creatives/{creativeId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "creativeId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCreativesCreate"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/creatives/{creativeId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "creativeId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCreativesWatch"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/creatives/{creativeId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "creativeId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCreativesList"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/creatives/{creativeId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "creativeId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCreativesStopWatching"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/creatives/{creativeId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "creativeId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCreativesGet"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/creatives/{creativeId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "creativeId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCreativesDealAssociationsRemove"] = adexchangebuyer2.post(
        "v2beta1/accounts/{accountId}/creatives/{creativeId}/dealAssociations:add",
        t.struct(
            {
                "creativeId": t.string().optional(),
                "accountId": t.string().optional(),
                "association": t.proxy(renames["CreativeDealAssociationIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCreativesDealAssociationsList"] = adexchangebuyer2.post(
        "v2beta1/accounts/{accountId}/creatives/{creativeId}/dealAssociations:add",
        t.struct(
            {
                "creativeId": t.string().optional(),
                "accountId": t.string().optional(),
                "association": t.proxy(renames["CreativeDealAssociationIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCreativesDealAssociationsAdd"] = adexchangebuyer2.post(
        "v2beta1/accounts/{accountId}/creatives/{creativeId}/dealAssociations:add",
        t.struct(
            {
                "creativeId": t.string().optional(),
                "accountId": t.string().optional(),
                "association": t.proxy(renames["CreativeDealAssociationIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsFinalizedProposalsList"] = adexchangebuyer2.post(
        "v2beta1/accounts/{accountId}/finalizedProposals/{proposalId}:resume",
        t.struct(
            {
                "accountId": t.string().optional(),
                "proposalId": t.string().optional(),
                "externalDealIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProposalOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsFinalizedProposalsPause"] = adexchangebuyer2.post(
        "v2beta1/accounts/{accountId}/finalizedProposals/{proposalId}:resume",
        t.struct(
            {
                "accountId": t.string().optional(),
                "proposalId": t.string().optional(),
                "externalDealIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProposalOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsFinalizedProposalsResume"] = adexchangebuyer2.post(
        "v2beta1/accounts/{accountId}/finalizedProposals/{proposalId}:resume",
        t.struct(
            {
                "accountId": t.string().optional(),
                "proposalId": t.string().optional(),
                "externalDealIds": t.array(t.string()).optional(),
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
