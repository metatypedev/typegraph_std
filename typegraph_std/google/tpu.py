from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_tpu():
    tpu = HTTPRuntime("https://tpu.googleapis.com/")

    renames = {
        "ErrorResponse": "_tpu_1_ErrorResponse",
        "NodeIn": "_tpu_2_NodeIn",
        "NodeOut": "_tpu_3_NodeOut",
        "GenerateServiceIdentityResponseIn": "_tpu_4_GenerateServiceIdentityResponseIn",
        "GenerateServiceIdentityResponseOut": "_tpu_5_GenerateServiceIdentityResponseOut",
        "ListLocationsResponseIn": "_tpu_6_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_tpu_7_ListLocationsResponseOut",
        "ListAcceleratorTypesResponseIn": "_tpu_8_ListAcceleratorTypesResponseIn",
        "ListAcceleratorTypesResponseOut": "_tpu_9_ListAcceleratorTypesResponseOut",
        "OperationMetadataIn": "_tpu_10_OperationMetadataIn",
        "OperationMetadataOut": "_tpu_11_OperationMetadataOut",
        "SchedulingConfigIn": "_tpu_12_SchedulingConfigIn",
        "SchedulingConfigOut": "_tpu_13_SchedulingConfigOut",
        "SymptomIn": "_tpu_14_SymptomIn",
        "SymptomOut": "_tpu_15_SymptomOut",
        "GuestAttributesEntryIn": "_tpu_16_GuestAttributesEntryIn",
        "GuestAttributesEntryOut": "_tpu_17_GuestAttributesEntryOut",
        "NetworkConfigIn": "_tpu_18_NetworkConfigIn",
        "NetworkConfigOut": "_tpu_19_NetworkConfigOut",
        "ListNodesResponseIn": "_tpu_20_ListNodesResponseIn",
        "ListNodesResponseOut": "_tpu_21_ListNodesResponseOut",
        "GetGuestAttributesRequestIn": "_tpu_22_GetGuestAttributesRequestIn",
        "GetGuestAttributesRequestOut": "_tpu_23_GetGuestAttributesRequestOut",
        "ListRuntimeVersionsResponseIn": "_tpu_24_ListRuntimeVersionsResponseIn",
        "ListRuntimeVersionsResponseOut": "_tpu_25_ListRuntimeVersionsResponseOut",
        "ShieldedInstanceConfigIn": "_tpu_26_ShieldedInstanceConfigIn",
        "ShieldedInstanceConfigOut": "_tpu_27_ShieldedInstanceConfigOut",
        "GuestAttributesValueIn": "_tpu_28_GuestAttributesValueIn",
        "GuestAttributesValueOut": "_tpu_29_GuestAttributesValueOut",
        "EmptyIn": "_tpu_30_EmptyIn",
        "EmptyOut": "_tpu_31_EmptyOut",
        "LocationIn": "_tpu_32_LocationIn",
        "LocationOut": "_tpu_33_LocationOut",
        "ListOperationsResponseIn": "_tpu_34_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_tpu_35_ListOperationsResponseOut",
        "GuestAttributesIn": "_tpu_36_GuestAttributesIn",
        "GuestAttributesOut": "_tpu_37_GuestAttributesOut",
        "GenerateServiceIdentityRequestIn": "_tpu_38_GenerateServiceIdentityRequestIn",
        "GenerateServiceIdentityRequestOut": "_tpu_39_GenerateServiceIdentityRequestOut",
        "ServiceAccountIn": "_tpu_40_ServiceAccountIn",
        "ServiceAccountOut": "_tpu_41_ServiceAccountOut",
        "OperationIn": "_tpu_42_OperationIn",
        "OperationOut": "_tpu_43_OperationOut",
        "AttachedDiskIn": "_tpu_44_AttachedDiskIn",
        "AttachedDiskOut": "_tpu_45_AttachedDiskOut",
        "GetGuestAttributesResponseIn": "_tpu_46_GetGuestAttributesResponseIn",
        "GetGuestAttributesResponseOut": "_tpu_47_GetGuestAttributesResponseOut",
        "AcceleratorConfigIn": "_tpu_48_AcceleratorConfigIn",
        "AcceleratorConfigOut": "_tpu_49_AcceleratorConfigOut",
        "StartNodeRequestIn": "_tpu_50_StartNodeRequestIn",
        "StartNodeRequestOut": "_tpu_51_StartNodeRequestOut",
        "StopNodeRequestIn": "_tpu_52_StopNodeRequestIn",
        "StopNodeRequestOut": "_tpu_53_StopNodeRequestOut",
        "AcceleratorTypeIn": "_tpu_54_AcceleratorTypeIn",
        "AcceleratorTypeOut": "_tpu_55_AcceleratorTypeOut",
        "RuntimeVersionIn": "_tpu_56_RuntimeVersionIn",
        "RuntimeVersionOut": "_tpu_57_RuntimeVersionOut",
        "AccessConfigIn": "_tpu_58_AccessConfigIn",
        "AccessConfigOut": "_tpu_59_AccessConfigOut",
        "StatusIn": "_tpu_60_StatusIn",
        "StatusOut": "_tpu_61_StatusOut",
        "ServiceIdentityIn": "_tpu_62_ServiceIdentityIn",
        "ServiceIdentityOut": "_tpu_63_ServiceIdentityOut",
        "NetworkEndpointIn": "_tpu_64_NetworkEndpointIn",
        "NetworkEndpointOut": "_tpu_65_NetworkEndpointOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["NodeIn"] = t.struct(
        {
            "networkConfig": t.proxy(renames["NetworkConfigIn"]).optional(),
            "description": t.string().optional(),
            "acceleratorType": t.string(),
            "runtimeVersion": t.string(),
            "tags": t.array(t.string()).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "dataDisks": t.array(t.proxy(renames["AttachedDiskIn"])).optional(),
            "acceleratorConfig": t.proxy(renames["AcceleratorConfigIn"]).optional(),
            "serviceAccount": t.proxy(renames["ServiceAccountIn"]).optional(),
            "schedulingConfig": t.proxy(renames["SchedulingConfigIn"]).optional(),
            "shieldedInstanceConfig": t.proxy(
                renames["ShieldedInstanceConfigIn"]
            ).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "health": t.string().optional(),
            "cidrBlock": t.string().optional(),
        }
    ).named(renames["NodeIn"])
    types["NodeOut"] = t.struct(
        {
            "networkConfig": t.proxy(renames["NetworkConfigOut"]).optional(),
            "description": t.string().optional(),
            "acceleratorType": t.string(),
            "runtimeVersion": t.string(),
            "tags": t.array(t.string()).optional(),
            "apiVersion": t.string().optional(),
            "id": t.string().optional(),
            "healthDescription": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "dataDisks": t.array(t.proxy(renames["AttachedDiskOut"])).optional(),
            "acceleratorConfig": t.proxy(renames["AcceleratorConfigOut"]).optional(),
            "serviceAccount": t.proxy(renames["ServiceAccountOut"]).optional(),
            "schedulingConfig": t.proxy(renames["SchedulingConfigOut"]).optional(),
            "shieldedInstanceConfig": t.proxy(
                renames["ShieldedInstanceConfigOut"]
            ).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "networkEndpoints": t.array(
                t.proxy(renames["NetworkEndpointOut"])
            ).optional(),
            "health": t.string().optional(),
            "symptoms": t.array(t.proxy(renames["SymptomOut"])).optional(),
            "createTime": t.string().optional(),
            "cidrBlock": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeOut"])
    types["GenerateServiceIdentityResponseIn"] = t.struct(
        {"identity": t.proxy(renames["ServiceIdentityIn"]).optional()}
    ).named(renames["GenerateServiceIdentityResponseIn"])
    types["GenerateServiceIdentityResponseOut"] = t.struct(
        {
            "identity": t.proxy(renames["ServiceIdentityOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateServiceIdentityResponseOut"])
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
    types["OperationMetadataIn"] = t.struct(
        {
            "target": t.string().optional(),
            "apiVersion": t.string().optional(),
            "createTime": t.string().optional(),
            "endTime": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "statusDetail": t.string().optional(),
            "verb": t.string().optional(),
        }
    ).named(renames["OperationMetadataIn"])
    types["OperationMetadataOut"] = t.struct(
        {
            "target": t.string().optional(),
            "apiVersion": t.string().optional(),
            "createTime": t.string().optional(),
            "endTime": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "statusDetail": t.string().optional(),
            "verb": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
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
    types["SymptomIn"] = t.struct(
        {
            "workerId": t.string().optional(),
            "createTime": t.string().optional(),
            "symptomType": t.string().optional(),
            "details": t.string().optional(),
        }
    ).named(renames["SymptomIn"])
    types["SymptomOut"] = t.struct(
        {
            "workerId": t.string().optional(),
            "createTime": t.string().optional(),
            "symptomType": t.string().optional(),
            "details": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SymptomOut"])
    types["GuestAttributesEntryIn"] = t.struct(
        {
            "key": t.string().optional(),
            "namespace": t.string().optional(),
            "value": t.string().optional(),
        }
    ).named(renames["GuestAttributesEntryIn"])
    types["GuestAttributesEntryOut"] = t.struct(
        {
            "key": t.string().optional(),
            "namespace": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GuestAttributesEntryOut"])
    types["NetworkConfigIn"] = t.struct(
        {
            "enableExternalIps": t.boolean().optional(),
            "canIpForward": t.boolean().optional(),
            "network": t.string().optional(),
            "subnetwork": t.string().optional(),
        }
    ).named(renames["NetworkConfigIn"])
    types["NetworkConfigOut"] = t.struct(
        {
            "enableExternalIps": t.boolean().optional(),
            "canIpForward": t.boolean().optional(),
            "network": t.string().optional(),
            "subnetwork": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkConfigOut"])
    types["ListNodesResponseIn"] = t.struct(
        {
            "nodes": t.array(t.proxy(renames["NodeIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListNodesResponseIn"])
    types["ListNodesResponseOut"] = t.struct(
        {
            "nodes": t.array(t.proxy(renames["NodeOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListNodesResponseOut"])
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
    types["ListRuntimeVersionsResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "runtimeVersions": t.array(t.proxy(renames["RuntimeVersionIn"])).optional(),
        }
    ).named(renames["ListRuntimeVersionsResponseIn"])
    types["ListRuntimeVersionsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "runtimeVersions": t.array(
                t.proxy(renames["RuntimeVersionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListRuntimeVersionsResponseOut"])
    types["ShieldedInstanceConfigIn"] = t.struct(
        {"enableSecureBoot": t.boolean().optional()}
    ).named(renames["ShieldedInstanceConfigIn"])
    types["ShieldedInstanceConfigOut"] = t.struct(
        {
            "enableSecureBoot": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShieldedInstanceConfigOut"])
    types["GuestAttributesValueIn"] = t.struct(
        {"items": t.array(t.proxy(renames["GuestAttributesEntryIn"])).optional()}
    ).named(renames["GuestAttributesValueIn"])
    types["GuestAttributesValueOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["GuestAttributesEntryOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GuestAttributesValueOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["GenerateServiceIdentityRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GenerateServiceIdentityRequestIn"])
    types["GenerateServiceIdentityRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GenerateServiceIdentityRequestOut"])
    types["ServiceAccountIn"] = t.struct(
        {"email": t.string().optional(), "scope": t.array(t.string()).optional()}
    ).named(renames["ServiceAccountIn"])
    types["ServiceAccountOut"] = t.struct(
        {
            "email": t.string().optional(),
            "scope": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceAccountOut"])
    types["OperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
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
    types["StartNodeRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["StartNodeRequestIn"]
    )
    types["StartNodeRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StartNodeRequestOut"])
    types["StopNodeRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["StopNodeRequestIn"]
    )
    types["StopNodeRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StopNodeRequestOut"])
    types["AcceleratorTypeIn"] = t.struct(
        {
            "name": t.string().optional(),
            "acceleratorConfigs": t.array(
                t.proxy(renames["AcceleratorConfigIn"])
            ).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["AcceleratorTypeIn"])
    types["AcceleratorTypeOut"] = t.struct(
        {
            "name": t.string().optional(),
            "acceleratorConfigs": t.array(
                t.proxy(renames["AcceleratorConfigOut"])
            ).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AcceleratorTypeOut"])
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
    types["StatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["ServiceIdentityIn"] = t.struct({"email": t.string().optional()}).named(
        renames["ServiceIdentityIn"]
    )
    types["ServiceIdentityOut"] = t.struct(
        {
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceIdentityOut"])
    types["NetworkEndpointIn"] = t.struct(
        {
            "accessConfig": t.proxy(renames["AccessConfigIn"]).optional(),
            "port": t.integer().optional(),
            "ipAddress": t.string().optional(),
        }
    ).named(renames["NetworkEndpointIn"])
    types["NetworkEndpointOut"] = t.struct(
        {
            "accessConfig": t.proxy(renames["AccessConfigOut"]).optional(),
            "port": t.integer().optional(),
            "ipAddress": t.string().optional(),
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
    functions["projectsLocationsRuntimeVersionsGet"] = tpu.get(
        "v2/{parent}/runtimeVersions",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
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
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListRuntimeVersionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = tpu.get(
        "v2/{name}/operations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
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
    functions["projectsLocationsNodesPatch"] = tpu.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["NodeOut"]),
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
    functions["projectsLocationsNodesStop"] = tpu.get(
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
    functions["projectsLocationsNodesDelete"] = tpu.get(
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
    functions["projectsLocationsAcceleratorTypesGet"] = tpu.get(
        "v2/{parent}/acceleratorTypes",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
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
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAcceleratorTypesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="tpu", renames=renames, types=Box(types), functions=Box(functions)
    )
