from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_acmedns() -> Import:
    acmedns = HTTPRuntime("https://acmedns.googleapis.com/")

    renames = {
        "ErrorResponse": "_acmedns_1_ErrorResponse",
        "AcmeTxtRecordIn": "_acmedns_2_AcmeTxtRecordIn",
        "AcmeTxtRecordOut": "_acmedns_3_AcmeTxtRecordOut",
        "AcmeChallengeSetIn": "_acmedns_4_AcmeChallengeSetIn",
        "AcmeChallengeSetOut": "_acmedns_5_AcmeChallengeSetOut",
        "RotateChallengesRequestIn": "_acmedns_6_RotateChallengesRequestIn",
        "RotateChallengesRequestOut": "_acmedns_7_RotateChallengesRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["AcmeTxtRecordIn"] = t.struct(
        {"fqdn": t.string().optional(), "digest": t.string().optional()}
    ).named(renames["AcmeTxtRecordIn"])
    types["AcmeTxtRecordOut"] = t.struct(
        {
            "fqdn": t.string().optional(),
            "updateTime": t.string().optional(),
            "digest": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AcmeTxtRecordOut"])
    types["AcmeChallengeSetIn"] = t.struct(
        {"record": t.array(t.proxy(renames["AcmeTxtRecordIn"])).optional()}
    ).named(renames["AcmeChallengeSetIn"])
    types["AcmeChallengeSetOut"] = t.struct(
        {
            "record": t.array(t.proxy(renames["AcmeTxtRecordOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AcmeChallengeSetOut"])
    types["RotateChallengesRequestIn"] = t.struct(
        {
            "accessToken": t.string(),
            "recordsToRemove": t.array(t.proxy(renames["AcmeTxtRecordIn"])).optional(),
            "recordsToAdd": t.array(t.proxy(renames["AcmeTxtRecordIn"])).optional(),
            "keepExpiredRecords": t.boolean().optional(),
        }
    ).named(renames["RotateChallengesRequestIn"])
    types["RotateChallengesRequestOut"] = t.struct(
        {
            "accessToken": t.string(),
            "recordsToRemove": t.array(t.proxy(renames["AcmeTxtRecordOut"])).optional(),
            "recordsToAdd": t.array(t.proxy(renames["AcmeTxtRecordOut"])).optional(),
            "keepExpiredRecords": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RotateChallengesRequestOut"])

    functions = {}
    functions["acmeChallengeSetsGet"] = acmedns.post(
        "v1/acmeChallengeSets/{rootDomain}:rotateChallenges",
        t.struct(
            {
                "rootDomain": t.string(),
                "accessToken": t.string(),
                "recordsToRemove": t.array(
                    t.proxy(renames["AcmeTxtRecordIn"])
                ).optional(),
                "recordsToAdd": t.array(t.proxy(renames["AcmeTxtRecordIn"])).optional(),
                "keepExpiredRecords": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AcmeChallengeSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["acmeChallengeSetsRotateChallenges"] = acmedns.post(
        "v1/acmeChallengeSets/{rootDomain}:rotateChallenges",
        t.struct(
            {
                "rootDomain": t.string(),
                "accessToken": t.string(),
                "recordsToRemove": t.array(
                    t.proxy(renames["AcmeTxtRecordIn"])
                ).optional(),
                "recordsToAdd": t.array(t.proxy(renames["AcmeTxtRecordIn"])).optional(),
                "keepExpiredRecords": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AcmeChallengeSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="acmedns", renames=renames, types=Box(types), functions=Box(functions)
    )
