from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_policyanalyzer():
    policyanalyzer = HTTPRuntime("https://policyanalyzer.googleapis.com/")

    renames = {
        "ErrorResponse": "_policyanalyzer_1_ErrorResponse",
        "GoogleCloudPolicyanalyzerV1QueryActivityResponseIn": "_policyanalyzer_2_GoogleCloudPolicyanalyzerV1QueryActivityResponseIn",
        "GoogleCloudPolicyanalyzerV1QueryActivityResponseOut": "_policyanalyzer_3_GoogleCloudPolicyanalyzerV1QueryActivityResponseOut",
        "GoogleCloudPolicyanalyzerV1ObservationPeriodIn": "_policyanalyzer_4_GoogleCloudPolicyanalyzerV1ObservationPeriodIn",
        "GoogleCloudPolicyanalyzerV1ObservationPeriodOut": "_policyanalyzer_5_GoogleCloudPolicyanalyzerV1ObservationPeriodOut",
        "GoogleCloudPolicyanalyzerV1ActivityIn": "_policyanalyzer_6_GoogleCloudPolicyanalyzerV1ActivityIn",
        "GoogleCloudPolicyanalyzerV1ActivityOut": "_policyanalyzer_7_GoogleCloudPolicyanalyzerV1ActivityOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudPolicyanalyzerV1QueryActivityResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "activities": t.array(
                t.proxy(renames["GoogleCloudPolicyanalyzerV1ActivityIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudPolicyanalyzerV1QueryActivityResponseIn"])
    types["GoogleCloudPolicyanalyzerV1QueryActivityResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "activities": t.array(
                t.proxy(renames["GoogleCloudPolicyanalyzerV1ActivityOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPolicyanalyzerV1QueryActivityResponseOut"])
    types["GoogleCloudPolicyanalyzerV1ObservationPeriodIn"] = t.struct(
        {"startTime": t.string().optional(), "endTime": t.string().optional()}
    ).named(renames["GoogleCloudPolicyanalyzerV1ObservationPeriodIn"])
    types["GoogleCloudPolicyanalyzerV1ObservationPeriodOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPolicyanalyzerV1ObservationPeriodOut"])
    types["GoogleCloudPolicyanalyzerV1ActivityIn"] = t.struct(
        {
            "activity": t.struct({"_": t.string().optional()}).optional(),
            "observationPeriod": t.proxy(
                renames["GoogleCloudPolicyanalyzerV1ObservationPeriodIn"]
            ).optional(),
            "fullResourceName": t.string().optional(),
            "activityType": t.string().optional(),
        }
    ).named(renames["GoogleCloudPolicyanalyzerV1ActivityIn"])
    types["GoogleCloudPolicyanalyzerV1ActivityOut"] = t.struct(
        {
            "activity": t.struct({"_": t.string().optional()}).optional(),
            "observationPeriod": t.proxy(
                renames["GoogleCloudPolicyanalyzerV1ObservationPeriodOut"]
            ).optional(),
            "fullResourceName": t.string().optional(),
            "activityType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPolicyanalyzerV1ActivityOut"])

    functions = {}
    functions["projectsLocationsActivityTypesActivitiesQuery"] = policyanalyzer.get(
        "v1/{parent}/activities:query",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudPolicyanalyzerV1QueryActivityResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="policyanalyzer",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
