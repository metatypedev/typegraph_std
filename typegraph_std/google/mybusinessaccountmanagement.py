from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_mybusinessaccountmanagement() -> Import:
    mybusinessaccountmanagement = HTTPRuntime(
        "https://mybusinessaccountmanagement.googleapis.com/"
    )

    renames = {
        "ErrorResponse": "_mybusinessaccountmanagement_1_ErrorResponse",
        "PostalAddressIn": "_mybusinessaccountmanagement_2_PostalAddressIn",
        "PostalAddressOut": "_mybusinessaccountmanagement_3_PostalAddressOut",
        "InvitationIn": "_mybusinessaccountmanagement_4_InvitationIn",
        "InvitationOut": "_mybusinessaccountmanagement_5_InvitationOut",
        "OrganizationInfoIn": "_mybusinessaccountmanagement_6_OrganizationInfoIn",
        "OrganizationInfoOut": "_mybusinessaccountmanagement_7_OrganizationInfoOut",
        "ListInvitationsResponseIn": "_mybusinessaccountmanagement_8_ListInvitationsResponseIn",
        "ListInvitationsResponseOut": "_mybusinessaccountmanagement_9_ListInvitationsResponseOut",
        "ListAccountAdminsResponseIn": "_mybusinessaccountmanagement_10_ListAccountAdminsResponseIn",
        "ListAccountAdminsResponseOut": "_mybusinessaccountmanagement_11_ListAccountAdminsResponseOut",
        "TransferLocationRequestIn": "_mybusinessaccountmanagement_12_TransferLocationRequestIn",
        "TransferLocationRequestOut": "_mybusinessaccountmanagement_13_TransferLocationRequestOut",
        "TargetLocationIn": "_mybusinessaccountmanagement_14_TargetLocationIn",
        "TargetLocationOut": "_mybusinessaccountmanagement_15_TargetLocationOut",
        "AccountIn": "_mybusinessaccountmanagement_16_AccountIn",
        "AccountOut": "_mybusinessaccountmanagement_17_AccountOut",
        "ListAccountsResponseIn": "_mybusinessaccountmanagement_18_ListAccountsResponseIn",
        "ListAccountsResponseOut": "_mybusinessaccountmanagement_19_ListAccountsResponseOut",
        "AdminIn": "_mybusinessaccountmanagement_20_AdminIn",
        "AdminOut": "_mybusinessaccountmanagement_21_AdminOut",
        "ListLocationAdminsResponseIn": "_mybusinessaccountmanagement_22_ListLocationAdminsResponseIn",
        "ListLocationAdminsResponseOut": "_mybusinessaccountmanagement_23_ListLocationAdminsResponseOut",
        "EmptyIn": "_mybusinessaccountmanagement_24_EmptyIn",
        "EmptyOut": "_mybusinessaccountmanagement_25_EmptyOut",
        "AcceptInvitationRequestIn": "_mybusinessaccountmanagement_26_AcceptInvitationRequestIn",
        "AcceptInvitationRequestOut": "_mybusinessaccountmanagement_27_AcceptInvitationRequestOut",
        "DeclineInvitationRequestIn": "_mybusinessaccountmanagement_28_DeclineInvitationRequestIn",
        "DeclineInvitationRequestOut": "_mybusinessaccountmanagement_29_DeclineInvitationRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["PostalAddressIn"] = t.struct(
        {
            "addressLines": t.array(t.string()).optional(),
            "recipients": t.array(t.string()).optional(),
            "locality": t.string().optional(),
            "regionCode": t.string(),
            "administrativeArea": t.string().optional(),
            "revision": t.integer().optional(),
            "organization": t.string().optional(),
            "languageCode": t.string().optional(),
            "postalCode": t.string().optional(),
            "sortingCode": t.string().optional(),
            "sublocality": t.string().optional(),
        }
    ).named(renames["PostalAddressIn"])
    types["PostalAddressOut"] = t.struct(
        {
            "addressLines": t.array(t.string()).optional(),
            "recipients": t.array(t.string()).optional(),
            "locality": t.string().optional(),
            "regionCode": t.string(),
            "administrativeArea": t.string().optional(),
            "revision": t.integer().optional(),
            "organization": t.string().optional(),
            "languageCode": t.string().optional(),
            "postalCode": t.string().optional(),
            "sortingCode": t.string().optional(),
            "sublocality": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostalAddressOut"])
    types["InvitationIn"] = t.struct(
        {
            "targetAccount": t.proxy(renames["AccountIn"]).optional(),
            "name": t.string(),
            "targetLocation": t.proxy(renames["TargetLocationIn"]).optional(),
        }
    ).named(renames["InvitationIn"])
    types["InvitationOut"] = t.struct(
        {
            "targetAccount": t.proxy(renames["AccountOut"]).optional(),
            "name": t.string(),
            "targetLocation": t.proxy(renames["TargetLocationOut"]).optional(),
            "role": t.string().optional(),
            "targetType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InvitationOut"])
    types["OrganizationInfoIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OrganizationInfoIn"]
    )
    types["OrganizationInfoOut"] = t.struct(
        {
            "address": t.proxy(renames["PostalAddressOut"]).optional(),
            "registeredDomain": t.string().optional(),
            "phoneNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrganizationInfoOut"])
    types["ListInvitationsResponseIn"] = t.struct(
        {"invitations": t.array(t.proxy(renames["InvitationIn"])).optional()}
    ).named(renames["ListInvitationsResponseIn"])
    types["ListInvitationsResponseOut"] = t.struct(
        {
            "invitations": t.array(t.proxy(renames["InvitationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListInvitationsResponseOut"])
    types["ListAccountAdminsResponseIn"] = t.struct(
        {"accountAdmins": t.array(t.proxy(renames["AdminIn"])).optional()}
    ).named(renames["ListAccountAdminsResponseIn"])
    types["ListAccountAdminsResponseOut"] = t.struct(
        {
            "accountAdmins": t.array(t.proxy(renames["AdminOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAccountAdminsResponseOut"])
    types["TransferLocationRequestIn"] = t.struct(
        {"destinationAccount": t.string()}
    ).named(renames["TransferLocationRequestIn"])
    types["TransferLocationRequestOut"] = t.struct(
        {
            "destinationAccount": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransferLocationRequestOut"])
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
    types["AccountIn"] = t.struct(
        {
            "type": t.string(),
            "name": t.string().optional(),
            "accountName": t.string(),
            "primaryOwner": t.string(),
        }
    ).named(renames["AccountIn"])
    types["AccountOut"] = t.struct(
        {
            "accountNumber": t.string().optional(),
            "role": t.string().optional(),
            "type": t.string(),
            "organizationInfo": t.proxy(renames["OrganizationInfoOut"]).optional(),
            "name": t.string().optional(),
            "verificationState": t.string().optional(),
            "vettedState": t.string().optional(),
            "accountName": t.string(),
            "permissionLevel": t.string().optional(),
            "primaryOwner": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountOut"])
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
    types["AdminIn"] = t.struct(
        {
            "account": t.string().optional(),
            "admin": t.string().optional(),
            "role": t.string(),
            "name": t.string().optional(),
        }
    ).named(renames["AdminIn"])
    types["AdminOut"] = t.struct(
        {
            "pendingInvitation": t.boolean().optional(),
            "account": t.string().optional(),
            "admin": t.string().optional(),
            "role": t.string(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdminOut"])
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
    types["AcceptInvitationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AcceptInvitationRequestIn"]
    )
    types["AcceptInvitationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AcceptInvitationRequestOut"])
    types["DeclineInvitationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeclineInvitationRequestIn"]
    )
    types["DeclineInvitationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeclineInvitationRequestOut"])

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
    functions["locationsAdminsList"] = mybusinessaccountmanagement.post(
        "v1/{parent}/admins",
        t.struct(
            {
                "parent": t.string(),
                "account": t.string().optional(),
                "admin": t.string().optional(),
                "role": t.string(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdminOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsAdminsDelete"] = mybusinessaccountmanagement.post(
        "v1/{parent}/admins",
        t.struct(
            {
                "parent": t.string(),
                "account": t.string().optional(),
                "admin": t.string().optional(),
                "role": t.string(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdminOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsAdminsPatch"] = mybusinessaccountmanagement.post(
        "v1/{parent}/admins",
        t.struct(
            {
                "parent": t.string(),
                "account": t.string().optional(),
                "admin": t.string().optional(),
                "role": t.string(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdminOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsAdminsCreate"] = mybusinessaccountmanagement.post(
        "v1/{parent}/admins",
        t.struct(
            {
                "parent": t.string(),
                "account": t.string().optional(),
                "admin": t.string().optional(),
                "role": t.string(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdminOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsList"] = mybusinessaccountmanagement.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "validateOnly": t.boolean().optional(),
                "type": t.string(),
                "accountName": t.string(),
                "primaryOwner": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsGet"] = mybusinessaccountmanagement.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "validateOnly": t.boolean().optional(),
                "type": t.string(),
                "accountName": t.string(),
                "primaryOwner": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCreate"] = mybusinessaccountmanagement.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "validateOnly": t.boolean().optional(),
                "type": t.string(),
                "accountName": t.string(),
                "primaryOwner": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsPatch"] = mybusinessaccountmanagement.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "validateOnly": t.boolean().optional(),
                "type": t.string(),
                "accountName": t.string(),
                "primaryOwner": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdminsDelete"] = mybusinessaccountmanagement.post(
        "v1/{parent}/admins",
        t.struct(
            {
                "parent": t.string(),
                "account": t.string().optional(),
                "admin": t.string().optional(),
                "role": t.string(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdminOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdminsList"] = mybusinessaccountmanagement.post(
        "v1/{parent}/admins",
        t.struct(
            {
                "parent": t.string(),
                "account": t.string().optional(),
                "admin": t.string().optional(),
                "role": t.string(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdminOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdminsPatch"] = mybusinessaccountmanagement.post(
        "v1/{parent}/admins",
        t.struct(
            {
                "parent": t.string(),
                "account": t.string().optional(),
                "admin": t.string().optional(),
                "role": t.string(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdminOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdminsCreate"] = mybusinessaccountmanagement.post(
        "v1/{parent}/admins",
        t.struct(
            {
                "parent": t.string(),
                "account": t.string().optional(),
                "admin": t.string().optional(),
                "role": t.string(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdminOut"]),
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

    return Import(
        importer="mybusinessaccountmanagement",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
