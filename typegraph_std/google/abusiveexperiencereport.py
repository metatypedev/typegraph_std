from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_abusiveexperiencereport() -> Import:
    abusiveexperiencereport = HTTPRuntime(
        "https://abusiveexperiencereport.googleapis.com/"
    )

    renames = {
        "ErrorResponse": "_abusiveexperiencereport_1_ErrorResponse",
        "SiteSummaryResponseIn": "_abusiveexperiencereport_2_SiteSummaryResponseIn",
        "SiteSummaryResponseOut": "_abusiveexperiencereport_3_SiteSummaryResponseOut",
        "ViolatingSitesResponseIn": "_abusiveexperiencereport_4_ViolatingSitesResponseIn",
        "ViolatingSitesResponseOut": "_abusiveexperiencereport_5_ViolatingSitesResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["SiteSummaryResponseIn"] = t.struct(
        {
            "reviewedSite": t.string().optional(),
            "reportUrl": t.string().optional(),
            "lastChangeTime": t.string().optional(),
            "enforcementTime": t.string().optional(),
            "underReview": t.boolean().optional(),
            "filterStatus": t.string().optional(),
            "abusiveStatus": t.string().optional(),
        }
    ).named(renames["SiteSummaryResponseIn"])
    types["SiteSummaryResponseOut"] = t.struct(
        {
            "reviewedSite": t.string().optional(),
            "reportUrl": t.string().optional(),
            "lastChangeTime": t.string().optional(),
            "enforcementTime": t.string().optional(),
            "underReview": t.boolean().optional(),
            "filterStatus": t.string().optional(),
            "abusiveStatus": t.string().optional(),
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
    functions["violatingSitesList"] = abusiveexperiencereport.get(
        "v1/violatingSites",
        t.struct({"auth": t.string().optional()}),
        t.proxy(renames["ViolatingSitesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sitesGet"] = abusiveexperiencereport.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SiteSummaryResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="abusiveexperiencereport",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
