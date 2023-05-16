from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_analyticshub() -> Import:
    analyticshub = HTTPRuntime("https://analyticshub.googleapis.com/")

    renames = {
        "ErrorResponse": "_analyticshub_1_ErrorResponse",
        "ListingIn": "_analyticshub_2_ListingIn",
        "ListingOut": "_analyticshub_3_ListingOut",
        "ListListingsResponseIn": "_analyticshub_4_ListListingsResponseIn",
        "ListListingsResponseOut": "_analyticshub_5_ListListingsResponseOut",
        "DestinationDatasetIn": "_analyticshub_6_DestinationDatasetIn",
        "DestinationDatasetOut": "_analyticshub_7_DestinationDatasetOut",
        "PolicyIn": "_analyticshub_8_PolicyIn",
        "PolicyOut": "_analyticshub_9_PolicyOut",
        "SubscribeListingResponseIn": "_analyticshub_10_SubscribeListingResponseIn",
        "SubscribeListingResponseOut": "_analyticshub_11_SubscribeListingResponseOut",
        "TestIamPermissionsResponseIn": "_analyticshub_12_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_analyticshub_13_TestIamPermissionsResponseOut",
        "ListDataExchangesResponseIn": "_analyticshub_14_ListDataExchangesResponseIn",
        "ListDataExchangesResponseOut": "_analyticshub_15_ListDataExchangesResponseOut",
        "BigQueryDatasetSourceIn": "_analyticshub_16_BigQueryDatasetSourceIn",
        "BigQueryDatasetSourceOut": "_analyticshub_17_BigQueryDatasetSourceOut",
        "GetPolicyOptionsIn": "_analyticshub_18_GetPolicyOptionsIn",
        "GetPolicyOptionsOut": "_analyticshub_19_GetPolicyOptionsOut",
        "PublisherIn": "_analyticshub_20_PublisherIn",
        "PublisherOut": "_analyticshub_21_PublisherOut",
        "EmptyIn": "_analyticshub_22_EmptyIn",
        "EmptyOut": "_analyticshub_23_EmptyOut",
        "DataExchangeIn": "_analyticshub_24_DataExchangeIn",
        "DataExchangeOut": "_analyticshub_25_DataExchangeOut",
        "ExprIn": "_analyticshub_26_ExprIn",
        "ExprOut": "_analyticshub_27_ExprOut",
        "ListOrgDataExchangesResponseIn": "_analyticshub_28_ListOrgDataExchangesResponseIn",
        "ListOrgDataExchangesResponseOut": "_analyticshub_29_ListOrgDataExchangesResponseOut",
        "AuditConfigIn": "_analyticshub_30_AuditConfigIn",
        "AuditConfigOut": "_analyticshub_31_AuditConfigOut",
        "AuditLogConfigIn": "_analyticshub_32_AuditLogConfigIn",
        "AuditLogConfigOut": "_analyticshub_33_AuditLogConfigOut",
        "GetIamPolicyRequestIn": "_analyticshub_34_GetIamPolicyRequestIn",
        "GetIamPolicyRequestOut": "_analyticshub_35_GetIamPolicyRequestOut",
        "OperationMetadataIn": "_analyticshub_36_OperationMetadataIn",
        "OperationMetadataOut": "_analyticshub_37_OperationMetadataOut",
        "SubscribeListingRequestIn": "_analyticshub_38_SubscribeListingRequestIn",
        "SubscribeListingRequestOut": "_analyticshub_39_SubscribeListingRequestOut",
        "DataProviderIn": "_analyticshub_40_DataProviderIn",
        "DataProviderOut": "_analyticshub_41_DataProviderOut",
        "BindingIn": "_analyticshub_42_BindingIn",
        "BindingOut": "_analyticshub_43_BindingOut",
        "SetIamPolicyRequestIn": "_analyticshub_44_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_analyticshub_45_SetIamPolicyRequestOut",
        "TestIamPermissionsRequestIn": "_analyticshub_46_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_analyticshub_47_TestIamPermissionsRequestOut",
        "DestinationDatasetReferenceIn": "_analyticshub_48_DestinationDatasetReferenceIn",
        "DestinationDatasetReferenceOut": "_analyticshub_49_DestinationDatasetReferenceOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ListingIn"] = t.struct(
        {
            "dataProvider": t.proxy(renames["DataProviderIn"]).optional(),
            "description": t.string().optional(),
            "displayName": t.string(),
            "primaryContact": t.string().optional(),
            "publisher": t.proxy(renames["PublisherIn"]).optional(),
            "requestAccess": t.string().optional(),
            "bigqueryDataset": t.proxy(renames["BigQueryDatasetSourceIn"]),
            "categories": t.array(t.string()).optional(),
            "documentation": t.string().optional(),
            "icon": t.string().optional(),
        }
    ).named(renames["ListingIn"])
    types["ListingOut"] = t.struct(
        {
            "dataProvider": t.proxy(renames["DataProviderOut"]).optional(),
            "description": t.string().optional(),
            "state": t.string().optional(),
            "displayName": t.string(),
            "primaryContact": t.string().optional(),
            "publisher": t.proxy(renames["PublisherOut"]).optional(),
            "requestAccess": t.string().optional(),
            "bigqueryDataset": t.proxy(renames["BigQueryDatasetSourceOut"]),
            "name": t.string().optional(),
            "categories": t.array(t.string()).optional(),
            "documentation": t.string().optional(),
            "icon": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListingOut"])
    types["ListListingsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "listings": t.array(t.proxy(renames["ListingIn"])).optional(),
        }
    ).named(renames["ListListingsResponseIn"])
    types["ListListingsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "listings": t.array(t.proxy(renames["ListingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListListingsResponseOut"])
    types["DestinationDatasetIn"] = t.struct(
        {
            "location": t.string(),
            "description": t.string().optional(),
            "datasetReference": t.proxy(renames["DestinationDatasetReferenceIn"]),
            "friendlyName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["DestinationDatasetIn"])
    types["DestinationDatasetOut"] = t.struct(
        {
            "location": t.string(),
            "description": t.string().optional(),
            "datasetReference": t.proxy(renames["DestinationDatasetReferenceOut"]),
            "friendlyName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DestinationDatasetOut"])
    types["PolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["SubscribeListingResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["SubscribeListingResponseIn"]
    )
    types["SubscribeListingResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SubscribeListingResponseOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
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
    types["BigQueryDatasetSourceIn"] = t.struct(
        {"dataset": t.string().optional()}
    ).named(renames["BigQueryDatasetSourceIn"])
    types["BigQueryDatasetSourceOut"] = t.struct(
        {
            "dataset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BigQueryDatasetSourceOut"])
    types["GetPolicyOptionsIn"] = t.struct(
        {"requestedPolicyVersion": t.integer().optional()}
    ).named(renames["GetPolicyOptionsIn"])
    types["GetPolicyOptionsOut"] = t.struct(
        {
            "requestedPolicyVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetPolicyOptionsOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["DataExchangeIn"] = t.struct(
        {
            "displayName": t.string(),
            "documentation": t.string().optional(),
            "description": t.string().optional(),
            "icon": t.string().optional(),
            "primaryContact": t.string().optional(),
        }
    ).named(renames["DataExchangeIn"])
    types["DataExchangeOut"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string(),
            "documentation": t.string().optional(),
            "description": t.string().optional(),
            "listingCount": t.integer().optional(),
            "icon": t.string().optional(),
            "primaryContact": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataExchangeOut"])
    types["ExprIn"] = t.struct(
        {
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
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
    types["AuditLogConfigIn"] = t.struct(
        {
            "logType": t.string().optional(),
            "exemptedMembers": t.array(t.string()).optional(),
        }
    ).named(renames["AuditLogConfigIn"])
    types["AuditLogConfigOut"] = t.struct(
        {
            "logType": t.string().optional(),
            "exemptedMembers": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditLogConfigOut"])
    types["GetIamPolicyRequestIn"] = t.struct(
        {"options": t.proxy(renames["GetPolicyOptionsIn"]).optional()}
    ).named(renames["GetIamPolicyRequestIn"])
    types["GetIamPolicyRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["GetPolicyOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIamPolicyRequestOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "target": t.string().optional(),
            "createTime": t.string().optional(),
            "endTime": t.string().optional(),
            "verb": t.string().optional(),
            "statusDetail": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "apiVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["SubscribeListingRequestIn"] = t.struct(
        {"destinationDataset": t.proxy(renames["DestinationDatasetIn"]).optional()}
    ).named(renames["SubscribeListingRequestIn"])
    types["SubscribeListingRequestOut"] = t.struct(
        {
            "destinationDataset": t.proxy(renames["DestinationDatasetOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscribeListingRequestOut"])
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
    types["BindingIn"] = t.struct(
        {
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "members": t.array(t.string()).optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "members": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
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
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
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

    functions = {}
    functions["projectsLocationsDataExchangesGetIamPolicy"] = analyticshub.get(
        "v1/{parent}/dataExchanges",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDataExchangesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataExchangesGet"] = analyticshub.get(
        "v1/{parent}/dataExchanges",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDataExchangesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataExchangesCreate"] = analyticshub.get(
        "v1/{parent}/dataExchanges",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDataExchangesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataExchangesPatch"] = analyticshub.get(
        "v1/{parent}/dataExchanges",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDataExchangesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataExchangesSetIamPolicy"] = analyticshub.get(
        "v1/{parent}/dataExchanges",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDataExchangesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataExchangesDelete"] = analyticshub.get(
        "v1/{parent}/dataExchanges",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDataExchangesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataExchangesTestIamPermissions"] = analyticshub.get(
        "v1/{parent}/dataExchanges",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDataExchangesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataExchangesList"] = analyticshub.get(
        "v1/{parent}/dataExchanges",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDataExchangesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataExchangesListingsGetIamPolicy"] = analyticshub.get(
        "v1/{parent}/listings",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListListingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataExchangesListingsSetIamPolicy"] = analyticshub.get(
        "v1/{parent}/listings",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListListingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsDataExchangesList"] = analyticshub.get(
        "v1/{organization}/dataExchanges",
        t.struct(
            {
                "organization": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOrgDataExchangesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="analyticshub",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
