from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_tpu() -> Import:
    tpu = HTTPRuntime("https://tpu.googleapis.com/")

    renames = {
        "ErrorResponse": "_tpu_1_ErrorResponse",
        "SymptomIn": "_tpu_2_SymptomIn",
        "SymptomOut": "_tpu_3_SymptomOut",
        "AcceleratorConfigIn": "_tpu_4_AcceleratorConfigIn",
        "AcceleratorConfigOut": "_tpu_5_AcceleratorConfigOut",
        "GuestAttributesValueIn": "_tpu_6_GuestAttributesValueIn",
        "GuestAttributesValueOut": "_tpu_7_GuestAttributesValueOut",
        "GenerateServiceIdentityRequestIn": "_tpu_8_GenerateServiceIdentityRequestIn",
        "GenerateServiceIdentityRequestOut": "_tpu_9_GenerateServiceIdentityRequestOut",
        "ServiceAccountIn": "_tpu_10_ServiceAccountIn",
        "ServiceAccountOut": "_tpu_11_ServiceAccountOut",
        "ListOperationsResponseIn": "_tpu_12_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_tpu_13_ListOperationsResponseOut",
        "NetworkEndpointIn": "_tpu_14_NetworkEndpointIn",
        "NetworkEndpointOut": "_tpu_15_NetworkEndpointOut",
        "ListLocationsResponseIn": "_tpu_16_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_tpu_17_ListLocationsResponseOut",
        "ListAcceleratorTypesResponseIn": "_tpu_18_ListAcceleratorTypesResponseIn",
        "ListAcceleratorTypesResponseOut": "_tpu_19_ListAcceleratorTypesResponseOut",
        "AttachedDiskIn": "_tpu_20_AttachedDiskIn",
        "AttachedDiskOut": "_tpu_21_AttachedDiskOut",
        "StatusIn": "_tpu_22_StatusIn",
        "StatusOut": "_tpu_23_StatusOut",
        "StopNodeRequestIn": "_tpu_24_StopNodeRequestIn",
        "StopNodeRequestOut": "_tpu_25_StopNodeRequestOut",
        "EmptyIn": "_tpu_26_EmptyIn",
        "EmptyOut": "_tpu_27_EmptyOut",
        "GuestAttributesEntryIn": "_tpu_28_GuestAttributesEntryIn",
        "GuestAttributesEntryOut": "_tpu_29_GuestAttributesEntryOut",
        "AccessConfigIn": "_tpu_30_AccessConfigIn",
        "AccessConfigOut": "_tpu_31_AccessConfigOut",
        "SchedulingConfigIn": "_tpu_32_SchedulingConfigIn",
        "SchedulingConfigOut": "_tpu_33_SchedulingConfigOut",
        "OperationMetadataIn": "_tpu_34_OperationMetadataIn",
        "OperationMetadataOut": "_tpu_35_OperationMetadataOut",
        "StartNodeRequestIn": "_tpu_36_StartNodeRequestIn",
        "StartNodeRequestOut": "_tpu_37_StartNodeRequestOut",
        "AcceleratorTypeIn": "_tpu_38_AcceleratorTypeIn",
        "AcceleratorTypeOut": "_tpu_39_AcceleratorTypeOut",
        "ListRuntimeVersionsResponseIn": "_tpu_40_ListRuntimeVersionsResponseIn",
        "ListRuntimeVersionsResponseOut": "_tpu_41_ListRuntimeVersionsResponseOut",
        "GuestAttributesIn": "_tpu_42_GuestAttributesIn",
        "GuestAttributesOut": "_tpu_43_GuestAttributesOut",
        "NetworkConfigIn": "_tpu_44_NetworkConfigIn",
        "NetworkConfigOut": "_tpu_45_NetworkConfigOut",
        "OperationIn": "_tpu_46_OperationIn",
        "OperationOut": "_tpu_47_OperationOut",
        "GetGuestAttributesResponseIn": "_tpu_48_GetGuestAttributesResponseIn",
        "GetGuestAttributesResponseOut": "_tpu_49_GetGuestAttributesResponseOut",
        "GetGuestAttributesRequestIn": "_tpu_50_GetGuestAttributesRequestIn",
        "GetGuestAttributesRequestOut": "_tpu_51_GetGuestAttributesRequestOut",
        "GenerateServiceIdentityResponseIn": "_tpu_52_GenerateServiceIdentityResponseIn",
        "GenerateServiceIdentityResponseOut": "_tpu_53_GenerateServiceIdentityResponseOut",
        "ServiceIdentityIn": "_tpu_54_ServiceIdentityIn",
        "ServiceIdentityOut": "_tpu_55_ServiceIdentityOut",
        "NodeIn": "_tpu_56_NodeIn",
        "NodeOut": "_tpu_57_NodeOut",
        "RuntimeVersionIn": "_tpu_58_RuntimeVersionIn",
        "RuntimeVersionOut": "_tpu_59_RuntimeVersionOut",
        "LocationIn": "_tpu_60_LocationIn",
        "LocationOut": "_tpu_61_LocationOut",
        "ShieldedInstanceConfigIn": "_tpu_62_ShieldedInstanceConfigIn",
        "ShieldedInstanceConfigOut": "_tpu_63_ShieldedInstanceConfigOut",
        "ListNodesResponseIn": "_tpu_64_ListNodesResponseIn",
        "ListNodesResponseOut": "_tpu_65_ListNodesResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["SymptomIn"] = t.struct(
        {
            "workerId": t.string().optional(),
            "details": t.string().optional(),
            "symptomType": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["SymptomIn"])
    types["SymptomOut"] = t.struct(
        {
            "workerId": t.string().optional(),
            "details": t.string().optional(),
            "symptomType": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SymptomOut"])
    types["AcceleratorConfigIn"] = t.struct(
        {"topology": t.string(), "type": t.string()}
    ).named(renames["AcceleratorConfigIn"])
    types["AcceleratorConfigOut"] = t.struct(
        {
            "topology": t.string(),
            "type": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AcceleratorConfigOut"])
    types["GuestAttributesValueIn"] = t.struct(
        {"items": t.array(t.proxy(renames["GuestAttributesEntryIn"])).optional()}
    ).named(renames["GuestAttributesValueIn"])
    types["GuestAttributesValueOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["GuestAttributesEntryOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GuestAttributesValueOut"])
    types["GenerateServiceIdentityRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GenerateServiceIdentityRequestIn"])
    types["GenerateServiceIdentityRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GenerateServiceIdentityRequestOut"])
    types["ServiceAccountIn"] = t.struct(
        {"scope": t.array(t.string()).optional(), "email": t.string().optional()}
    ).named(renames["ServiceAccountIn"])
    types["ServiceAccountOut"] = t.struct(
        {
            "scope": t.array(t.string()).optional(),
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceAccountOut"])
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
    types["NetworkEndpointIn"] = t.struct(
        {
            "port": t.integer().optional(),
            "ipAddress": t.string().optional(),
            "accessConfig": t.proxy(renames["AccessConfigIn"]).optional(),
        }
    ).named(renames["NetworkEndpointIn"])
    types["NetworkEndpointOut"] = t.struct(
        {
            "port": t.integer().optional(),
            "ipAddress": t.string().optional(),
            "accessConfig": t.proxy(renames["AccessConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkEndpointOut"])
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
    types["ListAcceleratorTypesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "acceleratorTypes": t.array(
                t.proxy(renames["AcceleratorTypeIn"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListAcceleratorTypesResponseIn"])
    types["ListAcceleratorTypesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "acceleratorTypes": t.array(
                t.proxy(renames["AcceleratorTypeOut"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAcceleratorTypesResponseOut"])
    types["AttachedDiskIn"] = t.struct(
        {"mode": t.string().optional(), "sourceDisk": t.string().optional()}
    ).named(renames["AttachedDiskIn"])
    types["AttachedDiskOut"] = t.struct(
        {
            "mode": t.string().optional(),
            "sourceDisk": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttachedDiskOut"])
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
    types["StopNodeRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["StopNodeRequestIn"]
    )
    types["StopNodeRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StopNodeRequestOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["GuestAttributesEntryIn"] = t.struct(
        {
            "value": t.string().optional(),
            "namespace": t.string().optional(),
            "key": t.string().optional(),
        }
    ).named(renames["GuestAttributesEntryIn"])
    types["GuestAttributesEntryOut"] = t.struct(
        {
            "value": t.string().optional(),
            "namespace": t.string().optional(),
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GuestAttributesEntryOut"])
    types["AccessConfigIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AccessConfigIn"]
    )
    types["AccessConfigOut"] = t.struct(
        {
            "externalIp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccessConfigOut"])
    types["SchedulingConfigIn"] = t.struct(
        {"reserved": t.boolean().optional(), "preemptible": t.boolean().optional()}
    ).named(renames["SchedulingConfigIn"])
    types["SchedulingConfigOut"] = t.struct(
        {
            "reserved": t.boolean().optional(),
            "preemptible": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SchedulingConfigOut"])
    types["OperationMetadataIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "verb": t.string().optional(),
            "apiVersion": t.string().optional(),
            "statusDetail": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "target": t.string().optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["OperationMetadataIn"])
    types["OperationMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "verb": t.string().optional(),
            "apiVersion": t.string().optional(),
            "statusDetail": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "target": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["StartNodeRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["StartNodeRequestIn"]
    )
    types["StartNodeRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StartNodeRequestOut"])
    types["AcceleratorTypeIn"] = t.struct(
        {
            "type": t.string().optional(),
            "name": t.string().optional(),
            "acceleratorConfigs": t.array(
                t.proxy(renames["AcceleratorConfigIn"])
            ).optional(),
        }
    ).named(renames["AcceleratorTypeIn"])
    types["AcceleratorTypeOut"] = t.struct(
        {
            "type": t.string().optional(),
            "name": t.string().optional(),
            "acceleratorConfigs": t.array(
                t.proxy(renames["AcceleratorConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AcceleratorTypeOut"])
    types["ListRuntimeVersionsResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "runtimeVersions": t.array(t.proxy(renames["RuntimeVersionIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListRuntimeVersionsResponseIn"])
    types["ListRuntimeVersionsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "runtimeVersions": t.array(
                t.proxy(renames["RuntimeVersionOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListRuntimeVersionsResponseOut"])
    types["GuestAttributesIn"] = t.struct(
        {
            "queryValue": t.proxy(renames["GuestAttributesValueIn"]).optional(),
            "queryPath": t.string().optional(),
        }
    ).named(renames["GuestAttributesIn"])
    types["GuestAttributesOut"] = t.struct(
        {
            "queryValue": t.proxy(renames["GuestAttributesValueOut"]).optional(),
            "queryPath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GuestAttributesOut"])
    types["NetworkConfigIn"] = t.struct(
        {
            "canIpForward": t.boolean().optional(),
            "network": t.string().optional(),
            "enableExternalIps": t.boolean().optional(),
            "subnetwork": t.string().optional(),
        }
    ).named(renames["NetworkConfigIn"])
    types["NetworkConfigOut"] = t.struct(
        {
            "canIpForward": t.boolean().optional(),
            "network": t.string().optional(),
            "enableExternalIps": t.boolean().optional(),
            "subnetwork": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkConfigOut"])
    types["OperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["GetGuestAttributesResponseIn"] = t.struct(
        {"guestAttributes": t.array(t.proxy(renames["GuestAttributesIn"])).optional()}
    ).named(renames["GetGuestAttributesResponseIn"])
    types["GetGuestAttributesResponseOut"] = t.struct(
        {
            "guestAttributes": t.array(
                t.proxy(renames["GuestAttributesOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetGuestAttributesResponseOut"])
    types["GetGuestAttributesRequestIn"] = t.struct(
        {
            "workerIds": t.array(t.string()).optional(),
            "queryPath": t.string().optional(),
        }
    ).named(renames["GetGuestAttributesRequestIn"])
    types["GetGuestAttributesRequestOut"] = t.struct(
        {
            "workerIds": t.array(t.string()).optional(),
            "queryPath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetGuestAttributesRequestOut"])
    types["GenerateServiceIdentityResponseIn"] = t.struct(
        {"identity": t.proxy(renames["ServiceIdentityIn"]).optional()}
    ).named(renames["GenerateServiceIdentityResponseIn"])
    types["GenerateServiceIdentityResponseOut"] = t.struct(
        {
            "identity": t.proxy(renames["ServiceIdentityOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateServiceIdentityResponseOut"])
    types["ServiceIdentityIn"] = t.struct({"email": t.string().optional()}).named(
        renames["ServiceIdentityIn"]
    )
    types["ServiceIdentityOut"] = t.struct(
        {
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceIdentityOut"])
    types["NodeIn"] = t.struct(
        {
            "tags": t.array(t.string()).optional(),
            "networkConfig": t.proxy(renames["NetworkConfigIn"]).optional(),
            "schedulingConfig": t.proxy(renames["SchedulingConfigIn"]).optional(),
            "description": t.string().optional(),
            "dataDisks": t.array(t.proxy(renames["AttachedDiskIn"])).optional(),
            "runtimeVersion": t.string(),
            "shieldedInstanceConfig": t.proxy(
                renames["ShieldedInstanceConfigIn"]
            ).optional(),
            "acceleratorType": t.string(),
            "acceleratorConfig": t.proxy(renames["AcceleratorConfigIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "health": t.string().optional(),
            "cidrBlock": t.string().optional(),
            "serviceAccount": t.proxy(renames["ServiceAccountIn"]).optional(),
        }
    ).named(renames["NodeIn"])
    types["NodeOut"] = t.struct(
        {
            "tags": t.array(t.string()).optional(),
            "healthDescription": t.string().optional(),
            "networkConfig": t.proxy(renames["NetworkConfigOut"]).optional(),
            "schedulingConfig": t.proxy(renames["SchedulingConfigOut"]).optional(),
            "networkEndpoints": t.array(
                t.proxy(renames["NetworkEndpointOut"])
            ).optional(),
            "state": t.string().optional(),
            "description": t.string().optional(),
            "dataDisks": t.array(t.proxy(renames["AttachedDiskOut"])).optional(),
            "runtimeVersion": t.string(),
            "symptoms": t.array(t.proxy(renames["SymptomOut"])).optional(),
            "shieldedInstanceConfig": t.proxy(
                renames["ShieldedInstanceConfigOut"]
            ).optional(),
            "acceleratorType": t.string(),
            "acceleratorConfig": t.proxy(renames["AcceleratorConfigOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "apiVersion": t.string().optional(),
            "health": t.string().optional(),
            "id": t.string().optional(),
            "cidrBlock": t.string().optional(),
            "serviceAccount": t.proxy(renames["ServiceAccountOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeOut"])
    types["RuntimeVersionIn"] = t.struct(
        {"version": t.string().optional(), "name": t.string().optional()}
    ).named(renames["RuntimeVersionIn"])
    types["RuntimeVersionOut"] = t.struct(
        {
            "version": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RuntimeVersionOut"])
    types["LocationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["ShieldedInstanceConfigIn"] = t.struct(
        {"enableSecureBoot": t.boolean().optional()}
    ).named(renames["ShieldedInstanceConfigIn"])
    types["ShieldedInstanceConfigOut"] = t.struct(
        {
            "enableSecureBoot": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShieldedInstanceConfigOut"])
    types["ListNodesResponseIn"] = t.struct(
        {
            "nodes": t.array(t.proxy(renames["NodeIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListNodesResponseIn"])
    types["ListNodesResponseOut"] = t.struct(
        {
            "nodes": t.array(t.proxy(renames["NodeOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListNodesResponseOut"])

    functions = {}
    functions["projectsLocationsGet"] = tpu.get(
        "v2/{name}/locations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGenerateServiceIdentity"] = tpu.get(
        "v2/{name}/locations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsList"] = tpu.get(
        "v2/{name}/locations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNodesGetGuestAttributes"] = tpu.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["NodeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNodesStart"] = tpu.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["NodeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNodesCreate"] = tpu.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["NodeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNodesPatch"] = tpu.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["NodeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNodesDelete"] = tpu.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["NodeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNodesStop"] = tpu.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["NodeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNodesList"] = tpu.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["NodeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNodesGet"] = tpu.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["NodeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = tpu.get(
        "v2/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = tpu.get(
        "v2/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = tpu.get(
        "v2/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = tpu.get(
        "v2/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAcceleratorTypesGet"] = tpu.get(
        "v2/{parent}/acceleratorTypes",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAcceleratorTypesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAcceleratorTypesList"] = tpu.get(
        "v2/{parent}/acceleratorTypes",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAcceleratorTypesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRuntimeVersionsGet"] = tpu.get(
        "v2/{parent}/runtimeVersions",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListRuntimeVersionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRuntimeVersionsList"] = tpu.get(
        "v2/{parent}/runtimeVersions",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListRuntimeVersionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="tpu", renames=renames, types=Box(types), functions=Box(functions)
    )
