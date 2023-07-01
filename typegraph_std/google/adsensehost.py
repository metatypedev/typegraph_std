from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_adsensehost():
    adsensehost = HTTPRuntime("https://www.googleapis.com/")

    renames = {
        "ErrorResponse": "_adsensehost_1_ErrorResponse",
        "AdCodeIn": "_adsensehost_2_AdCodeIn",
        "AdCodeOut": "_adsensehost_3_AdCodeOut",
        "AdUnitIn": "_adsensehost_4_AdUnitIn",
        "AdUnitOut": "_adsensehost_5_AdUnitOut",
        "AdUnitsIn": "_adsensehost_6_AdUnitsIn",
        "AdUnitsOut": "_adsensehost_7_AdUnitsOut",
        "AdStyleIn": "_adsensehost_8_AdStyleIn",
        "AdStyleOut": "_adsensehost_9_AdStyleOut",
        "AccountIn": "_adsensehost_10_AccountIn",
        "AccountOut": "_adsensehost_11_AccountOut",
        "AssociationSessionIn": "_adsensehost_12_AssociationSessionIn",
        "AssociationSessionOut": "_adsensehost_13_AssociationSessionOut",
        "AccountsIn": "_adsensehost_14_AccountsIn",
        "AccountsOut": "_adsensehost_15_AccountsOut",
        "UrlChannelsIn": "_adsensehost_16_UrlChannelsIn",
        "UrlChannelsOut": "_adsensehost_17_UrlChannelsOut",
        "ReportIn": "_adsensehost_18_ReportIn",
        "ReportOut": "_adsensehost_19_ReportOut",
        "AdClientIn": "_adsensehost_20_AdClientIn",
        "AdClientOut": "_adsensehost_21_AdClientOut",
        "CustomChannelsIn": "_adsensehost_22_CustomChannelsIn",
        "CustomChannelsOut": "_adsensehost_23_CustomChannelsOut",
        "UrlChannelIn": "_adsensehost_24_UrlChannelIn",
        "UrlChannelOut": "_adsensehost_25_UrlChannelOut",
        "CustomChannelIn": "_adsensehost_26_CustomChannelIn",
        "CustomChannelOut": "_adsensehost_27_CustomChannelOut",
        "AdClientsIn": "_adsensehost_28_AdClientsIn",
        "AdClientsOut": "_adsensehost_29_AdClientsOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
            "id": t.string().optional(),
            "code": t.string().optional(),
            "customStyle": t.proxy(renames["AdStyleIn"]).optional(),
            "name": t.string().optional(),
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
            "kind": t.string().optional(),
            "mobileContentAdsSettings": t.struct(
                {
                    "size": t.string().optional(),
                    "scriptingLanguage": t.string().optional(),
                    "type": t.string().optional(),
                    "markupLanguage": t.string().optional(),
                }
            ).optional(),
            "status": t.string().optional(),
        }
    ).named(renames["AdUnitIn"])
    types["AdUnitOut"] = t.struct(
        {
            "id": t.string().optional(),
            "code": t.string().optional(),
            "customStyle": t.proxy(renames["AdStyleOut"]).optional(),
            "name": t.string().optional(),
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
            "kind": t.string().optional(),
            "mobileContentAdsSettings": t.struct(
                {
                    "size": t.string().optional(),
                    "scriptingLanguage": t.string().optional(),
                    "type": t.string().optional(),
                    "markupLanguage": t.string().optional(),
                }
            ).optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdUnitOut"])
    types["AdUnitsIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["AdUnitIn"])).optional(),
        }
    ).named(renames["AdUnitsIn"])
    types["AdUnitsOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["AdUnitOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdUnitsOut"])
    types["AdStyleIn"] = t.struct(
        {
            "font": t.struct(
                {"size": t.string().optional(), "family": t.string().optional()}
            ).optional(),
            "corners": t.string().optional(),
            "kind": t.string().optional(),
            "colors": t.struct(
                {
                    "title": t.string().optional(),
                    "background": t.string().optional(),
                    "border": t.string().optional(),
                    "url": t.string().optional(),
                    "text": t.string().optional(),
                }
            ).optional(),
        }
    ).named(renames["AdStyleIn"])
    types["AdStyleOut"] = t.struct(
        {
            "font": t.struct(
                {"size": t.string().optional(), "family": t.string().optional()}
            ).optional(),
            "corners": t.string().optional(),
            "kind": t.string().optional(),
            "colors": t.struct(
                {
                    "title": t.string().optional(),
                    "background": t.string().optional(),
                    "border": t.string().optional(),
                    "url": t.string().optional(),
                    "text": t.string().optional(),
                }
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdStyleOut"])
    types["AccountIn"] = t.struct(
        {
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "status": t.string().optional(),
        }
    ).named(renames["AccountIn"])
    types["AccountOut"] = t.struct(
        {
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountOut"])
    types["AssociationSessionIn"] = t.struct(
        {
            "status": t.string().optional(),
            "accountId": t.string().optional(),
            "websiteLocale": t.string().optional(),
            "redirectUrl": t.string().optional(),
            "websiteUrl": t.string().optional(),
            "kind": t.string().optional(),
            "productCodes": t.array(t.string()).optional(),
            "userLocale": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["AssociationSessionIn"])
    types["AssociationSessionOut"] = t.struct(
        {
            "status": t.string().optional(),
            "accountId": t.string().optional(),
            "websiteLocale": t.string().optional(),
            "redirectUrl": t.string().optional(),
            "websiteUrl": t.string().optional(),
            "kind": t.string().optional(),
            "productCodes": t.array(t.string()).optional(),
            "userLocale": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssociationSessionOut"])
    types["AccountsIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["AccountIn"])).optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["AccountsIn"])
    types["AccountsOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["AccountOut"])).optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountsOut"])
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
            "averages": t.array(t.string()).optional(),
            "rows": t.array(t.array(t.string())).optional(),
            "totalMatchedRows": t.string().optional(),
            "headers": t.array(
                t.struct(
                    {
                        "currency": t.string().optional(),
                        "name": t.string().optional(),
                        "type": t.string().optional(),
                    }
                )
            ).optional(),
            "totals": t.array(t.string()).optional(),
            "kind": t.string().optional(),
            "warnings": t.array(t.string()).optional(),
        }
    ).named(renames["ReportIn"])
    types["ReportOut"] = t.struct(
        {
            "averages": t.array(t.string()).optional(),
            "rows": t.array(t.array(t.string())).optional(),
            "totalMatchedRows": t.string().optional(),
            "headers": t.array(
                t.struct(
                    {
                        "currency": t.string().optional(),
                        "name": t.string().optional(),
                        "type": t.string().optional(),
                    }
                )
            ).optional(),
            "totals": t.array(t.string()).optional(),
            "kind": t.string().optional(),
            "warnings": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportOut"])
    types["AdClientIn"] = t.struct(
        {
            "arcOptIn": t.boolean().optional(),
            "productCode": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "supportsReporting": t.boolean().optional(),
        }
    ).named(renames["AdClientIn"])
    types["AdClientOut"] = t.struct(
        {
            "arcOptIn": t.boolean().optional(),
            "productCode": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "supportsReporting": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdClientOut"])
    types["CustomChannelsIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "items": t.array(t.proxy(renames["CustomChannelIn"])).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["CustomChannelsIn"])
    types["CustomChannelsOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "items": t.array(t.proxy(renames["CustomChannelOut"])).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomChannelsOut"])
    types["UrlChannelIn"] = t.struct(
        {
            "urlPattern": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["UrlChannelIn"])
    types["UrlChannelOut"] = t.struct(
        {
            "urlPattern": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UrlChannelOut"])
    types["CustomChannelIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "code": t.string().optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["CustomChannelIn"])
    types["CustomChannelOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "code": t.string().optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomChannelOut"])
    types["AdClientsIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "items": t.array(t.proxy(renames["AdClientIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["AdClientsIn"])
    types["AdClientsOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "items": t.array(t.proxy(renames["AdClientOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdClientsOut"])

    functions = {}
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
                "maxResults": t.integer().optional(),
                "dimension": t.string().optional(),
                "metric": t.string().optional(),
                "startDate": t.string().optional(),
                "accountId": t.string().optional(),
                "sort": t.string().optional(),
                "filter": t.string().optional(),
                "locale": t.string().optional(),
                "startIndex": t.integer().optional(),
                "endDate": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdunitsDelete"] = adsensehost.post(
        "accounts/{accountId}/adclients/{adClientId}/adunits",
        t.struct(
            {
                "adClientId": t.string().optional(),
                "accountId": t.string().optional(),
                "id": t.string().optional(),
                "code": t.string().optional(),
                "customStyle": t.proxy(renames["AdStyleIn"]).optional(),
                "name": t.string().optional(),
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
                "kind": t.string().optional(),
                "mobileContentAdsSettings": t.struct(
                    {
                        "size": t.string().optional(),
                        "scriptingLanguage": t.string().optional(),
                        "type": t.string().optional(),
                        "markupLanguage": t.string().optional(),
                    }
                ).optional(),
                "status": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdUnitOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdunitsPatch"] = adsensehost.post(
        "accounts/{accountId}/adclients/{adClientId}/adunits",
        t.struct(
            {
                "adClientId": t.string().optional(),
                "accountId": t.string().optional(),
                "id": t.string().optional(),
                "code": t.string().optional(),
                "customStyle": t.proxy(renames["AdStyleIn"]).optional(),
                "name": t.string().optional(),
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
                "kind": t.string().optional(),
                "mobileContentAdsSettings": t.struct(
                    {
                        "size": t.string().optional(),
                        "scriptingLanguage": t.string().optional(),
                        "type": t.string().optional(),
                        "markupLanguage": t.string().optional(),
                    }
                ).optional(),
                "status": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdUnitOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdunitsUpdate"] = adsensehost.post(
        "accounts/{accountId}/adclients/{adClientId}/adunits",
        t.struct(
            {
                "adClientId": t.string().optional(),
                "accountId": t.string().optional(),
                "id": t.string().optional(),
                "code": t.string().optional(),
                "customStyle": t.proxy(renames["AdStyleIn"]).optional(),
                "name": t.string().optional(),
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
                "kind": t.string().optional(),
                "mobileContentAdsSettings": t.struct(
                    {
                        "size": t.string().optional(),
                        "scriptingLanguage": t.string().optional(),
                        "type": t.string().optional(),
                        "markupLanguage": t.string().optional(),
                    }
                ).optional(),
                "status": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdUnitOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdunitsList"] = adsensehost.post(
        "accounts/{accountId}/adclients/{adClientId}/adunits",
        t.struct(
            {
                "adClientId": t.string().optional(),
                "accountId": t.string().optional(),
                "id": t.string().optional(),
                "code": t.string().optional(),
                "customStyle": t.proxy(renames["AdStyleIn"]).optional(),
                "name": t.string().optional(),
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
                "kind": t.string().optional(),
                "mobileContentAdsSettings": t.struct(
                    {
                        "size": t.string().optional(),
                        "scriptingLanguage": t.string().optional(),
                        "type": t.string().optional(),
                        "markupLanguage": t.string().optional(),
                    }
                ).optional(),
                "status": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdUnitOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdunitsGetAdCode"] = adsensehost.post(
        "accounts/{accountId}/adclients/{adClientId}/adunits",
        t.struct(
            {
                "adClientId": t.string().optional(),
                "accountId": t.string().optional(),
                "id": t.string().optional(),
                "code": t.string().optional(),
                "customStyle": t.proxy(renames["AdStyleIn"]).optional(),
                "name": t.string().optional(),
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
                "kind": t.string().optional(),
                "mobileContentAdsSettings": t.struct(
                    {
                        "size": t.string().optional(),
                        "scriptingLanguage": t.string().optional(),
                        "type": t.string().optional(),
                        "markupLanguage": t.string().optional(),
                    }
                ).optional(),
                "status": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdUnitOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdunitsGet"] = adsensehost.post(
        "accounts/{accountId}/adclients/{adClientId}/adunits",
        t.struct(
            {
                "adClientId": t.string().optional(),
                "accountId": t.string().optional(),
                "id": t.string().optional(),
                "code": t.string().optional(),
                "customStyle": t.proxy(renames["AdStyleIn"]).optional(),
                "name": t.string().optional(),
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
                "kind": t.string().optional(),
                "mobileContentAdsSettings": t.struct(
                    {
                        "size": t.string().optional(),
                        "scriptingLanguage": t.string().optional(),
                        "type": t.string().optional(),
                        "markupLanguage": t.string().optional(),
                    }
                ).optional(),
                "status": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdUnitOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdunitsInsert"] = adsensehost.post(
        "accounts/{accountId}/adclients/{adClientId}/adunits",
        t.struct(
            {
                "adClientId": t.string().optional(),
                "accountId": t.string().optional(),
                "id": t.string().optional(),
                "code": t.string().optional(),
                "customStyle": t.proxy(renames["AdStyleIn"]).optional(),
                "name": t.string().optional(),
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
                "kind": t.string().optional(),
                "mobileContentAdsSettings": t.struct(
                    {
                        "size": t.string().optional(),
                        "scriptingLanguage": t.string().optional(),
                        "type": t.string().optional(),
                        "markupLanguage": t.string().optional(),
                    }
                ).optional(),
                "status": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdUnitOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdclientsGet"] = adsensehost.get(
        "accounts/{accountId}/adclients",
        t.struct(
            {
                "accountId": t.string().optional(),
                "pageToken": t.string().optional(),
                "maxResults": t.integer().optional(),
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
                "accountId": t.string().optional(),
                "pageToken": t.string().optional(),
                "maxResults": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdClientsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["associationsessionsVerify"] = adsensehost.get(
        "associationsessions/start",
        t.struct(
            {
                "userLocale": t.string().optional(),
                "websiteUrl": t.string().optional(),
                "productCode": t.string().optional(),
                "websiteLocale": t.string().optional(),
                "callbackUrl": t.string().optional(),
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
                "userLocale": t.string().optional(),
                "websiteUrl": t.string().optional(),
                "productCode": t.string().optional(),
                "websiteLocale": t.string().optional(),
                "callbackUrl": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssociationSessionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["urlchannelsList"] = adsensehost.post(
        "adclients/{adClientId}/urlchannels",
        t.struct(
            {
                "adClientId": t.string().optional(),
                "urlPattern": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UrlChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["urlchannelsDelete"] = adsensehost.post(
        "adclients/{adClientId}/urlchannels",
        t.struct(
            {
                "adClientId": t.string().optional(),
                "urlPattern": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UrlChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["urlchannelsInsert"] = adsensehost.post(
        "adclients/{adClientId}/urlchannels",
        t.struct(
            {
                "adClientId": t.string().optional(),
                "urlPattern": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UrlChannelOut"]),
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
    functions["reportsGenerate"] = adsensehost.get(
        "reports",
        t.struct(
            {
                "filter": t.string().optional(),
                "startIndex": t.integer().optional(),
                "endDate": t.string().optional(),
                "maxResults": t.integer().optional(),
                "metric": t.string().optional(),
                "startDate": t.string().optional(),
                "locale": t.string().optional(),
                "dimension": t.string().optional(),
                "sort": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customchannelsList"] = adsensehost.get(
        "adclients/{adClientId}/customchannels/{customChannelId}",
        t.struct(
            {
                "adClientId": t.string().optional(),
                "customChannelId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customchannelsInsert"] = adsensehost.get(
        "adclients/{adClientId}/customchannels/{customChannelId}",
        t.struct(
            {
                "adClientId": t.string().optional(),
                "customChannelId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customchannelsUpdate"] = adsensehost.get(
        "adclients/{adClientId}/customchannels/{customChannelId}",
        t.struct(
            {
                "adClientId": t.string().optional(),
                "customChannelId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customchannelsDelete"] = adsensehost.get(
        "adclients/{adClientId}/customchannels/{customChannelId}",
        t.struct(
            {
                "adClientId": t.string().optional(),
                "customChannelId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customchannelsPatch"] = adsensehost.get(
        "adclients/{adClientId}/customchannels/{customChannelId}",
        t.struct(
            {
                "adClientId": t.string().optional(),
                "customChannelId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customchannelsGet"] = adsensehost.get(
        "adclients/{adClientId}/customchannels/{customChannelId}",
        t.struct(
            {
                "adClientId": t.string().optional(),
                "customChannelId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="adsensehost",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
