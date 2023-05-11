from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_gmailpostmastertools() -> Import:
    gmailpostmastertools = HTTPRuntime("https://gmailpostmastertools.googleapis.com/")

    renames = {
        "ErrorResponse": "_gmailpostmastertools_1_ErrorResponse",
        "DomainIn": "_gmailpostmastertools_2_DomainIn",
        "DomainOut": "_gmailpostmastertools_3_DomainOut",
        "ListDomainsResponseIn": "_gmailpostmastertools_4_ListDomainsResponseIn",
        "ListDomainsResponseOut": "_gmailpostmastertools_5_ListDomainsResponseOut",
        "TrafficStatsIn": "_gmailpostmastertools_6_TrafficStatsIn",
        "TrafficStatsOut": "_gmailpostmastertools_7_TrafficStatsOut",
        "ListTrafficStatsResponseIn": "_gmailpostmastertools_8_ListTrafficStatsResponseIn",
        "ListTrafficStatsResponseOut": "_gmailpostmastertools_9_ListTrafficStatsResponseOut",
        "FeedbackLoopIn": "_gmailpostmastertools_10_FeedbackLoopIn",
        "FeedbackLoopOut": "_gmailpostmastertools_11_FeedbackLoopOut",
        "DeliveryErrorIn": "_gmailpostmastertools_12_DeliveryErrorIn",
        "DeliveryErrorOut": "_gmailpostmastertools_13_DeliveryErrorOut",
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
            "permission": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["DomainIn"])
    types["DomainOut"] = t.struct(
        {
            "name": t.string().optional(),
            "permission": t.string().optional(),
            "createTime": t.string().optional(),
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
    types["TrafficStatsIn"] = t.struct(
        {
            "dmarcSuccessRatio": t.number().optional(),
            "ipReputations": t.array(t.proxy(renames["IpReputationIn"])).optional(),
            "deliveryErrors": t.array(t.proxy(renames["DeliveryErrorIn"])).optional(),
            "dkimSuccessRatio": t.number().optional(),
            "spammyFeedbackLoops": t.array(
                t.proxy(renames["FeedbackLoopIn"])
            ).optional(),
            "name": t.string().optional(),
            "outboundEncryptionRatio": t.number().optional(),
            "domainReputation": t.string().optional(),
            "spfSuccessRatio": t.number().optional(),
            "inboundEncryptionRatio": t.number().optional(),
            "userReportedSpamRatio": t.number().optional(),
        }
    ).named(renames["TrafficStatsIn"])
    types["TrafficStatsOut"] = t.struct(
        {
            "dmarcSuccessRatio": t.number().optional(),
            "ipReputations": t.array(t.proxy(renames["IpReputationOut"])).optional(),
            "deliveryErrors": t.array(t.proxy(renames["DeliveryErrorOut"])).optional(),
            "dkimSuccessRatio": t.number().optional(),
            "spammyFeedbackLoops": t.array(
                t.proxy(renames["FeedbackLoopOut"])
            ).optional(),
            "name": t.string().optional(),
            "outboundEncryptionRatio": t.number().optional(),
            "domainReputation": t.string().optional(),
            "spfSuccessRatio": t.number().optional(),
            "inboundEncryptionRatio": t.number().optional(),
            "userReportedSpamRatio": t.number().optional(),
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
    functions["domainsTrafficStatsGet"] = gmailpostmastertools.get(
        "v1/{parent}/trafficStats",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "startDate.month": t.integer().optional(),
                "startDate.year": t.integer().optional(),
                "endDate.year": t.integer().optional(),
                "parent": t.string().optional(),
                "endDate.month": t.integer().optional(),
                "pageSize": t.integer().optional(),
                "endDate.day": t.integer().optional(),
                "startDate.day": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTrafficStatsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["domainsTrafficStatsList"] = gmailpostmastertools.get(
        "v1/{parent}/trafficStats",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "startDate.month": t.integer().optional(),
                "startDate.year": t.integer().optional(),
                "endDate.year": t.integer().optional(),
                "parent": t.string().optional(),
                "endDate.month": t.integer().optional(),
                "pageSize": t.integer().optional(),
                "endDate.day": t.integer().optional(),
                "startDate.day": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTrafficStatsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="gmailpostmastertools",
        renames=renames,
        types=types,
        functions=functions,
    )
