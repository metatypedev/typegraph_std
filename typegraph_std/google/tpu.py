from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_tpu() -> Import:
    tpu = HTTPRuntime("https://tpu.googleapis.com/")

    renames = {
        "ErrorResponse": "_tpu_1_ErrorResponse",
        "GetGuestAttributesRequestIn": "_tpu_2_GetGuestAttributesRequestIn",
        "GetGuestAttributesRequestOut": "_tpu_3_GetGuestAttributesRequestOut",
        "StopNodeRequestIn": "_tpu_4_StopNodeRequestIn",
        "StopNodeRequestOut": "_tpu_5_StopNodeRequestOut",
        "GuestAttributesIn": "_tpu_6_GuestAttributesIn",
        "GuestAttributesOut": "_tpu_7_GuestAttributesOut",
        "SchedulingConfigIn": "_tpu_8_SchedulingConfigIn",
        "SchedulingConfigOut": "_tpu_9_SchedulingConfigOut",
        "ListLocationsResponseIn": "_tpu_10_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_tpu_11_ListLocationsResponseOut",
        "StatusIn": "_tpu_12_StatusIn",
        "StatusOut": "_tpu_13_StatusOut",
        "ShieldedInstanceConfigIn": "_tpu_14_ShieldedInstanceConfigIn",
        "ShieldedInstanceConfigOut": "_tpu_15_ShieldedInstanceConfigOut",
        "ServiceIdentityIn": "_tpu_16_ServiceIdentityIn",
        "ServiceIdentityOut": "_tpu_17_ServiceIdentityOut",
        "SymptomIn": "_tpu_18_SymptomIn",
        "SymptomOut": "_tpu_19_SymptomOut",
        "EmptyIn": "_tpu_20_EmptyIn",
        "EmptyOut": "_tpu_21_EmptyOut",
        "OperationMetadataIn": "_tpu_22_OperationMetadataIn",
        "OperationMetadataOut": "_tpu_23_OperationMetadataOut",
        "ListRuntimeVersionsResponseIn": "_tpu_24_ListRuntimeVersionsResponseIn",
        "ListRuntimeVersionsResponseOut": "_tpu_25_ListRuntimeVersionsResponseOut",
        "ListNodesResponseIn": "_tpu_26_ListNodesResponseIn",
        "ListNodesResponseOut": "_tpu_27_ListNodesResponseOut",
        "AttachedDiskIn": "_tpu_28_AttachedDiskIn",
        "AttachedDiskOut": "_tpu_29_AttachedDiskOut",
        "AcceleratorConfigIn": "_tpu_30_AcceleratorConfigIn",
        "AcceleratorConfigOut": "_tpu_31_AcceleratorConfigOut",
        "GuestAttributesValueIn": "_tpu_32_GuestAttributesValueIn",
        "GuestAttributesValueOut": "_tpu_33_GuestAttributesValueOut",
        "NodeIn": "_tpu_34_NodeIn",
        "NodeOut": "_tpu_35_NodeOut",
        "ServiceAccountIn": "_tpu_36_ServiceAccountIn",
        "ServiceAccountOut": "_tpu_37_ServiceAccountOut",
        "OperationIn": "_tpu_38_OperationIn",
        "OperationOut": "_tpu_39_OperationOut",
        "NetworkConfigIn": "_tpu_40_NetworkConfigIn",
        "NetworkConfigOut": "_tpu_41_NetworkConfigOut",
        "LocationIn": "_tpu_42_LocationIn",
        "LocationOut": "_tpu_43_LocationOut",
        "RuntimeVersionIn": "_tpu_44_RuntimeVersionIn",
        "RuntimeVersionOut": "_tpu_45_RuntimeVersionOut",
        "AccessConfigIn": "_tpu_46_AccessConfigIn",
        "AccessConfigOut": "_tpu_47_AccessConfigOut",
        "GenerateServiceIdentityRequestIn": "_tpu_48_GenerateServiceIdentityRequestIn",
        "GenerateServiceIdentityRequestOut": "_tpu_49_GenerateServiceIdentityRequestOut",
        "GuestAttributesEntryIn": "_tpu_50_GuestAttributesEntryIn",
        "GuestAttributesEntryOut": "_tpu_51_GuestAttributesEntryOut",
        "ListOperationsResponseIn": "_tpu_52_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_tpu_53_ListOperationsResponseOut",
        "ListAcceleratorTypesResponseIn": "_tpu_54_ListAcceleratorTypesResponseIn",
        "ListAcceleratorTypesResponseOut": "_tpu_55_ListAcceleratorTypesResponseOut",
        "AcceleratorTypeIn": "_tpu_56_AcceleratorTypeIn",
        "AcceleratorTypeOut": "_tpu_57_AcceleratorTypeOut",
        "GenerateServiceIdentityResponseIn": "_tpu_58_GenerateServiceIdentityResponseIn",
        "GenerateServiceIdentityResponseOut": "_tpu_59_GenerateServiceIdentityResponseOut",
        "GetGuestAttributesResponseIn": "_tpu_60_GetGuestAttributesResponseIn",
        "GetGuestAttributesResponseOut": "_tpu_61_GetGuestAttributesResponseOut",
        "StartNodeRequestIn": "_tpu_62_StartNodeRequestIn",
        "StartNodeRequestOut": "_tpu_63_StartNodeRequestOut",
        "NetworkEndpointIn": "_tpu_64_NetworkEndpointIn",
        "NetworkEndpointOut": "_tpu_65_NetworkEndpointOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["StopNodeRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["StopNodeRequestIn"]
    )
    types["StopNodeRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StopNodeRequestOut"])
    types["GuestAttributesIn"] = t.struct(
        {
            "queryPath": t.string().optional(),
            "queryValue": t.proxy(renames["GuestAttributesValueIn"]).optional(),
        }
    ).named(renames["GuestAttributesIn"])
    types["GuestAttributesOut"] = t.struct(
        {
            "queryPath": t.string().optional(),
            "queryValue": t.proxy(renames["GuestAttributesValueOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GuestAttributesOut"])
    types["SchedulingConfigIn"] = t.struct(
        {"preemptible": t.boolean().optional(), "reserved": t.boolean().optional()}
    ).named(renames["SchedulingConfigIn"])
    types["SchedulingConfigOut"] = t.struct(
        {
            "preemptible": t.boolean().optional(),
            "reserved": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SchedulingConfigOut"])
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
    types["ShieldedInstanceConfigIn"] = t.struct(
        {"enableSecureBoot": t.boolean().optional()}
    ).named(renames["ShieldedInstanceConfigIn"])
    types["ShieldedInstanceConfigOut"] = t.struct(
        {
            "enableSecureBoot": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShieldedInstanceConfigOut"])
    types["ServiceIdentityIn"] = t.struct({"email": t.string().optional()}).named(
        renames["ServiceIdentityIn"]
    )
    types["ServiceIdentityOut"] = t.struct(
        {
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceIdentityOut"])
    types["SymptomIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "details": t.string().optional(),
            "workerId": t.string().optional(),
            "symptomType": t.string().optional(),
        }
    ).named(renames["SymptomIn"])
    types["SymptomOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "details": t.string().optional(),
            "workerId": t.string().optional(),
            "symptomType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SymptomOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["OperationMetadataIn"] = t.struct(
        {
            "endTime": t.string().optional(),
            "target": t.string().optional(),
            "verb": t.string().optional(),
            "apiVersion": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "statusDetail": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["OperationMetadataIn"])
    types["OperationMetadataOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "target": t.string().optional(),
            "verb": t.string().optional(),
            "apiVersion": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "statusDetail": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["ListRuntimeVersionsResponseIn"] = t.struct(
        {
            "runtimeVersions": t.array(t.proxy(renames["RuntimeVersionIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListRuntimeVersionsResponseIn"])
    types["ListRuntimeVersionsResponseOut"] = t.struct(
        {
            "runtimeVersions": t.array(
                t.proxy(renames["RuntimeVersionOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListRuntimeVersionsResponseOut"])
    types["ListNodesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "nodes": t.array(t.proxy(renames["NodeIn"])).optional(),
        }
    ).named(renames["ListNodesResponseIn"])
    types["ListNodesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "nodes": t.array(t.proxy(renames["NodeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListNodesResponseOut"])
    types["AttachedDiskIn"] = t.struct(
        {"sourceDisk": t.string().optional(), "mode": t.string().optional()}
    ).named(renames["AttachedDiskIn"])
    types["AttachedDiskOut"] = t.struct(
        {
            "sourceDisk": t.string().optional(),
            "mode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttachedDiskOut"])
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
    types["NodeIn"] = t.struct(
        {
            "shieldedInstanceConfig": t.proxy(
                renames["ShieldedInstanceConfigIn"]
            ).optional(),
            "description": t.string().optional(),
            "cidrBlock": t.string().optional(),
            "schedulingConfig": t.proxy(renames["SchedulingConfigIn"]).optional(),
            "networkConfig": t.proxy(renames["NetworkConfigIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "dataDisks": t.array(t.proxy(renames["AttachedDiskIn"])).optional(),
            "serviceAccount": t.proxy(renames["ServiceAccountIn"]).optional(),
            "health": t.string().optional(),
            "runtimeVersion": t.string(),
            "tags": t.array(t.string()).optional(),
            "acceleratorType": t.string(),
            "acceleratorConfig": t.proxy(renames["AcceleratorConfigIn"]).optional(),
        }
    ).named(renames["NodeIn"])
    types["NodeOut"] = t.struct(
        {
            "shieldedInstanceConfig": t.proxy(
                renames["ShieldedInstanceConfigOut"]
            ).optional(),
            "symptoms": t.array(t.proxy(renames["SymptomOut"])).optional(),
            "description": t.string().optional(),
            "cidrBlock": t.string().optional(),
            "schedulingConfig": t.proxy(renames["SchedulingConfigOut"]).optional(),
            "name": t.string().optional(),
            "networkEndpoints": t.array(
                t.proxy(renames["NetworkEndpointOut"])
            ).optional(),
            "apiVersion": t.string().optional(),
            "networkConfig": t.proxy(renames["NetworkConfigOut"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "dataDisks": t.array(t.proxy(renames["AttachedDiskOut"])).optional(),
            "serviceAccount": t.proxy(renames["ServiceAccountOut"]).optional(),
            "state": t.string().optional(),
            "health": t.string().optional(),
            "healthDescription": t.string().optional(),
            "createTime": t.string().optional(),
            "runtimeVersion": t.string(),
            "tags": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "acceleratorType": t.string(),
            "acceleratorConfig": t.proxy(renames["AcceleratorConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeOut"])
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
    types["OperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
    types["NetworkConfigIn"] = t.struct(
        {
            "subnetwork": t.string().optional(),
            "enableExternalIps": t.boolean().optional(),
            "canIpForward": t.boolean().optional(),
            "network": t.string().optional(),
        }
    ).named(renames["NetworkConfigIn"])
    types["NetworkConfigOut"] = t.struct(
        {
            "subnetwork": t.string().optional(),
            "enableExternalIps": t.boolean().optional(),
            "canIpForward": t.boolean().optional(),
            "network": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkConfigOut"])
    types["LocationIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
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
    types["AccessConfigIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AccessConfigIn"]
    )
    types["AccessConfigOut"] = t.struct(
        {
            "externalIp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccessConfigOut"])
    types["GenerateServiceIdentityRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GenerateServiceIdentityRequestIn"])
    types["GenerateServiceIdentityRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GenerateServiceIdentityRequestOut"])
    types["GuestAttributesEntryIn"] = t.struct(
        {
            "namespace": t.string().optional(),
            "value": t.string().optional(),
            "key": t.string().optional(),
        }
    ).named(renames["GuestAttributesEntryIn"])
    types["GuestAttributesEntryOut"] = t.struct(
        {
            "namespace": t.string().optional(),
            "value": t.string().optional(),
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GuestAttributesEntryOut"])
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
    types["ListAcceleratorTypesResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "acceleratorTypes": t.array(
                t.proxy(renames["AcceleratorTypeIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListAcceleratorTypesResponseIn"])
    types["ListAcceleratorTypesResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "acceleratorTypes": t.array(
                t.proxy(renames["AcceleratorTypeOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAcceleratorTypesResponseOut"])
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
    types["GenerateServiceIdentityResponseIn"] = t.struct(
        {"identity": t.proxy(renames["ServiceIdentityIn"]).optional()}
    ).named(renames["GenerateServiceIdentityResponseIn"])
    types["GenerateServiceIdentityResponseOut"] = t.struct(
        {
            "identity": t.proxy(renames["ServiceIdentityOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateServiceIdentityResponseOut"])
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
    types["StartNodeRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["StartNodeRequestIn"]
    )
    types["StartNodeRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StartNodeRequestOut"])
    types["NetworkEndpointIn"] = t.struct(
        {
            "ipAddress": t.string().optional(),
            "accessConfig": t.proxy(renames["AccessConfigIn"]).optional(),
            "port": t.integer().optional(),
        }
    ).named(renames["NetworkEndpointIn"])
    types["NetworkEndpointOut"] = t.struct(
        {
            "ipAddress": t.string().optional(),
            "accessConfig": t.proxy(renames["AccessConfigOut"]).optional(),
            "port": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkEndpointOut"])

    functions = {}
    functions["projectsLocationsList"] = tpu.get(
        "v2/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGenerateServiceIdentity"] = tpu.get(
        "v2/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = tpu.get(
        "v2/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRuntimeVersionsList"] = tpu.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["RuntimeVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRuntimeVersionsGet"] = tpu.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["RuntimeVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAcceleratorTypesGet"] = tpu.get(
        "v2/{parent}/acceleratorTypes",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
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
                "parent": t.string(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAcceleratorTypesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = tpu.get(
        "v2/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = tpu.get(
        "v2/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
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
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
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
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNodesStart"] = tpu.post(
        "v2/{parent}/nodes",
        t.struct(
            {
                "nodeId": t.string().optional(),
                "parent": t.string(),
                "shieldedInstanceConfig": t.proxy(
                    renames["ShieldedInstanceConfigIn"]
                ).optional(),
                "description": t.string().optional(),
                "cidrBlock": t.string().optional(),
                "schedulingConfig": t.proxy(renames["SchedulingConfigIn"]).optional(),
                "networkConfig": t.proxy(renames["NetworkConfigIn"]).optional(),
                "metadata": t.struct({"_": t.string().optional()}).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "dataDisks": t.array(t.proxy(renames["AttachedDiskIn"])).optional(),
                "serviceAccount": t.proxy(renames["ServiceAccountIn"]).optional(),
                "health": t.string().optional(),
                "runtimeVersion": t.string(),
                "tags": t.array(t.string()).optional(),
                "acceleratorType": t.string(),
                "acceleratorConfig": t.proxy(renames["AcceleratorConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNodesGetGuestAttributes"] = tpu.post(
        "v2/{parent}/nodes",
        t.struct(
            {
                "nodeId": t.string().optional(),
                "parent": t.string(),
                "shieldedInstanceConfig": t.proxy(
                    renames["ShieldedInstanceConfigIn"]
                ).optional(),
                "description": t.string().optional(),
                "cidrBlock": t.string().optional(),
                "schedulingConfig": t.proxy(renames["SchedulingConfigIn"]).optional(),
                "networkConfig": t.proxy(renames["NetworkConfigIn"]).optional(),
                "metadata": t.struct({"_": t.string().optional()}).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "dataDisks": t.array(t.proxy(renames["AttachedDiskIn"])).optional(),
                "serviceAccount": t.proxy(renames["ServiceAccountIn"]).optional(),
                "health": t.string().optional(),
                "runtimeVersion": t.string(),
                "tags": t.array(t.string()).optional(),
                "acceleratorType": t.string(),
                "acceleratorConfig": t.proxy(renames["AcceleratorConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNodesDelete"] = tpu.post(
        "v2/{parent}/nodes",
        t.struct(
            {
                "nodeId": t.string().optional(),
                "parent": t.string(),
                "shieldedInstanceConfig": t.proxy(
                    renames["ShieldedInstanceConfigIn"]
                ).optional(),
                "description": t.string().optional(),
                "cidrBlock": t.string().optional(),
                "schedulingConfig": t.proxy(renames["SchedulingConfigIn"]).optional(),
                "networkConfig": t.proxy(renames["NetworkConfigIn"]).optional(),
                "metadata": t.struct({"_": t.string().optional()}).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "dataDisks": t.array(t.proxy(renames["AttachedDiskIn"])).optional(),
                "serviceAccount": t.proxy(renames["ServiceAccountIn"]).optional(),
                "health": t.string().optional(),
                "runtimeVersion": t.string(),
                "tags": t.array(t.string()).optional(),
                "acceleratorType": t.string(),
                "acceleratorConfig": t.proxy(renames["AcceleratorConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNodesGet"] = tpu.post(
        "v2/{parent}/nodes",
        t.struct(
            {
                "nodeId": t.string().optional(),
                "parent": t.string(),
                "shieldedInstanceConfig": t.proxy(
                    renames["ShieldedInstanceConfigIn"]
                ).optional(),
                "description": t.string().optional(),
                "cidrBlock": t.string().optional(),
                "schedulingConfig": t.proxy(renames["SchedulingConfigIn"]).optional(),
                "networkConfig": t.proxy(renames["NetworkConfigIn"]).optional(),
                "metadata": t.struct({"_": t.string().optional()}).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "dataDisks": t.array(t.proxy(renames["AttachedDiskIn"])).optional(),
                "serviceAccount": t.proxy(renames["ServiceAccountIn"]).optional(),
                "health": t.string().optional(),
                "runtimeVersion": t.string(),
                "tags": t.array(t.string()).optional(),
                "acceleratorType": t.string(),
                "acceleratorConfig": t.proxy(renames["AcceleratorConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNodesPatch"] = tpu.post(
        "v2/{parent}/nodes",
        t.struct(
            {
                "nodeId": t.string().optional(),
                "parent": t.string(),
                "shieldedInstanceConfig": t.proxy(
                    renames["ShieldedInstanceConfigIn"]
                ).optional(),
                "description": t.string().optional(),
                "cidrBlock": t.string().optional(),
                "schedulingConfig": t.proxy(renames["SchedulingConfigIn"]).optional(),
                "networkConfig": t.proxy(renames["NetworkConfigIn"]).optional(),
                "metadata": t.struct({"_": t.string().optional()}).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "dataDisks": t.array(t.proxy(renames["AttachedDiskIn"])).optional(),
                "serviceAccount": t.proxy(renames["ServiceAccountIn"]).optional(),
                "health": t.string().optional(),
                "runtimeVersion": t.string(),
                "tags": t.array(t.string()).optional(),
                "acceleratorType": t.string(),
                "acceleratorConfig": t.proxy(renames["AcceleratorConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNodesList"] = tpu.post(
        "v2/{parent}/nodes",
        t.struct(
            {
                "nodeId": t.string().optional(),
                "parent": t.string(),
                "shieldedInstanceConfig": t.proxy(
                    renames["ShieldedInstanceConfigIn"]
                ).optional(),
                "description": t.string().optional(),
                "cidrBlock": t.string().optional(),
                "schedulingConfig": t.proxy(renames["SchedulingConfigIn"]).optional(),
                "networkConfig": t.proxy(renames["NetworkConfigIn"]).optional(),
                "metadata": t.struct({"_": t.string().optional()}).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "dataDisks": t.array(t.proxy(renames["AttachedDiskIn"])).optional(),
                "serviceAccount": t.proxy(renames["ServiceAccountIn"]).optional(),
                "health": t.string().optional(),
                "runtimeVersion": t.string(),
                "tags": t.array(t.string()).optional(),
                "acceleratorType": t.string(),
                "acceleratorConfig": t.proxy(renames["AcceleratorConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNodesStop"] = tpu.post(
        "v2/{parent}/nodes",
        t.struct(
            {
                "nodeId": t.string().optional(),
                "parent": t.string(),
                "shieldedInstanceConfig": t.proxy(
                    renames["ShieldedInstanceConfigIn"]
                ).optional(),
                "description": t.string().optional(),
                "cidrBlock": t.string().optional(),
                "schedulingConfig": t.proxy(renames["SchedulingConfigIn"]).optional(),
                "networkConfig": t.proxy(renames["NetworkConfigIn"]).optional(),
                "metadata": t.struct({"_": t.string().optional()}).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "dataDisks": t.array(t.proxy(renames["AttachedDiskIn"])).optional(),
                "serviceAccount": t.proxy(renames["ServiceAccountIn"]).optional(),
                "health": t.string().optional(),
                "runtimeVersion": t.string(),
                "tags": t.array(t.string()).optional(),
                "acceleratorType": t.string(),
                "acceleratorConfig": t.proxy(renames["AcceleratorConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNodesCreate"] = tpu.post(
        "v2/{parent}/nodes",
        t.struct(
            {
                "nodeId": t.string().optional(),
                "parent": t.string(),
                "shieldedInstanceConfig": t.proxy(
                    renames["ShieldedInstanceConfigIn"]
                ).optional(),
                "description": t.string().optional(),
                "cidrBlock": t.string().optional(),
                "schedulingConfig": t.proxy(renames["SchedulingConfigIn"]).optional(),
                "networkConfig": t.proxy(renames["NetworkConfigIn"]).optional(),
                "metadata": t.struct({"_": t.string().optional()}).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "dataDisks": t.array(t.proxy(renames["AttachedDiskIn"])).optional(),
                "serviceAccount": t.proxy(renames["ServiceAccountIn"]).optional(),
                "health": t.string().optional(),
                "runtimeVersion": t.string(),
                "tags": t.array(t.string()).optional(),
                "acceleratorType": t.string(),
                "acceleratorConfig": t.proxy(renames["AcceleratorConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(importer="tpu", renames=renames, types=types, functions=functions)
