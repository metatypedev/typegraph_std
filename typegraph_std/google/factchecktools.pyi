from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    GoogleProtobufEmptyIn: t.typedef = ...
    GoogleProtobufEmptyOut: t.typedef = ...
    GoogleFactcheckingFactchecktoolsV1alpha1FactCheckedClaimSearchResponseIn: t.typedef = (
        ...
    )
    GoogleFactcheckingFactchecktoolsV1alpha1FactCheckedClaimSearchResponseOut: t.typedef = (
        ...
    )
    GoogleFactcheckingFactchecktoolsV1alpha1ClaimRatingIn: t.typedef = ...
    GoogleFactcheckingFactchecktoolsV1alpha1ClaimRatingOut: t.typedef = ...
    GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupPageIn: t.typedef = ...
    GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupPageOut: t.typedef = ...
    GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupIn: t.typedef = ...
    GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupOut: t.typedef = ...
    GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewIn: t.typedef = ...
    GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewOut: t.typedef = ...
    GoogleFactcheckingFactchecktoolsV1alpha1ClaimAuthorIn: t.typedef = ...
    GoogleFactcheckingFactchecktoolsV1alpha1ClaimAuthorOut: t.typedef = ...
    GoogleFactcheckingFactchecktoolsV1alpha1PublisherIn: t.typedef = ...
    GoogleFactcheckingFactchecktoolsV1alpha1PublisherOut: t.typedef = ...
    GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewAuthorIn: t.typedef = ...
    GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewAuthorOut: t.typedef = ...
    GoogleFactcheckingFactchecktoolsV1alpha1ClaimIn: t.typedef = ...
    GoogleFactcheckingFactchecktoolsV1alpha1ClaimOut: t.typedef = ...
    GoogleFactcheckingFactchecktoolsV1alpha1ListClaimReviewMarkupPagesResponseIn: t.typedef = (
        ...
    )
    GoogleFactcheckingFactchecktoolsV1alpha1ListClaimReviewMarkupPagesResponseOut: t.typedef = (
        ...
    )

class FuncList:
    claimsSearch: t.func = ...
    pagesGet: t.func = ...
    pagesDelete: t.func = ...
    pagesList: t.func = ...
    pagesUpdate: t.func = ...
    pagesCreate: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_factchecktools() -> Import: ...
