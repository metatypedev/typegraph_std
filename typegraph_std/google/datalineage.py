from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_datalineage() -> Import:
    datalineage = HTTPRuntime("https://datalineage.googleapis.com/")

    renames = {
        "ErrorResponse": "_datalineage_1_ErrorResponse",
        "GoogleCloudDatacatalogLineageV1ProcessIn": "_datalineage_2_GoogleCloudDatacatalogLineageV1ProcessIn",
        "GoogleCloudDatacatalogLineageV1ProcessOut": "_datalineage_3_GoogleCloudDatacatalogLineageV1ProcessOut",
        "GoogleLongrunningOperationIn": "_datalineage_4_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_datalineage_5_GoogleLongrunningOperationOut",
        "GoogleCloudDatacatalogLineageV1EntityReferenceIn": "_datalineage_6_GoogleCloudDatacatalogLineageV1EntityReferenceIn",
        "GoogleCloudDatacatalogLineageV1EntityReferenceOut": "_datalineage_7_GoogleCloudDatacatalogLineageV1EntityReferenceOut",
        "GoogleCloudDatacatalogLineageV1LinkIn": "_datalineage_8_GoogleCloudDatacatalogLineageV1LinkIn",
        "GoogleCloudDatacatalogLineageV1LinkOut": "_datalineage_9_GoogleCloudDatacatalogLineageV1LinkOut",
        "GoogleCloudDatacatalogLineageV1EventLinkIn": "_datalineage_10_GoogleCloudDatacatalogLineageV1EventLinkIn",
        "GoogleCloudDatacatalogLineageV1EventLinkOut": "_datalineage_11_GoogleCloudDatacatalogLineageV1EventLinkOut",
        "GoogleCloudDatacatalogLineageV1ListRunsResponseIn": "_datalineage_12_GoogleCloudDatacatalogLineageV1ListRunsResponseIn",
        "GoogleCloudDatacatalogLineageV1ListRunsResponseOut": "_datalineage_13_GoogleCloudDatacatalogLineageV1ListRunsResponseOut",
        "GoogleCloudDatacatalogLineageV1RunIn": "_datalineage_14_GoogleCloudDatacatalogLineageV1RunIn",
        "GoogleCloudDatacatalogLineageV1RunOut": "_datalineage_15_GoogleCloudDatacatalogLineageV1RunOut",
        "GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesResponseIn": "_datalineage_16_GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesResponseIn",
        "GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesResponseOut": "_datalineage_17_GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesResponseOut",
        "GoogleCloudDatacatalogLineageV1OperationMetadataIn": "_datalineage_18_GoogleCloudDatacatalogLineageV1OperationMetadataIn",
        "GoogleCloudDatacatalogLineageV1OperationMetadataOut": "_datalineage_19_GoogleCloudDatacatalogLineageV1OperationMetadataOut",
        "GoogleProtobufEmptyIn": "_datalineage_20_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_datalineage_21_GoogleProtobufEmptyOut",
        "GoogleCloudDatacatalogLineageV1ListLineageEventsResponseIn": "_datalineage_22_GoogleCloudDatacatalogLineageV1ListLineageEventsResponseIn",
        "GoogleCloudDatacatalogLineageV1ListLineageEventsResponseOut": "_datalineage_23_GoogleCloudDatacatalogLineageV1ListLineageEventsResponseOut",
        "GoogleRpcStatusIn": "_datalineage_24_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_datalineage_25_GoogleRpcStatusOut",
        "GoogleCloudDatacatalogLineageV1SearchLinksRequestIn": "_datalineage_26_GoogleCloudDatacatalogLineageV1SearchLinksRequestIn",
        "GoogleCloudDatacatalogLineageV1SearchLinksRequestOut": "_datalineage_27_GoogleCloudDatacatalogLineageV1SearchLinksRequestOut",
        "GoogleCloudDatacatalogLineageV1SearchLinksResponseIn": "_datalineage_28_GoogleCloudDatacatalogLineageV1SearchLinksResponseIn",
        "GoogleCloudDatacatalogLineageV1SearchLinksResponseOut": "_datalineage_29_GoogleCloudDatacatalogLineageV1SearchLinksResponseOut",
        "GoogleCloudDatacatalogLineageV1ListProcessesResponseIn": "_datalineage_30_GoogleCloudDatacatalogLineageV1ListProcessesResponseIn",
        "GoogleCloudDatacatalogLineageV1ListProcessesResponseOut": "_datalineage_31_GoogleCloudDatacatalogLineageV1ListProcessesResponseOut",
        "GoogleCloudDatacatalogLineageV1LineageEventIn": "_datalineage_32_GoogleCloudDatacatalogLineageV1LineageEventIn",
        "GoogleCloudDatacatalogLineageV1LineageEventOut": "_datalineage_33_GoogleCloudDatacatalogLineageV1LineageEventOut",
        "GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesRequestIn": "_datalineage_34_GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesRequestIn",
        "GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesRequestOut": "_datalineage_35_GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesRequestOut",
        "GoogleLongrunningCancelOperationRequestIn": "_datalineage_36_GoogleLongrunningCancelOperationRequestIn",
        "GoogleLongrunningCancelOperationRequestOut": "_datalineage_37_GoogleLongrunningCancelOperationRequestOut",
        "GoogleCloudDatacatalogLineageV1ProcessLinkInfoIn": "_datalineage_38_GoogleCloudDatacatalogLineageV1ProcessLinkInfoIn",
        "GoogleCloudDatacatalogLineageV1ProcessLinkInfoOut": "_datalineage_39_GoogleCloudDatacatalogLineageV1ProcessLinkInfoOut",
        "GoogleCloudDatacatalogLineageV1OriginIn": "_datalineage_40_GoogleCloudDatacatalogLineageV1OriginIn",
        "GoogleCloudDatacatalogLineageV1OriginOut": "_datalineage_41_GoogleCloudDatacatalogLineageV1OriginOut",
        "GoogleCloudDatacatalogLineageV1ProcessLinksIn": "_datalineage_42_GoogleCloudDatacatalogLineageV1ProcessLinksIn",
        "GoogleCloudDatacatalogLineageV1ProcessLinksOut": "_datalineage_43_GoogleCloudDatacatalogLineageV1ProcessLinksOut",
        "GoogleLongrunningListOperationsResponseIn": "_datalineage_44_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_datalineage_45_GoogleLongrunningListOperationsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudDatacatalogLineageV1ProcessIn"] = t.struct(
        {
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "origin": t.proxy(
                renames["GoogleCloudDatacatalogLineageV1OriginIn"]
            ).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1ProcessIn"])
    types["GoogleCloudDatacatalogLineageV1ProcessOut"] = t.struct(
        {
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "origin": t.proxy(
                renames["GoogleCloudDatacatalogLineageV1OriginOut"]
            ).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1ProcessOut"])
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
    types["GoogleCloudDatacatalogLineageV1EntityReferenceIn"] = t.struct(
        {"fullyQualifiedName": t.string()}
    ).named(renames["GoogleCloudDatacatalogLineageV1EntityReferenceIn"])
    types["GoogleCloudDatacatalogLineageV1EntityReferenceOut"] = t.struct(
        {
            "fullyQualifiedName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1EntityReferenceOut"])
    types["GoogleCloudDatacatalogLineageV1LinkIn"] = t.struct(
        {
            "target": t.proxy(
                renames["GoogleCloudDatacatalogLineageV1EntityReferenceIn"]
            ).optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "source": t.proxy(
                renames["GoogleCloudDatacatalogLineageV1EntityReferenceIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1LinkIn"])
    types["GoogleCloudDatacatalogLineageV1LinkOut"] = t.struct(
        {
            "target": t.proxy(
                renames["GoogleCloudDatacatalogLineageV1EntityReferenceOut"]
            ).optional(),
            "endTime": t.string().optional(),
            "name": t.string().optional(),
            "startTime": t.string().optional(),
            "source": t.proxy(
                renames["GoogleCloudDatacatalogLineageV1EntityReferenceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1LinkOut"])
    types["GoogleCloudDatacatalogLineageV1EventLinkIn"] = t.struct(
        {
            "target": t.proxy(
                renames["GoogleCloudDatacatalogLineageV1EntityReferenceIn"]
            ),
            "source": t.proxy(
                renames["GoogleCloudDatacatalogLineageV1EntityReferenceIn"]
            ),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1EventLinkIn"])
    types["GoogleCloudDatacatalogLineageV1EventLinkOut"] = t.struct(
        {
            "target": t.proxy(
                renames["GoogleCloudDatacatalogLineageV1EntityReferenceOut"]
            ),
            "source": t.proxy(
                renames["GoogleCloudDatacatalogLineageV1EntityReferenceOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1EventLinkOut"])
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
    types["GoogleCloudDatacatalogLineageV1RunIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "state": t.string(),
            "endTime": t.string().optional(),
            "startTime": t.string(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1RunIn"])
    types["GoogleCloudDatacatalogLineageV1RunOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "state": t.string(),
            "endTime": t.string().optional(),
            "startTime": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1RunOut"])
    types[
        "GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesResponseIn"
    ] = t.struct(
        {
            "processLinks": t.array(
                t.proxy(renames["GoogleCloudDatacatalogLineageV1ProcessLinksIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesResponseIn"]
    )
    types[
        "GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesResponseOut"
    ] = t.struct(
        {
            "processLinks": t.array(
                t.proxy(renames["GoogleCloudDatacatalogLineageV1ProcessLinksOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesResponseOut"]
    )
    types["GoogleCloudDatacatalogLineageV1OperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogLineageV1OperationMetadataIn"])
    types["GoogleCloudDatacatalogLineageV1OperationMetadataOut"] = t.struct(
        {
            "state": t.string().optional(),
            "operationType": t.string().optional(),
            "createTime": t.string().optional(),
            "endTime": t.string().optional(),
            "resourceUuid": t.string().optional(),
            "resource": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1OperationMetadataOut"])
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
    types["GoogleCloudDatacatalogLineageV1ListLineageEventsResponseIn"] = t.struct(
        {
            "lineageEvents": t.array(
                t.proxy(renames["GoogleCloudDatacatalogLineageV1LineageEventIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1ListLineageEventsResponseIn"])
    types["GoogleCloudDatacatalogLineageV1ListLineageEventsResponseOut"] = t.struct(
        {
            "lineageEvents": t.array(
                t.proxy(renames["GoogleCloudDatacatalogLineageV1LineageEventOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1ListLineageEventsResponseOut"])
    types["GoogleRpcStatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["GoogleRpcStatusIn"])
    types["GoogleRpcStatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleRpcStatusOut"])
    types["GoogleCloudDatacatalogLineageV1SearchLinksRequestIn"] = t.struct(
        {
            "source": t.proxy(
                renames["GoogleCloudDatacatalogLineageV1EntityReferenceIn"]
            ).optional(),
            "pageToken": t.string().optional(),
            "target": t.proxy(
                renames["GoogleCloudDatacatalogLineageV1EntityReferenceIn"]
            ).optional(),
            "pageSize": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1SearchLinksRequestIn"])
    types["GoogleCloudDatacatalogLineageV1SearchLinksRequestOut"] = t.struct(
        {
            "source": t.proxy(
                renames["GoogleCloudDatacatalogLineageV1EntityReferenceOut"]
            ).optional(),
            "pageToken": t.string().optional(),
            "target": t.proxy(
                renames["GoogleCloudDatacatalogLineageV1EntityReferenceOut"]
            ).optional(),
            "pageSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1SearchLinksRequestOut"])
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
    types["GoogleCloudDatacatalogLineageV1ListProcessesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "processes": t.array(
                t.proxy(renames["GoogleCloudDatacatalogLineageV1ProcessIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1ListProcessesResponseIn"])
    types["GoogleCloudDatacatalogLineageV1ListProcessesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "processes": t.array(
                t.proxy(renames["GoogleCloudDatacatalogLineageV1ProcessOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1ListProcessesResponseOut"])
    types["GoogleCloudDatacatalogLineageV1LineageEventIn"] = t.struct(
        {
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "links": t.array(
                t.proxy(renames["GoogleCloudDatacatalogLineageV1EventLinkIn"])
            ).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1LineageEventIn"])
    types["GoogleCloudDatacatalogLineageV1LineageEventOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "links": t.array(
                t.proxy(renames["GoogleCloudDatacatalogLineageV1EventLinkOut"])
            ).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1LineageEventOut"])
    types[
        "GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesRequestIn"
    ] = t.struct(
        {
            "links": t.array(t.string()),
            "pageSize": t.integer().optional(),
            "pageToken": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesRequestIn"]
    )
    types[
        "GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesRequestOut"
    ] = t.struct(
        {
            "links": t.array(t.string()),
            "pageSize": t.integer().optional(),
            "pageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesRequestOut"]
    )
    types["GoogleLongrunningCancelOperationRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestIn"])
    types["GoogleLongrunningCancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestOut"])
    types["GoogleCloudDatacatalogLineageV1ProcessLinkInfoIn"] = t.struct(
        {
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "link": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1ProcessLinkInfoIn"])
    types["GoogleCloudDatacatalogLineageV1ProcessLinkInfoOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "link": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1ProcessLinkInfoOut"])
    types["GoogleCloudDatacatalogLineageV1OriginIn"] = t.struct(
        {"name": t.string().optional(), "sourceType": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogLineageV1OriginIn"])
    types["GoogleCloudDatacatalogLineageV1OriginOut"] = t.struct(
        {
            "name": t.string().optional(),
            "sourceType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1OriginOut"])
    types["GoogleCloudDatacatalogLineageV1ProcessLinksIn"] = t.struct(
        {
            "process": t.string().optional(),
            "links": t.array(
                t.proxy(renames["GoogleCloudDatacatalogLineageV1ProcessLinkInfoIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1ProcessLinksIn"])
    types["GoogleCloudDatacatalogLineageV1ProcessLinksOut"] = t.struct(
        {
            "process": t.string().optional(),
            "links": t.array(
                t.proxy(renames["GoogleCloudDatacatalogLineageV1ProcessLinkInfoOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1ProcessLinksOut"])
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

    functions = {}
    functions["projectsLocationsSearchLinks"] = datalineage.post(
        "v1/{parent}:batchSearchLinkProcesses",
        t.struct(
            {
                "parent": t.string(),
                "links": t.array(t.string()),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames[
                "GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBatchSearchLinkProcesses"] = datalineage.post(
        "v1/{parent}:batchSearchLinkProcesses",
        t.struct(
            {
                "parent": t.string(),
                "links": t.array(t.string()),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames[
                "GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = datalineage.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = datalineage.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = datalineage.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = datalineage.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
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
    functions["projectsLocationsProcessesRunsList"] = datalineage.post(
        "v1/{parent}/runs",
        t.struct(
            {
                "requestId": t.string().optional(),
                "parent": t.string(),
                "displayName": t.string().optional(),
                "attributes": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "state": t.string(),
                "endTime": t.string().optional(),
                "startTime": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogLineageV1RunOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessesRunsGet"] = datalineage.post(
        "v1/{parent}/runs",
        t.struct(
            {
                "requestId": t.string().optional(),
                "parent": t.string(),
                "displayName": t.string().optional(),
                "attributes": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "state": t.string(),
                "endTime": t.string().optional(),
                "startTime": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogLineageV1RunOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessesRunsPatch"] = datalineage.post(
        "v1/{parent}/runs",
        t.struct(
            {
                "requestId": t.string().optional(),
                "parent": t.string(),
                "displayName": t.string().optional(),
                "attributes": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "state": t.string(),
                "endTime": t.string().optional(),
                "startTime": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogLineageV1RunOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessesRunsDelete"] = datalineage.post(
        "v1/{parent}/runs",
        t.struct(
            {
                "requestId": t.string().optional(),
                "parent": t.string(),
                "displayName": t.string().optional(),
                "attributes": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "state": t.string(),
                "endTime": t.string().optional(),
                "startTime": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogLineageV1RunOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessesRunsCreate"] = datalineage.post(
        "v1/{parent}/runs",
        t.struct(
            {
                "requestId": t.string().optional(),
                "parent": t.string(),
                "displayName": t.string().optional(),
                "attributes": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "state": t.string(),
                "endTime": t.string().optional(),
                "startTime": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogLineageV1RunOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessesRunsLineageEventsList"] = datalineage.post(
        "v1/{parent}/lineageEvents",
        t.struct(
            {
                "parent": t.string(),
                "requestId": t.string().optional(),
                "startTime": t.string().optional(),
                "endTime": t.string().optional(),
                "links": t.array(
                    t.proxy(renames["GoogleCloudDatacatalogLineageV1EventLinkIn"])
                ).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogLineageV1LineageEventOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessesRunsLineageEventsDelete"] = datalineage.post(
        "v1/{parent}/lineageEvents",
        t.struct(
            {
                "parent": t.string(),
                "requestId": t.string().optional(),
                "startTime": t.string().optional(),
                "endTime": t.string().optional(),
                "links": t.array(
                    t.proxy(renames["GoogleCloudDatacatalogLineageV1EventLinkIn"])
                ).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogLineageV1LineageEventOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessesRunsLineageEventsGet"] = datalineage.post(
        "v1/{parent}/lineageEvents",
        t.struct(
            {
                "parent": t.string(),
                "requestId": t.string().optional(),
                "startTime": t.string().optional(),
                "endTime": t.string().optional(),
                "links": t.array(
                    t.proxy(renames["GoogleCloudDatacatalogLineageV1EventLinkIn"])
                ).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogLineageV1LineageEventOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessesRunsLineageEventsCreate"] = datalineage.post(
        "v1/{parent}/lineageEvents",
        t.struct(
            {
                "parent": t.string(),
                "requestId": t.string().optional(),
                "startTime": t.string().optional(),
                "endTime": t.string().optional(),
                "links": t.array(
                    t.proxy(renames["GoogleCloudDatacatalogLineageV1EventLinkIn"])
                ).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogLineageV1LineageEventOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="datalineage", renames=renames, types=types, functions=functions
    )
