from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_searchconsole() -> Import:
    searchconsole = HTTPRuntime("https://searchconsole.googleapis.com/")

    renames = {
        "ErrorResponse": "_searchconsole_1_ErrorResponse",
        "UrlInspectionResultIn": "_searchconsole_2_UrlInspectionResultIn",
        "UrlInspectionResultOut": "_searchconsole_3_UrlInspectionResultOut",
        "WmxSitemapContentIn": "_searchconsole_4_WmxSitemapContentIn",
        "WmxSitemapContentOut": "_searchconsole_5_WmxSitemapContentOut",
        "MobileFriendlyIssueIn": "_searchconsole_6_MobileFriendlyIssueIn",
        "MobileFriendlyIssueOut": "_searchconsole_7_MobileFriendlyIssueOut",
        "AmpInspectionResultIn": "_searchconsole_8_AmpInspectionResultIn",
        "AmpInspectionResultOut": "_searchconsole_9_AmpInspectionResultOut",
        "RunMobileFriendlyTestRequestIn": "_searchconsole_10_RunMobileFriendlyTestRequestIn",
        "RunMobileFriendlyTestRequestOut": "_searchconsole_11_RunMobileFriendlyTestRequestOut",
        "BlockedResourceIn": "_searchconsole_12_BlockedResourceIn",
        "BlockedResourceOut": "_searchconsole_13_BlockedResourceOut",
        "ItemIn": "_searchconsole_14_ItemIn",
        "ItemOut": "_searchconsole_15_ItemOut",
        "MobileUsabilityIssueIn": "_searchconsole_16_MobileUsabilityIssueIn",
        "MobileUsabilityIssueOut": "_searchconsole_17_MobileUsabilityIssueOut",
        "DetectedItemsIn": "_searchconsole_18_DetectedItemsIn",
        "DetectedItemsOut": "_searchconsole_19_DetectedItemsOut",
        "InspectUrlIndexResponseIn": "_searchconsole_20_InspectUrlIndexResponseIn",
        "InspectUrlIndexResponseOut": "_searchconsole_21_InspectUrlIndexResponseOut",
        "ApiDimensionFilterGroupIn": "_searchconsole_22_ApiDimensionFilterGroupIn",
        "ApiDimensionFilterGroupOut": "_searchconsole_23_ApiDimensionFilterGroupOut",
        "AmpIssueIn": "_searchconsole_24_AmpIssueIn",
        "AmpIssueOut": "_searchconsole_25_AmpIssueOut",
        "SitemapsListResponseIn": "_searchconsole_26_SitemapsListResponseIn",
        "SitemapsListResponseOut": "_searchconsole_27_SitemapsListResponseOut",
        "ImageIn": "_searchconsole_28_ImageIn",
        "ImageOut": "_searchconsole_29_ImageOut",
        "RunMobileFriendlyTestResponseIn": "_searchconsole_30_RunMobileFriendlyTestResponseIn",
        "RunMobileFriendlyTestResponseOut": "_searchconsole_31_RunMobileFriendlyTestResponseOut",
        "ApiDataRowIn": "_searchconsole_32_ApiDataRowIn",
        "ApiDataRowOut": "_searchconsole_33_ApiDataRowOut",
        "RichResultsInspectionResultIn": "_searchconsole_34_RichResultsInspectionResultIn",
        "RichResultsInspectionResultOut": "_searchconsole_35_RichResultsInspectionResultOut",
        "SearchAnalyticsQueryRequestIn": "_searchconsole_36_SearchAnalyticsQueryRequestIn",
        "SearchAnalyticsQueryRequestOut": "_searchconsole_37_SearchAnalyticsQueryRequestOut",
        "MobileUsabilityInspectionResultIn": "_searchconsole_38_MobileUsabilityInspectionResultIn",
        "MobileUsabilityInspectionResultOut": "_searchconsole_39_MobileUsabilityInspectionResultOut",
        "WmxSitemapIn": "_searchconsole_40_WmxSitemapIn",
        "WmxSitemapOut": "_searchconsole_41_WmxSitemapOut",
        "SitesListResponseIn": "_searchconsole_42_SitesListResponseIn",
        "SitesListResponseOut": "_searchconsole_43_SitesListResponseOut",
        "WmxSiteIn": "_searchconsole_44_WmxSiteIn",
        "WmxSiteOut": "_searchconsole_45_WmxSiteOut",
        "ApiDimensionFilterIn": "_searchconsole_46_ApiDimensionFilterIn",
        "ApiDimensionFilterOut": "_searchconsole_47_ApiDimensionFilterOut",
        "InspectUrlIndexRequestIn": "_searchconsole_48_InspectUrlIndexRequestIn",
        "InspectUrlIndexRequestOut": "_searchconsole_49_InspectUrlIndexRequestOut",
        "ResourceIssueIn": "_searchconsole_50_ResourceIssueIn",
        "ResourceIssueOut": "_searchconsole_51_ResourceIssueOut",
        "IndexStatusInspectionResultIn": "_searchconsole_52_IndexStatusInspectionResultIn",
        "IndexStatusInspectionResultOut": "_searchconsole_53_IndexStatusInspectionResultOut",
        "TestStatusIn": "_searchconsole_54_TestStatusIn",
        "TestStatusOut": "_searchconsole_55_TestStatusOut",
        "RichResultsIssueIn": "_searchconsole_56_RichResultsIssueIn",
        "RichResultsIssueOut": "_searchconsole_57_RichResultsIssueOut",
        "SearchAnalyticsQueryResponseIn": "_searchconsole_58_SearchAnalyticsQueryResponseIn",
        "SearchAnalyticsQueryResponseOut": "_searchconsole_59_SearchAnalyticsQueryResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["UrlInspectionResultIn"] = t.struct(
        {
            "ampResult": t.proxy(renames["AmpInspectionResultIn"]).optional(),
            "mobileUsabilityResult": t.proxy(
                renames["MobileUsabilityInspectionResultIn"]
            ).optional(),
            "inspectionResultLink": t.string().optional(),
            "indexStatusResult": t.proxy(
                renames["IndexStatusInspectionResultIn"]
            ).optional(),
            "richResultsResult": t.proxy(
                renames["RichResultsInspectionResultIn"]
            ).optional(),
        }
    ).named(renames["UrlInspectionResultIn"])
    types["UrlInspectionResultOut"] = t.struct(
        {
            "ampResult": t.proxy(renames["AmpInspectionResultOut"]).optional(),
            "mobileUsabilityResult": t.proxy(
                renames["MobileUsabilityInspectionResultOut"]
            ).optional(),
            "inspectionResultLink": t.string().optional(),
            "indexStatusResult": t.proxy(
                renames["IndexStatusInspectionResultOut"]
            ).optional(),
            "richResultsResult": t.proxy(
                renames["RichResultsInspectionResultOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UrlInspectionResultOut"])
    types["WmxSitemapContentIn"] = t.struct(
        {
            "submitted": t.string().optional(),
            "type": t.string().optional(),
            "indexed": t.string().optional(),
        }
    ).named(renames["WmxSitemapContentIn"])
    types["WmxSitemapContentOut"] = t.struct(
        {
            "submitted": t.string().optional(),
            "type": t.string().optional(),
            "indexed": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WmxSitemapContentOut"])
    types["MobileFriendlyIssueIn"] = t.struct({"rule": t.string().optional()}).named(
        renames["MobileFriendlyIssueIn"]
    )
    types["MobileFriendlyIssueOut"] = t.struct(
        {
            "rule": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MobileFriendlyIssueOut"])
    types["AmpInspectionResultIn"] = t.struct(
        {
            "pageFetchState": t.string().optional(),
            "issues": t.array(t.proxy(renames["AmpIssueIn"])).optional(),
            "robotsTxtState": t.string().optional(),
            "lastCrawlTime": t.string().optional(),
            "ampIndexStatusVerdict": t.string().optional(),
            "verdict": t.string().optional(),
            "indexingState": t.string().optional(),
            "ampUrl": t.string().optional(),
        }
    ).named(renames["AmpInspectionResultIn"])
    types["AmpInspectionResultOut"] = t.struct(
        {
            "pageFetchState": t.string().optional(),
            "issues": t.array(t.proxy(renames["AmpIssueOut"])).optional(),
            "robotsTxtState": t.string().optional(),
            "lastCrawlTime": t.string().optional(),
            "ampIndexStatusVerdict": t.string().optional(),
            "verdict": t.string().optional(),
            "indexingState": t.string().optional(),
            "ampUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AmpInspectionResultOut"])
    types["RunMobileFriendlyTestRequestIn"] = t.struct(
        {"requestScreenshot": t.boolean().optional(), "url": t.string().optional()}
    ).named(renames["RunMobileFriendlyTestRequestIn"])
    types["RunMobileFriendlyTestRequestOut"] = t.struct(
        {
            "requestScreenshot": t.boolean().optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunMobileFriendlyTestRequestOut"])
    types["BlockedResourceIn"] = t.struct({"url": t.string().optional()}).named(
        renames["BlockedResourceIn"]
    )
    types["BlockedResourceOut"] = t.struct(
        {
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BlockedResourceOut"])
    types["ItemIn"] = t.struct(
        {
            "name": t.string().optional(),
            "issues": t.array(t.proxy(renames["RichResultsIssueIn"])).optional(),
        }
    ).named(renames["ItemIn"])
    types["ItemOut"] = t.struct(
        {
            "name": t.string().optional(),
            "issues": t.array(t.proxy(renames["RichResultsIssueOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ItemOut"])
    types["MobileUsabilityIssueIn"] = t.struct(
        {
            "message": t.string().optional(),
            "severity": t.string().optional(),
            "issueType": t.string().optional(),
        }
    ).named(renames["MobileUsabilityIssueIn"])
    types["MobileUsabilityIssueOut"] = t.struct(
        {
            "message": t.string().optional(),
            "severity": t.string().optional(),
            "issueType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MobileUsabilityIssueOut"])
    types["DetectedItemsIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["ItemIn"])).optional(),
            "richResultType": t.string().optional(),
        }
    ).named(renames["DetectedItemsIn"])
    types["DetectedItemsOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["ItemOut"])).optional(),
            "richResultType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DetectedItemsOut"])
    types["InspectUrlIndexResponseIn"] = t.struct(
        {"inspectionResult": t.proxy(renames["UrlInspectionResultIn"]).optional()}
    ).named(renames["InspectUrlIndexResponseIn"])
    types["InspectUrlIndexResponseOut"] = t.struct(
        {
            "inspectionResult": t.proxy(renames["UrlInspectionResultOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InspectUrlIndexResponseOut"])
    types["ApiDimensionFilterGroupIn"] = t.struct(
        {
            "filters": t.array(t.proxy(renames["ApiDimensionFilterIn"])),
            "groupType": t.string(),
        }
    ).named(renames["ApiDimensionFilterGroupIn"])
    types["ApiDimensionFilterGroupOut"] = t.struct(
        {
            "filters": t.array(t.proxy(renames["ApiDimensionFilterOut"])),
            "groupType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApiDimensionFilterGroupOut"])
    types["AmpIssueIn"] = t.struct(
        {"issueMessage": t.string().optional(), "severity": t.string().optional()}
    ).named(renames["AmpIssueIn"])
    types["AmpIssueOut"] = t.struct(
        {
            "issueMessage": t.string().optional(),
            "severity": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AmpIssueOut"])
    types["SitemapsListResponseIn"] = t.struct(
        {"sitemap": t.array(t.proxy(renames["WmxSitemapIn"])).optional()}
    ).named(renames["SitemapsListResponseIn"])
    types["SitemapsListResponseOut"] = t.struct(
        {
            "sitemap": t.array(t.proxy(renames["WmxSitemapOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SitemapsListResponseOut"])
    types["ImageIn"] = t.struct(
        {"mimeType": t.string().optional(), "data": t.string().optional()}
    ).named(renames["ImageIn"])
    types["ImageOut"] = t.struct(
        {
            "mimeType": t.string().optional(),
            "data": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageOut"])
    types["RunMobileFriendlyTestResponseIn"] = t.struct(
        {
            "testStatus": t.proxy(renames["TestStatusIn"]).optional(),
            "screenshot": t.proxy(renames["ImageIn"]).optional(),
            "resourceIssues": t.array(t.proxy(renames["ResourceIssueIn"])).optional(),
            "mobileFriendlyIssues": t.array(
                t.proxy(renames["MobileFriendlyIssueIn"])
            ).optional(),
            "mobileFriendliness": t.string().optional(),
        }
    ).named(renames["RunMobileFriendlyTestResponseIn"])
    types["RunMobileFriendlyTestResponseOut"] = t.struct(
        {
            "testStatus": t.proxy(renames["TestStatusOut"]).optional(),
            "screenshot": t.proxy(renames["ImageOut"]).optional(),
            "resourceIssues": t.array(t.proxy(renames["ResourceIssueOut"])).optional(),
            "mobileFriendlyIssues": t.array(
                t.proxy(renames["MobileFriendlyIssueOut"])
            ).optional(),
            "mobileFriendliness": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunMobileFriendlyTestResponseOut"])
    types["ApiDataRowIn"] = t.struct(
        {
            "ctr": t.number(),
            "impressions": t.number(),
            "clicks": t.number(),
            "position": t.number(),
            "keys": t.array(t.string()),
        }
    ).named(renames["ApiDataRowIn"])
    types["ApiDataRowOut"] = t.struct(
        {
            "ctr": t.number(),
            "impressions": t.number(),
            "clicks": t.number(),
            "position": t.number(),
            "keys": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApiDataRowOut"])
    types["RichResultsInspectionResultIn"] = t.struct(
        {
            "detectedItems": t.array(t.proxy(renames["DetectedItemsIn"])).optional(),
            "verdict": t.string().optional(),
        }
    ).named(renames["RichResultsInspectionResultIn"])
    types["RichResultsInspectionResultOut"] = t.struct(
        {
            "detectedItems": t.array(t.proxy(renames["DetectedItemsOut"])).optional(),
            "verdict": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RichResultsInspectionResultOut"])
    types["SearchAnalyticsQueryRequestIn"] = t.struct(
        {
            "endDate": t.string().optional(),
            "dimensionFilterGroups": t.array(
                t.proxy(renames["ApiDimensionFilterGroupIn"])
            ).optional(),
            "searchType": t.string().optional(),
            "startRow": t.integer().optional(),
            "startDate": t.string().optional(),
            "aggregationType": t.string().optional(),
            "type": t.string().optional(),
            "dataState": t.string().optional(),
            "dimensions": t.array(t.string()).optional(),
            "rowLimit": t.integer().optional(),
        }
    ).named(renames["SearchAnalyticsQueryRequestIn"])
    types["SearchAnalyticsQueryRequestOut"] = t.struct(
        {
            "endDate": t.string().optional(),
            "dimensionFilterGroups": t.array(
                t.proxy(renames["ApiDimensionFilterGroupOut"])
            ).optional(),
            "searchType": t.string().optional(),
            "startRow": t.integer().optional(),
            "startDate": t.string().optional(),
            "aggregationType": t.string().optional(),
            "type": t.string().optional(),
            "dataState": t.string().optional(),
            "dimensions": t.array(t.string()).optional(),
            "rowLimit": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchAnalyticsQueryRequestOut"])
    types["MobileUsabilityInspectionResultIn"] = t.struct(
        {
            "issues": t.array(t.proxy(renames["MobileUsabilityIssueIn"])).optional(),
            "verdict": t.string().optional(),
        }
    ).named(renames["MobileUsabilityInspectionResultIn"])
    types["MobileUsabilityInspectionResultOut"] = t.struct(
        {
            "issues": t.array(t.proxy(renames["MobileUsabilityIssueOut"])).optional(),
            "verdict": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MobileUsabilityInspectionResultOut"])
    types["WmxSitemapIn"] = t.struct(
        {
            "lastSubmitted": t.string().optional(),
            "isPending": t.boolean().optional(),
            "isSitemapsIndex": t.boolean().optional(),
            "contents": t.array(t.proxy(renames["WmxSitemapContentIn"])).optional(),
            "type": t.string().optional(),
            "errors": t.string().optional(),
            "warnings": t.string().optional(),
            "lastDownloaded": t.string().optional(),
            "path": t.string().optional(),
        }
    ).named(renames["WmxSitemapIn"])
    types["WmxSitemapOut"] = t.struct(
        {
            "lastSubmitted": t.string().optional(),
            "isPending": t.boolean().optional(),
            "isSitemapsIndex": t.boolean().optional(),
            "contents": t.array(t.proxy(renames["WmxSitemapContentOut"])).optional(),
            "type": t.string().optional(),
            "errors": t.string().optional(),
            "warnings": t.string().optional(),
            "lastDownloaded": t.string().optional(),
            "path": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WmxSitemapOut"])
    types["SitesListResponseIn"] = t.struct(
        {"siteEntry": t.array(t.proxy(renames["WmxSiteIn"])).optional()}
    ).named(renames["SitesListResponseIn"])
    types["SitesListResponseOut"] = t.struct(
        {
            "siteEntry": t.array(t.proxy(renames["WmxSiteOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SitesListResponseOut"])
    types["WmxSiteIn"] = t.struct(
        {"siteUrl": t.string().optional(), "permissionLevel": t.string().optional()}
    ).named(renames["WmxSiteIn"])
    types["WmxSiteOut"] = t.struct(
        {
            "siteUrl": t.string().optional(),
            "permissionLevel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WmxSiteOut"])
    types["ApiDimensionFilterIn"] = t.struct(
        {"operator": t.string(), "dimension": t.string(), "expression": t.string()}
    ).named(renames["ApiDimensionFilterIn"])
    types["ApiDimensionFilterOut"] = t.struct(
        {
            "operator": t.string(),
            "dimension": t.string(),
            "expression": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApiDimensionFilterOut"])
    types["InspectUrlIndexRequestIn"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "inspectionUrl": t.string(),
            "siteUrl": t.string(),
        }
    ).named(renames["InspectUrlIndexRequestIn"])
    types["InspectUrlIndexRequestOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "inspectionUrl": t.string(),
            "siteUrl": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InspectUrlIndexRequestOut"])
    types["ResourceIssueIn"] = t.struct(
        {"blockedResource": t.proxy(renames["BlockedResourceIn"]).optional()}
    ).named(renames["ResourceIssueIn"])
    types["ResourceIssueOut"] = t.struct(
        {
            "blockedResource": t.proxy(renames["BlockedResourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceIssueOut"])
    types["IndexStatusInspectionResultIn"] = t.struct(
        {
            "sitemap": t.array(t.string()).optional(),
            "pageFetchState": t.string().optional(),
            "userCanonical": t.string().optional(),
            "referringUrls": t.array(t.string()).optional(),
            "indexingState": t.string().optional(),
            "coverageState": t.string().optional(),
            "crawledAs": t.string().optional(),
            "googleCanonical": t.string().optional(),
            "robotsTxtState": t.string().optional(),
            "verdict": t.string().optional(),
            "lastCrawlTime": t.string().optional(),
        }
    ).named(renames["IndexStatusInspectionResultIn"])
    types["IndexStatusInspectionResultOut"] = t.struct(
        {
            "sitemap": t.array(t.string()).optional(),
            "pageFetchState": t.string().optional(),
            "userCanonical": t.string().optional(),
            "referringUrls": t.array(t.string()).optional(),
            "indexingState": t.string().optional(),
            "coverageState": t.string().optional(),
            "crawledAs": t.string().optional(),
            "googleCanonical": t.string().optional(),
            "robotsTxtState": t.string().optional(),
            "verdict": t.string().optional(),
            "lastCrawlTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IndexStatusInspectionResultOut"])
    types["TestStatusIn"] = t.struct(
        {"details": t.string().optional(), "status": t.string().optional()}
    ).named(renames["TestStatusIn"])
    types["TestStatusOut"] = t.struct(
        {
            "details": t.string().optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestStatusOut"])
    types["RichResultsIssueIn"] = t.struct(
        {"severity": t.string().optional(), "issueMessage": t.string().optional()}
    ).named(renames["RichResultsIssueIn"])
    types["RichResultsIssueOut"] = t.struct(
        {
            "severity": t.string().optional(),
            "issueMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RichResultsIssueOut"])
    types["SearchAnalyticsQueryResponseIn"] = t.struct(
        {
            "responseAggregationType": t.string().optional(),
            "rows": t.array(t.proxy(renames["ApiDataRowIn"])).optional(),
        }
    ).named(renames["SearchAnalyticsQueryResponseIn"])
    types["SearchAnalyticsQueryResponseOut"] = t.struct(
        {
            "responseAggregationType": t.string().optional(),
            "rows": t.array(t.proxy(renames["ApiDataRowOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchAnalyticsQueryResponseOut"])

    functions = {}
    functions["searchanalyticsQuery"] = searchconsole.post(
        "webmasters/v3/sites/{siteUrl}/searchAnalytics/query",
        t.struct(
            {
                "siteUrl": t.string().optional(),
                "endDate": t.string().optional(),
                "dimensionFilterGroups": t.array(
                    t.proxy(renames["ApiDimensionFilterGroupIn"])
                ).optional(),
                "searchType": t.string().optional(),
                "startRow": t.integer().optional(),
                "startDate": t.string().optional(),
                "aggregationType": t.string().optional(),
                "type": t.string().optional(),
                "dataState": t.string().optional(),
                "dimensions": t.array(t.string()).optional(),
                "rowLimit": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchAnalyticsQueryResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sitemapsDelete"] = searchconsole.get(
        "webmasters/v3/sites/{siteUrl}/sitemaps",
        t.struct(
            {
                "siteUrl": t.string().optional(),
                "sitemapIndex": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SitemapsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sitemapsSubmit"] = searchconsole.get(
        "webmasters/v3/sites/{siteUrl}/sitemaps",
        t.struct(
            {
                "siteUrl": t.string().optional(),
                "sitemapIndex": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SitemapsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sitemapsGet"] = searchconsole.get(
        "webmasters/v3/sites/{siteUrl}/sitemaps",
        t.struct(
            {
                "siteUrl": t.string().optional(),
                "sitemapIndex": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SitemapsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sitemapsList"] = searchconsole.get(
        "webmasters/v3/sites/{siteUrl}/sitemaps",
        t.struct(
            {
                "siteUrl": t.string().optional(),
                "sitemapIndex": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SitemapsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["urlInspectionIndexInspect"] = searchconsole.post(
        "v1/urlInspection/index:inspect",
        t.struct(
            {
                "languageCode": t.string().optional(),
                "inspectionUrl": t.string(),
                "siteUrl": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InspectUrlIndexResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["urlTestingToolsMobileFriendlyTestRun"] = searchconsole.post(
        "v1/urlTestingTools/mobileFriendlyTest:run",
        t.struct(
            {
                "requestScreenshot": t.boolean().optional(),
                "url": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RunMobileFriendlyTestResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sitesList"] = searchconsole.delete(
        "webmasters/v3/sites/{siteUrl}",
        t.struct({"siteUrl": t.string().optional(), "auth": t.string().optional()}),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sitesGet"] = searchconsole.delete(
        "webmasters/v3/sites/{siteUrl}",
        t.struct({"siteUrl": t.string().optional(), "auth": t.string().optional()}),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sitesAdd"] = searchconsole.delete(
        "webmasters/v3/sites/{siteUrl}",
        t.struct({"siteUrl": t.string().optional(), "auth": t.string().optional()}),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sitesDelete"] = searchconsole.delete(
        "webmasters/v3/sites/{siteUrl}",
        t.struct({"siteUrl": t.string().optional(), "auth": t.string().optional()}),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="searchconsole",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
