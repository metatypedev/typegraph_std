from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_vpcaccess():
    vpcaccess = HTTPRuntime("https://vpcaccess.googleapis.com/")

    renames = {
        "ErrorResponse": "_vpcaccess_1_ErrorResponse",
        "ListLocationsResponseIn": "_vpcaccess_2_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_vpcaccess_3_ListLocationsResponseOut",
        "OperationMetadataV1Beta1In": "_vpcaccess_4_OperationMetadataV1Beta1In",
        "OperationMetadataV1Beta1Out": "_vpcaccess_5_OperationMetadataV1Beta1Out",
        "LocationIn": "_vpcaccess_6_LocationIn",
        "LocationOut": "_vpcaccess_7_LocationOut",
        "ConnectorIn": "_vpcaccess_8_ConnectorIn",
        "ConnectorOut": "_vpcaccess_9_ConnectorOut",
        "StatusIn": "_vpcaccess_10_StatusIn",
        "StatusOut": "_vpcaccess_11_StatusOut",
        "OperationMetadataIn": "_vpcaccess_12_OperationMetadataIn",
        "OperationMetadataOut": "_vpcaccess_13_OperationMetadataOut",
        "OperationIn": "_vpcaccess_14_OperationIn",
        "OperationOut": "_vpcaccess_15_OperationOut",
        "ListOperationsResponseIn": "_vpcaccess_16_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_vpcaccess_17_ListOperationsResponseOut",
        "SubnetIn": "_vpcaccess_18_SubnetIn",
        "SubnetOut": "_vpcaccess_19_SubnetOut",
        "ListConnectorsResponseIn": "_vpcaccess_20_ListConnectorsResponseIn",
        "ListConnectorsResponseOut": "_vpcaccess_21_ListConnectorsResponseOut",
        "OperationMetadataV1Alpha1In": "_vpcaccess_22_OperationMetadataV1Alpha1In",
        "OperationMetadataV1Alpha1Out": "_vpcaccess_23_OperationMetadataV1Alpha1Out",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["OperationMetadataV1Beta1In"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataV1Beta1In"]
    )
    types["OperationMetadataV1Beta1Out"] = t.struct(
        {
            "target": t.string().optional(),
            "endTime": t.string().optional(),
            "method": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataV1Beta1Out"])
    types["LocationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["ConnectorIn"] = t.struct(
        {
            "ipCidrRange": t.string().optional(),
            "name": t.string().optional(),
            "maxInstances": t.integer().optional(),
            "network": t.string().optional(),
            "minInstances": t.integer().optional(),
            "minThroughput": t.integer().optional(),
            "subnet": t.proxy(renames["SubnetIn"]).optional(),
            "maxThroughput": t.integer().optional(),
            "machineType": t.string().optional(),
        }
    ).named(renames["ConnectorIn"])
    types["ConnectorOut"] = t.struct(
        {
            "ipCidrRange": t.string().optional(),
            "name": t.string().optional(),
            "maxInstances": t.integer().optional(),
            "network": t.string().optional(),
            "minInstances": t.integer().optional(),
            "minThroughput": t.integer().optional(),
            "subnet": t.proxy(renames["SubnetOut"]).optional(),
            "state": t.string().optional(),
            "maxThroughput": t.integer().optional(),
            "machineType": t.string().optional(),
            "connectedProjects": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConnectorOut"])
    types["StatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "target": t.string().optional(),
            "createTime": t.string().optional(),
            "method": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["OperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
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
            "target": t.string().optional(),
            "insertTime": t.string().optional(),
            "endTime": t.string().optional(),
            "method": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataV1Alpha1Out"])

    functions = {}
    functions["projectsLocationsList"] = vpcaccess.get(
        "v1/{name}/locations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
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
    functions["projectsLocationsConnectorsList"] = vpcaccess.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
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
    functions["projectsLocationsConnectorsGet"] = vpcaccess.delete(
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
    functions["projectsLocationsOperationsGet"] = vpcaccess.get(
        "v1/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = vpcaccess.get(
        "v1/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="vpcaccess",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
