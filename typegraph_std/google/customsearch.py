from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_customsearch() -> Import:
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
                    "width": t.integer().optional(),
                    "source": t.string().optional(),
                    "height": t.integer().optional(),
                }
            ).optional(),
            "link": t.string().optional(),
            "title": t.string().optional(),
            "displayLink": t.string().optional(),
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
        }
    ).named(renames["PromotionIn"])
    types["PromotionOut"] = t.struct(
        {
            "image": t.struct(
                {
                    "width": t.integer().optional(),
                    "source": t.string().optional(),
                    "height": t.integer().optional(),
                }
            ).optional(),
            "link": t.string().optional(),
            "title": t.string().optional(),
            "displayLink": t.string().optional(),
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
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PromotionOut"])
    types["ResultIn"] = t.struct(
        {
            "labels": t.array(
                t.struct(
                    {
                        "name": t.string().optional(),
                        "label_with_op": t.string().optional(),
                        "displayName": t.string().optional(),
                    }
                )
            ).optional(),
            "cacheId": t.string().optional(),
            "htmlFormattedUrl": t.string().optional(),
            "image": t.struct(
                {
                    "contextLink": t.string().optional(),
                    "thumbnailLink": t.string().optional(),
                    "thumbnailWidth": t.integer().optional(),
                    "height": t.integer().optional(),
                    "byteSize": t.integer().optional(),
                    "width": t.integer().optional(),
                    "thumbnailHeight": t.integer().optional(),
                }
            ).optional(),
            "kind": t.string().optional(),
            "htmlSnippet": t.string().optional(),
            "mime": t.string().optional(),
            "link": t.string().optional(),
            "pagemap": t.struct({"_": t.string().optional()}).optional(),
            "snippet": t.string().optional(),
            "displayLink": t.string().optional(),
            "htmlTitle": t.string().optional(),
            "title": t.string().optional(),
            "formattedUrl": t.string().optional(),
            "fileFormat": t.string().optional(),
        }
    ).named(renames["ResultIn"])
    types["ResultOut"] = t.struct(
        {
            "labels": t.array(
                t.struct(
                    {
                        "name": t.string().optional(),
                        "label_with_op": t.string().optional(),
                        "displayName": t.string().optional(),
                    }
                )
            ).optional(),
            "cacheId": t.string().optional(),
            "htmlFormattedUrl": t.string().optional(),
            "image": t.struct(
                {
                    "contextLink": t.string().optional(),
                    "thumbnailLink": t.string().optional(),
                    "thumbnailWidth": t.integer().optional(),
                    "height": t.integer().optional(),
                    "byteSize": t.integer().optional(),
                    "width": t.integer().optional(),
                    "thumbnailHeight": t.integer().optional(),
                }
            ).optional(),
            "kind": t.string().optional(),
            "htmlSnippet": t.string().optional(),
            "mime": t.string().optional(),
            "link": t.string().optional(),
            "pagemap": t.struct({"_": t.string().optional()}).optional(),
            "snippet": t.string().optional(),
            "displayLink": t.string().optional(),
            "htmlTitle": t.string().optional(),
            "title": t.string().optional(),
            "formattedUrl": t.string().optional(),
            "fileFormat": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResultOut"])
    types["SearchIn"] = t.struct(
        {
            "queries": t.struct(
                {
                    "request": t.array(
                        t.struct(
                            {
                                "searchType": t.string().optional(),
                                "searchTerms": t.string().optional(),
                                "gl": t.string().optional(),
                                "imgSize": t.string().optional(),
                                "linkSite": t.string().optional(),
                                "safe": t.string().optional(),
                                "relatedSite": t.string().optional(),
                                "rights": t.string().optional(),
                                "hq": t.string().optional(),
                                "count": t.integer().optional(),
                                "sort": t.string().optional(),
                                "highRange": t.string().optional(),
                                "imgType": t.string().optional(),
                                "cx": t.string().optional(),
                                "language": t.string().optional(),
                                "totalResults": t.string().optional(),
                                "fileType": t.string().optional(),
                                "siteSearch": t.string().optional(),
                                "imgDominantColor": t.string().optional(),
                                "cr": t.string().optional(),
                                "startIndex": t.integer().optional(),
                                "googleHost": t.string().optional(),
                                "excludeTerms": t.string().optional(),
                                "inputEncoding": t.string().optional(),
                                "orTerms": t.string().optional(),
                                "lowRange": t.string().optional(),
                                "dateRestrict": t.string().optional(),
                                "title": t.string().optional(),
                                "outputEncoding": t.string().optional(),
                                "exactTerms": t.string().optional(),
                                "siteSearchFilter": t.string().optional(),
                                "startPage": t.integer().optional(),
                                "hl": t.string().optional(),
                                "imgColorType": t.string().optional(),
                                "disableCnTwTranslation": t.string().optional(),
                                "filter": t.string().optional(),
                            }
                        )
                    ).optional(),
                    "previousPage": t.array(
                        t.struct(
                            {
                                "fileType": t.string().optional(),
                                "imgDominantColor": t.string().optional(),
                                "hq": t.string().optional(),
                                "imgType": t.string().optional(),
                                "gl": t.string().optional(),
                                "startIndex": t.integer().optional(),
                                "filter": t.string().optional(),
                                "outputEncoding": t.string().optional(),
                                "inputEncoding": t.string().optional(),
                                "rights": t.string().optional(),
                                "searchType": t.string().optional(),
                                "totalResults": t.string().optional(),
                                "linkSite": t.string().optional(),
                                "cr": t.string().optional(),
                                "highRange": t.string().optional(),
                                "startPage": t.integer().optional(),
                                "imgColorType": t.string().optional(),
                                "title": t.string().optional(),
                                "count": t.integer().optional(),
                                "lowRange": t.string().optional(),
                                "cx": t.string().optional(),
                                "exactTerms": t.string().optional(),
                                "excludeTerms": t.string().optional(),
                                "siteSearchFilter": t.string().optional(),
                                "safe": t.string().optional(),
                                "dateRestrict": t.string().optional(),
                                "imgSize": t.string().optional(),
                                "hl": t.string().optional(),
                                "siteSearch": t.string().optional(),
                                "sort": t.string().optional(),
                                "orTerms": t.string().optional(),
                                "searchTerms": t.string().optional(),
                                "disableCnTwTranslation": t.string().optional(),
                                "googleHost": t.string().optional(),
                                "language": t.string().optional(),
                                "relatedSite": t.string().optional(),
                            }
                        )
                    ).optional(),
                    "nextPage": t.array(
                        t.struct(
                            {
                                "cx": t.string().optional(),
                                "fileType": t.string().optional(),
                                "gl": t.string().optional(),
                                "startPage": t.integer().optional(),
                                "highRange": t.string().optional(),
                                "imgDominantColor": t.string().optional(),
                                "sort": t.string().optional(),
                                "hq": t.string().optional(),
                                "rights": t.string().optional(),
                                "dateRestrict": t.string().optional(),
                                "relatedSite": t.string().optional(),
                                "imgColorType": t.string().optional(),
                                "title": t.string().optional(),
                                "excludeTerms": t.string().optional(),
                                "inputEncoding": t.string().optional(),
                                "filter": t.string().optional(),
                                "googleHost": t.string().optional(),
                                "imgSize": t.string().optional(),
                                "imgType": t.string().optional(),
                                "hl": t.string().optional(),
                                "searchType": t.string().optional(),
                                "siteSearch": t.string().optional(),
                                "siteSearchFilter": t.string().optional(),
                                "count": t.integer().optional(),
                                "cr": t.string().optional(),
                                "linkSite": t.string().optional(),
                                "safe": t.string().optional(),
                                "orTerms": t.string().optional(),
                                "exactTerms": t.string().optional(),
                                "language": t.string().optional(),
                                "searchTerms": t.string().optional(),
                                "outputEncoding": t.string().optional(),
                                "disableCnTwTranslation": t.string().optional(),
                                "startIndex": t.integer().optional(),
                                "lowRange": t.string().optional(),
                                "totalResults": t.string().optional(),
                            }
                        )
                    ).optional(),
                }
            ).optional(),
            "promotions": t.array(t.proxy(renames["PromotionIn"])).optional(),
            "url": t.struct(
                {"type": t.string().optional(), "template": t.string().optional()}
            ).optional(),
            "searchInformation": t.struct(
                {
                    "totalResults": t.string().optional(),
                    "formattedTotalResults": t.string().optional(),
                    "formattedSearchTime": t.string().optional(),
                    "searchTime": t.number().optional(),
                }
            ).optional(),
            "context": t.struct({"_": t.string().optional()}).optional(),
            "spelling": t.struct(
                {
                    "correctedQuery": t.string().optional(),
                    "htmlCorrectedQuery": t.string().optional(),
                }
            ).optional(),
            "items": t.array(t.proxy(renames["ResultIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["SearchIn"])
    types["SearchOut"] = t.struct(
        {
            "queries": t.struct(
                {
                    "request": t.array(
                        t.struct(
                            {
                                "searchType": t.string().optional(),
                                "searchTerms": t.string().optional(),
                                "gl": t.string().optional(),
                                "imgSize": t.string().optional(),
                                "linkSite": t.string().optional(),
                                "safe": t.string().optional(),
                                "relatedSite": t.string().optional(),
                                "rights": t.string().optional(),
                                "hq": t.string().optional(),
                                "count": t.integer().optional(),
                                "sort": t.string().optional(),
                                "highRange": t.string().optional(),
                                "imgType": t.string().optional(),
                                "cx": t.string().optional(),
                                "language": t.string().optional(),
                                "totalResults": t.string().optional(),
                                "fileType": t.string().optional(),
                                "siteSearch": t.string().optional(),
                                "imgDominantColor": t.string().optional(),
                                "cr": t.string().optional(),
                                "startIndex": t.integer().optional(),
                                "googleHost": t.string().optional(),
                                "excludeTerms": t.string().optional(),
                                "inputEncoding": t.string().optional(),
                                "orTerms": t.string().optional(),
                                "lowRange": t.string().optional(),
                                "dateRestrict": t.string().optional(),
                                "title": t.string().optional(),
                                "outputEncoding": t.string().optional(),
                                "exactTerms": t.string().optional(),
                                "siteSearchFilter": t.string().optional(),
                                "startPage": t.integer().optional(),
                                "hl": t.string().optional(),
                                "imgColorType": t.string().optional(),
                                "disableCnTwTranslation": t.string().optional(),
                                "filter": t.string().optional(),
                            }
                        )
                    ).optional(),
                    "previousPage": t.array(
                        t.struct(
                            {
                                "fileType": t.string().optional(),
                                "imgDominantColor": t.string().optional(),
                                "hq": t.string().optional(),
                                "imgType": t.string().optional(),
                                "gl": t.string().optional(),
                                "startIndex": t.integer().optional(),
                                "filter": t.string().optional(),
                                "outputEncoding": t.string().optional(),
                                "inputEncoding": t.string().optional(),
                                "rights": t.string().optional(),
                                "searchType": t.string().optional(),
                                "totalResults": t.string().optional(),
                                "linkSite": t.string().optional(),
                                "cr": t.string().optional(),
                                "highRange": t.string().optional(),
                                "startPage": t.integer().optional(),
                                "imgColorType": t.string().optional(),
                                "title": t.string().optional(),
                                "count": t.integer().optional(),
                                "lowRange": t.string().optional(),
                                "cx": t.string().optional(),
                                "exactTerms": t.string().optional(),
                                "excludeTerms": t.string().optional(),
                                "siteSearchFilter": t.string().optional(),
                                "safe": t.string().optional(),
                                "dateRestrict": t.string().optional(),
                                "imgSize": t.string().optional(),
                                "hl": t.string().optional(),
                                "siteSearch": t.string().optional(),
                                "sort": t.string().optional(),
                                "orTerms": t.string().optional(),
                                "searchTerms": t.string().optional(),
                                "disableCnTwTranslation": t.string().optional(),
                                "googleHost": t.string().optional(),
                                "language": t.string().optional(),
                                "relatedSite": t.string().optional(),
                            }
                        )
                    ).optional(),
                    "nextPage": t.array(
                        t.struct(
                            {
                                "cx": t.string().optional(),
                                "fileType": t.string().optional(),
                                "gl": t.string().optional(),
                                "startPage": t.integer().optional(),
                                "highRange": t.string().optional(),
                                "imgDominantColor": t.string().optional(),
                                "sort": t.string().optional(),
                                "hq": t.string().optional(),
                                "rights": t.string().optional(),
                                "dateRestrict": t.string().optional(),
                                "relatedSite": t.string().optional(),
                                "imgColorType": t.string().optional(),
                                "title": t.string().optional(),
                                "excludeTerms": t.string().optional(),
                                "inputEncoding": t.string().optional(),
                                "filter": t.string().optional(),
                                "googleHost": t.string().optional(),
                                "imgSize": t.string().optional(),
                                "imgType": t.string().optional(),
                                "hl": t.string().optional(),
                                "searchType": t.string().optional(),
                                "siteSearch": t.string().optional(),
                                "siteSearchFilter": t.string().optional(),
                                "count": t.integer().optional(),
                                "cr": t.string().optional(),
                                "linkSite": t.string().optional(),
                                "safe": t.string().optional(),
                                "orTerms": t.string().optional(),
                                "exactTerms": t.string().optional(),
                                "language": t.string().optional(),
                                "searchTerms": t.string().optional(),
                                "outputEncoding": t.string().optional(),
                                "disableCnTwTranslation": t.string().optional(),
                                "startIndex": t.integer().optional(),
                                "lowRange": t.string().optional(),
                                "totalResults": t.string().optional(),
                            }
                        )
                    ).optional(),
                }
            ).optional(),
            "promotions": t.array(t.proxy(renames["PromotionOut"])).optional(),
            "url": t.struct(
                {"type": t.string().optional(), "template": t.string().optional()}
            ).optional(),
            "searchInformation": t.struct(
                {
                    "totalResults": t.string().optional(),
                    "formattedTotalResults": t.string().optional(),
                    "formattedSearchTime": t.string().optional(),
                    "searchTime": t.number().optional(),
                }
            ).optional(),
            "context": t.struct({"_": t.string().optional()}).optional(),
            "spelling": t.struct(
                {
                    "correctedQuery": t.string().optional(),
                    "htmlCorrectedQuery": t.string().optional(),
                }
            ).optional(),
            "items": t.array(t.proxy(renames["ResultOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchOut"])

    functions = {}
    functions["cseList"] = customsearch.get(
        "customsearch/v1",
        t.struct(
            {
                "start": t.integer().optional(),
                "linkSite": t.string().optional(),
                "imgType": t.string().optional(),
                "q": t.string().optional(),
                "fileType": t.string().optional(),
                "imgColorType": t.string().optional(),
                "orTerms": t.string().optional(),
                "hl": t.string().optional(),
                "num": t.integer().optional(),
                "googlehost": t.string().optional(),
                "c2coff": t.string().optional(),
                "excludeTerms": t.string().optional(),
                "exactTerms": t.string().optional(),
                "siteSearchFilter": t.string().optional(),
                "relatedSite": t.string().optional(),
                "cx": t.string().optional(),
                "lr": t.string().optional(),
                "gl": t.string().optional(),
                "siteSearch": t.string().optional(),
                "highRange": t.string().optional(),
                "imgDominantColor": t.string().optional(),
                "safe": t.string().optional(),
                "rights": t.string().optional(),
                "searchType": t.string().optional(),
                "dateRestrict": t.string().optional(),
                "lowRange": t.string().optional(),
                "filter": t.string().optional(),
                "hq": t.string().optional(),
                "imgSize": t.string().optional(),
                "cr": t.string().optional(),
                "sort": t.string().optional(),
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
                "sort": t.string().optional(),
                "linkSite": t.string().optional(),
                "dateRestrict": t.string().optional(),
                "filter": t.string().optional(),
                "siteSearch": t.string().optional(),
                "cr": t.string().optional(),
                "orTerms": t.string().optional(),
                "hl": t.string().optional(),
                "fileType": t.string().optional(),
                "imgSize": t.string().optional(),
                "excludeTerms": t.string().optional(),
                "siteSearchFilter": t.string().optional(),
                "relatedSite": t.string().optional(),
                "lr": t.string().optional(),
                "gl": t.string().optional(),
                "num": t.integer().optional(),
                "cx": t.string().optional(),
                "googlehost": t.string().optional(),
                "exactTerms": t.string().optional(),
                "safe": t.string().optional(),
                "imgType": t.string().optional(),
                "imgDominantColor": t.string().optional(),
                "q": t.string().optional(),
                "lowRange": t.string().optional(),
                "start": t.integer().optional(),
                "rights": t.string().optional(),
                "highRange": t.string().optional(),
                "searchType": t.string().optional(),
                "hq": t.string().optional(),
                "c2coff": t.string().optional(),
                "imgColorType": t.string().optional(),
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
