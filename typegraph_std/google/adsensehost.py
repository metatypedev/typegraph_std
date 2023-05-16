from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_adsensehost() -> Import:
    adsensehost = HTTPRuntime("https://www.googleapis.com/")

    renames = {
        "ErrorResponse": "_adsensehost_1_ErrorResponse",
        "UrlChannelsIn": "_adsensehost_2_UrlChannelsIn",
        "UrlChannelsOut": "_adsensehost_3_UrlChannelsOut",
        "ReportIn": "_adsensehost_4_ReportIn",
        "ReportOut": "_adsensehost_5_ReportOut",
        "CustomChannelIn": "_adsensehost_6_CustomChannelIn",
        "CustomChannelOut": "_adsensehost_7_CustomChannelOut",
        "AdStyleIn": "_adsensehost_8_AdStyleIn",
        "AdStyleOut": "_adsensehost_9_AdStyleOut",
        "AdClientIn": "_adsensehost_10_AdClientIn",
        "AdClientOut": "_adsensehost_11_AdClientOut",
        "CustomChannelsIn": "_adsensehost_12_CustomChannelsIn",
        "CustomChannelsOut": "_adsensehost_13_CustomChannelsOut",
        "AssociationSessionIn": "_adsensehost_14_AssociationSessionIn",
        "AssociationSessionOut": "_adsensehost_15_AssociationSessionOut",
        "AccountIn": "_adsensehost_16_AccountIn",
        "AccountOut": "_adsensehost_17_AccountOut",
        "UrlChannelIn": "_adsensehost_18_UrlChannelIn",
        "UrlChannelOut": "_adsensehost_19_UrlChannelOut",
        "AdCodeIn": "_adsensehost_20_AdCodeIn",
        "AdCodeOut": "_adsensehost_21_AdCodeOut",
        "AdUnitIn": "_adsensehost_22_AdUnitIn",
        "AdUnitOut": "_adsensehost_23_AdUnitOut",
        "AdUnitsIn": "_adsensehost_24_AdUnitsIn",
        "AdUnitsOut": "_adsensehost_25_AdUnitsOut",
        "AdClientsIn": "_adsensehost_26_AdClientsIn",
        "AdClientsOut": "_adsensehost_27_AdClientsOut",
        "AccountsIn": "_adsensehost_28_AccountsIn",
        "AccountsOut": "_adsensehost_29_AccountsOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["UrlChannelsIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["UrlChannelIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["UrlChannelsIn"])
    types["UrlChannelsOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["UrlChannelOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UrlChannelsOut"])
    types["ReportIn"] = t.struct(
        {
            "headers": t.array(
                t.struct(
                    {
                        "name": t.string().optional(),
                        "type": t.string().optional(),
                        "currency": t.string().optional(),
                    }
                )
            ).optional(),
            "warnings": t.array(t.string()).optional(),
            "totals": t.array(t.string()).optional(),
            "kind": t.string().optional(),
            "rows": t.array(t.array(t.string())).optional(),
            "averages": t.array(t.string()).optional(),
            "totalMatchedRows": t.string().optional(),
        }
    ).named(renames["ReportIn"])
    types["ReportOut"] = t.struct(
        {
            "headers": t.array(
                t.struct(
                    {
                        "name": t.string().optional(),
                        "type": t.string().optional(),
                        "currency": t.string().optional(),
                    }
                )
            ).optional(),
            "warnings": t.array(t.string()).optional(),
            "totals": t.array(t.string()).optional(),
            "kind": t.string().optional(),
            "rows": t.array(t.array(t.string())).optional(),
            "averages": t.array(t.string()).optional(),
            "totalMatchedRows": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportOut"])
    types["CustomChannelIn"] = t.struct(
        {
            "id": t.string().optional(),
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "code": t.string().optional(),
        }
    ).named(renames["CustomChannelIn"])
    types["CustomChannelOut"] = t.struct(
        {
            "id": t.string().optional(),
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomChannelOut"])
    types["AdStyleIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "corners": t.string().optional(),
            "font": t.struct(
                {"family": t.string().optional(), "size": t.string().optional()}
            ).optional(),
            "colors": t.struct(
                {
                    "text": t.string().optional(),
                    "background": t.string().optional(),
                    "border": t.string().optional(),
                    "title": t.string().optional(),
                    "url": t.string().optional(),
                }
            ).optional(),
        }
    ).named(renames["AdStyleIn"])
    types["AdStyleOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "corners": t.string().optional(),
            "font": t.struct(
                {"family": t.string().optional(), "size": t.string().optional()}
            ).optional(),
            "colors": t.struct(
                {
                    "text": t.string().optional(),
                    "background": t.string().optional(),
                    "border": t.string().optional(),
                    "title": t.string().optional(),
                    "url": t.string().optional(),
                }
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdStyleOut"])
    types["AdClientIn"] = t.struct(
        {
            "productCode": t.string().optional(),
            "kind": t.string().optional(),
            "arcOptIn": t.boolean().optional(),
            "supportsReporting": t.boolean().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["AdClientIn"])
    types["AdClientOut"] = t.struct(
        {
            "productCode": t.string().optional(),
            "kind": t.string().optional(),
            "arcOptIn": t.boolean().optional(),
            "supportsReporting": t.boolean().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdClientOut"])
    types["CustomChannelsIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["CustomChannelIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["CustomChannelsIn"])
    types["CustomChannelsOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["CustomChannelOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomChannelsOut"])
    types["AssociationSessionIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "websiteLocale": t.string().optional(),
            "websiteUrl": t.string().optional(),
            "id": t.string().optional(),
            "status": t.string().optional(),
            "productCodes": t.array(t.string()).optional(),
            "accountId": t.string().optional(),
            "redirectUrl": t.string().optional(),
            "userLocale": t.string().optional(),
        }
    ).named(renames["AssociationSessionIn"])
    types["AssociationSessionOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "websiteLocale": t.string().optional(),
            "websiteUrl": t.string().optional(),
            "id": t.string().optional(),
            "status": t.string().optional(),
            "productCodes": t.array(t.string()).optional(),
            "accountId": t.string().optional(),
            "redirectUrl": t.string().optional(),
            "userLocale": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssociationSessionOut"])
    types["AccountIn"] = t.struct(
        {
            "name": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "status": t.string().optional(),
        }
    ).named(renames["AccountIn"])
    types["AccountOut"] = t.struct(
        {
            "name": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountOut"])
    types["UrlChannelIn"] = t.struct(
        {
            "id": t.string().optional(),
            "urlPattern": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["UrlChannelIn"])
    types["UrlChannelOut"] = t.struct(
        {
            "id": t.string().optional(),
            "urlPattern": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UrlChannelOut"])
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
    types["AdUnitIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "mobileContentAdsSettings": t.struct(
                {
                    "size": t.string().optional(),
                    "markupLanguage": t.string().optional(),
                    "scriptingLanguage": t.string().optional(),
                    "type": t.string().optional(),
                }
            ).optional(),
            "customStyle": t.proxy(renames["AdStyleIn"]).optional(),
            "code": t.string().optional(),
            "name": t.string().optional(),
            "contentAdsSettings": t.struct(
                {
                    "type": t.string().optional(),
                    "size": t.string().optional(),
                    "backupOption": t.struct(
                        {
                            "color": t.string().optional(),
                            "type": t.string().optional(),
                            "url": t.string().optional(),
                        }
                    ).optional(),
                }
            ).optional(),
            "status": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["AdUnitIn"])
    types["AdUnitOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "mobileContentAdsSettings": t.struct(
                {
                    "size": t.string().optional(),
                    "markupLanguage": t.string().optional(),
                    "scriptingLanguage": t.string().optional(),
                    "type": t.string().optional(),
                }
            ).optional(),
            "customStyle": t.proxy(renames["AdStyleOut"]).optional(),
            "code": t.string().optional(),
            "name": t.string().optional(),
            "contentAdsSettings": t.struct(
                {
                    "type": t.string().optional(),
                    "size": t.string().optional(),
                    "backupOption": t.struct(
                        {
                            "color": t.string().optional(),
                            "type": t.string().optional(),
                            "url": t.string().optional(),
                        }
                    ).optional(),
                }
            ).optional(),
            "status": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdUnitOut"])
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
    types["AdClientsIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["AdClientIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["AdClientsIn"])
    types["AdClientsOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["AdClientOut"])).optional(),
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

    functions = {}
    functions["reportsGenerate"] = adsensehost.get(
        "reports",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "dimension": t.string().optional(),
                "startDate": t.string().optional(),
                "metric": t.string().optional(),
                "filter": t.string().optional(),
                "endDate": t.string().optional(),
                "startIndex": t.integer().optional(),
                "locale": t.string().optional(),
                "sort": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["urlchannelsDelete"] = adsensehost.get(
        "adclients/{adClientId}/urlchannels",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "adClientId": t.string().optional(),
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
                "maxResults": t.integer().optional(),
                "adClientId": t.string().optional(),
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
                "maxResults": t.integer().optional(),
                "adClientId": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UrlChannelsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customchannelsUpdate"] = adsensehost.get(
        "adclients/{adClientId}/customchannels",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "adClientId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomChannelsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customchannelsPatch"] = adsensehost.get(
        "adclients/{adClientId}/customchannels",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "adClientId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomChannelsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customchannelsGet"] = adsensehost.get(
        "adclients/{adClientId}/customchannels",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "adClientId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomChannelsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customchannelsDelete"] = adsensehost.get(
        "adclients/{adClientId}/customchannels",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "adClientId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomChannelsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customchannelsInsert"] = adsensehost.get(
        "adclients/{adClientId}/customchannels",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "adClientId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomChannelsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customchannelsList"] = adsensehost.get(
        "adclients/{adClientId}/customchannels",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "adClientId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomChannelsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsGet"] = adsensehost.get(
        "accounts",
        t.struct(
            {"filterAdClientId": t.string().optional(), "auth": t.string().optional()}
        ),
        t.proxy(renames["AccountsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsList"] = adsensehost.get(
        "accounts",
        t.struct(
            {"filterAdClientId": t.string().optional(), "auth": t.string().optional()}
        ),
        t.proxy(renames["AccountsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsReportsGenerate"] = adsensehost.get(
        "accounts/{accountId}/reports",
        t.struct(
            {
                "startDate": t.string().optional(),
                "maxResults": t.integer().optional(),
                "locale": t.string().optional(),
                "metric": t.string().optional(),
                "sort": t.string().optional(),
                "startIndex": t.integer().optional(),
                "accountId": t.string().optional(),
                "endDate": t.string().optional(),
                "dimension": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdclientsGet"] = adsensehost.get(
        "accounts/{accountId}/adclients",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "accountId": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdClientsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdclientsList"] = adsensehost.get(
        "accounts/{accountId}/adclients",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "accountId": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdClientsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdunitsList"] = adsensehost.put(
        "accounts/{accountId}/adclients/{adClientId}/adunits",
        t.struct(
            {
                "accountId": t.string().optional(),
                "adClientId": t.string().optional(),
                "kind": t.string().optional(),
                "mobileContentAdsSettings": t.struct(
                    {
                        "size": t.string().optional(),
                        "markupLanguage": t.string().optional(),
                        "scriptingLanguage": t.string().optional(),
                        "type": t.string().optional(),
                    }
                ).optional(),
                "customStyle": t.proxy(renames["AdStyleIn"]).optional(),
                "code": t.string().optional(),
                "name": t.string().optional(),
                "contentAdsSettings": t.struct(
                    {
                        "type": t.string().optional(),
                        "size": t.string().optional(),
                        "backupOption": t.struct(
                            {
                                "color": t.string().optional(),
                                "type": t.string().optional(),
                                "url": t.string().optional(),
                            }
                        ).optional(),
                    }
                ).optional(),
                "status": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdUnitOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdunitsGet"] = adsensehost.put(
        "accounts/{accountId}/adclients/{adClientId}/adunits",
        t.struct(
            {
                "accountId": t.string().optional(),
                "adClientId": t.string().optional(),
                "kind": t.string().optional(),
                "mobileContentAdsSettings": t.struct(
                    {
                        "size": t.string().optional(),
                        "markupLanguage": t.string().optional(),
                        "scriptingLanguage": t.string().optional(),
                        "type": t.string().optional(),
                    }
                ).optional(),
                "customStyle": t.proxy(renames["AdStyleIn"]).optional(),
                "code": t.string().optional(),
                "name": t.string().optional(),
                "contentAdsSettings": t.struct(
                    {
                        "type": t.string().optional(),
                        "size": t.string().optional(),
                        "backupOption": t.struct(
                            {
                                "color": t.string().optional(),
                                "type": t.string().optional(),
                                "url": t.string().optional(),
                            }
                        ).optional(),
                    }
                ).optional(),
                "status": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdUnitOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdunitsGetAdCode"] = adsensehost.put(
        "accounts/{accountId}/adclients/{adClientId}/adunits",
        t.struct(
            {
                "accountId": t.string().optional(),
                "adClientId": t.string().optional(),
                "kind": t.string().optional(),
                "mobileContentAdsSettings": t.struct(
                    {
                        "size": t.string().optional(),
                        "markupLanguage": t.string().optional(),
                        "scriptingLanguage": t.string().optional(),
                        "type": t.string().optional(),
                    }
                ).optional(),
                "customStyle": t.proxy(renames["AdStyleIn"]).optional(),
                "code": t.string().optional(),
                "name": t.string().optional(),
                "contentAdsSettings": t.struct(
                    {
                        "type": t.string().optional(),
                        "size": t.string().optional(),
                        "backupOption": t.struct(
                            {
                                "color": t.string().optional(),
                                "type": t.string().optional(),
                                "url": t.string().optional(),
                            }
                        ).optional(),
                    }
                ).optional(),
                "status": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdUnitOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdunitsDelete"] = adsensehost.put(
        "accounts/{accountId}/adclients/{adClientId}/adunits",
        t.struct(
            {
                "accountId": t.string().optional(),
                "adClientId": t.string().optional(),
                "kind": t.string().optional(),
                "mobileContentAdsSettings": t.struct(
                    {
                        "size": t.string().optional(),
                        "markupLanguage": t.string().optional(),
                        "scriptingLanguage": t.string().optional(),
                        "type": t.string().optional(),
                    }
                ).optional(),
                "customStyle": t.proxy(renames["AdStyleIn"]).optional(),
                "code": t.string().optional(),
                "name": t.string().optional(),
                "contentAdsSettings": t.struct(
                    {
                        "type": t.string().optional(),
                        "size": t.string().optional(),
                        "backupOption": t.struct(
                            {
                                "color": t.string().optional(),
                                "type": t.string().optional(),
                                "url": t.string().optional(),
                            }
                        ).optional(),
                    }
                ).optional(),
                "status": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdUnitOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdunitsInsert"] = adsensehost.put(
        "accounts/{accountId}/adclients/{adClientId}/adunits",
        t.struct(
            {
                "accountId": t.string().optional(),
                "adClientId": t.string().optional(),
                "kind": t.string().optional(),
                "mobileContentAdsSettings": t.struct(
                    {
                        "size": t.string().optional(),
                        "markupLanguage": t.string().optional(),
                        "scriptingLanguage": t.string().optional(),
                        "type": t.string().optional(),
                    }
                ).optional(),
                "customStyle": t.proxy(renames["AdStyleIn"]).optional(),
                "code": t.string().optional(),
                "name": t.string().optional(),
                "contentAdsSettings": t.struct(
                    {
                        "type": t.string().optional(),
                        "size": t.string().optional(),
                        "backupOption": t.struct(
                            {
                                "color": t.string().optional(),
                                "type": t.string().optional(),
                                "url": t.string().optional(),
                            }
                        ).optional(),
                    }
                ).optional(),
                "status": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdUnitOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdunitsPatch"] = adsensehost.put(
        "accounts/{accountId}/adclients/{adClientId}/adunits",
        t.struct(
            {
                "accountId": t.string().optional(),
                "adClientId": t.string().optional(),
                "kind": t.string().optional(),
                "mobileContentAdsSettings": t.struct(
                    {
                        "size": t.string().optional(),
                        "markupLanguage": t.string().optional(),
                        "scriptingLanguage": t.string().optional(),
                        "type": t.string().optional(),
                    }
                ).optional(),
                "customStyle": t.proxy(renames["AdStyleIn"]).optional(),
                "code": t.string().optional(),
                "name": t.string().optional(),
                "contentAdsSettings": t.struct(
                    {
                        "type": t.string().optional(),
                        "size": t.string().optional(),
                        "backupOption": t.struct(
                            {
                                "color": t.string().optional(),
                                "type": t.string().optional(),
                                "url": t.string().optional(),
                            }
                        ).optional(),
                    }
                ).optional(),
                "status": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdUnitOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdunitsUpdate"] = adsensehost.put(
        "accounts/{accountId}/adclients/{adClientId}/adunits",
        t.struct(
            {
                "accountId": t.string().optional(),
                "adClientId": t.string().optional(),
                "kind": t.string().optional(),
                "mobileContentAdsSettings": t.struct(
                    {
                        "size": t.string().optional(),
                        "markupLanguage": t.string().optional(),
                        "scriptingLanguage": t.string().optional(),
                        "type": t.string().optional(),
                    }
                ).optional(),
                "customStyle": t.proxy(renames["AdStyleIn"]).optional(),
                "code": t.string().optional(),
                "name": t.string().optional(),
                "contentAdsSettings": t.struct(
                    {
                        "type": t.string().optional(),
                        "size": t.string().optional(),
                        "backupOption": t.struct(
                            {
                                "color": t.string().optional(),
                                "type": t.string().optional(),
                                "url": t.string().optional(),
                            }
                        ).optional(),
                    }
                ).optional(),
                "status": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdUnitOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["associationsessionsVerify"] = adsensehost.get(
        "associationsessions/start",
        t.struct(
            {
                "callbackUrl": t.string().optional(),
                "userLocale": t.string().optional(),
                "productCode": t.string().optional(),
                "websiteUrl": t.string().optional(),
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
                "callbackUrl": t.string().optional(),
                "userLocale": t.string().optional(),
                "productCode": t.string().optional(),
                "websiteUrl": t.string().optional(),
                "websiteLocale": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssociationSessionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adclientsGet"] = adsensehost.get(
        "adclients",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "maxResults": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "maxResults": t.integer().optional(),
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
