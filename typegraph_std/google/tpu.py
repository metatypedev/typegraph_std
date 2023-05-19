from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_tpu() -> Import:
    tpu = HTTPRuntime("https://tpu.googleapis.com/")

    renames = {
        "ErrorResponse": "_tpu_1_ErrorResponse",
        "StatusIn": "_tpu_2_StatusIn",
        "StatusOut": "_tpu_3_StatusOut",
        "GenerateServiceIdentityRequestIn": "_tpu_4_GenerateServiceIdentityRequestIn",
        "GenerateServiceIdentityRequestOut": "_tpu_5_GenerateServiceIdentityRequestOut",
        "GetGuestAttributesResponseIn": "_tpu_6_GetGuestAttributesResponseIn",
        "GetGuestAttributesResponseOut": "_tpu_7_GetGuestAttributesResponseOut",
        "GenerateServiceIdentityResponseIn": "_tpu_8_GenerateServiceIdentityResponseIn",
        "GenerateServiceIdentityResponseOut": "_tpu_9_GenerateServiceIdentityResponseOut",
        "EmptyIn": "_tpu_10_EmptyIn",
        "EmptyOut": "_tpu_11_EmptyOut",
        "ListLocationsResponseIn": "_tpu_12_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_tpu_13_ListLocationsResponseOut",
        "RuntimeVersionIn": "_tpu_14_RuntimeVersionIn",
        "RuntimeVersionOut": "_tpu_15_RuntimeVersionOut",
        "AttachedDiskIn": "_tpu_16_AttachedDiskIn",
        "AttachedDiskOut": "_tpu_17_AttachedDiskOut",
        "LocationIn": "_tpu_18_LocationIn",
        "LocationOut": "_tpu_19_LocationOut",
        "AcceleratorConfigIn": "_tpu_20_AcceleratorConfigIn",
        "AcceleratorConfigOut": "_tpu_21_AcceleratorConfigOut",
        "SymptomIn": "_tpu_22_SymptomIn",
        "SymptomOut": "_tpu_23_SymptomOut",
        "NodeIn": "_tpu_24_NodeIn",
        "NodeOut": "_tpu_25_NodeOut",
        "ServiceIdentityIn": "_tpu_26_ServiceIdentityIn",
        "ServiceIdentityOut": "_tpu_27_ServiceIdentityOut",
        "ListAcceleratorTypesResponseIn": "_tpu_28_ListAcceleratorTypesResponseIn",
        "ListAcceleratorTypesResponseOut": "_tpu_29_ListAcceleratorTypesResponseOut",
        "ShieldedInstanceConfigIn": "_tpu_30_ShieldedInstanceConfigIn",
        "ShieldedInstanceConfigOut": "_tpu_31_ShieldedInstanceConfigOut",
        "ListRuntimeVersionsResponseIn": "_tpu_32_ListRuntimeVersionsResponseIn",
        "ListRuntimeVersionsResponseOut": "_tpu_33_ListRuntimeVersionsResponseOut",
        "ListOperationsResponseIn": "_tpu_34_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_tpu_35_ListOperationsResponseOut",
        "GetGuestAttributesRequestIn": "_tpu_36_GetGuestAttributesRequestIn",
        "GetGuestAttributesRequestOut": "_tpu_37_GetGuestAttributesRequestOut",
        "OperationIn": "_tpu_38_OperationIn",
        "OperationOut": "_tpu_39_OperationOut",
        "GuestAttributesIn": "_tpu_40_GuestAttributesIn",
        "GuestAttributesOut": "_tpu_41_GuestAttributesOut",
        "AcceleratorTypeIn": "_tpu_42_AcceleratorTypeIn",
        "AcceleratorTypeOut": "_tpu_43_AcceleratorTypeOut",
        "NetworkConfigIn": "_tpu_44_NetworkConfigIn",
        "NetworkConfigOut": "_tpu_45_NetworkConfigOut",
        "OperationMetadataIn": "_tpu_46_OperationMetadataIn",
        "OperationMetadataOut": "_tpu_47_OperationMetadataOut",
        "GuestAttributesEntryIn": "_tpu_48_GuestAttributesEntryIn",
        "GuestAttributesEntryOut": "_tpu_49_GuestAttributesEntryOut",
        "ListNodesResponseIn": "_tpu_50_ListNodesResponseIn",
        "ListNodesResponseOut": "_tpu_51_ListNodesResponseOut",
        "NetworkEndpointIn": "_tpu_52_NetworkEndpointIn",
        "NetworkEndpointOut": "_tpu_53_NetworkEndpointOut",
        "ServiceAccountIn": "_tpu_54_ServiceAccountIn",
        "ServiceAccountOut": "_tpu_55_ServiceAccountOut",
        "AccessConfigIn": "_tpu_56_AccessConfigIn",
        "AccessConfigOut": "_tpu_57_AccessConfigOut",
        "StartNodeRequestIn": "_tpu_58_StartNodeRequestIn",
        "StartNodeRequestOut": "_tpu_59_StartNodeRequestOut",
        "GuestAttributesValueIn": "_tpu_60_GuestAttributesValueIn",
        "GuestAttributesValueOut": "_tpu_61_GuestAttributesValueOut",
        "StopNodeRequestIn": "_tpu_62_StopNodeRequestIn",
        "StopNodeRequestOut": "_tpu_63_StopNodeRequestOut",
        "SchedulingConfigIn": "_tpu_64_SchedulingConfigIn",
        "SchedulingConfigOut": "_tpu_65_SchedulingConfigOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["GenerateServiceIdentityRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GenerateServiceIdentityRequestIn"])
    types["GenerateServiceIdentityRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GenerateServiceIdentityRequestOut"])
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
    types["GenerateServiceIdentityResponseIn"] = t.struct(
        {"identity": t.proxy(renames["ServiceIdentityIn"]).optional()}
    ).named(renames["GenerateServiceIdentityResponseIn"])
    types["GenerateServiceIdentityResponseOut"] = t.struct(
        {
            "identity": t.proxy(renames["ServiceIdentityOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateServiceIdentityResponseOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["LocationIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["AcceleratorConfigIn"] = t.struct(
        {"type": t.string(), "topology": t.string()}
    ).named(renames["AcceleratorConfigIn"])
    types["AcceleratorConfigOut"] = t.struct(
        {
            "type": t.string(),
            "topology": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AcceleratorConfigOut"])
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
    types["NodeIn"] = t.struct(
        {
            "networkConfig": t.proxy(renames["NetworkConfigIn"]).optional(),
            "serviceAccount": t.proxy(renames["ServiceAccountIn"]).optional(),
            "acceleratorType": t.string(),
            "runtimeVersion": t.string(),
            "shieldedInstanceConfig": t.proxy(
                renames["ShieldedInstanceConfigIn"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "health": t.string().optional(),
            "cidrBlock": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "schedulingConfig": t.proxy(renames["SchedulingConfigIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "acceleratorConfig": t.proxy(renames["AcceleratorConfigIn"]).optional(),
            "dataDisks": t.array(t.proxy(renames["AttachedDiskIn"])).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["NodeIn"])
    types["NodeOut"] = t.struct(
        {
            "networkConfig": t.proxy(renames["NetworkConfigOut"]).optional(),
            "serviceAccount": t.proxy(renames["ServiceAccountOut"]).optional(),
            "acceleratorType": t.string(),
            "apiVersion": t.string().optional(),
            "runtimeVersion": t.string(),
            "shieldedInstanceConfig": t.proxy(
                renames["ShieldedInstanceConfigOut"]
            ).optional(),
            "networkEndpoints": t.array(
                t.proxy(renames["NetworkEndpointOut"])
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "health": t.string().optional(),
            "cidrBlock": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "healthDescription": t.string().optional(),
            "symptoms": t.array(t.proxy(renames["SymptomOut"])).optional(),
            "createTime": t.string().optional(),
            "schedulingConfig": t.proxy(renames["SchedulingConfigOut"]).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "acceleratorConfig": t.proxy(renames["AcceleratorConfigOut"]).optional(),
            "state": t.string().optional(),
            "dataDisks": t.array(t.proxy(renames["AttachedDiskOut"])).optional(),
            "description": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeOut"])
    types["ServiceIdentityIn"] = t.struct({"email": t.string().optional()}).named(
        renames["ServiceIdentityIn"]
    )
    types["ServiceIdentityOut"] = t.struct(
        {
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceIdentityOut"])
    types["ListAcceleratorTypesResponseIn"] = t.struct(
        {
            "acceleratorTypes": t.array(
                t.proxy(renames["AcceleratorTypeIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListAcceleratorTypesResponseIn"])
    types["ListAcceleratorTypesResponseOut"] = t.struct(
        {
            "acceleratorTypes": t.array(
                t.proxy(renames["AcceleratorTypeOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAcceleratorTypesResponseOut"])
    types["ShieldedInstanceConfigIn"] = t.struct(
        {"enableSecureBoot": t.boolean().optional()}
    ).named(renames["ShieldedInstanceConfigIn"])
    types["ShieldedInstanceConfigOut"] = t.struct(
        {
            "enableSecureBoot": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShieldedInstanceConfigOut"])
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
    types["OperationIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
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
    types["NetworkConfigIn"] = t.struct(
        {
            "enableExternalIps": t.boolean().optional(),
            "network": t.string().optional(),
            "subnetwork": t.string().optional(),
            "canIpForward": t.boolean().optional(),
        }
    ).named(renames["NetworkConfigIn"])
    types["NetworkConfigOut"] = t.struct(
        {
            "enableExternalIps": t.boolean().optional(),
            "network": t.string().optional(),
            "subnetwork": t.string().optional(),
            "canIpForward": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkConfigOut"])
    types["OperationMetadataIn"] = t.struct(
        {
            "apiVersion": t.string().optional(),
            "statusDetail": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "target": t.string().optional(),
            "createTime": t.string().optional(),
            "endTime": t.string().optional(),
            "verb": t.string().optional(),
        }
    ).named(renames["OperationMetadataIn"])
    types["OperationMetadataOut"] = t.struct(
        {
            "apiVersion": t.string().optional(),
            "statusDetail": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "target": t.string().optional(),
            "createTime": t.string().optional(),
            "endTime": t.string().optional(),
            "verb": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["GuestAttributesEntryIn"] = t.struct(
        {
            "namespace": t.string().optional(),
            "key": t.string().optional(),
            "value": t.string().optional(),
        }
    ).named(renames["GuestAttributesEntryIn"])
    types["GuestAttributesEntryOut"] = t.struct(
        {
            "namespace": t.string().optional(),
            "key": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GuestAttributesEntryOut"])
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
    types["NetworkEndpointIn"] = t.struct(
        {
            "port": t.integer().optional(),
            "accessConfig": t.proxy(renames["AccessConfigIn"]).optional(),
            "ipAddress": t.string().optional(),
        }
    ).named(renames["NetworkEndpointIn"])
    types["NetworkEndpointOut"] = t.struct(
        {
            "port": t.integer().optional(),
            "accessConfig": t.proxy(renames["AccessConfigOut"]).optional(),
            "ipAddress": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkEndpointOut"])
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
    types["AccessConfigIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AccessConfigIn"]
    )
    types["AccessConfigOut"] = t.struct(
        {
            "externalIp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccessConfigOut"])
    types["StartNodeRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["StartNodeRequestIn"]
    )
    types["StartNodeRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StartNodeRequestOut"])
    types["GuestAttributesValueIn"] = t.struct(
        {"items": t.array(t.proxy(renames["GuestAttributesEntryIn"])).optional()}
    ).named(renames["GuestAttributesValueIn"])
    types["GuestAttributesValueOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["GuestAttributesEntryOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GuestAttributesValueOut"])
    types["StopNodeRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["StopNodeRequestIn"]
    )
    types["StopNodeRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StopNodeRequestOut"])
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

    functions = {}
    functions["projectsLocationsList"] = tpu.post(
        "v2/{parent}:generateServiceIdentity",
        t.struct(
            {
                "parent": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GenerateServiceIdentityResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = tpu.post(
        "v2/{parent}:generateServiceIdentity",
        t.struct(
            {
                "parent": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GenerateServiceIdentityResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGenerateServiceIdentity"] = tpu.post(
        "v2/{parent}:generateServiceIdentity",
        t.struct(
            {
                "parent": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GenerateServiceIdentityResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAcceleratorTypesList"] = tpu.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["AcceleratorTypeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAcceleratorTypesGet"] = tpu.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["AcceleratorTypeOut"]),
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
    functions["projectsLocationsOperationsCancel"] = tpu.get(
        "v2/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = tpu.get(
        "v2/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = tpu.get(
        "v2/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = tpu.get(
        "v2/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNodesGet"] = tpu.patch(
        "v2/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "networkConfig": t.proxy(renames["NetworkConfigIn"]).optional(),
                "serviceAccount": t.proxy(renames["ServiceAccountIn"]).optional(),
                "acceleratorType": t.string(),
                "runtimeVersion": t.string(),
                "shieldedInstanceConfig": t.proxy(
                    renames["ShieldedInstanceConfigIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "health": t.string().optional(),
                "cidrBlock": t.string().optional(),
                "tags": t.array(t.string()).optional(),
                "schedulingConfig": t.proxy(renames["SchedulingConfigIn"]).optional(),
                "metadata": t.struct({"_": t.string().optional()}).optional(),
                "acceleratorConfig": t.proxy(renames["AcceleratorConfigIn"]).optional(),
                "dataDisks": t.array(t.proxy(renames["AttachedDiskIn"])).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNodesList"] = tpu.patch(
        "v2/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "networkConfig": t.proxy(renames["NetworkConfigIn"]).optional(),
                "serviceAccount": t.proxy(renames["ServiceAccountIn"]).optional(),
                "acceleratorType": t.string(),
                "runtimeVersion": t.string(),
                "shieldedInstanceConfig": t.proxy(
                    renames["ShieldedInstanceConfigIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "health": t.string().optional(),
                "cidrBlock": t.string().optional(),
                "tags": t.array(t.string()).optional(),
                "schedulingConfig": t.proxy(renames["SchedulingConfigIn"]).optional(),
                "metadata": t.struct({"_": t.string().optional()}).optional(),
                "acceleratorConfig": t.proxy(renames["AcceleratorConfigIn"]).optional(),
                "dataDisks": t.array(t.proxy(renames["AttachedDiskIn"])).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNodesDelete"] = tpu.patch(
        "v2/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "networkConfig": t.proxy(renames["NetworkConfigIn"]).optional(),
                "serviceAccount": t.proxy(renames["ServiceAccountIn"]).optional(),
                "acceleratorType": t.string(),
                "runtimeVersion": t.string(),
                "shieldedInstanceConfig": t.proxy(
                    renames["ShieldedInstanceConfigIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "health": t.string().optional(),
                "cidrBlock": t.string().optional(),
                "tags": t.array(t.string()).optional(),
                "schedulingConfig": t.proxy(renames["SchedulingConfigIn"]).optional(),
                "metadata": t.struct({"_": t.string().optional()}).optional(),
                "acceleratorConfig": t.proxy(renames["AcceleratorConfigIn"]).optional(),
                "dataDisks": t.array(t.proxy(renames["AttachedDiskIn"])).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNodesCreate"] = tpu.patch(
        "v2/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "networkConfig": t.proxy(renames["NetworkConfigIn"]).optional(),
                "serviceAccount": t.proxy(renames["ServiceAccountIn"]).optional(),
                "acceleratorType": t.string(),
                "runtimeVersion": t.string(),
                "shieldedInstanceConfig": t.proxy(
                    renames["ShieldedInstanceConfigIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "health": t.string().optional(),
                "cidrBlock": t.string().optional(),
                "tags": t.array(t.string()).optional(),
                "schedulingConfig": t.proxy(renames["SchedulingConfigIn"]).optional(),
                "metadata": t.struct({"_": t.string().optional()}).optional(),
                "acceleratorConfig": t.proxy(renames["AcceleratorConfigIn"]).optional(),
                "dataDisks": t.array(t.proxy(renames["AttachedDiskIn"])).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNodesStart"] = tpu.patch(
        "v2/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "networkConfig": t.proxy(renames["NetworkConfigIn"]).optional(),
                "serviceAccount": t.proxy(renames["ServiceAccountIn"]).optional(),
                "acceleratorType": t.string(),
                "runtimeVersion": t.string(),
                "shieldedInstanceConfig": t.proxy(
                    renames["ShieldedInstanceConfigIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "health": t.string().optional(),
                "cidrBlock": t.string().optional(),
                "tags": t.array(t.string()).optional(),
                "schedulingConfig": t.proxy(renames["SchedulingConfigIn"]).optional(),
                "metadata": t.struct({"_": t.string().optional()}).optional(),
                "acceleratorConfig": t.proxy(renames["AcceleratorConfigIn"]).optional(),
                "dataDisks": t.array(t.proxy(renames["AttachedDiskIn"])).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNodesStop"] = tpu.patch(
        "v2/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "networkConfig": t.proxy(renames["NetworkConfigIn"]).optional(),
                "serviceAccount": t.proxy(renames["ServiceAccountIn"]).optional(),
                "acceleratorType": t.string(),
                "runtimeVersion": t.string(),
                "shieldedInstanceConfig": t.proxy(
                    renames["ShieldedInstanceConfigIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "health": t.string().optional(),
                "cidrBlock": t.string().optional(),
                "tags": t.array(t.string()).optional(),
                "schedulingConfig": t.proxy(renames["SchedulingConfigIn"]).optional(),
                "metadata": t.struct({"_": t.string().optional()}).optional(),
                "acceleratorConfig": t.proxy(renames["AcceleratorConfigIn"]).optional(),
                "dataDisks": t.array(t.proxy(renames["AttachedDiskIn"])).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNodesGetGuestAttributes"] = tpu.patch(
        "v2/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "networkConfig": t.proxy(renames["NetworkConfigIn"]).optional(),
                "serviceAccount": t.proxy(renames["ServiceAccountIn"]).optional(),
                "acceleratorType": t.string(),
                "runtimeVersion": t.string(),
                "shieldedInstanceConfig": t.proxy(
                    renames["ShieldedInstanceConfigIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "health": t.string().optional(),
                "cidrBlock": t.string().optional(),
                "tags": t.array(t.string()).optional(),
                "schedulingConfig": t.proxy(renames["SchedulingConfigIn"]).optional(),
                "metadata": t.struct({"_": t.string().optional()}).optional(),
                "acceleratorConfig": t.proxy(renames["AcceleratorConfigIn"]).optional(),
                "dataDisks": t.array(t.proxy(renames["AttachedDiskIn"])).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNodesPatch"] = tpu.patch(
        "v2/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "networkConfig": t.proxy(renames["NetworkConfigIn"]).optional(),
                "serviceAccount": t.proxy(renames["ServiceAccountIn"]).optional(),
                "acceleratorType": t.string(),
                "runtimeVersion": t.string(),
                "shieldedInstanceConfig": t.proxy(
                    renames["ShieldedInstanceConfigIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "health": t.string().optional(),
                "cidrBlock": t.string().optional(),
                "tags": t.array(t.string()).optional(),
                "schedulingConfig": t.proxy(renames["SchedulingConfigIn"]).optional(),
                "metadata": t.struct({"_": t.string().optional()}).optional(),
                "acceleratorConfig": t.proxy(renames["AcceleratorConfigIn"]).optional(),
                "dataDisks": t.array(t.proxy(renames["AttachedDiskIn"])).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="tpu", renames=renames, types=Box(types), functions=Box(functions)
    )
