from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_adexchangebuyer2() -> Import:
    adexchangebuyer2 = HTTPRuntime("https://adexchangebuyer.googleapis.com/")

    renames = {
        "ErrorResponse": "_adexchangebuyer2_1_ErrorResponse",
        "CreativeIn": "_adexchangebuyer2_2_CreativeIn",
        "CreativeOut": "_adexchangebuyer2_3_CreativeOut",
        "ServingContextIn": "_adexchangebuyer2_4_ServingContextIn",
        "ServingContextOut": "_adexchangebuyer2_5_ServingContextOut",
        "CalloutStatusRowIn": "_adexchangebuyer2_6_CalloutStatusRowIn",
        "CalloutStatusRowOut": "_adexchangebuyer2_7_CalloutStatusRowOut",
        "ListBidResponsesWithoutBidsResponseIn": "_adexchangebuyer2_8_ListBidResponsesWithoutBidsResponseIn",
        "ListBidResponsesWithoutBidsResponseOut": "_adexchangebuyer2_9_ListBidResponsesWithoutBidsResponseOut",
        "ListProposalsResponseIn": "_adexchangebuyer2_10_ListProposalsResponseIn",
        "ListProposalsResponseOut": "_adexchangebuyer2_11_ListProposalsResponseOut",
        "CreativeDealAssociationIn": "_adexchangebuyer2_12_CreativeDealAssociationIn",
        "CreativeDealAssociationOut": "_adexchangebuyer2_13_CreativeDealAssociationOut",
        "ListProductsResponseIn": "_adexchangebuyer2_14_ListProductsResponseIn",
        "ListProductsResponseOut": "_adexchangebuyer2_15_ListProductsResponseOut",
        "ListCreativeStatusBreakdownByDetailResponseIn": "_adexchangebuyer2_16_ListCreativeStatusBreakdownByDetailResponseIn",
        "ListCreativeStatusBreakdownByDetailResponseOut": "_adexchangebuyer2_17_ListCreativeStatusBreakdownByDetailResponseOut",
        "UrlTargetingIn": "_adexchangebuyer2_18_UrlTargetingIn",
        "UrlTargetingOut": "_adexchangebuyer2_19_UrlTargetingOut",
        "ServingRestrictionIn": "_adexchangebuyer2_20_ServingRestrictionIn",
        "ServingRestrictionOut": "_adexchangebuyer2_21_ServingRestrictionOut",
        "PauseProposalRequestIn": "_adexchangebuyer2_22_PauseProposalRequestIn",
        "PauseProposalRequestOut": "_adexchangebuyer2_23_PauseProposalRequestOut",
        "ListNonBillableWinningBidsResponseIn": "_adexchangebuyer2_24_ListNonBillableWinningBidsResponseIn",
        "ListNonBillableWinningBidsResponseOut": "_adexchangebuyer2_25_ListNonBillableWinningBidsResponseOut",
        "MarketplaceTargetingIn": "_adexchangebuyer2_26_MarketplaceTargetingIn",
        "MarketplaceTargetingOut": "_adexchangebuyer2_27_MarketplaceTargetingOut",
        "FilteredBidDetailRowIn": "_adexchangebuyer2_28_FilteredBidDetailRowIn",
        "FilteredBidDetailRowOut": "_adexchangebuyer2_29_FilteredBidDetailRowOut",
        "NoteIn": "_adexchangebuyer2_30_NoteIn",
        "NoteOut": "_adexchangebuyer2_31_NoteOut",
        "ListClientUserInvitationsResponseIn": "_adexchangebuyer2_32_ListClientUserInvitationsResponseIn",
        "ListClientUserInvitationsResponseOut": "_adexchangebuyer2_33_ListClientUserInvitationsResponseOut",
        "CreativeStatusRowIn": "_adexchangebuyer2_34_CreativeStatusRowIn",
        "CreativeStatusRowOut": "_adexchangebuyer2_35_CreativeStatusRowOut",
        "GuaranteedFixedPriceTermsIn": "_adexchangebuyer2_36_GuaranteedFixedPriceTermsIn",
        "GuaranteedFixedPriceTermsOut": "_adexchangebuyer2_37_GuaranteedFixedPriceTermsOut",
        "AuctionContextIn": "_adexchangebuyer2_38_AuctionContextIn",
        "AuctionContextOut": "_adexchangebuyer2_39_AuctionContextOut",
        "PublisherProfileMobileApplicationIn": "_adexchangebuyer2_40_PublisherProfileMobileApplicationIn",
        "PublisherProfileMobileApplicationOut": "_adexchangebuyer2_41_PublisherProfileMobileApplicationOut",
        "AcceptProposalRequestIn": "_adexchangebuyer2_42_AcceptProposalRequestIn",
        "AcceptProposalRequestOut": "_adexchangebuyer2_43_AcceptProposalRequestOut",
        "DealIn": "_adexchangebuyer2_44_DealIn",
        "DealOut": "_adexchangebuyer2_45_DealOut",
        "TargetingCriteriaIn": "_adexchangebuyer2_46_TargetingCriteriaIn",
        "TargetingCriteriaOut": "_adexchangebuyer2_47_TargetingCriteriaOut",
        "TimeIntervalIn": "_adexchangebuyer2_48_TimeIntervalIn",
        "TimeIntervalOut": "_adexchangebuyer2_49_TimeIntervalOut",
        "TargetingValueIn": "_adexchangebuyer2_50_TargetingValueIn",
        "TargetingValueOut": "_adexchangebuyer2_51_TargetingValueOut",
        "NativeContentIn": "_adexchangebuyer2_52_NativeContentIn",
        "NativeContentOut": "_adexchangebuyer2_53_NativeContentOut",
        "ListDealAssociationsResponseIn": "_adexchangebuyer2_54_ListDealAssociationsResponseIn",
        "ListDealAssociationsResponseOut": "_adexchangebuyer2_55_ListDealAssociationsResponseOut",
        "MoneyIn": "_adexchangebuyer2_56_MoneyIn",
        "MoneyOut": "_adexchangebuyer2_57_MoneyOut",
        "VideoTargetingIn": "_adexchangebuyer2_58_VideoTargetingIn",
        "VideoTargetingOut": "_adexchangebuyer2_59_VideoTargetingOut",
        "ListClientsResponseIn": "_adexchangebuyer2_60_ListClientsResponseIn",
        "ListClientsResponseOut": "_adexchangebuyer2_61_ListClientsResponseOut",
        "DealPauseStatusIn": "_adexchangebuyer2_62_DealPauseStatusIn",
        "DealPauseStatusOut": "_adexchangebuyer2_63_DealPauseStatusOut",
        "ProposalIn": "_adexchangebuyer2_64_ProposalIn",
        "ProposalOut": "_adexchangebuyer2_65_ProposalOut",
        "ClientUserIn": "_adexchangebuyer2_66_ClientUserIn",
        "ClientUserOut": "_adexchangebuyer2_67_ClientUserOut",
        "SizeIn": "_adexchangebuyer2_68_SizeIn",
        "SizeOut": "_adexchangebuyer2_69_SizeOut",
        "DealTermsIn": "_adexchangebuyer2_70_DealTermsIn",
        "DealTermsOut": "_adexchangebuyer2_71_DealTermsOut",
        "PriceIn": "_adexchangebuyer2_72_PriceIn",
        "PriceOut": "_adexchangebuyer2_73_PriceOut",
        "TimeOfDayIn": "_adexchangebuyer2_74_TimeOfDayIn",
        "TimeOfDayOut": "_adexchangebuyer2_75_TimeOfDayOut",
        "CreativeSpecificationIn": "_adexchangebuyer2_76_CreativeSpecificationIn",
        "CreativeSpecificationOut": "_adexchangebuyer2_77_CreativeSpecificationOut",
        "ImageIn": "_adexchangebuyer2_78_ImageIn",
        "ImageOut": "_adexchangebuyer2_79_ImageOut",
        "DayPartTargetingIn": "_adexchangebuyer2_80_DayPartTargetingIn",
        "DayPartTargetingOut": "_adexchangebuyer2_81_DayPartTargetingOut",
        "DealServingMetadataIn": "_adexchangebuyer2_82_DealServingMetadataIn",
        "DealServingMetadataOut": "_adexchangebuyer2_83_DealServingMetadataOut",
        "RemoveDealAssociationRequestIn": "_adexchangebuyer2_84_RemoveDealAssociationRequestIn",
        "RemoveDealAssociationRequestOut": "_adexchangebuyer2_85_RemoveDealAssociationRequestOut",
        "VideoContentIn": "_adexchangebuyer2_86_VideoContentIn",
        "VideoContentOut": "_adexchangebuyer2_87_VideoContentOut",
        "FrequencyCapIn": "_adexchangebuyer2_88_FrequencyCapIn",
        "FrequencyCapOut": "_adexchangebuyer2_89_FrequencyCapOut",
        "ListImpressionMetricsResponseIn": "_adexchangebuyer2_90_ListImpressionMetricsResponseIn",
        "ListImpressionMetricsResponseOut": "_adexchangebuyer2_91_ListImpressionMetricsResponseOut",
        "NonGuaranteedAuctionTermsIn": "_adexchangebuyer2_92_NonGuaranteedAuctionTermsIn",
        "NonGuaranteedAuctionTermsOut": "_adexchangebuyer2_93_NonGuaranteedAuctionTermsOut",
        "LocationContextIn": "_adexchangebuyer2_94_LocationContextIn",
        "LocationContextOut": "_adexchangebuyer2_95_LocationContextOut",
        "AppContextIn": "_adexchangebuyer2_96_AppContextIn",
        "AppContextOut": "_adexchangebuyer2_97_AppContextOut",
        "ListFilteredBidsResponseIn": "_adexchangebuyer2_98_ListFilteredBidsResponseIn",
        "ListFilteredBidsResponseOut": "_adexchangebuyer2_99_ListFilteredBidsResponseOut",
        "ResumeProposalRequestIn": "_adexchangebuyer2_100_ResumeProposalRequestIn",
        "ResumeProposalRequestOut": "_adexchangebuyer2_101_ResumeProposalRequestOut",
        "CompleteSetupRequestIn": "_adexchangebuyer2_102_CompleteSetupRequestIn",
        "CompleteSetupRequestOut": "_adexchangebuyer2_103_CompleteSetupRequestOut",
        "ListCreativesResponseIn": "_adexchangebuyer2_104_ListCreativesResponseIn",
        "ListCreativesResponseOut": "_adexchangebuyer2_105_ListCreativesResponseOut",
        "ResumeProposalDealsRequestIn": "_adexchangebuyer2_106_ResumeProposalDealsRequestIn",
        "ResumeProposalDealsRequestOut": "_adexchangebuyer2_107_ResumeProposalDealsRequestOut",
        "PricePerBuyerIn": "_adexchangebuyer2_108_PricePerBuyerIn",
        "PricePerBuyerOut": "_adexchangebuyer2_109_PricePerBuyerOut",
        "TechnologyTargetingIn": "_adexchangebuyer2_110_TechnologyTargetingIn",
        "TechnologyTargetingOut": "_adexchangebuyer2_111_TechnologyTargetingOut",
        "NonGuaranteedFixedPriceTermsIn": "_adexchangebuyer2_112_NonGuaranteedFixedPriceTermsIn",
        "NonGuaranteedFixedPriceTermsOut": "_adexchangebuyer2_113_NonGuaranteedFixedPriceTermsOut",
        "CancelNegotiationRequestIn": "_adexchangebuyer2_114_CancelNegotiationRequestIn",
        "CancelNegotiationRequestOut": "_adexchangebuyer2_115_CancelNegotiationRequestOut",
        "PlatformContextIn": "_adexchangebuyer2_116_PlatformContextIn",
        "PlatformContextOut": "_adexchangebuyer2_117_PlatformContextOut",
        "FilteredBidCreativeRowIn": "_adexchangebuyer2_118_FilteredBidCreativeRowIn",
        "FilteredBidCreativeRowOut": "_adexchangebuyer2_119_FilteredBidCreativeRowOut",
        "ClientIn": "_adexchangebuyer2_120_ClientIn",
        "ClientOut": "_adexchangebuyer2_121_ClientOut",
        "PlacementTargetingIn": "_adexchangebuyer2_122_PlacementTargetingIn",
        "PlacementTargetingOut": "_adexchangebuyer2_123_PlacementTargetingOut",
        "ListBidMetricsResponseIn": "_adexchangebuyer2_124_ListBidMetricsResponseIn",
        "ListBidMetricsResponseOut": "_adexchangebuyer2_125_ListBidMetricsResponseOut",
        "SellerIn": "_adexchangebuyer2_126_SellerIn",
        "SellerOut": "_adexchangebuyer2_127_SellerOut",
        "CorrectionIn": "_adexchangebuyer2_128_CorrectionIn",
        "CorrectionOut": "_adexchangebuyer2_129_CorrectionOut",
        "WatchCreativeRequestIn": "_adexchangebuyer2_130_WatchCreativeRequestIn",
        "WatchCreativeRequestOut": "_adexchangebuyer2_131_WatchCreativeRequestOut",
        "AddDealAssociationRequestIn": "_adexchangebuyer2_132_AddDealAssociationRequestIn",
        "AddDealAssociationRequestOut": "_adexchangebuyer2_133_AddDealAssociationRequestOut",
        "BidResponseWithoutBidsStatusRowIn": "_adexchangebuyer2_134_BidResponseWithoutBidsStatusRowIn",
        "BidResponseWithoutBidsStatusRowOut": "_adexchangebuyer2_135_BidResponseWithoutBidsStatusRowOut",
        "ClientUserInvitationIn": "_adexchangebuyer2_136_ClientUserInvitationIn",
        "ClientUserInvitationOut": "_adexchangebuyer2_137_ClientUserInvitationOut",
        "DayPartIn": "_adexchangebuyer2_138_DayPartIn",
        "DayPartOut": "_adexchangebuyer2_139_DayPartOut",
        "ProductIn": "_adexchangebuyer2_140_ProductIn",
        "ProductOut": "_adexchangebuyer2_141_ProductOut",
        "ListBidResponseErrorsResponseIn": "_adexchangebuyer2_142_ListBidResponseErrorsResponseIn",
        "ListBidResponseErrorsResponseOut": "_adexchangebuyer2_143_ListBidResponseErrorsResponseOut",
        "EmptyIn": "_adexchangebuyer2_144_EmptyIn",
        "EmptyOut": "_adexchangebuyer2_145_EmptyOut",
        "AdSizeIn": "_adexchangebuyer2_146_AdSizeIn",
        "AdSizeOut": "_adexchangebuyer2_147_AdSizeOut",
        "ListCreativeStatusBreakdownByCreativeResponseIn": "_adexchangebuyer2_148_ListCreativeStatusBreakdownByCreativeResponseIn",
        "ListCreativeStatusBreakdownByCreativeResponseOut": "_adexchangebuyer2_149_ListCreativeStatusBreakdownByCreativeResponseOut",
        "BidMetricsRowIn": "_adexchangebuyer2_150_BidMetricsRowIn",
        "BidMetricsRowOut": "_adexchangebuyer2_151_BidMetricsRowOut",
        "ListFilterSetsResponseIn": "_adexchangebuyer2_152_ListFilterSetsResponseIn",
        "ListFilterSetsResponseOut": "_adexchangebuyer2_153_ListFilterSetsResponseOut",
        "CriteriaTargetingIn": "_adexchangebuyer2_154_CriteriaTargetingIn",
        "CriteriaTargetingOut": "_adexchangebuyer2_155_CriteriaTargetingOut",
        "RowDimensionsIn": "_adexchangebuyer2_156_RowDimensionsIn",
        "RowDimensionsOut": "_adexchangebuyer2_157_RowDimensionsOut",
        "AddNoteRequestIn": "_adexchangebuyer2_158_AddNoteRequestIn",
        "AddNoteRequestOut": "_adexchangebuyer2_159_AddNoteRequestOut",
        "ListFilteredBidRequestsResponseIn": "_adexchangebuyer2_160_ListFilteredBidRequestsResponseIn",
        "ListFilteredBidRequestsResponseOut": "_adexchangebuyer2_161_ListFilteredBidRequestsResponseOut",
        "AbsoluteDateRangeIn": "_adexchangebuyer2_162_AbsoluteDateRangeIn",
        "AbsoluteDateRangeOut": "_adexchangebuyer2_163_AbsoluteDateRangeOut",
        "ContactInformationIn": "_adexchangebuyer2_164_ContactInformationIn",
        "ContactInformationOut": "_adexchangebuyer2_165_ContactInformationOut",
        "RelativeDateRangeIn": "_adexchangebuyer2_166_RelativeDateRangeIn",
        "RelativeDateRangeOut": "_adexchangebuyer2_167_RelativeDateRangeOut",
        "PublisherProfileIn": "_adexchangebuyer2_168_PublisherProfileIn",
        "PublisherProfileOut": "_adexchangebuyer2_169_PublisherProfileOut",
        "ListLosingBidsResponseIn": "_adexchangebuyer2_170_ListLosingBidsResponseIn",
        "ListLosingBidsResponseOut": "_adexchangebuyer2_171_ListLosingBidsResponseOut",
        "ListClientUsersResponseIn": "_adexchangebuyer2_172_ListClientUsersResponseIn",
        "ListClientUsersResponseOut": "_adexchangebuyer2_173_ListClientUsersResponseOut",
        "DateIn": "_adexchangebuyer2_174_DateIn",
        "DateOut": "_adexchangebuyer2_175_DateOut",
        "FilterSetIn": "_adexchangebuyer2_176_FilterSetIn",
        "FilterSetOut": "_adexchangebuyer2_177_FilterSetOut",
        "CreativeSizeIn": "_adexchangebuyer2_178_CreativeSizeIn",
        "CreativeSizeOut": "_adexchangebuyer2_179_CreativeSizeOut",
        "MetricValueIn": "_adexchangebuyer2_180_MetricValueIn",
        "MetricValueOut": "_adexchangebuyer2_181_MetricValueOut",
        "ListPublisherProfilesResponseIn": "_adexchangebuyer2_182_ListPublisherProfilesResponseIn",
        "ListPublisherProfilesResponseOut": "_adexchangebuyer2_183_ListPublisherProfilesResponseOut",
        "InventorySizeTargetingIn": "_adexchangebuyer2_184_InventorySizeTargetingIn",
        "InventorySizeTargetingOut": "_adexchangebuyer2_185_InventorySizeTargetingOut",
        "AdTechnologyProvidersIn": "_adexchangebuyer2_186_AdTechnologyProvidersIn",
        "AdTechnologyProvidersOut": "_adexchangebuyer2_187_AdTechnologyProvidersOut",
        "PauseProposalDealsRequestIn": "_adexchangebuyer2_188_PauseProposalDealsRequestIn",
        "PauseProposalDealsRequestOut": "_adexchangebuyer2_189_PauseProposalDealsRequestOut",
        "OperatingSystemTargetingIn": "_adexchangebuyer2_190_OperatingSystemTargetingIn",
        "OperatingSystemTargetingOut": "_adexchangebuyer2_191_OperatingSystemTargetingOut",
        "ImpressionMetricsRowIn": "_adexchangebuyer2_192_ImpressionMetricsRowIn",
        "ImpressionMetricsRowOut": "_adexchangebuyer2_193_ImpressionMetricsRowOut",
        "BuyerIn": "_adexchangebuyer2_194_BuyerIn",
        "BuyerOut": "_adexchangebuyer2_195_BuyerOut",
        "NonBillableWinningBidStatusRowIn": "_adexchangebuyer2_196_NonBillableWinningBidStatusRowIn",
        "NonBillableWinningBidStatusRowOut": "_adexchangebuyer2_197_NonBillableWinningBidStatusRowOut",
        "HtmlContentIn": "_adexchangebuyer2_198_HtmlContentIn",
        "HtmlContentOut": "_adexchangebuyer2_199_HtmlContentOut",
        "DisapprovalIn": "_adexchangebuyer2_200_DisapprovalIn",
        "DisapprovalOut": "_adexchangebuyer2_201_DisapprovalOut",
        "DeliveryControlIn": "_adexchangebuyer2_202_DeliveryControlIn",
        "DeliveryControlOut": "_adexchangebuyer2_203_DeliveryControlOut",
        "RealtimeTimeRangeIn": "_adexchangebuyer2_204_RealtimeTimeRangeIn",
        "RealtimeTimeRangeOut": "_adexchangebuyer2_205_RealtimeTimeRangeOut",
        "StopWatchingCreativeRequestIn": "_adexchangebuyer2_206_StopWatchingCreativeRequestIn",
        "StopWatchingCreativeRequestOut": "_adexchangebuyer2_207_StopWatchingCreativeRequestOut",
        "MobileApplicationTargetingIn": "_adexchangebuyer2_208_MobileApplicationTargetingIn",
        "MobileApplicationTargetingOut": "_adexchangebuyer2_209_MobileApplicationTargetingOut",
        "SecurityContextIn": "_adexchangebuyer2_210_SecurityContextIn",
        "SecurityContextOut": "_adexchangebuyer2_211_SecurityContextOut",
        "CreativeRestrictionsIn": "_adexchangebuyer2_212_CreativeRestrictionsIn",
        "CreativeRestrictionsOut": "_adexchangebuyer2_213_CreativeRestrictionsOut",
        "FirstPartyMobileApplicationTargetingIn": "_adexchangebuyer2_214_FirstPartyMobileApplicationTargetingIn",
        "FirstPartyMobileApplicationTargetingOut": "_adexchangebuyer2_215_FirstPartyMobileApplicationTargetingOut",
        "PrivateDataIn": "_adexchangebuyer2_216_PrivateDataIn",
        "PrivateDataOut": "_adexchangebuyer2_217_PrivateDataOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["CreativeIn"] = t.struct(
        {
            "impressionTrackingUrls": t.array(t.string()).optional(),
            "creativeId": t.string().optional(),
            "agencyId": t.string().optional(),
            "attributes": t.array(t.string()).optional(),
            "declaredClickThroughUrls": t.array(t.string()).optional(),
            "adChoicesDestinationUrl": t.string().optional(),
            "apiUpdateTime": t.string().optional(),
            "dealsStatus": t.string().optional(),
            "detectedAdvertiserIds": t.array(t.string()).optional(),
            "accountId": t.string().optional(),
            "corrections": t.array(t.proxy(renames["CorrectionIn"])).optional(),
            "adTechnologyProviders": t.proxy(
                renames["AdTechnologyProvidersIn"]
            ).optional(),
            "servingRestrictions": t.array(
                t.proxy(renames["ServingRestrictionIn"])
            ).optional(),
            "advertiserName": t.string().optional(),
            "detectedLanguages": t.array(t.string()).optional(),
            "vendorIds": t.array(t.integer()).optional(),
            "detectedDomains": t.array(t.string()).optional(),
            "version": t.integer().optional(),
            "openAuctionStatus": t.string().optional(),
            "video": t.proxy(renames["VideoContentIn"]).optional(),
            "restrictedCategories": t.array(t.string()).optional(),
            "html": t.proxy(renames["HtmlContentIn"]).optional(),
            "native": t.proxy(renames["NativeContentIn"]).optional(),
            "detectedSensitiveCategories": t.array(t.integer()).optional(),
            "detectedProductCategories": t.array(t.integer()).optional(),
            "clickThroughUrls": t.array(t.string()).optional(),
        }
    ).named(renames["CreativeIn"])
    types["CreativeOut"] = t.struct(
        {
            "impressionTrackingUrls": t.array(t.string()).optional(),
            "creativeId": t.string().optional(),
            "agencyId": t.string().optional(),
            "attributes": t.array(t.string()).optional(),
            "declaredClickThroughUrls": t.array(t.string()).optional(),
            "adChoicesDestinationUrl": t.string().optional(),
            "apiUpdateTime": t.string().optional(),
            "dealsStatus": t.string().optional(),
            "detectedAdvertiserIds": t.array(t.string()).optional(),
            "accountId": t.string().optional(),
            "corrections": t.array(t.proxy(renames["CorrectionOut"])).optional(),
            "adTechnologyProviders": t.proxy(
                renames["AdTechnologyProvidersOut"]
            ).optional(),
            "servingRestrictions": t.array(
                t.proxy(renames["ServingRestrictionOut"])
            ).optional(),
            "advertiserName": t.string().optional(),
            "detectedLanguages": t.array(t.string()).optional(),
            "vendorIds": t.array(t.integer()).optional(),
            "detectedDomains": t.array(t.string()).optional(),
            "version": t.integer().optional(),
            "openAuctionStatus": t.string().optional(),
            "video": t.proxy(renames["VideoContentOut"]).optional(),
            "restrictedCategories": t.array(t.string()).optional(),
            "html": t.proxy(renames["HtmlContentOut"]).optional(),
            "native": t.proxy(renames["NativeContentOut"]).optional(),
            "detectedSensitiveCategories": t.array(t.integer()).optional(),
            "detectedProductCategories": t.array(t.integer()).optional(),
            "clickThroughUrls": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeOut"])
    types["ServingContextIn"] = t.struct(
        {
            "appType": t.proxy(renames["AppContextIn"]).optional(),
            "all": t.string().optional(),
            "auctionType": t.proxy(renames["AuctionContextIn"]).optional(),
            "securityType": t.proxy(renames["SecurityContextIn"]).optional(),
            "platform": t.proxy(renames["PlatformContextIn"]).optional(),
            "location": t.proxy(renames["LocationContextIn"]).optional(),
        }
    ).named(renames["ServingContextIn"])
    types["ServingContextOut"] = t.struct(
        {
            "appType": t.proxy(renames["AppContextOut"]).optional(),
            "all": t.string().optional(),
            "auctionType": t.proxy(renames["AuctionContextOut"]).optional(),
            "securityType": t.proxy(renames["SecurityContextOut"]).optional(),
            "platform": t.proxy(renames["PlatformContextOut"]).optional(),
            "location": t.proxy(renames["LocationContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServingContextOut"])
    types["CalloutStatusRowIn"] = t.struct(
        {
            "calloutStatusId": t.integer().optional(),
            "rowDimensions": t.proxy(renames["RowDimensionsIn"]).optional(),
            "impressionCount": t.proxy(renames["MetricValueIn"]).optional(),
        }
    ).named(renames["CalloutStatusRowIn"])
    types["CalloutStatusRowOut"] = t.struct(
        {
            "calloutStatusId": t.integer().optional(),
            "rowDimensions": t.proxy(renames["RowDimensionsOut"]).optional(),
            "impressionCount": t.proxy(renames["MetricValueOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CalloutStatusRowOut"])
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
    types["CreativeDealAssociationIn"] = t.struct(
        {
            "dealsId": t.string().optional(),
            "accountId": t.string().optional(),
            "creativeId": t.string().optional(),
        }
    ).named(renames["CreativeDealAssociationIn"])
    types["CreativeDealAssociationOut"] = t.struct(
        {
            "dealsId": t.string().optional(),
            "accountId": t.string().optional(),
            "creativeId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeDealAssociationOut"])
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
    types["ListCreativeStatusBreakdownByDetailResponseIn"] = t.struct(
        {
            "detailType": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "filteredBidDetailRows": t.array(
                t.proxy(renames["FilteredBidDetailRowIn"])
            ).optional(),
        }
    ).named(renames["ListCreativeStatusBreakdownByDetailResponseIn"])
    types["ListCreativeStatusBreakdownByDetailResponseOut"] = t.struct(
        {
            "detailType": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "filteredBidDetailRows": t.array(
                t.proxy(renames["FilteredBidDetailRowOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCreativeStatusBreakdownByDetailResponseOut"])
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
    types["ServingRestrictionIn"] = t.struct(
        {
            "disapproval": t.proxy(renames["DisapprovalIn"]).optional(),
            "contexts": t.array(t.proxy(renames["ServingContextIn"])).optional(),
            "disapprovalReasons": t.array(t.proxy(renames["DisapprovalIn"])).optional(),
            "status": t.string().optional(),
        }
    ).named(renames["ServingRestrictionIn"])
    types["ServingRestrictionOut"] = t.struct(
        {
            "disapproval": t.proxy(renames["DisapprovalOut"]).optional(),
            "contexts": t.array(t.proxy(renames["ServingContextOut"])).optional(),
            "disapprovalReasons": t.array(
                t.proxy(renames["DisapprovalOut"])
            ).optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServingRestrictionOut"])
    types["PauseProposalRequestIn"] = t.struct({"reason": t.string().optional()}).named(
        renames["PauseProposalRequestIn"]
    )
    types["PauseProposalRequestOut"] = t.struct(
        {
            "reason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PauseProposalRequestOut"])
    types["ListNonBillableWinningBidsResponseIn"] = t.struct(
        {
            "nonBillableWinningBidStatusRows": t.array(
                t.proxy(renames["NonBillableWinningBidStatusRowIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListNonBillableWinningBidsResponseIn"])
    types["ListNonBillableWinningBidsResponseOut"] = t.struct(
        {
            "nonBillableWinningBidStatusRows": t.array(
                t.proxy(renames["NonBillableWinningBidStatusRowOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListNonBillableWinningBidsResponseOut"])
    types["MarketplaceTargetingIn"] = t.struct(
        {
            "technologyTargeting": t.proxy(renames["TechnologyTargetingIn"]).optional(),
            "videoTargeting": t.proxy(renames["VideoTargetingIn"]).optional(),
            "geoTargeting": t.proxy(renames["CriteriaTargetingIn"]).optional(),
            "inventorySizeTargeting": t.proxy(
                renames["InventorySizeTargetingIn"]
            ).optional(),
            "placementTargeting": t.proxy(renames["PlacementTargetingIn"]).optional(),
        }
    ).named(renames["MarketplaceTargetingIn"])
    types["MarketplaceTargetingOut"] = t.struct(
        {
            "technologyTargeting": t.proxy(
                renames["TechnologyTargetingOut"]
            ).optional(),
            "videoTargeting": t.proxy(renames["VideoTargetingOut"]).optional(),
            "geoTargeting": t.proxy(renames["CriteriaTargetingOut"]).optional(),
            "inventorySizeTargeting": t.proxy(
                renames["InventorySizeTargetingOut"]
            ).optional(),
            "placementTargeting": t.proxy(renames["PlacementTargetingOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MarketplaceTargetingOut"])
    types["FilteredBidDetailRowIn"] = t.struct(
        {
            "bidCount": t.proxy(renames["MetricValueIn"]).optional(),
            "rowDimensions": t.proxy(renames["RowDimensionsIn"]).optional(),
            "detail": t.string().optional(),
            "detailId": t.integer().optional(),
        }
    ).named(renames["FilteredBidDetailRowIn"])
    types["FilteredBidDetailRowOut"] = t.struct(
        {
            "bidCount": t.proxy(renames["MetricValueOut"]).optional(),
            "rowDimensions": t.proxy(renames["RowDimensionsOut"]).optional(),
            "detail": t.string().optional(),
            "detailId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilteredBidDetailRowOut"])
    types["NoteIn"] = t.struct({"note": t.string().optional()}).named(renames["NoteIn"])
    types["NoteOut"] = t.struct(
        {
            "creatorRole": t.string().optional(),
            "noteId": t.string().optional(),
            "proposalRevision": t.string().optional(),
            "note": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NoteOut"])
    types["ListClientUserInvitationsResponseIn"] = t.struct(
        {
            "invitations": t.array(
                t.proxy(renames["ClientUserInvitationIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListClientUserInvitationsResponseIn"])
    types["ListClientUserInvitationsResponseOut"] = t.struct(
        {
            "invitations": t.array(
                t.proxy(renames["ClientUserInvitationOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListClientUserInvitationsResponseOut"])
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
    types["GuaranteedFixedPriceTermsIn"] = t.struct(
        {
            "impressionCap": t.string().optional(),
            "fixedPrices": t.array(t.proxy(renames["PricePerBuyerIn"])).optional(),
            "percentShareOfVoice": t.string().optional(),
            "reservationType": t.string().optional(),
            "minimumDailyLooks": t.string().optional(),
            "guaranteedImpressions": t.string().optional(),
            "guaranteedLooks": t.string().optional(),
        }
    ).named(renames["GuaranteedFixedPriceTermsIn"])
    types["GuaranteedFixedPriceTermsOut"] = t.struct(
        {
            "impressionCap": t.string().optional(),
            "fixedPrices": t.array(t.proxy(renames["PricePerBuyerOut"])).optional(),
            "percentShareOfVoice": t.string().optional(),
            "reservationType": t.string().optional(),
            "minimumDailyLooks": t.string().optional(),
            "guaranteedImpressions": t.string().optional(),
            "guaranteedLooks": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GuaranteedFixedPriceTermsOut"])
    types["AuctionContextIn"] = t.struct(
        {"auctionTypes": t.array(t.string()).optional()}
    ).named(renames["AuctionContextIn"])
    types["AuctionContextOut"] = t.struct(
        {
            "auctionTypes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuctionContextOut"])
    types["PublisherProfileMobileApplicationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "externalAppId": t.string().optional(),
            "appStore": t.string().optional(),
        }
    ).named(renames["PublisherProfileMobileApplicationIn"])
    types["PublisherProfileMobileApplicationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "externalAppId": t.string().optional(),
            "appStore": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublisherProfileMobileApplicationOut"])
    types["AcceptProposalRequestIn"] = t.struct(
        {"proposalRevision": t.string().optional()}
    ).named(renames["AcceptProposalRequestIn"])
    types["AcceptProposalRequestOut"] = t.struct(
        {
            "proposalRevision": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AcceptProposalRequestOut"])
    types["DealIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "deliveryControl": t.proxy(renames["DeliveryControlIn"]).optional(),
            "availableEndTime": t.string().optional(),
            "availableStartTime": t.string().optional(),
            "dealTerms": t.proxy(renames["DealTermsIn"]).optional(),
            "syndicationProduct": t.string().optional(),
            "createProductId": t.string().optional(),
            "webPropertyCode": t.string().optional(),
            "buyerPrivateData": t.proxy(renames["PrivateDataIn"]).optional(),
            "createProductRevision": t.string().optional(),
            "targetingCriterion": t.array(
                t.proxy(renames["TargetingCriteriaIn"])
            ).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["DealIn"])
    types["DealOut"] = t.struct(
        {
            "programmaticCreativeSource": t.string().optional(),
            "creativeRestrictions": t.proxy(
                renames["CreativeRestrictionsOut"]
            ).optional(),
            "proposalId": t.string().optional(),
            "displayName": t.string().optional(),
            "deliveryControl": t.proxy(renames["DeliveryControlOut"]).optional(),
            "targeting": t.proxy(renames["MarketplaceTargetingOut"]).optional(),
            "availableEndTime": t.string().optional(),
            "availableStartTime": t.string().optional(),
            "dealTerms": t.proxy(renames["DealTermsOut"]).optional(),
            "syndicationProduct": t.string().optional(),
            "creativePreApprovalPolicy": t.string().optional(),
            "sellerContacts": t.array(
                t.proxy(renames["ContactInformationOut"])
            ).optional(),
            "updateTime": t.string().optional(),
            "createProductId": t.string().optional(),
            "webPropertyCode": t.string().optional(),
            "dealId": t.string().optional(),
            "createTime": t.string().optional(),
            "creativeSafeFrameCompatibility": t.string().optional(),
            "dealServingMetadata": t.proxy(
                renames["DealServingMetadataOut"]
            ).optional(),
            "externalDealId": t.string().optional(),
            "buyerPrivateData": t.proxy(renames["PrivateDataOut"]).optional(),
            "createProductRevision": t.string().optional(),
            "isSetupComplete": t.boolean().optional(),
            "targetingCriterion": t.array(
                t.proxy(renames["TargetingCriteriaOut"])
            ).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DealOut"])
    types["TargetingCriteriaIn"] = t.struct(
        {
            "inclusions": t.array(t.proxy(renames["TargetingValueIn"])).optional(),
            "key": t.string().optional(),
            "exclusions": t.array(t.proxy(renames["TargetingValueIn"])).optional(),
        }
    ).named(renames["TargetingCriteriaIn"])
    types["TargetingCriteriaOut"] = t.struct(
        {
            "inclusions": t.array(t.proxy(renames["TargetingValueOut"])).optional(),
            "key": t.string().optional(),
            "exclusions": t.array(t.proxy(renames["TargetingValueOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetingCriteriaOut"])
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
    types["TargetingValueIn"] = t.struct(
        {
            "creativeSizeValue": t.proxy(renames["CreativeSizeIn"]).optional(),
            "dayPartTargetingValue": t.proxy(renames["DayPartTargetingIn"]).optional(),
            "stringValue": t.string().optional(),
            "longValue": t.string().optional(),
        }
    ).named(renames["TargetingValueIn"])
    types["TargetingValueOut"] = t.struct(
        {
            "creativeSizeValue": t.proxy(renames["CreativeSizeOut"]).optional(),
            "dayPartTargetingValue": t.proxy(renames["DayPartTargetingOut"]).optional(),
            "stringValue": t.string().optional(),
            "longValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetingValueOut"])
    types["NativeContentIn"] = t.struct(
        {
            "appIcon": t.proxy(renames["ImageIn"]).optional(),
            "clickTrackingUrl": t.string().optional(),
            "body": t.string().optional(),
            "callToAction": t.string().optional(),
            "clickLinkUrl": t.string().optional(),
            "priceDisplayText": t.string().optional(),
            "logo": t.proxy(renames["ImageIn"]).optional(),
            "starRating": t.number().optional(),
            "advertiserName": t.string().optional(),
            "videoUrl": t.string().optional(),
            "image": t.proxy(renames["ImageIn"]).optional(),
            "headline": t.string().optional(),
            "storeUrl": t.string().optional(),
        }
    ).named(renames["NativeContentIn"])
    types["NativeContentOut"] = t.struct(
        {
            "appIcon": t.proxy(renames["ImageOut"]).optional(),
            "clickTrackingUrl": t.string().optional(),
            "body": t.string().optional(),
            "callToAction": t.string().optional(),
            "clickLinkUrl": t.string().optional(),
            "priceDisplayText": t.string().optional(),
            "logo": t.proxy(renames["ImageOut"]).optional(),
            "starRating": t.number().optional(),
            "advertiserName": t.string().optional(),
            "videoUrl": t.string().optional(),
            "image": t.proxy(renames["ImageOut"]).optional(),
            "headline": t.string().optional(),
            "storeUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NativeContentOut"])
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
    types["DealPauseStatusIn"] = t.struct(
        {
            "buyerPauseReason": t.string().optional(),
            "sellerPauseReason": t.string().optional(),
            "hasBuyerPaused": t.boolean().optional(),
            "firstPausedBy": t.string().optional(),
            "hasSellerPaused": t.boolean().optional(),
        }
    ).named(renames["DealPauseStatusIn"])
    types["DealPauseStatusOut"] = t.struct(
        {
            "buyerPauseReason": t.string().optional(),
            "sellerPauseReason": t.string().optional(),
            "hasBuyerPaused": t.boolean().optional(),
            "firstPausedBy": t.string().optional(),
            "hasSellerPaused": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DealPauseStatusOut"])
    types["ProposalIn"] = t.struct(
        {
            "deals": t.array(t.proxy(renames["DealIn"])).optional(),
            "buyerPrivateData": t.proxy(renames["PrivateDataIn"]).optional(),
            "seller": t.proxy(renames["SellerIn"]).optional(),
            "buyerContacts": t.array(
                t.proxy(renames["ContactInformationIn"])
            ).optional(),
            "buyer": t.proxy(renames["BuyerIn"]).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["ProposalIn"])
    types["ProposalOut"] = t.struct(
        {
            "proposalRevision": t.string().optional(),
            "proposalState": t.string().optional(),
            "deals": t.array(t.proxy(renames["DealOut"])).optional(),
            "buyerPrivateData": t.proxy(renames["PrivateDataOut"]).optional(),
            "sellerContacts": t.array(
                t.proxy(renames["ContactInformationOut"])
            ).optional(),
            "billedBuyer": t.proxy(renames["BuyerOut"]).optional(),
            "seller": t.proxy(renames["SellerOut"]).optional(),
            "privateAuctionId": t.string().optional(),
            "buyerContacts": t.array(
                t.proxy(renames["ContactInformationOut"])
            ).optional(),
            "notes": t.array(t.proxy(renames["NoteOut"])).optional(),
            "isSetupComplete": t.boolean().optional(),
            "isRenegotiating": t.boolean().optional(),
            "updateTime": t.string().optional(),
            "proposalId": t.string().optional(),
            "buyer": t.proxy(renames["BuyerOut"]).optional(),
            "lastUpdaterOrCommentorRole": t.string().optional(),
            "originatorRole": t.string().optional(),
            "displayName": t.string().optional(),
            "termsAndConditions": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProposalOut"])
    types["ClientUserIn"] = t.struct(
        {
            "email": t.string().optional(),
            "clientAccountId": t.string().optional(),
            "userId": t.string().optional(),
            "status": t.string().optional(),
        }
    ).named(renames["ClientUserIn"])
    types["ClientUserOut"] = t.struct(
        {
            "email": t.string().optional(),
            "clientAccountId": t.string().optional(),
            "userId": t.string().optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientUserOut"])
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
    types["DealTermsIn"] = t.struct(
        {
            "brandingType": t.string().optional(),
            "estimatedGrossSpend": t.proxy(renames["PriceIn"]).optional(),
            "nonGuaranteedAuctionTerms": t.proxy(
                renames["NonGuaranteedAuctionTermsIn"]
            ).optional(),
            "guaranteedFixedPriceTerms": t.proxy(
                renames["GuaranteedFixedPriceTermsIn"]
            ).optional(),
            "sellerTimeZone": t.string().optional(),
            "nonGuaranteedFixedPriceTerms": t.proxy(
                renames["NonGuaranteedFixedPriceTermsIn"]
            ).optional(),
            "description": t.string().optional(),
            "estimatedImpressionsPerDay": t.string().optional(),
        }
    ).named(renames["DealTermsIn"])
    types["DealTermsOut"] = t.struct(
        {
            "brandingType": t.string().optional(),
            "estimatedGrossSpend": t.proxy(renames["PriceOut"]).optional(),
            "nonGuaranteedAuctionTerms": t.proxy(
                renames["NonGuaranteedAuctionTermsOut"]
            ).optional(),
            "guaranteedFixedPriceTerms": t.proxy(
                renames["GuaranteedFixedPriceTermsOut"]
            ).optional(),
            "sellerTimeZone": t.string().optional(),
            "nonGuaranteedFixedPriceTerms": t.proxy(
                renames["NonGuaranteedFixedPriceTermsOut"]
            ).optional(),
            "description": t.string().optional(),
            "estimatedImpressionsPerDay": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DealTermsOut"])
    types["PriceIn"] = t.struct(
        {
            "pricingType": t.string().optional(),
            "amount": t.proxy(renames["MoneyIn"]).optional(),
        }
    ).named(renames["PriceIn"])
    types["PriceOut"] = t.struct(
        {
            "pricingType": t.string().optional(),
            "amount": t.proxy(renames["MoneyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PriceOut"])
    types["TimeOfDayIn"] = t.struct(
        {
            "minutes": t.integer().optional(),
            "seconds": t.integer().optional(),
            "hours": t.integer().optional(),
            "nanos": t.integer().optional(),
        }
    ).named(renames["TimeOfDayIn"])
    types["TimeOfDayOut"] = t.struct(
        {
            "minutes": t.integer().optional(),
            "seconds": t.integer().optional(),
            "hours": t.integer().optional(),
            "nanos": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeOfDayOut"])
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
    types["ImageIn"] = t.struct(
        {
            "width": t.integer().optional(),
            "url": t.string().optional(),
            "height": t.integer().optional(),
        }
    ).named(renames["ImageIn"])
    types["ImageOut"] = t.struct(
        {
            "width": t.integer().optional(),
            "url": t.string().optional(),
            "height": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageOut"])
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
    types["DealServingMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DealServingMetadataIn"]
    )
    types["DealServingMetadataOut"] = t.struct(
        {
            "dealPauseStatus": t.proxy(renames["DealPauseStatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DealServingMetadataOut"])
    types["RemoveDealAssociationRequestIn"] = t.struct(
        {"association": t.proxy(renames["CreativeDealAssociationIn"]).optional()}
    ).named(renames["RemoveDealAssociationRequestIn"])
    types["RemoveDealAssociationRequestOut"] = t.struct(
        {
            "association": t.proxy(renames["CreativeDealAssociationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveDealAssociationRequestOut"])
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
    types["ListImpressionMetricsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "impressionMetricsRows": t.array(
                t.proxy(renames["ImpressionMetricsRowIn"])
            ).optional(),
        }
    ).named(renames["ListImpressionMetricsResponseIn"])
    types["ListImpressionMetricsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "impressionMetricsRows": t.array(
                t.proxy(renames["ImpressionMetricsRowOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListImpressionMetricsResponseOut"])
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
    types["LocationContextIn"] = t.struct(
        {"geoCriteriaIds": t.array(t.integer()).optional()}
    ).named(renames["LocationContextIn"])
    types["LocationContextOut"] = t.struct(
        {
            "geoCriteriaIds": t.array(t.integer()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationContextOut"])
    types["AppContextIn"] = t.struct(
        {"appTypes": t.array(t.string()).optional()}
    ).named(renames["AppContextIn"])
    types["AppContextOut"] = t.struct(
        {
            "appTypes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppContextOut"])
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
    types["ResumeProposalRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ResumeProposalRequestIn"]
    )
    types["ResumeProposalRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ResumeProposalRequestOut"])
    types["CompleteSetupRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CompleteSetupRequestIn"]
    )
    types["CompleteSetupRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CompleteSetupRequestOut"])
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
    types["ResumeProposalDealsRequestIn"] = t.struct(
        {"externalDealIds": t.array(t.string()).optional()}
    ).named(renames["ResumeProposalDealsRequestIn"])
    types["ResumeProposalDealsRequestOut"] = t.struct(
        {
            "externalDealIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResumeProposalDealsRequestOut"])
    types["PricePerBuyerIn"] = t.struct(
        {
            "buyer": t.proxy(renames["BuyerIn"]).optional(),
            "advertiserIds": t.array(t.string()).optional(),
            "price": t.proxy(renames["PriceIn"]).optional(),
        }
    ).named(renames["PricePerBuyerIn"])
    types["PricePerBuyerOut"] = t.struct(
        {
            "buyer": t.proxy(renames["BuyerOut"]).optional(),
            "advertiserIds": t.array(t.string()).optional(),
            "price": t.proxy(renames["PriceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PricePerBuyerOut"])
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
    types["NonGuaranteedFixedPriceTermsIn"] = t.struct(
        {"fixedPrices": t.array(t.proxy(renames["PricePerBuyerIn"])).optional()}
    ).named(renames["NonGuaranteedFixedPriceTermsIn"])
    types["NonGuaranteedFixedPriceTermsOut"] = t.struct(
        {
            "fixedPrices": t.array(t.proxy(renames["PricePerBuyerOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NonGuaranteedFixedPriceTermsOut"])
    types["CancelNegotiationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelNegotiationRequestIn"]
    )
    types["CancelNegotiationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelNegotiationRequestOut"])
    types["PlatformContextIn"] = t.struct(
        {"platforms": t.array(t.string()).optional()}
    ).named(renames["PlatformContextIn"])
    types["PlatformContextOut"] = t.struct(
        {
            "platforms": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlatformContextOut"])
    types["FilteredBidCreativeRowIn"] = t.struct(
        {
            "rowDimensions": t.proxy(renames["RowDimensionsIn"]).optional(),
            "creativeId": t.string().optional(),
            "bidCount": t.proxy(renames["MetricValueIn"]).optional(),
        }
    ).named(renames["FilteredBidCreativeRowIn"])
    types["FilteredBidCreativeRowOut"] = t.struct(
        {
            "rowDimensions": t.proxy(renames["RowDimensionsOut"]).optional(),
            "creativeId": t.string().optional(),
            "bidCount": t.proxy(renames["MetricValueOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilteredBidCreativeRowOut"])
    types["ClientIn"] = t.struct(
        {
            "role": t.string().optional(),
            "status": t.string().optional(),
            "clientName": t.string().optional(),
            "entityType": t.string().optional(),
            "entityId": t.string().optional(),
            "partnerClientId": t.string().optional(),
            "entityName": t.string().optional(),
            "clientAccountId": t.string().optional(),
            "visibleToSeller": t.boolean().optional(),
        }
    ).named(renames["ClientIn"])
    types["ClientOut"] = t.struct(
        {
            "role": t.string().optional(),
            "status": t.string().optional(),
            "clientName": t.string().optional(),
            "entityType": t.string().optional(),
            "entityId": t.string().optional(),
            "partnerClientId": t.string().optional(),
            "entityName": t.string().optional(),
            "clientAccountId": t.string().optional(),
            "visibleToSeller": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientOut"])
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
    types["WatchCreativeRequestIn"] = t.struct({"topic": t.string().optional()}).named(
        renames["WatchCreativeRequestIn"]
    )
    types["WatchCreativeRequestOut"] = t.struct(
        {
            "topic": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WatchCreativeRequestOut"])
    types["AddDealAssociationRequestIn"] = t.struct(
        {"association": t.proxy(renames["CreativeDealAssociationIn"]).optional()}
    ).named(renames["AddDealAssociationRequestIn"])
    types["AddDealAssociationRequestOut"] = t.struct(
        {
            "association": t.proxy(renames["CreativeDealAssociationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddDealAssociationRequestOut"])
    types["BidResponseWithoutBidsStatusRowIn"] = t.struct(
        {
            "rowDimensions": t.proxy(renames["RowDimensionsIn"]).optional(),
            "status": t.string().optional(),
            "impressionCount": t.proxy(renames["MetricValueIn"]).optional(),
        }
    ).named(renames["BidResponseWithoutBidsStatusRowIn"])
    types["BidResponseWithoutBidsStatusRowOut"] = t.struct(
        {
            "rowDimensions": t.proxy(renames["RowDimensionsOut"]).optional(),
            "status": t.string().optional(),
            "impressionCount": t.proxy(renames["MetricValueOut"]).optional(),
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
    types["DayPartIn"] = t.struct(
        {
            "startTime": t.proxy(renames["TimeOfDayIn"]).optional(),
            "endTime": t.proxy(renames["TimeOfDayIn"]).optional(),
            "dayOfWeek": t.string().optional(),
        }
    ).named(renames["DayPartIn"])
    types["DayPartOut"] = t.struct(
        {
            "startTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "endTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "dayOfWeek": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DayPartOut"])
    types["ProductIn"] = t.struct(
        {
            "webPropertyCode": t.string().optional(),
            "targetingCriterion": t.array(
                t.proxy(renames["TargetingCriteriaIn"])
            ).optional(),
            "displayName": t.string().optional(),
            "hasCreatorSignedOff": t.boolean().optional(),
            "syndicationProduct": t.string().optional(),
            "productRevision": t.string().optional(),
            "terms": t.proxy(renames["DealTermsIn"]).optional(),
            "publisherProfileId": t.string().optional(),
            "createTime": t.string().optional(),
            "availableEndTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "productId": t.string().optional(),
            "availableStartTime": t.string().optional(),
            "seller": t.proxy(renames["SellerIn"]).optional(),
            "creatorContacts": t.array(
                t.proxy(renames["ContactInformationIn"])
            ).optional(),
        }
    ).named(renames["ProductIn"])
    types["ProductOut"] = t.struct(
        {
            "webPropertyCode": t.string().optional(),
            "targetingCriterion": t.array(
                t.proxy(renames["TargetingCriteriaOut"])
            ).optional(),
            "displayName": t.string().optional(),
            "hasCreatorSignedOff": t.boolean().optional(),
            "syndicationProduct": t.string().optional(),
            "productRevision": t.string().optional(),
            "terms": t.proxy(renames["DealTermsOut"]).optional(),
            "publisherProfileId": t.string().optional(),
            "createTime": t.string().optional(),
            "availableEndTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "productId": t.string().optional(),
            "availableStartTime": t.string().optional(),
            "seller": t.proxy(renames["SellerOut"]).optional(),
            "creatorContacts": t.array(
                t.proxy(renames["ContactInformationOut"])
            ).optional(),
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["AdSizeIn"] = t.struct(
        {
            "height": t.string().optional(),
            "width": t.string().optional(),
            "sizeType": t.string().optional(),
        }
    ).named(renames["AdSizeIn"])
    types["AdSizeOut"] = t.struct(
        {
            "height": t.string().optional(),
            "width": t.string().optional(),
            "sizeType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdSizeOut"])
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
    types["BidMetricsRowIn"] = t.struct(
        {
            "bidsInAuction": t.proxy(renames["MetricValueIn"]).optional(),
            "measurableImpressions": t.proxy(renames["MetricValueIn"]).optional(),
            "rowDimensions": t.proxy(renames["RowDimensionsIn"]).optional(),
            "impressionsWon": t.proxy(renames["MetricValueIn"]).optional(),
            "billedImpressions": t.proxy(renames["MetricValueIn"]).optional(),
            "viewableImpressions": t.proxy(renames["MetricValueIn"]).optional(),
            "bids": t.proxy(renames["MetricValueIn"]).optional(),
            "reachedQueries": t.proxy(renames["MetricValueIn"]).optional(),
        }
    ).named(renames["BidMetricsRowIn"])
    types["BidMetricsRowOut"] = t.struct(
        {
            "bidsInAuction": t.proxy(renames["MetricValueOut"]).optional(),
            "measurableImpressions": t.proxy(renames["MetricValueOut"]).optional(),
            "rowDimensions": t.proxy(renames["RowDimensionsOut"]).optional(),
            "impressionsWon": t.proxy(renames["MetricValueOut"]).optional(),
            "billedImpressions": t.proxy(renames["MetricValueOut"]).optional(),
            "viewableImpressions": t.proxy(renames["MetricValueOut"]).optional(),
            "bids": t.proxy(renames["MetricValueOut"]).optional(),
            "reachedQueries": t.proxy(renames["MetricValueOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BidMetricsRowOut"])
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
    types["AddNoteRequestIn"] = t.struct(
        {"note": t.proxy(renames["NoteIn"]).optional()}
    ).named(renames["AddNoteRequestIn"])
    types["AddNoteRequestOut"] = t.struct(
        {
            "note": t.proxy(renames["NoteOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddNoteRequestOut"])
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
    types["RelativeDateRangeIn"] = t.struct(
        {"offsetDays": t.integer().optional(), "durationDays": t.integer().optional()}
    ).named(renames["RelativeDateRangeIn"])
    types["RelativeDateRangeOut"] = t.struct(
        {
            "offsetDays": t.integer().optional(),
            "durationDays": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RelativeDateRangeOut"])
    types["PublisherProfileIn"] = t.struct(
        {
            "buyerPitchStatement": t.string().optional(),
            "samplePageUrl": t.string().optional(),
            "displayName": t.string().optional(),
            "programmaticDealsContact": t.string().optional(),
            "rateCardInfoUrl": t.string().optional(),
            "publisherProfileId": t.string().optional(),
            "seller": t.proxy(renames["SellerIn"]).optional(),
            "topHeadlines": t.array(t.string()).optional(),
            "googlePlusUrl": t.string().optional(),
            "mediaKitUrl": t.string().optional(),
            "directDealsContact": t.string().optional(),
            "overview": t.string().optional(),
            "mobileApps": t.array(
                t.proxy(renames["PublisherProfileMobileApplicationIn"])
            ).optional(),
            "isParent": t.boolean().optional(),
            "audienceDescription": t.string().optional(),
            "logoUrl": t.string().optional(),
            "domains": t.array(t.string()).optional(),
        }
    ).named(renames["PublisherProfileIn"])
    types["PublisherProfileOut"] = t.struct(
        {
            "buyerPitchStatement": t.string().optional(),
            "samplePageUrl": t.string().optional(),
            "displayName": t.string().optional(),
            "programmaticDealsContact": t.string().optional(),
            "rateCardInfoUrl": t.string().optional(),
            "publisherProfileId": t.string().optional(),
            "seller": t.proxy(renames["SellerOut"]).optional(),
            "topHeadlines": t.array(t.string()).optional(),
            "googlePlusUrl": t.string().optional(),
            "mediaKitUrl": t.string().optional(),
            "directDealsContact": t.string().optional(),
            "overview": t.string().optional(),
            "mobileApps": t.array(
                t.proxy(renames["PublisherProfileMobileApplicationOut"])
            ).optional(),
            "isParent": t.boolean().optional(),
            "audienceDescription": t.string().optional(),
            "logoUrl": t.string().optional(),
            "domains": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublisherProfileOut"])
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
    types["FilterSetIn"] = t.struct(
        {
            "environment": t.string().optional(),
            "realtimeTimeRange": t.proxy(renames["RealtimeTimeRangeIn"]).optional(),
            "breakdownDimensions": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "platforms": t.array(t.string()).optional(),
            "publisherIdentifiers": t.array(t.string()).optional(),
            "creativeId": t.string().optional(),
            "absoluteDateRange": t.proxy(renames["AbsoluteDateRangeIn"]).optional(),
            "timeSeriesGranularity": t.string().optional(),
            "format": t.string().optional(),
            "dealId": t.string().optional(),
            "formats": t.array(t.string()).optional(),
            "relativeDateRange": t.proxy(renames["RelativeDateRangeIn"]).optional(),
            "sellerNetworkIds": t.array(t.integer()).optional(),
        }
    ).named(renames["FilterSetIn"])
    types["FilterSetOut"] = t.struct(
        {
            "environment": t.string().optional(),
            "realtimeTimeRange": t.proxy(renames["RealtimeTimeRangeOut"]).optional(),
            "breakdownDimensions": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "platforms": t.array(t.string()).optional(),
            "publisherIdentifiers": t.array(t.string()).optional(),
            "creativeId": t.string().optional(),
            "absoluteDateRange": t.proxy(renames["AbsoluteDateRangeOut"]).optional(),
            "timeSeriesGranularity": t.string().optional(),
            "format": t.string().optional(),
            "dealId": t.string().optional(),
            "formats": t.array(t.string()).optional(),
            "relativeDateRange": t.proxy(renames["RelativeDateRangeOut"]).optional(),
            "sellerNetworkIds": t.array(t.integer()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterSetOut"])
    types["CreativeSizeIn"] = t.struct(
        {
            "nativeTemplate": t.string().optional(),
            "skippableAdType": t.string().optional(),
            "allowedFormats": t.array(t.string()).optional(),
            "companionSizes": t.array(t.proxy(renames["SizeIn"])).optional(),
            "size": t.proxy(renames["SizeIn"]).optional(),
            "creativeSizeType": t.string().optional(),
        }
    ).named(renames["CreativeSizeIn"])
    types["CreativeSizeOut"] = t.struct(
        {
            "nativeTemplate": t.string().optional(),
            "skippableAdType": t.string().optional(),
            "allowedFormats": t.array(t.string()).optional(),
            "companionSizes": t.array(t.proxy(renames["SizeOut"])).optional(),
            "size": t.proxy(renames["SizeOut"]).optional(),
            "creativeSizeType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeSizeOut"])
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
    types["ImpressionMetricsRowIn"] = t.struct(
        {
            "rowDimensions": t.proxy(renames["RowDimensionsIn"]).optional(),
            "inventoryMatches": t.proxy(renames["MetricValueIn"]).optional(),
            "availableImpressions": t.proxy(renames["MetricValueIn"]).optional(),
            "responsesWithBids": t.proxy(renames["MetricValueIn"]).optional(),
            "successfulResponses": t.proxy(renames["MetricValueIn"]).optional(),
            "bidRequests": t.proxy(renames["MetricValueIn"]).optional(),
        }
    ).named(renames["ImpressionMetricsRowIn"])
    types["ImpressionMetricsRowOut"] = t.struct(
        {
            "rowDimensions": t.proxy(renames["RowDimensionsOut"]).optional(),
            "inventoryMatches": t.proxy(renames["MetricValueOut"]).optional(),
            "availableImpressions": t.proxy(renames["MetricValueOut"]).optional(),
            "responsesWithBids": t.proxy(renames["MetricValueOut"]).optional(),
            "successfulResponses": t.proxy(renames["MetricValueOut"]).optional(),
            "bidRequests": t.proxy(renames["MetricValueOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImpressionMetricsRowOut"])
    types["BuyerIn"] = t.struct({"accountId": t.string().optional()}).named(
        renames["BuyerIn"]
    )
    types["BuyerOut"] = t.struct(
        {
            "accountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuyerOut"])
    types["NonBillableWinningBidStatusRowIn"] = t.struct(
        {
            "bidCount": t.proxy(renames["MetricValueIn"]).optional(),
            "rowDimensions": t.proxy(renames["RowDimensionsIn"]).optional(),
            "status": t.string().optional(),
        }
    ).named(renames["NonBillableWinningBidStatusRowIn"])
    types["NonBillableWinningBidStatusRowOut"] = t.struct(
        {
            "bidCount": t.proxy(renames["MetricValueOut"]).optional(),
            "rowDimensions": t.proxy(renames["RowDimensionsOut"]).optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NonBillableWinningBidStatusRowOut"])
    types["HtmlContentIn"] = t.struct(
        {
            "width": t.integer().optional(),
            "snippet": t.string().optional(),
            "height": t.integer().optional(),
        }
    ).named(renames["HtmlContentIn"])
    types["HtmlContentOut"] = t.struct(
        {
            "width": t.integer().optional(),
            "snippet": t.string().optional(),
            "height": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HtmlContentOut"])
    types["DisapprovalIn"] = t.struct(
        {"reason": t.string().optional(), "details": t.array(t.string()).optional()}
    ).named(renames["DisapprovalIn"])
    types["DisapprovalOut"] = t.struct(
        {
            "reason": t.string().optional(),
            "details": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DisapprovalOut"])
    types["DeliveryControlIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeliveryControlIn"]
    )
    types["DeliveryControlOut"] = t.struct(
        {
            "frequencyCaps": t.array(t.proxy(renames["FrequencyCapOut"])).optional(),
            "deliveryRateType": t.string().optional(),
            "creativeBlockingLevel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeliveryControlOut"])
    types["RealtimeTimeRangeIn"] = t.struct(
        {"startTimestamp": t.string().optional()}
    ).named(renames["RealtimeTimeRangeIn"])
    types["RealtimeTimeRangeOut"] = t.struct(
        {
            "startTimestamp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RealtimeTimeRangeOut"])
    types["StopWatchingCreativeRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["StopWatchingCreativeRequestIn"])
    types["StopWatchingCreativeRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StopWatchingCreativeRequestOut"])
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
    types["SecurityContextIn"] = t.struct(
        {"securities": t.array(t.string()).optional()}
    ).named(renames["SecurityContextIn"])
    types["SecurityContextOut"] = t.struct(
        {
            "securities": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecurityContextOut"])
    types["CreativeRestrictionsIn"] = t.struct(
        {
            "skippableAdType": t.string().optional(),
            "creativeFormat": t.string().optional(),
            "creativeSpecifications": t.array(
                t.proxy(renames["CreativeSpecificationIn"])
            ),
        }
    ).named(renames["CreativeRestrictionsIn"])
    types["CreativeRestrictionsOut"] = t.struct(
        {
            "skippableAdType": t.string().optional(),
            "creativeFormat": t.string().optional(),
            "creativeSpecifications": t.array(
                t.proxy(renames["CreativeSpecificationOut"])
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeRestrictionsOut"])
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
    types["PrivateDataIn"] = t.struct({"referenceId": t.string().optional()}).named(
        renames["PrivateDataIn"]
    )
    types["PrivateDataOut"] = t.struct(
        {
            "referenceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrivateDataOut"])

    functions = {}
    functions["biddersAccountsFilterSetsList"] = adexchangebuyer2.delete(
        "v2beta1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersAccountsFilterSetsGet"] = adexchangebuyer2.delete(
        "v2beta1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersAccountsFilterSetsCreate"] = adexchangebuyer2.delete(
        "v2beta1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersAccountsFilterSetsDelete"] = adexchangebuyer2.delete(
        "v2beta1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
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
    functions["biddersAccountsFilterSetsLosingBidsList"] = adexchangebuyer2.get(
        "v2beta1/{filterSetName}/losingBids",
        t.struct(
            {
                "filterSetName": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "filterSetName": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListImpressionMetricsResponseOut"]),
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
    functions[
        "biddersAccountsFilterSetsFilteredBidsCreativesList"
    ] = adexchangebuyer2.get(
        "v2beta1/{filterSetName}/filteredBids/{creativeStatusId}/creatives",
        t.struct(
            {
                "filterSetName": t.string().optional(),
                "creativeStatusId": t.integer().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCreativeStatusBreakdownByCreativeResponseOut"]),
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
    functions[
        "biddersAccountsFilterSetsNonBillableWinningBidsList"
    ] = adexchangebuyer2.get(
        "v2beta1/{filterSetName}/nonBillableWinningBids",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filterSetName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListNonBillableWinningBidsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersFilterSetsList"] = adexchangebuyer2.get(
        "v2beta1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["FilterSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersFilterSetsDelete"] = adexchangebuyer2.get(
        "v2beta1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["FilterSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersFilterSetsCreate"] = adexchangebuyer2.get(
        "v2beta1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["FilterSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersFilterSetsGet"] = adexchangebuyer2.get(
        "v2beta1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["FilterSetOut"]),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filterSetName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBidMetricsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersFilterSetsBidResponseErrorsList"] = adexchangebuyer2.get(
        "v2beta1/{filterSetName}/bidResponseErrors",
        t.struct(
            {
                "filterSetName": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "filterSetName": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBidResponsesWithoutBidsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersFilterSetsImpressionMetricsList"] = adexchangebuyer2.get(
        "v2beta1/{filterSetName}/impressionMetrics",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filterSetName": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListImpressionMetricsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersFilterSetsFilteredBidsList"] = adexchangebuyer2.get(
        "v2beta1/{filterSetName}/filteredBids",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filterSetName": t.string().optional(),
                "pageToken": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "creativeStatusId": t.integer().optional(),
                "pageToken": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "creativeStatusId": t.integer().optional(),
                "filterSetName": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCreativeStatusBreakdownByDetailResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersFilterSetsFilteredBidRequestsList"] = adexchangebuyer2.get(
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
    functions["biddersFilterSetsLosingBidsList"] = adexchangebuyer2.get(
        "v2beta1/{filterSetName}/losingBids",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filterSetName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLosingBidsResponseOut"]),
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
    functions["accountsCreativesDealAssociationsRemove"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/creatives/{creativeId}/dealAssociations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "query": t.string().optional(),
                "creativeId": t.string().optional(),
                "accountId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDealAssociationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCreativesDealAssociationsAdd"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/creatives/{creativeId}/dealAssociations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "query": t.string().optional(),
                "creativeId": t.string().optional(),
                "accountId": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "query": t.string().optional(),
                "creativeId": t.string().optional(),
                "accountId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDealAssociationsResponseOut"]),
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
    functions["accountsProposalsCompleteSetup"] = adexchangebuyer2.put(
        "v2beta1/accounts/{accountId}/proposals/{proposalId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "proposalId": t.string().optional(),
                "deals": t.array(t.proxy(renames["DealIn"])).optional(),
                "buyerPrivateData": t.proxy(renames["PrivateDataIn"]).optional(),
                "seller": t.proxy(renames["SellerIn"]).optional(),
                "buyerContacts": t.array(
                    t.proxy(renames["ContactInformationIn"])
                ).optional(),
                "buyer": t.proxy(renames["BuyerIn"]).optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProposalOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsProposalsAccept"] = adexchangebuyer2.put(
        "v2beta1/accounts/{accountId}/proposals/{proposalId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "proposalId": t.string().optional(),
                "deals": t.array(t.proxy(renames["DealIn"])).optional(),
                "buyerPrivateData": t.proxy(renames["PrivateDataIn"]).optional(),
                "seller": t.proxy(renames["SellerIn"]).optional(),
                "buyerContacts": t.array(
                    t.proxy(renames["ContactInformationIn"])
                ).optional(),
                "buyer": t.proxy(renames["BuyerIn"]).optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProposalOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsProposalsPause"] = adexchangebuyer2.put(
        "v2beta1/accounts/{accountId}/proposals/{proposalId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "proposalId": t.string().optional(),
                "deals": t.array(t.proxy(renames["DealIn"])).optional(),
                "buyerPrivateData": t.proxy(renames["PrivateDataIn"]).optional(),
                "seller": t.proxy(renames["SellerIn"]).optional(),
                "buyerContacts": t.array(
                    t.proxy(renames["ContactInformationIn"])
                ).optional(),
                "buyer": t.proxy(renames["BuyerIn"]).optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProposalOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsProposalsCreate"] = adexchangebuyer2.put(
        "v2beta1/accounts/{accountId}/proposals/{proposalId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "proposalId": t.string().optional(),
                "deals": t.array(t.proxy(renames["DealIn"])).optional(),
                "buyerPrivateData": t.proxy(renames["PrivateDataIn"]).optional(),
                "seller": t.proxy(renames["SellerIn"]).optional(),
                "buyerContacts": t.array(
                    t.proxy(renames["ContactInformationIn"])
                ).optional(),
                "buyer": t.proxy(renames["BuyerIn"]).optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProposalOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsProposalsCancelNegotiation"] = adexchangebuyer2.put(
        "v2beta1/accounts/{accountId}/proposals/{proposalId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "proposalId": t.string().optional(),
                "deals": t.array(t.proxy(renames["DealIn"])).optional(),
                "buyerPrivateData": t.proxy(renames["PrivateDataIn"]).optional(),
                "seller": t.proxy(renames["SellerIn"]).optional(),
                "buyerContacts": t.array(
                    t.proxy(renames["ContactInformationIn"])
                ).optional(),
                "buyer": t.proxy(renames["BuyerIn"]).optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProposalOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsProposalsGet"] = adexchangebuyer2.put(
        "v2beta1/accounts/{accountId}/proposals/{proposalId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "proposalId": t.string().optional(),
                "deals": t.array(t.proxy(renames["DealIn"])).optional(),
                "buyerPrivateData": t.proxy(renames["PrivateDataIn"]).optional(),
                "seller": t.proxy(renames["SellerIn"]).optional(),
                "buyerContacts": t.array(
                    t.proxy(renames["ContactInformationIn"])
                ).optional(),
                "buyer": t.proxy(renames["BuyerIn"]).optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProposalOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsProposalsList"] = adexchangebuyer2.put(
        "v2beta1/accounts/{accountId}/proposals/{proposalId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "proposalId": t.string().optional(),
                "deals": t.array(t.proxy(renames["DealIn"])).optional(),
                "buyerPrivateData": t.proxy(renames["PrivateDataIn"]).optional(),
                "seller": t.proxy(renames["SellerIn"]).optional(),
                "buyerContacts": t.array(
                    t.proxy(renames["ContactInformationIn"])
                ).optional(),
                "buyer": t.proxy(renames["BuyerIn"]).optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProposalOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsProposalsResume"] = adexchangebuyer2.put(
        "v2beta1/accounts/{accountId}/proposals/{proposalId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "proposalId": t.string().optional(),
                "deals": t.array(t.proxy(renames["DealIn"])).optional(),
                "buyerPrivateData": t.proxy(renames["PrivateDataIn"]).optional(),
                "seller": t.proxy(renames["SellerIn"]).optional(),
                "buyerContacts": t.array(
                    t.proxy(renames["ContactInformationIn"])
                ).optional(),
                "buyer": t.proxy(renames["BuyerIn"]).optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProposalOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsProposalsAddNote"] = adexchangebuyer2.put(
        "v2beta1/accounts/{accountId}/proposals/{proposalId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "proposalId": t.string().optional(),
                "deals": t.array(t.proxy(renames["DealIn"])).optional(),
                "buyerPrivateData": t.proxy(renames["PrivateDataIn"]).optional(),
                "seller": t.proxy(renames["SellerIn"]).optional(),
                "buyerContacts": t.array(
                    t.proxy(renames["ContactInformationIn"])
                ).optional(),
                "buyer": t.proxy(renames["BuyerIn"]).optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProposalOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsProposalsUpdate"] = adexchangebuyer2.put(
        "v2beta1/accounts/{accountId}/proposals/{proposalId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "proposalId": t.string().optional(),
                "deals": t.array(t.proxy(renames["DealIn"])).optional(),
                "buyerPrivateData": t.proxy(renames["PrivateDataIn"]).optional(),
                "seller": t.proxy(renames["SellerIn"]).optional(),
                "buyerContacts": t.array(
                    t.proxy(renames["ContactInformationIn"])
                ).optional(),
                "buyer": t.proxy(renames["BuyerIn"]).optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProposalOut"]),
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
    functions["accountsClientsCreate"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/clients",
        t.struct(
            {
                "partnerClientId": t.string().optional(),
                "accountId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
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
                "partnerClientId": t.string().optional(),
                "accountId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListClientsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsClientsUpdate"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/clients",
        t.struct(
            {
                "partnerClientId": t.string().optional(),
                "accountId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
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
                "partnerClientId": t.string().optional(),
                "accountId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListClientsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsClientsInvitationsCreate"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/clients/{clientAccountId}/invitations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "accountId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "clientAccountId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListClientUserInvitationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsClientsInvitationsGet"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/clients/{clientAccountId}/invitations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "accountId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "clientAccountId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListClientUserInvitationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsClientsInvitationsList"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/clients/{clientAccountId}/invitations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "accountId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "clientAccountId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListClientUserInvitationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsClientsUsersGet"] = adexchangebuyer2.put(
        "v2beta1/accounts/{accountId}/clients/{clientAccountId}/users/{userId}",
        t.struct(
            {
                "userId": t.string().optional(),
                "clientAccountId": t.string().optional(),
                "accountId": t.string().optional(),
                "email": t.string().optional(),
                "status": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClientUserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsClientsUsersList"] = adexchangebuyer2.put(
        "v2beta1/accounts/{accountId}/clients/{clientAccountId}/users/{userId}",
        t.struct(
            {
                "userId": t.string().optional(),
                "clientAccountId": t.string().optional(),
                "accountId": t.string().optional(),
                "email": t.string().optional(),
                "status": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClientUserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsClientsUsersUpdate"] = adexchangebuyer2.put(
        "v2beta1/accounts/{accountId}/clients/{clientAccountId}/users/{userId}",
        t.struct(
            {
                "userId": t.string().optional(),
                "clientAccountId": t.string().optional(),
                "accountId": t.string().optional(),
                "email": t.string().optional(),
                "status": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClientUserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="adexchangebuyer2", renames=renames, types=types, functions=functions
    )
