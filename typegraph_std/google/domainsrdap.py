from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_domainsrdap() -> Import:
    domainsrdap = HTTPRuntime("https://domainsrdap.googleapis.com/")

    renames = {
        "ErrorResponse": "_domainsrdap_1_ErrorResponse",
        "HttpBodyIn": "_domainsrdap_2_HttpBodyIn",
        "HttpBodyOut": "_domainsrdap_3_HttpBodyOut",
        "NoticeIn": "_domainsrdap_4_NoticeIn",
        "NoticeOut": "_domainsrdap_5_NoticeOut",
        "LinkIn": "_domainsrdap_6_LinkIn",
        "LinkOut": "_domainsrdap_7_LinkOut",
        "RdapResponseIn": "_domainsrdap_8_RdapResponseIn",
        "RdapResponseOut": "_domainsrdap_9_RdapResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["HttpBodyIn"] = t.struct(
        {
            "contentType": t.string().optional(),
            "extensions": t.array(t.struct({"_": t.string().optional()})).optional(),
            "data": t.string().optional(),
        }
    ).named(renames["HttpBodyIn"])
    types["HttpBodyOut"] = t.struct(
        {
            "contentType": t.string().optional(),
            "extensions": t.array(t.struct({"_": t.string().optional()})).optional(),
            "data": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpBodyOut"])
    types["NoticeIn"] = t.struct(
        {
            "title": t.string().optional(),
            "description": t.array(t.string()).optional(),
            "type": t.string().optional(),
            "links": t.array(t.proxy(renames["LinkIn"])).optional(),
        }
    ).named(renames["NoticeIn"])
    types["NoticeOut"] = t.struct(
        {
            "title": t.string().optional(),
            "description": t.array(t.string()).optional(),
            "type": t.string().optional(),
            "links": t.array(t.proxy(renames["LinkOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NoticeOut"])
    types["LinkIn"] = t.struct(
        {
            "type": t.string().optional(),
            "title": t.string().optional(),
            "media": t.string().optional(),
            "rel": t.string().optional(),
            "hreflang": t.string().optional(),
            "href": t.string().optional(),
            "value": t.string().optional(),
        }
    ).named(renames["LinkIn"])
    types["LinkOut"] = t.struct(
        {
            "type": t.string().optional(),
            "title": t.string().optional(),
            "media": t.string().optional(),
            "rel": t.string().optional(),
            "hreflang": t.string().optional(),
            "href": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinkOut"])
    types["RdapResponseIn"] = t.struct(
        {
            "description": t.array(t.string()).optional(),
            "jsonResponse": t.proxy(renames["HttpBodyIn"]).optional(),
            "title": t.string().optional(),
            "rdapConformance": t.array(t.string()).optional(),
            "notices": t.array(t.proxy(renames["NoticeIn"])).optional(),
            "errorCode": t.integer().optional(),
            "lang": t.string().optional(),
        }
    ).named(renames["RdapResponseIn"])
    types["RdapResponseOut"] = t.struct(
        {
            "description": t.array(t.string()).optional(),
            "jsonResponse": t.proxy(renames["HttpBodyOut"]).optional(),
            "title": t.string().optional(),
            "rdapConformance": t.array(t.string()).optional(),
            "notices": t.array(t.proxy(renames["NoticeOut"])).optional(),
            "errorCode": t.integer().optional(),
            "lang": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RdapResponseOut"])

    functions = {}
    functions["v1GetDomains"] = domainsrdap.get(
        "v1/ip",
        t.struct({"auth": t.string().optional()}),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1GetHelp"] = domainsrdap.get(
        "v1/ip",
        t.struct({"auth": t.string().optional()}),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1GetEntities"] = domainsrdap.get(
        "v1/ip",
        t.struct({"auth": t.string().optional()}),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1GetNameservers"] = domainsrdap.get(
        "v1/ip",
        t.struct({"auth": t.string().optional()}),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1GetIp"] = domainsrdap.get(
        "v1/ip",
        t.struct({"auth": t.string().optional()}),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nameserverGet"] = domainsrdap.get(
        "v1/nameserver/{nameserverId}",
        t.struct({"nameserverId": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["RdapResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["domainGet"] = domainsrdap.get(
        "v1/domain/{domainName}",
        t.struct({"domainName": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["entityGet"] = domainsrdap.get(
        "v1/entity/{entityId}",
        t.struct({"entityId": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["RdapResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["autnumGet"] = domainsrdap.get(
        "v1/autnum/{autnumId}",
        t.struct({"autnumId": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["RdapResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["ipGet"] = domainsrdap.get(
        "v1/ip/{ipId}/{ipId1}",
        t.struct(
            {"ipId1": t.string(), "ipId": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["RdapResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="domainsrdap",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
