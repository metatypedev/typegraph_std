from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_authorizedbuyersmarketplace() -> Import:
    authorizedbuyersmarketplace = HTTPRuntime(
        "https://authorizedbuyersmarketplace.googleapis.com/"
    )

    renames = {
        "ErrorResponse": "_authorizedbuyersmarketplace_1_ErrorResponse",
        "PublisherProfileMobileApplicationIn": "_authorizedbuyersmarketplace_2_PublisherProfileMobileApplicationIn",
        "PublisherProfileMobileApplicationOut": "_authorizedbuyersmarketplace_3_PublisherProfileMobileApplicationOut",
        "RtbMetricsIn": "_authorizedbuyersmarketplace_4_RtbMetricsIn",
        "RtbMetricsOut": "_authorizedbuyersmarketplace_5_RtbMetricsOut",
        "MobileApplicationTargetingIn": "_authorizedbuyersmarketplace_6_MobileApplicationTargetingIn",
        "MobileApplicationTargetingOut": "_authorizedbuyersmarketplace_7_MobileApplicationTargetingOut",
        "BatchUpdateDealsRequestIn": "_authorizedbuyersmarketplace_8_BatchUpdateDealsRequestIn",
        "BatchUpdateDealsRequestOut": "_authorizedbuyersmarketplace_9_BatchUpdateDealsRequestOut",
        "ListClientUsersResponseIn": "_authorizedbuyersmarketplace_10_ListClientUsersResponseIn",
        "ListClientUsersResponseOut": "_authorizedbuyersmarketplace_11_ListClientUsersResponseOut",
        "ActivateClientRequestIn": "_authorizedbuyersmarketplace_12_ActivateClientRequestIn",
        "ActivateClientRequestOut": "_authorizedbuyersmarketplace_13_ActivateClientRequestOut",
        "DeliveryControlIn": "_authorizedbuyersmarketplace_14_DeliveryControlIn",
        "DeliveryControlOut": "_authorizedbuyersmarketplace_15_DeliveryControlOut",
        "MarketplaceTargetingIn": "_authorizedbuyersmarketplace_16_MarketplaceTargetingIn",
        "MarketplaceTargetingOut": "_authorizedbuyersmarketplace_17_MarketplaceTargetingOut",
        "ListPublisherProfilesResponseIn": "_authorizedbuyersmarketplace_18_ListPublisherProfilesResponseIn",
        "ListPublisherProfilesResponseOut": "_authorizedbuyersmarketplace_19_ListPublisherProfilesResponseOut",
        "CriteriaTargetingIn": "_authorizedbuyersmarketplace_20_CriteriaTargetingIn",
        "CriteriaTargetingOut": "_authorizedbuyersmarketplace_21_CriteriaTargetingOut",
        "SetReadyToServeRequestIn": "_authorizedbuyersmarketplace_22_SetReadyToServeRequestIn",
        "SetReadyToServeRequestOut": "_authorizedbuyersmarketplace_23_SetReadyToServeRequestOut",
        "SubscribeClientsRequestIn": "_authorizedbuyersmarketplace_24_SubscribeClientsRequestIn",
        "SubscribeClientsRequestOut": "_authorizedbuyersmarketplace_25_SubscribeClientsRequestOut",
        "TechnologyTargetingIn": "_authorizedbuyersmarketplace_26_TechnologyTargetingIn",
        "TechnologyTargetingOut": "_authorizedbuyersmarketplace_27_TechnologyTargetingOut",
        "SubscribeAuctionPackageRequestIn": "_authorizedbuyersmarketplace_28_SubscribeAuctionPackageRequestIn",
        "SubscribeAuctionPackageRequestOut": "_authorizedbuyersmarketplace_29_SubscribeAuctionPackageRequestOut",
        "DeactivateClientUserRequestIn": "_authorizedbuyersmarketplace_30_DeactivateClientUserRequestIn",
        "DeactivateClientUserRequestOut": "_authorizedbuyersmarketplace_31_DeactivateClientUserRequestOut",
        "ResumeFinalizedDealRequestIn": "_authorizedbuyersmarketplace_32_ResumeFinalizedDealRequestIn",
        "ResumeFinalizedDealRequestOut": "_authorizedbuyersmarketplace_33_ResumeFinalizedDealRequestOut",
        "ProposalIn": "_authorizedbuyersmarketplace_34_ProposalIn",
        "ProposalOut": "_authorizedbuyersmarketplace_35_ProposalOut",
        "AddCreativeRequestIn": "_authorizedbuyersmarketplace_36_AddCreativeRequestIn",
        "AddCreativeRequestOut": "_authorizedbuyersmarketplace_37_AddCreativeRequestOut",
        "PrivateAuctionTermsIn": "_authorizedbuyersmarketplace_38_PrivateAuctionTermsIn",
        "PrivateAuctionTermsOut": "_authorizedbuyersmarketplace_39_PrivateAuctionTermsOut",
        "CreativeRequirementsIn": "_authorizedbuyersmarketplace_40_CreativeRequirementsIn",
        "CreativeRequirementsOut": "_authorizedbuyersmarketplace_41_CreativeRequirementsOut",
        "FinalizedDealIn": "_authorizedbuyersmarketplace_42_FinalizedDealIn",
        "FinalizedDealOut": "_authorizedbuyersmarketplace_43_FinalizedDealOut",
        "UpdateDealRequestIn": "_authorizedbuyersmarketplace_44_UpdateDealRequestIn",
        "UpdateDealRequestOut": "_authorizedbuyersmarketplace_45_UpdateDealRequestOut",
        "PrivateDataIn": "_authorizedbuyersmarketplace_46_PrivateDataIn",
        "PrivateDataOut": "_authorizedbuyersmarketplace_47_PrivateDataOut",
        "ActivateClientUserRequestIn": "_authorizedbuyersmarketplace_48_ActivateClientUserRequestIn",
        "ActivateClientUserRequestOut": "_authorizedbuyersmarketplace_49_ActivateClientUserRequestOut",
        "UnsubscribeClientsRequestIn": "_authorizedbuyersmarketplace_50_UnsubscribeClientsRequestIn",
        "UnsubscribeClientsRequestOut": "_authorizedbuyersmarketplace_51_UnsubscribeClientsRequestOut",
        "CancelNegotiationRequestIn": "_authorizedbuyersmarketplace_52_CancelNegotiationRequestIn",
        "CancelNegotiationRequestOut": "_authorizedbuyersmarketplace_53_CancelNegotiationRequestOut",
        "DeactivateClientRequestIn": "_authorizedbuyersmarketplace_54_DeactivateClientRequestIn",
        "DeactivateClientRequestOut": "_authorizedbuyersmarketplace_55_DeactivateClientRequestOut",
        "TimeOfDayIn": "_authorizedbuyersmarketplace_56_TimeOfDayIn",
        "TimeOfDayOut": "_authorizedbuyersmarketplace_57_TimeOfDayOut",
        "DealIn": "_authorizedbuyersmarketplace_58_DealIn",
        "DealOut": "_authorizedbuyersmarketplace_59_DealOut",
        "InventorySizeTargetingIn": "_authorizedbuyersmarketplace_60_InventorySizeTargetingIn",
        "InventorySizeTargetingOut": "_authorizedbuyersmarketplace_61_InventorySizeTargetingOut",
        "PauseFinalizedDealRequestIn": "_authorizedbuyersmarketplace_62_PauseFinalizedDealRequestIn",
        "PauseFinalizedDealRequestOut": "_authorizedbuyersmarketplace_63_PauseFinalizedDealRequestOut",
        "PreferredDealTermsIn": "_authorizedbuyersmarketplace_64_PreferredDealTermsIn",
        "PreferredDealTermsOut": "_authorizedbuyersmarketplace_65_PreferredDealTermsOut",
        "ProgrammaticGuaranteedTermsIn": "_authorizedbuyersmarketplace_66_ProgrammaticGuaranteedTermsIn",
        "ProgrammaticGuaranteedTermsOut": "_authorizedbuyersmarketplace_67_ProgrammaticGuaranteedTermsOut",
        "ContactIn": "_authorizedbuyersmarketplace_68_ContactIn",
        "ContactOut": "_authorizedbuyersmarketplace_69_ContactOut",
        "ListDealsResponseIn": "_authorizedbuyersmarketplace_70_ListDealsResponseIn",
        "ListDealsResponseOut": "_authorizedbuyersmarketplace_71_ListDealsResponseOut",
        "SendRfpRequestIn": "_authorizedbuyersmarketplace_72_SendRfpRequestIn",
        "SendRfpRequestOut": "_authorizedbuyersmarketplace_73_SendRfpRequestOut",
        "PlacementTargetingIn": "_authorizedbuyersmarketplace_74_PlacementTargetingIn",
        "PlacementTargetingOut": "_authorizedbuyersmarketplace_75_PlacementTargetingOut",
        "NoteIn": "_authorizedbuyersmarketplace_76_NoteIn",
        "NoteOut": "_authorizedbuyersmarketplace_77_NoteOut",
        "ListFinalizedDealsResponseIn": "_authorizedbuyersmarketplace_78_ListFinalizedDealsResponseIn",
        "ListFinalizedDealsResponseOut": "_authorizedbuyersmarketplace_79_ListFinalizedDealsResponseOut",
        "VideoTargetingIn": "_authorizedbuyersmarketplace_80_VideoTargetingIn",
        "VideoTargetingOut": "_authorizedbuyersmarketplace_81_VideoTargetingOut",
        "ListClientsResponseIn": "_authorizedbuyersmarketplace_82_ListClientsResponseIn",
        "ListClientsResponseOut": "_authorizedbuyersmarketplace_83_ListClientsResponseOut",
        "TimeZoneIn": "_authorizedbuyersmarketplace_84_TimeZoneIn",
        "TimeZoneOut": "_authorizedbuyersmarketplace_85_TimeZoneOut",
        "InventoryTypeTargetingIn": "_authorizedbuyersmarketplace_86_InventoryTypeTargetingIn",
        "InventoryTypeTargetingOut": "_authorizedbuyersmarketplace_87_InventoryTypeTargetingOut",
        "ListProposalsResponseIn": "_authorizedbuyersmarketplace_88_ListProposalsResponseIn",
        "ListProposalsResponseOut": "_authorizedbuyersmarketplace_89_ListProposalsResponseOut",
        "MoneyIn": "_authorizedbuyersmarketplace_90_MoneyIn",
        "MoneyOut": "_authorizedbuyersmarketplace_91_MoneyOut",
        "PriceIn": "_authorizedbuyersmarketplace_92_PriceIn",
        "PriceOut": "_authorizedbuyersmarketplace_93_PriceOut",
        "DealPausingInfoIn": "_authorizedbuyersmarketplace_94_DealPausingInfoIn",
        "DealPausingInfoOut": "_authorizedbuyersmarketplace_95_DealPausingInfoOut",
        "AuctionPackageIn": "_authorizedbuyersmarketplace_96_AuctionPackageIn",
        "AuctionPackageOut": "_authorizedbuyersmarketplace_97_AuctionPackageOut",
        "OperatingSystemTargetingIn": "_authorizedbuyersmarketplace_98_OperatingSystemTargetingIn",
        "OperatingSystemTargetingOut": "_authorizedbuyersmarketplace_99_OperatingSystemTargetingOut",
        "EmptyIn": "_authorizedbuyersmarketplace_100_EmptyIn",
        "EmptyOut": "_authorizedbuyersmarketplace_101_EmptyOut",
        "UriTargetingIn": "_authorizedbuyersmarketplace_102_UriTargetingIn",
        "UriTargetingOut": "_authorizedbuyersmarketplace_103_UriTargetingOut",
        "PublisherProfileIn": "_authorizedbuyersmarketplace_104_PublisherProfileIn",
        "PublisherProfileOut": "_authorizedbuyersmarketplace_105_PublisherProfileOut",
        "ClientUserIn": "_authorizedbuyersmarketplace_106_ClientUserIn",
        "ClientUserOut": "_authorizedbuyersmarketplace_107_ClientUserOut",
        "ListAuctionPackagesResponseIn": "_authorizedbuyersmarketplace_108_ListAuctionPackagesResponseIn",
        "ListAuctionPackagesResponseOut": "_authorizedbuyersmarketplace_109_ListAuctionPackagesResponseOut",
        "ClientIn": "_authorizedbuyersmarketplace_110_ClientIn",
        "ClientOut": "_authorizedbuyersmarketplace_111_ClientOut",
        "BatchUpdateDealsResponseIn": "_authorizedbuyersmarketplace_112_BatchUpdateDealsResponseIn",
        "BatchUpdateDealsResponseOut": "_authorizedbuyersmarketplace_113_BatchUpdateDealsResponseOut",
        "AcceptProposalRequestIn": "_authorizedbuyersmarketplace_114_AcceptProposalRequestIn",
        "AcceptProposalRequestOut": "_authorizedbuyersmarketplace_115_AcceptProposalRequestOut",
        "FrequencyCapIn": "_authorizedbuyersmarketplace_116_FrequencyCapIn",
        "FrequencyCapOut": "_authorizedbuyersmarketplace_117_FrequencyCapOut",
        "AddNoteRequestIn": "_authorizedbuyersmarketplace_118_AddNoteRequestIn",
        "AddNoteRequestOut": "_authorizedbuyersmarketplace_119_AddNoteRequestOut",
        "AdSizeIn": "_authorizedbuyersmarketplace_120_AdSizeIn",
        "AdSizeOut": "_authorizedbuyersmarketplace_121_AdSizeOut",
        "DayPartTargetingIn": "_authorizedbuyersmarketplace_122_DayPartTargetingIn",
        "DayPartTargetingOut": "_authorizedbuyersmarketplace_123_DayPartTargetingOut",
        "FirstPartyMobileApplicationTargetingIn": "_authorizedbuyersmarketplace_124_FirstPartyMobileApplicationTargetingIn",
        "FirstPartyMobileApplicationTargetingOut": "_authorizedbuyersmarketplace_125_FirstPartyMobileApplicationTargetingOut",
        "DayPartIn": "_authorizedbuyersmarketplace_126_DayPartIn",
        "DayPartOut": "_authorizedbuyersmarketplace_127_DayPartOut",
        "UnsubscribeAuctionPackageRequestIn": "_authorizedbuyersmarketplace_128_UnsubscribeAuctionPackageRequestIn",
        "UnsubscribeAuctionPackageRequestOut": "_authorizedbuyersmarketplace_129_UnsubscribeAuctionPackageRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["PublisherProfileMobileApplicationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "appStore": t.string().optional(),
            "externalAppId": t.string().optional(),
        }
    ).named(renames["PublisherProfileMobileApplicationIn"])
    types["PublisherProfileMobileApplicationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "appStore": t.string().optional(),
            "externalAppId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublisherProfileMobileApplicationOut"])
    types["RtbMetricsIn"] = t.struct(
        {
            "bidRate7Days": t.number().optional(),
            "filteredBidRate7Days": t.number().optional(),
            "adImpressions7Days": t.string().optional(),
            "mustBidRateCurrentMonth": t.number().optional(),
            "bids7Days": t.string().optional(),
            "bidRequests7Days": t.string().optional(),
        }
    ).named(renames["RtbMetricsIn"])
    types["RtbMetricsOut"] = t.struct(
        {
            "bidRate7Days": t.number().optional(),
            "filteredBidRate7Days": t.number().optional(),
            "adImpressions7Days": t.string().optional(),
            "mustBidRateCurrentMonth": t.number().optional(),
            "bids7Days": t.string().optional(),
            "bidRequests7Days": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RtbMetricsOut"])
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
    types["BatchUpdateDealsRequestIn"] = t.struct(
        {"requests": t.array(t.proxy(renames["UpdateDealRequestIn"]))}
    ).named(renames["BatchUpdateDealsRequestIn"])
    types["BatchUpdateDealsRequestOut"] = t.struct(
        {
            "requests": t.array(t.proxy(renames["UpdateDealRequestOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateDealsRequestOut"])
    types["ListClientUsersResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "clientUsers": t.array(t.proxy(renames["ClientUserIn"])).optional(),
        }
    ).named(renames["ListClientUsersResponseIn"])
    types["ListClientUsersResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "clientUsers": t.array(t.proxy(renames["ClientUserOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListClientUsersResponseOut"])
    types["ActivateClientRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ActivateClientRequestIn"]
    )
    types["ActivateClientRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ActivateClientRequestOut"])
    types["DeliveryControlIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeliveryControlIn"]
    )
    types["DeliveryControlOut"] = t.struct(
        {
            "roadblockingType": t.string().optional(),
            "creativeRotationType": t.string().optional(),
            "companionDeliveryType": t.string().optional(),
            "deliveryRateType": t.string().optional(),
            "frequencyCap": t.array(t.proxy(renames["FrequencyCapOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeliveryControlOut"])
    types["MarketplaceTargetingIn"] = t.struct(
        {
            "userListTargeting": t.proxy(renames["CriteriaTargetingIn"]).optional(),
            "daypartTargeting": t.proxy(renames["DayPartTargetingIn"]).optional(),
        }
    ).named(renames["MarketplaceTargetingIn"])
    types["MarketplaceTargetingOut"] = t.struct(
        {
            "technologyTargeting": t.proxy(
                renames["TechnologyTargetingOut"]
            ).optional(),
            "placementTargeting": t.proxy(renames["PlacementTargetingOut"]).optional(),
            "geoTargeting": t.proxy(renames["CriteriaTargetingOut"]).optional(),
            "userListTargeting": t.proxy(renames["CriteriaTargetingOut"]).optional(),
            "daypartTargeting": t.proxy(renames["DayPartTargetingOut"]).optional(),
            "inventorySizeTargeting": t.proxy(
                renames["InventorySizeTargetingOut"]
            ).optional(),
            "videoTargeting": t.proxy(renames["VideoTargetingOut"]).optional(),
            "inventoryTypeTargeting": t.proxy(
                renames["InventoryTypeTargetingOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MarketplaceTargetingOut"])
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
    types["SetReadyToServeRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["SetReadyToServeRequestIn"]
    )
    types["SetReadyToServeRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SetReadyToServeRequestOut"])
    types["SubscribeClientsRequestIn"] = t.struct(
        {"clients": t.array(t.string()).optional()}
    ).named(renames["SubscribeClientsRequestIn"])
    types["SubscribeClientsRequestOut"] = t.struct(
        {
            "clients": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscribeClientsRequestOut"])
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
    types["SubscribeAuctionPackageRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["SubscribeAuctionPackageRequestIn"])
    types["SubscribeAuctionPackageRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SubscribeAuctionPackageRequestOut"])
    types["DeactivateClientUserRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DeactivateClientUserRequestIn"])
    types["DeactivateClientUserRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeactivateClientUserRequestOut"])
    types["ResumeFinalizedDealRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ResumeFinalizedDealRequestIn"])
    types["ResumeFinalizedDealRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ResumeFinalizedDealRequestOut"])
    types["ProposalIn"] = t.struct(
        {
            "buyerContacts": t.array(t.proxy(renames["ContactIn"])).optional(),
            "buyerPrivateData": t.proxy(renames["PrivateDataIn"]).optional(),
            "pausingConsented": t.boolean().optional(),
            "name": t.string().optional(),
            "notes": t.array(t.proxy(renames["NoteIn"])).optional(),
            "publisherProfile": t.string().optional(),
        }
    ).named(renames["ProposalIn"])
    types["ProposalOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "state": t.string().optional(),
            "lastUpdaterOrCommentorRole": t.string().optional(),
            "dealType": t.string().optional(),
            "sellerContacts": t.array(t.proxy(renames["ContactOut"])).optional(),
            "originatorRole": t.string().optional(),
            "buyerContacts": t.array(t.proxy(renames["ContactOut"])).optional(),
            "isRenegotiating": t.boolean().optional(),
            "buyerPrivateData": t.proxy(renames["PrivateDataOut"]).optional(),
            "pausingConsented": t.boolean().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "billedBuyer": t.string().optional(),
            "notes": t.array(t.proxy(renames["NoteOut"])).optional(),
            "publisherProfile": t.string().optional(),
            "buyer": t.string().optional(),
            "client": t.string().optional(),
            "proposalRevision": t.string().optional(),
            "termsAndConditions": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProposalOut"])
    types["AddCreativeRequestIn"] = t.struct({"creative": t.string().optional()}).named(
        renames["AddCreativeRequestIn"]
    )
    types["AddCreativeRequestOut"] = t.struct(
        {
            "creative": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddCreativeRequestOut"])
    types["PrivateAuctionTermsIn"] = t.struct(
        {"floorPrice": t.proxy(renames["PriceIn"]).optional()}
    ).named(renames["PrivateAuctionTermsIn"])
    types["PrivateAuctionTermsOut"] = t.struct(
        {
            "floorPrice": t.proxy(renames["PriceOut"]).optional(),
            "openAuctionAllowed": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrivateAuctionTermsOut"])
    types["CreativeRequirementsIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CreativeRequirementsIn"]
    )
    types["CreativeRequirementsOut"] = t.struct(
        {
            "creativeSafeFrameCompatibility": t.string().optional(),
            "skippableAdType": t.string().optional(),
            "creativePreApprovalPolicy": t.string().optional(),
            "creativeFormat": t.string().optional(),
            "programmaticCreativeSource": t.string().optional(),
            "maxAdDurationMs": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeRequirementsOut"])
    types["FinalizedDealIn"] = t.struct(
        {
            "name": t.string().optional(),
            "dealPausingInfo": t.proxy(renames["DealPausingInfoIn"]).optional(),
            "readyToServe": t.boolean().optional(),
            "dealServingStatus": t.string().optional(),
            "deal": t.proxy(renames["DealIn"]).optional(),
            "rtbMetrics": t.proxy(renames["RtbMetricsIn"]).optional(),
        }
    ).named(renames["FinalizedDealIn"])
    types["FinalizedDealOut"] = t.struct(
        {
            "name": t.string().optional(),
            "dealPausingInfo": t.proxy(renames["DealPausingInfoOut"]).optional(),
            "readyToServe": t.boolean().optional(),
            "dealServingStatus": t.string().optional(),
            "deal": t.proxy(renames["DealOut"]).optional(),
            "rtbMetrics": t.proxy(renames["RtbMetricsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FinalizedDealOut"])
    types["UpdateDealRequestIn"] = t.struct(
        {"deal": t.proxy(renames["DealIn"]), "updateMask": t.string().optional()}
    ).named(renames["UpdateDealRequestIn"])
    types["UpdateDealRequestOut"] = t.struct(
        {
            "deal": t.proxy(renames["DealOut"]),
            "updateMask": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateDealRequestOut"])
    types["PrivateDataIn"] = t.struct({"referenceId": t.string().optional()}).named(
        renames["PrivateDataIn"]
    )
    types["PrivateDataOut"] = t.struct(
        {
            "referenceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrivateDataOut"])
    types["ActivateClientUserRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ActivateClientUserRequestIn"]
    )
    types["ActivateClientUserRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ActivateClientUserRequestOut"])
    types["UnsubscribeClientsRequestIn"] = t.struct(
        {"clients": t.array(t.string()).optional()}
    ).named(renames["UnsubscribeClientsRequestIn"])
    types["UnsubscribeClientsRequestOut"] = t.struct(
        {
            "clients": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UnsubscribeClientsRequestOut"])
    types["CancelNegotiationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelNegotiationRequestIn"]
    )
    types["CancelNegotiationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelNegotiationRequestOut"])
    types["DeactivateClientRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeactivateClientRequestIn"]
    )
    types["DeactivateClientRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeactivateClientRequestOut"])
    types["TimeOfDayIn"] = t.struct(
        {
            "hours": t.integer().optional(),
            "seconds": t.integer().optional(),
            "nanos": t.integer().optional(),
            "minutes": t.integer().optional(),
        }
    ).named(renames["TimeOfDayIn"])
    types["TimeOfDayOut"] = t.struct(
        {
            "hours": t.integer().optional(),
            "seconds": t.integer().optional(),
            "nanos": t.integer().optional(),
            "minutes": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeOfDayOut"])
    types["DealIn"] = t.struct(
        {
            "estimatedGrossSpend": t.proxy(renames["MoneyIn"]).optional(),
            "flightEndTime": t.string().optional(),
            "targeting": t.proxy(renames["MarketplaceTargetingIn"]).optional(),
            "name": t.string().optional(),
            "flightStartTime": t.string().optional(),
            "preferredDealTerms": t.proxy(renames["PreferredDealTermsIn"]).optional(),
            "programmaticGuaranteedTerms": t.proxy(
                renames["ProgrammaticGuaranteedTermsIn"]
            ).optional(),
            "publisherProfile": t.string().optional(),
            "privateAuctionTerms": t.proxy(renames["PrivateAuctionTermsIn"]).optional(),
        }
    ).named(renames["DealIn"])
    types["DealOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "estimatedGrossSpend": t.proxy(renames["MoneyOut"]).optional(),
            "createTime": t.string().optional(),
            "flightEndTime": t.string().optional(),
            "dealType": t.string().optional(),
            "sellerTimeZone": t.proxy(renames["TimeZoneOut"]).optional(),
            "targeting": t.proxy(renames["MarketplaceTargetingOut"]).optional(),
            "deliveryControl": t.proxy(renames["DeliveryControlOut"]).optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "flightStartTime": t.string().optional(),
            "buyer": t.string().optional(),
            "preferredDealTerms": t.proxy(renames["PreferredDealTermsOut"]).optional(),
            "description": t.string().optional(),
            "client": t.string().optional(),
            "programmaticGuaranteedTerms": t.proxy(
                renames["ProgrammaticGuaranteedTermsOut"]
            ).optional(),
            "publisherProfile": t.string().optional(),
            "billedBuyer": t.string().optional(),
            "creativeRequirements": t.proxy(
                renames["CreativeRequirementsOut"]
            ).optional(),
            "proposalRevision": t.string().optional(),
            "privateAuctionTerms": t.proxy(
                renames["PrivateAuctionTermsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DealOut"])
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
    types["PauseFinalizedDealRequestIn"] = t.struct(
        {"reason": t.string().optional()}
    ).named(renames["PauseFinalizedDealRequestIn"])
    types["PauseFinalizedDealRequestOut"] = t.struct(
        {
            "reason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PauseFinalizedDealRequestOut"])
    types["PreferredDealTermsIn"] = t.struct(
        {"fixedPrice": t.proxy(renames["PriceIn"]).optional()}
    ).named(renames["PreferredDealTermsIn"])
    types["PreferredDealTermsOut"] = t.struct(
        {
            "fixedPrice": t.proxy(renames["PriceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PreferredDealTermsOut"])
    types["ProgrammaticGuaranteedTermsIn"] = t.struct(
        {
            "minimumDailyLooks": t.string().optional(),
            "impressionCap": t.string().optional(),
            "reservationType": t.string().optional(),
            "guaranteedLooks": t.string().optional(),
            "fixedPrice": t.proxy(renames["PriceIn"]).optional(),
            "percentShareOfVoice": t.string().optional(),
        }
    ).named(renames["ProgrammaticGuaranteedTermsIn"])
    types["ProgrammaticGuaranteedTermsOut"] = t.struct(
        {
            "minimumDailyLooks": t.string().optional(),
            "impressionCap": t.string().optional(),
            "reservationType": t.string().optional(),
            "guaranteedLooks": t.string().optional(),
            "fixedPrice": t.proxy(renames["PriceOut"]).optional(),
            "percentShareOfVoice": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProgrammaticGuaranteedTermsOut"])
    types["ContactIn"] = t.struct(
        {"displayName": t.string().optional(), "email": t.string().optional()}
    ).named(renames["ContactIn"])
    types["ContactOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContactOut"])
    types["ListDealsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "deals": t.array(t.proxy(renames["DealIn"])).optional(),
        }
    ).named(renames["ListDealsResponseIn"])
    types["ListDealsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "deals": t.array(t.proxy(renames["DealOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDealsResponseOut"])
    types["SendRfpRequestIn"] = t.struct(
        {
            "flightStartTime": t.string(),
            "geoTargeting": t.proxy(renames["CriteriaTargetingIn"]).optional(),
            "buyerContacts": t.array(t.proxy(renames["ContactIn"])).optional(),
            "preferredDealTerms": t.proxy(renames["PreferredDealTermsIn"]).optional(),
            "displayName": t.string(),
            "publisherProfile": t.string(),
            "inventorySizeTargeting": t.proxy(
                renames["InventorySizeTargetingIn"]
            ).optional(),
            "note": t.string().optional(),
            "flightEndTime": t.string(),
            "programmaticGuaranteedTerms": t.proxy(
                renames["ProgrammaticGuaranteedTermsIn"]
            ).optional(),
            "client": t.string().optional(),
            "estimatedGrossSpend": t.proxy(renames["MoneyIn"]).optional(),
        }
    ).named(renames["SendRfpRequestIn"])
    types["SendRfpRequestOut"] = t.struct(
        {
            "flightStartTime": t.string(),
            "geoTargeting": t.proxy(renames["CriteriaTargetingOut"]).optional(),
            "buyerContacts": t.array(t.proxy(renames["ContactOut"])).optional(),
            "preferredDealTerms": t.proxy(renames["PreferredDealTermsOut"]).optional(),
            "displayName": t.string(),
            "publisherProfile": t.string(),
            "inventorySizeTargeting": t.proxy(
                renames["InventorySizeTargetingOut"]
            ).optional(),
            "note": t.string().optional(),
            "flightEndTime": t.string(),
            "programmaticGuaranteedTerms": t.proxy(
                renames["ProgrammaticGuaranteedTermsOut"]
            ).optional(),
            "client": t.string().optional(),
            "estimatedGrossSpend": t.proxy(renames["MoneyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SendRfpRequestOut"])
    types["PlacementTargetingIn"] = t.struct(
        {
            "mobileApplicationTargeting": t.proxy(
                renames["MobileApplicationTargetingIn"]
            ).optional(),
            "uriTargeting": t.proxy(renames["UriTargetingIn"]).optional(),
        }
    ).named(renames["PlacementTargetingIn"])
    types["PlacementTargetingOut"] = t.struct(
        {
            "mobileApplicationTargeting": t.proxy(
                renames["MobileApplicationTargetingOut"]
            ).optional(),
            "uriTargeting": t.proxy(renames["UriTargetingOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlacementTargetingOut"])
    types["NoteIn"] = t.struct({"note": t.string().optional()}).named(renames["NoteIn"])
    types["NoteOut"] = t.struct(
        {
            "creatorRole": t.string().optional(),
            "note": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NoteOut"])
    types["ListFinalizedDealsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "finalizedDeals": t.array(t.proxy(renames["FinalizedDealIn"])).optional(),
        }
    ).named(renames["ListFinalizedDealsResponseIn"])
    types["ListFinalizedDealsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "finalizedDeals": t.array(t.proxy(renames["FinalizedDealOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListFinalizedDealsResponseOut"])
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
    types["InventoryTypeTargetingIn"] = t.struct(
        {"inventoryTypes": t.array(t.string()).optional()}
    ).named(renames["InventoryTypeTargetingIn"])
    types["InventoryTypeTargetingOut"] = t.struct(
        {
            "inventoryTypes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventoryTypeTargetingOut"])
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
    types["PriceIn"] = t.struct(
        {
            "amount": t.proxy(renames["MoneyIn"]).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["PriceIn"])
    types["PriceOut"] = t.struct(
        {
            "amount": t.proxy(renames["MoneyOut"]).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PriceOut"])
    types["DealPausingInfoIn"] = t.struct(
        {
            "pausingConsented": t.boolean().optional(),
            "pauseReason": t.string().optional(),
            "pauseRole": t.string().optional(),
        }
    ).named(renames["DealPausingInfoIn"])
    types["DealPausingInfoOut"] = t.struct(
        {
            "pausingConsented": t.boolean().optional(),
            "pauseReason": t.string().optional(),
            "pauseRole": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DealPausingInfoOut"])
    types["AuctionPackageIn"] = t.struct(
        {"displayName": t.string().optional(), "name": t.string().optional()}
    ).named(renames["AuctionPackageIn"])
    types["AuctionPackageOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "subscribedClients": t.array(t.string()).optional(),
            "creator": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "description": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuctionPackageOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["UriTargetingIn"] = t.struct(
        {
            "targetedUris": t.array(t.string()).optional(),
            "excludedUris": t.array(t.string()).optional(),
        }
    ).named(renames["UriTargetingIn"])
    types["UriTargetingOut"] = t.struct(
        {
            "targetedUris": t.array(t.string()).optional(),
            "excludedUris": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UriTargetingOut"])
    types["PublisherProfileIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "domains": t.array(t.string()).optional(),
            "mobileApps": t.array(
                t.proxy(renames["PublisherProfileMobileApplicationIn"])
            ).optional(),
            "publisherCode": t.string().optional(),
            "pitchStatement": t.string().optional(),
            "overview": t.string().optional(),
            "audienceDescription": t.string().optional(),
            "name": t.string().optional(),
            "directDealsContact": t.string().optional(),
            "topHeadlines": t.array(t.string()).optional(),
            "samplePageUrl": t.string().optional(),
            "mediaKitUrl": t.string().optional(),
            "isParent": t.boolean().optional(),
            "logoUrl": t.string().optional(),
            "programmaticDealsContact": t.string().optional(),
        }
    ).named(renames["PublisherProfileIn"])
    types["PublisherProfileOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "domains": t.array(t.string()).optional(),
            "mobileApps": t.array(
                t.proxy(renames["PublisherProfileMobileApplicationOut"])
            ).optional(),
            "publisherCode": t.string().optional(),
            "pitchStatement": t.string().optional(),
            "overview": t.string().optional(),
            "audienceDescription": t.string().optional(),
            "name": t.string().optional(),
            "directDealsContact": t.string().optional(),
            "topHeadlines": t.array(t.string()).optional(),
            "samplePageUrl": t.string().optional(),
            "mediaKitUrl": t.string().optional(),
            "isParent": t.boolean().optional(),
            "logoUrl": t.string().optional(),
            "programmaticDealsContact": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublisherProfileOut"])
    types["ClientUserIn"] = t.struct({"email": t.string()}).named(
        renames["ClientUserIn"]
    )
    types["ClientUserOut"] = t.struct(
        {
            "email": t.string(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientUserOut"])
    types["ListAuctionPackagesResponseIn"] = t.struct(
        {
            "auctionPackages": t.array(t.proxy(renames["AuctionPackageIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListAuctionPackagesResponseIn"])
    types["ListAuctionPackagesResponseOut"] = t.struct(
        {
            "auctionPackages": t.array(
                t.proxy(renames["AuctionPackageOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAuctionPackagesResponseOut"])
    types["ClientIn"] = t.struct(
        {
            "role": t.string(),
            "sellerVisible": t.boolean().optional(),
            "displayName": t.string(),
            "partnerClientId": t.string().optional(),
        }
    ).named(renames["ClientIn"])
    types["ClientOut"] = t.struct(
        {
            "role": t.string(),
            "name": t.string().optional(),
            "sellerVisible": t.boolean().optional(),
            "state": t.string().optional(),
            "displayName": t.string(),
            "partnerClientId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientOut"])
    types["BatchUpdateDealsResponseIn"] = t.struct(
        {"deals": t.array(t.proxy(renames["DealIn"])).optional()}
    ).named(renames["BatchUpdateDealsResponseIn"])
    types["BatchUpdateDealsResponseOut"] = t.struct(
        {
            "deals": t.array(t.proxy(renames["DealOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateDealsResponseOut"])
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
            "maxImpressions": t.integer().optional(),
            "timeUnitsCount": t.integer().optional(),
            "timeUnitType": t.string().optional(),
        }
    ).named(renames["FrequencyCapIn"])
    types["FrequencyCapOut"] = t.struct(
        {
            "maxImpressions": t.integer().optional(),
            "timeUnitsCount": t.integer().optional(),
            "timeUnitType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FrequencyCapOut"])
    types["AddNoteRequestIn"] = t.struct(
        {"note": t.proxy(renames["NoteIn"]).optional()}
    ).named(renames["AddNoteRequestIn"])
    types["AddNoteRequestOut"] = t.struct(
        {
            "note": t.proxy(renames["NoteOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddNoteRequestOut"])
    types["AdSizeIn"] = t.struct(
        {
            "type": t.string().optional(),
            "height": t.string().optional(),
            "width": t.string().optional(),
        }
    ).named(renames["AdSizeIn"])
    types["AdSizeOut"] = t.struct(
        {
            "type": t.string().optional(),
            "height": t.string().optional(),
            "width": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdSizeOut"])
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
    types["DayPartIn"] = t.struct(
        {
            "startTime": t.proxy(renames["TimeOfDayIn"]).optional(),
            "dayOfWeek": t.string().optional(),
            "endTime": t.proxy(renames["TimeOfDayIn"]).optional(),
        }
    ).named(renames["DayPartIn"])
    types["DayPartOut"] = t.struct(
        {
            "startTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "dayOfWeek": t.string().optional(),
            "endTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DayPartOut"])
    types["UnsubscribeAuctionPackageRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["UnsubscribeAuctionPackageRequestIn"])
    types["UnsubscribeAuctionPackageRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UnsubscribeAuctionPackageRequestOut"])

    functions = {}
    functions["buyersFinalizedDealsResume"] = authorizedbuyersmarketplace.get(
        "v1/{parent}/finalizedDeals",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFinalizedDealsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersFinalizedDealsAddCreative"] = authorizedbuyersmarketplace.get(
        "v1/{parent}/finalizedDeals",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFinalizedDealsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersFinalizedDealsSetReadyToServe"] = authorizedbuyersmarketplace.get(
        "v1/{parent}/finalizedDeals",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFinalizedDealsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersFinalizedDealsPause"] = authorizedbuyersmarketplace.get(
        "v1/{parent}/finalizedDeals",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFinalizedDealsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersFinalizedDealsGet"] = authorizedbuyersmarketplace.get(
        "v1/{parent}/finalizedDeals",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFinalizedDealsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersFinalizedDealsList"] = authorizedbuyersmarketplace.get(
        "v1/{parent}/finalizedDeals",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFinalizedDealsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersProposalsGet"] = authorizedbuyersmarketplace.post(
        "v1/{buyer}/proposals:sendRfp",
        t.struct(
            {
                "buyer": t.string(),
                "flightStartTime": t.string(),
                "geoTargeting": t.proxy(renames["CriteriaTargetingIn"]).optional(),
                "buyerContacts": t.array(t.proxy(renames["ContactIn"])).optional(),
                "preferredDealTerms": t.proxy(
                    renames["PreferredDealTermsIn"]
                ).optional(),
                "displayName": t.string(),
                "publisherProfile": t.string(),
                "inventorySizeTargeting": t.proxy(
                    renames["InventorySizeTargetingIn"]
                ).optional(),
                "note": t.string().optional(),
                "flightEndTime": t.string(),
                "programmaticGuaranteedTerms": t.proxy(
                    renames["ProgrammaticGuaranteedTermsIn"]
                ).optional(),
                "client": t.string().optional(),
                "estimatedGrossSpend": t.proxy(renames["MoneyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProposalOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersProposalsAccept"] = authorizedbuyersmarketplace.post(
        "v1/{buyer}/proposals:sendRfp",
        t.struct(
            {
                "buyer": t.string(),
                "flightStartTime": t.string(),
                "geoTargeting": t.proxy(renames["CriteriaTargetingIn"]).optional(),
                "buyerContacts": t.array(t.proxy(renames["ContactIn"])).optional(),
                "preferredDealTerms": t.proxy(
                    renames["PreferredDealTermsIn"]
                ).optional(),
                "displayName": t.string(),
                "publisherProfile": t.string(),
                "inventorySizeTargeting": t.proxy(
                    renames["InventorySizeTargetingIn"]
                ).optional(),
                "note": t.string().optional(),
                "flightEndTime": t.string(),
                "programmaticGuaranteedTerms": t.proxy(
                    renames["ProgrammaticGuaranteedTermsIn"]
                ).optional(),
                "client": t.string().optional(),
                "estimatedGrossSpend": t.proxy(renames["MoneyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProposalOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersProposalsPatch"] = authorizedbuyersmarketplace.post(
        "v1/{buyer}/proposals:sendRfp",
        t.struct(
            {
                "buyer": t.string(),
                "flightStartTime": t.string(),
                "geoTargeting": t.proxy(renames["CriteriaTargetingIn"]).optional(),
                "buyerContacts": t.array(t.proxy(renames["ContactIn"])).optional(),
                "preferredDealTerms": t.proxy(
                    renames["PreferredDealTermsIn"]
                ).optional(),
                "displayName": t.string(),
                "publisherProfile": t.string(),
                "inventorySizeTargeting": t.proxy(
                    renames["InventorySizeTargetingIn"]
                ).optional(),
                "note": t.string().optional(),
                "flightEndTime": t.string(),
                "programmaticGuaranteedTerms": t.proxy(
                    renames["ProgrammaticGuaranteedTermsIn"]
                ).optional(),
                "client": t.string().optional(),
                "estimatedGrossSpend": t.proxy(renames["MoneyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProposalOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersProposalsList"] = authorizedbuyersmarketplace.post(
        "v1/{buyer}/proposals:sendRfp",
        t.struct(
            {
                "buyer": t.string(),
                "flightStartTime": t.string(),
                "geoTargeting": t.proxy(renames["CriteriaTargetingIn"]).optional(),
                "buyerContacts": t.array(t.proxy(renames["ContactIn"])).optional(),
                "preferredDealTerms": t.proxy(
                    renames["PreferredDealTermsIn"]
                ).optional(),
                "displayName": t.string(),
                "publisherProfile": t.string(),
                "inventorySizeTargeting": t.proxy(
                    renames["InventorySizeTargetingIn"]
                ).optional(),
                "note": t.string().optional(),
                "flightEndTime": t.string(),
                "programmaticGuaranteedTerms": t.proxy(
                    renames["ProgrammaticGuaranteedTermsIn"]
                ).optional(),
                "client": t.string().optional(),
                "estimatedGrossSpend": t.proxy(renames["MoneyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProposalOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersProposalsCancelNegotiation"] = authorizedbuyersmarketplace.post(
        "v1/{buyer}/proposals:sendRfp",
        t.struct(
            {
                "buyer": t.string(),
                "flightStartTime": t.string(),
                "geoTargeting": t.proxy(renames["CriteriaTargetingIn"]).optional(),
                "buyerContacts": t.array(t.proxy(renames["ContactIn"])).optional(),
                "preferredDealTerms": t.proxy(
                    renames["PreferredDealTermsIn"]
                ).optional(),
                "displayName": t.string(),
                "publisherProfile": t.string(),
                "inventorySizeTargeting": t.proxy(
                    renames["InventorySizeTargetingIn"]
                ).optional(),
                "note": t.string().optional(),
                "flightEndTime": t.string(),
                "programmaticGuaranteedTerms": t.proxy(
                    renames["ProgrammaticGuaranteedTermsIn"]
                ).optional(),
                "client": t.string().optional(),
                "estimatedGrossSpend": t.proxy(renames["MoneyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProposalOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersProposalsAddNote"] = authorizedbuyersmarketplace.post(
        "v1/{buyer}/proposals:sendRfp",
        t.struct(
            {
                "buyer": t.string(),
                "flightStartTime": t.string(),
                "geoTargeting": t.proxy(renames["CriteriaTargetingIn"]).optional(),
                "buyerContacts": t.array(t.proxy(renames["ContactIn"])).optional(),
                "preferredDealTerms": t.proxy(
                    renames["PreferredDealTermsIn"]
                ).optional(),
                "displayName": t.string(),
                "publisherProfile": t.string(),
                "inventorySizeTargeting": t.proxy(
                    renames["InventorySizeTargetingIn"]
                ).optional(),
                "note": t.string().optional(),
                "flightEndTime": t.string(),
                "programmaticGuaranteedTerms": t.proxy(
                    renames["ProgrammaticGuaranteedTermsIn"]
                ).optional(),
                "client": t.string().optional(),
                "estimatedGrossSpend": t.proxy(renames["MoneyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProposalOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersProposalsSendRfp"] = authorizedbuyersmarketplace.post(
        "v1/{buyer}/proposals:sendRfp",
        t.struct(
            {
                "buyer": t.string(),
                "flightStartTime": t.string(),
                "geoTargeting": t.proxy(renames["CriteriaTargetingIn"]).optional(),
                "buyerContacts": t.array(t.proxy(renames["ContactIn"])).optional(),
                "preferredDealTerms": t.proxy(
                    renames["PreferredDealTermsIn"]
                ).optional(),
                "displayName": t.string(),
                "publisherProfile": t.string(),
                "inventorySizeTargeting": t.proxy(
                    renames["InventorySizeTargetingIn"]
                ).optional(),
                "note": t.string().optional(),
                "flightEndTime": t.string(),
                "programmaticGuaranteedTerms": t.proxy(
                    renames["ProgrammaticGuaranteedTermsIn"]
                ).optional(),
                "client": t.string().optional(),
                "estimatedGrossSpend": t.proxy(renames["MoneyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProposalOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersProposalsDealsGet"] = authorizedbuyersmarketplace.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "estimatedGrossSpend": t.proxy(renames["MoneyIn"]).optional(),
                "flightEndTime": t.string().optional(),
                "targeting": t.proxy(renames["MarketplaceTargetingIn"]).optional(),
                "flightStartTime": t.string().optional(),
                "preferredDealTerms": t.proxy(
                    renames["PreferredDealTermsIn"]
                ).optional(),
                "programmaticGuaranteedTerms": t.proxy(
                    renames["ProgrammaticGuaranteedTermsIn"]
                ).optional(),
                "publisherProfile": t.string().optional(),
                "privateAuctionTerms": t.proxy(
                    renames["PrivateAuctionTermsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DealOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersProposalsDealsList"] = authorizedbuyersmarketplace.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "estimatedGrossSpend": t.proxy(renames["MoneyIn"]).optional(),
                "flightEndTime": t.string().optional(),
                "targeting": t.proxy(renames["MarketplaceTargetingIn"]).optional(),
                "flightStartTime": t.string().optional(),
                "preferredDealTerms": t.proxy(
                    renames["PreferredDealTermsIn"]
                ).optional(),
                "programmaticGuaranteedTerms": t.proxy(
                    renames["ProgrammaticGuaranteedTermsIn"]
                ).optional(),
                "publisherProfile": t.string().optional(),
                "privateAuctionTerms": t.proxy(
                    renames["PrivateAuctionTermsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DealOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersProposalsDealsBatchUpdate"] = authorizedbuyersmarketplace.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "estimatedGrossSpend": t.proxy(renames["MoneyIn"]).optional(),
                "flightEndTime": t.string().optional(),
                "targeting": t.proxy(renames["MarketplaceTargetingIn"]).optional(),
                "flightStartTime": t.string().optional(),
                "preferredDealTerms": t.proxy(
                    renames["PreferredDealTermsIn"]
                ).optional(),
                "programmaticGuaranteedTerms": t.proxy(
                    renames["ProgrammaticGuaranteedTermsIn"]
                ).optional(),
                "publisherProfile": t.string().optional(),
                "privateAuctionTerms": t.proxy(
                    renames["PrivateAuctionTermsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DealOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersProposalsDealsPatch"] = authorizedbuyersmarketplace.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "estimatedGrossSpend": t.proxy(renames["MoneyIn"]).optional(),
                "flightEndTime": t.string().optional(),
                "targeting": t.proxy(renames["MarketplaceTargetingIn"]).optional(),
                "flightStartTime": t.string().optional(),
                "preferredDealTerms": t.proxy(
                    renames["PreferredDealTermsIn"]
                ).optional(),
                "programmaticGuaranteedTerms": t.proxy(
                    renames["ProgrammaticGuaranteedTermsIn"]
                ).optional(),
                "publisherProfile": t.string().optional(),
                "privateAuctionTerms": t.proxy(
                    renames["PrivateAuctionTermsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DealOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersAuctionPackagesGet"] = authorizedbuyersmarketplace.post(
        "v1/{auctionPackage}:subscribeClients",
        t.struct(
            {
                "auctionPackage": t.string(),
                "clients": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AuctionPackageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "buyersAuctionPackagesUnsubscribeClients"
    ] = authorizedbuyersmarketplace.post(
        "v1/{auctionPackage}:subscribeClients",
        t.struct(
            {
                "auctionPackage": t.string(),
                "clients": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AuctionPackageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersAuctionPackagesSubscribe"] = authorizedbuyersmarketplace.post(
        "v1/{auctionPackage}:subscribeClients",
        t.struct(
            {
                "auctionPackage": t.string(),
                "clients": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AuctionPackageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersAuctionPackagesUnsubscribe"] = authorizedbuyersmarketplace.post(
        "v1/{auctionPackage}:subscribeClients",
        t.struct(
            {
                "auctionPackage": t.string(),
                "clients": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AuctionPackageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersAuctionPackagesList"] = authorizedbuyersmarketplace.post(
        "v1/{auctionPackage}:subscribeClients",
        t.struct(
            {
                "auctionPackage": t.string(),
                "clients": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AuctionPackageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "buyersAuctionPackagesSubscribeClients"
    ] = authorizedbuyersmarketplace.post(
        "v1/{auctionPackage}:subscribeClients",
        t.struct(
            {
                "auctionPackage": t.string(),
                "clients": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AuctionPackageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersPublisherProfilesList"] = authorizedbuyersmarketplace.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["PublisherProfileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersPublisherProfilesGet"] = authorizedbuyersmarketplace.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["PublisherProfileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersClientsDeactivate"] = authorizedbuyersmarketplace.post(
        "v1/{name}:activate",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClientOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersClientsCreate"] = authorizedbuyersmarketplace.post(
        "v1/{name}:activate",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClientOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersClientsGet"] = authorizedbuyersmarketplace.post(
        "v1/{name}:activate",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClientOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersClientsList"] = authorizedbuyersmarketplace.post(
        "v1/{name}:activate",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClientOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersClientsPatch"] = authorizedbuyersmarketplace.post(
        "v1/{name}:activate",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClientOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersClientsActivate"] = authorizedbuyersmarketplace.post(
        "v1/{name}:activate",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClientOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersClientsUsersCreate"] = authorizedbuyersmarketplace.get(
        "v1/{parent}/users",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListClientUsersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersClientsUsersDeactivate"] = authorizedbuyersmarketplace.get(
        "v1/{parent}/users",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListClientUsersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersClientsUsersDelete"] = authorizedbuyersmarketplace.get(
        "v1/{parent}/users",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListClientUsersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersClientsUsersActivate"] = authorizedbuyersmarketplace.get(
        "v1/{parent}/users",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListClientUsersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersClientsUsersGet"] = authorizedbuyersmarketplace.get(
        "v1/{parent}/users",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListClientUsersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersClientsUsersList"] = authorizedbuyersmarketplace.get(
        "v1/{parent}/users",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListClientUsersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersFinalizedDealsList"] = authorizedbuyersmarketplace.get(
        "v1/{parent}/finalizedDeals",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFinalizedDealsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="authorizedbuyersmarketplace",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
