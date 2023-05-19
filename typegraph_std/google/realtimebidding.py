from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_realtimebidding() -> Import:
    realtimebidding = HTTPRuntime("https://realtimebidding.googleapis.com/")

    renames = {
        "ErrorResponse": "_realtimebidding_1_ErrorResponse",
        "ListPublisherConnectionsResponseIn": "_realtimebidding_2_ListPublisherConnectionsResponseIn",
        "ListPublisherConnectionsResponseOut": "_realtimebidding_3_ListPublisherConnectionsResponseOut",
        "GetRemarketingTagResponseIn": "_realtimebidding_4_GetRemarketingTagResponseIn",
        "GetRemarketingTagResponseOut": "_realtimebidding_5_GetRemarketingTagResponseOut",
        "AddTargetedSitesRequestIn": "_realtimebidding_6_AddTargetedSitesRequestIn",
        "AddTargetedSitesRequestOut": "_realtimebidding_7_AddTargetedSitesRequestOut",
        "CloseUserListRequestIn": "_realtimebidding_8_CloseUserListRequestIn",
        "CloseUserListRequestOut": "_realtimebidding_9_CloseUserListRequestOut",
        "PolicyComplianceIn": "_realtimebidding_10_PolicyComplianceIn",
        "PolicyComplianceOut": "_realtimebidding_11_PolicyComplianceOut",
        "NativeContentIn": "_realtimebidding_12_NativeContentIn",
        "NativeContentOut": "_realtimebidding_13_NativeContentOut",
        "OpenUserListRequestIn": "_realtimebidding_14_OpenUserListRequestIn",
        "OpenUserListRequestOut": "_realtimebidding_15_OpenUserListRequestOut",
        "AppTargetingIn": "_realtimebidding_16_AppTargetingIn",
        "AppTargetingOut": "_realtimebidding_17_AppTargetingOut",
        "MediaFileIn": "_realtimebidding_18_MediaFileIn",
        "MediaFileOut": "_realtimebidding_19_MediaFileOut",
        "ListPretargetingConfigsResponseIn": "_realtimebidding_20_ListPretargetingConfigsResponseIn",
        "ListPretargetingConfigsResponseOut": "_realtimebidding_21_ListPretargetingConfigsResponseOut",
        "CreativeDimensionsIn": "_realtimebidding_22_CreativeDimensionsIn",
        "CreativeDimensionsOut": "_realtimebidding_23_CreativeDimensionsOut",
        "BatchRejectPublisherConnectionsRequestIn": "_realtimebidding_24_BatchRejectPublisherConnectionsRequestIn",
        "BatchRejectPublisherConnectionsRequestOut": "_realtimebidding_25_BatchRejectPublisherConnectionsRequestOut",
        "CreativeIn": "_realtimebidding_26_CreativeIn",
        "CreativeOut": "_realtimebidding_27_CreativeOut",
        "EmptyIn": "_realtimebidding_28_EmptyIn",
        "EmptyOut": "_realtimebidding_29_EmptyOut",
        "AdvertiserAndBrandIn": "_realtimebidding_30_AdvertiserAndBrandIn",
        "AdvertiserAndBrandOut": "_realtimebidding_31_AdvertiserAndBrandOut",
        "ListBuyersResponseIn": "_realtimebidding_32_ListBuyersResponseIn",
        "ListBuyersResponseOut": "_realtimebidding_33_ListBuyersResponseOut",
        "StringTargetingDimensionIn": "_realtimebidding_34_StringTargetingDimensionIn",
        "StringTargetingDimensionOut": "_realtimebidding_35_StringTargetingDimensionOut",
        "AddTargetedPublishersRequestIn": "_realtimebidding_36_AddTargetedPublishersRequestIn",
        "AddTargetedPublishersRequestOut": "_realtimebidding_37_AddTargetedPublishersRequestOut",
        "BatchApprovePublisherConnectionsRequestIn": "_realtimebidding_38_BatchApprovePublisherConnectionsRequestIn",
        "BatchApprovePublisherConnectionsRequestOut": "_realtimebidding_39_BatchApprovePublisherConnectionsRequestOut",
        "PublisherConnectionIn": "_realtimebidding_40_PublisherConnectionIn",
        "PublisherConnectionOut": "_realtimebidding_41_PublisherConnectionOut",
        "WatchCreativesResponseIn": "_realtimebidding_42_WatchCreativesResponseIn",
        "WatchCreativesResponseOut": "_realtimebidding_43_WatchCreativesResponseOut",
        "CreativeServingDecisionIn": "_realtimebidding_44_CreativeServingDecisionIn",
        "CreativeServingDecisionOut": "_realtimebidding_45_CreativeServingDecisionOut",
        "DestinationNotCrawlableEvidenceIn": "_realtimebidding_46_DestinationNotCrawlableEvidenceIn",
        "DestinationNotCrawlableEvidenceOut": "_realtimebidding_47_DestinationNotCrawlableEvidenceOut",
        "HttpCallEvidenceIn": "_realtimebidding_48_HttpCallEvidenceIn",
        "HttpCallEvidenceOut": "_realtimebidding_49_HttpCallEvidenceOut",
        "PretargetingConfigIn": "_realtimebidding_50_PretargetingConfigIn",
        "PretargetingConfigOut": "_realtimebidding_51_PretargetingConfigOut",
        "DomainCallEvidenceIn": "_realtimebidding_52_DomainCallEvidenceIn",
        "DomainCallEvidenceOut": "_realtimebidding_53_DomainCallEvidenceOut",
        "ListUserListsResponseIn": "_realtimebidding_54_ListUserListsResponseIn",
        "ListUserListsResponseOut": "_realtimebidding_55_ListUserListsResponseOut",
        "WatchCreativesRequestIn": "_realtimebidding_56_WatchCreativesRequestIn",
        "WatchCreativesRequestOut": "_realtimebidding_57_WatchCreativesRequestOut",
        "DomainCallsIn": "_realtimebidding_58_DomainCallsIn",
        "DomainCallsOut": "_realtimebidding_59_DomainCallsOut",
        "ImageIn": "_realtimebidding_60_ImageIn",
        "ImageOut": "_realtimebidding_61_ImageOut",
        "DateIn": "_realtimebidding_62_DateIn",
        "DateOut": "_realtimebidding_63_DateOut",
        "PolicyTopicEvidenceIn": "_realtimebidding_64_PolicyTopicEvidenceIn",
        "PolicyTopicEvidenceOut": "_realtimebidding_65_PolicyTopicEvidenceOut",
        "HttpCookieEvidenceIn": "_realtimebidding_66_HttpCookieEvidenceIn",
        "HttpCookieEvidenceOut": "_realtimebidding_67_HttpCookieEvidenceOut",
        "DestinationNotWorkingEvidenceIn": "_realtimebidding_68_DestinationNotWorkingEvidenceIn",
        "DestinationNotWorkingEvidenceOut": "_realtimebidding_69_DestinationNotWorkingEvidenceOut",
        "UserListIn": "_realtimebidding_70_UserListIn",
        "UserListOut": "_realtimebidding_71_UserListOut",
        "SuspendPretargetingConfigRequestIn": "_realtimebidding_72_SuspendPretargetingConfigRequestIn",
        "SuspendPretargetingConfigRequestOut": "_realtimebidding_73_SuspendPretargetingConfigRequestOut",
        "ListBiddersResponseIn": "_realtimebidding_74_ListBiddersResponseIn",
        "ListBiddersResponseOut": "_realtimebidding_75_ListBiddersResponseOut",
        "BatchRejectPublisherConnectionsResponseIn": "_realtimebidding_76_BatchRejectPublisherConnectionsResponseIn",
        "BatchRejectPublisherConnectionsResponseOut": "_realtimebidding_77_BatchRejectPublisherConnectionsResponseOut",
        "VideoContentIn": "_realtimebidding_78_VideoContentIn",
        "VideoContentOut": "_realtimebidding_79_VideoContentOut",
        "DestinationUrlEvidenceIn": "_realtimebidding_80_DestinationUrlEvidenceIn",
        "DestinationUrlEvidenceOut": "_realtimebidding_81_DestinationUrlEvidenceOut",
        "NumericTargetingDimensionIn": "_realtimebidding_82_NumericTargetingDimensionIn",
        "NumericTargetingDimensionOut": "_realtimebidding_83_NumericTargetingDimensionOut",
        "AdTechnologyProvidersIn": "_realtimebidding_84_AdTechnologyProvidersIn",
        "AdTechnologyProvidersOut": "_realtimebidding_85_AdTechnologyProvidersOut",
        "EndpointIn": "_realtimebidding_86_EndpointIn",
        "EndpointOut": "_realtimebidding_87_EndpointOut",
        "ListCreativesResponseIn": "_realtimebidding_88_ListCreativesResponseIn",
        "ListCreativesResponseOut": "_realtimebidding_89_ListCreativesResponseOut",
        "PolicyTopicEntryIn": "_realtimebidding_90_PolicyTopicEntryIn",
        "PolicyTopicEntryOut": "_realtimebidding_91_PolicyTopicEntryOut",
        "UrlRestrictionIn": "_realtimebidding_92_UrlRestrictionIn",
        "UrlRestrictionOut": "_realtimebidding_93_UrlRestrictionOut",
        "BidderIn": "_realtimebidding_94_BidderIn",
        "BidderOut": "_realtimebidding_95_BidderOut",
        "BatchApprovePublisherConnectionsResponseIn": "_realtimebidding_96_BatchApprovePublisherConnectionsResponseIn",
        "BatchApprovePublisherConnectionsResponseOut": "_realtimebidding_97_BatchApprovePublisherConnectionsResponseOut",
        "RemoveTargetedPublishersRequestIn": "_realtimebidding_98_RemoveTargetedPublishersRequestIn",
        "RemoveTargetedPublishersRequestOut": "_realtimebidding_99_RemoveTargetedPublishersRequestOut",
        "RemoveTargetedAppsRequestIn": "_realtimebidding_100_RemoveTargetedAppsRequestIn",
        "RemoveTargetedAppsRequestOut": "_realtimebidding_101_RemoveTargetedAppsRequestOut",
        "ActivatePretargetingConfigRequestIn": "_realtimebidding_102_ActivatePretargetingConfigRequestIn",
        "ActivatePretargetingConfigRequestOut": "_realtimebidding_103_ActivatePretargetingConfigRequestOut",
        "ListEndpointsResponseIn": "_realtimebidding_104_ListEndpointsResponseIn",
        "ListEndpointsResponseOut": "_realtimebidding_105_ListEndpointsResponseOut",
        "DownloadSizeEvidenceIn": "_realtimebidding_106_DownloadSizeEvidenceIn",
        "DownloadSizeEvidenceOut": "_realtimebidding_107_DownloadSizeEvidenceOut",
        "AddTargetedAppsRequestIn": "_realtimebidding_108_AddTargetedAppsRequestIn",
        "AddTargetedAppsRequestOut": "_realtimebidding_109_AddTargetedAppsRequestOut",
        "HtmlContentIn": "_realtimebidding_110_HtmlContentIn",
        "HtmlContentOut": "_realtimebidding_111_HtmlContentOut",
        "BuyerIn": "_realtimebidding_112_BuyerIn",
        "BuyerOut": "_realtimebidding_113_BuyerOut",
        "UrlDownloadSizeIn": "_realtimebidding_114_UrlDownloadSizeIn",
        "UrlDownloadSizeOut": "_realtimebidding_115_UrlDownloadSizeOut",
        "RemoveTargetedSitesRequestIn": "_realtimebidding_116_RemoveTargetedSitesRequestIn",
        "RemoveTargetedSitesRequestOut": "_realtimebidding_117_RemoveTargetedSitesRequestOut",
        "VideoMetadataIn": "_realtimebidding_118_VideoMetadataIn",
        "VideoMetadataOut": "_realtimebidding_119_VideoMetadataOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ListPublisherConnectionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "publisherConnections": t.array(
                t.proxy(renames["PublisherConnectionIn"])
            ).optional(),
        }
    ).named(renames["ListPublisherConnectionsResponseIn"])
    types["ListPublisherConnectionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "publisherConnections": t.array(
                t.proxy(renames["PublisherConnectionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPublisherConnectionsResponseOut"])
    types["GetRemarketingTagResponseIn"] = t.struct(
        {"snippet": t.string().optional()}
    ).named(renames["GetRemarketingTagResponseIn"])
    types["GetRemarketingTagResponseOut"] = t.struct(
        {
            "snippet": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetRemarketingTagResponseOut"])
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
    types["CloseUserListRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CloseUserListRequestIn"]
    )
    types["CloseUserListRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CloseUserListRequestOut"])
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
    types["NativeContentIn"] = t.struct(
        {
            "videoUrl": t.string().optional(),
            "logo": t.proxy(renames["ImageIn"]).optional(),
            "advertiserName": t.string().optional(),
            "videoVastXml": t.string().optional(),
            "callToAction": t.string().optional(),
            "priceDisplayText": t.string().optional(),
            "headline": t.string().optional(),
            "appIcon": t.proxy(renames["ImageIn"]).optional(),
            "clickTrackingUrl": t.string().optional(),
            "clickLinkUrl": t.string().optional(),
            "starRating": t.number().optional(),
            "body": t.string().optional(),
            "image": t.proxy(renames["ImageIn"]).optional(),
        }
    ).named(renames["NativeContentIn"])
    types["NativeContentOut"] = t.struct(
        {
            "videoUrl": t.string().optional(),
            "logo": t.proxy(renames["ImageOut"]).optional(),
            "advertiserName": t.string().optional(),
            "videoVastXml": t.string().optional(),
            "callToAction": t.string().optional(),
            "priceDisplayText": t.string().optional(),
            "headline": t.string().optional(),
            "appIcon": t.proxy(renames["ImageOut"]).optional(),
            "clickTrackingUrl": t.string().optional(),
            "clickLinkUrl": t.string().optional(),
            "starRating": t.number().optional(),
            "body": t.string().optional(),
            "image": t.proxy(renames["ImageOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NativeContentOut"])
    types["OpenUserListRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OpenUserListRequestIn"]
    )
    types["OpenUserListRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["OpenUserListRequestOut"])
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
    types["BatchRejectPublisherConnectionsRequestIn"] = t.struct(
        {"names": t.array(t.string())}
    ).named(renames["BatchRejectPublisherConnectionsRequestIn"])
    types["BatchRejectPublisherConnectionsRequestOut"] = t.struct(
        {
            "names": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchRejectPublisherConnectionsRequestOut"])
    types["CreativeIn"] = t.struct(
        {
            "agencyId": t.string().optional(),
            "impressionTrackingUrls": t.array(t.string()).optional(),
            "declaredVendorIds": t.array(t.integer()).optional(),
            "video": t.proxy(renames["VideoContentIn"]).optional(),
            "declaredRestrictedCategories": t.array(t.string()).optional(),
            "advertiserName": t.string().optional(),
            "renderUrl": t.string().optional(),
            "html": t.proxy(renames["HtmlContentIn"]).optional(),
            "declaredAttributes": t.array(t.string()).optional(),
            "creativeId": t.string().optional(),
            "native": t.proxy(renames["NativeContentIn"]).optional(),
            "adChoicesDestinationUrl": t.string().optional(),
            "declaredClickThroughUrls": t.array(t.string()).optional(),
            "restrictedCategories": t.array(t.string()).optional(),
        }
    ).named(renames["CreativeIn"])
    types["CreativeOut"] = t.struct(
        {
            "agencyId": t.string().optional(),
            "impressionTrackingUrls": t.array(t.string()).optional(),
            "creativeServingDecision": t.proxy(
                renames["CreativeServingDecisionOut"]
            ).optional(),
            "declaredVendorIds": t.array(t.integer()).optional(),
            "video": t.proxy(renames["VideoContentOut"]).optional(),
            "declaredRestrictedCategories": t.array(t.string()).optional(),
            "version": t.integer().optional(),
            "apiUpdateTime": t.string().optional(),
            "advertiserName": t.string().optional(),
            "creativeFormat": t.string().optional(),
            "renderUrl": t.string().optional(),
            "html": t.proxy(renames["HtmlContentOut"]).optional(),
            "declaredAttributes": t.array(t.string()).optional(),
            "creativeId": t.string().optional(),
            "dealIds": t.array(t.string()).optional(),
            "native": t.proxy(renames["NativeContentOut"]).optional(),
            "adChoicesDestinationUrl": t.string().optional(),
            "declaredClickThroughUrls": t.array(t.string()).optional(),
            "accountId": t.string().optional(),
            "name": t.string().optional(),
            "restrictedCategories": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["AdvertiserAndBrandIn"] = t.struct(
        {
            "advertiserName": t.string().optional(),
            "brandId": t.string().optional(),
            "brandName": t.string().optional(),
            "advertiserId": t.string().optional(),
        }
    ).named(renames["AdvertiserAndBrandIn"])
    types["AdvertiserAndBrandOut"] = t.struct(
        {
            "advertiserName": t.string().optional(),
            "brandId": t.string().optional(),
            "brandName": t.string().optional(),
            "advertiserId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdvertiserAndBrandOut"])
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
    types["BatchApprovePublisherConnectionsRequestIn"] = t.struct(
        {"names": t.array(t.string())}
    ).named(renames["BatchApprovePublisherConnectionsRequestIn"])
    types["BatchApprovePublisherConnectionsRequestOut"] = t.struct(
        {
            "names": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchApprovePublisherConnectionsRequestOut"])
    types["PublisherConnectionIn"] = t.struct(
        {"biddingState": t.string().optional()}
    ).named(renames["PublisherConnectionIn"])
    types["PublisherConnectionOut"] = t.struct(
        {
            "biddingState": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "publisherPlatform": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublisherConnectionOut"])
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
    types["CreativeServingDecisionIn"] = t.struct(
        {
            "networkPolicyCompliance": t.proxy(
                renames["PolicyComplianceIn"]
            ).optional(),
            "detectedVendorIds": t.array(t.integer()).optional(),
            "lastStatusUpdate": t.string().optional(),
            "platformPolicyCompliance": t.proxy(
                renames["PolicyComplianceIn"]
            ).optional(),
            "detectedClickThroughUrls": t.array(t.string()).optional(),
            "detectedAttributes": t.array(t.string()).optional(),
            "detectedDomains": t.array(t.string()).optional(),
            "adTechnologyProviders": t.proxy(
                renames["AdTechnologyProvidersIn"]
            ).optional(),
            "detectedAdvertisers": t.array(
                t.proxy(renames["AdvertiserAndBrandIn"])
            ).optional(),
            "russiaPolicyCompliance": t.proxy(renames["PolicyComplianceIn"]).optional(),
            "detectedLanguages": t.array(t.string()).optional(),
            "detectedProductCategories": t.array(t.integer()).optional(),
            "chinaPolicyCompliance": t.proxy(renames["PolicyComplianceIn"]).optional(),
            "dealsPolicyCompliance": t.proxy(renames["PolicyComplianceIn"]).optional(),
            "detectedSensitiveCategories": t.array(t.integer()).optional(),
        }
    ).named(renames["CreativeServingDecisionIn"])
    types["CreativeServingDecisionOut"] = t.struct(
        {
            "networkPolicyCompliance": t.proxy(
                renames["PolicyComplianceOut"]
            ).optional(),
            "detectedVendorIds": t.array(t.integer()).optional(),
            "lastStatusUpdate": t.string().optional(),
            "platformPolicyCompliance": t.proxy(
                renames["PolicyComplianceOut"]
            ).optional(),
            "detectedClickThroughUrls": t.array(t.string()).optional(),
            "detectedAttributes": t.array(t.string()).optional(),
            "detectedDomains": t.array(t.string()).optional(),
            "adTechnologyProviders": t.proxy(
                renames["AdTechnologyProvidersOut"]
            ).optional(),
            "detectedAdvertisers": t.array(
                t.proxy(renames["AdvertiserAndBrandOut"])
            ).optional(),
            "russiaPolicyCompliance": t.proxy(
                renames["PolicyComplianceOut"]
            ).optional(),
            "detectedLanguages": t.array(t.string()).optional(),
            "detectedProductCategories": t.array(t.integer()).optional(),
            "chinaPolicyCompliance": t.proxy(renames["PolicyComplianceOut"]).optional(),
            "dealsPolicyCompliance": t.proxy(renames["PolicyComplianceOut"]).optional(),
            "detectedSensitiveCategories": t.array(t.integer()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeServingDecisionOut"])
    types["DestinationNotCrawlableEvidenceIn"] = t.struct(
        {
            "crawledUrl": t.string().optional(),
            "crawlTime": t.string().optional(),
            "reason": t.string().optional(),
        }
    ).named(renames["DestinationNotCrawlableEvidenceIn"])
    types["DestinationNotCrawlableEvidenceOut"] = t.struct(
        {
            "crawledUrl": t.string().optional(),
            "crawlTime": t.string().optional(),
            "reason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DestinationNotCrawlableEvidenceOut"])
    types["HttpCallEvidenceIn"] = t.struct(
        {"urls": t.array(t.string()).optional()}
    ).named(renames["HttpCallEvidenceIn"])
    types["HttpCallEvidenceOut"] = t.struct(
        {
            "urls": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpCallEvidenceOut"])
    types["PretargetingConfigIn"] = t.struct(
        {
            "minimumViewabilityDecile": t.integer().optional(),
            "webTargeting": t.proxy(renames["StringTargetingDimensionIn"]).optional(),
            "maximumQps": t.string().optional(),
            "displayName": t.string().optional(),
            "includedLanguages": t.array(t.string()).optional(),
            "appTargeting": t.proxy(renames["AppTargetingIn"]).optional(),
            "includedPlatforms": t.array(t.string()).optional(),
            "allowedUserTargetingModes": t.array(t.string()).optional(),
            "includedEnvironments": t.array(t.string()).optional(),
            "interstitialTargeting": t.string().optional(),
            "publisherTargeting": t.proxy(
                renames["StringTargetingDimensionIn"]
            ).optional(),
            "excludedContentLabelIds": t.array(t.string()).optional(),
            "geoTargeting": t.proxy(renames["NumericTargetingDimensionIn"]).optional(),
            "includedFormats": t.array(t.string()).optional(),
            "includedMobileOperatingSystemIds": t.array(t.string()).optional(),
            "includedCreativeDimensions": t.array(
                t.proxy(renames["CreativeDimensionsIn"])
            ).optional(),
            "verticalTargeting": t.proxy(
                renames["NumericTargetingDimensionIn"]
            ).optional(),
            "userListTargeting": t.proxy(
                renames["NumericTargetingDimensionIn"]
            ).optional(),
            "includedUserIdTypes": t.array(t.string()).optional(),
        }
    ).named(renames["PretargetingConfigIn"])
    types["PretargetingConfigOut"] = t.struct(
        {
            "name": t.string().optional(),
            "minimumViewabilityDecile": t.integer().optional(),
            "webTargeting": t.proxy(renames["StringTargetingDimensionOut"]).optional(),
            "maximumQps": t.string().optional(),
            "displayName": t.string().optional(),
            "includedLanguages": t.array(t.string()).optional(),
            "appTargeting": t.proxy(renames["AppTargetingOut"]).optional(),
            "includedPlatforms": t.array(t.string()).optional(),
            "allowedUserTargetingModes": t.array(t.string()).optional(),
            "state": t.string().optional(),
            "includedEnvironments": t.array(t.string()).optional(),
            "interstitialTargeting": t.string().optional(),
            "publisherTargeting": t.proxy(
                renames["StringTargetingDimensionOut"]
            ).optional(),
            "excludedContentLabelIds": t.array(t.string()).optional(),
            "geoTargeting": t.proxy(renames["NumericTargetingDimensionOut"]).optional(),
            "includedFormats": t.array(t.string()).optional(),
            "billingId": t.string().optional(),
            "invalidGeoIds": t.array(t.string()).optional(),
            "includedMobileOperatingSystemIds": t.array(t.string()).optional(),
            "includedCreativeDimensions": t.array(
                t.proxy(renames["CreativeDimensionsOut"])
            ).optional(),
            "verticalTargeting": t.proxy(
                renames["NumericTargetingDimensionOut"]
            ).optional(),
            "userListTargeting": t.proxy(
                renames["NumericTargetingDimensionOut"]
            ).optional(),
            "includedUserIdTypes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PretargetingConfigOut"])
    types["DomainCallEvidenceIn"] = t.struct(
        {
            "totalHttpCallCount": t.integer().optional(),
            "topHttpCallDomains": t.array(t.proxy(renames["DomainCallsIn"])).optional(),
        }
    ).named(renames["DomainCallEvidenceIn"])
    types["DomainCallEvidenceOut"] = t.struct(
        {
            "totalHttpCallCount": t.integer().optional(),
            "topHttpCallDomains": t.array(
                t.proxy(renames["DomainCallsOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DomainCallEvidenceOut"])
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
    types["WatchCreativesRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["WatchCreativesRequestIn"]
    )
    types["WatchCreativesRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["WatchCreativesRequestOut"])
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
    types["DateIn"] = t.struct(
        {
            "month": t.integer().optional(),
            "day": t.integer().optional(),
            "year": t.integer().optional(),
        }
    ).named(renames["DateIn"])
    types["DateOut"] = t.struct(
        {
            "month": t.integer().optional(),
            "day": t.integer().optional(),
            "year": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
    types["PolicyTopicEvidenceIn"] = t.struct(
        {
            "downloadSize": t.proxy(renames["DownloadSizeEvidenceIn"]).optional(),
            "destinationNotWorking": t.proxy(
                renames["DestinationNotWorkingEvidenceIn"]
            ).optional(),
            "httpCookie": t.proxy(renames["HttpCookieEvidenceIn"]).optional(),
            "destinationNotCrawlable": t.proxy(
                renames["DestinationNotCrawlableEvidenceIn"]
            ).optional(),
            "httpCall": t.proxy(renames["HttpCallEvidenceIn"]).optional(),
            "destinationUrl": t.proxy(renames["DestinationUrlEvidenceIn"]).optional(),
            "domainCall": t.proxy(renames["DomainCallEvidenceIn"]).optional(),
        }
    ).named(renames["PolicyTopicEvidenceIn"])
    types["PolicyTopicEvidenceOut"] = t.struct(
        {
            "downloadSize": t.proxy(renames["DownloadSizeEvidenceOut"]).optional(),
            "destinationNotWorking": t.proxy(
                renames["DestinationNotWorkingEvidenceOut"]
            ).optional(),
            "httpCookie": t.proxy(renames["HttpCookieEvidenceOut"]).optional(),
            "destinationNotCrawlable": t.proxy(
                renames["DestinationNotCrawlableEvidenceOut"]
            ).optional(),
            "httpCall": t.proxy(renames["HttpCallEvidenceOut"]).optional(),
            "destinationUrl": t.proxy(renames["DestinationUrlEvidenceOut"]).optional(),
            "domainCall": t.proxy(renames["DomainCallEvidenceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyTopicEvidenceOut"])
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
    types["DestinationNotWorkingEvidenceIn"] = t.struct(
        {
            "lastCheckTime": t.string().optional(),
            "urlRejected": t.string().optional(),
            "httpError": t.integer().optional(),
            "redirectionError": t.string().optional(),
            "platform": t.string().optional(),
            "expandedUrl": t.string().optional(),
            "dnsError": t.string().optional(),
            "invalidPage": t.string().optional(),
        }
    ).named(renames["DestinationNotWorkingEvidenceIn"])
    types["DestinationNotWorkingEvidenceOut"] = t.struct(
        {
            "lastCheckTime": t.string().optional(),
            "urlRejected": t.string().optional(),
            "httpError": t.integer().optional(),
            "redirectionError": t.string().optional(),
            "platform": t.string().optional(),
            "expandedUrl": t.string().optional(),
            "dnsError": t.string().optional(),
            "invalidPage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DestinationNotWorkingEvidenceOut"])
    types["UserListIn"] = t.struct(
        {
            "description": t.string().optional(),
            "urlRestriction": t.proxy(renames["UrlRestrictionIn"]),
            "membershipDurationDays": t.string(),
            "displayName": t.string(),
        }
    ).named(renames["UserListIn"])
    types["UserListOut"] = t.struct(
        {
            "description": t.string().optional(),
            "urlRestriction": t.proxy(renames["UrlRestrictionOut"]),
            "membershipDurationDays": t.string(),
            "status": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserListOut"])
    types["SuspendPretargetingConfigRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["SuspendPretargetingConfigRequestIn"])
    types["SuspendPretargetingConfigRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SuspendPretargetingConfigRequestOut"])
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
    types["DestinationUrlEvidenceIn"] = t.struct(
        {"destinationUrl": t.string().optional()}
    ).named(renames["DestinationUrlEvidenceIn"])
    types["DestinationUrlEvidenceOut"] = t.struct(
        {
            "destinationUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DestinationUrlEvidenceOut"])
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
    types["AdTechnologyProvidersIn"] = t.struct(
        {
            "detectedProviderIds": t.array(t.string()).optional(),
            "unidentifiedProviderDomains": t.array(t.string()).optional(),
            "detectedGvlIds": t.array(t.string()).optional(),
        }
    ).named(renames["AdTechnologyProvidersIn"])
    types["AdTechnologyProvidersOut"] = t.struct(
        {
            "detectedProviderIds": t.array(t.string()).optional(),
            "unidentifiedProviderDomains": t.array(t.string()).optional(),
            "detectedGvlIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdTechnologyProvidersOut"])
    types["EndpointIn"] = t.struct(
        {
            "maximumQps": t.string().optional(),
            "tradingLocation": t.string().optional(),
            "bidProtocol": t.string().optional(),
        }
    ).named(renames["EndpointIn"])
    types["EndpointOut"] = t.struct(
        {
            "name": t.string().optional(),
            "maximumQps": t.string().optional(),
            "tradingLocation": t.string().optional(),
            "url": t.string().optional(),
            "bidProtocol": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EndpointOut"])
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
    types["PolicyTopicEntryIn"] = t.struct(
        {
            "helpCenterUrl": t.string().optional(),
            "missingCertificate": t.boolean().optional(),
            "policyTopic": t.string().optional(),
            "evidences": t.array(t.proxy(renames["PolicyTopicEvidenceIn"])).optional(),
        }
    ).named(renames["PolicyTopicEntryIn"])
    types["PolicyTopicEntryOut"] = t.struct(
        {
            "helpCenterUrl": t.string().optional(),
            "missingCertificate": t.boolean().optional(),
            "policyTopic": t.string().optional(),
            "evidences": t.array(t.proxy(renames["PolicyTopicEvidenceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyTopicEntryOut"])
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
    types["BidderIn"] = t.struct({"_": t.string().optional()}).named(
        renames["BidderIn"]
    )
    types["BidderOut"] = t.struct(
        {
            "name": t.string().optional(),
            "cookieMatchingNetworkId": t.string().optional(),
            "bypassNonguaranteedDealsPretargeting": t.boolean().optional(),
            "cookieMatchingUrl": t.string().optional(),
            "dealsBillingId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BidderOut"])
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
    types["RemoveTargetedPublishersRequestIn"] = t.struct(
        {"publisherIds": t.array(t.string()).optional()}
    ).named(renames["RemoveTargetedPublishersRequestIn"])
    types["RemoveTargetedPublishersRequestOut"] = t.struct(
        {
            "publisherIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveTargetedPublishersRequestOut"])
    types["RemoveTargetedAppsRequestIn"] = t.struct(
        {"appIds": t.array(t.string()).optional()}
    ).named(renames["RemoveTargetedAppsRequestIn"])
    types["RemoveTargetedAppsRequestOut"] = t.struct(
        {
            "appIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveTargetedAppsRequestOut"])
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
    types["HtmlContentIn"] = t.struct(
        {
            "height": t.integer().optional(),
            "snippet": t.string().optional(),
            "width": t.integer().optional(),
        }
    ).named(renames["HtmlContentIn"])
    types["HtmlContentOut"] = t.struct(
        {
            "height": t.integer().optional(),
            "snippet": t.string().optional(),
            "width": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HtmlContentOut"])
    types["BuyerIn"] = t.struct({"_": t.string().optional()}).named(renames["BuyerIn"])
    types["BuyerOut"] = t.struct(
        {
            "billingIds": t.array(t.string()).optional(),
            "activeCreativeCount": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "maximumActiveCreativeCount": t.string().optional(),
            "bidder": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuyerOut"])
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
    types["RemoveTargetedSitesRequestIn"] = t.struct(
        {"sites": t.array(t.string()).optional()}
    ).named(renames["RemoveTargetedSitesRequestIn"])
    types["RemoveTargetedSitesRequestOut"] = t.struct(
        {
            "sites": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveTargetedSitesRequestOut"])
    types["VideoMetadataIn"] = t.struct(
        {
            "isVpaid": t.boolean().optional(),
            "vastVersion": t.string().optional(),
            "isValidVast": t.boolean().optional(),
            "duration": t.string().optional(),
            "skipOffset": t.string().optional(),
            "mediaFiles": t.array(t.proxy(renames["MediaFileIn"])).optional(),
        }
    ).named(renames["VideoMetadataIn"])
    types["VideoMetadataOut"] = t.struct(
        {
            "isVpaid": t.boolean().optional(),
            "vastVersion": t.string().optional(),
            "isValidVast": t.boolean().optional(),
            "duration": t.string().optional(),
            "skipOffset": t.string().optional(),
            "mediaFiles": t.array(t.proxy(renames["MediaFileOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoMetadataOut"])

    functions = {}
    functions["buyersList"] = realtimebidding.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BuyerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersGetRemarketingTag"] = realtimebidding.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BuyerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersGet"] = realtimebidding.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BuyerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersCreativesCreate"] = realtimebidding.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "view": t.string().optional(),
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
                "name": t.string(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersCreativesPatch"] = realtimebidding.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "view": t.string().optional(),
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
                "name": t.string(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreativeOut"]),
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
    functions["biddersList"] = realtimebidding.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BidderOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersGet"] = realtimebidding.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BidderOut"]),
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
    functions["biddersPretargetingConfigsAddTargetedSites"] = realtimebidding.post(
        "v1/{pretargetingConfig}:removeTargetedPublishers",
        t.struct(
            {
                "pretargetingConfig": t.string(),
                "publisherIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PretargetingConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPretargetingConfigsPatch"] = realtimebidding.post(
        "v1/{pretargetingConfig}:removeTargetedPublishers",
        t.struct(
            {
                "pretargetingConfig": t.string(),
                "publisherIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PretargetingConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPretargetingConfigsAddTargetedPublishers"] = realtimebidding.post(
        "v1/{pretargetingConfig}:removeTargetedPublishers",
        t.struct(
            {
                "pretargetingConfig": t.string(),
                "publisherIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PretargetingConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPretargetingConfigsGet"] = realtimebidding.post(
        "v1/{pretargetingConfig}:removeTargetedPublishers",
        t.struct(
            {
                "pretargetingConfig": t.string(),
                "publisherIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PretargetingConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPretargetingConfigsList"] = realtimebidding.post(
        "v1/{pretargetingConfig}:removeTargetedPublishers",
        t.struct(
            {
                "pretargetingConfig": t.string(),
                "publisherIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PretargetingConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPretargetingConfigsRemoveTargetedApps"] = realtimebidding.post(
        "v1/{pretargetingConfig}:removeTargetedPublishers",
        t.struct(
            {
                "pretargetingConfig": t.string(),
                "publisherIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PretargetingConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPretargetingConfigsActivate"] = realtimebidding.post(
        "v1/{pretargetingConfig}:removeTargetedPublishers",
        t.struct(
            {
                "pretargetingConfig": t.string(),
                "publisherIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PretargetingConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPretargetingConfigsAddTargetedApps"] = realtimebidding.post(
        "v1/{pretargetingConfig}:removeTargetedPublishers",
        t.struct(
            {
                "pretargetingConfig": t.string(),
                "publisherIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PretargetingConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPretargetingConfigsDelete"] = realtimebidding.post(
        "v1/{pretargetingConfig}:removeTargetedPublishers",
        t.struct(
            {
                "pretargetingConfig": t.string(),
                "publisherIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PretargetingConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPretargetingConfigsCreate"] = realtimebidding.post(
        "v1/{pretargetingConfig}:removeTargetedPublishers",
        t.struct(
            {
                "pretargetingConfig": t.string(),
                "publisherIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PretargetingConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPretargetingConfigsSuspend"] = realtimebidding.post(
        "v1/{pretargetingConfig}:removeTargetedPublishers",
        t.struct(
            {
                "pretargetingConfig": t.string(),
                "publisherIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PretargetingConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPretargetingConfigsRemoveTargetedSites"] = realtimebidding.post(
        "v1/{pretargetingConfig}:removeTargetedPublishers",
        t.struct(
            {
                "pretargetingConfig": t.string(),
                "publisherIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PretargetingConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "biddersPretargetingConfigsRemoveTargetedPublishers"
    ] = realtimebidding.post(
        "v1/{pretargetingConfig}:removeTargetedPublishers",
        t.struct(
            {
                "pretargetingConfig": t.string(),
                "publisherIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PretargetingConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersEndpointsPatch"] = realtimebidding.get(
        "v1/{parent}/endpoints",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEndpointsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPublisherConnectionsBatchApprove"] = realtimebidding.get(
        "v1/{parent}/publisherConnections",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPublisherConnectionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPublisherConnectionsGet"] = realtimebidding.get(
        "v1/{parent}/publisherConnections",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPublisherConnectionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPublisherConnectionsBatchReject"] = realtimebidding.get(
        "v1/{parent}/publisherConnections",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPublisherConnectionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPublisherConnectionsList"] = realtimebidding.get(
        "v1/{parent}/publisherConnections",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPublisherConnectionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="realtimebidding",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
