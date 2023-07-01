from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_adexperiencereport():
    adexperiencereport = HTTPRuntime("https://adexperiencereport.googleapis.com/")

    renames = {
        "ErrorResponse": "_adexperiencereport_1_ErrorResponse",
        "ViolatingSitesResponseIn": "_adexperiencereport_2_ViolatingSitesResponseIn",
        "ViolatingSitesResponseOut": "_adexperiencereport_3_ViolatingSitesResponseOut",
        "PlatformSummaryIn": "_adexperiencereport_4_PlatformSummaryIn",
        "PlatformSummaryOut": "_adexperiencereport_5_PlatformSummaryOut",
        "SiteSummaryResponseIn": "_adexperiencereport_6_SiteSummaryResponseIn",
        "SiteSummaryResponseOut": "_adexperiencereport_7_SiteSummaryResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["PlatformSummaryIn"] = t.struct(
        {
            "filterStatus": t.string().optional(),
            "underReview": t.boolean().optional(),
            "reportUrl": t.string().optional(),
            "betterAdsStatus": t.string().optional(),
            "enforcementTime": t.string().optional(),
            "region": t.array(t.string()).optional(),
            "lastChangeTime": t.string().optional(),
        }
    ).named(renames["PlatformSummaryIn"])
    types["PlatformSummaryOut"] = t.struct(
        {
            "filterStatus": t.string().optional(),
            "underReview": t.boolean().optional(),
            "reportUrl": t.string().optional(),
            "betterAdsStatus": t.string().optional(),
            "enforcementTime": t.string().optional(),
            "region": t.array(t.string()).optional(),
            "lastChangeTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlatformSummaryOut"])
    types["SiteSummaryResponseIn"] = t.struct(
        {
            "reviewedSite": t.string().optional(),
            "desktopSummary": t.proxy(renames["PlatformSummaryIn"]).optional(),
            "mobileSummary": t.proxy(renames["PlatformSummaryIn"]).optional(),
        }
    ).named(renames["SiteSummaryResponseIn"])
    types["SiteSummaryResponseOut"] = t.struct(
        {
            "reviewedSite": t.string().optional(),
            "desktopSummary": t.proxy(renames["PlatformSummaryOut"]).optional(),
            "mobileSummary": t.proxy(renames["PlatformSummaryOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SiteSummaryResponseOut"])

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
