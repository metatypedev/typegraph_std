from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_customsearch():
    customsearch = HTTPRuntime("https://customsearch.googleapis.com/")

    renames = {
        "ErrorResponse": "_customsearch_1_ErrorResponse",
        "PromotionIn": "_customsearch_2_PromotionIn",
        "PromotionOut": "_customsearch_3_PromotionOut",
        "ResultIn": "_customsearch_4_ResultIn",
        "ResultOut": "_customsearch_5_ResultOut",
        "SearchIn": "_customsearch_6_SearchIn",
        "SearchOut": "_customsearch_7_SearchOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["PromotionIn"] = t.struct(
        {
            "image": t.struct(
                {
                    "source": t.string().optional(),
                    "height": t.integer().optional(),
                    "width": t.integer().optional(),
                }
            ).optional(),
            "link": t.string().optional(),
            "title": t.string().optional(),
            "bodyLines": t.array(
                t.struct(
                    {
                        "url": t.string().optional(),
                        "title": t.string().optional(),
                        "link": t.string().optional(),
                        "htmlTitle": t.string().optional(),
                    }
                )
            ).optional(),
            "htmlTitle": t.string().optional(),
            "displayLink": t.string().optional(),
        }
    ).named(renames["PromotionIn"])
    types["PromotionOut"] = t.struct(
        {
            "image": t.struct(
                {
                    "source": t.string().optional(),
                    "height": t.integer().optional(),
                    "width": t.integer().optional(),
                }
            ).optional(),
            "link": t.string().optional(),
            "title": t.string().optional(),
            "bodyLines": t.array(
                t.struct(
                    {
                        "url": t.string().optional(),
                        "title": t.string().optional(),
                        "link": t.string().optional(),
                        "htmlTitle": t.string().optional(),
                    }
                )
            ).optional(),
            "htmlTitle": t.string().optional(),
            "displayLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PromotionOut"])
    types["ResultIn"] = t.struct(
        {
            "htmlFormattedUrl": t.string().optional(),
            "pagemap": t.struct({"_": t.string().optional()}).optional(),
            "mime": t.string().optional(),
            "kind": t.string().optional(),
            "displayLink": t.string().optional(),
            "cacheId": t.string().optional(),
            "snippet": t.string().optional(),
            "labels": t.array(
                t.struct(
                    {
                        "displayName": t.string().optional(),
                        "label_with_op": t.string().optional(),
                        "name": t.string().optional(),
                    }
                )
            ).optional(),
            "image": t.struct(
                {
                    "thumbnailLink": t.string().optional(),
                    "height": t.integer().optional(),
                    "width": t.integer().optional(),
                    "thumbnailHeight": t.integer().optional(),
                    "contextLink": t.string().optional(),
                    "thumbnailWidth": t.integer().optional(),
                    "byteSize": t.integer().optional(),
                }
            ).optional(),
            "formattedUrl": t.string().optional(),
            "htmlTitle": t.string().optional(),
            "htmlSnippet": t.string().optional(),
            "fileFormat": t.string().optional(),
            "title": t.string().optional(),
            "link": t.string().optional(),
        }
    ).named(renames["ResultIn"])
    types["ResultOut"] = t.struct(
        {
            "htmlFormattedUrl": t.string().optional(),
            "pagemap": t.struct({"_": t.string().optional()}).optional(),
            "mime": t.string().optional(),
            "kind": t.string().optional(),
            "displayLink": t.string().optional(),
            "cacheId": t.string().optional(),
            "snippet": t.string().optional(),
            "labels": t.array(
                t.struct(
                    {
                        "displayName": t.string().optional(),
                        "label_with_op": t.string().optional(),
                        "name": t.string().optional(),
                    }
                )
            ).optional(),
            "image": t.struct(
                {
                    "thumbnailLink": t.string().optional(),
                    "height": t.integer().optional(),
                    "width": t.integer().optional(),
                    "thumbnailHeight": t.integer().optional(),
                    "contextLink": t.string().optional(),
                    "thumbnailWidth": t.integer().optional(),
                    "byteSize": t.integer().optional(),
                }
            ).optional(),
            "formattedUrl": t.string().optional(),
            "htmlTitle": t.string().optional(),
            "htmlSnippet": t.string().optional(),
            "fileFormat": t.string().optional(),
            "title": t.string().optional(),
            "link": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResultOut"])
    types["SearchIn"] = t.struct(
        {
            "context": t.struct({"_": t.string().optional()}).optional(),
            "promotions": t.array(t.proxy(renames["PromotionIn"])).optional(),
            "url": t.struct(
                {"template": t.string().optional(), "type": t.string().optional()}
            ).optional(),
            "spelling": t.struct(
                {
                    "htmlCorrectedQuery": t.string().optional(),
                    "correctedQuery": t.string().optional(),
                }
            ).optional(),
            "items": t.array(t.proxy(renames["ResultIn"])).optional(),
            "queries": t.struct(
                {
                    "request": t.array(
                        t.struct(
                            {
                                "inputEncoding": t.string().optional(),
                                "totalResults": t.string().optional(),
                                "orTerms": t.string().optional(),
                                "filter": t.string().optional(),
                                "highRange": t.string().optional(),
                                "startIndex": t.integer().optional(),
                                "cx": t.string().optional(),
                                "startPage": t.integer().optional(),
                                "imgType": t.string().optional(),
                                "safe": t.string().optional(),
                                "siteSearch": t.string().optional(),
                                "googleHost": t.string().optional(),
                                "imgDominantColor": t.string().optional(),
                                "count": t.integer().optional(),
                                "title": t.string().optional(),
                                "outputEncoding": t.string().optional(),
                                "hl": t.string().optional(),
                                "hq": t.string().optional(),
                                "imgSize": t.string().optional(),
                                "searchTerms": t.string().optional(),
                                "excludeTerms": t.string().optional(),
                                "searchType": t.string().optional(),
                                "linkSite": t.string().optional(),
                                "lowRange": t.string().optional(),
                                "language": t.string().optional(),
                                "relatedSite": t.string().optional(),
                                "rights": t.string().optional(),
                                "dateRestrict": t.string().optional(),
                                "fileType": t.string().optional(),
                                "sort": t.string().optional(),
                                "disableCnTwTranslation": t.string().optional(),
                                "cr": t.string().optional(),
                                "exactTerms": t.string().optional(),
                                "imgColorType": t.string().optional(),
                                "gl": t.string().optional(),
                                "siteSearchFilter": t.string().optional(),
                            }
                        )
                    ).optional(),
                    "previousPage": t.array(
                        t.struct(
                            {
                                "language": t.string().optional(),
                                "cx": t.string().optional(),
                                "imgDominantColor": t.string().optional(),
                                "dateRestrict": t.string().optional(),
                                "imgColorType": t.string().optional(),
                                "inputEncoding": t.string().optional(),
                                "siteSearch": t.string().optional(),
                                "startIndex": t.integer().optional(),
                                "safe": t.string().optional(),
                                "rights": t.string().optional(),
                                "linkSite": t.string().optional(),
                                "googleHost": t.string().optional(),
                                "imgType": t.string().optional(),
                                "count": t.integer().optional(),
                                "totalResults": t.string().optional(),
                                "disableCnTwTranslation": t.string().optional(),
                                "searchType": t.string().optional(),
                                "filter": t.string().optional(),
                                "gl": t.string().optional(),
                                "exactTerms": t.string().optional(),
                                "hq": t.string().optional(),
                                "lowRange": t.string().optional(),
                                "highRange": t.string().optional(),
                                "imgSize": t.string().optional(),
                                "hl": t.string().optional(),
                                "excludeTerms": t.string().optional(),
                                "relatedSite": t.string().optional(),
                                "fileType": t.string().optional(),
                                "siteSearchFilter": t.string().optional(),
                                "sort": t.string().optional(),
                                "outputEncoding": t.string().optional(),
                                "orTerms": t.string().optional(),
                                "startPage": t.integer().optional(),
                                "searchTerms": t.string().optional(),
                                "cr": t.string().optional(),
                                "title": t.string().optional(),
                            }
                        )
                    ).optional(),
                    "nextPage": t.array(
                        t.struct(
                            {
                                "cr": t.string().optional(),
                                "imgSize": t.string().optional(),
                                "totalResults": t.string().optional(),
                                "count": t.integer().optional(),
                                "rights": t.string().optional(),
                                "lowRange": t.string().optional(),
                                "siteSearchFilter": t.string().optional(),
                                "highRange": t.string().optional(),
                                "cx": t.string().optional(),
                                "gl": t.string().optional(),
                                "dateRestrict": t.string().optional(),
                                "imgColorType": t.string().optional(),
                                "excludeTerms": t.string().optional(),
                                "exactTerms": t.string().optional(),
                                "orTerms": t.string().optional(),
                                "relatedSite": t.string().optional(),
                                "hq": t.string().optional(),
                                "fileType": t.string().optional(),
                                "title": t.string().optional(),
                                "siteSearch": t.string().optional(),
                                "linkSite": t.string().optional(),
                                "imgDominantColor": t.string().optional(),
                                "inputEncoding": t.string().optional(),
                                "hl": t.string().optional(),
                                "sort": t.string().optional(),
                                "outputEncoding": t.string().optional(),
                                "imgType": t.string().optional(),
                                "filter": t.string().optional(),
                                "disableCnTwTranslation": t.string().optional(),
                                "googleHost": t.string().optional(),
                                "searchTerms": t.string().optional(),
                                "language": t.string().optional(),
                                "startPage": t.integer().optional(),
                                "safe": t.string().optional(),
                                "searchType": t.string().optional(),
                                "startIndex": t.integer().optional(),
                            }
                        )
                    ).optional(),
                }
            ).optional(),
            "searchInformation": t.struct(
                {
                    "searchTime": t.number().optional(),
                    "formattedTotalResults": t.string().optional(),
                    "formattedSearchTime": t.string().optional(),
                    "totalResults": t.string().optional(),
                }
            ).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["SearchIn"])
    types["SearchOut"] = t.struct(
        {
            "context": t.struct({"_": t.string().optional()}).optional(),
            "promotions": t.array(t.proxy(renames["PromotionOut"])).optional(),
            "url": t.struct(
                {"template": t.string().optional(), "type": t.string().optional()}
            ).optional(),
            "spelling": t.struct(
                {
                    "htmlCorrectedQuery": t.string().optional(),
                    "correctedQuery": t.string().optional(),
                }
            ).optional(),
            "items": t.array(t.proxy(renames["ResultOut"])).optional(),
            "queries": t.struct(
                {
                    "request": t.array(
                        t.struct(
                            {
                                "inputEncoding": t.string().optional(),
                                "totalResults": t.string().optional(),
                                "orTerms": t.string().optional(),
                                "filter": t.string().optional(),
                                "highRange": t.string().optional(),
                                "startIndex": t.integer().optional(),
                                "cx": t.string().optional(),
                                "startPage": t.integer().optional(),
                                "imgType": t.string().optional(),
                                "safe": t.string().optional(),
                                "siteSearch": t.string().optional(),
                                "googleHost": t.string().optional(),
                                "imgDominantColor": t.string().optional(),
                                "count": t.integer().optional(),
                                "title": t.string().optional(),
                                "outputEncoding": t.string().optional(),
                                "hl": t.string().optional(),
                                "hq": t.string().optional(),
                                "imgSize": t.string().optional(),
                                "searchTerms": t.string().optional(),
                                "excludeTerms": t.string().optional(),
                                "searchType": t.string().optional(),
                                "linkSite": t.string().optional(),
                                "lowRange": t.string().optional(),
                                "language": t.string().optional(),
                                "relatedSite": t.string().optional(),
                                "rights": t.string().optional(),
                                "dateRestrict": t.string().optional(),
                                "fileType": t.string().optional(),
                                "sort": t.string().optional(),
                                "disableCnTwTranslation": t.string().optional(),
                                "cr": t.string().optional(),
                                "exactTerms": t.string().optional(),
                                "imgColorType": t.string().optional(),
                                "gl": t.string().optional(),
                                "siteSearchFilter": t.string().optional(),
                            }
                        )
                    ).optional(),
                    "previousPage": t.array(
                        t.struct(
                            {
                                "language": t.string().optional(),
                                "cx": t.string().optional(),
                                "imgDominantColor": t.string().optional(),
                                "dateRestrict": t.string().optional(),
                                "imgColorType": t.string().optional(),
                                "inputEncoding": t.string().optional(),
                                "siteSearch": t.string().optional(),
                                "startIndex": t.integer().optional(),
                                "safe": t.string().optional(),
                                "rights": t.string().optional(),
                                "linkSite": t.string().optional(),
                                "googleHost": t.string().optional(),
                                "imgType": t.string().optional(),
                                "count": t.integer().optional(),
                                "totalResults": t.string().optional(),
                                "disableCnTwTranslation": t.string().optional(),
                                "searchType": t.string().optional(),
                                "filter": t.string().optional(),
                                "gl": t.string().optional(),
                                "exactTerms": t.string().optional(),
                                "hq": t.string().optional(),
                                "lowRange": t.string().optional(),
                                "highRange": t.string().optional(),
                                "imgSize": t.string().optional(),
                                "hl": t.string().optional(),
                                "excludeTerms": t.string().optional(),
                                "relatedSite": t.string().optional(),
                                "fileType": t.string().optional(),
                                "siteSearchFilter": t.string().optional(),
                                "sort": t.string().optional(),
                                "outputEncoding": t.string().optional(),
                                "orTerms": t.string().optional(),
                                "startPage": t.integer().optional(),
                                "searchTerms": t.string().optional(),
                                "cr": t.string().optional(),
                                "title": t.string().optional(),
                            }
                        )
                    ).optional(),
                    "nextPage": t.array(
                        t.struct(
                            {
                                "cr": t.string().optional(),
                                "imgSize": t.string().optional(),
                                "totalResults": t.string().optional(),
                                "count": t.integer().optional(),
                                "rights": t.string().optional(),
                                "lowRange": t.string().optional(),
                                "siteSearchFilter": t.string().optional(),
                                "highRange": t.string().optional(),
                                "cx": t.string().optional(),
                                "gl": t.string().optional(),
                                "dateRestrict": t.string().optional(),
                                "imgColorType": t.string().optional(),
                                "excludeTerms": t.string().optional(),
                                "exactTerms": t.string().optional(),
                                "orTerms": t.string().optional(),
                                "relatedSite": t.string().optional(),
                                "hq": t.string().optional(),
                                "fileType": t.string().optional(),
                                "title": t.string().optional(),
                                "siteSearch": t.string().optional(),
                                "linkSite": t.string().optional(),
                                "imgDominantColor": t.string().optional(),
                                "inputEncoding": t.string().optional(),
                                "hl": t.string().optional(),
                                "sort": t.string().optional(),
                                "outputEncoding": t.string().optional(),
                                "imgType": t.string().optional(),
                                "filter": t.string().optional(),
                                "disableCnTwTranslation": t.string().optional(),
                                "googleHost": t.string().optional(),
                                "searchTerms": t.string().optional(),
                                "language": t.string().optional(),
                                "startPage": t.integer().optional(),
                                "safe": t.string().optional(),
                                "searchType": t.string().optional(),
                                "startIndex": t.integer().optional(),
                            }
                        )
                    ).optional(),
                }
            ).optional(),
            "searchInformation": t.struct(
                {
                    "searchTime": t.number().optional(),
                    "formattedTotalResults": t.string().optional(),
                    "formattedSearchTime": t.string().optional(),
                    "totalResults": t.string().optional(),
                }
            ).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchOut"])

    functions = {}
    functions["cseList"] = customsearch.get(
        "customsearch/v1",
        t.struct(
            {
                "imgDominantColor": t.string().optional(),
                "cx": t.string().optional(),
                "start": t.integer().optional(),
                "cr": t.string().optional(),
                "imgSize": t.string().optional(),
                "siteSearch": t.string().optional(),
                "lr": t.string().optional(),
                "safe": t.string().optional(),
                "linkSite": t.string().optional(),
                "q": t.string().optional(),
                "rights": t.string().optional(),
                "lowRange": t.string().optional(),
                "excludeTerms": t.string().optional(),
                "siteSearchFilter": t.string().optional(),
                "fileType": t.string().optional(),
                "relatedSite": t.string().optional(),
                "sort": t.string().optional(),
                "hl": t.string().optional(),
                "imgType": t.string().optional(),
                "imgColorType": t.string().optional(),
                "filter": t.string().optional(),
                "c2coff": t.string().optional(),
                "orTerms": t.string().optional(),
                "gl": t.string().optional(),
                "num": t.integer().optional(),
                "highRange": t.string().optional(),
                "googlehost": t.string().optional(),
                "searchType": t.string().optional(),
                "dateRestrict": t.string().optional(),
                "hq": t.string().optional(),
                "exactTerms": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["cseSiterestrictList"] = customsearch.get(
        "customsearch/v1/siterestrict",
        t.struct(
            {
                "googlehost": t.string().optional(),
                "cx": t.string().optional(),
                "filter": t.string().optional(),
                "imgColorType": t.string().optional(),
                "lowRange": t.string().optional(),
                "fileType": t.string().optional(),
                "orTerms": t.string().optional(),
                "imgDominantColor": t.string().optional(),
                "hl": t.string().optional(),
                "gl": t.string().optional(),
                "siteSearch": t.string().optional(),
                "imgSize": t.string().optional(),
                "q": t.string().optional(),
                "lr": t.string().optional(),
                "hq": t.string().optional(),
                "c2coff": t.string().optional(),
                "rights": t.string().optional(),
                "excludeTerms": t.string().optional(),
                "start": t.integer().optional(),
                "dateRestrict": t.string().optional(),
                "num": t.integer().optional(),
                "siteSearchFilter": t.string().optional(),
                "sort": t.string().optional(),
                "searchType": t.string().optional(),
                "safe": t.string().optional(),
                "relatedSite": t.string().optional(),
                "exactTerms": t.string().optional(),
                "linkSite": t.string().optional(),
                "cr": t.string().optional(),
                "imgType": t.string().optional(),
                "highRange": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="customsearch",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
