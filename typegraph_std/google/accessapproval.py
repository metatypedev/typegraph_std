from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_accessapproval():
    accessapproval = HTTPRuntime("https://accessapproval.googleapis.com/")

    renames = {
        "ErrorResponse": "_accessapproval_1_ErrorResponse",
        "EmptyIn": "_accessapproval_2_EmptyIn",
        "EmptyOut": "_accessapproval_3_EmptyOut",
        "ResourcePropertiesIn": "_accessapproval_4_ResourcePropertiesIn",
        "ResourcePropertiesOut": "_accessapproval_5_ResourcePropertiesOut",
        "InvalidateApprovalRequestMessageIn": "_accessapproval_6_InvalidateApprovalRequestMessageIn",
        "InvalidateApprovalRequestMessageOut": "_accessapproval_7_InvalidateApprovalRequestMessageOut",
        "AccessApprovalSettingsIn": "_accessapproval_8_AccessApprovalSettingsIn",
        "AccessApprovalSettingsOut": "_accessapproval_9_AccessApprovalSettingsOut",
        "ApprovalRequestIn": "_accessapproval_10_ApprovalRequestIn",
        "ApprovalRequestOut": "_accessapproval_11_ApprovalRequestOut",
        "ApproveApprovalRequestMessageIn": "_accessapproval_12_ApproveApprovalRequestMessageIn",
        "ApproveApprovalRequestMessageOut": "_accessapproval_13_ApproveApprovalRequestMessageOut",
        "ListApprovalRequestsResponseIn": "_accessapproval_14_ListApprovalRequestsResponseIn",
        "ListApprovalRequestsResponseOut": "_accessapproval_15_ListApprovalRequestsResponseOut",
        "SignatureInfoIn": "_accessapproval_16_SignatureInfoIn",
        "SignatureInfoOut": "_accessapproval_17_SignatureInfoOut",
        "AccessReasonIn": "_accessapproval_18_AccessReasonIn",
        "AccessReasonOut": "_accessapproval_19_AccessReasonOut",
        "AccessLocationsIn": "_accessapproval_20_AccessLocationsIn",
        "AccessLocationsOut": "_accessapproval_21_AccessLocationsOut",
        "DismissApprovalRequestMessageIn": "_accessapproval_22_DismissApprovalRequestMessageIn",
        "DismissApprovalRequestMessageOut": "_accessapproval_23_DismissApprovalRequestMessageOut",
        "DismissDecisionIn": "_accessapproval_24_DismissDecisionIn",
        "DismissDecisionOut": "_accessapproval_25_DismissDecisionOut",
        "ApproveDecisionIn": "_accessapproval_26_ApproveDecisionIn",
        "ApproveDecisionOut": "_accessapproval_27_ApproveDecisionOut",
        "AccessApprovalServiceAccountIn": "_accessapproval_28_AccessApprovalServiceAccountIn",
        "AccessApprovalServiceAccountOut": "_accessapproval_29_AccessApprovalServiceAccountOut",
        "EnrolledServiceIn": "_accessapproval_30_EnrolledServiceIn",
        "EnrolledServiceOut": "_accessapproval_31_EnrolledServiceOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["AccessApprovalSettingsIn"] = t.struct(
        {
            "preferredRequestExpirationDays": t.integer().optional(),
            "preferNoBroadApprovalRequests": t.boolean().optional(),
            "activeKeyVersion": t.string().optional(),
            "enrolledServices": t.array(
                t.proxy(renames["EnrolledServiceIn"])
            ).optional(),
            "notificationEmails": t.array(t.string()).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["AccessApprovalSettingsIn"])
    types["AccessApprovalSettingsOut"] = t.struct(
        {
            "preferredRequestExpirationDays": t.integer().optional(),
            "preferNoBroadApprovalRequests": t.boolean().optional(),
            "activeKeyVersion": t.string().optional(),
            "enrolledAncestor": t.boolean().optional(),
            "invalidKeyVersion": t.boolean().optional(),
            "ancestorHasActiveKeyVersion": t.boolean().optional(),
            "enrolledServices": t.array(
                t.proxy(renames["EnrolledServiceOut"])
            ).optional(),
            "notificationEmails": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccessApprovalSettingsOut"])
    types["ApprovalRequestIn"] = t.struct(
        {
            "dismiss": t.proxy(renames["DismissDecisionIn"]).optional(),
            "approve": t.proxy(renames["ApproveDecisionIn"]).optional(),
            "requestedExpiration": t.string().optional(),
            "requestedResourceName": t.string().optional(),
            "requestedLocations": t.proxy(renames["AccessLocationsIn"]).optional(),
            "name": t.string().optional(),
            "requestedResourceProperties": t.proxy(
                renames["ResourcePropertiesIn"]
            ).optional(),
            "requestedReason": t.proxy(renames["AccessReasonIn"]).optional(),
            "requestTime": t.string().optional(),
        }
    ).named(renames["ApprovalRequestIn"])
    types["ApprovalRequestOut"] = t.struct(
        {
            "dismiss": t.proxy(renames["DismissDecisionOut"]).optional(),
            "approve": t.proxy(renames["ApproveDecisionOut"]).optional(),
            "requestedExpiration": t.string().optional(),
            "requestedResourceName": t.string().optional(),
            "requestedLocations": t.proxy(renames["AccessLocationsOut"]).optional(),
            "name": t.string().optional(),
            "requestedResourceProperties": t.proxy(
                renames["ResourcePropertiesOut"]
            ).optional(),
            "requestedReason": t.proxy(renames["AccessReasonOut"]).optional(),
            "requestTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApprovalRequestOut"])
    types["ApproveApprovalRequestMessageIn"] = t.struct(
        {"expireTime": t.string().optional()}
    ).named(renames["ApproveApprovalRequestMessageIn"])
    types["ApproveApprovalRequestMessageOut"] = t.struct(
        {
            "expireTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApproveApprovalRequestMessageOut"])
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
    types["SignatureInfoIn"] = t.struct(
        {
            "googlePublicKeyPem": t.string().optional(),
            "signature": t.string().optional(),
            "customerKmsKeyVersion": t.string().optional(),
        }
    ).named(renames["SignatureInfoIn"])
    types["SignatureInfoOut"] = t.struct(
        {
            "googlePublicKeyPem": t.string().optional(),
            "signature": t.string().optional(),
            "customerKmsKeyVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SignatureInfoOut"])
    types["AccessReasonIn"] = t.struct(
        {"detail": t.string().optional(), "type": t.string().optional()}
    ).named(renames["AccessReasonIn"])
    types["AccessReasonOut"] = t.struct(
        {
            "detail": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccessReasonOut"])
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
    types["ApproveDecisionIn"] = t.struct(
        {
            "invalidateTime": t.string().optional(),
            "autoApproved": t.boolean().optional(),
            "expireTime": t.string().optional(),
            "signatureInfo": t.proxy(renames["SignatureInfoIn"]).optional(),
            "approveTime": t.string().optional(),
        }
    ).named(renames["ApproveDecisionIn"])
    types["ApproveDecisionOut"] = t.struct(
        {
            "invalidateTime": t.string().optional(),
            "autoApproved": t.boolean().optional(),
            "expireTime": t.string().optional(),
            "signatureInfo": t.proxy(renames["SignatureInfoOut"]).optional(),
            "approveTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApproveDecisionOut"])
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

    functions = {}
    functions["organizationsUpdateAccessApprovalSettings"] = accessapproval.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsGetServiceAccount"] = accessapproval.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsGetAccessApprovalSettings"] = accessapproval.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDeleteAccessApprovalSettings"] = accessapproval.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
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
    functions["organizationsApprovalRequestsApprove"] = accessapproval.get(
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
    functions["foldersUpdateAccessApprovalSettings"] = accessapproval.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersGetServiceAccount"] = accessapproval.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersGetAccessApprovalSettings"] = accessapproval.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersDeleteAccessApprovalSettings"] = accessapproval.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
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
    functions["projectsGetServiceAccount"] = accessapproval.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "preferredRequestExpirationDays": t.integer().optional(),
                "preferNoBroadApprovalRequests": t.boolean().optional(),
                "activeKeyVersion": t.string().optional(),
                "enrolledServices": t.array(
                    t.proxy(renames["EnrolledServiceIn"])
                ).optional(),
                "notificationEmails": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccessApprovalSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDeleteAccessApprovalSettings"] = accessapproval.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "preferredRequestExpirationDays": t.integer().optional(),
                "preferNoBroadApprovalRequests": t.boolean().optional(),
                "activeKeyVersion": t.string().optional(),
                "enrolledServices": t.array(
                    t.proxy(renames["EnrolledServiceIn"])
                ).optional(),
                "notificationEmails": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccessApprovalSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGetAccessApprovalSettings"] = accessapproval.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "preferredRequestExpirationDays": t.integer().optional(),
                "preferNoBroadApprovalRequests": t.boolean().optional(),
                "activeKeyVersion": t.string().optional(),
                "enrolledServices": t.array(
                    t.proxy(renames["EnrolledServiceIn"])
                ).optional(),
                "notificationEmails": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccessApprovalSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsUpdateAccessApprovalSettings"] = accessapproval.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "preferredRequestExpirationDays": t.integer().optional(),
                "preferNoBroadApprovalRequests": t.boolean().optional(),
                "activeKeyVersion": t.string().optional(),
                "enrolledServices": t.array(
                    t.proxy(renames["EnrolledServiceIn"])
                ).optional(),
                "notificationEmails": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccessApprovalSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsApprovalRequestsList"] = accessapproval.post(
        "v1/{name}:approve",
        t.struct(
            {
                "name": t.string().optional(),
                "expireTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApprovalRequestOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsApprovalRequestsInvalidate"] = accessapproval.post(
        "v1/{name}:approve",
        t.struct(
            {
                "name": t.string().optional(),
                "expireTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApprovalRequestOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsApprovalRequestsDismiss"] = accessapproval.post(
        "v1/{name}:approve",
        t.struct(
            {
                "name": t.string().optional(),
                "expireTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApprovalRequestOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsApprovalRequestsGet"] = accessapproval.post(
        "v1/{name}:approve",
        t.struct(
            {
                "name": t.string().optional(),
                "expireTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApprovalRequestOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsApprovalRequestsApprove"] = accessapproval.post(
        "v1/{name}:approve",
        t.struct(
            {
                "name": t.string().optional(),
                "expireTime": t.string().optional(),
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
