from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_gmailpostmastertools():
    gmailpostmastertools = HTTPRuntime("https://gmailpostmastertools.googleapis.com/")

    renames = {
        "ErrorResponse": "_gmailpostmastertools_1_ErrorResponse",
        "TrafficStatsIn": "_gmailpostmastertools_2_TrafficStatsIn",
        "TrafficStatsOut": "_gmailpostmastertools_3_TrafficStatsOut",
        "ListTrafficStatsResponseIn": "_gmailpostmastertools_4_ListTrafficStatsResponseIn",
        "ListTrafficStatsResponseOut": "_gmailpostmastertools_5_ListTrafficStatsResponseOut",
        "ListDomainsResponseIn": "_gmailpostmastertools_6_ListDomainsResponseIn",
        "ListDomainsResponseOut": "_gmailpostmastertools_7_ListDomainsResponseOut",
        "IpReputationIn": "_gmailpostmastertools_8_IpReputationIn",
        "IpReputationOut": "_gmailpostmastertools_9_IpReputationOut",
        "FeedbackLoopIn": "_gmailpostmastertools_10_FeedbackLoopIn",
        "FeedbackLoopOut": "_gmailpostmastertools_11_FeedbackLoopOut",
        "DeliveryErrorIn": "_gmailpostmastertools_12_DeliveryErrorIn",
        "DeliveryErrorOut": "_gmailpostmastertools_13_DeliveryErrorOut",
        "DomainIn": "_gmailpostmastertools_14_DomainIn",
        "DomainOut": "_gmailpostmastertools_15_DomainOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["TrafficStatsIn"] = t.struct(
        {
            "domainReputation": t.string().optional(),
            "spfSuccessRatio": t.number().optional(),
            "dkimSuccessRatio": t.number().optional(),
            "name": t.string().optional(),
            "deliveryErrors": t.array(t.proxy(renames["DeliveryErrorIn"])).optional(),
            "userReportedSpamRatio": t.number().optional(),
            "inboundEncryptionRatio": t.number().optional(),
            "dmarcSuccessRatio": t.number().optional(),
            "ipReputations": t.array(t.proxy(renames["IpReputationIn"])).optional(),
            "outboundEncryptionRatio": t.number().optional(),
            "spammyFeedbackLoops": t.array(
                t.proxy(renames["FeedbackLoopIn"])
            ).optional(),
        }
    ).named(renames["TrafficStatsIn"])
    types["TrafficStatsOut"] = t.struct(
        {
            "domainReputation": t.string().optional(),
            "spfSuccessRatio": t.number().optional(),
            "dkimSuccessRatio": t.number().optional(),
            "name": t.string().optional(),
            "deliveryErrors": t.array(t.proxy(renames["DeliveryErrorOut"])).optional(),
            "userReportedSpamRatio": t.number().optional(),
            "inboundEncryptionRatio": t.number().optional(),
            "dmarcSuccessRatio": t.number().optional(),
            "ipReputations": t.array(t.proxy(renames["IpReputationOut"])).optional(),
            "outboundEncryptionRatio": t.number().optional(),
            "spammyFeedbackLoops": t.array(
                t.proxy(renames["FeedbackLoopOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrafficStatsOut"])
    types["ListTrafficStatsResponseIn"] = t.struct(
        {
            "trafficStats": t.array(t.proxy(renames["TrafficStatsIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListTrafficStatsResponseIn"])
    types["ListTrafficStatsResponseOut"] = t.struct(
        {
            "trafficStats": t.array(t.proxy(renames["TrafficStatsOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTrafficStatsResponseOut"])
    types["ListDomainsResponseIn"] = t.struct(
        {
            "domains": t.array(t.proxy(renames["DomainIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListDomainsResponseIn"])
    types["ListDomainsResponseOut"] = t.struct(
        {
            "domains": t.array(t.proxy(renames["DomainOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDomainsResponseOut"])
    types["IpReputationIn"] = t.struct(
        {
            "sampleIps": t.array(t.string()).optional(),
            "ipCount": t.string().optional(),
            "reputation": t.string().optional(),
        }
    ).named(renames["IpReputationIn"])
    types["IpReputationOut"] = t.struct(
        {
            "sampleIps": t.array(t.string()).optional(),
            "ipCount": t.string().optional(),
            "reputation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IpReputationOut"])
    types["FeedbackLoopIn"] = t.struct(
        {"id": t.string().optional(), "spamRatio": t.number().optional()}
    ).named(renames["FeedbackLoopIn"])
    types["FeedbackLoopOut"] = t.struct(
        {
            "id": t.string().optional(),
            "spamRatio": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FeedbackLoopOut"])
    types["DeliveryErrorIn"] = t.struct(
        {
            "errorClass": t.string().optional(),
            "errorRatio": t.number().optional(),
            "errorType": t.string().optional(),
        }
    ).named(renames["DeliveryErrorIn"])
    types["DeliveryErrorOut"] = t.struct(
        {
            "errorClass": t.string().optional(),
            "errorRatio": t.number().optional(),
            "errorType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeliveryErrorOut"])
    types["DomainIn"] = t.struct(
        {
            "permission": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["DomainIn"])
    types["DomainOut"] = t.struct(
        {
            "permission": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DomainOut"])

    functions = {}
    functions["domainsGet"] = gmailpostmastertools.get(
        "v1/domains",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDomainsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["domainsList"] = gmailpostmastertools.get(
        "v1/domains",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDomainsResponseOut"]),
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
