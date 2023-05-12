from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_contactcenteraiplatform() -> Import:
    contactcenteraiplatform = HTTPRuntime(
        "https://contactcenteraiplatform.googleapis.com/"
    )

    renames = {
        "ErrorResponse": "_contactcenteraiplatform_1_ErrorResponse",
        "CancelOperationRequestIn": "_contactcenteraiplatform_2_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_contactcenteraiplatform_3_CancelOperationRequestOut",
        "StatusIn": "_contactcenteraiplatform_4_StatusIn",
        "StatusOut": "_contactcenteraiplatform_5_StatusOut",
        "OperationMetadataIn": "_contactcenteraiplatform_6_OperationMetadataIn",
        "OperationMetadataOut": "_contactcenteraiplatform_7_OperationMetadataOut",
        "ListOperationsResponseIn": "_contactcenteraiplatform_8_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_contactcenteraiplatform_9_ListOperationsResponseOut",
        "ListContactCentersResponseIn": "_contactcenteraiplatform_10_ListContactCentersResponseIn",
        "ListContactCentersResponseOut": "_contactcenteraiplatform_11_ListContactCentersResponseOut",
        "QuotaIn": "_contactcenteraiplatform_12_QuotaIn",
        "QuotaOut": "_contactcenteraiplatform_13_QuotaOut",
        "SAMLParamsIn": "_contactcenteraiplatform_14_SAMLParamsIn",
        "SAMLParamsOut": "_contactcenteraiplatform_15_SAMLParamsOut",
        "LocationIn": "_contactcenteraiplatform_16_LocationIn",
        "LocationOut": "_contactcenteraiplatform_17_LocationOut",
        "AdminUserIn": "_contactcenteraiplatform_18_AdminUserIn",
        "AdminUserOut": "_contactcenteraiplatform_19_AdminUserOut",
        "URIsIn": "_contactcenteraiplatform_20_URIsIn",
        "URIsOut": "_contactcenteraiplatform_21_URIsOut",
        "ContactCenterIn": "_contactcenteraiplatform_22_ContactCenterIn",
        "ContactCenterOut": "_contactcenteraiplatform_23_ContactCenterOut",
        "OperationIn": "_contactcenteraiplatform_24_OperationIn",
        "OperationOut": "_contactcenteraiplatform_25_OperationOut",
        "ListLocationsResponseIn": "_contactcenteraiplatform_26_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_contactcenteraiplatform_27_ListLocationsResponseOut",
        "InstanceConfigIn": "_contactcenteraiplatform_28_InstanceConfigIn",
        "InstanceConfigOut": "_contactcenteraiplatform_29_InstanceConfigOut",
        "ContactCenterQuotaIn": "_contactcenteraiplatform_30_ContactCenterQuotaIn",
        "ContactCenterQuotaOut": "_contactcenteraiplatform_31_ContactCenterQuotaOut",
        "EmptyIn": "_contactcenteraiplatform_32_EmptyIn",
        "EmptyOut": "_contactcenteraiplatform_33_EmptyOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["StatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["OperationMetadataIn"] = t.struct(
        {"contactCenter": t.proxy(renames["ContactCenterIn"]).optional()}
    ).named(renames["OperationMetadataIn"])
    types["OperationMetadataOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "verb": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "statusMessage": t.string().optional(),
            "contactCenter": t.proxy(renames["ContactCenterOut"]).optional(),
            "target": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
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
    types["QuotaIn"] = t.struct(
        {
            "contactCenterInstanceSize": t.string().optional(),
            "contactCenterCountSum": t.integer().optional(),
            "contactCenterCountLimit": t.integer().optional(),
        }
    ).named(renames["QuotaIn"])
    types["QuotaOut"] = t.struct(
        {
            "contactCenterInstanceSize": t.string().optional(),
            "contactCenterCountSum": t.integer().optional(),
            "contactCenterCountLimit": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuotaOut"])
    types["SAMLParamsIn"] = t.struct(
        {
            "ssoUri": t.string().optional(),
            "certificate": t.string().optional(),
            "userEmail": t.string().optional(),
            "entityId": t.string().optional(),
        }
    ).named(renames["SAMLParamsIn"])
    types["SAMLParamsOut"] = t.struct(
        {
            "ssoUri": t.string().optional(),
            "certificate": t.string().optional(),
            "userEmail": t.string().optional(),
            "entityId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SAMLParamsOut"])
    types["LocationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["AdminUserIn"] = t.struct(
        {"familyName": t.string().optional(), "givenName": t.string().optional()}
    ).named(renames["AdminUserIn"])
    types["AdminUserOut"] = t.struct(
        {
            "familyName": t.string().optional(),
            "givenName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdminUserOut"])
    types["URIsIn"] = t.struct(
        {
            "chatBotUri": t.string().optional(),
            "rootUri": t.string().optional(),
            "mediaUri": t.string().optional(),
            "virtualAgentStreamingServiceUri": t.string().optional(),
        }
    ).named(renames["URIsIn"])
    types["URIsOut"] = t.struct(
        {
            "chatBotUri": t.string().optional(),
            "rootUri": t.string().optional(),
            "mediaUri": t.string().optional(),
            "virtualAgentStreamingServiceUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["URIsOut"])
    types["ContactCenterIn"] = t.struct(
        {
            "customerDomainPrefix": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "samlParams": t.proxy(renames["SAMLParamsIn"]).optional(),
            "ccaipManagedUsers": t.boolean().optional(),
            "adminUser": t.proxy(renames["AdminUserIn"]).optional(),
            "userEmail": t.string().optional(),
            "name": t.string().optional(),
            "instanceConfig": t.proxy(renames["InstanceConfigIn"]).optional(),
            "displayName": t.string(),
        }
    ).named(renames["ContactCenterIn"])
    types["ContactCenterOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "customerDomainPrefix": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "samlParams": t.proxy(renames["SAMLParamsOut"]).optional(),
            "ccaipManagedUsers": t.boolean().optional(),
            "createTime": t.string().optional(),
            "uris": t.proxy(renames["URIsOut"]).optional(),
            "adminUser": t.proxy(renames["AdminUserOut"]).optional(),
            "userEmail": t.string().optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "instanceConfig": t.proxy(renames["InstanceConfigOut"]).optional(),
            "displayName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContactCenterOut"])
    types["OperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["ListLocationsResponseIn"] = t.struct(
        {
            "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListLocationsResponseIn"])
    types["ListLocationsResponseOut"] = t.struct(
        {
            "locations": t.array(t.proxy(renames["LocationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLocationsResponseOut"])
    types["InstanceConfigIn"] = t.struct({"instanceSize": t.string().optional()}).named(
        renames["InstanceConfigIn"]
    )
    types["InstanceConfigOut"] = t.struct(
        {
            "instanceSize": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceConfigOut"])
    types["ContactCenterQuotaIn"] = t.struct(
        {
            "quotas": t.array(t.proxy(renames["QuotaIn"])).optional(),
            "contactCenterCountSum": t.integer().optional(),
            "contactCenterCountLimit": t.integer().optional(),
        }
    ).named(renames["ContactCenterQuotaIn"])
    types["ContactCenterQuotaOut"] = t.struct(
        {
            "quotas": t.array(t.proxy(renames["QuotaOut"])).optional(),
            "contactCenterCountSum": t.integer().optional(),
            "contactCenterCountLimit": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContactCenterQuotaOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])

    functions = {}
    functions["projectsLocationsQueryContactCenterQuota"] = contactcenteraiplatform.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsList"] = contactcenteraiplatform.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = contactcenteraiplatform.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsContactCentersPatch"] = contactcenteraiplatform.post(
        "v1alpha1/{parent}/contactCenters",
        t.struct(
            {
                "contactCenterId": t.string(),
                "requestId": t.string().optional(),
                "parent": t.string(),
                "customerDomainPrefix": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "samlParams": t.proxy(renames["SAMLParamsIn"]).optional(),
                "ccaipManagedUsers": t.boolean().optional(),
                "adminUser": t.proxy(renames["AdminUserIn"]).optional(),
                "userEmail": t.string().optional(),
                "name": t.string().optional(),
                "instanceConfig": t.proxy(renames["InstanceConfigIn"]).optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsContactCentersDelete"] = contactcenteraiplatform.post(
        "v1alpha1/{parent}/contactCenters",
        t.struct(
            {
                "contactCenterId": t.string(),
                "requestId": t.string().optional(),
                "parent": t.string(),
                "customerDomainPrefix": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "samlParams": t.proxy(renames["SAMLParamsIn"]).optional(),
                "ccaipManagedUsers": t.boolean().optional(),
                "adminUser": t.proxy(renames["AdminUserIn"]).optional(),
                "userEmail": t.string().optional(),
                "name": t.string().optional(),
                "instanceConfig": t.proxy(renames["InstanceConfigIn"]).optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsContactCentersList"] = contactcenteraiplatform.post(
        "v1alpha1/{parent}/contactCenters",
        t.struct(
            {
                "contactCenterId": t.string(),
                "requestId": t.string().optional(),
                "parent": t.string(),
                "customerDomainPrefix": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "samlParams": t.proxy(renames["SAMLParamsIn"]).optional(),
                "ccaipManagedUsers": t.boolean().optional(),
                "adminUser": t.proxy(renames["AdminUserIn"]).optional(),
                "userEmail": t.string().optional(),
                "name": t.string().optional(),
                "instanceConfig": t.proxy(renames["InstanceConfigIn"]).optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsContactCentersGet"] = contactcenteraiplatform.post(
        "v1alpha1/{parent}/contactCenters",
        t.struct(
            {
                "contactCenterId": t.string(),
                "requestId": t.string().optional(),
                "parent": t.string(),
                "customerDomainPrefix": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "samlParams": t.proxy(renames["SAMLParamsIn"]).optional(),
                "ccaipManagedUsers": t.boolean().optional(),
                "adminUser": t.proxy(renames["AdminUserIn"]).optional(),
                "userEmail": t.string().optional(),
                "name": t.string().optional(),
                "instanceConfig": t.proxy(renames["InstanceConfigIn"]).optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsContactCentersCreate"] = contactcenteraiplatform.post(
        "v1alpha1/{parent}/contactCenters",
        t.struct(
            {
                "contactCenterId": t.string(),
                "requestId": t.string().optional(),
                "parent": t.string(),
                "customerDomainPrefix": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "samlParams": t.proxy(renames["SAMLParamsIn"]).optional(),
                "ccaipManagedUsers": t.boolean().optional(),
                "adminUser": t.proxy(renames["AdminUserIn"]).optional(),
                "userEmail": t.string().optional(),
                "name": t.string().optional(),
                "instanceConfig": t.proxy(renames["InstanceConfigIn"]).optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = contactcenteraiplatform.get(
        "v1alpha1/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = contactcenteraiplatform.get(
        "v1alpha1/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = contactcenteraiplatform.get(
        "v1alpha1/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = contactcenteraiplatform.get(
        "v1alpha1/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="contactcenteraiplatform",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
