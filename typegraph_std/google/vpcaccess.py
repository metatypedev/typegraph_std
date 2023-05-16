from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_vpcaccess() -> Import:
    vpcaccess = HTTPRuntime("https://vpcaccess.googleapis.com/")

    renames = {
        "ErrorResponse": "_vpcaccess_1_ErrorResponse",
        "ConnectorIn": "_vpcaccess_2_ConnectorIn",
        "ConnectorOut": "_vpcaccess_3_ConnectorOut",
        "OperationIn": "_vpcaccess_4_OperationIn",
        "OperationOut": "_vpcaccess_5_OperationOut",
        "ListLocationsResponseIn": "_vpcaccess_6_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_vpcaccess_7_ListLocationsResponseOut",
        "OperationMetadataIn": "_vpcaccess_8_OperationMetadataIn",
        "OperationMetadataOut": "_vpcaccess_9_OperationMetadataOut",
        "SubnetIn": "_vpcaccess_10_SubnetIn",
        "SubnetOut": "_vpcaccess_11_SubnetOut",
        "OperationMetadataV1Alpha1In": "_vpcaccess_12_OperationMetadataV1Alpha1In",
        "OperationMetadataV1Alpha1Out": "_vpcaccess_13_OperationMetadataV1Alpha1Out",
        "OperationMetadataV1Beta1In": "_vpcaccess_14_OperationMetadataV1Beta1In",
        "OperationMetadataV1Beta1Out": "_vpcaccess_15_OperationMetadataV1Beta1Out",
        "ListOperationsResponseIn": "_vpcaccess_16_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_vpcaccess_17_ListOperationsResponseOut",
        "LocationIn": "_vpcaccess_18_LocationIn",
        "LocationOut": "_vpcaccess_19_LocationOut",
        "ListConnectorsResponseIn": "_vpcaccess_20_ListConnectorsResponseIn",
        "ListConnectorsResponseOut": "_vpcaccess_21_ListConnectorsResponseOut",
        "StatusIn": "_vpcaccess_22_StatusIn",
        "StatusOut": "_vpcaccess_23_StatusOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ConnectorIn"] = t.struct(
        {
            "minInstances": t.integer().optional(),
            "maxInstances": t.integer().optional(),
            "network": t.string().optional(),
            "machineType": t.string().optional(),
            "ipCidrRange": t.string().optional(),
            "minThroughput": t.integer().optional(),
            "name": t.string().optional(),
            "maxThroughput": t.integer().optional(),
            "subnet": t.proxy(renames["SubnetIn"]).optional(),
        }
    ).named(renames["ConnectorIn"])
    types["ConnectorOut"] = t.struct(
        {
            "minInstances": t.integer().optional(),
            "maxInstances": t.integer().optional(),
            "network": t.string().optional(),
            "machineType": t.string().optional(),
            "ipCidrRange": t.string().optional(),
            "state": t.string().optional(),
            "minThroughput": t.integer().optional(),
            "name": t.string().optional(),
            "connectedProjects": t.array(t.string()).optional(),
            "maxThroughput": t.integer().optional(),
            "subnet": t.proxy(renames["SubnetOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConnectorOut"])
    types["OperationIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationOut"])
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
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "target": t.string().optional(),
            "method": t.string().optional(),
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["SubnetIn"] = t.struct(
        {"projectId": t.string().optional(), "name": t.string().optional()}
    ).named(renames["SubnetIn"])
    types["SubnetOut"] = t.struct(
        {
            "projectId": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubnetOut"])
    types["OperationMetadataV1Alpha1In"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataV1Alpha1In"]
    )
    types["OperationMetadataV1Alpha1Out"] = t.struct(
        {
            "method": t.string().optional(),
            "target": t.string().optional(),
            "insertTime": t.string().optional(),
            "endTime": t.string().optional(),
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
    types["LocationIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
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
    types["StatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])

    functions = {}
    functions["projectsLocationsList"] = vpcaccess.get(
        "v1/{name}/locations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
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
    functions["projectsLocationsConnectorsGet"] = vpcaccess.delete(
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
    functions["projectsLocationsConnectorsDelete"] = vpcaccess.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="vpcaccess",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
