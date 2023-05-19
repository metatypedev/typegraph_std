from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_acmedns() -> Import:
    acmedns = HTTPRuntime("https://acmedns.googleapis.com/")

    renames = {
        "ErrorResponse": "_acmedns_1_ErrorResponse",
        "AcmeChallengeSetIn": "_acmedns_2_AcmeChallengeSetIn",
        "AcmeChallengeSetOut": "_acmedns_3_AcmeChallengeSetOut",
        "RotateChallengesRequestIn": "_acmedns_4_RotateChallengesRequestIn",
        "RotateChallengesRequestOut": "_acmedns_5_RotateChallengesRequestOut",
        "AcmeTxtRecordIn": "_acmedns_6_AcmeTxtRecordIn",
        "AcmeTxtRecordOut": "_acmedns_7_AcmeTxtRecordOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
            "keepExpiredRecords": t.boolean().optional(),
            "recordsToAdd": t.array(t.proxy(renames["AcmeTxtRecordIn"])).optional(),
            "accessToken": t.string(),
            "recordsToRemove": t.array(t.proxy(renames["AcmeTxtRecordIn"])).optional(),
        }
    ).named(renames["RotateChallengesRequestIn"])
    types["RotateChallengesRequestOut"] = t.struct(
        {
            "keepExpiredRecords": t.boolean().optional(),
            "recordsToAdd": t.array(t.proxy(renames["AcmeTxtRecordOut"])).optional(),
            "accessToken": t.string(),
            "recordsToRemove": t.array(t.proxy(renames["AcmeTxtRecordOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RotateChallengesRequestOut"])
    types["AcmeTxtRecordIn"] = t.struct(
        {"digest": t.string().optional(), "fqdn": t.string().optional()}
    ).named(renames["AcmeTxtRecordIn"])
    types["AcmeTxtRecordOut"] = t.struct(
        {
            "digest": t.string().optional(),
            "updateTime": t.string().optional(),
            "fqdn": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AcmeTxtRecordOut"])

    functions = {}
    functions["acmeChallengeSetsRotateChallenges"] = acmedns.get(
        "v1/acmeChallengeSets/{rootDomain}",
        t.struct({"rootDomain": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["AcmeChallengeSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["acmeChallengeSetsGet"] = acmedns.get(
        "v1/acmeChallengeSets/{rootDomain}",
        t.struct({"rootDomain": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["AcmeChallengeSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="acmedns", renames=renames, types=Box(types), functions=Box(functions)
    )
