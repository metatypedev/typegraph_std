from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_customsearch() -> Import:
    customsearch = HTTPRuntime("https://customsearch.googleapis.com/")

    renames = {
        "ErrorResponse": "_customsearch_1_ErrorResponse",
        "ResultIn": "_customsearch_2_ResultIn",
        "ResultOut": "_customsearch_3_ResultOut",
        "SearchIn": "_customsearch_4_SearchIn",
        "SearchOut": "_customsearch_5_SearchOut",
        "PromotionIn": "_customsearch_6_PromotionIn",
        "PromotionOut": "_customsearch_7_PromotionOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ResultIn"] = t.struct(
        {
            "formattedUrl": t.string().optional(),
            "snippet": t.string().optional(),
            "title": t.string().optional(),
            "image": t.struct(
                {
                    "height": t.integer().optional(),
                    "byteSize": t.integer().optional(),
                    "contextLink": t.string().optional(),
                    "width": t.integer().optional(),
                    "thumbnailWidth": t.integer().optional(),
                    "thumbnailHeight": t.integer().optional(),
                    "thumbnailLink": t.string().optional(),
                }
            ).optional(),
            "fileFormat": t.string().optional(),
            "kind": t.string().optional(),
            "htmlTitle": t.string().optional(),
            "htmlSnippet": t.string().optional(),
            "pagemap": t.struct({"_": t.string().optional()}).optional(),
            "cacheId": t.string().optional(),
            "labels": t.array(
                t.struct(
                    {
                        "name": t.string().optional(),
                        "label_with_op": t.string().optional(),
                        "displayName": t.string().optional(),
                    }
                )
            ).optional(),
            "htmlFormattedUrl": t.string().optional(),
            "link": t.string().optional(),
            "mime": t.string().optional(),
            "displayLink": t.string().optional(),
        }
    ).named(renames["ResultIn"])
    types["ResultOut"] = t.struct(
        {
            "formattedUrl": t.string().optional(),
            "snippet": t.string().optional(),
            "title": t.string().optional(),
            "image": t.struct(
                {
                    "height": t.integer().optional(),
                    "byteSize": t.integer().optional(),
                    "contextLink": t.string().optional(),
                    "width": t.integer().optional(),
                    "thumbnailWidth": t.integer().optional(),
                    "thumbnailHeight": t.integer().optional(),
                    "thumbnailLink": t.string().optional(),
                }
            ).optional(),
            "fileFormat": t.string().optional(),
            "kind": t.string().optional(),
            "htmlTitle": t.string().optional(),
            "htmlSnippet": t.string().optional(),
            "pagemap": t.struct({"_": t.string().optional()}).optional(),
            "cacheId": t.string().optional(),
            "labels": t.array(
                t.struct(
                    {
                        "name": t.string().optional(),
                        "label_with_op": t.string().optional(),
                        "displayName": t.string().optional(),
                    }
                )
            ).optional(),
            "htmlFormattedUrl": t.string().optional(),
            "link": t.string().optional(),
            "mime": t.string().optional(),
            "displayLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResultOut"])
    types["SearchIn"] = t.struct(
        {
            "context": t.struct({"_": t.string().optional()}).optional(),
            "queries": t.struct(
                {
                    "request": t.array(
                        t.struct(
                            {
                                "outputEncoding": t.string().optional(),
                                "startPage": t.integer().optional(),
                                "fileType": t.string().optional(),
                                "hq": t.string().optional(),
                                "startIndex": t.integer().optional(),
                                "siteSearch": t.string().optional(),
                                "safe": t.string().optional(),
                                "totalResults": t.string().optional(),
                                "inputEncoding": t.string().optional(),
                                "gl": t.string().optional(),
                                "sort": t.string().optional(),
                                "exactTerms": t.string().optional(),
                                "cx": t.string().optional(),
                                "highRange": t.string().optional(),
                                "searchTerms": t.string().optional(),
                                "count": t.integer().optional(),
                                "lowRange": t.string().optional(),
                                "siteSearchFilter": t.string().optional(),
                                "filter": t.string().optional(),
                                "imgType": t.string().optional(),
                                "googleHost": t.string().optional(),
                                "dateRestrict": t.string().optional(),
                                "language": t.string().optional(),
                                "title": t.string().optional(),
                                "linkSite": t.string().optional(),
                                "rights": t.string().optional(),
                                "imgDominantColor": t.string().optional(),
                                "imgSize": t.string().optional(),
                                "imgColorType": t.string().optional(),
                                "relatedSite": t.string().optional(),
                                "cr": t.string().optional(),
                                "hl": t.string().optional(),
                                "searchType": t.string().optional(),
                                "orTerms": t.string().optional(),
                                "disableCnTwTranslation": t.string().optional(),
                                "excludeTerms": t.string().optional(),
                            }
                        )
                    ).optional(),
                    "nextPage": t.array(
                        t.struct(
                            {
                                "siteSearchFilter": t.string().optional(),
                                "totalResults": t.string().optional(),
                                "searchType": t.string().optional(),
                                "rights": t.string().optional(),
                                "cr": t.string().optional(),
                                "safe": t.string().optional(),
                                "imgColorType": t.string().optional(),
                                "fileType": t.string().optional(),
                                "excludeTerms": t.string().optional(),
                                "language": t.string().optional(),
                                "inputEncoding": t.string().optional(),
                                "disableCnTwTranslation": t.string().optional(),
                                "count": t.integer().optional(),
                                "startPage": t.integer().optional(),
                                "imgType": t.string().optional(),
                                "relatedSite": t.string().optional(),
                                "siteSearch": t.string().optional(),
                                "orTerms": t.string().optional(),
                                "googleHost": t.string().optional(),
                                "hl": t.string().optional(),
                                "lowRange": t.string().optional(),
                                "filter": t.string().optional(),
                                "highRange": t.string().optional(),
                                "linkSite": t.string().optional(),
                                "imgSize": t.string().optional(),
                                "sort": t.string().optional(),
                                "startIndex": t.integer().optional(),
                                "dateRestrict": t.string().optional(),
                                "gl": t.string().optional(),
                                "exactTerms": t.string().optional(),
                                "imgDominantColor": t.string().optional(),
                                "title": t.string().optional(),
                                "searchTerms": t.string().optional(),
                                "outputEncoding": t.string().optional(),
                                "cx": t.string().optional(),
                                "hq": t.string().optional(),
                            }
                        )
                    ).optional(),
                    "previousPage": t.array(
                        t.struct(
                            {
                                "searchTerms": t.string().optional(),
                                "fileType": t.string().optional(),
                                "filter": t.string().optional(),
                                "orTerms": t.string().optional(),
                                "linkSite": t.string().optional(),
                                "googleHost": t.string().optional(),
                                "siteSearchFilter": t.string().optional(),
                                "sort": t.string().optional(),
                                "gl": t.string().optional(),
                                "totalResults": t.string().optional(),
                                "imgType": t.string().optional(),
                                "imgColorType": t.string().optional(),
                                "hl": t.string().optional(),
                                "excludeTerms": t.string().optional(),
                                "rights": t.string().optional(),
                                "exactTerms": t.string().optional(),
                                "lowRange": t.string().optional(),
                                "language": t.string().optional(),
                                "imgDominantColor": t.string().optional(),
                                "count": t.integer().optional(),
                                "cx": t.string().optional(),
                                "safe": t.string().optional(),
                                "relatedSite": t.string().optional(),
                                "siteSearch": t.string().optional(),
                                "title": t.string().optional(),
                                "searchType": t.string().optional(),
                                "cr": t.string().optional(),
                                "inputEncoding": t.string().optional(),
                                "startIndex": t.integer().optional(),
                                "hq": t.string().optional(),
                                "imgSize": t.string().optional(),
                                "startPage": t.integer().optional(),
                                "dateRestrict": t.string().optional(),
                                "outputEncoding": t.string().optional(),
                                "disableCnTwTranslation": t.string().optional(),
                                "highRange": t.string().optional(),
                            }
                        )
                    ).optional(),
                }
            ).optional(),
            "items": t.array(t.proxy(renames["ResultIn"])).optional(),
            "url": t.struct(
                {"type": t.string().optional(), "template": t.string().optional()}
            ).optional(),
            "spelling": t.struct(
                {
                    "htmlCorrectedQuery": t.string().optional(),
                    "correctedQuery": t.string().optional(),
                }
            ).optional(),
            "kind": t.string().optional(),
            "promotions": t.array(t.proxy(renames["PromotionIn"])).optional(),
            "searchInformation": t.struct(
                {
                    "formattedTotalResults": t.string().optional(),
                    "searchTime": t.number().optional(),
                    "totalResults": t.string().optional(),
                    "formattedSearchTime": t.string().optional(),
                }
            ).optional(),
        }
    ).named(renames["SearchIn"])
    types["SearchOut"] = t.struct(
        {
            "context": t.struct({"_": t.string().optional()}).optional(),
            "queries": t.struct(
                {
                    "request": t.array(
                        t.struct(
                            {
                                "outputEncoding": t.string().optional(),
                                "startPage": t.integer().optional(),
                                "fileType": t.string().optional(),
                                "hq": t.string().optional(),
                                "startIndex": t.integer().optional(),
                                "siteSearch": t.string().optional(),
                                "safe": t.string().optional(),
                                "totalResults": t.string().optional(),
                                "inputEncoding": t.string().optional(),
                                "gl": t.string().optional(),
                                "sort": t.string().optional(),
                                "exactTerms": t.string().optional(),
                                "cx": t.string().optional(),
                                "highRange": t.string().optional(),
                                "searchTerms": t.string().optional(),
                                "count": t.integer().optional(),
                                "lowRange": t.string().optional(),
                                "siteSearchFilter": t.string().optional(),
                                "filter": t.string().optional(),
                                "imgType": t.string().optional(),
                                "googleHost": t.string().optional(),
                                "dateRestrict": t.string().optional(),
                                "language": t.string().optional(),
                                "title": t.string().optional(),
                                "linkSite": t.string().optional(),
                                "rights": t.string().optional(),
                                "imgDominantColor": t.string().optional(),
                                "imgSize": t.string().optional(),
                                "imgColorType": t.string().optional(),
                                "relatedSite": t.string().optional(),
                                "cr": t.string().optional(),
                                "hl": t.string().optional(),
                                "searchType": t.string().optional(),
                                "orTerms": t.string().optional(),
                                "disableCnTwTranslation": t.string().optional(),
                                "excludeTerms": t.string().optional(),
                            }
                        )
                    ).optional(),
                    "nextPage": t.array(
                        t.struct(
                            {
                                "siteSearchFilter": t.string().optional(),
                                "totalResults": t.string().optional(),
                                "searchType": t.string().optional(),
                                "rights": t.string().optional(),
                                "cr": t.string().optional(),
                                "safe": t.string().optional(),
                                "imgColorType": t.string().optional(),
                                "fileType": t.string().optional(),
                                "excludeTerms": t.string().optional(),
                                "language": t.string().optional(),
                                "inputEncoding": t.string().optional(),
                                "disableCnTwTranslation": t.string().optional(),
                                "count": t.integer().optional(),
                                "startPage": t.integer().optional(),
                                "imgType": t.string().optional(),
                                "relatedSite": t.string().optional(),
                                "siteSearch": t.string().optional(),
                                "orTerms": t.string().optional(),
                                "googleHost": t.string().optional(),
                                "hl": t.string().optional(),
                                "lowRange": t.string().optional(),
                                "filter": t.string().optional(),
                                "highRange": t.string().optional(),
                                "linkSite": t.string().optional(),
                                "imgSize": t.string().optional(),
                                "sort": t.string().optional(),
                                "startIndex": t.integer().optional(),
                                "dateRestrict": t.string().optional(),
                                "gl": t.string().optional(),
                                "exactTerms": t.string().optional(),
                                "imgDominantColor": t.string().optional(),
                                "title": t.string().optional(),
                                "searchTerms": t.string().optional(),
                                "outputEncoding": t.string().optional(),
                                "cx": t.string().optional(),
                                "hq": t.string().optional(),
                            }
                        )
                    ).optional(),
                    "previousPage": t.array(
                        t.struct(
                            {
                                "searchTerms": t.string().optional(),
                                "fileType": t.string().optional(),
                                "filter": t.string().optional(),
                                "orTerms": t.string().optional(),
                                "linkSite": t.string().optional(),
                                "googleHost": t.string().optional(),
                                "siteSearchFilter": t.string().optional(),
                                "sort": t.string().optional(),
                                "gl": t.string().optional(),
                                "totalResults": t.string().optional(),
                                "imgType": t.string().optional(),
                                "imgColorType": t.string().optional(),
                                "hl": t.string().optional(),
                                "excludeTerms": t.string().optional(),
                                "rights": t.string().optional(),
                                "exactTerms": t.string().optional(),
                                "lowRange": t.string().optional(),
                                "language": t.string().optional(),
                                "imgDominantColor": t.string().optional(),
                                "count": t.integer().optional(),
                                "cx": t.string().optional(),
                                "safe": t.string().optional(),
                                "relatedSite": t.string().optional(),
                                "siteSearch": t.string().optional(),
                                "title": t.string().optional(),
                                "searchType": t.string().optional(),
                                "cr": t.string().optional(),
                                "inputEncoding": t.string().optional(),
                                "startIndex": t.integer().optional(),
                                "hq": t.string().optional(),
                                "imgSize": t.string().optional(),
                                "startPage": t.integer().optional(),
                                "dateRestrict": t.string().optional(),
                                "outputEncoding": t.string().optional(),
                                "disableCnTwTranslation": t.string().optional(),
                                "highRange": t.string().optional(),
                            }
                        )
                    ).optional(),
                }
            ).optional(),
            "items": t.array(t.proxy(renames["ResultOut"])).optional(),
            "url": t.struct(
                {"type": t.string().optional(), "template": t.string().optional()}
            ).optional(),
            "spelling": t.struct(
                {
                    "htmlCorrectedQuery": t.string().optional(),
                    "correctedQuery": t.string().optional(),
                }
            ).optional(),
            "kind": t.string().optional(),
            "promotions": t.array(t.proxy(renames["PromotionOut"])).optional(),
            "searchInformation": t.struct(
                {
                    "formattedTotalResults": t.string().optional(),
                    "searchTime": t.number().optional(),
                    "totalResults": t.string().optional(),
                    "formattedSearchTime": t.string().optional(),
                }
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchOut"])
    types["PromotionIn"] = t.struct(
        {
            "bodyLines": t.array(
                t.struct(
                    {
                        "link": t.string().optional(),
                        "htmlTitle": t.string().optional(),
                        "title": t.string().optional(),
                        "url": t.string().optional(),
                    }
                )
            ).optional(),
            "link": t.string().optional(),
            "image": t.struct(
                {
                    "height": t.integer().optional(),
                    "width": t.integer().optional(),
                    "source": t.string().optional(),
                }
            ).optional(),
            "displayLink": t.string().optional(),
            "title": t.string().optional(),
            "htmlTitle": t.string().optional(),
        }
    ).named(renames["PromotionIn"])
    types["PromotionOut"] = t.struct(
        {
            "bodyLines": t.array(
                t.struct(
                    {
                        "link": t.string().optional(),
                        "htmlTitle": t.string().optional(),
                        "title": t.string().optional(),
                        "url": t.string().optional(),
                    }
                )
            ).optional(),
            "link": t.string().optional(),
            "image": t.struct(
                {
                    "height": t.integer().optional(),
                    "width": t.integer().optional(),
                    "source": t.string().optional(),
                }
            ).optional(),
            "displayLink": t.string().optional(),
            "title": t.string().optional(),
            "htmlTitle": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PromotionOut"])

    functions = {}
    functions["cseList"] = customsearch.get(
        "customsearch/v1",
        t.struct(
            {
                "num": t.integer().optional(),
                "excludeTerms": t.string().optional(),
                "start": t.integer().optional(),
                "q": t.string().optional(),
                "googlehost": t.string().optional(),
                "fileType": t.string().optional(),
                "orTerms": t.string().optional(),
                "gl": t.string().optional(),
                "hq": t.string().optional(),
                "c2coff": t.string().optional(),
                "dateRestrict": t.string().optional(),
                "relatedSite": t.string().optional(),
                "imgDominantColor": t.string().optional(),
                "siteSearchFilter": t.string().optional(),
                "lr": t.string().optional(),
                "filter": t.string().optional(),
                "imgSize": t.string().optional(),
                "safe": t.string().optional(),
                "highRange": t.string().optional(),
                "rights": t.string().optional(),
                "imgType": t.string().optional(),
                "siteSearch": t.string().optional(),
                "lowRange": t.string().optional(),
                "linkSite": t.string().optional(),
                "hl": t.string().optional(),
                "imgColorType": t.string().optional(),
                "searchType": t.string().optional(),
                "cx": t.string().optional(),
                "exactTerms": t.string().optional(),
                "sort": t.string().optional(),
                "cr": t.string().optional(),
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
                "siteSearch": t.string().optional(),
                "hl": t.string().optional(),
                "c2coff": t.string().optional(),
                "filter": t.string().optional(),
                "excludeTerms": t.string().optional(),
                "imgColorType": t.string().optional(),
                "fileType": t.string().optional(),
                "hq": t.string().optional(),
                "q": t.string().optional(),
                "gl": t.string().optional(),
                "lowRange": t.string().optional(),
                "dateRestrict": t.string().optional(),
                "relatedSite": t.string().optional(),
                "start": t.integer().optional(),
                "lr": t.string().optional(),
                "safe": t.string().optional(),
                "cx": t.string().optional(),
                "exactTerms": t.string().optional(),
                "cr": t.string().optional(),
                "num": t.integer().optional(),
                "rights": t.string().optional(),
                "searchType": t.string().optional(),
                "sort": t.string().optional(),
                "highRange": t.string().optional(),
                "imgSize": t.string().optional(),
                "googlehost": t.string().optional(),
                "imgType": t.string().optional(),
                "linkSite": t.string().optional(),
                "orTerms": t.string().optional(),
                "siteSearchFilter": t.string().optional(),
                "imgDominantColor": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="customsearch", renames=renames, types=types, functions=functions
    )
