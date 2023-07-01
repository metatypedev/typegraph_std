from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_realtimebidding():
    realtimebidding = HTTPRuntime("https://realtimebidding.googleapis.com/")

    renames = {
        "ErrorResponse": "_realtimebidding_1_ErrorResponse",
        "RemoveTargetedPublishersRequestIn": "_realtimebidding_2_RemoveTargetedPublishersRequestIn",
        "RemoveTargetedPublishersRequestOut": "_realtimebidding_3_RemoveTargetedPublishersRequestOut",
        "AdTechnologyProvidersIn": "_realtimebidding_4_AdTechnologyProvidersIn",
        "AdTechnologyProvidersOut": "_realtimebidding_5_AdTechnologyProvidersOut",
        "HttpCookieEvidenceIn": "_realtimebidding_6_HttpCookieEvidenceIn",
        "HttpCookieEvidenceOut": "_realtimebidding_7_HttpCookieEvidenceOut",
        "AdvertiserAndBrandIn": "_realtimebidding_8_AdvertiserAndBrandIn",
        "AdvertiserAndBrandOut": "_realtimebidding_9_AdvertiserAndBrandOut",
        "DestinationNotCrawlableEvidenceIn": "_realtimebidding_10_DestinationNotCrawlableEvidenceIn",
        "DestinationNotCrawlableEvidenceOut": "_realtimebidding_11_DestinationNotCrawlableEvidenceOut",
        "BatchRejectPublisherConnectionsRequestIn": "_realtimebidding_12_BatchRejectPublisherConnectionsRequestIn",
        "BatchRejectPublisherConnectionsRequestOut": "_realtimebidding_13_BatchRejectPublisherConnectionsRequestOut",
        "ImageIn": "_realtimebidding_14_ImageIn",
        "ImageOut": "_realtimebidding_15_ImageOut",
        "DestinationUrlEvidenceIn": "_realtimebidding_16_DestinationUrlEvidenceIn",
        "DestinationUrlEvidenceOut": "_realtimebidding_17_DestinationUrlEvidenceOut",
        "MediaFileIn": "_realtimebidding_18_MediaFileIn",
        "MediaFileOut": "_realtimebidding_19_MediaFileOut",
        "ListCreativesResponseIn": "_realtimebidding_20_ListCreativesResponseIn",
        "ListCreativesResponseOut": "_realtimebidding_21_ListCreativesResponseOut",
        "PublisherConnectionIn": "_realtimebidding_22_PublisherConnectionIn",
        "PublisherConnectionOut": "_realtimebidding_23_PublisherConnectionOut",
        "ListPretargetingConfigsResponseIn": "_realtimebidding_24_ListPretargetingConfigsResponseIn",
        "ListPretargetingConfigsResponseOut": "_realtimebidding_25_ListPretargetingConfigsResponseOut",
        "BatchApprovePublisherConnectionsResponseIn": "_realtimebidding_26_BatchApprovePublisherConnectionsResponseIn",
        "BatchApprovePublisherConnectionsResponseOut": "_realtimebidding_27_BatchApprovePublisherConnectionsResponseOut",
        "EmptyIn": "_realtimebidding_28_EmptyIn",
        "EmptyOut": "_realtimebidding_29_EmptyOut",
        "PolicyTopicEvidenceIn": "_realtimebidding_30_PolicyTopicEvidenceIn",
        "PolicyTopicEvidenceOut": "_realtimebidding_31_PolicyTopicEvidenceOut",
        "BidderIn": "_realtimebidding_32_BidderIn",
        "BidderOut": "_realtimebidding_33_BidderOut",
        "EndpointIn": "_realtimebidding_34_EndpointIn",
        "EndpointOut": "_realtimebidding_35_EndpointOut",
        "PretargetingConfigIn": "_realtimebidding_36_PretargetingConfigIn",
        "PretargetingConfigOut": "_realtimebidding_37_PretargetingConfigOut",
        "CreativeServingDecisionIn": "_realtimebidding_38_CreativeServingDecisionIn",
        "CreativeServingDecisionOut": "_realtimebidding_39_CreativeServingDecisionOut",
        "WatchCreativesRequestIn": "_realtimebidding_40_WatchCreativesRequestIn",
        "WatchCreativesRequestOut": "_realtimebidding_41_WatchCreativesRequestOut",
        "NumericTargetingDimensionIn": "_realtimebidding_42_NumericTargetingDimensionIn",
        "NumericTargetingDimensionOut": "_realtimebidding_43_NumericTargetingDimensionOut",
        "GetRemarketingTagResponseIn": "_realtimebidding_44_GetRemarketingTagResponseIn",
        "GetRemarketingTagResponseOut": "_realtimebidding_45_GetRemarketingTagResponseOut",
        "DestinationNotWorkingEvidenceIn": "_realtimebidding_46_DestinationNotWorkingEvidenceIn",
        "DestinationNotWorkingEvidenceOut": "_realtimebidding_47_DestinationNotWorkingEvidenceOut",
        "DateIn": "_realtimebidding_48_DateIn",
        "DateOut": "_realtimebidding_49_DateOut",
        "VideoMetadataIn": "_realtimebidding_50_VideoMetadataIn",
        "VideoMetadataOut": "_realtimebidding_51_VideoMetadataOut",
        "DomainCallEvidenceIn": "_realtimebidding_52_DomainCallEvidenceIn",
        "DomainCallEvidenceOut": "_realtimebidding_53_DomainCallEvidenceOut",
        "RemoveTargetedAppsRequestIn": "_realtimebidding_54_RemoveTargetedAppsRequestIn",
        "RemoveTargetedAppsRequestOut": "_realtimebidding_55_RemoveTargetedAppsRequestOut",
        "SuspendPretargetingConfigRequestIn": "_realtimebidding_56_SuspendPretargetingConfigRequestIn",
        "SuspendPretargetingConfigRequestOut": "_realtimebidding_57_SuspendPretargetingConfigRequestOut",
        "BuyerIn": "_realtimebidding_58_BuyerIn",
        "BuyerOut": "_realtimebidding_59_BuyerOut",
        "NativeContentIn": "_realtimebidding_60_NativeContentIn",
        "NativeContentOut": "_realtimebidding_61_NativeContentOut",
        "CloseUserListRequestIn": "_realtimebidding_62_CloseUserListRequestIn",
        "CloseUserListRequestOut": "_realtimebidding_63_CloseUserListRequestOut",
        "UserListIn": "_realtimebidding_64_UserListIn",
        "UserListOut": "_realtimebidding_65_UserListOut",
        "ListBuyersResponseIn": "_realtimebidding_66_ListBuyersResponseIn",
        "ListBuyersResponseOut": "_realtimebidding_67_ListBuyersResponseOut",
        "AddTargetedSitesRequestIn": "_realtimebidding_68_AddTargetedSitesRequestIn",
        "AddTargetedSitesRequestOut": "_realtimebidding_69_AddTargetedSitesRequestOut",
        "DomainCallsIn": "_realtimebidding_70_DomainCallsIn",
        "DomainCallsOut": "_realtimebidding_71_DomainCallsOut",
        "AppTargetingIn": "_realtimebidding_72_AppTargetingIn",
        "AppTargetingOut": "_realtimebidding_73_AppTargetingOut",
        "BatchApprovePublisherConnectionsRequestIn": "_realtimebidding_74_BatchApprovePublisherConnectionsRequestIn",
        "BatchApprovePublisherConnectionsRequestOut": "_realtimebidding_75_BatchApprovePublisherConnectionsRequestOut",
        "ListEndpointsResponseIn": "_realtimebidding_76_ListEndpointsResponseIn",
        "ListEndpointsResponseOut": "_realtimebidding_77_ListEndpointsResponseOut",
        "CreativeIn": "_realtimebidding_78_CreativeIn",
        "CreativeOut": "_realtimebidding_79_CreativeOut",
        "UrlDownloadSizeIn": "_realtimebidding_80_UrlDownloadSizeIn",
        "UrlDownloadSizeOut": "_realtimebidding_81_UrlDownloadSizeOut",
        "ListPublisherConnectionsResponseIn": "_realtimebidding_82_ListPublisherConnectionsResponseIn",
        "ListPublisherConnectionsResponseOut": "_realtimebidding_83_ListPublisherConnectionsResponseOut",
        "WatchCreativesResponseIn": "_realtimebidding_84_WatchCreativesResponseIn",
        "WatchCreativesResponseOut": "_realtimebidding_85_WatchCreativesResponseOut",
        "AddTargetedAppsRequestIn": "_realtimebidding_86_AddTargetedAppsRequestIn",
        "AddTargetedAppsRequestOut": "_realtimebidding_87_AddTargetedAppsRequestOut",
        "RemoveTargetedSitesRequestIn": "_realtimebidding_88_RemoveTargetedSitesRequestIn",
        "RemoveTargetedSitesRequestOut": "_realtimebidding_89_RemoveTargetedSitesRequestOut",
        "VideoContentIn": "_realtimebidding_90_VideoContentIn",
        "VideoContentOut": "_realtimebidding_91_VideoContentOut",
        "AddTargetedPublishersRequestIn": "_realtimebidding_92_AddTargetedPublishersRequestIn",
        "AddTargetedPublishersRequestOut": "_realtimebidding_93_AddTargetedPublishersRequestOut",
        "UrlRestrictionIn": "_realtimebidding_94_UrlRestrictionIn",
        "UrlRestrictionOut": "_realtimebidding_95_UrlRestrictionOut",
        "BatchRejectPublisherConnectionsResponseIn": "_realtimebidding_96_BatchRejectPublisherConnectionsResponseIn",
        "BatchRejectPublisherConnectionsResponseOut": "_realtimebidding_97_BatchRejectPublisherConnectionsResponseOut",
        "StringTargetingDimensionIn": "_realtimebidding_98_StringTargetingDimensionIn",
        "StringTargetingDimensionOut": "_realtimebidding_99_StringTargetingDimensionOut",
        "HtmlContentIn": "_realtimebidding_100_HtmlContentIn",
        "HtmlContentOut": "_realtimebidding_101_HtmlContentOut",
        "CreativeDimensionsIn": "_realtimebidding_102_CreativeDimensionsIn",
        "CreativeDimensionsOut": "_realtimebidding_103_CreativeDimensionsOut",
        "ListUserListsResponseIn": "_realtimebidding_104_ListUserListsResponseIn",
        "ListUserListsResponseOut": "_realtimebidding_105_ListUserListsResponseOut",
        "PolicyComplianceIn": "_realtimebidding_106_PolicyComplianceIn",
        "PolicyComplianceOut": "_realtimebidding_107_PolicyComplianceOut",
        "ListBiddersResponseIn": "_realtimebidding_108_ListBiddersResponseIn",
        "ListBiddersResponseOut": "_realtimebidding_109_ListBiddersResponseOut",
        "HttpCallEvidenceIn": "_realtimebidding_110_HttpCallEvidenceIn",
        "HttpCallEvidenceOut": "_realtimebidding_111_HttpCallEvidenceOut",
        "ActivatePretargetingConfigRequestIn": "_realtimebidding_112_ActivatePretargetingConfigRequestIn",
        "ActivatePretargetingConfigRequestOut": "_realtimebidding_113_ActivatePretargetingConfigRequestOut",
        "OpenUserListRequestIn": "_realtimebidding_114_OpenUserListRequestIn",
        "OpenUserListRequestOut": "_realtimebidding_115_OpenUserListRequestOut",
        "DownloadSizeEvidenceIn": "_realtimebidding_116_DownloadSizeEvidenceIn",
        "DownloadSizeEvidenceOut": "_realtimebidding_117_DownloadSizeEvidenceOut",
        "PolicyTopicEntryIn": "_realtimebidding_118_PolicyTopicEntryIn",
        "PolicyTopicEntryOut": "_realtimebidding_119_PolicyTopicEntryOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["RemoveTargetedPublishersRequestIn"] = t.struct(
        {"publisherIds": t.array(t.string()).optional()}
    ).named(renames["RemoveTargetedPublishersRequestIn"])
    types["RemoveTargetedPublishersRequestOut"] = t.struct(
        {
            "publisherIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveTargetedPublishersRequestOut"])
    types["AdTechnologyProvidersIn"] = t.struct(
        {
            "detectedGvlIds": t.array(t.string()).optional(),
            "unidentifiedProviderDomains": t.array(t.string()).optional(),
            "detectedProviderIds": t.array(t.string()).optional(),
        }
    ).named(renames["AdTechnologyProvidersIn"])
    types["AdTechnologyProvidersOut"] = t.struct(
        {
            "detectedGvlIds": t.array(t.string()).optional(),
            "unidentifiedProviderDomains": t.array(t.string()).optional(),
            "detectedProviderIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdTechnologyProvidersOut"])
    types["HttpCookieEvidenceIn"] = t.struct(
        {
            "cookieNames": t.array(t.string()).optional(),
            "maxCookieCount": t.integer().optional(),
        }
    ).named(renames["HttpCookieEvidenceIn"])
    types["HttpCookieEvidenceOut"] = t.struct(
        {
            "cookieNames": t.array(t.string()).optional(),
            "maxCookieCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpCookieEvidenceOut"])
    types["AdvertiserAndBrandIn"] = t.struct(
        {
            "brandName": t.string().optional(),
            "advertiserName": t.string().optional(),
            "advertiserId": t.string().optional(),
            "brandId": t.string().optional(),
        }
    ).named(renames["AdvertiserAndBrandIn"])
    types["AdvertiserAndBrandOut"] = t.struct(
        {
            "brandName": t.string().optional(),
            "advertiserName": t.string().optional(),
            "advertiserId": t.string().optional(),
            "brandId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdvertiserAndBrandOut"])
    types["DestinationNotCrawlableEvidenceIn"] = t.struct(
        {
            "crawlTime": t.string().optional(),
            "reason": t.string().optional(),
            "crawledUrl": t.string().optional(),
        }
    ).named(renames["DestinationNotCrawlableEvidenceIn"])
    types["DestinationNotCrawlableEvidenceOut"] = t.struct(
        {
            "crawlTime": t.string().optional(),
            "reason": t.string().optional(),
            "crawledUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DestinationNotCrawlableEvidenceOut"])
    types["BatchRejectPublisherConnectionsRequestIn"] = t.struct(
        {"names": t.array(t.string())}
    ).named(renames["BatchRejectPublisherConnectionsRequestIn"])
    types["BatchRejectPublisherConnectionsRequestOut"] = t.struct(
        {
            "names": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchRejectPublisherConnectionsRequestOut"])
    types["ImageIn"] = t.struct(
        {
            "height": t.integer().optional(),
            "width": t.integer().optional(),
            "url": t.string().optional(),
        }
    ).named(renames["ImageIn"])
    types["ImageOut"] = t.struct(
        {
            "height": t.integer().optional(),
            "width": t.integer().optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageOut"])
    types["DestinationUrlEvidenceIn"] = t.struct(
        {"destinationUrl": t.string().optional()}
    ).named(renames["DestinationUrlEvidenceIn"])
    types["DestinationUrlEvidenceOut"] = t.struct(
        {
            "destinationUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DestinationUrlEvidenceOut"])
    types["MediaFileIn"] = t.struct(
        {"bitrate": t.string().optional(), "mimeType": t.string().optional()}
    ).named(renames["MediaFileIn"])
    types["MediaFileOut"] = t.struct(
        {
            "bitrate": t.string().optional(),
            "mimeType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MediaFileOut"])
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
    types["PublisherConnectionIn"] = t.struct(
        {"biddingState": t.string().optional()}
    ).named(renames["PublisherConnectionIn"])
    types["PublisherConnectionOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "biddingState": t.string().optional(),
            "name": t.string().optional(),
            "publisherPlatform": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublisherConnectionOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["PolicyTopicEvidenceIn"] = t.struct(
        {
            "httpCookie": t.proxy(renames["HttpCookieEvidenceIn"]).optional(),
            "destinationNotWorking": t.proxy(
                renames["DestinationNotWorkingEvidenceIn"]
            ).optional(),
            "destinationNotCrawlable": t.proxy(
                renames["DestinationNotCrawlableEvidenceIn"]
            ).optional(),
            "httpCall": t.proxy(renames["HttpCallEvidenceIn"]).optional(),
            "destinationUrl": t.proxy(renames["DestinationUrlEvidenceIn"]).optional(),
            "downloadSize": t.proxy(renames["DownloadSizeEvidenceIn"]).optional(),
            "domainCall": t.proxy(renames["DomainCallEvidenceIn"]).optional(),
        }
    ).named(renames["PolicyTopicEvidenceIn"])
    types["PolicyTopicEvidenceOut"] = t.struct(
        {
            "httpCookie": t.proxy(renames["HttpCookieEvidenceOut"]).optional(),
            "destinationNotWorking": t.proxy(
                renames["DestinationNotWorkingEvidenceOut"]
            ).optional(),
            "destinationNotCrawlable": t.proxy(
                renames["DestinationNotCrawlableEvidenceOut"]
            ).optional(),
            "httpCall": t.proxy(renames["HttpCallEvidenceOut"]).optional(),
            "destinationUrl": t.proxy(renames["DestinationUrlEvidenceOut"]).optional(),
            "downloadSize": t.proxy(renames["DownloadSizeEvidenceOut"]).optional(),
            "domainCall": t.proxy(renames["DomainCallEvidenceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyTopicEvidenceOut"])
    types["BidderIn"] = t.struct({"_": t.string().optional()}).named(
        renames["BidderIn"]
    )
    types["BidderOut"] = t.struct(
        {
            "cookieMatchingNetworkId": t.string().optional(),
            "dealsBillingId": t.string().optional(),
            "name": t.string().optional(),
            "cookieMatchingUrl": t.string().optional(),
            "bypassNonguaranteedDealsPretargeting": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BidderOut"])
    types["EndpointIn"] = t.struct(
        {
            "tradingLocation": t.string().optional(),
            "maximumQps": t.string().optional(),
            "bidProtocol": t.string().optional(),
        }
    ).named(renames["EndpointIn"])
    types["EndpointOut"] = t.struct(
        {
            "name": t.string().optional(),
            "url": t.string().optional(),
            "tradingLocation": t.string().optional(),
            "maximumQps": t.string().optional(),
            "bidProtocol": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EndpointOut"])
    types["PretargetingConfigIn"] = t.struct(
        {
            "includedEnvironments": t.array(t.string()).optional(),
            "minimumViewabilityDecile": t.integer().optional(),
            "verticalTargeting": t.proxy(
                renames["NumericTargetingDimensionIn"]
            ).optional(),
            "webTargeting": t.proxy(renames["StringTargetingDimensionIn"]).optional(),
            "geoTargeting": t.proxy(renames["NumericTargetingDimensionIn"]).optional(),
            "appTargeting": t.proxy(renames["AppTargetingIn"]).optional(),
            "includedLanguages": t.array(t.string()).optional(),
            "maximumQps": t.string().optional(),
            "userListTargeting": t.proxy(
                renames["NumericTargetingDimensionIn"]
            ).optional(),
            "excludedContentLabelIds": t.array(t.string()).optional(),
            "includedPlatforms": t.array(t.string()).optional(),
            "allowedUserTargetingModes": t.array(t.string()).optional(),
            "interstitialTargeting": t.string().optional(),
            "includedMobileOperatingSystemIds": t.array(t.string()).optional(),
            "includedFormats": t.array(t.string()).optional(),
            "publisherTargeting": t.proxy(
                renames["StringTargetingDimensionIn"]
            ).optional(),
            "includedCreativeDimensions": t.array(
                t.proxy(renames["CreativeDimensionsIn"])
            ).optional(),
            "includedUserIdTypes": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["PretargetingConfigIn"])
    types["PretargetingConfigOut"] = t.struct(
        {
            "invalidGeoIds": t.array(t.string()).optional(),
            "includedEnvironments": t.array(t.string()).optional(),
            "minimumViewabilityDecile": t.integer().optional(),
            "verticalTargeting": t.proxy(
                renames["NumericTargetingDimensionOut"]
            ).optional(),
            "webTargeting": t.proxy(renames["StringTargetingDimensionOut"]).optional(),
            "geoTargeting": t.proxy(renames["NumericTargetingDimensionOut"]).optional(),
            "billingId": t.string().optional(),
            "state": t.string().optional(),
            "appTargeting": t.proxy(renames["AppTargetingOut"]).optional(),
            "includedLanguages": t.array(t.string()).optional(),
            "maximumQps": t.string().optional(),
            "userListTargeting": t.proxy(
                renames["NumericTargetingDimensionOut"]
            ).optional(),
            "excludedContentLabelIds": t.array(t.string()).optional(),
            "includedPlatforms": t.array(t.string()).optional(),
            "allowedUserTargetingModes": t.array(t.string()).optional(),
            "interstitialTargeting": t.string().optional(),
            "includedMobileOperatingSystemIds": t.array(t.string()).optional(),
            "includedFormats": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "publisherTargeting": t.proxy(
                renames["StringTargetingDimensionOut"]
            ).optional(),
            "includedCreativeDimensions": t.array(
                t.proxy(renames["CreativeDimensionsOut"])
            ).optional(),
            "includedUserIdTypes": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PretargetingConfigOut"])
    types["CreativeServingDecisionIn"] = t.struct(
        {
            "detectedLanguages": t.array(t.string()).optional(),
            "detectedSensitiveCategories": t.array(t.integer()).optional(),
            "networkPolicyCompliance": t.proxy(
                renames["PolicyComplianceIn"]
            ).optional(),
            "detectedAdvertisers": t.array(
                t.proxy(renames["AdvertiserAndBrandIn"])
            ).optional(),
            "detectedVendorIds": t.array(t.integer()).optional(),
            "chinaPolicyCompliance": t.proxy(renames["PolicyComplianceIn"]).optional(),
            "lastStatusUpdate": t.string().optional(),
            "detectedProductCategories": t.array(t.integer()).optional(),
            "russiaPolicyCompliance": t.proxy(renames["PolicyComplianceIn"]).optional(),
            "adTechnologyProviders": t.proxy(
                renames["AdTechnologyProvidersIn"]
            ).optional(),
            "detectedClickThroughUrls": t.array(t.string()).optional(),
            "detectedAttributes": t.array(t.string()).optional(),
            "dealsPolicyCompliance": t.proxy(renames["PolicyComplianceIn"]).optional(),
            "platformPolicyCompliance": t.proxy(
                renames["PolicyComplianceIn"]
            ).optional(),
            "detectedDomains": t.array(t.string()).optional(),
        }
    ).named(renames["CreativeServingDecisionIn"])
    types["CreativeServingDecisionOut"] = t.struct(
        {
            "detectedLanguages": t.array(t.string()).optional(),
            "detectedSensitiveCategories": t.array(t.integer()).optional(),
            "networkPolicyCompliance": t.proxy(
                renames["PolicyComplianceOut"]
            ).optional(),
            "detectedAdvertisers": t.array(
                t.proxy(renames["AdvertiserAndBrandOut"])
            ).optional(),
            "detectedVendorIds": t.array(t.integer()).optional(),
            "chinaPolicyCompliance": t.proxy(renames["PolicyComplianceOut"]).optional(),
            "lastStatusUpdate": t.string().optional(),
            "detectedProductCategories": t.array(t.integer()).optional(),
            "russiaPolicyCompliance": t.proxy(
                renames["PolicyComplianceOut"]
            ).optional(),
            "adTechnologyProviders": t.proxy(
                renames["AdTechnologyProvidersOut"]
            ).optional(),
            "detectedClickThroughUrls": t.array(t.string()).optional(),
            "detectedAttributes": t.array(t.string()).optional(),
            "dealsPolicyCompliance": t.proxy(renames["PolicyComplianceOut"]).optional(),
            "platformPolicyCompliance": t.proxy(
                renames["PolicyComplianceOut"]
            ).optional(),
            "detectedDomains": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeServingDecisionOut"])
    types["WatchCreativesRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["WatchCreativesRequestIn"]
    )
    types["WatchCreativesRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["WatchCreativesRequestOut"])
    types["NumericTargetingDimensionIn"] = t.struct(
        {
            "excludedIds": t.array(t.string()).optional(),
            "includedIds": t.array(t.string()).optional(),
        }
    ).named(renames["NumericTargetingDimensionIn"])
    types["NumericTargetingDimensionOut"] = t.struct(
        {
            "excludedIds": t.array(t.string()).optional(),
            "includedIds": t.array(t.string()).optional(),
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
    types["DestinationNotWorkingEvidenceIn"] = t.struct(
        {
            "dnsError": t.string().optional(),
            "invalidPage": t.string().optional(),
            "platform": t.string().optional(),
            "httpError": t.integer().optional(),
            "lastCheckTime": t.string().optional(),
            "urlRejected": t.string().optional(),
            "redirectionError": t.string().optional(),
            "expandedUrl": t.string().optional(),
        }
    ).named(renames["DestinationNotWorkingEvidenceIn"])
    types["DestinationNotWorkingEvidenceOut"] = t.struct(
        {
            "dnsError": t.string().optional(),
            "invalidPage": t.string().optional(),
            "platform": t.string().optional(),
            "httpError": t.integer().optional(),
            "lastCheckTime": t.string().optional(),
            "urlRejected": t.string().optional(),
            "redirectionError": t.string().optional(),
            "expandedUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DestinationNotWorkingEvidenceOut"])
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
    types["VideoMetadataIn"] = t.struct(
        {
            "isValidVast": t.boolean().optional(),
            "isVpaid": t.boolean().optional(),
            "mediaFiles": t.array(t.proxy(renames["MediaFileIn"])).optional(),
            "duration": t.string().optional(),
            "vastVersion": t.string().optional(),
            "skipOffset": t.string().optional(),
        }
    ).named(renames["VideoMetadataIn"])
    types["VideoMetadataOut"] = t.struct(
        {
            "isValidVast": t.boolean().optional(),
            "isVpaid": t.boolean().optional(),
            "mediaFiles": t.array(t.proxy(renames["MediaFileOut"])).optional(),
            "duration": t.string().optional(),
            "vastVersion": t.string().optional(),
            "skipOffset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoMetadataOut"])
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
    types["RemoveTargetedAppsRequestIn"] = t.struct(
        {"appIds": t.array(t.string()).optional()}
    ).named(renames["RemoveTargetedAppsRequestIn"])
    types["RemoveTargetedAppsRequestOut"] = t.struct(
        {
            "appIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveTargetedAppsRequestOut"])
    types["SuspendPretargetingConfigRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["SuspendPretargetingConfigRequestIn"])
    types["SuspendPretargetingConfigRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SuspendPretargetingConfigRequestOut"])
    types["BuyerIn"] = t.struct({"_": t.string().optional()}).named(renames["BuyerIn"])
    types["BuyerOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "bidder": t.string().optional(),
            "maximumActiveCreativeCount": t.string().optional(),
            "name": t.string().optional(),
            "billingIds": t.array(t.string()).optional(),
            "activeCreativeCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuyerOut"])
    types["NativeContentIn"] = t.struct(
        {
            "logo": t.proxy(renames["ImageIn"]).optional(),
            "advertiserName": t.string().optional(),
            "image": t.proxy(renames["ImageIn"]).optional(),
            "body": t.string().optional(),
            "appIcon": t.proxy(renames["ImageIn"]).optional(),
            "clickTrackingUrl": t.string().optional(),
            "starRating": t.number().optional(),
            "headline": t.string().optional(),
            "videoVastXml": t.string().optional(),
            "callToAction": t.string().optional(),
            "priceDisplayText": t.string().optional(),
            "clickLinkUrl": t.string().optional(),
            "videoUrl": t.string().optional(),
        }
    ).named(renames["NativeContentIn"])
    types["NativeContentOut"] = t.struct(
        {
            "logo": t.proxy(renames["ImageOut"]).optional(),
            "advertiserName": t.string().optional(),
            "image": t.proxy(renames["ImageOut"]).optional(),
            "body": t.string().optional(),
            "appIcon": t.proxy(renames["ImageOut"]).optional(),
            "clickTrackingUrl": t.string().optional(),
            "starRating": t.number().optional(),
            "headline": t.string().optional(),
            "videoVastXml": t.string().optional(),
            "callToAction": t.string().optional(),
            "priceDisplayText": t.string().optional(),
            "clickLinkUrl": t.string().optional(),
            "videoUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NativeContentOut"])
    types["CloseUserListRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CloseUserListRequestIn"]
    )
    types["CloseUserListRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CloseUserListRequestOut"])
    types["UserListIn"] = t.struct(
        {
            "urlRestriction": t.proxy(renames["UrlRestrictionIn"]),
            "description": t.string().optional(),
            "displayName": t.string(),
            "membershipDurationDays": t.string(),
        }
    ).named(renames["UserListIn"])
    types["UserListOut"] = t.struct(
        {
            "urlRestriction": t.proxy(renames["UrlRestrictionOut"]),
            "description": t.string().optional(),
            "displayName": t.string(),
            "name": t.string().optional(),
            "membershipDurationDays": t.string(),
            "status": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserListOut"])
    types["ListBuyersResponseIn"] = t.struct(
        {
            "buyers": t.array(t.proxy(renames["BuyerIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListBuyersResponseIn"])
    types["ListBuyersResponseOut"] = t.struct(
        {
            "buyers": t.array(t.proxy(renames["BuyerOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBuyersResponseOut"])
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
    types["DomainCallsIn"] = t.struct(
        {"httpCallCount": t.integer().optional(), "domain": t.string().optional()}
    ).named(renames["DomainCallsIn"])
    types["DomainCallsOut"] = t.struct(
        {
            "httpCallCount": t.integer().optional(),
            "domain": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DomainCallsOut"])
    types["AppTargetingIn"] = t.struct(
        {
            "mobileAppCategoryTargeting": t.proxy(
                renames["NumericTargetingDimensionIn"]
            ).optional(),
            "mobileAppTargeting": t.proxy(
                renames["StringTargetingDimensionIn"]
            ).optional(),
        }
    ).named(renames["AppTargetingIn"])
    types["AppTargetingOut"] = t.struct(
        {
            "mobileAppCategoryTargeting": t.proxy(
                renames["NumericTargetingDimensionOut"]
            ).optional(),
            "mobileAppTargeting": t.proxy(
                renames["StringTargetingDimensionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppTargetingOut"])
    types["BatchApprovePublisherConnectionsRequestIn"] = t.struct(
        {"names": t.array(t.string())}
    ).named(renames["BatchApprovePublisherConnectionsRequestIn"])
    types["BatchApprovePublisherConnectionsRequestOut"] = t.struct(
        {
            "names": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchApprovePublisherConnectionsRequestOut"])
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
    types["CreativeIn"] = t.struct(
        {
            "agencyId": t.string().optional(),
            "adChoicesDestinationUrl": t.string().optional(),
            "restrictedCategories": t.array(t.string()).optional(),
            "renderUrl": t.string().optional(),
            "native": t.proxy(renames["NativeContentIn"]).optional(),
            "declaredRestrictedCategories": t.array(t.string()).optional(),
            "creativeId": t.string().optional(),
            "declaredVendorIds": t.array(t.integer()).optional(),
            "impressionTrackingUrls": t.array(t.string()).optional(),
            "html": t.proxy(renames["HtmlContentIn"]).optional(),
            "video": t.proxy(renames["VideoContentIn"]).optional(),
            "declaredClickThroughUrls": t.array(t.string()).optional(),
            "declaredAttributes": t.array(t.string()).optional(),
            "advertiserName": t.string().optional(),
        }
    ).named(renames["CreativeIn"])
    types["CreativeOut"] = t.struct(
        {
            "agencyId": t.string().optional(),
            "adChoicesDestinationUrl": t.string().optional(),
            "restrictedCategories": t.array(t.string()).optional(),
            "renderUrl": t.string().optional(),
            "creativeServingDecision": t.proxy(
                renames["CreativeServingDecisionOut"]
            ).optional(),
            "version": t.integer().optional(),
            "native": t.proxy(renames["NativeContentOut"]).optional(),
            "declaredRestrictedCategories": t.array(t.string()).optional(),
            "creativeId": t.string().optional(),
            "declaredVendorIds": t.array(t.integer()).optional(),
            "impressionTrackingUrls": t.array(t.string()).optional(),
            "html": t.proxy(renames["HtmlContentOut"]).optional(),
            "video": t.proxy(renames["VideoContentOut"]).optional(),
            "declaredClickThroughUrls": t.array(t.string()).optional(),
            "declaredAttributes": t.array(t.string()).optional(),
            "creativeFormat": t.string().optional(),
            "apiUpdateTime": t.string().optional(),
            "name": t.string().optional(),
            "dealIds": t.array(t.string()).optional(),
            "advertiserName": t.string().optional(),
            "accountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeOut"])
    types["UrlDownloadSizeIn"] = t.struct(
        {
            "normalizedUrl": t.string().optional(),
            "downloadSizeKb": t.integer().optional(),
        }
    ).named(renames["UrlDownloadSizeIn"])
    types["UrlDownloadSizeOut"] = t.struct(
        {
            "normalizedUrl": t.string().optional(),
            "downloadSizeKb": t.integer().optional(),
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
    types["AddTargetedAppsRequestIn"] = t.struct(
        {"appIds": t.array(t.string()).optional(), "targetingMode": t.string()}
    ).named(renames["AddTargetedAppsRequestIn"])
    types["AddTargetedAppsRequestOut"] = t.struct(
        {
            "appIds": t.array(t.string()).optional(),
            "targetingMode": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddTargetedAppsRequestOut"])
    types["RemoveTargetedSitesRequestIn"] = t.struct(
        {"sites": t.array(t.string()).optional()}
    ).named(renames["RemoveTargetedSitesRequestIn"])
    types["RemoveTargetedSitesRequestOut"] = t.struct(
        {
            "sites": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveTargetedSitesRequestOut"])
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
    types["UrlRestrictionIn"] = t.struct(
        {
            "endDate": t.proxy(renames["DateIn"]).optional(),
            "url": t.string(),
            "startDate": t.proxy(renames["DateIn"]).optional(),
            "restrictionType": t.string().optional(),
        }
    ).named(renames["UrlRestrictionIn"])
    types["UrlRestrictionOut"] = t.struct(
        {
            "endDate": t.proxy(renames["DateOut"]).optional(),
            "url": t.string(),
            "startDate": t.proxy(renames["DateOut"]).optional(),
            "restrictionType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UrlRestrictionOut"])
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
    types["StringTargetingDimensionIn"] = t.struct(
        {
            "values": t.array(t.string()).optional(),
            "targetingMode": t.string().optional(),
        }
    ).named(renames["StringTargetingDimensionIn"])
    types["StringTargetingDimensionOut"] = t.struct(
        {
            "values": t.array(t.string()).optional(),
            "targetingMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StringTargetingDimensionOut"])
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
    types["ListUserListsResponseIn"] = t.struct(
        {
            "userLists": t.array(t.proxy(renames["UserListIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListUserListsResponseIn"])
    types["ListUserListsResponseOut"] = t.struct(
        {
            "userLists": t.array(t.proxy(renames["UserListOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListUserListsResponseOut"])
    types["PolicyComplianceIn"] = t.struct(
        {
            "topics": t.array(t.proxy(renames["PolicyTopicEntryIn"])).optional(),
            "status": t.string().optional(),
        }
    ).named(renames["PolicyComplianceIn"])
    types["PolicyComplianceOut"] = t.struct(
        {
            "topics": t.array(t.proxy(renames["PolicyTopicEntryOut"])).optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyComplianceOut"])
    types["ListBiddersResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "bidders": t.array(t.proxy(renames["BidderIn"])).optional(),
        }
    ).named(renames["ListBiddersResponseIn"])
    types["ListBiddersResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "bidders": t.array(t.proxy(renames["BidderOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBiddersResponseOut"])
    types["HttpCallEvidenceIn"] = t.struct(
        {"urls": t.array(t.string()).optional()}
    ).named(renames["HttpCallEvidenceIn"])
    types["HttpCallEvidenceOut"] = t.struct(
        {
            "urls": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpCallEvidenceOut"])
    types["ActivatePretargetingConfigRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ActivatePretargetingConfigRequestIn"])
    types["ActivatePretargetingConfigRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ActivatePretargetingConfigRequestOut"])
    types["OpenUserListRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OpenUserListRequestIn"]
    )
    types["OpenUserListRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["OpenUserListRequestOut"])
    types["DownloadSizeEvidenceIn"] = t.struct(
        {
            "totalDownloadSizeKb": t.integer().optional(),
            "topUrlDownloadSizeBreakdowns": t.array(
                t.proxy(renames["UrlDownloadSizeIn"])
            ).optional(),
        }
    ).named(renames["DownloadSizeEvidenceIn"])
    types["DownloadSizeEvidenceOut"] = t.struct(
        {
            "totalDownloadSizeKb": t.integer().optional(),
            "topUrlDownloadSizeBreakdowns": t.array(
                t.proxy(renames["UrlDownloadSizeOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DownloadSizeEvidenceOut"])
    types["PolicyTopicEntryIn"] = t.struct(
        {
            "evidences": t.array(t.proxy(renames["PolicyTopicEvidenceIn"])).optional(),
            "helpCenterUrl": t.string().optional(),
            "policyTopic": t.string().optional(),
            "missingCertificate": t.boolean().optional(),
        }
    ).named(renames["PolicyTopicEntryIn"])
    types["PolicyTopicEntryOut"] = t.struct(
        {
            "evidences": t.array(t.proxy(renames["PolicyTopicEvidenceOut"])).optional(),
            "helpCenterUrl": t.string().optional(),
            "policyTopic": t.string().optional(),
            "missingCertificate": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyTopicEntryOut"])

    functions = {}
    functions["biddersGet"] = realtimebidding.get(
        "v1/bidders",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBiddersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersEndpointsPatch"] = realtimebidding.get(
        "v1/{parent}/endpoints",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEndpointsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersEndpointsGet"] = realtimebidding.get(
        "v1/{parent}/endpoints",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEndpointsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersEndpointsList"] = realtimebidding.get(
        "v1/{parent}/endpoints",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEndpointsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "biddersPretargetingConfigsRemoveTargetedPublishers"
    ] = realtimebidding.post(
        "v1/{pretargetingConfig}:removeTargetedSites",
        t.struct(
            {
                "pretargetingConfig": t.string(),
                "sites": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PretargetingConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPretargetingConfigsSuspend"] = realtimebidding.post(
        "v1/{pretargetingConfig}:removeTargetedSites",
        t.struct(
            {
                "pretargetingConfig": t.string(),
                "sites": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PretargetingConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPretargetingConfigsPatch"] = realtimebidding.post(
        "v1/{pretargetingConfig}:removeTargetedSites",
        t.struct(
            {
                "pretargetingConfig": t.string(),
                "sites": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PretargetingConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPretargetingConfigsActivate"] = realtimebidding.post(
        "v1/{pretargetingConfig}:removeTargetedSites",
        t.struct(
            {
                "pretargetingConfig": t.string(),
                "sites": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PretargetingConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPretargetingConfigsGet"] = realtimebidding.post(
        "v1/{pretargetingConfig}:removeTargetedSites",
        t.struct(
            {
                "pretargetingConfig": t.string(),
                "sites": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PretargetingConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPretargetingConfigsAddTargetedApps"] = realtimebidding.post(
        "v1/{pretargetingConfig}:removeTargetedSites",
        t.struct(
            {
                "pretargetingConfig": t.string(),
                "sites": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PretargetingConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPretargetingConfigsRemoveTargetedApps"] = realtimebidding.post(
        "v1/{pretargetingConfig}:removeTargetedSites",
        t.struct(
            {
                "pretargetingConfig": t.string(),
                "sites": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PretargetingConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPretargetingConfigsAddTargetedPublishers"] = realtimebidding.post(
        "v1/{pretargetingConfig}:removeTargetedSites",
        t.struct(
            {
                "pretargetingConfig": t.string(),
                "sites": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PretargetingConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPretargetingConfigsCreate"] = realtimebidding.post(
        "v1/{pretargetingConfig}:removeTargetedSites",
        t.struct(
            {
                "pretargetingConfig": t.string(),
                "sites": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PretargetingConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPretargetingConfigsList"] = realtimebidding.post(
        "v1/{pretargetingConfig}:removeTargetedSites",
        t.struct(
            {
                "pretargetingConfig": t.string(),
                "sites": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PretargetingConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPretargetingConfigsAddTargetedSites"] = realtimebidding.post(
        "v1/{pretargetingConfig}:removeTargetedSites",
        t.struct(
            {
                "pretargetingConfig": t.string(),
                "sites": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PretargetingConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPretargetingConfigsDelete"] = realtimebidding.post(
        "v1/{pretargetingConfig}:removeTargetedSites",
        t.struct(
            {
                "pretargetingConfig": t.string(),
                "sites": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PretargetingConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPretargetingConfigsRemoveTargetedSites"] = realtimebidding.post(
        "v1/{pretargetingConfig}:removeTargetedSites",
        t.struct(
            {
                "pretargetingConfig": t.string(),
                "sites": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PretargetingConfigOut"]),
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
    functions["biddersCreativesList"] = realtimebidding.post(
        "v1/{parent}/creatives:watch",
        t.struct(
            {
                "parent": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WatchCreativesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersCreativesWatch"] = realtimebidding.post(
        "v1/{parent}/creatives:watch",
        t.struct(
            {
                "parent": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WatchCreativesResponseOut"]),
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
    functions["buyersUserListsList"] = realtimebidding.post(
        "v1/{name}:open",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UserListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersUserListsGetRemarketingTag"] = realtimebidding.post(
        "v1/{name}:open",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UserListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersUserListsClose"] = realtimebidding.post(
        "v1/{name}:open",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UserListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersUserListsUpdate"] = realtimebidding.post(
        "v1/{name}:open",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UserListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersUserListsCreate"] = realtimebidding.post(
        "v1/{name}:open",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UserListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersUserListsGet"] = realtimebidding.post(
        "v1/{name}:open",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UserListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersUserListsOpen"] = realtimebidding.post(
        "v1/{name}:open",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UserListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersCreativesList"] = realtimebidding.post(
        "v1/{parent}/creatives",
        t.struct(
            {
                "parent": t.string(),
                "agencyId": t.string().optional(),
                "adChoicesDestinationUrl": t.string().optional(),
                "restrictedCategories": t.array(t.string()).optional(),
                "renderUrl": t.string().optional(),
                "native": t.proxy(renames["NativeContentIn"]).optional(),
                "declaredRestrictedCategories": t.array(t.string()).optional(),
                "creativeId": t.string().optional(),
                "declaredVendorIds": t.array(t.integer()).optional(),
                "impressionTrackingUrls": t.array(t.string()).optional(),
                "html": t.proxy(renames["HtmlContentIn"]).optional(),
                "video": t.proxy(renames["VideoContentIn"]).optional(),
                "declaredClickThroughUrls": t.array(t.string()).optional(),
                "declaredAttributes": t.array(t.string()).optional(),
                "advertiserName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersCreativesPatch"] = realtimebidding.post(
        "v1/{parent}/creatives",
        t.struct(
            {
                "parent": t.string(),
                "agencyId": t.string().optional(),
                "adChoicesDestinationUrl": t.string().optional(),
                "restrictedCategories": t.array(t.string()).optional(),
                "renderUrl": t.string().optional(),
                "native": t.proxy(renames["NativeContentIn"]).optional(),
                "declaredRestrictedCategories": t.array(t.string()).optional(),
                "creativeId": t.string().optional(),
                "declaredVendorIds": t.array(t.integer()).optional(),
                "impressionTrackingUrls": t.array(t.string()).optional(),
                "html": t.proxy(renames["HtmlContentIn"]).optional(),
                "video": t.proxy(renames["VideoContentIn"]).optional(),
                "declaredClickThroughUrls": t.array(t.string()).optional(),
                "declaredAttributes": t.array(t.string()).optional(),
                "advertiserName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersCreativesGet"] = realtimebidding.post(
        "v1/{parent}/creatives",
        t.struct(
            {
                "parent": t.string(),
                "agencyId": t.string().optional(),
                "adChoicesDestinationUrl": t.string().optional(),
                "restrictedCategories": t.array(t.string()).optional(),
                "renderUrl": t.string().optional(),
                "native": t.proxy(renames["NativeContentIn"]).optional(),
                "declaredRestrictedCategories": t.array(t.string()).optional(),
                "creativeId": t.string().optional(),
                "declaredVendorIds": t.array(t.integer()).optional(),
                "impressionTrackingUrls": t.array(t.string()).optional(),
                "html": t.proxy(renames["HtmlContentIn"]).optional(),
                "video": t.proxy(renames["VideoContentIn"]).optional(),
                "declaredClickThroughUrls": t.array(t.string()).optional(),
                "declaredAttributes": t.array(t.string()).optional(),
                "advertiserName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersCreativesCreate"] = realtimebidding.post(
        "v1/{parent}/creatives",
        t.struct(
            {
                "parent": t.string(),
                "agencyId": t.string().optional(),
                "adChoicesDestinationUrl": t.string().optional(),
                "restrictedCategories": t.array(t.string()).optional(),
                "renderUrl": t.string().optional(),
                "native": t.proxy(renames["NativeContentIn"]).optional(),
                "declaredRestrictedCategories": t.array(t.string()).optional(),
                "creativeId": t.string().optional(),
                "declaredVendorIds": t.array(t.integer()).optional(),
                "impressionTrackingUrls": t.array(t.string()).optional(),
                "html": t.proxy(renames["HtmlContentIn"]).optional(),
                "video": t.proxy(renames["VideoContentIn"]).optional(),
                "declaredClickThroughUrls": t.array(t.string()).optional(),
                "declaredAttributes": t.array(t.string()).optional(),
                "advertiserName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="realtimebidding",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
