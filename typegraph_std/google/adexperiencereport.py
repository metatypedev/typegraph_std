from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_adexperiencereport() -> Import:
    adexperiencereport = HTTPRuntime("https://adexperiencereport.googleapis.com/")

    renames = {
        "ErrorResponse": "_adexperiencereport_1_ErrorResponse",
        "PlatformSummaryIn": "_adexperiencereport_2_PlatformSummaryIn",
        "PlatformSummaryOut": "_adexperiencereport_3_PlatformSummaryOut",
        "SiteSummaryResponseIn": "_adexperiencereport_4_SiteSummaryResponseIn",
        "SiteSummaryResponseOut": "_adexperiencereport_5_SiteSummaryResponseOut",
        "ViolatingSitesResponseIn": "_adexperiencereport_6_ViolatingSitesResponseIn",
        "ViolatingSitesResponseOut": "_adexperiencereport_7_ViolatingSitesResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["PlatformSummaryIn"] = t.struct(
        {
            "enforcementTime": t.string().optional(),
            "filterStatus": t.string().optional(),
            "betterAdsStatus": t.string().optional(),
            "region": t.array(t.string()).optional(),
            "underReview": t.boolean().optional(),
            "reportUrl": t.string().optional(),
            "lastChangeTime": t.string().optional(),
        }
    ).named(renames["PlatformSummaryIn"])
    types["PlatformSummaryOut"] = t.struct(
        {
            "enforcementTime": t.string().optional(),
            "filterStatus": t.string().optional(),
            "betterAdsStatus": t.string().optional(),
            "region": t.array(t.string()).optional(),
            "underReview": t.boolean().optional(),
            "reportUrl": t.string().optional(),
            "lastChangeTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlatformSummaryOut"])
    types["SiteSummaryResponseIn"] = t.struct(
        {
            "reviewedSite": t.string().optional(),
            "mobileSummary": t.proxy(renames["PlatformSummaryIn"]).optional(),
            "desktopSummary": t.proxy(renames["PlatformSummaryIn"]).optional(),
        }
    ).named(renames["SiteSummaryResponseIn"])
    types["SiteSummaryResponseOut"] = t.struct(
        {
            "reviewedSite": t.string().optional(),
            "mobileSummary": t.proxy(renames["PlatformSummaryOut"]).optional(),
            "desktopSummary": t.proxy(renames["PlatformSummaryOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SiteSummaryResponseOut"])
    types["ViolatingSitesResponseIn"] = t.struct(
        {
            "violatingSites": t.array(
                t.proxy(renames["SiteSummaryResponseIn"])
            ).optional()
        }
    ).named(renames["ViolatingSitesResponseIn"])
    types["ViolatingSitesResponseOut"] = t.struct(
        {
            "violatingSites": t.array(
                t.proxy(renames["SiteSummaryResponseOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ViolatingSitesResponseOut"])

    functions = {}
    functions["violatingSitesList"] = adexperiencereport.get(
        "v1/violatingSites",
        t.struct({"auth": t.string().optional()}),
        t.proxy(renames["ViolatingSitesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sitesGet"] = adexperiencereport.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SiteSummaryResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="adexperiencereport",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
