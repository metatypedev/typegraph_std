from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_authorizedbuyersmarketplace() -> Import:
    authorizedbuyersmarketplace = HTTPRuntime(
        "https://authorizedbuyersmarketplace.googleapis.com/"
    )

    renames = {
        "ErrorResponse": "_authorizedbuyersmarketplace_1_ErrorResponse",
        "DealPausingInfoIn": "_authorizedbuyersmarketplace_2_DealPausingInfoIn",
        "DealPausingInfoOut": "_authorizedbuyersmarketplace_3_DealPausingInfoOut",
        "DeactivateClientRequestIn": "_authorizedbuyersmarketplace_4_DeactivateClientRequestIn",
        "DeactivateClientRequestOut": "_authorizedbuyersmarketplace_5_DeactivateClientRequestOut",
        "EmptyIn": "_authorizedbuyersmarketplace_6_EmptyIn",
        "EmptyOut": "_authorizedbuyersmarketplace_7_EmptyOut",
        "UnsubscribeClientsRequestIn": "_authorizedbuyersmarketplace_8_UnsubscribeClientsRequestIn",
        "UnsubscribeClientsRequestOut": "_authorizedbuyersmarketplace_9_UnsubscribeClientsRequestOut",
        "AuctionPackageIn": "_authorizedbuyersmarketplace_10_AuctionPackageIn",
        "AuctionPackageOut": "_authorizedbuyersmarketplace_11_AuctionPackageOut",
        "SubscribeClientsRequestIn": "_authorizedbuyersmarketplace_12_SubscribeClientsRequestIn",
        "SubscribeClientsRequestOut": "_authorizedbuyersmarketplace_13_SubscribeClientsRequestOut",
        "SubscribeAuctionPackageRequestIn": "_authorizedbuyersmarketplace_14_SubscribeAuctionPackageRequestIn",
        "SubscribeAuctionPackageRequestOut": "_authorizedbuyersmarketplace_15_SubscribeAuctionPackageRequestOut",
        "SendRfpRequestIn": "_authorizedbuyersmarketplace_16_SendRfpRequestIn",
        "SendRfpRequestOut": "_authorizedbuyersmarketplace_17_SendRfpRequestOut",
        "ListAuctionPackagesResponseIn": "_authorizedbuyersmarketplace_18_ListAuctionPackagesResponseIn",
        "ListAuctionPackagesResponseOut": "_authorizedbuyersmarketplace_19_ListAuctionPackagesResponseOut",
        "ListClientUsersResponseIn": "_authorizedbuyersmarketplace_20_ListClientUsersResponseIn",
        "ListClientUsersResponseOut": "_authorizedbuyersmarketplace_21_ListClientUsersResponseOut",
        "UpdateDealRequestIn": "_authorizedbuyersmarketplace_22_UpdateDealRequestIn",
        "UpdateDealRequestOut": "_authorizedbuyersmarketplace_23_UpdateDealRequestOut",
        "CriteriaTargetingIn": "_authorizedbuyersmarketplace_24_CriteriaTargetingIn",
        "CriteriaTargetingOut": "_authorizedbuyersmarketplace_25_CriteriaTargetingOut",
        "BatchUpdateDealsResponseIn": "_authorizedbuyersmarketplace_26_BatchUpdateDealsResponseIn",
        "BatchUpdateDealsResponseOut": "_authorizedbuyersmarketplace_27_BatchUpdateDealsResponseOut",
        "InventoryTypeTargetingIn": "_authorizedbuyersmarketplace_28_InventoryTypeTargetingIn",
        "InventoryTypeTargetingOut": "_authorizedbuyersmarketplace_29_InventoryTypeTargetingOut",
        "TimeOfDayIn": "_authorizedbuyersmarketplace_30_TimeOfDayIn",
        "TimeOfDayOut": "_authorizedbuyersmarketplace_31_TimeOfDayOut",
        "PauseFinalizedDealRequestIn": "_authorizedbuyersmarketplace_32_PauseFinalizedDealRequestIn",
        "PauseFinalizedDealRequestOut": "_authorizedbuyersmarketplace_33_PauseFinalizedDealRequestOut",
        "FirstPartyMobileApplicationTargetingIn": "_authorizedbuyersmarketplace_34_FirstPartyMobileApplicationTargetingIn",
        "FirstPartyMobileApplicationTargetingOut": "_authorizedbuyersmarketplace_35_FirstPartyMobileApplicationTargetingOut",
        "ActivateClientRequestIn": "_authorizedbuyersmarketplace_36_ActivateClientRequestIn",
        "ActivateClientRequestOut": "_authorizedbuyersmarketplace_37_ActivateClientRequestOut",
        "FrequencyCapIn": "_authorizedbuyersmarketplace_38_FrequencyCapIn",
        "FrequencyCapOut": "_authorizedbuyersmarketplace_39_FrequencyCapOut",
        "TechnologyTargetingIn": "_authorizedbuyersmarketplace_40_TechnologyTargetingIn",
        "TechnologyTargetingOut": "_authorizedbuyersmarketplace_41_TechnologyTargetingOut",
        "DealIn": "_authorizedbuyersmarketplace_42_DealIn",
        "DealOut": "_authorizedbuyersmarketplace_43_DealOut",
        "SetReadyToServeRequestIn": "_authorizedbuyersmarketplace_44_SetReadyToServeRequestIn",
        "SetReadyToServeRequestOut": "_authorizedbuyersmarketplace_45_SetReadyToServeRequestOut",
        "AcceptProposalRequestIn": "_authorizedbuyersmarketplace_46_AcceptProposalRequestIn",
        "AcceptProposalRequestOut": "_authorizedbuyersmarketplace_47_AcceptProposalRequestOut",
        "ListPublisherProfilesResponseIn": "_authorizedbuyersmarketplace_48_ListPublisherProfilesResponseIn",
        "ListPublisherProfilesResponseOut": "_authorizedbuyersmarketplace_49_ListPublisherProfilesResponseOut",
        "InventorySizeTargetingIn": "_authorizedbuyersmarketplace_50_InventorySizeTargetingIn",
        "InventorySizeTargetingOut": "_authorizedbuyersmarketplace_51_InventorySizeTargetingOut",
        "TimeZoneIn": "_authorizedbuyersmarketplace_52_TimeZoneIn",
        "TimeZoneOut": "_authorizedbuyersmarketplace_53_TimeZoneOut",
        "DeliveryControlIn": "_authorizedbuyersmarketplace_54_DeliveryControlIn",
        "DeliveryControlOut": "_authorizedbuyersmarketplace_55_DeliveryControlOut",
        "RtbMetricsIn": "_authorizedbuyersmarketplace_56_RtbMetricsIn",
        "RtbMetricsOut": "_authorizedbuyersmarketplace_57_RtbMetricsOut",
        "ContactIn": "_authorizedbuyersmarketplace_58_ContactIn",
        "ContactOut": "_authorizedbuyersmarketplace_59_ContactOut",
        "PrivateDataIn": "_authorizedbuyersmarketplace_60_PrivateDataIn",
        "PrivateDataOut": "_authorizedbuyersmarketplace_61_PrivateDataOut",
        "FinalizedDealIn": "_authorizedbuyersmarketplace_62_FinalizedDealIn",
        "FinalizedDealOut": "_authorizedbuyersmarketplace_63_FinalizedDealOut",
        "UnsubscribeAuctionPackageRequestIn": "_authorizedbuyersmarketplace_64_UnsubscribeAuctionPackageRequestIn",
        "UnsubscribeAuctionPackageRequestOut": "_authorizedbuyersmarketplace_65_UnsubscribeAuctionPackageRequestOut",
        "PreferredDealTermsIn": "_authorizedbuyersmarketplace_66_PreferredDealTermsIn",
        "PreferredDealTermsOut": "_authorizedbuyersmarketplace_67_PreferredDealTermsOut",
        "PlacementTargetingIn": "_authorizedbuyersmarketplace_68_PlacementTargetingIn",
        "PlacementTargetingOut": "_authorizedbuyersmarketplace_69_PlacementTargetingOut",
        "NoteIn": "_authorizedbuyersmarketplace_70_NoteIn",
        "NoteOut": "_authorizedbuyersmarketplace_71_NoteOut",
        "DayPartTargetingIn": "_authorizedbuyersmarketplace_72_DayPartTargetingIn",
        "DayPartTargetingOut": "_authorizedbuyersmarketplace_73_DayPartTargetingOut",
        "ListDealsResponseIn": "_authorizedbuyersmarketplace_74_ListDealsResponseIn",
        "ListDealsResponseOut": "_authorizedbuyersmarketplace_75_ListDealsResponseOut",
        "PublisherProfileMobileApplicationIn": "_authorizedbuyersmarketplace_76_PublisherProfileMobileApplicationIn",
        "PublisherProfileMobileApplicationOut": "_authorizedbuyersmarketplace_77_PublisherProfileMobileApplicationOut",
        "ProposalIn": "_authorizedbuyersmarketplace_78_ProposalIn",
        "ProposalOut": "_authorizedbuyersmarketplace_79_ProposalOut",
        "CreativeRequirementsIn": "_authorizedbuyersmarketplace_80_CreativeRequirementsIn",
        "CreativeRequirementsOut": "_authorizedbuyersmarketplace_81_CreativeRequirementsOut",
        "ActivateClientUserRequestIn": "_authorizedbuyersmarketplace_82_ActivateClientUserRequestIn",
        "ActivateClientUserRequestOut": "_authorizedbuyersmarketplace_83_ActivateClientUserRequestOut",
        "VideoTargetingIn": "_authorizedbuyersmarketplace_84_VideoTargetingIn",
        "VideoTargetingOut": "_authorizedbuyersmarketplace_85_VideoTargetingOut",
        "ListClientsResponseIn": "_authorizedbuyersmarketplace_86_ListClientsResponseIn",
        "ListClientsResponseOut": "_authorizedbuyersmarketplace_87_ListClientsResponseOut",
        "PrivateAuctionTermsIn": "_authorizedbuyersmarketplace_88_PrivateAuctionTermsIn",
        "PrivateAuctionTermsOut": "_authorizedbuyersmarketplace_89_PrivateAuctionTermsOut",
        "ClientIn": "_authorizedbuyersmarketplace_90_ClientIn",
        "ClientOut": "_authorizedbuyersmarketplace_91_ClientOut",
        "MobileApplicationTargetingIn": "_authorizedbuyersmarketplace_92_MobileApplicationTargetingIn",
        "MobileApplicationTargetingOut": "_authorizedbuyersmarketplace_93_MobileApplicationTargetingOut",
        "PriceIn": "_authorizedbuyersmarketplace_94_PriceIn",
        "PriceOut": "_authorizedbuyersmarketplace_95_PriceOut",
        "AdSizeIn": "_authorizedbuyersmarketplace_96_AdSizeIn",
        "AdSizeOut": "_authorizedbuyersmarketplace_97_AdSizeOut",
        "UriTargetingIn": "_authorizedbuyersmarketplace_98_UriTargetingIn",
        "UriTargetingOut": "_authorizedbuyersmarketplace_99_UriTargetingOut",
        "DeactivateClientUserRequestIn": "_authorizedbuyersmarketplace_100_DeactivateClientUserRequestIn",
        "DeactivateClientUserRequestOut": "_authorizedbuyersmarketplace_101_DeactivateClientUserRequestOut",
        "ClientUserIn": "_authorizedbuyersmarketplace_102_ClientUserIn",
        "ClientUserOut": "_authorizedbuyersmarketplace_103_ClientUserOut",
        "MoneyIn": "_authorizedbuyersmarketplace_104_MoneyIn",
        "MoneyOut": "_authorizedbuyersmarketplace_105_MoneyOut",
        "MarketplaceTargetingIn": "_authorizedbuyersmarketplace_106_MarketplaceTargetingIn",
        "MarketplaceTargetingOut": "_authorizedbuyersmarketplace_107_MarketplaceTargetingOut",
        "CancelNegotiationRequestIn": "_authorizedbuyersmarketplace_108_CancelNegotiationRequestIn",
        "CancelNegotiationRequestOut": "_authorizedbuyersmarketplace_109_CancelNegotiationRequestOut",
        "ListFinalizedDealsResponseIn": "_authorizedbuyersmarketplace_110_ListFinalizedDealsResponseIn",
        "ListFinalizedDealsResponseOut": "_authorizedbuyersmarketplace_111_ListFinalizedDealsResponseOut",
        "AddNoteRequestIn": "_authorizedbuyersmarketplace_112_AddNoteRequestIn",
        "AddNoteRequestOut": "_authorizedbuyersmarketplace_113_AddNoteRequestOut",
        "PublisherProfileIn": "_authorizedbuyersmarketplace_114_PublisherProfileIn",
        "PublisherProfileOut": "_authorizedbuyersmarketplace_115_PublisherProfileOut",
        "DayPartIn": "_authorizedbuyersmarketplace_116_DayPartIn",
        "DayPartOut": "_authorizedbuyersmarketplace_117_DayPartOut",
        "ProgrammaticGuaranteedTermsIn": "_authorizedbuyersmarketplace_118_ProgrammaticGuaranteedTermsIn",
        "ProgrammaticGuaranteedTermsOut": "_authorizedbuyersmarketplace_119_ProgrammaticGuaranteedTermsOut",
        "BatchUpdateDealsRequestIn": "_authorizedbuyersmarketplace_120_BatchUpdateDealsRequestIn",
        "BatchUpdateDealsRequestOut": "_authorizedbuyersmarketplace_121_BatchUpdateDealsRequestOut",
        "ResumeFinalizedDealRequestIn": "_authorizedbuyersmarketplace_122_ResumeFinalizedDealRequestIn",
        "ResumeFinalizedDealRequestOut": "_authorizedbuyersmarketplace_123_ResumeFinalizedDealRequestOut",
        "AddCreativeRequestIn": "_authorizedbuyersmarketplace_124_AddCreativeRequestIn",
        "AddCreativeRequestOut": "_authorizedbuyersmarketplace_125_AddCreativeRequestOut",
        "OperatingSystemTargetingIn": "_authorizedbuyersmarketplace_126_OperatingSystemTargetingIn",
        "OperatingSystemTargetingOut": "_authorizedbuyersmarketplace_127_OperatingSystemTargetingOut",
        "ListProposalsResponseIn": "_authorizedbuyersmarketplace_128_ListProposalsResponseIn",
        "ListProposalsResponseOut": "_authorizedbuyersmarketplace_129_ListProposalsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["DealPausingInfoIn"] = t.struct(
        {
            "pauseRole": t.string().optional(),
            "pauseReason": t.string().optional(),
            "pausingConsented": t.boolean().optional(),
        }
    ).named(renames["DealPausingInfoIn"])
    types["DealPausingInfoOut"] = t.struct(
        {
            "pauseRole": t.string().optional(),
            "pauseReason": t.string().optional(),
            "pausingConsented": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DealPausingInfoOut"])
    types["DeactivateClientRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeactivateClientRequestIn"]
    )
    types["DeactivateClientRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeactivateClientRequestOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["UnsubscribeClientsRequestIn"] = t.struct(
        {"clients": t.array(t.string()).optional()}
    ).named(renames["UnsubscribeClientsRequestIn"])
    types["UnsubscribeClientsRequestOut"] = t.struct(
        {
            "clients": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UnsubscribeClientsRequestOut"])
    types["AuctionPackageIn"] = t.struct(
        {"name": t.string().optional(), "displayName": t.string().optional()}
    ).named(renames["AuctionPackageIn"])
    types["AuctionPackageOut"] = t.struct(
        {
            "creator": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "subscribedClients": t.array(t.string()).optional(),
            "updateTime": t.string().optional(),
            "displayName": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuctionPackageOut"])
    types["SubscribeClientsRequestIn"] = t.struct(
        {"clients": t.array(t.string()).optional()}
    ).named(renames["SubscribeClientsRequestIn"])
    types["SubscribeClientsRequestOut"] = t.struct(
        {
            "clients": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscribeClientsRequestOut"])
    types["SubscribeAuctionPackageRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["SubscribeAuctionPackageRequestIn"])
    types["SubscribeAuctionPackageRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SubscribeAuctionPackageRequestOut"])
    types["SendRfpRequestIn"] = t.struct(
        {
            "flightEndTime": t.string(),
            "client": t.string().optional(),
            "note": t.string().optional(),
            "flightStartTime": t.string(),
            "displayName": t.string(),
            "geoTargeting": t.proxy(renames["CriteriaTargetingIn"]).optional(),
            "estimatedGrossSpend": t.proxy(renames["MoneyIn"]).optional(),
            "buyerContacts": t.array(t.proxy(renames["ContactIn"])).optional(),
            "publisherProfile": t.string(),
            "inventorySizeTargeting": t.proxy(
                renames["InventorySizeTargetingIn"]
            ).optional(),
            "preferredDealTerms": t.proxy(renames["PreferredDealTermsIn"]).optional(),
            "programmaticGuaranteedTerms": t.proxy(
                renames["ProgrammaticGuaranteedTermsIn"]
            ).optional(),
        }
    ).named(renames["SendRfpRequestIn"])
    types["SendRfpRequestOut"] = t.struct(
        {
            "flightEndTime": t.string(),
            "client": t.string().optional(),
            "note": t.string().optional(),
            "flightStartTime": t.string(),
            "displayName": t.string(),
            "geoTargeting": t.proxy(renames["CriteriaTargetingOut"]).optional(),
            "estimatedGrossSpend": t.proxy(renames["MoneyOut"]).optional(),
            "buyerContacts": t.array(t.proxy(renames["ContactOut"])).optional(),
            "publisherProfile": t.string(),
            "inventorySizeTargeting": t.proxy(
                renames["InventorySizeTargetingOut"]
            ).optional(),
            "preferredDealTerms": t.proxy(renames["PreferredDealTermsOut"]).optional(),
            "programmaticGuaranteedTerms": t.proxy(
                renames["ProgrammaticGuaranteedTermsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SendRfpRequestOut"])
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
    types["BatchUpdateDealsResponseIn"] = t.struct(
        {"deals": t.array(t.proxy(renames["DealIn"])).optional()}
    ).named(renames["BatchUpdateDealsResponseIn"])
    types["BatchUpdateDealsResponseOut"] = t.struct(
        {
            "deals": t.array(t.proxy(renames["DealOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateDealsResponseOut"])
    types["InventoryTypeTargetingIn"] = t.struct(
        {"inventoryTypes": t.array(t.string()).optional()}
    ).named(renames["InventoryTypeTargetingIn"])
    types["InventoryTypeTargetingOut"] = t.struct(
        {
            "inventoryTypes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventoryTypeTargetingOut"])
    types["TimeOfDayIn"] = t.struct(
        {
            "seconds": t.integer().optional(),
            "minutes": t.integer().optional(),
            "nanos": t.integer().optional(),
            "hours": t.integer().optional(),
        }
    ).named(renames["TimeOfDayIn"])
    types["TimeOfDayOut"] = t.struct(
        {
            "seconds": t.integer().optional(),
            "minutes": t.integer().optional(),
            "nanos": t.integer().optional(),
            "hours": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeOfDayOut"])
    types["PauseFinalizedDealRequestIn"] = t.struct(
        {"reason": t.string().optional()}
    ).named(renames["PauseFinalizedDealRequestIn"])
    types["PauseFinalizedDealRequestOut"] = t.struct(
        {
            "reason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PauseFinalizedDealRequestOut"])
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
    types["FrequencyCapIn"] = t.struct(
        {
            "timeUnitType": t.string().optional(),
            "maxImpressions": t.integer().optional(),
            "timeUnitsCount": t.integer().optional(),
        }
    ).named(renames["FrequencyCapIn"])
    types["FrequencyCapOut"] = t.struct(
        {
            "timeUnitType": t.string().optional(),
            "maxImpressions": t.integer().optional(),
            "timeUnitsCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FrequencyCapOut"])
    types["TechnologyTargetingIn"] = t.struct(
        {
            "operatingSystemTargeting": t.proxy(
                renames["OperatingSystemTargetingIn"]
            ).optional(),
            "deviceCategoryTargeting": t.proxy(
                renames["CriteriaTargetingIn"]
            ).optional(),
            "deviceCapabilityTargeting": t.proxy(
                renames["CriteriaTargetingIn"]
            ).optional(),
        }
    ).named(renames["TechnologyTargetingIn"])
    types["TechnologyTargetingOut"] = t.struct(
        {
            "operatingSystemTargeting": t.proxy(
                renames["OperatingSystemTargetingOut"]
            ).optional(),
            "deviceCategoryTargeting": t.proxy(
                renames["CriteriaTargetingOut"]
            ).optional(),
            "deviceCapabilityTargeting": t.proxy(
                renames["CriteriaTargetingOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TechnologyTargetingOut"])
    types["DealIn"] = t.struct(
        {
            "privateAuctionTerms": t.proxy(renames["PrivateAuctionTermsIn"]).optional(),
            "name": t.string().optional(),
            "estimatedGrossSpend": t.proxy(renames["MoneyIn"]).optional(),
            "flightEndTime": t.string().optional(),
            "publisherProfile": t.string().optional(),
            "programmaticGuaranteedTerms": t.proxy(
                renames["ProgrammaticGuaranteedTermsIn"]
            ).optional(),
            "flightStartTime": t.string().optional(),
            "targeting": t.proxy(renames["MarketplaceTargetingIn"]).optional(),
            "preferredDealTerms": t.proxy(renames["PreferredDealTermsIn"]).optional(),
        }
    ).named(renames["DealIn"])
    types["DealOut"] = t.struct(
        {
            "privateAuctionTerms": t.proxy(
                renames["PrivateAuctionTermsOut"]
            ).optional(),
            "name": t.string().optional(),
            "estimatedGrossSpend": t.proxy(renames["MoneyOut"]).optional(),
            "client": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "deliveryControl": t.proxy(renames["DeliveryControlOut"]).optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "sellerTimeZone": t.proxy(renames["TimeZoneOut"]).optional(),
            "flightEndTime": t.string().optional(),
            "publisherProfile": t.string().optional(),
            "dealType": t.string().optional(),
            "programmaticGuaranteedTerms": t.proxy(
                renames["ProgrammaticGuaranteedTermsOut"]
            ).optional(),
            "flightStartTime": t.string().optional(),
            "targeting": t.proxy(renames["MarketplaceTargetingOut"]).optional(),
            "proposalRevision": t.string().optional(),
            "billedBuyer": t.string().optional(),
            "creativeRequirements": t.proxy(
                renames["CreativeRequirementsOut"]
            ).optional(),
            "preferredDealTerms": t.proxy(renames["PreferredDealTermsOut"]).optional(),
            "buyer": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DealOut"])
    types["SetReadyToServeRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["SetReadyToServeRequestIn"]
    )
    types["SetReadyToServeRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SetReadyToServeRequestOut"])
    types["AcceptProposalRequestIn"] = t.struct(
        {"proposalRevision": t.string().optional()}
    ).named(renames["AcceptProposalRequestIn"])
    types["AcceptProposalRequestOut"] = t.struct(
        {
            "proposalRevision": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AcceptProposalRequestOut"])
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
    types["DeliveryControlIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeliveryControlIn"]
    )
    types["DeliveryControlOut"] = t.struct(
        {
            "roadblockingType": t.string().optional(),
            "companionDeliveryType": t.string().optional(),
            "frequencyCap": t.array(t.proxy(renames["FrequencyCapOut"])).optional(),
            "deliveryRateType": t.string().optional(),
            "creativeRotationType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeliveryControlOut"])
    types["RtbMetricsIn"] = t.struct(
        {
            "bidRate7Days": t.number().optional(),
            "mustBidRateCurrentMonth": t.number().optional(),
            "adImpressions7Days": t.string().optional(),
            "filteredBidRate7Days": t.number().optional(),
            "bidRequests7Days": t.string().optional(),
            "bids7Days": t.string().optional(),
        }
    ).named(renames["RtbMetricsIn"])
    types["RtbMetricsOut"] = t.struct(
        {
            "bidRate7Days": t.number().optional(),
            "mustBidRateCurrentMonth": t.number().optional(),
            "adImpressions7Days": t.string().optional(),
            "filteredBidRate7Days": t.number().optional(),
            "bidRequests7Days": t.string().optional(),
            "bids7Days": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RtbMetricsOut"])
    types["ContactIn"] = t.struct(
        {"email": t.string().optional(), "displayName": t.string().optional()}
    ).named(renames["ContactIn"])
    types["ContactOut"] = t.struct(
        {
            "email": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContactOut"])
    types["PrivateDataIn"] = t.struct({"referenceId": t.string().optional()}).named(
        renames["PrivateDataIn"]
    )
    types["PrivateDataOut"] = t.struct(
        {
            "referenceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrivateDataOut"])
    types["FinalizedDealIn"] = t.struct(
        {
            "name": t.string().optional(),
            "deal": t.proxy(renames["DealIn"]).optional(),
            "rtbMetrics": t.proxy(renames["RtbMetricsIn"]).optional(),
            "dealPausingInfo": t.proxy(renames["DealPausingInfoIn"]).optional(),
            "readyToServe": t.boolean().optional(),
            "dealServingStatus": t.string().optional(),
        }
    ).named(renames["FinalizedDealIn"])
    types["FinalizedDealOut"] = t.struct(
        {
            "name": t.string().optional(),
            "deal": t.proxy(renames["DealOut"]).optional(),
            "rtbMetrics": t.proxy(renames["RtbMetricsOut"]).optional(),
            "dealPausingInfo": t.proxy(renames["DealPausingInfoOut"]).optional(),
            "readyToServe": t.boolean().optional(),
            "dealServingStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FinalizedDealOut"])
    types["UnsubscribeAuctionPackageRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["UnsubscribeAuctionPackageRequestIn"])
    types["UnsubscribeAuctionPackageRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UnsubscribeAuctionPackageRequestOut"])
    types["PreferredDealTermsIn"] = t.struct(
        {"fixedPrice": t.proxy(renames["PriceIn"]).optional()}
    ).named(renames["PreferredDealTermsIn"])
    types["PreferredDealTermsOut"] = t.struct(
        {
            "fixedPrice": t.proxy(renames["PriceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PreferredDealTermsOut"])
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
            "createTime": t.string().optional(),
            "creatorRole": t.string().optional(),
            "note": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NoteOut"])
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
    types["PublisherProfileMobileApplicationIn"] = t.struct(
        {
            "appStore": t.string().optional(),
            "externalAppId": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["PublisherProfileMobileApplicationIn"])
    types["PublisherProfileMobileApplicationOut"] = t.struct(
        {
            "appStore": t.string().optional(),
            "externalAppId": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublisherProfileMobileApplicationOut"])
    types["ProposalIn"] = t.struct(
        {
            "buyerPrivateData": t.proxy(renames["PrivateDataIn"]).optional(),
            "buyerContacts": t.array(t.proxy(renames["ContactIn"])).optional(),
            "pausingConsented": t.boolean().optional(),
            "name": t.string().optional(),
            "publisherProfile": t.string().optional(),
            "notes": t.array(t.proxy(renames["NoteIn"])).optional(),
        }
    ).named(renames["ProposalIn"])
    types["ProposalOut"] = t.struct(
        {
            "buyer": t.string().optional(),
            "state": t.string().optional(),
            "termsAndConditions": t.string().optional(),
            "buyerPrivateData": t.proxy(renames["PrivateDataOut"]).optional(),
            "buyerContacts": t.array(t.proxy(renames["ContactOut"])).optional(),
            "dealType": t.string().optional(),
            "proposalRevision": t.string().optional(),
            "originatorRole": t.string().optional(),
            "client": t.string().optional(),
            "pausingConsented": t.boolean().optional(),
            "name": t.string().optional(),
            "isRenegotiating": t.boolean().optional(),
            "billedBuyer": t.string().optional(),
            "sellerContacts": t.array(t.proxy(renames["ContactOut"])).optional(),
            "displayName": t.string().optional(),
            "updateTime": t.string().optional(),
            "lastUpdaterOrCommentorRole": t.string().optional(),
            "publisherProfile": t.string().optional(),
            "notes": t.array(t.proxy(renames["NoteOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProposalOut"])
    types["CreativeRequirementsIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CreativeRequirementsIn"]
    )
    types["CreativeRequirementsOut"] = t.struct(
        {
            "creativeFormat": t.string().optional(),
            "creativePreApprovalPolicy": t.string().optional(),
            "skippableAdType": t.string().optional(),
            "programmaticCreativeSource": t.string().optional(),
            "creativeSafeFrameCompatibility": t.string().optional(),
            "maxAdDurationMs": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeRequirementsOut"])
    types["ActivateClientUserRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ActivateClientUserRequestIn"]
    )
    types["ActivateClientUserRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ActivateClientUserRequestOut"])
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
    types["PrivateAuctionTermsIn"] = t.struct(
        {"floorPrice": t.proxy(renames["PriceIn"]).optional()}
    ).named(renames["PrivateAuctionTermsIn"])
    types["PrivateAuctionTermsOut"] = t.struct(
        {
            "openAuctionAllowed": t.boolean().optional(),
            "floorPrice": t.proxy(renames["PriceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrivateAuctionTermsOut"])
    types["ClientIn"] = t.struct(
        {
            "role": t.string(),
            "sellerVisible": t.boolean().optional(),
            "partnerClientId": t.string().optional(),
            "displayName": t.string(),
        }
    ).named(renames["ClientIn"])
    types["ClientOut"] = t.struct(
        {
            "role": t.string(),
            "sellerVisible": t.boolean().optional(),
            "partnerClientId": t.string().optional(),
            "displayName": t.string(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientOut"])
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
    types["AdSizeIn"] = t.struct(
        {
            "type": t.string().optional(),
            "width": t.string().optional(),
            "height": t.string().optional(),
        }
    ).named(renames["AdSizeIn"])
    types["AdSizeOut"] = t.struct(
        {
            "type": t.string().optional(),
            "width": t.string().optional(),
            "height": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdSizeOut"])
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
    types["DeactivateClientUserRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DeactivateClientUserRequestIn"])
    types["DeactivateClientUserRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeactivateClientUserRequestOut"])
    types["ClientUserIn"] = t.struct({"email": t.string()}).named(
        renames["ClientUserIn"]
    )
    types["ClientUserOut"] = t.struct(
        {
            "name": t.string().optional(),
            "state": t.string().optional(),
            "email": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientUserOut"])
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
    types["MarketplaceTargetingIn"] = t.struct(
        {
            "userListTargeting": t.proxy(renames["CriteriaTargetingIn"]).optional(),
            "daypartTargeting": t.proxy(renames["DayPartTargetingIn"]).optional(),
        }
    ).named(renames["MarketplaceTargetingIn"])
    types["MarketplaceTargetingOut"] = t.struct(
        {
            "inventoryTypeTargeting": t.proxy(
                renames["InventoryTypeTargetingOut"]
            ).optional(),
            "geoTargeting": t.proxy(renames["CriteriaTargetingOut"]).optional(),
            "videoTargeting": t.proxy(renames["VideoTargetingOut"]).optional(),
            "inventorySizeTargeting": t.proxy(
                renames["InventorySizeTargetingOut"]
            ).optional(),
            "userListTargeting": t.proxy(renames["CriteriaTargetingOut"]).optional(),
            "technologyTargeting": t.proxy(
                renames["TechnologyTargetingOut"]
            ).optional(),
            "daypartTargeting": t.proxy(renames["DayPartTargetingOut"]).optional(),
            "placementTargeting": t.proxy(renames["PlacementTargetingOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MarketplaceTargetingOut"])
    types["CancelNegotiationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelNegotiationRequestIn"]
    )
    types["CancelNegotiationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelNegotiationRequestOut"])
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
    types["AddNoteRequestIn"] = t.struct(
        {"note": t.proxy(renames["NoteIn"]).optional()}
    ).named(renames["AddNoteRequestIn"])
    types["AddNoteRequestOut"] = t.struct(
        {
            "note": t.proxy(renames["NoteOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddNoteRequestOut"])
    types["PublisherProfileIn"] = t.struct(
        {
            "audienceDescription": t.string().optional(),
            "name": t.string().optional(),
            "overview": t.string().optional(),
            "mobileApps": t.array(
                t.proxy(renames["PublisherProfileMobileApplicationIn"])
            ).optional(),
            "displayName": t.string().optional(),
            "mediaKitUrl": t.string().optional(),
            "pitchStatement": t.string().optional(),
            "directDealsContact": t.string().optional(),
            "samplePageUrl": t.string().optional(),
            "programmaticDealsContact": t.string().optional(),
            "domains": t.array(t.string()).optional(),
            "logoUrl": t.string().optional(),
            "topHeadlines": t.array(t.string()).optional(),
            "isParent": t.boolean().optional(),
            "publisherCode": t.string().optional(),
        }
    ).named(renames["PublisherProfileIn"])
    types["PublisherProfileOut"] = t.struct(
        {
            "audienceDescription": t.string().optional(),
            "name": t.string().optional(),
            "overview": t.string().optional(),
            "mobileApps": t.array(
                t.proxy(renames["PublisherProfileMobileApplicationOut"])
            ).optional(),
            "displayName": t.string().optional(),
            "mediaKitUrl": t.string().optional(),
            "pitchStatement": t.string().optional(),
            "directDealsContact": t.string().optional(),
            "samplePageUrl": t.string().optional(),
            "programmaticDealsContact": t.string().optional(),
            "domains": t.array(t.string()).optional(),
            "logoUrl": t.string().optional(),
            "topHeadlines": t.array(t.string()).optional(),
            "isParent": t.boolean().optional(),
            "publisherCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublisherProfileOut"])
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
    types["ProgrammaticGuaranteedTermsIn"] = t.struct(
        {
            "fixedPrice": t.proxy(renames["PriceIn"]).optional(),
            "minimumDailyLooks": t.string().optional(),
            "percentShareOfVoice": t.string().optional(),
            "guaranteedLooks": t.string().optional(),
            "reservationType": t.string().optional(),
            "impressionCap": t.string().optional(),
        }
    ).named(renames["ProgrammaticGuaranteedTermsIn"])
    types["ProgrammaticGuaranteedTermsOut"] = t.struct(
        {
            "fixedPrice": t.proxy(renames["PriceOut"]).optional(),
            "minimumDailyLooks": t.string().optional(),
            "percentShareOfVoice": t.string().optional(),
            "guaranteedLooks": t.string().optional(),
            "reservationType": t.string().optional(),
            "impressionCap": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProgrammaticGuaranteedTermsOut"])
    types["BatchUpdateDealsRequestIn"] = t.struct(
        {"requests": t.array(t.proxy(renames["UpdateDealRequestIn"]))}
    ).named(renames["BatchUpdateDealsRequestIn"])
    types["BatchUpdateDealsRequestOut"] = t.struct(
        {
            "requests": t.array(t.proxy(renames["UpdateDealRequestOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateDealsRequestOut"])
    types["ResumeFinalizedDealRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ResumeFinalizedDealRequestIn"])
    types["ResumeFinalizedDealRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ResumeFinalizedDealRequestOut"])
    types["AddCreativeRequestIn"] = t.struct({"creative": t.string().optional()}).named(
        renames["AddCreativeRequestIn"]
    )
    types["AddCreativeRequestOut"] = t.struct(
        {
            "creative": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddCreativeRequestOut"])
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

    functions = {}
    functions["biddersFinalizedDealsList"] = authorizedbuyersmarketplace.get(
        "v1/{parent}/finalizedDeals",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFinalizedDealsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersAuctionPackagesGet"] = authorizedbuyersmarketplace.get(
        "v1/{parent}/auctionPackages",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAuctionPackagesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "buyersAuctionPackagesUnsubscribeClients"
    ] = authorizedbuyersmarketplace.get(
        "v1/{parent}/auctionPackages",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAuctionPackagesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersAuctionPackagesSubscribe"] = authorizedbuyersmarketplace.get(
        "v1/{parent}/auctionPackages",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAuctionPackagesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersAuctionPackagesUnsubscribe"] = authorizedbuyersmarketplace.get(
        "v1/{parent}/auctionPackages",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAuctionPackagesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "buyersAuctionPackagesSubscribeClients"
    ] = authorizedbuyersmarketplace.get(
        "v1/{parent}/auctionPackages",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAuctionPackagesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersAuctionPackagesList"] = authorizedbuyersmarketplace.get(
        "v1/{parent}/auctionPackages",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAuctionPackagesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersPublisherProfilesGet"] = authorizedbuyersmarketplace.get(
        "v1/{parent}/publisherProfiles",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPublisherProfilesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersPublisherProfilesList"] = authorizedbuyersmarketplace.get(
        "v1/{parent}/publisherProfiles",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPublisherProfilesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersFinalizedDealsSetReadyToServe"] = authorizedbuyersmarketplace.get(
        "v1/{parent}/finalizedDeals",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
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
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
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
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
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
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFinalizedDealsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersFinalizedDealsResume"] = authorizedbuyersmarketplace.get(
        "v1/{parent}/finalizedDeals",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
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
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFinalizedDealsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersProposalsSendRfp"] = authorizedbuyersmarketplace.post(
        "v1/{proposal}:addNote",
        t.struct(
            {
                "proposal": t.string().optional(),
                "note": t.proxy(renames["NoteIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProposalOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersProposalsGet"] = authorizedbuyersmarketplace.post(
        "v1/{proposal}:addNote",
        t.struct(
            {
                "proposal": t.string().optional(),
                "note": t.proxy(renames["NoteIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProposalOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersProposalsPatch"] = authorizedbuyersmarketplace.post(
        "v1/{proposal}:addNote",
        t.struct(
            {
                "proposal": t.string().optional(),
                "note": t.proxy(renames["NoteIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProposalOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersProposalsAccept"] = authorizedbuyersmarketplace.post(
        "v1/{proposal}:addNote",
        t.struct(
            {
                "proposal": t.string().optional(),
                "note": t.proxy(renames["NoteIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProposalOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersProposalsCancelNegotiation"] = authorizedbuyersmarketplace.post(
        "v1/{proposal}:addNote",
        t.struct(
            {
                "proposal": t.string().optional(),
                "note": t.proxy(renames["NoteIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProposalOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersProposalsList"] = authorizedbuyersmarketplace.post(
        "v1/{proposal}:addNote",
        t.struct(
            {
                "proposal": t.string().optional(),
                "note": t.proxy(renames["NoteIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProposalOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersProposalsAddNote"] = authorizedbuyersmarketplace.post(
        "v1/{proposal}:addNote",
        t.struct(
            {
                "proposal": t.string().optional(),
                "note": t.proxy(renames["NoteIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProposalOut"]),
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
    functions["buyersProposalsDealsList"] = authorizedbuyersmarketplace.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["DealOut"]),
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
    functions["buyersProposalsDealsGet"] = authorizedbuyersmarketplace.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["DealOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersClientsActivate"] = authorizedbuyersmarketplace.get(
        "v1/{parent}/clients",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListClientsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersClientsCreate"] = authorizedbuyersmarketplace.get(
        "v1/{parent}/clients",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListClientsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersClientsPatch"] = authorizedbuyersmarketplace.get(
        "v1/{parent}/clients",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListClientsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersClientsDeactivate"] = authorizedbuyersmarketplace.get(
        "v1/{parent}/clients",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListClientsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersClientsGet"] = authorizedbuyersmarketplace.get(
        "v1/{parent}/clients",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListClientsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersClientsList"] = authorizedbuyersmarketplace.get(
        "v1/{parent}/clients",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListClientsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersClientsUsersDelete"] = authorizedbuyersmarketplace.post(
        "v1/{parent}/users",
        t.struct(
            {"parent": t.string(), "email": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["ClientUserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersClientsUsersActivate"] = authorizedbuyersmarketplace.post(
        "v1/{parent}/users",
        t.struct(
            {"parent": t.string(), "email": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["ClientUserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersClientsUsersList"] = authorizedbuyersmarketplace.post(
        "v1/{parent}/users",
        t.struct(
            {"parent": t.string(), "email": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["ClientUserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersClientsUsersDeactivate"] = authorizedbuyersmarketplace.post(
        "v1/{parent}/users",
        t.struct(
            {"parent": t.string(), "email": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["ClientUserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersClientsUsersGet"] = authorizedbuyersmarketplace.post(
        "v1/{parent}/users",
        t.struct(
            {"parent": t.string(), "email": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["ClientUserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersClientsUsersCreate"] = authorizedbuyersmarketplace.post(
        "v1/{parent}/users",
        t.struct(
            {"parent": t.string(), "email": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["ClientUserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="authorizedbuyersmarketplace",
        renames=renames,
        types=types,
        functions=functions,
    )
