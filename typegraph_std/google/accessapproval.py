from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_accessapproval() -> Import:
    accessapproval = HTTPRuntime("https://accessapproval.googleapis.com/")

    renames = {
        "ErrorResponse": "_accessapproval_1_ErrorResponse",
        "AccessReasonIn": "_accessapproval_2_AccessReasonIn",
        "AccessReasonOut": "_accessapproval_3_AccessReasonOut",
        "ApproveApprovalRequestMessageIn": "_accessapproval_4_ApproveApprovalRequestMessageIn",
        "ApproveApprovalRequestMessageOut": "_accessapproval_5_ApproveApprovalRequestMessageOut",
        "AccessLocationsIn": "_accessapproval_6_AccessLocationsIn",
        "AccessLocationsOut": "_accessapproval_7_AccessLocationsOut",
        "DismissApprovalRequestMessageIn": "_accessapproval_8_DismissApprovalRequestMessageIn",
        "DismissApprovalRequestMessageOut": "_accessapproval_9_DismissApprovalRequestMessageOut",
        "SignatureInfoIn": "_accessapproval_10_SignatureInfoIn",
        "SignatureInfoOut": "_accessapproval_11_SignatureInfoOut",
        "ApproveDecisionIn": "_accessapproval_12_ApproveDecisionIn",
        "ApproveDecisionOut": "_accessapproval_13_ApproveDecisionOut",
        "DismissDecisionIn": "_accessapproval_14_DismissDecisionIn",
        "DismissDecisionOut": "_accessapproval_15_DismissDecisionOut",
        "EmptyIn": "_accessapproval_16_EmptyIn",
        "EmptyOut": "_accessapproval_17_EmptyOut",
        "AccessApprovalSettingsIn": "_accessapproval_18_AccessApprovalSettingsIn",
        "AccessApprovalSettingsOut": "_accessapproval_19_AccessApprovalSettingsOut",
        "AccessApprovalServiceAccountIn": "_accessapproval_20_AccessApprovalServiceAccountIn",
        "AccessApprovalServiceAccountOut": "_accessapproval_21_AccessApprovalServiceAccountOut",
        "ListApprovalRequestsResponseIn": "_accessapproval_22_ListApprovalRequestsResponseIn",
        "ListApprovalRequestsResponseOut": "_accessapproval_23_ListApprovalRequestsResponseOut",
        "ResourcePropertiesIn": "_accessapproval_24_ResourcePropertiesIn",
        "ResourcePropertiesOut": "_accessapproval_25_ResourcePropertiesOut",
        "InvalidateApprovalRequestMessageIn": "_accessapproval_26_InvalidateApprovalRequestMessageIn",
        "InvalidateApprovalRequestMessageOut": "_accessapproval_27_InvalidateApprovalRequestMessageOut",
        "ApprovalRequestIn": "_accessapproval_28_ApprovalRequestIn",
        "ApprovalRequestOut": "_accessapproval_29_ApprovalRequestOut",
        "EnrolledServiceIn": "_accessapproval_30_EnrolledServiceIn",
        "EnrolledServiceOut": "_accessapproval_31_EnrolledServiceOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["ApproveApprovalRequestMessageIn"] = t.struct(
        {"expireTime": t.string().optional()}
    ).named(renames["ApproveApprovalRequestMessageIn"])
    types["ApproveApprovalRequestMessageOut"] = t.struct(
        {
            "expireTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApproveApprovalRequestMessageOut"])
    types["AccessLocationsIn"] = t.struct(
        {
            "principalOfficeCountry": t.string().optional(),
            "principalPhysicalLocationCountry": t.string().optional(),
        }
    ).named(renames["AccessLocationsIn"])
    types["AccessLocationsOut"] = t.struct(
        {
            "principalOfficeCountry": t.string().optional(),
            "principalPhysicalLocationCountry": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccessLocationsOut"])
    types["DismissApprovalRequestMessageIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DismissApprovalRequestMessageIn"])
    types["DismissApprovalRequestMessageOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DismissApprovalRequestMessageOut"])
    types["SignatureInfoIn"] = t.struct(
        {
            "customerKmsKeyVersion": t.string().optional(),
            "googlePublicKeyPem": t.string().optional(),
            "signature": t.string().optional(),
        }
    ).named(renames["SignatureInfoIn"])
    types["SignatureInfoOut"] = t.struct(
        {
            "customerKmsKeyVersion": t.string().optional(),
            "googlePublicKeyPem": t.string().optional(),
            "signature": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SignatureInfoOut"])
    types["ApproveDecisionIn"] = t.struct(
        {
            "signatureInfo": t.proxy(renames["SignatureInfoIn"]).optional(),
            "expireTime": t.string().optional(),
            "invalidateTime": t.string().optional(),
            "autoApproved": t.boolean().optional(),
            "approveTime": t.string().optional(),
        }
    ).named(renames["ApproveDecisionIn"])
    types["ApproveDecisionOut"] = t.struct(
        {
            "signatureInfo": t.proxy(renames["SignatureInfoOut"]).optional(),
            "expireTime": t.string().optional(),
            "invalidateTime": t.string().optional(),
            "autoApproved": t.boolean().optional(),
            "approveTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApproveDecisionOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["AccessApprovalSettingsIn"] = t.struct(
        {
            "activeKeyVersion": t.string().optional(),
            "preferredRequestExpirationDays": t.integer().optional(),
            "notificationEmails": t.array(t.string()).optional(),
            "enrolledServices": t.array(
                t.proxy(renames["EnrolledServiceIn"])
            ).optional(),
            "name": t.string().optional(),
            "preferNoBroadApprovalRequests": t.boolean().optional(),
        }
    ).named(renames["AccessApprovalSettingsIn"])
    types["AccessApprovalSettingsOut"] = t.struct(
        {
            "activeKeyVersion": t.string().optional(),
            "preferredRequestExpirationDays": t.integer().optional(),
            "notificationEmails": t.array(t.string()).optional(),
            "invalidKeyVersion": t.boolean().optional(),
            "enrolledServices": t.array(
                t.proxy(renames["EnrolledServiceOut"])
            ).optional(),
            "name": t.string().optional(),
            "ancestorHasActiveKeyVersion": t.boolean().optional(),
            "preferNoBroadApprovalRequests": t.boolean().optional(),
            "enrolledAncestor": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccessApprovalSettingsOut"])
    types["AccessApprovalServiceAccountIn"] = t.struct(
        {"name": t.string().optional(), "accountEmail": t.string().optional()}
    ).named(renames["AccessApprovalServiceAccountIn"])
    types["AccessApprovalServiceAccountOut"] = t.struct(
        {
            "name": t.string().optional(),
            "accountEmail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccessApprovalServiceAccountOut"])
    types["ListApprovalRequestsResponseIn"] = t.struct(
        {
            "approvalRequests": t.array(
                t.proxy(renames["ApprovalRequestIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListApprovalRequestsResponseIn"])
    types["ListApprovalRequestsResponseOut"] = t.struct(
        {
            "approvalRequests": t.array(
                t.proxy(renames["ApprovalRequestOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListApprovalRequestsResponseOut"])
    types["ResourcePropertiesIn"] = t.struct(
        {"excludesDescendants": t.boolean().optional()}
    ).named(renames["ResourcePropertiesIn"])
    types["ResourcePropertiesOut"] = t.struct(
        {
            "excludesDescendants": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourcePropertiesOut"])
    types["InvalidateApprovalRequestMessageIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["InvalidateApprovalRequestMessageIn"])
    types["InvalidateApprovalRequestMessageOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["InvalidateApprovalRequestMessageOut"])
    types["ApprovalRequestIn"] = t.struct(
        {
            "approve": t.proxy(renames["ApproveDecisionIn"]).optional(),
            "requestedResourceProperties": t.proxy(
                renames["ResourcePropertiesIn"]
            ).optional(),
            "requestedLocations": t.proxy(renames["AccessLocationsIn"]).optional(),
            "requestedResourceName": t.string().optional(),
            "name": t.string().optional(),
            "dismiss": t.proxy(renames["DismissDecisionIn"]).optional(),
            "requestedExpiration": t.string().optional(),
            "requestedReason": t.proxy(renames["AccessReasonIn"]).optional(),
            "requestTime": t.string().optional(),
        }
    ).named(renames["ApprovalRequestIn"])
    types["ApprovalRequestOut"] = t.struct(
        {
            "approve": t.proxy(renames["ApproveDecisionOut"]).optional(),
            "requestedResourceProperties": t.proxy(
                renames["ResourcePropertiesOut"]
            ).optional(),
            "requestedLocations": t.proxy(renames["AccessLocationsOut"]).optional(),
            "requestedResourceName": t.string().optional(),
            "name": t.string().optional(),
            "dismiss": t.proxy(renames["DismissDecisionOut"]).optional(),
            "requestedExpiration": t.string().optional(),
            "requestedReason": t.proxy(renames["AccessReasonOut"]).optional(),
            "requestTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApprovalRequestOut"])
    types["EnrolledServiceIn"] = t.struct(
        {
            "cloudProduct": t.string().optional(),
            "enrollmentLevel": t.string().optional(),
        }
    ).named(renames["EnrolledServiceIn"])
    types["EnrolledServiceOut"] = t.struct(
        {
            "cloudProduct": t.string().optional(),
            "enrollmentLevel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnrolledServiceOut"])

    functions = {}
    functions["projectsGetServiceAccount"] = accessapproval.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
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
    functions["foldersUpdateAccessApprovalSettings"] = accessapproval.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["AccessApprovalServiceAccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersDeleteAccessApprovalSettings"] = accessapproval.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["AccessApprovalServiceAccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersGetAccessApprovalSettings"] = accessapproval.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["AccessApprovalServiceAccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersGetServiceAccount"] = accessapproval.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["AccessApprovalServiceAccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersApprovalRequestsGet"] = accessapproval.get(
        "v1/{parent}/approvalRequests",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListApprovalRequestsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersApprovalRequestsDismiss"] = accessapproval.get(
        "v1/{parent}/approvalRequests",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListApprovalRequestsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersApprovalRequestsInvalidate"] = accessapproval.get(
        "v1/{parent}/approvalRequests",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListApprovalRequestsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersApprovalRequestsApprove"] = accessapproval.get(
        "v1/{parent}/approvalRequests",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListApprovalRequestsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersApprovalRequestsList"] = accessapproval.get(
        "v1/{parent}/approvalRequests",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListApprovalRequestsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDeleteAccessApprovalSettings"] = accessapproval.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "activeKeyVersion": t.string().optional(),
                "preferredRequestExpirationDays": t.integer().optional(),
                "notificationEmails": t.array(t.string()).optional(),
                "enrolledServices": t.array(
                    t.proxy(renames["EnrolledServiceIn"])
                ).optional(),
                "preferNoBroadApprovalRequests": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccessApprovalSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsGetServiceAccount"] = accessapproval.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "activeKeyVersion": t.string().optional(),
                "preferredRequestExpirationDays": t.integer().optional(),
                "notificationEmails": t.array(t.string()).optional(),
                "enrolledServices": t.array(
                    t.proxy(renames["EnrolledServiceIn"])
                ).optional(),
                "preferNoBroadApprovalRequests": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccessApprovalSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsGetAccessApprovalSettings"] = accessapproval.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "activeKeyVersion": t.string().optional(),
                "preferredRequestExpirationDays": t.integer().optional(),
                "notificationEmails": t.array(t.string()).optional(),
                "enrolledServices": t.array(
                    t.proxy(renames["EnrolledServiceIn"])
                ).optional(),
                "preferNoBroadApprovalRequests": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccessApprovalSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsUpdateAccessApprovalSettings"] = accessapproval.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "activeKeyVersion": t.string().optional(),
                "preferredRequestExpirationDays": t.integer().optional(),
                "notificationEmails": t.array(t.string()).optional(),
                "enrolledServices": t.array(
                    t.proxy(renames["EnrolledServiceIn"])
                ).optional(),
                "preferNoBroadApprovalRequests": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccessApprovalSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApprovalRequestsGet"] = accessapproval.post(
        "v1/{name}:dismiss",
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
    functions["organizationsApprovalRequestsInvalidate"] = accessapproval.post(
        "v1/{name}:dismiss",
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
    functions["organizationsApprovalRequestsApprove"] = accessapproval.post(
        "v1/{name}:dismiss",
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
    functions["organizationsApprovalRequestsList"] = accessapproval.post(
        "v1/{name}:dismiss",
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
    functions["organizationsApprovalRequestsDismiss"] = accessapproval.post(
        "v1/{name}:dismiss",
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
