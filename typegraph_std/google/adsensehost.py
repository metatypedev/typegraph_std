from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_adsensehost() -> Import:
    adsensehost = HTTPRuntime("https://www.googleapis.com/")

    renames = {
        "ErrorResponse": "_adsensehost_1_ErrorResponse",
        "CustomChannelsIn": "_adsensehost_2_CustomChannelsIn",
        "CustomChannelsOut": "_adsensehost_3_CustomChannelsOut",
        "AdUnitsIn": "_adsensehost_4_AdUnitsIn",
        "AdUnitsOut": "_adsensehost_5_AdUnitsOut",
        "UrlChannelIn": "_adsensehost_6_UrlChannelIn",
        "UrlChannelOut": "_adsensehost_7_UrlChannelOut",
        "UrlChannelsIn": "_adsensehost_8_UrlChannelsIn",
        "UrlChannelsOut": "_adsensehost_9_UrlChannelsOut",
        "AdClientsIn": "_adsensehost_10_AdClientsIn",
        "AdClientsOut": "_adsensehost_11_AdClientsOut",
        "AccountsIn": "_adsensehost_12_AccountsIn",
        "AccountsOut": "_adsensehost_13_AccountsOut",
        "AccountIn": "_adsensehost_14_AccountIn",
        "AccountOut": "_adsensehost_15_AccountOut",
        "AdCodeIn": "_adsensehost_16_AdCodeIn",
        "AdCodeOut": "_adsensehost_17_AdCodeOut",
        "CustomChannelIn": "_adsensehost_18_CustomChannelIn",
        "CustomChannelOut": "_adsensehost_19_CustomChannelOut",
        "AssociationSessionIn": "_adsensehost_20_AssociationSessionIn",
        "AssociationSessionOut": "_adsensehost_21_AssociationSessionOut",
        "AdClientIn": "_adsensehost_22_AdClientIn",
        "AdClientOut": "_adsensehost_23_AdClientOut",
        "ReportIn": "_adsensehost_24_ReportIn",
        "ReportOut": "_adsensehost_25_ReportOut",
        "AdStyleIn": "_adsensehost_26_AdStyleIn",
        "AdStyleOut": "_adsensehost_27_AdStyleOut",
        "AdUnitIn": "_adsensehost_28_AdUnitIn",
        "AdUnitOut": "_adsensehost_29_AdUnitOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["AdUnitsIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["AdUnitIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "etag": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["AdUnitsIn"])
    types["AdUnitsOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["AdUnitOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "etag": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdUnitsOut"])
    types["UrlChannelIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "urlPattern": t.string().optional(),
        }
    ).named(renames["UrlChannelIn"])
    types["UrlChannelOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "urlPattern": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UrlChannelOut"])
    types["UrlChannelsIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["UrlChannelIn"])).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["UrlChannelsIn"])
    types["UrlChannelsOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["UrlChannelOut"])).optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UrlChannelsOut"])
    types["AdClientsIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["AdClientIn"])).optional(),
            "etag": t.string().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["AdClientsIn"])
    types["AdClientsOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["AdClientOut"])).optional(),
            "etag": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdClientsOut"])
    types["AccountsIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "items": t.array(t.proxy(renames["AccountIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["AccountsIn"])
    types["AccountsOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "items": t.array(t.proxy(renames["AccountOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountsOut"])
    types["AccountIn"] = t.struct(
        {
            "name": t.string().optional(),
            "status": t.string().optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["AccountIn"])
    types["AccountOut"] = t.struct(
        {
            "name": t.string().optional(),
            "status": t.string().optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountOut"])
    types["AdCodeIn"] = t.struct(
        {"adCode": t.string().optional(), "kind": t.string().optional()}
    ).named(renames["AdCodeIn"])
    types["AdCodeOut"] = t.struct(
        {
            "adCode": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdCodeOut"])
    types["CustomChannelIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "code": t.string().optional(),
            "name": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["CustomChannelIn"])
    types["CustomChannelOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "code": t.string().optional(),
            "name": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomChannelOut"])
    types["AssociationSessionIn"] = t.struct(
        {
            "redirectUrl": t.string().optional(),
            "websiteLocale": t.string().optional(),
            "websiteUrl": t.string().optional(),
            "productCodes": t.array(t.string()).optional(),
            "status": t.string().optional(),
            "id": t.string().optional(),
            "userLocale": t.string().optional(),
            "accountId": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["AssociationSessionIn"])
    types["AssociationSessionOut"] = t.struct(
        {
            "redirectUrl": t.string().optional(),
            "websiteLocale": t.string().optional(),
            "websiteUrl": t.string().optional(),
            "productCodes": t.array(t.string()).optional(),
            "status": t.string().optional(),
            "id": t.string().optional(),
            "userLocale": t.string().optional(),
            "accountId": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssociationSessionOut"])
    types["AdClientIn"] = t.struct(
        {
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "arcOptIn": t.boolean().optional(),
            "productCode": t.string().optional(),
            "supportsReporting": t.boolean().optional(),
        }
    ).named(renames["AdClientIn"])
    types["AdClientOut"] = t.struct(
        {
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "arcOptIn": t.boolean().optional(),
            "productCode": t.string().optional(),
            "supportsReporting": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdClientOut"])
    types["ReportIn"] = t.struct(
        {
            "rows": t.array(t.array(t.string())).optional(),
            "kind": t.string().optional(),
            "totalMatchedRows": t.string().optional(),
            "averages": t.array(t.string()).optional(),
            "headers": t.array(
                t.struct(
                    {
                        "type": t.string().optional(),
                        "currency": t.string().optional(),
                        "name": t.string().optional(),
                    }
                )
            ).optional(),
            "warnings": t.array(t.string()).optional(),
            "totals": t.array(t.string()).optional(),
        }
    ).named(renames["ReportIn"])
    types["ReportOut"] = t.struct(
        {
            "rows": t.array(t.array(t.string())).optional(),
            "kind": t.string().optional(),
            "totalMatchedRows": t.string().optional(),
            "averages": t.array(t.string()).optional(),
            "headers": t.array(
                t.struct(
                    {
                        "type": t.string().optional(),
                        "currency": t.string().optional(),
                        "name": t.string().optional(),
                    }
                )
            ).optional(),
            "warnings": t.array(t.string()).optional(),
            "totals": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportOut"])
    types["AdStyleIn"] = t.struct(
        {
            "corners": t.string().optional(),
            "font": t.struct(
                {"size": t.string().optional(), "family": t.string().optional()}
            ).optional(),
            "colors": t.struct(
                {
                    "title": t.string().optional(),
                    "url": t.string().optional(),
                    "text": t.string().optional(),
                    "border": t.string().optional(),
                    "background": t.string().optional(),
                }
            ).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["AdStyleIn"])
    types["AdStyleOut"] = t.struct(
        {
            "corners": t.string().optional(),
            "font": t.struct(
                {"size": t.string().optional(), "family": t.string().optional()}
            ).optional(),
            "colors": t.struct(
                {
                    "title": t.string().optional(),
                    "url": t.string().optional(),
                    "text": t.string().optional(),
                    "border": t.string().optional(),
                    "background": t.string().optional(),
                }
            ).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdStyleOut"])
    types["AdUnitIn"] = t.struct(
        {
            "name": t.string().optional(),
            "contentAdsSettings": t.struct(
                {
                    "size": t.string().optional(),
                    "backupOption": t.struct(
                        {
                            "url": t.string().optional(),
                            "type": t.string().optional(),
                            "color": t.string().optional(),
                        }
                    ).optional(),
                    "type": t.string().optional(),
                }
            ).optional(),
            "status": t.string().optional(),
            "mobileContentAdsSettings": t.struct(
                {
                    "scriptingLanguage": t.string().optional(),
                    "markupLanguage": t.string().optional(),
                    "type": t.string().optional(),
                    "size": t.string().optional(),
                }
            ).optional(),
            "customStyle": t.proxy(renames["AdStyleIn"]).optional(),
            "id": t.string().optional(),
            "code": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["AdUnitIn"])
    types["AdUnitOut"] = t.struct(
        {
            "name": t.string().optional(),
            "contentAdsSettings": t.struct(
                {
                    "size": t.string().optional(),
                    "backupOption": t.struct(
                        {
                            "url": t.string().optional(),
                            "type": t.string().optional(),
                            "color": t.string().optional(),
                        }
                    ).optional(),
                    "type": t.string().optional(),
                }
            ).optional(),
            "status": t.string().optional(),
            "mobileContentAdsSettings": t.struct(
                {
                    "scriptingLanguage": t.string().optional(),
                    "markupLanguage": t.string().optional(),
                    "type": t.string().optional(),
                    "size": t.string().optional(),
                }
            ).optional(),
            "customStyle": t.proxy(renames["AdStyleOut"]).optional(),
            "id": t.string().optional(),
            "code": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdUnitOut"])

    functions = {}
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
    functions["accountsAdclientsList"] = adsensehost.get(
        "accounts/{accountId}/adclients/{adClientId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "adClientId": t.string().optional(),
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
                "accountId": t.string().optional(),
                "adClientId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdClientOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsReportsGenerate"] = adsensehost.get(
        "accounts/{accountId}/reports",
        t.struct(
            {
                "startIndex": t.integer().optional(),
                "locale": t.string().optional(),
                "dimension": t.string().optional(),
                "sort": t.string().optional(),
                "endDate": t.string().optional(),
                "accountId": t.string().optional(),
                "filter": t.string().optional(),
                "maxResults": t.integer().optional(),
                "startDate": t.string().optional(),
                "metric": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdunitsPatch"] = adsensehost.delete(
        "accounts/{accountId}/adclients/{adClientId}/adunits/{adUnitId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "adUnitId": t.string().optional(),
                "adClientId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdUnitOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdunitsGet"] = adsensehost.delete(
        "accounts/{accountId}/adclients/{adClientId}/adunits/{adUnitId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "adUnitId": t.string().optional(),
                "adClientId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdUnitOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdunitsGetAdCode"] = adsensehost.delete(
        "accounts/{accountId}/adclients/{adClientId}/adunits/{adUnitId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "adUnitId": t.string().optional(),
                "adClientId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdUnitOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdunitsUpdate"] = adsensehost.delete(
        "accounts/{accountId}/adclients/{adClientId}/adunits/{adUnitId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "adUnitId": t.string().optional(),
                "adClientId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdUnitOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdunitsList"] = adsensehost.delete(
        "accounts/{accountId}/adclients/{adClientId}/adunits/{adUnitId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "adUnitId": t.string().optional(),
                "adClientId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdUnitOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdunitsInsert"] = adsensehost.delete(
        "accounts/{accountId}/adclients/{adClientId}/adunits/{adUnitId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "adUnitId": t.string().optional(),
                "adClientId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdUnitOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdunitsDelete"] = adsensehost.delete(
        "accounts/{accountId}/adclients/{adClientId}/adunits/{adUnitId}",
        t.struct(
            {
                "accountId": t.string().optional(),
                "adUnitId": t.string().optional(),
                "adClientId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdUnitOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["urlchannelsDelete"] = adsensehost.get(
        "adclients/{adClientId}/urlchannels",
        t.struct(
            {
                "adClientId": t.string().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UrlChannelsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["urlchannelsInsert"] = adsensehost.get(
        "adclients/{adClientId}/urlchannels",
        t.struct(
            {
                "adClientId": t.string().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UrlChannelsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["urlchannelsList"] = adsensehost.get(
        "adclients/{adClientId}/urlchannels",
        t.struct(
            {
                "adClientId": t.string().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UrlChannelsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["associationsessionsStart"] = adsensehost.get(
        "associationsessions/verify",
        t.struct({"token": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["AssociationSessionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["associationsessionsVerify"] = adsensehost.get(
        "associationsessions/verify",
        t.struct({"token": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["AssociationSessionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["reportsGenerate"] = adsensehost.get(
        "reports",
        t.struct(
            {
                "endDate": t.string().optional(),
                "startDate": t.string().optional(),
                "sort": t.string().optional(),
                "filter": t.string().optional(),
                "dimension": t.string().optional(),
                "locale": t.string().optional(),
                "maxResults": t.integer().optional(),
                "startIndex": t.integer().optional(),
                "metric": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adclientsList"] = adsensehost.get(
        "adclients/{adClientId}",
        t.struct({"adClientId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["AdClientOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adclientsGet"] = adsensehost.get(
        "adclients/{adClientId}",
        t.struct({"adClientId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["AdClientOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customchannelsGet"] = adsensehost.put(
        "adclients/{adClientId}/customchannels",
        t.struct(
            {
                "adClientId": t.string().optional(),
                "kind": t.string().optional(),
                "code": t.string().optional(),
                "name": t.string().optional(),
                "id": t.string().optional(),
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
                "code": t.string().optional(),
                "name": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customchannelsList"] = adsensehost.put(
        "adclients/{adClientId}/customchannels",
        t.struct(
            {
                "adClientId": t.string().optional(),
                "kind": t.string().optional(),
                "code": t.string().optional(),
                "name": t.string().optional(),
                "id": t.string().optional(),
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
                "code": t.string().optional(),
                "name": t.string().optional(),
                "id": t.string().optional(),
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
                "code": t.string().optional(),
                "name": t.string().optional(),
                "id": t.string().optional(),
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
                "code": t.string().optional(),
                "name": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="adsensehost", renames=renames, types=types, functions=functions
    )
