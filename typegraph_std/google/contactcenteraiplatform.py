from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_contactcenteraiplatform() -> Import:
    contactcenteraiplatform = HTTPRuntime(
        "https://contactcenteraiplatform.googleapis.com/"
    )

    renames = {
        "ErrorResponse": "_contactcenteraiplatform_1_ErrorResponse",
        "ContactCenterQuotaIn": "_contactcenteraiplatform_2_ContactCenterQuotaIn",
        "ContactCenterQuotaOut": "_contactcenteraiplatform_3_ContactCenterQuotaOut",
        "InstanceConfigIn": "_contactcenteraiplatform_4_InstanceConfigIn",
        "InstanceConfigOut": "_contactcenteraiplatform_5_InstanceConfigOut",
        "SAMLParamsIn": "_contactcenteraiplatform_6_SAMLParamsIn",
        "SAMLParamsOut": "_contactcenteraiplatform_7_SAMLParamsOut",
        "QuotaIn": "_contactcenteraiplatform_8_QuotaIn",
        "QuotaOut": "_contactcenteraiplatform_9_QuotaOut",
        "AdminUserIn": "_contactcenteraiplatform_10_AdminUserIn",
        "AdminUserOut": "_contactcenteraiplatform_11_AdminUserOut",
        "LocationIn": "_contactcenteraiplatform_12_LocationIn",
        "LocationOut": "_contactcenteraiplatform_13_LocationOut",
        "ContactCenterIn": "_contactcenteraiplatform_14_ContactCenterIn",
        "ContactCenterOut": "_contactcenteraiplatform_15_ContactCenterOut",
        "ListLocationsResponseIn": "_contactcenteraiplatform_16_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_contactcenteraiplatform_17_ListLocationsResponseOut",
        "ListContactCentersResponseIn": "_contactcenteraiplatform_18_ListContactCentersResponseIn",
        "ListContactCentersResponseOut": "_contactcenteraiplatform_19_ListContactCentersResponseOut",
        "ListOperationsResponseIn": "_contactcenteraiplatform_20_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_contactcenteraiplatform_21_ListOperationsResponseOut",
        "OperationIn": "_contactcenteraiplatform_22_OperationIn",
        "OperationOut": "_contactcenteraiplatform_23_OperationOut",
        "StatusIn": "_contactcenteraiplatform_24_StatusIn",
        "StatusOut": "_contactcenteraiplatform_25_StatusOut",
        "EmptyIn": "_contactcenteraiplatform_26_EmptyIn",
        "EmptyOut": "_contactcenteraiplatform_27_EmptyOut",
        "CancelOperationRequestIn": "_contactcenteraiplatform_28_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_contactcenteraiplatform_29_CancelOperationRequestOut",
        "URIsIn": "_contactcenteraiplatform_30_URIsIn",
        "URIsOut": "_contactcenteraiplatform_31_URIsOut",
        "OperationMetadataIn": "_contactcenteraiplatform_32_OperationMetadataIn",
        "OperationMetadataOut": "_contactcenteraiplatform_33_OperationMetadataOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ContactCenterQuotaIn"] = t.struct(
        {
            "contactCenterCountSum": t.integer().optional(),
            "contactCenterCountLimit": t.integer().optional(),
            "quotas": t.array(t.proxy(renames["QuotaIn"])).optional(),
        }
    ).named(renames["ContactCenterQuotaIn"])
    types["ContactCenterQuotaOut"] = t.struct(
        {
            "contactCenterCountSum": t.integer().optional(),
            "contactCenterCountLimit": t.integer().optional(),
            "quotas": t.array(t.proxy(renames["QuotaOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContactCenterQuotaOut"])
    types["InstanceConfigIn"] = t.struct({"instanceSize": t.string().optional()}).named(
        renames["InstanceConfigIn"]
    )
    types["InstanceConfigOut"] = t.struct(
        {
            "instanceSize": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceConfigOut"])
    types["SAMLParamsIn"] = t.struct(
        {
            "userEmail": t.string().optional(),
            "certificate": t.string().optional(),
            "entityId": t.string().optional(),
            "ssoUri": t.string().optional(),
        }
    ).named(renames["SAMLParamsIn"])
    types["SAMLParamsOut"] = t.struct(
        {
            "userEmail": t.string().optional(),
            "certificate": t.string().optional(),
            "entityId": t.string().optional(),
            "ssoUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SAMLParamsOut"])
    types["QuotaIn"] = t.struct(
        {
            "contactCenterInstanceSize": t.string().optional(),
            "contactCenterCountLimit": t.integer().optional(),
            "contactCenterCountSum": t.integer().optional(),
        }
    ).named(renames["QuotaIn"])
    types["QuotaOut"] = t.struct(
        {
            "contactCenterInstanceSize": t.string().optional(),
            "contactCenterCountLimit": t.integer().optional(),
            "contactCenterCountSum": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuotaOut"])
    types["AdminUserIn"] = t.struct(
        {"givenName": t.string().optional(), "familyName": t.string().optional()}
    ).named(renames["AdminUserIn"])
    types["AdminUserOut"] = t.struct(
        {
            "givenName": t.string().optional(),
            "familyName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdminUserOut"])
    types["LocationIn"] = t.struct(
        {
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["ContactCenterIn"] = t.struct(
        {
            "adminUser": t.proxy(renames["AdminUserIn"]).optional(),
            "displayName": t.string(),
            "instanceConfig": t.proxy(renames["InstanceConfigIn"]).optional(),
            "userEmail": t.string().optional(),
            "samlParams": t.proxy(renames["SAMLParamsIn"]).optional(),
            "ccaipManagedUsers": t.boolean().optional(),
            "name": t.string().optional(),
            "customerDomainPrefix": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ContactCenterIn"])
    types["ContactCenterOut"] = t.struct(
        {
            "adminUser": t.proxy(renames["AdminUserOut"]).optional(),
            "updateTime": t.string().optional(),
            "displayName": t.string(),
            "state": t.string().optional(),
            "uris": t.proxy(renames["URIsOut"]).optional(),
            "instanceConfig": t.proxy(renames["InstanceConfigOut"]).optional(),
            "userEmail": t.string().optional(),
            "samlParams": t.proxy(renames["SAMLParamsOut"]).optional(),
            "ccaipManagedUsers": t.boolean().optional(),
            "name": t.string().optional(),
            "customerDomainPrefix": t.string(),
            "createTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContactCenterOut"])
    types["ListLocationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
        }
    ).named(renames["ListLocationsResponseIn"])
    types["ListLocationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "locations": t.array(t.proxy(renames["LocationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLocationsResponseOut"])
    types["ListContactCentersResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "contactCenters": t.array(t.proxy(renames["ContactCenterIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListContactCentersResponseIn"])
    types["ListContactCentersResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "contactCenters": t.array(t.proxy(renames["ContactCenterOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListContactCentersResponseOut"])
    types["ListOperationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(t.proxy(renames["OperationIn"])).optional(),
        }
    ).named(renames["ListOperationsResponseIn"])
    types["ListOperationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(t.proxy(renames["OperationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListOperationsResponseOut"])
    types["OperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["StatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["URIsIn"] = t.struct(
        {
            "virtualAgentStreamingServiceUri": t.string().optional(),
            "rootUri": t.string().optional(),
            "chatBotUri": t.string().optional(),
            "mediaUri": t.string().optional(),
        }
    ).named(renames["URIsIn"])
    types["URIsOut"] = t.struct(
        {
            "virtualAgentStreamingServiceUri": t.string().optional(),
            "rootUri": t.string().optional(),
            "chatBotUri": t.string().optional(),
            "mediaUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["URIsOut"])
    types["OperationMetadataIn"] = t.struct(
        {"contactCenter": t.proxy(renames["ContactCenterIn"]).optional()}
    ).named(renames["OperationMetadataIn"])
    types["OperationMetadataOut"] = t.struct(
        {
            "verb": t.string().optional(),
            "contactCenter": t.proxy(renames["ContactCenterOut"]).optional(),
            "createTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "endTime": t.string().optional(),
            "target": t.string().optional(),
            "statusMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])

    functions = {}
    functions["projectsLocationsGet"] = contactcenteraiplatform.get(
        "v1alpha1/{name}/locations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsQueryContactCenterQuota"] = contactcenteraiplatform.get(
        "v1alpha1/{name}/locations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsList"] = contactcenteraiplatform.get(
        "v1alpha1/{name}/locations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = contactcenteraiplatform.post(
        "v1alpha1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = contactcenteraiplatform.post(
        "v1alpha1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = contactcenteraiplatform.post(
        "v1alpha1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = contactcenteraiplatform.post(
        "v1alpha1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsContactCentersGet"] = contactcenteraiplatform.patch(
        "v1alpha1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "adminUser": t.proxy(renames["AdminUserIn"]).optional(),
                "displayName": t.string(),
                "instanceConfig": t.proxy(renames["InstanceConfigIn"]).optional(),
                "userEmail": t.string().optional(),
                "samlParams": t.proxy(renames["SAMLParamsIn"]).optional(),
                "ccaipManagedUsers": t.boolean().optional(),
                "customerDomainPrefix": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsContactCentersCreate"] = contactcenteraiplatform.patch(
        "v1alpha1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "adminUser": t.proxy(renames["AdminUserIn"]).optional(),
                "displayName": t.string(),
                "instanceConfig": t.proxy(renames["InstanceConfigIn"]).optional(),
                "userEmail": t.string().optional(),
                "samlParams": t.proxy(renames["SAMLParamsIn"]).optional(),
                "ccaipManagedUsers": t.boolean().optional(),
                "customerDomainPrefix": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsContactCentersDelete"] = contactcenteraiplatform.patch(
        "v1alpha1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "adminUser": t.proxy(renames["AdminUserIn"]).optional(),
                "displayName": t.string(),
                "instanceConfig": t.proxy(renames["InstanceConfigIn"]).optional(),
                "userEmail": t.string().optional(),
                "samlParams": t.proxy(renames["SAMLParamsIn"]).optional(),
                "ccaipManagedUsers": t.boolean().optional(),
                "customerDomainPrefix": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsContactCentersList"] = contactcenteraiplatform.patch(
        "v1alpha1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "adminUser": t.proxy(renames["AdminUserIn"]).optional(),
                "displayName": t.string(),
                "instanceConfig": t.proxy(renames["InstanceConfigIn"]).optional(),
                "userEmail": t.string().optional(),
                "samlParams": t.proxy(renames["SAMLParamsIn"]).optional(),
                "ccaipManagedUsers": t.boolean().optional(),
                "customerDomainPrefix": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsContactCentersPatch"] = contactcenteraiplatform.patch(
        "v1alpha1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "adminUser": t.proxy(renames["AdminUserIn"]).optional(),
                "displayName": t.string(),
                "instanceConfig": t.proxy(renames["InstanceConfigIn"]).optional(),
                "userEmail": t.string().optional(),
                "samlParams": t.proxy(renames["SAMLParamsIn"]).optional(),
                "ccaipManagedUsers": t.boolean().optional(),
                "customerDomainPrefix": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="contactcenteraiplatform",
        renames=renames,
        types=types,
        functions=functions,
    )
