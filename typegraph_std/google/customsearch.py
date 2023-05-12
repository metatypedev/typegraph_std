from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_customsearch() -> Import:
    customsearch = HTTPRuntime("https://customsearch.googleapis.com/")

    renames = {
        "ErrorResponse": "_customsearch_1_ErrorResponse",
        "SearchIn": "_customsearch_2_SearchIn",
        "SearchOut": "_customsearch_3_SearchOut",
        "PromotionIn": "_customsearch_4_PromotionIn",
        "PromotionOut": "_customsearch_5_PromotionOut",
        "ResultIn": "_customsearch_6_ResultIn",
        "ResultOut": "_customsearch_7_ResultOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["SearchIn"] = t.struct(
        {
            "searchInformation": t.struct(
                {
                    "totalResults": t.string().optional(),
                    "formattedTotalResults": t.string().optional(),
                    "searchTime": t.number().optional(),
                    "formattedSearchTime": t.string().optional(),
                }
            ).optional(),
            "promotions": t.array(t.proxy(renames["PromotionIn"])).optional(),
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["ResultIn"])).optional(),
            "spelling": t.struct(
                {
                    "correctedQuery": t.string().optional(),
                    "htmlCorrectedQuery": t.string().optional(),
                }
            ).optional(),
            "url": t.struct(
                {"type": t.string().optional(), "template": t.string().optional()}
            ).optional(),
            "context": t.struct({"_": t.string().optional()}).optional(),
            "queries": t.struct(
                {
                    "previousPage": t.array(
                        t.struct(
                            {
                                "cr": t.string().optional(),
                                "relatedSite": t.string().optional(),
                                "lowRange": t.string().optional(),
                                "gl": t.string().optional(),
                                "excludeTerms": t.string().optional(),
                                "siteSearch": t.string().optional(),
                                "count": t.integer().optional(),
                                "inputEncoding": t.string().optional(),
                                "searchType": t.string().optional(),
                                "language": t.string().optional(),
                                "fileType": t.string().optional(),
                                "rights": t.string().optional(),
                                "imgType": t.string().optional(),
                                "title": t.string().optional(),
                                "cx": t.string().optional(),
                                "startIndex": t.integer().optional(),
                                "imgSize": t.string().optional(),
                                "searchTerms": t.string().optional(),
                                "outputEncoding": t.string().optional(),
                                "googleHost": t.string().optional(),
                                "dateRestrict": t.string().optional(),
                                "highRange": t.string().optional(),
                                "safe": t.string().optional(),
                                "imgColorType": t.string().optional(),
                                "disableCnTwTranslation": t.string().optional(),
                                "sort": t.string().optional(),
                                "filter": t.string().optional(),
                                "hl": t.string().optional(),
                                "hq": t.string().optional(),
                                "siteSearchFilter": t.string().optional(),
                                "orTerms": t.string().optional(),
                                "startPage": t.integer().optional(),
                                "exactTerms": t.string().optional(),
                                "totalResults": t.string().optional(),
                                "linkSite": t.string().optional(),
                                "imgDominantColor": t.string().optional(),
                            }
                        )
                    ).optional(),
                    "nextPage": t.array(
                        t.struct(
                            {
                                "searchTerms": t.string().optional(),
                                "totalResults": t.string().optional(),
                                "imgSize": t.string().optional(),
                                "cr": t.string().optional(),
                                "siteSearch": t.string().optional(),
                                "gl": t.string().optional(),
                                "exactTerms": t.string().optional(),
                                "highRange": t.string().optional(),
                                "siteSearchFilter": t.string().optional(),
                                "count": t.integer().optional(),
                                "googleHost": t.string().optional(),
                                "dateRestrict": t.string().optional(),
                                "imgDominantColor": t.string().optional(),
                                "relatedSite": t.string().optional(),
                                "startPage": t.integer().optional(),
                                "lowRange": t.string().optional(),
                                "cx": t.string().optional(),
                                "title": t.string().optional(),
                                "inputEncoding": t.string().optional(),
                                "startIndex": t.integer().optional(),
                                "orTerms": t.string().optional(),
                                "searchType": t.string().optional(),
                                "imgType": t.string().optional(),
                                "outputEncoding": t.string().optional(),
                                "imgColorType": t.string().optional(),
                                "linkSite": t.string().optional(),
                                "sort": t.string().optional(),
                                "disableCnTwTranslation": t.string().optional(),
                                "fileType": t.string().optional(),
                                "excludeTerms": t.string().optional(),
                                "rights": t.string().optional(),
                                "safe": t.string().optional(),
                                "language": t.string().optional(),
                                "hq": t.string().optional(),
                                "hl": t.string().optional(),
                                "filter": t.string().optional(),
                            }
                        )
                    ).optional(),
                    "request": t.array(
                        t.struct(
                            {
                                "inputEncoding": t.string().optional(),
                                "filter": t.string().optional(),
                                "fileType": t.string().optional(),
                                "exactTerms": t.string().optional(),
                                "highRange": t.string().optional(),
                                "sort": t.string().optional(),
                                "disableCnTwTranslation": t.string().optional(),
                                "rights": t.string().optional(),
                                "siteSearch": t.string().optional(),
                                "imgType": t.string().optional(),
                                "outputEncoding": t.string().optional(),
                                "imgSize": t.string().optional(),
                                "language": t.string().optional(),
                                "safe": t.string().optional(),
                                "count": t.integer().optional(),
                                "imgColorType": t.string().optional(),
                                "cx": t.string().optional(),
                                "hq": t.string().optional(),
                                "linkSite": t.string().optional(),
                                "searchTerms": t.string().optional(),
                                "siteSearchFilter": t.string().optional(),
                                "hl": t.string().optional(),
                                "dateRestrict": t.string().optional(),
                                "orTerms": t.string().optional(),
                                "cr": t.string().optional(),
                                "excludeTerms": t.string().optional(),
                                "title": t.string().optional(),
                                "gl": t.string().optional(),
                                "imgDominantColor": t.string().optional(),
                                "googleHost": t.string().optional(),
                                "totalResults": t.string().optional(),
                                "startIndex": t.integer().optional(),
                                "relatedSite": t.string().optional(),
                                "startPage": t.integer().optional(),
                                "lowRange": t.string().optional(),
                                "searchType": t.string().optional(),
                            }
                        )
                    ).optional(),
                }
            ).optional(),
        }
    ).named(renames["SearchIn"])
    types["SearchOut"] = t.struct(
        {
            "searchInformation": t.struct(
                {
                    "totalResults": t.string().optional(),
                    "formattedTotalResults": t.string().optional(),
                    "searchTime": t.number().optional(),
                    "formattedSearchTime": t.string().optional(),
                }
            ).optional(),
            "promotions": t.array(t.proxy(renames["PromotionOut"])).optional(),
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["ResultOut"])).optional(),
            "spelling": t.struct(
                {
                    "correctedQuery": t.string().optional(),
                    "htmlCorrectedQuery": t.string().optional(),
                }
            ).optional(),
            "url": t.struct(
                {"type": t.string().optional(), "template": t.string().optional()}
            ).optional(),
            "context": t.struct({"_": t.string().optional()}).optional(),
            "queries": t.struct(
                {
                    "previousPage": t.array(
                        t.struct(
                            {
                                "cr": t.string().optional(),
                                "relatedSite": t.string().optional(),
                                "lowRange": t.string().optional(),
                                "gl": t.string().optional(),
                                "excludeTerms": t.string().optional(),
                                "siteSearch": t.string().optional(),
                                "count": t.integer().optional(),
                                "inputEncoding": t.string().optional(),
                                "searchType": t.string().optional(),
                                "language": t.string().optional(),
                                "fileType": t.string().optional(),
                                "rights": t.string().optional(),
                                "imgType": t.string().optional(),
                                "title": t.string().optional(),
                                "cx": t.string().optional(),
                                "startIndex": t.integer().optional(),
                                "imgSize": t.string().optional(),
                                "searchTerms": t.string().optional(),
                                "outputEncoding": t.string().optional(),
                                "googleHost": t.string().optional(),
                                "dateRestrict": t.string().optional(),
                                "highRange": t.string().optional(),
                                "safe": t.string().optional(),
                                "imgColorType": t.string().optional(),
                                "disableCnTwTranslation": t.string().optional(),
                                "sort": t.string().optional(),
                                "filter": t.string().optional(),
                                "hl": t.string().optional(),
                                "hq": t.string().optional(),
                                "siteSearchFilter": t.string().optional(),
                                "orTerms": t.string().optional(),
                                "startPage": t.integer().optional(),
                                "exactTerms": t.string().optional(),
                                "totalResults": t.string().optional(),
                                "linkSite": t.string().optional(),
                                "imgDominantColor": t.string().optional(),
                            }
                        )
                    ).optional(),
                    "nextPage": t.array(
                        t.struct(
                            {
                                "searchTerms": t.string().optional(),
                                "totalResults": t.string().optional(),
                                "imgSize": t.string().optional(),
                                "cr": t.string().optional(),
                                "siteSearch": t.string().optional(),
                                "gl": t.string().optional(),
                                "exactTerms": t.string().optional(),
                                "highRange": t.string().optional(),
                                "siteSearchFilter": t.string().optional(),
                                "count": t.integer().optional(),
                                "googleHost": t.string().optional(),
                                "dateRestrict": t.string().optional(),
                                "imgDominantColor": t.string().optional(),
                                "relatedSite": t.string().optional(),
                                "startPage": t.integer().optional(),
                                "lowRange": t.string().optional(),
                                "cx": t.string().optional(),
                                "title": t.string().optional(),
                                "inputEncoding": t.string().optional(),
                                "startIndex": t.integer().optional(),
                                "orTerms": t.string().optional(),
                                "searchType": t.string().optional(),
                                "imgType": t.string().optional(),
                                "outputEncoding": t.string().optional(),
                                "imgColorType": t.string().optional(),
                                "linkSite": t.string().optional(),
                                "sort": t.string().optional(),
                                "disableCnTwTranslation": t.string().optional(),
                                "fileType": t.string().optional(),
                                "excludeTerms": t.string().optional(),
                                "rights": t.string().optional(),
                                "safe": t.string().optional(),
                                "language": t.string().optional(),
                                "hq": t.string().optional(),
                                "hl": t.string().optional(),
                                "filter": t.string().optional(),
                            }
                        )
                    ).optional(),
                    "request": t.array(
                        t.struct(
                            {
                                "inputEncoding": t.string().optional(),
                                "filter": t.string().optional(),
                                "fileType": t.string().optional(),
                                "exactTerms": t.string().optional(),
                                "highRange": t.string().optional(),
                                "sort": t.string().optional(),
                                "disableCnTwTranslation": t.string().optional(),
                                "rights": t.string().optional(),
                                "siteSearch": t.string().optional(),
                                "imgType": t.string().optional(),
                                "outputEncoding": t.string().optional(),
                                "imgSize": t.string().optional(),
                                "language": t.string().optional(),
                                "safe": t.string().optional(),
                                "count": t.integer().optional(),
                                "imgColorType": t.string().optional(),
                                "cx": t.string().optional(),
                                "hq": t.string().optional(),
                                "linkSite": t.string().optional(),
                                "searchTerms": t.string().optional(),
                                "siteSearchFilter": t.string().optional(),
                                "hl": t.string().optional(),
                                "dateRestrict": t.string().optional(),
                                "orTerms": t.string().optional(),
                                "cr": t.string().optional(),
                                "excludeTerms": t.string().optional(),
                                "title": t.string().optional(),
                                "gl": t.string().optional(),
                                "imgDominantColor": t.string().optional(),
                                "googleHost": t.string().optional(),
                                "totalResults": t.string().optional(),
                                "startIndex": t.integer().optional(),
                                "relatedSite": t.string().optional(),
                                "startPage": t.integer().optional(),
                                "lowRange": t.string().optional(),
                                "searchType": t.string().optional(),
                            }
                        )
                    ).optional(),
                }
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchOut"])
    types["PromotionIn"] = t.struct(
        {
            "displayLink": t.string().optional(),
            "title": t.string().optional(),
            "image": t.struct(
                {
                    "height": t.integer().optional(),
                    "width": t.integer().optional(),
                    "source": t.string().optional(),
                }
            ).optional(),
            "link": t.string().optional(),
            "bodyLines": t.array(
                t.struct(
                    {
                        "url": t.string().optional(),
                        "htmlTitle": t.string().optional(),
                        "link": t.string().optional(),
                        "title": t.string().optional(),
                    }
                )
            ).optional(),
            "htmlTitle": t.string().optional(),
        }
    ).named(renames["PromotionIn"])
    types["PromotionOut"] = t.struct(
        {
            "displayLink": t.string().optional(),
            "title": t.string().optional(),
            "image": t.struct(
                {
                    "height": t.integer().optional(),
                    "width": t.integer().optional(),
                    "source": t.string().optional(),
                }
            ).optional(),
            "link": t.string().optional(),
            "bodyLines": t.array(
                t.struct(
                    {
                        "url": t.string().optional(),
                        "htmlTitle": t.string().optional(),
                        "link": t.string().optional(),
                        "title": t.string().optional(),
                    }
                )
            ).optional(),
            "htmlTitle": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PromotionOut"])
    types["ResultIn"] = t.struct(
        {
            "pagemap": t.struct({"_": t.string().optional()}).optional(),
            "link": t.string().optional(),
            "snippet": t.string().optional(),
            "cacheId": t.string().optional(),
            "htmlFormattedUrl": t.string().optional(),
            "htmlTitle": t.string().optional(),
            "labels": t.array(
                t.struct(
                    {
                        "label_with_op": t.string().optional(),
                        "displayName": t.string().optional(),
                        "name": t.string().optional(),
                    }
                )
            ).optional(),
            "htmlSnippet": t.string().optional(),
            "image": t.struct(
                {
                    "thumbnailWidth": t.integer().optional(),
                    "thumbnailLink": t.string().optional(),
                    "height": t.integer().optional(),
                    "contextLink": t.string().optional(),
                    "thumbnailHeight": t.integer().optional(),
                    "byteSize": t.integer().optional(),
                    "width": t.integer().optional(),
                }
            ).optional(),
            "fileFormat": t.string().optional(),
            "displayLink": t.string().optional(),
            "title": t.string().optional(),
            "formattedUrl": t.string().optional(),
            "kind": t.string().optional(),
            "mime": t.string().optional(),
        }
    ).named(renames["ResultIn"])
    types["ResultOut"] = t.struct(
        {
            "pagemap": t.struct({"_": t.string().optional()}).optional(),
            "link": t.string().optional(),
            "snippet": t.string().optional(),
            "cacheId": t.string().optional(),
            "htmlFormattedUrl": t.string().optional(),
            "htmlTitle": t.string().optional(),
            "labels": t.array(
                t.struct(
                    {
                        "label_with_op": t.string().optional(),
                        "displayName": t.string().optional(),
                        "name": t.string().optional(),
                    }
                )
            ).optional(),
            "htmlSnippet": t.string().optional(),
            "image": t.struct(
                {
                    "thumbnailWidth": t.integer().optional(),
                    "thumbnailLink": t.string().optional(),
                    "height": t.integer().optional(),
                    "contextLink": t.string().optional(),
                    "thumbnailHeight": t.integer().optional(),
                    "byteSize": t.integer().optional(),
                    "width": t.integer().optional(),
                }
            ).optional(),
            "fileFormat": t.string().optional(),
            "displayLink": t.string().optional(),
            "title": t.string().optional(),
            "formattedUrl": t.string().optional(),
            "kind": t.string().optional(),
            "mime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResultOut"])

    functions = {}
    functions["cseList"] = customsearch.get(
        "customsearch/v1",
        t.struct(
            {
                "imgColorType": t.string().optional(),
                "imgDominantColor": t.string().optional(),
                "imgSize": t.string().optional(),
                "siteSearchFilter": t.string().optional(),
                "cr": t.string().optional(),
                "gl": t.string().optional(),
                "start": t.integer().optional(),
                "safe": t.string().optional(),
                "lowRange": t.string().optional(),
                "relatedSite": t.string().optional(),
                "cx": t.string().optional(),
                "num": t.integer().optional(),
                "hq": t.string().optional(),
                "excludeTerms": t.string().optional(),
                "sort": t.string().optional(),
                "q": t.string().optional(),
                "linkSite": t.string().optional(),
                "c2coff": t.string().optional(),
                "imgType": t.string().optional(),
                "siteSearch": t.string().optional(),
                "highRange": t.string().optional(),
                "googlehost": t.string().optional(),
                "lr": t.string().optional(),
                "searchType": t.string().optional(),
                "orTerms": t.string().optional(),
                "hl": t.string().optional(),
                "dateRestrict": t.string().optional(),
                "exactTerms": t.string().optional(),
                "filter": t.string().optional(),
                "rights": t.string().optional(),
                "fileType": t.string().optional(),
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
                "filter": t.string().optional(),
                "c2coff": t.string().optional(),
                "excludeTerms": t.string().optional(),
                "imgSize": t.string().optional(),
                "googlehost": t.string().optional(),
                "imgType": t.string().optional(),
                "dateRestrict": t.string().optional(),
                "cr": t.string().optional(),
                "imgColorType": t.string().optional(),
                "safe": t.string().optional(),
                "lowRange": t.string().optional(),
                "linkSite": t.string().optional(),
                "searchType": t.string().optional(),
                "hl": t.string().optional(),
                "siteSearchFilter": t.string().optional(),
                "num": t.integer().optional(),
                "orTerms": t.string().optional(),
                "hq": t.string().optional(),
                "highRange": t.string().optional(),
                "relatedSite": t.string().optional(),
                "exactTerms": t.string().optional(),
                "start": t.integer().optional(),
                "cx": t.string().optional(),
                "siteSearch": t.string().optional(),
                "rights": t.string().optional(),
                "fileType": t.string().optional(),
                "sort": t.string().optional(),
                "gl": t.string().optional(),
                "q": t.string().optional(),
                "lr": t.string().optional(),
                "imgDominantColor": t.string().optional(),
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
