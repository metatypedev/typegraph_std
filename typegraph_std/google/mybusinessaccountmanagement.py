from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_mybusinessaccountmanagement():
    mybusinessaccountmanagement = HTTPRuntime(
        "https://mybusinessaccountmanagement.googleapis.com/"
    )

    renames = {
        "ErrorResponse": "_mybusinessaccountmanagement_1_ErrorResponse",
        "ListInvitationsResponseIn": "_mybusinessaccountmanagement_2_ListInvitationsResponseIn",
        "ListInvitationsResponseOut": "_mybusinessaccountmanagement_3_ListInvitationsResponseOut",
        "TargetLocationIn": "_mybusinessaccountmanagement_4_TargetLocationIn",
        "TargetLocationOut": "_mybusinessaccountmanagement_5_TargetLocationOut",
        "ListLocationAdminsResponseIn": "_mybusinessaccountmanagement_6_ListLocationAdminsResponseIn",
        "ListLocationAdminsResponseOut": "_mybusinessaccountmanagement_7_ListLocationAdminsResponseOut",
        "EmptyIn": "_mybusinessaccountmanagement_8_EmptyIn",
        "EmptyOut": "_mybusinessaccountmanagement_9_EmptyOut",
        "InvitationIn": "_mybusinessaccountmanagement_10_InvitationIn",
        "InvitationOut": "_mybusinessaccountmanagement_11_InvitationOut",
        "AdminIn": "_mybusinessaccountmanagement_12_AdminIn",
        "AdminOut": "_mybusinessaccountmanagement_13_AdminOut",
        "TransferLocationRequestIn": "_mybusinessaccountmanagement_14_TransferLocationRequestIn",
        "TransferLocationRequestOut": "_mybusinessaccountmanagement_15_TransferLocationRequestOut",
        "AccountIn": "_mybusinessaccountmanagement_16_AccountIn",
        "AccountOut": "_mybusinessaccountmanagement_17_AccountOut",
        "DeclineInvitationRequestIn": "_mybusinessaccountmanagement_18_DeclineInvitationRequestIn",
        "DeclineInvitationRequestOut": "_mybusinessaccountmanagement_19_DeclineInvitationRequestOut",
        "PostalAddressIn": "_mybusinessaccountmanagement_20_PostalAddressIn",
        "PostalAddressOut": "_mybusinessaccountmanagement_21_PostalAddressOut",
        "ListAccountAdminsResponseIn": "_mybusinessaccountmanagement_22_ListAccountAdminsResponseIn",
        "ListAccountAdminsResponseOut": "_mybusinessaccountmanagement_23_ListAccountAdminsResponseOut",
        "AcceptInvitationRequestIn": "_mybusinessaccountmanagement_24_AcceptInvitationRequestIn",
        "AcceptInvitationRequestOut": "_mybusinessaccountmanagement_25_AcceptInvitationRequestOut",
        "ListAccountsResponseIn": "_mybusinessaccountmanagement_26_ListAccountsResponseIn",
        "ListAccountsResponseOut": "_mybusinessaccountmanagement_27_ListAccountsResponseOut",
        "OrganizationInfoIn": "_mybusinessaccountmanagement_28_OrganizationInfoIn",
        "OrganizationInfoOut": "_mybusinessaccountmanagement_29_OrganizationInfoOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
        {"locationName": t.string().optional(), "address": t.string().optional()}
    ).named(renames["TargetLocationIn"])
    types["TargetLocationOut"] = t.struct(
        {
            "locationName": t.string().optional(),
            "address": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetLocationOut"])
    types["ListLocationAdminsResponseIn"] = t.struct(
        {"admins": t.array(t.proxy(renames["AdminIn"])).optional()}
    ).named(renames["ListLocationAdminsResponseIn"])
    types["ListLocationAdminsResponseOut"] = t.struct(
        {
            "admins": t.array(t.proxy(renames["AdminOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLocationAdminsResponseOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["InvitationIn"] = t.struct(
        {
            "name": t.string(),
            "targetAccount": t.proxy(renames["AccountIn"]).optional(),
            "targetLocation": t.proxy(renames["TargetLocationIn"]).optional(),
        }
    ).named(renames["InvitationIn"])
    types["InvitationOut"] = t.struct(
        {
            "name": t.string(),
            "targetAccount": t.proxy(renames["AccountOut"]).optional(),
            "targetLocation": t.proxy(renames["TargetLocationOut"]).optional(),
            "targetType": t.string().optional(),
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InvitationOut"])
    types["AdminIn"] = t.struct(
        {
            "name": t.string().optional(),
            "role": t.string(),
            "account": t.string().optional(),
            "admin": t.string().optional(),
        }
    ).named(renames["AdminIn"])
    types["AdminOut"] = t.struct(
        {
            "name": t.string().optional(),
            "role": t.string(),
            "pendingInvitation": t.boolean().optional(),
            "account": t.string().optional(),
            "admin": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdminOut"])
    types["TransferLocationRequestIn"] = t.struct(
        {"destinationAccount": t.string()}
    ).named(renames["TransferLocationRequestIn"])
    types["TransferLocationRequestOut"] = t.struct(
        {
            "destinationAccount": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransferLocationRequestOut"])
    types["AccountIn"] = t.struct(
        {
            "type": t.string(),
            "primaryOwner": t.string(),
            "accountName": t.string(),
            "name": t.string().optional(),
        }
    ).named(renames["AccountIn"])
    types["AccountOut"] = t.struct(
        {
            "permissionLevel": t.string().optional(),
            "organizationInfo": t.proxy(renames["OrganizationInfoOut"]).optional(),
            "type": t.string(),
            "verificationState": t.string().optional(),
            "role": t.string().optional(),
            "primaryOwner": t.string(),
            "vettedState": t.string().optional(),
            "accountNumber": t.string().optional(),
            "accountName": t.string(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountOut"])
    types["DeclineInvitationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeclineInvitationRequestIn"]
    )
    types["DeclineInvitationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeclineInvitationRequestOut"])
    types["PostalAddressIn"] = t.struct(
        {
            "revision": t.integer().optional(),
            "regionCode": t.string(),
            "postalCode": t.string().optional(),
            "languageCode": t.string().optional(),
            "organization": t.string().optional(),
            "addressLines": t.array(t.string()).optional(),
            "sublocality": t.string().optional(),
            "locality": t.string().optional(),
            "recipients": t.array(t.string()).optional(),
            "sortingCode": t.string().optional(),
            "administrativeArea": t.string().optional(),
        }
    ).named(renames["PostalAddressIn"])
    types["PostalAddressOut"] = t.struct(
        {
            "revision": t.integer().optional(),
            "regionCode": t.string(),
            "postalCode": t.string().optional(),
            "languageCode": t.string().optional(),
            "organization": t.string().optional(),
            "addressLines": t.array(t.string()).optional(),
            "sublocality": t.string().optional(),
            "locality": t.string().optional(),
            "recipients": t.array(t.string()).optional(),
            "sortingCode": t.string().optional(),
            "administrativeArea": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostalAddressOut"])
    types["ListAccountAdminsResponseIn"] = t.struct(
        {"accountAdmins": t.array(t.proxy(renames["AdminIn"])).optional()}
    ).named(renames["ListAccountAdminsResponseIn"])
    types["ListAccountAdminsResponseOut"] = t.struct(
        {
            "accountAdmins": t.array(t.proxy(renames["AdminOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAccountAdminsResponseOut"])
    types["AcceptInvitationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AcceptInvitationRequestIn"]
    )
    types["AcceptInvitationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AcceptInvitationRequestOut"])
    types["ListAccountsResponseIn"] = t.struct(
        {
            "accounts": t.array(t.proxy(renames["AccountIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListAccountsResponseIn"])
    types["ListAccountsResponseOut"] = t.struct(
        {
            "accounts": t.array(t.proxy(renames["AccountOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAccountsResponseOut"])
    types["OrganizationInfoIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OrganizationInfoIn"]
    )
    types["OrganizationInfoOut"] = t.struct(
        {
            "phoneNumber": t.string().optional(),
            "registeredDomain": t.string().optional(),
            "address": t.proxy(renames["PostalAddressOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrganizationInfoOut"])

    functions = {}
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
    functions["accountsPatch"] = mybusinessaccountmanagement.get(
        "v1/accounts",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parentAccount": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAccountsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCreate"] = mybusinessaccountmanagement.get(
        "v1/accounts",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parentAccount": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "parentAccount": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "parentAccount": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAccountsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsInvitationsAccept"] = mybusinessaccountmanagement.get(
        "v1/{parent}/invitations",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInvitationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsInvitationsDecline"] = mybusinessaccountmanagement.get(
        "v1/{parent}/invitations",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInvitationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsInvitationsList"] = mybusinessaccountmanagement.get(
        "v1/{parent}/invitations",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInvitationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdminsDelete"] = mybusinessaccountmanagement.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "role": t.string(),
                "account": t.string().optional(),
                "admin": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdminOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdminsCreate"] = mybusinessaccountmanagement.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "role": t.string(),
                "account": t.string().optional(),
                "admin": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdminOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdminsList"] = mybusinessaccountmanagement.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "role": t.string(),
                "account": t.string().optional(),
                "admin": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdminOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdminsPatch"] = mybusinessaccountmanagement.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "role": t.string(),
                "account": t.string().optional(),
                "admin": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdminOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="mybusinessaccountmanagement",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
