from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_mybusinessaccountmanagement() -> Import:
    mybusinessaccountmanagement = HTTPRuntime(
        "https://mybusinessaccountmanagement.googleapis.com/"
    )

    renames = {
        "ErrorResponse": "_mybusinessaccountmanagement_1_ErrorResponse",
        "ListLocationAdminsResponseIn": "_mybusinessaccountmanagement_2_ListLocationAdminsResponseIn",
        "ListLocationAdminsResponseOut": "_mybusinessaccountmanagement_3_ListLocationAdminsResponseOut",
        "InvitationIn": "_mybusinessaccountmanagement_4_InvitationIn",
        "InvitationOut": "_mybusinessaccountmanagement_5_InvitationOut",
        "AdminIn": "_mybusinessaccountmanagement_6_AdminIn",
        "AdminOut": "_mybusinessaccountmanagement_7_AdminOut",
        "ListInvitationsResponseIn": "_mybusinessaccountmanagement_8_ListInvitationsResponseIn",
        "ListInvitationsResponseOut": "_mybusinessaccountmanagement_9_ListInvitationsResponseOut",
        "TargetLocationIn": "_mybusinessaccountmanagement_10_TargetLocationIn",
        "TargetLocationOut": "_mybusinessaccountmanagement_11_TargetLocationOut",
        "TransferLocationRequestIn": "_mybusinessaccountmanagement_12_TransferLocationRequestIn",
        "TransferLocationRequestOut": "_mybusinessaccountmanagement_13_TransferLocationRequestOut",
        "DeclineInvitationRequestIn": "_mybusinessaccountmanagement_14_DeclineInvitationRequestIn",
        "DeclineInvitationRequestOut": "_mybusinessaccountmanagement_15_DeclineInvitationRequestOut",
        "EmptyIn": "_mybusinessaccountmanagement_16_EmptyIn",
        "EmptyOut": "_mybusinessaccountmanagement_17_EmptyOut",
        "AcceptInvitationRequestIn": "_mybusinessaccountmanagement_18_AcceptInvitationRequestIn",
        "AcceptInvitationRequestOut": "_mybusinessaccountmanagement_19_AcceptInvitationRequestOut",
        "AccountIn": "_mybusinessaccountmanagement_20_AccountIn",
        "AccountOut": "_mybusinessaccountmanagement_21_AccountOut",
        "PostalAddressIn": "_mybusinessaccountmanagement_22_PostalAddressIn",
        "PostalAddressOut": "_mybusinessaccountmanagement_23_PostalAddressOut",
        "OrganizationInfoIn": "_mybusinessaccountmanagement_24_OrganizationInfoIn",
        "OrganizationInfoOut": "_mybusinessaccountmanagement_25_OrganizationInfoOut",
        "ListAccountsResponseIn": "_mybusinessaccountmanagement_26_ListAccountsResponseIn",
        "ListAccountsResponseOut": "_mybusinessaccountmanagement_27_ListAccountsResponseOut",
        "ListAccountAdminsResponseIn": "_mybusinessaccountmanagement_28_ListAccountAdminsResponseIn",
        "ListAccountAdminsResponseOut": "_mybusinessaccountmanagement_29_ListAccountAdminsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ListLocationAdminsResponseIn"] = t.struct(
        {"admins": t.array(t.proxy(renames["AdminIn"])).optional()}
    ).named(renames["ListLocationAdminsResponseIn"])
    types["ListLocationAdminsResponseOut"] = t.struct(
        {
            "admins": t.array(t.proxy(renames["AdminOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLocationAdminsResponseOut"])
    types["InvitationIn"] = t.struct(
        {
            "name": t.string(),
            "targetLocation": t.proxy(renames["TargetLocationIn"]).optional(),
            "targetAccount": t.proxy(renames["AccountIn"]).optional(),
        }
    ).named(renames["InvitationIn"])
    types["InvitationOut"] = t.struct(
        {
            "name": t.string(),
            "targetLocation": t.proxy(renames["TargetLocationOut"]).optional(),
            "role": t.string().optional(),
            "targetAccount": t.proxy(renames["AccountOut"]).optional(),
            "targetType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InvitationOut"])
    types["AdminIn"] = t.struct(
        {
            "role": t.string(),
            "admin": t.string().optional(),
            "name": t.string().optional(),
            "account": t.string().optional(),
        }
    ).named(renames["AdminIn"])
    types["AdminOut"] = t.struct(
        {
            "pendingInvitation": t.boolean().optional(),
            "role": t.string(),
            "admin": t.string().optional(),
            "name": t.string().optional(),
            "account": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdminOut"])
    types["ListInvitationsResponseIn"] = t.struct(
        {"invitations": t.array(t.proxy(renames["InvitationIn"])).optional()}
    ).named(renames["ListInvitationsResponseIn"])
    types["ListInvitationsResponseOut"] = t.struct(
        {
            "invitations": t.array(t.proxy(renames["InvitationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListInvitationsResponseOut"])
    types["TargetLocationIn"] = t.struct(
        {"address": t.string().optional(), "locationName": t.string().optional()}
    ).named(renames["TargetLocationIn"])
    types["TargetLocationOut"] = t.struct(
        {
            "address": t.string().optional(),
            "locationName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetLocationOut"])
    types["TransferLocationRequestIn"] = t.struct(
        {"destinationAccount": t.string()}
    ).named(renames["TransferLocationRequestIn"])
    types["TransferLocationRequestOut"] = t.struct(
        {
            "destinationAccount": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransferLocationRequestOut"])
    types["DeclineInvitationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeclineInvitationRequestIn"]
    )
    types["DeclineInvitationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeclineInvitationRequestOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["AcceptInvitationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AcceptInvitationRequestIn"]
    )
    types["AcceptInvitationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AcceptInvitationRequestOut"])
    types["AccountIn"] = t.struct(
        {
            "accountName": t.string(),
            "name": t.string().optional(),
            "type": t.string(),
            "primaryOwner": t.string(),
        }
    ).named(renames["AccountIn"])
    types["AccountOut"] = t.struct(
        {
            "role": t.string().optional(),
            "vettedState": t.string().optional(),
            "organizationInfo": t.proxy(renames["OrganizationInfoOut"]).optional(),
            "verificationState": t.string().optional(),
            "permissionLevel": t.string().optional(),
            "accountName": t.string(),
            "accountNumber": t.string().optional(),
            "name": t.string().optional(),
            "type": t.string(),
            "primaryOwner": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountOut"])
    types["PostalAddressIn"] = t.struct(
        {
            "postalCode": t.string().optional(),
            "locality": t.string().optional(),
            "sublocality": t.string().optional(),
            "regionCode": t.string(),
            "administrativeArea": t.string().optional(),
            "addressLines": t.array(t.string()).optional(),
            "sortingCode": t.string().optional(),
            "organization": t.string().optional(),
            "recipients": t.array(t.string()).optional(),
            "revision": t.integer().optional(),
            "languageCode": t.string().optional(),
        }
    ).named(renames["PostalAddressIn"])
    types["PostalAddressOut"] = t.struct(
        {
            "postalCode": t.string().optional(),
            "locality": t.string().optional(),
            "sublocality": t.string().optional(),
            "regionCode": t.string(),
            "administrativeArea": t.string().optional(),
            "addressLines": t.array(t.string()).optional(),
            "sortingCode": t.string().optional(),
            "organization": t.string().optional(),
            "recipients": t.array(t.string()).optional(),
            "revision": t.integer().optional(),
            "languageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostalAddressOut"])
    types["OrganizationInfoIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OrganizationInfoIn"]
    )
    types["OrganizationInfoOut"] = t.struct(
        {
            "address": t.proxy(renames["PostalAddressOut"]).optional(),
            "phoneNumber": t.string().optional(),
            "registeredDomain": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrganizationInfoOut"])
    types["ListAccountsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "accounts": t.array(t.proxy(renames["AccountIn"])).optional(),
        }
    ).named(renames["ListAccountsResponseIn"])
    types["ListAccountsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "accounts": t.array(t.proxy(renames["AccountOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAccountsResponseOut"])
    types["ListAccountAdminsResponseIn"] = t.struct(
        {"accountAdmins": t.array(t.proxy(renames["AdminIn"])).optional()}
    ).named(renames["ListAccountAdminsResponseIn"])
    types["ListAccountAdminsResponseOut"] = t.struct(
        {
            "accountAdmins": t.array(t.proxy(renames["AdminOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAccountAdminsResponseOut"])

    functions = {}
    functions["accountsCreate"] = mybusinessaccountmanagement.get(
        "v1/accounts",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parentAccount": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAccountsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsPatch"] = mybusinessaccountmanagement.get(
        "v1/accounts",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parentAccount": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAccountsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsGet"] = mybusinessaccountmanagement.get(
        "v1/accounts",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parentAccount": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAccountsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsList"] = mybusinessaccountmanagement.get(
        "v1/accounts",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parentAccount": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAccountsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsInvitationsList"] = mybusinessaccountmanagement.post(
        "v1/{name}:decline",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsInvitationsAccept"] = mybusinessaccountmanagement.post(
        "v1/{name}:decline",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsInvitationsDecline"] = mybusinessaccountmanagement.post(
        "v1/{name}:decline",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdminsDelete"] = mybusinessaccountmanagement.get(
        "v1/{parent}/admins",
        t.struct({"parent": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ListAccountAdminsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdminsPatch"] = mybusinessaccountmanagement.get(
        "v1/{parent}/admins",
        t.struct({"parent": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ListAccountAdminsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdminsCreate"] = mybusinessaccountmanagement.get(
        "v1/{parent}/admins",
        t.struct({"parent": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ListAccountAdminsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdminsList"] = mybusinessaccountmanagement.get(
        "v1/{parent}/admins",
        t.struct({"parent": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ListAccountAdminsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsTransfer"] = mybusinessaccountmanagement.post(
        "v1/{name}:transfer",
        t.struct(
            {
                "name": t.string(),
                "destinationAccount": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsAdminsCreate"] = mybusinessaccountmanagement.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsAdminsList"] = mybusinessaccountmanagement.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsAdminsPatch"] = mybusinessaccountmanagement.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsAdminsDelete"] = mybusinessaccountmanagement.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="mybusinessaccountmanagement",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
