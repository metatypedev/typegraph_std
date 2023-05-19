from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_authorizedbuyersmarketplace() -> Import:
    authorizedbuyersmarketplace = HTTPRuntime(
        "https://authorizedbuyersmarketplace.googleapis.com/"
    )

    renames = {
        "ErrorResponse": "_authorizedbuyersmarketplace_1_ErrorResponse",
        "PlacementTargetingIn": "_authorizedbuyersmarketplace_2_PlacementTargetingIn",
        "PlacementTargetingOut": "_authorizedbuyersmarketplace_3_PlacementTargetingOut",
        "ProposalIn": "_authorizedbuyersmarketplace_4_ProposalIn",
        "ProposalOut": "_authorizedbuyersmarketplace_5_ProposalOut",
        "UnsubscribeClientsRequestIn": "_authorizedbuyersmarketplace_6_UnsubscribeClientsRequestIn",
        "UnsubscribeClientsRequestOut": "_authorizedbuyersmarketplace_7_UnsubscribeClientsRequestOut",
        "MoneyIn": "_authorizedbuyersmarketplace_8_MoneyIn",
        "MoneyOut": "_authorizedbuyersmarketplace_9_MoneyOut",
        "PriceIn": "_authorizedbuyersmarketplace_10_PriceIn",
        "PriceOut": "_authorizedbuyersmarketplace_11_PriceOut",
        "PauseFinalizedDealRequestIn": "_authorizedbuyersmarketplace_12_PauseFinalizedDealRequestIn",
        "PauseFinalizedDealRequestOut": "_authorizedbuyersmarketplace_13_PauseFinalizedDealRequestOut",
        "PreferredDealTermsIn": "_authorizedbuyersmarketplace_14_PreferredDealTermsIn",
        "PreferredDealTermsOut": "_authorizedbuyersmarketplace_15_PreferredDealTermsOut",
        "CriteriaTargetingIn": "_authorizedbuyersmarketplace_16_CriteriaTargetingIn",
        "CriteriaTargetingOut": "_authorizedbuyersmarketplace_17_CriteriaTargetingOut",
        "InventorySizeTargetingIn": "_authorizedbuyersmarketplace_18_InventorySizeTargetingIn",
        "InventorySizeTargetingOut": "_authorizedbuyersmarketplace_19_InventorySizeTargetingOut",
        "TimeOfDayIn": "_authorizedbuyersmarketplace_20_TimeOfDayIn",
        "TimeOfDayOut": "_authorizedbuyersmarketplace_21_TimeOfDayOut",
        "BatchUpdateDealsResponseIn": "_authorizedbuyersmarketplace_22_BatchUpdateDealsResponseIn",
        "BatchUpdateDealsResponseOut": "_authorizedbuyersmarketplace_23_BatchUpdateDealsResponseOut",
        "SubscribeClientsRequestIn": "_authorizedbuyersmarketplace_24_SubscribeClientsRequestIn",
        "SubscribeClientsRequestOut": "_authorizedbuyersmarketplace_25_SubscribeClientsRequestOut",
        "FrequencyCapIn": "_authorizedbuyersmarketplace_26_FrequencyCapIn",
        "FrequencyCapOut": "_authorizedbuyersmarketplace_27_FrequencyCapOut",
        "ListFinalizedDealsResponseIn": "_authorizedbuyersmarketplace_28_ListFinalizedDealsResponseIn",
        "ListFinalizedDealsResponseOut": "_authorizedbuyersmarketplace_29_ListFinalizedDealsResponseOut",
        "EmptyIn": "_authorizedbuyersmarketplace_30_EmptyIn",
        "EmptyOut": "_authorizedbuyersmarketplace_31_EmptyOut",
        "PublisherProfileMobileApplicationIn": "_authorizedbuyersmarketplace_32_PublisherProfileMobileApplicationIn",
        "PublisherProfileMobileApplicationOut": "_authorizedbuyersmarketplace_33_PublisherProfileMobileApplicationOut",
        "NoteIn": "_authorizedbuyersmarketplace_34_NoteIn",
        "NoteOut": "_authorizedbuyersmarketplace_35_NoteOut",
        "ListClientsResponseIn": "_authorizedbuyersmarketplace_36_ListClientsResponseIn",
        "ListClientsResponseOut": "_authorizedbuyersmarketplace_37_ListClientsResponseOut",
        "DeliveryControlIn": "_authorizedbuyersmarketplace_38_DeliveryControlIn",
        "DeliveryControlOut": "_authorizedbuyersmarketplace_39_DeliveryControlOut",
        "OperatingSystemTargetingIn": "_authorizedbuyersmarketplace_40_OperatingSystemTargetingIn",
        "OperatingSystemTargetingOut": "_authorizedbuyersmarketplace_41_OperatingSystemTargetingOut",
        "ProgrammaticGuaranteedTermsIn": "_authorizedbuyersmarketplace_42_ProgrammaticGuaranteedTermsIn",
        "ProgrammaticGuaranteedTermsOut": "_authorizedbuyersmarketplace_43_ProgrammaticGuaranteedTermsOut",
        "DayPartTargetingIn": "_authorizedbuyersmarketplace_44_DayPartTargetingIn",
        "DayPartTargetingOut": "_authorizedbuyersmarketplace_45_DayPartTargetingOut",
        "PrivateDataIn": "_authorizedbuyersmarketplace_46_PrivateDataIn",
        "PrivateDataOut": "_authorizedbuyersmarketplace_47_PrivateDataOut",
        "InventoryTypeTargetingIn": "_authorizedbuyersmarketplace_48_InventoryTypeTargetingIn",
        "InventoryTypeTargetingOut": "_authorizedbuyersmarketplace_49_InventoryTypeTargetingOut",
        "UpdateDealRequestIn": "_authorizedbuyersmarketplace_50_UpdateDealRequestIn",
        "UpdateDealRequestOut": "_authorizedbuyersmarketplace_51_UpdateDealRequestOut",
        "ListProposalsResponseIn": "_authorizedbuyersmarketplace_52_ListProposalsResponseIn",
        "ListProposalsResponseOut": "_authorizedbuyersmarketplace_53_ListProposalsResponseOut",
        "ClientIn": "_authorizedbuyersmarketplace_54_ClientIn",
        "ClientOut": "_authorizedbuyersmarketplace_55_ClientOut",
        "FirstPartyMobileApplicationTargetingIn": "_authorizedbuyersmarketplace_56_FirstPartyMobileApplicationTargetingIn",
        "FirstPartyMobileApplicationTargetingOut": "_authorizedbuyersmarketplace_57_FirstPartyMobileApplicationTargetingOut",
        "PrivateAuctionTermsIn": "_authorizedbuyersmarketplace_58_PrivateAuctionTermsIn",
        "PrivateAuctionTermsOut": "_authorizedbuyersmarketplace_59_PrivateAuctionTermsOut",
        "ListDealsResponseIn": "_authorizedbuyersmarketplace_60_ListDealsResponseIn",
        "ListDealsResponseOut": "_authorizedbuyersmarketplace_61_ListDealsResponseOut",
        "UriTargetingIn": "_authorizedbuyersmarketplace_62_UriTargetingIn",
        "UriTargetingOut": "_authorizedbuyersmarketplace_63_UriTargetingOut",
        "VideoTargetingIn": "_authorizedbuyersmarketplace_64_VideoTargetingIn",
        "VideoTargetingOut": "_authorizedbuyersmarketplace_65_VideoTargetingOut",
        "FinalizedDealIn": "_authorizedbuyersmarketplace_66_FinalizedDealIn",
        "FinalizedDealOut": "_authorizedbuyersmarketplace_67_FinalizedDealOut",
        "AuctionPackageIn": "_authorizedbuyersmarketplace_68_AuctionPackageIn",
        "AuctionPackageOut": "_authorizedbuyersmarketplace_69_AuctionPackageOut",
        "SubscribeAuctionPackageRequestIn": "_authorizedbuyersmarketplace_70_SubscribeAuctionPackageRequestIn",
        "SubscribeAuctionPackageRequestOut": "_authorizedbuyersmarketplace_71_SubscribeAuctionPackageRequestOut",
        "AddNoteRequestIn": "_authorizedbuyersmarketplace_72_AddNoteRequestIn",
        "AddNoteRequestOut": "_authorizedbuyersmarketplace_73_AddNoteRequestOut",
        "ContactIn": "_authorizedbuyersmarketplace_74_ContactIn",
        "ContactOut": "_authorizedbuyersmarketplace_75_ContactOut",
        "CancelNegotiationRequestIn": "_authorizedbuyersmarketplace_76_CancelNegotiationRequestIn",
        "CancelNegotiationRequestOut": "_authorizedbuyersmarketplace_77_CancelNegotiationRequestOut",
        "CreativeRequirementsIn": "_authorizedbuyersmarketplace_78_CreativeRequirementsIn",
        "CreativeRequirementsOut": "_authorizedbuyersmarketplace_79_CreativeRequirementsOut",
        "TechnologyTargetingIn": "_authorizedbuyersmarketplace_80_TechnologyTargetingIn",
        "TechnologyTargetingOut": "_authorizedbuyersmarketplace_81_TechnologyTargetingOut",
        "PublisherProfileIn": "_authorizedbuyersmarketplace_82_PublisherProfileIn",
        "PublisherProfileOut": "_authorizedbuyersmarketplace_83_PublisherProfileOut",
        "DeactivateClientUserRequestIn": "_authorizedbuyersmarketplace_84_DeactivateClientUserRequestIn",
        "DeactivateClientUserRequestOut": "_authorizedbuyersmarketplace_85_DeactivateClientUserRequestOut",
        "SetReadyToServeRequestIn": "_authorizedbuyersmarketplace_86_SetReadyToServeRequestIn",
        "SetReadyToServeRequestOut": "_authorizedbuyersmarketplace_87_SetReadyToServeRequestOut",
        "ResumeFinalizedDealRequestIn": "_authorizedbuyersmarketplace_88_ResumeFinalizedDealRequestIn",
        "ResumeFinalizedDealRequestOut": "_authorizedbuyersmarketplace_89_ResumeFinalizedDealRequestOut",
        "DealIn": "_authorizedbuyersmarketplace_90_DealIn",
        "DealOut": "_authorizedbuyersmarketplace_91_DealOut",
        "AddCreativeRequestIn": "_authorizedbuyersmarketplace_92_AddCreativeRequestIn",
        "AddCreativeRequestOut": "_authorizedbuyersmarketplace_93_AddCreativeRequestOut",
        "BatchUpdateDealsRequestIn": "_authorizedbuyersmarketplace_94_BatchUpdateDealsRequestIn",
        "BatchUpdateDealsRequestOut": "_authorizedbuyersmarketplace_95_BatchUpdateDealsRequestOut",
        "TimeZoneIn": "_authorizedbuyersmarketplace_96_TimeZoneIn",
        "TimeZoneOut": "_authorizedbuyersmarketplace_97_TimeZoneOut",
        "MobileApplicationTargetingIn": "_authorizedbuyersmarketplace_98_MobileApplicationTargetingIn",
        "MobileApplicationTargetingOut": "_authorizedbuyersmarketplace_99_MobileApplicationTargetingOut",
        "ListPublisherProfilesResponseIn": "_authorizedbuyersmarketplace_100_ListPublisherProfilesResponseIn",
        "ListPublisherProfilesResponseOut": "_authorizedbuyersmarketplace_101_ListPublisherProfilesResponseOut",
        "UnsubscribeAuctionPackageRequestIn": "_authorizedbuyersmarketplace_102_UnsubscribeAuctionPackageRequestIn",
        "UnsubscribeAuctionPackageRequestOut": "_authorizedbuyersmarketplace_103_UnsubscribeAuctionPackageRequestOut",
        "ActivateClientUserRequestIn": "_authorizedbuyersmarketplace_104_ActivateClientUserRequestIn",
        "ActivateClientUserRequestOut": "_authorizedbuyersmarketplace_105_ActivateClientUserRequestOut",
        "DayPartIn": "_authorizedbuyersmarketplace_106_DayPartIn",
        "DayPartOut": "_authorizedbuyersmarketplace_107_DayPartOut",
        "ActivateClientRequestIn": "_authorizedbuyersmarketplace_108_ActivateClientRequestIn",
        "ActivateClientRequestOut": "_authorizedbuyersmarketplace_109_ActivateClientRequestOut",
        "DealPausingInfoIn": "_authorizedbuyersmarketplace_110_DealPausingInfoIn",
        "DealPausingInfoOut": "_authorizedbuyersmarketplace_111_DealPausingInfoOut",
        "AcceptProposalRequestIn": "_authorizedbuyersmarketplace_112_AcceptProposalRequestIn",
        "AcceptProposalRequestOut": "_authorizedbuyersmarketplace_113_AcceptProposalRequestOut",
        "MarketplaceTargetingIn": "_authorizedbuyersmarketplace_114_MarketplaceTargetingIn",
        "MarketplaceTargetingOut": "_authorizedbuyersmarketplace_115_MarketplaceTargetingOut",
        "SendRfpRequestIn": "_authorizedbuyersmarketplace_116_SendRfpRequestIn",
        "SendRfpRequestOut": "_authorizedbuyersmarketplace_117_SendRfpRequestOut",
        "ListAuctionPackagesResponseIn": "_authorizedbuyersmarketplace_118_ListAuctionPackagesResponseIn",
        "ListAuctionPackagesResponseOut": "_authorizedbuyersmarketplace_119_ListAuctionPackagesResponseOut",
        "DeactivateClientRequestIn": "_authorizedbuyersmarketplace_120_DeactivateClientRequestIn",
        "DeactivateClientRequestOut": "_authorizedbuyersmarketplace_121_DeactivateClientRequestOut",
        "RtbMetricsIn": "_authorizedbuyersmarketplace_122_RtbMetricsIn",
        "RtbMetricsOut": "_authorizedbuyersmarketplace_123_RtbMetricsOut",
        "AdSizeIn": "_authorizedbuyersmarketplace_124_AdSizeIn",
        "AdSizeOut": "_authorizedbuyersmarketplace_125_AdSizeOut",
        "ClientUserIn": "_authorizedbuyersmarketplace_126_ClientUserIn",
        "ClientUserOut": "_authorizedbuyersmarketplace_127_ClientUserOut",
        "ListClientUsersResponseIn": "_authorizedbuyersmarketplace_128_ListClientUsersResponseIn",
        "ListClientUsersResponseOut": "_authorizedbuyersmarketplace_129_ListClientUsersResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["PlacementTargetingIn"] = t.struct(
        {
            "uriTargeting": t.proxy(renames["UriTargetingIn"]).optional(),
            "mobileApplicationTargeting": t.proxy(
                renames["MobileApplicationTargetingIn"]
            ).optional(),
        }
    ).named(renames["PlacementTargetingIn"])
    types["PlacementTargetingOut"] = t.struct(
        {
            "uriTargeting": t.proxy(renames["UriTargetingOut"]).optional(),
            "mobileApplicationTargeting": t.proxy(
                renames["MobileApplicationTargetingOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlacementTargetingOut"])
    types["ProposalIn"] = t.struct(
        {
            "buyerContacts": t.array(t.proxy(renames["ContactIn"])).optional(),
            "pausingConsented": t.boolean().optional(),
            "buyerPrivateData": t.proxy(renames["PrivateDataIn"]).optional(),
            "notes": t.array(t.proxy(renames["NoteIn"])).optional(),
            "publisherProfile": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ProposalIn"])
    types["ProposalOut"] = t.struct(
        {
            "buyerContacts": t.array(t.proxy(renames["ContactOut"])).optional(),
            "buyer": t.string().optional(),
            "billedBuyer": t.string().optional(),
            "dealType": t.string().optional(),
            "state": t.string().optional(),
            "termsAndConditions": t.string().optional(),
            "pausingConsented": t.boolean().optional(),
            "buyerPrivateData": t.proxy(renames["PrivateDataOut"]).optional(),
            "displayName": t.string().optional(),
            "notes": t.array(t.proxy(renames["NoteOut"])).optional(),
            "client": t.string().optional(),
            "proposalRevision": t.string().optional(),
            "isRenegotiating": t.boolean().optional(),
            "publisherProfile": t.string().optional(),
            "lastUpdaterOrCommentorRole": t.string().optional(),
            "updateTime": t.string().optional(),
            "sellerContacts": t.array(t.proxy(renames["ContactOut"])).optional(),
            "name": t.string().optional(),
            "originatorRole": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProposalOut"])
    types["UnsubscribeClientsRequestIn"] = t.struct(
        {"clients": t.array(t.string()).optional()}
    ).named(renames["UnsubscribeClientsRequestIn"])
    types["UnsubscribeClientsRequestOut"] = t.struct(
        {
            "clients": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UnsubscribeClientsRequestOut"])
    types["MoneyIn"] = t.struct(
        {
            "currencyCode": t.string().optional(),
            "units": t.string().optional(),
            "nanos": t.integer().optional(),
        }
    ).named(renames["MoneyIn"])
    types["MoneyOut"] = t.struct(
        {
            "currencyCode": t.string().optional(),
            "units": t.string().optional(),
            "nanos": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoneyOut"])
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
    types["TimeOfDayIn"] = t.struct(
        {
            "minutes": t.integer().optional(),
            "hours": t.integer().optional(),
            "nanos": t.integer().optional(),
            "seconds": t.integer().optional(),
        }
    ).named(renames["TimeOfDayIn"])
    types["TimeOfDayOut"] = t.struct(
        {
            "minutes": t.integer().optional(),
            "hours": t.integer().optional(),
            "nanos": t.integer().optional(),
            "seconds": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeOfDayOut"])
    types["BatchUpdateDealsResponseIn"] = t.struct(
        {"deals": t.array(t.proxy(renames["DealIn"])).optional()}
    ).named(renames["BatchUpdateDealsResponseIn"])
    types["BatchUpdateDealsResponseOut"] = t.struct(
        {
            "deals": t.array(t.proxy(renames["DealOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateDealsResponseOut"])
    types["SubscribeClientsRequestIn"] = t.struct(
        {"clients": t.array(t.string()).optional()}
    ).named(renames["SubscribeClientsRequestIn"])
    types["SubscribeClientsRequestOut"] = t.struct(
        {
            "clients": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscribeClientsRequestOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["NoteIn"] = t.struct({"note": t.string().optional()}).named(renames["NoteIn"])
    types["NoteOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "creatorRole": t.string().optional(),
            "note": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NoteOut"])
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
    types["DeliveryControlIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeliveryControlIn"]
    )
    types["DeliveryControlOut"] = t.struct(
        {
            "deliveryRateType": t.string().optional(),
            "companionDeliveryType": t.string().optional(),
            "roadblockingType": t.string().optional(),
            "frequencyCap": t.array(t.proxy(renames["FrequencyCapOut"])).optional(),
            "creativeRotationType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeliveryControlOut"])
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
    types["ProgrammaticGuaranteedTermsIn"] = t.struct(
        {
            "reservationType": t.string().optional(),
            "impressionCap": t.string().optional(),
            "fixedPrice": t.proxy(renames["PriceIn"]).optional(),
            "minimumDailyLooks": t.string().optional(),
            "guaranteedLooks": t.string().optional(),
            "percentShareOfVoice": t.string().optional(),
        }
    ).named(renames["ProgrammaticGuaranteedTermsIn"])
    types["ProgrammaticGuaranteedTermsOut"] = t.struct(
        {
            "reservationType": t.string().optional(),
            "impressionCap": t.string().optional(),
            "fixedPrice": t.proxy(renames["PriceOut"]).optional(),
            "minimumDailyLooks": t.string().optional(),
            "guaranteedLooks": t.string().optional(),
            "percentShareOfVoice": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProgrammaticGuaranteedTermsOut"])
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
    types["PrivateDataIn"] = t.struct({"referenceId": t.string().optional()}).named(
        renames["PrivateDataIn"]
    )
    types["PrivateDataOut"] = t.struct(
        {
            "referenceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrivateDataOut"])
    types["InventoryTypeTargetingIn"] = t.struct(
        {"inventoryTypes": t.array(t.string()).optional()}
    ).named(renames["InventoryTypeTargetingIn"])
    types["InventoryTypeTargetingOut"] = t.struct(
        {
            "inventoryTypes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InventoryTypeTargetingOut"])
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
    types["ClientIn"] = t.struct(
        {
            "displayName": t.string(),
            "partnerClientId": t.string().optional(),
            "role": t.string(),
            "sellerVisible": t.boolean().optional(),
        }
    ).named(renames["ClientIn"])
    types["ClientOut"] = t.struct(
        {
            "displayName": t.string(),
            "partnerClientId": t.string().optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "role": t.string(),
            "sellerVisible": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientOut"])
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
    types["ListDealsResponseIn"] = t.struct(
        {
            "deals": t.array(t.proxy(renames["DealIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListDealsResponseIn"])
    types["ListDealsResponseOut"] = t.struct(
        {
            "deals": t.array(t.proxy(renames["DealOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDealsResponseOut"])
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
    types["FinalizedDealIn"] = t.struct(
        {
            "dealPausingInfo": t.proxy(renames["DealPausingInfoIn"]).optional(),
            "readyToServe": t.boolean().optional(),
            "rtbMetrics": t.proxy(renames["RtbMetricsIn"]).optional(),
            "name": t.string().optional(),
            "dealServingStatus": t.string().optional(),
            "deal": t.proxy(renames["DealIn"]).optional(),
        }
    ).named(renames["FinalizedDealIn"])
    types["FinalizedDealOut"] = t.struct(
        {
            "dealPausingInfo": t.proxy(renames["DealPausingInfoOut"]).optional(),
            "readyToServe": t.boolean().optional(),
            "rtbMetrics": t.proxy(renames["RtbMetricsOut"]).optional(),
            "name": t.string().optional(),
            "dealServingStatus": t.string().optional(),
            "deal": t.proxy(renames["DealOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FinalizedDealOut"])
    types["AuctionPackageIn"] = t.struct(
        {"name": t.string().optional(), "displayName": t.string().optional()}
    ).named(renames["AuctionPackageIn"])
    types["AuctionPackageOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "subscribedClients": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "creator": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuctionPackageOut"])
    types["SubscribeAuctionPackageRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["SubscribeAuctionPackageRequestIn"])
    types["SubscribeAuctionPackageRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SubscribeAuctionPackageRequestOut"])
    types["AddNoteRequestIn"] = t.struct(
        {"note": t.proxy(renames["NoteIn"]).optional()}
    ).named(renames["AddNoteRequestIn"])
    types["AddNoteRequestOut"] = t.struct(
        {
            "note": t.proxy(renames["NoteOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddNoteRequestOut"])
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
    types["CancelNegotiationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelNegotiationRequestIn"]
    )
    types["CancelNegotiationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelNegotiationRequestOut"])
    types["CreativeRequirementsIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CreativeRequirementsIn"]
    )
    types["CreativeRequirementsOut"] = t.struct(
        {
            "creativePreApprovalPolicy": t.string().optional(),
            "programmaticCreativeSource": t.string().optional(),
            "creativeSafeFrameCompatibility": t.string().optional(),
            "skippableAdType": t.string().optional(),
            "maxAdDurationMs": t.string().optional(),
            "creativeFormat": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeRequirementsOut"])
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
    types["PublisherProfileIn"] = t.struct(
        {
            "name": t.string().optional(),
            "logoUrl": t.string().optional(),
            "publisherCode": t.string().optional(),
            "directDealsContact": t.string().optional(),
            "programmaticDealsContact": t.string().optional(),
            "mobileApps": t.array(
                t.proxy(renames["PublisherProfileMobileApplicationIn"])
            ).optional(),
            "domains": t.array(t.string()).optional(),
            "pitchStatement": t.string().optional(),
            "displayName": t.string().optional(),
            "mediaKitUrl": t.string().optional(),
            "topHeadlines": t.array(t.string()).optional(),
            "overview": t.string().optional(),
            "isParent": t.boolean().optional(),
            "audienceDescription": t.string().optional(),
            "samplePageUrl": t.string().optional(),
        }
    ).named(renames["PublisherProfileIn"])
    types["PublisherProfileOut"] = t.struct(
        {
            "name": t.string().optional(),
            "logoUrl": t.string().optional(),
            "publisherCode": t.string().optional(),
            "directDealsContact": t.string().optional(),
            "programmaticDealsContact": t.string().optional(),
            "mobileApps": t.array(
                t.proxy(renames["PublisherProfileMobileApplicationOut"])
            ).optional(),
            "domains": t.array(t.string()).optional(),
            "pitchStatement": t.string().optional(),
            "displayName": t.string().optional(),
            "mediaKitUrl": t.string().optional(),
            "topHeadlines": t.array(t.string()).optional(),
            "overview": t.string().optional(),
            "isParent": t.boolean().optional(),
            "audienceDescription": t.string().optional(),
            "samplePageUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublisherProfileOut"])
    types["DeactivateClientUserRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DeactivateClientUserRequestIn"])
    types["DeactivateClientUserRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeactivateClientUserRequestOut"])
    types["SetReadyToServeRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["SetReadyToServeRequestIn"]
    )
    types["SetReadyToServeRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SetReadyToServeRequestOut"])
    types["ResumeFinalizedDealRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ResumeFinalizedDealRequestIn"])
    types["ResumeFinalizedDealRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ResumeFinalizedDealRequestOut"])
    types["DealIn"] = t.struct(
        {
            "privateAuctionTerms": t.proxy(renames["PrivateAuctionTermsIn"]).optional(),
            "flightEndTime": t.string().optional(),
            "preferredDealTerms": t.proxy(renames["PreferredDealTermsIn"]).optional(),
            "flightStartTime": t.string().optional(),
            "name": t.string().optional(),
            "programmaticGuaranteedTerms": t.proxy(
                renames["ProgrammaticGuaranteedTermsIn"]
            ).optional(),
            "targeting": t.proxy(renames["MarketplaceTargetingIn"]).optional(),
            "publisherProfile": t.string().optional(),
            "estimatedGrossSpend": t.proxy(renames["MoneyIn"]).optional(),
        }
    ).named(renames["DealIn"])
    types["DealOut"] = t.struct(
        {
            "description": t.string().optional(),
            "privateAuctionTerms": t.proxy(
                renames["PrivateAuctionTermsOut"]
            ).optional(),
            "client": t.string().optional(),
            "deliveryControl": t.proxy(renames["DeliveryControlOut"]).optional(),
            "flightEndTime": t.string().optional(),
            "preferredDealTerms": t.proxy(renames["PreferredDealTermsOut"]).optional(),
            "displayName": t.string().optional(),
            "createTime": t.string().optional(),
            "flightStartTime": t.string().optional(),
            "billedBuyer": t.string().optional(),
            "sellerTimeZone": t.proxy(renames["TimeZoneOut"]).optional(),
            "creativeRequirements": t.proxy(
                renames["CreativeRequirementsOut"]
            ).optional(),
            "buyer": t.string().optional(),
            "name": t.string().optional(),
            "programmaticGuaranteedTerms": t.proxy(
                renames["ProgrammaticGuaranteedTermsOut"]
            ).optional(),
            "targeting": t.proxy(renames["MarketplaceTargetingOut"]).optional(),
            "dealType": t.string().optional(),
            "publisherProfile": t.string().optional(),
            "proposalRevision": t.string().optional(),
            "estimatedGrossSpend": t.proxy(renames["MoneyOut"]).optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DealOut"])
    types["AddCreativeRequestIn"] = t.struct({"creative": t.string().optional()}).named(
        renames["AddCreativeRequestIn"]
    )
    types["AddCreativeRequestOut"] = t.struct(
        {
            "creative": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddCreativeRequestOut"])
    types["BatchUpdateDealsRequestIn"] = t.struct(
        {"requests": t.array(t.proxy(renames["UpdateDealRequestIn"]))}
    ).named(renames["BatchUpdateDealsRequestIn"])
    types["BatchUpdateDealsRequestOut"] = t.struct(
        {
            "requests": t.array(t.proxy(renames["UpdateDealRequestOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateDealsRequestOut"])
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
    types["UnsubscribeAuctionPackageRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["UnsubscribeAuctionPackageRequestIn"])
    types["UnsubscribeAuctionPackageRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UnsubscribeAuctionPackageRequestOut"])
    types["ActivateClientUserRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ActivateClientUserRequestIn"]
    )
    types["ActivateClientUserRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ActivateClientUserRequestOut"])
    types["DayPartIn"] = t.struct(
        {
            "endTime": t.proxy(renames["TimeOfDayIn"]).optional(),
            "startTime": t.proxy(renames["TimeOfDayIn"]).optional(),
            "dayOfWeek": t.string().optional(),
        }
    ).named(renames["DayPartIn"])
    types["DayPartOut"] = t.struct(
        {
            "endTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "startTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "dayOfWeek": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DayPartOut"])
    types["ActivateClientRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ActivateClientRequestIn"]
    )
    types["ActivateClientRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ActivateClientRequestOut"])
    types["DealPausingInfoIn"] = t.struct(
        {
            "pauseReason": t.string().optional(),
            "pauseRole": t.string().optional(),
            "pausingConsented": t.boolean().optional(),
        }
    ).named(renames["DealPausingInfoIn"])
    types["DealPausingInfoOut"] = t.struct(
        {
            "pauseReason": t.string().optional(),
            "pauseRole": t.string().optional(),
            "pausingConsented": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DealPausingInfoOut"])
    types["AcceptProposalRequestIn"] = t.struct(
        {"proposalRevision": t.string().optional()}
    ).named(renames["AcceptProposalRequestIn"])
    types["AcceptProposalRequestOut"] = t.struct(
        {
            "proposalRevision": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AcceptProposalRequestOut"])
    types["MarketplaceTargetingIn"] = t.struct(
        {
            "daypartTargeting": t.proxy(renames["DayPartTargetingIn"]).optional(),
            "userListTargeting": t.proxy(renames["CriteriaTargetingIn"]).optional(),
        }
    ).named(renames["MarketplaceTargetingIn"])
    types["MarketplaceTargetingOut"] = t.struct(
        {
            "daypartTargeting": t.proxy(renames["DayPartTargetingOut"]).optional(),
            "placementTargeting": t.proxy(renames["PlacementTargetingOut"]).optional(),
            "videoTargeting": t.proxy(renames["VideoTargetingOut"]).optional(),
            "geoTargeting": t.proxy(renames["CriteriaTargetingOut"]).optional(),
            "userListTargeting": t.proxy(renames["CriteriaTargetingOut"]).optional(),
            "inventorySizeTargeting": t.proxy(
                renames["InventorySizeTargetingOut"]
            ).optional(),
            "technologyTargeting": t.proxy(
                renames["TechnologyTargetingOut"]
            ).optional(),
            "inventoryTypeTargeting": t.proxy(
                renames["InventoryTypeTargetingOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MarketplaceTargetingOut"])
    types["SendRfpRequestIn"] = t.struct(
        {
            "flightEndTime": t.string(),
            "geoTargeting": t.proxy(renames["CriteriaTargetingIn"]).optional(),
            "inventorySizeTargeting": t.proxy(
                renames["InventorySizeTargetingIn"]
            ).optional(),
            "client": t.string().optional(),
            "publisherProfile": t.string(),
            "displayName": t.string(),
            "flightStartTime": t.string(),
            "note": t.string().optional(),
            "buyerContacts": t.array(t.proxy(renames["ContactIn"])).optional(),
            "preferredDealTerms": t.proxy(renames["PreferredDealTermsIn"]).optional(),
            "estimatedGrossSpend": t.proxy(renames["MoneyIn"]).optional(),
            "programmaticGuaranteedTerms": t.proxy(
                renames["ProgrammaticGuaranteedTermsIn"]
            ).optional(),
        }
    ).named(renames["SendRfpRequestIn"])
    types["SendRfpRequestOut"] = t.struct(
        {
            "flightEndTime": t.string(),
            "geoTargeting": t.proxy(renames["CriteriaTargetingOut"]).optional(),
            "inventorySizeTargeting": t.proxy(
                renames["InventorySizeTargetingOut"]
            ).optional(),
            "client": t.string().optional(),
            "publisherProfile": t.string(),
            "displayName": t.string(),
            "flightStartTime": t.string(),
            "note": t.string().optional(),
            "buyerContacts": t.array(t.proxy(renames["ContactOut"])).optional(),
            "preferredDealTerms": t.proxy(renames["PreferredDealTermsOut"]).optional(),
            "estimatedGrossSpend": t.proxy(renames["MoneyOut"]).optional(),
            "programmaticGuaranteedTerms": t.proxy(
                renames["ProgrammaticGuaranteedTermsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SendRfpRequestOut"])
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
    types["DeactivateClientRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeactivateClientRequestIn"]
    )
    types["DeactivateClientRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeactivateClientRequestOut"])
    types["RtbMetricsIn"] = t.struct(
        {
            "bids7Days": t.string().optional(),
            "bidRate7Days": t.number().optional(),
            "filteredBidRate7Days": t.number().optional(),
            "bidRequests7Days": t.string().optional(),
            "adImpressions7Days": t.string().optional(),
            "mustBidRateCurrentMonth": t.number().optional(),
        }
    ).named(renames["RtbMetricsIn"])
    types["RtbMetricsOut"] = t.struct(
        {
            "bids7Days": t.string().optional(),
            "bidRate7Days": t.number().optional(),
            "filteredBidRate7Days": t.number().optional(),
            "bidRequests7Days": t.string().optional(),
            "adImpressions7Days": t.string().optional(),
            "mustBidRateCurrentMonth": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RtbMetricsOut"])
    types["AdSizeIn"] = t.struct(
        {
            "height": t.string().optional(),
            "type": t.string().optional(),
            "width": t.string().optional(),
        }
    ).named(renames["AdSizeIn"])
    types["AdSizeOut"] = t.struct(
        {
            "height": t.string().optional(),
            "type": t.string().optional(),
            "width": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdSizeOut"])
    types["ClientUserIn"] = t.struct({"email": t.string()}).named(
        renames["ClientUserIn"]
    )
    types["ClientUserOut"] = t.struct(
        {
            "state": t.string().optional(),
            "email": t.string(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientUserOut"])
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

    functions = {}
    functions["buyersClientsCreate"] = authorizedbuyersmarketplace.get(
        "v1/{parent}/clients",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListClientsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersClientsActivate"] = authorizedbuyersmarketplace.get(
        "v1/{parent}/clients",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListClientsResponseOut"]),
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
    functions["buyersProposalsGet"] = authorizedbuyersmarketplace.post(
        "v1/{proposal}:cancelNegotiation",
        t.struct(
            {
                "proposal": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProposalOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersProposalsPatch"] = authorizedbuyersmarketplace.post(
        "v1/{proposal}:cancelNegotiation",
        t.struct(
            {
                "proposal": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProposalOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersProposalsList"] = authorizedbuyersmarketplace.post(
        "v1/{proposal}:cancelNegotiation",
        t.struct(
            {
                "proposal": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProposalOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersProposalsSendRfp"] = authorizedbuyersmarketplace.post(
        "v1/{proposal}:cancelNegotiation",
        t.struct(
            {
                "proposal": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProposalOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersProposalsAddNote"] = authorizedbuyersmarketplace.post(
        "v1/{proposal}:cancelNegotiation",
        t.struct(
            {
                "proposal": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProposalOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersProposalsAccept"] = authorizedbuyersmarketplace.post(
        "v1/{proposal}:cancelNegotiation",
        t.struct(
            {
                "proposal": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProposalOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersProposalsCancelNegotiation"] = authorizedbuyersmarketplace.post(
        "v1/{proposal}:cancelNegotiation",
        t.struct(
            {
                "proposal": t.string().optional(),
                "_": t.string().optional(),
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
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "privateAuctionTerms": t.proxy(
                    renames["PrivateAuctionTermsIn"]
                ).optional(),
                "flightEndTime": t.string().optional(),
                "preferredDealTerms": t.proxy(
                    renames["PreferredDealTermsIn"]
                ).optional(),
                "flightStartTime": t.string().optional(),
                "programmaticGuaranteedTerms": t.proxy(
                    renames["ProgrammaticGuaranteedTermsIn"]
                ).optional(),
                "targeting": t.proxy(renames["MarketplaceTargetingIn"]).optional(),
                "publisherProfile": t.string().optional(),
                "estimatedGrossSpend": t.proxy(renames["MoneyIn"]).optional(),
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
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "privateAuctionTerms": t.proxy(
                    renames["PrivateAuctionTermsIn"]
                ).optional(),
                "flightEndTime": t.string().optional(),
                "preferredDealTerms": t.proxy(
                    renames["PreferredDealTermsIn"]
                ).optional(),
                "flightStartTime": t.string().optional(),
                "programmaticGuaranteedTerms": t.proxy(
                    renames["ProgrammaticGuaranteedTermsIn"]
                ).optional(),
                "targeting": t.proxy(renames["MarketplaceTargetingIn"]).optional(),
                "publisherProfile": t.string().optional(),
                "estimatedGrossSpend": t.proxy(renames["MoneyIn"]).optional(),
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
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "privateAuctionTerms": t.proxy(
                    renames["PrivateAuctionTermsIn"]
                ).optional(),
                "flightEndTime": t.string().optional(),
                "preferredDealTerms": t.proxy(
                    renames["PreferredDealTermsIn"]
                ).optional(),
                "flightStartTime": t.string().optional(),
                "programmaticGuaranteedTerms": t.proxy(
                    renames["ProgrammaticGuaranteedTermsIn"]
                ).optional(),
                "targeting": t.proxy(renames["MarketplaceTargetingIn"]).optional(),
                "publisherProfile": t.string().optional(),
                "estimatedGrossSpend": t.proxy(renames["MoneyIn"]).optional(),
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
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "privateAuctionTerms": t.proxy(
                    renames["PrivateAuctionTermsIn"]
                ).optional(),
                "flightEndTime": t.string().optional(),
                "preferredDealTerms": t.proxy(
                    renames["PreferredDealTermsIn"]
                ).optional(),
                "flightStartTime": t.string().optional(),
                "programmaticGuaranteedTerms": t.proxy(
                    renames["ProgrammaticGuaranteedTermsIn"]
                ).optional(),
                "targeting": t.proxy(renames["MarketplaceTargetingIn"]).optional(),
                "publisherProfile": t.string().optional(),
                "estimatedGrossSpend": t.proxy(renames["MoneyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DealOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersAuctionPackagesGet"] = authorizedbuyersmarketplace.post(
        "v1/{name}:subscribe",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
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
        "v1/{name}:subscribe",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AuctionPackageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersAuctionPackagesList"] = authorizedbuyersmarketplace.post(
        "v1/{name}:subscribe",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
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
        "v1/{name}:subscribe",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AuctionPackageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersAuctionPackagesUnsubscribe"] = authorizedbuyersmarketplace.post(
        "v1/{name}:subscribe",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AuctionPackageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersAuctionPackagesSubscribe"] = authorizedbuyersmarketplace.post(
        "v1/{name}:subscribe",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
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
    functions["buyersFinalizedDealsPause"] = authorizedbuyersmarketplace.post(
        "v1/{name}:resume",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FinalizedDealOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersFinalizedDealsSetReadyToServe"] = authorizedbuyersmarketplace.post(
        "v1/{name}:resume",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FinalizedDealOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersFinalizedDealsGet"] = authorizedbuyersmarketplace.post(
        "v1/{name}:resume",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FinalizedDealOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersFinalizedDealsList"] = authorizedbuyersmarketplace.post(
        "v1/{name}:resume",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FinalizedDealOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersFinalizedDealsAddCreative"] = authorizedbuyersmarketplace.post(
        "v1/{name}:resume",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FinalizedDealOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersFinalizedDealsResume"] = authorizedbuyersmarketplace.post(
        "v1/{name}:resume",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FinalizedDealOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersFinalizedDealsList"] = authorizedbuyersmarketplace.get(
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

    return Import(
        importer="authorizedbuyersmarketplace",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
