from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_adsensehost() -> Import:
    adsensehost = HTTPRuntime("https://www.googleapis.com/")

    renames = {
        "ErrorResponse": "_adsensehost_1_ErrorResponse",
        "AdClientsIn": "_adsensehost_2_AdClientsIn",
        "AdClientsOut": "_adsensehost_3_AdClientsOut",
        "AccountsIn": "_adsensehost_4_AccountsIn",
        "AccountsOut": "_adsensehost_5_AccountsOut",
        "ReportIn": "_adsensehost_6_ReportIn",
        "ReportOut": "_adsensehost_7_ReportOut",
        "AdUnitIn": "_adsensehost_8_AdUnitIn",
        "AdUnitOut": "_adsensehost_9_AdUnitOut",
        "AdCodeIn": "_adsensehost_10_AdCodeIn",
        "AdCodeOut": "_adsensehost_11_AdCodeOut",
        "AccountIn": "_adsensehost_12_AccountIn",
        "AccountOut": "_adsensehost_13_AccountOut",
        "CustomChannelsIn": "_adsensehost_14_CustomChannelsIn",
        "CustomChannelsOut": "_adsensehost_15_CustomChannelsOut",
        "AdStyleIn": "_adsensehost_16_AdStyleIn",
        "AdStyleOut": "_adsensehost_17_AdStyleOut",
        "UrlChannelsIn": "_adsensehost_18_UrlChannelsIn",
        "UrlChannelsOut": "_adsensehost_19_UrlChannelsOut",
        "CustomChannelIn": "_adsensehost_20_CustomChannelIn",
        "CustomChannelOut": "_adsensehost_21_CustomChannelOut",
        "AdUnitsIn": "_adsensehost_22_AdUnitsIn",
        "AdUnitsOut": "_adsensehost_23_AdUnitsOut",
        "AssociationSessionIn": "_adsensehost_24_AssociationSessionIn",
        "AssociationSessionOut": "_adsensehost_25_AssociationSessionOut",
        "AdClientIn": "_adsensehost_26_AdClientIn",
        "AdClientOut": "_adsensehost_27_AdClientOut",
        "UrlChannelIn": "_adsensehost_28_UrlChannelIn",
        "UrlChannelOut": "_adsensehost_29_UrlChannelOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["AdClientsIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["AdClientIn"])).optional(),
        }
    ).named(renames["AdClientsIn"])
    types["AdClientsOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["AdClientOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdClientsOut"])
    types["AccountsIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "items": t.array(t.proxy(renames["AccountIn"])).optional(),
        }
    ).named(renames["AccountsIn"])
    types["AccountsOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "items": t.array(t.proxy(renames["AccountOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountsOut"])
    types["ReportIn"] = t.struct(
        {
            "rows": t.array(t.array(t.string())).optional(),
            "warnings": t.array(t.string()).optional(),
            "totals": t.array(t.string()).optional(),
            "kind": t.string().optional(),
            "headers": t.array(
                t.struct(
                    {
                        "currency": t.string().optional(),
                        "name": t.string().optional(),
                        "type": t.string().optional(),
                    }
                )
            ).optional(),
            "totalMatchedRows": t.string().optional(),
            "averages": t.array(t.string()).optional(),
        }
    ).named(renames["ReportIn"])
    types["ReportOut"] = t.struct(
        {
            "rows": t.array(t.array(t.string())).optional(),
            "warnings": t.array(t.string()).optional(),
            "totals": t.array(t.string()).optional(),
            "kind": t.string().optional(),
            "headers": t.array(
                t.struct(
                    {
                        "currency": t.string().optional(),
                        "name": t.string().optional(),
                        "type": t.string().optional(),
                    }
                )
            ).optional(),
            "totalMatchedRows": t.string().optional(),
            "averages": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportOut"])
    types["AdUnitIn"] = t.struct(
        {
            "status": t.string().optional(),
            "contentAdsSettings": t.struct(
                {
                    "backupOption": t.struct(
                        {
                            "type": t.string().optional(),
                            "url": t.string().optional(),
                            "color": t.string().optional(),
                        }
                    ).optional(),
                    "size": t.string().optional(),
                    "type": t.string().optional(),
                }
            ).optional(),
            "mobileContentAdsSettings": t.struct(
                {
                    "scriptingLanguage": t.string().optional(),
                    "type": t.string().optional(),
                    "size": t.string().optional(),
                    "markupLanguage": t.string().optional(),
                }
            ).optional(),
            "code": t.string().optional(),
            "name": t.string().optional(),
            "customStyle": t.proxy(renames["AdStyleIn"]).optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["AdUnitIn"])
    types["AdUnitOut"] = t.struct(
        {
            "status": t.string().optional(),
            "contentAdsSettings": t.struct(
                {
                    "backupOption": t.struct(
                        {
                            "type": t.string().optional(),
                            "url": t.string().optional(),
                            "color": t.string().optional(),
                        }
                    ).optional(),
                    "size": t.string().optional(),
                    "type": t.string().optional(),
                }
            ).optional(),
            "mobileContentAdsSettings": t.struct(
                {
                    "scriptingLanguage": t.string().optional(),
                    "type": t.string().optional(),
                    "size": t.string().optional(),
                    "markupLanguage": t.string().optional(),
                }
            ).optional(),
            "code": t.string().optional(),
            "name": t.string().optional(),
            "customStyle": t.proxy(renames["AdStyleOut"]).optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdUnitOut"])
    types["AdCodeIn"] = t.struct(
        {"kind": t.string().optional(), "adCode": t.string().optional()}
    ).named(renames["AdCodeIn"])
    types["AdCodeOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "adCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdCodeOut"])
    types["AccountIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "status": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["AccountIn"])
    types["AccountOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "status": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountOut"])
    types["CustomChannelsIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "etag": t.string().optional(),
            "items": t.array(t.proxy(renames["CustomChannelIn"])).optional(),
        }
    ).named(renames["CustomChannelsIn"])
    types["CustomChannelsOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "etag": t.string().optional(),
            "items": t.array(t.proxy(renames["CustomChannelOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomChannelsOut"])
    types["AdStyleIn"] = t.struct(
        {
            "font": t.struct(
                {"family": t.string().optional(), "size": t.string().optional()}
            ).optional(),
            "colors": t.struct(
                {
                    "text": t.string().optional(),
                    "border": t.string().optional(),
                    "background": t.string().optional(),
                    "title": t.string().optional(),
                    "url": t.string().optional(),
                }
            ).optional(),
            "kind": t.string().optional(),
            "corners": t.string().optional(),
        }
    ).named(renames["AdStyleIn"])
    types["AdStyleOut"] = t.struct(
        {
            "font": t.struct(
                {"family": t.string().optional(), "size": t.string().optional()}
            ).optional(),
            "colors": t.struct(
                {
                    "text": t.string().optional(),
                    "border": t.string().optional(),
                    "background": t.string().optional(),
                    "title": t.string().optional(),
                    "url": t.string().optional(),
                }
            ).optional(),
            "kind": t.string().optional(),
            "corners": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdStyleOut"])
    types["UrlChannelsIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["UrlChannelIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["UrlChannelsIn"])
    types["UrlChannelsOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["UrlChannelOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UrlChannelsOut"])
    types["CustomChannelIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "id": t.string().optional(),
            "code": t.string().optional(),
        }
    ).named(renames["CustomChannelIn"])
    types["CustomChannelOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "id": t.string().optional(),
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomChannelOut"])
    types["AdUnitsIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "items": t.array(t.proxy(renames["AdUnitIn"])).optional(),
        }
    ).named(renames["AdUnitsIn"])
    types["AdUnitsOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "items": t.array(t.proxy(renames["AdUnitOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdUnitsOut"])
    types["AssociationSessionIn"] = t.struct(
        {
            "redirectUrl": t.string().optional(),
            "websiteLocale": t.string().optional(),
            "websiteUrl": t.string().optional(),
            "userLocale": t.string().optional(),
            "productCodes": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "accountId": t.string().optional(),
            "status": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["AssociationSessionIn"])
    types["AssociationSessionOut"] = t.struct(
        {
            "redirectUrl": t.string().optional(),
            "websiteLocale": t.string().optional(),
            "websiteUrl": t.string().optional(),
            "userLocale": t.string().optional(),
            "productCodes": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "accountId": t.string().optional(),
            "status": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssociationSessionOut"])
    types["AdClientIn"] = t.struct(
        {
            "productCode": t.string().optional(),
            "kind": t.string().optional(),
            "supportsReporting": t.boolean().optional(),
            "arcOptIn": t.boolean().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["AdClientIn"])
    types["AdClientOut"] = t.struct(
        {
            "productCode": t.string().optional(),
            "kind": t.string().optional(),
            "supportsReporting": t.boolean().optional(),
            "arcOptIn": t.boolean().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdClientOut"])
    types["UrlChannelIn"] = t.struct(
        {
            "urlPattern": t.string().optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["UrlChannelIn"])
    types["UrlChannelOut"] = t.struct(
        {
            "urlPattern": t.string().optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UrlChannelOut"])

    functions = {}
    functions["urlchannelsList"] = adsensehost.delete(
        "adclients/{adClientId}/urlchannels/{urlChannelId}",
        t.struct(
            {
                "urlChannelId": t.string().optional(),
                "adClientId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UrlChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["urlchannelsInsert"] = adsensehost.delete(
        "adclients/{adClientId}/urlchannels/{urlChannelId}",
        t.struct(
            {
                "urlChannelId": t.string().optional(),
                "adClientId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UrlChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["urlchannelsDelete"] = adsensehost.delete(
        "adclients/{adClientId}/urlchannels/{urlChannelId}",
        t.struct(
            {
                "urlChannelId": t.string().optional(),
                "adClientId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UrlChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["associationsessionsVerify"] = adsensehost.get(
        "associationsessions/start",
        t.struct(
            {
                "websiteUrl": t.string().optional(),
                "productCode": t.string().optional(),
                "userLocale": t.string().optional(),
                "callbackUrl": t.string().optional(),
                "websiteLocale": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssociationSessionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["associationsessionsStart"] = adsensehost.get(
        "associationsessions/start",
        t.struct(
            {
                "websiteUrl": t.string().optional(),
                "productCode": t.string().optional(),
                "userLocale": t.string().optional(),
                "callbackUrl": t.string().optional(),
                "websiteLocale": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssociationSessionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsList"] = adsensehost.get(
        "accounts/{accountId}",
        t.struct({"accountId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["AccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsGet"] = adsensehost.get(
        "accounts/{accountId}",
        t.struct({"accountId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["AccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsReportsGenerate"] = adsensehost.get(
        "accounts/{accountId}/reports",
        t.struct(
            {
                "startDate": t.string().optional(),
                "sort": t.string().optional(),
                "filter": t.string().optional(),
                "dimension": t.string().optional(),
                "maxResults": t.integer().optional(),
                "startIndex": t.integer().optional(),
                "endDate": t.string().optional(),
                "metric": t.string().optional(),
                "locale": t.string().optional(),
                "accountId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdclientsList"] = adsensehost.get(
        "accounts/{accountId}/adclients/{adClientId}",
        t.struct(
            {
                "adClientId": t.string().optional(),
                "accountId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdClientOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdclientsGet"] = adsensehost.get(
        "accounts/{accountId}/adclients/{adClientId}",
        t.struct(
            {
                "adClientId": t.string().optional(),
                "accountId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdClientOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdunitsList"] = adsensehost.get(
        "accounts/{accountId}/adclients/{adClientId}/adunits/{adUnitId}",
        t.struct(
            {
                "adClientId": t.string().optional(),
                "accountId": t.string().optional(),
                "adUnitId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdUnitOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdunitsGetAdCode"] = adsensehost.get(
        "accounts/{accountId}/adclients/{adClientId}/adunits/{adUnitId}",
        t.struct(
            {
                "adClientId": t.string().optional(),
                "accountId": t.string().optional(),
                "adUnitId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdUnitOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdunitsPatch"] = adsensehost.get(
        "accounts/{accountId}/adclients/{adClientId}/adunits/{adUnitId}",
        t.struct(
            {
                "adClientId": t.string().optional(),
                "accountId": t.string().optional(),
                "adUnitId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdUnitOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdunitsDelete"] = adsensehost.get(
        "accounts/{accountId}/adclients/{adClientId}/adunits/{adUnitId}",
        t.struct(
            {
                "adClientId": t.string().optional(),
                "accountId": t.string().optional(),
                "adUnitId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdUnitOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdunitsUpdate"] = adsensehost.get(
        "accounts/{accountId}/adclients/{adClientId}/adunits/{adUnitId}",
        t.struct(
            {
                "adClientId": t.string().optional(),
                "accountId": t.string().optional(),
                "adUnitId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdUnitOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdunitsInsert"] = adsensehost.get(
        "accounts/{accountId}/adclients/{adClientId}/adunits/{adUnitId}",
        t.struct(
            {
                "adClientId": t.string().optional(),
                "accountId": t.string().optional(),
                "adUnitId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdUnitOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdunitsGet"] = adsensehost.get(
        "accounts/{accountId}/adclients/{adClientId}/adunits/{adUnitId}",
        t.struct(
            {
                "adClientId": t.string().optional(),
                "accountId": t.string().optional(),
                "adUnitId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdUnitOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customchannelsList"] = adsensehost.put(
        "adclients/{adClientId}/customchannels",
        t.struct(
            {
                "adClientId": t.string().optional(),
                "kind": t.string().optional(),
                "name": t.string().optional(),
                "id": t.string().optional(),
                "code": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customchannelsDelete"] = adsensehost.put(
        "adclients/{adClientId}/customchannels",
        t.struct(
            {
                "adClientId": t.string().optional(),
                "kind": t.string().optional(),
                "name": t.string().optional(),
                "id": t.string().optional(),
                "code": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customchannelsPatch"] = adsensehost.put(
        "adclients/{adClientId}/customchannels",
        t.struct(
            {
                "adClientId": t.string().optional(),
                "kind": t.string().optional(),
                "name": t.string().optional(),
                "id": t.string().optional(),
                "code": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customchannelsGet"] = adsensehost.put(
        "adclients/{adClientId}/customchannels",
        t.struct(
            {
                "adClientId": t.string().optional(),
                "kind": t.string().optional(),
                "name": t.string().optional(),
                "id": t.string().optional(),
                "code": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customchannelsInsert"] = adsensehost.put(
        "adclients/{adClientId}/customchannels",
        t.struct(
            {
                "adClientId": t.string().optional(),
                "kind": t.string().optional(),
                "name": t.string().optional(),
                "id": t.string().optional(),
                "code": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customchannelsUpdate"] = adsensehost.put(
        "adclients/{adClientId}/customchannels",
        t.struct(
            {
                "adClientId": t.string().optional(),
                "kind": t.string().optional(),
                "name": t.string().optional(),
                "id": t.string().optional(),
                "code": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["reportsGenerate"] = adsensehost.get(
        "reports",
        t.struct(
            {
                "endDate": t.string().optional(),
                "maxResults": t.integer().optional(),
                "sort": t.string().optional(),
                "startIndex": t.integer().optional(),
                "locale": t.string().optional(),
                "startDate": t.string().optional(),
                "metric": t.string().optional(),
                "dimension": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adclientsGet"] = adsensehost.get(
        "adclients",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdClientsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adclientsList"] = adsensehost.get(
        "adclients",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdClientsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="adsensehost",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
