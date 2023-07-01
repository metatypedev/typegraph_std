from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_searchconsole():
    searchconsole = HTTPRuntime("https://searchconsole.googleapis.com/")

    renames = {
        "ErrorResponse": "_searchconsole_1_ErrorResponse",
        "RichResultsIssueIn": "_searchconsole_2_RichResultsIssueIn",
        "RichResultsIssueOut": "_searchconsole_3_RichResultsIssueOut",
        "RunMobileFriendlyTestRequestIn": "_searchconsole_4_RunMobileFriendlyTestRequestIn",
        "RunMobileFriendlyTestRequestOut": "_searchconsole_5_RunMobileFriendlyTestRequestOut",
        "RichResultsInspectionResultIn": "_searchconsole_6_RichResultsInspectionResultIn",
        "RichResultsInspectionResultOut": "_searchconsole_7_RichResultsInspectionResultOut",
        "AmpIssueIn": "_searchconsole_8_AmpIssueIn",
        "AmpIssueOut": "_searchconsole_9_AmpIssueOut",
        "InspectUrlIndexRequestIn": "_searchconsole_10_InspectUrlIndexRequestIn",
        "InspectUrlIndexRequestOut": "_searchconsole_11_InspectUrlIndexRequestOut",
        "BlockedResourceIn": "_searchconsole_12_BlockedResourceIn",
        "BlockedResourceOut": "_searchconsole_13_BlockedResourceOut",
        "WmxSitemapContentIn": "_searchconsole_14_WmxSitemapContentIn",
        "WmxSitemapContentOut": "_searchconsole_15_WmxSitemapContentOut",
        "SearchAnalyticsQueryRequestIn": "_searchconsole_16_SearchAnalyticsQueryRequestIn",
        "SearchAnalyticsQueryRequestOut": "_searchconsole_17_SearchAnalyticsQueryRequestOut",
        "ItemIn": "_searchconsole_18_ItemIn",
        "ItemOut": "_searchconsole_19_ItemOut",
        "UrlInspectionResultIn": "_searchconsole_20_UrlInspectionResultIn",
        "UrlInspectionResultOut": "_searchconsole_21_UrlInspectionResultOut",
        "ApiDimensionFilterGroupIn": "_searchconsole_22_ApiDimensionFilterGroupIn",
        "ApiDimensionFilterGroupOut": "_searchconsole_23_ApiDimensionFilterGroupOut",
        "RunMobileFriendlyTestResponseIn": "_searchconsole_24_RunMobileFriendlyTestResponseIn",
        "RunMobileFriendlyTestResponseOut": "_searchconsole_25_RunMobileFriendlyTestResponseOut",
        "WmxSiteIn": "_searchconsole_26_WmxSiteIn",
        "WmxSiteOut": "_searchconsole_27_WmxSiteOut",
        "MobileUsabilityInspectionResultIn": "_searchconsole_28_MobileUsabilityInspectionResultIn",
        "MobileUsabilityInspectionResultOut": "_searchconsole_29_MobileUsabilityInspectionResultOut",
        "ApiDataRowIn": "_searchconsole_30_ApiDataRowIn",
        "ApiDataRowOut": "_searchconsole_31_ApiDataRowOut",
        "InspectUrlIndexResponseIn": "_searchconsole_32_InspectUrlIndexResponseIn",
        "InspectUrlIndexResponseOut": "_searchconsole_33_InspectUrlIndexResponseOut",
        "AmpInspectionResultIn": "_searchconsole_34_AmpInspectionResultIn",
        "AmpInspectionResultOut": "_searchconsole_35_AmpInspectionResultOut",
        "SitemapsListResponseIn": "_searchconsole_36_SitemapsListResponseIn",
        "SitemapsListResponseOut": "_searchconsole_37_SitemapsListResponseOut",
        "SearchAnalyticsQueryResponseIn": "_searchconsole_38_SearchAnalyticsQueryResponseIn",
        "SearchAnalyticsQueryResponseOut": "_searchconsole_39_SearchAnalyticsQueryResponseOut",
        "ApiDimensionFilterIn": "_searchconsole_40_ApiDimensionFilterIn",
        "ApiDimensionFilterOut": "_searchconsole_41_ApiDimensionFilterOut",
        "WmxSitemapIn": "_searchconsole_42_WmxSitemapIn",
        "WmxSitemapOut": "_searchconsole_43_WmxSitemapOut",
        "SitesListResponseIn": "_searchconsole_44_SitesListResponseIn",
        "SitesListResponseOut": "_searchconsole_45_SitesListResponseOut",
        "MobileUsabilityIssueIn": "_searchconsole_46_MobileUsabilityIssueIn",
        "MobileUsabilityIssueOut": "_searchconsole_47_MobileUsabilityIssueOut",
        "ResourceIssueIn": "_searchconsole_48_ResourceIssueIn",
        "ResourceIssueOut": "_searchconsole_49_ResourceIssueOut",
        "ImageIn": "_searchconsole_50_ImageIn",
        "ImageOut": "_searchconsole_51_ImageOut",
        "DetectedItemsIn": "_searchconsole_52_DetectedItemsIn",
        "DetectedItemsOut": "_searchconsole_53_DetectedItemsOut",
        "TestStatusIn": "_searchconsole_54_TestStatusIn",
        "TestStatusOut": "_searchconsole_55_TestStatusOut",
        "MobileFriendlyIssueIn": "_searchconsole_56_MobileFriendlyIssueIn",
        "MobileFriendlyIssueOut": "_searchconsole_57_MobileFriendlyIssueOut",
        "IndexStatusInspectionResultIn": "_searchconsole_58_IndexStatusInspectionResultIn",
        "IndexStatusInspectionResultOut": "_searchconsole_59_IndexStatusInspectionResultOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["RichResultsIssueIn"] = t.struct(
        {"issueMessage": t.string().optional(), "severity": t.string().optional()}
    ).named(renames["RichResultsIssueIn"])
    types["RichResultsIssueOut"] = t.struct(
        {
            "issueMessage": t.string().optional(),
            "severity": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RichResultsIssueOut"])
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
    types["AmpIssueIn"] = t.struct(
        {"severity": t.string().optional(), "issueMessage": t.string().optional()}
    ).named(renames["AmpIssueIn"])
    types["AmpIssueOut"] = t.struct(
        {
            "severity": t.string().optional(),
            "issueMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AmpIssueOut"])
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
    types["BlockedResourceIn"] = t.struct({"url": t.string().optional()}).named(
        renames["BlockedResourceIn"]
    )
    types["BlockedResourceOut"] = t.struct(
        {
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BlockedResourceOut"])
    types["WmxSitemapContentIn"] = t.struct(
        {
            "indexed": t.string().optional(),
            "type": t.string().optional(),
            "submitted": t.string().optional(),
        }
    ).named(renames["WmxSitemapContentIn"])
    types["WmxSitemapContentOut"] = t.struct(
        {
            "indexed": t.string().optional(),
            "type": t.string().optional(),
            "submitted": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WmxSitemapContentOut"])
    types["SearchAnalyticsQueryRequestIn"] = t.struct(
        {
            "rowLimit": t.integer().optional(),
            "startDate": t.string().optional(),
            "aggregationType": t.string().optional(),
            "dimensions": t.array(t.string()).optional(),
            "type": t.string().optional(),
            "searchType": t.string().optional(),
            "dataState": t.string().optional(),
            "dimensionFilterGroups": t.array(
                t.proxy(renames["ApiDimensionFilterGroupIn"])
            ).optional(),
            "endDate": t.string().optional(),
            "startRow": t.integer().optional(),
        }
    ).named(renames["SearchAnalyticsQueryRequestIn"])
    types["SearchAnalyticsQueryRequestOut"] = t.struct(
        {
            "rowLimit": t.integer().optional(),
            "startDate": t.string().optional(),
            "aggregationType": t.string().optional(),
            "dimensions": t.array(t.string()).optional(),
            "type": t.string().optional(),
            "searchType": t.string().optional(),
            "dataState": t.string().optional(),
            "dimensionFilterGroups": t.array(
                t.proxy(renames["ApiDimensionFilterGroupOut"])
            ).optional(),
            "endDate": t.string().optional(),
            "startRow": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchAnalyticsQueryRequestOut"])
    types["ItemIn"] = t.struct(
        {
            "issues": t.array(t.proxy(renames["RichResultsIssueIn"])).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ItemIn"])
    types["ItemOut"] = t.struct(
        {
            "issues": t.array(t.proxy(renames["RichResultsIssueOut"])).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ItemOut"])
    types["UrlInspectionResultIn"] = t.struct(
        {
            "indexStatusResult": t.proxy(
                renames["IndexStatusInspectionResultIn"]
            ).optional(),
            "richResultsResult": t.proxy(
                renames["RichResultsInspectionResultIn"]
            ).optional(),
            "inspectionResultLink": t.string().optional(),
            "mobileUsabilityResult": t.proxy(
                renames["MobileUsabilityInspectionResultIn"]
            ).optional(),
            "ampResult": t.proxy(renames["AmpInspectionResultIn"]).optional(),
        }
    ).named(renames["UrlInspectionResultIn"])
    types["UrlInspectionResultOut"] = t.struct(
        {
            "indexStatusResult": t.proxy(
                renames["IndexStatusInspectionResultOut"]
            ).optional(),
            "richResultsResult": t.proxy(
                renames["RichResultsInspectionResultOut"]
            ).optional(),
            "inspectionResultLink": t.string().optional(),
            "mobileUsabilityResult": t.proxy(
                renames["MobileUsabilityInspectionResultOut"]
            ).optional(),
            "ampResult": t.proxy(renames["AmpInspectionResultOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UrlInspectionResultOut"])
    types["ApiDimensionFilterGroupIn"] = t.struct(
        {
            "groupType": t.string(),
            "filters": t.array(t.proxy(renames["ApiDimensionFilterIn"])),
        }
    ).named(renames["ApiDimensionFilterGroupIn"])
    types["ApiDimensionFilterGroupOut"] = t.struct(
        {
            "groupType": t.string(),
            "filters": t.array(t.proxy(renames["ApiDimensionFilterOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApiDimensionFilterGroupOut"])
    types["RunMobileFriendlyTestResponseIn"] = t.struct(
        {
            "mobileFriendliness": t.string().optional(),
            "resourceIssues": t.array(t.proxy(renames["ResourceIssueIn"])).optional(),
            "mobileFriendlyIssues": t.array(
                t.proxy(renames["MobileFriendlyIssueIn"])
            ).optional(),
            "testStatus": t.proxy(renames["TestStatusIn"]).optional(),
            "screenshot": t.proxy(renames["ImageIn"]).optional(),
        }
    ).named(renames["RunMobileFriendlyTestResponseIn"])
    types["RunMobileFriendlyTestResponseOut"] = t.struct(
        {
            "mobileFriendliness": t.string().optional(),
            "resourceIssues": t.array(t.proxy(renames["ResourceIssueOut"])).optional(),
            "mobileFriendlyIssues": t.array(
                t.proxy(renames["MobileFriendlyIssueOut"])
            ).optional(),
            "testStatus": t.proxy(renames["TestStatusOut"]).optional(),
            "screenshot": t.proxy(renames["ImageOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunMobileFriendlyTestResponseOut"])
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
    types["MobileUsabilityInspectionResultIn"] = t.struct(
        {
            "verdict": t.string().optional(),
            "issues": t.array(t.proxy(renames["MobileUsabilityIssueIn"])).optional(),
        }
    ).named(renames["MobileUsabilityInspectionResultIn"])
    types["MobileUsabilityInspectionResultOut"] = t.struct(
        {
            "verdict": t.string().optional(),
            "issues": t.array(t.proxy(renames["MobileUsabilityIssueOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MobileUsabilityInspectionResultOut"])
    types["ApiDataRowIn"] = t.struct(
        {
            "position": t.number(),
            "impressions": t.number(),
            "clicks": t.number(),
            "ctr": t.number(),
            "keys": t.array(t.string()),
        }
    ).named(renames["ApiDataRowIn"])
    types["ApiDataRowOut"] = t.struct(
        {
            "position": t.number(),
            "impressions": t.number(),
            "clicks": t.number(),
            "ctr": t.number(),
            "keys": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApiDataRowOut"])
    types["InspectUrlIndexResponseIn"] = t.struct(
        {"inspectionResult": t.proxy(renames["UrlInspectionResultIn"]).optional()}
    ).named(renames["InspectUrlIndexResponseIn"])
    types["InspectUrlIndexResponseOut"] = t.struct(
        {
            "inspectionResult": t.proxy(renames["UrlInspectionResultOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InspectUrlIndexResponseOut"])
    types["AmpInspectionResultIn"] = t.struct(
        {
            "ampUrl": t.string().optional(),
            "lastCrawlTime": t.string().optional(),
            "issues": t.array(t.proxy(renames["AmpIssueIn"])).optional(),
            "robotsTxtState": t.string().optional(),
            "verdict": t.string().optional(),
            "indexingState": t.string().optional(),
            "pageFetchState": t.string().optional(),
            "ampIndexStatusVerdict": t.string().optional(),
        }
    ).named(renames["AmpInspectionResultIn"])
    types["AmpInspectionResultOut"] = t.struct(
        {
            "ampUrl": t.string().optional(),
            "lastCrawlTime": t.string().optional(),
            "issues": t.array(t.proxy(renames["AmpIssueOut"])).optional(),
            "robotsTxtState": t.string().optional(),
            "verdict": t.string().optional(),
            "indexingState": t.string().optional(),
            "pageFetchState": t.string().optional(),
            "ampIndexStatusVerdict": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AmpInspectionResultOut"])
    types["SitemapsListResponseIn"] = t.struct(
        {"sitemap": t.array(t.proxy(renames["WmxSitemapIn"])).optional()}
    ).named(renames["SitemapsListResponseIn"])
    types["SitemapsListResponseOut"] = t.struct(
        {
            "sitemap": t.array(t.proxy(renames["WmxSitemapOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SitemapsListResponseOut"])
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
    types["WmxSitemapIn"] = t.struct(
        {
            "path": t.string().optional(),
            "isSitemapsIndex": t.boolean().optional(),
            "type": t.string().optional(),
            "isPending": t.boolean().optional(),
            "lastSubmitted": t.string().optional(),
            "warnings": t.string().optional(),
            "errors": t.string().optional(),
            "contents": t.array(t.proxy(renames["WmxSitemapContentIn"])).optional(),
            "lastDownloaded": t.string().optional(),
        }
    ).named(renames["WmxSitemapIn"])
    types["WmxSitemapOut"] = t.struct(
        {
            "path": t.string().optional(),
            "isSitemapsIndex": t.boolean().optional(),
            "type": t.string().optional(),
            "isPending": t.boolean().optional(),
            "lastSubmitted": t.string().optional(),
            "warnings": t.string().optional(),
            "errors": t.string().optional(),
            "contents": t.array(t.proxy(renames["WmxSitemapContentOut"])).optional(),
            "lastDownloaded": t.string().optional(),
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
    types["ResourceIssueIn"] = t.struct(
        {"blockedResource": t.proxy(renames["BlockedResourceIn"]).optional()}
    ).named(renames["ResourceIssueIn"])
    types["ResourceIssueOut"] = t.struct(
        {
            "blockedResource": t.proxy(renames["BlockedResourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceIssueOut"])
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
    types["DetectedItemsIn"] = t.struct(
        {
            "richResultType": t.string().optional(),
            "items": t.array(t.proxy(renames["ItemIn"])).optional(),
        }
    ).named(renames["DetectedItemsIn"])
    types["DetectedItemsOut"] = t.struct(
        {
            "richResultType": t.string().optional(),
            "items": t.array(t.proxy(renames["ItemOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DetectedItemsOut"])
    types["TestStatusIn"] = t.struct(
        {"status": t.string().optional(), "details": t.string().optional()}
    ).named(renames["TestStatusIn"])
    types["TestStatusOut"] = t.struct(
        {
            "status": t.string().optional(),
            "details": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestStatusOut"])
    types["MobileFriendlyIssueIn"] = t.struct({"rule": t.string().optional()}).named(
        renames["MobileFriendlyIssueIn"]
    )
    types["MobileFriendlyIssueOut"] = t.struct(
        {
            "rule": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MobileFriendlyIssueOut"])
    types["IndexStatusInspectionResultIn"] = t.struct(
        {
            "indexingState": t.string().optional(),
            "pageFetchState": t.string().optional(),
            "robotsTxtState": t.string().optional(),
            "referringUrls": t.array(t.string()).optional(),
            "userCanonical": t.string().optional(),
            "googleCanonical": t.string().optional(),
            "lastCrawlTime": t.string().optional(),
            "sitemap": t.array(t.string()).optional(),
            "verdict": t.string().optional(),
            "coverageState": t.string().optional(),
            "crawledAs": t.string().optional(),
        }
    ).named(renames["IndexStatusInspectionResultIn"])
    types["IndexStatusInspectionResultOut"] = t.struct(
        {
            "indexingState": t.string().optional(),
            "pageFetchState": t.string().optional(),
            "robotsTxtState": t.string().optional(),
            "referringUrls": t.array(t.string()).optional(),
            "userCanonical": t.string().optional(),
            "googleCanonical": t.string().optional(),
            "lastCrawlTime": t.string().optional(),
            "sitemap": t.array(t.string()).optional(),
            "verdict": t.string().optional(),
            "coverageState": t.string().optional(),
            "crawledAs": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IndexStatusInspectionResultOut"])

    functions = {}
    functions["sitemapsSubmit"] = searchconsole.get(
        "webmasters/v3/sites/{siteUrl}/sitemaps/{feedpath}",
        t.struct(
            {
                "feedpath": t.string().optional(),
                "siteUrl": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WmxSitemapOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sitemapsDelete"] = searchconsole.get(
        "webmasters/v3/sites/{siteUrl}/sitemaps/{feedpath}",
        t.struct(
            {
                "feedpath": t.string().optional(),
                "siteUrl": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WmxSitemapOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sitemapsList"] = searchconsole.get(
        "webmasters/v3/sites/{siteUrl}/sitemaps/{feedpath}",
        t.struct(
            {
                "feedpath": t.string().optional(),
                "siteUrl": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WmxSitemapOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sitemapsGet"] = searchconsole.get(
        "webmasters/v3/sites/{siteUrl}/sitemaps/{feedpath}",
        t.struct(
            {
                "feedpath": t.string().optional(),
                "siteUrl": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WmxSitemapOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["searchanalyticsQuery"] = searchconsole.post(
        "webmasters/v3/sites/{siteUrl}/searchAnalytics/query",
        t.struct(
            {
                "siteUrl": t.string().optional(),
                "rowLimit": t.integer().optional(),
                "startDate": t.string().optional(),
                "aggregationType": t.string().optional(),
                "dimensions": t.array(t.string()).optional(),
                "type": t.string().optional(),
                "searchType": t.string().optional(),
                "dataState": t.string().optional(),
                "dimensionFilterGroups": t.array(
                    t.proxy(renames["ApiDimensionFilterGroupIn"])
                ).optional(),
                "endDate": t.string().optional(),
                "startRow": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchAnalyticsQueryResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sitesList"] = searchconsole.get(
        "webmasters/v3/sites/{siteUrl}",
        t.struct({"siteUrl": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["WmxSiteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sitesDelete"] = searchconsole.get(
        "webmasters/v3/sites/{siteUrl}",
        t.struct({"siteUrl": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["WmxSiteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sitesAdd"] = searchconsole.get(
        "webmasters/v3/sites/{siteUrl}",
        t.struct({"siteUrl": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["WmxSiteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sitesGet"] = searchconsole.get(
        "webmasters/v3/sites/{siteUrl}",
        t.struct({"siteUrl": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["WmxSiteOut"]),
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

    return Import(
        importer="searchconsole",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
