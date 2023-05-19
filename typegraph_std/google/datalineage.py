from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_datalineage() -> Import:
    datalineage = HTTPRuntime("https://datalineage.googleapis.com/")

    renames = {
        "ErrorResponse": "_datalineage_1_ErrorResponse",
        "GoogleCloudDatacatalogLineageV1RunIn": "_datalineage_2_GoogleCloudDatacatalogLineageV1RunIn",
        "GoogleCloudDatacatalogLineageV1RunOut": "_datalineage_3_GoogleCloudDatacatalogLineageV1RunOut",
        "GoogleCloudDatacatalogLineageV1LinkIn": "_datalineage_4_GoogleCloudDatacatalogLineageV1LinkIn",
        "GoogleCloudDatacatalogLineageV1LinkOut": "_datalineage_5_GoogleCloudDatacatalogLineageV1LinkOut",
        "GoogleCloudDatacatalogLineageV1ProcessLinksIn": "_datalineage_6_GoogleCloudDatacatalogLineageV1ProcessLinksIn",
        "GoogleCloudDatacatalogLineageV1ProcessLinksOut": "_datalineage_7_GoogleCloudDatacatalogLineageV1ProcessLinksOut",
        "GoogleCloudDatacatalogLineageV1ListRunsResponseIn": "_datalineage_8_GoogleCloudDatacatalogLineageV1ListRunsResponseIn",
        "GoogleCloudDatacatalogLineageV1ListRunsResponseOut": "_datalineage_9_GoogleCloudDatacatalogLineageV1ListRunsResponseOut",
        "GoogleCloudDatacatalogLineageV1OperationMetadataIn": "_datalineage_10_GoogleCloudDatacatalogLineageV1OperationMetadataIn",
        "GoogleCloudDatacatalogLineageV1OperationMetadataOut": "_datalineage_11_GoogleCloudDatacatalogLineageV1OperationMetadataOut",
        "GoogleLongrunningListOperationsResponseIn": "_datalineage_12_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_datalineage_13_GoogleLongrunningListOperationsResponseOut",
        "GoogleCloudDatacatalogLineageV1SearchLinksRequestIn": "_datalineage_14_GoogleCloudDatacatalogLineageV1SearchLinksRequestIn",
        "GoogleCloudDatacatalogLineageV1SearchLinksRequestOut": "_datalineage_15_GoogleCloudDatacatalogLineageV1SearchLinksRequestOut",
        "GoogleCloudDatacatalogLineageV1LineageEventIn": "_datalineage_16_GoogleCloudDatacatalogLineageV1LineageEventIn",
        "GoogleCloudDatacatalogLineageV1LineageEventOut": "_datalineage_17_GoogleCloudDatacatalogLineageV1LineageEventOut",
        "GoogleProtobufEmptyIn": "_datalineage_18_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_datalineage_19_GoogleProtobufEmptyOut",
        "GoogleRpcStatusIn": "_datalineage_20_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_datalineage_21_GoogleRpcStatusOut",
        "GoogleLongrunningCancelOperationRequestIn": "_datalineage_22_GoogleLongrunningCancelOperationRequestIn",
        "GoogleLongrunningCancelOperationRequestOut": "_datalineage_23_GoogleLongrunningCancelOperationRequestOut",
        "GoogleCloudDatacatalogLineageV1OriginIn": "_datalineage_24_GoogleCloudDatacatalogLineageV1OriginIn",
        "GoogleCloudDatacatalogLineageV1OriginOut": "_datalineage_25_GoogleCloudDatacatalogLineageV1OriginOut",
        "GoogleLongrunningOperationIn": "_datalineage_26_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_datalineage_27_GoogleLongrunningOperationOut",
        "GoogleCloudDatacatalogLineageV1ProcessIn": "_datalineage_28_GoogleCloudDatacatalogLineageV1ProcessIn",
        "GoogleCloudDatacatalogLineageV1ProcessOut": "_datalineage_29_GoogleCloudDatacatalogLineageV1ProcessOut",
        "GoogleCloudDatacatalogLineageV1SearchLinksResponseIn": "_datalineage_30_GoogleCloudDatacatalogLineageV1SearchLinksResponseIn",
        "GoogleCloudDatacatalogLineageV1SearchLinksResponseOut": "_datalineage_31_GoogleCloudDatacatalogLineageV1SearchLinksResponseOut",
        "GoogleCloudDatacatalogLineageV1ProcessLinkInfoIn": "_datalineage_32_GoogleCloudDatacatalogLineageV1ProcessLinkInfoIn",
        "GoogleCloudDatacatalogLineageV1ProcessLinkInfoOut": "_datalineage_33_GoogleCloudDatacatalogLineageV1ProcessLinkInfoOut",
        "GoogleCloudDatacatalogLineageV1EventLinkIn": "_datalineage_34_GoogleCloudDatacatalogLineageV1EventLinkIn",
        "GoogleCloudDatacatalogLineageV1EventLinkOut": "_datalineage_35_GoogleCloudDatacatalogLineageV1EventLinkOut",
        "GoogleCloudDatacatalogLineageV1ListProcessesResponseIn": "_datalineage_36_GoogleCloudDatacatalogLineageV1ListProcessesResponseIn",
        "GoogleCloudDatacatalogLineageV1ListProcessesResponseOut": "_datalineage_37_GoogleCloudDatacatalogLineageV1ListProcessesResponseOut",
        "GoogleCloudDatacatalogLineageV1EntityReferenceIn": "_datalineage_38_GoogleCloudDatacatalogLineageV1EntityReferenceIn",
        "GoogleCloudDatacatalogLineageV1EntityReferenceOut": "_datalineage_39_GoogleCloudDatacatalogLineageV1EntityReferenceOut",
        "GoogleCloudDatacatalogLineageV1ListLineageEventsResponseIn": "_datalineage_40_GoogleCloudDatacatalogLineageV1ListLineageEventsResponseIn",
        "GoogleCloudDatacatalogLineageV1ListLineageEventsResponseOut": "_datalineage_41_GoogleCloudDatacatalogLineageV1ListLineageEventsResponseOut",
        "GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesRequestIn": "_datalineage_42_GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesRequestIn",
        "GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesRequestOut": "_datalineage_43_GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesRequestOut",
        "GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesResponseIn": "_datalineage_44_GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesResponseIn",
        "GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesResponseOut": "_datalineage_45_GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudDatacatalogLineageV1RunIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "endTime": t.string().optional(),
            "state": t.string(),
            "startTime": t.string(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1RunIn"])
    types["GoogleCloudDatacatalogLineageV1RunOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "endTime": t.string().optional(),
            "state": t.string(),
            "startTime": t.string(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1RunOut"])
    types["GoogleCloudDatacatalogLineageV1LinkIn"] = t.struct(
        {
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "source": t.proxy(
                renames["GoogleCloudDatacatalogLineageV1EntityReferenceIn"]
            ).optional(),
            "target": t.proxy(
                renames["GoogleCloudDatacatalogLineageV1EntityReferenceIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1LinkIn"])
    types["GoogleCloudDatacatalogLineageV1LinkOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "source": t.proxy(
                renames["GoogleCloudDatacatalogLineageV1EntityReferenceOut"]
            ).optional(),
            "name": t.string().optional(),
            "target": t.proxy(
                renames["GoogleCloudDatacatalogLineageV1EntityReferenceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1LinkOut"])
    types["GoogleCloudDatacatalogLineageV1ProcessLinksIn"] = t.struct(
        {
            "links": t.array(
                t.proxy(renames["GoogleCloudDatacatalogLineageV1ProcessLinkInfoIn"])
            ).optional(),
            "process": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1ProcessLinksIn"])
    types["GoogleCloudDatacatalogLineageV1ProcessLinksOut"] = t.struct(
        {
            "links": t.array(
                t.proxy(renames["GoogleCloudDatacatalogLineageV1ProcessLinkInfoOut"])
            ).optional(),
            "process": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1ProcessLinksOut"])
    types["GoogleCloudDatacatalogLineageV1ListRunsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "runs": t.array(
                t.proxy(renames["GoogleCloudDatacatalogLineageV1RunIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1ListRunsResponseIn"])
    types["GoogleCloudDatacatalogLineageV1ListRunsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "runs": t.array(
                t.proxy(renames["GoogleCloudDatacatalogLineageV1RunOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1ListRunsResponseOut"])
    types["GoogleCloudDatacatalogLineageV1OperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogLineageV1OperationMetadataIn"])
    types["GoogleCloudDatacatalogLineageV1OperationMetadataOut"] = t.struct(
        {
            "resource": t.string().optional(),
            "state": t.string().optional(),
            "resourceUuid": t.string().optional(),
            "operationType": t.string().optional(),
            "createTime": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1OperationMetadataOut"])
    types["GoogleLongrunningListOperationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(
                t.proxy(renames["GoogleLongrunningOperationIn"])
            ).optional(),
        }
    ).named(renames["GoogleLongrunningListOperationsResponseIn"])
    types["GoogleLongrunningListOperationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(
                t.proxy(renames["GoogleLongrunningOperationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleLongrunningListOperationsResponseOut"])
    types["GoogleCloudDatacatalogLineageV1SearchLinksRequestIn"] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "source": t.proxy(
                renames["GoogleCloudDatacatalogLineageV1EntityReferenceIn"]
            ).optional(),
            "target": t.proxy(
                renames["GoogleCloudDatacatalogLineageV1EntityReferenceIn"]
            ).optional(),
            "pageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1SearchLinksRequestIn"])
    types["GoogleCloudDatacatalogLineageV1SearchLinksRequestOut"] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "source": t.proxy(
                renames["GoogleCloudDatacatalogLineageV1EntityReferenceOut"]
            ).optional(),
            "target": t.proxy(
                renames["GoogleCloudDatacatalogLineageV1EntityReferenceOut"]
            ).optional(),
            "pageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1SearchLinksRequestOut"])
    types["GoogleCloudDatacatalogLineageV1LineageEventIn"] = t.struct(
        {
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "name": t.string().optional(),
            "links": t.array(
                t.proxy(renames["GoogleCloudDatacatalogLineageV1EventLinkIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1LineageEventIn"])
    types["GoogleCloudDatacatalogLineageV1LineageEventOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "name": t.string().optional(),
            "links": t.array(
                t.proxy(renames["GoogleCloudDatacatalogLineageV1EventLinkOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1LineageEventOut"])
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
    types["GoogleRpcStatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["GoogleRpcStatusIn"])
    types["GoogleRpcStatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleRpcStatusOut"])
    types["GoogleLongrunningCancelOperationRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestIn"])
    types["GoogleLongrunningCancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestOut"])
    types["GoogleCloudDatacatalogLineageV1OriginIn"] = t.struct(
        {"sourceType": t.string().optional(), "name": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogLineageV1OriginIn"])
    types["GoogleCloudDatacatalogLineageV1OriginOut"] = t.struct(
        {
            "sourceType": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1OriginOut"])
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
    types["GoogleCloudDatacatalogLineageV1ProcessIn"] = t.struct(
        {
            "origin": t.proxy(
                renames["GoogleCloudDatacatalogLineageV1OriginIn"]
            ).optional(),
            "name": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1ProcessIn"])
    types["GoogleCloudDatacatalogLineageV1ProcessOut"] = t.struct(
        {
            "origin": t.proxy(
                renames["GoogleCloudDatacatalogLineageV1OriginOut"]
            ).optional(),
            "name": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1ProcessOut"])
    types["GoogleCloudDatacatalogLineageV1SearchLinksResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "links": t.array(
                t.proxy(renames["GoogleCloudDatacatalogLineageV1LinkIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1SearchLinksResponseIn"])
    types["GoogleCloudDatacatalogLineageV1SearchLinksResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "links": t.array(
                t.proxy(renames["GoogleCloudDatacatalogLineageV1LinkOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1SearchLinksResponseOut"])
    types["GoogleCloudDatacatalogLineageV1ProcessLinkInfoIn"] = t.struct(
        {
            "endTime": t.string().optional(),
            "link": t.string().optional(),
            "startTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1ProcessLinkInfoIn"])
    types["GoogleCloudDatacatalogLineageV1ProcessLinkInfoOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "link": t.string().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1ProcessLinkInfoOut"])
    types["GoogleCloudDatacatalogLineageV1EventLinkIn"] = t.struct(
        {
            "source": t.proxy(
                renames["GoogleCloudDatacatalogLineageV1EntityReferenceIn"]
            ),
            "target": t.proxy(
                renames["GoogleCloudDatacatalogLineageV1EntityReferenceIn"]
            ),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1EventLinkIn"])
    types["GoogleCloudDatacatalogLineageV1EventLinkOut"] = t.struct(
        {
            "source": t.proxy(
                renames["GoogleCloudDatacatalogLineageV1EntityReferenceOut"]
            ),
            "target": t.proxy(
                renames["GoogleCloudDatacatalogLineageV1EntityReferenceOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1EventLinkOut"])
    types["GoogleCloudDatacatalogLineageV1ListProcessesResponseIn"] = t.struct(
        {
            "processes": t.array(
                t.proxy(renames["GoogleCloudDatacatalogLineageV1ProcessIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1ListProcessesResponseIn"])
    types["GoogleCloudDatacatalogLineageV1ListProcessesResponseOut"] = t.struct(
        {
            "processes": t.array(
                t.proxy(renames["GoogleCloudDatacatalogLineageV1ProcessOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1ListProcessesResponseOut"])
    types["GoogleCloudDatacatalogLineageV1EntityReferenceIn"] = t.struct(
        {"fullyQualifiedName": t.string()}
    ).named(renames["GoogleCloudDatacatalogLineageV1EntityReferenceIn"])
    types["GoogleCloudDatacatalogLineageV1EntityReferenceOut"] = t.struct(
        {
            "fullyQualifiedName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1EntityReferenceOut"])
    types["GoogleCloudDatacatalogLineageV1ListLineageEventsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "lineageEvents": t.array(
                t.proxy(renames["GoogleCloudDatacatalogLineageV1LineageEventIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1ListLineageEventsResponseIn"])
    types["GoogleCloudDatacatalogLineageV1ListLineageEventsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "lineageEvents": t.array(
                t.proxy(renames["GoogleCloudDatacatalogLineageV1LineageEventOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1ListLineageEventsResponseOut"])
    types[
        "GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesRequestIn"
    ] = t.struct(
        {
            "pageToken": t.string().optional(),
            "links": t.array(t.string()),
            "pageSize": t.integer().optional(),
        }
    ).named(
        renames["GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesRequestIn"]
    )
    types[
        "GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesRequestOut"
    ] = t.struct(
        {
            "pageToken": t.string().optional(),
            "links": t.array(t.string()),
            "pageSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesRequestOut"]
    )
    types[
        "GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesResponseIn"
    ] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "processLinks": t.array(
                t.proxy(renames["GoogleCloudDatacatalogLineageV1ProcessLinksIn"])
            ).optional(),
        }
    ).named(
        renames["GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesResponseIn"]
    )
    types[
        "GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesResponseOut"
    ] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "processLinks": t.array(
                t.proxy(renames["GoogleCloudDatacatalogLineageV1ProcessLinksOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesResponseOut"]
    )

    functions = {}
    functions["projectsLocationsBatchSearchLinkProcesses"] = datalineage.post(
        "v1/{parent}:searchLinks",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "source": t.proxy(
                    renames["GoogleCloudDatacatalogLineageV1EntityReferenceIn"]
                ).optional(),
                "target": t.proxy(
                    renames["GoogleCloudDatacatalogLineageV1EntityReferenceIn"]
                ).optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogLineageV1SearchLinksResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSearchLinks"] = datalineage.post(
        "v1/{parent}:searchLinks",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "source": t.proxy(
                    renames["GoogleCloudDatacatalogLineageV1EntityReferenceIn"]
                ).optional(),
                "target": t.proxy(
                    renames["GoogleCloudDatacatalogLineageV1EntityReferenceIn"]
                ).optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogLineageV1SearchLinksResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = datalineage.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = datalineage.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = datalineage.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = datalineage.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessesGet"] = datalineage.delete(
        "v1/{name}",
        t.struct(
            {
                "allowMissing": t.boolean().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessesPatch"] = datalineage.delete(
        "v1/{name}",
        t.struct(
            {
                "allowMissing": t.boolean().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessesCreate"] = datalineage.delete(
        "v1/{name}",
        t.struct(
            {
                "allowMissing": t.boolean().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessesList"] = datalineage.delete(
        "v1/{name}",
        t.struct(
            {
                "allowMissing": t.boolean().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessesDelete"] = datalineage.delete(
        "v1/{name}",
        t.struct(
            {
                "allowMissing": t.boolean().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessesRunsGet"] = datalineage.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "allowMissing": t.boolean().optional(),
                "displayName": t.string().optional(),
                "endTime": t.string().optional(),
                "state": t.string(),
                "startTime": t.string(),
                "attributes": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogLineageV1RunOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessesRunsList"] = datalineage.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "allowMissing": t.boolean().optional(),
                "displayName": t.string().optional(),
                "endTime": t.string().optional(),
                "state": t.string(),
                "startTime": t.string(),
                "attributes": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogLineageV1RunOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessesRunsDelete"] = datalineage.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "allowMissing": t.boolean().optional(),
                "displayName": t.string().optional(),
                "endTime": t.string().optional(),
                "state": t.string(),
                "startTime": t.string(),
                "attributes": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogLineageV1RunOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessesRunsCreate"] = datalineage.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "allowMissing": t.boolean().optional(),
                "displayName": t.string().optional(),
                "endTime": t.string().optional(),
                "state": t.string(),
                "startTime": t.string(),
                "attributes": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogLineageV1RunOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessesRunsPatch"] = datalineage.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "allowMissing": t.boolean().optional(),
                "displayName": t.string().optional(),
                "endTime": t.string().optional(),
                "state": t.string(),
                "startTime": t.string(),
                "attributes": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogLineageV1RunOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessesRunsLineageEventsDelete"] = datalineage.get(
        "v1/{parent}/lineageEvents",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogLineageV1ListLineageEventsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessesRunsLineageEventsGet"] = datalineage.get(
        "v1/{parent}/lineageEvents",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogLineageV1ListLineageEventsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessesRunsLineageEventsCreate"] = datalineage.get(
        "v1/{parent}/lineageEvents",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogLineageV1ListLineageEventsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessesRunsLineageEventsList"] = datalineage.get(
        "v1/{parent}/lineageEvents",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogLineageV1ListLineageEventsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="datalineage",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
