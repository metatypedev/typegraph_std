from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_analyticshub() -> Import:
    analyticshub = HTTPRuntime("https://analyticshub.googleapis.com/")

    renames = {
        "ErrorResponse": "_analyticshub_1_ErrorResponse",
        "SetIamPolicyRequestIn": "_analyticshub_2_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_analyticshub_3_SetIamPolicyRequestOut",
        "ListOrgDataExchangesResponseIn": "_analyticshub_4_ListOrgDataExchangesResponseIn",
        "ListOrgDataExchangesResponseOut": "_analyticshub_5_ListOrgDataExchangesResponseOut",
        "DestinationDatasetReferenceIn": "_analyticshub_6_DestinationDatasetReferenceIn",
        "DestinationDatasetReferenceOut": "_analyticshub_7_DestinationDatasetReferenceOut",
        "AuditLogConfigIn": "_analyticshub_8_AuditLogConfigIn",
        "AuditLogConfigOut": "_analyticshub_9_AuditLogConfigOut",
        "OperationMetadataIn": "_analyticshub_10_OperationMetadataIn",
        "OperationMetadataOut": "_analyticshub_11_OperationMetadataOut",
        "DataProviderIn": "_analyticshub_12_DataProviderIn",
        "DataProviderOut": "_analyticshub_13_DataProviderOut",
        "GetIamPolicyRequestIn": "_analyticshub_14_GetIamPolicyRequestIn",
        "GetIamPolicyRequestOut": "_analyticshub_15_GetIamPolicyRequestOut",
        "ListingIn": "_analyticshub_16_ListingIn",
        "ListingOut": "_analyticshub_17_ListingOut",
        "SubscribeListingResponseIn": "_analyticshub_18_SubscribeListingResponseIn",
        "SubscribeListingResponseOut": "_analyticshub_19_SubscribeListingResponseOut",
        "ListListingsResponseIn": "_analyticshub_20_ListListingsResponseIn",
        "ListListingsResponseOut": "_analyticshub_21_ListListingsResponseOut",
        "ExprIn": "_analyticshub_22_ExprIn",
        "ExprOut": "_analyticshub_23_ExprOut",
        "GetPolicyOptionsIn": "_analyticshub_24_GetPolicyOptionsIn",
        "GetPolicyOptionsOut": "_analyticshub_25_GetPolicyOptionsOut",
        "BindingIn": "_analyticshub_26_BindingIn",
        "BindingOut": "_analyticshub_27_BindingOut",
        "DataExchangeIn": "_analyticshub_28_DataExchangeIn",
        "DataExchangeOut": "_analyticshub_29_DataExchangeOut",
        "TestIamPermissionsResponseIn": "_analyticshub_30_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_analyticshub_31_TestIamPermissionsResponseOut",
        "BigQueryDatasetSourceIn": "_analyticshub_32_BigQueryDatasetSourceIn",
        "BigQueryDatasetSourceOut": "_analyticshub_33_BigQueryDatasetSourceOut",
        "EmptyIn": "_analyticshub_34_EmptyIn",
        "EmptyOut": "_analyticshub_35_EmptyOut",
        "ListDataExchangesResponseIn": "_analyticshub_36_ListDataExchangesResponseIn",
        "ListDataExchangesResponseOut": "_analyticshub_37_ListDataExchangesResponseOut",
        "PolicyIn": "_analyticshub_38_PolicyIn",
        "PolicyOut": "_analyticshub_39_PolicyOut",
        "TestIamPermissionsRequestIn": "_analyticshub_40_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_analyticshub_41_TestIamPermissionsRequestOut",
        "AuditConfigIn": "_analyticshub_42_AuditConfigIn",
        "AuditConfigOut": "_analyticshub_43_AuditConfigOut",
        "SubscribeListingRequestIn": "_analyticshub_44_SubscribeListingRequestIn",
        "SubscribeListingRequestOut": "_analyticshub_45_SubscribeListingRequestOut",
        "PublisherIn": "_analyticshub_46_PublisherIn",
        "PublisherOut": "_analyticshub_47_PublisherOut",
        "DestinationDatasetIn": "_analyticshub_48_DestinationDatasetIn",
        "DestinationDatasetOut": "_analyticshub_49_DestinationDatasetOut",
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
    types["ListOrgDataExchangesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "dataExchanges": t.array(t.proxy(renames["DataExchangeIn"])).optional(),
        }
    ).named(renames["ListOrgDataExchangesResponseIn"])
    types["ListOrgDataExchangesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "dataExchanges": t.array(t.proxy(renames["DataExchangeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListOrgDataExchangesResponseOut"])
    types["DestinationDatasetReferenceIn"] = t.struct(
        {"projectId": t.string(), "datasetId": t.string()}
    ).named(renames["DestinationDatasetReferenceIn"])
    types["DestinationDatasetReferenceOut"] = t.struct(
        {
            "projectId": t.string(),
            "datasetId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DestinationDatasetReferenceOut"])
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
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "target": t.string().optional(),
            "statusDetail": t.string().optional(),
            "verb": t.string().optional(),
            "apiVersion": t.string().optional(),
            "createTime": t.string().optional(),
            "endTime": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
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
    types["GetIamPolicyRequestIn"] = t.struct(
        {"options": t.proxy(renames["GetPolicyOptionsIn"]).optional()}
    ).named(renames["GetIamPolicyRequestIn"])
    types["GetIamPolicyRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["GetPolicyOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIamPolicyRequestOut"])
    types["ListingIn"] = t.struct(
        {
            "documentation": t.string().optional(),
            "primaryContact": t.string().optional(),
            "publisher": t.proxy(renames["PublisherIn"]).optional(),
            "displayName": t.string(),
            "requestAccess": t.string().optional(),
            "dataProvider": t.proxy(renames["DataProviderIn"]).optional(),
            "description": t.string().optional(),
            "categories": t.array(t.string()).optional(),
            "icon": t.string().optional(),
            "bigqueryDataset": t.proxy(renames["BigQueryDatasetSourceIn"]),
        }
    ).named(renames["ListingIn"])
    types["ListingOut"] = t.struct(
        {
            "documentation": t.string().optional(),
            "primaryContact": t.string().optional(),
            "publisher": t.proxy(renames["PublisherOut"]).optional(),
            "displayName": t.string(),
            "requestAccess": t.string().optional(),
            "dataProvider": t.proxy(renames["DataProviderOut"]).optional(),
            "description": t.string().optional(),
            "categories": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "icon": t.string().optional(),
            "bigqueryDataset": t.proxy(renames["BigQueryDatasetSourceOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListingOut"])
    types["SubscribeListingResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["SubscribeListingResponseIn"]
    )
    types["SubscribeListingResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SubscribeListingResponseOut"])
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
    types["ExprIn"] = t.struct(
        {
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "location": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "location": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["GetPolicyOptionsIn"] = t.struct(
        {"requestedPolicyVersion": t.integer().optional()}
    ).named(renames["GetPolicyOptionsIn"])
    types["GetPolicyOptionsOut"] = t.struct(
        {
            "requestedPolicyVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetPolicyOptionsOut"])
    types["BindingIn"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "role": t.string().optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["DataExchangeIn"] = t.struct(
        {
            "description": t.string().optional(),
            "icon": t.string().optional(),
            "displayName": t.string(),
            "primaryContact": t.string().optional(),
            "documentation": t.string().optional(),
        }
    ).named(renames["DataExchangeIn"])
    types["DataExchangeOut"] = t.struct(
        {
            "description": t.string().optional(),
            "icon": t.string().optional(),
            "displayName": t.string(),
            "listingCount": t.integer().optional(),
            "primaryContact": t.string().optional(),
            "name": t.string().optional(),
            "documentation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataExchangeOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["BigQueryDatasetSourceIn"] = t.struct(
        {"dataset": t.string().optional()}
    ).named(renames["BigQueryDatasetSourceIn"])
    types["BigQueryDatasetSourceOut"] = t.struct(
        {
            "dataset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BigQueryDatasetSourceOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ListDataExchangesResponseIn"] = t.struct(
        {
            "dataExchanges": t.array(t.proxy(renames["DataExchangeIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListDataExchangesResponseIn"])
    types["ListDataExchangesResponseOut"] = t.struct(
        {
            "dataExchanges": t.array(t.proxy(renames["DataExchangeOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDataExchangesResponseOut"])
    types["PolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
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
    types["SubscribeListingRequestIn"] = t.struct(
        {"destinationDataset": t.proxy(renames["DestinationDatasetIn"]).optional()}
    ).named(renames["SubscribeListingRequestIn"])
    types["SubscribeListingRequestOut"] = t.struct(
        {
            "destinationDataset": t.proxy(renames["DestinationDatasetOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscribeListingRequestOut"])
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
    types["DestinationDatasetIn"] = t.struct(
        {
            "datasetReference": t.proxy(renames["DestinationDatasetReferenceIn"]),
            "description": t.string().optional(),
            "location": t.string(),
            "friendlyName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["DestinationDatasetIn"])
    types["DestinationDatasetOut"] = t.struct(
        {
            "datasetReference": t.proxy(renames["DestinationDatasetReferenceOut"]),
            "description": t.string().optional(),
            "location": t.string(),
            "friendlyName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DestinationDatasetOut"])

    functions = {}
    functions["organizationsLocationsDataExchangesList"] = analyticshub.get(
        "v1/{organization}/dataExchanges",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "organization": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOrgDataExchangesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataExchangesSetIamPolicy"] = analyticshub.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "icon": t.string().optional(),
                "displayName": t.string(),
                "primaryContact": t.string().optional(),
                "documentation": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DataExchangeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataExchangesDelete"] = analyticshub.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "icon": t.string().optional(),
                "displayName": t.string(),
                "primaryContact": t.string().optional(),
                "documentation": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DataExchangeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataExchangesList"] = analyticshub.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "icon": t.string().optional(),
                "displayName": t.string(),
                "primaryContact": t.string().optional(),
                "documentation": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DataExchangeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataExchangesGet"] = analyticshub.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "icon": t.string().optional(),
                "displayName": t.string(),
                "primaryContact": t.string().optional(),
                "documentation": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DataExchangeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataExchangesCreate"] = analyticshub.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "icon": t.string().optional(),
                "displayName": t.string(),
                "primaryContact": t.string().optional(),
                "documentation": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DataExchangeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataExchangesGetIamPolicy"] = analyticshub.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "icon": t.string().optional(),
                "displayName": t.string(),
                "primaryContact": t.string().optional(),
                "documentation": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DataExchangeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataExchangesTestIamPermissions"] = analyticshub.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "icon": t.string().optional(),
                "displayName": t.string(),
                "primaryContact": t.string().optional(),
                "documentation": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DataExchangeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataExchangesPatch"] = analyticshub.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "icon": t.string().optional(),
                "displayName": t.string(),
                "primaryContact": t.string().optional(),
                "documentation": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DataExchangeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataExchangesListingsGetIamPolicy"] = analyticshub.post(
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
    functions["projectsLocationsDataExchangesListingsCreate"] = analyticshub.post(
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
    functions["projectsLocationsDataExchangesListingsList"] = analyticshub.post(
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
    functions["projectsLocationsDataExchangesListingsSubscribe"] = analyticshub.post(
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
    functions["projectsLocationsDataExchangesListingsDelete"] = analyticshub.post(
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
    functions["projectsLocationsDataExchangesListingsGet"] = analyticshub.post(
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
    functions["projectsLocationsDataExchangesListingsSetIamPolicy"] = analyticshub.post(
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
    functions["projectsLocationsDataExchangesListingsPatch"] = analyticshub.post(
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
    functions[
        "projectsLocationsDataExchangesListingsTestIamPermissions"
    ] = analyticshub.post(
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

    return Import(
        importer="analyticshub", renames=renames, types=types, functions=functions
    )
