from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_adexchangebuyer2() -> Import:
    adexchangebuyer2 = HTTPRuntime("https://adexchangebuyer.googleapis.com/")

    renames = {
        "ErrorResponse": "_adexchangebuyer2_1_ErrorResponse",
        "PublisherProfileMobileApplicationIn": "_adexchangebuyer2_2_PublisherProfileMobileApplicationIn",
        "PublisherProfileMobileApplicationOut": "_adexchangebuyer2_3_PublisherProfileMobileApplicationOut",
        "ProductIn": "_adexchangebuyer2_4_ProductIn",
        "ProductOut": "_adexchangebuyer2_5_ProductOut",
        "PlacementTargetingIn": "_adexchangebuyer2_6_PlacementTargetingIn",
        "PlacementTargetingOut": "_adexchangebuyer2_7_PlacementTargetingOut",
        "MoneyIn": "_adexchangebuyer2_8_MoneyIn",
        "MoneyOut": "_adexchangebuyer2_9_MoneyOut",
        "ClientUserInvitationIn": "_adexchangebuyer2_10_ClientUserInvitationIn",
        "ClientUserInvitationOut": "_adexchangebuyer2_11_ClientUserInvitationOut",
        "ListCreativesResponseIn": "_adexchangebuyer2_12_ListCreativesResponseIn",
        "ListCreativesResponseOut": "_adexchangebuyer2_13_ListCreativesResponseOut",
        "SellerIn": "_adexchangebuyer2_14_SellerIn",
        "SellerOut": "_adexchangebuyer2_15_SellerOut",
        "LocationContextIn": "_adexchangebuyer2_16_LocationContextIn",
        "LocationContextOut": "_adexchangebuyer2_17_LocationContextOut",
        "ContactInformationIn": "_adexchangebuyer2_18_ContactInformationIn",
        "ContactInformationOut": "_adexchangebuyer2_19_ContactInformationOut",
        "CreativeRestrictionsIn": "_adexchangebuyer2_20_CreativeRestrictionsIn",
        "CreativeRestrictionsOut": "_adexchangebuyer2_21_CreativeRestrictionsOut",
        "TechnologyTargetingIn": "_adexchangebuyer2_22_TechnologyTargetingIn",
        "TechnologyTargetingOut": "_adexchangebuyer2_23_TechnologyTargetingOut",
        "CreativeIn": "_adexchangebuyer2_24_CreativeIn",
        "CreativeOut": "_adexchangebuyer2_25_CreativeOut",
        "ClientIn": "_adexchangebuyer2_26_ClientIn",
        "ClientOut": "_adexchangebuyer2_27_ClientOut",
        "ListLosingBidsResponseIn": "_adexchangebuyer2_28_ListLosingBidsResponseIn",
        "ListLosingBidsResponseOut": "_adexchangebuyer2_29_ListLosingBidsResponseOut",
        "FilteredBidDetailRowIn": "_adexchangebuyer2_30_FilteredBidDetailRowIn",
        "FilteredBidDetailRowOut": "_adexchangebuyer2_31_FilteredBidDetailRowOut",
        "DisapprovalIn": "_adexchangebuyer2_32_DisapprovalIn",
        "DisapprovalOut": "_adexchangebuyer2_33_DisapprovalOut",
        "UrlTargetingIn": "_adexchangebuyer2_34_UrlTargetingIn",
        "UrlTargetingOut": "_adexchangebuyer2_35_UrlTargetingOut",
        "AbsoluteDateRangeIn": "_adexchangebuyer2_36_AbsoluteDateRangeIn",
        "AbsoluteDateRangeOut": "_adexchangebuyer2_37_AbsoluteDateRangeOut",
        "AdSizeIn": "_adexchangebuyer2_38_AdSizeIn",
        "AdSizeOut": "_adexchangebuyer2_39_AdSizeOut",
        "DeliveryControlIn": "_adexchangebuyer2_40_DeliveryControlIn",
        "DeliveryControlOut": "_adexchangebuyer2_41_DeliveryControlOut",
        "EmptyIn": "_adexchangebuyer2_42_EmptyIn",
        "EmptyOut": "_adexchangebuyer2_43_EmptyOut",
        "CriteriaTargetingIn": "_adexchangebuyer2_44_CriteriaTargetingIn",
        "CriteriaTargetingOut": "_adexchangebuyer2_45_CriteriaTargetingOut",
        "PublisherProfileIn": "_adexchangebuyer2_46_PublisherProfileIn",
        "PublisherProfileOut": "_adexchangebuyer2_47_PublisherProfileOut",
        "MarketplaceTargetingIn": "_adexchangebuyer2_48_MarketplaceTargetingIn",
        "MarketplaceTargetingOut": "_adexchangebuyer2_49_MarketplaceTargetingOut",
        "ImageIn": "_adexchangebuyer2_50_ImageIn",
        "ImageOut": "_adexchangebuyer2_51_ImageOut",
        "ListBidResponsesWithoutBidsResponseIn": "_adexchangebuyer2_52_ListBidResponsesWithoutBidsResponseIn",
        "ListBidResponsesWithoutBidsResponseOut": "_adexchangebuyer2_53_ListBidResponsesWithoutBidsResponseOut",
        "DealPauseStatusIn": "_adexchangebuyer2_54_DealPauseStatusIn",
        "DealPauseStatusOut": "_adexchangebuyer2_55_DealPauseStatusOut",
        "ListPublisherProfilesResponseIn": "_adexchangebuyer2_56_ListPublisherProfilesResponseIn",
        "ListPublisherProfilesResponseOut": "_adexchangebuyer2_57_ListPublisherProfilesResponseOut",
        "SecurityContextIn": "_adexchangebuyer2_58_SecurityContextIn",
        "SecurityContextOut": "_adexchangebuyer2_59_SecurityContextOut",
        "RealtimeTimeRangeIn": "_adexchangebuyer2_60_RealtimeTimeRangeIn",
        "RealtimeTimeRangeOut": "_adexchangebuyer2_61_RealtimeTimeRangeOut",
        "AddNoteRequestIn": "_adexchangebuyer2_62_AddNoteRequestIn",
        "AddNoteRequestOut": "_adexchangebuyer2_63_AddNoteRequestOut",
        "PricePerBuyerIn": "_adexchangebuyer2_64_PricePerBuyerIn",
        "PricePerBuyerOut": "_adexchangebuyer2_65_PricePerBuyerOut",
        "CreativeSpecificationIn": "_adexchangebuyer2_66_CreativeSpecificationIn",
        "CreativeSpecificationOut": "_adexchangebuyer2_67_CreativeSpecificationOut",
        "BuyerIn": "_adexchangebuyer2_68_BuyerIn",
        "BuyerOut": "_adexchangebuyer2_69_BuyerOut",
        "TargetingValueIn": "_adexchangebuyer2_70_TargetingValueIn",
        "TargetingValueOut": "_adexchangebuyer2_71_TargetingValueOut",
        "NonGuaranteedFixedPriceTermsIn": "_adexchangebuyer2_72_NonGuaranteedFixedPriceTermsIn",
        "NonGuaranteedFixedPriceTermsOut": "_adexchangebuyer2_73_NonGuaranteedFixedPriceTermsOut",
        "TargetingCriteriaIn": "_adexchangebuyer2_74_TargetingCriteriaIn",
        "TargetingCriteriaOut": "_adexchangebuyer2_75_TargetingCriteriaOut",
        "NonBillableWinningBidStatusRowIn": "_adexchangebuyer2_76_NonBillableWinningBidStatusRowIn",
        "NonBillableWinningBidStatusRowOut": "_adexchangebuyer2_77_NonBillableWinningBidStatusRowOut",
        "ResumeProposalRequestIn": "_adexchangebuyer2_78_ResumeProposalRequestIn",
        "ResumeProposalRequestOut": "_adexchangebuyer2_79_ResumeProposalRequestOut",
        "VideoTargetingIn": "_adexchangebuyer2_80_VideoTargetingIn",
        "VideoTargetingOut": "_adexchangebuyer2_81_VideoTargetingOut",
        "NativeContentIn": "_adexchangebuyer2_82_NativeContentIn",
        "NativeContentOut": "_adexchangebuyer2_83_NativeContentOut",
        "ServingRestrictionIn": "_adexchangebuyer2_84_ServingRestrictionIn",
        "ServingRestrictionOut": "_adexchangebuyer2_85_ServingRestrictionOut",
        "CalloutStatusRowIn": "_adexchangebuyer2_86_CalloutStatusRowIn",
        "CalloutStatusRowOut": "_adexchangebuyer2_87_CalloutStatusRowOut",
        "SizeIn": "_adexchangebuyer2_88_SizeIn",
        "SizeOut": "_adexchangebuyer2_89_SizeOut",
        "VideoContentIn": "_adexchangebuyer2_90_VideoContentIn",
        "VideoContentOut": "_adexchangebuyer2_91_VideoContentOut",
        "ListProductsResponseIn": "_adexchangebuyer2_92_ListProductsResponseIn",
        "ListProductsResponseOut": "_adexchangebuyer2_93_ListProductsResponseOut",
        "MetricValueIn": "_adexchangebuyer2_94_MetricValueIn",
        "MetricValueOut": "_adexchangebuyer2_95_MetricValueOut",
        "ListBidMetricsResponseIn": "_adexchangebuyer2_96_ListBidMetricsResponseIn",
        "ListBidMetricsResponseOut": "_adexchangebuyer2_97_ListBidMetricsResponseOut",
        "CancelNegotiationRequestIn": "_adexchangebuyer2_98_CancelNegotiationRequestIn",
        "CancelNegotiationRequestOut": "_adexchangebuyer2_99_CancelNegotiationRequestOut",
        "NoteIn": "_adexchangebuyer2_100_NoteIn",
        "NoteOut": "_adexchangebuyer2_101_NoteOut",
        "CreativeStatusRowIn": "_adexchangebuyer2_102_CreativeStatusRowIn",
        "CreativeStatusRowOut": "_adexchangebuyer2_103_CreativeStatusRowOut",
        "ListCreativeStatusBreakdownByDetailResponseIn": "_adexchangebuyer2_104_ListCreativeStatusBreakdownByDetailResponseIn",
        "ListCreativeStatusBreakdownByDetailResponseOut": "_adexchangebuyer2_105_ListCreativeStatusBreakdownByDetailResponseOut",
        "GuaranteedFixedPriceTermsIn": "_adexchangebuyer2_106_GuaranteedFixedPriceTermsIn",
        "GuaranteedFixedPriceTermsOut": "_adexchangebuyer2_107_GuaranteedFixedPriceTermsOut",
        "FilterSetIn": "_adexchangebuyer2_108_FilterSetIn",
        "FilterSetOut": "_adexchangebuyer2_109_FilterSetOut",
        "PauseProposalDealsRequestIn": "_adexchangebuyer2_110_PauseProposalDealsRequestIn",
        "PauseProposalDealsRequestOut": "_adexchangebuyer2_111_PauseProposalDealsRequestOut",
        "DealTermsIn": "_adexchangebuyer2_112_DealTermsIn",
        "DealTermsOut": "_adexchangebuyer2_113_DealTermsOut",
        "BidMetricsRowIn": "_adexchangebuyer2_114_BidMetricsRowIn",
        "BidMetricsRowOut": "_adexchangebuyer2_115_BidMetricsRowOut",
        "PauseProposalRequestIn": "_adexchangebuyer2_116_PauseProposalRequestIn",
        "PauseProposalRequestOut": "_adexchangebuyer2_117_PauseProposalRequestOut",
        "ListFilterSetsResponseIn": "_adexchangebuyer2_118_ListFilterSetsResponseIn",
        "ListFilterSetsResponseOut": "_adexchangebuyer2_119_ListFilterSetsResponseOut",
        "DealIn": "_adexchangebuyer2_120_DealIn",
        "DealOut": "_adexchangebuyer2_121_DealOut",
        "ListDealAssociationsResponseIn": "_adexchangebuyer2_122_ListDealAssociationsResponseIn",
        "ListDealAssociationsResponseOut": "_adexchangebuyer2_123_ListDealAssociationsResponseOut",
        "ResumeProposalDealsRequestIn": "_adexchangebuyer2_124_ResumeProposalDealsRequestIn",
        "ResumeProposalDealsRequestOut": "_adexchangebuyer2_125_ResumeProposalDealsRequestOut",
        "ListProposalsResponseIn": "_adexchangebuyer2_126_ListProposalsResponseIn",
        "ListProposalsResponseOut": "_adexchangebuyer2_127_ListProposalsResponseOut",
        "RemoveDealAssociationRequestIn": "_adexchangebuyer2_128_RemoveDealAssociationRequestIn",
        "RemoveDealAssociationRequestOut": "_adexchangebuyer2_129_RemoveDealAssociationRequestOut",
        "AppContextIn": "_adexchangebuyer2_130_AppContextIn",
        "AppContextOut": "_adexchangebuyer2_131_AppContextOut",
        "FirstPartyMobileApplicationTargetingIn": "_adexchangebuyer2_132_FirstPartyMobileApplicationTargetingIn",
        "FirstPartyMobileApplicationTargetingOut": "_adexchangebuyer2_133_FirstPartyMobileApplicationTargetingOut",
        "TimeOfDayIn": "_adexchangebuyer2_134_TimeOfDayIn",
        "TimeOfDayOut": "_adexchangebuyer2_135_TimeOfDayOut",
        "ProposalIn": "_adexchangebuyer2_136_ProposalIn",
        "ProposalOut": "_adexchangebuyer2_137_ProposalOut",
        "OperatingSystemTargetingIn": "_adexchangebuyer2_138_OperatingSystemTargetingIn",
        "OperatingSystemTargetingOut": "_adexchangebuyer2_139_OperatingSystemTargetingOut",
        "ServingContextIn": "_adexchangebuyer2_140_ServingContextIn",
        "ServingContextOut": "_adexchangebuyer2_141_ServingContextOut",
        "PrivateDataIn": "_adexchangebuyer2_142_PrivateDataIn",
        "PrivateDataOut": "_adexchangebuyer2_143_PrivateDataOut",
        "DealServingMetadataIn": "_adexchangebuyer2_144_DealServingMetadataIn",
        "DealServingMetadataOut": "_adexchangebuyer2_145_DealServingMetadataOut",
        "FrequencyCapIn": "_adexchangebuyer2_146_FrequencyCapIn",
        "FrequencyCapOut": "_adexchangebuyer2_147_FrequencyCapOut",
        "InventorySizeTargetingIn": "_adexchangebuyer2_148_InventorySizeTargetingIn",
        "InventorySizeTargetingOut": "_adexchangebuyer2_149_InventorySizeTargetingOut",
        "ListClientUsersResponseIn": "_adexchangebuyer2_150_ListClientUsersResponseIn",
        "ListClientUsersResponseOut": "_adexchangebuyer2_151_ListClientUsersResponseOut",
        "TimeIntervalIn": "_adexchangebuyer2_152_TimeIntervalIn",
        "TimeIntervalOut": "_adexchangebuyer2_153_TimeIntervalOut",
        "CorrectionIn": "_adexchangebuyer2_154_CorrectionIn",
        "CorrectionOut": "_adexchangebuyer2_155_CorrectionOut",
        "ListClientUserInvitationsResponseIn": "_adexchangebuyer2_156_ListClientUserInvitationsResponseIn",
        "ListClientUserInvitationsResponseOut": "_adexchangebuyer2_157_ListClientUserInvitationsResponseOut",
        "StopWatchingCreativeRequestIn": "_adexchangebuyer2_158_StopWatchingCreativeRequestIn",
        "StopWatchingCreativeRequestOut": "_adexchangebuyer2_159_StopWatchingCreativeRequestOut",
        "MobileApplicationTargetingIn": "_adexchangebuyer2_160_MobileApplicationTargetingIn",
        "MobileApplicationTargetingOut": "_adexchangebuyer2_161_MobileApplicationTargetingOut",
        "PlatformContextIn": "_adexchangebuyer2_162_PlatformContextIn",
        "PlatformContextOut": "_adexchangebuyer2_163_PlatformContextOut",
        "AdTechnologyProvidersIn": "_adexchangebuyer2_164_AdTechnologyProvidersIn",
        "AdTechnologyProvidersOut": "_adexchangebuyer2_165_AdTechnologyProvidersOut",
        "CreativeDealAssociationIn": "_adexchangebuyer2_166_CreativeDealAssociationIn",
        "CreativeDealAssociationOut": "_adexchangebuyer2_167_CreativeDealAssociationOut",
        "NonGuaranteedAuctionTermsIn": "_adexchangebuyer2_168_NonGuaranteedAuctionTermsIn",
        "NonGuaranteedAuctionTermsOut": "_adexchangebuyer2_169_NonGuaranteedAuctionTermsOut",
        "ClientUserIn": "_adexchangebuyer2_170_ClientUserIn",
        "ClientUserOut": "_adexchangebuyer2_171_ClientUserOut",
        "RelativeDateRangeIn": "_adexchangebuyer2_172_RelativeDateRangeIn",
        "RelativeDateRangeOut": "_adexchangebuyer2_173_RelativeDateRangeOut",
        "CreativeSizeIn": "_adexchangebuyer2_174_CreativeSizeIn",
        "CreativeSizeOut": "_adexchangebuyer2_175_CreativeSizeOut",
        "AddDealAssociationRequestIn": "_adexchangebuyer2_176_AddDealAssociationRequestIn",
        "AddDealAssociationRequestOut": "_adexchangebuyer2_177_AddDealAssociationRequestOut",
        "BidResponseWithoutBidsStatusRowIn": "_adexchangebuyer2_178_BidResponseWithoutBidsStatusRowIn",
        "BidResponseWithoutBidsStatusRowOut": "_adexchangebuyer2_179_BidResponseWithoutBidsStatusRowOut",
        "PriceIn": "_adexchangebuyer2_180_PriceIn",
        "PriceOut": "_adexchangebuyer2_181_PriceOut",
        "AcceptProposalRequestIn": "_adexchangebuyer2_182_AcceptProposalRequestIn",
        "AcceptProposalRequestOut": "_adexchangebuyer2_183_AcceptProposalRequestOut",
        "DayPartIn": "_adexchangebuyer2_184_DayPartIn",
        "DayPartOut": "_adexchangebuyer2_185_DayPartOut",
        "ListNonBillableWinningBidsResponseIn": "_adexchangebuyer2_186_ListNonBillableWinningBidsResponseIn",
        "ListNonBillableWinningBidsResponseOut": "_adexchangebuyer2_187_ListNonBillableWinningBidsResponseOut",
        "ListCreativeStatusBreakdownByCreativeResponseIn": "_adexchangebuyer2_188_ListCreativeStatusBreakdownByCreativeResponseIn",
        "ListCreativeStatusBreakdownByCreativeResponseOut": "_adexchangebuyer2_189_ListCreativeStatusBreakdownByCreativeResponseOut",
        "FilteredBidCreativeRowIn": "_adexchangebuyer2_190_FilteredBidCreativeRowIn",
        "FilteredBidCreativeRowOut": "_adexchangebuyer2_191_FilteredBidCreativeRowOut",
        "DateIn": "_adexchangebuyer2_192_DateIn",
        "DateOut": "_adexchangebuyer2_193_DateOut",
        "ImpressionMetricsRowIn": "_adexchangebuyer2_194_ImpressionMetricsRowIn",
        "ImpressionMetricsRowOut": "_adexchangebuyer2_195_ImpressionMetricsRowOut",
        "AuctionContextIn": "_adexchangebuyer2_196_AuctionContextIn",
        "AuctionContextOut": "_adexchangebuyer2_197_AuctionContextOut",
        "CompleteSetupRequestIn": "_adexchangebuyer2_198_CompleteSetupRequestIn",
        "CompleteSetupRequestOut": "_adexchangebuyer2_199_CompleteSetupRequestOut",
        "HtmlContentIn": "_adexchangebuyer2_200_HtmlContentIn",
        "HtmlContentOut": "_adexchangebuyer2_201_HtmlContentOut",
        "ListImpressionMetricsResponseIn": "_adexchangebuyer2_202_ListImpressionMetricsResponseIn",
        "ListImpressionMetricsResponseOut": "_adexchangebuyer2_203_ListImpressionMetricsResponseOut",
        "DayPartTargetingIn": "_adexchangebuyer2_204_DayPartTargetingIn",
        "DayPartTargetingOut": "_adexchangebuyer2_205_DayPartTargetingOut",
        "ListBidResponseErrorsResponseIn": "_adexchangebuyer2_206_ListBidResponseErrorsResponseIn",
        "ListBidResponseErrorsResponseOut": "_adexchangebuyer2_207_ListBidResponseErrorsResponseOut",
        "RowDimensionsIn": "_adexchangebuyer2_208_RowDimensionsIn",
        "RowDimensionsOut": "_adexchangebuyer2_209_RowDimensionsOut",
        "WatchCreativeRequestIn": "_adexchangebuyer2_210_WatchCreativeRequestIn",
        "WatchCreativeRequestOut": "_adexchangebuyer2_211_WatchCreativeRequestOut",
        "ListFilteredBidRequestsResponseIn": "_adexchangebuyer2_212_ListFilteredBidRequestsResponseIn",
        "ListFilteredBidRequestsResponseOut": "_adexchangebuyer2_213_ListFilteredBidRequestsResponseOut",
        "ListFilteredBidsResponseIn": "_adexchangebuyer2_214_ListFilteredBidsResponseIn",
        "ListFilteredBidsResponseOut": "_adexchangebuyer2_215_ListFilteredBidsResponseOut",
        "ListClientsResponseIn": "_adexchangebuyer2_216_ListClientsResponseIn",
        "ListClientsResponseOut": "_adexchangebuyer2_217_ListClientsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["PublisherProfileMobileApplicationIn"] = t.struct(
        {
            "externalAppId": t.string().optional(),
            "name": t.string().optional(),
            "appStore": t.string().optional(),
        }
    ).named(renames["PublisherProfileMobileApplicationIn"])
    types["PublisherProfileMobileApplicationOut"] = t.struct(
        {
            "externalAppId": t.string().optional(),
            "name": t.string().optional(),
            "appStore": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublisherProfileMobileApplicationOut"])
    types["ProductIn"] = t.struct(
        {
            "seller": t.proxy(renames["SellerIn"]).optional(),
            "productId": t.string().optional(),
            "displayName": t.string().optional(),
            "targetingCriterion": t.array(
                t.proxy(renames["TargetingCriteriaIn"])
            ).optional(),
            "webPropertyCode": t.string().optional(),
            "publisherProfileId": t.string().optional(),
            "availableEndTime": t.string().optional(),
            "availableStartTime": t.string().optional(),
            "terms": t.proxy(renames["DealTermsIn"]).optional(),
            "syndicationProduct": t.string().optional(),
            "productRevision": t.string().optional(),
            "updateTime": t.string().optional(),
            "hasCreatorSignedOff": t.boolean().optional(),
            "createTime": t.string().optional(),
            "creatorContacts": t.array(
                t.proxy(renames["ContactInformationIn"])
            ).optional(),
        }
    ).named(renames["ProductIn"])
    types["ProductOut"] = t.struct(
        {
            "seller": t.proxy(renames["SellerOut"]).optional(),
            "productId": t.string().optional(),
            "displayName": t.string().optional(),
            "targetingCriterion": t.array(
                t.proxy(renames["TargetingCriteriaOut"])
            ).optional(),
            "webPropertyCode": t.string().optional(),
            "publisherProfileId": t.string().optional(),
            "availableEndTime": t.string().optional(),
            "availableStartTime": t.string().optional(),
            "terms": t.proxy(renames["DealTermsOut"]).optional(),
            "syndicationProduct": t.string().optional(),
            "productRevision": t.string().optional(),
            "updateTime": t.string().optional(),
            "hasCreatorSignedOff": t.boolean().optional(),
            "createTime": t.string().optional(),
            "creatorContacts": t.array(
                t.proxy(renames["ContactInformationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductOut"])
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
    types["ClientUserInvitationIn"] = t.struct(
        {
            "email": t.string().optional(),
            "invitationId": t.string().optional(),
            "clientAccountId": t.string().optional(),
        }
    ).named(renames["ClientUserInvitationIn"])
    types["ClientUserInvitationOut"] = t.struct(
        {
            "email": t.string().optional(),
            "invitationId": t.string().optional(),
            "clientAccountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientUserInvitationOut"])
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
    types["LocationContextIn"] = t.struct(
        {"geoCriteriaIds": t.array(t.integer()).optional()}
    ).named(renames["LocationContextIn"])
    types["LocationContextOut"] = t.struct(
        {
            "geoCriteriaIds": t.array(t.integer()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationContextOut"])
    types["ContactInformationIn"] = t.struct(
        {"name": t.string().optional(), "email": t.string().optional()}
    ).named(renames["ContactInformationIn"])
    types["ContactInformationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContactInformationOut"])
    types["CreativeRestrictionsIn"] = t.struct(
        {
            "creativeFormat": t.string().optional(),
            "creativeSpecifications": t.array(
                t.proxy(renames["CreativeSpecificationIn"])
            ),
            "skippableAdType": t.string().optional(),
        }
    ).named(renames["CreativeRestrictionsIn"])
    types["CreativeRestrictionsOut"] = t.struct(
        {
            "creativeFormat": t.string().optional(),
            "creativeSpecifications": t.array(
                t.proxy(renames["CreativeSpecificationOut"])
            ),
            "skippableAdType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeRestrictionsOut"])
    types["TechnologyTargetingIn"] = t.struct(
        {
            "deviceCategoryTargeting": t.proxy(
                renames["CriteriaTargetingIn"]
            ).optional(),
            "operatingSystemTargeting": t.proxy(
                renames["OperatingSystemTargetingIn"]
            ).optional(),
            "deviceCapabilityTargeting": t.proxy(
                renames["CriteriaTargetingIn"]
            ).optional(),
        }
    ).named(renames["TechnologyTargetingIn"])
    types["TechnologyTargetingOut"] = t.struct(
        {
            "deviceCategoryTargeting": t.proxy(
                renames["CriteriaTargetingOut"]
            ).optional(),
            "operatingSystemTargeting": t.proxy(
                renames["OperatingSystemTargetingOut"]
            ).optional(),
            "deviceCapabilityTargeting": t.proxy(
                renames["CriteriaTargetingOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TechnologyTargetingOut"])
    types["CreativeIn"] = t.struct(
        {
            "clickThroughUrls": t.array(t.string()).optional(),
            "detectedAdvertiserIds": t.array(t.string()).optional(),
            "version": t.integer().optional(),
            "adTechnologyProviders": t.proxy(
                renames["AdTechnologyProvidersIn"]
            ).optional(),
            "html": t.proxy(renames["HtmlContentIn"]).optional(),
            "openAuctionStatus": t.string().optional(),
            "servingRestrictions": t.array(
                t.proxy(renames["ServingRestrictionIn"])
            ).optional(),
            "dealsStatus": t.string().optional(),
            "native": t.proxy(renames["NativeContentIn"]).optional(),
            "detectedDomains": t.array(t.string()).optional(),
            "agencyId": t.string().optional(),
            "video": t.proxy(renames["VideoContentIn"]).optional(),
            "vendorIds": t.array(t.integer()).optional(),
            "detectedProductCategories": t.array(t.integer()).optional(),
            "impressionTrackingUrls": t.array(t.string()).optional(),
            "advertiserName": t.string().optional(),
            "detectedLanguages": t.array(t.string()).optional(),
            "restrictedCategories": t.array(t.string()).optional(),
            "attributes": t.array(t.string()).optional(),
            "declaredClickThroughUrls": t.array(t.string()).optional(),
            "creativeId": t.string().optional(),
            "adChoicesDestinationUrl": t.string().optional(),
            "corrections": t.array(t.proxy(renames["CorrectionIn"])).optional(),
            "apiUpdateTime": t.string().optional(),
            "accountId": t.string().optional(),
            "detectedSensitiveCategories": t.array(t.integer()).optional(),
        }
    ).named(renames["CreativeIn"])
    types["CreativeOut"] = t.struct(
        {
            "clickThroughUrls": t.array(t.string()).optional(),
            "detectedAdvertiserIds": t.array(t.string()).optional(),
            "version": t.integer().optional(),
            "adTechnologyProviders": t.proxy(
                renames["AdTechnologyProvidersOut"]
            ).optional(),
            "html": t.proxy(renames["HtmlContentOut"]).optional(),
            "openAuctionStatus": t.string().optional(),
            "servingRestrictions": t.array(
                t.proxy(renames["ServingRestrictionOut"])
            ).optional(),
            "dealsStatus": t.string().optional(),
            "native": t.proxy(renames["NativeContentOut"]).optional(),
            "detectedDomains": t.array(t.string()).optional(),
            "agencyId": t.string().optional(),
            "video": t.proxy(renames["VideoContentOut"]).optional(),
            "vendorIds": t.array(t.integer()).optional(),
            "detectedProductCategories": t.array(t.integer()).optional(),
            "impressionTrackingUrls": t.array(t.string()).optional(),
            "advertiserName": t.string().optional(),
            "detectedLanguages": t.array(t.string()).optional(),
            "restrictedCategories": t.array(t.string()).optional(),
            "attributes": t.array(t.string()).optional(),
            "declaredClickThroughUrls": t.array(t.string()).optional(),
            "creativeId": t.string().optional(),
            "adChoicesDestinationUrl": t.string().optional(),
            "corrections": t.array(t.proxy(renames["CorrectionOut"])).optional(),
            "apiUpdateTime": t.string().optional(),
            "accountId": t.string().optional(),
            "detectedSensitiveCategories": t.array(t.integer()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeOut"])
    types["ClientIn"] = t.struct(
        {
            "entityId": t.string().optional(),
            "entityType": t.string().optional(),
            "visibleToSeller": t.boolean().optional(),
            "clientName": t.string().optional(),
            "entityName": t.string().optional(),
            "clientAccountId": t.string().optional(),
            "status": t.string().optional(),
            "partnerClientId": t.string().optional(),
            "role": t.string().optional(),
        }
    ).named(renames["ClientIn"])
    types["ClientOut"] = t.struct(
        {
            "entityId": t.string().optional(),
            "entityType": t.string().optional(),
            "visibleToSeller": t.boolean().optional(),
            "clientName": t.string().optional(),
            "entityName": t.string().optional(),
            "clientAccountId": t.string().optional(),
            "status": t.string().optional(),
            "partnerClientId": t.string().optional(),
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientOut"])
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
    types["FilteredBidDetailRowIn"] = t.struct(
        {
            "bidCount": t.proxy(renames["MetricValueIn"]).optional(),
            "detailId": t.integer().optional(),
            "detail": t.string().optional(),
            "rowDimensions": t.proxy(renames["RowDimensionsIn"]).optional(),
        }
    ).named(renames["FilteredBidDetailRowIn"])
    types["FilteredBidDetailRowOut"] = t.struct(
        {
            "bidCount": t.proxy(renames["MetricValueOut"]).optional(),
            "detailId": t.integer().optional(),
            "detail": t.string().optional(),
            "rowDimensions": t.proxy(renames["RowDimensionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilteredBidDetailRowOut"])
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
    types["AdSizeIn"] = t.struct(
        {
            "width": t.string().optional(),
            "height": t.string().optional(),
            "sizeType": t.string().optional(),
        }
    ).named(renames["AdSizeIn"])
    types["AdSizeOut"] = t.struct(
        {
            "width": t.string().optional(),
            "height": t.string().optional(),
            "sizeType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdSizeOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["PublisherProfileIn"] = t.struct(
        {
            "isParent": t.boolean().optional(),
            "directDealsContact": t.string().optional(),
            "googlePlusUrl": t.string().optional(),
            "rateCardInfoUrl": t.string().optional(),
            "topHeadlines": t.array(t.string()).optional(),
            "buyerPitchStatement": t.string().optional(),
            "publisherProfileId": t.string().optional(),
            "overview": t.string().optional(),
            "mediaKitUrl": t.string().optional(),
            "mobileApps": t.array(
                t.proxy(renames["PublisherProfileMobileApplicationIn"])
            ).optional(),
            "domains": t.array(t.string()).optional(),
            "logoUrl": t.string().optional(),
            "samplePageUrl": t.string().optional(),
            "displayName": t.string().optional(),
            "audienceDescription": t.string().optional(),
            "seller": t.proxy(renames["SellerIn"]).optional(),
            "programmaticDealsContact": t.string().optional(),
        }
    ).named(renames["PublisherProfileIn"])
    types["PublisherProfileOut"] = t.struct(
        {
            "isParent": t.boolean().optional(),
            "directDealsContact": t.string().optional(),
            "googlePlusUrl": t.string().optional(),
            "rateCardInfoUrl": t.string().optional(),
            "topHeadlines": t.array(t.string()).optional(),
            "buyerPitchStatement": t.string().optional(),
            "publisherProfileId": t.string().optional(),
            "overview": t.string().optional(),
            "mediaKitUrl": t.string().optional(),
            "mobileApps": t.array(
                t.proxy(renames["PublisherProfileMobileApplicationOut"])
            ).optional(),
            "domains": t.array(t.string()).optional(),
            "logoUrl": t.string().optional(),
            "samplePageUrl": t.string().optional(),
            "displayName": t.string().optional(),
            "audienceDescription": t.string().optional(),
            "seller": t.proxy(renames["SellerOut"]).optional(),
            "programmaticDealsContact": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublisherProfileOut"])
    types["MarketplaceTargetingIn"] = t.struct(
        {
            "technologyTargeting": t.proxy(renames["TechnologyTargetingIn"]).optional(),
            "geoTargeting": t.proxy(renames["CriteriaTargetingIn"]).optional(),
            "inventorySizeTargeting": t.proxy(
                renames["InventorySizeTargetingIn"]
            ).optional(),
            "videoTargeting": t.proxy(renames["VideoTargetingIn"]).optional(),
            "placementTargeting": t.proxy(renames["PlacementTargetingIn"]).optional(),
        }
    ).named(renames["MarketplaceTargetingIn"])
    types["MarketplaceTargetingOut"] = t.struct(
        {
            "technologyTargeting": t.proxy(
                renames["TechnologyTargetingOut"]
            ).optional(),
            "geoTargeting": t.proxy(renames["CriteriaTargetingOut"]).optional(),
            "inventorySizeTargeting": t.proxy(
                renames["InventorySizeTargetingOut"]
            ).optional(),
            "videoTargeting": t.proxy(renames["VideoTargetingOut"]).optional(),
            "placementTargeting": t.proxy(renames["PlacementTargetingOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MarketplaceTargetingOut"])
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
    types["ListBidResponsesWithoutBidsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "bidResponseWithoutBidsStatusRows": t.array(
                t.proxy(renames["BidResponseWithoutBidsStatusRowIn"])
            ).optional(),
        }
    ).named(renames["ListBidResponsesWithoutBidsResponseIn"])
    types["ListBidResponsesWithoutBidsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "bidResponseWithoutBidsStatusRows": t.array(
                t.proxy(renames["BidResponseWithoutBidsStatusRowOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBidResponsesWithoutBidsResponseOut"])
    types["DealPauseStatusIn"] = t.struct(
        {
            "buyerPauseReason": t.string().optional(),
            "hasBuyerPaused": t.boolean().optional(),
            "hasSellerPaused": t.boolean().optional(),
            "firstPausedBy": t.string().optional(),
            "sellerPauseReason": t.string().optional(),
        }
    ).named(renames["DealPauseStatusIn"])
    types["DealPauseStatusOut"] = t.struct(
        {
            "buyerPauseReason": t.string().optional(),
            "hasBuyerPaused": t.boolean().optional(),
            "hasSellerPaused": t.boolean().optional(),
            "firstPausedBy": t.string().optional(),
            "sellerPauseReason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DealPauseStatusOut"])
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
    types["SecurityContextIn"] = t.struct(
        {"securities": t.array(t.string()).optional()}
    ).named(renames["SecurityContextIn"])
    types["SecurityContextOut"] = t.struct(
        {
            "securities": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecurityContextOut"])
    types["RealtimeTimeRangeIn"] = t.struct(
        {"startTimestamp": t.string().optional()}
    ).named(renames["RealtimeTimeRangeIn"])
    types["RealtimeTimeRangeOut"] = t.struct(
        {
            "startTimestamp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RealtimeTimeRangeOut"])
    types["AddNoteRequestIn"] = t.struct(
        {"note": t.proxy(renames["NoteIn"]).optional()}
    ).named(renames["AddNoteRequestIn"])
    types["AddNoteRequestOut"] = t.struct(
        {
            "note": t.proxy(renames["NoteOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddNoteRequestOut"])
    types["PricePerBuyerIn"] = t.struct(
        {
            "advertiserIds": t.array(t.string()).optional(),
            "buyer": t.proxy(renames["BuyerIn"]).optional(),
            "price": t.proxy(renames["PriceIn"]).optional(),
        }
    ).named(renames["PricePerBuyerIn"])
    types["PricePerBuyerOut"] = t.struct(
        {
            "advertiserIds": t.array(t.string()).optional(),
            "buyer": t.proxy(renames["BuyerOut"]).optional(),
            "price": t.proxy(renames["PriceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PricePerBuyerOut"])
    types["CreativeSpecificationIn"] = t.struct(
        {
            "creativeSize": t.proxy(renames["AdSizeIn"]).optional(),
            "creativeCompanionSizes": t.array(t.proxy(renames["AdSizeIn"])).optional(),
        }
    ).named(renames["CreativeSpecificationIn"])
    types["CreativeSpecificationOut"] = t.struct(
        {
            "creativeSize": t.proxy(renames["AdSizeOut"]).optional(),
            "creativeCompanionSizes": t.array(t.proxy(renames["AdSizeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeSpecificationOut"])
    types["BuyerIn"] = t.struct({"accountId": t.string().optional()}).named(
        renames["BuyerIn"]
    )
    types["BuyerOut"] = t.struct(
        {
            "accountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuyerOut"])
    types["TargetingValueIn"] = t.struct(
        {
            "creativeSizeValue": t.proxy(renames["CreativeSizeIn"]).optional(),
            "dayPartTargetingValue": t.proxy(renames["DayPartTargetingIn"]).optional(),
            "longValue": t.string().optional(),
            "stringValue": t.string().optional(),
        }
    ).named(renames["TargetingValueIn"])
    types["TargetingValueOut"] = t.struct(
        {
            "creativeSizeValue": t.proxy(renames["CreativeSizeOut"]).optional(),
            "dayPartTargetingValue": t.proxy(renames["DayPartTargetingOut"]).optional(),
            "longValue": t.string().optional(),
            "stringValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetingValueOut"])
    types["NonGuaranteedFixedPriceTermsIn"] = t.struct(
        {"fixedPrices": t.array(t.proxy(renames["PricePerBuyerIn"])).optional()}
    ).named(renames["NonGuaranteedFixedPriceTermsIn"])
    types["NonGuaranteedFixedPriceTermsOut"] = t.struct(
        {
            "fixedPrices": t.array(t.proxy(renames["PricePerBuyerOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NonGuaranteedFixedPriceTermsOut"])
    types["TargetingCriteriaIn"] = t.struct(
        {
            "exclusions": t.array(t.proxy(renames["TargetingValueIn"])).optional(),
            "inclusions": t.array(t.proxy(renames["TargetingValueIn"])).optional(),
            "key": t.string().optional(),
        }
    ).named(renames["TargetingCriteriaIn"])
    types["TargetingCriteriaOut"] = t.struct(
        {
            "exclusions": t.array(t.proxy(renames["TargetingValueOut"])).optional(),
            "inclusions": t.array(t.proxy(renames["TargetingValueOut"])).optional(),
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetingCriteriaOut"])
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
    types["ResumeProposalRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ResumeProposalRequestIn"]
    )
    types["ResumeProposalRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ResumeProposalRequestOut"])
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
    types["NativeContentIn"] = t.struct(
        {
            "appIcon": t.proxy(renames["ImageIn"]).optional(),
            "starRating": t.number().optional(),
            "image": t.proxy(renames["ImageIn"]).optional(),
            "advertiserName": t.string().optional(),
            "callToAction": t.string().optional(),
            "logo": t.proxy(renames["ImageIn"]).optional(),
            "headline": t.string().optional(),
            "body": t.string().optional(),
            "videoUrl": t.string().optional(),
            "clickLinkUrl": t.string().optional(),
            "storeUrl": t.string().optional(),
            "clickTrackingUrl": t.string().optional(),
            "priceDisplayText": t.string().optional(),
        }
    ).named(renames["NativeContentIn"])
    types["NativeContentOut"] = t.struct(
        {
            "appIcon": t.proxy(renames["ImageOut"]).optional(),
            "starRating": t.number().optional(),
            "image": t.proxy(renames["ImageOut"]).optional(),
            "advertiserName": t.string().optional(),
            "callToAction": t.string().optional(),
            "logo": t.proxy(renames["ImageOut"]).optional(),
            "headline": t.string().optional(),
            "body": t.string().optional(),
            "videoUrl": t.string().optional(),
            "clickLinkUrl": t.string().optional(),
            "storeUrl": t.string().optional(),
            "clickTrackingUrl": t.string().optional(),
            "priceDisplayText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NativeContentOut"])
    types["ServingRestrictionIn"] = t.struct(
        {
            "disapprovalReasons": t.array(t.proxy(renames["DisapprovalIn"])).optional(),
            "contexts": t.array(t.proxy(renames["ServingContextIn"])).optional(),
            "disapproval": t.proxy(renames["DisapprovalIn"]).optional(),
            "status": t.string().optional(),
        }
    ).named(renames["ServingRestrictionIn"])
    types["ServingRestrictionOut"] = t.struct(
        {
            "disapprovalReasons": t.array(
                t.proxy(renames["DisapprovalOut"])
            ).optional(),
            "contexts": t.array(t.proxy(renames["ServingContextOut"])).optional(),
            "disapproval": t.proxy(renames["DisapprovalOut"]).optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServingRestrictionOut"])
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
    types["MetricValueIn"] = t.struct(
        {"value": t.string().optional(), "variance": t.string().optional()}
    ).named(renames["MetricValueIn"])
    types["MetricValueOut"] = t.struct(
        {
            "value": t.string().optional(),
            "variance": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricValueOut"])
    types["ListBidMetricsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "bidMetricsRows": t.array(t.proxy(renames["BidMetricsRowIn"])).optional(),
        }
    ).named(renames["ListBidMetricsResponseIn"])
    types["ListBidMetricsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "bidMetricsRows": t.array(t.proxy(renames["BidMetricsRowOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBidMetricsResponseOut"])
    types["CancelNegotiationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelNegotiationRequestIn"]
    )
    types["CancelNegotiationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelNegotiationRequestOut"])
    types["NoteIn"] = t.struct({"note": t.string().optional()}).named(renames["NoteIn"])
    types["NoteOut"] = t.struct(
        {
            "noteId": t.string().optional(),
            "note": t.string().optional(),
            "creatorRole": t.string().optional(),
            "createTime": t.string().optional(),
            "proposalRevision": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NoteOut"])
    types["CreativeStatusRowIn"] = t.struct(
        {
            "rowDimensions": t.proxy(renames["RowDimensionsIn"]).optional(),
            "creativeStatusId": t.integer().optional(),
            "bidCount": t.proxy(renames["MetricValueIn"]).optional(),
        }
    ).named(renames["CreativeStatusRowIn"])
    types["CreativeStatusRowOut"] = t.struct(
        {
            "rowDimensions": t.proxy(renames["RowDimensionsOut"]).optional(),
            "creativeStatusId": t.integer().optional(),
            "bidCount": t.proxy(renames["MetricValueOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeStatusRowOut"])
    types["ListCreativeStatusBreakdownByDetailResponseIn"] = t.struct(
        {
            "filteredBidDetailRows": t.array(
                t.proxy(renames["FilteredBidDetailRowIn"])
            ).optional(),
            "detailType": t.string().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListCreativeStatusBreakdownByDetailResponseIn"])
    types["ListCreativeStatusBreakdownByDetailResponseOut"] = t.struct(
        {
            "filteredBidDetailRows": t.array(
                t.proxy(renames["FilteredBidDetailRowOut"])
            ).optional(),
            "detailType": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCreativeStatusBreakdownByDetailResponseOut"])
    types["GuaranteedFixedPriceTermsIn"] = t.struct(
        {
            "guaranteedImpressions": t.string().optional(),
            "minimumDailyLooks": t.string().optional(),
            "impressionCap": t.string().optional(),
            "fixedPrices": t.array(t.proxy(renames["PricePerBuyerIn"])).optional(),
            "percentShareOfVoice": t.string().optional(),
            "reservationType": t.string().optional(),
            "guaranteedLooks": t.string().optional(),
        }
    ).named(renames["GuaranteedFixedPriceTermsIn"])
    types["GuaranteedFixedPriceTermsOut"] = t.struct(
        {
            "guaranteedImpressions": t.string().optional(),
            "minimumDailyLooks": t.string().optional(),
            "impressionCap": t.string().optional(),
            "fixedPrices": t.array(t.proxy(renames["PricePerBuyerOut"])).optional(),
            "percentShareOfVoice": t.string().optional(),
            "reservationType": t.string().optional(),
            "guaranteedLooks": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GuaranteedFixedPriceTermsOut"])
    types["FilterSetIn"] = t.struct(
        {
            "timeSeriesGranularity": t.string().optional(),
            "platforms": t.array(t.string()).optional(),
            "breakdownDimensions": t.array(t.string()).optional(),
            "realtimeTimeRange": t.proxy(renames["RealtimeTimeRangeIn"]).optional(),
            "creativeId": t.string().optional(),
            "sellerNetworkIds": t.array(t.integer()).optional(),
            "format": t.string().optional(),
            "formats": t.array(t.string()).optional(),
            "environment": t.string().optional(),
            "publisherIdentifiers": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "dealId": t.string().optional(),
            "absoluteDateRange": t.proxy(renames["AbsoluteDateRangeIn"]).optional(),
            "relativeDateRange": t.proxy(renames["RelativeDateRangeIn"]).optional(),
        }
    ).named(renames["FilterSetIn"])
    types["FilterSetOut"] = t.struct(
        {
            "timeSeriesGranularity": t.string().optional(),
            "platforms": t.array(t.string()).optional(),
            "breakdownDimensions": t.array(t.string()).optional(),
            "realtimeTimeRange": t.proxy(renames["RealtimeTimeRangeOut"]).optional(),
            "creativeId": t.string().optional(),
            "sellerNetworkIds": t.array(t.integer()).optional(),
            "format": t.string().optional(),
            "formats": t.array(t.string()).optional(),
            "environment": t.string().optional(),
            "publisherIdentifiers": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "dealId": t.string().optional(),
            "absoluteDateRange": t.proxy(renames["AbsoluteDateRangeOut"]).optional(),
            "relativeDateRange": t.proxy(renames["RelativeDateRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterSetOut"])
    types["PauseProposalDealsRequestIn"] = t.struct(
        {
            "reason": t.string().optional(),
            "externalDealIds": t.array(t.string()).optional(),
        }
    ).named(renames["PauseProposalDealsRequestIn"])
    types["PauseProposalDealsRequestOut"] = t.struct(
        {
            "reason": t.string().optional(),
            "externalDealIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PauseProposalDealsRequestOut"])
    types["DealTermsIn"] = t.struct(
        {
            "description": t.string().optional(),
            "nonGuaranteedAuctionTerms": t.proxy(
                renames["NonGuaranteedAuctionTermsIn"]
            ).optional(),
            "estimatedGrossSpend": t.proxy(renames["PriceIn"]).optional(),
            "sellerTimeZone": t.string().optional(),
            "nonGuaranteedFixedPriceTerms": t.proxy(
                renames["NonGuaranteedFixedPriceTermsIn"]
            ).optional(),
            "brandingType": t.string().optional(),
            "guaranteedFixedPriceTerms": t.proxy(
                renames["GuaranteedFixedPriceTermsIn"]
            ).optional(),
            "estimatedImpressionsPerDay": t.string().optional(),
        }
    ).named(renames["DealTermsIn"])
    types["DealTermsOut"] = t.struct(
        {
            "description": t.string().optional(),
            "nonGuaranteedAuctionTerms": t.proxy(
                renames["NonGuaranteedAuctionTermsOut"]
            ).optional(),
            "estimatedGrossSpend": t.proxy(renames["PriceOut"]).optional(),
            "sellerTimeZone": t.string().optional(),
            "nonGuaranteedFixedPriceTerms": t.proxy(
                renames["NonGuaranteedFixedPriceTermsOut"]
            ).optional(),
            "brandingType": t.string().optional(),
            "guaranteedFixedPriceTerms": t.proxy(
                renames["GuaranteedFixedPriceTermsOut"]
            ).optional(),
            "estimatedImpressionsPerDay": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DealTermsOut"])
    types["BidMetricsRowIn"] = t.struct(
        {
            "rowDimensions": t.proxy(renames["RowDimensionsIn"]).optional(),
            "viewableImpressions": t.proxy(renames["MetricValueIn"]).optional(),
            "impressionsWon": t.proxy(renames["MetricValueIn"]).optional(),
            "bids": t.proxy(renames["MetricValueIn"]).optional(),
            "measurableImpressions": t.proxy(renames["MetricValueIn"]).optional(),
            "reachedQueries": t.proxy(renames["MetricValueIn"]).optional(),
            "billedImpressions": t.proxy(renames["MetricValueIn"]).optional(),
            "bidsInAuction": t.proxy(renames["MetricValueIn"]).optional(),
        }
    ).named(renames["BidMetricsRowIn"])
    types["BidMetricsRowOut"] = t.struct(
        {
            "rowDimensions": t.proxy(renames["RowDimensionsOut"]).optional(),
            "viewableImpressions": t.proxy(renames["MetricValueOut"]).optional(),
            "impressionsWon": t.proxy(renames["MetricValueOut"]).optional(),
            "bids": t.proxy(renames["MetricValueOut"]).optional(),
            "measurableImpressions": t.proxy(renames["MetricValueOut"]).optional(),
            "reachedQueries": t.proxy(renames["MetricValueOut"]).optional(),
            "billedImpressions": t.proxy(renames["MetricValueOut"]).optional(),
            "bidsInAuction": t.proxy(renames["MetricValueOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BidMetricsRowOut"])
    types["PauseProposalRequestIn"] = t.struct({"reason": t.string().optional()}).named(
        renames["PauseProposalRequestIn"]
    )
    types["PauseProposalRequestOut"] = t.struct(
        {
            "reason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PauseProposalRequestOut"])
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
    types["DealIn"] = t.struct(
        {
            "availableStartTime": t.string().optional(),
            "createProductRevision": t.string().optional(),
            "targetingCriterion": t.array(
                t.proxy(renames["TargetingCriteriaIn"])
            ).optional(),
            "displayName": t.string().optional(),
            "deliveryControl": t.proxy(renames["DeliveryControlIn"]).optional(),
            "syndicationProduct": t.string().optional(),
            "dealTerms": t.proxy(renames["DealTermsIn"]).optional(),
            "createProductId": t.string().optional(),
            "webPropertyCode": t.string().optional(),
            "description": t.string().optional(),
            "buyerPrivateData": t.proxy(renames["PrivateDataIn"]).optional(),
            "availableEndTime": t.string().optional(),
        }
    ).named(renames["DealIn"])
    types["DealOut"] = t.struct(
        {
            "availableStartTime": t.string().optional(),
            "createProductRevision": t.string().optional(),
            "dealId": t.string().optional(),
            "isSetupComplete": t.boolean().optional(),
            "sellerContacts": t.array(
                t.proxy(renames["ContactInformationOut"])
            ).optional(),
            "creativeSafeFrameCompatibility": t.string().optional(),
            "proposalId": t.string().optional(),
            "dealServingMetadata": t.proxy(
                renames["DealServingMetadataOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "targetingCriterion": t.array(
                t.proxy(renames["TargetingCriteriaOut"])
            ).optional(),
            "displayName": t.string().optional(),
            "creativePreApprovalPolicy": t.string().optional(),
            "updateTime": t.string().optional(),
            "deliveryControl": t.proxy(renames["DeliveryControlOut"]).optional(),
            "syndicationProduct": t.string().optional(),
            "dealTerms": t.proxy(renames["DealTermsOut"]).optional(),
            "targeting": t.proxy(renames["MarketplaceTargetingOut"]).optional(),
            "createProductId": t.string().optional(),
            "creativeRestrictions": t.proxy(
                renames["CreativeRestrictionsOut"]
            ).optional(),
            "webPropertyCode": t.string().optional(),
            "externalDealId": t.string().optional(),
            "programmaticCreativeSource": t.string().optional(),
            "description": t.string().optional(),
            "buyerPrivateData": t.proxy(renames["PrivateDataOut"]).optional(),
            "availableEndTime": t.string().optional(),
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
    types["ResumeProposalDealsRequestIn"] = t.struct(
        {"externalDealIds": t.array(t.string()).optional()}
    ).named(renames["ResumeProposalDealsRequestIn"])
    types["ResumeProposalDealsRequestOut"] = t.struct(
        {
            "externalDealIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResumeProposalDealsRequestOut"])
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
    types["RemoveDealAssociationRequestIn"] = t.struct(
        {"association": t.proxy(renames["CreativeDealAssociationIn"]).optional()}
    ).named(renames["RemoveDealAssociationRequestIn"])
    types["RemoveDealAssociationRequestOut"] = t.struct(
        {
            "association": t.proxy(renames["CreativeDealAssociationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveDealAssociationRequestOut"])
    types["AppContextIn"] = t.struct(
        {"appTypes": t.array(t.string()).optional()}
    ).named(renames["AppContextIn"])
    types["AppContextOut"] = t.struct(
        {
            "appTypes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppContextOut"])
    types["FirstPartyMobileApplicationTargetingIn"] = t.struct(
        {
            "targetedAppIds": t.array(t.string()).optional(),
            "excludedAppIds": t.array(t.string()).optional(),
        }
    ).named(renames["FirstPartyMobileApplicationTargetingIn"])
    types["FirstPartyMobileApplicationTargetingOut"] = t.struct(
        {
            "targetedAppIds": t.array(t.string()).optional(),
            "excludedAppIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FirstPartyMobileApplicationTargetingOut"])
    types["TimeOfDayIn"] = t.struct(
        {
            "hours": t.integer().optional(),
            "seconds": t.integer().optional(),
            "minutes": t.integer().optional(),
            "nanos": t.integer().optional(),
        }
    ).named(renames["TimeOfDayIn"])
    types["TimeOfDayOut"] = t.struct(
        {
            "hours": t.integer().optional(),
            "seconds": t.integer().optional(),
            "minutes": t.integer().optional(),
            "nanos": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeOfDayOut"])
    types["ProposalIn"] = t.struct(
        {
            "seller": t.proxy(renames["SellerIn"]).optional(),
            "buyerPrivateData": t.proxy(renames["PrivateDataIn"]).optional(),
            "displayName": t.string().optional(),
            "deals": t.array(t.proxy(renames["DealIn"])).optional(),
            "buyer": t.proxy(renames["BuyerIn"]).optional(),
            "buyerContacts": t.array(
                t.proxy(renames["ContactInformationIn"])
            ).optional(),
        }
    ).named(renames["ProposalIn"])
    types["ProposalOut"] = t.struct(
        {
            "isRenegotiating": t.boolean().optional(),
            "seller": t.proxy(renames["SellerOut"]).optional(),
            "proposalState": t.string().optional(),
            "billedBuyer": t.proxy(renames["BuyerOut"]).optional(),
            "termsAndConditions": t.string().optional(),
            "privateAuctionId": t.string().optional(),
            "proposalId": t.string().optional(),
            "buyerPrivateData": t.proxy(renames["PrivateDataOut"]).optional(),
            "sellerContacts": t.array(
                t.proxy(renames["ContactInformationOut"])
            ).optional(),
            "isSetupComplete": t.boolean().optional(),
            "updateTime": t.string().optional(),
            "displayName": t.string().optional(),
            "deals": t.array(t.proxy(renames["DealOut"])).optional(),
            "originatorRole": t.string().optional(),
            "lastUpdaterOrCommentorRole": t.string().optional(),
            "notes": t.array(t.proxy(renames["NoteOut"])).optional(),
            "proposalRevision": t.string().optional(),
            "buyer": t.proxy(renames["BuyerOut"]).optional(),
            "buyerContacts": t.array(
                t.proxy(renames["ContactInformationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProposalOut"])
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
    types["ServingContextIn"] = t.struct(
        {
            "auctionType": t.proxy(renames["AuctionContextIn"]).optional(),
            "securityType": t.proxy(renames["SecurityContextIn"]).optional(),
            "appType": t.proxy(renames["AppContextIn"]).optional(),
            "platform": t.proxy(renames["PlatformContextIn"]).optional(),
            "location": t.proxy(renames["LocationContextIn"]).optional(),
            "all": t.string().optional(),
        }
    ).named(renames["ServingContextIn"])
    types["ServingContextOut"] = t.struct(
        {
            "auctionType": t.proxy(renames["AuctionContextOut"]).optional(),
            "securityType": t.proxy(renames["SecurityContextOut"]).optional(),
            "appType": t.proxy(renames["AppContextOut"]).optional(),
            "platform": t.proxy(renames["PlatformContextOut"]).optional(),
            "location": t.proxy(renames["LocationContextOut"]).optional(),
            "all": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServingContextOut"])
    types["PrivateDataIn"] = t.struct({"referenceId": t.string().optional()}).named(
        renames["PrivateDataIn"]
    )
    types["PrivateDataOut"] = t.struct(
        {
            "referenceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrivateDataOut"])
    types["DealServingMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DealServingMetadataIn"]
    )
    types["DealServingMetadataOut"] = t.struct(
        {
            "dealPauseStatus": t.proxy(renames["DealPauseStatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DealServingMetadataOut"])
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
    types["ListClientUsersResponseIn"] = t.struct(
        {
            "users": t.array(t.proxy(renames["ClientUserIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListClientUsersResponseIn"])
    types["ListClientUsersResponseOut"] = t.struct(
        {
            "users": t.array(t.proxy(renames["ClientUserOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListClientUsersResponseOut"])
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
    types["CorrectionIn"] = t.struct(
        {
            "contexts": t.array(t.proxy(renames["ServingContextIn"])).optional(),
            "details": t.array(t.string()).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["CorrectionIn"])
    types["CorrectionOut"] = t.struct(
        {
            "contexts": t.array(t.proxy(renames["ServingContextOut"])).optional(),
            "details": t.array(t.string()).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CorrectionOut"])
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
    types["CreativeDealAssociationIn"] = t.struct(
        {
            "creativeId": t.string().optional(),
            "accountId": t.string().optional(),
            "dealsId": t.string().optional(),
        }
    ).named(renames["CreativeDealAssociationIn"])
    types["CreativeDealAssociationOut"] = t.struct(
        {
            "creativeId": t.string().optional(),
            "accountId": t.string().optional(),
            "dealsId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeDealAssociationOut"])
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
    types["ClientUserIn"] = t.struct(
        {
            "email": t.string().optional(),
            "status": t.string().optional(),
            "userId": t.string().optional(),
            "clientAccountId": t.string().optional(),
        }
    ).named(renames["ClientUserIn"])
    types["ClientUserOut"] = t.struct(
        {
            "email": t.string().optional(),
            "status": t.string().optional(),
            "userId": t.string().optional(),
            "clientAccountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientUserOut"])
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
    types["CreativeSizeIn"] = t.struct(
        {
            "skippableAdType": t.string().optional(),
            "companionSizes": t.array(t.proxy(renames["SizeIn"])).optional(),
            "size": t.proxy(renames["SizeIn"]).optional(),
            "nativeTemplate": t.string().optional(),
            "creativeSizeType": t.string().optional(),
            "allowedFormats": t.array(t.string()).optional(),
        }
    ).named(renames["CreativeSizeIn"])
    types["CreativeSizeOut"] = t.struct(
        {
            "skippableAdType": t.string().optional(),
            "companionSizes": t.array(t.proxy(renames["SizeOut"])).optional(),
            "size": t.proxy(renames["SizeOut"]).optional(),
            "nativeTemplate": t.string().optional(),
            "creativeSizeType": t.string().optional(),
            "allowedFormats": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeSizeOut"])
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
    types["AcceptProposalRequestIn"] = t.struct(
        {"proposalRevision": t.string().optional()}
    ).named(renames["AcceptProposalRequestIn"])
    types["AcceptProposalRequestOut"] = t.struct(
        {
            "proposalRevision": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AcceptProposalRequestOut"])
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
    types["ImpressionMetricsRowIn"] = t.struct(
        {
            "bidRequests": t.proxy(renames["MetricValueIn"]).optional(),
            "rowDimensions": t.proxy(renames["RowDimensionsIn"]).optional(),
            "successfulResponses": t.proxy(renames["MetricValueIn"]).optional(),
            "availableImpressions": t.proxy(renames["MetricValueIn"]).optional(),
            "inventoryMatches": t.proxy(renames["MetricValueIn"]).optional(),
            "responsesWithBids": t.proxy(renames["MetricValueIn"]).optional(),
        }
    ).named(renames["ImpressionMetricsRowIn"])
    types["ImpressionMetricsRowOut"] = t.struct(
        {
            "bidRequests": t.proxy(renames["MetricValueOut"]).optional(),
            "rowDimensions": t.proxy(renames["RowDimensionsOut"]).optional(),
            "successfulResponses": t.proxy(renames["MetricValueOut"]).optional(),
            "availableImpressions": t.proxy(renames["MetricValueOut"]).optional(),
            "inventoryMatches": t.proxy(renames["MetricValueOut"]).optional(),
            "responsesWithBids": t.proxy(renames["MetricValueOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImpressionMetricsRowOut"])
    types["AuctionContextIn"] = t.struct(
        {"auctionTypes": t.array(t.string()).optional()}
    ).named(renames["AuctionContextIn"])
    types["AuctionContextOut"] = t.struct(
        {
            "auctionTypes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuctionContextOut"])
    types["CompleteSetupRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CompleteSetupRequestIn"]
    )
    types["CompleteSetupRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CompleteSetupRequestOut"])
    types["HtmlContentIn"] = t.struct(
        {
            "height": t.integer().optional(),
            "width": t.integer().optional(),
            "snippet": t.string().optional(),
        }
    ).named(renames["HtmlContentIn"])
    types["HtmlContentOut"] = t.struct(
        {
            "height": t.integer().optional(),
            "width": t.integer().optional(),
            "snippet": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HtmlContentOut"])
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
    types["WatchCreativeRequestIn"] = t.struct({"topic": t.string().optional()}).named(
        renames["WatchCreativeRequestIn"]
    )
    types["WatchCreativeRequestOut"] = t.struct(
        {
            "topic": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WatchCreativeRequestOut"])
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
    types["ListFilteredBidsResponseIn"] = t.struct(
        {
            "creativeStatusRows": t.array(
                t.proxy(renames["CreativeStatusRowIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListFilteredBidsResponseIn"])
    types["ListFilteredBidsResponseOut"] = t.struct(
        {
            "creativeStatusRows": t.array(
                t.proxy(renames["CreativeStatusRowOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListFilteredBidsResponseOut"])
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

    functions = {}
    functions["accountsFinalizedProposalsList"] = adexchangebuyer2.post(
        "v2beta1/accounts/{accountId}/finalizedProposals/{proposalId}:pause",
        t.struct(
            {
                "proposalId": t.string().optional(),
                "accountId": t.string().optional(),
                "reason": t.string().optional(),
                "externalDealIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProposalOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsFinalizedProposalsResume"] = adexchangebuyer2.post(
        "v2beta1/accounts/{accountId}/finalizedProposals/{proposalId}:pause",
        t.struct(
            {
                "proposalId": t.string().optional(),
                "accountId": t.string().optional(),
                "reason": t.string().optional(),
                "externalDealIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProposalOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsFinalizedProposalsPause"] = adexchangebuyer2.post(
        "v2beta1/accounts/{accountId}/finalizedProposals/{proposalId}:pause",
        t.struct(
            {
                "proposalId": t.string().optional(),
                "accountId": t.string().optional(),
                "reason": t.string().optional(),
                "externalDealIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProposalOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsProductsGet"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/products",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "accountId": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListProductsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsProductsList"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/products",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "accountId": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListProductsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCreativesList"] = adexchangebuyer2.post(
        "v2beta1/accounts/{accountId}/creatives/{creativeId}:watch",
        t.struct(
            {
                "creativeId": t.string().optional(),
                "accountId": t.string().optional(),
                "topic": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCreativesGet"] = adexchangebuyer2.post(
        "v2beta1/accounts/{accountId}/creatives/{creativeId}:watch",
        t.struct(
            {
                "creativeId": t.string().optional(),
                "accountId": t.string().optional(),
                "topic": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCreativesUpdate"] = adexchangebuyer2.post(
        "v2beta1/accounts/{accountId}/creatives/{creativeId}:watch",
        t.struct(
            {
                "creativeId": t.string().optional(),
                "accountId": t.string().optional(),
                "topic": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCreativesCreate"] = adexchangebuyer2.post(
        "v2beta1/accounts/{accountId}/creatives/{creativeId}:watch",
        t.struct(
            {
                "creativeId": t.string().optional(),
                "accountId": t.string().optional(),
                "topic": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCreativesStopWatching"] = adexchangebuyer2.post(
        "v2beta1/accounts/{accountId}/creatives/{creativeId}:watch",
        t.struct(
            {
                "creativeId": t.string().optional(),
                "accountId": t.string().optional(),
                "topic": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCreativesWatch"] = adexchangebuyer2.post(
        "v2beta1/accounts/{accountId}/creatives/{creativeId}:watch",
        t.struct(
            {
                "creativeId": t.string().optional(),
                "accountId": t.string().optional(),
                "topic": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "accountId": t.string().optional(),
                "query": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "accountId": t.string().optional(),
                "query": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "accountId": t.string().optional(),
                "query": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDealAssociationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsClientsList"] = adexchangebuyer2.post(
        "v2beta1/accounts/{accountId}/clients",
        t.struct(
            {
                "accountId": t.string().optional(),
                "entityId": t.string().optional(),
                "entityType": t.string().optional(),
                "visibleToSeller": t.boolean().optional(),
                "clientName": t.string().optional(),
                "entityName": t.string().optional(),
                "clientAccountId": t.string().optional(),
                "status": t.string().optional(),
                "partnerClientId": t.string().optional(),
                "role": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClientOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsClientsUpdate"] = adexchangebuyer2.post(
        "v2beta1/accounts/{accountId}/clients",
        t.struct(
            {
                "accountId": t.string().optional(),
                "entityId": t.string().optional(),
                "entityType": t.string().optional(),
                "visibleToSeller": t.boolean().optional(),
                "clientName": t.string().optional(),
                "entityName": t.string().optional(),
                "clientAccountId": t.string().optional(),
                "status": t.string().optional(),
                "partnerClientId": t.string().optional(),
                "role": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClientOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsClientsGet"] = adexchangebuyer2.post(
        "v2beta1/accounts/{accountId}/clients",
        t.struct(
            {
                "accountId": t.string().optional(),
                "entityId": t.string().optional(),
                "entityType": t.string().optional(),
                "visibleToSeller": t.boolean().optional(),
                "clientName": t.string().optional(),
                "entityName": t.string().optional(),
                "clientAccountId": t.string().optional(),
                "status": t.string().optional(),
                "partnerClientId": t.string().optional(),
                "role": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClientOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsClientsCreate"] = adexchangebuyer2.post(
        "v2beta1/accounts/{accountId}/clients",
        t.struct(
            {
                "accountId": t.string().optional(),
                "entityId": t.string().optional(),
                "entityType": t.string().optional(),
                "visibleToSeller": t.boolean().optional(),
                "clientName": t.string().optional(),
                "entityName": t.string().optional(),
                "clientAccountId": t.string().optional(),
                "status": t.string().optional(),
                "partnerClientId": t.string().optional(),
                "role": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClientOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsClientsInvitationsCreate"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/clients/{clientAccountId}/invitations/{invitationId}",
        t.struct(
            {
                "clientAccountId": t.string().optional(),
                "invitationId": t.string().optional(),
                "accountId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClientUserInvitationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsClientsInvitationsList"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/clients/{clientAccountId}/invitations/{invitationId}",
        t.struct(
            {
                "clientAccountId": t.string().optional(),
                "invitationId": t.string().optional(),
                "accountId": t.string().optional(),
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
                "invitationId": t.string().optional(),
                "accountId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClientUserInvitationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsClientsUsersGet"] = adexchangebuyer2.put(
        "v2beta1/accounts/{accountId}/clients/{clientAccountId}/users/{userId}",
        t.struct(
            {
                "clientAccountId": t.string().optional(),
                "accountId": t.string().optional(),
                "userId": t.string().optional(),
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
                "clientAccountId": t.string().optional(),
                "accountId": t.string().optional(),
                "userId": t.string().optional(),
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
                "clientAccountId": t.string().optional(),
                "accountId": t.string().optional(),
                "userId": t.string().optional(),
                "email": t.string().optional(),
                "status": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClientUserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsProposalsAddNote"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/proposals",
        t.struct(
            {
                "filterSyntax": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "accountId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListProposalsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsProposalsCompleteSetup"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/proposals",
        t.struct(
            {
                "filterSyntax": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "accountId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListProposalsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsProposalsCreate"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/proposals",
        t.struct(
            {
                "filterSyntax": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "accountId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListProposalsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsProposalsGet"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/proposals",
        t.struct(
            {
                "filterSyntax": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "accountId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListProposalsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsProposalsAccept"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/proposals",
        t.struct(
            {
                "filterSyntax": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "accountId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListProposalsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsProposalsPause"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/proposals",
        t.struct(
            {
                "filterSyntax": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "accountId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListProposalsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsProposalsResume"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/proposals",
        t.struct(
            {
                "filterSyntax": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "accountId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListProposalsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsProposalsCancelNegotiation"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/proposals",
        t.struct(
            {
                "filterSyntax": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "accountId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListProposalsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsProposalsUpdate"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/proposals",
        t.struct(
            {
                "filterSyntax": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "accountId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListProposalsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsProposalsList"] = adexchangebuyer2.get(
        "v2beta1/accounts/{accountId}/proposals",
        t.struct(
            {
                "filterSyntax": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "accountId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListProposalsResponseOut"]),
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
    functions["biddersAccountsFilterSetsDelete"] = adexchangebuyer2.get(
        "v2beta1/{ownerName}/filterSets",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "ownerName": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "ownerName": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "ownerName": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "ownerName": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFilterSetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersAccountsFilterSetsFilteredBidsList"] = adexchangebuyer2.get(
        "v2beta1/{filterSetName}/filteredBids",
        t.struct(
            {
                "filterSetName": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
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
                "creativeStatusId": t.integer().optional(),
                "pageSize": t.integer().optional(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filterSetName": t.string().optional(),
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
    functions[
        "biddersAccountsFilterSetsBidResponsesWithoutBidsList"
    ] = adexchangebuyer2.get(
        "v2beta1/{filterSetName}/bidResponsesWithoutBids",
        t.struct(
            {
                "filterSetName": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBidResponsesWithoutBidsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersAccountsFilterSetsBidResponseErrorsList"] = adexchangebuyer2.get(
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
    functions["biddersFilterSetsList"] = adexchangebuyer2.post(
        "v2beta1/{ownerName}/filterSets",
        t.struct(
            {
                "ownerName": t.string().optional(),
                "isTransient": t.boolean().optional(),
                "timeSeriesGranularity": t.string().optional(),
                "platforms": t.array(t.string()).optional(),
                "breakdownDimensions": t.array(t.string()).optional(),
                "realtimeTimeRange": t.proxy(renames["RealtimeTimeRangeIn"]).optional(),
                "creativeId": t.string().optional(),
                "sellerNetworkIds": t.array(t.integer()).optional(),
                "format": t.string().optional(),
                "formats": t.array(t.string()).optional(),
                "environment": t.string().optional(),
                "publisherIdentifiers": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "dealId": t.string().optional(),
                "absoluteDateRange": t.proxy(renames["AbsoluteDateRangeIn"]).optional(),
                "relativeDateRange": t.proxy(renames["RelativeDateRangeIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FilterSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersFilterSetsDelete"] = adexchangebuyer2.post(
        "v2beta1/{ownerName}/filterSets",
        t.struct(
            {
                "ownerName": t.string().optional(),
                "isTransient": t.boolean().optional(),
                "timeSeriesGranularity": t.string().optional(),
                "platforms": t.array(t.string()).optional(),
                "breakdownDimensions": t.array(t.string()).optional(),
                "realtimeTimeRange": t.proxy(renames["RealtimeTimeRangeIn"]).optional(),
                "creativeId": t.string().optional(),
                "sellerNetworkIds": t.array(t.integer()).optional(),
                "format": t.string().optional(),
                "formats": t.array(t.string()).optional(),
                "environment": t.string().optional(),
                "publisherIdentifiers": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "dealId": t.string().optional(),
                "absoluteDateRange": t.proxy(renames["AbsoluteDateRangeIn"]).optional(),
                "relativeDateRange": t.proxy(renames["RelativeDateRangeIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FilterSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersFilterSetsGet"] = adexchangebuyer2.post(
        "v2beta1/{ownerName}/filterSets",
        t.struct(
            {
                "ownerName": t.string().optional(),
                "isTransient": t.boolean().optional(),
                "timeSeriesGranularity": t.string().optional(),
                "platforms": t.array(t.string()).optional(),
                "breakdownDimensions": t.array(t.string()).optional(),
                "realtimeTimeRange": t.proxy(renames["RealtimeTimeRangeIn"]).optional(),
                "creativeId": t.string().optional(),
                "sellerNetworkIds": t.array(t.integer()).optional(),
                "format": t.string().optional(),
                "formats": t.array(t.string()).optional(),
                "environment": t.string().optional(),
                "publisherIdentifiers": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "dealId": t.string().optional(),
                "absoluteDateRange": t.proxy(renames["AbsoluteDateRangeIn"]).optional(),
                "relativeDateRange": t.proxy(renames["RelativeDateRangeIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FilterSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersFilterSetsCreate"] = adexchangebuyer2.post(
        "v2beta1/{ownerName}/filterSets",
        t.struct(
            {
                "ownerName": t.string().optional(),
                "isTransient": t.boolean().optional(),
                "timeSeriesGranularity": t.string().optional(),
                "platforms": t.array(t.string()).optional(),
                "breakdownDimensions": t.array(t.string()).optional(),
                "realtimeTimeRange": t.proxy(renames["RealtimeTimeRangeIn"]).optional(),
                "creativeId": t.string().optional(),
                "sellerNetworkIds": t.array(t.integer()).optional(),
                "format": t.string().optional(),
                "formats": t.array(t.string()).optional(),
                "environment": t.string().optional(),
                "publisherIdentifiers": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "dealId": t.string().optional(),
                "absoluteDateRange": t.proxy(renames["AbsoluteDateRangeIn"]).optional(),
                "relativeDateRange": t.proxy(renames["RelativeDateRangeIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FilterSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersFilterSetsBidResponsesWithoutBidsList"] = adexchangebuyer2.get(
        "v2beta1/{filterSetName}/bidResponsesWithoutBids",
        t.struct(
            {
                "filterSetName": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBidResponsesWithoutBidsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersFilterSetsBidMetricsList"] = adexchangebuyer2.get(
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
    functions["biddersFilterSetsNonBillableWinningBidsList"] = adexchangebuyer2.get(
        "v2beta1/{filterSetName}/nonBillableWinningBids",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filterSetName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListNonBillableWinningBidsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersFilterSetsImpressionMetricsList"] = adexchangebuyer2.get(
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
    functions["biddersFilterSetsFilteredBidsList"] = adexchangebuyer2.get(
        "v2beta1/{filterSetName}/filteredBids",
        t.struct(
            {
                "filterSetName": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "filterSetName": t.string().optional(),
                "pageSize": t.integer().optional(),
                "creativeStatusId": t.integer().optional(),
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
    functions["biddersFilterSetsFilteredBidRequestsList"] = adexchangebuyer2.get(
        "v2beta1/{filterSetName}/filteredBidRequests",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filterSetName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFilteredBidRequestsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="adexchangebuyer2",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
