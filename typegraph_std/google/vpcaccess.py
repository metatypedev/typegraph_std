from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_vpcaccess() -> Import:
    vpcaccess = HTTPRuntime("https://vpcaccess.googleapis.com/")

    renames = {
        "ErrorResponse": "_vpcaccess_1_ErrorResponse",
        "ListLocationsResponseIn": "_vpcaccess_2_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_vpcaccess_3_ListLocationsResponseOut",
        "LocationIn": "_vpcaccess_4_LocationIn",
        "LocationOut": "_vpcaccess_5_LocationOut",
        "ListOperationsResponseIn": "_vpcaccess_6_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_vpcaccess_7_ListOperationsResponseOut",
        "OperationIn": "_vpcaccess_8_OperationIn",
        "OperationOut": "_vpcaccess_9_OperationOut",
        "StatusIn": "_vpcaccess_10_StatusIn",
        "StatusOut": "_vpcaccess_11_StatusOut",
        "ConnectorIn": "_vpcaccess_12_ConnectorIn",
        "ConnectorOut": "_vpcaccess_13_ConnectorOut",
        "SubnetIn": "_vpcaccess_14_SubnetIn",
        "SubnetOut": "_vpcaccess_15_SubnetOut",
        "ListConnectorsResponseIn": "_vpcaccess_16_ListConnectorsResponseIn",
        "ListConnectorsResponseOut": "_vpcaccess_17_ListConnectorsResponseOut",
        "OperationMetadataV1Alpha1In": "_vpcaccess_18_OperationMetadataV1Alpha1In",
        "OperationMetadataV1Alpha1Out": "_vpcaccess_19_OperationMetadataV1Alpha1Out",
        "OperationMetadataV1Beta1In": "_vpcaccess_20_OperationMetadataV1Beta1In",
        "OperationMetadataV1Beta1Out": "_vpcaccess_21_OperationMetadataV1Beta1Out",
        "OperationMetadataIn": "_vpcaccess_22_OperationMetadataIn",
        "OperationMetadataOut": "_vpcaccess_23_OperationMetadataOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["LocationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
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
    types["OperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
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
    types["ConnectorIn"] = t.struct(
        {
            "name": t.string().optional(),
            "network": t.string().optional(),
            "ipCidrRange": t.string().optional(),
            "minThroughput": t.integer().optional(),
            "maxThroughput": t.integer().optional(),
            "subnet": t.proxy(renames["SubnetIn"]).optional(),
            "machineType": t.string().optional(),
            "minInstances": t.integer().optional(),
            "maxInstances": t.integer().optional(),
        }
    ).named(renames["ConnectorIn"])
    types["ConnectorOut"] = t.struct(
        {
            "name": t.string().optional(),
            "network": t.string().optional(),
            "ipCidrRange": t.string().optional(),
            "state": t.string().optional(),
            "minThroughput": t.integer().optional(),
            "maxThroughput": t.integer().optional(),
            "connectedProjects": t.array(t.string()).optional(),
            "subnet": t.proxy(renames["SubnetOut"]).optional(),
            "machineType": t.string().optional(),
            "minInstances": t.integer().optional(),
            "maxInstances": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConnectorOut"])
    types["SubnetIn"] = t.struct(
        {"name": t.string().optional(), "projectId": t.string().optional()}
    ).named(renames["SubnetIn"])
    types["SubnetOut"] = t.struct(
        {
            "name": t.string().optional(),
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubnetOut"])
    types["ListConnectorsResponseIn"] = t.struct(
        {
            "connectors": t.array(t.proxy(renames["ConnectorIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListConnectorsResponseIn"])
    types["ListConnectorsResponseOut"] = t.struct(
        {
            "connectors": t.array(t.proxy(renames["ConnectorOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListConnectorsResponseOut"])
    types["OperationMetadataV1Alpha1In"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataV1Alpha1In"]
    )
    types["OperationMetadataV1Alpha1Out"] = t.struct(
        {
            "method": t.string().optional(),
            "insertTime": t.string().optional(),
            "endTime": t.string().optional(),
            "target": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataV1Alpha1Out"])
    types["OperationMetadataV1Beta1In"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataV1Beta1In"]
    )
    types["OperationMetadataV1Beta1Out"] = t.struct(
        {
            "method": t.string().optional(),
            "createTime": t.string().optional(),
            "endTime": t.string().optional(),
            "target": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataV1Beta1Out"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "method": t.string().optional(),
            "createTime": t.string().optional(),
            "endTime": t.string().optional(),
            "target": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])

    functions = {}
    functions["projectsLocationsList"] = vpcaccess.get(
        "v1/{name}/locations",
        t.struct(
            {
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = vpcaccess.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = vpcaccess.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectorsCreate"] = vpcaccess.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectorsPatch"] = vpcaccess.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectorsGet"] = vpcaccess.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectorsList"] = vpcaccess.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectorsDelete"] = vpcaccess.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="vpcaccess", renames=renames, types=types, functions=functions
    )
