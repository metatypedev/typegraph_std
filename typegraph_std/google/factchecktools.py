from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_factchecktools() -> Import:
    factchecktools = HTTPRuntime("https://factchecktools.googleapis.com/")

    renames = {
        "ErrorResponse": "_factchecktools_1_ErrorResponse",
        "GoogleFactcheckingFactchecktoolsV1alpha1ClaimIn": "_factchecktools_2_GoogleFactcheckingFactchecktoolsV1alpha1ClaimIn",
        "GoogleFactcheckingFactchecktoolsV1alpha1ClaimOut": "_factchecktools_3_GoogleFactcheckingFactchecktoolsV1alpha1ClaimOut",
        "GoogleFactcheckingFactchecktoolsV1alpha1ClaimAuthorIn": "_factchecktools_4_GoogleFactcheckingFactchecktoolsV1alpha1ClaimAuthorIn",
        "GoogleFactcheckingFactchecktoolsV1alpha1ClaimAuthorOut": "_factchecktools_5_GoogleFactcheckingFactchecktoolsV1alpha1ClaimAuthorOut",
        "GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupPageIn": "_factchecktools_6_GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupPageIn",
        "GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupPageOut": "_factchecktools_7_GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupPageOut",
        "GoogleFactcheckingFactchecktoolsV1alpha1PublisherIn": "_factchecktools_8_GoogleFactcheckingFactchecktoolsV1alpha1PublisherIn",
        "GoogleFactcheckingFactchecktoolsV1alpha1PublisherOut": "_factchecktools_9_GoogleFactcheckingFactchecktoolsV1alpha1PublisherOut",
        "GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupIn": "_factchecktools_10_GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupIn",
        "GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupOut": "_factchecktools_11_GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupOut",
        "GoogleFactcheckingFactchecktoolsV1alpha1FactCheckedClaimSearchResponseIn": "_factchecktools_12_GoogleFactcheckingFactchecktoolsV1alpha1FactCheckedClaimSearchResponseIn",
        "GoogleFactcheckingFactchecktoolsV1alpha1FactCheckedClaimSearchResponseOut": "_factchecktools_13_GoogleFactcheckingFactchecktoolsV1alpha1FactCheckedClaimSearchResponseOut",
        "GoogleProtobufEmptyIn": "_factchecktools_14_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_factchecktools_15_GoogleProtobufEmptyOut",
        "GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewAuthorIn": "_factchecktools_16_GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewAuthorIn",
        "GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewAuthorOut": "_factchecktools_17_GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewAuthorOut",
        "GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewIn": "_factchecktools_18_GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewIn",
        "GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewOut": "_factchecktools_19_GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewOut",
        "GoogleFactcheckingFactchecktoolsV1alpha1ClaimRatingIn": "_factchecktools_20_GoogleFactcheckingFactchecktoolsV1alpha1ClaimRatingIn",
        "GoogleFactcheckingFactchecktoolsV1alpha1ClaimRatingOut": "_factchecktools_21_GoogleFactcheckingFactchecktoolsV1alpha1ClaimRatingOut",
        "GoogleFactcheckingFactchecktoolsV1alpha1ListClaimReviewMarkupPagesResponseIn": "_factchecktools_22_GoogleFactcheckingFactchecktoolsV1alpha1ListClaimReviewMarkupPagesResponseIn",
        "GoogleFactcheckingFactchecktoolsV1alpha1ListClaimReviewMarkupPagesResponseOut": "_factchecktools_23_GoogleFactcheckingFactchecktoolsV1alpha1ListClaimReviewMarkupPagesResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleFactcheckingFactchecktoolsV1alpha1ClaimIn"] = t.struct(
        {
            "claimDate": t.string().optional(),
            "claimant": t.string().optional(),
            "claimReview": t.array(
                t.proxy(
                    renames["GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewIn"]
                )
            ).optional(),
            "text": t.string().optional(),
        }
    ).named(renames["GoogleFactcheckingFactchecktoolsV1alpha1ClaimIn"])
    types["GoogleFactcheckingFactchecktoolsV1alpha1ClaimOut"] = t.struct(
        {
            "claimDate": t.string().optional(),
            "claimant": t.string().optional(),
            "claimReview": t.array(
                t.proxy(
                    renames["GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewOut"]
                )
            ).optional(),
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFactcheckingFactchecktoolsV1alpha1ClaimOut"])
    types["GoogleFactcheckingFactchecktoolsV1alpha1ClaimAuthorIn"] = t.struct(
        {
            "imageUrl": t.string().optional(),
            "jobTitle": t.string().optional(),
            "name": t.string().optional(),
            "sameAs": t.string().optional(),
        }
    ).named(renames["GoogleFactcheckingFactchecktoolsV1alpha1ClaimAuthorIn"])
    types["GoogleFactcheckingFactchecktoolsV1alpha1ClaimAuthorOut"] = t.struct(
        {
            "imageUrl": t.string().optional(),
            "jobTitle": t.string().optional(),
            "name": t.string().optional(),
            "sameAs": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFactcheckingFactchecktoolsV1alpha1ClaimAuthorOut"])
    types["GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupPageIn"] = t.struct(
        {
            "name": t.string().optional(),
            "pageUrl": t.string().optional(),
            "publishDate": t.string().optional(),
            "versionId": t.string().optional(),
            "claimReviewAuthor": t.proxy(
                renames["GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewAuthorIn"]
            ).optional(),
            "claimReviewMarkups": t.array(
                t.proxy(
                    renames[
                        "GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupPageIn"])
    types[
        "GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupPageOut"
    ] = t.struct(
        {
            "name": t.string().optional(),
            "pageUrl": t.string().optional(),
            "publishDate": t.string().optional(),
            "versionId": t.string().optional(),
            "claimReviewAuthor": t.proxy(
                renames["GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewAuthorOut"]
            ).optional(),
            "claimReviewMarkups": t.array(
                t.proxy(
                    renames[
                        "GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupPageOut"]
    )
    types["GoogleFactcheckingFactchecktoolsV1alpha1PublisherIn"] = t.struct(
        {"site": t.string().optional(), "name": t.string().optional()}
    ).named(renames["GoogleFactcheckingFactchecktoolsV1alpha1PublisherIn"])
    types["GoogleFactcheckingFactchecktoolsV1alpha1PublisherOut"] = t.struct(
        {
            "site": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFactcheckingFactchecktoolsV1alpha1PublisherOut"])
    types["GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupIn"] = t.struct(
        {
            "claimLocation": t.string().optional(),
            "claimAuthor": t.proxy(
                renames["GoogleFactcheckingFactchecktoolsV1alpha1ClaimAuthorIn"]
            ).optional(),
            "url": t.string().optional(),
            "claimAppearances": t.array(t.string()).optional(),
            "rating": t.proxy(
                renames["GoogleFactcheckingFactchecktoolsV1alpha1ClaimRatingIn"]
            ).optional(),
            "claimFirstAppearance": t.string().optional(),
            "claimReviewed": t.string().optional(),
            "claimDate": t.string().optional(),
        }
    ).named(renames["GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupIn"])
    types["GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupOut"] = t.struct(
        {
            "claimLocation": t.string().optional(),
            "claimAuthor": t.proxy(
                renames["GoogleFactcheckingFactchecktoolsV1alpha1ClaimAuthorOut"]
            ).optional(),
            "url": t.string().optional(),
            "claimAppearances": t.array(t.string()).optional(),
            "rating": t.proxy(
                renames["GoogleFactcheckingFactchecktoolsV1alpha1ClaimRatingOut"]
            ).optional(),
            "claimFirstAppearance": t.string().optional(),
            "claimReviewed": t.string().optional(),
            "claimDate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupOut"])
    types[
        "GoogleFactcheckingFactchecktoolsV1alpha1FactCheckedClaimSearchResponseIn"
    ] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "claims": t.array(
                t.proxy(renames["GoogleFactcheckingFactchecktoolsV1alpha1ClaimIn"])
            ).optional(),
        }
    ).named(
        renames[
            "GoogleFactcheckingFactchecktoolsV1alpha1FactCheckedClaimSearchResponseIn"
        ]
    )
    types[
        "GoogleFactcheckingFactchecktoolsV1alpha1FactCheckedClaimSearchResponseOut"
    ] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "claims": t.array(
                t.proxy(renames["GoogleFactcheckingFactchecktoolsV1alpha1ClaimOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleFactcheckingFactchecktoolsV1alpha1FactCheckedClaimSearchResponseOut"
        ]
    )
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
    types["GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewAuthorIn"] = t.struct(
        {"imageUrl": t.string().optional(), "name": t.string().optional()}
    ).named(renames["GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewAuthorIn"])
    types["GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewAuthorOut"] = t.struct(
        {
            "imageUrl": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewAuthorOut"])
    types["GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewIn"] = t.struct(
        {
            "url": t.string().optional(),
            "publisher": t.proxy(
                renames["GoogleFactcheckingFactchecktoolsV1alpha1PublisherIn"]
            ).optional(),
            "textualRating": t.string().optional(),
            "title": t.string().optional(),
            "languageCode": t.string().optional(),
            "reviewDate": t.string().optional(),
        }
    ).named(renames["GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewIn"])
    types["GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewOut"] = t.struct(
        {
            "url": t.string().optional(),
            "publisher": t.proxy(
                renames["GoogleFactcheckingFactchecktoolsV1alpha1PublisherOut"]
            ).optional(),
            "textualRating": t.string().optional(),
            "title": t.string().optional(),
            "languageCode": t.string().optional(),
            "reviewDate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewOut"])
    types["GoogleFactcheckingFactchecktoolsV1alpha1ClaimRatingIn"] = t.struct(
        {
            "bestRating": t.integer().optional(),
            "ratingValue": t.integer().optional(),
            "worstRating": t.integer().optional(),
            "textualRating": t.string().optional(),
            "ratingExplanation": t.string().optional(),
            "imageUrl": t.string().optional(),
        }
    ).named(renames["GoogleFactcheckingFactchecktoolsV1alpha1ClaimRatingIn"])
    types["GoogleFactcheckingFactchecktoolsV1alpha1ClaimRatingOut"] = t.struct(
        {
            "bestRating": t.integer().optional(),
            "ratingValue": t.integer().optional(),
            "worstRating": t.integer().optional(),
            "textualRating": t.string().optional(),
            "ratingExplanation": t.string().optional(),
            "imageUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFactcheckingFactchecktoolsV1alpha1ClaimRatingOut"])
    types[
        "GoogleFactcheckingFactchecktoolsV1alpha1ListClaimReviewMarkupPagesResponseIn"
    ] = t.struct(
        {
            "claimReviewMarkupPages": t.array(
                t.proxy(
                    renames[
                        "GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupPageIn"
                    ]
                )
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(
        renames[
            "GoogleFactcheckingFactchecktoolsV1alpha1ListClaimReviewMarkupPagesResponseIn"
        ]
    )
    types[
        "GoogleFactcheckingFactchecktoolsV1alpha1ListClaimReviewMarkupPagesResponseOut"
    ] = t.struct(
        {
            "claimReviewMarkupPages": t.array(
                t.proxy(
                    renames[
                        "GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupPageOut"
                    ]
                )
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleFactcheckingFactchecktoolsV1alpha1ListClaimReviewMarkupPagesResponseOut"
        ]
    )

    functions = {}
    functions["pagesGet"] = factchecktools.post(
        "v1alpha1/pages",
        t.struct(
            {
                "name": t.string().optional(),
                "pageUrl": t.string().optional(),
                "publishDate": t.string().optional(),
                "versionId": t.string().optional(),
                "claimReviewAuthor": t.proxy(
                    renames[
                        "GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewAuthorIn"
                    ]
                ).optional(),
                "claimReviewMarkups": t.array(
                    t.proxy(
                        renames[
                            "GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupIn"
                        ]
                    )
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupPageOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["pagesUpdate"] = factchecktools.post(
        "v1alpha1/pages",
        t.struct(
            {
                "name": t.string().optional(),
                "pageUrl": t.string().optional(),
                "publishDate": t.string().optional(),
                "versionId": t.string().optional(),
                "claimReviewAuthor": t.proxy(
                    renames[
                        "GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewAuthorIn"
                    ]
                ).optional(),
                "claimReviewMarkups": t.array(
                    t.proxy(
                        renames[
                            "GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupIn"
                        ]
                    )
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupPageOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["pagesDelete"] = factchecktools.post(
        "v1alpha1/pages",
        t.struct(
            {
                "name": t.string().optional(),
                "pageUrl": t.string().optional(),
                "publishDate": t.string().optional(),
                "versionId": t.string().optional(),
                "claimReviewAuthor": t.proxy(
                    renames[
                        "GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewAuthorIn"
                    ]
                ).optional(),
                "claimReviewMarkups": t.array(
                    t.proxy(
                        renames[
                            "GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupIn"
                        ]
                    )
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupPageOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["pagesList"] = factchecktools.post(
        "v1alpha1/pages",
        t.struct(
            {
                "name": t.string().optional(),
                "pageUrl": t.string().optional(),
                "publishDate": t.string().optional(),
                "versionId": t.string().optional(),
                "claimReviewAuthor": t.proxy(
                    renames[
                        "GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewAuthorIn"
                    ]
                ).optional(),
                "claimReviewMarkups": t.array(
                    t.proxy(
                        renames[
                            "GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupIn"
                        ]
                    )
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupPageOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["pagesCreate"] = factchecktools.post(
        "v1alpha1/pages",
        t.struct(
            {
                "name": t.string().optional(),
                "pageUrl": t.string().optional(),
                "publishDate": t.string().optional(),
                "versionId": t.string().optional(),
                "claimReviewAuthor": t.proxy(
                    renames[
                        "GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewAuthorIn"
                    ]
                ).optional(),
                "claimReviewMarkups": t.array(
                    t.proxy(
                        renames[
                            "GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupIn"
                        ]
                    )
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupPageOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["claimsSearch"] = factchecktools.get(
        "v1alpha1/claims:search",
        t.struct(
            {
                "languageCode": t.string().optional(),
                "maxAgeDays": t.integer().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "reviewPublisherSiteFilter": t.string().optional(),
                "offset": t.integer().optional(),
                "query": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames[
                "GoogleFactcheckingFactchecktoolsV1alpha1FactCheckedClaimSearchResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="factchecktools", renames=renames, types=types, functions=functions
    )
