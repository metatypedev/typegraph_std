from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_mybusinessaccountmanagement() -> Import:
    mybusinessaccountmanagement = HTTPRuntime(
        "https://mybusinessaccountmanagement.googleapis.com/"
    )

    renames = {
        "ErrorResponse": "_mybusinessaccountmanagement_1_ErrorResponse",
        "ListAccountsResponseIn": "_mybusinessaccountmanagement_2_ListAccountsResponseIn",
        "ListAccountsResponseOut": "_mybusinessaccountmanagement_3_ListAccountsResponseOut",
        "OrganizationInfoIn": "_mybusinessaccountmanagement_4_OrganizationInfoIn",
        "OrganizationInfoOut": "_mybusinessaccountmanagement_5_OrganizationInfoOut",
        "ListLocationAdminsResponseIn": "_mybusinessaccountmanagement_6_ListLocationAdminsResponseIn",
        "ListLocationAdminsResponseOut": "_mybusinessaccountmanagement_7_ListLocationAdminsResponseOut",
        "TargetLocationIn": "_mybusinessaccountmanagement_8_TargetLocationIn",
        "TargetLocationOut": "_mybusinessaccountmanagement_9_TargetLocationOut",
        "PostalAddressIn": "_mybusinessaccountmanagement_10_PostalAddressIn",
        "PostalAddressOut": "_mybusinessaccountmanagement_11_PostalAddressOut",
        "AcceptInvitationRequestIn": "_mybusinessaccountmanagement_12_AcceptInvitationRequestIn",
        "AcceptInvitationRequestOut": "_mybusinessaccountmanagement_13_AcceptInvitationRequestOut",
        "AccountIn": "_mybusinessaccountmanagement_14_AccountIn",
        "AccountOut": "_mybusinessaccountmanagement_15_AccountOut",
        "AdminIn": "_mybusinessaccountmanagement_16_AdminIn",
        "AdminOut": "_mybusinessaccountmanagement_17_AdminOut",
        "InvitationIn": "_mybusinessaccountmanagement_18_InvitationIn",
        "InvitationOut": "_mybusinessaccountmanagement_19_InvitationOut",
        "TransferLocationRequestIn": "_mybusinessaccountmanagement_20_TransferLocationRequestIn",
        "TransferLocationRequestOut": "_mybusinessaccountmanagement_21_TransferLocationRequestOut",
        "ListAccountAdminsResponseIn": "_mybusinessaccountmanagement_22_ListAccountAdminsResponseIn",
        "ListAccountAdminsResponseOut": "_mybusinessaccountmanagement_23_ListAccountAdminsResponseOut",
        "DeclineInvitationRequestIn": "_mybusinessaccountmanagement_24_DeclineInvitationRequestIn",
        "DeclineInvitationRequestOut": "_mybusinessaccountmanagement_25_DeclineInvitationRequestOut",
        "EmptyIn": "_mybusinessaccountmanagement_26_EmptyIn",
        "EmptyOut": "_mybusinessaccountmanagement_27_EmptyOut",
        "ListInvitationsResponseIn": "_mybusinessaccountmanagement_28_ListInvitationsResponseIn",
        "ListInvitationsResponseOut": "_mybusinessaccountmanagement_29_ListInvitationsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["OrganizationInfoIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OrganizationInfoIn"]
    )
    types["OrganizationInfoOut"] = t.struct(
        {
            "registeredDomain": t.string().optional(),
            "phoneNumber": t.string().optional(),
            "address": t.proxy(renames["PostalAddressOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrganizationInfoOut"])
    types["ListLocationAdminsResponseIn"] = t.struct(
        {"admins": t.array(t.proxy(renames["AdminIn"])).optional()}
    ).named(renames["ListLocationAdminsResponseIn"])
    types["ListLocationAdminsResponseOut"] = t.struct(
        {
            "admins": t.array(t.proxy(renames["AdminOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLocationAdminsResponseOut"])
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
    types["PostalAddressIn"] = t.struct(
        {
            "recipients": t.array(t.string()).optional(),
            "organization": t.string().optional(),
            "locality": t.string().optional(),
            "addressLines": t.array(t.string()).optional(),
            "revision": t.integer().optional(),
            "postalCode": t.string().optional(),
            "sublocality": t.string().optional(),
            "sortingCode": t.string().optional(),
            "languageCode": t.string().optional(),
            "administrativeArea": t.string().optional(),
            "regionCode": t.string(),
        }
    ).named(renames["PostalAddressIn"])
    types["PostalAddressOut"] = t.struct(
        {
            "recipients": t.array(t.string()).optional(),
            "organization": t.string().optional(),
            "locality": t.string().optional(),
            "addressLines": t.array(t.string()).optional(),
            "revision": t.integer().optional(),
            "postalCode": t.string().optional(),
            "sublocality": t.string().optional(),
            "sortingCode": t.string().optional(),
            "languageCode": t.string().optional(),
            "administrativeArea": t.string().optional(),
            "regionCode": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostalAddressOut"])
    types["AcceptInvitationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AcceptInvitationRequestIn"]
    )
    types["AcceptInvitationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AcceptInvitationRequestOut"])
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
            "type": t.string(),
            "role": t.string().optional(),
            "accountNumber": t.string().optional(),
            "verificationState": t.string().optional(),
            "primaryOwner": t.string(),
            "accountName": t.string(),
            "permissionLevel": t.string().optional(),
            "organizationInfo": t.proxy(renames["OrganizationInfoOut"]).optional(),
            "vettedState": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountOut"])
    types["AdminIn"] = t.struct(
        {
            "admin": t.string().optional(),
            "role": t.string(),
            "name": t.string().optional(),
            "account": t.string().optional(),
        }
    ).named(renames["AdminIn"])
    types["AdminOut"] = t.struct(
        {
            "admin": t.string().optional(),
            "role": t.string(),
            "name": t.string().optional(),
            "account": t.string().optional(),
            "pendingInvitation": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdminOut"])
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
            "role": t.string().optional(),
            "targetAccount": t.proxy(renames["AccountOut"]).optional(),
            "targetType": t.string().optional(),
            "targetLocation": t.proxy(renames["TargetLocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InvitationOut"])
    types["TransferLocationRequestIn"] = t.struct(
        {"destinationAccount": t.string()}
    ).named(renames["TransferLocationRequestIn"])
    types["TransferLocationRequestOut"] = t.struct(
        {
            "destinationAccount": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransferLocationRequestOut"])
    types["ListAccountAdminsResponseIn"] = t.struct(
        {"accountAdmins": t.array(t.proxy(renames["AdminIn"])).optional()}
    ).named(renames["ListAccountAdminsResponseIn"])
    types["ListAccountAdminsResponseOut"] = t.struct(
        {
            "accountAdmins": t.array(t.proxy(renames["AdminOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAccountAdminsResponseOut"])
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
    types["ListInvitationsResponseIn"] = t.struct(
        {"invitations": t.array(t.proxy(renames["InvitationIn"])).optional()}
    ).named(renames["ListInvitationsResponseIn"])
    types["ListInvitationsResponseOut"] = t.struct(
        {
            "invitations": t.array(t.proxy(renames["InvitationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListInvitationsResponseOut"])

    functions = {}
    functions["accountsPatch"] = mybusinessaccountmanagement.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["AccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsList"] = mybusinessaccountmanagement.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["AccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsCreate"] = mybusinessaccountmanagement.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["AccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsGet"] = mybusinessaccountmanagement.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["AccountOut"]),
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
    functions["accountsAdminsDelete"] = mybusinessaccountmanagement.get(
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
    functions["locationsAdminsPatch"] = mybusinessaccountmanagement.delete(
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
        types=types,
        functions=functions,
    )
