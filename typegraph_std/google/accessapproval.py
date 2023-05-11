from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_accessapproval() -> Import:
    accessapproval = HTTPRuntime("https://accessapproval.googleapis.com/")

    renames = {
        "ErrorResponse": "_accessapproval_1_ErrorResponse",
        "AccessApprovalServiceAccountIn": "_accessapproval_2_AccessApprovalServiceAccountIn",
        "AccessApprovalServiceAccountOut": "_accessapproval_3_AccessApprovalServiceAccountOut",
        "EmptyIn": "_accessapproval_4_EmptyIn",
        "EmptyOut": "_accessapproval_5_EmptyOut",
        "ApprovalRequestIn": "_accessapproval_6_ApprovalRequestIn",
        "ApprovalRequestOut": "_accessapproval_7_ApprovalRequestOut",
        "SignatureInfoIn": "_accessapproval_8_SignatureInfoIn",
        "SignatureInfoOut": "_accessapproval_9_SignatureInfoOut",
        "ApproveDecisionIn": "_accessapproval_10_ApproveDecisionIn",
        "ApproveDecisionOut": "_accessapproval_11_ApproveDecisionOut",
        "ResourcePropertiesIn": "_accessapproval_12_ResourcePropertiesIn",
        "ResourcePropertiesOut": "_accessapproval_13_ResourcePropertiesOut",
        "AccessLocationsIn": "_accessapproval_14_AccessLocationsIn",
        "AccessLocationsOut": "_accessapproval_15_AccessLocationsOut",
        "InvalidateApprovalRequestMessageIn": "_accessapproval_16_InvalidateApprovalRequestMessageIn",
        "InvalidateApprovalRequestMessageOut": "_accessapproval_17_InvalidateApprovalRequestMessageOut",
        "ListApprovalRequestsResponseIn": "_accessapproval_18_ListApprovalRequestsResponseIn",
        "ListApprovalRequestsResponseOut": "_accessapproval_19_ListApprovalRequestsResponseOut",
        "AccessReasonIn": "_accessapproval_20_AccessReasonIn",
        "AccessReasonOut": "_accessapproval_21_AccessReasonOut",
        "ApproveApprovalRequestMessageIn": "_accessapproval_22_ApproveApprovalRequestMessageIn",
        "ApproveApprovalRequestMessageOut": "_accessapproval_23_ApproveApprovalRequestMessageOut",
        "DismissApprovalRequestMessageIn": "_accessapproval_24_DismissApprovalRequestMessageIn",
        "DismissApprovalRequestMessageOut": "_accessapproval_25_DismissApprovalRequestMessageOut",
        "AccessApprovalSettingsIn": "_accessapproval_26_AccessApprovalSettingsIn",
        "AccessApprovalSettingsOut": "_accessapproval_27_AccessApprovalSettingsOut",
        "EnrolledServiceIn": "_accessapproval_28_EnrolledServiceIn",
        "EnrolledServiceOut": "_accessapproval_29_EnrolledServiceOut",
        "DismissDecisionIn": "_accessapproval_30_DismissDecisionIn",
        "DismissDecisionOut": "_accessapproval_31_DismissDecisionOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ApprovalRequestIn"] = t.struct(
        {
            "requestedExpiration": t.string().optional(),
            "requestedResourceName": t.string().optional(),
            "dismiss": t.proxy(renames["DismissDecisionIn"]).optional(),
            "name": t.string().optional(),
            "approve": t.proxy(renames["ApproveDecisionIn"]).optional(),
            "requestedLocations": t.proxy(renames["AccessLocationsIn"]).optional(),
            "requestedReason": t.proxy(renames["AccessReasonIn"]).optional(),
            "requestedResourceProperties": t.proxy(
                renames["ResourcePropertiesIn"]
            ).optional(),
            "requestTime": t.string().optional(),
        }
    ).named(renames["ApprovalRequestIn"])
    types["ApprovalRequestOut"] = t.struct(
        {
            "requestedExpiration": t.string().optional(),
            "requestedResourceName": t.string().optional(),
            "dismiss": t.proxy(renames["DismissDecisionOut"]).optional(),
            "name": t.string().optional(),
            "approve": t.proxy(renames["ApproveDecisionOut"]).optional(),
            "requestedLocations": t.proxy(renames["AccessLocationsOut"]).optional(),
            "requestedReason": t.proxy(renames["AccessReasonOut"]).optional(),
            "requestedResourceProperties": t.proxy(
                renames["ResourcePropertiesOut"]
            ).optional(),
            "requestTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApprovalRequestOut"])
    types["SignatureInfoIn"] = t.struct(
        {
            "signature": t.string().optional(),
            "googlePublicKeyPem": t.string().optional(),
            "customerKmsKeyVersion": t.string().optional(),
        }
    ).named(renames["SignatureInfoIn"])
    types["SignatureInfoOut"] = t.struct(
        {
            "signature": t.string().optional(),
            "googlePublicKeyPem": t.string().optional(),
            "customerKmsKeyVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SignatureInfoOut"])
    types["ApproveDecisionIn"] = t.struct(
        {
            "invalidateTime": t.string().optional(),
            "approveTime": t.string().optional(),
            "autoApproved": t.boolean().optional(),
            "signatureInfo": t.proxy(renames["SignatureInfoIn"]).optional(),
            "expireTime": t.string().optional(),
        }
    ).named(renames["ApproveDecisionIn"])
    types["ApproveDecisionOut"] = t.struct(
        {
            "invalidateTime": t.string().optional(),
            "approveTime": t.string().optional(),
            "autoApproved": t.boolean().optional(),
            "signatureInfo": t.proxy(renames["SignatureInfoOut"]).optional(),
            "expireTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApproveDecisionOut"])
    types["ResourcePropertiesIn"] = t.struct(
        {"excludesDescendants": t.boolean().optional()}
    ).named(renames["ResourcePropertiesIn"])
    types["ResourcePropertiesOut"] = t.struct(
        {
            "excludesDescendants": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourcePropertiesOut"])
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
    types["InvalidateApprovalRequestMessageIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["InvalidateApprovalRequestMessageIn"])
    types["InvalidateApprovalRequestMessageOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["InvalidateApprovalRequestMessageOut"])
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
    types["ApproveApprovalRequestMessageIn"] = t.struct(
        {"expireTime": t.string().optional()}
    ).named(renames["ApproveApprovalRequestMessageIn"])
    types["ApproveApprovalRequestMessageOut"] = t.struct(
        {
            "expireTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApproveApprovalRequestMessageOut"])
    types["DismissApprovalRequestMessageIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DismissApprovalRequestMessageIn"])
    types["DismissApprovalRequestMessageOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DismissApprovalRequestMessageOut"])
    types["AccessApprovalSettingsIn"] = t.struct(
        {
            "preferNoBroadApprovalRequests": t.boolean().optional(),
            "enrolledServices": t.array(
                t.proxy(renames["EnrolledServiceIn"])
            ).optional(),
            "notificationEmails": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "preferredRequestExpirationDays": t.integer().optional(),
            "activeKeyVersion": t.string().optional(),
        }
    ).named(renames["AccessApprovalSettingsIn"])
    types["AccessApprovalSettingsOut"] = t.struct(
        {
            "preferNoBroadApprovalRequests": t.boolean().optional(),
            "enrolledServices": t.array(
                t.proxy(renames["EnrolledServiceOut"])
            ).optional(),
            "ancestorHasActiveKeyVersion": t.boolean().optional(),
            "notificationEmails": t.array(t.string()).optional(),
            "enrolledAncestor": t.boolean().optional(),
            "name": t.string().optional(),
            "preferredRequestExpirationDays": t.integer().optional(),
            "invalidKeyVersion": t.boolean().optional(),
            "activeKeyVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccessApprovalSettingsOut"])
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
    functions["projectsApprovalRequestsGet"] = accessapproval.get(
        "v1/{parent}/approvalRequests",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListApprovalRequestsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsApprovalRequestsInvalidate"] = accessapproval.get(
        "v1/{parent}/approvalRequests",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListApprovalRequestsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsApprovalRequestsDismiss"] = accessapproval.get(
        "v1/{parent}/approvalRequests",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListApprovalRequestsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsApprovalRequestsApprove"] = accessapproval.get(
        "v1/{parent}/approvalRequests",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListApprovalRequestsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsApprovalRequestsList"] = accessapproval.get(
        "v1/{parent}/approvalRequests",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListApprovalRequestsResponseOut"]),
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
    functions["organizationsUpdateAccessApprovalSettings"] = accessapproval.delete(
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
    functions["organizationsApprovalRequestsInvalidate"] = accessapproval.get(
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
    functions["foldersUpdateAccessApprovalSettings"] = accessapproval.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["AccessApprovalSettingsOut"]),
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
    functions["foldersApprovalRequestsInvalidate"] = accessapproval.post(
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
    functions["foldersApprovalRequestsApprove"] = accessapproval.post(
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
    functions["foldersApprovalRequestsList"] = accessapproval.post(
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
    functions["foldersApprovalRequestsGet"] = accessapproval.post(
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
    functions["foldersApprovalRequestsDismiss"] = accessapproval.post(
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
        importer="accessapproval", renames=renames, types=types, functions=functions
    )
