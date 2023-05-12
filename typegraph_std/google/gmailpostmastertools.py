from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_gmailpostmastertools() -> Import:
    gmailpostmastertools = HTTPRuntime("https://gmailpostmastertools.googleapis.com/")

    renames = {
        "ErrorResponse": "_gmailpostmastertools_1_ErrorResponse",
        "FeedbackLoopIn": "_gmailpostmastertools_2_FeedbackLoopIn",
        "FeedbackLoopOut": "_gmailpostmastertools_3_FeedbackLoopOut",
        "TrafficStatsIn": "_gmailpostmastertools_4_TrafficStatsIn",
        "TrafficStatsOut": "_gmailpostmastertools_5_TrafficStatsOut",
        "DomainIn": "_gmailpostmastertools_6_DomainIn",
        "DomainOut": "_gmailpostmastertools_7_DomainOut",
        "ListTrafficStatsResponseIn": "_gmailpostmastertools_8_ListTrafficStatsResponseIn",
        "ListTrafficStatsResponseOut": "_gmailpostmastertools_9_ListTrafficStatsResponseOut",
        "ListDomainsResponseIn": "_gmailpostmastertools_10_ListDomainsResponseIn",
        "ListDomainsResponseOut": "_gmailpostmastertools_11_ListDomainsResponseOut",
        "IpReputationIn": "_gmailpostmastertools_12_IpReputationIn",
        "IpReputationOut": "_gmailpostmastertools_13_IpReputationOut",
        "DeliveryErrorIn": "_gmailpostmastertools_14_DeliveryErrorIn",
        "DeliveryErrorOut": "_gmailpostmastertools_15_DeliveryErrorOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["TrafficStatsIn"] = t.struct(
        {
            "spfSuccessRatio": t.number().optional(),
            "outboundEncryptionRatio": t.number().optional(),
            "domainReputation": t.string().optional(),
            "dkimSuccessRatio": t.number().optional(),
            "deliveryErrors": t.array(t.proxy(renames["DeliveryErrorIn"])).optional(),
            "name": t.string().optional(),
            "userReportedSpamRatio": t.number().optional(),
            "ipReputations": t.array(t.proxy(renames["IpReputationIn"])).optional(),
            "inboundEncryptionRatio": t.number().optional(),
            "dmarcSuccessRatio": t.number().optional(),
            "spammyFeedbackLoops": t.array(
                t.proxy(renames["FeedbackLoopIn"])
            ).optional(),
        }
    ).named(renames["TrafficStatsIn"])
    types["TrafficStatsOut"] = t.struct(
        {
            "spfSuccessRatio": t.number().optional(),
            "outboundEncryptionRatio": t.number().optional(),
            "domainReputation": t.string().optional(),
            "dkimSuccessRatio": t.number().optional(),
            "deliveryErrors": t.array(t.proxy(renames["DeliveryErrorOut"])).optional(),
            "name": t.string().optional(),
            "userReportedSpamRatio": t.number().optional(),
            "ipReputations": t.array(t.proxy(renames["IpReputationOut"])).optional(),
            "inboundEncryptionRatio": t.number().optional(),
            "dmarcSuccessRatio": t.number().optional(),
            "spammyFeedbackLoops": t.array(
                t.proxy(renames["FeedbackLoopOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrafficStatsOut"])
    types["DomainIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "permission": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["DomainIn"])
    types["DomainOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "permission": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DomainOut"])
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
            "reputation": t.string().optional(),
            "ipCount": t.string().optional(),
        }
    ).named(renames["IpReputationIn"])
    types["IpReputationOut"] = t.struct(
        {
            "sampleIps": t.array(t.string()).optional(),
            "reputation": t.string().optional(),
            "ipCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IpReputationOut"])
    types["DeliveryErrorIn"] = t.struct(
        {
            "errorRatio": t.number().optional(),
            "errorClass": t.string().optional(),
            "errorType": t.string().optional(),
        }
    ).named(renames["DeliveryErrorIn"])
    types["DeliveryErrorOut"] = t.struct(
        {
            "errorRatio": t.number().optional(),
            "errorClass": t.string().optional(),
            "errorType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeliveryErrorOut"])

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
                "parent": t.string().optional(),
                "endDate.day": t.integer().optional(),
                "pageSize": t.integer().optional(),
                "startDate.day": t.integer().optional(),
                "endDate.year": t.integer().optional(),
                "startDate.year": t.integer().optional(),
                "startDate.month": t.integer().optional(),
                "pageToken": t.string().optional(),
                "endDate.month": t.integer().optional(),
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
                "parent": t.string().optional(),
                "endDate.day": t.integer().optional(),
                "pageSize": t.integer().optional(),
                "startDate.day": t.integer().optional(),
                "endDate.year": t.integer().optional(),
                "startDate.year": t.integer().optional(),
                "startDate.month": t.integer().optional(),
                "pageToken": t.string().optional(),
                "endDate.month": t.integer().optional(),
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
        types=Box(types),
        functions=Box(functions),
    )
