from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_abusiveexperiencereport():
    abusiveexperiencereport = HTTPRuntime(
        "https://abusiveexperiencereport.googleapis.com/"
    )

    renames = {
        "ErrorResponse": "_abusiveexperiencereport_1_ErrorResponse",
        "ViolatingSitesResponseIn": "_abusiveexperiencereport_2_ViolatingSitesResponseIn",
        "ViolatingSitesResponseOut": "_abusiveexperiencereport_3_ViolatingSitesResponseOut",
        "SiteSummaryResponseIn": "_abusiveexperiencereport_4_SiteSummaryResponseIn",
        "SiteSummaryResponseOut": "_abusiveexperiencereport_5_SiteSummaryResponseOut",
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
    types["SiteSummaryResponseIn"] = t.struct(
        {
            "reportUrl": t.string().optional(),
            "enforcementTime": t.string().optional(),
            "filterStatus": t.string().optional(),
            "underReview": t.boolean().optional(),
            "reviewedSite": t.string().optional(),
            "lastChangeTime": t.string().optional(),
            "abusiveStatus": t.string().optional(),
        }
    ).named(renames["SiteSummaryResponseIn"])
    types["SiteSummaryResponseOut"] = t.struct(
        {
            "reportUrl": t.string().optional(),
            "enforcementTime": t.string().optional(),
            "filterStatus": t.string().optional(),
            "underReview": t.boolean().optional(),
            "reviewedSite": t.string().optional(),
            "lastChangeTime": t.string().optional(),
            "abusiveStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SiteSummaryResponseOut"])

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
