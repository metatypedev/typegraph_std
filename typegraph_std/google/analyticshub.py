from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_analyticshub():
    analyticshub = HTTPRuntime("https://analyticshub.googleapis.com/")

    renames = {
        "ErrorResponse": "_analyticshub_1_ErrorResponse",
        "OperationMetadataIn": "_analyticshub_2_OperationMetadataIn",
        "OperationMetadataOut": "_analyticshub_3_OperationMetadataOut",
        "ListOrgDataExchangesResponseIn": "_analyticshub_4_ListOrgDataExchangesResponseIn",
        "ListOrgDataExchangesResponseOut": "_analyticshub_5_ListOrgDataExchangesResponseOut",
        "GetPolicyOptionsIn": "_analyticshub_6_GetPolicyOptionsIn",
        "GetPolicyOptionsOut": "_analyticshub_7_GetPolicyOptionsOut",
        "TestIamPermissionsResponseIn": "_analyticshub_8_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_analyticshub_9_TestIamPermissionsResponseOut",
        "DataProviderIn": "_analyticshub_10_DataProviderIn",
        "DataProviderOut": "_analyticshub_11_DataProviderOut",
        "AuditLogConfigIn": "_analyticshub_12_AuditLogConfigIn",
        "AuditLogConfigOut": "_analyticshub_13_AuditLogConfigOut",
        "GetIamPolicyRequestIn": "_analyticshub_14_GetIamPolicyRequestIn",
        "GetIamPolicyRequestOut": "_analyticshub_15_GetIamPolicyRequestOut",
        "TestIamPermissionsRequestIn": "_analyticshub_16_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_analyticshub_17_TestIamPermissionsRequestOut",
        "ListDataExchangesResponseIn": "_analyticshub_18_ListDataExchangesResponseIn",
        "ListDataExchangesResponseOut": "_analyticshub_19_ListDataExchangesResponseOut",
        "ListListingsResponseIn": "_analyticshub_20_ListListingsResponseIn",
        "ListListingsResponseOut": "_analyticshub_21_ListListingsResponseOut",
        "ExprIn": "_analyticshub_22_ExprIn",
        "ExprOut": "_analyticshub_23_ExprOut",
        "DestinationDatasetReferenceIn": "_analyticshub_24_DestinationDatasetReferenceIn",
        "DestinationDatasetReferenceOut": "_analyticshub_25_DestinationDatasetReferenceOut",
        "SubscribeListingResponseIn": "_analyticshub_26_SubscribeListingResponseIn",
        "SubscribeListingResponseOut": "_analyticshub_27_SubscribeListingResponseOut",
        "PolicyIn": "_analyticshub_28_PolicyIn",
        "PolicyOut": "_analyticshub_29_PolicyOut",
        "DataExchangeIn": "_analyticshub_30_DataExchangeIn",
        "DataExchangeOut": "_analyticshub_31_DataExchangeOut",
        "BigQueryDatasetSourceIn": "_analyticshub_32_BigQueryDatasetSourceIn",
        "BigQueryDatasetSourceOut": "_analyticshub_33_BigQueryDatasetSourceOut",
        "SetIamPolicyRequestIn": "_analyticshub_34_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_analyticshub_35_SetIamPolicyRequestOut",
        "AuditConfigIn": "_analyticshub_36_AuditConfigIn",
        "AuditConfigOut": "_analyticshub_37_AuditConfigOut",
        "ListingIn": "_analyticshub_38_ListingIn",
        "ListingOut": "_analyticshub_39_ListingOut",
        "BindingIn": "_analyticshub_40_BindingIn",
        "BindingOut": "_analyticshub_41_BindingOut",
        "EmptyIn": "_analyticshub_42_EmptyIn",
        "EmptyOut": "_analyticshub_43_EmptyOut",
        "SubscribeListingRequestIn": "_analyticshub_44_SubscribeListingRequestIn",
        "SubscribeListingRequestOut": "_analyticshub_45_SubscribeListingRequestOut",
        "DestinationDatasetIn": "_analyticshub_46_DestinationDatasetIn",
        "DestinationDatasetOut": "_analyticshub_47_DestinationDatasetOut",
        "PublisherIn": "_analyticshub_48_PublisherIn",
        "PublisherOut": "_analyticshub_49_PublisherOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "target": t.string().optional(),
            "apiVersion": t.string().optional(),
            "endTime": t.string().optional(),
            "verb": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "statusDetail": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
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
    types["GetPolicyOptionsIn"] = t.struct(
        {"requestedPolicyVersion": t.integer().optional()}
    ).named(renames["GetPolicyOptionsIn"])
    types["GetPolicyOptionsOut"] = t.struct(
        {
            "requestedPolicyVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetPolicyOptionsOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
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
    types["GetIamPolicyRequestIn"] = t.struct(
        {"options": t.proxy(renames["GetPolicyOptionsIn"]).optional()}
    ).named(renames["GetIamPolicyRequestIn"])
    types["GetIamPolicyRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["GetPolicyOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIamPolicyRequestOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
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
    types["SubscribeListingResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["SubscribeListingResponseIn"]
    )
    types["SubscribeListingResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SubscribeListingResponseOut"])
    types["PolicyIn"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["DataExchangeIn"] = t.struct(
        {
            "primaryContact": t.string().optional(),
            "icon": t.string().optional(),
            "description": t.string().optional(),
            "displayName": t.string(),
            "documentation": t.string().optional(),
        }
    ).named(renames["DataExchangeIn"])
    types["DataExchangeOut"] = t.struct(
        {
            "primaryContact": t.string().optional(),
            "icon": t.string().optional(),
            "description": t.string().optional(),
            "displayName": t.string(),
            "documentation": t.string().optional(),
            "listingCount": t.integer().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataExchangeOut"])
    types["BigQueryDatasetSourceIn"] = t.struct(
        {"dataset": t.string().optional()}
    ).named(renames["BigQueryDatasetSourceIn"])
    types["BigQueryDatasetSourceOut"] = t.struct(
        {
            "dataset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BigQueryDatasetSourceOut"])
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
    types["AuditConfigIn"] = t.struct(
        {
            "auditLogConfigs": t.array(t.proxy(renames["AuditLogConfigIn"])).optional(),
            "service": t.string().optional(),
        }
    ).named(renames["AuditConfigIn"])
    types["AuditConfigOut"] = t.struct(
        {
            "auditLogConfigs": t.array(
                t.proxy(renames["AuditLogConfigOut"])
            ).optional(),
            "service": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditConfigOut"])
    types["ListingIn"] = t.struct(
        {
            "dataProvider": t.proxy(renames["DataProviderIn"]).optional(),
            "displayName": t.string(),
            "icon": t.string().optional(),
            "primaryContact": t.string().optional(),
            "publisher": t.proxy(renames["PublisherIn"]).optional(),
            "bigqueryDataset": t.proxy(renames["BigQueryDatasetSourceIn"]),
            "categories": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "documentation": t.string().optional(),
            "requestAccess": t.string().optional(),
        }
    ).named(renames["ListingIn"])
    types["ListingOut"] = t.struct(
        {
            "dataProvider": t.proxy(renames["DataProviderOut"]).optional(),
            "displayName": t.string(),
            "icon": t.string().optional(),
            "primaryContact": t.string().optional(),
            "publisher": t.proxy(renames["PublisherOut"]).optional(),
            "bigqueryDataset": t.proxy(renames["BigQueryDatasetSourceOut"]),
            "categories": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "documentation": t.string().optional(),
            "name": t.string().optional(),
            "requestAccess": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListingOut"])
    types["BindingIn"] = t.struct(
        {
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["SubscribeListingRequestIn"] = t.struct(
        {"destinationDataset": t.proxy(renames["DestinationDatasetIn"]).optional()}
    ).named(renames["SubscribeListingRequestIn"])
    types["SubscribeListingRequestOut"] = t.struct(
        {
            "destinationDataset": t.proxy(renames["DestinationDatasetOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscribeListingRequestOut"])
    types["DestinationDatasetIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "datasetReference": t.proxy(renames["DestinationDatasetReferenceIn"]),
            "description": t.string().optional(),
            "friendlyName": t.string().optional(),
            "location": t.string(),
        }
    ).named(renames["DestinationDatasetIn"])
    types["DestinationDatasetOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "datasetReference": t.proxy(renames["DestinationDatasetReferenceOut"]),
            "description": t.string().optional(),
            "friendlyName": t.string().optional(),
            "location": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DestinationDatasetOut"])
    types["PublisherIn"] = t.struct(
        {"primaryContact": t.string().optional(), "name": t.string().optional()}
    ).named(renames["PublisherIn"])
    types["PublisherOut"] = t.struct(
        {
            "primaryContact": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublisherOut"])

    functions = {}
    functions["organizationsLocationsDataExchangesList"] = analyticshub.get(
        "v1/{organization}/dataExchanges",
        t.struct(
            {
                "organization": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOrgDataExchangesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataExchangesList"] = analyticshub.post(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataExchangesGet"] = analyticshub.post(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataExchangesSetIamPolicy"] = analyticshub.post(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataExchangesCreate"] = analyticshub.post(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataExchangesDelete"] = analyticshub.post(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataExchangesTestIamPermissions"] = analyticshub.post(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataExchangesPatch"] = analyticshub.post(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataExchangesGetIamPolicy"] = analyticshub.post(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataExchangesListingsCreate"] = analyticshub.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "dataProvider": t.proxy(renames["DataProviderIn"]).optional(),
                "displayName": t.string(),
                "icon": t.string().optional(),
                "primaryContact": t.string().optional(),
                "publisher": t.proxy(renames["PublisherIn"]).optional(),
                "bigqueryDataset": t.proxy(renames["BigQueryDatasetSourceIn"]),
                "categories": t.array(t.string()).optional(),
                "description": t.string().optional(),
                "documentation": t.string().optional(),
                "requestAccess": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDataExchangesListingsTestIamPermissions"
    ] = analyticshub.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "dataProvider": t.proxy(renames["DataProviderIn"]).optional(),
                "displayName": t.string(),
                "icon": t.string().optional(),
                "primaryContact": t.string().optional(),
                "publisher": t.proxy(renames["PublisherIn"]).optional(),
                "bigqueryDataset": t.proxy(renames["BigQueryDatasetSourceIn"]),
                "categories": t.array(t.string()).optional(),
                "description": t.string().optional(),
                "documentation": t.string().optional(),
                "requestAccess": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataExchangesListingsList"] = analyticshub.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "dataProvider": t.proxy(renames["DataProviderIn"]).optional(),
                "displayName": t.string(),
                "icon": t.string().optional(),
                "primaryContact": t.string().optional(),
                "publisher": t.proxy(renames["PublisherIn"]).optional(),
                "bigqueryDataset": t.proxy(renames["BigQueryDatasetSourceIn"]),
                "categories": t.array(t.string()).optional(),
                "description": t.string().optional(),
                "documentation": t.string().optional(),
                "requestAccess": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataExchangesListingsDelete"] = analyticshub.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "dataProvider": t.proxy(renames["DataProviderIn"]).optional(),
                "displayName": t.string(),
                "icon": t.string().optional(),
                "primaryContact": t.string().optional(),
                "publisher": t.proxy(renames["PublisherIn"]).optional(),
                "bigqueryDataset": t.proxy(renames["BigQueryDatasetSourceIn"]),
                "categories": t.array(t.string()).optional(),
                "description": t.string().optional(),
                "documentation": t.string().optional(),
                "requestAccess": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataExchangesListingsSubscribe"] = analyticshub.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "dataProvider": t.proxy(renames["DataProviderIn"]).optional(),
                "displayName": t.string(),
                "icon": t.string().optional(),
                "primaryContact": t.string().optional(),
                "publisher": t.proxy(renames["PublisherIn"]).optional(),
                "bigqueryDataset": t.proxy(renames["BigQueryDatasetSourceIn"]),
                "categories": t.array(t.string()).optional(),
                "description": t.string().optional(),
                "documentation": t.string().optional(),
                "requestAccess": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDataExchangesListingsSetIamPolicy"
    ] = analyticshub.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "dataProvider": t.proxy(renames["DataProviderIn"]).optional(),
                "displayName": t.string(),
                "icon": t.string().optional(),
                "primaryContact": t.string().optional(),
                "publisher": t.proxy(renames["PublisherIn"]).optional(),
                "bigqueryDataset": t.proxy(renames["BigQueryDatasetSourceIn"]),
                "categories": t.array(t.string()).optional(),
                "description": t.string().optional(),
                "documentation": t.string().optional(),
                "requestAccess": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataExchangesListingsGet"] = analyticshub.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "dataProvider": t.proxy(renames["DataProviderIn"]).optional(),
                "displayName": t.string(),
                "icon": t.string().optional(),
                "primaryContact": t.string().optional(),
                "publisher": t.proxy(renames["PublisherIn"]).optional(),
                "bigqueryDataset": t.proxy(renames["BigQueryDatasetSourceIn"]),
                "categories": t.array(t.string()).optional(),
                "description": t.string().optional(),
                "documentation": t.string().optional(),
                "requestAccess": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDataExchangesListingsGetIamPolicy"
    ] = analyticshub.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "dataProvider": t.proxy(renames["DataProviderIn"]).optional(),
                "displayName": t.string(),
                "icon": t.string().optional(),
                "primaryContact": t.string().optional(),
                "publisher": t.proxy(renames["PublisherIn"]).optional(),
                "bigqueryDataset": t.proxy(renames["BigQueryDatasetSourceIn"]),
                "categories": t.array(t.string()).optional(),
                "description": t.string().optional(),
                "documentation": t.string().optional(),
                "requestAccess": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataExchangesListingsPatch"] = analyticshub.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "dataProvider": t.proxy(renames["DataProviderIn"]).optional(),
                "displayName": t.string(),
                "icon": t.string().optional(),
                "primaryContact": t.string().optional(),
                "publisher": t.proxy(renames["PublisherIn"]).optional(),
                "bigqueryDataset": t.proxy(renames["BigQueryDatasetSourceIn"]),
                "categories": t.array(t.string()).optional(),
                "description": t.string().optional(),
                "documentation": t.string().optional(),
                "requestAccess": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="analyticshub",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
