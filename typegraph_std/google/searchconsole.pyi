from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    RichResultsIssueIn: t.typedef = ...
    RichResultsIssueOut: t.typedef = ...
    RunMobileFriendlyTestRequestIn: t.typedef = ...
    RunMobileFriendlyTestRequestOut: t.typedef = ...
    RichResultsInspectionResultIn: t.typedef = ...
    RichResultsInspectionResultOut: t.typedef = ...
    AmpIssueIn: t.typedef = ...
    AmpIssueOut: t.typedef = ...
    InspectUrlIndexRequestIn: t.typedef = ...
    InspectUrlIndexRequestOut: t.typedef = ...
    BlockedResourceIn: t.typedef = ...
    BlockedResourceOut: t.typedef = ...
    WmxSitemapContentIn: t.typedef = ...
    WmxSitemapContentOut: t.typedef = ...
    SearchAnalyticsQueryRequestIn: t.typedef = ...
    SearchAnalyticsQueryRequestOut: t.typedef = ...
    ItemIn: t.typedef = ...
    ItemOut: t.typedef = ...
    UrlInspectionResultIn: t.typedef = ...
    UrlInspectionResultOut: t.typedef = ...
    ApiDimensionFilterGroupIn: t.typedef = ...
    ApiDimensionFilterGroupOut: t.typedef = ...
    RunMobileFriendlyTestResponseIn: t.typedef = ...
    RunMobileFriendlyTestResponseOut: t.typedef = ...
    WmxSiteIn: t.typedef = ...
    WmxSiteOut: t.typedef = ...
    MobileUsabilityInspectionResultIn: t.typedef = ...
    MobileUsabilityInspectionResultOut: t.typedef = ...
    ApiDataRowIn: t.typedef = ...
    ApiDataRowOut: t.typedef = ...
    InspectUrlIndexResponseIn: t.typedef = ...
    InspectUrlIndexResponseOut: t.typedef = ...
    AmpInspectionResultIn: t.typedef = ...
    AmpInspectionResultOut: t.typedef = ...
    SitemapsListResponseIn: t.typedef = ...
    SitemapsListResponseOut: t.typedef = ...
    SearchAnalyticsQueryResponseIn: t.typedef = ...
    SearchAnalyticsQueryResponseOut: t.typedef = ...
    ApiDimensionFilterIn: t.typedef = ...
    ApiDimensionFilterOut: t.typedef = ...
    WmxSitemapIn: t.typedef = ...
    WmxSitemapOut: t.typedef = ...
    SitesListResponseIn: t.typedef = ...
    SitesListResponseOut: t.typedef = ...
    MobileUsabilityIssueIn: t.typedef = ...
    MobileUsabilityIssueOut: t.typedef = ...
    ResourceIssueIn: t.typedef = ...
    ResourceIssueOut: t.typedef = ...
    ImageIn: t.typedef = ...
    ImageOut: t.typedef = ...
    DetectedItemsIn: t.typedef = ...
    DetectedItemsOut: t.typedef = ...
    TestStatusIn: t.typedef = ...
    TestStatusOut: t.typedef = ...
    MobileFriendlyIssueIn: t.typedef = ...
    MobileFriendlyIssueOut: t.typedef = ...
    IndexStatusInspectionResultIn: t.typedef = ...
    IndexStatusInspectionResultOut: t.typedef = ...

class FuncList:
    sitemapsSubmit: t.func = ...
    sitemapsDelete: t.func = ...
    sitemapsList: t.func = ...
    sitemapsGet: t.func = ...
    searchanalyticsQuery: t.func = ...
    sitesList: t.func = ...
    sitesDelete: t.func = ...
    sitesAdd: t.func = ...
    sitesGet: t.func = ...
    urlInspectionIndexInspect: t.func = ...
    urlTestingToolsMobileFriendlyTestRun: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_searchconsole() -> Import: ...
