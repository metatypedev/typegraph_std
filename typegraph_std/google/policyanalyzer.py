from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_policyanalyzer() -> Import:
    policyanalyzer = HTTPRuntime("https://policyanalyzer.googleapis.com/")

    renames = {
        "ErrorResponse": "_policyanalyzer_1_ErrorResponse",
        "GoogleCloudPolicyanalyzerV1QueryActivityResponseIn": "_policyanalyzer_2_GoogleCloudPolicyanalyzerV1QueryActivityResponseIn",
        "GoogleCloudPolicyanalyzerV1QueryActivityResponseOut": "_policyanalyzer_3_GoogleCloudPolicyanalyzerV1QueryActivityResponseOut",
        "GoogleCloudPolicyanalyzerV1ActivityIn": "_policyanalyzer_4_GoogleCloudPolicyanalyzerV1ActivityIn",
        "GoogleCloudPolicyanalyzerV1ActivityOut": "_policyanalyzer_5_GoogleCloudPolicyanalyzerV1ActivityOut",
        "GoogleCloudPolicyanalyzerV1ObservationPeriodIn": "_policyanalyzer_6_GoogleCloudPolicyanalyzerV1ObservationPeriodIn",
        "GoogleCloudPolicyanalyzerV1ObservationPeriodOut": "_policyanalyzer_7_GoogleCloudPolicyanalyzerV1ObservationPeriodOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudPolicyanalyzerV1QueryActivityResponseIn"] = t.struct(
        {
            "activities": t.array(
                t.proxy(renames["GoogleCloudPolicyanalyzerV1ActivityIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudPolicyanalyzerV1QueryActivityResponseIn"])
    types["GoogleCloudPolicyanalyzerV1QueryActivityResponseOut"] = t.struct(
        {
            "activities": t.array(
                t.proxy(renames["GoogleCloudPolicyanalyzerV1ActivityOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPolicyanalyzerV1QueryActivityResponseOut"])
    types["GoogleCloudPolicyanalyzerV1ActivityIn"] = t.struct(
        {
            "activity": t.struct({"_": t.string().optional()}).optional(),
            "fullResourceName": t.string().optional(),
            "observationPeriod": t.proxy(
                renames["GoogleCloudPolicyanalyzerV1ObservationPeriodIn"]
            ).optional(),
            "activityType": t.string().optional(),
        }
    ).named(renames["GoogleCloudPolicyanalyzerV1ActivityIn"])
    types["GoogleCloudPolicyanalyzerV1ActivityOut"] = t.struct(
        {
            "activity": t.struct({"_": t.string().optional()}).optional(),
            "fullResourceName": t.string().optional(),
            "observationPeriod": t.proxy(
                renames["GoogleCloudPolicyanalyzerV1ObservationPeriodOut"]
            ).optional(),
            "activityType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPolicyanalyzerV1ActivityOut"])
    types["GoogleCloudPolicyanalyzerV1ObservationPeriodIn"] = t.struct(
        {"endTime": t.string().optional(), "startTime": t.string().optional()}
    ).named(renames["GoogleCloudPolicyanalyzerV1ObservationPeriodIn"])
    types["GoogleCloudPolicyanalyzerV1ObservationPeriodOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPolicyanalyzerV1ObservationPeriodOut"])

    functions = {}
    functions["projectsLocationsActivityTypesActivitiesQuery"] = policyanalyzer.get(
        "v1/{parent}/activities:query",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudPolicyanalyzerV1QueryActivityResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="policyanalyzer", renames=renames, types=types, functions=functions
    )
