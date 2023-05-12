from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_analyticshub() -> Import:
    analyticshub = HTTPRuntime("https://analyticshub.googleapis.com/")

    renames = {
        "ErrorResponse": "_analyticshub_1_ErrorResponse",
        "SetIamPolicyRequestIn": "_analyticshub_2_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_analyticshub_3_SetIamPolicyRequestOut",
        "BindingIn": "_analyticshub_4_BindingIn",
        "BindingOut": "_analyticshub_5_BindingOut",
        "DataProviderIn": "_analyticshub_6_DataProviderIn",
        "DataProviderOut": "_analyticshub_7_DataProviderOut",
        "SubscribeListingRequestIn": "_analyticshub_8_SubscribeListingRequestIn",
        "SubscribeListingRequestOut": "_analyticshub_9_SubscribeListingRequestOut",
        "TestIamPermissionsResponseIn": "_analyticshub_10_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_analyticshub_11_TestIamPermissionsResponseOut",
        "OperationMetadataIn": "_analyticshub_12_OperationMetadataIn",
        "OperationMetadataOut": "_analyticshub_13_OperationMetadataOut",
        "GetPolicyOptionsIn": "_analyticshub_14_GetPolicyOptionsIn",
        "GetPolicyOptionsOut": "_analyticshub_15_GetPolicyOptionsOut",
        "PolicyIn": "_analyticshub_16_PolicyIn",
        "PolicyOut": "_analyticshub_17_PolicyOut",
        "ListOrgDataExchangesResponseIn": "_analyticshub_18_ListOrgDataExchangesResponseIn",
        "ListOrgDataExchangesResponseOut": "_analyticshub_19_ListOrgDataExchangesResponseOut",
        "BigQueryDatasetSourceIn": "_analyticshub_20_BigQueryDatasetSourceIn",
        "BigQueryDatasetSourceOut": "_analyticshub_21_BigQueryDatasetSourceOut",
        "TestIamPermissionsRequestIn": "_analyticshub_22_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_analyticshub_23_TestIamPermissionsRequestOut",
        "AuditConfigIn": "_analyticshub_24_AuditConfigIn",
        "AuditConfigOut": "_analyticshub_25_AuditConfigOut",
        "SubscribeListingResponseIn": "_analyticshub_26_SubscribeListingResponseIn",
        "SubscribeListingResponseOut": "_analyticshub_27_SubscribeListingResponseOut",
        "ExprIn": "_analyticshub_28_ExprIn",
        "ExprOut": "_analyticshub_29_ExprOut",
        "DataExchangeIn": "_analyticshub_30_DataExchangeIn",
        "DataExchangeOut": "_analyticshub_31_DataExchangeOut",
        "ListingIn": "_analyticshub_32_ListingIn",
        "ListingOut": "_analyticshub_33_ListingOut",
        "GetIamPolicyRequestIn": "_analyticshub_34_GetIamPolicyRequestIn",
        "GetIamPolicyRequestOut": "_analyticshub_35_GetIamPolicyRequestOut",
        "AuditLogConfigIn": "_analyticshub_36_AuditLogConfigIn",
        "AuditLogConfigOut": "_analyticshub_37_AuditLogConfigOut",
        "EmptyIn": "_analyticshub_38_EmptyIn",
        "EmptyOut": "_analyticshub_39_EmptyOut",
        "ListListingsResponseIn": "_analyticshub_40_ListListingsResponseIn",
        "ListListingsResponseOut": "_analyticshub_41_ListListingsResponseOut",
        "DestinationDatasetIn": "_analyticshub_42_DestinationDatasetIn",
        "DestinationDatasetOut": "_analyticshub_43_DestinationDatasetOut",
        "DestinationDatasetReferenceIn": "_analyticshub_44_DestinationDatasetReferenceIn",
        "DestinationDatasetReferenceOut": "_analyticshub_45_DestinationDatasetReferenceOut",
        "ListDataExchangesResponseIn": "_analyticshub_46_ListDataExchangesResponseIn",
        "ListDataExchangesResponseOut": "_analyticshub_47_ListDataExchangesResponseOut",
        "PublisherIn": "_analyticshub_48_PublisherIn",
        "PublisherOut": "_analyticshub_49_PublisherOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "policy": t.proxy(renames["PolicyIn"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
    types["BindingIn"] = t.struct(
        {
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["DataProviderIn"] = t.struct(
        {"primaryContact": t.string().optional(), "name": t.string().optional()}
    ).named(renames["DataProviderIn"])
    types["DataProviderOut"] = t.struct(
        {
            "primaryContact": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataProviderOut"])
    types["SubscribeListingRequestIn"] = t.struct(
        {"destinationDataset": t.proxy(renames["DestinationDatasetIn"]).optional()}
    ).named(renames["SubscribeListingRequestIn"])
    types["SubscribeListingRequestOut"] = t.struct(
        {
            "destinationDataset": t.proxy(renames["DestinationDatasetOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscribeListingRequestOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "statusDetail": t.string().optional(),
            "endTime": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "apiVersion": t.string().optional(),
            "target": t.string().optional(),
            "verb": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["GetPolicyOptionsIn"] = t.struct(
        {"requestedPolicyVersion": t.integer().optional()}
    ).named(renames["GetPolicyOptionsIn"])
    types["GetPolicyOptionsOut"] = t.struct(
        {
            "requestedPolicyVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetPolicyOptionsOut"])
    types["PolicyIn"] = t.struct(
        {
            "version": t.integer().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "version": t.integer().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["ListOrgDataExchangesResponseIn"] = t.struct(
        {
            "dataExchanges": t.array(t.proxy(renames["DataExchangeIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListOrgDataExchangesResponseIn"])
    types["ListOrgDataExchangesResponseOut"] = t.struct(
        {
            "dataExchanges": t.array(t.proxy(renames["DataExchangeOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListOrgDataExchangesResponseOut"])
    types["BigQueryDatasetSourceIn"] = t.struct(
        {"dataset": t.string().optional()}
    ).named(renames["BigQueryDatasetSourceIn"])
    types["BigQueryDatasetSourceOut"] = t.struct(
        {
            "dataset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BigQueryDatasetSourceOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["AuditConfigIn"] = t.struct(
        {
            "service": t.string().optional(),
            "auditLogConfigs": t.array(t.proxy(renames["AuditLogConfigIn"])).optional(),
        }
    ).named(renames["AuditConfigIn"])
    types["AuditConfigOut"] = t.struct(
        {
            "service": t.string().optional(),
            "auditLogConfigs": t.array(
                t.proxy(renames["AuditLogConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditConfigOut"])
    types["SubscribeListingResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["SubscribeListingResponseIn"]
    )
    types["SubscribeListingResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SubscribeListingResponseOut"])
    types["ExprIn"] = t.struct(
        {
            "location": t.string().optional(),
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "location": t.string().optional(),
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["DataExchangeIn"] = t.struct(
        {
            "displayName": t.string(),
            "description": t.string().optional(),
            "primaryContact": t.string().optional(),
            "icon": t.string().optional(),
            "documentation": t.string().optional(),
        }
    ).named(renames["DataExchangeIn"])
    types["DataExchangeOut"] = t.struct(
        {
            "displayName": t.string(),
            "description": t.string().optional(),
            "primaryContact": t.string().optional(),
            "listingCount": t.integer().optional(),
            "name": t.string().optional(),
            "icon": t.string().optional(),
            "documentation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataExchangeOut"])
    types["ListingIn"] = t.struct(
        {
            "categories": t.array(t.string()).optional(),
            "primaryContact": t.string().optional(),
            "documentation": t.string().optional(),
            "displayName": t.string(),
            "description": t.string().optional(),
            "requestAccess": t.string().optional(),
            "dataProvider": t.proxy(renames["DataProviderIn"]).optional(),
            "icon": t.string().optional(),
            "bigqueryDataset": t.proxy(renames["BigQueryDatasetSourceIn"]),
            "publisher": t.proxy(renames["PublisherIn"]).optional(),
        }
    ).named(renames["ListingIn"])
    types["ListingOut"] = t.struct(
        {
            "categories": t.array(t.string()).optional(),
            "state": t.string().optional(),
            "primaryContact": t.string().optional(),
            "name": t.string().optional(),
            "documentation": t.string().optional(),
            "displayName": t.string(),
            "description": t.string().optional(),
            "requestAccess": t.string().optional(),
            "dataProvider": t.proxy(renames["DataProviderOut"]).optional(),
            "icon": t.string().optional(),
            "bigqueryDataset": t.proxy(renames["BigQueryDatasetSourceOut"]),
            "publisher": t.proxy(renames["PublisherOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListingOut"])
    types["GetIamPolicyRequestIn"] = t.struct(
        {"options": t.proxy(renames["GetPolicyOptionsIn"]).optional()}
    ).named(renames["GetIamPolicyRequestIn"])
    types["GetIamPolicyRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["GetPolicyOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIamPolicyRequestOut"])
    types["AuditLogConfigIn"] = t.struct(
        {
            "exemptedMembers": t.array(t.string()).optional(),
            "logType": t.string().optional(),
        }
    ).named(renames["AuditLogConfigIn"])
    types["AuditLogConfigOut"] = t.struct(
        {
            "exemptedMembers": t.array(t.string()).optional(),
            "logType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditLogConfigOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ListListingsResponseIn"] = t.struct(
        {
            "listings": t.array(t.proxy(renames["ListingIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListListingsResponseIn"])
    types["ListListingsResponseOut"] = t.struct(
        {
            "listings": t.array(t.proxy(renames["ListingOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListListingsResponseOut"])
    types["DestinationDatasetIn"] = t.struct(
        {
            "friendlyName": t.string().optional(),
            "description": t.string().optional(),
            "location": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "datasetReference": t.proxy(renames["DestinationDatasetReferenceIn"]),
        }
    ).named(renames["DestinationDatasetIn"])
    types["DestinationDatasetOut"] = t.struct(
        {
            "friendlyName": t.string().optional(),
            "description": t.string().optional(),
            "location": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "datasetReference": t.proxy(renames["DestinationDatasetReferenceOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DestinationDatasetOut"])
    types["DestinationDatasetReferenceIn"] = t.struct(
        {"datasetId": t.string(), "projectId": t.string()}
    ).named(renames["DestinationDatasetReferenceIn"])
    types["DestinationDatasetReferenceOut"] = t.struct(
        {
            "datasetId": t.string(),
            "projectId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DestinationDatasetReferenceOut"])
    types["ListDataExchangesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "dataExchanges": t.array(t.proxy(renames["DataExchangeIn"])).optional(),
        }
    ).named(renames["ListDataExchangesResponseIn"])
    types["ListDataExchangesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "dataExchanges": t.array(t.proxy(renames["DataExchangeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDataExchangesResponseOut"])
    types["PublisherIn"] = t.struct(
        {"name": t.string().optional(), "primaryContact": t.string().optional()}
    ).named(renames["PublisherIn"])
    types["PublisherOut"] = t.struct(
        {
            "name": t.string().optional(),
            "primaryContact": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublisherOut"])

    functions = {}
    functions["organizationsLocationsDataExchangesList"] = analyticshub.get(
        "v1/{organization}/dataExchanges",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "organization": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOrgDataExchangesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataExchangesList"] = analyticshub.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataExchangesPatch"] = analyticshub.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataExchangesCreate"] = analyticshub.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataExchangesSetIamPolicy"] = analyticshub.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataExchangesDelete"] = analyticshub.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataExchangesGet"] = analyticshub.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataExchangesGetIamPolicy"] = analyticshub.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataExchangesTestIamPermissions"] = analyticshub.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataExchangesListingsSetIamPolicy"] = analyticshub.get(
        "v1/{parent}/listings",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListListingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataExchangesListingsSubscribe"] = analyticshub.get(
        "v1/{parent}/listings",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListListingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataExchangesListingsPatch"] = analyticshub.get(
        "v1/{parent}/listings",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListListingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataExchangesListingsGetIamPolicy"] = analyticshub.get(
        "v1/{parent}/listings",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListListingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDataExchangesListingsTestIamPermissions"
    ] = analyticshub.get(
        "v1/{parent}/listings",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListListingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataExchangesListingsDelete"] = analyticshub.get(
        "v1/{parent}/listings",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListListingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataExchangesListingsCreate"] = analyticshub.get(
        "v1/{parent}/listings",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListListingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataExchangesListingsGet"] = analyticshub.get(
        "v1/{parent}/listings",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListListingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataExchangesListingsList"] = analyticshub.get(
        "v1/{parent}/listings",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListListingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="analyticshub",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
