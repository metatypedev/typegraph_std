from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_factchecktools():
    factchecktools = HTTPRuntime("https://factchecktools.googleapis.com/")

    renames = {
        "ErrorResponse": "_factchecktools_1_ErrorResponse",
        "GoogleFactcheckingFactchecktoolsV1alpha1ListClaimReviewMarkupPagesResponseIn": "_factchecktools_2_GoogleFactcheckingFactchecktoolsV1alpha1ListClaimReviewMarkupPagesResponseIn",
        "GoogleFactcheckingFactchecktoolsV1alpha1ListClaimReviewMarkupPagesResponseOut": "_factchecktools_3_GoogleFactcheckingFactchecktoolsV1alpha1ListClaimReviewMarkupPagesResponseOut",
        "GoogleProtobufEmptyIn": "_factchecktools_4_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_factchecktools_5_GoogleProtobufEmptyOut",
        "GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewIn": "_factchecktools_6_GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewIn",
        "GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewOut": "_factchecktools_7_GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewOut",
        "GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupIn": "_factchecktools_8_GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupIn",
        "GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupOut": "_factchecktools_9_GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupOut",
        "GoogleFactcheckingFactchecktoolsV1alpha1ClaimIn": "_factchecktools_10_GoogleFactcheckingFactchecktoolsV1alpha1ClaimIn",
        "GoogleFactcheckingFactchecktoolsV1alpha1ClaimOut": "_factchecktools_11_GoogleFactcheckingFactchecktoolsV1alpha1ClaimOut",
        "GoogleFactcheckingFactchecktoolsV1alpha1PublisherIn": "_factchecktools_12_GoogleFactcheckingFactchecktoolsV1alpha1PublisherIn",
        "GoogleFactcheckingFactchecktoolsV1alpha1PublisherOut": "_factchecktools_13_GoogleFactcheckingFactchecktoolsV1alpha1PublisherOut",
        "GoogleFactcheckingFactchecktoolsV1alpha1FactCheckedClaimSearchResponseIn": "_factchecktools_14_GoogleFactcheckingFactchecktoolsV1alpha1FactCheckedClaimSearchResponseIn",
        "GoogleFactcheckingFactchecktoolsV1alpha1FactCheckedClaimSearchResponseOut": "_factchecktools_15_GoogleFactcheckingFactchecktoolsV1alpha1FactCheckedClaimSearchResponseOut",
        "GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewAuthorIn": "_factchecktools_16_GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewAuthorIn",
        "GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewAuthorOut": "_factchecktools_17_GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewAuthorOut",
        "GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupPageIn": "_factchecktools_18_GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupPageIn",
        "GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupPageOut": "_factchecktools_19_GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupPageOut",
        "GoogleFactcheckingFactchecktoolsV1alpha1ClaimRatingIn": "_factchecktools_20_GoogleFactcheckingFactchecktoolsV1alpha1ClaimRatingIn",
        "GoogleFactcheckingFactchecktoolsV1alpha1ClaimRatingOut": "_factchecktools_21_GoogleFactcheckingFactchecktoolsV1alpha1ClaimRatingOut",
        "GoogleFactcheckingFactchecktoolsV1alpha1ClaimAuthorIn": "_factchecktools_22_GoogleFactcheckingFactchecktoolsV1alpha1ClaimAuthorIn",
        "GoogleFactcheckingFactchecktoolsV1alpha1ClaimAuthorOut": "_factchecktools_23_GoogleFactcheckingFactchecktoolsV1alpha1ClaimAuthorOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types[
        "GoogleFactcheckingFactchecktoolsV1alpha1ListClaimReviewMarkupPagesResponseIn"
    ] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "claimReviewMarkupPages": t.array(
                t.proxy(
                    renames[
                        "GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupPageIn"
                    ]
                )
            ).optional(),
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
            "nextPageToken": t.string().optional(),
            "claimReviewMarkupPages": t.array(
                t.proxy(
                    renames[
                        "GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupPageOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleFactcheckingFactchecktoolsV1alpha1ListClaimReviewMarkupPagesResponseOut"
        ]
    )
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
    types["GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewIn"] = t.struct(
        {
            "publisher": t.proxy(
                renames["GoogleFactcheckingFactchecktoolsV1alpha1PublisherIn"]
            ).optional(),
            "textualRating": t.string().optional(),
            "languageCode": t.string().optional(),
            "url": t.string().optional(),
            "title": t.string().optional(),
            "reviewDate": t.string().optional(),
        }
    ).named(renames["GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewIn"])
    types["GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewOut"] = t.struct(
        {
            "publisher": t.proxy(
                renames["GoogleFactcheckingFactchecktoolsV1alpha1PublisherOut"]
            ).optional(),
            "textualRating": t.string().optional(),
            "languageCode": t.string().optional(),
            "url": t.string().optional(),
            "title": t.string().optional(),
            "reviewDate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewOut"])
    types["GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupIn"] = t.struct(
        {
            "claimAppearances": t.array(t.string()).optional(),
            "claimFirstAppearance": t.string().optional(),
            "rating": t.proxy(
                renames["GoogleFactcheckingFactchecktoolsV1alpha1ClaimRatingIn"]
            ).optional(),
            "claimLocation": t.string().optional(),
            "claimDate": t.string().optional(),
            "claimAuthor": t.proxy(
                renames["GoogleFactcheckingFactchecktoolsV1alpha1ClaimAuthorIn"]
            ).optional(),
            "url": t.string().optional(),
            "claimReviewed": t.string().optional(),
        }
    ).named(renames["GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupIn"])
    types["GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupOut"] = t.struct(
        {
            "claimAppearances": t.array(t.string()).optional(),
            "claimFirstAppearance": t.string().optional(),
            "rating": t.proxy(
                renames["GoogleFactcheckingFactchecktoolsV1alpha1ClaimRatingOut"]
            ).optional(),
            "claimLocation": t.string().optional(),
            "claimDate": t.string().optional(),
            "claimAuthor": t.proxy(
                renames["GoogleFactcheckingFactchecktoolsV1alpha1ClaimAuthorOut"]
            ).optional(),
            "url": t.string().optional(),
            "claimReviewed": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupOut"])
    types["GoogleFactcheckingFactchecktoolsV1alpha1ClaimIn"] = t.struct(
        {
            "text": t.string().optional(),
            "claimant": t.string().optional(),
            "claimReview": t.array(
                t.proxy(
                    renames["GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewIn"]
                )
            ).optional(),
            "claimDate": t.string().optional(),
        }
    ).named(renames["GoogleFactcheckingFactchecktoolsV1alpha1ClaimIn"])
    types["GoogleFactcheckingFactchecktoolsV1alpha1ClaimOut"] = t.struct(
        {
            "text": t.string().optional(),
            "claimant": t.string().optional(),
            "claimReview": t.array(
                t.proxy(
                    renames["GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewOut"]
                )
            ).optional(),
            "claimDate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFactcheckingFactchecktoolsV1alpha1ClaimOut"])
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
    types["GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewAuthorIn"] = t.struct(
        {"name": t.string().optional(), "imageUrl": t.string().optional()}
    ).named(renames["GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewAuthorIn"])
    types["GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewAuthorOut"] = t.struct(
        {
            "name": t.string().optional(),
            "imageUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewAuthorOut"])
    types["GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupPageIn"] = t.struct(
        {
            "name": t.string().optional(),
            "claimReviewMarkups": t.array(
                t.proxy(
                    renames[
                        "GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupIn"
                    ]
                )
            ).optional(),
            "pageUrl": t.string().optional(),
            "claimReviewAuthor": t.proxy(
                renames["GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewAuthorIn"]
            ).optional(),
            "publishDate": t.string().optional(),
            "versionId": t.string().optional(),
        }
    ).named(renames["GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupPageIn"])
    types[
        "GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupPageOut"
    ] = t.struct(
        {
            "name": t.string().optional(),
            "claimReviewMarkups": t.array(
                t.proxy(
                    renames[
                        "GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupOut"
                    ]
                )
            ).optional(),
            "pageUrl": t.string().optional(),
            "claimReviewAuthor": t.proxy(
                renames["GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewAuthorOut"]
            ).optional(),
            "publishDate": t.string().optional(),
            "versionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupPageOut"]
    )
    types["GoogleFactcheckingFactchecktoolsV1alpha1ClaimRatingIn"] = t.struct(
        {
            "worstRating": t.integer().optional(),
            "ratingExplanation": t.string().optional(),
            "bestRating": t.integer().optional(),
            "imageUrl": t.string().optional(),
            "textualRating": t.string().optional(),
            "ratingValue": t.integer().optional(),
        }
    ).named(renames["GoogleFactcheckingFactchecktoolsV1alpha1ClaimRatingIn"])
    types["GoogleFactcheckingFactchecktoolsV1alpha1ClaimRatingOut"] = t.struct(
        {
            "worstRating": t.integer().optional(),
            "ratingExplanation": t.string().optional(),
            "bestRating": t.integer().optional(),
            "imageUrl": t.string().optional(),
            "textualRating": t.string().optional(),
            "ratingValue": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFactcheckingFactchecktoolsV1alpha1ClaimRatingOut"])
    types["GoogleFactcheckingFactchecktoolsV1alpha1ClaimAuthorIn"] = t.struct(
        {
            "imageUrl": t.string().optional(),
            "sameAs": t.string().optional(),
            "jobTitle": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleFactcheckingFactchecktoolsV1alpha1ClaimAuthorIn"])
    types["GoogleFactcheckingFactchecktoolsV1alpha1ClaimAuthorOut"] = t.struct(
        {
            "imageUrl": t.string().optional(),
            "sameAs": t.string().optional(),
            "jobTitle": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFactcheckingFactchecktoolsV1alpha1ClaimAuthorOut"])

    functions = {}
    functions["claimsSearch"] = factchecktools.get(
        "v1alpha1/claims:search",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "maxAgeDays": t.integer().optional(),
                "pageToken": t.string().optional(),
                "languageCode": t.string().optional(),
                "offset": t.integer().optional(),
                "reviewPublisherSiteFilter": t.string().optional(),
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
    functions["pagesUpdate"] = factchecktools.delete(
        "v1alpha1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["pagesCreate"] = factchecktools.delete(
        "v1alpha1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["pagesGet"] = factchecktools.delete(
        "v1alpha1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["pagesList"] = factchecktools.delete(
        "v1alpha1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["pagesDelete"] = factchecktools.delete(
        "v1alpha1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="factchecktools",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
