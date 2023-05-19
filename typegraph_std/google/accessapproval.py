from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_accessapproval() -> Import:
    accessapproval = HTTPRuntime("https://accessapproval.googleapis.com/")

    renames = {
        "ErrorResponse": "_accessapproval_1_ErrorResponse",
        "AccessApprovalSettingsIn": "_accessapproval_2_AccessApprovalSettingsIn",
        "AccessApprovalSettingsOut": "_accessapproval_3_AccessApprovalSettingsOut",
        "ApproveDecisionIn": "_accessapproval_4_ApproveDecisionIn",
        "ApproveDecisionOut": "_accessapproval_5_ApproveDecisionOut",
        "InvalidateApprovalRequestMessageIn": "_accessapproval_6_InvalidateApprovalRequestMessageIn",
        "InvalidateApprovalRequestMessageOut": "_accessapproval_7_InvalidateApprovalRequestMessageOut",
        "DismissApprovalRequestMessageIn": "_accessapproval_8_DismissApprovalRequestMessageIn",
        "DismissApprovalRequestMessageOut": "_accessapproval_9_DismissApprovalRequestMessageOut",
        "AccessLocationsIn": "_accessapproval_10_AccessLocationsIn",
        "AccessLocationsOut": "_accessapproval_11_AccessLocationsOut",
        "ApproveApprovalRequestMessageIn": "_accessapproval_12_ApproveApprovalRequestMessageIn",
        "ApproveApprovalRequestMessageOut": "_accessapproval_13_ApproveApprovalRequestMessageOut",
        "ApprovalRequestIn": "_accessapproval_14_ApprovalRequestIn",
        "ApprovalRequestOut": "_accessapproval_15_ApprovalRequestOut",
        "EmptyIn": "_accessapproval_16_EmptyIn",
        "EmptyOut": "_accessapproval_17_EmptyOut",
        "DismissDecisionIn": "_accessapproval_18_DismissDecisionIn",
        "DismissDecisionOut": "_accessapproval_19_DismissDecisionOut",
        "SignatureInfoIn": "_accessapproval_20_SignatureInfoIn",
        "SignatureInfoOut": "_accessapproval_21_SignatureInfoOut",
        "ListApprovalRequestsResponseIn": "_accessapproval_22_ListApprovalRequestsResponseIn",
        "ListApprovalRequestsResponseOut": "_accessapproval_23_ListApprovalRequestsResponseOut",
        "EnrolledServiceIn": "_accessapproval_24_EnrolledServiceIn",
        "EnrolledServiceOut": "_accessapproval_25_EnrolledServiceOut",
        "AccessReasonIn": "_accessapproval_26_AccessReasonIn",
        "AccessReasonOut": "_accessapproval_27_AccessReasonOut",
        "ResourcePropertiesIn": "_accessapproval_28_ResourcePropertiesIn",
        "ResourcePropertiesOut": "_accessapproval_29_ResourcePropertiesOut",
        "AccessApprovalServiceAccountIn": "_accessapproval_30_AccessApprovalServiceAccountIn",
        "AccessApprovalServiceAccountOut": "_accessapproval_31_AccessApprovalServiceAccountOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["AccessApprovalSettingsIn"] = t.struct(
        {
            "preferNoBroadApprovalRequests": t.boolean().optional(),
            "notificationEmails": t.array(t.string()).optional(),
            "enrolledServices": t.array(
                t.proxy(renames["EnrolledServiceIn"])
            ).optional(),
            "preferredRequestExpirationDays": t.integer().optional(),
            "activeKeyVersion": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["AccessApprovalSettingsIn"])
    types["AccessApprovalSettingsOut"] = t.struct(
        {
            "preferNoBroadApprovalRequests": t.boolean().optional(),
            "notificationEmails": t.array(t.string()).optional(),
            "enrolledServices": t.array(
                t.proxy(renames["EnrolledServiceOut"])
            ).optional(),
            "ancestorHasActiveKeyVersion": t.boolean().optional(),
            "enrolledAncestor": t.boolean().optional(),
            "preferredRequestExpirationDays": t.integer().optional(),
            "invalidKeyVersion": t.boolean().optional(),
            "activeKeyVersion": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccessApprovalSettingsOut"])
    types["ApproveDecisionIn"] = t.struct(
        {
            "autoApproved": t.boolean().optional(),
            "signatureInfo": t.proxy(renames["SignatureInfoIn"]).optional(),
            "expireTime": t.string().optional(),
            "approveTime": t.string().optional(),
            "invalidateTime": t.string().optional(),
        }
    ).named(renames["ApproveDecisionIn"])
    types["ApproveDecisionOut"] = t.struct(
        {
            "autoApproved": t.boolean().optional(),
            "signatureInfo": t.proxy(renames["SignatureInfoOut"]).optional(),
            "expireTime": t.string().optional(),
            "approveTime": t.string().optional(),
            "invalidateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApproveDecisionOut"])
    types["InvalidateApprovalRequestMessageIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["InvalidateApprovalRequestMessageIn"])
    types["InvalidateApprovalRequestMessageOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["InvalidateApprovalRequestMessageOut"])
    types["DismissApprovalRequestMessageIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DismissApprovalRequestMessageIn"])
    types["DismissApprovalRequestMessageOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DismissApprovalRequestMessageOut"])
    types["AccessLocationsIn"] = t.struct(
        {
            "principalPhysicalLocationCountry": t.string().optional(),
            "principalOfficeCountry": t.string().optional(),
        }
    ).named(renames["AccessLocationsIn"])
    types["AccessLocationsOut"] = t.struct(
        {
            "principalPhysicalLocationCountry": t.string().optional(),
            "principalOfficeCountry": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccessLocationsOut"])
    types["ApproveApprovalRequestMessageIn"] = t.struct(
        {"expireTime": t.string().optional()}
    ).named(renames["ApproveApprovalRequestMessageIn"])
    types["ApproveApprovalRequestMessageOut"] = t.struct(
        {
            "expireTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApproveApprovalRequestMessageOut"])
    types["ApprovalRequestIn"] = t.struct(
        {
            "requestTime": t.string().optional(),
            "name": t.string().optional(),
            "requestedLocations": t.proxy(renames["AccessLocationsIn"]).optional(),
            "requestedResourceProperties": t.proxy(
                renames["ResourcePropertiesIn"]
            ).optional(),
            "approve": t.proxy(renames["ApproveDecisionIn"]).optional(),
            "requestedResourceName": t.string().optional(),
            "dismiss": t.proxy(renames["DismissDecisionIn"]).optional(),
            "requestedReason": t.proxy(renames["AccessReasonIn"]).optional(),
            "requestedExpiration": t.string().optional(),
        }
    ).named(renames["ApprovalRequestIn"])
    types["ApprovalRequestOut"] = t.struct(
        {
            "requestTime": t.string().optional(),
            "name": t.string().optional(),
            "requestedLocations": t.proxy(renames["AccessLocationsOut"]).optional(),
            "requestedResourceProperties": t.proxy(
                renames["ResourcePropertiesOut"]
            ).optional(),
            "approve": t.proxy(renames["ApproveDecisionOut"]).optional(),
            "requestedResourceName": t.string().optional(),
            "dismiss": t.proxy(renames["DismissDecisionOut"]).optional(),
            "requestedReason": t.proxy(renames["AccessReasonOut"]).optional(),
            "requestedExpiration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApprovalRequestOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["DismissDecisionIn"] = t.struct(
        {"implicit": t.boolean().optional(), "dismissTime": t.string().optional()}
    ).named(renames["DismissDecisionIn"])
    types["DismissDecisionOut"] = t.struct(
        {
            "implicit": t.boolean().optional(),
            "dismissTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DismissDecisionOut"])
    types["SignatureInfoIn"] = t.struct(
        {
            "customerKmsKeyVersion": t.string().optional(),
            "signature": t.string().optional(),
            "googlePublicKeyPem": t.string().optional(),
        }
    ).named(renames["SignatureInfoIn"])
    types["SignatureInfoOut"] = t.struct(
        {
            "customerKmsKeyVersion": t.string().optional(),
            "signature": t.string().optional(),
            "googlePublicKeyPem": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SignatureInfoOut"])
    types["ListApprovalRequestsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "approvalRequests": t.array(
                t.proxy(renames["ApprovalRequestIn"])
            ).optional(),
        }
    ).named(renames["ListApprovalRequestsResponseIn"])
    types["ListApprovalRequestsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "approvalRequests": t.array(
                t.proxy(renames["ApprovalRequestOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListApprovalRequestsResponseOut"])
    types["EnrolledServiceIn"] = t.struct(
        {
            "enrollmentLevel": t.string().optional(),
            "cloudProduct": t.string().optional(),
        }
    ).named(renames["EnrolledServiceIn"])
    types["EnrolledServiceOut"] = t.struct(
        {
            "enrollmentLevel": t.string().optional(),
            "cloudProduct": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnrolledServiceOut"])
    types["AccessReasonIn"] = t.struct(
        {"type": t.string().optional(), "detail": t.string().optional()}
    ).named(renames["AccessReasonIn"])
    types["AccessReasonOut"] = t.struct(
        {
            "type": t.string().optional(),
            "detail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccessReasonOut"])
    types["ResourcePropertiesIn"] = t.struct(
        {"excludesDescendants": t.boolean().optional()}
    ).named(renames["ResourcePropertiesIn"])
    types["ResourcePropertiesOut"] = t.struct(
        {
            "excludesDescendants": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourcePropertiesOut"])
    types["AccessApprovalServiceAccountIn"] = t.struct(
        {"accountEmail": t.string().optional(), "name": t.string().optional()}
    ).named(renames["AccessApprovalServiceAccountIn"])
    types["AccessApprovalServiceAccountOut"] = t.struct(
        {
            "accountEmail": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccessApprovalServiceAccountOut"])

    functions = {}
    functions["organizationsGetServiceAccount"] = accessapproval.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["AccessApprovalSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsUpdateAccessApprovalSettings"] = accessapproval.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["AccessApprovalSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDeleteAccessApprovalSettings"] = accessapproval.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["AccessApprovalSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsGetAccessApprovalSettings"] = accessapproval.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["AccessApprovalSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApprovalRequestsApprove"] = accessapproval.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ApprovalRequestOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApprovalRequestsList"] = accessapproval.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ApprovalRequestOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApprovalRequestsInvalidate"] = accessapproval.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ApprovalRequestOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApprovalRequestsDismiss"] = accessapproval.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ApprovalRequestOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApprovalRequestsGet"] = accessapproval.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ApprovalRequestOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersGetServiceAccount"] = accessapproval.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["AccessApprovalSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersUpdateAccessApprovalSettings"] = accessapproval.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["AccessApprovalSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersDeleteAccessApprovalSettings"] = accessapproval.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["AccessApprovalSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersGetAccessApprovalSettings"] = accessapproval.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["AccessApprovalSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersApprovalRequestsDismiss"] = accessapproval.post(
        "v1/{name}:invalidate",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApprovalRequestOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersApprovalRequestsApprove"] = accessapproval.post(
        "v1/{name}:invalidate",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApprovalRequestOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersApprovalRequestsGet"] = accessapproval.post(
        "v1/{name}:invalidate",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApprovalRequestOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersApprovalRequestsList"] = accessapproval.post(
        "v1/{name}:invalidate",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApprovalRequestOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersApprovalRequestsInvalidate"] = accessapproval.post(
        "v1/{name}:invalidate",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApprovalRequestOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGetAccessApprovalSettings"] = accessapproval.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsUpdateAccessApprovalSettings"] = accessapproval.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGetServiceAccount"] = accessapproval.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDeleteAccessApprovalSettings"] = accessapproval.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsApprovalRequestsGet"] = accessapproval.post(
        "v1/{name}:invalidate",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApprovalRequestOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsApprovalRequestsDismiss"] = accessapproval.post(
        "v1/{name}:invalidate",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApprovalRequestOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsApprovalRequestsList"] = accessapproval.post(
        "v1/{name}:invalidate",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApprovalRequestOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsApprovalRequestsApprove"] = accessapproval.post(
        "v1/{name}:invalidate",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApprovalRequestOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsApprovalRequestsInvalidate"] = accessapproval.post(
        "v1/{name}:invalidate",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApprovalRequestOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="accessapproval",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
