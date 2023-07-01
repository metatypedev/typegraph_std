from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_contactcenteraiplatform():
    contactcenteraiplatform = HTTPRuntime(
        "https://contactcenteraiplatform.googleapis.com/"
    )

    renames = {
        "ErrorResponse": "_contactcenteraiplatform_1_ErrorResponse",
        "QuotaIn": "_contactcenteraiplatform_2_QuotaIn",
        "QuotaOut": "_contactcenteraiplatform_3_QuotaOut",
        "CancelOperationRequestIn": "_contactcenteraiplatform_4_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_contactcenteraiplatform_5_CancelOperationRequestOut",
        "OperationIn": "_contactcenteraiplatform_6_OperationIn",
        "OperationOut": "_contactcenteraiplatform_7_OperationOut",
        "URIsIn": "_contactcenteraiplatform_8_URIsIn",
        "URIsOut": "_contactcenteraiplatform_9_URIsOut",
        "LocationIn": "_contactcenteraiplatform_10_LocationIn",
        "LocationOut": "_contactcenteraiplatform_11_LocationOut",
        "ListOperationsResponseIn": "_contactcenteraiplatform_12_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_contactcenteraiplatform_13_ListOperationsResponseOut",
        "EmptyIn": "_contactcenteraiplatform_14_EmptyIn",
        "EmptyOut": "_contactcenteraiplatform_15_EmptyOut",
        "ContactCenterQuotaIn": "_contactcenteraiplatform_16_ContactCenterQuotaIn",
        "ContactCenterQuotaOut": "_contactcenteraiplatform_17_ContactCenterQuotaOut",
        "BasicAuthConfigIn": "_contactcenteraiplatform_18_BasicAuthConfigIn",
        "BasicAuthConfigOut": "_contactcenteraiplatform_19_BasicAuthConfigOut",
        "SAMLParamsIn": "_contactcenteraiplatform_20_SAMLParamsIn",
        "SAMLParamsOut": "_contactcenteraiplatform_21_SAMLParamsOut",
        "ContactCenterIn": "_contactcenteraiplatform_22_ContactCenterIn",
        "ContactCenterOut": "_contactcenteraiplatform_23_ContactCenterOut",
        "ListContactCentersResponseIn": "_contactcenteraiplatform_24_ListContactCentersResponseIn",
        "ListContactCentersResponseOut": "_contactcenteraiplatform_25_ListContactCentersResponseOut",
        "InstanceConfigIn": "_contactcenteraiplatform_26_InstanceConfigIn",
        "InstanceConfigOut": "_contactcenteraiplatform_27_InstanceConfigOut",
        "ListLocationsResponseIn": "_contactcenteraiplatform_28_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_contactcenteraiplatform_29_ListLocationsResponseOut",
        "SamlConfigIn": "_contactcenteraiplatform_30_SamlConfigIn",
        "SamlConfigOut": "_contactcenteraiplatform_31_SamlConfigOut",
        "AuthenticationConfigIn": "_contactcenteraiplatform_32_AuthenticationConfigIn",
        "AuthenticationConfigOut": "_contactcenteraiplatform_33_AuthenticationConfigOut",
        "StatusIn": "_contactcenteraiplatform_34_StatusIn",
        "StatusOut": "_contactcenteraiplatform_35_StatusOut",
        "OperationMetadataIn": "_contactcenteraiplatform_36_OperationMetadataIn",
        "OperationMetadataOut": "_contactcenteraiplatform_37_OperationMetadataOut",
        "AdminUserIn": "_contactcenteraiplatform_38_AdminUserIn",
        "AdminUserOut": "_contactcenteraiplatform_39_AdminUserOut",
        "GoogleCloudCommonOperationMetadataIn": "_contactcenteraiplatform_40_GoogleCloudCommonOperationMetadataIn",
        "GoogleCloudCommonOperationMetadataOut": "_contactcenteraiplatform_41_GoogleCloudCommonOperationMetadataOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["OperationIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationOut"])
    types["URIsIn"] = t.struct(
        {
            "rootUri": t.string().optional(),
            "mediaUri": t.string().optional(),
            "chatBotUri": t.string().optional(),
            "virtualAgentStreamingServiceUri": t.string().optional(),
        }
    ).named(renames["URIsIn"])
    types["URIsOut"] = t.struct(
        {
            "rootUri": t.string().optional(),
            "mediaUri": t.string().optional(),
            "chatBotUri": t.string().optional(),
            "virtualAgentStreamingServiceUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["URIsOut"])
    types["LocationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["BasicAuthConfigIn"] = t.struct({"enabled": t.boolean()}).named(
        renames["BasicAuthConfigIn"]
    )
    types["BasicAuthConfigOut"] = t.struct(
        {"enabled": t.boolean(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["BasicAuthConfigOut"])
    types["SAMLParamsIn"] = t.struct(
        {
            "userEmail": t.string().optional(),
            "ssoUri": t.string().optional(),
            "certificate": t.string().optional(),
            "entityId": t.string().optional(),
        }
    ).named(renames["SAMLParamsIn"])
    types["SAMLParamsOut"] = t.struct(
        {
            "userEmail": t.string().optional(),
            "ssoUri": t.string().optional(),
            "certificate": t.string().optional(),
            "entityId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SAMLParamsOut"])
    types["ContactCenterIn"] = t.struct(
        {
            "instanceConfig": t.proxy(renames["InstanceConfigIn"]).optional(),
            "adminUser": t.proxy(renames["AdminUserIn"]).optional(),
            "displayName": t.string(),
            "kmsKey": t.string().optional(),
            "samlParams": t.proxy(renames["SAMLParamsIn"]).optional(),
            "name": t.string().optional(),
            "ccaipManagedUsers": t.boolean().optional(),
            "customerDomainPrefix": t.string(),
            "userEmail": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ContactCenterIn"])
    types["ContactCenterOut"] = t.struct(
        {
            "instanceConfig": t.proxy(renames["InstanceConfigOut"]).optional(),
            "state": t.string().optional(),
            "adminUser": t.proxy(renames["AdminUserOut"]).optional(),
            "uris": t.proxy(renames["URIsOut"]).optional(),
            "updateTime": t.string().optional(),
            "displayName": t.string(),
            "kmsKey": t.string().optional(),
            "samlParams": t.proxy(renames["SAMLParamsOut"]).optional(),
            "name": t.string().optional(),
            "ccaipManagedUsers": t.boolean().optional(),
            "customerDomainPrefix": t.string(),
            "userEmail": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContactCenterOut"])
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
    types["InstanceConfigIn"] = t.struct({"instanceSize": t.string().optional()}).named(
        renames["InstanceConfigIn"]
    )
    types["InstanceConfigOut"] = t.struct(
        {
            "instanceSize": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceConfigOut"])
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
    types["SamlConfigIn"] = t.struct(
        {
            "entityId": t.string().optional(),
            "cert": t.string().optional(),
            "loginUri": t.string().optional(),
            "emailMapping": t.string().optional(),
        }
    ).named(renames["SamlConfigIn"])
    types["SamlConfigOut"] = t.struct(
        {
            "entityId": t.string().optional(),
            "cert": t.string().optional(),
            "loginUri": t.string().optional(),
            "emailMapping": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SamlConfigOut"])
    types["AuthenticationConfigIn"] = t.struct(
        {
            "basicAuthSetting": t.proxy(renames["BasicAuthConfigIn"]),
            "samlSetting": t.proxy(renames["SamlConfigIn"]),
            "name": t.string().optional(),
        }
    ).named(renames["AuthenticationConfigIn"])
    types["AuthenticationConfigOut"] = t.struct(
        {
            "basicAuthSetting": t.proxy(renames["BasicAuthConfigOut"]),
            "samlSetting": t.proxy(renames["SamlConfigOut"]),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthenticationConfigOut"])
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
    types["OperationMetadataIn"] = t.struct(
        {"contactCenter": t.proxy(renames["ContactCenterIn"]).optional()}
    ).named(renames["OperationMetadataIn"])
    types["OperationMetadataOut"] = t.struct(
        {
            "statusMessage": t.string().optional(),
            "createTime": t.string().optional(),
            "endTime": t.string().optional(),
            "verb": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "target": t.string().optional(),
            "contactCenter": t.proxy(renames["ContactCenterOut"]).optional(),
            "apiVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
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
    types["GoogleCloudCommonOperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudCommonOperationMetadataIn"])
    types["GoogleCloudCommonOperationMetadataOut"] = t.struct(
        {
            "apiVersion": t.string().optional(),
            "statusDetail": t.string().optional(),
            "target": t.string().optional(),
            "createTime": t.string().optional(),
            "endTime": t.string().optional(),
            "verb": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudCommonOperationMetadataOut"])

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
    functions["projectsLocationsContactCentersGet"] = contactcenteraiplatform.get(
        "v1alpha1/{parent}/contactCenters",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListContactCentersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsContactCentersPatch"] = contactcenteraiplatform.get(
        "v1alpha1/{parent}/contactCenters",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListContactCentersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsContactCentersUpdateAuthentication_config"
    ] = contactcenteraiplatform.get(
        "v1alpha1/{parent}/contactCenters",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListContactCentersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsContactCentersCreate"] = contactcenteraiplatform.get(
        "v1alpha1/{parent}/contactCenters",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListContactCentersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsContactCentersDelete"] = contactcenteraiplatform.get(
        "v1alpha1/{parent}/contactCenters",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListContactCentersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsContactCentersGetAuthentication_config"
    ] = contactcenteraiplatform.get(
        "v1alpha1/{parent}/contactCenters",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListContactCentersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsContactCentersList"] = contactcenteraiplatform.get(
        "v1alpha1/{parent}/contactCenters",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListContactCentersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="contactcenteraiplatform",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
