from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_domainsrdap() -> Import:
    domainsrdap = HTTPRuntime("https://domainsrdap.googleapis.com/")

    renames = {
        "ErrorResponse": "_domainsrdap_1_ErrorResponse",
        "NoticeIn": "_domainsrdap_2_NoticeIn",
        "NoticeOut": "_domainsrdap_3_NoticeOut",
        "LinkIn": "_domainsrdap_4_LinkIn",
        "LinkOut": "_domainsrdap_5_LinkOut",
        "HttpBodyIn": "_domainsrdap_6_HttpBodyIn",
        "HttpBodyOut": "_domainsrdap_7_HttpBodyOut",
        "RdapResponseIn": "_domainsrdap_8_RdapResponseIn",
        "RdapResponseOut": "_domainsrdap_9_RdapResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["NoticeIn"] = t.struct(
        {
            "title": t.string().optional(),
            "type": t.string().optional(),
            "description": t.array(t.string()).optional(),
            "links": t.array(t.proxy(renames["LinkIn"])).optional(),
        }
    ).named(renames["NoticeIn"])
    types["NoticeOut"] = t.struct(
        {
            "title": t.string().optional(),
            "type": t.string().optional(),
            "description": t.array(t.string()).optional(),
            "links": t.array(t.proxy(renames["LinkOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NoticeOut"])
    types["LinkIn"] = t.struct(
        {
            "type": t.string().optional(),
            "hreflang": t.string().optional(),
            "value": t.string().optional(),
            "title": t.string().optional(),
            "href": t.string().optional(),
            "rel": t.string().optional(),
            "media": t.string().optional(),
        }
    ).named(renames["LinkIn"])
    types["LinkOut"] = t.struct(
        {
            "type": t.string().optional(),
            "hreflang": t.string().optional(),
            "value": t.string().optional(),
            "title": t.string().optional(),
            "href": t.string().optional(),
            "rel": t.string().optional(),
            "media": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinkOut"])
    types["HttpBodyIn"] = t.struct(
        {
            "extensions": t.array(t.struct({"_": t.string().optional()})).optional(),
            "contentType": t.string().optional(),
            "data": t.string().optional(),
        }
    ).named(renames["HttpBodyIn"])
    types["HttpBodyOut"] = t.struct(
        {
            "extensions": t.array(t.struct({"_": t.string().optional()})).optional(),
            "contentType": t.string().optional(),
            "data": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpBodyOut"])
    types["RdapResponseIn"] = t.struct(
        {
            "title": t.string().optional(),
            "description": t.array(t.string()).optional(),
            "lang": t.string().optional(),
            "rdapConformance": t.array(t.string()).optional(),
            "errorCode": t.integer().optional(),
            "jsonResponse": t.proxy(renames["HttpBodyIn"]).optional(),
            "notices": t.array(t.proxy(renames["NoticeIn"])).optional(),
        }
    ).named(renames["RdapResponseIn"])
    types["RdapResponseOut"] = t.struct(
        {
            "title": t.string().optional(),
            "description": t.array(t.string()).optional(),
            "lang": t.string().optional(),
            "rdapConformance": t.array(t.string()).optional(),
            "errorCode": t.integer().optional(),
            "jsonResponse": t.proxy(renames["HttpBodyOut"]).optional(),
            "notices": t.array(t.proxy(renames["NoticeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RdapResponseOut"])

    functions = {}
    functions["ipGet"] = domainsrdap.get(
        "v1/ip/{ipId}/{ipId1}",
        t.struct(
            {"ipId1": t.string(), "ipId": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["RdapResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1GetNameservers"] = domainsrdap.get(
        "v1/entities",
        t.struct({"auth": t.string().optional()}),
        t.proxy(renames["RdapResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1GetIp"] = domainsrdap.get(
        "v1/entities",
        t.struct({"auth": t.string().optional()}),
        t.proxy(renames["RdapResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1GetDomains"] = domainsrdap.get(
        "v1/entities",
        t.struct({"auth": t.string().optional()}),
        t.proxy(renames["RdapResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1GetHelp"] = domainsrdap.get(
        "v1/entities",
        t.struct({"auth": t.string().optional()}),
        t.proxy(renames["RdapResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1GetEntities"] = domainsrdap.get(
        "v1/entities",
        t.struct({"auth": t.string().optional()}),
        t.proxy(renames["RdapResponseOut"]),
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

    return Import(
        importer="domainsrdap",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
