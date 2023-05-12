from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_realtimebidding() -> Import:
    realtimebidding = HTTPRuntime("https://realtimebidding.googleapis.com/")

    renames = {
        "ErrorResponse": "_realtimebidding_1_ErrorResponse",
        "DomainCallEvidenceIn": "_realtimebidding_2_DomainCallEvidenceIn",
        "DomainCallEvidenceOut": "_realtimebidding_3_DomainCallEvidenceOut",
        "ListPublisherConnectionsResponseIn": "_realtimebidding_4_ListPublisherConnectionsResponseIn",
        "ListPublisherConnectionsResponseOut": "_realtimebidding_5_ListPublisherConnectionsResponseOut",
        "HttpCallEvidenceIn": "_realtimebidding_6_HttpCallEvidenceIn",
        "HttpCallEvidenceOut": "_realtimebidding_7_HttpCallEvidenceOut",
        "ListEndpointsResponseIn": "_realtimebidding_8_ListEndpointsResponseIn",
        "ListEndpointsResponseOut": "_realtimebidding_9_ListEndpointsResponseOut",
        "CreativeIn": "_realtimebidding_10_CreativeIn",
        "CreativeOut": "_realtimebidding_11_CreativeOut",
        "DestinationNotWorkingEvidenceIn": "_realtimebidding_12_DestinationNotWorkingEvidenceIn",
        "DestinationNotWorkingEvidenceOut": "_realtimebidding_13_DestinationNotWorkingEvidenceOut",
        "GetRemarketingTagResponseIn": "_realtimebidding_14_GetRemarketingTagResponseIn",
        "GetRemarketingTagResponseOut": "_realtimebidding_15_GetRemarketingTagResponseOut",
        "PolicyTopicEvidenceIn": "_realtimebidding_16_PolicyTopicEvidenceIn",
        "PolicyTopicEvidenceOut": "_realtimebidding_17_PolicyTopicEvidenceOut",
        "PublisherConnectionIn": "_realtimebidding_18_PublisherConnectionIn",
        "PublisherConnectionOut": "_realtimebidding_19_PublisherConnectionOut",
        "PretargetingConfigIn": "_realtimebidding_20_PretargetingConfigIn",
        "PretargetingConfigOut": "_realtimebidding_21_PretargetingConfigOut",
        "ListUserListsResponseIn": "_realtimebidding_22_ListUserListsResponseIn",
        "ListUserListsResponseOut": "_realtimebidding_23_ListUserListsResponseOut",
        "StringTargetingDimensionIn": "_realtimebidding_24_StringTargetingDimensionIn",
        "StringTargetingDimensionOut": "_realtimebidding_25_StringTargetingDimensionOut",
        "EmptyIn": "_realtimebidding_26_EmptyIn",
        "EmptyOut": "_realtimebidding_27_EmptyOut",
        "DomainCallsIn": "_realtimebidding_28_DomainCallsIn",
        "DomainCallsOut": "_realtimebidding_29_DomainCallsOut",
        "AddTargetedAppsRequestIn": "_realtimebidding_30_AddTargetedAppsRequestIn",
        "AddTargetedAppsRequestOut": "_realtimebidding_31_AddTargetedAppsRequestOut",
        "HtmlContentIn": "_realtimebidding_32_HtmlContentIn",
        "HtmlContentOut": "_realtimebidding_33_HtmlContentOut",
        "UrlRestrictionIn": "_realtimebidding_34_UrlRestrictionIn",
        "UrlRestrictionOut": "_realtimebidding_35_UrlRestrictionOut",
        "WatchCreativesResponseIn": "_realtimebidding_36_WatchCreativesResponseIn",
        "WatchCreativesResponseOut": "_realtimebidding_37_WatchCreativesResponseOut",
        "NumericTargetingDimensionIn": "_realtimebidding_38_NumericTargetingDimensionIn",
        "NumericTargetingDimensionOut": "_realtimebidding_39_NumericTargetingDimensionOut",
        "NativeContentIn": "_realtimebidding_40_NativeContentIn",
        "NativeContentOut": "_realtimebidding_41_NativeContentOut",
        "ListPretargetingConfigsResponseIn": "_realtimebidding_42_ListPretargetingConfigsResponseIn",
        "ListPretargetingConfigsResponseOut": "_realtimebidding_43_ListPretargetingConfigsResponseOut",
        "ListBiddersResponseIn": "_realtimebidding_44_ListBiddersResponseIn",
        "ListBiddersResponseOut": "_realtimebidding_45_ListBiddersResponseOut",
        "BidderIn": "_realtimebidding_46_BidderIn",
        "BidderOut": "_realtimebidding_47_BidderOut",
        "PolicyComplianceIn": "_realtimebidding_48_PolicyComplianceIn",
        "PolicyComplianceOut": "_realtimebidding_49_PolicyComplianceOut",
        "UserListIn": "_realtimebidding_50_UserListIn",
        "UserListOut": "_realtimebidding_51_UserListOut",
        "DestinationUrlEvidenceIn": "_realtimebidding_52_DestinationUrlEvidenceIn",
        "DestinationUrlEvidenceOut": "_realtimebidding_53_DestinationUrlEvidenceOut",
        "ListBuyersResponseIn": "_realtimebidding_54_ListBuyersResponseIn",
        "ListBuyersResponseOut": "_realtimebidding_55_ListBuyersResponseOut",
        "DateIn": "_realtimebidding_56_DateIn",
        "DateOut": "_realtimebidding_57_DateOut",
        "ActivatePretargetingConfigRequestIn": "_realtimebidding_58_ActivatePretargetingConfigRequestIn",
        "ActivatePretargetingConfigRequestOut": "_realtimebidding_59_ActivatePretargetingConfigRequestOut",
        "VideoMetadataIn": "_realtimebidding_60_VideoMetadataIn",
        "VideoMetadataOut": "_realtimebidding_61_VideoMetadataOut",
        "BatchRejectPublisherConnectionsResponseIn": "_realtimebidding_62_BatchRejectPublisherConnectionsResponseIn",
        "BatchRejectPublisherConnectionsResponseOut": "_realtimebidding_63_BatchRejectPublisherConnectionsResponseOut",
        "VideoContentIn": "_realtimebidding_64_VideoContentIn",
        "VideoContentOut": "_realtimebidding_65_VideoContentOut",
        "BatchRejectPublisherConnectionsRequestIn": "_realtimebidding_66_BatchRejectPublisherConnectionsRequestIn",
        "BatchRejectPublisherConnectionsRequestOut": "_realtimebidding_67_BatchRejectPublisherConnectionsRequestOut",
        "RemoveTargetedPublishersRequestIn": "_realtimebidding_68_RemoveTargetedPublishersRequestIn",
        "RemoveTargetedPublishersRequestOut": "_realtimebidding_69_RemoveTargetedPublishersRequestOut",
        "CreativeDimensionsIn": "_realtimebidding_70_CreativeDimensionsIn",
        "CreativeDimensionsOut": "_realtimebidding_71_CreativeDimensionsOut",
        "RemoveTargetedSitesRequestIn": "_realtimebidding_72_RemoveTargetedSitesRequestIn",
        "RemoveTargetedSitesRequestOut": "_realtimebidding_73_RemoveTargetedSitesRequestOut",
        "RemoveTargetedAppsRequestIn": "_realtimebidding_74_RemoveTargetedAppsRequestIn",
        "RemoveTargetedAppsRequestOut": "_realtimebidding_75_RemoveTargetedAppsRequestOut",
        "AdTechnologyProvidersIn": "_realtimebidding_76_AdTechnologyProvidersIn",
        "AdTechnologyProvidersOut": "_realtimebidding_77_AdTechnologyProvidersOut",
        "WatchCreativesRequestIn": "_realtimebidding_78_WatchCreativesRequestIn",
        "WatchCreativesRequestOut": "_realtimebidding_79_WatchCreativesRequestOut",
        "AdvertiserAndBrandIn": "_realtimebidding_80_AdvertiserAndBrandIn",
        "AdvertiserAndBrandOut": "_realtimebidding_81_AdvertiserAndBrandOut",
        "AppTargetingIn": "_realtimebidding_82_AppTargetingIn",
        "AppTargetingOut": "_realtimebidding_83_AppTargetingOut",
        "BatchApprovePublisherConnectionsRequestIn": "_realtimebidding_84_BatchApprovePublisherConnectionsRequestIn",
        "BatchApprovePublisherConnectionsRequestOut": "_realtimebidding_85_BatchApprovePublisherConnectionsRequestOut",
        "AddTargetedSitesRequestIn": "_realtimebidding_86_AddTargetedSitesRequestIn",
        "AddTargetedSitesRequestOut": "_realtimebidding_87_AddTargetedSitesRequestOut",
        "BatchApprovePublisherConnectionsResponseIn": "_realtimebidding_88_BatchApprovePublisherConnectionsResponseIn",
        "BatchApprovePublisherConnectionsResponseOut": "_realtimebidding_89_BatchApprovePublisherConnectionsResponseOut",
        "DownloadSizeEvidenceIn": "_realtimebidding_90_DownloadSizeEvidenceIn",
        "DownloadSizeEvidenceOut": "_realtimebidding_91_DownloadSizeEvidenceOut",
        "ListCreativesResponseIn": "_realtimebidding_92_ListCreativesResponseIn",
        "ListCreativesResponseOut": "_realtimebidding_93_ListCreativesResponseOut",
        "SuspendPretargetingConfigRequestIn": "_realtimebidding_94_SuspendPretargetingConfigRequestIn",
        "SuspendPretargetingConfigRequestOut": "_realtimebidding_95_SuspendPretargetingConfigRequestOut",
        "AddTargetedPublishersRequestIn": "_realtimebidding_96_AddTargetedPublishersRequestIn",
        "AddTargetedPublishersRequestOut": "_realtimebidding_97_AddTargetedPublishersRequestOut",
        "ImageIn": "_realtimebidding_98_ImageIn",
        "ImageOut": "_realtimebidding_99_ImageOut",
        "DestinationNotCrawlableEvidenceIn": "_realtimebidding_100_DestinationNotCrawlableEvidenceIn",
        "DestinationNotCrawlableEvidenceOut": "_realtimebidding_101_DestinationNotCrawlableEvidenceOut",
        "OpenUserListRequestIn": "_realtimebidding_102_OpenUserListRequestIn",
        "OpenUserListRequestOut": "_realtimebidding_103_OpenUserListRequestOut",
        "MediaFileIn": "_realtimebidding_104_MediaFileIn",
        "MediaFileOut": "_realtimebidding_105_MediaFileOut",
        "HttpCookieEvidenceIn": "_realtimebidding_106_HttpCookieEvidenceIn",
        "HttpCookieEvidenceOut": "_realtimebidding_107_HttpCookieEvidenceOut",
        "PolicyTopicEntryIn": "_realtimebidding_108_PolicyTopicEntryIn",
        "PolicyTopicEntryOut": "_realtimebidding_109_PolicyTopicEntryOut",
        "CloseUserListRequestIn": "_realtimebidding_110_CloseUserListRequestIn",
        "CloseUserListRequestOut": "_realtimebidding_111_CloseUserListRequestOut",
        "UrlDownloadSizeIn": "_realtimebidding_112_UrlDownloadSizeIn",
        "UrlDownloadSizeOut": "_realtimebidding_113_UrlDownloadSizeOut",
        "CreativeServingDecisionIn": "_realtimebidding_114_CreativeServingDecisionIn",
        "CreativeServingDecisionOut": "_realtimebidding_115_CreativeServingDecisionOut",
        "EndpointIn": "_realtimebidding_116_EndpointIn",
        "EndpointOut": "_realtimebidding_117_EndpointOut",
        "BuyerIn": "_realtimebidding_118_BuyerIn",
        "BuyerOut": "_realtimebidding_119_BuyerOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["HttpCallEvidenceIn"] = t.struct(
        {"urls": t.array(t.string()).optional()}
    ).named(renames["HttpCallEvidenceIn"])
    types["HttpCallEvidenceOut"] = t.struct(
        {
            "urls": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpCallEvidenceOut"])
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
            "impressionTrackingUrls": t.array(t.string()).optional(),
            "declaredClickThroughUrls": t.array(t.string()).optional(),
            "restrictedCategories": t.array(t.string()).optional(),
            "declaredVendorIds": t.array(t.integer()).optional(),
            "renderUrl": t.string().optional(),
            "declaredRestrictedCategories": t.array(t.string()).optional(),
            "advertiserName": t.string().optional(),
            "creativeId": t.string().optional(),
            "declaredAttributes": t.array(t.string()).optional(),
            "html": t.proxy(renames["HtmlContentIn"]).optional(),
            "agencyId": t.string().optional(),
            "adChoicesDestinationUrl": t.string().optional(),
            "video": t.proxy(renames["VideoContentIn"]).optional(),
            "native": t.proxy(renames["NativeContentIn"]).optional(),
        }
    ).named(renames["CreativeIn"])
    types["CreativeOut"] = t.struct(
        {
            "accountId": t.string().optional(),
            "dealIds": t.array(t.string()).optional(),
            "impressionTrackingUrls": t.array(t.string()).optional(),
            "declaredClickThroughUrls": t.array(t.string()).optional(),
            "restrictedCategories": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "declaredVendorIds": t.array(t.integer()).optional(),
            "renderUrl": t.string().optional(),
            "declaredRestrictedCategories": t.array(t.string()).optional(),
            "advertiserName": t.string().optional(),
            "creativeId": t.string().optional(),
            "declaredAttributes": t.array(t.string()).optional(),
            "creativeFormat": t.string().optional(),
            "html": t.proxy(renames["HtmlContentOut"]).optional(),
            "creativeServingDecision": t.proxy(
                renames["CreativeServingDecisionOut"]
            ).optional(),
            "agencyId": t.string().optional(),
            "apiUpdateTime": t.string().optional(),
            "adChoicesDestinationUrl": t.string().optional(),
            "video": t.proxy(renames["VideoContentOut"]).optional(),
            "native": t.proxy(renames["NativeContentOut"]).optional(),
            "version": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeOut"])
    types["DestinationNotWorkingEvidenceIn"] = t.struct(
        {
            "urlRejected": t.string().optional(),
            "dnsError": t.string().optional(),
            "platform": t.string().optional(),
            "expandedUrl": t.string().optional(),
            "redirectionError": t.string().optional(),
            "invalidPage": t.string().optional(),
            "lastCheckTime": t.string().optional(),
            "httpError": t.integer().optional(),
        }
    ).named(renames["DestinationNotWorkingEvidenceIn"])
    types["DestinationNotWorkingEvidenceOut"] = t.struct(
        {
            "urlRejected": t.string().optional(),
            "dnsError": t.string().optional(),
            "platform": t.string().optional(),
            "expandedUrl": t.string().optional(),
            "redirectionError": t.string().optional(),
            "invalidPage": t.string().optional(),
            "lastCheckTime": t.string().optional(),
            "httpError": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DestinationNotWorkingEvidenceOut"])
    types["GetRemarketingTagResponseIn"] = t.struct(
        {"snippet": t.string().optional()}
    ).named(renames["GetRemarketingTagResponseIn"])
    types["GetRemarketingTagResponseOut"] = t.struct(
        {
            "snippet": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetRemarketingTagResponseOut"])
    types["PolicyTopicEvidenceIn"] = t.struct(
        {
            "httpCall": t.proxy(renames["HttpCallEvidenceIn"]).optional(),
            "destinationUrl": t.proxy(renames["DestinationUrlEvidenceIn"]).optional(),
            "httpCookie": t.proxy(renames["HttpCookieEvidenceIn"]).optional(),
            "downloadSize": t.proxy(renames["DownloadSizeEvidenceIn"]).optional(),
            "domainCall": t.proxy(renames["DomainCallEvidenceIn"]).optional(),
            "destinationNotCrawlable": t.proxy(
                renames["DestinationNotCrawlableEvidenceIn"]
            ).optional(),
            "destinationNotWorking": t.proxy(
                renames["DestinationNotWorkingEvidenceIn"]
            ).optional(),
        }
    ).named(renames["PolicyTopicEvidenceIn"])
    types["PolicyTopicEvidenceOut"] = t.struct(
        {
            "httpCall": t.proxy(renames["HttpCallEvidenceOut"]).optional(),
            "destinationUrl": t.proxy(renames["DestinationUrlEvidenceOut"]).optional(),
            "httpCookie": t.proxy(renames["HttpCookieEvidenceOut"]).optional(),
            "downloadSize": t.proxy(renames["DownloadSizeEvidenceOut"]).optional(),
            "domainCall": t.proxy(renames["DomainCallEvidenceOut"]).optional(),
            "destinationNotCrawlable": t.proxy(
                renames["DestinationNotCrawlableEvidenceOut"]
            ).optional(),
            "destinationNotWorking": t.proxy(
                renames["DestinationNotWorkingEvidenceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyTopicEvidenceOut"])
    types["PublisherConnectionIn"] = t.struct(
        {"biddingState": t.string().optional()}
    ).named(renames["PublisherConnectionIn"])
    types["PublisherConnectionOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "publisherPlatform": t.string().optional(),
            "biddingState": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublisherConnectionOut"])
    types["PretargetingConfigIn"] = t.struct(
        {
            "includedUserIdTypes": t.array(t.string()).optional(),
            "includedFormats": t.array(t.string()).optional(),
            "includedEnvironments": t.array(t.string()).optional(),
            "minimumViewabilityDecile": t.integer().optional(),
            "userListTargeting": t.proxy(
                renames["NumericTargetingDimensionIn"]
            ).optional(),
            "displayName": t.string().optional(),
            "publisherTargeting": t.proxy(
                renames["StringTargetingDimensionIn"]
            ).optional(),
            "geoTargeting": t.proxy(renames["NumericTargetingDimensionIn"]).optional(),
            "allowedUserTargetingModes": t.array(t.string()).optional(),
            "maximumQps": t.string().optional(),
            "webTargeting": t.proxy(renames["StringTargetingDimensionIn"]).optional(),
            "includedPlatforms": t.array(t.string()).optional(),
            "excludedContentLabelIds": t.array(t.string()).optional(),
            "includedCreativeDimensions": t.array(
                t.proxy(renames["CreativeDimensionsIn"])
            ).optional(),
            "verticalTargeting": t.proxy(
                renames["NumericTargetingDimensionIn"]
            ).optional(),
            "includedLanguages": t.array(t.string()).optional(),
            "appTargeting": t.proxy(renames["AppTargetingIn"]).optional(),
            "includedMobileOperatingSystemIds": t.array(t.string()).optional(),
            "interstitialTargeting": t.string().optional(),
        }
    ).named(renames["PretargetingConfigIn"])
    types["PretargetingConfigOut"] = t.struct(
        {
            "includedUserIdTypes": t.array(t.string()).optional(),
            "includedFormats": t.array(t.string()).optional(),
            "includedEnvironments": t.array(t.string()).optional(),
            "minimumViewabilityDecile": t.integer().optional(),
            "userListTargeting": t.proxy(
                renames["NumericTargetingDimensionOut"]
            ).optional(),
            "displayName": t.string().optional(),
            "publisherTargeting": t.proxy(
                renames["StringTargetingDimensionOut"]
            ).optional(),
            "invalidGeoIds": t.array(t.string()).optional(),
            "geoTargeting": t.proxy(renames["NumericTargetingDimensionOut"]).optional(),
            "state": t.string().optional(),
            "allowedUserTargetingModes": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "maximumQps": t.string().optional(),
            "webTargeting": t.proxy(renames["StringTargetingDimensionOut"]).optional(),
            "includedPlatforms": t.array(t.string()).optional(),
            "excludedContentLabelIds": t.array(t.string()).optional(),
            "includedCreativeDimensions": t.array(
                t.proxy(renames["CreativeDimensionsOut"])
            ).optional(),
            "verticalTargeting": t.proxy(
                renames["NumericTargetingDimensionOut"]
            ).optional(),
            "includedLanguages": t.array(t.string()).optional(),
            "billingId": t.string().optional(),
            "appTargeting": t.proxy(renames["AppTargetingOut"]).optional(),
            "includedMobileOperatingSystemIds": t.array(t.string()).optional(),
            "interstitialTargeting": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PretargetingConfigOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["UrlRestrictionIn"] = t.struct(
        {
            "startDate": t.proxy(renames["DateIn"]).optional(),
            "restrictionType": t.string().optional(),
            "endDate": t.proxy(renames["DateIn"]).optional(),
            "url": t.string(),
        }
    ).named(renames["UrlRestrictionIn"])
    types["UrlRestrictionOut"] = t.struct(
        {
            "startDate": t.proxy(renames["DateOut"]).optional(),
            "restrictionType": t.string().optional(),
            "endDate": t.proxy(renames["DateOut"]).optional(),
            "url": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UrlRestrictionOut"])
    types["WatchCreativesResponseIn"] = t.struct(
        {"subscription": t.string().optional(), "topic": t.string().optional()}
    ).named(renames["WatchCreativesResponseIn"])
    types["WatchCreativesResponseOut"] = t.struct(
        {
            "subscription": t.string().optional(),
            "topic": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WatchCreativesResponseOut"])
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
    types["NativeContentIn"] = t.struct(
        {
            "starRating": t.number().optional(),
            "logo": t.proxy(renames["ImageIn"]).optional(),
            "priceDisplayText": t.string().optional(),
            "advertiserName": t.string().optional(),
            "image": t.proxy(renames["ImageIn"]).optional(),
            "clickLinkUrl": t.string().optional(),
            "videoVastXml": t.string().optional(),
            "callToAction": t.string().optional(),
            "body": t.string().optional(),
            "headline": t.string().optional(),
            "videoUrl": t.string().optional(),
            "appIcon": t.proxy(renames["ImageIn"]).optional(),
            "clickTrackingUrl": t.string().optional(),
        }
    ).named(renames["NativeContentIn"])
    types["NativeContentOut"] = t.struct(
        {
            "starRating": t.number().optional(),
            "logo": t.proxy(renames["ImageOut"]).optional(),
            "priceDisplayText": t.string().optional(),
            "advertiserName": t.string().optional(),
            "image": t.proxy(renames["ImageOut"]).optional(),
            "clickLinkUrl": t.string().optional(),
            "videoVastXml": t.string().optional(),
            "callToAction": t.string().optional(),
            "body": t.string().optional(),
            "headline": t.string().optional(),
            "videoUrl": t.string().optional(),
            "appIcon": t.proxy(renames["ImageOut"]).optional(),
            "clickTrackingUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NativeContentOut"])
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
    types["BidderIn"] = t.struct({"_": t.string().optional()}).named(
        renames["BidderIn"]
    )
    types["BidderOut"] = t.struct(
        {
            "cookieMatchingUrl": t.string().optional(),
            "cookieMatchingNetworkId": t.string().optional(),
            "name": t.string().optional(),
            "bypassNonguaranteedDealsPretargeting": t.boolean().optional(),
            "dealsBillingId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BidderOut"])
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
    types["UserListIn"] = t.struct(
        {
            "description": t.string().optional(),
            "membershipDurationDays": t.string(),
            "displayName": t.string(),
            "urlRestriction": t.proxy(renames["UrlRestrictionIn"]),
        }
    ).named(renames["UserListIn"])
    types["UserListOut"] = t.struct(
        {
            "description": t.string().optional(),
            "membershipDurationDays": t.string(),
            "status": t.string().optional(),
            "displayName": t.string(),
            "urlRestriction": t.proxy(renames["UrlRestrictionOut"]),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserListOut"])
    types["DestinationUrlEvidenceIn"] = t.struct(
        {"destinationUrl": t.string().optional()}
    ).named(renames["DestinationUrlEvidenceIn"])
    types["DestinationUrlEvidenceOut"] = t.struct(
        {
            "destinationUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DestinationUrlEvidenceOut"])
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
    types["DateIn"] = t.struct(
        {
            "year": t.integer().optional(),
            "month": t.integer().optional(),
            "day": t.integer().optional(),
        }
    ).named(renames["DateIn"])
    types["DateOut"] = t.struct(
        {
            "year": t.integer().optional(),
            "month": t.integer().optional(),
            "day": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
    types["ActivatePretargetingConfigRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ActivatePretargetingConfigRequestIn"])
    types["ActivatePretargetingConfigRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ActivatePretargetingConfigRequestOut"])
    types["VideoMetadataIn"] = t.struct(
        {
            "isValidVast": t.boolean().optional(),
            "duration": t.string().optional(),
            "vastVersion": t.string().optional(),
            "isVpaid": t.boolean().optional(),
            "skipOffset": t.string().optional(),
            "mediaFiles": t.array(t.proxy(renames["MediaFileIn"])).optional(),
        }
    ).named(renames["VideoMetadataIn"])
    types["VideoMetadataOut"] = t.struct(
        {
            "isValidVast": t.boolean().optional(),
            "duration": t.string().optional(),
            "vastVersion": t.string().optional(),
            "isVpaid": t.boolean().optional(),
            "skipOffset": t.string().optional(),
            "mediaFiles": t.array(t.proxy(renames["MediaFileOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoMetadataOut"])
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
        {"videoUrl": t.string().optional(), "videoVastXml": t.string().optional()}
    ).named(renames["VideoContentIn"])
    types["VideoContentOut"] = t.struct(
        {
            "videoUrl": t.string().optional(),
            "videoMetadata": t.proxy(renames["VideoMetadataOut"]).optional(),
            "videoVastXml": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoContentOut"])
    types["BatchRejectPublisherConnectionsRequestIn"] = t.struct(
        {"names": t.array(t.string())}
    ).named(renames["BatchRejectPublisherConnectionsRequestIn"])
    types["BatchRejectPublisherConnectionsRequestOut"] = t.struct(
        {
            "names": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchRejectPublisherConnectionsRequestOut"])
    types["RemoveTargetedPublishersRequestIn"] = t.struct(
        {"publisherIds": t.array(t.string()).optional()}
    ).named(renames["RemoveTargetedPublishersRequestIn"])
    types["RemoveTargetedPublishersRequestOut"] = t.struct(
        {
            "publisherIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveTargetedPublishersRequestOut"])
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
    types["RemoveTargetedSitesRequestIn"] = t.struct(
        {"sites": t.array(t.string()).optional()}
    ).named(renames["RemoveTargetedSitesRequestIn"])
    types["RemoveTargetedSitesRequestOut"] = t.struct(
        {
            "sites": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveTargetedSitesRequestOut"])
    types["RemoveTargetedAppsRequestIn"] = t.struct(
        {"appIds": t.array(t.string()).optional()}
    ).named(renames["RemoveTargetedAppsRequestIn"])
    types["RemoveTargetedAppsRequestOut"] = t.struct(
        {
            "appIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveTargetedAppsRequestOut"])
    types["AdTechnologyProvidersIn"] = t.struct(
        {
            "detectedProviderIds": t.array(t.string()).optional(),
            "detectedGvlIds": t.array(t.string()).optional(),
            "unidentifiedProviderDomains": t.array(t.string()).optional(),
        }
    ).named(renames["AdTechnologyProvidersIn"])
    types["AdTechnologyProvidersOut"] = t.struct(
        {
            "detectedProviderIds": t.array(t.string()).optional(),
            "detectedGvlIds": t.array(t.string()).optional(),
            "unidentifiedProviderDomains": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdTechnologyProvidersOut"])
    types["WatchCreativesRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["WatchCreativesRequestIn"]
    )
    types["WatchCreativesRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["WatchCreativesRequestOut"])
    types["AdvertiserAndBrandIn"] = t.struct(
        {
            "advertiserName": t.string().optional(),
            "brandName": t.string().optional(),
            "advertiserId": t.string().optional(),
            "brandId": t.string().optional(),
        }
    ).named(renames["AdvertiserAndBrandIn"])
    types["AdvertiserAndBrandOut"] = t.struct(
        {
            "advertiserName": t.string().optional(),
            "brandName": t.string().optional(),
            "advertiserId": t.string().optional(),
            "brandId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdvertiserAndBrandOut"])
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
    types["AddTargetedSitesRequestIn"] = t.struct(
        {"sites": t.array(t.string()).optional(), "targetingMode": t.string()}
    ).named(renames["AddTargetedSitesRequestIn"])
    types["AddTargetedSitesRequestOut"] = t.struct(
        {
            "sites": t.array(t.string()).optional(),
            "targetingMode": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddTargetedSitesRequestOut"])
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
    types["SuspendPretargetingConfigRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["SuspendPretargetingConfigRequestIn"])
    types["SuspendPretargetingConfigRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SuspendPretargetingConfigRequestOut"])
    types["AddTargetedPublishersRequestIn"] = t.struct(
        {"targetingMode": t.string(), "publisherIds": t.array(t.string()).optional()}
    ).named(renames["AddTargetedPublishersRequestIn"])
    types["AddTargetedPublishersRequestOut"] = t.struct(
        {
            "targetingMode": t.string(),
            "publisherIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddTargetedPublishersRequestOut"])
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
    types["DestinationNotCrawlableEvidenceIn"] = t.struct(
        {
            "crawledUrl": t.string().optional(),
            "reason": t.string().optional(),
            "crawlTime": t.string().optional(),
        }
    ).named(renames["DestinationNotCrawlableEvidenceIn"])
    types["DestinationNotCrawlableEvidenceOut"] = t.struct(
        {
            "crawledUrl": t.string().optional(),
            "reason": t.string().optional(),
            "crawlTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DestinationNotCrawlableEvidenceOut"])
    types["OpenUserListRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OpenUserListRequestIn"]
    )
    types["OpenUserListRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["OpenUserListRequestOut"])
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
    types["PolicyTopicEntryIn"] = t.struct(
        {
            "evidences": t.array(t.proxy(renames["PolicyTopicEvidenceIn"])).optional(),
            "missingCertificate": t.boolean().optional(),
            "helpCenterUrl": t.string().optional(),
            "policyTopic": t.string().optional(),
        }
    ).named(renames["PolicyTopicEntryIn"])
    types["PolicyTopicEntryOut"] = t.struct(
        {
            "evidences": t.array(t.proxy(renames["PolicyTopicEvidenceOut"])).optional(),
            "missingCertificate": t.boolean().optional(),
            "helpCenterUrl": t.string().optional(),
            "policyTopic": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyTopicEntryOut"])
    types["CloseUserListRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CloseUserListRequestIn"]
    )
    types["CloseUserListRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CloseUserListRequestOut"])
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
    types["CreativeServingDecisionIn"] = t.struct(
        {
            "detectedAttributes": t.array(t.string()).optional(),
            "detectedProductCategories": t.array(t.integer()).optional(),
            "detectedClickThroughUrls": t.array(t.string()).optional(),
            "chinaPolicyCompliance": t.proxy(renames["PolicyComplianceIn"]).optional(),
            "dealsPolicyCompliance": t.proxy(renames["PolicyComplianceIn"]).optional(),
            "networkPolicyCompliance": t.proxy(
                renames["PolicyComplianceIn"]
            ).optional(),
            "lastStatusUpdate": t.string().optional(),
            "detectedVendorIds": t.array(t.integer()).optional(),
            "platformPolicyCompliance": t.proxy(
                renames["PolicyComplianceIn"]
            ).optional(),
            "detectedLanguages": t.array(t.string()).optional(),
            "detectedSensitiveCategories": t.array(t.integer()).optional(),
            "adTechnologyProviders": t.proxy(
                renames["AdTechnologyProvidersIn"]
            ).optional(),
            "russiaPolicyCompliance": t.proxy(renames["PolicyComplianceIn"]).optional(),
            "detectedAdvertisers": t.array(
                t.proxy(renames["AdvertiserAndBrandIn"])
            ).optional(),
            "detectedDomains": t.array(t.string()).optional(),
        }
    ).named(renames["CreativeServingDecisionIn"])
    types["CreativeServingDecisionOut"] = t.struct(
        {
            "detectedAttributes": t.array(t.string()).optional(),
            "detectedProductCategories": t.array(t.integer()).optional(),
            "detectedClickThroughUrls": t.array(t.string()).optional(),
            "chinaPolicyCompliance": t.proxy(renames["PolicyComplianceOut"]).optional(),
            "dealsPolicyCompliance": t.proxy(renames["PolicyComplianceOut"]).optional(),
            "networkPolicyCompliance": t.proxy(
                renames["PolicyComplianceOut"]
            ).optional(),
            "lastStatusUpdate": t.string().optional(),
            "detectedVendorIds": t.array(t.integer()).optional(),
            "platformPolicyCompliance": t.proxy(
                renames["PolicyComplianceOut"]
            ).optional(),
            "detectedLanguages": t.array(t.string()).optional(),
            "detectedSensitiveCategories": t.array(t.integer()).optional(),
            "adTechnologyProviders": t.proxy(
                renames["AdTechnologyProvidersOut"]
            ).optional(),
            "russiaPolicyCompliance": t.proxy(
                renames["PolicyComplianceOut"]
            ).optional(),
            "detectedAdvertisers": t.array(
                t.proxy(renames["AdvertiserAndBrandOut"])
            ).optional(),
            "detectedDomains": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreativeServingDecisionOut"])
    types["EndpointIn"] = t.struct(
        {
            "tradingLocation": t.string().optional(),
            "maximumQps": t.string().optional(),
            "bidProtocol": t.string().optional(),
        }
    ).named(renames["EndpointIn"])
    types["EndpointOut"] = t.struct(
        {
            "tradingLocation": t.string().optional(),
            "maximumQps": t.string().optional(),
            "name": t.string().optional(),
            "url": t.string().optional(),
            "bidProtocol": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EndpointOut"])
    types["BuyerIn"] = t.struct({"_": t.string().optional()}).named(renames["BuyerIn"])
    types["BuyerOut"] = t.struct(
        {
            "bidder": t.string().optional(),
            "activeCreativeCount": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "billingIds": t.array(t.string()).optional(),
            "maximumActiveCreativeCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuyerOut"])

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
    functions["buyersCreativesGet"] = realtimebidding.get(
        "v1/{parent}/creatives",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCreativesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersCreativesCreate"] = realtimebidding.get(
        "v1/{parent}/creatives",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCreativesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersCreativesPatch"] = realtimebidding.get(
        "v1/{parent}/creatives",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCreativesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["buyersCreativesList"] = realtimebidding.get(
        "v1/{parent}/creatives",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCreativesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
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
    functions["biddersPublisherConnectionsList"] = realtimebidding.post(
        "v1/{parent}/publisherConnections:batchApprove",
        t.struct(
            {
                "parent": t.string(),
                "names": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchApprovePublisherConnectionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPublisherConnectionsGet"] = realtimebidding.post(
        "v1/{parent}/publisherConnections:batchApprove",
        t.struct(
            {
                "parent": t.string(),
                "names": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchApprovePublisherConnectionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPublisherConnectionsBatchReject"] = realtimebidding.post(
        "v1/{parent}/publisherConnections:batchApprove",
        t.struct(
            {
                "parent": t.string(),
                "names": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchApprovePublisherConnectionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPublisherConnectionsBatchApprove"] = realtimebidding.post(
        "v1/{parent}/publisherConnections:batchApprove",
        t.struct(
            {
                "parent": t.string(),
                "names": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchApprovePublisherConnectionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPretargetingConfigsPatch"] = realtimebidding.post(
        "v1/{pretargetingConfig}:removeTargetedApps",
        t.struct(
            {
                "pretargetingConfig": t.string(),
                "appIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PretargetingConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPretargetingConfigsDelete"] = realtimebidding.post(
        "v1/{pretargetingConfig}:removeTargetedApps",
        t.struct(
            {
                "pretargetingConfig": t.string(),
                "appIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PretargetingConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPretargetingConfigsActivate"] = realtimebidding.post(
        "v1/{pretargetingConfig}:removeTargetedApps",
        t.struct(
            {
                "pretargetingConfig": t.string(),
                "appIds": t.array(t.string()).optional(),
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
        "v1/{pretargetingConfig}:removeTargetedApps",
        t.struct(
            {
                "pretargetingConfig": t.string(),
                "appIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PretargetingConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPretargetingConfigsAddTargetedApps"] = realtimebidding.post(
        "v1/{pretargetingConfig}:removeTargetedApps",
        t.struct(
            {
                "pretargetingConfig": t.string(),
                "appIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PretargetingConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPretargetingConfigsSuspend"] = realtimebidding.post(
        "v1/{pretargetingConfig}:removeTargetedApps",
        t.struct(
            {
                "pretargetingConfig": t.string(),
                "appIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PretargetingConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPretargetingConfigsGet"] = realtimebidding.post(
        "v1/{pretargetingConfig}:removeTargetedApps",
        t.struct(
            {
                "pretargetingConfig": t.string(),
                "appIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PretargetingConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPretargetingConfigsAddTargetedSites"] = realtimebidding.post(
        "v1/{pretargetingConfig}:removeTargetedApps",
        t.struct(
            {
                "pretargetingConfig": t.string(),
                "appIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PretargetingConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPretargetingConfigsRemoveTargetedSites"] = realtimebidding.post(
        "v1/{pretargetingConfig}:removeTargetedApps",
        t.struct(
            {
                "pretargetingConfig": t.string(),
                "appIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PretargetingConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPretargetingConfigsAddTargetedPublishers"] = realtimebidding.post(
        "v1/{pretargetingConfig}:removeTargetedApps",
        t.struct(
            {
                "pretargetingConfig": t.string(),
                "appIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PretargetingConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPretargetingConfigsCreate"] = realtimebidding.post(
        "v1/{pretargetingConfig}:removeTargetedApps",
        t.struct(
            {
                "pretargetingConfig": t.string(),
                "appIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PretargetingConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPretargetingConfigsList"] = realtimebidding.post(
        "v1/{pretargetingConfig}:removeTargetedApps",
        t.struct(
            {
                "pretargetingConfig": t.string(),
                "appIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PretargetingConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersPretargetingConfigsRemoveTargetedApps"] = realtimebidding.post(
        "v1/{pretargetingConfig}:removeTargetedApps",
        t.struct(
            {
                "pretargetingConfig": t.string(),
                "appIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PretargetingConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersCreativesWatch"] = realtimebidding.get(
        "v1/{parent}/creatives",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "view": t.string().optional(),
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
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "view": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCreativesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["biddersEndpointsPatch"] = realtimebidding.get(
        "v1/{parent}/endpoints",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEndpointsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="realtimebidding",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
