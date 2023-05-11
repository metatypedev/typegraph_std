from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_realtimebidding() -> Import:
    realtimebidding = HTTPRuntime("https://realtimebidding.googleapis.com/")

    renames = {
        "ErrorResponse": "_realtimebidding_1_ErrorResponse",
        "UrlRestrictionIn": "_realtimebidding_2_UrlRestrictionIn",
        "UrlRestrictionOut": "_realtimebidding_3_UrlRestrictionOut",
        "EmptyIn": "_realtimebidding_4_EmptyIn",
        "EmptyOut": "_realtimebidding_5_EmptyOut",
        "PublisherConnectionIn": "_realtimebidding_6_PublisherConnectionIn",
        "PublisherConnectionOut": "_realtimebidding_7_PublisherConnectionOut",
        "HttpCookieEvidenceIn": "_realtimebidding_8_HttpCookieEvidenceIn",
        "HttpCookieEvidenceOut": "_realtimebidding_9_HttpCookieEvidenceOut",
        "DomainCallEvidenceIn": "_realtimebidding_10_DomainCallEvidenceIn",
        "DomainCallEvidenceOut": "_realtimebidding_11_DomainCallEvidenceOut",
        "DateIn": "_realtimebidding_12_DateIn",
        "DateOut": "_realtimebidding_13_DateOut",
        "AdTechnologyProvidersIn": "_realtimebidding_14_AdTechnologyProvidersIn",
        "AdTechnologyProvidersOut": "_realtimebidding_15_AdTechnologyProvidersOut",
        "CloseUserListRequestIn": "_realtimebidding_16_CloseUserListRequestIn",
        "CloseUserListRequestOut": "_realtimebidding_17_CloseUserListRequestOut",
        "PretargetingConfigIn": "_realtimebidding_18_PretargetingConfigIn",
        "PretargetingConfigOut": "_realtimebidding_19_PretargetingConfigOut",
        "SuspendPretargetingConfigRequestIn": "_realtimebidding_20_SuspendPretargetingConfigRequestIn",
        "SuspendPretargetingConfigRequestOut": "_realtimebidding_21_SuspendPretargetingConfigRequestOut",
        "BatchApprovePublisherConnectionsRequestIn": "_realtimebidding_22_BatchApprovePublisherConnectionsRequestIn",
        "BatchApprovePublisherConnectionsRequestOut": "_realtimebidding_23_BatchApprovePublisherConnectionsRequestOut",
        "BidderIn": "_realtimebidding_24_BidderIn",
        "BidderOut": "_realtimebidding_25_BidderOut",
        "NumericTargetingDimensionIn": "_realtimebidding_26_NumericTargetingDimensionIn",
        "NumericTargetingDimensionOut": "_realtimebidding_27_NumericTargetingDimensionOut",
        "GetRemarketingTagResponseIn": "_realtimebidding_28_GetRemarketingTagResponseIn",
        "GetRemarketingTagResponseOut": "_realtimebidding_29_GetRemarketingTagResponseOut",
        "DestinationUrlEvidenceIn": "_realtimebidding_30_DestinationUrlEvidenceIn",
        "DestinationUrlEvidenceOut": "_realtimebidding_31_DestinationUrlEvidenceOut",
        "NativeContentIn": "_realtimebidding_32_NativeContentIn",
        "NativeContentOut": "_realtimebidding_33_NativeContentOut",
        "AddTargetedAppsRequestIn": "_realtimebidding_34_AddTargetedAppsRequestIn",
        "AddTargetedAppsRequestOut": "_realtimebidding_35_AddTargetedAppsRequestOut",
        "VideoContentIn": "_realtimebidding_36_VideoContentIn",
        "VideoContentOut": "_realtimebidding_37_VideoContentOut",
        "CreativeServingDecisionIn": "_realtimebidding_38_CreativeServingDecisionIn",
        "CreativeServingDecisionOut": "_realtimebidding_39_CreativeServingDecisionOut",
        "OpenUserListRequestIn": "_realtimebidding_40_OpenUserListRequestIn",
        "OpenUserListRequestOut": "_realtimebidding_41_OpenUserListRequestOut",
        "UserListIn": "_realtimebidding_42_UserListIn",
        "UserListOut": "_realtimebidding_43_UserListOut",
        "ListUserListsResponseIn": "_realtimebidding_44_ListUserListsResponseIn",
        "ListUserListsResponseOut": "_realtimebidding_45_ListUserListsResponseOut",
        "RemoveTargetedPublishersRequestIn": "_realtimebidding_46_RemoveTargetedPublishersRequestIn",
        "RemoveTargetedPublishersRequestOut": "_realtimebidding_47_RemoveTargetedPublishersRequestOut",
        "BatchRejectPublisherConnectionsResponseIn": "_realtimebidding_48_BatchRejectPublisherConnectionsResponseIn",
        "BatchRejectPublisherConnectionsResponseOut": "_realtimebidding_49_BatchRejectPublisherConnectionsResponseOut",
        "BatchApprovePublisherConnectionsResponseIn": "_realtimebidding_50_BatchApprovePublisherConnectionsResponseIn",
        "BatchApprovePublisherConnectionsResponseOut": "_realtimebidding_51_BatchApprovePublisherConnectionsResponseOut",
        "VideoMetadataIn": "_realtimebidding_52_VideoMetadataIn",
        "VideoMetadataOut": "_realtimebidding_53_VideoMetadataOut",
        "DestinationNotCrawlableEvidenceIn": "_realtimebidding_54_DestinationNotCrawlableEvidenceIn",
        "DestinationNotCrawlableEvidenceOut": "_realtimebidding_55_DestinationNotCrawlableEvidenceOut",
        "ListBiddersResponseIn": "_realtimebidding_56_ListBiddersResponseIn",
        "ListBiddersResponseOut": "_realtimebidding_57_ListBiddersResponseOut",
        "PolicyTopicEntryIn": "_realtimebidding_58_PolicyTopicEntryIn",
        "PolicyTopicEntryOut": "_realtimebidding_59_PolicyTopicEntryOut",
        "AdvertiserAndBrandIn": "_realtimebidding_60_AdvertiserAndBrandIn",
        "AdvertiserAndBrandOut": "_realtimebidding_61_AdvertiserAndBrandOut",
        "PolicyTopicEvidenceIn": "_realtimebidding_62_PolicyTopicEvidenceIn",
        "PolicyTopicEvidenceOut": "_realtimebidding_63_PolicyTopicEvidenceOut",
        "EndpointIn": "_realtimebidding_64_EndpointIn",
        "EndpointOut": "_realtimebidding_65_EndpointOut",
        "ImageIn": "_realtimebidding_66_ImageIn",
        "ImageOut": "_realtimebidding_67_ImageOut",
        "ListCreativesResponseIn": "_realtimebidding_68_ListCreativesResponseIn",
        "ListCreativesResponseOut": "_realtimebidding_69_ListCreativesResponseOut",
        "DomainCallsIn": "_realtimebidding_70_DomainCallsIn",
        "DomainCallsOut": "_realtimebidding_71_DomainCallsOut",
        "ActivatePretargetingConfigRequestIn": "_realtimebidding_72_ActivatePretargetingConfigRequestIn",
        "ActivatePretargetingConfigRequestOut": "_realtimebidding_73_ActivatePretargetingConfigRequestOut",
        "ListEndpointsResponseIn": "_realtimebidding_74_ListEndpointsResponseIn",
        "ListEndpointsResponseOut": "_realtimebidding_75_ListEndpointsResponseOut",
        "DownloadSizeEvidenceIn": "_realtimebidding_76_DownloadSizeEvidenceIn",
        "DownloadSizeEvidenceOut": "_realtimebidding_77_DownloadSizeEvidenceOut",
        "AddTargetedSitesRequestIn": "_realtimebidding_78_AddTargetedSitesRequestIn",
        "AddTargetedSitesRequestOut": "_realtimebidding_79_AddTargetedSitesRequestOut",
        "PolicyComplianceIn": "_realtimebidding_80_PolicyComplianceIn",
        "PolicyComplianceOut": "_realtimebidding_81_PolicyComplianceOut",
        "RemoveTargetedSitesRequestIn": "_realtimebidding_82_RemoveTargetedSitesRequestIn",
        "RemoveTargetedSitesRequestOut": "_realtimebidding_83_RemoveTargetedSitesRequestOut",
        "WatchCreativesResponseIn": "_realtimebidding_84_WatchCreativesResponseIn",
        "WatchCreativesResponseOut": "_realtimebidding_85_WatchCreativesResponseOut",
        "BuyerIn": "_realtimebidding_86_BuyerIn",
        "BuyerOut": "_realtimebidding_87_BuyerOut",
        "CreativeDimensionsIn": "_realtimebidding_88_CreativeDimensionsIn",
        "CreativeDimensionsOut": "_realtimebidding_89_CreativeDimensionsOut",
        "HtmlContentIn": "_realtimebidding_90_HtmlContentIn",
        "HtmlContentOut": "_realtimebidding_91_HtmlContentOut",
        "ListBuyersResponseIn": "_realtimebidding_92_ListBuyersResponseIn",
        "ListBuyersResponseOut": "_realtimebidding_93_ListBuyersResponseOut",
        "MediaFileIn": "_realtimebidding_94_MediaFileIn",
        "MediaFileOut": "_realtimebidding_95_MediaFileOut",
        "DestinationNotWorkingEvidenceIn": "_realtimebidding_96_DestinationNotWorkingEvidenceIn",
        "DestinationNotWorkingEvidenceOut": "_realtimebidding_97_DestinationNotWorkingEvidenceOut",
        "ListPretargetingConfigsResponseIn": "_realtimebidding_98_ListPretargetingConfigsResponseIn",
        "ListPretargetingConfigsResponseOut": "_realtimebidding_99_ListPretargetingConfigsResponseOut",
        "HttpCallEvidenceIn": "_realtimebidding_100_HttpCallEvidenceIn",
        "HttpCallEvidenceOut": "_realtimebidding_101_HttpCallEvidenceOut",
        "RemoveTargetedAppsRequestIn": "_realtimebidding_102_RemoveTargetedAppsRequestIn",
        "RemoveTargetedAppsRequestOut": "_realtimebidding_103_RemoveTargetedAppsRequestOut",
        "WatchCreativesRequestIn": "_realtimebidding_104_WatchCreativesRequestIn",
        "WatchCreativesRequestOut": "_realtimebidding_105_WatchCreativesRequestOut",
        "UrlDownloadSizeIn": "_realtimebidding_106_UrlDownloadSizeIn",
        "UrlDownloadSizeOut": "_realtimebidding_107_UrlDownloadSizeOut",
        "ListPublisherConnectionsResponseIn": "_realtimebidding_108_ListPublisherConnectionsResponseIn",
        "ListPublisherConnectionsResponseOut": "_realtimebidding_109_ListPublisherConnectionsResponseOut",
        "AppTargetingIn": "_realtimebidding_110_AppTargetingIn",
        "AppTargetingOut": "_realtimebidding_111_AppTargetingOut",
        "StringTargetingDimensionIn": "_realtimebidding_112_StringTargetingDimensionIn",
        "StringTargetingDimensionOut": "_realtimebidding_113_StringTargetingDimensionOut",
        "CreativeIn": "_realtimebidding_114_CreativeIn",
        "CreativeOut": "_realtimebidding_115_CreativeOut",
        "AddTargetedPublishersRequestIn": "_realtimebidding_116_AddTargetedPublishersRequestIn",
        "AddTargetedPublishersRequestOut": "_realtimebidding_117_AddTargetedPublishersRequestOut",
        "BatchRejectPublisherConnectionsRequestIn": "_realtimebidding_118_BatchRejectPublisherConnectionsRequestIn",
        "BatchRejectPublisherConnectionsRequestOut": "_realtimebidding_119_BatchRejectPublisherConnectionsRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["UrlRestrictionIn"] = t.struct(
        {
            "endDate": t.proxy(renames["DateIn"]).optional(),
            "startDate": t.proxy(renames["DateIn"]).optional(),
            "url": t.string(),
            "restrictionType": t.string().optional(),
        }
    ).named(renames["UrlRestrictionIn"])
    types["UrlRestrictionOut"] = t.struct(
        {
            "endDate": t.proxy(renames["DateOut"]).optional(),
            "startDate": t.proxy(renames["DateOut"]).optional(),
            "url": t.string(),
            "restrictionType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UrlRestrictionOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["PublisherConnectionIn"] = t.struct(
        {"biddingState": t.string().optional()}
    ).named(renames["PublisherConnectionIn"])
    types["PublisherConnectionOut"] = t.struct(
        {
            "biddingState": t.string().optional(),
            "publisherPlatform": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublisherConnectionOut"])
    types["HttpCookieEvidenceIn"] = t.struct(
        {
            "maxCookieCount": t.integer().optional(),
            "cookieNames": t.array(t.string()).optional(),
        }
    ).named(renames["HttpCookieEvidenceIn"])
    types["HttpCookieEvidenceOut"] = t.struct(
        {
            "maxCookieCount": t.integer().optional(),
            "cookieNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpCookieEvidenceOut"])
    types["DomainCallEvidenceIn"] = t.struct(
        {
            "topHttpCallDomains": t.array(t.proxy(renames["DomainCallsIn"])).optional(),
            "totalHttpCallCount": t.integer().optional(),
        }
    ).named(renames["DomainCallEvidenceIn"])
    types["DomainCallEvidenceOut"] = t.struct(
        {
            "topHttpCallDomains": t.array(
                t.proxy(renames["DomainCallsOut"])
            ).optional(),
            "totalHttpCallCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DomainCallEvidenceOut"])
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
    types["AdTechnologyProvidersIn"] = t.struct(
        {
            "unidentifiedProviderDomains": t.array(t.string()).optional(),
            "detectedProviderIds": t.array(t.string()).optional(),
            "detectedGvlIds": t.array(t.string()).optional(),
        }
    ).named(renames["AdTechnologyProvidersIn"])
    types["AdTechnologyProvidersOut"] = t.struct(
        {
            "unidentifiedProviderDomains": t.array(t.string()).optional(),
            "detectedProviderIds": t.array(t.string()).optional(),
            "detectedGvlIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdTechnologyProvidersOut"])
    types["CloseUserListRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CloseUserListRequestIn"]
    )
    types["CloseUserListRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CloseUserListRequestOut"])
    types["PretargetingConfigIn"] = t.struct(
        {
            "includedLanguages": t.array(t.string()).optional(),
            "includedMobileOperatingSystemIds": t.array(t.string()).optional(),
            "includedUserIdTypes": t.array(t.string()).optional(),
            "includedFormats": t.array(t.string()).optional(),
            "minimumViewabilityDecile": t.integer().optional(),
            "maximumQps": t.string().optional(),
            "publisherTargeting": t.proxy(
                renames["StringTargetingDimensionIn"]
            ).optional(),
            "verticalTargeting": t.proxy(
                renames["NumericTargetingDimensionIn"]
            ).optional(),
            "userListTargeting": t.proxy(
                renames["NumericTargetingDimensionIn"]
            ).optional(),
            "geoTargeting": t.proxy(renames["NumericTargetingDimensionIn"]).optional(),
            "displayName": t.string().optional(),
            "includedCreativeDimensions": t.array(
                t.proxy(renames["CreativeDimensionsIn"])
            ).optional(),
            "excludedContentLabelIds": t.array(t.string()).optional(),
            "includedPlatforms": t.array(t.string()).optional(),
            "includedEnvironments": t.array(t.string()).optional(),
            "appTargeting": t.proxy(renames["AppTargetingIn"]).optional(),
            "allowedUserTargetingModes": t.array(t.string()).optional(),
            "webTargeting": t.proxy(renames["StringTargetingDimensionIn"]).optional(),
            "interstitialTargeting": t.string().optional(),
        }
    ).named(renames["PretargetingConfigIn"])
    types["PretargetingConfigOut"] = t.struct(
        {
            "includedLanguages": t.array(t.string()).optional(),
            "includedMobileOperatingSystemIds": t.array(t.string()).optional(),
            "includedUserIdTypes": t.array(t.string()).optional(),
            "includedFormats": t.array(t.string()).optional(),
            "minimumViewabilityDecile": t.integer().optional(),
            "maximumQps": t.string().optional(),
            "publisherTargeting": t.proxy(
                renames["StringTargetingDimensionOut"]
            ).optional(),
            "verticalTargeting": t.proxy(
                renames["NumericTargetingDimensionOut"]
            ).optional(),
            "invalidGeoIds": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "userListTargeting": t.proxy(
                renames["NumericTargetingDimensionOut"]
            ).optional(),
            "geoTargeting": t.proxy(renames["NumericTargetingDimensionOut"]).optional(),
            "displayName": t.string().optional(),
            "state": t.string().optional(),
            "includedCreativeDimensions": t.array(
                t.proxy(renames["CreativeDimensionsOut"])
            ).optional(),
            "excludedContentLabelIds": t.array(t.string()).optional(),
            "includedPlatforms": t.array(t.string()).optional(),
            "includedEnvironments": t.array(t.string()).optional(),
            "billingId": t.string().optional(),
            "appTargeting": t.proxy(renames["AppTargetingOut"]).optional(),
            "allowedUserTargetingModes": t.array(t.string()).optional(),
            "webTargeting": t.proxy(renames["StringTargetingDimensionOut"]).optional(),
            "interstitialTargeting": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PretargetingConfigOut"])
    types["SuspendPretargetingConfigRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["SuspendPretargetingConfigRequestIn"])
    types["SuspendPretargetingConfigRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SuspendPretargetingConfigRequestOut"])
    types["BatchApprovePublisherConnectionsRequestIn"] = t.struct(
        {"names": t.array(t.string())}
    ).named(renames["BatchApprovePublisherConnectionsRequestIn"])
    types["BatchApprovePublisherConnectionsRequestOut"] = t.struct(
        {
            "names": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchApprovePublisherConnectionsRequestOut"])
    types["BidderIn"] = t.struct({"_": t.string().optional()}).named(
        renames["BidderIn"]
    )
    types["BidderOut"] = t.struct(
        {
            "dealsBillingId": t.string().optional(),
            "name": t.string().optional(),
            "cookieMatchingNetworkId": t.string().optional(),
            "cookieMatchingUrl": t.string().optional(),
            "bypassNonguaranteedDealsPretargeting": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BidderOut"])
    types["NumericTargetingDimensionIn"] = t.struct(
        {
            "includedIds": t.array(t.string()).optional(),
            "excludedIds": t.array(t.string()).optional(),
        }
    ).named(renames["NumericTargetingDimensionIn"])
    types["NumericTargetingDimensionOut"] = t.struct(
        {
            "includedIds": t.array(t.string()).optional(),
            "excludedIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NumericTargetingDimensionOut"])
    types["GetRemarketingTagResponseIn"] = t.struct(
        {"snippet": t.string().optional()}
    ).named(renames["GetRemarketingTagResponseIn"])
    types["GetRemarketingTagResponseOut"] = t.struct(
        {
            "snippet": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetRemarketingTagResponseOut"])
    types["DestinationUrlEvidenceIn"] = t.struct(
        {"destinationUrl": t.string().optional()}
    ).named(renames["DestinationUrlEvidenceIn"])
    types["DestinationUrlEvidenceOut"] = t.struct(
        {
            "destinationUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DestinationUrlEvidenceOut"])
    types["NativeContentIn"] = t.struct(
        {
            "body": t.string().optional(),
            "image": t.proxy(renames["ImageIn"]).optional(),
            "advertiserName": t.string().optional(),
            "videoUrl": t.string().optional(),
            "starRating": t.number().optional(),
            "headline": t.string().optional(),
            "logo": t.proxy(renames["ImageIn"]).optional(),
            "callToAction": t.string().optional(),
            "clickLinkUrl": t.string().optional(),
            "videoVastXml": t.string().optional(),
            "priceDisplayText": t.string().optional(),
            "appIcon": t.proxy(renames["ImageIn"]).optional(),
            "clickTrackingUrl": t.string().optional(),
        }
    ).named(renames["NativeContentIn"])
    types["NativeContentOut"] = t.struct(
        {
            "body": t.string().optional(),
            "image": t.proxy(renames["ImageOut"]).optional(),
            "advertiserName": t.string().optional(),
            "videoUrl": t.string().optional(),
            "starRating": t.number().optional(),
            "headline": t.string().optional(),
            "logo": t.proxy(renames["ImageOut"]).optional(),
            "callToAction": t.string().optional(),
            "clickLinkUrl": t.string().optional(),
            "videoVastXml": t.string().optional(),
            "priceDisplayText": t.string().optional(),
            "appIcon": t.proxy(renames["ImageOut"]).optional(),
            "clickTrackingUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NativeContentOut"])
    types["AddTargetedAppsRequestIn"] = t.struct(
        {"targetingMode": t.string(), "appIds": t.array(t.string()).optional()}
    ).named(renames["AddTargetedAppsRequestIn"])
    types["AddTargetedAppsRequestOut"] = t.struct(
        {
            "targetingMode": t.string(),
            "appIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddTargetedAppsRequestOut"])
    types["VideoContentIn"] = t.struct(
        {"videoVastXml": t.string().optional(), "videoUrl": t.string().optional()}
    ).named(renames["VideoContentIn"])
    types["VideoContentOut"] = t.struct(
        {
            "videoMetadata": t.proxy(renames["VideoMetadataOut"]).optional(),
            "videoVastXml": t.string().optional(),
            "videoUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoContentOut"])
    types["CreativeServingDecisionIn"] = t.struct(
        {
            "networkPolicyCompliance": t.proxy(
                renames["PolicyComplianceIn"]
            ).optional(),
            "detectedSensitiveCategories": t.array(t.integer()).optional(),
            "russiaPolicyCompliance": t.proxy(renames["PolicyComplianceIn"]).optional(),
            "detectedLanguages": t.array(t.string()).optional(),
            "dealsPolicyCompliance": t.proxy(renames["PolicyComplianceIn"]).optional(),
            "platformPolicyCompliance": t.proxy(
                renames["PolicyComplianceIn"]
            ).optional(),
            "detectedDomains": t.array(t.string()).optional(),
            "detectedAttributes": t.array(t.string()).optional(),
            "detectedVendorIds": t.array(t.integer()).optional(),
            "chinaPolicyCompliance": t.proxy(renames["PolicyComplianceIn"]).optional(),
            "lastStatusUpdate": t.string().optional(),
            "detectedAdvertisers": t.array(
                t.proxy(renames["AdvertiserAndBrandIn"])
            ).optional(),
            "adTechnologyProviders": t.proxy(
                renames["AdTechnologyProvidersIn"]
            ).optional(),
            "detectedProductCategories": t.array(t.integer()).optional(),
            "detectedClickThroughUrls": t.array(t.string()).optional(),
        }
    ).named(renames["CreativeServingDecisionIn"])
    types["CreativeServingDecisionOut"] = t.struct(
        {
            "networkPolicyCompliance": t.proxy(
                renames["PolicyComplianceOut"]
            ).optional(),
            "detectedSensitiveCategories": t.array(t.integer()).optional(),
            "russiaPolicyCompliance": t.proxy(
                renames["PolicyComplianceOut"]
            ).optional(),
            "detectedLanguages": t.array(t.string()).optional(),
            "dealsPolicyCompliance": t.proxy(renames["PolicyComplianceOut"]).optional(),
            "platformPolicyCompliance": t.proxy(
                renames["PolicyComplianceOut"]
            ).optional(),
            "detectedDomains": t.array(t.string()).optional(),
            "detectedAttributes": t.array(t.string()).optional(),
            "detectedVendorIds": t.array(t.integer()).optional(),
            "chinaPolicyCompliance": t.proxy(renames["PolicyComplianceOut"]).optional(),
            "lastStatusUpdate": t.string().optional(),
            "detectedAdvertisers": t.array(
                t.proxy(renames["AdvertiserAndBrandOut"])
            ).optional(),
            "adTechnologyProviders": t.proxy(
                renames["AdTechnologyProvidersOut"]
            ).optional(),
            "detectedProductCategories": t.array(t.integer()).optional(),
            "detectedClickThroughUrls": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeServingDecisionOut"])
    types["OpenUserListRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OpenUserListRequestIn"]
    )
    types["OpenUserListRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["OpenUserListRequestOut"])
    types["UserListIn"] = t.struct(
        {
            "description": t.string().optional(),
            "displayName": t.string(),
            "urlRestriction": t.proxy(renames["UrlRestrictionIn"]),
            "membershipDurationDays": t.string(),
        }
    ).named(renames["UserListIn"])
    types["UserListOut"] = t.struct(
        {
            "description": t.string().optional(),
            "displayName": t.string(),
            "status": t.string().optional(),
            "name": t.string().optional(),
            "urlRestriction": t.proxy(renames["UrlRestrictionOut"]),
            "membershipDurationDays": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserListOut"])
    types["ListUserListsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "userLists": t.array(t.proxy(renames["UserListIn"])).optional(),
        }
    ).named(renames["ListUserListsResponseIn"])
    types["ListUserListsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "userLists": t.array(t.proxy(renames["UserListOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListUserListsResponseOut"])
    types["RemoveTargetedPublishersRequestIn"] = t.struct(
        {"publisherIds": t.array(t.string()).optional()}
    ).named(renames["RemoveTargetedPublishersRequestIn"])
    types["RemoveTargetedPublishersRequestOut"] = t.struct(
        {
            "publisherIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveTargetedPublishersRequestOut"])
    types["BatchRejectPublisherConnectionsResponseIn"] = t.struct(
        {
            "publisherConnections": t.array(
                t.proxy(renames["PublisherConnectionIn"])
            ).optional()
        }
    ).named(renames["BatchRejectPublisherConnectionsResponseIn"])
    types["BatchRejectPublisherConnectionsResponseOut"] = t.struct(
        {
            "publisherConnections": t.array(
                t.proxy(renames["PublisherConnectionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchRejectPublisherConnectionsResponseOut"])
    types["BatchApprovePublisherConnectionsResponseIn"] = t.struct(
        {
            "publisherConnections": t.array(
                t.proxy(renames["PublisherConnectionIn"])
            ).optional()
        }
    ).named(renames["BatchApprovePublisherConnectionsResponseIn"])
    types["BatchApprovePublisherConnectionsResponseOut"] = t.struct(
        {
            "publisherConnections": t.array(
                t.proxy(renames["PublisherConnectionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchApprovePublisherConnectionsResponseOut"])
    types["VideoMetadataIn"] = t.struct(
        {
            "vastVersion": t.string().optional(),
            "duration": t.string().optional(),
            "skipOffset": t.string().optional(),
            "mediaFiles": t.array(t.proxy(renames["MediaFileIn"])).optional(),
            "isValidVast": t.boolean().optional(),
            "isVpaid": t.boolean().optional(),
        }
    ).named(renames["VideoMetadataIn"])
    types["VideoMetadataOut"] = t.struct(
        {
            "vastVersion": t.string().optional(),
            "duration": t.string().optional(),
            "skipOffset": t.string().optional(),
            "mediaFiles": t.array(t.proxy(renames["MediaFileOut"])).optional(),
            "isValidVast": t.boolean().optional(),
            "isVpaid": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoMetadataOut"])
    types["DestinationNotCrawlableEvidenceIn"] = t.struct(
        {
            "reason": t.string().optional(),
            "crawlTime": t.string().optional(),
            "crawledUrl": t.string().optional(),
        }
    ).named(renames["DestinationNotCrawlableEvidenceIn"])
    types["DestinationNotCrawlableEvidenceOut"] = t.struct(
        {
            "reason": t.string().optional(),
            "crawlTime": t.string().optional(),
            "crawledUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DestinationNotCrawlableEvidenceOut"])
    types["ListBiddersResponseIn"] = t.struct(
        {
            "bidders": t.array(t.proxy(renames["BidderIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListBiddersResponseIn"])
    types["ListBiddersResponseOut"] = t.struct(
        {
            "bidders": t.array(t.proxy(renames["BidderOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBiddersResponseOut"])
    types["PolicyTopicEntryIn"] = t.struct(
        {
            "policyTopic": t.string().optional(),
            "evidences": t.array(t.proxy(renames["PolicyTopicEvidenceIn"])).optional(),
            "missingCertificate": t.boolean().optional(),
            "helpCenterUrl": t.string().optional(),
        }
    ).named(renames["PolicyTopicEntryIn"])
    types["PolicyTopicEntryOut"] = t.struct(
        {
            "policyTopic": t.string().optional(),
            "evidences": t.array(t.proxy(renames["PolicyTopicEvidenceOut"])).optional(),
            "missingCertificate": t.boolean().optional(),
            "helpCenterUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyTopicEntryOut"])
    types["AdvertiserAndBrandIn"] = t.struct(
        {
            "advertiserId": t.string().optional(),
            "brandName": t.string().optional(),
            "brandId": t.string().optional(),
            "advertiserName": t.string().optional(),
        }
    ).named(renames["AdvertiserAndBrandIn"])
    types["AdvertiserAndBrandOut"] = t.struct(
        {
            "advertiserId": t.string().optional(),
            "brandName": t.string().optional(),
            "brandId": t.string().optional(),
            "advertiserName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdvertiserAndBrandOut"])
    types["PolicyTopicEvidenceIn"] = t.struct(
        {
            "destinationNotWorking": t.proxy(
                renames["DestinationNotWorkingEvidenceIn"]
            ).optional(),
            "downloadSize": t.proxy(renames["DownloadSizeEvidenceIn"]).optional(),
            "domainCall": t.proxy(renames["DomainCallEvidenceIn"]).optional(),
            "destinationNotCrawlable": t.proxy(
                renames["DestinationNotCrawlableEvidenceIn"]
            ).optional(),
            "httpCall": t.proxy(renames["HttpCallEvidenceIn"]).optional(),
            "destinationUrl": t.proxy(renames["DestinationUrlEvidenceIn"]).optional(),
            "httpCookie": t.proxy(renames["HttpCookieEvidenceIn"]).optional(),
        }
    ).named(renames["PolicyTopicEvidenceIn"])
    types["PolicyTopicEvidenceOut"] = t.struct(
        {
            "destinationNotWorking": t.proxy(
                renames["DestinationNotWorkingEvidenceOut"]
            ).optional(),
            "downloadSize": t.proxy(renames["DownloadSizeEvidenceOut"]).optional(),
            "domainCall": t.proxy(renames["DomainCallEvidenceOut"]).optional(),
            "destinationNotCrawlable": t.proxy(
                renames["DestinationNotCrawlableEvidenceOut"]
            ).optional(),
            "httpCall": t.proxy(renames["HttpCallEvidenceOut"]).optional(),
            "destinationUrl": t.proxy(renames["DestinationUrlEvidenceOut"]).optional(),
            "httpCookie": t.proxy(renames["HttpCookieEvidenceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyTopicEvidenceOut"])
    types["EndpointIn"] = t.struct(
        {
            "bidProtocol": t.string().optional(),
            "maximumQps": t.string().optional(),
            "tradingLocation": t.string().optional(),
        }
    ).named(renames["EndpointIn"])
    types["EndpointOut"] = t.struct(
        {
            "bidProtocol": t.string().optional(),
            "maximumQps": t.string().optional(),
            "tradingLocation": t.string().optional(),
            "name": t.string().optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EndpointOut"])
    types["ImageIn"] = t.struct(
        {
            "width": t.integer().optional(),
            "height": t.integer().optional(),
            "url": t.string().optional(),
        }
    ).named(renames["ImageIn"])
    types["ImageOut"] = t.struct(
        {
            "width": t.integer().optional(),
            "height": t.integer().optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageOut"])
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
    types["DomainCallsIn"] = t.struct(
        {"domain": t.string().optional(), "httpCallCount": t.integer().optional()}
    ).named(renames["DomainCallsIn"])
    types["DomainCallsOut"] = t.struct(
        {
            "domain": t.string().optional(),
            "httpCallCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DomainCallsOut"])
    types["ActivatePretargetingConfigRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ActivatePretargetingConfigRequestIn"])
    types["ActivatePretargetingConfigRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ActivatePretargetingConfigRequestOut"])
    types["ListEndpointsResponseIn"] = t.struct(
        {
            "endpoints": t.array(t.proxy(renames["EndpointIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListEndpointsResponseIn"])
    types["ListEndpointsResponseOut"] = t.struct(
        {
            "endpoints": t.array(t.proxy(renames["EndpointOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListEndpointsResponseOut"])
    types["DownloadSizeEvidenceIn"] = t.struct(
        {
            "topUrlDownloadSizeBreakdowns": t.array(
                t.proxy(renames["UrlDownloadSizeIn"])
            ).optional(),
            "totalDownloadSizeKb": t.integer().optional(),
        }
    ).named(renames["DownloadSizeEvidenceIn"])
    types["DownloadSizeEvidenceOut"] = t.struct(
        {
            "topUrlDownloadSizeBreakdowns": t.array(
                t.proxy(renames["UrlDownloadSizeOut"])
            ).optional(),
            "totalDownloadSizeKb": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DownloadSizeEvidenceOut"])
    types["AddTargetedSitesRequestIn"] = t.struct(
        {"targetingMode": t.string(), "sites": t.array(t.string()).optional()}
    ).named(renames["AddTargetedSitesRequestIn"])
    types["AddTargetedSitesRequestOut"] = t.struct(
        {
            "targetingMode": t.string(),
            "sites": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddTargetedSitesRequestOut"])
    types["PolicyComplianceIn"] = t.struct(
        {
            "status": t.string().optional(),
            "topics": t.array(t.proxy(renames["PolicyTopicEntryIn"])).optional(),
        }
    ).named(renames["PolicyComplianceIn"])
    types["PolicyComplianceOut"] = t.struct(
        {
            "status": t.string().optional(),
            "topics": t.array(t.proxy(renames["PolicyTopicEntryOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyComplianceOut"])
    types["RemoveTargetedSitesRequestIn"] = t.struct(
        {"sites": t.array(t.string()).optional()}
    ).named(renames["RemoveTargetedSitesRequestIn"])
    types["RemoveTargetedSitesRequestOut"] = t.struct(
        {
            "sites": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveTargetedSitesRequestOut"])
    types["WatchCreativesResponseIn"] = t.struct(
        {"topic": t.string().optional(), "subscription": t.string().optional()}
    ).named(renames["WatchCreativesResponseIn"])
    types["WatchCreativesResponseOut"] = t.struct(
        {
            "topic": t.string().optional(),
            "subscription": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WatchCreativesResponseOut"])
    types["BuyerIn"] = t.struct({"_": t.string().optional()}).named(renames["BuyerIn"])
    types["BuyerOut"] = t.struct(
        {
            "activeCreativeCount": t.string().optional(),
            "billingIds": t.array(t.string()).optional(),
            "maximumActiveCreativeCount": t.string().optional(),
            "name": t.string().optional(),
            "bidder": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuyerOut"])
    types["CreativeDimensionsIn"] = t.struct(
        {"height": t.string().optional(), "width": t.string().optional()}
    ).named(renames["CreativeDimensionsIn"])
    types["CreativeDimensionsOut"] = t.struct(
        {
            "height": t.string().optional(),
            "width": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeDimensionsOut"])
    types["HtmlContentIn"] = t.struct(
        {
            "width": t.integer().optional(),
            "height": t.integer().optional(),
            "snippet": t.string().optional(),
        }
    ).named(renames["HtmlContentIn"])
    types["HtmlContentOut"] = t.struct(
        {
            "width": t.integer().optional(),
            "height": t.integer().optional(),
            "snippet": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HtmlContentOut"])
    types["ListBuyersResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "buyers": t.array(t.proxy(renames["BuyerIn"])).optional(),
        }
    ).named(renames["ListBuyersResponseIn"])
    types["ListBuyersResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "buyers": t.array(t.proxy(renames["BuyerOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBuyersResponseOut"])
    types["MediaFileIn"] = t.struct(
        {"mimeType": t.string().optional(), "bitrate": t.string().optional()}
    ).named(renames["MediaFileIn"])
    types["MediaFileOut"] = t.struct(
        {
            "mimeType": t.string().optional(),
            "bitrate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MediaFileOut"])
    types["DestinationNotWorkingEvidenceIn"] = t.struct(
        {
            "platform": t.string().optional(),
            "lastCheckTime": t.string().optional(),
            "redirectionError": t.string().optional(),
            "expandedUrl": t.string().optional(),
            "invalidPage": t.string().optional(),
            "dnsError": t.string().optional(),
            "httpError": t.integer().optional(),
            "urlRejected": t.string().optional(),
        }
    ).named(renames["DestinationNotWorkingEvidenceIn"])
    types["DestinationNotWorkingEvidenceOut"] = t.struct(
        {
            "platform": t.string().optional(),
            "lastCheckTime": t.string().optional(),
            "redirectionError": t.string().optional(),
            "expandedUrl": t.string().optional(),
            "invalidPage": t.string().optional(),
            "dnsError": t.string().optional(),
            "httpError": t.integer().optional(),
            "urlRejected": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DestinationNotWorkingEvidenceOut"])
    types["ListPretargetingConfigsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "pretargetingConfigs": t.array(
                t.proxy(renames["PretargetingConfigIn"])
            ).optional(),
        }
    ).named(renames["ListPretargetingConfigsResponseIn"])
    types["ListPretargetingConfigsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "pretargetingConfigs": t.array(
                t.proxy(renames["PretargetingConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPretargetingConfigsResponseOut"])
    types["HttpCallEvidenceIn"] = t.struct(
        {"urls": t.array(t.string()).optional()}
    ).named(renames["HttpCallEvidenceIn"])
    types["HttpCallEvidenceOut"] = t.struct(
        {
            "urls": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpCallEvidenceOut"])
    types["RemoveTargetedAppsRequestIn"] = t.struct(
        {"appIds": t.array(t.string()).optional()}
    ).named(renames["RemoveTargetedAppsRequestIn"])
    types["RemoveTargetedAppsRequestOut"] = t.struct(
        {
            "appIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveTargetedAppsRequestOut"])
    types["WatchCreativesRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["WatchCreativesRequestIn"]
    )
    types["WatchCreativesRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["WatchCreativesRequestOut"])
    types["UrlDownloadSizeIn"] = t.struct(
        {
            "downloadSizeKb": t.integer().optional(),
            "normalizedUrl": t.string().optional(),
        }
    ).named(renames["UrlDownloadSizeIn"])
    types["UrlDownloadSizeOut"] = t.struct(
        {
            "downloadSizeKb": t.integer().optional(),
            "normalizedUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UrlDownloadSizeOut"])
    types["ListPublisherConnectionsResponseIn"] = t.struct(
        {
            "publisherConnections": t.array(
                t.proxy(renames["PublisherConnectionIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListPublisherConnectionsResponseIn"])
    types["ListPublisherConnectionsResponseOut"] = t.struct(
        {
            "publisherConnections": t.array(
                t.proxy(renames["PublisherConnectionOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPublisherConnectionsResponseOut"])
    types["AppTargetingIn"] = t.struct(
        {
            "mobileAppTargeting": t.proxy(
                renames["StringTargetingDimensionIn"]
            ).optional(),
            "mobileAppCategoryTargeting": t.proxy(
                renames["NumericTargetingDimensionIn"]
            ).optional(),
        }
    ).named(renames["AppTargetingIn"])
    types["AppTargetingOut"] = t.struct(
        {
            "mobileAppTargeting": t.proxy(
                renames["StringTargetingDimensionOut"]
            ).optional(),
            "mobileAppCategoryTargeting": t.proxy(
                renames["NumericTargetingDimensionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppTargetingOut"])
    types["StringTargetingDimensionIn"] = t.struct(
        {
            "targetingMode": t.string().optional(),
            "values": t.array(t.string()).optional(),
        }
    ).named(renames["StringTargetingDimensionIn"])
    types["StringTargetingDimensionOut"] = t.struct(
        {
            "targetingMode": t.string().optional(),
            "values": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StringTargetingDimensionOut"])
    types["CreativeIn"] = t.struct(
        {
            "creativeId": t.string().optional(),
            "html": t.proxy(renames["HtmlContentIn"]).optional(),
            "declaredClickThroughUrls": t.array(t.string()).optional(),
            "agencyId": t.string().optional(),
            "restrictedCategories": t.array(t.string()).optional(),
            "declaredVendorIds": t.array(t.integer()).optional(),
            "declaredAttributes": t.array(t.string()).optional(),
            "native": t.proxy(renames["NativeContentIn"]).optional(),
            "advertiserName": t.string().optional(),
            "renderUrl": t.string().optional(),
            "impressionTrackingUrls": t.array(t.string()).optional(),
            "adChoicesDestinationUrl": t.string().optional(),
            "declaredRestrictedCategories": t.array(t.string()).optional(),
            "video": t.proxy(renames["VideoContentIn"]).optional(),
        }
    ).named(renames["CreativeIn"])
    types["CreativeOut"] = t.struct(
        {
            "creativeId": t.string().optional(),
            "html": t.proxy(renames["HtmlContentOut"]).optional(),
            "version": t.integer().optional(),
            "declaredClickThroughUrls": t.array(t.string()).optional(),
            "agencyId": t.string().optional(),
            "creativeServingDecision": t.proxy(
                renames["CreativeServingDecisionOut"]
            ).optional(),
            "apiUpdateTime": t.string().optional(),
            "restrictedCategories": t.array(t.string()).optional(),
            "declaredVendorIds": t.array(t.integer()).optional(),
            "declaredAttributes": t.array(t.string()).optional(),
            "native": t.proxy(renames["NativeContentOut"]).optional(),
            "creativeFormat": t.string().optional(),
            "advertiserName": t.string().optional(),
            "dealIds": t.array(t.string()).optional(),
            "accountId": t.string().optional(),
            "renderUrl": t.string().optional(),
            "name": t.string().optional(),
            "impressionTrackingUrls": t.array(t.string()).optional(),
            "adChoicesDestinationUrl": t.string().optional(),
            "declaredRestrictedCategories": t.array(t.string()).optional(),
            "video": t.proxy(renames["VideoContentOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeOut"])
    types["AddTargetedPublishersRequestIn"] = t.struct(
        {"publisherIds": t.array(t.string()).optional(), "targetingMode": t.string()}
    ).named(renames["AddTargetedPublishersRequestIn"])
    types["AddTargetedPublishersRequestOut"] = t.struct(
        {
            "publisherIds": t.array(t.string()).optional(),
            "targetingMode": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddTargetedPublishersRequestOut"])
    types["BatchRejectPublisherConnectionsRequestIn"] = t.struct(
        {"names": t.array(t.string())}
    ).named(renames["BatchRejectPublisherConnectionsRequestIn"])
    types["BatchRejectPublisherConnectionsRequestOut"] = t.struct(
        {
            "names": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchRejectPublisherConnectionsRequestOut"])

    functions = {}
    functions["biddersGet"] = realtimebidding.get(
        "v1/bidders",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBiddersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersList"] = realtimebidding.get(
        "v1/bidders",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBiddersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPretargetingConfigsSuspend"] = realtimebidding.get(
        "v1/{parent}/pretargetingConfigs",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPretargetingConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPretargetingConfigsPatch"] = realtimebidding.get(
        "v1/{parent}/pretargetingConfigs",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPretargetingConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPretargetingConfigsCreate"] = realtimebidding.get(
        "v1/{parent}/pretargetingConfigs",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPretargetingConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPretargetingConfigsRemoveTargetedSites"] = realtimebidding.get(
        "v1/{parent}/pretargetingConfigs",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPretargetingConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPretargetingConfigsAddTargetedSites"] = realtimebidding.get(
        "v1/{parent}/pretargetingConfigs",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPretargetingConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "biddersPretargetingConfigsRemoveTargetedPublishers"
    ] = realtimebidding.get(
        "v1/{parent}/pretargetingConfigs",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPretargetingConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPretargetingConfigsAddTargetedPublishers"] = realtimebidding.get(
        "v1/{parent}/pretargetingConfigs",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPretargetingConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPretargetingConfigsAddTargetedApps"] = realtimebidding.get(
        "v1/{parent}/pretargetingConfigs",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPretargetingConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPretargetingConfigsDelete"] = realtimebidding.get(
        "v1/{parent}/pretargetingConfigs",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPretargetingConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPretargetingConfigsRemoveTargetedApps"] = realtimebidding.get(
        "v1/{parent}/pretargetingConfigs",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPretargetingConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPretargetingConfigsGet"] = realtimebidding.get(
        "v1/{parent}/pretargetingConfigs",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPretargetingConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPretargetingConfigsActivate"] = realtimebidding.get(
        "v1/{parent}/pretargetingConfigs",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPretargetingConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPretargetingConfigsList"] = realtimebidding.get(
        "v1/{parent}/pretargetingConfigs",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPretargetingConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersCreativesWatch"] = realtimebidding.get(
        "v1/{parent}/creatives",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "view": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCreativesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersCreativesList"] = realtimebidding.get(
        "v1/{parent}/creatives",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "view": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCreativesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersEndpointsGet"] = realtimebidding.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "bidProtocol": t.string().optional(),
                "maximumQps": t.string().optional(),
                "tradingLocation": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EndpointOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersEndpointsList"] = realtimebidding.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "bidProtocol": t.string().optional(),
                "maximumQps": t.string().optional(),
                "tradingLocation": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EndpointOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersEndpointsPatch"] = realtimebidding.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "bidProtocol": t.string().optional(),
                "maximumQps": t.string().optional(),
                "tradingLocation": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EndpointOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPublisherConnectionsGet"] = realtimebidding.post(
        "v1/{parent}/publisherConnections:batchReject",
        t.struct(
            {
                "parent": t.string(),
                "names": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchRejectPublisherConnectionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPublisherConnectionsBatchApprove"] = realtimebidding.post(
        "v1/{parent}/publisherConnections:batchReject",
        t.struct(
            {
                "parent": t.string(),
                "names": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchRejectPublisherConnectionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPublisherConnectionsList"] = realtimebidding.post(
        "v1/{parent}/publisherConnections:batchReject",
        t.struct(
            {
                "parent": t.string(),
                "names": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchRejectPublisherConnectionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPublisherConnectionsBatchReject"] = realtimebidding.post(
        "v1/{parent}/publisherConnections:batchReject",
        t.struct(
            {
                "parent": t.string(),
                "names": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchRejectPublisherConnectionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersGetRemarketingTag"] = realtimebidding.get(
        "v1/buyers",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBuyersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersGet"] = realtimebidding.get(
        "v1/buyers",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBuyersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersList"] = realtimebidding.get(
        "v1/buyers",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBuyersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersCreativesPatch"] = realtimebidding.get(
        "v1/{name}",
        t.struct(
            {
                "view": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersCreativesCreate"] = realtimebidding.get(
        "v1/{name}",
        t.struct(
            {
                "view": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersCreativesList"] = realtimebidding.get(
        "v1/{name}",
        t.struct(
            {
                "view": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersCreativesGet"] = realtimebidding.get(
        "v1/{name}",
        t.struct(
            {
                "view": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersUserListsClose"] = realtimebidding.get(
        "v1/{name}:getRemarketingTag",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GetRemarketingTagResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersUserListsList"] = realtimebidding.get(
        "v1/{name}:getRemarketingTag",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GetRemarketingTagResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersUserListsOpen"] = realtimebidding.get(
        "v1/{name}:getRemarketingTag",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GetRemarketingTagResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersUserListsGet"] = realtimebidding.get(
        "v1/{name}:getRemarketingTag",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GetRemarketingTagResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersUserListsCreate"] = realtimebidding.get(
        "v1/{name}:getRemarketingTag",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GetRemarketingTagResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersUserListsUpdate"] = realtimebidding.get(
        "v1/{name}:getRemarketingTag",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GetRemarketingTagResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersUserListsGetRemarketingTag"] = realtimebidding.get(
        "v1/{name}:getRemarketingTag",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GetRemarketingTagResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="realtimebidding", renames=renames, types=types, functions=functions
    )
