from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_contactcenteraiplatform() -> Import:
    contactcenteraiplatform = HTTPRuntime(
        "https://contactcenteraiplatform.googleapis.com/"
    )

    renames = {
        "ErrorResponse": "_contactcenteraiplatform_1_ErrorResponse",
        "SAMLParamsIn": "_contactcenteraiplatform_2_SAMLParamsIn",
        "SAMLParamsOut": "_contactcenteraiplatform_3_SAMLParamsOut",
        "StatusIn": "_contactcenteraiplatform_4_StatusIn",
        "StatusOut": "_contactcenteraiplatform_5_StatusOut",
        "URIsIn": "_contactcenteraiplatform_6_URIsIn",
        "URIsOut": "_contactcenteraiplatform_7_URIsOut",
        "InstanceConfigIn": "_contactcenteraiplatform_8_InstanceConfigIn",
        "InstanceConfigOut": "_contactcenteraiplatform_9_InstanceConfigOut",
        "ContactCenterIn": "_contactcenteraiplatform_10_ContactCenterIn",
        "ContactCenterOut": "_contactcenteraiplatform_11_ContactCenterOut",
        "ListLocationsResponseIn": "_contactcenteraiplatform_12_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_contactcenteraiplatform_13_ListLocationsResponseOut",
        "LocationIn": "_contactcenteraiplatform_14_LocationIn",
        "LocationOut": "_contactcenteraiplatform_15_LocationOut",
        "OperationIn": "_contactcenteraiplatform_16_OperationIn",
        "OperationOut": "_contactcenteraiplatform_17_OperationOut",
        "EmptyIn": "_contactcenteraiplatform_18_EmptyIn",
        "EmptyOut": "_contactcenteraiplatform_19_EmptyOut",
        "AdminUserIn": "_contactcenteraiplatform_20_AdminUserIn",
        "AdminUserOut": "_contactcenteraiplatform_21_AdminUserOut",
        "OperationMetadataIn": "_contactcenteraiplatform_22_OperationMetadataIn",
        "OperationMetadataOut": "_contactcenteraiplatform_23_OperationMetadataOut",
        "CancelOperationRequestIn": "_contactcenteraiplatform_24_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_contactcenteraiplatform_25_CancelOperationRequestOut",
        "QuotaIn": "_contactcenteraiplatform_26_QuotaIn",
        "QuotaOut": "_contactcenteraiplatform_27_QuotaOut",
        "ListOperationsResponseIn": "_contactcenteraiplatform_28_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_contactcenteraiplatform_29_ListOperationsResponseOut",
        "ContactCenterQuotaIn": "_contactcenteraiplatform_30_ContactCenterQuotaIn",
        "ContactCenterQuotaOut": "_contactcenteraiplatform_31_ContactCenterQuotaOut",
        "ListContactCentersResponseIn": "_contactcenteraiplatform_32_ListContactCentersResponseIn",
        "ListContactCentersResponseOut": "_contactcenteraiplatform_33_ListContactCentersResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["SAMLParamsIn"] = t.struct(
        {
            "certificate": t.string().optional(),
            "ssoUri": t.string().optional(),
            "userEmail": t.string().optional(),
            "entityId": t.string().optional(),
        }
    ).named(renames["SAMLParamsIn"])
    types["SAMLParamsOut"] = t.struct(
        {
            "certificate": t.string().optional(),
            "ssoUri": t.string().optional(),
            "userEmail": t.string().optional(),
            "entityId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SAMLParamsOut"])
    types["StatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
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
    types["InstanceConfigIn"] = t.struct({"instanceSize": t.string().optional()}).named(
        renames["InstanceConfigIn"]
    )
    types["InstanceConfigOut"] = t.struct(
        {
            "instanceSize": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceConfigOut"])
    types["ContactCenterIn"] = t.struct(
        {
            "adminUser": t.proxy(renames["AdminUserIn"]).optional(),
            "customerDomainPrefix": t.string(),
            "displayName": t.string(),
            "ccaipManagedUsers": t.boolean().optional(),
            "samlParams": t.proxy(renames["SAMLParamsIn"]).optional(),
            "instanceConfig": t.proxy(renames["InstanceConfigIn"]).optional(),
            "userEmail": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ContactCenterIn"])
    types["ContactCenterOut"] = t.struct(
        {
            "adminUser": t.proxy(renames["AdminUserOut"]).optional(),
            "customerDomainPrefix": t.string(),
            "displayName": t.string(),
            "uris": t.proxy(renames["URIsOut"]).optional(),
            "ccaipManagedUsers": t.boolean().optional(),
            "samlParams": t.proxy(renames["SAMLParamsOut"]).optional(),
            "updateTime": t.string().optional(),
            "instanceConfig": t.proxy(renames["InstanceConfigOut"]).optional(),
            "userEmail": t.string().optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
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
    types["LocationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["OperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["OperationMetadataIn"] = t.struct(
        {"contactCenter": t.proxy(renames["ContactCenterIn"]).optional()}
    ).named(renames["OperationMetadataIn"])
    types["OperationMetadataOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "apiVersion": t.string().optional(),
            "verb": t.string().optional(),
            "createTime": t.string().optional(),
            "statusMessage": t.string().optional(),
            "target": t.string().optional(),
            "contactCenter": t.proxy(renames["ContactCenterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["QuotaIn"] = t.struct(
        {
            "contactCenterCountSum": t.integer().optional(),
            "contactCenterCountLimit": t.integer().optional(),
            "contactCenterInstanceSize": t.string().optional(),
        }
    ).named(renames["QuotaIn"])
    types["QuotaOut"] = t.struct(
        {
            "contactCenterCountSum": t.integer().optional(),
            "contactCenterCountLimit": t.integer().optional(),
            "contactCenterInstanceSize": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuotaOut"])
    types["ListOperationsResponseIn"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["OperationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListOperationsResponseIn"])
    types["ListOperationsResponseOut"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["OperationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListOperationsResponseOut"])
    types["ContactCenterQuotaIn"] = t.struct(
        {
            "contactCenterCountSum": t.integer().optional(),
            "quotas": t.array(t.proxy(renames["QuotaIn"])).optional(),
            "contactCenterCountLimit": t.integer().optional(),
        }
    ).named(renames["ContactCenterQuotaIn"])
    types["ContactCenterQuotaOut"] = t.struct(
        {
            "contactCenterCountSum": t.integer().optional(),
            "quotas": t.array(t.proxy(renames["QuotaOut"])).optional(),
            "contactCenterCountLimit": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContactCenterQuotaOut"])
    types["ListContactCentersResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "contactCenters": t.array(t.proxy(renames["ContactCenterIn"])).optional(),
        }
    ).named(renames["ListContactCentersResponseIn"])
    types["ListContactCentersResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "contactCenters": t.array(t.proxy(renames["ContactCenterOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListContactCentersResponseOut"])

    functions = {}
    functions["projectsLocationsList"] = contactcenteraiplatform.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsQueryContactCenterQuota"] = contactcenteraiplatform.get(
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
    functions["projectsLocationsContactCentersDelete"] = contactcenteraiplatform.post(
        "v1alpha1/{parent}/contactCenters",
        t.struct(
            {
                "requestId": t.string().optional(),
                "contactCenterId": t.string(),
                "parent": t.string(),
                "adminUser": t.proxy(renames["AdminUserIn"]).optional(),
                "customerDomainPrefix": t.string(),
                "displayName": t.string(),
                "ccaipManagedUsers": t.boolean().optional(),
                "samlParams": t.proxy(renames["SAMLParamsIn"]).optional(),
                "instanceConfig": t.proxy(renames["InstanceConfigIn"]).optional(),
                "userEmail": t.string().optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
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
                "requestId": t.string().optional(),
                "contactCenterId": t.string(),
                "parent": t.string(),
                "adminUser": t.proxy(renames["AdminUserIn"]).optional(),
                "customerDomainPrefix": t.string(),
                "displayName": t.string(),
                "ccaipManagedUsers": t.boolean().optional(),
                "samlParams": t.proxy(renames["SAMLParamsIn"]).optional(),
                "instanceConfig": t.proxy(renames["InstanceConfigIn"]).optional(),
                "userEmail": t.string().optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsContactCentersPatch"] = contactcenteraiplatform.post(
        "v1alpha1/{parent}/contactCenters",
        t.struct(
            {
                "requestId": t.string().optional(),
                "contactCenterId": t.string(),
                "parent": t.string(),
                "adminUser": t.proxy(renames["AdminUserIn"]).optional(),
                "customerDomainPrefix": t.string(),
                "displayName": t.string(),
                "ccaipManagedUsers": t.boolean().optional(),
                "samlParams": t.proxy(renames["SAMLParamsIn"]).optional(),
                "instanceConfig": t.proxy(renames["InstanceConfigIn"]).optional(),
                "userEmail": t.string().optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
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
                "requestId": t.string().optional(),
                "contactCenterId": t.string(),
                "parent": t.string(),
                "adminUser": t.proxy(renames["AdminUserIn"]).optional(),
                "customerDomainPrefix": t.string(),
                "displayName": t.string(),
                "ccaipManagedUsers": t.boolean().optional(),
                "samlParams": t.proxy(renames["SAMLParamsIn"]).optional(),
                "instanceConfig": t.proxy(renames["InstanceConfigIn"]).optional(),
                "userEmail": t.string().optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
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
                "requestId": t.string().optional(),
                "contactCenterId": t.string(),
                "parent": t.string(),
                "adminUser": t.proxy(renames["AdminUserIn"]).optional(),
                "customerDomainPrefix": t.string(),
                "displayName": t.string(),
                "ccaipManagedUsers": t.boolean().optional(),
                "samlParams": t.proxy(renames["SAMLParamsIn"]).optional(),
                "instanceConfig": t.proxy(renames["InstanceConfigIn"]).optional(),
                "userEmail": t.string().optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
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

    return Import(
        importer="contactcenteraiplatform",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
