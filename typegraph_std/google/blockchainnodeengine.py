from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_blockchainnodeengine():
    blockchainnodeengine = HTTPRuntime("https://blockchainnodeengine.googleapis.com/")

    renames = {
        "ErrorResponse": "_blockchainnodeengine_1_ErrorResponse",
        "EthereumEndpointsIn": "_blockchainnodeengine_2_EthereumEndpointsIn",
        "EthereumEndpointsOut": "_blockchainnodeengine_3_EthereumEndpointsOut",
        "CancelOperationRequestIn": "_blockchainnodeengine_4_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_blockchainnodeengine_5_CancelOperationRequestOut",
        "BlockchainNodeIn": "_blockchainnodeengine_6_BlockchainNodeIn",
        "BlockchainNodeOut": "_blockchainnodeengine_7_BlockchainNodeOut",
        "LocationIn": "_blockchainnodeengine_8_LocationIn",
        "LocationOut": "_blockchainnodeengine_9_LocationOut",
        "StatusIn": "_blockchainnodeengine_10_StatusIn",
        "StatusOut": "_blockchainnodeengine_11_StatusOut",
        "GethDetailsIn": "_blockchainnodeengine_12_GethDetailsIn",
        "GethDetailsOut": "_blockchainnodeengine_13_GethDetailsOut",
        "OperationIn": "_blockchainnodeengine_14_OperationIn",
        "OperationOut": "_blockchainnodeengine_15_OperationOut",
        "ListOperationsResponseIn": "_blockchainnodeengine_16_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_blockchainnodeengine_17_ListOperationsResponseOut",
        "ListBlockchainNodesResponseIn": "_blockchainnodeengine_18_ListBlockchainNodesResponseIn",
        "ListBlockchainNodesResponseOut": "_blockchainnodeengine_19_ListBlockchainNodesResponseOut",
        "EndpointInfoIn": "_blockchainnodeengine_20_EndpointInfoIn",
        "EndpointInfoOut": "_blockchainnodeengine_21_EndpointInfoOut",
        "GoogleProtobufEmptyIn": "_blockchainnodeengine_22_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_blockchainnodeengine_23_GoogleProtobufEmptyOut",
        "OperationMetadataIn": "_blockchainnodeengine_24_OperationMetadataIn",
        "OperationMetadataOut": "_blockchainnodeengine_25_OperationMetadataOut",
        "EthereumDetailsIn": "_blockchainnodeengine_26_EthereumDetailsIn",
        "EthereumDetailsOut": "_blockchainnodeengine_27_EthereumDetailsOut",
        "ListLocationsResponseIn": "_blockchainnodeengine_28_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_blockchainnodeengine_29_ListLocationsResponseOut",
        "ConnectionInfoIn": "_blockchainnodeengine_30_ConnectionInfoIn",
        "ConnectionInfoOut": "_blockchainnodeengine_31_ConnectionInfoOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["EthereumEndpointsIn"] = t.struct({"_": t.string().optional()}).named(
        renames["EthereumEndpointsIn"]
    )
    types["EthereumEndpointsOut"] = t.struct(
        {
            "executionClientPrometheusMetricsApiEndpoint": t.string().optional(),
            "beaconPrometheusMetricsApiEndpoint": t.string().optional(),
            "beaconApiEndpoint": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EthereumEndpointsOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["BlockchainNodeIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "ethereumDetails": t.proxy(renames["EthereumDetailsIn"]).optional(),
            "blockchainType": t.string().optional(),
        }
    ).named(renames["BlockchainNodeIn"])
    types["BlockchainNodeOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "ethereumDetails": t.proxy(renames["EthereumDetailsOut"]).optional(),
            "createTime": t.string().optional(),
            "blockchainType": t.string().optional(),
            "connectionInfo": t.proxy(renames["ConnectionInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BlockchainNodeOut"])
    types["LocationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
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
    types["GethDetailsIn"] = t.struct(
        {"garbageCollectionMode": t.string().optional()}
    ).named(renames["GethDetailsIn"])
    types["GethDetailsOut"] = t.struct(
        {
            "garbageCollectionMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GethDetailsOut"])
    types["OperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
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
    types["ListBlockchainNodesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "blockchainNodes": t.array(t.proxy(renames["BlockchainNodeIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListBlockchainNodesResponseIn"])
    types["ListBlockchainNodesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "blockchainNodes": t.array(
                t.proxy(renames["BlockchainNodeOut"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBlockchainNodesResponseOut"])
    types["EndpointInfoIn"] = t.struct({"_": t.string().optional()}).named(
        renames["EndpointInfoIn"]
    )
    types["EndpointInfoOut"] = t.struct(
        {
            "jsonRpcApiEndpoint": t.string().optional(),
            "websocketsApiEndpoint": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EndpointInfoOut"])
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "statusMessage": t.string().optional(),
            "createTime": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "verb": t.string().optional(),
            "target": t.string().optional(),
            "apiVersion": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["EthereumDetailsIn"] = t.struct(
        {
            "gethDetails": t.proxy(renames["GethDetailsIn"]).optional(),
            "apiEnableAdmin": t.boolean().optional(),
            "network": t.string().optional(),
            "apiEnableDebug": t.boolean().optional(),
            "executionClient": t.string().optional(),
            "consensusClient": t.string().optional(),
            "nodeType": t.string().optional(),
        }
    ).named(renames["EthereumDetailsIn"])
    types["EthereumDetailsOut"] = t.struct(
        {
            "gethDetails": t.proxy(renames["GethDetailsOut"]).optional(),
            "apiEnableAdmin": t.boolean().optional(),
            "network": t.string().optional(),
            "apiEnableDebug": t.boolean().optional(),
            "executionClient": t.string().optional(),
            "additionalEndpoints": t.proxy(renames["EthereumEndpointsOut"]).optional(),
            "consensusClient": t.string().optional(),
            "nodeType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EthereumDetailsOut"])
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
    types["ConnectionInfoIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ConnectionInfoIn"]
    )
    types["ConnectionInfoOut"] = t.struct(
        {
            "endpointInfo": t.proxy(renames["EndpointInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConnectionInfoOut"])

    functions = {}
    functions["projectsLocationsList"] = blockchainnodeengine.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = blockchainnodeengine.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBlockchainNodesPatch"] = blockchainnodeengine.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BlockchainNodeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBlockchainNodesCreate"] = blockchainnodeengine.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BlockchainNodeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBlockchainNodesDelete"] = blockchainnodeengine.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BlockchainNodeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBlockchainNodesList"] = blockchainnodeengine.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BlockchainNodeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBlockchainNodesGet"] = blockchainnodeengine.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BlockchainNodeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = blockchainnodeengine.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = blockchainnodeengine.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = blockchainnodeengine.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = blockchainnodeengine.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="blockchainnodeengine",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
