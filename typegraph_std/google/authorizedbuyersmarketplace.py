from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_authorizedbuyersmarketplace():
    authorizedbuyersmarketplace = HTTPRuntime(
        "https://authorizedbuyersmarketplace.googleapis.com/"
    )

    renames = {
        "ErrorResponse": "_authorizedbuyersmarketplace_1_ErrorResponse",
        "TechnologyTargetingIn": "_authorizedbuyersmarketplace_2_TechnologyTargetingIn",
        "TechnologyTargetingOut": "_authorizedbuyersmarketplace_3_TechnologyTargetingOut",
        "FinalizedDealIn": "_authorizedbuyersmarketplace_4_FinalizedDealIn",
        "FinalizedDealOut": "_authorizedbuyersmarketplace_5_FinalizedDealOut",
        "InventorySizeTargetingIn": "_authorizedbuyersmarketplace_6_InventorySizeTargetingIn",
        "InventorySizeTargetingOut": "_authorizedbuyersmarketplace_7_InventorySizeTargetingOut",
        "CancelNegotiationRequestIn": "_authorizedbuyersmarketplace_8_CancelNegotiationRequestIn",
        "CancelNegotiationRequestOut": "_authorizedbuyersmarketplace_9_CancelNegotiationRequestOut",
        "FirstPartyMobileApplicationTargetingIn": "_authorizedbuyersmarketplace_10_FirstPartyMobileApplicationTargetingIn",
        "FirstPartyMobileApplicationTargetingOut": "_authorizedbuyersmarketplace_11_FirstPartyMobileApplicationTargetingOut",
        "ActivateClientRequestIn": "_authorizedbuyersmarketplace_12_ActivateClientRequestIn",
        "ActivateClientRequestOut": "_authorizedbuyersmarketplace_13_ActivateClientRequestOut",
        "ListFinalizedDealsResponseIn": "_authorizedbuyersmarketplace_14_ListFinalizedDealsResponseIn",
        "ListFinalizedDealsResponseOut": "_authorizedbuyersmarketplace_15_ListFinalizedDealsResponseOut",
        "SendRfpRequestIn": "_authorizedbuyersmarketplace_16_SendRfpRequestIn",
        "SendRfpRequestOut": "_authorizedbuyersmarketplace_17_SendRfpRequestOut",
        "BatchUpdateDealsResponseIn": "_authorizedbuyersmarketplace_18_BatchUpdateDealsResponseIn",
        "BatchUpdateDealsResponseOut": "_authorizedbuyersmarketplace_19_BatchUpdateDealsResponseOut",
        "VideoTargetingIn": "_authorizedbuyersmarketplace_20_VideoTargetingIn",
        "VideoTargetingOut": "_authorizedbuyersmarketplace_21_VideoTargetingOut",
        "MoneyIn": "_authorizedbuyersmarketplace_22_MoneyIn",
        "MoneyOut": "_authorizedbuyersmarketplace_23_MoneyOut",
        "SubscribeClientsRequestIn": "_authorizedbuyersmarketplace_24_SubscribeClientsRequestIn",
        "SubscribeClientsRequestOut": "_authorizedbuyersmarketplace_25_SubscribeClientsRequestOut",
        "UpdateDealRequestIn": "_authorizedbuyersmarketplace_26_UpdateDealRequestIn",
        "UpdateDealRequestOut": "_authorizedbuyersmarketplace_27_UpdateDealRequestOut",
        "PlacementTargetingIn": "_authorizedbuyersmarketplace_28_PlacementTargetingIn",
        "PlacementTargetingOut": "_authorizedbuyersmarketplace_29_PlacementTargetingOut",
        "UnsubscribeClientsRequestIn": "_authorizedbuyersmarketplace_30_UnsubscribeClientsRequestIn",
        "UnsubscribeClientsRequestOut": "_authorizedbuyersmarketplace_31_UnsubscribeClientsRequestOut",
        "MobileApplicationTargetingIn": "_authorizedbuyersmarketplace_32_MobileApplicationTargetingIn",
        "MobileApplicationTargetingOut": "_authorizedbuyersmarketplace_33_MobileApplicationTargetingOut",
        "ListProposalsResponseIn": "_authorizedbuyersmarketplace_34_ListProposalsResponseIn",
        "ListProposalsResponseOut": "_authorizedbuyersmarketplace_35_ListProposalsResponseOut",
        "OperatingSystemTargetingIn": "_authorizedbuyersmarketplace_36_OperatingSystemTargetingIn",
        "OperatingSystemTargetingOut": "_authorizedbuyersmarketplace_37_OperatingSystemTargetingOut",
        "DealIn": "_authorizedbuyersmarketplace_38_DealIn",
        "DealOut": "_authorizedbuyersmarketplace_39_DealOut",
        "InventoryTypeTargetingIn": "_authorizedbuyersmarketplace_40_InventoryTypeTargetingIn",
        "InventoryTypeTargetingOut": "_authorizedbuyersmarketplace_41_InventoryTypeTargetingOut",
        "PrivateDataIn": "_authorizedbuyersmarketplace_42_PrivateDataIn",
        "PrivateDataOut": "_authorizedbuyersmarketplace_43_PrivateDataOut",
        "AuctionPackageIn": "_authorizedbuyersmarketplace_44_AuctionPackageIn",
        "AuctionPackageOut": "_authorizedbuyersmarketplace_45_AuctionPackageOut",
        "ListAuctionPackagesResponseIn": "_authorizedbuyersmarketplace_46_ListAuctionPackagesResponseIn",
        "ListAuctionPackagesResponseOut": "_authorizedbuyersmarketplace_47_ListAuctionPackagesResponseOut",
        "PriceIn": "_authorizedbuyersmarketplace_48_PriceIn",
        "PriceOut": "_authorizedbuyersmarketplace_49_PriceOut",
        "DeactivateClientRequestIn": "_authorizedbuyersmarketplace_50_DeactivateClientRequestIn",
        "DeactivateClientRequestOut": "_authorizedbuyersmarketplace_51_DeactivateClientRequestOut",
        "DayPartIn": "_authorizedbuyersmarketplace_52_DayPartIn",
        "DayPartOut": "_authorizedbuyersmarketplace_53_DayPartOut",
        "NoteIn": "_authorizedbuyersmarketplace_54_NoteIn",
        "NoteOut": "_authorizedbuyersmarketplace_55_NoteOut",
        "ContactIn": "_authorizedbuyersmarketplace_56_ContactIn",
        "ContactOut": "_authorizedbuyersmarketplace_57_ContactOut",
        "MarketplaceTargetingIn": "_authorizedbuyersmarketplace_58_MarketplaceTargetingIn",
        "MarketplaceTargetingOut": "_authorizedbuyersmarketplace_59_MarketplaceTargetingOut",
        "ListClientUsersResponseIn": "_authorizedbuyersmarketplace_60_ListClientUsersResponseIn",
        "ListClientUsersResponseOut": "_authorizedbuyersmarketplace_61_ListClientUsersResponseOut",
        "PreferredDealTermsIn": "_authorizedbuyersmarketplace_62_PreferredDealTermsIn",
        "PreferredDealTermsOut": "_authorizedbuyersmarketplace_63_PreferredDealTermsOut",
        "AcceptProposalRequestIn": "_authorizedbuyersmarketplace_64_AcceptProposalRequestIn",
        "AcceptProposalRequestOut": "_authorizedbuyersmarketplace_65_AcceptProposalRequestOut",
        "PrivateAuctionTermsIn": "_authorizedbuyersmarketplace_66_PrivateAuctionTermsIn",
        "PrivateAuctionTermsOut": "_authorizedbuyersmarketplace_67_PrivateAuctionTermsOut",
        "ListPublisherProfilesResponseIn": "_authorizedbuyersmarketplace_68_ListPublisherProfilesResponseIn",
        "ListPublisherProfilesResponseOut": "_authorizedbuyersmarketplace_69_ListPublisherProfilesResponseOut",
        "PublisherProfileIn": "_authorizedbuyersmarketplace_70_PublisherProfileIn",
        "PublisherProfileOut": "_authorizedbuyersmarketplace_71_PublisherProfileOut",
        "DealPausingInfoIn": "_authorizedbuyersmarketplace_72_DealPausingInfoIn",
        "DealPausingInfoOut": "_authorizedbuyersmarketplace_73_DealPausingInfoOut",
        "TimeOfDayIn": "_authorizedbuyersmarketplace_74_TimeOfDayIn",
        "TimeOfDayOut": "_authorizedbuyersmarketplace_75_TimeOfDayOut",
        "ProgrammaticGuaranteedTermsIn": "_authorizedbuyersmarketplace_76_ProgrammaticGuaranteedTermsIn",
        "ProgrammaticGuaranteedTermsOut": "_authorizedbuyersmarketplace_77_ProgrammaticGuaranteedTermsOut",
        "SubscribeAuctionPackageRequestIn": "_authorizedbuyersmarketplace_78_SubscribeAuctionPackageRequestIn",
        "SubscribeAuctionPackageRequestOut": "_authorizedbuyersmarketplace_79_SubscribeAuctionPackageRequestOut",
        "AdSizeIn": "_authorizedbuyersmarketplace_80_AdSizeIn",
        "AdSizeOut": "_authorizedbuyersmarketplace_81_AdSizeOut",
        "ClientUserIn": "_authorizedbuyersmarketplace_82_ClientUserIn",
        "ClientUserOut": "_authorizedbuyersmarketplace_83_ClientUserOut",
        "RtbMetricsIn": "_authorizedbuyersmarketplace_84_RtbMetricsIn",
        "RtbMetricsOut": "_authorizedbuyersmarketplace_85_RtbMetricsOut",
        "BatchUpdateDealsRequestIn": "_authorizedbuyersmarketplace_86_BatchUpdateDealsRequestIn",
        "BatchUpdateDealsRequestOut": "_authorizedbuyersmarketplace_87_BatchUpdateDealsRequestOut",
        "UnsubscribeAuctionPackageRequestIn": "_authorizedbuyersmarketplace_88_UnsubscribeAuctionPackageRequestIn",
        "UnsubscribeAuctionPackageRequestOut": "_authorizedbuyersmarketplace_89_UnsubscribeAuctionPackageRequestOut",
        "AddCreativeRequestIn": "_authorizedbuyersmarketplace_90_AddCreativeRequestIn",
        "AddCreativeRequestOut": "_authorizedbuyersmarketplace_91_AddCreativeRequestOut",
        "UriTargetingIn": "_authorizedbuyersmarketplace_92_UriTargetingIn",
        "UriTargetingOut": "_authorizedbuyersmarketplace_93_UriTargetingOut",
        "PauseFinalizedDealRequestIn": "_authorizedbuyersmarketplace_94_PauseFinalizedDealRequestIn",
        "PauseFinalizedDealRequestOut": "_authorizedbuyersmarketplace_95_PauseFinalizedDealRequestOut",
        "AddNoteRequestIn": "_authorizedbuyersmarketplace_96_AddNoteRequestIn",
        "AddNoteRequestOut": "_authorizedbuyersmarketplace_97_AddNoteRequestOut",
        "ClientIn": "_authorizedbuyersmarketplace_98_ClientIn",
        "ClientOut": "_authorizedbuyersmarketplace_99_ClientOut",
        "DeliveryControlIn": "_authorizedbuyersmarketplace_100_DeliveryControlIn",
        "DeliveryControlOut": "_authorizedbuyersmarketplace_101_DeliveryControlOut",
        "TimeZoneIn": "_authorizedbuyersmarketplace_102_TimeZoneIn",
        "TimeZoneOut": "_authorizedbuyersmarketplace_103_TimeZoneOut",
        "ListClientsResponseIn": "_authorizedbuyersmarketplace_104_ListClientsResponseIn",
        "ListClientsResponseOut": "_authorizedbuyersmarketplace_105_ListClientsResponseOut",
        "ActivateClientUserRequestIn": "_authorizedbuyersmarketplace_106_ActivateClientUserRequestIn",
        "ActivateClientUserRequestOut": "_authorizedbuyersmarketplace_107_ActivateClientUserRequestOut",
        "FrequencyCapIn": "_authorizedbuyersmarketplace_108_FrequencyCapIn",
        "FrequencyCapOut": "_authorizedbuyersmarketplace_109_FrequencyCapOut",
        "DayPartTargetingIn": "_authorizedbuyersmarketplace_110_DayPartTargetingIn",
        "DayPartTargetingOut": "_authorizedbuyersmarketplace_111_DayPartTargetingOut",
        "ResumeFinalizedDealRequestIn": "_authorizedbuyersmarketplace_112_ResumeFinalizedDealRequestIn",
        "ResumeFinalizedDealRequestOut": "_authorizedbuyersmarketplace_113_ResumeFinalizedDealRequestOut",
        "PublisherProfileMobileApplicationIn": "_authorizedbuyersmarketplace_114_PublisherProfileMobileApplicationIn",
        "PublisherProfileMobileApplicationOut": "_authorizedbuyersmarketplace_115_PublisherProfileMobileApplicationOut",
        "CreativeRequirementsIn": "_authorizedbuyersmarketplace_116_CreativeRequirementsIn",
        "CreativeRequirementsOut": "_authorizedbuyersmarketplace_117_CreativeRequirementsOut",
        "DeactivateClientUserRequestIn": "_authorizedbuyersmarketplace_118_DeactivateClientUserRequestIn",
        "DeactivateClientUserRequestOut": "_authorizedbuyersmarketplace_119_DeactivateClientUserRequestOut",
        "EmptyIn": "_authorizedbuyersmarketplace_120_EmptyIn",
        "EmptyOut": "_authorizedbuyersmarketplace_121_EmptyOut",
        "ListDealsResponseIn": "_authorizedbuyersmarketplace_122_ListDealsResponseIn",
        "ListDealsResponseOut": "_authorizedbuyersmarketplace_123_ListDealsResponseOut",
        "SetReadyToServeRequestIn": "_authorizedbuyersmarketplace_124_SetReadyToServeRequestIn",
        "SetReadyToServeRequestOut": "_authorizedbuyersmarketplace_125_SetReadyToServeRequestOut",
        "ProposalIn": "_authorizedbuyersmarketplace_126_ProposalIn",
        "ProposalOut": "_authorizedbuyersmarketplace_127_ProposalOut",
        "CriteriaTargetingIn": "_authorizedbuyersmarketplace_128_CriteriaTargetingIn",
        "CriteriaTargetingOut": "_authorizedbuyersmarketplace_129_CriteriaTargetingOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["FinalizedDealIn"] = t.struct(
        {
            "deal": t.proxy(renames["DealIn"]).optional(),
            "name": t.string().optional(),
            "dealServingStatus": t.string().optional(),
            "dealPausingInfo": t.proxy(renames["DealPausingInfoIn"]).optional(),
            "readyToServe": t.boolean().optional(),
            "rtbMetrics": t.proxy(renames["RtbMetricsIn"]).optional(),
        }
    ).named(renames["FinalizedDealIn"])
    types["FinalizedDealOut"] = t.struct(
        {
            "deal": t.proxy(renames["DealOut"]).optional(),
            "name": t.string().optional(),
            "dealServingStatus": t.string().optional(),
            "dealPausingInfo": t.proxy(renames["DealPausingInfoOut"]).optional(),
            "readyToServe": t.boolean().optional(),
            "rtbMetrics": t.proxy(renames["RtbMetricsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FinalizedDealOut"])
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
    types["CancelNegotiationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelNegotiationRequestIn"]
    )
    types["CancelNegotiationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelNegotiationRequestOut"])
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
    types["ActivateClientRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ActivateClientRequestIn"]
    )
    types["ActivateClientRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ActivateClientRequestOut"])
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
    types["SendRfpRequestIn"] = t.struct(
        {
            "programmaticGuaranteedTerms": t.proxy(
                renames["ProgrammaticGuaranteedTermsIn"]
            ).optional(),
            "flightStartTime": t.string(),
            "estimatedGrossSpend": t.proxy(renames["MoneyIn"]).optional(),
            "client": t.string().optional(),
            "publisherProfile": t.string(),
            "geoTargeting": t.proxy(renames["CriteriaTargetingIn"]).optional(),
            "buyerContacts": t.array(t.proxy(renames["ContactIn"])).optional(),
            "note": t.string().optional(),
            "flightEndTime": t.string(),
            "preferredDealTerms": t.proxy(renames["PreferredDealTermsIn"]).optional(),
            "inventorySizeTargeting": t.proxy(
                renames["InventorySizeTargetingIn"]
            ).optional(),
            "displayName": t.string(),
        }
    ).named(renames["SendRfpRequestIn"])
    types["SendRfpRequestOut"] = t.struct(
        {
            "programmaticGuaranteedTerms": t.proxy(
                renames["ProgrammaticGuaranteedTermsOut"]
            ).optional(),
            "flightStartTime": t.string(),
            "estimatedGrossSpend": t.proxy(renames["MoneyOut"]).optional(),
            "client": t.string().optional(),
            "publisherProfile": t.string(),
            "geoTargeting": t.proxy(renames["CriteriaTargetingOut"]).optional(),
            "buyerContacts": t.array(t.proxy(renames["ContactOut"])).optional(),
            "note": t.string().optional(),
            "flightEndTime": t.string(),
            "preferredDealTerms": t.proxy(renames["PreferredDealTermsOut"]).optional(),
            "inventorySizeTargeting": t.proxy(
                renames["InventorySizeTargetingOut"]
            ).optional(),
            "displayName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SendRfpRequestOut"])
    types["BatchUpdateDealsResponseIn"] = t.struct(
        {"deals": t.array(t.proxy(renames["DealIn"])).optional()}
    ).named(renames["BatchUpdateDealsResponseIn"])
    types["BatchUpdateDealsResponseOut"] = t.struct(
        {
            "deals": t.array(t.proxy(renames["DealOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateDealsResponseOut"])
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
    types["MoneyIn"] = t.struct(
        {
            "units": t.string().optional(),
            "nanos": t.integer().optional(),
            "currencyCode": t.string().optional(),
        }
    ).named(renames["MoneyIn"])
    types["MoneyOut"] = t.struct(
        {
            "units": t.string().optional(),
            "nanos": t.integer().optional(),
            "currencyCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoneyOut"])
    types["SubscribeClientsRequestIn"] = t.struct(
        {"clients": t.array(t.string()).optional()}
    ).named(renames["SubscribeClientsRequestIn"])
    types["SubscribeClientsRequestOut"] = t.struct(
        {
            "clients": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscribeClientsRequestOut"])
    types["UpdateDealRequestIn"] = t.struct(
        {"updateMask": t.string().optional(), "deal": t.proxy(renames["DealIn"])}
    ).named(renames["UpdateDealRequestIn"])
    types["UpdateDealRequestOut"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "deal": t.proxy(renames["DealOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateDealRequestOut"])
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
    types["UnsubscribeClientsRequestIn"] = t.struct(
        {"clients": t.array(t.string()).optional()}
    ).named(renames["UnsubscribeClientsRequestIn"])
    types["UnsubscribeClientsRequestOut"] = t.struct(
        {
            "clients": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UnsubscribeClientsRequestOut"])
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
    types["DealIn"] = t.struct(
        {
            "privateAuctionTerms": t.proxy(renames["PrivateAuctionTermsIn"]).optional(),
            "publisherProfile": t.string().optional(),
            "programmaticGuaranteedTerms": t.proxy(
                renames["ProgrammaticGuaranteedTermsIn"]
            ).optional(),
            "preferredDealTerms": t.proxy(renames["PreferredDealTermsIn"]).optional(),
            "targeting": t.proxy(renames["MarketplaceTargetingIn"]).optional(),
            "flightEndTime": t.string().optional(),
            "estimatedGrossSpend": t.proxy(renames["MoneyIn"]).optional(),
            "flightStartTime": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["DealIn"])
    types["DealOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "description": t.string().optional(),
            "creativeRequirements": t.proxy(
                renames["CreativeRequirementsOut"]
            ).optional(),
            "billedBuyer": t.string().optional(),
            "sellerTimeZone": t.proxy(renames["TimeZoneOut"]).optional(),
            "privateAuctionTerms": t.proxy(
                renames["PrivateAuctionTermsOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "client": t.string().optional(),
            "displayName": t.string().optional(),
            "publisherProfile": t.string().optional(),
            "proposalRevision": t.string().optional(),
            "programmaticGuaranteedTerms": t.proxy(
                renames["ProgrammaticGuaranteedTermsOut"]
            ).optional(),
            "preferredDealTerms": t.proxy(renames["PreferredDealTermsOut"]).optional(),
            "buyer": t.string().optional(),
            "dealType": t.string().optional(),
            "targeting": t.proxy(renames["MarketplaceTargetingOut"]).optional(),
            "deliveryControl": t.proxy(renames["DeliveryControlOut"]).optional(),
            "flightEndTime": t.string().optional(),
            "estimatedGrossSpend": t.proxy(renames["MoneyOut"]).optional(),
            "flightStartTime": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DealOut"])
    types["InventoryTypeTargetingIn"] = t.struct(
        {"inventoryTypes": t.array(t.string()).optional()}
    ).named(renames["InventoryTypeTargetingIn"])
    types["InventoryTypeTargetingOut"] = t.struct(
        {
            "inventoryTypes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventoryTypeTargetingOut"])
    types["PrivateDataIn"] = t.struct({"referenceId": t.string().optional()}).named(
        renames["PrivateDataIn"]
    )
    types["PrivateDataOut"] = t.struct(
        {
            "referenceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrivateDataOut"])
    types["AuctionPackageIn"] = t.struct(
        {"displayName": t.string().optional(), "name": t.string().optional()}
    ).named(renames["AuctionPackageIn"])
    types["AuctionPackageOut"] = t.struct(
        {
            "subscribedClients": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "creator": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuctionPackageOut"])
    types["ListAuctionPackagesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "auctionPackages": t.array(t.proxy(renames["AuctionPackageIn"])).optional(),
        }
    ).named(renames["ListAuctionPackagesResponseIn"])
    types["ListAuctionPackagesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "auctionPackages": t.array(
                t.proxy(renames["AuctionPackageOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAuctionPackagesResponseOut"])
    types["PriceIn"] = t.struct(
        {
            "type": t.string().optional(),
            "amount": t.proxy(renames["MoneyIn"]).optional(),
        }
    ).named(renames["PriceIn"])
    types["PriceOut"] = t.struct(
        {
            "type": t.string().optional(),
            "amount": t.proxy(renames["MoneyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PriceOut"])
    types["DeactivateClientRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeactivateClientRequestIn"]
    )
    types["DeactivateClientRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeactivateClientRequestOut"])
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
    types["NoteIn"] = t.struct({"note": t.string().optional()}).named(renames["NoteIn"])
    types["NoteOut"] = t.struct(
        {
            "note": t.string().optional(),
            "createTime": t.string().optional(),
            "creatorRole": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NoteOut"])
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
    types["MarketplaceTargetingIn"] = t.struct(
        {
            "userListTargeting": t.proxy(renames["CriteriaTargetingIn"]).optional(),
            "daypartTargeting": t.proxy(renames["DayPartTargetingIn"]).optional(),
        }
    ).named(renames["MarketplaceTargetingIn"])
    types["MarketplaceTargetingOut"] = t.struct(
        {
            "userListTargeting": t.proxy(renames["CriteriaTargetingOut"]).optional(),
            "daypartTargeting": t.proxy(renames["DayPartTargetingOut"]).optional(),
            "inventoryTypeTargeting": t.proxy(
                renames["InventoryTypeTargetingOut"]
            ).optional(),
            "geoTargeting": t.proxy(renames["CriteriaTargetingOut"]).optional(),
            "videoTargeting": t.proxy(renames["VideoTargetingOut"]).optional(),
            "technologyTargeting": t.proxy(
                renames["TechnologyTargetingOut"]
            ).optional(),
            "placementTargeting": t.proxy(renames["PlacementTargetingOut"]).optional(),
            "inventorySizeTargeting": t.proxy(
                renames["InventorySizeTargetingOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MarketplaceTargetingOut"])
    types["ListClientUsersResponseIn"] = t.struct(
        {
            "clientUsers": t.array(t.proxy(renames["ClientUserIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListClientUsersResponseIn"])
    types["ListClientUsersResponseOut"] = t.struct(
        {
            "clientUsers": t.array(t.proxy(renames["ClientUserOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListClientUsersResponseOut"])
    types["PreferredDealTermsIn"] = t.struct(
        {"fixedPrice": t.proxy(renames["PriceIn"]).optional()}
    ).named(renames["PreferredDealTermsIn"])
    types["PreferredDealTermsOut"] = t.struct(
        {
            "fixedPrice": t.proxy(renames["PriceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PreferredDealTermsOut"])
    types["AcceptProposalRequestIn"] = t.struct(
        {"proposalRevision": t.string().optional()}
    ).named(renames["AcceptProposalRequestIn"])
    types["AcceptProposalRequestOut"] = t.struct(
        {
            "proposalRevision": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AcceptProposalRequestOut"])
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
    types["PublisherProfileIn"] = t.struct(
        {
            "samplePageUrl": t.string().optional(),
            "publisherCode": t.string().optional(),
            "pitchStatement": t.string().optional(),
            "programmaticDealsContact": t.string().optional(),
            "directDealsContact": t.string().optional(),
            "logoUrl": t.string().optional(),
            "domains": t.array(t.string()).optional(),
            "topHeadlines": t.array(t.string()).optional(),
            "mediaKitUrl": t.string().optional(),
            "isParent": t.boolean().optional(),
            "mobileApps": t.array(
                t.proxy(renames["PublisherProfileMobileApplicationIn"])
            ).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "overview": t.string().optional(),
            "audienceDescription": t.string().optional(),
        }
    ).named(renames["PublisherProfileIn"])
    types["PublisherProfileOut"] = t.struct(
        {
            "samplePageUrl": t.string().optional(),
            "publisherCode": t.string().optional(),
            "pitchStatement": t.string().optional(),
            "programmaticDealsContact": t.string().optional(),
            "directDealsContact": t.string().optional(),
            "logoUrl": t.string().optional(),
            "domains": t.array(t.string()).optional(),
            "topHeadlines": t.array(t.string()).optional(),
            "mediaKitUrl": t.string().optional(),
            "isParent": t.boolean().optional(),
            "mobileApps": t.array(
                t.proxy(renames["PublisherProfileMobileApplicationOut"])
            ).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "overview": t.string().optional(),
            "audienceDescription": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublisherProfileOut"])
    types["DealPausingInfoIn"] = t.struct(
        {
            "pausingConsented": t.boolean().optional(),
            "pauseRole": t.string().optional(),
            "pauseReason": t.string().optional(),
        }
    ).named(renames["DealPausingInfoIn"])
    types["DealPausingInfoOut"] = t.struct(
        {
            "pausingConsented": t.boolean().optional(),
            "pauseRole": t.string().optional(),
            "pauseReason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DealPausingInfoOut"])
    types["TimeOfDayIn"] = t.struct(
        {
            "hours": t.integer().optional(),
            "nanos": t.integer().optional(),
            "minutes": t.integer().optional(),
            "seconds": t.integer().optional(),
        }
    ).named(renames["TimeOfDayIn"])
    types["TimeOfDayOut"] = t.struct(
        {
            "hours": t.integer().optional(),
            "nanos": t.integer().optional(),
            "minutes": t.integer().optional(),
            "seconds": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeOfDayOut"])
    types["ProgrammaticGuaranteedTermsIn"] = t.struct(
        {
            "impressionCap": t.string().optional(),
            "guaranteedLooks": t.string().optional(),
            "percentShareOfVoice": t.string().optional(),
            "reservationType": t.string().optional(),
            "fixedPrice": t.proxy(renames["PriceIn"]).optional(),
            "minimumDailyLooks": t.string().optional(),
        }
    ).named(renames["ProgrammaticGuaranteedTermsIn"])
    types["ProgrammaticGuaranteedTermsOut"] = t.struct(
        {
            "impressionCap": t.string().optional(),
            "guaranteedLooks": t.string().optional(),
            "percentShareOfVoice": t.string().optional(),
            "reservationType": t.string().optional(),
            "fixedPrice": t.proxy(renames["PriceOut"]).optional(),
            "minimumDailyLooks": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProgrammaticGuaranteedTermsOut"])
    types["SubscribeAuctionPackageRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["SubscribeAuctionPackageRequestIn"])
    types["SubscribeAuctionPackageRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SubscribeAuctionPackageRequestOut"])
    types["AdSizeIn"] = t.struct(
        {
            "height": t.string().optional(),
            "width": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["AdSizeIn"])
    types["AdSizeOut"] = t.struct(
        {
            "height": t.string().optional(),
            "width": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdSizeOut"])
    types["ClientUserIn"] = t.struct({"email": t.string()}).named(
        renames["ClientUserIn"]
    )
    types["ClientUserOut"] = t.struct(
        {
            "state": t.string().optional(),
            "name": t.string().optional(),
            "email": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientUserOut"])
    types["RtbMetricsIn"] = t.struct(
        {
            "mustBidRateCurrentMonth": t.number().optional(),
            "bidRate7Days": t.number().optional(),
            "bidRequests7Days": t.string().optional(),
            "filteredBidRate7Days": t.number().optional(),
            "adImpressions7Days": t.string().optional(),
            "bids7Days": t.string().optional(),
        }
    ).named(renames["RtbMetricsIn"])
    types["RtbMetricsOut"] = t.struct(
        {
            "mustBidRateCurrentMonth": t.number().optional(),
            "bidRate7Days": t.number().optional(),
            "bidRequests7Days": t.string().optional(),
            "filteredBidRate7Days": t.number().optional(),
            "adImpressions7Days": t.string().optional(),
            "bids7Days": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RtbMetricsOut"])
    types["BatchUpdateDealsRequestIn"] = t.struct(
        {"requests": t.array(t.proxy(renames["UpdateDealRequestIn"]))}
    ).named(renames["BatchUpdateDealsRequestIn"])
    types["BatchUpdateDealsRequestOut"] = t.struct(
        {
            "requests": t.array(t.proxy(renames["UpdateDealRequestOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateDealsRequestOut"])
    types["UnsubscribeAuctionPackageRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["UnsubscribeAuctionPackageRequestIn"])
    types["UnsubscribeAuctionPackageRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UnsubscribeAuctionPackageRequestOut"])
    types["AddCreativeRequestIn"] = t.struct({"creative": t.string().optional()}).named(
        renames["AddCreativeRequestIn"]
    )
    types["AddCreativeRequestOut"] = t.struct(
        {
            "creative": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddCreativeRequestOut"])
    types["UriTargetingIn"] = t.struct(
        {
            "excludedUris": t.array(t.string()).optional(),
            "targetedUris": t.array(t.string()).optional(),
        }
    ).named(renames["UriTargetingIn"])
    types["UriTargetingOut"] = t.struct(
        {
            "excludedUris": t.array(t.string()).optional(),
            "targetedUris": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UriTargetingOut"])
    types["PauseFinalizedDealRequestIn"] = t.struct(
        {"reason": t.string().optional()}
    ).named(renames["PauseFinalizedDealRequestIn"])
    types["PauseFinalizedDealRequestOut"] = t.struct(
        {
            "reason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PauseFinalizedDealRequestOut"])
    types["AddNoteRequestIn"] = t.struct(
        {"note": t.proxy(renames["NoteIn"]).optional()}
    ).named(renames["AddNoteRequestIn"])
    types["AddNoteRequestOut"] = t.struct(
        {
            "note": t.proxy(renames["NoteOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddNoteRequestOut"])
    types["ClientIn"] = t.struct(
        {
            "sellerVisible": t.boolean().optional(),
            "role": t.string(),
            "partnerClientId": t.string().optional(),
            "displayName": t.string(),
        }
    ).named(renames["ClientIn"])
    types["ClientOut"] = t.struct(
        {
            "sellerVisible": t.boolean().optional(),
            "role": t.string(),
            "partnerClientId": t.string().optional(),
            "state": t.string().optional(),
            "displayName": t.string(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientOut"])
    types["DeliveryControlIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeliveryControlIn"]
    )
    types["DeliveryControlOut"] = t.struct(
        {
            "deliveryRateType": t.string().optional(),
            "frequencyCap": t.array(t.proxy(renames["FrequencyCapOut"])).optional(),
            "roadblockingType": t.string().optional(),
            "companionDeliveryType": t.string().optional(),
            "creativeRotationType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeliveryControlOut"])
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
    types["ListClientsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "clients": t.array(t.proxy(renames["ClientIn"])).optional(),
        }
    ).named(renames["ListClientsResponseIn"])
    types["ListClientsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "clients": t.array(t.proxy(renames["ClientOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListClientsResponseOut"])
    types["ActivateClientUserRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ActivateClientUserRequestIn"]
    )
    types["ActivateClientUserRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ActivateClientUserRequestOut"])
    types["FrequencyCapIn"] = t.struct(
        {
            "timeUnitType": t.string().optional(),
            "timeUnitsCount": t.integer().optional(),
            "maxImpressions": t.integer().optional(),
        }
    ).named(renames["FrequencyCapIn"])
    types["FrequencyCapOut"] = t.struct(
        {
            "timeUnitType": t.string().optional(),
            "timeUnitsCount": t.integer().optional(),
            "maxImpressions": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FrequencyCapOut"])
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
    types["ResumeFinalizedDealRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ResumeFinalizedDealRequestIn"])
    types["ResumeFinalizedDealRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ResumeFinalizedDealRequestOut"])
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
    types["CreativeRequirementsIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CreativeRequirementsIn"]
    )
    types["CreativeRequirementsOut"] = t.struct(
        {
            "programmaticCreativeSource": t.string().optional(),
            "creativePreApprovalPolicy": t.string().optional(),
            "creativeFormat": t.string().optional(),
            "skippableAdType": t.string().optional(),
            "maxAdDurationMs": t.string().optional(),
            "creativeSafeFrameCompatibility": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeRequirementsOut"])
    types["DeactivateClientUserRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DeactivateClientUserRequestIn"])
    types["DeactivateClientUserRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeactivateClientUserRequestOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["SetReadyToServeRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["SetReadyToServeRequestIn"]
    )
    types["SetReadyToServeRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SetReadyToServeRequestOut"])
    types["ProposalIn"] = t.struct(
        {
            "buyerPrivateData": t.proxy(renames["PrivateDataIn"]).optional(),
            "publisherProfile": t.string().optional(),
            "notes": t.array(t.proxy(renames["NoteIn"])).optional(),
            "name": t.string().optional(),
            "pausingConsented": t.boolean().optional(),
            "buyerContacts": t.array(t.proxy(renames["ContactIn"])).optional(),
        }
    ).named(renames["ProposalIn"])
    types["ProposalOut"] = t.struct(
        {
            "state": t.string().optional(),
            "billedBuyer": t.string().optional(),
            "buyerPrivateData": t.proxy(renames["PrivateDataOut"]).optional(),
            "updateTime": t.string().optional(),
            "publisherProfile": t.string().optional(),
            "sellerContacts": t.array(t.proxy(renames["ContactOut"])).optional(),
            "lastUpdaterOrCommentorRole": t.string().optional(),
            "notes": t.array(t.proxy(renames["NoteOut"])).optional(),
            "buyer": t.string().optional(),
            "originatorRole": t.string().optional(),
            "isRenegotiating": t.boolean().optional(),
            "name": t.string().optional(),
            "client": t.string().optional(),
            "pausingConsented": t.boolean().optional(),
            "termsAndConditions": t.string().optional(),
            "proposalRevision": t.string().optional(),
            "buyerContacts": t.array(t.proxy(renames["ContactOut"])).optional(),
            "dealType": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProposalOut"])
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

    functions = {}
    functions["biddersFinalizedDealsList"] = authorizedbuyersmarketplace.get(
        "v1/{parent}/finalizedDeals",
        t.struct(
            {
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
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
                "programmaticGuaranteedTerms": t.proxy(
                    renames["ProgrammaticGuaranteedTermsIn"]
                ).optional(),
                "flightStartTime": t.string(),
                "estimatedGrossSpend": t.proxy(renames["MoneyIn"]).optional(),
                "client": t.string().optional(),
                "publisherProfile": t.string(),
                "geoTargeting": t.proxy(renames["CriteriaTargetingIn"]).optional(),
                "buyerContacts": t.array(t.proxy(renames["ContactIn"])).optional(),
                "note": t.string().optional(),
                "flightEndTime": t.string(),
                "preferredDealTerms": t.proxy(
                    renames["PreferredDealTermsIn"]
                ).optional(),
                "inventorySizeTargeting": t.proxy(
                    renames["InventorySizeTargetingIn"]
                ).optional(),
                "displayName": t.string(),
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
                "programmaticGuaranteedTerms": t.proxy(
                    renames["ProgrammaticGuaranteedTermsIn"]
                ).optional(),
                "flightStartTime": t.string(),
                "estimatedGrossSpend": t.proxy(renames["MoneyIn"]).optional(),
                "client": t.string().optional(),
                "publisherProfile": t.string(),
                "geoTargeting": t.proxy(renames["CriteriaTargetingIn"]).optional(),
                "buyerContacts": t.array(t.proxy(renames["ContactIn"])).optional(),
                "note": t.string().optional(),
                "flightEndTime": t.string(),
                "preferredDealTerms": t.proxy(
                    renames["PreferredDealTermsIn"]
                ).optional(),
                "inventorySizeTargeting": t.proxy(
                    renames["InventorySizeTargetingIn"]
                ).optional(),
                "displayName": t.string(),
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
                "programmaticGuaranteedTerms": t.proxy(
                    renames["ProgrammaticGuaranteedTermsIn"]
                ).optional(),
                "flightStartTime": t.string(),
                "estimatedGrossSpend": t.proxy(renames["MoneyIn"]).optional(),
                "client": t.string().optional(),
                "publisherProfile": t.string(),
                "geoTargeting": t.proxy(renames["CriteriaTargetingIn"]).optional(),
                "buyerContacts": t.array(t.proxy(renames["ContactIn"])).optional(),
                "note": t.string().optional(),
                "flightEndTime": t.string(),
                "preferredDealTerms": t.proxy(
                    renames["PreferredDealTermsIn"]
                ).optional(),
                "inventorySizeTargeting": t.proxy(
                    renames["InventorySizeTargetingIn"]
                ).optional(),
                "displayName": t.string(),
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
                "programmaticGuaranteedTerms": t.proxy(
                    renames["ProgrammaticGuaranteedTermsIn"]
                ).optional(),
                "flightStartTime": t.string(),
                "estimatedGrossSpend": t.proxy(renames["MoneyIn"]).optional(),
                "client": t.string().optional(),
                "publisherProfile": t.string(),
                "geoTargeting": t.proxy(renames["CriteriaTargetingIn"]).optional(),
                "buyerContacts": t.array(t.proxy(renames["ContactIn"])).optional(),
                "note": t.string().optional(),
                "flightEndTime": t.string(),
                "preferredDealTerms": t.proxy(
                    renames["PreferredDealTermsIn"]
                ).optional(),
                "inventorySizeTargeting": t.proxy(
                    renames["InventorySizeTargetingIn"]
                ).optional(),
                "displayName": t.string(),
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
                "programmaticGuaranteedTerms": t.proxy(
                    renames["ProgrammaticGuaranteedTermsIn"]
                ).optional(),
                "flightStartTime": t.string(),
                "estimatedGrossSpend": t.proxy(renames["MoneyIn"]).optional(),
                "client": t.string().optional(),
                "publisherProfile": t.string(),
                "geoTargeting": t.proxy(renames["CriteriaTargetingIn"]).optional(),
                "buyerContacts": t.array(t.proxy(renames["ContactIn"])).optional(),
                "note": t.string().optional(),
                "flightEndTime": t.string(),
                "preferredDealTerms": t.proxy(
                    renames["PreferredDealTermsIn"]
                ).optional(),
                "inventorySizeTargeting": t.proxy(
                    renames["InventorySizeTargetingIn"]
                ).optional(),
                "displayName": t.string(),
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
                "programmaticGuaranteedTerms": t.proxy(
                    renames["ProgrammaticGuaranteedTermsIn"]
                ).optional(),
                "flightStartTime": t.string(),
                "estimatedGrossSpend": t.proxy(renames["MoneyIn"]).optional(),
                "client": t.string().optional(),
                "publisherProfile": t.string(),
                "geoTargeting": t.proxy(renames["CriteriaTargetingIn"]).optional(),
                "buyerContacts": t.array(t.proxy(renames["ContactIn"])).optional(),
                "note": t.string().optional(),
                "flightEndTime": t.string(),
                "preferredDealTerms": t.proxy(
                    renames["PreferredDealTermsIn"]
                ).optional(),
                "inventorySizeTargeting": t.proxy(
                    renames["InventorySizeTargetingIn"]
                ).optional(),
                "displayName": t.string(),
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
                "programmaticGuaranteedTerms": t.proxy(
                    renames["ProgrammaticGuaranteedTermsIn"]
                ).optional(),
                "flightStartTime": t.string(),
                "estimatedGrossSpend": t.proxy(renames["MoneyIn"]).optional(),
                "client": t.string().optional(),
                "publisherProfile": t.string(),
                "geoTargeting": t.proxy(renames["CriteriaTargetingIn"]).optional(),
                "buyerContacts": t.array(t.proxy(renames["ContactIn"])).optional(),
                "note": t.string().optional(),
                "flightEndTime": t.string(),
                "preferredDealTerms": t.proxy(
                    renames["PreferredDealTermsIn"]
                ).optional(),
                "inventorySizeTargeting": t.proxy(
                    renames["InventorySizeTargetingIn"]
                ).optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProposalOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersProposalsDealsPatch"] = authorizedbuyersmarketplace.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["DealOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersProposalsDealsList"] = authorizedbuyersmarketplace.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["DealOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersProposalsDealsBatchUpdate"] = authorizedbuyersmarketplace.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["DealOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersProposalsDealsGet"] = authorizedbuyersmarketplace.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["DealOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersFinalizedDealsList"] = authorizedbuyersmarketplace.post(
        "v1/{name}:pause",
        t.struct(
            {
                "name": t.string(),
                "reason": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FinalizedDealOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersFinalizedDealsAddCreative"] = authorizedbuyersmarketplace.post(
        "v1/{name}:pause",
        t.struct(
            {
                "name": t.string(),
                "reason": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FinalizedDealOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersFinalizedDealsResume"] = authorizedbuyersmarketplace.post(
        "v1/{name}:pause",
        t.struct(
            {
                "name": t.string(),
                "reason": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FinalizedDealOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersFinalizedDealsGet"] = authorizedbuyersmarketplace.post(
        "v1/{name}:pause",
        t.struct(
            {
                "name": t.string(),
                "reason": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FinalizedDealOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersFinalizedDealsSetReadyToServe"] = authorizedbuyersmarketplace.post(
        "v1/{name}:pause",
        t.struct(
            {
                "name": t.string(),
                "reason": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FinalizedDealOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersFinalizedDealsPause"] = authorizedbuyersmarketplace.post(
        "v1/{name}:pause",
        t.struct(
            {
                "name": t.string(),
                "reason": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FinalizedDealOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "buyersAuctionPackagesSubscribeClients"
    ] = authorizedbuyersmarketplace.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["AuctionPackageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "buyersAuctionPackagesUnsubscribeClients"
    ] = authorizedbuyersmarketplace.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["AuctionPackageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersAuctionPackagesSubscribe"] = authorizedbuyersmarketplace.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["AuctionPackageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersAuctionPackagesUnsubscribe"] = authorizedbuyersmarketplace.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["AuctionPackageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersAuctionPackagesList"] = authorizedbuyersmarketplace.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["AuctionPackageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersAuctionPackagesGet"] = authorizedbuyersmarketplace.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
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
    functions["buyersClientsUsersDelete"] = authorizedbuyersmarketplace.post(
        "v1/{name}:deactivate",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClientUserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersClientsUsersCreate"] = authorizedbuyersmarketplace.post(
        "v1/{name}:deactivate",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClientUserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersClientsUsersList"] = authorizedbuyersmarketplace.post(
        "v1/{name}:deactivate",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClientUserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersClientsUsersGet"] = authorizedbuyersmarketplace.post(
        "v1/{name}:deactivate",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClientUserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersClientsUsersActivate"] = authorizedbuyersmarketplace.post(
        "v1/{name}:deactivate",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClientUserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersClientsUsersDeactivate"] = authorizedbuyersmarketplace.post(
        "v1/{name}:deactivate",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClientUserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="authorizedbuyersmarketplace",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
