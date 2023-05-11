from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_acmedns() -> Import:
    acmedns = HTTPRuntime("https://acmedns.googleapis.com/")

    renames = {
        "ErrorResponse": "_acmedns_1_ErrorResponse",
        "RotateChallengesRequestIn": "_acmedns_2_RotateChallengesRequestIn",
        "RotateChallengesRequestOut": "_acmedns_3_RotateChallengesRequestOut",
        "AcmeTxtRecordIn": "_acmedns_4_AcmeTxtRecordIn",
        "AcmeTxtRecordOut": "_acmedns_5_AcmeTxtRecordOut",
        "AcmeChallengeSetIn": "_acmedns_6_AcmeChallengeSetIn",
        "AcmeChallengeSetOut": "_acmedns_7_AcmeChallengeSetOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["AcmeTxtRecordIn"] = t.struct(
        {"fqdn": t.string().optional(), "digest": t.string().optional()}
    ).named(renames["AcmeTxtRecordIn"])
    types["AcmeTxtRecordOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "fqdn": t.string().optional(),
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

    return Import(importer="acmedns", renames=renames, types=types, functions=functions)
