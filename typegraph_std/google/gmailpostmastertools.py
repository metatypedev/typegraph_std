from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_gmailpostmastertools() -> Import:
    gmailpostmastertools = HTTPRuntime("https://gmailpostmastertools.googleapis.com/")

    renames = {
        "ErrorResponse": "_gmailpostmastertools_1_ErrorResponse",
        "DomainIn": "_gmailpostmastertools_2_DomainIn",
        "DomainOut": "_gmailpostmastertools_3_DomainOut",
        "ListDomainsResponseIn": "_gmailpostmastertools_4_ListDomainsResponseIn",
        "ListDomainsResponseOut": "_gmailpostmastertools_5_ListDomainsResponseOut",
        "DeliveryErrorIn": "_gmailpostmastertools_6_DeliveryErrorIn",
        "DeliveryErrorOut": "_gmailpostmastertools_7_DeliveryErrorOut",
        "ListTrafficStatsResponseIn": "_gmailpostmastertools_8_ListTrafficStatsResponseIn",
        "ListTrafficStatsResponseOut": "_gmailpostmastertools_9_ListTrafficStatsResponseOut",
        "FeedbackLoopIn": "_gmailpostmastertools_10_FeedbackLoopIn",
        "FeedbackLoopOut": "_gmailpostmastertools_11_FeedbackLoopOut",
        "TrafficStatsIn": "_gmailpostmastertools_12_TrafficStatsIn",
        "TrafficStatsOut": "_gmailpostmastertools_13_TrafficStatsOut",
        "IpReputationIn": "_gmailpostmastertools_14_IpReputationIn",
        "IpReputationOut": "_gmailpostmastertools_15_IpReputationOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["DomainIn"] = t.struct(
        {
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "permission": t.string().optional(),
        }
    ).named(renames["DomainIn"])
    types["DomainOut"] = t.struct(
        {
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "permission": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DomainOut"])
    types["ListDomainsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "domains": t.array(t.proxy(renames["DomainIn"])).optional(),
        }
    ).named(renames["ListDomainsResponseIn"])
    types["ListDomainsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "domains": t.array(t.proxy(renames["DomainOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDomainsResponseOut"])
    types["DeliveryErrorIn"] = t.struct(
        {
            "errorType": t.string().optional(),
            "errorRatio": t.number().optional(),
            "errorClass": t.string().optional(),
        }
    ).named(renames["DeliveryErrorIn"])
    types["DeliveryErrorOut"] = t.struct(
        {
            "errorType": t.string().optional(),
            "errorRatio": t.number().optional(),
            "errorClass": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeliveryErrorOut"])
    types["ListTrafficStatsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "trafficStats": t.array(t.proxy(renames["TrafficStatsIn"])).optional(),
        }
    ).named(renames["ListTrafficStatsResponseIn"])
    types["ListTrafficStatsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "trafficStats": t.array(t.proxy(renames["TrafficStatsOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTrafficStatsResponseOut"])
    types["FeedbackLoopIn"] = t.struct(
        {"spamRatio": t.number().optional(), "id": t.string().optional()}
    ).named(renames["FeedbackLoopIn"])
    types["FeedbackLoopOut"] = t.struct(
        {
            "spamRatio": t.number().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FeedbackLoopOut"])
    types["TrafficStatsIn"] = t.struct(
        {
            "spfSuccessRatio": t.number().optional(),
            "inboundEncryptionRatio": t.number().optional(),
            "dmarcSuccessRatio": t.number().optional(),
            "deliveryErrors": t.array(t.proxy(renames["DeliveryErrorIn"])).optional(),
            "spammyFeedbackLoops": t.array(
                t.proxy(renames["FeedbackLoopIn"])
            ).optional(),
            "dkimSuccessRatio": t.number().optional(),
            "ipReputations": t.array(t.proxy(renames["IpReputationIn"])).optional(),
            "name": t.string().optional(),
            "outboundEncryptionRatio": t.number().optional(),
            "domainReputation": t.string().optional(),
            "userReportedSpamRatio": t.number().optional(),
        }
    ).named(renames["TrafficStatsIn"])
    types["TrafficStatsOut"] = t.struct(
        {
            "spfSuccessRatio": t.number().optional(),
            "inboundEncryptionRatio": t.number().optional(),
            "dmarcSuccessRatio": t.number().optional(),
            "deliveryErrors": t.array(t.proxy(renames["DeliveryErrorOut"])).optional(),
            "spammyFeedbackLoops": t.array(
                t.proxy(renames["FeedbackLoopOut"])
            ).optional(),
            "dkimSuccessRatio": t.number().optional(),
            "ipReputations": t.array(t.proxy(renames["IpReputationOut"])).optional(),
            "name": t.string().optional(),
            "outboundEncryptionRatio": t.number().optional(),
            "domainReputation": t.string().optional(),
            "userReportedSpamRatio": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrafficStatsOut"])
    types["IpReputationIn"] = t.struct(
        {
            "reputation": t.string().optional(),
            "sampleIps": t.array(t.string()).optional(),
            "ipCount": t.string().optional(),
        }
    ).named(renames["IpReputationIn"])
    types["IpReputationOut"] = t.struct(
        {
            "reputation": t.string().optional(),
            "sampleIps": t.array(t.string()).optional(),
            "ipCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IpReputationOut"])

    functions = {}
    functions["domainsList"] = gmailpostmastertools.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["DomainOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["domainsGet"] = gmailpostmastertools.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["DomainOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["domainsTrafficStatsList"] = gmailpostmastertools.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["TrafficStatsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["domainsTrafficStatsGet"] = gmailpostmastertools.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["TrafficStatsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="gmailpostmastertools",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
