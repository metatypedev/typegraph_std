from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_acmedns():
    acmedns = HTTPRuntime("https://acmedns.googleapis.com/")

    renames = {
        "ErrorResponse": "_acmedns_1_ErrorResponse",
        "RotateChallengesRequestIn": "_acmedns_2_RotateChallengesRequestIn",
        "RotateChallengesRequestOut": "_acmedns_3_RotateChallengesRequestOut",
        "AcmeChallengeSetIn": "_acmedns_4_AcmeChallengeSetIn",
        "AcmeChallengeSetOut": "_acmedns_5_AcmeChallengeSetOut",
        "AcmeTxtRecordIn": "_acmedns_6_AcmeTxtRecordIn",
        "AcmeTxtRecordOut": "_acmedns_7_AcmeTxtRecordOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["RotateChallengesRequestIn"] = t.struct(
        {
            "keepExpiredRecords": t.boolean().optional(),
            "recordsToRemove": t.array(t.proxy(renames["AcmeTxtRecordIn"])).optional(),
            "recordsToAdd": t.array(t.proxy(renames["AcmeTxtRecordIn"])).optional(),
            "accessToken": t.string(),
        }
    ).named(renames["RotateChallengesRequestIn"])
    types["RotateChallengesRequestOut"] = t.struct(
        {
            "keepExpiredRecords": t.boolean().optional(),
            "recordsToRemove": t.array(t.proxy(renames["AcmeTxtRecordOut"])).optional(),
            "recordsToAdd": t.array(t.proxy(renames["AcmeTxtRecordOut"])).optional(),
            "accessToken": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RotateChallengesRequestOut"])
    types["AcmeChallengeSetIn"] = t.struct(
        {"record": t.array(t.proxy(renames["AcmeTxtRecordIn"])).optional()}
    ).named(renames["AcmeChallengeSetIn"])
    types["AcmeChallengeSetOut"] = t.struct(
        {
            "record": t.array(t.proxy(renames["AcmeTxtRecordOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AcmeChallengeSetOut"])
    types["AcmeTxtRecordIn"] = t.struct(
        {"digest": t.string().optional(), "fqdn": t.string().optional()}
    ).named(renames["AcmeTxtRecordIn"])
    types["AcmeTxtRecordOut"] = t.struct(
        {
            "digest": t.string().optional(),
            "fqdn": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AcmeTxtRecordOut"])

    functions = {}
    functions["acmeChallengeSetsGet"] = acmedns.post(
        "v1/acmeChallengeSets/{rootDomain}:rotateChallenges",
        t.struct(
            {
                "rootDomain": t.string(),
                "keepExpiredRecords": t.boolean().optional(),
                "recordsToRemove": t.array(
                    t.proxy(renames["AcmeTxtRecordIn"])
                ).optional(),
                "recordsToAdd": t.array(t.proxy(renames["AcmeTxtRecordIn"])).optional(),
                "accessToken": t.string(),
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
                "keepExpiredRecords": t.boolean().optional(),
                "recordsToRemove": t.array(
                    t.proxy(renames["AcmeTxtRecordIn"])
                ).optional(),
                "recordsToAdd": t.array(t.proxy(renames["AcmeTxtRecordIn"])).optional(),
                "accessToken": t.string(),
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
