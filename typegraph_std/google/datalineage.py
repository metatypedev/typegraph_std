from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_datalineage():
    datalineage = HTTPRuntime("https://datalineage.googleapis.com/")

    renames = {
        "ErrorResponse": "_datalineage_1_ErrorResponse",
        "GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesResponseIn": "_datalineage_2_GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesResponseIn",
        "GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesResponseOut": "_datalineage_3_GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesResponseOut",
        "GoogleCloudDatacatalogLineageV1OriginIn": "_datalineage_4_GoogleCloudDatacatalogLineageV1OriginIn",
        "GoogleCloudDatacatalogLineageV1OriginOut": "_datalineage_5_GoogleCloudDatacatalogLineageV1OriginOut",
        "GoogleCloudDatacatalogLineageV1EntityReferenceIn": "_datalineage_6_GoogleCloudDatacatalogLineageV1EntityReferenceIn",
        "GoogleCloudDatacatalogLineageV1EntityReferenceOut": "_datalineage_7_GoogleCloudDatacatalogLineageV1EntityReferenceOut",
        "GoogleCloudDatacatalogLineageV1SearchLinksRequestIn": "_datalineage_8_GoogleCloudDatacatalogLineageV1SearchLinksRequestIn",
        "GoogleCloudDatacatalogLineageV1SearchLinksRequestOut": "_datalineage_9_GoogleCloudDatacatalogLineageV1SearchLinksRequestOut",
        "GoogleCloudDatacatalogLineageV1ListRunsResponseIn": "_datalineage_10_GoogleCloudDatacatalogLineageV1ListRunsResponseIn",
        "GoogleCloudDatacatalogLineageV1ListRunsResponseOut": "_datalineage_11_GoogleCloudDatacatalogLineageV1ListRunsResponseOut",
        "GoogleCloudDatacatalogLineageV1LineageEventIn": "_datalineage_12_GoogleCloudDatacatalogLineageV1LineageEventIn",
        "GoogleCloudDatacatalogLineageV1LineageEventOut": "_datalineage_13_GoogleCloudDatacatalogLineageV1LineageEventOut",
        "GoogleCloudDatacatalogLineageV1EventLinkIn": "_datalineage_14_GoogleCloudDatacatalogLineageV1EventLinkIn",
        "GoogleCloudDatacatalogLineageV1EventLinkOut": "_datalineage_15_GoogleCloudDatacatalogLineageV1EventLinkOut",
        "GoogleCloudDatacatalogLineageV1ProcessIn": "_datalineage_16_GoogleCloudDatacatalogLineageV1ProcessIn",
        "GoogleCloudDatacatalogLineageV1ProcessOut": "_datalineage_17_GoogleCloudDatacatalogLineageV1ProcessOut",
        "GoogleLongrunningCancelOperationRequestIn": "_datalineage_18_GoogleLongrunningCancelOperationRequestIn",
        "GoogleLongrunningCancelOperationRequestOut": "_datalineage_19_GoogleLongrunningCancelOperationRequestOut",
        "GoogleCloudDatacatalogLineageV1LinkIn": "_datalineage_20_GoogleCloudDatacatalogLineageV1LinkIn",
        "GoogleCloudDatacatalogLineageV1LinkOut": "_datalineage_21_GoogleCloudDatacatalogLineageV1LinkOut",
        "GoogleLongrunningOperationIn": "_datalineage_22_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_datalineage_23_GoogleLongrunningOperationOut",
        "GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesRequestIn": "_datalineage_24_GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesRequestIn",
        "GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesRequestOut": "_datalineage_25_GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesRequestOut",
        "GoogleCloudDatacatalogLineageV1ProcessLinkInfoIn": "_datalineage_26_GoogleCloudDatacatalogLineageV1ProcessLinkInfoIn",
        "GoogleCloudDatacatalogLineageV1ProcessLinkInfoOut": "_datalineage_27_GoogleCloudDatacatalogLineageV1ProcessLinkInfoOut",
        "GoogleProtobufEmptyIn": "_datalineage_28_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_datalineage_29_GoogleProtobufEmptyOut",
        "GoogleCloudDatacatalogLineageV1ProcessLinksIn": "_datalineage_30_GoogleCloudDatacatalogLineageV1ProcessLinksIn",
        "GoogleCloudDatacatalogLineageV1ProcessLinksOut": "_datalineage_31_GoogleCloudDatacatalogLineageV1ProcessLinksOut",
        "GoogleLongrunningListOperationsResponseIn": "_datalineage_32_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_datalineage_33_GoogleLongrunningListOperationsResponseOut",
        "GoogleCloudDatacatalogLineageV1ListLineageEventsResponseIn": "_datalineage_34_GoogleCloudDatacatalogLineageV1ListLineageEventsResponseIn",
        "GoogleCloudDatacatalogLineageV1ListLineageEventsResponseOut": "_datalineage_35_GoogleCloudDatacatalogLineageV1ListLineageEventsResponseOut",
        "GoogleCloudDatacatalogLineageV1ListProcessesResponseIn": "_datalineage_36_GoogleCloudDatacatalogLineageV1ListProcessesResponseIn",
        "GoogleCloudDatacatalogLineageV1ListProcessesResponseOut": "_datalineage_37_GoogleCloudDatacatalogLineageV1ListProcessesResponseOut",
        "GoogleRpcStatusIn": "_datalineage_38_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_datalineage_39_GoogleRpcStatusOut",
        "GoogleCloudDatacatalogLineageV1SearchLinksResponseIn": "_datalineage_40_GoogleCloudDatacatalogLineageV1SearchLinksResponseIn",
        "GoogleCloudDatacatalogLineageV1SearchLinksResponseOut": "_datalineage_41_GoogleCloudDatacatalogLineageV1SearchLinksResponseOut",
        "GoogleCloudDatacatalogLineageV1RunIn": "_datalineage_42_GoogleCloudDatacatalogLineageV1RunIn",
        "GoogleCloudDatacatalogLineageV1RunOut": "_datalineage_43_GoogleCloudDatacatalogLineageV1RunOut",
        "GoogleCloudDatacatalogLineageV1OperationMetadataIn": "_datalineage_44_GoogleCloudDatacatalogLineageV1OperationMetadataIn",
        "GoogleCloudDatacatalogLineageV1OperationMetadataOut": "_datalineage_45_GoogleCloudDatacatalogLineageV1OperationMetadataOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["GoogleCloudDatacatalogLineageV1EntityReferenceIn"] = t.struct(
        {"fullyQualifiedName": t.string()}
    ).named(renames["GoogleCloudDatacatalogLineageV1EntityReferenceIn"])
    types["GoogleCloudDatacatalogLineageV1EntityReferenceOut"] = t.struct(
        {
            "fullyQualifiedName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1EntityReferenceOut"])
    types["GoogleCloudDatacatalogLineageV1SearchLinksRequestIn"] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "target": t.proxy(
                renames["GoogleCloudDatacatalogLineageV1EntityReferenceIn"]
            ).optional(),
            "source": t.proxy(
                renames["GoogleCloudDatacatalogLineageV1EntityReferenceIn"]
            ).optional(),
            "pageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1SearchLinksRequestIn"])
    types["GoogleCloudDatacatalogLineageV1SearchLinksRequestOut"] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "target": t.proxy(
                renames["GoogleCloudDatacatalogLineageV1EntityReferenceOut"]
            ).optional(),
            "source": t.proxy(
                renames["GoogleCloudDatacatalogLineageV1EntityReferenceOut"]
            ).optional(),
            "pageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1SearchLinksRequestOut"])
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
    types["GoogleCloudDatacatalogLineageV1LineageEventIn"] = t.struct(
        {
            "startTime": t.string().optional(),
            "name": t.string().optional(),
            "links": t.array(
                t.proxy(renames["GoogleCloudDatacatalogLineageV1EventLinkIn"])
            ).optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1LineageEventIn"])
    types["GoogleCloudDatacatalogLineageV1LineageEventOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "name": t.string().optional(),
            "links": t.array(
                t.proxy(renames["GoogleCloudDatacatalogLineageV1EventLinkOut"])
            ).optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1LineageEventOut"])
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
    types["GoogleCloudDatacatalogLineageV1ProcessIn"] = t.struct(
        {
            "origin": t.proxy(
                renames["GoogleCloudDatacatalogLineageV1OriginIn"]
            ).optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1ProcessIn"])
    types["GoogleCloudDatacatalogLineageV1ProcessOut"] = t.struct(
        {
            "origin": t.proxy(
                renames["GoogleCloudDatacatalogLineageV1OriginOut"]
            ).optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1ProcessOut"])
    types["GoogleLongrunningCancelOperationRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestIn"])
    types["GoogleLongrunningCancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestOut"])
    types["GoogleCloudDatacatalogLineageV1LinkIn"] = t.struct(
        {
            "source": t.proxy(
                renames["GoogleCloudDatacatalogLineageV1EntityReferenceIn"]
            ).optional(),
            "startTime": t.string().optional(),
            "target": t.proxy(
                renames["GoogleCloudDatacatalogLineageV1EntityReferenceIn"]
            ).optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1LinkIn"])
    types["GoogleCloudDatacatalogLineageV1LinkOut"] = t.struct(
        {
            "name": t.string().optional(),
            "source": t.proxy(
                renames["GoogleCloudDatacatalogLineageV1EntityReferenceOut"]
            ).optional(),
            "startTime": t.string().optional(),
            "target": t.proxy(
                renames["GoogleCloudDatacatalogLineageV1EntityReferenceOut"]
            ).optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1LinkOut"])
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
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
    types["GoogleCloudDatacatalogLineageV1ProcessLinkInfoIn"] = t.struct(
        {
            "link": t.string().optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1ProcessLinkInfoIn"])
    types["GoogleCloudDatacatalogLineageV1ProcessLinkInfoOut"] = t.struct(
        {
            "link": t.string().optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1ProcessLinkInfoOut"])
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
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
    types["GoogleLongrunningListOperationsResponseIn"] = t.struct(
        {
            "operations": t.array(
                t.proxy(renames["GoogleLongrunningOperationIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleLongrunningListOperationsResponseIn"])
    types["GoogleLongrunningListOperationsResponseOut"] = t.struct(
        {
            "operations": t.array(
                t.proxy(renames["GoogleLongrunningOperationOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleLongrunningListOperationsResponseOut"])
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
    types["GoogleRpcStatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["GoogleRpcStatusIn"])
    types["GoogleRpcStatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleRpcStatusOut"])
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
    types["GoogleCloudDatacatalogLineageV1RunIn"] = t.struct(
        {
            "state": t.string(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "startTime": t.string(),
            "endTime": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1RunIn"])
    types["GoogleCloudDatacatalogLineageV1RunOut"] = t.struct(
        {
            "state": t.string(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "startTime": t.string(),
            "endTime": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1RunOut"])
    types["GoogleCloudDatacatalogLineageV1OperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogLineageV1OperationMetadataIn"])
    types["GoogleCloudDatacatalogLineageV1OperationMetadataOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "resourceUuid": t.string().optional(),
            "createTime": t.string().optional(),
            "operationType": t.string().optional(),
            "resource": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogLineageV1OperationMetadataOut"])

    functions = {}
    functions["projectsLocationsBatchSearchLinkProcesses"] = datalineage.post(
        "v1/{parent}:searchLinks",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "target": t.proxy(
                    renames["GoogleCloudDatacatalogLineageV1EntityReferenceIn"]
                ).optional(),
                "source": t.proxy(
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
                "target": t.proxy(
                    renames["GoogleCloudDatacatalogLineageV1EntityReferenceIn"]
                ).optional(),
                "source": t.proxy(
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
    functions["projectsLocationsOperationsCancel"] = datalineage.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = datalineage.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = datalineage.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = datalineage.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessesDelete"] = datalineage.post(
        "v1/{parent}/processes",
        t.struct(
            {
                "parent": t.string(),
                "requestId": t.string().optional(),
                "origin": t.proxy(
                    renames["GoogleCloudDatacatalogLineageV1OriginIn"]
                ).optional(),
                "attributes": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogLineageV1ProcessOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessesPatch"] = datalineage.post(
        "v1/{parent}/processes",
        t.struct(
            {
                "parent": t.string(),
                "requestId": t.string().optional(),
                "origin": t.proxy(
                    renames["GoogleCloudDatacatalogLineageV1OriginIn"]
                ).optional(),
                "attributes": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogLineageV1ProcessOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessesGet"] = datalineage.post(
        "v1/{parent}/processes",
        t.struct(
            {
                "parent": t.string(),
                "requestId": t.string().optional(),
                "origin": t.proxy(
                    renames["GoogleCloudDatacatalogLineageV1OriginIn"]
                ).optional(),
                "attributes": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogLineageV1ProcessOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessesList"] = datalineage.post(
        "v1/{parent}/processes",
        t.struct(
            {
                "parent": t.string(),
                "requestId": t.string().optional(),
                "origin": t.proxy(
                    renames["GoogleCloudDatacatalogLineageV1OriginIn"]
                ).optional(),
                "attributes": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogLineageV1ProcessOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessesCreate"] = datalineage.post(
        "v1/{parent}/processes",
        t.struct(
            {
                "parent": t.string(),
                "requestId": t.string().optional(),
                "origin": t.proxy(
                    renames["GoogleCloudDatacatalogLineageV1OriginIn"]
                ).optional(),
                "attributes": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogLineageV1ProcessOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessesRunsDelete"] = datalineage.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDatacatalogLineageV1RunOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessesRunsPatch"] = datalineage.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDatacatalogLineageV1RunOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessesRunsCreate"] = datalineage.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDatacatalogLineageV1RunOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessesRunsList"] = datalineage.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDatacatalogLineageV1RunOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessesRunsGet"] = datalineage.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDatacatalogLineageV1RunOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessesRunsLineageEventsCreate"] = datalineage.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "allowMissing": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessesRunsLineageEventsGet"] = datalineage.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "allowMissing": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessesRunsLineageEventsList"] = datalineage.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "allowMissing": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessesRunsLineageEventsDelete"] = datalineage.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "allowMissing": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="datalineage",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
